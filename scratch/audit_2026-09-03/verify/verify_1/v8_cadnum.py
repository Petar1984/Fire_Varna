# -*- coding: utf-8 -*-
import sys, io, json, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
d=json.load(open("C:/git/Varna_buildings/output/geocoder_index.json",encoding='utf-8'))
ent=d['entries']
def key(e): return (e.get('addr_key') or '')
sel=[e for e in ent if e.get('kind')=='mf' and e.get('en') is not None and 'левски' in key(e).lower() and 'бл. 2' in key(e)]
sel=[e for e in sel if key(e).strip().endswith('бл. 2') or ', бл. 2' == key(e)[-7:]]
print("--- авторитет: входове с addr_key завършващ 'кв. Левски, бл. 2', вх. А ---")
for e in ent:
    if e.get('kind')=='mf' and str(e.get('en'))=='А' and (e.get('addr_key') or '')=='кв. Левски, бл. 2':
        print(f"  id={e['id']:6d} pin={e['pin']} cadnum={e.get('cadnum')} section={e.get('section_cadnum')} complex={e.get('complex_id')} bg={e.get('bg')} phys={e.get('physical_building_id')}")
print()
# всички addr_key варианти около 'Левски, бл. 2'
c=collections.Counter(e.get('addr_key') for e in ent if e.get('addr_key') and 'Левски, бл. 2' in e.get('addr_key'))
for k,v in sorted(c.items()): print(f"  {v:4d}  {k}")
