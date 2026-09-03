# -*- coding: utf-8 -*-
import sys, json, re, collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
info, cols = load_info(); rows=info['rows']
# does any addr look cadastral?
cad=re.compile(r'\b\d{4,5}\.\d+')
n=sum(1 for a in info['dict']['addr'] if cad.search(a))
print('addr стойности с кадастрален шаблон:', n, 'от', len(info['dict']['addr']))
print('с 10135:', sum(1 for a in info['dict']['addr'] if '10135' in a))
# name-bearing addr values
PAT=re.compile(r'(ЦДГ|ОДЗ|\bДГ\b|ясл|ДЯ\b|детск)', re.I)
hits=[a for a in info['dict']['addr'] if PAT.search(a)]
print('\nadr стойности с ЦДГ/ОДЗ/ДГ/ясла:', len(hits))
for a in hits[:40]: print('   ', a)
