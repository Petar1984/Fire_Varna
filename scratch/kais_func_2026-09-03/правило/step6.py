# -*- coding: utf-8 -*-
import sys, json, collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
from shapely.geometry import Point
from shapely.strtree import STRtree
info, cols = load_info(); polys = load_geoms(); rows = info['rows']
dl = load_delivered()
pts=[Point(*to_m(r['lon'],r['lat'])) for r in dl]
ptree=STRtree(pts)
dictf=info['dict']['func']; fi=cols['func']; ri=cols['reg']
REG='район Владислав Варненчик'; rk=info['dict']['reg'].index(REG)
CP={18116:'а',16753:'б',16619:'в',18347:'г'}
for fname in ['Сграда за детско заведение','Сграда за образование','Здравно заведение']:
    k=dictf.index(fname)
    idxs=[i for i,r in enumerate(rows) if r[fi]==k and r[ri]==rk]
    print('=== %s · %s: %d тела' % (fname,REG,len(idxs)))
    cl=json.load(open('_cl_%d.json'%k))
    freeset={i for c in cl for i in c}
    for i in sorted(idxs):
        p=polys[i]
        near=sorted(((pts[int(j)].distance(p),int(j)) for j in ptree.query(p.buffer(120.0))
                     if pts[int(j)].distance(p)<=120.0))
        tag='СВОБОДНО' if i in freeset else 'покрито '
        cp=' [КТ '+CP[i]+']' if i in CP else ''
        n0 = ('%s %.1fm'%(dl[near[0][1]]['name'][:34],near[0][0])) if near else '—'
        print('  %s i=%-6d %7.1f m2 %-18s %-26s %s%s' % (tag,i,rows[i][cols['area_m2']],
              (field(info,cols,rows[i],'prop') or '')[:18],
              (field(info,cols,rows[i],'addr') or field(info,cols,rows[i],'quar') or '')[:26], n0, cp))
