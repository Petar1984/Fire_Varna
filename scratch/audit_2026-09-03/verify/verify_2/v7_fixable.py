# -*- coding: utf-8 -*-
"""Колко от ЛАТИНСКИТЕ редове на Fire_Varna имат готов кирилски низ в доставения
   data/address_rows.json (свързване Fire_Varna→geocoder_index по pin+addr_key→cadnum
   →address_index ред). Ако е висок процент — поправката е ВРЪЗКА, не превод."""
import json, re, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
FV="C:/git/Fire_Varna/"; VB="C:/git/Varna_buildings/output/"
si=json.load(open(FV+"data/search_index.json",encoding="utf-8")); E=si["entries"]
gi=json.load(open(VB+"geocoder_index.json",encoding="utf-8"))["entries"]
ai=json.load(open(VB+"address_index.json",encoding="utf-8"))
row_of={}                     # cadnum -> (index, normalized_address)
for k,r in enumerate(ai): row_of[r[4]]=(k,r[0])
gmap=collections.defaultdict(list)
for e in gi: gmap[(round(e["pin"][0],5),round(e["pin"][1],5),e.get("kind"))].append(e)

WS=re.compile(r"\s+")
def pretty(s): return WS.sub(" ",str(s).replace("|"," ")).strip()
CYR=set("абвгдежзийклмнопрстуфхцчшщъьюя")
def al(s):
    t=str(s).lower(); c=any(ch in CYR for ch in t); l=any(ch in "abcdefghijklmnopqrstuvwxyz" for ch in t)
    return "mixed" if c and l else "cyr" if c else "lat" if l else "none"

st=collections.Counter(); ex=[]
for e in E:
    lab=e.get("label")
    if not lab: continue
    s=pretty(lab)
    if al(s) not in ("lat","mixed"): continue
    st["латински/смесени редове"]+=1
    key=(round(e["pin"][0],5),round(e["pin"][1],5),e.get("kind"))
    cands=[g for g in gmap.get(key,[]) if (g.get("addr_key") or "")==lab or pretty(g.get("addr_key") or "")==s]
    if not cands: cands=gmap.get(key,[])
    if not cands: st["без съответствие в geocoder_index"]+=1; continue
    g=cands[0]; rc=row_of.get(g.get("cadnum"))
    if not rc: st["cadnum няма ред в address_index"]+=1; continue
    k,na=rc
    if al(na)=="cyr" and any(ch.isalpha() for ch in na):
        st["ГОТОВ кирилски ред (само липсва display_id)"]+=1
        if len(ex)<10: ex.append((s,"→",na))
    elif not any(ch.isalpha() for ch in str(na)): st["редът е само число"]+=1
    else: st["редът не е кирилски"]+=1
tot=st["латински/смесени редове"]
for k,v in st.most_common(): print("%-42s %6d  %5.1f%%"%(k,v,100.0*v/tot))
print("\nпримери (какво вижда сега → какво вече лежи в address_rows.json):")
for x in ex: print("   ",x)
