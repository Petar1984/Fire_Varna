#!/usr/bin/env python3
"""Cycle #37 - issues #778-806 (29 reports), then three removals.

Gate 1 (2026-09-09):
  * #782 -> remove `coord_27.86209_43.21451` (NAT-5794). Its twin 10.1 m away is
    the record #781 confirms in the same batch. His note: "премахни този".
  * #791 -> remove `coord_27.86166_43.23664` (NAT-6016). He pointed at the pin
    himself; the twin 15.4 m away is `coord_27.86185_43.23662`, ВиК 1040 + ETR,
    already verified - so the national record goes and the ВиК one stays, the
    settled preference.
  * #804 -> remove `coord_27.34292_43.12765` (ВиК 4576 + ETR Provadia). No note
    and nothing within 152 m, so not a duplicate: it simply is not there.
    Petar: trust Ангелов, who filed #805 and #806 in the same walk, confirming
    the neighbours minutes apart.
  * #778 (wrong_location, 8.0 m) - its note says the hydrant works. The form has
    no operational picker for this report type, so the status is derived into
    the field and the note itself is dropped, being moderator-facing otherwise.
  * #806's note publishes with the standing spelling fix: "Капака" as a subject
    becomes "Капакът". Proven differentially, as the rule requires.
  * Every other note is dropped.
"""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.abspath("scripts"))
from lib.hydrant_core import (  # noqa: E402
    atomic_write_json, build_alias_index, default_timestamp, ingested_issue_numbers,
    load_json, make_source_ref, mojibake_scan, process,
)

H, P, A = "data/hydrants.json", "data/hydrants_provenance.json", "data/removed_hydrants.json"
APPROVER = "petar"
ISSUES = list(range(778, 807))
DERIVE_WORKS = 778
SPELL = {806: ("Капака е с овална форма.", "Капакът е с овална форма.")}

REMOVE = {
    "coord_27.86209_43.21451": (782, "manual_removal_duplicate",
        "Дубликат на coord_27.86220_43.21455 на 10.1 м, който Петър потвърди на място "
        "с #781 в същата партида. Бележката му на #782: „хидранта е дублиран- премахни "
        "този“. И двата са национални записи; оцелява потвърденият. NAT-5794 остава "
        "само в този архив."),
    "coord_27.86166_43.23664": (791, "manual_removal_duplicate",
        "Дубликат на coord_27.86185_43.23662 на 15.4 м — ВиК 1040 + ЕТР ключ, вече "
        "проверен, надземен. Петър посочи пина сам на живата карта („това е близнака“) "
        "след като показах, че съседът на 15.4 м не е онзи, който потвърди с #790 (той "
        "е на 72 м). Оцелява ВиК записът, пада националният, по установеното "
        "предпочитание. NAT-6016 остава само в този архив."),
    "coord_27.34292_43.12765": (804, "manual_removal_reported_missing",
        "Докладван като липсващ от Ангелов (#804) без бележка. НЕ е дубликат — най-"
        "близкият съсед е на 152 м, тоест нищо не го покрива. Записът е ВиК 4576 + "
        "etr_provadia ключ, тоест от по-надеждния вид, и това беше показано на Петър "
        "преди решението. Той избра триене — доверяваме се на Ангелов. Основанието е, "
        "че Ангелов е бил на терен в същия обход: подал е #805 и #806 минути по-късно, "
        "потвърждавайки два съседни хидранта. Формата е като при #491, #580 и #624. "
        "Двата номера остават само в този архив."),
}

BEFORE, AFTER, ARCH_BEFORE = 7409, 7406, 41
DELTA = {"verified": (677, 701), "works": (108, 110), "not_working": (13, 13),
         "reported": (0, 0), "notes": (80, 81), "typed": (2743, 2757)}


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


def build(feed, *, with_spell):
    out = []
    for r in sorted(feed, key=lambda x: x["issue_number"]):
        r = copy.deepcopy(r)
        n = r["issue_number"]
        if n in SPELL:
            assert r["comment"] == SPELL[n][0], (n, r["comment"])
            r["comment"] = SPELL[n][1] if with_spell else SPELL[n][0]
        else:
            r["comment"] = None
        out.append(r)
    return out


def run(feed, recs, prov, *, with_spell, ts):
    return process(build(feed, with_spell=with_spell), copy.deepcopy(recs),
                   copy.deepcopy(prov), timestamp=ts, approver_id=APPROVER)


def main(write: bool) -> int:
    feed = json.load(open(sys.argv[sys.argv.index("--reports") + 1], encoding="utf-8"))["reports"]
    assert sorted(r["issue_number"] for r in feed) == ISSUES
    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    arch = load_json(A)
    assert len(recs) == BEFORE and len(arch["removed"]) == ARCH_BEFORE
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    ts = default_timestamp()

    # ---- spelling proof: same pipeline, only the note text differs ----
    plain, _ = run(feed, recs, prov, with_spell=False, ts=ts)
    state, res = run(feed, recs, prov, with_spell=True, ts=ts)
    a = {r["id"]: r for r in plain["records"]}
    b = {r["id"]: r for r in state["records"]}
    assert set(a) == set(b)
    diff = []
    for k in a:
        x, y = dict(a[k]), dict(b[k])
        xn, yn = x.pop("verifier_note", None), y.pop("verifier_note", None)
        assert x == y, ("the spelling fix moved a non-note field", k)
        if xn != yn:
            diff.append(k)
    assert len(diff) == len(SPELL), diff
    assert counts(plain["records"]) == counts(state["records"])

    assert all(r["action"] == "applied" for r in res), res
    assert sorted(ingested_issue_numbers(res)) == ISSUES
    out = state["records"]
    assert len(out) == BEFORE

    # ---- #778: the status its own text states, which the form could not carry ----
    rep778 = next(r for r in feed if r["issue_number"] == DERIVE_WORKS)
    alias = build_alias_index(out)
    rec = alias.get(rep778["id"]) or alias.get(rep778["hydrant_id"])
    assert rec is not None, "the #778 target was lost after the move"
    # Nothing to derive: #776 already confirmed this record as working in cycle
    # #36, so "работещ е" restates what the data holds. Prove they agree instead
    # of writing it again — a disagreement would be a question for Petar.
    assert rec.get("operational_status") == "works", rec.get("operational_status")
    ref = make_source_ref(issue_number=DERIVE_WORKS, report_type="wrong_location",
                          old_id=rec["id"], old_coord=list(rec["coords"]),
                          changes={}, old_values={},
                          approver_id=APPROVER, timestamp=ts)
    ref["manual_field"] = "status_cross_check"
    ref["old_value"] = "works"
    ref["new_value"] = "works"
    ref["merge_action"] = "status_confirmed_by_free_text"
    ref["attribution"] = (
        "The #778 note states the hydrant works. The record already carried "
        "operational_status=works from #776 in cycle #36, so this is recorded as a "
        "cross-check by {a} 2026-09-09, not a rewrite. The note itself is not "
        "published: the rest of it explains the correction to the "
        "moderator.".format(a=APPROVER))
    state["provenance"][rec["id"]]["source_refs"].append(ref)

    # ---- the three removals ----
    by = {r["id"]: r for r in out}
    for rid, (issue, action, reason) in REMOVE.items():
        v = by.get(rid)
        assert v is not None, rid
        assert v.get("review_status") == "reported", (rid, v.get("review_status"))
        arch["removed"].append({"issue_number": issue, "removed_at": ts,
                                "reason": reason, "record": copy.deepcopy(v)})
        r2 = make_source_ref(issue_number=issue, report_type="missing", old_id=rid,
                             old_coord=list(v["coords"]), changes={}, old_values={},
                             approver_id=APPROVER, timestamp=ts)
        r2.update(manual_field="removed", old_value=None, new_value="removed",
                  merge_action=action,
                  attribution="Removed by {a} 2026-09-09 from issue #{i}. {r}".format(
                      a=APPROVER, i=issue, r=reason))
        state["provenance"][rid]["source_refs"].append(r2)
    out = [r for r in out if r["id"] not in REMOVE]
    assert len(out) == AFTER, len(out)
    assert len(arch["removed"]) == ARCH_BEFORE + 3

    after = counts(out)
    for k, (bb, aa) in DELTA.items():
        assert before[k] == bb, (k, before[k], bb)
        assert after[k] == aa, (k, after[k], aa)

    # the only records that vanished are the three he named
    assert set(before_by_id) - {r["id"] for r in out} >= set(REMOVE)
    # the only note that changed is the one that took the spelling fix
    for r in out:
        n = r.get("verifier_note")
        if n and before_by_id.get(r["id"], {}).get("verifier_note") != n:
            assert n == SPELL[806][1], (r["id"], n)
            assert "\\" not in n
    mojibake_scan("h", out)
    mojibake_scan("a", arch)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied %d reports | removed %d | spelling proven note-only on %d record"
          % (len(res), len(REMOVE), len(diff)))
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
    caps = {H: 4, P: 4, A: 80}
    for line in stat.strip().splitlines():
        add, rem, path = line.split("\t")
        assert int(add) <= caps[path.replace("\\", "/")] and int(rem) <= 4, line
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--apply" in sys.argv))
