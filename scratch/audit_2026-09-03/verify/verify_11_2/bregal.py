# -*- coding: utf-8 -*-
import json, io, sys, math
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
INFO=r'C:\git\varna_3d\web\varna_buildings_info.json'
GJ=r'C:\git\varna_3d\web\varna_buildings_3d.geojson'
inf=json.load(io.open(INFO,encoding='utf-8'))
C=inf['columns']; DIC=inf['dict']; R=inf['rows']
def val(col,v): return DIC[col][v] if (col in DIC and isinstance(v,int) and 0<=v<len(DIC[col])) else v
si=C.index('street'); ni=C.index('num'); fi=C.index('func'); ai=C.index('addr')
want=[]
for i,row in enumerate(R):
    s=val('street',row[si]); n=str(val('num',row[ni]))
    if isinstance(s,str) and ('БРЕГАЛНИЦА' in s.upper()) and n in ('1','3','5','65'):
        want.append((i,s,n,val('func',row[fi]),val('addr',row[ai])))
    if isinstance(s,str) and ('АЛЕКО КОНСТАНТИНОВ' in s.upper()) and n in ('3','5'):
        want.append((i,s,n,val('func',row[fi]),val('addr',row[ai])))
g=json.load(io.open(GJ,encoding='utf-8'))
ids={w[0] for w in want}
cen={}
for f in g['features']:
    i=f['properties'].get('i')
    if i in ids:
        xs=[];ys=[]
        def walk(c):
            if isinstance(c[0],(int,float)): xs.append(c[0]); ys.append(c[1])
            else:
                for k in c: walk(k)
        walk(f['geometry']['coordinates'])
        cen[i]=(sum(ys)/len(ys), sum(xs)/len(xs))
def hav(a,b,c,d):
    Rr=6371000.0
    p1=math.radians(a);p2=math.radians(c); dp=math.radians(c-a); dl=math.radians(d-b)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*Rr*math.asin(math.sqrt(h))
A=(43.217378,27.916067)
print('Аджибадем пин', A)
for w in sorted(want):
    i=w[0]
    if i in cen:
        print('  i=%-6d %-24s %-4s %-45s %8.1f m' % (i,w[1],w[2],str(w[3])[:45], hav(A[0],A[1],cen[i][0],cen[i][1])))
