# -*- coding: utf-8 -*-
import json, math, sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
FV = r'C:/git/Fire_Varna'
rows = json.load(open(FV+'/data/address_rows.json', encoding='utf-8'))['rows']
def hav(a,b):
    R=6371008.8
    la1,lo1,la2,lo2=map(math.radians,[a[0],a[1],b[0],b[1]])
    h=math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
hits=[r for r in rows if re.search(r'republika|република', r[0], re.I)]
print('редове с „република" в ключа:', len(hits))
from collections import Counter
c=Counter(r[0] for r in hits)
for k,n in sorted(c.items())[:60]:
    pts=[(r[1],r[2]) for r in hits if r[0]==k]
    la=sum(p[0] for p in pts)/len(pts); lo=sum(p[1] for p in pts)/len(pts)
    print('  %-40s n=%-4d centroid %.6f,%.6f' % (k,n,la,lo))
