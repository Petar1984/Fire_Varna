# -*- coding: utf-8 -*-
"""M7: ДУБЛИРАЩИТЕ СЕ СГРАДИ — слоят, който одитът изобщо не мери.
Авторитетът (ADR-038 physical_building_sidecar) казва кои кадастрални секции са ЕДНА
физическа сграда; геокодерът носи physical_building_id; доставката го ИЗПУСКА
(index.html:5255 „pbid always null -> every row passes through").
READ-ONLY. Изход: m7_pbid.json"""
import json, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
SC = json.load(open(r"C:/git/Varna_buildings/output/physical_building_sidecar.json", encoding='utf-8'))
m = SC['cadnum_to_physical_building_id']
grp = collections.Counter(m.values())
print("АВТОРИТЕТ (ADR-038):")
print("  кадастрални секции в сидекара:", len(m))
print("  физически сгради:", len(grp))
print("  секции, които трябва да се слеят (483-198):", len(m)-len(grp))
print("  stats от самия сидекар:", json.dumps(SC['stats'], ensure_ascii=False))

G = json.load(open(r"C:/git/Varna_buildings/output/geocoder_index.json", encoding='utf-8'))
ge = G['entries']
has = [e for e in ge if e.get('physical_building_id') is not None]
print("\nГЕОКОДЕР:")
print("  записи:", len(ge), "· с physical_building_id:", len(has))
print("  physical_building_reps в индекса:", len(G.get('physical_building_reps') or {}))
by = collections.Counter(e['physical_building_id'] for e in has)
print("  групи:", len(by), "· групи с >1 запис:", sum(1 for v in by.values() if v > 1))
print("  записи в групи >1:", sum(v for v in by.values() if v > 1))

D = json.load(open(r"C:/git/Fire_Varna/data/search_index.json", encoding='utf-8'))
de = D['entries']
print("\nДОСТАВКА:")
print("  записи:", len(de))
print("  с physical_building_id:", sum(1 for e in de if 'physical_building_id' in e), "(полето е отрязано)")
print("  с life_safety_rank:", sum(1 for e in de if 'life_safety_rank' in e), "(също отрязано)")
# кои записи от геокодера с pbid стигат до доставката (по координата)
dp = collections.Counter((round(e['pin'][0],5), round(e['pin'][1],5)) for e in de)
reach = sum(1 for e in has if dp.get((round(e['pin'][0],5), round(e['pin'][1],5))))
print("  от", len(has), "записа с pbid в геокодера, на същата координата в доставката има:", reach)
ex = []
for pb, n in by.most_common(8):
    rows = [e for e in has if e['physical_building_id'] == pb]
    ex.append({"pbid": pb, "n": n, "cadnums": [r.get('cadnum') for r in rows][:6],
               "pins": [r['pin'] for r in rows][:6]})
    print("   ", pb, "n=", n, [r.get('cadnum') for r in rows][:5])
json.dump({"sidecar_cadnums": len(m), "sidecar_physical_buildings": len(grp),
           "collapsible": len(m)-len(grp), "sidecar_stats": SC['stats'],
           "geocoder_with_pbid": len(has), "geocoder_pbid_groups": len(by),
           "delivery_with_pbid": 0, "delivery_reachable_rows": reach, "examples": ex},
          open("m7_pbid.json","w",encoding='utf-8'), ensure_ascii=False, indent=1)
