# -*- coding: utf-8 -*-
import json,sys,collections,re
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"
EN=json.load(open(VB+"/search_index_entrances.json",encoding="utf-8"))
SU=json.load(open(VB+"/section_units.json",encoding="utf-8"))
recs=list(EN["storedFields"].values())
su_ent=collections.defaultdict(list)
su_cad=set()
for u in SU:
    su_cad.add(u["section_cadnum"])
    for e in (u.get("entrances") or []):
        if e and e.get("en") not in (None,""): su_ent[u["section_cadnum"]].append(str(e["en"]))
su_keys={(c,e) for c,v in su_ent.items() for e in v}
missing=[r for r in recs if (r["building_cadnum"],str(r["entrance"])) not in su_keys]

def dirty(s):
    s=str(s)
    return bool(re.search(r"[,;/]| |тяло|бл|вх", s, re.I)) or len(s)>3
d=[r for r in missing if dirty(r["entrance"])]
print("missing docs total:",len(missing))
print("  with a COMPOSITE/dirty entrance label (comma, space, 'тяло', len>3):",len(d))
print("  label histogram (top 20):",collections.Counter(str(r['entrance']) for r in missing).most_common(20))
print()
in_su=[r for r in missing if r["building_cadnum"] in su_cad]
print("missing whose section IS in section_units:",len(in_su),
      "over",len({r['building_cadnum'] for r in in_su}),"sections")
d2=[r for r in in_su if dirty(r["entrance"])]
print("  of those, dirty label:",len(d2))
# for the in_su ones: does section_units already have MORE entrances than EN for that section?
en_per_cad=collections.Counter(r["building_cadnum"] for r in recs)
cmp=collections.Counter()
for c in {r["building_cadnum"] for r in in_su}:
    a,b=en_per_cad[c],len(su_ent.get(c,[]))
    cmp["SU>=EN" if b>=a else "SU<EN"]+=1
print("  sections where section_units has >= as many entrances as EN:",cmp)
print()
notin=[r for r in missing if r["building_cadnum"] not in su_cad]
print("missing whose SECTION is absent from section_units:",len(notin),
      "over",len({r['building_cadnum'] for r in notin}),"sections (different KAIS extract)")
# reverse
en_keys={(r["building_cadnum"],str(r["entrance"])) for r in recs}
extra=[k for k in su_keys if k not in en_keys]
print("section_units entrances absent from EN:",len(extra))
