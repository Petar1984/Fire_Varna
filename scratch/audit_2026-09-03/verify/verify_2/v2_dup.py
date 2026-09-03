# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №2 / находка №6 — независима проверка на дублетите в доставката."""
import json, math, re, difflib, unicodedata, sys, hashlib
FV = "C:/git/Fire_Varna/"
places = json.load(open(FV+"data/places.json", encoding="utf-8"))["places"]
hotels = json.load(open(FV+"data/hotels.json", encoding="utf-8"))["hotels"]
rows = ([dict(r, _set="places") for r in places] + [dict(r, _set="hotels") for r in hotels])
print("места=%d хотели=%d общо=%d" % (len(places), len(hotels), len(rows)))

def hav(a, b):
    R = 6371000.0
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    h = (math.sin((p2-p1)/2)**2 +
         math.cos(p1)*math.cos(p2)*math.sin(math.radians(b[1]-a[1])/2)**2)
    return 2*R*math.asin(math.sqrt(h))

# --- моя собствена нормализация (не преписвам чуждата) -----------------------
LATIN2CYR = {"O":"О","o":"о","A":"А","a":"а","E":"Е","e":"е","P":"Р","p":"р",
             "C":"С","c":"с","T":"Т","H":"Н","K":"К","k":"к","M":"М","B":"В",
             "X":"Х","x":"х","y":"у","I":"І"}
TYPE = set("""училище училища гимназия гимназии профилирана професионална частна частно
основно средно начално национално техникум техническа математическа езикова спортно
детска градина ясла детско заведение болница многопрофилна специализирана университетска
активно лечение хоспис дкц мбал умбал сбал сбалк център медицински хотел къща комплекс
оу су соу ну нуи пг мг пмг ег чоу чсу чег чпг втг вмг цплр пгтмд иток еад еоод оод ад
дг цдг одз одг дя чдг варна варненски по и на с за към при от""".split())
def core(s):
    t = "".join(LATIN2CYR.get(ch, ch) for ch in s)
    t = t.lower().replace("ё", "е")
    t = re.sub(r"[^\wа-я]+", " ", t, flags=re.U)
    ws = [w for w in t.split() if w and w not in TYPE and not w.isdigit()]
    return "".join(ws)
for r in rows:
    r["_core"] = core(r["name"])

# --- (1) МЕХАНИЧНАТА ПРОБА: точно същият скелет и ≤150 m ---------------------
exact150, exact_far, near5, fuzzy = [], [], [], []
for i in range(len(rows)):
    for j in range(i+1, len(rows)):
        A, B = rows[i], rows[j]
        d = hav((A["lat"], A["lon"]), (B["lat"], B["lon"]))
        same = A["_core"] and A["_core"] == B["_core"]
        if same and d <= 150: exact150.append((round(d,1), A["name"], B["name"]))
        if same and d > 150:  exact_far.append((round(d,1), A["name"], B["name"]))
        if d <= 5 and A["name"] != B["name"]: near5.append((round(d,1), A["name"], B["name"]))
        if A["_core"] and B["_core"] and not same:
            s = difflib.SequenceMatcher(None, A["_core"], B["_core"]).ratio()
            if s >= 0.84: fuzzy.append((round(s,3), round(d,1), A["name"], B["name"]))
print("\n(1) точен скелет ≤150 m:", len(exact150))
for x in sorted(exact150): print("   ", x)
print("(1б) точен скелет >150 m:", len(exact_far))
for x in sorted(exact_far, reverse=True): print("   ", x)
print("(2) ≤5 m с различни имена:", len(near5))
for x in sorted(near5): print("   ", x)
print("(3) размит скелет ≥0.84 (БЕЗ праг за разстояние):", len(fuzzy))
for x in sorted(fuzzy, reverse=True): print("   ", x)

# --- (4) поименно: шестте твърдения на находката ------------------------------
def find(sub, s=None):
    return [r for r in rows if sub.lower() in r["name"].lower() and (s is None or r["_set"] == s)]
print("\n(4) ПОИМЕННО")
def pair_report(tag, la, lb):
    for a in la:
        for b in lb:
            if a is b: continue
            d = hav((a["lat"], a["lon"]), (b["lat"], b["lon"]))
            print(f"  {tag}: {d:9.1f} m | {a['name']!r} ({a['lat']},{a['lon']},src={a.get('src')}) "
                  f"<-> {b['name']!r} ({b['lat']},{b['lon']},src={b.get('src')})")
            print(f"      core_a={a['_core']!r} core_b={b['_core']!r} равни={a['_core']==b['_core']} "
                  f"ratio={difflib.SequenceMatcher(None,a['_core'],b['_core']).ratio():.3f}")
t = find("текстил"); pair_report("ПГТМД", t, t)
e = find("зюпери"); pair_report("Екзюпери", e, e)
a = find("арабаджиев"); pair_report("Арабаджиев", a, a)
y = find("явор") + find("голдън"); pair_report("Явор/Голдън", find("явор"), find("голдън"))
k = find("кардиолайф") + find("СБАЛК"); pair_report("СБАЛК", find("СБАЛК"), find("СБАЛК"))
dz = find("диспансер") ; dg = find("52")
pair_report("Диспансер/ДГ52", dz, [x for x in dg if "лястовиц" in x["name"].lower()])
ig = find("иглика"); pair_report("Иглика", ig, ig)
