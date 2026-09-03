# -*- coding: utf-8 -*-
"""M3: ОБОРВАНЕ на „входовият индекс няма координати".
Съединява авторитета (search_index_entrances.json.storedFields: building_cadnum+entrance+lat+lng)
с доставката (Fire_Varna/data/search_index.json: entries с 'en') ред по ред.
READ-ONLY. Изход: m3_entrances_join.json"""
import json, sys, math, collections
sys.stdout.reconfigure(encoding='utf-8')

AUT = json.load(open(r"C:/git/Varna_buildings/output/search_index_entrances.json", encoding='utf-8'))['storedFields']
DEL = json.load(open(r"C:/git/Fire_Varna/data/search_index.json", encoding='utf-8'))['entries']

aut = [dict(v) for v in AUT.values()]
dele = [e for e in DEL if isinstance(e, dict) and 'en' in e]
print("авторитет входови документа:", len(aut), "· уникални сгради:", len(set(a['building_cadnum'] for a in aut)))
print("доставени входа (entries с 'en'):", len(dele))
print("има ли lat/lng в авторитета:", all(('lat' in a and 'lng' in a) for a in aut))

# ключ по координата (5 dp ≈ 1 m) + буква
def k5(lat, lng): return (round(float(lat),5), round(float(lng),5))
dmap = collections.defaultdict(list)
for e in dele:
    dmap[(k5(e['pin'][0], e['pin'][1]), str(e['en']))].append(e)
dmap_coord = collections.defaultdict(list)
for e in dele:
    dmap_coord[k5(e['pin'][0], e['pin'][1])].append(e)

hit_ce, hit_c, miss = 0, 0, []
for a in aut:
    key = (k5(a['lat'], a['lng']), str(a['entrance']))
    if dmap.get(key): hit_ce += 1
    elif dmap_coord.get(key[0]): hit_c += 1
    else: miss.append(a)
print(f"съвпадат по координата+буква: {hit_ce}")
print(f"съвпадат по координата, но НЕ по буква: {hit_c}")
print(f"НЕ стигат до доставката (нищо на тази координата): {len(miss)}")
print(f"проверка: {hit_ce}+{hit_c}+{len(miss)} = {hit_ce+hit_c+len(miss)} (=5314?)")

# профил на липсващите
print("\n-- профил на липсващите --")
print("уникални сгради сред липсващите:", len(set(m['building_cadnum'] for m in miss)))
print("unit_count=0:", sum(1 for m in miss if m['unit_count']==0))
print("само гаражи/склад (residential=0):", sum(1 for m in miss if m['residential']==0))
print("residential>0:", sum(1 for m in miss if m['residential']>0))
print("сума жилища зад липсващите входове:", sum(m['residential'] for m in miss))
by_cad = collections.Counter(m['building_cadnum'] for m in miss)
print("топ сгради с най-много липсващи входа:", by_cad.most_common(6))
for m in sorted(miss, key=lambda x:-x['unit_count'])[:8]:
    print("  ", m['building_cadnum'], "вх."+m['entrance'], "units", m['unit_count'],
          "res", m['residential'], m['lat'], m['lng'])

json.dump({"authority_docs": len(aut), "delivered_entrances": len(dele),
           "authority_has_coords": True,
           "match_coord_and_letter": hit_ce, "match_coord_only": hit_c,
           "missing": len(miss),
           "missing_unique_buildings": len(set(m['building_cadnum'] for m in miss)),
           "missing_residential_units_total": sum(m['residential'] for m in miss),
           "missing_rows": miss},
          open("m3_entrances_join.json","w",encoding='utf-8'), ensure_ascii=False, indent=1)
