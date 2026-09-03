# -*- coding: utf-8 -*-
"""Колко информация губи skel-транслитерацията: различни кирилски улици -> един и същ латински етикет."""
import json, collections, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
FV="C:/git/Fire_Varna/"
p=json.load(open(FV+"data/address_rows.json",encoding="utf-8")); o=p["field_order"]
NA=o.index("normalized_address"); rows=p["rows"]
C={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'}
def norm(s):
    s=str(s or '').lower().replace('блок','бл').replace('вход','вх')
    s=re.sub(r"[.№,'\"-]",' ',s); return re.sub(r'\s+',' ',s).strip()
def skel(w):
    w=str(w).lower(); o=''.join(C.get(ch,ch) for ch in w)
    o=re.sub(r'[yj]','i',o); return re.sub(r'(\D)\1+',r'\1',o)
TYPE={'ul','bul','pl'}
def street_key(s):
    toks=[skel(w) for w in norm(s).split(' ') if w]
    toks=[t for t in toks if t]
    while toks and toks[0] in TYPE: toks.pop(0)
    return ' '.join(toks)
# улицата = normalized_address без крайното число
m=collections.defaultdict(set)
for r in rows:
    na=r[NA]
    if not na: continue
    parts=na.split()
    while parts and re.fullmatch(r'\d+[а-яa-z]?', parts[-1].lower()): parts.pop()
    st=' '.join(parts)
    if not st: continue
    m[street_key(st)].add(st)
amb={k:v for k,v in m.items() if len(v)>1}
print("различни улични низа       =", len(set().union(*m.values())))
print("различни латински ключове  =", len(m))
print("ключове с >1 кирилска улица=", len(amb))
tot=sum(len(v) for v in amb.values())
print("кирилски улици, слети в тях=", tot)
for k,v in sorted(amb.items(), key=lambda kv:-len(kv[1]))[:15]:
    print("  %-30s <- %s" % (k, ' | '.join(sorted(v))[:150]))
