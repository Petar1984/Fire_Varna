# -*- coding: utf-8 -*-
"""Build a compact centroid cache for the KAIS buildings (read-only over C:/git)."""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

OUT = os.path.dirname(os.path.abspath(__file__))
GEO = 'C:/git/varna_3d/web/varna_buildings_3d.geojson'
INFO = 'C:/git/varna_3d/web/varna_buildings_info.json'

info = json.load(open(INFO, encoding='utf-8'))
COL = {c: i for i, c in enumerate(info['columns'])}
D = info['dict']
rows = info['rows']

fc = json.load(open(GEO, encoding='utf-8'))
feats = fc['features']
print('features', len(feats), 'rows', len(rows))

cent = [None] * len(rows)
n_multi = 0
for f in feats:
    i = f['properties']['i']
    g = f['geometry']
    if g['type'] == 'Polygon':
        ring = g['coordinates'][0]
    elif g['type'] == 'MultiPolygon':
        ring = g['coordinates'][0][0]; n_multi += 1
    else:
        continue
    # planar centroid of the outer ring (shoelace); fall back to mean for degenerate rings
    a = cx = cy = 0.0
    n = len(ring)
    for k in range(n - 1):
        x1, y1 = ring[k][0], ring[k][1]
        x2, y2 = ring[k + 1][0], ring[k + 1][1]
        cr = x1 * y2 - x2 * y1
        a += cr; cx += (x1 + x2) * cr; cy += (y1 + y2) * cr
    if abs(a) < 1e-14:
        xs = [p[0] for p in ring]; ys = [p[1] for p in ring]
        lon, lat = sum(xs) / len(xs), sum(ys) / len(ys)
    else:
        lon, lat = cx / (3 * a), cy / (3 * a)
    if i < len(cent):
        cent[i] = [round(lat, 6), round(lon, 6)]

missing = sum(1 for c in cent if c is None)
print('multipolygons', n_multi, 'rows without geometry', missing)

out = {
    '_meta': {
        'src_geojson': GEO, 'src_info': INFO,
        'n_features': len(feats), 'n_rows': len(rows),
        'rows_without_geometry': missing,
        'command': 'python build_cache.py',
    },
    'func_dict': D['func'],
    'centroids': cent,
    'func': [r[COL['func']] for r in rows],
    'area_m2': [r[COL['area_m2']] for r in rows],
    'floors': [r[COL['floors']] for r in rows],
    'addr': [(D['addr'][r[COL['addr']]] if r[COL['addr']] >= 0 else '') for r in rows],
    'quar': [(D['quar'][r[COL['quar']]] if r[COL['quar']] >= 0 else '') for r in rows],
    'reg': [(D['reg'][r[COL['reg']]] if r[COL['reg']] >= 0 else '') for r in rows],
    'prop': [(D['prop'][r[COL['prop']]] if r[COL['prop']] >= 0 else '') for r in rows],
}
p = os.path.join(OUT, 'kais_cache.json')
json.dump(out, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
print('written', p, os.path.getsize(p))
