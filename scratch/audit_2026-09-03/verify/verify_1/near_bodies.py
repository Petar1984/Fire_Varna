# -*- coding: utf-8 -*-
"""READ-ONLY: кои КАИС тела стоят около пина на „Диспансер за белодробни заболявания"."""
import json, math
GJ = r"C:\git\varna_3d\web\varna_buildings_3d.geojson"
INFO = r"C:\git\varna_3d\web\varna_buildings_info.json"
PIN = (43.209744, 27.890788)
R = 150.0

def hav(a, b):
    Rm = 6371000.0
    la1, lo1 = map(math.radians, a); la2, lo2 = map(math.radians, b)
    return 2 * Rm * math.asin(math.sqrt(math.sin((la2 - la1) / 2) ** 2 +
        math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2))

def rings(g):
    return [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]

gj = json.load(open(GJ, encoding="utf-8"))
info = json.load(open(INFO, encoding="utf-8"))
cols, D, rows = info["columns"], info["dict"], info["rows"]
def rec(i):
    r = rows[i]; out = {}
    for c, v in zip(cols, r):
        out[c] = (D[c][v] if v >= 0 else None) if c in D else v
    return out

out = []
for f in gj["features"]:
    g = f.get("geometry")
    if not g: continue
    xs = []; ys = []
    for poly in rings(g):
        for pt in poly[0]:
            xs.append(pt[0]); ys.append(pt[1])
    if not xs: continue
    c = (sum(ys) / len(ys), sum(xs) / len(xs))
    d = hav(PIN, c)
    if d <= R:
        out.append((round(d, 1), f["properties"].get("i"), rec(f["properties"].get("i"))))
out.sort()
for d, i, r in out:
    print("%7.1f m  i=%-7d %-38s %s" % (d, i, r["func"], r["addr"]))
