# -*- coding: utf-8 -*-
import json,sys,collections
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"
EN=json.load(open(VB+"/search_index_entrances.json",encoding="utf-8"))
SU=json.load(open(VB+"/section_units.json",encoding="utf-8"))
G=json.load(open(VB+"/geocoder_index.json",encoding="utf-8"))
recs=list(EN["storedFields"].values())
LAT2CYR=str.maketrans({"A":"А","B":"В","E":"Е","K":"К","M":"М","H":"Н","O":"О","P":"Р","C":"С","T":"Т","X":"Х","Y":"У",
                       "a":"а","b":"в","e":"е","k":"к","m":"м","o":"о","p":"р","c":"с","t":"т","x":"х","y":"у"})
def fold(s): return str(s).strip().upper().translate(LAT2CYR)
su_ent=collections.defaultdict(set); su_cad=set(); su_lab={}
for u in SU:
    su_cad.add(u["section_cadnum"]); su_lab[u["section_cadnum"]]=u.get("label")
    for e in (u.get("entrances") or []):
        if e and e.get("en") not in (None,""): su_ent[u["section_cadnum"]].add(fold(e["en"]))
still=[r for r in recs if fold(r["entrance"]) not in su_ent.get(r["building_cadnum"],set())]
a=[r for r in still if r["building_cadnum"] in su_cad]
b=[r for r in still if r["building_cadnum"] not in su_cad]
print("A) section present in section_units, this entrance missing:",len(a),"over",len({r['building_cadnum'] for r in a}),"sections")
print("   of these sections, HOW MANY still have >=1 entrance delivered:",
      len({r['building_cadnum'] for r in a if su_ent.get(r['building_cadnum'])}),
      "| ZERO entrances:",len({r['building_cadnum'] for r in a if not su_ent.get(r['building_cadnum'])}))
print("   units behind A:",sum(r.get('unit_count') or 0 for r in a))
print("B) section absent from section_units entirely:",len(b),"over",len({r['building_cadnum'] for r in b}),"sections")
print("   units behind B:",sum(r.get('unit_count') or 0 for r in b))
# are B sections present anywhere in the geocoder (as address/mf rows)?
gcad={e.get("cadnum") for e in G["entries"] if e.get("cadnum")}
gsec={e.get("section_cadnum") for e in G["entries"] if e.get("section_cadnum")}
bcads={r["building_cadnum"] for r in b}
print("   B sections present in geocoder anyway (any row):",len(bcads&(gcad|gsec)),"of",len(bcads))
acads={r["building_cadnum"] for r in a}
print("   A sections present in geocoder (any row):",len(acads&(gcad|gsec)),"of",len(acads))
