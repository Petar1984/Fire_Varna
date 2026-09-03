# -*- coding: utf-8 -*-
"""PIP: в коя КАИС сграда пада всеки пин. Чете само; нищо не пише в C:/git."""
import json, io, sys, math
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
GJ = r'C:\git\varna_3d\web\varna_buildings_3d.geojson'
INFO = r'C:\git\varna_3d\web\varna_buildings_info.json'
g=json.load(io.open(GJ,encoding='utf-8'))
feats=g['features']
print('features', len(feats))
inf=json.load(io.open(INFO,encoding='utf-8'))
C=inf['columns']; DIC=inf['dict']; R=inf['rows']
def rec(i):
    o=dict(zip(C,R[i])); out={}
    for k,v in o.items():
        out[k]=DIC[k][v] if (k in DIC and isinstance(v,int) and 0<=v<len(DIC[k])) else v
    return out
# index features by i
byi={}
for f in feats:
    i=f['properties'].get('i')
    if i is not None: byi[i]=f
print('with i', len(byi))

def rings(geom):
    t=geom['type']; c=geom['coordinates']
    if t=='Polygon': return [c]
    if t=='MultiPolygon': return c
    return []
def pip(pt, geom):
    x,y=pt
    for poly in rings(geom):
        ring=poly[0]
        inside=False
        n=len(ring)
        for a in range(n):
            x1,y1=ring[a][0],ring[a][1]; x2,y2=ring[(a+1)%n][0],ring[(a+1)%n][1]
            if ((y1>y)!=(y2>y)) and (x < (x2-x1)*(y-y1)/(y2-y1)+x1):
                inside = not inside
        if inside:
            # holes
            hole=False
            for h in poly[1:]:
                ins=False; n2=len(h)
                for a in range(n2):
                    x1,y1=h[a][0],h[a][1]; x2,y2=h[(a+1)%n2][0],h[(a+1)%n2][1]
                    if ((y1>y)!=(y2>y)) and (x < (x2-x1)*(y-y1)/(y2-y1)+x1):
                        ins = not ins
                if ins: hole=True
            if not hole: return True
    return False

def bbox(geom):
    xs=[];ys=[]
    for poly in rings(geom):
        for ring in poly:
            for p in ring: xs.append(p[0]); ys.append(p[1])
    return min(xs),min(ys),max(xs),max(ys)

BB={i:bbox(f['geometry']) for i,f in byi.items()}

def which(lat,lon):
    hits=[]
    for i,(x0,y0,x1,y1) in BB.items():
        if x0-1e-6<=lon<=x1+1e-6 and y0-1e-6<=lat<=y1+1e-6:
            if pip((lon,lat), byi[i]['geometry']): hits.append(i)
    return hits

def hav(a,b,c,d):
    R=6371000.0
    p1=math.radians(a);p2=math.radians(c)
    dp=math.radians(c-a);dl=math.radians(d-b)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(h))

TARGETS=[
 ("Диспансер за белодробни заболявания (доставка, ДКЦ)", 43.209744, 27.890788),
 ("ДГ№52 „Бялата лястовица“ (регистър)", 43.209723, 27.890771),
 ("Аджибадем Сити Клиник (доставка, болница)", 43.217378, 27.916067),
 ("Медицински комплекс „Майчин дом“ (доставка, болница)", 43.220199, 27.9265),
]
for nm,lat,lon in TARGETS:
    h=which(lat,lon)
    print('\n==', nm, lat, lon)
    print('   PIP hits:', h)
    for i in h:
        print('   i=%d'%i, json.dumps(rec(i), ensure_ascii=False))
print('\n-- разстояние диспансер↔ДГ52: %.2f m' % hav(43.209744,27.890788,43.209723,27.890771))
print('\n-- i=1522 --', json.dumps(rec(1522), ensure_ascii=False))
print('-- i=1523 --', json.dumps(rec(1523), ensure_ascii=False))
