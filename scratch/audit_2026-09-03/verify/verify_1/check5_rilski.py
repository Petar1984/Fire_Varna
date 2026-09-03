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
for p in places:
    if 'Рилски' in p['name']:
        print('PLACE:', p['kind'],'|',p['name'],'|',p['lat'],p['lon'],'|',p['zone'])
from collections import Counter
c=Counter(r[0] for r in rows if 'народни будители' in r[0])
for k,n in sorted(c.items()):
    pts=[(r[1],r[2]) for r in rows if r[0]==k]
    print('  key %-34s n=%-4d %.6f,%.6f' % (k,n,sum(x[0] for x in pts)/n,sum(x[1] for x in pts)/n))
ir=[p for p in places if p['kind']=='ДКЦ' and 'Рилски' in p['name']][0]
nb=[r for r in rows if r[0]=='ул народни будители 5']
if nb:
    la=sum(r[1] for r in nb)/len(nb); lo=sum(r[2] for r in nb)/len(nb)
    print('d(II ДКЦ Св. Иван Рилски, ул народни будители 5) = %.1f m' % hav((ir['lat'],ir['lon']),(la,lo)))
