"""Regenerate scratch/places_search/m7_trigger_tokens.json — measured, never hand-listed.

Usage:
  python gen_m7_tokens.py --check   # rebuild with the CURRENT engine and diff against
                                    # the tracked file -> GREEN means the tracked list
                                    # is what this engine answers today
  python gen_m7_tokens.py --write   # write the file with the CURRENT engine (F12-е)

Амандамент №4 т. 4: `--check` used to rebuild with the OLD literal branch, so it
was red BY CONSTRUCTION and its green never meant anything. The literal branch
is the deliberately broken input and it lives where broken inputs belong —
`m7_significance_gate.py --literal`. No tracked tool is red by design.
"""
import importlib.util
import json
import pathlib
import sys

# Runnable from the folder it lives in: the checkout is found relative to
# this file, never through a fixed path pinned to one machine (F12-ж).
REPO = pathlib.Path(__file__).resolve().parents[2]
TARGET = REPO / "scratch" / "places_search" / "m7_trigger_tokens.json"

spec = importlib.util.spec_from_file_location(
    "rs", str(REPO / "scratch" / "places_search" / "recall_sweep.py"))
rs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rs)


META_NEW = {
    "what": "М7 („голото място“, план §3й-б S4): всяка единична дума, която може да задейства клона.",
    "rule": "Дума в `qtk` или `ltk` на поне един изнесен ред И значима по правилото на останалата машина (F12-е: >2 знака в двете изписвания, без типов префикс „кв/жк/к/м/с/о/т/и“, без число, без общата дума на речника). `legtk` (старите зонови думи на реда) и `ktk` (видът) НЕ задействат — затова „зпз“ влиза САМО като днешната местност, не като наследена дума.",
    "how_to_reproduce": "зареди scratch/places_search/recall_sweep.py като модул и извикай search(<дума>) — клонът е `M7-bare-location`.",
}

FOR_SIGNATURE_NEW = [
    "„зпз“: и алиас на местността Западна промишлена зона, и наследена дума на реда — по правилото по-горе задейства САМО като местност (1 ред).",
    "F12-е (амандамент №2, решение 2) затвори дефекта: думите с `word_class` = „short“ (к, кв, м, о, с, т, жк, и, 1, 2) идват от ПРЕФИКСА на името („к.к.“, „кв.“, „м-т“, „с.о.“, „ж.к.“), не от мястото, и вече НЕ задействат клона — „к“ отговаряше със 163 реда, „кв“ с 36, днес и двете падат в M3 с 0. Остават в списъка с `triggers: false`, за да се вижда какво е изхвърлено.",
    "„приморски“ и „приморският“ са алиаси на местността Морска градина — затова районна на вид дума отговаря през М7. Контролата на Сол (гейт 6) очакваше M3; амандамент №2 решение 3 я приема като подписваема делта в манифеста P7→F12.",
    "Мярката пита с НОРМАЛИЗИРАНАТА дума. Затова „iug“ (латиница, 3 знака) задейства с 1 ред, а „юг“ — както го пише човек — не задейства (M3, 0 реда): токенът е `word_class` = „short“, защото в името „с.о. Боровец-юг“ е двузнаков.",
    "„св“ задейства (44 реда), защото токенизаторът разгъва съкращението в „свети“ ПРЕДИ правилото за дължина — това е същото правило, по което работи и останалата машина, не изключение.",
]


def word_class(tok, codes_by_cls):
    """Where the word COMES FROM, measured on the token the source wrote.

    „short“ = every occurrence is a type prefix or a numeral („к.к.“ → „к“,
    „Боровец-юг“ → „юг“, „Възраждане 1“ → „1“) · „significant“ = a word of the
    canonical NAME · „alias“ = only a word of an accepted alias of that code."""
    def big(t):
        return not t.num and len(t.orig) > 2 and len(t.s) > 2
    name_hits, alias_hits = [], []
    for cls, codes in codes_by_cls.items():
        for code in codes:
            for t in rs.place_tokens(rs.LOCATIONS[cls][code]["name"]):
                if t.s == tok:
                    name_hits.append(t)
            for t in rs.LOC_EXTRA.get(cls, {}).get(code, ()):
                if t.s == tok:
                    alias_hits.append(t)
    if any(big(t) for t in name_hits):
        return "significant"
    if any(big(t) for t in alias_hits):
        return "alias"
    return "short"


def build(meta, for_signature):
    per_token_codes = {}
    rows_carrying = {}
    for rec in rs.RECS:
        for cls, field, toks in ((u"quarter", rec.quarter, rec.qtk),
                                 (u"locality", rec.locality, rec.ltk)):
            if not field:
                continue
            code = field.get("code")
            # Counted per OCCURRENCE, exactly as the tracked file counts: „к.к.“
            # puts the token „k“ into `qtk` twice and the number says so.
            for tok in toks:
                per_token_codes.setdefault(tok, {}).setdefault(cls, {})
                per_token_codes[tok][cls][code] = per_token_codes[tok][cls].get(code, 0) + 1
                rows_carrying[tok] = rows_carrying.get(tok, 0) + 1
    tokens = []
    triggering = 0
    for tok in sorted(per_token_codes):
        rows, branch = rs.search(tok)[:2]
        triggers = branch == "M7-bare-location"
        triggering += 1 if triggers else 0
        classes = sorted(per_token_codes[tok])
        tokens.append({
            "token": tok,
            "classes": classes,
            "codes": {c: {k: per_token_codes[tok][c][k]
                          for k in sorted(per_token_codes[tok][c])} for c in classes},
            "rows_carrying_the_token": rows_carrying[tok],
            "triggers": triggers,
            "branch": branch,
            "rows_answered": len(rows),
            "word_class": word_class(tok, per_token_codes[tok]),
        })
    doc = {
        "_meta": dict(meta, measured={
            "tokens": len(tokens),
            "trigger_today": triggering,
            "rows_of_the_delivery": len(rs.RECS),
        }, for_signature=for_signature),
        "signed_by": "pending — Петър",
        "date": "2026-09-05",
        "tokens": tokens,
    }
    return json.dumps(doc, ensure_ascii=False, indent=1) + "\n"


if "--check" in sys.argv:
    text = build(META_NEW, FOR_SIGNATURE_NEW)
    tracked = TARGET.read_text(encoding="utf-8")
    print("the current engine reproduces the tracked file byte for byte:",
          text == tracked)
    if text != tracked:
        import difflib
        for line in list(difflib.unified_diff(tracked.splitlines(), text.splitlines(),
                                              "tracked", "rebuilt", lineterm=""))[:40]:
            print(line)
        sys.exit(2)
elif "--write" in sys.argv:
    text = build(META_NEW, FOR_SIGNATURE_NEW)
    TARGET.write_text(text, encoding="utf-8", newline=chr(10))
    doc = json.loads(text)
    print("written:", TARGET, "tokens", doc["_meta"]["measured"]["tokens"],
          "trigger_today", doc["_meta"]["measured"]["trigger_today"])
else:
    raise SystemExit("--check or --write")
