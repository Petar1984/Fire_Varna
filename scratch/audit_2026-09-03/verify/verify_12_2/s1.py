# -*- coding: utf-8 -*-
"""READ-ONLY: reproduce finding 12 numbers and join entrance index <-> geocoder <-> delivery."""
import json, sys, collections, math
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"
FV=r"C:/git/Fire_Varna/data"

EN=json.load(open(VB+"/search_index_entrances.json",encoding="utf-8"))
G=json.load(open(VB+"/geocoder_index.json",encoding="utf-8"))
SI=json.load(open(FV+"/search_index.json",encoding="utf-8"))

ids=list(EN["documentIds"].values())
sf=EN["storedFields"]
en_recs=[]
for k,v in sf.items():
    en_recs.append(v)
print("EN documentCount",EN["documentCount"],"storedFields",len(sf),"ids",len(ids),"unique ids",len(set(ids)))
print("EN has lat/lng in stored:",all(("lat" in r and "lng" in r) for r in en_recs))
en_keys=collections.Counter((r["building_cadnum"],r["entrance"]) for r in en_recs)
print("EN unique (cadnum,entrance):",len(en_keys),"dups:",sum(1 for v in en_keys.values() if v>1))
en_bldg=collections.Counter(r["building_cadnum"] for r in en_recs)
print("EN distinct building_cadnum:",len(en_bldg))

GE=G["entries"]
gent=[e for e in GE if e.get("en") is not None]
print("geocoder entries",len(GE),"with en",len(gent))
g_keys_cad=collections.Counter((e["cadnum"],e["en"]) for e in gent)
g_keys_sec=collections.Counter((e.get("section_cadnum") or e["cadnum"],e["en"]) for e in gent)
print("geocoder unique (cadnum,en):",len(g_keys_cad),"(section_cadnum,en):",len(g_keys_sec))

setEN=set(en_keys); setG=set(g_keys_cad); setGs=set(g_keys_sec)
print("EN∩G(cadnum):",len(setEN&setG),"EN-only:",len(setEN-setG),"G-only:",len(setG-setEN))
print("EN∩G(section):",len(setEN&setGs),"EN-only:",len(setEN-setGs),"G-only:",len(setGs-setEN))

# delivered
E=SI["entries"]
dent=[e for e in E if e.get("en") is not None]
print("delivered entries",len(E),"with en",len(dent))
print("delivered distinct g:",len({e.get("g") for e in dent}))
print("delivered distinct (g,en):",len({(e.get("g"),str(e["en"])) for e in dent}))
json.dump({"en_only_keys":sorted([f"{a}:{b}" for a,b in (setEN-setG)])[:50]},open("s1_sample.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
