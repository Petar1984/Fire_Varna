#!/usr/bin/env python3
"""Coverage delta per (file, field) between a base delivery and a candidate one.

Why this exists: лот 1в-В moved 103 hotels from a named resort to a bare
"район X" and nobody noticed until Petar opened the map. The tests could not
notice either — they assert the shape of a row, never the *coverage* of the
delivery as a whole. This gate compares two deliveries row by row and refuses
the candidate unless every lost or changed row is listed by name in a signed
allow-file.

Classes per (file, field):
  lost       a named value in the base became null / "район X" in the candidate
  changed    a named value became a *different* named value
  gained     a null in the base became a named value
  unchanged  the same named value on both sides
  reordered  the same ordinal carries a different name (the join broke)

Exit codes:
  0  no lost/changed rows, or every one of them is covered by the allow-file
  2  at least one lost/changed row is not covered by the allow-file
  3  the allow-file lists a row that is not lost/changed ("listed but unchanged")
  4  usage / input error
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

# The delivery has no place_id, so the join key is (file, name, ordinal): the
# position in the array. A different name at the same ordinal is not a join —
# it is a reorder, and it is counted separately instead of being compared.
FILES = ("places", "hotels")
ARRAY_KEY = {"places": "places", "hotels": "hotels"}

# The compat label: `zone` is a named zone unless it is the bare district word.
DISTRICT_MARK = "район "

FIELDS = ("zone_named", "quarter", "locality", "district")

EXIT_OK = 0
EXIT_UNCOVERED = 2
EXIT_ALLOW_STALE = 3
EXIT_USAGE = 4


def read_source(spec: str) -> str:
    """Read a delivery from the worktree or from git: `git:<rev>:<path>`."""
    if spec.startswith("git:"):
        rest = spec[len("git:"):]
        rev, _, path = rest.partition(":")
        if not rev or not path:
            raise ValueError("git spec must be git:<rev>:<path>, got %r" % spec)
        out = subprocess.run(
            ["git", "show", "%s:%s" % (rev, path)],
            capture_output=True,
        )
        if out.returncode != 0:
            raise ValueError(
                "git show %s:%s failed: %s" % (rev, path, out.stderr.decode("utf-8", "replace").strip())
            )
        return out.stdout.decode("utf-8")
    return Path(spec).read_text(encoding="utf-8")


def load_rows(spec: str, file_key: str) -> list:
    data = json.loads(read_source(spec))
    rows = data.get(ARRAY_KEY[file_key])
    if not isinstance(rows, list):
        raise ValueError("%s: no %r array" % (spec, ARRAY_KEY[file_key]))
    return rows


def field_value(row: dict, field: str):
    """The comparable value of a field, or None when the row carries nothing.

    A typed field is compared by its `code` (the closed-list identity), not by
    its printed name. `zone_named` is the compat label and counts only when it
    is a real zone name — "район Приморски" is the honest absence, not a value.
    """
    if field == "zone_named":
        zone = row.get("zone")
        if not isinstance(zone, str) or not zone or zone.startswith(DISTRICT_MARK):
            return None
        return zone
    value = row.get(field)
    if not isinstance(value, dict):
        return None
    code = value.get("code")
    return code if isinstance(code, str) and code else None


def row_src(row: dict) -> str:
    src = row.get("src")
    return src if isinstance(src, str) and src else "?"


def compare(base_rows: list, cand_rows: list, file_key: str) -> dict:
    """Row-by-row comparison of one delivery pair."""
    pairs = min(len(base_rows), len(cand_rows))
    reordered = []
    for i in range(pairs):
        if base_rows[i].get("name") != cand_rows[i].get("name"):
            reordered.append(
                {
                    "ordinal": i,
                    "base_name": base_rows[i].get("name"),
                    "candidate_name": cand_rows[i].get("name"),
                }
            )
    reordered_ordinals = {r["ordinal"] for r in reordered}

    fields = {}
    for field in FIELDS:
        counts = {
            "before": 0,
            "after": 0,
            "lost": 0,
            "changed": 0,
            "gained": 0,
            "unchanged": 0,
            "reordered": len(reordered),
        }
        lost_rows, changed_rows = [], []
        for i in range(pairs):
            before = field_value(base_rows[i], field)
            after = field_value(cand_rows[i], field)
            if before is not None:
                counts["before"] += 1
            if after is not None:
                counts["after"] += 1
            if i in reordered_ordinals:
                # The join broke here; comparing two different places would
                # invent a "loss" that never happened.
                continue
            if before is not None and after is None:
                counts["lost"] += 1
                lost_rows.append(
                    {
                        "file": file_key,
                        "name": cand_rows[i].get("name"),
                        "field": field,
                        "from": before,
                        "to": None,
                        "src": row_src(cand_rows[i]),
                        "ordinal": i,
                    }
                )
            elif before is not None and after is not None and before != after:
                counts["changed"] += 1
                changed_rows.append(
                    {
                        "file": file_key,
                        "name": cand_rows[i].get("name"),
                        "field": field,
                        "from": before,
                        "to": after,
                        "src": row_src(cand_rows[i]),
                        "ordinal": i,
                    }
                )
            elif before is None and after is not None:
                counts["gained"] += 1
            elif before is not None and after is not None:
                counts["unchanged"] += 1
        fields[field] = {"counts": counts, "lost_rows": lost_rows, "changed_rows": changed_rows}

    return {
        "rows_base": len(base_rows),
        "rows_candidate": len(cand_rows),
        "compared": pairs,
        "reordered_rows": reordered,
        "fields": fields,
    }


def load_allow(path: str | None) -> tuple[list, dict]:
    """Read the signed allow-file. Absent path = no allowance at all."""
    if not path:
        return [], {}
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    rows = data.get("rows")
    if not isinstance(rows, list):
        raise ValueError("%s: no `rows` array" % path)
    meta = {
        "path": path,
        "signed_by": data.get("signed_by"),
        "date": data.get("date"),
        "rows": len(rows),
    }
    return rows, meta


def allow_key(row: dict) -> tuple:
    return (row.get("file"), row.get("name"), row.get("field"), row.get("from"), row.get("to"))


def render_md(result: dict) -> str:
    out = ["# Покритие по (файл, поле) — гейт `gates/coverage.py`", ""]
    out.append("Base: `%s`" % result["base_spec_text"])
    out.append("")
    out.append("Candidate: `%s`" % result["candidate_spec_text"])
    out.append("")
    allow = result["allow"]
    if allow:
        out.append(
            "Allow-файл: `%s` · подписал: **%s** · дата: %s · редове: %d"
            % (allow.get("path"), allow.get("signed_by"), allow.get("date"), allow.get("rows"))
        )
    else:
        out.append("Allow-файл: няма")
    out.append("")
    out.append("| файл | поле | before | after | lost | changed | gained | unchanged | reordered |")
    out.append("|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for file_key in FILES:
        block = result["files"].get(file_key)
        if not block:
            continue
        for field in FIELDS:
            c = block["fields"][field]["counts"]
            out.append(
                "| %s | %s | %d | %d | %d | %d | %d | %d | %d |"
                % (
                    file_key,
                    field,
                    c["before"],
                    c["after"],
                    c["lost"],
                    c["changed"],
                    c["gained"],
                    c["unchanged"],
                    c["reordered"],
                )
            )
    for file_key in FILES:
        block = result["files"].get(file_key)
        if not block:
            continue
        for field in FIELDS:
            for kind, key in (("Загубени", "lost_rows"), ("Сменени", "changed_rows")):
                rows = block["fields"][field][key]
                if not rows:
                    continue
                out.append("")
                out.append("## %s · %s · %s (%d)" % (kind, file_key, field, len(rows)))
                out.append("")
                out.append("| # | име | преди | след | src | покрит от allow |")
                out.append("|---:|---|---|---|---|---|")
                for n, r in enumerate(rows, 1):
                    out.append(
                        "| %d | %s | %s | %s | %s | %s |"
                        % (
                            n,
                            r["name"],
                            r["from"],
                            "—" if r["to"] is None else r["to"],
                            r["src"],
                            "да" if r.get("allowed") else "НЕ",
                        )
                    )
    if result["allow_stale"]:
        out.append("")
        out.append("## Изброени в allow, но непроменени (грешка 3)")
        out.append("")
        for r in result["allow_stale"]:
            out.append("- %s · %s · %s: %s → %s" % (r.get("file"), r.get("name"), r.get("field"), r.get("from"), r.get("to")))
    out.append("")
    out.append("**Изход: %d** (%s)" % (result["exit_code"], result["verdict"]))
    out.append("")
    return "\n".join(out)


def run(
    places_base: str | None,
    places_candidate: str | None,
    hotels_base: str | None,
    hotels_candidate: str | None,
    allow_path: str | None,
    out_dir: str | None,
) -> dict:
    specs = {
        "places": (places_base, places_candidate),
        "hotels": (hotels_base, hotels_candidate),
    }
    files = {}
    for file_key in FILES:
        base_spec, cand_spec = specs[file_key]
        if not base_spec or not cand_spec:
            continue
        files[file_key] = compare(
            load_rows(base_spec, file_key), load_rows(cand_spec, file_key), file_key
        )
    if not files:
        raise ValueError("nothing to compare: give --places-base/--places-candidate and/or the hotels pair")

    allow_rows, allow_meta = load_allow(allow_path)
    allowed_keys = {}
    for r in allow_rows:
        allowed_keys.setdefault(allow_key(r), []).append(r)
    used_keys = set()

    uncovered = 0
    for file_key, block in files.items():
        for field in FIELDS:
            for key in ("lost_rows", "changed_rows"):
                for row in block["fields"][field][key]:
                    k = allow_key(row)
                    if k in allowed_keys:
                        row["allowed"] = True
                        used_keys.add(k)
                    else:
                        row["allowed"] = False
                        uncovered += 1

    # Сол S6: a row listed in the allow-file that did not actually move is a
    # stale signature — it must be removed, not carried forward silently.
    allow_stale = [r for k, rs in allowed_keys.items() if k not in used_keys for r in rs]

    if allow_stale:
        exit_code, verdict = EXIT_ALLOW_STALE, "allow-файл с изброен, но непроменен ред"
    elif uncovered:
        exit_code, verdict = EXIT_UNCOVERED, "%d непокрити загубени/сменени реда" % uncovered
    else:
        exit_code, verdict = EXIT_OK, "нула непокрити загубени/сменени реда"

    result = {
        "base_spec_text": "places=%s hotels=%s" % (places_base, hotels_base),
        "candidate_spec_text": "places=%s hotels=%s" % (places_candidate, hotels_candidate),
        "files": files,
        "allow": allow_meta,
        "allow_stale": allow_stale,
        "uncovered": uncovered,
        "exit_code": exit_code,
        "verdict": verdict,
    }

    if out_dir:
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "coverage.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (out / "coverage.md").write_text(render_md(result), encoding="utf-8", newline="\n")
    return result


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="coverage delta per (file, field)")
    ap.add_argument("--places-base")
    ap.add_argument("--places-candidate")
    ap.add_argument("--hotels-base")
    ap.add_argument("--hotels-candidate")
    ap.add_argument("--allow", help="gates/allow/<ГГГГ-ММ-ДД>_<тема>.json")
    ap.add_argument("--out", default="gates/out", help="output directory (default gates/out)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    try:
        result = run(
            args.places_base,
            args.places_candidate,
            args.hotels_base,
            args.hotels_candidate,
            args.allow,
            args.out,
        )
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        sys.stderr.write("coverage: %s\n" % exc)
        return EXIT_USAGE

    if not args.quiet:
        for file_key in FILES:
            block = result["files"].get(file_key)
            if not block:
                continue
            for field in FIELDS:
                c = block["fields"][field]["counts"]
                sys.stdout.write(
                    "%-7s %-10s before=%-4d after=%-4d lost=%-4d changed=%-4d gained=%-4d reordered=%d\n"
                    % (file_key, field, c["before"], c["after"], c["lost"], c["changed"], c["gained"], c["reordered"])
                )
        sys.stdout.write("uncovered=%d exit=%d (%s)\n" % (result["uncovered"], result["exit_code"], result["verdict"]))
    return result["exit_code"]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
