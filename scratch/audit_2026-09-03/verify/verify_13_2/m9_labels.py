# -*- coding: utf-8 -*-
"""M9: пълната верига на етикета (index.html:4878 baseAddressLabel @ HEAD 6460961):
label -> address_rows[display_id].normalized_address -> district. READ-ONLY."""
import json, sys, re, collections
sys.stdout.reconfigure(encoding='utf-8')
D = json.load(open(r"C:/git/Fire_Varna/data/search_index.json", encoding='utf-8'))
AR = json.load(open(r"C:/git/Fire_Varna/data/address_rows.json", encoding='utf-8'))
E = D['entries']; DN = D['district_names']
order = AR['field_order']; rows = AR['rows']
ina = order.index('normalized_address')
def pretty(s): return re.sub(r'\s+', ' ', str(s).replace('|', ' ')).strip()
def base(e):
    if e.get('label'): return pretty(e['label'])
    di = e.get('display_id')
    if di is not None and di < len(rows):
        na = rows[di][ina]
        if na: return na
    if e.get('d') is not None and e['d'] < len(DN): return DN[e['d']]
    return '(адрес)'
labs = [base(e) for e in E]
src = collections.Counter('label' if e.get('label') else ('rows' if (e.get('display_id') is not None and e['display_id']<len(rows) and rows[e['display_id']][ina]) else 'район') for e in E)
print("източник на етикета:", src.most_common(), "| черновата: label 43 133 / rows 43 097 / район 2")
nod = sum(1 for s in labs if not re.search(r'[0-9]', s))
print("без нито една цифра:", nod, f"({100*nod/len(E):.0f}%)", "| черновата: 35 273 (41 %)")
gv = sum(1 for s in labs if s.lower().replace('.','').replace(',','').startswith('гр варна район'))
print("започващи с 'гр варна район':", gv, "| черновата: 23 113")
c = collections.Counter(labs)
print("уникални етикети:", len(c), "| черновата: 25 344")
print("топ 3:", c.most_common(3))
lat = re.compile(r'[a-z]', re.I); cyr = re.compile(r'[\u0400-\u04FF]')
ul = sum(1 for s in c if lat.search(s) and not cyr.search(s))
print("уникални етикети САМО на латиница:", ul, "| черновата: 13 683")
