#!/usr/bin/env python3
"""Cycle #56 - issues #924-930, Petar's first confirmations of the Burgas-side
records added by ADR 013: seven national records in Obzor, 93-231 m apart.

Gate 1 (2026-10-17, "давай"): all seven grey -> red (verified, надземен, not
tested). Two of them carry a type correction from the reporter: NAT-7212
and NAT-7367 were imported as подземен and are reported надземен - the person
who saw the hydrant outranks the registry, the same call as #923. No notes,
no near-match, nothing removed.
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
ISSUES = list(range(924, 931))
WORKER_FIELDS = ("issue_number", "id", "report_type", "reported_at", "hydrant_id",
                 "reported_coord", "type", "operational_status", "comment")
BOTH = {"existence_status", "operational_status"}
TARGETS = {  # issue -> (target, NAT id, changed fields)
    924: ("coord_27.87988_42.81768", "NAT-7212", BOTH | {"type"}),
    925: ("coord_27.88270_42.82321", "NAT-7367", BOTH | {"type"}),
    926: ("coord_27.88064_42.82357", "NAT-7382", BOTH),
    927: ("coord_27.87831_42.82239", "NAT-7383", BOTH),
    928: ("coord_27.87805_42.82495", "NAT-7241", BOTH),
    929: ("coord_27.87915_42.82475", "NAT-7242", BOTH),
    930: ("coord_27.88141_42.82672", "NAT-7379", BOTH),
}
COUNT = 7454
DELTA = {"verified": (786, 793), "works": (130, 130), "not_working": (18, 18),
         "reported": (0, 0), "notes": (104, 104), "typed": (2850, 2850)}


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
    for r in reps:
        tgt = TARGETS[r["issue_number"]][0]
        assert r["report_type"] == "exists_confirmed" and r["hydrant_id"] == tgt, r
        assert r["type"] == "надземен" and r["operational_status"] == "not_tested", r
        assert not r.get("comment"), r["comment"]

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    assert len(recs) == COUNT, len(recs)
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    for n, (tgt, nat, fields) in TARGETS.items():
        was = before_by_id[tgt]
        assert was["legacy_ids"] == [nat] and was["origin"] == "national", (n, was)
        assert was.get("existence_status") is None, (n, "already verified")
        assert was["type"] == ("подземен" if "type" in fields else "надземен"), (n, was["type"])

    ts = default_timestamp()
    state, res = process(reps, recs, prov, timestamp=ts, approver_id=APPROVER)
    out = state["records"]
    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    assert len(out) == COUNT, len(out)

    by = {r["id"]: r for r in out}
    for r in res:
        tgt, nat, fields = TARGETS[r["issue_number"]]
        assert r["target_id_before"] == r["target_id_after"] == tgt, r
        assert set(r["changes"]) == fields, (r["issue_number"], r["changes"])
        hit = by[tgt]
        assert (hit["existence_status"], hit["type"], hit["operational_status"]) == \
            ("verified", "надземен", "not_tested"), r["issue_number"]
        assert hit["coords"] == before_by_id[tgt]["coords"] and hit["legacy_ids"] == [nat]
    touched = {t[0] for t in TARGETS.values()}
    for r in out:
        if r["id"] not in touched:
            assert r == before_by_id[r["id"]], r["id"]

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

    print("applied #924-930 -> seven Obzor records grey to red, 2 type corrections")
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
