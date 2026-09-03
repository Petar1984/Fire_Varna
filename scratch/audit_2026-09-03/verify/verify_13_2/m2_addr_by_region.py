# -*- coding: utf-8 -*-
"""M2: покритие на КАИС сградите с адрес ПО РАЙОН (черновата дава само глобалните 52,89 %).
READ-ONLY. Изход: m2_addr_by_region.json"""
import json, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open(r"C:/git/varna_3d/web/varna_buildings_info.json", encoding='utf-8'))
cols = d['columns']; ci = {c:i for i,c in enumerate(cols)}
DR = d['dict']
def val(row, col):
    v = row[ci[col]]
    if col in DR:
        return None if v == -1 else DR[col][v]
    return v
agg = collections.defaultdict(lambda: {"buildings":0,"with_addr":0,"with_street":0,"with_num":0})
tot = {"buildings":0,"with_addr":0,"with_street":0,"with_num":0}
for row in d['rows']:
    reg = val(row,'reg') or "(без район)"
    a = agg[reg]; a["buildings"] += 1; tot["buildings"] += 1
    if val(row,'addr'):   a["with_addr"] += 1;   tot["with_addr"] += 1
    if val(row,'street'): a["with_street"] += 1; tot["with_street"] += 1
    if val(row,'num'):    a["with_num"] += 1;    tot["with_num"] += 1
print(f"{'район':28s} {'сгради':>7s} {'адрес':>7s} {'%':>6s} {'улица':>7s} {'%':>6s} {'НОМЕР':>7s} {'%':>6s}")
rows = sorted(agg.items(), key=lambda kv:-kv[1]['buildings'])
for reg,a in rows:
    b=a['buildings']
    print(f"{reg:28s} {b:7d} {a['with_addr']:7d} {100*a['with_addr']/b:5.1f}% {a['with_street']:7d} {100*a['with_street']/b:5.1f}% {a['with_num']:7d} {100*a['with_num']/b:5.1f}%")
b=tot['buildings']
print(f"{'ОБЩО':28s} {b:7d} {tot['with_addr']:7d} {100*tot['with_addr']/b:5.1f}% {tot['with_street']:7d} {100*tot['with_street']/b:5.1f}% {tot['with_num']:7d} {100*tot['with_num']/b:5.1f}%")
json.dump({"total":tot,"by_region":dict(agg)}, open("m2_addr_by_region.json","w",encoding='utf-8'), ensure_ascii=False, indent=1)
