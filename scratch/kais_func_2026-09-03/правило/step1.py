# -*- coding: utf-8 -*-
import sys, json, time
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from lib_kais import *
t0=time.time()
info, cols = load_info()
print('cols', cols)
polys = load_geoms()
print('geoms', len(polys), '%.1fs' % (time.time()-t0))
dl = load_delivered()
print('delivered', len(dl))
from shapely.strtree import STRtree
tree = STRtree(polys)
print('tree built %.1fs' % (time.time()-t0))
# sanity: total area vs area_m2 column
import statistics
ia = cols['area_m2']
sample = [0, 1, 2, 100, 5000, 40000, 80496]
for i in sample:
    print(i, 'shapely %.1f' % polys[i].area, 'kais', info['rows'][i][ia])
