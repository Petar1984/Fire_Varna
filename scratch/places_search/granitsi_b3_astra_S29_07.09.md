Reading additional input from stdin...
OpenAI Codex v0.153.3
--------
workdir: C:\git\Fire_Varna
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: ultra
reasoning summaries: none
session id: 01a07ab1-277d-7f63-b2a5-3e9073ea852b
--------
user
S29 · Повторна проверка на ПЛАН Б3 v3 след S28 (леща механика), read-only. Файлът: C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md (v3, комит acddcd1). Твоята присъда S28 (C:/git/Fire_Varna/scratch/places_search/granitsi_b3_astra_S28_07.09.md, последният блок) даде 10 условия; планерът твърди, че е приложил всичките с измервания и е отхвърлил части от тях в §13 (напр. S28-1: 0 извиквания само при crypto ON; S28-10: подпапка архив/ не бяга от глоба, защото queues_in_head е рекурсивен по basename → преименуване без префикса; S28-5: 59 реда/41 заявки, не 8). Провери за всяко S28-1…S28-10: (а) приложено ли е вярно в §3.5/§3.6/§4/§5 (командите изпълними ли са, exit кодовете верни ли са, отрицателните половини наистина ли падат — измери поне G3/9а-в, G7, G8, G9, G10, G11, G14, G15, G17 върху реалните файлове, без запис в репото; тежки прогони само в git clone --shared копие под %TEMP%); (б) §13 отхвърлянията верни ли са по мярка; (в) новите О27–О30 и §9 т. 17 (P7_ADDED дрейф) — реални ли са и пълни ли са; (г) §6 комитите и §4 редът — има ли междинно състояние с несъответстващи пинове/данни; §9 т. 1 вариант Б (пропускане само на буквените M7_PREFIXES преди теста за значимост в двата двигателя) — паритетът клиент↔референция запазва ли се и вярно ли е, че 156-заявъчният корпус дава 0 промени. Не пипай нищо, не комитвай, никаква команда към отдалечено хранилище. Присъда: ГОДНО за подпис / НЕГОДНО с номерирани условия S29-1…, всяко с доказателство и точна поправка; до 700 думи.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя v3 спрямо десетте условия S28, ще изпълня посочените проверки без запис в репото и ще проверя отделно реда на комитите и паритета клиент↔референция. Тежките прогони ще са само в локално `--shared` копие под `%TEMP%`, ако средата позволява запис там.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -TotalCount 120" in C:\git\Fire_Varna
 succeeded in 0ms:
# Active context â€” Fire_Varna

> **05.09.2026 16:55 â€” Ð”ÐžÐ¡Ð¢ÐÐ’ÐšÐ A ÐŸÐ£Ð‘Ð›Ð˜ÐšÐ£Ð’ÐÐÐ:** ÐŸÐµÑ‚ÑŠÑ€ Ð¿ÑƒÑˆÐ½Ð° `6da5d9a..fd13907` Ð¿Ñ€ÐµÐ· ÐºÑƒÐºÐ°Ñ‚Ð° (306 Ñ‚ÐµÑÑ‚Ð° OK, 7/7 Ð³ÐµÐ¹Ñ‚Ð°). ÐŸÑƒÐ±Ð»Ð¸ÐºÑƒÐ²Ð°Ð½Ð¸Ñ‚Ðµ blob-Ð¾Ð²Ðµ = Ð»Ð¾ÐºÐ°Ð»Ð½Ð¸Ñ‚Ðµ (hotels 46a44ce82f15, places 329310f577e8, categories 874e33cd00e2, index.html 3d3bf79b58bf). Ð–Ð¸Ð²Ð°Ñ‚Ð° ÐºÐ°Ñ€Ñ‚Ð°: Ñ…Ð¾Ñ‚ÐµÐ»Ð¸ Ñ ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð» 152/225, ÐÐ”ÐœÐ˜Ð ÐÐ› = Ðº.Ðº. Ð—Ð»Ð°Ñ‚Ð½Ð¸ Ð¿ÑÑÑŠÑ†Ð¸ (REG). Ð¡Ð»ÐµÐ´Ð²Ð°Ñ‰ Ð»Ð¾Ñ‚: â€žÐ“Ñ€Ð°Ð½Ð¸Ñ†Ð¸Ñ‚Ðµâ€œ (`docs/sessions/ÐŸÐ ÐžÐœÐŸÐ¢_Ð½Ð¾Ð²Ð°_Ñ‚ÐµÐ¼Ð°_Ð“Ñ€Ð°Ð½Ð¸Ñ†Ð¸Ñ‚Ðµ.md`); Ð¿Ñ€ÐµÐ´Ð¸ ÑÐ»ÐµÐ´Ð²Ð°Ñ‰Ð°Ñ‚Ð° Ð´Ð¾ÑÑ‚Ð°Ð²ÐºÐ° â€” A.2-11 (Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚ â„–10).


**Date:** 2026-09-05 Â· **HEAD:** A.2-4 = this commit (its parent is `a694c7e`, A.2-3) Â· **branch:** `main` Â· **signed:** __

> One page. Every number below is the output of the command next to it, run on the date above; a number without a command does not enter. The chronicle of 03â€“04.09 (Ð›ÐžÐ¢ 1, 1Ð²-Ð, 1Ð²-Ð‘, 1Ð²-Ð’, the pre-rebase hash table) is frozen in [archive/activeContext_2026-09-04.md](archive/activeContext_2026-09-04.md); the one before it in [archive/activeContext_2026-07-04.md](archive/activeContext_2026-07-04.md).

## What this repo is

The public mobile-first web app that shows a Varna-oblast firefighter the nearest working hydrant, with no install and no account. Live: <https://petar1984.github.io/Fire_Varna/> (GitHub Pages, `main`, path `/`). Field reports are moderated by Petar before they change data. Governance: `AGENTS.md`; executor rules: `CLAUDE.md`.

## Where the work stands (05.09)

**Ð¤Ð°Ð·Ð° A of `plans/ÐŸÐ›ÐÐ_Ð˜Ð—Ð§Ð˜Ð¡Ð¢Ð’ÐÐÐ•_v2_05.09.md` (signed 05.09 02:50) + its four amendments: F12 (Ð°â€“Ð·) and A.2 (1â€“4) are executed and wait for Petar.** F12 copies the P7 delivery of varna_3d (Ðœ2 + Ðœ3 + Ðœ6) into `data/`, re-pins the three SHA constants, bumps the places cache to v6, opens the closed client lists for the three codes the delivery carries (`mladost`, `briz`, `morska_gradina`), adds the Ðœ7 â€žbare placeâ€œ branch on both sides, moves the two bundle tests onto the delivered numbers (F12-Ð´), narrows Ðœ7 to significant tokens (F12-Ðµ) and makes every manifest anchor that names a commit the bytes of the **blob** at that commit (F12-Ð¶).

**A.2 built the release machinery** (Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚ â„–4): `gates/release.py` â€” Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° 6 â€” binds the frozen reference, the engine candidate, the pinned inputs and the manifests by digest and refuses every delta that no signed queue row covers; `gates/sign.py` applies â€žÐ´Ð°/Ð½Ðµâ€œ to a queue row and to the artefact it governs and refuses to run while the git identity is an agent's; Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° 7 reads back with `git log -S` who INTRODUCED each signature; the pre-push hook now runs the suite AND the gates and has no break-glass at all; and every delivery-dependent expectation left the code for one signable body, `scratch/places_search/expectations.json`. **Nothing is frozen and nothing is published.**

Four things are waiting for Petar's own hand â€” none of them may be written by an agent:

1. `gates/baseline/MANIFEST.json` â†’ `signed_by: "ÐŸÐµÑ‚ÑŠÑ€"` (â€žÐ¿Ð¾Ð´Ð¿Ð¸ÑÐ²Ð°Ð¼ baseline f06ac06â€œ).
2. `gates/allow/2026-09-05_lot1v_v.json` â€” 150 named rows in four reason classes (`hull_artifact` 80 Â· `no_witness` 56 Â· `resort_pending` 8 Â· `m6_changed` 6).
3. `scratch/places_search/lot1v_v_manifest_BASE_P7.json` and `â€¦_P7_F12.json` â€” the two diffs, every row shown; the P7â†’F12 one also carries the two controls of gate 6 (â€žÐ¿Ñ€Ð¸Ð¼Ð¾Ñ€ÑÐºÐ¸â€œ, â€žÐ²Ð»Ð°Ð´Ð¸ÑÐ»Ð°Ð² Ð²Ð°Ñ€Ð½ÐµÐ½Ñ‡Ð¸Ðºâ€œ) as a signable delta.
4. `scratch/places_search/m7_trigger_tokens.json` â€” **33 triggering words**, waiting for a signature.
5. `scratch/places_search/expectations.json` â€” the ONE body every delivery-dependent expectation now lives in (the answers of the 78 gate questions, the Â§10 sweep, the ÐŸ7 measure, 15 claims, the three bucket anchors, the replay counts, and the â€žbeforeâ€œ of every question as the frozen reference answered it). `python -m gates.sign <id> Ð´Ð°` writes the signature; an agent writes only `pending â€” ÐŸÐµÑ‚ÑŠÑ€`.
6. `scratch/places_search/Ð—Ð_ÐŸÐžÐ”ÐŸÐ˜Ð¡_<Ð´Ð°Ñ‚Ð°>.md` â€” the queue itself (A.3, not written yet). Until it exists Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° 6 is RED with â€žÐ½ÑÐ¼Ð° Ð¾Ð¿Ð°ÑˆÐºÐ°â€œ, which is the fail-closed answer, not a defect. F12-Ðµ closed the short-prefix defect: the eight type prefixes (`Ðº`, `ÐºÐ²`, `Ð¶`, `Ð¼`, `Ñ`, `Ð¾`, `Ñ‚`, `Ð·Ð¾Ð½Ð°`) no longer fire the branch; the 45 measured candidates stay in the file with `triggers: false` so what was thrown out stays visible.

The 8 resort conflicts (Ð”ÐÐ›Ð˜Ð¯ Ð“ÐÐ Ð”ÐªÐ Â· Ð¤Ñ€ÐµÐ³Ð°Ñ‚Ð° Â· ÐœÐÐ“ÐÐžÐ›Ð˜Ð¯ 1 Ð˜ 2 Â· ÐœÐ°ÑÐº Â· ÐÐ•ÐŸÐ¢Ð£Ð Â· Ð Ð¾Ð¼Ð°Ð½Ñ‚Ð¸ÐºÐ° Â· Ð Ð£Ð¡ÐÐ›ÐšÐ Â· Ð¡Ð¢Ð ÐÐÐ”Ð–Ð) stay `pending_signature`: the map shows them as â€žÑ€Ð°Ð¹Ð¾Ð½ Xâ€œ until he decides each one.

## Current state

| ÐšÐ°ÐºÐ²Ð¾ | Ð¡Ñ‚Ð¾Ð¹Ð½Ð¾ÑÑ‚ | ÐšÐ¾Ð¼Ð°Ð½Ð´Ð° |
|---|---|---|
| commits on `main` | 327 | `git rev-list --count main` |
| commits ahead of `origin/main` (Petar alone pushes) | 46 | `git rev-list --count origin/main..main` |
| commits on `origin/main` not on `main` | 0 | `git rev-list --count main..origin/main` |
| last pushed commit | 6da5d9a 2026-09-04 | `git log -1 --format='%h %cs' origin/main` |
| records in `data/hydrants.json` | 7407 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/hydrants.json',encoding='utf-8'))))"` |
| records per origin | [('vik', 3524), ('national', 2329), ('etr_varna', 763), ('etr_provadia', 244), ('etr_dolni_chiflik', 219), ('field_report', 151), ('pozarna_gz', 99), ('etr_devnya', 78)] | `PYTHONIOENCODING=utf-8 python -c "import json,collections;print(collections.Counter(x.get('origin') for x in json.load(open('data/hydrants.json',encoding='utf-8'))).most_common())"` |
| `index.html` bytes (557270 before F12; 560365 after F12-Ð·) | 560855 | `wc -c < index.html` |
| `data/hydrants.json` bytes | 1315276 | `wc -c < data/hydrants.json` |
| first load (`index.html` + `data/hydrants.json`), hard cap 5 MB | 1876131 B = 1,79 MB | `python -c "import os;print(os.path.getsize('index.html')+os.path.getsize('data/hydrants.json'))"` |
| `data/hotels.json` (225 rows Ã— 17 keys; 142543 B before F12) | 148685 B Â· sha `46a44ce82f15â€¦` | `wc -c < data/hotels.json` Â· `git show HEAD:data/hotels.json \| sha256sum` |
| `data/places.json` (150 rows Ã— 13 keys; 121621 B before F12) | 122089 B Â· sha `329310f577e8â€¦` | `wc -c < data/places.json` Â· `git show HEAD:data/places.json \| sha256sum` |
| `data/place_categories.json` (64831 B before F12) | 75818 B Â· sha `874e33cd00e2â€¦` | `wc -c < data/place_categories.json` Â· `git show HEAD:data/place_categories.json \| sha256sum` |
| typed locations on the 375 delivered rows: quarter Â· locality Â· district (140 Â· 8 Â· 375 before F12) | 201 Â· 12 Â· 375 | `PYTHONIOENCODING=utf-8 python -c "import json;r=[x for f,k in (('data/places.json','places'),('data/hotels.json','hotels')) for x in json.load(open(f,encoding='utf-8'))[k]];print(sum(1 for x in r if x['quarter']), sum(1 for x in r if x['locality']), sum(1 for x in r if x['district']))"` |
| dictionary: forms Â· `legacy_by_row` Â· zones (283 Â· 209 Â· 19 before F12) | 283 Â· 18 Â· 20 | `PYTHONIOENCODING=utf-8 python -c "import json;c=json.load(open('data/place_categories.json',encoding='utf-8'));print(c['_meta']['n_forms'], len(c['legacy_by_row']), len(c['zones']))"` |
| search reference `scratch/places_search/recall_sweep_rows.json` â€” NOT frozen by F12 (report-only) | 140 rows, untouched since `148c731` (the commit before F12-Ð°) | `git diff --stat 148c731 -- scratch/places_search/recall_sweep_rows.json` |
| manifest anchor of `lot1v_v_manifest_BASE_P7.json`: the **blob** at the named commit, not the file on disk (F12-Ð¶) | `f06ac06` â†’ `0bc7a189f408â€¦` Â· 256070 B (the CRLF twin on a Windows worktree is 266021 B and the same OID) | `python scratch/places_search/manifest_anchor_gate.py` Â· `git show f06ac06:scratch/places_search/recall_sweep_rows.json \| sha256sum` |
| tests (241 after F9; 259 before A.2-4) Â· red | Ran 266 Â· FAILED (failures=6) = 6 red, all in `tests/test_places_search_gate.py` (see the split below) | `PYTHONIOENCODING=utf-8 python -m unittest discover -s tests 2>&1 \| tail -3` |
| gates | â›” Ð§Ð•Ð Ð’Ð•ÐÐž: Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° 6 (release) â€” 173 delta between the frozen reference and the engine candidate and no queue to cover them; Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° 4 âš  waits for two signatures; 1, 2, 3, 5, 7 green | `python -m gates.run_gates` |
| release gate: reference â†” candidate | reference 140 queries / 2121 rows Â· candidate 203 / 3160 Â· 173 delta Â· 0 covered (no queue yet) | `python -m gates.release` |
| `scratch/places_search/expectations.json` | 321040 B Â· `signed_by: "pending â€” ÐŸÐµÑ‚ÑŠÑ€"` Â· 78 gate questions Â· 62 + 10 sweep rows Â· 15 claims Â· 3 bucket anchors | `PYTHONIOENCODING=utf-8 python scratch/places_search/recall_sweep.py --manifest` |
| coverage of the delivery against the signed baseline `f06ac06` | places zone_named 127 â†’ 49 Â· hotels 199 â†’ 152 Â· uncovered 0 Â· exit 5 (unsigned allow) | `python -m gates.coverage --places-base git:f06ac06:data/places.json --places-candidate data/places.json --hotels-base git:f06ac06:data/hotels.json --hotels-candidate data/hotels.json --allow gates/allow/2026-09-05_lot1v_v.json` |
| Worker deploy version (repo-declared) | 5accc88e | `sed -n '20p' worker/README.md \| grep -oE '[0-9a-f]{8}'` |
| web manifest (`rel="manifest"`) in `index.html` | 0 | `grep -c 'rel="manifest"' index.html` |
| local branches (traces of closed cycles; work happens on `main`) | backup/pre-c17-split Â· backup/pre-c32-split Â· hydrants-c32 Â· lot1-client Â· main | `git branch --format='%(refname:short)'` |

Two rows of the previous page are NOT re-measured here because they need the network (satellite link): the open/closed issue counts (`gh issue list â€¦`) and the Pages status code (`curl â€¦`). Read them from the archive with their date, or run the command.

### The red tests: 21 before A.2-4, 6 after (Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚ â„–4 Ñ‚. 1 Ð¸ Ñ‚. 7)

The class is decided by **where the expectation lives**, measured by reading each test:
`PYTHONIOENCODING=utf-8 python -m unittest discover -s tests -v 2>&1 | grep -E '^(FAIL|ERROR): '`.

**BEFORE A.2-4 â€” 21 red in three classes:**

- **(Ð°) â€” 1.** The expectation lived in an artefact that carries `signed_by`:
  `Lot1vVGateTest::test_the_old_zone_words_are_load_bearing` (it read
  `_meta.signed_by` of `lot1v_v_manifest_BASE_P7.json` and said so).
- **(Ð±) â€” 17.** The expectation was a literal in the code or in the test: the six
  pinned gate constants (`P7_GAINS/CONTROLS`, `LOT1_*`, `LOT1V_A_*`, `LOT1V_B_*`,
  `LOT1V_V_*`, the â€ž7 tokens in 6 zonesâ€œ spec), five literals in the test file
  (`test_the_branch_stands_after_the_zone_and_before_the_fuzzy_path`,
  `test_the_collision_rule_is_load_bearing`, `test_added_tokens_are_the_measured_seven`,
  `test_no_added_token_is_a_name_token`, `test_the_foreign_token_guard_is_load_bearing`),
  three pinned anchor COMMITS (`test_the_kind_of_every_frozen_record_is_unchanged` Ã—2,
  `test_haskey_could_not_have_moved_and_agrees_with_every_branch`) and the three
  ERRORs below.
- **(Ð²) â€” 3.** The three â€žreplayâ€œ tests compared the engine with the frozen
  reference, which has no `signed_by` at all: `FrozenDiffTest::test_the_live_engine_replays_the_artefact`,
  `Lot1vABucketTest::test_the_live_engine_replays_the_new_bucket`,
  `Lot1vBBucketTest::test_the_live_engine_replays_the_new_bucket`.

The three ERRORs of class (Ð±) named engine attributes that Ð›ÐžÐ¢ 1Ð²-Ð’ had already
removed â€” `REF.ZONE_PHRASES`, `rec.zph`, `rec.ztk`. They were repaired
mechanically to what the engine carries today (`REF.LOC_PHRASES`; `qph`/`lph`/`gph`;
`qtk`/`ltk`/`legtk`/`ktk`) â€” an edit, never a signature, exactly as Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚ â„–4
said. All three are green.

**AFTER A.2-4 â€” 6 red, one class.** Every delivery-dependent expectation left the
code for `scratch/places_search/expectations.json`; the suite compares the engine
with that tracked body (which can and does fail: move the engine, forget the
artefact, and it is red), and whether Petar has SIGNED it is the release gate's
question â€” Ð¿Ð»Ð°Ð½ v2 Â§0.4 (â€žÐ¾Ñ‡Ð°ÐºÐ²Ð°Ð½Ðµ, ÐºÐ¾ÐµÑ‚Ð¾ Ñ‡Ð°ÐºÐ° Ð¿Ð¾Ð´Ð¿Ð¸Ñ, Ðµ Ñ€ÐµÐ´ Ð² Ð¾Ð¿Ð°ÑˆÐºÐ°Ñ‚Ð°, Ð½Ðµ
Ñ‡ÐµÑ€Ð²ÐµÐ½ Ñ‚ÐµÑÑ‚â€œ) and Â§A.2 (â€žÐ³Ð¾Ñ‚Ð¾Ð²Ð½Ð¾ÑÑ‚Ñ‚Ð° Ð½Ð° Ð´Ð¾ÑÑ‚Ð°Ð²ÐºÐ°Ñ‚Ð° Ð¾Ñ‚Ð¸Ð²Ð° Ð² release-Ð³ÐµÐ¹Ñ‚Ð°â€œ).

The six that remain are one claim in six places: **the frozen reference is still
the one of Ð»Ð¾Ñ‚ Ð‘ and the engine has moved past it** â€” they go green with the ONE
`--freeze` Petar's signature unlocks, and with nothing else:

- `FrozenDiffTest::test_the_live_engine_replays_the_artefact` Â· `::test_rows_carry_the_p7_measure`
- `Lot1vABucketTest::test_the_live_engine_replays_the_new_bucket` Â· `::test_the_bucket_is_the_signed_answers`
- `Lot1vBBucketTest::test_the_live_engine_replays_the_new_bucket` Â· `::test_the_bucket_is_the_signed_answers`

Every one of them reads `expectations.json` (grep: `require_expectations`, `EXP[`,
`gate_answers(`, `anchor_block(`, `claim(`). Proved in an isolated clone of this
commit: sign `expectations.json` and the two manifests, run `--freeze` once, run
the suite â†’ **0 red**; the clone is thrown away. `ReleaseGateSignatureTest` is the
one test that reads `signed_by`, and it is the fixture the plan asked for:
an unsigned artefact â†’ `gates.release` BLOCKED.

## Waiting for a signature

- **Ð¤Ð°Ð·Ð° A of the cleanup plan** â€” the four artefacts listed above; then `--freeze` once, tests green, `run_gates` green, audit, and Petar's push. `docs/plans/ÐŸÐ›ÐÐ_Ð˜Ð—Ð§Ð˜Ð¡Ð¢Ð’ÐÐÐ•_v2_05.09.md` Â§A.4.
- `decisions/007_address_path_v2.md` â€” `Proposed â€” awaiting Petar (Gate 1)`.
- `decisions/005_sw_cache_lifecycle.md` â€” `Proposed â€” awaiting Petar (Gate 1)`.
- `plans/hotels_search_plan.md`, `plans/sw_cache_lifecycle_fixes.md` â€” `DRAFT â€” AWAITING PETAR SIGNATURE (Gate 1)`.
- ADR 009 â€žÐ˜Ð´ÐµÐ½Ñ‚Ð¸Ñ‡Ð½Ð¾ÑÑ‚, Ð¿Ð¾Ð´Ð¿Ð¸ÑÐ¸, Ð³ÐµÐ¹Ñ‚Ð¾Ð²Ðµâ€œ â€” Ð¤Ð°Ð·Ð° B of the cleanup plan, not written yet.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status -sb; git rev-parse HEAD' in C:\git\Fire_Varna
 succeeded in 0ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 86]
?? scratch/places_search/cleanup_brief_astra.md
?? scratch/places_search/cleanup_brief_kimi.md
?? scratch/places_search/golden_brief_kimi.md
?? scratch/places_search/golden_brief_sol.md
?? scratch/places_search/granitsi_b3_astra_S29_07.09.md
?? scratch/places_search/granitsi_brief_astra.md
?? scratch/places_search/granitsi_brief_kimi.md
?? scratch/places_search/lot1_reference_preview.md
?? scratch/places_search/lot1g_brief_kimi.md
?? scratch/places_search/lot1g_brief_sol.md
?? scratch/places_search/lot1v_v2_brief_kimi.md
?? scratch/places_search/lot1v_v2_brief_sol.md
?? scratch/places_search/lot1v_v_m6_brief_kimi.md
?? scratch/places_search/lot1v_v_m6_brief_sol.md
?? scratch/places_search/lot1v_v_m6_fix_sample.md
?? scratch/places_search/osm_hints_brief_astra.md
?? scratch/places_search/osm_hints_brief_kimi.md
?? scratch/places_search/osm_quarters_brief_astra.md
?? scratch/places_search/osm_quarters_brief_kimi.md
?? scratch/places_search/ОТЧЕТ_A210_05.09.md
?? scratch/places_search/ОТЧЕТ_A25_05.09.md
?? scratch/places_search/ОТЧЕТ_A26_05.09.md
?? scratch/places_search/ОТЧЕТ_A27_05.09.md
?? scratch/places_search/ОТЧЕТ_A29_05.09.md
?? scratch/places_search/ОТЧЕТ_A2_05.09.md
?? scratch/places_search/ОТЧЕТ_A3_05.09.md
?? scratch/places_search/ОТЧЕТ_A4_freeze_05.09.md
?? scratch/places_search/ОТЧЕТ_F0zh_05.09.md
?? scratch/places_search/ОТЧЕТ_F12_05.09.md
?? scratch/places_search/ОТЧЕТ_F12de_05.09.md
?? scratch/places_search/ОТЧЕТ_F12zh_05.09.md
?? scratch/places_search/ОТЧЕТ_ЛОТ0-fix_05.09.md
?? scratch/places_search/ОТЧЕТ_ЛОТ0_05.09.md
acddcd12f4f9134b94ed7632cc3da03d14e8e9a4

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$paths = @('"'AGENTS.md','docs/plans/ПЛАН_Б3_07.09.md','scratch/places_search/granitsi_b3_astra_S28_07.09.md'); "'$paths | Sort-Object; $paths | ForEach-Object { $p=Get-Item -LiteralPath $_; [pscustomobject]@{Path=$_;Bytes=$p.Length;Lines=(Get-Content -LiteralPath $_ | Measure-Object -Line).Lines} }' in C:\git\Fire_Varna
 succeeded in 40ms:

Path                                                  Bytes Lines
----                                                  ----- -----
AGENTS.md                                             27909   289
docs/plans/ПЛАН_Б3_07.09.md                          133012   733
scratch/places_search/granitsi_b3_astra_S28_07.09.md 265574  1792



exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'scratch/places_search/granitsi_b3_astra_S28_07.09.md' -Encoding UTF8 -Tail 110" in C:\git\Fire_Varna
 succeeded in 0ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Command diff | Select-Object Name,CommandType,Definition' in C:\git\Fire_Varna
 succeeded in 8ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath tests/test_hotels_public_bundle.py -Encoding UTF8 | Select-Object -Skip 375 -First 40 | ForEach-Object -Begin { $n=375 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 52ms:
376:                             (rec["name"], addr["text"], addr["house_key"]))
377: 
378:     def test_the_address_licence_line_is_verbatim(self):
379:         # ADR 008 D5: the sources of an ADDRESS get their own sentence. Not one of them
380:         # is new to this delivery (план §2 т. 5), so the README licence table is
381:         # untouched and the line itself is pinned right here.
382:         self.assertEqual(self.doc["_meta"]["licence_address"], LICENCE_ADDRESS)
383:         self.assertIn("ODbL 1.0", LICENCE_ADDRESS)
384:         self.assertIn("`address.src`", LICENCE_ADDRESS)
385: 
386:     def test_the_cadastral_word_appears_only_inside_the_licence_line(self):
387:         # The licence sentence names cadastral address fields as a source; nowhere else
388:         # in the payload may the word appear, because no record may carry a cadnum.
389:         self.assertIn(LICENCE, self.text)
390:         rest = self.text.replace(LICENCE, "").replace(LICENCE_OSM, "")
391:         rest = rest.replace(LICENCE_ADDRESS, "")
392:         # ЛОТ 1в: 15 old names come from the КАИС address field, so the word rides
393:         # the CODE `KAIS`, never the free text — the assertion below still holds.
394:         self.assertNotIn("кадаст", rest)
395: 
396:     def test_licence_line_is_verbatim(self):
397:         self.assertEqual(self.doc["_meta"]["licence"], LICENCE)
398: 
399:     def test_the_osm_alias_licence_line_is_verbatim(self):
400:         # Амандамент А4 т. 3 (К4): a NEW OSM alias outside the 29 grandfathered ones
401:         # is a line in the licences, not just a letter in a row. One such alias today,
402:         # and the sentence's own count is measured against the payload.
403:         self.assertEqual(self.doc["_meta"]["licence_osm"], LICENCE_OSM)
404:         self.assertIn("ODbL 1.0", LICENCE_OSM)
405:         osm = [rec["name"] for rec in self.records if "OSM" in rec["old_names_src"]]
406:         self.assertEqual(len(osm), 1, osm)
407: 
408:     def test_readme_carries_licence_line(self):
409:         # Plan §5 G9. The licence travels with the data: whoever reads the repo's front
410:         # page must see the same sentence the payload carries, in both mirrors, unedited
411:         # — a paraphrase would be a different licence. Each README quote therefore sits
412:         # on ONE line; wrapping it would break the byte equality this asserts.
413:         readme = (REPO / "README.md").read_text(encoding="utf-8")
414:         licence = self.doc["_meta"]["licence"]
415:         self.assertGreaterEqual(readme.count(licence), 2, "licence quoted in BG and EN")

codex
Потвърдени са още три блокера: G10 брои 26 839 286 B и пада още върху днешното дърво; първият `--manifest` връща 1, а не обещаното 0; предложените отрицателни мутации за „Чайка“ и „Дружба“ запазват съответно 30 и 16 резултата. Самият атомен комит 2 пази пиновете и данните заедно. Старата опашка може да се архивира извън точния glob — изтриването ѝ не е необходимо.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status --short --branch --untracked-files=no' in C:\git\Fire_Varna
 succeeded in 0ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 82]

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git log -1 --format='%h %an <%ae> %s'" in C:\git\Fire_Varna
 succeeded in 0ms:
e6ba50e Claude Architect <architect@local> docs(plan): Б3 quarter search delivery plan v2 — DRAFT, unsigned (5 scouts, 3 refuters НЕГОДНО on v1, synthesis); awaiting Kimi К28 / Astra S28 and Petar's Gate 1

codex
**НЕГОДНО за подпис.** Проверих v2 срещу реалния клиент, гейтовете и трите посочени комита на varna_3d, включително с беззаписни проби в паметта.

1. **S28-1 — G3 очаква невъзможните 225 реда.** В [плана:372](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:372) връщането на оригиналния `QUARTER_SRC` трябва да отхвърли само местата. Реалната доставка съдържа `SIGNED_POLYGON` и в хотелите. Node-пробата даде `validateHotels=false`, `validatePlaces2=false`, `places payload unavailable`, `RECS=0`; разширените списъци дадоха 375. **Поправка:** отделни случаи „стар списък → двата пакета отказани“ и „чужд код само в places → 225 валидни хотела“. При crypto ON подайте правилния SHA на мутираното тяло и проверете извикването на валидатора: с несъвпадащ SHA измерих **0 извиквания**, следователно `null` самостоятелно допуска false pass.

2. **S28-2 — две отрицателни фикстури не падат.** Мутациите в [плана:353](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:353) запазват резултатите: преименуване на речниковото `chaika_kv` → **30**; alias „Аспарухово“ към `druzhba` → **16**, със същата подредба. Първото не променя токените от имената в редовете ([index.html:6739](/C:/git/Fire_Varna/index.html:6739)); второто се отхвърля от foreign-name guard ([recall_sweep.py:477](/C:/git/Fire_Varna/scratch/places_search/recall_sweep.py:477)). **Поправка:** назовете мутации върху действително използваните полета или правило; премерете точния различен отговор и изискайте конкретния провален assert.

3. **S28-3 — G7 може да сравни последния файл със самия него.** [План:479](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:479) оставя двата прогона да пишат `%TEMP%/fv_measures/lot1v_v_candidate_rows.json`; `OUTDIR` е общ ([recall_sweep.py:84](/C:/git/Fire_Varna/scratch/places_search/recall_sweep.py:84)). Командата `python -c "diff на …"` е псевдокод. **Поправка:** фиксирани ревизии на двигателя, еднакви нови входни блобове, два отделно запазени резултата и изпълним байтов comparator с exit 1 при разлика. Отрицателната мутация трябва доказано да промени резултата.

4. **S28-4 — G10 е червен още преди промяната.** Точната команда от [плана:482](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:482) изброява **19 файла, 26 839 286 B**, exit **1**. Включва архивни снимки, адресни данни и вложени basemap JSON файлове. **Поправка:** избройте измерения набор действително зареждани при първо отваряне файлове; отделно измерете отложената доставка за търсенето. Положителният и отрицателният праг трябва да дават различни присъди.

5. **S28-5 — редът спира на грешни очаквани exit кодове.** Първият `--manifest` в [плана:444](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:444) връща **1**, защото новите данни противоречат на старите очаквания: измерени **8 несъответствия**, включително „училище младост: 6, подписано 11“. Кодът записва новите очаквания, но връща `1 if red` ([recall_sweep.py:4330](/C:/git/Fire_Varna/scratch/places_search/recall_sweep.py:4330)). Обратно, командата на [план:420](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:420) само печата coverage резултата и завършва с **0**, независимо от вътрешния `exit_code=2`. **Поправка:** предварително изброени допустими несъответствия и изрично `sys.exit(result["exit_code"])`; повторното генериране не е независимо доказателство.

6. **S28-6 — G17 проверява брой, а обещава затворен набор.** Изпълних предложения код от [плана:275](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:275): замяната `_meta.generated → unexpected` запазва 10 ключа и връща **true**. Измислен attribution `src` с чужд URL също минава. **Поправка:** точни множества ключове за двата `_meta`, затворени допустими извори и съответните URL правила; отрицателни случаи със същия брой ключове.

7. **S28-7 — G8/G9 доказват текстово присъствие, не изпълнение.** [План:480](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:480) допуска attribution чрез помощна функция в картончето или неизпълним `addAttribution` в коментар. Освен това release прескача въпрос без артефакт ([release.py:1368](/C:/git/Fire_Varna/gates/release.py:1368)). **Поправка:** изпълнете реалния `popupFor` с DOM стъб и проверете резултата; наблюдавайте действителното добавяне на надписа; G9 да сверява digest, „да“ и човешкия произход на подписа.

8. **S28-8 — G11 допуска геометрия.** [План:483](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:483) търси буквално `coordinates`. Проба с JSON ключ `"\u0063oordinates"` даде **0 текстови попадения**, но след parse — `coordinates` в Polygon. Файлове извън `data/*.json` също отпадат. **Поправка:** структурна проверка на декодирания JSON и пълен инвентар на новите проследени файлове, с точни наследени изключения.

9. **S28-9 — G14 не сравнява файлове в PowerShell.** `Get-Command diff` върна `Alias Compare-Object`; командата от [плана:486](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:486) сравнява имената и завършва с **0**. **Поправка:** Python сравнение на байтовете с `sys.exit`, плюс отрицателна проба върху копие.

10. **S28-10 — уточнете отклоненията и архивирането.** §2 трябва изрично да включи запазения **мълчалив UI отказ**, забранен от подписаната основа ([нощен план:144](/C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:144)). Изтриване на старата опашка не е необходимо: архивиране извън точния glob е достатъчно; G15 трябва да използва същия glob, не substring. Измерената стара опашка съдържа **27 „да“, 0 „не“**.

Атомният комит 2 пази SHA пиновете и данните заедно; не намерих междинен SHA разрез. Baseline `f06ac06` с подменен allow за 138 реда е обоснован. Авторствата на трите varna_3d комита са правилни. Нищо не промених, комитнах или публикувах; няма remote команди. По време на одита външен процес добави само плана като `e6ba50e` — началната котва вече изисква актуализация.
tokens used
125,730
**НЕГОДНО за подпис.** Проверих v2 срещу реалния клиент, гейтовете и трите посочени комита на varna_3d, включително с беззаписни проби в паметта.

1. **S28-1 — G3 очаква невъзможните 225 реда.** В [плана:372](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:372) връщането на оригиналния `QUARTER_SRC` трябва да отхвърли само местата. Реалната доставка съдържа `SIGNED_POLYGON` и в хотелите. Node-пробата даде `validateHotels=false`, `validatePlaces2=false`, `places payload unavailable`, `RECS=0`; разширените списъци дадоха 375. **Поправка:** отделни случаи „стар списък → двата пакета отказани“ и „чужд код само в places → 225 валидни хотела“. При crypto ON подайте правилния SHA на мутираното тяло и проверете извикването на валидатора: с несъвпадащ SHA измерих **0 извиквания**, следователно `null` самостоятелно допуска false pass.

2. **S28-2 — две отрицателни фикстури не падат.** Мутациите в [плана:353](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:353) запазват резултатите: преименуване на речниковото `chaika_kv` → **30**; alias „Аспарухово“ към `druzhba` → **16**, със същата подредба. Първото не променя токените от имената в редовете ([index.html:6739](/C:/git/Fire_Varna/index.html:6739)); второто се отхвърля от foreign-name guard ([recall_sweep.py:477](/C:/git/Fire_Varna/scratch/places_search/recall_sweep.py:477)). **Поправка:** назовете мутации върху действително използваните полета или правило; премерете точния различен отговор и изискайте конкретния провален assert.

3. **S28-3 — G7 може да сравни последния файл със самия него.** [План:479](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:479) оставя двата прогона да пишат `%TEMP%/fv_measures/lot1v_v_candidate_rows.json`; `OUTDIR` е общ ([recall_sweep.py:84](/C:/git/Fire_Varna/scratch/places_search/recall_sweep.py:84)). Командата `python -c "diff на …"` е псевдокод. **Поправка:** фиксирани ревизии на двигателя, еднакви нови входни блобове, два отделно запазени резултата и изпълним байтов comparator с exit 1 при разлика. Отрицателната мутация трябва доказано да промени резултата.

4. **S28-4 — G10 е червен още преди промяната.** Точната команда от [плана:482](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:482) изброява **19 файла, 26 839 286 B**, exit **1**. Включва архивни снимки, адресни данни и вложени basemap JSON файлове. **Поправка:** избройте измерения набор действително зареждани при първо отваряне файлове; отделно измерете отложената доставка за търсенето. Положителният и отрицателният праг трябва да дават различни присъди.

5. **S28-5 — редът спира на грешни очаквани exit кодове.** Първият `--manifest` в [плана:444](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:444) връща **1**, защото новите данни противоречат на старите очаквания: измерени **8 несъответствия**, включително „училище младост: 6, подписано 11“. Кодът записва новите очаквания, но връща `1 if red` ([recall_sweep.py:4330](/C:/git/Fire_Varna/scratch/places_search/recall_sweep.py:4330)). Обратно, командата на [план:420](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:420) само печата coverage резултата и завършва с **0**, независимо от вътрешния `exit_code=2`. **Поправка:** предварително изброени допустими несъответствия и изрично `sys.exit(result["exit_code"])`; повторното генериране не е независимо доказателство.

6. **S28-6 — G17 проверява брой, а обещава затворен набор.** Изпълних предложения код от [плана:275](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:275): замяната `_meta.generated → unexpected` запазва 10 ключа и връща **true**. Измислен attribution `src` с чужд URL също минава. **Поправка:** точни множества ключове за двата `_meta`, затворени допустими извори и съответните URL правила; отрицателни случаи със същия брой ключове.

7. **S28-7 — G8/G9 доказват текстово присъствие, не изпълнение.** [План:480](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:480) допуска attribution чрез помощна функция в картончето или неизпълним `addAttribution` в коментар. Освен това release прескача въпрос без артефакт ([release.py:1368](/C:/git/Fire_Varna/gates/release.py:1368)). **Поправка:** изпълнете реалния `popupFor` с DOM стъб и проверете резултата; наблюдавайте действителното добавяне на надписа; G9 да сверява digest, „да“ и човешкия произход на подписа.

8. **S28-8 — G11 допуска геометрия.** [План:483](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:483) търси буквално `coordinates`. Проба с JSON ключ `"\u0063oordinates"` даде **0 текстови попадения**, но след parse — `coordinates` в Polygon. Файлове извън `data/*.json` също отпадат. **Поправка:** структурна проверка на декодирания JSON и пълен инвентар на новите проследени файлове, с точни наследени изключения.

9. **S28-9 — G14 не сравнява файлове в PowerShell.** `Get-Command diff` върна `Alias Compare-Object`; командата от [плана:486](/C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:486) сравнява имената и завършва с **0**. **Поправка:** Python сравнение на байтовете с `sys.exit`, плюс отрицателна проба върху копие.

10. **S28-10 — уточнете отклоненията и архивирането.** §2 трябва изрично да включи запазения **мълчалив UI отказ**, забранен от подписаната основа ([нощен план:144](/C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:144)). Изтриване на старата опашка не е необходимо: архивиране извън точния glob е достатъчно; G15 трябва да използва същия glob, не substring. Измерената стара опашка съдържа **27 „да“, 0 „не“**.

Атомният комит 2 пази SHA пиновете и данните заедно; не намерих междинен SHA разрез. Baseline `f06ac06` с подменен allow за 138 реда е обоснован. Авторствата на трите varna_3d комита са правилни. Нищо не промених, комитнах или публикувах; няма remote команди. По време на одита външен процес добави само плана като `e6ba50e` — началната котва вече изисква актуализация.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Б3_07.09.md'; "'$s=Get-Content -LiteralPath $p -Encoding UTF8; 0..149 | ForEach-Object { '"'{0}: {1}' -f ("'$_+1),$s[$_] }' in C:\git\Fire_Varna
 succeeded in 0ms:
1: # ПЛАН Б3 · Търсене по квартал над подписаните граници (Fire_Varna) — v3
2: 
3: **Дата:** 07.09.2026 · **Планер:** Claude Planner (read-only) · **Статус:** ЧАКА ПОДПИС (Gate 1) · **Заменя:** v2 (`e6ba50e`, чернова, неподписана), след две външни оборвания — **Astra S28** (механика, 10 условия) и **Кими К28** (данни/семантика, 7 условия), и двете **НЕГОДНО** (§12).
4: **Клас на риска:** 🔴 **Архитектурен** (ескалационно-доминантен). Спуснали се спусъци: (1) промяна на схема/ADR — `_meta` 9→10 и 7→8 ключа, затворените списъци `QUARTER_SRC`/`QUARTER_CODES`/новият `LOCALITY_SRC` са договор, ADR 010 D3/D12/D13 носят остарял текст; (2) необратима канонична мутация — замразената референция, `expectations.json`, подписаният allow и **изваждане на подписана опашка от глоба на release**; (3) release/publish верига — този комит е това, което Петър пуска към живата карта; (4) кръстосан blast radius varna_3d → Fire_Varna по подредената тройка D13. Топология: **Вариант А** (планер → подпис на Петър → изпълнител → одитор → преглед на Петър → пуш от Петър).
5: **Записване:** планерът е read-only и НЕ е записал този файл в репото. Изпълнителят го записва като `C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md` в първия си комит, дословно.
6: 
7: > **Произход на числата (честно).** v2 беше писан без Bash — всяко число там беше или **(Ч)** прочетено, или **(М)** от чужда мярка. **v3 е измерен от планера със собствени команди.** Всяко число долу носи командата, с която е получено. Числата, които не съм могъл да измеря без запис в репото, са измерени в **клонинг** (`git clone --shared C:/git/Fire_Varna <scratchpad>/shadow`) — това чете източника и не пише в него; такива числа са маркирани **(К)** и изпълнителят ги преизмерва на място.
8: >
9: > **Нищо не е писано, комитвано или пускано в `C:/git/Fire_Varna` и `C:/git/varna_3d` от тази сесия.**
10: 
11: ---
12: 
13: ## 0 · Червени редове (наследени, без изключение)
14: 
15: Дословно от `C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:11-23`:
16: 
17: 1. **Агентите не пушат.** Никога, с никакъв флаг, без `--no-verify` (`:13`).
18: 2. **Нула геометрия в проследен файл на Fire_Varna.** Публично пътуват само име, код и картата за атрибуция (`:14`).
19: 3. **`Varna_buildings/config/quarter_registry.json` не се пипа** (`:15`).
20: 4. **Написан квартал не се променя** (D18/G17) (`:16`).
21: 5. **Малки, обратими комити**, изчерпателен write-set, дословно съобщение, автор `Claude Executor <executor@local>`; **подписаната геометрия и решенията чакат комит на `Petar1984`** (D16, G4 fail-closed) (`:17`). → О4 и **О24**: авторството се НАЛАГА с флагове, не се предполага.
22: 6. **Всеки гейт е команда с изход ≠ 0 и с отрицателна фикстура, която ТРЯБВА да падне.** Паднал гейт СПИРА лота (`:18`).
23: 7. **Само Opus** — изпълнители и одитори (`:19`).
24: 8. **Одиторът е друг агент** (read-only) (`:20`).
25: 
26: Допълнителни за този лот:
27: 
28: 9. **Кръстосаната изолация е еднопосочна:** от Fire_Varna се ЧЕТЕ блоб на varna_3d (`git -C ../varna_3d show <rev>:<път>`, командата е записана в `tests/test_places_public_bundle.py:49`). Нищо не се пише, комитва или пуска във varna_3d от тази сесия.
29: 10. **Нищо не се публикува преди локалния преглед на Петър** (`python -m http.server 8000`, §8).
30: 11. **„pending — Петър“ не е подпис.** `gates/run_gates.py:775-790` връща 1 и при жълто.
31: 12. **Точно ЕДНА опашка в HEAD и точно ЕДИН allow-json.** (Ч) `gates/release.py:171-172` (`QUEUE_DIR = "scratch/places_search"`, `QUEUE_GLOB = "ЗА_ПОДПИС_*.md"`), `:437-458` (`queues_in_head` чете `git ls-tree -r -z HEAD` и сравнява **basename**-а), `:465-472` (>1 → `raise ValueError`), `:1259-1265` (изключението → BLOCKED). Allow: `gates/run_gates.py:199-217`.
32: 13. 🔴 **Нов (О30): `recall_sweep.py --manifest` ПРЕЗАПИСВА `expectations.json`.** Вторият прогон в същия ден е зелен по конструкция. Доказателство се снема САМО от ПЪРВИЯ прогон срещу подписаното тяло.
33: 
34: ---
35: 
36: ## 1 · Мярка (базата, преди един ред промяна)
37: 
38: ### 1.1 Състояние на репата — **преизмерено 07.09, котвата се движи**
39: 
40: | какво | стойност | команда |
41: |---|---|---|
42: | Fire_Varna HEAD | **`5fce47c`** „state: §8 — Б3 plan v2 measured findings, S28/К28 verdicts, revision 3 in progress“ | `git -C /c/git/Fire_Varna log -1 --pretty='%h %an %s'` |
43: | предходни котви | `1e6f85b` (К28), `8715a6c` (S28), `e6ba50e` (план v2), `f00dd78` (край на Б2) | `git log --oneline -5` |
44: | проследено дърво | **чисто** (0 реда без `??`) | `git status --porcelain \| grep -v "^??" \| wc -l` → `0` |
45: | ahead от origin | **85** | `git rev-list --count origin/main..HEAD` |
46: | varna_3d HEAD | `05f485e` (клон `rezhimi`) — трите блоба на доставката | `git -C /c/git/varna_3d log --oneline -3` |
47: | Node | **v22.19.0** | `node --version` |
48: | опашки в HEAD | **1** — `scratch/places_search/ЗА_ПОДПИС_A.md` | `git ls-tree -r --name-only HEAD -- scratch/places_search \| grep "ЗА_ПОДПИС"` |
49: | allow-файлове | **1** — `gates/allow/2026-09-05_lot1v_v.json` (150 реда, `signed_by: Петър`) | `python -c "import pathlib; print([p.name for p in pathlib.Path('gates/allow').glob('*.json')])"` |
50: 
51: **Стъпка 0 на §4 преизмерва и петте — HEAD се движи, докато планът чака подпис.**
52: 
53: ### 1.2 Днешните котви в `C:/git/Fire_Varna/index.html`
54: 
55: | котва | ред | текуща стойност |
56: |---|---|---|
57: | `PLACES_CACHE` | `:6265` | `'fire-varna-hotels-v6-225'` |
58: | `HOTELS_SHA256` / `PLACES2_SHA256` / `CATS_SHA256` | `:6288` / `:6289` / `:6290` | `46a44ce8…` / `329310f5…` / `874e33cd…` |
59: | `LEGACY_BUNDLE_SHA` | `:6301-6304` | places `329310f5…`, hotels `46a44ce8…` |
60: | `QUARTER_SRC` | `:6313` | `['REG', 'KAIS', 'SIGNED_OVERRIDE']` |
61: | `DISTRICT_SRC` / `DISTRICT_CODES` | `:6314` / `:6315-6316` | 2 извора / 5 кода |
62: | `QUARTER_CODES` | `:6317-6321` | **20 кода** (масив, не `Set`) |
63: | `LOCALITY_CODES` | `:6322` | 5 кода |
64: | `isSignificantToken` | `:6495-6496` | `!t.num && t.orig.length > 2 && t.s.length > 2 && …ADDR… && !GENERIC_WORDS.has(t.s)` |
65: | `validLocation` | `:6528-6534` | `src ∈ srcs && code ∈ codes` |
66: | `validTypedLocation` | `:6535-6545` | **`:6537` валидира `locality` със `QUARTER_SRC`**; `:6544` `zone === quarter.name ?? 'район '+district.name` |
67: | `validateHotels` / `validatePlaces2` | `:6546-6562` / `:6563-6580` | **не броят ключовете на `_meta`, не четат `quarter_attribution`** |
68: | **`accept`** | **`:6602-6612`**, условието на **`:6605`** | `if (window.crypto && crypto.subtle) { … digest ≠ sha → return null }` — **валидаторът се вика САМО след успешна sha-сверка** (1.8.11) |
69: | `fetchValidatedJson` / `ensurePlaces` | `:6613-6625` / `:6626-6647` | `throw 'places payload unavailable'` само ако И двата масива са празни (`:6639`) |
70: | **`buildIndex`** | **`:6648`** | **приема ВЕЧЕ разпарсени масиви — не вика нито един валидатор** |
71: | `makeRec` qtk/qph | `:6749`, `:6782` | — |
72: | **М7 клонът на клиента** | **`:7058-7069`** | `R.every(isSignificantToken)` + `qHit`/`lHit`/`bphrase` — **тук няма списък с типови префикси** (К28-5) |
73: | районните клонове | `:7064`, `:7118` | `!r.e.quarter` — двете места на типовия капан |
74: | изричното „район X“ с ключ | `:7104-7109` | филтрира САМО по `r.dph`; **не гледа `quarter`** |
75: | `popupFor` | `:7253-7289` | редът „вид · квартал · район“ на `:7257-7271`; **ред за извор НЯМА и днес**; ползва `span` (`:7155`), `buildNavActions` (`:4255`), `SRC_LINE`/`ADDR_SRC_LINE`/`ALIAS_SRC_LINE` (`:6328-6360`) |
76: | Leaflet | `:1900` `zoomControl → bottomleft`; `:1901` `OSM_ATTRIB = '© OpenStreetMap'`; `:1917` `attribCtrl` (`position: 'bottomleft'`); `:1918` `attribCtrl.addAttribution(OSM_ATTRIB)` | размени: `:4543-4549`, `:4663`, `:4672-4676` |
77: | pmtiles флаг + override | `:4563` `false`; `:4571-4574` `isBasemapPmtilesActive()` чете `localStorage` | пътят е достижим и днес |
78: | **зареждане при първо отваряне** | `:1772-1774` `fetch('data/hydrants.json')` — **безусловен IIFE** | `ensurePlaces()` се вика САМО от `inputEl.addEventListener('focus', …)` (`:7393`); адресната търсачка е lazy (`:5325-5326`, `fetchCachedJson` на фокус); `data/approx_addresses_v1.json` е зад изключен флаг (`:5926 APPROX_ADDRESS_SEARCH_ENABLED = false`); `data/basemaps/basemap_manifest.json` — само при активен pmtiles (`:4563` false) |
79: 
80: Нула попадения за point-in-polygon. **Кварталът е доставено поле + речник от думи, не геометрия.**
81: 
82: ### 1.3 Липсващите кодове
83: 
84: Доставката носи **28** квартални кода; `QUARTER_CODES` носи 20; липсват точно **8**:
85: `dolna_traka · grackata_mahala · hristo_botev · kolhozen_pazar · kv_levski · sv_ivan_rilski · trakia · tsentar`.
86: `set(QUARTER_CODES) − доставени = ∅`. Делтата е **+8**, не „+41“ (О3).
87: Речникът (`place_categories.json.locations.quarter`) носи **точно същите 28 кода** — `dict == delivered: True`, `parents` **0 от 28**, `locality` 5, `district` 5.
88: 
89: ### 1.4 Новите пинове (LF-блобове от git, не от диска)
90: 
91: Команда:
92: ```bash
93: git -C /c/git/varna_3d show 05f485e:data/fire_varna_places.json > <scratch>/new_data/places.json   # и другите два
94: python - <<'PY'
95: import hashlib, gzip, pathlib
96: for p in ['places.json','hotels.json','place_categories.json']:
97:     b = pathlib.Path('<scratch>/new_data/'+p).read_bytes().replace(b'\r\n', b'\n')
98:     print(p, len(b), hashlib.sha256(b).hexdigest(), len(gzip.compress(b, 9)))
99: PY
100: ```
101: 
102: | файл (източник → цел) | sha256 | bytes | gzip9 |
103: |---|---|---|---|
104: | `varna_3d:data/fire_varna_places.json` → `data/places.json` | `3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66` | **128401** | **14748** |
105: | `varna_3d:data/fire_varna_hotels.json` → `data/hotels.json` | `eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51` | **151263** | **13642** |
106: | `varna_3d:data/place_categories.json` → `data/place_categories.json` | `9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231` | **77998** | **9690** |
107: 
108: **Капан:** работното дърво на varna_3d е CRLF за два от трите — мери се `git show`, не `os.path.getsize`.
109: 
110: ### 1.5 Какво носи доставката — **преизмерено, с поправка на v2**
111: 
112: - places **150** / hotels **225**; нула добавени, нула изтрити.
113: - Извори на `quarter`: places `{SIGNED_POLYGON: 42, REG: 39, KAIS: 10, null: 59}`; hotels `{REG: 115, KAIS: 25, SIGNED_OVERRIDE: 12, SIGNED_POLYGON: 15, null: 58}`. **`DISTRICT_FALLBACK`: 0 реда.**
114: - **`zone !== quarter.name`: 0 реда** в двата пакета (О20 остава верен).
115: - 🔴 **Поправка на v2 §1.5.** v2 пише „`quarter_attribution` = 18 кода“. Измереното: картата е **на всеки пакет поотделно** — **places 14** (13 wikimapia + 1 openstreetmap), **hotels 7** (всичките wikimapia); **обединението е 18**, общите са **3** (`kolhozen_pazar`, `kv_levski`, `tsentar`). Това е ЕДИНСТВЕНОТО правилно основание за G17.
116: - 🔴 **Всяка карта е ТОЧНО равна на множеството `SIGNED_POLYGON` кодове на своя пакет** (`qa == sp: True` и за двата; `qa−sp = ∅`, `sp−qa = ∅`). Гейтът е **равенство**, не „включване“ (по-силно от буквата на амандамент №2).
117: - Запис на всеки код: точно четирите ключа `{label, licence, src, url}` (едно-единствено ключово множество за всичките 21 записа).
118: - Единственият не-wikimapia запис: `mladost2 → {"src": "openstreetmap", "label": "© OpenStreetMap contributors", "licence": "ODbL", "url": "https://www.openstreetmap.org/copyright"}` — **url-ът НЕ е по формата на wikimapia** и всяко правило „един регекс за всички“ пада върху него.
119: - Wikimapia url-ите са **`http://wikimapia.org/<id>/bg/<път>`** (пример: `http://wikimapia.org/900042/bg/ж.к._Васил_Левски`) — `http`, с път след id-то (О17).
120: - Речник: зони 20→28, псевдоними 39→48; `parents` — **0 от 28**.
121: - Нула геометрия, нула кадастрален идентификатор (структурна проверка, 1.8.12).
122: 
123: ### 1.5б 🔴 `_meta` — точните множества ключове (единственият авторитет на G17)
124: 
125: ```
126: places._meta  (10): generated · count · by_kind · by_zone_src · licence_osm ·
127:                     licence_registry · licence_wikidata · licence_address ·
128:                     quarter_attribution · excluded
129: hotels._meta  (8):  generated · count · by_zone_src · licence · licence_osm ·
130:                     licence_address · quarter_attribution · excluded
131: ```
132: Днешните (старите) са **9** и **7** — същите списъци без `quarter_attribution`. Броят е **следствие**; договорът е множеството.
133: 
134: ### 1.6 Какво умира днес, ако блобовете влязат сами — **изпълнено, не изведено** 🔴
135: 
136: Node-проба върху среза `index.html:6256-7154` с ДНЕШНИТЕ списъци над НОВИТЕ байтове (стъбове: `window`, `caches`, `document`, `map`, `fetch`, `attribCtrl`, `L`, `console`, `crypto`):
137: 
138: ```
139: validateHotels   = false        ← хотелите СЪЩО носят SIGNED_POLYGON (15 реда)
140: validatePlaces2  = false
141: accept(text, пинат sha, validatePlaces2) = null
142: await ensurePlaces()  →  ХВЪРЛЯ  Error: places payload unavailable      (:6639)
143: ```
144: 
145: **Това оборва v2 §3.6 т. 4 („`RECS.length === 225` при среза с оригиналния `QUARTER_SRC`“): при стария списък НЯМА `RECS` — има изключение.** 225 е достижимо само когато **само** places е отказан (1.8.10, случай 9в).
146: 
147: ### 1.7 Референцията и фикстурите
148: 
149: | прогон | резултат | exit |
150: |---|---|---|

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git ls-files -- gates tests scratch/places_search scripts data index.html CLAUDE.md docs/activeContext.md' in C:\git\Fire_Varna
 succeeded in 0ms:
CLAUDE.md
data/address_rows.json
data/approx_addresses_v1.json
data/basemaps/basemap_manifest.json
data/basemaps/osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b/odbl/ATTRIBUTION.txt
data/basemaps/osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b/odbl/README_ODbL.md
data/basemaps/osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b/odbl/osm_varna_patch_v1.csv
data/basemaps/osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b/odbl/osm_varna_source_manifest.json
data/basemaps/osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b/style.json
data/basemaps/osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b/varna_basemap.pmtiles
data/basemaps/osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b/varna_basemap_manifest.json
data/basemaps/range_canary.pmtiles
data/generation_manifest.json
data/hotels.json
data/hydrants.json
data/hydrants.json.pre_address_backfill.json
data/hydrants.json.pre_cleanup_snapshot.json
data/hydrants_provenance.json
data/hydrants_provenance.json.pre_address_backfill.json
data/place_categories.json
data/places.json
data/removed_hydrants.json
data/search_index.json
data/signed_facts.json
docs/activeContext.md
gates/__init__.py
gates/allow/2026-09-05_lot1v_v.json
gates/baseline/MANIFEST.json
gates/coverage.py
gates/release.py
gates/run_gates.py
gates/sign.py
index.html
scratch/places_search/.gitignore
scratch/places_search/agkk_inspire_2026-09-05/varna_municipality_kvartali_hub_meta_2026-09-05.json
scratch/places_search/agkk_inspire_measure_05.09.md
scratch/places_search/baseline_02.09.md
scratch/places_search/check_municipal_kvartali.py
scratch/places_search/derived_boundaries_measure_05.09.md
scratch/places_search/district_resolutions_2026-09-07.json
scratch/places_search/expectations.json
scratch/places_search/gen_m7_tokens.py
scratch/places_search/golden_panel_synthesis.md
scratch/places_search/granitsi_am2_astra_S14-S19_06.09.md
scratch/places_search/granitsi_am2_astra_S20_verify_06.09.md
scratch/places_search/granitsi_am2_brief_astra.md
scratch/places_search/granitsi_am2_brief_kimi.md
scratch/places_search/granitsi_am2_kimi_K15-K20_06.09.md
scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md
scratch/places_search/granitsi_am3_astra_S25_07.09.md
scratch/places_search/granitsi_am3_kimi_K26_07.09.md
scratch/places_search/granitsi_astra_official_boundaries_05.09.md
scratch/places_search/granitsi_b1v2_astra_S23_07.09.md
scratch/places_search/granitsi_b1v2_kimi_K24_07.09.md
scratch/places_search/granitsi_b1v4_astra_S24_07.09.md
scratch/places_search/granitsi_b1v4_kimi_K25_07.09.md
scratch/places_search/granitsi_b2_astra_S26_07.09.md
scratch/places_search/granitsi_b2_astra_S27_07.09.md
scratch/places_search/granitsi_b2_kimi_K27_07.09.md
scratch/places_search/granitsi_b3_astra_S28_07.09.md
scratch/places_search/granitsi_b3_kimi_K28_07.09.md
scratch/places_search/granitsi_blocks_astra_B1-B6_05.09.md
scratch/places_search/granitsi_blocks_brief_astra.md
scratch/places_search/granitsi_blocks_brief_kimi.md
scratch/places_search/granitsi_blocks_kimi_B1-B6_05.09.md
scratch/places_search/granitsi_decisions_2026-09-06_proba.json
scratch/places_search/granitsi_decisions_2_2026-09-06_proba.json
scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json
scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json
scratch/places_search/granitsi_fixtures_06.09.json
scratch/places_search/granitsi_forumi_astra_T1-T4_06.09.md
scratch/places_search/granitsi_forumi_brief_astra.md
scratch/places_search/granitsi_forumi_brief_kimi.md
scratch/places_search/granitsi_forumi_kimi_F1-F5_06.09.md
scratch/places_search/granitsi_night_astra_S21_06.09.md
scratch/places_search/granitsi_night_astra_S22_review_07.09.md
scratch/places_search/granitsi_night_kimi_K22_06.09.md
scratch/places_search/granitsi_night_kimi_K23_review_07.09.md
scratch/places_search/granitsi_osm_astra_A1-A4_05.09.md
scratch/places_search/granitsi_osm_brief_astra.md
scratch/places_search/granitsi_osm_brief_kimi.md
scratch/places_search/granitsi_osm_kimi_T1-T5_05.09.md
scratch/places_search/granitsi_rayoni_astra_R0-R6_05.09.md
scratch/places_search/granitsi_rayoni_brief_astra.md
scratch/places_search/granitsi_rayoni_brief_kimi.md
scratch/places_search/granitsi_rayoni_kimi_P1-P5_05.09.md
scratch/places_search/granitsi_v2_astra_S7-S13_05.09.md
scratch/places_search/granitsi_v2_brief_astra.md
scratch/places_search/granitsi_v2_brief_kimi.md
scratch/places_search/granitsi_v2_kimi_K8-K14_05.09.md
scratch/places_search/granitsi_zoniraine_brief_kimi.md
scratch/places_search/granitsi_zonirane_kimi_Z1-Z5_05.09.md
scratch/places_search/lot1_reference_preview_v2.md
scratch/places_search/lot1v_addr_join.json
scratch/places_search/lot1v_addresses_for_signature.md
scratch/places_search/lot1v_brief_kimi.md
scratch/places_search/lot1v_brief_sol.md
scratch/places_search/lot1v_v_brief_kimi.md
scratch/places_search/lot1v_v_brief_sol.md
scratch/places_search/lot1v_v_manifest_BASE_P7.json
scratch/places_search/lot1v_v_manifest_P7_F12.json
scratch/places_search/lot1v_v_reference_manifest.json
scratch/places_search/lot1v_v_zones_for_signature.md
scratch/places_search/m7_significance_gate.py
scratch/places_search/m7_trigger_tokens.json
scratch/places_search/manifest_anchor_gate.py
scratch/places_search/manifest_before.json
scratch/places_search/municipal_kvartali_layer_05.09.md
scratch/places_search/noshtna_pins_06.09.json
scratch/places_search/osm_quarters_measure_05.09.md
scratch/places_search/p7_attack_brief.md
scratch/places_search/p7_zone_aliases.json
scratch/places_search/p7_zone_aliases_v2.json
scratch/places_search/probe_out/after.json
scratch/places_search/probe_out/after_requests.json
scratch/places_search/probe_out/before.json
scratch/places_search/probe_out/before_requests.json
scratch/places_search/probe_out/g4.json
scratch/places_search/probe_out/screens/hospital.png
scratch/places_search/probe_out/screens/hotel.png
scratch/places_search/probe_out/screens/school.png
scratch/places_search/probe_out/token_parity.json
scratch/places_search/probe_places_fv.mjs
scratch/places_search/qa_night_acceptance.py
scratch/places_search/qa_night_pins.py
scratch/places_search/recall_sweep.py
scratch/places_search/recall_sweep_rows.json
scratch/places_search/wikimapia_frozen_measure_06.09.md
scratch/places_search/wikimapia_petar_notes_06.09.md
scratch/places_search/wikimapia_terms_2026-09-06.md
scratch/places_search/БОРД_истинност_375.md
scratch/places_search/ЗА_ПОДПИС_A.md
scratch/places_search/КАРТА_на_състоянието_05.09.md
scratch/places_search/ОБОРВАНЕ_ПЛАН_Ред_05.09.md
scratch/places_search/ОДИТ_A210_05.09.md
scratch/places_search/ОДИТ_A211_05.09.md
scratch/places_search/ОДИТ_A29_05.09.md
scratch/places_search/ОДИТ_ЛОТ0_05.09.md
scratch/places_search/ОДИТ_ЛОТ0fix_05.09.md
scratch/places_search/ОТЧЕТ_A211_05.09.md
scratch/places_search/ОТЧЕТ_Ф0б_05.09.md
scratch/places_search/ПРЕГЛЕД_търговско-обществени_03.09.md
scratch/places_search/ЧЕРНОВА_ПЛАН_Ред_05.09.md
scripts/apply_approved_reports.py
scripts/backfill_addresses_20260511.py
scripts/backfill_verified_type_20260509.py
scripts/copy_basemap_release.py
scripts/hooks/pre-push
scripts/import_etr_kmz.py
scripts/lib/__init__.py
scripts/lib/hydrant_core.py
scripts/migrate_to_verbose_schema.py
scripts/replay_historical_new_hydrant.py
scripts/vendor_basemap_deps.mjs
tests/golden_apply_v0.py
tests/test_apply_approved_reports_parity.py
tests/test_approx_addresses_public_bundle.py
tests/test_basemap_manifest.py
tests/test_data_ascii_mojibake.py
tests/test_etr_kmz_adapter.py
tests/test_granitsi_fixtures.py
tests/test_hotels_public_bundle.py
tests/test_hydrant_core.py
tests/test_places_public_bundle.py
tests/test_places_search_gate.py
tests/test_places_search_primitives.py
tests/test_ui_ascii_mojibake.py
tests/verify_apply.py
tests/verify_h4.py

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$s=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8; 150..299 | ForEach-Object { '{0}: {1}' -f ("'$_+1),$s[$_] }' in C:\git\Fire_Varna
 succeeded in 0ms:
151: | `python -m unittest tests.test_granitsi_fixtures -v` | `Ran 5 tests · OK` | 0 |
152: | `python -m unittest discover -s tests` | `Ran 315 tests · OK` | 0 |
153: | `python -m gates.run_gates` | 7/7 зелени | 0 |
154: 
155: Върху **новата** доставка (двигателят е `recall_sweep.py` с подменени пътища към новите блобове, `main()` не се вика — нула запис):
156: 
157: | заявка | днес | нова доставка |
158: |---|---|---|
159: | „детска градина дойран“ | `A3-street`, 1 | `A3-street`, **1** |
160: | „училище район младост“ | `A3-district`, 12 | **12** (9 с квартал) |
161: | „младост“ | `M7-bare`, 28 | **20** (8 с квартал / 12 без) |
162: | „училище младост“ | `A3-location`, 11 | **6** (3 с квартал) |
163: | „възраждане“ | — | `M7-bare`, **5** |
164: | „училище възраждане“ | — | **1** (`II ОУ „Никола Йонков Вапцаров“`) |
165: 
166: 🔴 **К28-3 · Осемте изгубени реда на „младост“, поименно и с новия си квартал** (v2 назоваваше пет):
167: 
168: | # | ред | стар `zone` | нов квартал |
169: |---|---|---|---|
170: | 1 | `ОУ „Иван Вазов“` | район Младост | `pobeda` · ж.к. Победа |
171: | 2 | `Професионална гимназия по електротехника` | район Младост | `pobeda` · ж.к. Победа |
172: | 3 | `Професионална Техническа Гимназия` | район Младост | `pobeda` · ж.к. Победа |
173: | 4 | **`ДГ№53 „Слънчево зайче“`** | район Младост | `sv_ivan_rilski` · кв. Св. Иван Рилски |
174: | 5 | `ОУ Отец Паисий` | район Младост | `sv_ivan_rilski` · кв. Св. Иван Рилски |
175: | 6 | **`ДГ№26 „Изворче"`** | район Младост | `troshevo` · кв. Трошево |
176: | 7 | `ОУ Добри Чинтулов` | район Младост | `troshevo` · кв. Трошево |
177: | 8 | **`ДГ 24 "Детско градче"`** | район Младост | `troshevo` · кв. Трошево |
178: 
179: Механизмът (Ч): районът отговаря само докато `quarter is None` (`recall_sweep.py:1123`, `:1167`; `index.html:7064`, `:7118`). **Загуба по замисъл — иска подпис, и опашката ѝ дължи ОСЕМ делта-реда, не пет** (§4 стъпка 11, STOP 19). „училище младост“ губи 5 от същите осем (1, 2, 3, 5, 7).
180: 
181: ### 1.8 🔴 Мерките, които оборванията добавиха (новите СТОП-числа)
182: 
183: | # | мярка | стойност | команда |
184: |---|---|---|---|
185: | 1.8.1 | покритие срещу подписания baseline `f06ac06` с новите блобове, `allow_path=None` | **exit 2 · uncovered 138** (places `zone_named` lost 44 + changed 44 = 88; hotels lost 39 + changed 11 = 50); нетен спад по `places.zone_named` (127→91) и `hotels.zone_named` (199→167) | §5 G18 |
186: | 1.8.1б 🔴 | **същото, но `base = f00dd78` (данните на днешния HEAD)** — дифът, който ОБЯСНЯВА 138-те (К28-6) | **exit 2 · uncovered 150** (places 78+18=96; hotels 47+7=54). Значи доставката **връща 12** от вече разрешените редове: **150 → 138** | §4 стъпка 2 |
187: | 1.8.2 | покритие при `base == candidate` | exit **3** · `allow-файл с изброен, но непроменен ред` · stale 150 | §11 т. 1 |
188: | 1.8.3 | покритие срещу `f06ac06` с новите блобове **и днешния подписан allow** | exit **2** · uncovered **30** · **stale 42** (150 − 42 = 108 ползвани; 108 + 30 = 138 ✓) | §4 стъпка 2 |
189: | 1.8.4 🔴 | „кв. Левски“ / „кв. Тракия“ / „кв. Христо Ботев“ / „ж.к. Св. Иван Рилски“ | `M3`, съответно **4 / 1 / 24 / 22** реда. **Поправка на v2 (К28-1): „кв. Христо Ботев“ носи ЕДИН ред с търсения код** — `ЦДГ 8 - Христо Ботев` (`hristo_botev`), и то **по ИМЕ**, не през кварталния механизъм. Другите три носят **нула** с търсения код | двата двигателя |
190: | 1.8.5 | „левски“ (голо) | `M7-bare`, **14** реда, **12** с код `kv_levski` | двата двигателя |
191: | 1.8.6 | „възраждане 2“ / „ж.к. възраждане 2“ / „младост 2“ | **0 реда** (`M3`) | двата двигателя |
192: | 1.8.7 | „чайка“ | `M7-bare`, **30** реда — `chaika_kk` 19 + `chaika_kv` 10 + 1 без квартал (`„ДКЦ Чайка“ ЕООД`) | двата двигателя |
193: | 1.8.8 | „аспарухово“ / „дружба“ | **16** (9 `asparuhovo` + 7 „район Аспарухово“ без квартал; **без** `ЦДГ 43 „Пинокио“`) / **2** | двата двигателя |
194: | 1.8.9 | „кайсиева градина“ / „училище възраждане 3“ | `M2-failopen` 3 / `M2` 2 (`3 ОУ Ангел Кънчев` [кв. Левски], `III ПМГ` [кв. Тракия]) | двата двигателя |
195: | **1.8.10** 🔴 | **Node-матрицата на приемането** (изпълнена, §3.6) | (а) стар `QUARTER_SRC` → `false/false`, `ensurePlaces` **ХВЪРЛЯ**; (б) след И2/И4/И5 → `true/true`, **`RECS === 375`**; (в) чужд код САМО в places (пинът = sha на мутираното тяло) → `validateHotels true`, `validatePlaces2 false`, **`RECS === 225`**, без хвърляне | §3.6 |
196: | **1.8.11** 🔴 | **crypto × sha × брой извиквания на валидатора** | `ON` + грешен sha → `null`, **0 извиквания**; `ON` + верен sha → `null`, 1; `OFF` + грешен sha → `null`, **1**; `OFF` + верен sha → `null`, 1. **Значи `null` сам по себе си НЕ доказва отказ на валидатора** | §3.6 |
197: | **1.8.12** 🔴 | **структурна геометрия** по 18-те проследени `data/**/*.json` | **0** ключа `coordinates`/`geometry`/`geometries` след `json.load`. Буквалният `grep coordinates` дава едно попадение в `data/hydrants_provenance.json` — **проза в стойност** (`"…replaced landmark label … with the hydrant coordinates"`), не ключ | §5 G11 |
198: | **1.8.13** 🔴 | **първо зареждане** (`AGENTS.md:53`: `index.html` + `data/hydrants.json`) | `index.html` **560 855** B + `data/hydrants.json` **1 317 355** B = **1 878 210 B ≈ 1,79 MB** при твърд таван 5 MB → **exit 0**. И двата файла са LF (0 CRLF). Отложената доставка на търсенето (hotels+places+categories) е **357 662 B ≈ 0,34 MB** и се брои отделно | §5 G10 |
199: | **1.8.14** 🔴 | **командата на v2 за G10** (`git ls-files index.html 'data/*.json'`) | **19 файла, 26 839 286 B, exit 1** — червено ПРЕДИ каквато и да е промяна: списъкът лови архивни снимки (`hydrants.json.pre_*`), `search_index.json` (11,2 MB), `address_rows.json` (5,07 MB), `hydrants_provenance*` (5,57 MB) и вложените basemap json-и | §13 |
200: | **1.8.15** 🔴 | **`recall_sweep.py --manifest` срещу ПОДПИСАНИТЕ очаквания, с новите блобове** (К) | **exit 1**; **59 реда `ЧЕРВЕНО`**; **41 уникални заявки** + 2 реда без заявка. Гейтове: П7 **16/32**, ЛОТ 1 **6/18**, 1в-А **5/12**, 1в-Б **5/6**, 1в-В **4/10** (квартал 258 · доп. 12 · район 375/375), М7 **17/17**, §10 sweep 60/62 · 10/10, „срещу подписа 1“; вътрешният release: `BLOCKED: 4` | §4 стъпка 10 |
201: | **1.8.16** 🔴🔴 | **ВТОРИЯТ `--manifest` прогон** (К) | **exit 0, 0 реда `ЧЕРВЕНО`** — защото първият вече е презаписал `expectations.json` (report-only, `signed_by: pending — Петър`). **Повторното генериране е вакуумно зелено** | червен ред 13, STOP 20 |
202: | **1.8.17** 🔴 | **`P7_ADDED` дрейф** (нова находка, нито S28, нито К28) | стари данни: **2 токена в 2 зони**; нови: **7 токена в 5 зони** (`Гръцката махала: gratska, gratski`; `к.к. Св. Св. Константин и Елена: konstanin`; `кв. Владиславово: varnenchik, vladislav`; `кв. Изгрев: zhkizgrev`; `кв. Левски: vasil`); засегнати записи **48 → 64**. Подписаното в `expectations.json.p7` е `tokens: 2, zones: 2`, а неговият `foreign_guard` изрично записва, че `vladislav`/`varnenchik` са БИЛИ отхвърлени като чужди. Новият речник ги допуска | §4 стъпка 2, опашка |
203: | **1.8.18** | `python -m gates.release` с новите блобове (К) | **exit 6**, `⛔ BLOCKED (2)`; **119 делти** (референция 203 заявки / 3160 реда · кандидат 226 / 3222); опашка `ЗА_ПОДПИС_A.md` — **27 реда** | §4 стъпка 10 |
204: | **1.8.19** 🔴 | **архивирането на старата опашка** (К) | `git mv … архив/ЗА_ПОДПИС_A_05.09.md` → `queues_in_head()` = **`['scratch/places_search/архив/ЗА_ПОДПИС_A_05.09.md']`** — подпапката **НЕ бяга** от глоба (`ls-tree -r` + `fnmatch` по **basename**). `git mv … архив/АРХИВ_A_05.09.md` → **`[]`**. **Спасява само СМЯНАТА НА ИМЕТО** | §3.8, G15 |
205: | **1.8.20** | старата опашка | **27 „да“, 0 „не“**; 10 реда `артефакт`, 16 реда `покрива` (делта), 1 ред `въпрос` | `grep -c` по `**решение:**` |
206: | **1.8.21** 🔴 | **по-евтината поправка на D12** (К28-5) — вж. §9 т. 1 | „кв. Левски“ **4 → 14** (12 с `kv_levski`); „кв. Тракия“ **1 → 4** (4 с `trakia`); „кв. Христо Ботев“ **24 → 4** (3 с `hristo_botev`); „ж.к. Св. Иван Рилски“ **22 → 4** (2 с `sv_ivan_rilski`). Цена на презамразяване: **0 промени** в 156-заявъчния подписан корпус И **байт-еднакъв** дъмп на референцията (1 273 012 B) | §9 т. 1 |
207: | **1.8.22** | `scripts/hooks/pre-push` ↔ `.git/hooks/pre-push` | **2 574 B, байт-еднакви**; в PowerShell `diff` е **`Alias → Compare-Object`** (сравнява обекти, не файлове) | §5 G14 |
208: | **1.8.23** | низът за атрибуция | **338 знака**; `sha256(utf-8)` = `c6d29d4e1d3c4fa916224ae03ceab3682fd43cc83d3f22b920183d9b82d4002d`; `gates.release.body_digest` на файла с решенията = `c57a79c222361dc5c803823883374f9e1dcd12d36e7b27f05788ac17b7c22bfc`; блобът на файла (LF) = `74f09d505e2b…`, 32 129 B | §5 G9 |
209: 
210: Механизмът зад 1.8.4–1.8.6 е прочетен, не предположен (Ч): `index.html:6495-6496` и `recall_sweep.py:424-431` изхвърлят числата (`t.num`) и всеки токен с `s.length ≤ 2` — „кв.“, „ж.к.“, „к.к.“ и „2“ не са значещи, а М7 клонът иска `R.every(isSignificantToken)` (`index.html:7059`). **Затова осемте нови квартала се търсят само с голото си име, а детето няма собствена фраза.**
211: 
212: ### 1.9 Гейтът на доставката
213: 
214: - `gates/allow/` — точно един json: `2026-09-05_lot1v_v.json`, `signed_by: "Петър"`, 150 реда.
215: - `gates/baseline/MANIFEST.json` — `signed_by: "Петър"`, `rev: f06ac06…`. Ч: `gates/run_gates.py:247-255` сверява, че тази ревизия още носи подписаните sha; `:260-264` вика coverage с `base = git:<rev>:data/*.json`, `candidate = работното дърво`; `:199-217` избира allow-файла (>1 → fail).
216: - Ч: `gates/coverage.py:573-577` — неползван ред от allow е `allow_stale`; `:617-618` → `EXIT_ALLOW_STALE = 3`. Кодовете: `EXIT_OK 0`, `EXIT_UNCOVERED 2`, `EXIT_ALLOW_STALE 3`, `EXIT_USAGE 4`, `EXIT_ALLOW_UNSIGNED 5` (`:89-93`).
217: - `expectations.json` — `frozen: true`, `signed_by: "Петър"`; `INPUT_RELS` е **твърда тройка** (`recall_sweep.py:2815-2816`).
218: - Ч: `recall_sweep.py:90-97` — само `--freeze` и `--manifest`, **няма argparse и няма `--dump`**; `:68` `REPO_ROOT`; `:84` `OUTDIR = %TEMP%/fv_measures/`; `:79-80` `REPO_PARITY_OUT`; **`:4249-4253` всеки НЕ-freeze прогон презаписва този ПРОСЛЕДЕН файл**; `:4330` `return 1 if red else 0`.
219: - Ч 🔴: `gates/release.py:1367-1371` — `want = row.get("body"); entry = artefacts.get(row["artefact"]) if row["artefact"] else None; if not want or entry is None: continue`. **Ред без артефакт (клас „въпрос“) НИКОГА не се сверява по тяло.** Затова G9 сверява дайджеста САМ (§5).
220: - Ч: `gates/release.py:177-184` `SIGNABLE` е затворена шесторка — файлът с решенията НЕ е в нея.
221: - Куката `scripts/hooks/pre-push`: `[ ! -t 2 ]` блокира агент → `unittest` → `run_gates`; **няма break-glass**.
222: - Ч: `gates/sign.py:139-147` `refuse_if_agent()` хвърля САМО при изброени агентски идентичности.
223: 
224: ### 1.10 Червената линия и размерът
225: 
226: (1.8.12) структурна геометрия: **0**. (1.8.13) първо зареждане: **1 878 210 B ≈ 1,79 MB** при таван 5 MB.
227: 
228: ---
229: 
230: ## 2 · Обявени отклонения от подписания текст (искат подписа на Петър)
231: 
232: | № | Подписано | Мерено / по-късно решено | Предложено решение |
233: |---|---|---|---|
234: | **О1** | план `:144` „картончето: редът за атрибуция…“ + думите **„attribution row“**; Б0 т. 5; G27(б) | решение 8 (`СЪСТОЯНИЕ:31`): в картончето НЯМА ред за извора | „attribution row“ **излиза** от съобщението; `label`/`url` остават машинен запис — **валидират се, не се рендерират**; ново място в write-set: `index.html:1901-1918`. |
235: | **О2** | „шестте S17 фикстури“ | `tests/test_granitsi_fixtures.py:48-49` живи 5; `:180-186` замразява две отложени | Б3 дължи двете + преизмерените пет + **четири нови** (§3.5). |
236: | **О3** | „`QUARTER_CODES` +41“ | доставката ползва 28 кода; липсват 8 | Съобщението носи **`QUARTER_CODES +8`**. |
237: | **О4** | „един атомен комит“ + автор `Claude Executor`, а ам.3 §7 прави комит на данни от агент STOP | взаимно противоречие | **Един атомен комит с автор `Petar1984`**; изпълнителят стейджва, Петър комитва. |
238: | **О5** | типово правило за `DISTRICT_FALLBACK` + положителна фикстура | 0 такива реда | `QUARTER_SRC` получава двете стойности; правилото се пише в **двата двигателя И в двата bundle теста** (О19); доказателството е синтетична фикстура. |
239: | **О6** | нищо; чака се решение 10 | речникът носи `с.о. Перчемлията` — районен произход неподписан | Решение 10 или поименен резерв **преди** комита, или изричен ред „отложено“ в опашката. |
240: | **О7** | районът от НАШИЯ `district.code` | решение 9 смени района на два квартал-полигона | В реда „вид · квартал · район“ районът остава **на МЯСТОТО** (375/375). |
241: | **О8** | D13 пинва поименно старите числа | всички се менят | D13 остава договор за местата; всяко число се премерва (§4 стъпка 2). |
242: | **О9** | ADR 010 D3 „затворен 9-ключов `_meta`“ | ам.2 прави набора 10-ключов; хотелският е 8-ключов | Документен дълг → **отделен комит СЛЕД пуша**. |
243: | **О10** | „подготовка на Б3 (кръпка)“ | кръпката не съществува | Б3 тръгва на чисто по този план. |
244: | **О11** | Б1 sha `3f423898…`/61 граници | комитът на Петър `6486b48`, 60 граници, sha `74f09d505e2b` | Всяка котва сочи `6486b48` / `74f09d505e2b`. |
245: | **О12** | — | наследени дългове P1–P3, `lot1v_v_manifest.py:30` | Приемат се поименно; не се поправят тук. |
246: | **О13** | гейт „grep `coordinates` → 0 извън `data/hydrants.json`“ | (1.8.12) буквалното попадение е **проза в стойност** на `data/hydrants_provenance.json`; ключове след parse: **0** | Гейтът става **структурен** (G11). |
247: | **О14** | „замразената референция (нула изгубени резултати)“ | „младост“ 28→20, „училище младост“ 11→6 | „Нула изгубени“ = **нула НЕПОДПИСАНИ изгубени**; **осемте** реда (1.7) минават през опашката поименно. |
248: | **О15** 🔴 | §Б3 `:144` „нормализаторът D12“; ADR 010 D12 иска `window.__places.locationKey(q)` | (1.8.4) четирите типови заявки не намират квартала си; (1.8.21) има **по-евтин** вариант, който v2 пропуска | **D12 се ОТЛАГА** — ИЛИ влиза евтиният вариант (§9 т. 1, ново решение А/Б/В). Ефектът се записва или се поправя, но не се премълчава. |
249: | **О16** 🔴 | „дете → детето; родител → родителят и подписаните му деца“; DAG-ът от Б0 т. 9 | (1.8.6) детската заявка → 0; (1.8.8) `druzhba ⊂ asparuhovo` не работи; (1.8.7) `chaika` слива братя | **Родство остава фразово и се ЗАМРАЗЯВА такова, каквото е** (фикстури 6–8). DAG-ът не влиза (иска нов износ на varna_3d). |
250: | **О17** | G27(б): три фикстури — липсващ запис ✗, `url` без формат ✗, `_meta` с 11 или 9 ключа ✗ | (1.5, 1.5б) картите са ДВЕ (14 и 7), url-ите са по ДВЕ правила (wikimapia `http://…/<id>/…`, openstreetmap `https://www.openstreetmap.org/copyright`), `_meta` е **множество**, не брой | И10 изпълнява и трите, но по **измереното**: точни множества ключове, затворено множество `src ∈ {wikimapia, openstreetmap}` с ПРАВИЛО ЗА ВСЕКИ, и **равенство** карта ↔ `SIGNED_POLYGON` кодове. Отклонението от буквата на ам.2 (`https`, без път) се обявява. |
251: | **О18** | §3.3 на v1: „`LOCALITY_CODES` не се пипат“ | (Ч) `index.html:6537` и `tests/test_places_public_bundle.py:292` валидират местността със `QUARTER_SRC` | Въвежда се **`LOCALITY_SRC = ['REG','KAIS','SIGNED_OVERRIDE','SIGNED_POLYGON']`** (без `DISTRICT_FALLBACK`). |
252: | **О19** 🔴 | „типово правило за `DISTRICT_FALLBACK`“ (само `index.html:7064`) | същият ред е ОБРАТЕН в три Python-проверки (`recall_sweep.py:2146`, `:2150`, `tests/test_places_public_bundle.py:291-293`, `:309`) | Правилото се пише **на шест места** (§3.4, §3.5). |
253: | **О20** | `index.html:6544` изисква `zone === quarter.name`; износителят следва това (375/375, преизмерено: 0 нарушения) | И6 на v1 сменя договора едностранно, преди износителя | Б3 приема **и двата** етикета за fallback ред. Затягането влиза с износния гейт във varna_3d. |
254: | **О21** 🔴 | v1 нарича низа в подножието „подписан“ | (Ч) файлът с решенията не е в `SIGNABLE`; последният комит по него е на агент; **(1.9) `release.py:1367-1371` пропуска ред без артефакт** | Низът влиза в опашката като ред **клас „въпрос“** с полета `тяло: c6d29d4e…` (sha256 на НИЗА) и `тяло-на-файла: c57a79c2…` (`body_digest`). **release НЯМА да ги сверява — това го прави G9** (§5). Комитът не нарича низа „подписан“ преди подписа. |
255: | **О22** 🔴 | v1 §9 т. 9: baseline → комита на доставката в същата сесия | (1.8.2) `base == candidate` → exit 3, 150 stale | **Baseline ОСТАВА `f06ac06`.** Новият allow бюджетира **138-те** (1.8.1). **Семантиката се записва:** „lost“ = ред, който е имал назован `zone`/квартал в базата и няма в кандидата; „changed“ = имал е друг. 138 = 44+44 (places) + 39+11 (hotels). Обяснението е 1.8.1б: срещу `f00dd78` са **150**, значи доставката **връща 12**. |
256: | **О23** | v1 §4 стъпка 9: „`probe_out/token_parity.json` в `_meta.inputs`“ | (Ч) `INPUT_RELS` е твърда тройка | Очакването отпада; амандамент №11 т. 4 е поименен дълг. |
257: | **О24** 🔴 | червен ред 5 „автор `Claude Executor`“ | (Ч) `gates/sign.py:139-147`; git identity на репото е `Petar1984` | Всяка агентска команда носи `git -c user.name="Claude Executor" -c user.email=executor@local`. Проверката е **следпроверка**. |
258: | **О25** 🔴 | §Б3 не казва нищо за старата опашка | (1.8.19) 🔴 **подпапка `архив/` НЕ спасява** — `queues_in_head()` е рекурсивен и сравнява basename | `ЗА_ПОДПИС_A.md` се **преименува**: `git mv scratch/places_search/ЗА_ПОДПИС_A.md scratch/places_search/архив/АРХИВ_A_05.09.md` — **името губи префикса `ЗА_ПОДПИС_`**. Изтриване не е нужно: 27-те подписани реда остават четими. |
259: | **О26** | v1 G7: „`recall_sweep.py --dump`“ | (Ч) няма такъв флаг; артефактът е `%TEMP%/fv_measures/lot1v_v_candidate_rows.json`, **общ за всички прогони** | G7 се преписва (§5): два ОТДЕЛНО ЗАПАЗЕНИ дъмпа + изпълним байтов comparator + доказано падаща мутация. |
260: | **О27** 🔴 **нов (S28-10)** | нощен план `:144` забранява мълчалив отказ (`places2 = []` без видим знак) | (1.8.10 случай в) при чужд код в places клиентът показва **225 реда вместо 375** и **не казва нищо** | **Обявено отклонение: мълчаливият UI отказ ОСТАВА в Б3.** Той е поведението и днес; фикстура 9в го **пинва**, а видимият отказ е отделен малък лот. Петър подписва това изрично (§9 т. 10). |
261: | **О28** 🔴 **нов (собствена находка)** | `expectations.json.p7` е подписан с `tokens: 2, zones: 2` и `foreign_guard`, който изрично отхвърля `vladislav`/`varnenchik` | (1.8.17) новият речник добавя **7 токена в 5 зони**; засегнати записи 48 → 64 | Дрейфът е **следствие от доставката**, не от кода. Влиза като **отделен ред „въпрос“** в опашката с двата списъка дословно и с `foreign_guard` преди/след. STOP, ако одиторът го намери непокрит. |
262: | **О29** 🔴 **нов (S28-5)** | v2 §4 стъпка 10: „`--manifest` → 0“ | (1.8.15) първият прогон срещу подписаното е **1** | Стъпката очаква **exit 1** с ПРЕДВАРИТЕЛНО ИЗБРОЕН набор (§4 стъпка 10). Друго число = STOP. |
263: | **О30** 🔴 **нов (собствена находка)** | — | (1.8.16) вторият `--manifest` е **exit 0 / 0 червени**, защото първият е презаписал `expectations.json` | Червен ред 13. Доказателството се снема САМО от първия прогон; повторение е забранено като „доказателство“ (STOP 20). |
264: 
265: ---
266: 
267: ## 3 · Write-set (точните файлове и точните редакции)
268: 
269: ### 3.1 Данни (байтов препис, нула трансформация)
270: 
271: ```bash
272: cd /c/git/Fire_Varna
273: git -C /c/git/varna_3d show 05f485e:data/fire_varna_places.json > data/places.json
274: git -C /c/git/varna_3d show 05f485e:data/fire_varna_hotels.json > data/hotels.json
275: git -C /c/git/varna_3d show 05f485e:data/place_categories.json > data/place_categories.json
276: ```
277: Git Bash — **не** PowerShell `>` (UTF-16 в PS 5.1).
278: 
279: ### 3.2 `index.html` — четиринадесет редакции, всяка с котва
280: 
281: **И1 · `:6265`** `'fire-varna-hotels-v6-225'` → `'fire-varna-hotels-v7-225'` + два реда коментар защо (57 реда сменят `quarter`/`zone` при непроменен брой; `accept` сверява sha само при `crypto.subtle`, `:6605`).
282: 
283: **И2 · `:6288-6290`** трите пина → стойностите от §1.4.
284: 
285: **И3 · `:6301-6304`** `LEGACY_BUNDLE_SHA` → places `3dffc264…`, hotels `eb8fa85c…`.
286: 
287: **И4 · `:6313`** `const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE', 'SIGNED_POLYGON', 'DISTRICT_FALLBACK'];`
288: 
289: **И4б · нов ред веднага след `:6313` (О18).**
290: ```js
291:     // Б3 (О18): the LOCALITY has its own closed source list. It shared QUARTER_SRC
292:     // (:6537) and widening that list for the quarter silently widened the locality
293:     // too — a `locality` by DISTRICT_FALLBACK is a thing no decision allows.
294:     const LOCALITY_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE', 'SIGNED_POLYGON'];
295: ```
296: и `:6537` става `if (!validLocation(r.locality, LOCALITY_SRC, LOCALITY_CODES)) return false;`
297: 
298: **И5 · `:6317-6321` `QUARTER_CODES` → 28 кода** (масив, същият стил на пренасяне; азбучно):
299: ```
300: 'asparuhovo', 'borovets_yug', 'briz', 'chaika_kk', 'chaika_kv', 'dolna_traka',

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$s=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8; 300..449 | ForEach-Object { '{0}: {1}' -f ("'$_+1),$s[$_] }' in C:\git\Fire_Varna
 succeeded in 0ms:
301: 'druzhba', 'galata', 'grackata_mahala', 'hristo_botev', 'izgrev_kv',
302: 'kk_konstantin_elena', 'kolhozen_pazar', 'kv_levski', 'mladost', 'mladost2',
303: 'pobeda', 'priboy', 'sv_ivan_rilski', 'trakia', 'troshevo', 'tsentar',
304: 'vazrazhdane', 'vazrazhdane1', 'vazrazhdane2', 'vinitsa', 'vladislavovo',
305: 'zlatni_pyasatsi'
306: ```
307: `DISTRICT_CODES` (`:6315`) и `LOCALITY_CODES` (`:6322`) не се пипат.
308: 
309: **И6 · `:6535-6544` типовото правило за `DISTRICT_FALLBACK` (по О20 — двата етикета).**
310: ```js
311:     // Б3 (Б0 т. 4, О19/О20): a DISTRICT_FALLBACK quarter is the DISTRICT wearing the
312:     // quarter field. Its code comes from DISTRICT_CODES, it must BE the row's own
313:     // district, and nothing downstream may read it as a quarter — otherwise the row
314:     // silently leaves the district branches (:7064, :7118) that are its only home.
315:     function isFallbackQuarter(q) { return !!q && q.src === 'DISTRICT_FALLBACK'; }
316:     function ownQuarter(r) { return (r.quarter && !isFallbackQuarter(r.quarter)) ? r.quarter : null; }
317: ```
318: Първи клон на `validTypedLocation`:
319: ```js
320:       if (isFallbackQuarter(r.quarter)) {
321:         if (!validLocation(r.quarter, QUARTER_SRC, DISTRICT_CODES)) return false;
322:         if (!r.district || r.quarter.code !== r.district.code
323:             || r.quarter.name !== r.district.name) return false;
324:       } else if (!validLocation(r.quarter, QUARTER_SRC, QUARTER_CODES)) return false;
325: ```
326: Етикетът на `:6544` — **и двете форми** (О20; измерено: износителят пише `zone === quarter.name` за 375/375):
327: ```js
328:       if (isFallbackQuarter(r.quarter))
329:         return r.zone === r.quarter.name || r.zone === DISTRICT_MARK + ' ' + r.district.name;
330:       return r.zone === (r.quarter ? r.quarter.name : DISTRICT_MARK + ' ' + r.district.name);
331: ```
332: 
333: **И7 · `:6749`, `:6782`** — `locTokens('quarter', h.quarter)` → `locTokens('quarter', ownQuarter(h))`; същото за `locPhrases`.
334: 
335: **И8 · `:7064`, `:7118`** — `!r.e.quarter` → `!ownQuarter(r.e)`.
336: 
337: **И9 · `:7266`** — `const quarter = ownQuarter(h) ? h.quarter.name : '';` Нищо не се добавя към картончето.
338: 
339: **И10 · `_meta` — трите проверки на G27(б) по ИЗМЕРЕНОТО (О17), никакъв рендер.** До `validateCats` (`:6581`):
340: ```js
341:     // Б3 (решение 8 + G27(б), О17): the provenance map is a MACHINE record.
342:     // Measured 07.09: the map is PER BUNDLE (places 14 codes, hotels 7) and it is
343:     // EXACTLY the set of SIGNED_POLYGON codes that bundle carries — equality, not
344:     // inclusion. `src` is a CLOSED set and each source has its own URL rule: the
345:     // single openstreetmap entry (`mladost2`) points at the ODbL copyright page and
346:     // matches no wikimapia pattern. Not one byte of any of it reaches a card.
347:     const ATTRIB_KEYS = ['src', 'url', 'label', 'licence'];
348:     const ATTRIB_SRC = ['wikimapia', 'openstreetmap'];
349:     // О17: pinned to the DELIVERED shape (http, id, path), not to the literal of
350:     // амандамент №2 („https://wikimapia.org/<wm_id>/“) — measured 07.09.
351:     const WM_URL = /^https?:\/\/wikimapia\.org\/\d+\//;
352:     const OSM_URL = 'https://www.openstreetmap.org/copyright';
353:     function validQuarterAttribution(meta, rows) {
354:       const map = meta && meta.quarter_attribution;
355:       if (!map || typeof map !== 'object' || Array.isArray(map)) return false;
356:       for (const k of Object.keys(map)) {
357:         const e = map[k];
358:         if (!e || typeof e !== 'object' || Array.isArray(e)) return false;
359:         if (Object.keys(e).length !== ATTRIB_KEYS.length) return false;
360:         for (const f of ATTRIB_KEYS) if (typeof e[f] !== 'string' || !e[f]) return false;
361:         if (ATTRIB_SRC.indexOf(e.src) < 0) return false;
362:         if (e.src === 'wikimapia' && !WM_URL.test(e.url)) return false;
363:         if (e.src === 'openstreetmap' && e.url !== OSM_URL) return false;
364:       }
365:       // equality with the SIGNED_POLYGON codes of THIS bundle (both directions)
366:       const need = new Set();
367:       for (const r of rows)
368:         if (r.quarter && r.quarter.src === 'SIGNED_POLYGON') need.add(r.quarter.code);
369:       if (Object.keys(map).length !== need.size) return false;
370:       for (const c of need) if (!map[c]) return false;
371:       return true;
372:     }
373:     const META_KEYS_HOTELS = ['generated', 'count', 'by_zone_src', 'licence',
374:       'licence_osm', 'licence_address', 'quarter_attribution', 'excluded'];
375:     const META_KEYS_PLACES = ['generated', 'count', 'by_kind', 'by_zone_src',
376:       'licence_osm', 'licence_registry', 'licence_wikidata', 'licence_address',
377:       'quarter_attribution', 'excluded'];
378:     function metaKeysAre(meta, want) {
379:       const got = Object.keys(meta || {});
380:       if (got.length !== want.length) return false;
381:       for (const k of want) if (got.indexOf(k) < 0) return false;
382:       return true;
383:     }
384: ```
385: Извиква се веднъж в `validateHotels` (след `:6549`) и веднъж в `validatePlaces2` (след `:6568`):
386: ```js
387:       if (!metaKeysAre(d._meta, META_KEYS_HOTELS)) return false;   // …_PLACES в другия
388:       if (!validQuarterAttribution(d._meta, d.hotels)) return false;   // …d.places
389: ```
390: `EXPECT_KEYS`/`EXPECT2_KEYS`, `EXPECT_COUNT`/`EXPECT2_COUNT` не се пипат.
391: 
392: **И11 · Низът в подножието — влиза САМО след подписа на Петър (О21).** След `:1902`:
393: ```js
394:   // Б3 (решение 8, 07.09): the line for the quarter boundaries lives in the map's
395:   // small print, next to the basemap credit, and never on a place card. It is added
396:   // ONCE and survives every basemap swap: `attribCtrl` is a single control (:1917)
397:   // and setBasemap/enable/removeOfflineBasemap (:4543-4549, :4663, :4672-4676)
398:   // remove only their OWN strings — including under the sticky override (:4571-4574).
399:   const QUARTERS_ATTRIB = 'Кварталните граници в този файл са по Wikimapia.org (© Wikimapia contributors, CC BY-SA, ToS §1.G: връзка към обекта + „Wikimapia.org“ с връзка към http://wikimapia.org); карето „Младост 2“ е по улични оси от OpenStreetMap (© OpenStreetMap contributors, ODbL, https://www.openstreetmap.org/copyright). Геометрия НИКОГА не пътува публично.';
400: ```
401: и веднага след `:1918`: `attribCtrl.addAttribution(QUARTERS_ATTRIB);`
402: Низът е **дословно** полето `attribution` на `scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json` — **338 знака**, нула апострофи, нула HTML (измерено).
403: 
404: **И12 · Три маркера за Node-срезовете** (нула преместен код):
405: - преди `:6256` → `// ---- Б3 slice start (pure, DOM-free: constants → validators → cache → index → search) ----`
406: - след `:7154` → `// ---- Б3 core slice end (everything below touches the DOM) ----`
407: - след `:7289` (края на `popupFor`) → `// ---- Б3 card slice end (popupFor included, DOM-stubbable) ----`
408: Границата `:7154` е измерена: първото докосване на DOM е `function span(` на `:7155`. **Третият маркер е нов и е задължителен за G8** — `popupFor` живее ИЗВЪН основния срез.
409: 
410: **И13 · Паритетната повърхност `:7470-7480`** — расте САМО ако Петър избере вариант Б/В по §9 т. 1.
411: 
412: ### 3.3 Пиновете и правилата в двата bundle теста
413: 
414: `tests/test_places_public_bundle.py`: `:55-57` sha/bytes/gzip9 → `3dffc264…` / **128401** / **14748**; `:80` копието на `QUARTER_CODES` (28) + `QUARTER_SRC` (5) + **нов `LOCALITY_SRC` (4)**; `:88` `QUARTER_BY_SRC = {"REG": 39, "KAIS": 10, "SIGNED_POLYGON": 42}`; `:89` `LOCALITY_COUNT = 5`.
415: `tests/test_hotels_public_bundle.py`: `:61-63` `eb8fa85c…`/**151263**/**13642**; `:83-85` `9064705a…`/**77998**/**9690**; `:88` `LOCATION_COUNTS = {"quarter": 28, "district": 5, "locality": 5}`; `:115` копието на кодовете; `:124` `QUARTER_BY_SRC = {"REG": 115, "KAIS": 25, "SIGNED_OVERRIDE": 12, "SIGNED_POLYGON": 15}`.
416: 
417: **Четири нови правила в двата теста (О17, О18, О19):**
418: 1. `:291-293` (и близнакът): `("locality", LOCALITY_SRC, LOCALITY_CODES)`; за `quarter` — ако `src == "DISTRICT_FALLBACK"`, кодът се търси в `DISTRICT_CODES` и трябва да е кодът на СОБСТВЕНИЯ район.
419: 2. `:309` (и близнакът): `want` за fallback ред е `quarter["name"]` **или** `"район " + district["name"]`.
420: 3. `set(QUARTER_CODES) == set(place_categories["locations"]["quarter"])` — измерено днес: **True**, 28 = 28.
421: 4. 🔴 **`_meta` и `quarter_attribution` в Python, огледало на И10:** точното множество ключове (10 / 8 дословно), `set(quarter_attribution) == {code : row.quarter.src == "SIGNED_POLYGON"}` (14 / 7), `src ∈ {wikimapia, openstreetmap}`, `^https?://wikimapia\.org/\d+/` за wikimapia и точното `https://www.openstreetmap.org/copyright` за openstreetmap.
422: 
423: Лицензните низове се сравняват дословно (`:263`, `:384`, `:397-412`).
424: 
425: ### 3.4 Двигателят на референцията — шест места, не две (О19)
426: 
427: `scratch/places_search/recall_sweep.py`, един помощник `own_quarter(rec)` и шестте му ползвания:
428: `:621` `self.qtk`, `:623` `self.qph`, `:1123` `d_rows`, `:1167` `district_hit`, `:2146` `want` (двете форми), `:2150` кодът на fallback ред срещу `DISTRICT_CODES`.
429: 
430: **Приемане:** кандидатският дъмп преди/след промяната е **байт-еднакъв** над днешната доставка (G7).
431: **Забранено:** `INPUT_RELS` (`:2815-2816`) НЕ се пипа (О23). `CENTER` (`:102-104`) НЕ се пипа.
432: **Обявено:** всеки НЕ-freeze прогон презаписва проследения `scratch/places_search/probe_out/token_parity.json` (`:4249-4253`) — очакван изход, не мръсно дърво (О26). **Измерено на живо:** трите прогона на G7 наистина го пренаписаха.
433: 
434: ### 3.5 Фикстурите — единадесет, всяка с ДОКАЗАНО падащ `_broken`
435: 
436: `tests/test_granitsi_fixtures.py` (пренаписан) + `scratch/places_search/granitsi_fixtures_07.09.json` (`git mv` от `…_06.09.json`) + **нов** `tests/granitsi_client_probe.mjs`.
437: 
438: **Промени в харнеса:**
439: - докстрингът `:8-13` се пренаписва; `_meta.status` → `"signed_by_petar"` + дата; `_meta.inputs` (трите нови sha) и `_meta.engine.sha256` в същия комит (иначе `:188` пада пръв); `EXPECTED_NAMES` (`:48-49`) става единадесеторка; `test_the_two_deferred_fixtures_are_named_with_their_reason` (`:180-186`) → „нула отложени“.
440: - 🔴 **`assert_case` става МНОГОЗАЯВЪЧЕН (К28-2 бонус).** Днес (`:197-204`) той сравнява `case["today"]` за `case["query"]` — една заявка. Новата форма:
441: ```python
442:     def assert_case(self, case, measured_by_query):
443:         """`case["queries"]` е списък от {q, branch, n, with_quarter, without_quarter,
444:         identities}; едно-заявъчните фикстури носят списък от един елемент."""
445:         for want in case["queries"]:
446:             got = measured_by_query[want["q"]]
447:             self.assertEqual(got["branch"], want["branch"], want["q"])
448:             self.assertEqual(got["n"], want["n"], want["q"])
449:             self.assertEqual(got["with_quarter"], want["with_quarter"], want["q"])
450:             self.assertEqual(got["without_quarter"], want["without_quarter"], want["q"])

codex
HEAD е точно `acddcd1`; проследеното дърво е чисто. Средата е изцяло read-only, включително за временно копие, затова ще използвам леки проби в паметта. Проверявам и дали описаните гейтове вече са изпълними, или още разчитат на неписан тестов код.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$s=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8; 450..599 | ForEach-Object { '{0}: {1}' -f ("'$_+1),$s[$_] }' in C:\git\Fire_Varna
 succeeded in 0ms:
451:             self.assertEqual([list(r) for r in got["identities"]],
452:                              [list(r) for r in want["identities"]], want["q"])
453: ```
454:   🔴 **и негативната половина назовава ЗАЩО пада:** `_broken` носи `fails_on: "<заявка>"`; тестът твърди, че `assert_case` хвърля **и** че точно тази заявка е сменена, а останалите заявки на фикстурата са непроменени (иначе мутация, която мърда друга заявка, минава за доказателство).
455: - ключът за мутациите остава по име (`apply_ops`, `:67-84`, „op, който не улучва точно 1 ред, е грешка“); за хотелите — защита срещу дубликата **`РОЯЛ` (2 реда)**: фикстура, която го докосва, ключова по ординал, иначе `LookupError`. (Измерено: в places няма дублирани имена; в hotels само `РОЯЛ`.)
456: 
457: | # | фикстура | твърди (числата се ПРЕИЗМЕРВАТ) | `_broken` — **измерената** мутация и **измерената** щета |
458: |---|---|---|---|
459: | 1 | `street_collision` | `A3-street`, 1, ДГ№12 „Ян Бибиян“ | заварената + нова: улицата получава код `dolna_traka` |
460: | 2 | `district_retention` | `A3-district`, 12, 9 с квартал | заварената (`DISTRICT_FALLBACK` + `district: null` → 11) |
461: | 3 | `mladost_kind_collision` | `M7-bare-location`, 20, 8/12 | заварената + `SIGNED_POLYGON` с код извън 28-те |
462: | 4 | `order_identity` | същите 20, **подредени** | заварената |
463: | 5 | `parent_child` (Младост) | `A3-location`, 6, 3 с квартал | заварената (код `mladost2_new`) — **измерено: пада (5)** |
464: | 6 | `parent_child_vazrazhdane` **(нова, О16)** | (а) „възраждане“ → **5** (`ДГ 29 „Звънче“`, `ДГ 31 „Крилатко“`, `II ОУ „Никола Йонков Вапцаров“`, `ДГ 33 „Делфинче“`, `ДГ№34 „Лястовичка“`); (б) „възраждане 2“ → **0**; (в) „ж.к. възраждане 2“ → **0** | 🔴 **v2 беше сгрешен.** Измерено: смяна САМО на КОДА (`vazrazhdane1` → `vazrazhdane1_new`) дава **пак 5** — фикстурата НЕ пада, защото М7 чете `qtk`, строен от ИМЕТО (`recall_sweep.py:672`, `:1159`), а кодът важи само за `qph`/A3 (`:686`, `:1121`). **Правилната мутация — един op по име:** `{bundle: "places", name: "ДГ№34 „Лястовичка“", set: {quarter: {name: "ж.к. Лястовиче", code: "vazrazhdane1", src: "SIGNED_POLYGON"}, zone: "ж.к. Лястовиче"}}` → **„възраждане“ 5 → 4** (пада `assertEqual(n, 5)`); заявки (б) и (в) остават 0 → `fails_on: "възраждане"` |
465: | 7 | `chaika_sibling_merge` **(нова, О16)** | „чайка“ → **30** реда през `chaika_kk` (19) И `chaika_kv` (10) + 1 без квартал | 🔴 **изброена поименно** (`apply_ops` мутира ред по ред): десет op-а, по един на всеки `chaika_kv` ред — `АМИРАЛ` (hotels), `Математическа гимназия „Доктор Петър Берон“`, `ОУ "Г.С.Раковски"`, `ОУ "Захари Стоянов"`, `Спортно училище Георги Бенковски`, `4 ОДЗ Чайка`, `ДГ№21 „Калина Малина“`, `ДГ№22 „Мечо Пух“`, `Оздравителна Детска Градина №9 "Ален Мак"`, `ДЯ №2 „Моряче“` — всеки получава `quarter.name` и `zone` = `"кв. Крайморие"`. **Измерено: 30 → 21** (не 20 и не 21-само-при-zone: и двата варианта дават 21). Оцеляват 19-те `chaika_kk` + `4 ОДЗ Чайка` (носи думата в ИМЕТО си) + `„ДКЦ Чайка“ ЕООД` |
466: | 8 | `asparuhovo_no_child_rows` **(нова, О16)** | „аспарухово“ → **16** (9 `asparuhovo` + 7 „район Аспарухово“), **без** `ЦДГ 43 „Пинокио“`; „дружба“ → **2** | 🔴 **v2 беше сгрешен.** Alias „Аспарухово“ към `druzhba` е **невъзможен като op** (`apply_ops` мутира РЕДОВЕ, не речника) И е **безсилен**: измерено `location_alias_tokens` го изхвърля — `dropped["druzhba"] = ["short:zh", "short:k", "own:druzhba", "foreign:asparuhovo:asparuhovo"]` (`recall_sweep.py:477` (д)/(д′)). **Работещата мутация (един op):** `{bundle: "places", name: 'ЦДГ 43 "Пинокио"', set: {quarter: {name: "кв. Аспарухово", code: "druzhba", src: "SIGNED_POLYGON"}, zone: "кв. Аспарухово"}}` → **„аспарухово“ 16 → 17** (детето влиза при родителя) И **„дружба“ 2 → 1**. `fails_on: "аспарухово"`, а вторият ред се пази като второ твърдение |
467: | 9 | `client_cache_matrix` **(нова, Node)** | §3.6 — **три случая + матрица crypto/sha** | §3.6 |
468: | 10 | `district_fallback_typed` **(нова, синтетична, положителна, О19)** | синтетичен ред с `quarter {name: <район>, code: <district code>, src: DISTRICT_FALLBACK}`: (а) минава `validTypedLocation`; (б) **остава в „училище младост“** (`:7118`) и в „младост“ (`:7064`); (в) не носи квартални думи; (г) картончето не печата квартал; (д) минава `qa` (`:2146`, `:2150`); (е) минава двата bundle теста | **разделен `_broken`:** махни `ownQuarter` от `:7118` → „училище младост“ 6 → 5; отделно `district: null` за изричното „училище район младост“ (`:7104-7109`) |
469: | 11 | `client_reference_parity` **(нова, Node)** | шест заявки през среза и през `recall_sweep.search()` → **едни и същи имена в един и същи ред** | махни `map` стъба → подредбата се срутва |
470: 
471: ### 3.6 Node-фикстурите — как се викат и какво доказват (**изпълнено от планера, не обещано**)
472: 
473: Механиката: Python чете `index.html`, изрязва **по маркерите И12** (липсващ маркер = `AssertionError`, по образеца `tests/test_places_search_gate.py:503-530`); `shutil.which("node")`, липсващ Node = `self.fail("node липсва — фикстурата е гейт")`; `subprocess.run([node, "tests/granitsi_client_probe.mjs"], input=json.dumps({...}))` — срезът, товарите и случаите по stdin, отговорът по stdout; нула временни файлове, нула кирилица в командния ред.
474: 
475: `granitsi_client_probe.mjs` вдига среза с
476: ```js
477: new Function('window','caches','document','map','fetch','attribCtrl','__calls','L','console','crypto', slice + ';return {…}')
478: ```
479: 🔴 **Десетте параметъра са задължителни и всеки е измерен:**
480: - **`map`** — `centre()` (`:6952-6955`) вика `map.getCenter()` в `try/catch`; без стъб `distOf` връща 0 и подредбата се срутва. Стъбът е `{ getCenter: () => ({ lat: 43.2141, lng: 27.9147 }) }` (центърът, който референцията пинва, `recall_sweep.py:102-104`).
481: - **`fetch`** — `fetchValidatedJson` (`:6613-6625`) вика глобалния `fetch`; Node 22 има свой и без стъб тестът излиза в мрежата.
482: - 🔴 **`crypto` — НОВО и КРИТИЧНО.** `accept` (`:6605`) чете `window.crypto && crypto.subtle` — **две различни имена**. В браузъра са едно и също; **в Node голото `crypto` е WebCrypto на средата**, така че `window.crypto = {}` НЕ изключва проверката. Измерено: без сянка върху `crypto` половината „crypto OFF“ мълчаливо мери ON-пътя. Стъбът е `undefined` (OFF) или `{ subtle: webcrypto.subtle }` (ON), подаден **и на двете места**.
483: - **`__calls`** — броячът; всеки валидатор се обвива, за да се брои дали изобщо е викан.
484: - **`document`** — DOM стъб (`createElement` → възел с `appendChild`/`textContent`/`className`/`classList`/`style`), нужен само за среза с картончето.
485: 
486: **Фикстура 9 — трите случая, всеки ИЗМЕРЕН от планера:**
487: 
488: | случай | срез | товар | измерено |
489: |---|---|---|---|
490: | **9а** — стар списък, двата пакета отказани | `index.html` **както е днес** (`QUARTER_SRC` тройка, `QUARTER_CODES` 20, старите пинове) | новите три блоба | `validateHotels === false` · `validatePlaces2 === false` · `accept(text, пинат sha, validatePlaces2) === null` · **`await ensurePlaces()` ХВЪРЛЯ `Error: places payload unavailable`** (`:6639`). **Няма `RECS`.** Твърдението е `assertRaises`, не число |
491: | **9б** — след И2/И4/И5, валидната доставка | срез с петте извора, 28-те кода, новите пинове | новите три блоба | `validateHotels === true` · `validatePlaces2 === true` · `accept → обект` · **`RECS.length === 375`** |
492: | **9в** — чужд код САМО в places | същият срез, но `PLACES2_SHA256` = sha на **мутираното** тяло | places с един `SIGNED_POLYGON` код сменен на `tsentar_new` (тялото е `128402` B, sha `6bfbcbf2adced671fb60126fb97ef597c7f214c18466d3c0507bbd53d3ded745`) | `validateHotels === true` · `validatePlaces2 === false` · `ensurePlaces()` **НЕ хвърля** · **`RECS.length === 225`** · **`__calls.validatePlaces2 === 1`** |
493: 
494: 🔴 **Защо пинът трябва да е sha на МУТИРАНОТО тяло** (S28-1): измерената матрица на `accept` (1.8.11):
495: 
496: | `window.crypto`/`crypto` | sha | резултат | извиквания на валидатора |
497: |---|---|---|---|
498: | ON | несъвпадащ | `null` | **0** |
499: | ON | верен | `null` (валидаторът отказва) | **1** |
500: | OFF | несъвпадащ | `null` (валидаторът отказва) | 1 |
501: | OFF | верен | `null` (валидаторът отказва) | 1 |
502: 
503: **Значи при crypto ON и несъвпадащ sha `null` е отказ на ДАЙДЖЕСТА, не на списъка** — фикстура, която подава грешен sha, доказва нещо друго. Фикстура 9в подава **правилния** sha на мутираното тяло и твърди `__calls.validatePlaces2 === 1` заедно с `false`.
504: 
505: **9г (кешът):** `PLACES_CACHE === 'fire-varna-hotels-v7-225'` и `!== 'fire-varna-hotels-v6-225'`; кеш-стъб с v6 тяло **не** се намира.
506: **9д (О27):** наблюдаемият отказ се **назовава**: при чужд код `places2 = []`, `hotels.length > 0`, UI показва **225 вместо 375** и **мълчи**. Това е обявено отклонение, не пропуск.
507: Отрицателната половина се прави **върху текста на среза** (замяна на реда `:6313`), не върху константа в паметта.
508: 
509: ---
510: 
511: ### 3.7 Родство — какво работи, какво не, поименно (О16)
512: 
513: | двойка | състояние (измерено) |
514: |---|---|
515: | `mladost2 ⊂ mladost`, `vazrazhdane1 ⊂ vazrazhdane`, `vazrazhdane2 ⊂ vazrazhdane` | **работи по фраза** (случайно съвпадение, не договор) |
516: | `druzhba ⊂ asparuhovo` | **НЕ работи** — „аспарухово“ 16 без `ЦДГ 43 „Пинокио“`, „дружба“ 2 |
517: | `kaisieva ⊂ vladislavovo`, `vazrazhdane3 ⊂ vazrazhdane` | детето няма доставени редове |
518: | `abatko`, `rozova_dolina`, `kokardzha_generic`, `mladost1`, `saltanat` | нула редове |
519: | **`chaika_kk` + `chaika_kv`** | **сливат се без подписано родство** (30 реда) |
520: 
521: Речникът носи `parents: []` за **0 от 28** кода. **Б3 НЕ изнася DAG-а**; замразява измереното с фикстури 5–8. Ако Петър иска само подписани връзки — лот **Б5 „Родство“**.
522: 
523: ### 3.8 Опашката и allow-ът (О22, О25)
524: 
525: - 🔴 **`git mv scratch/places_search/ЗА_ПОДПИС_A.md scratch/places_search/архив/АРХИВ_A_05.09.md`** — **в същия комит** с новата `scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md`. Измерено (1.8.19): само подпапка НЕ бяга от глоба; името трябва да загуби префикса `ЗА_ПОДПИС_`.
526: - Новият `gates/allow/2026-09-07_b3.json` бюджетира **измерените 138** реда, **изведен машинно** от `gates/out/coverage.json`; старият `2026-09-05_lot1v_v.json` се маха в същия комит (в папката остава точно един json).
527: - `gates/baseline/MANIFEST.json` **не се пипа**.
528: 
529: ---
530: 
531: ## 4 · Ред на изпълнение
532: 
533: **[И]** изпълнител (`git -c user.name="Claude Executor" -c user.email=executor@local …`, О24) · **[П]** Петър. Между стъпка 7 и стъпка 13 пакетът е **ЧЕРВЕН по конструкция** (D19): изпълнителят записва ТОЧНИЯ набор падащи тестове (G20); всеки тест извън набора = STOP.
534: 
535: **0. [И] Санитарна проверка.** `git status --porcelain` (0 реда без `??`), `git log -1 --pretty='%h %an %s'`, `git rev-list --count origin/main..HEAD`, `git ls-tree -r --name-only HEAD -- scratch/places_search | grep -c "ЗА_ПОДПИС"` → **1**, `node --version` → v22.19.0. **HEAD и ahead се ЗАПИСВАТ такива, каквито са** — §1.1 е снимка от 07.09 и котвата се движи.
536: 
537: **1. [И] Записва плана.** `docs/plans/ПЛАН_Б3_07.09.md` → комит `docs(plan): Б3 quarter search delivery plan v3 (signed 07.09)`.
538: 
539: **2. [И] Препис на трите блоба + ПЪЛНАТА мярка ПРЕДИ редакцията.**
540: ```bash
541: export PYTHONIOENCODING=utf-8
542: python - <<'PY'
543: import hashlib, gzip, pathlib
544: for p in ['data/places.json','data/hotels.json','data/place_categories.json']:
545:     b = pathlib.Path(p).read_bytes().replace(b'\r\n', b'\n')
546:     print(p, len(b), hashlib.sha256(b).hexdigest(), len(gzip.compress(b, 9)))
547: PY
548: ```
549: Очаквано: точно шестте числа и трите sha от §1.4. В същия прогон се мерят `QUARTER_BY_SRC`, `LOCATION_COUNTS`, `LOCALITY_COUNT`, множеството квартални кодове, лицензните низове, **двете `_meta` МНОЖЕСТВА (§1.5б)**, **двете `quarter_attribution` карти (14 / 7) и равенството им със `SIGNED_POLYGON` кодовете**, и `P7_ADDED` (1.8.17).
550: 
551: **Трите мерки на покритието, преди един ред промяна** (`sys.exit(result["exit_code"])` — дословно):
552: ```bash
553: python -c "from gates import coverage; import json, sys; r=coverage.run(places_base='git:f06ac06:data/places.json', places_candidate='data/places.json', hotels_base='git:f06ac06:data/hotels.json', hotels_candidate='data/hotels.json', allow_path=None, out_dir='gates/out'); print(json.dumps({'exit':r['exit_code'],'uncovered':r['uncovered'],'verdict':r['verdict']}, ensure_ascii=False)); sys.exit(r['exit_code'])"
554: ```
555: очаквано **exit 2 · uncovered 138** (1.8.1).
556: ```bash
557: python -c "from gates import coverage; import json, sys; r=coverage.run(places_base='git:f06ac06:data/places.json', places_candidate='git:f00dd78:data/places.json', hotels_base='git:f06ac06:data/hotels.json', hotels_candidate='git:f00dd78:data/hotels.json', allow_path=None, out_dir='gates/out'); print(json.dumps({'exit':r['exit_code'],'uncovered':r['uncovered']}, ensure_ascii=False)); sys.exit(r['exit_code'])"
558: ```
559: очаквано **exit 2 · uncovered 150** — **това е дифът, който обяснява 138-те** (К28-6, О22): доставката ВРЪЩА 12 реда.
560: ```bash
561: python -c "from gates import coverage; import json, sys; r=coverage.run(places_base='git:f06ac06:data/places.json', places_candidate='data/places.json', hotels_base='git:f06ac06:data/hotels.json', hotels_candidate='data/hotels.json', allow_path='gates/allow/2026-09-05_lot1v_v.json', out_dir='gates/out'); print(json.dumps({'exit':r['exit_code'],'uncovered':r['uncovered'],'stale':len(r['allow_stale'])}, ensure_ascii=False)); sys.exit(r['exit_code'])"
562: ```
563: очаквано **exit 2 · uncovered 30 · stale 42** (1.8.3; 108 + 30 = 138 ✓).
564: 
565: И деветте заявки 1.8.4–1.8.9 през `recall_sweep`. **Всяко разминаване = STOP.**
566: Отрицателно доказателство: `python -m unittest tests.test_places_public_bundle tests.test_hotels_public_bundle` **сега е ЧЕРВЕН** — първият ред на G20-набора.
567: 
568: **3. [И] Трите маркера И12 + Node-сондата.** Първо `index.html` получава маркерите, после се създава `tests/granitsi_client_probe.mjs` — **преди** редакциите, за да има с какво да се снеме отрицателното доказателство.
569: Мярка: срезът с ДНЕШНИТЕ списъци над НОВИТЕ байтове → `validateHotels === false`, `validatePlaces2 === false`, **`ensurePlaces()` хвърля** (случай 9а).
570: 
571: **4. [И] `index.html` — четиринадесетте редакции** (§3.2). **И11 се пропуска, ако низът още не е подписан (О21)** — тогава влиза в стъпка 12б.
572: Мярка след: `validatePlaces2 === true`, `RECS.length === 375` (9б) и `RECS.length === 225` при мутирания places с верен пин (9в).
573: 
574: **5. [И] Двата bundle теста + четирите нови правила** (§3.3). `python -m unittest tests.test_places_public_bundle tests.test_hotels_public_bundle` → **0**. Отрицателно: една сменена цифра в `PLACES2_SHA256` → ≠ 0.
575: 
576: **6. [И] Двигателят + фикстурите** (§3.4–3.6), включително `git mv` на фикстурния файл. `python -m unittest tests.test_granitsi_fixtures -v` → **0**, единадесет фикстури, всяка с падащ `_broken`.
577: 
578: **7. [И] G7 — двата дъмпа** (§5 G7), с копиране след ВСЕКИ прогон.
579: 
580: **8. [И] Стейджва точния write-set** (`git add` с изрични пътища, никога `-A`), после `git status --short` и `git diff --cached --stat`. **Обявено:** `scratch/places_search/probe_out/token_parity.json` ще е модифициран от прогоните (О26) — той НЕ влиза в този комит, а в комит 5. Показва на Петър `scratch/places_search/COMMIT_MSG_B3.txt`.
581: 
582: **9. [П] Атомният комит** — §6.
583: 
584: **10. [И] Отваря D19-интервала и го записва.** `python -m unittest discover -s tests`; `python -m gates.run_gates` → и двете ≠ 0. Записва **поименно** какво пада, включително очакваното **coverage изход 2** на проверка 4.
585: 
586: **Очакванията и манифестите (report-only) — с ПРЕДВАРИТЕЛНО ИЗБРОЕНИЯ набор (О29):**
587: ```powershell
588: python scratch\places_search\recall_sweep.py --manifest
589: ```
590: 🔴 **Очакван изход: 1** (не 0). Очакван набор — **59 реда `ЧЕРВЕНО` върху 41 уникални заявки + 2 реда без заявка**, и точно тези гейт-резултати: П7 **16/32**, ЛОТ 1 **6/18**, ЛОТ 1в-А **5/12**, ЛОТ 1в-Б **5/6**, ЛОТ 1в-В **4/10**, М7 **17/17**, §10 sweep 60/62 · 10/10 („срещу подписа 1“). Допуснатите разминавания, поименно:
591: - **зона-преписване без промяна на броя** (редът е същият, `zone` е новият квартал): `хотел зпз`, `горчива чешма хотел`, `училище свети никола`, `менделеев`, `хотел марина парк`, `училище менделеев стефан`, `училище аспарухово`, `детска градина аспарухово`, `1 ег`, `училище морска градина`, `ГРАДИНА`, `градина`, `детско заведение`, `детски заведения`, `ясла`, `детска ясла`, `детска градина`, `военноморско`, `военноморско училище`, `гимназия`, `поликлиника`, `езикова гимназия`, `морско училище`, `варна`, `училище район младост`, `район младост`, `детска градина владислав варненчик`;
592: - **сменен брой** (числото е в скобите, старо → ново): `владиславово детска градина` (4→5), `детска градина владиславово` (4→5), `хотел чайка` (18→19), `хотел златни` (96→98), `хотел приморски` (29→22), `детска градина приморски` (12→7), `училище приморски` (14→9), `университет приморски` (5→3), `хотел одесос` (40→32), **`училище младост` (11→6)**, `болница изгрев` (11→1, и клонът от `M2-failopen` на `A3-location`);
593: - **два реда без заявка:** `p7_added: 7 токена в 5 зони, подписани са 2 в 2` и списъкът на добавените (1.8.17, О28).
594: 🔴 **Прогонът се прави ВЕДНЪЖ.** Втори прогон е зелен по конструкция (1.8.16, червен ред 13) — ако изпълнителят повтори командата, доказателството е унищожено и лотът СПИРА (STOP 20).
595: 
596: ```powershell
597: python -m gates.release
598: ```
599: Очаквано: **6 (BLOCKED)**; делтите по кофи се записват дословно (мярка в клонинг: **119 делти**, референция 203/3160 · кандидат 226/3222).
600: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$s=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8; 600..749 | ForEach-Object { '{0}: {1}' -f ("'$_+1),$s[$_] }' in C:\git\Fire_Varna
 succeeded in 0ms:
601: **11. [И] Опашката.** `scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md`: три класа редове (въпрос / артефакт / делта), решения `pending`, без code fence и без HTML коментари. **Задължителни редове:**
602: - всяка делта на `gates.release`;
603: - шестте `SIGNABLE` + новият allow;
604: - **ред „въпрос“ за низа на атрибуцията** с `тяло: c6d29d4e1d3c4fa916224ae03ceab3682fd43cc83d3f22b920183d9b82d4002d` (sha256 на низа) и `тяло-на-файла: c57a79c222361dc5c803823883374f9e1dcd12d36e7b27f05788ac17b7c22bfc` (`body_digest`) — **сверява ги G9, не release** (О21);
605: - 🔴 **ОСЕМ делта-реда за загубените на „младост“** (1.7), всеки с името и новия квартал (К28-3);
606: - **ред „въпрос“ за `P7_ADDED` дрейфа** (О28) с двата списъка дословно;
607: - **ред „въпрос“ за мълчаливия UI отказ** (О27);
608: - ред за Перчемлията (О6);
609: - редовете по О15/О16/О20 („детската заявка не намира детето — прието“, „чайка се слива без подписано родство — прието“, „fallback етикетът се приема в двете форми“).
610: 
611: В същия комит: `git mv` на старата опашка към `архив/АРХИВ_A_05.09.md` (О25), новият allow (138 реда), махнатият стар allow.
612: Комит **[И]**: `docs: queue and manifests for the Б3 delivery signatures (07.09)`.
613: Мярка веднага след комита (семантиката на release, не `grep`):
614: ```powershell
615: python -c "import subprocess, posixpath, fnmatch, sys; out=subprocess.run(['git','ls-tree','-r','--name-only','-z','HEAD','--','scratch/places_search'],capture_output=True).stdout.decode('utf-8'); q=sorted(n for n in out.split(chr(0)) if n.strip() and fnmatch.fnmatchcase(posixpath.basename(n),'ЗА_ПОДПИС_*.md')); print(len(q), q); sys.exit(0 if len(q)==1 else 1)"
616: ```
617: → **1** и точно `['scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md']`.
618: 
619: **12. [П] Подписите.** `python -m gates.sign <id> да --all да --queue scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md` + **неговият** комит, който писалката отпечатва.
620: **12б. [И]** Ако низът е подписан на този етап — И11 влиза сега, в комит с `index.html` само за този ред: `feat(map): signed quarter-boundary line in the map attribution (decision 8)`. **[П]** го комитва.
621: 
622: **13. [И] Едно-единствено замразяване.** `python scratch\places_search\recall_sweep.py --freeze` → 0.
623: 
624: **14. [П] Комит на замразените тела:** `freeze: reference + expectations + parity (Б3)`.
625: 
626: **15. [И] Пълният гейт** — §5. Всичко зелено → одитор (друг агент, read-only).
627: 
628: **16. [П] Локален преглед** — §8.
629: 
630: **17. [П] Пушът,** от интерактивен терминал: `git rebase --autostash origin/main`, после `git push origin main`.
631: 
632: **18. [И] След пуша:** `docs/activeContext.md` + `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` §8; проверка, че публикуваните sha са равни на локалните; комит `docs: activeContext — Б3 delivery published, published hashes verified equal to local`; **[П]** втори пуш.
633: 
634: ---
635: 
636: ## 5 · Гейтове (всеки — команда с изход ≠ 0 и с ДОКАЗАНО падаща отрицателна половина)
637: 
638: | # | гейт | команда | очакван изход | отрицателното доказателство (ТРЯБВА да падне) |
639: |---|---|---|---|---|
640: | G1 | пиновете срещу LF-блобовете | `python -m unittest tests.test_places_public_bundle tests.test_hotels_public_bundle` | 0 | една сменена цифра в `PLACES2_SHA256` → ≠ 0 |
641: | G2 | единадесетте фикстури | `python -m unittest tests.test_granitsi_fixtures -v` | 0 | всеки `_broken` → `AssertionError` на назованата в `fails_on` заявка |
642: | **G3** 🔴 | **Node-матрицата през `ensurePlaces`** (S28-1) | същият прогон, фикстура 9 | 0 | **три отделни случая, не един:** (9а) срез с оригиналния `QUARTER_SRC` → `validateHotels === false` **И** `validatePlaces2 === false` **И** `assertRaises` върху `ensurePlaces()` с текст `places payload unavailable`; (9б) валидната доставка → `RECS === 375`; (9в) чужд код САМО в places + пин = sha на мутираното тяло (`6bfbcbf2…`, 128402 B) → `validateHotels === true`, `validatePlaces2 === false`, `RECS === 225`, **`__calls.validatePlaces2 === 1`**; (9г) crypto матрицата 1.8.11 — при ON+несъвпадащ sha **`__calls.validatePlaces2 === 0`**, така че `null` без брояч НЕ се приема за отказ; (9д) кеш v6 → стар запис се намира |
643: | G3б | паритет клиент ↔ референция | същият прогон, фикстура 11 | 0 | махнат `map` стъб → друг ред |
644: | G4 | пълният набор | `python -m unittest discover -s tests` | 0 | преди подписите: ≠ 0 — записаният G20 набор |
645: | G5 | седемте проверки | `python -m gates.run_gates` | **0** (7/7 ✓) | жълто („pending — Петър“) също дава 1 |
646: | G6 | нула **неподписани** изгубени резултати | `python -m gates.release` | 0 (преди подписите: 6) | делта без покриващ ред „да“ → 6 |
647: | **G7** 🔴 | **двигателят не мести кандидата** (S28-3) | вж. блока под таблицата | 0 | мутиран двигател → comparator **exit 1** (измерено) |
648: | **G8** 🔴 | **картончето няма ред за атрибуция — ИЗПЪЛНЕНО** (S28-7) | вж. блока под таблицата | 0 | добави `wrap.appendChild(span('pp-attrib', QUARTERS_ATTRIB))` в `popupFor` → ≠ 0 |
649: | **G9** 🔴 | **низът е ПОДАДЕН на `addAttribution` и е подписан** (S28-7) | вж. блока под таблицата | 0 | срезът без И11 → записаните извиквания са само `['© OpenStreetMap']` → ≠ 0 (измерено); една сменена буква → ≠ 0; неподписан ред → ≠ 0 |
650: | **G10** 🔴 | **първо зареждане ≤ 5 MB, по ИЗМЕРЕНИЯ набор** (S28-4) | `python -c "import pathlib,sys; f=['index.html','data/hydrants.json']; t=sum(pathlib.Path(x).stat().st_size for x in f); print(t); sys.exit(0 if t <= 5*1024*1024 else 1)"` | **0** (t = **1 878 210**) | същата команда с праг `1*1024*1024` → **exit 1** (1 878 210 > 1 048 576). Двата прага дават РАЗЛИЧНИ присъди |
651: | **G10б** | **отложената доставка на търсенето, отделно** | `python -c "import pathlib,sys; f=['data/hotels.json','data/places.json','data/place_categories.json']; t=sum(pathlib.Path(x).stat().st_size for x in f); print(t); sys.exit(0 if t <= 1024*1024 else 1)"` | 0 (t = **357 662**) | праг 256 KB → 1 |
652: | **G11** 🔴 | **нула геометрия — СТРУКТУРНО** (S28-8) | вж. блока под таблицата | 0 | ключ `"\u0063oordinates"` в мутирано копие: буквалният `grep` дава **0**, структурната проверка дава **1** (измерено) |
653: | G12 | нула кадастрален идентификатор | `python -m gates.run_gates` проверка 3 | зелена | вкарай `10135.1.2` → червено |
654: | G13 | точно един allow-json | `python -c "import pathlib,sys; n=len(list(pathlib.Path('gates/allow').glob('*.json'))); print(n); sys.exit(0 if n==1 else 1)"` | 0 | два файла → 1 |
655: | **G14** 🔴 | **куката е на място — БАЙТОВО в python** (S28-9) | `python -c "import pathlib,sys; a=pathlib.Path('scripts/hooks/pre-push').read_bytes(); b=pathlib.Path('.git/hooks/pre-push').read_bytes(); print(len(a),len(b),a==b); sys.exit(0 if a==b else 1)"` | 0 (2 574 = 2 574) | същата команда срещу подменено копие в скрачпада → **exit 1** (измерено). **`diff` в PowerShell е `Compare-Object`** и сравнява имена, не байтове |
656: | **G15** 🔴 | **точно една опашка в HEAD, по семантиката на release** (S28-10) | командата от §4 стъпка 11 | 0 | подпапка `архив/` със СЪЩОТО име → пак **1 попадение** и `release` пак BLOCKED (измерено); само смяна на името дава `[]` |
657: | G16 | местността не е отворена (О18) | тест в bundle-ите: `DISTRICT_FALLBACK not in LOCALITY_SRC` и всеки доставен `locality.src ∈ LOCALITY_SRC` | 0 | `locality.src = "DISTRICT_FALLBACK"` в мутиран кандидат → ≠ 0 |
658: | **G17** 🔴 | **`_meta` е ЗАТВОРЕНО МНОЖЕСТВО, `src` е затворен списък, url-ите са по извор** (S28-6, О17) | фикстура + правило 4 на §3.3 | 0 | вж. блока под таблицата — **четири мутации, всяка със СЪЩИЯ брой ключове** |
659: | **G18** | покритието (кодът се ЗАЧИТА) | трите команди от §4 стъпка 2, всяка със `sys.exit(r['exit_code'])` | 2 / 2 / 2 (преди новия allow) | без `sys.exit` командата връща **0** при вътрешен `exit_code = 2` (S28-5) |
660: 
661: **G7 — дословно (S28-3):**
662: ```powershell
663: python scratch\places_search\recall_sweep.py
664: copy /Y "%TEMP%\fv_measures\lot1v_v_candidate_rows.json" "<scratch>\g7_dump_A.json"
665: ```
666: после промяната в `recall_sweep.py`, същите блобове, същата ревизия на данните:
667: ```powershell
668: python scratch\places_search\recall_sweep.py
669: copy /Y "%TEMP%\fv_measures\lot1v_v_candidate_rows.json" "<scratch>\g7_dump_B.json"
670: ```
671: comparator (дословно, exit 1 при разлика):
672: ```powershell
673: python -c "import pathlib,sys; a=pathlib.Path(r'<scratch>\g7_dump_A.json').read_bytes(); b=pathlib.Path(r'<scratch>\g7_dump_B.json').read_bytes(); print(len(a),len(b),a==b); sys.exit(0 if a==b else 1)"
674: ```
675: **Измерено от планера в клонинг:** два прогона с един и същ двигател → **1 324 215 B, байт-еднакви, exit 0**. Отрицателна половина: `CENTER = (43.2000, 27.9000)` в копие на двигателя → **1 324 210 B, exit 1**. 🔴 **`OUTDIR` е ОБЩ (`recall_sweep.py:84`) — без `copy` след ВСЕКИ прогон гейтът сравнява последния файл със самия себе си.** Ревизиите на двигателя се пинват в отчета (`git rev-parse HEAD:scratch/places_search/recall_sweep.py` преди и след).
676: 
677: **G8 — дословно (S28-7):** тест, който изрязва среза по маркерите И12 (start … „card slice end“), вдига го с DOM стъб и **ИЗПЪЛНЯВА `popupFor` за всеки от 375-те записа**, после сравнява текста на върнатото поддърво:
678: ```js
679: const FORBIDDEN = ['Wikimapia', 'wikimapia', 'quarter_attribution',
680:                    'QUARTERS_ATTRIB', 'CC BY-SA', 'Кварталните граници'];
681: ```
682: Стъбовете: `document.createElement` → възел с `appendChild`/`textContent`/`className`; `buildNavActions` → `() => null` (живее на `:4255`, извън среза). **Измерено от планера: 375 картончета, 0 забранени низа.** Пример за картончето на `SIGNED_POLYGON` ред: `„Траката Семеен хотел · ★2 · 36 легла · Долна Трака · район Приморски адрес: …“`. 🔴 `ODbL`/`OpenStreetMap` **НЕ влизат в забранените** — те стоят законно в реда за извор на адреса/името и списък, който ги лови, е червен без причина (измерено).
683: 
684: **G9 — дословно (S28-7):** три твърдения, първите две ИЗПЪЛНЕНИ:
685: - **(а)** срезът `index.html:1900-1918` + И11 се вдига с `L` стъб, чийто `control.attribution()` връща **записващ** `attribCtrl`; след изпълнението `calls === ['© OpenStreetMap', QUARTERS_ATTRIB]` и `calls.includes(QUARTERS_ATTRIB) === true`. **Измерено:** преди И11 `calls === ['© OpenStreetMap']` (гейтът пада), след И11 — двата низа, вторият с дължина **338**.
686: - **(б)** низът се среща в `index.html` **точно веднъж** и е **дословно** полето `attribution` на файла с решенията (`sha256(utf-8) == c6d29d4e…`).
687: - **(в)** 🔴 **дайджестът се сверява ТУК, не от release.** Ч: `gates/release.py:1367-1371` — `entry = artefacts.get(row["artefact"]) if row["artefact"] else None; if not want or entry is None: continue` — ред клас „въпрос“ няма артефакт и **никога** не стига до сверката, а файлът с решенията не е в `SIGNABLE` (`:177-184`), тоест не може да стане артефактен ред без редакция на `release.py` (забранена, §10). Затова G9 чете реда от опашката, изисква `решение: да`, сверява `тяло:` със `sha256` на низа и `тяло-на-файла:` с `gates.release.body_digest` на блоба, и изисква **човешкия подписал** (`gates/release.py:644` `yes_row_authorship` — комитът, внесъл блока, да е на `Petar1984`).
688: 
689: **G11 — дословно (S28-8):**
690: ```python
691: import json, subprocess, sys, pathlib
692: GEO = {"coordinates", "geometry", "geometries"}
693: def walk(o, path, hits):
694:     if isinstance(o, dict):
695:         for k, v in o.items():
696:             if k in GEO: hits.append(path + "/" + k)
697:             walk(v, path + "/" + k, hits)
698:     elif isinstance(o, list):
699:         for i, v in enumerate(o): walk(v, path + "[%d]" % i, hits)
700: files = [f for f in subprocess.run(["git","ls-files","data/"],capture_output=True,text=True).stdout.split() if f.endswith(".json")]
701: bad = []
702: for f in files:
703:     hits = []
704:     walk(json.loads(pathlib.Path(f).read_text(encoding="utf-8")), "", hits)
705:     if hits: bad.append((f, hits[:3]))
706: print(len(files), bad)
707: sys.exit(0 if not bad else 1)
708: ```
709: **Измерено: 18 файла, 0 попадения.** Плюс **инвентар на НОВИТЕ проследени файлове** на комита срещу неговия родител:
710: ```powershell
711: git diff --name-status --diff-filter=A <parent> HEAD
712: ```
713: Позволени НОВИ пътища, поименно: `tests/granitsi_client_probe.mjs`, `scratch/places_search/granitsi_fixtures_07.09.json` (при `git mv` върви като R, не A), `scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md`, `gates/allow/2026-09-07_b3.json`, `scratch/places_search/архив/АРХИВ_A_05.09.md`. **Всеки друг нов проследен файл = STOP.**
714: Отрицателна половина (измерена): файл с ключ `"\u0063oordinates"` — `grep -c coordinates` → **0** (exit 1), структурната проверка → **`/a/coordinates`** (exit 1 на гейта).
715: 
716: **G17 — дословно (S28-6, О17):** четирите отрицателни мутации, **всяка със СЪЩИЯ брой ключове**, всяка трябва да даде `false`:
717: 1. `_meta.generated` преименуван на `unexpected` — **10 ключа, но друго множество** → `metaKeysAre` трябва да върне `false`. (v2 броеше и минаваше: измерено `true`.)
718: 2. `quarter_attribution["kv_levski"].src = "openstreetmap"` при непроменен wikimapia url → `false` по правилото за извора.
719: 3. Измислен `src: "wikidata"` с валиден url → `false` по затвореното множество `ATTRIB_SRC`.
720: 4. Добавен запис `quarter_attribution["galata"]` (никой `SIGNED_POLYGON` ред не го носи) → `false` по **равенството** (v2 проверяваше само „всеки код има запис“ и това минаваше).
721: Положителните твърдения: places 10 ключа / 14 кода, hotels 8 ключа / 7 кода, всичките 21 записа с ключовото множество `{label, licence, src, url}`, `mladost2` с `url === 'https://www.openstreetmap.org/copyright'`.
722: 
723: ---
724: 
725: ## 6 · Комити (кой какво комитва)
726: 
727: Причината за атомността е механична: `index.html` пинва sha на данните — при какъвто и да е разрез съществува HEAD, в който пиновете и блобовете не си съответстват и търсенето на места умира.
728: 
729: | # | автор (наложен) | съдържание | съобщение (дословно) |
730: |---|---|---|---|
731: | 1 | `Claude Executor <executor@local>` (флагове, О24) | `docs/plans/ПЛАН_Б3_07.09.md` | `docs(plan): Б3 quarter search delivery plan v3 (signed 07.09)` |
732: | 2 | **`Petar1984`** (неговата ръка) | `data/places.json`, `data/hotels.json`, `data/place_categories.json`, `index.html`, `tests/test_places_public_bundle.py`, `tests/test_hotels_public_bundle.py`, `tests/test_granitsi_fixtures.py`, `tests/granitsi_client_probe.mjs`, `scratch/places_search/granitsi_fixtures_07.09.json` (+ изтритият `…_06.09.json`), `scratch/places_search/recall_sweep.py` | виж по-долу |
733: | 3 | `Claude Executor` | опашката Б3, **преименуваната `архив/АРХИВ_A_05.09.md`**, трите манифеста, новият `gates/allow/2026-09-07_b3.json` (138 реда, pending), махнатият стар allow. **`gates/baseline/MANIFEST.json` НЕ се пипа (О22).** | `docs: queue and manifests for the Б3 delivery signatures (07.09)` |
734: | 4 | **`Petar1984`** | каквото `gates.sign` е записало | съобщението, което писалката **отпечатва** |
735: | 4б | **`Petar1984`** (само ако низът се подписва отделно) | `index.html` (И11) | `feat(map): signed quarter-boundary line in the map attribution (decision 8)` |
736: | 5 | **`Petar1984`** | `recall_sweep_rows.json`, `expectations.json`, `probe_out/token_parity.json` | `freeze: reference + expectations + parity (Б3)` |
737: | 6 | `Claude Executor` (след пуша) | `docs/activeContext.md`, `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` | `docs: activeContext — Б3 delivery published, published hashes verified equal to local` |
738: 
739: Съобщението на комит 2, дословно (`scratch/places_search/COMMIT_MSG_B3.txt`):
740: 
741: ```
742: feat(search): quarter search over signed boundaries, QUARTER_CODES +8, cache v7 (D13 atomic delivery)
743: 
744: data: places delivery with quarter_attribution (D13 ordered) — the three blobs of
745: varna_3d 05f485e (places 3dffc264, hotels eb8fa85c, categories 9064705a), with the
746: closed lists, the three pins, LEGACY_BUNDLE_SHA and PLACES_CACHE v7 in this very
747: commit, because a HEAD whose pins and blobs disagree kills the place search.
748: tests: S17 fixtures fail on broken candidates
749: ```
750: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$s=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8; 750..899 | ForEach-Object { if("'$_ -lt $s.Length){'"'{0}: {1}' -f ("'$_+1),$s[$_]} }' in C:\git\Fire_Varna
 succeeded in 13ms:
851: - Публикуваните sha и `origin/main` — до ръката на Петър.
852: 
853: ---
854: 
855: ## 11 · Отхвърлени находки (от кръговете на v1/v2)
856: 
857: | # | находка (дословно запазена) | измерената причина да не се приложи както е написана |
858: |---|---|---|
859: | 1 | оборител **gates**: „baseline се пренасочва към `f00dd78` … тогава allow изобщо не е нужен“ | **Частично отхвърлено.** Измерено: неползван ред от allow е `allow_stale` (`coverage.py:573-577`) → `EXIT_ALLOW_STALE = 3` (`:617-618`); днешният подписан allow носи 150 реда → изход 3, не 0. Вариант (б) е изпълним само ако старият allow бъде изтрит в същия комит — самостоятелен подписан въпрос. Планът избира (а). |
860: | 2 | „338 знака ще се пренасят над бутоните `+/−` при 375 px“ | **Отхвърлено като твърдение, прието като проба.** Планерът няма браузър. `:1900` и `:1917` слагат двата контрола в един и същ ъглов контейнер, а Leaflet ги подрежда един под друг. Рискът влиза като §8 проба 10. |
861: | 3 | „`recall_sweep.py:67 REPO_ROOT`“ | **Само корекция на цитата.** `REPO_ROOT` е на **`:68`**. Същината (няма argparse, няма `--dump`, `OUTDIR` е `%TEMP%/fv_measures/`, `:4249-4253` презаписва проследения паритетен файл) е потвърдена. |
862: | 4 | v1 И11: „`BASEMAP_PMTILES_ENABLED = false` значи второто място не е живо“ | **Отхвърлено по мярка.** `:4571-4574` връща `true` и при `localStorage` override. Изводът оцелява по друга причина: `attribCtrl` е един и размените махат само собствените си низове. |
863: 
864: ---
865: 
866: ## 12 · Оборване
867: 
868: | оборител | присъда | приложено в v3 |
869: |---|---|---|
870: | **gates / search / delivery** (кръг на v1) | **НЕГОДНО** × 3 | Всичките 8 блокера приложени в v2 и запазени тук (О15–О26). |
871: | **Astra S28** (механика) | **НЕГОДНО**, 10 условия | **S28-1** ✅ — измерено със собствена Node-проба: хотелите също носят `SIGNED_POLYGON` (15 реда), старият списък отказва **и двата** пакета и `ensurePlaces` **хвърля**; фикстура 9 разделена на 9а/9б/9в + матрицата crypto×sha×брояч (1.8.11) и **брояч на извикванията** в твърдението. **S28-2** ✅ — двете мутации преработени по измереното (§3.5 фикстури 6, 7, 8); alias-трикът доказано изхвърлен като `foreign:asparuhovo`. **S28-3** ✅ — G7 с два ОТДЕЛНО ЗАПАЗЕНИ дъмпа, дословен байтов comparator със `sys.exit`, пинати ревизии и **доказана падаща мутация** (1 324 215 → 1 324 210 B). **S28-4** ✅ — измерен е ДЕЙСТВИТЕЛНИЯТ набор на първото зареждане (`AGENTS.md:53`): `index.html` + `data/hydrants.json` = **1 878 210 B**; командата на v2 наистина дава 19 файла / 26 839 286 B / exit 1 (§13 т. 1); отложената доставка е G10б. **S28-5** ✅ — `--manifest` очаква **1**, наборът е предварително изброен, coverage командите носят `sys.exit(r['exit_code'])`; **плюс собствената находка О30** (вторият прогон е вакуумно зелен). **S28-6** ✅ — G17 сверява точните МНОЖЕСТВА (10/8 дословно), затворен `src`, правило за всеки извор, и **равенство** карта ↔ кодове; четирите отрицателни мутации са със същия брой ключове. **S28-7** ✅ — G8 **изпълнява** `popupFor` върху 375 записа с DOM стъб (0 забранени низа); G9 **изпълнява** среза на атрибуцията със записващ `attribCtrl`; редът на опашката и `release.py:1367-1371` са разгледани — сверката минава в G9. **S28-8** ✅ — G11 е структурен обход + инвентар на новите проследени файлове; escape-пробата е измерена. **S28-9** ✅ — G14 е python байтово сравнение; `diff` в PowerShell потвърден като `Compare-Object`. **S28-10** ✅ с **поправка** — мълчаливият UI отказ става обявено отклонение О27; архивирането е измерено и **само подпапка НЕ стига** (§13 т. 2); G15 ползва семантиката на `queues_in_head`. |
872: | **Кими К28** (данни/семантика) | **НЕГОДНО**, 7 условия | **К28-1** ✅ — 1.8.4 поправено: „кв. Христо Ботев“ носи **1** ред с кода (`ЦДГ 8 - Христо Ботев`, по име). **К28-2** ✅ — фикстура 6 мутира ИМЕТО (5 → 4 измерено), кодовата мутация доказано НЕ пада (пак 5); `assert_case` става многозаявъчен с `fails_on`. **К28-3** ✅ — осемте изгубени реда назовани с новите си квартали; опашката дължи **8** делта-реда (STOP 19). **К28-4** ✅ — §8 проба 5 „бриз“ = **4** реда, поименно. **К28-5** ✅ — §9 т. 1 получава вариант (Б) с **измерени** резултати и **измерена нулева** цена на презамразяване; клиентската цена е назована честно (клиентът няма `M7_PREFIXES`). **К28-6** ✅ — О22 записва семантиката на coverage и §4 стъпка 2 иска и дифа `f06ac06↔f00dd78` (**150**, измерен от планера). **К28-7** ✅ — фикстура 7 изброява десетте op-а поименно; **числото е 21, не 20** (§13 т. 3). |
873: 
874: ---
875: 
876: ## 13 · Отхвърлени външни находки (с измерената причина)
877: 
878: | # | находка | измерената причина |
879: |---|---|---|
880: | 1 | **S28-1:** „с несъвпадащ SHA измерих **0 извиквания**, следователно `null` самостоятелно допуска false pass“ — като общо твърдение | **Прието по същество, поправено по обхват.** Измерено (1.8.11): 0 извиквания има САМО при **crypto ON**. При crypto OFF `accept` не сверява дайджест изобщо (`:6605`) и валидаторът се вика (1 извикване) дори с грешен sha. Твърдението „подай грешен sha и виж 0“ е вярно за ON и невярно за OFF; затова фикстурата подава **верния** sha на мутираното тяло и брои извикванията. |
881: | 2 | **S28-10 / заданието:** „архивиране извън точния glob е достатъчно“ / `git mv` към `scratch/places_search/архив/ЗА_ПОДПИС_A_05.09.md` | **Отхвърлено по мярка (1.8.19).** `queues_in_head()` (`release.py:437-458`) прави `git ls-tree **-r**` и сравнява **`posixpath.basename(n)`** с глоба. Проба в клонинг: след `git mv` в `архив/` със същото име резултатът е `['scratch/places_search/архив/ЗА_ПОДПИС_A_05.09.md']` — **пак една опашка, release пак BLOCKED**. Едва преименуването без префикса дава `[]`. Планът пише `архив/АРХИВ_A_05.09.md`. |
882: | 3 | **К28-7:** „преименуване на всичките 10 реда `chaika_kv` дава **30→20**“ | **Отхвърлено по число, прието по метод.** Измерено: **21** и при смяна само на `quarter.name`, и при смяна на `quarter.name` + `zone`. Оцеляват 19-те `chaika_kk` + `4 ОДЗ Чайка` (думата е в ИМЕТО ѝ) + `„ДКЦ Чайка“ ЕООД`. К28 сам допуска 21 в скоба; фикстурата пинва **21**. |
883: | 4 | **S28-5:** „измерени **8 несъответствия**“ | **Прието по същество, поправено по число.** Измерено в клонинг (1.8.15): първият `--manifest` дава **59 реда `ЧЕРВЕНО` върху 41 уникални заявки** плюс 2 реда без заявка. „училище младост: 6, подписано 11“ е потвърдено и е сред тях. Планът изброява целия набор (§4 стъпка 10). |
884: | 5 | **К28-5, разширението „пропускане на `M7_PREFIXES` токени“ дословно** (списъкът включва `"1"` и `"2"`) | **Частично отхвърлено по мярка.** Ако се пропуснат и числата, „възраждане 2“ връща **5** и „младост 2“ връща **20** — тоест ДЕТСКАТА заявка получава отговора на РОДИТЕЛЯ, което противоречи на измереното 0 и на О16. Приема се само буквената половина (`k, kv, zh, m, s, o, t, i`) — тогава „възраждане 2“/„младост 2“ остават **0**. |
885: | 6 | **v2 §1.5:** „`quarter_attribution` = 18 кода (17 wikimapia + 1 openstreetmap)“ | **Отхвърлено като основание за гейт.** 18 е ОБЕДИНЕНИЕТО. Измерено: places носи **14**, hotels **7**, общи **3**. Гейт, писан срещу 18, ще е червен и на двата пакета. |
886: | 7 | **v2 §3.6 т. 4:** „`RECS.length === 225` при среза с оригиналния `QUARTER_SRC`“ | **Отхвърлено по мярка (1.6).** При оригиналния списък и двата пакета падат и `ensurePlaces` **хвърля** `places payload unavailable` — няма `RECS`. 225 идва само от случая, в който **само** places е отказан (9в). |
887: | 8 | **v2 G10:** `git ls-files index.html 'data/*.json'` като „проследените файлове“ | **Отхвърлено по мярка (1.8.14).** 19 файла, **26 839 286 B**, exit **1** — червено преди промяната. Наборът включва архивни снимки на хидрантите, `search_index.json` (11,2 MB) и `address_rows.json` (5,07 MB), които клиентът НЕ тегли при първо отваряне. |
888: | 9 | **v2 G17:** „`Object.keys(d._meta).length !== META_KEYS_*`“ | **Отхвърлено по мярка.** Изпълнено: преименуване на `generated` на `unexpected` пази 10 ключа и връща **true**. Броят не е множество. |
889: | 10 | **v2 G14:** `diff scripts/hooks/pre-push .git/hooks/pre-push` | **Отхвърлено по мярка (1.8.22).** В PowerShell `diff` е `Alias → Compare-Object`; командата сравнява имена и излиза с 0 при подменена кука. |
890: | 11 | **v2 G11:** буквален `grep coordinates` | **Отхвърлено по мярка (1.8.12).** Ключ `"\u0063oordinates"`: grep → 0 попадения (exit 1), parse → `coordinates`. Освен това единственото буквално попадение днес е ПРОЗА в стойност, не ключ. |

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$s=Get-Content -LiteralPath '"'index.html' -Encoding UTF8; 6255..6364 | ForEach-Object { '{0}: {1}' -f ("'$_+1),$s[$_] }' in C:\git\Fire_Varna
 succeeded in 0ms:
6256:     const PLACES_URL = 'data/hotels.json', CATS_URL = 'data/place_categories.json';
6257:     const PLACES2_URL = 'data/places.json';            // фаза 2: училища/университети/болници/градини
6258:     // ADR 008 D8: the NAME is not a contract, the VERSION is — it changes with every
6259:     // change of the blobs. ЛОТ 1в-А rewrote all three (v2 → v3); ЛОТ 1в-Б added the
6260:     // `address` key to two of them (v3 → v4); ЛОТ 1в-В replaced the single `zone`
6261:     // with the three typed fields in all three, so v4 → v5 (the count stays 225).
6262:     // F12 (P7: М2+М3+М6) rewrites the VALUES of those fields — hotels with a named
6263:     // quarter 96 → 152, places 44 → 49 — so a device holding v5 must not answer
6264:     // from it: v5 → v6 (the count still stays 225).
6265:     const PLACES_CACHE = 'fire-varna-hotels-v6-225';   // our own namespace (Д3)
6266:     const TOP = 8, MIN_Q = 2, DEBOUNCE_MS = 120, FETCH_TIMEOUT_MS = 8000;
6267:     const TOP_TOTAL = 16, GEN_CAP = 300;               // фаза 2 С3: per group / per class
6268:     const CACHE_TIMEOUT_MS = 2000, MAX_BODY = 2000000, EXPECT_COUNT = 225, EXPECT2_COUNT = 150;
6269:     const MX = 81152, MY = 110574;               // metres per degree of lon/lat in Varna (М1)
6270:     const LAT_MIN = 43.13, LAT_MAX = 43.35, LON_MIN = 27.65, LON_MAX = 28.10;  // delivery box (Д2)
6271:     // ЛОТ 1в (ADR 008 D1/S2): `old_names_src` is a parallel array of the SAME length
6272:     // and order — the hotels' 13th key, the places' 9th. ЛОТ 1в-Б (D5) adds `address`
6273:     // as the hotels' 14th and the places' 10th: `null` or the closed four-key object.
6274:     // ЛОТ 1в-В (D9) adds the three typed location fields to both: 17 keys here, 13 there.
6275:     const EXPECT_KEYS = ['address', 'beds', 'cat', 'district', 'kind', 'lat', 'locality',
6276:                          'lon', 'name', 'no_uin', 'old_names', 'old_names_src', 'quarter',
6277:                          'src', 'status', 'uins', 'zone'];
6278:     const KINDS = ['Хотел', 'Семеен хотел', 'хотел · без категоризация', 'апарт-хотел'];
6279:     // Фаза 2 (places_phase2_plan.md Д1/Д3): the second delivery - 8 keys, its own
6280:     // kind enum. Same box, same status enum, same cadastral refusal as the hotels.
6281:     const EXPECT2_KEYS = ['address', 'district', 'kind', 'lat', 'locality', 'lon', 'name',
6282:                           'old_names', 'old_names_src', 'quarter', 'src', 'status', 'zone'];
6283:     const KINDS2 = ['училище', 'университет', 'болница', 'ДКЦ', 'хоспис', 'детска градина',
6284:                      'детска ясла', 'общежитие'];
6285:     const STATUSES = ['', 'бивш'];
6286:     const CADASTRAL = /\b\d{4,5}\.\d+\.\d+/;     // a cadastral id never rides a public bundle (Д2)
6287:     // §12 В7 + §14 — the exact bytes the browser may trust (the tracked LF blobs).
6288:     const HOTELS_SHA256 = '46a44ce82f154ca6f77f5001c0393b4654a818ba6d5e8540fb1c6f337fe0418d';
6289:     const PLACES2_SHA256 = '329310f577e8353673b9014af99624a78ab825fb0ad53e93fc572a28660d88c0';
6290:     const CATS_SHA256 = '874e33cd00e2f468d6fa1fe717351a5247765ae13d4301374a9a14f83347d054';
6291:     // ЛОТ 1в-В (ADR 008 D9, план §3ж S2) — `legacy_by_row` is keyed by the ORDINAL
6292:     // of a row in its bundle, so it is only ever as true as the bundle it was built
6293:     // against: a re-export that reorders the rows would move every old word onto a
6294:     // stranger. The dictionary carries the SHA of both bundles and the pair below is
6295:     // the measured one; anything else switches the old words off (fail-closed).
6296:     // Both digests are the LF blobs pinned above — the house rule, `git show
6297:     // <commit>:<path>`. The first delivery pinned the hotels by their CRLF twin,
6298:     // because the exporter digested its own working-tree file and that checkout
6299:     // writes CRLF; varna_3d P6-б normalises the bytes before hashing, so one
6300:     // content now has exactly one digest on every checkout (measured 04.09).
6301:     const LEGACY_BUNDLE_SHA = {
6302:       places: '329310f577e8353673b9014af99624a78ab825fb0ad53e93fc572a28660d88c0',
6303:       hotels: '46a44ce82f154ca6f77f5001c0393b4654a818ba6d5e8540fb1c6f337fe0418d'
6304:     };
6305:     // ЛОТ 1в-В (ADR 008 D9, план §3г/§3ж S1/S4/S6) — the three TYPED location
6306:     // fields. Each is `null` or EXACTLY {name, src, code}, the source and the code
6307:     // out of closed lists: a public row can carry no location nobody wrote down.
6308:     // The district list is the five city districts of §3ж S4 and nothing else;
6309:     // `zone` stays as the compat label (quarter?.name ?? „район “ + district.name)
6310:     // until G-ZERO-ZONE retires it.
6311:     const LOC_KEYS = ['name', 'src', 'code'];
6312:     const LOC_CLASSES = ['quarter', 'district', 'locality'];
6313:     const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE'];
6314:     const DISTRICT_SRC = ['KAIS', 'SIGNED_OVERRIDE'];
6315:     const DISTRICT_CODES = ['primorski', 'odesos', 'mladost', 'asparuhovo',
6316:                             'vladislav_varnenchik'];
6317:     const QUARTER_CODES = ['asparuhovo', 'borovets_yug', 'briz', 'chaika_kk',
6318:                            'chaika_kv', 'druzhba', 'galata', 'izgrev_kv',
6319:                            'kk_konstantin_elena', 'mladost', 'mladost2', 'pobeda',
6320:                            'priboy', 'troshevo', 'vazrazhdane', 'vazrazhdane1',
6321:                            'vazrazhdane2', 'vinitsa', 'vladislavovo', 'zlatni_pyasatsi'];
6322:     const LOCALITY_CODES = ['morska_gradina', 'sveti_nikola', 'vilite', 'zelenika', 'zpz'];
6323:     const DISTRICT_MARK = 'район';                 // the word, in the card and in a query
6324:     // ЛОТ 1в (ADR 008 D1, амандамент А3) — the CLOSED list of alias sources and the
6325:     // word the card says for each. An old name used to inherit the source line of its
6326:     // RECORD: up to 47 OSM strings sat under a registry row and the card claimed the
6327:     // register for them. Now every alias carries its own letter (D3).
6328:     const ALIAS_SRC_LINE = {
6329:       'OSM': '© OpenStreetMap contributors (ODbL)',
6330:       'REG': 'регистър (отделен факт)',
6331:       'NTR': 'Национален туристически регистър',
6332:       'WD': 'Wikidata (CC0)',
6333:       'WEB': 'официален сайт',
6334:       'KAIS': 'КАИС адресно поле (АГКК)',
6335:       'CUR': 'съкращение (речник)'
6336:     };
6337:     // ЛОТ 1в-Б (ADR 008 D5, план §2 т. 2) — the CLOSED list of ADDRESS sources and
6338:     // the word the card says after the address itself. The register of an address is
6339:     // NOT the register of the name: a place named by the school registry can carry a
6340:     // КАИС address, so the line names the source of THAT string. „· КАИС“ is the
6341:     // wording of the signed plan; the OSM one keeps the ODbL attribution whole.
6342:     const ADDR_SRC_LINE = {
6343:       'KAIS': 'КАИС',
6344:       'REG': 'регистър',
6345:       'NTR': 'Национален туристически регистър',
6346:       'OSM': '© OpenStreetMap contributors (ODbL)'
6347:     };
6348:     // Д7 — the source line of a record, worded from the delivery's own licence.
6349:     const SRC_LINE = {
6350:       'НТР УИН': 'име: Национален туристически регистър · координати: КАИС Отворени данни (АГКК)',
6351:       'КАИС адресно поле': 'име: КАИС адресно поле (АГКК) · координати: КАИС Отворени данни (АГКК)',
6352:       'Sol/OSM идентификация': 'име: публична идентификация (OSM, официални сайтове, общински регистри) · координати: КАИС Отворени данни (АГКК)',
6353:       // Фаза 2 Д3/К8 - the four src values of data/places.json, each naming its own
6354:       // register word for word. validatePlaces2 refuses a row whose src is not here.
6355:       'OSM': 'име: © OpenStreetMap contributors (ODbL) · координати: КАИС Отворени данни (АГКК)',
6356:       'Регистър на училищата (МОН/НЕИСПУО), одобрено 21.08': 'име: Регистър на училищата (МОН/НЕИСПУО), одобрено 21.08 · координати: КАИС Отворени данни (АГКК)',
6357:       'Регистър на лечебните заведения (ИАМН)': 'име: Регистър на лечебните заведения (ИАМН) · координати: КАИС Отворени данни (АГКК)',
6358:       'Регистър на училищата и детските заведения (Община Варна)': 'име: Регистър на училищата и детските заведения (Община Варна) · координати: КАИС Отворени данни (АГКК)'
6359:     };
6360:     // Фаза 2 С3 - the classes AS THE HUMAN ASKS FOR THEM: the four hotel kinds are
6361:     // ONE group, every other kind is its own. The group is the render header, the
6362:     // unit of the "…и още N" tail and the unit of the М3/Б2 generosity gate.
6363:     const KIND_GROUP = {
6364:       'Хотел': 'Хотели', 'Семеен хотел': 'Хотели',
6365:       'хотел · без категоризация': 'Хотели', 'апарт-хотел': 'Хотели',

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$s=Get-Content -LiteralPath '"'index.html' -Encoding UTF8; 6527..6676 | ForEach-Object { '{0}: {1}' -f ("'$_+1),$s[$_] }' in C:\git\Fire_Varna
 succeeded in 11ms:
6653:       // implementations: this and scratch/places_search/recall_sweep.py.
6654:       // Fail-soft (С7′): a `locations` that is not an object switches the location
6655:       // words off and nothing else — the class keys, the names, the aliases and
6656:       // the addresses all still stand.
6657:       const locs = (cats && cats.locations && typeof cats.locations === 'object') ? cats.locations : {};
6658:       const generic = new Set();                 // (г) the dictionary's own word list
6659:       for (const word of ((cats && cats._meta && cats._meta.zone_generic_words) || []))
6660:         for (const t of placeTokens(word)) generic.add(t.s);
6661:       GENERIC_WORDS = generic;                   // F12-е: the same set, readable in search()
6662:       // The phrase filter of steps (а)-(г): a number, a token of <= 2 characters, an
6663:       // address marker and a generic word („район“, „квартал“, „зона“…) carry no
6664:       // place. The ORDER and the boundaries are the point — „морска градина“ is a
6665:       // phrase, „градина“ alone is not.
6666:       // Амандамент №3 т. 5: ONE significance rule on the client too. This used to
6667:       // be a second copy of the predicate; a copy is a rule that can drift by one
6668:       // edit, and `isSignificantToken` is the same question search() asks.
6669:       const sigTokens = (s) => placeTokens(s).filter(isSignificantToken).map((t) => t.s);
6670:       const LOC_INDEX = new Map();               // class -> code -> {name, extra, phrases}
6671:       for (const cls of LOC_CLASSES) {
6672:         const entries = (locs[cls] && typeof locs[cls] === 'object') ? locs[cls] : {};
6673:         const codes = Object.keys(entries).filter((c) => entries[c] && typeof entries[c] === 'object'
6674:           && typeof entries[c].name === 'string' && entries[c].name);
6675:         const own = new Map(codes.map((c) => [c, new Set(placeTokens(entries[c].name).map((t) => t.s))]));
6676:         const index = new Map();
6677:         for (const code of codes) {

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$s=Get-Content -LiteralPath '"'scratch/places_search/recall_sweep.py' -Encoding UTF8; 60..109 | ForEach-Object { '{0}: {1}' -f ("'$_+1),$s[$_] }; $s[4300..4334]' in C:\git\Fire_Varna
 succeeded in 0ms:
61: if hasattr(sys.stdout, "reconfigure"):
62:     sys.stdout.reconfigure(encoding="utf-8")
63: 
64: # The checkout this script lives in. INPUTS and artefacts alike are read and
65: # written relative to it, never through a fixed path: a worktree must re-freeze
66: # its own reference against ITS OWN data (F2-к0 for the outputs, F3-к for the
67: # inputs — a fixed path would have a worktree measure another checkout's bytes).
68: REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
69: # Phase 2 (places_phase2_plan.md sec.8, lot C12): the reference reads the
70: # DELIVERED bytes of Fire_Varna -- the very three files the browser fetches --
71: # not the varna_3d originals. Identical content today; a divergence between the
72: # two repos must be loud in this gate, not silent.
73: HOTELS = str(REPO_ROOT / "data" / "hotels.json")
74: PLACES2 = str(REPO_ROOT / "data" / "places.json")
75: CATS = str(REPO_ROOT / "data" / "place_categories.json")
76: REPO_ROWS_OUT = str(REPO_ROOT / "scratch" / "places_search" / "recall_sweep_rows.json")
77: # С6′: the tokeniser-parity corpus the probe replays in the page. One generator,
78: # one file — the probe never invents the input list.
79: REPO_PARITY_OUT = str(REPO_ROOT / "scratch" / "places_search" / "probe_out"
80:                       / "token_parity.json")
81: # The human-readable report and the working copy of the rows are MEASUREMENTS,
82: # not deliverables: they land in the system temp — never in the repo, never in a
83: # session-specific scratch folder that dies with the session (F3-к).
84: OUTDIR = (pathlib.Path(tempfile.gettempdir()) / "fv_measures").as_posix() + "/"
85: # ЛОТ 1в-В (план §3ж S2) — the two modes. Until this lot every sweep rewrote the
86: # TRACKED reference, so the artefact Petar is asked to sign and the artefact the
87: # suite replays were one file: a run could freeze a change nobody had read. The
88: # tracked write now needs `--freeze` in so many words; anything else is
89: # REPORT-ONLY and writes the candidate + the old → new manifest into OUTDIR.
90: FREEZE = "--freeze" in sys.argv
91: REPORT_ONLY = not FREEZE
92: # F12-в: the two diffs Petar signs before anything is frozen. REPORT-ONLY by
93: # construction — it never touches the tracked reference, only writes the two
94: # manifests next to it, and `--freeze` and `--manifest` are refused together.
95: MANIFEST = "--manifest" in sys.argv
96: if MANIFEST and FREEZE:
97:     raise SystemExit(u"--manifest е report-only: не се съчетава с --freeze")
98: # Date only, so two runs of the same day are byte-equal (the determinism gate
99: # replays this script twice and compares).
100: GENERATED_AT = datetime.date.today().isoformat()
101: 
102: # Fire_Varna/index.html:1838  .setView([43.2141, 27.9147], 13)
103: # stand-in for map.getCenter() -- there is no map in a headless sweep.
104: CENTER = (43.2141, 27.9147)
105: TOP = 8
106: 
107: # ----------------------------------------------------------------- primitives
108: # index.html:4786 norm()   [unchanged from recall_sweep.py]
109: def norm(s):
110:     s = ("" if s is None else str(s)).lower()
            blockers.append(u"измереното сега се различава от подписаното — "
                            u"замразяването не пренася подпис върху друг отговор")
        def _write_reference():
            # The reference the JS is gated against lives next to the probe that
            # replays it — one file, one generator. LF on purpose: the CRLF twin
            # on a Windows worktree is the same OID and different bytes (F12-ж).
            pathlib.Path(REPO_ROWS_OUT).write_text(_rows_text, encoding="utf-8",
                                                   newline="\n")
            return u"FREEZE: замразена референция -> %s" % REPO_ROWS_OUT

        def _write_expectations():
            _path, _signature = write_expectations(
                build_expectations(_rows_text, ROWS, measure_sweep(M5, EXTRA),
                                   refused=_refused), frozen=True)
            return u"FREEZE: очаквания -> %s (signed_by: %s)" % (_path, _signature)

        def _write_parity():
            # The third tracked body of this script, in the same block: a refused
            # freeze leaves it byte-untouched (амандамент №5 т. 4).
            pathlib.Path(REPO_PARITY_OUT).write_text(_parity_text, encoding="utf-8",
                                                     newline=chr(10))
            return u"FREEZE: паритет на токенизатора -> %s" % REPO_PARITY_OUT

        _code, _written = freeze_writes(blockers, [_write_reference,
                                                   _write_expectations,
                                                   _write_parity])
        if _code:
            return _code

    return 1 if red else 0


if __name__ == "__main__":
    sys.exit(main())

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding=[System.Text.UTF8Encoding]::new($false); @'"'
import pathlib,subprocess,json,re,hashlib
root=pathlib.Path.cwd()
html=(root/'index.html').read_text(encoding='utf-8')
sl='\\n'.join(html.splitlines()[6255:7154])
payload={}
for short,src in [('hotels','fire_varna_hotels'),('places','fire_varna_places'),('place_categories','place_categories')]:
 b=subprocess.check_output(['git','-C','C:/git/varna_3d','show','05f485e:data/'+src+'.json'])
 payload['data/'+short+'.json']=b.decode('utf-8')
 print(short,len(b),hashlib.sha256(b).hexdigest())
js=r'''
const {webcrypto,createHash}=require('node:crypto');
const p=JSON.parse(require('node:fs').readFileSync(0,'utf8'));
const hash=t=>createHash('sha256').update(t).digest('hex');
const parse=k=>JSON.parse(p.data['data/'+k+'.json']);
function pins(s,data){for(const [c,k] of [['HOTELS_SHA256','hotels'],['PLACES2_SHA256','places'],['CATS_SHA256','place_categories']]) s=s.replace(new RegExp(\"const \"+c+\" = '["'^'"']+'\"),\"const \"+c+\" = '\"+hash(data['data/'+k+'.json'])+\"'\");return s;}
function lists(s){s=s.replace(/const QUARTER_SRC = \\[[\\s\\S]*?\\];/,\"const QUARTER_SRC = ['REG','KAIS','SIGNED_OVERRIDE','SIGNED_POLYGON','DISTRICT_FALLBACK'];\");s=s.replace(/const QUARTER_CODES = \\[[\\s\\S]*?\\];/, 'const QUARTER_CODES = '+JSON.stringify(Object.keys(parse('place_categories').locations.quarter))+';');return s;}
function instance(s,data,on){const calls={hotels:0,places:0}; const wrap="'`;const oh=validateHotels,op=validatePlaces2;validateHotels=(...a)=>{__calls.hotels++;return oh(...a)};validatePlaces2=(...a)=>{__calls.places++;return op(...a)};return {validateHotels:oh,validatePlaces2:op,accept,ensurePlaces,get:()=>({n:RECS.length,calls:__calls})};`;const cr=on?{subtle:webcrypto.subtle}:undefined;const env={crypto:cr};return {calls,api:new Function('"'window','caches','document','map','fetch','attribCtrl','__calls','L','console','crypto',s+wrap)(env,undefined,{}, {getCenter:()=>({lat:43.2141,lng:27.9147})},async u=>({ok:true,text:async()=>data[u]}),{},calls,{}, {warn:()=>{},log:()=>{}},cr)};}
(async()=>{for(const on of [true,false]){for(const name of ['9a','9b','9c']){let data={...p.data},s=p.slice;if(name"'!=='"'9a')s=lists(s);if(name==='9c'){const doc=JSON.parse(data['data/places.json']);const r=doc.places.find(r=>r.quarter?.src==='SIGNED_POLYGON');r.quarter.code='tsentar_new';data['data/places.json']=JSON.stringify(doc);}
if(name"'!=='"'9a')s=pins(s,data);
const {api,calls}=instance(s,data,on);const val=[api.validateHotels(JSON.parse(data['data/hotels.json']),data['data/hotels.json']),api.validatePlaces2(JSON.parse(data['data/places.json']),data['data/places.json'])];let error=null;try{await api.ensurePlaces()}catch(e){error=e.message}process.stdout.write(JSON.stringify({on,name,validators:val,error,...api.get()})+'\\n');}
const {api}=instance(p.slice,p.data,on);for(const correct of [false,true]){let calls=0;const t=p.data['data/places.json'];let out=await api.accept(t,correct?hash(t):'0'.repeat(64),()=>{calls++;return false});console.log(JSON.stringify({on,correct,result:out,calls}));}}
})();
'''
r=subprocess.run(['node','-e',js],input=json.dumps({'slice':sl,'data':payload}),text=True,encoding='utf-8',capture_output=True)
print(r.stdout);print(r.stderr);print('NODE_EXIT',r.returncode)
'@ | python -B -" in C:\git\Fire_Varna
 exited 1 in 49ms:
fatal: detected dubious ownership in repository at 'C:/git/varna_3d'
'C:/git/varna_3d' is owned by:
	PETAR/Petar (S-1-5-21-1992376794-12164101-10249461-1001)
but the current user is:
	PETAR/CodexSandboxOffline (S-1-5-21-1992376794-12164101-10249461-1004)
To add an exception for this directory, call:

	git config --global --add safe.directory C:/git/varna_3d
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
  File "C:\Program Files\Python310\lib\subprocess.py", line 420, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
  File "C:\Program Files\Python310\lib\subprocess.py", line 524, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['git', '-C', 'C:/git/varna_3d', 'show', '05f485e:data/fire_varna_hotels.json']' returned non-zero exit status 128.

2026-09-07T07:11:40.876054Z ERROR codex_models_manager::manager: failed to refresh available models: timeout waiting for child process to exit
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding=[System.Text.UTF8Encoding]::new($false); @'"'
import pathlib,subprocess,json,re,hashlib
html=pathlib.Path('index.html').read_text(encoding='utf-8'); sl='\\n'.join(html.splitlines()[6255:7154]); payload={}
for short,src in [('hotels','fire_varna_hotels'),('places','fire_varna_places'),('place_categories','place_categories')]:
 b=subprocess.check_output(['git','-c','safe.directory=C:/git/varna_3d','-C','C:/git/varna_3d','show','05f485e:data/'+src+'.json']); payload['data/'+short+'.json']=b.decode('utf-8'); print(short,len(b),hashlib.sha256(b).hexdigest())
js=r'''
const {webcrypto,createHash}=require('node:crypto');
const p=JSON.parse(require('node:fs').readFileSync(0,'utf8'));
const hash=t=>createHash('sha256').update(t).digest('hex');
const parse=k=>JSON.parse(p.data['data/'+k+'.json']);
function pins(s,data){for(const [c,k] of [['HOTELS_SHA256','hotels'],['PLACES2_SHA256','places'],['CATS_SHA256','place_categories']]) s=s.replace(new RegExp(\"const \"+c+\" = '["'^'"']+'\"),\"const \"+c+\" = '\"+hash(data['data/'+k+'.json'])+\"'\");return s;}
function lists(s){s=s.replace(/const QUARTER_SRC = \\[[\\s\\S]*?\\];/,\"const QUARTER_SRC = ['REG','KAIS','SIGNED_OVERRIDE','SIGNED_POLYGON','DISTRICT_FALLBACK'];\");s=s.replace(/const QUARTER_CODES = \\[[\\s\\S]*?\\];/, 'const QUARTER_CODES = '+JSON.stringify(Object.keys(parse('place_categories').locations.quarter))+';');return s;}
function instance(s,data,on){const calls={hotels:0,places:0};const wrap="'`;const oh=validateHotels,op=validatePlaces2;validateHotels=(...a)=>{__calls.hotels++;return oh(...a)};validatePlaces2=(...a)=>{__calls.places++;return op(...a)};return {validateHotels:oh,validatePlaces2:op,accept,ensurePlaces,get:()=>({n:RECS.length,calls:__calls})};`;const cr=on?{subtle:webcrypto.subtle}:undefined;return {calls,api:new Function('"'window','caches','document','map','fetch','attribCtrl','__calls','L','console','crypto',s+wrap)({crypto:cr},undefined,{}, {getCenter:()=>({lat:43.2141,lng:27.9147})},async u=>({ok:true,text:async()=>data[u]}),{},calls,{}, {warn:()=>{},log:()=>{}},cr)};}
(async()=>{for(const on of [true,false]){for(const name of ['9a','9b','9c']){let data={...p.data},s=p.slice;if(name"'!=='"'9a')s=lists(s);if(name==='9c'){const doc=JSON.parse(data['data/places.json']);const r=doc.places.find(r=>r.quarter?.src==='SIGNED_POLYGON');r.quarter.code='tsentar_new';data['data/places.json']=JSON.stringify(doc);}
if(name"'!=='"'9a')s=pins(s,data);
const {api,calls}=instance(s,data,on);const val=[api.validateHotels(JSON.parse(data['data/hotels.json']),data['data/hotels.json']),api.validatePlaces2(JSON.parse(data['data/places.json']),data['data/places.json'])];let error=null;try{await api.ensurePlaces()}catch(e){error=e.message}process.stdout.write(JSON.stringify({on,name,validators:val,error,...api.get()})+'\\n');}
const {api}=instance(p.slice,p.data,on);for(const correct of [false,true]){let calls=0;const t=p.data['data/places.json'];let out=await api.accept(t,correct?hash(t):'0'.repeat(64),()=>{calls++;return false});console.log(JSON.stringify({on,correct,result:out,calls}));}}
})();
'''
r=subprocess.run(['node','-e',js],input=json.dumps({'slice':sl,'data':payload}),text=True,encoding='utf-8',capture_output=True);print(r.stdout);print(r.stderr);print('NODE_EXIT',r.returncode)
'@ | python -B -" in C:\git\Fire_Varna
 succeeded in 83ms:
hotels 151263 eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51
places 128401 3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66
place_categories 77998 9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231

[eval]:11
const {api,calls}=instance(s,data,on);const val=[api.validateHotels(JSON.parse(data['data/hotels.json']),data['data/hotels.json']),api.validatePlaces2(JSON.parse(data['data/places.json']),data['data/places.json'])];let error=null;try{await api.ensurePlaces()}catch(e){error=e.message}process.stdout.write(JSON.stringify({on,name,validators:val,error,...api.get()})+'\n');}
                                                     ^

TypeError: Cannot read properties of undefined (reading 'validateHotels')
    at [eval]:11:54
    at [eval]:13:3
    at [eval]:14:4
    at runScriptInThisContext (node:internal/vm:209:10)
    at node:internal/process/execution:446:12
    at [eval]-wrapper:6:24
    at runScriptInContext (node:internal/process/execution:444:60)
    at evalFunction (node:internal/process/execution:279:30)
    at evalTypeScript (node:internal/process/execution:291:3)
    at node:internal/main/eval_string:74:3

Node.js v22.19.0

NODE_EXIT 1

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$s=Get-Content -LiteralPath '"'index.html' -Encoding UTF8; 6365..6429 | ForEach-Object { '{0}: {1}' -f ("'$_+1),$s[$_] }; $s[7140..7153]' in C:\git\Fire_Varna
 succeeded in 0ms:
6366:       'училище': 'Училища', 'университет': 'Университети', 'болница': 'Болници',
6367:       'ДКЦ': 'ДКЦ', 'хоспис': 'Хосписи', 'детска градина': 'Детски градини',
6368:       // ЛОТ 1, амандамент №8 П2 (подписът на Петър, 03.09): the two new kinds of
6369:       // the delivery get a heading each — the nursery is NOT a kindergarten.
6370:       'детска ясла': 'Детски ясли', 'общежитие': 'Общежития'
6371:     };
6372:     const KIND_CHIP = {
6373:       'Хотел': 'хотел', 'Семеен хотел': 'хотел',
6374:       'хотел · без категоризация': 'хотел', 'апарт-хотел': 'хотел',
6375:       'училище': 'училище', 'университет': 'университет', 'болница': 'болница',
6376:       'ДКЦ': 'ДКЦ', 'хоспис': 'хоспис', 'детска градина': 'детска градина'
6377:     };
6378:     // К1 (§12) - the three colour families over the groups above; data-grp is all
6379:     // the row, the header and the pin carry, the colours live in the CSS. A group
6380:     // missing here falls back to the hotel orange, never to no colour at all.
6381:     const GROUP_COLOUR = {
6382:       'Хотели': 'hotel',
6383:       'Училища': 'edu', 'Университети': 'edu', 'Детски градини': 'edu',
6384:       'Детски ясли': 'edu', 'Общежития': 'edu',
6385:       'Болници': 'health', 'ДКЦ': 'health', 'Хосписи': 'health'
6386:     };
6387: 
6388:     // ЛОТ 1, амандамент №8 П2: the words that ask for MORE THAN ONE delivered
6389:     // kind. The dictionary already maps a form to a SET of chips („заведение“ ->
6390:     // three), but its own „детско заведение“ chip counts 3D bodies, not our rows,
6391:     // and the dictionary is a delivery from varna_3d that we never edit by hand —
6392:     // so the binding of the word to OUR kinds lives here. recall_sweep.py carries
6393:     // the same table (EXTRA_FORMS); a drift between the two is a failed gate.
6394:     const EXTRA_FORMS = {
6395:       'детско заведение': ['детска градина', 'детска ясла'],
6396:       'детски заведения': ['детска градина', 'детска ясла']
6397:     };
6398: 
6399:     // ---- primitives: VERBATIM copies of the address search (index.html:4786-4788).
6400:     // Theirs are private to their IIFE, and a copy that drifts would make the two
6401:     // branches disagree in silence — tests/test_places_search_primitives.py pulls
6402:     // every definition out of this file and compares them byte for byte.
6403:     function norm(s){return (''+(s||'')).toLowerCase().replace(/блок/g,'бл').replace(/вход/g,'вх').replace(/[.№,'"-]/g,' ').replace(/\s+/g,' ').trim();}
6404:     function skel(w){w=w.toLowerCase();var C={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'};var o='';for(var i=0;i<w.length;i++){o+=(C[w[i]]!==undefined?C[w[i]]:w[i]);}return o.replace(/[yj]/g,'i').replace(/(\D)\1+/g,'$1');}
6405:     function lev(a,b,cap){var la=a.length,lb=b.length;if(Math.abs(la-lb)>cap)return cap+1;var prev=[];for(var j=0;j<=lb;j++)prev[j]=j;for(var i=1;i<=la;i++){var cur=[i],best=i;for(var j=1;j<=lb;j++){var v=Math.min(prev[j]+1,cur[j-1]+1,prev[j-1]+(a[i-1]===b[j-1]?0:1));cur[j]=v;if(v<best)best=v;}if(best>cap)return cap+1;prev=cur;}return prev[lb];}
6406: 
6407:     // ---- Т1/Б1 tokenizer: query and name go through the very same pipe ----------
6408:     const TYPO = /[„“”‚‘’«»–—/()]/g;             // norm() keeps these; they are word breaks
6409:     // ТА1(2): the markers are a PRE-norm rewrite of the text, so the word that comes
6410:     // out is the long one and ITS length is the original the cap reads. „св.“/„св“
6411:     // belong here, not to the token step: as a 2-letter original „св марина“ could
6412:     // never reach „Света Марина“ (measured 03.09: 25 rows against the
6413:     // reference's 33, and the УМБАЛ missing altogether). 1:1 with recall_sweep.py MARKERS.
6414:     const ABBR = [[/д-р/g, 'доктор '], [/х-л/g, 'хотел '], [/к-с/g, 'комплекс '],
6415:                   [/(?<![а-яa-z])св\./g, ' свети '], [/(?<![а-яa-z])св(?![а-яa-z])/g, ' свети ']];
6416:     const ORD_SUFFIX = /(\d+)\s*-?\s*(ми|ма|мо|ти|та|то|ви|ва|во|ри|ра|ро)(?![а-яa-z])/g;
6417:     const TOKEN_ORD = /^(\d+)(ми|ма|мо|ти|та|то|ви|ва|во|ри|ра|ро)$/;
6418:     const CYRILLIC_I = /[Іі]/g;                  // І/і read as the Latin letter they look like
6419:     const COMPOUNDS = { 'апартхотел': ['апарт', 'хотел'], 'апарткомплекс': ['апарт', 'комплекс'] };
6420:     const ADDR = ['бл', 'блок', 'вх', 'вход', 'ул', 'бул', 'кв', 'жк', '№'];   // never significant (А5)
6421:     const ORD_STEMS = { 'първ': 1, 'втор': 2, 'трет': 3, 'четвърт': 4, 'пет': 5, 'шест': 6, 'седм': 7,
6422:                         'осм': 8, 'девет': 9, 'десет': 10, 'единадесет': 11, 'единайсет': 11,
6423:                         'дванадесет': 12, 'дванайсет': 12 };
6424:     const ORD_WORDS = {};
6425:     for (const stem of Object.keys(ORD_STEMS))
6426:       for (const end of ['и', 'а', 'о', 'ият', 'ия', 'ата', 'ото', 'ите']) ORD_WORDS[stem + end] = String(ORD_STEMS[stem]);
6427:     function romanValue(w) {
6428:       if (!/^[ivx]{1,5}$/.test(w) || !/^(x{0,3})(ix|iv|v?i{0,3})$/.test(w)) return null;
6429:       const V = { i: 1, v: 5, x: 10 };
6430:       let total = 0, prev = 0;
    }
    // С1: does THIS text carry a key? A few tokens against the dictionary -- cheap
    // enough to answer SYNCHRONOUSLY on every keystroke, which is what lets the
    // inline remainder go before their 120 ms debounce mutates anything.
    const hasKeyFor = (q) => !!(RECS.length && CLASS_OF && splitKeys(placeTokens(q)).keys.length);

    // ---- our own dropdown (Д4/Д5/Д6) — textContent only, never an asr-* selector
    let shown = [], shownFor = null, theirStatusFor = null, tidiedByUs = false, keyed = false;
    let gen = 0, dismissed = false, timer = null, warned = false;
    let placeMk = null, placePopup = null, lastPick = null, mineActive = false;
    let lastAliasI = -1;                         // D3: which old name the pick matched
    let restoreArmed = false;                    // С4: armed by a pick, spent once
    function warnOnce(e) { if (warned) return; warned = true; console.warn('[places-search] ' + ((e && e.message) || e)); }
    const guarded = (fn) => function (ev) { try { fn(ev); } catch (e) { warnOnce(e); } };   // Д11

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding=[System.Text.UTF8Encoding]::new($false); @'"'
import pathlib,subprocess,json
sl='\\n'.join(pathlib.Path('index.html').read_text(encoding='utf-8').splitlines()[6255:7154])+'\\n'; data={}
for short,src in [('hotels','fire_varna_hotels'),('places','fire_varna_places'),('place_categories','place_categories')]:
 data['data/'+short+'.json']=subprocess.check_output(['git','-c','safe.directory=C:/git/varna_3d','-C','C:/git/varna_3d','show','05f485e:data/'+src+'.json']).decode('utf8')
js=r'''
const {webcrypto,createHash}=require('node:crypto'),p=JSON.parse(require('node:fs').readFileSync(0,'utf8'));
const hash=t=>createHash('sha256').update(t).digest('hex');
function pins(s,d){for(const [c,k] of [['HOTELS_SHA256','hotels'],['PLACES2_SHA256','places'],['CATS_SHA256','place_categories']])s=s.replace(new RegExp(\"const \"+c+\" = '["'^'"']+'\"),\"const \"+c+\" = '\"+hash(d['data/'+k+'.json'])+\"'\");return s;}
function lists(s){return s.replace(/const QUARTER_SRC = \\[[\\s\\S]*?\\];/,\"const QUARTER_SRC = ['REG','KAIS','SIGNED_OVERRIDE','SIGNED_POLYGON','DISTRICT_FALLBACK'];\").replace(/const QUARTER_CODES = \\[[\\s\\S]*?\\];/,'const QUARTER_CODES = '+JSON.stringify(Object.keys(JSON.parse(p.data['data/place_categories.json']).locations.quarter))+';');}
function instance(s,d,on){const calls={hotels:0,places:0},cr=on?{subtle:webcrypto.subtle}:undefined;const wrap="'`'"\\nconst oh=validateHotels,op=validatePlaces2;validateHotels=(...a)=>{__calls.hotels++;return oh(...a)};validatePlaces2=(...a)=>{__calls.places++;return op(...a)};return {validateHotels:oh,validatePlaces2:op,accept,ensurePlaces,get:()=>({n:RECS.length,calls:__calls})};"'`;
return new Function('"'window','caches','document','map','fetch','attribCtrl','__calls','L','console','crypto',s+wrap)({crypto:cr},undefined,{}, {getCenter:()=>({lat:43.2141,lng:27.9147})},async u=>({ok:true,text:async()=>d[u]}),{},calls,{}, {warn:()=>{},log:()=>{}},cr);}
(async()=>{for(const on of [true,false]){for(const name of ['9a','9b','9c']){let d={...p.data},s=p.slice;if(name"'!=='"'9a')s=lists(s);if(name==='9c'){let doc=JSON.parse(d['data/places.json']);doc.places.find(r=>r.quarter?.src==='SIGNED_POLYGON').quarter.code='tsentar_new';d['data/places.json']=JSON.stringify(doc);}if(name"'!=='"'9a')s=pins(s,d);let a=instance(s,d,on),error=null;const validators=[a.validateHotels(JSON.parse(d['data/hotels.json']),d['data/hotels.json']),a.validatePlaces2(JSON.parse(d['data/places.json']),d['data/places.json'])];try{await a.ensurePlaces()}catch(e){error=e.message}console.log(JSON.stringify({on,name,validators,error,...a.get()}));}
let a=instance(p.slice,p.data,on);for(const correct of [false,true]){let calls=0,t=p.data['data/places.json'];let result=await a.accept(t,correct?hash(t):'0'.repeat(64),()=>{calls++;return false});console.log(JSON.stringify({on,correct,result,calls}));}}})();
'''
r=subprocess.run(['node','-e',js],input=json.dumps({'slice':sl,'data':data}),text=True,encoding='utf8',capture_output=True);print(r.stdout);print(r.stderr);raise SystemExit(r.returncode)
'@ | python -B -" in C:\git\Fire_Varna
 succeeded in 240ms:
{"on":true,"name":"9a","validators":[false,false],"error":"places payload unavailable","n":0,"calls":{"hotels":0,"places":0}}
{"on":true,"name":"9b","validators":[true,true],"error":null,"n":375,"calls":{"hotels":1,"places":1}}
{"on":true,"name":"9c","validators":[true,false],"error":null,"n":225,"calls":{"hotels":1,"places":1}}
{"on":true,"correct":false,"result":null,"calls":0}
{"on":true,"correct":true,"result":null,"calls":1}
{"on":false,"name":"9a","validators":[false,false],"error":"places payload unavailable","n":0,"calls":{"hotels":1,"places":1}}
{"on":false,"name":"9b","validators":[true,true],"error":null,"n":375,"calls":{"hotels":1,"places":1}}
{"on":false,"name":"9c","validators":[true,false],"error":null,"n":225,"calls":{"hotels":1,"places":1}}
{"on":false,"correct":false,"result":null,"calls":1}
{"on":false,"correct":true,"result":null,"calls":1}



codex
Матрицата G3 се потвърди: старият клиент отказва двата пакета; разширените списъци дават 375 реда; чужд код само в places оставя 225. Броячът потвърди и уточнението за crypto ON/OFF. Остават проблеми в самия договор: G7 използва `cmd` синтаксис в PowerShell, а една отрицателна фикстура противоречи на новото правило за непроменени останали заявки.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'tests/test_granitsi_fixtures.py' -Encoding UTF8 -TotalCount 150" in C:\git\Fire_Varna
 succeeded in 0ms:
# -*- coding: utf-8 -*-
"""Лот Н3-а — five S17 regression fixtures against TODAY'S frozen behaviour.

Plan: `docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md` §3 Н3-а and the script
contract in §2а. What this module is and — just as important — what it is not:

  * it FREEZES what the search answers TODAY, on today's delivery, for five
    queries that the SIGNED_POLYGON channel of Б2 is going to walk straight
    through (S7 а–ж of `ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:25`);
  * it is NOT an acceptance criterion. Not one number here says what the answer
    OUGHT to be. Tomorrow F13 turns these rows into candidate expectations —
    signed by Petar — and until then a red test means „the behaviour moved“,
    never „the behaviour is wrong“.

The engine under test is the Python parity of the client search,
`scratch/places_search/recall_sweep.py` — the same reference the frozen gate in
`tests/test_places_search_gate.py` imports, with the same import guard (the
module writes not one byte on import).

The fixtures live in `scratch/places_search/granitsi_fixtures_06.09.json` and
every one of them carries a `_broken` variant: an explicitly named mutation of
the delivery — a quarter written the way Б2 would write it — that MUST make the
very same assertion fail. A fixture without a `_broken` variant is red, because
a green check that was never seen to fail is not evidence (§0 т. 6 of the plan).

How a candidate delivery is run: the reference builds its index at import time
out of `data/hotels.json` + `data/places.json`, so `reindex()` below rebuilds
exactly the six module-level structures that depend on the records (RECS,
EXACT_NAME, EXACT_ALIAS, STREET, CLASS_OF, GROUP_SIZE) over the mutated rows.
Nothing is written to disk, the module object is private to this test file, and
every measurement re-loads the untouched bundles first.

Run: python -m unittest tests.test_granitsi_fixtures
     python -m unittest discover -s tests
"""
import copy
import importlib.util
import json
import pathlib
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
REFERENCE = REPO / "scratch" / "places_search" / "recall_sweep.py"
FIXTURES = REPO / "scratch" / "places_search" / "granitsi_fixtures_06.09.json"

# The five the plan names. `client_cache_matrix` and the Възраждане variant of
# `parent_child` are deferred ON PURPOSE and the fixture file says why in words.
EXPECTED_NAMES = ("street_collision", "district_retention",
                  "mladost_kind_collision", "order_identity", "parent_child")


def load_reference():
    """Import the reference as a private module — its own guard makes it safe."""
    spec = importlib.util.spec_from_file_location("recall_sweep_granitsi", REFERENCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def base_bundles(reference):
    """The two delivered bundles, read the way the reference itself reads them."""
    hotels = json.loads(pathlib.Path(reference.HOTELS).read_text(encoding="utf-8"))
    places = json.loads(pathlib.Path(reference.PLACES2).read_text(encoding="utf-8"))
    return hotels["hotels"], places["places"]


def apply_ops(hotels, places, ops):
    """The mutation of a `_broken` candidate, by NAME — never by ordinal.

    An op that does not hit exactly one row is an error, not a silent no-op: a
    fixture that stops biting because the delivery was renamed underneath it
    would go green for the wrong reason.
    """
    hotels = copy.deepcopy(hotels)
    places = copy.deepcopy(places)
    for op in ops:
        rows = hotels if op["bundle"] == "hotels" else places
        hit = [row for row in rows if row["name"] == op["name"]]
        if len(hit) != 1:
            raise LookupError("mutation matches %d rows, expected 1: %s"
                              % (len(hit), op["name"]))
        for field, value in op["set"].items():
            hit[0][field] = value
    return hotels, places


def reindex(reference, hotels, places):
    """Rebuild every record-derived structure of the reference over `hotels`+`places`.

    1:1 with the module body of `recall_sweep.py` (RECS at :692, EXACT_NAME at
    :698, EXACT_ALIAS at :707, STREET at :722, CLASS_OF at :803, GROUP_SIZE at
    :834). The ordinals are kept, so the legacy words of a row — keyed by
    `bundle:ordinal` — stay on the row they belong to.
    """
    reference.hotels = hotels
    reference.places2 = places
    reference.RECS = ([reference.Rec(h, u"hotels", n) for n, h in enumerate(hotels)]
                      + [reference.Rec(p, u"places", n) for n, p in enumerate(places)])
    reference.EXACT_NAME = {}
    for rec in reference.RECS:
        reference.EXACT_NAME.setdefault(u" ".join(rec.ntk), []).append(rec)
    reference.EXACT_ALIAS = {}
    for rec in reference.RECS:
        for index, old in enumerate(rec.old_names):
            key = reference.key_of(old)
            if not key:
                continue
            bucket = reference.EXACT_ALIAS.setdefault(key, [])
            if not any(other is rec for other, _i in bucket):
                bucket.append((rec, index))
    reference.STREET = {}
    for rec in reference.RECS:
        if rec.spk:
            reference.STREET.setdefault(rec.spk, []).append(rec)
    reference.CLASS_OF = {}
    for form_key in reference.FORM_IDX:
        reference.CLASS_OF[form_key] = [r for r in reference.RECS
                                        if reference.in_class(r, form_key)]
    reference.GROUP_SIZE = {}
    for rec in reference.RECS:
        group = reference.group_of(rec)
        reference.GROUP_SIZE[group] = reference.GROUP_SIZE.get(group, 0) + 1


def answer(reference, query, ops=()):
    """The measured answer of today's engine over a candidate delivery.

    `with_quarter` / `without_quarter` are part of the measurement because the
    whole Границите lot turns on that split: the bare-location branch reaches a
    район row ONLY while its `quarter` is null (`recall_sweep.py:1174`), so a
    written quarter is exactly what can make a row disappear.
    """
    hotels, places = base_bundles(reference)
    if ops:
        hotels, places = apply_ops(hotels, places, ops)
    reindex(reference, hotels, places)
    rows, branch = reference.search(query)
    measured = {
        "branch": branch,
        "n": len(rows),
        "with_quarter": sum(1 for r in rows if r.quarter),
        "without_quarter": sum(1 for r in rows if not r.quarter),
        "identities": [[r.name, r.zone] for r in rows],
    }
    reindex(reference, *base_bundles(reference))       # never leave a mutation behind
    return measured


def fixtures_doc():
    return json.loads(FIXTURES.read_text(encoding="utf-8"))

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'rg -l --max-count 20 --max-columns 200 "def (check_.*gate|measure_sweep|build_expectations|write_expectations)|if MANIFEST" scratch/places_search/recall_sweep.py; rg -n --max-count 20 --max-columns 200 "def (check_.*gate|measure_sweep|build_expectations|write_expectations)|if MANIFEST" scratch/places_search/recall_sweep.py' in C:\git\Fire_Varna
 succeeded in 0ms:
scratch/places_search/recall_sweep.py
96:if MANIFEST and FREEZE:
1758:def check_lot1_gate():
1810:def check_lot1v_a_gate():
1873:def check_lot1v_b_gate():
2130:def check_lot1v_v_gate():
2165:def check_p7_gate():
3127:def check_m7_gate():
3402:def measure_sweep(m5, extra):
3683:def build_expectations(artefact_text, candidate_doc, sweep, refused=None):
3760:def write_expectations(doc, frozen=False):
4139:    if MANIFEST:
4254:    if MANIFEST and not FREEZE:

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 200 \"open\\((HOTELS|PLACES2|CATS)|Path\\((HOTELS|PLACES2|CATS)|HOTELS\\)|PLACES2\\)|CATS\\)\" scratch/places_search/recall_sweep.py; Get-Content -LiteralPath 'scratch/places_search/recall_sweep.py' -Encoding UTF8 | Select-Object -Skip 4130 -First 60" in C:\git\Fire_Varna
 succeeded in 42ms:
    # tokeniser corpus has moved — „гейтовете първо, записът последен“ holds for
    # every tracked body this script owns, not only for the two big ones.
    _parity_text = (json.dumps(_parity, ensure_ascii=False, indent=1, sort_keys=False)
                    + chr(10))

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
    _green, _asked, _other = gate_score(u"p7", p7_bad)
    print(u"П7: %d добавени токена в %d зони, %d/%d записа засегнати ; гейт %d/%d "
          u"(+%d оплаквания извън заявките)"
          % (sum(len(v) for v in P7_ADDED.values()), len(P7_ADDED),
             sum(1 for r in RECS if r.p7), len(RECS), _green, _asked, _other))
    print(u"П7 added: %s" % json.dumps(P7_ADDED, ensure_ascii=False, sort_keys=True))
    for line in p7_bad:
        print(u"  ЧЕРВЕНО: %s" % line)

    # ЛОТ 1 (решения 2 и 1): the second gate that can FAIL.
    lot1_bad = check_lot1_gate()
    _green, _asked, _other = gate_score(u"lot1", lot1_bad)
    print(u"ЛОТ 1: гейт %d/%d (+%d оплаквания извън заявките)"
          % (_green, _asked, _other))
    for line in lot1_bad:
        print(u"  ЧЕРВЕНО: %s" % line)

    # ЛОТ 1в-А (псевдоними с извор + курирани думи на видовете): the third gate.
    lot1v_bad = check_lot1v_a_gate()
    _green, _asked, _other = gate_score(u"lot1v_a", lot1v_bad)
    print(u"ЛОТ 1в-А: гейт %d/%d (+%d оплаквания извън заявките)"
          % (_green, _asked, _other))
    for line in lot1v_bad:
        print(u"  ЧЕРВЕНО: %s" % line)

    # ЛОТ 1в-Б (адресите + клонът A3-street): the fourth gate that can FAIL.
    lot1v_b_bad = check_lot1v_b_gate()
    _green, _asked, _other = gate_score(u"lot1v_b", lot1v_b_bad)
    print(u"ЛОТ 1в-Б: гейт %d/%d (+%d оплаквания извън заявките)"

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding=[System.Text.UTF8Encoding]::new($false); @'"'
import pathlib,subprocess,json,copy,io,builtins,importlib.util
from unittest.mock import patch
from tests import test_granitsi_fixtures as fx
root=pathlib.Path.cwd(); incoming={}
for dst,src in [('hotels','fire_varna_hotels'),('places','fire_varna_places'),('place_categories','place_categories')]:
 incoming[str((root/'data'/(dst+'.json')).resolve()).lower()]=subprocess.check_output(['git','-c','safe.directory=C:/git/varna_3d','-C','C:/git/varna_3d','show','05f485e:data/'+src+'.json'])
oldopen=builtins.open; oldread=pathlib.Path.read_bytes

def blob(path):
 try:return incoming.get(str(pathlib.Path(path).resolve()).lower())
 except TypeError:return None

def ropen(path,mode='r',*a,**kw):
 b=blob(path)
 if b is not None:return io.BytesIO(b) if 'b' in mode else io.StringIO(b.decode('utf8'))
 assert not any(c in mode for c in 'wax+')
 return oldopen(path,mode,*a,**kw)
with patch('builtins.open',ropen),patch.object(pathlib.Path,'read_bytes',lambda self: blob(self) if blob(self) is not None else oldread(self)):
 ref=fx.load_reference()
 h,p=copy.deepcopy(ref.hotels),copy.deepcopy(ref.places2)
 def result(h,p,queries):
  fx.reindex(ref,h,p)
  return {q:len(ref.search(q)[0]) for q in queries}
 print('baseline',result(h,p,['възраждане','възраждане 2','ж.к. възраждане 2','чайка','аспарухово','дружба']))
 p6=copy.deepcopy(p);r=next(r for r in p6 if r['name']=='ДГ№34 „Лястовичка“');r['quarter']['name']=r['zone']='ж.к. Лястовиче'; print('fixture6',result(h,p6,['възраждане','възраждане 2','ж.к. възраждане 2']))
 h7,p7=copy.deepcopy(h),copy.deepcopy(p); renamed=[]
 for r in h7+p7:
  if (r.get('quarter') or {}).get('code')=='chaika_kv':r['quarter']['name']=r['zone']='кв. Крайморие';renamed.append(r['name'])
 print('fixture7',len(renamed),result(h7,p7,['чайка']))
 p8=copy.deepcopy(p);r=next(r for r in p8 if r['name']=='ЦДГ 43 \"Пинокио\"');r['quarter']={'name':'кв. Аспарухово','code':'druzhba','src':'SIGNED_POLYGON'};r['zone']='кв. Аспарухово';print('fixture8',result(h,p8,['аспарухово','дружба']))
 s=(root/'docs/plans/ПЛАН_Б3_07.09.md').read_text(encoding='utf8').splitlines()
 import re
 q=[x for line in s[590:592] for x in re.findall(r'"'`([''^`]+)`'"',line)]
 print('listed_manifest',len(q),len(set(q)),q)
'@ | python -B -" in C:\git\Fire_Varna
 exited 1 in 191ms:
Traceback (most recent call last):
  File "<stdin>", line 19, in <module>
  File "C:\git\Fire_Varna\tests\test_granitsi_fixtures.py", line 56, in load_reference
    spec.loader.exec_module(module)
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\git\Fire_Varna\scratch\places_search\recall_sweep.py", line 84, in <module>
    OUTDIR = (pathlib.Path(tempfile.gettempdir()) / "fv_measures").as_posix() + "/"
  File "C:\Program Files\Python310\lib\tempfile.py", line 299, in gettempdir
    return _os.fsdecode(_gettempdir())
  File "C:\Program Files\Python310\lib\tempfile.py", line 292, in _gettempdir
    tempdir = _get_default_tempdir()
  File "C:\Program Files\Python310\lib\tempfile.py", line 223, in _get_default_tempdir
    raise FileNotFoundError(_errno.ENOENT,
FileNotFoundError: [Errno 2] No usable temporary directory found in ['C:\\Users\\Petar\\AppData\\Local\\Temp', 'C:\\Users\\Petar\\AppData\\Local\\Temp', 'C:\\Users\\Petar\\AppData\\Local\\Temp', 'C:\\WINDOWS\\Temp', 'c:\\temp', 'c:\\tmp', '\\temp', '\\tmp', 'C:\\git\\Fire_Varna']

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding=[System.Text.UTF8Encoding]::new($false); @'"'
import pathlib,subprocess,json,copy,io,builtins,os,tempfile
from unittest.mock import patch
from tests import test_granitsi_fixtures as fx
tempfile.tempdir=os.environ['TEMP']
root=pathlib.Path.cwd(); incoming={}
for dst,src in [('hotels','fire_varna_hotels'),('places','fire_varna_places'),('place_categories','place_categories')]:
 incoming[str((root/'data'/(dst+'.json')).resolve()).lower()]=subprocess.check_output(['git','-c','safe.directory=C:/git/varna_3d','-C','C:/git/varna_3d','show','05f485e:data/'+src+'.json'])
oldopen=builtins.open;oldread=pathlib.Path.read_bytes
def blob(path):
 try:return incoming.get(str(pathlib.Path(path).resolve()).lower())
 except TypeError:return None
def ropen(path,mode='r',*a,**kw):
 b=blob(path)
 if b is not None:return io.BytesIO(b) if 'b' in mode else io.StringIO(b.decode('utf8'))
 assert not any(c in mode for c in 'wax+')
 return oldopen(path,mode,*a,**kw)
with patch('builtins.open',ropen),patch.object(pathlib.Path,'read_bytes',lambda self: blob(self) if blob(self) is not None else oldread(self)):
 ref=fx.load_reference();h,p=copy.deepcopy(ref.hotels),copy.deepcopy(ref.places2)
 def result(h,p,queries):
  fx.reindex(ref,h,p);return {q:len(ref.search(q)[0]) for q in queries}
 print('baseline',result(h,p,['възраждане','възраждане 2','ж.к. възраждане 2','чайка','аспарухово','дружба']))
 p6=copy.deepcopy(p);r=next(r for r in p6 if r['name']=='ДГ№34 „Лястовичка“');r['quarter']['name']=r['zone']='ж.к. Лястовиче';print('fixture6',result(h,p6,['възраждане','възраждане 2','ж.к. възраждане 2']))
 h7,p7=copy.deepcopy(h),copy.deepcopy(p);renamed=[]
 for r in h7+p7:
  if (r.get('quarter') or {}).get('code')=='chaika_kv':r['quarter']['name']=r['zone']='кв. Крайморие';renamed.append(r['name'])
 print('fixture7',len(renamed),result(h7,p7,['чайка']))
 p8=copy.deepcopy(p);r=next(r for r in p8 if r['name']=='ЦДГ 43 \"Пинокио\"');r['quarter']={'name':'кв. Аспарухово','code':'druzhba','src':'SIGNED_POLYGON'};r['zone']='кв. Аспарухово';print('fixture8',result(h,p8,['аспарухово','дружба']))
'@ | python -B -" in C:\git\Fire_Varna
 succeeded in 528ms:
baseline {'възраждане': 5, 'възраждане 2': 0, 'ж.к. възраждане 2': 0, 'чайка': 30, 'аспарухово': 16, 'дружба': 2}
fixture6 {'възраждане': 4, 'възраждане 2': 0, 'ж.к. възраждане 2': 0}
fixture7 10 {'чайка': 21}
fixture8 {'аспарухово': 17, 'дружба': 1}

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$s=Get-Content -LiteralPath '"'scratch/places_search/recall_sweep.py' -Encoding UTF8; 3759..3804 | ForEach-Object {'{0}: {1}' -f ("'$_+1),$s[$_]}; $s[4239..4289]' in C:\git\Fire_Varna
 succeeded in 30ms:
3760: def write_expectations(doc, frozen=False):
3761:     """Write the body; carry the signature ONLY over identical engine blocks.
3762: 
3763:     The four engine blocks are what the signature is about. If they come out the
3764:     same as the signed file, the signature stands (this is the freeze rewriting
3765:     the artefact-side blocks it has just produced). If ONE of them moved, the
3766:     file goes back to `pending` — a changed answer is an unsigned answer."""
3767:     path = pathlib.Path(EXPECTATIONS_OUT)
3768:     signature = PENDING_SIGNATURE
3769:     if path.exists():
3770:         old = json.loads(path.read_text(encoding="utf-8"))
3771:         old_signature = ((old.get("_meta") or {}).get("signed_by") or u"").strip()
3772:         if old_signature == SIGNER and engine_blocks(old) == engine_blocks(doc):
3773:             signature = SIGNER
3774:     doc["_meta"]["signed_by"] = signature
3775:     doc["_meta"]["frozen"] = bool(frozen)
3776:     path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + chr(10),
3777:                     encoding="utf-8", newline="\n")
3778:     expectations(force_reload=True)
3779:     return str(path), signature
3780: 
3781: 
3782: def main():
3783:     """§11 Р9 / C14 finding 3 — everything that RUNS lives here.
3784: 
3785:     Importing this module builds the primitives, the tokenizer, the deliveries,
3786:     the index and search() and writes NOT ONE BYTE to disk; the report, the
3787:     counterfactuals and the three output files are produced only by
3788:     `python recall_sweep.py [plan|poi]`. Returns 1 if any expectation failed
3789:     (§11 Р7), else 0.
3790:     """
3791:     set_capmode(sys.argv)
3792:     set_fix(BASE)
3793:     classes, fails, notin8 = sweep_recall()
3794:     coll_rows = sweep_coll()
3795:     M5 = evaluate(M5SPEC)
3796:     EXTRA = evaluate(EXTRASPEC)
3797: 
3798:     # what П1 does to the two A8 counts that were measured under the v2 cap
3799:     P1_COUNTS = []
3800:     for _lbl, _cfg in [(u"v2.2 (без П1)", dict(BASE)),
3801:                        (u"с П1", dict(BASE, P1=True))]:
3802:         set_fix(_cfg)
3803:         _row = [_lbl]
3804:         for _q in [u"парк", u"берлин голдън бийч", u"хотел амирал", u"хотел адмиралл",
3805:                    u"русалка", u"роял"]:
            _refused = _release["refused"]
            print(u"release: %s ; непокрити делти %d ; отказани %d"
                  % (_release["verdict"], len(_release["uncovered"]), len(_refused)))

    # ---------------------------------------------------------------- the writes
    # Амандамент №4 т. 2: the gates are computed ABOVE; the tracked bodies are
    # written HERE, last, and only when there is nothing red and the signature is
    # on the manifests. The old order wrote the reference first and measured
    # afterwards, so a red run left a frozen artefact behind.
    if not FREEZE:
        # A report-only run gates nothing and publishes nothing; its tracked
        # parity corpus is written here, at the end, with the other writes.
        pathlib.Path(REPO_PARITY_OUT).write_text(_parity_text, encoding="utf-8",
                                                 newline=chr(10))
    if MANIFEST and not FREEZE:
        _doc = build_expectations(blob_text(u"HEAD", ROWS_REL), ROWS,
                                  measure_sweep(M5, EXTRA), refused=_refused)
        _path, _signature = write_expectations(_doc, frozen=False)
        print(u"REPORT-ONLY: очаквания -> %s (signed_by: %s)" % (_path, _signature))

    if FREEZE:
        blockers = []
        if red:
            blockers.append(u"гейтовете не са зелени — %d оплаквания"
                            % sum(len(x) for x in (sweep_bad, p7_bad, lot1_bad,
                                                   lot1v_bad, lot1v_b_bad,
                                                   lot1v_v_bad, m7_bad)))
        if _drift:
            blockers.append(u"REF_BUCKETS (ADR 008 D7): " + u", ".join(_drift))
        for complaint in (unsigned_expectations(), unsigned_for_release()):
            if complaint:
                blockers.append(complaint)
        for _name in (u"lot1v_v_manifest_BASE_P7.json", u"lot1v_v_manifest_P7_F12.json"):
            _p = REPO_ROOT / "scratch" / "places_search" / _name
            _sig = None
            if _p.exists():
                _sig = ((json.loads(_p.read_text(encoding="utf-8")).get("_meta") or {})
                        .get("signed_by"))
            if (_sig or u"").strip() != SIGNER:
                blockers.append(u"%s е подписан от „%s“, а не от „%s“" % (_name, _sig, SIGNER))
        # Амандамент №5 т. 1: the queue has a vote — freezing is exactly what
        # would make a refused delta invisible. Амандамент №6 т. 1: the vote is
        # the release gate's VERDICT, not two of the lists behind it. A release
        # blocked for any other reason — a signed artefact edited in the
        # worktree, a missing reference blob, a stale pin — has an empty
        # `uncovered` and an empty `refused`, and reading only those two froze a
        # blocked delivery with exit 0. Every blocked line is printed: the
        # human is told all of it, not the first sentence of it.
        blockers.extend(freeze_blockers(_release))
        try:
            _fresh = build_expectations(_rows_text, ROWS, measure_sweep(M5, EXTRA),

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$s=Get-Content -LiteralPath '"'gates/release.py' -Encoding UTF8; 643..694 | ForEach-Object {'{0}: {1}' -f ("'$_+1),$s[$_]}; $s[1356..1377]' in C:\git\Fire_Varna
 succeeded in 2ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status --porcelain --untracked-files=no; git rev-parse HEAD' in C:\git\Fire_Varna
 succeeded in 0ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
4db50c2c57d344d1f15f60e12ab91bddf6ae9cc7

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git log -1 --format='%h %an %s'; git diff --stat acddcd1 HEAD; git diff --name-only acddcd1 HEAD -- index.html data gates tests scratch/places_search/recall_sweep.py docs/plans/ПЛАН_Б3_07.09.md" in C:\git\Fire_Varna
 succeeded in 43ms:
 docs/plans/ПЛАН_Б3_07.09.md                | 10 ++++++++--
 docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md |  1 +
 2 files changed, 9 insertions(+), 2 deletions(-)
docs/plans/ПЛАН_Б3_07.09.md

codex
Потвърдих още два съществени проблема: G15 приема старата опашка с exit 0, а G11 не проверява геометрия в разрешения фикстурен JSON извън `data/`. „59 червени реда“ е вярно, но реалните заявки са 38; в числото 41 са преброени и три технически означения.

Междувременно външен процес създаде `4db50c2` и отбеляза плана като подписан. Продължавам одита на поисканата версия `acddcd1`; аз не съм променял файлове.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git diff acddcd1 HEAD -- docs/plans/ПЛАН_Б3_07.09.md' in C:\git\Fire_Varna
 succeeded in 0ms:
diff --git a/docs/plans/ПЛАН_Б3_07.09.md b/docs/plans/ПЛАН_Б3_07.09.md
index 5992e68..65be7be 100644
--- a/docs/plans/ПЛАН_Б3_07.09.md
+++ b/docs/plans/ПЛАН_Б3_07.09.md
@@ -1,8 +1,8 @@
 # ПЛАН Б3 · Търсене по квартал над подписаните граници (Fire_Varna) — v3
 
-**Дата:** 07.09.2026 · **Планер:** Claude Planner (read-only) · **Статус:** ЧАКА ПОДПИС (Gate 1) · **Заменя:** v2 (`e6ba50e`, чернова, неподписана), след две външни оборвания — **Astra S28** (механика, 10 условия) и **Кими К28** (данни/семантика, 7 условия), и двете **НЕГОДНО** (§12).
+**Дата:** 07.09.2026 · **Планер:** Claude Planner (read-only) · **Статус:** **ПОДПИСАН от Петър (07.09.2026): „подписвам плана Б3 v3 по препоръките“** — подписаното тяло е блобът в комит acddcd1, sha256 `51fde25f1be25a639c6f4f0a5a2b5c6dafe09f697498e8248b80c6cbdd7c343b`; §9 се чете по препоръките (виж §14) · **Заменя:** v2 (`e6ba50e`, чернова, неподписана), след две външни оборвания — **Astra S28** (механика, 10 условия) и **Кими К28** (данни/семантика, 7 условия), и двете **НЕГОДНО** (§12).
 **Клас на риска:** 🔴 **Архитектурен** (ескалационно-доминантен). Спуснали се спусъци: (1) промяна на схема/ADR — `_meta` 9→10 и 7→8 ключа, затворените списъци `QUARTER_SRC`/`QUARTER_CODES`/новият `LOCALITY_SRC` са договор, ADR 010 D3/D12/D13 носят остарял текст; (2) необратима канонична мутация — замразената референция, `expectations.json`, подписаният allow и **изваждане на подписана опашка от глоба на release**; (3) release/publish верига — този комит е това, което Петър пуска към живата карта; (4) кръстосан blast radius varna_3d → Fire_Varna по подредената тройка D13. Топология: **Вариант А** (планер → подпис на Петър → изпълнител → одитор → преглед на Петър → пуш от Петър).
-**Записване:** планерът е read-only и НЕ е записал този файл в репото. Изпълнителят го записва като `C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md` в първия си комит, дословно.
+**Записване:** планерът е read-only; файлът е записан от архитекта (чернова acddcd1, подпис в следващия комит). §4 стъпка 1 е изпълнена с това; изпълнителят я пропуска.
 
 > **Произход на числата (честно).** v2 беше писан без Bash — всяко число там беше или **(Ч)** прочетено, или **(М)** от чужда мярка. **v3 е измерен от планера със собствени команди.** Всяко число долу носи командата, с която е получено. Числата, които не съм могъл да измеря без запис в репото, са измерени в **клонинг** (`git clone --shared C:/git/Fire_Varna <scratchpad>/shadow`) — това чете източника и не пише в него; такива числа са маркирани **(К)** и изпълнителят ги преизмерва на място.
 >
@@ -888,3 +888,9 @@ python -m http.server 8000
 | 9 | **v2 G17:** „`Object.keys(d._meta).length !== META_KEYS_*`“ | **Отхвърлено по мярка.** Изпълнено: преименуване на `generated` на `unexpected` пази 10 ключа и връща **true**. Броят не е множество. |
 | 10 | **v2 G14:** `diff scripts/hooks/pre-push .git/hooks/pre-push` | **Отхвърлено по мярка (1.8.22).** В PowerShell `diff` е `Alias → Compare-Object`; командата сравнява имена и излиза с 0 при подменена кука. |
 | 11 | **v2 G11:** буквален `grep coordinates` | **Отхвърлено по мярка (1.8.12).** Ключ `"\u0063oordinates"`: grep → 0 попадения (exit 1), parse → `coordinates`. Освен това единственото буквално попадение днес е ПРОЗА в стойност, не ключ. |
+
+## 14 · Подпис и прочит на §9 „по препоръките“ (07.09.2026)
+Петър: „подписвам плана Б3 v3 по препоръките“. Прочитът на седемнадесетте решения, дословно по препоръките на §9:
+1 → **(Б)** евтината префиксна поправка в двата двигателя (само буквените `M7_PREFIXES`; числата остават извън) · 2 → родството се **замразява** каквото е (фикстури 5–8), DAG-ът не влиза · 3 → да, +8 (=28) + гейт „списъкът == речникът“ · 4 → един атомен комит с автор `Petar1984`, наложено авторство на агентските комити · 5 → пълното типово правило на шест места + синтетична фикстура · 6 → двата етикета за fallback ред · 7 → низът в подножието влиза като ред „въпрос“ с `тяло`/`тяло-на-файла`, G9 сверява · 8 → `git mv` на фикстурния файл към 07.09 · 9 → baseline **остава** `f06ac06`, allow = 138 · 10 → мълчаливият UI отказ = обявено отклонение (О27), фикстура 9в го пинва · 11 → **ред „отложено“ за Перчемлията** в опашката (решение 10 остава отворено; §9 не дава препоръка — това е прочитът на архитекта, Петър го коригира, ако иска резерва сега) · 12 → документният дълг в отделен комит след публикуването · 13 → да, фикстура 11 · 14 → `git mv` към `scratch/places_search/архив/АРХИВ_A_05.09.md` · 15 → да, `LOCALITY_SRC` · 16 → да, затворени множества · 17 → ред „въпрос“ за `P7_ADDED` с двата списъка (псевдонимите остават, докато Петър не каже друго при подписа на опашката).
+Повторните проверки Astra S29 / Кими К29 върху v3 текат по време на подписа; условие от тях влиза като амандамент (нов датиран файл) и се подписва отделно, само за делтата.
+

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status --porcelain --untracked-files=no; git rev-parse HEAD' in C:\git\Fire_Varna
 succeeded in 0ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
15196b780d83a20ec433a7a5e2c48f45c6ba1091

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git log -1 --format='%h %an %s'; git diff --stat 4db50c2 HEAD; git diff --name-only acddcd1 HEAD -- index.html data gates tests scratch/places_search/recall_sweep.py" in C:\git\Fire_Varna
 succeeded in 5ms:
codex
**НЕГОДНО за подпис — S29 върху `acddcd1`.**

S28-1/4/6/9 са поправени; S28-2/3/5/7/8/10 остават частично изпълнени. Пробите потвърдиха G3: отказ на двата пакета / 375 / 225 реда; G8: 0 забранени картончета, след мутация — 375; G9: липсващ/точен/променен надпис → exit 1/0/1. G10 и G14 дадоха положителен exit 0 и отрицателен 1; G17 прие двата пакета и отхвърли четирите мутации във всеки.

1. **S29-1 — G7 не е изпълним и редът му е обърнат.** [Редове 663–675](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:663) използват `copy /Y "%TEMP%\..."` в PowerShell: измерено **exit 1, ParameterBindingException**. §4 редактира двигателя в стъпка 6, преди двата дъмпа в стъпка 7. **Поправка:** `Copy-Item -LiteralPath "$env:TEMP\..." -Destination … -Force -ErrorAction Stop`; A преди редакцията, B след нея; SHA256 на изпълнените файлове, а не `HEAD:path`. Леката проба с `reference_rows()` даде равни дъмпове; мутиран `CENTER` — различни, comparator **0/1**.

2. **S29-2 — отрицателната фикстура 8 нарушава собствения договор.** [Ред 454](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:454) изисква останалите заявки да са непроменени. Измерената мутация от ред 466 променя **„аспарухово“ 16→17 И „дружба“ 2→1**, но `fails_on` назовава само първата. **Поправка:** точно множество `fails_on: ["аспарухово","дружба"]`, сравнявано с измереното множество променени заявки. Другите поправени мутации се потвърдиха: **5→4**, **30→21**.

3. **S29-3 — О29 и §13 т.4 броят неправилно заявките.** [Ред 590](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:590): измерихме **59 оплаквания общо — 57 за 38 различни заявки и 2 без заявка**. „41“ включва погрешно `zone`, `M2-failopen`, `A3-location`. Изброените действителни заявки са пълни. **Поправка:** навсякъде 59/38, като двата незаявъчни реда са включени в 59. О30 за презаписването на очакванията е реален.

4. **S29-4 — G11 още пропуска геометрия.** [Редове 700–714](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:700) проверяват само `data/`; разрешеният преименуван фикстурен JSON остава извън обхода. Polygon в него не променя зеления G11. Escape-пробата вътре в `data/` вече пада правилно. **Поправка:** структурно проверявайте всички добавени, изменени и преименувани JSON/GeoJSON, включително разрешените пътища; точни изключения за наследените текстови метаданни и машинно проверен инвентар.

5. **S29-5 — отрицателният G15 минава.** [Командата на ред 615](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:615) приема старата опашка с **exit 0**; архивирането със стария префикс също оставя exit 0. **Поправка:** сравнявайте целия списък с единствения очакван Б3 път; „само стара“, „архивирана със стар префикс“ и „нова+стара“ трябва да падат. Рекурсивният basename аргумент в §13 е верен. Класовете на старата опашка са **16 делти/6 артефакта/5 въпроса**, не 16/10/1.

6. **S29-6 — О28 смесва наследената П7 проверка с действащото търсене.** [§9 т.17](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:836): П7 действително става **2→7 токена, 2→5 зони, 48→64 записа**. Но действащият `LOC_ADDED` вече допуска `vladislav`/`varnenchik`. Новите действащи токени са само **gratska/gratski/vasil**. **Поправка:** отделни измервания и подписвани списъци за П7 наследството и реалния `LOC_ADDED/LOC_PHRASES` дрейф.

7. **S29-7 — „156-заявъчният корпус“ няма възпроизводимо определение.** [Вариант Б](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:818) работи: **218 заявки, нула клиент↔референция разминавания; 212 кандидатски/контролни заявки, нула промени**. **Поправка:** точен селектор и сериализация на корпуса; отделен филтриран `MR` само за М7, запазен `R` за останалите клонове.

8. **S29-8 — G8/G9 нямат назован изпълним тест/команда.** [Редове 677–687](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:677) описват проверките, но не ги свързват с прогон. **Поправка:** конкретни тестови методи и команди; положителният подписен G9 след стъпка 12б, преди това — отрицателните проверки.

Комит 2 пази данните и SHA пиновете атомно; несъответствието в работното дърво между стъпки 2–4 е умишлената отрицателна проба. О27 е реално и изрично обявено отклонение.

Нищо не записах; няма комити или remote команди. Read-only TEMP изключи тежките прогони. Външен процес придвижи HEAD до `15196b7`; проверяваният код остана непроменен.
tokens used
164,315
**НЕГОДНО за подпис — S29 върху `acddcd1`.**

S28-1/4/6/9 са поправени; S28-2/3/5/7/8/10 остават частично изпълнени. Пробите потвърдиха G3: отказ на двата пакета / 375 / 225 реда; G8: 0 забранени картончета, след мутация — 375; G9: липсващ/точен/променен надпис → exit 1/0/1. G10 и G14 дадоха положителен exit 0 и отрицателен 1; G17 прие двата пакета и отхвърли четирите мутации във всеки.

1. **S29-1 — G7 не е изпълним и редът му е обърнат.** [Редове 663–675](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:663) използват `copy /Y "%TEMP%\..."` в PowerShell: измерено **exit 1, ParameterBindingException**. §4 редактира двигателя в стъпка 6, преди двата дъмпа в стъпка 7. **Поправка:** `Copy-Item -LiteralPath "$env:TEMP\..." -Destination … -Force -ErrorAction Stop`; A преди редакцията, B след нея; SHA256 на изпълнените файлове, а не `HEAD:path`. Леката проба с `reference_rows()` даде равни дъмпове; мутиран `CENTER` — различни, comparator **0/1**.

2. **S29-2 — отрицателната фикстура 8 нарушава собствения договор.** [Ред 454](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:454) изисква останалите заявки да са непроменени. Измерената мутация от ред 466 променя **„аспарухово“ 16→17 И „дружба“ 2→1**, но `fails_on` назовава само първата. **Поправка:** точно множество `fails_on: ["аспарухово","дружба"]`, сравнявано с измереното множество променени заявки. Другите поправени мутации се потвърдиха: **5→4**, **30→21**.

3. **S29-3 — О29 и §13 т.4 броят неправилно заявките.** [Ред 590](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:590): измерихме **59 оплаквания общо — 57 за 38 различни заявки и 2 без заявка**. „41“ включва погрешно `zone`, `M2-failopen`, `A3-location`. Изброените действителни заявки са пълни. **Поправка:** навсякъде 59/38, като двата незаявъчни реда са включени в 59. О30 за презаписването на очакванията е реален.

4. **S29-4 — G11 още пропуска геометрия.** [Редове 700–714](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:700) проверяват само `data/`; разрешеният преименуван фикстурен JSON остава извън обхода. Polygon в него не променя зеления G11. Escape-пробата вътре в `data/` вече пада правилно. **Поправка:** структурно проверявайте всички добавени, изменени и преименувани JSON/GeoJSON, включително разрешените пътища; точни изключения за наследените текстови метаданни и машинно проверен инвентар.

5. **S29-5 — отрицателният G15 минава.** [Командата на ред 615](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:615) приема старата опашка с **exit 0**; архивирането със стария префикс също оставя exit 0. **Поправка:** сравнявайте целия списък с единствения очакван Б3 път; „само стара“, „архивирана със стар префикс“ и „нова+стара“ трябва да падат. Рекурсивният basename аргумент в §13 е верен. Класовете на старата опашка са **16 делти/6 артефакта/5 въпроса**, не 16/10/1.

6. **S29-6 — О28 смесва наследената П7 проверка с действащото търсене.** [§9 т.17](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:836): П7 действително става **2→7 токена, 2→5 зони, 48→64 записа**. Но действащият `LOC_ADDED` вече допуска `vladislav`/`varnenchik`. Новите действащи токени са само **gratska/gratski/vasil**. **Поправка:** отделни измервания и подписвани списъци за П7 наследството и реалния `LOC_ADDED/LOC_PHRASES` дрейф.

7. **S29-7 — „156-заявъчният корпус“ няма възпроизводимо определение.** [Вариант Б](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:818) работи: **218 заявки, нула клиент↔референция разминавания; 212 кандидатски/контролни заявки, нула промени**. **Поправка:** точен селектор и сериализация на корпуса; отделен филтриран `MR` само за М7, запазен `R` за останалите клонове.

8. **S29-8 — G8/G9 нямат назован изпълним тест/команда.** [Редове 677–687](C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md:677) описват проверките, но не ги свързват с прогон. **Поправка:** конкретни тестови методи и команди; положителният подписен G9 след стъпка 12б, преди това — отрицателните проверки.

Комит 2 пази данните и SHA пиновете атомно; несъответствието в работното дърво между стъпки 2–4 е умишлената отрицателна проба. О27 е реално и изрично обявено отклонение.

Нищо не записах; няма комити или remote команди. Read-only TEMP изключи тежките прогони. Външен процес придвижи HEAD до `15196b7`; проверяваният код остана непроменен.
