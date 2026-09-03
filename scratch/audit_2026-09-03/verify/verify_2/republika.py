import json, math
def hav(a,b,c,d):
    R=6371008.8
    p1,p2=math.radians(a),math.radians(c)
    dp=math.radians(c-a); dl=math.radians(d-b)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(h))
d=json.load(open(r'C:/git/Fire_Varna/data/search_index.json',encoding='utf-8'))
hits=[x for x in d['entries'] if 'republika' in x.get('label','') or 'република' in x.get('label','')]
print('entries with republika:',len(hits))
n15=[x for x in hits if x['label'].split('|')[-1]=='15']
print('republika + номер 15:',len(n15))
for x in n15[:20]: print('  ',x['label'],x['pin'],x['kind'])
E=(43.231009,27.878521)  # Хоспис Царица Елеонора, доставен пин
for x in n15[:20]:
    print('   d(Елеонора, %s) = %.1f m'%(x['label'], hav(E[0],E[1],x['pin'][0],x['pin'][1])))
