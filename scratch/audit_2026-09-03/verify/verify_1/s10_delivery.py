import json, collections, sys, io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
FV="C:/git/Fire_Varna"; VB="C:/git/Varna_buildings"
S=json.load(open(FV+"/data/search_index.json",encoding="utf-8"))
E=S["entries"]
print("delivered entries:",len(E))
print("sample entry:", json.dumps(E[0],ensure_ascii=False)[:400])
en=[e for e in E if e.get("en")]
print("delivered with en:",len(en))
print("sample en:", json.dumps(en[0],ensure_ascii=False)[:400])
print("keys on en entries:", collections.Counter(tuple(sorted(e.keys())) for e in en).most_common(3))
print("distinct g among en entries:", len({e.get("g") for e in en}))
print("kinds:", collections.Counter(e.get("kind") for e in E))
