# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №1 · находка №4 — независима проверка на „7 еднозначни двора".
Собствен прочит на КАИС: центроид = средно по ВСИЧКИ пръстени на полигона
(различно от кеша на измервача, който взима само първия пръстен).
READ-ONLY.
"""
from __future__ import annotations
import json, math, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
V3 = Path("C:/git/varna_3d"); OUT = Path(__file__).resolve().parent
AUD = Path("C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/audit_2026-09-03/места-покритие")

info = json.loads((V3/"web/varna_buildings_info.json").read_text(encoding="utf-8"))
cols = info["columns"]; D = info["dict"]; ci = {c:i for i,c in enumerate(cols)}
fn = D["func"]
kid = [i for i,n in enumerate(fn) if n == "Сграда за детско заведение"]
assert len(kid) == 1, kid
kid = kid[0]
kids = {}
for i,r in enumerate(info["rows"]):
    if r[ci["func"]] == kid:
        kids[i] = {"addr": D["addr"][r[ci["addr"]]] if r[ci["addr"]]>=0 else "",
                   "area": r[ci["area_m2"]]}
print("КАИС сгради с функция „Сграда за детско заведение“:", len(kids))

gj = json.loads((V3/"web/varna_buildings_3d.geojson").read_text(encoding="utf-8"))
print("полигони в geojson:", len(gj["features"]))
for ft in gj["features"]:
    i = ft["properties"].get("i")
    if i not in kids: continue
    g = ft["geometry"]
    rings = g["coordinates"] if g["type"]=="Polygon" else [r for poly in g["coordinates"] for r in poly]
    pts = [c for ring in rings for c in ring]
    kids[i]["lat"] = sum(p[1] for p in pts)/len(pts)
    kids[i]["lon"] = sum(p[0] for p in pts)/len(pts)
kids = {i:v for i,v in kids.items() if "lat" in v}
print("с геометрия:", len(kids))

def hav(a,b,c,d):
    R=6371000.0; p1,p2=math.radians(a),math.radians(c)
    dp=p2-p1; dl=math.radians(d-b)
    x=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(x))

miss = json.loads((AUD/"missing.json").read_text(encoding="utf-8"))["детски градини (общински, ЛИПСВАЩИ)"]
VILLAGE = {48,49,50,51}          # 51 = RAJON_ID 15 = село (виж kimi_obrazovanie.txt:1080/1103)
print()
res = {}
for r in miss:
    g = r.get("geo")
    tag = "СЕЛО" if r["no"] in VILLAGE else "град"
    if not g:
        print(f"ДГ№{r['no']:>2} {tag:5s} — няма геокод"); res[r["no"]]=("няма геокод",0,tag); continue
    la,lo = g["lat"], g["lon"]
    near = sorted(((hav(la,lo,v["lat"],v["lon"]), i) for i,v in kids.items()), key=lambda t:t[0])
    near = [(d,i) for d,i in near if d <= 150]
    # single-link ≤45 m клъстери
    ids=[i for _,i in near]; parent={i:i for i in ids}
    def f(x):
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for a in range(len(ids)):
        for b in range(a+1,len(ids)):
            ia,ib=ids[a],ids[b]
            if hav(kids[ia]["lat"],kids[ia]["lon"],kids[ib]["lat"],kids[ib]["lon"])<=45:
                parent[f(ia)]=f(ib)
    cl={}
    for d,i in near: cl.setdefault(f(i),[]).append((d,i))
    yards=sorted(((min(d for d,_ in v), len(v), [i for _,i in v]) for v in cl.values()))
    within80=[y for y in yards if y[0]<=80]
    if not yards: verd="без сграда ≤150 m"
    elif len(within80)==1: verd=f"ЕДНОЗНАЧНО място ({within80[0][1]} тела, {within80[0][0]:.0f} m)"
    elif len(within80)>1: verd=f"НЕЕДНОЗНАЧНО — {len(within80)} двора ≤80 m"
    else: verd=f"далечно място ({yards[0][0]:.0f} m)"
    res[r["no"]]=(verd,len(yards),tag)
    print(f"ДГ№{r['no']:>2} {tag:5s} · дворове≤150m={len(yards)} · {verd:42s} | {r['name'][:34]}")

print()
from collections import Counter
city=[v for k,v in res.items() if v[2]=="град"]
print("В ГРАДА:", len(city))
print(Counter(v[0].split(" (")[0].split(" —")[0] for v in city))
print("СЕЛА:", len([v for v in res.values() if v[2]=="СЕЛО"]))
json.dump({str(k):v for k,v in res.items()}, open(OUT/"v1_yards.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
