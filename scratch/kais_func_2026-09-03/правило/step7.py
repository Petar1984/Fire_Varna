# -*- coding: utf-8 -*-
"""Site-level hole: cluster bodies first, then ask whether the SITE has a place."""
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

MATCH={'Сграда за детско заведение':{'детска градина'},
       'Сграда за образование':{'училище','университет'},
       'Здравно заведение':{'болница','ДКЦ','хоспис'},
       'Хотел':{'Хотел','Семеен хотел','апарт-хотел','хотел · без категоризация'},
       'Апартаментен хотел':{'Хотел','Семеен хотел','апарт-хотел','хотел · без категоризация'},
       'Курортна, туристическа сграда':{'Хотел','Семеен хотел','апарт-хотел','хотел · без категоризация'}}

def clusters(idxs, gap=40.0):
    sub=[polys[i] for i in idxs]; t=STRtree(sub); par=list(range(len(idxs)))
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
    return [sorted(v) for v in g.values()]

out={}
for fname,kinds in MATCH.items():
    k=dictf.index(fname)
    idxs=[i for i,r in enumerate(rows) if r[fi]==k]
    cl=clusters(idxs)
    stats={}
    for thr in (10.0,30.0,60.0,120.0):
        cov=0
        for c in cl:
            hit=False
            for i in c:
                p=polys[i]
                for j in ptree.query(p.buffer(thr)):
                    j=int(j)
                    if pts[j].distance(p)<=thr and dl[j]['kind'] in kinds: hit=True;break
                if hit:break
            cov+= 1 if hit else 0
        stats[thr]=(cov,len(cl)-cov)
    print('%-32s тела %5d · площадки %4d | ' % (fname,len(idxs),len(cl)) +
          ' · '.join('≤%dm покрити %d/непокрити %d'%(int(t),v[0],v[1]) for t,v in stats.items()))
    out[fname]={'bodies':len(idxs),'clusters':len(cl),
                'cov':{str(int(t)):{'covered':v[0],'free':v[1]} for t,v in stats.items()},
                'cl':cl}
json.dump(out, open('_step7.json','w',encoding='utf-8'), ensure_ascii=False)
