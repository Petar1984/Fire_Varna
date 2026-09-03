# -*- coding: utf-8 -*-
"""Свободните КАИС площадки срещу ЛИПСВАЩИТЕ регистрови редове (предишен одит)."""
import sys, json
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
from shapely.geometry import Point
from shapely.ops import unary_union
from shapely.strtree import STRtree
info,cols=load_info(); polys=load_geoms()
doc=json.load(open('placement.json',encoding='utf-8'))
mis=json.load(open(G+'Fire_Varna/scratch/audit_2026-09-03/places_missing.json',encoding='utf-8'))
PAIR={'детски градини (общински, ЛИПСВАЩИ)':'Сграда за детско заведение',
      'ясли (ЛИПСВАЩИ)':'Сграда за детско заведение',
      'училища (ЛИПСВАЩИ регистрови реда)':'Сграда за образование',
      'болници (ЛИПСВАЩИ)':'Здравно заведение','ДКЦ (ЛИПСВАЩИ)':'Здравно заведение',
      'хосписи (ЛИПСВАЩИ)':'Здравно заведение'}
geo={}
for k,f in PAIR.items():
    for r in mis[k]:
        g=r.get('geo')
        if g and g.get('lat'): geo.setdefault(f,[]).append((r['name'],g['lat'],g['lon'],g.get('method','')))
for f,e in doc['hole'].items():
    if f not in geo: continue
    print('=== %s · %d свободни площадки срещу %d геокодирани липсващи реда' % (f,len(e['free60']),len(geo[f])))
    hit=0
    for s in e['free60']:
        g=unary_union([polys[i] for i in s['bodies']])
        c=[]
        for nm,la,lo,me in geo[f]:
            d=g.distance(Point(*to_m(lo,la)))
            if d<=200: c.append((round(d,1),nm,me))
        c.sort()
        if c:
            hit+=1
            print('   %-34s %7.0f m2 → %s' % ((s['addr'] or s['quar'] or '')[:34], s['area_m2'],
                  ' | '.join('%s (%.0f m, %s)'%(n[:34],d,m[:18]) for d,n,m in c[:2])))
    print('   площадки с поне един липсващ регистров ред на ≤200 m: %d от %d' % (hit,len(e['free60'])))
    print()
