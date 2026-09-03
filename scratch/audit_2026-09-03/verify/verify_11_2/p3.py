# -*- coding: utf-8 -*-
import json, io, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d=json.load(io.open(r'C:\git\varna_3d\web\varna_poi_names.json',encoding='utf-8'))
print(type(d), list(d)[:8] if isinstance(d,dict) else len(d))
R = d['items'] if isinstance(d,dict) and 'items' in d else (d['poi'] if isinstance(d,dict) and 'poi' in d else d)
if isinstance(R,dict): R=list(R.values())
print('N', len(R))
for idx in (148, 222, 223, 233, 232):
    try:
        print(idx, json.dumps(R[idx], ensure_ascii=False)[:500])
    except Exception as e:
        print(idx, 'ERR', e)
print('--- by name ---')
for i,p in enumerate(R):
    n=str(p.get('name',''))
    if any(k in n for k in ['джибадем','Майчин','Диспансер','Бялата лястовица','52']):
        print(i, json.dumps(p, ensure_ascii=False)[:400])
