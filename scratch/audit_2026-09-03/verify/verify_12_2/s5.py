# -*- coding: utf-8 -*-
import json,sys,collections
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"
SU=json.load(open(VB+"/section_units.json",encoding="utf-8"))
print("type",type(SU))
if isinstance(SU,dict):
    print("keys",list(SU.keys())[:20])
    for k in list(SU.keys())[:6]:
        v=SU[k]
        print(k,type(v),(len(v) if hasattr(v,'__len__') else v))
