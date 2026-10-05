#!/usr/bin/env python3
"""Cycle #50 - issue #899, a relocation, then one duplicate removed.

Gate 1 (2026-10-05):
  * #899 wrong_location on ВиК VIK-VARNA_IZTOK-0164 (+ ETR), grey and untyped:
    moved 15.4 m to the stairs that lead down to the boulevard pavement,
    verified, надземен, not tested -> red. The note is a landmark and
    publishes, with the comma before the relative clause added ("до
    стълбището, което слиза ...") - proven differentially.
  * The moved pin landed 18.2 m from ВиК 569 (+ ETR), grey and untyped. Asked
    whether there are one or two hydrants there, Petar answered: "същият
    хидрант е - премахни другият който е на 18 метра". So 569 is removed and
    archived whole; its numbers live on in the archive.
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
ISSUES = [899]
WORKER_FIELDS = ("issue_number", "id", "report_type", "reported_at", "hydrant_id",
                 "reported_coord", "type", "operational_status", "comment")

TARGET_BEFORE = "coord_27.90865_43.21910"
TARGET_AFTER = "coord_27.90846_43.21913"
NEW_COORD = [27.908465, 43.21913]
NOTE_RAW = "Хидрантът се намира до стълбището което слиза към тротоара на булеварда"
NOTE = "Хидрантът се намира до стълбището, което слиза към тротоара на булеварда"

REMOVE_ID = "coord_27.90846_43.21929"
REMOVE_REASON = (
    "Дубликат на coord_27.90846_43.21913 (VIK-VARNA_IZTOK-0164), който Петър премести "
    "с #899 до стълбището към тротоара на булеварда. Новата точка падна на 18.2 м от този "
    "запис; попитан дали там има един или два хидранта, Петър отговори: „същият хидрант е "
    "— премахни другият който е на 18 метра“. Записът беше сив и без тип. Номерата 569 и "
    "etr_varna:27.90845834,43.21929273 остават само в този архив.")

BEFORE, AFTER, ARCH_BEFORE = 7411, 7410, 53
DELTA = {"verified": (767, 768), "works": (121, 121), "not_working": (17, 17),
         "reported": (0, 0), "notes": (95, 96), "typed": (2802, 2803)}


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
    for r in feed:
        r = {k: copy.deepcopy(r.get(k)) for k in WORKER_FIELDS}
        assert r["comment"] == NOTE_RAW, repr(r["comment"])
        r["comment"] = NOTE if corrected else NOTE_RAW
        out.append(r)
    return out


def main(write: bool) -> int:
    feed = json.load(open(sys.argv[sys.argv.index("--reports") + 1], encoding="utf-8"))["reports"]
    assert [r["issue_number"] for r in feed] == ISSUES, [r["issue_number"] for r in feed]
    f = feed[0]
    assert f["report_type"] == "wrong_location" and f["hydrant_id"] == TARGET_BEFORE
    assert f["reported_coord"] == NEW_COORD and f["type"] == "надземен"
    assert f["operational_status"] == "not_tested"

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    arch = load_json(A)
    assert len(recs) == BEFORE and len(arch["removed"]) == ARCH_BEFORE
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    gone = before_by_id[REMOVE_ID]
    assert gone["legacy_ids"][0] == "569"
    assert gone.get("existence_status") is None and gone.get("type") is None
    assert not gone.get("verifier_note") and not gone.get("address")
    assert not before_by_id[TARGET_BEFORE].get("address")
    ts = default_timestamp()

    # ---- differential proof: only the note may differ ----
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
    assert differ == [TARGET_AFTER], differ
    assert counts(plain["records"]) == counts(state["records"])

    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    r0 = res[0]
    assert r0["target_id_before"] == TARGET_BEFORE and r0["target_id_after"] == TARGET_AFTER
    out = state["records"]
    by = {r["id"]: r for r in out}
    hit = by[TARGET_AFTER]
    assert hit["coords"] == NEW_COORD
    assert (hit["existence_status"], hit["type"], hit["operational_status"], hit["verifier_note"]) == \
        ("verified", "надземен", "not_tested", NOTE)
    # the move keeps every registry key and adds the retired id as an alias
    assert {TARGET_BEFORE, "VIK-VARNA_IZTOK-0164",
            "etr_varna:27.90865249,43.21910371"} <= set(hit["legacy_ids"]), hit["legacy_ids"]

    # ---- the duplicate, on Petar's word ----
    v = by[REMOVE_ID]
    assert v == before_by_id[REMOVE_ID], "the duplicate must be untouched before removal"
    arch["removed"].append({"issue_number": 899, "removed_at": ts,
                            "reason": REMOVE_REASON, "record": copy.deepcopy(v)})
    ref = make_source_ref(issue_number=899, report_type="wrong_location", old_id=REMOVE_ID,
                          old_coord=list(v["coords"]), changes={}, old_values={},
                          approver_id=APPROVER, timestamp=ts)
    ref.update(manual_field="removed", old_value=None, new_value="removed",
               merge_action="manual_removal_duplicate",
               attribution="Removed by {a} 2026-10-05 after issue #899. {r}".format(
                   a=APPROVER, r=REMOVE_REASON))
    state["provenance"][REMOVE_ID]["source_refs"].append(ref)
    out = [r for r in out if r["id"] != REMOVE_ID]
    assert len(out) == AFTER and len(arch["removed"]) == ARCH_BEFORE + 1

    fix = make_source_ref(issue_number=899, report_type="wrong_location", old_id=None,
                          old_coord=None, changes={}, old_values={},
                          approver_id=APPROVER, timestamp=ts)
    fix.update(manual_field="note_spelling_fix", old_value=NOTE_RAW, new_value=NOTE,
               merge_action="note_spelling_fix",
               attribution=("Spelling corrected before ingest by {a} 2026-10-05 under the "
                            "standing 18.08 rule (comma before the relative clause); the "
                            "reporter's original wording is preserved here.").format(a=APPROVER))
    state["provenance"][TARGET_AFTER]["source_refs"].append(fix)

    # nothing else moved
    for r in out:
        if r["id"] != TARGET_AFTER:
            assert r == before_by_id[r["id"]], r["id"]
    assert set(before_by_id) - {r["id"] for r in out} == {TARGET_BEFORE, REMOVE_ID}
    assert {r["id"] for r in out} - set(before_by_id) == {TARGET_AFTER}

    after = counts(out)
    for k, (bb, aa) in DELTA.items():
        assert before[k] == bb, (k, before[k], bb)
        assert after[k] == aa, (k, after[k], aa)
    blob = json.dumps(out, ensure_ascii=False) + json.dumps(state["provenance"], ensure_ascii=False)
    for name in {x["reporter"].strip() for x in feed if x.get("reporter")}:
        assert ('"%s"' % name) not in blob, "reporter name reached the data as a value"
    mojibake_scan("h", out)
    mojibake_scan("a", arch)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied #899 (moved 15.4 m, note fixed - proven) | removed duplicate ВиК 569")
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
