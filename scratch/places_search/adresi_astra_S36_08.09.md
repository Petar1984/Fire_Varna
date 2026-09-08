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
session id: 01a07e93-27b9-7710-aca6-8f74eba4cae3
--------
user
S36 · Външно око (леща ГИС-практика и механика): БЕЗ ЗАСТЪПВАЩИ СЕ ПОЛИГОНИ. Петър (08.09): „Центърът и Завод Дружба се застъпват — ще имаме конфликти там… не искам да имаме полигони, които се застъпват“; освен това иска обособени зони за Общината, Стадион Спартак, Лятно кино Тракия и Операта (ориентири за пожарникаря). Данни (read-only): подписаните 60 полигона (git -C C:/git/varna_3d show 05f485e:data/quarters_signed.geojson; _meta.parent_child = 11 родства + 2 в properties (Боровец-север/юг → несъществуващ „borovets“)); предложението за дупките C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/gaps_proposal_08.09.geojson (20 кандидата с code/kind/parent/verdict) и decisions_5_draft_08.09.json; разширеният Център tsentar_extended_08.09.geojson; ЧЕРНОВАТА НА РАЗДЕЛЯНЕТО partition_draft_08.09.geojson + partition_report_08.09.json: 79 полигона, правило „детето изрязва родителя; при застъпване без родство по-малкият печели и двойката се флагва“ → 0 остатъчни застъпвания, 61 спорни двойки (напр. ПЗ Планова × Владиславово 0,41 km² 61 % от по-малкия; Възраждане × Възраждане 4 72 %; Максуда × Св. Иван Рилски 39 %; Капелова градина × ЗПЗ 23 %; Център × Погребите 23 %; Център × Завод Дружба 9 %; и десетки ивици < 0,01 km²); загуби на площ: Възраждане 97,5 % (родителят става ивица), Младост 90,6 %, Морска градина 53,6 %, Левски 29,5 %, Владиславово 25,8 %. Контекст: кварталът на всяка сграда/адрес ще се извежда при билд от тези полигони (координатата решава), публично пътуват само имената; търсенето „Възраждане“ трябва да намира и Възраждане 1–4; картончето показва „вид · квартал · район“. Въпроси: (1) правилният модел: строго разделяне (partition, всяка точка в точно един полигон; децата изрязват родителите; родителят остава само като ГРУПА за търсене) срещу йерархия със застъпване, решавана при заявка — какво е професионалната практика за адресна принадлежност и за ориентири; (2) ориентирите (Опера, Община, Стадион, Лятно кино): обособени зони, изрязани от квартала (адресът на Операта става „Операта“, не „Център“) или отделен слой „ориентир“ върху квартала („Център, до Операта“) — кое е правилно за пожарникар и за адресите; (3) правилото за 61-те спорни двойки: кои може да се решат автоматично (ивици под праг — кой праг, напр. < 0,01 km² или < 5 % от по-малкия) и кои са борд; (4) границата на разширения Център (обединение на Wikimapia полигони с изрязване) — приемлива ли е или Петър трябва да я начертае по улици; как се пази провенансът (кой полигон откъде идва) при изрязване; (5) как двата потребителя (Fire_Varna адреси; 3D карта) консумират разделянето — един код на сграда + parent верига; какво се променя в плана „Адресите по полигон“ v3 (docs/plans/ПЛАН_Адресите_по_полигон_08.09.md §2/§3) и в ADR 010 D6/D8. Не пипай нищо. До 800 думи: препоръка + условия, с числа.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя черновата, плана и ADR спрямо данните и външни ГИС източници. Ще остана изцяло в read-only режим и ще отделя геометричните конфликти от решенията за адресна принадлежност.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -TotalCount 150" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status -sb' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$targets = @('"'C:\\git\\Fire_Varna\\AGENTS.md','C:\\git\\Fire_Varna\\scratch\\boundary_gallery\\granitsi_preview_05.09','C:\\git\\Fire_Varna\\docs\\plans','C:\\git\\Fire_Varna\\docs\\decisions','C:\\git\\varna_3d\\AGENTS.md'); foreach ("'$target in $targets) { if (Test-Path -LiteralPath $target -PathType Leaf) { Get-Item -LiteralPath $target | Select-Object -ExpandProperty FullName } elseif (Test-Path -LiteralPath $target) { Get-ChildItem -LiteralPath $target -File | Where-Object { $_.Name -match '"'08\\.09|010' } | Select-Object -ExpandProperty FullName } else { Write-Output ('MISSING: ' + "'$target) } }' in C:\git\Fire_Varna
 succeeded in 516ms:
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

 succeeded in 484ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 126]
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
?? scratch/places_search/adresi_astra_S36_08.09.md
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

 succeeded in 685ms:
C:\git\Fire_Varna\AGENTS.md
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\address_rows_08.09.json
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\adresi_proposal_08.09.html
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\adresi_proposal_08.09.json
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\decisions_5_draft_08.09.json
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\gaps_buildings_08.09.json
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\gaps_candidates_08.09.geojson
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\gaps_candidates_wm_details_08.09.json
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\gaps_preview_08.09.html
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\gaps_proposal_08.09.geojson
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\gaps_proposal_08.09.html
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\gaps_proposal_08.09.json
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\hotels_08.09.json
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\partition_draft_08.09.geojson
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\partition_report_08.09.json
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\places_08.09.json
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\quarters_overlay_08.09.html
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\quarters_signed_08.09.geojson
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\reclass_08.09.json
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\reclass_map_08.09.html
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\tsentar_extended_08.09.geojson
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\tsveten_candidate_08.09.geojson
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\tsveten_preview_08.09.html
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\tsveten_preview_08.09.json
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\zone_to_quarter_draft_08.09.json
C:\git\Fire_Varna\docs\plans\ПЛАН_Адресите_по_полигон_08.09.md
C:\git\Fire_Varna\docs\decisions\010_signed_quarter_boundaries.md
C:\git\varna_3d\AGENTS.md

web search: 
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -Encoding UTF8 -TotalCount 32" in C:\git\Fire_Varna
 succeeded in 522ms:
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


web search: site.postgis.net ST_Covers boundary ST_Contains geometry ...
codex
Основният риск е, че „0 застъпвания“ доказва геометрично разделяне, но не и правилно присвоени квартали. Проверявам и какво остават родителите след изрязването — особено Възраждане и Младост — и дали малките ивици могат изобщо да се приемат за технически грешки.

web search: 
web search: site.wikimapia.org terms reference purposes only accuracy data ...
codex
Има две важни уточнения от файловете: предложението съдържа 29 обекта, от които 19 кандидата; 20-те решения включват и Центъра. От 61-те спорни двойки 48 са под 0,01 km², но източниците декларират точност 50–100 m — малката площ сама по себе си не оправдава автоматично изрязване.

codex
Открихме и съществено несъответствие между входовете и черновата: няма значими остатъчни застъпвания, но липсват около 1,207 km² от обединението на подадените геометрии. Разликата е в разширения Център. Освен това ADR D8 вече допуска буфер `precision_m`; план v3 го описва като строго съдържание без буфер и трябва да се коригира.

codex
**Препоръчвам строго разделяне за адресната принадлежност, йерархия за търсенето и отделна идентичност за ориентирите. Настоящата чернова обаче не е готова за подпис.** Нищо не е променено.

Обхватът е S36. Прочетени са текущият контекст, план v3, ADR 010 и шестте входа; измерванията са в EPSG:32635. Инвентарът на входовете е:

```text
git 05f485e:data/quarters_signed.geojson 301917
decisions_5_draft_08.09.json 8665
gaps_proposal_08.09.geojson 63743
partition_draft_08.09.geojson 208247
partition_report_08.09.json 13076
tsentar_extended_08.09.geojson 5441
```

Размерите са байтове; файловете са в посочената галерия. Метаданните казват **„чернова за решения 5 — неподписано“**. Предложението всъщност има **29 обекта, 19 кандидата**; решенията са **19 кандидата + Център**. В изходните 79 обекта липсва пълна проследимост на операциите.

**Критично измерване:** черновата има 79 валидни обекта, но **150 отделни компонента**. Няма значими остатъчни застъпвания, обаче спрямо подадените входове **липсват 1,206831 km²**. Разширеният Център е **3,268 km²**, полученият — **1,889 km²**: загубата е **42,2%**, а не отчетените 2,8%. Последното съответства само на най-големия входен компонент. Вероятно останалите компоненти са отпаднали; причината не е доказана без рецептата.

1. **Моделът.** За единствена квартална принадлежност разделянето е подходящо: без обща положителна площ, със споделени граници. Йерархично застъпване е нормално между различни нива, но тук няма нужда потребителите да разрешават конфликти при заявка. Това съответства на разграничението между правилата за застъпвания и празнини в [ГИС топологията](https://pro.arcgis.com/en/pro-app/3.5/help/editing/geodatabase-topology-rules-for-polygon-features.htm).

   „Точно един“ важи **в подписан обхват**, с изрично правило за граничните точки: `covers` може да върне двама съседи. Извън обхвата — неизвестно, без измислена принадлежност. [PostGIS](https://postgis.net/docs/ST_Covers.html)

   Родителят остава група; смисленият остатък получава отделна пространствена идентичност. Загубите **97,5% за Възраждане, 90,6% за Младост, 53,6% за Морската градина** изискват преглед. Нормализирайте родствата: двете връзки към липсващия `borovets` и **липсващия parent на Възраждане 4**. Последното обяснява защо неговото 72% застъпване е третирано като неродствено.

2. **Ориентирите.** Операта, Общината, стадионът и киното трябва да имат собствени имена/обекти, **без да заменят квартала на адреса**. За самата сграда: „Операта, Център“; за съседен адрес „до Операта“ само при проверена близост. Съвременният [NENA модел](https://cdn.ymaws.com/www.nena.org/resource/resmgr/standards/nena-sta-006.3_ng9-1-1_gis_d.pdf) отделя адреси, обекти, псевдоними и административни области; това е полезна практика, не българска нормативна норма.

   Ако искаш непременно площни зони, разделете квартала на неприпокриващи се клетки с отделно `landmark`, като `quarter` остава „Център“. Така обособяването не преименува адресите. Радиусът за уличните ориентири **120 m** не се пренася автоматично.

3. **Спорните двойки.** Прагът **<10 000 m² И <5%** отделя **48 двойки** за ускорен преглед; **13** остават задължителен борд. С „ИЛИ“ минават 53, включително **Манастирски рид × Виница: 54 000 m² / 3,2%**.

   **Нито една двойка не е автоматично оправдана само от площта.** Автоматизация допускайте след установена обща граница, подписан приоритет на източниците и проверка за засегнати адреси/входове. Декларираните точности са **59 × 100 m и 1 × 50 m**; те не са допустими разстояния за автоматично прилепване. [Esri](https://pro.arcgis.com/en/pro-app/3.3/help/data/topologies/topology-in-arcgis.htm) изрично различава точността на източника от много по-малкия изчислителен толеранс. „По-малкият печели“ е механика, не доказателство за принадлежност.

4. **Центърът и произходът.** Обединението е начална хипотеза. Рецептата включва **Wikimapia 20880220**, въпреки че същият безименен триъгълник е отбелязан **„отпада“**. Петър трябва да потвърди границата по разпознаваеми улици/обекти и адресни примери; не е нужно лично да рисува всеки връх.

   Запазете оригиналите и за всеки резултат: входни кодове/хешове, добавящи и изрязващи геометрии, ред на операциите, CRS/точност, решение и нов подпис. **59 резултата още носят `src="подписан"`**, което не удостоверява изменената геометрия. Това следва принципа за проследими производни във [W3C PROV](https://www.w3.org/TR/prov-o/).

5. **Договорът за двата потребителя.** Един производител, версия и правило за представителната координата; вътрешно — краен код + parent верига, публично — нужните имена. „Възраждане“ включва 1–4; „Възраждане 1“ изключва съседните деца.

   В [план v3](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:215) §2/§3 добавете гейтове за покритие, гранични точки, засегнати адреси, родства и еднакви резултати между потребителите. В [ADR D8](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:52) отделете груповата обвивка от изрязания остатък. **D8 вече допуска `precision_m` буфер** — v3 неправилно го представя като строго съдържание.

   **D6 остава отделно решение:** за местата полигонът сега е свидетел и пази написания квартал/12 изключения. Координатното правило за адресите не отменя това автоматично. Всички предложени изменения са обратими и неподписани; отворени остават остатъчните зони, спорните граници и евентуалната промяна на D6.
tokens used
62,858
**Препоръчвам строго разделяне за адресната принадлежност, йерархия за търсенето и отделна идентичност за ориентирите. Настоящата чернова обаче не е готова за подпис.** Нищо не е променено.

Обхватът е S36. Прочетени са текущият контекст, план v3, ADR 010 и шестте входа; измерванията са в EPSG:32635. Инвентарът на входовете е:

```text
git 05f485e:data/quarters_signed.geojson 301917
decisions_5_draft_08.09.json 8665
gaps_proposal_08.09.geojson 63743
partition_draft_08.09.geojson 208247
partition_report_08.09.json 13076
tsentar_extended_08.09.geojson 5441
```

Размерите са байтове; файловете са в посочената галерия. Метаданните казват **„чернова за решения 5 — неподписано“**. Предложението всъщност има **29 обекта, 19 кандидата**; решенията са **19 кандидата + Център**. В изходните 79 обекта липсва пълна проследимост на операциите.

**Критично измерване:** черновата има 79 валидни обекта, но **150 отделни компонента**. Няма значими остатъчни застъпвания, обаче спрямо подадените входове **липсват 1,206831 km²**. Разширеният Център е **3,268 km²**, полученият — **1,889 km²**: загубата е **42,2%**, а не отчетените 2,8%. Последното съответства само на най-големия входен компонент. Вероятно останалите компоненти са отпаднали; причината не е доказана без рецептата.

1. **Моделът.** За единствена квартална принадлежност разделянето е подходящо: без обща положителна площ, със споделени граници. Йерархично застъпване е нормално между различни нива, но тук няма нужда потребителите да разрешават конфликти при заявка. Това съответства на разграничението между правилата за застъпвания и празнини в [ГИС топологията](https://pro.arcgis.com/en/pro-app/3.5/help/editing/geodatabase-topology-rules-for-polygon-features.htm).

   „Точно един“ важи **в подписан обхват**, с изрично правило за граничните точки: `covers` може да върне двама съседи. Извън обхвата — неизвестно, без измислена принадлежност. [PostGIS](https://postgis.net/docs/ST_Covers.html)

   Родителят остава група; смисленият остатък получава отделна пространствена идентичност. Загубите **97,5% за Възраждане, 90,6% за Младост, 53,6% за Морската градина** изискват преглед. Нормализирайте родствата: двете връзки към липсващия `borovets` и **липсващия parent на Възраждане 4**. Последното обяснява защо неговото 72% застъпване е третирано като неродствено.

2. **Ориентирите.** Операта, Общината, стадионът и киното трябва да имат собствени имена/обекти, **без да заменят квартала на адреса**. За самата сграда: „Операта, Център“; за съседен адрес „до Операта“ само при проверена близост. Съвременният [NENA модел](https://cdn.ymaws.com/www.nena.org/resource/resmgr/standards/nena-sta-006.3_ng9-1-1_gis_d.pdf) отделя адреси, обекти, псевдоними и административни области; това е полезна практика, не българска нормативна норма.

   Ако искаш непременно площни зони, разделете квартала на неприпокриващи се клетки с отделно `landmark`, като `quarter` остава „Център“. Така обособяването не преименува адресите. Радиусът за уличните ориентири **120 m** не се пренася автоматично.

3. **Спорните двойки.** Прагът **<10 000 m² И <5%** отделя **48 двойки** за ускорен преглед; **13** остават задължителен борд. С „ИЛИ“ минават 53, включително **Манастирски рид × Виница: 54 000 m² / 3,2%**.

   **Нито една двойка не е автоматично оправдана само от площта.** Автоматизация допускайте след установена обща граница, подписан приоритет на източниците и проверка за засегнати адреси/входове. Декларираните точности са **59 × 100 m и 1 × 50 m**; те не са допустими разстояния за автоматично прилепване. [Esri](https://pro.arcgis.com/en/pro-app/3.3/help/data/topologies/topology-in-arcgis.htm) изрично различава точността на източника от много по-малкия изчислителен толеранс. „По-малкият печели“ е механика, не доказателство за принадлежност.

4. **Центърът и произходът.** Обединението е начална хипотеза. Рецептата включва **Wikimapia 20880220**, въпреки че същият безименен триъгълник е отбелязан **„отпада“**. Петър трябва да потвърди границата по разпознаваеми улици/обекти и адресни примери; не е нужно лично да рисува всеки връх.

   Запазете оригиналите и за всеки резултат: входни кодове/хешове, добавящи и изрязващи геометрии, ред на операциите, CRS/точност, решение и нов подпис. **59 резултата още носят `src="подписан"`**, което не удостоверява изменената геометрия. Това следва принципа за проследими производни във [W3C PROV](https://www.w3.org/TR/prov-o/).

5. **Договорът за двата потребителя.** Един производител, версия и правило за представителната координата; вътрешно — краен код + parent верига, публично — нужните имена. „Възраждане“ включва 1–4; „Възраждане 1“ изключва съседните деца.

   В [план v3](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:215) §2/§3 добавете гейтове за покритие, гранични точки, засегнати адреси, родства и еднакви резултати между потребителите. В [ADR D8](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:52) отделете груповата обвивка от изрязания остатък. **D8 вече допуска `precision_m` буфер** — v3 неправилно го представя като строго съдържание.

   **D6 остава отделно решение:** за местата полигонът сега е свидетел и пази написания квартал/12 изключения. Координатното правило за адресите не отменя това автоматично. Всички предложени изменения са обратими и неподписани; отворени остават остатъчните зони, спорните граници и евентуалната промяна на D6.
