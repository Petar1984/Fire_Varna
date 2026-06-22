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
    # Collapse duplicate-coordinate source points (same source_uid) so each alias
    # is appended at most once. ArcGIS KMZ exports contain repeated placemarks at
    # identical coordinates; without this an alias could land in legacy_ids 2-3x.
    # Mirrors the ADD path, which already dedupes member uids.
    member_aliases = list(dict.fromkeys(comp.member_uids))
    added = [uid for uid in member_aliases if uid not in existing]
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
        "source_origin": comp.representative.origin,
        "old_legacy_ids": existing,
        "new_legacy_ids": new_legacy,
        "added_aliases": added,
        # Every distinct source alias in this collapsed <2 m component, not just
        # the ones newly appended. H4 apply needs the full set to distinguish a
        # clean noop (all present) from a partial apply (some present, some not).
        "member_aliases": member_aliases,
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


# ---------- H4 signed apply ----------
#
# Per docs/plans/h4_kmz_apply_plan.md (approved, Petar 2026-06-22). Apply is an
# explicit opt-in (--apply); without it the script stays dry-run only. Apply
# mutates only data/hydrants.json, data/hydrants_provenance.json, the FLAG queue,
# and the post-apply report. It applies the confident outcomes:
#   * UPDATE (<= Rm): append ETR aliases to legacy_ids + one provenance ref.
#   * ADD (> Rf): append a {id, coords, origin, legacy_ids} record + provenance.
#   * FLAG ((Rm, Rf]): NOT applied — written to the manual-review queue only.
#
# Idempotency design: classification is computed against the BASE records (those
# whose origin does not start with "etr_"), so prior H4 ADD records never alter
# the signed UPDATE/FLAG/ADD batch. Whether each item is applied or a no-op is
# then resolved per item against the FULL alias index.

APPLY_SCHEMA_VERSION = "h4_kmz_apply_v1"
FLAG_QUEUE_SCHEMA_VERSION = "h4_kmz_flag_queue_v1"

DEFAULT_FLAG_QUEUE = "docs/audits/h2_kmz_flag_queue.json"
DEFAULT_APPLY_REPORT = "docs/audits/h4_kmz_apply_report.json"

# First-apply signed baseline (H2 dry-run report metadata; SIGNED Petar 2026-06-22).
# Enforced only when the data is still pristine (no ETR records yet); an already
# applied dataset legitimately differs and is validated for full consistency.
BASELINE_HYDRANTS_COUNT = 5911
BASELINE_PROVENANCE_COUNT = 5911
BASELINE_HYDRANTS_SHA = (
    "65F4E4CCCE8528E53710BC53EEA3590D6B2BD92DDCABC81803B8DBAFDA93585B")
BASELINE_PROVENANCE_SHA = (
    "894F81F6C2728BEB3356551A9FD6074435A520E3C00CA6AA843E58ED43D1016E")

# Signed batch counts the recompute must reproduce on every apply run.
EXPECTED_UPDATED = 3170
EXPECTED_FLAGGED = 317
EXPECTED_ADDED = 1306
EXPECTED_OUTPUT_COUNT = 7217  # BASELINE_HYDRANTS_COUNT + EXPECTED_ADDED

UPDATE_MERGE_ACTION = "kmz_etr_update"
ADD_MERGE_ACTION = "kmz_etr_add"
ETR_CONFIRM_ATTRIBUTION = "confirmed by ETR"
QUEUE_STATUS_PENDING = "pending_manual_review"


@dataclass(frozen=True)
class ApplyExpectations:
    """Hardcoded preconditions a real apply must satisfy. Any None field skips
    that specific assertion (tests over synthetic batches pass all-None)."""

    hydrants_count: int | None
    provenance_count: int | None
    hydrants_sha: str | None
    provenance_sha: str | None
    updated: int | None
    flagged: int | None
    added: int | None
    output_count: int | None


# The signed H4 batch (Petar 2026-06-22): the real apply over data/hydrants.json
# must reproduce exactly these. main() always uses this; only tests override it.
SIGNED_EXPECTATIONS = ApplyExpectations(
    hydrants_count=BASELINE_HYDRANTS_COUNT,
    provenance_count=BASELINE_PROVENANCE_COUNT,
    hydrants_sha=BASELINE_HYDRANTS_SHA,
    provenance_sha=BASELINE_PROVENANCE_SHA,
    updated=EXPECTED_UPDATED,
    flagged=EXPECTED_FLAGGED,
    added=EXPECTED_ADDED,
    output_count=EXPECTED_OUTPUT_COUNT,
)

# Synthetic-batch apply (tests only): no hardcoded baseline/count expectations;
# the expected output count is derived dynamically as base_count + planned ADDs.
NO_FIXED_EXPECTATIONS = ApplyExpectations(
    None, None, None, None, None, None, None, None)


class ApplyError(Exception):
    """An apply precondition or invariant failed. Fail loud and write nothing.

    Raised for baseline mismatch, recompute mismatch, alias/id collision,
    partial-apply detection, or any post-construction invariant violation."""


def is_etr_origin(record: dict) -> bool:
    origin = record.get("origin")
    return isinstance(origin, str) and origin.startswith("etr_")


def base_records_for_classification(records: list[dict]) -> list[dict]:
    """Records used as the stable classification base.

    Records appended by a prior H4 ADD run carry origin=etr_<municipality>;
    excluding them (by object reference, so UPDATE targets keep their identity)
    means dedup/classify reproduces the signed batch on a second run instead of
    seeing the just-added points as zero-distance self-matches."""
    return [r for r in records if not is_etr_origin(r)]


def _has_provenance_ref(provenance: dict, key: str, merge_action: str) -> bool:
    entry = provenance.get(key)
    if not isinstance(entry, dict):
        return False
    return any(ref.get("merge_action") == merge_action
               for ref in entry.get("source_refs", []))


# ----- Preflight -----

def assert_input_integrity(records: list[dict], provenance: dict) -> None:
    """Structural invariants required before any apply, on any run."""
    ids = [r["id"] for r in records]
    if len(ids) != len(set(ids)):
        raise ApplyError("duplicate record ids present before apply")
    for r in records:
        if "legacy_ids" not in r or not isinstance(r["legacy_ids"], list):
            raise ApplyError(f"record {r.get('id')!r} missing legacy_ids list")
        if len(r["legacy_ids"]) != len(set(r["legacy_ids"])):
            raise ApplyError(f"record {r.get('id')!r} has duplicate legacy_ids")
    for key, entry in provenance.items():
        if not isinstance(entry, dict) or "source_refs" not in entry:
            raise ApplyError(f"provenance key {key!r} missing source_refs")


def assert_first_apply_baseline(sha_in: str, sha_prov: str, count_in: int,
                                count_prov: int, expected: ApplyExpectations) -> None:
    """Pristine-data precondition. Only enforced when no ETR records exist yet,
    and only for the fields the caller pins (None fields are skipped)."""
    if expected.hydrants_count is not None and count_in != expected.hydrants_count:
        raise ApplyError(
            f"baseline hydrants count {count_in} != {expected.hydrants_count}")
    if expected.provenance_count is not None and count_prov != expected.provenance_count:
        raise ApplyError(
            f"baseline provenance count {count_prov} != {expected.provenance_count}")
    if expected.hydrants_sha is not None and sha_in.upper() != expected.hydrants_sha:
        raise ApplyError(
            f"baseline hydrants sha {sha_in} != {expected.hydrants_sha}")
    if expected.provenance_sha is not None and sha_prov.upper() != expected.provenance_sha:
        raise ApplyError(
            f"baseline provenance sha {sha_prov} != {expected.provenance_sha}")


def assert_recompute_counts(report: dict, base_count: int,
                            expected: ApplyExpectations) -> None:
    """The recompute must reproduce the signed batch exactly, every run (for the
    fields the caller pins)."""
    s = report["summary"]
    if expected.updated is not None and s["updated"] != expected.updated:
        raise ApplyError(
            f"recomputed updated {s['updated']} != {expected.updated}")
    if expected.flagged is not None and s["flagged"] != expected.flagged:
        raise ApplyError(
            f"recomputed flagged {s['flagged']} != {expected.flagged}")
    if expected.added is not None and s["added"] != expected.added:
        raise ApplyError(
            f"recomputed added {s['added']} != {expected.added}")
    if expected.output_count is not None:
        projected = s["projected_output_count_if_applied"]
        if base_count + s["added"] != expected.output_count or projected != expected.output_count:
            raise ApplyError(
                f"projected output {projected} (base {base_count} + {s['added']}) "
                f"!= {expected.output_count}")


# ----- Plan resolution (pure: classify each preview as apply/noop, detect faults) -----

def _resolve_update(pv: dict, alias: dict, provenance: dict):
    """Classify one UPDATE preview against live data.

    Returns (state, missing_aliases, fault) where state is 'apply' or 'noop',
    and fault is None or a (code, ...) tuple that must abort the whole run."""
    target = alias.get(pv["target_id"])
    if target is None:
        return None, [], ("update_target_missing", pv["target_id"])
    legacy = target.get("legacy_ids", [])
    member = pv["member_aliases"]
    present = [a for a in member if a in legacy]
    missing = [a for a in member if a not in legacy]
    # Alias collision: a not-yet-applied alias is already bound to a DIFFERENT
    # record. Never steal an alias from another hydrant.
    for a in missing:
        other = alias.get(a)
        if other is not None and other is not target:
            return None, [], ("alias_collision", a, target["id"], other["id"])
    if present and missing:
        return None, [], ("partial_update", pv["target_id"], present, missing)
    if present and not missing:
        # Fully present already: a no-op only if the H4 provenance ref also exists.
        if not _has_provenance_ref(provenance, target["id"], UPDATE_MERGE_ACTION):
            return None, [], ("update_alias_without_provenance", target["id"])
        return "noop", [], None
    return "apply", missing, None


def _resolve_add(g: dict, alias: dict, provenance: dict):
    """Classify one ADD group against live data.

    Returns (state, fault) where state is 'apply' or 'noop'."""
    rec = g["record"]
    if set(rec.keys()) != {"id", "coords", "origin", "legacy_ids"}:
        return None, ("add_record_bad_shape", rec.get("id"), sorted(rec.keys()))
    cid = rec["id"]
    existing = alias.get(cid)
    if existing is None:
        # Id free; an alias already bound elsewhere is a collision.
        for a in rec["legacy_ids"]:
            if a in alias:
                return None, ("add_alias_bound_elsewhere", a, alias[a]["id"])
        if cid in provenance:
            return None, ("add_provenance_without_record", cid)
        return "apply", None
    # Id already present: must be the same logical record to be a no-op.
    if existing.get("coords") != rec["coords"] or existing.get("origin") != rec["origin"]:
        return None, ("add_id_collision", cid, existing.get("origin"))
    missing = [a for a in rec["legacy_ids"] if a not in existing.get("legacy_ids", [])]
    if missing:
        return None, ("add_record_missing_aliases", cid, missing)
    if not _has_provenance_ref(provenance, cid, ADD_MERGE_ACTION):
        return None, ("add_record_without_provenance", cid)
    return "noop", None


def build_apply_plan(previews: dict, records: list[dict], provenance: dict) -> dict:
    """Resolve every UPDATE/ADD preview into apply/noop actions against live data.

    Pure: mutates nothing. Collects every collision / partial-apply fault; the
    caller aborts the run (writing nothing) if any fault is present."""
    alias = core.build_alias_index(records)
    faults: list[tuple] = []
    update_actions: list[dict] = []
    add_actions: list[dict] = []

    for pv in previews["update_previews"]:
        state, missing, fault = _resolve_update(pv, alias, provenance)
        if fault is not None:
            faults.append(fault)
            continue
        update_actions.append({"preview": pv, "target_id": pv["target_id"],
                               "state": state, "missing": missing})

    for g in previews["add_groups"]:
        state, fault = _resolve_add(g, alias, provenance)
        if fault is not None:
            faults.append(fault)
            continue
        add_actions.append({"group": g, "state": state})

    return {"update_actions": update_actions, "add_actions": add_actions,
            "faults": faults}


# ----- Mutation -----

def apply_update(target: dict, missing: list[str], pv: dict, provenance: dict,
                 *, timestamp: str) -> None:
    """Append missing ETR aliases to legacy_ids and one provenance ref. Touches
    no other field of the target record (plan UPDATE Semantics)."""
    old_legacy = list(target["legacy_ids"])
    new_legacy = old_legacy + missing  # existing order preserved, ETR appended
    target["legacy_ids"] = new_legacy
    provenance.setdefault(target["id"], {"source_refs": []})["source_refs"].append({
        "old_id": target["id"],
        "old_coord": list(target["coords"]),
        "manual_field": "legacy_ids",
        "old_value": old_legacy,
        "new_value": new_legacy,
        "attribution": ETR_CONFIRM_ATTRIBUTION,
        "timestamp": timestamp,
        "merge_action": UPDATE_MERGE_ACTION,
        "source_origin": pv["source_origin"],
        "source_file": pv["provenance_ref"]["source_file"],
        "source_uids": list(missing),
        "distance_m": pv["distance_m"],
        "conflict_flags": [],
    })


def apply_add(group: dict, records: list[dict], alias: dict, provenance: dict,
              *, timestamp: str) -> None:
    """Append the new {id, coords, origin, legacy_ids} record and its provenance."""
    rec = dict(group["record"])  # defensive copy; preview dict is not shared in
    records.append(rec)
    alias[rec["id"]] = rec
    for a in rec["legacy_ids"]:
        alias.setdefault(a, rec)
    provenance[rec["id"]] = {"source_refs": [{
        "old_id": None,
        "old_coord": None,
        "manual_field": "new_record",
        "old_value": None,
        "new_value": dict(rec),
        "attribution": ETR_CONFIRM_ATTRIBUTION,
        "timestamp": timestamp,
        "merge_action": ADD_MERGE_ACTION,
        "source_origin": rec["origin"],
        "source_file": group["representative_source_file"],
        "source_uids": list(rec["legacy_ids"]),
        "conflict_flags": [],
    }]}


def build_flag_queue(flag_rows: list[dict], *, timestamp: str) -> dict:
    """Versioned FLAG queue (plan FLAG Semantics). Deterministic on every run."""
    queued = []
    for row in flag_rows:
        queued.append({"flag_id": row["flag_id"],
                       "queue_status": QUEUE_STATUS_PENDING,
                       **{k: v for k, v in row.items() if k != "flag_id"}})
    return {
        "schema_version": FLAG_QUEUE_SCHEMA_VERSION,
        "generated_at": timestamp,
        "queue_status_default": QUEUE_STATUS_PENDING,
        "count": len(queued),
        "flags": queued,
    }


# ----- Post-construction validation -----

def validate_apply_state(records: list[dict], provenance: dict,
                         before_snapshot: dict, update_target_ids: set) -> dict:
    """Assert the mutated in-memory state is internally consistent and that
    UPDATE touched nothing but legacy_ids. Returns a validation summary dict.

    before_snapshot: {id: deepcopy of original record} for every pre-apply record.
    update_target_ids: ids that were UPDATE targets this run."""
    ids = [r["id"] for r in records]
    dup_after = len(ids) - len(set(ids))
    if dup_after:
        raise ApplyError(f"duplicate ids after apply: {dup_after}")
    for r in records:
        if len(r["legacy_ids"]) != len(set(r["legacy_ids"])):
            raise ApplyError(
                f"record {r['id']!r} has duplicate legacy_ids after apply")
    current = {r["id"]: r for r in records}

    missing_prov = sum(1 for r in records if r["id"] not in provenance)
    if missing_prov:
        raise ApplyError(f"{missing_prov} records missing provenance after apply")
    orphan_prov = sum(1 for k in provenance if k not in current)
    if orphan_prov:
        raise ApplyError(f"{orphan_prov} provenance keys without a record after apply")

    unexpected = 0
    for rid, before in before_snapshot.items():
        after = current.get(rid)
        if after is None:
            raise ApplyError(f"pre-apply record {rid} vanished during apply")
        if set(before.keys()) != set(after.keys()):
            raise ApplyError(f"record {rid} gained/lost a field during apply")
        before_other = {k: v for k, v in before.items() if k != "legacy_ids"}
        after_other = {k: v for k, v in after.items() if k != "legacy_ids"}
        if before_other != after_other:
            unexpected += 1
            raise ApplyError(
                f"UPDATE mutated a field outside legacy_ids on record {rid}")
        if rid not in update_target_ids and before.get("legacy_ids") != after.get("legacy_ids"):
            unexpected += 1
            raise ApplyError(f"legacy_ids changed on non-UPDATE record {rid}")
    return {
        "duplicate_ids_after": dup_after,
        "missing_provenance_after": missing_prov,
        "unexpected_field_mutations": unexpected,
    }


# ----- Report assembly -----

def build_apply_report(*, timestamp, plan, applied_updates, applied_adds,
                       noop_updates, noop_adds, queued_flags, previews,
                       report_dry, sha_in_before, sha_in_after, sha_prov_before,
                       sha_prov_after, count_in_before, count_in_after,
                       count_prov_before, count_prov_after, h2_report_path,
                       h2_report_sha, validation, output_files, args,
                       expected_output_count) -> dict:
    # Per-municipality applied/noop aggregation, keyed by source file.
    per = {b: {"source_file": b, "municipality": m, "applied_updates": 0,
               "applied_adds": 0, "queued_flags": 0, "noop_updates": 0,
               "noop_adds": 0}
           for b, m in KNOWN_KMZ}
    for a in plan["update_actions"]:
        bucket = per[a["preview"]["source_file"]]
        bucket["applied_updates" if a["state"] == "apply" else "noop_updates"] += 1
    for a in plan["add_actions"]:
        bucket = per[a["group"]["representative_source_file"]]
        bucket["applied_adds" if a["state"] == "apply" else "noop_adds"] += 1
    for row in previews["flag_rows"]:
        per[row["source_file"]]["queued_flags"] += 1

    s = report_dry["summary"]
    return {
        "schema_version": APPLY_SCHEMA_VERSION,
        "mode": "apply",
        "generated_at": timestamp,
        "inputs": {
            "hydrants_json": {
                "path": args.input.replace(os.sep, "/"),
                "sha256_before": sha_in_before,
                "sha256_after": sha_in_after,
                "record_count_before": count_in_before,
                "record_count_after": count_in_after,
            },
            "provenance_json": {
                "path": args.provenance.replace(os.sep, "/"),
                "sha256_before": sha_prov_before,
                "sha256_after": sha_prov_after,
                "record_count_before": count_prov_before,
                "record_count_after": count_prov_after,
            },
            "h2_dry_run_report": {
                "path": h2_report_path,
                "sha256": h2_report_sha,
            },
            "kmz_files": report_dry["inputs"]["kmz_files"],
        },
        "thresholds_m": report_dry["thresholds_m"],
        "summary": {
            "planned_updates": s["updated"],
            "planned_adds": s["added"],
            "planned_flags": s["flagged"],
            "applied_updates": applied_updates,
            "applied_adds": applied_adds,
            "queued_flags": queued_flags,
            "noop_updates": noop_updates,
            "noop_adds": noop_adds,
            "record_count_before": count_in_before,
            "record_count_after": count_in_after,
            "expected_record_count_after": expected_output_count,
            "provenance_count_before": count_prov_before,
            "provenance_count_after": count_prov_after,
            "collisions": 0,
            "partial_apply_detected": False,
        },
        "output_files": output_files,
        "per_file": [per[b] for b, _m in KNOWN_KMZ],
        "validation": {
            "dry_run_default_preserved": True,
            "only_allowed_paths_written": True,
            "mojibake_scan_passed": True,
            "duplicate_ids_after": validation["duplicate_ids_after"],
            "missing_provenance_after": validation["missing_provenance_after"],
            "unexpected_field_mutations": validation["unexpected_field_mutations"],
        },
    }


def run_apply(args, timestamp: str, *, expected: ApplyExpectations = SIGNED_EXPECTATIONS) -> int:
    """Signed apply path. Mutates only the four allowed files; fails loud and
    writes nothing on any precondition/invariant failure.

    expected pins the hardcoded baseline + signed-batch counts. main() always
    passes SIGNED_EXPECTATIONS (the real data guard); tests pass
    NO_FIXED_EXPECTATIONS so a synthetic batch of any size can be applied."""
    import copy

    # 1. Load + hash protected files BEFORE any mutation.
    sha_in_before = sha256_file(args.input)
    sha_prov_before = sha256_file(args.provenance)
    records = core.load_json(args.input)
    provenance = core.load_json(args.provenance)
    count_in_before = len(records)
    count_prov_before = len(provenance)

    # 2. Structural integrity (every run).
    assert_input_integrity(records, provenance)

    # 3. First-apply baseline only while the data is still pristine. An already
    #    applied dataset (ETR records present) legitimately differs.
    first_apply = not any(is_etr_origin(r) for r in records)
    if first_apply:
        assert_first_apply_baseline(sha_in_before, sha_prov_before,
                                    count_in_before, count_prov_before, expected)

    # 4. Recompute the signed batch against the stable base records.
    base = base_records_for_classification(records)
    files = load_source_dir(args.source_dir)
    input_meta = {"path": args.input.replace(os.sep, "/"),
                  "sha256": sha_in_before, "record_count": count_in_before}
    provenance_meta = {"path": args.provenance.replace(os.sep, "/"),
                       "sha256": sha_prov_before, "record_count": count_prov_before}
    report_dry, previews = run_consolidation(
        files, base, provenance, timestamp=timestamp,
        input_meta=input_meta, provenance_meta=provenance_meta)
    assert_recompute_counts(report_dry, len(base), expected)
    expected_out = (expected.output_count if expected.output_count is not None
                    else len(base) + report_dry["summary"]["added"])

    # 5. Resolve apply/noop per item; abort loud on any collision/partial fault.
    plan = build_apply_plan(previews, records, provenance)
    if plan["faults"]:
        preview = "; ".join(str(f) for f in plan["faults"][:10])
        raise ApplyError(
            f"{len(plan['faults'])} collision/partial-apply fault(s) detected; "
            f"writing nothing. First faults: {preview}")

    # 6. Snapshot every pre-apply record to prove UPDATE only touches legacy_ids.
    before_snapshot = {r["id"]: copy.deepcopy(r) for r in records}
    update_target_ids = {a["target_id"] for a in plan["update_actions"]}
    alias = core.build_alias_index(records)

    # 7. Mutate in memory: UPDATE then ADD.
    applied_updates = noop_updates = 0
    for a in plan["update_actions"]:
        if a["state"] == "apply":
            apply_update(alias[a["target_id"]], a["missing"], a["preview"],
                         provenance, timestamp=timestamp)
            applied_updates += 1
        else:
            noop_updates += 1
    applied_adds = noop_adds = 0
    for a in plan["add_actions"]:
        if a["state"] == "apply":
            apply_add(a["group"], records, alias, provenance, timestamp=timestamp)
            applied_adds += 1
        else:
            noop_adds += 1

    flag_queue = build_flag_queue(previews["flag_rows"], timestamp=timestamp)
    queued_flags = flag_queue["count"]

    # 8. Validate the mutated state (count, uniqueness, provenance, field guard).
    validation = validate_apply_state(records, provenance, before_snapshot,
                                      update_target_ids)
    count_in_after = len(records)
    count_prov_after = len(provenance)
    if count_in_after != expected_out:
        raise ApplyError(
            f"record count after apply {count_in_after} != {expected_out}")
    if count_prov_after != count_in_after:
        raise ApplyError(
            f"provenance count {count_prov_after} != record count {count_in_after}")

    # 9. Mojibake scan all four outputs BEFORE writing anything.
    output_files_map = {
        "hydrants_json": args.input.replace(os.sep, "/"),
        "provenance_json": args.provenance.replace(os.sep, "/"),
        "flag_queue": args.flag_queue.replace(os.sep, "/"),
        "apply_report": args.apply_report.replace(os.sep, "/"),
    }
    core.mojibake_scan("hydrants", records)
    core.mojibake_scan("provenance", provenance)
    core.mojibake_scan("flag_queue", flag_queue)

    # 10. Record the (untouched) H2 dry-run report hash for the apply report.
    h2_report_path = args.json_report.replace(os.sep, "/")
    h2_report_sha = sha256_file(args.json_report) if os.path.exists(args.json_report) else None

    # 11. Write data + provenance + flag queue, then hash them for the report.
    core.atomic_write_json(args.input, records)
    core.atomic_write_json(args.provenance, provenance)
    core.atomic_write_json(args.flag_queue, flag_queue, indent=2)
    sha_in_after = sha256_file(args.input)
    sha_prov_after = sha256_file(args.provenance)

    apply_report = build_apply_report(
        timestamp=timestamp, plan=plan,
        applied_updates=applied_updates, applied_adds=applied_adds,
        noop_updates=noop_updates, noop_adds=noop_adds, queued_flags=queued_flags,
        previews=previews, report_dry=report_dry,
        sha_in_before=sha_in_before, sha_in_after=sha_in_after,
        sha_prov_before=sha_prov_before, sha_prov_after=sha_prov_after,
        count_in_before=count_in_before, count_in_after=count_in_after,
        count_prov_before=count_prov_before, count_prov_after=count_prov_after,
        h2_report_path=h2_report_path, h2_report_sha=h2_report_sha,
        validation=validation, output_files=output_files_map, args=args,
        expected_output_count=expected_out)
    core.mojibake_scan("apply_report", apply_report)
    core.atomic_write_json(args.apply_report, apply_report, indent=2)

    _print_apply_summary(apply_report, args, sha_in_after, sha_prov_after)
    return 0


def _print_apply_summary(report, args, sha_in_after, sha_prov_after) -> None:
    s = report["summary"]
    print("H4 KMZ signed apply summary")
    print(f"  input:               {args.input}")
    print(f"  provenance:          {args.provenance}")
    print(f"  record_count_before: {s['record_count_before']}")
    print(f"  record_count_after:  {s['record_count_after']} "
          f"(expected {s['expected_record_count_after']})")
    print(f"  provenance_before:   {s['provenance_count_before']}")
    print(f"  provenance_after:    {s['provenance_count_after']}")
    print(f"  applied_updates:     {s['applied_updates']}  (noop {s['noop_updates']})")
    print(f"  applied_adds:        {s['applied_adds']}  (noop {s['noop_adds']})")
    print(f"  queued_flags:        {s['queued_flags']}")
    print(f"  hydrants  sha after: {sha_in_after}")
    print(f"  provenance sha after:{sha_prov_after}")
    print(f"  flag_queue:          {args.flag_queue}")
    print(f"  apply_report:        {args.apply_report}")
    print("  H2 dry-run report left unchanged (pre-apply artifact).")


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
    parser.add_argument("--flag-queue", default=DEFAULT_FLAG_QUEUE,
                        help="FLAG manual-review queue written in --apply mode.")
    parser.add_argument("--apply-report", default=DEFAULT_APPLY_REPORT,
                        help="Post-apply report written in --apply mode.")
    parser.add_argument("--timestamp", default=None,
                        help="ISO-8601 timestamp recorded in the report. Defaults "
                             "to current local time.")
    # Dry-run is the default. --apply (H4, signed) is an explicit opt-in that
    # mutates data/provenance and writes the FLAG queue + apply report; it never
    # rewrites the H2 dry-run report (a pre-apply artifact).
    parser.add_argument("--apply", action="store_true",
                        help="H4 signed apply: mutate data/provenance, write the "
                             "FLAG queue and apply report. Without it, dry-run only.")
    return parser


def main(argv=None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    args = build_parser().parse_args(argv)
    timestamp = args.timestamp or core.default_timestamp()

    if args.apply:
        return run_apply(args, timestamp)

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
