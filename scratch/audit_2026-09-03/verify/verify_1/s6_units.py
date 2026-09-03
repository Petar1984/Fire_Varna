import json, collections, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
VB = "C:/git/Varna_buildings"
U = json.load(open(VB+"/output/section_units.json", encoding="utf-8"))
print("section_units:", type(U).__name__, len(U))
print("sample keys:", list(U[0].keys()))
tot_en = 0; labelled = 0
by_cad = {}
for u in U:
    ens = u.get("entrances") or []
    tot_en += len(ens)
    lab = [e for e in ens if e and e.get("en") not in (None,"")]
    labelled += len(lab)
    by_cad[u.get("section_cadnum") or u.get("cadnum")] = u
print("total entrance objects in section_units:", tot_en, "labelled:", labelled)
print("distinct section units:", len(by_cad))
json.dump({"units":len(U),"entrance_objs":tot_en,"labelled":labelled}, open("s6.json","w"))
