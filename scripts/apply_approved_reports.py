#!/usr/bin/env python3
"""Apply GitHub-issue reports labeled 'approved' (and not 'ingested') to
data/hydrants.json + provenance. Per Section B6 of
docs/audits/backfill_and_submission_extension_plan_20260509.md.

Default is dry-run; --apply writes. Single-admin: --approver-id ("petar")
goes into every provenance entry. Multi-admin extension points: grep
MULTI-ADMIN.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone


DEFAULT_WORKER_URL = "https://varna-hydrants-proxy.petar-dikov2019.workers.dev/issues"

KNOWN_REPORT_TYPES = frozenset({
    "exists_confirmed", "new_hydrant", "damaged", "missing", "wrong_location",
})

# Canonical vocabulary, mirrored from Worker normalizeIssue() and the frontend
# canonicalTypeFromPicker / canonicalOperationalFromPicker helpers.
CANONICAL_TYPES = frozenset({"надземен", "подземен"})
CANONICAL_OPERATIONAL = frozenset({"works", "not_working", "not_tested"})

# Worker per_page upper bound. Pagination is not supported; if the approved
# backlog ever exceeds this, ingest must run more frequently or the Worker
# needs a paging contract.
WORKER_MAX_REPORTS = 100

# Varna conservative bbox; guards bad coords from new_hydrant / wrong_location.
LON_MIN, LON_MAX = 26.5, 28.5
LAT_MIN, LAT_MAX = 42.7, 44.0


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


# ---------- Worker fetch ----------

def fetch_approved_reports(worker_url: str) -> list[dict]:
    """GET /issues, return reports labeled 'approved' and not 'ingested'."""
    sep = "&" if "?" in worker_url else "?"
    url = f"{worker_url}{sep}limit={WORKER_MAX_REPORTS}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "User-Agent": "apply_approved_reports/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status != 200:
                raise SystemExit(f"Worker GET failed: HTTP {resp.status}")
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise SystemExit(f"Worker GET failed: {exc}")
    reports = payload.get("reports")
    if not isinstance(reports, list):
        raise SystemExit("Worker response missing 'reports' array")
    return [
        r for r in reports
        if "approved" in (r.get("labels") or []) and "ingested" not in (r.get("labels") or [])
    ]


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
                    changes, old_values, approver_id, timestamp):
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
    return {
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


def _append_ref(state, key, *, report, report_type, old_id, old_coord,
                changes, old_values, approver_id, timestamp):
    state["provenance"][key]["source_refs"].append(make_source_ref(
        issue_number=report.get("issue_number"),
        report_type=report_type,
        old_id=old_id, old_coord=old_coord,
        changes=changes, old_values=old_values,
        approver_id=approver_id, timestamp=timestamp,
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


def apply_new_hydrant(state, report, timestamp, approver_id):
    coord = report.get("reported_coord")
    if not coords_in_bbox(coord):
        return _skip(report, "missing_or_invalid_coord")
    lon, lat = float(coord[0]), float(coord[1])
    new_id = canonical_coord_id(lon, lat)
    if new_id in state["alias"]:
        return _skip(report, "id_collision")

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
    return {
        "summary": {
            "fetched_count": len(reports),
            "applied_count": sum(1 for r in result_records if r["action"] == "applied"),
            "skipped_count": len(skipped),
            "skipped_reasons": dict(Counter(r["skip_reason"] for r in skipped)),
            "by_report_type": dict(Counter(r.get("report_type") for r in reports)),
            "approver_id": approver_id,
            "timestamp": timestamp,
            "input_count": input_count,
            "output_count": output_count,
        },
        "records": result_records,
    }


def ingested_issue_numbers(result_records):
    return sorted(
        r["issue_number"] for r in result_records
        if r["action"] == "applied" and r.get("issue_number") is not None
    )


def print_summary(s):
    print("Apply approved reports summary")
    for k in ("worker_url", "approver_id", "timestamp", "fetched_count",
              "applied_count", "skipped_count", "input_count", "output_count"):
        print(f"  {k+':':16s} {s.get(k, '')}")
    for label, key in (("skip_reasons", "skipped_reasons"),
                       ("by_report_type", "by_report_type")):
        if s.get(key):
            print(f"  {label}:")
            for k, v in sorted(s[key].items()):
                print(f"    {k}: {v}")


# ---------- CLI ----------

def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--worker-url", default=DEFAULT_WORKER_URL)
    parser.add_argument("--input", required=True)
    parser.add_argument("--provenance", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--timestamp", default=None,
                        help="ISO-8601 timestamp recorded in provenance entries. "
                             "Defaults to current local time.")
    parser.add_argument("--approver-id", default="petar",
                        help="Approver identity recorded in provenance. "
                             "Single-admin model; multi-admin sprint will "
                             "derive this from authenticated user.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    if args.apply and args.dry_run:
        parser.error("--apply and --dry-run are mutually exclusive")
    timestamp = args.timestamp or default_timestamp()

    records = load_json(args.input)
    provenance = load_json(args.provenance)
    input_count = len(records)

    reports = fetch_approved_reports(args.worker_url)
    state, result_records = process(
        reports, records, provenance,
        timestamp=timestamp, approver_id=args.approver_id,
    )

    mojibake_scan("hydrants", state["records"])
    mojibake_scan("provenance", state["provenance"])
    report = build_report(
        reports, result_records,
        approver_id=args.approver_id, timestamp=timestamp,
        input_count=input_count, output_count=len(state["records"]),
    )
    mojibake_scan("report", report)

    s = dict(report["summary"])
    s["worker_url"] = args.worker_url
    print_summary(s)

    if args.apply:
        atomic_write_json(args.input, state["records"])
        atomic_write_json(args.provenance, state["provenance"])
        atomic_write_json(args.report, report, indent=2)
        print(f"Wrote: {args.input}")
        print(f"Wrote: {args.provenance}")
        print(f"Wrote: {args.report}")
        ingested = ingested_issue_numbers(result_records)
        if ingested:
            print()
            print("After review of these changes, manually add label 'ingested'")
            print("and remove label 'approved' on these issues in GitHub:")
            for n in ingested:
                print(f"  #{n}")
    else:
        print()
        print("Dry run only; no files written. Use --apply to write changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
