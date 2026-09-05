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
HUMAN = u"Petar1984"
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

    `--queue` may be given relative to the current directory or absolute, so the
    path is resolved before it is compared with the root; a path outside the
    checkout is printed as it was given instead of raising.
    """
    try:
        return str(pathlib.Path(path).resolve().relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


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


def decide_row(lines, row, decision, today):
    """Rewrite the `решение` and `дата` fields of one row, in place."""
    changed = 0
    inside = False
    for i, line in enumerate(lines):
        head = release.QUEUE_HEAD.match(line)
        if head:
            inside = head.group(1) == row["id"]
            continue
        if not inside:
            continue
        pair = release.QUEUE_KEY.match(line)
        if not pair:
            continue
        key = pair.group(1).strip()
        if key == release.FIELD_DECISION:
            lines[i] = re.sub(r":(\*\*)?\s*.*$", lambda m: ":%s %s"
                              % (m.group(1) or "", decision), line)
            changed += 1
        elif key == release.FIELD_DATE:
            lines[i] = re.sub(r":(\*\*)?\s*.*$", lambda m: ":%s %s"
                              % (m.group(1) or "", today), line)
            changed += 1
    return changed


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
    for row, decision in plan:
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
        if decision == NO:
            complaint = refusal_scope_complaint(row)
            if complaint:
                refusals.append(complaint)
                continue
        if decide_row(lines, row, decision, today) < 2:
            refusals.append(u"ред %s: липсва „%s“ или „%s“ в тялото на реда"
                            % (row["id"], release.FIELD_DECISION, release.FIELD_DATE))
            continue
        touched.append(u"ред %s → %s (%s)" % (row["id"], decision, today))
        if decision != YES:
            continue
        target = row["artefact"]
        if not target:
            continue
        if target not in table:
            refusals.append(u"ред %s сочи непознат артефакт %r (познати: %s)"
                            % (row["id"], target, u", ".join(sorted(table))))
            continue
        complaint, body = apply_signature(table[target])
        if complaint:
            refusals.append(u"ред %s: %s" % (row["id"], complaint))
            continue
        if body is not None:
            pending_writes.append((REPO_ROOT / table[target], body))
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
