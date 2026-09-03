# -*- coding: utf-8 -*-
"""Откъде идва латиницата и възстановима ли е кирилицата (Varna_buildings)."""
import json, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
VB="C:/git/Varna_buildings/output/"
gi=json.load(open(VB+"geocoder_index.json",encoding="utf-8"))["entries"]
pv=json.load(open(VB+"address_provenance.json",encoding="utf-8"))
CYR=set("абвгдежзийклмнопрстуфхцчшщъьюя"); LAT=set("abcdefghijklmnopqrstuvwxyz")
def al(s):
    t=str(s or "").lower(); c=any(ch in CYR for ch in t); l=any(ch in LAT for ch in t)
    return "mixed" if c and l else "cyr" if c else "lat" if l else "none"

lat=[e for e in gi if e.get("addr_key") and al(e["addr_key"]) in ("lat","mixed")]
print("geocoder_index записи =",len(gi),"; с латински/смесен addr_key =",len(lat))

src=collections.Counter(); rec=collections.Counter(); ex=[]
for e in lat:
    cd=e.get("cadnum"); p=pv.get(cd) or {}
    src[p.get("address_source","(няма)")]+=1
    aa=p.get("address_authority") or {}
    alt=aa.get("alternative_value")
    role=aa.get("alternative_role")
    a=al(alt) if alt else "(няма)"
    rec[(a,role)]+=1
    if a=="cyr" and len(ex)<8:
        ex.append((e["addr_key"], aa.get("chosen_value"), alt, aa.get("chosen_source"), aa.get("detection_reason")))
print("\nadress_source за латинските:", src.most_common())
print("\nalternative_value (азбука, роля):")
for k,v in rec.most_common(): print("   ",k,"→",v)
n_cyr=sum(v for (a,r),v in rec.items() if a=="cyr")
print("\nвъзстановими от alternative_value (кирилица) =",n_cyr,"/",len(lat),"= %.1f%%"%(100.0*n_cyr/len(lat)))
print("\nпримери (addr_key | chosen_value | alternative_value | source | reason):")
for x in ex: print("   ",x)

# обратната транслитерация е ли безопасна? (демонстрация)
import re
C={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'}
def skel(w):
    o="".join(C.get(ch,ch) for ch in w.lower()); o=re.sub(r"[yj]","i",o); return re.sub(r"(\D)\1+",r"\1",o)
print("\nskel() е необратим — колизии:")
for a,b in [("Южен","Иужен"),("войвода","воивода"),("Козлодуй","Козлодуи"),("Гълъбец","Галабец")]:
    print("   skel(%s)=%s  skel(%s)=%s  →  %s"%(a,skel(a),b,skel(b),"СЪЩОТО" if skel(a)==skel(b) else "различно"))
json.dump({"gi_entries":len(gi),"latin_addr_key":len(lat),
           "address_source":dict(src),
           "alt_value":{str(k):v for k,v in rec.items()},
           "recoverable_cyr":n_cyr},
          open("C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/audit_2026-09-03/verify_2/v7_source.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
