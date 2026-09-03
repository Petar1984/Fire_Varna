# -*- coding: utf-8 -*-
import json, sys, io
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
B='C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/kais_func_2026-09-03/'
P=json.load(open(B+'парцели/plots_by_func.json',encoding='utf-8'))['plots']
C=json.load(open(B+'парцели/candidates.json',encoding='utf-8'))['candidates']
CL=['детско заведение','образование','здравно заведение','хотел','курортна/туристическа','общежитие','социални грижи']
REGS=['район Владислав Варненчик','район Приморски','район Младост','район Одесос','район Аспарухово']
def regof(o):
    r=[x for x in (o.get('reg') or []) if x]
    return r[0] if r else '—'
def srcgrp(c):
    s=c.get('name_src','')
    if s.startswith('б'): return 'OSM'
    if s.startswith('в2'): return 'в2'
    if s.startswith('в'): return 'регистър'
    if s.startswith('а'): return 'КАИС'
    return '—'
print('| клас | район | КАИС парцели | доставени | канд. С ИМЕ (OSM / регистър / в2) | канд. БЕЗ ИМЕ |')
print('|---|---|---:|---:|---|---:|')
for cls in CL:
    par=defaultdict(int); cand=defaultdict(lambda: defaultdict(int)); noname=defaultdict(int)
    for pl in P[cls]['link_45m']: par[regof(pl)]+=1
    for c in C[cls]:
        rg=regof(c)
        if c['name_src']=='без име': noname[rg]+=1
        else: cand[rg][srcgrp(c)]+=1
    keys=sorted(par, key=lambda r: (REGS.index(r) if r in REGS else 9))
    T=[0,0,0,0,0,0]
    lines=[]
    for rg in keys:
        n=par[rg]; cw=cand[rg]; nn=noname[rg]
        named=sum(cw.values()); deliv=n-named-nn
        lines.append('|  | %s | %d | %d | %d (%d / %d / %d) | %d |' % (
            rg.replace('район ',''), n, deliv, named, cw.get('OSM',0), cw.get('регистър',0), cw.get('в2',0), nn))
        T=[T[0]+n,T[1]+deliv,T[2]+named,T[3]+cw.get('OSM',0),T[4]+cw.get('регистър',0),T[5]+cw.get('в2',0)]
    TN=sum(noname.values())
    print('| **%s** | **всички** | **%d** | **%d** | **%d (%d / %d / %d)** | **%d** |' % (cls,T[0],T[1],T[2],T[3],T[4],T[5],TN))
    for l in lines: print(l)
