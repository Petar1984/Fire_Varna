# -*- coding: utf-8 -*-
import json,sys,collections
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"
SU=json.load(open(VB+"/section_units.json",encoding="utf-8"))
print("records",len(SU))
print("sample keys",list(SU[0].keys()))
print("sample",json.dumps(SU[0],ensure_ascii=False)[:600])
tot=0; keys=set(); withpin=0
for u in SU:
    for e in (u.get("entrances") or []):
        if e is None or e.get("en") in (None,""): continue
        tot+=1
        keys.add((u.get("cadnum") or u.get("section_cadnum"), str(e["en"])))
        if e.get("lat") is not None: withpin+=1
print("section_units entrance rows (en non-empty):",tot,"unique (cadnum,en):",len(keys),"with lat:",withpin)
EN=json.load(open(VB+"/search_index_entrances.json",encoding="utf-8"))
enk={(r["building_cadnum"],str(r["entrance"])) for r in EN["storedFields"].values()}
G=json.load(open(VB+"/geocoder_index.json",encoding="utf-8"))
gk={(e["cadnum"],str(e["en"])) for e in G["entries"] if e.get("en") is not None}
print("SU∩G",len(keys&gk),"SU-only",len(keys-gk),"G-only",len(gk-keys))
print("SU∩EN",len(keys&enk),"SU-only vs EN",len(keys-enk),"EN-only vs SU",len(enk-keys))
json.dump({"su_only_vs_en":sorted(f"{a}:{b}" for a,b in (keys-enk))[:40],
           "en_only_vs_su":sorted(f"{a}:{b}" for a,b in (enk-keys))[:40]},
          open("s6_samples.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
