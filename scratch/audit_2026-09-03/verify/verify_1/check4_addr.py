# -*- coding: utf-8 -*-
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
def key(pat):
    hits=[r for r in rows if re.fullmatch(pat, r[0], re.I)]
    if not hits: return None
    la=sum(r[1] for r in hits)/len(hits); lo=sum(r[2] for r in hits)/len(hits)
    return (la,lo,len(hits))
for pat in [r'бул република 91', r'.*мануш войвода.*', r'.*народни будители.*', r'.*херман шкорпил.*', r'.*дубровник 58', r'.*съборни 40', r'.*христо попович 18']:
    print(pat, '->', key(pat))
kard=(43.213541,27.91808)
r91=key(r'бул република 91')
print('d(Кардиолайф пин, бул република 91) = %.1f m' % hav(kard,(r91[0],r91[1])))
print('d(Кардиолайф пин, i=9626 пин на Елеонора) = %.1f m' % hav(kard,(43.231009,27.878521)))
disp=[p for p in places if 'Диспансер' in p['name']][0]
mv=key(r'.*мануш войвода.*')
if mv: print('d(Диспансер пин, мануш войвода) = %.1f m' % hav((disp['lat'],disp['lon']),(mv[0],mv[1])))
ir=[p for p in places if 'Иван Рилски' in p['name']][0]
nb=key(r'.*народни будители.*')
if nb: print('d(II ДКЦ Св. Иван Рилски, народни будители) = %.1f m' % hav((ir['lat'],ir['lon']),(nb[0],nb[1])))
