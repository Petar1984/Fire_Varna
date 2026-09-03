# -*- coding: utf-8 -*-
"""READ-ONLY: най-близкото КАИС тяло със здравна функция до всеки от трите пина."""
import json, math
GJ = r"C:\git\varna_3d\web\varna_buildings_3d.geojson"
INFO = r"C:\git\varna_3d\web\varna_buildings_info.json"
PINS = {
    "Аджибадем Сити Клиник": (43.217378, 27.916067),
    "Майчин дом": (43.220199, 27.9265),
    "Диспансер (ДКЦ)": (43.209744, 27.890788),
}
def hav(a, b):
    R = 6371000.0
    la1, lo1 = map(math.radians, a); la2, lo2 = map(math.radians, b)
    return 2 * R * math.asin(math.sqrt(math.sin((la2-la1)/2)**2 +
        math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2))
def rings(g): return [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]

info = json.load(open(INFO, encoding="utf-8"))
cols, D, rows = info["columns"], info["dict"], info["rows"]
fi = cols.index("func"); ai = cols.index("addr")
funcs = D["func"]; addrs = D["addr"]
health = [k for k, v in enumerate(funcs) if "Здравно" in v or "болниц" in v.lower()]
print("здравни функции в речника:", [funcs[k] for k in health])
hset = set(health)
gj = json.load(open(GJ, encoding="utf-8"))
best = {k: (1e9, None) for k in PINS}
for f in gj["features"]:
    i = f["properties"].get("i")
    if i is None or rows[i][fi] not in hset: continue
    g = f.get("geometry")
    if not g: continue
    xs = []; ys = []
    for poly in rings(g):
        for pt in poly[0]: xs.append(pt[0]); ys.append(pt[1])
    c = (sum(ys)/len(ys), sum(xs)/len(xs))
    for name, p in PINS.items():
        d = hav(p, c)
        if d < best[name][0]: best[name] = (d, i)
for name, (d, i) in best.items():
    print("%-24s -> %.1f m  i=%s  %s | %s" % (name, d, i, funcs[rows[i][fi]], addrs[rows[i][ai]]))
