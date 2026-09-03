# -*- coding: utf-8 -*-
"""Възстановима ли е кирилицата за латинските записи — по cadnum от address_index."""
import json, collections, sys, re
sys.stdout.reconfigure(encoding="utf-8")
VB="C:/git/Varna_buildings/output/"
gi=json.load(open(VB+"geocoder_index.json",encoding="utf-8"))["entries"]
ai=json.load(open(VB+"address_index.json",encoding="utf-8"))
pv=json.load(open(VB+"address_provenance.json",encoding="utf-8"))
CYR=set("абвгдежзийклмнопрстуфхцчшщъьюя")
def al(s):
    t=str(s or "").lower(); c=any(ch in CYR for ch in t); l=any(ch in "abcdefghijklmnopqrstuvwxyz" for ch in t)
    return "mixed" if c and l else "cyr" if c else "lat" if l else "none"
by_cad={}
for r in ai:
    by_cad.setdefault(r[4], r[0])
print("address_index редове =",len(ai),"; уникални cadnum =",len(by_cad))

lat=[e for e in gi if e.get("addr_key") and al(e["addr_key"]) in ("lat","mixed")]
print("латински/смесен addr_key =",len(lat))
st=collections.Counter(); ex=[]
for e in lat:
    na=by_cad.get(e.get("cadnum"))
    if na is None: st["няма ред в address_index"]+=1; continue
    a=al(na)
    has_letter=any(ch.isalpha() for ch in str(na))
    if a=="cyr" and has_letter: st["кирилски с дума"]+=1; ex.append((e["addr_key"],na)) if len(ex)<8 else None
    elif not has_letter: st["само число"]+=1
    else: st["друго(%s)"%a]+=1
print("\nсъстояние на кирилския ред за латинските записи:")
for k,v in st.most_common(): print("   %-28s %6d  (%.1f%%)"%(k,v,100.0*v/len(lat)))
print("\nпримери (латински addr_key → кирилски address_index):")
for x in ex: print("   ",x)

# комбинирано: кирилица от address_index ИЛИ от alternative_value
n=0
for e in lat:
    na=by_cad.get(e.get("cadnum"))
    ok = na is not None and al(na)=="cyr" and any(ch.isalpha() for ch in str(na))
    if not ok:
        aa=(pv.get(e.get("cadnum")) or {}).get("address_authority") or {}
        alt=aa.get("alternative_value")
        ok = bool(alt) and al(alt)=="cyr"
    if ok: n+=1
print("\nкирилица налична (address_index ИЛИ alternative_value) = %d / %d = %.1f%%"%(n,len(lat),100.0*n/len(lat)))
