# -*- coding: utf-8 -*-
import sys, io, collections, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from fvlib import *
AUT=json.load(open("C:/git/Varna_buildings/output/geocoder_index.json",encoding='utf-8'))['entries']
bypin={}
for e in AUT: bypin.setdefault((tuple(e['pin']),str(e.get('en'))),[]).append(e)
ENT=[e for e in E if e.get('kind')=='mf' and e.get('en') is not None]
by=collections.defaultdict(list)
for e in ENT: by[norm(fmt(e))].append(e)
print("unique entrance labels =",len(by), " entrance entries =",len(ENT))
B={l:v for l,v in by.items() if len({e.get('g') for e in v})>1}
A={l:v for l,v in by.items() if len({e.get('g') for e in v})==1 and len({tuple(e['pin']) for e in v})>1}
print("B groups=%d (%.1f%% of labels) entries=%d (%.1f%% of entries)"%(len(B),100*len(B)/len(by),sum(len(v) for v in B.values()),100*sum(len(v) for v in B.values())/len(ENT)))
print("A groups=%d entries=%d"%(len(A),sum(len(v) for v in A.values())))
ac=0; dists=[]
for lab,es in A.items():
    cads=set()
    for e in es:
        for a in bypin.get((tuple(e['pin']),str(e.get('en'))),[]):
            if a.get('kind')=='mf': cads.add(a.get('cadnum'))
    if len(cads)>1: ac+=1
    pts=[tuple(e['pin']) for e in es]
    dists.append((max(dm(x,y) for i,x in enumerate(pts) for y in pts[i+1:]), fmt(es[0]), len(es)))
print("A groups where the hidden pin is a DIFFERENT cadnum =",ac,"of",len(A))
dists.sort(reverse=True)
print("class A - largest hidden separation:")
for d,l,n in dists[:8]: print("   %7.1f m  n=%d  %s"%(d,n,l))
print("class A - smallest:")
for d,l,n in sorted(dists)[:4]: print("   %7.1f m  n=%d  %s"%(d,n,l))
