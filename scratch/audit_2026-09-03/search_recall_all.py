# -*- coding: utf-8 -*-
"""recall_all.py — READ-ONLY recall audit of the Fire_Varna places searcher.

Runs every one of the 361 loaded records (226 hotels + 135 places) through the
signed reference matcher (scratch/places_search/recall_sweep.py, imported as a
MODULE — main() is never called, the module writes nothing on import) with five
query shapes per record, plus a 20-query typo battery.

Q1  the full name exactly as it is stored
Q2  the name without quotes and without the type words / abbreviations
    (numbers, roman and arabic, stay)
Q3  kind word + Q2 name              ("детска градина Приказка")
Q4  kind word + zone without its type prefix ("детска градина Владиславово")
Q5  the single main word of the name ("Приказка")
Q6  20 typo queries, >=1 per group, each aimed at a named record

Everything is deterministic: no randomness, no clock, no argv, sorted output.
Writes ONLY into its own directory.
"""
import hashlib
import json
import os
import re
import sys

sys.dont_write_bytecode = True
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REF_DIR = r"C:/git/Fire_Varna/scratch/places_search"
HERE = os.path.dirname(os.path.abspath(__file__))

# --- guard: prove the reference writes nothing when imported -----------------
WATCH = [REF_DIR + "/recall_sweep_rows.json",
         REF_DIR + "/probe_out/token_parity.json"]


def _snap():
    d = {}
    for p in WATCH:
        d[p] = (hashlib.sha256(open(p, "rb").read()).hexdigest()
                if os.path.exists(p) else None)
    return d


_BEFORE = _snap()
sys.path.insert(0, REF_DIR)
import recall_sweep as rs                                    # noqa: E402
_AFTER = _snap()
assert _BEFORE == _AFTER, "IMPORT WROTE TO THE REFERENCE — ABORT"

TOP = rs.TOP                                                 # 8

# ---------------------------------------------------------------- vocabulary
# Type words and abbreviations stripped for Q2/Q3/Q5. Compared post-lowercase
# after dots/hyphens/quotes have already become separators, so "ц.д.г."
# and "ЦДГ" collapse to the same key.
TYPE_WORDS = set(u"""
дг одз цдг чдг дя оу су соу чоу чсу пг пмг ег гпче нуи
умбал мбал сбал сбагал сбалок дкц
хотел хотела хотелът апартхотел
училище училището училища гимназия гимназията
болница болницата хоспис университет университета университетът
ясла ясли яслата детска детски градина градини градината
""".split())
# multi-word type phrases removed BEFORE the single words (order matters)
TYPE_PHRASES = [[u"детска", u"градина"], [u"детски", u"градини"],
                [u"детска", u"ясла"], [u"детска", u"ясли"]]

# Words that are never "the main word" a human would type (Q5).
PARTICLES = set(u"""
свети св света свето доктор др проф професор академик акад инж
на по за и при със с във в от до край нов нова ново
варна варненски варненска варненско град гр бивше бивш бивша
ад еад еоод оод ооо дззд сдружение фондация
""".split())

KIND_WORD = {
    u"Хотел": u"хотел",
    u"Семеен хотел": u"хотел",
    u"хотел · без категоризация": u"хотел",
    u"апарт-хотел": u"хотел",
    u"училище": u"училище",
    u"университет": u"университет",
    u"болница": u"болница",
    u"ДКЦ": u"дкц",
    u"хоспис": u"хоспис",
    u"детска градина": u"детска градина",
}

ZONE_PREFIX = re.compile(u"^(\u0436\\.\u043a\\.|\u043a\\.\u043a\\.|\u043a\\.\u0437\\.|"
                         u"\u0441\\.\u043e\\.|\u043a\u0432\\.|\u043c-\u0442|\u043c\\.|"
                         u"\u0440\u0430\u0439\u043e\u043d)\\s+")
SEP = re.compile(u"[\\s.,\u2116\\-\u201e\u201c\u201d\u201a\u2018\u2019\u00ab\u00bb"
                 u"\u2013\u2014/()'\"]+")
CYR = re.compile(u"[\u0410-\u042f\u0430-\u044f]")
QUOTED = re.compile(u"\u201e([^\u201e\u201c]+)\u201c|\"([^\"]+)\"|"
                    u"\u201c([^\u201c\u201d]+)\u201d")


def words(s):
    return [w for w in SEP.split(s) if w]


def strip_types(ws):
    out = list(ws)
    for ph in TYPE_PHRASES:
        i = 0
        while i <= len(out) - len(ph):
            if [w.lower() for w in out[i:i + len(ph)]] == ph:
                del out[i:i + len(ph)]
            else:
                i += 1
    return [w for w in out if w.lower() not in TYPE_WORDS]


def q2_name(name):
    """name minus quotes minus type words; numbers kept, order kept"""
    return u" ".join(strip_types(words(name)))


def is_num(w):
    lw = w.lower()
    if w.isdigit():
        return True
    return bool(rs.ROMAN_SHAPE.match(lw) and rs.ROMAN_OK.match(lw))


def q5_main(name):
    """The one word a human would actually type. Returns (word, kind).
       Preference: (1) the innermost quoted segment if there is one,
       (2) cyrillic tokens over latin ones, (3) longest, ties -> the later one.
       Numbers only if nothing else survives."""
    cands = None
    m = QUOTED.findall(name)
    if m:
        seg = [g for g in m[-1] if g]
        if seg:
            c = strip_types(words(seg[0]))
            c = [w for w in c if w.lower() not in PARTICLES]
            if c:
                cands = c
    if cands is None:
        c = strip_types(words(name))
        cands = [w for w in c if w.lower() not in PARTICLES]
    real = [w for w in cands if not is_num(w)]
    if real:
        cyr = [w for w in real if CYR.search(w)]
        pool = cyr or real
        best = None
        for w in pool:
            if best is None or len(w) >= len(best):
                best = w
        return best, u"word"
    nums = [w for w in cands if is_num(w)]
    if nums:
        return nums[-1], u"number"
    return u"", u"none"


def zone_bare(zone):
    return ZONE_PREFIX.sub(u"", zone).strip()


# --------------------------------------------------------------------- probe
def probe(rec, qtype, q, note=u""):
    q = (q or u"").strip()
    if not q:
        return {"qtype": qtype, "q": q, "rank": None, "n": 0,
                "branch": u"\u2014", "first": u"", "first_zone": u"",
                "note": u"\u043f\u0440\u0430\u0437\u043d\u0430 \u0437\u0430\u044f\u0432\u043a\u0430"}
    rows, br = rs.search(q)
    rk = rs.rank_of(rows, rec)
    return {"qtype": qtype, "q": q,
            "rank": (rk + 1) if rk >= 0 else None,
            "n": len(rows), "branch": br,
            "first": rows[0].name if rows else u"",
            "first_zone": rows[0].zone if rows else u"",
            "note": note}


def pct(a, b):
    return u"%.1f%%" % (100.0 * a / b) if b else u"—"


def write_summary(payload, out_rows, by_q, by_grp_q, agg, twins, q4_bad):
    L = []
    A = L.append
    m = payload["_meta"]
    A(u"# Тест: излизат ли правилно всички 361 записа (Q1–Q6)")
    A(u"")
    A(u"Референция: `%s`" % m["reference"])
    A(u"sha256(recall_sweep.py) = `%s`" % m["reference_sha256"])
    A(u"Импортът не пише в референцията: **%s** "
      u"(sha256 на recall_sweep_rows.json и probe_out/token_parity.json "
      u"преди/след импорта са еднакви)." % m["import_writes_nothing"])
    A(u"CAPMODE = `%s` · FIX = `%s` · GEN_CAP = %d · TOP = %d"
      % (m["capmode"], json.dumps(m["fix"], sort_keys=True), m["gen_cap"],
         m["TOP"]))
    A(u"Записи: **%d** · редове в recall_all.json: **%d**"
      % (m["records"], m["rows"]))
    A(u"")
    A(u"## 1. Обобщение по вид заявка")
    A(u"")
    A(u"| заявка | какво е | n | recall@1 | recall@3 | recall@8 | не се "
      u"намира |")
    A(u"|---|---|---:|---:|---:|---:|---:|")
    WHAT = {"Q1": u"пълното име както е",
            "Q2": u"името без кавички и без типовите думи",
            "Q3": u"вид + име",
            "Q4": u"вид + квартал",
            "Q5": u"само главната дума",
            "Q6": u"20 типични грешки при писане"}
    for k in sorted(by_q):
        s = agg(by_q[k])
        A(u"| %s | %s | %d | %d (%s) | %d (%s) | %d (%s) | %d |"
          % (k, WHAT[k], s["n"], s["r1"], pct(s["r1"], s["n"]),
             s["r3"], pct(s["r3"], s["n"]), s["r8"], pct(s["r8"], s["n"]),
             s["miss"]))
    A(u"")
    A(u"> Q4 се чете иначе: „вид + квартал“ връща КАТЕГОРИЕН списък "
      u"(десетки редове, подредени по близост до центъра на кадъра), затова "
      u"recall@1/@3/@8 там мери подредбата, а дефектът е колоната "
      u"„не се намира“.")
    A(u"")
    A(u"## 2. По клас × вид заявка")
    A(u"")
    A(u"| клас | заявка | n | r@1 | r@3 | r@8 | не се намира |")
    A(u"|---|---|---:|---:|---:|---:|---:|")
    for k in sorted(by_grp_q):
        s = agg(by_grp_q[k])
        A(u"| %s | %s | %d | %d | %d | %d | %d |"
          % (k[0], k[1], s["n"], s["r1"], s["r3"], s["r8"], s["miss"]))
    A(u"")
    A(u"## 3. Записите, които НЕ се намират по собственото си име (Q1/Q2)")
    A(u"")
    A(u"| заявка | запис | клас | квартал | q | n | branch | първи ред |")
    A(u"|---|---|---|---|---|---:|---|---|")
    for x in out_rows:
        if x["qtype"] in ("Q1", "Q2") and x["rank"] is None:
            A(u"| %s | %s | %s | %s | `%s` | %d | %s | %s |"
              % (x["qtype"], x["name"], x["group"], x["zone"], x["q"],
                 x["n"], x["branch"], x["first"] or u"—"))
    A(u"")
    A(u"## 4. Двойките с еднакъв скелет — кой печели")
    A(u"")
    A(u"| скелет | n | branch | печели | членове (ранг) |")
    A(u"|---|---:|---|---|---|")
    for k, v in sorted(twins.items()):
        mem = u" · ".join(u"%s (%s) → %s" % (x["name"], x["zone"], x["rank"])
                          for x in v["members"])
        A(u"| `%s` | %d | %s | %s | %s |" % (k, v["n"], v["branch"],
                                             v["winner"], mem))
    A(u"")
    A(u"## 5. Q4 = 0: класове/квартали, при които „вид + квартал“ "
      u"не връща записа")
    A(u"")
    A(u"| клас · квартал | заявка | върнати редове | branch | първи ред | "
      u"липсващи |")
    A(u"|---|---|---:|---|---|---:|")
    for k, v in sorted(q4_bad.items()):
        A(u"| %s | `%s` | %d | %s | %s | %d |"
          % (k, v["q"], v["n"], v["branch"], v["first"] or u"—",
             len(v["names"])))
    A(u"")
    A(u"## 6. Q6 — 20-те най-чести грешки при писане")
    A(u"")
    A(u"| заявка | вид грешка | цел | ранг | n | branch | първи ред |")
    A(u"|---|---|---|---:|---:|---|---|")
    for x in out_rows:
        if x["qtype"] == "Q6":
            A(u"| `%s` | %s | %s | %s | %d | %s | %s |"
              % (x["q"], x["note"], x["name"], x["rank"], x["n"],
                 x["branch"], x["first"]))
    A(u"")
    A(u"## 7. Как са построени заявките (за повторяемост)")
    A(u"")
    A(u"* **Q2** — от името се махат кавичките и типовите думи/съкращения; "
      u"числата (арабски и римски) остават. Списък: `%s`."
      % u", ".join(m["type_words"]))
    A(u"* **Q3** — думата за вид (`хотел`, `училище`, `детска градина`, "
      u"`болница`, `университет`, `дкц`, `хоспис`) + Q2-името.")
    A(u"* **Q4** — думата за вид + кварталът без типовия си префикс "
      u"(`ж.к.`, `кв.`, `к.к.`, `к.з.`, `с.о.`, `м-т`, `м.`, `район`).")
    A(u"* **Q5** — една дума: ако името има кавички, най-дългата дума "
      u"вътре в тях; иначе най-дългата дума на името; кирилицата има "
      u"предимство пред латиницата; изключени са частиците: `%s`. "
      u"Ако не остане дума, се взема числото (маркирано `q5_kind=number`)."
      % u", ".join(m["particles"]))
    A(u"")
    A(u"## 8. Обхват на измереното")
    A(u"")
    A(u"Мерено е през Python-референцията `recall_sweep.py` (подписана, "
      u"1:1 с index.html по построение). Пълният JS-паритет е доказан за "
      u"103 заявки в C16 — паритетът за всичките %d заявки тук НЕ е мерен "
      u"в браузър и остава за проба на Сол." % len(out_rows))
    A(u"")
    txt = u"\n".join(L)
    q = os.path.join(HERE, "summary.md")
    f = open(q, "w", encoding="utf-8", newline="\n")
    f.write(txt)
    f.close()
    print(u"sha256(summary.md)=%s"
          % hashlib.sha256(txt.encode("utf-8")).hexdigest())


def main():
    recs = list(rs.RECS)
    skel_map = {}
    for r in recs:
        skel_map.setdefault(rs.key_of(r.name), []).append(r)

    out_rows = []
    for i, r in enumerate(recs):
        grp = rs.group_of(r)
        kw = KIND_WORD[r.kind]
        n2 = q2_name(r.name)
        main_w, main_kind = q5_main(r.name)
        zb = zone_bare(r.zone)
        sk = rs.key_of(r.name)
        base = {"i": i, "name": r.name, "kind": r.kind, "group": grp,
                "zone": r.zone, "zone_bare": zb, "skel": sk,
                "skel_twins": len(skel_map[sk]), "q5_kind": main_kind,
                "lat": r.lat, "lon": r.lon}
        qs = [
            ("Q1", r.name, u""),
            ("Q2", n2,
             u"\u0438\u0434\u0435\u043d\u0442\u0438\u0447\u043d\u0430 \u0441 Q1"
             if n2.strip() == r.name.strip() else u""),
            ("Q3", (kw + u" " + n2).strip(),
             u"\u0431\u0435\u0437 \u0438\u043c\u0435" if not n2 else u""),
            ("Q4", (kw + u" " + zb).strip(), u""),
            ("Q5", main_w,
             u"\u0433\u043b\u0430\u0432\u043d\u0430\u0442\u0430 \u0434\u0443\u043c\u0430 "
             u"\u0435 \u0447\u0438\u0441\u043b\u043e" if main_kind == "number"
             else (u"\u043d\u044f\u043c\u0430 \u0433\u043b\u0430\u0432\u043d\u0430 "
                   u"\u0434\u0443\u043c\u0430" if main_kind == "none" else u"")),
        ]
        for qt, q, note in qs:
            row = dict(base)
            row.update(probe(r, qt, q, note))
            out_rows.append(row)

    # ------------------------------------------------------------- Q6 typos
    by_name = {}
    for r in recs:
        by_name.setdefault(r.name, []).append(r)

    TYPOS = [
        (u"\u0410\u0414\u041c\u0418\u0420\u0410\u041b",
         u"\u0445\u043e\u0442\u0435\u043b \u0430\u0434\u043c\u0438\u0440\u0430\u043b\u043b",
         u"\u0443\u0434\u0432\u043e\u0435\u043d\u0430 \u0431\u0443\u043a\u0432\u0430"),
        (u"\u0410\u0414\u041c\u0418\u0420\u0410\u041b", u"hotel admiral",
         u"\u043d\u0430 \u043b\u0430\u0442\u0438\u043d\u0438\u0446\u0430"),
        (u"\u0410\u0414\u041c\u0418\u0420\u0410\u041b",
         u"\u0445\u043e\u0442\u0435\u043b \u0430\u0434\u043c\u0438\u0440a\u043b",
         u"\u0441\u043c\u0435\u0441\u0435\u043d\u0430 \u043a\u0438\u0440\u0438\u043b\u0438\u0446\u0430/\u043b\u0430\u0442\u0438\u043d\u0438\u0446\u0430 (a)"),
        (u"\u0425\u041e\u041b\u0418\u0414\u0415\u0419 \u041f\u0410\u0420\u041a",
         u"\u0445\u043e\u043b\u0438\u0434\u0435\u0438 \u043f\u0430\u0440\u043a",
         u"\u0439 -> \u0438"),
        (u"\u0411\u041e\u041d\u0418\u0422\u0410/BONITA", u"bonita hotel",
         u"\u043b\u0430\u0442\u0438\u043d\u0438\u0446\u0430 + \u043e\u0431\u0440\u0430\u0442\u0435\u043d \u0440\u0435\u0434"),
        (u"\u041f\u0410\u041b\u041c \u0411\u0418\u0419\u0427",
         u"\u043f\u0430\u043b\u043c \u0431\u0438\u0447",
         u"\u0438\u0437\u043f\u0443\u0441\u043d\u0430\u0442\u0430 \u0431\u0443\u043a\u0432\u0430"),
        (u"\u0414\u0413 39 \"\u041f\u0440\u0438\u043a\u0430\u0437\u043a\u0430\"",
         u"\u0434\u0435\u0442\u0441\u043a\u0430 \u0433\u0440\u0430\u0434\u0438\u043d\u0430 39",
         u"\u0441\u0430\u043c\u043e \u043d\u043e\u043c\u0435\u0440"),
        (u"\u0414\u0413 39 \"\u041f\u0440\u0438\u043a\u0430\u0437\u043a\u0430\"",
         u"\u0434\u0433 \u043f\u0440\u0438\u043a\u0430\u0437\u043a\u0430",
         u"\u0441\u044a\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0435 + \u0438\u043c\u0435"),
        (u"\u0414\u0413 39 \"\u041f\u0440\u0438\u043a\u0430\u0437\u043a\u0430\"",
         u"\u0446\u0434\u0433 \u043f\u0440\u0438\u043a\u0430\u0437\u043a\u0430",
         u"\u0433\u0440\u0435\u0448\u043d\u043e \u0441\u044a\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0435"),
        (u"\u0414\u0435\u0442\u0441\u043a\u0430 \u0433\u0440\u0430\u0434\u0438\u043d\u0430 "
         u"\"\u0416\u0438\u0440\u0430\u0444\u0447\u0435\"",
         u"\u0436\u0438\u0440\u0430\u0444\u0447\u0435",
         u"\u0441\u0430\u043c\u043e \u0438\u043c\u0435"),
        (u"3 \u041e\u0423 \u0410\u043d\u0433\u0435\u043b \u041a\u044a\u043d\u0447\u0435\u0432",
         u"\u043e\u0443 \u0430\u043d\u0433\u0435\u043b \u043a\u044a\u043d\u0447\u0435\u0432",
         u"\u0431\u0435\u0437 \u043d\u043e\u043c\u0435\u0440\u0430"),
        (u"3 \u041e\u0423 \u0410\u043d\u0433\u0435\u043b \u041a\u044a\u043d\u0447\u0435\u0432",
         u"\u0443\u0447\u0438\u043b\u0438\u0449\u0435 \u043a\u044a\u043d\u0447\u0435\u0432",
         u"\u0432\u0438\u0434 + \u0444\u0430\u043c\u0438\u043b\u0438\u044f"),
        (u"\u0421\u0423 \u201e\u041f\u0435\u0439\u043e \u041a\u0440\u0430\u0447\u043e\u043b\u043e\u0432 "
         u"\u042f\u0432\u043e\u0440\u043e\u0432\u201c",
         u"\u0441\u0443 \u044f\u0432\u043e\u0440\u043e\u0432",
         u"\u0441\u044a\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0435 + \u0444\u0430\u043c\u0438\u043b\u0438\u044f"),
        (u"\u0421\u0423 \u201e\u041f\u0435\u0439\u043e \u041a\u0440\u0430\u0447\u043e\u043b\u043e\u0432 "
         u"\u042f\u0432\u043e\u0440\u043e\u0432\u201c",
         u"\u0443\u0447\u0438\u043b\u0438\u0449\u0435 \u0438\u0430\u0432\u043e\u0440\u043e\u0432",
         u"\u044f -> \u0438\u0430"),
        (u"\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u0438 "
         u"\u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442 "
         u"\u201e\u041f\u0440\u043e\u0444. \u0434-\u0440 \u041f\u0430\u0440\u0430\u0441\u043a\u0435\u0432 "
         u"\u0421\u0442\u043e\u044f\u043d\u043e\u0432\u201c",
         u"\u043c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u0438 "
         u"\u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442 "
         u"\u0432\u0430\u0440\u043d\u0430",
         u"\u0434\u043e\u0431\u0430\u0432\u0435\u043d\u0430 \u0434\u0443\u043c\u0430"),
        (u"\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438 "
         u"\u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442 \u2013 "
         u"\u0412\u0430\u0440\u043d\u0430",
         u"\u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438 "
         u"\u0443\u043d\u0438\u0432\u0435\u0440\u0438\u0441\u0442\u0435\u0442",
         u"\u0440\u0430\u0437\u043c\u0435\u0441\u0442\u0435\u043d\u0438 \u0431\u0443\u043a\u0432\u0438"),
        (u"\u201e\u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u0441\u043a\u0430 "
         u"\u043c\u043d\u043e\u0433\u043e\u043f\u0440\u043e\u0444\u0438\u043b\u043d\u0430 "
         u"\u0431\u043e\u043b\u043d\u0438\u0446\u0430 \u0437\u0430 \u0430\u043a\u0442\u0438\u0432\u043d\u043e "
         u"\u043b\u0435\u0447\u0435\u043d\u0438\u0435 \u201e\u0421\u0432\u0435\u0442\u0430 "
         u"\u041c\u0430\u0440\u0438\u043d\u0430\u201c\u201c \u0415\u0410\u0414",
         u"\u0431\u043e\u043b\u043d\u0438\u0446\u0430 \u0441\u0432 \u043c\u0430\u0440\u0438\u043d\u0430",
         u"\u0441\u044a\u043a\u0440\u0430\u0442\u0435\u043d\u043e \u201e\u0441\u0432\u201c"),
        (u"\u201e\u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u0441\u043a\u0430 "
         u"\u043c\u043d\u043e\u0433\u043e\u043f\u0440\u043e\u0444\u0438\u043b\u043d\u0430 "
         u"\u0431\u043e\u043b\u043d\u0438\u0446\u0430 \u0437\u0430 \u0430\u043a\u0442\u0438\u0432\u043d\u043e "
         u"\u043b\u0435\u0447\u0435\u043d\u0438\u0435 \u201e\u0421\u0432\u0435\u0442\u0430 "
         u"\u041c\u0430\u0440\u0438\u043d\u0430\u201c\u201c \u0415\u0410\u0414",
         u"\u0443\u043c\u0431\u0430\u043b \u0441\u0432\u0435\u0442\u0430 \u043c\u0430\u0440\u0438\u043d\u0430",
         u"\u0430\u0431\u0440\u0435\u0432\u0438\u0430\u0442\u0443\u0440\u0430"),
        (u"\u201e\u0414\u041a\u0426 3 \u2013 \u0412\u0430\u0440\u043d\u0430\u201c "
         u"\u0415\u041e\u041e\u0414", u"\u0434\u043a\u04463",
         u"\u0441\u043b\u044f\u0442\u043e \u0441 \u0447\u0438\u0441\u043b\u043e\u0442\u043e"),
        (u"\u201e\u0425\u043e\u0441\u043f\u0438\u0441 \u041c\u0438\u0448\u0435\u043b "
         u"\u041f\u0430\u0440\u0435\u201c \u041e\u041e\u0414",
         u"\u0445\u043e\u0441\u043f\u0438\u0441 \u043c\u0438\u0448\u0435\u043b \u043f\u0430\u0440\u0435",
         u"\u043f\u044a\u043b\u043d\u043e \u0438\u043c\u0435, \u043c\u0430\u043b\u043a\u0438 "
         u"\u0431\u0443\u043a\u0432\u0438"),
    ]
    for nm, q, why in TYPOS:
        tgt = by_name.get(nm)
        assert tgt, u"Q6 target not in data: %r" % nm
        r = tgt[0]
        sk = rs.key_of(r.name)
        row = {"i": recs.index(r), "name": r.name, "kind": r.kind,
               "group": rs.group_of(r), "zone": r.zone,
               "zone_bare": zone_bare(r.zone), "skel": sk,
               "skel_twins": len(skel_map[sk]), "q5_kind": u"\u2014",
               "lat": r.lat, "lon": r.lon}
        row.update(probe(r, "Q6", q, why))
        out_rows.append(row)

    # --------------------------------------------------------------- summary
    def agg(rows):
        return {"n": len(rows),
                "r1": sum(1 for x in rows if x["rank"] == 1),
                "r3": sum(1 for x in rows if x["rank"] and x["rank"] <= 3),
                "r8": sum(1 for x in rows if x["rank"] and x["rank"] <= TOP),
                "miss": sum(1 for x in rows if x["rank"] is None)}

    by_q, by_grp_q = {}, {}
    for x in out_rows:
        by_q.setdefault(x["qtype"], []).append(x)
        by_grp_q.setdefault((x["group"], x["qtype"]), []).append(x)

    summary = {"by_qtype": dict((k, agg(v)) for k, v in sorted(by_q.items())),
               "by_group_qtype": dict((u"%s|%s" % k, agg(v))
                                      for k, v in sorted(by_grp_q.items()))}

    twins = {}
    for k, v in sorted(skel_map.items()):
        if len(v) > 1:
            rows, br = rs.search(v[0].name)
            twins[k] = {
                "branch": br, "n": len(rows),
                "winner": (rows[0].name + u" (" + rows[0].zone + u")")
                if rows else u"\u2014",
                "members": [{"name": m.name, "zone": m.zone, "kind": m.kind,
                             "rank": (rs.rank_of(rows, m) + 1)
                             if rs.rank_of(rows, m) >= 0 else None}
                            for m in v]}

    q4_bad = {}
    for x in out_rows:
        if x["qtype"] != "Q4" or x["rank"] is not None:
            continue
        k = u"%s | %s" % (x["group"], x["zone"])
        q4_bad.setdefault(k, {"q": x["q"], "n": x["n"], "branch": x["branch"],
                              "first": x["first"], "names": []})
        q4_bad[k]["names"].append(x["name"])

    payload = {
        "_meta": {
            "what": u"recall \u043d\u0430 361 \u0437\u0430\u043f\u0438\u0441\u0430 "
                    u"\u00d7 Q1..Q5 + 20 \u0437\u0430\u044f\u0432\u043a\u0438 Q6",
            "reference": REF_DIR + "/recall_sweep.py (imported, main() NOT run)",
            "reference_sha256": hashlib.sha256(
                open(REF_DIR + "/recall_sweep.py", "rb").read()).hexdigest(),
            "records": len(recs), "rows": len(out_rows), "TOP": TOP,
            "capmode": rs.CAPMODE, "fix": rs.FIX, "gen_cap": rs.GEN_CAP,
            "import_writes_nothing": _BEFORE == _AFTER,
            "type_words": sorted(TYPE_WORDS),
            "particles": sorted(PARTICLES)},
        "summary": summary,
        "skeleton_twins": twins,
        "q4_zero": q4_bad,
        "rows": out_rows}
    txt = json.dumps(payload, ensure_ascii=False, indent=1,
                     sort_keys=False) + "\n"
    p = os.path.join(HERE, "recall_all.json")
    f = open(p, "w", encoding="utf-8", newline="\n")
    f.write(txt)
    f.close()
    write_summary(payload, out_rows, by_q, by_grp_q, agg, twins, q4_bad)
    print(u"rows=%d -> %s" % (len(out_rows), p))
    print(u"sha256(recall_all.json)=%s"
          % hashlib.sha256(txt.encode("utf-8")).hexdigest())
    for k in sorted(by_q):
        s = agg(by_q[k])
        print(u"%-3s n=%4d  r@1=%4d  r@3=%4d  r@8=%4d  miss=%3d"
              % (k, s["n"], s["r1"], s["r3"], s["r8"], s["miss"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
