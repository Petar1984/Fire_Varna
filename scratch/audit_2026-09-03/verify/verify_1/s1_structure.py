import json, collections, itertools
VB = "C:/git/Varna_buildings"
EN = json.load(open(VB+"/output/search_index_entrances.json", encoding="utf-8"))
print("EN top keys:", list(EN.keys()))
for k in EN:
    v = EN[k]
    print(" ", k, type(v).__name__, (len(v) if hasattr(v,'__len__') else v))
ids = EN["documentIds"]
print("documentIds type:", type(ids).__name__, "len", len(ids))
it = list(itertools.islice(ids.items() if isinstance(ids,dict) else enumerate(ids), 5))
print("sample:", it)
