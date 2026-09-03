# -*- coding: utf-8 -*-
import sys, json, math, collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
ar=json.load(open(G+'Fire_Varna/data/address_rows.json',encoding='utf-8'))['rows']
print('n address rows', len(ar))
def show(sub, maxn=25):
    hit=[r for r in ar if sub in r[0]]
    keys=collections.Counter(r[0] for r in hit)
    print('  „%s“ → %d реда, %d ключа' % (sub,len(hit),len(keys)))
    for k,n in keys.most_common(maxn): print('      %-52s %d' % (k,n))
for s in ['бл 402','бл 309','бл 21','бл 20','бл 208','шести септември','6 ти септември','ниш','георги минков']:
    show(s, 12)
