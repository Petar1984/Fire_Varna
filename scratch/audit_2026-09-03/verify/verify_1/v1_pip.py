# -*- coding: utf-8 -*-
"""Пада ли изключеният OSM пин ВЪТРЕ в КАИС сграда? (точка-в-полигон, без библиотеки)"""
import json,sys,math
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
V3="C:/git/varna_3d/"
gj=json.load(open(V3+"web/varna_buildings_3d.geojson",encoding="utf-8"))
info=json.load(open(V3+"web/varna_buildings_info.json",encoding="utf-8"))
ci={c:i for i,c in enumerate(info["columns"])}; D=info["dict"]
def func(i):
    r=info["rows"][i]; return D["func"][r[ci["func"]]] if r[ci["func"]]>=0 else ""
TEST=[("Калина Малина (ДГ№21)",43.217605,27.938426,56375),
      ("Слънчева дъга (ДГ№16)",43.218227,27.921423,55414),
      ("ЦДГ Незабравка (ДГ№11)",43.225183,27.919848,50086),
      ("Теменужка (ДГ№4)",43.204379,27.914376,-1)]
def inring(x,y,ring):
    ins=False; n=len(ring)
    for a in range(n):
        x1,y1=ring[a][0],ring[a][1]; x2,y2=ring[(a+1)%n][0],ring[(a+1)%n][1]
        if (y1>y)!=(y2>y):
            xi=x1+(y-y1)*(x2-x1)/(y2-y1)
            if x<xi: ins=not ins
    return ins
def hav(a,b,c,d):
    R=6371000.0;p1,p2=math.radians(a),math.radians(c)
    return 2*R*math.asin(math.sqrt(math.sin((p2-p1)/2)**2+math.cos(p1)*math.cos(p2)*math.sin(math.radians(d-b)/2)**2))
hits={t[0]:[] for t in TEST}
mind={t[0]:(9e9,None) for t in TEST}
for ft in gj["features"]:
    g=ft["geometry"]; i=ft["properties"].get("i")
    polys=[g["coordinates"]] if g["type"]=="Polygon" else g["coordinates"]
    for poly in polys:
        ring=poly[0]
        lons=[c[0] for c in ring]; lats=[c[1] for c in ring]
        for nm,la,lo,decl in TEST:
            if min(lons)-0.0006<lo<max(lons)+0.0006 and min(lats)-0.0006<la<max(lats)+0.0006:
                cl=min(hav(la,lo,c[1],c[0]) for c in ring)
                if cl<mind[nm][0]: mind[nm]=(cl,i)
                if inring(lo,la,ring): hits[nm].append(i)
for nm,la,lo,decl in TEST:
    h=sorted(set(hits[nm]))
    print(f"{nm:26s} · деклариран i={decl:6d} · ВЪТРЕ в сгради: {h if h else 'НИКОЯ'}"
          f" · най-близък ръб {mind[nm][0]:.1f} m (i={mind[nm][1]})"
          + (f" · func(i={decl})={func(decl)!r}" if decl>=0 else ""))
