# -*- coding: utf-8 -*-
import json,sys,collections
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"; FV=r"C:/git/Fire_Varna/data"
G=json.load(open(VB+"/geocoder_index.json",encoding="utf-8"))
SI=json.load(open(FV+"/search_index.json",encoding="utf-8"))
print("SI keys",list(SI.keys()))
E=SI["entries"]
dent=[e for e in E if e.get("en") is not None]
print("delivered entrance sample:",json.dumps(dent[0],ensure_ascii=False)[:400])
pbr=G.get("physical_building_reps")
print("pbr type",type(pbr),"len",len(pbr) if pbr is not None else None)
if isinstance(pbr,list): print("pbr sample",json.dumps(pbr[:3],ensure_ascii=False)[:400])
elif isinstance(pbr,dict):
    k=list(pbr.keys())[:3]
    for kk in k: print("pbr",kk,json.dumps(pbr[kk],ensure_ascii=False)[:300])
# distinct g among ALL delivered entries
print("delivered distinct g over all entries:",len({e.get('g') for e in E if e.get('g') is not None}))
gc=collections.Counter(e.get('g') for e in dent)
print("top g by entrance count:",gc.most_common(5))
