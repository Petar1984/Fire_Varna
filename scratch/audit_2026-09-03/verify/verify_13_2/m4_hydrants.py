# -*- coding: utf-8 -*-
"""M4: хидрантите — слоят, който изобщо не влезе в одита. Покритие и дублети.
READ-ONLY. Изход: m4_hydrants.json"""
import json, sys, math, collections
sys.stdout.reconfigure(encoding='utf-8')
H = json.load(open(r"C:/git/Fire_Varna/data/hydrants.json", encoding='utf-8'))
print("хидранти:", len(H))
print("полета:", collections.Counter(k for h in H for k in h.keys()).most_common())
print("origin:", collections.Counter(h.get('origin') for h in H).most_common())
# точни дублети по координата
c = collections.Counter(tuple(h['coords']) for h in H)
dup = {k:v for k,v in c.items() if v>1}
print("точни дублети по координата:", len(dup), "групи ·", sum(dup.values()), "записа")
# дублирани id / legacy_ids
ids = collections.Counter(h.get('id') for h in H)
print("повторени id:", sum(1 for v in ids.values() if v>1))
leg = collections.Counter(x for h in H for x in (h.get('legacy_ids') or []))
print("legacy_id, срещан >1 път:", sum(1 for v in leg.values() if v>1),
      "· примери:", [k for k,v in leg.most_common(5) if v>1])
# близнаци <=3 m
CELL=0.00005
g=collections.defaultdict(list)
for i,h in enumerate(H):
    x,y=h['coords']; g[(int(y/CELL),int(x/CELL))].append(i)
def hav(a,b,cc,d):
    R=6371000.0; p=math.pi/180
    dla=(cc-a)*p; dln=(d-b)*p
    z=math.sin(dla/2)**2+math.cos(a*p)*math.cos(cc*p)*math.sin(dln/2)**2
    return 2*R*math.asin(math.sqrt(z))
seen=set(); near=[]
for (gi,gj),idxs in g.items():
    cand=[]
    for di in (-1,0,1):
        for dj in (-1,0,1): cand+=g.get((gi+di,gj+dj),[])
    for a in idxs:
        for b in cand:
            if b<=a: continue
            x1,y1=H[a]['coords']; x2,y2=H[b]['coords']
            d=hav(y1,x1,y2,x2)
            if d<=3.0 and (a,b) not in seen:
                seen.add((a,b)); near.append({"a":H[a]['id'],"b":H[b]['id'],"m":round(d,2),
                                              "oa":H[a].get('origin'),"ob":H[b].get('origin')})
print("двойки хидранти на <=3 m:", len(near))
for n in near[:8]: print("  ", n)
json.dump({"count":len(H),"exact_coord_dup_groups":len(dup),
           "exact_coord_dup_rows":sum(dup.values()),
           "pairs_le_3m":len(near),"pairs":near[:200]},
          open("m4_hydrants.json","w",encoding='utf-8'), ensure_ascii=False, indent=1)
