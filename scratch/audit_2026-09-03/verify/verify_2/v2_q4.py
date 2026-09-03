# -*- coding: utf-8 -*-
# Оборител №2 / находка №1 · стъпка 2: собствено преброяване на Q4 ("вид + квартал").
import io, json, os, sys
from collections import Counter, OrderedDict
sys.path.insert(0, r"C:\git\Fire_Varna\scratch\places_search")
sys.path.insert(0, r"C:\Users\Petar\AppData\Local\Temp\claude\C--git\fb0c0608-7fdb-4635-a8fc-44575d26700a\scratchpad\audit_2026-09-03\търсачка")
import recall_sweep as rs
import recall_all as ra                      # само за KIND_WORD / zone_bare

recs = list(rs.RECS)
print(u"записи общо: %d" % len(recs))

cache = {}
def srch(q):
    if q not in cache:
        cache[q] = rs.search(q)
    return cache[q]

miss, r1, r3, r8 = [], 0, 0, 0
per_query = OrderedDict()
for i, r in enumerate(recs):
    kw = ra.KIND_WORD[r.kind]
    zb = ra.zone_bare(r.zone)
    q = (kw + u" " + zb).strip()
    rows, br = srch(q)
    rk = rs.rank_of(rows, r)
    rank = (rk + 1) if rk >= 0 else None
    per_query.setdefault(q, {"n": len(rows), "branch": br, "tot": 0, "miss": 0,
                             "first": rows[0].name if rows else u"",
                             "first_zone": rows[0].zone if rows else u""})
    per_query[q]["tot"] += 1
    if rank is None:
        miss.append((i, r.name, r.kind, r.zone, q, len(rows), br))
        per_query[q]["miss"] += 1
    else:
        if rank <= 1: r1 += 1
        if rank <= 3: r3 += 1
        if rank <= 8: r8 += 1

print(u"Q4: r@1=%d  r@3=%d  r@8=%d  не се намира=%d  (%.1f%%)"
      % (r1, r3, r8, len(miss), 100.0*len(miss)/len(recs)))
print(u"различни Q4 заявки: %d" % len(per_query))
bad = [(q, v) for q, v in per_query.items() if v["miss"]]
print(u"заявки, при които ПОНЕ ЕДИН запис пада: %d" % len(bad))
print(u"")
print(u"| заявка | върнати | клон | скрити/общо в зоната | първи ред (зона) |")
for q, v in sorted(bad, key=lambda kv: -kv[1]["miss"]):
    print(u"| %-34s | %4d | %-22s | %3d/%-3d | %s (%s) |"
          % (q, v["n"], v["branch"], v["miss"], v["tot"], v["first"], v["first_zone"]))
print(u"\nсбор на скритите: %d" % sum(v["miss"] for _, v in bad))

# по група
g = Counter()
for m in miss:
    g[m[2]] += 1
print(u"\nпо вид: %s" % dict(g))

# колко от миналите Q4 заявки минават през A3
brs = Counter(v["branch"] for v in per_query.values())
print(u"клонове по различни заявки: %s" % dict(brs))
json.dump({"miss": miss, "per_query": per_query}, io.open("v2_q4.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
