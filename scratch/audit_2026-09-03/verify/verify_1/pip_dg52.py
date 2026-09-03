# -*- coding: utf-8 -*-
"""READ-ONLY: point-in-polygon за трите пина от находка №11 срещу КАИС телата."""
import json, sys, math
GJ = r"C:\git\varna_3d\web\varna_buildings_3d.geojson"
INFO = r"C:\git\varna_3d\web\varna_buildings_info.json"

PINS = {
    "ДГ№52 Бялата лястовица": (43.209723, 27.890771),
    "Аджибадем Сити Клиник (болница)": (43.217378, 27.916067),
    "Медицински комплекс Майчин дом (болница)": (43.220199, 27.9265),
}

def rings(geom):
    t = geom["type"]; c = geom["coordinates"]
    if t == "Polygon": return [c]
    if t == "MultiPolygon": return c
    return []

def pip(lon, lat, ring):
    inside = False
    n = len(ring)
    for k in range(n):
        x1, y1 = ring[k][0], ring[k][1]
        x2, y2 = ring[(k + 1) % n][0], ring[(k + 1) % n][1]
        if (y1 > lat) != (y2 > lat):
            xin = x1 + (lat - y1) * (x2 - x1) / (y2 - y1)
            if lon < xin: inside = not inside
    return inside

gj = json.load(open(GJ, encoding="utf-8"))
feats = gj["features"]
info = json.load(open(INFO, encoding="utf-8"))
cols, D, rows = info["columns"], info["dict"], info["rows"]
def rec(i):
    r = rows[i]; out = {}
    for c, v in zip(cols, r):
        out[c] = (D[c][v] if v >= 0 else None) if c in D else v
    return out

print("features:", len(feats))
hits = {k: [] for k in PINS}
for f in feats:
    i = f["properties"].get("i")
    g = f.get("geometry")
    if not g: continue
    rs = rings(g)
    # bbox
    xs = []; ys = []
    for poly in rs:
        for pt in poly[0]:
            xs.append(pt[0]); ys.append(pt[1])
    if not xs: continue
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    for name, (lat, lon) in PINS.items():
        if x0 - 1e-6 <= lon <= x1 + 1e-6 and y0 - 1e-6 <= lat <= y1 + 1e-6:
            for poly in rs:
                if pip(lon, lat, poly[0]):
                    hits[name].append(i)
                    break

for name, (lat, lon) in PINS.items():
    print("\n==", name, (lat, lon))
    if not hits[name]:
        print("   пинът НЕ пада в никакво КАИС тяло")
    for i in hits[name]:
        print("   i=%d %s" % (i, json.dumps(rec(i), ensure_ascii=False)))
