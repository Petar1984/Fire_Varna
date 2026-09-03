import json, collections, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
VB = "C:/git/Varna_buildings"
EN = json.load(open(VB+"/output/search_index_entrances.json", encoding="utf-8"))
G  = json.load(open(VB+"/output/geocoder_index.json", encoding="utf-8"))
gen = [e for e in G["entries"] if e.get("en")]
gkeys = {(e["section_cadnum"], e["en"]) for e in gen}
gkeys_ci = {(c, en.strip().upper()) for c, en in gkeys}
docs=[]
for k,did in EN["documentIds"].items():
    sf=EN["storedFields"][k]; docs.append((sf["building_cadnum"], sf["entrance"], sf))
dkeys={(c,e) for c,e,_ in docs}
miss = sorted(dkeys-gkeys)
print("miss exact:", len(miss))
miss_ci = [(c,e) for c,e in miss if (c, e.strip().upper()) not in gkeys_ci]
print("miss after case-insensitive fold:", len(miss_ci))
print("explained purely by letter case:", len(miss)-len(miss_ci))
# reverse
extra = sorted(gkeys-dkeys)
dkeys_ci = {(c,e.strip().upper()) for c,e in dkeys}
extra_ci=[(c,e) for c,e in extra if (c,e.strip().upper()) not in dkeys_ci]
print("geocoder-only exact:", len(extra), "after fold:", len(extra_ci))
print("net gap exact:", len(miss)-len(extra), " net gap folded:", len(miss_ci)-len(extra_ci))
json.dump({"miss_exact":len(miss),"miss_folded":len(miss_ci),"case_only":len(miss)-len(miss_ci),
           "extra_exact":len(extra),"extra_folded":len(extra_ci)}, open("s8.json","w"))
# sample of real (folded) misses with units
sample=[]
for c,e in miss_ci[:400]:
    sf=[s for cc,ee,s in docs if cc==c and ee==e][0]
    sample.append({"cad":c,"en":e,"units":sf["unit_count"],"lat":sf["lat"],"lng":sf["lng"]})
json.dump(sample, open("miss_folded_sample.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
uc = sum(s["units"] for s in sample)
print("sum unit_count over folded misses (first 400):", uc)
