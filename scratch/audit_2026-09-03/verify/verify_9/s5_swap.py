# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №9 · стъпка 5 — вредно ли е „решението“: кадастърът над кутията?"""
import json, sys
from collections import Counter
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
A = Path(r"C:\Users\Petar\AppData\Local\Temp\claude\C--git\fb0c0608-7fdb-4635-a8fc-44575d26700a\scratchpad\audit_2026-09-03\вид-квартал\anomalies.json")
rows = json.load(open(A, encoding="utf-8"))["all_rows"]
FIRE = Path(r"C:\git\Fire_Varna")
hot = json.load(open(FIRE/"data"/"hotels.json", encoding="utf-8"))["hotels"]

# --- A. цената ДНЕС: 13-те хотела, които не се броят към „Златни пясъци“ ----
CH13 = ["hotels[0]","hotels[1]","hotels[4]","hotels[33]","hotels[34]","hotels[37]",
        "hotels[100]","hotels[101]","hotels[102]","hotels[103]","hotels[104]",
        "hotels[113]","hotels[210]"]
byk = {x["key"]: x for x in rows}
beds = 0
print("=== A. цената на 13-те (какво не влиза в списъка „Златни пясъци“) ===")
for k in CH13:
    i = int(k.split("[")[1][:-1]); h = hot[i]
    bl = h.get("beds") or []
    bl = bl if isinstance(bl, list) else [bl]
    b = sum(v for v in bl if isinstance(v, int)); beds += b
    print(f"  {k:<12} {h['name'][:26]:<28} легла={h.get('beds')!s:<6} вид={h.get('kind')!s:<22} зона={h.get('zone')}")
print("СБОР легла на 13-те:", beds)
zl = [x for x in rows if x["zone"] == "к.к. Златни пясъци"]
def bsum(h):
    bl = h.get("beds") or []
    bl = bl if isinstance(bl, list) else [bl]
    return sum(v for v in bl if isinstance(v, int))
zl_beds = sum(bsum(hot[int(x['key'].split('[')[1][:-1])]) for x in zl if x["file"] == "hotels")
print(f"днес „к.к. Златни пясъци“ = {len(zl)} реда; ако 13-те се върнат → {len(zl)+13}")
print(f"легла днес в Златни: {zl_beds} · с 13-те: {zl_beds+beds} (+{beds/zl_beds*100:.1f}%)")

# --- B. глобалният ефект от размяната ---------------------------------------
print("\n=== B. алтернативна стълба: КАИС quar → чертан → кутия ===")
moved, unchanged, lost_named = [], 0, []
for x in rows:
    new = x.get("quar_show") or x.get("drawn_show") or x["zone"]
    if new == x["zone"]:
        unchanged += 1
    else:
        moved.append((x, new))
print("редове, които биха СМЕНИЛИ показа:", len(moved), "· непроменени:", unchanged)
print("  по стъпка днес:", dict(Counter(x["step"] for x, _ in moved)))
print("  по двойка (днес → ново), топ 15:")
for (a, b), n in Counter((x["zone"], nw) for x, nw in moved).most_common(15):
    print(f"     {n:>3}  „{a}“ → „{b}“")
# вреда: ред, който днес носи ИМЕНУВАН квартал, а новото е общо (район/гр. Варна)
GEN = lambda s: s.startswith("район ") or s in ("гр. Варна", "Виница/север", "Аспарухово/Галата")
harm = [(x, nw) for x, nw in moved if not GEN(x["zone"]) and GEN(nw)]
gain = [(x, nw) for x, nw in moved if GEN(x["zone"]) and not GEN(nw)]
print("  ВРЕДА (именуван → общ):", len(harm))
for x, nw in harm[:10]: print(f"     {x['key']:<12} {x['name'][:24]:<26} „{x['zone']}“ → „{nw}“")
print("  ПЕЧАЛБА (общ → именуван):", len(gain))
for x, nw in gain[:10]: print(f"     {x['key']:<12} {x['name'][:24]:<26} „{x['zone']}“ → „{nw}“")

# --- C. само стъпка 1 ↔ 2 (кадастърът над кутията, чертаният си остава 3) ---
print("\n=== C. само КАИС над кутията (стъпка 1↔2) ===")
sw = [(x, x["quar_show"]) for x in rows if x["step"] == "1" and x.get("quar_show")
      and x["quar_show"] != x["zone"]]
print("реда, които се местят:", len(sw))
print("  по двойка:", dict(Counter((x["zone"], nw) for x, nw in sw)))
print("  от 13-те Чайка/Златни се поправят:", len([1 for x, _ in sw if x["key"] in CH13]),
      "· остават криви:", 13 - len([1 for x, _ in sw if x["key"] in CH13]))
rest = [k for k in CH13 if k not in {x['key'] for x, _ in sw}]
print("  остават (поправят се само от чертания слой, стъпка 3):",
      [byk[k]["name"] for k in rest])
