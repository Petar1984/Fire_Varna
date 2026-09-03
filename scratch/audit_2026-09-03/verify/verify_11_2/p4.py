# -*- coding: utf-8 -*-
import json, io, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d=json.load(io.open(r'C:\git\varna_3d\web\varna_poi_names.json',encoding='utf-8'))
print('fields', json.dumps(d['fields'], ensure_ascii=False))
R=d['rows']
print('N rows', len(R))
F=d['fields']
def rec(r): return dict(zip(F,r))
for idx in (148, 222, 223, 233, 232, 30, 63):
    print(idx, json.dumps(rec(R[idx]), ensure_ascii=False)[:400])
print('--- by name ---')
for i,r in enumerate(R):
    o=rec(r); n=str(o.get('name',''))
    if any(k in n for k in ['джибадем','Майчин','Диспансер','лястовиц','Белодроб']):
        print(i, json.dumps(o, ensure_ascii=False)[:400])
