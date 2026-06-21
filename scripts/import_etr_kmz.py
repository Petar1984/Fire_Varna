#!/usr/bin/env python3
"""H2 KMZ adapter: dry-run consolidation report for the 2026-06-17 ETR batch.

Per docs/plans/h2_kmz_adapter_plan.md (signed E0, Petar 2026-06-21). This adapter
parses the four ArcGIS-exported ETR KMZ files in data/hydrants_17_06_26/, collapses
near-duplicate source points, matches them against data/hydrants.json through the
H1 shared core, and emits a DRY-RUN consolidation report for review.

It is dry-run ONLY by design:
  * there is no --apply flag (H4 owns signed apply);
  * it never writes data/hydrants.json or data/hydrants_provenance.json;
  * it writes only the requested JSON + Markdown report artifacts.

It reuses the H1 primitives in scripts/lib/hydrant_core.py (load_json, distance_m,
match_point, coords_in_bbox, CoordIdRegistry, canonical_coord_id, mojibake_scan).
It deliberately does NOT call apply_new_hydrant(): that handler is field-report
specific (origin="field_report", existence_status, report_id, reporter fields) and
the ETR KMZ carry none of those — only coordinates.

Standard library only (zipfile, xml.etree.ElementTree, argparse, json, hashlib,
dataclasses); no third-party KML dependency, matching the AGENTS dependency gate.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

# Make scripts/lib importable whether run directly or imported by the test suite
# from any working directory (mirrors apply_approved_reports.py).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import hydrant_core as core  # noqa: E402


# ---------- Thresholds (from the signed E0 + the H2 plan) ----------

# Strict intra-batch dedup: KMZ source points closer than this collapse into one
# source cluster before any matching (plan §3).
INTRA_BATCH_DEDUP_STRICT_LT_M = 2.0
# Spatial decision bands reuse the signed H1 thresholds (Petar 2026-06-21).
RM_UPDATE_LTE_M = core.DEFAULT_RM_M  # 5.0
RF_FLAG_LTE_M = core.DEFAULT_RF_M    # 20.0
# Strict ADD-candidate clustering: collapse new points closer than Rm into one
# ADD preview so the incoming batch does not seed its own duplicates (plan §7).
ADD_CANDIDATE_CLUSTER_STRICT_LT_M = core.DEFAULT_RM_M  # 5.0

SCHEMA_VERSION = "h2_kmz_dry_run_v1"

# E0 raw-independent baseline (SIGNED Petar 2026-06-21) for reconciliation. E0
# classified every raw placemark independently; H2 first collapses duplicates,
# so H2 counts are expected at or below these, with the gap explained by dedup.
E0_RAW_POINTS = 4860
E0_UPDATED = 3237
E0_FLAGGED = 318
E0_ADDED = 1305

# The exact four known ETR KMZ basenames, in explicit canonical order. H2 requires
# exactly this set (Decision Ledger: no --allow-extra in H2). Origin is etr_<muni>.
KNOWN_KMZ: list[tuple[str, str]] = [
    ("Пожарни хидранти ЕТР Варна.kmz", "varna"),
    ("Пожарни хидранти ЕТР Провадия.kmz", "provadia"),
    ("Пожарни хидранти ЕТР Долни Чифлик.kmz", "dolni_chiflik"),
    ("Пожарни хидранти ЕТР Девня.kmz", "devnya"),
]

DEFAULT_SOURCE_DIR = "data/hydrants_17_06_26"
DEFAULT_INPUT = "data/hydrants.json"
DEFAULT_PROVENANCE = "data/hydrants_provenance.json"
DEFAULT_JSON_REPORT = "docs/audits/h2_kmz_consolidation_dry_run.json"
DEFAULT_MD_REPORT = "docs/audits/h2_kmz_consolidation_dry_run.md"


class KmzParseError(Exception):
    """A KMZ archive is malformed for H2 purposes (no/ambiguous inner KML, or an
    unexpected source-dir file set). Fail loud; never silently skip a source."""


def origin_for_municipality(municipality: str) -> str:
    return f"etr_{municipality}"


# ---------- Source model ----------

@dataclass(frozen=True)
class KmzSourcePoint:
    """One raw KML Placemark/Point. `name` is raw context only — KMZ names are
    noisy/blank ArcGIS artifacts and must never be parsed into ids/type/status."""

    source_uid: str
    source_file: str          # basename
    source_sha256: str
    municipality: str
    origin: str
    placemark_index: int      # 0-based index of the Placemark within its file
    name: str
    lon: float
    lat: float
    alt: float | None


@dataclass
class KmzFile:
    path: str                 # forward-slash relative path for reports
    basename: str
    municipality: str
    origin: str
    sha256: str
    kml_entry: str
    placemarks: int
    points: int               # parseable Point/coordinates count
    extended_data: int        # counted but never read (KMZ have zero)
    schema_data: int
    missing_coords: int       # placemarks with no/unparseable coordinates
    source_points: list[KmzSourcePoint] = field(default_factory=list)


@dataclass
class SourceComponent:
    """A <2 m connected component of source points collapsed into one cluster."""

    representative: KmzSourcePoint
    members: list[KmzSourcePoint]
    member_uids: list[str]
    member_names: list[str]
    cross_file: bool


# ---------- KMZ parsing ----------

def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def _parse_coord_text(text: str):
    """Parse a KML `coordinates` value `lon,lat[,alt]` -> (lon, lat, alt|None).

    KML order is lon,lat,alt. Returns None when it cannot be parsed (counted as a
    missing coordinate by the caller)."""
    if not text:
        return None
    parts = text.strip().split(",")
    if len(parts) < 2:
        return None
    try:
        lon = float(parts[0])
        lat = float(parts[1])
    except ValueError:
        return None
    alt = None
    if len(parts) >= 3 and parts[2].strip() != "":
        try:
            alt = float(parts[2])
        except ValueError:
            alt = None
    return lon, lat, alt


def source_uid_for(origin: str, lon: float, lat: float) -> str:
    """Coordinate-derived source alias: etr_<municipality>:<lon8>,<lat8>.

    KMZ carry no source ids, so the alias is deterministic from coordinates and
    auditable (Decision Ledger; confirm exact string before H4 apply)."""
    return f"{origin}:{lon:.8f},{lat:.8f}"


def parse_kmz(path: str, municipality: str, *, report_path: str | None = None) -> KmzFile:
    """Parse one ETR KMZ into a KmzFile. Requires exactly one inner KML entry.

    report_path overrides the forward-slash path recorded in the report (defaults
    to the on-disk path)."""
    origin = origin_for_municipality(municipality)
    basename = os.path.basename(path)
    sha = sha256_file(path)
    with zipfile.ZipFile(path) as z:
        kml_entries = [n for n in z.namelist() if n.lower().endswith(".kml")]
        if len(kml_entries) != 1:
            raise KmzParseError(
                f"{basename}: expected exactly one inner KML entry, "
                f"found {kml_entries!r}")
        kml_entry = kml_entries[0]
        with z.open(kml_entry) as f:
            xml_bytes = f.read()

    root = ET.fromstring(xml_bytes)
    placemarks = root.findall(".//{*}Placemark")
    extended_data = len(root.findall(".//{*}ExtendedData"))
    schema_data = len(root.findall(".//{*}SchemaData"))

    points: list[KmzSourcePoint] = []
    missing_coords = 0
    for idx, pm in enumerate(placemarks):
        coord_el = pm.find(".//{*}Point/{*}coordinates")
        parsed = _parse_coord_text(coord_el.text) if coord_el is not None else None
        if parsed is None:
            missing_coords += 1
            continue
        lon, lat, alt = parsed
        name_el = pm.find("{*}name")
        name = name_el.text if (name_el is not None and name_el.text is not None) else ""
        points.append(KmzSourcePoint(
            source_uid=source_uid_for(origin, lon, lat),
            source_file=basename,
            source_sha256=sha,
            municipality=municipality,
            origin=origin,
            placemark_index=idx,
            name=name,
            lon=lon, lat=lat, alt=alt,
        ))

    rel = report_path if report_path is not None else path.replace(os.sep, "/")
    return KmzFile(
        path=rel, basename=basename, municipality=municipality, origin=origin,
        sha256=sha, kml_entry=kml_entry, placemarks=len(placemarks),
        points=len(points), extended_data=extended_data, schema_data=schema_data,
        missing_coords=missing_coords, source_points=points,
    )


def load_source_dir(source_dir: str) -> list[KmzFile]:
    """Parse exactly the four known ETR KMZ files from source_dir, in canonical
    order. Fail loud if the .kmz set does not match (no --allow-extra in H2)."""
    present = sorted(
        n for n in os.listdir(source_dir) if n.lower().endswith(".kmz"))
    expected = sorted(b for b, _m in KNOWN_KMZ)
    if present != expected:
        raise KmzParseError(
            f"source dir {source_dir}: KMZ set mismatch.\n"
            f"  expected: {expected}\n"
            f"  found:    {present}\n"
            "H2 requires exactly the four known ETR KMZ files; an --allow-extra "
            "option is not approved for H2.")
    files: list[KmzFile] = []
    for basename, municipality in KNOWN_KMZ:  # canonical order, not directory order
        on_disk = os.path.join(source_dir, basename)
        rel = f"{source_dir}/{basename}".replace(os.sep, "/")
        files.append(parse_kmz(on_disk, municipality, report_path=rel))
    return files


# ---------- Spatial clustering ----------

def _connected_components(points: list[KmzSourcePoint], threshold_m: float) -> list[list[int]]:
    """Union-find connected components where any two points are strictly closer
    than threshold_m. Returns lists of indices into `points`, each in ascending
    index order (so the earliest member, by the caller's pre-sort, is first).

    O(n^2) pairwise — the H1 plan accepts the linear approach at KMZ volume. It is
    exact: connectivity is transitive (A-B and B-C under the threshold yield one
    component) which a nearest-pair-only pass would miss."""
    n = len(points)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            # Keep the smaller index as root for deterministic structure.
            parent[max(ra, rb)] = min(ra, rb)

    coords = [(p.lon, p.lat) for p in points]
    for i in range(n):
        ci = coords[i]
        for j in range(i + 1, n):
            if core.distance_m(ci, coords[j]) < threshold_m:
                union(i, j)

    groups: dict[int, list[int]] = {}
    for i in range(n):
        groups.setdefault(find(i), []).append(i)
    # Return components ordered by their earliest member for determinism.
    return [groups[r] for r in sorted(groups, key=lambda r: groups[r][0])]


def dedup_source_points(files: list[KmzFile]):
    """Flatten valid (in-bbox) source points, sort by (file order, placemark
    index), and collapse <2 m connected components into SourceComponents.

    Returns (components, invalid_by_file) where invalid_by_file maps basename ->
    count of out-of-bbox points excluded from matching (plan §2, §3, Test 5)."""
    file_order = {f.basename: i for i, f in enumerate(files)}

    valid: list[KmzSourcePoint] = []
    invalid_by_file: dict[str, int] = {f.basename: 0 for f in files}
    for f in files:
        for p in f.source_points:
            if core.coords_in_bbox([p.lon, p.lat]):
                valid.append(p)
            else:
                invalid_by_file[p.source_file] += 1

    valid.sort(key=lambda p: (file_order[p.source_file], p.placemark_index))

    components: list[SourceComponent] = []
    for idx_group in _connected_components(valid, INTRA_BATCH_DEDUP_STRICT_LT_M):
        members = [valid[i] for i in idx_group]
        # Earliest by (file order, placemark index) is the representative.
        members.sort(key=lambda p: (file_order[p.source_file], p.placemark_index))
        rep = members[0]
        cross_file = len({m.source_file for m in members}) > 1
        components.append(SourceComponent(
            representative=rep,
            members=members,
            member_uids=[m.source_uid for m in members],
            member_names=[m.name for m in members],
            cross_file=cross_file,
        ))
    return components, invalid_by_file


# ---------- Match classification ----------

@dataclass
class ClassifiedComponent:
    component: SourceComponent
    decision: str
    nearest_record: dict | None
    distance_m: float | None


def classify_components(components: list[SourceComponent], records: list[dict]) -> list[ClassifiedComponent]:
    """Match each deduped representative against existing records via the H1
    matcher (Rm=5, Rf=20), preserving H1 boundary + tie-break semantics."""
    out: list[ClassifiedComponent] = []
    for comp in components:
        rep = comp.representative
        m = core.match_point((rep.lon, rep.lat), records,
                             rm_m=RM_UPDATE_LTE_M, rf_m=RF_FLAG_LTE_M)
        out.append(ClassifiedComponent(
            component=comp, decision=m.decision,
            nearest_record=m.nearest_record, distance_m=m.distance_m))
    return out


# ---------- Previews ----------

def build_update_preview(cc: ClassifiedComponent, *, timestamp: str) -> dict:
    """Preview an UPDATE: append ETR aliases to legacy_ids + a provenance ref.

    No coords/origin/type/address/status change — KMZ confirm existence only
    (plan §5, Test 9). Returns an in-memory preview; nothing is written."""
    rec = cc.nearest_record
    comp = cc.component
    existing = list(rec.get("legacy_ids", []))
    added = [uid for uid in comp.member_uids if uid not in existing]
    new_legacy = existing + added  # existing order preserved, ETR aliases appended

    if added:
        manual_field, old_value, new_value = "legacy_ids", existing, new_legacy
    else:
        manual_field, old_value, new_value = "noop", None, None

    provenance_ref = {
        "old_id": rec["id"],
        "old_coord": list(rec["coords"]),
        "manual_field": manual_field,
        "old_value": old_value,
        "new_value": new_value,
        "attribution": "Dry-run H2 KMZ import: existence confirmed by ETR",
        "timestamp": timestamp,
        "merge_action": "kmz_etr_update_preview",
        "source_origin": comp.representative.origin,
        "source_file": comp.representative.source_file,
        "source_uids": added,
        "distance_m": round(cc.distance_m, 3),
        "conflict_flags": [],
    }
    return {
        "target_id": rec["id"],
        "distance_m": round(cc.distance_m, 3),
        "source_file": comp.representative.source_file,
        "municipality": comp.representative.municipality,
        "old_legacy_ids": existing,
        "new_legacy_ids": new_legacy,
        "added_aliases": added,
        "provenance_ref": provenance_ref,
    }


def build_flag_row(cc: ClassifiedComponent) -> dict:
    """Preview a FLAG: a manual-review row. Mutates nothing (plan §6, Test 10)."""
    rep = cc.component.representative
    rec = cc.nearest_record
    return {
        "source_uid": rep.source_uid,
        "source_file": rep.source_file,
        "municipality": rep.municipality,
        "origin": rep.origin,
        "placemark_index": rep.placemark_index,
        "name": rep.name,
        "lon": rep.lon,
        "lat": rep.lat,
        "nearest_existing_id": rec["id"],
        "nearest_existing_origin": rec.get("origin"),
        "nearest_existing_lon": rec["coords"][0],
        "nearest_existing_lat": rec["coords"][1],
        "distance_m": round(cc.distance_m, 3),
        "member_count": len(cc.component.members),
        "member_uids": cc.component.member_uids,
        "reason": "spatial_near_match",
    }


def build_add_record(rep: KmzSourcePoint, legacy_ids: list[str], registry) -> dict:
    """Preview an ADD record. Exactly {id, coords, origin, legacy_ids} — no
    type/status/address from H2 (plan §7, Test 11). id uses the H1 coord stub."""
    return {
        "id": registry.id_for_new_record(rep.lon, rep.lat),
        "coords": [rep.lon, rep.lat],
        "origin": rep.origin,
        "legacy_ids": legacy_ids,
    }


def cluster_add_candidates(add_components: list[ClassifiedComponent], *, registry, files):
    """Collapse ADD candidates strictly closer than Rm into one ADD preview each
    (plan §7). Returns a list of add_group dicts, each carrying a 4-field preview
    record plus cluster metadata, sorted deterministically."""
    file_order = {f.basename: i for i, f in enumerate(files)}
    reps = [cc.component.representative for cc in add_components]
    # Sort candidates so the earliest is the cluster representative.
    order = sorted(range(len(add_components)),
                   key=lambda i: (file_order[reps[i].source_file], reps[i].placemark_index))
    ordered = [add_components[i] for i in order]
    ordered_reps = [reps[i] for i in order]

    groups: list[dict] = []
    for idx_group in _connected_components(ordered_reps, ADD_CANDIDATE_CLUSTER_STRICT_LT_M):
        cluster = [ordered[i] for i in idx_group]
        rep = cluster[0].component.representative
        # legacy_ids = every source member uid across the cluster, order-preserved.
        legacy_ids: list[str] = []
        municipalities: set[str] = set()
        source_member_count = 0
        for cc in cluster:
            for uid in cc.component.member_uids:
                if uid not in legacy_ids:
                    legacy_ids.append(uid)
            municipalities.update(m.municipality for m in cc.component.members)
            source_member_count += len(cc.component.members)
        cross_muni = len(municipalities) > 1
        groups.append({
            "record": build_add_record(rep, legacy_ids, registry),
            "representative_uid": rep.source_uid,
            "representative_source_file": rep.source_file,
            "representative_placemark_index": rep.placemark_index,
            "candidate_count": len(cluster),
            "source_member_count": source_member_count,
            "cross_municipality_add_cluster": cross_muni,
            "member_uids": legacy_ids,
        })
    # Deterministic order by representative (file order, placemark index, uid).
    groups.sort(key=lambda g: (file_order[g["representative_source_file"]],
                               g["representative_placemark_index"],
                               g["representative_uid"]))
    return groups


# ---------- Report assembly ----------

_DECISION_ORDER = {core.SpatialDecision.UPDATE: 0,
                   core.SpatialDecision.FLAG: 1,
                   core.SpatialDecision.ADD: 2}


def run_consolidation(files, records, provenance, *, timestamp,
                      input_meta=None, provenance_meta=None, registry=None):
    """Pure in-memory pipeline: dedup -> classify -> previews -> report dict.

    Takes already-parsed KmzFile list + existing records/provenance (read-only).
    Returns (report, previews) where previews holds the in-memory UPDATE previews
    and ADD/FLAG structures used for the mojibake scan and counts. Mutates none of
    its inputs."""
    if registry is None:
        registry = core.CoordIdRegistry()
    file_order = {f.basename: i for i, f in enumerate(files)}

    components, invalid_by_file = dedup_source_points(files)
    classified = classify_components(components, records)

    updates = [cc for cc in classified if cc.decision == core.SpatialDecision.UPDATE]
    flags = [cc for cc in classified if cc.decision == core.SpatialDecision.FLAG]
    add_candidates = [cc for cc in classified if cc.decision == core.SpatialDecision.ADD]

    update_previews = [build_update_preview(cc, timestamp=timestamp) for cc in updates]
    flag_rows = [build_flag_row(cc) for cc in flags]
    flag_rows.sort(key=lambda r: (file_order[r["source_file"]],
                                  r["placemark_index"], r["source_uid"]))
    for i, row in enumerate(flag_rows, start=1):
        row_with_id = {"flag_id": f"FLAG-{i:04d}"}
        row_with_id.update(row)
        flag_rows[i - 1] = row_with_id

    add_groups = cluster_add_candidates(add_candidates, registry=registry, files=files)

    # ----- per-file aggregation -----
    per_file = []
    for f in files:
        reps_here = [cc for cc in classified
                     if cc.component.representative.source_file == f.basename]
        nonrep_here = 0
        for comp in components:
            for m in comp.members:
                if m is not comp.representative and m.source_file == f.basename:
                    nonrep_here += 1
        upd_here = sum(1 for cc in reps_here if cc.decision == core.SpatialDecision.UPDATE)
        flag_here = sum(1 for cc in reps_here if cc.decision == core.SpatialDecision.FLAG)
        addc_here = sum(1 for cc in reps_here if cc.decision == core.SpatialDecision.ADD)
        added_here = sum(1 for g in add_groups
                         if g["representative_source_file"] == f.basename)
        per_file.append({
            "source_file": f.basename,
            "municipality": f.municipality,
            "origin": f.origin,
            "raw_points": f.points,
            "missing_coords": f.missing_coords,
            "invalid_coords": invalid_by_file.get(f.basename, 0),
            "extended_data": f.extended_data,
            "schema_data": f.schema_data,
            "dedup_representatives": len(reps_here),
            "dedup_nonrepresentatives": nonrep_here,
            "updated": upd_here,
            "flagged": flag_here,
            "add_candidates": addc_here,
            "added": added_here,
        })

    # ----- summary -----
    raw_kmz_points = sum(f.points for f in files)
    total_invalid = sum(invalid_by_file.values())
    total_missing = sum(f.missing_coords for f in files)
    deduped = len(components)
    collapsed_2m = sum(len(c.members) - 1 for c in components)
    n_updated = len(updates)
    n_flagged = len(flags)
    n_add_candidates = len(add_candidates)
    n_added = len(add_groups)
    add_collapsed_5m = n_add_candidates - n_added
    record_count = len(records)

    summary = {
        "raw_kmz_points": raw_kmz_points,
        "valid_source_points": raw_kmz_points - total_invalid,
        "invalid_coords": total_invalid,
        "missing_coords": total_missing,
        "deduped_source_points": deduped,
        "intra_batch_duplicates_collapsed": collapsed_2m,
        "updated": n_updated,
        "flagged": n_flagged,
        "add_candidates": n_add_candidates,
        "added": n_added,
        "add_candidates_collapsed": add_collapsed_5m,
        "projected_output_count_if_applied": record_count + n_added,
    }

    # ----- E0 reconciliation -----
    e0_reconciliation = {
        "e0_raw_independent": {
            "raw_points": E0_RAW_POINTS,
            "updated": E0_UPDATED,
            "flagged": E0_FLAGGED,
            "added": E0_ADDED,
        },
        "h2_post_dedup": {
            "deduped_source_points": deduped,
            "updated": n_updated,
            "flagged": n_flagged,
            "added": n_added,
        },
        "deltas": {
            "raw_points": deduped - E0_RAW_POINTS,
            "updated": n_updated - E0_UPDATED,
            "flagged": n_flagged - E0_FLAGGED,
            "added": n_added - E0_ADDED,
        },
        "reduction_attribution": {
            "intra_batch_2m_collapsed": collapsed_2m,
            "add_candidate_5m_collapsed": add_collapsed_5m,
        },
        "explanation": (
            "E0 classified 4,860 raw placemarks independently. H2 first collapses "
            "<2 m source components (intra_batch_2m), then collapses ADD candidates "
            "<5 m (add_candidate_5m), so duplicate source members no longer produce "
            "their own UPDATE/FLAG/ADD rows."),
    }

    inputs = {
        "hydrants_json": input_meta or {
            "path": DEFAULT_INPUT, "sha256": None, "record_count": record_count},
        "provenance_json": provenance_meta or {
            "path": DEFAULT_PROVENANCE, "sha256": None,
            "record_count": len(provenance) if hasattr(provenance, "__len__") else None},
        "kmz_files": [{
            "path": f.path,
            "sha256": f.sha256,
            "municipality": f.municipality,
            "origin": f.origin,
            "kml_entry": f.kml_entry,
            "placemarks": f.placemarks,
            "points": f.points,
            "extended_data": f.extended_data,
            "schema_data": f.schema_data,
            "missing_coords": f.missing_coords,
            "invalid_coords": invalid_by_file.get(f.basename, 0),
        } for f in files],
    }

    cross_file_components = [
        {
            "representative_uid": c.representative.source_uid,
            "member_uids": c.member_uids,
            "member_files": sorted({m.source_file for m in c.members}),
            "member_count": len(c.members),
        }
        for c in components if c.cross_file
    ]
    cross_muni_add = [g for g in add_groups if g["cross_municipality_add_cluster"]]

    report = {
        "schema_version": SCHEMA_VERSION,
        "mode": "dry_run",
        "generated_at": timestamp,
        "thresholds_m": {
            "intra_batch_dedup_strict_lt": INTRA_BATCH_DEDUP_STRICT_LT_M,
            "rm_update_lte": RM_UPDATE_LTE_M,
            "rf_flag_lte": RF_FLAG_LTE_M,
            "add_candidate_cluster_strict_lt": ADD_CANDIDATE_CLUSTER_STRICT_LT_M,
        },
        "inputs": inputs,
        "summary": summary,
        "per_file": per_file,
        "e0_reconciliation": e0_reconciliation,
        "review_notes": {
            "cross_file_dedup_components": cross_file_components,
            "cross_municipality_add_clusters": [
                {
                    "id": g["record"]["id"],
                    "representative_uid": g["representative_uid"],
                    "member_uids": g["member_uids"],
                } for g in cross_muni_add
            ],
        },
        "flags": flag_rows,
        "add_groups": add_groups,
        "update_groups_summary_only": True,
    }

    previews = {
        "update_previews": update_previews,
        "flag_rows": flag_rows,
        "add_groups": add_groups,
    }
    return report, previews


# ---------- Markdown rendering ----------

def _md_table(headers: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def render_markdown(report: dict) -> str:
    s = report["summary"]
    t = report["thresholds_m"]
    inp = report["inputs"]
    e0 = report["e0_reconciliation"]
    lines: list[str] = []

    lines.append("# H2 KMZ Consolidation — Dry-Run Report")
    lines.append("")
    lines.append(f"- Mode: **{report['mode']}** — NO data was mutated.")
    lines.append(f"- Generated at: `{report['generated_at']}`")
    lines.append(f"- Schema: `{report['schema_version']}`")
    lines.append(
        f"- Input `{inp['hydrants_json']['path']}` "
        f"sha256 `{inp['hydrants_json']['sha256']}` "
        f"({inp['hydrants_json']['record_count']} records)")
    lines.append(
        f"- Provenance `{inp['provenance_json']['path']}` "
        f"sha256 `{inp['provenance_json']['sha256']}` "
        f"({inp['provenance_json']['record_count']} records)")
    lines.append(
        f"- Thresholds (m): intra-batch dedup `< {t['intra_batch_dedup_strict_lt']}`, "
        f"UPDATE `<= {t['rm_update_lte']}`, FLAG `(.., {t['rf_flag_lte']}]`, "
        f"ADD cluster `< {t['add_candidate_cluster_strict_lt']}`")
    lines.append("")
    lines.append(
        "> Dry run only; no hydrant/provenance files written. H4 signed apply "
        "required before any change to `data/hydrants.json`.")
    lines.append("")

    # 2. Summary
    lines.append("## Summary")
    lines.append("")
    lines.append(_md_table(
        ["metric", "value"],
        [["raw KMZ points", s["raw_kmz_points"]],
         ["valid source points", s["valid_source_points"]],
         ["invalid (out-of-bbox) coords", s["invalid_coords"]],
         ["missing coords", s["missing_coords"]],
         ["deduped source points", s["deduped_source_points"]],
         ["intra-batch duplicates collapsed (<2 m)", s["intra_batch_duplicates_collapsed"]],
         ["UPDATE", s["updated"]],
         ["FLAG", s["flagged"]],
         ["ADD candidates", s["add_candidates"]],
         ["ADD (after <5 m cluster)", s["added"]],
         ["ADD candidates collapsed (<5 m)", s["add_candidates_collapsed"]],
         ["projected output count if applied", s["projected_output_count_if_applied"]]]))
    lines.append("")

    # 3. Per-file
    lines.append("## Per-file breakdown")
    lines.append("")
    lines.append(_md_table(
        ["source_file", "muni", "raw", "dedup_reps", "dedup_drops",
         "UPDATE", "FLAG", "ADD_cand", "ADD"],
        [[pf["source_file"], pf["municipality"], pf["raw_points"],
          pf["dedup_representatives"], pf["dedup_nonrepresentatives"],
          pf["updated"], pf["flagged"], pf["add_candidates"], pf["added"]]
         for pf in report["per_file"]]))
    lines.append("")

    # 4. E0 reconciliation
    lines.append("## E0 reconciliation")
    lines.append("")
    h2 = e0["h2_post_dedup"]
    raw_e0 = e0["e0_raw_independent"]
    d = e0["deltas"]
    lines.append(_md_table(
        ["metric", "E0 raw independent", "H2 post-dedup", "delta"],
        [["raw / deduped points", raw_e0["raw_points"], h2["deduped_source_points"], d["raw_points"]],
         ["UPDATE", raw_e0["updated"], h2["updated"], d["updated"]],
         ["FLAG", raw_e0["flagged"], h2["flagged"], d["flagged"]],
         ["ADD", raw_e0["added"], h2["added"], d["added"]]]))
    lines.append("")
    ra = e0["reduction_attribution"]
    lines.append(
        f"Reduction attribution: `intra_batch_2m` collapsed "
        f"**{ra['intra_batch_2m_collapsed']}** points; `add_candidate_5m` collapsed "
        f"**{ra['add_candidate_5m_collapsed']}** ADD candidates.")
    lines.append("")
    lines.append(e0["explanation"])
    lines.append("")

    # 7. Review notes (placed before the long FLAG table for visibility)
    rn = report["review_notes"]
    lines.append("## Review notes")
    lines.append("")
    lines.append(
        f"- Cross-file dedup components: **{len(rn['cross_file_dedup_components'])}**")
    lines.append(
        f"- Cross-municipality ADD clusters: **{len(rn['cross_municipality_add_clusters'])}**")
    lines.append("")

    # 6. Full FLAG list
    lines.append(f"## FLAG review list ({len(report['flags'])})")
    lines.append("")
    if report["flags"]:
        lines.append(_md_table(
            ["#", "source_file", "placemark", "source_uid", "lon", "lat",
             "nearest_id", "nearest_origin", "distance_m", "name"],
            [[r["flag_id"], r["source_file"], r["placemark_index"], r["source_uid"],
              r["lon"], r["lat"], r["nearest_existing_id"], r["nearest_existing_origin"],
              r["distance_m"], (r["name"] or "").replace("|", "\\|").replace("\n", " ")]
             for r in report["flags"]]))
    else:
        lines.append("_No FLAG rows._")
    lines.append("")
    return "\n".join(lines) + "\n"


# ---------- CLI ----------

def _atomic_write_text(path: str, text: str) -> None:
    import tempfile
    parent = os.path.dirname(path) or "."
    os.makedirs(parent, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".tmp_", dir=parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        os.replace(tmp, path)
    except Exception:
        try:
            os.remove(tmp)
        except OSError:
            pass
        raise


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source-dir", default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--provenance", default=DEFAULT_PROVENANCE)
    parser.add_argument("--json-report", default=DEFAULT_JSON_REPORT)
    parser.add_argument("--md-report", default=DEFAULT_MD_REPORT)
    parser.add_argument("--timestamp", default=None,
                        help="ISO-8601 timestamp recorded in the report. Defaults "
                             "to current local time.")
    # NOTE: there is deliberately no --apply. H2 is dry-run only; H4 owns apply.
    return parser


def main(argv=None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    args = build_parser().parse_args(argv)
    timestamp = args.timestamp or core.default_timestamp()

    # Dry-run safety: hash the protected files BEFORE doing anything.
    sha_in_before = sha256_file(args.input)
    sha_prov_before = sha256_file(args.provenance)

    records = core.load_json(args.input)
    provenance = core.load_json(args.provenance)
    input_meta = {"path": args.input.replace(os.sep, "/"),
                  "sha256": sha_in_before, "record_count": len(records)}
    provenance_meta = {"path": args.provenance.replace(os.sep, "/"),
                       "sha256": sha_prov_before, "record_count": len(provenance)}

    files = load_source_dir(args.source_dir)
    report, previews = run_consolidation(
        files, records, provenance, timestamp=timestamp,
        input_meta=input_meta, provenance_meta=provenance_meta)

    # Mojibake scan: preview records, preview provenance snippets, full report.
    core.mojibake_scan("add_groups", previews["add_groups"])
    core.mojibake_scan("update_previews", previews["update_previews"])
    core.mojibake_scan("flags", previews["flag_rows"])
    core.mojibake_scan("report", report)

    core.atomic_write_json(args.json_report, report, indent=2)
    _atomic_write_text(args.md_report, render_markdown(report))

    # Dry-run safety: protected files must be byte-identical afterwards.
    sha_in_after = sha256_file(args.input)
    sha_prov_after = sha256_file(args.provenance)
    if sha_in_after != sha_in_before or sha_prov_after != sha_prov_before:
        raise AssertionError(
            "DRY-RUN VIOLATION: protected data file changed during the run.")

    _print_summary(report, args, sha_in_before, sha_prov_before)
    return 0


def _print_summary(report, args, sha_in, sha_prov) -> None:
    s = report["summary"]
    e0 = report["e0_reconciliation"]["deltas"]
    print("H2 KMZ consolidation dry-run summary")
    print(f"  source_dir:        {args.source_dir}")
    print(f"  input:             {args.input} (sha256 {sha_in})")
    print(f"  provenance:        {args.provenance} (sha256 {sha_prov})")
    print(f"  raw_kmz_points:    {s['raw_kmz_points']}")
    print(f"  deduped_points:    {s['deduped_source_points']} "
          f"(collapsed <2 m: {s['intra_batch_duplicates_collapsed']})")
    print(f"  UPDATE:            {s['updated']}  (E0 delta {e0['updated']:+d})")
    print(f"  FLAG:              {s['flagged']}  (E0 delta {e0['flagged']:+d})")
    print(f"  ADD candidates:    {s['add_candidates']}")
    print(f"  ADD (post <5 m):   {s['added']}  (E0 delta {e0['added']:+d}; "
          f"collapsed <5 m: {s['add_candidates_collapsed']})")
    print(f"  projected output:  {s['projected_output_count_if_applied']}")
    print(f"  json report:       {args.json_report}")
    print(f"  md report:         {args.md_report}")
    print()
    print("Dry run only; no hydrant/provenance files written. H4 signed apply required.")


if __name__ == "__main__":
    raise SystemExit(main())
