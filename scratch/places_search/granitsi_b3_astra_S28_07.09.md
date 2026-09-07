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
session id: 01a07a5d-0ed0-7790-b9c9-1a1268d4dbac
--------
user
S28 · Оборване на ПЛАН Б3 v2 (леща механика), read-only. Файлът: C:/git/Fire_Varna/docs/plans/ПЛАН_Б3_07.09.md (v2, след три вътрешни оборвания). Подписаната основа: docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md §0, §2а, §Б3 (ред 143-145), амандамент 3 (docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md), решения 8 и 9 в docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md §4, §6-§8; ADR docs/decisions/010_signed_quarter_boundaries.md (D12, D13). Доставката на varna_3d е в комити c1bb9dc/d17de0d/05f485e на C:/git/varna_3d (клон rezhimi; чети с git -C C:/git/varna_3d show). Атакувай плана срещу РЕАЛНИТЕ файлове с измервания: (1) всеки гейт в §5 — може ли да мине без да докаже твърдението (false pass), падат ли наистина отрицателните половини; (2) редът на D13 в §4/§6 — има ли състояние между комитите, в което index.html пинва един sha, а data носи друг, и дали гейтът на доставката (gates/run_gates.py, gates/release.py, gates/sign.py, scripts/hooks/pre-push, scratch/places_search/expectations.json, gates/baseline) ще е зелен при описания ред; твърденията за опашката ЗА_ПОДПИС и allow-json (§3.8) — вярно ли е, че трябва да се изтрие подписана опашка от HEAD, и безопасно ли е; (3) Node-фикстурите §3.6 — реално ли изрязват валидаторите от index.html и наблюдаем ли е отказът при чужд код; PLACES_CACHE v7 и accept при crypto.subtle; (4) §3.2 четиринадесетте редакции — котвите верни ли са (провери редовете), типовият капан !r.e.quarter при DISTRICT_FALLBACK, речникът/родството §3.7; (5) §6 комитите — авторства, дословни съобщения, PowerShell без &&, нищо не се публикува; §2 обявените отклонения пълни ли са. Не пипай нищо, не комитвай, никаква команда към отдалечено хранилище. Присъда: ГОДНО за подпис / НЕГОДНО с номерирани условия (S28-1…), всяко с доказателство path:line или изход на команда и с точна поправка; до 900 думи.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя гейтовете срещу реалните файлове и посочените комити, включително отрицателните случаи и междинното D13 състояние. Работя само за четене, без промени, комити или команди към remote.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/activeContext.md -TotalCount 150' in C:\git\Fire_Varna
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

Parked scope (nothing opens until Ð¤Ð°Ð·Ð° A is pushed): `plans/PARKED.md`.

## Forbidden here

`git push`, Worker deploy, any publish â€” Petar only. Personal data in `data/`, in issues or in docs. New runtime or build-time dependencies, Bulgarian UI wording changes, a first load over 5 MB â€” not without Petar. Cross-repo edits from this checkout. `--freeze` on the search reference without a signed manifest. Writing `signed_by: "ÐŸÐµÑ‚ÑŠÑ€"` â€” an agent writes `pending â€” ÐŸÐµÑ‚ÑŠÑ€` and nothing else.

## Where things are

`index.html` (the whole app shell) Â· `data/hydrants.json` (runtime dataset) Â· `data/{places,hotels,place_categories}.json` (the places search, delivered from varna_3d) Â· `data/search_index.json` + `data/address_rows.json` (built in Varna_buildings) Â· `gates/` (the release gates: sha pins, key sets, cadastral scan, coverage, signed facts) Â· `worker/` (Cloudflare Worker source) Â· `sw.js` (ADR 002/005) Â· `scratch/places_search/` (the reference engine, the manifests, the boards) Â· `docs/decisions/` (ADRs) Â· `docs/plans/` (the task contracts) Â· `docs/archive/` (frozen chronicles).

Doctrine shared with Varna_buildings: ADR 004 â†’ Varna_buildings ADR 058. varna_3d generates the places delivery and consumes the hydrants for its 3D map.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status --short --branch' in C:\git\Fire_Varna
 succeeded in 0ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 81]
?? docs/plans/ПЛАН_Б3_07.09.md
?? scratch/places_search/cleanup_brief_astra.md
?? scratch/places_search/cleanup_brief_kimi.md
?? scratch/places_search/golden_brief_kimi.md
?? scratch/places_search/golden_brief_sol.md
?? scratch/places_search/granitsi_b3_astra_S28_07.09.md
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git ls-files -- AGENTS.md CLAUDE.md docs/activeContext.md 'docs/plans/ПЛАН_Б3_07.09.md' 'docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md' 'docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md' 'docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md' docs/decisions/010_signed_quarter_boundaries.md index.html data scripts tests gates scratch/places_search/expectations.json" in C:\git\Fire_Varna
 succeeded in 0ms:
AGENTS.md
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
docs/decisions/010_signed_quarter_boundaries.md
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md
gates/__init__.py
gates/allow/2026-09-05_lot1v_v.json
gates/baseline/MANIFEST.json
gates/coverage.py
gates/release.py
gates/run_gates.py
gates/sign.py
index.html
scratch/places_search/expectations.json
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
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8 -TotalCount 150 | ForEach-Object -Begin { "'$n=0 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 15ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Item -LiteralPath 'docs/plans/ПЛАН_Б3_07.09.md','docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md','docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md','docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md','docs/decisions/010_signed_quarter_boundaries.md' | Sort-Object FullName | Select-Object FullName,Length" in C:\git\Fire_Varna
 succeeded in 47ms:

FullName                                                                      Length
--------                                                                      ------
C:\git\Fire_Varna\docs\decisions\010_signed_quarter_boundaries.md              53242
C:\git\Fire_Varna\docs\plans\ПЛАН_Б3_07.09.md                                  95033
C:\git\Fire_Varna\docs\plans\ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md               62452
C:\git\Fire_Varna\docs\plans\ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md  29465
C:\git\Fire_Varna\docs\sessions\СЪСТОЯНИЕ_Границите_06.09.md                   29242



exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8 | Select-Object -Skip 150 -First 150 | ForEach-Object -Begin { "'$n=150 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
151: 
152: (М) `grep coordinates` по проследените `data/*.json`: единственото попадение е `data/hydrants_provenance.json:1`; трите доставени файла — нула. Размер (М): ≈ 2 235 872 B ≈ 2,24 MB при праг 5 MB.
153: 
154: ---
155: 
156: ## 2 · Обявени отклонения от подписания текст (искат подписа на Петър)
157: 
158: | № | Подписано | Мерено / по-късно решено | Предложено решение |
159: |---|---|---|---|
160: | **О1** | план `:144` „картончето: редът за атрибуция…“ + думите **„attribution row“** в дословното съобщение; Б0 т. 5; G27(б) | решение 8 (`СЪСТОЯНИЕ:31`): в картончето НЯМА ред за извора | „attribution row“ **излиза** от съобщението; `label`/`url` остават машинен запис — **валидират се, не се рендерират**; ново място в write-set: `index.html:1901-1918`. |
161: | **О2** | „шестте S17 фикстури“ | `tests/test_granitsi_fixtures.py:48-49` живи 5; `:180-186` замразява две отложени поименно | Б3 дължи двете + преизмерените пет + **четири нови** (§3.5). Записаният мотив за отлагането на `client_cache_matrix` е фактически неверен и се пренаписва. |
162: | **О3** | „`QUARTER_CODES` +41“ | доставката ползва 28 кода; липсват 8 | Съобщението носи **`QUARTER_CODES +8`**. |
163: | **О4** | „един атомен комит“ + три дословни съобщения + автор `Claude Executor`, а ам.3 §7 прави комит на данни от агент STOP | взаимно противоречие | **Един атомен комит с автор `Petar1984`**; изпълнителят стейджва, Петър комитва. Другите две съобщения оцеляват дословно в тялото. |
164: | **О5** | типово правило за `DISTRICT_FALLBACK` + положителна фикстура (A6) | 0 такива реда | `QUARTER_SRC` получава двете стойности; правилото се пише в **двата двигателя И в двата bundle теста** (О19); доказателството е синтетична фикстура. |
165: | **О6** | нищо; чака се решение 10 | речникът носи `с.о. Перчемлията` — районен произход неподписан | Решение 10 или поименен резерв **преди** комита, или изричен ред „отложено“ в опашката. |
166: | **О7** | районът от НАШИЯ `district.code` | решение 9 смени района на два **квартал**-полигона | В реда „вид · квартал · район“ районът остава **на МЯСТОТО** (375/375). |
167: | **О8** | D13 пинва поименно старите числа | всички се менят | D13 остава договор за **местата**; всяко число се премерва (§4 стъпка 2). |
168: | **О9** | ADR 010 D3 „затворен 9-ключов `_meta`“; G27 липсва в ADR-а | ам.2 прави набора 10-ключов | Документен дълг → **отделен комит СЛЕД пуша** (решение 12). |
169: | **О10** | „подготовка на Б3 (кръпка)“ | кръпката не съществува | Б3 тръгва на чисто по този план. |
170: | **О11** | Б1 sha `3f423898…`/61 граници | комитът на Петър `6486b48`, 60 граници, sha `74f09d505e2b` | Всяка котва сочи `6486b48` / `74f09d505e2b`. |
171: | **О12** | — | наследени дългове P1–P3, `lot1v_v_manifest.py:30` | Приемат се поименно; не се поправят тук. |
172: | **О13** | гейт „grep `coordinates` → 0 извън `data/hydrants.json`“ | попадението е в `data/hydrants_provenance.json:1` | Гейтът се преформулира (G11, §5). |
173: | **О14** | „замразената референция (нула изгубени резултати)“ | „младост“ 28→20, „училище младост“ 11→6 | „Нула изгубени“ = **нула НЕПОДПИСАНИ изгубени**; всяка делта минава през опашката. |
174: | **О15** 🔴 | §Б3 `:144` „**нормализаторът D12 за новите имена**“; ADR 010 D12 (`:60`) иска `window.__places.locationKey(q)` в паритетния корпус | (Ч) `index.html:6495-6496` + (М) 1.8.4: „кв. Левски“, „кв. Тракия“, „кв. Христо Ботев“, „ж.к. Св. Иван Рилски“ **не намират квартала си**; голото име го намира | **D12 се ОТЛАГА** (лот Б5). Ефектът се записва: осемте нови квартала се търсят САМО с голото име; типовият префикс дава чужди редове. §8 проба 4 се пренаписва на измереното. Ако Петър каже „сега“ — това е друг лот с нов паритетен корпус и нов кръг делти. |
175: | **О16** 🔴 | §Б3 `:144` „дете → детето; родител → родителят и подписаните му деца“; DAG-ът от Б0 т. 9 (11 двойки) | (М) 1.8.6: „възраждане 2“ / „младост 2“ → **0 реда**; (М) 1.8.8: `druzhba ⊂ asparuhovo` **не работи**, макар и двата да носят редове; (М) 1.8.7: фразата **слива** `chaika_kk`+`chaika_kv` без подписано родство | **Родство остава фразово и се ЗАМРАЗЯВА такова, каквото е**: работи за `mladost2`/`vazrazhdane1`/`vazrazhdane2` (споделена фраза), не работи за `druzhba`, и произвежда неподписано сливане при `chaika`. Половината „дете → детето“ **не работи** и се подписва като известно поведение. DAG-ът не влиза (иска нов износ на varna_3d). |
176: | **О17** | G27(б) (ам.2 `:103`): три фикстури — липсващ запис ✗, `url` без `wm_id` формат ✗, `_meta` с 11 или 9 ключа ✗ | (Ч) `index.html:6546-6580` **не броят ключовете на `_meta`**; (М) доставеният url е `http://wikimapia.org/900042/bg/…` — не буквата на амандамента (`https://…/<wm_id>/`) | И10 изпълнява **и трите**: затворен `_meta` набор (places 10, hotels 8), запис за всеки `SIGNED_POLYGON` код, и `url` по **измерената** форма `^https?://wikimapia\.org/\d+/` при `src === 'wikimapia'`. Отклонението от буквата на амандамента (http и път след id) се обявява. |
177: | **О18** | §3.3 на v1: „`LOCALITY_CODES` не се пипат“ | (Ч) `index.html:6537` и `tests/test_places_public_bundle.py:292` валидират **местността със `QUARTER_SRC`** — И4 би отворил местността за `SIGNED_POLYGON` и `DISTRICT_FALLBACK` | Въвежда се **`LOCALITY_SRC = ['REG','KAIS','SIGNED_OVERRIDE','SIGNED_POLYGON']`** (без `DISTRICT_FALLBACK`) на `:6537` и в двата теста. Стеснението е безплатно (доставените locality извори са REG/KAIS) и пази К27 „местност никога не пълни quarter“. |
178: | **О19** 🔴 | §Б3: „типово правило за `DISTRICT_FALLBACK`“ (само `index.html:7064`) | (Ч) същият ред е ОБРАТЕН в три Python-проверки: `recall_sweep.py:2146` (`want = quarter.name` → иска „Младост“, не „район Младост“), `:2150` (районен код → „квартал извън речника“), `tests/test_places_public_bundle.py:291-293` и `:309` (и близнакът за хотелите) | Правилото се пише **на шест места** (§3.4, §3.5): `recall_sweep.py:621,623,1123,1167,2146,2150` + двата bundle теста. Фикстура 10 минава синтетичния ред през `search`, през `qa` на референцията И през двата bundle теста. |
179: | **О20** 🔴 | `index.html:6544` днес изисква `zone === quarter.name` при непразен quarter; износителят във varna_3d следва това правило (375/375) | И6 на v1 сменя договора **едностранно, преди износителя** → първата истинска fallback доставка би паднала мълчаливо | Б3 приема **и двата** етикета за fallback ред: `zone === quarter.name || zone === 'район ' + district.name`. Затягането до само „район X“ влиза в лота, който носи и износния гейт във varna_3d (D13 звено 2). |
180: | **О21** 🔴 | v1 нарича низа в подножието „подписан“ | (Ч) `gates/release.py:177-184`: `scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json` **не е в `SIGNABLE`**; (М) последният комит по него е на `Claude Executor` (`3d747d3`). Подписано от Петър (решение 8) е само **мястото** | Низът влиза в опашката като ред **клас „въпрос“** с видимо `тяло: <sha256>` и се подписва от Петър **преди** комита на доставката. Едва тогава G9 го чете. Комитът не го нарича „подписан“ преди подписа. |
181: | **О22** 🔴 | v1 §9 т. 9: baseline → комита на доставката в същата подписна сесия | (М) 1.8.2: `base == candidate` → **exit 3**, 150 stale реда; (Ч) `gates/coverage.py:573-577,617` | **Baseline ОСТАВА `f06ac06` в комита на доставката.** Новият allow бюджетира **измерените 138 преместени реда** (1.8.1), не 30-те „непокрити днес“. Пренасочването на baseline е **отделен, по-късен подписан лот** заедно с нулиране на allow-редовете. |
182: | **О23** | v1 §4 стъпка 9: „`probe_out/token_parity.json` в `_meta.inputs`“ | (Ч) `recall_sweep.py:2815-2816` — твърда тройка; `build_expectations` я ползва буквално | Очакването **отпада**; амандамент №11 т. 4 се записва като поименен дълг (към О12). Изпълнителят НЕ пипа `INPUT_RELS`. |
183: | **О24** 🔴 | червен ред 5 „автор `Claude Executor`“ | (Ч) `gates/sign.py:139-147` отказва само при изброени агентски идентичности; git identity на репото е `Petar1984` → **агентски комит без `--author` излиза с неговото име** | Всяка агентска команда се пише дословно `git -c user.name="Claude Executor" -c user.email=executor@local commit …`. Проверката на самоличността става **следпроверка**: `git log -1 --pretty='%an <%ae> · %cn <%ce>'` след всеки комит. |
184: | **О25** 🔴 | §Б3 не казва нищо за старата опашка | (Ч) `gates/release.py:465-472` + (М) в HEAD има точно 1 опашка (`ЗА_ПОДПИС_A.md`) | Втора опашка в HEAD прави release **BLOCKED по причина, която никакъв подпис не маха**. `ЗА_ПОДПИС_A.md` се **маха от HEAD** (`git rm` или `git mv` към име ИЗВЪН глоба `ЗА_ПОДПИС_*.md`) в СЪЩИЯ комит с новата опашка. Решение на Петър: архивно име или само в историята (тя носи 27 подписани реда от 05.09). |
185: | **О26** | v1 G7: „`recall_sweep.py --dump`“ | (Ч) няма argparse, няма `--dump`; артефактът е `%TEMP%/fv_measures/lot1v_v_candidate_rows.json`; **всеки report-only прогон презаписва проследения `scratch/places_search/probe_out/token_parity.json`** (`:4249-4253`) | G7 се преписва (§5); проследеният паритетен файл се обявява в write-set-а на комит 5 (замразяването) и в §4 стъпка 6 се очаква като модифициран. |
186: 
187: ---
188: 
189: ## 3 · Write-set (точните файлове и точните редакции)
190: 
191: ### 3.1 Данни (байтов препис, нула трансформация)
192: 
193: ```bash
194: cd /c/git/Fire_Varna
195: git -C /c/git/varna_3d show 05f485e:data/fire_varna_places.json > data/places.json
196: git -C /c/git/varna_3d show 05f485e:data/fire_varna_hotels.json > data/hotels.json
197: git -C /c/git/varna_3d show 05f485e:data/place_categories.json > data/place_categories.json
198: ```
199: Git Bash — **не** PowerShell `>` (UTF-16 в PS 5.1).
200: 
201: ### 3.2 `index.html` — четиринадесет редакции, всяка с котва
202: 
203: **И1 · `:6265`** `'fire-varna-hotels-v6-225'` → `'fire-varna-hotels-v7-225'`, плюс два реда към коментара `:6262-6264` защо (57 реда сменят `quarter`/`zone` при непроменен брой; `accept` сверява sha само при `crypto.subtle`, `:6605`).
204: 
205: **И2 · `:6288-6290`** трите пина → стойностите от §1.4.
206: 
207: **И3 · `:6301-6304`** `LEGACY_BUNDLE_SHA` → places `3dffc264…`, hotels `eb8fa85c…`.
208: 
209: **И4 · `:6313`** `const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE', 'SIGNED_POLYGON', 'DISTRICT_FALLBACK'];`
210: 
211: **И4б · нов ред веднага след `:6313` (О18).**
212: ```js
213:     // Б3 (О18): the LOCALITY has its own closed source list. It shared QUARTER_SRC
214:     // (:6537) and widening that list for the quarter silently widened the locality
215:     // too — a `locality` by DISTRICT_FALLBACK is a thing no decision allows and К27
216:     // („местност никога не пълни quarter“) forbids in the other direction as well.
217:     const LOCALITY_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE', 'SIGNED_POLYGON'];
218: ```
219: и `:6537` става `if (!validLocation(r.locality, LOCALITY_SRC, LOCALITY_CODES)) return false;`
220: 
221: **И5 · `:6317-6321` `QUARTER_CODES` → 28 кода** (азбучно, същият стил на пренасяне):
222: ```
223: 'asparuhovo', 'borovets_yug', 'briz', 'chaika_kk', 'chaika_kv', 'dolna_traka',
224: 'druzhba', 'galata', 'grackata_mahala', 'hristo_botev', 'izgrev_kv',
225: 'kk_konstantin_elena', 'kolhozen_pazar', 'kv_levski', 'mladost', 'mladost2',
226: 'pobeda', 'priboy', 'sv_ivan_rilski', 'trakia', 'troshevo', 'tsentar',
227: 'vazrazhdane', 'vazrazhdane1', 'vazrazhdane2', 'vinitsa', 'vladislavovo',
228: 'zlatni_pyasatsi'
229: ```
230: `DISTRICT_CODES` (`:6315`) и `LOCALITY_CODES` (`:6322`) не се пипат.
231: 
232: **И6 · `:6535-6544` типовото правило за `DISTRICT_FALLBACK` (по О20 — двата етикета).**
233: ```js
234:     // Б3 (Б0 т. 4, О19/О20): a DISTRICT_FALLBACK quarter is the DISTRICT wearing the
235:     // quarter field. Its code comes from DISTRICT_CODES, it must BE the row's own
236:     // district, and nothing downstream may read it as a quarter — otherwise the row
237:     // silently leaves the district branches (:7064, :7118) that are its only home.
238:     function isFallbackQuarter(q) { return !!q && q.src === 'DISTRICT_FALLBACK'; }
239:     function ownQuarter(r) { return (r.quarter && !isFallbackQuarter(r.quarter)) ? r.quarter : null; }
240: ```
241: Първи клон на `validTypedLocation`:
242: ```js
243:       if (isFallbackQuarter(r.quarter)) {
244:         if (!validLocation(r.quarter, QUARTER_SRC, DISTRICT_CODES)) return false;
245:         if (!r.district || r.quarter.code !== r.district.code
246:             || r.quarter.name !== r.district.name) return false;
247:       } else if (!validLocation(r.quarter, QUARTER_SRC, QUARTER_CODES)) return false;
248: ```
249: Етикетът на `:6544` — **и двете форми, докато износителят не е затегнат (О20):**
250: ```js
251:       // О20: the exporter still writes `zone = quarter.name` for every row (375/375
252:       // measured). Refusing the old label here would kill the FIRST real fallback
253:       // delivery on the consumer side, before the producer has been changed.
254:       if (isFallbackQuarter(r.quarter))
255:         return r.zone === r.quarter.name || r.zone === DISTRICT_MARK + ' ' + r.district.name;
256:       return r.zone === (r.quarter ? r.quarter.name : DISTRICT_MARK + ' ' + r.district.name);
257: ```
258: 
259: **И7 · `:6749`, `:6782`** — `locTokens('quarter', h.quarter)` → `locTokens('quarter', ownQuarter(h))`; същото за `locPhrases`.
260: 
261: **И8 · `:7064`, `:7118`** — `!r.e.quarter` → `!ownQuarter(r.e)`.
262: 
263: **И9 · `:7266`** — `const quarter = ownQuarter(h) ? h.quarter.name : '';` Нищо не се добавя към картончето.
264: 
265: **И10 · `_meta` — трите проверки на G27(б) (О17), никакъв рендер.** До `validateCats` (`:6581`):
266: ```js
267:     // Б3 (решение 8 + G27(б), О17): the provenance map is a MACHINE record. Every
268:     // code a row carries by SIGNED_POLYGON must have a four-key entry — a delivery
269:     // we cannot credit is a delivery we refuse — the `_meta` set is CLOSED, and not
270:     // one byte of any of it reaches a card.
271:     const ATTRIB_KEYS = ['src', 'url', 'label', 'licence'];
272:     // О17: pinned to the DELIVERED shape (http, id, path), not to the literal of
273:     // амандамент №2 („https://wikimapia.org/<wm_id>/“) — measured 07.09.
274:     const WM_URL = /^https?:\/\/wikimapia\.org\/\d+\//;
275:     function validQuarterAttribution(meta, rows) {
276:       const map = meta && meta.quarter_attribution;
277:       if (!map || typeof map !== 'object' || Array.isArray(map)) return false;
278:       for (const k of Object.keys(map)) {
279:         const e = map[k];
280:         if (!e || typeof e !== 'object' || Array.isArray(e)) return false;
281:         if (Object.keys(e).length !== ATTRIB_KEYS.length) return false;
282:         for (const f of ATTRIB_KEYS) if (typeof e[f] !== 'string' || !e[f]) return false;
283:         if (e.src === 'wikimapia' && !WM_URL.test(e.url)) return false;
284:       }
285:       for (const r of rows)
286:         if (r.quarter && r.quarter.src === 'SIGNED_POLYGON' && !map[r.quarter.code]) return false;
287:       return true;
288:     }
289:     const META_KEYS_HOTELS = 8, META_KEYS_PLACES = 10;   // ам.2 :103 — затворен набор
290: ```
291: Извиква се веднъж в `validateHotels` (след `:6549`) и веднъж в `validatePlaces2` (след `:6568`):
292: ```js
293:       if (Object.keys(d._meta).length !== META_KEYS_HOTELS) return false;      // …PLACES в другия
294:       if (!validQuarterAttribution(d._meta, d.hotels)) return false;           // …d.places
295: ```
296: `EXPECT_KEYS`/`EXPECT2_KEYS`, `EXPECT_COUNT`/`EXPECT2_COUNT` не се пипат.
297: 
298: **И11 · Низът в подножието — влиза САМО след подписа на Петър (О21).** След `:1902`:
299: ```js
300:   // Б3 (решение 8, 07.09): the line for the quarter boundaries lives in the map's

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/activeContext.md -Encoding UTF8 -TotalCount 22' in C:\git\Fire_Varna
 succeeded in 5ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git log -1 --format='%H %an <%ae> %s'" in C:\git\Fire_Varna
 succeeded in 0ms:
f00dd781ba8c41d70f84c4f1621c04b65afd1d74 Claude Architect <architect@local> state: §8 — Б2 closed by Petar's three varna_3d commits (c1bb9dc, d17de0d, 05f485e; OID 7/7), Б3 planning workflow started

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8 | Select-Object -Skip 300 -First 150 | ForEach-Object -Begin { "'$n=300 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 61ms:
301:   // small print, next to the basemap credit, and never on a place card. It is added
302:   // ONCE and survives every basemap swap: `attribCtrl` is a single control (:1917)
303:   // and setBasemap/enable/removeOfflineBasemap (:4543-4549, :4663, :4672-4676)
304:   // remove only their OWN strings — including under the sticky override (:4571-4574).
305:   const QUARTERS_ATTRIB = 'Кварталните граници в този файл са по Wikimapia.org (© Wikimapia contributors, CC BY-SA, ToS §1.G: връзка към обекта + „Wikimapia.org“ с връзка към http://wikimapia.org); карето „Младост 2“ е по улични оси от OpenStreetMap (© OpenStreetMap contributors, ODbL, https://www.openstreetmap.org/copyright). Геометрия НИКОГА не пътува публично.';
306: ```
307: и веднага след `:1918`: `attribCtrl.addAttribution(QUARTERS_ATTRIB);`
308: Низът е **дословно** полето `attribution` на `C:/git/Fire_Varna/scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json:854` (Ч) — нула апострофи, нула HTML.
309: 
310: **И12 · Два маркера за Node-среза** (нула преместен код): преди `:6256` → `// ---- Б3 slice start (pure, DOM-free: constants → validators → cache → index → search) ----`; след `:7154` → `// ---- Б3 slice end (everything below touches the DOM) ----`. Границата е измерена: първото докосване на DOM е `function span(` на `:7155`.
311: 
312: **И13 · Паритетната повърхност `:7470-7480` не расте.** `locationKey` (D12) е отложен — **О15**, не „решение 2“.
313: 
314: ### 3.3 Пиновете и правилата в двата bundle теста
315: 
316: `tests/test_places_public_bundle.py`: `:55-57` sha/bytes/gzip9 → `3dffc264…` / 128401 / 14748; `:80` копието на `QUARTER_CODES` (28) + `QUARTER_SRC` (5 стойности) + **нов `LOCALITY_SRC` (4)**; `:88` `QUARTER_BY_SRC = {"REG": 39, "KAIS": 10, "SIGNED_POLYGON": 42}`; `:89` `LOCALITY_COUNT = 5`.
317: `tests/test_hotels_public_bundle.py`: `:61-63` `eb8fa85c…`/151263/13642; `:83-85` `9064705a…`/77998/9690; `:88` `LOCATION_COUNTS = {"quarter": 28, "district": 5, "locality": 5}`; `:89` `LEGACY_ROWS = 18`; `:115` копието на кодовете; `:124` `QUARTER_BY_SRC = {"REG": 115, "KAIS": 25, "SIGNED_OVERRIDE": 12, "SIGNED_POLYGON": 15}`; `:125` `LOCALITY_COUNT = 7`.
318: 
319: **Три нови правила в двата теста (О18, О19):**
320: 1. `:291-293` (и близнакът `:290` в хотелите): `("locality", LOCALITY_SRC, LOCALITY_CODES)`; за `quarter` — ако `src == "DISTRICT_FALLBACK"`, кодът се търси в `DISTRICT_CODES` и трябва да е кодът на СОБСТВЕНИЯ район на реда.
321: 2. `:309` (и близнакът): `want` за fallback ред е `quarter["name"]` **или** `"район " + district["name"]` — двете форми, по О20.
322: 3. Нов гейт (един източник на истина): `set(QUARTER_CODES) == set(place_categories["locations"]["quarter"])`.
323: Лицензните низове се сравняват дословно (`:263`, `:384`, `:397-412`) — ако износът е пипнал низ, константата **и** README влизат в същия комит.
324: 
325: ### 3.4 Двигателят на референцията — шест места, не две (О19)
326: 
327: `scratch/places_search/recall_sweep.py`, един помощник `own_quarter(rec)` и неговите шест ползвания (Ч, всички прочетени):
328: - `:621` `self.qtk = self._loc_tokens(u"quarter", …)` → `own_quarter(self)`
329: - `:623` `self.qph = self._loc_phrases(u"quarter", …)` → `own_quarter(self)`
330: - `:1123` `d_rows = [r for r in cls if r.quarter is None …]` → `own_quarter(r) is None`
331: - `:1167` `district_hit = [… if r.quarter is None …]` → `own_quarter(r) is None`
332: - `:2146` `want = (r.quarter or {}).get("name") or (u"район " + …)` → **двете форми за fallback ред** (О20)
333: - `:2150` `if r.quarter and r.quarter.get("code") not in LOCATIONS[u"quarter"]` → за fallback ред се сверява срещу `DISTRICT_CODES` и срещу собствения район
334: 
335: **Приемане:** кандидатският дъмп преди/след промяната е **байт-еднакъв** над днешната доставка (G7).
336: **Забранено:** `INPUT_RELS` (`:2815-2816`) НЕ се пипа (О23).
337: **Обявено:** всеки НЕ-freeze прогон презаписва проследения `scratch/places_search/probe_out/token_parity.json` (`:4249-4253`) — това не е мръсно дърво по случайност, а очакван изход (О26).
338: 
339: ### 3.5 Фикстурите — единадесет, всяка с падащ `_broken`
340: 
341: `tests/test_granitsi_fixtures.py` (пренаписан) + `scratch/places_search/granitsi_fixtures_07.09.json` (`git mv` от `…_06.09.json`) + **нов** `tests/granitsi_client_probe.mjs`.
342: 
343: Промени в харнеса: докстрингът `:8-13` се пренаписва (след F13 това СА подписани очаквания); `_meta.status` → `"signed_by_petar"` + дата; `_meta.inputs` (трите нови sha) и `_meta.engine.sha256` — в същия комит (иначе `:188` пада пръв); `EXPECTED_NAMES` (`:48-49`) става единадесеторка; `test_the_two_deferred_fixtures_are_named_with_their_reason` (`:180-186`) → „нула отложени“; `assert_case` (`:197-204`) остава за Python-фикстурите, `branch` е **незадължителен** за Node-фикстурите; ключът за мутациите остава по име (`:67-84`), а за хотелите — защита срещу дубликата „РОЯЛ“ · „Хотел“ (225 реда, 224 уникални двойки): фикстура, която го докосва, ключова по **ординал**, иначе `LookupError`.
344: 
345: | # | фикстура | твърди (числата се ПРЕИЗМЕРВАТ) | `_broken`, който ТРЯБВА да падне |
346: |---|---|---|---|
347: | 1 | `street_collision` | `A3-street`, 1, ДГ№12 „Ян Бибиян“ | заварената + нова: улицата получава код `dolna_traka` |
348: | 2 | `district_retention` | `A3-district`, 12, 9 с квартал, новите `zone` | заварената (`DISTRICT_FALLBACK` + `district: null` → 11) |
349: | 3 | `mladost_kind_collision` | `M7-bare-location`, 20, 8/12 | заварената + `SIGNED_POLYGON` с код извън 28-те |
350: | 4 | `order_identity` | същите 20, **подредени** | заварената |
351: | 5 | `parent_child` (Младост) | `A3-location`, 6, 3 с квартал | код `mladost2_new` без подредената тройка |
352: | 6 | `parent_child_vazrazhdane` **(нова, ЗАМРАЗЯВА измереното, О16)** | (а) „възраждане“ → 5 (родител + `vazrazhdane1`/`vazrazhdane2`); (б) **„възраждане 2“ → 0** и (в) **„ж.к. възраждане 2“ → 0** — детската заявка НЕ намира детето | кодът на ДГ№34 „Лястовичка“ → `vazrazhdane1_new` → родителят връща 4 |
353: | 7 | `chaika_sibling_merge` **(нова, О16)** | „чайка“ → 30 реда през `chaika_kk` И `chaika_kv` — фразата слива братя без подписано родство | смени името на `chaika_kv` на нещо без думата „Чайка“ → сливането изчезва |
354: | 8 | `asparuhovo_no_child_rows` **(нова, О16)** | „аспарухово“ → 16 реда, **без** ЦДГ 43 „Пинокио“ (`druzhba`); „дружба“ → 2 | дай на `druzhba` alias „Аспарухово“ → 17 |
355: | 9 | `client_cache_matrix.foreign_code_while_other_bundle_valid` **(нова, Node)** | §3.6 | (а) `QUARTER_SRC` без `SIGNED_POLYGON` **в текста на среза** → `places2 = []` и `RECS.length === 225`; (б) `PLACES_CACHE` остава v6 → кеш-стъбът намира стария запис |
356: | 10 | `district_fallback_typed` **(нова, синтетична, положителна, О19)** | синтетичен ред с `quarter {name: <район>, code: <district code>, src: DISTRICT_FALLBACK}`: (а) минава `validTypedLocation`; (б) **остава в отговора на ГОЛАТА заявка „училище младост“** (клонът `:7118`) и на „младост“ (`:7064`); (в) не носи квартални думи; (г) картончето не печата квартал; (д) минава `qa` на `recall_sweep` (`:2146`, `:2150`); (е) минава двата bundle теста | **разделен `_broken`:** махни `ownQuarter` от `:7118` → „училище младост“ 6 → 5 (измерено); отделно `district: null` за изричното „училище район младост“ (клонът `:7104-7109`, който НЕ гледа `quarter`) |
357: | 11 | `client_reference_parity` **(нова, Node, §9 т. 13)** | шест заявки през среза на `index.html` (с `map` стъб) и през `recall_sweep.search()` → **едни и същи имена в един и същи ред** | махни `map` стъба → подредбата се срутва (измерено) |
358: 
359: ### 3.6 Node-фикстурите — как се викат и какво доказват (пренаписано след блокер 1)
360: 
361: Механиката: Python чете `index.html`, изрязва **по маркерите И12** (липсващ маркер = `AssertionError`, по образеца `tests/test_places_search_gate.py:503-530`); `shutil.which("node")`, **липсващ Node = `self.fail("node липсва — фикстурата е гейт")`**; `subprocess.run([node, "tests/granitsi_client_probe.mjs"], input=json.dumps({...}))` — срезът, товарите и случаите по stdin, отговорът по stdout; нула временни файлове, нула кирилица в командния ред.
362: 
363: `granitsi_client_probe.mjs` вдига среза с
364: `new Function('window','caches','document','map','fetch', slice + '; return {…}')` и подава стъбове: `window` (само `window.crypto`, за on/off), `caches` (кеш-матрицата), **`map`** и **`fetch`**.
365: 🔴 **`map` е задължителен:** `centre()` (`:6952-6955`) вика `map.getCenter()` в `try/catch`; без стъб `distOf` връща 0 и подредбата се срутва до реда на доставката. Стъбът е `{ getCenter: () => ({ lat: 43.2141, lng: 27.9147 }) }` — центърът, който референцията пинва (`recall_sweep.py:102-104`).
366: 🔴 **`fetch` е задължителен:** `fetchValidatedJson` (`:6613-6625`) вика глобалния `fetch`; Node 22 има свой и без стъб тестът излиза в мрежата.
367: 
368: **Приемането минава през пътя, който наистина отказва (не през гол `buildIndex`).** Причината е измерена и прочетена: `buildIndex` (`index.html:6648`) приема **вече разпарсени масиви и не вика нито един валидатор** — затова `RECS.length === 375` е свойство на файла, не на списъците, и е зелено дори при неразширен `QUARTER_SRC`. Фикстура 9 твърди:
369: 1. `validateHotels(hotels_ok, text) === true` **и** `validatePlaces2(places_new, text) === false` **преди** И4+И5, `=== true` **след** тях — булевите валидатори се произнасят поотделно;
370: 2. `accept(text, sha, validatePlaces2) === null` при чужд код, при crypto **ON** и **OFF** — отказът не зависи от `crypto.subtle`;
371: 3. `PLACES_CACHE === 'fire-varna-hotels-v7-225'` и `!== 'fire-varna-hotels-v6-225'`; кеш-стъб с v6 тяло **не** се намира;
372: 4. **`await ensurePlaces()`** със стъбнати `fetch`/`caches` → `RECS.length === 375` при валидната доставка и **`=== 225` при среза с оригиналния `QUARTER_SRC`** (`places2 = []`, `:6638`). Това е половината, която пада.
373: 5. Наблюдаемият отказ се **назовава**: при чужд код `places2 = []`, `hotels.length > 0`, `ensurePlaces` **не** хвърля (`:6639` иска и двата празни). UI-отказ не се въвежда в Б3 (§9 т. 10).
374: Отрицателната половина се прави **върху текста на среза** (замяна на реда `:6313` с днешната тройка), не върху константа, подадена в паметта.
375: 
376: ### 3.7 Родство — какво работи, какво не, поименно (О16)
377: 
378: (М) Фразовата карта на класа `quarter` над новия речник: `chaika → [chaika_kk, chaika_kv]`, `mladost → [mladost, mladost2]`, `vazrazhdane → [vazrazhdane, vazrazhdane1, vazrazhdane2]`, `borovets → [borovets_yug]`.
379: Подписаният DAG (11 двойки) срещу измереното:
380: 
381: | двойка | състояние |
382: |---|---|
383: | `mladost2 ⊂ mladost`, `vazrazhdane1 ⊂ vazrazhdane`, `vazrazhdane2 ⊂ vazrazhdane` | **работи по фраза** (случайно съвпадение, не договор) |
384: | `druzhba ⊂ asparuhovo` | **НЕ работи**, макар и двата да носят редове — единственият случай, който Петър може да види днес |
385: | `kaisieva ⊂ vladislavovo`, `vazrazhdane3 ⊂ vazrazhdane` | детето няма доставени редове |
386: | `abatko`, `rozova_dolina`, `kokardzha_generic`, `mladost1`, `saltanat` | нула редове |
387: | **`chaika_kk` + `chaika_kv`** | **сливат се без подписано родство** — фразовият механизъм не е DAG; същото ще стане с `borovets_sever`, ако получи ред |
388: 
389: **Б3 НЕ изнася DAG-а** (иска нов износ на varna_3d → нов блоб → нов комит на Петър там). Б3 **замразява** измереното с фикстури 5–8. Ако Петър иска само подписани връзки, единственият честен носител е `place_categories.json.locations.quarter[<code>].parents: [<code>]` (нула геометрия) — лот **Б5 „Родство“**.
390: 
391: ### 3.8 Опашката и allow-ът (О22, О25)
392: 
393: - `git rm scratch/places_search/ЗА_ПОДПИС_A.md` (или `git mv` към име извън глоба) — **в същия комит** с новата `scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md`.
394: - Новият `gates/allow/2026-09-07_b3.json` бюджетира **измерените 138 преместени реда** (1.8.1), генериран машинно от `gates/out/coverage.json`; старият `gates/allow/2026-09-05_lot1v_v.json` се маха в същия комит (в папката остава точно един json).
395: - `gates/baseline/MANIFEST.json` **не се пипа** в този лот.
396: 
397: ---
398: 
399: ## 4 · Ред на изпълнение
400: 
401: **[И]** изпълнител (`git -c user.name="Claude Executor" -c user.email=executor@local …`, О24) · **[П]** Петър. Между стъпка 7 и стъпка 13 пакетът е **ЧЕРВЕН по конструкция** (D19): изпълнителят записва ТОЧНИЯ набор падащи тестове и проверки (G20); всеки тест извън набора = STOP.
402: 
403: **0. [И] Санитарна проверка.** `git status --porcelain` (нула редове без `??`), `git log -1 --pretty='%h %an %s'`, `git rev-list --count origin/main..main`, `git ls-tree -r --name-only HEAD -- scratch/places_search | grep -c "ЗА_ПОДПИС"` → **1**.
404: 
405: **1. [И] Записва плана.** `docs/plans/ПЛАН_Б3_07.09.md` → комит `docs(plan): Б3 quarter search delivery plan v2 (signed 07.09)`.
406: 
407: **2. [И] Препис на трите блоба + ПЪЛНАТА мярка ПРЕДИ редакцията.**
408: ```bash
409: export PYTHONIOENCODING=utf-8
410: python - <<'PY'
411: import hashlib, gzip, pathlib
412: for p in ['data/places.json','data/hotels.json','data/place_categories.json']:
413:     b = pathlib.Path(p).read_bytes().replace(b'\r\n', b'\n')
414:     print(p, len(b), hashlib.sha256(b).hexdigest(), len(gzip.compress(b, 9)))
415: PY
416: ```
417: Очаквано: точно шестте числа и трите sha от §1.4. В същия прогон се мерят `QUARTER_BY_SRC`, `LOCATION_COUNTS`, `LEGACY_ROWS`, `LOCALITY_COUNT`, множеството квартални кодове, лицензните низове, формата на всеки `quarter_attribution.url` и **броят ключове на `_meta`** (10/8).
418: **Плюс двете нови мерки, преди един ред промяна:**
419: ```
420: python -c "from gates import coverage; import json; print(json.dumps(coverage.run(places_base='git:f06ac06:data/places.json', places_candidate='data/places.json', hotels_base='git:f06ac06:data/hotels.json', hotels_candidate='data/hotels.json', allow_path=None, out_dir='gates/out'), ensure_ascii=False)[:400])"
421: ```
422: очаквано: **exit 2, 138 непокрити** (1.8.1). И деветте заявки от 1.8.4–1.8.9 през `recall_sweep`. **Всяко разминаване = STOP.**
423: Отрицателно доказателство: `python -m unittest tests.test_places_public_bundle tests.test_hotels_public_bundle` **сега е ЧЕРВЕН** — първият ред на G20-набора.
424: 
425: **3. [И] Маркерите И12 + Node-сондата.** Първо `index.html` получава двата маркера, после се създава `tests/granitsi_client_probe.mjs` — **преди** редакциите, за да има с какво да се снеме отрицателното доказателство (поправка на v1: сондата не може да се вика преди да съществува).
426: Мярка: срезът с ДНЕШНИТЕ списъци над НОВИТЕ байтове → `validatePlaces2 === false`, `await ensurePlaces()` → `RECS.length === 225`.
427: 
428: **4. [И] `index.html` — четиринадесетте редакции** (§3.2), без нито един ред извън списъка. **И11 се пропуска, ако низът още не е подписан (О21)** — тогава влиза в стъпка 12б.
429: Мярка след: `validatePlaces2 === true`, `RECS.length === 375`.
430: 
431: **5. [И] Двата bundle теста + трите нови правила** (§3.3). `python -m unittest tests.test_places_public_bundle tests.test_hotels_public_bundle` → **0**. Отрицателно: една сменена цифра в `PLACES_SHA256` → ≠ 0.
432: 
433: **6. [И] Двигателят + фикстурите** (§3.4–3.6), включително `git mv` на фикстурния файл. `python -m unittest tests.test_granitsi_fixtures -v` → **0**, единадесет фикстури, всяка с падащ `_broken`.
434: Двигателят отделно (G7): дъмпът `%TEMP%/fv_measures/lot1v_v_candidate_rows.json` от **отделно пълно дърво** (`git worktree add <scratchpad>/head_wt HEAD`) срещу дъмпа след промяната → **0 реда разлика**.
435: 
436: **7. [И] Стейджва точния write-set** (`git add` с изрични пътища, никога `-A`), после `git status --short` и `git diff --cached --stat`. **Обявено:** `scratch/places_search/probe_out/token_parity.json` ще е модифициран от прогоните (О26) — той НЕ влиза в този комит, а в комит 5.
437: Показва на Петър подготвеното съобщение `scratch/places_search/COMMIT_MSG_B3.txt`.
438: 
439: **8. [П] Атомният комит** — §6.
440: 
441: **9. [И] Отваря D19-интервала и го записва.** `python -m unittest discover -s tests`; `python -m gates.run_gates` → и двете ≠ 0. Записва **поименно** какво пада, включително очакваното **coverage изход 2** на проверка 4. Всеки тест/проверка ИЗВЪН набора = STOP.
442: Тук се мери `gates/out/coverage.json`: кои редове иска allow-файлът. Ред, който не се извежда механично → STOP.
443: 
444: **10. [И] Очаквания и манифести (report-only).** `python scratch/places_search/recall_sweep.py --manifest` → 0 (пише кандидата, трите манифеста и НЕПОДПИСАН `expectations.json`; **`_meta.inputs` остава тройка — О23**); `python -m gates.release` → **6 (BLOCKED)** с точния брой делти по кофи, който се записва.
445: 
446: **11. [И] Опашката.** `scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md`: три класа редове (въпрос / артефакт / делта), решения `pending`, без code fence и без HTML коментари. **Задължителни редове:** всяка делта на `gates.release`; шестте `SIGNABLE` + новият allow; **ред „въпрос“ с `тяло: <sha256>` за низа на атрибуцията (О21)**; ред за Перчемлията (О6); редовете по О15/О16/О20 („детската заявка не намира детето — прието“, „чайка се слива без подписано родство — прието“, „fallback етикетът се приема в двете форми“).
447: В същия комит: `git rm` на `ЗА_ПОДПИС_A.md` (О25), новият allow (138 реда), махнатият стар allow.
448: Комит **[И]**: `docs: queue and manifests for the Б3 delivery signatures (07.09)`.
449: Мярка веднага след комита: `git ls-tree -r --name-only HEAD -- scratch/places_search | grep -c "ЗА_ПОДПИС"` → **1**.
450: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git ls-files -- scratch/places_search/recall_sweep.py scratch/places_search/js_token_probe.js tests/test_places_public_bundle.py tests/test_hotels_public_bundle.py tests/test_granitsi_fixtures.py scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json' in C:\git\Fire_Varna
 succeeded in 2ms:
codex
Потвърдих HEAD `f00dd78` и 81 локални комита напред. Има непроcледени брифове и самия план, но няма промени по проследените файлове. Вече се очертава разминаване в Node-проверката: връщането на стария списък с извори засяга и двата пакета, а планът очаква хотелите да останат приети.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8 | Select-Object -Skip 450 -First 150 | ForEach-Object -Begin { "'$n=450 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
451: **12. [П] Подписите.** `python -m gates.sign <id> да --all да --queue scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md` + **неговият** комит, който писалката отпечатва.
452: **12б. [И]** Ако низът е подписан на този етап — И11 влиза сега, в комит с `index.html` само за този ред: `feat(map): signed quarter-boundary line in the map attribution (decision 8)`. **[П]** го комитва (текст, който отива на живата карта).
453: 
454: **13. [И] Едно-единствено замразяване.** `python scratch/places_search/recall_sweep.py --freeze` → 0; пише `recall_sweep_rows.json`, `expectations.json`, `probe_out/token_parity.json`.
455: 
456: **14. [П] Комит на замразените тела:** `freeze: reference + expectations + parity (Б3)`.
457: 
458: **15. [И] Пълният гейт** — §5. Всичко зелено → одитор (друг агент, read-only).
459: 
460: **16. [П] Локален преглед** — §8.
461: 
462: **17. [П] Пушът,** от интерактивен терминал: `git rebase --autostash origin/main`, после `git push origin main`.
463: 
464: **18. [И] След пуша:** `docs/activeContext.md` + `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` §8; проверка, че публикуваните sha са равни на локалните; комит `docs: activeContext — Б3 delivery published, published hashes verified equal to local`; **[П]** втори пуш.
465: 
466: ---
467: 
468: ## 5 · Гейтове (всеки — команда с изход ≠ 0 и с доказано падаща отрицателна половина)
469: 
470: | # | гейт | команда | очакван изход | отрицателното доказателство (ТРЯБВА да падне) |
471: |---|---|---|---|---|
472: | G1 | пиновете срещу LF-блобовете | `python -m unittest tests.test_places_public_bundle tests.test_hotels_public_bundle` | 0 | една сменена цифра в `PLACES_SHA256` → ≠ 0 |
473: | G2 | единадесетте фикстури | `python -m unittest tests.test_granitsi_fixtures -v` | 0 | всеки `_broken` → `AssertionError` (тестът го иска) |
474: | G3 | Node-половината **през `ensurePlaces`** | същият прогон, фикстура 9 | 0 | срез с оригиналния `QUARTER_SRC` (`:6313`) → `places2 = []`, `RECS.length === 225`; кеш v6 → стар запис се намира |
475: | G3б | паритет клиент ↔ референция | същият прогон, фикстура 11 | 0 | махнат `map` стъб → друг ред |
476: | G4 | пълният набор | `python -m unittest discover -s tests` | 0 | преди подписите: ≠ 0 — записаният G20 набор |
477: | G5 | седемте проверки | `python -m gates.run_gates` | **0** (7/7 ✓) | жълто („pending — Петър“) също дава 1 |
478: | G6 | нула **неподписани** изгубени резултати | `python -m gates.release` | 0 (преди подписите: 6) | делта без покриващ ред „да“ → 6 |
479: | G7 | двигателят не мести кандидата (О26) | `git worktree add <scratchpad>/head_wt HEAD`; прогон оттам и оттук; `python -c "diff на %TEMP%/fv_measures/lot1v_v_candidate_rows.json"` | 0 реда | нарочна промяна в правило → диф ≠ 0 |
480: | G8 | картончето няма ред за атрибуция | тест: срезът `function popupFor` … `return wrap;` не съдържа `quarter_attribution`, `Wikimapia`, `QUARTERS_ATTRIB` | 0 | добави ред с `QUARTERS_ATTRIB` в `popupFor` → ≠ 0 |
481: | G9 | низът в подножието, дословно и **само след подпис** | тест: (а) низът от `granitsi_decisions_4_2026-09-07_proba.json["attribution"]` се среща **в `index.html` точно веднъж** (обхватът е дословно този файл — низът стои и в проследения план); (б) подаден е на `attribCtrl.addAttribution`; (в) `тяло: <sha256>` на блоба стои на подписан ред от опашката | 0 | една сменена буква → ≠ 0; неподписан блоб → ≠ 0 |
482: | G10 | размер ≤ 5 MB, върху **проследените** файлове | `python -c "import subprocess,pathlib,sys; f=subprocess.run(['git','ls-files','index.html','data/*.json'],capture_output=True,text=True).stdout.split(); t=sum(pathlib.Path(x).stat().st_size for x in f); print(t); sys.exit(0 if t < 5*1024*1024 else 1)"` | 0 (число ≈ 2,24 MB) | праг 1 MB в същата команда → изход 1 |
483: | G11 | нула геометрия (О13) | python-обвивка: (а) `coordinates` в трите доставени файла → 0 попадения, иначе **изход 1**; (б) нула НОВИ попадения спрямо **`git show f00dd78:<път>`** (не „HEAD“) в останалите проследени `data/*.json` | 0 | вкарай `"coordinates"` в `data/places.json` → 1 |
484: | G12 | нула кадастрален идентификатор | `python -m gates.run_gates` проверка 3 | зелена | вкарай `10135.1.2` → червено |
485: | G13 | точно един allow-json | `python -c "import pathlib,sys; n=len(list(pathlib.Path('gates/allow').glob('*.json'))); print(n); sys.exit(0 if n==1 else 1)"` | 0 | два файла → 1 (и `run_gates` проверка 4 червена) |
486: | G14 | куката е на място | `diff scripts/hooks/pre-push .git/hooks/pre-push` | 0 | подменена кука → diff ≠ 0 (проба в скрачпад-копие) |
487: | **G15** | **точно една опашка в HEAD (О25)** | `python -c "import subprocess,sys; out=subprocess.run(['git','ls-tree','-r','--name-only','-z','HEAD','--','scratch/places_search'],capture_output=True).stdout.decode('utf-8'); n=sum(1 for x in out.split('\0') if 'ЗА_ПОДПИС' in x); print(n); sys.exit(0 if n==1 else 1)"` | 0 | върни втората опашка → `python -m gates.release` дава 6 с думите „повече от една опашка в HEAD“ |
488: | **G16** | **местността не е отворена (О18)** | тест в bundle-ите: `DISTRICT_FALLBACK not in LOCALITY_SRC` и всеки доставен `locality.src ∈ LOCALITY_SRC` | 0 | сложи `locality.src = "DISTRICT_FALLBACK"` в мутиран кандидат → ≠ 0 |
489: | **G17** | **`_meta` е затворен и url-ите са по формата (О17)** | фикстура: `_meta` с 9 или 11 ключа → `validatePlaces2 false`; запис с `url: "http://example.com/1/"` при `src: "wikimapia"` → false; `SIGNED_POLYGON` код без запис → false | 0 | всяка от трите мутации, която НЕ падне → тестът е червен |
490: 
491: ---
492: 
493: ## 6 · Комити (кой какво комитва)
494: 
495: Причината за атомността е механична: `index.html` пинва sha на данните — при какъвто и да е разрез съществува HEAD, в който пиновете и блобовете не си съответстват и търсенето на места умира.
496: 
497: | # | автор (наложен) | съдържание | съобщение (дословно) |
498: |---|---|---|---|
499: | 1 | `Claude Executor <executor@local>` (флагове, О24) | `docs/plans/ПЛАН_Б3_07.09.md` | `docs(plan): Б3 quarter search delivery plan v2 (signed 07.09)` |
500: | 2 | **`Petar1984`** (неговата ръка) | `data/places.json`, `data/hotels.json`, `data/place_categories.json`, `index.html`, `tests/test_places_public_bundle.py`, `tests/test_hotels_public_bundle.py`, `tests/test_granitsi_fixtures.py`, `tests/granitsi_client_probe.mjs`, `scratch/places_search/granitsi_fixtures_07.09.json` (+ изтритият `…_06.09.json`), `scratch/places_search/recall_sweep.py` | виж по-долу |
501: | 3 | `Claude Executor` | опашката Б3, **изтритата `ЗА_ПОДПИС_A.md`**, трите манифеста, новият `gates/allow/2026-09-07_b3.json` (138 реда, pending), махнатият стар allow. **`gates/baseline/MANIFEST.json` НЕ се пипа (О22).** | `docs: queue and manifests for the Б3 delivery signatures (07.09)` |
502: | 4 | **`Petar1984`** | каквото `gates.sign` е записало | съобщението, което писалката **отпечатва** |
503: | 4б | **`Petar1984`** (само ако низът се подписва отделно) | `index.html` (И11) | `feat(map): signed quarter-boundary line in the map attribution (decision 8)` |
504: | 5 | **`Petar1984`** | `recall_sweep_rows.json`, `expectations.json`, `probe_out/token_parity.json` | `freeze: reference + expectations + parity (Б3)` |
505: | 6 | `Claude Executor` (след пуша) | `docs/activeContext.md`, `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` | `docs: activeContext — Б3 delivery published, published hashes verified equal to local` |
506: 
507: Съобщението на комит 2, дословно (`scratch/places_search/COMMIT_MSG_B3.txt`):
508: 
509: ```
510: feat(search): quarter search over signed boundaries, QUARTER_CODES +8, cache v7 (D13 atomic delivery)
511: 
512: data: places delivery with quarter_attribution (D13 ordered) — the three blobs of
513: varna_3d 05f485e (places 3dffc264, hotels eb8fa85c, categories 9064705a), with the
514: closed lists, the three pins, LEGACY_BUNDLE_SHA and PLACES_CACHE v7 in this very
515: commit, because a HEAD whose pins and blobs disagree kills the place search.
516: tests: S17 fixtures fail on broken candidates
517: ```
518: 
519: Командите за комит 2 (PowerShell, по една на ред, без `&&`):
520: ```powershell
521: cd C:\git\Fire_Varna
522: git status --short
523: git diff --cached --stat
524: git commit -F scratch\places_search\COMMIT_MSG_B3.txt
525: git log -1 --pretty='%h %an <%ae> · %cn <%ce> · %s'
526: ```
527: **Следпроверка (О24):** последният ред трябва да върне `Petar1984 <petar.dikov2019@gmail.com>` и като автор, и като комитър. Предварителното `git config user.name` **не доказва нищо** — то връща `Petar1984` и когато го пуска агент (`gates/sign.py:139-147` отказва само при изброени агентски идентичности).
528: **Ако Петър предпочете три комита** (по буквата на `:144`): редът е `data+index.html` → `tests` → `docs`, но D13 се нарушава. Планерът не го препоръчва.
529: 
530: ---
531: 
532: ## 7 · STOP условия
533: 
534: 1. **Всяко число от §1, премерено различно** — трите sha, шестте байта/gzip, осемте липсващи кода, 57-те реда, 201-те написани, числата на фикстурите, **и новите: 138 непокрити реда (1.8.1), 1 опашка в HEAD, деветте заявки 1.8.4–1.8.9**.
535: 2. `gates.release` дава делта, която опашката не покрива, или ред „не“ (терминален).
536: 3. `gates/out/coverage.json` иска allow-ред, който не се извежда механично.
537: 4. Паднал тест **извън** записания D19/G20 набор (включително: проверка 4 с изход, различен от очаквания 2).
538: 5. `python -m gates.run_gates` жълто, третирано като зелено.
539: 6. Дифът на кандидата преди/след промяната в `recall_sweep.py` е ≠ 0 реда.
540: 7. Липсващ `node`, липсващ маркер за среза, или Node-фикстура, минала **без** `map`/`fetch` стъб.
541: 8. Опит за комит на данни от агент · `push` от агент · `--no-verify` · пипане на `.git/hooks`.
542: 9. Работното дърво не е чисто по проследен файл при старта, или чужд стейджнат диф.
543: 10. Решение 10 / резервът за Перчемлията (О6) не е подписан и одиторът настоява.
544: 11. Износът е сменил лицензен низ, а константата в теста и README не са в същия комит.
545: 12. Петър не е видял картата локално преди пуша.
546: 13. **Повече от една опашка в HEAD** или повече от един allow-json (О25).
547: 14. **`_meta.inputs` не съдържа обявеното множество** (трите блоба — О23), или `INPUT_RELS` е пипнат.
548: 15. **Комит с автор `Petar1984`, направен не от неговата ръка** (О24).
549: 16. **Низът за атрибуция е влязъл в `index.html` преди подписания ред с неговия `тяло: <sha256>`** (О21).
550: 17. **`gates/baseline/MANIFEST.json` е пипнат в този лот** (О22).
551: 18. Проследеният `probe_out/token_parity.json` се появи в комит 2 вместо в комит 5 (О26).
552: 
553: ---
554: 
555: ## 8 · Локален преглед (как Петър гледа)
556: 
557: ```powershell
558: cd C:\git\Fire_Varna
559: python -m http.server 8000
560: ```
561: `http://localhost:8000/index.html`, отворена конзола, ширина 375 px, Hard reload (кешът вече е v7). Първо: конзолата е чиста и **няма** реда `legacy_by_row: друг пакет…`.
562: 
563: | # | пишеш | очакваш (числата се преизмерват преди прегледа) |
564: |---|---|---|
565: | 1 | `Кайсиева градина` | в нашата секция — **няма** квартални редове (3 реда `M2-failopen`); в адресната търсачка отгоре — 9 реда. Измерено ограничение, решение 1. |
566: | 2 | `училище Възраждане 3` | **2 реда по ИМЕТО**: `3 ОУ Ангел Кънчев` [**кв. Левски**] и `III ПМГ` [**кв. Тракия**] — **нито един от двата не е във Възраждане 3**. Това е шум по името, не отговор по квартал; „3“ се хваща като част от името. |
567: | 3 | `възраждане`, после `възраждане 2` | **5** реда (родител + `vazrazhdane1`/`vazrazhdane2`) и **0 реда** за детето. **Половината „дете → детето“ НЕ работи** (О16) — това подписваш. |
568: | 4 | `левски`, после `кв. Левски` | голото `левски` → **14 реда, 12 с код `kv_levski`** (`I ЕГ`, `Технически университет – Варна`, `ДГ№10 „Карамфилче“`, хотел `Сорбона`). `кв. Левски` → **4 ЧУЖДИ реда** (НУ Васил Левски [Аспарухово], ПГ „Васил Левски“ [район Младост], ДГ№40 [Владиславово], болница Лисичкова). **Типовият префикс не се нормализира — D12 е отложен (О15).** Същото за `кв. Тракия` (1 чужд ред), `кв. Христо Ботев` (24), `ж.к. Св. Иван Рилски` (22). |
569: | 5 | `бриз` | `IV ЕГ Жолио Кюри` и `ПГ „Д. И. Менделеев“` — двата нови `SIGNED_POLYGON` реда. |
570: | 6 | `чайка` | **30 реда, смесени между к.к. Чайка и кв. Чайка** — фразата слива двата кода без подписано родство (О16). |
571: | 7 | `аспарухово`, после `дружба` | 16 реда **без** ЦДГ 43 „Пинокио“, и 2 реда. Подписаното родство `druzhba ⊂ asparuhovo` **не действа в търсенето**. |
572: | 8 | `Никея` (хотел в Чайка) → картончето | ред **„вид · к.к. Чайка · район Приморски“**; **НЯМА ред за извор**; долу вляво, до `© OpenStreetMap`, стои низът за границите. |
573: | 9 | `училище район Младост` / `младост` | **12** / **20**. Изричното районно търсене задържа и петте училища със собствен квартал. |
574: | 10 | **надписът при 375 px** | низът е 338 знака и застава в **същия долен ляв ъгъл**, където са бутоните `+`/`−` (`index.html:1900` и `:1917`). Проверява се **на екрана**: бутоните `+`/`−` и локацията остават **видими и натискаеми** при трите базови карти. Ако не са — §9 т. 7, вариант „къс низ“. |
575: 
576: ---
577: 
578: ## 9 · Решения за Петър
579: 
580: 1. 🔴 **„Кайсиева градина“ и „училище Възраждане 3“ днес са неизпълними**, а „кв. Левски“ / „кв. Тракия“ / „кв. Христо Ботев“ / „ж.к. Св. Иван Рилски“ **връщат чужди редове**, защото типовият префикс не е значещ токен (`index.html:6495-6496`). Препоръка: **(а)** Б3 тръгва както е, с О15 подписан изрично; D12 (нормализаторът + `locationKey` в паритета) е лот **Б5**; трите ледждерни реда (`ДГ 39 „Приказка“`, `ОУ Стоян Михайловски` → `kaisieva`; `ДГ 29 „Звънче“` → `vazrazhdane3`) отиват в борда на същия лот. **Този подпис е ЗАДЪЛЖИТЕЛЕН преди старта, не препоръка.**
581: 2. 🔴 **Правилото родител/дете.** Измерено: работи по фраза само за Младост/Възраждане, **не работи** за `druzhba ⊂ asparuhovo`, **не работи** за детската заявка, и **слива** `chaika_kk`+`chaika_kv` без подписано родство. Препоръка: **замразяваме измереното** (фикстури 5–8) и подписваш О16. Вариант Б: `locations.quarter[<code>].parents` в речника — тогава днешната доставка отпада и цикълът се повтаря отначало.
582: 3. **`QUARTER_CODES` +8 (=28)** + машинен гейт „списъкът == речника“. Препоръка: **да**.
583: 4. **Един атомен комит с твой автор** (О4) + наложено авторство на агентските комити (О24). Препоръка: **да**.
584: 5. **`DISTRICT_FALLBACK`: пълното типово правило на ШЕСТ места** (двата двигателя + двата bundle теста, О19) + синтетична положителна фикстура с разделен `_broken`. Препоръка: **пълното правило**.
585: 6. **Етикетът на fallback ред се приема в ДВЕТЕ форми** (О20); затягането до „район X“ влиза заедно с износния гейт във varna_3d. Препоръка: **да** (иначе първата истинска fallback доставка умира мълчаливо).
586: 7. 🔴 **Низът в подножието не е твой подпис днес** (О21): последният комит по файла с решенията е на агент и файлът не е в `SIGNABLE`. Препоръка: подписваш го като **ред „въпрос“ с `тяло: <sha256>`** преди комита на доставката. Две бележки: низът казва „в този файл“ (писан е за файла с решенията), а на 375 px заема долния ляв ъгъл при бутоните за мащаб — §8 проба 10 решава дали остава дословен или искаш къс вариант.
587: 8. **`granitsi_fixtures_06.09.json` → `…_07.09.json`** (`git mv`). Препоръка: **да**.
588: 9. 🔴 **baseline и allow (О22).** Препоръка: **baseline ОСТАВА `f06ac06` в този лот**; новият allow бюджетира **138-те измерени преместени реда** (не 30-те „непокрити днес“); пренасочването на baseline към комита на доставката е **отделен по-късен подписан лот** заедно с нулиране на allow-редовете и прогон `run_gates` → 7/7. Причина: `base == candidate` дава `EXIT_ALLOW_STALE = 3` (`gates/coverage.py:617`), а празен allow прави гейта вакуумно зелен.
589: 10. **Наблюдаемият отказ при чужд код** остава само пинат (фикстура 9). Видим UI-отказ е отделен малък лот.
590: 11. **Перчемлията / решение 10** (О6) — подпиши поименния резерв **преди** комита или сложи изричен „отложено“ ред в опашката.
591: 12. **Документният дълг** (О9 + О23: `_meta.inputs` без паритета) — **отделен комит след пуша**.
592: 13. **Node-паритетната фикстура е ПОСТРОЕНА** (фикстура 11, §3.5) — вече не е обещание без write-set. Препоръка: **да**.
593: 14. 🔴 **Старата опашка `ЗА_ПОДПИС_A.md` (О25)** — маха се от HEAD в комит 3, иначе release е BLOCKED завинаги (`gates/release.py:465-472`). Твоят избор: **архивно име извън глоба** (`scratch/places_search/архив/A_05.09.md`) или само в git историята (тя носи 27 подписани реда).
594: 15. **`LOCALITY_SRC` (О18)** — стеснението, което пази местността от `DISTRICT_FALLBACK`. Препоръка: **да**.
595: 16. **`_meta` става затворен набор в клиента (О17)** — 10/8 ключа и url-формата по измерената форма. Препоръка: **да** (това е половината от G27(б), която иначе остава неналожена във Fire_Varna).
596: 
597: ---
598: 
599: ## 10 · Какво НЕ се пипа
600: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath index.html -Encoding UTF8 | Select-Object -Skip 6250 -First 110 | ForEach-Object -Begin { $n=6250 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 127ms:
6251:     const inputEl = document.getElementById('addrSearchInput');
6252:     const theirsEl = document.getElementById('addrSearchResults');
6253:     const box = document.getElementById('placesSearchResults');
6254:     if (!inputEl || !theirsEl || !box) return;   // header markup missing -> no-op
6255: 
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath index.html -Encoding UTF8 | Select-Object -Skip 6510 -First 150 | ForEach-Object -Begin { $n=6510 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 109ms:
6511:     // ЛОТ 1в-Б (ADR 008 D5, план §2г S5): `address` is `null` or EXACTLY the four
6512:     // keys, all four non-empty strings, the source from the closed list. The client
6513:     // never parses `text`: `street_phrase` and `house_key` leave the exporter WITH
6514:     // it, so a drift between them is a STOP over there, never a guess here.
6515:     const ADDR_KEYS = ['text', 'src', 'street_phrase', 'house_key'];
6516:     function validAddress(r) {
6517:       const a = r.address;
6518:       if (a === null) return true;
6519:       if (!a || typeof a !== 'object' || Array.isArray(a)) return false;
6520:       if (Object.keys(a).length !== ADDR_KEYS.length) return false;
6521:       for (const k of ADDR_KEYS) if (typeof a[k] !== 'string' || !a[k]) return false;
6522:       return !!ADDR_SRC_LINE[a.src];
6523:     }
6524:     // ЛОТ 1в-В (ADR 008 D9, план §3ж S1): `null` or EXACTLY the three keys, all
6525:     // three non-empty strings, the source and the code from THEIR closed lists.
6526:     // A location the lists do not know is a REFUSAL of the whole delivery, never
6527:     // a name printed on a card because it happened to be in the file.
6528:     function validLocation(value, srcs, codes) {
6529:       if (value === null) return true;
6530:       if (!value || typeof value !== 'object' || Array.isArray(value)) return false;
6531:       if (Object.keys(value).length !== LOC_KEYS.length) return false;
6532:       for (const k of LOC_KEYS) if (typeof value[k] !== 'string' || !value[k]) return false;
6533:       return srcs.indexOf(value.src) >= 0 && codes.indexOf(value.code) >= 0;
6534:     }
6535:     function validTypedLocation(r) {
6536:       if (!validLocation(r.quarter, QUARTER_SRC, QUARTER_CODES)) return false;
6537:       if (!validLocation(r.locality, QUARTER_SRC, LOCALITY_CODES)) return false;
6538:       // S4: the district is the one field that is never null — „район X“ is the
6539:       // honest answer when nothing else can be sourced, so a row without one is
6540:       // not publishable at all.
6541:       if (!r.district || !validLocation(r.district, DISTRICT_SRC, DISTRICT_CODES)) return false;
6542:       // S1: `zone` is the compat label and it FOLLOWS from the typed fields. A row
6543:       // whose label does not follow is a different delivery, not a row.
6544:       return r.zone === (r.quarter ? r.quarter.name : DISTRICT_MARK + ' ' + r.district.name);
6545:     }
6546:     function validateHotels(d, text) {
6547:       if (!d || !d._meta || !Array.isArray(d.hotels)) return false;
6548:       if (d.hotels.length !== EXPECT_COUNT || d._meta.count !== EXPECT_COUNT) return false;
6549:       if (typeof d._meta.licence !== 'string' || !d._meta.licence || CADASTRAL.test(text)) return false;
6550:       for (const h of d.hotels) {
6551:         if (Object.keys(h).length !== EXPECT_KEYS.length) return false;
6552:         for (const k of EXPECT_KEYS) if (!(k in h)) return false;
6553:         for (const k of ['old_names', 'old_names_src', 'cat', 'beds', 'uins']) if (!Array.isArray(h[k])) return false;
6554:         if (!validAliasSrc(h) || !validAddress(h) || !validTypedLocation(h)) return false;
6555:         if (typeof h.name !== 'string' || !h.name || typeof h.zone !== 'string' || !h.zone) return false;
6556:         if (typeof h.no_uin !== 'boolean') return false;
6557:         if (KINDS.indexOf(h.kind) < 0 || STATUSES.indexOf(h.status) < 0 || !SRC_LINE[h.src]) return false;
6558:         if (!isFinite(h.lat) || !isFinite(h.lon)) return false;
6559:         if (h.lat < LAT_MIN || h.lat > LAT_MAX || h.lon < LON_MIN || h.lon > LON_MAX) return false;
6560:       }
6561:       return true;
6562:     }
6563:     function validatePlaces2(d, text) {           // фаза 2 Д3: 8 keys, enums, box, count
6564:       if (!d || !d._meta || !Array.isArray(d.places)) return false;
6565:       if (d.places.length !== EXPECT2_COUNT || d._meta.count !== EXPECT2_COUNT) return false;
6566:       if (typeof d._meta.licence_osm !== 'string' || !d._meta.licence_osm) return false;
6567:       if (typeof d._meta.licence_registry !== 'string' || !d._meta.licence_registry) return false;
6568:       if (CADASTRAL.test(text)) return false;
6569:       for (const p of d.places) {
6570:         if (Object.keys(p).length !== EXPECT2_KEYS.length) return false;
6571:         for (const k of EXPECT2_KEYS) if (!(k in p)) return false;
6572:         if (!Array.isArray(p.old_names) || !Array.isArray(p.old_names_src)) return false;
6573:         if (!validAliasSrc(p) || !validAddress(p) || !validTypedLocation(p)) return false;
6574:         if (typeof p.name !== 'string' || !p.name || typeof p.zone !== 'string' || !p.zone) return false;
6575:         if (KINDS2.indexOf(p.kind) < 0 || STATUSES.indexOf(p.status) < 0 || !SRC_LINE[p.src]) return false;
6576:         if (!isFinite(p.lat) || !isFinite(p.lon)) return false;
6577:         if (p.lat < LAT_MIN || p.lat > LAT_MAX || p.lon < LON_MIN || p.lon > LON_MAX) return false;
6578:       }
6579:       return true;
6580:     }
6581:     const validateCats = (d) => !!(d && d._meta && d._meta.schema === 1 && d.forms &&
6582:                                    typeof d.forms === 'object' && Array.isArray(d.chips));
6583:     const raced = (p) => Promise.race([p, new Promise((res) => setTimeout(() => res(null), CACHE_TIMEOUT_MS))]);
6584:     async function cacheText(url) {              // В7: only OUR open namespace, never caches.match
6585:       if (typeof caches === 'undefined') return null;
6586:       try {
6587:         return await raced((async function () {
6588:           const hit = await (await caches.open(PLACES_CACHE)).match(url);
6589:           return hit ? await hit.text() : null;
6590:         })());
6591:       } catch (e) { return null; }
6592:     }
6593:     async function cachePut(url, text) {         // best-effort: the cache never blocks the parse
6594:       if (typeof caches === 'undefined') return;
6595:       try {
6596:         await raced((async function () {
6597:           const c = await caches.open(PLACES_CACHE);
6598:           await c.put(url, new Response(text, { headers: { 'Content-Type': 'application/json' } }));
6599:         })());
6600:       } catch (e) { /* ignored on purpose */ }
6601:     }
6602:     async function accept(text, sha, validate) {
6603:       if (typeof text !== 'string' || !text || text.length > MAX_BODY) return null;
6604:       try {
6605:         if (window.crypto && crypto.subtle) {    // В7: content check; structure is the fallback
6606:           const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
6607:           if (Array.from(new Uint8Array(digest)).map((b) => b.toString(16).padStart(2, '0')).join('') !== sha) return null;
6608:         }
6609:         const data = JSON.parse(text);
6610:         return validate(data, text) ? data : null;
6611:       } catch (e) { return null; }
6612:     }
6613:     async function fetchValidatedJson(url, sha, validate) {
6614:       const ac = ('AbortController' in window) ? new AbortController() : null;
6615:       const timer = setTimeout(function () { if (ac) ac.abort(); }, FETCH_TIMEOUT_MS);   // covers text() too
6616:       let text = null;
6617:       try {
6618:         const resp = await fetch(url, ac ? { cache: 'no-cache', signal: ac.signal } : { cache: 'no-cache' });
6619:         if (resp.ok) text = await resp.text();
6620:       } catch (e) { text = null; }
6621:       clearTimeout(timer);
6622:       const fresh = await accept(text, sha, validate);
6623:       if (fresh) { cachePut(url, text); return fresh; }
6624:       return await accept(await cacheText(url), sha, validate);   // В7: a bad cache is ignored, not deleted
6625:     }
6626:     function ensurePlaces() {
6627:       if (placesPromise) return placesPromise;
6628:       placesPromise = (async function () {
6629:         // С3: three files, allSettled - one refusal never takes the others down.
6630:         // Hotels without places, places without hotels; the dictionary is OPTIONAL
6631:         // (without it there are no keys and every token is a plain name - which is
6632:         // the 3D marker rule itself: "хотел адмирал" still finds АДМИРАЛ).
6633:         const got = (await Promise.allSettled([
6634:           fetchValidatedJson(PLACES_URL, HOTELS_SHA256, validateHotels),
6635:           fetchValidatedJson(PLACES2_URL, PLACES2_SHA256, validatePlaces2),
6636:           fetchValidatedJson(CATS_URL, CATS_SHA256, validateCats)
6637:         ])).map((r) => (r.status === 'fulfilled' ? r.value : null));
6638:         const hotels = got[0] ? got[0].hotels : [], places2 = got[1] ? got[1].places : [];
6639:         if (!hotels.length && !places2.length) throw new Error('places payload unavailable');
6640:         buildIndex(hotels, places2, got[2]);
6641:         return true;
6642:       })();
6643:       // Д2: fail closed to ABSENCE, not to a dead session — the next FOCUS tries again
6644:       // (a keystroke never does: the input path only reads an index that is already in).
6645:       placesPromise.catch(function (e) { placesPromise = null; warnOnce(e); });
6646:       return placesPromise;
6647:     }
6648:     function buildIndex(hotels, places2, cats) {
6649:       // ЛОТ 1в-В (план §3г, §3ж S3) — THREE dictionaries, one per class. The class
6650:       // travels with the word because „младост“ is a quarter AND a district: one
6651:       // flat token set could not tell them apart, and that is how СУ „Гео Милев“
6652:       // ended up inside a drawn industrial-zone hull. ONE rule, two
6653:       // implementations: this and scratch/places_search/recall_sweep.py.
6654:       // Fail-soft (С7′): a `locations` that is not an object switches the location
6655:       // words off and nothing else — the class keys, the names, the aliases and
6656:       // the addresses all still stand.
6657:       const locs = (cats && cats.locations && typeof cats.locations === 'object') ? cats.locations : {};
6658:       const generic = new Set();                 // (г) the dictionary's own word list
6659:       for (const word of ((cats && cats._meta && cats._meta.zone_generic_words) || []))
6660:         for (const t of placeTokens(word)) generic.add(t.s);

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8 | Select-Object -Skip 578 -First 150 | ForEach-Object -Begin { "'$n=578 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 53ms:
579: 
580: 1. 🔴 **„Кайсиева градина“ и „училище Възраждане 3“ днес са неизпълними**, а „кв. Левски“ / „кв. Тракия“ / „кв. Христо Ботев“ / „ж.к. Св. Иван Рилски“ **връщат чужди редове**, защото типовият префикс не е значещ токен (`index.html:6495-6496`). Препоръка: **(а)** Б3 тръгва както е, с О15 подписан изрично; D12 (нормализаторът + `locationKey` в паритета) е лот **Б5**; трите ледждерни реда (`ДГ 39 „Приказка“`, `ОУ Стоян Михайловски` → `kaisieva`; `ДГ 29 „Звънче“` → `vazrazhdane3`) отиват в борда на същия лот. **Този подпис е ЗАДЪЛЖИТЕЛЕН преди старта, не препоръка.**
581: 2. 🔴 **Правилото родител/дете.** Измерено: работи по фраза само за Младост/Възраждане, **не работи** за `druzhba ⊂ asparuhovo`, **не работи** за детската заявка, и **слива** `chaika_kk`+`chaika_kv` без подписано родство. Препоръка: **замразяваме измереното** (фикстури 5–8) и подписваш О16. Вариант Б: `locations.quarter[<code>].parents` в речника — тогава днешната доставка отпада и цикълът се повтаря отначало.
582: 3. **`QUARTER_CODES` +8 (=28)** + машинен гейт „списъкът == речника“. Препоръка: **да**.
583: 4. **Един атомен комит с твой автор** (О4) + наложено авторство на агентските комити (О24). Препоръка: **да**.
584: 5. **`DISTRICT_FALLBACK`: пълното типово правило на ШЕСТ места** (двата двигателя + двата bundle теста, О19) + синтетична положителна фикстура с разделен `_broken`. Препоръка: **пълното правило**.
585: 6. **Етикетът на fallback ред се приема в ДВЕТЕ форми** (О20); затягането до „район X“ влиза заедно с износния гейт във varna_3d. Препоръка: **да** (иначе първата истинска fallback доставка умира мълчаливо).
586: 7. 🔴 **Низът в подножието не е твой подпис днес** (О21): последният комит по файла с решенията е на агент и файлът не е в `SIGNABLE`. Препоръка: подписваш го като **ред „въпрос“ с `тяло: <sha256>`** преди комита на доставката. Две бележки: низът казва „в този файл“ (писан е за файла с решенията), а на 375 px заема долния ляв ъгъл при бутоните за мащаб — §8 проба 10 решава дали остава дословен или искаш къс вариант.
587: 8. **`granitsi_fixtures_06.09.json` → `…_07.09.json`** (`git mv`). Препоръка: **да**.
588: 9. 🔴 **baseline и allow (О22).** Препоръка: **baseline ОСТАВА `f06ac06` в този лот**; новият allow бюджетира **138-те измерени преместени реда** (не 30-те „непокрити днес“); пренасочването на baseline към комита на доставката е **отделен по-късен подписан лот** заедно с нулиране на allow-редовете и прогон `run_gates` → 7/7. Причина: `base == candidate` дава `EXIT_ALLOW_STALE = 3` (`gates/coverage.py:617`), а празен allow прави гейта вакуумно зелен.
589: 10. **Наблюдаемият отказ при чужд код** остава само пинат (фикстура 9). Видим UI-отказ е отделен малък лот.
590: 11. **Перчемлията / решение 10** (О6) — подпиши поименния резерв **преди** комита или сложи изричен „отложено“ ред в опашката.
591: 12. **Документният дълг** (О9 + О23: `_meta.inputs` без паритета) — **отделен комит след пуша**.
592: 13. **Node-паритетната фикстура е ПОСТРОЕНА** (фикстура 11, §3.5) — вече не е обещание без write-set. Препоръка: **да**.
593: 14. 🔴 **Старата опашка `ЗА_ПОДПИС_A.md` (О25)** — маха се от HEAD в комит 3, иначе release е BLOCKED завинаги (`gates/release.py:465-472`). Твоят избор: **архивно име извън глоба** (`scratch/places_search/архив/A_05.09.md`) или само в git историята (тя носи 27 подписани реда).
594: 15. **`LOCALITY_SRC` (О18)** — стеснението, което пази местността от `DISTRICT_FALLBACK`. Препоръка: **да**.
595: 16. **`_meta` става затворен набор в клиента (О17)** — 10/8 ключа и url-формата по измерената форма. Препоръка: **да** (това е половината от G27(б), която иначе остава неналожена във Fire_Varna).
596: 
597: ---
598: 
599: ## 10 · Какво НЕ се пипа
600: 
601: - `Varna_buildings/config/quarter_registry.json` и изобщо репото `Varna_buildings`.
602: - `varna_3d`: чете се **само** блоб; `data/quarters_signed.geojson` никога не влиза във Fire_Varna.
603: - **Написаните 201 квартала** (D18/G17) и леджерът.
604: - `DISTRICT_CODES` (`:6315`), `LOCALITY_CODES` (`:6322`), `EXPECT_KEYS`/`EXPECT2_KEYS`, `EXPECT_COUNT`/`EXPECT2_COUNT`, `TOP`/`MIN_Q`/`DEBOUNCE_MS`, `KINDS`/`KINDS2`/`STATUSES`.
605: - **`gates/baseline/MANIFEST.json`** (О22) и **`INPUT_RELS` в `recall_sweep.py:2815-2816`** (О23).
606: - Адресната търсачка (`index.html:5928-6070`, `data/approx_addresses_v1.json`).
607: - Хидрантите, формата за докладване, Worker-ът, базовите карти и `BASEMAP_PMTILES_ENABLED` (`:4563`).
608: - Двигателите на гейта: `gates/run_gates.py`, `gates/release.py`, `gates/sign.py`, `gates/coverage.py`, `scripts/hooks/pre-push` — нула редакции.
609: - Числата на `granitsi_fixtures_06.09.json` като исторически запис.
610: - `probe_places_fv.mjs` (CDP сондата).
611: - Публикуваните sha и `origin/main` — до ръката на Петър.
612: 
613: ---
614: 
615: ## 11 · Отхвърлени находки
616: 
617: | # | находка (дословно запазена) | измерената причина да не се приложи както е написана |
618: |---|---|---|
619: | 1 | оборител **gates**, блокер 2, поправка **(б)**: „baseline се пренасочва към `f00dd78` … тогава **allow изобщо не е нужен**“ | **Частично отхвърлено.** (Ч) `gates/coverage.py:573-577` прави `allow_stale` от всеки **неползван** ред на allow-файла, а `:617-618` го превръща в `EXIT_ALLOW_STALE = 3`. Днешният подписан allow носи 150 реда, бюджетирани срещу доставката от 05.09; при `base = f00dd78` те стават неползвани → **изход 3, не 0**. Мярката на оборителя е правена с `allow=None`, а `gates/run_gates.py:199-217` избира файла от папката, ако има такъв. Значи вариант (б) е изпълним само ако старият allow бъде **изтрит** в същия комит — а изтриване на подписан артефакт е самостоятелен подписан въпрос. Затова планът избира вариант (а): baseline остава `f06ac06`, allow бюджетира 138-те реда (О22). |
620: | 2 | оборители **gates** и **delivery**, минор: „338 знака плътен текст **ще се пренасят над бутоните** `+/−` при 375 px“ / „ще **закрива** управлението“ | **Отхвърлено като твърдение, прието като проба.** Планерът няма браузър и не е измерил оформлението. (Ч) `index.html:1900` и `:1917` слагат `zoomControl` и `attribCtrl` в **един и същ ъглов контейнер** (`bottomleft`), а Leaflet подрежда контролите в един ъгъл **един под друг**, не един върху друг — „покрива бутоните“ е предположение, не мярка. Рискът (низът изяжда ъгъла и избутва бутоните) е реален, затова влиза в §8 като **проба 10 на екрана на Петър**, а не като изречение в плана. |
621: | 3 | оборител **delivery**, майор G7: цитатът „`:67` `REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]`“ | **Само корекция на цитата, същността е приета.** (Ч) `REPO_ROOT` е на **`recall_sweep.py:68`**; `:64-67` е коментарът над него. Всичко останало в находката е потвърдено: няма argparse и няма `--dump` (grep за `--dump|argparse` в целия файл → нула попадения), `OUTDIR` е `%TEMP%/fv_measures/` (`:84`), а `:4249-4253` презаписва проследения паритетен файл при всеки НЕ-freeze прогон. Планът ползва `:68` в §3.4/О26. |
622: | 4 | v1, §3.2 И11: „**Второто място не е живо:** `BASEMAP_PMTILES_ENABLED = false` (`:4563`)“ | **Собствена находка на v1, отхвърлена по мярка (по минора на оборител „search“).** (Ч) `index.html:4571-4574` `isBasemapPmtilesActive()` връща `true` и при `localStorage[BASEMAP_OVERRIDE_KEY] === '1'` — пътят е достижим и днес. Изводът оцелява по ДРУГА причина, която сега е в коментара на И11: `attribCtrl` е един-единствен и размените махат само собствените си низове (`:4543-4549`, `:4663`, `:4672-4676`). |
623: 
624: ---
625: 
626: ## 12 · Оборване
627: 
628: | оборител | присъда | блокери | майори | минори | приложено в v2 |
629: |---|---|---|---|---|---|
630: | **gates** | **НЕГОДНО** | 3 | 7 | 3 | **Приложени всичките 3 блокера:** (1) `RECS === 375` е грешен критерий — потвърдено чрез `index.html:6648` (`buildIndex` приема разпарсени масиви, не вика валидатор) → §3.6 минава през `accept`/`ensurePlaces`, отрицателната половина е върху текста на `:6313`; (2) baseline→доставка прави проверка 4 невъзможно зелена → **О22**, §9 т. 9, 1.8.1–1.8.3, STOP 17; (3) фикстура 8 не упражнява клона си — потвърдено чрез `index.html:7104-7109` (изричното „район X“ филтрира само по `dph`) → фикстура 10 с разделен `_broken`. **Майори:** D12/родство необявени → **О15/О16**; G10/G11/G13/G14 без падаща половина → §5 пренаписан; агентски низ, наречен „подписан“ → **О21**; половин G27(б) → **О17** (и трите проверки в И10); стъпка 9 иска невъзможен изход → **О23**; §9 т. 13 подписва несъществуваща фикстура → фикстура 11 построена. **Минори:** обемът на allow → 1.8.1 + STOP 1; „комит на Петър“ неразличим → **О24**; надписът при 375 px → §8 проба 10. **Отхвърлено:** поправка (б) на блокер 2 (§11 т. 1) и формулировката „покрива бутоните“ (§11 т. 2). |
631: | **search** | **НЕГОДНО** | 2 | 4 | 2 | **Приложени и двата блокера:** (1) D12 отпада, а §8 проба 4 обещава обратното — механизмът потвърден чрез `index.html:6495-6496` и `recall_sweep.py:424-431` (типовият префикс не е значещ токен) → **О15**, §8 проба 4 пренаписана на измереното (4 чужди реда), §9 т. 1 става задължителен подпис; (2) „дете → детето“ връща 0 — потвърдено чрез същите два реда (числата се изхвърлят) → фикстура 6 замразява **0**, §8 проба 3 пренаписана. **Майори:** `druzhba ⊂ asparuhovo` не работи → фикстура 8 + §3.7 поименна таблица на 11-те двойки; `chaika_kk`+`chaika_kv` се сливат без подписано родство → фикстура 7 + §3.7; `DISTRICT_FALLBACK` е опроверган в три Python проверки — потвърдено чрез `recall_sweep.py:2146`, `:2150`, `tests/test_places_public_bundle.py:291-293`, `:309` → **О19**, §3.4 шест места, §3.3 три правила, фикстура 10 (д)(е); И4 отваря и местността — потвърдено чрез `index.html:6537` → **О18** + `LOCALITY_SRC` + G16. **Минори:** доводът за pmtiles → §11 т. 4 (собствената грешка на v1, поправена); „училище Възраждане 3“ е подвеждащ отговор → §8 проба 2 със зоните. |
632: | **delivery** | **НЕГОДНО** | 3 | 3 | 3 | **Приложени и трите блокера:** (1) втора опашка в HEAD убива release — потвърдено чрез `gates/release.py:171-172`, `:437-458`, `:465-472`, `:1259-1265` и наличния `scratch/places_search/ЗА_ПОДПИС_A.md` → **О25**, `git rm` в комит 3, **G15**, STOP 13, решение 14; (2) baseline в същата сесия → същото като gates блокер 2 (**О22**); (3) `token_parity` никога не влиза в `_meta.inputs` — потвърдено чрез `recall_sweep.py:2815-2816` → **О23**, очакването махнато от стъпка 10, STOP 14. **Майори:** G7 вика несъществуващ флаг и мутира проследен файл → **О26**, G7 пренаписан през `%TEMP%` артефакта и `git worktree`, паритетният файл обявен в §4 стъпка 7 и комит 5; git identity инертна → **О24**, наложени `-c user.name/-c user.email` + следпроверка; И6 обръща подредената тройка → **О20**, двата етикета се приемат. **Минори:** двойният HEAD → §1.1 с една стойност (`f00dd78`, ahead 81) и оборения ред; сондата преди създаването си → §4 стъпка 3 я създава преди редакциите; обхватът на G9 → записан дословно в §5. |

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath index.html -Encoding UTF8 | Select-Object -Skip 6359 -First 150 | ForEach-Object -Begin { $n=6359 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 80ms:
6360:     // Фаза 2 С3 - the classes AS THE HUMAN ASKS FOR THEM: the four hotel kinds are
6361:     // ONE group, every other kind is its own. The group is the render header, the
6362:     // unit of the "…и още N" tail and the unit of the М3/Б2 generosity gate.
6363:     const KIND_GROUP = {
6364:       'Хотел': 'Хотели', 'Семеен хотел': 'Хотели',
6365:       'хотел · без категоризация': 'Хотели', 'апарт-хотел': 'Хотели',
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
6431:       for (let i = w.length - 1; i >= 0; i--) { const v = V[w[i]]; total += v < prev ? -v : v; if (v > prev) prev = v; }
6432:       return String(total);
6433:     }
6434:     function rewriteToken(w) {
6435:       w = w.replace(CYRILLIC_I, 'i');
6436:       if (w === 'св') return 'свети';
6437:       if (w === 'др') return 'доктор';
6438:       const roman = romanValue(w);
6439:       if (roman !== null) return roman;
6440:       if (ORD_WORDS[w] !== undefined) return ORD_WORDS[w];
6441:       const attached = TOKEN_ORD.exec(w);
6442:       return attached ? attached[1] : w;
6443:     }
6444:     function placeTokens(s) {
6445:       let text = String(s == null ? '' : s).toLowerCase().replace(TYPO, ' ');
6446:       for (const pair of ABBR) text = text.replace(pair[0], pair[1]);
6447:       text = text.replace(ORD_SUFFIX, '$1');     // "7-мо" -> "7": norm() would split it
6448:       const out = [];
6449:       for (const word of norm(text).split(' ')) {
6450:         if (!word) continue;
6451:         for (const part of (COMPOUNDS[word] || [word])) {
6452:           const t = skel(rewriteToken(part));
6453:           if (t) out.push({ s: t, orig: word, num: /^\d+$/.test(t) });
6454:         }
6455:       }
6456:       return out;
6457:     }
6458:     const keyOf = (s) => placeTokens(s).map((t) => t.s).join(' ');
6459:     // ЛОТ 1в амандамент А4 т. 1 (ADR 008 D2): the generic GEOGRAPHIC words of an
6460:     // alias, normalised by the very tokeniser that will meet them.
6461:     const ALIAS_GENERIC = new Set(['варна', 'гр', 'град'].map(keyOf));
6462:     // А4 т. 2: how many tokens of a query are significant (A5's own filter). A
6463:     // one-word query never reaches EXACT_ALIAS — measured, „синчец“ has to keep
6464:     // ДГ 30 „Синчец“ first, and a CURRENT name must not lose to somebody's OLD one
6465:     // on a partial match. The alias tokens are in `aset` anyway.
6466:     const aliasSignificant = (qt) =>
6467:       qt.filter((t) => !t.num && t.orig.length > 2 && ADDR.indexOf(t.orig) < 0).length;
6468:     function exactAlias(qt) {                    // [] = this query is nobody's whole alias
6469:       if (!EXACT_ALIAS || aliasSignificant(qt) < 2) return [];
6470:       return EXACT_ALIAS.get(qt.map((t) => t.s).join(' ')) || [];
6471:     }
6472:     // Д7/D3: WHICH alias the query matched — the card names the source of THAT
6473:     // string. -1 = the current name matched (then the record's own `src` speaks).
6474:     function matchedAliasIndex(rec, qt) {
6475:       if (!rec || !rec.atk || !rec.atk.length) return -1;
6476:       const whole = exactAlias(qt);
6477:       for (const hit of whole) if (hit.rec === rec) return hit.i;
6478:       for (const t of qt) {
6479:         if (t.num || t.orig.length <= 2 || ADDR.indexOf(t.orig) >= 0) continue;
6480:         if (rec.nset.has(t.s)) continue;         // А4: an exact NAME match owns the token
6481:         for (let i = 0; i < rec.atk.length; i++) if (rec.atk[i].has(t.s)) return i;
6482:       }
6483:       return -1;
6484:     }
6485: 
6486:     // ---- Д2/Д3/В7: load once, validate before trusting, cache only what validated
6487:     let RECS = [], FORMS = null, CLASS_OF = null, placesPromise = null, GROUP_SIZE = null;
6488:     let EXACT_NAME = null;                       // ЛОТ 1 решение 2: joined name tokens -> records
6489:     let EXACT_ALIAS = null;                      // ЛОТ 1в D2: joined alias tokens -> {rec, i}
6490:     let STREET = null;                           // ЛОТ 1в-Б D6: joined street phrase -> records
6491:     // F12-е: the dictionary's own generic words, lifted out of buildIndex so the
6492:     // М7 branch in search() can ask the SAME significance question the index asks.
6493:     let GENERIC_WORDS = new Set();
6494:     // Steps (а)-(г) of П7 on ONE token — 1:1 with recall_sweep.py significant_token().
6495:     const isSignificantToken = (t) => !t.num && t.orig.length > 2 && t.s.length > 2
6496:       && ADDR.indexOf(t.orig) < 0 && !GENERIC_WORDS.has(t.s);
6497:     const groupOf = (rec) => KIND_GROUP[rec.e.kind] || rec.e.kind;
6498:     const colourOf = (kind) => GROUP_COLOUR[KIND_GROUP[kind]] || 'hotel';   // К1
6499:     // С3 - the bug Sol found: the <=300 generosity of М3/Б2 was read off the WHOLE
6500:     // index. With 361 records that would switch the keyless branch off entirely, so
6501:     // it is decided per CLASS: a record is generous if its own group is <= GEN_CAP.
6502:     const genOk = (rec) => (GROUP_SIZE.get(groupOf(rec)) || 0) <= GEN_CAP;
6503:     // ЛОТ 1в D1/S2: same length, same order, every letter from the closed list.
6504:     // A missing or unknown source is a REFUSAL, not a blank line on the card.
6505:     function validAliasSrc(r) {
6506:       if (r.old_names_src.length !== r.old_names.length) return false;
6507:       for (const code of r.old_names_src)
6508:         if (typeof code !== 'string' || !ALIAS_SRC_LINE[code]) return false;
6509:       return true;

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath index.html -Encoding UTF8 | Select-Object -Skip 6246 -First 19 | ForEach-Object -Begin { $n=6246 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 73ms:
6247:   // =========================================================================
6248:   (function initPlacesSearch() {
6249:     const HOTELS_SEARCH_ENABLED = true;          // kill-switch (Д11): false = no branch at all
6250:     if (!HOTELS_SEARCH_ENABLED) return;
6251:     const inputEl = document.getElementById('addrSearchInput');
6252:     const theirsEl = document.getElementById('addrSearchResults');
6253:     const box = document.getElementById('placesSearchResults');
6254:     if (!inputEl || !theirsEl || !box) return;   // header markup missing -> no-op
6255: 
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath index.html -Encoding UTF8 | Select-Object -Skip 7037 -First 123 | ForEach-Object -Begin { $n=7037 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 88ms:
7038:         const rows = orderCategory(cls, c), exact = EXACT_NAME.get(qt.map((t) => t.s).join(' '));
7039:         return { category: true, hasKey: hasKey,
7040:                  rows: exact ? stableUnique(orderCategory(exact, c).concat(rows)) : rows };
7041:       }
7042:       // М7 (план §3й-б S4) — a BARE location word, without a class key. It stands
7043:       // BEFORE the М3/Б2 generosity gate on purpose: „златни пясъци“ is a place the
7044:       // human named in full, and the size of the class it falls in may not decide
7045:       // whether we answer. Only `qtk` and `ltk` trigger it: `legtk` is a row's
7046:       // history and not its address (Кими К5-г), so „зпз“ fires as the locality it
7047:       // is TODAY and never as the old zone word; the kind is the class list, not a
7048:       // place; and the district enters only through rows with no quarter of their
7049:       // own, exactly as the district branch says. `hasKey` stays false, so our
7050:       // section still renders UNDER the untouched building address search.
7051:       // F12-е: every word must be SIGNIFICANT by the rule the rest of the machine
7052:       // uses — the number filter alone let the TYPE PREFIXES of the names in
7053:       // („к.к.“, „кв.“, „ж.к.“, „м-т“, „с.о.“), and „к“ answered with 163 rows.
7054:       // Амандамент №3 т. 6 — fail-closed: an EMPTY GENERIC_WORDS means the
7055:       // dictionary did not load, and a degraded client must not invent its own
7056:       // significance rule and answer with places (the reference: the same guard
7057:       // on GENERIC_TOKENS in bare_location_query).
7058:       if (!hasKey && GENERIC_WORDS.size && R.length && !R.some((t) => t.orig === DISTRICT_MARK)
7059:           && !R.some((t) => STREET_MARK.indexOf(t.orig) >= 0) && R.every(isSignificantToken)) {
7060:         const qHit = cls.filter((r) => R.every((t) => r.qtk.indexOf(t.s) >= 0));
7061:         const lHit = cls.filter((r) => R.every((t) => r.ltk.indexOf(t.s) >= 0));
7062:         if (qHit.length || lHit.length) {
7063:           const bphrase = R.map((t) => t.s).join(' ');
7064:           const dHit = cls.filter((r) => !r.e.quarter && r.dph.has(bphrase));
7065:           const bare = stableUnique(orderCategory(cls.filter((r) => nameHasPhrase(r, R)), c)
7066:                                     .concat(orderCategory(qHit, c), orderCategory(lHit, c),
7067:                                             orderCategory(dHit, c)));
7068:           if (bare.length) return { category: true, hasKey: false, rows: bare };
7069:         }
7070:       }
7071:       if (!hasKey) {                             // М3/Б2 generosity gate, PER CLASS (С3)
7072:         cls = cls.filter(genOk);
7073:         if (!cls.length) return { category: false, hasKey: false, rows: [] };
7074:         // ЛОТ 1в-В (S3): „район X“ is explicit with or without a class word — the
7075:         // marker is the word the HUMAN wrote, and it asks for the district of every
7076:         // record. Nothing else of this lot fires without a key: a bare location
7077:         // phrase stays what it was, so the frozen reference keeps its keyless rows.
7078:         if (R.some((t) => t.orig === DISTRICT_MARK)) {
7079:           const rest = R.filter((t) => t.orig !== DISTRICT_MARK);
7080:           const dphrase = rest.map((t) => t.s).join(' ');
7081:           const rows = rest.length ? cls.filter((r) => r.dph.has(dphrase)) : [];
7082:           if (rows.length) return { category: true, hasKey: false, rows: orderCategory(rows, c) };
7083:         }
7084:       }
7085:       if (hasKey) {                              // А3′: key + a purely zone/kind rest = filtered list
7086:         const zk = new Set(), nm = new Set();
7087:         for (const r of cls) { for (const v of r.zkset) zk.add(v); for (const v of r.nset) nm.add(v); }
7088:         // ЛОТ 1 решение 1: the class-wide name veto below is right about the CLASS
7089:         // and wrong about the RECORD. When the rest is the WHOLE significant phrase
7090:         // of some record's location and only that veto stands in the way, the choice
7091:         // is made PER RECORD: the exact name/alias sequence first, then the rows of
7092:         // the location itself.
7093:         const vetoed = R.some((t) => nm.has(t.s)), phrase = R.map((t) => t.s).join(' ');
7094:         // ЛОТ 1в-В (S3): „ул./бул./пл. X“ is a STREET before it is anything else —
7095:         // „бул. Владислав Варненчик“ is a boulevard, and the quarter of the same
7096:         // name must never take the query off it.
7097:         if (R.some((t) => STREET_MARK.indexOf(t.orig) >= 0)) {
7098:           const marked = streetRows(R, cls, c);
7099:           if (marked) return { category: true, hasKey: hasKey, rows: marked };
7100:         }
7101:         // ЛОТ 1в-В (S3): the EXPLICIT „район X“ asks for the whole district —
7102:         // every record in it, with a quarter or without. It is recognised by the
7103:         // word the human wrote, never by the district name alone.
7104:         if (R.some((t) => t.orig === DISTRICT_MARK)) {
7105:           const rest = R.filter((t) => t.orig !== DISTRICT_MARK);
7106:           const dphrase = rest.map((t) => t.s).join(' ');
7107:           const rows = rest.length ? cls.filter((r) => r.dph.has(dphrase)) : [];
7108:           if (rows.length) return { category: true, hasKey: hasKey, rows: orderCategory(rows, c) };
7109:         }
7110:         // ЛОТ 1в-В (S3): the BARE location phrase — the quarter first, then the
7111:         // locality and the row's own old words, then the district and ONLY for
7112:         // records with no quarter of their own. With that restriction „училище
7113:         // младост“ is „the schools of the quarter plus the schools of the district
7114:         // that have no quarter“ — the two Petar named are in it; without it the
7115:         // same query is an unbounded district sweep that buries them.
7116:         const qRows = cls.filter((r) => r.qph.has(phrase));
7117:         const lRows = cls.filter((r) => r.lph.has(phrase) || r.gph.has(phrase));
7118:         const dRows = cls.filter((r) => !r.e.quarter && r.dph.has(phrase));
7119:         if (qRows.length || lRows.length || dRows.length) {
7120:           const head = vetoed ? orderCategory(cls.filter((r) => nameHasPhrase(r, R)), c) : [];
7121:           const rows = stableUnique(head.concat(orderCategory(qRows, c),
7122:                                                 orderCategory(lRows, c),
7123:                                                 orderCategory(dRows, c)));
7124:           if (rows.length) return { category: true, hasKey: hasKey, rows: rows };
7125:         }
7126:         if (R.every((t) => zk.has(t.s)) && !vetoed) {
7127:           const flt = cls.filter((r) => R.every((t) => r.zkset.has(t.s)));
7128:           if (flt.length) return { category: true, hasKey: hasKey, rows: orderCategory(flt, c) };
7129:         }
7130:       }
7131:       // ADR 008 D6: exact name/alias -> zone (П7) -> STREET -> fuzzy/fail-open. With a
7132:       // key the answer is the class on that street; without one it is the address the
7133:       // human typed, and `hasKey` stays false — so our section renders UNDER the
7134:       // building address search, whose rows and whose Enter stay exactly as they were.
7135:       const street = streetRows(R, cls, c);
7136:       if (street) return { category: true, hasKey: hasKey, rows: street };
7137:       let rows = runScored(cls, R, hasKey, sk.dead, c);
7138:       if (!rows.length && hasKey)                // А1 fail-open: the keys become plain names
7139:         rows = runScored(RECS, sk.slots.map((x) => x.t), false, sk.dead, c);
7140:       return { category: false, hasKey: hasKey, rows: rows };
7141:     }
7142:     // С1: does THIS text carry a key? A few tokens against the dictionary -- cheap
7143:     // enough to answer SYNCHRONOUSLY on every keystroke, which is what lets the
7144:     // inline remainder go before their 120 ms debounce mutates anything.
7145:     const hasKeyFor = (q) => !!(RECS.length && CLASS_OF && splitKeys(placeTokens(q)).keys.length);
7146: 
7147:     // ---- our own dropdown (Д4/Д5/Д6) — textContent only, never an asr-* selector
7148:     let shown = [], shownFor = null, theirStatusFor = null, tidiedByUs = false, keyed = false;
7149:     let gen = 0, dismissed = false, timer = null, warned = false;
7150:     let placeMk = null, placePopup = null, lastPick = null, mineActive = false;
7151:     let lastAliasI = -1;                         // D3: which old name the pick matched
7152:     let restoreArmed = false;                    // С4: armed by a pick, spent once
7153:     function warnOnce(e) { if (warned) return; warned = true; console.warn('[places-search] ' + ((e && e.message) || e)); }
7154:     const guarded = (fn) => function (ev) { try { fn(ev); } catch (e) { warnOnce(e); } };   // Д11
7155:     function span(cls, text) { const el = document.createElement('span'); el.className = cls; el.textContent = text; return el; }
7156:     function hideMine() {
7157:       box.classList.remove('visible'); box.replaceChildren();
7158:       box.style.top = ''; box.style.maxHeight = '';
7159:       keyed = false; bareTheirs();               // С1: an empty list leaves no inline remainder
7160:       shown = []; shownFor = null;

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git -c safe.directory=C:/git/varna_3d -C C:/git/varna_3d show --format=fuller --stat c1bb9dc d17de0d 05f485e' in C:\git\Fire_Varna
 succeeded in 0ms:
commit c1bb9dceac4f416cd855485d5fa726b02c7b0d69
Author:     Petar1984 <petar.dikov2019@gmail.com>
AuthorDate: Mon Sep 7 07:23:15 2026 +0300
Commit:     Petar1984 <petar.dikov2019@gmail.com>
CommitDate: Mon Sep 7 07:23:15 2026 +0300

    data: place coordinates from KAIS bodies (Б0 т. 11) and identity re-keyed without the zone (375 place_id unchanged), inputs pinned
    
    57 identity zones refreshed; registry manifest accepted and pinned (decision 6: 9 zone rows, 3 grandfathered + 6 board_queue).
    
    Подписвам по амандамент №3 (решения 1–6): data/place_identity.json SHA256 4819ab3e1d74f516de051b5f05abf4721c6f8c42cf2c5c2a293ba95eedc7d0c2 (ключ <файл>|skel(име), котви kais_i и УИН, 375/375 place_id непроменени спрямо tests/fixtures/identity_rekey_base_2026-09-07.json, 57 зони освежени само върху редове с празен записан квартал); data/fire_varna_location_inputs.json SHA256 c7450ded1b8ade5bdb3b63924971d2be0d9b9ea1a792175df0331526ed4679ee (пиновете, приети с --accept-identity); data/registry_manifest.json SHA256 bb04640e9762a12a5028b99ee70b1053687cfa4ed55b6e7e2f4c2e191b114abb (девет реда със сменена зонова дума, приети по решение 6).

 data/fire_varna_location_inputs.json |   32 +-
 data/place_identity.json             | 2808 ++++++++++++++++++++++++++--------
 data/registry_manifest.json          |   18 +-
 3 files changed, 2191 insertions(+), 667 deletions(-)

commit d17de0d483d9206a9df447ac99cd83bf15ab5ab8
Author:     Petar1984 <petar.dikov2019@gmail.com>
AuthorDate: Mon Sep 7 07:23:19 2026 +0300
Commit:     Petar1984 <petar.dikov2019@gmail.com>
CommitDate: Mon Sep 7 07:23:19 2026 +0300

    data: places and hotels with quarter by signed polygon, search dictionary regenerated
    
    Подписвам по нощния план (Б2, Б0 т. 4/5/6/9/12) и амандамент №3: data/fire_varna_places.json SHA256 3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66; data/fire_varna_hotels.json SHA256 eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51; data/place_categories.json SHA256 9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231. Таблица на изходите: 201 записани непроменени (G17), 65 присвоени по полигон (57 написани от SIGNED_POLYGON, 8 честно неписани), 63 в ръба, 41 с пин извън всяка граница, 5 в двойна зона; районна резерва 0. Неподвижна точка: места, хотели и леджер байт-еднакви при повторен прогон.

 data/fire_varna_hotels.json | 169 ++++++++++++++----
 data/fire_varna_places.json | 427 +++++++++++++++++++++++++++++++++++---------
 data/place_categories.json  | 320 ++++++++++++++++++++++-----------
 3 files changed, 695 insertions(+), 221 deletions(-)

commit 05f485e844333a86aa418de660e84e72ed9e0e4e
Author:     Petar1984 <petar.dikov2019@gmail.com>
AuthorDate: Mon Sep 7 07:23:23 2026 +0300
Commit:     Petar1984 <petar.dikov2019@gmail.com>
CommitDate: Mon Sep 7 07:23:23 2026 +0300

    data: p8a quarter assignment ledger 07.09
    
    Подписвам: scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json SHA256 5ec64c682a46463c1f4890510736a13a5766ada61fcc757af281f6c82d3a7d94; _meta.base_rev 8d60aebb365fb8e74ccc863d3b3db90b74180a3b; старият леджер lot1v_locations_375.json е непроменен (SHA256 d5050f1cfb3d4289e62a288b64a4658b15106a7876f7aa8fb1d1a39980c76075). M6 върху този леджер: нула падания, точно осемте pending_signature реда (ДАЛИЯ ГАРДЪН, МАГНОЛИЯ 1 И 2, Маяк, НЕПТУН, РУСАЛКА, Романтика, СТРАНДЖА, Фрегата).

 .../_addr/lot1v_locations_375_p8a_07.09.json       | 34669 +++++++++++++++++++
 1 file changed, 34669 insertions(+)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git log -2 --format='%H %an <%ae> %s'" in C:\git\Fire_Varna
 succeeded in 0ms:
e6ba50e804e75927d07facc9ff81241bbe82e2a1 Claude Architect <architect@local> docs(plan): Б3 quarter search delivery plan v2 — DRAFT, unsigned (5 scouts, 3 refuters НЕГОДНО on v1, synthesis); awaiting Kimi К28 / Astra S28 and Petar's Gate 1
f00dd781ba8c41d70f84c4f1621c04b65afd1d74 Claude Architect <architect@local> state: §8 — Б2 closed by Petar's three varna_3d commits (c1bb9dc, d17de0d, 05f485e; OID 7/7), Б3 planning workflow started

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
const fs=require('fs'); const cp=require('child_process'); const html=fs.readFileSync('index.html','utf8'); const slice=html.split(/\\r?\\n/).slice(6255,7154).join('\\n'); const git=(p)=>cp.execFileSync('git',['-c','safe.directory=C:/git/varna_3d','-C','C:/git/varna_3d','show','05f485e:'+p],{encoding:'utf8'}); const ht=git('data/fire_varna_hotels.json'),pt=git('data/fire_varna_places.json'),ct=git('data/place_categories.json');const payload={'data/hotels.json':ht,'data/places.json':pt,'data/place_categories.json':ct};
const make=(s,cryptoOn=false)=>new Function('window','caches','document','map','fetch',s+'; return {validateHotels,validatePlaces2,accept,ensurePlaces,cacheText,get RECS(){return RECS},get CACHE(){return PLACES_CACHE}}')({crypto:cryptoOn?globalThis.crypto:null},undefined,{}, {getCenter:()=>({lat:43.2141,lng:27.9147})},async url=>({ok:true,text:async()=>payload[url]}));
(async()=>{const api=make(slice); console.log('slice compiles: true; validators',api.validateHotels(JSON.parse(ht),ht),api.validatePlaces2(JSON.parse(pt),pt));try{await api.ensurePlaces();console.log('ensure count',api.RECS.length)}catch(e){console.log('ensure ERROR:',e.message,'RECS',api.RECS.length)}
const codes=Object.keys(JSON.parse(ct).locations.quarter);let open=slice.replace(\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE'];\",\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE', 'SIGNED_POLYGON', 'DISTRICT_FALLBACK'];\").replace(/const QUARTER_CODES = \\[[\\s\\S]*?\\];/,'const QUARTER_CODES = '+JSON.stringify(codes)+';'); const newApi=make(open); await newApi.ensurePlaces();console.log('opened lists crypto OFF:',newApi.RECS.length); const broken=make(open.replace(\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE', 'SIGNED_POLYGON', 'DISTRICT_FALLBACK'];\",\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE'];\"));try{await broken.ensurePlaces();console.log('broken count:',broken.RECS.length)}catch(e){console.log('broken original QUARTER_SRC:',e.message,'RECS',broken.RECS.length)}
console.log('global crypto',typeof globalThis.crypto,'subtle',"'!!globalThis.crypto?.subtle);let called=0;const valid=()=>{called++;return false}; await make(slice,true).accept(pt,'"'329310f577e8353673b9014af99624a78ab825fb0ad53e93fc572a28660d88c0',valid);console.log('crypto ON mismatched pin validator calls:',called);
})();
'@ | node" in C:\git\Fire_Varna
 exited 1 in 104ms:
[stdin]:3
(async()=>{const api=make(slice); console.log('slice compiles: true; validators',api.validateHotels(JSON.parse(ht),ht),api.validatePlaces2(JSON.parse(pt),pt));try{await api.ensurePlaces();console.log('ensure count',api.RECS.length)}catch(e){console.log('ensure ERROR:',e.message,'RECS',api.RECS.length)}
                                                                                     ^

TypeError: Cannot read properties of undefined (reading 'validateHotels')
    at [stdin]:3:86
    at [stdin]:6:3
    at runScriptInThisContext (node:internal/vm:209:10)
    at node:internal/process/execution:446:12
    at [stdin]-wrapper:6:24
    at runScriptInContext (node:internal/process/execution:444:60)
    at evalFunction (node:internal/process/execution:279:30)
    at evalTypeScript (node:internal/process/execution:291:3)
    at node:internal/main/eval_stdin:53:5
    at Socket.<anonymous> (node:internal/process/execution:201:5)

Node.js v22.19.0

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
const fs=require('fs'); const cp=require('child_process'); const html=fs.readFileSync('index.html','utf8'); const slice=html.split(/\\r?\\n/).slice(6255,7154).join('\\n')+'\\n'; const git=(p)=>cp.execFileSync('git',['-c','safe.directory=C:/git/varna_3d','-C','C:/git/varna_3d','show','05f485e:'+p],{encoding:'utf8'}); const ht=git('data/fire_varna_hotels.json'),pt=git('data/fire_varna_places.json'),ct=git('data/place_categories.json');const payload={'data/hotels.json':ht,'data/places.json':pt,'data/place_categories.json':ct};
const make=(s,cryptoOn=false)=>new Function('window','caches','document','map','fetch',s+'; return {validateHotels,validatePlaces2,accept,ensurePlaces,cacheText,get RECS(){return RECS},get CACHE(){return PLACES_CACHE}}')({crypto:cryptoOn?globalThis.crypto:null},undefined,{}, {getCenter:()=>({lat:43.2141,lng:27.9147})},async url=>({ok:true,text:async()=>payload[url]}));
(async()=>{const api=make(slice); console.log('slice compiles: true; validators',api.validateHotels(JSON.parse(ht),ht),api.validatePlaces2(JSON.parse(pt),pt));try{await api.ensurePlaces();console.log('ensure count',api.RECS.length)}catch(e){console.log('ensure ERROR:',e.message,'RECS',api.RECS.length)}
const codes=Object.keys(JSON.parse(ct).locations.quarter);let open=slice.replace(\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE'];\",\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE', 'SIGNED_POLYGON', 'DISTRICT_FALLBACK'];\").replace(/const QUARTER_CODES = \\[[\\s\\S]*?\\];/,'const QUARTER_CODES = '+JSON.stringify(codes)+';'); const newApi=make(open); await newApi.ensurePlaces();console.log('opened lists crypto OFF:',newApi.RECS.length); const broken=make(open.replace(\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE', 'SIGNED_POLYGON', 'DISTRICT_FALLBACK'];\",\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE'];\"));try{await broken.ensurePlaces();console.log('broken count:',broken.RECS.length)}catch(e){console.log('broken original QUARTER_SRC:',e.message,'RECS',broken.RECS.length)}
console.log('global crypto',typeof globalThis.crypto,'subtle',"'!!globalThis.crypto?.subtle);let called=0;const valid=()=>{called++;return false}; await make(slice,true).accept(pt,'"'329310f577e8353673b9014af99624a78ab825fb0ad53e93fc572a28660d88c0',valid);console.log('crypto ON mismatched pin validator calls:',called);
})();
'@ | node" in C:\git\Fire_Varna
 succeeded in 157ms:
slice compiles: true; validators false false
[places-search] places payload unavailable
ensure ERROR: places payload unavailable RECS 0
[places-search] legacy_by_row: друг пакет — старите зонови думи са изключени
opened lists crypto OFF: 375
broken original QUARTER_SRC: places payload unavailable RECS 0
[places-search] places payload unavailable
global crypto object subtle true
crypto ON mismatched pin validator calls: 0

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md' -Encoding UTF8 | Select-Object -Skip 140 -First 8 | ForEach-Object -Begin { "'$n=140 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 35ms:
141: Write-set: `src/fire_varna_locations.py` (каналът `SIGNED_POLYGON` + `DISTRICT_FALLBACK`, четене на `quarters_signed.geojson` по sha; `LEDGER` сочи НОВ датиран леджер `scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` с `_meta.base_rev` = комитът на стария; старият не се пипа), `src/qa_p8a.py`, `data/fire_varna_places.json`, `data/fire_varna_hotels.json` (износът), `data/fire_varna_location_inputs.json` (пиновете, вкл. `quarters_signed.geojson` sha), новият леджер. Съобщения: `feat(p8a): SIGNED_POLYGON channel with district fallback, new dated ledger, written quarters untouched` · `data: places export with quarter_attribution (decisions 3)`. Правила: само ПРАЗЕН квартал се пише; най-малкият съдържащ полигон; двойка без подписано родство и място в двата → `disputed`, не се пише; ръб `max(50, precision_m)` → `edge_pending`; без полигон → районът само по Б0 т. 4 (i)–(iii): не в зони на отложени кодове, не при `pin_outside_all` без съгласен свидетел, и винаги заместим; записан ≠ полигон → леджер `disputed`, редът непроменен (G17). Гейт: fallback-ред в зона на отложен код → ✗; fallback-ред, защитен от G17 в следваща версия → ✗ (фикстура с втора версия, в която подписан полигон трябва да го замести). Координати: САМО от `place_identity.json` след хода по Б0 т. 11 (G9 зелен); изнесените координати са забранени за присвояване (D7) — гейт: скриптът не отваря `data/fire_varna_*.json` за четене на координати (AST-проверка като в Н4). Изходите на таблицата по Б0 т. 12 се броят и записват поименно. Десетият ключ по Б0 т. 5 във varna_3d: `META_KEYS` (places 9→10, hotels 7→8 — измерено от Astra), двата износителя (`export_fire_varna_places.py:816`, `export_fire_varna_hotels.py:420`), QA/M6 и `build_place_categories.py` (родители и полигонен провенанс) в един varna_3d комит на изпълнителя; **износените данни (`data/fire_varna_*.json`, новият леджер) остават стейджнати за комита на Петър** (D16/G4) с готово съобщение в доклада. **Гейт (червен):** G17 (всеки записан квартал в стария леджер-блоб `git show <base_rev>:…` е байт-равен в новия износ), G4 (fail-closed без подпис → тук подписът е този план + sha на решенията, записани в `_meta`), `qa_fire_varna_places_export.py` с 10 ключа, брой присвоени = броят „би получил“ от Н2 (мярката и резултатът трябва да съвпадат до място), `edge_pending` и `disputed` в леджера поименно, `python -m unittest` зелен.
142: 
143: ### Б3 · Търсене по квартал F13 (Fire_Varna) — СУТРИНТА, не нощес (Astra S21 т. 4–5: доставката е един атомен комит с подписи, които само Петър дава)
144: Write-set: `index.html` (`QUARTER_SRC`, `QUARTER_CODES` +41, `PLACES_CACHE` v7, нормализаторът D12 за новите имена, правилото родител/дете при търсене: дете → детето; родител → родителят и подписаните му деца; картончето: редът за атрибуция от `_meta.quarter_attribution`), `data/places.json`, `data/hotels.json` (доставката от Б2 по подредената тройка на D13: пинове + `expectations.json` + двата преписа), `tests/test_granitsi_fixtures.py` (шестте S17 фикстури, вкл. `client_cache_matrix` в node — изпълнителят назовава изпълнителя), `release/sign` артефактите по гейта на доставката от 05.09. Съобщения: `feat(search): quarter search over signed boundaries, attribution row, QUARTER_CODES +41, cache v7` · `data: places delivery with quarter_attribution (D13 ordered)` · `tests: S17 fixtures fail on broken candidates`. Пълният write-set по Astra S21 т. 4: трите data файла (`places.json`, `hotels.json`, **`place_categories.json`**), `index.html` (`PLACES_CACHE` v7, трите SHA, `LEGACY_BUNDLE_SHA`, затворените списъци `:6265`, зареждане/валидиране `:6528`, атрибуцията в паметта `:6657`, D12/индекс/търсене и картончето `:7253`; **типово правило за `DISTRICT_FALLBACK`** — районен код в `quarter` не бива да чупи `!quarter` условието на районното търсене `:7064`), двата bundle теста (`test_places_public_bundle.py:55`, `test_hotels_public_bundle.py:61`), `expectations.json`, трите манифеста, референтният/паритетният корпус и Python паритетът на търсенето (D13 `:62`). Нощес изпълнителят **подготвя** дифа като кръпка (`scratch/places_search/b3_patch_07.09.diff`, непроследена) и фикстурата `client_cache_matrix.foreign_code_while_other_bundle_valid` (Node: валидни хотели, кеш v6/v7, crypto on/off; приемане = двата булеви валидатора минават И 150+225 реда реално се индексират; чужд код → наблюдаем отказ, не `places2=[]` мълчаливо). **Гейт (сутрин, след комитите и подписите на Петър):** замразената референция (нула изгубени резултати), шестте фикстури падат на счупен кандидат и минават след, `python -m unittest discover -s tests` и `python -m gates.run_gates` зелени, размерът ≤ 5 MB, никаква геометрия в проследените `data/*.json` на Fire_Varna (grep за `coordinates` в тях → 0 извън `data/hydrants.json`).
145: 
146: ### Б4 · Одит на Б1–Б3 и докладът
147: Одитор (Opus, read-only, друг агент) на всеки лот: гейтовете преизпълнени, дифът срещу write-set-а (всеки допълнителен файл = находка), авторите, съобщенията, sha веригата решения → граници → леджер → износ → доставка. Докладът `docs/audits/ДОКЛАД_07.09_нощна_смяна.md` (Fire_Varna) носи числата на А и Б, всички sha, спрелите лотове с причината, и §„Какво прави Петър сутринта“: комит на `quarters_signed.geojson` (G4), препотвърждаване на решенията по sha, преглед на дифа в трите репа, регистърът (Ваялар, Евксиноград/Траката, Цветен квартал, `parents`, 16-те), Gate 2, пуш.
148: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md' -Encoding UTF8 -TotalCount 92 | ForEach-Object -Begin { "'$n=0 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 6ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/decisions/010_signed_quarter_boundaries.md' -Encoding UTF8 | Select-Object -Skip 50 -First 15 | ForEach-Object -Begin { "'$n=50 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 33ms:
51: 
52: **D8 · Йерархията — само подписана и геометрично доказана.** Родство се чете единствено от `parents` (днес 6 записа), ациклично И доказано: **дете ⊆ родител в рамките на `precision_m` буфер**; фалшив `parent` = червено. **Числовата опашка в `is_child` (`:488-503`) не е родство при полигони.** „≤ 1 полигон на място“ важи между НЕСРАВНИМИ квартали. **В ПРАЗЕН ред пише детето; в ред с написан квартал полигонът НИКОГА не уточнява.** Възраждане 1–4 нямат `parents` — поправка в регистъра, ПРЕДИ кода (D14).
53: 
54: **D9 · Версии, диф и откат (К5, S1).** **ВСЯКА нова версия иска подпис на Петър.** Прагове: > 2 места сменят квартал ИЛИ > 10 % площ → двоен запис преди/след и пълно преизмерване; под тях — обикновен отчет. `--diff <предишна>` е ГЕЙТ с изход ≠ 0 над праговете (G15). **Версия 1: диф-гейтът е НЕПРИЛОЖИМ, не червен.** **Откат на лоша версия:** предишната подписана версия се връща като НОВА версия (`version` расте, `previous_version` сочи отхвърлената, `note` носи довода), минава пълния G1+G15 и се комитва от Петър; никакво `git revert` върху геометрия и никакво тихо редактиране. Всеки диф се предава като ред клас „въпрос“ (по D3 не може да е „артефакт“).
55: 
56: **D10 · Леджерът и пиновете (S1, S2).** Към **23-те колони** (М0.4): точка/тяло + CRS, кандидат-полигони, канал, `dist_to_edge_m`, състояние по D6, старо/ново по КОД, хешове на геометрия/регистър/алгоритъм, `approval_digest`. В `_meta`: `pins_polygons` до `pins_m6` (`:1111`), `polygon_review` до `pending_signature` (`:1140`), и **`base_rev` — ревизията P7, срещу която се мерят D18 и манифестът-данни**. **Координатата идва от `lat`/`lon`, добавени в `data/place_identity.json`** (мерено: 375 обекта, 0 с координата) като НОВ ПИНАТ вход в `RECORDED_INPUTS` (`:91-92`), с гейт G9. **Пиновете на `quarters_signed.geojson`, `place_identity.json` и `web/varna_buildings_3d.geojson` влизат в `build_inputs` (`:1247-1253`) И СЕ СВЕРЯВАТ в `_check_pins` (`:623-639`) и в G-M6.** `--inputs` (`:1305-1310`) е ПИСАТЕЛ, пуска се веднъж.
57: 
58: **D11 · Инструментът и provenance (S3).** Свой „режим граница“ във `varna_3d/web`, **нула нови runtime зависимости** (`web/vendor` държи само maplibre-gl **5.7.2** — `web/vendor/maplibre-gl.js:3` — и pmtiles 4.3.0; М0.18). `pitch = 0` + `map.setTerrain(null)` (`web/index.html:1962-1963`), `#pitch` disabled, кликът отговаря ПРЕДИ хидранта (`:4571`). Лентата на неточността: `line-width` по `156543.03392·cos(43,2°)/2^z` → z13 3,6 · z16 28,7 · z18 114,9 px за 50 m (М0.13). Слоеве-свидетели: КАИС телата, 375-те пина, OSM етикет-точките, **предишната версия като отделен слой**. Записва целия набор на D1. `preserveDrawingBuffer` — **един условен ред** зад `?granitsa` (`:828-841`). **STOP:** безусловен `preserveDrawingBuffer`; какъвто и да е `POST` в `serve.py`. Износ = Blob + `<a download>`.
59: 
60: **D12 · Търсенето (клас B) — К6 + S4.** Идемпотентен `location_key(toks) -> (type, phrase)`, приложен ИДЕНТИЧНО върху индекса и остатъка, дефиниран върху **СПИСЪК ОТ ТОКЕНИ**. Типовият префикс е поредица с двете си арности. Хвърля съюза „и“ и префикса, **пази числата** и затворен списък посоки. Правило: остатъкът == пълната фраза на ТОЧНО ЕДИН запис, иначе уникална СЪСЕДНА подфраза; пазач: число / посока / „sveti“ никога не квалифицира. **Областта е ИЗНЕСЕНИЯТ речник**, премерен наново преди подпис. **Типът СТЕСНЯВА само когато е изричен И съвпада с поне един кандидат.** **Двусмислието не ражда нов видим текст** (`AGENTS.md:138`) — **обявено ОТКЛОНЕНИЕ от К6**: уточнителят при двусмислие е отложен, защото иска дословен български текст от Петър (решение §6.20); днешното поведение при двусмислие се запазва и се пази от замразена заявка. **Родител ⊃ дете живее в ИЗНОСА** (per-code `type` и `parents` по КОДОВЕ); затворените списъци → `_meta` до `zone_generic_words` (`build_place_categories.py:566`), fail-closed. **Паритет:** `window.__places.locationKey(q)` влиза в корпуса `probe_out/token_parity.json` (**759 низа**, М0.18). **11 подписани вектора** + проби съюз, точкувана форма, число, посока, двусмислие, йерархия. Манифест по `bundle:ordinal` („РОЯЛ“ ×2; `release.compare()` сравнява по име, `gates/release.py:780-823`). **Смяна на КЛОН при непроменени редове = делта от първи ред.**
61: 
62: **D13 · Атомност през ТРИ репа (S5/S6).** Един комит през две репа не съществува. **Подредената тройка важи за ДАННИТЕ, не за инструмента:** инструментът (Г1) и гейтовете му са предпоставка и стоят извън тройката. Тройката е: **(1) Varna_buildings** — записът, `parents`, преподписаната константа (D14); **(2) varna_3d** — резолверът, двата износни гейта (`qa_fire_varna_export.py:191`, `qa_fire_varna_places_export.py:323`), вторият препис (`qa_fire_varna_m6.py:58-64`), износът; **(3) Fire_Varna** — **блобовете влизат в СЪЩИЯ комит със затворените списъци**: `QUARTER_SRC` (`index.html:6313`), `QUARTER_CODES` (`:6317`), `LOCALITY_CODES` (`:6322`), трите SHA пина (`:6288-6290`), `LEGACY_BUNDLE_SHA` (`:6301`), `PLACES_CACHE` v6 → **v7** (`:6265`), и поименно пиновете на двата теста: `PLACES_SHA256`/`BYTES` 122089/`GZIP9` 13728, `HOTELS_*` 148685/13084, `CATEGORIES_*` 75818/9104, `QUARTER_BY_SRC` (точно равенство), `QUARTER_CODES`, `LOCALITY_CODES`, `LOCATION_COUNTS` {quarter 20, district 5, locality 5}, `LEGACY_ROWS` 18, `LOCALITY_COUNT`; плюс baseline → `fd13907` (`signed_by: "pending — Петър"`) и подмяната на allow-файла. Числата се ПРЕМЕРВАТ след чертането. Тихата смърт, доказана: непознат `src` → `validLocation` false (`:6528-6534`) → `validTypedLocation` (`:6535-6541`) → `validatePlaces2` (`:6569-6576`) → `null` → `places2 = []`, хотелите остават (`:6627-6640`) — **150 места изчезват мълчаливо**; `accept` сверява SHA само при `crypto.subtle` (`:6605`) → кешът задължително на v7. **Манифестите са ТРИ** (`gates/release.py:157-159`): `lot1v_v_manifest_BASE_P7.json` = дифът на ДАННИТЕ (P7→P8 по `place_id`), `lot1v_v_manifest_P7_F12.json` = дифът на ПОВЕДЕНИЕТО, `lot1v_v_reference_manifest.json` = манифестът на референцията; и трите се преизползват в съществуващите слотове с `_meta.what` и изричен ред „името е остаряло“. Имената живеят на **ПЕТ ръчни места**: `gates/release.py:157-159`, `:175-183`, `manifest_anchor_gate.py:42-44`, `recall_sweep.py:3070-3071`, `recall_sweep.py:2661`. **Замразените тела са ТРИ** (амандамент №11 т. 4): референцията `recall_sweep_rows.json` (вързана през `expectations._meta.reference`), `expectations.json`, и паритетният корпус `probe_out/token_parity.json`, който **днес не е вързан от нищо** и влиза в `expectations._meta.inputs`.
63: 
64: **D14 · Регистърът е подписано тяло (S5).** `Varna_buildings/js/lib_quarter_registry.mjs:35` заключва `schema_version`, `id`, `display`, `kind`, `aliases`, `parents`; `:45` държи `REGISTRY_SIGNED_SHA256`; `:121-127` хвърля „never patch the constant to make a build pass“. Затова: (1) промяната е **СОБСТВЕН датиран план в Varna_buildings със собствен §7 (дефиниция за готово)**, минаващ през неговите Approval gates (`AGENTS.md:273-275`) **и през Кими и Astra** (§0.3), чиято присъда влиза в **собствен амандамент — нов датиран файл** в същата папка; (2) константата се преизчислява и **подписва от Петър, в негов комит**, заедно с данните; (3) `node js/test_quarter_registry.mjs` тича в кръга (G5); (4) **агент никога не пипа константата**. Преди комита: нула съвпадения на новото име в 449 `quar` + 19 813 `addr` и нула сблъсък на `match_key` (М0.14); след комита `qa_fire_varna_location_isolation.py` зелено (G6/G10) — `place_zones._registry:252-255` индексира БЕЗ вид.
65: 

codex
Node-срезът действително включва валидаторите и се изпълнява. Пробата в паметта даде `places payload unavailable` и 0 реда при стария `QUARTER_SRC`, вместо обещаните 225. Намерихме и риск от фалшиво зелен G7: двата прогона пишат в един и същ временен файл. Междувременно друг процес комитна плана като `e6ba50e`; продължавам проверката на v2.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
const fs=require('fs'),cp=require('child_process'),crypto=require('crypto');const plan=fs.readFileSync('docs/plans/ПЛАН_Б3_07.09.md','utf8').split(/\\r?\\n/);let s=fs.readFileSync('index.html','utf8').split(/\\r?\\n/).slice(6255,7154).join('\\n')+'\\n';const read=p=>JSON.parse(cp.execFileSync('git',['-c','safe.directory=C:/git/varna_3d','-C','C:/git/varna_3d','show','05f485e:'+p],{encoding:'utf8'}));const p=read('data/fire_varna_places.json'),h=read('data/fire_varna_hotels.json'),c=read('data/place_categories.json');s=s.replace(\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE'];\",\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE','SIGNED_POLYGON','DISTRICT_FALLBACK'];\").replace(/const QUARTER_CODES = \\[[\\s\\S]*?\\];/,'const QUARTER_CODES = '+JSON.stringify(Object.keys(c.locations.quarter))+';');s+=plan.slice(270,289).join('\\n')+'\\n';s=s.replace(\"if (CADASTRAL.test(text)) return false;\",\"if (CADASTRAL.test(text)) return false;\\nif(Object.keys(d._meta).length"'!==META_KEYS_PLACES||!validQuarterAttribution(d._meta,d.places))return false;");s+='"'return {validatePlaces2,validQuarterAttribution};';const api=new Function('window','caches','document','map','fetch',s)({},undefined,{}, {},()=>{throw Error('network forbidden')});console.log('meta original keys:',Object.keys(p._meta));console.log('baseline validate:',api.validatePlaces2(p,JSON.stringify(p)));p._meta.unexpected=p._meta.schema;delete p._meta.schema;console.log('same-count schema removed + unexpected key:',Object.keys(p._meta).length,api.validatePlaces2(p,JSON.stringify(p)));let q=structuredClone(p);q._meta.quarter_attribution[Object.keys(q._meta.quarter_attribution)[0]].src='made_up_source';q._meta.quarter_attribution[Object.keys(q._meta.quarter_attribution)[0]].url='http://example.com/1/';console.log('foreign provenance+url:',api.validatePlaces2(q,JSON.stringify(q)));
'@ | node" in C:\git\Fire_Varna
 exited 1 in 23ms:
node:fs:441
    return binding.readFileUtf8(path, stringToFlags(options.flag));
                   ^

Error: ENOENT: no such file or directory, open 'C:\git\Fire_Varna\docs\plans\????_?3_07.09.md'
    at Object.readFileSync (node:fs:441:20)
    at [stdin]:1:91
    at runScriptInThisContext (node:internal/vm:209:10)
    at node:internal/process/execution:446:12
    at [stdin]-wrapper:6:24
    at runScriptInContext (node:internal/process/execution:444:60)
    at evalFunction (node:internal/process/execution:279:30)
    at evalTypeScript (node:internal/process/execution:291:3)
    at node:internal/main/eval_stdin:53:5
    at Socket.<anonymous> (node:internal/process/execution:201:5) {
  errno: -4058,
  code: 'ENOENT',
  syscall: 'open',
  path: 'C:\\git\\Fire_Varna\\docs\\plans\\????_?3_07.09.md'
}

Node.js v22.19.0

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/decisions/010_signed_quarter_boundaries.md' -Encoding UTF8 | Select-Object -Skip 59 -First 3 | ForEach-Object -Begin { "'$n=59 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 25ms:
60: **D12 · Търсенето (клас B) — К6 + S4.** Идемпотентен `location_key(toks) -> (type, phrase)`, приложен ИДЕНТИЧНО върху индекса и остатъка, дефиниран върху **СПИСЪК ОТ ТОКЕНИ**. Типовият префикс е поредица с двете си арности. Хвърля съюза „и“ и префикса, **пази числата** и затворен списък посоки. Правило: остатъкът == пълната фраза на ТОЧНО ЕДИН запис, иначе уникална СЪСЕДНА подфраза; пазач: число / посока / „sveti“ никога не квалифицира. **Областта е ИЗНЕСЕНИЯТ речник**, премерен наново преди подпис. **Типът СТЕСНЯВА само когато е изричен И съвпада с поне един кандидат.** **Двусмислието не ражда нов видим текст** (`AGENTS.md:138`) — **обявено ОТКЛОНЕНИЕ от К6**: уточнителят при двусмислие е отложен, защото иска дословен български текст от Петър (решение §6.20); днешното поведение при двусмислие се запазва и се пази от замразена заявка. **Родител ⊃ дете живее в ИЗНОСА** (per-code `type` и `parents` по КОДОВЕ); затворените списъци → `_meta` до `zone_generic_words` (`build_place_categories.py:566`), fail-closed. **Паритет:** `window.__places.locationKey(q)` влиза в корпуса `probe_out/token_parity.json` (**759 низа**, М0.18). **11 подписани вектора** + проби съюз, точкувана форма, число, посока, двусмислие, йерархия. Манифест по `bundle:ordinal` („РОЯЛ“ ×2; `release.compare()` сравнява по име, `gates/release.py:780-823`). **Смяна на КЛОН при непроменени редове = делта от първи ред.**
61: 
62: **D13 · Атомност през ТРИ репа (S5/S6).** Един комит през две репа не съществува. **Подредената тройка важи за ДАННИТЕ, не за инструмента:** инструментът (Г1) и гейтовете му са предпоставка и стоят извън тройката. Тройката е: **(1) Varna_buildings** — записът, `parents`, преподписаната константа (D14); **(2) varna_3d** — резолверът, двата износни гейта (`qa_fire_varna_export.py:191`, `qa_fire_varna_places_export.py:323`), вторият препис (`qa_fire_varna_m6.py:58-64`), износът; **(3) Fire_Varna** — **блобовете влизат в СЪЩИЯ комит със затворените списъци**: `QUARTER_SRC` (`index.html:6313`), `QUARTER_CODES` (`:6317`), `LOCALITY_CODES` (`:6322`), трите SHA пина (`:6288-6290`), `LEGACY_BUNDLE_SHA` (`:6301`), `PLACES_CACHE` v6 → **v7** (`:6265`), и поименно пиновете на двата теста: `PLACES_SHA256`/`BYTES` 122089/`GZIP9` 13728, `HOTELS_*` 148685/13084, `CATEGORIES_*` 75818/9104, `QUARTER_BY_SRC` (точно равенство), `QUARTER_CODES`, `LOCALITY_CODES`, `LOCATION_COUNTS` {quarter 20, district 5, locality 5}, `LEGACY_ROWS` 18, `LOCALITY_COUNT`; плюс baseline → `fd13907` (`signed_by: "pending — Петър"`) и подмяната на allow-файла. Числата се ПРЕМЕРВАТ след чертането. Тихата смърт, доказана: непознат `src` → `validLocation` false (`:6528-6534`) → `validTypedLocation` (`:6535-6541`) → `validatePlaces2` (`:6569-6576`) → `null` → `places2 = []`, хотелите остават (`:6627-6640`) — **150 места изчезват мълчаливо**; `accept` сверява SHA само при `crypto.subtle` (`:6605`) → кешът задължително на v7. **Манифестите са ТРИ** (`gates/release.py:157-159`): `lot1v_v_manifest_BASE_P7.json` = дифът на ДАННИТЕ (P7→P8 по `place_id`), `lot1v_v_manifest_P7_F12.json` = дифът на ПОВЕДЕНИЕТО, `lot1v_v_reference_manifest.json` = манифестът на референцията; и трите се преизползват в съществуващите слотове с `_meta.what` и изричен ред „името е остаряло“. Имената живеят на **ПЕТ ръчни места**: `gates/release.py:157-159`, `:175-183`, `manifest_anchor_gate.py:42-44`, `recall_sweep.py:3070-3071`, `recall_sweep.py:2661`. **Замразените тела са ТРИ** (амандамент №11 т. 4): референцията `recall_sweep_rows.json` (вързана през `expectations._meta.reference`), `expectations.json`, и паритетният корпус `probe_out/token_parity.json`, който **днес не е вързан от нищо** и влиза в `expectations._meta.inputs`.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
const fs=require('fs'),cp=require('child_process');const path='docs/plans/\\u041f\\u041b\\u0410\\u041d_\\u04113_07.09.md';const plan=fs.readFileSync(path,'utf8').split(/\\r?\\n/);let s=fs.readFileSync('index.html','utf8').split(/\\r?\\n/).slice(6255,7154).join('\\n')+'\\n';const read=p=>JSON.parse(cp.execFileSync('git',['-c','safe.directory=C:/git/varna_3d','-C','C:/git/varna_3d','show','05f485e:'+p],{encoding:'utf8'}));const p=read('data/fire_varna_places.json'),c=read('data/place_categories.json');s=s.replace(\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE'];\",\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE','SIGNED_POLYGON','DISTRICT_FALLBACK'];\").replace(/const QUARTER_CODES = \\[[\\s\\S]*?\\];/,'const QUARTER_CODES = '+JSON.stringify(Object.keys(c.locations.quarter))+';');s+=plan.slice(270,289).join('\\n')+'\\n';s=s.replace(\"if (CADASTRAL.test(text)) return false;\",\"if (CADASTRAL.test(text)) return false;\\nif(Object.keys(d._meta).length"'!==META_KEYS_PLACES||!validQuarterAttribution(d._meta,d.places))return false;");s+='"'return {validatePlaces2,validQuarterAttribution};';const api=new Function('window','caches','document','map','fetch',s)({},undefined,{}, {},()=>{throw Error('network forbidden')});console.log('meta original keys:',Object.keys(p._meta));console.log('baseline validate:',api.validatePlaces2(p,JSON.stringify(p)));p._meta.unexpected=p._meta.schema;delete p._meta.schema;console.log('same-count schema removed + unexpected key:',Object.keys(p._meta).length,api.validatePlaces2(p,JSON.stringify(p)));let q=structuredClone(p);q._meta.quarter_attribution[Object.keys(q._meta.quarter_attribution)[0]].src='made_up_source';q._meta.quarter_attribution[Object.keys(q._meta.quarter_attribution)[0]].url='http://example.com/1/';console.log('foreign provenance+url:',api.validatePlaces2(q,JSON.stringify(q)));
'@ | node" in C:\git\Fire_Varna
 succeeded in 59ms:
meta original keys: [
  'generated',
  'count',
  'by_kind',
  'by_zone_src',
  'licence_osm',
  'licence_registry',
  'licence_wikidata',
  'licence_address',
  'quarter_attribution',
  'excluded'
]
baseline validate: true
same-count schema removed + unexpected key: 11 false
foreign provenance+url: false

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
const fs=require('fs'),cp=require('child_process');const plan=fs.readFileSync('docs/plans/\\u041f\\u041b\\u0410\\u041d_\\u04113_07.09.md','utf8').split(/\\r?\\n/);let s=fs.readFileSync('index.html','utf8').split(/\\r?\\n/).slice(6255,7154).join('\\n')+'\\n';const read=p=>JSON.parse(cp.execFileSync('git',['-c','safe.directory=C:/git/varna_3d','-C','C:/git/varna_3d','show','05f485e:'+p],{encoding:'utf8'}));const p=read('data/fire_varna_places.json'),c=read('data/place_categories.json');s=s.replace(\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE'];\",\"const QUARTER_SRC = ['REG', 'KAIS', 'SIGNED_OVERRIDE','SIGNED_POLYGON','DISTRICT_FALLBACK'];\").replace(/const QUARTER_CODES = \\[[\\s\\S]*?\\];/,'const QUARTER_CODES = '+JSON.stringify(Object.keys(c.locations.quarter))+';');s+=plan.slice(270,289).join('\\n')+'\\n';s=s.replace(\"if (CADASTRAL.test(text)) return false;\",\"if (CADASTRAL.test(text)) return false;\\nif(Object.keys(d._meta).length"'!==META_KEYS_PLACES||!validQuarterAttribution(d._meta,d.places))return false;");s+='"'return {validatePlaces2,validQuarterAttribution};';const api=new Function('window','caches','document','map','fetch',s)({},undefined,{}, {},()=>{throw Error('network forbidden')});console.log('baseline validate:',api.validatePlaces2(p,JSON.stringify(p)));p._meta.unexpected=p._meta.generated;delete p._meta.generated;console.log('same-count generated removed + unexpected key:',Object.keys(p._meta).length,api.validatePlaces2(p,JSON.stringify(p)));let q=structuredClone(p);q._meta.quarter_attribution[Object.keys(q._meta.quarter_attribution)[0]].src='made_up_source';q._meta.quarter_attribution[Object.keys(q._meta.quarter_attribution)[0]].url='http://example.com/1/';console.log('foreign provenance+url:',api.validatePlaces2(q,JSON.stringify(q)));
'@ | node" in C:\git\Fire_Varna
 succeeded in 62ms:
baseline validate: true
same-count generated removed + unexpected key: 10 true
foreign provenance+url: true

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md' -Encoding UTF8 | Select-Object -Skip 24 -First 25 | ForEach-Object -Begin { "'$n=24 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 20ms:
25: 
26: ## 4 · Нощната смяна 06→07.09 — резултат (добавено сутринта на 07.09 по часовника на машината)
27: - Планът `docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md` (v2, подписан от Петър) е изпълнен от Opus изпълнители с одитор на всеки ход: **част А 7/7 зелени**, **Б1 зелен** (`varna_3d/data/quarters_signed.geojson`, 61 граници, СТЕЙДЖНАТ за комита на Петър, sha `3f423898…`), **Б2-0 червен на G9** (основата на самоличността от 04.09 се е разместила → отделно освежаване сутринта), Б2/Б3 не са тръгвали. Докладът: `docs/audits/ДОКЛАД_07.09_нощна_смяна.md` (§6 = прегледът от три ъгъла: архитект, Кими К23, Astra S22). Първата стъпка на Петър е §6.4 на доклада.
28: 
29: - **Решения 4 (07.09, Петър, след нощта):** площта „Виница - север“ в Уикимапия е част от Добрева чешма → `dobreva` = обединението на двата полигона (1,43 km²), `vinitsa_sever` = **изключен** (регистърът го деактивира, ход Р). Файл: `scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json`; обединената геометрия в `granitsi_preview_05.09/unions_2026-09-07.geojson`. Следствие за сутринта: Б1 се пресглобява от решения 4 (строителят трябва да поддържа `wikimapia_union` с два свидетеля); нито едно от 375-те места не е в засегнатата площ. Картата на резултата вече го показва (60 граници).
30: 
31: - **Решение 8 (07.09, Петър):** в картончето на мястото НЯМА ред за извора на квартала („квартал по Wikimapia.org · обектът · потвърдено от Петър“ — „това можеш да го махнеш“). Кварталът се показва само в реда „вид · квартал · район“. Споменаването на Wikimapia отива в дребния надпис в долния край на картата (Leaflet attribution), до „© OpenStreetMap contributors“. Следствие за Б3: G27(б) се изпълнява чрез надписа на картата, не чрез ред в картончето; `quarter_attribution` остава в `_meta` (машинен запис), UI низ в картончето няма.
32: 
33: - **Решение 9 (07.09, Петър):** „Кочмар и Възраждане 4 не са във Владиславово“ → районът на двата квартал-полигона е **Младост**, както казва официалната граница на АГКК (AU5 10135-03; представителните точки са 782 m и 509 m навътре в Младост). Причина за грешката: районът на кварталите в артефакта се извежда от НАШИЯ слой с районите по представителна точка, а той се разминава с официалната граница около бул. „Трети март“. Местата не са засегнати (district.code на местата е 375/375 с АГКК). Следствие: (а) двата спора в `_meta.district_witness_disputes` получават `resolution: "petar_agkk"` и `district = mladost`, `district_src = "agkk_au5_confirmed_by_petar"`; (б) мярка сутринта: нашият слой с районите срещу AU5 по цялата граница Владиславово/Младост (и петте граници) — къде още се разминават; (в) сградната мярка Н4 „само район“ да ползва AU5, не нашия слой.
34: 
35: - **Мярка 07.09 (архитект): нашият слой с районите (m6000_private/number_viewer/quarters_layer.geojson, authority OSM) срещу официалните пет района на АГКК (AU5):** Приморски IoU 0,995 (0,24 km² разминаване) · Аспарухово 0,960 (2,74 km²: петно 137 ha „наш излишък“ при 43,1815 N 27,9165 E, 82 ha „липсва при нас“ при 43,1968 N 27,9001 E — зоната на пристанището/езерото между Аспарухово и Одесос) · Одесос 0,799 (1,36 km²) · **Владиславово 0,790 (4,54 km²: 404 ha наш излишък при 43,2463 N 27,8804 E — точно зоната на Кочмар и Възраждане 4, която АГКК дава на Младост)** · **Младост 0,692 (4,17 km²)**. Изводът: OSM-слоят с районите не е годен за районна граница; официалният е AU5. Кочмар и Възраждане 4: наш слой → Владиславово, АГКК → Младост (решение 9 на Петър съвпада с АГКК). **Предложение за решение 10:** районът на квартал-полигоните да се извежда от AU5 (официално, с подписан crosswalk 10135-0N → словесен код), а OSM-слоят с районите да отпадне като извор за район навсякъде (3D картата: дълг).
36: 
37: - **Мярка 07.09 (архитект) за решение 10:** представителните точки на 60-те граници срещу AU5 и срещу нашия OSM слой: **57 съгласни, точно 2 флипа (Кочмар, Възраждане 4 — вече решени по решение 9), 1 извън всичките пет района на АГКК: с.о. Перчемлията** (не е и в нашия слой). Следствие: гейтът на решение 10 „60/60 в AU5“ иска поименен, подписан резерв за Перчемлията (район Приморски по регистъра/адресите, `district_src: "registry_declared"`), иначе е червен. Други флипове край пристанището/Одесос НЯМА при днешните полигони.
38: 
39: - **Б1 ЗАТВОРЕН (07.09):** Петър комитна `varna_3d/data/quarters_signed.geojson` — **6486b48 (Petar1984)**, „data: signed quarter boundaries v1 (decisions 4, sha 74f09d505e2b)“, с подписното изречение в тялото (решения 4 блоб 74f09d50…, решение 9 d494d4d2…, AU5 crosswalk, артефакт c1551d24…, 60 граници, 301 917 B). Предхождащи изпълнителски комити: 63d077d, 8c262e9, 6dde0a5, 7fb0e92, e2da307 (varna_3d); 3d747d3, e6c706d (Fire_Varna). Прегледи: Кими К24/К25, Astra S23/S24 (записите в scratch/places_search/). Дребни дългове: `ours` в решен спор не се сверява (false-pass), семантиката на `counts.features_with_our_district`, закованият sha на resolutions; `vinitsa_sever` нормализаторен път в регистъра; решение 10 (район от AU5 навсякъде; Перчемлията извън AU5 → подписан резерв) чака Петър.
40: 
41: ## 5 · Б2 (07.09, Workflow granitsi-b2) — резултат
42: - **Б2-0а (освежаване на основата на самоличностите): ЗЕЛЕН, одит ГОДНО** — 77 реда (72 хотела + 5 места) с променени `zone`/`key`, произходът доказан 1:1 срещу комит e613089 от 05.09; 0 нови/изчезнали place_id; гейт `src/qa_identity_refresh.py` (varna_3d 3de6661). Заварената червена мярка `qa_place_sites.py` става зелена.
43: - **Б2-0 (координати от кадастралните тела, Б0 т. 11): ЗЕЛЕН, одит ГОДНО** — 375/375 с координата, 0 без; G9 срещу освежената основа само в четирите координатни ключа; генераторът + гейт (varna_3d 5c6fdd0). `data/place_identity.json` е **СТЕЙДЖНАТ** (sha `1141bbc2…`) за комита на Петър — но виж дълга за пина по-долу.
44: - **Б2 (присвояване P8-а): изпълнител зелен, одитори НЕГОДНО (2 блокера, 2 major)** — числата съвпадат с нощната мярка (written 201; assigned_polygon 65; edge 63; pin_outside_all 41; disputed_overlap 5; SIGNED_POLYGON пише 57: 42 места + 15 хотела; DISTRICT_FALLBACK 0), леджерът на конфликтите е произведен (286/33/49/7). **Блокер 1:** ключът на самоличността е `file|skeleton|zone` (`src/place_identity.py:207,222`) — присвояването сменя `zone` на 57 реда и **57 места губят place_id**; генераторът пада (2 реда „оттеглени без решение“). Това е дефект на дизайна на D10 (зоната е част от ключа), открит от гейта, не от кода на лота. **Major 2:** `qa_place_zone_aliases.py` 0 → 1: три доставени зони липсват в речника на търсенето (Гръцката махала, Долна Трака, Колхозен пазар), `place_categories.json` не е прегенериран, `legacy_bundle_sha` сочи стария износ. **Major 3:** `qa_fire_varna_m6.py` чете стария леджер (write-set-ът „QA/M6“ не е изпълнен); новият леджер не спазва буквата на D6 за свидетеля. Комитите с код (da77ff2, 0ecd814) остават — с данните на HEAD всички гейтове са зелени (проверено от архитекта).
45: - **Паркиране (архитект):** четирите изхода са копирани в `scratchpad/b2_outputs_2026-09-07/` (places 89e60d2e…, hotels b4f1f0bb…, inputs c06b93ab…, леджер fba94bf8…), махнати от индекса и работното дърво (HEAD износите върнати: 329310f5…, 46a44ce8…); стейджнат остава само `data/place_identity.json`. Гейтове след паркирането: `qa_place_zone_aliases` 0, пълният набор OK.
46: - **Дълг за пина:** `data/fire_varna_location_inputs.json` пинва старата самоличност (e8b4c836…), а стейджнатата е 1141bbc2… — никой гейт не го лови (`_check_pins` сверява само NTR/M6). Пинът се пренаписва в Б2; до тогава комитът на самоличността носи застоял пин. Препоръка: самоличността остава стейджната до Б2-повторението.
47: - **Следва:** амандамент №3 (малък): ключ на самоличността без зоната (или ре-закотвяне при смяна на зона), прегенериране на `place_categories.json` и речника на зоните (alias-и за трите нови имена), `qa_fire_varna_m6.py` към новия леджер, D6-формата на свидетеля; оборване (Opus → Кими/Astra) → подпис → Б2 повторение.
48: 
49: - **Находка (одитор Б2-R1-fix, 07.09):** проследеният `varna_3d/scratch/place_bodies/qa_place_bodies.md` (заварен мръсен преди нощта, пинат sha 51b0f4d9…) е бил ПРЕЗАПИСАН от прекратения първи прогон на Б2 (07.09 02:25; сега sha 2633e165…, 153 разменени реда със зоните на онзи прогон). Файлът е генериран QA-отчет (колона „зона“); предишното мръсно съдържание няма копие никъде. Архитектът НЕ го пипа: след успешния Б2 отчетът се прегенерира от актуалните данни и разликата спрямо HEAD ще е легитимна; решението (прегенерирай / върни HEAD) е на Петър при Gate 2.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 200 '"'^##|''^###'"' 'docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md' 'docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md'" in C:\git\Fire_Varna
 succeeded in 0ms:
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:5:## 1 · Какво имаме
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:12:## 2 · Защо ни бяха кварталите (замисълът от `ПРОМПТ_нова_тема_Границите.md` и `ПЛАН_ЛОТ_Границите.md`)
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:15:## 3 · Как продължаваме (редът от амандамент №2, ревизия 2б)
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:26:## 4 · Нощната смяна 06→07.09 — резултат (добавено сутринта на 07.09 по часовника на машината)
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:41:## 5 · Б2 (07.09, Workflow granitsi-b2) — резултат
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:51:## 6 · Б2 ПОВТОРЕНИЕ по амандамент №3 — ЗЕЛЕНО (07.09, Workflow granitsi-b2-rerun-3)
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:58:## 7 · Външен преглед на Б2 (07.09 сутрин) — К27 ГОДНО, S26 НЕГОДНО → поправено
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:65:## 8 · Б2 ЗАТВОРЕН — комитите на Петър (07.09) · Б3 в планиране
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:8:## 1 · Мярката (read-only, 07.09)
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:20:## 2 · Двата пътя и присъдата
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:28:## 3 · Write-set и дословни съобщения (varna_3d, автор `Claude Executor <executor@local>`)
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:42:## 4 · Ред на изпълнение
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:51:## 5 · Гейтове и отрицателни фикстури (всяка ТРЯБВА да падне)
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:63:## 6 · Комитите на Петър, в този ред
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:69:## 7 · STOP
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:74:## 8 · Решенията за Петър
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:88:## 9 · Оборване — Кими К26 (леща данни/самоличност), приложено като условия на амандамента
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:96:## 10 · Оборване — Astra S25 (леща механика), приложено като задължителни условия
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:107:## 11 · Статус

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath index.html -Encoding UTF8 | Select-Object -Skip 7249 -First 42 | ForEach-Object -Begin { $n=7249 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 70ms:
7250:     }
7251: 
7252:     // ---- Д7/В1: the selection — their slot cleared through their PUBLIC contract
7253:     function popupFor(h) {
7254:       const wrap = document.createElement('div');
7255:       wrap.className = 'place-popup';
7256:       wrap.appendChild(span('pp-title', h.name + (h.status === 'бивш' ? ' (бивш)' : '')));
7257:       const bits = [h.kind];                     // С3: cat/beds ride the hotels only
7258:       if (h.cat && h.cat.length) bits.push('★' + h.cat.join('/'));
7259:       if (h.beds && h.beds.length) bits.push(h.beds.join('+') + ' легла');
7260:       // ЛОТ 1в-В (план §3г т. 5 + К6 (5)): „вид · кв. X · район Y · доп.: Z“. Every
7261:       // part is NULL-SAFE — a record with no quarter simply has no quarter part and
7262:       // no empty separator, the district always carries its marker („район“), and a
7263:       // district that reads exactly like the quarter is printed once. Until this lot
7264:       // the card said one `zone` string and a drawn hull could speak as a quarter.
7265:       const district = h.district ? DISTRICT_MARK + ' ' + h.district.name : '';
7266:       const quarter = h.quarter ? h.quarter.name : '';
7267:       if (quarter) bits.push(quarter);
7268:       if (district && district !== quarter) bits.push(district);
7269:       if (!quarter && !district) bits.push(h.zone);        // compat: a pre-D9 payload
7270:       if (h.locality) bits.push('доп.: ' + h.locality.name);
7271:       wrap.appendChild(span('pp-sub', bits.join(' · ')));
7272:       // ЛОТ 1в-Б (ADR 008 D5, план §2 т. 2): the address stands under „вид · зона“ and
7273:       // names the source of THAT string, not the record's. 185 of the 375 have none —
7274:       // then there is no line at all and the zone above stays the honest answer.
7275:       if (h.address && ADDR_SRC_LINE[h.address.src])
7276:         wrap.appendChild(span('pp-addr', 'адрес: ' + h.address.text + ' · ' + ADDR_SRC_LINE[h.address.src]));
7277:       if (h.old_names.length) wrap.appendChild(span('pp-old', 'старо име: ' + h.old_names.join(', ')));
7278:       // ADR 008 D3: when the row was found through an OLD name, the source line of
7279:       // that STRING is the one that is true — until ЛОТ 1в the card printed the
7280:       // record's register for an OSM string it never came from.
7281:       const ai = (h === lastPick) ? lastAliasI : -1;
7282:       const acode = (ai >= 0 && Array.isArray(h.old_names_src)) ? h.old_names_src[ai] : null;
7283:       if (acode && ALIAS_SRC_LINE[acode])
7284:         wrap.appendChild(span('pp-old-src', 'извор на „' + h.old_names[ai] + '“: ' + ALIAS_SRC_LINE[acode]));
7285:       wrap.appendChild(span('pp-src', SRC_LINE[h.src]));
7286:       const nav = buildNavActions(h.lat, h.lon);
7287:       if (nav) wrap.appendChild(nav);
7288:       return wrap;
7289:     }
7290:     function openPlacePopup(h) {
7291:       // С4: the self-restore is GONE. Leaflet has no "closed by a human" mark, so

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md' -Encoding UTF8 | Select-Object -Skip 50 -First 27 | ForEach-Object -Begin { "'$n=50 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 23ms:
51: ## 6 · Б2 ПОВТОРЕНИЕ по амандамент №3 — ЗЕЛЕНО (07.09, Workflow granitsi-b2-rerun-3)
52: - **Б2-R1** (прекодиране): varna_3d a28edc2 (ключ без зоната), 8a60972, 7bac5e5, bb09535 (`--accept-identity`), 4bdcc7c (харнеси, utf-8), 36e8513 (замразената основа като фикстура `tests/fixtures/identity_rekey_base_2026-09-07.json`, доказано от чисто дърво). 375/375 place_id непроменени.
53: - **Б2-R2** (присвояване): 679451d (свидетели в леджера, A6), 2624218 (M6 с изричен леджер), 822656d (неподвижна точка, A3), bd00c2c (подписан alias override, решение 5), 0c1ed71 (речник: 60 кода + 5 района + Перчемлията, П2), 26da605 (П4 в qa_p8a). Архитектът: `.gitignore` изключение за `data/zone_alias_overrides.json` (major на общия одит).
54: - **Числата:** таблица 201 written / 41 pin_outside_all / 63 edge_pending / 5 disputed_overlap / 65 assigned_polygon / 0 assigned_district = 375; SIGNED_POLYGON пише 57 (всичките върху празни записани квартали, П4); G17 201/201; неподвижна точка: места, хотели, леджер байт-еднакви; M6 fails 0, exit 3 с точно осемте pending; речник: 32 доставени зони, 28 съвпадат, 4 „unmatched“ (за преглед), override „Виница-север“ приложен 0 пъти (няма доставена такава зона — очаквано).
55: - **СТЕЙДЖНАТИ за Петър (7 файла):** place_identity 4819ab3e… · fire_varna_location_inputs c7450ded… · fire_varna_places 3dffc264… · fire_varna_hotels eb8fa85c… · place_categories 9064705a… · registry_manifest bb04640e… (решение 6: 9 реда със сменена зонова дума) · леджер lot1v_locations_375_p8a_07.09 5ec64c68…. Одити: R1-fixture ГОДНО, R2 ГОДНО, общ ГОДНО (2 major: .gitignore — поправен; манифестът не е байт-еднакъв — очаквано по решение 6, 9 реда).
56: - **Следва:** Кими/Astra преглед → трите комита на Петър (§6 на амандамента) → Б3 → локален преглед → пуш.
57: 
58: ## 7 · Външен преглед на Б2 (07.09 сутрин) — К27 ГОДНО, S26 НЕГОДНО → поправено
59: - **Кими К27 (данни): ГОДНО** с четири проверки за Петър, отговорени с мярка: (1) четирите „unmatched“ зони са **петте районни думи** (район Аспарухово · Младост · Одесос · Приморски), покрити от районната книга на речника (гейт (f)); (2) осемте присвоени-но-неписани реда: 4 с местностен победител (Джоя → zelenika, Дива → alen_mak/DROP, Казабланка Грийн → sveti_nikola, Людо → zelenika — местност никога не пълни quarter) + 4 pending_signature (МАГНОЛИЯ 1 И 2, РУСАЛКА, СТРАНДЖА → chaika_kk; Романтика → fichoza) — поименно в леджера; (3) деветте реда на манифеста: 3 grandfathered (Военно-морска болница → кв. Изгрев 148 m навътре; ИУ 2-ри корпус → кв. Левски 299 m; ТУ → кв. Левски 116 m) + 6 board_queue (II ДКЦ → кв. Аспарухово 316 m; 3 ОУ Ангел Кънчев → кв. Левски 258 m; Морска гимназия → кв. Аспарухово 111 m; ОУ Славейков → кв. Тракия 138 m; ПТГ → ж.к. Победа 204 m, `pobeda` Е сред 60-те подписани; ПГ Менделеев → ж.к. Бриз 150 m) — всичките по SIGNED_POLYGON, всеки пин над 100 m от ръба; (4) alias „Виница-север → dobreva“ е в `place_categories.json` като подписана, видима, неприложена таблица (0 доставени зони с тази дума); 23-те кадастрални адреса са регистров ред (сутрешният списък), не износ.
60: - **Astra S26 (механика): НЕГОДНО за комит с три условия** — (1) `qa_fixed_point.py` нормализираше JSON и без `--ignore` → false pass срещу A3 при различни сурови байтове и еднакъв JSON; (2) unittest наборът непотвърден в нейното read-only копие; (3) комит-текстовете 2 и 3 бяха парафрази на §6. **Поправено:** (1) varna_3d **0ba2e9d** (Claude Executor): без `--ignore` = сурови байтове, с `--ignore` = нормализацията на A3 само за назованите ключове; секция 5 в `fixed_point_negatives.py` (леджер indent=2 → червено, леджер CRLF → червено, местата indent=2 с --ignore → зелено) — false pass-ът възпроизведен на HEAD~1 (exit 0) и затворен (exit 1); трите реални сравнения 0/0/0 (леджер сурово 965 388 B); (2) `python -B -m unittest discover -s tests` в главната сесия: **Ran 16 tests · OK**, нула променени проследени файлове; (3) трите `COMMIT_MSG_b2_*.txt` пренаписани: subject дословно по §6 (ред 63–68), комит 1 с реда за 57-те зони + манифеста (A7), тялото = подписните sha. Записите: Fire_Varna e4303f6 (К27 + S26).
61: - **Стейджнатите 7 блоба непокътнати** след поправката (4819ab3e · c7450ded · 3dffc264 · eb8fa85c · 9064705a · bb04640e · 5ec64c68). Дълг за следващ планер (изпълнителят, необхванато): при разлика само в отстъпа `first_difference` печата два еднакви реда (присъдата е вярна, доказателството нямо); хотелският износ в работното дърво е с CRLF (158 850 B) срещу LF блоб (151 263 B) — git го нормализира, сравнява се само през `--ignore`.
62: - **Одит на 0ba2e9d (Opus, read-only): ГОДНО** — два файла, автор и committer изпълнителят, суров режим без `--ignore` доказан (CRLF пробата пада), 10/10 фикстури с изход 1 (не 2), трите сверки 0/0/0, пресечно множество с товара празно, нула команди навън. Три дълга за закаляване (преди следващата доставка, не преди този комит): **P1** `--ignore` с ключ, който липсва и в двата документа, включва нормализацията и връща 0 (трябва изход 2; `qa_fixed_point.py:111-116`); **P2** `expect()` в стенда брои всеки ненулев изход за червено (крах ≠ присъда); **P3** `first_difference` strip-ва разликата при друг indent (козметика). **Astra S27: ГОДНО за трите комита** — 0ba2e9d измерен, секция 5 = 1/1/0, сверките 0/0/0, 7/7 блоба, комит-текстовете дословно по §6. Записи: Fire_Varna 99c8624.
63: - **Следва:** трите комита на Петър (§6, `git commit -F scratch/granitsi/COMMIT_MSG_b2_*.txt -- <пътища>`, проверка по OID с `git ls-tree HEAD`) → Б3 в Fire_Varna → локален преглед (`python -m http.server 8000`) → неговите публикувания. Отворени за Петър: `qa_place_bodies.md` (мръсен проследен отчет с новите зони — прегенерирай или върни HEAD, не мълчаливо), решение 10 (AU5 районите), сутрешният регистров списък.
64: 
65: ## 8 · Б2 ЗАТВОРЕН — комитите на Петър (07.09) · Б3 в планиране
66: - **varna_3d (Petar1984):** c1bb9dc „data: place coordinates from KAIS bodies (Б0 т. 11) and identity re-keyed without the zone (375 place_id unchanged), inputs pinned“ (identity + inputs + manifest) · d17de0d „data: places and hotels with quarter by signed polygon, search dictionary regenerated“ · 05f485e „data: p8a quarter assignment ledger 07.09“. OID-ите на седемте блоба в HEAD съвпадат 7/7 с индекса преди комита (identity 9799654836fb · inputs cf1025fc834b · manifest 5934f07f91cf · places 89c00b2219e1 · hotels 35002c1d186e · categories 283d9f33bf5e · леджер a0e31fec3b0b). Мръсен остава само `scratch/place_bodies/qa_place_bodies.md` (решение на Петър).
67: - **Б3 (търсене по квартал, Fire_Varna):** нощта не е подготвила кръпката (Б2/Б3 не тръгнаха); решение 8 сменя подписания текст (без ред за атрибуция в картончето, Wikimapia в надписа на картата). Тръгва планиращ workflow `granitsi-b3-plan` (5 разузнавачи → планер → 3 оборители → синтез, Opus, read-only) → `docs/plans/ПЛАН_Б3_07.09.md` → Кими/Astra → подпис на Петър → изпълнение с изпълнител+одитор → локален преглед на http://localhost:8000 → неговите публикувания.
68: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md' -Encoding UTF8 | Select-Object -Skip 62 -First 12 | ForEach-Object -Begin { "'$n=62 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 27ms:
63: ## 6 · Комитите на Петър, в този ред
64: 
65: 1. `data/place_identity.json` + `data/fire_varna_location_inputs.json` — `data: place coordinates from KAIS bodies (Б0 т. 11) and identity re-keyed without the zone (375 place_id unchanged), inputs pinned` (файлът носи ДВА товара: 1664/164 реда, от които 375-те координати на Б2-0)
66: 2. `data/fire_varna_places.json`, `data/fire_varna_hotels.json`, `data/place_categories.json` — `data: places and hotels with quarter by signed polygon, search dictionary regenerated`
67: 3. новият леджер — `data: p8a quarter assignment ledger 07.09`
68: 
69: ## 7 · STOP
70: 
71: Лотът спира и пита Петър при: сирак след прекодирането (поименно) · неподвижната точка различна извън `_meta.generated` · G17 показва променен написан квартал · зона без регистров запис след прегенерирането · опит да се впише ред в `RENAMES`/`MERGES` · комит на данни от агент · зелен гейт без доказано падаща отрицателна фикстура · `--inputs` без `--accept-identity`.
72: **Не е червен гейт, а грешка на оператора:** `qa_place_identity_coords.py` (G9) съди лот Б2-0 и по конструкция забранява смяна на `key`/`zone` — в този лот НЕ се пуска.
73: 
74: ## 8 · Решенията за Петър

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath index.html -Encoding UTF8 | Select-Object -Skip 6738 -First 52 | ForEach-Object -Begin { $n=6738 } -Process { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 64ms:
6739:           const out = placeTokens(field.name).map((t) => t.s);
6740:           const entry = LOC_INDEX.get(cls).get(field.code);
6741:           for (const t of (entry ? entry.extra : []))
6742:             if (out.indexOf(t.s) < 0 && !ntk.some((v) => quality(t, v) > 0)) out.push(t.s);
6743:           return out;
6744:         };
6745:         const locPhrases = (cls, field) => {
6746:           const entry = field ? LOC_INDEX.get(cls).get(field.code) : null;
6747:           return entry ? entry.phrases : new Set();
6748:         };
6749:         const qtk = locTokens('quarter', h.quarter), ltk = locTokens('locality', h.locality);
6750:         const legacy = legacyRows[bundle + ':' + ordinal];
6751:         const legtk = [], gph = new Set();
6752:         for (const word of (Array.isArray(legacy) ? legacy : [])) {
6753:           if (typeof word !== 'string') continue;
6754:           const tk = sigTokens(word);
6755:           if (!tk.length) continue;
6756:           const forms = [tk.join(' ')];
6757:           for (const pair of (legacyLookup.get(tk.join(' ')) || []))
6758:             for (const form of LOC_INDEX.get(pair[0]).get(pair[1]).phrases) forms.push(form);
6759:           for (const form of forms) {
6760:             gph.add(form);
6761:             for (const t of form.split(' ')) if (legtk.indexOf(t) < 0) legtk.push(t);
6762:           }
6763:         }
6764:         // А6 + ЛОТ 1в амандамент А4 т. 1: old names are name tokens minus the noise
6765:         // AND minus the generic GEOGRAPHIC words — „Висше военноморско училище,
6766:         // Варна“ must not answer for the whole city on „варна“. The CLASS words
6767:         // STAY: measured, without „училище“ the ВВМУ falls to second on
6768:         // „военноморско училище“ behind „Спортно училище Георги Бенковски“.
6769:         const aset = new Set(), atk = [];
6770:         for (const old of h.old_names) {
6771:           const one = new Set();
6772:           for (const t of placeTokens(old))
6773:             if (!t.num && t.orig.length > 2 && ADDR.indexOf(t.orig) < 0
6774:                 && !ALIAS_GENERIC.has(t.s)) { aset.add(t.s); one.add(t.s); }
6775:           atk.push(one);
6776:         }
6777:         // ЛОТ 1в-Б (ADR 008 D6, план §2г S4): the ORDERED street phrase and the
6778:         // house number as the DELIVERY wrote them — never parsed out of `text`
6779:         // here. They stand OUTSIDE nset/aset/zkset/significant/A5, so A4's token
6780:         // priorities and the location path can neither see them nor move them.
6781:         const addr = h.address || null;
6782:         const qph = locPhrases('quarter', h.quarter), lph = locPhrases('locality', h.locality);
6783:         return { e: h, bundle: bundle, ordinal: ordinal,
6784:                  ntk: ntk, ktk: ktk, nset: new Set(ntk), aset: aset, atk: atk,
6785:                  kkey: ktk.join(' '),
6786:                  // М7 (план §3й-б S4): the three token sets STAY APART. `zkset`
6787:                  // below is their union plus the kind, and a union cannot say
6788:                  // whether „зпз“ arrived as today's locality or as a row's old
6789:                  // word — М7 needs exactly that difference, so it reads these.
6790:                  qtk: qtk, ltk: ltk, legtk: legtk,

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git diff --stat f00dd78 e6ba50e' in C:\git\Fire_Varna
 succeeded in 0ms:
 docs/plans/ПЛАН_Б3_07.09.md | 632 ++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 632 insertions(+)

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
