# -*- coding: utf-8 -*-
"""M6: изворът на всяко място по клас (OSM срещу регистър) + Чайка-броячът.
READ-ONLY. Изход: m6_provenance.json"""
import json, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
P = json.load(open(r"C:/git/Fire_Varna/data/places.json", encoding='utf-8'))
ps = P['places'] if isinstance(P, dict) and 'places' in P else P
H = json.load(open(r"C:/git/Fire_Varna/data/hotels.json", encoding='utf-8'))
hs = H['hotels'] if isinstance(H, dict) and 'hotels' in H else H
t = collections.defaultdict(lambda: collections.Counter())
for p in ps:
    t[p['kind']][ 'OSM' if p.get('src')=='OSM' else 'регистър' ] += 1
print(f"{'клас':18s} {'общо':>5s} {'OSM':>5s} {'%OSM':>6s} {'регистър':>9s}")
for k, c in sorted(t.items(), key=lambda kv: -sum(kv[1].values())):
    tot = sum(c.values())
    print(f"{k:18s} {tot:5d} {c['OSM']:5d} {100*c['OSM']/tot:5.1f}% {c['регистър']:9d}")
tot = len(ps); osm = sum(1 for p in ps if p.get('src')=='OSM')
print(f"{'ОБЩО места':18s} {tot:5d} {osm:5d} {100*osm/tot:5.1f}% {tot-osm:9d}")
z = collections.Counter([p.get('zone') for p in ps] + [h.get('zone') for h in hs])
print("\nзона к.к. Чайка (места+хотели):", z.get('к.к. Чайка'), "| черновата: 38")
print("хотели с зона к.к. Чайка:", sum(1 for h in hs if h.get('zone')=='к.к. Чайка'))
print("места с зона к.к. Чайка:", sum(1 for p in ps if p.get('zone')=='к.к. Чайка'))
json.dump({"by_class": {k: dict(v) for k, v in t.items()}, "osm_total": osm, "places": tot,
           "chayka": z.get('к.к. Чайка')}, open("m6_provenance.json","w",encoding='utf-8'),
          ensure_ascii=False, indent=1)
