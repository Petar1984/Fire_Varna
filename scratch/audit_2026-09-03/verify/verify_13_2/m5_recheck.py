# -*- coding: utf-8 -*-
"""M5: възпроизвеждане на 6 числа от черновата. READ-ONLY."""
import json, sys, collections, re
sys.stdout.reconfigure(encoding='utf-8')
SI = json.load(open(r"C:/git/Fire_Varna/data/search_index.json", encoding='utf-8'))
E = SI['entries']
print("[1] entries:", len(E), "| черновата: 86 232")
print("    по kind:", collections.Counter(e.get('kind') for e in E).most_common(),
      "| черновата: address 70 575 · mf 14 687 · parcel 970")
lat = re.compile(r'[a-z]', re.I); cyr = re.compile(r'[\u0400-\u04FF]')
labs = [e.get('label') or '' for e in E]
only_lat = sum(1 for s in labs if lat.search(s) and not cyr.search(s))
mixed   = sum(1 for s in labs if lat.search(s) and cyr.search(s))
print("[2] само латиница:", only_lat, f"({100*only_lat/len(E):.1f}%)", "| черновата: 31 916 (37,0 %)")
print("    смесени:", mixed, "| черновата: 2 838")
ent = [e for e in E if 'en' in e]
print("[3] входове:", len(ent), "| черновата: 4 764")
print("    без display_id:", sum(1 for e in ent if 'display_id' not in e), "| черновата: 2 916")
print("    без 'g' (сграда-родител):", sum(1 for e in ent if 'g' not in e), "| черновата: 0")
par = [e for e in E if e.get('kind')=='parcel']
def dec(x):
    s = repr(float(x)); return len(s.split('.')[1]) if '.' in s else 0
p7 = sum(1 for e in par if max(dec(e['pin'][0]), dec(e['pin'][1])) >= 7)
print("[4] parcel-пинове със >=7 знака:", p7, "| черновата: 296")
H = json.load(open(r"C:/git/Fire_Varna/data/hotels.json", encoding='utf-8'))
hs = H['hotels'] if isinstance(H, dict) and 'hotels' in H else (H if isinstance(H, list) else list(H.values())[0])
print("[5] хотели:", len(hs), "| черновата: 226")
uin = [h for h in hs if h.get('uin') or h.get('УИН') or h.get('ntr_uin')]
print("    редове с УИН:", len(uin), "· уникални:", len(set((h.get('uin') or h.get('ntr_uin')) for h in uin)),
      "| черновата: 213 уникални УИН, 34 без")
P = json.load(open(r"C:/git/Fire_Varna/data/places.json", encoding='utf-8'))
ps = P['places'] if isinstance(P, dict) and 'places' in P else (P if isinstance(P, list) else list(P.values())[0])
print("[6] места:", len(ps), "| черновата: 135")
print("    по вид:", collections.Counter(p.get('kind') or p.get('type') for p in ps).most_common(),
      "| черновата: 60/46/13/7/6/3")
