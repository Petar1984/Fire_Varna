# -*- coding: utf-8 -*-
import sys, json, math, collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
from shapely.geometry import Point
from shapely.strtree import STRtree
info,cols=load_info(); polys=load_geoms(); rows=info['rows']
ar=json.load(open(G+'Fire_Varna/data/address_rows.json',encoding='utf-8'))['rows']
# has ул ниш 29?
print('ул ниш 29 в адресната машина:', any(r[0]=='ул ниш 29' for r in ar),
      '| ключове ниш N:', sorted({r[0] for r in ar if r[0].startswith('ул ниш ')}))
print()
CL={ 'а · ул. Шести септември 6':[18116,18117],
     'б · ж.к. Вл. Варненчик 203 m2':[16753,16754,16755,16756,16757],
     'в · ж.к. Вл. Валненчик 190 m2':[16617,16618,16619],
     'г · ул. Ниш 29':[18347],
     'Георги Минков 2 (двор)':[18334,18335,18336,18337,18338,18339,18340,18341],
     'ЦДГ 10 Приказка':[18481,18482] }
KEYS=['кв владиславово бл 402','бул владислав варненчик бл 309','кв владиславово бл 21',
      'кв владиславово бл 20','ул шести септември 6','ул ниш 19','кв владиславово бл 208',
      'бул владислав варненчик бл 208']
for label,idxs in CL.items():
    print('=== %s  (тела %s)' % (label, idxs))
    from shapely.ops import unary_union
    geom=unary_union([polys[i] for i in idxs])
    for k in KEYS:
        rr=[r for r in ar if r[0]==k]
        if not rr: continue
        ds=sorted(geom.distance(Point(*to_m(r[2],r[1]))) for r in rr)
        print('     %-34s n=%2d  min %6.1f m  median %6.1f m' % (k,len(rr),ds[0],ds[len(ds)//2]))
