# -*- coding: utf-8 -*-
"""Пре-брой на здравното покритие: кой регистров ред ГО ИМА на картата (по обект, не по име)."""
import json, math, sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
FV = r'C:/git/Fire_Varna'
rows = json.load(open(FV+'/data/address_rows.json', encoding='utf-8'))['rows']
places = json.load(open(FV+'/data/places.json', encoding='utf-8'))['places']
def hav(a,b):
    R=6371008.8
    la1,lo1,la2,lo2=map(math.radians,[a[0],a[1],b[0],b[1]])
    h=math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
def gk(k):
    hits=[r for r in rows if r[0]==k]
    if not hits: return None
    return (sum(r[1] for r in hits)/len(hits), sum(r[2] for r in hits)/len(hits), len(hits))
P = {p['name']: (p['lat'],p['lon'],p['kind']) for p in places}
def find(sub):
    for n,(la,lo,k) in P.items():
        if sub.lower() in n.lower(): return (n,la,lo,k)
    return None
pairs = [
 ('#2 Еврохоспитал', 'Eurohospital', 'ул найден райков 2 а'),
 ('#8 Марко Антонов', 'Марко Антонов', None),
 ('#9 СБАЛПФЗ', 'Диспансер за белодробни', 'ул мануш войвода 11 а'),
 ('#23 ДКЦ Св. Иван Рилски', 'Иван Рилски', 'ул народни будители 5'),
 ('#25 ДКЦ Св. Марина', 'Света Марина', 'бул христо смирненски 1'),
 ('#7 Кардиолайф', 'Кардиолайф', 'бул република 91'),
]
for lbl, sub, key in pairs:
    f = [x for x in [ (n,la,lo,k) for n,(la,lo,k) in P.items() if sub.lower() in n.lower() ] ]
    f = [x for x in f if x[3] in ('болница','ДКЦ','хоспис')]
    if not f:
        print('%-26s НЯМА доставен ред' % lbl); continue
    n,la,lo,k = f[0]
    g = gk(key) if key else None
    d = ('%.1f m' % hav((la,lo),(g[0],g[1]))) if g else ('ключът „%s" липсва' % key if key else '—')
    print('%-26s доставен като „%s" (клас %s) · до регистровия адрес: %s' % (lbl, n, k, d))
print()
# алтернативни ключове за Найден Райков
from collections import Counter
c=Counter(r[0] for r in rows if 'райков' in r[0])
print('ключове „райков":', dict(c))
