import json, sys, io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
VB="C:/git/Varna_buildings"; FV="C:/git/Fire_Varna"
G=json.load(open(VB+"/output/geocoder_index.json",encoding="utf-8"))
S=json.load(open(FV+"/data/search_index.json",encoding="utf-8"))
dpins={tuple(e["pin"]) for e in S["entries"] if e.get("pin")}
for c in ["10135.xxxx","10135.xxxx","10135.xxxx","10135.xxxx","10135.xxxx","10135.xxxx"]:
    ge=[e for e in G["entries"] if e.get("cadnum")==c]
    print(c, "geocoder entries:", [(e["kind"], tuple(e["pin"])) for e in ge],
          "| pin present in DELIVERY:", all(tuple(e["pin"]) in dpins for e in ge))
