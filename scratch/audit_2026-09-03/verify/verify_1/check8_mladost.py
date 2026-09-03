# -*- coding: utf-8 -*-
"""Колко регистрови заведения седят на МК „Младост" и колко от тях са на картата."""
import json, re, sys, io, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
src = open(r'C:/git/varna_3d/scratch/refactor/_addr/sol_lechebni.txt', encoding='utf-8').read().splitlines()
rng = list(range(549,567)) + list(range(572,581)) + list(range(679,686)) + list(range(588,675))
hits = []
for i in rng:
    ln = src[i]
    if not ln.startswith('|'): continue
    c = [x.strip() for x in ln.strip('|').split('|')]
    if len(c) < 4: continue
    no, name, typ, addr = c[0], c[1], c[2], c[3]
    if re.search(r'Младост', addr):
        hits.append((no, typ, name, addr))
print('регистрови редове с „Младост" в адреса:', len(hits))
for h in hits: print('  №%-4s %-16s %s   << %s' % h)
places = json.load(open(r'C:/git/Fire_Varna/data/places.json', encoding='utf-8'))['places']
blob = json.dumps(places, ensure_ascii=False).lower()
print()
for no, typ, name, addr in hits:
    core = re.sub(r'[„“"]','',name)
    tok = [w for w in re.findall(r'[А-Яа-яA-Za-z\-]{4,}', core) if w.lower() not in ('еоод','оод','ЕАД'.lower(),'ад','варна','хоспис','специализирана','болница','активно','лечение','медицински','център')]
    ok = any(t.lower() in blob for t in tok)
    print('  №%-4s %-40s на картата: %s   (маркери: %s)' % (no, core[:40], 'ДА' if ok else 'НЕ', ','.join(tok[:3])))
