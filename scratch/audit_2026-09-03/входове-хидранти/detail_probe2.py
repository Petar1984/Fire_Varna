# -*- coding: utf-8 -*-
"""Втора допълнителна мярка: същността на en=null + хидрантните двойки в (0,10] m. READ-ONLY."""
import json, sys, math, collections, os
sys.stdout.reconfigure(encoding='utf-8')
OUT = os.path.dirname(os.path.abspath(__file__))
SU = json.load(open(r"C:/git/Varna_buildings/output/section_units.json", encoding="utf-8"))
H  = json.load(open(r"C:/git/Fire_Varna/data/hydrants.json", encoding="utf-8"))

def mask(c):
    p = str(c).split(".")
    return ".".join([p[0]] + [(s if i >= 3 else "xxxx") for i, s in enumerate(p[1:], 1)])

print("=== Q1: какво Е записът с en=null ===")
ex = [e for u in SU for e in (u.get("entrances") or []) if e.get("en") is None]
print("брой                                 : %d" % len(ex))
print("полета: " + str(collections.Counter(k for e in ex for k in e).most_common()))
print("проба : " + json.dumps(ex[0], ensure_ascii=False))
print("източник (source): " + " · ".join("%s=%d" % (k, v) for k, v in
      collections.Counter(e.get("source") for e in ex).most_common()))
print("с координата lat/lng                 : %d" % sum(1 for e in ex if e.get("lat") is not None))

print("\n=== Q2: истинската дупка — секции с апартаменти, но БЕЗ търсим вход ===")
lab = set(u["section_cadnum"] for u in SU
          for e in (u.get("entrances") or []) if e.get("en") is not None)
gap = [u for u in SU if u["section_cadnum"] not in lab]
print("секции общо                          : %d" % len(SU))
print("секции с поне един етикетиран вход   : %d  (%.1f %%)" % (len(lab), 100.0*len(lab)/len(SU)))
print("секции БЕЗ нито един етикетиран вход : %d  (%.1f %%)" % (len(gap), 100.0*len(gap)/len(SU)))
gap_apt = [u for u in gap if (u.get("apartment_count") or 0) > 0]
print("  · от тях с apartment_count > 0     : %d" % len(gap_apt))
print("  · апартаменти зад тях              : %d" % sum(u.get("apartment_count") or 0 for u in gap_apt))
print("  · апартаменти в секции С вход      : %d"
      % sum(u.get("apartment_count") or 0 for u in SU if u["section_cadnum"] in lab))
print("  · типове: " + " · ".join("%s=%d" % (k, v) for k, v in
      collections.Counter(u.get("building_type") for u in gap_apt).most_common(5)))
print("-- 6 примера: най-много апартаменти без нито един търсим вход --")
for u in sorted(gap_apt, key=lambda u: -(u.get("apartment_count") or 0))[:6]:
    print("   %s  апарт.=%d обекти=%d ет.=%s · %s · %s · pin=%s,%s"
          % (mask(u["section_cadnum"]), u.get("apartment_count"), u.get("object_count"),
             u.get("floors_section"), u.get("label"), u.get("building_type"),
             u["section_pin"]["lat"], u["section_pin"]["lng"]))

print("\n=== Q3: хидрантни двойки в (0, 10] m ===")
HQ = json.load(open(OUT + "/hydrants_quick.json", encoding="utf-8"))
R = 6371000.0
def hav(la1, ln1, la2, ln2):
    p = math.pi/180.0
    z = math.sin((la2-la1)*p/2)**2 + math.cos(la1*p)*math.cos(la2*p)*math.sin((ln2-ln1)*p/2)**2
    return 2*R*math.asin(math.sqrt(z))
CELLH = 0.00015
gh = collections.defaultdict(list)
for i, h in enumerate(H):
    x, y = h["coords"]
    gh[(int(y/CELLH), int(x/CELLH))].append(i)
seen = set(); mid = []
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
            x1, y1 = H[a]["coords"]; x2, y2 = H[b]["coords"]
            d = hav(y1, x1, y2, x2)
            if 0.0 < d <= 10.0:
                mid.append((d, H[a], H[b]))
print("двойки с 0 < d <= 10 m               : %d" % len(mid))
print("  по двойка origin: " + " · ".join("%s+%s=%d" % (k[0], k[1], v) for k, v in
      collections.Counter(tuple(sorted((a.get("origin"), b.get("origin")))) for _, a, b in mid).most_common()))
print("-- 6 примера --")
for d, a, b in sorted(mid, key=lambda t: t[0])[:6]:
    print("   %.2f m · %s (%s) %s  <->  %s (%s) %s"
          % (d, a["id"], a.get("origin"), a["coords"], b["id"], b.get("origin"), b["coords"]))

print("\n=== Q4: хидранти — region / address / type покритие ===")
print("region: " + " · ".join("%s=%d" % (k, v) for k, v in
      collections.Counter(h.get("region") for h in H).most_common(10)))
print("type  : " + " · ".join("%s=%d" % (k, v) for k, v in
      collections.Counter(h.get("type") for h in H).most_common(10)))
print("с адрес: %d · с report_id: %d · с verifier_note: %d"
      % (sum(1 for h in H if h.get("address")), sum(1 for h in H if h.get("report_id")),
         sum(1 for h in H if h.get("verifier_note"))))
print("\n=== Q5: хидранти по груб квадрант (за да се види обхватът) ===")
b = collections.Counter()
for h in H:
    x, y = h["coords"]
    b[(round(y, 1), round(x, 1))] += 1
for k, v in b.most_common(10):
    print("   lat~%.1f lng~%.1f : %d" % (k[0], k[1], v))
