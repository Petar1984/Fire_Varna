# -*- coding: utf-8 -*-
"""
recall_sweep_v22.py — FINAL: copy of recall_sweep_v21.py with the four repairs
Petar signed on 02.09 switched ON (П2+П3+П4+П5+П6, WITHOUT П1), and the "парк" line
of A8 corrected as a FACT of the data and regenerated with sec.11 B1: 19 rows =
12 exact "ПАРК" first, then 7 fuzzy.
The diff v21 -> v22 IS the change list; the diff recall_sweep.py -> v21 is the
sec.10 amendment list.

  П2 (over A7) name coverage ^ between "active before бивш" and "distance ^"
  П3 (over A5) a numeric token with no EXACT match rejects the record
  П4 (over A1) a dictionary word with an EMPTY class is a name token AND a
     filter: a row without an EXACT name/alias match for it drops out
  П5 (over A5) without a key a 2-char word is significant on an EXACT match
     against a record whose whole name is that single token ("йо" -> Йо)
  П6 (over A5, signed sec.9 v1.4) without a key a 2-char token that matches a
     NAME token EXACTLY becomes significant when the query carries at least one
     MORE token that also matches the same record exactly ("7 су", "1 ег")

  A1  a form is a KEY only if its class holds >=1 loaded record; with several
      keys the LEFTMOST is the class, the rest become name tokens; if the search
      inside the class returns 0 rows -> retry with all keys as names (fail-open)
  A2  a ONE-TOKEN form also selects records whose kind tokens contain the chip's
      HEAD word (place_categories.json chips[].head)  -> "хотели" = 226
  A3  key + remainder that matches zone/kind tokens EXACTLY -> filtered category
      list, nearest first  ("хотел златни" = 85, "хотел семеен" = 50)
  A4  one token = one match, best by priority
      name-exact > alias > zone/kind-exact > name-prefix > name-fuzzy;
      an exact zone/kind match EATS the token (no fuzzy name credit for it)
  A5  significance: without a key >=3 original chars, not an address marker,
      not a number; with a key any exact/prefix non-numeric match also counts,
      and a purely numeric token counts only with a key and only exact
  A6  old_names are NAME TOKENS (not a phrase), minus tokens <=2 chars and
      address markers, and (ЛОТ 1в А4 т. 1) minus the generic GEOGRAPHIC words
      „варна“/„гр“/„град“; the CLASS words of an alias stay -- measured
  A0  ЛОТ 1в D2 + А4 т. 2: the WHOLE normalised alias is an index of its own
      (EXACT_ALIAS) and it is consulted BEFORE A1, but only for a query of at
      least two significant tokens
  A7  order: bestNameKind v (3/2/1) -> nameMatched v -> totalMatched v -> sum v
      -> active before "бивш" -> distance to centre ^ -> name length ^ -> bg abc
  A8  the M5 expectations as corrected by sec.10

READ-ONLY. Writes nothing but its own report next to itself.
NEVER prints cadastral identifiers (record["uins"] is not read at all).

Sources replicated 1:1:
  norm/skel/lev  -> C:/git/Fire_Varna/index.html lines 4786-4789
  TYPO/MARKERS/kindOf -> C:/git/varna_3d/web/poi-search.js lines 49, 97-151
  T1..M5 + sec.10 -> C:/git/Fire_Varna/docs/plans/places_search_plan_2026-09-02.md
"""
import datetime
import hashlib
import json
import math
import re
import sys
import io
import pathlib
import tempfile

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# The checkout this script lives in. INPUTS and artefacts alike are read and
# written relative to it, never through a fixed path: a worktree must re-freeze
# its own reference against ITS OWN data (F2-к0 for the outputs, F3-к for the
# inputs — a fixed path would have a worktree measure another checkout's bytes).
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
# Phase 2 (places_phase2_plan.md sec.8, lot C12): the reference reads the
# DELIVERED bytes of Fire_Varna -- the very three files the browser fetches --
# not the varna_3d originals. Identical content today; a divergence between the
# two repos must be loud in this gate, not silent.
HOTELS = str(REPO_ROOT / "data" / "hotels.json")
PLACES2 = str(REPO_ROOT / "data" / "places.json")
CATS = str(REPO_ROOT / "data" / "place_categories.json")
REPO_ROWS_OUT = str(REPO_ROOT / "scratch" / "places_search" / "recall_sweep_rows.json")
# С6′: the tokeniser-parity corpus the probe replays in the page. One generator,
# one file — the probe never invents the input list.
REPO_PARITY_OUT = str(REPO_ROOT / "scratch" / "places_search" / "probe_out"
                      / "token_parity.json")
# The human-readable report and the working copy of the rows are MEASUREMENTS,
# not deliverables: they land in the system temp — never in the repo, never in a
# session-specific scratch folder that dies with the session (F3-к).
OUTDIR = (pathlib.Path(tempfile.gettempdir()) / "fv_measures").as_posix() + "/"
# ЛОТ 1в-В (план §3ж S2) — the two modes. Until this lot every sweep rewrote the
# TRACKED reference, so the artefact Petar is asked to sign and the artefact the
# suite replays were one file: a run could freeze a change nobody had read. The
# tracked write now needs `--freeze` in so many words; anything else is
# REPORT-ONLY and writes the candidate + the old → new manifest into OUTDIR.
FREEZE = "--freeze" in sys.argv
REPORT_ONLY = not FREEZE
# F12-в: the two diffs Petar signs before anything is frozen. REPORT-ONLY by
# construction — it never touches the tracked reference, only writes the two
# manifests next to it, and `--freeze` and `--manifest` are refused together.
MANIFEST = "--manifest" in sys.argv
if MANIFEST and FREEZE:
    raise SystemExit(u"--manifest е report-only: не се съчетава с --freeze")
# Date only, so two runs of the same day are byte-equal (the determinism gate
# replays this script twice and compares).
GENERATED_AT = datetime.date.today().isoformat()

# Fire_Varna/index.html:1838  .setView([43.2141, 27.9147], 13)
# stand-in for map.getCenter() -- there is no map in a headless sweep.
CENTER = (43.2141, 27.9147)
TOP = 8

# ----------------------------------------------------------------- primitives
# index.html:4786 norm()   [unchanged from recall_sweep.py]
def norm(s):
    s = ("" if s is None else str(s)).lower()
    s = s.replace("\u0431\u043b\u043e\u043a", "\u0431\u043b")   # блок -> бл
    s = s.replace("\u0432\u0445\u043e\u0434", "\u0432\u0445")   # вход -> вх
    s = re.sub(r"[.\u2116,'\"\-]", " ", s)                      # [.№,'"-] -> space
    s = re.sub(r"\s+", " ", s)
    return s.strip()

# index.html:4787 skel()
_SKEL = {
    "\u0430": "a", "\u0431": "b", "\u0432": "v", "\u0433": "g", "\u0434": "d",
    "\u0435": "e", "\u0436": "zh", "\u0437": "z", "\u0438": "i", "\u0439": "i",
    "\u043a": "k", "\u043b": "l", "\u043c": "m", "\u043d": "n", "\u043e": "o",
    "\u043f": "p", "\u0440": "r", "\u0441": "s", "\u0442": "t", "\u0443": "u",
    "\u0444": "f", "\u0445": "h", "\u0446": "ts", "\u0447": "ch", "\u0448": "sh",
    "\u0449": "sht", "\u044a": "a", "\u044c": "", "\u044e": "yu", "\u044f": "ya",
}

def skel(w):
    w = w.lower()
    o = "".join(_SKEL.get(ch, ch) for ch in w)
    o = re.sub(r"[yj]", "i", o)
    o = re.sub(r"([^0-9])\1+", r"\1", o)   # JS /(\D)\1+/g ; \D == [^0-9]
    return o

# index.html:4788 lev()
def lev(a, b, cap):
    la, lb = len(a), len(b)
    if abs(la - lb) > cap:
        return cap + 1
    prev = list(range(lb + 1))
    for i in range(1, la + 1):
        cur = [i] * (lb + 1)
        best = i
        for j in range(1, lb + 1):
            v = min(prev[j] + 1, cur[j - 1] + 1,
                    prev[j - 1] + (0 if a[i - 1] == b[j - 1] else 1))
            cur[j] = v
            if v < best:
                best = v
        if best > cap:
            return cap + 1
        prev = cur
    return prev[lb]

# ------------------------------------------------------------------- T1 tokens
TYPO = re.compile(u"[\u201e\u201c\u201d\u201a\u2018\u2019\u00ab\u00bb\u2013\u2014/()]")

LET = u"\u0410-\u042f\u0430-\u044fA-Za-z"
NOL = u"(?<![" + LET + u"])"
NOR = u"(?![" + LET + u"])"
MARKERS = [
    (re.compile(NOL + u"\u0445\\s*-\\s*\u043b" + NOR, re.I), u" \u0445\u043e\u0442\u0435\u043b "),
    (re.compile(NOL + u"\u043a\\s*-\\s*\u0441" + NOR, re.I), u" \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0441 "),
    (re.compile(NOL + u"\u0434\\s*-\\s*\u0440" + NOR, re.I), u" \u0434\u043e\u043a\u0442\u043e\u0440 "),
    (re.compile(NOL + u"\u0441\u0432\\." , re.I), u" \u0441\u0432\u0435\u0442\u0438 "),
    (re.compile(NOL + u"\u0441\u0432" + NOR, re.I), u" \u0441\u0432\u0435\u0442\u0438 "),
]
ORD_SUF = re.compile(
    u"(\\d+)\\s*-?\\s*(\u043c\u0438|\u043c\u0430|\u043c\u043e|\u0442\u0438|\u0442\u0430|\u0442\u043e|"
    u"\u0432\u0438|\u0432\u0430|\u0432\u043e|\u0440\u0438|\u0440\u0430|\u0440\u043e)(?![" + LET + u"])", re.I)

_ORD_STEM = {
    u"\u043f\u044a\u0440\u0432": 1, u"\u0432\u0442\u043e\u0440": 2, u"\u0442\u0440\u0435\u0442": 3,
    u"\u0447\u0435\u0442\u0432\u044a\u0440\u0442": 4, u"\u043f\u0435\u0442": 5, u"\u0448\u0435\u0441\u0442": 6,
    u"\u0441\u0435\u0434\u043c": 7, u"\u043e\u0441\u043c": 8, u"\u0434\u0435\u0432\u0435\u0442": 9,
    u"\u0434\u0435\u0441\u0435\u0442": 10, u"\u0435\u0434\u0438\u043d\u0430\u0434\u0435\u0441\u0435\u0442": 11,
    u"\u0435\u0434\u0438\u043d\u0430\u0439\u0441\u0435\u0442": 11,
    u"\u0434\u0432\u0430\u043d\u0430\u0434\u0435\u0441\u0435\u0442": 12,
    u"\u0434\u0432\u0430\u043d\u0430\u0439\u0441\u0435\u0442": 12,
}
_ORD_END = [u"\u0438", u"\u0430", u"\u043e", u"\u0438\u044f\u0442", u"\u0438\u044f",
            u"\u0430\u0442\u0430", u"\u043e\u0442\u043e", u"\u0438\u0442\u0435"]
ORD_WORDS = {}
for _st, _n in _ORD_STEM.items():
    for _e in _ORD_END:
        ORD_WORDS[_st + _e] = str(_n)

# sec.11 B1: compounds norm() cannot split, because they carry no separator at all.
COMPOUNDS = {u"апартхотел": [u"апарт", u"хотел"],
             u"апарткомплекс": [u"апарт", u"комплекс"]}

ROMAN_OK = re.compile(r"^(x{0,3})(ix|iv|v?i{0,3})$")
ROMAN_SHAPE = re.compile(r"^[ivx]{1,5}$")
_RV = {"i": 1, "v": 5, "x": 10}

def roman_to_arabic(t):
    tot, prev = 0, 0
    for ch in reversed(t):
        v = _RV[ch]
        tot += -v if v < prev else v
        if v > prev:
            prev = v
    return str(tot)


class Tok(object):
    __slots__ = ("s", "orig", "num")

    def __init__(self, s, orig, num):
        self.s = s
        self.orig = orig
        self.num = num


def place_tokens(s):
    """plan sec.3 T1 -> list[Tok]"""
    raw = "" if s is None else str(s)
    raw = TYPO.sub(" ", raw)
    raw = raw.replace(u"\u0406", "I").replace(u"\u0456", "i")
    for rx, to in MARKERS:
        raw = rx.sub(to, raw)
    raw = ORD_SUF.sub(r"\1", raw)
    n = norm(raw)
    if not n:
        return []
    out = []
    for w in n.split(" "):
        if not w:
            continue
        # B1: a split compound yields two tokens, and both keep the WHOLE word
        # as their original -- significance (A5) reads the original, not the part.
        for part in COMPOUNDS.get(w, [w]):
            # §11 Р10: the bare „др“ is a TOKEN-level rewrite in the client
            # (rewriteToken) and in tests/test_places_search_primitives.py; the
            # MARKERS above only catch the hyphenated „д-р“. The original stays
            # „др“ — А5 reads the original, and the client keeps it too.
            if part == u"др":
                part = u"доктор"
            if ROMAN_SHAPE.match(part) and ROMAN_OK.match(part):
                out.append(Tok(roman_to_arabic(part), w, True))
                continue
            if part in ORD_WORDS:
                out.append(Tok(ORD_WORDS[part], w, True))
                continue
            if part.isdigit():
                out.append(Tok(part, w, True))
                continue
            sk = skel(part)
            if sk:
                out.append(Tok(sk, w, False))
    return out


def key_of(s):
    return " ".join(t.s for t in place_tokens(s))


# ------------------------------------------------------------------ T2 / K2
cats = json.load(open(CATS, encoding="utf-8"))
hotels = json.load(open(HOTELS, encoding="utf-8"))["hotels"]
places2 = json.load(open(PLACES2, encoding="utf-8"))["places"]

# --- A2: chip -> head  (place_categories.json chips[] carries "head")
CHIP_HEAD = {}
for _c in cats["chips"]:
    CHIP_HEAD[_c["chip"]] = _c.get("head") or _c["chip"]

# form-key -> {chips: chip-keys, heads: head-keys, forms: raw forms}
FORM_IDX = {}
for form, chips in cats["forms"].items():
    fk = key_of(form)
    if not fk:
        continue
    e = FORM_IDX.setdefault(fk, {"chips": set(), "heads": set(), "forms": set()})
    e["forms"].add(form)
    for c in chips:
        e["chips"].add(key_of(c))
        e["heads"].add(key_of(CHIP_HEAD.get(c, c)))

# LOT 1, amendment 8 P2 (Petar's signature, 03.09): the words that ask for MORE
# THAN ONE delivered kind. The dictionary already maps a form to a SET of chips
# („заведение“ -> three), but its own „детско заведение“ chip counts 3D bodies,
# not our rows, and the dictionary is a delivery from varna_3d that is never
# hand-edited — so the binding of the word to OUR kinds lives here. index.html
# carries the same table (EXTRA_FORMS); a drift between the two is a failed gate.
# Only the chip set is widened: `heads` drives the ONE-token A2 rule and both
# words here are two tokens, so a head would be dead weight.
EXTRA_FORMS = {
    u"детско заведение": [u"детска градина", u"детска ясла"],
    u"детски заведения": [u"детска градина", u"детска ясла"],
}
for form, kinds in EXTRA_FORMS.items():
    fk = key_of(form)
    if fk:
        e = FORM_IDX.setdefault(fk, {"chips": set(), "heads": set(), "forms": set()})
        e["forms"].add(form)
        for c in kinds:
            e["chips"].add(key_of(c))
MAXFORM = 3   # plan sec.3 T2: forms up to 3 tokens

# A5: address markers are never significant (post-norm forms: блок->бл, вход->вх)
ADDR = set([u"\u0431\u043b", u"\u0431\u043b\u043e\u043a", u"\u0432\u0445",
            u"\u0432\u0445\u043e\u0434", u"\u0443\u043b", u"\u0431\u0443\u043b",
            u"\u043a\u0432", u"\u0436\u043a", u"\u2116"])

# ЛОТ 1в, амандамент А4 т. 1 (ADR 008 D2): the generic GEOGRAPHIC words of an alias
# never become name tokens — „Висше военноморско училище, Варна“ would otherwise
# answer for the whole city on „варна“. The CLASS words of an alias STAY:
# measured 04.09, without „училище“ in `aset` the ВВМУ falls to SECOND on
# „военноморско училище“ behind the П2 coverage of „Спортно училище“.
ALIAS_GENERIC = set([skel(u"\u0432\u0430\u0440\u043d\u0430"), skel(u"\u0433\u0440"), skel(u"\u0433\u0440\u0430\u0434")])


# ---------------------------------------------------------------- \u041f7 (\u00a711 v2.1)
# The registry's other spellings of a quarter become ZONE tokens of the records
# that sit in it, so \u201e\u0432\u043b\u0430\u0434\u0438\u0441\u043b\u0430\u0432\u043e\u0432\u043e \u0434\u0435\u0442\u0441\u043a\u0430 \u0433\u0440\u0430\u0434\u0438\u043d\u0430\u201c reaches both spellings of the
# same place. ONE rule, two implementations: this and index.html buildIndex.
# Nothing here ever touches ntk/nset/aset \u2014 the name path (\u041f2) is untouched.
def name_quality(t, v):
    """index.html quality() verbatim: 3 exact / 2 prefix / 1 lev<=2 from 4 chars.

    Step (\u0436) must not move with the counterfactual variants below (the index is
    built once, at import), so it reads the SIGNED cap, not FIX/CAPMODE."""
    if t.num:
        return 3 if v == t.s else 0
    if len(t.orig) <= 1:
        return 0
    if v == t.s:
        return 3
    if v.startswith(t.s):
        return 2
    return 0 if len(t.orig) <= 3 else (1 if lev(t.s, v, 2) <= 2 else 0)


def zone_alias_tokens(cats_doc, zones):
    """\u00a711 steps (\u0430)-(\u0435) + (\u0434\u2032) \u2014 the per-zone CANDIDATES, before step (\u0436).

    Fail-soft (\u04217\u2032): without a well-formed `zones` object \u041f7 is simply off.
    Returns (extra, added, dropped): extra {zone: [Tok]}, added {zone: [str]},
    dropped {zone: ["reason:token"]}."""
    zdict = (cats_doc or {}).get("zones")
    if not isinstance(zdict, dict):
        return {}, {}, {}
    meta = (cats_doc or {}).get("_meta") or {}

    def family(z):
        e = zdict.get(z)
        return (e.get("family") or z) if isinstance(e, dict) else z

    own = dict((z, set(t.s for t in place_tokens(z))) for z in zones)
    generic = set()
    for word in (meta.get("zone_generic_words") or []):
        for t in place_tokens(word):
            generic.add(t.s)
    # (\u0434\u2032) \u04201: a token that IS, or is within lev<=2 of, an own token of a zone
    # from ANOTHER family is a foreign name \u2014 `primorski`/`primorskiat` fall here.
    # The >=3 floor is mandatory: without it `zpz` dies against \u201ezh\u201c.
    foreign = {}
    for z in zones:
        foreign[z] = set(tok for z2 in zones if family(z2) != family(z)
                         for tok in own[z2] if len(tok) >= 3)

    extra, added, dropped = {}, {}, {}
    for z in zones:
        e = zdict.get(z)
        aliases = e.get("aliases") if isinstance(e, dict) else None
        if not isinstance(aliases, list):
            continue
        for alias in aliases:
            if not isinstance(alias, str):
                continue
            for t in place_tokens(alias):
                why = None
                if t.num:                                        # (\u0430)
                    why = "num"
                elif len(t.orig) <= 2 or len(t.s) <= 2:          # (\u0431)
                    why = "short"
                elif t.orig in ADDR:                             # (\u0432)
                    why = "addr"
                elif t.s in generic:                             # (\u0433)
                    why = "generic"
                elif t.s in own[z]:                              # (\u0435)
                    why = "own"
                else:
                    for fk in foreign[z]:                        # (\u0434) + (\u0434\u2032)
                        if fk == t.s or lev(t.s, fk, 2) <= 2:
                            why = "foreign:" + fk
                            break
                if why:
                    tag = why + ":" + t.s
                    if tag not in dropped.setdefault(z, []):
                        dropped[z].append(tag)
                elif t.s not in added.setdefault(z, []):
                    added[z].append(t.s)
                    extra.setdefault(z, []).append(t)
    for z in added:
        added[z].sort()
    return extra, added, dropped


ZONES_IN = sorted(set([h["zone"] for h in hotels] + [p["zone"] for p in places2]))
# ЛОТ 1в-В: `zones` + П7 are SUPERSEDED by the three typed dictionaries below and
# feed nothing but `check_p7_gate()`, which pins the old flat zone list and is
# RED until Petar signs the manifest. They are kept so that gate can fail loudly
# with a named difference instead of crashing on a missing name.
ZONE_EXTRA, P7_ADDED, P7_DROPPED = zone_alias_tokens(cats, ZONES_IN)

# ============================================== ЛОТ 1в-В (план §3г, §3ж S3/S6)
# The delivery stopped carrying ONE „zone“ string: every record now has three
# TYPED fields — `quarter` | `district` | `locality`, each `null` or
# {name, src, code} — and the dictionary answers with three SEPARATE (class,
# code) dictionaries plus `legacy_by_row`. The class travels with the word
# because „младост“ is a quarter AND a district; one flat token set could not
# tell them apart, and that is exactly what put СУ „Гео Милев“ in a drawn
# industrial-zone hull. `zone` stays as the compat label (quarter?.name ??
# „район “ + district.name) until G-ZERO-ZONE.
LOC_CLASSES = (u"quarter", u"district", u"locality")

GENERIC_TOKENS = set()
for _w in ((cats.get("_meta") or {}).get("zone_generic_words") or []):
    for _t in place_tokens(_w):
        GENERIC_TOKENS.add(_t.s)


def significant_token(t):
    """Steps (а)-(г) of П7 on ONE token — the rule the whole machine shares.

    F12-е: it used to live only inside `significant_tokens` below, so the М7
    branch (which reads QUERY tokens, not a location string) could not ask it
    and fell back on the number filter alone. One rule, one place to read it."""
    return (not t.num and len(t.orig) > 2 and len(t.s) > 2
            and t.orig not in ADDR and t.s not in GENERIC_TOKENS)


def significant_tokens(s):
    """The phrase filter of П7 steps (а)-(г): what is left of a location string.

    A number, a token of <=2 characters, an address marker and the dictionary's
    own generic words („район“, „квартал“, „зона“…) never carry a place: that is
    why „район Младост“ and „Младост“ are ONE phrase and „район“ alone is none."""
    return [t.s for t in place_tokens(s) if significant_token(t)]


def location_dicts(cats_doc):
    """{class: {code: {"name", "aliases"}}} — fail-soft exactly like П7.

    A `locations` that is not an object, an entry without a name or an alias
    that is not a string switches that class off; nothing throws and the rest
    of the index still stands (С7′)."""
    out = dict((c, {}) for c in LOC_CLASSES)
    loc = (cats_doc or {}).get("locations")
    if not isinstance(loc, dict):
        return out
    for cls in LOC_CLASSES:
        entries = loc.get(cls)
        if not isinstance(entries, dict):
            continue
        for code, e in entries.items():
            if not isinstance(e, dict) or not isinstance(e.get("name"), str) or not e["name"]:
                continue
            aliases = e.get("aliases")
            out[cls][code] = {
                "name": e["name"],
                "aliases": [a for a in (aliases if isinstance(aliases, list) else [])
                            if isinstance(a, str)],
            }
    return out


def location_alias_tokens(entries):
    """П7 steps (а)-(е) + (д′), scoped INSIDE one class (план §3ж S3).

    „Foreign“ is measured against the other entries OF THE SAME CLASS only. The
    class travels with the word, so the district „Младост“ can no longer veto
    the quarter „ж.к. Младост 2“ — as one flat zone list it did, and the two
    spellings of one quarter fought each other. Returns (extra, added, dropped)
    keyed by code; `extra` holds Tok objects, `added`/`dropped` are strings."""
    own = dict((code, set(t.s for t in place_tokens(e["name"])))
               for code, e in entries.items())
    foreign = {}
    for code in entries:
        foreign[code] = set(tok for c2 in entries if c2 != code
                            for tok in own[c2] if len(tok) >= 3)
    extra, added, dropped = {}, {}, {}
    for code, e in entries.items():
        for alias in e["aliases"]:
            for t in place_tokens(alias):
                why = None
                if t.num:                                        # (а)
                    why = "num"
                elif len(t.orig) <= 2 or len(t.s) <= 2:          # (б)
                    why = "short"
                elif t.orig in ADDR:                             # (в)
                    why = "addr"
                elif t.s in GENERIC_TOKENS:                      # (г)
                    why = "generic"
                elif t.s in own[code]:                           # (е)
                    why = "own"
                else:
                    for fk in foreign[code]:                     # (д) + (д′)
                        if fk == t.s or lev(t.s, fk, 2) <= 2:
                            why = "foreign:" + fk
                            break
                if why:
                    tag = why + ":" + t.s
                    if tag not in dropped.setdefault(code, []):
                        dropped[code].append(tag)
                elif t.s not in added.setdefault(code, []):
                    added[code].append(t.s)
                    extra.setdefault(code, []).append(t)
    for code in added:
        added[code].sort()
    return extra, added, dropped


def location_phrases(entries, added):
    """{code: {phrase}} — the canonical name and every ACCEPTED alias form.

    Same rule as ЛОТ 1 decision 1, one class at a time: an alias becomes a
    phrase only when every significant token of it is already a token of that
    entry (its own, or one the step above accepted). The ORDER and the
    boundaries are the point — „морска градина“ is a phrase, „градина“ is not."""
    out = {}
    for code, e in entries.items():
        own = significant_tokens(e["name"])
        allowed = set(own) | set(added.get(code) or ())
        forms = set([u" ".join(own)]) if own else set()
        for alias in e["aliases"]:
            tk = significant_tokens(alias)
            if tk and all(t in allowed for t in tk):
                forms.add(u" ".join(tk))
        out[code] = forms
    return out


LOCATIONS = location_dicts(cats)
LOC_EXTRA, LOC_ADDED, LOC_DROPPED, LOC_PHRASES = {}, {}, {}, {}
for _cls in LOC_CLASSES:
    LOC_EXTRA[_cls], LOC_ADDED[_cls], LOC_DROPPED[_cls] = location_alias_tokens(LOCATIONS[_cls])
    LOC_PHRASES[_cls] = location_phrases(LOCATIONS[_cls], LOC_ADDED[_cls])


def bundle_digests(path):
    """Both digests of ONE content: the LF blob and its CRLF twin.

    Measured 04.09: varna_3d's own gate digests its WORKING-TREE bytes and that
    checkout stores `fire_varna_hotels.json` with CRLF, so the dictionary
    carries the CRLF digest for the hotels and the LF one for the places — the
    same content, two line endings. Content identity is what protects the
    ordinals, so both spellings of it are accepted and nothing else is."""
    raw = pathlib.Path(path).read_bytes().replace(b"\r\n", b"\n")
    return set([hashlib.sha256(raw).hexdigest(),
                hashlib.sha256(raw.replace(b"\n", b"\r\n")).hexdigest()])


# `legacy_by_row` is keyed by the ORDINAL of the row in its bundle, so it is only
# ever as true as the bundle it was built against: a re-export that reorders the
# rows would move every old word onto a stranger. The dictionary carries the SHA
# of both bundles; a mismatch switches the legacy words OFF (fail-closed), it
# never guesses. The words are INDEXED only — never shown, never a district alias.
LEGACY_BUNDLE_SHA = ((cats.get("_meta") or {}).get("legacy_bundle_sha") or {})
LEGACY_SHA_OK = all(LEGACY_BUNDLE_SHA.get(key) in bundle_digests(path)
                    for key, path in (("places", PLACES2), ("hotels", HOTELS)))
LEGACY_BY_ROW = (cats.get("legacy_by_row") or {}) if LEGACY_SHA_OK else {}
if not isinstance(LEGACY_BY_ROW, dict):
    LEGACY_BY_ROW = {}


# A legacy word that IS a dictionary entry inherits ITS forms: „Западна
# промишлена зона“ was delivered as a zone yesterday and the dictionary knows
# „ЗПЗ“ for it, so the row that used to carry it stays reachable by both. Only
# the quarter and the locality classes are consulted — a district is never a
# per-row word, it has a branch of its own.
LEGACY_LOOKUP = {}
for _cls in (u"quarter", u"locality"):
    for _code, _forms in LOC_PHRASES[_cls].items():
        _own = u" ".join(significant_tokens(LOCATIONS[_cls][_code]["name"]))
        if _own:
            LEGACY_LOOKUP.setdefault(_own, []).append((_cls, _code))


def legacy_of(bundle, ordinal):
    """(words, tokens, phrases) of ONE row — [] when the SHA guard is closed."""
    words = LEGACY_BY_ROW.get(u"%s:%d" % (bundle, ordinal))
    words = [w for w in words if isinstance(w, str)] if isinstance(words, list) else []
    tokens, phrases = [], set()

    def add(tk):
        phrases.add(u" ".join(tk))
        for t in tk:
            if t not in tokens:
                tokens.append(t)

    for word in words:
        tk = significant_tokens(word)
        if not tk:
            continue
        add(tk)
        for cls, code in LEGACY_LOOKUP.get(u" ".join(tk), ()):
            for form in LOC_PHRASES[cls][code]:
                add(form.split(u" "))
    return words, tokens, phrases


class Rec(object):
    def __init__(self, h, bundle=u"", ordinal=-1):
        self.name = h["name"]
        self.kind = h["kind"]
        self.zone = h["zone"]
        self.status = h.get("status") or ""
        self.lat = h["lat"]
        self.lon = h["lon"]
        self.ntk = [t.s for t in place_tokens(self.name)]
        self.nset = set(self.ntk)
        self.ktk = [t.s for t in place_tokens(self.kind)]
        # ЛОТ 1в-В: the three TYPED fields of the delivery, each with its own
        # token set and its own phrase set. `zone` is only the compat label now.
        self.quarter = h.get("quarter") or None
        self.district = h.get("district") or None
        self.locality = h.get("locality") or None
        self.p7 = []
        self.qtk = self._loc_tokens(u"quarter", self.quarter)
        self.ltk = self._loc_tokens(u"locality", self.locality)
        self.qph = self._loc_phrases(u"quarter", self.quarter)
        self.lph = self._loc_phrases(u"locality", self.locality)
        self.dph = self._loc_phrases(u"district", self.district)
        self.bundle = bundle                              # „hotels“ | „places“
        self.ordinal = ordinal                            # its row in THAT bundle
        self.legacy, self.legtk, self.gph = legacy_of(bundle, ordinal)
        # The token set the matcher reads as „zone/kind“: kind + quarter +
        # locality + the row's own legacy words. The DISTRICT is deliberately
        # out of it — „младост“ must not filter every school of the district
        # through A3′; the district has a branch of its own (план §3ж S3).
        self.zkset = set(self.qtk) | set(self.ltk) | set(self.legtk) | set(self.ktk)
        self.kkey = " ".join(self.ktk)
        # A6: old_names are NAME TOKENS, minus <=2 chars and address markers.
        # ЛОТ 1в А4 т. 1: minus the generic geographic words as well — the class
        # words stay, which is what puts the ВВМУ first on „военноморско училище“.
        # D1/D3: the alias STRINGS and their sources travel with the record, so the
        # index below can key the whole phrase and the card can name its source.
        self.old_names = list(h.get("old_names") or [])
        self.old_src = list(h.get("old_names_src") or [])
        self.aset = set()
        for o in self.old_names:
            for t in place_tokens(o):
                if t.num:
                    continue
                if len(t.orig) <= 2 or t.orig in ADDR:
                    continue
                if t.s in ALIAS_GENERIC:
                    continue
                self.aset.add(t.s)
        # ЛОТ 1в-Б (ADR 008 D6, план §2г S4): the ORDERED street phrase and the
        # house number as the DELIVERY wrote them. 1:1 with the client, and OUTSIDE
        # nset/aset/zkset — the name path and П7 neither see them nor are moved
        # by them. The client does not parse `text` either; both read these fields.
        _addr = h.get("address") or None
        self.address = _addr
        self.spk = key_of(_addr["street_phrase"]) if _addr else u""
        self.hkey = key_of(_addr["house_key"]) if _addr else u""
        dy = (self.lat - CENTER[0]) * 110574.0
        dx = (self.lon - CENTER[1]) * 81152.0
        self.dist = math.hypot(dx, dy)

    def _loc_tokens(self, cls, field):
        """Own tokens of a typed field + the ACCEPTED aliases of its code.

        П7 step (ж) survives whole: an alias token that touches a NAME token of
        THIS record (exact, prefix or fuzzy) is dropped for this record alone,
        so a location word can never displace the name path."""
        if not field:
            return []
        out = [t.s for t in place_tokens(field.get("name") or u"")]
        for t in LOC_EXTRA.get(cls, {}).get(field.get("code"), ()):
            if any(name_quality(t, v) > 0 for v in self.ntk):
                continue
            if t.s not in out:
                out.append(t.s)
                if cls == u"quarter":
                    self.p7.append(t.s)
        return out

    def _loc_phrases(self, cls, field):
        """The phrase forms of a typed field — {} when the field is null."""
        if not field:
            return set()
        return set(LOC_PHRASES.get(cls, {}).get(field.get("code")) or set())


# Phase 2: ONE index, two deliveries. `kind` carries the class of every record
# (hotels: 4 kinds; places: school/university/hospital/DKC/hospice/kindergarten).
# Nothing else in the matcher knows which file a row came from.
RECS = ([Rec(h, u"hotels", n) for n, h in enumerate(hotels)]
        + [Rec(p, u"places", n) for n, p in enumerate(places2)])

# ЛОТ 1, decision 2 — the exact-CURRENT-name index: joined name tokens -> records.
# old_names stay out of it on purpose (measured: 0 old-name keys coincide with a
# populated category key, and a global alias index would wake „ИУ“/„МУ“).
EXACT_NAME = {}
for _rec in RECS:
    EXACT_NAME.setdefault(u" ".join(_rec.ntk), []).append(_rec)

# ЛОТ 1в, ADR 008 D2 (S1) — the exact-ALIAS index: the WHOLE normalised alias
# maps to (record, index of that alias). A6 indexes an alias as separate TOKENS,
# so the full string „Висше военноморско училище, Варна“ loses to the class
# key „училище“ (A1 blocks the fail-open). The index is consulted BEFORE A1,
# exactly as EXACT_NAME stands before the category list.
EXACT_ALIAS = {}
for _rec in RECS:
    for _i, _old in enumerate(_rec.old_names):
        _k = key_of(_old)
        if not _k:
            continue
        _bucket = EXACT_ALIAS.setdefault(_k, [])
        if not any(_r is _rec for _r, _j in _bucket):
            _bucket.append((_rec, _i))


# ЛОТ 1в-Б, ADR 008 D6 — the WHOLE street phrase maps to the records on it. A
# partial phrase is not a street: „<улица> <номер>“ and „<клас> <улица>“ both ask
# for the street the delivery named, and a number behind a phrase that is nobody's
# whole street never takes part (план §2г S4). 1:1 with index.html `STREET`.
STREET = {}
for _rec in RECS:
    if _rec.spk:
        STREET.setdefault(_rec.spk, []).append(_rec)

# The prefix the SOURCE wrote, never one we add. „№“ is dropped with them.
STREET_MARK = (u"ул", u"бул", u"пл")


def street_rows(R, cls):
    """ЛОТ 1в-Б (ADR 008 D6) — the A3-street branch; None = not a street query.

    Reads `spk`/`hkey` and NOTHING else: no nset, no aset, no zkset, no
    significant(), no A5. When the phrase is ALSO an exact name or zone/kind token
    of the searched set, the street is chosen only if the human said „ул./бул./пл.“
    or named a house number — otherwise the name path keeps the query untouched.
    """
    if not STREET:
        return None
    marked = any(t.orig in STREET_MARK for t in R)
    rest = [t for t in R if t.orig not in STREET_MARK and t.orig != u"№"]
    if not rest:
        return None
    num = rest[-1] if rest[-1].num else None
    phrase = rest[:-1] if num else rest
    if not phrase or any(t.num for t in phrase):
        return None
    hits = STREET.get(u" ".join(t.s for t in phrase))
    if not hits:
        return None                              # not a whole street -> not a street
    if not marked and not num:
        for t in phrase:
            for rec in cls:
                if t.s in rec.nset or t.s in rec.zkset:
                    return None
    keep = set(id(r) for r in cls)
    rows = [r for r in hits if id(r) in keep]
    if num:
        rows = [r for r in rows if r.hkey == num.s]
    return order_category(rows) if rows else None


def alias_significant(qt):
    """Амандамент А4 т. 2: the significant tokens of a query, A5's own filter.

    A one-word query never reaches EXACT_ALIAS: measured 04.09, „синчец“ has to
    keep ДГ 30 „Синчец“ first (a CURRENT name must not lose to somebody's OLD
    one on a partial match), and the alias tokens are in `aset` anyway.
    """
    return sum(1 for t in qt
               if (not t.num) and len(t.orig) > 2 and t.orig not in ADDR)


def exact_alias(qt):
    """The records whose WHOLE alias is exactly this query. [] = no such thing."""
    if alias_significant(qt) < 2:
        return []
    return EXACT_ALIAS.get(u" ".join(t.s for t in qt)) or []


def in_class(rec, fk):
    """plan sec.3 K2 + A2:
       (a) kindKey in the form's chips;
       (b) the form is ONE token and that token is in the kind's tokens (K2b);
       (c) A2: the form is ONE token and the chip's HEAD (tokenised) sits inside
           the kind's tokens -> "хотели"/"хотелите" reach апарт-хотел too."""
    e = FORM_IDX[fk]
    if rec.kkey in e["chips"]:
        return True
    parts = fk.split(" ")
    if len(parts) == 1:
        if parts[0] in rec.ktk:
            return True
        for hk in e["heads"]:                                   # A2
            hp = hk.split(" ")
            if hp and all(p in rec.ktk for p in hp):
                return True
    return False


# A1: a form is a KEY only if its class holds >=1 loaded record.
CLASS_OF = {}
for fk in FORM_IDX:
    CLASS_OF[fk] = [r for r in RECS if in_class(r, fk)]

# --- phase 2, Sol C3: the classes AS THE HUMAN ASKS FOR THEM. The four hotel
# kinds are ONE group ("Хотели"); every other kind is its own group. The group is
# also the unit of the M3/B2 generosity gate below (index.html render() groups by
# exactly this table, so the reference and the browser cut the same way).
KIND_GROUP = {
    u"Хотел": u"Хотели",
    u"Семеен хотел": u"Хотели",
    u"хотел · без категоризация": u"Хотели",
    u"апарт-хотел": u"Хотели",
    u"училище": u"Училища",
    u"университет": u"Университети",
    u"болница": u"Болници",
    u"ДКЦ": u"ДКЦ",
    u"хоспис": u"Хосписи",
    u"детска градина": u"Детски градини",
    # LOT 1, amendment 8 P2: the two new kinds of the delivery get a heading each
    # — the nursery is NOT a kindergarten (Petar's words, 03.09).
    u"детска ясла": u"Детски ясли",
    u"общежитие": u"Общежития",
}
GEN_CAP = 300                                    # M3/B2: the generosity ceiling


def group_of(rec):
    return KIND_GROUP.get(rec.kind, rec.kind)


GROUP_SIZE = {}
for _r in RECS:
    GROUP_SIZE[group_of(_r)] = GROUP_SIZE.get(group_of(_r), 0) + 1


def gen_ok(rec):
    """M3/B2 as Sol repaired it (phase-2 plan sec.7 C3): without a key the
       generosity is decided by the size of the record's OWN class, not by the
       size of the whole index. With 226 hotels the old wording was harmless;
       with 361 records it would have switched the keyless branch off entirely."""
    return GROUP_SIZE.get(group_of(rec), 0) <= GEN_CAP


# --------------------------------------------------------------- M2 matching
# §11 Р9: the cap mode comes from an EXPLICIT list and only when we are run as a
# script — on import (the gate test) argv belongs to the test runner, so the
# module must keep the signed default and never read it.
CAPMODES = ("plan", "poi")
CAPMODE = "plan"                                           # "plan" | "poi"


def set_capmode(argv):
    """The cap mode is the first POSITIONAL word; `--freeze`/`--manifest` are not it.

    Read positionally, `recall_sweep.py --manifest` died with „CAPMODE must be
    one of plan, poi“ — a flag the script itself defines, refused by the script
    itself, is the kind of gate that teaches a human to stop reading errors."""
    global CAPMODE
    positional = [a for a in argv[1:] if not a.startswith("--")]
    mode = positional[0] if positional else "plan"
    if mode not in CAPMODES:
        raise SystemExit("recall_sweep: CAPMODE must be one of %s, got %r"
                         % (", ".join(CAPMODES), mode))
    CAPMODE = mode

# ---- candidate rule REPAIRS, measured as counterfactuals in sec. в4 ----------
# П1  fuzzy only from 6 original chars up (4-5 chars: exact/prefix + lev<=1)
# П2  A7: "покритие на името" (unmatched name tokens ^) just before distance
# П3  a purely numeric token must match EXACTLY or the record is rejected
# П4  a dictionary word whose class is EMPTY must match a name/alias, else 0 rows
# П5 SIGNED 02.09 too: without a key a 2-char word is significant only on an EXACT
# match against a record whose whole name is that single token ("йо" -> хотел Йо).
# П6 SIGNED 02.09 (sec.9 v1.4): without a key a 2-char token with an EXACT name
# match is significant when ANOTHER query token also matches that record exactly.
BASE = {"P1": False, "P2": True, "P3": True, "P4": True, "P5": True,
        "P6": True}                                          # signed 02.09
FIX = dict(BASE)


def set_fix(cfg):
    for _k in FIX:
        FIX[_k] = bool(cfg.get(_k, False))


def kind_gen(t, v):
    """plan sec.3 M2: 3 exact / 2 prefix / 1 lev<=cap ; 2-3 chars exact+prefix
       only ; 1 char nothing ; purely numeric -> exact only."""
    q = t.s
    if t.num:
        return 3 if v == q else 0
    L = len(t.orig)
    if L <= 1:
        return 0
    if v == q:
        return 3
    if v.startswith(q):
        return 2
    if L <= 3:
        return 0
    if FIX["P1"] and L <= 5:                       # П1
        return 1 if lev(q, v, 1) <= 1 else 0
    cap = 2 if CAPMODE == "plan" else (2 if len(q) >= 7 else 1)
    return 1 if lev(q, v, cap) <= cap else 0


def token_match(rec, t):
    """A4: ONE match per token, best by priority
       name-exact(3) > alias(3) > zone/kind-exact > name-prefix(2) > name-fuzzy(1).
       An exact zone/kind match EATS the token: no fuzzy name credit afterwards.
       Returns (category, quality) with category in {"name","alias","zk",None}."""
    if t.s in rec.nset:
        return ("name", 3)
    if (not t.num) and len(t.orig) > 2 and t.s in rec.aset:
        return ("alias", 3)
    if t.s in rec.zkset:
        return ("zk", 3)
    kn = 0
    for v in rec.ntk:
        k = kind_gen(t, v)
        if k > kn:
            kn = k
            if kn == 2:
                break
    if kn:
        return ("name", kn)
    return (None, 0)


def significant(t, cat, q, has_key, rec=None, R=None):
    """A5. Base (always): >=3 original chars, not an address marker, not a number.
       With a key the base is EXTENDED (not replaced): any non-numeric exact or
       prefix match counts ("хотел йо"), and a purely numeric token counts only
       with a key and only exact ("градина 12", "дкц 2")."""
    if cat not in ("name", "alias"):
        return False
    if t.orig in ADDR:
        return False
    if t.num:
        return has_key and q == 3
    if len(t.orig) >= 3:
        return True
    if has_key and q >= 2:
        return True
    if (FIX.get("P5") and not has_key and cat == "name" and q == 3
            and rec is not None and len(rec.ntk) == 1):
        return True                                  # П5 (signed)
    # П6 (signed §9 v1.4): a 2-char token that hits a NAME token EXACTLY is
    # significant when the query carries at least one MORE token that also matches
    # this very record exactly (the number is conjunctive anyway by П3).
    if (FIX.get("P6") and not has_key and cat == "name" and q == 3
            and len(t.orig) == 2 and rec is not None and R):
        for t2 in R:
            if t2 is t:
                continue
            c2, q2 = token_match(rec, t2)
            if q2 == 3 and c2 in ("name", "alias"):
                return True                              # П6 (signed)
    return False


def score(rec, R, has_key):
    """A4 + A5 -> (bestNameKind, nameMatched, totalMatched, sum, qualified, uncov)"""
    best_nk = 0
    nmatched = 0
    total = 0
    ssum = 0
    qual = False
    numfail = False
    for t in R:
        cat, q = token_match(rec, t)
        if cat is None:
            if t.num and FIX["P3"]:                # \u041f3: numbers are conjunctive
                numfail = True
            continue
        total += 1
        if cat == "zk":
            ssum += 3                      # M4 weight: zone/kind x1 (quality 3)
        else:
            nmatched += 1
            ssum += 2 * q                  # M4 weight: name x2
            if q > best_nk:
                best_nk = q
            if significant(t, cat, q, has_key, rec, R):
                qual = True
    if numfail:
        qual = False
    # \u041f2: how many of the record's OWN name tokens stayed untouched
    uncov = 0
    for v in set(rec.ntk):
        if not any(kind_gen(t, v) for t in R):
            uncov += 1
    return best_nk, nmatched, total, ssum, qual, uncov


def order_named(rows):
    """A7 (M4 refined); rows = (rec, bestNameKind, nameMatched, total, sum, uncov)"""
    rows.sort(key=lambda x: (-x[1], -x[2], -x[3], -x[4],
                             1 if x[0].status == u"\u0431\u0438\u0432\u0448" else 0,
                             x[5] if FIX["P2"] else 0,          # \u041f2
                             x[0].dist, len(x[0].name), x[0].name.lower()))
    return [x[0] for x in rows]


def order_category(recs):
    """plan sec.3 M1: nearest to the frame centre first (CENTER stand-in)."""
    return sorted(recs, key=lambda r: (r.dist, len(r.name), r.name.lower()))


def stable_unique(recs):
    """ЛОТ 1: dedupe by the RECORD OBJECT, keeping the first place; the already
    ordered lists are never re-sorted."""
    out, seen = [], set()
    for r in recs:
        if id(r) not in seen:
            seen.add(id(r))
            out.append(r)
    return out


def name_has_phrase(rec, R):
    """ЛОТ 1, decision 1: R as an EXACT ordered run of the CURRENT name tokens
    (no prefix, no fuzzy). An alias proves the sequence only when it is a single
    token — `aset` keeps tokens, not phrases, so a longer R through it would be
    a sum of different aliases, which the rule forbids."""
    seq = [t.s for t in R]
    for i in range(len(rec.ntk) - len(seq) + 1):
        if rec.ntk[i:i + len(seq)] == seq:
            return True
    return len(seq) == 1 and seq[0] in rec.aset


# --------------------------------------------------------------------- search
def split_keys(qt):
    """T2 + A1: longest form at each position, but ONLY forms whose class holds
       >=1 loaded record become keys. Returns (keys, slots, dead) where slots is
       the positional list of (token, key_index_or_None) and `dead` are the
       tokens of dictionary forms whose class is EMPTY (A1 -> plain names)."""
    keys = []
    slots = []
    dead = []
    i = 0
    while i < len(qt):
        hit = None
        for L in range(min(MAXFORM, len(qt) - i), 0, -1):
            fk = " ".join(t.s for t in qt[i:i + L])
            if fk in FORM_IDX and CLASS_OF[fk]:      # A1: populated only
                hit = (fk, L)
                break
        if hit:
            ki = len(keys)
            keys.append(hit[0])
            for j in range(hit[1]):
                slots.append((qt[i + j], ki))
            i += hit[1]
        else:
            for L in range(min(MAXFORM, len(qt) - i), 0, -1):
                fk = " ".join(t.s for t in qt[i:i + L])
                if fk in FORM_IDX:                   # exists but class is empty
                    dead.extend(qt[i:i + L])
                    break
            slots.append((qt[i], None))
            i += 1
    return keys, slots, dead


def run_scored(cls, R, has_key, dead=()):
    scored = []
    for r in cls:
        if FIX["P4"] and dead:                       # П4 (exact name/alias only:
            ok = True                                # a fuzzy coincidence such as
            for t in dead:                           # болница~БОНИТА is not proof
                cat, q = token_match(r, t)           # that the class word is there)
                if cat not in ("name", "alias") or q != 3:
                    ok = False
                    break
            if not ok:
                continue
        bnk, nm, tot, ssum, qual, unc = score(r, R, has_key)
        if qual:
            scored.append((r, bnk, nm, tot, ssum, unc))
    return order_named(scored)


# ============================== ЛОТ 1в-В (план §3ж S3) — the typed branches
DISTRICT_MARK = u"район"


def district_rows(R, cls):
    """The EXPLICIT „район X“ branch: None = the query did not ask for one.

    „район X“ is the one location phrase that searches the WHOLE district —
    every record in it, with a quarter or without. It is recognised by the word
    the human wrote („район“), never by the district name alone: bare „младост“
    is the quarter first (below), or the district would swallow it."""
    if not any(t.orig == DISTRICT_MARK for t in R):
        return None
    rest = [t for t in R if t.orig != DISTRICT_MARK]
    if not rest:
        return None
    phrase = u" ".join(t.s for t in rest)
    rows = [r for r in cls if phrase in r.dph]
    return order_category(rows) if rows else None


def location_rows(R, cls):
    """The BARE location phrase → (quarter rows, locality/legacy rows, district rows).

    None = the phrase is nobody's location. The district answers ONLY for
    records with no quarter of their own (план §3ж S3): with that restriction
    „училище младост“ is „the schools of the quarter Младост plus the schools
    of район Младост that have no quarter“ — the two Petar named are in it —
    and without it the same query is an unbounded district sweep that buries
    them. The old zone words of a row live in `gph`: they are INDEXED here and
    shown nowhere."""
    if not R:
        return None
    phrase = u" ".join(t.s for t in R)
    q_rows = [r for r in cls if phrase in r.qph]
    l_rows = [r for r in cls if phrase in r.lph or phrase in r.gph]
    d_rows = [r for r in cls if r.quarter is None and phrase in r.dph]
    if not (q_rows or l_rows or d_rows):
        return None
    return order_category(q_rows), order_category(l_rows), order_category(d_rows)


# The one switch of the engine, and it exists for ONE reader: the P7 → F12
# manifest has to show what М7 moved, and „what it moved“ can only be measured
# by running the same data with the branch off. The client has no such flag —
# it is never asked to measure itself — and nothing but `--manifest` flips it.
M7_ENABLED = True


def bare_location_rows(R, cls):
    """М7 (план §3й-б S4): a BARE location word, without a class key.

    Sol’s S4 overturned the literal М7: `location_rows` compares the WHOLE
    phrase, so „златни“ alone could never reach „к.к. Златни пясъци“, and the
    only token set the client kept (`zkset`) mixes quarter, locality, legacy and
    kind together — a branch built on it would answer a locality query with the
    rows of a KIND. So the trigger reads `qtk` and `ltk` and nothing else:

      * `legtk` (the OLD zone words of a row) never triggers and never enters
        (Кими К5-г): those words are a row’s history, not its address, and
        „зпз“ — which is both a locality alias and a legacy word — therefore
        fires ONLY as the locality it is today;
      * `ktk` (the kind) never triggers: „училище“ is the class list, not a place;
      * the district never triggers by name — bare „младост“ is the quarter
        first, exactly as `district_rows` says, and the district enters only
        through the rows that have no quarter of their own.

    Returns [] when the words are nobody’s quarter or locality.
    """
    if not R:
        return []
    tokens = [t.s for t in R]
    quarter_hit = [r for r in cls if all(t in r.qtk for t in tokens)]
    locality_hit = [r for r in cls if all(t in r.ltk for t in tokens)]
    if not (quarter_hit or locality_hit):
        return []
    phrase = u" ".join(tokens)
    # The exact-name head of ЛОТ 1 decision 1 keeps a record whose own NAME is
    # the phrase above the location rows it happens to share the word with.
    head = order_category([r for r in cls if name_has_phrase(r, R)])
    district_hit = [r for r in cls if r.quarter is None and phrase in r.dph]
    return stable_unique(head + order_category(quarter_hit)
                         + order_category(locality_hit) + order_category(district_hit))


def bare_location_query(R):
    """The shape of a query М7 may answer: a bare place, nothing else.

    A district marker („район X“) has its own branch, a street marker („ул. X“)
    is a street before it is a quarter, and a number is an address — none of
    the three is a bare location word.

    F12-е: and every word has to be SIGNIFICANT by the rule the rest of the
    machine already uses. The literal branch filtered numbers only, so the TYPE
    PREFIXES the location names carry („к.к.“, „кв.“, „ж.к.“, „м-т“, „с.о.“)
    reached `qtk`/`ltk` as tokens of their own and answered as places: measured
    04.09 on this delivery „к“ returned 163 rows and „кв“ 36. A prefix is not a
    place, and `significant_token` is where that is written down once."""
    if not M7_ENABLED or not R:
        return False
    if any(t.orig == DISTRICT_MARK for t in R):
        return False
    if any(t.orig in STREET_MARK for t in R):
        return False
    return all(significant_token(t) for t in R)


def has_key_of(q):
    """The `hasKey` the CLIENT returns for this query — 1:1 with index.html.

    A0 answers before A1 can spend a word on a class key, so an exact alias
    carries no key however many dictionary words it contains."""
    qt = place_tokens(q)
    if not qt or exact_alias(qt):
        return False
    return bool(split_keys(qt)[0])


def row_out(rec):
    """One reference row: the compat label AND the three typed fields (S1).

    The base artefact knows {name, zone} only, so the typed fields can only be
    NEW in the comparison — never „changed“. `src` and `code` travel with the
    name because the manifest has to say WHY a label is what it is."""
    def loc(field):
        if not field:
            return None
        return {"name": field.get("name"), "src": field.get("src"),
                "code": field.get("code")}
    return {"name": rec.name, "zone": rec.zone, "kind": rec.kind,
            "quarter": loc(rec.quarter), "district": loc(rec.district),
            "locality": loc(rec.locality)}


def search(q):
    """Returns (rows, branch). rows is the FULL list (the TOP-8 cut is in render)."""
    qt = place_tokens(q)
    if not qt:
        return [], "empty"
    # A0 (ADR 008 D2, амандамент А4 т. 2): a query that IS somebody's whole
    # alias answers with that record, before A1 can spend it on a class key.
    hit = exact_alias(qt)
    if hit:
        return order_category([r for r, _i in hit]), "A0-exact-alias"
    keys, slots, dead = split_keys(qt)
    if keys:
        # A1: the LEFTMOST key is the class; the other key words become names.
        cls = CLASS_OF[keys[0]]
        R = [t for (t, ki) in slots if ki is None or ki != 0]
        has_key = True
    else:
        cls = RECS
        R = [t for (t, ki) in slots]
        has_key = False
    if not R:
        # M1: key only. ЛОТ 1, decision 2 — a record whose CURRENT name is the
        # very same ordered token sequence as the whole query stands ABOVE the
        # category list; the category order itself is not recomputed.
        rows = order_category(cls)
        exact = EXACT_NAME.get(u" ".join(t.s for t in qt)) or []
        if exact:
            rows = stable_unique(order_category(exact) + rows)
        return rows, "M1-category"
    if not has_key and bare_location_query(R):
        # М7 (план §3й-б S4) stands BEFORE the M3/B2 generosity gate on purpose:
        # „златни пясъци“ is a place the human named in full, and the size of the
        # class it happens to fall in may not decide whether we answer it. It
        # keeps `hasKey` False, so the client still renders our section UNDER the
        # untouched building address search.
        bare = bare_location_rows(R, cls)
        if bare:
            return bare, "M7-bare-location"
    if not has_key:                                        # M3/B2 gate, PER CLASS
        cls = [r for r in cls if gen_ok(r)]
        if not cls:
            return [], "M3-too-big"
        # ЛОТ 1в-В (S3): „район X“ is explicit with or without a class word — the
        # marker is the word the HUMAN wrote, and it asks for the district of every
        # record. Nothing else of this lot fires without a key: a bare location
        # phrase stays what it was, so the frozen reference keeps its keyless rows.
        explicit_district = district_rows(R, cls)
        if explicit_district is not None:
            return explicit_district, "A3-district"
    # ---- A3: key + remainder that is PURELY zone/kind -> filtered category list
    if has_key:
        zk_all = set()
        nm_all = set()
        for r in cls:
            zk_all |= r.zkset
            nm_all |= r.nset
        # ЛОТ 1, decision 1: the class-wide name veto below is right about the
        # class and wrong about the record. When the remainder is the WHOLE
        # significant phrase of some record's location and only that veto stands
        # in the way, the choice is made PER RECORD: the exact name/alias
        # sequence first, then the rows of the location itself.
        vetoed = any(t.s in nm_all for t in R)
        # ЛОТ 1в-В (S3): „ул./бул./пл. X“ is a STREET before it is anything else
        # — „бул. Владислав Варненчик“ is a boulevard, and the quarter of the
        # same name must never take the query off it.
        if any(t.orig in STREET_MARK for t in R):
            marked = street_rows(R, cls)
            if marked:
                return marked, "A3-street"
        # ЛОТ 1в-В: the explicit district first, then the bare location phrase.
        explicit = district_rows(R, cls)
        if explicit is not None:
            return explicit, "A3-district"
        loc = location_rows(R, cls)
        if loc is not None:
            head = (order_category([r for r in cls if name_has_phrase(r, R)])
                    if vetoed else [])
            rows = stable_unique(head + loc[0] + loc[1] + loc[2])
            if rows:
                return rows, ("A3-record+zone-phrase" if head else "A3-location")
        # A3' (see report sec. г): A4's priority also governs the branch --
        # a token that matches a NAME exactly is a name token, not a filter.
        if R and all(t.s in zk_all for t in R) and not vetoed:
            flt = [r for r in cls if all(t.s in r.zkset for t in R)]
            if flt:
                return order_category(flt), "A3-category+zone/kind"
    # ADR 008 D6: exact name/alias -> zone (П7) -> STREET -> fuzzy/fail-open. With
    # a key the answer is the class on that street; without one it is the address
    # the human typed and `has_key` stays False, so the client renders our section
    # UNDER the untouched building address search (план §2г S4).
    street = street_rows(R, cls)
    if street:
        return street, "A3-street"
    rows = run_scored(cls, R, has_key, dead)
    if rows:
        return rows, ("M2" if has_key else "M3")
    if has_key:
        # A1 fail-open: retry with ALL keys as plain name tokens, whole delivery
        R2 = [t for (t, ki) in slots]
        rows = run_scored(RECS, R2, False, dead)
        if rows:
            return rows, "M2-failopen"
    return [], ("M2" if has_key else "M3")


def rows_label(rows, n=3):
    return u" · ".join(u"%s (%s)" % (r.name, r.zone) for r in rows[:n]) or u"—"


# ============================================================== SWEEP (a)
def name_words(rec_name):
    """post-norm words of the name, tagged as key / non-key (A1 definition)"""
    qt = place_tokens(rec_name)
    keys, slots, dead = split_keys(qt)
    return [(t.orig, ki is not None) for (t, ki) in slots]


LAT = re.compile(r"[A-Za-z]")


def latin_half(name):
    if "/" not in name:
        return None
    parts = [p.strip() for p in name.split("/")]
    parts = [p for p in parts if p]
    best, bn = None, 0
    for p in parts:
        c = len(LAT.findall(p))
        if c > bn:
            bn, best = c, p
    return best if bn else None


def rank_of(rows, rec):
    for i, r in enumerate(rows):
        if r is rec:
            return i
    return -1


CLS_ORDER = [u"A1 цялото име (малки букви)", u"A2 името без ключовите думи",
             u"A3 всяка значеща дума ≥4 знака", u"A4 латинската половина при „/“"]


def sweep_recall():
    classes = dict((k, []) for k in CLS_ORDER)
    fails = dict((k, []) for k in CLS_ORDER)
    notin8 = dict((k, []) for k in CLS_ORDER)
    for rec in RECS:
        ws = name_words(rec.name)
        q = rec.name.lower()
        rows, br = search(q)
        classes[CLS_ORDER[0]].append((rec, q, rank_of(rows, rec), len(rows), br))
        rest = [w for w, isk in ws if not isk]
        q2 = " ".join(rest)
        if q2:
            rows, br = search(q2)
            classes[CLS_ORDER[1]].append((rec, q2, rank_of(rows, rec), len(rows), br))
        for w, isk in ws:
            if isk or len(w) < 4:
                continue
            rows, br = search(w)
            classes[CLS_ORDER[2]].append((rec, w, rank_of(rows, rec), len(rows), br))
        lh = latin_half(rec.name)
        if lh:
            rows, br = search(lh)
            classes[CLS_ORDER[3]].append((rec, lh, rank_of(rows, rec), len(rows), br))
    for k, v in classes.items():
        for rec, q, rk, n, br in v:
            if rk < 0:
                fails[k].append((rec, q, n, br))
            elif rk >= TOP:
                notin8[k].append((rec, q, rk, n, br))
    return classes, fails, notin8


# ============================================================== SWEEP (b)
COLL = [u"парк", u"бриз", u"роял", u"402", u"блок с", u"бл 402", u"вх 3",
        u"чайка", u"виница", u"златни", u"хотел", u"хотели", u"семеен хотел",
        u"хотел златни", u"хотел адмирал", u"адмирал", u"хотел адмиралл",
        u"хотел амирал", u"адмирал златни", u"хотел адмирал златни пясъци",
        u"берлин голдън бийч", u"лти берлин", u"lti", u"royal", u"синчец",
        u"хотел синчец", u"русалка", u"бонита", u"bonita", u"хелиос спа",
        u"спа хелиос", u"парк хотел бриз", u"морска градина", u"аквапарк",
        u"комплекс", u"ьььь"]

def sweep_coll():
    out = []
    for q in COLL:
        rows, br = search(q)
        out.append((q, len(rows), br, rows[:3]))
    return out


# ============================================================== SWEEP (c) M5/A8
M5SPEC = []
EXTRASPEC = []


def chk(q, expect, ok_fn):
    M5SPEC.append((q, expect, ok_fn))


def evaluate(spec):
    out = []
    for q, expect, ok_fn in spec:
        rows, br = search(q)
        out.append((q, expect, len(rows), br, rows_label(rows, 3), ok_fn(rows)))
    return out


Z_ZL = u"к.к. Златни пясъци"
# F2-д: the zone was renamed in the delivery („к.к. Св. Константин“ ->
# „к.к. Св. Св. Константин и Елена“, all 40 records); the constant follows the data.
Z_SK = u"к.к. Св. Св. Константин и Елена"
Z_OD = u"район Одесос"
Z_VN = u"Виница/север"
Z_CH = u"к.к. Чайка"


def first_is(rows, name, zone=None):
    return bool(rows) and rows[0].name.strip() == name and (zone is None or rows[0].zone == zone)


def nz(r):
    return (r.name.strip(), r.zone)


chk(u"хотел адмирал", u"3 реда: АДМИРАЛ (Златни), Адмирал (Св. Константин), АМИРАЛ (Приморски)",
    lambda r: len(r) == 3 and sorted(x.name for x in r) == sorted([u"АДМИРАЛ", u"Адмирал", u"АМИРАЛ"]))
chk(u"адмирал", u"същите 3",
    lambda r: len(r) == 3 and sorted(x.name for x in r) == sorted([u"АДМИРАЛ", u"Адмирал", u"АМИРАЛ"]))
chk(u"хотел адмиралл", u"3", lambda r: len(r) == 3)
chk(u"хотел амирал", u"3", lambda r: len(r) == 3)
chk(u"адмирал златни", u"А8: точно 3, АДМИРАЛ (Златни) първи",
    lambda r: len(r) == 3 and nz(r[0]) == (u"АДМИРАЛ", Z_ZL))
chk(u"хотел адмирал златни пясъци", u"А8: точно 3, АДМИРАЛ (Златни) първи",
    lambda r: len(r) == 3 and nz(r[0]) == (u"АДМИРАЛ", Z_ZL))
chk(u"хотели", u"А8: 225", lambda r: len(r) == 225)
chk(u"хотел", u"категорийният списък (225)", lambda r: len(r) == 225)
chk(u"хотелите", u"А8: 225", lambda r: len(r) == 225)
chk(u"семеен хотел", u"само семейните (50)",
    lambda r: len(r) == 50 and all(x.kind == u"Семеен хотел" for x in r))
chk(u"хотел златни", u"А8: 96", lambda r: len(r) == 96 and all(x.zone == Z_ZL for x in r))
# фаза 2: същата заявка, по-голям индекс — размитата опашка по `бийч`/`голдън`
# хваща и места; първият ред (върху който е гейтът) е непокътнат.
chk(u"берлин голдън бийч", u"А8 (фаза 2): първият ред БЕРЛИН ГОЛДЪН БИЙЧ (20 реда общо)",
    lambda r: len(r) == 20 and first_is(r, u"БЕРЛИН ГОЛДЪН БИЙЧ"))
chk(u"лти берлин", u"А8: БЕРЛИН ГОЛДЪН БИЙЧ първи",
    lambda r: first_is(r, u"БЕРЛИН ГОЛДЪН БИЙЧ"))
chk(u"lti", u"А8: БЕРЛИН ГОЛДЪН БИЙЧ първи",
    lambda r: first_is(r, u"БЕРЛИН ГОЛДЪН БИЙЧ"))
chk(u"роял", u"А8: РОЯЛ (Одесос), РОЯЛ (Златни), после Royal Beach; размита опашка ОК",
    lambda r: len(r) >= 3 and nz(r[0]) == (u"РОЯЛ", Z_OD) and nz(r[1]) == (u"РОЯЛ", Z_ZL)
              and nz(r[2]) == (u"Royal Beach", Z_CH))
chk(u"royal", u"А8: същите 3 в същия ред; размита опашка ОК",
    lambda r: len(r) >= 3 and nz(r[0]) == (u"РОЯЛ", Z_OD) and nz(r[1]) == (u"РОЯЛ", Z_ZL)
              and nz(r[2]) == (u"Royal Beach", Z_CH))
# фаза 2: има място, НАИМЕНУВАНО „Синчец“ (ДГ 30). По А4 точното име и
# псевдонимът са равностойни (k3), така че решава разстоянието до центъра:
# ДГ 30 (Младост) е по-близо от ДАНА ПАЛАС (Златни). С ключ — хотелът.
chk(u"синчец", u"фаза 2: ДГ 30 „Синчец“ (името), после ДАНА ПАЛАС (старото име)",
    lambda r: len(r) == 2 and r[0].name == u'ДГ 30 "Синчец"' and r[1].name == u"ДАНА ПАЛАС")
chk(u"хотел синчец", u"ДАНА ПАЛАС", lambda r: first_is(r, u"ДАНА ПАЛАС"))
# фаза 2 + §8: зоната на РУСАЛКА е вече кварталът (Виница/север →
# к.к. Чайка), а МЕЖДУ двата хотела влиза ДЯ №13 „Русалка“ (по-близо).
chk(u"русалка", u"фаза 2: РУСАЛКА (к.к. Чайка), ДЯ „Русалка“, Русалка (Св. К.) „бивш“",
    lambda r: len(r) >= 3 and nz(r[0]) == (u"РУСАЛКА", Z_CH)
              and r[1].kind == u"детска ясла"
              and nz(r[2]) == (u"Русалка", Z_SK) and r[2].status == u"бивш")
chk(u"бонита", u"БОНИТА/BONITA", lambda r: first_is(r, u"БОНИТА/BONITA"))
chk(u"bonita", u"БОНИТА/BONITA", lambda r: first_is(r, u"БОНИТА/BONITA"))
chk(u"хелиос спа", u"ХОТЕЛ  ХЕЛИОС СПА", lambda r: first_is(r, u"ХОТЕЛ  ХЕЛИОС СПА"))
chk(u"спа хелиос", u"ХОТЕЛ  ХЕЛИОС СПА", lambda r: first_is(r, u"ХОТЕЛ  ХЕЛИОС СПА"))
# фаза 2: точните 12 са същите (всичките са хотели); размитата опашка
# расте от 7 на 10 с местата (Левенщайн 2 от `park`). Разделянето 12/10 е гейтът.
chk(u"парк", u"А8 (фаза 2): 22 реда — първите 12 с точно „ПАРК“, после 10 размити",
    lambda r: (len(r) == 22
               and all(u"park" in x.nset for x in r[:12])
               and not any(u"park" in x.nset for x in r[12:])))
# фаза 2: класът „детска градина“ вече е НАСЕЛЕН, затова по А1 формата
# „градина“ е КЛЮЧ (точно както „болница“ и „дкц“) → категориен списък.
# ЛОТ 1 решение 2 (подписано 03.09): хотел ГРАДИНА носи ТОЧНО това име, така че
# застава НАД списъка; детските градини остават в същия ред след него. F2-д: 51
# градини на доставката (яслите са СВОЙ клас и не влизат тук — §Д5 на превюто).
chk(u"градина", u"ЛОТ 1 решение 2: хотел ГРАДИНА + категорийният списък (1+51)",
    lambda r: (len(r) == 52 and r[0].name == u"ГРАДИНА"
               and all(x.kind == u"детска градина" for x in r[1:])))
chk(u"блок с", u"0 наши реда", lambda r: len(r) == 0)
chk(u"402", u"0 наши реда", lambda r: len(r) == 0)
chk(u"бл. 402", u"0 наши реда", lambda r: len(r) == 0)
chk(u"вх 3", u"0 наши реда", lambda r: len(r) == 0)
chk(u"ьььь", u"0 наши реда", lambda r: len(r) == 0)
# ФАЗА 2 · гейтът на интуитивните заявки (places_phase2_plan.md §3).
# Дотук тези заявки чакаха 0 реда, ЗАЩОТО класовете ги нямаше в доставката.
# Сега ги има — очакванията са ДОСЛОВНО тези от §3 на плана за фаза 2:
# както е записано там, „падне ли — правилото“, така че паднал ред тук
# е искане за подписано правило, не за тихо преписване на очакването.
UMBAL = u"„Университетска многопрофилна болница за активно лечение „Света Марина““ ЕАД"
VII_SU = u"VII СУ „Найден Геров“"
II_OU = u"II ОУ „Никола Йонков Вапцаров“"
II_DKC = u"II ДКЦ Св. Иван Рилски"
VVMU = u"ВВМУ „Н. Й. Вапцаров“"

# §3 ред 1 — категорийните списъци на шестте класа
def _cat(kind, n):
    return lambda r: len(r) == n and all(x.kind == kind for x in r)


for _q, _k, _n in [(u"училище", u"училище", 57),
                   (u"училища", u"училище", 57),
                   (u"университет", u"университет", 7),
                   (u"болница", u"болница", 11),
                   (u"детска градина", u"детска градина", 51),
                   (u"дкц", u"ДКЦ", 7),
                   (u"хоспис", u"хоспис", 6)]:
    chk(_q, u"§3: категориен списък на класа (%d)" % _n, _cat(_k, _n))

# §3 ред 2 — VII СУ „Найден Геров“ първи
for _q in [u"7 су", u"седмо су", u"vii су", u"7-мо су"]:
    chk(_q, u"§3: VII СУ „Найден Геров“ първи", lambda r: first_is(r, VII_SU))

# §3 ред 3 — Вапцаров. §9 v1.4: очакването е поправено като ФАКТ на
# данните: две институции носят това име (училището и ВВМУ) и двете съвпадат
# точно; редът между тях е по П2 (покритие на името). Гейтът: двата реда
# са първите два. С класовия ключ („2 оу вапцаров“) училището е първо.
chk(u"2 оу вапцаров", u"§3: II ОУ „Никола Йонков Вапцаров“ първи",
    lambda r: first_is(r, II_OU))
chk(u"вапцаров", u"§3 (§9 v1.4): двете „Вапцаров“ в първите два (редът — по П2)",
    lambda r: len(r) >= 2 and set([r[0].name, r[1].name]) == set([II_OU, VVMU]))

# §3 ред 4 — I ЕГ първи
for _q in [u"1 ег", u"i ег"]:
    chk(_q, u"§3: I ЕГ първи", lambda r: first_is(r, u"I ЕГ"))

# §3 ред 5 — II ДКЦ Св. Иван Рилски
for _q in [u"дкц 2", u"2 дкц", u"дкц св иван рилски"]:
    chk(_q, u"§3: II ДКЦ Св. Иван Рилски първи", lambda r: first_is(r, II_DKC))

# §3 ред 6 — УМБАЛ „Св. Марина“ по извора (регистровото име на ИАМН)
for _q in [u"болница света марина", u"св марина", u"умбал"]:
    chk(_q, u"§3: УМБАЛ „Св. Марина“ първи (регистровото име)", lambda r: first_is(r, UMBAL))

# §3 ред 7 — „ДГ №12 (по извора)“: дотук очакването беше честните 0 реда, защото
# ДГ №12 я нямаше в доставката. ЛОТ 1 я донесе от регистъра — очакването става
# редът, който §3 на плана за фаза 2 искаше от самото начало (§Б20–Б22).
for _q in [u"градина 12", u"дг 12", u"детска градина 12"]:
    chk(_q, u"§3 „по извора“: 1 — ДГ№12 „Ян Бибиян“",
        lambda r: len(r) == 1 and first_is(r, u"ДГ№12 „Ян Бибиян“"))

# §3 ред 8 — университетите
# §9 v1.4: „ту варна“ ОТПАДА от гейта — псевдонимът „ТУ“ стои в `rejected` на
# одобрения речник varna_3d/data/place_aliases.json (правилото на Петър от 21.08:
# само официални съкращения); решението за него е в 3D-то, не тук. „технически
# университет“ намира ТУ-Варна и остава в гейта.
for _q, _name in [(u"икономически университет", u"Икономически университет - Варна"),
                  (u"технически университет", u"Технически университет – Варна"),
                  (u"медицински университет", u"Медицински университет „Проф. д-р Параскев Стоянов“"),
                  (u"ввму", u"ВВМУ „Н. Й. Вапцаров“"),
                  (u"вму", u"ВВМУ „Н. Й. Вапцаров“"),
                  (u"всу", u"Варненски Свободен Университет „Черноризец Храбър“")]:
    chk(_q, u"§3: %s първи" % _name,
        (lambda name: (lambda r: first_is(r, name)))(_name))

# §3 ред 10 — адресните заявки от G3-корпуса: 0 наши реда
for _q in [u"бл. 402 вх. 3", u"макгахан 15"]:
    chk(_q, u"§3: 0 наши реда (адресните отгоре, байт-равни)", lambda r: len(r) == 0)

# ------------------------------------------- extra probes asked for tonight
def chk2(q, expect, ok_fn):
    EXTRASPEC.append((q, expect, ok_fn))


chk2(u"хотел йо", u"Йо", lambda r: first_is(r, u"Йо"))
chk2(u"хотел градина", u"ГРАДИНА", lambda r: first_is(r, u"ГРАДИНА"))
chk2(u"хотел семеен", u"50", lambda r: len(r) == 50 and all(x.kind == u"Семеен хотел" for x in r))
chk2(u"хотел адмирал", u"3, най-близкият (от точните) първи",
     lambda r: len(r) == 3 and nz(r[0]) == (u"Адмирал", Z_SK))
chk2(u"аквапарк клуб", u"ПРЕСТИЖ ДЕЛУКС АКВАПАРК КЛУБ",
     lambda r: first_is(r, u"ПРЕСТИЖ ДЕЛУКС АКВАПАРК КЛУБ"))
chk2(u"ritsa", u"Апарт комплекс Ritsa / „Рица“",
     lambda r: first_is(r, u"Апарт комплекс Ritsa / „Рица“"))
chk2(u"арабела блок с", u"АРАБЕЛА", lambda r: first_is(r, u"АРАБЕЛА"))
chk2(u"арабела", u"АРАБЕЛА", lambda r: first_is(r, u"АРАБЕЛА"))
chk2(u"мак", u"ПРЕСТИЖ ДЕЛУКС АКВАПАРК КЛУБ (псевдоним „Мак“)",
     lambda r: first_is(r, u"ПРЕСТИЖ ДЕЛУКС АКВАПАРК КЛУБ"))
chk2(u"йо", u"Йо (голата 2-знакова заявка — по П5)", lambda r: first_is(r, u"Йо"))

# G12b unit tests of placeTokens
# ------------------------------------------- П7 · the C16 gate (§11 С2′–С4′, Р3)
# С4′: a count is not an expectation — „владиславово училище“ was 4 by fail-open
# before П7 too. Every row below is {name, zone, kind} AND the branch, measured
# on 03.09 with П7 off and on; for the GAINS `M2-failopen` is red by
# construction. Each tuple is (query, branch, total rows, why, rows checked from
# the top — the whole list when it is short enough to write out).

# §11 v2.1 — the окончателен measured result of the rule. Р5: a zone that enters
# the delivery WITHOUT a registry entry legitimately changes this, and red here
# is then a signed decision to take, not a defect to paper over.
P7_EXPECTED = {
    u"Западна промишлена зона": [u"zpz"],
    u"ж.к. Владислав Варненчик": [u"vladislavovo"],
    # Амандамент №10 (3): the SEVENTH token, and it came from the data, not from
    # the rule. Решение „к.к. Св. Константин“ -> „к.к. Св. Св. Константин и Елена“
    # made the zone match its registry family, and the registry spells the family
    # „Кк Св. Констанин и Елена“ — a typo IN THE SOURCE, kept because it is what a
    # human types. Р5: a zone that enters the delivery legitimately changes this.
    u"к.к. Св. Св. Константин и Елена": [u"konstanin"],
    u"кв. Владиславово": [u"varnenchik", u"vladislav"],
    u"кв. Изгрев": [u"zhkizgrev"],
    u"м-т Горчивата чешма": [u"gorchiva"],
}

P7_GAINS = [
    # F2-д (§Б27/§Б28 + §Г на подписаното превю): ЛОТ 1 положи 3 градини повече в
    # двете изписвания на квартала, така че двете заявки връщат 5 вместо 2. Целият
    # списък е гейт — редът е част от подписа, не само броят.
    (u'владиславово детска градина', u'A3-category+zone/kind', 5, u'§11 Р3: 5-те градини от 2-те изписвания', [
        (u'ДГ 39 "Приказка"', u'ж.к. Владислав Варненчик', u'детска градина'),
        (u'ДГ№40 „Детски свят“', u'кв. Владиславово', u'детска градина'),
        (u'ОДЗ Маргаритка', u'кв. Владиславово', u'детска градина'),
        (u'ДГ№41 „Първи юни“', u'ж.к. Владислав Варненчик', u'детска градина'),
        (u'ДГ№37 „Пламъче“', u'ж.к. Владислав Варненчик', u'детска градина'),
    ]),
    (u'детска градина владислав варненчик', u'A3-category+zone/kind', 5, u'§11 Р3: същите 5', [
        (u'ДГ 39 "Приказка"', u'ж.к. Владислав Варненчик', u'детска градина'),
        (u'ДГ№40 „Детски свят“', u'кв. Владиславово', u'детска градина'),
        (u'ОДЗ Маргаритка', u'кв. Владиславово', u'детска градина'),
        (u'ДГ№41 „Първи юни“', u'ж.к. Владислав Варненчик', u'детска градина'),
        (u'ДГ№37 „Пламъче“', u'ж.к. Владислав Варненчик', u'детска градина'),
    ]),
    (u'владиславово училище', u'A3-category+zone/kind', 4, u'§11 Р3: 4-те училища поименно (не по fail-open)', [
        (u'ОУ Стоян Михайловски', u'ж.к. Владислав Варненчик', u'училище'),
        (u'ОУ Патриарх Евтимий', u'ж.к. Владислав Варненчик', u'училище'),
        (u'СУ „Пейо Крачолов Яворов“', u'ж.к. Владислав Варненчик', u'училище'),
        (u'І ОУ „Свети княз Борис I“', u'ж.к. Владислав Варненчик', u'училище'),
    ]),
    (u'хотел владиславово', u'A3-category+zone/kind', 2, u'§11 Р3: Комитово/Станкино ханче', [
        (u'Хотел-ресторант „Комитово ханче“', u'ж.к. Владислав Варненчик', u'хотел · без категоризация'),
        (u'Станкино ханче', u'ж.к. Владислав Варненчик', u'Семеен хотел'),
    ]),
    (u'дкц владиславово', u'A3-category+zone/kind', 1, u'§11 Р3: ДКЦ 3 – Варна', [
        (u'„ДКЦ 3 – Варна“ ЕООД', u'ж.к. Владислав Варненчик', u'ДКЦ'),
    ]),
    (u'хотел зпз', u'A3-category+zone/kind', 1, u'§11 С2′: хотелите в Западна промишлена зона', [
        (u'АДАМО', u'Западна промишлена зона', u'Хотел'),
    ]),
    (u'горчива чешма хотел', u'A3-category+zone/kind', 1, u'§11 С2′: хотелът в м-т Горчивата чешма', [
        (u'Алекта', u'м-т Горчивата чешма', u'Семеен хотел'),
    ]),
    (u'училище жкизгрев', u'A3-category+zone/kind', 4, u'§11 С2′: училищата в кв. Изгрев', [
        (u'ОУ "Стефан Караджа"', u'кв. Изгрев', u'училище'),
        (u'I ЕГ', u'кв. Изгрев', u'училище'),
        (u'3 ОУ Ангел Кънчев', u'кв. Изгрев', u'училище'),
        (u'ОУ Черноризец Храбър', u'кв. Изгрев', u'училище'),
    ]),
    # Амандамент №10 (3): the query for the seventh token. Measured 04.09 on the
    # ЛОТ 1 delivery: the misspelling „констанин“ used to be 25 rows of fail-open by
    # name; with the alias it is the category+zone list of the resort itself.
    (u'хотел констанин', u'A3-category+zone/kind', 37,
     u'§11 С2′: хотелите в к.к. Св. Св. Константин и Елена по регистровото изписване', [
        (u'Калифорния', u'к.к. Св. Св. Константин и Елена', u'Семеен хотел'),
        (u'Амфора', u'к.к. Св. Св. Константин и Елена', u'Семеен хотел'),
        (u'Адия Блу', u'к.к. Св. Св. Константин и Елена', u'Семеен хотел'),
    ]),
]

P7_CONTROLS = [
    (u'хотел приморският', u'M2', 1, u'§11 Р1: 1 ред, ПРИМОРСКИ по име — (д′) държи', [
        (u'ПРИМОРСКИ', u'к.к. Св. Св. Константин и Елена', u'Хотел'),
    ]),
    (u'приморският хотел', u'M2', 1, u'§11 Р1: същият ред', [
        (u'ПРИМОРСКИ', u'к.к. Св. Св. Константин и Елена', u'Хотел'),
    ]),
    (u'приморският хотел варна', u'M2', 11, u'§11 Р1: първият ред непроменен', [
        (u'Варна', u'район Одесос', u'Семеен хотел'),
        (u'Marina Varna Apartments', u'кв. Аспарухово', u'апарт-хотел'),
        (u'ГОЛДЪН ТЮЛИП ВАРНА', u'район Одесос', u'Хотел'),
    ]),
    (u'хотел приморски', u"A3-record+zone-phrase", 5,
     u'ЛОТ 1 решение 1 (беше M2/1): ПРИМОРСКИ по име + 4-те в район Приморски', [
        (u'ПРИМОРСКИ', u'к.к. Св. Св. Константин и Елена', u'Хотел'),
        (u'Маргарита', u'район Приморски', u'Семеен хотел'),
        (u'Вемара сити', u'район Приморски', u'Семеен хотел'),
        (u'Траката', u'район Приморски', u'Семеен хотел'),
        (u'Еллинис', u'район Приморски', u'Семеен хотел'),
    ]),
    (u'хотел бриз', u'M2', 6, u'§11 Р3: 6 реда, ПАРК ХОТЕЛ БРИЗ първи, Камелия липсва', [
        (u'ПАРК ХОТЕЛ БРИЗ', u'к.к. Златни пясъци', u'Хотел'),
        (u'Казабланка Грийн', u'кв. Свети Никола', u'Семеен хотел'),
        (u'Морски бряг', u'к.к. Чайка', u'Семеен хотел'),
        (u'ГРИЙН ПАРК', u'к.к. Златни пясъци', u'Хотел'),
        (u'ПАРАДАЙЗ ГРИЙН ПАРК', u'к.к. Златни пясъци', u'Хотел'),
        (u'БЕРЛИН ГРИЙН ПАРК', u'к.к. Златни пясъци', u'Хотел'),
    ]),
    (u'хотел свети никола', u'A3-category+zone/kind', 2, u'§11 Р3: 2 хотела от 2 изписвания (вярно и без П7)', [
        (u'Камелия', u'м. Св. Никола', u'Семеен хотел'),
        (u'Казабланка Грийн', u'кв. Свети Никола', u'Семеен хотел'),
    ]),
    (u'училище свети никола', u"A3-record+zone-phrase", 1,
     u'ЛОТ 1 решение 1 (беше M2/8): пълната зонова фраза — Менделеев в м-т Свети Никола', [
        (u'Професионална гимназия по химични и хранително-вкусови технологии "Д. И. Менделеев"', u'м-т Свети Никола', u'училище'),
    ]),
    (u'менделеев', u'M3', 1, u'§11 Р3: ПГ „Менделеев“ (1)', [
        (u'Професионална гимназия по химични и хранително-вкусови технологии "Д. И. Менделеев"', u'м-т Свети Никола', u'училище'),
    ]),
    (u'хотел зеленика', u"A3-record+zone-phrase", 2,
     u'ЛОТ 1 решение 1 (беше M2/1): Зеленика по име (дедуплиран) + Джоя от зоната', [
        (u'Зеленика', u'с.о. Зеленика', u'Семеен хотел'),
        (u'Джоя', u'м. Зеленика', u'Семеен хотел'),
    ]),
    (u'хотел варненчик', u'A3-category+zone/kind', 2, u'§11 Р4: Комитово/Станкино; КАРНИВАЛ не е в А3′ и днес', [
        (u'Хотел-ресторант „Комитово ханче“', u'ж.к. Владислав Варненчик', u'хотел · без категоризация'),
        (u'Станкино ханче', u'ж.к. Владислав Варненчик', u'Семеен хотел'),
    ]),
    (u'хотел марина парк', u'M2', 27, u'§11 Сол (4): МАРИНА първи', [
        (u'МАРИНА', u'к.к. Св. Св. Константин и Елена', u'Хотел'),
        (u'Санта Марина', u'Морска градина', u'Семеен хотел'),
        (u'Marina Varna Apartments', u'кв. Аспарухово', u'апарт-хотел'),
    ]),
    (u'училище менделеев стефан', u'M2', 3, u'§11: ОУ „Стефан Караджа“ първи', [
        (u'ОУ "Стефан Караджа"', u'кв. Изгрев', u'училище'),
        (u'Професионална гимназия по химични и хранително-вкусови технологии "Д. И. Менделеев"', u'м-т Свети Никола', u'училище'),
        (u'ОУ Стоян Михайловски', u'ж.к. Владислав Варненчик', u'училище'),
    ]),
    # F2-д (§Б30): 12-те хотела, презонирани от „к.к. Чайка“ в „к.к. Златни пясъци“
    # (П7 на подписа), напускат този отговор — 38 → 26. Първите три не мърдат.
    (u'хотел чайка', u'A3-category+zone/kind', 26, u'§11 §5: 26 (12-те презонирани излизат)', [
        (u'АМИРАЛ', u'кв. Чайка', u'Хотел'),
        (u'Trigor City / Guest Apartments', u'к.к. Чайка', u'апарт-хотел'),
        (u'РУСАЛКА', u'к.к. Чайка', u'Хотел'),
    ]),
    (u'училище изгрев', u'A3-category+zone/kind', 5, u'§11 §5: непроменен', [
        (u'ОУ "Стефан Караджа"', u'кв. Изгрев', u'училище'),
        (u'I ЕГ', u'кв. Изгрев', u'училище'),
        (u'3 ОУ Ангел Кънчев', u'кв. Изгрев', u'училище'),
        (u'ОУ Черноризец Храбър', u'кв. Изгрев', u'училище'),
        (u'ЧСУ „Монтесори Варна“', u'Изгрев 1', u'училище'),
    ]),
    # F2-д (§Б31): „Медицински комплекс „Майчин дом“ – Варна“ не е болница в
    # регистъра на ИАМН и излиза от класа с доставката — 3 → 2.
    (u'болница изгрев', u'A3-category+zone/kind', 2, u'§11 §5: 2 (Майчин дом излиза от класа)', [
        (u'„Многопрофилна болница за активно лечение Света Анна – Варна“ АД', u'кв. Изгрев', u'болница'),
        (u'Военно-морска болница', u'кв. Изгрев', u'болница'),
    ]),
    (u'училище аспарухово', u'A3-category+zone/kind', 5, u'§11 §5: 4 + СУУНЗ Шишманов, непроменен', [
        (u'Морска гимназия "Св. Николай Чудотворец"', u'кв. Аспарухово', u'училище'),
        (u'ОУ Христо Ботев', u'кв. Аспарухово', u'училище'),
        (u'СУ „Любен Каравелов“', u'кв. Аспарухово', u'училище'),
        (u'НУ Васил Левски', u'кв. Аспарухово', u'училище'),
        (u'СУУНЗ Проф. д-р Иван Шишманов', u'Аспарухово/Галата', u'училище'),
    ]),
    (u'2 оу', u'M3', 1, u'§9: II ОУ „Вапцаров“', [
        (u'II ОУ „Никола Йонков Вапцаров“', u'ж.к. Възраждане', u'училище'),
    ]),
    (u'1 ег', u'M3', 1, u'§9: I ЕГ', [
        (u'I ЕГ', u'кв. Изгрев', u'училище'),
    ]),
    (u'7 су', u'M3', 1, u'§9: VII СУ „Найден Геров“', [
        (u'VII СУ „Найден Геров“', u'кв. Чайка', u'училище'),
    ]),
    (u'др шишманов', u'M3', 1, u'§11 Р10: голото „др“ → доктор (примитивният тест)', [
        (u'СУУНЗ Проф. д-р Иван Шишманов', u'Аспарухово/Галата', u'училище'),
    ]),
    # Амандамент №2 (ж) + П3 на подписа: този ред БЕШЕ диференциалът на К2 (§12, д)
    # — 12 реда на M2-failopen с предпазителя, 4 на A3 без него. ЛОТ 1 донесе
    # законна данна (ДГ№19 „Славейче“ е първата градина със зона „район Приморски“),
    # която го обезсилва: сега заявката е обикновен A3 списък с 1 ред и вече не
    # различава предпазителя. Остава като обикновен ред с новата си стойност;
    # диференциалът се носи от В1/В2 в LOT1_CONTROLS (§В на подписаното превю).
    (u'детска градина приморски', u'A3-category+zone/kind', 1, u'Амандамент №2 (ж): вече не е диференциал — 1 ред по зоната', [
        (u'ДГ№19 „Славейче“', u'район Приморски', u'детска градина'),
    ]),
    (u'детска градина аспарухово', u'A3-category+zone/kind', 2, u'§11 С3′ диференциал: 2 (без предпазителя: 4)', [
        (u'ДГ№44 „Валентина Терешкова"', u'кв. Аспарухово', u'детска градина'),
        (u'ДГ №45 Морски свят', u'кв. Аспарухово', u'детска градина'),
    ]),
    (u'училище приморски', u'A3-category+zone/kind', 2, u'§11 С3′ диференциал: 2 (без предпазителя: 8)', [
        (u'ЧОУ "Феникс 2020"', u'район Приморски', u'училище'),
        (u'ПГ по Компютърно Моделиране и Компютърни Системи "Акад. Благовест Сендов"', u'район Приморски', u'училище'),
    ]),
]


# ------------------------------------------------------------------ ЛОТ 1 gate
# The two client rules of ЛОТ 1, as {name, zone, kind} + branch — never a row
# count alone. Decision 2 is the exact CURRENT name above the category list;
# decision 1 is the per-record zone phrase when the class-wide name veto blocks
# an otherwise valid full zone phrase. The four rows of the 103 that these two
# rules move are gated where they live (gate_m5_a8 „градина“ and the three П7
# controls); everything below is new.
LOT1_GAINS = [
    (u'хотел одесос', u"A3-record+zone-phrase", 23,
     u'решение 1: ПАРК ХОТЕЛ ОДЕСОС по име + 22-та в район Одесос', [
        (u'ПАРК ХОТЕЛ ОДЕСОС', u'к.к. Златни пясъци', u'Хотел'),
        (u'Каприз', u'район Одесос', u'Семеен хотел'),
    ]),
    (u'хотел морска градина', u"A3-record+zone-phrase", 18,
     u'решение 1: двутокенова пълна зона — 18-те в Морска градина', [
        (u'Орбита', u'Морска градина', u'Хотел'),
    ]),
    (u'училище морска градина', u"A3-record+zone-phrase", 6,
     u'решение 1: същата фраза в класа „училище“ — 6 реда', [
        (u'8 СОУПЧЕ', u'Морска градина', u'училище'),
    ]),
    # F2-д (§Б33/§Б34): хотел ГРАДИНА е презониран в „к.к. Златни пясъци“ (П7), а
    # списъкът под него е вече 51 градини — яслите имат СВОЙ клас и излизат оттук.
    (u'ГРАДИНА', u"M1-category", 52,
     u'решение 2: хотел ГРАДИНА над 51-те детски градини (главни букви)', [
        (u'ГРАДИНА', u'к.к. Златни пясъци', u'Хотел'),
        (u'ДГ№12 „Ян Бибиян“', u'м-т Шашкъна', u'детска градина'),
    ]),
    (u'градина', u"M1-category", 52,
     u'решение 2: същото с малки букви', [
        (u'ГРАДИНА', u'к.к. Златни пясъци', u'Хотел'),
        (u'ДГ№12 „Ян Бибиян“', u'м-т Шашкъна', u'детска градина'),
    ]),
    # Амандамент №8 П2 (подписът на Петър, 03.09) — трите нови думи на доставката
    # и Владиславово. Стойностите са МЕРЕНИ върху d9c6c06, не преписани.
    (u'детско заведение', u"M1-category", 61,
     u'П2: една форма, два вида — 51 градини + 10 ясли в един отговор', [
        (u'ДГ№12 „Ян Бибиян“', u'м-т Шашкъна', u'детска градина'),
        (u'ДЯ №4 „Приказен свят“', u'кв. Изгрев', u'детска ясла'),
    ]),
    (u'детски заведения', u"M1-category", 61,
     u'П2: същото в множествено число — същият набор, същата подредба', [
        (u'ДГ№12 „Ян Бибиян“', u'м-т Шашкъна', u'детска градина'),
        (u'ДЯ №4 „Приказен свят“', u'кв. Изгрев', u'детска ясла'),
    ]),
    (u'ясла', u"M1-category", 10,
     u'нов вид „детска ясла“: главата на чипа е ключ сама по себе си', [
        (u'ДЯ №4 „Приказен свят“', u'кв. Изгрев', u'детска ясла'),
    ]),
    (u'детска ясла', u"M1-category", 10,
     u'нов вид „детска ясла“: пълната форма; яслите НЕ са в „детска градина“', [
        (u'ДЯ №4 „Приказен свят“', u'кв. Изгрев', u'детска ясла'),
    ]),
    (u'общежитие', u"M1-category", 1,
     u'нов вид „общежитие“: единственият ред на доставката', [
        (u'ЦПЛР – Средношколско общежитие „Михаил Колони“', u'м-т Шашкъна', u'общежитие'),
    ]),
    (u'детска градина владиславово', u"A3-category+zone/kind", 5,
     u'Владиславово: 4 положени по регистър + ОДЗ Маргаритка (ДГ№42 е на борда)', [
        (u'ДГ 39 "Приказка"', u'ж.к. Владислав Варненчик', u'детска градина'),
        (u'ДГ№40 „Детски свят“', u'кв. Владиславово', u'детска градина'),
    ]),
]

LOT1_CONTROLS = [
    (u'хотел одес', u'M2', 2, u'решение 1: частична фраза — няма override', [
        (u'ПАРК ХОТЕЛ ОДЕСОС', u'к.к. Златни пясъци', u'Хотел'),
        (u'Модус', u'Морска градина', u'Хотел'),
    ]),
    (u'хотел градина', u'M2', 1, u'решение 1: „градина“ не е пълната зона „морска градина“', [
        (u'ГРАДИНА', u'к.к. Златни пясъци', u'Хотел'),
    ]),
    (u'хотел владиславово', u'A3-category+zone/kind', 2,
     u'решение 1: приетата П7 форма минава по стария клон — непроменено', [
        (u'Хотел-ресторант „Комитово ханче“', u'ж.к. Владислав Варненчик', u'хотел · без категоризация'),
        (u'Станкино ханче', u'ж.к. Владислав Варненчик', u'Семеен хотел'),
    ]),
    # F2-д (§Б5): клонът е непокътнат, но 12 хотела влизат в зоната и 1 излиза
    # („Явор“ ≡ Голдън Лайн, слят) — 85 → 96, и водещият ред се сменя.
    (u'хотел златни', u'A3-category+zone/kind', 96, u'решение 1: legacy А3′ непокътнат (12 презонирани влизат)', [
        (u'ОАЗИС/OAZIS', u'к.к. Златни пясъци', u'Хотел'),
    ]),
    (u'детска градина', u"M1-category", 51,
     u'решение 2: няма запис с точно това име — категорийният списък стои сам', [
        (u'ДГ№12 „Ян Бибиян“', u'м-т Шашкъна', u'детска градина'),
    ]),
    # Амандамент №2 (ж) -> §В на подписаното превю: старата П7 контрола „детска
    # градина приморски“ е обезсилена от законна данна (ДГ№19 „Славейче“ е първата
    # градина със зона „район Приморски“). Тези две я заместват: всяка сама държи
    # и клона, и броя, и всяка пада, ако предпазителят (д)+(д′) на П7 отпадне.
    (u'детска ясла аспарухово', u'M2-failopen', 13,
     u'В1: няма ясла в „кв. Аспарухово“ → fail-open по имена, не А3 списък', [
        (u'ДЯ №14 „Звънче“', u'район Одесос', u'детска ясла'),
    ]),
    (u'университет приморски', u'M2-failopen', 9,
     u'В2: няма университет в „район Приморски“ → fail-open; води хотел ПРИМОРСКИ', [
        (u'ПРИМОРСКИ', u'к.к. Св. Св. Константин и Елена', u'Хотел'),
    ]),
]


def check_lot1_gate():
    """The ЛОТ 1 gate; returns the list of failures (empty list = green).

    Same shape and same fail-loud contract as check_p7_gate(): main() exits 1 on
    any entry, and tests/test_places_search_gate.py runs this very function."""
    bad = []
    for label, spec in ((u"gain", LOT1_GAINS), (u"control", LOT1_CONTROLS)):
        for q, branch, n, why, want in spec:
            rows, br = search(q)
            got = [(r.name.strip(), r.zone, r.kind) for r in rows]
            if br != branch:
                bad.append(u"%s `%s`: branch %s, expected %s" % (label, q, br, branch))
            if len(rows) != n:
                bad.append(u"%s `%s`: %d rows, expected %d" % (label, q, len(rows), n))
            if got[:len(want)] != want:
                bad.append(u"%s `%s`: rows differ from the signed expectation "
                           u"(first %d): %s" % (label, q, len(want), got[:len(want)]))
    return bad


# --- ЛОТ 1в-А (04.09) — the alias gate: every row below is MEASURED, not wished.
# The three canals of the lot: the curated class words of the dictionary (S3),
# the alias tokens in `aset` with the class words kept (амандамент А4 т. 1), and
# the whole-alias index EXACT_ALIAS behind the two-token floor (А4 т. 2).
LOT1V_A_GAINS = [
    (u'Висше военноморско училище, Варна', u'A0-exact-alias', 1,
     u'А4 т. 2: целият псевдоним (Wikidata Q7035695, CC0, достъп 03.09.2026) '
     u'се проверява преди A1 — иначе класовият ключ „училище“ го изяжда', [
        (u'ВВМУ „Н. Й. Вапцаров“', u'кв. Чайка', u'университет'),
    ]),
    (u'военноморско', u'M3', 2,
     u'А4 т. 1: единичният токен на псевдонима е в `aset` — ВВМУ пръв', [
        (u'ВВМУ „Н. Й. Вапцаров“', u'кв. Чайка', u'университет'),
        (u'Военноморски клуб', u'район Одесос', u'Хотел'),
    ]),
    (u'военноморско училище', u'M2-failopen', 6,
     u'А4 т. 1: класовата дума ОСТАВА в `aset` — без нея ВВМУ пада втори '
     u'зад „Спортно училище Георги Бенковски“ (измерено)', [
        (u'ВВМУ „Н. Й. Вапцаров“', u'кв. Чайка', u'университет'),
        (u'Спортно училище Георги Бенковски', u'кв. Чайка', u'училище'),
    ]),
    (u'гимназия', u'M1-category', 57,
     u'S3/К2: „гимназия“ → училище (ЗПУО чл. 17–18) — M3/12 става M1/57', [
        (u'ОУ "Васил Априлов"', u'м-т Шашкъна', u'училище'),
        (u'8 СОУПЧЕ', u'Морска градина', u'училище'),
    ]),
    (u'гимназия богоров', u'M2', 1,
     u'S3: класовата дума + собственото име — 13 реда стават 1', [
        (u'ПГИ „Д-р Иван Богоров“', u'ж.к. Младост', u'училище'),
    ]),
    (u'поликлиника', u'M1-category', 7,
     u'S3/К2: разговорната форма, подписана изрично от Петър (Gate 1-А) — 1 → 7', [
        (u'„ДКЦ 4 – Варна“ ЕООД', u'кв. Изгрев', u'ДКЦ'),
        (u'„ДКЦ Чайка“ ЕООД', u'кв. Чайка', u'ДКЦ'),
    ]),
    (u'диагностично-консултативен център 3', u'M2', 1,
     u'S3/К2: ЗЛЗ чл. 10 — 0 реда стават 1', [
        (u'„ДКЦ 3 – Варна“ ЕООД', u'ж.к. Владислав Варненчик', u'ДКЦ'),
    ]),
    (u'езикова гимназия', u'M2', 2,
     u'І ЕГ ← Wikidata Q12291800, IV ЕГ ← Q12299161 + регистъра school#40: '
     u'12 реда без нито една ЕГ стават 2, I ЕГ пръв', [
        (u'I ЕГ', u'кв. Изгрев', u'училище'),
        (u'IV ЕГ Жолио Кюри', u'ж.к. Бриз', u'училище'),
    ]),
    (u'международен дом на учените', u'M3', 1,
     u'К4: OSM way 199237000 (ODbL) — хотелът МДУ се намира по разгърнатото име', [
        (u'МДУ ФРЕДЕРИК ЖОЛИО-КЮРИ', u'к.к. Св. Св. Константин и Елена', u'Хотел'),
    ]),
]

LOT1V_A_CONTROLS = [
    # Планът §0 и ADR 008 D2: „морско“ ≠ „военноморско“ — известна дупка, която
    # НЕ се затваря с измислена форма. Мярката: заявката връща морската гимназия
    # и НУЛА реда на ВВМУ; check_lot1v_a_gate() проверява и второто.
    (u'морско училище', u'M2', 1,
     u'известна дупка: ВВМУ НЕ се намира по „морско училище“ (0 реда) — '
     u'псевдоним не се измисля', [
        (u'Морска гимназия "Св. Николай Чудотворец"', u'кв. Аспарухово', u'училище'),
    ]),
    (u'варна', u'M3', 27,
     u'А4 т. 1: „варна“ е генерична географска дума и НЕ влиза в `aset` — '
     u'нула реда само заради псевдоним (проверено поименно)', [
        (u'Варна', u'район Одесос', u'Семеен хотел'),
        (u'Marina Varna Apartments', u'кв. Аспарухово', u'апарт-хотел'),
    ]),
    (u'синчец', u'M3', 2,
     u'А4 т. 2: под прага от два значещи токена — сегашното име ДГ 30 „Синчец“ '
     u'остава пред хотел ДАНА ПАЛАС, чийто СТАР низ е „СИНЧЕЦ“', [
        (u'ДГ 30 "Синчец"', u'ж.к. Младост', u'детска градина'),
        (u'ДАНА ПАЛАС', u'к.к. Златни пясъци', u'Хотел'),
    ]),
]


def check_lot1v_a_gate():
    """The ЛОТ 1в-А gate; returns the list of failures (empty list = green).

    Same fail-loud contract as check_p7_gate()/check_lot1_gate(): main() exits 1
    on any entry and tests/test_places_search_gate.py runs this very function.
    Two of the rows carry a claim a prefix cannot express, so they are checked
    by name here: „морско училище“ must return NO ВВМУ at all, and „варна“ must
    return no row that stands there through an alias alone.
    """
    bad = []
    for label, spec in ((u"gain", LOT1V_A_GAINS), (u"control", LOT1V_A_CONTROLS)):
        for q, branch, n, why, want in spec:
            rows, br = search(q)
            got = [(r.name.strip(), r.zone, r.kind) for r in rows]
            if br != branch:
                bad.append(u"%s `%s`: branch %s, expected %s" % (label, q, br, branch))
            if len(rows) != n:
                bad.append(u"%s `%s`: %d rows, expected %d" % (label, q, len(rows), n))
            if got[:len(want)] != want:
                bad.append(u"%s `%s`: rows differ from the measured expectation "
                           u"(first %d): %s" % (label, q, len(want), got[:len(want)]))
    hole = [r.name for r in search(u"морско училище")[0] if r.name.startswith(u"ВВМУ")]
    if hole:
        bad.append(u"„морско училище“ вече връща ВВМУ (%s) — дупката е затворена "
                   u"без подпис" % u", ".join(hole))
    qt = place_tokens(u"варна")
    alias_only = [r.name for r in search(u"варна")[0]
                  if all(token_match(r, t)[0] == "alias" for t in qt)]
    if alias_only:
        bad.append(u"„варна“ връща редове само по псевдоним: %s"
                   % u", ".join(alias_only))
    return bad




# --- ЛОТ 1в-Б (04.09) — the address gate: Сол S4's SIX queries, measured here
# with the delivery of P5 (25a6d79). Three of them are the gains of the new
# A3-street branch, three are controls that must NOT move: the number without a
# street, the zone phrase and the name phrase both keep their branch.
LOT1V_B_GAINS = [
    (u'детска градина дойран', u'A3-street', 1,
     u'S4 гейт 1: „<клас> <улица>“ — класът на улицата, само ДГ№12 '
     u'(ул. ДОЙРАН 9, КАИС); преди лота заявката даваше 12 реда по fail-open', [
        (u'ДГ№12 „Ян Бибиян“', u'м-т Шашкъна', u'детска градина'),
    ]),
    (u'дойран 9', u'A3-street', 1,
     u'S4 гейт 2: „<улица> <номер>“ — само ДГ№12 в местата, без ключ '
     u'(`hasKey=false`), тоест адресната търсачка на сградите остава отгоре '
     u'с Enter, а местата стоят в своята секция; преди лота 0 реда', [
        (u'ДГ№12 „Ян Бибиян“', u'м-т Шашкъна', u'детска градина'),
    ]),
    # S4 предвиди ДВА записа на ул. Дойран (мярката му беше върху 236-те
    # join-нати реда); доставката на P5 носи ТРИ — ЦПЛР „Михаил Колони“ на
    # ул. ДОЙРАН 17 също получи адрес. Редът е този, който Сол поиска (ДГ№12,
    # после очната болница), а третият ред е измерен факт, не отклонение от
    # правилото: подредбата е по близост до центъра (210 / 298 / 349 m).
    (u'ул. дойран', u'A3-street', 3,
     u'S4 гейт 3: „ул. <улица>“ — ДГ№12, после очната болница, после '
     u'общежитието на ул. ДОЙРАН 17 (трети измерен ред, S4 знаеше за два)', [
        (u'ДГ№12 „Ян Бибиян“', u'м-т Шашкъна', u'детска градина'),
        (u'„Университетска специализирана болница по очни болести за активно лечение – Варна“ ЕООД',
         u'м-т Шашкъна', u'болница'),
        (u'ЦПЛР – Средношколско общежитие „Михаил Колони“', u'м-т Шашкъна', u'общежитие'),
    ]),
]

LOT1V_B_CONTROLS = [
    (u'детска градина 12', u'M2', 1,
     u'S4 гейт 4: число без съвпаднала ПЪЛНА улица не участва — заявката '
     u'остава M2 по името „12“, не става адрес', [
        (u'ДГ№12 „Ян Бибиян“', u'м-т Шашкъна', u'детска градина'),
    ]),
    (u'училище владислав варненчик', u'A3-category+zone/kind', 4,
     u'S4 гейт 5: зоната стои ПРЕД улицата — същите 4 зонови училища, макар '
     u'„владислав варненчик“ да е и улична фраза на 4 други записа', [
        (u'ОУ Стоян Михайловски', u'ж.к. Владислав Варненчик', u'училище'),
        (u'ОУ Патриарх Евтимий', u'ж.к. Владислав Варненчик', u'училище'),
        (u'СУ „Пейо Крачолов Яворов“', u'ж.к. Владислав Варненчик', u'училище'),
        (u'І ОУ „Свети княз Борис I“', u'ж.к. Владислав Варненчик', u'училище'),
    ]),
    (u'хотел приморски', u'A3-record+zone-phrase', 5,
     u'S4 гейт 6: колизия улица↔име — без „ул./бул./пл.“ и без номер улицата '
     u'НЕ се избира, така че ПАНОРАМА (бул. ПРИМОРСКИ 31) не влиза', [
        (u'ПРИМОРСКИ', u'к.к. Св. Св. Константин и Елена', u'Хотел'),
        (u'Маргарита', u'район Приморски', u'Семеен хотел'),
        (u'Вемара сити', u'район Приморски', u'Семеен хотел'),
        (u'Траката', u'район Приморски', u'Семеен хотел'),
        (u'Еллинис', u'район Приморски', u'Семеен хотел'),
    ]),
]


# ЛОТ 1в-Б, гейт 6 на Сол: three BARE phrases that intersect a street with a
# name or a zone and must not become an address without „ул./бул./пл.“. They
# live outside the buckets, so the manifest reads them from here — a second copy
# inside the manifest writer would be a second truth.
COLLISION_CONTROLS = ((u"приморски", "M3", u"ПРИМОРСКИ"),
                      (u"роза", "M3", u"ДЯ №7 „Роза“"),
                      (u"владислав варненчик", "M3", u"КАРНИВАЛ"))


def check_lot1v_b_gate():
    """The ЛОТ 1в-Б gate; returns the list of failures (empty list = green).

    Same fail-loud contract as the three gates above. Two claims cannot be put
    into a (branch, n, prefix) triple, so they are checked by name: „дойран 9“
    must carry NO class key (the client renders our section under the untouched
    address search only while `hasKey` is false), and an exact alias must still
    beat its own street when the query carries neither „ул./бул./пл.“ nor a
    number — „алеко константинов“ is І ОУ „Свети княз Борис I“, and only
    „ул. алеко константинов“ is the street.
    """
    bad = []
    for label, spec in ((u"gain", LOT1V_B_GAINS), (u"control", LOT1V_B_CONTROLS)):
        for q, branch, n, why, want in spec:
            rows, br = search(q)
            got = [(r.name.strip(), r.zone, r.kind) for r in rows]
            if br != branch:
                bad.append(u"%s `%s`: branch %s, expected %s" % (label, q, br, branch))
            if len(rows) != n:
                bad.append(u"%s `%s`: %d rows, expected %d" % (label, q, len(rows), n))
            if got[:len(want)] != want:
                bad.append(u"%s `%s`: rows differ from the measured expectation "
                           u"(first %d): %s" % (label, q, len(want), got[:len(want)]))
    keys, _slots, _dead = split_keys(place_tokens(u"дойран 9"))
    if keys:
        bad.append(u"„дойран 9“ носи класов ключ %s — адресните резултати на "
                   u"сградите вече не са отгоре" % u", ".join(keys))
    rows, br = search(u"алеко константинов")
    if br != "A0-exact-alias" or [r.name for r in rows] != [u"І ОУ „Свети княз Борис I“"]:
        bad.append(u"колизия улица↔псевдоним: „алеко константинов“ дава %s/%d (%s) — "
                   u"псевдонимът трябва да е пръв без „ул./бул./пл.“"
                   % (br, len(rows), u", ".join(r.name for r in rows[:3])))
    rows, br = search(u"ул. алеко константинов")
    if br != "A3-street":
        bad.append(u"„ул. алеко константинов“ дава %s — с префикс улицата печели" % br)
    # Гейт 6 на Сол е защитен от РЕДА на клоновете (A3-record+zone-phrase стои
    # преди улицата), не от правилото за колизия — измерено 04.09. Затова
    # правилото си има собствени редове: три голи улични фрази, които се
    # пресичат с име или зона и НЕ бива да стават адрес без „ул./бул./пл.“.
    for q, want_branch, want_first in COLLISION_CONTROLS:
        rows, br = search(q)
        first = rows[0].name if rows else u"—"
        if br != want_branch or first != want_first:
            bad.append(u"колизия улица↔име/зона: „%s“ дава %s/%s, очаквано %s/%s — "
                       u"без „ул./бул./пл.“ и без номер улицата не се избира"
                       % (q, br, first, want_branch, want_first))
    return bad


# --- ЛОТ 1в-В (04.09) — the typed-location gate: the six queries план §3ж S3
# named, MEASURED on the P6 delivery (varna_3d 756d166), plus three controls.
# Where Sol's expectation and the delivery disagreed the DELIVERY is written
# down and the difference is named in the manifest, never smoothed over:
#   · „училище възраждане“ = 2, not 1 — ОУ „Свети Иван Рилски“ keeps the row it
#     always had through its OWN old zone word („ж.к. Възраждане“, indexed per
#     record and shown nowhere). Its card now says „район Младост“, which is the
#     repair Petar asked for; whether the old word should keep the row is a line
#     in the manifest, not a decision for the executor;
#   · „детска градина владиславово“ = 5 — ДГ№40 „Детски свят“ is the fifth and
#     it arrives by the same old-word index, not by a registry segment.
LOT1V_V_GAINS = [
    (u'училище младост', u'A3-location', 11,
     u'S3 гейт 1: кварталът пръв, после районът САМО за записите без квартал — '
     u'2 в ж.к. Младост 2 + 9 в район Младост, между тях Гео Милев и Иван Рилски', [
        (u'ПГИ „Д-р Иван Богоров“', u'ж.к. Младост 2', u'училище'),
        (u'СУ „Неофит Бозвели“', u'район Младост', u'училище'),
        (u'ОУ „Иван Вазов“', u'район Младост', u'училище'),
    ]),
    (u'училище възраждане', u'A3-location', 2,
     u'S3 гейт 2: II ОУ по квартал; вторият ред е ОУ „Свети Иван Рилски“ по '
     u'СТАРАТА си зонова дума — измерено, Сол очакваше 1', [
        (u'II ОУ „Никола Йонков Вапцаров“', u'ж.к. Възраждане 2', u'училище'),
        (u'ОУ „Свети Иван Рилски“', u'район Младост', u'училище'),
    ]),
    (u'хотел зпз', u'A3-location', 1,
     u'S3 гейт 3: само АДАМО — „ЗПЗ“ е псевдоним на допълнителното място и '
     u'живее в стария ред на записа, не върху цял район', [
        (u'АДАМО', u'район Младост', u'Хотел'),
    ]),
    (u'хотел морска градина', u'A3-location', 18,
     u'S3 гейт 4: 18-те стари реда остават намираеми по думата, която вече не '
     u'се показва никъде', [
        (u'Орбита', u'район Одесос', u'Хотел'),
        (u'РЕВЕРАНС', u'район Одесос', u'Хотел'),
        (u'Family Hotel Astra', u'район Одесос', u'хотел · без категоризация'),
    ]),
    (u'училище владислав варненчик', u'A3-location', 4,
     u'S3 гейт 5: точно 4-те училища на квартала — показът е „кв. Владиславово“, '
     u'а „ж.к. Владислав Варненчик“ е негов псевдоним (§3в)', [
        (u'ОУ Стоян Михайловски', u'кв. Владиславово', u'училище'),
        (u'ОУ Патриарх Евтимий', u'кв. Владиславово', u'училище'),
        (u'СУ „Пейо Крачолов Яворов“', u'кв. Владиславово', u'училище'),
        (u'І ОУ „Свети княз Борис I“', u'кв. Владиславово', u'училище'),
    ]),
    (u'детска градина владиславово', u'A3-location', 5,
     u'S3 гейт 6: 4 по квартал + ДГ№40 по старата си зонова дума — мярката '
     u'реши (Сол очакваше 4 или 5)', [
        (u'ДГ 39 "Приказка"', u'кв. Владиславово', u'детска градина'),
        (u'ОДЗ Маргаритка', u'кв. Владиславово', u'детска градина'),
        (u'ДГ№41 „Първи юни“', u'кв. Владиславово', u'детска градина'),
        (u'ДГ№37 „Пламъче“', u'кв. Владиславово', u'детска градина'),
        (u'ДГ№40 „Детски свят“', u'район Владислав Варненчик', u'детска градина'),
    ]),
]

LOT1V_V_CONTROLS = [
    (u'училище район младост', u'A3-district', 12,
     u'изричното „район X“ пита ЦЕЛИЯ район — 12, тоест 11-те горе минус '
     u'ПГИ (тя е в квартала, но КАИС я държи в район Младост) плюс двете с '
     u'квартал в друг район', [
        (u'ОУ „Иван Вазов“', u'район Младост', u'училище'),
        (u'Професионална гимназия по електротехника', u'район Младост', u'училище'),
        (u'Професионална Техническа Гимназия', u'район Младост', u'училище'),
    ]),
    (u'училище морска градина', u'A3-location', 6,
     u'старата зонова дума на местата: 6-те училища остават, както §3ж S2 иска', [
        (u'8 СОУПЧЕ', u'район Одесос', u'училище'),
        (u'ОУ "Св.св.Кирил и Методий"', u'район Одесос', u'училище'),
        (u'ВТГ „Георги Стойков Раковски"', u'район Одесос', u'училище'),
    ]),
    (u'район младост', u'A3-district', 36,
     u'изричното „район X“ работи и БЕЗ класова дума — 36-те записа на района, '
     u'по близост; без ключ, значи стоим под адресната търсачка на сградите', [
        (u'ОУ „Иван Вазов“', u'район Младост', u'училище'),
        (u'Професионална гимназия по електротехника', u'район Младост', u'училище'),
        (u'Професионална Техническа Гимназия', u'район Младост', u'училище'),
    ]),
    (u'бул. владислав варненчик 225', u'A3-street', 1,
     u'булевардът е улица: разпознава се ПРЕДИ всяко местоположение и не '
     u'докосва квартала със същото име', [
        (u'ОУ „Свети Иван Рилски“', u'район Младост', u'училище'),
    ]),
]

DISTRICT_CODES = (u"primorski", u"odesos", u"mladost", u"asparuhovo",
                  u"vladislav_varnenchik")


def check_lot1v_v_gate():
    """The ЛОТ 1в-В gate: the typed schema, the guards and the nine queries.

    Same fail-loud contract as the four gates above. The schema half is what
    makes „100 % с извор“ measurable — a record without a district, a code
    outside the closed lists or a compat label that does not follow from the
    typed fields is red here, in the суite, without a browser."""
    bad = []
    if not LEGACY_SHA_OK:
        bad.append(u"legacy_bundle_sha: речникът е строен срещу друг пакет — "
                   u"старите зонови думи са изключени (fail-closed)")
    for r in RECS:
        if not r.district or r.district.get("code") not in DISTRICT_CODES:
            bad.append(u"%s: район извън затворения списък (%s)"
                       % (r.name, json.dumps(r.district, ensure_ascii=False)))
            continue
        want = (r.quarter or {}).get("name") or (u"район " + r.district["name"])
        if r.zone != want:
            bad.append(u"%s: `zone` = %s, а типовите полета дават %s"
                       % (r.name, r.zone, want))
        if r.quarter and r.quarter.get("code") not in LOCATIONS[u"quarter"]:
            bad.append(u"%s: квартал извън речника (%s)" % (r.name, r.quarter.get("code")))
        if r.locality and r.locality.get("code") not in LOCATIONS[u"locality"]:
            bad.append(u"%s: допълнително място извън речника (%s)"
                       % (r.name, r.locality.get("code")))
        if r.zone in r.legacy:
            bad.append(u"%s: старата зонова дума е и показваната зона (%s)"
                       % (r.name, r.zone))
    for label, spec in ((u"gain", LOT1V_V_GAINS), (u"control", LOT1V_V_CONTROLS)):
        for q, branch, n, why, want in spec:
            rows, br = search(q)
            got = [(r.name.strip(), r.zone, r.kind) for r in rows]
            if br != branch:
                bad.append(u"%s `%s`: branch %s, expected %s" % (label, q, br, branch))
            if len(rows) != n:
                bad.append(u"%s `%s`: %d rows, expected %d" % (label, q, len(rows), n))
            if got[:len(want)] != want:
                bad.append(u"%s `%s`: rows differ from the measured expectation "
                           u"(first %d): %s" % (label, q, len(want), got[:len(want)]))
    if has_key_of(u"бул. владислав варненчик 225"):
        bad.append(u"„бул. владислав варненчик 225“ носи класов ключ — адресната "
                   u"търсачка на сградите вече не е отгоре")
    return bad


def check_p7_gate():
    """Runs the gate; returns the list of failures (empty list = green).

    Р7: this is what makes the reference able to FAIL. main() exits 1 on any
    entry here, and tests/test_places_search_gate.py runs the same function, so
    a regression is red in the suite without a human eye."""
    bad = []
    n_tok = sum(len(v) for v in P7_ADDED.values())
    if n_tok != 7 or len(P7_ADDED) != 6:
        bad.append(u"p7_added: expected 7 tokens in 6 zones, got %d in %d (%s)"
                   % (n_tok, len(P7_ADDED),
                      json.dumps(P7_ADDED, ensure_ascii=False, sort_keys=True)))
    if P7_ADDED != P7_EXPECTED:
        bad.append(u"p7_added != §11 v2.1: %s"
                   % json.dumps(P7_ADDED, ensure_ascii=False, sort_keys=True))
    for label, spec in ((u"gain", P7_GAINS), (u"control", P7_CONTROLS)):
        for q, branch, n, why, want in spec:
            rows, br = search(q)
            got = [(r.name.strip(), r.zone, r.kind) for r in rows]
            if br != branch:
                bad.append(u"%s `%s`: branch %s, expected %s" % (label, q, br, branch))
            if len(rows) != n:
                bad.append(u"%s `%s`: %d rows, expected %d" % (label, q, len(rows), n))
            if got[:len(want)] != want:
                bad.append(u"%s `%s`: rows differ from the measured expectation "
                           u"(first %d): %s" % (label, q, len(want), got[:len(want)]))
    return bad


G12B = [(u"VII", "7"), (u"седмо", "7"), (u"7-мо", "7"), (u"І", "1"),
        (u"св.", u"sveti"), (u"д-р", u"doktor"), (u"х-л", u"hotel"),
        (u"к-с", u"kompleks"), (u"апартхотел", u"hotel")]

# ------------------------------------------------- counterfactual rule repairs
VARIANTS = [
    (u"§10 буквално (без П2–П5) — прогонът v2.1", {}),
    (u"**подписаният набор П2+П3+П4+П5 — v2.2**", dict(BASE)),
    (u"−П5 (за сравнение: `йо` остава ненамерен)", dict(BASE, P5=False)),
    (u"+П1 (отхвърлен: мени и `берлин голдън бийч` 16→14)", dict(BASE, P1=True)),
]

# ---------------------------------------- narrative: cause + smallest repair
MISS_WHY = {
    u"роял": (u"**А7** (подредбата). И трите са точни (k3), с 1 именно съвпадение "
              u"и еднаква сума → решава „разстояние до центъра ↑“, а Royal Beach "
              u"(Чайка, 11 258 м) стои МЕЖДУ двата РОЯЛ (1 583 м и 12 428 м). "
              u"Очакването на А8 „РОЯЛ, РОЯЛ, после Royal Beach“ иска критерий, "
              u"който А7 няма.",
              u"**П2** — между „действащ преди бивш“ и „разстояние“ се вмъква "
              u"**покритие на името ↑**: РОЯЛ покрива цялото си име (0 непокрити "
              u"токена), Royal Beach — половината (1 непокрит). Един ключ повече "
              u"в сортировката; не пипа „най-близкият първи“ при равни имена "
              u"(тримата Адмирали остават както са)."),
    u"royal": (u"Същото като `роял`.", u"Същото — **П2**."),
    u"парк": (u"**А8 сам по себе си**: „18 реда, всички с точно ПАРК“ не може да е "
              u"вярно едновременно — точните са **12**, а 19 се получава само с "
              u"размитата опашка (Арт, Art Green…, Апарт комплекс…, АРЕНА МАР, "
              u"ДОЛЧЕ МАРЕ, ПАЛМ БИЙЧ — всички на Левенщайн 2 от `park`). "
              u"Правилото-причина за опашката е **А5+М2**: `парк` е 4 знака ≥3 → "
              u"значеща, а М2 дава размито от 4 знака нагоре.",
              u"**П1** — размитото да важи от **6** оригинални знака нагоре "
              u"(4–5 знака: точно/префикс/Левенщайн ≤1). Тогава `парк` = 12 реда, "
              u"всички с точно ПАРК; `хотел амирал` (6) и `хотел адмиралл` (8) "
              u"остават 3. **Цената:** същият cap стои зад другото число на А8 — "
              u"`берлин голдън бийч` пада от 16 на 14 реда (`бийч` е 4 знака). "
              u"Тоест двете половини на реда „парк“ в А8 не могат да са верни "
              u"едновременно: или 19 реда с размита опашка (както А8 изрично "
              u"позволява за `роял` и `русалка`), или 12 реда, всички точни, и "
              u"тогава числото 16 при `берлин голдън бийч` става 14. **Това е "
              u"решение за Петър, не за скрипта** — затова П1 стои ИЗВЪН "
              u"препоръчания набор."),
    u"болница света марина": (
        u"**А1**. „болница“ е форма с ПРАЗЕН клас → пада до именен токен; "
        u"„света“ съвпада точно (СВЕТА ЕЛЕНА…), „марина“ — точно/размито "
        u"(Санта Марина, Marina Varna…), а М2 иска само ЕДНА значеща дума → 16 реда.",
        u"**П4** — празният клас остава именен токен, но е и **филтър**: ред без "
        u"съвпадение по име/псевдоним за самата дума („болница“) отпада → 0 реда. "
        u"Не пипа „градина“→ГРАДИНА, „аквапарк клуб“, „галерия графит“, "
        u"„комплекс ritsa“ (там думата съвпада с името)."),
    u"градина 12": (
        u"**А5**. След А1 „градина“ е име (и намира хотел ГРАДИНА); „12“ е числов "
        u"токен без ключ → по А5 не е значещ, но и не пречи — а М2 иска само една "
        u"значеща дума. §3 М5 чака 0 („класът не е в доставката“), А8 мълчи.",
        u"**П3** — числов токен, който не съвпада ТОЧНО с токен на записа, "
        u"отхвърля записа (числата са конюнктивни). „КАМПУС 90“ остава намираем "
        u"(90 съвпада), „402“/„бл 402“/„вх 3“ си остават 0."),
}

DIFF_G = [
    u"Освен буквалните А1–А8, за да тръгне изобщо, се наложиха следните "
    u"уточнения — всяко е решение, което §10 оставя отворено:",
    u"",
    u"1. **А1, сканирането.** „Най-дългата форма на позиция“ вече прескача "
    u"НЕнаселените форми и опитва по-къса: инак `детска градина` би глътнала "
    u"`градина`, а класът ѝ е празен. Ключ е само форма с ≥1 зареден запис.",
    u"2. **А1, вторите ключове.** Ключ-думите след най-левия се връщат като "
    u"именни токени НА СВОЯТА ПОЗИЦИЯ (важно, докато псевдонимите бяха фраза; "
    u"след А6 вече е без значение).",
    u"3. **А1, fail-open.** Повторението с ключовете като имена се прави върху "
    u"ЦЯЛАТА доставка (не в класа) и с изключен ключов режим; клон "
    u"`M2-failopen`. В този прогон не се задейства нито веднъж.",
    u"4. **А2, откъде е главната дума.** `forms[форма] → [чип]`, после "
    u"`chips[].head` за този чип; правилото важи само за ЕДНО-токенните форми "
    u"(както е записано). К2(б) от §3 се пази — А2 е добавка, не замяна.",
    u"5. **А3′ — единственото същинско доуточняване.** А3 буквално („всеки "
    u"останал токен съвпада точно със зонов или видов токен“) чупи "
    u"„хотел градина“: `градина` е зонов токен на **Морска градина** и заявката "
    u"връща 2-та хотела в тази зона вместо хотел ГРАДИНА. Затова приоритетът на "
    u"А4 (**име точно > зона/вид точно**) важи и при ИЗБОРА на клона: А3 се "
    u"пуска само ако никой остатъчен токен не съвпада ТОЧНО с име в класа. "
    u"С това „хотел златни“ = 85 и „хотел семеен“ = 50 остават, а "
    u"„хотел градина“ = ГРАДИНА.",
    u"6. **А3, филтърът е конюнктивен** (записът трябва да покрие ВСИЧКИ "
    u"остатъчни токени по зона/вид); празен резултат пропада към именното "
    u"търсене, не към 0.",
    u"7. **А4, псевдонимът е ТОЧНО съвпадение.** В приоритетния списък "
    u"„псевдоним“ е едно ниво между „име точно“ и „зона/вид точно“ → без "
    u"префикс и без размито по псевдоним. Тежести за сумата: име `2×качество`, "
    u"зона/вид `3` (М4: име ×2, зона ×1 при качество 3).",
    u"8. **А5, клаузата „с ключ“ е РАЗШИРЕНИЕ, не замяна.** Ако „значеща с ключ“ "
    u"означаваше САМО точно/префиксно съвпадение, „хотел амирал“ пада от 3 на 1 "
    u"ред (АДМИРАЛ съвпада само размито), а М5 иска 3. Затова: базата "
    u"(≥3 знака, не маркер, не число) важи винаги, а ключът ДОБАВЯ късите точни "
    u"съвпадения („хотел йо“) и точните числа.",
    u"9. **А5, адресните маркери не са значещи никога** — и с ключ. Инак "
    u"„хотел бл“ би бил заявка.",
    u"10. **А6, псевдонимните токени не дават кредит на числа** и падат при "
    u"≤2 знака (затова „Арабела блок С“ = само `arabela`, а „Мак“ (3) остава).",
    u"11. **А7, „българска азбучна“** = `name.lower()` по кодови точки "
    u"(непроменено от v2); центърът за близостта е началният `setView` "
    u"(43.2141, 27.9147), защото в безглав прогон няма карта.",
    u"",
    u"12. **П2/П3/П4/П5 (подписани 02.09).** П2 добавя „покритие на името ↑“ в А7 "
    u"между статуса и разстоянието; П3 прави числовия токен конюнктивен; П4 прави "
    u"празния клас филтър с ТОЧНО съвпадение по име/псевдоним; П5 пуска "
    u"2-знаковата дума без ключ, но само срещу едно-токенно име, съвпаднало точно. "
    u"П1 е отхвърлена.",
    u"",
    u"**Какво се смени в поведението спрямо v2** (същите данни, същият cap):",
    u"",
    u"| заявка/мярка | v2 | v2.1 | правилото |",
    u"|---|---|---|---|",
    u"| 4-те неоткриваеми (ГРАДИНА, ГАЛЕРИЯ ГРАФИТ, Апарт комплекс Ritsa, "
    u"ПРЕСТИЖ ДЕЛУКС АКВАПАРК КЛУБ) | 0 реда | намерени, 1-ви ред | А1 |",
    u"| `хотели` / `хотелите` | 217 | **226** | А2 |",
    u"| `хотел златни` | 1 (Златен рог) | **85** | А3 |",
    u"| `хотел семеен` | (не е в М5) | **50** | А3 |",
    u"| `адмирал златни` · `хотел адмирал златни пясъци` | 4 | **3** | А4 |",
    u"| `lti` | 0 | **1, БЕРЛИН ГОЛДЪН БИЙЧ** | А6 |",
    u"| `лти берлин` | ГРИЙН ПАРК първи | **ГОЛДЪН БИЙЧ първи** | А6 |",
    u"| `блок с` · `бл. 402` | 1 (Адия Блу) | **0** | А5 |",
    u"| `7 су` · `седмо су` · `vii су` | 2 | **0** | А5 |",
    u"| `мак` | (не е в М5) | **ПРЕСТИЖ ДЕЛУКС АКВАПАРК КЛУБ** | А6 |",
    u"| `русалка` | РУСАЛКА, Русалка, Musala | същите, но редът е гейтнат | А7 |",
    u"| `роял` · `royal` | РОЯЛ, **Royal Beach**, РОЯЛ | РОЯЛ, РОЯЛ, Royal Beach | П2 |",
    u"| `болница света марина` | 16 | **0** | П4 |",
    u"| `градина 12` | 1 (ГРАДИНА) | **0** | П3 |",
    u"| `парк` | 18, редът не е гейтван | **19 = 12 точни + 7 размити**, гейтван | А8 (факт) |",
    u"| М5 по А8 | 19/35 (v2) → 31/36 (v2.1) | **36/36** | П2+П3+П4 |",
    u"| `йо` (гола заявка) | 0 реда | **хотел Йо** | П5 |",
    u"| A1 / A2 recall | 222/226 · 225/225 | **226/226 · 226/226** | А1 + П5 |",
    u"",
    u"**Остатъчните проблеми след v2.1 (с причина):**",
    u"",
    u"1. **`йо` — ЗАТВОРЕН с П5** (подписана 02.09). Без ключ 2-знакова дума е "
    u"значеща само при ТОЧНО съвпадение със запис, чието цяло име е този единствен "
    u"токен; префиксните 2-знакови съвпадения продължават да не квалифицират. "
    u"А1/А2 = **226/226**, 36/36 и 10/10 остават, нула други промени "
    u"(редът `−П5` в в4 е мярката).",
    u"2. **`парк` — ЗАТВОРЕН** с поправката на очакването като факт (12 точни "
    u"първи, после 7 размити = 19 реда); гейтът вече проверява и разделянето "
    u"12/7, не само броя.",
    u"3. **`чайка` → Villa Chinka** (1 ред, размито). Зоната „к.к. Чайка“ не "
    u"квалифицира сама (правилно по §3), но `chaika`~`chinka` е на Левенщайн 2. "
    u"П1 (размито от 6 знака) го маха; иначе е безобиден единичен ред.",
    u"4. **`берлин голдън бийч` = 16 реда**, от които 11 съдържат точен токен от "
    u"заявката — първият ред е верният, останалите са опашка по `голдън`/`бийч`. "
    u"А8 го приема така.",
]

# ADR 008 D7 — the bucket list of the artefact, fail-closed and hand-kept on
# THREE sides: here, in the probe that replays the rows
# (scratch/places_search/probe_places_fv.mjs, `REF_BUCKETS`) and in the suite
# (tests/test_places_search_gate.py, `REF_BUCKETS`), which compares all three.
# A bucket added on one side alone would grow or shrink the reference in silence.
# main() refuses to write an artefact whose keys are not exactly this list.
REF_BUCKETS = ("gate_m5_a8", "extra", "gate_p7", "gate_lot1", "gate_lot1v_a",
               "gate_lot1v_b")
# ЛОТ 1в-В (план §3ж S2): the bucket the CANDIDATE carries and the frozen
# artefact does not. It becomes the seventh member of REF_BUCKETS on all three
# sides in the same commit that freezes the reference — after Petar signs the
# manifest, never before. Until then it is allowed in the report-only candidate
# and in nothing else.
PENDING_BUCKET = "gate_lot1v_v"
# F12-б/в: the М7 bucket. Same rule as the one above — it rides the report-only
# candidate and the P7 → F12 manifest, and it joins REF_BUCKETS on all three
# sides only in the commit that freezes the reference, after Petar signs.
M7_BUCKET = "gate_m7_bare"


def m7_queries():
    """Every query the М7 bucket carries — measured, never hand-listed.

    Two shapes, both of them „a bare place and nothing else“: the FULL phrase of
    every quarter and locality the delivery carries (that is what a human types
    when he knows the name — „златни пясъци“), and every SINGLE word that can
    reach the branch (that is what he types when he does not — „златни“). The
    list is derived from the delivered rows, so it moves with the delivery and
    the signed `m7_trigger_tokens.json` describes exactly the second half."""
    out = set()
    for rec in RECS:
        for cls, field in ((u"quarter", rec.quarter), (u"locality", rec.locality)):
            if not field:
                continue
            for phrase in LOC_PHRASES[cls].get(field.get("code")) or ():
                out.add(phrase)
        if rec.quarter:
            out.update(rec.qtk)
        if rec.locality:
            out.update(rec.ltk)
    return sorted(out)


def bucket_drift(doc, pending=()):
    """The keys of an artefact against REF_BUCKETS; empty list = no drift.

    `pending` is the report-only escape hatch and it is explicit at every call
    site: a bucket named there is allowed in a CANDIDATE, never in the frozen
    reference (main() passes nothing when it writes the tracked file)."""
    drift = [u"липсва " + b for b in REF_BUCKETS
             if not isinstance(doc.get(b), list)]
    drift += [u"нов " + b for b in doc
              if b != "_meta" and b not in REF_BUCKETS and b not in pending]
    return drift


def base_adapter(doc):
    """READ-ONLY view of the frozen artefact in the candidate's shape (S2).

    The base was written before the typed fields existed: `hasKey` and the
    three location fields are simply absent there, so the adapter fills them
    with None and the comparator reads None as „the base cannot say“, never as
    a difference. Returns (entries, duplicates); nothing is written back."""
    entries, duplicates = {}, []
    for bucket, rows in doc.items():
        if bucket == "_meta" or not isinstance(rows, list):
            continue
        for entry in rows:
            key = (bucket, entry.get("q"))
            if key in entries:
                duplicates.append(u"%s · %s" % key)
                continue
            entries[key] = {
                "branch": entry.get("branch"),
                "hasKey": entry.get("hasKey"),
                "n": entry.get("n"),
                "rows": [{"name": r.get("name"), "zone": r.get("zone"),
                          "kind": r.get("kind"), "quarter": r.get("quarter"),
                          "district": r.get("district"), "locality": r.get("locality")}
                         for r in (entry.get("rows") or [])],
            }
    return entries, duplicates


def compare_buckets(base, cand):
    """(bucket, q) by (bucket, q): what moved, what did not, what must STOP.

    The comparison is the one S2 named — branch, hasKey and the ORDERED rows —
    and the row identity is (name, zone): the base knows no typed fields, so a
    typed field can only ever be new, never „changed“. `pending` rows (a bucket
    the base never had) are reported apart from the STOP-worthy `extra`."""
    moved, unchanged, extra, missing = [], [], [], []
    for key in sorted(cand, key=lambda k: (k[0], k[1] or u"")):
        bucket, q = key
        if key not in base:
            # A row of the PENDING bucket is new by construction — it is the new
            # bucket itself. A row that appears in a FROZEN bucket is an extra,
            # and an extra is a STOP: the reference may only grow by signature.
            if bucket in REF_BUCKETS:
                extra.append({"bucket": bucket, "q": q,
                              "why": u"нов ред в замразен bucket"})
            continue
        old, new = base[key], cand[key]
        old_rows = [(r["name"], r["zone"]) for r in old["rows"]]
        new_rows = [(r["name"], r["zone"]) for r in new["rows"]]
        why = []
        if old["branch"] != new["branch"]:
            why.append(u"клон %s → %s" % (old["branch"], new["branch"]))
        if old["hasKey"] is not None and old["hasKey"] != new["hasKey"]:
            why.append(u"hasKey %s → %s" % (old["hasKey"], new["hasKey"]))
        if len(old_rows) != len(new_rows):
            why.append(u"редове %d → %d" % (len(old_rows), len(new_rows)))
        elif [r[0] for r in old_rows] != [r[0] for r in new_rows]:
            why.append(u"друга подредба или други записи")
        elif old_rows != new_rows:
            why.append(u"само етикетът на зоната")
        record = {"bucket": bucket, "q": q,
                  "old": {"branch": old["branch"], "hasKey": old["hasKey"],
                          "rows": old["rows"]},
                  "new": {"branch": new["branch"], "hasKey": new["hasKey"],
                          "rows": new["rows"]},
                  "why": why}
        (moved if why else unchanged).append(record)
    for key in sorted(base, key=lambda k: (k[0], k[1] or u"")):
        if key not in cand:
            missing.append({"bucket": key[0], "q": key[1],
                            "why": u"редът го няма в кандидата"})
    return moved, unchanged, extra, missing


# Г7 (план §2) — the ten records Petar reads with his own eyes, one per root
# cause. The keys are matched against the delivered names and each one must
# resolve to EXACTLY one record; 0 or 2 is a failure of the manifest, not a
# reason to guess.
LOT1V_V_FIXTURE = (
    (u"СУ „Гео Милев“", u"чертаната обвивка ЗПЗ падна — районът е честният отговор"),
    (u"ОУ „Свети Иван Рилски“", u"обвивката „Възраждане“ падна; училището е в район Младост"),
    (u"ДГ 32 \"Моряче\"", u"ЗПЗ не е квартал (типовият гейт)"),
    (u"ДГ 36 \"Морска звездица\"", u"ЗПЗ слиза в „допълнително“, кварталът остава празен"),
    (u"„Университетска многопрофилна болница за активно лечение „Света Марина““ ЕАД",
     u"КАИС кварталът печели: к.к. Св. Св. Константин и Елена"),
    (u"Дукеса", u"хотел от Морска градина → район Приморски"),
    (u"АДАМО", u"хотел от ЗПЗ → район Младост; „зпз“ остава търсима дума на реда"),
    (u"Вентура", u"кв. Аспарухово без извор → район Аспарухово"),
    (u"ПРЕСЛАВ", u"подписаният курортен override (SIGNED_OVERRIDE)"),
    (u"„Многопрофилна болница за активно лечение Варна“ ЕООД",
     u"вече беше „район X“ — контролата, която НЕ мърда"),
)


# The generation the manifest is measured AGAINST: the last commit of лот Б — the
# one the frozen reference AND the previous delivery both come from. „HEAD“ would
# answer with the new labels the moment the delivery is committed, and a manifest
# that compares a thing to itself says „nothing moved“ in perfect good faith.
BASE_COMMIT = u"f06ac06"


def delivered_zones(commit=BASE_COMMIT):
    """{(bundle, ordinal): (name, zone)} as a COMMIT delivers it — None if git cannot.

    The manifest has to say how many RECORDS change their label, and the only
    honest source for the old label is the committed blob, never a memory of
    it. The key is the ORDINAL, not the name: „РОЯЛ“ is delivered twice (a hotel
    and a place), and a name-keyed dictionary silently loses one of them — the
    count came out 210 instead of 209 while the two files agree row for row."""
    import subprocess
    out = {}
    for key, path in ((u"hotels", u"data/hotels.json"), (u"places", u"data/places.json")):
        got = subprocess.run(["git", "-C", str(REPO_ROOT), "show",
                              u"%s:%s" % (commit, path)],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if got.returncode != 0:
            return None
        try:
            doc = json.loads(got.stdout.decode("utf-8"))
        except ValueError:
            return None
        for n, rec in enumerate(doc.get(key) or []):
            out[(key, n)] = (rec.get("name"), rec.get("zone"))
    return out


def write_manifest(rows_doc, candidate_path, candidate_text):
    """The old → new manifest Petar signs BEFORE anything is frozen (S2).

    Everything in it is measured here and now: the SHA of the base, of the
    candidate and of the three inputs, every (bucket, q) that moves with the
    reason it moved, the records whose label changes, the nine gate queries and
    the four STOP conditions. Returns the path it wrote."""
    base_doc = json.loads(pathlib.Path(REPO_ROWS_OUT).read_text(encoding="utf-8"))
    base, duplicates = base_adapter(base_doc)
    cand, cand_dup = base_adapter(rows_doc)
    moved, unchanged, extra, missing = compare_buckets(base, cand)
    # The manifest is read by a HUMAN: it carries the first eight rows of every
    # side — what render() actually shows — and says how many stayed behind. The
    # full ordered lists live in the candidate artefact, whose SHA is pinned above.
    HEAD = TOP

    def row_line(r):
        line = u"%s · %s" % ((r.get("name") or u"").strip(), r.get("zone"))
        loc = r.get("locality") or None
        return line + (u" · доп.: " + loc["name"] if loc else u"")

    def side(entry):
        rows = entry["rows"]
        head = [row_line(r) for r in rows[:HEAD]]
        if len(rows) > HEAD:
            head.append(u"…и още %d" % (len(rows) - HEAD))
        return {"branch": entry["branch"], "hasKey": entry["hasKey"],
                "n": len(rows), "rows": head}

    for record in moved:
        record["old"] = side({"branch": record["old"]["branch"],
                              "hasKey": record["old"]["hasKey"],
                              "rows": record["old"]["rows"]})
        record["new"] = side({"branch": record["new"]["branch"],
                              "hasKey": record["new"]["hasKey"],
                              "rows": record["new"]["rows"]})

    def sha_of(path):
        raw = pathlib.Path(path).read_bytes()
        return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}

    old_zones = delivered_zones()
    changed_records, order_drift = None, []

    def old_zone_of(rec):
        """The label HEAD delivers for THIS row — by ordinal, checked by name."""
        was = old_zones.get((rec.bundle, rec.ordinal))
        if was is None:
            order_drift.append(u"%s:%d липсва в HEAD" % (rec.bundle, rec.ordinal))
            return None
        if was[0] != rec.name:
            order_drift.append(u"%s:%d е „%s“ в HEAD и „%s“ сега"
                               % (rec.bundle, rec.ordinal, was[0], rec.name))
        return was[1]

    if old_zones is not None:
        changed_records = [
            {"name": r.name, "old": old_zone_of(r), "new": r.zone,
             "src": ((r.quarter or {}).get("src") if r.quarter
                     else (r.district or {}).get("src")),
             "locality": (r.locality or {}).get("name")}
            for r in RECS if old_zone_of(r) != r.zone]
    fixture, fixture_bad = [], []
    for key, why in LOT1V_V_FIXTURE:
        hits = [r for r in RECS if r.name.strip() == key.strip()]
        if len(hits) != 1:
            fixture_bad.append(u"%s → %d записа" % (key, len(hits)))
            continue
        r = hits[0]
        fixture.append({"name": r.name, "why": why,
                        "old": None if old_zones is None else old_zone_of(r),
                        "new": r.zone, "quarter": r.quarter, "district": r.district,
                        "locality": r.locality, "legacy_terms": r.legacy})
    gate = []
    for label, spec in ((u"gain", LOT1V_V_GAINS), (u"control", LOT1V_V_CONTROLS)):
        for q, branch, n, why, want in spec:
            rows, br = search(q)
            gate.append({"class": label, "q": q, "expect": why, "branch": br,
                         "hasKey": has_key_of(q), "n": len(rows),
                         "ok": br == branch and len(rows) == n
                               and [(x.name.strip(), x.zone, x.kind) for x in rows][:len(want)] == list(want),
                         "rows": side({"branch": br, "hasKey": has_key_of(q),
                                       "rows": [row_out(x) for x in rows]})["rows"]})
    manifest = {
        "_meta": {
            "what": u"ЛОТ 1в-В · манифест old → new на референцията (report-only)",
            "plan": u"docs/plans/ПЛАН_ЛОТ1в-В_кварталите.md §3ж S2 / §3з",
            "generator": u"scratch/places_search/recall_sweep.py --report-only",
            "generated": None,
            "frozen": False,
            "signed_by_petar": None,
            "pending_bucket": PENDING_BUCKET,
            "note": (u"Референцията НЕ е замразена. Тестовете, които пинват старата, "
                     u"са ЧЕРВЕНИ до подписа — това е гейтът, не дефект."),
            "base": dict(sha_of(REPO_ROWS_OUT),
                         path=u"scratch/places_search/recall_sweep_rows.json",
                         commit=BASE_COMMIT,
                         what=u"артефактът и доставката след лот Б"),
            # The candidate is a MEASUREMENT and lives in the system temp; only its
            # name and its digest belong in a tracked file (an absolute path would
            # pin this artefact to one machine and one user).
            "candidate": {"path": u"<system temp>/fv_measures/"
                                  + candidate_path.rsplit(u"/", 1)[-1],
                          "sha256": hashlib.sha256(candidate_text.encode("utf-8")).hexdigest(),
                          "bytes": len(candidate_text.encode("utf-8"))},
            "inputs": {u"data/places.json": sha_of(PLACES2),
                       u"data/hotels.json": sha_of(HOTELS),
                       u"data/place_categories.json": sha_of(CATS)},
        },
        "totals": {
            "records": len(RECS),
            "quarter": sum(1 for r in RECS if r.quarter),
            "locality": sum(1 for r in RECS if r.locality),
            "district": sum(1 for r in RECS if r.district),
            "records_changing_zone": None if changed_records is None else len(changed_records),
            "reference_rows_base": sum(len(v["rows"]) for v in base.values()),
            "reference_rows_candidate": sum(len(v["rows"]) for v in cand.values()),
            "queries_base": len(base),
            "queries_candidate": len(cand),
            "queries_moved": len(moved),
            "queries_unchanged": len(unchanged),
            "queries_in_pending_bucket": sum(1 for b, _q in cand if b == PENDING_BUCKET),
        },
        "stop_conditions": {
            "duplicate": duplicates + cand_dup,
            "missing": missing,
            "extra": extra,
            "fixture_unresolved": fixture_bad,
            "delivery_order_drift": sorted(set(order_drift)),
            "unsigned": (u"да — манифестът чака подписа на Петър; докато го няма, "
                         u"нищо не се замразява"),
        },
        "gate_queries": gate,
        "fixture_10": fixture,
        "records_changing_zone": changed_records,
        "moved": moved,
        "unchanged": [{"bucket": x["bucket"], "q": x["q"]} for x in unchanged],
    }
    manifest["_meta"]["generated"] = GENERATED_AT
    out = OUTDIR + "lot1v_v_reference_manifest.json"
    open(out, "w", encoding="utf-8").write(
        json.dumps(manifest, ensure_ascii=False, indent=1, sort_keys=False) + chr(10))
    return out


def reference_rows():
    """The seven buckets of the reference, measured here and now.

    It was inline in main() until F12-в: the two manifests have to build the
    same buckets a second time (with the М7 branch switched off) and a copy
    of the loops would be a second truth about what the reference IS."""
    ROWS = {
        "_meta": {
            "source": "measures/recall_sweep_v22.py",
            "rules": "plan sec.3 (T1/T2/K2/M1-M5) + sec.10 A1-A8 + P2+P3+P4 (no P1)",
            "data": ["Fire_Varna/data/hotels.json",
                     "Fire_Varna/data/places.json",
                     "Fire_Varna/data/place_categories.json"],
            "records": len(RECS),
            "center": [CENTER[0], CENTER[1]],
            "top_cut_is_in_render": TOP,
            "note": ("full ordered lists; the TOP-8 cut belongs to render(), not to "
                     "the search. No cadastral identifiers are read or written."),
            # П7 (§11 v2.1): what the quarter aliases actually added, and why
            # every other candidate fell. The C16 gate reads p7_added and goes
            # red on any drift from the seven tokens in six zones (Амандамент №10).
            "p7_added": P7_ADDED,
            "p7_dropped": P7_DROPPED,
            "p7_zones_with_aliases": len(P7_ADDED),
            "p7_tokens": sum(len(v) for v in P7_ADDED.values()),
            "p7_records_touched": sum(1 for r in RECS if r.p7),
            "p7_alias_strings": sum(len(v.get("aliases") or [])
                                    for v in (cats.get("zones") or {}).values()),
        },
        "gate_m5_a8": [],
        "extra": [],
        # С2′: one query per added token plus the controls of §11 Р3 — the probe
        # replays this bucket too, so the JS↔Python parity covers П7 itself.
        "gate_p7": [],
        # ЛОТ 1: the two client rules, in their own bucket — the 103 rows above
        # keep their identity, so the signed change list stays readable.
        "gate_lot1": [],
        # ЛОТ 1в-А (ADR 008 D4/D7, план §2г S3/S6): АДИТИВНО. The 122 rows above
        # did not move one label when the aliases and the curated class words
        # landed (measured against a58010e), so nothing is re-frozen; the twelve
        # measured rows of the new lot arrive as a bucket of their own.
        "gate_lot1v_a": [],
        # ЛОТ 1в-Б (ADR 008 D6/D7, план §2г S4/S6): АДИТИВНО again. Measured
        # against a58010e and against the committed `gate_lot1v_a`, not one of the
        # 122 + 12 rows moved when the addresses and the street branch landed, so
        # nothing is re-frozen; Сол's six queries arrive as a bucket of their own.
        "gate_lot1v_b": [],
        # ЛОТ 1в-В (план §3ж S2/S3): the PENDING bucket. It rides the report-only
        # candidate and the manifest; it becomes the seventh member of REF_BUCKETS
        # on all three sides in the same commit that freezes the reference — after
        # Petar signs, never before.
        "gate_lot1v_v": [],
        # F12-б/в: М7 („голото място“). Every query here is a bare quarter or
        # locality word — the bucket exists so the P7 → F12 manifest can show
        # what the new branch answers, row by row, before anything is frozen.
        "gate_m7_bare": [],
    }
    for _q, _br, _n, _why, _want in P7_GAINS + P7_CONTROLS:
        _r, _b = search(_q)
        ROWS["gate_p7"].append({
            "q": _q,
            "expect": _why,
            "branch": _b,
            "hasKey": has_key_of(_q),
            "n": len(_r),
            "ok": (_b == _br and len(_r) == _n
                   and [(x.name.strip(), x.zone, x.kind) for x in _r][:len(_want)] == _want),
            "rows": [row_out(x) for x in _r],
        })
    for _q, _br, _n, _why, _want in LOT1_GAINS + LOT1_CONTROLS:
        _r, _b = search(_q)
        ROWS["gate_lot1"].append({
            "q": _q,
            "expect": _why,
            "branch": _b,
            "hasKey": has_key_of(_q),
            "n": len(_r),
            "ok": (_b == _br and len(_r) == _n
                   and [(x.name.strip(), x.zone, x.kind) for x in _r][:len(_want)] == _want),
            "rows": [row_out(x) for x in _r],
        })
    # ЛОТ 1в-А: the same shape as the two gates above — `kind` rides in the
    # `ok` flag (the expectation triples of LOT1V_A_GAINS/LOT1V_A_CONTROLS carry
    # it), while the rows keep the (name, zone) schema the artefact has always had.
    for _q, _br, _n, _why, _want in LOT1V_A_GAINS + LOT1V_A_CONTROLS:
        _r, _b = search(_q)
        ROWS["gate_lot1v_a"].append({
            "q": _q,
            "expect": _why,
            "branch": _b,
            "hasKey": has_key_of(_q),
            "n": len(_r),
            "ok": (_b == _br and len(_r) == _n
                   and [(x.name.strip(), x.zone, x.kind) for x in _r][:len(_want)] == _want),
            "rows": [row_out(x) for x in _r],
        })
    for _q, _br, _n, _why, _want in LOT1V_B_GAINS + LOT1V_B_CONTROLS:
        _r, _b = search(_q)
        ROWS["gate_lot1v_b"].append({
            "q": _q,
            "expect": _why,
            "branch": _b,
            "hasKey": has_key_of(_q),
            "n": len(_r),
            "ok": (_b == _br and len(_r) == _n
                   and [(x.name.strip(), x.zone, x.kind) for x in _r][:len(_want)] == _want),
            "rows": [row_out(x) for x in _r],
        })
    for _q, _br, _n, _why, _want in LOT1V_V_GAINS + LOT1V_V_CONTROLS:
        _r, _b = search(_q)
        ROWS["gate_lot1v_v"].append({
            "q": _q,
            "expect": _why,
            "branch": _b,
            "hasKey": has_key_of(_q),
            "n": len(_r),
            "ok": (_b == _br and len(_r) == _n
                   and [(x.name.strip(), x.zone, x.kind) for x in _r][:len(_want)] == _want),
            "rows": [row_out(x) for x in _r],
        })
    for _q in m7_queries():
        _r, _b = search(_q)
        ROWS[M7_BUCKET].append({
            "q": _q,
            "expect": u"М7: голо име на квартал/местност",
            "branch": _b,
            "hasKey": has_key_of(_q),
            "n": len(_r),
            "ok": _b == "M7-bare-location",
            "rows": [row_out(x) for x in _r],
        })
    for _bucket, _spec in [("gate_m5_a8", M5SPEC), ("extra", EXTRASPEC)]:
        for _q, _exp, _fn in _spec:
            _r, _b = search(_q)
            ROWS[_bucket].append({
                "q": _q,
                "expect": _exp,
                "branch": _b,
                "hasKey": has_key_of(_q),
                "n": len(_r),
                "ok": bool(_fn(_r)),
                "rows": [row_out(x) for x in _r],
            })
    return ROWS


def full_side(entry):
    """A whole side of a moved query — ALL rows, not the first eight (Сол S5).

    The eight-row head of the лот-В manifest is what `render()` shows; a
    signature over a head is a signature over a summary, and the rows that were
    cut are exactly the ones nobody checked."""
    return {"branch": entry["branch"], "hasKey": entry["hasKey"],
            "n": len(entry["rows"]),
            "rows": [{"name": (r.get("name") or u"").strip(), "zone": r.get("zone"),
                      "kind": r.get("kind"),
                      # The WITNESS: which channel named the location of this row.
                      # „район X“ carries the district's own source, never a
                      # quarter's — that is the honest answer, and it says so.
                      "witness": ((r.get("quarter") or {}).get("src") if r.get("quarter")
                                  else (r.get("district") or {}).get("src")),
                      "quarter": r.get("quarter"), "district": r.get("district"),
                      "locality": r.get("locality")}
                     for r in entry["rows"]]}


def manifest_diff(base_entries, cand_entries, frozen_only):
    """moved / unchanged / extra / missing between two shapes of the reference."""
    moved, unchanged, extra, missing = compare_buckets(base_entries, cand_entries)
    if frozen_only:
        moved = [m for m in moved if m["bucket"] in REF_BUCKETS]
        unchanged = [u for u in unchanged if u["bucket"] in REF_BUCKETS]
    for record in moved:
        record["old"] = full_side(record["old"])
        record["new"] = full_side(record["new"])
    return moved, unchanged, extra, missing


def sha_and_bytes(path):
    raw = pathlib.Path(path).read_bytes()
    return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}


def manifest_meta(what, base, candidate):
    return {
        "what": what,
        "plan": u"docs/plans/ПЛАН_ЛОТ0_гейтове_P7_F12.md §F12-в",
        "generator": u"scratch/places_search/recall_sweep.py --manifest (report-only)",
        "generated": GENERATED_AT,
        "frozen": False,
        "signed_by": u"pending — Петър",
        "note": (u"Референцията НЕ е замразена и този прогон не я пипа. Тестовете, "
                 u"които пинват старите числа, остават ЧЕРВЕНИ до подписа — това е "
                 u"гейтът, не дефект."),
        "base": base,
        "candidate": candidate,
        "inputs": {u"data/places.json": sha_and_bytes(PLACES2),
                   u"data/hotels.json": sha_and_bytes(HOTELS),
                   u"data/place_categories.json": sha_and_bytes(CATS)},
    }


def write_two_manifests(rows_with_m7):
    """The two diffs of F12-в, both report-only, both showing EVERY row.

    BASE → P7 is the DATA: the frozen artefact of лот Б against today's engine
    with М7 switched OFF, so every difference in it comes from М2+М3+М6 and from
    nothing else. P7 → F12 is the BRANCH: the same engine with М7 off against the
    same engine with М7 on, so every difference in it comes from М7 alone. Two
    causes, two documents — one manifest carrying both would ask Petar to sign a
    sum he cannot take apart."""
    global M7_ENABLED
    base_doc = json.loads(pathlib.Path(REPO_ROWS_OUT).read_text(encoding="utf-8"))
    frozen, frozen_dup = base_adapter(base_doc)
    with_m7, with_dup = base_adapter(rows_with_m7)

    M7_ENABLED = False
    try:
        rows_p7 = reference_rows()
    finally:
        M7_ENABLED = True
    without_m7, without_dup = base_adapter(rows_p7)

    def dump(doc):
        return json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=False) + chr(10)

    p7_text = dump(rows_p7)
    f12_text = dump(rows_with_m7)

    # ---------------------------------------------------------- BASE → P7 (data)
    moved, unchanged, extra, missing = manifest_diff(frozen, without_m7, True)
    old_zones = delivered_zones()
    order_drift = []

    def old_zone_of(rec):
        was = old_zones.get((rec.bundle, rec.ordinal)) if old_zones is not None else None
        if was is None:
            order_drift.append(u"%s:%d липсва в %s" % (rec.bundle, rec.ordinal, BASE_COMMIT))
            return None
        if was[0] != rec.name:
            order_drift.append(u"%s:%d е „%s“ в %s и „%s“ сега"
                               % (rec.bundle, rec.ordinal, was[0], BASE_COMMIT, rec.name))
        return was[1]

    changed_records = None
    if old_zones is not None:
        changed_records = [
            {"name": r.name.strip(), "bundle": u"%s:%d" % (r.bundle, r.ordinal),
             "old": old_zone_of(r), "new": r.zone,
             "witness": ((r.quarter or {}).get("src") if r.quarter
                         else (r.district or {}).get("src")),
             "quarter": r.quarter, "district": r.district, "locality": r.locality,
             "legacy_terms": r.legacy}
            for r in RECS if old_zone_of(r) != r.zone]
    base_p7 = {
        "_meta": manifest_meta(
            u"F12-в · манифест BASE → P7 (данните: М2+М3+М6). М7 е ИЗКЛЮЧЕН тук — "
            u"клонът има свой манифест.",
            dict(sha_and_bytes(REPO_ROWS_OUT),
                 path=u"scratch/places_search/recall_sweep_rows.json",
                 commit=BASE_COMMIT, what=u"замразената референция след лот Б"),
            {"what": u"днешният двигател с М7 = OFF",
             "sha256": hashlib.sha256(p7_text.encode("utf-8")).hexdigest(),
             "bytes": len(p7_text.encode("utf-8"))}),
        "totals": {
            "records": len(RECS),
            "quarter": sum(1 for r in RECS if r.quarter),
            "locality": sum(1 for r in RECS if r.locality),
            "district": sum(1 for r in RECS if r.district),
            "records_changing_zone": None if changed_records is None else len(changed_records),
            "queries_base": len(frozen),
            "queries_candidate": sum(1 for b, _q in without_m7 if b in REF_BUCKETS),
            "queries_moved": len(moved),
            "queries_unchanged": len(unchanged),
            "rows_shown": sum(len(m["old"]["rows"]) + len(m["new"]["rows"]) for m in moved),
        },
        "stop_conditions": {
            "duplicate": frozen_dup + without_dup,
            "missing": missing,
            "extra": extra,
            "delivery_order_drift": sorted(set(order_drift)),
            "unsigned": (u"да — манифестът чака подписа на Петър; докато го няма, "
                         u"нищо не се замразява"),
        },
        "records_changing_zone": changed_records,
        # The лот-В bucket is PENDING: the base never carried it, so it can only
        # be „new“ to the comparator above and would fall out of the document
        # entirely. It is exactly where the expectation of the В-gate queries
        # lives, so it is written out in full — that is what the suite reads
        # instead of a number typed into a test (F12-в).
        "gate_lot1v_v": [{"q": e["q"], "expect": e["expect"], "branch": e["branch"],
                          "hasKey": e["hasKey"], "n": e["n"], "ok": e["ok"],
                          "rows": full_side({"branch": e["branch"], "hasKey": e["hasKey"],
                                             "rows": e["rows"]})["rows"]}
                         for e in rows_p7[PENDING_BUCKET]],
        "moved": moved,
        "unchanged": [{"bucket": x["bucket"], "q": x["q"]} for x in unchanged],
    }

    # ----------------------------------------------------------- P7 → F12 (М7)
    m7_moved, m7_unchanged, m7_extra, m7_missing = manifest_diff(without_m7, with_m7, False)
    touched = [{"bucket": m["bucket"], "q": m["q"], "why": m["why"]}
               for m in m7_moved if m["bucket"] != M7_BUCKET]
    controls = []
    for q, want_branch, want_first in COLLISION_CONTROLS:
        M7_ENABLED = False
        try:
            off_rows, off_branch = search(q)
            off = (off_branch, [r.name.strip() for r in off_rows])
        finally:
            M7_ENABLED = True
        on_rows, on_branch = search(q)
        if (on_branch, [r.name.strip() for r in on_rows]) != off:
            controls.append({
                "q": q, "expected_branch": want_branch, "expected_first": want_first,
                "without_m7": {"branch": off[0], "n": len(off[1]), "first": off[1][0] if off[1] else None},
                "with_m7": {"branch": on_branch, "n": len(on_rows),
                            "first": on_rows[0].name.strip() if on_rows else None},
                "why": u"контрола ИЗВЪН кофите (гейт 6 на Сол) — М7 я мести; иска думата на Петър",
            })
    p7_f12 = {
        "_meta": manifest_meta(
            u"F12-в · манифест P7 → F12 (само М7). Един и същ двигател, едни и същи "
            u"данни, с изключен и с включен клон.",
            {"what": u"днешният двигател с М7 = OFF",
             "sha256": hashlib.sha256(p7_text.encode("utf-8")).hexdigest(),
             "bytes": len(p7_text.encode("utf-8"))},
            {"what": u"днешният двигател с М7 = ON",
             "sha256": hashlib.sha256(f12_text.encode("utf-8")).hexdigest(),
             "bytes": len(f12_text.encode("utf-8"))}),
        "totals": {
            "m7_bucket": M7_BUCKET,
            "m7_queries": len(m7_queries()),
            "m7_queries_answered_by_the_branch": sum(
                1 for e in rows_with_m7[M7_BUCKET] if e["branch"] == "M7-bare-location"),
            "m7_rows": sum(len(e["rows"]) for e in rows_with_m7[M7_BUCKET]),
            "old_queries_touched": len(touched),
            "controls_outside_the_buckets_touched": len(controls),
        },
        "stop_conditions": {
            "old_queries_touched": touched,
            "missing": m7_missing,
            "extra": [e for e in m7_extra if e["bucket"] != M7_BUCKET],
            "unsigned": (u"да — списъкът на задействащите думи е "
                         u"scratch/places_search/m7_trigger_tokens.json и също чака подпис"),
        },
        "controls_outside_the_buckets": controls,
        "gate_m7_bare": [{"q": e["q"], "branch": e["branch"], "hasKey": e["hasKey"],
                          "n": e["n"],
                          "rows": full_side({"branch": e["branch"], "hasKey": e["hasKey"],
                                             "rows": e["rows"]})["rows"]}
                         for e in rows_with_m7[M7_BUCKET]],
        "moved": m7_moved,
    }

    out_dir = pathlib.Path(REPO_ROOT) / "scratch" / "places_search"
    written = []
    for name, doc in ((u"lot1v_v_manifest_BASE_P7.json", base_p7),
                      (u"lot1v_v_manifest_P7_F12.json", p7_f12)):
        path = out_dir / name
        path.write_text(dump(doc), encoding="utf-8", newline="\n")
        written.append(str(path))
    return written


def main():
    """§11 Р9 / C14 finding 3 — everything that RUNS lives here.

    Importing this module builds the primitives, the tokenizer, the deliveries,
    the index and search() and writes NOT ONE BYTE to disk; the report, the
    counterfactuals and the three output files are produced only by
    `python recall_sweep.py [plan|poi]`. Returns 1 if any expectation failed
    (§11 Р7), else 0.
    """
    set_capmode(sys.argv)
    set_fix(BASE)
    classes, fails, notin8 = sweep_recall()
    coll_rows = sweep_coll()
    M5 = evaluate(M5SPEC)
    EXTRA = evaluate(EXTRASPEC)

    # what П1 does to the two A8 counts that were measured under the v2 cap
    P1_COUNTS = []
    for _lbl, _cfg in [(u"v2.2 (без П1)", dict(BASE)),
                       (u"с П1", dict(BASE, P1=True))]:
        set_fix(_cfg)
        _row = [_lbl]
        for _q in [u"парк", u"берлин голдън бийч", u"хотел амирал", u"хотел адмиралл",
                   u"русалка", u"роял"]:
            _r, _b = search(_q)
            _ex = sum(1 for x in _r if any(t.s in x.nset for t in place_tokens(_q)))
            _row.append((_q, len(_r), _ex))
        P1_COUNTS.append(_row)
    set_fix(BASE)
    VAR_ROWS = []
    for vname, cfg in VARIANTS:
        set_fix(cfg)
        m5 = evaluate(M5SPEC)
        ex = evaluate(EXTRASPEC)
        cl, fl, n8 = sweep_recall()
        VAR_ROWS.append((vname, m5, ex, cl, fl,
                         [x[0] for x in m5 if not x[5]] + [x[0] for x in ex if not x[5]]))
    set_fix(BASE)

    # =============================================================== the report
    L = []
    w = L.append
    w(u"# Recall-прогон v2.2 · 226-те хотела · А1–А8 + подписаните П2+П3+П4+П5")
    w(u"")
    w(u"Скрипт: `measures/recall_sweep_v22.py` — копие на `recall_sweep_v21.py` с "
      u"включени **П2** (покритие на името преди близостта), **П3** (числов токен без "
      u"точно съвпадение отхвърля записа), **П4** (дума от речника с празен клас = "
      u"именен токен И филтър) и **П5 включена** (без ключ 2-знакова дума е значеща "
      u"при точно съвпадение с едно-токенно име → `йо` → хотел Йо), **без П1**; "
      u"редът „парк“ на А8 е поправен като ФАКТ: 19 реда — първите 12 с точно „ПАРК“, "
      u"после 7-те размити. Само четене. "
      u"Кадастрални идентификатори не се четат и не се изписват.")
    w(u"**П5 включена (подписана 02.09).** Единствената ѝ следа в резултатите е редът "
      u"`йо` в допълнителните проверки (10-та заявка, добавена тази нощ): 0 реда → "
      u"**Йо**. Всичко останало е байт-същото — А1/А2 се вдигат от 225/226 на "
      u"**226/226**, гейтът на §10 е затворен и по двете си половини.")
    w(u"Еталонът за JS-а ред по ред: `measures/recall_sweep_v22_rows.json` "
      u"(пълните списъци име · зона за 36-те гейт-заявки и 9-те допълнителни).")
    w(u"Данни: `varna_3d/data/fire_varna_hotels.json` (%d записа) · "
      u"`varna_3d/data/place_categories.json` (%d форми, %d чипа с `head`)."
      % (len(RECS), len(cats["forms"]), len(cats["chips"])))
    w(u"Център за М1/А3 (`map.getCenter()` няма в безглав прогон): "
      u"**43.2141, 27.9147** — началният `setView` на `Fire_Varna/index.html:1838`.")
    w(u"")
    w(u"## 0 · Санитарна проверка на токенизатора (G12б)")
    w(u"")
    w(u"| вход | placeTokens | очаквано | |")
    w(u"|---|---|---|---|")
    for src, exp in G12B:
        got = " ".join(t.s for t in place_tokens(src))
        w(u"| `%s` | `%s` | `%s` | %s |" % (src, got, exp, u"ДА" if got == exp else u"**НЕ**"))
    w(u"")
    w(u"### 0б · Населените класове (А1) и обхватът им (А2)")
    w(u"")
    w(u"| форма | ключ | клас (записи) | по (а) чип | по (б) К2б | по (в) А2 head |")
    w(u"|---|---|---|---|---|---|")
    for form in [u"хотел", u"хотели", u"хотелите", u"хотелът", u"хотела",
                 u"семеен хотел", u"апарт-хотел", u"комплекс", u"аквапарк",
                 u"градина", u"галерия", u"клуб", u"парк"]:
        fk = key_of(form)
        if fk not in FORM_IDX:
            w(u"| `%s` | — | (не е форма в речника) | | | |" % form)
            continue
        e = FORM_IDX[fk]
        a = [r for r in RECS if r.kkey in e["chips"]]
        parts = fk.split(" ")
        b = [r for r in RECS if r not in a and len(parts) == 1 and parts[0] in r.ktk]
        c3 = [r for r in CLASS_OF[fk] if r not in a and r not in b]
        n = len(CLASS_OF[fk])
        w(u"| `%s` | `%s` | %s | %d | %d | %d |"
          % (form, fk, (u"**%d**" % n) if n else u"0 → **не е ключ (А1)**",
             len(a), len(b), len(c3)))
    w(u"")
    kinds = {}
    for r in RECS:
        kinds[r.kind] = kinds.get(r.kind, 0) + 1
    w(u"Видове в доставката: " + u" · ".join(u"%s %d" % (k, v) for k, v in
                                              sorted(kinds.items(), key=lambda x: -x[1])))
    w(u"")
    w(u"## а · Recall по клас заявки (226 записа)")
    w(u"")
    w(u"| клас заявки | заявки | намерен | %% | в първите 8 | %% |")
    w(u"|---|---|---|---|---|---|")
    recall_line = {}
    for k in CLS_ORDER:
        v = classes[k]
        n = len(v)
        found = sum(1 for _, _, rk, _, _ in v if rk >= 0)
        top8 = sum(1 for _, _, rk, _, _ in v if 0 <= rk < TOP)
        recall_line[k] = (n, found, top8)
        w(u"| %s | %d | %d | %.1f | %d | %.1f |"
          % (k, n, found, 100.0 * found / n if n else 0.0, top8,
             100.0 * top8 / n if n else 0.0))
    w(u"")
    for k in CLS_ORDER:
        w(u"### %s" % k)
        w(u"")
        if not fails[k]:
            w(u"Ненамерени: **0**.")
        else:
            w(u"Ненамерени (**%d**):" % len(fails[k]))
            w(u"")
            w(u"| запис | зона | заявка | редове | клон |")
            w(u"|---|---|---|---|---|")
            for rec, q, n, br in fails[k]:
                w(u"| %s | %s | `%s` | %d | %s |" % (rec.name, rec.zone, q, n, br))
        w(u"")
        if notin8[k]:
            w(u"Намерени, но извън първите 8 (**%d**):" % len(notin8[k]))
            w(u"")
            w(u"| запис | зона | заявка | позиция | редове | клон |")
            w(u"|---|---|---|---|---|---|")
            for rec, q, rk, n, br in notin8[k]:
                w(u"| %s | %s | `%s` | %d | %d | %s |" % (rec.name, rec.zone, q, rk + 1, n, br))
        else:
            w(u"Извън първите 8: **0**.")
        w(u"")
    w(u"## б · Таблица на колизиите")
    w(u"")
    w(u"| заявка | редове | клон | първите 3 (име · зона) |")
    w(u"|---|---|---|---|")
    for q, n, br, top3 in coll_rows:
        w(u"| `%s` | %d | %s | %s |" % (q, n, br, rows_label(top3, 3)))
    w(u"")
    w(u"## в · Срещу М5 по А8")
    w(u"")
    w(u"| заявка | очаквано (М5 по А8) | измерено | клон | първите 3 | съвпада |")
    w(u"|---|---|---|---|---|---|")
    for q, exp, n, br, lab, ok in M5:
        w(u"| `%s` | %s | %d реда | %s | %s | %s |"
          % (q, exp, n, br, lab, u"ДА" if ok else u"**НЕ**"))
    w(u"")
    bad = [x for x in M5 if not x[5]]
    w(u"**Разминавания с М5 по А8: %d от %d.**" % (len(bad), len(M5)))
    w(u"")
    for q, exp, n, br, lab, ok in bad:
        why, fix = MISS_WHY.get(q, (u"(без анализ)", u"(без предложение)"))
        w(u"- **`%s`** — очаквано: %s · измерено: %d реда (%s) · %s" % (q, exp, n, br, lab))
        w(u"  - *правило-причина:* %s" % why)
        w(u"  - *най-малката поправка на правилото:* %s" % fix)
    w(u"")
    w(u"### в2 · Допълнителните проверки от промпта")
    w(u"")
    w(u"| заявка | очаквано | измерено | клон | първите 3 | съвпада |")
    w(u"|---|---|---|---|---|---|")
    for q, exp, n, br, lab, ok in EXTRA:
        w(u"| `%s` | %s | %d реда | %s | %s | %s |"
          % (q, exp, n, br, lab, u"ДА" if ok else u"**НЕ**"))
    w(u"")
    badx = [x for x in EXTRA if not x[5]]
    w(u"**Разминавания в допълнителните проверки: %d от %d.**" % (len(badx), len(EXTRA)))
    w(u"")
    w(u"### в3 · Кой ред е най-близък до центъра (43.2141, 27.9147)")
    w(u"")
    _adm, _ = search(u"хотел адмирал")
    w(u"| # | име | зона | статус | разстояние |")
    w(u"|---|---|---|---|---|")
    for i, r in enumerate(_adm):
        w(u"| %d | %s | %s | %s | %.0f м |" % (i + 1, r.name, r.zone, r.status or u"—", r.dist))
    w(u"")
    _royal, _ = search(u"роял")
    w(u"`роял` (пълен ред):")
    w(u"")
    w(u"| # | име | зона | качество | разстояние |")
    w(u"|---|---|---|---|---|")
    for i, r in enumerate(_royal):
        bnk, nm, tot, ssum, qual, unc = score(r, place_tokens(u"роял"), False)
        w(u"| %d | %s | %s | k%d | %.0f м |" % (i + 1, r.name, r.zone, bnk, r.dist))
    w(u"")
    _park, _ = search(u"парк")
    w(u"`парк` — кои редове НЕ са точни:")
    w(u"")
    w(u"| # | име | зона | качество |")
    w(u"|---|---|---|---|")
    for i, r in enumerate(_park):
        if u"park" not in r.nset:
            bnk, nm, tot, ssum, qual, unc = score(r, place_tokens(u"парк"), False)
            w(u"| %d | %s | %s | k%d (размито) |" % (i + 1, r.name, r.zone, bnk))
    w(u"")
    w(u"### в4 · Контрафакт: кандидат-поправките НА ПРАВИЛОТО (мерени, не приети наслуки)")
    w(u"")
    w(u"| вариант | М5/А8 | доп. | A1 recall | A3 recall | остатъчни разминавания |")
    w(u"|---|---|---|---|---|---|")
    for vname, m5, ex, cl, fl, miss in VAR_ROWS:
        a1 = cl[CLS_ORDER[0]]
        a3 = cl[CLS_ORDER[2]]
        f1 = sum(1 for _, _, rk, _, _ in a1 if rk >= 0)
        f3 = sum(1 for _, _, rk, _, _ in a3 if rk >= 0)
        w(u"| %s | %d/%d | %d/%d | %d/%d | %d/%d | %s |"
          % (vname, sum(1 for x in m5 if x[5]), len(m5),
             sum(1 for x in ex if x[5]), len(ex),
             f1, len(a1), f3, len(a3),
             u", ".join(u"`%s`" % q for q in miss) or u"—"))
    w(u"")
    w(u"Легенда на поправките (всяка е ЕДНО изречение върху едно правило):")
    w(u"")
    w(u"- **П1 (над А5/М2):** размитото съвпадение (Левенщайн ≤2) важи от **6 оригинални "
      u"знака** нагоре; при 4–5 знака — точно, префиксно и Левенщайн ≤1.")
    w(u"- **П2 (над А7):** между „действащ преди бивш“ и „разстояние до центъра“ се "
      u"вмъква **покритие на името ↑** (брой НЕсъвпаднали собствени именни токени).")
    w(u"- **П3 (над А5):** чисто числов токен, който **не съвпада точно** с токен на "
      u"записа, отхвърля записа (числата са конюнктивни, не по избор).")
    w(u"- **П4 (над А1):** дума от речника, чийто клас е **празен**, остава именен токен, "
      u"но е и **филтър**: ред без ТОЧНО съвпадение по име/псевдоним за нея отпада "
      u"(размитото съвпадение `болница`~БОНИТА не е доказателство, че думата я има).")
    w(u"- **П5 (над А5, ПОДПИСАНА 02.09):** без ключ дума от 2 знака е значеща само при "
      u"ТОЧНО съвпадение със запис, чието цяло име е този единствен токен → затваря "
      u"`йо` и вдига А1/А2 на **226/226** (гейтът на §10). Нула други промени: "
      u"префиксните 2-знакови съвпадения НЕ квалифицират.")
    w(u"")
    w(u"Цената на П1 (двете числа на А8 са мерени при стария cap):")
    w(u"")
    w(u"| заявка | без П1: редове (от тях точни) | с П1: редове (от тях точни) |")
    w(u"|---|---|---|")
    for _i in range(len(P1_COUNTS[0]) - 1):
        _q, _n0, _e0 = P1_COUNTS[0][_i + 1]
        _q2, _n1, _e1 = P1_COUNTS[1][_i + 1]
        w(u"| `%s` | %d (%d) | %d (%d) |" % (_q, _n0, _e0, _n1, _e1))
    w(u"")
    w(u"**Присъда на прогона.** Подписаният набор **П2+П3+П4+П5** затваря и петте "
      u"разминавания на v2.1 И дупката `йо`; редът „парк“ на А8 е поправен като факт "
      u"(12 точни, после 7 размити = 19), а П1 остава ОТХВЪРЛЕН, защото щеше да смени "
      u"и второто измерено число на А8 (`берлин голдън бийч` 16→14). "
      u"**Гейтът на §10 е затворен: 0 разминавания с М5 по А8 (36/36) и 226/226 за "
      u"А1/А2**, плюс 10/10 на допълнителните проверки.")
    w(u"")
    w(u"## г · Разликите v2 → v2.2 в правилата, които се наложиха")
    w(u"")
    for ln in DIFF_G:
        w(ln)
    w(u"")

    # ------------------------------------------------- the row-by-row JS baseline
    set_fix(BASE)
    ROWS = reference_rows()
    # ADR 008 D7: an artefact whose buckets are not exactly REF_BUCKETS is a
    # DIFFERENT reference — it is never written, however green the rows are.
    # ЛОТ 1в-В: the pending bucket is allowed in the report-only CANDIDATE and
    # nowhere else, so `--freeze` still refuses it until all three sides name it.
    _drift = bucket_drift(ROWS, pending=() if FREEZE else (PENDING_BUCKET, M7_BUCKET))
    if _drift:
        raise SystemExit(u"REF_BUCKETS (ADR 008 D7): " + u", ".join(_drift))
    pathlib.Path(OUTDIR).mkdir(parents=True, exist_ok=True)
    ROWS_OUT = OUTDIR + ("recall_sweep_v22_rows.json" if FREEZE
                         else "lot1v_v_candidate_rows.json")
    _rows_text = json.dumps(ROWS, ensure_ascii=False, indent=1, sort_keys=False) + chr(10)
    open(ROWS_OUT, "w", encoding="utf-8").write(_rows_text)
    if FREEZE:
        # The reference the JS is gated against lives next to the probe that replays
        # it (scratch/places_search/recall_sweep_rows.json) - one file, one generator.
        open(REPO_ROWS_OUT, "w", encoding="utf-8").write(_rows_text)
        print(u"FREEZE: замразена референция -> %s" % REPO_ROWS_OUT)
    else:
        _manifest_out = write_manifest(ROWS, ROWS_OUT, _rows_text)
        print(u"REPORT-ONLY (ЛОТ 1в-В): кандидат -> %s" % ROWS_OUT)
        print(u"REPORT-ONLY: манифест old → new -> %s" % _manifest_out)
        print(u"REPORT-ONLY: замразената референция НЕ е пипана (%s)" % REPO_ROWS_OUT)

    # С6′ — the parity corpus: every KEPT alias of the 28 zones and the name of
    # every one of the 361 records, with this tokeniser's answer. The probe runs
    # placeTokens (JS, in the page) over exactly these strings and compares
    # {s, orig, num} one by one; „1:1“ is a claim only while it is measured.
    _corpus = []
    for _z in sorted((cats.get("zones") or {}).keys()):
        for _a in ((cats["zones"][_z].get("aliases")) or []):
            if _a not in _corpus:
                _corpus.append(_a)
    _n_aliases = len(_corpus)
    for _r in RECS:
        if _r.name not in _corpus:
            _corpus.append(_r.name)
    _n_names = len(_corpus) - _n_aliases
    # ЛОТ 1в D1/D2: an alias is a searchable STRING now (EXACT_ALIAS keys the
    # whole phrase), so the two tokenisers have to agree on it as well.
    for _r in RECS:
        for _o in _r.old_names:
            if _o not in _corpus:
                _corpus.append(_o)
    _n_old = len(_corpus) - _n_aliases - _n_names
    # ЛОТ 1в-Б D6: `street_phrase` and `house_key` are searchable STRINGS now —
    # both tokenisers have to agree on them too, or the A3-street branch would
    # index one thing in Python and another in the page.
    for _r in RECS:
        if not _r.address:
            continue
        for _s in (_r.address["street_phrase"], _r.address["house_key"]):
            if _s not in _corpus:
                _corpus.append(_s)
    _n_addr = len(_corpus) - _n_aliases - _n_names - _n_old
    # ЛОТ 1в-В (С6′ по трите полета): the canonical name and every alias of every
    # quarter, district and locality, plus the old zone words that live on the rows.
    # All of them are searchable STRINGS now — three separate token sets and a
    # per-row legacy index — so the two tokenisers have to agree on them as well.
    for _cls in LOC_CLASSES:
        for _code in sorted(LOCATIONS[_cls]):
            _e = LOCATIONS[_cls][_code]
            for _s in [_e["name"]] + list(_e["aliases"]):
                if _s not in _corpus:
                    _corpus.append(_s)
    _n_loc = len(_corpus) - _n_aliases - _n_names - _n_old - _n_addr
    for _r in RECS:
        for _s in _r.legacy:
            if _s not in _corpus:
                _corpus.append(_s)
    _n_legacy = len(_corpus) - _n_aliases - _n_names - _n_old - _n_addr - _n_loc
    _parity = {
        "_meta": {
            "source": "scratch/places_search/recall_sweep.py (place_tokens)",
            "what": "С6′ tokeniser parity corpus: kept zone aliases + record names",
            "aliases": _n_aliases,
            "zones_with_aliases": len(cats.get("zones") or {}),
            "records": len(RECS),
            "names": _n_names,
            "old_names": _n_old,
            "addresses": _n_addr,
            "locations": _n_loc,
            "legacy_terms": _n_legacy,
            "strings": len(_corpus),
        },
        "strings": [{"s": _x,
                     "tokens": [{"s": _t.s, "orig": _t.orig, "num": bool(_t.num)}
                                for _t in place_tokens(_x)]}
                    for _x in _corpus],
    }
    open(REPO_PARITY_OUT, "w", encoding="utf-8").write(
        json.dumps(_parity, ensure_ascii=False, indent=1, sort_keys=False) + chr(10))

    OUT = OUTDIR + ("recall_sweep_v22.md" if CAPMODE == "plan"
                    else "recall_sweep_v22_cap_poi.md")
    open(OUT, "w", encoding="utf-8").write(u"\n".join(L) + u"\n")
    if MANIFEST:
        for _path in write_two_manifests(ROWS):
            print(u"манифест -> %s" % _path)
    print(u"CAPMODE=%s -> %s" % (CAPMODE, OUT))
    print(u"rows -> %s (%d + %d заявки, %d реда общо)"
          % (ROWS_OUT, len(ROWS["gate_m5_a8"]), len(ROWS["extra"]),
             sum(len(x["rows"]) for x in ROWS["gate_m5_a8"] + ROWS["extra"])))
    print(u"M5/A8: %d/%d съвпадат ; extra %d/%d"
          % (len(M5) - len(bad), len(M5), len(EXTRA) - len(badx), len(EXTRA)))
    for k in CLS_ORDER:
        n, found, top8 = recall_line[k]
        print(u"%-36s n=%3d found=%3d top8=%3d" % (k, n, found, top8))
    print(u"--- misses (M5/A8) ---")
    for q, exp, n, br, lab, ok in M5:
        if not ok:
            print(u"  %-32s %-22s %3d  %s" % (q, br, n, lab))
    print(u"--- misses (extra) ---")
    for q, exp, n, br, lab, ok in EXTRA:
        if not ok:
            print(u"  %-32s %-22s %3d  %s" % (q, br, n, lab))

    # П7 (§11 Р7): the gate that can FAIL. Nothing above this line ever could.
    p7_bad = check_p7_gate()
    print(u"П7: %d добавени токена в %d зони, %d/%d записа засегнати ; гейт %d/%d"
          % (sum(len(v) for v in P7_ADDED.values()), len(P7_ADDED),
             sum(1 for r in RECS if r.p7), len(RECS),
             len(P7_GAINS) + len(P7_CONTROLS) - len(p7_bad),
             len(P7_GAINS) + len(P7_CONTROLS)))
    print(u"П7 added: %s" % json.dumps(P7_ADDED, ensure_ascii=False, sort_keys=True))
    for line in p7_bad:
        print(u"  ЧЕРВЕНО: %s" % line)

    # ЛОТ 1 (решения 2 и 1): the second gate that can FAIL.
    lot1_bad = check_lot1_gate()
    print(u"ЛОТ 1: гейт %d/%d"
          % (len(LOT1_GAINS) + len(LOT1_CONTROLS) - len(lot1_bad),
             len(LOT1_GAINS) + len(LOT1_CONTROLS)))
    for line in lot1_bad:
        print(u"  ЧЕРВЕНО: %s" % line)

    # ЛОТ 1в-А (псевдоними с извор + курирани думи на видовете): the third gate.
    lot1v_bad = check_lot1v_a_gate()
    print(u"ЛОТ 1в-А: гейт %d/%d"
          % (len(LOT1V_A_GAINS) + len(LOT1V_A_CONTROLS) - len(lot1v_bad),
             len(LOT1V_A_GAINS) + len(LOT1V_A_CONTROLS)))
    for line in lot1v_bad:
        print(u"  ЧЕРВЕНО: %s" % line)

    # ЛОТ 1в-Б (адресите + клонът A3-street): the fourth gate that can FAIL.
    lot1v_b_bad = check_lot1v_b_gate()
    print(u"ЛОТ 1в-Б: гейт %d/%d"
          % (len(LOT1V_B_GAINS) + len(LOT1V_B_CONTROLS) - len(lot1v_b_bad),
             len(LOT1V_B_GAINS) + len(LOT1V_B_CONTROLS)))
    for line in lot1v_b_bad:
        print(u"  ЧЕРВЕНО: %s" % line)

    # ЛОТ 1в-В (типовите полета + деветте заявки): the fifth gate that can FAIL.
    lot1v_v_bad = check_lot1v_v_gate()
    print(u"ЛОТ 1в-В: гейт %d/%d ; квартал %d · допълнително %d · район %d/%d"
          % (len(LOT1V_V_GAINS) + len(LOT1V_V_CONTROLS) - len(lot1v_v_bad),
             len(LOT1V_V_GAINS) + len(LOT1V_V_CONTROLS),
             sum(1 for r in RECS if r.quarter), sum(1 for r in RECS if r.locality),
             sum(1 for r in RECS if r.district), len(RECS)))
    for line in lot1v_v_bad:
        print(u"  ЧЕРВЕНО: %s" % line)

    return 1 if (bad or badx or p7_bad or lot1_bad or lot1v_bad or lot1v_b_bad
                 or lot1v_v_bad) else 0


if __name__ == "__main__":
    sys.exit(main())
