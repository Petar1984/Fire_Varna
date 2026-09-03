# -*- coding: utf-8 -*-
"""Section 4 of the synthesis: register rows with NO delivered place, by name."""
import json, sys, io
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
BASE='C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/kais_func_2026-09-03/'
r=json.load(open(BASE+'регистри/registry_geocoded.json',encoding='utf-8'))
SK={'_meta','ОБРАТНО: доставени места без регистров ред','КАИС места по клас (целият град)'}
DEL={'доставено по име','доставено по положение'}
rows=[]
for cls in r:
    if cls in SK: continue
    for y in r[cls]:
        rows.append((cls,y))
print('регистрови реда общо:',len(rows))
print('delivered_status:',Counter(y['delivered_status'] for _,y in rows))
miss=[(c,y) for c,y in rows if y['delivered_status'] not in DEL]
print('НЕдоставени:',len(miss),'| по присъда:',Counter(y['verdict'] for _,y in miss))
out=[]
for c,y in miss:
    s=(y.get('sites') or [None])[0]
    out.append({'клас':c,'име':y['name'],'адрес':y['address'],'присъда':y['verdict'],
                'геокод':(y['geo'] or {}).get('method'),'увереност':(y['geo'] or {}).get('confidence'),
                'lat':(y['geo'] or {}).get('lat'),'lon':(y['geo'] or {}).get('lon'),
                'място_lat':s['lat'] if s else None,'място_lon':s['lon'] if s else None,
                'd_m':s['d_m'] if s else None,'тела':s['n_bodies'] if s else None,
                'площ':s['area_m2'] if s else None,'addr_КАИС':s['addr'] if s else None,
                'район':s['reg'] if s else None,'n_sites_150':y.get('n_sites_150')})
json.dump(out,open('missing_register_rows.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for v in ['еднозначно','спорно','без тяло','село — извън гр. Варна','адресът не се геокодира']:
    g=[o for o in out if o['присъда']==v]
    print()
    print('### %s — %d' % (v,len(g)))
    for o in g:
        print('  [%s] %-52s | %-46s | %s | d=%s m | %s тела %s m2 | %s' % (
            o['клас'][:14], o['име'][:52], (o['адрес'] or '')[:46], (o['увереност'] or '—'),
            o['d_m'], o['тела'], o['площ'], (o['addr_КАИС'] or '')[:34]))
