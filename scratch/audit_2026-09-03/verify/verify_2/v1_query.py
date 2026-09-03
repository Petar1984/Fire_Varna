# -*- coding: utf-8 -*-
# Оборител №2 / находка №1 · стъпка 1: възпроизвеждам "хотел одесос" и броя хотелите по зона.
import io, json, os, sys
sys.path.insert(0, r"C:\git\Fire_Varna\scratch\places_search")
import recall_sweep as rs                      # if __name__-guard -> importът не пуска main()

def show(q):
    rows, br = rs.search(q)
    print(u"ЗАЯВКА %-32s n=%-4d branch=%s" % (u"'"+q+u"'", len(rows), br))
    for r in rows[:6]:
        print(u"      -> %s | вид=%s | зона=%s" % (r.name, r.kind, r.zone))
    if len(rows) > 6:
        print(u"      ... още %d" % (len(rows)-6))
    return rows, br

for q in [u"хотел одесос", u"хотел златни пясъци", u"хотел златни",
          u"хотел морска градина", u"училище морска градина",
          u"хотел приморски", u"одесос", u"хотел"]:
    show(q)
    print("")

# --- броя по зона направо от данните (не от търсачката)
from collections import Counter
hot = [r for r in rs.RECS if r.kind in (u"Хотел", u"Семеен хотел",
                                        u"хотел · без категоризация", u"апарт-хотел")]
print(u"общо хотел-записи: %d" % len(hot))
c = Counter(r.zone for r in hot)
for z, n in sorted(c.items(), key=lambda kv: -kv[1]):
    print(u"   %-34s %d" % (z, n))
print(u"\nхотели със зона 'район Одесос': %d" % c.get(u"район Одесос", 0))
print(u"хотели, чието ИМЕ носи токена 'одесос': %s"
      % [r.name + u" / " + r.zone for r in hot if u"odesos" in {v for v in r.nset} or
         any(t.s in r.nset for t in rs.place_tokens(u"одесос"))])
