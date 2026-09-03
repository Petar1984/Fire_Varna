# -*- coding: utf-8 -*-
import sys, io, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from fvlib import *
ENT=[e for e in E if e.get('kind')=='mf' and e.get('en') is not None]
by=collections.defaultdict(list)
for e in ENT: by[norm(fmt(e))].append(e)
B={}   # клас B: >1 dropdown ред (различно g) -> вижда N еднакви реда
A={}   # клас A: >1 пин, но ЕДНО g -> слива се в 1 ред, другите места СКРИТИ
for lab,es in by.items():
    gs={e.get('g') for e in es}; pins={tuple(e['pin']) for e in es}
    if len(gs)>1: B[lab]=es
    elif len(pins)>1: A[lab]=es
print("клас B (N реда един до друг, различно g):  групи=%d записи=%d"%(len(B),sum(len(v) for v in B.values())))
print("клас A (1 ред, >1 място СКРИТО, същото g): групи=%d записи=%d"%(len(A),sum(len(v) for v in A.values())))
rowhist=collections.Counter()
for lab,es in B.items(): rowhist[len({e.get('g') for e in es})]+=1
print("клас B — брой dropdown редове на група:", dict(sorted(rowhist.items())))
big=[(len({e.get('g') for e in es}),lab,es) for lab,es in B.items()]
big.sort(reverse=True)
print("\n--- клас B, най-много редове ---")
for n,lab,es in big[:8]:
    pts=[tuple(e['pin']) for e in es]
    mx=max(dm(a,b) for i,a in enumerate(pts) for b in pts[i+1:])
    print(f"  редове={n} записи={len(es)} разделение={mx:.0f} m   {fmt(es[0])}")
# двата „кандидата" от черновата — в кой клас са?
print("\n--- проверка на двата примера от черновата ---")
for probe in ["цар симеон 36 · вх в","ул братя георгиевич 15 · вх а"]:
    es=by.get(probe)
    if es is None:
        print("   НЯМА такъв ключ:",probe); continue
    gs={e.get('g') for e in es}; pts=[tuple(e['pin']) for e in es]
    mx=max(dm(a,b) for i,a in enumerate(pts) for b in pts[i+1:]) if len(pts)>1 else 0
    print(f"   '{probe}': записи={len(es)} уникални g={len(gs)} разстояние={mx:.1f} m -> клас {'B (виждат се 2 реда)' if len(gs)>1 else 'A (сливат се в 1 ред; второто място СКРИТО)'}")
# А колко от клас-B групите биха се събрали в топ-8 наведнъж?
over8=sum(1 for lab,es in B.items() if len({e.get('g') for e in es})>8)
print("\nклас B групи с >8 реда (не се побират в дропдауна):",over8)
