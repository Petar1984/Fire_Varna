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
session id: 01a07dfc-5989-7412-8ea2-58f03adffa62
--------
user
S34 · Оборване на ПЛАН „Адресите по полигон“ v2 (леща ДОСТАВКА и УПРАВЛЕНИЕ), read-only. Файл: C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md (v2, f745349). Контекст: три репа — C:/git/Varna_buildings (генератори, config/quarter_registry.json НЕ се пипа), C:/git/varna_3d (частните полигони 05f485e), C:/git/Fire_Varna (публично; Б3 е СТЕЙДЖНАТ и некомитнат — git diff --cached, 14 пътя; Петър: „не искам да комитвам когато е грешно“, „няма да трупаме грешки“). ADR-и: docs/decisions/006_places_in_search.md (D12 Accepted: адресният път недосегаем), 007_address_path_v2.md (Proposed, неподписан), 010_signed_quarter_boundaries.md; гейтът на доставката gates/run_gates.py, gates/release.py, gates/sign.py, gates/coverage.py, scripts/hooks/pre-push; ADR 003 (dual-Claude governance) и AGENTS.md на трите репа. Атакувай: (1) Р0/Р0-б и предложения ADR 064 — правилно ли е разчетено, че ADR 006 D12 забранява лота и че 007 трябва да се подпише + разшири; минималният управленски път; kill switch-ът; (2) §5 редът на комитите през трите репа и „една публикация“ с висящия Б3 (Б3 пръв от ръката на Петър; index.html в двата write-set-а; опашка/allow/freeze/release — има ли междинно състояние с несъответстващи пинове и данни; коя опашка, колко реда, колко подписа; PowerShell командите без &&, без UTF-16 редирект); (3) идентичности (Claude Executor за код, Петър за данни/подписи), D16/G4; частният леджер — къде живее и дали не изтича кадастрални идентификатори/координати; полигонният пин по OID без копие на геометрия; (4) размерът и кешът (search_index +?, generation_id, PLACES_CACHE/fire-varna-search-* кешове, sw.js недосегаем); (5) STOP условията и §10; какво точно подписва Петър (Р0–Р18) — изброй ги в едно изречение всяко и кажи кои са излишни/сливаеми. Нищо не пипай, нищо към отдалечено хранилище. Присъда: ГОДНО за подпис / НЕГОДНО с S34-1… (доказателство + точна поправка); до 800 думи.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя плана спрямо ADR-ите, гейтовете и staged Б3, без промени и без достъп до remote. Ще разделя проверката между управление, доставка и кеш/поверителност, после ще събера конкретните блокери и поправки.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -TotalCount 130" in C:\git\Fire_Varna
 succeeded in 529ms:
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status -sb' in C:\git\Fire_Varna
 succeeded in 392ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 106]
M  data/hotels.json
M  data/place_categories.json
M  data/places.json
A  gates/probe/b3_g11.py
M  index.html
D  scratch/places_search/granitsi_fixtures_06.09.json
A  scratch/places_search/granitsi_fixtures_07.09.json
 M scratch/places_search/lot1v_v_reference_manifest.json
 M scratch/places_search/probe_out/token_parity.json
M  scratch/places_search/probe_places_fv.mjs
M  scratch/places_search/recall_sweep.py
A  tests/granitsi_client_probe.mjs
A  tests/test_b3_gates.py
M  tests/test_granitsi_fixtures.py
M  tests/test_hotels_public_bundle.py
M  tests/test_places_public_bundle.py
?? scratch/places_search/COMMIT_MSG_B3.txt
?? scratch/places_search/adresi_astra_S32_08.09.md
?? scratch/places_search/adresi_astra_S33_08.09.md
?? scratch/places_search/adresi_astra_S34_08.09.md
?? scratch/places_search/cleanup_brief_astra.md
?? scratch/places_search/cleanup_brief_kimi.md
?? scratch/places_search/golden_brief_kimi.md
?? scratch/places_search/golden_brief_sol.md
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
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$paths = @('"'AGENTS.md','docs/plans/ПЛАН_Адресите_по_полигон_08.09.md','docs/decisions/003_dual_claude_code_governance.md','docs/decisions/006_places_in_search.md','docs/decisions/007_address_path_v2.md','docs/decisions/010_signed_quarter_boundaries.md'); "'$paths | Sort-Object | ForEach-Object { if (Test-Path -LiteralPath $_) { Get-Item -LiteralPath $_ | Select-Object FullName,Length } else { '"'ABSENT '+"'$_ } }' in C:\git\Fire_Varna
 succeeded in 626ms:

FullName                                                            Length
--------                                                            ------
C:\git\Fire_Varna\AGENTS.md                                          27909
C:\git\Fire_Varna\docs\decisions\003_dual_claude_code_governance.md   3118
C:\git\Fire_Varna\docs\decisions\006_places_in_search.md             17058
C:\git\Fire_Varna\docs\decisions\007_address_path_v2.md               9511
C:\git\Fire_Varna\docs\decisions\010_signed_quarter_boundaries.md    53242
C:\git\Fire_Varna\docs\plans\ПЛАН_Адресите_по_полигон_08.09.md       97454



exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -Encoding UTF8 -TotalCount 28" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$f='"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md'; "'$l=Get-Content -LiteralPath $f -Encoding UTF8; '"'LINES '+"'$l.Count; for($i=0;$i -lt [Math]::Min(145,$l.Count);$i++){ '"'{0}: {1}' -f ("'$i+1),$l[$i] }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git log -1 --format='%h %s'" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git diff --cached --stat' in C:\git\Fire_Varna
 succeeded in 509ms:
10aabba state: §12 — address-by-polygon plan v2 (draft f745349), map probe for Petar, four external reviews launched (S32/S33/S34/К32)

 succeeded in 661ms:
# Active context — Fire_Varna

> **05.09.2026 16:55 — ДОСТАВКА A ПУБЛИКУВАНА:** Петър пушна `6da5d9a..fd13907` през куката (306 теста OK, 7/7 гейта). Публикуваните blob-ове = локалните (hotels 46a44ce82f15, places 329310f577e8, categories 874e33cd00e2, index.html 3d3bf79b58bf). Живата карта: хотели с квартал 152/225, АДМИРАЛ = к.к. Златни пясъци (REG). Следващ лот: „Границите“ (`docs/sessions/ПРОМПТ_нова_тема_Границите.md`); преди следващата доставка — A.2-11 (амандамент №10).


**Date:** 2026-09-05 · **HEAD:** A.2-4 = this commit (its parent is `a694c7e`, A.2-3) · **branch:** `main` · **signed:** __

> One page. Every number below is the output of the command next to it, run on the date above; a number without a command does not enter. The chronicle of 03–04.09 (ЛОТ 1, 1в-А, 1в-Б, 1в-В, the pre-rebase hash table) is frozen in [archive/activeContext_2026-09-04.md](archive/activeContext_2026-09-04.md); the one before it in [archive/activeContext_2026-07-04.md](archive/activeContext_2026-07-04.md).

## What this repo is

The public mobile-first web app that shows a Varna-oblast firefighter the nearest working hydrant, with no install and no account. Live: <https://petar1984.github.io/Fire_Varna/> (GitHub Pages, `main`, path `/`). Field reports are moderated by Petar before they change data. Governance: `AGENTS.md`; executor rules: `CLAUDE.md`.

## Where the work stands (05.09)

**Фаза A of `plans/ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md` (signed 05.09 02:50) + its four amendments: F12 (а–з) and A.2 (1–4) are executed and wait for Petar.** F12 copies the P7 delivery of varna_3d (М2 + М3 + М6) into `data/`, re-pins the three SHA constants, bumps the places cache to v6, opens the closed client lists for the three codes the delivery carries (`mladost`, `briz`, `morska_gradina`), adds the М7 „bare place“ branch on both sides, moves the two bundle tests onto the delivered numbers (F12-д), narrows М7 to significant tokens (F12-е) and makes every manifest anchor that names a commit the bytes of the **blob** at that commit (F12-ж).

**A.2 built the release machinery** (амандамент №4): `gates/release.py` — проверка 6 — binds the frozen reference, the engine candidate, the pinned inputs and the manifests by digest and refuses every delta that no signed queue row covers; `gates/sign.py` applies „да/не“ to a queue row and to the artefact it governs and refuses to run while the git identity is an agent's; проверка 7 reads back with `git log -S` who INTRODUCED each signature; the pre-push hook now runs the suite AND the gates and has no break-glass at all; and every delivery-dependent expectation left the code for one signable body, `scratch/places_search/expectations.json`. **Nothing is frozen and nothing is published.**

Four things are waiting for Petar's own hand — none of them may be written by an agent:

1. `gates/baseline/MANIFEST.json` → `signed_by: "Петър"` („подписвам baseline f06ac06“).
2. `gates/allow/2026-09-05_lot1v_v.json` — 150 named rows in four reason classes (`hull_artifact` 80 · `no_witness` 56 · `resort_pending` 8 · `m6_changed` 6).
3. `scratch/places_search/lot1v_v_manifest_BASE_P7.json` and `…_P7_F12.json` — the two diffs, every row shown; the P7→F12 one also carries the two controls of gate 6 („приморски“, „владислав варненчик“) as a signable delta.
4. `scratch/places_search/m7_trigger_tokens.json` — **33 triggering words**, waiting for a signature.
5. `scratch/places_search/expectations.json` — the ONE body every delivery-dependent expectation now lives in (the answers of the 78 gate questions, the §10 sweep, the П7 measure, 15 claims, the three bucket anchors, the replay counts, and the „before“ of every question as the frozen reference answered it). `python -m gates.sign <id> да` writes the signature; an agent writes only `pending — Петър`.
6. `scratch/places_search/ЗА_ПОДПИС_<дата>.md` — the queue itself (A.3, not written yet). Until it exists проверка 6 is RED with „няма опашка“, which is the fail-closed answer, not a defect. F12-е closed the short-prefix defect: the eight type prefixes (`к`, `кв`, `ж`, `м`, `с`, `о`, `т`, `зона`) no longer fire the branch; the 45 measured candidates stay in the file with `triggers: false` so what was thrown out stays visible.


 succeeded in 519ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
 data/hotels.json                                   |  169 ++-
 data/place_categories.json                         |  320 ++--
 data/places.json                                   |  427 ++++--
 gates/probe/b3_g11.py                              |  121 ++
 index.html                                         |  130 +-
 scratch/places_search/granitsi_fixtures_06.09.json |  855 -----------
 scratch/places_search/granitsi_fixtures_07.09.json | 1572 ++++++++++++++++++++
 scratch/places_search/probe_places_fv.mjs          |    2 +-
 scratch/places_search/recall_sweep.py              |   66 +-
 tests/granitsi_client_probe.mjs                    |  278 ++++
 tests/test_b3_gates.py                             |  202 +++
 tests/test_granitsi_fixtures.py                    |  642 ++++++--
 tests/test_hotels_public_bundle.py                 |  130 +-
 tests/test_places_public_bundle.py                 |  185 ++-
 14 files changed, 3843 insertions(+), 1256 deletions(-)

 succeeded in 743ms:
LINES 546
1: # ПЛАН · Адресите по полигон (v2)
2: 
3: **Файл:** `C:/git/Fire_Varna/scratch/places_search/ПЛАН_Адресите_по_полигон_v2_08.09.md`
4: **Дата:** 08.09.2026 · **Автор:** Planner (read-only, Opus) · **Статус:** ЧЕРНОВА — чака Gate 1 (подпис на Петър)
5: **Заменя:** v1 от 08.09 (същия ден). **Основание за v2:** три състезателни опровержения (gates / semantics / delivery), всичките с присъда **НЕГОДНО**. Всяка находка е сверена срещу файловете; приетите са вградени тук, отхвърлените са в §11, присъдите — в §12.
6: **Изпълнител:** Opus Executor · **Одитор:** Opus, състезателен · **Публикува:** Петър.
7: 
8: **Клас на риска: 🔴 АРХИТЕКТУРЕН.** Задействани спусъци: (1) нов канон за квартала в доставяни данни; (2) промяна на схемата на публичния payload (`index_schema_version`, `ALLOWED_ENTRY_KEYS`); (3) нов външен източник на имена в публична повърхност (подписаните полигони); (4) междурепова радиация `Varna_buildings → varna_3d → Fire_Varna`; (5) отмяна/уточняване на подписани прецеденти (Р38; отношението към ADR 010); **(6) НОВ — лотът е забранен от ПРИЕТ ADR 006 D12 и е разрешен само от НЕПОДПИСАН ADR 007** (`C:/git/Fire_Varna/docs/decisions/006_places_in_search.md:157-163`, `007_address_path_v2.md:3`), при това пипа изрично пиннатите „scorer and comparator“ (`007:15`); (7) доставка към публикуване, комбинирана с висящата Б3. Топология: **Вариант А**.
9: 
10: **Две доставки в един лот:**
11: - **(A) Каноничен квартал** — думата идва от подписания полигон под точката; написаният свидетел остава търсим, никога авторитетен.
12: - **(B) Ориентир за блоковете** — всеки блоков ред носи ориентир („кв. Левски, бл. 11, до ул. Студентска“), за да са различими едноименните блокове.
13: 
14: ---
15: 
16: ## 0 · Червени редове (важат за всеки ход)
17: 
18: 1. **Агентите не публикуват.** Никакъв `git push`, никакъв remote, никакъв `--no-verify`. Агентът казва „публикуване“ и спира. `git push` **не стои** в нито един команден списък на този план (§5.Д).
19: 2. **Нула геометрия и нула реконструкция на границата в публичен файл.** По ADR 010 D3 (`010:42`) публично излизат само `name`/`code`/`src`. **Не се изнася `dist_to_edge_m`** — нито поле, нито кофа, нито закръглено; забраната става структурна проверка в публикационния гейт (§4.1, G-A2).
20: 3. **`config/quarter_registry.json` не се пипа** (подписът `REGISTRY_SIGNED_SHA256`, `js/lib_quarter_registry.mjs:45-46`). Всяко движение в регистъра (родителите на Възраждане 1–4, Розова долина, Кокарджа, Абатко, Салтанат, висящият `borovets`) отива в **сутрешния списък**.
21: 4. **Данните комитва Петър** (D16/G4). Изпълнителят комитва само код, тестове, гейтове и документи.
22: 5. **Всеки гейт е команда с изход ≠ 0 и назована отрицателна фикстура, която ТРЯБВА да падне** — и фикстурата трябва да пада по НОВОТО твърдение, не по стара проверка (§6; прецедент `checkFixture`, `js/test_fire_varna_publish_gate.mjs`).
23: 6. **Само Opus.** Всеки `Agent`/`agent()` с `model: "opus"`.
24: 7. **Мярка преди промяна, с произход на всяко число.** Числата в §1.А носят етикет за извор (СКАУТ / опровергател / задание). Всяко число, което влиза в подпис, гейт или фикстура, се преизмерва в М0 (§1.Б); **разминаване с базата тук = СПИРАЙ** (§7).
25: 8. **Нула кадастрални идентификатори, нула ГРАО, нула PII** в двата адресни payload-а.
26: 9. **Атрибуцията не се пипа от този лот.** Измерено: низът „Кварталните граници“ днес **не съществува** в `index.html` (СКАУТ 5; потвърдено косвено — той стои само като ЗАБРАНЕН литерал в `tests/test_b3_gates.py:43-44`). Този лот не добавя и не преформулира нито един атрибуционен ред; `FORBIDDEN` остава зелен (G-B6). Ако Б3 достави ред за атрибуция, обхватът му за адресните редове е решение на Петър — **отделен ред в сутрешния списък**, не тук.
27: 10. **Б3 (местата) не се ПРОМЕНЯ от този лот**, но **се КОМИТВА пръв, от ръката на Петър** (§5.0). Двата текста на v1 (§0.10 „не се пипа“ ↔ §5.Г „влиза в HEAD пръв“) са изравнени тук.
28: 11. **Един логически комит = един ход**, точното съобщение от §5, стейджване с явни пътища, никога `git add -A`. **`index.html` е в ДВАТА write-set-а** — преди F1 `git diff --cached -- index.html` трябва да е празен (§7 т. 14).
29: 12. **`sw.js` не се пипа** (недосегаем и по `006:158`, и по `007:13`; освен това промяната е безполезна — `sw.js:104-106` трие само кешове с префикси `B2_CACHE_PREFIXES`, а `fire-varna-search-*` не е сред тях).
30: 
31: ---
32: 
33: ## 1 · Мярка
34: 
35: ### А. Базата (всяко число с извор)
36: 
37: **Публичните payload-и днес** (`C:/git/Fire_Varna/data/`, СКАУТ 1 §0/§2, СКАУТ 5 §A):
38: 
39: | факт | стойност |
40: |---|---|
41: | `search_index.json` | 11 242 756 B · 86 232 записа · `index_schema_version "2.0"` · `address_row_count 80510` · `vocab` 2 889 · `district_names` 5 |
42: | по вид | address 70 575 · mf 14 687 · parcel 970 |
43: | полета | `label` 43 133 · `display_id` 43 295 · и двете 196 · `qtk` 19 494 · `alias_tk` 574 · `stk` 362 · `btk` 5 567 · `d` 85 935 |
44: | `address_rows.json` | 5 073 137 B · 80 510 реда · `field_order ["normalized_address","lat","lng"]` |
45: | first load | HEAD 560 855 + 1 317 355 = 1 878 210 B (кап 5 MB); адресните са lazy — 15,57 MiB на първи фокус |
46: | `district_names` | **проверено от Planner-а сега:** `["Аспарухово","Владислав Варненчик","Младост","Одесос","Приморски"]` (`data/search_index.json`, top-level) — `d=3` е Одесос, `d=4` е Приморски |
47: 
48: **Подписаните полигони** (`C:/git/varna_3d/data/quarters_signed.geojson`): **проверено от Planner-а сега — 60 имена**, сред които `ж.к. Възраждане` + `Възраждане 1..4`, `ж.к. Младост` + `Младост 1/2`, `кв. Чайка` И `к.к. Чайка`, `кв. Левски`, `кв. Виница`, `Център`, `Колхозен пазар`; **няма „Цветен квартал“, няма „Боровец“ (само север/юг)**.
49: 
50: **Класове спрямо полигоните** (СКАУТ 3 §1–§5): inside-undisputed 42 566 · inside-edge 26 227 · overlap-incomparable 4 174 · outside-all 13 265. Върху inside-undisputed: съвпада 4 569 · противоречи 4 399 · без дума 33 598. Класове на несъгласие (n≥5, 53 реда): `vinitsa`→Манастирски рид 1 264 / Акчелар 651 / Ален Мак 205 / Св. Никола 64 / Сотира 63 / Перчемлията 88 / Евксиноград 68; `tsveten kvartal`→кв. Левски 318, →Изгрев 9; `mikroraion`→Център 269, →Гръцката махала 154; `kolhozen pazar`→кв. Тракия 245; **`chaika`→кв. Левски 150**; `rozova dolina`→Аспарухово 177.
51: Дупки (outside-all, само `mf` носят дума): Център 753 · Колхозен пазар 490 · Левски 478 · Гръцката махала 410 · Чайка 219 · Цветен квартал 197 · Виница 1 461 · без дума 8 810.
52: Припокривания: 5 620 → **подписан parent/child 1 446 · несравними 4 174** (СКАУТ 3 §5; обръща сплита 4 202/1 418 от мярката 08.09 → М0.4).
53: Проверимост на днешните думи: от 19 494 с `qtk` само **8 968 (46,0 %)** стоят там, където полигон може да ги потвърди или обори.
54: 
55: **Лентата и конкурентите (числа на опровергателите — задължителни за преизмерване в М0.5):**
56: 
57: | факт | gates | semantics |
58: |---|---:|---:|
59: | в точно един полигон | 67 347 | — |
60: | от тях в собствената лента | 25 613 | 25 613 |
61: | от тях с конкурент в лентата | **11 641 (45,4 %)** | **11 625 (44,3 %)** |
62: | извън лентата, но с конкурент | 2 156 | — |
63: | извън всички, но в лентата на ТОЧНО ЕДИН | **4 042** | — |
64: | извън всички, в лентата на няколко / далече | 620 / 8 603 | — |
65: 
66: **Флагманът (двамата опровергатели съвпадат, третият го потвърждава по друг път):** записът `{"kind":"mf","pin":[43.22212,27.9378],"tk":["studentska","bl","11"],"qtk":["chaika"],"label":"кв. Чайка, бл. 11","g":"b6797e83ec13fe798"}` е **вътре в кв. Левски на 67,4 m от ръба** при `precision_m = 100`; най-близкият чужд полигон **ж.к. Бриз е на 82,8 m** — тоест конкурент В лентата. Под Р5(а) и Р5(в) на v1 този запис **остава без квартал** → v1 не решаваше жалбата на Петър (§12).
67: Съседни случаи: „Цветен квартал, бл. 11“ вътре в кв. Левски на 56,3 m с конкуренти Изгрев 49,5 m и Кокарджа 49,0 m; запис `pin [43.21976, 27.91949]`, днес „кв. Левски, бл. 11, бул. Царевец“, е **51,2 m ИЗВЪН** кв. Левски.
68: 114: 
115: ### В. Точки на вмъкване (всички проверени лично от Planner-а сега)
116: 
117: **`C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs`:** `:452-454` S9 база · **`:457-458` `TYPEWORDS` (няма „do“)** · `:459-471` `canon` · `:481-487` `entryTokenSet(e)` — чете **геокодерния** запис, не публичния `o` · `:502-509` `s9Inconsistency` (правило (1): всички улични токени липсват → inconsistent) · **`:609-619` `resolveC2BlockLabel` — fail-closed, `reason:"token_inconsistent"`** · `:698` `o = {kind,pin}` · **`:701` `qtk` — единственото място, където кварталните токени влизат в индекса** · `:722-724` dtk/stk/btk · `:731` `evaluateRow` · **`:743-754` C2** · `:757-779` S9 · `:806` `display_id` само при липсващ label · `:826-842` F3 (не прилага повторно токеновия гард) · `:847-850` tidy · **`:857-871` регистърът** · **`:873-922` Р38** · `:923` push.
118: 
119: **`js/lib_fire_varna_block_labels.mjs`:** `:39` `STREET_TYPE_RE = /^(ул|бул|бл\.вход|пл)\.?$/i` · `:106-126` `extractStreet` (без типов опенер → `null`) · `:155` `buildBlockLabelIndex` · `:168` `cleanQuarterDisplay(info.quarter)` · `:170` `extractStreet(info.addrLine)` · `:183` база `` `${quarter}, бл. ${rec.n}` `` · **`:191-199` Pass C — улица САМО при колизия, лепи се като `${base}, ${street}` (без „до“)** · `:203-215` stats.
120: 
121: **`js/test_fire_varna_publish_gate.mjs`:** `:40-47` входовете (полигони НЕ се четат) · **`:56-59` `ALLOWED_ENTRY_KEYS` (13 ключа, затворен набор — всеки непознат ключ вече е нарушение)** · `:62-68` `PRIVATE_KEYS` · `:71` каднум · `:78-80` регион · `:101-104` `FORBIDDEN_SUBSTRINGS` · `:108` bbox · `:110` `TOKEN_FIELDS` · `:128-147` топ-ниво (НЕ е затворено множество).
122: 
123: **`C:/git/Fire_Varna/index.html`:** `4881-4892` `baseAddressLabel` (label → `addressRows[display_id].normalized_address` → район) · `4893-4897` `formatAddressHit` · `5088-5100` `dedupeDisplayRows` · **`5134` резервен vocab · `5140-5145` postings · `5151` `_areaVocab = dtk∪qtk∪stk`** · `5164-5171` `qBlk`/`areaPresent`/`blockTyped` · `5197-5221` `scoreEntry`: tk `:5204` → alias `:5205` → **`matchedCore += 1` `:5206`** → **qtk `:5207`** → dtk `:5208` → stk `:5209` · **`:5216-5219` `dem`/`ddem`/`odem`/`sdem` — всичките с условие `matchedCore === 0`** · `5230-5256` компаратор, **`5252-5253` `tk.length + qtk.length`** · `5265` `trueTie` · **`5278-5288` груповият блоков клон** · `5291-5299` bare-block · `5303`/`5313` двете проекции · `5327` `SEARCH_CACHE` · **`5351-5372` `ensureSearchData` — тук е единственият слой, който може да е fail-closed** · `5411-5423` `buildExactItem` (`5417` заглавие, `5420` „район X“) · `5430` `'Няма съвпадения'` · `5926` approx = false.
124: 
125: ### Г. Гейтове днес — какво покрива адресната доставка
126: 
127: Нула от седемте на `run_gates`: `SHA_PINS` (`gates/run_gates.py:68-72`) и `PUBLIC_BLOBS` (`:82-87`) са затворени около hotels/places/categories/signed_facts; **`check_no_cad_ids` чете РАБОТНОТО ДЪРВО и мълчаливо пропуска липсващ файл** (`:188-191`); `coverage.py:75` = `("places","hotels")`. Пипат адресите само `tests/test_data_ascii_mojibake.py:35-36` и `tests/test_basemap_manifest.py:164-165`. `data/generation_manifest.json` не се чете от никого. `recall_sweep.py:73-76` работи само върху hotels/places/categories → **замразеният корпус не покрива адреси и няма адресна `--freeze` команда** (`:90`). Единственият истински пазач е публикационният гейт в `Varna_buildings`.
128: `gates/probe/b3_g11.py` (стейджнат): инвентар + съдържание от ЕДНА снимка (`:91-93`, `:55-62`), но **`ALLOWED_NEW` е затворена седморка (`:40-46`) и `stray_new` дава exit 1 (`:116-119`)**; при `HEAD --cached` след комита дифът е празен и това рамо е инертно.
129: 
130: ---
131: 
132: ## 2 · Целта и НЕ-целта
133: 
134: **Вярно = координатата решава квартала; името е свидетел.**
135: 
136: | Класификация на пина | Каноничен квартал | Написан свидетел | Дисплей |
137: |---|---|---|---|
138: | в точно един полигон, **извън лентата** | името на полигона | `wtk` (търсим, демотиран) | „кв. Левски, …“ |
139: | в точно един полигон, **в лентата** | по Р5 (а/б/в/г) | същото | по Р5 |
140: | подписан parent/child + геометрично доказан | **само детето** | същото | детето |
141: | parent обявен, но недоказан геометрично | няма | същото | само „район X“ + леджер |
142: | несравнимо припокриване | няма | същото | само „район X“ |
143: | извън всички (вкл. „в лентата на един“, Р5-д) | по Р5-д | същото, **без гард** | по Р5-д |
144: 
145: **Целта:**

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$l=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md' -Encoding UTF8; for("'$i=145;$i -lt 290;$i++){ '"'{0}: {1}' -f ("'$i+1),$l[$i] }' in C:\git\Fire_Varna
 succeeded in 746ms:
146: 1. Публичната квартална дума за еднозначните редове е името от подписания полигон, на **двата** дисплей пътя (label и display_id).
147: 2. Написаният свидетел остава **търсим** (правилото на Р38 „добавя, никога не реже“, комит `bfb5f86`), но **не удовлетворява изричен квартален филтър, когато записът има канон, който му противоречи**.
148: 3. Всеки блоков ред носи **ориентир**, доставен **структурно** (стига и до двата дисплей пътя, без да пипа `address_rows.json` и без да минава през токеновия гард на C2).
149: 4. Неопределеното се показва като неопределено — доколкото текстът позволява (§3 Р12: 2 775 реда днес биха си противоречили сами).
150: 5. Дупките, ръбовете и споровете отиват в **частен леджер** и в борда, не в данните.
151: 
152: **НЕ-целта (изрично забранено):** най-близък полигон / буфер / разширяване на полигон; промяна на координата, номер, вход или идентичност; геометрия или разстояние до ръб в публичен файл; движение в регистъра; палене на approx (`index.html:5926`); преименуване на `.asr-item`; промяна на низа `'Няма съвпадения'` (`:5430`); промяна на СЪДЪРЖАНИЕТО на `data/address_rows.json` (ADR 007 D2); промяна на `sw.js`.
153: 
154: ---
155: 
156: ## 3 · Решения за Петър преди билда
157: 
158: > Всяко решение = един ред за подпис. Без подпис по Р0–Р18 билдът не тръгва.
159: 
160: **Р0 · Управленското разрешение (НОВО, блокиращо).** ADR 006 D12 (**Accepted**) изброява поименно `data/search_index.json`, `data/address_rows.json`, `sw.js` и **„every function of `initAddressSearch`“** като недосегаеми, а гейтът му е „адресният корпус е байт-идентичен“ (`006:157-163`). ADR 007, който вдига това, е **Proposed — awaiting Petar** (`007:3`) и при това пинова изрично **„the scorer and comparator“** (`007:15`) — точно каквото този лот пипа.
161: *Препоръка:* **подпиши ADR 007 И подпиши разширението му** (нов ADR 064, §4.1), което: (а) вдига 006 D12 за изброения адресен write-set; (б) **разпинова `scoreEntry` и компаратора** за назованите редове; (в) обявява, че G3 престава да е байтова равнопоставеност и се заменя с диференциален address replay; (г) **не** вдига `sw.js` и **не** вдига съдържанието на `address_rows.json`.
162: 
163: **Р0-б · Kill switch `ADDRESS_PATH_V2`.** ADR 007 D4 иска селектор на всеки use site, никога ранен `return`.
164: *Препоръка:* **да** — селектор около четирите нови места в клиента (`quarterPrefix`, `orientationSuffix`, гарда на свидетеля, `otk` клона). Цена: ~20 реда и двойна фикстура в replay-а (флаг вкл./изкл.).
165: 
166: **Р1 · Дупката „Център“** (753 mf извън всички + част от 8 810-те без дума).
167: *Препоръка:* неопределено; „район Одесос/Приморски“ по измерения `d`; свидетелят остава търсим; ред в борда „Център иска подписан полигон“. **Не разширяваме полигон.**
168: 
169: **Р2 · „Цветен квартал“** (няма полигон, няма запис в регистъра; 197 извън + 318 несъгласия към кв. Левски + 9 към Изгрев).
170: *Препоръка:* координатата решава — 318-те стават „кв. Левски“ (при Р5 (в)/(г); при (а)/(б) част от тях падат в лентата и остават неопределени — числото идва от М0.5); „цветен квартал“ остава свидетел; 197-те извън — по Р5-д.
171: 
172: **Р3 · „Колхозен пазар“** (490 извън + 245 несъгласия към кв. Тракия).
173: *Препоръка:* същото правило като Р2.
174: 
175: **Р4 · Флагманът Левски–Чайка при Студентска.** Измерено: пинът е ВЪТРЕ в кв. Левски на 67,4 m при `precision_m = 100`, конкурентът Бриз е на 82,8 m.
176: *Препоръка:* **„кв. Левски“ канон, „Чайка“ свидетел** — изпълнимо САМО при Р5 (в) или (г). При (а) и (б) този запис остава без квартал и **лотът не решава жалбата ти** — това е записано тук, на първа страница, не на осма.
177: 
178: **Р5 · Лентата — четири варианта с измерените цени** (числата се финализират от М0.5; днешните оценки в скоби):
179: 
180: | вариант | правило | губят име | флагманът |
181: |---|---|---:|---|
182: | (а) строга | всичко в собствената лента → неопределено | ~25 613 | ✗ |
183: | (б) конкурентна (v1 Р5в) | неопределено само при конкурент в лентата | ~11 6xx | ✗ |
184: | **(в) съдържанието решава (препоръка)** | пинът е в точно един полигон → името се дава; лентата се записва само в леджера | 0 | ✓ |
185: | (г) по-близкият конкурент | неопределено само ако чужд ръб е ПО-БЛИЗО от собствения | подмножество на (б) | ✓ (Бриз 82,8 > 67,4) |
186: 
187: *Довод за (в):* неопределеността не може да стане чуждо име; чужд полигон, който НЕ съдържа точката, не може да я спечели. *Честната цена:* при (в) грешка е възможна за записите на ≤ band от ръба (~25 613) — тя се лови от леджера и от извадката на Петър, не от гейт. Ако искаш нула такъв риск → (а), но тогава подпиши изрично, че флагманът остава без квартал.
188: **Прагът „15 %“ от v1 отпада** — той не е решение, а тавтология (§12).
189: 
190: **Р5-д · Класът „извън всички, но в лентата на ТОЧНО ЕДИН полигон“ (~4 042; пример: „кв. Левски, бл. 11, бул. Царевец“ на 51,2 m извън).**
191: *Препоръка:* **остава неопределен (без канон), НО свидетелят му НЕ се гаси** (виж Р14-б) — така „бл 11 левски“ продължава да го връща, само че под редовете с канон, с назована причина в леджера. Алтернативи за подпис: (i) получава името; (ii) пълно мълчание (не се препоръчва — истински Левски бл. 11 изчезва от собствената заявка на Петър).
192: 
193: **Р6 · Р38 (зоната „Виница“) срещу подписаните полигони.** Зоната хваща 9 771 реда (8 996 „без свидетелство“), а Манастирски рид (1 264), Акчелар (651), Ален Мак (205), Св. Никола (64), Бриз, Перчемлията, Евксиноград, Сотира имат СВОИ полигони.
194: *Препоръка:* подписаният полигон има предимство; Р38 работи само там, където резолверът връща неопределено; правилото „добавя, никога не реже“ се запазва, но добавеният токен отива в свидетелското поле. Отменя част от подписан на 12.08 прецедент → иска изричен нов подпис.
195: 
196: **Р6-б · Отношението към ADR 010 (D6/D7/D8).** ADR 010 D6 (`010:48`) урежда канала `SIGNED_POLYGON` в `varna_3d/src/fire_varna_locations.py` за **375-те МЕСТА** („пише само в ред без свидетел, извън ръба, в точно един полигон“); този лот е ДРУГА повърхност (адресният индекс, генериран в `Varna_buildings`) — затова тук няма автоматична отмяна (§11.2). Но политиките се разминават в три точки и това трябва да е ПОДПИСАНО, не мълчаливо: (1) тук полигонът пише и в ред с написан свидетел (~4 399 замени); (2) при Р5(в) пише и в лентата (~25 613); (3) D8 иска геометрично доказано `дете ⊆ родител` — приемаме го дословно (недоказаният parent → неопределено + червен ред в леджера).
197: *Препоръка:* ADR 064 изброява трите разминавания и казва „ADR 010 остава непроменен за местата“.
198: 
199: **Р7 · Несравними припокривания (4 174; топ: Аспарухово+Розова долина 746, Гръцката махала+Център 621, Възраждане+Възраждане 1 545 …).**
200: *Препоръка:* неопределено + леджер. Липсващите йерархии (1 179 + 746 + 525 + 296 + 239 записа) са ход в регистъра → **сутрешен списък**. Признатата цена: ~2 985 записа остават неопределени само заради липсващ `parent`.
201: 
202: **Р8 · Approx пакетът** (8 361, `index.html:5926 = false`). *Препоръка:* остава изключен; при палене минава през същия резолвер.
203: 
204: **Р9 · Ориентир: винаги или само при колизия?** Днес улица се лепи само при сблъсък в СЪЩИЯ написан квартал (`lib_fire_varna_block_labels.mjs:191-199`); само 26 етикета носят улица.
205: *Препоръка:* **винаги за блокови редове** („много блокове 11 в кв левски не е добре“). Колизионният детектор остава само за да маркира `must_disambiguate` и да храни G-A6б.
206: 
207: **Р9-б · Какво става, когато ориентирите СЪВПАДАТ** (измерено: 24 (gates) / 16 (semantics) неразличими групи; примери: ж.к. Бриз бл. В — 13 групи, „ул. Д-р Петър Скорчев“ 4 пъти; кв. Трошево бл. 5 — две групи „ул. Радост“; кв. Чайка бл. 37 — две групи БЕЗ улица).
208: *Препоръка:* втора степен на ориентира — **втората по близост различаваща улица**; ако и тя не различава — **разстоянието в метри** („до ул. Радост, 40 m“ / „…, 90 m“); остатъкът след двете степени е **подписан списък изключения** от М0.6, срещу който G-A6б сверява (гейт срещу измерен остатък, не срещу нула).
209: 
210: **Р9-в · Един източник на уличния текст.** С Р9 ориентирът става структурен → Pass C (`:191-199`) **спира** да лепи улица в `label` (иначе „бл. 11, ул. Мир, до ул. Мир“). Цена: ~26 етикета губят суфикса си, който се връща като структурен ориентир; диффът се мери (G-A10). *Алтернатива:* Pass C остава и структурният ориентир се пропуска там — по-малък диф, две правила.
211: 
212: **Р10 · Какво е „собствена улица“ и как се изписва.** Днешният `extractStreet` иска типов опенер (`:39`) → за „Студентска бл. 11“ връща **null** (17,5 % от блоковите `address_line` дават улица), но `tk` на записа НОСИ `studentska`.
213: *Препоръка (Р10-а):* собствена улица = `extractStreet(addrLine)` **ИЛИ** улично име от речника (1 625 имена), чиито токени са в `tk` на записа. Изписване: собствена → „, ул. Х“; чужда (най-близка) → „, **до** ул. Х“.
214: *Следствие за подписа:* при Р10-а флагманът се изписва **„кв. Левски, бл. 11, ул. Студентска“** (собствена улица), не „до ул. Студентска“. Ако предпочиташ „до“ — тогава Р10-б: собствена улица САМО по `extractStreet`, и флагманът минава по клона „най-близка“ (52 m). **Един низ, не два** — Р13 се подравнява по избора тук.
215: 
216: **Р11 · Радиус за „най-близка улица“.** Измерено: медиана 36,7 m, p90 93,9 m; 4 243 от 5 567 имат улица ≤ 120 m.
217: *Препоръка:* **120 m**, детерминистично разкъсване на равенства (по-малко разстояние → по-малък `skel` низ → по-малък `_ord`).
218: 
219: **Р11-б · Качество на ориентира.** 339 от 4 243 са на ≥ 100 m; парсването ражда низове като „ул кк зл пясъци х л вихрен“, „ул жк изгрев“, „ул д р индржишка кръстева“.
220: *Препоръка:* (1) ≤ 60 m → „до ул. Х“; 60–120 m → „до ул. Х, ~N m“; > 120 m → без ориентир, причина `no_street_within_radius`; (2) **филтър за нелегитимни низове** (токени `жк/кк/зпз/х л`, числови опашки, повече от 4 инициала) → причина `street_string_rejected`; (3) затворен списък допустими причини: `own_street`, `nearest_street`, `no_street_within_radius`, `street_string_rejected`, `no_block_number`.
221: 
222: **Р12 · Къде живее кварталната дума в дисплея.**
223: - (а) вътре в `label` — тогава display_id пътят (43 099 реда) остава без квартал завинаги;
224: - **(б) препоръка — структурно поле `q` + топ-ключ `quarter_names[]`** по образеца на `d`/`district_names`; кварталният сегмент напуска `label`; клиентът композира заглавието.
225: - **Р12-б (НОВО, задължително допълнение):** при (б) заглавието по display_id пътя е `префикс + ', ' + normalized_address`, а самият текст носи квартална дума → **2 775 записа биха се изписали „ж.к. Бриз, акчелар“**. Варианти: (i) **материализира се `label` само за тези 2 775** (байтовете се мерят в М0.10) — препоръка; (ii) амандамент на ADR 007 D2 и нормализация в `build_fire_varna_address_rows.mjs:98` — по-скъпо управленски; (iii) приема се и се обявява. Отделно 11 627 реда с НЕОПРЕДЕЛЕН канон запазват квартална дума в текста си → §2 цел 4 важи с това ограничение, освен ако не изберем (i) и за тях (цената пак е в М0.10).
226: - **Р12-в · Подписан таван за размера.** Оценките: +1,26 MB (semantics) / +1,54 MB (delivery) само за квартала, преди ориентира и материализацията. *Препоръка:* подписваш число `N` байта за СБОРА на двата lazy payload-а (днес 15,57 MiB); гейт G-B3 го чете от `expectations.json`; надвишаване = СПИРАЙ.
227: 
228: **Р13 · Точните низове (за дословен подпис, след избора по Р10 и М0.12):**
229: 1. заглавие с квартал и собствена улица: `кв. Левски, бл. 11, ул. Студентска` *(при Р10-а)* **или** `кв. Левски, бл. 11, до ул. Студентска` *(при Р10-б)*;
230: 2. заглавие без квартал: `бл. 11, до ул. Студентска` + втори ред `район Приморски`;
231: 3. адресен ред извън всички полигони: `ул. Битоля 13` + `район Приморски` (**не Одесос** — v1 сгреши; `d=4` = Приморски, `district_names` проверен);
232: 4. префиксът се взима **дословно** от `name` на полигона, с типовата представка, без превод.
233: 
234: **Р14 · Гардът на свидетеля.**
235: *Препоръка:* (а) `wtk` = написаните токени **МИНУС** каноничните на същия запис (иначе инвариантът `wtk ∩ qtk = ∅` пада на първия билд — ~4 588 записа имат съгласна дума); (б) речникът за „изричен квартален филтър“ се строи от **`quarter_names` (всичките 60 канонични имена)**, не от наблюдаваните `qtk` — иначе кварталите, които не са раздали нито едно име, нямат гард и „ж.к. Дружба, бл. 11“ остава пълно съвпадение през свидетеля.
236: **Р14-б · Обхват на гарда:** гардът гаси свидетеля САМО за записи с **`q != null`** (има канон, който му противоречи). Записите с неопределен канон (в т.ч. Р5-д) запазват силата на свидетеля, но с демотиране `wdem`. Така „чайка студентска бл 11“ не е пълно съвпадение, а „бл 11 левски“ все пак връща блока на бул. Царевец.
237: 
238: **Р15 · Ориентирът е СТРУКТУРЕН, не в `label` и не в `stk`.**
239: *Довод 1:* `resolveC2BlockLabel` (`:609-619`) е fail-closed по `s9Inconsistency`, а „до“ **не е в `TYPEWORDS` (`:457-458`)** → етикет „бл. 11, до ул. Мир“ с чужда улица дава `streetMissing === streetTotal` → `token_inconsistent` → етикетът се ИЗХВЪРЛЯ. *Довод 2:* `entryTokenSet` (`:481-487`) чете геокодерния `e`, а `o.stk` се пише на `:723` върху публичния обект — спасяването „през stk“ на v1 не работи без мутиране на `e`. *Довод 3:* `_areaVocab` (`:5151`) се храни от `stk` → ~306 нови улични имена биха превключили цяло семейство заявки в груповия блоков клон (`:5278-5288`).
240: *Препоръка:* ново поле `o` (индекс в топ-ключ `orientations[]`) + нови токени в **`otk`** (в postings и vocab, **НЕ в `_areaVocab`**), с демотер `otdem = 1`, ако поне един токен на заявката е съвпаднал **само** през `otk` (per-token, не `matchedCore === 0` — иначе демотерът е мъртъв, както е `sdem` при блокови заявки). Така: (1) `label` не се пипа → C2/S9 остават непокътнати; (2) ориентирът стига и до двата дисплей пътя (включително 205-те блокови реда без `label`); (3) „студентска бл 11“ не сменя клона на рендера.
241: 
242: **Р16 · Каноничните токени.** Правилото „skel(name без представка), разделено на думи“ дава голи цифри `1`,`2`,`3`,`4` (Младост 1/2, Възраждане 1–4 — проверено в имената) и къси `sv`, `rid`, `mak`.
243: *Препоръка:* числов или ≤ 2-знаков суфикс НЕ влиза самостоятелно в `qtk` (само биграмата „mladost 1“); токени с дължина ≤ 2 и чисти числа се изхвърлят. Делтата в подредбата (`:5252-5253`) се мери.
244: 
245: **Р17 · Как двете доставки стават ЕДНА публикация.** *Препоръка:* Б3 се комитва ПРЪВ, от твоята ръка (данните са твои), после върви адресният лот; подпис и замразяване **само когато и двете са в HEAD** (проверка 1 чете работното дърво, проверка 6 — блоба на HEAD).
246: 
247: **Р18 · G-B1 и `ALLOWED_NEW`.** Адресният лот добавя ≥ 4 нови проследени файла; `gates/probe/b3_g11.py:40-46` е затворена седморка и е част от стейджнатия Б3.
248: *Препоръка:* лотът получава **свой** пробен файл `gates/probe/addr_g11.py` (копие на механиката със свой `ALLOWED_NEW`), за да не пипаме Б3-евия артефакт. Алтернатива: разширяваш `ALLOWED_NEW` с четирите пътя — тогава §0.10 се амандира за този един ред.
249: 
250: ---
251: 
252: ## 4 · Write-set по репа
253: 
254: ### 4.1 `C:/git/Varna_buildings` (Executor комитва)
255: 
256: **НОВ · `tools/build_signed_quarter_index.py`** — Python пре-стъпка (прецедент `tools/build_quarname_enclosures.py`).
257: - Вход: блобът на полигоните, прочетен **в Python** (`git cat-file blob <OID>`, никакви пренасочвания) + `config/quarter_registry.json` само за четене.
258: - Проверява `OID` и sha256 срещу пиновете от М0.1/М0.2 → несъответствие = throw, нищо не се пише.
259: - EPSG:4326 → 32635; за всеки полигон: външен пръстен, `band_m = max(50, precision_m)`, bbox; **изчислява и таблица „кой полигон е конкурент на кого“ само за ЛЕДЖЕРА** (никога за публичния изход).
260: - Изход: `output/signed_quarters_baked.json` (частен) + `output/signed_quarters_baked_schema.json` (tracked по изключението `!output/*_schema.json`).
261: - Забрана: нищо извън `output/` (образец `_assert_private_out`, `tools/build_number_pins.py:883-896`).
262: 
263: **НОВ · `js/lib_signed_quarters.mjs`** — резолверът (НЕ в `lib_quarter_registry.mjs` — Д10, `js/test_quarter_registry.mjs:189-200`).
264: - `loadSignedQuarters(path)` — сверява `source_oid`/`source_sha256` с пинатите константи, проверява 60 полигона и `band_policy`, иначе throw с инструкция (образец `loadVinitsaZone`, `:158-186`).
265: - `resolveQuarter(model, pin)` → `{code, display, tokens, verdict, band_m, d_edge_own, nearest_other}`; `verdict ∈ inside_clear | inside_band | overlap_child | overlap_unproven | overlap_incomparable | outside_near_one | outside`.
266: - Правилата по подписания Р5/Р5-д; **`d_edge_own` и `nearest_other` се връщат САМО за леджера и никога не влизат в `o`.**
267: - `overlap_child` изисква геометрично доказано `дете ⊆ родител` в буфера (ADR 010 D8); недоказан parent → `overlap_unproven`.
268: - **Никакъв fallback по най-близък полигон — забранено на ниво код и на ниво тест.**
269: - `tokens` по Р16.
270: 
271: **НОВ · `js/lib_block_orientation.mjs`** — ориентирът (B): собствена улица по Р10, най-близка ≤ R по Р11 с филтъра на Р11-б, втора степен и разстояние по Р9-б, затворен списък причини.
272: 
273: **НОВ · `js/test_signed_quarter_resolver.mjs`** (G-A3) · **НОВ · `js/test_block_orientation.mjs`** (G-A6) · **НОВ · `js/test_quarter_ledger.mjs`** (G-A5) · **НОВ · `js/test_fire_varna_determinism.mjs`** (G-A8).
274: 
275: **ПРОМЯНА · `js/build_fire_varna_search_index.mjs`**
276: 1. `main()`: зарежда `SIGNED_QUARTERS` + `ORIENTATION_MODEL` до `loadVinitsaZone`.
277: 2. Pass 2, **`:701`**: `o.qtk` вече не се преписва от геокодера. Ново:
278:  - `const sq = resolveQuarter(SIGNED_QUARTERS, o.pin);`
279:  - `o.qtk = sq.tokens` и `o.q = quarterNameIndex(sq.display)` **само** при присъда с канон;
280:  - **`o.wtk = написаните токени МИНУС `o.qtk`** (Р14-а); празен масив не се пише;
281:  - `o.otk` = токените на ориентира (собствена улица НЕ дублира `tk`; чуждата влиза само тук), `o.o` = индекс в `orientations[]`.
282: 3. **`:743` C2 и `:826-842` F3 не се пипат**; `label` вече не носи квартален сегмент (т. 5) и не носи улица (Р9-в) → рискът `token_inconsistent` не расте; броячът `c2ResByReason` се сравнява преди/след (G-A9).
283: 4. **`:873-922` Р38** се обвива в `if (!sq.hasCanon)`; добавеният токен отива в `wtk`.
284: 5. `stripQuarterSegment(label)` — само първият сегмент, само при `looksLikeQuarterSegment` (образец `lib_quarter_registry.mjs:220-229`); прилага се СЛЕД регистъра (`:857-871`), преди push.
285: 6. **Материализация на `label`** за подписаното подмножество по Р12-б (2 775 + евентуално 11 627) — само там, само с изчистения текст, с ледгер ред за всеки.
286: 7. Нови топ-ключове `quarter_names` (≤ 60) и `orientations` (сортиран, дедупликиран); `index_schema_version` `"2.0"` → **`"3.0"`**.
287: 8. `vocab` (`:956-965`) се разширява с `wtk` и `otk`.
288: 9. Нов частен изход `output/quarter_polygon_ledger.json`: старо име + **`source` (kais/osm) + `mode` + `confidence` + `distance_m` на написания свидетел**, ново име, присъда, `d_edge_own`, `nearest_other`, ориентир + причина, `complex_id`.
289: 10. Отчетът (`:1071-1159`) получава броячи по присъда, по клас на несъгласие, по причина за ориентира, `blockGroups/collisionPairs/disambiguated` и `c2ResByReason` **преди и след**.
290: 11. Забрана: `d_edge_own`, `nearest_other`, `competitors` не влизат в `o` при никакви обстоятелства.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$l=Get-Content -LiteralPath '"'AGENTS.md' -Encoding UTF8; for("'$i=0;$i -lt [Math]::Min(150,$l.Count);$i++){ '"'{0}: {1}' -f ("'$i+1),$l[$i] }' in C:\git\Fire_Varna
 succeeded in 891ms:
1: # AGENTS.md
2: 
3: > **Canonical current state:** [`docs/activeContext.md`](docs/activeContext.md) — the last-updated commit, the sprint status, and every live number this repo declares. If this file conflicts with `activeContext.md`, the latter wins.
4: >
5: > Read this **before** making any changes to this repo.
6: > Project owner: **Petar** - solo developer in Bulgaria, AI-assisted workflow, no formal CS background.
7: > If anything here conflicts with a user request in chat, raise the conflict; do not silently override.
8: 
9: ---
10: 
11: ## What This Project Is
12: 
13: Mobile-first **PWA for Varna fire department and a volunteer rescue squad** - locates the nearest fire hydrant via GPS.
14: 
15: <!-- сверка 01.09.2026: спорно, виж C:\git\plan.md приложение Е ред 13 -->
16: 
17: - **Primary users:** Varna firefighters (~30-50). Emergency use, on phones, often with gloves.
18: 
19:   <!-- непроверено (01.09.2026): няма измерим източник в репото -->
20: 
21: - **Secondary users:** volunteer rescue squad. Verification and feedback only; **NOT for emergency use.**
22: - **Distribution:** GitHub Pages from `main`, HTTPS required.
23: - **Language:** Bulgarian only. No localization layer. UI labels are precise and reviewed by Petar.
24: 
25: The app loads a static hydrant dataset, shows the user's GPS position, and guides them to the nearest hydrant.
26: 
27: ---
28: 
29: ## Entry Point
30: 
31: **Start here:** [`docs/activeContext.md`](docs/activeContext.md). It is the canonical current state of this repo — branch and HEAD, dataset counts, byte sizes, what shipped last, what is in flight. Read it before this file; on any conflict about current state it wins.
32: 
33: **Trunk:** `main`. It is the GitHub default (`git symbolic-ref refs/remotes/origin/HEAD` → `refs/remotes/origin/main`) and the branch the published site is served from. The other branches listed by `git branch -a` are frozen traces of past cycles; work happens on `main` only. Agents commit to `main` locally; Petar alone pushes, so `main` can sit ahead of `origin/main` between Gate 2 and the push — read `git status -sb` instead of assuming.
34: 
35: **What is forbidden here** is written in § Hard Constraints, § System Invariants and § When To Stop And Ask. Read those three before the first edit; they are not restated in this section.
36: 
37: **Live numbers live in the entry point, not here.** No state number enters this file: record counts, per-origin counts, file counts, byte sizes and commit hashes quoted as state belong in [`docs/activeContext.md` § Current State](docs/activeContext.md#current-state); a commit named as provenance (the commit of an import, of a fix) is a pointer, not state. What stays here are numbers that are rules — hard caps, intervals, thresholds (§ Hard Constraints) — and pointers into configuration, such as the Worker deploy version in § Report Flow. A figure that carries a `непроверено` marker has no measurable source in this repo; never quote it as state.
38: 
39: ---
40: 
41: ## Runtime Architecture
42: 
43: Static GitHub Pages frontend. No backend in the repo and no runtime build step.
44: 
45: <!-- сверка 01.09.2026: спорно, виж C:\git\plan.md приложение Е ред 26 -->
46: 
47: | Component | Current State |
48: |---|---|
49: | App shell | `index.html` with inlined Leaflet, MarkerCluster, CSS, and app logic |
50: | Hydrant data | `data/hydrants.json`, loaded by `fetch` on app init |
51: | Report submission | Cloudflare Worker proxy |
52: | Report polling | Cloudflare Worker `GET /issues`, every 15 s |
53: | **Frontend first load** | `index.html` + `data/hydrants.json` |
54: 
55: Hydrant data lives in `data/hydrants.json` (record count and per-origin counts: see [`docs/activeContext.md` § Current State](docs/activeContext.md#current-state); the live origins are `vik`, `national`, `field_report`, `etr_varna`, `etr_provadia`, `etr_dolni_chiflik`, `etr_devnya`, `pozarna_gz`). Loaded via fetch on app init. `index.html` contains UI shell, Leaflet, MarkerCluster, app logic, and an empty `<script id="hydrantData">` placeholder populated at runtime.
56: 
57: Current byte sizes for `index.html`, `data/hydrants.json`, and first load are canonical in [docs/activeContext.md § Current State](docs/activeContext.md#current-state).
58: 
59: Local testing requires HTTP, not `file://`:
60: 
61: ```powershell
62: python -m http.server 8000
63: ```
64: 
65: ---
66: 
67: ## Data Model
68: 
69: `data/hydrants.json` is the runtime dataset. The original KMZ-derived `hydrants_varna.json` remains as a reference/source artifact, not the full runtime dataset.
70: 
71: Runtime verbose schema (compact-schema compatibility was removed in `142a494`):
72: 
73: ```text
74: { id, coords, origin, legacy_ids, type?, region?, address?,
75:   existence_status?, operational_status?, review_status?,
76:   verifier_note?, report_id?, reported_at? }
77: ```
78: 
79: - `coords` is `[lon, lat]` in WGS84 and is always present.
80: - `origin` is always present. Canonical network origins are `vik` (В и К export) and `national` (national dataset); field-submitted records carry `field_report`. The `etr_*` origins are the post-2026-06-21 ЕТР hydrant-register KMZ imports (`Пожарни хидранти ЕТР ….kmz`), one `origin` per municipality. `pozarna_gz` is not an ЕТР register but a separate import; it is listed in the same table:
81: 
82:   | `origin` | Source (register or import) |
83:   |---|---|
84:   | `etr_varna` | ЕТР Варна |
85:   | `etr_provadia` | ЕТР Провадия |
86:   | `etr_dolni_chiflik` | ЕТР Долни Чифлик |
87:   | `etr_devnya` | ЕТР Девня |
88:   | `pozarna_gz` | POZARNA.DWG import, Golden Sands (commit `e846b87`) |
89: 
90:   Import mechanics (distance-≤5 m ETR aliases folded into `legacy_ids`; only unmatched ETR points added as standalone records) are in [`docs/plans/h2_kmz_adapter_plan.md`](docs/plans/h2_kmz_adapter_plan.md) and the dry-run audit `docs/audits/h2_kmz_consolidation_dry_run.md`; per-source counts and the current baseline live in [`docs/activeContext.md`](docs/activeContext.md). Further `etr_*` origins may appear as more municipal registers are imported. Older app builds and unknown `origin` values must fall back to canonical/unverified rendering.
91: - `legacy_ids` is the array of a record's prior IDs (used for polling dedupe); always present.
92: - `type`, `region`, `address` are sparse descriptive fields.
93: - Visual / moderation state is split across three sparse fields, not one app-level `status`:
94: 
95: | Field | Observed values | Meaning / render |
96: |---|---|---|
97: | `existence_status` | `verified` | Hydrant physically confirmed on-site (red pin) |
98: | `review_status` | none present in the dataset today (historically `reported`) | Reported damaged / missing / needs attention (yellow pin) |
99: | `operational_status` | `works`, `not_working`, `not_tested` | Operational state, independent of existence |
100: | (all three absent) | — | Canonical unverified record (gray pin) |
101: 
102: Older app builds and unknown values must fall back to canonical/unverified behavior. `report_id` / `reported_at` carry field-report provenance.
103: 
104: ### Wrong-Location Ingest Rule
105: 
106: For `wrong_location` reports, **always update the existing record's coordinate field (`coords`) in place. Never create a new `field_*` record for `wrong_location`.**
107: 
108: | Target ID type | Action |
109: |---|---|
110: | Canonical IDs (every id starts with `coord_<lon>_<lat>`; disambiguated duplicates carry a `__NAT-####` suffix (count them with `python -c "import json;print(sum(1 for r in json.load(open('data/hydrants.json',encoding='utf-8')) if '__' in r['id']))"`); `NAT-`, `VIK-`, `GZ-` survive in `legacy_ids`) | update `coords` in `data/hydrants.json` |
111: | `field_*` IDs (no record carries one today; `field_*` survives only in `legacy_ids`) | update `coords` in `data/hydrants.json` |
112: 
113: `field_reports.json` is no longer a current file; all records (including `field_*`) live in `data/hydrants.json` only. After the coord update, set `existence_status` to `"verified"`. Old coords go in the commit message for audit trail. A `new_hydrant` report creates a record with a `coord_<lon>_<lat>` id; the `field_*` identifier it came in with is kept in `legacy_ids`. No record in the dataset carries a `field_*` id.
114: 
115: ### National Dataset Role
116: 
117: The national source files are kept as archive/reference only. They are not loaded directly at runtime.
118: 
119: Future option, not implemented: build-time enrichment of runtime data with national metadata only where spatial match is <=5m. Defer until there is concrete user demand.
120: 
121: ---
122: 
123: ## Report Flow
124: 
125: Reports are submitted via `fetch` POST to Cloudflare Worker `varna-hydrants-proxy.petar-dikov2019.workers.dev`. Worker creates a labeled GitHub issue in this repo. Reports queue locally if offline.
126: 
127: Worker source now lives in the `worker/` directory in this repo (extracted in `914dc2a`); see `worker/README.md` for deploy notes. The Cloudflare deployment remains manual; the Worker deploy version is repo-declared as `5accc88e`.
128: 
129: ---
130: 
131: ## Hard Constraints
132: 
133: | Constraint | Reason |
134: |---|---|
135: | Static hosting only (GitHub Pages free tier) | Budget = 0 BGN |
136: | App shell at repo root (`index.html`) plus static `data/hydrants.json` | GitHub Pages serves it |
137: | First load <= 3 MB ideal, **5 MB hard cap** | Mobile data, emergency use |
138: | Bulgarian UI labels preserved verbatim | Users speak Bulgarian only; wording is reviewed |
139: | Mobile-first: touch targets >= 44px, no hover-dependent UX | Field use, gloves, sweat |
140: | HTTPS-required APIs must work: Geolocation, DeviceOrientation, Worker `fetch` | Core features depend on these |
141: | **Scope: Varna oblast only** | National scope explicitly out of v1 |
142: | No new runtime or build-time dependencies without Petar approval | Keep static architecture simple |
143: | No secrets in the repo — Cloudflare/Worker credentials, `wrangler` secrets, `.dev.vars`, `.env` are gitignored and never committed | Public GitHub Pages repo |
144: | No automated commits, no automated pushes — agents commit locally with explicit paths; **Petar alone pushes** | Reversibility & release control |
145: 
146: ---
147: 
148: ## Dual-Claude-Code Workflow
149: 
150: All planning, execution, and audit run in **Claude Code** (Planner read-only / Executor / Auditor — model per `~/.claude/agents`, not pinned here) with planning and execution kept in **separate agents**; Petar holds the sign-off and push gates. See ADR [`docs/decisions/003_dual_claude_code_governance.md`](docs/decisions/003_dual_claude_code_governance.md).

codex
Б3 действително е staged в 14 пътя, включително `index.html`; има и две отделни unstaged промени. В плана вече са адресирани част от рисковете от v1. Проверявам дали описаният ред за подписи и комити е изпълним през реалните гейтове.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$l=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md' -Encoding UTF8; for("'$i=290;$i -lt 390;$i++){ '"'{0}: {1}' -f ("'$i+1),$l[$i] }' in C:\git\Fire_Varna
 succeeded in 1033ms:
291: 
292: **ПРОМЯНА · `js/lib_fire_varna_block_labels.mjs`** — Pass A `:168` остава свидетел; Pass B `:183` базата става `бл. ${rec.n}`; **Pass C `:191-199` спира да лепи улица** (Р9-в), само маркира `must_disambiguate`; нови stats `orientationOwn/Nearest/None/Rejected/collisionUnresolved`.
293: 
294: **ПРОМЯНА · `js/test_fire_varna_publish_gate.mjs`**
295: - `ALLOWED_ENTRY_KEYS` (`:56-59`) += `"q"`, `"wtk"`, `"otk"`, `"o"`; `TOKEN_FIELDS` (`:110`) += `"wtk"`, `"otk"`.
296: - **Затворен набор ТОП-ключове** (днес топ-нивото е отворено, `:128-147`) + забранени имена `dist_edge_m`, `edge_m`, `poly`, `ring`, `geometry`, `coordinates`, `geometries` навсякъде в документа.
297: - `quarter_names` / `orientations`: масиви от низове, без mojibake/каднум/цифрова серия ≥ 5; `q` и `o` — цели числа в обхват; **всеки `qtk` токен ∈ речника от `quarter_names`**; `wtk ∩ qtk = ∅`.
298: - **НОВ вход: `output/signed_quarters_baked.json`** — гейтът сам преизчислява присъдата за **всеки** запис с `q` и пада при разминаване (това е G-A4; без този вход фикстурата „`qtk:["chaika"]` при пин в Левски“ е зелена, защото „chaika“ Е валидно канонично име).
299: - Отровени фикстури, всяка задължително падаща: (ф1) `coordinates` в НОВ топ-ключ; (ф2) `q` извън обхвата; (ф3) `qtk` с неканоничен токен; (ф4) `wtk ∩ qtk ≠ ∅`; (ф5) `quarter_names` с не-низ; (ф6) **запис с `q` = Чайка при пин вътре в кв. Левски**; (ф7) `o` без съответен ред в `orientations`.
300: 
301: **ПРОМЯНА · `package.json`** — `build:signed-quarters`, `test:signed-quarters`, `test:block-orientation`, `test:fire-varna-determinism`; **`build:fire-varna` (подразбиращият се път, който пише в `../Fire_Varna/data` и НЕ строи манифеста) се обявява за забранен** — доставя се само през `:staging` + ръчно копиране на трите файла заедно.
302: 
303: **НОВ · `docs/decisions/064_signed_quarter_polygons_decide_the_public_quarter.md`** — ADR (кондензиран шаблон) + ред в `docs/decisions/README.md`; изрично: кои клаузи на ADR 006/007 се вдигат, кои разминавания с ADR 010 се обявяват (Р6-б), че `sw.js` и съдържанието на `address_rows.json` остават недосегаеми; `docs/activeContext.md` + `docs/unknowns.md` в същия ред.
304: 
305: ### 4.2 `C:/git/varna_3d`
306: **Нула промени, нула комита.** Само четене на блоба по OID (М0.1).
307: 
308: ### 4.3 `C:/git/Fire_Varna` (Executor комитва кода; данните — Петър)
309: 
310: **ПРОМЯНА · `index.html`:**
311: 1. `:5134` и `:5140-5145` — `wtk` и `otk` влизат в резервния vocab и в postings.
312: 2. `:5151` `_areaVocab` остава `['dtk','qtk','stk']` — **`wtk` и `otk` НЕ влизат** (иначе „студентска бл 11“ сменя клона на рендера, `:5168-5171` → `:5278-5288`).
313: 3. След `:5152`: `index._signedQuarterVocab` = множеството токени, произведени от **`quarter_names`** (Р14-б), не от наблюдаваните `qtk`.
314: 4. След `:5185`: `qFilterTok[qi] = _signedQuarterVocab.has(toks[qi])`.
315: 5. `scoreEntry` **след `:5209`**: клон за `wtk` — при `qFilterTok[qi] === true` **И** `e.q != null` свидетелят се пропуска изцяло (`best` остава 0 → `all=false`); иначе важи с `matchedViaWitness += 1`. Отделен клон за `otk` с `matchedViaOtkOnly`.
316: 6. `:5216-5221`: `wdem = matchedViaWitness > 0 && matchedCore === 0 ? 1 : 0`; **`otdem = matchedViaOtkOnly > 0 ? 1 : 0`** (per-token, съзнателно различно от `sdem`, който е мъртъв при блокови заявки, защото `bl`/номерът винаги удрят `tk`); нови редове в компаратора между `:5239` и `:5240` и в `trueTie` (`:5265`).
317: 7. `:5252-5253` подредбата остава `tk.length + qtk.length` — `wtk`/`otk` не се броят; делтата от смяната на `qtk` се обяснява в replay-а.
318: 8. `baseAddressLabel` (`:4881-4892`) остава само адрес; нови `quarterPrefix(hit)` от `quarter_names[hit.q]` и `orientationSuffix(hit)` от `orientations[hit.o]`; `formatAddressHit` (`:4893-4897`) композира `prefix + ', ' + base + suffix` (липсващ `q`/`o` → съответната част отпада).
319: 9. `dedupeDisplayRows` (`:5088-5100`): ключът става `norm(label) + '||' + (g ?? '') + '||' + (q ?? '') + '||' + (o ?? '')`.
320: 10. Двете проекции (`:5303`, `:5313`) получават `q` и `o`.
321: 11. `buildExactItem` (`:5411-5423`): заглавието минава през `formatAddressHit`; редът „район X“ (`:5420`) остава непроменен; класът `.asr-item` не се пипа.
322: 12. `ctx` при избор (`≈:5858-5866`) и заглавието на панела (`≈:5648`) взимат същия композиран низ.
323: 13. **`validateSearchPayload(idx, rowsPayload)` — нова функция ВЪТРЕ в среза** (Р0-б флагът я не изключва), викана от `ensureSearchData` преди `searchIndex = idx` (`:5364`): `index_schema_version === '3.0'`; всяко `q`/`o` резолвира; `idx.address_row_count === rowsPayload.rows.length`. Отказ = цялата доставка се отхвърля.
324: 14. `:5327` `SEARCH_CACHE` → `'fire-varna-search-v3'` в СЪЩИЯ комит с payload-а. **`sw.js` не се пипа** (§0.12); старият кеш `fire-varna-search-v2` остава да лежи — записва се като дълг (§9).
325: 15. Маркери за среза: `// ---- ADDR slice start` … `// ---- ADDR slice end` около `norm/skel/matchKindSet/prepareIndex/runGeocoderSearch/scoreEntry/formatAddressHit/dedupeDisplayRows` **и около `validateSearchPayload`** (иначе G-B5 е неизпълним). Липсващ маркер = `AssertionError`.
326: 16. Не се пипат: `'Няма съвпадения'` (`:5430`), `APPROX_ADDRESS_SEARCH_ENABLED` (`:5926`), PLACES клонът.
327: 
328: **НОВ · `tests/address_replay.mjs`** — изрязва среза по маркерите и го изпълнява в Node със стъбове (модел `tests/granitsi_client_probe.mjs`), с флага `ADDRESS_PATH_V2` в двете положения.
329: **НОВ · `scratch/places_search/address_corpus_build.py`** — **детерминистичен селектор** на корпуса (сортиран обход на класовете, фиксирано правило „първите N по нарастващ `_ord`“, без произволност, без seed) → пише кандидата в temp и, само с `--freeze`, проследената референция.
330: **НОВ · `scratch/places_search/address_replay_rows.json`** — замразеният корпус, сверяван като **блоб** (`git show HEAD:`; готовата проверка е `worktree_differs`, `gates/release.py:313`). Стратификация ≥ 8 заявки на клас: съгласни · несъгласни (Виница-зона, Колхозен пазар, Цветен квартал, Чайка/Студентска, микрорайон) · вътре без дума · извън всички · **извън, но в лентата на един** · parent/child · несравними · в лентата · блокови колизии · вход · координатен клон · **display_id път**. Всеки ред носи кой дисплей път е дал текста.
331: **НОВ · `tests/test_address_replay.py`** — обвивката; чете очакванията от нова секция `address_replay` в `expectations.json` („No number below is typed by an agent“ — числата идват от `--freeze`).
332: **НОВ · `tests/test_address_generation.py`** — сверява `data/generation_manifest.json` (`sha256/bytes/entry_count/address_row_count/max_display_id`) срещу блобовете в СЪЩАТА снимка (`git show :<path>` / `HEAD:<path>`) + подписания таван от Р12-в.
333: **НОВ · `gates/probe/addr_g11.py`** — по Р18 (или разширяване на `ALLOWED_NEW`, ако Петър избере другия вариант).
334: **ПРОМЯНА · `gates/run_gates.py`** — `PUBLIC_BLOBS` (`:82-87`) += двата адресни блоба; **проверка 3 се пренаписва:** чете блоба (`git show :<path>`), а **липсващ файл от списъка става ЧЕРВЕН, не тих пропуск** (`:188-190`). `SHA_PINS` не се пипа.
335: **ПРОМЯНА · `tests/test_data_ascii_mojibake.py`** — обхватът включва `quarter_names`, `orientations` и `label`; сигнатури `U+FFFD` и `[Ð Ñ Â][\u0080-\u00FF]`.
336: **ПРОМЯНА · `docs/decisions/007_address_path_v2.md`** — амандамент (write-set + разпиноване на scorer/comparator + новите гейтове; `address_rows.json` и `sw.js` остават недосегаеми) + `docs/activeContext.md`.
337: 
338: **ДАННИ (комитва Петър):** `data/search_index.json`, `data/address_rows.json`, `data/generation_manifest.json` — трите заедно, в един комит.
339: 
340: ---
341: 
342: ## 5 · Ред на изпълнение
343: 
344: ### 0. Предусловие (ръката на Петър)
345: Б3 се комитва пръв (данните са негови). След това `git status --porcelain` няма стейджнати `data/` и `index.html` пътища — проверява се от Изпълнителя (М0.11); ако не е така — **СТОП**.
346: 
347: ### А. Varna_buildings (Executor, локални комити)
348: 1. **М0** (§1.Б) → `output/addr_quarter_M0.json`. Без него нищо не тръгва.
349: 2. Копира полигоните през Python по OID (никакви `>` и `|`); проверява `git check-ignore -v output/quarters_signed.geojson`.
350: 3. **V1** `tools/build_signed_quarter_index.py` + схемата → `feat(quarters): bake signed quarter polygons into a private resolver input`
351: 4. **V2** `js/lib_signed_quarters.mjs` → `feat(quarters): add lib_signed_quarters resolver with a pinned polygon digest`
352: 5. **V3** `js/test_signed_quarter_resolver.mjs` → `test(quarters): resolver truth gate with poisoned fixtures`
353:  *Доказателство:* вариант с „най-близък полигон“ трябва да **падне**; изходът се записва.
354: 6. **V4** `js/lib_block_orientation.mjs` → `feat(fire-varna): block orientation model with own and nearest street`
355: 7. **V5** генераторът: `q` + `wtk` + `otk`/`o` + `quarter_names`/`orientations` + schema 3.0 + Р38 подчинение + излизане на квартала от `label` → `feat(fire-varna): canonical quarter q, witness wtk and structural block orientation`
356: 8. **V6** материализацията по Р12-б → `feat(fire-varna): materialise labels where the address text contradicts the signed quarter`
357: 9. **V7** частният леджер + брояците → `feat(fire-varna): private quarter ledger and build-report counters`
358: 10. **V8** публикационният гейт (нови ключове, затворено топ-ниво, полигонният вход, 7 фикстури) → `test(fire-varna): publish gate verifies the quarter against the signed polygons`
359: 11. **V9** ориентирният гейт → `test(fire-varna): block orientation gate with a signed floor and collision fixtures`
360: 12. **V10** детерминизъм → `test(fire-varna): byte-identical rebuild gate`
361: 13. **V11** ADR 064 + индекс + activeContext + unknowns → `docs(adr): ADR 064 signed quarter polygons decide the public quarter word`
362: 14. Билд през staging + гейтовете G-A* (никакъв билд по подразбиращия се път).
363: 
364: ### Б. Fire_Varna (Executor, локални комити — само код)
365: 15. **F1** клиентът (16-те точки) + маркерите + `ADDRESS_PATH_V2` → `feat(search): render the canonical quarter and the block orientation from structured fields`
366: 16. **F2** replay двигателят + селекторът на корпуса + `expectations.address_replay` + `tests/test_address_replay.py` → `test(search): address replay gate with a frozen stratified corpus`
367: 17. **F3** `gates/run_gates.py` (блоб-четене + липсващ файл = червено) + `tests/test_address_generation.py` + mojibake обхватът + `gates/probe/addr_g11.py` → `feat(gates): address blobs join the cadastral-id, geometry and manifest checks`
368: 18. **F4** амандаментът на ADR 007 + `docs/activeContext.md` → `docs: ADR 007 amendment for the signed-quarter address delivery`
369: 
370: ### В. Доставка на данните
371: 19. Изпълнителят копира трите файла от `output/fire_varna_staging/` в `Fire_Varna/data/` **заедно** и пуска целия набор гейтове. Не комитва.
372: 20. Петър комитва данните (D16/G4).
373: 
374: ### Г. Една публикация
375: Ред: **Б3 (ръката на Петър) → Varna_buildings → varna_3d (нула) → Fire_Varna код → адресните данни (ръката на Петър)**. Подпис и замразяване САМО когато и двете доставки са в HEAD. Една опашка (`ЗА_ПОДПИС_Б3_07.09.md` — адресните редове се ДОБАВЯТ в нея; преименуването на старата опашка е ход на Б3, не на този лот). Един allow-файл (адресният лот не иска нови allow редове). Едно `--freeze` за местата и едно за адресите, и двете СЛЕД подписа, всяко със свой комит. Един назован червен интервал по G20, различим от Б3-евия.
376: 
377: ### Д. Командите на Петър (по една на ред, без `&&`; **без `git push`**)
378: 
379: ```powershell
380: cd C:\git\Varna_buildings
381: npm run build:signed-quarters
382: npm run test:signed-quarters
383: npm run test:block-orientation
384: npm run build:fire-varna:staging
385: npm run test:fire-varna-publish-gate:staging
386: npm run test:fire-varna-determinism
387: cd C:\git\Fire_Varna
388: git status --porcelain
389: git add data/search_index.json data/address_rows.json data/generation_manifest.json
390: git commit -m "data(search): quarter from signed polygons + block orientation"

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$l=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md' -Encoding UTF8; for("'$i=390;$i -lt 490;$i++){ '"'{0}: {1}' -f ("'$i+1),$l[$i] }' in C:\git\Fire_Varna
 succeeded in 787ms:
391: $env:PYTHONIOENCODING="utf-8"
392: python -m unittest discover -s tests
393: python -m gates.run_gates
394: python gates/probe/addr_g11.py <комитът преди първия ход на лота>
395: python -m gates.sign R<n> да --queue scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md
396: git add scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md
397: git commit -m "sign: address delivery rows"
398: python scratch/places_search/address_corpus_build.py --freeze
399: git add scratch/places_search/address_replay_rows.json scratch/places_search/expectations.json
400: git commit -m "freeze: address replay reference"
401: python -m unittest discover -s tests
402: python -m gates.run_gates
403: ```
404: 
405: **ПУБЛИКУВАНЕ — след Gate 2, с отделна твоя дума.** (v1 слагаше `git push` редом с 13 неподписани решения; `python -m gates.sign` без аргументи пада с usage, `gates/sign.py:419-427`; `--freeze` преди комит прави проверка 6 BLOCKED, `gates/release.py:313`.)
406: 
407: ---
408: 
409: ## 6 · Гейтове
410: 
411: Всеки ред: команда · очакван изход · отрицателна фикстура, която ТРЯБВА да падне.
412: 
413: | # | Гейт | Команда | Изход | Отрицателното (задължително пада) |
414: |---|---|---|---|---|
415: | G-A1 | Пинът на полигоните (OID + sha, четени в Python) | `python tools/build_signed_quarter_index.py` | 0 | подменен байт в опечения вход; подаден commit-ish вместо OID |
416: | G-A2 | Публикационен гейт (разширен) | `npm run test:fire-varna-publish-gate:staging` | 0 | ф1 `coordinates` в нов топ-ключ; ф2 `q` извън обхват; ф3 неканоничен `qtk`; ф4 `wtk∩qtk≠∅`; ф5 не-низ в `quarter_names`; ф7 `o` без ред |
417: | G-A3 | **Истинност на резолвера** | `node js/test_signed_quarter_resolver.mjs` | 0 | (а) резолвер с „най-близък полигон“; (б) пин в зоната Виница вътре в Манастирски рид, обявен за Виница; (в) недоказан parent, обявен за дете |
418: | **G-A3-г** | **Флагманът, поименно** | част от G-A3 | 0 | **пинът `[43.22212, 27.9378]` ТРЯБВА да върне присъда, която дава „кв. Левски“** (при подписания Р5); пинът `[43.21976, 27.91949]` ТРЯБВА да върне класа по Р5-д |
419: | G-A4 | **Свидетелят не е авторитет — върху ДОСТАВЕНИТЕ байтове** | част от G-A2 (с полигонния вход) | 0 | ф6: запис с `q`/`qtk` = Чайка при пин вътре в кв. Левски |
420: | G-A5 | Пълнота на леджера (вкл. `source`/`mode`/`confidence` на свидетеля) | `node js/test_quarter_ledger.mjs` | 0 | изтрит ред за запис с различен свидетел |
421: | G-A6а | **Ориентир — подписан ПОД, не дизюнкция** | `node js/test_block_orientation.mjs` | 0 | брой блокови редове с `own`/`nearest` под пода от М0.6 (при валидни причини) → червено; причина извън затворения списък → червено |
422: | G-A6б | Различимост при колизия | същият | 0 | две групи в една двойка (квартал, блок №) с еднакъв ориентир и **извън** подписания списък изключения |
423: | G-A6в | Качество на ориентира | същият | 0 | ориентир с отхвърлен низ („ул кк зл пясъци…“); ориентир над подписания праг без бележка за разстояние |
424: | G-A7 | Р38 подчинение | част от G-A3 | 0 | ред в зоната с подписан фин квартал, префиксиран „кв. Виница“ |
425: | G-A8 | Два билда байт-идентични | `npm run test:fire-varna-determinism` | 0 | подменен байт в едното копие |
426: | G-A9 | Дрифт: S9 + C2 | вграден в билда (`:1042-1051`) + брояч | 0 | `tokenInconsistentTotal` > 20 % от 5 828; **`c2ResByReason.token_inconsistent` над подписания таван от М0.7** |
427: | G-A10 | Бюджет на диффа по етикетите | част от билда | 0 | брой сменени `label` извън подписания интервал (квартален сегмент + махнатия уличен суфикс) |
428: | G-B1 | Нула геометрия, структурно | `python gates/probe/addr_g11.py <родител>` | 0 | копие с ключ `coordinates`; **нов непосочен проследен файл → изход 1** (истински родител, не `HEAD`, иначе рамото е инертно) |
429: | G-B2 | Нула кадастрални id в адресните блобове | `python -m gates.run_gates` (проверка 3, вече по блоб) | 0 | посят `10135.1.1005.1` в **блоба**; **преименуван/липсващ файл от `PUBLIC_BLOBS` → червено** |
430: | G-B3 | Поколение ↔ размер ↔ броеве ↔ таван | `python -m unittest tests.test_address_generation` | 0 | чужд `bytes` в манифеста; `address_row_count ≠ rows.length`; сбор над подписания таван (Р12-в) |
431: | G-B4 | **Address replay** | `python -m unittest tests.test_address_replay` | 0 | (i) „чайка студентска бл 11“ като ПЪЛНО съвпадение; (ii) ред, назначен по най-близък полигон; (iii) два неразличими „бл 11 левски“; (iv) **заявка, която днес не е `blockTyped`, а утре става**; (v) `ADDRESS_PATH_V2=false`, който не връща базовото поведение |
432: | G-B5 | **Клиентска fail-closed валидация (собствен ред)** | `python -m unittest tests.test_address_replay -k validate` | 0 | (а) `index_schema_version "2.0"`; (б) `q` извън `quarter_names`; (в) несъвпадащи поколения на двата файла |
433: | G-B6 | `FORBIDDEN` остава зелен | `python -m unittest tests.test_b3_gates` | без нови червени спрямо М0.9 | забранен низ, вкаран в адресен етикет |
434: | G-B7 | Mojibake / UTF-8 | `python -m unittest tests.test_data_ascii_mojibake` | 0 | посято `Ð` и `U+FFFD` в `quarter_names`/`orientations` |
435: | G-B8 | Пълният набор | `python -m unittest discover -s tests` · `python -m gates.run_gates` | 0 червени извън назования интервал; 7/7 след подписа | — |
436: 
437: ---
438: 
439: ## 7 · STOP — спри и питай Петър
440: 
441: 1. М0.1/М0.3/М0.4/М0.5 дават числа, различни от §1.А.
442: 2. **М0.5-б показва за флагмана присъда, различна от подписаната по Р4/Р5** (тогава лотът не решава жалбата и това се казва веднага).
443: 3. **М0.6 се разминава с §1.А** (385 ↔ 91 ↔ 95; 24 ↔ 16; 1 324 ↔ 213).
444: 4. Който и да е гейт е червен и поправката не е очевидно безопасна.
445: 5. Билдът иска промяна в `config/quarter_registry.json`.
446: 6. Блоковите колизии след смяната се променят с > 20 % спрямо М0.7.
447: 7. `c2ResByReason.token_inconsistent` расте над подписания таван (ориентирът яде етикети).
448: 8. S9 `tokenInconsistentTotal` мърда с > 20 % спрямо 5 828.
449: 9. Сборът на двата lazy payload-а мине подписания таван (Р12-в).
450: 10. Резолверът иска ново публично поле извън `q`, `wtk`, `otk`, `o`.
451: 11. Появи се нужда да се пипне `data/address_rows.json`, `sw.js` или approx пакетът.
452: 12. Втора опашка `ЗА_ПОДПИС_*` в HEAD или втори json в `gates/allow/`.
453: 13. Някой ход изисква публикуване, remote достъп или `--no-verify`.
454: 14. **`git diff --cached` не е празен преди F1 или преди `gates.sign`** (смесени поколения / чужди хънкове в адресния комит).
455: 15. Пожелано е име за точка, която резолверът е обявил за неопределена („нека все пак сложим нещо“).
456: 
457: ---
458: 
459: ## 8 · Локален преглед (проби с очакван резултат)
460: 
461: `python -m http.server 8000`, 375 px, ръчно, преди Gate 2:
462: 
463: | # | Заявка | Очаквано |
464: |---|---|---|
465: | 1 | `бл 11 левски` | само блокове с пин в полигона кв. Левски **плюс** блокът на бул. Царевец (Р5-д, без квартална дума, демотиран); **всеки ред носи различен ориентир**; групата „N блока № 11“ брои каноничните |
466: | 2 | `студентска бл 11` | ред 1 = **кв. Левски, бл. 11, ул. Студентска** (Р10-а) или **…, до ул. Студентска** (Р10-б) — точно подписаният низ; „Чайка“ не се появява в заглавието; **рендерът остава в обикновения списък, не в груповия блоков клон** |
467: | 3 | `чайка студентска бл 11` | блокът **НЕ е пълно съвпадение** (`all=false`); ако излезе, е под редовете с истинска Чайка |
468: | 4 | `бл 11 чайка` | само блокове в полигоните к.к./кв. Чайка; Студентска бл. 11 не е сред тях |
469: | 5 | `левски битоля 13` | без квартална дума, вторият ред е **„район Приморски“**; „левски“ не дава пълно съвпадение |
470: | 6 | `цветен квартал битоля` | намира (свидетелят работи), нито един ред не показва „Цветен квартал“ като квартал |
471: | 7 | `бреза 6` | заглавие **кв. Левски**, свидетелят остава търсим |
472: | 8 | `манастирски рид` / `акчелар` / `ален мак` / `бриз` | фините подписани квартали, не „кв. Виница“ |
473: | 9 | `дълбокото дере` | продължава да намира (Р38 „добавя, никога не реже“) |
474: | 10 | `27 юли 22` · `алеко константинов 10` | Център (ако вътре) · кв. Тракия |
475: | 11 | **ред по display_id пътя** (напр. `константин и фружин бл 302`) | заглавието носи квартала И ориентира; при материализация (Р12-б) няма „ж.к. Бриз, акчелар“ |
476: | 12 | `дружба бл 11` / ТВ кула | по подписания Р5; редът не изчезва |
477: | 13 | `ADDRESS_PATH_V2 = false` | поведението е базовото; нито един нов низ не се показва |
478: | 14 | празна проверка | конзолата без грешки; `data/search_index.json` 200; картата под 3 s; трите режима; PLACES взима Enter само при `'Няма съвпадения'` |
479: | 15 | смяна на поколението | при подменен `address_rows` клиентът **отказва** доставката (fail-closed); стар кеш v2 не се сервира на страницата |
480: 
481: ---
482: 
483: ## 9 · Рискове и дългове
484: 
485: 1. **Смяна на собственика на Enter** — когато свидетелят спре да удовлетворява квартален филтър, някои заявки минават към PLACES (`:7508-7527`). Фикстура в двете посоки в G-B4.
486: 2. **Подредбата ще се раздвижи** (`:5252-5253`) за 19 494 записа; делтата се обяснява в replay-а.
487: 3. **Блоковите колизии се преизчисляват**; М0.7 е задължителната преди/след мярка.
488: 4. **Записи, които губят кварталната си дума** — при Р5(в) са само неопределените класове; при Р5(а) са ~25 613 повече. Съзнателна цена, не изненада.
489: 5. **Латиницата (31 916 етикета)** е отделен лот (ADR 007 D5.2) върху същите редове: първо кварталът, после латиницата.
490: 6. **Регистърът е тесен, не полигоните** — `parent` за 6 от 60; ~2 985 записа остават неопределени заради това. Сутрешен списък.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$l=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md' -Encoding UTF8; for("'$i=490;$i -lt $l.Count;$i++){ '"'{0}: {1}' -f ("'$i+1),$l[$i] }' in C:\git\Fire_Varna
 succeeded in 688ms:
491: 7. **Полигони, които не раздават нито едно име** — броят зависи от подписания Р5 (при §4.1-строгия прочит на v1 бяха 15, при §2-прочита 11); финалният брой е ПОДПИСАНО очакване от М0.5.
492: 8. **Дупките Център / Цветен квартал / Колхозен пазар** остават отворени.
493: 9. **Replay-ът е нов двигател** — разсинхронизиран срез трябва да пада шумно (`AssertionError`).
494: 10. **Двата адресни блоба нямат sha пин от край до край в клиента**; този лот стеснява дупката през манифеста (G-B3), пълният пин е дълг.
495: 11. **Approx пакетът** ще внесе написаната дума наново, ако бъде запален без резолвера.
496: 12. **Червената база** — днес `run_gates` exit 1 и 24/342 паднали; адресният интервал по G20 трябва да е различим.
497: 13. **`PROTECTED_CACHES` (`sw.js:46`) остава да сочи `fire-varna-search-v2`** — след v3 това е мъртъв ред и старият кеш лежи, докато браузърът не го изчисти. Не се пипа тук (§0.12) → сутрешен списък.
498: 14. **Написаният свидетел е 58 % OSM `nearest_point`** (флагманът — на 707 m). Това е аргумент да не е авторитет никога, и колона `source` в леджера; не е повод да се маха от търсенето.
499: 
500: ---
501: 
502: ## 10 · Какво НЕ се пипа
503: 
504: - `Varna_buildings/config/quarter_registry.json` и `REGISTRY_SIGNED_SHA256` (`js/lib_quarter_registry.mjs:45-46`); `lib_quarter_registry.mjs` (Д10).
505: - `Fire_Varna/data/address_rows.json` като съдържание (ADR 007 D2).
506: - **`Fire_Varna/sw.js`** (недосегаем по `006:158` и `007:13`; освен това промяната е без ефект — `sw.js:104-106`).
507: - `varna_3d` — нула комита.
508: - Стейджнатият Б3 write-set (14 пътя, вкл. `gates/probe/b3_g11.py` и `tests/test_b3_gates.py`) — освен ако Петър не подпише Р18 вариант „разширяване на `ALLOWED_NEW`“.
509: - `PRIVATE_KEYS` (`test_fire_varna_publish_gate.mjs:62-68`) и `FORBIDDEN_SUBSTRINGS` (`:101-104`).
510: - `SHA_PINS` (`index.html:6291-6293`, `gates/run_gates.py:68-72`); `SIGNABLE` (`gates/release.py:177-185`) — освен новата секция в `expectations.json`.
511: - `'Няма съвпадения'` (`index.html:5430`), класът `.asr-item`, `APPROX_ADDRESS_SEARCH_ENABLED` (`:5926`).
512: - Атрибуционните низове и `tests/test_b3_gates.py:43-44`.
513: - Подразбиращият се път `npm run build:fire-varna`.
514: 
515: ---
516: 
517: ## 11 · Отхвърлени находки (с измерената причина)
518: 
519: 1. **„М0.1 е противоречие 05f485e ↔ 6486b48“ (находка на v1, оборена от gates/semantics/delivery — приема се ОБОРВАНЕТО, отхвърля се находката на v1).** Двамата опровергатели измериха един и същ блоб (`rev-parse` OID `82706fb5fef494175f912db82a871a6c38b4e472`, 301 917 B, sha256 `c1551d24…871b3`) за двата комита. В v2 пинът е OID, а СПИРАЙ по т. 1 отпада.
520: 2. **semantics: „Планът отменя ADR 010 D6/D7/D8“ — ОТХВЪРЛЕНО КАТО ФОРМУЛИРОВКА.** Проверено в `docs/decisions/010_signed_quarter_boundaries.md:48-52`: D6 урежда канала `SIGNED_POLYGON` в `varna_3d/src/fire_varna_locations.py` (между ред 873 и 875) за **375-те места**, с гейтове в `qa_fire_varna_m6.py:304-308`; той не се произнася за адресния индекс, който се строи в друго репо, от друг конвейер, за друга повърхност. Затова „отмяна на подписан прецедент“ не е точно. **Задължението обаче е прието:** ADR 064 изрично изброява трите разминавания и казва, че ADR 010 остава непроменен за местата (Р6-б). D8 (геометрично доказано дете ⊆ родител) се приема ДОСЛОВНО и влиза в резолвера.
521: 3. **semantics, „бонус“ към Битоля: „§1.А твърди, че Битоля носи `qtk = tsveten kvartal`“ — ОТХВЪРЛЕНО.** v1 §1.А цитира СКАУТ 3 §9, който дава ЕДИН пример („ул. Битоля 11, `qtk=tsveten kvartal`“), а не разпределение; същият СКАУТ в §3 брои `tsveten kvartal → кв. Левски` 318. Планът никога не е твърдял „всички Битоля са tsveten kvartal“. **Приета е обаче основната част:** районът в Р13.3/§8-5 е **Приморски**, не Одесос — `district_names` е проверен от Planner-а сега.
522: 4. **gates, ПОПРАВКАТА за G-B2 („мутирай реалния път `data/search_index.json`, върни го след теста“) — ОТХВЪРЛЕНА КАТО МЕТОД.** Проверка 1 чете работното дърво (`run_gates.py:141-147`), а `release.worktree_differs` (`:313`) третира „modified/staged/untracked“ еднакво — мутиране на доставен tracked блоб по време на гейт-кръг може да влезе в подпис. Прието е ТВЪРДЕНИЕТО (фикстурата днес е зелена по конструкция) и е реализирано другояче: проверка 3 чете блоба (`git show :<path>`), списъкът се параметризира за теста, а липсващ файл става червен.
523: 5. **delivery, „G-A1 никога не може да се съгласи с извора“ — ЧАСТИЧНО ОТХВЪРЛЕНО.** Пре-стъпката на v1 вече хвърляше при несъответствие на sha, тоест повреден копие би паднал шумно, а не тихо. Прието е реалното ядро: **пинът, изчислен през PowerShell пайп, е артефакт на обвивката** — затова в v2 всички байтове се четат в Python и пинът е OID.
524: 6. **Числата, които двамата опровергатели дават различно, не са отхвърлени, а изпратени на М0** (11 641 ↔ 11 625; 24 ↔ 16 неразличими групи; 385 ↔ 91 ↔ 95 блока „11“; 1 324 ↔ 213 без улица; +1,26 ↔ +1,54 MB). Планът не може да носи две числа за едно нещо; М0 е единственият им източник, а разминаването е СПИРАЙ (§7 т. 1 и 3).
525: 
526: ---
527: 
528: ## 12 · Оборване (какво казаха трите опровержения и какво е приложено)
529: 
530: **Опровергател „gates“ — присъда НЕГОДНО.** 8 блокера, 6 мажора, 4 минора.
531: Приложени блокери: флагманът пада под собствената политика → **нов Р5 с вариантите (в)/(г) + G-A3-г с поименна фикстура**; М0.5 е измеримо днес и оборва Р5в → **фалшивият праг 15 % махнат, вариантите носят измерените си цени**; `wtk ∩ qtk = ∅` срещу „свидетелят винаги“ → **Р14-а (изваждане)**; G-A6а без зъби → **подписан ПОД + затворен списък причини**; G-A6б червен върху данните → **Р9-б (втора степен + подписан списък изключения)**; ориентирът не стига до 205-те реда → **Р15 (структурно поле `o`)**; G-B5 извън среза → **`validateSearchPayload` вътре в среза + собствен гейт-ред**; корпусът без селектор и без freeze → **`address_corpus_build.py --freeze` + команда в §5.Д**.
532: Приложени мажори: противоречието §2 ↔ §4.1 за `inside_clear` → **една дефиниция в §2 + Р5**; класът „извън, но в лентата на един“ → **Р5-д + Р14-б**; фикстурите на G-B2/G-A2 ф1 → **блоб-четене, липсващ файл = червено, затворено топ-ниво, фикстура на топ ниво**; `stk` пренарежда груповия режим → **`otk`, извън `_areaVocab`**; гардът от наблюдавани `qtk` → **речник от `quarter_names`**; §0.10 ↔ §5.Г → **изравнени (Б3 се комитва пръв)**; G-B1 → **Р18 (собствен пробен файл) + истински родител**. Минорите за качеството на ориентира (Р11-б), фантомния М0.1, `git push` и регистрите по display_id пътя — също приложени.
533: 
534: **Опровергател „semantics“ — присъда НЕГОДНО.** 5 блокера, 8 мажора, 3 минора.
535: Приложени: флагманът (дублира gates) → същият Р5/G-A3-г; „Р5в е мъртъв при раждане“ → **преписан Р5**; **вторият дисплей път пак показва противоречивата дума (2 775 реда) → нов Р12-б с материализация и измерена цена** — това беше най-скъпата пропусната пробойна на v1; G-A4 без зъби (публикационният гейт не чете полигони) → **полигонният вход влиза в гейта + ф6**; G-A6б неизпълним → Р9-б.
536: Мажори: собствената улица не се извлича за 82,5 % (`STREET_TYPE_RE:39`, `extractStreet:106-126` — проверено) → **Р10 с две дефиниции и подравнен Р13**; `_areaVocab` 88 → ~600 → Р15; Р12 занижен размер → **Р12-в с подписан таван**; грешният район на Битоля → **Приморски**; ориентирът и 581-те реда → Р15; отношението към ADR 010 → **Р6-б (с корекция на формулировката, §11.2)**; свидетелят не е „кадастралната дума“, а 58 % OSM `nearest_point` (флагманът на 707 m) → **преименуван навсякъде + колона `source` в леджера**; G-B1 → Р18; `sw.js` промяната без ефект → **`sw.js` изобщо не се пипа**. Минори: М0.1, М0.3 (четири дефиниции), голите цифри в каноничните токени → **Р16** (проверено срещу 60-те имена).
537: 
538: **Опровергател „delivery“ — присъда НЕГОДНО.** 4 блокера, 9 мажора, 2 минора.
539: Приложени блокери: **лотът е забранен от ПРИЕТ ADR 006 D12 и разрешен само от НЕПОДПИСАН ADR 007, а v1 не искаше този подпис → нов Р0 + Р0-б (kill switch)** — това е най-тежката управленска пробойна на v1; PowerShell разваля байтовете (`>` → UTF-16LE) → **пин по OID, четене в Python**; `python -m gates.sign` без аргументи пада, а редът подпис→freeze→run_gates дава червена проверка 6 → **пренаписан §5.Д**; ориентирът убива C2 етикета (`TYPEWORDS:457-458` няма „do“; `resolveC2BlockLabel:617` е fail-closed; `entryTokenSet:481-487` чете `e`, не `o`) → **Р15: ориентирът напуска `label` изцяло**.
540: Мажори: подписваният низ ≠ низът на Р10 → **Р10 + Р13 подравнени**; базата зад Р11 е сгрешена → **М0.6 + СПИРАЙ**; `_areaVocab` флип → Р15 + фикстура (iv) в G-B4; 205-те реда → Р15; **`git add index.html` би внесъл хънковете на Б3 → §5.0 + STOP т. 14**; `sw.js` недосегаем → §0.12; Р12 занижен размер → Р12-в; G-B1 → Р18. Минори: М0.1; преименуването на опашката е ход на Б3 (проверено: `b3_g11.py:44` вече изброява `архив/АРХИВ_A_05.09.md`) → §5.Г.
541: 
542: **Общо:** приети 17 блокера (след сливане на дублиращите се), 23 мажора; отхвърлени/преформулирани 5 находки и 1 предложена поправка (§11); 6 числови разминавания са изпратени на М0 с изричен СПИРАЙ.
543: 
544: ---
545: 
546: **Gate 1:** планът чака думата на Петър по **Р0–Р18** и по класа 🔴. Без подпис Изпълнителят не пише нито ред. Публикуването е негово.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git diff f745349 --numstat -- 'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md'" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$l=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md' -Encoding UTF8; for("'$i=233;$i -lt 241;$i++){ '"'{0}: {1}' -f ("'$i+1),$l[$i] }; $m=Get-Content -LiteralPath '"'AGENTS.md' -Encoding UTF8; for("'$i=150;$i -lt 272;$i++){ '"'{0}: {1}' -f ("'$i+1),$m[$i] }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$f='"'docs/decisions/007_address_path_v2.md'; "'$l=Get-Content -LiteralPath $f -Encoding UTF8; for($i=0;$i -lt [Math]::Min(145,$l.Count);$i++){ '"'{0}: {1}' -f ("'$i+1),$l[$i] }' in C:\git\Fire_Varna
 succeeded in 409ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied

 succeeded in 635ms:
234: **Р14 · Гардът на свидетеля.**
235: *Препоръка:* (а) `wtk` = написаните токени **МИНУС** каноничните на същия запис (иначе инвариантът `wtk ∩ qtk = ∅` пада на първия билд — ~4 588 записа имат съгласна дума); (б) речникът за „изричен квартален филтър“ се строи от **`quarter_names` (всичките 60 канонични имена)**, не от наблюдаваните `qtk` — иначе кварталите, които не са раздали нито едно име, нямат гард и „ж.к. Дружба, бл. 11“ остава пълно съвпадение през свидетеля.
236: **Р14-б · Обхват на гарда:** гардът гаси свидетеля САМО за записи с **`q != null`** (има канон, който му противоречи). Записите с неопределен канон (в т.ч. Р5-д) запазват силата на свидетеля, но с демотиране `wdem`. Така „чайка студентска бл 11“ не е пълно съвпадение, а „бл 11 левски“ все пак връща блока на бул. Царевец.
237: 
238: **Р15 · Ориентирът е СТРУКТУРЕН, не в `label` и не в `stk`.**
239: *Довод 1:* `resolveC2BlockLabel` (`:609-619`) е fail-closed по `s9Inconsistency`, а „до“ **не е в `TYPEWORDS` (`:457-458`)** → етикет „бл. 11, до ул. Мир“ с чужда улица дава `streetMissing === streetTotal` → `token_inconsistent` → етикетът се ИЗХВЪРЛЯ. *Довод 2:* `entryTokenSet` (`:481-487`) чете геокодерния `e`, а `o.stk` се пише на `:723` върху публичния обект — спасяването „през stk“ на v1 не работи без мутиране на `e`. *Довод 3:* `_areaVocab` (`:5151`) се храни от `stk` → ~306 нови улични имена биха превключили цяло семейство заявки в груповия блоков клон (`:5278-5288`).
240: *Препоръка:* ново поле `o` (индекс в топ-ключ `orientations[]`) + нови токени в **`otk`** (в postings и vocab, **НЕ в `_areaVocab`**), с демотер `otdem = 1`, ако поне един токен на заявката е съвпаднал **само** през `otk` (per-token, не `matchedCore === 0` — иначе демотерът е мъртъв, както е `sdem` при блокови заявки). Така: (1) `label` не се пипа → C2/S9 остават непокътнати; (2) ориентирът стига и до двата дисплей пътя (включително 205-те блокови реда без `label`); (3) „студентска бл 11“ не сменя клона на рендера.
241: 
151: 
152: | Role | Agent | What it can do | What it cannot do |
153: |---|---|---|---|
154: | **Planner** | Claude Code (Opus, read-only) | Read the repo, measure, draft plans, architect, audit | Edit tracked files, commit, push |
155: | **Researcher** | Claude Code (Opus, read-only) | Planner sub-phase: gather evidence and measurements | Edit files, decide architecture |
156: | **Executor** | Claude Code (Opus) | Implement the Petar-signed plan, edit files, create local commits | Architect, expand scope, push |
157: | **Auditor** | Claude Code (Opus, read-only, adversarial) | Independently verify the Executor's diff against the plan | Edit files, push |
158: | **Orchestrator** | Petar | Sign plans (Gate 1), review diffs (Gate 2), push to remote | — |
159: 
160: **Petar = orchestrator and sole push authority.** All architectural and data decisions go through him. Chain: `Planner → GATE 1 (Petar signs) → Executor (local commit) → Auditor → GATE 2 (Petar reviews diff) → Petar pushes`.
161: 
162: Approval gates:
163: 
164: - **Architecture changes** (file layout, module split, new patterns) -> Planner discussion + ADR first.
165: - **Data source changes** -> fresh Planner analysis required.
166: - **UI label / wording changes** -> Petar approval.
167: - **New runtime or build-time dependencies** -> Petar approval.
168: - **Refactoring scope** -> Planner plan (signed by Petar) + Petar approval before edits.
169: 
170: ### Planner Plan Preamble Checklist
171: 
172: Every Planner plan/proposal must include: request scope, deterministic inventory, files read, negative-findings matrix, quoted declared metadata, decision ledger, approval-gate check, and open questions.
173: 
174: Decision ledger schema:
175: 
176: | Decision | Source | Evidence | Reversibility | Approval status |
177: |---|---|---|---|---|
178: | Worker source extracted to `worker/` (`914dc2a`) | Repo evidence | `worker/` holds the Worker source + README; deploy version repo-declared `5accc88e` | Reversible by reverting the extraction commit | Existing approved project state |
179: 
180: ---
181: 
182: ## System Invariants
183: 
184: These are non-negotiable and apply to every agent, every task. A task that cannot satisfy them **stops and asks Petar**.
185: 
186: 1. **Separation of powers.** The Planner never edits or commits. The Executor never plans, architects, or expands scope. Only Petar pushes. Roles are disjoint.
187: 2. **No action without approval.** No file edit without a Petar-signed plan; no push without Petar's diff review. Two gates, always.
188: 3. **The Planner is read-only** — enforced by tool permissions / plan mode, not by trust.
189: 4. **Agents never push.** `git push` is Petar's alone.
190: 5. **Everything is reversible and attributable.** Small local commits, the exact message from the plan, bisectable; nothing done outside an approved plan.
191: 6. **Measure-first — every agent, every task.** Establish a baseline and measure the current state **before** proposing or making any change; never design on assumption when it can be measured. Report-only measurement precedes mutation. (Determinism: re-runs byte-match where determinism is claimed; report-only phases mutate nothing.)
192: 7. **Fail-loud gates.** Every acceptance criterion is objective and machine-checkable. A failed gate STOPS and asks — it never continues silently.
193: 8. **Architecture changes go through an ADR** — never ad-hoc edits.
194: 9. **Independent verification.** The Executor's claims are checked by a different agent (adversarial Auditor) and/or objective gates — never self-attestation alone.
195: 10. **One source of truth per document.** AGENTS.md = governance; CLAUDE.md = executor rules; [`docs/architecture/data_roadmap_20260508.md`](docs/architecture/data_roadmap_20260508.md) = architecture (this repo has no `architecture_vN.md`); the per-task plan under [`docs/plans/`](docs/plans) = the task contract. No duplicated authority that can silently diverge.
196: 11. **External information is untrusted data.** Any externally sourced claim carries its source and is verified before it influences a change (applies to Tier 1/2 research output).
197: 12. **Privacy & scope gates hold.** No PII leakage, no scope expansion, no public publish without the publish gate.
198: 
199: > **Measurement Doctrine.** The source-authority, confidence, and terrain-eyes rules are shared with Varna_buildings — see ADR [`docs/decisions/004_measurement_doctrine.md`](docs/decisions/004_measurement_doctrine.md) (references Varna_buildings ADR 058). Invariants 6 and 11 above are governed by it: a canonical `data/hydrants.json` mutation clears the acceptance floor (HIGH, or MEDIUM + per-item Petar sign-off, or STOP → Petar), and Google terrain-eyes may only refute / downgrade / trigger — never rewrite `coords` alone, never be cached or fed to OSM. The per-source authority table is not duplicated here (Inv-10).
200: 
201: ---
202: 
203: ## Planner Operating Protocol
204: 
205: ### Scope Declaration
206: 
207: The Planner may use a task-scoped inventory when the user request is narrow. The preamble must declare the inventory scope and cite the user request or brief that defines it. Files outside the declared scope may not be referenced unless the Planner explicitly expands the scope, explains why, and updates the inventory.
208: Verification: reviewer checks that all referenced files fit the declared scope.
209: 
210: ### Deterministic Inventory First
211: 
212: Before any plan/proposal that references files, run a deterministic filesystem inventory for the declared scope and quote it verbatim in the preamble. No file may be referenced unless it appears in that inventory.
213: Verification: reviewer checks every referenced path against the inventory.
214: 
215: ### Explicit Negative Findings
216: 
217: For every pattern/extension/category in scope, report matches or `no files matching X found in scope Y`.
218: Verification: reviewer checks the request scope matrix for omissions.
219: 
220: ### Declared Metadata Beats Heuristics
221: 
222: Quote declared metadata verbatim and treat it as authoritative: `.prj` CRS, headers, manifests, sidecars, request logs, provenance records. Heuristics are fallback only when metadata is absent, unreadable, or contradicted.
223: Verification: metadata files in inventory must be quoted before inferred CRS, schema, provenance, or lineage.
224: 
225: ### Binary File Reading Rule
226: 
227: Referencing a binary/source archive requires content inspection, not filename inspection. KMZ means unzip/list archive and inspect inner KML/doc.kml. DBF/SHP means inspect schema and metadata with `ogrinfo -al -so` / `ogrinfo -al` from GDAL, QGIS equivalent tooling, or a documented DBF/SHP parser. If required tooling is unavailable, state the file is unread and do not infer its contents.
228: Verification: plan lists tool used, command, and inspected inner files/layers.
229: 
230: ### Referenced Files Must Be Read
231: 
232: If a file is referenced, its content must have been read in the same session. Path-name matching is not reading. Preamble must list `Files read`.
233: Verification: reviewer compares referenced paths against `Files read`.
234: 
235: ### Non-ASCII Encoding Gate
236: 
237: Before committing or handing off files containing non-ASCII text, especially Cyrillic, verify UTF-8 round-trip integrity and scan for mojibake.
238: 
239: Per-file detection form:
240: `Select-String -Path <path> -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8`
241: 
242: Note: this regex uses Unicode escape notation (\u00D0 = Ð, \u00D1 = Ñ, \u00C2 = Â) rather than literal characters so this proposal file passes its own mojibake scan. When invoking the scan from a shell, either form is functionally equivalent.
243: 
244: Repo-wide pre-commit detection form:
245: `git diff --cached --name-only --diff-filter=ACMR | ForEach-Object { Select-String -Path $_ -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8 }`
246: 
247: Also recommend adding `.editorconfig` with `charset = utf-8` and a git pre-commit hook that blocks staged text files containing mojibake markers.
248: Verification: handoff notes include encoding check output; reviewer may rerun the command or hook.
249: 
250: ---
251: 
252: ## Current Repo State
253: 
254: Working directory: `C:\git\Fire_Varna`. Tracked top-level entries, as `git ls-files` reports them. Per-folder file counts are state, not rules — they are not carried here; read them from `git ls-files` when you need them:
255: 
256: ```text
257: C:\git\Fire_Varna\
258: ├── index.html                     <- current app shell
259: ├── data/                          <- runtime hydrant data (hydrants.json — record count in
260: │                                     docs/activeContext.md; hydrants_provenance.json;
261: │                                     search_index.json + address_rows.json, built in Varna_buildings)
262: ├── scripts/                       <- ingest / migration / backfill tooling
263: │   ├── apply_approved_reports.py
264: │   ├── migrate_to_verbose_schema.py
265: │   ├── backfill_addresses_20260511.py / backfill_verified_type_20260509.py
266: │   ├── replay_historical_new_hydrant.py
267: │   ├── import_etr_kmz.py          <- ЕТР KMZ register adapter
268: │   ├── copy_basemap_release.py / vendor_basemap_deps.mjs
269: │   └── lib/hydrant_core.py        <- H1 shared core (spatial dedup)
270: ├── tests/                         <- unittest suite (test_hydrant_core.py,
271: │                                     test_apply_approved_reports_parity.py, golden fixtures);
272: │                                     verify_apply.py / verify_h4.py — one-off checkers (Р-21 of the 01.09 plan)

 succeeded in 650ms:
1: # ADR 007 — The address path and its delivery: a signed write-set, a differential G3 and a kill switch
2: 
3: **Status:** Proposed — awaiting Petar (Gate 1). · **Date:** 2026-09-03. · **Amends:** ADR 006 D4 and D12 (the named untouchables) for one enumerated write-set only; everything else in 006 stays in force. · **Plan:** `docs/plans/recommendations_2026-09-03.md` §3 (ЛОТ 2 „Адресният път и доставката му"), decisions 3, 5, 15, 16, 17, 18, 19 of `docs/audits/ОДИТ_03.09_система.md` §7. · **Attacks that shaped it:** Sol (`scratch/audit_2026-09-03/sol_verdict_2.md` §4–§6 — the contract below is his, accepted almost verbatim), the judge panel (`judges_summary.txt`, cost/risk lens), Kimi (data lens on the labels).
4: 
5: ## Context
6: 
7: The system audit of 03.09 measured the address path — the search every call goes through — for the first time (`ОДИТ_03.09_система.md` §10.4): over a deterministic sample of 3 470 queries against the live engine, a plain address (`kind:address`) reaches the exact record in the top 8 only 16.8 % of the time, while the *label* is found 94.1 % of the time. The cause is not the matcher: 71 100 of 86 232 records (82.5 %) share their label with another record, the first row is another pin under the same text in 75 % of the cases (median 461 m away, p90 2 710 m), and `dedupeDisplayRows` folds equal labels after the cut to 8. Three more facts belong to the same path: 31 916 records (13 683 of the 25 343 unique labels, 54 %) reach the firefighter in Latin because the build writes the cleaned `addr_key` as `label` and the UI prefers `label` over the Cyrillic `address_rows` text; the type word the app itself prints („кв.", „ж.к.") throws the target out of the list (removing it from the query: +7.8 points @1 over 694 labels, 84 improved / 4 worse); and the address renderer has no „…и още N" tail, so 8 of 984 equal candidates look like the complete answer. ADR 006 D12 forbids every function of `initAddressSearch` and pins `data/search_index.json` byte-for-byte; G3 is defined as byte-equality of the address-search probe corpus. None of the fixes above is possible under that contract — and Sol showed that even the „one line in the build" for the Cyrillic labels changes the pinned `search_index.json`, so the amendment is a precondition for the *data* fix too, not only for the code.
8: 
9: ## Decision
10: 
11: **D1 — Scope of the amendment.** D4/D12 of ADR 006 remain in force outside the write-set enumerated here. The amendment enters *before* the first change of ЛОТ 2 (data or code). Nothing else in 006 changes: the places IIFE keeps its own contract, gates and kill switch.
12: 
13: **D2 — Data write-set (Varna_buildings → Fire_Varna).** `js/build_fire_varna_search_index.mjs`, `js/test_fire_varna_publish_gate.mjs` and the generated `Fire_Varna/data/search_index.json` (with a new `generation_manifest.json`). Untouchable: `data/address_rows.json`, `sw.js`, `worker/`, the hydrant / report / compass paths, `data/approx_addresses_v1.json`.
14: 
15: **D3 — Address write-set (Fire_Varna `index.html`, inside `initAddressSearch`).** Only: the flag and its helpers, `dedupeDisplayRows`, `runGeocoderSearch` (the dedupe-before-cut and the query dispatch), `buildExactItem`, `renderResults`, `renderCombined`, and one named renderer for the block warning. Pinned (still forbidden): the scorer and comparator, `selectResult`, click/Enter navigation, the detail fetch, the exact-coordinate path, every other function and every `asr-*` / `search-pin*` selector.
16: 
17: **D4 — Kill switch `ADDRESS_PATH_V2`.** A selector at each of the use sites in D3 — never an early `return` at the top of the IIFE (that would remove the address search). With `ADDRESS_PATH_V2 = false` the DOM, the backing identity, the selection and the failure/race behaviour are byte-equal to the signed post-ЛОТ-2 baseline; with `true` only the differential G3 differences enumerated in D6 are allowed — any other difference is STOP. Precedent: ADR 006 D11.
18: 
19: **D5 — The five changes and their exact rules.**
20: 1. *Physical-building group key* (decision 18): the delivery carries `pb = HMAC-SHA256(secret, "vpb1|" + private_pbid)` rendered as `b` + 16 lowercase hex — a separate domain from `g`, never a raw or bare-hashed cadastral id (the raw `physical_building_id` is `min(member cadnum)`); a public-safe representative map `pbr: pb → _ord` (or a marker on the representative row); `PB_KEY_RE` + type/shape check + dotted-cadnum poison fixtures in the publish gate; snapshot gate (today 483 stamped rows / 198 groups: 420 `mf` + 63 `address`, never `en` or parcel); two builds with the same inputs are byte-identical; churn gate over the private sorted member sets — split / merge / migration / representative change is STOP until a signed migration manifest. `PRIVATE_KEYS` and `FORBIDDEN_SUBSTRINGS` stay untouched; only `pb` (and `pbr`) enter `ALLOWED_ENTRY_KEYS`.
21: 2. *Cyrillic labels* (decision 5): a late selective pass in the build after F3 (lines ~806 and ~826): emit `display_id` wherever `address_rows` has the row, and drop `label` only where the Cyrillic row is at least as informative — with an exact old→new ledger, the F3 block labels (196 rows) kept, and a quality gate that fails on empty / letterless / ≤3-character / less-informative labels (Sol measured 11 813 shorter and 17 letterless results under a naive flip — those keep `label`). „Адрес:" prefixes (522 labels) are cleaned in the same build. The UI preference in `baseAddressLabel` follows the data (step 2 before step 1 where `display_id` exists).
22: 3. *Dedupe before the cut and the tail* (decisions 3, 17): `R` = the full ranked set after physical/block grouping; `D = dedupeV2(R)` with the key `norm(label) + '||' + g + '||' + pin(5 dp)`; `V = D.slice(0, limit)`; `N = |D| − |V|` rendered as „…и още N" — a tail node without `data-idx`, not selectable, not in `currentResults`.
23: 4. *Type word as a second-pass fallback* (decision 15): only on the raw query, only when the legacy path has no clean all-token hit, only for the enumerated set „кв./ж.к./к.к./в.з." + „Адрес:" + „·" — never „ул./бул./пл." (38 street names exist both as „ул" and „бул"), never on the index or the label („кв. Чайка" and „к.к. Чайка" stay distinct).
24: 5. *Differentiator* (decision 16): each row may carry a deterministic meta text „distance · bearing" from the operational anchor `lastFix` (GPS fix, manual pin, or the previously selected address); no anchor → no suffix; `map.getCenter()` is never a fallback; rank, identity, click, Enter and navigation do not change. Plus one named renderer: when a block has sections but the requested entrance is not labelled, the row says „входовете на този блок не са етикетирани" instead of silently returning the block pin (decision 19).
25: 
26: **D6 — G3 becomes a differential replay.** The corpus: fixed payload hashes, browser/viewport, cache state, a fixed WGS84 anchor injected before every headless query (and a separate no-fix series expecting zero suffixes), the nine original G3 queries, the 3 470-row engine corpus of the audit, and targeted series (`pb` groups, >200 m label groups, Чайка/к.к. Чайка, bare block + entrance, no-GPS). The proof: full `outerHTML` + backing identity (pin, `g`, nav coordinates, popup title, selection side effects) for every visible row. Allowed differences, and only these: (18) folding of members of a signed `pb` group to the signed representative; (3) the same label/g appearing at a different exact pin, relative order of old identities preserved; (15) only the signed diff when the fallback fires; (16) only the deterministic meta text; (17) `N = |D| − |V|`. Everything else is STOP.
27: 
28: **D7 — Order inside the lot.** ADR (this document) → the build (2, 1 with the privacy contract, the manifest, the publish gate with the new readability and privacy checks) → the client (4 → 3 → 5 → 4 with the flag) → the harness before/after (`kind:address` recall @8 from 16.8 % upward with 0 worsened labels; the type-word A/B re-measured after the Cyrillic labels, because the 694-label sample will grow by ~39 000 rows) → audit → Gate 2.
29: 
30: ## Consequences
31: 
32: - The address path gets, for the first time, a kill switch and a differential contract; the price is one signature on this ADR and the loss of byte-equality as the definition of G3.
33: - The delivery grows by `pb`/`pbr` (~200 KB raw) and loses ~900 KB of Latin labels where the Cyrillic row replaces them; the gzip gain is small (~20 KB, Sol) — the point is readability, not bytes.
34: - Every step is reversible: the flag for the client, the manifest for the data, `git revert` per commit.
35: 
36: ## Rollback
37: 
38: `ADDRESS_PATH_V2 = false` restores the signed post-ЛОТ-2 baseline without a revert; the data change reverts with the commit that carried the new `search_index.json` (the old manifest is kept in `Varna_buildings/output/fire_varna_baseline/`).
39: 
40: ## Obligations
41: 
42: 1. Sign this ADR before any file in D2/D3 is touched (Petar, Gate 1).
43: 2. Re-measure decision 15 after the Cyrillic labels; re-measure the 545 label groups >200 m after `pb` (Sol: `pb` alone resolves none of them — 3 is evaluated independently).
44: 3. The frozen G3 baseline (`scratch/places_search/probe_out/before.json`) is re-frozen once, in its own commit, after the build lands and before the client changes.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$l=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md' -Encoding UTF8; "'$hits = for($i=155;$i -lt 249;$i++){ if($l[$i] -match '"'"'^'"\\*\\*(Р\\d+(?:-[абвгд])?)\\b' -or "'$l[$i] -match '"'"'^- '"\\*\\*(Р\\d+(?:-[абвгд])?)\\b'){ '{0}: {1}' -f ("'$i+1),$Matches[1] } }; $hits; '"'DECISION_ROWS '+"'$hits.Count' in C:\git\Fire_Varna
 succeeded in 630ms:
160: Р0
163: Р0-б
166: Р1
169: Р2
172: Р3
175: Р4
178: Р5
190: Р5-д
193: Р6
196: Р6-б
199: Р7
202: Р8
204: Р9
207: Р9-б
210: Р9-в
212: Р10
216: Р11
219: Р11-б
222: Р12
225: Р12-б
226: Р12-в
228: Р13
234: Р14
236: Р14-б
238: Р15
242: Р16
245: Р17
247: Р18
DECISION_ROWS 28

codex
Има потвърдени блокери: флагът за изключване не може да възстанови старото поведение след загубата на старите полета; посочената Б3 опашка липсва; описаната клиентска валидация не доказва общо поколение на двата адресни файла. Уточнявам точния път за подписи и замразяване.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$f='"'docs/decisions/010_signed_quarter_boundaries.md'; "'$l=Get-Content -LiteralPath $f -Encoding UTF8; for($i=40;$i -lt 125;$i++){ '"'{0}: {1}' -f ("'$i+1),$l[$i] }' in C:\git\Fire_Varna
 succeeded in 579ms:
41: 
42: **D3 · Къде живее геометрията и как е вързана.** Каноничен файл: **`varna_3d/data/quarters_signed.geojson`**, версиониран в git. `m6000_private` НЕ е git репо; `Fire_Varna/data/` е публичната папка и отпада по S5; **това решение стои върху предусловие 5 и не е валидно, докато G19 не покаже частно репо.** Файлът се хваща от `varna_3d/.gitignore:4` и `:23` → иска `!data/quarters_signed.geojson` **след ред 23** (М0.9). **Публикува се само `quarter: {name, code, src}` и изведеният `zone`; геометрия никога.** К5 ↔ S5: следвам S5 за РЕДА и К5 за ВЕРСИЯТА — `polygon_version` и `polygon_sha256` са ЗАДЪЛЖИТЕЛНИ в `expectations.json._meta` и в `data/place_categories.json._meta`, **никога на ред** (редът е 13/17 ключа, `index.html:6275`, `:6281`; `_meta` на доставката е затворен 9-ключов набор, `qa_fire_varna_places_export.py:62`, налаган на `:550`). **Ограничение, мерено:** `SIGNABLE` (`gates/release.py:175-183`) е затворена шесторка с пътища спрямо Fire_Varna, а `blob_at` (`:223`) чете блоб от ТОВА репо — **чужд път е недостъпен, значи геометрията НЕ може да получи ред клас „артефакт“.** Дайджестът ѝ пътува през `expectations._meta.polygon_sha256` + ред клас „въпрос“ с видимо `тяло: <sha256>` + G4 и G7. Разширяването на `SIGNABLE`/`blob_at` към чуждо репо е **съзнателно отложено за Фаза C**.
43: 
44: **D4 · Регистър ↔ полигон: три декларирани множества.** Всеки жилищен код (kind ∈ {кв, жк, кк}, ЧЕТЕН ОТ РЕГИСТЪРА, никога от литерал) попада в точно едно от `polygon` · `no_boundary` (Feature с `geometry: null`, RFC 7946, с довод и подпис) · `deferred` (`_meta.deferred`, с довод и дата, броен дълг). Липса и в трите = ЧЕРВЕНО. К7 т. 1: празен квартал носи `_meta.no_places: [{code, why, signed_by, signed_at}]`; гейтът сравнява МНОЖЕСТВА: „жилищни кодове с нула доставени реда ⊆ `no_places` ∪ `deferred`“, падайки поименно. **Ако `tsveten_kvartal` попадне в `no_boundary`/`deferred`, проверката след пуша №2 става НЕПРИЛОЖИМА и това се записва в отчета** (решение §6.28).
45: 
46: **D5 · Ново име само с ≥ 2 свидетеля (К3) и обратим път.** „Цветен квартал“: свидетел 1 = подписът на Петър; свидетел 2 = `node/9664925200` с 15 места на ≤ 900 m. Втори свидетел може да е и АГКК именувана точка (Левски и Максуда имат; М0.21), ред от пощенския указател или общинска публикация с адрес (М0.22) — по-силни от OSM възел, защото са официални. При ЕДИН свидетел името е `alias`, не код. **Отмяна:** ред клас „въпрос“ + обратен диф с двоен запис + махане на кода от петте затворени списъка в един комит на Fire_Varna; фикстура: код в доставка, който вече не е в регистъра → червено. Записът влиза през конвейера на Varna_buildings (D14).
47: 
48: **D6 · `SIGNED_POLYGON` — свидетел ранг 3 (S1/К2).** Нов канал под `REG-*` (0), `KAIS-quar` (1), `KAIS-addr` (2). ОТДЕЛЕН блок в `varna_3d/src/fire_varna_locations.py` **между ред 873 и 875** — след записа на `picked` в `out` (867–873), преди `if signed:` (875) — и **никога в цикъла `offered/ranked/conflict` (785–853)**, където `conflict` бланкира вече написано поле (`:834`, `:852`) и вкарва реда в `pending_signature`. **Шест състояния:** `confirmed` · `compatible` (деклариран родител/дете, БЕЗ замяна и без уточняване) · `disputed` · `edge_pending` (D7) · `override_noted` · `written`. Пише САМО в ред без нито един свидетел, без `pending`, извън ръба, в точно един полигон (или в декларираното дете), с `witness=[CH_SIGNED_POLYGON]` и кода в `channels[CH_SIGNED_POLYGON].ids` (`qa_fire_varna_m6.py:304-308`). Полигон-местност никога не пълни `quarter` — `classify(code) == field` (`KIND_CLASS:118`), с падаща фикстура. `_narrow` (`:907-917`) уточнява САМО вътре в полигонния канал. **`SIGNED_OVERRIDE` се пази безусловно (S1):** при 12-те подписани хотела блокът само сравнява и пише `override_noted` в леджера; никога не мени полето, никога не влиза в `signed_vs_witness`, а `CHANNEL_RANK` не получава ключ `SIGNED_OVERRIDE`. **`disputed` е ЛЕДЖЕР-САМО:** редът остава дословно както е, отива в `polygon_review`, нищо публично не се мени. Това е **обявено ОТКЛОНЕНИЕ от К2** (решение §6.4): `LOC_KEYS` са точно 3 (`index.html:6311`, `:6531-6533`), няма ключ за `winner`/`reason`, а „падане до район“ би изтрило написан от по-силен канал квартал. Таблицата на К2 е входна карта за реда в опашката; спорът се версионира (`polygon_review[i].polygon_version`). **159 е ДОПУСТИМАТА популация, не write-set.** 8-те сблъсъка не се решават от полигона.
49: 
50: **D7 · Ръбът: `max(50, precision_m)` в EPSG:32635 върху пиннати ИЗВОРНИ координати (S2 + К5).** `_meta.precision_floor_m = 50`; гейтът отказва `precision_m < 50`. Забранено е да се четат изнесените координати (`fire_varna_locations.py:968-982` прави точно това и се маха от полигонния път). Мери се И точката, И закотвеното тяло (`evidence.kais_i`); разминаване → `edge_pending`. Формулата е `shapely.geometry.shape(f["geometry"]).boundary.distance(point)` — през `shape`, защото подписан квартал реалистично е MultiPolygon. Проекция: `place_identity.make_projection()` (`:219-236`); `pyproj` 3.6.1, `shapely` 2.1.2 — нула нови зависимости. **Никакво местене, никакъв snap.** `SIGNED_POLYGON_BORDER` НЕ става публикуван `src` — **обявено ОТКЛОНЕНИЕ от К5** (решение §6.16).
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
66: **D15 · Гейт 0 преди опашката.** `ЗА_ПОДПИС_Г.md` не се ПИШЕ, преди да е зелено: `release.find_queue` е рекурсивната версия; в HEAD има точно една опашка; в `gates/allow/` има точно един json (`run_gates.py:199-217`). Архивът на опашките е **извън** `scratch/places_search`. G0 е гейт-ред на всяка стъпка, чийто write-set пипа опашка или allow-файл.
67: 
68: **D16 · Идентичности и write-set-ове.** Всеки комит носи изчерпателен write-set и дословно съобщение (таблицата е в плана §2). `Claude Architect` за планове и решения, `Claude Executor` за изпълнение, `Petar1984` само за `gates.sign`, подписаната геометрия и регистъра. Ръчният комит на Петър във varna_3d/Varna_buildings е **втори, назован клас** до амандамент №4 т. 6 и влиза като **амандамент — нов датиран файл**.
69: 
70: **D17 · Дайджестът на тялото за доставка Г.** Амандамент №11 приема вариант (а) изрично „за доставка A“. За доставка Г вариантът се **преобявява** (решение §6.5): важи (а) — несъвпадение се прощава само когато последният комит по артефакта е на `Petar1984` — и G12 проверява точно това.
71: 
72: **D18 · Написаният квартал не се променя.** След P8 всеки от **201-те** реда с написан квартал (М0.4) ЗАПАЗВА кода си. Базата „преди“ е назована: `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json`, където `<base_rev>` е `_meta.base_rev` на леджера (D10) — същата ревизия, която храни манифеста-данни. Проверката е команда с изход ≠ 0 (G17).
73: 
74: **D19 · Интервалът на замразяването е обявен, изброен и ограден.** `location_phrases` е подписана претенция в `expectations.json` (`tests/test_places_search_gate.py:464-478` я сверява с `REF.LOC_PHRASES`), а `--freeze` пренаписва очакванията едва СЛЕД подписа (амандамент №11 т. 3). Значи между F13-а и единственото `--freeze` `python -m unittest discover -s tests` е червен по конструкция. Това не е „червено по замисъл“, а **обявен интервал с гейт**: изпълнителят записва при отварянето му ТОЧНИЯ набор падащи тестове (G20), той трябва да е подмножество на назования в плана §2, всеки тест извън набора = STOP, и след `--freeze` наборът е ПРАЗЕН. Интервалът не пресича нито един гейт-ред, който твърди зелено.
75: 
76: **D20 · Затварящият документен комит.** Новите четири хеша се вписват в `docs/activeContext.md` СЛЕД пуша, в отделен комит на `Claude Architect` (Г3), който Петър пуска втори път. Локалното ≠ пушнатото за времето между двата пуша е очаквано и е назовано в §3 на плана.
77: 
78: ## Как е изпълнена всяка приета атака
79: 
80: | Атака | Къде | Отклонение |
81: |---|---|---|
82: | К1 задължителни свойства | D1 | — |
83: | К2 спорът | D6 | **ДА** — леджер-само; без `winner`/`reason`; редът не пада до район → §6.4 |
84: | К3 два свидетеля | D5 | — |
85: | К4 лицензът в лота | D2, G21 | — |
86: | К5 версия, диф, откат | D3, D7, D9, G15 | **ДА** — `SIGNED_POLYGON_BORDER` не се публикува → §6.16 |
87: | К6 нормализатор + вектори | D12 | **ДА** — уточнителят при двусмислие отложен → §6.20 |
88: | К7 празен квартал / припокриване | D4, D8 | — |
89: | S1 ранг 3 + `SIGNED_OVERRIDE` се пази | D6, D8, D10 | — |
90: | S2 ръбът | D7 | — |
91: | S3 provenance | D1, D11 | — |
92: | S4 идентичности | D12 | — |
93: | S5 атомност и „varna_3d не се приема за частно“ | D3, D13, D14 | **ДА (условно)** — канонът е varna_3d при доказано частно репо; **G19 мери преди Г2** → §6.3 |
94: | S6 четирите счупвания | D6, D8, D12, D13 | — |
95: 
96: Таблицата се сверява от одитора на Г0 (read-only) и от Кими/Astra при оборването: всеки ред има **или** непразна клетка „къде“, **или** маркер „ДА“ с номер на решение в §6; ред без едно от двете е находка. Скрипт за това не се пише — архитектът не пише код, а стойност за картата няма (решение на архитекта, §6а т. 22 на плана).
97: 
98: ## Последствия
99: 
100: **+** Петте района са доказано верни спрямо официалната граница (375/375); шест квартала получават официален полигон без нито един нарисуван връх; 12 места получават квартал с извор АГКК още преди вечерта; 159 реда без нито един написан свидетел могат да получат квартал по проследим път; 201-те написани получават второ око, чието несъгласие остава ВИДИМО и чийто код е защитен от гейт (D18); „училище цветен квартал“ и „училище св св константин и елена“ стават възможни.
101: 
102: **−** Честните цени: една вечер на Петър — по-къса след D0 (остатъкът: 26 жилищни кода без официален полигон, от които центърът няма НИКАКЪВ официален извор), но с непроверима дължина (144,80 km² изпъкнала обвивка); **единайсет негови докосвания**; 8-те сблъсъка остават `pending` и G-M6 остава изход 3 (G8); всяка нова версия е нов подпис; шест затворени списъка, три манифеста и три репа мърдат в подредена тройка; регистърът иска собствен план, собствено оборване и преподписана константа; геометрията не може да е подписан артефакт по днешния `SIGNABLE`; лицензът на „по улици“ може да отнеме CC0; обявен червен интервал (D19).
103: 
104: ## Какво НЕ е
105: 
106: Не е връщане към машинните обвивки (126 обвивки, IoU 0,13). Не е OSM като съдия. **Не е замяна на регистъра с АГКК:** официалният полигон пише само в празни редове, спорът с написан извор е видим, а суровите отговори на АГКК не се публикуват и не се проследяват преди G22. Не е сваляне на пощенския указател „за всеки случай“ — Ф0-б тръгва само с думата на Петър (11,3 MB през сателита). Не е нова зависимост — `terra-draw`/`mapbox-gl-draw` отпадат, **geojson.io също отпада** (празната подложка е входът, който роди обвивките). Не е поправка на едно училище: поправят се съюзът, префиксът, числата, посоките и 11-те сблъсъчни думи. **Не решава 8-те `pending_signature`.** Не публикува геометрия, `place_id`, `SIGNED_POLYGON_BORDER` или нов ключ в реда. Не е промяна на ADR 007 и не е ADR 009. **Съзнателно отложено, с име и дата:** разширяването на `SIGNABLE`/`blob_at` към чуждо репо и преименуването на манифестните слотове (Фаза C); `POST` в `serve.py`; `place_id` в блобовете (ADR 009, Фаза B); уточнителят при двусмислие (иска дословен текст от Петър); изнасянето на фрази за всичките 32 кода; кодовете в `_meta.deferred` — **броен дълг**, не мълчание.
107: 
108: ## Гейтове
109: 
110: Всеки ред е команда с изход ≠ 0, с назован файл и с отрицателна фикстура, която ТРЯБВА да падне преди да се пипнат данни. Планът §7 изброява всичките.
111: 
112: | # | Команда (файл) | Отрицателна фикстура |
113: |---|---|---|
114: | G0 | `python -m gates.release` (Fire_Varna) | втора опашка, **комитната** в scratch-клонинг → блок; два json в `gates/allow/` → ✗. Таблицата „Как е изпълнена всяка приета атака“ се сверява от одитора на Г0 и от Кими/Astra (ред без „къде“ и без „ДА“ + §6 номер = находка), не от скрипт |
115: | G1 | `python src/qa_quarters_signed.py` (нов, varna_3d) | 17 фикстури в `--break-me`: самопресичане · дублиран код · код извън регистъра · жилищен код извън трите множества · припокриване > `max(50, precision_m)` · деклариран родител без съдържание · дете без деклариран родител · полигон-местност за `quarter` · `method:"по улици"` без ключ · `method:"по сгради"` при `faza0_signed:false` · `basemap`/`visible_layers` = `sat` · лиценз, несъгласен с метода · липсващо задължително property · `precision_m` = 25 · разминат `approval_digest` · липсващ/празен файл = ЧЕРВЕНО · `--diff`: версия, мърдаща 3 места, и версия, мърдаща 11 % площ |
116: | G2 | `python src/qa_quarters_license.py` | `.geojson` с кадастрален низ ВЪТРЕ в координатен масив (+ доказателство, че СТАРИЯТ гейт е зелен) · `cadnum` в `properties` · `2026.09.05` червено / `2026-09-05` зелено. Поправят се `data_files()` (`:85-86`) и `walk_coords` (`:106-118`) |
117: | G3 | `python src/qa_no_cad_ids.py` | новият проследен файл е ВЪТРЕ в обхвата, не в `ALLOW` |
118: | G4 | `python src/qa_quarters_author.py` (нов): `git ls-files --error-unmatch data/quarters_signed.geojson` **и** `git log --format='%an' -1 -- …` == `Petar1984` | празен изход или непроследен път = ЧЕРВЕНО (fail-closed) |
119: | G5 | `node js/test_quarter_registry.mjs` (Varna_buildings) | регистър без преподписан `REGISTRY_SIGNED_SHA256` → червено |
120: | G6 | `python src/qa_registry_name_clash.py` (нов): 0 съвпадения в 449 `quar` + 19 813 `addr`, 0 сблъсъка на `match_key` | псевдоним, който прави стар запис двусмислен → G-ISO ✗ |
121: | G7 | четящ прогон `python src/fire_varna_locations.py` през `_check_pins` | подменен байт в `quarters_signed.geojson` / `place_identity.json` → `die` |
122: | G8 | `python src/qa_fire_varna_m6.py` → **изход 3, `fails` = 0, точно 8 `pending` (същите осем имена)** | девети `pending` или ≥ 1 `fail` = STOP. Публикацията остава забранена от Фаза A (`ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md` §A.4) и се отпушва само от Фаза D — решение §6.29. Петте нови избора се ДОБАВЯТ към `choices` (`:173-176`): `channel`, `polycode`, `edge`, `dispute`, `child`; `CHANNEL_RANK` се чете с `.get` (`:310`, `:314` днес хвърлят `KeyError`) |
123: | G9 | сверка на прегенерирания `place_identity.json` | ≥ 1 разминат `place_id`/`kais_i`/`kais_d_m` → STOP |
124: | G10 | `python src/qa_fire_varna_location_isolation.py` → 4/4 | мръднат чужд артефакт → ✗ |
125: | G11 | `python scratch/places_search/recall_sweep.py` (report-only) срещу назован изход: 140 замразени в 6 кофи + `tokens` 45 / `trigger_today` 33 (`m7_trigger_tokens.json._meta.measured`) + 0 непокрити делти; `node scratch/places_search/probe_places_fv.mjs` над 759 низа + `locationKey`; **контролните заявки се мерят ТУК, преди пуша** | нарочно разминат JS клон → паритетът пада |

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$l=Get-Content -LiteralPath '"'docs/decisions/010_signed_quarter_boundaries.md' -Encoding UTF8; for("'$i=63;$i -lt 70;$i++){ '"'{0}: {1}' -f ("'$i+1),$l[$i] }' in C:\git\Fire_Varna
 succeeded in 571ms:
64: **D14 · Регистърът е подписано тяло (S5).** `Varna_buildings/js/lib_quarter_registry.mjs:35` заключва `schema_version`, `id`, `display`, `kind`, `aliases`, `parents`; `:45` държи `REGISTRY_SIGNED_SHA256`; `:121-127` хвърля „never patch the constant to make a build pass“. Затова: (1) промяната е **СОБСТВЕН датиран план в Varna_buildings със собствен §7 (дефиниция за готово)**, минаващ през неговите Approval gates (`AGENTS.md:273-275`) **и през Кими и Astra** (§0.3), чиято присъда влиза в **собствен амандамент — нов датиран файл** в същата папка; (2) константата се преизчислява и **подписва от Петър, в негов комит**, заедно с данните; (3) `node js/test_quarter_registry.mjs` тича в кръга (G5); (4) **агент никога не пипа константата**. Преди комита: нула съвпадения на новото име в 449 `quar` + 19 813 `addr` и нула сблъсък на `match_key` (М0.14); след комита `qa_fire_varna_location_isolation.py` зелено (G6/G10) — `place_zones._registry:252-255` индексира БЕЗ вид.
65: 
66: **D15 · Гейт 0 преди опашката.** `ЗА_ПОДПИС_Г.md` не се ПИШЕ, преди да е зелено: `release.find_queue` е рекурсивната версия; в HEAD има точно една опашка; в `gates/allow/` има точно един json (`run_gates.py:199-217`). Архивът на опашките е **извън** `scratch/places_search`. G0 е гейт-ред на всяка стъпка, чийто write-set пипа опашка или allow-файл.
67: 
68: **D16 · Идентичности и write-set-ове.** Всеки комит носи изчерпателен write-set и дословно съобщение (таблицата е в плана §2). `Claude Architect` за планове и решения, `Claude Executor` за изпълнение, `Petar1984` само за `gates.sign`, подписаната геометрия и регистъра. Ръчният комит на Петър във varna_3d/Varna_buildings е **втори, назован клас** до амандамент №4 т. 6 и влиза като **амандамент — нов датиран файл**.
69: 
70: **D17 · Дайджестът на тялото за доставка Г.** Амандамент №11 приема вариант (а) изрично „за доставка A“. За доставка Г вариантът се **преобявява** (решение §6.5): важи (а) — несъвпадение се прощава само когато последният комит по артефакта е на `Petar1984` — и G12 проверява точно това.

codex
**НЕГОДНО за подпис.** [Планът](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:1) съвпада с `f745349`; текущият HEAD е `10aabba`. Потвърдени са 14 staged пътя на Б3. Нищо не променях; никакъв remote достъп.

- **S34-1 — Управленското разрешение е прекомерно и закъсняло.** D12 действително защитава адресния път, но подписването на целия 007 приема и несвързаните му D5 промени. Поправка: ограничен амандамент във Fire_Varna плюс ADR064 за генератора, подписани **преди V1/F1**, вместо оформяни чак във V11/F4. `Claude Architect` оформя решенията, `Claude Executor` изпълнява; човешките data-комити са изрично условие на лота — [D16/G4](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:68) не проверява авторството на всички данни.

- **S34-2 — Kill switch-ът няма определена възстановима база.** Четирите селектора пропускат dedupe; валидацията винаги изисква schema3, а генераторът вече заменя `qtk` и премахва етикетни сегменти (§3/§4.3). Поправка: пинната база след миграцията и селектори за всички разлики, или откат на съгласуваните клиент+данни.

- **S34-3 — Комитният ред създава счупен checkpoint.** Р.324 изисква кеш+payload в един комит, но F1 предхожда данните: schema3 клиент срещу schema2. Б3 самият има съгласувани staged пинове. Поправка: Б3 пръв след независимия му одит; съвместими подготвителни code-комити; Петър активира минималния клиентски хънк с трите файла чрез изрично разрешение. §10 трябва да пази **Б3 хънковете**, вместо целия `index.html`.

- **S34-4 — Опашката е неназована практически.** `ЗА_ПОДПИС_Б3_07.09.md` липсва; наличната A има **27 реда, всички „да“**; allow има **150 реда**. Новите адресни редове/подписи нямат брой, уникални ID и съпоставка с тела. Поправка: една предварително инвентаризирана опашка; измерени Б3 allow-делти; след `gates.sign` се комитват и променените артефакти, не само опашката.

- **S34-5 — Address release липсва.** [release.py](C:/git/Fire_Varna/gates/release.py:154) свързва само places engine/reference; §10 забранява необходимото разширение. Съществуващият places `--freeze` пресъздава `expectations.json` без `address_replay`, заличавайки секцията. Поправка: подписано разширение за двата корпуса, входни дайджести, отказани делти и взаимно запазващи секциите freeze-команди.

- **S34-6 — Поколението не се проверява.** `generation_id` е само в манифеста; клиентът не го чете и кешира файловете поотделно преди валидация. Проверка на броя допуска разместени адреси. Поправка: SHA-свързана двойка преди активиране на кеша, фикстура със същия брой разместени редове. Днес lazy сборът е **16 315 893 B**; Р12-в трябва да съдържа измерен таван. Б3 вече вдига `PLACES_CACHE` на v7; search-v3 не изисква промяна на `sw.js`, но v2 остава дисков разход.

- **S34-7 — STOP договорът е неизпълним.** М0 трябва едновременно да разреши противоречивите числа и да спре при разлика; М0.10 иска новия билд преди кода. Поправка: отделен измервателен етап, после окончателни числа/подпис; точен G20 набор; STOP при всяко друго падане. PowerShell блокът правилно избягва `&&`/UTF-16 пренасочване, но изисква `$LASTEXITCODE` проверки след всяка команда.

- **S34-8 — Частният изход има пропуснат write-set.** Леджерът е в игнорирания `Varna_buildings/output/quarter_polygon_ledger.json`; теч не установих. OID е потвърден; копирането на геометрията е излишно — парсвайте буфера. Обявеното `!output/*_schema.json` обаче не съществува: добавете точно изключение за новата схема и проверка срещу реална геометрия; публичните отчети да съдържат само агрегати/дайджести.

Петър трябва да разреши **28 именувани избора**, без това автоматично да означава 28 технически подписа:

- **Р0:** ограничения адресен договор. **Р0-б:** точната база и обхватът на изключването.
- **Р1:** неопределеност за непокрития Център.
- **Р2:** полигонен канон за Цветен квартал.
- **Р3:** същото за Колхозен пазар.
- **Р4:** Левски за флагмана Студентска.
- **Р5:** политиката за граничната лента. **Р5-д:** неопределеност със запазен свидетел извън полигоните.
- **Р6:** предимството пред Р38. **Р6-б:** отделният адресен обхват спрямо ADR010.
- **Р7:** неопределеност при несравними припокривания.
- **Р8:** approx остава изключен.
- **Р9:** ориентир за блоковите редове. **Р9-б:** вторично различаване и изключения. **Р9-в:** премахване на дублирания уличен суфикс.
- **Р10:** собствена улица и „ул.“/„до ул.“.
- **Р11:** радиусът. **Р11-б:** качеството и причините за отказ.
- **Р12:** структурният квартал. **Р12-б:** материализираните етикети. **Р12-в:** измереният байтов таван.
- **Р13:** дословните български низове.
- **Р14:** свидетелските токени. **Р14-б:** обхватът на гарда.
- **Р15:** структурният ориентир и демотирането.
- **Р16:** каноничната токенизация.
- **Р17:** редът на доставката.
- **Р18:** адресният публикационен пробник.

Сливаеми: **Р1–Р4** като примери/фикстури към Р5/Р7; **Р6-б→Р0**, **Р9-в+Р15**, **Р10+Р13**, **Р11+Р11-б**, **Р12+Р12-б**, **Р14+Р14-б+Р16**, **Р17+Р18**. **Р8** е запазен инвариант, без отделен подпис.
tokens used
85,936
**НЕГОДНО за подпис.** [Планът](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:1) съвпада с `f745349`; текущият HEAD е `10aabba`. Потвърдени са 14 staged пътя на Б3. Нищо не променях; никакъв remote достъп.

- **S34-1 — Управленското разрешение е прекомерно и закъсняло.** D12 действително защитава адресния път, но подписването на целия 007 приема и несвързаните му D5 промени. Поправка: ограничен амандамент във Fire_Varna плюс ADR064 за генератора, подписани **преди V1/F1**, вместо оформяни чак във V11/F4. `Claude Architect` оформя решенията, `Claude Executor` изпълнява; човешките data-комити са изрично условие на лота — [D16/G4](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:68) не проверява авторството на всички данни.

- **S34-2 — Kill switch-ът няма определена възстановима база.** Четирите селектора пропускат dedupe; валидацията винаги изисква schema3, а генераторът вече заменя `qtk` и премахва етикетни сегменти (§3/§4.3). Поправка: пинната база след миграцията и селектори за всички разлики, или откат на съгласуваните клиент+данни.

- **S34-3 — Комитният ред създава счупен checkpoint.** Р.324 изисква кеш+payload в един комит, но F1 предхожда данните: schema3 клиент срещу schema2. Б3 самият има съгласувани staged пинове. Поправка: Б3 пръв след независимия му одит; съвместими подготвителни code-комити; Петър активира минималния клиентски хънк с трите файла чрез изрично разрешение. §10 трябва да пази **Б3 хънковете**, вместо целия `index.html`.

- **S34-4 — Опашката е неназована практически.** `ЗА_ПОДПИС_Б3_07.09.md` липсва; наличната A има **27 реда, всички „да“**; allow има **150 реда**. Новите адресни редове/подписи нямат брой, уникални ID и съпоставка с тела. Поправка: една предварително инвентаризирана опашка; измерени Б3 allow-делти; след `gates.sign` се комитват и променените артефакти, не само опашката.

- **S34-5 — Address release липсва.** [release.py](C:/git/Fire_Varna/gates/release.py:154) свързва само places engine/reference; §10 забранява необходимото разширение. Съществуващият places `--freeze` пресъздава `expectations.json` без `address_replay`, заличавайки секцията. Поправка: подписано разширение за двата корпуса, входни дайджести, отказани делти и взаимно запазващи секциите freeze-команди.

- **S34-6 — Поколението не се проверява.** `generation_id` е само в манифеста; клиентът не го чете и кешира файловете поотделно преди валидация. Проверка на броя допуска разместени адреси. Поправка: SHA-свързана двойка преди активиране на кеша, фикстура със същия брой разместени редове. Днес lazy сборът е **16 315 893 B**; Р12-в трябва да съдържа измерен таван. Б3 вече вдига `PLACES_CACHE` на v7; search-v3 не изисква промяна на `sw.js`, но v2 остава дисков разход.

- **S34-7 — STOP договорът е неизпълним.** М0 трябва едновременно да разреши противоречивите числа и да спре при разлика; М0.10 иска новия билд преди кода. Поправка: отделен измервателен етап, после окончателни числа/подпис; точен G20 набор; STOP при всяко друго падане. PowerShell блокът правилно избягва `&&`/UTF-16 пренасочване, но изисква `$LASTEXITCODE` проверки след всяка команда.

- **S34-8 — Частният изход има пропуснат write-set.** Леджерът е в игнорирания `Varna_buildings/output/quarter_polygon_ledger.json`; теч не установих. OID е потвърден; копирането на геометрията е излишно — парсвайте буфера. Обявеното `!output/*_schema.json` обаче не съществува: добавете точно изключение за новата схема и проверка срещу реална геометрия; публичните отчети да съдържат само агрегати/дайджести.

Петър трябва да разреши **28 именувани избора**, без това автоматично да означава 28 технически подписа:

- **Р0:** ограничения адресен договор. **Р0-б:** точната база и обхватът на изключването.
- **Р1:** неопределеност за непокрития Център.
- **Р2:** полигонен канон за Цветен квартал.
- **Р3:** същото за Колхозен пазар.
- **Р4:** Левски за флагмана Студентска.
- **Р5:** политиката за граничната лента. **Р5-д:** неопределеност със запазен свидетел извън полигоните.
- **Р6:** предимството пред Р38. **Р6-б:** отделният адресен обхват спрямо ADR010.
- **Р7:** неопределеност при несравними припокривания.
- **Р8:** approx остава изключен.
- **Р9:** ориентир за блоковите редове. **Р9-б:** вторично различаване и изключения. **Р9-в:** премахване на дублирания уличен суфикс.
- **Р10:** собствена улица и „ул.“/„до ул.“.
- **Р11:** радиусът. **Р11-б:** качеството и причините за отказ.
- **Р12:** структурният квартал. **Р12-б:** материализираните етикети. **Р12-в:** измереният байтов таван.
- **Р13:** дословните български низове.
- **Р14:** свидетелските токени. **Р14-б:** обхватът на гарда.
- **Р15:** структурният ориентир и демотирането.
- **Р16:** каноничната токенизация.
- **Р17:** редът на доставката.
- **Р18:** адресният публикационен пробник.

Сливаеми: **Р1–Р4** като примери/фикстури към Р5/Р7; **Р6-б→Р0**, **Р9-в+Р15**, **Р10+Р13**, **Р11+Р11-б**, **Р12+Р12-б**, **Р14+Р14-б+Р16**, **Р17+Р18**. **Р8** е запазен инвариант, без отделен подпис.
