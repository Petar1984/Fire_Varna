# -*- coding: utf-8 -*-
"""What does 'outside any KAIS body' actually mean on the ground?
For every one of the 135 places: distance to the nearest KAIS polygon whose
func matches the expected one. Read-only."""
import json, math, sys, io, statistics
from collections import Counter, defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

FV = r"C:/git/Fire_Varna"
V3 = r"C:/git/varna_3d"
OUT = r"C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/audit_2026-09-03/verify_10_2"

places = json.load(open(FV + "/data/places.json", encoding="utf-8"))["places"]
gj = json.load(open(V3 + "/web/varna_buildings_3d.geojson", encoding="utf-8"))
INFO = json.load(open(V3 + "/web/varna_buildings_info.json", encoding="utf-8"))
_c = {c: i for i, c in enumerate(INFO["columns"])}


def bfield(i, col):
    v = INFO["rows"][i][_c[col]]
    return INFO["dict"][col][v] if v >= 0 else ""


def rings_of(g):
    t = g["type"]
    return [g["coordinates"]] if t == "Polygon" else list(g["coordinates"]) if t == "MultiPolygon" else []


polys = []
for ft in gj["features"]:
    i = ft["properties"].get("i")
    f = bfield(i, "func") if i is not None else ""
    for poly in rings_of(ft["geometry"]):
        o = poly[0]
        xs = [p[0] for p in o]
        ys = [p[1] for p in o]
        polys.append((min(xs), min(ys), max(xs), max(ys), poly, i, f))

CELL = 0.002
grid = defaultdict(list)
for k, p in enumerate(polys):
    for cx in range(int(p[0] / CELL), int(p[2] / CELL) + 1):
        for cy in range(int(p[1] / CELL), int(p[3] / CELL) + 1):
            grid[(cx, cy)].append(k)

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


def nearest_with_func(lon, lat, want, radius_m=400.0):
    """distance (0 if inside) to nearest polygon with func == want; also count of
    distinct such polygons within 60 m."""
    kx, ky = mlon(lat), MLAT
    rc = int(radius_m / (CELL * min(kx, ky))) + 1
    best = (1e18, None)
    near60 = set()
    seen = set()
    cx0, cy0 = int(lon / CELL), int(lat / CELL)
    for cx in range(cx0 - rc, cx0 + rc + 1):
        for cy in range(cy0 - rc, cy0 + rc + 1):
            for k in grid.get((cx, cy), ()):
                if k in seen:
                    continue
                seen.add(k)
                x0, y0, x1, y1, poly, i, f = polys[k]
                if f != want:
                    continue
                ddx = (x0 - lon) * kx if lon < x0 else (lon - x1) * kx if lon > x1 else 0.0
                ddy = (y0 - lat) * ky if lat < y0 else (lat - y1) * ky if lat > y1 else 0.0
                if math.hypot(ddx, ddy) > max(radius_m, best[0]):
                    continue
                if x0 <= lon <= x1 and y0 <= lat <= y1 and pt_in_ring(lon, lat, poly[0]):
                    best = (0.0, i)
                    near60.add(i)
                    continue
                d = 1e18
                for ring in poly:
                    for n in range(len(ring) - 1):
                        dd = seg_dist_m(lon, lat, ring[n][0], ring[n][1],
                                        ring[n + 1][0], ring[n + 1][1], kx, ky)
                        if dd < d:
                            d = dd
                if d < best[0]:
                    best = (d, i)
                if d <= 60:
                    near60.add(i)
    return best[0], best[1], len(near60)


EXPECTED = {"детска градина": "Сграда за детско заведение",
            "училище": "Сграда за образование",
            "университет": "Сграда за образование",
            "болница": "Здравно заведение", "ДКЦ": "Здравно заведение",
            "хоспис": "Здравно заведение"}

prev = json.load(open(OUT + "/pip_independent.json", encoding="utf-8"))
verdict = {r["name"]: r for r in prev["places"]}

rows = []
for p in places:
    want = EXPECTED[p["kind"]]
    d, i, n60 = nearest_with_func(p["lon"], p["lat"], want)
    v = verdict[p["name"]]["verdict"]
    rows.append({"name": p["name"], "kind": p["kind"], "zone": p.get("zone"),
                 "lat": p["lat"], "lon": p["lon"], "pip": v,
                 "d_to_right_func_m": None if i is None else round(d, 1),
                 "right_func_i": i, "bodies_of_right_func_within_60m": n60})

out = [r for r in rows if r["pip"] == "вън"]
ins = [r for r in rows if r["pip"] == "съвпада"]
wf = [r for r in rows if r["pip"] == "друга функция"]


def buck(d):
    if d is None:
        return "няма такава функция <400 m"
    return ("0" if d == 0 else "0-5" if d <= 5 else "5-10" if d <= 10 else "10-20" if d <= 20
            else "20-50" if d <= 50 else "50-100" if d <= 100 else ">100")


print("=== 62-те „вън“: разстояние до тяло с ПРАВИЛНАТА функция ===")
print(dict(sorted(Counter(buck(r["d_to_right_func_m"]) for r in out).items())))
dd = [r["d_to_right_func_m"] for r in out if r["d_to_right_func_m"] is not None]
print("n=%d  медиана %.1f m  средно %.1f m  max %.1f m  ≤20 m: %d  ≤50 m: %d"
      % (len(dd), statistics.median(dd), sum(dd) / len(dd), max(dd),
         sum(1 for x in dd if x <= 20), sum(1 for x in dd if x <= 50)))
print("без тяло с правилната функция до 400 m:",
      sum(1 for r in out if r["d_to_right_func_m"] is None))

print("\n=== 11-те „друга функция“ (ВЪТРЕ, но в чуждо тяло) ===")
print(dict(sorted(Counter(buck(r["d_to_right_func_m"]) for r in wf).items())))
for r in wf:
    print("   %-46s %-16s d=%s" % (r["name"][:46], r["kind"], r["d_to_right_func_m"]))

print("\n=== 62-те „съвпада“ (контрола) ===")
print(dict(sorted(Counter(buck(r["d_to_right_func_m"]) for r in ins).items())))

print("\n=== колко тела с правилната функция има около мястото (комплекс?) ===")
print("вън   :", dict(sorted(Counter(min(r["bodies_of_right_func_within_60m"], 6) for r in out).items())))
print("вътре :", dict(sorted(Counter(min(r["bodies_of_right_func_within_60m"], 6) for r in ins).items())))

print("\n=== примерите от черновата ===")
for nm in ["Раковски", "Неофит Бозвели", "Чайка", "Военно", "Яворов", "МБАЛ Варна"]:
    for r in rows:
        if nm.lower() in r["name"].lower():
            print("  %-46s pip=%-14s d_до_правилна_функция=%s m  тела≤60m=%d"
                  % (r["name"][:46], r["pip"], r["d_to_right_func_m"],
                     r["bodies_of_right_func_within_60m"]))

worst = sorted([r for r in out if r["d_to_right_func_m"] is not None],
               key=lambda r: -r["d_to_right_func_m"])[:10]
print("\n=== най-далечните 10 от 62-те ===")
for r in worst:
    print("  %6.1f m  %-44s %s" % (r["d_to_right_func_m"], r["name"][:44], r["kind"]))

json.dump(rows, open(OUT + "/severity_rows.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("\nwrote", OUT + "/severity_rows.json")
