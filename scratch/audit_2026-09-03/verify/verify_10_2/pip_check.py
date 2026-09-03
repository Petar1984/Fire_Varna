# -*- coding: utf-8 -*-
"""Independent re-measurement of finding #10 (read-only)."""
import json, math, sys, io
from collections import Counter, defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

FV = r"C:/git/Fire_Varna"
V3 = r"C:/git/varna_3d"
OUT = r"C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/audit_2026-09-03/verify_10_2"

places = json.load(open(FV + "/data/places.json", encoding="utf-8"))["places"]
hotels = json.load(open(FV + "/data/hotels.json", encoding="utf-8"))
if isinstance(hotels, dict):
    hotels = hotels.get("hotels", hotels.get("rows"))
print("places", len(places), "hotels", len(hotels))

gj = json.load(open(V3 + "/web/varna_buildings_3d.geojson", encoding="utf-8"))
feats = gj["features"]
print("kais features", len(feats))

INFO = json.load(open(V3 + "/web/varna_buildings_info.json", encoding="utf-8"))
_c = {c: i for i, c in enumerate(INFO["columns"])}


def bfield(i, col):
    v = INFO["rows"][i][_c[col]]
    return INFO["dict"][col][v] if v >= 0 else ""


def rings_of(g):
    t = g["type"]
    if t == "Polygon":
        return [g["coordinates"]]
    if t == "MultiPolygon":
        return list(g["coordinates"])
    return []


def pt_in_ring(x, y, ring):
    c, n = False, len(ring)
    j = n - 1
    for i in range(n):
        xi, yi = ring[i][0], ring[i][1]
        xj, yj = ring[j][0], ring[j][1]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            c = not c
        j = i
    return c


polys = []
for ft in feats:
    i = ft["properties"].get("i")
    for poly in rings_of(ft["geometry"]):
        outer = poly[0]
        xs = [p[0] for p in outer]
        ys = [p[1] for p in outer]
        polys.append((min(xs), min(ys), max(xs), max(ys), poly, i))
print("polygons(incl. multipart)", len(polys))
print("KAIS bbox lon %.5f..%.5f lat %.5f..%.5f" % (
    min(p[0] for p in polys), max(p[2] for p in polys),
    min(p[1] for p in polys), max(p[3] for p in polys)))

CELL = 0.002
grid = defaultdict(list)
for k, (x0, y0, x1, y1, poly, i) in enumerate(polys):
    for cx in range(int(x0 / CELL), int(x1 / CELL) + 1):
        for cy in range(int(y0 / CELL), int(y1 / CELL) + 1):
            grid[(cx, cy)].append(k)


def cells_around(lon, lat, r_cells):
    cx0, cy0 = int(lon / CELL), int(lat / CELL)
    for cx in range(cx0 - r_cells, cx0 + r_cells + 1):
        for cy in range(cy0 - r_cells, cy0 + r_cells + 1):
            for k in grid.get((cx, cy), ()):
                yield k


def hit(lon, lat):
    seen = set()
    for k in cells_around(lon, lat, 1):
        if k in seen:
            continue
        seen.add(k)
        x0, y0, x1, y1, poly, i = polys[k]
        if not (x0 <= lon <= x1 and y0 <= lat <= y1):
            continue
        if pt_in_ring(lon, lat, poly[0]):
            if not any(pt_in_ring(lon, lat, h) for h in poly[1:]):
                return i
    return None


MLAT = 111320.0


def mlon(lat):
    return 111320.0 * math.cos(math.radians(lat))


def seg_dist_m(px, py, ax, ay, bx, by, kx, ky):
    Ax, Ay = (ax - px) * kx, (ay - py) * ky
    Bx, By = (bx - px) * kx, (by - py) * ky
    dx, dy = Bx - Ax, By - Ay
    L2 = dx * dx + dy * dy
    if L2 == 0:
        return math.hypot(Ax, Ay)
    t = max(0.0, min(1.0, -(Ax * dx + Ay * dy) / L2))
    return math.hypot(Ax + t * dx, Ay + t * dy)


def nearest_edge(lon, lat, max_cells=6):
    kx, ky = mlon(lat), MLAT
    best = (1e18, None)
    seen = set()
    for r in range(1, max_cells + 1):
        for k in cells_around(lon, lat, r):
            if k in seen:
                continue
            seen.add(k)
            x0, y0, x1, y1, poly, i = polys[k]
            ddx = (x0 - lon) * kx if lon < x0 else (lon - x1) * kx if lon > x1 else 0.0
            ddy = (y0 - lat) * ky if lat < y0 else (lat - y1) * ky if lat > y1 else 0.0
            if math.hypot(ddx, ddy) >= best[0]:
                continue
            for ring in poly:
                for n in range(len(ring) - 1):
                    d = seg_dist_m(lon, lat, ring[n][0], ring[n][1],
                                   ring[n + 1][0], ring[n + 1][1], kx, ky)
                    if d < best[0]:
                        best = (d, i)
        if best[0] < r * CELL * min(kx, ky) * 0.9:
            break
    return best


def count_within(lon, lat, radius_m):
    kx, ky = mlon(lat), MLAT
    n = 0
    seen = set()
    rc = int(radius_m / (CELL * min(kx, ky))) + 1
    for k in cells_around(lon, lat, rc):
        if k in seen:
            continue
        seen.add(k)
        x0, y0, x1, y1, poly, i = polys[k]
        ddx = (x0 - lon) * kx if lon < x0 else (lon - x1) * kx if lon > x1 else 0.0
        ddy = (y0 - lat) * ky if lat < y0 else (lat - y1) * ky if lat > y1 else 0.0
        if math.hypot(ddx, ddy) <= radius_m:
            n += 1
    return n


EXPECTED = {"детска градина": "Сграда за детско заведение",
            "училище": "Сграда за образование",
            "университет": "Сграда за образование",
            "болница": "Здравно заведение", "ДКЦ": "Здравно заведение",
            "хоспис": "Здравно заведение"}

res = {"places": [], "hotels": []}
fit = Counter()
for p in places:
    i = hit(p["lon"], p["lat"])
    exp = EXPECTED[p["kind"]]
    if i is None:
        d, ni = nearest_edge(p["lon"], p["lat"])
        fit[(p["kind"], "вън")] += 1
        nf = bfield(ni, "func") if ni is not None else ""
        res["places"].append({"name": p["name"], "kind": p["kind"], "lat": p["lat"],
                              "lon": p["lon"], "zone": p.get("zone"), "verdict": "вън",
                              "nearest_m": round(d, 1), "nearest_i": ni,
                              "nearest_func": nf,
                              "nearest_addr": bfield(ni, "addr") if ni is not None else "",
                              "func_matches": nf == exp,
                              "kais_within_50m": count_within(p["lon"], p["lat"], 50),
                              "kais_within_100m": count_within(p["lon"], p["lat"], 100)})
    else:
        f = bfield(i, "func")
        fit[(p["kind"], "съвпада" if f == exp else "друга функция")] += 1
        res["places"].append({"name": p["name"], "kind": p["kind"], "lat": p["lat"],
                              "lon": p["lon"],
                              "verdict": "съвпада" if f == exp else "друга функция",
                              "kais_i": i, "kais_func": f})

hfit = Counter()
for h in hotels:
    lat, lon = h.get("lat"), h.get("lon")
    i = hit(lon, lat)
    if i is None:
        d, ni = nearest_edge(lon, lat)
        hfit["вън"] += 1
        res["hotels"].append({"name": h.get("name"), "lat": lat, "lon": lon,
                              "nearest_m": round(d, 1), "nearest_i": ni,
                              "nearest_func": bfield(ni, "func") if ni is not None else "",
                              "kais_within_50m": count_within(lon, lat, 50)})
    else:
        hfit["вътре"] += 1

print("\n--- PLACES ---")
tab = defaultdict(dict)
for (k, v), n in fit.items():
    tab[k][v] = n
tot = Counter()
for k in sorted(tab):
    print(" ", k, dict(tab[k]))
    for v, n in tab[k].items():
        tot[v] += n
print("TOTAL", dict(tot), "sum", sum(tot.values()))
print("--- HOTELS ---", dict(hfit))
print("inside places+hotels:", tot.get("съвпада", 0) + tot.get("друга функция", 0) + hfit["вътре"],
      "of", len(places) + len(hotels))

outs = [r for r in res["places"] if r["verdict"] == "вън"]


def bucket(d):
    return ("0-5" if d <= 5 else "5-10" if d <= 10 else "10-20" if d <= 20
            else "20-50" if d <= 50 else "50-100" if d <= 100 else ">100")


print("\nnearest-edge buckets (places out):",
      dict(sorted(Counter(bucket(r["nearest_m"]) for r in outs).items())))
print("nearest polygon has the EXPECTED func:", sum(1 for r in outs if r["func_matches"]), "of", len(outs))
print("zero KAIS polygons within 50 m:", sum(1 for r in outs if r["kais_within_50m"] == 0))
print("zero KAIS polygons within 100 m:", sum(1 for r in outs if r["kais_within_100m"] == 0))
print("hotel out buckets:",
      dict(sorted(Counter(bucket(r["nearest_m"]) for r in res["hotels"]).items())))

json.dump(res, open(OUT + "/pip_independent.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("\nwrote", OUT + "/pip_independent.json")
