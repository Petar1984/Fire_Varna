#!/usr/bin/env python3
"""Cycle #47 - issues #873-879 (7 reports): two of Petar's and a five-hydrant
walk by an 01 РСПБЗН officer.

Gate 1 (2026-10-02, "давай" on the full board):
  * #873 exists_confirmed on ВиК 998 (+ ETR), grey and untyped -> verified,
    надземен, not tested: red. Filed 26.09, after cycle #46 was closed.
  * #874 new_hydrant at [27.879204, 43.232793] -> clean ADD, 148 m from the
    nearest record; подземен, not tested: red.
  * #875-#879, ten minutes along one street: five hydrants already verified
    but never run; each now confirmed working, and each note publishes as
    written - the pressure and the date of the test are what someone standing
    there needs, the same call Petar made for this reporter's #636/#637. #875's
    note is worded a little differently from the other four (dash, capital,
    no "г."); that is the reporter's style, not spelling, so it is left alone.
    #879's record also gains its first type, надземен.

Nothing removed, no near-match. The reporter names never reach the core and
are proven absent from the written data.
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
ISSUES = list(range(873, 880))
WORKER_FIELDS = ("issue_number", "id", "report_type", "reported_at", "hydrant_id",
                 "reported_coord", "type", "operational_status", "comment")

NEW_ID = "coord_27.87920_43.23279"
NEW_COORD = [27.879204, 43.232793]
NEW_REPORT_ID = "12c162e7-0bed-4ae2-b6f9-8c419b63e80a"

NOTE_A = "С добро налягане - Проверен на 02.10.26"
NOTE_B = "С добро налягане, проверен на 02.10.26г."
# issue -> (target, the fields the report must change, expected after-state)
EXPECT = {
    873: ("coord_27.89670_43.23558", {"existence_status", "type", "operational_status"},
          {"existence_status": "verified", "type": "надземен",
           "operational_status": "not_tested", "verifier_note": None}),
    875: ("coord_27.90405_43.20722", {"operational_status", "verifier_note"},
          {"existence_status": "verified", "type": "надземен",
           "operational_status": "works", "verifier_note": NOTE_A}),
    876: ("coord_27.90300_43.20682", {"operational_status", "verifier_note"},
          {"existence_status": "verified", "type": "надземен",
           "operational_status": "works", "verifier_note": NOTE_B}),
    877: ("coord_27.90196_43.20645", {"operational_status", "verifier_note"},
          {"existence_status": "verified", "type": "надземен",
           "operational_status": "works", "verifier_note": NOTE_B}),
    878: ("coord_27.90136_43.20628", {"operational_status", "verifier_note"},
          {"existence_status": "verified", "type": "надземен",
           "operational_status": "works", "verifier_note": NOTE_B}),
    879: ("coord_27.90490_43.20762", {"type", "operational_status", "verifier_note"},
          {"existence_status": "verified", "type": "надземен",
           "operational_status": "works", "verifier_note": NOTE_B}),
}

BEFORE, AFTER = 7400, 7401
DELTA = {"verified": (750, 752), "works": (116, 121), "not_working": (17, 17),
         "reported": (0, 0), "notes": (87, 92), "typed": (2784, 2787)}


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
    assert sorted(r["issue_number"] for r in feed) == ISSUES, [r["issue_number"] for r in feed]
    reporters = {r["reporter"].strip() for r in feed if r.get("reporter")}
    reps = [{k: copy.deepcopy(r.get(k)) for k in WORKER_FIELDS}
            for r in sorted(feed, key=lambda x: x["issue_number"])]
    by_num = {r["issue_number"]: r for r in reps}

    # the batch is exactly what the board showed
    r874 = by_num[874]
    assert r874["report_type"] == "new_hydrant" and r874["reported_coord"] == NEW_COORD
    assert r874["id"] == NEW_REPORT_ID and not r874.get("comment")
    assert r874["type"] == "подземен" and r874["operational_status"] == "not_tested"
    for n, (tgt, _, after) in EXPECT.items():
        r = by_num[n]
        assert r["report_type"] == "exists_confirmed" and r["hydrant_id"] == tgt, (n, r)
        assert r["type"] == after["type"] and r["operational_status"] == after["operational_status"], (n, r)
        assert r.get("comment") == after["verifier_note"], (n, repr(r.get("comment")))
    for note in (NOTE_A, NOTE_B):
        assert "\\" not in note and "\n" not in note and note == note.strip()

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    assert len(recs) == BEFORE, len(recs)
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    assert NEW_ID not in before_by_id
    for n, (tgt, _, _) in EXPECT.items():
        assert not before_by_id[tgt].get("verifier_note"), (n, "a note would be replaced")

    ts = default_timestamp()
    state, res = process(reps, recs, prov, timestamp=ts, approver_id=APPROVER)
    out = state["records"]

    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    assert len(out) == AFTER, len(out)
    res_by = {r["issue_number"]: r for r in res}
    assert res_by[874]["target_id_before"] is None and res_by[874]["target_id_after"] == NEW_ID

    by = {r["id"]: r for r in out}
    for n, (tgt, fields, after) in EXPECT.items():
        rr = res_by[n]
        assert rr["target_id_before"] == rr["target_id_after"] == tgt, (n, rr)
        assert set(rr["changes"]) == fields, (n, rr["changes"])
        hit = by[tgt]
        for k, v in after.items():
            assert hit.get(k) == v, (n, k, hit.get(k), v)
        assert hit["coords"] == before_by_id[tgt]["coords"], n

    assert by[NEW_ID] == {
        "id": NEW_ID, "coords": NEW_COORD, "origin": "field_report",
        "existence_status": "verified",
        "legacy_ids": [NEW_REPORT_ID, "field_" + NEW_REPORT_ID[:8]],
        "type": "подземен", "operational_status": "not_tested",
        "report_id": NEW_REPORT_ID, "reported_at": "2026-10-02T08:52:58+03:00",
    }, by[NEW_ID]

    touched = {t for t, _, _ in EXPECT.values()} | {NEW_ID}
    for r in out:
        if r["id"] not in touched:
            assert r == before_by_id[r["id"]], r["id"]
    assert {r["id"] for r in out} - set(before_by_id) == {NEW_ID}
    assert set(before_by_id) - {r["id"] for r in out} == set()

    after = counts(out)
    for k, (b, a) in DELTA.items():
        assert before[k] == b, (k, before[k], b)
        assert after[k] == a, (k, after[k], a)

    blob = json.dumps(out, ensure_ascii=False) + json.dumps(state["provenance"], ensure_ascii=False)
    for name in reporters:
        assert ('"%s"' % name) not in blob, "reporter name reached the data as a value"
        if len(name.split()) > 1:
            assert name not in blob, "full reporter name reached the data"
    mojibake_scan("h", out)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied %d reports | ADD %s | published notes: 5" % (len(res), NEW_ID))
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
