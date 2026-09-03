# -*- coding: utf-8 -*-
"""Оборител №1 / находка №7 — независимо преброяване на азбуките в показаните адресни етикети.
Възпроизвежда веригата от index.html:baseAddressLabel/formatAddressHit:
  (1) label -> prettyKey(label)   (2) display_id -> address_rows[..].normalized_address
  (3) d -> district_names[d]      (4) '(адрес)'
+ ' · вх. <en>' САМО когато kind=='mf' и en!=null (това е разлика спрямо check_A5.py!)
"""
import json, collections, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
FV = "C:/git/Fire_Varna/"
si = json.load(open(FV+"data/search_index.json", encoding="utf-8"))
E = si["entries"]; DN = si["district_names"]
payload = json.load(open(FV+"data/address_rows.json", encoding="utf-8"))
order = payload["field_order"]; NA = order.index("normalized_address")
rows = payload["rows"]

CYR = set("абвгдежзийклмнопрстуфхцчшщъьюяѝ")
LAT = set("abcdefghijklmnopqrstuvwxyz")
def cls(s):
    t = s.lower(); c = any(ch in CYR for ch in t); l = any(ch in LAT for ch in t)
    return "mixed" if (c and l) else "cyr" if c else "lat" if l else "none"

def pretty(s): return " ".join(str(s).replace("|"," ").split())

src = collections.Counter(); shown = []
both = 0
for e in E:
    if e.get("label") is not None:
        base = pretty(e["label"]); src["label"] += 1
        if e.get("display_id") is not None: both += 1
    elif e.get("display_id") is not None:
        base = rows[e["display_id"]][NA]; src["rows"] += 1
    elif e.get("d") is not None:
        base = DN[e["d"]]; src["district"] += 1
    else:
        base = "(адрес)"; src["none"] += 1
    # верният код: суфикс само за kind 'mf'
    if e.get("kind") == "mf" and e.get("en") is not None:
        s = base + " · вх. " + str(e["en"])
    else:
        s = base
    shown.append((s, base, e))

print("entries              =", len(E))
print("label_source         =", dict(src))
print("label И display_id   =", both, "  <-- ако е 0: няма кирилски дубльор за етикетите с label")
ab = collections.Counter(cls(s) for s, b, e in shown)
print("azbuka(записи)       =", dict(ab))
print("  lat дял            = %.2f%%" % (100.0*ab["lat"]/len(E)))
print("  lat+mixed дял      = %.2f%%" % (100.0*(ab["lat"]+ab["mixed"])/len(E)))
uniq = set(s for s, b, e in shown)
print("уникални показани    =", len(uniq))
abu = collections.Counter(cls(s) for s in uniq)
print("azbuka(уникални)     =", dict(abu))
# азбука само по base (без вх.)
ubase = set(b for s, b, e in shown)
print("уникални base        =", len(ubase), dict(collections.Counter(cls(b) for b in ubase)))
# address_rows кирилица?
abr = collections.Counter(cls(r[NA]) for r in rows if r[NA])
print("address_rows(%d)   =" % len(rows), dict(abr))
# кой kind носи латиницата
kk = collections.Counter((e.get("kind"), cls(s)) for s, b, e in shown)
print("kind x azbuka        =", dict(kk))
