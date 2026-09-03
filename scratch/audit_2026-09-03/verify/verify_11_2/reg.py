# -*- coding: utf-8 -*-
"""Разчита таблиците в sol_lechebni.txt (първото копие) и брои видовете."""
import io, re, sys, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p=r'C:\git\varna_3d\scratch\refactor\_addr\sol_lechebni.txt'
lines=io.open(p,encoding='utf-8').read().split('\n')
rows={}
for ln in lines:
    m=re.match(r'^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|', ln)
    if m:
        no=int(m.group(1))
        if no in rows: continue           # първото копие води
        rows[no]=(m.group(2), m.group(3).strip(), m.group(4).strip())
print('редове в регистъра:', len(rows), 'min/max', min(rows), max(rows))
import collections
print(collections.Counter(v[1] for v in rows.values()))
print('МЦ на брой:', sum(1 for v in rows.values() if v[1]=='МЦ'))
json.dump({str(k):v for k,v in rows.items()}, io.open(r'C:\Users\Petar\AppData\Local\Temp\claude\C--git\fb0c0608-7fdb-4635-a8fc-44575d26700a\scratchpad\audit_2026-09-03\verify_11_2\reg_rows.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
for no in (9,43,56,68):
    print(no, rows[no])
