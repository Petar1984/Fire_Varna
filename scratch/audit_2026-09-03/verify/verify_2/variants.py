# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\git\Fire_Varna\scratch\places_search")
import recall_sweep as rs
RECS = rs.RECS

def search_variant(q, mode):
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
        elif mode == "A":
            if all_zone:
                flt = [r for r in cls if all(t.s in r.zkset for t in R)]
                if flt:
                    return rs.order_category(flt), "A3'-perrecord"
        elif mode == "B":
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
