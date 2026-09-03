import json, collections, re, sys, io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
VB="C:/git/Varna_buildings"; FV="C:/git/Fire_Varna"
EN=json.load(open(VB+"/output/search_index_entrances.json",encoding="utf-8"))
G=json.load(open(VB+"/output/geocoder_index.json",encoding="utf-8"))
U=json.load(open(VB+"/output/section_units.json",encoding="utf-8"))
gen=[e for e in G["entries"] if e.get("en")]
LAT2CYR=str.maketrans("ABEKMHOPCTYXaebkmhopctyx","АВЕКМНОРСТУХАЕВКМНОРСТУХ")
norm=lambda s: s.strip().upper().translate(LAT2CYR)
gk={(e["section_cadnum"], norm(e["en"])) for e in gen}
docs=[EN["storedFields"][k] for k in EN["storedFields"]]
miss=[sf for sf in docs if (sf["building_cadnum"], norm(sf["entrance"])) not in gk]
COMP=re.compile(r"[,\-+/\s\"]|ТЯЛО|СЕКЦИЯ")
dirty=[s for s in miss if COMP.search(norm(s["entrance"])) or len(norm(s["entrance"]))>2]
clean=[s for s in miss if s not in dirty]
u_by={u["section_cadnum"]:u for u in U}
cls=collections.Counter()
for s in clean:
    u=u_by.get(s["building_cadnum"])
    if u is None: cls["A: cadnum absent from section_units (not an MF section)"]+=1
    else:
        lab=[str(e["en"]) for e in (u.get("entrances") or []) if e and e.get("en") not in (None,"")]
        unl=sum(1 for e in (u.get("entrances") or []) if e and e.get("en") in (None,""))
        if not lab and unl: cls["B: unit exists, ALL its entrances unlabelled"]+=1
        elif not lab and not unl: cls["C: unit exists with ZERO entrance objects"]+=1
        else: cls["D: unit exists, has other labels, this one absent"]+=1
print("=== corrected numbers ===")
print("authority(strategic_intel May-24) entrance docs :", len(docs))
print("geocoder/delivery(section_units Aug-15) entrance:", len(gen))
print("raw subtraction 5314-4764                       :", len(docs)-len(gen))
print("docs absent by EXACT key                        :", sum(1 for sf in docs if (sf['building_cadnum'],sf['entrance']) not in {(e['section_cadnum'],e['en']) for e in gen}))
print("docs absent after case+homoglyph fold           :", len(miss))
print("  of them dirty/composite labels                :", len(dirty))
print("  of them clean single labels                   :", len(clean), " units:", sum(s['unit_count'] for s in clean))
print("  distinct buildings behind the clean ones      :", len({s['building_cadnum'] for s in clean}))
print("geocoder entrances absent from authority (fold) :", len([e for e in gen if (e['section_cadnum'],norm(e['en'])) not in {(s['building_cadnum'],norm(s['entrance'])) for s in docs}]))
print()
print("=== why the clean ones are absent ===")
for k,v in sorted(cls.items()): print(f"  {k}: {v}")
print()
print("=== building-level, corrected ===")
print("buildings in authority entrance index :", len({s['building_cadnum'] for s in docs}))
print("section_cadnum in geocoder entrances  :", len({e['section_cadnum'] for e in gen}))
print("subset? ", {e['section_cadnum'] for e in gen} <= {s['building_cadnum'] for s in docs})
print("distinct complex_id in geocoder en    :", len({e.get('complex_id') for e in gen}))
S=json.load(open(FV+"/data/search_index.json",encoding="utf-8"))
print("distinct g in DELIVERED en entries    :", len({e.get('g') for e in S['entries'] if e.get('en')}))
json.dump({"clean":len(clean),"dirty":len(dirty),"miss":len(miss),
           "clean_units":sum(s['unit_count'] for s in clean),
           "clean_buildings":len({s['building_cadnum'] for s in clean}),
           "cls":dict(cls)}, open("final.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
