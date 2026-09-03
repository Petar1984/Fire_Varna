# -*- coding: utf-8 -*-
import json, io, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d=json.load(io.open(r'C:\git\varna_3d\web\varna_buildings_info.json',encoding='utf-8'))
print(type(d), list(d)[:10] if isinstance(d,dict) else len(d))
if isinstance(d,dict) and 'fields' in d:
    print('fields', json.dumps(d['fields'], ensure_ascii=False))
    R=d.get('rows') or d.get('items')
    F=d['fields']
    for idx in (1523, 51508, 55428, 8600, 26117, 39593):
        try: print(idx, json.dumps(dict(zip(F,R[idx])), ensure_ascii=False)[:400])
        except Exception as e: print(idx,'ERR',e)
else:
    print(json.dumps(d if not isinstance(d,list) else d[:2], ensure_ascii=False)[:1200])
