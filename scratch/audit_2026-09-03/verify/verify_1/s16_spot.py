import json, collections, sys, io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
VB="C:/git/Varna_buildings"
U=json.load(open(VB+"/output/section_units.json",encoding="utf-8"))
AI=json.load(open(VB+"/output/address_index.json",encoding="utf-8"))
ai={r[4]:r for r in AI}
ucad={u["section_cadnum"] for u in U}
for c in ["10135.xxxx","10135.xxxx","10135.xxxx","10135.xxxx","10135.xxxx","10135.xxxx"]:
    r=ai.get(c)
    print(c, "| in section_units:", c in ucad, "| functype:", r[3] if r else None, "| addr:", (r[0] if r else None))
# functype distribution of class-A buildings
EN=json.load(open(VB+"/output/search_index_entrances.json",encoding="utf-8"))
G=json.load(open(VB+"/output/geocoder_index.json",encoding="utf-8"))
gen=[e for e in G["entries"] if e.get("en")]
LAT2CYR=str.maketrans("ABEKMHOPCTYXaebkmhopctyx","АВЕКМНОРСТУХАЕВКМНОРСТУХ")
norm=lambda s: s.strip().upper().translate(LAT2CYR)
gk={(e["section_cadnum"],norm(e["en"])) for e in gen}
docs=[EN["storedFields"][k] for k in EN["storedFields"]]
import re
COMP=re.compile(r"[,\-+/\s\"]|ТЯЛО|СЕКЦИЯ")
miss=[s for s in docs if (s["building_cadnum"],norm(s["entrance"])) not in gk]
clean=[s for s in miss if not (COMP.search(norm(s["entrance"])) or len(norm(s["entrance"]))>2)]
A={s["building_cadnum"] for s in clean if s["building_cadnum"] not in ucad}
print("\nfunctype of the 120 class-A buildings:")
for k,v in collections.Counter(ai[c][3] for c in A if c in ai).most_common(): print("  ",v,k)
