import json, collections
G='C:/git/'
p=json.load(open(G+'Fire_Varna/data/places.json',encoding='utf-8'))['places']
h=json.load(open(G+'Fire_Varna/data/hotels.json',encoding='utf-8'))['hotels']
print('n places', len(p), 'n hotels', len(h))
print('place keys union', sorted({k for r in p for k in r}))
print('hotel keys union', sorted({k for r in h for k in r}))
for r in p[:4]: print(json.dumps(r,ensure_ascii=False))
print('...')
for r in h[:3]: print(json.dumps(r,ensure_ascii=False))
print()
print('place src', collections.Counter(r.get('src') for r in p))
print('place status', collections.Counter(r.get('status') for r in p))
print('place kind', collections.Counter(r.get('kind') for r in p))
print('hotel src', collections.Counter(r.get('src') for r in h).most_common(20))
print('hotel kind', collections.Counter(r.get('kind') for r in h))
