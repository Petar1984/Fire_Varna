# -*- coding: utf-8 -*-
"""POZARNA.DWG bulk import (Golden Sands): append grey (canonical) hydrant
records to data/hydrants.json + provenance. Additive only — existing records
must survive byte-for-byte (gated below). Gate 1 = Petar's chat approval
2026-08-31 ("добави ги като сиви и ще ги проверим")."""
import json, math, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HYDRANTS = r"C:\git\Fire_Varna\data\hydrants.json"
PROV = r"C:\git\Fire_Varna\data\hydrants_provenance.json"
GEOJSON = r"C:\git\Fire_Varna\scratch\pozarna_gz\pozarna_gz_wgs84.geojson"
RAW = r"C:\git\Fire_Varna\scratch\pozarna_gz\px_wgs84.json"
DUP_SKIP_M = 5.0          # <5 m to a live record = same hydrant (DWG min spacing is 6.26 m)
NEAR_FLAG_M = 15.0        # 5-15 m: kept but listed for the field check

live = json.load(open(HYDRANTS, encoding="utf-8"))
prov = json.load(open(PROV, encoding="utf-8"))
gj = json.load(open(GEOJSON, encoding="utf-8"))
new_pts = [f["geometry"]["coordinates"] for f in gj["features"] if f["properties"]["kind"] == "hydrant"]
assert len(new_pts) == 105, len(new_pts)

before_count = len(live)
before_serialized = json.dumps(live[:len(live)], ensure_ascii=False)  # snapshot for the no-mutation gate
existing_ids = {r["id"] for r in live}
for r in live:
    for a in r.get("legacy_ids", []):
        existing_ids.add(a)

R, rad = 6371000, math.pi / 180
def dist_m(a, b):
    dlat = (a[1] - b[1]) * rad
    dlon = (a[0] - b[0]) * rad * math.cos(a[1] * rad)
    return R * math.hypot(dlat, dlon)

near_live = [r for r in live if 43.25 <= r["coords"][1] <= 43.32 and 28.0 <= r["coords"][0] <= 28.08]

skipped, flagged, records, prov_add = [], [], [], {}
for n, (lon, lat) in enumerate(new_pts, start=1):
    lon6, lat6 = round(lon, 6), round(lat, 6)
    best, best_id = 1e9, None
    for r in near_live:
        d = dist_m((lon6, lat6), r["coords"])
        if d < best:
            best, best_id = d, r["id"]
    dwg_id = "GZ-DWG-%03d" % n
    if best < DUP_SKIP_M:
        skipped.append((dwg_id, round(best, 1), best_id))
        continue
    if best < NEAR_FLAG_M:
        flagged.append((dwg_id, round(best, 1), best_id))
    rid = "coord_%.5f_%.5f" % (lon6, lat6)
    assert rid not in existing_ids, "id collision: " + rid
    existing_ids.add(rid)
    records.append({
        "id": rid,
        "coords": [lon6, lat6],
        "origin": "pozarna_gz",
        "legacy_ids": [dwg_id],
        "region": "КК Златни пясъци",
    })
    prov_add[rid] = {"source_refs": [{
        "old_id": dwg_id,
        "old_coord": [lon6, lat6],
        "s": "POZARNA.DWG слой PX (КС1970 К-7 -> КК2005 grid bojko108/transformations -> WGS84)",
        "merge_action": "winner",
        "conflict_flags": [],
    }]}

print("new records:", len(records), "| skipped as dup(<%gm):" % DUP_SKIP_M, len(skipped), "| flagged 5-15 m:", len(flagged))
for s in skipped: print("  SKIP", s)
for f in flagged: print("  FLAG", f)

merged = live + records
# ---- gates ----
assert len(merged) == before_count + len(records)
assert json.dumps(merged[:before_count], ensure_ascii=False) == before_serialized, "existing records mutated!"
assert len({r["id"] for r in merged}) == len(merged), "duplicate ids in merged set"
for r in records:
    assert 43.27 <= r["coords"][1] <= 43.31 and 28.03 <= r["coords"][0] <= 28.05, r
    assert "existence_status" not in r and "review_status" not in r  # must render grey (canonical)
overlap = set(prov_add) & set(prov)
assert not overlap, overlap

if "--apply" in sys.argv:
    with open(HYDRANTS, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(merged, ensure_ascii=False) + "\n")
    prov.update(prov_add)
    with open(PROV, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(prov, ensure_ascii=False) + "\n")
    back = json.load(open(HYDRANTS, encoding="utf-8"))
    assert len(back) == before_count + len(records)
    assert json.dumps(back[:before_count], ensure_ascii=False) == before_serialized
    print("APPLIED: %d -> %d records" % (before_count, len(back)))
else:
    print("dry run (pass --apply to write)")
