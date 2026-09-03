# -*- coding: utf-8 -*-
"""Section 1: class x district matrix (parcels / delivered / named candidates / unnamed)."""
import json, sys, io
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
B='C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/kais_func_2026-09-03/'
P=json.load(open(B+'парцели/plots_by_func.json',encoding='utf-8'))['plots']
CL=['детско заведение','образование','здравно заведение','хотел','курортна/туристическа','общежитие','социални грижи']
REGS=['район Владислав Варненчик','район Приморски','район Младост','район Одесос','район Аспарухово']
def regof(pl):
    r=pl.get('reg') or []
    r=[x for x in r if x]
    return r[0] if r else '—'
tot=defaultdict(lambda: defaultdict(lambda: [0,0,0,0]))
for cls in CL:
    for pl in P[cls]['link_45m']:
        rg=regof(pl)
        cell=tot[cls][rg]
        cell[0]+=1
        if pl.get('delivered'): cell[1]+=1
        elif pl.get('name'): cell[2]+=1
        else: cell[3]+=1
print('| клас | район | КАИС парцели | доставени | кандидати С ИМЕ | кандидати БЕЗ ИМЕ |')
print('|---|---|---:|---:|---:|---:|')
for cls in CL:
    rows=sorted(tot[cls].items(), key=lambda kv: (REGS.index(kv[0]) if kv[0] in REGS else 9))
    s=[0,0,0,0]
    for rg,c in rows:
        for k in range(4): s[k]+=c[k]
    print('| **%s** | **всички** | **%d** | **%d** | **%d** | **%d** |' % (cls,*s))
    for rg,c in rows:
        print('| %s | %s | %d | %d | %d | %d |' % ('', rg.replace('район ',''), *c))
