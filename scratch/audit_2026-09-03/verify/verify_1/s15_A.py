import json, collections, re, sys, io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
VB="C:/git/Varna_buildings"
EN=json.load(open(VB+"/output/search_index_entrances.json",encoding="utf-8"))
G=json.load(open(VB+"/output/geocoder_index.json",encoding="utf-8"))
U=json.load(open(VB+"/output/section_units.json",encoding="utf-8"))
gen=[e for e in G["entries"] if e.get("en")]
LAT2CYR=str.maketrans("ABEKMHOPCTYXaebkmhopctyx","АВЕКМНОРСТУХАЕВКМНОРСТУХ")
norm=lambda s: s.strip().upper().translate(LAT2CYR)
gk={(e["section_cadnum"],norm(e["en"])) for e in gen}
docs=[EN["storedFields"][k] for k in EN["storedFields"]]
miss=[sf for sf in docs if (sf["building_cadnum"],norm(sf["entrance"])) not in gk]
COMP=re.compile(r"[,\-+/\s\"]|ТЯЛО|СЕКЦИЯ")
clean=[s for s in miss if not (COMP.search(norm(s["entrance"])) or len(norm(s["entrance"]))>2)]
u_cad={u["section_cadnum"] for u in U}
A=[s for s in clean if s["building_cadnum"] not in u_cad]
print("class A rows:",len(A),"buildings:",len({s['building_cadnum'] for s in A}),"units:",sum(s['unit_count'] for s in A))
# what kind are those buildings in the geocoder?
kind_by={}
for e in G["entries"]:
    for k in ("cadnum","section_cadnum"):
        if e.get(k): kind_by.setdefault(e[k],set()).add(e["kind"])
print("kinds of class-A buildings:", collections.Counter(frozenset(kind_by.get(s['building_cadnum'],set())) for s in A))
D=[s for s in clean if s["building_cadnum"] in u_cad]
print("class B/D rows:",len(D),"buildings:",len({s['building_cadnum'] for s in D}),"units:",sum(s['unit_count'] for s in D))
top=sorted(A,key=lambda s:-s["unit_count"])[:10]
for t in top: print("  A:",t["building_cadnum"],t["entrance"],"units",t["unit_count"],t["lat"],t["lng"])
top=sorted(D,key=lambda s:-s["unit_count"])[:10]
for t in top: print("  D:",t["building_cadnum"],t["entrance"],"units",t["unit_count"],t["lat"],t["lng"])
