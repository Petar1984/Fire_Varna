#!/usr/bin/env python3
"""Cycle #41 - issue #857, a single damaged report.

Ангелов on NAT-6910: "Върти се безконечно" - the spindle turns without
engaging, a hydrant that looks fine and gives no water. The record goes grey ->
black (verified + not_working) and the note publishes as written: physical
damage is the clearest pass there is of the publishing test.

The word "безконечно" is left alone. It is a real Bulgarian word and in any case
word choice is the reporter's, never the spelling rule's business.

Six other issues were open at the same time (#858-863) and are NOT in this
batch: they carry the `app-feedback` labels from the new in-app feedback
feature. The Worker feed excludes them on its own, which is the feature working
as designed - they belong to the /feedback cycle, not to hydrant moderation.
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
ISSUES = [857]
TARGET = "coord_27.33462_43.34636"
NOTE = "Върти се безконечно"
EXPECTED_COUNT = 7400
DELTA = {"verified": (743, 744), "works": (112, 112), "not_working": (15, 16),
         "reported": (0, 0), "notes": (85, 86), "typed": (2780, 2780)}


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
    assert reps[0]["report_type"] == "damaged", reps[0]["report_type"]
    assert reps[0]["comment"] == NOTE, reps[0]["comment"]

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
    assert {r["target_id_after"] for r in res} == {TARGET}

    # nothing but the one record moved
    for r in out:
        if r["id"] != TARGET:
            assert r == before_by_id[r["id"]], r["id"]
    hit = next(r for r in out if r["id"] == TARGET)
    assert hit.get("existence_status") == "verified"
    assert hit.get("operational_status") == "not_working"
    assert hit.get("verifier_note") == NOTE
    assert "\\" not in NOTE and "\n" not in NOTE

    after = counts(out)
    for k, (b, a) in DELTA.items():
        assert before[k] == b, (k, before[k], b)
        assert after[k] == a, (k, after[k], a)
    mojibake_scan("h", out)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied #857 (damaged) -> %s goes black" % TARGET)
    print("  note published: %s" % NOTE)
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
