# -*- coding: utf-8 -*-
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
d=json.load(open("C:/git/Varna_buildings/output/block_identity_sidecar.json",encoding='utf-8'))
print(type(d), (list(d.keys())[:8] if isinstance(d,dict) else len(d)))
if isinstance(d,dict):
    k=list(d.keys())
    for kk in k[:3]: print(kk, json.dumps(d[kk],ensure_ascii=False)[:400])
