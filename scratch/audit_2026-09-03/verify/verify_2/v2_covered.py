# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №2 · находка №4 — качеството на 35-те „покрити": колко далеч е
доставеният пин от най-близкото КАИС „детско заведение"?  READ-ONLY.
    python v2_covered.py
"""
from __future__ import annotations
import json, math, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
V3, FV = Path("C:/git/varna_3d"), Path("C:/git/Fire_Varna")
AUD = Path("C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/audit_2026-09-03/места-покритие")

info = json.loads((V3 / "web/varna_buildings_info.json").read_text(encoding="utf-8"))
DICT, ROWS, COLS = info["dict"], info["rows"], info["columns"]
ci = {c: k for k, c in enumerate(COLS)}
gj = json.loads((V3 / "web/varna_buildings_3d.geojson").read_text(encoding="utf-8"))

def centroid(g):
    pts = []
    def w(x):
        if isinstance(x, list) and x and isinstance(x[0], (int, float)): pts.append(x)
        elif isinstance(x, list):
            for y in x: w(y)
    w(g["coordinates"])
    return sum(p[1] for p in pts)/len(pts), sum(p[0] for p in pts)/len(pts)

CEN = {f["properties"]["i"]: centroid(f["geometry"]) for f in gj["features"] if "i" in f["properties"]}
def dec(c, r):
    v = r[ci[c]]
    return ("" if v == -1 else DICT[c][v]) if c in DICT else v
def hav(a,b,c,d):
    p1,p2=math.radians(a),math.radians(c)
    h=math.sin((p2-p1)/2)**2+math.cos(p1)*math.cos(p2)*math.sin(math.radians(d-b)/2)**2
    return 2*6371000.0*math.asin(math.sqrt(h))

KID = [{"i": i, "lat": CEN[i][0], "lon": CEN[i][1], "addr": dec("addr", r), "area": r[ci["area_m2"]]}
       for i, r in enumerate(ROWS) if dec("func", r) == "Сграда за детско заведение" and i in CEN]

verd = json.loads((AUD / "missing.json").read_text(encoding="utf-8"))["доставени ДГ — присъда"]
print("=== 46-те доставени · разстояние до най-близкото КАИС „детско заведение“")
buckets = {"≤30 m": 0, "30–80 m": 0, "80–150 m": 0, ">150 m": 0}
far = []
for v in sorted(verd, key=lambda x: x["delivered"]):
    d, best = min(((hav(v["lat"], v["lon"], k["lat"], k["lon"]), k) for k in KID), key=lambda t: t[0])
    b = "≤30 m" if d <= 30 else "30–80 m" if d <= 80 else "80–150 m" if d <= 150 else ">150 m"
    buckets[b] += 1
    if d > 80:
        far.append((round(d), v["delivered"], v["class"], v.get("reg_name"), best["addr"][:40], round(best["area"])))
print(json.dumps(buckets, ensure_ascii=False))
print("\n  пинове на >80 m от каквото и да е КАИС детско заведение:")
for d, nm, cl, rg, ba, ar in sorted(far, reverse=True):
    print(f"   {d:6} m  {nm[:38]:38} [{cl}] рег={rg} | най-близко: {ba} ({ar} m2)")

# --- частният регистър
regs = json.loads((AUD / "registers.json").read_text(encoding="utf-8"))
print("\n=== ключове в registers.json:", list(regs.keys()))
for k in regs:
    if "част" in k.lower() or "privat" in k.lower():
        v = regs[k]
        print(f"  {k}: n={len(v)}")
        for r in (v if isinstance(v, list) else [])[:15]:
            print("    ", json.dumps(r, ensure_ascii=False)[:150])
