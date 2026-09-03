# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №9 · стъпка 3 — 9-те 'кутия≠зона', 37-те 'район …' и разпадът на 34."""
import json, sys
from collections import Counter
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
A = Path(r"C:\Users\Petar\AppData\Local\Temp\claude\C--git\fb0c0608-7fdb-4635-a8fc-44575d26700a\scratchpad\audit_2026-09-03\вид-квартал\anomalies.json")
rows = json.load(open(A, encoding="utf-8"))["all_rows"]

def box(lat, lon):
    if lat >= 43.2780: return "к.к. Златни пясъци"
    if lat >= 43.2600 and lon >= 28.0250: return "к.к. Чайка"
    if lat >= 43.2460: return "Виница/север"
    if lat >= 43.2150 and lon >= 27.9900: return "к.к. Св. Константин"
    if lat <= 43.1900: return "Аспарухово/Галата"
    return "гр. Варна"

print("=== A. разпад на 34-те показ-разминавания зона↔КАИС ===")
show = [x for x in rows if x.get("quar_show") and x.get("zone") and x["quar_show"] != x["zone"]]
def norm(s):
    s = (s or "").lower().replace('"','').replace('„','').replace('“','')
    s = s.replace("св.св.","св св").replace("св. св.","св св").replace("свети свети","св св")
    s = s.replace("св. константин и елена","св св константин и елена")
    s = s.replace("к.к.","").replace("с.о.","").replace("кв.","").strip()
    return " ".join(s.split())
same_place, diff_place = [], []
for x in show:
    z, q = norm(x["zone"]), norm(x["quar_show"])
    # „св константин“ ⊂ „св св константин и елена“ = ЕДИН И СЪЩ курорт
    if ("константин" in z and "константин" in q):
        same_place.append(x)
    else:
        diff_place.append(x)
print("  същият курорт, различно ИЗПИСВАНЕ (Св. Константин ↔ Св.св. Константин и Елена):", len(same_place))
print("  НАИСТИНА различно място:", len(diff_place))
for x in sorted(diff_place, key=lambda y: y["zone"]):
    print(f"     {x['key']:<12} {x['name'][:26]:<28} зона „{x['zone']}“ → КАИС „{x['quar_show']}“ (dist {x['bld_dist_m']} m)")

print("\n=== B. кутията срещу ЗАПИСАНАТА зона (курортните) ===")
res = [x for x in rows if x["zone"] in ("к.к. Златни пясъци","к.к. Чайка","к.к. Св. Константин")]
bad = [x for x in res if box(x["lat"], x["lon"]) != x["zone"]]
print("курортни редове:", len(res), "· кутията дава друго при", len(bad))
for x in sorted(bad, key=lambda y: y["lat"]):
    print(f"   {x['key']:<12} {x['name'][:24]:<26} lat={x['lat']:.5f} кутия={box(x['lat'],x['lon']):<20} записано={x['zone']:<22} стъпка={x['step']}")

print("\n=== C. общите етикети („район …“, кутии, „гр. Варна“) ===")
gen = [x for x in rows if x["zone"].startswith("район ") or x["zone"] in ("гр. Варна","Виница/север","Аспарухово/Галата")]
print("общо реда с ОБЩ етикет:", len(gen), dict(Counter(x["zone"] for x in gen)))
print("  от тях по стъпка:", dict(Counter(x["step"] for x in gen)))
# кои са блокирани от поименните изключения (PIP_EXCLUDE)
import re
blocked = [x for x in gen if x.get("step_note") and ("поименното изключение" in x["step_note"])]
print("  паднали, защото отгоре стои САМО поименно изключение:", len(blocked))
print("  по изключение:", dict(Counter(
    re.findall(r'изключение „([^“]+)“', x["step_note"])[0] if re.findall(r'изключение „([^“]+)“', x["step_note"]) else "?"
    for x in blocked)))
key_names = Counter()
for x in blocked:
    for k in re.findall(r'„([^“]+)“', x["step_note"]):
        key_names[k] += 1
print("  всички ключове, споменати в бележките на блокираните:", dict(key_names))
print("  примери:")
for x in blocked[:6]:
    print(f"     {x['key']:<12} {x['name'][:26]:<28} зона={x['zone']:<18} | {x['step_note'][:150]}")
json.dump({"diff_place": diff_place, "same_spelling": len(same_place),
           "box_vs_zone": bad, "generic": len(gen), "blocked": len(blocked)},
          open(Path(__file__).with_name("s3_out.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
