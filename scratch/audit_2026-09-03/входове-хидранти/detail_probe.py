# -*- coding: utf-8 -*-
"""Допълнителни мерки + примери към measure_entrances.py. READ-ONLY."""
import json, sys, math, re, collections, os
sys.stdout.reconfigure(encoding='utf-8')
OUT = os.path.dirname(os.path.abspath(__file__))
VB  = r"C:/git/Varna_buildings/output"
FV  = r"C:/git/Fire_Varna/data"

J   = json.load(open(OUT + "/entrances_join.json", encoding="utf-8"))
DUP = json.load(open(OUT + "/entrance_duplicates.json", encoding="utf-8"))
SU  = json.load(open(VB + "/section_units.json", encoding="utf-8"))
H   = json.load(open(FV + "/hydrants.json", encoding="utf-8"))

def mask(c):
    p = str(c).split(".")
    return ".".join([p[0]] + [(s if i >= 3 else "xxxx") for i, s in enumerate(p[1:], 1)])

R = 6371000.0
def hav(la1, ln1, la2, ln2):
    p = math.pi/180.0
    z = math.sin((la2-la1)*p/2)**2 + math.cos(la1*p)*math.cos(la2*p)*math.sin((ln2-ln1)*p/2)**2
    return 2*R*math.asin(math.sqrt(z))

print("=== П1: входовите записи БЕЗ буква в section_units (en=null) ===")
nn = [ (u, e) for u in SU for e in (u.get("entrances") or []) if e.get("en") is None ]
print("записи с en=null                     : %d" % len(nn))
print("апартаменти зад тях (n_apt)          : %d"
      % sum((e.get("n_apt") or 0) for _, e in nn))
print("обекти зад тях (object_count)        : %d"
      % sum((e.get("object_count") or 0) for _, e in nn))
secs_null = set(u["section_cadnum"] for u, _ in nn)
secs_lab  = set(u["section_cadnum"] for u in SU for e in (u.get("entrances") or []) if e.get("en") is not None)
print("секции, засегнати от en=null         : %d" % len(secs_null))
print("  · от тях БЕЗ нито един етикетиран вход: %d  <- сградата няма НИТО един търсим вход"
      % len(secs_null - secs_lab))
print("  · смесени (има и етикетирани)      : %d" % len(secs_null & secs_lab))
mixed = [(u, e) for u, e in nn if u["section_cadnum"] in secs_lab]
print("записи en=null в СМЕСЕНИ секции      : %d" % len(mixed))
bt = collections.Counter(u.get("building_type") for u, _ in nn)
print("типове сгради: " + " · ".join("%s=%d" % (k, v) for k, v in bt.most_common(5)))
print("-- 6 примера за секция изцяло без етикетиран вход (най-много апартаменти) --")
per = collections.defaultdict(lambda: [0, None])
for u, e in nn:
    if u["section_cadnum"] in secs_lab:
        continue
    per[u["section_cadnum"]][0] += (e.get("n_apt") or 0)
    per[u["section_cadnum"]][1] = u
for cad, (apt, u) in sorted(per.items(), key=lambda kv: -kv[1][0])[:6]:
    print("   %s  апарт.=%d  вх.записи=%d  · %s · %s · pin=%s,%s"
          % (mask(cad), apt, len([1 for uu, ee in nn if uu["section_cadnum"] == cad]),
             u.get("label"), u.get("building_type"),
             u["section_pin"]["lat"], u["section_pin"]["lng"]))

print("\n=== П2: 192-те сгради от стария индекс, които ги няма като секция (15.08) ===")
un = J["b_entrance_index_5314"]["unmatched_rows"]
no_sec = [r for r in un if not r["cad_in_section_units"]]
print("документи                            : %d" % len(no_sec))
print("уникални сгради                      : %d" % len(set(r["cad"] for r in no_sec)))
print("от тях кадастр.№ ГО ИМА в геокодера (като адрес/сграда): %d"
      % sum(1 for r in no_sec if r["cad_in_geocoder"]))
print("жилища зад тях                       : %d" % sum(r["residential"] for r in no_sec))
reg = collections.Counter(r["cad"].split(".")[1] for r in no_sec)
print("по кадастрален район (топ 8): " + " · ".join("р-н %s=%d" % (k, v) for k, v in reg.most_common(8)))

print("\n=== П3: 110-те „чист етикет, но буквата липсва“ ===")
clean = [r for r in un if r["cad_in_section_units"] and r["cad_in_delivery"] and not r["composite"]]
print("документи                            : %d" % len(clean))
print("жилища зад тях                       : %d" % sum(r["residential"] for r in clean))
print("-- 6 примера (какви букви ИМА доставката за същата сграда) --")
for r in sorted(clean, key=lambda r: -r["units"])[:6]:
    print("   %s  липсва вх.„%s\"  обекти=%d жил.=%d · доставени за сградата: %s · %s"
          % (mask(r["cad"]), r["entrance"], r["units"], r["residential"],
             r["section_entrances_in_delivery"], r["section_label"]))

print("\n=== П4: 60-те съставни/мръсни етикета ===")
comp = [r for r in un if r["composite"]]
print("документи                            : %d" % len(comp))
print("проби: " + " · ".join(sorted(set('„%s"' % r["entrance"] for r in comp))[:22]))
print("-- 6 примера --")
for r in sorted(comp, key=lambda r: -r["units"])[:6]:
    print("   %s  вх.„%s\"  обекти=%d · доставени за сградата: %s · %s"
          % (mask(r["cad"]), r["entrance"], r["units"],
             r["section_entrances_in_delivery"], r["section_label"]))

print("\n=== П5: дублети (публична група g, вход) — 40 групи / 82 записа ===")
dg = DUP["dup_g_en"]
print("групи                                : %d · записи: %d" % (len(dg), sum(x["n"] for x in dg)))
sp = collections.Counter()
rows = []
for x in dg:
    mx = 0.0
    P = x["pins"]
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            mx = max(mx, hav(P[i][0], P[i][1], P[j][0], P[j][1]))
    b = ("<=5 m" if mx <= 5 else "5-25 m" if mx <= 25 else "25-100 m" if mx <= 100 else ">100 m")
    sp[b] += 1
    rows.append((mx, x))
for k in ["<=5 m", "5-25 m", "25-100 m", ">100 m"]:
    print("   %-10s %3d групи" % (k, sp.get(k, 0)))
print("-- 6 примера (една и съща публична група + една и съща буква, различни секции) --")
for mx, x in sorted(rows, key=lambda t: -t[0])[:6]:
    print("   g=%s вх.„%s\" x%d  раздалечени %0.1f m · секции: %s · показва: %s"
          % (x["g"], x["en"], x["n"], mx, [mask(c) for c in x["cads"]], x["shown"][:2]))

print("\n=== П6: входове с ИДЕНТИЧНА координата (11 групи / 22 записа) ===")
for k in DUP["identical_coords"]:
    print("   %s  x%d  вх.%s  сграда %s  → %s"
          % (k["pin"], k["n"], k["en"], [mask(c) for c in k["cads"]], k["shown"]))

print("\n=== П7: ХИДРАНТИ — рамката на „извън кутията“ ===")
lats = [h["coords"][1] for h in H]
lngs = [h["coords"][0] for h in H]
print("реална кутия на слоя: lat %.5f..%.5f · lng %.5f..%.5f" % (min(lats), max(lats), min(lngs), max(lngs)))
BB = {"minLat": 43.00, "maxLat": 43.45, "minLng": 27.60, "maxLng": 28.15}
out = [h for h in H if not (BB["minLat"] <= h["coords"][1] <= BB["maxLat"]
                            and BB["minLng"] <= h["coords"][0] <= BB["maxLng"])]
print("извън COORD_BBOX (index.html)        : %d от %d = %.1f %%" % (len(out), len(H), 100.0*len(out)/len(H)))
print("  по origin: " + " · ".join("%s=%d" % (k, v) for k, v in
      collections.Counter(h.get("origin") for h in out).most_common()))
print("  по region: " + " · ".join("%s=%d" % (k, v) for k, v in
      collections.Counter(h.get("region") for h in out).most_common(8)))
# тесен градски прозорец
CB = {"minLat": 43.15, "maxLat": 43.30, "minLng": 27.78, "maxLng": 28.06}
city = [h for h in H if CB["minLat"] <= h["coords"][1] <= CB["maxLat"]
        and CB["minLng"] <= h["coords"][0] <= CB["maxLng"]]
print("в тесния градски прозорец (43.15-43.30 / 27.78-28.06): %d" % len(city))
print("извън него (областта ОДМВР Варна)    : %d" % (len(H) - len(city)))

print("\n=== П8: ХИДРАНТИ — идентични координати (3 групи / 27 записа) ===")
cc = collections.Counter(tuple(h["coords"]) for h in H)
for k, v in sorted(cc.items(), key=lambda kv: -kv[1])[:6]:
    if v < 2:
        continue
    grp = [h for h in H if tuple(h["coords"]) == k]
    print("   %s  x%d  origin=%s  id-та: %s"
          % (list(k), v, sorted(set(g.get("origin") for g in grp)),
             [g["id"] for g in grp][:6]))

print("\n=== П9: ХИДРАНТИ — двойките <=10 m по origin, без national+national ===")
HQ = json.load(open(OUT + "/hydrants_quick.json", encoding="utf-8"))
mixed_pairs = [p for p in HQ["pairs_3m"] if p["oa"] != p["ob"]]
print("двойки <=3 m с РАЗЛИЧЕН origin       : %d" % len(mixed_pairs))
print("двойки <=10 m общо                   : %d" % HQ["pairs_le_10m"])
print("  по двойка origin: " + " · ".join("%s=%d" % (k, v) for k, v in HQ["pairs_10m_by_origin"].items()))
print("-- 6 примера за двойки <=3 m (не-нулево разстояние) --")
for p in sorted([q for q in HQ["pairs_3m"] if q["m"] > 0.0], key=lambda q: q["m"])[:6]:
    print("   %s (%s) %s  <->  %s (%s) %s  = %s m"
          % (p["a"], p["oa"], p["coords_a"], p["b"], p["ob"], p["coords_b"], p["m"]))
