import json
G='C:/git/'
h=json.load(open(G+'Fire_Varna/data/hotels.json',encoding='utf-8'))
print('hotels keys', list(h.keys()))
print(json.dumps(h['_meta'], ensure_ascii=False)[:2500])
