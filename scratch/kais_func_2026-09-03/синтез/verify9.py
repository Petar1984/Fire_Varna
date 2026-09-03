# -*- coding: utf-8 -*-
"""V13-V14: independent point-in-polygon over all 361 delivered records, and the
uncovered-site count for the three institutional classes."""
import json, sys, io, math
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
G='C:/git/'
info=json.load(open(G+'varna_3d/web/varna_buildings_info.json',encoding='utf-8'))
ci={c:i for i,c in enumerate(info['columns'])}; ROWS=info['rows']; FD=info['dict']['func']
idx_of={n:i for i,n in enumerate(FD)}
gj=json.load(open(G+'varna_3d/web/varna_buildings_3d.geojson',encoding='utf-8'))
from shapely.geometry import shape, Point
from shapely.strtree import STRtree
from shapely.ops import transform
LAT0=43.22; MY=111320.0; MX=111320.0*math.cos(math.radians(LAT0))
pr=lambda g: transform(lambda x,y:((x-27.92)*MX,(y-LAT0)*MY), g)
geoms=[None]*len(ROWS)
for f in gj['features']: geoms[f['properties']['i']]=shape(f['geometry'])
tree=STRtree(geoms)
places=json.load(open(G+'Fire_Varna/data/places.json',encoding='utf-8'))
hotels=json.load(open(G+'Fire_Varna/data/hotels.json',encoding='utf-8'))
pl=places['places'] if isinstance(places,dict) else places
ho=hotels['hotels'] if isinstance(hotels,dict) else hotels
recs=[('places',p) for p in pl]+[('hotels',h) for h in ho]
inside=0; d10=0; d30=0; d60=0; over60=0; far=[]
for src,r in recs:
    lat=r.get('lat'); lon=r.get('lon'); pt=Point(lon,lat)
    cand=tree.query(pt.buffer(0.0012))
    best=1e9; hit=False
    ppt=Point((lon-27.92)*MX,(lat-LAT0)*MY)
    for j in cand:
        g=geoms[j]
        if g.covers(pt): hit=True; best=0.0; break
        d=pr(g).distance(ppt)
        if d<best: best=d
    if hit: inside+=1
    elif best<=10: d10+=1
    elif best<=30: d30+=1
    elif best<=60: d60+=1
    else: over60+=1; far.append((round(best,1), r.get('name')))
print('V13 · собствен PiP над 361 доставени записа')
print('  вътре %d | ≤10 m %d | ≤30 m %d | ≤60 m %d | >60 m %d' % (inside,d10,d30,d60,over60))
print('  кумулативно: вътре %d · ≤10 %d · ≤30 %d · ≤60 %d' % (inside,inside+d10,inside+d10+d30,inside+d10+d30+d60))
print('  над 60 m:', far)

print()
print('V14 · непокрити площадки (тела ≤40 m = площадка; доставено от класа ≤60 m)')
KIND={'Сграда за детско заведение':{'детска градина'},
      'Сграда за образование':{'училище','университет'},
      'Здравно заведение':{'болница','ДКЦ','хоспис'}}
for fn,kinds in KIND.items():
    ids=[i for i,r in enumerate(ROWS) if r[ci['func']]==idx_of[fn]]
    P={i:pr(geoms[i]) for i in ids}
    objs=[P[i] for i in ids]; t2=STRtree(objs)
    par={i:i for i in ids}
    def fi(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for k,i in enumerate(ids):
        for j in t2.query(objs[k].buffer(40.0)):
            if ids[j]==i: continue
            if objs[k].distance(objs[j])<=40.0:
                a,b=fi(i),fi(ids[j])
                if a!=b: par[a]=b
    grp=Counter(fi(i) for i in ids)
    pts=[Point((p['lon']-27.92)*MX,(p['lat']-LAT0)*MY) for p in pl if p.get('kind') in kinds]
    unc=0; unc30=0
    for root in grp:
        members=[i for i in ids if fi(i)==root]
        gg=[P[i] for i in members]
        ok30=any(min(g.distance(q) for g in gg)<=30.0 for q in pts)
        ok=any(min(g.distance(q) for g in gg)<=60.0 for q in pts)
        if not ok30: unc30+=1
        if not ok: unc+=1
    print('  %-28s тела %4d | площадки %3d | покрити при ≤60 m %3d | покрити при ≤30 m %3d'
          % (fn,len(ids),len(grp),len(grp)-unc,len(grp)-unc30))
