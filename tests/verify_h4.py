import json, hashlib, collections, subprocess
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest().upper()
def ok(c): return 'PASS' if c else '***FAIL***'
H='data/hydrants.json'; P='data/hydrants_provenance.json'; FQ='docs/audits/h2_kmz_flag_queue.json'
d=json.load(open(H,encoding='utf-8')); p=json.load(open(P,encoding='utf-8')); fq=json.load(open(FQ,encoding='utf-8'))
etr=[o for o in d if str(o.get('origin','')).startswith('etr_')]; nonetr=len(d)-len(etr); ids=[o['id'] for o in d]
dupleg=[o['id'] for o in d if o.get('legacy_ids') and len(o['legacy_ids'])!=len(set(o['legacy_ids']))]
upd=[o for o in d if not str(o.get('origin','')).startswith('etr_') and any(str(x).startswith('etr_') for x in (o.get('legacy_ids') or []))]
print('hydrants count 7217 :',len(d),ok(len(d)==7217))
print('hydrants sha 9E4FCB37:',sha(H)[:8],ok(sha(H).startswith('9E4FCB37')))
print('originals intact 5911:',nonetr,ok(nonetr==5911))
print('etr ADDs 1306       :',len(etr),ok(len(etr)==1306))
print('ADD shape exact     :',ok(all(set(o)=={'id','coords','origin','legacy_ids'} for o in etr)))
print('no duplicate ids    :',ok(len(ids)==len(set(ids))))
print('no dup legacy_ids   :',ok(not dupleg),dupleg[:3])
print('UPDATE targets ~3166:',len(upd))
print('prov keys 7217      :',len(p),ok(len(p)==7217))
print('prov sha 13D49812   :',sha(P)[:8],ok(sha(P).startswith('13D49812')))
ma=collections.Counter(r.get('merge_action') for v in p.values() for r in v.get('source_refs',[]))
print('prov add1306 upd3170:',ma.get('kmz_etr_add'),ma.get('kmz_etr_update'),ok(ma.get('kmz_etr_add')==1306 and ma.get('kmz_etr_update')==3170))
flags=fq if isinstance(fq,list) else (fq.get('flags') or next((v for v in fq.values() if isinstance(v,list)),[]))
print('FLAG queue 317      :',len(flags),ok(len(flags)==317))
for f in (H,P):
    o=subprocess.run(['git','show','HEAD:'+f],capture_output=True)
    try: print('committed HEAD',f,len(json.loads(o.stdout.decode('utf-8'))),ok(len(json.loads(o.stdout.decode('utf-8')))==7217))
    except Exception as e: print('committed HEAD',f,'ERROR',str(e)[:60])
