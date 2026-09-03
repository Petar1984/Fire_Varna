# -*- coding: utf-8 -*-
import json,sys,collections
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"; FV=r"C:/git/Fire_Varna/data"
G=json.load(open(VB+"/geocoder_index.json",encoding="utf-8"))
D=json.load(open(FV+"/search_index.json",encoding="utf-8"))
gent=[e for e in G["entries"] if e.get("en") is not None]
dent=[e for e in D["entries"] if e.get("en") is not None]
gk=collections.Counter((tuple(e["pin"]),str(e["en"])) for e in gent)
dk=collections.Counter((tuple(e["pin"]),str(e["en"])) for e in dent)
print("geocoder entrance rows",len(gent),"delivered",len(dent))
print("multiset equal (pin,en):", gk==dk)
print("g-only",sum((gk-dk).values()),"d-only",sum((dk-gk).values()))
print("4764/5314 =",round(100*4764/5314,4))
print("4764/4764 =",round(100*4764/4764,2))
# arithmetic of the finding
print("608-58 =",608-58)
