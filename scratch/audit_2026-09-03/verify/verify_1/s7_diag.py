import json, collections, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
VB = "C:/git/Varna_buildings"
EN = json.load(open(VB+"/output/search_index_entrances.json", encoding="utf-8"))
G  = json.load(open(VB+"/output/geocoder_index.json", encoding="utf-8"))
U  = json.load(open(VB+"/output/section_units.json", encoding="utf-8"))
AI = json.load(open(VB+"/output/address_index.json", encoding="utf-8"))
ai_cad = {r[4] for r in AI}

gen = [e for e in G["entries"] if e.get("en")]
gkeys = {(e["section_cadnum"], e["en"]) for e in gen}
print("geocoder en entries:", len(gen), "distinct (sec,en) keys:", len(gkeys))

# section_units labelled entrance keys
ukeys = set(); ukeys_all = set(); u_by_cad = {}
u_unlab = collections.Counter()
for u in U:
    sc = u.get("section_cadnum")
    u_by_cad[sc] = u
    for e in (u.get("entrances") or []):
        if not e: continue
        if e.get("en") in (None, ""):
            u_unlab[sc] += 1
            continue
        ukeys.add((sc, str(e["en"])))
print("section_units labelled entrance keys:", len(ukeys))
print("ukeys == gkeys ?", ukeys == gkeys, "| only in units:", len(ukeys-gkeys), "| only in geocoder:", len(gkeys-ukeys))
missing_units_in_ai = {sc for (sc,_) in (ukeys-gkeys)} - ai_cad
print("units-only keys whose cadnum is absent from address_index:", len(missing_units_in_ai))

# authority docs
docs = []
for k, did in EN["documentIds"].items():
    sf = EN["storedFields"][k]
    docs.append((sf["building_cadnum"], sf["entrance"], sf["unit_count"], sf["lat"], sf["lng"]))
dkeys = {(c,e) for c,e,_,_,_ in docs}
print("authority entrance doc keys:", len(dkeys))
miss = sorted(dkeys - gkeys)
extra = sorted(gkeys - dkeys)
print("docs not in geocoder:", len(miss), "| geocoder not in docs:", len(extra))

# classify miss
c_no_unit = 0; c_unit_no_such_en = 0; c_unit_unlabelled = 0
detail = []
for cad, en in miss:
    u = u_by_cad.get(cad)
    if u is None:
        c_no_unit += 1; why = "cadnum not an MF section unit at all"
    else:
        ens = [str(e.get("en")) for e in (u.get("entrances") or []) if e and e.get("en") not in (None,"")]
        nun = sum(1 for e in (u.get("entrances") or []) if e and e.get("en") in (None,""))
        if not ens and nun:
            c_unit_unlabelled += 1; why = f"unit has {nun} UNLABELLED entrances"
        else:
            c_unit_no_such_en += 1; why = f"unit labelled ens={ens} (no '{en}')"
    detail.append({"cad":cad,"en":en,"why":why})
print("miss: cadnum has no section unit:", c_no_unit)
print("miss: unit exists, all its entrances unlabelled:", c_unit_unlabelled)
print("miss: unit exists with other labels:", c_unit_no_such_en)
json.dump(detail, open("miss_detail.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
for d in detail[:10]: print("  ", d["cad"], d["en"], "|", d["why"])
