#!/usr/bin/env python3
"""Cycle #55 - issues #912-923 (12 reports): Petar's evening walk in the centre
(10.10), one new hydrant in Владиславово (11.10), and the first two reports of
the campaign's 37th reporter in the Provadia area (13.10).

Gate 1 (2026-10-15, "давай" on the full board):
  * #912, #914, #920, #921: new hydrants, clean ADDs (39-101 m out), not
    tested -> red.
  * #913, #915-#919: grey records confirmed on site, not tested -> red; #913's
    ВиК 330 also gets its first type, подземен.
  * #922, #923 (37th reporter): NAT-6887 (Провадия, ж.к. Север) and NAT-7055
    (Славейково) confirmed WORKING -> green. #923 corrects the imported type
    подземен -> надземен: the reporter stood at it.

Two questions were put to Petar and left unanswered, so nothing is removed and
both neighbours are proven untouched:
  * #918's NAT-5315 is 14.2 m from NAT-5316 (both national, надземен);
  * #921's new hydrant is 39 m from the grey NAT-6135 (надземен).
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
ISSUES = list(range(912, 924))
WORKER_FIELDS = ("issue_number", "id", "report_type", "reported_at", "hydrant_id",
                 "reported_coord", "type", "operational_status", "comment")

NEW = {912: "подземен", 914: "подземен", 920: "подземен", 921: "надземен"}
CONFIRM = {  # issue -> (target, changed fields, type after, operational after)
    913: ("coord_27.90899_43.21664", {"existence_status", "type", "operational_status"}, "подземен", "not_tested"),
    915: ("coord_27.91947_43.20548", {"existence_status", "operational_status"}, "надземен", "not_tested"),
    916: ("coord_27.92158_43.20436", {"existence_status", "operational_status"}, "надземен", "not_tested"),
    917: ("coord_27.92181_43.20393", {"existence_status", "operational_status"}, "надземен", "not_tested"),
    918: ("coord_27.92092_43.20469", {"existence_status", "operational_status"}, "надземен", "not_tested"),
    919: ("coord_27.91063_43.21565", {"existence_status", "operational_status"}, "подземен", "not_tested"),
    922: ("coord_27.44488_43.19199", {"existence_status", "operational_status"}, "надземен", "works"),
    923: ("coord_27.24174_43.12017", {"existence_status", "type", "operational_status"}, "надземен", "works"),
}
UNANSWERED_NEIGHBOURS = ("coord_27.92088_43.20457", "coord_27.85820_43.24514")  # NAT-5316, NAT-6135

BEFORE, AFTER = 7413, 7417
DELTA = {"verified": (774, 786), "works": (128, 130), "not_working": (18, 18),
         "reported": (0, 0), "notes": (104, 104), "typed": (2808, 2813)}


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
        n = r["issue_number"]
        assert not r.get("comment"), (n, r["comment"])
        if n in NEW:
            assert r["report_type"] == "new_hydrant" and r["type"] == NEW[n], r
            assert r["operational_status"] == "not_tested", r
            lon, lat = r["reported_coord"]
            assert 26.5 <= lon <= 28.5 and 42.7 <= lat <= 44.0, r["reported_coord"]
        else:
            tgt, _, t, op = CONFIRM[n]
            assert r["report_type"] == "exists_confirmed" and r["hydrant_id"] == tgt, r
            assert r["type"] == t and r["operational_status"] == op, r

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    assert len(recs) == BEFORE, len(recs)
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    for n, (tgt, _, _, _) in CONFIRM.items():
        assert before_by_id[tgt].get("existence_status") is None, (n, "target already verified")
    assert before_by_id["coord_27.24174_43.12017"]["type"] == "подземен"
    for nb in UNANSWERED_NEIGHBOURS:
        assert nb in before_by_id, nb

    ts = default_timestamp()
    state, res = process(reps, recs, prov, timestamp=ts, approver_id=APPROVER)
    out = state["records"]
    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    assert len(out) == AFTER, len(out)

    by = {r["id"]: r for r in out}
    new_ids = set()
    for r in res:
        n = r["issue_number"]
        if n in NEW:
            assert r["target_id_before"] is None, r
            new_id = r["target_id_after"]
            assert new_id.startswith("coord_") and new_id not in before_by_id, new_id
            f = by_feed[n]
            assert by[new_id] == {
                "id": new_id, "coords": f["reported_coord"], "origin": "field_report",
                "existence_status": "verified",
                "legacy_ids": [f["id"], "field_" + f["id"][:8]],
                "type": NEW[n], "operational_status": "not_tested",
                "report_id": f["id"], "reported_at": f["reported_at"],
            }, by[new_id]
            new_ids.add(new_id)
        else:
            tgt, fields, t, op = CONFIRM[n]
            assert r["target_id_before"] == r["target_id_after"] == tgt, r
            assert set(r["changes"]) == fields, (n, r["changes"])
            hit = by[tgt]
            assert (hit["existence_status"], hit["type"], hit["operational_status"]) == ("verified", t, op), n
            assert hit["coords"] == before_by_id[tgt]["coords"], n
            assert not hit.get("verifier_note"), n

    touched = {c[0] for c in CONFIRM.values()} | new_ids
    for r in out:
        if r["id"] not in touched:
            assert r == before_by_id[r["id"]], r["id"]
    assert {r["id"] for r in out} - set(before_by_id) == new_ids
    assert set(before_by_id) - {r["id"] for r in out} == set()
    for nb in UNANSWERED_NEIGHBOURS:
        assert by[nb] == before_by_id[nb], nb

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

    print("applied #912-923 | added %d | confirmed %d | removed 0" % (len(new_ids), len(CONFIRM)))
    for k in DELTA:
        print("  %-12s %s -> %s" % (k, before[k], after[k]))
    print("  %-12s %s -> %s" % ("records", BEFORE, len(out)))
    print("  new ids: %s" % ", ".join(sorted(new_ids)))
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
