#!/usr/bin/env python3
"""Backfill type="надземен" for verified hydrants whose type is absent.

Per docs/audits/backfill_and_submission_extension_plan_20260509.md Section A.

Default mode is dry-run. Use --apply to write data/hydrants.json,
data/hydrants_provenance.json, and the migration report.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from collections import Counter
from datetime import datetime, timezone


EXPECTED_COUNT = 5901
EXPECTED_VERIFIED_COUNT = 23
EXPECTED_BEFORE_TYPES = {"<absent>": 3610, "надземен": 1144, "подземен": 1147}
EXPECTED_AFTER_TYPES = {"<absent>": 3602, "надземен": 1152, "подземен": 1147}
BACKFILL_TYPE = "надземен"
ATTRIBUTION = (
    "Petar physical verification: all currently verified records are physically надземни"
)

EXPECTED_TARGETS = {
    "coord_27.90237_43.21801": {
        "coords": [27.902373, 43.218008],
        "legacy_ids": ["VIK-VARNA_ZAPAD-0158"],
    },
    "coord_27.90313_43.21833": {
        "coords": [27.903127, 43.218328],
        "legacy_ids": ["VIK-VARNA_ZAPAD-0159"],
    },
    "coord_27.90397_43.21860": {
        "coords": [27.903968, 43.218596],
        "legacy_ids": ["877-ZP"],
    },
    "coord_27.90493_43.21885": {
        "coords": [27.90493, 43.218849],
        "legacy_ids": ["VIK-VARNA_IZTOK-0167"],
    },
    "coord_27.90614_43.21898": {
        "coords": [27.90614, 43.218982],
        "legacy_ids": ["VIK-VARNA_IZTOK-0173"],
    },
    "coord_27.90733_43.21900": {
        "coords": [27.907334, 43.218998],
        "legacy_ids": ["VIK-VARNA_IZTOK-0169"],
    },
    "coord_27.93420_43.21373": {
        "coords": [27.934205, 43.213728],
        "legacy_ids": ["271"],
    },
    "coord_27.93447_43.21327": {
        "coords": [27.934473, 43.213267],
        "legacy_ids": ["913"],
    },
}


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


def type_key(record: dict) -> str:
    value = record.get("type")
    if value is None or str(value).strip() == "":
        return "<absent>"
    return str(value)


def type_counts(records: list[dict]) -> dict[str, int]:
    return dict(Counter(type_key(r) for r in records))


def verified_records(records: list[dict]) -> list[dict]:
    return [r for r in records if r.get("existence_status") == "verified"]


def missing_verified_type_ids(records: list[dict]) -> set[str]:
    return {
        r.get("id")
        for r in verified_records(records)
        if type_key(r) == "<absent>"
    }


def assert_coords_equal(actual, expected, record_id: str) -> None:
    if not isinstance(actual, list) or len(actual) != 2:
        raise AssertionError(f"{record_id}: bad coords {actual!r}")
    if len(expected) != 2:
        raise AssertionError(f"{record_id}: bad expected coords {expected!r}")
    if actual[0] != expected[0] or actual[1] != expected[1]:
        raise AssertionError(
            f"{record_id}: coords {actual!r} != expected {expected!r}"
        )


def assert_before(records: list[dict], provenance: dict) -> None:
    if len(records) != EXPECTED_COUNT:
        raise AssertionError(f"record count {len(records)} != {EXPECTED_COUNT}")
    if len(provenance) != EXPECTED_COUNT:
        raise AssertionError(f"provenance entries {len(provenance)} != {EXPECTED_COUNT}")

    verified = verified_records(records)
    if len(verified) != EXPECTED_VERIFIED_COUNT:
        raise AssertionError(
            f"verified count {len(verified)} != {EXPECTED_VERIFIED_COUNT}"
        )

    counts = type_counts(records)
    if counts != EXPECTED_BEFORE_TYPES:
        raise AssertionError(f"before type counts {counts!r} != {EXPECTED_BEFORE_TYPES!r}")

    actual_targets = missing_verified_type_ids(records)
    expected_targets = set(EXPECTED_TARGETS)
    if actual_targets != expected_targets:
        raise AssertionError(
            "missing verified type ids mismatch: "
            f"missing={sorted(expected_targets - actual_targets)!r}, "
            f"unexpected={sorted(actual_targets - expected_targets)!r}"
        )

    by_id = {r["id"]: r for r in records}
    if len(by_id) != len(records):
        raise AssertionError("duplicate runtime ids found")

    for record_id, expected in EXPECTED_TARGETS.items():
        record = by_id.get(record_id)
        if record is None:
            raise AssertionError(f"{record_id}: missing target")
        if record.get("origin") != "vik":
            raise AssertionError(f"{record_id}: origin {record.get('origin')!r} != 'vik'")
        if record.get("existence_status") != "verified":
            raise AssertionError(f"{record_id}: not verified")
        if type_key(record) != "<absent>":
            raise AssertionError(f"{record_id}: type already populated")
        assert_coords_equal(record.get("coords"), expected["coords"], record_id)
        if record.get("legacy_ids") != expected["legacy_ids"]:
            raise AssertionError(
                f"{record_id}: legacy_ids {record.get('legacy_ids')!r} "
                f"!= {expected['legacy_ids']!r}"
            )
        entry = provenance.get(record_id)
        if not entry or not isinstance(entry.get("source_refs"), list):
            raise AssertionError(f"{record_id}: provenance source_refs missing")


def build_manual_ref(record: dict, timestamp: str) -> dict:
    return {
        "old_id": record["id"],
        "old_coord": list(record["coords"]),
        "manual_field": "type",
        "old_value": None,
        "new_value": BACKFILL_TYPE,
        "attribution": ATTRIBUTION,
        "timestamp": timestamp,
        "merge_action": "manual_backfill",
        "conflict_flags": [],
    }


def apply_backfill(records: list[dict], provenance: dict, timestamp: str) -> dict:
    by_id = {r["id"]: r for r in records}
    report_records = []

    for record_id in EXPECTED_TARGETS:
        record = by_id[record_id]
        old_snapshot = json.dumps(record, ensure_ascii=False, sort_keys=True)
        old_type = record.get("type") if "type" in record else None
        record["type"] = BACKFILL_TYPE
        new_snapshot = json.dumps(
            {k: v for k, v in record.items() if k != "type"},
            ensure_ascii=False,
            sort_keys=True,
        )
        old_without_type = json.dumps(
            {k: v for k, v in json.loads(old_snapshot).items() if k != "type"},
            ensure_ascii=False,
            sort_keys=True,
        )
        if new_snapshot != old_without_type:
            raise AssertionError(f"{record_id}: unexpected field mutation")

        provenance[record_id]["source_refs"].append(build_manual_ref(record, timestamp))

        report_records.append(
            {
                "id": record_id,
                "origin": record.get("origin"),
                "coords": record.get("coords"),
                "old_type": old_type,
                "new_type": BACKFILL_TYPE,
                "legacy_ids": record.get("legacy_ids", []),
                "provenance_appended": True,
            }
        )

    report_records.sort(key=lambda r: r["id"])
    return {
        "summary": {
            "input_count": EXPECTED_COUNT,
            "verified_count": EXPECTED_VERIFIED_COUNT,
            "changed_count": len(report_records),
            "unchanged_verified_typed_count": EXPECTED_VERIFIED_COUNT - len(report_records),
            "timestamp": timestamp,
            "attribution": ATTRIBUTION,
        },
        "records": report_records,
    }


def assert_after(records: list[dict], provenance: dict, report: dict) -> None:
    if len(records) != EXPECTED_COUNT:
        raise AssertionError(f"after record count {len(records)} != {EXPECTED_COUNT}")
    if len(provenance) != EXPECTED_COUNT:
        raise AssertionError(f"after provenance entries {len(provenance)} != {EXPECTED_COUNT}")
    if len(verified_records(records)) != EXPECTED_VERIFIED_COUNT:
        raise AssertionError("verified count changed")
    if missing_verified_type_ids(records):
        raise AssertionError(
            f"verified missing types remain: {sorted(missing_verified_type_ids(records))!r}"
        )

    counts = type_counts(records)
    if counts != EXPECTED_AFTER_TYPES:
        raise AssertionError(f"after type counts {counts!r} != {EXPECTED_AFTER_TYPES!r}")

    by_id = {r["id"]: r for r in records}
    for record_id, expected in EXPECTED_TARGETS.items():
        record = by_id[record_id]
        if record.get("type") != BACKFILL_TYPE:
            raise AssertionError(f"{record_id}: type not backfilled")
        assert_coords_equal(record.get("coords"), expected["coords"], record_id)
        refs = provenance[record_id].get("source_refs", [])
        manual_refs = [
            ref for ref in refs
            if ref.get("merge_action") == "manual_backfill"
            and ref.get("manual_field") == "type"
            and ref.get("new_value") == BACKFILL_TYPE
        ]
        if len(manual_refs) != 1:
            raise AssertionError(
                f"{record_id}: expected one manual_backfill provenance ref, "
                f"found {len(manual_refs)}"
            )

    report_ids = {r["id"] for r in report.get("records", [])}
    if report_ids != set(EXPECTED_TARGETS):
        raise AssertionError("report records do not match expected targets")


def mojibake_scan_text(name: str, obj) -> None:
    text = json.dumps(obj, ensure_ascii=False)
    if re.search(r"[\u00D0\u00D1\u00C2][\u0080-\u00FF]", text):
        raise AssertionError(f"mojibake pattern detected in serialized {name}")


def default_timestamp() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--provenance", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--timestamp", default=default_timestamp())
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    if args.apply and args.dry_run:
        parser.error("--apply and --dry-run are mutually exclusive")

    records = load_json(args.input)
    provenance = load_json(args.provenance)

    assert_before(records, provenance)
    report = apply_backfill(records, provenance, args.timestamp)
    assert_after(records, provenance, report)

    mojibake_scan_text("hydrants", records)
    mojibake_scan_text("provenance", provenance)
    mojibake_scan_text("report", report)

    print("Backfill verified type summary")
    print(f"  changed_count: {report['summary']['changed_count']}")
    print("  verified_missing_type_after: 0")
    print("  type_counts_after:")
    for key, count in sorted(type_counts(records).items()):
        print(f"    {key}: {count}")

    if args.apply:
        atomic_write_json(args.input, records)
        atomic_write_json(args.provenance, provenance)
        atomic_write_json(args.report, report, indent=2)
        print(f"Wrote: {args.input}")
        print(f"Wrote: {args.provenance}")
        print(f"Wrote: {args.report}")
    else:
        print("Dry run only; no files written. Use --apply to write changes.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
