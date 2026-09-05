#!/usr/bin/env python3
"""Cycle #34 adapter - issue #751.

One exists_confirmed from Petar on a grey ВиК record whose existence_status,
type and operational_status were all empty, so the confirmation types it and
turns it green in a single step. No note, no near-match, no override table -
the shape to aim for.

Petar's approval in chat is Gate 1; the `approved` label is not used on this
route, so the report is taken from the Worker's normalized feed and fed to the
sanctioned handler in hydrant_core.

Nothing is written unless every assertion below holds.
"""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.abspath("scripts"))
from lib.hydrant_core import (  # noqa: E402
    atomic_write_json, build_report, default_timestamp, ingested_issue_numbers,
    load_json, mojibake_scan, process,
)

HYDRANTS = "data/hydrants.json"
PROVENANCE = "data/hydrants_provenance.json"
APPROVER = "petar"

EXPECTED_APPLY = [751]
EXPECTED_TOUCHED = {"coord_27.92250_43.22347"}
EXPECTED_COUNT = 7411          # unchanged: a confirmation adds no record
EXPECTED_DELTA = {             # measured in the read-only simulation
    "verified": (644, 645), "works": (97, 97), "not_working": (11, 11),
    "reported": (0, 0), "notes": (71, 71), "typed": (2732, 2733),
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
    reports = sorted(feed, key=lambda r: r["issue_number"])
    assert [r["issue_number"] for r in reports] == EXPECTED_APPLY, reports

    before_bytes = open(HYDRANTS, "rb").read()
    before_sha = hashlib.sha256(before_bytes).hexdigest()
    records = json.loads(before_bytes.decode("utf-8"))
    provenance = load_json(PROVENANCE)
    assert len(records) == EXPECTED_COUNT, len(records)
    before_counts = counts(records)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in records}
    gz_before = json.dumps([r for r in records if r.get("origin") == "pozarna_gz"],
                           ensure_ascii=False, sort_keys=True)

    timestamp = default_timestamp()
    state, results = process(reports, records, provenance,
                             timestamp=timestamp, approver_id=APPROVER)
    out = state["records"]

    # ---- Gate: the pipeline did exactly what was signed off ----
    assert all(r["action"] == "applied" for r in results), results
    assert sorted(ingested_issue_numbers(results)) == EXPECTED_APPLY
    assert len(out) == EXPECTED_COUNT, len(out)

    after_counts = counts(out)
    for k, (exp_b, exp_a) in EXPECTED_DELTA.items():
        assert before_counts[k] == exp_b, (k, before_counts[k], exp_b)
        assert after_counts[k] == exp_a, (k, after_counts[k], exp_a)

    # ---- Gate: only the intended record changed ----
    touched = {r["target_id_after"] for r in results}
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

    # ---- Gate: published notes stay clean text ----
    for r in out:
        note = r.get("verifier_note")
        if note:
            assert "\\" not in note, (r["id"], note)
            assert note == note.strip() and note, (r["id"], note)
    mojibake_scan("hydrants", out)
    mojibake_scan("provenance", state["provenance"])

    # ---- Gate: the source file was never touched by the dry run ----
    assert hashlib.sha256(open(HYDRANTS, "rb").read()).hexdigest() == before_sha

    summary = build_report(reports, results, approver_id=APPROVER,
                           timestamp=timestamp, input_count=EXPECTED_COUNT,
                           output_count=len(out))["summary"]
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    for r in results:
        print("  #{n} {t} {a} -> {i}".format(
            n=r["issue_number"], t=r["report_type"], a=r["action"],
            i=r["target_id_after"]))
        print("     ", json.dumps(r["changes"], ensure_ascii=False))
    print()
    for k in EXPECTED_DELTA:
        print("  {k:<12} {b} -> {a}".format(k=k, b=before_counts[k], a=after_counts[k]))
    print("  {k:<12} {b} -> {a}".format(k="records", b=EXPECTED_COUNT, a=len(out)))
    print("\nALL GATES PASSED")

    if not apply_writes:
        print("dry-run; nothing written (pass --apply to write)")
        return 0

    # Both data files are stored as compact single-line JSON; passing indent
    # would reformat the whole file and bury one real change under a 300k-line
    # diff (cycle #33). The numstat gate below measures that rather than
    # trusting the writer.
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
