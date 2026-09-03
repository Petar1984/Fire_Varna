# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\git\Fire_Varna\scratch\places_search")
sys.path.insert(0, r"C:\Users\Petar\AppData\Local\Temp\claude\C--git\fb0c0608-7fdb-4635-a8fc-44575d26700a\scratchpad\audit_2026-09-03\търсачка")
sys.path.insert(0, r"C:\Users\Petar\AppData\Local\Temp\claude\C--git\fb0c0608-7fdb-4635-a8fc-44575d26700a\scratchpad\audit_2026-09-03\verify_2")
import recall_sweep as rs, recall_all as ra
from variants import search_variant

print(u'=== 4.1 Q3 (vid + ime): kogo chupi variant A ===')
for r in rs.RECS:
    kw = ra.KIND_WORD[r.kind]
    n2 = ra.q2_name(r.name)
    q = (kw + u" " + n2).strip()
    if not q:
        continue
    rb, brb = search_variant(q, "base")
    rA, brA = search_variant(q, "A")
    kb, ka = rs.rank_of(rb, r), rs.rank_of(rA, r)
    if (kb >= 0) != (ka >= 0) or (kb >= 0 and ka >= 0 and ka > kb):
        print(u'  ZAYAVKA %-34s | %s [%s]' % (q, r.name, r.zone))
        print(u'      base: rang=%s n=%d (%s)  ->  A: rang=%s n=%d (%s)'
              % ((kb + 1) if kb >= 0 else u'NYAMA', len(rb), brb,
                 (ka + 1) if ka >= 0 else u'NYAMA', len(rA), brA))

print(u'\n=== 4.2 "hotel gradina" - edinstveniyat pat do hotel GRADINA (chernova 3.2) ===')
for m in ("base", "A", "B"):
    rows, br = search_variant(u"хотел градина", m)
    idx = [i for i, x in enumerate(rows) if x.name.strip() == u"ГРАДИНА"]
    print(u'  %-5s n=%-3d klon=%-20s rang na hotel GRADINA = %s ; 1-vi: %s [%s]'
          % (m, len(rows), br, (idx[0] + 1) if idx else u'NYAMA',
             rows[0].name if rows else u'-', rows[0].zone if rows else u'-'))

print(u'\n=== 4.3 drugi "vid + ime, koeto e i kvartal" ===')
for q, who in [(u"хотел приморски", u"ПРИМОРСКИ"), (u"хотел зеленика", u"Зеленика"),
               (u"хотел чайка", u"Чайка"), (u"детска градина чайка", u"Чайка"),
               (u"хотел одесос", u"ОДЕСОС"), (u"училище изгрев", u"Изгрев")]:
    out = []
    for m in ("base", "A", "B"):
        rows, br = search_variant(q, m)
        idx = [i for i, x in enumerate(rows) if who.lower() in x.name.lower()]
        out.append(u'%s n=%-3d rang=%s' % (m, len(rows), (idx[0] + 1) if idx else u'NYAMA'))
    print(u'  %-30s [%s] %s' % (q, who, u' | '.join(out)))
