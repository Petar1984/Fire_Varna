# -*- coding: utf-8 -*-
"""Quarter aliases, read from the SIGNED register
C:/git/Varna_buildings/config/quarter_registry.json (schema 1.1, подпис 12.08).

Used only to decide whether an address key like "кв кайсиева градина бл 208"
belongs to the same quarter as a register address "ж.к. Вл. Варненчик до бл.208".
No name is invented here: every alias comes from the register file.
"""
import json, os, sys, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from namelib import norm_addr

REG = 'C:/git/Varna_buildings/config/quarter_registry.json'


class Quarters:
    def __init__(self, path=REG):
        d = json.load(open(path, encoding='utf-8'))
        self.entries = d['entries']
        self.by_id = {e['id']: e for e in self.entries}
        self.display2id = {}
        self.alias2id = {}
        for e in self.entries:
            self.display2id[norm_addr(e['display'])] = e['id']
            for a in e.get('aliases', []):
                self.alias2id[self._core(a)] = e['id']
            self.alias2id[self._core(e['display'])] = e['id']
        # parents: id -> set of ancestor ids
        self.parents = {}
        for e in self.entries:
            ps = set()
            for p in e.get('parents', []) or []:
                pid = self.display2id.get(norm_addr(p))
                if pid:
                    ps.add(pid)
            self.parents[e['id']] = ps
        # family = self + ancestors + descendants
        self.family = {}
        for i in self.by_id:
            fam = {i} | self.parents.get(i, set())
            for j, ps in self.parents.items():
                if i in ps:
                    fam.add(j)
            self.family[i] = fam

    @staticmethod
    def _core(a):
        s = norm_addr(a)
        s = re.sub(r'^(кв|жк|кк|мест|м|со|сп|ж к|к к)\s+', '', s)
        s = re.sub(r'\b[ivx]+\s*мр\b|\bмр\b|\b[ivx]+\b', ' ', s)
        s = re.sub(r'\s+', ' ', s).strip()
        return s

    def resolve(self, text):
        """id of the quarter a free-text address head names, or None."""
        c = self._core(text)
        if not c:
            return None
        if c in self.alias2id:
            return self.alias2id[c]
        # longest alias that is a substring of the head
        best = None
        for a, i in self.alias2id.items():
            if len(a) >= 5 and a in c:
                if best is None or len(a) > len(best[0]):
                    best = (a, i)
        return best[1] if best else None

    def same_family(self, a_text, b_text):
        ia, ib = self.resolve(a_text), self.resolve(b_text)
        if ia is None or ib is None:
            return False
        return ib in self.family.get(ia, {ia}) or ia in self.family.get(ib, {ib})
