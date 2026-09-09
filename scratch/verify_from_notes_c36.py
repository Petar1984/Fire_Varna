#!/usr/bin/env python3
"""Mark 14 hydrants verified on the strength of the colleague notes imported
into `address` (Petar, 2026-09-09).

His reading, and it is his to make: a note that describes the hydrant relative
to something a person can see was written by a colleague standing there, so it
proves existence. Locality names, parcel numbers and junk values do not.

`existence_status` only. Operation is NOT touched anywhere here: not one of
these texts says water was ever run, and Petar said so himself. The three that
describe the object itself also carry its type, so that is set too.

Effect on the map: grey -> red ("on site, untested"), which is what
hydrantStatusClass returns for verified with no operational status.

Reservoirs are deliberately NOT in this list. 31 records read "Водоем" or
"Естествени водоизточници"; the data model has no notion of one, so verifying
them would draw a red hydrant pin over a water tank. They stay grey until the
model can say what they are.
"""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.abspath("scripts"))
from lib.hydrant_core import (atomic_write_json, default_timestamp, load_json,
                              make_source_ref, mojibake_scan)

H, P = "data/hydrants.json", "data/hydrants_provenance.json"
APPROVER = "petar"
# landmark notes -> existence only
LANDMARK = [
    "coord_27.84698_43.24041", "coord_27.84695_43.24089", "coord_27.70903_43.42921",
    "coord_27.85492_43.23286", "coord_27.84539_43.24166", "coord_27.90104_43.21602",
    "coord_28.04296_43.28781", "coord_27.83351_43.25322", "coord_27.82144_43.19847",
    "coord_27.77070_43.19980", "coord_27.56853_43.46579",
]
# notes that describe the object itself. The import already set their `type`
# from the same sentence, and it matches — so this is a cross-check, not a write.
DESCRIBED = {
    "coord_27.77462_43.20141": "надземен",
    "coord_27.83735_43.25332": "надземен",
    "coord_27.83868_43.24510": "подземен",
}
BEFORE, VERIFIED_B, VERIFIED_A, TYPED_B, TYPED_A = 7410, 664, 678, 2743, 2743


def main(write: bool) -> int:
    raw = open(H, "rb").read(); sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8")); prov = load_json(P)
    assert len(recs) == BEFORE, len(recs)
    by = {r["id"]: r for r in recs}
    before = copy.deepcopy(recs)
    targets = LANDMARK + list(DESCRIBED)
    assert len(targets) == 14 and len(set(targets)) == 14

    def count(rs, f, v):
        return sum(1 for r in rs if r.get(f) == v)
    def typed(rs):
        return sum(1 for r in rs if r.get("type"))
    assert count(recs, "existence_status", "verified") == VERIFIED_B
    assert typed(recs) == TYPED_B

    ts = default_timestamp()
    for tid in targets:
        r = by[tid]
        note = (r.get("address") or "").strip()
        # Every gate that matters: it must be grey, it must have the note the
        # decision was made on, and it must not already carry a status.
        assert note, tid
        assert r.get("existence_status") is None, (tid, r.get("existence_status"))
        assert r.get("operational_status") is None, tid
        assert r.get("review_status") is None, tid
        changes = {"existence_status": {"new": "verified"}}
        r["existence_status"] = "verified"
        if tid in DESCRIBED:
            # The note names the kind; the import already wrote it. Prove they
            # agree instead of overwriting — a mismatch would mean the note and
            # the registry disagree, and that is a question for Petar, not a fix.
            assert r.get("type") == DESCRIBED[tid], (tid, r.get("type"), DESCRIBED[tid])
        ref = make_source_ref(issue_number=None, report_type="imported_note",
                              old_id=tid, old_coord=list(r["coords"]),
                              changes=changes, old_values={},
                              approver_id=APPROVER, timestamp=ts)
        ref["merge_action"] = "verified_from_imported_note"
        ref["attribution"] = (
            "Existence confirmed by %s 2026-09-09 from the colleague note carried "
            "into `address` by the registry import: \"%s\". The note describes the "
            "hydrant against something visible on site, so someone stood there. "
            "operational_status deliberately untouched — no text here says water "
            "was ever run." % (APPROVER, note)
        ) if tid in LANDMARK else (
            "Existence confirmed by {a} 2026-09-09 from the imported colleague "
            "note: \"{n}\" — it describes the object itself, so it was seen. The "
            "kind it names matches the type the import already carried ({t}), "
            "recorded here as a cross-check rather than a rewrite. "
            "operational_status untouched.".format(a=APPROVER, n=note, t=DESCRIBED[tid])
        )
        prov.setdefault(tid, {"source_refs": []})["source_refs"].append(ref)

    # nothing but existence_status and the three types may have moved
    for old, new in zip(before, recs):
        assert old["id"] == new["id"]
        if new["id"] not in targets:
            assert old == new, new["id"]
        else:
            o, n = dict(old), dict(new)
            o.pop("existence_status", None); n.pop("existence_status", None)
            o.pop("type", None); n.pop("type", None)
            assert o == n, new["id"]
    assert count(recs, "existence_status", "verified") == VERIFIED_A
    assert typed(recs) == TYPED_A
    assert count(recs, "operational_status", "works") == count(before, "operational_status", "works")
    assert count(recs, "operational_status", "not_working") == count(before, "operational_status", "not_working")
    # no reservoir was touched
    for r in recs:
        a = (r.get("address") or "")
        if "Водоем" in a or "водоизточници" in a:
            assert r.get("existence_status") is None, ("reservoir verified!", r["id"])
    mojibake_scan("h", recs); mojibake_scan("p", prov)
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha

    print("verified from imported notes: %d (11 landmark + 3 described)" % len(targets))
    print("  verified %d -> %d | typed %d -> %d | records %d (unchanged)"
          % (VERIFIED_B, VERIFIED_A, TYPED_B, TYPED_A, len(recs)))
    print("  reservoirs left grey: %d"
          % sum(1 for r in recs if "Водоем" in (r.get("address") or "")
                or "водоизточници" in (r.get("address") or "")))
    print("\nALL GATES PASSED")
    if not write:
        print("dry-run"); return 0
    atomic_write_json(H, recs); atomic_write_json(P, prov)
    stat = subprocess.run(["git", "diff", "--numstat", H, P],
                          capture_output=True, text=True, check=True).stdout
    print(stat, end="")
    for line in stat.strip().splitlines():
        add, rem, _ = line.split("\t")
        assert int(add) <= 4 and int(rem) <= 4, line
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--apply" in sys.argv))
