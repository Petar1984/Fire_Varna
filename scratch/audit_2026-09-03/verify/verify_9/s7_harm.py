# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №9 · стъпка 7 — ВРЕДАТА на решението: разпиляване на показа."""
import json, sys
from collections import Counter
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
A = Path(r"C:\Users\Petar\AppData\Local\Temp\claude\C--git\fb0c0608-7fdb-4635-a8fc-44575d26700a\scratchpad\audit_2026-09-03\вид-квартал\anomalies.json")
rows = json.load(open(A, encoding="utf-8"))["all_rows"]
sk = [x for x in rows if x["zone"] == "к.к. Св. Константин"]
print("днес zone == „к.к. Св. Константин“:", len(sk), "реда · показен низ: 1 вариант")
new = Counter()
for x in sk:
    new[x["quar_show"] or x["zone"]] += 1
print("след размяната (стъпка 1↔2) курортът се показва в", len(new), "варианта:")
for k, v in new.most_common(): print(f"   {v:>3}  „{k}“")
print()
zl = [x for x in rows if x["zone"] == "к.к. Златни пясъци"]
newz = Counter(x["quar_show"] or x["zone"] for x in zl)
print("днес zone == „к.к. Златни пясъци“:", len(zl), "реда · 1 вариант")
print("след размяната:", len(newz), "варианта:")
for k, v in newz.most_common(): print(f"   {v:>3}  „{k}“")
print()
ch = [x for x in rows if x["zone"] == "к.к. Чайка"]
newc = Counter(x["quar_show"] or x["zone"] for x in ch)
print("днес zone == „к.к. Чайка“:", len(ch), "реда · 1 вариант · след размяната:", len(newc))
for k, v in newc.most_common(): print(f"   {v:>3}  „{k}“")
tot_before = len({x["zone"] for x in rows})
tot_after = len({(x["quar_show"] or x["zone"]) for x in rows})
print(f"\nразлични показни низа върху 361-те реда: днес {tot_before} → след размяната {tot_after}")
