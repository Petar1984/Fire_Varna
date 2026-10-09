#!/usr/bin/env python3
"""Cycle #53 - issues #904-906, three new hydrants in the village of Поляците.

Filed by the reporter signing as "Служител" (seven earlier reports around
Provadia and Golden Sands), 10:50-10:56 on 09.10. The village already has
registry ВиК hydrants, but the nearest is 103-202 m away from each point, so
all three are clean ADDs. #904 подземен, not tested -> red; #905 подземен and
#906 надземен, both working -> green. No notes, nothing removed.
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
ISSUES = [904, 905, 906]
WORKER_FIELDS = ("issue_number", "id", "report_type", "reported_at", "hydrant_id",
                 "reported_coord", "type", "operational_status", "comment")
NEW = {  # issue -> (new id, type, operational)
    904: ("coord_27.11951_42.98749", "подземен", "not_tested"),
    905: ("coord_27.12726_42.98459", "подземен", "works"),
    906: ("coord_27.12822_42.98456", "надземен", "works"),
}
BEFORE, AFTER = 7410, 7413
DELTA = {"verified": (769, 772), "works": (124, 126), "not_working": (17, 17),
         "reported": (0, 0), "notes": (99, 99), "typed": (2804, 2807)}


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
    by_feed = {r["issue_number"]: r for r in feed}
    reporters = {r["reporter"].strip() for r in feed if r.get("reporter")}
    reps = [{k: copy.deepcopy(r.get(k)) for k in WORKER_FIELDS}
            for r in sorted(feed, key=lambda x: x["issue_number"])]
    for r in reps:
        _, t, op = NEW[r["issue_number"]]
        assert r["report_type"] == "new_hydrant" and r["type"] == t and r["operational_status"] == op, r
        assert not r.get("comment"), r["comment"]
        lon, lat = r["reported_coord"]
        assert 26.5 <= lon <= 28.5 and 42.7 <= lat <= 44.0, r["reported_coord"]

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    assert len(recs) == BEFORE, len(recs)
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    assert all(i not in before_by_id for i, _, _ in NEW.values())

    ts = default_timestamp()
    state, res = process(reps, recs, prov, timestamp=ts, approver_id=APPROVER)
    out = state["records"]
    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    assert len(out) == AFTER, len(out)

    by = {r["id"]: r for r in out}
    for r in res:
        new_id, t, op = NEW[r["issue_number"]]
        assert r["target_id_before"] is None and r["target_id_after"] == new_id, r
        f = by_feed[r["issue_number"]]
        assert by[new_id] == {
            "id": new_id, "coords": f["reported_coord"], "origin": "field_report",
            "existence_status": "verified",
            "legacy_ids": [f["id"], "field_" + f["id"][:8]],
            "type": t, "operational_status": op,
            "report_id": f["id"], "reported_at": f["reported_at"],
        }, by[new_id]
    for r in out:
        if r["id"] in before_by_id:
            assert r == before_by_id[r["id"]], r["id"]
    assert {r["id"] for r in out} - set(before_by_id) == {i for i, _, _ in NEW.values()}

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

    print("applied #904-906 -> three new hydrants in Поляците (1 red, 2 green)")
    for k in DELTA:
        print("  %-12s %s -> %s" % (k, before[k], after[k]))
    print("  %-12s %s -> %s" % ("records", BEFORE, len(out)))
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
