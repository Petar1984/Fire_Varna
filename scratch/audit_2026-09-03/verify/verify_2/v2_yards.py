# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №2 · находка №4 — НЕЗАВИСИМ авторитет: КАИС func „Сграда за детско
заведение".  Групира ги в дворове и мери кои дворове НЯМАТ доставен пин.
Проверява и 7-те „еднозначни двора" на одита срещу адреса+функцията в КАИС.
READ-ONLY.   python v2_yards.py
"""
from __future__ import annotations
import json, math, re, sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
V3 = Path("C:/git/varna_3d")
FV = Path("C:/git/Fire_Varna")
AUD = Path("C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/audit_2026-09-03/места-покритие")
OUT = Path(__file__).resolve().parent

info = json.loads((V3 / "web/varna_buildings_info.json").read_text(encoding="utf-8"))
DICT, ROWS, COLS = info["dict"], info["rows"], info["columns"]
ci = {c: k for k, c in enumerate(COLS)}
gj = json.loads((V3 / "web/varna_buildings_3d.geojson").read_text(encoding="utf-8"))


def centroid(geom):
    pts = []
    def walk(x):
        if isinstance(x, list) and x and isinstance(x[0], (int, float)):
            pts.append(x)
        elif isinstance(x, list):
            for y in x:
                walk(y)
    walk(geom["coordinates"])
    return sum(p[1] for p in pts) / len(pts), sum(p[0] for p in pts) / len(pts)


CEN = {}
for f in gj["features"]:
    i = f["properties"].get("i")
    if i is not None:
        CEN[i] = centroid(f["geometry"])


def dec(col, r):
    v = r[ci[col]]
    return ("" if v == -1 else DICT[col][v]) if col in DICT else v


def hav(a, b, c, d):
    p1, p2 = math.radians(a), math.radians(c)
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(d - b) / 2) ** 2
    return 2 * 6371000.0 * math.asin(math.sqrt(h))


KID = []
for i, r in enumerate(ROWS):
    if dec("func", r) == "Сграда за детско заведение" and i in CEN:
        la, lo = CEN[i]
        KID.append({"i": i, "lat": la, "lon": lo, "addr": dec("addr", r),
                    "area": r[ci["area_m2"]], "quar": dec("quar", r)})
print("КАИС тела с func „Сграда за детско заведение“:", len(KID))

# --- слепване в дворове: единично свързване на ≤70 m
parent = list(range(len(KID)))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb: parent[rb] = ra
for a in range(len(KID)):
    for b in range(a + 1, len(KID)):
        if hav(KID[a]["lat"], KID[a]["lon"], KID[b]["lat"], KID[b]["lon"]) <= 70:
            union(a, b)
yards = defaultdict(list)
for k in range(len(KID)):
    yards[find(k)].append(KID[k])
YARDS = []
for members in yards.values():
    la = sum(m["lat"] for m in members) / len(members)
    lo = sum(m["lon"] for m in members) / len(members)
    YARDS.append({"lat": la, "lon": lo, "n": len(members),
                  "area": round(sum(m["area"] for m in members), 1),
                  "addr": sorted({m["addr"] for m in members if m["addr"]})[:3],
                  "ids": [m["i"] for m in members]})
YARDS.sort(key=lambda y: -y["area"])
print("дворове (слепване ≤70 m):", len(YARDS))

# --- доставените места от класа „детска градина“
places = json.loads((FV / "data/places.json").read_text(encoding="utf-8"))["places"]
DG = [p for p in places if p["kind"] == "детска градина"]
SCH = [p for p in places if p["kind"] == "училище"]

for R in (80, 120):
    hit = 0
    for y in YARDS:
        d = min(hav(y["lat"], y["lon"], p["lat"], p["lon"]) for p in DG)
        y["d_dg_%d" % R] = round(d, 1)
        if d <= R:
            hit += 1
    print(f"дворове с доставен ДГ-пин на ≤{R} m: {hit}/{len(YARDS)}  "
          f"({100.0*hit/len(YARDS):.1f} %) — БЕЗ пин: {len(YARDS)-hit}")

no_pin = [y for y in YARDS if y["d_dg_120"] > 120]
print("\n=== дворове БЕЗ ДГ-пин на ≤120 m (подредени по застроена площ):")
for y in no_pin[:40]:
    dsch = min(hav(y["lat"], y["lon"], p["lat"], p["lon"]) for p in SCH)
    print(f"  {y['area']:8.0f} m2  n={y['n']:<2} d_ДГ={y['d_dg_120']:7.0f} m  d_учил={dsch:6.0f} m  "
          f"{y['lat']:.5f},{y['lon']:.5f}  | {' / '.join(y['addr'])[:60]}")
print("  ... общо", len(no_pin))

# --- 7-те „еднозначни двора" на одита срещу КАИС func
miss = json.loads((AUD / "missing.json").read_text(encoding="utf-8"))["детски градини (общински, ЛИПСВАЩИ)"]
print("\n=== 18-те липсващи · има ли КАИС „детско заведение“ около геокода?")
rowsum = []
for x in miss:
    g = x.get("geo")
    if not g:
        print(f"  ДГ№{x['no']:<3} {x['name'][:34]:34} | БЕЗ ГЕОКОД (село)")
        rowsum.append((x["no"], "село", None, None)); continue
    la, lo = g["lat"], g["lon"]
    near = sorted(((hav(la, lo, k["lat"], k["lon"]), k) for k in KID), key=lambda t: t[0])[:3]
    best_d, best = near[0]
    chosen = (x.get("kais_near") or [{}])[0]
    same = (chosen.get("i") == best["i"]) if chosen else False
    print(f"  ДГ№{x['no']:<3} {x['name'][:32]:32} | одит взе i={chosen.get('i')} на {chosen.get('d_m')} m "
          f"({str(chosen.get('addr'))[:26]}) | КАИС детско заведение: i={best['i']} на {best_d:.0f} m "
          f"({best['area']:.0f} m2, {best['addr'][:26]}) | СЪВПАДАТ={same}")
    rowsum.append((x["no"], x["site_verdict"], round(best_d), best["i"]))

json.dump({"yards": YARDS, "no_pin_120": no_pin, "missing_vs_kidfunc": rowsum},
          open(OUT / "v2_yards.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
