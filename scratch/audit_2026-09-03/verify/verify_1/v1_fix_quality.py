# -*- coding: utf-8 -*-
"""Какво КАЧЕСТВО има „готовата кирилица" на пина на всеки латински етикет."""
import json, collections, sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
FV="C:/git/Fire_Varna/"
si=json.load(open(FV+"data/search_index.json",encoding="utf-8")); E=si["entries"]; DN=si["district_names"]
p=json.load(open(FV+"data/address_rows.json",encoding="utf-8")); o=p["field_order"]
NA=o.index("normalized_address"); LA=o.index("lat"); LN=o.index("lng"); rows=p["rows"]
CYR=set("абвгдежзийклмнопрстуфхцчшщъьюя"); LAT=set("abcdefghijklmnopqrstuvwxyz")
def cls(s):
    t=s.lower(); c=any(ch in CYR for ch in t); l=any(ch in LAT for ch in t)
    return "mixed" if (c and l) else "cyr" if c else "lat" if l else "none"
def pretty(s): return " ".join(str(s).replace("|"," ").split())
def base(e):
    if e.get("label") is not None: return pretty(e["label"])
    if e.get("display_id") is not None: return rows[e["display_id"]][NA]
    if e.get("d") is not None: return DN[e["d"]]
    return "(адрес)"
rowpin=collections.defaultdict(list)
for i,r in enumerate(rows):
    if r[NA]: rowpin[(round(r[LA],5),round(r[LN],5))].append(i)
def words(s): return sum(1 for w in s.split() if any(ch in CYR for ch in w.lower()))
stat=collections.Counter(); ex=collections.defaultdict(list)
for e in E:
    b=base(e)
    if cls(b)!="lat": continue
    pin=e.get("pin"); ids=rowpin.get((round(pin[0],5),round(pin[1],5)),[]) if pin else []
    cands=[rows[i][NA] for i in ids]
    if not cands: stat["няма кандидат"]+=1; ex["няма кандидат"].append((b,None)); continue
    best=max(cands,key=lambda s:(words(s),len(s)))
    if words(best)==0: k="кандидатът е САМО число"
    elif words(best)==1: k="кандидатът е 1 дума"
    else: k="кандидатът е >=2 думи"
    stat[k]+=1
    if len(ex[k])<8: ex[k].append((b,best))
for k,v in stat.most_common():
    print("%-26s %6d  (%.1f%%)" % (k,v,100.0*v/31916))
    for a,c in ex[k][:5]: print("      %-32s -> %r" % (a,c))
