# -*- coding: utf-8 -*-
import json, io, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d=json.load(io.open(r'C:\git\varna_3d\data\places.json',encoding='utf-8'))
P=d['places']
for idx in (232, 148):
    print(idx, json.dumps(P[idx], ensure_ascii=False)[:700])
print('--- ДГ 52 ---')
for i,p in enumerate(P):
    n=str(p.get('name',''))
    if '52' in n or 'лястовиц' in n:
        print(i, json.dumps(p, ensure_ascii=False)[:500])
