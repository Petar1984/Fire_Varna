# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №2 · находка №4 — колко от „еднозначните дворове" издържат
адресна проверка в КАИС (а не само близост).  READ-ONLY.
    python v2_kais.py
"""
from __future__ import annotations
import json, math, re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
V3 = Path("C:/git/varna_3d")

info = json.loads((V3 / "web/varna_buildings_info.json").read_text(encoding="utf-8"))
DICT, ROWS, COLS = info["dict"], info["rows"], info["columns"]
ci = {c: k for k, c in enumerate(COLS)}
gj = json.loads((V3 / "web/varna_buildings_3d.geojson").read_text(encoding="utf-8"))
feats = gj["features"]
print("features:", len(feats), "| rows:", len(ROWS))


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


def dec(col, r):
    v = r[ci[col]]
    if col in DICT:
        return "" if v == -1 else DICT[col][v]
    return v


IDX = {}
for f in feats:
    i = f["properties"].get("i")
    if i is None:
        continue
    IDX[i] = f

def hav(a, b, c, d):
    p1, p2 = math.radians(a), math.radians(c)
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(d - b) / 2) ** 2
    return 2 * 6371000.0 * math.asin(math.sqrt(h))


def search(pattern, min_area=0.0):
    rx = re.compile(pattern, re.I)
    out = []
    for i, r in enumerate(ROWS):
        a = dec("addr", r)
        if a and rx.search(a):
            if r[ci["area_m2"]] >= min_area:
                f = IDX.get(i)
                la, lo = centroid(f["geometry"]) if f else (None, None)
                out.append({"i": i, "addr": a, "func": dec("func", r), "area": r[ci["area_m2"]],
                            "floors": r[ci["floors"]], "lat": la, "lon": lo, "quar": dec("quar", r)})
    return out


CASES = [
    ("ДГ№16 „Слънчева Дъга“ · ул. Уйлям Гладстон 5", r"гладстон", (43.217433, 27.920787)),
    ("ДГ№25 „Златното зрънце“ · ж.к. Младост до бл.127", r"младост.*127|127.*младост", (43.2318, 27.8735)),
    ("ДГ№53 „Слънчево зайче“ · ул. Кап. Райчо Николов 103А", r"капитан райчо|кап\.?\s*райчо", (43.2149, 27.8941)),
    ("ДГ№6 „Палечко“ · ул. Тодор Влайков 71", r"тодор влайков\D*71", (43.20819, 27.889012)),
    ("ДГ№19 „Славейче“ · ул. Студентска 7", r"студентска\D*7\b", (43.222673, 27.93343)),
    ("ДГ№2 „Щастливо детство“ · ул. Барутен погреб 6", r"барутен погреб", (43.203677, 27.898279)),
]
for title, pat, (la, lo) in CASES:
    print("\n===", title)
    hits = search(pat)
    hits.sort(key=lambda h: -h["area"])
    print("   КАИС тела с този адресен низ:", len(hits))
    for h in hits[:8]:
        d = hav(la, lo, h["lat"], h["lon"]) if h["lat"] else -1
        print(f"     i={h['i']:<7} {h['area']:8.1f} m2  ет={h['floors']}  d={d:7.0f} m  func={h['func'][:28]:28} | {h['addr'][:52]}")

# функционалният клас: има ли изобщо „детска градина“ в КАИС func
print("\n=== КАИС func-стойности, съдържащи „дет“ / „градин“ / „учил“:")
from collections import Counter
cnt = Counter()
for r in ROWS:
    fu = dec("func", r)
    if fu and re.search(r"дет|градин|учил", fu, re.I):
        cnt[fu] += 1
for k, v in cnt.most_common(20):
    print(f"   {v:6}  {k}")
