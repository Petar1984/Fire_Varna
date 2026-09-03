# -*- coding: utf-8 -*-
"""Builds the markdown fragments for КАНДИДАТИ.md sections 1 and 2 from the
verified measurement outputs. Cadastral numbers are masked (there are none)."""
import json, sys, io, re
from collections import defaultdict, Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
B='C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/kais_func_2026-09-03/'
C=json.load(open(B+'парцели/candidates.json',encoding='utf-8'))
P=json.load(open(B+'парцели/plots_by_func.json',encoding='utf-8'))
cands=C['candidates']

MASK=re.compile(r'\b\d{4,5}\.\d+\.\d+\b')
def m(s): return MASK.sub('10135.xxxx', s or '')
def short(a, n=44):
    a=m(' · '.join(a) if isinstance(a,list) else (a or ''))
    a=a.replace('гр. Варна, район ','').replace('гр. Варна, ','')
    return a[:n] if a else '—'
def reg(r):
    r=' / '.join(r) if isinstance(r,list) else (r or '')
    return r.replace('район ','') or '—'
def src_label(c):
    ch=c.get('channels') or {}
    if c['name_src']=='без име': return 'без име'
    s=c['name_src']
    if s.startswith('б'):
        b=(ch.get('b_osm') or [{}])[0]
        ex=' · ИЗКЛЮЧЕН %s' % (b.get('why_excluded','')[:22]) if b.get('excluded') else ''
        return 'OSM POI %.1f m%s' % (b.get('d_m',0), ex)
    if s.startswith('в2'):
        return 'регистър по УЛИЦА от КАИС addr (геокодът не потвърждава)'
    if s.startswith('в'):
        r=(ch.get('c_reg') or [{}])[0]
        return 'регистър %.0f m · %s' % (r.get('d_m',0), r.get('method',''))
    if s.startswith('а'):
        return 'КАИС addr'
    return s

order=['детско заведение','образование','здравно заведение','хотел','курортна/туристическа','общежитие','социални грижи']
CP={ (43.24473,27.85411):'а', (43.24456,27.84592):'б', (43.24946,27.84414):'в', (43.24709,27.85397):'г' }
def cp_of(c):
    for (la,lo),lbl in CP.items():
        if abs(c['lat']-la)<0.0012 and abs(c['lon']-lo)<0.0012: return lbl
    return ''

out=[]
def row(c, cls):
    return {'клас':cls,'име':c['name'] or 'без име','извор':src_label(c),
            'адрес_КАИС':short(c['addr'],80),'lat':c['lat'],'lon':c['lon'],
            'площ_m2':c['area_m2'],'тела':c['n_bodies'],'ет':c['floors_max'],
            'район':reg(c['reg']),'парцел':c['plot'],'кт':cp_of(c)}
for cls in order:
    for c in cands[cls]:
        out.append(row(c,cls))
json.dump(out,open('candidates_flat.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('кандидати общо:',len(out),Counter(o['клас'] for o in out))

def table(rows, title):
    print()
    print('**%s — %d**' % (title,len(rows)))
    print()
    print('| име | извор на името | КАИС адрес | коорд. | площ m² | тела | ет. | район |')
    print('|---|---|---|---|---:|---:|---:|---|')
    for o in rows:
        print('| %s%s | %s | %s | %.5f,%.5f | %.0f | %d | %d | %s |' % (
            ('**(%s)** ' % o['кт']) if o['кт'] else '', o['име'], o['извор'],
            o['адрес_КАИС'], o['lat'], o['lon'], o['площ_m2'], o['тела'], o['ет'], o['район']))

dz=[o for o in out if o['клас']=='детско заведение']
vv=[o for o in dz if 'Владислав Варненчик' in o['район']]
vv.sort(key=lambda o:(o['кт'] or 'я'))
table(vv,'ВЛАДИСЛАВОВО · детски заведения — кандидати')
rest=[o for o in dz if o not in vv]
rest.sort(key=lambda o:(o['име']=='без име', -o['площ_m2']))
table(rest,'Детски заведения — останалите райони')
for cls,t in [('образование','Образование'),('здравно заведение','Здравни заведения'),
              ('социални грижи','Заведения за социални грижи'),('общежитие','Общежития')]:
    g=[o for o in out if o['клас']==cls]
    g.sort(key=lambda o:(o['име']=='без име', -o['площ_m2']))
    table(g,t)
acc=[o for o in out if o['клас'] in ('хотел','курортна/туристическа')]
acc.sort(key=lambda o:(o['име']=='без име', -o['площ_m2']))
table(acc[:26],'Настаняване (хотел + курортна) — с име и 20-те най-големи без име, от общо %d' % len(acc))
