import json, collections, sys, io, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
VB = "C:/git/Varna_buildings"
EN = json.load(open(VB+"/output/search_index_entrances.json", encoding="utf-8"))
G  = json.load(open(VB+"/output/geocoder_index.json", encoding="utf-8"))
GE = G["entries"]; reps = G.get("physical_building_reps", {})
docs = []
for k, did in EN["documentIds"].items():
    sf = EN["storedFields"][k]
    docs.append({"doc": did, "cad": sf["building_cadnum"], "en": sf["entrance"],
                 "lat": sf["lat"], "lng": sf["lng"], "units": sf["unit_count"]})
gen = [e for e in GE if e.get("en")]
g_keys = {(e.get("section_cadnum"), e["en"]) for e in gen} | {(e.get("cadnum"), e["en"]) for e in gen}
miss = [d for d in docs if (d["cad"], d["en"]) not in g_keys]
print("miss:", len(miss))

# rep-based collapse test
g_rep_keys = collections.defaultdict(list)
for e in gen:
    sc = e.get("section_cadnum") or e.get("cadnum")
    g_rep_keys[(reps.get(sc, sc), e["en"])].append(e)
collapsed = [d for d in miss if (reps.get(d["cad"], d["cad"]), d["en"]) in g_rep_keys]
print("miss explained by physical_building_reps collapse:", len(collapsed))

# how many miss cadnums appear in reps at all
in_reps = sum(1 for d in miss if d["cad"] in reps)
print("miss docs whose cadnum is in physical_building_reps:", in_reps)

# does the cadnum appear anywhere in geocoder (any kind)?
all_cad = collections.Counter()
for e in GE:
    for k in ("cadnum","section_cadnum"):
        if e.get(k): all_cad[e[k]] += 1
miss_cad_present = sum(1 for d in miss if all_cad.get(d["cad"]))
print("miss docs whose cadnum exists somewhere in geocoder:", miss_cad_present)
print("miss docs whose cadnum absent from geocoder entirely:", len(miss)-miss_cad_present)

# distinct buildings among miss
mc = collections.Counter(d["cad"] for d in miss)
print("distinct miss buildings:", len(mc))
print("top miss buildings:", mc.most_common(8))
# how many miss buildings have SOME entrance in geocoder (partial loss) vs none
g_cads_en = {e.get("section_cadnum") for e in gen} | {e.get("cadnum") for e in gen}
partial = sum(1 for c in mc if c in g_cads_en)
print("miss buildings with SOME entrance in geocoder (partial):", partial, "/", len(mc))
json.dump({"miss_count": len(miss), "collapsed": len(collapsed)}, open("s5.json","w"))
