# -*- coding: utf-8 -*-
import json, io, sys, math
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
INFO=r'C:\git\varna_3d\web\varna_buildings_info.json'
GJ=r'C:\git\varna_3d\web\varna_buildings_3d.geojson'
inf=json.load(io.open(INFO,encoding='utf-8'))
C=inf['columns']; DIC=inf['dict']; R=inf['rows']
si=C.index('street'); ni=C.index('num'); fi=C.index('func')
STR=DIC['street']; NUM=DIC.get('num'); FUN=DIC['func']
def val(col,v):
    return DIC[col][v] if (col in DIC and isinstance(v,int) and 0<=v<len(DIC[col])) else v
hits=[]
for i,row in enumerate(R):
    s=val('street',row[si])
    if isinstance(s,str) and 'МАНУШ' in s.upper():
        hits.append((i, s, val('num',row[ni]), val('func',row[fi])))
print('Мануш войвода сгради:', len(hits))
for h in hits[:40]: print(' ', h)
# centroids
g=json.load(io.open(GJ,encoding='utf-8'))
cen={}
for f in g['features']:
    i=f['properties'].get('i')
    if i is None: continue
    if i not in [h[0] for h in hits] and i not in (1523,):
        continue
    xs=[];ys=[]
    def walk(c):
        if isinstance(c[0],(int,float)): xs.append(c[0]); ys.append(c[1])
        else:
            for k in c: walk(k)
    walk(f['geometry']['coordinates'])
    cen[i]=(sum(ys)/len(ys), sum(xs)/len(xs))
def hav(a,b,c,d):
    Rr=6371000.0
    p1=math.radians(a);p2=math.radians(c)
    dp=math.radians(c-a);dl=math.radians(d-b)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*Rr*math.asin(math.sqrt(h))
D=(43.209744,27.890788)
print('\nдиспансерният пин', D)
for h in hits:
    i=h[0]
    if i in cen:
        print('  i=%-6d %-22s %-6s %-40s %8.1f m' % (i,h[1],str(h[2]),h[3][:40], hav(D[0],D[1],cen[i][0],cen[i][1])))
