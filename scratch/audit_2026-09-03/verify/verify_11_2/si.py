# -*- coding: utf-8 -*-
import json, io, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d=json.load(io.open(r'C:\git\Fire_Varna\data\search_index.json',encoding='utf-8'))
print(type(d), list(d)[:10] if isinstance(d,dict) else len(d))
