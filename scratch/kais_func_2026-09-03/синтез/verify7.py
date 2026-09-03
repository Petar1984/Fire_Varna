# -*- coding: utf-8 -*-
"""V12: size of the centroid defect in the 'регистри' cache, over all 635 bodies
of the three classes + the four control-point bodies."""
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
TG=['Сграда за детско заведение','Сграда за образование','Здравно заведение']
ids=set(i for i,r in enumerate(ROWS) if FD[r[ci['func']]] in TG) if True else set()
ids=set(i for i,r in enumerate(ROWS) if r[ci['func']]>=0 and FD[r[ci['func']]] in TG)
MX=111320.0*math.cos(math.radians(43.22)); MY=111320.0
dev=[]; cp={18116:'а',16753:'б',16619:'в',18347:'г'}
cpdev={}
for f in gj['features']:
    i=f['properties']['i']
    if i in ids or i in cp:
        c=shape(f['geometry']).centroid; b=CEN[i]
        d=math.hypot((c.x-b[1])*MX,(c.y-b[0])*MY)
        if i in ids: dev.append(d)
        if i in cp: cpdev[i]=d
dev.sort()
n=len(dev)
print('тела в трите класа:',n)
print('отклонение центроид (кеш на „регистри“) срещу истинския центроид:')
print('  медиана %.2f m | 90-и персентил %.1f m | максимум %.1f m | >10 m: %d | >30 m: %d'
      % (dev[n//2], dev[int(n*0.9)], dev[-1], sum(1 for d in dev if d>10), sum(1 for d in dev if d>30)))
print('контролните точки:', {cp[i]: round(d,1) for i,d in sorted(cpdev.items())})
