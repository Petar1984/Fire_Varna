#!/usr/bin/env python3
"""Remove NAT-5345 (`coord_28.04427_43.29473`), reported missing in issue #762.

A `missing` report never deletes on its own - it only raises the yellow flag.
Deleting is Petar's manual call, and he made it on 2026-09-08 looking at the
flagged pin. This is the same shape as #491, #580 and #624: an institutional
reporter (Иван Драганов, 01 РСПБЗН) says the hydrant is not there, and Petar
chooses to trust him. The evidence here is firmer than in #758: he checked on
site AND asked the hotel owners, who confirmed there is none at that spot, so
nothing in the wording leaves room for a buried hydrant.

Not a duplicate: the nearest record is 38.3 m away, and it is the Golden Sands
hydrant the SAME reporter confirmed exists (but broken) in #763 - so he treated
the two as separate points on the same walk, and this one simply was not there.

The record keeps three ways back: the full copy in data/removed_hydrants.json,
the `manual_removal_reported_missing` ref left on its provenance entry, and git.
NAT-5345 travels with the archive copy only; it is not grafted onto a neighbour.

Nothing is written unless every assertion below holds.
"""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.abspath("scripts"))
from lib.hydrant_core import (  # noqa: E402
    atomic_write_json, default_timestamp, load_json, make_source_ref, mojibake_scan,
)

HYDRANTS = "data/hydrants.json"
PROVENANCE = "data/hydrants_provenance.json"
ARCHIVE = "data/removed_hydrants.json"
APPROVER = "petar"

TARGET = "coord_28.04427_43.29473"
ISSUE = 762
EXPECTED_BEFORE = 7412
EXPECTED_AFTER = 7411
EXPECTED_ARCHIVE_BEFORE = 38
# The record is yellow, carries a note and a type; it was never verified and
# has no operational status, so only these three counters may move.
EXPECTED_DELTA = {
    "verified": (657, 657), "works": (106, 106), "not_working": (13, 13),
    "reported": (1, 0), "notes": (80, 79), "typed": (2740, 2739),
}
REASON = (
    "Докладван като липсващ от 01 РСПБЗН (#762): „При проверка не е намерен такъв "
    "хидрант. Собствениците на хотела твърдят, че няма такъв на посоченото място.“ "
    "Не е дубликат — най-близкият съсед е на 38.3 м и е хидрантът от Златни "
    "пясъци, който СЪЩИЯТ докладчик потвърди в #763 като съществуващ (неработещ), "
    "тоест е третирал двете точки като различни на един и същи обход. Формата е "
    "като при #491, #580, #624 и #758, но доказателството тук е по-твърдо: освен "
    "проверката на място има и потвърждение от собствениците на хотела, и нищо в "
    "текста не допуска „затрупан“. NAT-5345 остава само в този архив и НЕ се "
    "прехвърля към съсед."
)


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
    before_bytes = open(HYDRANTS, "rb").read()
    before_sha = hashlib.sha256(before_bytes).hexdigest()
    records = json.loads(before_bytes.decode("utf-8"))
    provenance = load_json(PROVENANCE)
    archive = load_json(ARCHIVE)
    assert len(records) == EXPECTED_BEFORE, len(records)
    assert len(archive["removed"]) == EXPECTED_ARCHIVE_BEFORE, len(archive["removed"])

    hits = [r for r in records if r["id"] == TARGET]
    assert len(hits) == 1, len(hits)
    victim = copy.deepcopy(hits[0])
    assert victim.get("review_status") == "reported", victim
    assert victim.get("legacy_ids") == ["NAT-5345"], victim
    before_counts = counts(records)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in records}

    out = [r for r in records if r["id"] != TARGET]
    assert len(out) == EXPECTED_AFTER, len(out)

    # ---- Gate: exactly one record left, every other one byte-identical ----
    assert set(before_by_id) - {r["id"] for r in out} == {TARGET}
    for r in out:
        assert r == before_by_id[r["id"]], r["id"]

    after_counts = counts(out)
    for k, (exp_b, exp_a) in EXPECTED_DELTA.items():
        assert before_counts[k] == exp_b, (k, before_counts[k], exp_b)
        assert after_counts[k] == exp_a, (k, after_counts[k], exp_a)

    timestamp = default_timestamp()

    # ---- The archive: the whole record, and why it went ----
    archive["removed"].append({
        "issue_number": ISSUE,
        "removed_at": timestamp,
        "reason": REASON,
        "record": victim,
    })
    assert len(archive["removed"]) == EXPECTED_ARCHIVE_BEFORE + 1
    assert archive["removed"][-1]["record"] == victim

    # ---- Provenance: the entry stays, and says the record was removed ----
    assert TARGET in provenance, "no provenance entry to mark"
    ref = make_source_ref(issue_number=ISSUE, report_type="missing",
                          old_id=TARGET, old_coord=list(victim["coords"]),
                          changes={}, old_values={},
                          approver_id=APPROVER, timestamp=timestamp)
    ref["manual_field"] = "removed"
    ref["old_value"] = None
    ref["new_value"] = "removed"
    ref["merge_action"] = "manual_removal_reported_missing"
    ref["attribution"] = "Removed by {a} 2026-09-08 from issue #{i}. {r}".format(
        a=APPROVER, i=ISSUE, r=REASON)
    provenance[TARGET]["source_refs"].append(ref)
    assert sum(1 for x in provenance[TARGET]["source_refs"]
               if x.get("manual_field") == "removed") == 1

    mojibake_scan("hydrants", out)
    mojibake_scan("archive", archive)
    mojibake_scan("provenance", provenance)
    assert hashlib.sha256(open(HYDRANTS, "rb").read()).hexdigest() == before_sha

    print("REMOVING", TARGET, "(NAT-5345, подземен, yellow)")
    print("  note was:", victim.get("verifier_note"))
    print("  records  ", EXPECTED_BEFORE, "->", len(out))
    for k in EXPECTED_DELTA:
        print("  %-12s %s -> %s" % (k, before_counts[k], after_counts[k]))
    print("  archive  ", EXPECTED_ARCHIVE_BEFORE, "->", len(archive["removed"]))
    print("\nALL GATES PASSED")

    if not apply_writes:
        print("dry-run; nothing written (pass --apply to write)")
        return 0

    atomic_write_json(HYDRANTS, out)
    atomic_write_json(PROVENANCE, provenance)
    # The archive is stored with indent=1 — measured, not assumed: only that
    # value round-trips the HEAD blob byte-identically. The two data files stay
    # compact. Getting this wrong reformats the file and buries the change.
    atomic_write_json(ARCHIVE, archive, indent=1)
    print("WROTE", HYDRANTS, PROVENANCE, ARCHIVE)

    stat = subprocess.run(["git", "diff", "--numstat", HYDRANTS, PROVENANCE, ARCHIVE],
                          capture_output=True, text=True, check=True).stdout
    print(stat, end="")
    limits = {HYDRANTS: 4, PROVENANCE: 4, ARCHIVE: 40}  # the archive appends a block
    for line in stat.strip().splitlines():
        added, removed, path = line.split("\t")
        cap = limits[path.replace("\\", "/")]
        assert int(added) <= cap and int(removed) <= 4, (path, added, removed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--apply" in sys.argv))
