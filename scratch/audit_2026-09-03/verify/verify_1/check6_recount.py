# -*- coding: utf-8 -*-
"""Строг пре-брой на покритието по здравеопазване (независим от measure_places.py)."""
import json, sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
FV = r'C:/git/Fire_Varna'
places = json.load(open(FV+'/data/places.json', encoding='utf-8'))['places']
hotels = json.load(open(FV+'/data/hotels.json', encoding='utf-8'))
si = json.load(open(FV+'/data/search_index.json', encoding='utf-8'))

names_all = [p['name'] for p in places]
def blob():
    s = json.dumps(places, ensure_ascii=False) + json.dumps(hotels, ensure_ascii=False)
    return s.lower()
B = blob()
SI = json.dumps(si, ensure_ascii=False).lower()

probes = {
 'диализ': 'диализ',
 'Виртус': 'виртус',
 'Ненов': 'ненов',
 'Хипократ': 'хипократ',
 'Лисичкова': 'лисичкова',
 'СБР Варна / рехабилитация': 'рехабилитац',
 'Света Елена': 'елена 1',
 'доц. Георгиев (очна)': 'георгиев',
 'Клементина': 'клементина',
 'Еквита': 'еквита',
 'Младост-М': 'младост-м',
 'Надежда (хоспис)': 'хоспис надежда',
 'Магдалена': 'магдалена',
 'Медицинска грижа': 'медицинска грижа',
}
print('=== има ли ги изобщо в доставката (places+hotels) / в search_index ===')
for lbl, pat in probes.items():
    print('%-28s places/hotels: %-5s search_index: %s' % (lbl, pat in B, pat in SI))
print()
print('=== всички имена на здравни места ===')
for p in places:
    if p['kind'] in ('болница','ДКЦ','хоспис'):
        print(' ', p['kind'], '|', p['name'])
