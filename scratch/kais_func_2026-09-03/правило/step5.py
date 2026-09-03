# -*- coding: utf-8 -*-
"""Cluster the free bodies into sites; break down by район."""
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
dictf=info['dict']['func']; fi=cols['func']

def clusters(idxs, gap=40.0):
    """union-find on 'polygons within gap metres'"""
    sub=[polys[i] for i in idxs]
    t=STRtree(sub)
    par=list(range(len(idxs)))
    def find(a):
        while par[a]!=a: par[a]=par[par[a]]; a=par[a]
        return a
    for a,p in enumerate(sub):
        for b in t.query(p.buffer(gap)):
            b=int(b)
            if b<=a: continue
            if p.distance(sub[b])<=gap:
                ra,rb=find(a),find(b)
                if ra!=rb: par[ra]=rb
    g=collections.defaultdict(list)
    for a in range(len(idxs)): g[find(a)].append(idxs[a])
    return list(g.values())

for fname in ['Сграда за детско заведение','Сграда за образование','Здравно заведение',
              'Хотел','Апартаментен хотел','Курортна, туристическа сграда']:
    k=dictf.index(fname)
    idxs=[i for i,r in enumerate(rows) if r[fi]==k]
    free=[]
    for i in idxs:
        p=polys[i]
        if not [j for j in ptree.query(p.buffer(30.0)) if pts[int(j)].distance(p)<=30.0]:
            free.append(i)
    cl=clusters(free)
    byreg=collections.Counter()
    for c in cl:
        byreg[field(info,cols,rows[c[0]],'reg')]+=1
    print('%-32s тела БЕЗ място %4d → площадки (клъстери ≤40 m) %4d' % (fname,len(free),len(cl)))
    print('      по район: '+' · '.join('%s %d'%(r,n) for r,n in byreg.most_common()))
    json.dump([sorted(c) for c in cl], open('_cl_%d.json'%k,'w'))
