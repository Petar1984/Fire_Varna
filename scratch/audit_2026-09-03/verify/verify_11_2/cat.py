# -*- coding: utf-8 -*-
import json, io, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d=json.load(io.open(r'C:\git\Fire_Varna\data\place_categories.json',encoding='utf-8'))
print(type(d), list(d)[:10] if isinstance(d,dict) else len(d))
s=json.dumps(d, ensure_ascii=False)
for k in ('болница','дкц','диспансер','медицински'):
    print(k, k in s.lower())
print(s[:1500])
