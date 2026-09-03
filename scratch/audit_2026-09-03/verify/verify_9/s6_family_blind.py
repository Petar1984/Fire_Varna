# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №9 · стъпка 6 — защо „СЕМЕЙСТВО 0/34“ не е доказателство за съгласие."""
import json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
A = Path(r"C:\Users\Petar\AppData\Local\Temp\claude\C--git\fb0c0608-7fdb-4635-a8fc-44575d26700a\scratchpad\audit_2026-09-03\вид-квартал\anomalies.json")
rows = json.load(open(A, encoding="utf-8"))["all_rows"]
VB = Path(r"C:\git\Varna_buildings")
sys.path.insert(0, str(VB/"tools"))
from quarter_name_fold import match_key
reg = json.load(open(VB/"config"/"quarter_registry.json", encoding="utf-8"))
fam = {}
for e in reg["entries"]:
    for form in [e["display"], *e.get("aliases", [])]:
        fam.setdefault(match_key(str(form)), set()).add(e["display"])

CH13 = {"hotels[0]","hotels[1]","hotels[4]","hotels[33]","hotels[34]","hotels[37]",
        "hotels[100]","hotels[101]","hotels[102]","hotels[103]","hotels[104]",
        "hotels[113]","hotels[210]"}
print("=== суровият КАИС quar се хваща ли от регистъра (fam_quar) ===")
for x in rows:
    if x["key"] in CH13:
        raw = x.get("bld_quar")
        mk = match_key(str(raw)) if raw else None
        print(f"  {x['key']:<12} {x['name'][:20]:<22} суров={str(raw)[:26]:<28} "
              f"match_key={str(mk)[:24]:<26} в регистъра={'ДА' if mk in fam else 'НЕ':<3} "
              f"fam_quar={x.get('fam_quar')} · dist={x['bld_dist_m']} m")
show = [x for x in rows if x.get("quar_show") and x.get("zone") and x["quar_show"] != x["zone"]]
print("\nот 34-те показ-разминавания: fam_quar е None при", len([x for x in show if not x.get("fam_quar")]),
      "· fam_zone е None при", len([x for x in show if not x.get("fam_zone")]))
print("→ затова cmp_fam (иска И ДВЕТЕ) мълчи: „СЕМЕЙСТВО 0/34“ е СЛЯПО, не съгласие.")
print("\n„и двете страни в регистъра: 34“ и „показът се разминава: 34“ са ДВЕ РАЗЛИЧНИ множества:")
both = {x["key"] for x in rows if x.get("fam_zone") and x.get("fam_quar")}
print("   |и двете в регистъра| =", len(both), "· |показ-разминавания| =", len(show),
      "· ПРЕСИЧАНЕ =", len(both & {x["key"] for x in show}))
