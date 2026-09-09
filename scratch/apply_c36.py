#!/usr/bin/env python3
"""Cycle #36 - issues #770-777, then the removal Petar asked for in #775.

Gate 1 (2026-09-09): "действай както е отбелязано в докладите".
  * All five notes are questions to the moderator or instructions, not
    landmarks, so none of them publish. Their answers went into the chat.
  * #772 is applied LITERALLY as a wrong_location move, per his instruction,
    even though the destination lands 2.8 m from #771's record - I offered the
    duplicate reading and he chose the literal one.
  * #775 is a `missing` report whose note says "Премахни този". The flag alone
    never deletes; the removal below is his manual call. The record carries
    ВиК 269 + an ETR key while the survivor is the national one, which reverses
    the usual preference - flagged to him, and he confirmed.
"""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.abspath("scripts"))
from lib.hydrant_core import (atomic_write_json, default_timestamp,
                              ingested_issue_numbers, load_json,
                              make_source_ref, mojibake_scan, process)

H, P, A = "data/hydrants.json", "data/hydrants_provenance.json", "data/removed_hydrants.json"
APPROVER = "petar"
ISSUES = list(range(770, 778))
VICTIM, VICTIM_ISSUE = "coord_27.88273_43.21143", 775
BEFORE, AFTER = 7411, 7410
DELTA = {"verified": (657, 664), "works": (106, 108), "not_working": (13, 13),
         "reported": (0, 0), "notes": (79, 79), "typed": (2739, 2743)}
ARCH_BEFORE = 39
REASON = (
    "Докладван като дубликат от Петър (#775): „Хидранта е дублиран с този до спирка "
    "звезда. Това е дубликата, за предният вече подадох сигнал. Премахни този.“ "
    "Оцелелият е coord_27.88301_43.21144 на 22.9 м, за който Петър подаде #774 в "
    "същата минута. ⚠️ Обратно на обичайното: тук отпада ВиК записът (269 + "
    "etr_varna:27.88272757,43.21142958), а остава националният — показано му беше "
    "изрично преди решението и той потвърди „действай както е отбелязано в "
    "докладите“. Двата номера остават само в този архив."
)

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
    reps = [{**r, "comment": None} for r in sorted(feed, key=lambda x: x["issue_number"])]
    assert [r["issue_number"] for r in reps] == ISSUES

    raw = open(H, "rb").read(); sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8")); prov = load_json(P); arch = load_json(A)
    assert len(recs) == BEFORE and len(arch["removed"]) == ARCH_BEFORE
    before = counts(recs); before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}

    ts = default_timestamp()
    state, res = process(reps, recs, prov, timestamp=ts, approver_id=APPROVER)
    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    out = state["records"]; assert len(out) == BEFORE

    # no note may reach the data this cycle
    for r in out:
        n = r.get("verifier_note")
        if n:
            assert r["id"] in before_by_id and before_by_id[r["id"]].get("verifier_note") == n, r["id"]

    # ---- the removal Petar asked for in #775 ----
    hits = [r for r in out if r["id"] == VICTIM]; assert len(hits) == 1
    victim = copy.deepcopy(hits[0])
    assert victim.get("review_status") == "reported", victim
    assert victim.get("legacy_ids") == ["269", "etr_varna:27.88272757,43.21142958"], victim
    out = [r for r in out if r["id"] != VICTIM]
    assert len(out) == AFTER

    after = counts(out)
    for k, (b, a) in DELTA.items():
        assert before[k] == b, (k, before[k], b)
        assert after[k] == a, (k, after[k], a)

    arch["removed"].append({"issue_number": VICTIM_ISSUE, "removed_at": ts,
                            "reason": REASON, "record": victim})
    ref = make_source_ref(issue_number=VICTIM_ISSUE, report_type="missing",
                          old_id=VICTIM, old_coord=list(victim["coords"]),
                          changes={}, old_values={}, approver_id=APPROVER, timestamp=ts)
    ref.update(manual_field="removed", old_value=None, new_value="removed",
               merge_action="manual_removal_duplicate",
               attribution="Removed by %s 2026-09-09 from issue #%d. %s" % (APPROVER, VICTIM_ISSUE, REASON))
    state["provenance"][VICTIM]["source_refs"].append(ref)

    mojibake_scan("h", out); mojibake_scan("a", arch); mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied:", sorted(ingested_issue_numbers(res)))
    print("removed:", VICTIM, victim.get("legacy_ids"))
    for k in DELTA: print("  %-12s %s -> %s" % (k, before[k], after[k]))
    print("  %-12s %s -> %s" % ("records", BEFORE, len(out)))
    print("  %-12s %s -> %s" % ("archive", ARCH_BEFORE, len(arch["removed"])))
    print("\nALL GATES PASSED")
    if not write:
        print("dry-run"); return 0
    atomic_write_json(H, out); atomic_write_json(P, state["provenance"])
    atomic_write_json(A, arch, indent=1)          # the archive is indent=1
    stat = subprocess.run(["git", "diff", "--numstat", H, P, A],
                          capture_output=True, text=True, check=True).stdout
    print(stat, end="")
    caps = {H: 4, P: 4, A: 40}
    for line in stat.strip().splitlines():
        add, rem, path = line.split("\t")
        assert int(add) <= caps[path.replace("\\", "/")] and int(rem) <= 4, line
    return 0

if __name__ == "__main__":
    raise SystemExit(main("--apply" in sys.argv))
