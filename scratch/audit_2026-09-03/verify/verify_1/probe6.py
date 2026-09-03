# -*- coding: utf-8 -*-
"""Оборител №1 · находка №6 — моя собствена проба „същият скелет ≤150 m“ + по-силни проби."""
import json, math, re, difflib
FV = r"C:/git/Fire_Varna"

def hav(la1, lo1, la2, lo2):
    R = 6371008.8
    p1, p2 = math.radians(la1), math.radians(la2)
    a = math.sin((p2-p1)/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(math.radians(lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(a))

places = json.load(open(FV+"/data/places.json", encoding="utf-8"))["places"]
hotels = json.load(open(FV+"/data/hotels.json", encoding="utf-8"))["hotels"]
rows = [dict(r, set="places") for r in places] + [dict(r, set="hotels") for r in hotels]

QUOTES = '"\u201e\u201c\u201d\u00ab\u00bb\u2019\u2018\''
# моят собствен списък типови думи (независим от measure_places.py)
TYPE = ["дг","цдг","одз","одг","дя","чдг","детска","градина","ясла","ясли","детски",
        "оу","су","сou","пг","пгт","гимназия","професионална","профилирана","частна",
        "училище","начално","основно","средно","хотел","семеен","парк","апартхотел",
        "еоод","оод","еад","ад","болница","специализирана","дкц","мц","хоспис","за",
        "по","и","на","с","център","медицински","университет","колеж","зa"]

def skel(s, drop_digits=True):
    t = "".join(" " if ch in QUOTES else ch for ch in s).lower()
    t = re.sub(r"/[^/]*/", " ", t)
    t = re.sub(r"[\u2116#\-.,()]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    ws = [w for w in t.split() if w not in TYPE]
    t = " ".join(ws)
    if drop_digits:
        t = re.sub(r"\d+", " ", t)
    return re.sub(r"[^\u0430-\u044fa-z0-9]", "", t)

for r in rows:
    r["skel"] = skel(r["name"])

# --- A. моята проба „идентичен скелет ≤150 m“
A, A_far = [], []
for i in range(len(rows)):
    for j in range(i+1, len(rows)):
        a, b = rows[i], rows[j]
        if a["skel"] and a["skel"] == b["skel"]:
            d = hav(a["lat"], a["lon"], b["lat"], b["lon"])
            (A if d <= 150 else A_far).append((round(d,1), a["name"], b["name"]))
print("A) идентичен скелет ≤150 m : %d двойки" % len(A))
for x in sorted(A): print("   ", x)
print("A') идентичен скелет >150 m : %d двойки" % len(A_far))
for x in sorted(A_far)[:8]: print("   ", x)

# --- B. по-силна проба: difflib върху скелета, без праг за разстояние
CHECK = {("ПГ по текстил и моден дизайн","Професионална Гимназия по Текстил и Моден Дизайн"),
         ('ПГ ИТOK "Екзюпери"','Частна профилирана гимназия "Антонан дьо Сент-Екзюпери"'),
         ('ОУ "Константин Арабаджиев"',"ОУ „Константин Арабаджиев“"),
         ("ГОЛДЪН ЛАЙН","Явор"),
         ("Диспансер за белодробни заболявания","ДГ№52 „Бялата лястовица\"")}
def in_check(a,b): return (a,b) in CHECK or (b,a) in CHECK

for thr in (0.90, 0.84, 0.80, 0.70):
    hits, tp = 0, 0
    for i in range(len(rows)):
        for j in range(i+1, len(rows)):
            a, b = rows[i], rows[j]
            if not a["skel"] or not b["skel"]: continue
            s = difflib.SequenceMatcher(None, a["skel"], b["skel"]).ratio()
            if s >= thr:
                hits += 1
                if in_check(a["name"], b["name"]): tp += 1
    print("B) difflib(скелет) >= %.2f : %d двойки общо, от 5-те целеви хванати %d" % (thr, hits, tp))

# --- C. „подниз“: скелетът на единия се съдържа в скелета на другия (>=8 знака)
sub = []
for i in range(len(rows)):
    for j in range(i+1, len(rows)):
        a, b = rows[i]["skel"], rows[j]["skel"]
        if len(a) >= 8 and len(b) >= 8 and (a in b or b in a) and a != b:
            sub.append((round(hav(rows[i]["lat"],rows[i]["lon"],rows[j]["lat"],rows[j]["lon"]),1),
                        rows[i]["name"], rows[j]["name"]))
print("C) единият скелет е подниз на другия (>=8 знака): %d двойки" % len(sub))
for x in sorted(sub): print("   ", x)

# --- D. близост
for lim in (5, 25, 50, 120):
    n = sum(1 for i in range(len(rows)) for j in range(i+1, len(rows))
            if hav(rows[i]["lat"],rows[i]["lon"],rows[j]["lat"],rows[j]["lon"]) <= lim)
    print("D) двойки на <= %3d m : %d" % (lim, n))
