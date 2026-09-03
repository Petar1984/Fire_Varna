# -*- coding: utf-8 -*-
import json,sys,collections
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"
EN=json.load(open(VB+"/search_index_entrances.json",encoding="utf-8"))
G=json.load(open(VB+"/geocoder_index.json",encoding="utf-8"))
recs=list(EN["storedFields"].values())
gent=[e for e in G["entries"] if e.get("en") is not None]
gkeys={(e["cadnum"],e["en"]) for e in gent}
gcad_ent={e["cadnum"] for e in gent}
all_gcad={e.get("cadnum") for e in G["entries"] if e.get("cadnum")}
all_gsec={e.get("section_cadnum") for e in G["entries"] if e.get("section_cadnum")}

en_cad={r["building_cadnum"] for r in recs}
print("EN sections:",len(en_cad),"| geocoder sections WITH entrance entries:",len(gcad_ent))
print("EN sections missing from geocoder-entrance set:",len(en_cad-gcad_ent))
print("geocoder-entrance sections missing from EN:",len(gcad_ent-en_cad))
print("EN sections absent from geocoder ENTIRELY (any entry cadnum):",len(en_cad-all_gcad))
print("EN sections absent from geocoder (cadnum or section_cadnum):",len(en_cad-(all_gcad|all_gsec)))

missing=[r for r in recs if (r["building_cadnum"],r["entrance"]) not in gkeys]
print("EN docs whose (cadnum,entrance) is missing in geocoder:",len(missing))
extra=[k for k in gkeys if (k[0],k[1]) not in {(r["building_cadnum"],r["entrance"]) for r in recs}]
print("geocoder entrance keys not in EN:",len(extra))
print("net =",len(missing)-len(extra))

# classify missing: section entirely absent vs section present but no entrance entry
m_abs=[r for r in missing if r["building_cadnum"] not in (all_gcad|all_gsec)]
m_pres_noent=[r for r in missing if r["building_cadnum"] in (all_gcad|all_gsec) and r["building_cadnum"] not in gcad_ent]
m_pres_partial=[r for r in missing if r["building_cadnum"] in gcad_ent]
print("  (a) section absent from geocoder entirely:",len(m_abs),"over",len({r['building_cadnum'] for r in m_abs}),"sections")
print("  (b) section present in geocoder but NO entrance entries at all:",len(m_pres_noent),"over",len({r['building_cadnum'] for r in m_pres_noent}),"sections")
print("  (c) section HAS entrance entries but this letter missing:",len(m_pres_partial),"over",len({r['building_cadnum'] for r in m_pres_partial}),"sections")
json.dump({"a":[f"{r['building_cadnum']}:{r['entrance']}" for r in m_abs][:40],
           "b":[f"{r['building_cadnum']}:{r['entrance']}" for r in m_pres_noent][:40],
           "c":[f"{r['building_cadnum']}:{r['entrance']}" for r in m_pres_partial][:40],
           "extra_in_geocoder":[f"{a}:{b}" for a,b in sorted(extra)][:60]},
          open("s4_samples.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
