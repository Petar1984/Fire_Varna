#!/usr/bin/env python3
"""Cycle #33 adapter - issues #741-750.

Petar's Gate-1 decision (2026-09-05): the two near-match pairs are ONE hydrant
each, seen by two phones. In both pairs the record is kept at K. Raykov's
coordinate together with his note, and the Sluzhitel twin does not land:

    #743 superseded by #744   6.9 m apart, 58 s
    #746 superseded by #747   7.4 m apart, 27 s

Dropping the twin means neither report FLAGs - the survivor's nearest neighbour
is the pre-existing record 80 m / 244 m away - so no flag override is needed and
every record is still built by the sanctioned handler in hydrant_core.

A superseded report leaves no mark in the data by itself. Per the standing rule
that a no-op must be logged or a later reconciliation reads it as a missed
report, each survivor gets a `duplicate_report_superseded` provenance ref naming
the dropped issue and the reason.

Nothing is written unless every assertion below holds.
"""
from __future__ import annotations
import copy, hashlib, json, os, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.abspath("scripts"))
from lib.hydrant_core import (  # noqa: E402
    atomic_write_json, build_report, default_timestamp, ingested_issue_numbers,
    load_json, make_source_ref, mojibake_scan, process,
)

HYDRANTS = "data/hydrants.json"
PROVENANCE = "data/hydrants_provenance.json"
APPROVER = "petar"

# Gate-1: {dropped issue: (surviving issue, metres, seconds)}
SUPERSEDED = {743: (744, 6.9, 58), 746: (747, 7.4, 27)}

EXPECTED_APPLY = [741, 742, 744, 745, 747, 748, 749, 750]
EXPECTED_BEFORE = 7407
EXPECTED_AFTER = 7411
EXPECTED_TOUCHED = {
    "coord_27.90540_43.21059", "coord_27.94364_43.21543",
    "coord_27.94221_43.21850", "coord_27.94240_43.22267",
}
EXPECTED_DELTA = {  # measured in the read-only simulation
    "verified": (636, 644), "works": (95, 97), "not_working": (11, 11),
    "reported": (0, 0), "notes": (68, 71), "typed": (2724, 2732),
}


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


def main(apply_writes: bool) -> int:
    reports_path = sys.argv[sys.argv.index("--reports") + 1]
    feed = json.load(open(reports_path, encoding="utf-8"))["reports"]
    by_num = {r["issue_number"]: r for r in feed}

    # Feed in issue-number order; the superseded twins never reach process().
    reports = [by_num[n] for n in EXPECTED_APPLY]
    assert len(reports) == 8, len(reports)
    for dropped, (survivor, _, _) in SUPERSEDED.items():
        assert dropped in by_num and dropped not in EXPECTED_APPLY
        assert survivor in EXPECTED_APPLY

    before_bytes = open(HYDRANTS, "rb").read()
    before_sha = hashlib.sha256(before_bytes).hexdigest()
    records = json.loads(before_bytes.decode("utf-8"))
    provenance = load_json(PROVENANCE)
    assert len(records) == EXPECTED_BEFORE, len(records)
    before_counts = counts(records)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in records}
    gz_before = json.dumps([r for r in records if r.get("origin") == "pozarna_gz"],
                           ensure_ascii=False, sort_keys=True)

    timestamp = default_timestamp()
    state, results = process(reports, records, provenance,
                             timestamp=timestamp, approver_id=APPROVER)
    out = state["records"]

    # ---- Gate: the pipeline did exactly what was signed off ----
    actions = {r["issue_number"]: r["action"] for r in results}
    assert all(a == "applied" for a in actions.values()), actions
    assert sorted(actions) == EXPECTED_APPLY, sorted(actions)
    assert len(out) == EXPECTED_AFTER, len(out)
    assert sorted(ingested_issue_numbers(results)) == EXPECTED_APPLY

    after_counts = counts(out)
    for k, (exp_b, exp_a) in EXPECTED_DELTA.items():
        assert before_counts[k] == exp_b, (k, before_counts[k], exp_b)
        assert after_counts[k] == exp_a, (k, after_counts[k], exp_a)

    # ---- Gate: the superseded twins left NO record behind ----
    for dropped in SUPERSEDED:
        uid = by_num[dropped]["id"]
        hits = [r for r in out if uid in (r.get("legacy_ids") or [])
                or r.get("report_id") == uid]
        assert not hits, (dropped, [h["id"] for h in hits])

    # ---- Gate: only the intended pre-existing records changed ----
    touched = {r["target_id_after"] for r in results
               if r["report_type"] == "exists_confirmed"}
    assert touched == EXPECTED_TOUCHED, touched
    for r in out:
        old = before_by_id.get(r["id"])
        if old is not None and r["id"] not in touched:
            assert r == old, r["id"]

    # ---- Gate: Golden Sands stays exactly as Petar left it ----
    gz_after = [r for r in out if r.get("origin") == "pozarna_gz"]
    assert len(gz_after) == 99, len(gz_after)
    assert json.dumps(gz_after, ensure_ascii=False, sort_keys=True) == gz_before
    assert not any(r.get("existence_status") == "verified" for r in gz_after)

    # ---- Gate: published notes are clean text (escaped-quote / literal-\n bugs) ----
    for r in out:
        note = r.get("verifier_note")
        if note:
            assert "\\" not in note, (r["id"], note)
            assert note == note.strip() and note, (r["id"], note)
    mojibake_scan("hydrants", out)
    mojibake_scan("provenance", state["provenance"])

    # ---- Provenance: record WHY the two dropped reports never landed ----
    for dropped, (survivor, metres, seconds) in SUPERSEDED.items():
        rec_id = next(r["target_id_after"] for r in results
                      if r["issue_number"] == survivor)
        drop = by_num[dropped]
        ref = make_source_ref(
            issue_number=dropped, report_type=drop["report_type"],
            old_id=None, old_coord=None, changes={}, old_values={},
            approver_id=APPROVER, timestamp=timestamp,
        )
        ref["manual_field"] = "duplicate_report_superseded"
        ref["old_value"] = {
            "coords": drop["reported_coord"], "type": drop.get("type"),
            "operational_status": drop.get("operational_status"),
            "report_id": drop["id"], "reported_at": drop.get("reported_at"),
        }
        ref["new_value"] = None
        ref["merge_action"] = "duplicate_report_superseded"
        ref["attribution"] = (
            "Superseded by issue #{s}, decided by {a} 2026-09-05: the two reports "
            "are {m} m and {sec} s apart with the same hydrant type - one hydrant "
            "seen by two phones, not two hydrants. The record is kept at the "
            "coordinate of issue #{s} with its note; issue #{d} is not applied."
        ).format(s=survivor, a=APPROVER, m=metres, sec=seconds, d=dropped)
        state["provenance"][rec_id]["source_refs"].append(ref)

    for dropped, (survivor, _, _) in SUPERSEDED.items():
        rec_id = next(r["target_id_after"] for r in results
                      if r["issue_number"] == survivor)
        refs = state["provenance"][rec_id]["source_refs"]
        assert sum(x["issue_number"] == dropped for x in refs) == 1, rec_id
        assert sum(x["issue_number"] == survivor for x in refs) == 1, rec_id

    # ---- Gate: the source file was never touched by the dry run ----
    assert hashlib.sha256(open(HYDRANTS, "rb").read()).hexdigest() == before_sha

    summary = build_report(reports, results, approver_id=APPROVER,
                           timestamp=timestamp, input_count=EXPECTED_BEFORE,
                           output_count=len(out))["summary"]
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    for r in results:
        print("  #{n:>3} {t:<17} {a} -> {i}".format(
            n=r["issue_number"], t=r["report_type"], a=r["action"],
            i=r["target_id_after"]))
    for dropped, (survivor, m, s) in SUPERSEDED.items():
        print("  #{d:>3} {t:<17} superseded by #{s} ({m} m, {sec} s)".format(
            d=dropped, t="new_hydrant", s=survivor, m=m, sec=s))
    print()
    for k in EXPECTED_DELTA:
        print("  {k:<12} {b} -> {a}".format(k=k, b=before_counts[k], a=after_counts[k]))
    print("  {k:<12} {b} -> {a}".format(k="records", b=EXPECTED_BEFORE, a=len(out)))
    print("\nALL GATES PASSED")

    if not apply_writes:
        print("dry-run; nothing written (pass --apply to write)")
        return 0

    # Both data files are stored as compact single-line JSON, exactly as
    # apply_approved_reports.py writes them; only the run report is indented.
    # Passing indent here would reformat the whole file and bury eight real
    # changes under a 300k-line diff.
    atomic_write_json(HYDRANTS, out)
    atomic_write_json(PROVENANCE, state["provenance"])
    print("WROTE", HYDRANTS, "and", PROVENANCE)

    # ---- Gate: the diff must stay reviewable ----
    # A reformat is silent in the data but fatal to review, so measure it
    # rather than trusting the writer.
    import subprocess
    stat = subprocess.run(["git", "diff", "--numstat", HYDRANTS, PROVENANCE],
                          capture_output=True, text=True, check=True).stdout
    print(stat, end="")
    for line in stat.strip().splitlines():
        added, removed, path = line.split("\t")
        assert int(added) <= 4 and int(removed) <= 4, (path, added, removed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--apply" in sys.argv))
