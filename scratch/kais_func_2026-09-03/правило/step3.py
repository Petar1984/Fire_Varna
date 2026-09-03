# -*- coding: utf-8 -*-
"""Placement: PiP of the 361 delivered records against the 80 497 polygons."""
import sys, json, collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
from shapely.geometry import Point
from shapely.strtree import STRtree

info, cols = load_info()
polys = load_geoms()
tree = STRtree(polys)
rows = info['rows']
dl = load_delivered()

res=[]
for r in dl:
    pt = Point(*to_m(r['lon'], r['lat']))
    inside=[]
    for i in tree.query(pt):
        i=int(i)
        if polys[i].covers(pt): inside.append(i)
    if inside:
        # tie-break: smallest area (the most specific body)
        inside.sort(key=lambda i:(polys[i].area,i))
        b=inside[0]; d=0.0; nin=len(inside)
    else:
        j=int(tree.query_nearest(pt))
        b=j; d=polys[j].distance(pt); nin=0
    br=rows[b]
    res.append(dict(r, i=b, dist_m=round(d,2), n_inside=nin,
        func=field(info,cols,br,'func'), prop=field(info,cols,br,'prop'),
        area=br[cols['area_m2']], floors=br[cols['floors']],
        reg=field(info,cols,br,'reg'), quar=field(info,cols,br,'quar'),
        addr=field(info,cols,br,'addr'), street=field(info,cols,br,'street'),
        num=field(info,cols,br,'num')))
json.dump(res, open('_step3.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('inside', sum(1 for x in res if x['dist_m']==0.0), '/', len(res))
print()
for kind in ['детска градина','училище','университет','болница','ДКЦ','хоспис']:
    sub=[x for x in res if x['kind']==kind]
    c=collections.Counter(x['func'] for x in sub if x['dist_m']==0.0)
    print('== %s (%d) вътре=%d' % (kind,len(sub),sum(1 for x in sub if x['dist_m']==0)))
    for f,n in c.most_common(): print('     %3d %s' % (n,f))
    out=[x for x in sub if x['dist_m']>0]
    print('     вън:', ', '.join('%s %.1fm→%s'%(x['name'][:28],x['dist_m'],x['func']) for x in out[:8]))
print()
hk=[x for x in res if x['file']=='hotels.json']
print('== хотели (%d) вътре=%d' % (len(hk),sum(1 for x in hk if x['dist_m']==0)))
c=collections.Counter(x['func'] for x in hk if x['dist_m']==0.0)
for f,n in c.most_common(): print('     %3d %s' % (n,f))
print('     вън:', sum(1 for x in hk if x['dist_m']>0))
