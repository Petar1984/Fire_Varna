# -*- coding: utf-8 -*-
"""Section 3 of the synthesis: delivered places on a foreign body / far from a correct one."""
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
BASE='C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/kais_func_2026-09-03/'
p=json.load(open(BASE+'правило/placement.json',encoding='utf-8'))
rows=p['placement']
bad=[r for r in rows if r['func_class']!='вярна']
print('НЕ-вярна функция:',len(bad),'| по клас:',{})
from collections import Counter
print(Counter(r['func_class'] for r in rows))
print('над 30 m от кое да е тяло:',[(r['name'],r['dist_m'],r['func']) for r in rows if r['dist_m']>30])
print('над 60 m:',[r['name'] for r in rows if r['dist_m']>60])
def bucket(r):
    d=r.get('ok_d')
    if d is None: return 'няма вярно тяло'
    if d>200: return 'ГРЕШКА (>200 m)'
    if d>60: return '60-200 m'
    if d>30: return '30-60 m'
    return 'ФЛАГ щракни (<=30 m)'
bad.sort(key=lambda r: -(r.get('ok_d') if r.get('ok_d') is not None else 1e9))
out=[]
for r in bad:
    out.append({'name':r['name'],'kind':r['kind'],'file':r['file'],'zone':r['zone'],'src':r['src'],
                'lat':r['lat'],'lon':r['lon'],'body_func':r['func'],'func_class':r['func_class'],
                'dist_m':r['dist_m'],'ok_d':r.get('ok_d'),'bucket':bucket(r),'addr':r.get('addr')})
json.dump(out,open('foreign_body.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(Counter(o['bucket'] for o in out))
print()
for o in out:
    if o['bucket'] in ('ГРЕШКА (>200 m)','60-200 m') or o['func_class']!='друга':
        print('%-9s %7s m | %-52s | %-14s | %-38s | %s' % (o['bucket'], o['ok_d'], o['name'][:52], o['kind'], o['body_func'][:38], o['zone']))
