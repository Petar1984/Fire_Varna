# -*- coding: utf-8 -*-
"""Колко от латинските етикети са само транслитерация, и колко са ОЩЕ и осакатени
   от skel() (й/ю/я→i/iu/ia, ъ→a, двойни съгласни събрани)."""
import json, re, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
FV="C:/git/Fire_Varna/"
si=json.load(open(FV+"data/search_index.json",encoding="utf-8")); E=si["entries"]
WS=re.compile(r"\s+")
def pretty(s): return WS.sub(" ",str(s).replace("|"," ")).strip()
CYR=set("абвгдежзийклмнопрстуфхцчшщъьюя")
def al(s):
    t=s.lower(); c=any(ch in CYR for ch in t); l=any(ch in "abcdefghijklmnopqrstuvwxyz" for ch in t)
    return "mixed" if c and l else "cyr" if c else "lat" if l else "none"
cnt=collections.Counter()
for e in E:
    if e.get("label"):
        s=pretty(e["label"])
        if al(s) in ("lat","mixed"): cnt[s]+=1
print("най-честите латински етикети на екрана (брой записа):")
for s,n in cnt.most_common(20): print("   %5d  %s"%(n,s))
deg=[s for s in cnt if re.search(r"(iu|ia|sht|zh|ts|ch|sh)", s)]
print("\nетикети със skel-белези (iu/ia/sht/zh/ts/ch/sh) =",len(deg),"от",len(cnt),"уникални латински")
print("примери:",sorted(deg)[:15])
