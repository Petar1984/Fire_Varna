# -*- coding: utf-8 -*-
"""Synthesis auditor: independent re-measurement of 3+ numbers per measurer.
READ-ONLY over C:/git. Deterministic."""
import json, sys, io, math
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

G = 'C:/git/'
info = json.load(open(G+'varna_3d/web/varna_buildings_info.json', encoding='utf-8'))
COLS = info['columns']; ROWS = info['rows']; D = info['dict']
ci = {c: i for i, c in enumerate(COLS)}
func_dict = D['func']; reg_dict = D['reg']; addr_dict = D['addr']; prop_dict = D['prop']

print('=== V1 (парцели#1, регистри#1, правило§1) func речник ===')
print('cmd: len(info["dict"]["func"]) ; Counter(row[func])')
print('func стойности:', len(func_dict))
fc = Counter(r[ci['func']] for r in ROWS)
empty = fc.get(-1, 0)
print('редове общо:', len(ROWS), '| с празна func (-1):', empty, '| с func:', len(ROWS)-empty)
TARGET = ['Сграда за детско заведение','Сграда за образование','Здравно заведение',
          'Хотел','Апартаментен хотел','Курортна, туристическа сграда','Общежитие',
          'Заведение за социални грижи']
idx_of = {n: i for i, n in enumerate(func_dict)}
for n in TARGET:
    print('  %-32s %5d' % (n, fc.get(idx_of[n], 0)))

print()
print('=== V2 (правило§0, парцели osm_cov) доставка ===')
print('cmd: len(places.json), len(hotels.json), Counter(src)')
places = json.load(open(G+'Fire_Varna/data/places.json', encoding='utf-8'))
hotels = json.load(open(G+'Fire_Varna/data/hotels.json', encoding='utf-8'))
pl = places['places'] if isinstance(places, dict) and 'places' in places else places
ho = hotels['hotels'] if isinstance(hotels, dict) and 'hotels' in hotels else hotels
print('places:', len(pl), '| hotels:', len(ho), '| общо:', len(pl)+len(ho))
print('places по src:', Counter((p.get('src') or '')[:40] for p in pl).most_common())
print('places по kind:', Counter(p.get('kind') for p in pl).most_common())

print()
print('=== V3 (правило§5, парцели§9) контролните точки ===')
print('cmd: shapely covers() върху varna_buildings_3d.geojson + rows[i]')
gj = json.load(open(G+'varna_3d/web/varna_buildings_3d.geojson', encoding='utf-8'))
feats = gj['features']
print('полигони:', len(feats))
byi = {}
for f in feats:
    byi[f['properties']['i']] = f
print('уникални i:', len(byi), '| min/max:', min(byi), max(byi))
from shapely.geometry import shape, Point
CP = [('а', 43.24473, 27.85411, 18116), ('б', 43.24456, 27.84592, 16753),
      ('в', 43.24946, 27.84414, 16619), ('г', 43.24709, 27.85397, 18347)]
for lbl, lat, lon, i in CP:
    f = byi[i]; g = shape(f['geometry'])
    inside = g.covers(Point(lon, lat))
    r = ROWS[i]
    print('  (%s) i=%d вътре=%s func=%s prop=%s ет=%s площ_КАИС=%s addr=%s' % (
        lbl, i, inside, func_dict[r[ci['func']]], prop_dict[r[ci['prop']]],
        r[ci['floors']], r[ci['area_m2']],
        addr_dict[r[ci['addr']]] if r[ci['addr']] >= 0 else '—'))

print()
print('=== V4 (регистри) регистрови редове и адресна машина ===')
print('cmd: len(places_registers.json rows), len(address_rows.json rows/keys)')
pr = json.load(open(G+'Fire_Varna/scratch/audit_2026-09-03/places_registers.json', encoding='utf-8'))
def count_rows(o):
    if isinstance(o, list): return len(o)
    if isinstance(o, dict):
        for k in ('rows','registers','items','records'):
            if k in o and isinstance(o[k], list): return len(o[k])
    return None
print('places_registers top keys:', list(pr.keys()) if isinstance(pr, dict) else 'list')
ar = json.load(open(G+'Fire_Varna/data/address_rows.json', encoding='utf-8'))
arows = ar['rows'] if isinstance(ar, dict) and 'rows' in ar else ar
print('address_rows редове:', len(arows), '| различни ключа:', len({r[0] for r in arows}))
poi = json.load(open(G+'varna_3d/web/varna_poi_names.json', encoding='utf-8'))
prows = poi['rows'] if isinstance(poi, dict) and 'rows' in poi else poi
print('varna_poi_names редове:', len(prows), '| полета:', poi.get('fields') if isinstance(poi, dict) else '')
