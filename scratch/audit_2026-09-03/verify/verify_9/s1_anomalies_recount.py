# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №9 · стъпка 1 — преброяване НАНОВО върху anomalies.json (all_rows)."""
import json, sys
from collections import Counter, defaultdict
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
A = Path(r"C:\Users\Petar\AppData\Local\Temp\claude\C--git\fb0c0608-7fdb-4635-a8fc-44575d26700a\scratchpad\audit_2026-09-03\вид-квартал\anomalies.json")
d = json.load(open(A, encoding="utf-8"))
rows = d["all_rows"]
print("редове:", len(rows))

show = [x for x in rows if x.get("quar_show") and x.get("zone") and x["quar_show"] != x["zone"]]
print("ПОКАЗ зона↔КАИС се разминава:", len(show))
print("  по стъпка:", dict(Counter(x["step"] for x in show)))
print("  по двойка (zone → quar_show):")
for (z,q),n in Counter((x["zone"], x["quar_show"]) for x in show).most_common():
    print(f"     {n:>3}  „{z}“ → „{q}“")

fam = [x for x in rows if x.get("fam_zone") and x.get("fam_quar") and x["fam_zone"] != x["fam_quar"]]
print("СЕМЕЙСТВО зона↔КАИС се разминава:", len(fam))
both = [x for x in rows if x.get("fam_zone") and x.get("fam_quar")]
print("и двете страни в регистъра:", len(both))
print("  колко от 'показ'-разминаванията са и в 'и двете в регистъра':",
      len([x for x in show if x.get("fam_zone") and x.get("fam_quar")]))
print("  fam_zone=None сред показ-разминаванията:", len([x for x in show if not x.get("fam_zone")]))
print("  fam_quar=None сред показ-разминаванията:", len([x for x in show if not x.get("fam_quar")]))

print()
print("=== ЧАЙКА-редовете (zone == 'к.к. Чайка') ===")
ch = [x for x in rows if x["zone"] == "к.к. Чайка"]
print("общо:", len(ch), " lat диапазон: %.4f – %.4f" % (min(x["lat"] for x in ch), max(x["lat"] for x in ch)))
kais_zl = [x for x in ch if x.get("quar_show") == "к.к. Златни пясъци"]
drawn_zl = [x for x in ch if x.get("drawn_show") == "к.к. Златни пясъци"]
uni = {x["key"] for x in kais_zl} | {x["key"] for x in drawn_zl}
inter = {x["key"] for x in kais_zl} & {x["key"] for x in drawn_zl}
print("КАИС казва Златни пясъци:", len(kais_zl), sorted(x["name"] for x in kais_zl))
print("чертан слой казва Златни:", len(drawn_zl), sorted(x["name"] for x in drawn_zl))
print("ОБЕДИНЕНИЕ (поне един свидетел):", len(uni))
print("ПРЕСИЧАНЕ (и двамата):", len(inter))
byk = {x["key"]: x for x in ch}
print("само КАИС:", sorted(byk[k]["name"] for k in ({x['key'] for x in kais_zl} - inter)))
print("само чертан:", sorted(byk[k]["name"] for k in ({x['key'] for x in drawn_zl} - inter)))
lats = [byk[k]["lat"] for k in uni]
print("lat ивица на обединението: %.4f – %.4f" % (min(lats), max(lats)))
print()
for k in sorted(uni, key=lambda k: byk[k]["lat"]):
    x = byk[k]
    print(f"  {x['key']:<12} {x['name'][:28]:<30} lat={x['lat']:.5f} lon={x['lon']:.5f} "
          f"КАИС={x.get('quar_show')!s:<20} чертан={x.get('drawn_show')!s:<20} обв={x.get('encl_show')!s} стъпка={x['step']}")
print()
print("Чайка-редове, при които НИТО ЕДИН свидетел не казва Златни:", len(ch)-len(uni))
for x in sorted([y for y in ch if y["key"] not in uni], key=lambda y: y["lat"]):
    print(f"  {x['key']:<12} {x['name'][:28]:<30} lat={x['lat']:.5f} КАИС={x.get('quar_show')!s:<22} чертан={x.get('drawn_show')!s:<22} обв={x.get('encl_show')}")
