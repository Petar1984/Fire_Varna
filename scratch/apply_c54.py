#!/usr/bin/env python3
"""Cycle #54 - issues #907-911 (5 reports).

Gate 1 (2026-10-10, "давай" on the full board):
  * #907-#909: an 01 РСПБЗН officer along ул. "Студентска", three verified
    hydrants run for the first time. #907 does NOT work -> black, note
    "Проверен на 10.10.26г."; #908 works but has no caps -> green, note kept
    as written; #909 works -> green. Notes publish as written.
  * #910 (Petar): ВиК 255, grey and untyped -> verified, подземен, red. Note is
    a landmark; spelling fixed: "до електрическият стълб" -> "до
    електрическия стълб" (full article after a preposition).
  * #911 (Petar): NAT-5457 moved ~12 m next to the bus stop opposite the
    Niagara hotel, grey -> red (type надземен already on record). Note is a
    landmark; the hotel name gets its capital ("ниагара" -> "Ниагара"). The
    landing point is 48.6 m from ВиК 255, which #910 confirmed separately -
    two hydrants, not a duplicate.

Both note fixes are proven differentially: the pipeline runs with the
original and the corrected texts, and the results may differ only in
verifier_note on exactly those two records.
"""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.abspath("scripts"))
from lib.hydrant_core import (  # noqa: E402
    atomic_write_json, default_timestamp, ingested_issue_numbers, load_json,
    make_source_ref, mojibake_scan, process,
)

H, P = "data/hydrants.json", "data/hydrants_provenance.json"
APPROVER = "petar"
ISSUES = [907, 908, 909, 910, 911]
WORKER_FIELDS = ("issue_number", "id", "report_type", "reported_at", "hydrant_id",
                 "reported_coord", "type", "operational_status", "comment")

N907 = "Проверен на 10.10.26г."
N908 = "Работи с добро налягане, но няма тапи. Проверен на 10.10.26г."
N909 = "Работи с добро налягане. Проверен на 10.10.26г."
N910_RAW = ("Хидрантът е на тротоара, точно до електрическият стълб (на кръстовището). "
            "Между тротоара и тревната площ.")
N910 = ("Хидрантът е на тротоара, точно до електрическия стълб (на кръстовището). "
        "Между тротоара и тревната площ.")
N911_RAW = "Хидрантът е точно до спирката срещу хотел ниагара"
N911 = "Хидрантът е точно до спирката срещу хотел Ниагара"
FIXED = {910: (N910_RAW, N910, "full article after a preposition: електрическият -> електрическия"),
         911: (N911_RAW, N911, "proper noun capitalised: ниагара -> Ниагара")}
RAW = {907: N907, 908: N908, 909: N909, 910: N910_RAW, 911: N911_RAW}

# issue -> (target before, target after, changed fields, expected after-state)
EXPECT = {
    907: ("coord_27.92651_43.22456", "coord_27.92651_43.22456", {"operational_status", "verifier_note"},
          {"existence_status": "verified", "type": "надземен", "operational_status": "not_working",
           "verifier_note": N907}),
    908: ("coord_27.92771_43.22446", "coord_27.92771_43.22446", {"operational_status", "verifier_note"},
          {"existence_status": "verified", "type": "надземен", "operational_status": "works",
           "verifier_note": N908}),
    909: ("coord_27.92871_43.22437", "coord_27.92871_43.22437", {"operational_status", "verifier_note"},
          {"existence_status": "verified", "type": "надземен", "operational_status": "works",
           "verifier_note": N909}),
    910: ("coord_27.98463_43.24859", "coord_27.98463_43.24859",
          {"existence_status", "type", "operational_status", "verifier_note"},
          {"existence_status": "verified", "type": "подземен", "operational_status": "not_tested",
           "verifier_note": N910}),
    911: ("coord_27.98443_43.24818", "coord_27.98430_43.24823",
          {"coords", "id", "existence_status", "operational_status", "verifier_note"},
          {"existence_status": "verified", "type": "надземен", "operational_status": "not_tested",
           "verifier_note": N911, "coords": [27.984301, 43.248229]}),
}

COUNT = 7413
DELTA = {"verified": (772, 774), "works": (126, 128), "not_working": (17, 18),
         "reported": (0, 0), "notes": (99, 104), "typed": (2807, 2808)}


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


def build(feed, *, corrected):
    out = []
    for r in sorted(feed, key=lambda x: x["issue_number"]):
        r = {k: copy.deepcopy(r.get(k)) for k in WORKER_FIELDS}
        n = r["issue_number"]
        assert r["comment"] == RAW[n], (n, repr(r["comment"]))
        if n in FIXED and corrected:
            r["comment"] = FIXED[n][1]
        out.append(r)
    return out


def main(write: bool) -> int:
    feed = json.load(open(sys.argv[sys.argv.index("--reports") + 1], encoding="utf-8"))["reports"]
    assert sorted(r["issue_number"] for r in feed) == ISSUES, [r["issue_number"] for r in feed]
    reporters = {r["reporter"].strip() for r in feed if r.get("reporter")}
    for t in (N907, N908, N909, N910, N911):
        assert "\\" not in t and "\n" not in t and t == t.strip()

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    assert len(recs) == COUNT, len(recs)
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    for n, (tb, _, _, _) in EXPECT.items():
        assert not before_by_id[tb].get("verifier_note"), (n, "a note would be replaced")
    assert "coord_27.98430_43.24823" not in before_by_id
    ts = default_timestamp()

    plain, _ = process(build(feed, corrected=False), copy.deepcopy(recs), copy.deepcopy(prov),
                       timestamp=ts, approver_id=APPROVER)
    state, res = process(build(feed, corrected=True), copy.deepcopy(recs), copy.deepcopy(prov),
                         timestamp=ts, approver_id=APPROVER)
    a = {r["id"]: r for r in plain["records"]}
    b = {r["id"]: r for r in state["records"]}
    assert set(a) == set(b)
    differ = []
    for k in a:
        x, y = dict(a[k]), dict(b[k])
        xn, yn = x.pop("verifier_note", None), y.pop("verifier_note", None)
        assert x == y, ("a note fix moved a non-note field", k)
        if xn != yn:
            differ.append(k)
    assert sorted(differ) == sorted([EXPECT[910][1], EXPECT[911][1]]), differ
    assert counts(plain["records"]) == counts(state["records"])

    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    out = state["records"]
    assert len(out) == COUNT, len(out)
    by = {r["id"]: r for r in out}
    for r in res:
        tb, ta, fields, after = EXPECT[r["issue_number"]]
        assert r["target_id_before"] == tb and r["target_id_after"] == ta, r
        assert set(r["changes"]) == fields, (r["issue_number"], r["changes"])
        hit = by[ta]
        for k, v in after.items():
            assert hit.get(k) == v, (r["issue_number"], k, hit.get(k), v)
    # the move keeps every registry key and records the retired id as an alias
    assert {"coord_27.98443_43.24818", "NAT-5457"} <= set(by["coord_27.98430_43.24823"]["legacy_ids"])

    report_type_of = {r["issue_number"]: r["report_type"] for r in res}
    for n, (old, new, why) in FIXED.items():
        ref = make_source_ref(issue_number=n, report_type=report_type_of[n], old_id=None,
                              old_coord=None, changes={}, old_values={},
                              approver_id=APPROVER, timestamp=ts)
        ref.update(manual_field="note_spelling_fix", old_value=old, new_value=new,
                   merge_action="note_spelling_fix",
                   attribution=("Spelling corrected before ingest by {a} 2026-10-10 under the "
                                "standing 18.08 rule ({w}); the reporter's original wording is "
                                "preserved here.").format(a=APPROVER, w=why))
        state["provenance"][EXPECT[n][1]]["source_refs"].append(ref)

    touched = {t[1] for t in EXPECT.values()}
    for r in out:
        if r["id"] not in touched:
            assert r == before_by_id[r["id"]], r["id"]
    assert set(before_by_id) - {r["id"] for r in out} == {"coord_27.98443_43.24818"}
    assert {r["id"] for r in out} - set(before_by_id) == {"coord_27.98430_43.24823"}

    after = counts(out)
    for k, (bb, aa) in DELTA.items():
        assert before[k] == bb, (k, before[k], bb)
        assert after[k] == aa, (k, after[k], aa)
    for r in out:
        assert r.get("verifier_note") not in (N910_RAW, N911_RAW), r["id"]

    blob = json.dumps(out, ensure_ascii=False) + json.dumps(state["provenance"], ensure_ascii=False)
    for name in reporters:
        assert ('"%s"' % name) not in blob, "reporter name reached the data as a value"
        if len(name.split()) > 1:
            assert name not in blob, "full reporter name reached the data"
    mojibake_scan("h", out)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied #907-911 | note fixes: 2 (proven) | 1 moved")
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
