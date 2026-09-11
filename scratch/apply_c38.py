#!/usr/bin/env python3
"""Cycle #38 - issues #807-818 (12 reports), then four removals.

Three separate walks: Свилен Рачев in the south, Георги through Provadia, Petar
across eastern Varna.

Gate 1 (2026-09-12):
  * #815 -> remove `coord_27.92113_43.21036`. A corner duplicate: the survivor
    is filed under бул. "Осми Приморски полк" and this one under ул. "Генерал
    Столипин", 8.0 m apart - one hydrant entered twice, once per street. The
    survivor is the record Petar confirmed with #814 and carries the full
    VIK-VARNA_IZTOK-0031 number against a bare "785".
  * #810, #811, #813 -> removed. Three bare `missing` from Георги with no
    explanation, none of them a duplicate (37-50 m to the nearest record).
    Petar chose to trust him: Георги checked carefully on that same walk, also
    filing #809 (damaged) and #812 (wrong location), and has 46 reports behind
    him. Same shape as #804 last cycle.
  * #812's note stays. It is a `wrong_location` note, which the standing rule
    drops - but that rule exists for notes explaining why the map was wrong.
    This one explains nothing; it tells you where to look once the pin has
    moved, so it publishes, with "В дясно" corrected to "Вдясно".
  * #807 ("Слабо налягане") and #809 ("Спирателния кран") publish as written.
    The second is a verbless fragment whose article could be read either way -
    the edge of the spelling rule, so it is left alone.
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
ISSUES = list(range(807, 819))
DROP_NOTE = {815}
KEEP_NOTE = {807, 809, 812}
SPELL = {812: ("В дясно до близката къща", "Вдясно до близката къща")}

REMOVE = {
    "coord_27.92113_43.21036": (815, "manual_removal_duplicate",
        "Дубликат на coord_27.92115_43.21029 на 8.0 м. Бележката на Петър в #815: "
        "„Дублиран с 27.92115_43.21029. Премахни този.“ Двата записа са на ъгъл и са "
        "заведени по различни улици — оцелелият по бул. „Осми Приморски полк“, този по "
        "ул. „Генерал Столипин“ — тоест един хидрант, вписан два пъти. Оцелява онзи, "
        "който Петър потвърди с #814 и който носи пълния номер VIK-VARNA_IZTOK-0031 "
        "срещу голото „785“. Номерата 785 и etr_varna:27.92113247,43.21035705 остават "
        "само в този архив."),
    "coord_27.53363_43.45657": (810, "manual_removal_reported_missing",
        "Докладван като липсващ от Георги (#810) без бележка. НЕ е дубликат — най-"
        "близкият съсед е на 37.5 м. Петър реши да се довери на докладчика: Георги е "
        "проверявал внимателно в същия обход (подаде и #809 повреден, и #812 грешна "
        "локация) и има 46 доклада от началото на кампанията. Формата е като при #491, "
        "#580, #624 и #804. ЕТР ключът остава само в този архив."),
    "coord_27.53408_43.45647": (811, "manual_removal_reported_missing",
        "Докладван като липсващ от Георги (#811) без бележка. НЕ е дубликат — най-"
        "близкият съсед е на 37.5 м. Същото решение и същият обход като #810. ВиК "
        "номерът 21340 остава само в този архив."),
    "coord_27.54049_43.46184": (813, "manual_removal_reported_missing",
        "Докладван като липсващ от Георги (#813) без бележка. НЕ е дубликат — най-"
        "близкият съсед е на 50 м. Същото решение и същият обход като #810 и #811. ВиК "
        "номерът 21331 остава само в този архив."),
}

BEFORE, AFTER, ARCH_BEFORE = 7406, 7403, 44
DELTA = {"verified": (701, 709), "works": (110, 111), "not_working": (13, 15),
         "reported": (0, 0), "notes": (81, 84), "typed": (2757, 2761)}


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
        elif n not in KEEP_NOTE:
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
    assert len(out) == BEFORE + 1, len(out)   # #808 adds one

    # ---- the four removals ----
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
                   attribution="Removed by {a} 2026-09-12 from issue #{i}. {r}".format(
                       a=APPROVER, i=issue, r=reason))
        state["provenance"][rid]["source_refs"].append(ref)
    out = [r for r in out if r["id"] not in REMOVE]
    assert len(out) == AFTER, len(out)
    assert len(arch["removed"]) == ARCH_BEFORE + 4

    after = counts(out)
    for k, (bb, aa) in DELTA.items():
        assert before[k] == bb, (k, before[k], bb)
        assert after[k] == aa, (k, after[k], aa)

    # A wrong_location move retires the old canonical id too, so the set of
    # vanished ids is the removals PLUS whatever #812 moved off.
    moved = {r["target_id_before"] for r in res
             if r.get("report_type") == "wrong_location"
             and r.get("target_id_before") != r.get("target_id_after")}
    assert set(before_by_id) - {r["id"] for r in out} == set(REMOVE) | moved,         set(before_by_id) - {r["id"] for r in out} ^ (set(REMOVE) | moved)
    # every note that is new is one we meant to publish, and it is clean text
    published = {SPELL[812][1]}
    for n in KEEP_NOTE - set(SPELL):
        published.add(next(r["comment"] for r in feed if r["issue_number"] == n))
    for r in out:
        note = r.get("verifier_note")
        if note and before_by_id.get(r["id"], {}).get("verifier_note") != note:
            assert note in published, (r["id"], note)
            assert "\\" not in note and note == note.strip()
    # the dropped note never reached the data
    dropped = next(r["comment"] for r in feed if r["issue_number"] in DROP_NOTE)
    assert dropped
    for r in out:
        assert r.get("verifier_note") != dropped, r["id"]

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
    caps = {H: 4, P: 4, A: 100}
    for line in stat.strip().splitlines():
        add, rem, path = line.split("\t")
        assert int(add) <= caps[path.replace("\\", "/")] and int(rem) <= 4, line
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--apply" in sys.argv))
