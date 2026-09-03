import json,collections
d=json.load(open(r'C:/git/Fire_Varna/data/search_index.json',encoding='utf-8'))
E=d['entries']
c=collections.Counter(x.get('label','').split('|')[0] for x in E)
pat=['korpil','шкорп','herman','german','ерман']
for k in sorted(c):
    if any(p in k for p in pat): print('улица:',repr(k),c[k])
print('---')
for x in E:
    l=x.get('label','')
    if 'korpil' in l or 'шкорп' in l: print(l,x['pin'],x['kind'])
