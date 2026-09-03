# -*- coding: utf-8 -*-
"""Вреден ли е „преводът в показа" по КООРДИНАТА: колко пъти кирилският кандидат
на същия пин НЕ е същият адрес (skel(кандидат) != латинския етикет)."""
import json, collections, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
FV="C:/git/Fire_Varna/"
si=json.load(open(FV+"data/search_index.json",encoding="utf-8")); E=si["entries"]
p=json.load(open(FV+"data/address_rows.json",encoding="utf-8")); o=p["field_order"]
NA=o.index("normalized_address"); LA=o.index("lat"); LN=o.index("lng"); rows=p["rows"]
C={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'}
def norm(s):
    s=str(s or '').lower().replace('блок','бл').replace('вход','вх')
    s=re.sub(r"[.№,'\"-]",' ',s); return re.sub(r'\s+',' ',s).strip()
def skel(w):
    w=str(w).lower(); q=''.join(C.get(ch,ch) for ch in w)
    q=re.sub(r'[yj]','i',q); return re.sub(r'(\D)\1+',r'\1',q)
TYPE={'ul','bul','pl'}
def key(s):
    t=[skel(w) for w in norm(s).split(' ') if w]; t=[x for x in t if x]
    while t and t[0] in TYPE: t.pop(0)
    return ' '.join(t)
CYR=set("абвгдежзийклмнопрстуфхцчшщъьюя"); LAT=set("abcdefghijklmnopqrstuvwxyz")
def cls(s):
    t=s.lower(); c=any(ch in CYR for ch in t); l=any(ch in LAT for ch in t)
    return "mixed" if (c and l) else "cyr" if c else "lat" if l else "none"
def pretty(s): return " ".join(str(s).replace("|"," ").split())
rowpin=collections.defaultdict(list)
for r in rows:
    if r[NA]: rowpin[(round(r[LA],5),round(r[LN],5))].append(r[NA])
ok=mis=nocand=0; ex=[]
for e in E:
    if e.get("label") is None: continue
    b=pretty(e["label"])
    if cls(b)!="lat": continue
    pin=e.get("pin"); cands=rowpin.get((round(pin[0],5),round(pin[1],5)),[]) if pin else []
    if not cands: nocand+=1; continue
    if any(key(c)==key(b) for c in cands): ok+=1
    else:
        mis+=1
        if len(ex)<10: ex.append((b,cands[:2]))
tot=ok+mis+nocand
print("латински етикети            =", tot)
print("  кандидат на пина = СЪЩИЯ адрес  =", ok, "(%.1f%%)"%(100.0*ok/tot))
print("  кандидат на пина = ДРУГ адрес   =", mis, "(%.1f%%)"%(100.0*mis/tot))
print("  няма кандидат на пина           =", nocand, "(%.1f%%)"%(100.0*nocand/tot))
for b,c in ex: print("      %-30s -> %s" % (b, c))
