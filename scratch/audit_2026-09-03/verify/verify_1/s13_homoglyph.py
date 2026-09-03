import json, collections, re, sys, io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
VB="C:/git/Varna_buildings"
EN=json.load(open(VB+"/output/search_index_entrances.json",encoding="utf-8"))
G=json.load(open(VB+"/output/geocoder_index.json",encoding="utf-8"))
gen=[e for e in G["entries"] if e.get("en")]
LAT2CYR=str.maketrans("ABEKMHOPCTYXaebkmhopctyx","АВЕКМНОРСТУХАЕВКМНОРСТУХ")
def norm(s):
    return s.strip().upper().translate(LAT2CYR)
gk={(e["section_cadnum"], norm(e["en"])) for e in gen}
docs=[EN["storedFields"][k] for k in EN["storedFields"]]
miss=[sf for sf in docs if (sf["building_cadnum"], norm(sf["entrance"])) not in gk]
print("misses after case+homoglyph fold:", len(miss))
extra_docs={(sf["building_cadnum"], norm(sf["entrance"])) for sf in docs}
extra=[e for e in gen if (e["section_cadnum"], norm(e["en"])) not in extra_docs]
print("geocoder-only after fold:", len(extra))
print("net:", len(miss)-len(extra))
# composite labels
COMP=re.compile(r"[,\-+/\s]|ТЯЛО|СЕКЦИЯ|И$|\"")
comp=[sf for sf in miss if COMP.search(norm(sf["entrance"])) or len(norm(sf["entrance"]))>2]
print("of those, composite/dirty labels (comma, dash, plus, ТЯЛО, СЕКЦИЯ, quotes, len>2):", len(comp))
rest=[sf for sf in miss if sf not in comp]
print("clean single-token misses:", len(rest), "units:", sum(s["unit_count"] for s in rest))
cnt=collections.Counter(norm(s["entrance"]) for s in comp)
print("dirty label sample:", cnt.most_common(15))
json.dump({"miss_fold":len(miss),"extra_fold":len(extra),"composite":len(comp),"clean":len(rest),
           "clean_units":sum(s["unit_count"] for s in rest)}, open("s13.json","w"))
json.dump(sorted(rest,key=lambda s:-s["unit_count"]), open("clean_misses.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
