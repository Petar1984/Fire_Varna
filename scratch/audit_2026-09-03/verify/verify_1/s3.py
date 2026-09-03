import json, collections, itertools, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
VB = "C:/git/Varna_buildings"
G = json.load(open(VB+"/output/geocoder_index.json", encoding="utf-8"))
print("G keys:", list(G.keys()))
GE = G["entries"]
print("entries:", len(GE))
print("kinds:", collections.Counter(e["kind"] for e in GE))
with_en = [e for e in GE if e.get("en")]
print("with en:", len(with_en))
print("sample en entry:", json.dumps(with_en[0], ensure_ascii=False)[:800])
print("sample non-en:", json.dumps([e for e in GE if not e.get("en")][0], ensure_ascii=False)[:600])
for k in G:
    if k!="entries":
        print("meta", k, json.dumps(G[k], ensure_ascii=False)[:400])
