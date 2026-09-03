# -*- coding: utf-8 -*-
import json, io, sys, collections
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d=json.load(io.open(r'C:\git\Fire_Varna\data\places.json',encoding='utf-8'))
P=d['places']
print('N places', len(P))
print('by_kind', json.dumps(d['_meta']['by_kind'], ensure_ascii=False))
print('--- excluded ---')
print(json.dumps(d['_meta']['excluded'], ensure_ascii=False, indent=1)[:4000])
print('--- targets ---')
for i,p in enumerate(P):
    n=p.get('name','')
    if any(k in n for k in ['Аджибадем','Майчин','Диспансер','белодроб','СБАЛПФЗ','Нова','Оксигена','Олимед']):
        print(i, json.dumps(p, ensure_ascii=False))
print('--- all kind=болница/ДКЦ ---')
for i,p in enumerate(P):
    if p.get('kind') in ('болница','ДКЦ','хоспис'):
        print(i, p.get('kind'),'|', p.get('name'),'|', p.get('src'),'|', p.get('lat'), p.get('lon'))
