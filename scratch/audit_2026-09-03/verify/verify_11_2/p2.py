# -*- coding: utf-8 -*-
import json, io, sys, collections
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d=json.load(io.open(r'C:\git\varna_3d\data\places.json',encoding='utf-8'))
print(type(d), list(d)[:8] if isinstance(d,dict) else len(d))
P = d['places'] if isinstance(d,dict) and 'places' in d else d
print('N', len(P))
print(collections.Counter(p.get('subtype') for p in P if p.get('kind')=='venue'))
print('--- МЦ rows ---')
for i,p in enumerate(P):
    if p.get('subtype')=='медицински център':
        print(i, json.dumps(p, ensure_ascii=False)[:400])
print('--- name matches ---')
for i,p in enumerate(P):
    n = str(p.get('name',''))
    if any(k in n for k in ['джибадем','Майчин','майчин','белодроб','Диспансер','СБАЛПФЗ','пневмо','Пневмо']):
        print(i, json.dumps(p, ensure_ascii=False)[:600])
