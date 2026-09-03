# -*- coding: utf-8 -*-
"""Named examples of the free sites."""
import sys, json, collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
from shapely.ops import unary_union
info,cols=load_info(); polys=load_geoms(); rows=info['rows']
d7=json.load(open('_step7.json',encoding='utf-8'))
from shapely.geometry import Point
from shapely.strtree import STRtree
dl=load_delivered(); pts=[Point(*to_m(r['lon'],r['lat'])) for r in dl]
ptree=STRtree(pts)
MATCH={'Сграда за детско заведение':{'детска градина'},
 'Сграда за образование':{'училище','университет'},
 'Здравно заведение':{'болница','ДКЦ','хоспис'},
 'Хотел':{'Хотел','Семеен хотел','апарт-хотел','хотел · без категоризация'},
 'Апартаментен хотел':{'Хотел','Семеен хотел','апарт-хотел','хотел · без категоризация'}}
for fname,kinds in MATCH.items():
    e=d7[fname]; free=[]
    for c in e['cl']:
        g=unary_union([polys[i] for i in c])
        hit=any(pts[int(j)].distance(g)<=60.0 and dl[int(j)]['kind'] in kinds for j in ptree.query(g.buffer(60.0)))
        if not hit:
            area=sum(rows[i][cols['area_m2']] for i in c)
            free.append((area,c,g))
    free.sort(reverse=True,key=lambda x:x[0])
    print('=== %s: %d непокрити площадки (≤60 m) — 8-те най-големи' % (fname,len(free)))
    for area,c,g in free[:8]:
        i=c[0]; r=rows[i]
        cen=g.centroid
        lat=LAT0+cen.y/MPD; lon=LON0+cen.x/KX
        print('   %8.0f m2 · %2d тела · %-16s %-40s %.5f,%.5f' % (area,len(c),
             (field(info,cols,r,'reg') or '')[6:20], ((field(info,cols,r,'addr') or field(info,cols,r,'quar') or '')[:40]), lat,lon))
    print()
