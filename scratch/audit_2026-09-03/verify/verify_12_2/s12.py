# -*- coding: utf-8 -*-
import json,sys,collections,unicodedata
sys.stdout.reconfigure(encoding="utf-8")
VB=r"C:/git/Varna_buildings/output"
EN=json.load(open(VB+"/search_index_entrances.json",encoding="utf-8"))
SU=json.load(open(VB+"/section_units.json",encoding="utf-8"))
recs=list(EN["storedFields"].values())
su_ent=collections.defaultdict(set); su_cad=set()
for u in SU:
    su_cad.add(u["section_cadnum"])
    for e in (u.get("entrances") or []):
        if e and e.get("en") not in (None,""): su_ent[u["section_cadnum"]].add(str(e["en"]))
su_keys={(c,e) for c,v in su_ent.items() for e in v}
missing=[r for r in recs if (r["building_cadnum"],str(r["entrance"])) not in su_keys]

# Latin->Cyrillic homoglyph fold
LAT2CYR=str.maketrans({"A":"А","B":"В","E":"Е","K":"К","M":"М","H":"Н","O":"О","P":"Р","C":"С","T":"Т","X":"Х","Y":"У",
                       "a":"а","b":"в","e":"е","k":"к","m":"м","o":"о","p":"р","c":"с","t":"т","x":"х","y":"у"})
def fold(s): return str(s).strip().upper().translate(LAT2CYR)
su_fold={(c,fold(e)) for c,e in su_keys}
still=[r for r in missing if (r["building_cadnum"],fold(r["entrance"])) not in su_fold]
print("missing before homoglyph+case fold:",len(missing))
print("missing AFTER latin->cyrillic + upper fold:",len(still))
print("  => explained purely by alphabet/case normalisation:",len(missing)-len(still))
in_su=[r for r in still if r["building_cadnum"] in su_cad]
notin=[r for r in still if r["building_cadnum"] not in su_cad]
print("  remaining, section present in section_units:",len(in_su),"over",len({r['building_cadnum'] for r in in_su}),"sections")
print("  remaining, section ABSENT from section_units:",len(notin),"over",len({r['building_cadnum'] for r in notin}),"sections")
print("  remaining label histogram:",collections.Counter(str(r['entrance']) for r in still).most_common(15))
# reverse direction with fold
en_fold={(r["building_cadnum"],fold(r["entrance"])) for r in recs}
extra=[k for k in su_keys if (k[0],fold(k[1])) not in en_fold]
print("section_units entrances absent from EN after fold:",len(extra))
json.dump({"remaining_examples":[{"cad":r["building_cadnum"],"en":r["entrance"],"units":r["unit_count"],
                                  "lat":r["lat"],"lng":r["lng"],
                                  "su_has":sorted(su_ent.get(r["building_cadnum"],[]))}
                                 for r in sorted(still,key=lambda x:-(x.get("unit_count") or 0))[:25]]},
          open("s12_remaining.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
