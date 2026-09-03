# -*- coding: utf-8 -*-
"""Оборител №1 · находка №6 — независима проверка на разстоянията и на пробата."""
import json, math, re, itertools, unicodedata, sys
FV = r"C:/git/Fire_Varna"

def hav(la1, lo1, la2, lo2):
    R = 6371008.8
    p1, p2 = math.radians(la1), math.radians(la2)
    dp = p2 - p1
    dl = math.radians(lo2 - lo1)
    a = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(a))

places = json.load(open(FV+"/data/places.json", encoding="utf-8"))["places"]
hotels = json.load(open(FV+"/data/hotels.json", encoding="utf-8"))["hotels"]
rows = [dict(r, set="places") for r in places] + [dict(r, set="hotels") for r in hotels]
print("N places=%d  N hotels=%d  N rows=%d" % (len(places), len(hotels), len(rows)))

def find(sub, s="both"):
    out = []
    for r in rows:
        if sub.lower() in r["name"].lower():
            out.append(r)
    return out

PAIRS = [
    ("ПГ по текстил и моден дизайн", "Професионална Гимназия по Текстил и Моден Дизайн"),
    ("ПГ ИТOK", "Антонан дьо Сент-Екзюпери"),
    ('ОУ "Константин Арабаджиев"', "ОУ „Константин Арабаджиев“"),
    ("ГОЛДЪН ЛАЙН", "Явор"),
    ("Диспансер за белодробни заболявания", "ДГ№52"),
    ("Кардиолайф", "по кардиология Варна"),
    ("Иглика-2", "Иглика"),
]
print("\n--- разстояния (моята хаверсинова функция, R=6371008.8 m) ---")
for a, b in PAIRS:
    A = [r for r in rows if a in r["name"]]
    B = [r for r in rows if b in r["name"] and r["name"] not in [x["name"] for x in A]]
    if len(A) != 1 or len(B) < 1:
        print("!! %-40s -> A=%d B=%d" % (a, len(A), len(B)))
        continue
    B = [x for x in B if x["name"] != A[0]["name"]]
    B0 = min(B, key=lambda x: hav(A[0]["lat"], A[0]["lon"], x["lat"], x["lon"]))
    d = hav(A[0]["lat"], A[0]["lon"], B0["lat"], B0["lon"])
    print("%8.1f m  | %s (%s) <-> %s (%s)" % (d, A[0]["name"], A[0]["src"], B0["name"], B0["src"]))
