#!/usr/bin/env python3
"""Cycle #42 - issues #864-867 (4 reports), then one removal.

Three confirmations on grey records and one duplicate cleanup.

Gate 1 (2026-09-21, "давай" on the full board):
  * #864 -> remove `coord_27.89809_43.21850` (ВиК 741 + ETR key). Petar's note:
    "Дублиран с този на ъгъла на гранд мол. Премахни този". The twin sits 6.8 m
    away and the next neighbour is 40.9 m out, so the pair really is alone: two
    consecutive ВиК numbers (740 and 741) on one address, ул. "Атанас Христов"
    - one hydrant entered twice by the registry. Both carry an ETR key, so the
    usual preference does not decide it; what does is which record holds more
    truth. The survivor is verified on site and typed надземен, this one an
    empty grey row. Same reasoning as #832 in cycle #40.
  * #865, #866, #867 -> plain confirmations, no notes, no near-matches, every
    target grey before the batch.
  * #867 is the first report from **Пламен Тодоров**, the campaign's 35th
    reporter, and it is in Provadia rather than Varna. The record (NAT-7108)
    already carried type=подземен, so the report cross-checks the type and adds
    what the import never had: that the hydrant gives water.

No note publishes. #864's is moderator-facing - it tells the moderator what to
delete, and once the deletion is applied it is also false.
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
ISSUES = [864, 865, 866, 867]
KEEP_NOTE: set[int] = set()          # nothing publishes this cycle
NOTE_864 = "Дублиран с този на ъгъла на гранд мол.\nПремахни този"

REMOVE = {
    "coord_27.89809_43.21850": (864, "manual_removal_duplicate",
        "Дубликат на coord_27.89802_43.21854 на 6.8 м. Бележката на Петър в #864: "
        "„Дублиран с този на ъгъла на гранд мол. Премахни този.“ Двата записа носят "
        "последователни ВиК номера — 740 и 741 — на един и същ адрес, ул. „Атанас "
        "Христов“, тоест регистърът е вписал един хидрант два пъти. Следващият съсед е "
        "чак на 40.9 м, така че двойката наистина е сама. И двата носят ЕТР ключ, "
        "затова обичайното предпочитание не решава; решава кой запис носи повече "
        "истина: оцелелият е проверен на място и типизиран надземен, а този е празен "
        "сив ред без тип — същото основание като при #832. Номерът 741 и "
        "etr_varna:27.89808810,43.21850262 остават само в този архив."),
}

BEFORE, AFTER, ARCH_BEFORE = 7400, 7399, 51
DELTA = {"verified": (744, 747), "works": (112, 113), "not_working": (16, 16),
         "reported": (0, 0), "notes": (86, 86), "typed": (2780, 2782)}


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
    assert sorted(r["issue_number"] for r in feed) == ISSUES

    # The note must reach the adapter unescaped, or dropping it would be the
    # only reason a backslash never hit the map (the #685 bug).
    raw864 = next(r for r in feed if r["issue_number"] == 864)["comment"]
    assert raw864 == NOTE_864, repr(raw864)
    assert "\\" not in raw864 and "\n" in raw864

    reps = []
    for r in sorted(feed, key=lambda x: x["issue_number"]):
        r = copy.deepcopy(r)
        if r["issue_number"] not in KEEP_NOTE:
            r["comment"] = None
        reps.append(r)
    assert not any(r.get("comment") for r in reps), "no note publishes this cycle"

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    arch = load_json(A)
    assert len(recs) == BEFORE and len(arch["removed"]) == ARCH_BEFORE
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}

    ts = default_timestamp()
    state, res = process(reps, recs, prov, timestamp=ts, approver_id=APPROVER)
    out = state["records"]
    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    assert len(out) == BEFORE, len(out)          # confirmations add no records

    # every report landed on the record the board named, and on no other
    TARGETS = {864: "coord_27.89809_43.21850", 865: "coord_27.90983_43.21930",
               866: "coord_27.88983_43.21303", 867: "coord_27.44283_43.16538"}
    for r in res:
        assert r["target_id_after"] == TARGETS[r["issue_number"]], r
        assert r["target_id_before"] == r["target_id_after"], r
    touched = set(TARGETS.values())
    for r in out:
        if r["id"] not in touched:
            assert r == before_by_id[r["id"]], r["id"]

    # the three confirmations land exactly the values the reports carried
    by = {r["id"]: r for r in out}
    for n, want_type, want_op in ((865, "надземен", "not_tested"),
                                  (866, "подземен", "not_tested"),
                                  (867, "подземен", "works")):
        rec = by[TARGETS[n]]
        assert rec.get("existence_status") == "verified", (n, rec.get("existence_status"))
        assert rec.get("type") == want_type, (n, rec.get("type"))
        assert rec.get("operational_status") == want_op, (n, rec.get("operational_status"))
        assert rec.get("review_status") is None, (n, rec.get("review_status"))
    # #867's record was already typed подземен: a cross-check, never a rewrite
    assert before_by_id[TARGETS[867]].get("type") == "подземен"

    # ---- the removal ----
    for rid, (issue, action, reason) in REMOVE.items():
        v = by.get(rid)
        assert v is not None, rid
        assert v.get("review_status") == "reported", (rid, v.get("review_status"))
        assert v.get("verifier_note") is None, "the dropped note must not have landed"
        arch["removed"].append({"issue_number": issue, "removed_at": ts,
                                "reason": reason, "record": copy.deepcopy(v)})
        ref = make_source_ref(issue_number=issue, report_type="missing", old_id=rid,
                              old_coord=list(v["coords"]), changes={}, old_values={},
                              approver_id=APPROVER, timestamp=ts)
        ref.update(manual_field="removed", old_value=None, new_value="removed",
                   merge_action=action,
                   attribution="Removed by {a} 2026-09-21 from issue #{i}. {r}".format(
                       a=APPROVER, i=issue, r=reason))
        state["provenance"][rid]["source_refs"].append(ref)
    out = [r for r in out if r["id"] not in REMOVE]
    assert len(out) == AFTER, len(out)
    assert len(arch["removed"]) == ARCH_BEFORE + 1

    # the twin the removal keeps is untouched and still the verified one
    twin = next(r for r in out if r["id"] == "coord_27.89802_43.21854")
    assert twin == before_by_id["coord_27.89802_43.21854"]
    assert twin.get("existence_status") == "verified" and twin.get("type") == "надземен"

    after = counts(out)
    for k, (b, a) in DELTA.items():
        assert before[k] == b, (k, before[k], b)
        assert after[k] == a, (k, after[k], a)

    # the only id that vanished is the removal
    assert set(before_by_id) - {r["id"] for r in out} == set(REMOVE)
    # not one note changed anywhere
    for r in out:
        assert r.get("verifier_note") == before_by_id[r["id"]].get("verifier_note"), r["id"]
    # the dropped note reached no record at all
    for r in out:
        assert r.get("verifier_note") != NOTE_864, r["id"]

    mojibake_scan("h", out)
    mojibake_scan("a", arch)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied %d reports | removed %d | published notes: 0" % (len(res), len(REMOVE)))
    for k in DELTA:
        print("  %-12s %s -> %s" % (k, before[k], after[k]))
    print("  %-12s %s -> %s" % ("records", BEFORE, len(out)))
    print("  %-12s %s -> %s" % ("grey", BEFORE - before["verified"], len(out) - after["verified"]))
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
