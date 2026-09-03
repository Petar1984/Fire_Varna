# -*- coding: utf-8 -*-
"""Покритие по район: OSM POI, доставени места, тела по функция.

    set PYTHONIOENCODING=utf-8
    python osm_cov.py      ->  osm_cov.json + osm_cov.txt
"""
import json, os, sys, collections, pickle

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from geolib import to_xy, bbox, pt_ring_dist

info = json.load(open('C:/git/varna_3d/web/varna_buildings_info.json', encoding='utf-8'))
ROWS, D, COL = info['rows'], info['dict'], info['columns']
IC = {c: k for k, c in enumerate(COL)}
RAW = pickle.load(open(os.path.join(HERE, '_rings.pkl'), 'rb'))
XY, BB = {}, {}
for i, rs in RAW.items():
    pr = [to_xy(p[0], p[1]) for p in rs[0]]
    XY[i] = pr
    BB[i] = bbox(pr)

CELL = 120.0
grid = collections.defaultdict(list)
for i in range(len(ROWS)):
    b = BB[i]
    for gx in range(int(b[0] // CELL), int(b[2] // CELL) + 1):
        for gy in range(int(b[1] // CELL), int(b[3] // CELL) + 1):
            grid[(gx, gy)].append(i)


def near(xy, rmax=150.0):
    best = (float('inf'), None)
    for gx in range(int((xy[0] - rmax) // CELL), int((xy[0] + rmax) // CELL) + 1):
        for gy in range(int((xy[1] - rmax) // CELL), int((xy[1] + rmax) // CELL) + 1):
            for i in grid.get((gx, gy), ()):
                b = BB[i]
                if not (b[0] - rmax <= xy[0] <= b[2] + rmax
                        and b[1] - rmax <= xy[1] <= b[3] + rmax):
                    continue
                d = pt_ring_dist(xy, XY[i])
                if d < best[0]:
                    best = (d, i)
    return best


def reg_of(i):
    if i is None or ROWS[i][IC['reg']] < 0:
        return '(няма)'
    return D['reg'][ROWS[i][IC['reg']]]


out, res = [], {}


def w(t=''):
    print(t)
    out.append(t)


poi = json.load(open('C:/git/varna_3d/web/varna_poi_names.json', encoding='utf-8'))
c_poi = collections.Counter()
for r in poi['rows']:
    c_poi[reg_of(near(to_xy(r[3], r[2]))[1])] += 1
res['poi_by_reg'] = dict(c_poi)

pl = json.load(open('C:/git/Fire_Varna/data/places.json', encoding='utf-8'))['places']
c_pl = collections.Counter()
for p in pl:
    c_pl[reg_of(near(to_xy(p['lon'], p['lat']))[1])] += 1
res['places_by_reg'] = dict(c_pl)
res['places_by_src'] = dict(collections.Counter(p['src'] for p in pl))
res['places_osm'] = sum(1 for p in pl if p['src'].startswith('OSM'))

ho = json.load(open('C:/git/Fire_Varna/data/hotels.json', encoding='utf-8'))['hotels']
res['hotels_by_src'] = dict(collections.Counter(h.get('src', '') for h in ho))

FID = {n: k for k, n in enumerate(D['func'])}
res['bodies_by_reg'] = {}
for f in ('Сграда за детско заведение', 'Сграда за образование', 'Здравно заведение',
          'Хотел', 'Апартаментен хотел', 'Курортна, туристическа сграда'):
    res['bodies_by_reg'][f] = dict(collections.Counter(
        D['reg'][r[IC['reg']]] for r in ROWS
        if r[IC['func']] == FID[f] and r[IC['reg']] >= 0))

w('== OSM POI по район ==')
for k, v in c_poi.most_common():
    w(f'  {v:4d}  {k}')
w('== доставени места (places.json) по район ==')
for k, v in c_pl.most_common():
    w(f'  {v:4d}  {k}')
w('== places.json по src ==')
for k, v in res['places_by_src'].items():
    w(f'  {v:4d}  {k}')
w('== hotels.json по src ==')
for k, v in res['hotels_by_src'].items():
    w(f'  {v:4d}  {k}')
w('== тела по функция и район ==')
for f, d in res['bodies_by_reg'].items():
    w(f'  {f}: ' + ' · '.join(f'{k.replace("район ", "")}={v}'
                              for k, v in sorted(d.items(), key=lambda x: -x[1])))

json.dump(res, open(os.path.join(HERE, 'osm_cov.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
open(os.path.join(HERE, 'osm_cov.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print()
print('written osm_cov.json + osm_cov.txt')
