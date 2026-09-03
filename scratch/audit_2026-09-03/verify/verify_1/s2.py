import json, collections, itertools, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
VB = "C:/git/Varna_buildings"
EN = json.load(open(VB+"/output/search_index_entrances.json", encoding="utf-8"))
ids = EN["documentIds"]
sf = EN["storedFields"]
print("sample documentIds:", list(itertools.islice(ids.items(),5)))
print("sample storedFields:", list(itertools.islice(sf.items(),3)))
vals = list(ids.values())
print("unique doc ids:", len(set(vals)))
cad = collections.Counter(v.rsplit(":",1)[0] for v in vals)
print("distinct cadnum prefix:", len(cad))
print("top cad:", cad.most_common(5))
