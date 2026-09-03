# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №2 · находка №4 — независима реплика на числата за детските градини.
READ-ONLY: чете само C:/git/Fire_Varna и C:/git/varna_3d.
    python v2_dg.py
"""
from __future__ import annotations
import json, math, re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
FV = Path("C:/git/Fire_Varna")
V3 = Path("C:/git/varna_3d")
OUT = Path(__file__).resolve().parent

# ---------------------------------------------------------------- 1. регистър
raw = (V3 / "scratch/refactor/_addr/kimi_obrazovanie.txt").read_text(encoding="utf-8").splitlines()
reg_lines = [ln for ln in raw[405:458] if ln.strip()]
REG = []
for ln in reg_lines:
    parts = ln.split("|")
    m = re.match(r"^\s*ДГ\s*[№#]?\s*(\d+)\s*(.*)$", parts[0])
    assert m, ln
    num = int(m.group(1))
    nm = m.group(2)
    REG.append({"num": num, "raw": parts[0].strip(), "name": nm.strip(),
                "addr": parts[1].strip() if len(parts) > 1 else "",
                "rajon": parts[2].strip() if len(parts) > 2 else ""})
assert len(REG) == 53, len(REG)
assert sorted(r["num"] for r in REG) == list(range(1, 54))

QUOTES = '"\u201e\u201c\u201d\u00ab\u00bb\u2018\u2019\u2033\u2032`\u00b4\''
def core(s: str) -> str:
    t = "".join(" " if ch in QUOTES else ch for ch in s).lower()
    t = t.replace("\u0451", "\u0435")
    t = re.sub(r"/[^/]*/", " ", t)          # /с яслена група/
    t = re.sub(r"\(.*?\)", " ", t)
    for tok in ("оздравителна детска градина", "логопедична", "детска градина",
                "детска ясла", "чцдг", "чдг", "цдг", "одз", "одг", "дя", "дг",
                "филиал", "ясла", "с яг"):
        t = re.sub(r"(?:^|[\s\-\u2116#.])" + re.escape(tok) + r"(?:[\s\-\u2116#.]|$)", " ", t)
    t = re.sub(r"[^\u0430-\u044f\u0430-\u044fa-z]", "", t)
    return t

for r in REG:
    r["core"] = core(r["name"])

# ---------------------------------------------------------------- 2. доставка
places = json.loads((FV / "data/places.json").read_text(encoding="utf-8"))["places"]
DG = [p for p in places if p["kind"] == "детска градина"]

def is_nursery(name: str) -> bool:
    t = "".join(" " if ch in QUOTES else ch for ch in name).lower()
    return bool(re.search(r"(^|[\s\.])(дя|детска ясла|ясла)(\s|$|[\u2116#\d\(])", t))

def is_private(name: str) -> bool:
    return bool(re.search(r"(^|\s)(чдг|чцдг)(\s|$|[\u2116#\d\u201e\"])", name.lower()))

def hav(a, b, c, d):
    p1, p2 = math.radians(a), math.radians(c)
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(d - b) / 2) ** 2
    return 2 * 6371000.0 * math.asin(math.sqrt(h))

rows_by_core = {}
for r in REG:
    rows_by_core.setdefault(r["core"], []).append(r)

report = []
for p in sorted(DG, key=lambda x: x["name"]):
    c = core(p["name"])
    cls, hit = None, None
    if is_nursery(p["name"]):
        cls = "ясла"
    elif is_private(p["name"]):
        cls = "частна"
    else:
        cand = rows_by_core.get(c) or [r for r in REG if c and (c in r["core"] or r["core"] in c) and min(len(c), len(r["core"])) >= 4]
        if len(cand) == 1:
            cls, hit = "общинска", cand[0]["num"]
        elif len(cand) > 1:
            cls, hit = "общинска?", [x["num"] for x in cand]
        else:
            cls = "БЕЗ СЪОТВЕТНИК"
    report.append({"name": p["name"], "core": c, "class": cls, "reg": hit,
                   "lat": p["lat"], "lon": p["lon"], "zone": p.get("zone"), "src": p.get("src")})

print("=== доставени под клас „детска градина“:", len(DG))
for r in report:
    print(f"  {r['class']:>15} | reg={r['reg']} | {r['name']}")

from collections import Counter
print("\n=== разпад по клас:", Counter(r["class"] for r in report))
muni_rows = [r for r in report if r["class"].startswith("общинска")]
covered = sorted({r["reg"] for r in muni_rows if isinstance(r["reg"], int)})
print("общински РЕДОВЕ:", len(muni_rows), "| покрити УНИКАЛНИ регистрови №:", len(covered))
print("покрити №:", covered)
missing = [r for r in REG if r["num"] not in covered]
print("ЛИПСВАЩИ:", len(missing), "->", [r["num"] for r in missing])
print("покритие %:", round(100.0 * len(covered) / 53, 2))
city = [r for r in missing if "гр. Варна" in r["addr"] or "гр.Варна" in r["addr"]]
nocity = [r for r in missing if r not in city]
print("липсващи с адрес „гр. Варна“:", len(city), [r["num"] for r in city])
print("липсващи БЕЗ „гр. Варна“:", len(nocity), [(r['num'], r['addr']) for r in nocity])

json.dump({"report": report, "covered": covered,
           "missing": [{"num": r["num"], "name": r["name"], "addr": r["addr"]} for r in missing]},
          open(OUT / "v2_dg.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
