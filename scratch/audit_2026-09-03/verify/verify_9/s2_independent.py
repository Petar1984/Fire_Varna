# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №9 · стъпка 2 — НЕЗАВИСИМО от anomalies.json: суровите файлове.
READ-ONLY. Нищо в C:/git не се пише."""
import json, sys
from collections import Counter
from pathlib import Path
from shapely.geometry import shape, Point
from shapely.strtree import STRtree
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIRE = Path(r"C:\git\Fire_Varna"); V3D = Path(r"C:\git\varna_3d")
M6 = Path(r"C:\git\m6000_private\number_viewer")

def jl(p): return json.load(open(p, encoding="utf-8"))

# --- 1. кутията, преписана от МЯРКА §1.3 (не импортирана) -------------------
def box(lat, lon):
    if lat >= 43.2780: return "к.к. Златни пясъци"
    if lat >= 43.2600 and lon >= 28.0250: return "к.к. Чайка"
    if lat >= 43.2460: return "Виница/север"
    if lat >= 43.2150 and lon >= 27.9900: return "к.к. Св. Константин"
    if lat <= 43.1900: return "Аспарухово/Галата"
    return "гр. Варна"

hot = jl(FIRE/"data"/"hotels.json")["hotels"]
pl  = jl(FIRE/"data"/"places.json")["places"]
rows = ([{"key": f"hotels[{i}]", "name": r["name"], "lat": r["lat"], "lon": r["lon"],
          "zone": r.get("zone")} for i, r in enumerate(hot)] +
        [{"key": f"places[{i}]", "name": r["name"], "lat": r["lat"], "lon": r["lon"],
          "zone": r.get("zone")} for i, r in enumerate(pl)])
print("редове:", len(rows), "(hotels %d + places %d)" % (len(hot), len(pl)))

# ГЕЙТ: записаната зона на курортните редове = кутията
res = [x for x in rows if x["zone"] in ("к.к. Златни пясъци","к.к. Чайка","к.к. Св. Константин")]
bad = [x for x in res if box(x["lat"], x["lon"]) != x["zone"]]
print("ГЕЙТ · курортни редове %d, кутията ги възпроизвежда: %d разминавания" % (len(res), len(bad)))
print("  разпределение на кутията по всички 361:", dict(Counter(box(x["lat"],x["lon"]) for x in rows)))

# --- 2. КАИС сграда под пина ------------------------------------------------
print("\nчета КАИС сградите …", flush=True)
info = jl(V3D/"web"/"varna_buildings_info.json")
cols, dct, irows = info["columns"], info["dict"], info["rows"]
qi = cols.index("quar")
gj = jl(V3D/"web"/"varna_buildings_3d.geojson")
feats = gj["features"]
geoms, idxs = [], []
for f in feats:
    p = f.get("properties") or {}
    i = p.get("i")
    if i is None: continue
    try: g = shape(f["geometry"])
    except Exception: continue
    geoms.append(g); idxs.append(i)
tree = STRtree(geoms)
print("сгради с геометрия:", len(geoms))

def quar_of(i):
    v = irows[i][qi]
    return dct["quar"][v] if isinstance(v, int) and 0 <= v < len(dct["quar"]) else None

def under(lat, lon):
    pt = Point(lon, lat)
    for j in tree.query(pt):
        if geoms[j].covers(pt):
            return idxs[j]
    return None

# --- 3. чертаният слой ------------------------------------------------------
dr = jl(M6/"quarters_drawn_v1.geojson")["features"]
dgeoms, dkeys = [], []
for f in dr:
    try: g = shape(f["geometry"])
    except Exception: continue
    dgeoms.append(g); dkeys.append((f.get("properties") or {}).get("key"))
dtree = STRtree(dgeoms)
def drawn_keys(lat, lon):
    pt = Point(lon, lat)
    return sorted({dkeys[j] for j in dtree.query(pt) if dgeoms[j].covers(pt)})

# --- 4. Чайка-редовете ------------------------------------------------------
ch = [x for x in rows if x["zone"] == "к.к. Чайка"]
print("\n=== zone == 'к.к. Чайка': %d реда ===" % len(ch))
out = []
for x in sorted(ch, key=lambda y: y["lat"]):
    i = under(x["lat"], x["lon"])
    q = quar_of(i) if i is not None else None
    dk = drawn_keys(x["lat"], x["lon"])
    out.append({**x, "bld_i": i, "kais_quar": q, "drawn": dk})
zl_k = [x for x in out if x["kais_quar"] and "ЗЛАТНИ" in x["kais_quar"].upper()]
zl_d = [x for x in out if any("златни" in (k or "").lower() for k in x["drawn"])]
uni = {x["key"] for x in zl_k} | {x["key"] for x in zl_d}
inter = {x["key"] for x in zl_k} & {x["key"] for x in zl_d}
print("КАИС (суров quar съдържа ЗЛАТНИ): %d" % len(zl_k))
print("чертан ключ съдържа 'златни'   : %d" % len(zl_d))
print("ОБЕДИНЕНИЕ: %d · ПРЕСИЧАНЕ: %d" % (len(uni), len(inter)))
lats = [x["lat"] for x in out if x["key"] in uni]
print("lat ивица: %.5f – %.5f" % (min(lats), max(lats)))
print()
for x in out:
    m = "★" if x["key"] in uni else " "
    print(f"{m} {x['key']:<12} {x['name'][:26]:<28} lat={x['lat']:.5f} lon={x['lon']:.5f} "
          f"КАИС={str(x['kais_quar'])[:34]:<36} чертан={','.join(x['drawn']) or '—'}")
json.dump(out, open(Path(__file__).with_name("chayka_rows.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
