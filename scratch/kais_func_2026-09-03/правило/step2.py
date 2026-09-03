# -*- coding: utf-8 -*-
import sys, json
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
from shapely.geometry import Point
from shapely.strtree import STRtree
info, cols = load_info()
polys = load_geoms()
tree = STRtree(polys)
rows = info['rows']

CP = [('а','ул. Шести септември 6',43.24473,27.85411),
      ('б','ж.к. Владислав Варненчик',43.24456,27.84592),
      ('в','ж.к. „Владислав Валненчик“ (typo)',43.24946,27.84414),
      ('г','ул. Ниш 29',43.24709,27.85397)]
for tag,label,lat,lon in CP:
    pt = Point(*to_m(lon,lat))
    cand = tree.query(pt.buffer(1.0))
    hit=[]
    for i in cand:
        i=int(i)
        if polys[i].contains(pt) or polys[i].distance(pt)<0.5:
            hit.append(i)
    print('=== (%s) %s  %.5f %.5f' % (tag,label,lat,lon))
    if not hit:
        # nearest
        near = tree.query_nearest(pt)
        i=int(near if not hasattr(near,'__len__') else near[0])
        hit=[i]; print('  (не е вътре; най-близкото)')
    for i in hit:
        r=rows[i]
        print('   i=%d func=%s prop=%s floors=%s area=%s reg=%s quar=%s' % (
            i, field(info,cols,r,'func'), field(info,cols,r,'prop'), r[cols['floors']],
            r[cols['area_m2']], field(info,cols,r,'reg'), field(info,cols,r,'quar')))
        print('      addr=%r street=%r num=%r' % (field(info,cols,r,'addr'),
              field(info,cols,r,'street'), field(info,cols,r,'num')))
