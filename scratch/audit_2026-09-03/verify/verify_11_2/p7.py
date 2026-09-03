# -*- coding: utf-8 -*-
import json, io, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d=json.load(io.open(r'C:\git\varna_3d\web\varna_buildings_info.json',encoding='utf-8'))
print('columns', json.dumps(d['columns'], ensure_ascii=False))
print('note', json.dumps(d.get('note'), ensure_ascii=False)[:800])
print('address_model', json.dumps(d.get('address_model'), ensure_ascii=False)[:400])
R=d['rows']; C=d['columns']; DIC=d['dict']
print('N rows', len(R))
def rec(i):
    o=dict(zip(C,R[i]))
    out={}
    for k,v in o.items():
        if k in DIC and isinstance(v,int) and 0<=v<len(DIC[k]):
            out[k]=DIC[k][v]
        else:
            out[k]=v
    return out
for idx in (1522,1523,51508,55428,8600,26117,39593):
    print(idx, json.dumps(rec(idx), ensure_ascii=False)[:500])
