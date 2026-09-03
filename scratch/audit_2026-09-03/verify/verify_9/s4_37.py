# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №9 · стъпка 4 — откъде е числото 37 („чакат пре-начертаване“)?"""
import json, re, sys
from collections import Counter
from pathlib import Path
from shapely.geometry import shape, Point
from shapely.strtree import STRtree
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
A = Path(r"C:\Users\Petar\AppData\Local\Temp\claude\C--git\fb0c0608-7fdb-4635-a8fc-44575d26700a\scratchpad\audit_2026-09-03\вид-квартал\anomalies.json")
rows = json.load(open(A, encoding="utf-8"))["all_rows"]
M6 = Path(r"C:\git\m6000_private\number_viewer\quarters_drawn_v1.geojson")
EXC = ('оу "константин арабаджиев', "чайка", "южна промишлена зона")

dr = json.load(open(M6, encoding="utf-8"))["features"]
g, k = [], []
for f in dr:
    try: gg = shape(f["geometry"])
    except Exception: continue
    g.append(gg); k.append(((f.get("properties") or {}).get("key") or "").lower())
t = STRtree(g)
def hits(lat, lon):
    p = Point(lon, lat)
    return sorted({k[j] for j in t.query(p) if g[j].covers(p)})

cnt = Counter(); rows_in = []
for x in rows:
    h = hits(x["lat"], x["lon"])
    exc = [q for q in h if q in EXC]
    canon = [q for q in h if q not in EXC]
    if exc:
        cnt[tuple(exc)] += 1
    if exc and not canon:
        rows_in.append({**x, "exc": exc})
print("редове, падащи в поне едно поименно изключение:", sum(cnt.values()))
for kk, v in cnt.most_common(): print("   ", kk, v)
print("редове, върху които стои САМО изключение (няма каноничен полигон):", len(rows_in))
print("   по изключение:", dict(Counter(tuple(x["exc"]) for x in rows_in)))
print("   по зона:", dict(Counter(x["zone"] for x in rows_in)))
print("   по стъпка:", dict(Counter(x["step"] for x in rows_in)))
# двата за пре-чертаване (без 'чайка', която има подписано правило)
two = [x for x in rows_in if any(e in ('оу "константин арабаджиев', "южна промишлена зона") for e in x["exc"])]
print("САМО двата за пре-чертаване (арабаджиев / южна пром. зона):", len(two))
print("   по зона:", dict(Counter(x["zone"] for x in two)))
print("   по стъпка:", dict(Counter(x["step"] for x in two)))
# кандидат-източник на 37: редове на стъпка 4/H с общ етикет и изключение отгоре
c37 = [x for x in two if x["step"] in ("4", "H")]
print("от тях на стъпка 4/H:", len(c37))
# кандидат: „район Одесос“ 42 · редове с 'южна промишлена зона' отгоре
odes = [x for x in rows if x["zone"] == "район Одесос"]
o_exc = [x for x in odes if any(q in EXC for q in hits(x["lat"], x["lon"]))]
print("„район Одесос“ реда:", len(odes), "· от тях с изключение отгоре:", len(o_exc))
json.dump(rows_in, open(Path(__file__).with_name("s4_out.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
