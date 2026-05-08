"""Apply approved field-report mutations to field_reports.json and index.html.

Idempotent: re-run safe; matches by `i`. Driven by an in-script mutation table.
"""
import json
import re
import sys
import io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(r"c:\Projects\Varna_hydrants")
FR = ROOT / "field_reports.json"
INDEX = ROOT / "index.html"

NEW_HYDRANTS = [
    {
        "issue": 16,
        "i": "field_a641fc26",
        "report_id": "a641fc26-7c60-404d-9a51-844a0b9af3e7",
        "c": [27.875344, 43.239089],
        "a": "Пред бл 17 вх 1",
        "reported_at": "2026-05-05T16:40:45Z",
    },
    {
        "issue": 17,
        "i": "field_79c7d4b5",
        "report_id": "79c7d4b5-9b46-442b-8b0d-d80b11a4ca9a",
        "c": [27.877168, 43.239038],
        "a": "На велоалеята",
        "reported_at": "2026-05-05T16:43:07Z",
    },
    {
        "issue": 18,
        "i": "field_9e4cbe81",
        "report_id": "9e4cbe81-f755-42a3-987b-11acf5d8d31e",
        "c": [27.880378, 43.239405],
        "a": "Срещу каса на easypay до дърво",
        "reported_at": "2026-05-05T16:46:17Z",
    },
    {
        "issue": 19,
        "i": "field_2e92297a",
        "report_id": "2e92297a-c426-4ded-beef-c257fa61dc50",
        "c": [27.881519, 43.239128],
        "a": "В парка до велоалеята",
        "reported_at": "2026-05-05T16:47:50Z",
    },
    {
        "issue": 20,
        "i": "field_eec742fe",
        "report_id": "eec742fe-94de-409f-902e-02f68deee26d",
        "c": [27.882429, 43.232609],
        "a": "До магазин бурлекс",
        "reported_at": "2026-05-05T16:52:42Z",
    },
    {
        "issue": 21,
        "i": "field_c1eff605",
        "report_id": "c1eff605-1934-40ac-8bb0-98834e53bbf8",
        "c": [27.889152, 43.227634],
        "a": "До входа на подземният паркинг",
        "reported_at": "2026-05-05T16:58:39Z",
    },
    {
        "issue": 22,
        "i": "field_35aeaca9",
        "report_id": "35aeaca9-cdb0-4b0a-97ec-0d7aaa96cfde",
        "c": [27.896106, 43.222344],
        "a": "Срещу магазин Тръпкови и diad clima, до трафопост 2313",
        "reported_at": "2026-05-05T17:03:22Z",
    },
]

# Canonical exists_confirmed: just set status="verified".
EXISTS_CONFIRMED = [
    ("VIK-VARNA_ZAPAD-0158", 23),
    ("VIK-VARNA_ZAPAD-0159", 24),
    ("877-ZP", 25),
    ("VIK-VARNA_IZTOK-0167", 26),
    ("VIK-VARNA_IZTOK-0173", 27),
    ("VIK-VARNA_IZTOK-0169", 28),
]

# wrong_location: update c, set status="verified".
WRONG_LOCATION = [
    {
        "issue": 14,
        "i": "field_ba91e3ff",
        "old_c": [27.847459, 43.250244],
        "new_c": [27.847417, 43.250208],
    },
    {
        "issue": 15,
        "i": "NAT-14277",
        "old_c": [27.847454000277494, 43.246812000089385],
        "new_c": [27.847444, 43.246995],
    },
]


def build_new_record(spec):
    return {
        "i": spec["i"],
        "s": "",
        "a": spec["a"],
        "r": "",
        "z": "",
        "st": "",
        "t": "надземен",
        "c": spec["c"],
        "o": "field_report",
        "report_id": spec["report_id"],
        "reported_at": spec["reported_at"],
        "status": "verified",
    }


def apply_mutations(records, label):
    by_id = {r.get("i"): r for r in records}

    # Backfill: any field_* with empty/missing/"не знам" t -> "надземен"
    backfilled = []
    for r in records:
        i = r.get("i", "")
        if i.startswith("field_"):
            t = r.get("t")
            if not t or t == "не знам":
                r["t"] = "надземен"
                backfilled.append(i)

    # Apply exists_confirmed: set status="verified".
    for hid, _issue in EXISTS_CONFIRMED:
        r = by_id.get(hid)
        if r is None:
            print(f"  [{label}] WARN: exists_confirmed target not found: {hid}")
            continue
        r["status"] = "verified"
        if hid.startswith("field_"):
            t = r.get("t")
            if not t or t == "не знам":
                r["t"] = "надземен"

    # Apply wrong_location: update c, set status="verified".
    # Assertions enforce ingest rule. Canonical IDs (NAT-, VIK-, 877-ZP, etc.)
    # only live in index.html embedded JSON, never in field_reports.json — so
    # for field_reports.json we soft-skip canonical targets with a WARN, which
    # is the expected state. Hard assertions cover everything else.
    ids_before = {r.get("i") for r in records}
    field_ids_before = {i for i in ids_before if i and i.startswith("field_")}
    count_before = len(records)

    for spec in WRONG_LOCATION:
        target_id = spec["i"]
        is_field_id = target_id.startswith("field_")
        r = by_id.get(target_id)
        if r is None:
            if not is_field_id and label == "field_reports.json":
                # Canonical IDs are not expected in field_reports.json — skip.
                print(
                    f"  [{label}] SKIP: wrong_location canonical target "
                    f"{target_id} not in this dataset (expected; lives in "
                    f"index.html embedded JSON)"
                )
                continue
            raise AssertionError(
                f"[{label}] wrong_location target_id not in records: {target_id}"
            )
        cur = r.get("c")
        old_c, new_c = spec["old_c"], spec["new_c"]
        tol = 0.001
        matches_old = (
            abs(cur[0] - old_c[0]) <= tol and abs(cur[1] - old_c[1]) <= tol
        )
        matches_new = (
            abs(cur[0] - new_c[0]) <= tol and abs(cur[1] - new_c[1]) <= tol
        )
        assert matches_old or matches_new, (
            f"[{label}] wrong_location {target_id}: current c={cur} matches "
            f"neither old_c={old_c} nor new_c={new_c} within tol={tol} — "
            f"refusing to overwrite (target may have shifted; re-check report)"
        )
        r["c"] = spec["new_c"]
        r["status"] = "verified"
        # If field_*, ensure t="надземен" (already covered by backfill above).

    assert len(records) == count_before, (
        f"[{label}] wrong_location must not change record count "
        f"({count_before} -> {len(records)})"
    )
    field_ids_after = {
        r.get("i") for r in records
        if r.get("i", "") and r.get("i", "").startswith("field_")
    }
    assert field_ids_after == field_ids_before, (
        f"[{label}] wrong_location must not create new field_* IDs; "
        f"new IDs detected: {field_ids_after - field_ids_before}"
    )

    # Append new hydrants (idempotency: skip if i already present).
    appended = []
    for spec in NEW_HYDRANTS:
        if spec["i"] in by_id:
            print(f"  [{label}] SKIP: {spec['i']} already present (idempotent)")
            continue
        rec = build_new_record(spec)
        records.append(rec)
        by_id[spec["i"]] = rec
        appended.append(spec["i"])

    print(f"  [{label}] backfilled t for {len(backfilled)} field_* records: {backfilled}")
    print(f"  [{label}] appended {len(appended)} new records: {appended}")
    return records


def main():
    # 1. field_reports.json
    fr = json.loads(FR.read_text(encoding="utf-8"))
    print(f"field_reports.json: {len(fr)} records before")
    fr = apply_mutations(fr, "field_reports.json")
    print(f"field_reports.json: {len(fr)} records after")
    FR.write_text(
        json.dumps(fr, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # 2. index.html embedded JSON (single megaline).
    html = INDEX.read_text(encoding="utf-8")
    pattern = re.compile(
        r'(<script id="hydrantData" type="application/json">)(\[.*?\])(</script>)',
        re.DOTALL,
    )
    m = pattern.search(html)
    if not m:
        sys.exit("ERROR: hydrantData script tag not found")
    embedded = json.loads(m.group(2))
    print(f"index.html embedded: {len(embedded)} records before")
    embedded = apply_mutations(embedded, "index.html")
    print(f"index.html embedded: {len(embedded)} records after")
    new_json = json.dumps(embedded, ensure_ascii=False, separators=(",", ":"))
    new_html = html[: m.start(2)] + new_json + html[m.end(2):]
    INDEX.write_text(new_html, encoding="utf-8")

    print("OK")


if __name__ == "__main__":
    main()
