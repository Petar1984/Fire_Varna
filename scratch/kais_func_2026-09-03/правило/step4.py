# -*- coding: utf-8 -*-
"""The hole: KAIS bodies with a target function and no delivered record on/near them."""
import sys, json, collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
from shapely.geometry import Point
from shapely.strtree import STRtree
info, cols = load_info(); polys = load_geoms(); rows = info['rows']
dl = load_delivered()
pts = [Point(*to_m(r['lon'], r['lat'])) for r in dl]
ptree = STRtree(pts)

TARGET = {'Сграда за детско заведение':'детска градина',
          'Сграда за образование':'училище/университет',
          'Здравно заведение':'болница/ДКЦ/хоспис',
          'Хотел':'хотел','Апартаментен хотел':'хотел',
          'Курортна, туристическа сграда':'хотел',
          'Заведение за социални грижи':'(соц. грижи — извън мандата?)',
          'Общежитие':'(общежитие — извън мандата?)'}
fi=cols['func']; dictf=info['dict']['func']
for fname,label in TARGET.items():
    k=dictf.index(fname)
    idxs=[i for i,r in enumerate(rows) if r[fi]==k]
    covered=0; free=[]
    for i in idxs:
        p=polys[i]
        near=[j for j in ptree.query(p.buffer(30.0)) if pts[int(j)].distance(p)<=30.0]
        if near: covered+=1
        else: free.append(i)
    print('%-34s общо %5d · с доставено място ≤30 m %4d · БЕЗ %5d   (%s)' % (fname,len(idxs),covered,len(free),label))
    json.dump(free, open('_free_%d.json'%k,'w'))
