# -*- coding: utf-8 -*-
import json, collections, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
FV = "C:/git/Fire_Varna/"
si = json.load(open(FV+"data/search_index.json", encoding="utf-8"))
E = si["entries"]; DN = si["district_names"]
p = json.load(open(FV+"data/address_rows.json", encoding="utf-8"))
o = p["field_order"]; NA=o.index("normalized_address"); LA=o.index("lat"); LN=o.index("lng")
rows = p["rows"]
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
def shown(e):
    b=base(e)
    return b+" · вх. "+str(e["en"]) if (e.get("kind")=="mf" and e.get("en") is not None) else b

# 1) пинове с ДВЕТЕ азбуки едновременно
bypin=collections.defaultdict(set)
for e in E:
    pin=e.get("pin")
    if not pin: continue
    bypin[(round(pin[0],5),round(pin[1],5))].add(cls(shown(e)))
both=[k for k,v in bypin.items() if "lat" in v and "cyr" in v]
print("пинове общо              =", len(bypin))
print("пинове с lat И cyr       =", len(both))
bothx=[k for k,v in bypin.items() if ("lat" in v or "mixed" in v) and ("cyr" in v or "mixed" in v)]
print("пинове с lat|mixed И cyr =", len(bothx))
for k in sorted(both)[:6]:
    labs=sorted({shown(e) for e in E if e.get("pin") and (round(e["pin"][0],5),round(e["pin"][1],5))==k})
    print("  ",k,labs[:6])

# 2) примерите от черновата
ex=["atanas dalchev 1","prof d r vladimir vasilev 2","kap petko voivoda 14","iuzhen zaliv 4","kozlodui 14"]
S=[shown(e) for e in E]
first_lat=next((i for i,s in enumerate(S) if cls(s)=="lat"), None)
print("първи запис в индекса    =", repr(S[0]), "| pin", E[0].get("pin"))
print("първи ЛАТИНСКИ запис     =", repr(S[first_lat]), "| pin", E[first_lat].get("pin"))
for q in ex:
    hits=[(s,e.get("pin")) for s,e in zip(S,E) if s==q]
    print("  %-28s -> %d записа, пин %s" % (q, len(hits), hits[0][1] if hits else None))

# 3) има ли кирилски дубльор по КООРДИНАТА за латинските етикети?
rowpin=collections.defaultdict(list)
for r in rows:
    if r[NA]: rowpin[(round(r[LA],5),round(r[LN],5))].append(r[NA])
lat_e=[e for e,s in zip(E,S) if cls(s)=="lat"]
hit=sum(1 for e in lat_e if e.get("pin") and (round(e["pin"][0],5),round(e["pin"][1],5)) in rowpin)
print("латински записи          =", len(lat_e))
print("  от тях с кирилски ред на СЪЩИЯ пин =", hit, "(%.1f%%)" % (100.0*hit/len(lat_e)))
mix_e=[e for e,s in zip(E,S) if cls(s)=="mixed"]
hitm=sum(1 for e in mix_e if e.get("pin") and (round(e["pin"][0],5),round(e["pin"][1],5)) in rowpin)
print("смесени записи           =", len(mix_e), "| с кирилски ред на същия пин =", hitm)
