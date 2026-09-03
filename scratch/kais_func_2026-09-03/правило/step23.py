# -*- coding: utf-8 -*-
"""Съвпадение по АДРЕСЕН НИЗ (улица+номер), не по геокод."""
import sys, json, re, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
info,cols=load_info(); rows=info['rows']
doc=json.load(open('placement.json',encoding='utf-8'))
mis=json.load(open(G+'Fire_Varna/scratch/audit_2026-09-03/places_missing.json',encoding='utf-8'))
def nrm(s):
    s=(s or '').lower().replace('ул.',' ').replace('бул.',' ').replace('"',' ').replace('“',' ').replace('„',' ')
    s=s.replace('№',' ').replace('.',' ').replace('-',' ').replace(',',' ')
    s=re.sub(r'\b(гр|кв|ж|к|с|о|м|т|р|н|до|бл|блок)\b',' ',s)
    return ' '.join(s.split())
def key(street,num):
    return nrm(street)+' '+nrm(str(num)) if street and num is not None else None
# КАИС ключове на свободните площадки
free={}
for f,e in doc['hole'].items():
    for s in e['free60']:
        for i in s['bodies']:
            st=field(info,cols,rows[i],'street'); nu=field(info,cols,rows[i],'num')
            k=key(st,nu)
            if k: free.setdefault(f,{}).setdefault(k,s); break
PAIR={'детски градини (общински, ЛИПСВАЩИ)':'Сграда за детско заведение',
      'ясли (ЛИПСВАЩИ)':'Сграда за детско заведение',
      'училища (ЛИПСВАЩИ регистрови реда)':'Сграда за образование',
      'болници (ЛИПСВАЩИ)':'Здравно заведение','ДКЦ (ЛИПСВАЩИ)':'Здравно заведение',
      'хосписи (ЛИПСВАЩИ)':'Здравно заведение'}
tot=hit=0
for k,f in PAIR.items():
    for r in mis[k]:
        tot+=1
        a=nrm(r.get('address'))
        for kk,s in (free.get(f) or {}).items():
            toks=kk.split()
            if len(toks)>=2 and ' '.join(toks) in a:
                hit+=1
                print('   ТОЧЕН АДРЕС: %-40s ←→ КАИС „%s“ (%d тела, %.0f m2, %s)'
                      % (r['name'][:40], kk, len(s['bodies']), s['area_m2'], (s['reg'] or '')[:20]))
                break
print('   регистрови липсващи реда: %d · с ТОЧНО съвпадение улица+номер срещу свободна площадка: %d' % (tot,hit))
