import json, collections
G='C:/git/'
p=json.load(open(G+'Fire_Varna/data/places.json',encoding='utf-8'))
print('places keys', list(p.keys()))
print('meta', json.dumps(p['_meta'], ensure_ascii=False)[:2000])
rows=p['places'] if 'places' in p else None
print('list key candidates', [k for k in p if k!='_meta'])
