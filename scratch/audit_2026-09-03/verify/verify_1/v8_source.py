# -*- coding: utf-8 -*-
import sys, io, json, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
p="C:/git/Varna_buildings/output/geocoder_index.json"
d=json.load(open(p,encoding='utf-8'))
print("keys:",list(d.keys())[:12])
ent=d.get('entries') or d.get('records') or None
print("entries:",len(ent) if ent else None)
if ent: 
    ks=collections.Counter()
    for e in ent[:5000]:
        for k in e: ks[k]+=1
    print(sorted(ks))
    print(json.dumps(ent[0],ensure_ascii=False)[:600])
