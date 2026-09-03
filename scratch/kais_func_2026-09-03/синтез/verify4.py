# -*- coding: utf-8 -*-
"""V9: cross-check the centroid clustering with MY OWN centroids (shapely, projected),
   brute force, to make sure V7's STRtree run was not the odd one out."""
import json, sys, io, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
G='C:/git/'
info=json.load(open(G+'varna_3d/web/varna_buildings_info.json',encoding='utf-8'))
ci={c:i for i,c in enumerate(info['columns'])}; ROWS=info['rows']; FD=info['dict']['func']
idx_of={n:i for i,n in enumerate(FD)}
gj=json.load(open(G+'varna_3d/web/varna_buildings_3d.geojson',encoding='utf-8'))
from shapely.geometry import shape
LAT0=43.22; MY=111320.0; MX=111320.0*math.cos(math.radians(LAT0))
cent={}; poly={}
for f in gj['features']:
    i=f['properties']['i']; g=shape(f['geometry']); c=g.centroid
    cent[i]=(c.x*MX, c.y*MY)
def bf(ids, thr, pts):
    par={i:i for i in ids}
    def fi(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for a in range(len(ids)):
        ia=ids[a]; xa,ya=pts[ia]
        for b in range(a+1,len(ids)):
            ib=ids[b]; xb,yb=pts[ib]
            if abs(xa-xb)>thr or abs(ya-yb)>thr: continue
            if math.hypot(xa-xb,ya-yb)<=thr:
                ra,rb=fi(ia),fi(ib)
                if ra!=rb: par[ra]=rb
    return len(set(fi(i) for i in ids))
for n in ['Сграда за детско заведение','Сграда за образование','Здравно заведение']:
    ids=[i for i,r in enumerate(ROWS) if r[ci['func']]==idx_of[n]]
    print('%-28s тела %4d | центроид≤45m (моят проектиран центроид) %3d' % (n,len(ids),bf(ids,45.0,cent)))
