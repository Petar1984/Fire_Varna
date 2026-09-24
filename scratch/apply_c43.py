#!/usr/bin/env python3
"""Cycle #43 - issue #868, a single confirmation that turns red into green.

Недко (ВСА), 3-та РСПБЗН - the campaign's 36th reporter and his first report -
confirmed NAT-14582 as надземен and working. The record was already verified
(#696, cycle #30) but had stayed `not_tested`, i.e. red. The type matches what
it carries, so the only field that moves is operational_status:
not_tested -> works. No note, no near-match, nothing removed.
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
ISSUES = [868]
TARGET = "coord_27.85046_43.25218"
EXPECTED_COUNT = 7399          # unchanged: a confirmation adds no record
DELTA = {"verified": (747, 747), "works": (113, 114), "not_working": (16, 16),
         "reported": (0, 0), "notes": (86, 86), "typed": (2782, 2782)}


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
    reps = sorted(feed, key=lambda x: x["issue_number"])
    assert [r["issue_number"] for r in reps] == ISSUES, [r["issue_number"] for r in reps]
    rep = reps[0]
    assert rep["report_type"] == "exists_confirmed", rep["report_type"]
    assert rep["hydrant_id"] == TARGET, rep["hydrant_id"]
    assert rep["type"] == "надземен" and rep["operational_status"] == "works", rep
    # No note was reviewed on the board; if one appears the batch is not what
    # Petar approved and the run must stop rather than publish it.
    assert not rep.get("comment"), rep["comment"]

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    assert len(recs) == EXPECTED_COUNT, len(recs)
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}

    was = before_by_id[TARGET]
    assert was.get("existence_status") == "verified", was.get("existence_status")
    assert was.get("type") == "надземен", was.get("type")
    assert was.get("operational_status") == "not_tested", was.get("operational_status")

    ts = default_timestamp()
    state, res = process(reps, recs, prov, timestamp=ts, approver_id=APPROVER)
    out = state["records"]

    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    assert len(out) == EXPECTED_COUNT, len(out)
    assert {r["target_id_after"] for r in res} == {TARGET}
    # exactly one field moved, and it is the one the report is about
    assert set(res[0]["changes"]) == {"operational_status"}, res[0]["changes"]

    for r in out:
        if r["id"] != TARGET:
            assert r == before_by_id[r["id"]], r["id"]
    hit = next(r for r in out if r["id"] == TARGET)
    assert hit.get("operational_status") == "works"
    assert hit.get("type") == "надземен"
    assert hit.get("existence_status") == "verified"
    assert hit.get("verifier_note") == was.get("verifier_note")
    rest_now = {k: v for k, v in hit.items() if k != "operational_status"}
    rest_was = {k: v for k, v in was.items() if k != "operational_status"}
    assert rest_now == rest_was, "a field other than operational_status moved"

    after = counts(out)
    for k, (b, a) in DELTA.items():
        assert before[k] == b, (k, before[k], b)
        assert after[k] == a, (k, after[k], a)
    mojibake_scan("h", out)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied #868 (exists_confirmed) -> %s goes red to green" % TARGET)
    for k in DELTA:
        print("  %-12s %s -> %s" % (k, before[k], after[k]))
    print("  %-12s %s (unchanged)" % ("records", len(out)))
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
