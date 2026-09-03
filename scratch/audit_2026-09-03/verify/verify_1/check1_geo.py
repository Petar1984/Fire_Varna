# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №1 / находка №3 — независима проверка на координатите."""
import json, math, re, sys, io, hashlib
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

FV = r'C:/git/Fire_Varna'

def sha(p):
    return hashlib.sha256(open(p,'rb').read()).hexdigest()[:16]

def hav(a, b):
    R = 6371008.8
    la1, lo1, la2, lo2 = map(math.radians, [a[0], a[1], b[0], b[1]])
    dla, dlo = la2-la1, lo2-lo1
    h = math.sin(dla/2)**2 + math.cos(la1)*math.cos(la2)*math.sin(dlo/2)**2
    return 2*R*math.asin(math.sqrt(h))

places = json.load(open(FV+'/data/places.json', encoding='utf-8'))['places']
rows = json.load(open(FV+'/data/address_rows.json', encoding='utf-8'))
print('sha16 places.json =', sha(FV+'/data/places.json'))
print('sha16 address_rows.json =', sha(FV+'/data/address_rows.json'))
print('rows type', type(rows).__name__, len(rows))

by = {}
for p in places:
    by.setdefault(p['name'], []).append(p)

def get(sub):
    return [p for p in places if sub.lower() in p['name'].lower()]

kard = get('Кардиолайф')[0]
sbalk = [p for p in places if 'кардиология Варна' in p['name']][0]
elen = get('Елеонора')[0]
print('Кардиолайф :', kard['lat'], kard['lon'], kard['zone'])
print('СБАЛК Варна:', sbalk['lat'], sbalk['lon'], sbalk['zone'])
print('Ц.Елеонора :', elen['lat'], elen['lon'], elen['zone'])
print('d(Кардиолайф, СБАЛК Варна) = %.1f m' % hav((kard['lat'],kard['lon']),(sbalk['lat'],sbalk['lon'])))
print('d(Кардиолайф, Ц.Елеонора)  = %.1f m' % hav((kard['lat'],kard['lon']),(elen['lat'],elen['lon'])))
