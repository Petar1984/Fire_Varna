# -*- coding: utf-8 -*-
import sys, json, collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
from shapely.geometry import Point
from shapely.ops import unary_union
from shapely.strtree import STRtree
info,cols=load_info(); polys=load_geoms(); rows=info['rows']
ar=json.load(open(G+'Fire_Varna/data/address_rows.json',encoding='utf-8'))['rows']
a=unary_union([polys[18116],polys[18117]])
# every address key within 200 m of body (a)
near=collections.defaultdict(lambda:1e9)
for k,lat,lon in ar:
    d=a.distance(Point(*to_m(lon,lat)))
    if d<200: near[k]=min(near[k],d)
print('=== адресни ключове ≤200 m от тяло (а) 6-ти септември')
for k,d in sorted(near.items(), key=lambda kv:kv[1])[:18]: print('   %6.1f m  %s'%(d,k))
print()
# делivered pins in Vladislavovo
dl=load_delivered()
for r in dl:
    if 'ладислав' in r.get('zone','') or 'ладиславово' in r.get('zone',''):
        print('   доставено: %-32s %-16s zone=%s src=%s' % (r['name'][:32],r['kind'],r['zone'],r['src'][:28]))
