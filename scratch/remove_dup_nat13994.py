#!/usr/bin/env python3
"""Remove NAT-13994, the duplicate 2.8 m from ВиК 268 on ул. Райко Даскалов.

Cycle #36 applied #772 literally as a move, on Petar's instruction, and the
result was exactly what I flagged then: two pins 2.8 m apart. He looked at the
map and said "това е един хидрант — дублиран — нямаме 2 хидранта там".

Survivor: `coord_27.88516_43.21074` — the richer record, carrying ВиК 268, an
ETR key, a region and the type. That follows the settled preference (#684/#685).

The loser's imported text ("На тротоара на улицата. Добро налягане.") is the
one thing it had that the survivor lacks, and it is exactly the kind of line
the publishing test wants, so it is carried over as the survivor's
`verifier_note` instead of disappearing into the archive.

`operational_status` is NOT touched. The text says the pressure is good, which
implies water was once run, but the same restraint was applied to all 14
imported notes this cycle; changing it here alone would be inconsistent, and
turning a pin green on an undated imported note is Petar's call to make for all
three "налягане" records at once.
"""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.abspath("scripts"))
from lib.hydrant_core import (atomic_write_json, default_timestamp, load_json,
                              make_source_ref, mojibake_scan)

H, P, A = "data/hydrants.json", "data/hydrants_provenance.json", "data/removed_hydrants.json"
APPROVER = "petar"
LOSER, SURVIVOR, ISSUE = "coord_27.88519_43.21075", "coord_27.88516_43.21074", 772
BEFORE, AFTER, ARCH_BEFORE = 7410, 7409, 40
NOTE = "На тротоара на улицата. Добро налягане."
REASON = (
    "Дубликат на coord_27.88516_43.21074 на 2.8 м. Докладът #772 беше приложен "
    "буквално като преместване по изричното решение на Петър („действай както е "
    "отбелязано в докладите“), при което двата записа се оказаха един до друг — "
    "предупредено беше преди прилагането. Петър погледна картата и реши: „това е "
    "един хидрант — дублиран — нямаме 2 хидранта там.“ Оцелява ВиК записът, който "
    "носи ВиК 268, ЕТР ключ, район и тип надземен; този носеше само NAT-13994. "
    "Текстът му „На тротоара на улицата. Добро налягане.“ е пренесен върху "
    "оцелелия като verifier_note, за да не падне от картата."
)


def main(write: bool) -> int:
    raw = open(H, "rb").read(); sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8")); prov = load_json(P); arch = load_json(A)
    assert len(recs) == BEFORE and len(arch["removed"]) == ARCH_BEFORE
    by = {r["id"]: r for r in recs}
    loser, surv = by[LOSER], by[SURVIVOR]
    assert loser["legacy_ids"] == ["coord_27.88522_43.21090", "NAT-13994"], loser
    assert surv["legacy_ids"] == ["268", "etr_varna:27.88515581,43.21074187"], surv
    assert (loser.get("address") or "").strip() == NOTE, loser.get("address")
    assert surv.get("verifier_note") is None, "survivor already has a note"
    victim = copy.deepcopy(loser)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}

    ts = default_timestamp()
    surv["verifier_note"] = NOTE
    out = [r for r in recs if r["id"] != LOSER]
    assert len(out) == AFTER

    # nothing else moved
    for r in out:
        if r["id"] != SURVIVOR:
            assert r == before_by_id[r["id"]], r["id"]
    o, n = dict(before_by_id[SURVIVOR]), dict(surv)
    o.pop("verifier_note", None); n.pop("verifier_note", None)
    assert o == n, "survivor changed beyond its note"
    for f, v in (("existence_status", "verified"), ("operational_status", "not_tested")):
        assert surv.get(f) == v, (f, surv.get(f))

    arch["removed"].append({"issue_number": ISSUE, "removed_at": ts,
                            "reason": REASON, "record": victim})
    ref = make_source_ref(issue_number=ISSUE, report_type="wrong_location",
                          old_id=LOSER, old_coord=list(victim["coords"]),
                          changes={}, old_values={}, approver_id=APPROVER, timestamp=ts)
    ref.update(manual_field="removed", old_value=None, new_value="removed",
               merge_action="manual_removal_duplicate",
               attribution="Removed by %s 2026-09-09. %s" % (APPROVER, REASON))
    prov[LOSER]["source_refs"].append(ref)
    ref2 = make_source_ref(issue_number=ISSUE, report_type="wrong_location",
                           old_id=SURVIVOR, old_coord=list(surv["coords"]),
                           changes={"verifier_note": {"new": NOTE}}, old_values={},
                           approver_id=APPROVER, timestamp=ts)
    ref2["merge_action"] = "note_carried_from_removed_duplicate"
    ref2["attribution"] = (
        "The removed duplicate %s carried this text in its imported `address`; it is "
        "the one thing it had that this record lacked, so it moves here rather than "
        "vanishing with it. operational_status deliberately untouched." % LOSER)
    prov[SURVIVOR]["source_refs"].append(ref2)

    mojibake_scan("h", out); mojibake_scan("a", arch); mojibake_scan("p", prov)
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha
    v = sum(1 for r in out if r.get("existence_status") == "verified")
    print("removed %s (NAT-13994) | survivor %s keeps ВиК 268 + ETR" % (LOSER, SURVIVOR))
    print("  note carried over: %s" % NOTE)
    print("  records %d -> %d | verified 678 -> %d | archive %d -> %d"
          % (BEFORE, len(out), v, ARCH_BEFORE, len(arch["removed"])))
    print("\nALL GATES PASSED")
    if not write:
        print("dry-run"); return 0
    atomic_write_json(H, out); atomic_write_json(P, prov); atomic_write_json(A, arch, indent=1)
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
