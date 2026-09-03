import json, collections, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
VB = "C:/git/Varna_buildings"
EN = json.load(open(VB+"/output/search_index_entrances.json", encoding="utf-8"))
G  = json.load(open(VB+"/output/geocoder_index.json", encoding="utf-8"))
GE = G["entries"]
reps = G.get("physical_building_reps", {})

# authority entrance docs
docs = []
for k, did in EN["documentIds"].items():
    sf = EN["storedFields"][k]
    docs.append({"doc": did, "cad": sf["building_cadnum"], "en": sf["entrance"],
                 "lat": sf["lat"], "lng": sf["lng"], "units": sf["unit_count"]})
print("docs:", len(docs))

gen = [e for e in GE if e.get("en")]
print("geocoder entries with en:", len(gen))
# geocoder join keys
g_by_sec = collections.defaultdict(list)
for e in gen:
    g_by_sec[(e.get("section_cadnum"), e["en"])].append(e)
g_by_cad = collections.defaultdict(list)
for e in gen:
    g_by_cad[(e.get("cadnum"), e["en"])].append(e)

hit_sec = sum(1 for d in docs if (d["cad"], d["en"]) in g_by_sec)
hit_cad = sum(1 for d in docs if (d["cad"], d["en"]) in g_by_cad)
print("docs matched by (section_cadnum,en):", hit_sec)
print("docs matched by (cadnum,en):", hit_cad)
either = [d for d in docs if (d["cad"], d["en"]) in g_by_sec or (d["cad"], d["en"]) in g_by_cad]
print("docs matched by either:", len(either))
miss = [d for d in docs if (d["cad"], d["en"]) not in g_by_sec and (d["cad"], d["en"]) not in g_by_cad]
print("docs unmatched:", len(miss))

# reverse: geocoder en entries not backed by a doc
docset_sec = {(d["cad"], d["en"]) for d in docs}
gmiss = [e for e in gen if (e.get("section_cadnum"), e["en"]) not in docset_sec and (e.get("cadnum"), e["en"]) not in docset_sec]
print("geocoder en entries with no authority doc:", len(gmiss))
json.dump(miss, open("miss_docs.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump([{k:e.get(k) for k in ("id","kind","cadnum","section_cadnum","en","complex_id","pin")} for e in gmiss],
          open("miss_geo.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
print("sample miss docs:", json.dumps(miss[:5], ensure_ascii=False))
