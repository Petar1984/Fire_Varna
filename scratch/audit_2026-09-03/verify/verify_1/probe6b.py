# -*- coding: utf-8 -*-
import json, math, collections
FV = r"C:/git/Fire_Varna"
def hav(la1,lo1,la2,lo2):
    R=6371008.8; p1,p2=math.radians(la1),math.radians(la2)
    a=math.sin((p2-p1)/2)**2+math.cos(p1)*math.cos(p2)*math.sin(math.radians(lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(a))
places=json.load(open(FV+"/data/places.json",encoding="utf-8"))["places"]
hotels=json.load(open(FV+"/data/hotels.json",encoding="utf-8"))["hotels"]
rows=[dict(r,set="places") for r in places]+[dict(r,set="hotels") for r in hotels]
print("двойки на <=25 m (всички):")
for i in range(len(rows)):
    for j in range(i+1,len(rows)):
        d=hav(rows[i]["lat"],rows[i]["lon"],rows[j]["lat"],rows[j]["lon"])
        if d<=25:
            print("  %6.1f m | %-55s [%s] <-> %-55s [%s]"%(d,rows[i]["name"],rows[i]["set"],rows[j]["name"],rows[j]["set"]))
g=collections.Counter((round(r["lat"],6),round(r["lon"],6)) for r in rows)
print("\nгрупи с ИДЕНТИЧНА координата (6 знака):", sum(1 for v in g.values() if v>1))
for k,v in g.items():
    if v>1:
        print("  ",k,v,[r["name"] for r in rows if (round(r["lat"],6),round(r["lon"],6))==k])
