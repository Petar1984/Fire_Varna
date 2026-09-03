# -*- coding: utf-8 -*-
# Стъпка 6: спасява ли ПЪЛНАТА форма на квартала („хотел район одесос“) днешния код?
import sys
sys.path.insert(0, r"C:\git\Fire_Varna\scratch\places_search")
import recall_sweep as rs
for q in [u"хотел одесос", u"хотел район одесос", u"хотели одесос",
          u"хотел одесос варна", u"хотел морска градина", u"хотел в морска градина",
          u"училище морска градина", u"училище район приморски",
          u"детска градина владиславово", u"детска градина аспарухово"]:
    rows, br = rs.search(q)
    z = {}
    for r in rows:
        z[r.zone] = z.get(r.zone, 0) + 1
    print(u"%-32s n=%-4d %-24s zoni=%s"
          % (q, len(rows), br, sorted(z.items(), key=lambda kv: -kv[1])[:3]))
