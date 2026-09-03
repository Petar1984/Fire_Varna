# -*- coding: utf-8 -*-
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
d=json.load(open("C:/git/Varna_buildings/output/geocoder_index.json",encoding='utf-8'))
ent=d['entries']
by_pin={}
for e in ent: by_pin.setdefault(tuple(e['pin']),[]).append(e)
PINS=[(43.21726,27.92271),(43.21486,27.9253),(43.21614,27.92066),(43.22176,27.92891),
      (43.22217,27.92914),(43.22186,27.92608),(43.2191,27.92062),(43.22009,27.91845)]
print("--- 'кв. Левски, бл. 2 · вх. А' — авторитетът зад всеки от 8-те записа ---")
for p in PINS:
    for e in by_pin.get(p,[]):
        if e.get('kind')=='mf' and e.get('en') is not None:
            print(f"  {p}  cadnum={e.get('cadnum'):22s} section={str(e.get('section_cadnum')):22s} en={e.get('en')}")
            print(f"        complex_id={e.get('complex_id')}")
print()
print("--- 'цар симеон 36 · вх. В' ×2 (did 80012/80013) ---")
for p in [(43.19894,27.91273),(43.19901,27.91274)]:
    for e in by_pin.get(p,[]):
        if e.get('kind')=='mf': print(f"  {p} cad={e.get('cadnum')} sect={e.get('section_cadnum')} en={e.get('en')} complex={e.get('complex_id')}")
print("--- 'ул братя георгиевич 15 · вх. А' ×2 (did 51335/51336) ---")
for p in [(43.20863,27.91193),(43.20878,27.91184)]:
    for e in by_pin.get(p,[]):
        if e.get('kind')=='mf': print(f"  {p} cad={e.get('cadnum')} sect={e.get('section_cadnum')} en={e.get('en')} complex={e.get('complex_id')}")
