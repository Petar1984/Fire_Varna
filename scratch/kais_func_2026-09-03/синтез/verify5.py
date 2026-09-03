# -*- coding: utf-8 -*-
"""V10: why 89 vs 80 - compare the two centroid definitions body by body."""
import json, sys, io, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
G='C:/git/'
info=json.load(open(G+'varna_3d/web/varna_buildings_info.json',encoding='utf-8'))
ci={c:i for i,c in enumerate(info['columns'])}; ROWS=info['rows']; FD=info['dict']['func']
idx_of={n:i for i,n in enumerate(FD)}
C=json.load(open('C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/kais_func_2026-09-03/регистри/kais_cache.json',encoding='utf-8'))
CEN=C['centroids']
gj=json.load(open(G+'varna_3d/web/varna_buildings_3d.geojson',encoding='utf-8'))
from shapely.geometry import shape
ids=[i for i,r in enumerate(ROWS) if r[ci['func']]==idx_of['Сграда за детско заведение']]
S={}
for f in gj['features']:
    i=f['properties']['i']
    if i in set(ids): S[i]=shape(f['geometry']).centroid
MX=111320.0*math.cos(math.radians(43.22)); MY=111320.0
worst=[]
for i in ids:
    a=S[i]; b=CEN[i]
    d=math.hypot((a.x-b[1])*MX,(a.y-b[0])*MY)
    worst.append((d,i))
worst.sort(reverse=True)
print('ДЗ тела:',len(ids))
print('max отклонение между двата центроида: %.1f m ; медиана %.2f m' % (worst[0][0], worst[len(worst)//2][0]))
print('топ 5:', [(round(d,1),i) for d,i in worst[:5]])
