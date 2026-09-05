#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`gates.sign` — the one hand that turns „pending — Петър“ into „Петър“.

    python -m gates.sign <id> да|не [--all да|не] [--queue <path>]

План v2 §0.5: an executor writes `pending` and nothing else; the decision is
applied by THIS tool, run by Petar himself, and the commit that carries it is
his. The tool therefore does three things and refuses to do a fourth:

  1. it records the decision and the date on the queue row named by `<id>`;
  2. it writes the signature into the artefact that row governs — the allow
     file, the baseline manifest, `expectations.json`, the two report-only
     manifests, the лот-В manifest, the М7 trigger list;
  3. it PRINTS the `git commit` command for Petar.

It never commits: the commit is where the authorship lives (`run_gates`
проверка 7 reads it back with `git log -S`), and a commit made by a tool an
agent can run is a commit an agent can make. For the same reason the tool
refuses to run at all while the git identity of the checkout is an agent's.

`--all да|не` applies that decision to every row still `pending` AFTER the
named row is decided — план §A.3 R1: „подписва по клас, с възможност за
изключение по ред“. The exception is the positional pair, the class is `--all`.

It COMPUTES FIRST AND WRITES LAST (амандамент №5 т. 2): the queue is edited in
memory, every artefact body is prepared in a buffer, and the writes happen in
one block only after the last row is decided. A refusal on row 2 therefore
leaves row 1's artefact untouched — „НИЩО НЕ Е ЗАПИСАНО“ means zero changed
files, and `git status --porcelain` is what says so.

„не“ is TERMINAL (план v2 §0.6): a row that was refused is „отказано“ and this
tool will not re-decide it. A decided row is never silently overwritten either
— re-applying the same decision is a no-op, changing it is a refusal with the
words „ръчна редакция + нов кръг“.

A „не“ NAMES ITS QUERY (амандамент №6 т. 2): the pen refuses to write „не“ on a
row whose `покрива` carries `кофа/*`. A refusal over a whole bucket is a class
permission that happens to say no — it collides with every class „да“ over the
same bucket, and the collision is the thing that made the verdict depend on the
order of the file. The rule is enforced where the decision is written, so a
queue that reached the gate has already been through it.

AND THAT QUERY HAS TO EXIST (амандамент №7 т. 1): before it writes „не“ the pen
asks `gates.release.refusable_deltas()` for the deltas of the moment and refuses
a row that names none of them. `gate_lot1/Градината` instead of
`gate_lot1/градина` used to be a refusal about nothing: it matched no delta,
the gate stayed green over the difference Petar meant to refuse, and the freeze
carried it into the reference. The gate blocks such a row now; here it is never
written, and the answer comes back while the human is still at the keyboard.

THE QUESTION IS ASKED OF THE RAW `покрива` (амандамент №8 т. 1): every word of
it, per pattern, including the ones a machine cannot read as a query at all
(`gate_lot1градина`, no slash) and including none at all — an empty `покрива`
under a „не“ refuses nothing and is refused here.

AND THE ANCHOR IT WRITES IS PETAR'S COMMIT (амандамент №8 т. 4): the pen fills
`_meta.queue_reference` in as he signs, and it will not write a commit that is
not his — a signature that arrives with an anchor the gate blocks is a
signature that has to be undone by hand.

ONLY A DELTA ROW IS ASKED ABOUT QUERIES (амандамент №9 т. 5). The queue carries
three kinds of row: a „въпрос“ (no artefact, no `покрива` — Q7 „break-glass:
вън“), an „артефакт“ (a body to sign and no `покрива` — the baseline, the
codes) and a „делта“ (a `покрива` field). The refusal rules above are rules
about deltas; applied to the other two they made a political „не“ unwritable and
held the delivery over a row that was never about a query. „не“ on a question is
recorded and goes no further; „не“ on an artefact means the body is NOT signed,
and the release then blocks on the artefact.

AND IT WRITES DOWN WHAT IT SIGNED (амандамент №9 т. 7): `- **тяло:** <sha256>`
on the row, the digest of the artefact body without the signature field. Check 6
recompares that number with the blob at HEAD, so a rewrite that touches no
digest-bound field is caught by the release gate — and therefore by `--freeze`,
which reads the release verdict — instead of only by `run_gates` проверка 7.
"""

from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import re
import subprocess
import sys

from gates import coverage
from gates import release

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

SIGNER = u"Петър"
PENDING_SIGNATURE = u"pending — Петър"
HUMAN = release.HUMAN_AUTHOR
# The identities the agents commit with (амандамент №4 т. 6). The tool refuses
# to run under any of them: without this the barrier is only a habit.
AGENT_IDENTITIES = (u"Claude Executor", u"Claude Architect",
                    u"executor@local", u"architect@local")

YES, NO, PENDING = release.YES, release.NO, release.PENDING

EXIT_OK = 0
EXIT_REFUSED = 3
EXIT_USAGE = 4


def artefacts():
    """{name: path} — the signable bodies, straight from `gates.release`.

    ONE list: what the pen may sign is exactly what the gate reads back, and a
    name the gate does not know is refused here instead of producing a signature
    nobody checks."""
    return release.signable()


def repo_relative(path):
    """The path as the repository names it — for the `git add` line it prints.

    `release.repo_relative` is the one truth (the gate names the same paths in
    the same shape); a path outside the checkout is printed as it was given
    instead of raising, because this end of it is a line for a human to copy.
    """
    return release.repo_relative(path) or str(path)


def git_identity():
    """The name and e-mail git would put on a commit made right now."""
    out = subprocess.run(["git", "-C", str(REPO_ROOT), "var", "GIT_AUTHOR_IDENT"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        raise SystemExit(u"git не казва кой е авторът: %s"
                         % out.stderr.decode("utf-8", "replace").strip())
    ident = out.stdout.decode("utf-8", "replace").strip()
    match = re.match(r"^(.*?)\s*<([^>]*)>", ident)
    return (match.group(1), match.group(2)) if match else (ident, u"")


def refuse_if_agent():
    name, email = git_identity()
    for forbidden in AGENT_IDENTITIES:
        if forbidden in (name, email):
            raise SystemExit(
                u"ОТКАЗ: git авторът тук е „%s <%s>“ — подпис слага само Петър, "
                u"с ръката си (план v2 §0.5). Изпълнителите пишат само „%s“."
                % (name, email, PENDING_SIGNATURE))
    return name, email


def apply_signature(rel_path):
    """COMPUTE the signed body of one artefact — and write not one byte.

    Амандамент №5 т. 2: this used to write the file and let a later row refuse,
    after which the tool printed „НИЩО НЕ Е ЗАПИСАНО“ over a changed worktree.
    It now returns a buffer and `main` performs every write in one block, after
    the last decision is known: compute first, write last — the same rule
    `--freeze` follows.

    Returns `(complaint, text)`: a complaint means nothing may be written at
    all; `text is None` with no complaint means the artefact already carries the
    signature (idempotent).

    The edit is textual and byte-minimal on purpose. Re-dumping the JSON would
    rewrite bytes nobody decided to change, and the digest of a signed document
    is the thing every gate binds to."""
    path = REPO_ROOT / rel_path
    if not path.exists():
        return (u"липсва %s" % rel_path, None)
    text = path.read_text(encoding="utf-8")
    pending = u'"%s"' % PENDING_SIGNATURE
    signed = u'"%s"' % SIGNER
    if pending not in text:
        if signed in text:
            return (None, None)              # already signed — idempotent
        return (u"%s не носи %r — не пипам нищо" % (rel_path, PENDING_SIGNATURE), None)
    if text.count(pending) != 1:
        return (u"%s носи %d пъти %r — подписът е по един на артефакт"
                % (rel_path, text.count(pending), PENDING_SIGNATURE), None)
    return (None, text.replace(pending, signed))


def with_queue_anchor(rel_path, text):
    """(text, note, complaint) — the expectations body with a CURRENT queue anchor.

    Амандамент №7 т. 3: both writers of `_meta.queue_reference` name the same
    reference — `recall_sweep.build_expectations` when it measures the body and
    this tool when Petar signs one. Normally the generator has already written
    it and nothing moves: the edit of a signature stays the byte-minimal
    substitution it has always been. The field is rewritten here only when it is
    missing (a body measured before this rule) or stale (a freeze has been
    committed since), and then the note says so out loud, because the bytes of a
    signed document changed for a second reason.

    Only the expectations carry this anchor — the other artefacts are signed
    without touching a byte beyond the signature. A body that cannot get a valid
    anchor is not signed at all: the complaint travels with the refusals, which
    is what „нищо не е записано“ means here as everywhere else.

    AND THE ANCHOR HAS TO BE PETAR'S COMMIT (амандамент №8 т. 4). The gate
    already blocks a `_meta.queue_reference` whose commit belongs to somebody
    else (`release.queue_reference`); the pen refuses to WRITE one. Otherwise
    the signature and the refusal it protects would be born already broken —
    Petar signs, the gate blocks him for a field his own tool just filled in,
    and the only way out is a hand edit of a signed body. The freeze is
    committed by Petar (амандамент №6), so the carrier of the reference is his
    commit; when it is not, this is the round to say so.
    """
    if rel_path != release.EXPECTATIONS_REL:
        return (text, None, None)
    try:
        anchor = release.queue_reference_anchor()
    except (ValueError, OSError) as exc:
        return (text, None, u"котвата „_meta.%s“ не можа да се измери: %s"
                % (release.QUEUE_REFERENCE_KEY, exc))
    author = release.commit_author(anchor["commit"])
    if author != release.HUMAN_AUTHOR:
        return (text, None,
                u"котвата „_meta.%s“ би сочила комит %s на %r — референцията, "
                u"срещу която се пише опашката, стои в комит на %s "
                u"(замразяването го комитва Петър)"
                % (release.QUEUE_REFERENCE_KEY, anchor["commit"][:7],
                   author or u"—", release.HUMAN_AUTHOR))
    try:
        doc = json.loads(text)
    except ValueError as exc:
        return (text, None, u"%s не е валиден JSON: %s" % (rel_path, exc))
    meta = doc.get("_meta")
    if not isinstance(meta, dict):
        return (text, None,
                u"%s няма `_meta` — котвата няма къде да се запише" % rel_path)
    if meta.get(release.QUEUE_REFERENCE_KEY) == anchor:
        return (text, None, None)
    meta[release.QUEUE_REFERENCE_KEY] = anchor
    # The same dump the generator uses (`indent=1`, no ASCII escaping): the two
    # writers of this body have to produce one shape, or the diff of a signature
    # would be the whole file.
    return (json.dumps(doc, ensure_ascii=False, indent=1) + u"\n",
            u"котва „_meta.%s“ → %s (%s)" % (release.QUEUE_REFERENCE_KEY,
                                             anchor["commit"][:7], anchor["path"]),
            None)


def refusal_scope_complaint(row):
    """Why this row may not be answered „не“ — or None.

    Амандамент №6 т. 2: a refusal is a decision about a named query, so its
    `покрива` is `кофа/точната заявка`. `кофа/*` under a „не“ would refuse a
    whole bucket in one word, next to a „да“ that allows the same bucket by
    class — two rows about the same delta, disagreeing. `gates.release` reads
    such a queue fail-closed („не“ wins); here it is not written at all."""
    wide = release.wildcard_covers(row["covers"])
    if not wide:
        return None
    return (u"ред %s отказва с широк шаблон (%s) — „не“ носи ТОЧНАТА заявка "
            u"(`покрива: кофа/заявката`), не цяла кофа (амандамент №6 т. 2)"
            % (row["id"], u", ".join(wide)))


def refusal_target_complaint(row, deltas):
    """Why this „не“ names a query nobody delivered — or None.

    Амандамент №7 т. 1. `deltas` is the set of `(кофа, заявка)` pairs
    `gates.release` is judging right now; every `покрива` pattern of a refusal
    has to hit at least one of them, or the row is a decision about something
    that does not exist. The check is per PATTERN on purpose: a row that refuses
    three queries and misspells one of them is a row with a typo in it, and the
    two other refusals do not make the typo true.

    Амандамент №8 т. 1: the measurement is over the RAW `покрива`, through
    `release.patterns_that_cover` and `release.refusal_pattern_reason` — the two
    functions the gate itself uses. Filtering the patterns down to the readable
    ones first meant a pattern with no slash at all — `gate_lot1градина` —
    vanished before it was measured, and a row whose only content was that word
    was written as a refusal about nothing. An empty `покрива` under a „не“ is
    refused for the same reason: the pen writes refusals by name, and there is
    no name here.

    Only a DELTA row reaches this question (амандамент №9 т. 5); the caller
    decides the class, so a „не“ on Q7 is not measured against queries it was
    never about."""
    if not row["covers"]:
        return (u"ред %s отказва заявка, която не съществува: %s"
                % (row["id"], release.REFUSAL_EMPTY))
    hit = release.patterns_that_cover(row, deltas)
    missing = []
    for pattern in row["covers"]:
        reason = release.refusal_pattern_reason(pattern, hit)
        if reason:
            missing.append(u"%s (%s)" % (pattern, reason))
    if not missing:
        return None
    return (u"ред %s отказва заявка, която не съществува: %s — „не“ се пише по "
            u"ТОЧНАТА заявка от текущите делти на gates.release (амандамент №7 "
            u"т. 1, №8 т. 1); провери изписването с `python -m gates.release`"
            % (row["id"], u"; ".join(missing)))


def refusable_deltas_once(cache):
    """The delta set, measured at most once per run (the engine costs a second).

    Returns `(deltas, complaint)` and remembers both: a queue with five „не“
    rows asks the same question five times and gets the same answer, computed
    once, so the pen can never judge two rows against two different sets."""
    if "deltas" not in cache:
        cache["deltas"], cache["complaint"] = release.refusable_deltas()
    return cache["deltas"], cache["complaint"]


def decide_row(lines, row, decision, today, body_sha=None):
    """Rewrite `решение`, `дата` — and `тяло` — of one row, in place.

    Returns how many of the two REQUIRED fields it rewrote; the caller refuses a
    row that does not carry both. `body_sha` is the digest of the artefact body
    this signature is being given to (амандамент №9 т. 7): the field is replaced
    where the row already has it and inserted after the row's last field where it
    does not, in the bullet style that row is written in.

    The scan stops at the next heading: an inserted line has to land inside the
    row it belongs to, and a queue with two headings of one id is a queue this
    tool must not spread a decision across.
    """
    changed = 0
    inside = False
    last_field, body_at, style = None, None, u"- **%s:** %s"
    for i, line in enumerate(lines):
        head = release.QUEUE_HEAD.match(line)
        if head:
            if inside:
                break
            inside = head.group(1) == row["id"]
            continue
        if not inside:
            continue
        pair = release.QUEUE_KEY.match(line)
        if not pair:
            continue
        key = pair.group(1).strip()
        if last_field is None and u"**" not in line:
            style = u"- %s: %s"
        last_field = i
        if key == release.FIELD_DECISION:
            lines[i] = re.sub(r":(\*\*)?\s*.*$", lambda m: ":%s %s"
                              % (m.group(1) or "", decision), line)
            changed += 1
        elif key == release.FIELD_DATE:
            lines[i] = re.sub(r":(\*\*)?\s*.*$", lambda m: ":%s %s"
                              % (m.group(1) or "", today), line)
            changed += 1
        elif key == release.FIELD_BODY:
            body_at = i
    if body_sha:
        written = style % (release.FIELD_BODY, body_sha)
        if body_at is not None:
            lines[body_at] = written
        elif last_field is not None:
            lines.insert(last_field + 1, written)
    return changed


def duplicate_field_complaint(row):
    """Why this row may not be decided at all — or None (амандамент №9 т. 2).

    A field written twice is read by the parser as its last value and by the
    human as its first; the gate blocks such a row, and the pen will not put a
    decision into one either — `decide_row` would rewrite BOTH lines and the
    queue would then say something neither of them said."""
    doubled = [f for f in (row.get("duplicates") or []) if f in release.KNOWN_FIELDS]
    if not doubled:
        return None
    return (u"ред %s носи два пъти полето „%s“ — един ред, едно решение; "
            u"оправи опашката с ръка и пусни пак"
            % (row["id"], u"“, „".join(doubled)))


def main(argv):
    coverage.use_utf8_console()
    ap = argparse.ArgumentParser(
        description=u"Прилага решение „да/не“ върху ред от опашката и артефакта му")
    ap.add_argument("row_id", help=u"id на реда (R1, R2, Q7 …)")
    ap.add_argument("decision", help=u"да | не")
    ap.add_argument("--all", dest="all_decision",
                    help=u"да | не — същото решение върху всички ОСТАНАЛИ pending редове")
    ap.add_argument("--queue", help=u"scratch/places_search/ЗА_ПОДПИС_<дата>.md")
    args = ap.parse_args(argv)

    if args.decision not in (YES, NO):
        sys.stdout.write(u"решението е „да“ или „не“, не %r\n" % args.decision)
        return EXIT_USAGE
    if args.all_decision is not None and args.all_decision not in (YES, NO):
        sys.stdout.write(u"--all приема „да“ или „не“, не %r\n" % args.all_decision)
        return EXIT_USAGE

    name, email = refuse_if_agent()
    if name != HUMAN:
        sys.stdout.write(u"⚠ git авторът тук е „%s <%s>“, а подписът се пише от "
                         u"„%s“ — проверката на авторството (run_gates 7) ще го "
                         u"каже на пуша.\n" % (name, email, HUMAN))

    try:
        queue_path = release.find_queue(args.queue)
    except ValueError as exc:
        sys.stdout.write(u"%s\n" % exc)
        return EXIT_USAGE
    if queue_path is None or not queue_path.exists():
        sys.stdout.write(u"няма опашка %s/%s — няма какво да се подписва\n"
                         % (release.QUEUE_DIR, release.QUEUE_GLOB))
        return EXIT_USAGE

    rows = release.parse_queue(queue_path)
    by_id = dict((row["id"], row) for row in rows)
    if args.row_id not in by_id:
        sys.stdout.write(u"в %s няма ред %r (има: %s)\n"
                         % (queue_path.name, args.row_id, u", ".join(sorted(by_id))))
        return EXIT_USAGE

    plan = [(by_id[args.row_id], args.decision)]
    if args.all_decision:
        plan += [(row, args.all_decision) for row in rows
                 if row["id"] != args.row_id and row["decision"] == PENDING]

    today = datetime.date.today().isoformat()
    # The queue is edited IN MEMORY (`lines`) and the artefacts are computed
    # into `pending_writes`; not one byte reaches the disk before the loop is
    # over and `refusals` is empty (амандамент №5 т. 2).
    lines = queue_path.read_text(encoding="utf-8").splitlines()
    table = artefacts()
    touched, refusals, signed_files = [], [], []
    pending_writes = []
    delta_cache = {}
    anchor_notes = []
    for row, decision in plan:
        complaint = duplicate_field_complaint(row)
        if complaint:
            refusals.append(complaint)
            continue
        if row["decision"] == NO:
            refusals.append(u"ред %s е ОТКАЗАН на %s — „не“ е терминално "
                            u"(план v2 §0.6)" % (row["id"], row["date"] or u"—"))
            continue
        if row["decision"] == YES and decision != YES:
            refusals.append(u"ред %s вече е „да“ — смяна на решение става с ръчна "
                            u"редакция и нов кръг, не с този инструмент" % row["id"])
            continue
        if row["decision"] == decision:
            touched.append(u"ред %s вече е %r — нищо не се променя" % (row["id"], decision))
            continue
        kind = release.row_class(row)
        if decision == NO and kind == release.CLASS_DELTA:
            # The refusal rules of амандаменти 6–8 are rules about DELTAS
            # (амандамент №9 т. 5): a „не“ on a question or on an artefact
            # names no query and is not asked to.
            complaint = refusal_scope_complaint(row)
            if complaint:
                refusals.append(complaint)
                continue
            deltas, why_not = refusable_deltas_once(delta_cache)
            if why_not:
                # The live half of the set is still measured; the missing half
                # is said out loud, because a „не“ answered against half a
                # picture is a decision the human should see the shape of.
                sys.stdout.write(u"⚠ котвата на отказите: %s\n" % why_not)
            complaint = refusal_target_complaint(row, deltas)
            if complaint:
                refusals.append(complaint)
                continue

        # The artefact is prepared BEFORE the row is rewritten: the digest of
        # the body this signature is given to belongs on the row, and the row is
        # written once (амандамент №9 т. 7).
        target = row["artefact"] if decision == YES else u""
        body, note, body_sha = None, None, None
        if target:
            if target not in table:
                refusals.append(u"ред %s сочи непознат артефакт %r (познати: %s)"
                                % (row["id"], target, u", ".join(sorted(table))))
                continue
            complaint, body = apply_signature(table[target])
            if complaint:
                refusals.append(u"ред %s: %s" % (row["id"], complaint))
                continue
            if body is not None:
                body, note, anchor_complaint = with_queue_anchor(table[target], body)
                if anchor_complaint:
                    refusals.append(u"ред %s: %s" % (row["id"], anchor_complaint))
                    continue
            # `body is None` means the artefact already carries the signature;
            # the bytes on disk are then the body this row is about.
            source = body if body is not None else \
                (REPO_ROOT / table[target]).read_text(encoding="utf-8")
            try:
                body_sha = release.body_digest(source)
            except (ValueError, OSError) as exc:
                refusals.append(u"ред %s: тялото на %s не може да се смята — %s"
                                % (row["id"], table[target], exc))
                continue
        if decide_row(lines, row, decision, today, body_sha) < 2:
            refusals.append(u"ред %s: липсва „%s“ или „%s“ в тялото на реда"
                            % (row["id"], release.FIELD_DECISION, release.FIELD_DATE))
            continue
        touched.append(u"ред %s → %s (%s) · клас %s" % (row["id"], decision, today, kind))
        if not target:
            continue
        if body is not None:
            if note:
                anchor_notes.append(note)
            pending_writes.append((REPO_ROOT / table[target], body))
        if body_sha:
            touched.append(u"ред %s · тяло %s → %s"
                           % (row["id"], body_sha[:12], table[target]))
        signed_files.append(table[target])

    if refusals:
        for line in refusals:
            sys.stdout.write(u"✗ %s\n" % line)
        sys.stdout.write(u"НИЩО НЕ Е ЗАПИСАНО — нула променени файлове; "
                         u"оправи горното и пусни пак.\n")
        return EXIT_REFUSED

    # --- the writes, all of them, here and nowhere else ----------------------
    for path, body in pending_writes:
        path.write_text(body, encoding="utf-8", newline="\n")
    queue_path.write_text(u"\n".join(lines) + u"\n", encoding="utf-8", newline="\n")
    for line in touched:
        sys.stdout.write(u"✓ %s\n" % line)
    for rel in signed_files:
        sys.stdout.write(u"✓ подпис „%s“ → %s\n" % (SIGNER, rel))
    for note in anchor_notes:
        sys.stdout.write(u"✓ %s\n" % note)

    paths = [repo_relative(queue_path)] + signed_files
    sys.stdout.write(
        u"\nКомитът е ТВОЙ, Петре — този инструмент не комитва:\n\n"
        u"    git add %s\n"
        u"    git commit -m \"sign: %s %s (%s)\"\n\n"
        u"После: python -m gates.run_gates\n"
        % (u" ".join(paths), args.row_id, args.decision, today))
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
