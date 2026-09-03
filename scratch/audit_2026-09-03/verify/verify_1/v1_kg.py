# -*- coding: utf-8 -*-
"""ОБОРИТЕЛ №1 · находка №4 — независима проверка на:
   (1) 53 регистрови общински ДГ
   (2) колко от тях са покрити от 46-те доставени реда
   (3) разбивката на 46-те реда по вид
   (4) 7-те „еднозначен двор" сред липсващите в града
READ-ONLY. Пише само в собствената си папка.
"""
from __future__ import annotations
import json, re, sys, math, unicodedata
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FV = Path("C:/git/Fire_Varna")
V3 = Path("C:/git/varna_3d")
OUT = Path(__file__).resolve().parent

# ---------- 1. регистърът, дословно от преписа ----------
src = (V3 / "scratch/refactor/_addr/kimi_obrazovanie.txt").read_text(encoding="utf-8").splitlines()
reg_lines = src[405:458]          # 1-based 406..458
reg = []
for ln in reg_lines:
    parts = ln.split("|")
    assert len(parts) == 5, ln
    m = re.match(r"ДГ\s*№\s*(\d+)", parts[0])
    reg.append({"no": int(m.group(1)), "name": parts[0].strip(),
                "addr": parts[1].strip(), "rajon": parts[2].strip()})
print("регистрови реда 406–458:", len(reg), "· уникални номера:", len(set(r['no'] for r in reg)),
      "· min/max:", min(r['no'] for r in reg), max(r['no'] for r in reg))

# ---------- 2. доставените ----------
pl = json.loads((FV / "data/places.json").read_text(encoding="utf-8"))
kg = [p for p in pl["places"] if p["kind"] == "детска градина"]
print("доставени под клас „детска градина“:", len(kg))

def core(s: str) -> str:
    """скелет: сваля вида, номерата, пунктуацията, малки букви, без интервали"""
    s = s.lower().replace("ё", "е")
    s = re.sub(r"/[^/]*/", " ", s)          # „/с яслена група/", „/със специални групи/"
    s = re.sub(r"\([^)]*\)", " ", s)        # „(филиал)"
    s = re.sub(r"[\"“”„»«'`]", " ", s)
    for w in ("оздравителна", "логопедична", "детска градина", "детска ясла", "детско заведение",
              "детска", "градина", "ясла", "филиал", "цдг", "чдг", "одз", "одг", "дг", "дя",
              "с яг", "яг"):
        s = s.replace(w, " ")
    s = re.sub(r"[^а-я ]", " ", s)
    return re.sub(r"\s+", "", s)

def num(s: str):
    m = re.search(r"(?:№\s*|\b)(\d{1,2})\b", s)
    return int(m.group(1)) if m else None

reg_core = {}
for r in reg:
    reg_core.setdefault(core(r["name"]), []).append(r)

# --- независимо съпоставяне: 1) по СКЕЛЕТ на името  2) по НОМЕР, ако няма име
covered, rows_muni, unmatched, nursery, private = {}, [], [], [], []
for p in kg:
    nm = p["name"]
    low = nm.lower()
    if "ясла" in low or re.match(r"^\s*дя\b", low) or "дя " in low.replace("(", " ").replace(")", " "):
        nursery.append(nm); continue
    if low.startswith("чдг") or "част" in low:
        private.append(nm); continue
    c = core(nm)
    hit = reg_core.get(c)
    if hit and len(hit) == 1:
        r = hit[0]
        covered.setdefault(r["no"], []).append(nm)
        rows_muni.append((nm, r["no"], "по име"))
        continue
    n = num(nm)
    cand = [r for r in reg if r["no"] == n] if n else []
    if cand:
        covered.setdefault(n, []).append(nm)
        rows_muni.append((nm, n, "по номер (име не съвпада)"))
    else:
        unmatched.append(nm)

print()
print("МОЯТА разбивка на 46-те:")
print("  редове-общински ДГ :", len(rows_muni))
print("  ясли               :", len(nursery), nursery)
print("  частни             :", len(private), private)
print("  без съответник     :", len(unmatched), unmatched)
print("  СБОР               :", len(rows_muni)+len(nursery)+len(private)+len(unmatched))
print()
print("уникални покрити регистрови ДГ:", len(covered))
dup = {k: v for k, v in covered.items() if len(v) > 1}
print("регистрови ДГ с >1 доставен ред:", dup)
missing = sorted(r["no"] for r in reg if r["no"] not in covered)
print("ЛИПСВАЩИ (номера):", missing, "· брой:", len(missing))
print("ПОКРИТИЕ: %d/%d = %.1f %%" % (len(covered), len(reg), 100.0*len(covered)/len(reg)))

# село?
vill = [r for r in reg if r["no"] in missing and re.search(r"\bс\s*\.", r["addr"])]
print()
print("липсващи с изричен адрес в СЕЛО:", [(r['no'], r['addr']) for r in vill])
no_settlement = [r for r in reg if r["no"] in missing and "варна" not in r["addr"].lower()
                 and not re.search(r"\bс\s*\.", r["addr"])]
print("липсващи БЕЗ 'гр. Варна' и без 'с.' в адреса:", [(r['no'], r['addr'], 'rajon '+r['rajon']) for r in no_settlement])
json.dump({"missing": missing, "covered": {str(k): v for k, v in covered.items()},
           "rows_muni": rows_muni, "nursery": nursery, "private": private,
           "unmatched": unmatched},
          open(OUT/"v1_match.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
