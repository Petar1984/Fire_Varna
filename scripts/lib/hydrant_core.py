#!/usr/bin/env python3
"""Shared core for applying approved hydrant field reports.

Reusable, non-network logic extracted from scripts/apply_approved_reports.py per
docs/plans/h1_shared_core_spatial_dedup.md. The adapter (apply_approved_reports.py)
keeps Worker fetch, argparse, printing, and dry-run/apply write selection; this
module owns the constants, IO safety, identity/index helpers, spatial matcher,
diff/provenance helpers, typed handlers, and the process/report pipeline.

Standard library only. Default behavior is computed in memory; callers decide
whether to write.
"""

from __future__ import annotations

import json
import math
import os
import re
import tempfile
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone


KNOWN_REPORT_TYPES = frozenset({
    "exists_confirmed", "new_hydrant", "damaged", "missing", "wrong_location",
})

# Canonical vocabulary, mirrored from Worker normalizeIssue() and the frontend
# canonicalTypeFromPicker / canonicalOperationalFromPicker helpers.
CANONICAL_TYPES = frozenset({"надземен", "подземен"})
CANONICAL_OPERATIONAL = frozenset({"works", "not_working", "not_tested"})

# Varna conservative bbox; guards bad coords from new_hydrant / wrong_location.
LON_MIN, LON_MAX = 26.5, 28.5
LAT_MIN, LAT_MAX = 42.7, 44.0

# Signed spatial thresholds (Petar, 2026-06-21): UPDATE <= Rm, FLAG (Rm, Rf], ADD > Rf.
DEFAULT_RM_M = 5.0
DEFAULT_RF_M = 20.0

# Mean Earth radius (m); matches the data_audit / migrate_to_verbose_schema.py
# dedup methodology, so spatial distances reproduce the planning probe exactly.
EARTH_RADIUS_M = 6371008.8


# ---------- IO ----------

def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def atomic_write_json(path: str, obj, *, indent=None) -> None:
    parent = os.path.dirname(path) or "."
    os.makedirs(parent, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".tmp_", dir=parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            json.dump(obj, f, ensure_ascii=False, indent=indent)
            f.write("\n")
        os.replace(tmp, path)
    except Exception:
        try:
            os.remove(tmp)
        except OSError:
            pass
        raise


def mojibake_scan(name: str, obj) -> None:
    text = json.dumps(obj, ensure_ascii=False)
    if re.search(r"[ÐÑÂ][-ÿ]", text):
        raise AssertionError(f"mojibake pattern detected in serialized {name}")


def default_timestamp() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


# ---------- Index / lookup ----------

def build_alias_index(records: list[dict]) -> dict[str, dict]:
    idx: dict[str, dict] = {}
    for r in records:
        idx[r["id"]] = r
        for alias in r.get("legacy_ids", []):
            if alias and alias not in idx:
                idx[alias] = r
    return idx


def canonical_coord_id(lon: float, lat: float) -> str:
    return f"coord_{lon:.5f}_{lat:.5f}"


def coords_in_bbox(coord) -> bool:
    if not isinstance(coord, (list, tuple)) or len(coord) != 2:
        return False
    lon, lat = coord
    if not isinstance(lon, (int, float)) or not isinstance(lat, (int, float)):
        return False
    return LON_MIN <= lon <= LON_MAX and LAT_MIN <= lat <= LAT_MAX


def field_short_id(full_id: str) -> str | None:
    """Mirror the frontend's `field_<8>` truncation."""
    if not isinstance(full_id, str) or not full_id:
        return None
    if full_id.startswith("field_"):
        return full_id
    return "field_" + full_id.replace("-", "")[:8]


# ---------- Stable-id registry (H1 stub; migration is H3) ----------

class StableIdRegistry:
    """Interface for minting ids for brand-new records. H1 stub only: real
    stable-id assignment and migration of existing coord_ ids is H3 scope."""

    def id_for_new_record(self, lon, lat, *, source_ref=None) -> str:
        raise NotImplementedError


class CoordIdRegistry(StableIdRegistry):
    """Default H1 registry: keeps the existing coord_<lon>_<lat> id shape so
    ADD output stays byte-compatible with current data."""

    def id_for_new_record(self, lon, lat, *, source_ref=None) -> str:
        return canonical_coord_id(lon, lat)


# ---------- Spatial matching ----------

class SpatialDecision:
    """Signed thresholds (Petar, 2026-06-21): UPDATE <= Rm, FLAG (Rm, Rf], ADD > Rf."""

    UPDATE = "UPDATE"
    FLAG = "FLAG"
    ADD = "ADD"


@dataclass(frozen=True)
class SpatialMatch:
    decision: str
    nearest_record: dict | None
    distance_m: float | None


def distance_m(a, b) -> float:
    """Local equirectangular meter distance between two (lon, lat) points.

    Deterministic, stdlib-only, accurate enough for the 1-25 m comparisons this
    matcher makes in the Varna oblast. EARTH_RADIUS_M matches the data_audit
    dedup methodology so distances reproduce the planning probe exactly."""
    lon1, lat1 = a
    lon2, lat2 = b
    lat0 = math.radians((lat1 + lat2) / 2.0)
    x = math.radians(lon2 - lon1) * math.cos(lat0) * EARTH_RADIUS_M
    y = math.radians(lat2 - lat1) * EARTH_RADIUS_M
    return math.hypot(x, y)


def find_nearest_hydrant(point, records):
    """Linear scan for the nearest record to `point` (lon, lat).

    Returns (record, distance_m) or (None, None) when there is no usable record.
    Ties break deterministically by (distance_m, record id). H1 keeps this a
    linear scan: at issue-ingest volume a grid index would be premature; KMZ H2
    can add one if needed."""
    nearest = None
    nearest_distance = None
    for rec in records:
        coords = rec.get("coords")
        if not isinstance(coords, (list, tuple)) or len(coords) != 2:
            continue
        d = distance_m(point, (coords[0], coords[1]))
        if nearest is None or (d, rec["id"]) < (nearest_distance, nearest["id"]):
            nearest, nearest_distance = rec, d
    return nearest, nearest_distance


def classify_spatial_match(distance, *, rm_m=DEFAULT_RM_M, rf_m=DEFAULT_RF_M) -> str:
    if distance is None:
        return SpatialDecision.ADD
    if distance <= rm_m:
        return SpatialDecision.UPDATE
    if distance <= rf_m:
        return SpatialDecision.FLAG
    return SpatialDecision.ADD


def match_point(point, records, *, rm_m=DEFAULT_RM_M, rf_m=DEFAULT_RF_M) -> SpatialMatch:
    """Classify a candidate point against existing records: UPDATE / FLAG / ADD."""
    nearest, distance = find_nearest_hydrant(point, records)
    if nearest is None:
        return SpatialMatch(SpatialDecision.ADD, None, None)
    decision = classify_spatial_match(distance, rm_m=rm_m, rf_m=rf_m)
    return SpatialMatch(decision, nearest, distance)


# ---------- Diff helpers ----------

def diff_set(rec, field, new_value, changes, old_values):
    if rec.get(field) != new_value:
        old_values[field] = rec.get(field)
        rec[field] = new_value
        changes[field] = {"old": old_values[field], "new": new_value}


def diff_del(rec, field, changes, old_values):
    if field in rec:
        old_values[field] = rec[field]
        del rec[field]
        changes[field] = {"old": old_values[field], "new": None}


# ---------- Provenance ----------

def make_source_ref(*, issue_number, report_type, old_id, old_coord,
                    changes, old_values, approver_id, timestamp, distance_m=None):
    if len(changes) == 0:
        manual_field, old_value, new_value = "noop", None, None
    elif len(changes) == 1:
        manual_field = next(iter(changes))
        old_value = old_values.get(manual_field)
        new_value = changes[manual_field]["new"]
    else:
        manual_field = "multiple"
        old_value = dict(old_values)
        new_value = {k: v["new"] for k, v in changes.items()}
    ref = {
        "old_id": old_id,
        "old_coord": old_coord,
        "manual_field": manual_field,
        "old_value": old_value,
        "new_value": new_value,
        "attribution": f"Approved by {approver_id} from issue #{issue_number}",
        "timestamp": timestamp,
        "merge_action": "ingest_approved_report",
        "issue_number": issue_number,
        "report_type": report_type,
        "conflict_flags": [],
        # MULTI-ADMIN: shift_id and authorization_check fields append here.
    }
    # Spatial UPDATE provenance only: existing handlers pass distance_m=None and
    # must not gain this field (parity constraint).
    if distance_m is not None:
        ref["distance_m"] = round(distance_m, 3)
    return ref


# ---------- Result records ----------

def _applied(report, target_before, target_after, changes):
    return {
        "issue_number": report.get("issue_number"),
        "report_type": report.get("report_type"),
        "action": "applied",
        "target_id_before": target_before,
        "target_id_after": target_after,
        "changes": changes,
    }


def _skip(report, reason):
    return {
        "issue_number": report.get("issue_number"),
        "report_type": report.get("report_type"),
        "action": "skipped",
        "skip_reason": reason,
    }


def _flagged(report, nearest_id, distance):
    # Distinct from "skipped": a flagged near-match is a manual-review queue
    # item, not a parse/lookup failure, and must not be marked ingested.
    return {
        "issue_number": report.get("issue_number"),
        "report_type": report.get("report_type"),
        "action": "flagged",
        "flag_reason": "spatial_near_match",
        "nearest_id": nearest_id,
        "distance_m": round(distance, 3),
        "changes": {},
    }


def _append_ref(state, key, *, report, report_type, old_id, old_coord,
                changes, old_values, approver_id, timestamp, distance_m=None):
    state["provenance"][key]["source_refs"].append(make_source_ref(
        issue_number=report.get("issue_number"),
        report_type=report_type,
        old_id=old_id, old_coord=old_coord,
        changes=changes, old_values=old_values,
        approver_id=approver_id, timestamp=timestamp,
        distance_m=distance_m,
    ))


# ---------- Apply functions ----------

def apply_exists_confirmed(state, report, timestamp, approver_id):
    rec = state["alias"].get(report.get("hydrant_id"))
    if rec is None:
        return _skip(report, "target_not_found")
    changes, old_values = {}, {}
    diff_set(rec, "existence_status", "verified", changes, old_values)
    rtype = report.get("type")
    if rtype in CANONICAL_TYPES:
        diff_set(rec, "type", rtype, changes, old_values)
    rop = report.get("operational_status")
    if rop in CANONICAL_OPERATIONAL:
        diff_set(rec, "operational_status", rop, changes, old_values)
    # Clear the moderation gate so the canonical fields render post-approval.
    diff_del(rec, "review_status", changes, old_values)
    _append_ref(state, rec["id"], report=report, report_type="exists_confirmed",
                old_id=rec["id"], old_coord=list(rec["coords"]),
                changes=changes, old_values=old_values,
                approver_id=approver_id, timestamp=timestamp)
    return _applied(report, rec["id"], rec["id"], changes)


def apply_new_hydrant(state, report, timestamp, approver_id, *,
                      registry=None, rm_m=DEFAULT_RM_M, rf_m=DEFAULT_RF_M):
    """Spatial-dedup new_hydrant: within Rm -> UPDATE the nearest record, within
    (Rm, Rf] -> FLAG for manual review, beyond Rf (or empty dataset) -> ADD.

    Spatial dedup applies to new_hydrant only; the other handlers are unchanged.
    """
    if registry is None:
        registry = CoordIdRegistry()
    coord = report.get("reported_coord")
    if not coords_in_bbox(coord):
        return _skip(report, "missing_or_invalid_coord")
    lon, lat = float(coord[0]), float(coord[1])
    new_id = registry.id_for_new_record(lon, lat)
    # Exact-id idempotency guard (unchanged): a report already ingested at this
    # canonical coord must not be re-added or re-applied.
    if new_id in state["alias"]:
        return _skip(report, "id_collision")

    match = match_point((lon, lat), state["records"], rm_m=rm_m, rf_m=rf_m)
    if match.decision == SpatialDecision.UPDATE:
        return _apply_new_hydrant_update(state, report, match, timestamp, approver_id)
    if match.decision == SpatialDecision.FLAG:
        return _flagged(report, match.nearest_record["id"], match.distance_m)
    return _apply_new_hydrant_add(state, report, lon, lat, new_id, timestamp, approver_id)


def _apply_new_hydrant_update(state, report, match, timestamp, approver_id):
    # Within Rm of an existing record: treat the report as confirmation of that
    # record. Mutate the existing record, never its coordinates or id. The
    # report wins for canonical type/operational_status; review_status is left
    # untouched (Petar 2026-06-21).
    rec = match.nearest_record
    changes, old_values = {}, {}

    full = report.get("id")
    if isinstance(full, str) and full:
        legacy = list(rec.get("legacy_ids", []))
        if full not in legacy:
            legacy.append(full)
        short = field_short_id(full)
        if short and short != full and short not in legacy:
            legacy.append(short)
        diff_set(rec, "legacy_ids", legacy, changes, old_values)

    diff_set(rec, "existence_status", "verified", changes, old_values)
    rtype = report.get("type")
    if rtype in CANONICAL_TYPES:
        diff_set(rec, "type", rtype, changes, old_values)
    rop = report.get("operational_status")
    if rop in CANONICAL_OPERATIONAL:
        diff_set(rec, "operational_status", rop, changes, old_values)
    # review_status intentionally NOT touched on new_hydrant UPDATE.

    _append_ref(state, rec["id"], report=report, report_type="new_hydrant",
                old_id=rec["id"], old_coord=list(rec["coords"]),
                changes=changes, old_values=old_values,
                approver_id=approver_id, timestamp=timestamp,
                distance_m=match.distance_m)

    res = _applied(report, rec["id"], rec["id"], changes)
    res["spatial_decision"] = SpatialDecision.UPDATE
    res["distance_m"] = round(match.distance_m, 3)
    return res


def _apply_new_hydrant_add(state, report, lon, lat, new_id, timestamp, approver_id):
    # Beyond Rf of any existing record: genuinely new. Keeps the current ADD
    # record/provenance shape byte-for-byte.
    legacy: list[str] = []
    full = report.get("id")
    if isinstance(full, str) and full:
        legacy.append(full)
        short = field_short_id(full)
        if short and short != full:
            legacy.append(short)

    new_record: dict = {
        "id": new_id,
        "coords": [lon, lat],
        "origin": "field_report",
        "existence_status": "verified",
        "legacy_ids": legacy,
    }
    if report.get("type") in CANONICAL_TYPES:
        new_record["type"] = report["type"]
    if report.get("operational_status") in CANONICAL_OPERATIONAL:
        new_record["operational_status"] = report["operational_status"]
    if isinstance(full, str) and full:
        new_record["report_id"] = full
    if isinstance(report.get("reported_at"), str):
        new_record["reported_at"] = report["reported_at"]

    state["records"].append(new_record)
    state["alias"][new_id] = new_record
    for alias in legacy:
        state["alias"][alias] = new_record

    state["provenance"][new_id] = {"source_refs": [make_source_ref(
        issue_number=report.get("issue_number"),
        report_type="new_hydrant",
        old_id=None, old_coord=None,
        changes={"new_record": {"new": dict(new_record)}},
        old_values={},
        approver_id=approver_id, timestamp=timestamp,
    )]}
    return _applied(report, None, new_id, {"created": new_record})


def apply_damaged(state, report, timestamp, approver_id):
    rec = state["alias"].get(report.get("hydrant_id"))
    if rec is None:
        return _skip(report, "target_not_found")
    changes, old_values = {}, {}
    rop = report.get("operational_status")
    if rop in CANONICAL_OPERATIONAL:
        diff_set(rec, "operational_status", rop, changes, old_values)
    # damaged keeps review_status='reported' per Section B6: a follow-up
    # resolution flow (future sprint) clears it, not ingest.
    diff_set(rec, "review_status", "reported", changes, old_values)
    _append_ref(state, rec["id"], report=report, report_type="damaged",
                old_id=rec["id"], old_coord=list(rec["coords"]),
                changes=changes, old_values=old_values,
                approver_id=approver_id, timestamp=timestamp)
    return _applied(report, rec["id"], rec["id"], changes)


def apply_missing(state, report, timestamp, approver_id):
    # Section B6 (verbatim): "missing: keep review_status:'reported'". Ingest
    # never auto-drops the record — a false-positive missing report would
    # otherwise destroy data with no recovery path beyond provenance surgery.
    # A separate sprint will build the "really delete this hydrant" workflow.
    rec = state["alias"].get(report.get("hydrant_id"))
    if rec is None:
        return _skip(report, "target_not_found")
    changes, old_values = {}, {}
    diff_set(rec, "review_status", "reported", changes, old_values)
    _append_ref(state, rec["id"], report=report, report_type="missing",
                old_id=rec["id"], old_coord=list(rec["coords"]),
                changes=changes, old_values=old_values,
                approver_id=approver_id, timestamp=timestamp)
    return _applied(report, rec["id"], rec["id"], changes)


def apply_wrong_location(state, report, timestamp, approver_id):
    rec = state["alias"].get(report.get("hydrant_id"))
    if rec is None:
        return _skip(report, "target_not_found")
    coord = report.get("reported_coord")
    if not coords_in_bbox(coord):
        return _skip(report, "missing_or_invalid_coord")
    lon, lat = float(coord[0]), float(coord[1])
    old_id, old_coord = rec["id"], list(rec["coords"])
    new_id = canonical_coord_id(lon, lat)
    if new_id != old_id and new_id in state["alias"]:
        return _skip(report, "id_collision")

    changes, old_values = {}, {}
    if old_coord != [lon, lat]:
        old_values["coords"] = old_coord
        rec["coords"] = [lon, lat]
        changes["coords"] = {"old": old_coord, "new": [lon, lat]}
    if new_id != old_id:
        old_values["id"] = old_id
        rec["id"] = new_id
        legacy = list(rec.get("legacy_ids", []))
        if old_id not in legacy:
            legacy.insert(0, old_id)
        rec["legacy_ids"] = legacy
        changes["id"] = {"old": old_id, "new": new_id}
        # Re-key provenance to the new canonical id; alias rebuild covers
        # old_id via the now-extended legacy_ids list.
        state["provenance"][new_id] = state["provenance"].pop(old_id, {"source_refs": []})
        state["alias"][new_id] = rec
    diff_set(rec, "existence_status", "verified", changes, old_values)
    diff_del(rec, "review_status", changes, old_values)

    _append_ref(state, rec["id"], report=report, report_type="wrong_location",
                old_id=old_id, old_coord=old_coord,
                changes=changes, old_values=old_values,
                approver_id=approver_id, timestamp=timestamp)
    return _applied(report, old_id, rec["id"], changes)


DISPATCH = {
    "exists_confirmed": apply_exists_confirmed,
    "new_hydrant":      apply_new_hydrant,
    "damaged":          apply_damaged,
    "missing":          apply_missing,
    "wrong_location":   apply_wrong_location,
}


# ---------- Pipeline ----------

def process(reports, records, provenance, *, timestamp, approver_id):
    state = {
        "records": list(records),
        "provenance": provenance,
        "alias": build_alias_index(records),
    }
    result_records: list[dict] = []
    for report in reports:
        rtype = report.get("report_type")
        if rtype not in KNOWN_REPORT_TYPES:
            result_records.append(_skip(report, "parse_error"))
            continue
        try:
            res = DISPATCH[rtype](state, report, timestamp, approver_id)
        except Exception as exc:
            res = _skip(report, f"exception:{type(exc).__name__}")
            res["exception_message"] = str(exc)
        result_records.append(res)
    state["alias"] = build_alias_index(state["records"])
    return state, result_records


def build_report(reports, result_records, *, approver_id, timestamp,
                 input_count, output_count):
    skipped = [r for r in result_records if r["action"] == "skipped"]
    flagged = [r for r in result_records if r["action"] == "flagged"]
    summary = {
        "fetched_count": len(reports),
        "applied_count": sum(1 for r in result_records if r["action"] == "applied"),
        "skipped_count": len(skipped),
        "skipped_reasons": dict(Counter(r["skip_reason"] for r in skipped)),
        "by_report_type": dict(Counter(r.get("report_type") for r in reports)),
        "approver_id": approver_id,
        "timestamp": timestamp,
        "input_count": input_count,
        "output_count": output_count,
    }
    # Add flagged keys only when at least one flagged result exists, so reports
    # with no near-matches stay byte-identical to the pre-H1 shape.
    if flagged:
        summary["flagged_count"] = len(flagged)
        summary["flagged_reasons"] = dict(Counter(r["flag_reason"] for r in flagged))
    return {
        "summary": summary,
        "records": result_records,
    }


def ingested_issue_numbers(result_records):
    return sorted(
        r["issue_number"] for r in result_records
        if r["action"] == "applied" and r.get("issue_number") is not None
    )
