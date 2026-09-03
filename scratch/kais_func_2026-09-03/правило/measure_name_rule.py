# -*- coding: utf-8 -*-
"""ЗАДАЧА „правило", част (2) — ПРАВИЛОТО ЗА ИМЕТО, измерено през търсачката.

    set PYTHONIOENCODING=utf-8 && python measure_name_rule.py

Референцията `C:/git/Fire_Varna/scratch/places_search/recall_sweep.py` се ИМПОРТИРА
(нейният `main()` е под предпазителя `if __name__ == "__main__"`, тъй че при import
не тръгва).  Индексът ѝ се строи при import от ДОСТАВЕНИТЕ байтове; тук той се
удължава В ПАМЕТТА с хипотетични записи и `search()` се пуска наново.  Нищо не се
пише в C:/git.

Какво мери:
  (1) базата — какво дават заявките на Петър днес;
  (2) седем ФОРМИ на името за едно и също място, всяка срещу 9 заявки;
  (3) регресия — за всеки от 361-те доставени записа: връща ли се на 1-во място
      при заявка = собственото му име, преди и след добавката.
"""
from __future__ import annotations
import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, r"C:/git/Fire_Varna/scratch/places_search")
import recall_sweep as RS                                   # noqa: E402

BASE = list(RS.RECS)
BASE_CLASS_OF = dict(RS.CLASS_OF)
BASE_GROUP_SIZE = dict(RS.GROUP_SIZE)
Z = "ж.к. Владислав Варненчик"


def rebuild(extra):
    """Индексът наново: RECS + CLASS_OF + GROUP_SIZE (трите глобала, които search() чете)."""
    RS.RECS = BASE + [RS.Rec(h) for h in extra]
    RS.CLASS_OF = {fk: [r for r in RS.RECS if RS.in_class(r, fk)] for fk in RS.FORM_IDX}
    gs = {}
    for r in RS.RECS:
        gs[RS.group_of(r)] = gs.get(RS.group_of(r), 0) + 1
    RS.GROUP_SIZE = gs


def rank(q, want):
    rows, br = RS.search(q)
    r = None
    for k, x in enumerate(rows):
        if x.name == want:
            r = k + 1
            break
    return rows, br, r


def show(q, want=None, n=3):
    rows, br, r = rank(q, want) if want else (RS.search(q) + (None,))
    print("   %-38s -> %3d реда · %-22s място %-3s | топ: %s"
          % ("„%s“" % q, len(rows), br, (r if r else "—"),
             " · ".join(x.name[:30] for x in rows[:n]) or "—"))


def h(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


Q = ["детска градина владиславово", "детска градина ниш 29", "ниш 29", "мечо пух",
     "детска градина ниш", "детска градина шести септември 6", "ясла 6",
     "детско заведение владиславово", "приказка"]

FORMS = {
    "A · КАИС функция + КАИС адрес В ИМЕТО": [
        dict(name="Детско заведение (без име в регистъра), ул. Ниш 29", kind="детска градина",
             lat=43.24709, lon=27.85397, zone=Z, old_names=[], status="")],
    "B · само регистрово име": [
        dict(name="ДЯ №6 „Мечо Пух“", kind="детска градина",
             lat=43.24709, lon=27.85397, zone=Z, old_names=[], status="")],
    "C · нов клас „детска ясла“ (регистрово име)": [
        dict(name="ДЯ №6 „Мечо Пух“", kind="детска ясла",
             lat=43.24709, lon=27.85397, zone=Z, old_names=[], status="")],
    "D · регистрово име + КАИС адрес В ИМЕТО": [
        dict(name="ДЯ №6 „Мечо Пух“ (ул. Ниш 29)", kind="детска градина",
             lat=43.24709, lon=27.85397, zone=Z, old_names=[], status="")],
    "E · КАИС-носено име (полето addr)": [
        dict(name="ЦДГ 10 - ПРИКАЗКА", kind="детска градина",
             lat=43.24709, lon=27.85397, zone=Z, old_names=[], status="")],
    "F · функция + адрес, кратко": [
        dict(name="Детска градина, ул. Ниш 29", kind="детска градина",
             lat=43.24709, lon=27.85397, zone=Z, old_names=[], status="")],
    "G · регистрово име, адресът в old_names": [
        dict(name="ДЯ №6 „Мечо Пух“", kind="детска градина", lat=43.24709, lon=27.85397,
             zone=Z, old_names=["ул. Ниш 29", "Детска ясла 6"], status="")],
    "H · D + old_names (D и G заедно)": [
        dict(name="ДЯ №6 „Мечо Пух“ (ул. Ниш 29)", kind="детска градина", lat=43.24709,
             lon=27.85397, zone=Z, old_names=["Детска ясла 6", "ДЯ 6"], status="")],
}


def main():
    h("§A · БАЗАТА — 361 доставени записа, нищо добавено")
    rebuild([])
    for q in Q + ["детска ясла владиславово", "ясла", "детски градини владиславово"]:
        show(q)
    print("   FORM_IDX: %d форми · с непразен клас: %d"
          % (len(RS.FORM_IDX), sum(1 for v in RS.CLASS_OF.values() if v)))
    print("   П7 зонови синоними на „ж.к. Владислав Варненчик“: %s"
          % RS.P7_ADDED.get("ж.к. Владислав Варненчик"))
    print("   класът на формата „детско заведение“ (detsko zavedenie): %d записа"
          % len(RS.CLASS_OF.get("detsko zavedenie", [])))

    h("§Б · ОСЕМТЕ ФОРМИ НА ИМЕТО, всяка срещу 9-те заявки")
    table = {}
    for lab, ex in FORMS.items():
        rebuild(ex)
        want = ex[0]["name"]
        print("--- " + lab)
        row = {}
        for q in Q:
            rows, br, r = rank(q, want)
            row[q] = {"n": len(rows), "branch": br, "rank": r}
            show(q, want)
        table[lab] = row
    json.dump(table, open("name_rule_search.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    h("§В · РЕГРЕСИЯ: заявка = собственото име, място 1 за всеки от 361-те")
    rebuild([])
    base_ok, base_bad = 0, []
    for r in BASE:
        rows, br, k = rank(r.name, r.name)
        if k == 1:
            base_ok += 1
        else:
            base_bad.append((r.name, k))
    print("   БАЗА: %d/%d на 1-во място по собственото си име" % (base_ok, len(BASE)))
    for n, k in base_bad[:8]:
        print("       не е първи: %-46s място %s" % (n[:46], k or "—"))

    # добавката: 5-те свободни площадки във Владиславово, форма D
    ADD = [
        dict(name="ДЯ №6 „Мечо Пух“ (ул. Ниш 29)", kind="детска градина",
             lat=43.24709, lon=27.85397, zone=Z, old_names=[], status=""),
        dict(name="Детско заведение (без име в регистъра), ул. Шести септември 6",
             kind="детска градина", lat=43.24476, lon=27.85417, zone=Z, old_names=[], status=""),
        dict(name="Детско заведение (без име в регистъра), ж.к. Владислав Варненчик до бл. 309",
             kind="детска градина", lat=43.24482, lon=27.84589, zone=Z, old_names=[], status=""),
        dict(name="Детско заведение (без име в регистъра), ж.к. Владислав Варненчик до бл. 402",
             kind="детска градина", lat=43.24947, lon=27.84418, zone=Z, old_names=[], status=""),
        dict(name="Детско заведение (без име в регистъра), ул. Георги Минков 2",
             kind="детска градина", lat=43.24855, lon=27.85095, zone=Z, old_names=[], status=""),
    ]
    rebuild(ADD)
    aft_ok, aft_bad = 0, []
    for r in BASE:
        rows, br, k = rank(r.name, r.name)
        if k == 1:
            aft_ok += 1
        else:
            aft_bad.append((r.name, k))
    print("   СЛЕД +5 (форма D/A, Владиславово): %d/%d · регресии: %d"
          % (aft_ok, len(BASE), base_ok - aft_ok))
    lost = set(n for n, _ in aft_bad) - set(n for n, _ in base_bad)
    for n in sorted(lost):
        print("       НОВА регресия: %s" % n)
    print()
    for q in ["детска градина владиславово", "детски градини владиславово",
              "детска градина ниш 29", "детско заведение владиславово",
              "детска градина шести септември 6"]:
        show(q, None, 8)


if __name__ == "__main__":
    main()
