# -*- coding: utf-8 -*-
"""Geocode register addresses through Fire_Varna/data/address_rows.json.

Deterministic cascade; every hit records the method, how many address rows were
averaged and how far apart those rows are, so a weak hit ("само улица", a whole
street averaged) can be told from a strong one ("точен ключ").
"""
import json, re, collections, sys, os, math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from namelib import norm_addr, ordinal_variants
from geolib import MX, MY
from quarters import Quarters

ADDR_ROWS = 'C:/git/Fire_Varna/data/address_rows.json'

STRONG = {'точен ключ', 'точен ключ (без тип)', 'точен ключ (сменен тип)',
          'точен ключ (добавен тип)', 'улица+номер', 'квартал + блок',
          'блок (единствен ключ)', 'квартал + блок [регистър на кварталите]'}

TYPEWORDS = ('ул', 'бул', 'пл', 'кв', 'жк', 'кк', 'м', 'мест', 'местност',
             'ал', 'со', 'сп', 'мр', 'к', 'с')


def clean_register_address(a):
    """Strip register markup: verdict glyphs, notes, parentheses, extra addresses."""
    a = re.sub('[\u2713\u25b3\u26a0]', ' ', a)
    a = a.replace('**', ' ')
    a = re.sub(r'\(.*?\)', ' ', a)
    a = re.split(r'[;+]| и ул ', a)[0]
    a = re.sub(r'\bет\.?\s*\d.*$', '', a)
    a = re.sub(r'\bтяло\b.*$', '', a)
    a = re.sub(r'\bУПИ\b.*$', '', a)
    return a.strip(' ,')


class Geocoder:
    def __init__(self, path=ADDR_ROWS):
        d = json.load(open(path, encoding='utf-8'))
        self.rows = d['rows']
        self.by_key = collections.defaultdict(list)
        for k, la, lo in self.rows:
            self.by_key[k].append((la, lo))
        self.keys = sorted(self.by_key)
        try:
            self.Q = Quarters()
        except Exception:
            self.Q = None

    @staticmethod
    def _spread(pts):
        """Max pairwise separation of the averaged rows, in metres (approx)."""
        if len(pts) < 2:
            return 0.0
        la = [p[0] for p in pts]; lo = [p[1] for p in pts]
        return round(math.hypot((max(la) - min(la)) * MY,
                                (max(lo) - min(lo)) * MX), 1)

    def _hit(self, keys, method):
        pts = []
        for k in keys:
            pts.extend(self.by_key[k])
        if not pts:
            return None
        la = sum(p[0] for p in pts) / len(pts)
        lo = sum(p[1] for p in pts) / len(pts)
        return {'lat': round(la, 6), 'lon': round(lo, 6), 'method': method,
                'n_rows': len(pts), 'n_keys': len(keys),
                'spread_m': self._spread(pts),
                'strong': method.split(' [')[0] in STRONG,
                'matched_key': ' | '.join(sorted(keys)[:4])}

    def _try_exact(self, s):
        for v in ordinal_variants(s):
            if v in self.by_key:
                return self._hit([v], 'точен ключ')
            toks = v.split(' ')
            if toks and toks[0] in TYPEWORDS:
                s2 = ' '.join(toks[1:])
                if s2 in self.by_key:
                    return self._hit([s2], 'точен ключ (без тип)')
                for t in ('ул', 'бул', 'пл'):
                    if (t + ' ' + s2) in self.by_key:
                        return self._hit([t + ' ' + s2], 'точен ключ (сменен тип)')
            else:
                for t in ('ул', 'бул', 'пл'):
                    if (t + ' ' + v) in self.by_key:
                        return self._hit([t + ' ' + v], 'точен ключ (добавен тип)')
        return None

    def geocode(self, address):
        if not address:
            return None
        s = norm_addr(clean_register_address(address))
        if not s or len(s) < 3:
            return None
        s = re.sub(r'\bдо\s+блок\b', 'бл', s)
        s = re.sub(r'\bблок\b', 'бл', s)
        s = re.sub(r'\bбл\s*([0-9])', r'бл \1', s)

        r = self._try_exact(s)
        if r:
            return r

        m = re.match(r'^(кв|жк|кк|мест|м|со|сп)\s+(.+?)\s+(ул|бул|пл|ал)\s+(.+)$', s)
        if m:
            r = self._try_exact(m.group(3) + ' ' + m.group(4))
            if r:
                r['method'] += ' [след квартал]'
                return r

        m = re.search(r'\bбл\s*([0-9]+[а-я]?)\b', s)
        if m:
            blk = m.group(1)
            head = re.sub(r'\b(до|срещу|зад|гр|варна)\b', ' ', s[:m.start()]).strip()
            cand = [k for k in self.keys if k.endswith(' бл ' + blk)]
            if head and cand:
                hw = [w for w in head.split() if len(w) > 3 and w not in TYPEWORDS]
                narrow = [k for k in cand if all(w[:5] in k for w in hw)] if hw else []
                if not narrow and hw:
                    narrow = [k for k in cand if hw[-1][:5] in k]
                if not narrow and self.Q is not None:
                    # the signed quarter register: "ж.к. Вл. Варненчик" also covers
                    # "кв. Владиславово" and its child "кв. Кайсиева градина"
                    fam = [k for k in cand
                           if self.Q.same_family(head, k[:k.rfind(' бл ')])]
                    if fam:
                        return self._hit(fam, 'квартал + блок [регистър на кварталите]')
                if narrow:
                    return self._hit(narrow, 'квартал + блок')
            # "ул. 6-ти септември до бл.9" — the head is a STREET the index knows;
            # never average ten unrelated "бл 9" keys across the city for it.
            head_is_street = False
            for v in ordinal_variants(head):
                st = [w for w in v.split() if w not in TYPEWORDS and len(w) > 2]
                if st and any(all(w in k for w in st) for k in self.keys):
                    head_is_street = True
                    break
            if not head_is_street:
                if len(cand) == 1:
                    return self._hit(cand, 'блок (единствен ключ)')
                if cand:
                    return self._hit(cand, 'блок (без квартал, ' + str(len(cand)) + ' ключа)')

        m = re.search(r'\b([0-9]+\s*[а-я]?)\s*$', s)
        num = re.sub(r'\s+', '', m.group(1)) if m else None
        street = s[:m.start()].strip() if m else s
        for v in ordinal_variants(street):
            st = [w for w in v.split() if w not in TYPEWORDS and len(w) > 2]
            if not st:
                continue
            cand = [k for k in self.keys if all(w in k for w in st)]
            if num:
                exact = [k for k in cand if k.split()[-1] == num]
                if exact:
                    return self._hit(exact, 'улица+номер')
            if cand:
                return self._hit(cand[:80],
                                 'само улица' if not num
                                 else 'улица (номерът не се намери)')
        return None
