# -*- coding: utf-8 -*-
"""ЗАДАЧА „правило" (03.09.2026) — READ-ONLY измервач.

Gate „мястото ляга върху тяло с вярна функция" + правилото за името.

    set PYTHONIOENCODING=utf-8 && python measure_rule.py

Пише САМО в собствената си папка: placement.json (+ stdout, който влиза в
summary.md).  Нищо в C:/git не се пипа.

ИЗВОРИ (всички четени, нито един писан)
  C:/git/varna_3d/web/varna_buildings_info.json    80 497 реда, 37 func
  C:/git/varna_3d/web/varna_buildings_3d.geojson   80 497 полигона
  C:/git/Fire_Varna/data/places.json               135 доставени места
  C:/git/Fire_Varna/data/hotels.json               226 доставени хотела
  C:/git/Fire_Varna/data/address_rows.json         80 510 адресни реда

ПРОЕКЦИЯ: локална equirectangular около (43.22, 27.92), 111320 m/градус и
cos(lat) по x — СЪЩОТО приближение, с което конвейерът мери своите 60 m
(build_poi_names.py dist_m, export_fire_varna_places.py dist_m).  Проверката е
в §0: shapely-площта срещу колоната area_m2 на КАИС.
"""
from __future__ import annotations
import collections
import json
import math
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from shapely.geometry import Point                       # noqa: E402
from shapely.ops import unary_union                      # noqa: E402
from shapely.strtree import STRtree                      # noqa: E402

G = "C:/git/"
LAT0, LON0 = 43.22, 27.92
MPD = 111320.0
KX = MPD * math.cos(math.radians(LAT0))
OUT = "placement.json"

# =============================================================================
# §1 — ТАБЛИЦАТА НА СЪОТВЕТСТВИЯТА (класът на мястото → функцията на тялото)
# =============================================================================
# Не я измислям: за образованието и здравето тя вече СЪЩЕСТВУВА в конвейера —
# build_poi_names.py:204 PROFILE_FUNC (клас на OSM → КАИС функция), плюс
# SPORT_FUNC (:220 „салонът в двора носи името на училището") и AUX_FUNC (:194
# „функции, които никога не са самата институция").  Тук е пренесена дословно и
# разширена САМО с хотелите, които PROFILE_FUNC не покрива.
MATCH = {
    "детска градина": ["Сграда за детско заведение"],
    "училище":        ["Сграда за образование"],
    "университет":    ["Сграда за образование"],
    "болница":        ["Здравно заведение"],
    "ДКЦ":            ["Здравно заведение"],
    "хоспис":         ["Здравно заведение"],
    "Хотел":                     ["Хотел", "Апартаментен хотел", "Курортна, туристическа сграда"],
    "Семеен хотел":              ["Хотел", "Апартаментен хотел", "Курортна, туристическа сграда"],
    "апарт-хотел":               ["Хотел", "Апартаментен хотел", "Курортна, туристическа сграда"],
    "хотел · без категоризация": ["Хотел", "Апартаментен хотел", "Курортна, туристическа сграда"],
}
YARD_FUNC = {"Спортна сграда, база"}                       # build_poi_names.py:220
AUX_FUNC = {"Складова база, склад", "Гараж", "Селскостопанска сграда",
            "Постройка на допълващото застрояване"}        # build_poi_names.py:194
CLASS_ORDER = ["детска градина", "училище", "университет", "болница", "ДКЦ",
               "хоспис", "Хотел", "Семеен хотел", "апарт-хотел",
               "хотел · без категоризация"]


def to_m(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * MPD)


def to_deg(x, y):
    return (LAT0 + y / MPD, LON0 + x / KX)


def load_info():
    d = json.load(open(G + "varna_3d/web/varna_buildings_info.json", encoding="utf-8"))
    return d, {c: i for i, c in enumerate(d["columns"])}


def field(d, cols, row, name):
    v = row[cols[name]]
    if name in d["dict"]:
        return d["dict"][name][v] if isinstance(v, int) and 0 <= v < len(d["dict"][name]) else None
    return v


def load_geoms():
    from shapely.geometry import Polygon
    gj = json.load(open(G + "varna_3d/web/varna_buildings_3d.geojson", encoding="utf-8"))
    polys = [None] * len(gj["features"])
    for f in gj["features"]:
        rings = f["geometry"]["coordinates"]
        polys[f["properties"]["i"]] = Polygon([to_m(x, y) for x, y in rings[0]],
                                              [[to_m(x, y) for x, y in r] for r in rings[1:]])
    return polys


def load_delivered():
    out = []
    for fn, key, pre in (("Fire_Varna/data/places.json", "places", "P"),
                         ("Fire_Varna/data/hotels.json", "hotels", "H")):
        for k, r in enumerate(json.load(open(G + fn, encoding="utf-8"))[key]):
            out.append(dict(rid="%s%03d" % (pre, k), file=fn.split("/")[-1],
                            name=r["name"], kind=r["kind"], lat=r["lat"], lon=r["lon"],
                            zone=r.get("zone", ""), src=r.get("src", ""),
                            status=r.get("status", ""), old_names=r.get("old_names") or []))
    return out


def clusters(idxs, polys, gap=40.0):
    """Площадка = свързаните тела на <= gap m. Union-find върху STRtree."""
    sub = [polys[i] for i in idxs]
    t = STRtree(sub)
    par = list(range(len(idxs)))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a
    for a, p in enumerate(sub):
        for b in t.query(p.buffer(gap)):
            b = int(b)
            if b > a and p.distance(sub[b]) <= gap:
                ra, rb = find(a), find(b)
                if ra != rb:
                    par[ra] = rb
    g = collections.defaultdict(list)
    for a in range(len(idxs)):
        g[find(a)].append(idxs[a])
    return sorted([sorted(v) for v in g.values()])


def h(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def main():
    info, cols = load_info()
    rows = info["rows"]
    polys = load_geoms()
    tree = STRtree(polys)
    dl = load_delivered()
    dictf = info["dict"]["func"]
    fi = cols["func"]
    doc = {"_meta": {"command": "python measure_rule.py",
                     "n_buildings": len(rows), "n_delivered": len(dl),
                     "projection": "equirectangular @ (43.22,27.92), 111320 m/deg",
                     "match_table_source": "varna_3d/src/build_poi_names.py:194/204/220"}}

    # ---- §0 проекция ------------------------------------------------------
    h("§0 · ПРОВЕРКА НА ПРОЕКЦИЯТА (shapely площ срещу колоната area_m2)")
    err = []
    for i in (0, 1, 2, 100, 5000, 40000, 80496):
        a, b = polys[i].area, rows[i][cols["area_m2"]]
        err.append(abs(a - b) / b)
        print("   i=%-6d shapely %9.1f m2 · КАИС %9.1f m2 · грешка %.2f %%"
              % (i, a, b, 100 * abs(a - b) / b))
    print("   максимална грешка: %.2f %%" % (100 * max(err)))
    doc["_meta"]["projection_max_err_pct"] = round(100 * max(err), 3)

    # ---- §1 речникът func -------------------------------------------------
    h("§1 · РЕЧНИКЪТ `func` — 37 стойности, с броя тела на всяка")
    cnt = collections.Counter(r[fi] for r in rows)
    doc["func_dict"] = []
    for k, f in enumerate(dictf):
        doc["func_dict"].append({"k": k, "func": f, "n": cnt.get(k, 0)})
        print("   %5d  %s" % (cnt.get(k, 0), f))
    h("§1б · ТАБЛИЦАТА НА СЪОТВЕТСТВИЯТА (клас на мястото -> функция на тялото)")
    for k in CLASS_ORDER:
        print("   %-28s -> %s" % (k, " | ".join(MATCH[k])))
    print("   двор (част от мястото)      -> " + " | ".join(sorted(YARD_FUNC)))
    print("   помощна (никога мястото)    -> " + " | ".join(sorted(AUX_FUNC)))
    doc["match_table"] = {"match": MATCH, "yard": sorted(YARD_FUNC), "aux": sorted(AUX_FUNC)}

    # ---- §2 разполагане на 361-те -----------------------------------------
    h("§2 · РАЗПОЛАГАНЕ: PiP на 361-те записа срещу 80 497 полигона")
    sub = {}
    for f in sorted({x for v in MATCH.values() for x in v}):
        idx = [i for i, r in enumerate(rows) if r[fi] == dictf.index(f)]
        sub[f] = (idx, STRtree([polys[i] for i in idx]))
    place = []
    for r in dl:
        pt = Point(*to_m(r["lon"], r["lat"]))
        ins = [int(i) for i in tree.query(pt) if polys[int(i)].covers(pt)]
        ok = set(MATCH[r["kind"]])
        if ins:
            good = [i for i in ins if field(info, cols, rows[i], "func") in ok]
            pick = sorted(good or ins, key=lambda i: (polys[i].area, i))[0]
            d = 0.0
        else:
            cand = []
            for rad in (30.0, 120.0, 600.0, 5000.0):
                cand = [(polys[int(i)].distance(pt), int(i)) for i in tree.query(pt.buffer(rad))]
                if cand:
                    break
            d, pick = min(cand)
        f = field(info, cols, rows[pick], "func")
        cls = ("вярна" if f in ok else
               "двор" if (f in YARD_FUNC and r["kind"] in ("училище", "университет", "детска градина")) else
               "помощна" if f in AUX_FUNC else "друга")
        best = (1e9, None)
        for fn in ok:
            idx, t = sub[fn]
            for rad in (10, 30, 60, 120, 300, 1200, 6000):
                c = [(t.geometries[int(j)].distance(pt), idx[int(j)]) for j in t.query(pt.buffer(rad))]
                if c:
                    best = min(best, min(c))
                    break
        place.append(dict(rid=r["rid"], file=r["file"], name=r["name"], kind=r["kind"],
                          zone=r["zone"], src=r["src"], lat=r["lat"], lon=r["lon"],
                          i=pick, dist_m=round(d, 2), n_inside=len(ins), func=f,
                          func_class=cls, area_m2=rows[pick][cols["area_m2"]],
                          floors=rows[pick][cols["floors"]],
                          prop=field(info, cols, rows[pick], "prop"),
                          reg=field(info, cols, rows[pick], "reg"),
                          addr=field(info, cols, rows[pick], "addr"),
                          ok_i=best[1], ok_d=round(best[0], 2)))
    doc["placement"] = place

    def bucket(d):
        return ("вътре" if d == 0 else "<=10 m" if d <= 10 else "<=30 m" if d <= 30
                else "<=60 m" if d <= 60 else "> 60 m")
    BUK = ["вътре", "<=10 m", "<=30 m", "<=60 m", "> 60 m"]
    CLS = ["вярна", "двор", "помощна", "друга"]
    grid = collections.Counter((bucket(x["dist_m"]), x["func_class"]) for x in place)
    print("   %-8s | %s | общо" % ("кофа", " ".join("%9s" % c for c in CLS)))
    for b in BUK:
        tot = sum(grid[(b, c)] for c in CLS)
        print("   %-8s | %s | %4d" % (b, " ".join("%9d" % grid[(b, c)] for c in CLS), tot))
    print("   %-8s | %s | %4d" % ("ОБЩО", " ".join(
        "%9d" % sum(grid[(b, c)] for b in BUK) for c in CLS), len(place)))
    doc["buckets"] = {b: {c: grid[(b, c)] for c in CLS} for b in BUK}

    h("§2б · по клас")
    for k in CLASS_ORDER:
        s = [x for x in place if x["kind"] == k]
        if not s:
            continue
        ds = sorted(x["dist_m"] for x in s)
        print("   %-26s n=%3d · вътре %3d · <=10 m %3d · >30 m %2d · вярна %3d · друга %2d · d(p95)=%.1f m"
              % (k, len(s), sum(1 for x in s if x["dist_m"] == 0),
                 sum(1 for x in s if 0 < x["dist_m"] <= 10),
                 sum(1 for x in s if x["dist_m"] > 30),
                 sum(1 for x in s if x["func_class"] == "вярна"),
                 sum(1 for x in s if x["func_class"] == "друга"),
                 ds[min(len(ds) - 1, int(0.95 * len(ds)))]))

    h("§2в · ПОИМЕННО: всички > 30 m от тялото си")
    for x in sorted((x for x in place if x["dist_m"] > 30), key=lambda x: -x["dist_m"]):
        print("   %6.1f m · %-42s %-14s %-24s func=%-26s ok_d=%.1f m"
              % (x["dist_m"], x["name"][:42], x["kind"], x["zone"][:24], x["func"][:26], x["ok_d"]))
    print("   (записи > 60 m: %d)" % sum(1 for x in place if x["dist_m"] > 60))

    h("§2г · ПОИМЕННО: ДРУГА функция (кандидати за преместване/проверка)")
    oth = sorted((x for x in place if x["func_class"] == "друга"),
                 key=lambda x: (x["file"], -x["ok_d"]))
    print("   места (%d):" % sum(1 for x in oth if x["file"] == "places.json"))
    for x in oth:
        if x["file"] == "places.json":
            print("     %-42s %-14s d=%5.1f func=%-30s ok_d=%7.1f m"
                  % (x["name"][:42], x["kind"], x["dist_m"], x["func"][:30], x["ok_d"]))
    hh = [x for x in oth if x["file"] == "hotels.json"]
    print("   хотели (%d) — 12-те с най-далечно вярно тяло:" % len(hh))
    for x in hh[:12]:
        print("     %-42s %-24s func=%-30s ok_d=%7.1f m"
              % (x["name"][:42], x["zone"][:24], x["func"][:30], x["ok_d"]))
    doc["yard_rows"] = [x["name"] for x in place if x["func_class"] == "двор"]
    doc["aux_rows"] = [x["name"] for x in place if x["func_class"] == "помощна"]

    h("§2д · ok_d — разстояние до НАЙ-БЛИЗКОТО тяло с ВЯРНА функция")
    c = collections.Counter()
    for x in place:
        d = x["ok_d"]
        c["0 (вътре/допира)" if d == 0 else "<=10 m" if d <= 10 else "<=30 m" if d <= 30
          else "<=60 m" if d <= 60 else "<=200 m" if d <= 200 else "> 200 m"] += 1
    for k in ["0 (вътре/допира)", "<=10 m", "<=30 m", "<=60 m", "<=200 m", "> 200 m"]:
        print("   %-18s %3d" % (k, c[k]))
    doc["ok_d_hist"] = dict(c)

    # ---- §3 дупката --------------------------------------------------------
    h("§3 · ДУПКАТА: тела с целева функция БЕЗ доставено място")
    hole = {}
    pts = [Point(*to_m(r["lon"], r["lat"])) for r in dl]
    ptree = STRtree(pts)
    for f in ["Сграда за детско заведение", "Сграда за образование", "Здравно заведение",
              "Хотел", "Апартаментен хотел", "Курортна, туристическа сграда"]:
        kinds = {k for k, v in MATCH.items() if f in v}
        idx = [i for i, r in enumerate(rows) if r[fi] == dictf.index(f)]
        cl = clusters(idx, polys)
        cov, free = {}, {}
        for thr in (10.0, 30.0, 60.0, 120.0):
            fr = []
            for cc in cl:
                g = unary_union([polys[i] for i in cc])
                hit = any(pts[int(j)].distance(g) <= thr and dl[int(j)]["kind"] in kinds
                          for j in ptree.query(g.buffer(thr)))
                if not hit:
                    fr.append(cc)
            cov[str(int(thr))] = len(cl) - len(fr)
            free[str(int(thr))] = fr
        f60 = []
        for cc in free["60"]:
            g = unary_union([polys[i] for i in cc])
            la, lo = to_deg(*list(g.centroid.coords)[0])
            f60.append({"bodies": cc,
                        "area_m2": round(sum(rows[i][cols["area_m2"]] for i in cc), 1),
                        "reg": field(info, cols, rows[cc[0]], "reg"),
                        "addr": field(info, cols, rows[cc[0]], "addr"),
                        "quar": field(info, cols, rows[cc[0]], "quar"),
                        "lat": round(la, 6), "lon": round(lo, 6)})
        hole[f] = {"bodies": len(idx), "clusters": len(cl), "covered": cov, "free60": f60}
        print("   %-32s тела %5d · площадки %4d | непокрити: <=10 m %4d · <=30 m %4d · <=60 m %4d · <=120 m %4d"
              % (f, len(idx), len(cl), len(cl) - cov["10"], len(cl) - cov["30"],
                 len(cl) - cov["60"], len(cl) - cov["120"]))
    doc["hole"] = hole
    h("§3б · 6-те най-големи непокрити площадки (праг 60 m) на функция")
    for f, e in hole.items():
        print("   --- %s (%d непокрити)" % (f, len(e["free60"])))
        for s in sorted(e["free60"], key=lambda s: -s["area_m2"])[:6]:
            print("       %8.0f m2 · %2d тела · %-22s %-38s %.5f,%.5f"
                  % (s["area_m2"], len(s["bodies"]), (s["reg"] or "")[:22],
                     (s["addr"] or s["quar"] or "")[:38], s["lat"], s["lon"]))

    # ---- §4 контролните точки ---------------------------------------------
    h("§4 · КОНТРОЛНИТЕ ТОЧКИ НА ПЕТЪР")
    CP = [("а", "ул. Шести септември 6", 43.24473, 27.85411),
          ("б", "ж.к. Владислав Варненчик", 43.24456, 27.84592),
          ("в", "ж.к. Владислав Валненчик (typo)", 43.24946, 27.84414),
          ("г", "ул. Ниш 29", 43.24709, 27.85397)]
    cpout = []
    for tag, lab, lat, lon in CP:
        pt = Point(*to_m(lon, lat))
        ins = [int(i) for i in tree.query(pt) if polys[int(i)].covers(pt)]
        i = ins[0] if ins else int(min((polys[int(j)].distance(pt), int(j))
                                       for j in tree.query(pt.buffer(60)))[1])
        r = rows[i]
        e = dict(tag=tag, label=lab, i=i, func=field(info, cols, r, "func"),
                 prop=field(info, cols, r, "prop"), floors=r[cols["floors"]],
                 area_m2=r[cols["area_m2"]], reg=field(info, cols, r, "reg"),
                 addr=field(info, cols, r, "addr"), quar=field(info, cols, r, "quar"),
                 inside=bool(ins))
        cpout.append(e)
        print("   (%s) %-34s -> i=%-6d %s · %s · %s ет. · %.1f m2"
              % (tag, lab, i, e["func"], e["prop"], e["floors"], e["area_m2"]))
        print("        КАИС addr = %r · quar = %r · вътре=%s" % (e["addr"], e["quar"], bool(ins)))
    doc["control_points"] = cpout

    h("§4б · Владислав Варненчик: всички тела „Сграда за детско заведение“")
    rk = info["dict"]["reg"].index("район Владислав Варненчик")
    idx = [i for i, r in enumerate(rows)
           if r[fi] == dictf.index("Сграда за детско заведение") and r[cols["reg"]] == rk]
    cpi = {e["i"]: e["tag"] for e in cpout}
    vv = []
    for i in idx:
        p = polys[i]
        near = sorted((pts[int(j)].distance(p), int(j)) for j in ptree.query(p.buffer(200.0))
                      if dl[int(j)]["kind"] == "детска градина")
        d0, j0 = (near[0] if near else (None, None))
        vv.append(dict(i=i, area_m2=rows[i][cols["area_m2"]],
                       addr=field(info, cols, rows[i], "addr"),
                       quar=field(info, cols, rows[i], "quar"),
                       prop=field(info, cols, rows[i], "prop"),
                       nearest=(dl[j0]["name"] if j0 is not None else None),
                       nearest_d=(round(d0, 1) if d0 is not None else None),
                       cp=cpi.get(i)))
        print("   i=%-6d %7.1f m2 %-18s %-30s | най-близка доставена ДГ: %s%s"
              % (i, rows[i][cols["area_m2"]], (field(info, cols, rows[i], "prop") or "")[:18],
                 (field(info, cols, rows[i], "addr") or field(info, cols, rows[i], "quar") or "")[:30],
                 ("%s %.1f m" % (dl[j0]["name"][:26], d0)) if j0 is not None else "— (няма на 200 m)",
                 ("   [КТ %s]" % cpi[i] if i in cpi else "")))
    doc["vladislavovo_kindergartens"] = vv
    print("   тела: %d · с доставена ДГ на <=60 m: %d · с доставена ДГ на <=200 m: %d"
          % (len(vv), sum(1 for x in vv if x["nearest_d"] is not None and x["nearest_d"] <= 60),
             sum(1 for x in vv if x["nearest_d"] is not None)))

    # ---- §5 адресната машина към контролните точки -------------------------
    h("§5 · АДРЕСНАТА МАШИНА срещу контролните точки (кандидати, НЕ присъди)")
    ar = json.load(open(G + "Fire_Varna/data/address_rows.json", encoding="utf-8"))["rows"]
    GRP = {"а · ул. Шести септември 6": [18116, 18117],
           "б · ж.к. Вл. Варненчик 203 m2": [16753, 16754, 16755, 16756, 16757],
           "в · ж.к. Вл. Валненчик 190 m2": [16617, 16618, 16619],
           "г · ул. Ниш 29": [18347],
           "Георги Минков 2 (дворът)": [18334, 18335, 18336, 18337, 18338, 18339, 18340, 18341]}
    KEYS = ["ул шести септември 6", "бул владислав варненчик бл 9", "кв владиславово бл 402",
            "бул владислав варненчик бл 309", "кв владиславово бл 21", "кв владиславово бл 20",
            "ул ниш 29", "ул ниш 19"]
    a5 = {}
    for lab, ii in GRP.items():
        g = unary_union([polys[i] for i in ii])
        line = []
        for k in KEYS:
            rr = [r for r in ar if r[0] == k]
            if not rr:
                continue
            d = min(g.distance(Point(*to_m(r[2], r[1]))) for r in rr)
            if d <= 250:
                line.append([round(d, 1), k, len(rr)])
        line.sort()
        a5[lab] = line
        print("   --- %s" % lab)
        for d, k, n in line:
            print("       %7.1f m  „%s“  (%d реда)" % (d, k, n))
    doc["address_machine"] = a5

    # ---- §6 хотелите -------------------------------------------------------
    h("§6 · ХОТЕЛИТЕ: КАИС функции за настаняване")
    for f in ["Хотел", "Апартаментен хотел", "Курортна, туристическа сграда", "Общежитие"]:
        n = cnt.get(dictf.index(f), 0)
        e = hole.get(f)
        tail = ("" if not e else
                " · %4d площадки · %4d непокрити (<=60 m) · %4d непокрити (<=120 m)"
                % (e["clusters"], e["clusters"] - e["covered"]["60"],
                   e["clusters"] - e["covered"]["120"]))
        print("   %-32s %5d тела%s" % (f, n, tail))
    strict = sum(hole[f]["clusters"] - hole[f]["covered"]["60"]
                 for f in ("Хотел", "Апартаментен хотел"))
    print("   ДУПКАТА по строгото четене (Хотел + Апартаментен хотел): %d площадки" % strict)
    print("   Курортна, туристическа сграда: %d непокрити площадки — 1001 тела, но класът "
          "покрива и вили/бунгала, НЕ е доказателство за хотел"
          % (hole["Курортна, туристическа сграда"]["clusters"]
             - hole["Курортна, туристическа сграда"]["covered"]["60"]))

    json.dump(doc, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\nЗаписано: %s (%d записа в placement)" % (OUT, len(place)))


if __name__ == "__main__":
    main()
