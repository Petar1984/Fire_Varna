# -*- coding: utf-8 -*-
"""Порт на norm()/skel() от index.html:4838-4839 → може ли кирилска заявка да намери
   латински етикет (т.е. проблемът само в ПОКАЗА ли е, или и в намирането)."""
import json, re, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
FV="C:/git/Fire_Varna/"
si=json.load(open(FV+"data/search_index.json",encoding="utf-8")); E=si["entries"]

C={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'}
def norm(s):
    s=str(s or "").lower().replace("блок","бл").replace("вход","вх")
    s=re.sub(r"[.№,'\"\-]"," ",s); return re.sub(r"\s+"," ",s).strip()
def skel(w):
    w=w.lower(); o="".join(C.get(ch,ch) for ch in w)
    o=re.sub(r"[yj]","i",o); return re.sub(r"(\D)\1+",r"\1",o)

# 1) целият речник е ли на латиница
CYR=set("абвгдежзийклмнопрстуфхцчшщъьюя")
vocab=set(si["vocab"])
print("vocab с кирилски знак =", sum(1 for t in vocab if any(ch in CYR for ch in t)), "от", len(vocab))

# 2) tk на записа с латински етикет носи ли името на улицата?
def toks_of(e):
    t=[]
    for f in ("tk","qtk","alias_tk","dtk","stk"): t += (e.get(f) or [])
    return t

def label_tokens(lab):
    return [skel(x) for x in norm(str(lab).replace("|"," ")).split() if x]

miss=collections.Counter(); ex=[]
for e in E:
    lab=e.get("label")
    if not lab: continue
    lt=[t for t in label_tokens(lab) if not t.isdigit()]
    if not lt: continue
    have=set(toks_of(e))
    missing=[t for t in lt if t not in have]
    miss["label_entries"]+=1
    if missing:
        miss["with_missing"]+=1
        if len(ex)<8: ex.append((lab, lt, sorted(have), missing))
print("записи с label =",miss["label_entries"],"; от тях с НЕиндексирана дума от етикета =",miss["with_missing"])
for x in ex: print("   ",x)

# 3) конкретно: намира ли се „атанас далчев 1"
q="атанас далчев 1"
qt=[skel(x) for x in norm(q).split()]
print("\nзаявка",q,"→ токени",qt)
hits=[]
for i,e in enumerate(E):
    have=set(toks_of(e))
    if all(any(v==t or v.startswith(t) for v in have) for t in qt): hits.append(i)
print("  записи, чиито токени покриват ВСИЧКИ токени на заявката:",len(hits), hits[:5])
for i in hits[:3]: print("   ",json.dumps(E[i],ensure_ascii=False))

# 4) обратно: кирилска заявка срещу кирилски етикет — контрола
q2="владимир василев 2"
qt2=[skel(x) for x in norm(q2).split()]
h2=[i for i,e in enumerate(E) if all(any(v==t or v.startswith(t) for v in set(toks_of(e))) for t in qt2)]
print("заявка",q2,"→",qt2,"; покриващи записи:",len(h2))
