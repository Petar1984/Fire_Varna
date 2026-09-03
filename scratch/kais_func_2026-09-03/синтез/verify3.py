# -*- coding: utf-8 -*-
"""V8: reproduce the 'регистри' site count with THEIR centroid cache + THEIR rule,
   then compare to polygon-min-distance on the same ids."""
import json, sys, io, math
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
C = json.load(open('C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/kais_func_2026-09-03/регистри/kais_cache.json', encoding='utf-8'))
CENT = C['centroids']; FUNC = C['func']; FD = C['func_dict']
idx_of = {n: i for i, n in enumerate(FD)}
def dm(a, b):
    R = 6371000.0
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    h = (math.sin((p2-p1)/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(math.radians(b[1]-a[1])/2)**2)
    return 2*R*math.asin(math.sqrt(h))
def sites(ids, link):
    par = {i: i for i in ids}
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    # brute force O(n^2) - no grid, so no bucketing artefacts
    for a in range(len(ids)):
        for b in range(a+1, len(ids)):
            i, j = ids[a], ids[b]
            if dm(CENT[i], CENT[j]) <= link:
                ra, rb = f(i), f(j)
                if ra != rb: par[ra] = rb
    return len(set(f(i) for i in ids))
print('V8 · клъстери по ЦЕНТРОИД (кешът на „регистри“), brute force, без решетка')
for n in ['Сграда за детско заведение', 'Сграда за образование', 'Здравно заведение']:
    ids = [i for i, fv in enumerate(FUNC) if fv == idx_of[n]]
    print('  %-28s тела %4d | ≤45 m %3d | ≤40 m %3d | ≤30 m %3d' %
          (n, len(ids), sites(ids, 45.0), sites(ids, 40.0), sites(ids, 30.0)))
