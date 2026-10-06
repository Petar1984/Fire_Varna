#!/usr/bin/env python3
"""Cycle #51 - issue #900, a single confirmation on a grey ETR record.

Petar confirmed `coord_27.97552_43.22443` (ETR key only), grey and untyped, as
надземен, not tested: grey -> red. No note, no near-match, nothing removed;
the nearest records are 87-125 m away.
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
ISSUES = [900]
TARGET = "coord_27.97552_43.22443"
EXPECTED_COUNT = 7410
WORKER_FIELDS = ("issue_number", "id", "report_type", "reported_at", "hydrant_id",
                 "reported_coord", "type", "operational_status", "comment")
DELTA = {"verified": (768, 769), "works": (121, 121), "not_working": (17, 17),
         "reported": (0, 0), "notes": (96, 96), "typed": (2803, 2804)}


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
    assert [r["issue_number"] for r in feed] == ISSUES, [r["issue_number"] for r in feed]
    reporters = {r["reporter"].strip() for r in feed if r.get("reporter")}
    reps = [{k: copy.deepcopy(r.get(k)) for k in WORKER_FIELDS} for r in feed]
    rep = reps[0]
    assert rep["report_type"] == "exists_confirmed" and rep["hydrant_id"] == TARGET
    assert rep["type"] == "надземен" and rep["operational_status"] == "not_tested"
    assert not rep.get("comment"), rep["comment"]

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    assert len(recs) == EXPECTED_COUNT, len(recs)
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    was = before_by_id[TARGET]
    for k in ("existence_status", "type", "operational_status", "verifier_note", "address"):
        assert was.get(k) is None, (k, was.get(k))

    ts = default_timestamp()
    state, res = process(reps, recs, prov, timestamp=ts, approver_id=APPROVER)
    out = state["records"]
    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    assert len(out) == EXPECTED_COUNT, len(out)
    assert {r["target_id_after"] for r in res} == {TARGET}
    assert set(res[0]["changes"]) == {"existence_status", "type", "operational_status"}

    for r in out:
        if r["id"] != TARGET:
            assert r == before_by_id[r["id"]], r["id"]
    hit = next(r for r in out if r["id"] == TARGET)
    assert (hit["existence_status"], hit["type"], hit["operational_status"]) == \
        ("verified", "надземен", "not_tested")
    assert hit["coords"] == was["coords"] and hit["legacy_ids"] == was["legacy_ids"]

    after = counts(out)
    for k, (b, a) in DELTA.items():
        assert before[k] == b, (k, before[k], b)
        assert after[k] == a, (k, after[k], a)
    blob = json.dumps(out, ensure_ascii=False) + json.dumps(state["provenance"], ensure_ascii=False)
    for name in reporters:
        assert ('"%s"' % name) not in blob, "reporter name reached the data as a value"
    mojibake_scan("h", out)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied #900 (exists_confirmed) -> %s goes grey to red" % TARGET)
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
