# -*- coding: utf-8 -*-
"""M8: реплика на dedupeDisplayRows ключа (index.html:5104 @ HEAD 6460961):
key = norm(label) + '||' + (g != null ? g : '').  Колко ключа събират >1 запис и на какво разстояние.
READ-ONLY. Изход: m8_dedupe.json"""
import json, sys, math, collections, re
sys.stdout.reconfigure(encoding='utf-8')
D = json.load(open(r"C:/git/Fire_Varna/data/search_index.json", encoding='utf-8'))
E = D['entries']; DN = D['district_names']
def pretty(s): return re.sub(r'\s+', ' ', str(s).replace('|', ' ')).strip()
def base(e):
    if e.get('label'): return pretty(e['label'])
    if e.get('d') is not None and e['d'] < len(DN): return DN[e['d']]
    return '(адрес)'
def fmt(e):
    b = base(e)
    return b + ' · вх. ' + str(e['en']) if (e.get('kind') == 'mf' and e.get('en') is not None) else b
def norm(s): return re.sub(r'\s+', ' ', str(s).lower().strip())
g = collections.defaultdict(list)
for e in E:
    g[(norm(fmt(e)), str(e['g']) if e.get('g') is not None else '')].append(e)
multi = {k: v for k, v in g.items() if len(v) > 1}
print("ключове с >1 запис:", len(multi), "| черновата: 9 053")
print("записи в тях:", sum(len(v) for v in multi.values()), "| черновата: 67 357")
def hav(a,b,c,d):
    R=6371000.0; p=math.pi/180
    z=math.sin((c-a)*p/2)**2+math.cos(a*p)*math.cos(c*p)*math.sin((d-b)*p/2)**2
    return 2*R*math.asin(math.sqrt(z))
hist = collections.Counter(); worst = []
for k, v in multi.items():
    pins = [tuple(x['pin']) for x in v]
    mx = 0.0
    if len(set(pins)) > 1:
        for i in range(len(pins)):
            for j in range(i+1, len(pins)):
                mx = max(mx, hav(pins[i][0], pins[i][1], pins[j][0], pins[j][1]))
                if len(pins) > 60: break
            if len(pins) > 60: break
    b = '0 (същ пин)' if mx == 0 else ('<50 m' if mx < 50 else ('50-200 m' if mx < 200 else '>200 m'))
    hist[b] += 1
    if mx > 200: worst.append((round(mx), k[0], len(v)))
for k in ['0 (същ пин)', '<50 m', '50-200 m', '>200 m']:
    print(f"  {k:14s} {hist.get(k,0):6d}")
print("| черновата: 545 ключа на >200 m, 662 на 50-200 m")
worst.sort(reverse=True)
for w in worst[:6]: print("  ", w[0], "m ·", w[2], "пина ·", w[1][:60])
json.dump({"multi_keys": len(multi), "rows": sum(len(v) for v in multi.values()),
           "hist": dict(hist), "worst": worst[:60]},
          open("m8_dedupe.json","w",encoding='utf-8'), ensure_ascii=False, indent=1)
