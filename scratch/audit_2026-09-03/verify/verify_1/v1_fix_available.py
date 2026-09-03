# -*- coding: utf-8 -*-
"""Има ли ГОТОВ кирилски низ за всеки латински етикет (т.е. вреден ли е „преводът")."""
import json, collections, sys, io
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
used=set(e["display_id"] for e in E if e.get("display_id") is not None)
print("address_rows общо        =", len(rows))
print("реферирани от entries    =", len(used))
print("НЕреферирани             =", len(rows)-len(used))
rowpin=collections.defaultdict(list)
for i,r in enumerate(rows):
    if r[NA]: rowpin[(round(r[LA],5),round(r[LN],5))].append(i)
lat=[e for e in E if cls(base(e))=="lat"]
free=0; onlyused=0; none=0
for e in lat:
    pin=e.get("pin")
    ids=rowpin.get((round(pin[0],5),round(pin[1],5)),[]) if pin else []
    if not ids: none+=1
    elif any(i not in used for i in ids): free+=1
    else: onlyused+=1
print("латински записи          =", len(lat))
print("  кирилски ред на пина, СВОБОДЕН   =", free)
print("  кирилски ред на пина, вече зает  =", onlyused)
print("  без кирилски ред на пина         =", none)
# примери на двойката (латиница -> наличната кирилица)
n=0
for e in lat:
    pin=e.get("pin")
    ids=rowpin.get((round(pin[0],5),round(pin[1],5)),[]) if pin else []
    if ids:
        print("   %-34s -> %s" % (base(e), rows[ids[0]][NA]))
        n+=1
        if n>=12: break
