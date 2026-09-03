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
B={l:v for l,v in by.items() if len({e.get('g') for e in v})>1}
cause=collections.Counter(); prefix=collections.Counter(); rows_total=0
examples=collections.defaultdict(list)
for lab,es in B.items():
    rows_total += len({e.get('g') for e in es})
    cids=set()
    for e in es:
        for a in bypin.get((tuple(e['pin']),str(e.get('en'))),[]):
            if a.get('kind')=='mf': cids.add(a.get('complex_id'))
    kinds={ (c.split('|')[1] if c and '|' in c else '?') for c in cids }
    k = 'block' if kinds=={'block'} else ('addr' if kinds=={'addr'} else '+'.join(sorted(kinds)))
    cause[k]+=1
    examples[k].append(fmt(es[0]))
    prefix[fmt(es[0]).split(',')[0]]+=1
print("class B groups =",len(B)," dropdown rows total =",rows_total)
print("cause by complex_id type:",dict(cause))
for k,v in examples.items(): print("   ",k,"->",v[:4])
print("TOP prefix:")
for z,n in prefix.most_common(12): print("   %4d  %s"%(n,z))
