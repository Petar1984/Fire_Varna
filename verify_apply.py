import json, hashlib, collections, subprocess
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest().upper()
def ok(c): return 'PASS' if c else '***FAIL***'
H='data/hydrants.json'; P='data/hydrants_provenance.json'
d=json.load(open(H,encoding='utf-8')); p=json.load(open(P,encoding='utf-8'))
ids=[o['id'] for o in d]; orig=collections.Counter(o.get('origin') for o in d)
dupleg=[o['id'] for o in d if o.get('legacy_ids') and len(o['legacy_ids'])!=len(set(o['legacy_ids']))]
print('hydrants count 7238 :',len(d),ok(len(d)==7238))
print('hydrants sha 89AD7559:',sha(H)[:8],ok(sha(H).startswith('89AD7559')))
print('prov keys 7238      :',len(p),ok(len(p)==7238))
print('prov sha 7E83EF1A   :',sha(P)[:8],ok(sha(P).startswith('7E83EF1A')))
print('ids == prov keys    :',ok(set(ids)==set(p.keys())))
print('no duplicate ids    :',ok(len(ids)==len(set(ids))))
print('no dup legacy_ids   :',ok(not dupleg))
print('field_report = 45   :',orig.get('field_report'),ok(orig.get('field_report')==45))
print('etr_* = 1306        :',sum(v for k,v in orig.items() if str(k).startswith('etr_')),ok(sum(v for k,v in orig.items() if str(k).startswith('etr_'))==1306))
print('vik/national        :',orig.get('vik'),orig.get('national'),ok(orig.get('vik')==3542 and orig.get('national')==2345))
for f in (H,P):
    o=subprocess.run(['git','show','HEAD:'+f],capture_output=True)
    try: print('committed HEAD',f,len(json.loads(o.stdout.decode('utf-8'))),ok(len(json.loads(o.stdout.decode('utf-8')))==7238))
    except Exception as e: print('committed HEAD',f,'ERROR',str(e)[:60])
