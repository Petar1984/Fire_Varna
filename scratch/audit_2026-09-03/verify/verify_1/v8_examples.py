# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from fvlib import *
ENT=[e for e in E if e.get('kind')=='mf' and e.get('en') is not None]
def show(sub, pool=None):
    pool = ENT if pool is None else pool
    print("=== търсено:", sub)
    hits=[e for e in pool if sub in norm(fmt(e))]
    for e in hits:
        print(f"   {e['kind']:7s} {fmt(e):42s} pin={e['pin']} g={e.get('g')} did={e.get('display_id')} район={DN[e['d']] if e.get('d') is not None else None}")
    pts=[tuple(e['pin']) for e in hits]
    if len(pts)>1:
        mx=max(dm(a,b) for i,a in enumerate(pts) for b in pts[i+1:])
        print(f"   -> записи={len(hits)} уникални пинове={len(set(pts))} уникални g={len({e.get('g') for e in hits})} макс.разделение={mx:.1f} m")
    print()
for s in ["кв левски бл 2 · вх а","цар симеон 36","братя георгиевич 15"]:
    show(s)
show("кв левски бл 2", E)
