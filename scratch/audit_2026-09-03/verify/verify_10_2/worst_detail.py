# -*- coding: utf-8 -*-
"""Detail on the genuinely-far cases + on the 11 'wrong func' ones. Read-only."""
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
OUT = r"C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/audit_2026-09-03/verify_10_2"

pip = json.load(open(OUT + "/pip_independent.json", encoding="utf-8"))
sev = {r["name"]: r for r in json.load(open(OUT + "/severity_rows.json", encoding="utf-8"))}

print("=== 62-те „вън“: най-близкото КАИС тяло ИЗОБЩО (не само с вярна функция) ===")
out = [r for r in pip["places"] if r["verdict"] == "вън"]
out.sort(key=lambda r: -sev[r["name"]]["d_to_right_func_m"]
         if sev[r["name"]]["d_to_right_func_m"] is not None else 1e9)
for r in out[:12]:
    s = sev[r["name"]]
    print("  %-42s | до ЛЮБО тяло %5.1f m (%s) | до ВЯРНАТА функция %s m"
          % (r["name"][:42], r["nearest_m"], r["nearest_func"][:28], s["d_to_right_func_m"]))

print("\n=== разпределение: до ЛЮБО тяло (62-те вън) ===")
from collections import Counter
def b(d):
    return "0-5" if d <= 5 else "5-10" if d <= 10 else "10-20" if d <= 20 else "20-50" if d <= 50 else ">50"
print(dict(sorted(Counter(b(r["nearest_m"]) for r in out).items())))
print("макс до ЛЮБО тяло: %.1f m" % max(r["nearest_m"] for r in out))

print("\n=== 12-те хотела „вън“ ===")
for r in sorted(pip["hotels"], key=lambda r: -r["nearest_m"]):
    print("  %6.1f m  %-40s  %s" % (r["nearest_m"], str(r["name"])[:40], r["nearest_func"][:30]))

print("\n=== ГЕЙТЪТ „ляга върху тяло“ — кого пропуска и кого спира ===")
allr = list(sev.values())
pass_gate = [r for r in allr if r["pip"] in ("съвпада", "друга функция")]
fail_gate = [r for r in allr if r["pip"] == "вън"]
bad = lambda r: (r["d_to_right_func_m"] is None) or r["d_to_right_func_m"] > 60
print("минават гейта, но са >60 m от вярно тяло (лъжливо ГОДНО): %d"
      % sum(1 for r in pass_gate if bad(r)))
for r in pass_gate:
    if bad(r):
        print("    -> %-44s %s  d=%s" % (r["name"][:44], r["kind"], r["d_to_right_func_m"]))
print("падат на гейта, но са ≤10 m от вярно тяло (лъжливо НЕГОДНО): %d"
      % sum(1 for r in fail_gate if r["d_to_right_func_m"] is not None and r["d_to_right_func_m"] <= 10))
print("падат на гейта И са >60 m (истински дефект): %d"
      % sum(1 for r in fail_gate if bad(r)))
