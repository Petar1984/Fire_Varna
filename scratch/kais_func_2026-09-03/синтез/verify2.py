# -*- coding: utf-8 -*-
"""V5-V7: register row count, VV bodies, and the clustering-method discrepancy."""
import json, sys, io, math
from collections import Counter, defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
G = 'C:/git/'
info = json.load(open(G+'varna_3d/web/varna_buildings_info.json', encoding='utf-8'))
COLS = info['columns']; ROWS = info['rows']; D = info['dict']
ci = {c: i for i, c in enumerate(COLS)}
func_dict = D['func']; reg_dict = D['reg']
idx_of = {n: i for i, n in enumerate(func_dict)}

print('=== V5 (регистри#7) регистрови редове ===')
pr = json.load(open(G+'Fire_Varna/scratch/audit_2026-09-03/places_registers.json', encoding='utf-8'))
tot = 0
for k, v in pr.items():
    if k == '_meta': continue
    n = len(v) if isinstance(v, list) else len(v.get('rows', []))
    tot += n
    print('  %-16s %3d' % (k, n))
print('  ОБЩО           %3d' % tot)

print()
print('=== V6 (правило§4б, парцели р.10) Владиславово: тела ДЗ ===')
vv = [i for i, r in enumerate(ROWS)
      if r[ci['func']] == idx_of['Сграда за детско заведение']
      and r[ci['reg']] >= 0 and 'Владислав Варненчик' in reg_dict[r[ci['reg']]]]
print('cmd: rows where func==ДЗ and reg contains "Владислав Варненчик" ->', len(vv))
print('по район (всички ДЗ тела):',
      Counter(reg_dict[r[ci['reg']]] if r[ci['reg']] >= 0 else '—'
              for r in ROWS if r[ci['func']] == idx_of['Сграда за детско заведение']).most_common())

print()
print('=== V7 РАЗМИНАВАНЕТО: клъстериране 45 m — полигон-полигон срещу центроид-центроид ===')
gj = json.load(open(G+'varna_3d/web/varna_buildings_3d.geojson', encoding='utf-8'))
from shapely.geometry import shape
from shapely.strtree import STRtree
LAT0, LON0 = 43.22, 27.92
MY = 111320.0; MX = 111320.0*math.cos(math.radians(LAT0))
geoms = {}
for f in gj['features']:
    i = f['properties']['i']
    g = shape(f['geometry'])
    geoms[i] = g

def proj(g):
    from shapely.ops import transform
    return transform(lambda x, y: ((x-LON0)*MX, (y-LAT0)*MY), g)

def clusters(ids, thr, mode):
    P = {i: proj(geoms[i]) for i in ids}
    if mode == 'centroid':
        C = {i: P[i].centroid for i in ids}
        objs = [C[i] for i in ids]
    else:
        objs = [P[i] for i in ids]
    tree = STRtree(objs)
    parent = {i: i for i in ids}
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def uni(a, b):
        ra, rb = find(a), find(b)
        if ra != rb: parent[rb] = ra
    for k, i in enumerate(ids):
        o = objs[k]
        for j in tree.query(o.buffer(thr)):
            jj = ids[j]
            if jj == i: continue
            if o.distance(objs[j]) <= thr: uni(i, jj)
    return len(set(find(i) for i in ids))

for name in ['Сграда за детско заведение', 'Сграда за образование', 'Здравно заведение']:
    ids = [i for i, r in enumerate(ROWS) if r[ci['func']] == idx_of[name]]
    a = clusters(ids, 1.0, 'poly'); b40 = clusters(ids, 40.0, 'poly')
    b = clusters(ids, 45.0, 'poly'); c = clusters(ids, 45.0, 'centroid')
    print('%-28s тела %4d | А(поли≤1m) %3d | поли≤40m %3d | поли≤45m %3d | ЦЕНТРОИД≤45m %3d'
          % (name, len(ids), a, b40, b, c))
