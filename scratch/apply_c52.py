#!/usr/bin/env python3
"""Cycle #52 - issues #901-903, an 01 РСПБЗН officer's evening walk.

Three hydrants 67-130 m apart, all already verified but never run; each now
confirmed working with the note "Работи с добро налягане, проверен на
06.10.26" (#903 with a trailing "г."). Red -> green, notes published as
written - the same call as this reporter's walk in cycle #47 (#875-#879).
No near-match, nothing removed; only operational_status and the note move.
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
ISSUES = [901, 902, 903]
WORKER_FIELDS = ("issue_number", "id", "report_type", "reported_at", "hydrant_id",
                 "reported_coord", "type", "operational_status", "comment")
NOTE_A = "Работи с добро налягане, проверен на 06.10.26"
NOTE_B = "Работи с добро налягане, проверен на 06.10.26г."
TARGETS = {901: ("coord_27.89998_43.21764", NOTE_A),
           902: ("coord_27.90055_43.21720", NOTE_A),
           903: ("coord_27.90157_43.21774", NOTE_B)}
EXPECTED_COUNT = 7410
DELTA = {"verified": (769, 769), "works": (121, 124), "not_working": (17, 17),
         "reported": (0, 0), "notes": (96, 99), "typed": (2804, 2804)}


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
        tgt, note = TARGETS[r["issue_number"]]
        assert r["report_type"] == "exists_confirmed" and r["hydrant_id"] == tgt, r
        assert r["type"] == "надземен" and r["operational_status"] == "works", r
        assert r["comment"] == note, (r["issue_number"], repr(r["comment"]))
    for note in (NOTE_A, NOTE_B):
        assert "\\" not in note and "\n" not in note and note == note.strip()

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    assert len(recs) == EXPECTED_COUNT, len(recs)
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    for tgt, _ in TARGETS.values():
        was = before_by_id[tgt]
        assert (was.get("existence_status"), was.get("type"), was.get("operational_status")) == \
            ("verified", "надземен", "not_tested"), (tgt, was)
        assert not was.get("verifier_note"), (tgt, "a note would be replaced")

    ts = default_timestamp()
    state, res = process(reps, recs, prov, timestamp=ts, approver_id=APPROVER)
    out = state["records"]
    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    assert len(out) == EXPECTED_COUNT, len(out)

    by = {r["id"]: r for r in out}
    for r in res:
        tgt, note = TARGETS[r["issue_number"]]
        assert r["target_id_before"] == r["target_id_after"] == tgt, r
        assert set(r["changes"]) == {"operational_status", "verifier_note"}, r["changes"]
        hit = by[tgt]
        assert hit["operational_status"] == "works" and hit["verifier_note"] == note
        rest_now = {k: v for k, v in hit.items() if k not in ("operational_status", "verifier_note")}
        rest_was = {k: v for k, v in before_by_id[tgt].items()
                    if k not in ("operational_status", "verifier_note")}
        assert rest_now == rest_was, tgt
    touched = {t for t, _ in TARGETS.values()}
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
        if len(name.split()) > 1:
            assert name not in blob, "full reporter name reached the data"
    mojibake_scan("h", out)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied #901-903 -> three red hydrants go green, notes published")
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
