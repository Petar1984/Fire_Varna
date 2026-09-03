# -*- coding: utf-8 -*-
# Оборител №2 / находка №1 · стъпка 3: ВРЕДНО ЛИ Е „решението"?
# Строя двата очевидни варианта на per-record поправката и меря Q1..Q5 за всеки.
import io, json, sys
from collections import Counter, OrderedDict
sys.path.insert(0, r"C:\git\Fire_Varna\scratch\places_search")
sys.path.insert(0, r"C:\Users\Petar\AppData\Local\Temp\claude\C--git\fb0c0608-7fdb-4635-a8fc-44575d26700a\scratchpad\audit_2026-09-03\търсачка")
import recall_sweep as rs
import recall_all as ra

RECS = rs.RECS

def search_variant(q, mode):
    """mode: 'base' = днешният код; 'A' = per-record (зоната бие името);
       'B' = обединение (именните попадения ПЪРВИ, после зоновите)."""
    qt = rs.place_tokens(q)
    if not qt:
        return [], "empty"
    keys, slots, dead = rs.split_keys(qt)
    if keys:
        cls = rs.CLASS_OF[keys[0]]
        R = [t for (t, ki) in slots if ki is None or ki != 0]
        has_key = True
    else:
        cls = RECS
        R = [t for (t, ki) in slots]
        has_key = False
    if not R:
        return rs.order_category(cls), "M1-category"
    if not has_key:
        cls = [r for r in cls if rs.gen_ok(r)]
        if not cls:
            return [], "M3-too-big"
    if has_key:
        zk_all, nm_all = set(), set()
        for r in cls:
            zk_all |= r.zkset
            nm_all |= r.nset
        hits_name = any(t.s in nm_all for t in R)
        all_zone = all(t.s in zk_all for t in R)
        if mode == "base":
            if all_zone and not hits_name:
                flt = [r for r in cls if all(t.s in r.zkset for t in R)]
                if flt:
                    return rs.order_category(flt), "A3-category+zone/kind"
        elif mode == "A":                      # per-record: махам class-wide nm-пазача
            if all_zone:
                flt = [r for r in cls if all(t.s in r.zkset for t in R)]
                if flt:
                    return rs.order_category(flt), "A3'-perrecord"
        elif mode == "B":                      # обединение
            if all_zone:
                flt = [r for r in cls if all(t.s in r.zkset for t in R)]
                if flt:
                    named = rs.run_scored(cls, R, has_key, dead)
                    seen = set(id(x) for x in named)
                    tail = [r for r in rs.order_category(flt) if id(r) not in seen]
                    if named or tail:
                        return list(named) + tail, "A3''-union"
    rows = rs.run_scored(cls, R, has_key, dead)
    if rows:
        return rows, ("M2" if has_key else "M3")
    if has_key:
        R2 = [t for (t, ki) in slots]
        rows = rs.run_scored(RECS, R2, False, dead)
        if rows:
            return rows, "M2-failopen"
    return [], ("M2" if has_key else "M3")


# --- 1. сравнение по трите спорни заявки
print(u"=== какво връщат трите варианта ===")
for q in [u"хотел Одесос", u"хотел Морска градина", u"училище Морска градина",
          u"хотел Приморски", u"хотел Златни пясъци", u"хотел Зеленика"]:
    line = []
    for m in ("base", "A", "B"):
        rows, br = search_variant(q, m)
        first = (rows[0].name + u" [" + rows[0].zone + u"]") if rows else u"—"
        line.append(u"%s: n=%d (%s) 1-ви=%s" % (m, len(rows), br, first))
    print(u"\n  %s" % q)
    for l in line:
        print(u"     " + l)

# --- 2. пълен Q1..Q5 recall за трите варианта
def sweep(mode):
    cache = {}
    agg = OrderedDict((k, {"n": 0, "r1": 0, "r3": 0, "r8": 0, "miss": 0})
                      for k in ("Q1", "Q2", "Q3", "Q4", "Q5"))
    for r in RECS:
        kw = ra.KIND_WORD[r.kind]
        n2 = ra.q2_name(r.name)
        mw, mk = ra.q5_main(r.name)
        zb = ra.zone_bare(r.zone)
        for qt, q in (("Q1", r.name), ("Q2", n2), ("Q3", (kw + u" " + n2).strip()),
                      ("Q4", (kw + u" " + zb).strip()), ("Q5", mw)):
            q = (q or u"").strip()
            a = agg[qt]
            a["n"] += 1
            if not q:
                a["miss"] += 1
                continue
            k = (mode, q)
            if k not in cache:
                cache[k] = search_variant(q, mode)
            rows, br = cache[k]
            rk = rs.rank_of(rows, r)
            if rk < 0:
                a["miss"] += 1
                continue
            if rk + 1 <= 1: a["r1"] += 1
            if rk + 1 <= 3: a["r3"] += 1
            if rk + 1 <= 8: a["r8"] += 1
    return agg

print(u"\n=== Q1..Q5 recall за трите варианта (361 записа) ===")
print(u"%-6s %-5s %6s %6s %6s %6s" % ("mode", "Q", "r@1", "r@3", "r@8", "miss"))
res = {}
for m in ("base", "A", "B"):
    res[m] = sweep(m)
    for k, v in res[m].items():
        print(u"%-6s %-5s %6d %6d %6d %6d" % (m, k, v["r1"], v["r3"], v["r8"], v["miss"]))
    print("")

print(u"=== разлики спрямо base ===")
for m in ("A", "B"):
    for k in res[m]:
        b, v = res["base"][k], res[m][k]
        d = [(f, v[f] - b[f]) for f in ("r1", "r3", "r8", "miss") if v[f] != b[f]]
        if d:
            print(u"  %s %s: %s" % (m, k, d))
