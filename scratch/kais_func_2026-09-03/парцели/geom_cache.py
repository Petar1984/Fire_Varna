# -*- coding: utf-8 -*-
"""Extract building geometry (exterior rings) for selected func classes into a cache."""
import json, sys, os, collections
sys.stdout.reconfigure(encoding='utf-8')

GIT = 'C:/git'
INFO = GIT + '/varna_3d/web/varna_buildings_info.json'
GEO  = GIT + '/varna_3d/web/varna_buildings_3d.geojson'
OUT  = os.path.dirname(os.path.abspath(__file__))

info = json.load(open(INFO, encoding='utf-8'))
rows, D = info['rows'], info['dict']

gj = json.load(open(GEO, encoding='utf-8'))
feats = gj['features']
print('features', len(feats), 'rows', len(rows))

gtypes = collections.Counter(f['geometry']['type'] for f in feats)
print('geometry types', dict(gtypes))

# index by properties.i
byi = {}
dup = 0
for f in feats:
    i = f['properties']['i']
    if i in byi: dup += 1
    byi[i] = f
print('unique i', len(byi), 'dups', dup)
print('i range', min(byi), max(byi))

# ring extraction
def rings(g):
    if g['type'] == 'Polygon':
        return [g['coordinates'][0]]
    if g['type'] == 'MultiPolygon':
        return [p[0] for p in g['coordinates']]
    return []

out = {}
for i, f in byi.items():
    rs = rings(f['geometry'])
    out[i] = rs
json.dump({'n': len(out)}, open(OUT + '/_geom_meta.json', 'w'))

import pickle
pickle.dump(out, open(OUT + '/_rings.pkl', 'wb'))
print('cached rings for', len(out))
