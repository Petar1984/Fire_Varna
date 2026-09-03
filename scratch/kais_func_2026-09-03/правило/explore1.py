import json, io, sys, collections
G='C:/git/'
info=json.load(open(G+'varna_3d/web/varna_buildings_info.json',encoding='utf-8'))
print('top keys', list(info.keys()))
print('columns', info.get('columns'))
print('dict keys', list(info['dict'].keys()))
for k,v in info['dict'].items():
    print(k, 'len', len(v))
print('rows', len(info['rows']), 'row0', info['rows'][0])
print()
print('--- FUNC DICT ---')
for i,f in enumerate(info['dict']['func']):
    print(i, repr(f))
