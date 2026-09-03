import json, collections, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
VB="C:/git/Varna_buildings"; FV="C:/git/Fire_Varna"
EN=json.load(open(VB+"/output/search_index_entrances.json",encoding="utf-8"))
G=json.load(open(VB+"/output/geocoder_index.json",encoding="utf-8"))
gen=[e for e in G["entries"] if e.get("en")]
print("geocoder en entries:",len(gen))
print("distinct section_cadnum among them:", len({e["section_cadnum"] for e in gen}))
print("distinct cadnum among them:", len({e["cadnum"] for e in gen}))
print("distinct complex_id:", len({e.get("complex_id") for e in gen}))
docs_cad={EN["storedFields"][k]["building_cadnum"] for k in EN["storedFields"]}
print("distinct buildings in entrance search index:", len(docs_cad))
print("overlap of building sets:", len(docs_cad & {e["section_cadnum"] for e in gen}))
# delivered
S=json.load(open(FV+"/data/search_index.json",encoding="utf-8"))
print("delivered keys:", list(S.keys())[:12])
