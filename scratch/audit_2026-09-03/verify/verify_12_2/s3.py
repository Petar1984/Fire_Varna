# -*- coding: utf-8 -*-
import json,sys,collections
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"
G=json.load(open(VB+"/geocoder_index.json",encoding="utf-8"))
gent=[e for e in G["entries"] if e.get("en") is not None]
print("geocoder entrance entries:",len(gent))
print("distinct complex_id:",len({e.get("complex_id") for e in gent}))
print("distinct cadnum:",len({e["cadnum"] for e in gent}))
print("distinct section_cadnum:",len({e.get("section_cadnum") for e in gent}))
# is complex_id count == 1748 ?
cc=collections.Counter(e.get("complex_id") for e in gent)
print("complex_id groups:",len(cc))
# how many sections per complex
sec_per_complex=collections.defaultdict(set)
for e in gent: sec_per_complex[e.get("complex_id")].add(e.get("section_cadnum"))
h=collections.Counter(len(v) for v in sec_per_complex.values())
print("sections per complex hist:",dict(sorted(h.items())))
