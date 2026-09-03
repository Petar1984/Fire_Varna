# -*- coding: utf-8 -*-
"""READ-ONLY: закотвените редове на регистровата извадка, които находка №11 цитира."""
import io
SRC = r"C:\git\varna_3d\scratch\refactor\_addr\sol_lechebni.txt"
WANT = {371: "СБАЛПФЗ", 405: "Олимед", 417: "Майчин дом", 430: "Аджибадем"}
lines = io.open(SRC, encoding="utf-8").read().split("\n")
for n, tag in sorted(WANT.items()):
    print("%s | ред %d: %s" % (tag, n, lines[n - 1].strip()))
