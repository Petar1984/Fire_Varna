#!/usr/bin/env python3
"""Cycle #44 - issues #869-870 (2 reports), both from one 01 РСПБЗН officer.

Gate 1 (2026-09-24, "давай"):
  * #869 new_hydrant -> a clean ADD at [27.890295, 43.221856], placed by hand
    on site: надземен, works, so it enters green. The nearest record is 70.8 m
    away - a grey ETR row with no type, never checked - far beyond the 20 m
    band, so it is left alone.
  * #870 exists_confirmed on NAT-5220 -> grey to BLACK (verified + not_working)
    and its note publishes as written: "Липсва гайката отгоре. Не може да се
    използва ключ." The hydrant stands there but the key has nothing to grip -
    exactly what someone standing in front of it needs to know. Spelling clean;
    the type matches the one on record, so it is not rewritten.

The reporter's name is never passed to the core and must not reach the data
(PII gate); the adapter strips it and proves it absent.
"""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.abspath("scripts"))
from lib.hydrant_core import (  # noqa: E402
    atomic_write_json, default_timestamp, ingested_issue_numbers, load_json,
    mojibake_scan, process,
)

H, P = "data/hydrants.json", "data/hydrants_provenance.json"
APPROVER = "petar"
ISSUES = [869, 870]
NEW_ID = "coord_27.89029_43.22186"
NEW_COORD = [27.890295, 43.221856]
NEW_REPORT_ID = "f8cc6752-b680-4b0e-82dc-7afb78951a8e"
TARGET_870 = "coord_27.88998_43.22109"
NOTE_870 = "Липсва гайката отгоре. Не може да се използва ключ."
# Only these fields reach process(): the Worker's report shape, nothing else.
WORKER_FIELDS = ("issue_number", "id", "report_type", "reported_at", "hydrant_id",
                 "reported_coord", "type", "operational_status", "comment")

BEFORE, AFTER = 7399, 7400
DELTA = {"verified": (747, 749), "works": (114, 115), "not_working": (16, 17),
         "reported": (0, 0), "notes": (86, 87), "typed": (2782, 2783)}


def counts(rs):
    c = {k: 0 for k in DELTA}
    for r in rs:
        c["verified"] += r.get("existence_status") == "verified"
        c["works"] += r.get("operational_status") == "works"
        c["not_working"] += r.get("operational_status") == "not_working"
        c["reported"] += r.get("review_status") == "reported"
        c["notes"] += bool(r.get("verifier_note"))
        c["typed"] += bool(r.get("type"))
    return c


def main(write: bool) -> int:
    feed = json.load(open(sys.argv[sys.argv.index("--reports") + 1], encoding="utf-8"))["reports"]
    assert sorted(r["issue_number"] for r in feed) == ISSUES
    reporters = {r["reporter"] for r in feed if r.get("reporter")}
    assert reporters, "expected a reporter name to guard against"

    reps = [{k: copy.deepcopy(r.get(k)) for k in WORKER_FIELDS}
            for r in sorted(feed, key=lambda x: x["issue_number"])]
    r869, r870 = reps
    assert r869["report_type"] == "new_hydrant" and r869["reported_coord"] == NEW_COORD
    assert r869["id"] == NEW_REPORT_ID and not r869.get("comment")
    assert r870["report_type"] == "exists_confirmed" and r870["hydrant_id"] == TARGET_870
    assert r870["comment"] == NOTE_870, repr(r870["comment"])
    assert "\\" not in NOTE_870 and "\n" not in NOTE_870

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    assert len(recs) == BEFORE, len(recs)
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    assert NEW_ID not in before_by_id
    was = before_by_id[TARGET_870]
    assert was.get("existence_status") is None and was.get("type") == "надземен", was

    ts = default_timestamp()
    state, res = process(reps, recs, prov, timestamp=ts, approver_id=APPROVER)
    out = state["records"]

    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    assert len(out) == AFTER, len(out)
    by_issue = {r["issue_number"]: r for r in res}
    assert by_issue[869]["target_id_before"] is None
    assert by_issue[869]["target_id_after"] == NEW_ID
    assert by_issue[870]["target_id_before"] == by_issue[870]["target_id_after"] == TARGET_870
    assert set(by_issue[870]["changes"]) == {"existence_status", "operational_status",
                                             "verifier_note"}, by_issue[870]["changes"]

    by = {r["id"]: r for r in out}
    new = by[NEW_ID]
    assert new == {
        "id": NEW_ID, "coords": NEW_COORD, "origin": "field_report",
        "existence_status": "verified",
        "legacy_ids": [NEW_REPORT_ID, "field_" + NEW_REPORT_ID[:8]],
        "type": "надземен", "operational_status": "works",
        "report_id": NEW_REPORT_ID, "reported_at": "2026-09-24T18:15:04+03:00",
    }, new
    hit = by[TARGET_870]
    assert hit.get("existence_status") == "verified"
    assert hit.get("operational_status") == "not_working"
    assert hit.get("verifier_note") == NOTE_870
    assert hit.get("type") == "надземен"

    # nothing else moved, and the only new id is the ADD
    for r in out:
        if r["id"] not in (NEW_ID, TARGET_870):
            assert r == before_by_id[r["id"]], r["id"]
    assert {r["id"] for r in out} - set(before_by_id) == {NEW_ID}
    assert set(before_by_id) - {r["id"] for r in out} == set()

    after = counts(out)
    for k, (b, a) in DELTA.items():
        assert before[k] == b, (k, before[k], b)
        assert after[k] == a, (k, after[k], a)

    # PII gate: no reporter name anywhere in what gets written
    blob = json.dumps(out, ensure_ascii=False) + json.dumps(state["provenance"], ensure_ascii=False)
    for name in reporters:
        assert name not in blob, "reporter name reached the data"
    mojibake_scan("h", out)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied #869 (ADD %s, green) and #870 (%s, black + note)" % (NEW_ID, TARGET_870))
    for k in DELTA:
        print("  %-12s %s -> %s" % (k, before[k], after[k]))
    print("  %-12s %s -> %s" % ("records", BEFORE, len(out)))
    print("  %-12s %s -> %s" % ("grey", BEFORE - before["verified"], len(out) - after["verified"]))
    print("\nALL GATES PASSED")
    if not write:
        print("dry-run; nothing written (pass --apply to write)")
        return 0

    atomic_write_json(H, out)
    atomic_write_json(P, state["provenance"])
    stat = subprocess.run(["git", "diff", "--numstat", H, P],
                          capture_output=True, text=True, check=True).stdout
    print(stat, end="")
    for line in stat.strip().splitlines():
        add, rem, _ = line.split("\t")
        assert int(add) <= 4 and int(rem) <= 4, line
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--apply" in sys.argv))
