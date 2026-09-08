#!/usr/bin/env python3
"""Cycle #35 adapter - issues #752-769 (18 reports).

Petar's Gate-1 decisions (2026-09-08), all "go with the recommendations":

  * Golden Sands is open to field reports. Six reports land on `pozarna_gz`
    records after Иван Драганов walked the resort. The old invariant "99 grey,
    byte-identical" is retired here on his word; what replaces it is measured
    below - the block still holds 99 records and ONLY the five reported ones
    change.
  * Five notes get the spelling fix from the standing 18.08 rule, applied
    BEFORE ingest. Proven, not asserted: the pipeline runs twice, once with the
    original notes and once with the corrected ones, and the two results must be
    identical field-for-field except `verifier_note` on exactly those five
    records, with every colour counter equal.
  * Three `wrong_location` notes are dropped (#759, #764, #769) - the settled
    rule, ninth cycle running. #769's also carried a message to the moderator
    and a bug report about the form.
  * #754 types `works` into the field, derived from its own text ("Работи, но
    трудно се спира водата"), with a provenance ref marking it derived rather
    than submitted - the #634 precedent. Its note publishes too, because it
    carries the valve warning on top of the status.
  * #762's note publishes whole; trimming it was an option, never a
    recommendation, and rewording is Petar's own call.

Nothing is written unless every assertion below holds.
"""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.abspath("scripts"))
from lib.hydrant_core import (  # noqa: E402
    atomic_write_json, build_report, default_timestamp, ingested_issue_numbers,
    load_json, make_source_ref, mojibake_scan, process,
)

HYDRANTS = "data/hydrants.json"
PROVENANCE = "data/hydrants_provenance.json"
APPROVER = "petar"

DROP_NOTE = {759, 764, 769}          # wrong_location: the settled rule
DERIVE_WORKS = {754}                 # status lifted out of the free text

# {issue: (original note, corrected note)} - the 18.08 spelling rule.
SPELL = {
    756: ("Хидранта се намира в шахта до оградата.",
          "Хидрантът се намира в шахта до оградата."),
    757: ("Хидранта е изведен над земята, но е необходима стойка.",
          "Хидрантът е изведен над земята, но е необходима стойка."),
    761: ("Хидранта е подземен, но е изведен над земята и е необходима стойка.",
          "Хидрантът е подземен, но е изведен над земята и е необходима стойка."),
    767: ('В ляво от входа за подземният паркинг на х-л "Интернационал"',
          'Вляво от входа за подземния паркинг на х-л "Интернационал"'),
    768: ("Във двора на болницата.", "В двора на болницата."),
}

EXPECTED_ISSUES = list(range(752, 770))
EXPECTED_BEFORE = 7411
EXPECTED_AFTER = 7413
EXPECTED_TOUCHED = {
    "coord_27.89998_43.21764", "coord_27.92226_43.22306", "coord_27.92448_43.20860",
    "coord_27.92483_43.23097", "coord_27.92594_43.22860", "coord_27.92993_43.22256",
    "coord_28.03925_43.28792", "coord_28.04236_43.28271", "coord_28.04264_43.28569",
    "coord_28.04297_43.28948", "coord_28.04320_43.28940", "coord_28.04406_43.28819",
    "coord_28.04427_43.29473", "coord_28.04427_43.29507", "coord_28.04554_43.29651",
    "coord_28.04944_43.30139",
}
EXPECTED_DELTA = {
    "verified": (645, 657), "works": (97, 106), "not_working": (11, 13),
    "reported": (0, 2), "notes": (71, 81), "typed": (2733, 2741),
}
# Golden Sands: the block keeps all 99 records and only these five move.
GZ_TOUCHED = {
    "coord_28.04944_43.30139",   # #757 -> green
    "coord_28.04297_43.28948",   # #759 moves it 14.9 m, #760 -> black
    "coord_28.04427_43.29507",   # #763 -> black
    "coord_28.04406_43.28819",   # #766 -> green
    "coord_28.04236_43.28271",   # #767 -> green
}
GZ_MOVED_FROM = "coord_28.04287_43.28959"


def counts(records):
    c = {k: 0 for k in EXPECTED_DELTA}
    for r in records:
        c["verified"] += r.get("existence_status") == "verified"
        c["works"] += r.get("operational_status") == "works"
        c["not_working"] += r.get("operational_status") == "not_working"
        c["reported"] += r.get("review_status") == "reported"
        c["notes"] += bool(r.get("verifier_note"))
        c["typed"] += bool(r.get("type"))
    return c


def build_reports(feed, *, with_spell: bool):
    """The reports as they go into the handler, with Petar's decisions applied."""
    out = []
    for r in sorted(feed, key=lambda x: x["issue_number"]):
        r = copy.deepcopy(r)
        n = r["issue_number"]
        if n in DROP_NOTE:
            r["comment"] = None
        if n in DERIVE_WORKS:
            assert r.get("operational_status") is None, (n, r.get("operational_status"))
            r["operational_status"] = "works"
        if n in SPELL:
            assert r["comment"] == SPELL[n][0], (n, r["comment"])
            if with_spell:
                r["comment"] = SPELL[n][1]
        out.append(r)
    return out


def run(feed, records, provenance, *, with_spell, timestamp):
    return process(build_reports(feed, with_spell=with_spell),
                   copy.deepcopy(records), copy.deepcopy(provenance),
                   timestamp=timestamp, approver_id=APPROVER)


def main(apply_writes: bool) -> int:
    feed = json.load(open(sys.argv[sys.argv.index("--reports") + 1],
                          encoding="utf-8"))["reports"]
    assert sorted(r["issue_number"] for r in feed) == EXPECTED_ISSUES

    before_bytes = open(HYDRANTS, "rb").read()
    before_sha = hashlib.sha256(before_bytes).hexdigest()
    records = json.loads(before_bytes.decode("utf-8"))
    provenance = load_json(PROVENANCE)
    assert len(records) == EXPECTED_BEFORE, len(records)
    before_counts = counts(records)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in records}
    gz_before = {r["id"] for r in records if r.get("origin") == "pozarna_gz"}
    assert len(gz_before) == 99, len(gz_before)

    timestamp = default_timestamp()

    # ---- The spelling proof: same pipeline, only the note text differs ----
    plain_state, _ = run(feed, records, provenance, with_spell=False, timestamp=timestamp)
    state, results = run(feed, records, provenance, with_spell=True, timestamp=timestamp)
    out = state["records"]

    a = {r["id"]: r for r in plain_state["records"]}
    b = {r["id"]: r for r in out}
    assert set(a) == set(b), "the spelling fix changed which records exist"
    note_only = []
    for k in a:
        x, y = dict(a[k]), dict(b[k])
        xn, yn = x.pop("verifier_note", None), y.pop("verifier_note", None)
        assert x == y, ("the spelling fix changed a non-note field", k)
        if xn != yn:
            note_only.append((k, xn, yn))
    assert len(note_only) == len(SPELL), (len(note_only), len(SPELL))
    assert counts(plain_state["records"]) == counts(out), "the spelling fix moved a colour"

    # ---- Gate: the pipeline did exactly what was signed off ----
    assert all(r["action"] == "applied" for r in results), \
        [r for r in results if r["action"] != "applied"]
    assert sorted(ingested_issue_numbers(results)) == EXPECTED_ISSUES
    assert len(out) == EXPECTED_AFTER, len(out)
    touched = {r["target_id_after"] for r in results}
    assert touched == EXPECTED_TOUCHED, touched ^ EXPECTED_TOUCHED

    after_counts = counts(out)
    for k, (exp_b, exp_a) in EXPECTED_DELTA.items():
        assert before_counts[k] == exp_b, (k, before_counts[k], exp_b)
        assert after_counts[k] == exp_a, (k, after_counts[k], exp_a)

    # ---- Gate: nothing outside the reported records moved ----
    for r in out:
        old = before_by_id.get(r["id"])
        if old is not None and r["id"] not in touched:
            assert r == old, r["id"]

    # ---- Gate: Golden Sands, under its NEW rule ----
    # The block is no longer frozen - Petar opened it to field reports on
    # 2026-09-08 - but it may only change where a report actually landed.
    gz_after = {r["id"] for r in out if r.get("origin") == "pozarna_gz"}
    assert len(gz_after) == 99, len(gz_after)
    assert gz_after == (gz_before - {GZ_MOVED_FROM}) | {"coord_28.04297_43.28948"}
    gz_recs = {r["id"]: r for r in out if r.get("origin") == "pozarna_gz"}
    for rid, rec in gz_recs.items():
        if rid in GZ_TOUCHED:
            assert rec.get("existence_status") == "verified", rid
        else:
            assert rec == before_by_id[rid], ("untouched Golden Sands record moved", rid)
    assert sum(1 for r in gz_recs.values() if r.get("operational_status") == "works") == 3
    assert sum(1 for r in gz_recs.values() if r.get("operational_status") == "not_working") == 2

    # ---- Gate: the three wrong_location notes never reached the data ----
    for n in DROP_NOTE:
        dropped = next(r["comment"] for r in feed if r["issue_number"] == n)
        assert dropped, n
        for r in out:
            assert r.get("verifier_note") != dropped, (n, r["id"])

    # ---- Gate: published notes are clean text ----
    for r in out:
        note = r.get("verifier_note")
        if note:
            assert "\\" not in note, (r["id"], note)
            assert note == note.strip() and note, (r["id"], note)
    mojibake_scan("hydrants", out)
    mojibake_scan("provenance", state["provenance"])

    # ---- Provenance: the original wording, and the derived status ----
    by_issue = {r["issue_number"]: r for r in results}
    for n, (original, corrected) in SPELL.items():
        rid = by_issue[n]["target_id_after"]
        ref = make_source_ref(issue_number=n, report_type=by_issue[n]["report_type"],
                              old_id=None, old_coord=None, changes={}, old_values={},
                              approver_id=APPROVER, timestamp=timestamp)
        ref["manual_field"] = "note_spelling_fix"
        ref["old_value"] = original
        ref["new_value"] = corrected
        ref["merge_action"] = "note_spelling_fix"
        ref["attribution"] = (
            "Spelling corrected before ingest by {a} 2026-09-08 under the standing "
            "18.08 rule; the reporter's original wording is preserved here. Proven "
            "not to move any colour: the pipeline was run with and without the "
            "correction and the two results differ only in verifier_note."
        ).format(a=APPROVER)
        state["provenance"][rid]["source_refs"].append(ref)

    for n in DERIVE_WORKS:
        rid = by_issue[n]["target_id_after"]
        ref = make_source_ref(issue_number=n, report_type=by_issue[n]["report_type"],
                              old_id=None, old_coord=None, changes={}, old_values={},
                              approver_id=APPROVER, timestamp=timestamp)
        ref["manual_field"] = "derive_status_from_free_text"
        ref["old_value"] = None
        ref["new_value"] = "works"
        ref["merge_action"] = "derive_status_from_free_text"
        ref["attribution"] = (
            "operational_status was empty in the report; 'works' is DERIVED by {a} "
            "2026-09-08 from the reporter's own text \"Работи, но трудно се спира "
            "водата\", not submitted through the form. The note publishes as well, "
            "because it carries the valve warning on top of the status."
        ).format(a=APPROVER)
        state["provenance"][rid]["source_refs"].append(ref)

    # ---- Gate: the source file was never touched by the dry run ----
    assert hashlib.sha256(open(HYDRANTS, "rb").read()).hexdigest() == before_sha

    summary = build_report(build_reports(feed, with_spell=True), results,
                           approver_id=APPROVER, timestamp=timestamp,
                           input_count=EXPECTED_BEFORE, output_count=len(out))["summary"]
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    for r in results:
        print("  #{n} {t:<16} {a:<8} -> {i}".format(
            n=r["issue_number"], t=r["report_type"], a=r["action"], i=r["target_id_after"]))
    print("\n  spelling fixes proven note-only on {n} records:".format(n=len(note_only)))
    for rid, old, new in sorted(note_only):
        print("    {i}\n      - {o}\n      + {n}".format(i=rid, o=old, n=new))
    print("\n  wrong_location notes dropped: {d}".format(d=sorted(DROP_NOTE)))
    print()
    for k in EXPECTED_DELTA:
        print("  {k:<12} {b} -> {a}".format(k=k, b=before_counts[k], a=after_counts[k]))
    print("  {k:<12} {b} -> {a}".format(k="records", b=EXPECTED_BEFORE, a=len(out)))
    print("  Golden Sands  99 records, {v} verified ({w} works, {nw} not working)".format(
        v=sum(1 for r in gz_recs.values() if r.get("existence_status") == "verified"),
        w=sum(1 for r in gz_recs.values() if r.get("operational_status") == "works"),
        nw=sum(1 for r in gz_recs.values() if r.get("operational_status") == "not_working")))
    print("\nALL GATES PASSED")

    if not apply_writes:
        print("dry-run; nothing written (pass --apply to write)")
        return 0

    # Compact single-line JSON, as apply_approved_reports.py writes it; an
    # indent here would bury the real changes under a 300k-line diff (cycle #33).
    atomic_write_json(HYDRANTS, out)
    atomic_write_json(PROVENANCE, state["provenance"])
    print("WROTE", HYDRANTS, "and", PROVENANCE)

    stat = subprocess.run(["git", "diff", "--numstat", HYDRANTS, PROVENANCE],
                          capture_output=True, text=True, check=True).stdout
    print(stat, end="")
    for line in stat.strip().splitlines():
        added, removed, path = line.split("\t")
        assert int(added) <= 4 and int(removed) <= 4, (path, added, removed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--apply" in sys.argv))
