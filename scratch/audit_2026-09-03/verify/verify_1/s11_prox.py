import json, collections, math, sys, io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
VB="C:/git/Varna_buildings"
EN=json.load(open(VB+"/output/search_index_entrances.json",encoding="utf-8"))
G=json.load(open(VB+"/output/geocoder_index.json",encoding="utf-8"))
U=json.load(open(VB+"/output/section_units.json",encoding="utf-8"))
gen=[e for e in G["entries"] if e.get("en")]
gkeys={(e["section_cadnum"],e["en"]) for e in gen}
gkeys_ci={(c,en.strip().upper()) for c,en in gkeys}
docs=[]
for k in EN["storedFields"]:
    sf=EN["storedFields"][k]
    docs.append(sf)
miss=[sf for sf in docs if (sf["building_cadnum"],sf["entrance"]) not in gkeys
      and (sf["building_cadnum"],sf["entrance"].strip().upper()) not in gkeys_ci]
print("folded misses:",len(miss))

# complex map for miss cadnums
comp_by_sec={u["section_cadnum"]:u.get("complex_id") for u in U}
sec_by_comp=collections.defaultdict(list)
for u in U: sec_by_comp[u.get("complex_id")].append(u["section_cadnum"])
g_by_comp_en=collections.defaultdict(set)
for e in gen: g_by_comp_en[(e.get("complex_id"), e["en"].strip().upper())].add(e["section_cadnum"])
same_complex=0
for sf in miss:
    c=comp_by_sec.get(sf["building_cadnum"])
    if c and (c, sf["entrance"].strip().upper()) in g_by_comp_en: same_complex+=1
print("folded misses whose SAME complex already has that entrance letter in geocoder:", same_complex)

# proximity: nearest geocoder entrance with same folded letter
def m(a,b,c,d):
    dx=(c-a)*111320.0; dy=(d-b)*111320.0*math.cos(math.radians(a))
    return math.hypot(dx,dy)
by_letter=collections.defaultdict(list)
for e in gen:
    p=e.get("pin")
    if p: by_letter[e["en"].strip().upper()].append((p[0],p[1]))
buckets=collections.Counter(); worst=[]
for sf in miss:
    L=sf["entrance"].strip().upper()
    cands=by_letter.get(L,[])
    best=min((m(sf["lat"],sf["lng"],la,ln) for la,ln in cands), default=None)
    if best is None: buckets["no such letter anywhere"]+=1; continue
    b = "<=15m" if best<=15 else "<=30m" if best<=30 else "<=60m" if best<=60 else ">60m"
    buckets[b]+=1
    if best>60: worst.append({"cad":sf["building_cadnum"],"en":sf["entrance"],"units":sf["unit_count"],
                              "lat":sf["lat"],"lng":sf["lng"],"nearest_same_letter_m":round(best,1)})
print("nearest same-letter geocoder entrance:", dict(buckets))
print("units at stake (all folded misses):", sum(s["unit_count"] for s in miss))
print("units in >60m group:", sum(w["units"] for w in worst), "rows:", len(worst))
worst.sort(key=lambda w:-w["units"])
json.dump(worst, open("worst_misses.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
for w in worst[:12]: print("   ", w)
