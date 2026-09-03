# -*- coding: utf-8 -*-
import json,sys,collections
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"
S=json.load(open(VB+"/strategic_intel.json",encoding="utf-8"))
print("source_data_date",S.get("source_data_date"),"schema",S.get("schema_version"))
print("counts",json.dumps(S.get("counts"),ensure_ascii=False)[:400])
bi=S["building_intel"]
print("building_intel type",type(bi),"len",len(bi))
k0=list(bi.keys())[0] if isinstance(bi,dict) else None
print("sample",json.dumps(bi[k0] if k0 else bi[0],ensure_ascii=False)[:500])
