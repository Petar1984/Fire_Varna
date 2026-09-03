# -*- coding: utf-8 -*-
import sys, json, collections, re
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
info,cols=load_info()
h=[a for a in info['dict']['addr'] if '10135' in a]
print('addr стойности с „10135“:', len(h))
for a in h[:8]: print('   ', a)
