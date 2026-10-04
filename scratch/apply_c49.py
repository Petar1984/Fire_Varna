#!/usr/bin/env python3
"""Cycle #49 - issues #886-898 (13 reports, all Petar's), then one removal.

Gate 1 (2026-10-04, "давай" on the full board):
  * #887-#895: nine new надземни hydrants along an alley in the Sea Garden,
    40-107 m apart, in a stretch where the nearest registry record is
    140-500 m away - none of them was known. Clean ADDs, not tested: red.
  * #886: a new подземен hydrant on the carriageway, buried in soil. The note
    publishes with the first word fixed ("Пидранта" -> "Хидрантът"); filed
    "не е тестван", so red - the same call as #880.
  * #896: NAT-5481, already typed надземен, grey -> red.
  * #897 + #898: a relocation sent as two reports. #897 adds the hydrant
    "Зад спирката" (the note publishes - a landmark); #898 marks the old
    ВиК record VIK-VARNA_ZAPAD-0042, 28.4 m away, with "този да се премахне",
    so it is removed and archived whole. It was grey and untyped; its numbers
    live on in the archive, as with #832 and #864. #898's note is an
    instruction to the moderator and does not publish.

The note fix is proven differentially: the pipeline runs with the original and
the corrected text, and the results may differ only in verifier_note on the
#886 record.
"""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.abspath("scripts"))
from lib.hydrant_core import (  # noqa: E402
    atomic_write_json, default_timestamp, ingested_issue_numbers, load_json,
    make_source_ref, mojibake_scan, process,
)

H, P, A = "data/hydrants.json", "data/hydrants_provenance.json", "data/removed_hydrants.json"
APPROVER = "petar"
ISSUES = list(range(886, 899))
WORKER_FIELDS = ("issue_number", "id", "report_type", "reported_at", "hydrant_id",
                 "reported_coord", "type", "operational_status", "comment")

NOTE_886_RAW = ("Пидранта е точно на пътното платно и е затрупан с пръст. "
                "Работоспособността му е под сериозно съмнение")
NOTE_886 = ("Хидрантът е точно на пътното платно и е затрупан с пръст. "
            "Работоспособността му е под сериозно съмнение")
NOTE_897 = "Зад спирката"
NOTE_898_RAW = ("Ток що оставих доклад за местонохождението на хидранта (намира се зад "
                "спирката)- този да се премахне")

NEW = {  # issue -> (new id, type)
    886: ("coord_27.90158_43.21826", "подземен"),
    887: ("coord_27.93488_43.20735", "надземен"),
    888: ("coord_27.93566_43.20784", "надземен"),
    889: ("coord_27.93662_43.20840", "надземен"),
    890: ("coord_27.93711_43.20885", "надземен"),
    891: ("coord_27.93807_43.20933", "надземен"),
    892: ("coord_27.93940_43.20941", "надземен"),
    893: ("coord_27.93988_43.20943", "надземен"),
    894: ("coord_27.93408_43.20687", "надземен"),
    895: ("coord_27.93323_43.20659", "надземен"),
    897: ("coord_27.88777_43.22707", "надземен"),
}
CONFIRM_896 = "coord_27.92838_43.20999"
REMOVE_ID = "coord_27.88808_43.22695"
REMOVE_REASON = (
    "Преместен с два доклада на Петър от 04.10: #897 добави хидранта на новото му място "
    "„Зад спирката“ (coord_27.88777_43.22707, на 28.4 м), а #898 отбеляза този като липсващ "
    "с бележката „този да се премахне“. Записът беше сив и без тип. Номерата "
    "VIK-VARNA_ZAPAD-0042 и etr_varna:27.88808413,43.22695372 остават само в този архив, "
    "както при #832 и #864.")

BEFORE, AFTER, ARCH_BEFORE = 7401, 7411, 52
DELTA = {"verified": (755, 767), "works": (121, 121), "not_working": (17, 17),
         "reported": (0, 0), "notes": (93, 95), "typed": (2791, 2802)}


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
        if n == 886:
            assert r["comment"] == NOTE_886_RAW, repr(r["comment"])
            r["comment"] = NOTE_886 if corrected else NOTE_886_RAW
        elif n == 897:
            assert r["comment"] == NOTE_897, repr(r["comment"])
        elif n == 898:
            assert r["comment"] == NOTE_898_RAW, repr(r["comment"])
            r["comment"] = None
        else:
            assert not r.get("comment"), (n, r["comment"])
        out.append(r)
    return out


def main(write: bool) -> int:
    feed = json.load(open(sys.argv[sys.argv.index("--reports") + 1], encoding="utf-8"))["reports"]
    assert sorted(r["issue_number"] for r in feed) == ISSUES, [r["issue_number"] for r in feed]
    by_feed = {r["issue_number"]: r for r in feed}
    for n, (_, t) in NEW.items():
        f = by_feed[n]
        assert f["report_type"] == "new_hydrant" and f["type"] == t, (n, f)
        assert f["operational_status"] == "not_tested", n
    assert by_feed[896]["report_type"] == "exists_confirmed" and by_feed[896]["hydrant_id"] == CONFIRM_896
    assert by_feed[898]["report_type"] == "missing" and by_feed[898]["hydrant_id"] == REMOVE_ID

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    arch = load_json(A)
    assert len(recs) == BEFORE and len(arch["removed"]) == ARCH_BEFORE
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    gone = before_by_id[REMOVE_ID]
    assert gone.get("existence_status") is None and gone.get("type") is None
    assert "VIK-VARNA_ZAPAD-0042" in gone["legacy_ids"]
    assert all(new_id not in before_by_id for new_id, _ in NEW.values())
    ts = default_timestamp()

    # ---- differential proof: only the #886 note may differ ----
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
        assert x == y, ("the note fix moved a non-note field", k)
        if xn != yn:
            differ.append(k)
    assert differ == [NEW[886][0]], differ
    assert counts(plain["records"]) == counts(state["records"])

    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    out = state["records"]
    assert len(out) == BEFORE + len(NEW), len(out)
    res_by = {r["issue_number"]: r for r in res}

    by = {r["id"]: r for r in out}
    for n, (new_id, t) in NEW.items():
        assert res_by[n]["target_id_before"] is None and res_by[n]["target_id_after"] == new_id, n
        rec = by[new_id]
        assert rec["coords"] == by_feed[n]["reported_coord"], n
        assert (rec["origin"], rec["existence_status"], rec["type"], rec["operational_status"]) == \
            ("field_report", "verified", t, "not_tested"), n
        assert rec["report_id"] == by_feed[n]["id"] and rec["reported_at"] == by_feed[n]["reported_at"], n
    assert by[NEW[886][0]]["verifier_note"] == NOTE_886
    assert by[NEW[897][0]]["verifier_note"] == NOTE_897
    for n in NEW:
        if n not in (886, 897):
            assert not by[NEW[n][0]].get("verifier_note"), n
    r896 = by[CONFIRM_896]
    assert set(res_by[896]["changes"]) == {"existence_status", "operational_status"}
    assert (r896["existence_status"], r896["type"], r896["operational_status"]) == \
        ("verified", "надземен", "not_tested")

    # ---- the removal ----
    v = by[REMOVE_ID]
    assert v.get("review_status") == "reported" and not v.get("verifier_note"), v
    arch["removed"].append({"issue_number": 898, "removed_at": ts,
                            "reason": REMOVE_REASON, "record": copy.deepcopy(v)})
    ref = make_source_ref(issue_number=898, report_type="missing", old_id=REMOVE_ID,
                          old_coord=list(v["coords"]), changes={}, old_values={},
                          approver_id=APPROVER, timestamp=ts)
    ref.update(manual_field="removed", old_value=None, new_value="removed",
               merge_action="manual_removal_duplicate",
               attribution="Removed by {a} 2026-10-04 from issue #898. {r}".format(
                   a=APPROVER, r=REMOVE_REASON))
    state["provenance"][REMOVE_ID]["source_refs"].append(ref)
    out = [r for r in out if r["id"] != REMOVE_ID]
    assert len(out) == AFTER, len(out)
    assert len(arch["removed"]) == ARCH_BEFORE + 1

    # ---- the original wording of the fixed note stays in provenance ----
    fix = make_source_ref(issue_number=886, report_type="new_hydrant", old_id=None,
                          old_coord=None, changes={}, old_values={},
                          approver_id=APPROVER, timestamp=ts)
    fix.update(manual_field="note_spelling_fix", old_value=NOTE_886_RAW, new_value=NOTE_886,
               merge_action="note_spelling_fix",
               attribution=("Spelling corrected before ingest by {a} 2026-10-04 under the "
                            "standing 18.08 rule (Пидранта -> Хидрантът); the reporter's "
                            "original wording is preserved here.").format(a=APPROVER))
    state["provenance"][NEW[886][0]]["source_refs"].append(fix)

    # nothing else moved
    touched = {CONFIRM_896} | {i for i, _ in NEW.values()}
    for r in out:
        if r["id"] not in touched:
            assert r == before_by_id[r["id"]], r["id"]
    assert set(before_by_id) - {r["id"] for r in out} == {REMOVE_ID}
    assert {r["id"] for r in out} - set(before_by_id) == {i for i, _ in NEW.values()}

    after = counts(out)
    for k, (bb, aa) in DELTA.items():
        assert before[k] == bb, (k, before[k], bb)
        assert after[k] == aa, (k, after[k], aa)
    for r in out:
        assert r.get("verifier_note") not in (NOTE_886_RAW, NOTE_898_RAW), r["id"]
        note = r.get("verifier_note")
        if note:
            assert "\\" not in note and "\n" not in note and note == note.strip(), r["id"]

    blob = json.dumps(out, ensure_ascii=False) + json.dumps(state["provenance"], ensure_ascii=False)
    for name in {f["reporter"].strip() for f in feed if f.get("reporter")}:
        assert ('"%s"' % name) not in blob, "reporter name reached the data as a value"
    mojibake_scan("h", out)
    mojibake_scan("a", arch)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied %d reports | added %d | removed 1 | note fixes: 1 (proven)" % (len(res), len(NEW)))
    for k in DELTA:
        print("  %-12s %s -> %s" % (k, before[k], after[k]))
    print("  %-12s %s -> %s" % ("records", BEFORE, len(out)))
    print("  %-12s %s -> %s" % ("archive", ARCH_BEFORE, len(arch["removed"])))
    print("\nALL GATES PASSED")
    if not write:
        print("dry-run; nothing written (pass --apply to write)")
        return 0

    atomic_write_json(H, out)
    atomic_write_json(P, state["provenance"])
    atomic_write_json(A, arch, indent=1)
    stat = subprocess.run(["git", "diff", "--numstat", H, P, A],
                          capture_output=True, text=True, check=True).stdout
    print(stat, end="")
    caps = {H: 4, P: 4, A: 100}
    for line in stat.strip().splitlines():
        add, rem, path = line.split("\t")
        assert int(add) <= caps[path.replace("\\", "/")] and int(rem) <= 4, line
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--apply" in sys.argv))
