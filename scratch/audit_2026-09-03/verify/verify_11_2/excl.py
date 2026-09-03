# -*- coding: utf-8 -*-
import json, io, sys, collections
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d=json.load(io.open(r'C:\git\Fire_Varna\data\places.json',encoding='utf-8'))
E=d['_meta']['excluded']
print('excluded N', len(E))
print(collections.Counter(e['why'].split(':')[0] if ':' in e['why'] else e['why'][:30] for e in E))
mc=[e for e in E if 'МЦ' in e['why'] or 'медицински център' in e['why']]
print('\nМЦ-мотивирани изключвания:', len(mc))
for e in mc: print('  ', e['src'][:6],'|', e['kind'],'|', e['name'][:70],'|', e['why'][:90])
