#!/usr/bin/env python3
"""Cycle #40 - issues #829-856 (28 reports), then three removals.

A long walk of Petar's through central and eastern Varna (27 reports) plus one
confirmation from инсп. Пеев (#847).

Gate 1 (2026-09-15) - "действай, както са докладвани", after the coordinates of
both doubtful pairs were put in front of him:

  * #830 -> remove `coord_27.88272_43.22018` (NAT-5330). Twin NAT-5218 at 8.9 m,
    already verified. Both national; the confirmed one survives.
  * #829 -> remove `coord_28.04967_43.30160` (NAT-5390). Twin `GZ-DWG-004` at
    **30.2 m** - twice the distance of any duplicate we have taken before, and
    the reason this one was put to him explicitly. He confirmed. The twin is a
    Golden Sands record, verified and working; the next neighbour is 38.9 m out,
    so the area is sparse and the pair really is alone.
  * #832 -> remove `coord_27.86864_43.22731`. The twin is 5.3 m away and the
    removal REVERSES the usual preference: the record going carries the full
    VIK-VARNA_ZAPAD-0004 number, the survivor a bare "1278". Both hold an ETR
    key. What settles it is which record holds more truth: the survivor is
    verified on site and typed надземен, the loser an empty grey row. Shown to
    him before the decision; the number lives on in the archive, as with #474
    and #481.

  * #839's note publishes: "Зад билборда (посока катедралата)". The second case
    after #812 - a `wrong_location` note that explains nothing about why the map
    was wrong and instead names a landmark the map cannot show. The rule still
    drops these by default.
  * #851's note drops (moderator-facing), as do the three "махни този" notes.
  * #846 is a no-op: it repeats #845 on the same record, filed because the
    reporter's connection dropped and he did not know whether the first had
    landed. It had.
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
ISSUES = list(range(829, 857))
KEEP_NOTE = {839}

REMOVE = {
    "coord_27.88272_43.22018": (830, "manual_removal_duplicate",
        "Дубликат на coord_27.88274_43.22010 на 8.9 м, който вече е проверен на място. "
        "Бележката на Петър в #830: „Хидранта е дублиран с 27.88274_43.22010 — махни "
        "този.“ И двата са национални записи; оцелява потвърденият. NAT-5330 остава "
        "само в този архив."),
    "coord_28.04967_43.30160": (829, "manual_removal_duplicate",
        "Дубликат на coord_28.04944_43.30139 (GZ-DWG-004, Златни пясъци, проверен и "
        "работещ) на **30.2 м**. Бележката на Петър в #829: „дублиран с Хидрант "
        "coord_28.04944_43.30139 — премахни този.“ ⚠️ Разстоянието е двойно над всеки "
        "дубликат, който сме приемали досега (5–16 м), и точно затова случаят му беше "
        "показан изрично с координати и линк към двата пина преди решението. Той "
        "потвърди. И двата записа са подземни, а следващият съсед е чак на 38.9 м, "
        "тоест районът е рядък и двойката наистина е сама. NAT-5390 остава само в този "
        "архив."),
    "coord_27.86864_43.22731": (832, "manual_removal_duplicate",
        "Дубликат на coord_27.86863_43.22726 на 5.3 м. Бележката на Петър в #832: "
        "„дублиран с 27.86863_43.22726 — махни този.“ ⚠️ Обратно на обичайното "
        "предпочитание: отпада записът с ПЪЛНИЯ номер VIK-VARNA_ZAPAD-0004, а остава "
        "онзи с голото „1278“. И двата носят ЕТР ключ. Решаващото е кой запис носи "
        "повече истина: оцелелият е проверен на място и типизиран надземен, а този е "
        "празен сив ред без тип. Показано му беше преди решението. Номерата "
        "VIK-VARNA_ZAPAD-0004 и etr_varna:27.86864309,43.22730731 остават само в този "
        "архив, както при #474 и #481."),
}

BEFORE, AFTER, ARCH_BEFORE = 7403, 7400, 48
DELTA = {"verified": (719, 743), "works": (111, 112), "not_working": (15, 15),
         "reported": (0, 0), "notes": (84, 85), "typed": (2769, 2780)}


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
    reps = []
    for r in sorted(feed, key=lambda x: x["issue_number"]):
        r = copy.deepcopy(r)
        if r["issue_number"] not in KEEP_NOTE:
            r["comment"] = None
        reps.append(r)
    kept = [r["comment"] for r in reps if r.get("comment")]
    assert len(kept) == len(KEEP_NOTE), kept

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
    assert len(out) == BEFORE, len(out)

    # ---- the three removals ----
    by = {r["id"]: r for r in out}
    for rid, (issue, action, reason) in REMOVE.items():
        v = by.get(rid)
        assert v is not None, rid
        assert v.get("review_status") == "reported", (rid, v.get("review_status"))
        arch["removed"].append({"issue_number": issue, "removed_at": ts,
                                "reason": reason, "record": copy.deepcopy(v)})
        ref = make_source_ref(issue_number=issue, report_type="missing", old_id=rid,
                              old_coord=list(v["coords"]), changes={}, old_values={},
                              approver_id=APPROVER, timestamp=ts)
        ref.update(manual_field="removed", old_value=None, new_value="removed",
                   merge_action=action,
                   attribution="Removed by {a} 2026-09-15 from issue #{i}. {r}".format(
                       a=APPROVER, i=issue, r=reason))
        state["provenance"][rid]["source_refs"].append(ref)
    out = [r for r in out if r["id"] not in REMOVE]
    assert len(out) == AFTER, len(out)
    assert len(arch["removed"]) == ARCH_BEFORE + 3

    after = counts(out)
    for k, (b, a) in DELTA.items():
        assert before[k] == b, (k, before[k], b)
        assert after[k] == a, (k, after[k], a)

    # the only ids that vanished are the removals plus whatever #839/#851 moved off
    moved = {r["target_id_before"] for r in res
             if r.get("report_type") == "wrong_location"
             and r.get("target_id_before") != r.get("target_id_after")}
    assert set(before_by_id) - {r["id"] for r in out} == set(REMOVE) | moved

    # the only new note is the one we meant to publish, and it is clean text
    for r in out:
        note = r.get("verifier_note")
        if note and before_by_id.get(r["id"], {}).get("verifier_note") != note:
            assert note in kept, (r["id"], note)
            assert "\\" not in note and "\n" not in note, (r["id"], note)
    # every dropped note stayed out
    for r in feed:
        if r["issue_number"] not in KEEP_NOTE and r.get("comment"):
            for x in out:
                assert x.get("verifier_note") != r["comment"], (r["issue_number"], x["id"])

    mojibake_scan("h", out)
    mojibake_scan("a", arch)
    mojibake_scan("p", state["provenance"])
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("applied %d reports | removed %d | published notes: %d" % (len(res), len(REMOVE), len(kept)))
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
