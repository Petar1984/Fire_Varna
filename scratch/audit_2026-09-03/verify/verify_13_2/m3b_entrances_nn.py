# -*- coding: utf-8 -*-
"""M3b: същото съединение, но с ТОЛЕРАНС (най-близък доставен вход със същата буква).
READ-ONLY. Изход: m3b_entrances_nn.json"""
import json, sys, math, collections
sys.stdout.reconfigure(encoding='utf-8')
AUT = json.load(open(r"C:/git/Varna_buildings/output/search_index_entrances.json", encoding='utf-8'))['storedFields']
DEL = json.load(open(r"C:/git/Fire_Varna/data/search_index.json", encoding='utf-8'))['entries']
aut = list(AUT.values())
dele = [e for e in DEL if isinstance(e, dict) and 'en' in e]

CELL = 0.0015  # ~150 m
grid = collections.defaultdict(list)
for e in dele:
    la, ln = e['pin'][0], e['pin'][1]
    grid[(int(la/CELL), int(ln/CELL))].append(e)

def hav(a,b,c,d):
    R=6371000.0; p=math.pi/180
    dla=(c-a)*p; dln=(d-b)*p
    x=math.sin(dla/2)**2+math.cos(a*p)*math.cos(c*p)*math.sin(dln/2)**2
    return 2*R*math.asin(math.sqrt(x))

buckets = collections.Counter(); dists=[]; far=[]
for a in aut:
    la, ln = float(a['lat']), float(a['lng']); L = str(a['entrance'])
    gi, gj = int(la/CELL), int(ln/CELL)
    best=None
    for di in (-1,0,1):
        for dj in (-1,0,1):
            for e in grid.get((gi+di, gj+dj), ()):
                if str(e['en']) != L: continue
                dd = hav(la, ln, e['pin'][0], e['pin'][1])
                if best is None or dd < best[0]: best=(dd,e)
    if best is None:
        buckets['няма същата буква в 150 m']+=1; far.append(a); continue
    dd=best[0]; dists.append(dd)
    if dd<=5: buckets['<=5 m']+=1
    elif dd<=25: buckets['5-25 m']+=1
    elif dd<=100: buckets['25-100 m']+=1
    else: buckets['>100 m']+=1; far.append(a)
tot=len(aut)
for k in ['<=5 m','5-25 m','25-100 m','>100 m','няма същата буква в 150 m']:
    v=buckets.get(k,0); print(f"{k:30s} {v:6d}  {100*v/tot:5.1f}%")
matched = buckets.get('<=5 m',0)+buckets.get('5-25 m',0)
print(f"\nдоказано доставени (<=25 m, същата буква): {matched} от {tot} = {100*matched/tot:.1f}%")
unmatched = tot - matched
print(f"НЕдоказани: {unmatched}  (черновата твърди 550)")
print("жилища зад НЕдоказаните (>100 m или без буква):", sum(x['residential'] for x in far))
json.dump({"authority": tot, "delivered": len(dele), "buckets": dict(buckets),
           "matched_le_25m": matched, "unmatched": unmatched,
           "far_sample": far[:40]}, open("m3b_entrances_nn.json","w",encoding='utf-8'),
          ensure_ascii=False, indent=1)
