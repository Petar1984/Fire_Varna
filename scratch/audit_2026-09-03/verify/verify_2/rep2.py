import json, math
def hav(a,b,c,d):
    R=6371008.8
    p1,p2=math.radians(a),math.radians(c)
    dp=math.radians(c-a); dl=math.radians(d-b)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(h))
E=(43.231009,27.878521)
d=json.load(open(r'C:/git/Fire_Varna/data/search_index.json',encoding='utf-8'))
hits=[x for x in d['entries'] if 'republika' in x.get('label','')]
for x in sorted(hits,key=lambda x:hav(E[0],E[1],x['pin'][0],x['pin'][1]))[:25]:
    print('%7.1f m  %-40s %s %s'%(hav(E[0],E[1],x['pin'][0],x['pin'][1]),x['label'],x['pin'],x['kind']))
