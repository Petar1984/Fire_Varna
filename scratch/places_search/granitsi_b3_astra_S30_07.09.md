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
session id: 01a07b4d-a147-7b80-b1dd-8fad2dd855f9
--------
user
S30 · Преглед на ИЗПЪЛНЕНИЕТО на Б3 (§4 стъпки 0–7), леща механика, read-only. Нищо не е комитнато: write-set-ът е СТЕЙДЖНАТ в C:/git/Fire_Varna (git diff --cached, 13 пътя), HEAD 2591ab8 (родителят на бъдещия атомен комит 2 на Петър). Подписаната основа: docs/plans/ПЛАН_Б3_07.09.md (v3, §14) + docs/plans/ПЛАН_Б3_07.09_амандамент_1.md (подписан); чернова docs/plans/ПЛАН_Б3_07.09_амандамент_2.md (три механични точки, неподписана — червените по тях са обявени). Изпълнителите A/B/C и одиторът твърдят: трите блоба = §1.4 (3dffc264/eb8fa85c/9064705a); index.html 13 редакции (И1–И10, И13, без И11) + маркерите И12 + вариант Б (M7_PREFIXES буквени, филтриран MR само в М7 клона); двата bundle теста 66 OK; tests/test_granitsi_fixtures.py 17 OK с 11 фикстури (всяка _broken доказано мърда точно fails_on); Node сонда tests/granitsi_client_probe.mjs; gates/probe/b3_g11.py (+ флаг --cached); tests/test_b3_gates.py; G7 dump A == dump B (1 324 215 B), engine_A != engine_B; паритет клиент↔референция 11/11; червен набор: 25 теста (21 замразена референция → стъпка 13; 3 MapAttributionTest → 12б; 1 PlacesCacheNameTest → амандамент 2), run_gates: coverage exit 2 (→ стъпка 11) и release BLOCKED 2 (двигателят не е подписаният кандидат; lot1v_v_reference_manifest.json мръсен → амандамент 2 т. 3); G11 --cached: stray_new tests/test_b3_gates.py (→ амандамент 2 т. 2). Атакувай: (1) git diff --cached -- index.html — всеки hunk към номерирана редакция; нищо извън §3.2; И11 отсъства; типовото правило DISTRICT_FALLBACK + двата етикета; вариант Б не пипа други клонове; паритетната повърхност :7470-7480 (стара номерация) непокътната; (2) валидаторите: затворени множества _meta (10/8), src правила, равенство карта↔SIGNED_POLYGON — опитай мутации през сондата; (3) фикстурите: избери 3 _broken и премери сам; Node фикстури 9/11 — стъбове map/fetch задължителни, отказът наблюдаем; (4) recall_sweep.py: own_quarter на шестте места, INPUT_RELS непипнат, MR/R; (5) гейтове с отрицателни половини (G1, G7, G8, G10 първо зареждане, G11, G14); (6) всяко червено извън обявения набор = блокер; (7) COMMIT_MSG_B3.txt дословно по §6; авторството ще е на Петър. Тежки прогони само в git clone --shared под %TEMP%; не пипай, не стейджвай, не комитвай, нищо към отдалечено хранилище. Присъда: ГОДНО за атомния комит на Петър / НЕГОДНО с S30-1… (доказателство + точна поправка); до 700 думи.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя стейджнатото изпълнение спрямо подписаните документи и ще разделя механичния одит между независими агенти. Започвам с HEAD, индекса и обхвата; тежките прогони ще опитам само в изолиран shared clone под `%TEMP%`, ако ограниченията на средата го позволят.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status --short --branch' in C:\git\Fire_Varna
 succeeded in 36ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 92]
M  data/hotels.json
M  data/place_categories.json
M  data/places.json
A  gates/probe/b3_g11.py
M  index.html
D  scratch/places_search/granitsi_fixtures_06.09.json
A  scratch/places_search/granitsi_fixtures_07.09.json
 M scratch/places_search/lot1v_v_reference_manifest.json
 M scratch/places_search/probe_out/token_parity.json
M  scratch/places_search/recall_sweep.py
A  tests/granitsi_client_probe.mjs
A  tests/test_b3_gates.py
M  tests/test_granitsi_fixtures.py
M  tests/test_hotels_public_bundle.py
M  tests/test_places_public_bundle.py
?? scratch/places_search/COMMIT_MSG_B3.txt
?? scratch/places_search/cleanup_brief_astra.md
?? scratch/places_search/cleanup_brief_kimi.md
?? scratch/places_search/golden_brief_kimi.md
?? scratch/places_search/golden_brief_sol.md
?? scratch/places_search/granitsi_b3_astra_S30_07.09.md
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
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git rev-parse HEAD' in C:\git\Fire_Varna
 succeeded in 0ms:
2591ab84903262a4a5112dbdd646f4deeb9c6795

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git diff --cached --name-status' in C:\git\Fire_Varna
 succeeded in 0ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
M	data/hotels.json
M	data/place_categories.json
M	data/places.json
A	gates/probe/b3_g11.py
M	index.html
D	scratch/places_search/granitsi_fixtures_06.09.json
A	scratch/places_search/granitsi_fixtures_07.09.json
M	scratch/places_search/recall_sweep.py
A	tests/granitsi_client_probe.mjs
A	tests/test_b3_gates.py
M	tests/test_granitsi_fixtures.py
M	tests/test_hotels_public_bundle.py
M	tests/test_places_public_bundle.py

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/activeContext.md -TotalCount 100' in C:\git\Fire_Varna
 succeeded in 14ms:
Context_2026-09-04.md](archive/activeContext_2026-09-04.md); the one before it in [archive/activeContext_2026-07-04.md](archive/activeContext_2026-07-04.md).

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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'C:/Users/Petar/.codex/plugins/cache/claude-cowork/engineering/1.2.0/skills/code-review/SKILL.md' -TotalCount 150" in C:\git\Fire_Varna
 succeeded in 0ms:
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                      CODE REVIEW                                   â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚  STANDALONE (always works)                                       â”‚
â”‚  âœ“ Paste a diff, PR URL, or point to files                      â”‚
â”‚  âœ“ Security audit (OWASP top 10, injection, auth)               â”‚
â”‚  âœ“ Performance review (N+1, memory leaks, complexity)           â”‚
â”‚  âœ“ Correctness (edge cases, error handling, race conditions)    â”‚
â”‚  âœ“ Style (naming, structure, readability)                        â”‚
â”‚  âœ“ Actionable suggestions with code examples                    â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚  SUPERCHARGED (when you connect your tools)                      â”‚
â”‚  + Source control: Pull PR diff automatically                    â”‚
â”‚  + Project tracker: Link findings to tickets                     â”‚
â”‚  + Knowledge base: Check against team coding standards           â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

## Review Dimensions
[1-2 sentence overview of the changes and overall quality]

### Critical Issues
codex
HEAD е `2591ab8`, а индексът съдържа точно 13 пътя. Има и нестейджнати артефакти, затова ще проверявам кои байтове чете всеки гейт. Прилагам умението `engineering:code-review` за независим преглед на коректността и отрицателните проверки.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git ls-files -- docs/plans/ПЛАН_Б3* gates tests scratch/places_search/COMMIT_MSG_B3.txt scratch/places_search/lot1v_v_reference_manifest.json scratch/places_search/probe_out/token_parity.json docs/activeContext.md AGENTS.md CLAUDE.md .gitattributes' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/activeContext.md -Encoding UTF8 -TotalCount 100' in C:\git\Fire_Varna
 succeeded in 0ms:
.gitattributes
AGENTS.md
CLAUDE.md
docs/activeContext.md
docs/plans/ПЛАН_Б3_07.09.md
docs/plans/ПЛАН_Б3_07.09_амандамент_1.md
docs/plans/ПЛАН_Б3_07.09_амандамент_2.md
gates/__init__.py
gates/allow/2026-09-05_lot1v_v.json
gates/baseline/MANIFEST.json
gates/coverage.py
gates/probe/b3_g11.py
gates/release.py
gates/run_gates.py
gates/sign.py
scratch/places_search/lot1v_v_reference_manifest.json
scratch/places_search/probe_out/token_parity.json
tests/golden_apply_v0.py
tests/granitsi_client_probe.mjs
tests/test_apply_approved_reports_parity.py
tests/test_approx_addresses_public_bundle.py
tests/test_b3_gates.py
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

 succeeded in 0ms:
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

The 8 resort conflicts (ДАЛИЯ ГАРДЪН · Фрегата · МАГНОЛИЯ 1 И 2 · Маяк · НЕПТУН · Романтика · РУСАЛКА · СТРАНДЖА) stay `pending_signature`: the map shows them as „район X“ until he decides each one.

## Current state

| Какво | Стойност | Команда |
|---|---|---|
| commits on `main` | 327 | `git rev-list --count main` |
| commits ahead of `origin/main` (Petar alone pushes) | 46 | `git rev-list --count origin/main..main` |
| commits on `origin/main` not on `main` | 0 | `git rev-list --count main..origin/main` |
| last pushed commit | 6da5d9a 2026-09-04 | `git log -1 --format='%h %cs' origin/main` |
| records in `data/hydrants.json` | 7407 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/hydrants.json',encoding='utf-8'))))"` |
| records per origin | [('vik', 3524), ('national', 2329), ('etr_varna', 763), ('etr_provadia', 244), ('etr_dolni_chiflik', 219), ('field_report', 151), ('pozarna_gz', 99), ('etr_devnya', 78)] | `PYTHONIOENCODING=utf-8 python -c "import json,collections;print(collections.Counter(x.get('origin') for x in json.load(open('data/hydrants.json',encoding='utf-8'))).most_common())"` |
| `index.html` bytes (557270 before F12; 560365 after F12-з) | 560855 | `wc -c < index.html` |
| `data/hydrants.json` bytes | 1315276 | `wc -c < data/hydrants.json` |
| first load (`index.html` + `data/hydrants.json`), hard cap 5 MB | 1876131 B = 1,79 MB | `python -c "import os;print(os.path.getsize('index.html')+os.path.getsize('data/hydrants.json'))"` |
| `data/hotels.json` (225 rows × 17 keys; 142543 B before F12) | 148685 B · sha `46a44ce82f15…` | `wc -c < data/hotels.json` · `git show HEAD:data/hotels.json \| sha256sum` |
| `data/places.json` (150 rows × 13 keys; 121621 B before F12) | 122089 B · sha `329310f577e8…` | `wc -c < data/places.json` · `git show HEAD:data/places.json \| sha256sum` |
| `data/place_categories.json` (64831 B before F12) | 75818 B · sha `874e33cd00e2…` | `wc -c < data/place_categories.json` · `git show HEAD:data/place_categories.json \| sha256sum` |
| typed locations on the 375 delivered rows: quarter · locality · district (140 · 8 · 375 before F12) | 201 · 12 · 375 | `PYTHONIOENCODING=utf-8 python -c "import json;r=[x for f,k in (('data/places.json','places'),('data/hotels.json','hotels')) for x in json.load(open(f,encoding='utf-8'))[k]];print(sum(1 for x in r if x['quarter']), sum(1 for x in r if x['locality']), sum(1 for x in r if x['district']))"` |
| dictionary: forms · `legacy_by_row` · zones (283 · 209 · 19 before F12) | 283 · 18 · 20 | `PYTHONIOENCODING=utf-8 python -c "import json;c=json.load(open('data/place_categories.json',encoding='utf-8'));print(c['_meta']['n_forms'], len(c['legacy_by_row']), len(c['zones']))"` |
| search reference `scratch/places_search/recall_sweep_rows.json` — NOT frozen by F12 (report-only) | 140 rows, untouched since `148c731` (the commit before F12-а) | `git diff --stat 148c731 -- scratch/places_search/recall_sweep_rows.json` |
| manifest anchor of `lot1v_v_manifest_BASE_P7.json`: the **blob** at the named commit, not the file on disk (F12-ж) | `f06ac06` → `0bc7a189f408…` · 256070 B (the CRLF twin on a Windows worktree is 266021 B and the same OID) | `python scratch/places_search/manifest_anchor_gate.py` · `git show f06ac06:scratch/places_search/recall_sweep_rows.json \| sha256sum` |
| tests (241 after F9; 259 before A.2-4) · red | Ran 266 · FAILED (failures=6) = 6 red, all in `tests/test_places_search_gate.py` (see the split below) | `PYTHONIOENCODING=utf-8 python -m unittest discover -s tests 2>&1 \| tail -3` |
| gates | ⛔ ЧЕРВЕНО: проверка 6 (release) — 173 delta between the frozen reference and the engine candidate and no queue to cover them; проверка 4 ⚠ waits for two signatures; 1, 2, 3, 5, 7 green | `python -m gates.run_gates` |
| release gate: reference ↔ candidate | reference 140 queries / 2121 rows · candidate 203 / 3160 · 173 delta · 0 covered (no queue yet) | `python -m gates.release` |
| `scratch/places_search/expectations.json` | 321040 B · `signed_by: "pending — Петър"` · 78 gate questions · 62 + 10 sweep rows · 15 claims · 3 bucket anchors | `PYTHONIOENCODING=utf-8 python scratch/places_search/recall_sweep.py --manifest` |
| coverage of the delivery against the signed baseline `f06ac06` | places zone_named 127 → 49 · hotels 199 → 152 · uncovered 0 · exit 5 (unsigned allow) | `python -m gates.coverage --places-base git:f06ac06:data/places.json --places-candidate data/places.json --hotels-base git:f06ac06:data/hotels.json --hotels-candidate data/hotels.json --allow gates/allow/2026-09-05_lot1v_v.json` |
| Worker deploy version (repo-declared) | 5accc88e | `sed -n '20p' worker/README.md \| grep -oE '[0-9a-f]{8}'` |
| web manifest (`rel="manifest"`) in `index.html` | 0 | `grep -c 'rel="manifest"' index.html` |
| local branches (traces of closed cycles; work happens on `main`) | backup/pre-c17-split · backup/pre-c32-split · hydrants-c32 · lot1-client · main | `git branch --format='%(refname:short)'` |

Two rows of the previous page are NOT re-measured here because they need the network (satellite link): the open/closed issue counts (`gh issue list …`) and the Pages status code (`curl …`). Read them from the archive with their date, or run the command.

### The red tests: 21 before A.2-4, 6 after (амандамент №4 т. 1 и т. 7)

The class is decided by **where the expectation lives**, measured by reading each test:
`PYTHONIOENCODING=utf-8 python -m unittest discover -s tests -v 2>&1 | grep -E '^(FAIL|ERROR): '`.

**BEFORE A.2-4 — 21 red in three classes:**

- **(а) — 1.** The expectation lived in an artefact that carries `signed_by`:
  `Lot1vVGateTest::test_the_old_zone_words_are_load_bearing` (it read
  `_meta.signed_by` of `lot1v_v_manifest_BASE_P7.json` and said so).
- **(б) — 17.** The expectation was a literal in the code or in the test: the six
  pinned gate constants (`P7_GAINS/CONTROLS`, `LOT1_*`, `LOT1V_A_*`, `LOT1V_B_*`,
  `LOT1V_V_*`, the „7 tokens in 6 zones“ spec), five literals in the test file
  (`test_the_branch_stands_after_the_zone_and_before_the_fuzzy_path`,
  `test_the_collision_rule_is_load_bearing`, `test_added_tokens_are_the_measured_seven`,
  `test_no_added_token_is_a_name_token`, `test_the_foreign_token_guard_is_load_bearing`),
  three pinned anchor COMMITS (`test_the_kind_of_every_frozen_record_is_unchanged` ×2,
  `test_haskey_could_not_have_moved_and_agrees_with_every_branch`) and the three
  ERRORs below.
- **(в) — 3.** The three „replay“ tests compared the engine with the frozen
  reference, which has no `signed_by` at all: `FrozenDiffTest::test_the_live_engine_replays_the_artefact`,
  `Lot1vABucketTest::test_the_live_engine_replays_the_new_bucket`,
  `Lot1vBBucketTest::test_the_live_engine_replays_the_new_bucket`.

The three ERRORs of class (б) named engine attributes that ЛОТ 1в-В had already
removed — `REF.ZONE_PHRASES`, `rec.zph`, `rec.ztk`. They were repaired
mechanically to what the engine carries today (`REF.LOC_PHRASES`; `qph`/`lph`/`gph`;
`qtk`/`ltk`/`legtk`/`ktk`) — an edit, never a signature, exactly as амандамент №4
said. All three are green.

**AFTER A.2-4 — 6 red, one class.** Every delivery-dependent expectation left the
code for `scratch/places_search/expectations.json`; the suite compares the engine
with that tracked body (which can and does fail: move the engine, forget the
artefact, and it is red), and whether Petar has SIGNED it is the release gate's
question — план v2 §0.4 („очакване, което чака подпис, е ред в опашката, не
червен тест“) and §A.2 („готовността на доставката отива в release-гейта“).

The six that remain are one claim in six places: **the frozen reference is still
the one of лот Б and the engine has moved past it** — they go green with the ONE

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09_амандамент_1.md' -Encoding UTF8 -TotalCount 150" in C:\git\Fire_Varna
 succeeded in 0ms:
# АМАНДАМЕНТ №1 към ПЛАН Б3 · 07.09.2026

**Какво изменя:** `docs/plans/ПЛАН_Б3_07.09.md` (v3, ПОДПИСАН от Петър, комит `4db50c2`, §14).
**Основание:** повторната проверка **Astra S29** върху v3 върна **НЕГОДНО** с осем МЕХАНИЧНИ условия (Кими К29: ГОДНО, без условия). §14 на плана предвижда точно това: „условие от тях влиза като амандамент (нов датиран файл) и се подписва отделно, само за делтата“.
**Какво НЕ се променя:** нито едно от **седемнадесетте подписани решения** на §9 (прочитът в §14 остава дословен). Всички редакции тук са в **гейтове, команди, броени числа и реда на две стъпки** — нула нови решения, нула нов write-set, нула ново поведение на картата.
**Статут:** **ПОДПИСАН от Петър (07.09.2026): „подписвам“** — подписаното тяло е блобът в комит 1daefb6, sha256 `b769d83a38e098290a062dc3a7ad8366cf82412f939d61592e95ceb6880fa149`. Изпълнението на Б3 тръгва по ПЛАН v3 (4db50c2) + този амандамент.
**Всяко твърдение по-долу е измерено** в `git clone --shared` копие (скрачпад), с новите блобове на `varna_3d 05f485e`, чиито три пина съвпаднаха байт в байт с §1.4 (`3dffc264… / eb8fa85c… / 9064705a…`). Работното дърво на `C:/git/Fire_Varna` е непипнато (`git status --porcelain` без проследени редове).

---

## 1 · Приетите осем условия

### S29-1 · G7 не е изпълним в PowerShell и редът му е обърнат

**Място:** §5, блокът „G7 — дословно“, **редове 661–675**; и §4, **редове 576–578**.
**СТАРО (663–664 и 668–669, дословно):**
```powershell
python scratch\places_search\recall_sweep.py
copy /Y "%TEMP%\fv_measures\lot1v_v_candidate_rows.json" "<scratch>\g7_dump_A.json"
```
**СТАРО (край на ред 675):** „Ревизиите на двигателя се пинват в отчета (`git rev-parse HEAD:scratch/places_search/recall_sweep.py` преди и след).“

**НОВО — дъмп A, в НОВАТА стъпка 5б (ПРЕДИ редакцията на двигателя):**
```powershell
python scratch\places_search\recall_sweep.py
Copy-Item -LiteralPath "$env:TEMP\fv_measures\lot1v_v_candidate_rows.json" -Destination "<scratch>\g7_dump_A.json" -Force -ErrorAction Stop
python -c "import hashlib,pathlib; b=pathlib.Path('scratch/places_search/recall_sweep.py').read_bytes().replace(b'\r\n',b'\n'); print('engine_A', hashlib.sha256(b).hexdigest())"
```
**НОВО — дъмп B, в стъпка 7 (СЛЕД §3.4–3.6):**
```powershell
python scratch\places_search\recall_sweep.py
Copy-Item -LiteralPath "$env:TEMP\fv_measures\lot1v_v_candidate_rows.json" -Destination "<scratch>\g7_dump_B.json" -Force -ErrorAction Stop
python -c "import hashlib,pathlib; b=pathlib.Path('scratch/places_search/recall_sweep.py').read_bytes().replace(b'\r\n',b'\n'); print('engine_B', hashlib.sha256(b).hexdigest())"
```
**НОВО — двата comparator-а (и двата задължителни, exit ≠ 0 спира лота):**
```powershell
python -c "import pathlib,sys; a=pathlib.Path(r'<scratch>\g7_dump_A.json').read_bytes(); b=pathlib.Path(r'<scratch>\g7_dump_B.json').read_bytes(); print(len(a),len(b),a==b); sys.exit(0 if a==b else 1)"
python -c "import sys; A='<engine_A>'; B='<engine_B>'; print(A,B,A!=B); sys.exit(0 if A!=B else 1)"
```
Вторият е новото: без него гейтът може да сравни **същия** двигател със себе си и да мине празен.
**Мярка:** `powershell -NoProfile -Command '…try { copy /Y "$env:TEMP\nope.json" "X.txt" } catch { exit 1 }'` → **exit 1, `ParameterBindingException`** (`copy` е псевдоним на `Copy-Item`; `%TEMP%` не се разгръща в PowerShell); същото с `Copy-Item -LiteralPath "$env:TEMP\…" -Force -ErrorAction Stop` → **exit 0, файлът е там**. · `git rev-parse HEAD:scratch/places_search/recall_sweep.py` преди и след редакция в работното дърво → **един и същ OID `bae0c1bf…`**, докато `sha256` на изпълнения файл се мени `0869f12c…` → `ec6fef0a…`: пинът по `HEAD:path` е сляп точно за това, което G7 мери. · Дъмпът след прогон → **1 324 215 B** (числото на плана се потвърждава).

### S29-2 · Отрицателната фикстура 8 нарушава собствения си договор

**Място:** §3.5, **ред 454** (правилото на харнеса) и **ред 466** (фикстура 8).
**СТАРО (454):** „`_broken` носи `fails_on: "<заявка>"`; тестът твърди, че `assert_case` хвърля **и** че точно тази заявка е сменена, а останалите заявки на фикстурата са непроменени“.
**СТАРО (край на 466):** „`fails_on: "аспарухово"`, а вторият ред се пази като второ твърдение“.

**НОВО (454):** `_broken` носи **`fails_on: [<заявка>, …]` — МНОЖЕСТВО**, и тестът мери кои заявки наистина са мръднали:
```python
    qs = [w["q"] for w in case["queries"]]
    clean  = dict((q, answer(self.reference, q)) for q in qs)          # без ops
    broken_m = dict((q, answer(self.reference, q, broken["ops"])) for q in qs)
    changed = sorted(q for q in qs if broken_m[q] != clean[q])
    self.assertEqual(changed, sorted(broken["fails_on"]), name)        # ТОЧНО множеството
    with self.assertRaises(AssertionError):                            # и то наистина чупи
        self.assert_case(case, broken_m)
```
Едно-заявъчните фикстури носят списък от един елемент. Мутация, която мърда заявка ИЗВЪН `fails_on`, вече не минава за доказателство — и мутация, която НЕ мърда обявена заявка, също пада.
**НОВО (край на 466):** → **„аспарухово“ 16 → 17** (детето влиза при родителя) **И** **„дружба“ 2 → 1** (клонът пада от `M7-bare-location` на `M3`). **`fails_on: ["аспарухово", "дружба"]`** — двете са РАВНОПРАВНИ твърдения на една мутация, не главно и второстепенно.

**Мярка:** един `op` (`ЦДГ 43 "Пинокио"` → `quarter {name: "кв. Аспарухово", code: "druzhba", src: SIGNED_POLYGON}`, `zone: "кв. Аспарухово"`) над целия корпус (226 записа + шестте фикстурни заявки), сравнение чист ↔ мутиран:
**променени записи: 4; различни заявки: 4** — `аспарухово 16→17`, `дружба M7/2 → M3/1`, и латинските им близнаци `asparuhovo`, `druzhba` в кофата `gate_m7_bare`. **Нищо друго не мърда.** Другите поправени мутации на плана се потвърдиха непроменени (`чайка` 30, `възраждане` 5/0/0).

### S29-3 · О29 и §13 т.4 броят заявките погрешно

**Място:** §4 стъпка 10, **ред 590**; §1.8.15, **ред 200**; §13 т.4, **ред 883**.
**СТАРО:** „**59 реда `ЧЕРВЕНО` върху 41 уникални заявки + 2 реда без заявка**“ (и двата ѝ близнака на редове 200 и 883).
**НОВО:** „**59 оплаквания общо: 57 реда върху 38 различни заявки + 2 реда без заявка**“.

Двата реда без заявка остават дословно: `p7_added: 7 токена в 5 зони, подписани са 2 в 2` и `p7_added ≠ подписаното: {…}`.
**Мярка:** `python scratch\places_search\recall_sweep.py --manifest` (ЕДИН прогон, в клонинга) → **exit 1**; `grep -c ЧЕРВЕНО` → **59**; парсване по регекса `ЧЕРВЕНО:\s*\S+\s*` + обратни апострофи → **57 реда с заявка, 38 различни, 2 реда без заявка**.
Изброените в плана заявки са ПЪЛНИ и ВЕРНИ: множеството от редове 591–592 минус прозаичния `zone` дава **точно същите 38** (`plan − measured = ∅`, `measured − plan = ∅`). Сгрешено е само числото в заглавието: „41“ включва `zone`, `M2-failopen` и `A3-location`, които не са заявки.
Гейт-резултатите на плана се потвърдиха дословно: П7 **16/32**, ЛОТ 1 **6/18**, 1в-А **5/12**, 1в-Б **5/6**, 1в-В **4/10** (квартал 258 · доп. 12 · район 375/375), М7 **17/17**, §10 sweep **60/62 · 10/10**, „срещу подписа 1“, `release: BLOCKED: 4`.

### S29-4 · G11 гледа само `data/` и пропуска геометрия

**Място:** §5, блокът „G11 — дословно“, **редове 689–714**.
**СТАРО (ред 700):**
```python
files = [f for f in subprocess.run(["git","ls-files","data/"],capture_output=True,text=True).stdout.split() if f.endswith(".json")]
```
**НОВО — целият блок се заменя със скрипта `gates/probe/b3_g11.py` (нов файл в write-set-а, стъпка 3):**
```python
# -*- coding: utf-8 -*-
"""G11 — нула геометрия, СТРУКТУРНО, по ЦЕЛИЯ комит (S29-4)."""
import json, subprocess, sys, pathlib
GEO = {"coordinates", "geometry", "geometries"}
# ТОЧНИТЕ наследени изключения: (път, JSON-указател, тип на стойността).
LEGACY = {("scratch/places_search/granitsi_fixtures_07.09.json", "/_meta/geometry", str)}
ALLOWED_NEW = {"tests/granitsi_client_probe.mjs",
               "scratch/places_search/granitsi_fixtures_07.09.json",
               "scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md",
               "gates/allow/2026-09-07_b3.json",
               "scratch/places_search/архив/АРХИВ_A_05.09.md",
               "gates/probe/b3_g11.py"}
def walk(o, path, hits):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in GEO: hits.append((path + "/" + k, type(v)))
            walk(v, path + "/" + k, hits)
    elif isinstance(o, list):
        for i, v in enumerate(o): walk(v, path + "[%d]" % i, hits)
def changed(parent):
    parts = [p for p in subprocess.run(["git", "diff", "--name-status", "-z",
        "--find-renames", "--diff-filter=AMR", parent, "HEAD"],
        capture_output=True).stdout.decode("utf-8").split(chr(0)) if p != ""]
    files, new, i = [], [], 0
    while i < len(parts):                     # R носи ДВА пътя, A и M — по един
        if parts[i][0] == "R": files.append(parts[i + 2]); i += 3
        else:
            if parts[i][0] == "A": new.append(parts[i + 1])
            files.append(parts[i + 1]); i += 2
    return files, new
def main(parent):
    tracked = [f for f in subprocess.run(["git", "ls-files", "data/"],
               capture_output=True, text=True).stdout.split() if f.endswith(".json")]
    touched, new = changed(parent)
    scope = sorted(set(tracked) | set(f for f in touched
                   if f.lower().endswith((".json", ".geojson"))))
    bad, unread = [], []
    for f in scope:
        p = pathlib.Path(f)
        if not p.exists(): continue
        try: doc = json.loads(p.read_text(encoding="utf-8"))
        except ValueError as exc: unread.append((f, str(exc))); continue
        hits = []; walk(doc, "", hits)
        bad += [(f, ptr, typ.__name__) for ptr, typ in hits
                if (f, ptr, typ) not in LEGACY]
    stray = sorted(set(new) - ALLOWED_NEW)
    print(json.dumps({"scope": len(scope), "geo_hits": bad, "unreadable": unread,
                      "stray_new": stray}, ensure_ascii=False))
    sys.exit(0 if not bad and not unread and not stray else 1)
if __name__ == "__main__":
    main(sys.argv[1])
```
**Команда:** `python gates\probe\b3_g11.py <parent>` → **0**. Инвентарът на новите файлове (стария ред 711) влиза В СЪЩИЯ скрипт (`stray_new`), а не в отделна `git diff` команда за четене с очи.
**Мярка** (клонинг, симулиран Б3-комит с `git mv` на фикстурата): чисто → `{"scope": 19, "geo_hits": [], "unreadable": [], "stray_new": []}` · **exit 0**; `Polygon` вкаран в **преименуваната фикстура** → `geo_hits: [["…granitsi_fixtures_07.09.json", "/_smuggled/coordinates", "list"]]` · **exit 1**; **СТАРИЯТ G11 върху същото дърво** → `18 []` · **exit 0** — сляп, точно както казва S29.
Наследеното изключение е РЕАЛНО и носещо: фикстурният `_meta.geometry` е ПРОЗА в стойност („нула координати — фикстурите носят само имена, кодове и клонове“); без реда `LEGACY` същият чист комит дава `geo_hits: [[…, "/_meta/geometry", "str"]]` · **exit 1**.

### S29-5 · Отрицателният G15 минава

**Място:** §4 стъпка 11, **редове 614–617**; §5 ред **656**; §1.8.20 ред **205**.
**СТАРО (615, край):** `… print(len(q), q); sys.exit(0 if len(q)==1 else 1)`
**НОВО (615):**
```powershell
python -c "import subprocess, posixpath, fnmatch, sys; WANT=['scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md']; out=subprocess.run(['git','ls-tree','-r','--name-only','-z','HEAD','--','scratch/places_search'],capture_output=True).stdout.decode('utf-8'); q=sorted(n for n in out.split(chr(0)) if n.strip() and fnmatch.fnmatchcase(posixpath.basename(n),'ЗА_ПОДПИС_*.md')); print(len(q), q); sys.exit(0 if q==WANT else 1)"
```
**НОВО (656, колоната „отрицателното доказателство“):** трите случая, всеки ДОКАЗАНО падащ — „само старата опашка“ · „архивирана СЪС стария префикс“ · „новата + старата“.


exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09_амандамент_2.md' -Encoding UTF8 -TotalCount 150" in C:\git\Fire_Varna
 succeeded in 0ms:
# АМАНДАМЕНТ №2 към ПЛАН Б3 · 07.09.2026 (нощта, чернова на архитекта)

**Какво изменя:** `docs/plans/ПЛАН_Б3_07.09.md` (v3, подписан 4db50c2) + амандамент №1 (подписан 4fdd303).
**Основание:** изпълнител B спря правилно на §7 т. 4 — червен тест ИЗВЪН обявения набор, който никоя следваща подписана стъпка не гаси. Изпълнител A остави две находки от същия механичен род. Нито едно от 17-те подписани решения не се променя; нито един нов избор за картата.
**Статут:** ⏳ **за подпис на Петър сутринта — само делтата; преди атомния комит 2.** Поправките НЕ са приложени през нощта (нито един ред извън write-set-а без подпис); червените остават обявени в набора D19/G20.

## 1 · Трите механични поправки

### А2-1 · Второто ръчно копие на името на кеша (ADR 008 D8)
**Мярка (B):** `tests/test_places_search_gate.PlacesCacheNameTest.test_the_probe_uses_the_name_index_html_owns` → exit 1: `'fire-varna-hotels-v7-225' != 'fire-varna-hotels-v6-225'`. Причина: `scratch/places_search/probe_places_fv.mjs:802` носи `const PLACES_CACHE = "fire-varna-hotels-v6-225";` (ползван на :1002, :1004, :1533); `git grep` показва точно двете живи копия (index.html и сондата). В контрафактуален клонинг с новите данни, но със стария index.html, тестът е зелен — червеното е следствие само от И1. ADR 008 D8 казва изрично: името се води на ръка от ДВЕ страни.
**Поправка:** нова редакция **И1б** в write-set-а: `scratch/places_search/probe_places_fv.mjs:802` → `const PLACES_CACHE = "fire-varna-hotels-v7-225";` (един ред; §10 не забранява файла). Влиза в атомния комит 2. Гейт: същият тест → 0; отрицателно: върни v6 → 1.

### А2-2 · Гейтът на новите файлове не познава собствения си тестов файл
**Мярка (A):** `gates/probe/b3_g11.py` `ALLOWED_NEW` (амандамент 1, S29-4) не изброява `tests/test_b3_gates.py` (файлът е поискан от S29-8 в същия амандамент) → `stray_new: ["tests/test_b3_gates.py"]`, exit 1 при комита (STOP 22 по конструкция).
**Поправка:** `ALLOWED_NEW` получава реда `"tests/test_b3_gates.py"`. Гейт: `python gates/probe/b3_g11.py HEAD --cached` → 0; отрицателно: непознат нов файл в скрачпад-клонинг → 1.

### А2-3 · О26 се разширява с втори проследен изход на двигателя
**Мярка (A/B):** обикновеният (не-freeze) прогон на `recall_sweep.py` пише и `scratch/places_search/lot1v_v_reference_manifest.json` (проследен), не само `probe_out/token_parity.json`. Дали байтовете се менят при днешните прогони: виж реда „git diff --stat“ в доклада на изпълнител C.
**Поправка:** О26 и §4 стъпка 7 назовават и двата файла; ако манифестът е променен, той пътува с комит 5 (замразяването), не с комит 2; ако е байт-еднакъв — записва се, че е бил пренаписан без промяна.

## 2 · Уточнение, което НЕ е поправка (записва се)
**Фикстура 9в:** пинът на плана за мутираното тяло (128 402 B / `6bfbcbf2…`) не се възпроизвежда; §3.5 казва, че числата се преизмерват. Мутацията се записва дословно: първият обект `"quarter"` със `"src": "SIGNED_POLYGON"` в `data/places.json` получава `"code": "tsentar_new"` (беше `kv_levski`) → тяло 128 403 B, sha256 `2064527328899246c32b0c83f8fc3dba9c01d1cbbb67791a6dcc18e88c997733`. Изпълнител C я пинва така.

## 3 · Какво подписва Петър
Един подпис за трите реда: И1б (v7 в сондата), `ALLOWED_NEW` + `tests/test_b3_gates.py`, О26 с втория файл. Нищо друго не се променя.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09_амандамент_1.md' -Encoding UTF8 | Select-Object -Skip 150 -First 150" in C:\git\Fire_Varna
 succeeded in 7ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "python -B -c \"from pathlib import Path; p=Path('docs/plans/ПЛАН_Б3_07.09.md'); lines=p.read_text(encoding='utf-8').splitlines(); print('\\n'.join(str(i+1)+': '+s for i,s in enumerate(lines) if s.startswith('#')))\"" in C:\git\Fire_Varna
 exited 1 in 4ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath scratch/places_search/COMMIT_MSG_B3.txt -Encoding UTF8 -TotalCount 100' in C:\git\Fire_Varna
 succeeded in 0ms:
feat(search): quarter search over signed boundaries, QUARTER_CODES +8, cache v7 (D13 atomic delivery)

data: places delivery with quarter_attribution (D13 ordered) — the three blobs of
varna_3d 05f485e (places 3dffc264, hotels eb8fa85c, categories 9064705a), with the
closed lists, the three pins, LEGACY_BUNDLE_SHA and PLACES_CACHE v7 in this very
commit, because a HEAD whose pins and blobs disagree kills the place search.
tests: S17 fixtures fail on broken candidates

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath gates/run_gates.py -Encoding UTF8 -TotalCount 150' in C:\git\Fire_Varna
 succeeded in 0ms:
#!/usr/bin/env python3
"""The single executable the push waits on.

    python -m gates.run_gates [--base git:<rev>] [--allow <path>]

Seven checks, one table, one exit code:

  1. sha pins        the three SHA256 constants in `index.html` against the
                     LF-normalised bytes of the three delivered blobs — exactly
                     the bytes `fetchValidatedJson` digests in the browser
  2. key sets        every row carries exactly EXPECT_KEYS / EXPECT2_KEYS
                     (hotels 17, places 13) — the count and the names
  3. qa_no_cad_ids   no cadastral identifier ever rides a public blob
  4. coverage        gates/coverage.py against the last signed baseline
                     (gates/baseline/MANIFEST.json); no baseline = STOP
  5. signed_facts    data/signed_facts.json — the small judging file
  6. release         gates/release.py — the frozen reference, the engine
                     candidate, the pinned inputs and the manifests bound by
                     digest; every delta covered by a signed queue row
  7. authorship      every `signed_by: "Петър"` was introduced by a commit of
                     Petar1984, never by an agent (`git log -S`) — AND the body
                     it protects has not been rewritten since: the newest commit
                     on a signed artefact is Petar's too, or he recorded the
                     digest of the resulting body himself (амандамент №5 т. 3),
                     on a queue whose own authorship was settled first
                     (амандамент №6 т. 3) and with HIS commit as the one that
                     introduced the number (амандамент №8 т. 2) — and every
                     „да“ ROW of that queue was introduced by a commit of his
                     as well (амандамент №9 т. 2)

The gate never imports `unittest` and never reads `tests/`: a check that shares
code with the suite it guards cannot fail independently of it.

Every check runs, always: the table is written for the human, not stopped at
the first mark. Exit code: 0 only when every check is green; 1 when any check
is red OR yellow — "pending — Петър" is not a signature (Амандамент №1, т. 8),
and neither is "Петърчо Иванов": the signature is compared exactly, by
`coverage.is_signed_by_petar`, for the baseline manifest and the allow-file
alike. `--base` replaces the signed baseline with an ad-hoc revision and is
therefore ⚠ by construction: it measures, it does not absolve.
One number for the pre-push hook to read.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from gates import coverage
from gates import release

REPO_ROOT = Path(__file__).resolve().parent.parent

INDEX_HTML = "index.html"
BASELINE_PATH = "gates/baseline/MANIFEST.json"
ALLOW_DIR = "gates/allow"
SIGNED_FACTS_PATH = "data/signed_facts.json"
# The only author whose commit may INTRODUCE a signature (§0.5) — one string,
# kept in `gates.release` and read by every gate that asks whose hand it was.
HUMAN_AUTHOR = release.HUMAN_AUTHOR

# (constant in index.html, delivered blob)
SHA_PINS = (
    ("HOTELS_SHA256", "data/hotels.json"),
    ("PLACES2_SHA256", "data/places.json"),
    ("CATS_SHA256", "data/place_categories.json"),
)

ROW_FILES = (
    ("hotels", "data/hotels.json", "hotels", "EXPECT_KEYS", 17),
    ("places", "data/places.json", "places", "EXPECT2_KEYS", 13),
)

# A cadastral id never rides a public bundle (ADR 008 Д2) — the same regex the
# client applies to the fetched text, applied here to the tracked bytes.
CADASTRAL_RE = re.compile(r"\b\d{4,5}\.\d+\.\d+")
PUBLIC_BLOBS = (
    "data/hotels.json",
    "data/places.json",
    "data/place_categories.json",
    SIGNED_FACTS_PATH,
)

OK, WARN, BAD = "✓", "⚠", "✗"


class Check:
    """One row of the table: a mark, a name, and the words behind it."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.mark = OK
        self.lines: list[str] = []

    def say(self, text: str) -> None:
        self.lines.append(text)

    def fail(self, text: str) -> None:
        self.mark = BAD
        self.lines.append(text)

    def warn(self, text: str) -> None:
        if self.mark == OK:
            self.mark = WARN
        self.lines.append(text)


def read_text(rel: str) -> str:
    return (REPO_ROOT / rel).read_text(encoding="utf-8")


def lf_bytes(rel: str) -> bytes:
    """The bytes the browser sees: the tracked LF blob, whatever the checkout wrote."""
    return (REPO_ROOT / rel).read_bytes().replace(b"\r\n", b"\n")


def js_const_string(html: str, name: str) -> str | None:
    m = re.search(r"const\s+%s\s*=\s*'([0-9a-f]{64})'" % re.escape(name), html)
    return m.group(1) if m else None


def js_const_array(html: str, name: str) -> list[str] | None:
    """Read a JS array of single-quoted strings out of index.html.

    The closed lists live in the app shell and nowhere else; duplicating them
    here would create a second truth that drifts.
    """
    m = re.search(r"const\s+%s\s*=\s*\[(.*?)\]\s*;" % re.escape(name), html, re.S)
    if not m:
        return None
    return re.findall(r"'([^']*)'", m.group(1))


def check_sha_pins() -> Check:
    check = Check("1 · sha пинове (index.html ↔ LF байтовете)")
    html = read_text(INDEX_HTML)
    for const_name, rel in SHA_PINS:
        pinned = js_const_string(html, const_name)
        if not pinned:
            check.fail("%s: константата липсва в %s" % (const_name, INDEX_HTML))
            continue
        actual = hashlib.sha256(lf_bytes(rel)).hexdigest()
        if actual == pinned:
            check.say("%s = %s ✓ %s" % (const_name, pinned[:12], rel))
        else:

codex
Средата е с наложен `read-only` достъп и не позволява създаване на shared clone под `%TEMP%`. Ще продължа с проверките на индекса и мутации само в паметта; тежките suite/G7 прогони ще отбележа като невъзпроизведени тук, без да ги заменям с прогон в основното checkout. Трите червени точки от амандамент №2 са потвърдени като обявени, но той още е неподписан.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "python -X utf8 -B -c \"from pathlib import Path; p=Path('docs/plans/ПЛАН_Б3_07.09.md'); lines=p.read_text(encoding='utf-8').splitlines(); print('\\n'.join(str(i+1)+': '+s for i,s in enumerate(lines) if s.startswith('#')))\"" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8 | Select-Object -Skip 50 -First 130" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8 | Select-Object -Skip 530 -First 150" in C:\git\Fire_Varna
 succeeded in 0ms:
1: # ПЛАН Б3 · Търсене по квартал над подписаните граници (Fire_Varna) — v3
13: ## 0 · Червени редове (наследени, без изключение)
36: ## 1 · Мярка (базата, преди един ред промяна)
38: ### 1.1 Състояние на репата — **преизмерено 07.09, котвата се движи**
53: ### 1.2 Днешните котви в `C:/git/Fire_Varna/index.html`
82: ### 1.3 Липсващите кодове
89: ### 1.4 Новите пинове (LF-блобове от git, не от диска)
110: ### 1.5 Какво носи доставката — **преизмерено, с поправка на v2**
123: ### 1.5б 🔴 `_meta` — точните множества ключове (единственият авторитет на G17)
134: ### 1.6 Какво умира днес, ако блобовете влязат сами — **изпълнено, не изведено** 🔴
147: ### 1.7 Референцията и фикстурите
181: ### 1.8 🔴 Мерките, които оборванията добавиха (новите СТОП-числа)
212: ### 1.9 Гейтът на доставката
224: ### 1.10 Червената линия и размерът
230: ## 2 · Обявени отклонения от подписания текст (искат подписа на Петър)
267: ## 3 · Write-set (точните файлове и точните редакции)
269: ### 3.1 Данни (байтов препис, нула трансформация)
279: ### 3.2 `index.html` — четиринадесет редакции, всяка с котва
412: ### 3.3 Пиновете и правилата в двата bundle теста
425: ### 3.4 Двигателят на референцията — шест места, не две (О19)
434: ### 3.5 Фикстурите — единадесет, всяка с ДОКАЗАНО падащ `_broken`
471: ### 3.6 Node-фикстурите — как се викат и какво доказват (**изпълнено от планера, не обещано**)
511: ### 3.7 Родство — какво работи, какво не, поименно (О16)
523: ### 3.8 Опашката и allow-ът (О22, О25)
531: ## 4 · Ред на изпълнение
636: ## 5 · Гейтове (всеки — команда с изход ≠ 0 и с ДОКАЗАНО падаща отрицателна половина)
725: ## 6 · Комити (кой какво комитва)
763: ## 7 · STOP условия
790: ## 8 · Локален преглед (как Петър гледа)
814: ## 9 · Решения за Петър
840: ## 10 · Какво НЕ се пипа
855: ## 11 · Отхвърлени находки (от кръговете на v1/v2)
866: ## 12 · Оборване
876: ## 13 · Отхвърлени външни находки (с измерената причина)
892: ## 14 · Подпис и прочит на §9 „по препоръките“ (07.09.2026)

 succeeded in 0ms:
**Стъпка 0 на §4 преизмерва и петте — HEAD се движи, докато планът чака подпис.**

### 1.2 Днешните котви в `C:/git/Fire_Varna/index.html`

| котва | ред | текуща стойност |
|---|---|---|
| `PLACES_CACHE` | `:6265` | `'fire-varna-hotels-v6-225'` |
| `HOTELS_SHA256` / `PLACES2_SHA256` / `CATS_SHA256` | `:6288` / `:6289` / `:6290` | `46a44ce8…` / `329310f5…` / `874e33cd…` |
| `LEGACY_BUNDLE_SHA` | `:6301-6304` | places `329310f5…`, hotels `46a44ce8…` |
| `QUARTER_SRC` | `:6313` | `['REG', 'KAIS', 'SIGNED_OVERRIDE']` |
| `DISTRICT_SRC` / `DISTRICT_CODES` | `:6314` / `:6315-6316` | 2 извора / 5 кода |
| `QUARTER_CODES` | `:6317-6321` | **20 кода** (масив, не `Set`) |
| `LOCALITY_CODES` | `:6322` | 5 кода |
| `isSignificantToken` | `:6495-6496` | `!t.num && t.orig.length > 2 && t.s.length > 2 && …ADDR… && !GENERIC_WORDS.has(t.s)` |
| `validLocation` | `:6528-6534` | `src ∈ srcs && code ∈ codes` |
| `validTypedLocation` | `:6535-6545` | **`:6537` валидира `locality` със `QUARTER_SRC`**; `:6544` `zone === quarter.name ?? 'район '+district.name` |
| `validateHotels` / `validatePlaces2` | `:6546-6562` / `:6563-6580` | **не броят ключовете на `_meta`, не четат `quarter_attribution`** |
| **`accept`** | **`:6602-6612`**, условието на **`:6605`** | `if (window.crypto && crypto.subtle) { … digest ≠ sha → return null }` — **валидаторът се вика САМО след успешна sha-сверка** (1.8.11) |
| `fetchValidatedJson` / `ensurePlaces` | `:6613-6625` / `:6626-6647` | `throw 'places payload unavailable'` само ако И двата масива са празни (`:6639`) |
| **`buildIndex`** | **`:6648`** | **приема ВЕЧЕ разпарсени масиви — не вика нито един валидатор** |
| `makeRec` qtk/qph | `:6749`, `:6782` | — |
| **М7 клонът на клиента** | **`:7058-7069`** | `R.every(isSignificantToken)` + `qHit`/`lHit`/`bphrase` — **тук няма списък с типови префикси** (К28-5) |
| районните клонове | `:7064`, `:7118` | `!r.e.quarter` — двете места на типовия капан |
| изричното „район X“ с ключ | `:7104-7109` | филтрира САМО по `r.dph`; **не гледа `quarter`** |
| `popupFor` | `:7253-7289` | редът „вид · квартал · район“ на `:7257-7271`; **ред за извор НЯМА и днес**; ползва `span` (`:7155`), `buildNavActions` (`:4255`), `SRC_LINE`/`ADDR_SRC_LINE`/`ALIAS_SRC_LINE` (`:6328-6360`) |
| Leaflet | `:1900` `zoomControl → bottomleft`; `:1901` `OSM_ATTRIB = '© OpenStreetMap'`; `:1917` `attribCtrl` (`position: 'bottomleft'`); `:1918` `attribCtrl.addAttribution(OSM_ATTRIB)` | размени: `:4543-4549`, `:4663`, `:4672-4676` |
| pmtiles флаг + override | `:4563` `false`; `:4571-4574` `isBasemapPmtilesActive()` чете `localStorage` | пътят е достижим и днес |
| **зареждане при първо отваряне** | `:1772-1774` `fetch('data/hydrants.json')` — **безусловен IIFE** | `ensurePlaces()` се вика САМО от `inputEl.addEventListener('focus', …)` (`:7393`); адресната търсачка е lazy (`:5325-5326`, `fetchCachedJson` на фокус); `data/approx_addresses_v1.json` е зад изключен флаг (`:5926 APPROX_ADDRESS_SEARCH_ENABLED = false`); `data/basemaps/basemap_manifest.json` — само при активен pmtiles (`:4563` false) |

Нула попадения за point-in-polygon. **Кварталът е доставено поле + речник от думи, не геометрия.**

### 1.3 Липсващите кодове

Доставката носи **28** квартални кода; `QUARTER_CODES` носи 20; липсват точно **8**:
`dolna_traka · grackata_mahala · hristo_botev · kolhozen_pazar · kv_levski · sv_ivan_rilski · trakia · tsentar`.
`set(QUARTER_CODES) − доставени = ∅`. Делтата е **+8**, не „+41“ (О3).
Речникът (`place_categories.json.locations.quarter`) носи **точно същите 28 кода** — `dict == delivered: True`, `parents` **0 от 28**, `locality` 5, `district` 5.

### 1.4 Новите пинове (LF-блобове от git, не от диска)

Команда:
```bash
git -C /c/git/varna_3d show 05f485e:data/fire_varna_places.json > <scratch>/new_data/places.json   # и другите два
python - <<'PY'
import hashlib, gzip, pathlib
for p in ['places.json','hotels.json','place_categories.json']:
    b = pathlib.Path('<scratch>/new_data/'+p).read_bytes().replace(b'\r\n', b'\n')
    print(p, len(b), hashlib.sha256(b).hexdigest(), len(gzip.compress(b, 9)))
PY
```

| файл (източник → цел) | sha256 | bytes | gzip9 |
|---|---|---|---|
| `varna_3d:data/fire_varna_places.json` → `data/places.json` | `3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66` | **128401** | **14748** |
| `varna_3d:data/fire_varna_hotels.json` → `data/hotels.json` | `eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51` | **151263** | **13642** |
| `varna_3d:data/place_categories.json` → `data/place_categories.json` | `9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231` | **77998** | **9690** |

**Капан:** работното дърво на varna_3d е CRLF за два от трите — мери се `git show`, не `os.path.getsize`.

### 1.5 Какво носи доставката — **преизмерено, с поправка на v2**

- places **150** / hotels **225**; нула добавени, нула изтрити.
- Извори на `quarter`: places `{SIGNED_POLYGON: 42, REG: 39, KAIS: 10, null: 59}`; hotels `{REG: 115, KAIS: 25, SIGNED_OVERRIDE: 12, SIGNED_POLYGON: 15, null: 58}`. **`DISTRICT_FALLBACK`: 0 реда.**
- **`zone !== quarter.name`: 0 реда** в двата пакета (О20 остава верен).
- 🔴 **Поправка на v2 §1.5.** v2 пише „`quarter_attribution` = 18 кода“. Измереното: картата е **на всеки пакет поотделно** — **places 14** (13 wikimapia + 1 openstreetmap), **hotels 7** (всичките wikimapia); **обединението е 18**, общите са **3** (`kolhozen_pazar`, `kv_levski`, `tsentar`). Това е ЕДИНСТВЕНОТО правилно основание за G17.
- 🔴 **Всяка карта е ТОЧНО равна на множеството `SIGNED_POLYGON` кодове на своя пакет** (`qa == sp: True` и за двата; `qa−sp = ∅`, `sp−qa = ∅`). Гейтът е **равенство**, не „включване“ (по-силно от буквата на амандамент №2).
- Запис на всеки код: точно четирите ключа `{label, licence, src, url}` (едно-единствено ключово множество за всичките 21 записа).
- Единственият не-wikimapia запис: `mladost2 → {"src": "openstreetmap", "label": "© OpenStreetMap contributors", "licence": "ODbL", "url": "https://www.openstreetmap.org/copyright"}` — **url-ът НЕ е по формата на wikimapia** и всяко правило „един регекс за всички“ пада върху него.
- Wikimapia url-ите са **`http://wikimapia.org/<id>/bg/<път>`** (пример: `http://wikimapia.org/900042/bg/ж.к._Васил_Левски`) — `http`, с път след id-то (О17).
- Речник: зони 20→28, псевдоними 39→48; `parents` — **0 от 28**.
- Нула геометрия, нула кадастрален идентификатор (структурна проверка, 1.8.12).

### 1.5б 🔴 `_meta` — точните множества ключове (единственият авторитет на G17)

```
places._meta  (10): generated · count · by_kind · by_zone_src · licence_osm ·
                    licence_registry · licence_wikidata · licence_address ·
                    quarter_attribution · excluded
hotels._meta  (8):  generated · count · by_zone_src · licence · licence_osm ·
                    licence_address · quarter_attribution · excluded
```
Днешните (старите) са **9** и **7** — същите списъци без `quarter_attribution`. Броят е **следствие**; договорът е множеството.

### 1.6 Какво умира днес, ако блобовете влязат сами — **изпълнено, не изведено** 🔴

Node-проба върху среза `index.html:6256-7154` с ДНЕШНИТЕ списъци над НОВИТЕ байтове (стъбове: `window`, `caches`, `document`, `map`, `fetch`, `attribCtrl`, `L`, `console`, `crypto`):

```
validateHotels   = false        ← хотелите СЪЩО носят SIGNED_POLYGON (15 реда)
validatePlaces2  = false
accept(text, пинат sha, validatePlaces2) = null
await ensurePlaces()  →  ХВЪРЛЯ  Error: places payload unavailable      (:6639)
```

**Това оборва v2 §3.6 т. 4 („`RECS.length === 225` при среза с оригиналния `QUARTER_SRC`“): при стария списък НЯМА `RECS` — има изключение.** 225 е достижимо само когато **само** places е отказан (1.8.10, случай 9в).

### 1.7 Референцията и фикстурите

| прогон | резултат | exit |
|---|---|---|
| `python -m unittest tests.test_granitsi_fixtures -v` | `Ran 5 tests · OK` | 0 |
| `python -m unittest discover -s tests` | `Ran 315 tests · OK` | 0 |
| `python -m gates.run_gates` | 7/7 зелени | 0 |

Върху **новата** доставка (двигателят е `recall_sweep.py` с подменени пътища към новите блобове, `main()` не се вика — нула запис):

| заявка | днес | нова доставка |
|---|---|---|
| „детска градина дойран“ | `A3-street`, 1 | `A3-street`, **1** |
| „училище район младост“ | `A3-district`, 12 | **12** (9 с квартал) |
| „младост“ | `M7-bare`, 28 | **20** (8 с квартал / 12 без) |
| „училище младост“ | `A3-location`, 11 | **6** (3 с квартал) |
| „възраждане“ | — | `M7-bare`, **5** |
| „училище възраждане“ | — | **1** (`II ОУ „Никола Йонков Вапцаров“`) |

🔴 **К28-3 · Осемте изгубени реда на „младост“, поименно и с новия си квартал** (v2 назоваваше пет):

| # | ред | стар `zone` | нов квартал |
|---|---|---|---|
| 1 | `ОУ „Иван Вазов“` | район Младост | `pobeda` · ж.к. Победа |
| 2 | `Професионална гимназия по електротехника` | район Младост | `pobeda` · ж.к. Победа |
| 3 | `Професионална Техническа Гимназия` | район Младост | `pobeda` · ж.к. Победа |
| 4 | **`ДГ№53 „Слънчево зайче“`** | район Младост | `sv_ivan_rilski` · кв. Св. Иван Рилски |
| 5 | `ОУ Отец Паисий` | район Младост | `sv_ivan_rilski` · кв. Св. Иван Рилски |
| 6 | **`ДГ№26 „Изворче"`** | район Младост | `troshevo` · кв. Трошево |
| 7 | `ОУ Добри Чинтулов` | район Младост | `troshevo` · кв. Трошево |
| 8 | **`ДГ 24 "Детско градче"`** | район Младост | `troshevo` · кв. Трошево |

Механизмът (Ч): районът отговаря само докато `quarter is None` (`recall_sweep.py:1123`, `:1167`; `index.html:7064`, `:7118`). **Загуба по замисъл — иска подпис, и опашката ѝ дължи ОСЕМ делта-реда, не пет** (§4 стъпка 11, STOP 19). „училище младост“ губи 5 от същите осем (1, 2, 3, 5, 7).


 succeeded in 0ms:
## 4 · Ред на изпълнение

**[И]** изпълнител (`git -c user.name="Claude Executor" -c user.email=executor@local …`, О24) · **[П]** Петър. Между стъпка 7 и стъпка 13 пакетът е **ЧЕРВЕН по конструкция** (D19): изпълнителят записва ТОЧНИЯ набор падащи тестове (G20); всеки тест извън набора = STOP.

**0. [И] Санитарна проверка.** `git status --porcelain` (0 реда без `??`), `git log -1 --pretty='%h %an %s'`, `git rev-list --count origin/main..HEAD`, `git ls-tree -r --name-only HEAD -- scratch/places_search | grep -c "ЗА_ПОДПИС"` → **1**, `node --version` → v22.19.0. **HEAD и ahead се ЗАПИСВАТ такива, каквито са** — §1.1 е снимка от 07.09 и котвата се движи.

**1. [И] Записва плана.** `docs/plans/ПЛАН_Б3_07.09.md` → комит `docs(plan): Б3 quarter search delivery plan v3 (signed 07.09)`.

**2. [И] Препис на трите блоба + ПЪЛНАТА мярка ПРЕДИ редакцията.**
```bash
export PYTHONIOENCODING=utf-8
python - <<'PY'
import hashlib, gzip, pathlib
for p in ['data/places.json','data/hotels.json','data/place_categories.json']:
    b = pathlib.Path(p).read_bytes().replace(b'\r\n', b'\n')
    print(p, len(b), hashlib.sha256(b).hexdigest(), len(gzip.compress(b, 9)))
PY
```
Очаквано: точно шестте числа и трите sha от §1.4. В същия прогон се мерят `QUARTER_BY_SRC`, `LOCATION_COUNTS`, `LOCALITY_COUNT`, множеството квартални кодове, лицензните низове, **двете `_meta` МНОЖЕСТВА (§1.5б)**, **двете `quarter_attribution` карти (14 / 7) и равенството им със `SIGNED_POLYGON` кодовете**, и `P7_ADDED` (1.8.17).

**Трите мерки на покритието, преди един ред промяна** (`sys.exit(result["exit_code"])` — дословно):
```bash
python -c "from gates import coverage; import json, sys; r=coverage.run(places_base='git:f06ac06:data/places.json', places_candidate='data/places.json', hotels_base='git:f06ac06:data/hotels.json', hotels_candidate='data/hotels.json', allow_path=None, out_dir='gates/out'); print(json.dumps({'exit':r['exit_code'],'uncovered':r['uncovered'],'verdict':r['verdict']}, ensure_ascii=False)); sys.exit(r['exit_code'])"
```
очаквано **exit 2 · uncovered 138** (1.8.1).
```bash
python -c "from gates import coverage; import json, sys; r=coverage.run(places_base='git:f06ac06:data/places.json', places_candidate='git:f00dd78:data/places.json', hotels_base='git:f06ac06:data/hotels.json', hotels_candidate='git:f00dd78:data/hotels.json', allow_path=None, out_dir='gates/out'); print(json.dumps({'exit':r['exit_code'],'uncovered':r['uncovered']}, ensure_ascii=False)); sys.exit(r['exit_code'])"
```
очаквано **exit 2 · uncovered 150** — **това е дифът, който обяснява 138-те** (К28-6, О22): доставката ВРЪЩА 12 реда.
```bash
python -c "from gates import coverage; import json, sys; r=coverage.run(places_base='git:f06ac06:data/places.json', places_candidate='data/places.json', hotels_base='git:f06ac06:data/hotels.json', hotels_candidate='data/hotels.json', allow_path='gates/allow/2026-09-05_lot1v_v.json', out_dir='gates/out'); print(json.dumps({'exit':r['exit_code'],'uncovered':r['uncovered'],'stale':len(r['allow_stale'])}, ensure_ascii=False)); sys.exit(r['exit_code'])"
```
очаквано **exit 2 · uncovered 30 · stale 42** (1.8.3; 108 + 30 = 138 ✓).

И деветте заявки 1.8.4–1.8.9 през `recall_sweep`. **Всяко разминаване = STOP.**
Отрицателно доказателство: `python -m unittest tests.test_places_public_bundle tests.test_hotels_public_bundle` **сега е ЧЕРВЕН** — първият ред на G20-набора.

**3. [И] Трите маркера И12 + Node-сондата.** Първо `index.html` получава маркерите, после се създава `tests/granitsi_client_probe.mjs` — **преди** редакциите, за да има с какво да се снеме отрицателното доказателство.
Мярка: срезът с ДНЕШНИТЕ списъци над НОВИТЕ байтове → `validateHotels === false`, `validatePlaces2 === false`, **`ensurePlaces()` хвърля** (случай 9а).

**4. [И] `index.html` — четиринадесетте редакции** (§3.2). **И11 се пропуска, ако низът още не е подписан (О21)** — тогава влиза в стъпка 12б.
Мярка след: `validatePlaces2 === true`, `RECS.length === 375` (9б) и `RECS.length === 225` при мутирания places с верен пин (9в).

**5. [И] Двата bundle теста + четирите нови правила** (§3.3). `python -m unittest tests.test_places_public_bundle tests.test_hotels_public_bundle` → **0**. Отрицателно: една сменена цифра в `PLACES2_SHA256` → ≠ 0.

**6. [И] Двигателят + фикстурите** (§3.4–3.6), включително `git mv` на фикстурния файл. `python -m unittest tests.test_granitsi_fixtures -v` → **0**, единадесет фикстури, всяка с падащ `_broken`.

**7. [И] G7 — двата дъмпа** (§5 G7), с копиране след ВСЕКИ прогон.

**8. [И] Стейджва точния write-set** (`git add` с изрични пътища, никога `-A`), после `git status --short` и `git diff --cached --stat`. **Обявено:** `scratch/places_search/probe_out/token_parity.json` ще е модифициран от прогоните (О26) — той НЕ влиза в този комит, а в комит 5. Показва на Петър `scratch/places_search/COMMIT_MSG_B3.txt`.

**9. [П] Атомният комит** — §6.

**10. [И] Отваря D19-интервала и го записва.** `python -m unittest discover -s tests`; `python -m gates.run_gates` → и двете ≠ 0. Записва **поименно** какво пада, включително очакваното **coverage изход 2** на проверка 4.

**Очакванията и манифестите (report-only) — с ПРЕДВАРИТЕЛНО ИЗБРОЕНИЯ набор (О29):**
```powershell
python scratch\places_search\recall_sweep.py --manifest
```
🔴 **Очакван изход: 1** (не 0). Очакван набор — **59 реда `ЧЕРВЕНО` върху 41 уникални заявки + 2 реда без заявка**, и точно тези гейт-резултати: П7 **16/32**, ЛОТ 1 **6/18**, ЛОТ 1в-А **5/12**, ЛОТ 1в-Б **5/6**, ЛОТ 1в-В **4/10**, М7 **17/17**, §10 sweep 60/62 · 10/10 („срещу подписа 1“). Допуснатите разминавания, поименно:
- **зона-преписване без промяна на броя** (редът е същият, `zone` е новият квартал): `хотел зпз`, `горчива чешма хотел`, `училище свети никола`, `менделеев`, `хотел марина парк`, `училище менделеев стефан`, `училище аспарухово`, `детска градина аспарухово`, `1 ег`, `училище морска градина`, `ГРАДИНА`, `градина`, `детско заведение`, `детски заведения`, `ясла`, `детска ясла`, `детска градина`, `военноморско`, `военноморско училище`, `гимназия`, `поликлиника`, `езикова гимназия`, `морско училище`, `варна`, `училище район младост`, `район младост`, `детска градина владислав варненчик`;
- **сменен брой** (числото е в скобите, старо → ново): `владиславово детска градина` (4→5), `детска градина владиславово` (4→5), `хотел чайка` (18→19), `хотел златни` (96→98), `хотел приморски` (29→22), `детска градина приморски` (12→7), `училище приморски` (14→9), `университет приморски` (5→3), `хотел одесос` (40→32), **`училище младост` (11→6)**, `болница изгрев` (11→1, и клонът от `M2-failopen` на `A3-location`);
- **два реда без заявка:** `p7_added: 7 токена в 5 зони, подписани са 2 в 2` и списъкът на добавените (1.8.17, О28).
🔴 **Прогонът се прави ВЕДНЪЖ.** Втори прогон е зелен по конструкция (1.8.16, червен ред 13) — ако изпълнителят повтори командата, доказателството е унищожено и лотът СПИРА (STOP 20).

```powershell
python -m gates.release
```
Очаквано: **6 (BLOCKED)**; делтите по кофи се записват дословно (мярка в клонинг: **119 делти**, референция 203/3160 · кандидат 226/3222).

**11. [И] Опашката.** `scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md`: три класа редове (въпрос / артефакт / делта), решения `pending`, без code fence и без HTML коментари. **Задължителни редове:**
- всяка делта на `gates.release`;
- шестте `SIGNABLE` + новият allow;
- **ред „въпрос“ за низа на атрибуцията** с `тяло: c6d29d4e1d3c4fa916224ae03ceab3682fd43cc83d3f22b920183d9b82d4002d` (sha256 на низа) и `тяло-на-файла: c57a79c222361dc5c803823883374f9e1dcd12d36e7b27f05788ac17b7c22bfc` (`body_digest`) — **сверява ги G9, не release** (О21);
- 🔴 **ОСЕМ делта-реда за загубените на „младост“** (1.7), всеки с името и новия квартал (К28-3);
- **ред „въпрос“ за `P7_ADDED` дрейфа** (О28) с двата списъка дословно;
- **ред „въпрос“ за мълчаливия UI отказ** (О27);
- ред за Перчемлията (О6);
- редовете по О15/О16/О20 („детската заявка не намира детето — прието“, „чайка се слива без подписано родство — прието“, „fallback етикетът се приема в двете форми“).

В същия комит: `git mv` на старата опашка към `архив/АРХИВ_A_05.09.md` (О25), новият allow (138 реда), махнатият стар allow.
Комит **[И]**: `docs: queue and manifests for the Б3 delivery signatures (07.09)`.
Мярка веднага след комита (семантиката на release, не `grep`):
```powershell
python -c "import subprocess, posixpath, fnmatch, sys; out=subprocess.run(['git','ls-tree','-r','--name-only','-z','HEAD','--','scratch/places_search'],capture_output=True).stdout.decode('utf-8'); q=sorted(n for n in out.split(chr(0)) if n.strip() and fnmatch.fnmatchcase(posixpath.basename(n),'ЗА_ПОДПИС_*.md')); print(len(q), q); sys.exit(0 if len(q)==1 else 1)"
```
→ **1** и точно `['scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md']`.

**12. [П] Подписите.** `python -m gates.sign <id> да --all да --queue scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md` + **неговият** комит, който писалката отпечатва.
**12б. [И]** Ако низът е подписан на този етап — И11 влиза сега, в комит с `index.html` само за този ред: `feat(map): signed quarter-boundary line in the map attribution (decision 8)`. **[П]** го комитва.

**13. [И] Едно-единствено замразяване.** `python scratch\places_search\recall_sweep.py --freeze` → 0.

**14. [П] Комит на замразените тела:** `freeze: reference + expectations + parity (Б3)`.

**15. [И] Пълният гейт** — §5. Всичко зелено → одитор (друг агент, read-only).

**16. [П] Локален преглед** — §8.

**17. [П] Пушът,** от интерактивен терминал: `git rebase --autostash origin/main`, после `git push origin main`.

**18. [И] След пуша:** `docs/activeContext.md` + `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` §8; проверка, че публикуваните sha са равни на локалните; комит `docs: activeContext — Б3 delivery published, published hashes verified equal to local`; **[П]** втори пуш.

---

## 5 · Гейтове (всеки — команда с изход ≠ 0 и с ДОКАЗАНО падаща отрицателна половина)

| # | гейт | команда | очакван изход | отрицателното доказателство (ТРЯБВА да падне) |
|---|---|---|---|---|
| G1 | пиновете срещу LF-блобовете | `python -m unittest tests.test_places_public_bundle tests.test_hotels_public_bundle` | 0 | една сменена цифра в `PLACES2_SHA256` → ≠ 0 |
| G2 | единадесетте фикстури | `python -m unittest tests.test_granitsi_fixtures -v` | 0 | всеки `_broken` → `AssertionError` на назованата в `fails_on` заявка |
| **G3** 🔴 | **Node-матрицата през `ensurePlaces`** (S28-1) | същият прогон, фикстура 9 | 0 | **три отделни случая, не един:** (9а) срез с оригиналния `QUARTER_SRC` → `validateHotels === false` **И** `validatePlaces2 === false` **И** `assertRaises` върху `ensurePlaces()` с текст `places payload unavailable`; (9б) валидната доставка → `RECS === 375`; (9в) чужд код САМО в places + пин = sha на мутираното тяло (`6bfbcbf2…`, 128402 B) → `validateHotels === true`, `validatePlaces2 === false`, `RECS === 225`, **`__calls.validatePlaces2 === 1`**; (9г) crypto матрицата 1.8.11 — при ON+несъвпадащ sha **`__calls.validatePlaces2 === 0`**, така че `null` без брояч НЕ се приема за отказ; (9д) кеш v6 → стар запис се намира |
| G3б | паритет клиент ↔ референция | същият прогон, фикстура 11 | 0 | махнат `map` стъб → друг ред |
| G4 | пълният набор | `python -m unittest discover -s tests` | 0 | преди подписите: ≠ 0 — записаният G20 набор |
| G5 | седемте проверки | `python -m gates.run_gates` | **0** (7/7 ✓) | жълто („pending — Петър“) също дава 1 |
| G6 | нула **неподписани** изгубени резултати | `python -m gates.release` | 0 (преди подписите: 6) | делта без покриващ ред „да“ → 6 |
| **G7** 🔴 | **двигателят не мести кандидата** (S28-3) | вж. блока под таблицата | 0 | мутиран двигател → comparator **exit 1** (измерено) |
| **G8** 🔴 | **картончето няма ред за атрибуция — ИЗПЪЛНЕНО** (S28-7) | вж. блока под таблицата | 0 | добави `wrap.appendChild(span('pp-attrib', QUARTERS_ATTRIB))` в `popupFor` → ≠ 0 |
| **G9** 🔴 | **низът е ПОДАДЕН на `addAttribution` и е подписан** (S28-7) | вж. блока под таблицата | 0 | срезът без И11 → записаните извиквания са само `['© OpenStreetMap']` → ≠ 0 (измерено); една сменена буква → ≠ 0; неподписан ред → ≠ 0 |
| **G10** 🔴 | **първо зареждане ≤ 5 MB, по ИЗМЕРЕНИЯ набор** (S28-4) | `python -c "import pathlib,sys; f=['index.html','data/hydrants.json']; t=sum(pathlib.Path(x).stat().st_size for x in f); print(t); sys.exit(0 if t <= 5*1024*1024 else 1)"` | **0** (t = **1 878 210**) | същата команда с праг `1*1024*1024` → **exit 1** (1 878 210 > 1 048 576). Двата прага дават РАЗЛИЧНИ присъди |
| **G10б** | **отложената доставка на търсенето, отделно** | `python -c "import pathlib,sys; f=['data/hotels.json','data/places.json','data/place_categories.json']; t=sum(pathlib.Path(x).stat().st_size for x in f); print(t); sys.exit(0 if t <= 1024*1024 else 1)"` | 0 (t = **357 662**) | праг 256 KB → 1 |
| **G11** 🔴 | **нула геометрия — СТРУКТУРНО** (S28-8) | вж. блока под таблицата | 0 | ключ `"\u0063oordinates"` в мутирано копие: буквалният `grep` дава **0**, структурната проверка дава **1** (измерено) |
| G12 | нула кадастрален идентификатор | `python -m gates.run_gates` проверка 3 | зелена | вкарай `10135.1.2` → червено |
| G13 | точно един allow-json | `python -c "import pathlib,sys; n=len(list(pathlib.Path('gates/allow').glob('*.json'))); print(n); sys.exit(0 if n==1 else 1)"` | 0 | два файла → 1 |
| **G14** 🔴 | **куката е на място — БАЙТОВО в python** (S28-9) | `python -c "import pathlib,sys; a=pathlib.Path('scripts/hooks/pre-push').read_bytes(); b=pathlib.Path('.git/hooks/pre-push').read_bytes(); print(len(a),len(b),a==b); sys.exit(0 if a==b else 1)"` | 0 (2 574 = 2 574) | същата команда срещу подменено копие в скрачпада → **exit 1** (измерено). **`diff` в PowerShell е `Compare-Object`** и сравнява имена, не байтове |
| **G15** 🔴 | **точно една опашка в HEAD, по семантиката на release** (S28-10) | командата от §4 стъпка 11 | 0 | подпапка `архив/` със СЪЩОТО име → пак **1 попадение** и `release` пак BLOCKED (измерено); само смяна на името дава `[]` |
| G16 | местността не е отворена (О18) | тест в bundle-ите: `DISTRICT_FALLBACK not in LOCALITY_SRC` и всеки доставен `locality.src ∈ LOCALITY_SRC` | 0 | `locality.src = "DISTRICT_FALLBACK"` в мутиран кандидат → ≠ 0 |
| **G17** 🔴 | **`_meta` е ЗАТВОРЕНО МНОЖЕСТВО, `src` е затворен списък, url-ите са по извор** (S28-6, О17) | фикстура + правило 4 на §3.3 | 0 | вж. блока под таблицата — **четири мутации, всяка със СЪЩИЯ брой ключове** |
| **G18** | покритието (кодът се ЗАЧИТА) | трите команди от §4 стъпка 2, всяка със `sys.exit(r['exit_code'])` | 2 / 2 / 2 (преди новия allow) | без `sys.exit` командата връща **0** при вътрешен `exit_code = 2` (S28-5) |

**G7 — дословно (S28-3):**
```powershell
python scratch\places_search\recall_sweep.py
copy /Y "%TEMP%\fv_measures\lot1v_v_candidate_rows.json" "<scratch>\g7_dump_A.json"
```
после промяната в `recall_sweep.py`, същите блобове, същата ревизия на данните:
```powershell
python scratch\places_search\recall_sweep.py
copy /Y "%TEMP%\fv_measures\lot1v_v_candidate_rows.json" "<scratch>\g7_dump_B.json"
```
comparator (дословно, exit 1 при разлика):
```powershell
python -c "import pathlib,sys; a=pathlib.Path(r'<scratch>\g7_dump_A.json').read_bytes(); b=pathlib.Path(r'<scratch>\g7_dump_B.json').read_bytes(); print(len(a),len(b),a==b); sys.exit(0 if a==b else 1)"
```
**Измерено от планера в клонинг:** два прогона с един и същ двигател → **1 324 215 B, байт-еднакви, exit 0**. Отрицателна половина: `CENTER = (43.2000, 27.9000)` в копие на двигателя → **1 324 210 B, exit 1**. 🔴 **`OUTDIR` е ОБЩ (`recall_sweep.py:84`) — без `copy` след ВСЕКИ прогон гейтът сравнява последния файл със самия себе си.** Ревизиите на двигателя се пинват в отчета (`git rev-parse HEAD:scratch/places_search/recall_sweep.py` преди и след).

**G8 — дословно (S28-7):** тест, който изрязва среза по маркерите И12 (start … „card slice end“), вдига го с DOM стъб и **ИЗПЪЛНЯВА `popupFor` за всеки от 375-те записа**, после сравнява текста на върнатото поддърво:
```js
const FORBIDDEN = ['Wikimapia', 'wikimapia', 'quarter_attribution',
                   'QUARTERS_ATTRIB', 'CC BY-SA', 'Кварталните граници'];

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8 | Select-Object -Skip 715 -First 95" in C:\git\Fire_Varna
 succeeded in 14ms:


## 6 · Комити (кой какво комитва)

Причината за атомността е механична: `index.html` пинва sha на данните — при какъвто и да е разрез съществува HEAD, в който пиновете и блобовете не си съответстват и търсенето на места умира.

| # | автор (наложен) | съдържание | съобщение (дословно) |
|---|---|---|---|
| 1 | `Claude Executor <executor@local>` (флагове, О24) | `docs/plans/ПЛАН_Б3_07.09.md` | `docs(plan): Б3 quarter search delivery plan v3 (signed 07.09)` |
| 2 | **`Petar1984`** (неговата ръка) | `data/places.json`, `data/hotels.json`, `data/place_categories.json`, `index.html`, `tests/test_places_public_bundle.py`, `tests/test_hotels_public_bundle.py`, `tests/test_granitsi_fixtures.py`, `tests/granitsi_client_probe.mjs`, `scratch/places_search/granitsi_fixtures_07.09.json` (+ изтритият `…_06.09.json`), `scratch/places_search/recall_sweep.py` | виж по-долу |
| 3 | `Claude Executor` | опашката Б3, **преименуваната `архив/АРХИВ_A_05.09.md`**, трите манифеста, новият `gates/allow/2026-09-07_b3.json` (138 реда, pending), махнатият стар allow. **`gates/baseline/MANIFEST.json` НЕ се пипа (О22).** | `docs: queue and manifests for the Б3 delivery signatures (07.09)` |
| 4 | **`Petar1984`** | каквото `gates.sign` е записало | съобщението, което писалката **отпечатва** |
| 4б | **`Petar1984`** (само ако низът се подписва отделно) | `index.html` (И11) | `feat(map): signed quarter-boundary line in the map attribution (decision 8)` |
| 5 | **`Petar1984`** | `recall_sweep_rows.json`, `expectations.json`, `probe_out/token_parity.json` | `freeze: reference + expectations + parity (Б3)` |
| 6 | `Claude Executor` (след пуша) | `docs/activeContext.md`, `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` | `docs: activeContext — Б3 delivery published, published hashes verified equal to local` |

Съобщението на комит 2, дословно (`scratch/places_search/COMMIT_MSG_B3.txt`):

```
feat(search): quarter search over signed boundaries, QUARTER_CODES +8, cache v7 (D13 atomic delivery)

data: places delivery with quarter_attribution (D13 ordered) — the three blobs of
varna_3d 05f485e (places 3dffc264, hotels eb8fa85c, categories 9064705a), with the
closed lists, the three pins, LEGACY_BUNDLE_SHA and PLACES_CACHE v7 in this very
commit, because a HEAD whose pins and blobs disagree kills the place search.
tests: S17 fixtures fail on broken candidates
```

Командите за комит 2 (PowerShell, по една на ред, без `&&`):
```powershell
cd C:\git\Fire_Varna
git status --short
git diff --cached --stat
git commit -F scratch\places_search\COMMIT_MSG_B3.txt
git log -1 --pretty='%h %an <%ae> · %cn <%ce> · %s'
```
**Следпроверка (О24):** последният ред трябва да върне `Petar1984 <petar.dikov2019@gmail.com>` и като автор, и като комитър. Предварителното `git config user.name` **не доказва нищо**.

---

## 7 · STOP условия

1. **Всяко число от §1, премерено различно** — трите sha, шестте байта/gzip, осемте липсващи кода, числата на фикстурите, **и новите: 138 / 150 / (30 + 42) на покритието, 1 878 210 B първо зареждане, 1 опашка в HEAD, деветте заявки 1.8.4–1.8.9, двете `_meta` множества, двете карти 14/7**.
2. `gates.release` дава делта, която опашката не покрива, или ред „не“ (терминален).
3. `gates/out/coverage.json` иска allow-ред, който не се извежда механично.
4. Паднал тест **извън** записания D19/G20 набор.
5. `python -m gates.run_gates` жълто, третирано като зелено.
6. Дифът на кандидата преди/след промяната в `recall_sweep.py` е ≠ 0 байта (G7).
7. Липсващ `node`, липсващ маркер за среза, или Node-фикстура, минала **без** `map`/`fetch`/**`crypto`** стъб.
8. Опит за комит на данни от агент · `push` от агент · `--no-verify` · пипане на `.git/hooks`.
9. Работното дърво не е чисто по проследен файл при старта, или чужд стейджнат диф.
10. Решение 10 / резервът за Перчемлията (О6) не е подписан и одиторът настоява.
11. Износът е сменил лицензен низ, а константата в теста и README не са в същия комит.
12. Петър не е видял картата локално преди пуша.
13. **Повече от една опашка в HEAD** (по семантиката на `queues_in_head`, не по `grep`) или повече от един allow-json.
14. **`_meta.inputs` не съдържа обявеното множество**, или `INPUT_RELS` е пипнат.
15. **Комит с автор `Petar1984`, направен не от неговата ръка** (О24).
16. **Низът за атрибуция е влязъл в `index.html` преди подписания ред с двата му дайджеста** (О21).
17. **`gates/baseline/MANIFEST.json` е пипнат** (О22).
18. Проследеният `probe_out/token_parity.json` се появи в комит 2 вместо в комит 5 (О26).
19. 🔴 **Опашката носи по-малко от ОСЕМ делта-реда за загубените на „младост“** (1.7, К28-3).
20. 🔴 **`--manifest` е пуснат повече от веднъж преди подписите** (1.8.16, О30) — второто число е вакуумно зелено и не е доказателство.
21. 🔴 **Стар/нов файл със `SIGNED_POLYGON` код, който `quarter_attribution` не носи, ИЛИ запис в картата без такъв ред** — равенството е гейт и в двете посоки (G17).
22. 🔴 **Нов проследен файл извън поименния списък на G11.**

---

## 8 · Локален преглед (как Петър гледа)

```powershell
cd C:\git\Fire_Varna
python -m http.server 8000
```
`http://localhost:8000/index.html`, отворена конзола, ширина 375 px, Hard reload (кешът вече е v7). Първо: конзолата е чиста и **няма** реда `legacy_by_row: друг пакет…`.

| # | пишеш | очакваш (числата са измерени 07.09) |
|---|---|---|
| 1 | `Кайсиева градина` | в нашата секция — **3 реда `M2-failopen`**, нито един квартален; в адресната търсачка отгоре — 9 реда. |
| 2 | `училище Възраждане 3` | **2 реда по ИМЕТО**: `3 ОУ Ангел Кънчев` [**кв. Левски**] и `III ПМГ` [**кв. Тракия**] — **нито един не е във Възраждане 3**. Шум по името, не отговор по квартал. |
| 3 | `възраждане`, после `възраждане 2` | **5** реда (`ДГ 29 „Звънче“`, `ДГ 31 „Крилатко“`, `II ОУ „Никола Йонков Вапцаров“`, `ДГ 33 „Делфинче“`, `ДГ№34 „Лястовичка“`) и **0 реда** за детето. **Половината „дете → детето“ НЕ работи** (О16) — това подписваш. |
| 4 | `левски`, после `кв. Левски` | голото `левски` → **14 реда, 12 с код `kv_levski`**. `кв. Левски` → **4 ЧУЖДИ реда** (`НУ Васил Левски` [кв. Аспарухово], `ПГ „Васил Левски“`, `ДГ№40` [кв. Владиславово], болница). Същото за `кв. Тракия` (**1**, и той е `dolna_traka`), `кв. Христо Ботев` (**24**, от които **точно 1** е `hristo_botev` — `ЦДГ 8 - Христо Ботев`, и то по име), `ж.к. Св. Иван Рилски` (**22**, нула с кода). **Ако избереш вариант Б по §9 т. 1, тези четири стават 14 / 4 / 4 / 4 с 12 / 4 / 3 / 2 верни реда.** |
| 5 | `бриз` | 🔴 **4 реда** (не 2): `ПАРК ХОТЕЛ БРИЗ` [к.к. Златни пясъци — **по име**], `IV ЕГ Жолио Кюри` [ж.к. Бриз, нов], `ПГ „Д. И. Менделеев“` [ж.к. Бриз, нов], `Камелия` [ж.к. Бриз, заварен]. Двата нови са `SIGNED_POLYGON`. |
| 6 | `чайка` | **30 реда** — 19 `chaika_kk` + 10 `chaika_kv` + `„ДКЦ Чайка“ ЕООД` (без квартал). Фразата слива двата кода без подписано родство (О16). |
| 7 | `аспарухово`, после `дружба` | **16** реда (9 с `asparuhovo`, 7 „район Аспарухово“) **без** `ЦДГ 43 „Пинокио“`, и **2** реда. Подписаното родство `druzhba ⊂ asparuhovo` **не действа**. |
| 8 | `Никея` (хотел в Чайка) → картончето | ред **„вид · к.к. Чайка · район Приморски“**; **НЯМА ред за извор** (измерено: 375/375 картончета без нито един от забранените низове); долу вляво, до `© OpenStreetMap`, стои низът за границите. |
| 9 | `училище район Младост` / `младост` | **12** / **20**. Изричното районно търсене задържа и петте училища със собствен квартал. |
| 10 | **надписът при 375 px** | низът е **338 знака** и застава в същия долен ляв ъгъл, където са бутоните `+`/`−` (`:1900` и `:1917`). Проверява се **на екрана**: бутоните `+`/`−` и локацията остават **видими и натискаеми** при трите базови карти. Ако не са — §9 т. 7, вариант „къс низ“. |
| 11 🔴 | **отказът, който мълчи** (О27) | ако някога доставка донесе код извън списъка, в нашата секция ще има **225 реда вместо 375 и НУЛА съобщение**. Днес това не се вижда — подписваш го като известно поведение. |

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8 | Select-Object -Skip 885 -First 110" in C:\git\Fire_Varna
 succeeded in 15ms:
| 7 | **v2 §3.6 т. 4:** „`RECS.length === 225` при среза с оригиналния `QUARTER_SRC`“ | **Отхвърлено по мярка (1.6).** При оригиналния списък и двата пакета падат и `ensurePlaces` **хвърля** `places payload unavailable` — няма `RECS`. 225 идва само от случая, в който **само** places е отказан (9в). |
| 8 | **v2 G10:** `git ls-files index.html 'data/*.json'` като „проследените файлове“ | **Отхвърлено по мярка (1.8.14).** 19 файла, **26 839 286 B**, exit **1** — червено преди промяната. Наборът включва архивни снимки на хидрантите, `search_index.json` (11,2 MB) и `address_rows.json` (5,07 MB), които клиентът НЕ тегли при първо отваряне. |
| 9 | **v2 G17:** „`Object.keys(d._meta).length !== META_KEYS_*`“ | **Отхвърлено по мярка.** Изпълнено: преименуване на `generated` на `unexpected` пази 10 ключа и връща **true**. Броят не е множество. |
| 10 | **v2 G14:** `diff scripts/hooks/pre-push .git/hooks/pre-push` | **Отхвърлено по мярка (1.8.22).** В PowerShell `diff` е `Alias → Compare-Object`; командата сравнява имена и излиза с 0 при подменена кука. |
| 11 | **v2 G11:** буквален `grep coordinates` | **Отхвърлено по мярка (1.8.12).** Ключ `"\u0063oordinates"`: grep → 0 попадения (exit 1), parse → `coordinates`. Освен това единственото буквално попадение днес е ПРОЗА в стойност, не ключ. |

## 14 · Подпис и прочит на §9 „по препоръките“ (07.09.2026)
Петър: „подписвам плана Б3 v3 по препоръките“. Прочитът на седемнадесетте решения, дословно по препоръките на §9:
1 → **(Б)** евтината префиксна поправка в двата двигателя (само буквените `M7_PREFIXES`; числата остават извън) · 2 → родството се **замразява** каквото е (фикстури 5–8), DAG-ът не влиза · 3 → да, +8 (=28) + гейт „списъкът == речникът“ · 4 → един атомен комит с автор `Petar1984`, наложено авторство на агентските комити · 5 → пълното типово правило на шест места + синтетична фикстура · 6 → двата етикета за fallback ред · 7 → низът в подножието влиза като ред „въпрос“ с `тяло`/`тяло-на-файла`, G9 сверява · 8 → `git mv` на фикстурния файл към 07.09 · 9 → baseline **остава** `f06ac06`, allow = 138 · 10 → мълчаливият UI отказ = обявено отклонение (О27), фикстура 9в го пинва · 11 → **ред „отложено“ за Перчемлията** в опашката (решение 10 остава отворено; §9 не дава препоръка — това е прочитът на архитекта, Петър го коригира, ако иска резерва сега) · 12 → документният дълг в отделен комит след публикуването · 13 → да, фикстура 11 · 14 → `git mv` към `scratch/places_search/архив/АРХИВ_A_05.09.md` · 15 → да, `LOCALITY_SRC` · 16 → да, затворени множества · 17 → ред „въпрос“ за `P7_ADDED` с двата списъка (псевдонимите остават, докато Петър не каже друго при подписа на опашката).
Повторните проверки Astra S29 / Кими К29 върху v3 текат по време на подписа; условие от тях влиза като амандамент (нов датиран файл) и се подписва отделно, само за делтата.


exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8 | Select-Object -Skip 565 -First 68" in C:\git\Fire_Varna
 succeeded in 0ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09.md' -Encoding UTF8 | Select-Object -Skip 635 -First 25" in C:\git\Fire_Varna
 succeeded in 0ms:
## 5 · Гейтове (всеки — команда с изход ≠ 0 и с ДОКАЗАНО падаща отрицателна половина)

| # | гейт | команда | очакван изход | отрицателното доказателство (ТРЯБВА да падне) |
|---|---|---|---|---|
| G1 | пиновете срещу LF-блобовете | `python -m unittest tests.test_places_public_bundle tests.test_hotels_public_bundle` | 0 | една сменена цифра в `PLACES2_SHA256` → ≠ 0 |
| G2 | единадесетте фикстури | `python -m unittest tests.test_granitsi_fixtures -v` | 0 | всеки `_broken` → `AssertionError` на назованата в `fails_on` заявка |
| **G3** 🔴 | **Node-матрицата през `ensurePlaces`** (S28-1) | същият прогон, фикстура 9 | 0 | **три отделни случая, не един:** (9а) срез с оригиналния `QUARTER_SRC` → `validateHotels === false` **И** `validatePlaces2 === false` **И** `assertRaises` върху `ensurePlaces()` с текст `places payload unavailable`; (9б) валидната доставка → `RECS === 375`; (9в) чужд код САМО в places + пин = sha на мутираното тяло (`6bfbcbf2…`, 128402 B) → `validateHotels === true`, `validatePlaces2 === false`, `RECS === 225`, **`__calls.validatePlaces2 === 1`**; (9г) crypto матрицата 1.8.11 — при ON+несъвпадащ sha **`__calls.validatePlaces2 === 0`**, така че `null` без брояч НЕ се приема за отказ; (9д) кеш v6 → стар запис се намира |
| G3б | паритет клиент ↔ референция | същият прогон, фикстура 11 | 0 | махнат `map` стъб → друг ред |
| G4 | пълният набор | `python -m unittest discover -s tests` | 0 | преди подписите: ≠ 0 — записаният G20 набор |
| G5 | седемте проверки | `python -m gates.run_gates` | **0** (7/7 ✓) | жълто („pending — Петър“) също дава 1 |
| G6 | нула **неподписани** изгубени резултати | `python -m gates.release` | 0 (преди подписите: 6) | делта без покриващ ред „да“ → 6 |
| **G7** 🔴 | **двигателят не мести кандидата** (S28-3) | вж. блока под таблицата | 0 | мутиран двигател → comparator **exit 1** (измерено) |
| **G8** 🔴 | **картончето няма ред за атрибуция — ИЗПЪЛНЕНО** (S28-7) | вж. блока под таблицата | 0 | добави `wrap.appendChild(span('pp-attrib', QUARTERS_ATTRIB))` в `popupFor` → ≠ 0 |
| **G9** 🔴 | **низът е ПОДАДЕН на `addAttribution` и е подписан** (S28-7) | вж. блока под таблицата | 0 | срезът без И11 → записаните извиквания са само `['© OpenStreetMap']` → ≠ 0 (измерено); една сменена буква → ≠ 0; неподписан ред → ≠ 0 |
| **G10** 🔴 | **първо зареждане ≤ 5 MB, по ИЗМЕРЕНИЯ набор** (S28-4) | `python -c "import pathlib,sys; f=['index.html','data/hydrants.json']; t=sum(pathlib.Path(x).stat().st_size for x in f); print(t); sys.exit(0 if t <= 5*1024*1024 else 1)"` | **0** (t = **1 878 210**) | същата команда с праг `1*1024*1024` → **exit 1** (1 878 210 > 1 048 576). Двата прага дават РАЗЛИЧНИ присъди |
| **G10б** | **отложената доставка на търсенето, отделно** | `python -c "import pathlib,sys; f=['data/hotels.json','data/places.json','data/place_categories.json']; t=sum(pathlib.Path(x).stat().st_size for x in f); print(t); sys.exit(0 if t <= 1024*1024 else 1)"` | 0 (t = **357 662**) | праг 256 KB → 1 |
| **G11** 🔴 | **нула геометрия — СТРУКТУРНО** (S28-8) | вж. блока под таблицата | 0 | ключ `"\u0063oordinates"` в мутирано копие: буквалният `grep` дава **0**, структурната проверка дава **1** (измерено) |
| G12 | нула кадастрален идентификатор | `python -m gates.run_gates` проверка 3 | зелена | вкарай `10135.1.2` → червено |
| G13 | точно един allow-json | `python -c "import pathlib,sys; n=len(list(pathlib.Path('gates/allow').glob('*.json'))); print(n); sys.exit(0 if n==1 else 1)"` | 0 | два файла → 1 |
| **G14** 🔴 | **куката е на място — БАЙТОВО в python** (S28-9) | `python -c "import pathlib,sys; a=pathlib.Path('scripts/hooks/pre-push').read_bytes(); b=pathlib.Path('.git/hooks/pre-push').read_bytes(); print(len(a),len(b),a==b); sys.exit(0 if a==b else 1)"` | 0 (2 574 = 2 574) | същата команда срещу подменено копие в скрачпада → **exit 1** (измерено). **`diff` в PowerShell е `Compare-Object`** и сравнява имена, не байтове |
| **G15** 🔴 | **точно една опашка в HEAD, по семантиката на release** (S28-10) | командата от §4 стъпка 11 | 0 | подпапка `архив/` със СЪЩОТО име → пак **1 попадение** и `release` пак BLOCKED (измерено); само смяна на името дава `[]` |
| G16 | местността не е отворена (О18) | тест в bundle-ите: `DISTRICT_FALLBACK not in LOCALITY_SRC` и всеки доставен `locality.src ∈ LOCALITY_SRC` | 0 | `locality.src = "DISTRICT_FALLBACK"` в мутиран кандидат → ≠ 0 |
| **G17** 🔴 | **`_meta` е ЗАТВОРЕНО МНОЖЕСТВО, `src` е затворен списък, url-ите са по извор** (S28-6, О17) | фикстура + правило 4 на §3.3 | 0 | вж. блока под таблицата — **четири мутации, всяка със СЪЩИЯ брой ключове** |
| **G18** | покритието (кодът се ЗАЧИТА) | трите команди от §4 стъпка 2, всяка със `sys.exit(r['exit_code'])` | 2 / 2 / 2 (преди новия allow) | без `sys.exit` командата връща **0** при вътрешен `exit_code = 2` (S28-5) |


exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import subprocess,hashlib,json,re,pathlib
S=lambda *a:subprocess.check_output(['git',*a])
paths=S('diff','--cached','--name-only','-z').decode().strip('\\0').split('\\0')
records=[]
for p in paths:
    try: b=S('show',':'+p)
    except subprocess.CalledProcessError: records.append({'p':p,'deleted':True});continue
    w=pathlib.Path(p).read_bytes().replace(b'\\r\\n',b'\\n')
    records.append({'p':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'worktree_LF_equal':b==w})
print(json.dumps(records,ensure_ascii=False,indent=1))
plan=pathlib.Path('docs/plans/ПЛАН_Б3_07.09.md').read_text(encoding='utf-8')
section=plan.split('Съобщението на комит 2, дословно')[1]
expected=section.split('"'```'"')[1].strip('\\n')+'\\n'
actual=pathlib.Path('scratch/places_search/COMMIT_MSG_B3.txt').read_bytes()
print('commitmsg_LF_literal_equal',expected.encode()==actual.replace(b'\\r\\n',b'\\n'),'utf8_roundtrip',actual.decode('utf-8').encode('utf-8')==actual)
print('amendments',[(p,pathlib.Path(p).stat().st_mtime,hashlib.sha256(pathlib.Path(p).read_bytes().replace(b'\\r\\n',b'\\n')).hexdigest()) for p in ['docs/plans/ПЛАН_Б3_07.09.md','docs/plans/ПЛАН_Б3_07.09_амандамент_1.md','docs/plans/ПЛАН_Б3_07.09_амандамент_2.md']])
'@ | python -X utf8 -B -" in C:\git\Fire_Varna
 exited 1 in 198ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
fatal: path 'scratch/places_search/granitsi_fixtures_06.09.json' does not exist (neither on disk nor in the index)
[
 {
  "p": "data/hotels.json",
  "bytes": 151263,
  "sha256": "eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51",
  "worktree_LF_equal": true
 },
 {
  "p": "data/place_categories.json",
  "bytes": 77998,
  "sha256": "9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231",
  "worktree_LF_equal": true
 },
 {
  "p": "data/places.json",
  "bytes": 128401,
  "sha256": "3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66",
  "worktree_LF_equal": true
 },
 {
  "p": "gates/probe/b3_g11.py",
  "bytes": 3573,
  "sha256": "259301b0e95e1e92d67de3b067551054aa31cdcad7bc9b1e782c0896d2a0863e",
  "worktree_LF_equal": true
 },
 {
  "p": "index.html",
  "bytes": 566532,
  "sha256": "f533ca229e9b0bfc2fd035a707960b94b21c5e2daa7186d335b304d061c91478",
  "worktree_LF_equal": true
 },
 {
  "p": "scratch/places_search/granitsi_fixtures_06.09.json",
  "deleted": true
 },
 {
  "p": "scratch/places_search/granitsi_fixtures_07.09.json",
  "bytes": 51875,
  "sha256": "59c59fce3882bdf96e680b95858c7710aa2c319456a5473761630b8766e104a6",
  "worktree_LF_equal": true
 },
 {
  "p": "scratch/places_search/recall_sweep.py",
  "bytes": 232691,
  "sha256": "5a051c8f1080142896822125300b94cf6bce854e52aa67dcfa95bc93293382cb",
  "worktree_LF_equal": true
 },
 {
  "p": "tests/granitsi_client_probe.mjs",
  "bytes": 12242,
  "sha256": "933a5926d4d3e92d7251fc6fa9a661f3499e8b10250e505a58bd9fb99bc2abbd",
  "worktree_LF_equal": true
 },
 {
  "p": "tests/test_b3_gates.py",
  "bytes": 10134,
  "sha256": "9a8c5a3554201879b78d22d494d2ffe51e0ad30d274e60a5634f222c6225e4e4",
  "worktree_LF_equal": true
 },
 {
  "p": "tests/test_granitsi_fixtures.py",
  "bytes": 34389,
  "sha256": "a75b26d63de55ad302b8430ae7032e4fb2fe678cc8bd6a122f8f04099c108450",
  "worktree_LF_equal": true
 },
 {
  "p": "tests/test_hotels_public_bundle.py",
  "bytes": 40386,
  "sha256": "a17483b527b7d4205f2318ba46f076f8986f0f177f9ae3ae7586a1b1b229fdb8",
  "worktree_LF_equal": true
 },
 {
  "p": "tests/test_places_public_bundle.py",
  "bytes": 34824,
  "sha256": "1846e8b0c4897f1d01fe55a5e2c65478bca64bbfcc918c8b29307c5187c05369",
  "worktree_LF_equal": true
 }
]
Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
  File "C:\Program Files\Python310\lib\pathlib.py", line 1134, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
  File "C:\Program Files\Python310\lib\pathlib.py", line 1119, in open
    return self._accessor.open(self, mode, buffering, encoding, errors,
OSError: [Errno 22] Invalid argument: 'docs\\plans\\????_?3_07.09.md'

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 'class PlacesCacheNameTest|class .*Test' tests/test_places_search_gate.py" in C:\git\Fire_Varna
 succeeded in 0ms:
tests/test_places_search_gate.py

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Select-String -LiteralPath tests/test_places_search_gate.py -Pattern '"'^class PlacesCacheNameTest|''^class .*Test'"' -Encoding UTF8" in C:\git\Fire_Varna
 succeeded in 8ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git log -3 --format='%h %an %s'" in C:\git\Fire_Varna
 succeeded in 0ms:
8cbcaf0 Claude Architect docs(plan): Б3 amendment 2 draft — auditor's minors folded in (G11 --cached declared, fixture 4 re-derived, probe fix, manifest travels with commit 5); execution 0–7 audited ГОДНО recorded
2591ab8 Claude Architect docs(plan): Б3 amendment 2 DRAFT — three mechanical items found by executors A/B (probe PLACES_CACHE copy v7 per ADR 008 D8, ALLOWED_NEW + tests/test_b3_gates.py, О26 second rewritten file); fixture 9в mutation pinned by measurement; for Petar's morning signature
4fdd303 Claude Architect docs(plan): Б3 amendment 1 SIGNED by Petar (07.09); state §8 — execution workflow starts (three executors, auditor, no agent commits)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Item -LiteralPath 'docs/plans/ПЛАН_Б3_07.09_амандамент_2.md' | Select-Object FullName,Length,LastWriteTime" in C:\git\Fire_Varna
 succeeded in 0ms:

FullName                                                   Length LastWriteTime       
--------                                                   ------ -------------       
C:\git\Fire_Varna\docs\plans\ПЛАН_Б3_07.09_амандамент_2.md   8763 9/7/2026 12:59:09 PM



exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git diff --cached --stat' in C:\git\Fire_Varna
 succeeded in 0ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
 data/hotels.json                                   |  169 ++-
 data/place_categories.json                         |  320 ++--
 data/places.json                                   |  427 ++++--
 gates/probe/b3_g11.py                              |   66 +
 index.html                                         |  130 +-
 scratch/places_search/granitsi_fixtures_06.09.json |  855 -----------
 scratch/places_search/granitsi_fixtures_07.09.json | 1572 ++++++++++++++++++++
 scratch/places_search/recall_sweep.py              |   66 +-
 tests/granitsi_client_probe.mjs                    |  278 ++++
 tests/test_b3_gates.py                             |  202 +++
 tests/test_granitsi_fixtures.py                    |  642 ++++++--
 tests/test_hotels_public_bundle.py                 |  130 +-
 tests/test_places_public_bundle.py                 |  120 +-
 13 files changed, 3722 insertions(+), 1255 deletions(-)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "python -X utf8 -B -c \"import pathlib,hashlib,subprocess; p=pathlib.Path('docs/plans/ПЛАН_Б3_07.09.md'); b=p.read_bytes(); t=b.decode('utf-8'); a=t.index('Съобщението на комит 2, дословно'); e=t[a:].split(chr(96)*3)[1].strip(chr(10)+chr(13))+chr(10); m=pathlib.Path('scratch/places_search/COMMIT_MSG_B3.txt').read_bytes(); print('commit_message_literal_equal',e.encode().replace(b'\\r\\n',b'\\n')==m.replace(b'\\r\\n',b'\\n')); print('utf8_roundtrip',m.decode('utf-8').encode()==m); print('HEAD',subprocess.check_output(['git','rev-parse','HEAD']).decode().strip()); print('plan_sha',hashlib.sha256(b.replace(b'\\r\\n',b'\\n')).hexdigest())\"" in C:\git\Fire_Varna
 succeeded in 0ms:
commit_message_literal_equal True
utf8_roundtrip True
HEAD 8cbcaf039dba5b46ea69e4884d26e951a62b545c
plan_sha fb24f9dece7c1deafa2dee504b1dc7f5d1d9aff4ee6d0bbc7b8e53ff527d7653

codex
Всичките 16 hunks в `index.html` се съпоставят с разрешените редакции; И11 отсъства, а паритетният участък е непокътнат. Открит е проблем в G11: при невалиден родител скриптът връща успех.

Междувременно друг процес е придвижил HEAD от `2591ab8` до `8cbcaf0` и е разширил черновата на амандамент №2. Ще довърша одита спрямо заявения `2591ab8` и ще проверя дали 13-те стейджнати тела са останали същите.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath gates/probe/b3_g11.py -Encoding UTF8 -TotalCount 100' in C:\git\Fire_Varna
 succeeded in 0ms:
# -*- coding: utf-8 -*-
"""G11 — нула геометрия, СТРУКТУРНО, по ЦЕЛИЯ комит (S29-4).

Usage: python gates/probe/b3_g11.py <parent> [--cached]

The body below is the script of амандамент №1 S29-4, verbatim, with ONE declared
extension: the optional second argument `--cached` makes `changed()` diff <parent>
against the INDEX (`git diff --cached --name-status -z --find-renames
--diff-filter=AMR <parent>`) instead of against HEAD. Reason: the Б3 data commit is
made by Petar's own hand (план §6, О4), so the gate has to be runnable on the
STAGED write-set, before that commit exists. Without the flag the behaviour is the
signed one, byte for byte: <parent> against HEAD.
"""
import json, subprocess, sys, pathlib
GEO = {"coordinates", "geometry", "geometries"}
# ТОЧНИТЕ наследени изключения: (път, JSON-указател, тип на стойността).
LEGACY = {("scratch/places_search/granitsi_fixtures_07.09.json", "/_meta/geometry", str)}
ALLOWED_NEW = {"tests/granitsi_client_probe.mjs",
               "scratch/places_search/granitsi_fixtures_07.09.json",
               "scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md",
               "gates/allow/2026-09-07_b3.json",
               "scratch/places_search/архив/АРХИВ_A_05.09.md",
               "gates/probe/b3_g11.py"}
def walk(o, path, hits):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in GEO: hits.append((path + "/" + k, type(v)))
            walk(v, path + "/" + k, hits)
    elif isinstance(o, list):
        for i, v in enumerate(o): walk(v, path + "[%d]" % i, hits)
def changed(parent, cached=False):
    cmd = ["git", "diff", "--name-status", "-z", "--find-renames",
           "--diff-filter=AMR", parent, "HEAD"]
    if cached:                                # the staged write-set, before the commit
        cmd = ["git", "diff", "--cached", "--name-status", "-z", "--find-renames",
               "--diff-filter=AMR", parent]
    parts = [p for p in subprocess.run(cmd,
        capture_output=True).stdout.decode("utf-8").split(chr(0)) if p != ""]
    files, new, i = [], [], 0
    while i < len(parts):                     # R носи ДВА пътя, A и M — по един
        if parts[i][0] == "R": files.append(parts[i + 2]); i += 3
        else:
            if parts[i][0] == "A": new.append(parts[i + 1])
            files.append(parts[i + 1]); i += 2
    return files, new
def main(parent, cached=False):
    tracked = [f for f in subprocess.run(["git", "ls-files", "data/"],
               capture_output=True, text=True).stdout.split() if f.endswith(".json")]
    touched, new = changed(parent, cached)
    scope = sorted(set(tracked) | set(f for f in touched
                   if f.lower().endswith((".json", ".geojson"))))
    bad, unread = [], []
    for f in scope:
        p = pathlib.Path(f)
        if not p.exists(): continue
        try: doc = json.loads(p.read_text(encoding="utf-8"))
        except ValueError as exc: unread.append((f, str(exc))); continue
        hits = []; walk(doc, "", hits)
        bad += [(f, ptr, typ.__name__) for ptr, typ in hits
                if (f, ptr, typ) not in LEGACY]
    stray = sorted(set(new) - ALLOWED_NEW)
    print(json.dumps({"scope": len(scope), "geo_hits": bad, "unreadable": unread,
                      "stray_new": stray}, ensure_ascii=False))
    sys.exit(0 if not bad and not unread and not stray else 1)
if __name__ == "__main__":
    main(sys.argv[1], "--cached" in sys.argv[2:])

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath tests/test_places_search_gate.py -Encoding UTF8 | Select-Object -Skip 2710 -First 32' in C:\git\Fire_Varna
 succeeded in 16ms:
        deaf = run_gates.check_signature_authorship()
        self.assertEqual(deaf.mark, run_gates.BAD, deaf.lines)
        self.assertTrue([line for line in deaf.lines if u"HEAD носи опашка" in line],
                        deaf.lines)


class PlacesCacheNameTest(unittest.TestCase):
    """ADR 008 D8: the cache namespace is a hand-kept copy on two sides.

    `index.html` owns the name and changes it with every change of the blobs; the
    probe WRITES a stale body into that namespace (the В7 staleCache refusal) and
    reads it back (the warm scenario). A stale copy in the probe turns the refusal
    scenario into a plain 404 in silence — measured on F5-а, where the constant
    moved to v3-225. `sw.js` must NOT protect it (D8): the SW does not cache it.
    """

    def test_the_probe_uses_the_name_index_html_owns(self):
        index = re.search(r"const PLACES_CACHE = '([^']+)'", INDEX.read_text(encoding="utf-8"))
        probe = re.search(r'const PLACES_CACHE = "([^"]+)"', PROBE.read_text(encoding="utf-8"))
        self.assertIsNotNone(index, "PLACES_CACHE is gone from index.html")
        self.assertIsNotNone(probe, "PLACES_CACHE is gone from the probe")
        self.assertEqual(index.group(1), probe.group(1))

    def test_the_service_worker_does_not_protect_the_places_cache(self):
        name = re.search(r"const PLACES_CACHE = '([^']+)'",
                         INDEX.read_text(encoding="utf-8")).group(1)
        self.assertNotIn(name, (REPO / "sw.js").read_text(encoding="utf-8"))


class Lot1FormTableTest(unittest.TestCase):
    """Амандамент №8 П2 („детско заведение“) — gated WITHOUT a browser.


exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git diff --name-status 2591ab8 8cbcaf0' in C:\git\Fire_Varna
 succeeded in 0ms:
M	docs/plans/ПЛАН_Б3_07.09_амандамент_2.md

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git diff --cached --check' in C:\git\Fire_Varna
 succeeded in 0ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied

codex
Валидаторите приеха двете чисти доставки и отхвърлиха всичките 26 мутации, включително смяна на ключ при запазен брой и разминаване карта↔`SIGNED_POLYGON`. G8 също мина: 375 картончета без атрибуция, а подхвърленият ред се улавя.

Втората проба на G11 потвърди отделен пропуск: `--cached` избира пътищата от индекса, но чете съдържанието от работното дърво. Така стейджната геометрия може да бъде скрита с чисто нестейджнато копие.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "python -X utf8 -B -c \"import subprocess,hashlib,json; paths=['data/hotels.json','data/place_categories.json','data/places.json','gates/probe/b3_g11.py','index.html','scratch/places_search/granitsi_fixtures_07.09.json','scratch/places_search/recall_sweep.py','tests/granitsi_client_probe.mjs','tests/test_b3_gates.py','tests/test_granitsi_fixtures.py','tests/test_hotels_public_bundle.py','tests/test_places_public_bundle.py']; print(json.dumps({p:hashlib.sha256(subprocess.check_output(['git','show',':'+p])).hexdigest() for p in paths},indent=1)); print('unstaged_tracked'); print(subprocess.check_output(['git','diff','--name-only']).decode())\"" in C:\git\Fire_Varna
 succeeded in 182ms:
{
 "data/hotels.json": "eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51",
 "data/place_categories.json": "9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231",
 "data/places.json": "3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66",
 "gates/probe/b3_g11.py": "259301b0e95e1e92d67de3b067551054aa31cdcad7bc9b1e782c0896d2a0863e",
 "index.html": "f533ca229e9b0bfc2fd035a707960b94b21c5e2daa7186d335b304d061c91478",
 "scratch/places_search/granitsi_fixtures_07.09.json": "59c59fce3882bdf96e680b95858c7710aa2c319456a5473761630b8766e104a6",
 "scratch/places_search/recall_sweep.py": "5a051c8f1080142896822125300b94cf6bce854e52aa67dcfa95bc93293382cb",
 "tests/granitsi_client_probe.mjs": "933a5926d4d3e92d7251fc6fa9a661f3499e8b10250e505a58bd9fb99bc2abbd",
 "tests/test_b3_gates.py": "9a8c5a3554201879b78d22d494d2ffe51e0ad30d274e60a5634f222c6225e4e4",
 "tests/test_granitsi_fixtures.py": "a75b26d63de55ad302b8430ae7032e4fb2fe678cc8bd6a122f8f04099c108450",
 "tests/test_hotels_public_bundle.py": "a17483b527b7d4205f2318ba46f076f8986f0f177f9ae3ae7586a1b1b229fdb8",
 "tests/test_places_public_bundle.py": "1846e8b0c4897f1d01fe55a5e2c65478bca64bbfcc918c8b29307c5187c05369"
}
unstaged_tracked
scratch/places_search/lot1v_v_reference_manifest.json
scratch/places_search/probe_out/token_parity.json


exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Б3_07.09_амандамент_2.md' -Encoding UTF8 | Select-Object -Skip 17 -First 35" in C:\git\Fire_Varna
 succeeded in 0ms:
**Мярка (A/B):** обикновеният (не-freeze) прогон на `recall_sweep.py` пише и `scratch/places_search/lot1v_v_reference_manifest.json` (проследен), не само `probe_out/token_parity.json`. Дали байтовете се менят при днешните прогони: виж реда „git diff --stat“ в доклада на изпълнител C.
**Поправка:** О26 и §4 стъпка 7 назовават и двата файла; ако манифестът е променен, той пътува с комит 5 (замразяването), не с комит 2; ако е байт-еднакъв — записва се, че е бил пренаписан без промяна.

### А2-4 · G11 приема `--cached` (обявено разширение на подписания скрипт)
**Мярка (A, одитор):** амандамент 1 S29-4 дава скрипта дословно с команда `python gates\probe3_g11.py <parent>` (диф родител→HEAD). Комит 2 е ръката на Петър (§6, О4) — гейтът трябва да е изпълним ВЪРХУ СТЕЙДЖА, преди комитът да съществува. Изпълнител A добави втори режим: `python gates/probe/b3_g11.py HEAD --cached` (диф родител→индекс), обявен в докстринга; без флага поведението е подписаното байт за байт.
**Поправка:** редът се подписва като част от S29-4. Гейт: `--cached` върху стейджа → 0 след А2-2; след комита на Петър — и без флага → 0.

## 2 · Уточнения, които НЕ са поправки (записват се за подписа)
**Фикстура 9в:** пинът на плана за мутираното тяло (128 402 B / `6bfbcbf2…`) не се възпроизвежда; §3.5 казва, че числата се преизмерват. Мутацията се записва дословно: първият обект `"quarter"` със `"src": "SIGNED_POLYGON"` в `data/places.json` получава `"code": "tsentar_new"` (беше `kv_levski`) → тяло 128 403 B, sha256 `2064527328899246c32b0c83f8fc3dba9c01d1cbbb67791a6dcc18e88c997733`. Изпълнител C я пинна така (`was_code: kv_levski`); одиторът я премери независимо: същите байтове и sha.
**Фикстура 4 (`order_identity`):** „заварената“ мутация вече ДОБАВЯ ред (ОУ „Иван Вазов“ отиде в ж.к. Победа с доставката: 20 → 21), а фикстурата съществува, за да покаже, че сравнение по множество не лови пренареждане. Преизведена по същия клас като 6/7/8: `27 ДГ Успех` получава квартал {ж.к. Младост, mladost, SIGNED_POLYGON} при непипнат `zone` → 20 реда, СЪЩОТО множество, ред 12 → ред 2. Одиторът: „same SET=True, same ORDER=False“ — точно това, което фикстурата пази.
**`tests/granitsi_client_probe.mjs`:** изпълнител C поправи 4 реда в сондата на A (askът `search` чете `x.e.name`, защото клиентският ред е обвивката `{e: record, …}`); без поправката фикстура 11 щеше да сравнява `[null, null, …]` — вакуумно зелено. Файлът е в същия некомитнат write-set; подписаното не е пипано.
**Харнесът** брои `with_quarter`/`without_quarter` по `own_quarter(r)`, не по суровото поле (иначе DISTRICT_FALLBACK ред би се броил за квартален); върху днешната доставка (0 fallback реда) разликата е нула.

## 3 · Изпълнение и одит (нощта на 07→08.09, за протокола)
Стъпки 0–7 са изпълнени (изпълнители A, B, C; Opus) и одитирани (**ГОДНО**, 8 минора, нула блокери/майори): 13 пътя стейджнати, нищо комитнато; червеният набор D19/G20 е точно обявеният — 25 теста (21 замразена референция → стъпка 13; 3 `MapAttributionTest` → 12б; 1 `PlacesCacheNameTest` → А2-1), `run_gates` две червени (покритие exit 2 → стъпка 11; release BLOCKED 2 → стъпки 11/13/14 + А2-3), G11 `--cached` само `stray_new tests/test_b3_gates.py` → А2-2. Кими К30 / Astra S30 върху стейджнатия диф — виж записите.

## 4 · Какво подписва Петър
Един подпис за четирите реда: А2-1 (v7 в сондата), А2-2 (`ALLOWED_NEW` + `tests/test_b3_gates.py`), А2-3 (манифестът пътува с комит 5, препоръка б), А2-4 (`--cached`), плюс уточненията в §2. Нищо от 17-те решения не се променя. **Редът сутринта:** подпис → изпълнител прилага А2-1/А2-2 (два реда) и ги стейджва → атомният комит 2 на Петър.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "python -X utf8 -B -c \"import subprocess,hashlib,gzip,json; rows=[]; targets={'data/places.json':('places',10),'data/hotels.json':('hotels',8),'data/place_categories.json':('',0)}; pattern=__import__('re').compile(r'[\\u00D0\\u00D1\\u00C2][\\u0080-\\u00FF]'); changed=subprocess.check_output(['git','diff','--cached','--name-only','--diff-filter=ACMR','-z']).decode().split(chr(0)); bad=[]; print('all_staged_utf8_roundtrip_mojibake'); [(bad.append(p) if pattern.search(subprocess.check_output(['git','show',':'+p]).decode('utf-8')) else None) for p in changed if p]; print('bad',bad); [(rows.append((p,len(b),len(gzip.compress(b,9)),hashlib.sha256(b).hexdigest())) ) for p in targets for b in [subprocess.check_output(['git','show',':'+p])]]; print(json.dumps(rows));\"" in C:\git\Fire_Varna
 succeeded in 208ms:
all_staged_utf8_roundtrip_mojibake
bad []
[["data/places.json", 128401, 14748, "3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66"], ["data/hotels.json", 151263, 13642, "eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51"], ["data/place_categories.json", 77998, 9690, "9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231"]]

codex
И трите избрани `_broken` мутации промениха точно своите `fails_on`; Node проверките за отказ и реда на резултатите също минаха.

Намерихме още един блокер: двата bundle теста дават `66 OK` и при сменена цифра в клиентския `PLACES2_SHA256`. Те сравняват данните със собствени SHA константи и изобщо не четат `index.html`, затова обещаната отрицателна половина на G1 не работи.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "python -X utf8 -B -c \"import pathlib; p=pathlib.Path('tests/test_places_public_bundle.py'); a=p.read_text(encoding='utf-8').splitlines(); print('\\n'.join(str(i+1)+': '+a[i] for i in range(245,267))); p=pathlib.Path('tests/test_hotels_public_bundle.py'); a=p.read_text(encoding='utf-8').splitlines(); print('\\n'.join(str(i+1)+': '+a[i] for i in range(246,264)))\"" in C:\git\Fire_Varna
 succeeded in 0ms:
246: 
247: def read(path):
248:     raw = path.read_bytes()
249:     text = raw.decode("utf-8")
250:     return raw, text, json.loads(text)
251: 
252: 
253: class PlacesBundleTest(unittest.TestCase):
254:     @classmethod
255:     def setUpClass(cls):
256:         cls.raw, cls.text, cls.doc = read(PLACES)
257:         cls.records = cls.doc.get("places", [])
258: 
259:     def test_bytes_sha_gzip_match_the_tracked_blob(self):
260:         self.assertEqual(len(self.raw), PLACES_BYTES)
261:         self.assertEqual(hashlib.sha256(self.raw).hexdigest(), PLACES_SHA256)
262:         self.assertEqual(len(gzip.compress(self.raw, 9, mtime=0)), PLACES_GZIP9)
263: 
264:     def test_top_level_shape_and_count(self):
265:         self.assertEqual(set(self.doc.keys()), TOP_LEVEL_KEYS)
266:         self.assertIsInstance(self.records, list)
267:         self.assertEqual(self.doc["_meta"]["count"], EXPECTED_COUNT)
247:     text = raw.decode("utf-8")
248:     return raw, text, json.loads(text)
249: 
250: 
251: class HotelsBundleTest(unittest.TestCase):
252:     @classmethod
253:     def setUpClass(cls):
254:         cls.raw, cls.text, cls.doc = read(HOTELS)
255:         cls.records = cls.doc.get("hotels", [])
256: 
257:     def test_bytes_sha_gzip_match_the_tracked_blob(self):
258:         self.assertEqual(len(self.raw), HOTELS_BYTES)
259:         self.assertEqual(hashlib.sha256(self.raw).hexdigest(), HOTELS_SHA256)
260:         self.assertEqual(len(gzip.compress(self.raw, 9, mtime=0)), HOTELS_GZIP9)
261: 
262:     def test_top_level_shape_and_count(self):
263:         self.assertEqual(set(self.doc.keys()), TOP_LEVEL_KEYS)
264:         self.assertIsInstance(self.records, list)

codex
Корпусът по подписания селектор даде същите отговори за всичките 226 реда; `R \ MR` е непроменен, а четирите целеви заявки с префикс дават очакваните нови резултати. G10 и G14 дадоха различни изходи за положителната и отрицателната проба. До момента присъдата е „НЕГОДНО“ заради трите потвърдени пропуска в гейтовете; финализирам доказателствата и ограниченията на прогона.
collab: Wait
codex
**НЕГОДНО за атомния комит на Петър.** Потвърдени са три допълнителни механични блокера.

1. **S30-1 — G11 проверява други байтове.** [b3_g11.py:54](C:/git/Fire_Varna/gates/probe/b3_g11.py:54) чете работното дърво, въпреки че `--cached` избира пътищата от индекса. Проба с действителния модул и I/O стъбове: стейджнато `{"a":{"coordinates":[[1,2]]}}`, локално `{}` → **`geo_hits:[]`, exit 0**. Липсващ локален файл също се пропуска. **Поправка:** съдържание и инвентар от една Git снимка — `:<path>` при `--cached`, `HEAD:<path>` иначе; невъзможен прочит да проваля гейта. Добавяне на отрицателен тест със стейджнато/локално разминаване.

2. **S30-2 — Git грешка става зелено.** Действителният прогон `python -X utf8 -B gates/probe/b3_g11.py DOES_NOT_EXIST_S30` върна **exit 0**, `scope:18`, празни списъци. [Ред 37](C:/git/Fire_Varna/gates/probe/b3_g11.py:37) игнорира неуспешния Git процес; същото важи за инвентара. **Поправка:** проверен `returncode`/`check=True` за всички Git извиквания, запазена диагностика и отрицателен тест с несъществуващ родител.

3. **S30-3 — обещаната отрицателна половина на G1 не работи.** Едносимволна мутация в паметта на клиентския `PLACES2_SHA256`, `3dffc264…→0dffc264…`, оставя двата bundle теста **66 OK, exit 0**. Те направиха **нула прочитания на `index.html`**. [SHA тестът](C:/git/Fire_Varna/tests/test_places_public_bundle.py:259) сравнява с отделна тестова константа; мутирането именно на нея действително го проваля. **Поправка:** същата G1 команда да сверява трите клиентски пина с LF телата и да включва отрицателния тест с една сменена цифра.

Провереното изпълнение извън тези пропуски:

- Трите стейджнати блоба съвпадат с §1.4 по SHA, размер и gzip. `COMMIT_MSG_B3.txt` съвпада дословно с §6 след LF нормализация. UTF-8 проверката и `git diff --cached --check` са чисти.
- Всичките **16 hunks** на `index.html` са разрешени. Старите котви → редакции: `6253→И12; 6262→И1; 6285→И2; 6299→И3; 6310→И4/И4б/И5; 6494→И13/Б; 6532→И6/И4б/И10; 6566,6578→И10; 6746,6779→И7; 7055→И8/Б; 7115→И8; 7152→И12; 7263→И9; 7287→И12`. И11 отсъства; старият участък 7470–7480 е непокътнат. Типовото правило и двата fallback етикета минават.
- **66 bundle теста и 17 фикстурни теста — OK.** Двете чисти доставки са приети; всичките **26 валидаторни мутации** са отказани.
- Трите независимо измерени `_broken`: Възраждане **5→4**, Чайка **30→21**, Аспарухово **16→17** и Дружба **M7/2→M3/1**. Всяка променя точно `fails_on`.
- Node отказът без `fetch` е наблюдаем; без `map` се пренареждат **6/6** заявки. Фикстура 11 доказва паритет **6/6**; отделното заявено „11/11“ не е независимо потвърдено.
- Шестте места с `own_quarter` са покрити; `INPUT_RELS` е непроменен. Подписаният корпус **226 реда**, включително `R \ MR`, е без разлики. G8, G10 и G14 имат проверени положителни и отрицателни половини.

Тежките G7 дъмпове, пълният suite и `run_gates` не са повторени: наложеният read-only sandbox не позволява TEMP clone. Затова точният набор от 25 червени теста остава непотвърден независимо.

По време на одита външен процес придвижи HEAD **2591ab8→8cbcaf0**, променяйки само черновата на амандамент №2; стейджнатите тела останаха същите. Поправките изискват подписана делта, включително вече обявените неподписани точки. Не съм редактирал, стейджвал или комитвал; атомният комит остава действие на Петър.
tokens used
83,589
**НЕГОДНО за атомния комит на Петър.** Потвърдени са три допълнителни механични блокера.

1. **S30-1 — G11 проверява други байтове.** [b3_g11.py:54](C:/git/Fire_Varna/gates/probe/b3_g11.py:54) чете работното дърво, въпреки че `--cached` избира пътищата от индекса. Проба с действителния модул и I/O стъбове: стейджнато `{"a":{"coordinates":[[1,2]]}}`, локално `{}` → **`geo_hits:[]`, exit 0**. Липсващ локален файл също се пропуска. **Поправка:** съдържание и инвентар от една Git снимка — `:<path>` при `--cached`, `HEAD:<path>` иначе; невъзможен прочит да проваля гейта. Добавяне на отрицателен тест със стейджнато/локално разминаване.

2. **S30-2 — Git грешка става зелено.** Действителният прогон `python -X utf8 -B gates/probe/b3_g11.py DOES_NOT_EXIST_S30` върна **exit 0**, `scope:18`, празни списъци. [Ред 37](C:/git/Fire_Varna/gates/probe/b3_g11.py:37) игнорира неуспешния Git процес; същото важи за инвентара. **Поправка:** проверен `returncode`/`check=True` за всички Git извиквания, запазена диагностика и отрицателен тест с несъществуващ родител.

3. **S30-3 — обещаната отрицателна половина на G1 не работи.** Едносимволна мутация в паметта на клиентския `PLACES2_SHA256`, `3dffc264…→0dffc264…`, оставя двата bundle теста **66 OK, exit 0**. Те направиха **нула прочитания на `index.html`**. [SHA тестът](C:/git/Fire_Varna/tests/test_places_public_bundle.py:259) сравнява с отделна тестова константа; мутирането именно на нея действително го проваля. **Поправка:** същата G1 команда да сверява трите клиентски пина с LF телата и да включва отрицателния тест с една сменена цифра.

Провереното изпълнение извън тези пропуски:

- Трите стейджнати блоба съвпадат с §1.4 по SHA, размер и gzip. `COMMIT_MSG_B3.txt` съвпада дословно с §6 след LF нормализация. UTF-8 проверката и `git diff --cached --check` са чисти.
- Всичките **16 hunks** на `index.html` са разрешени. Старите котви → редакции: `6253→И12; 6262→И1; 6285→И2; 6299→И3; 6310→И4/И4б/И5; 6494→И13/Б; 6532→И6/И4б/И10; 6566,6578→И10; 6746,6779→И7; 7055→И8/Б; 7115→И8; 7152→И12; 7263→И9; 7287→И12`. И11 отсъства; старият участък 7470–7480 е непокътнат. Типовото правило и двата fallback етикета минават.
- **66 bundle теста и 17 фикстурни теста — OK.** Двете чисти доставки са приети; всичките **26 валидаторни мутации** са отказани.
- Трите независимо измерени `_broken`: Възраждане **5→4**, Чайка **30→21**, Аспарухово **16→17** и Дружба **M7/2→M3/1**. Всяка променя точно `fails_on`.
- Node отказът без `fetch` е наблюдаем; без `map` се пренареждат **6/6** заявки. Фикстура 11 доказва паритет **6/6**; отделното заявено „11/11“ не е независимо потвърдено.
- Шестте места с `own_quarter` са покрити; `INPUT_RELS` е непроменен. Подписаният корпус **226 реда**, включително `R \ MR`, е без разлики. G8, G10 и G14 имат проверени положителни и отрицателни половини.

Тежките G7 дъмпове, пълният suite и `run_gates` не са повторени: наложеният read-only sandbox не позволява TEMP clone. Затова точният набор от 25 червени теста остава непотвърден независимо.

По време на одита външен процес придвижи HEAD **2591ab8→8cbcaf0**, променяйки само черновата на амандамент №2; стейджнатите тела останаха същите. Поправките изискват подписана делта, включително вече обявените неподписани точки. Не съм редактирал, стейджвал или комитвал; атомният комит остава действие на Петър.
