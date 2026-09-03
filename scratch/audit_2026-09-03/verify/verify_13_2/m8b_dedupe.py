# -*- coding: utf-8 -*-
"""M8b: реплика на dedupeDisplayRows с ПЪЛНАТА верига на етикета (поправка на m8).
key = norm(formatAddressHit(r)) + '||' + (g ?? ''). READ-ONLY."""
import json, sys, math, collections, re
sys.stdout.reconfigure(encoding='utf-8')
D = json.load(open(r"C:/git/Fire_Varna/data/search_index.json", encoding='utf-8'))
AR = json.load(open(r"C:/git/Fire_Varna/data/address_rows.json", encoding='utf-8'))
E = D['entries']; DN = D['district_names']; rows = AR['rows']; ina = AR['field_order'].index('normalized_address')
def pretty(s): return re.sub(r'\s+', ' ', str(s).replace('|', ' ')).strip()
def base(e):
    if e.get('label'): return pretty(e['label'])
    di = e.get('display_id')
    if di is not None and di < len(rows) and rows[di][ina]: return rows[di][ina]
    if e.get('d') is not None and e['d'] < len(DN): return DN[e['d']]
    return '(адрес)'
def fmt(e):
    b = base(e)
    return b + ' · вх. ' + str(e['en']) if (e.get('kind') == 'mf' and e.get('en') is not None) else b
def norm(s): return re.sub(r'\s+', ' ', str(s).lower().strip())
g = collections.defaultdict(list)
for e in E: g[(norm(fmt(e)), str(e['g']) if e.get('g') is not None else '')].append(e)
multi = {k: v for k, v in g.items() if len(v) > 1}
print("ключове с >1 запис:", len(multi), "| черновата: 9 053")
print("записи в тях:", sum(len(v) for v in multi.values()), "| черновата: 67 357")
def hav(a,b,c,d):
    R=6371000.0; p=math.pi/180
    z=math.sin((c-a)*p/2)**2+math.cos(a*p)*math.cos(c*p)*math.sin((d-b)*p/2)**2
    return 2*R*math.asin(math.sqrt(z))
hist = collections.Counter()
for k, v in multi.items():
    pins = list({tuple(x['pin']) for x in v})
    mx = 0.0
    for i in range(len(pins)):
        for j in range(i+1, len(pins)):
            mx = max(mx, hav(pins[i][0], pins[i][1], pins[j][0], pins[j][1]))
    hist['<5m' if mx < 5 else ('5-50m' if mx < 50 else ('50-200m' if mx < 200 else '>200m'))] += 1
print("хистограма:", dict(hist), "| черновата: <5 232 · 5-50 7614 · 50-200 662 · >200 545")
json.dump({"multi_keys": len(multi), "rows": sum(len(v) for v in multi.values()), "hist": dict(hist)},
          open("m8b_dedupe.json","w",encoding='utf-8'), ensure_ascii=False, indent=1)
