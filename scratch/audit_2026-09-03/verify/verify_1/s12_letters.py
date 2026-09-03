import json, collections, sys, io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
VB="C:/git/Varna_buildings"
EN=json.load(open(VB+"/output/search_index_entrances.json",encoding="utf-8"))
G=json.load(open(VB+"/output/geocoder_index.json",encoding="utf-8"))
gen=[e for e in G["entries"] if e.get("en")]
gl=collections.Counter(e["en"].strip().upper() for e in gen)
print("geocoder distinct letters:", len(gl))
print(sorted(gl.items(), key=lambda x:-x[1])[:30])
gkeys={(e["section_cadnum"],e["en"]) for e in gen}
gkeys_ci={(c,en.strip().upper()) for c,en in gkeys}
docs=[EN["storedFields"][k] for k in EN["storedFields"]]
dl=collections.Counter(sf["entrance"].strip().upper() for sf in docs)
print("doc distinct letters:", len(dl))
print(sorted(dl.items(), key=lambda x:-x[1])[:30])
miss=[sf for sf in docs if (sf["building_cadnum"],sf["entrance"]) not in gkeys
      and (sf["building_cadnum"],sf["entrance"].strip().upper()) not in gkeys_ci]
ml=collections.Counter(sf["entrance"].strip().upper() for sf in miss)
print("miss letters not present anywhere in geocoder:",
      sorted([(k,v) for k,v in ml.items() if k not in gl], key=lambda x:-x[1])[:40])
print("sum of those:", sum(v for k,v in ml.items() if k not in gl))
