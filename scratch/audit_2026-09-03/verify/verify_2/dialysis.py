import json
d=json.load(open(r'C:/git/Fire_Varna/data/search_index.json',encoding='utf-8'))
E=d['entries']
def look(street,num):
    r=[x for x in E if x.get('label','').startswith(street) ]
    exact=[x for x in r if x.get('label','').split('|')[-1]==num]
    print('%-22s | улица общо %4d | с №%s: %d' % (street,len(r),num,len(exact)))
    for x in exact[:4]: print('      ',x.get('label',''),x['pin'],x['kind'])
# 16 ДЦ Виртус Медикал – ул. Херман Шкорпил 6
look('herman skorpil','6')
look('german skorpil','6')
# 17 ДЦ проф. Ненов – пл. Съборни 40
look('saborni','40')
look('sabroni','40')
# 18 ДЦ Хипократ – ул. Дубровник 58
look('dubrovnik','58')
print()
print('--- всички улици, съдържащи skorpil / saborni / dubrovnik ---')
import collections
c=collections.Counter(x.get('label','').split('|')[0] for x in E)
for k in sorted(c):
    if 'skorpil' in k or 'sabor' in k or 'dubrovnik' in k: print('  ',k,c[k])
