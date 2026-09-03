# -*- coding: utf-8 -*-
import sys, io, json, collections, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
d=json.load(open("C:/git/Varna_buildings/output/geocoder_index.json",encoding='utf-8'))
ent=[e for e in d['entries'] if e.get('kind')=='mf' and e.get('en') is not None]
print("авторитет: входови записа =",len(ent))
def dm(a,b):
    R=6371000.0; p1,p2=math.radians(a[0]),math.radians(b[0])
    h=math.sin((p2-p1)/2)**2+math.cos(p1)*math.cos(p2)*math.sin(math.radians(b[1]-a[1])/2)**2
    return 2*R*math.asin(math.sqrt(h))
# ИСТИНСКИ дублиран вход = същата кадастрална СЕКЦИЯ + същата буква, два записа
g=collections.defaultdict(list)
for e in ent: g[(e.get('section_cadnum'), str(e.get('en')))].append(e)
dups={k:v for k,v in g.items() if len(v)>1}
print("ИСТИНСКИ дублети (същ section_cadnum + същ en) : групи =",len(dups)," записи =",sum(len(v) for v in dups.values()))
for k,v in list(dups.items())[:10]:
    pts=[tuple(x['pin']) for x in v]
    mx=max(dm(a,b) for i,a in enumerate(pts) for b in pts[i+1:])
    print(f"   {k}  n={len(v)}  разделение={mx:.1f} m")
# същият cadnum (сграда) + буква
g2=collections.defaultdict(list)
for e in ent: g2[(e.get('cadnum'), str(e.get('en')))].append(e)
d2={k:v for k,v in g2.items() if len(v)>1}
print("същ cadnum + същ en : групи =",len(d2)," записи =",sum(len(v) for v in d2.values()))
# същият complex_id + буква (=> едно g в доставката => СЛИВАТ СЕ)
g3=collections.defaultdict(list)
for e in ent: g3[(e.get('complex_id'), str(e.get('en')))].append(e)
d3={k:v for k,v in g3.items() if len(v)>1}
print("същ complex_id + същ en (сливат се в 1 ред): групи =",len(d3)," записи =",sum(len(v) for v in d3.values()))
diffcad=sum(1 for k,v in d3.items() if len({x.get('cadnum') for x in v})>1)
print("   от тях с РАЗЛИЧЕН cadnum (различни сгради, скрити зад 1 ред) =",diffcad)
