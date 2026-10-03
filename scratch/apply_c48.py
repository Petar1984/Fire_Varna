#!/usr/bin/env python3
"""Cycle #48 - issues #880-885 (6 reports, all Petar's), plus one stale
imported note removed.

Gate 1 (2026-10-03, "давай - остави 880 червен - може и да работи"):
  * #880 damaged on NAT-5393: type надземен -> подземен (the body was knocked
    off; it now looks like an underground one). He filed "не е тестван", so it
    stays RED - same call as #213 in July. The note publishes and replaces the
    older "наклонен, ударен от автомобил" one, with the space before the
    ellipsis removed under the standing spelling rule.
  * #881, #882 plain confirmations: grey -> red, надземен.
  * #883 wrong_location on NAT-12741, 9 m. The record was one of the 14
    verified on 09.09 from an imported registry note, "в градинката до
    Билла", shown as the popup title. Petar stood there and saw no Billa (OSM
    has one 102 m east, last surveyed 2020-11 - most likely closed). So:
      - the `address` holding that note is removed, or it would stay the title
        on the moved pin; the text lives on in provenance;
      - only the landmark part of his note publishes, spelling fixed:
        "Хидрантът е срещу ел. табла." The rest explained the map to the
        moderator.
  * #884 exists_confirmed then #885 wrong_location on the same ETR record, two
    minutes apart: verified + надземен, then moved 10.5 m. #885's note drops -
    "на тротоара до булеварда" restates what the moved pin shows, and the rest
    is moderator-facing.

The two changed notes are proven differentially: the pipeline runs with the
original and with the corrected text, and the results may differ only in
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
ISSUES = list(range(880, 886))
WORKER_FIELDS = ("issue_number", "id", "report_type", "reported_at", "hydrant_id",
                 "reported_coord", "type", "operational_status", "comment")

NOTE_880_RAW = ("Бил е надземен, сега прилича на подземен (вероятно ударен от автомобил и "
                "модифициран) ... пълен с пръст, работоспособността му е под силно съмнение")
NOTE_880 = ("Бил е надземен, сега прилича на подземен (вероятно ударен от автомобил и "
            "модифициран)... пълен с пръст, работоспособността му е под силно съмнение")
NOTE_883_RAW = ("Не знам защо на предният пишеше в градинката до билла... няма магазин билла "
                "наблизо. Хидранта е срущу ел табла")
NOTE_883 = "Хидрантът е срещу ел. табла."
NOTE_885_RAW = ("Хидранта се намира на тротоара до булеварда, току що го отбелязах като "
                "съществуващ в предният доклад, но позицията му е малко по встрани (където я "
                "отбулязах сега")
# issue -> (corrected text, provenance action, why)
FIXED = {
    880: (NOTE_880, "note_spelling_fix",
          "Spelling corrected before ingest by {a} 2026-10-03 under the standing 18.08 rule "
          "(no space before the ellipsis); the reporter's original wording is preserved here."),
    883: (NOTE_883, "note_reworded",
          "Trimmed before ingest at Petar's approval 2026-10-03: only the landmark that helps "
          "someone at the hydrant publishes ('opposite the electrical boards'), with the "
          "spelling fixed (Хидранта -> Хидрантът, срущу -> срещу, ел -> ел.). The rest "
          "explained the map to the moderator. The full original text is preserved here."),
}
RAW = {880: NOTE_880_RAW, 883: NOTE_883_RAW, 885: NOTE_885_RAW}
DROP = {885}

STALE_ID_BEFORE = "coord_27.90104_43.21602"   # NAT-12741
STALE_ID_AFTER = "coord_27.90115_43.21600"
STALE_ADDRESS = "в градинката до Билла"

# issue -> (target before, target after, changed fields)
EXPECT = {
    880: ("coord_27.88454_43.22904", "coord_27.88454_43.22904", {"type", "verifier_note"}),
    881: ("coord_27.91796_43.22439", "coord_27.91796_43.22439",
          {"existence_status", "type", "operational_status"}),
    882: ("coord_27.92079_43.22292", "coord_27.92079_43.22292",
          {"existence_status", "type", "operational_status"}),
    883: (STALE_ID_BEFORE, STALE_ID_AFTER,
          {"coords", "id", "type", "operational_status", "verifier_note"}),
    884: ("coord_27.90267_43.21694", "coord_27.90267_43.21694",
          {"existence_status", "type", "operational_status"}),
    885: ("coord_27.90267_43.21694", "coord_27.90268_43.21703", {"coords", "id"}),
}

BEFORE = 7401
DELTA = {"verified": (752, 755), "works": (121, 121), "not_working": (17, 17),
         "reported": (0, 0), "notes": (92, 93), "typed": (2787, 2791)}


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
        if n in RAW:
            assert r["comment"] == RAW[n], (n, repr(r["comment"]))
        if n in DROP:
            r["comment"] = None
        elif n in FIXED and corrected:
            r["comment"] = FIXED[n][0]
        out.append(r)
    return out


def main(write: bool) -> int:
    feed = json.load(open(sys.argv[sys.argv.index("--reports") + 1], encoding="utf-8"))["reports"]
    assert sorted(r["issue_number"] for r in feed) == ISSUES, [r["issue_number"] for r in feed]
    assert {r["issue_number"] for r in feed if r.get("comment")} == set(RAW)
    for t in (NOTE_880, NOTE_883):
        assert "\\" not in t and "\n" not in t and t == t.strip()

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    assert len(recs) == BEFORE, len(recs)
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    assert before_by_id[STALE_ID_BEFORE]["address"].strip() == STALE_ADDRESS
    assert STALE_ID_AFTER not in before_by_id and "coord_27.90268_43.21703" not in before_by_id
    addresses_before = sum(bool(r.get("address")) for r in recs)
    ts = default_timestamp()

    # ---- differential proof: only the two corrected notes may differ ----
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
        assert x == y, ("a note correction moved a non-note field", k)
        if xn != yn:
            differ.append(k)
    assert sorted(differ) == sorted([EXPECT[880][1], EXPECT[883][1]]), differ
    assert counts(plain["records"]) == counts(state["records"])

    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    out = state["records"]
    assert len(out) == BEFORE, len(out)
    for r in res:
        tb, ta, fields = EXPECT[r["issue_number"]]
        assert r["target_id_before"] == tb and r["target_id_after"] == ta, r
        assert set(r["changes"]) == fields, (r["issue_number"], r["changes"])

    by = {r["id"]: r for r in out}
    # #880: red, подземен, new note
    r880 = by[EXPECT[880][1]]
    assert (r880["existence_status"], r880["type"], r880["operational_status"],
            r880["verifier_note"]) == ("verified", "подземен", "not_tested", NOTE_880)
    for n in (881, 882):
        r = by[EXPECT[n][1]]
        assert (r["existence_status"], r["type"], r["operational_status"]) == \
            ("verified", "надземен", "not_tested"), n
        assert not r.get("verifier_note"), n
    r885 = by[EXPECT[885][1]]
    assert r885["coords"] == [27.902682, 43.217034]
    assert (r885["existence_status"], r885["type"], r885["operational_status"]) == \
        ("verified", "надземен", "not_tested")
    assert not r885.get("verifier_note")

    # ---- #883: moved, landmark note, and the stale imported note removed ----
    r883 = by[STALE_ID_AFTER]
    assert r883["coords"] == [27.901149, 43.215997]
    assert r883["verifier_note"] == NOTE_883
    old_addr = r883.pop("address")
    assert old_addr.strip() == STALE_ADDRESS, old_addr
    ref = make_source_ref(issue_number=883, report_type="wrong_location",
                          old_id=STALE_ID_AFTER, old_coord=list(r883["coords"]),
                          changes={}, old_values={}, approver_id=APPROVER, timestamp=ts)
    ref.update(manual_field="address", old_value=old_addr, new_value=None,
               merge_action="imported_note_removed",
               attribution=(
                   "Removed by {a} 2026-10-03 from issue #883. The `address` held a note "
                   "imported from the national registry, 'in the little garden next to "
                   "Billa', shown as the popup title; the record was verified from it on "
                   "2026-09-09. Petar stood at the hydrant and found no Billa nearby (OSM "
                   "has one 102 m east, last surveyed 2020-11 - most likely closed). Left "
                   "in place it would have stayed the title of the moved pin. The landmark "
                   "now comes from his own report instead.").format(a=APPROVER))
    state["provenance"][STALE_ID_AFTER]["source_refs"].append(ref)

    # ---- the original wording of every changed note stays in provenance ----
    report_type_of = {r["issue_number"]: r["report_type"] for r in res}
    for n, (fixed, action, why) in FIXED.items():
        rid = EXPECT[n][1]
        ref = make_source_ref(issue_number=n, report_type=report_type_of[n],
                              old_id=None, old_coord=None, changes={}, old_values={},
                              approver_id=APPROVER, timestamp=ts)
        ref.update(manual_field=action, old_value=RAW[n], new_value=fixed,
                   merge_action=action, attribution=why.format(a=APPROVER))
        state["provenance"][rid]["source_refs"].append(ref)

    # nothing else moved
    touched_after = {t[1] for t in EXPECT.values()}
    retired = {STALE_ID_BEFORE, "coord_27.90267_43.21694"}
    for r in out:
        if r["id"] not in touched_after:
            assert r == before_by_id[r["id"]], r["id"]
    assert set(before_by_id) - {r["id"] for r in out} == retired
    assert {r["id"] for r in out} - set(before_by_id) == {STALE_ID_AFTER, "coord_27.90268_43.21703"}
    assert sum(bool(r.get("address")) for r in out) == addresses_before - 1

    after = counts(out)
    for k, (bb, aa) in DELTA.items():
        assert before[k] == bb, (k, before[k], bb)
        assert after[k] == aa, (k, after[k], aa)
    # the dropped and replaced texts reached no record
    for r in out:
        assert r.get("verifier_note") not in (NOTE_883_RAW, NOTE_885_RAW, NOTE_880_RAW), r["id"]
        assert STALE_ADDRESS not in (r.get("address") or ""), r["id"]

    blob = json.dumps(out, ensure_ascii=False) + json.dumps(state["provenance"], ensure_ascii=False)
    for name in {f["reporter"].strip() for f in feed if f.get("reporter")}:
        assert ('"%s"' % name) not in blob, "reporter name reached the data as a value"
    mojibake_scan("h", out)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied %d reports | notes changed: 2 (proven) | stale address removed: 1" % len(res))
    for k in DELTA:
        print("  %-12s %s -> %s" % (k, before[k], after[k]))
    print("  %-12s %s (unchanged)" % ("records", len(out)))
    print("  %-12s %s -> %s" % ("addresses", addresses_before, addresses_before - 1))
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
