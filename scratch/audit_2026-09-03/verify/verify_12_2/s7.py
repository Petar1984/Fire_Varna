# -*- coding: utf-8 -*-
import json,sys,collections
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"
SI=json.load(open(VB+"/strategic_intel.json",encoding="utf-8"))
print("type",type(SI))
if isinstance(SI,dict): print("keys",list(SI.keys())[:20])
elif isinstance(SI,list): print("len",len(SI),"sample keys",list(SI[0].keys())[:30])
