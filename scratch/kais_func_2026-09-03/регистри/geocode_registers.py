# -*- coding: utf-8 -*-
"""
Register row -> address -> coordinate -> KAIS body with the matching function.

READ-ONLY over C:/git.  Everything written goes into this script's own folder.

Sources
  registers : C:/git/Fire_Varna/scratch/audit_2026-09-03/places_registers.json
              (verbatim transcript of varna_3d/scratch/refactor/_addr/kimi_obrazovanie.txt
               and sol_lechebni.txt)
  geocoder  : C:/git/Fire_Varna/data/address_rows.json  (normalized_address, lat, lng)
  KAIS      : kais_cache.json  (built by build_cache.py from
              varna_3d/web/varna_buildings_3d.geojson + varna_buildings_info.json)
  delivery  : C:/git/Fire_Varna/data/places.json

Run:  python build_cache.py && python geocode_registers.py
"""
import json, math, os, re, sys, unicodedata
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
G = 'C:/git/'
R_BODY = 150.0      # KAIS body search radius, per the task
R_LINK = 45.0       # single-linkage radius: several bodies = one site
R_DELIV = 60.0      # "already delivered" radius, per the task
R_FAR = 400.0       # informational: nearest site beyond R_BODY


# ---------------------------------------------------------------- helpers
def norm(s):
    """identical to the app's own normalizer (Fire_Varna/.../verify_1/fvlib.py: norm)"""
    s = ('' if s is None else str(s)).lower().replace('блок', 'бл').replace('вход', 'вх')
    s = re.sub(r"[.№,'\"\-]", ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


QUOTES = '„“”«»‘’‚`´'


def clean(s):
    s = unicodedata.normalize('NFC', str(s))
    for q in QUOTES:
        s = s.replace(q, ' ')
    s = s.replace('–', '-').replace('—', '-')
    return re.sub(r'\s+', ' ', s).strip()


def dm(a, b):
    R = 6371000.0
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    h = (math.sin((p2 - p1) / 2) ** 2 +
         math.cos(p1) * math.cos(p2) * math.sin(math.radians(b[1] - a[1]) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def mean_pt(pts):
    return [round(sum(p[0] for p in pts) / len(pts), 6),
            round(sum(p[1] for p in pts) / len(pts), 6)]


def spread(pts):
    if len(pts) < 2:
        return 0.0
    c = mean_pt(pts)
    return max(dm(c, p) for p in pts)


# ---------------------------------------------------------------- load
REG = json.load(open(G + 'Fire_Varna/scratch/audit_2026-09-03/places_registers.json', encoding='utf-8'))
AR = json.load(open(G + 'Fire_Varna/data/address_rows.json', encoding='utf-8'))
KA = json.load(open(HERE + '/kais_cache.json', encoding='utf-8'))
PL = json.load(open(G + 'Fire_Varna/data/places.json', encoding='utf-8'))['places']

by_key = defaultdict(list)
for a, la, ln in AR['rows']:
    by_key[a].append((la, ln))
KEYS = sorted(by_key)
KEYSET = set(KEYS)

FUNC = KA['func_dict']
CLASS_FUNC = {
    'детско заведение': ['Сграда за детско заведение'],
    'образование': ['Сграда за образование'],
    'здравно': ['Здравно заведение'],
}
FIDX = {c: set(FUNC.index(f) for f in fs) for c, fs in CLASS_FUNC.items()}
CENT, FN, AREA, ADDR, QUAR, PROP, FLOORS, REGN = (
    KA['centroids'], KA['func'], KA['area_m2'], KA['addr'], KA['quar'],
    KA['prop'], KA['floors'], KA['reg'])
BY_CLASS = {c: [i for i, f in enumerate(FN) if f in idxs] for c, idxs in FIDX.items()}


# ------------------------------------------------ global sites per class
def build_sites(idx, link=R_LINK):
    """single-linkage over ALL bodies of the class -> physical sites"""
    par = {i: i for i in idx}

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    # grid bucketing keeps it O(n) instead of O(n^2)
    cell = link / 111000.0 * 1.5
    grid = defaultdict(list)
    for i in idx:
        c = CENT[i]
        grid[(int(c[0] / cell), int(c[1] / cell))].append(i)
    for (gx, gy), members in list(grid.items()):
        neigh = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                neigh += grid.get((gx + dx, gy + dy), [])
        for a in members:
            for b in neigh:
                if a < b and dm(CENT[a], CENT[b]) <= link:
                    ra, rb = f(a), f(b)
                    if ra != rb:
                        par[ra] = rb
    g = defaultdict(list)
    for i in idx:
        g[f(i)].append(i)
    sites = []
    for _, m in g.items():
        m.sort(key=lambda i: -AREA[i])
        pts = [CENT[i] for i in m]
        c = mean_pt(pts)
        addrs = [ADDR[i] for i in m if ADDR[i]]
        sites.append({'site_id': len(sites), 'n_bodies': len(m),
                      'lat': c[0], 'lon': c[1],
                      'area_m2': round(sum(AREA[i] for i in m), 1),
                      'max_area_m2': AREA[m[0]], 'floors_max': max(FLOORS[i] for i in m),
                      'addr': (addrs[0] if addrs else ''),
                      'addrs': sorted(set(addrs)),
                      'prop': PROP[m[0]], 'reg': REGN[m[0]],
                      'quar': QUAR[m[0]], 'i_list': m,
                      'radius_m': round(max(dm(c, p) for p in pts), 1) if len(pts) > 1 else 0.0})
    return sites


SITES = {cls: build_sites(idx) for cls, idx in BY_CLASS.items()}


def sites_near(pt, cls, rmax=R_BODY):
    out = []
    for s in SITES[cls]:
        if abs(s['lat'] - pt[0]) > (rmax + 300) / 111000.0:
            continue
        d = min(dm(pt, CENT[i]) for i in s['i_list'])
        if d <= rmax:
            o = dict(s)
            o['d_m'] = round(d, 1)
            o.pop('i_list', None)
            o['bodies'] = [{'i': i, 'd_m': round(dm(pt, CENT[i]), 1), 'addr': ADDR[i],
                            'area_m2': AREA[i], 'floors': FLOORS[i], 'prop': PROP[i],
                            'lat': CENT[i][0], 'lon': CENT[i][1]}
                           for i in sorted(s['i_list'], key=lambda i: dm(pt, CENT[i]))]
            out.append(o)
    return sorted(out, key=lambda x: x['d_m'])


# ---------------------------------------------------------------- geocoding
QUARTER_PREFIXES = {
    'владислав варненчик': ['кв владиславово', 'бул владислав варненчик', 'вл варненчик',
                            'жк вл варненчик', 'жк вл варненчик м р',
                            'гр варна район владислав варненчик',
                            'гр варна район владислав варненчик жк владислав варненчик',
                            'гр варна район владислав варненчик жк вл варненчик м р',
                            'гр варна район владислав варненчик жк влладислав варненчик м р',
                            'гр варна район владислав варненчик жк власислав варненчик до',
                            'владислав варненчик до', 'кв кайсиева градина'],
    'кайсиева градина': ['кв кайсиева градина'],
    'чайка': ['кв чайка', 'чайка', 'гр варна район приморски жк чайка'],
    'младост': ['жк младост 1', 'жк младост 2', 'жк младост', 'младост',
                'младост зпз', 'младост 83', 'младост зпз 83', 'младост 48',
                'младост зпз 48', 'гр варна район младост жк младост',
                'гр варна район младост'],
    'възраждане': ['жк възраждане 1', 'жк възраждане 2', 'жк възраждане 3',
                   'жк възраждане 4', 'жк възраждане', 'възраждане',
                   'гр варна район младост жк възраждане',
                   'гр варна район младост жк възраждане до'],
    'възраждане 1': ['жк възраждане 1'],
    'възраждане 2': ['жк възраждане 2'],
    'възраждане 3': ['жк възраждане 3'],
    'възраждане 4': ['жк възраждане 4'],
    'трошево': ['кв трошево'],
    'победа': ['победа', 'победа до'],
    'дружба': ['дружба', 'дружба 12', 'гр варна район аспарухово жк дружба'],
    'изгрев': ['изгрев'],
}
VILLAGE = re.compile(r'\bс\s*\.\s*(тополи|каменар|константиново|звездица|зорница|казашко)', re.I)
STREET_TYPES = ('ул', 'бул', 'пл', 'площад', 'ал', 'алея', 'м', 'местност', 'жк', 'кв', 'кк',
                'со', 'сп', 'мест', 'кс', 'к', 'с', 'до', 'при', 'срещу')
_G1 = ('ул', 'бул', 'пл', 'площад', 'ал', 'алея')
_G2 = ('жк', 'кв', 'кк', 'м', 'со', 'местност', 'мест', 'сп', 'к к', 'с о')
TYPE_GROUP = {}
for _t in _G1:
    TYPE_GROUP[_t] = _G1
for _t in _G2:
    TYPE_GROUP[_t] = _G2

ORD_WORD = {'1': 'първа', '2': 'втора', '3': 'трета', '4': 'четвърта', '5': 'пета',
            '6': 'шести', '7': 'седма', '8': 'осми', '9': 'девета', '10': 'десета',
            '16': 'шестнадесета', '30': 'тридесета'}
ROMAN = {'iii': '3', 'vii': '7', 'viii': '8', 'ii': '2', 'iv': '4', 'vi': '6', 'ix': '9',
         'x': '10', 'v': '5', 'i': '1'}


def variants(a):
    """textual variants of one address: roman numerals, ordinal words, 'св. св.' -> 'св'"""
    out = [a]
    b = a
    for rn, ar in ROMAN.items():
        b = re.sub(r'(?<![а-яa-zА-ЯA-Z])' + rn + r'(?![а-яa-zА-ЯA-Z])', ar, b, flags=re.I)
    if b != a:
        out.append(b)
    for v in list(out):
        w = re.sub(r'\b(\d{1,2})\s*-?\s*(?:ви|ти|ри|ра|ва|во|ма|та|я|ия)\b',
                   lambda m: ORD_WORD.get(m.group(1), m.group(0)), v)
        if w != v:
            out.append(w)
    for v in list(out):
        w = re.sub(r'\bсв\s*\.?\s*св\s*\.?', 'св ', v, flags=re.I)
        if w != v:
            out.append(w)
    return out


def strip_lead(a):
    a = re.sub(r'^\s*гр\s*\.?\s*варна\s*,?\s*', '', a, flags=re.I)
    a = re.sub(r'^\s*(р\s*-?\s*н|район)\s+[а-яa-z. ]+?,\s*', '', a, flags=re.I)
    return a.strip(' ,')


def block_key_groups(raw):
    """'до бл. 402' inside a quarter -> {real address_rows key: coordinate}"""
    n = norm(clean(raw))
    m = re.search(r'\bбл\s*(\d+[а-я]?)\b', n)
    if not m:
        return None
    num = m.group(1)
    head = n[:m.start()]
    out = []
    for q, prefs in QUARTER_PREFIXES.items():
        hit = q in head
        if q == 'владислав варненчик' and re.search(r'вл(адислав)? варненчик|владиславово', head):
            hit = True
        if hit:
            out += [p + ' бл ' + num for p in prefs if (p + ' бл ' + num) in KEYSET]
    if not out:                       # street + block, e.g. 'ул. Евлоги Георгиев до бл. 25'
        toks = head.split()
        for cut in range(len(toks)):
            pref = re.sub(r'\b(до|при|срещу)$', '', ' '.join(toks[cut:])).strip()
            if pref and (pref + ' бл ' + num) in KEYSET:
                out.append(pref + ' бл ' + num)
    out = sorted(set(out))
    return {k: mean_pt(by_key[k]) for k in out} or None


def _tokens(a):
    """normalized tokens with any 'бл N' / 'вх X' tail removed"""
    n = norm(strip_lead(a))
    n = re.sub(r'\b(до|при|срещу)?\s*бл\s*\d+[а-я]?\b', ' ', n)
    n = re.sub(r'\bвх\s*[а-я0-9]\b', ' ', n)
    n = re.sub(r'\bм р\b|\bмр\b', ' ', n)
    n = re.sub(r'\bж к\b', 'жк', n)      # 'ж.к.' normalizes to 'ж к'; keys write 'жк'
    n = re.sub(r'\bк к\b', 'кк', n)
    n = re.sub(r'\bс о\b', 'со', n)
    return re.sub(r'\s+', ' ', n).strip().split()


def _ok_street(tokens):
    """a street-only candidate must carry at least one real word"""
    return any(t not in STREET_TYPES and not t.isdigit() and len(t) >= 3 for t in tokens)


def _parses(a):
    """candidate readings of one address, best first.
    'бул република 15 мц младост' -> house 15 on Република.
    'жк младост 2 ул иван церов'  -> NOT house 2: 2 belongs to the quarter,
                                     the street is what follows."""
    toks = _tokens(a)
    out = []
    if toks and re.fullmatch(r'\d+[а-яa-z]?', toks[-1]):
        out.append((toks, len(toks) - 1))
    k = None
    for i in range(len(toks) - 1, -1, -1):
        if re.fullmatch(r'\d+[а-яa-z]?', toks[i]):
            k = i
            break
    if k is not None and k < len(toks) - 1:
        head = toks[:k]
        if not (head and head[0] in _G2):          # a quarter number, not a house number
            out.append((toks[:k + 1], k))
        out.append((toks[k + 1:], None))           # the street after the quarter number
    if not out:
        out.append((toks, None))
    return out


def _parse(a):
    return _parses(a)[0]


def _prefixable(head, cut):
    """which street-type words may be put in front of head[cut:]"""
    if cut == 0:
        return _G1 + _G2
    prev = head[cut - 1]
    if prev in _G2:
        return _G2
    if prev in _G1:
        return _G1
    return _G1 + _G2


def num_candidates(a):
    out = []
    for toks, numpos in _parses(a):
        if numpos is None:
            continue
        out += _num_cands(toks, numpos)
    seen, res = set(), []
    for c in out:
        if c not in seen:
            seen.add(c)
            res.append(c)
    return res


def _num_cands(toks, numpos):
    num = toks[numpos]
    head = toks[:numpos]
    out = []
    for cut in range(len(head)):
        suf = head[cut:]
        if not _ok_street(suf):
            continue
        out.append(' '.join(suf) + ' ' + num)
        if suf[0] not in STREET_TYPES:
            for t in _prefixable(head, cut):
                out.append(t + ' ' + ' '.join(suf) + ' ' + num)
        else:
            for t in TYPE_GROUP.get(suf[0], ()):
                out.append(' '.join([t] + suf[1:]) + ' ' + num)
    seen, res = set(), []
    for c in out:
        if c not in seen:
            seen.add(c)
            res.append(c)
    return res


def street_candidates(a):
    out = []
    for toks, numpos in _parses(a):
        out += _street_cands(toks, numpos)
    seen, res = set(), []
    for c in out:
        if c not in seen:
            seen.add(c)
            res.append(c)
    return res


def _street_cands(toks, numpos):
    head = toks[:numpos] if numpos is not None else toks
    out = []
    for cut in range(len(head)):
        suf = head[cut:]
        if not _ok_street(suf):
            continue
        out.append(' '.join(suf))
        if suf[0] not in STREET_TYPES:
            for t in _prefixable(head, cut):
                out.append(t + ' ' + ' '.join(suf))
        else:
            for t in TYPE_GROUP.get(suf[0], ()):
                out.append(' '.join([t] + suf[1:]))
    seen, res = set(), []
    for c in out:
        if c not in seen:
            seen.add(c)
            res.append(c)
    return res


KEY_TOKENS = {k: k.split() for k in KEYS}
LONG_INDEX = defaultdict(set)
for _k, _t in KEY_TOKENS.items():
    for _w in _t:
        if len(_w) >= 4 and not _w.isdigit():
            LONG_INDEX[_w].add(_k)


def longword_match(a, with_number=True):
    """last resort: every long word of the address must be in the key.
    Handles the register's initials ('ул. Г.Колев 92' -> 'ул генерал колев 92')."""
    toks, numpos = _parse(a)
    if with_number and numpos is None:
        for t2, n2 in _parses(a):
            if n2 is not None:
                toks, numpos = t2, n2
                break
    num = toks[numpos] if numpos is not None else None
    head = toks[:numpos] if numpos is not None else toks
    longs = [t for t in head if len(t) >= 4 and not t.isdigit() and t not in STREET_TYPES]
    if not longs or any(t not in LONG_INDEX for t in longs):
        return None
    cand = set(LONG_INDEX[longs[0]])
    for t in longs[1:]:
        cand &= LONG_INDEX[t]
    if not cand:
        return None
    if with_number:
        if num is None:
            return None
        cand = {k for k in cand
                if KEY_TOKENS[k][-1] == num and len(KEY_TOKENS[k]) >= 2
                and KEY_TOKENS[k][-2] not in ('бл', 'вх')}
    if not cand:
        return None
    ks = sorted(cand)
    pts = [p for k in ks for p in by_key[k]]
    sp = spread(pts)
    if sp > 250:
        return None
    c, used, tot, sp, ngrp = resolve_points(pts)
    return {'ok': True, 'lat': c[0], 'lon': c[1],
            'method': ('улица+номер · по дълги думи' if with_number else 'улица · по дълги думи'),
            'confidence': 'точен' if with_number else 'улица без номер',
            'keys': ks[:6], 'n_keys': len(ks), 'n_rows': tot, 'n_rows_used': used,
            'n_groups': ngrp, 'spread_m': sp, 'long_words': longs}


def quarter_fallback(a):
    n = norm(clean(a))
    for q, prefs in QUARTER_PREFIXES.items():
        hit = q in n
        if q == 'владислав варненчик' and re.search(r'вл(адислав)? варненчик|владиславово', n):
            hit = True
        if hit:
            ks = [k for k in KEYS if any(k == p or k.startswith(p + ' ') for p in prefs)]
            if ks:
                pts = [p for k in ks for p in by_key[k]]
                c = mean_pt(pts)
                return {'ok': True, 'lat': c[0], 'lon': c[1],
                        'method': 'квартал (адресът няма улица/номер)',
                        'confidence': 'квартал', 'keys': prefs[:4], 'n_keys': len(ks),
                        'n_rows': len(pts), 'spread_m': round(spread(pts), 1), 'quarter': q}
    return None



def resolve_points(pts, link=200.0):
    """address_rows carries rows that share a normalized key yet sit kilometres apart
    (measured: 'бул цар освободител 150' = 5 rows, spread 2225 m).  Take the densest
    tight group instead of the mean, and report how much of the key it holds."""
    n = len(pts)
    par = list(range(n))

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for i in range(n):
        for j in range(i + 1, n):
            if dm(pts[i], pts[j]) <= link:
                a, b = f(i), f(j)
                if a != b:
                    par[a] = b
    g = {}
    for i in range(n):
        g.setdefault(f(i), []).append(pts[i])
    groups = sorted(g.values(), key=lambda m: (-len(m), spread(m)))
    best = groups[0]
    return mean_pt(best), len(best), n, round(spread(best), 1), len(groups)


def _hit(cand, how, conf, method):
    if how == 'exact':
        pts, ks = by_key[cand], [cand]
    else:
        ks = [k for k in KEYS if k.startswith(cand + ' ')]
        if not ks:
            return None
        pts = [p for k in ks for p in by_key[k]]
    c, used, tot, sp, ngrp = resolve_points(pts)
    if ngrp > 1:
        method += ' (ключът е разпръснат: %d групи, взета най-голямата %d/%d реда)' % (ngrp, used, tot)
    return {'ok': True, 'lat': c[0], 'lon': c[1], 'method': method,
            'confidence': conf, 'keys': ks[:6], 'n_keys': len(ks),
            'n_rows': tot, 'n_rows_used': used, 'n_groups': ngrp, 'spread_m': sp}


def geocode_one(raw):
    a = clean(raw)
    if VILLAGE.search(a) or re.match(r'^\s*с\s*\.\s*[А-Я]', a):
        return {'ok': False, 'method': 'село — извън гр. Варна', 'confidence': 'няма'}
    vs = variants(a)
    for v in vs:                                            # 1. block key
        gr = block_key_groups(v)
        if gr:
            pts = list(gr.values())
            sp = spread(pts)
            c = mean_pt(pts)
            return {'ok': True, 'lat': c[0], 'lon': c[1], 'method': 'блок',
                    'confidence': 'блок' if sp <= 200 else 'блок (нееднозначен квартал)',
                    'keys': sorted(gr), 'groups': gr, 'spread_m': round(sp, 1),
                    'n_rows': sum(len(by_key[k]) for k in gr)}
    for v in vs:                                            # 2. street + number, exact
        for cand in num_candidates(v):
            if cand in KEYSET:
                return _hit(cand, 'exact', 'точен', 'улица+номер · точен ключ')
    for v in vs:                                            # 3. street + number, subset
        for cand in num_candidates(v):
            h = _hit(cand, 'prefix', 'точен', 'улица+номер · подмножество на ключа')
            if h:
                return h
    for v in vs:                                            # 4. street only, exact
        for cand in street_candidates(v):
            if cand in KEYSET:
                return _hit(cand, 'exact', 'улица без номер', 'улица · точен ключ')
    for v in vs:                                            # 5. street only, subset
        for cand in street_candidates(v):
            h = _hit(cand, 'prefix', 'улица без номер', 'улица · подмножество на ключа')
            if h:
                return h
    for v in vs:                                            # 6. long words + number
        h = longword_match(v, True)
        if h:
            return h
    for v in vs:                                            # 7. long words only
        h = longword_match(v, False)
        if h:
            return h
    h = quarter_fallback(a)                                 # 8. quarter centroid
    if h:
        return h
    return {'ok': False, 'method': 'адресът не се геокодира', 'confidence': 'няма'}


# ---------------------------------------------------------------- delivery
KIND_CLASS = {'детска градина': 'детско заведение', 'училище': 'образование',
              'университет': 'образование', 'болница': 'здравно', 'ДКЦ': 'здравно',
              'хоспис': 'здравно'}
DELIV = [dict(p, _cls=KIND_CLASS.get(p['kind'])) for p in PL]

_STOP = (r'\b(дг|цдг|одз|одг|дя|детска|градина|ясла|детско|заведение|оу|су|соу|ну|пг|пгт|ег|мг|'
         r'пмг|чдг|чоу|чсу|чег|чпг|чцдг|еоод|оод|ад|еад|мбал|сбал|дкц|хоспис|филиал|варна|яг|'
         r'яслена|група|бивше|бивш|за|по|на|и|при|св|свв|свети|света|логопедична|оздравителна|'
         r'многопрофилна|специализирана|болница|активно|лечение|център|университетска|'
         r'общинско|основно|средно|училище|гимназия|професионална|частно|частна|д|р|проф|доц|акад)\b')


def name_core(s):
    s = clean(s).lower()
    s = re.sub(r'[^а-яa-z0-9 ]', ' ', s)
    s = re.sub(_STOP, ' ', s)
    return re.sub(r'\s+', '', s)


def delivered_near(pts, cls, rmax=R_DELIV):
    out, seen = [], set()
    for p in DELIV:
        if p['_cls'] != cls:
            continue
        d = min(dm(pt, (p['lat'], p['lon'])) for pt in pts)
        if d <= rmax and p['name'] not in seen:
            seen.add(p['name'])
            out.append({'name': p['name'], 'kind': p['kind'], 'src': p['src'],
                        'zone': p.get('zone', ''), 'd_m': round(d, 1),
                        'old_names': p.get('old_names', [])})
    return sorted(out, key=lambda x: x['d_m'])


KG_FAMILY = {'дг', 'цдг', 'одз', 'одг', 'чдг', 'чцдг', 'дя', 'ясла'}
COMPANY = {'еоод', 'оод', 'ад', 'еад', 'ет', 'дззд', 'мц', 'мк', 'упи'}


def acronyms(s):
    out = set()
    for w in re.findall(r'\b[А-ЯA-Z]{2,8}\b', clean(s)):
        w = w.lower()
        if w in COMPANY:
            continue
        out.add('дз' if w in KG_FAMILY else ('су' if w == 'соу' else w))
    return out


def acro_ok(reg_name, dl_name, strict):
    if not strict:
        return True
    A, B = acronyms(reg_name), acronyms(dl_name)
    if not A or not B:
        return True
    return bool(A & B)


def same_name(reg_name, dl, strict=False):
    a = name_core(reg_name)
    if len(a) < 4:
        return False
    for cand in [dl['name']] + list(dl.get('old_names') or []):
        b = name_core(cand)
        if len(b) >= 4 and (a == b or a in b or b in a) and acro_ok(reg_name, cand, strict):
            return True
    return False


# ---------------------------------------------------------------- run
GROUPS = [
    ('детски градини (общински)', 'dg_municipal', 'детско заведение'),
    ('детски ясли', 'nurseries', 'детско заведение'),
    ('детски градини (частни)', 'dg_private', 'детско заведение'),
    ('училища', 'schools', 'образование'),
    ('ЦПЛР', 'cplr', 'образование'),
    ('болници', 'hospitals', 'здравно'),
    ('ДКЦ', 'dkc', 'здравно'),
    ('хосписи', 'hospices', 'здравно'),
]


def address_parts(a):
    a = clean(a)
    a = re.sub(r'\*\*[^*]*\*\*', ' ', a)
    a = re.sub(r'\([^)]*\)', ' ', a)
    a = a.replace('✓', ' ').replace('△', ' ').replace('⚠', ' ')
    a = re.sub(r',?\s*ет\s*\.?\s*[0-9]+(\s*-\s*[0-9]+)?\s*', ' ', a)
    parts = [p.strip(' ,') for p in re.split(r';|\s+и\s+(?=ул|бул)', a) if p.strip(' ,')]
    return parts or [a]


def geocode(addr):
    parts = address_parts(addr)
    best = None
    for p in parts:
        g = geocode_one(p)
        g['address_used'] = p
        g['address_parts'] = parts
        if g.get('ok') and g['confidence'] in ('точен', 'блок'):
            return g
        best = best or g
    return best


RESULT = {'_meta': {
    'what': 'регистров ред -> адрес -> координата -> КАИС тяло с вярна функция',
    'command': 'python build_cache.py && python geocode_registers.py',
    'sources': {
        'регистри': G + 'Fire_Varna/scratch/audit_2026-09-03/places_registers.json',
        'геокод': G + 'Fire_Varna/data/address_rows.json',
        'КАИС': G + 'varna_3d/web/varna_buildings_3d.geojson + varna_buildings_info.json',
        'доставка': G + 'Fire_Varna/data/places.json'},
    'функции': CLASS_FUNC,
    'радиуси': {'тела': R_BODY, 'клъстер (единично свързване)': R_LINK,
                'доставено място': R_DELIV, 'информативно извън радиуса': R_FAR},
    'присъда': ('еднозначно = точно 1 КАИС място (клъстер тела) от класа на <=150 m, '
                'или няколко, но само едно на <=80 m; спорно = 2+; без тяло = 0'),
    'КАИС места по клас': {c: len(v) for c, v in SITES.items()},
}}

used_delivered = set()
for label, key, cls in GROUPS:
    rows = []
    for r in REG[key]:
        addr = r.get('address') or ''
        geo = geocode(addr)
        rec = {'no': r.get('no'), 'name': r.get('name'), 'address': addr,
               'rajon': r.get('rajon') or r.get('rajon_id'), 'geo': geo}
        if geo.get('ok'):
            pt = (geo['lat'], geo['lon'])
            if geo.get('groups') and len(geo['groups']) > 1:
                scored = []
                for k, c in geo['groups'].items():
                    s = sites_near(tuple(c), cls)
                    scored.append((s[0]['d_m'] if s else 9e9, k, c))
                scored.sort()
                if scored[0][0] < 9e9:
                    pt = tuple(scored[0][2])
                    geo['picked_key'] = scored[0][1]
                    geo['method'] = 'блок (кварталът разграничен по функцията на тялото)'
                    geo['lat'], geo['lon'] = pt[0], pt[1]
            st = sites_near(pt, cls)
            rec['n_sites_150'] = len(st)
            rec['n_bodies_150'] = sum(len([b for b in s['bodies'] if b['d_m'] <= R_BODY]) for s in st)
            rec['sites'] = st
            if not st:
                rec['verdict'] = 'без тяло'
                far = sites_near(pt, cls, R_FAR)
                rec['nearest_beyond_150'] = ({k: v for k, v in far[0].items() if k != 'bodies'}
                                             if far else None)
            elif len(st) == 1:
                rec['verdict'] = 'еднозначно'
            else:
                near = [s for s in st if s['d_m'] <= 80]
                rec['verdict'] = 'еднозначно' if len(near) == 1 else 'спорно'
            anchors = [pt] + [(s['lat'], s['lon']) for s in st[:2]]
            dl = delivered_near(anchors, cls)
            rec['delivered_near_60m'] = dl
            rec['delivered_near_150m'] = delivered_near(anchors, cls, 150.0)
            st_ac = cls != 'здравно'
            rec['delivered_same_name'] = [d['name'] for d in dl if same_name(r['name'], d, st_ac)]
            rec['delivered_other_name'] = [d['name'] for d in dl if not same_name(r['name'], d, st_ac)]
            for d in dl:
                used_delivered.add((d['name'], d['kind']))
        else:
            rec['verdict'] = geo['method']
            for k in ('delivered_near_60m', 'delivered_near_150m',
                      'delivered_same_name', 'delivered_other_name'):
                rec[k] = []
        nm = [p['name'] for p in DELIV if p['_cls'] == cls and same_name(r['name'], p, cls != 'здравно')]
        rec['delivered_by_name_anywhere'] = nm
        for n2 in nm:
            k2 = [p for p in DELIV if p['name'] == n2][0]
            used_delivered.add((n2, k2['kind']))
        rows.append(rec)
    RESULT[label] = rows

# ------------------------- who owns which delivered place
# a delivered place matched BY NAME belongs to that register row; another row must not
# count it as "already delivered" merely because its (street-level) geocode is close.
name_owner = {}
for label, key, cls in GROUPS:
    for r in RESULT[label]:
        for n in r['delivered_by_name_anywhere']:
            name_owner.setdefault(n, (label, r['no'], r['name']))
for label, key, cls in GROUPS:
    for r in RESULT[label]:
        mine = set(r['delivered_by_name_anywhere'])
        pos = [d for d in r['delivered_near_60m']
               if d['name'] in mine or name_owner.get(d['name'], (None, None, None))[2] == r['name']
               or d['name'] not in name_owner]
        r['delivered_pos_free'] = pos
        if mine:
            r['delivered_status'] = 'доставено по име'
        elif pos:
            r['delivered_status'] = 'доставено по положение'
        else:
            r['delivered_status'] = 'НЕ е доставено'
            r['taken_by_other'] = [{'name': d['name'], 'd_m': d['d_m'],
                                    'owner': name_owner.get(d['name'])}
                                   for d in r['delivered_near_60m']]

rev = defaultdict(list)
for p in DELIV:
    if (p['name'], p['kind']) in used_delivered:
        continue
    cls = p['_cls']
    st = sites_near((p['lat'], p['lon']), cls, 80) if cls else []
    rev[p['kind']].append({'name': p['name'], 'kind': p['kind'], 'src': p['src'],
                           'zone': p.get('zone', ''), 'lat': p['lat'], 'lon': p['lon'],
                           'status': p.get('status', ''), 'old_names': p.get('old_names', []),
                           'kais_site_80m': ({k: v for k, v in st[0].items() if k != 'bodies'}
                                             if st else None)})
RESULT['ОБРАТНО: доставени места без регистров ред'] = dict(rev)

# --------------------------------------- KAIS sites nobody delivered (whole city)
gap = {}
for cls in SITES:
    kinds = [k for k, c in KIND_CLASS.items() if c == cls]
    lst = []
    for s in SITES[cls]:
        d = [(round(dm((s['lat'], s['lon']), (p['lat'], p['lon'])), 1), p['name'], p['kind'])
             for p in DELIV if p['kind'] in kinds
             and dm((s['lat'], s['lon']), (p['lat'], p['lon'])) <= 80]
        o = {k: v for k, v in s.items() if k != 'i_list'}
        o['delivered_80m'] = sorted(d)
        lst.append(o)
    gap[cls] = lst
RESULT['КАИС места по клас (целият град)'] = gap
json.dump(RESULT, open(HERE + '/registry_geocoded.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- console
hdr = ('клас', 'реда', 'геок', 'едн', 'спор', 'безтл', 'дост60', 'име', 'село', 'негео')
print('%-28s %5s %5s %5s %5s %5s %6s %5s %5s %5s' % hdr)
tot = Counter()
for label, key, cls in GROUPS:
    rows = RESULT[label]
    v = dict(rows=len(rows),
             geo=sum(1 for r in rows if r['geo'].get('ok')),
             one=sum(1 for r in rows if r['verdict'] == 'еднозначно'),
             amb=sum(1 for r in rows if r['verdict'] == 'спорно'),
             nob=sum(1 for r in rows if r['verdict'] == 'без тяло'),
             dl=sum(1 for r in rows if r['delivered_near_60m']),
             nm=sum(1 for r in rows if r['delivered_by_name_anywhere']),
             vil=sum(1 for r in rows if 'село' in r['verdict']),
             ng=sum(1 for r in rows if r['verdict'].startswith('адресът')))
    print('%-28s %5d %5d %5d %5d %5d %6d %5d %5d %5d' % (
        label, v['rows'], v['geo'], v['one'], v['amb'], v['nob'], v['dl'], v['nm'],
        v['vil'], v['ng']))
    for k, x in v.items():
        tot[k] += x
print('%-28s %5d %5d %5d %5d %5d %6d %5d %5d %5d' % (
    'ОБЩО', tot['rows'], tot['geo'], tot['one'], tot['amb'], tot['nob'],
    tot['dl'], tot['nm'], tot['vil'], tot['ng']))
print()
print('КАИС места (клъстери от тела, link=%.0f m):' % R_LINK,
      {c: len(v) for c, v in SITES.items()})
for cls in SITES:
    lst = gap[cls]
    nodel = [s for s in lst if not s['delivered_80m']]
    print('  %-18s места=%3d  с доставено място <=80 m: %3d  БЕЗ: %3d' %
          (cls, len(lst), len(lst) - len(nodel), len(nodel)))
rv = RESULT['ОБРАТНО: доставени места без регистров ред']
print()
print('доставени места без регистров ред:', sum(len(x) for x in rv.values()),
      dict((k, len(x)) for k, x in rv.items()))
print('написано:', HERE + '/registry_geocoded.json')
