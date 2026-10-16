#!/usr/bin/env python3
"""ADR 013 - add the Burgas-side hydrants that the national registry assigns
to a Varna oblast fire unit ("към У ПБЗН – Бяла").

The May import excluded 38 region-81 records (NAT-7208 … NAT-7386) as Burgas
oblast. Petar decided on 16.10.2026 that they belong on the map. 37 are added:
NAT-7385 is a 1.96 m duplicate of NAT-7227 in the source itself (same note,
same type, same creation date) and is recorded in NAT-7227's history instead.

Every record is written exactly like the other national imports: grey,
origin "national", legacy_ids ["NAT-n"], type from the source name, pyproj
EPSG:3857 -> EPSG:4326 (always_xy) - the transform that reproduces the
existing national coordinates bit for bit - and the same "winner" provenance
ref, plus one ref carrying this decision.

The source is read only: C:/Projects/Varna_hydrants/geo_fire_hydrants.json.
"""
from __future__ import annotations
import copy, hashlib, json, math, os, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.abspath("scripts"))
from lib.hydrant_core import (  # noqa: E402
    atomic_write_json, default_timestamp, load_json, make_source_ref, mojibake_scan,
)
from pyproj import Transformer  # noqa: E402

H, P = "data/hydrants.json", "data/hydrants_provenance.json"
SRC = r"C:/Projects/Varna_hydrants/geo_fire_hydrants.json"
SRC_FEATURES = 17962
APPROVER = "petar"
EXCLUDED_IN_MAY = [7208, 7212, 7213, 7214, 7219, 7224, 7226, 7227, 7228, 7232, 7234, 7235, 7236,
                   7237, 7238, 7241, 7242, 7249, 7364, 7365, 7366, 7367, 7368, 7369, 7370, 7371,
                   7372, 7373, 7377, 7378, 7379, 7380, 7381, 7382, 7383, 7384, 7385, 7386]
DUP_KEPT, DUP_DROPPED = 7227, 7385
TYPE_OF = {"Надземен хидрант": "надземен", "Подземен хидрант": "подземен"}
RAW_TYPE_OF = {"Надземен хидрант": "ground", "Подземен хидрант": "underground"}
UNIT = "У ПБЗН - Бяла"
BEFORE, ADDED = 7417, 37
DELTA = {"verified": (786, 786), "works": (130, 130), "not_working": (18, 18),
         "reported": (0, 0), "notes": (104, 104), "typed": (2813, 2850)}


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


def dist(a, b):
    return math.hypot((b[0] - a[0]) * math.cos(math.radians(a[1])) * 111320,
                      (b[1] - a[1]) * 111320)


def main(write: bool) -> int:
    # ---- the source, read only ----
    src_raw = open(SRC, "rb").read()
    src_sha = hashlib.sha256(src_raw).hexdigest()
    feats = json.loads(src_raw.decode("utf-8"))["features"]
    assert len(feats) == SRC_FEATURES, len(feats)
    by_num = {f["properties"]["id"]: f for f in feats}
    t = Transformer.from_crs("EPSG:3857", "EPSG:4326", always_xy=True)

    raw = open(H, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw.decode("utf-8"))
    prov = load_json(P)
    assert len(recs) == BEFORE, len(recs)
    before = counts(recs)
    before_by_id = {r["id"]: copy.deepcopy(r) for r in recs}
    on_map = {l for r in recs for l in (r.get("legacy_ids") or [])}

    # ---- calibration: the transform reproduces the May import bit for bit ----
    exact = 0
    for r in recs:
        n = next((int(l[4:]) for l in r.get("legacy_ids") or [] if l.startswith("NAT-")), None)
        if r.get("origin") == "national" and n in by_num:
            c = by_num[n]["geometry"]["coordinates"]
            if list(t.transform(c[0], c[1])) == r["coords"]:
                exact += 1
    assert exact >= 2298, ("transform calibration", exact)

    # ---- the 38 excluded in May ----
    for n in EXCLUDED_IN_MAY:
        p = by_num[n]["properties"]
        assert p["geo_region_structure_id"] == 81, (n, p["geo_region_structure_id"])
        assert p["is_active"] is True and p["n_fire_hydrant_status_id"] == 1, n
        assert UNIT in (p["notes"] or ""), (n, p["notes"])
        assert p["name"] in TYPE_OF, (n, p["name"])
        assert "NAT-%d" % n not in on_map, (n, "already on the map")

    def ll(n):
        c = by_num[n]["geometry"]["coordinates"]
        return list(t.transform(c[0], c[1]))

    # ---- the source duplicate ----
    a, b = by_num[DUP_KEPT]["properties"], by_num[DUP_DROPPED]["properties"]
    dup_m = dist(ll(DUP_KEPT), ll(DUP_DROPPED))
    assert dup_m < 3.0, dup_m
    assert " ".join(a["notes"].split()) == " ".join(b["notes"].split()), (a["notes"], b["notes"])
    assert a["name"] == b["name"] and a["created_on"] == b["created_on"]

    ts = default_timestamp()
    adding = [n for n in EXCLUDED_IN_MAY if n != DUP_DROPPED]
    assert len(adding) == ADDED
    new_recs, new_prov = [], {}
    for n in adding:
        p = by_num[n]["properties"]
        lon, lat = ll(n)
        assert 26.5 <= lon <= 28.5 and 42.7 <= lat <= 44.0, (n, lon, lat)
        rid = "coord_%.5f_%.5f" % (lon, lat)
        assert rid not in before_by_id, (n, rid)
        near = min(dist([lon, lat], r["coords"]) for r in recs)
        assert near >= 20.0, (n, near)
        rec = {"id": rid, "coords": [lon, lat], "origin": "national",
               "legacy_ids": ["NAT-%d" % n], "type": TYPE_OF[p["name"]]}
        winner = {"old_id": "NAT-%d" % n, "old_coord": [lon, lat],
                  "raw_type": RAW_TYPE_OF[p["name"]],
                  "z": "uin=%s; created=%s; updated=%s; geo_region=%s" % (
                      p.get("uin") or n, p.get("created_on") or "", p.get("updated_on") or "",
                      p["geo_region_structure_id"]),
                  "merge_action": "winner", "conflict_flags": []}
        why = ("Added by {a} 2026-10-16 under ADR 013. Excluded on 2026-05-09 as Burgas oblast; "
               "the national registry assigns it to a Varna oblast unit (source note: {note}). "
               "Source: geo_fire_hydrants.json sha256 {sha}.").format(a=APPROVER, note=p["notes"],
                                                                     sha=src_sha[:16])
        if n == DUP_KEPT:
            why += (" NAT-%d is the same hydrant entered twice in the source (%.2f m away, same "
                    "note, type and creation date) and was not added." % (DUP_DROPPED, dup_m))
        ref = make_source_ref(issue_number=None, report_type=None, old_id="NAT-%d" % n,
                              old_coord=[lon, lat], changes={}, old_values={},
                              approver_id=APPROVER, timestamp=ts)
        ref.update(manual_field="scope", old_value="excluded", new_value="included",
                   merge_action="scope_extension_adr013", attribution=why)
        new_recs.append(rec)
        new_prov[rid] = {"source_refs": [winner, ref]}

    out = recs + new_recs
    assert len({r["id"] for r in out}) == len(out), "duplicate id"
    prov2 = dict(prov)
    for k, v in new_prov.items():
        assert k not in prov2, k
        prov2[k] = v

    # ---- nothing else moved ----
    for r in out[:BEFORE]:
        assert r == before_by_id[r["id"]], r["id"]
    for k in prov:
        assert prov2[k] == prov[k], k
    after = counts(out)
    for k, (bb, aa) in DELTA.items():
        assert before[k] == bb, (k, before[k], bb)
        assert after[k] == aa, (k, after[k], aa)
    assert len(out) == BEFORE + ADDED
    mojibake_scan("h", out)
    mojibake_scan("p", prov2)
    assert hashlib.sha256(open(H, "rb").read()).hexdigest() == sha
    assert hashlib.sha256(open(SRC, "rb").read()).hexdigest() == src_sha

    types = {}
    for r in new_recs:
        types[r["type"]] = types.get(r["type"], 0) + 1
    print("ADR 013: adding %d Burgas-side national records (types %s); NAT-%d dropped as a %.2f m "
          "duplicate of NAT-%d" % (len(new_recs), types, DUP_DROPPED, dup_m, DUP_KEPT))
    print("  calibration: %d national records reproduced bit for bit by the transform" % exact)
    print("  source sha256 %s (read only, unchanged)" % src_sha)
    for k in DELTA:
        print("  %-12s %s -> %s" % (k, before[k], after[k]))
    print("  %-12s %s -> %s" % ("records", BEFORE, len(out)))
    print("  southmost lat now %.5f" % min(r["coords"][1] for r in out))
    print("\nALL GATES PASSED")
    if not write:
        print("dry-run; nothing written (pass --apply to write)")
        return 0

    atomic_write_json(H, out)
    atomic_write_json(P, prov2)
    stat = subprocess.run(["git", "diff", "--numstat", H, P],
                          capture_output=True, text=True, check=True).stdout
    print(stat, end="")
    for line in stat.strip().splitlines():
        add, rem, _ = line.split("\t")
        assert int(add) <= 4 and int(rem) <= 4, line
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--apply" in sys.argv))
