import json, math
def hav(a,b,c,d):
    R=6371008.8
    p1,p2=math.radians(a),math.radians(c)
    dp=math.radians(c-a); dl=math.radians(d-b)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(h))
P=json.load(open(r'C:/git/Fire_Varna/data/places.json',encoding='utf-8'))['places']
by={}
for x in P: by.setdefault(x['name'],[]).append(x)
def g(sub):
    for x in P:
        if sub in x['name']: return x
    return None
k=g('Кардиолайф'); v=g('кардиология Варна'); e=g('Царица Елеонора')
print('Кардиолайф   ', k['lat'], k['lon'])
print('СБАЛК Варна  ', v['lat'], v['lon'])
print('Цар.Елеонора ', e['lat'], e['lon'])
print('d(Кардиолайф, СБАЛК Варна) = %.1f m' % hav(k['lat'],k['lon'],v['lat'],v['lon']))
print('d(Кардиолайф, Цар.Елеонора[=МК Младост-прокси]) = %.1f m' % hav(k['lat'],k['lon'],e['lat'],e['lon']))
