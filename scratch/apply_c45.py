#!/usr/bin/env python3
"""Cycle #45 - issue #871, a single confirmation that turns red into green.

The third report in seven hours from the same 01 РСПБЗН officer, on the same
walk. The target is a field-report record, already verified and typed
надземен, which never carried an operational status at all - so it showed
red. He confirmed the same type and that it works; the only field that moves
is operational_status: (absent) -> works. No note, no near-match, nothing
removed. Same shape as cycle #43.
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
ISSUES = [871]
TARGET = "coord_27.89740_43.21260"
EXPECTED_COUNT = 7400          # unchanged: a confirmation adds no record
WORKER_FIELDS = ("issue_number", "id", "report_type", "reported_at", "hydrant_id",
                 "reported_coord", "type", "operational_status", "comment")
DELTA = {"verified": (749, 749), "works": (115, 116), "not_working": (17, 17),
         "reported": (0, 0), "notes": (87, 87), "typed": (2783, 2783)}


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
    reporters = {r["reporter"] for r in feed if r.get("reporter")}
    reps = [{k: copy.deepcopy(r.get(k)) for k in WORKER_FIELDS} for r in feed]
    rep = reps[0]
    assert rep["report_type"] == "exists_confirmed", rep["report_type"]
    assert rep["hydrant_id"] == TARGET, rep["hydrant_id"]
    assert rep["type"] == "надземен" and rep["operational_status"] == "works", rep
    # No note was reviewed on the board; if one appears, stop rather than publish it.
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
    assert was.get("operational_status") is None, was.get("operational_status")

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
    rest_now = {k: v for k, v in hit.items() if k != "operational_status"}
    rest_was = {k: v for k, v in was.items() if k != "operational_status"}
    assert rest_now == rest_was, "a field other than operational_status moved"

    after = counts(out)
    for k, (b, a) in DELTA.items():
        assert before[k] == b, (k, before[k], b)
        assert after[k] == a, (k, after[k], a)

    blob = json.dumps(out, ensure_ascii=False) + json.dumps(state["provenance"], ensure_ascii=False)
    for name in reporters:
        assert name not in blob, "reporter name reached the data"
    mojibake_scan("h", out)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied #871 (exists_confirmed) -> %s goes red to green" % TARGET)
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
