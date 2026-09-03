# -*- coding: utf-8 -*-
import json,sys,collections
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"
EN=json.load(open(VB+"/search_index_entrances.json",encoding="utf-8"))
SU=json.load(open(VB+"/section_units.json",encoding="utf-8"))
recs=list(EN["storedFields"].values())
su_by_cad={}
for u in SU:
    su_by_cad[u["section_cadnum"]]=u
su_keys=set()
for u in SU:
    for e in (u.get("entrances") or []):
        if e and e.get("en") not in (None,""): su_keys.add((u["section_cadnum"],str(e["en"])))
missing=[r for r in recs if (r["building_cadnum"],str(r["entrance"])) not in su_keys]
print("EN docs absent from section_units:",len(missing))
# how many of their sections exist in section_units at all
insu=[r for r in missing if r["building_cadnum"] in su_by_cad]
print("  of which section exists in section_units:",len(insu),
      "| section NOT in section_units:",len(missing)-len(insu))
noent=[r for r in insu if not (su_by_cad[r["building_cadnum"]].get("entrances") or [])]
print("  section exists but has ZERO entrances in section_units:",len(noent),
      "over",len({r['building_cadnum'] for r in noent}),"sections")
# unit_count distribution of the missing docs
uc=[r.get("unit_count") or 0 for r in missing]
print("  missing docs unit_count: sum",sum(uc),"median",sorted(uc)[len(uc)//2],"max",max(uc))
print("  missing docs with unit_count==0:",sum(1 for x in uc if x==0))
# examples
ex=sorted(missing,key=lambda r:-(r.get("unit_count") or 0))[:8]
for r in ex:
    u=su_by_cad.get(r["building_cadnum"])
    print("   ",r["building_cadnum"],r["entrance"],"units",r["unit_count"],
          "| SU label:",(u or {}).get("label"),"| SU entrances:",len((u or {}).get("entrances") or []))
