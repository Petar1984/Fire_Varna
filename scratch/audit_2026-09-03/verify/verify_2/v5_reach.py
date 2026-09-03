# -*- coding: utf-8 -*-
# Стъпка 5: губи ли пожарникарят ДОСТЪП до 62-та записа, или само един път до тях?
import io, json, sys
from collections import Counter
sys.path.insert(0, r"C:\git\Fire_Varna\scratch\places_search")
sys.path.insert(0, r"C:\Users\Petar\AppData\Local\Temp\claude\C--git\fb0c0608-7fdb-4635-a8fc-44575d26700a\scratchpad\audit_2026-09-03\търсачка")
import recall_sweep as rs, recall_all as ra

d = json.load(io.open("v2_q4.json", encoding="utf-8"))
miss_idx = set(m[0] for m in d["miss"])
print(u"nenamereni po Q4: %d" % len(miss_idx))

cache = {}
def S(q):
    if q not in cache:
        cache[q] = rs.search(q)
    return cache[q]

st = Counter()
worst = []
for i, r in enumerate(rs.RECS):
    if i not in miss_idx:
        continue
    kw = ra.KIND_WORD[r.kind]
    n2 = ra.q2_name(r.name)
    res = {}
    for tag, q in (("Q1", r.name), ("Q3", (kw + u" " + n2).strip())):
        q = (q or u"").strip()
        if not q:
            res[tag] = None
            continue
        rows, br = S(q)
        k = rs.rank_of(rows, r)
        res[tag] = (k + 1) if k >= 0 else None
    ok1 = res["Q1"] is not None and res["Q1"] <= 8
    ok3 = res["Q3"] is not None and res["Q3"] <= 8
    st["Q1<=8" if ok1 else "Q1 NE"] += 1
    st["Q3<=8" if ok3 else "Q3 NE"] += 1
    if not (ok1 or ok3):
        worst.append((r.name, r.zone, res))
print(u"ot 62-ta: %s" % dict(st))
print(u"nedostignati i po ime (Q1 i Q3 nad rang 8 ili lipsvat): %d" % len(worst))
for w in worst:
    print(u"   %s [%s] %s" % w)

# --- znamenatel po ZAYAVKI
pq = d["per_query"]
print(u"\nrazlichni Q4 zayavki: %d ; schupeni: %d (%.1f%%)"
      % (len(pq), sum(1 for v in pq.values() if v["miss"]),
         100.0 * sum(1 for v in pq.values() if v["miss"]) / len(pq)))
