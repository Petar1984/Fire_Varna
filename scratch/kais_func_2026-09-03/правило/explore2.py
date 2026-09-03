import json, collections
G='C:/git/'
info=json.load(open(G+'varna_3d/web/varna_buildings_info.json',encoding='utf-8'))
cnt=collections.Counter(r[1] for r in info['rows'])
print('--- func counts (all Varna) ---')
for i,f in enumerate(info['dict']['func']):
    print(f'{cnt.get(i,0):6d}  {i:2d}  {f}')
print()
print('reg dict', info['dict']['reg'])
print('prop dict', info['dict']['prop'])
print('note', info.get('note'))
print('address_model', info.get('address_model'))
