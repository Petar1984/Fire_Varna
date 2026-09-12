#!/usr/bin/env python3
"""Cycle #39 - issues #819-828 (10 reports).

Two morning walks of Petar's: Кичево 07:21-07:27, eastern Varna 08:17-08:19.
Ten `exists_confirmed` on grey records, not one note, not one duplicate, no
near-match, nothing removed. Like cycle #34 this adapter carries no override
table at all - the shape every cycle aims for.

Worth one line for the record: #825 and #826 sit **9.3 m apart** and Petar
confirmed both in the same minute. They are two existing records, not a new
pin, so nothing flags - but 9.3 m is inside the band where a `new_hydrant`
would. He confirmed both deliberately, so if that pair ever reads like a
duplicate later, this is the note saying it was checked on foot.
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
ISSUES = list(range(819, 829))
EXPECTED_COUNT = 7403          # unchanged: confirmations add no records
DELTA = {"verified": (709, 719), "works": (111, 111), "not_working": (15, 15),
         "reported": (0, 0), "notes": (84, 84), "typed": (2761, 2769)}


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
    assert [r["issue_number"] for r in reps] == ISSUES
    # No note is expected anywhere in this batch; if one appears the batch is
    # not what was reviewed and the run must stop rather than publish it.
    for r in reps:
        assert not r.get("comment"), (r["issue_number"], r["comment"])

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    assert len(recs) == EXPECTED_COUNT, len(recs)
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}

    ts = default_timestamp()
    state, res = process(reps, recs, prov, timestamp=ts, approver_id=APPROVER)
    out = state["records"]

    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    assert len(out) == EXPECTED_COUNT, len(out)

    touched = {r["target_id_after"] for r in res}
    assert len(touched) == len(ISSUES), touched      # ten reports, ten records
    for r in out:
        if r["id"] not in touched:
            assert r == before_by_id[r["id"]], r["id"]

    after = counts(out)
    for k, (b, a) in DELTA.items():
        assert before[k] == b, (k, before[k], b)
        assert after[k] == a, (k, after[k], a)
    for r in out:
        note = r.get("verifier_note")
        if note:
            assert before_by_id[r["id"]].get("verifier_note") == note, r["id"]
    mojibake_scan("h", out)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied %d confirmations, no notes, no removals" % len(res))
    for k in DELTA:
        print("  %-12s %s -> %s" % (k, before[k], after[k]))
    print("  %-12s %s (unchanged)" % ("records", len(out)))
    print("  %-12s %s -> %s" % ("grey", len(recs) - before["verified"], len(out) - after["verified"]))
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
