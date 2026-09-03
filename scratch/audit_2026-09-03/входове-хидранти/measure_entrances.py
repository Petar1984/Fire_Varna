# -*- coding: utf-8 -*-
"""
ОДИТ „входове-хидранти" — 03.09.2026. READ-ONLY.
Изход: entrances_join.json, entrance_duplicates.json, hydrants_quick.json
Всяко число се печата на stdout със своята мярка.
Пускане: PYTHONIOENCODING=utf-8 python measure_entrances.py
"""
import json, sys, math, re, collections, unicodedata, os, subprocess
sys.stdout.reconfigure(encoding='utf-8')

VB   = r"C:/git/Varna_buildings/output"
FV   = r"C:/git/Fire_Varna/data"
OUT  = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- зареждане
GEO = json.load(open(VB + "/geocoder_index.json", encoding="utf-8"))
SU  = json.load(open(VB + "/section_units.json", encoding="utf-8"))
EIX = json.load(open(VB + "/search_index_entrances.json", encoding="utf-8"))
SI  = json.load(open(VB + "/strategic_intel.json", encoding="utf-8"))
DEL = json.load(open(FV + "/search_index.json", encoding="utf-8"))
ARW = json.load(open(FV + "/address_rows.json", encoding="utf-8"))

gent  = GEO["entries"]
dent  = DEL["entries"]
arows = ARW["rows"]
dnames = DEL.get("district_names") or []

print("=== ИЗВОРИ ===")
print("geocoder_index.entries               : %d" % len(gent))
print("section_units.json секции            : %d" % len(SU))
print("search_index_entrances documents     : %d   (strategic_intel source_data_date=%s)"
      % (EIX["documentCount"], SI["source_data_date"]))
print("strategic_intel.counts.entrance_groups: %d" % SI["counts"]["entrance_groups"])
print("Fire_Varna search_index.entries      : %d" % len(dent))
print("Fire_Varna address_rows.rows         : %d" % len(arows))

# ---------------------------------------------------------------- нормализация
LAT2CYR = {"A":"А","B":"В","E":"Е","K":"К","M":"М","H":"Н","O":"О","P":"Р",
           "C":"С","T":"Т","X":"Х","Y":"У"}
def nen(v):
    """нормализиран етикет на вход: NFKC, без кавички/интервали, главни, латиница->кирилица"""
    if v is None:
        return None
    s = unicodedata.normalize("NFKC", str(v)).strip()
    s = s.strip('"\u201c\u201d\u00ab\u00bb\'')
    s = re.sub(r"\s+", "", s)
    s = s.upper()
    return "".join(LAT2CYR.get(ch, ch) for ch in s)

def is_composite(v):
    """съставен/мръсен етикет: разделител, съюз „и", „тяло", скоба, две+ букви"""
    if v is None:
        return False
    s = unicodedata.normalize("NFKC", str(v)).strip().upper()
    if re.search(r"[,/]", s):                  return True
    if re.search(r"(^|\s)И(\s|$)", s):         return True
    if "ТЯЛО" in s:                            return True
    if "(" in s:                               return True
    if re.search(r"[-\u2013\u2014]", s):       return True
    n = nen(s) or ""
    if re.fullmatch(r"[А-Я]{2,}", n):          return True
    return False

def norm_label(s):
    """точното norm() от index.html:4839 (UI дедуп ключ)"""
    s = ("" if s is None else str(s)).lower().replace("блок", "бл").replace("вход", "вх")
    s = re.sub(r"[.№,'\"\-]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

R = 6371000.0
def hav(la1, ln1, la2, ln2):
    p = math.pi / 180.0
    dla = (la2 - la1) * p
    dln = (ln2 - ln1) * p
    z = math.sin(dla/2)**2 + math.cos(la1*p) * math.cos(la2*p) * math.sin(dln/2)**2
    return 2 * R * math.asin(math.sqrt(z))

def mask(c):
    """кадастрален номер -> публична маска 10135.xxxx.xxxx.N"""
    if not c:
        return c
    p = str(c).split(".")
    out = [p[0]]
    for i, seg in enumerate(p[1:], start=1):
        out.append(seg if i >= 3 else "xxxx")
    return ".".join(out)

# ================================================================ М0: мост геокодер -> доставка
print("\n=== М0: мостът геокодер -> доставка (входовите редове) ===")
gEn = [e for e in gent if "en" in e]
dEn = [e for e in dent if "en" in e]
print("геокодер редове с 'en'               : %d" % len(gEn))
print("доставка редове с 'en' (kind=mf)     : %d" % len(dEn))
bad_pin = 0
bad_en  = 0
nmin = min(len(gEn), len(dEn))
for i in range(nmin):
    g, d = gEn[i], dEn[i]
    if list(g["pin"]) != list(d["pin"]):
        bad_pin += 1
    if str(g["en"]) != str(d["en"]):
        bad_en += 1
bridge_ok = (len(gEn) == len(dEn) and bad_pin == 0 and bad_en == 0)
print("несъвпадащи pin по позиция           : %d" % bad_pin)
print("несъвпадащи en по позиция            : %d" % bad_en)
print("мостът е 1:1 и подреден              : %s" % bridge_ok)

DELV = []
for i in range(nmin):
    g, d = gEn[i], dEn[i]
    DELV.append({
        "i": i,
        "cad": g.get("section_cadnum") or g.get("cadnum"),
        "en_raw": d["en"], "en": nen(d["en"]),
        "lat": d["pin"][0], "lng": d["pin"][1],
        "g": d.get("g"), "display_id": d.get("display_id"),
        "label_field": d.get("label"), "d": d.get("d"),
    })

# ================================================================ М1 (а): section_units <-> доставка
print("\n=== М1 (а): section_units.json <-> доставката, ред по ред по (сграда, вход) ===")
au = []
au_null = 0
for u in SU:
    for e in (u.get("entrances") or []):
        if e.get("en") is None:
            au_null += 1
            continue
        au.append({"cad": u["section_cadnum"], "en_raw": e["en"], "en": nen(e["en"]),
                   "lat": e.get("lat"), "lng": e.get("lng"),
                   "n_apt": e.get("n_apt"), "label": u.get("label"),
                   "btype": u.get("building_type")})
print("входови записа в section_units       : %d" % (au_null + len(au)))
print("  · без буква/номер (en=null)        : %d   <- никога не стават търсим вход" % au_null)
print("  · с етикет (авторитет)             : %d" % len(au))

A = collections.Counter((x["cad"], x["en"]) for x in au)
D = collections.Counter((x["cad"], x["en"]) for x in DELV)
a_keys, d_keys = set(A), set(D)
both = a_keys & d_keys
print("уникални (сграда,вход) в авторитета  : %d" % len(a_keys))
print("уникални (сграда,вход) в доставката  : %d" % len(d_keys))
print("в авторитета, но НЕ в доставката     : %d" % len(a_keys - d_keys))
print("в доставката, но НЕ в авторитета     : %d" % len(d_keys - a_keys))
cov_a = 100.0 * len(both) / len(a_keys)
cov_d = 100.0 * len(both) / len(d_keys)
print("покритие авторитет -> доставка       : %d/%d = %.2f %%" % (len(both), len(a_keys), cov_a))
print("покритие доставка -> авторитет       : %d/%d = %.2f %%" % (len(both), len(d_keys), cov_d))
print("сгради с етикетиран вход (авторитет) : %d" % len(set(x["cad"] for x in au)))
print("сгради с етикетиран вход (доставка)  : %d" % len(set(x["cad"] for x in DELV)))

aidx = {}
for x in au:
    aidx.setdefault((x["cad"], x["en"]), x)
coord_d = []
for x in DELV:
    k = (x["cad"], x["en"])
    if k in aidx and aidx[k]["lat"] is not None:
        coord_d.append(hav(aidx[k]["lat"], aidx[k]["lng"], x["lat"], x["lng"]))
coord_d.sort()
if coord_d:
    print("координатна разлика авторитет/доставка: max=%.2f m · p99=%.2f m · >1 m: %d от %d"
          % (coord_d[-1], coord_d[int(0.99*len(coord_d))], sum(1 for v in coord_d if v > 1), len(coord_d)))

# ================================================================ М2 (б): 5314 <-> доставка
print("\n=== М2 (б): search_index_entrances (5 314, извор %s) <-> доставката (4 764) ===" % SI["source_data_date"])
E5 = [dict(v) for v in EIX["storedFields"].values()]
for e in E5:
    e["en"] = nen(e["entrance"])
print("документи в стария входов индекс     : %d" % len(E5))
print("  · уникални сгради                  : %d" % len(set(e["building_cadnum"] for e in E5)))
print("  · съставни/мръсни етикети          : %d" % sum(1 for e in E5 if is_composite(e["entrance"])))

d_by_key = collections.defaultdict(list)
d_by_cad = collections.defaultdict(list)
for x in DELV:
    d_by_key[(x["cad"], x["en"])].append(x)
    d_by_cad[x["cad"]].append(x)

su_sections = {u["section_cadnum"]: u for u in SU}
geo_cads = set(e.get("cadnum") for e in gent)

CELL = 0.0015
grid = collections.defaultdict(list)
for x in DELV:
    grid[(int(x["lat"]/CELL), int(x["lng"]/CELL))].append(x)

def nearest(lat, lng, letter=None):
    gi, gj = int(lat/CELL), int(lng/CELL)
    best = None
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            for e in grid.get((gi+di, gj+dj), ()):
                if letter is not None and e["en"] != letter:
                    continue
                dd = hav(lat, lng, e["lat"], e["lng"])
                if best is None or dd < best[0]:
                    best = (dd, e)
    return best

key_hit = cad_only = no_cad = 0
buckets = collections.Counter()
unmatched_rows = []
for e in E5:
    k = (e["building_cadnum"], e["en"])
    if d_by_key.get(k):
        key_hit += 1
        continue
    same_cad  = d_by_cad.get(e["building_cadnum"])
    nn_letter = nearest(e["lat"], e["lng"], e["en"])
    nn_any    = nearest(e["lat"], e["lng"], None)
    if same_cad:
        cad_only += 1
    else:
        no_cad += 1
    b = ("няма същата буква в 150 m" if nn_letter is None else
         "<=5 m" if nn_letter[0] <= 5 else
         "5-25 m" if nn_letter[0] <= 25 else
         "25-100 m" if nn_letter[0] <= 100 else ">100 m")
    buckets[b] += 1
    sec = su_sections.get(e["building_cadnum"])
    unmatched_rows.append({
        "cad": e["building_cadnum"], "entrance": e["entrance"], "en_norm": e["en"],
        "lat": e["lat"], "lng": e["lng"], "units": e["unit_count"], "residential": e["residential"],
        "cad_in_delivery": bool(same_cad),
        "cad_in_section_units": sec is not None,
        "section_btype": (sec or {}).get("building_type"),
        "section_label": (sec or {}).get("label"),
        "section_entrances_in_delivery": sorted(x["en_raw"] for x in (same_cad or [])),
        "cad_in_geocoder": e["building_cadnum"] in geo_cads,
        "composite": is_composite(e["entrance"]),
        "nn_same_letter_m": None if nn_letter is None else round(nn_letter[0], 1),
        "nn_any_letter_m": None if nn_any is None else round(nn_any[0], 1),
        "nn_any_letter": None if nn_any is None else nn_any[1]["en_raw"],
        "bucket": b,
    })

tot5 = len(E5)
print("съвпадат по (кадастрален №, вход)    : %d/%d = %.1f %%   <- ДОКАЗАНО доставени"
      % (key_hit, tot5, 100.0*key_hit/tot5))
print("НЕ съвпадат по ключ                  : %d" % (tot5 - key_hit))
print("  · сградата я има в доставката, буквата — не : %d" % cad_only)
print("  · сградата изобщо я няма в доставката       : %d" % no_cad)
print("  разбивка по разстояние до най-близкия доставен вход СЪС СЪЩАТА буква:")
for kk in ["<=5 m", "5-25 m", "25-100 m", ">100 m", "няма същата буква в 150 m"]:
    v = buckets.get(kk, 0)
    print("    %-28s %5d  (%4.1f %% от 5 314)" % (kk, v, 100.0*v/tot5))
soft = key_hit + buckets.get("<=5 m", 0) + buckets.get("5-25 m", 0)
print("мярката на критика (само буква + <=25 m, БЕЗ кадастрален ключ): 4 289/5 314 = 80.7 %")
print("строгата мярка (кадастрален № + вход)                        : %d/5 314 = %.1f %%" % (key_hit, 100.0*key_hit/tot5))
print("смекчена (ключ ИЛИ <=25 m със същата буква)                  : %d/5 314 = %.1f %%" % (soft, 100.0*soft/tot5))

print("\n-- защо не са доставени (профил на несъвпадналите) --")
prof = collections.Counter()
for r in unmatched_rows:
    if not r["cad_in_section_units"]:
        prof["сградата я няма като секция в section_units (15.08)"] += 1
    elif not r["cad_in_delivery"]:
        prof["секцията съществува, но без НИТО ЕДИН етикетиран вход в доставката"] += 1
    elif r["composite"]:
        prof["съставен/мръсен етикет ('А,Б', '1 и 2', 'А-5')"] += 1
    else:
        prof["чист етикет, но буквата липсва в новия извор"] += 1
for k, v in prof.most_common():
    print("   %5d  %s" % (v, k))
res_lost = sum(r["residential"] for r in unmatched_rows)
print("жилища зад несъвпадналите входове    : %d" % res_lost)
print("  · от тях в група „>100 m / няма буква\": %d"
      % sum(r["residential"] for r in unmatched_rows if r["bucket"] in (">100 m", "няма същата буква в 150 m")))
print("  · типове сгради на несъвпадналите (по section_units): "
      + " · ".join("%s=%d" % (k, v) for k, v in
                   collections.Counter(r["section_btype"] for r in unmatched_rows).most_common(6)))

print("\n-- 6 примера за НЕдоставени входове (кадастралните № маскирани) --")
for r in sorted([x for x in unmatched_rows if x["bucket"] in (">100 m", "няма същата буква в 150 m")],
                key=lambda r: -r["units"])[:6]:
    print("   %s  вх.„%s\"  обекти=%d жил.=%d  %s,%s  · %s  · най-близък същ.буква=%s m · най-близък изобщо=%s m (вх.%s)"
          % (mask(r["cad"]), r["entrance"], r["units"], r["residential"], r["lat"], r["lng"],
             r["section_label"] or "(няма секция 15.08)", r["nn_same_letter_m"],
             r["nn_any_letter_m"], r["nn_any_letter"]))

# ================================================================ М3 (в): дублирани входове
print("\n=== М3 (в): ДУБЛИРАНИ входове в доставката ===")
dup_key = {k: v for k, v in d_by_key.items() if len(v) > 1}
print("един и същ (кадастрален №, вход) >1 път : %d групи · %d записа"
      % (len(dup_key), sum(len(v) for v in dup_key.values())))
dup_g_all = collections.defaultdict(list)
for x in DELV:
    dup_g_all[(x["g"], x["en"])].append(x)
dup_g = {k: v for k, v in dup_g_all.items() if len(v) > 1}
print("един и същ (публична група g, вход) >1 път: %d групи · %d записа"
      % (len(dup_g), sum(len(v) for v in dup_g.values())))

coord_groups = collections.defaultdict(list)
for x in DELV:
    coord_groups[(x["lat"], x["lng"])].append(x)
coord_dup = {k: v for k, v in coord_groups.items() if len(v) > 1}
print("входове с ИДЕНТИЧНА координата       : %d групи · %d записа"
      % (len(coord_dup), sum(len(v) for v in coord_dup.values())))
cd_same_b = sum(1 for v in coord_dup.values() if len(set(x["cad"] for x in v)) == 1)
print("  · от тях в една и съща сграда      : %d групи" % cd_same_b)
print("  · през РАЗЛИЧНИ сгради             : %d групи" % (len(coord_dup) - cd_same_b))

def base_label(x):
    if x["label_field"]:
        return re.sub(r"\s+", " ", str(x["label_field"]).replace("|", " ")).strip()
    di = x["display_id"]
    if di is not None and 0 <= di < len(arows):
        na = arows[di][0]
        if na:
            return na
    if x["d"] is not None and x["d"] < len(dnames):
        return dnames[x["d"]]
    return "(адрес)"

for x in DELV:
    x["shown"]  = base_label(x) + " · вх. " + str(x["en_raw"])
    x["nshown"] = norm_label(x["shown"])

txt = collections.defaultdict(list)
for x in DELV:
    txt[x["nshown"]].append(x)
txt_multi  = {k: v for k, v in txt.items() if len(v) > 1}
txt_diffg  = {k: v for k, v in txt_multi.items() if len(set(x["g"] for x in v)) > 1}
print("еднакъв ПОКАЗВАН текст, >1 запис     : %d групи · %d записа"
      % (len(txt_multi), sum(len(v) for v in txt_multi.values())))
print("  · през РАЗЛИЧНИ сгради (различен g -> UI-дедупът НЕ ги слива): %d групи · %d записа   (предишна мярка: 182/418)"
      % (len(txt_diffg), sum(len(v) for v in txt_diffg.values())))
print("  · в една и съща група g (UI-дедупът ги слива до 1 ред): %d групи · %d записа"
      % (len(txt_multi) - len(txt_diffg),
         sum(len(v) for v in txt_multi.values()) - sum(len(v) for v in txt_diffg.values())))

spread = collections.Counter()
txt_rows = []
for k, v in txt_diffg.items():
    mx = 0.0
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            mx = max(mx, hav(v[i]["lat"], v[i]["lng"], v[j]["lat"], v[j]["lng"]))
    b = ("<=25 m" if mx <= 25 else "25-100 m" if mx <= 100 else
         "100-500 m" if mx <= 500 else "500-2000 m" if mx <= 2000 else ">2000 m")
    spread[b] += 1
    txt_rows.append({"shown": v[0]["shown"], "n": len(v), "max_m": round(mx, 1),
                     "cads": [x["cad"] for x in v], "gs": sorted(set(x["g"] for x in v)),
                     "pins": [[x["lat"], x["lng"]] for x in v]})
print("  разстояние между най-отдалечените в групата:")
for kk in ["<=25 m", "25-100 m", "100-500 m", "500-2000 m", ">2000 m"]:
    print("    %-12s %4d групи" % (kk, spread.get(kk, 0)))

print("\n-- 6 примера за еднакъв показван текст на различни сгради --")
for r in sorted(txt_rows, key=lambda r: -r["max_m"])[:6]:
    print("   „%s\"  x%d  раздалечени до %s m  · %s"
          % (r["shown"], r["n"], r["max_m"],
             " | ".join("%s@%s,%s" % (mask(c), p[0], p[1]) for c, p in zip(r["cads"], r["pins"]))))

print("\n-- 6 примера за идентична координата --")
for (la, ln), v in sorted(coord_dup.items(), key=lambda kv: -len(kv[1]))[:6]:
    print("   %s,%s  x%d  входове: %s  сгради: %s  показва: %s"
          % (la, ln, len(v), [x["en_raw"] for x in v],
             sorted(set(mask(x["cad"]) for x in v)), sorted(set(x["shown"] for x in v))[:2]))

# ================================================================ М4: хидранти
print("\n=== М4: ХИДРАНТИ — КРАТКА мярка (пълният одит е ОТДЕЛНА тема) ===")
H = json.load(open(FV + "/hydrants.json", encoding="utf-8"))
print("записи в data/hydrants.json          : %d" % len(H))
print("по origin: " + " · ".join("%s=%d" % (k, v) for k, v in
      collections.Counter(h.get("origin") for h in H).most_common()))
print("existence_status: " + " · ".join("%s=%d" % (k, v) for k, v in
      collections.Counter(str(h.get("existence_status")) for h in H).most_common()))
print("operational_status: " + " · ".join("%s=%d" % (k, v) for k, v in
      collections.Counter(str(h.get("operational_status")) for h in H).most_common()))

BB = {"minLat": 43.00, "maxLat": 43.45, "minLng": 27.60, "maxLng": 28.15}  # COORD_BBOX от index.html
def valid(h):
    c = h.get("coords")
    return isinstance(c, list) and len(c) == 2 and all(isinstance(v, (int, float)) for v in c)
nocoord = [h for h in H if not valid(h)]
inside  = [h for h in H if valid(h) and BB["minLat"] <= h["coords"][1] <= BB["maxLat"]
           and BB["minLng"] <= h["coords"][0] <= BB["maxLng"]]
outside = [h for h in H if valid(h) and h not in inside]
print("без валидна координата               : %d" % len(nocoord))
print("извън кутията COORD_BBOX             : %d" % len(outside))
for h in outside[:6]:
    print("   %s %s origin=%s" % (h["id"], h["coords"], h.get("origin")))

cc = collections.Counter(tuple(h["coords"]) for h in H if valid(h))
exact = {k: v for k, v in cc.items() if v > 1}
print("ИДЕНТИЧНИ координати                 : %d групи · %d записа" % (len(exact), sum(exact.values())))

CELLH = 0.00015
gh = collections.defaultdict(list)
for i, h in enumerate(H):
    if not valid(h):
        continue
    x, y = h["coords"]
    gh[(int(y/CELLH), int(x/CELLH))].append(i)
pairs3, pairs10 = [], []
seen = set()
for (gi, gj), idxs in gh.items():
    cand = []
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            cand += gh.get((gi+di, gj+dj), [])
    for a in idxs:
        for b in cand:
            if b <= a or (a, b) in seen:
                continue
            seen.add((a, b))
            x1, y1 = H[a]["coords"]
            x2, y2 = H[b]["coords"]
            dd = hav(y1, x1, y2, x2)
            if dd <= 10.0:
                rec = {"a": H[a]["id"], "b": H[b]["id"], "m": round(dd, 2),
                       "oa": H[a].get("origin"), "ob": H[b].get("origin"),
                       "coords_a": H[a]["coords"], "coords_b": H[b]["coords"]}
                pairs10.append(rec)
                if dd <= 3.0:
                    pairs3.append(rec)
print("двойки на <= 3 m                     : %d" % len(pairs3))
print("двойки на <= 10 m                    : %d" % len(pairs10))
def by_origin(pairs):
    return collections.Counter(tuple(sorted((p["oa"], p["ob"]))) for p in pairs).most_common(12)
print("  <=3 m по двойка origin : " + " · ".join("%s+%s=%d" % (a, b, v) for (a, b), v in by_origin(pairs3)))
print("  <=10 m по двойка origin: " + " · ".join("%s+%s=%d" % (a, b, v) for (a, b), v in by_origin(pairs10)))
ids = collections.Counter(h.get("id") for h in H)
leg = collections.Counter(x for h in H for x in (h.get("legacy_ids") or []))
print("повторени id                         : %d" % sum(1 for v in ids.values() if v > 1))
print("legacy_id, срещан >1 път             : %d" % sum(1 for v in leg.values() if v > 1))
print("\n-- 6 примера за двойки на <= 3 m --")
for p in sorted(pairs3, key=lambda p: p["m"])[:6]:
    print("   %s (%s)  <->  %s (%s)  = %s m" % (p["a"], p["oa"], p["b"], p["ob"], p["m"]))

# ================================================================ запис
head = subprocess.run(["git", "-C", "C:/git/Fire_Varna", "rev-parse", "--short", "HEAD"],
                      capture_output=True, text=True).stdout.strip()
json.dump({
    "head_fire_varna": head,
    "sources": {"geocoder_entries": len(gent), "section_units": len(SU),
                "entrance_index_docs": EIX["documentCount"],
                "strategic_intel_date": SI["source_data_date"],
                "delivery_entries": len(dent), "address_rows": len(arows)},
    "bridge": {"geocoder_en_rows": len(gEn), "delivery_en_rows": len(dEn),
               "pin_mismatch": bad_pin, "en_mismatch": bad_en, "one_to_one": bridge_ok},
    "a_section_units": {
        "entrance_records_total": au_null + len(au), "en_null": au_null, "labelled": len(au),
        "authority_keys": len(a_keys), "delivery_keys": len(d_keys), "in_both": len(both),
        "authority_only": sorted(list(a_keys - d_keys))[:200],
        "delivery_only": sorted(list(d_keys - a_keys))[:200],
        "coverage_authority_pct": round(cov_a, 3), "coverage_delivery_pct": round(cov_d, 3),
        "coord_delta_max_m": round(coord_d[-1], 3) if coord_d else None},
    "b_entrance_index_5314": {
        "total": tot5, "key_match": key_hit, "key_match_pct": round(100.0*key_hit/tot5, 2),
        "cad_present_letter_missing": cad_only, "cad_absent": no_cad,
        "distance_buckets": dict(buckets), "soft_match": soft,
        "soft_match_pct": round(100.0*soft/tot5, 2),
        "critic_claim": "4289/5314 = 80.7 % — мярка без кадастрален ключ (само буква + <=25 m)",
        "reason_profile": dict(prof), "residential_behind_unmatched": res_lost,
        "unmatched_rows": unmatched_rows},
    "c_duplicates_summary": {
        "dup_cad_en_groups": len(dup_key), "dup_g_en_groups": len(dup_g),
        "identical_coord_groups": len(coord_dup),
        "identical_coord_rows": sum(len(v) for v in coord_dup.values()),
        "same_shown_text_groups": len(txt_multi),
        "same_shown_text_diff_building_groups": len(txt_diffg),
        "same_shown_text_diff_building_rows": sum(len(v) for v in txt_diffg.values()),
        "spread_buckets": dict(spread)},
}, open(OUT + "/entrances_join.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

json.dump({
    "dup_cad_en": [{"cad": k[0], "en": k[1],
                    "rows": [{"lat": x["lat"], "lng": x["lng"], "en_raw": x["en_raw"],
                              "g": x["g"], "shown": x["shown"]} for x in v]}
                   for k, v in dup_key.items()],
    "dup_g_en": [{"g": k[0], "en": k[1], "n": len(v),
                  "cads": [x["cad"] for x in v],
                  "pins": [[x["lat"], x["lng"]] for x in v],
                  "shown": sorted(set(x["shown"] for x in v))}
                 for k, v in sorted(dup_g.items(), key=lambda kv: -len(kv[1]))],
    "identical_coords": [{"pin": list(k), "n": len(v), "en": [x["en_raw"] for x in v],
                          "cads": sorted(set(x["cad"] for x in v)),
                          "shown": sorted(set(x["shown"] for x in v))}
                         for k, v in sorted(coord_dup.items(), key=lambda kv: -len(kv[1]))],
    "same_shown_text_diff_building": sorted(txt_rows, key=lambda r: -r["max_m"]),
}, open(OUT + "/entrance_duplicates.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

json.dump({
    "count": len(H),
    "by_origin": dict(collections.Counter(h.get("origin") for h in H)),
    "existence_status": dict(collections.Counter(str(h.get("existence_status")) for h in H)),
    "operational_status": dict(collections.Counter(str(h.get("operational_status")) for h in H)),
    "invalid_coords": len(nocoord),
    "outside_bbox": [{"id": h["id"], "coords": h["coords"], "origin": h.get("origin")} for h in outside],
    "identical_coord_groups": len(exact), "identical_coord_rows": sum(exact.values()),
    "pairs_le_3m": len(pairs3), "pairs_le_10m": len(pairs10),
    "pairs_3m_by_origin": {"%s+%s" % (a, b): v for (a, b), v in by_origin(pairs3)},
    "pairs_10m_by_origin": {"%s+%s" % (a, b): v for (a, b), v in by_origin(pairs10)},
    "duplicate_ids": sum(1 for v in ids.values() if v > 1),
    "legacy_id_reused": sum(1 for v in leg.values() if v > 1),
    "pairs_3m": sorted(pairs3, key=lambda p: p["m"]),
}, open(OUT + "/hydrants_quick.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("\nзаписани: entrances_join.json · entrance_duplicates.json · hydrants_quick.json")
print("HEAD Fire_Varna: %s" % head)
