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
session id: 01a07dfc-0ff9-7983-b964-a2a6348ca9e5
--------
user
S33 · Оборване на ПЛАН „Адресите по полигон“ v2 (леща СЕМАНТИКА НА ТЪРСЕНЕТО и UX за пожарникаря), read-only. Файл: C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md (v2, f745349). Целта на Петър (дословно): „този бл 11 на студентска е в квартал левски… като напиша бл 11 левски ми изкарва няколко блока с номера 11… искам да има и най-близка улица или някакъв друг ориентир… много блокове 11 в кв левски не е добре“. Проба на предложението (визуализирана за него): scratch/boundary_gallery/granitsi_preview_05.09/adresi_proposal_08.09.json (5 274 блокови записа: old/new_v1/new_v2/свидетел/клас/ориентир). Атакувай семантиката: (1) §2 и §3 Р5 (четирите варианта на лентата; препоръка (в) „съдържанието решава“) — вярна ли е препоръката за пожарникар, който търси по квартал + блок; каква е реалната цена на грешките при ≤100 m от ръба; вариант (г) по-добър ли е; (2) Р9/Р9-б/Р10/Р11/Р11-б — ориентирът: „ул. Студентска“ vs „до ул. Студентска“, втора степен и метри, филтърът за нелегитимни низове, радиусът 120 m — измери върху data/search_index.json + data/address_rows.json колко блока остават неразличими след двете степени и дай примери; (3) Р14 гардът на свидетеля (кадастралната/OSM дума търси, но не потвърждава квартал): какво се случва с „чайка студентска бл 11“, „бл 11 левски“, „бл 11 чайка“, „студентска бл 11“ — симулирай с реалния матчер на index.html (~5130-5260) в паметта, ако можеш; подредбата (tk.length+qtk.length) не се ли чупи от новите полета; (4) Р12/Р12-б второто дисплей поле (display_id път, 43 295 реда) — наистина ли думата стига до всички редове; (5) UI низовете и картончето — какво вижда потребителят при неопределен квартал („район Приморски, бл. 11, до ул. Студентска“) — приемливо ли е за пожарникар; (6) Р7 припокриванията и Р1–Р3 дупките — препоръките пълни ли са. Нищо не пипай. Присъда: ГОДНО за подпис / НЕГОДНО с S33-1… (измерване + точна поправка); до 800 думи.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя плана срещу реалните данни и матчера, без промени по файловете. Ще разделя проверките за квартала, ориентирите и второто дисплей поле, после ще дам присъда с измервания и точни поправки.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git rev-parse --short HEAD' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status -sb' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -TotalCount 120" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p = @('"'docs/activeContext.md','AGENTS.md','docs/plans/ПЛАН_Адресите_по_полигон_08.09.md','scratch/boundary_gallery/granitsi_preview_05.09/adresi_proposal_08.09.json','data/search_index.json','data/address_rows.json','index.html'); "'$p | Sort-Object | ForEach-Object { $f = Get-Item -LiteralPath $_; '"'{0}"'`t{1}'"' -f "'$_,$f.Length }' in C:\git\Fire_Varna
 succeeded in 438ms:
f745349

 succeeded in 454ms:
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

 succeeded in 620ms:
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

 succeeded in 629ms:
AGENTS.md`t27909
data/address_rows.json`t5073137
data/search_index.json`t11242756
docs/activeContext.md`t15557
docs/plans/ПЛАН_Адресите_по_полигон_08.09.md`t97454
index.html`t566532
scratch/boundary_gallery/granitsi_preview_05.09/adresi_proposal_08.09.json`t3286362

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -Encoding UTF8 -TotalCount 60" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg --max-count 20 --max-columns 200 -n '"'^(##|###)|Р14|Р12-б|Р11-б|Р9-б'"' 'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md'" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md' -Encoding UTF8 -TotalCount 150" in C:\git\Fire_Varna
 succeeded in 418ms:
16:## 0 · Червени редове (важат за всеки ход)
33:## 1 · Мярка
35:### А. Базата (всяко число с извор)
95:### Б. М0 — задължително преизмерване преди първия ред код
115:### В. Точки на вмъкване (всички проверени лично от Planner-а сега)
125:### Г. Гейтове днес — какво покрива адресната доставка
132:## 2 · Целта и НЕ-целта
156:## 3 · Решения за Петър преди билда
191:[Omitted long matching line]
207:[Omitted long matching line]
219:[Omitted long matching line]
225:[Omitted long matching line]
234:**Р14 · Гардът на свидетеля.**
236:[Omitted long matching line]
252:## 4 · Write-set по репа
254:### 4.1 `C:/git/Varna_buildings` (Executor комитва)
271:[Omitted long matching line]
280: - **`o.wtk = написаните токени МИНУС `o.qtk`** (Р14-а); празен масив не се пише;
285:[Omitted long matching line]
305:### 4.2 `C:/git/varna_3d`

 succeeded in 617ms:
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

 succeeded in 586ms:
# ПЛАН · Адресите по полигон (v2)

**Файл:** `C:/git/Fire_Varna/scratch/places_search/ПЛАН_Адресите_по_полигон_v2_08.09.md`
**Дата:** 08.09.2026 · **Автор:** Planner (read-only, Opus) · **Статус:** ЧЕРНОВА — чака Gate 1 (подпис на Петър)
**Заменя:** v1 от 08.09 (същия ден). **Основание за v2:** три състезателни опровержения (gates / semantics / delivery), всичките с присъда **НЕГОДНО**. Всяка находка е сверена срещу файловете; приетите са вградени тук, отхвърлените са в §11, присъдите — в §12.
**Изпълнител:** Opus Executor · **Одитор:** Opus, състезателен · **Публикува:** Петър.

**Клас на риска: 🔴 АРХИТЕКТУРЕН.** Задействани спусъци: (1) нов канон за квартала в доставяни данни; (2) промяна на схемата на публичния payload (`index_schema_version`, `ALLOWED_ENTRY_KEYS`); (3) нов външен източник на имена в публична повърхност (подписаните полигони); (4) междурепова радиация `Varna_buildings → varna_3d → Fire_Varna`; (5) отмяна/уточняване на подписани прецеденти (Р38; отношението към ADR 010); **(6) НОВ — лотът е забранен от ПРИЕТ ADR 006 D12 и е разрешен само от НЕПОДПИСАН ADR 007** (`C:/git/Fire_Varna/docs/decisions/006_places_in_search.md:157-163`, `007_address_path_v2.md:3`), при това пипа изрично пиннатите „scorer and comparator“ (`007:15`); (7) доставка към публикуване, комбинирана с висящата Б3. Топология: **Вариант А**.

**Две доставки в един лот:**
- **(A) Каноничен квартал** — думата идва от подписания полигон под точката; написаният свидетел остава търсим, никога авторитетен.
- **(B) Ориентир за блоковете** — всеки блоков ред носи ориентир („кв. Левски, бл. 11, до ул. Студентска“), за да са различими едноименните блокове.

---

## 0 · Червени редове (важат за всеки ход)

1. **Агентите не публикуват.** Никакъв `git push`, никакъв remote, никакъв `--no-verify`. Агентът казва „публикуване“ и спира. `git push` **не стои** в нито един команден списък на този план (§5.Д).
2. **Нула геометрия и нула реконструкция на границата в публичен файл.** По ADR 010 D3 (`010:42`) публично излизат само `name`/`code`/`src`. **Не се изнася `dist_to_edge_m`** — нито поле, нито кофа, нито закръглено; забраната става структурна проверка в публикационния гейт (§4.1, G-A2).
3. **`config/quarter_registry.json` не се пипа** (подписът `REGISTRY_SIGNED_SHA256`, `js/lib_quarter_registry.mjs:45-46`). Всяко движение в регистъра (родителите на Възраждане 1–4, Розова долина, Кокарджа, Абатко, Салтанат, висящият `borovets`) отива в **сутрешния списък**.
4. **Данните комитва Петър** (D16/G4). Изпълнителят комитва само код, тестове, гейтове и документи.
5. **Всеки гейт е команда с изход ≠ 0 и назована отрицателна фикстура, която ТРЯБВА да падне** — и фикстурата трябва да пада по НОВОТО твърдение, не по стара проверка (§6; прецедент `checkFixture`, `js/test_fire_varna_publish_gate.mjs`).
6. **Само Opus.** Всеки `Agent`/`agent()` с `model: "opus"`.
7. **Мярка преди промяна, с произход на всяко число.** Числата в §1.А носят етикет за извор (СКАУТ / опровергател / задание). Всяко число, което влиза в подпис, гейт или фикстура, се преизмерва в М0 (§1.Б); **разминаване с базата тук = СПИРАЙ** (§7).
8. **Нула кадастрални идентификатори, нула ГРАО, нула PII** в двата адресни payload-а.
9. **Атрибуцията не се пипа от този лот.** Измерено: низът „Кварталните граници“ днес **не съществува** в `index.html` (СКАУТ 5; потвърдено косвено — той стои само като ЗАБРАНЕН литерал в `tests/test_b3_gates.py:43-44`). Този лот не добавя и не преформулира нито един атрибуционен ред; `FORBIDDEN` остава зелен (G-B6). Ако Б3 достави ред за атрибуция, обхватът му за адресните редове е решение на Петър — **отделен ред в сутрешния списък**, не тук.
10. **Б3 (местата) не се ПРОМЕНЯ от този лот**, но **се КОМИТВА пръв, от ръката на Петър** (§5.0). Двата текста на v1 (§0.10 „не се пипа“ ↔ §5.Г „влиза в HEAD пръв“) са изравнени тук.
11. **Един логически комит = един ход**, точното съобщение от §5, стейджване с явни пътища, никога `git add -A`. **`index.html` е в ДВАТА write-set-а** — преди F1 `git diff --cached -- index.html` трябва да е празен (§7 т. 14).
12. **`sw.js` не се пипа** (недосегаем и по `006:158`, и по `007:13`; освен това промяната е безполезна — `sw.js:104-106` трие само кешове с префикси `B2_CACHE_PREFIXES`, а `fire-varna-search-*` не е сред тях).

---

## 1 · Мярка

### А. Базата (всяко число с извор)

**Публичните payload-и днес** (`C:/git/Fire_Varna/data/`, СКАУТ 1 §0/§2, СКАУТ 5 §A):

| факт | стойност |
|---|---|
| `search_index.json` | 11 242 756 B · 86 232 записа · `index_schema_version "2.0"` · `address_row_count 80510` · `vocab` 2 889 · `district_names` 5 |
| по вид | address 70 575 · mf 14 687 · parcel 970 |
| полета | `label` 43 133 · `display_id` 43 295 · и двете 196 · `qtk` 19 494 · `alias_tk` 574 · `stk` 362 · `btk` 5 567 · `d` 85 935 |
| `address_rows.json` | 5 073 137 B · 80 510 реда · `field_order ["normalized_address","lat","lng"]` |
| first load | HEAD 560 855 + 1 317 355 = 1 878 210 B (кап 5 MB); адресните са lazy — 15,57 MiB на първи фокус |
| `district_names` | **проверено от Planner-а сега:** `["Аспарухово","Владислав Варненчик","Младост","Одесос","Приморски"]` (`data/search_index.json`, top-level) — `d=3` е Одесос, `d=4` е Приморски |

**Подписаните полигони** (`C:/git/varna_3d/data/quarters_signed.geojson`): **проверено от Planner-а сега — 60 имена**, сред които `ж.к. Възраждане` + `Възраждане 1..4`, `ж.к. Младост` + `Младост 1/2`, `кв. Чайка` И `к.к. Чайка`, `кв. Левски`, `кв. Виница`, `Център`, `Колхозен пазар`; **няма „Цветен квартал“, няма „Боровец“ (само север/юг)**.

**Класове спрямо полигоните** (СКАУТ 3 §1–§5): inside-undisputed 42 566 · inside-edge 26 227 · overlap-incomparable 4 174 · outside-all 13 265. Върху inside-undisputed: съвпада 4 569 · противоречи 4 399 · без дума 33 598. Класове на несъгласие (n≥5, 53 реда): `vinitsa`→Манастирски рид 1 264 / Акчелар 651 / Ален Мак 205 / Св. Никола 64 / Сотира 63 / Перчемлията 88 / Евксиноград 68; `tsveten kvartal`→кв. Левски 318, →Изгрев 9; `mikroraion`→Център 269, →Гръцката махала 154; `kolhozen pazar`→кв. Тракия 245; **`chaika`→кв. Левски 150**; `rozova dolina`→Аспарухово 177.
Дупки (outside-all, само `mf` носят дума): Център 753 · Колхозен пазар 490 · Левски 478 · Гръцката махала 410 · Чайка 219 · Цветен квартал 197 · Виница 1 461 · без дума 8 810.
Припокривания: 5 620 → **подписан parent/child 1 446 · несравними 4 174** (СКАУТ 3 §5; обръща сплита 4 202/1 418 от мярката 08.09 → М0.4).
Проверимост на днешните думи: от 19 494 с `qtk` само **8 968 (46,0 %)** стоят там, където полигон може да ги потвърди или обори.

**Лентата и конкурентите (числа на опровергателите — задължителни за преизмерване в М0.5):**

| факт | gates | semantics |
|---|---:|---:|
| в точно един полигон | 67 347 | — |
| от тях в собствената лента | 25 613 | 25 613 |
| от тях с конкурент в лентата | **11 641 (45,4 %)** | **11 625 (44,3 %)** |
| извън лентата, но с конкурент | 2 156 | — |
| извън всички, но в лентата на ТОЧНО ЕДИН | **4 042** | — |
| извън всички, в лентата на няколко / далече | 620 / 8 603 | — |

**Флагманът (двамата опровергатели съвпадат, третият го потвърждава по друг път):** записът `{"kind":"mf","pin":[43.22212,27.9378],"tk":["studentska","bl","11"],"qtk":["chaika"],"label":"кв. Чайка, бл. 11","g":"b6797e83ec13fe798"}` е **вътре в кв. Левски на 67,4 m от ръба** при `precision_m = 100`; най-близкият чужд полигон **ж.к. Бриз е на 82,8 m** — тоест конкурент В лентата. Под Р5(а) и Р5(в) на v1 този запис **остава без квартал** → v1 не решаваше жалбата на Петър (§12).
Съседни случаи: „Цветен квартал, бл. 11“ вътре в кв. Левски на 56,3 m с конкуренти Изгрев 49,5 m и Кокарджа 49,0 m; запис `pin [43.21976, 27.91949]`, днес „кв. Левски, бл. 11, бул. Царевец“, е **51,2 m ИЗВЪН** кв. Левски.

**Днешното поведение на клиента** (СКАУТ 2 §1, реален матчер): „чайка студентска бл 11“ → ред 1 = `кв. Чайка, бл. 11`, `all=true`, съвпадението през **`qtk`**; „левски студентска бл 11“ → сградата **не излиза изобщо**; „левски битоля 13“ → `all=true` за улица извън всички полигони.

**Ориентирът (B) — база с ПРОТИВОРЕЧИЯ, които М0.6 решава:**

| факт | извор | стойност |
|---|---|---|
| mf записи с „бл 11“ в града | задание (Петър) | 385 |
| mf с `btk`, съдържащ „11“ | delivery | **91** |
| mf етикети `бл\.\s*11(?!\d)` | delivery | **95** |
| етикети с улица след блоковия номер | задание | 26 |
| mf с блоков номер (`btk`) общо | gates | 5 567 |
| от тях с улична точка ≤ 120 m | gates | 4 243 |
| от тях БЕЗ улица ≤ 120 m | gates | **1 324 (23,8 %)** |
| блокови групи по `g` / без улица в 120 m | semantics | 1 353 / **213 (15,7 %)** |
| колизионни двойки (каноничен квартал, блок №) | gates 186 · semantics 550 | — |
| от тях НЕразличими по ориентир | **gates 24 · semantics 16** | — |
| разстояние: медиана / p90 / ≥100 m | gates | 36,7 m / 93,9 m / **339 от 4 243** |
| `address_line` с уличен опенер | gates 21 717/60 614 (35,8 %) · semantics 185/1 056 блокови (17,5 %) | — |
| **клъстерът на флагмана** | delivery/semantics | `cluster_5eb05fc2c606f820`, `address_line = "Студентска бл. 11"` → `extractStreet` дава **null** (няма „ул.“), а `tk` на записа НОСИ `studentska` |

**Свидетелят НЕ е „кадастралната дума“** (semantics, върху `app/modules/search/data/search_bridge.json`): от 60 604 клъстера с `quarter.name` — `source`: **osm 35 054 / kais 25 550**; `mode`: nearest_point 33 188 / polygon_cover 1 866 / null 25 550; флагманът носи `{name:"кв. Чайка", source:"osm", confidence:"low", mode:"nearest_point", distance_m: 707.5}`. Затова в целия план думата е **„написан свидетел“** с колона `source` в леджера.

**Размерът на промяната (две независими оценки, и двете >> „~+0,3 MB“ от v1):** semantics ≈ **+1,26 MB** само за каноничния `qtk` + `q`; delivery ≈ **+1,54 MB** (q 0,308 + wtk 0,420 + нето qtk 0,812). Реалната стойност зависи от правилото за `wtk` (§4.1 т. 2) → М0.10.

**Двата дисплей пътя:** 42 937 само `label` · 43 099 само `display_id` · 196 и двете. **205 mf записа носят `btk` и НЯМАТ `label`** (gates и delivery съвпадат); общо 581 записа без `label` носят „бл“ в текста си от `address_rows` (delivery). За display_id пътя: **2 775 записа без `label`** биха се изписали „<каноничен квартал>, <ПРОТИВОРЕЧАЩА написана дума>“, а **11 627** с неопределен канон запазват квартална дума в свободния текст (semantics).

### Б. М0 — задължително преизмерване преди първия ред код

Изпълнителят пуска и записва в `C:/git/Varna_buildings/output/addr_quarter_M0.json` (частно, `output/*` е gitignored). **Нула shell-пренасочвания и нула пайпове за байтове** (PowerShell 5.1 превръща `>` в UTF-16LE; delivery измери 603 838 B вместо 301 917 B и трети sha при пайп).

| № | какво | как | защо |
|---|---|---|---|
| М0.1 | **OID на полигоните** | `git -C C:/git/varna_3d rev-parse 05f485e:data/quarters_signed.geojson` | пинът е СЪДЪРЖАНИЕ, не комит; двамата опровергатели измериха един и същ блоб `82706fb5fef494175f912db82a871a6c38b4e472`, 301 917 B, sha256 `c1551d24…871b3` за 05f485e И 6486b48 → „противоречието“ на v1 отпада (§11.1) |
| М0.2 | байтовете + sha256 | Python: `subprocess.run(["git","-C","C:/git/varna_3d","cat-file","blob",OID],capture_output=True).stdout` → sha256 върху буфера → `open(...,"wb")` | константата `SIGNED_QUARTERS_OID/SHA256` не бива да пинова артефакт на обвивката |
| М0.3 | квартални маркери в `address_rows` | явен списък дефиниции | не е противоречие, а 4 дефиниции: буквално „кв./ж.к.“ **0**; водещ гол маркер **4 965**; „местност“ някъде **4 139**; подписано име като дума **23 888** (semantics) |
| М0.4 | сплит на припокриванията | скрипт по метода на СКАУТ 3 | 1 446/4 174 срещу 4 202/1 418 |
| М0.5 | **лентата: пълната таблица** | нов скрипт: за всеки пин — съдържащи полигони, `d_edge` до собствения ръб, най-близък чужд ръб | дава числата за Р5 (а)/(б)/(в)/(г) и за Р5-д; днешните оценки: 25 613 в лентата, 11 641/11 625 с конкурент, 2 156 извън лентата с конкурент, 4 042 извън-но-в-лентата |
| М0.5-б | **флагманите поименно** | същият скрипт, за пиновете `[43.22212,27.9378]`, `[43.21976,27.91949]`, „Цветен квартал бл. 11“, 3 записа на ул. Битоля | тези числа влизат ДОСЛОВНО в Р4/Р5 и в фикстурата на G-A3-г |
| М0.6 | **ориентирът** | за всички mf с `btk`: собствена улица (двете дефиниции на Р10), най-близка улична точка ≤ R, разстояние, отхвърлени низове, колизионни двойки и НЕразличими групи | сверява 385↔91↔95, 24↔16, 1 324↔213; **разминаване = СПИРАЙ** |
| М0.7 | блокови колизии ПРЕДИ | `npm run build:fire-varna:staging`, запис на `blockGroups/collisionPairs/collisionGroups/disambiguated/collisionNoStreet` (`build_fire_varna_search_index.mjs:1113-1116`) + `c2ResByReason` | смяната на квартала и махането на уличния суфикс пренареждат ключа `(quarter, block#)` |
| М0.8 | S9 базата | същият билд, `tokenInconsistentTotal` срещу `S9_BASELINE = 5828` (`:452-454`, `:1042-1051`) | дрифт гейтът ще реагира |
| М0.9 | червената база на Fire_Varna | `python -m gates.run_gates` · `python -m unittest discover -s tests` | днес: exit 1 (✗4, ✗6) и 24/342 паднали (СКАУТ 4) — адресният лот декларира СВОЙ назован интервал по G20 |
| М0.10 | **размерът** | пробен билд с новите полета → байтове на двата payload-а | Р12-в подписва таван; днес 15,57 MiB lazy |
| М0.11 | **състоянието на индекса** | `git -C C:/git/Fire_Varna status --porcelain` + `git diff --cached --stat -- index.html` | delivery измери `M  index.html` СТЕЙДЖНАТ (106+/24−) — F1 не тръгва, докато Б3 не е комитнат |
| М0.12 | районът на флагманите | `d` на записите с `bitolia`, `studentska bl 11` | v1 писа „район Одесос“; semantics измери 42/42 = **Приморски** (`d=4`), а `district_names` е проверен от Planner-а |

### В. Точки на вмъкване (всички проверени лично от Planner-а сега)

**`C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs`:** `:452-454` S9 база · **`:457-458` `TYPEWORDS` (няма „do“)** · `:459-471` `canon` · `:481-487` `entryTokenSet(e)` — чете **геокодерния** запис, не публичния `o` · `:502-509` `s9Inconsistency` (правило (1): всички улични токени липсват → inconsistent) · **`:609-619` `resolveC2BlockLabel` — fail-closed, `reason:"token_inconsistent"`** · `:698` `o = {kind,pin}` · **`:701` `qtk` — единственото място, където кварталните токени влизат в индекса** · `:722-724` dtk/stk/btk · `:731` `evaluateRow` · **`:743-754` C2** · `:757-779` S9 · `:806` `display_id` само при липсващ label · `:826-842` F3 (не прилага повторно токеновия гард) · `:847-850` tidy · **`:857-871` регистърът** · **`:873-922` Р38** · `:923` push.

**`js/lib_fire_varna_block_labels.mjs`:** `:39` `STREET_TYPE_RE = /^(ул|бул|бл\.вход|пл)\.?$/i` · `:106-126` `extractStreet` (без типов опенер → `null`) · `:155` `buildBlockLabelIndex` · `:168` `cleanQuarterDisplay(info.quarter)` · `:170` `extractStreet(info.addrLine)` · `:183` база `` `${quarter}, бл. ${rec.n}` `` · **`:191-199` Pass C — улица САМО при колизия, лепи се като `${base}, ${street}` (без „до“)** · `:203-215` stats.

**`js/test_fire_varna_publish_gate.mjs`:** `:40-47` входовете (полигони НЕ се четат) · **`:56-59` `ALLOWED_ENTRY_KEYS` (13 ключа, затворен набор — всеки непознат ключ вече е нарушение)** · `:62-68` `PRIVATE_KEYS` · `:71` каднум · `:78-80` регион · `:101-104` `FORBIDDEN_SUBSTRINGS` · `:108` bbox · `:110` `TOKEN_FIELDS` · `:128-147` топ-ниво (НЕ е затворено множество).

**`C:/git/Fire_Varna/index.html`:** `4881-4892` `baseAddressLabel` (label → `addressRows[display_id].normalized_address` → район) · `4893-4897` `formatAddressHit` · `5088-5100` `dedupeDisplayRows` · **`5134` резервен vocab · `5140-5145` postings · `5151` `_areaVocab = dtk∪qtk∪stk`** · `5164-5171` `qBlk`/`areaPresent`/`blockTyped` · `5197-5221` `scoreEntry`: tk `:5204` → alias `:5205` → **`matchedCore += 1` `:5206`** → **qtk `:5207`** → dtk `:5208` → stk `:5209` · **`:5216-5219` `dem`/`ddem`/`odem`/`sdem` — всичките с условие `matchedCore === 0`** · `5230-5256` компаратор, **`5252-5253` `tk.length + qtk.length`** · `5265` `trueTie` · **`5278-5288` груповият блоков клон** · `5291-5299` bare-block · `5303`/`5313` двете проекции · `5327` `SEARCH_CACHE` · **`5351-5372` `ensureSearchData` — тук е единственият слой, който може да е fail-closed** · `5411-5423` `buildExactItem` (`5417` заглавие, `5420` „район X“) · `5430` `'Няма съвпадения'` · `5926` approx = false.

### Г. Гейтове днес — какво покрива адресната доставка

Нула от седемте на `run_gates`: `SHA_PINS` (`gates/run_gates.py:68-72`) и `PUBLIC_BLOBS` (`:82-87`) са затворени около hotels/places/categories/signed_facts; **`check_no_cad_ids` чете РАБОТНОТО ДЪРВО и мълчаливо пропуска липсващ файл** (`:188-191`); `coverage.py:75` = `("places","hotels")`. Пипат адресите само `tests/test_data_ascii_mojibake.py:35-36` и `tests/test_basemap_manifest.py:164-165`. `data/generation_manifest.json` не се чете от никого. `recall_sweep.py:73-76` работи само върху hotels/places/categories → **замразеният корпус не покрива адреси и няма адресна `--freeze` команда** (`:90`). Единственият истински пазач е публикационният гейт в `Varna_buildings`.
`gates/probe/b3_g11.py` (стейджнат): инвентар + съдържание от ЕДНА снимка (`:91-93`, `:55-62`), но **`ALLOWED_NEW` е затворена седморка (`:40-46`) и `stray_new` дава exit 1 (`:116-119`)**; при `HEAD --cached` след комита дифът е празен и това рамо е инертно.

---

## 2 · Целта и НЕ-целта

**Вярно = координатата решава квартала; името е свидетел.**

| Класификация на пина | Каноничен квартал | Написан свидетел | Дисплей |
|---|---|---|---|
| в точно един полигон, **извън лентата** | името на полигона | `wtk` (търсим, демотиран) | „кв. Левски, …“ |
| в точно един полигон, **в лентата** | по Р5 (а/б/в/г) | същото | по Р5 |
| подписан parent/child + геометрично доказан | **само детето** | същото | детето |
| parent обявен, но недоказан геометрично | няма | същото | само „район X“ + леджер |
| несравнимо припокриване | няма | същото | само „район X“ |
| извън всички (вкл. „в лентата на един“, Р5-д) | по Р5-д | същото, **без гард** | по Р5-д |

**Целта:**
1. Публичната квартална дума за еднозначните редове е името от подписания полигон, на **двата** дисплей пътя (label и display_id).
2. Написаният свидетел остава **търсим** (правилото на Р38 „добавя, никога не реже“, комит `bfb5f86`), но **не удовлетворява изричен квартален филтър, когато записът има канон, който му противоречи**.
3. Всеки блоков ред носи **ориентир**, доставен **структурно** (стига и до двата дисплей пътя, без да пипа `address_rows.json` и без да минава през токеновия гард на C2).
4. Неопределеното се показва като неопределено — доколкото текстът позволява (§3 Р12: 2 775 реда днес биха си противоречили сами).
5. Дупките, ръбовете и споровете отиват в **частен леджер** и в борда, не в данните.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$t=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md' -Encoding UTF8; "'$t[150..299]' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$t=Get-Content -LiteralPath '"'index.html' -Encoding UTF8; "'$t[5119..5268]' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git diff --numstat HEAD -- index.html data/search_index.json data/address_rows.json 'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md'" in C:\git\Fire_Varna
 succeeded in 568ms:

**НЕ-целта (изрично забранено):** най-близък полигон / буфер / разширяване на полигон; промяна на координата, номер, вход или идентичност; геометрия или разстояние до ръб в публичен файл; движение в регистъра; палене на approx (`index.html:5926`); преименуване на `.asr-item`; промяна на низа `'Няма съвпадения'` (`:5430`); промяна на СЪДЪРЖАНИЕТО на `data/address_rows.json` (ADR 007 D2); промяна на `sw.js`.

---

## 3 · Решения за Петър преди билда

> Всяко решение = един ред за подпис. Без подпис по Р0–Р18 билдът не тръгва.

**Р0 · Управленското разрешение (НОВО, блокиращо).** ADR 006 D12 (**Accepted**) изброява поименно `data/search_index.json`, `data/address_rows.json`, `sw.js` и **„every function of `initAddressSearch`“** като недосегаеми, а гейтът му е „адресният корпус е байт-идентичен“ (`006:157-163`). ADR 007, който вдига това, е **Proposed — awaiting Petar** (`007:3`) и при това пинова изрично **„the scorer and comparator“** (`007:15`) — точно каквото този лот пипа.
*Препоръка:* **подпиши ADR 007 И подпиши разширението му** (нов ADR 064, §4.1), което: (а) вдига 006 D12 за изброения адресен write-set; (б) **разпинова `scoreEntry` и компаратора** за назованите редове; (в) обявява, че G3 престава да е байтова равнопоставеност и се заменя с диференциален address replay; (г) **не** вдига `sw.js` и **не** вдига съдържанието на `address_rows.json`.

**Р0-б · Kill switch `ADDRESS_PATH_V2`.** ADR 007 D4 иска селектор на всеки use site, никога ранен `return`.
*Препоръка:* **да** — селектор около четирите нови места в клиента (`quarterPrefix`, `orientationSuffix`, гарда на свидетеля, `otk` клона). Цена: ~20 реда и двойна фикстура в replay-а (флаг вкл./изкл.).

**Р1 · Дупката „Център“** (753 mf извън всички + част от 8 810-те без дума).
*Препоръка:* неопределено; „район Одесос/Приморски“ по измерения `d`; свидетелят остава търсим; ред в борда „Център иска подписан полигон“. **Не разширяваме полигон.**

**Р2 · „Цветен квартал“** (няма полигон, няма запис в регистъра; 197 извън + 318 несъгласия към кв. Левски + 9 към Изгрев).
*Препоръка:* координатата решава — 318-те стават „кв. Левски“ (при Р5 (в)/(г); при (а)/(б) част от тях падат в лентата и остават неопределени — числото идва от М0.5); „цветен квартал“ остава свидетел; 197-те извън — по Р5-д.

**Р3 · „Колхозен пазар“** (490 извън + 245 несъгласия към кв. Тракия).
*Препоръка:* същото правило като Р2.

**Р4 · Флагманът Левски–Чайка при Студентска.** Измерено: пинът е ВЪТРЕ в кв. Левски на 67,4 m при `precision_m = 100`, конкурентът Бриз е на 82,8 m.
*Препоръка:* **„кв. Левски“ канон, „Чайка“ свидетел** — изпълнимо САМО при Р5 (в) или (г). При (а) и (б) този запис остава без квартал и **лотът не решава жалбата ти** — това е записано тук, на първа страница, не на осма.

**Р5 · Лентата — четири варианта с измерените цени** (числата се финализират от М0.5; днешните оценки в скоби):

| вариант | правило | губят име | флагманът |
|---|---|---:|---|
| (а) строга | всичко в собствената лента → неопределено | ~25 613 | ✗ |
| (б) конкурентна (v1 Р5в) | неопределено само при конкурент в лентата | ~11 6xx | ✗ |
| **(в) съдържанието решава (препоръка)** | пинът е в точно един полигон → името се дава; лентата се записва само в леджера | 0 | ✓ |
| (г) по-близкият конкурент | неопределено само ако чужд ръб е ПО-БЛИЗО от собствения | подмножество на (б) | ✓ (Бриз 82,8 > 67,4) |

*Довод за (в):* неопределеността не може да стане чуждо име; чужд полигон, който НЕ съдържа точката, не може да я спечели. *Честната цена:* при (в) грешка е възможна за записите на ≤ band от ръба (~25 613) — тя се лови от леджера и от извадката на Петър, не от гейт. Ако искаш нула такъв риск → (а), но тогава подпиши изрично, че флагманът остава без квартал.
**Прагът „15 %“ от v1 отпада** — той не е решение, а тавтология (§12).

**Р5-д · Класът „извън всички, но в лентата на ТОЧНО ЕДИН полигон“ (~4 042; пример: „кв. Левски, бл. 11, бул. Царевец“ на 51,2 m извън).**
*Препоръка:* **остава неопределен (без канон), НО свидетелят му НЕ се гаси** (виж Р14-б) — така „бл 11 левски“ продължава да го връща, само че под редовете с канон, с назована причина в леджера. Алтернативи за подпис: (i) получава името; (ii) пълно мълчание (не се препоръчва — истински Левски бл. 11 изчезва от собствената заявка на Петър).

**Р6 · Р38 (зоната „Виница“) срещу подписаните полигони.** Зоната хваща 9 771 реда (8 996 „без свидетелство“), а Манастирски рид (1 264), Акчелар (651), Ален Мак (205), Св. Никола (64), Бриз, Перчемлията, Евксиноград, Сотира имат СВОИ полигони.
*Препоръка:* подписаният полигон има предимство; Р38 работи само там, където резолверът връща неопределено; правилото „добавя, никога не реже“ се запазва, но добавеният токен отива в свидетелското поле. Отменя част от подписан на 12.08 прецедент → иска изричен нов подпис.

**Р6-б · Отношението към ADR 010 (D6/D7/D8).** ADR 010 D6 (`010:48`) урежда канала `SIGNED_POLYGON` в `varna_3d/src/fire_varna_locations.py` за **375-те МЕСТА** („пише само в ред без свидетел, извън ръба, в точно един полигон“); този лот е ДРУГА повърхност (адресният индекс, генериран в `Varna_buildings`) — затова тук няма автоматична отмяна (§11.2). Но политиките се разминават в три точки и това трябва да е ПОДПИСАНО, не мълчаливо: (1) тук полигонът пише и в ред с написан свидетел (~4 399 замени); (2) при Р5(в) пише и в лентата (~25 613); (3) D8 иска геометрично доказано `дете ⊆ родител` — приемаме го дословно (недоказаният parent → неопределено + червен ред в леджера).
*Препоръка:* ADR 064 изброява трите разминавания и казва „ADR 010 остава непроменен за местата“.

**Р7 · Несравними припокривания (4 174; топ: Аспарухово+Розова долина 746, Гръцката махала+Център 621, Възраждане+Възраждане 1 545 …).**
*Препоръка:* неопределено + леджер. Липсващите йерархии (1 179 + 746 + 525 + 296 + 239 записа) са ход в регистъра → **сутрешен списък**. Признатата цена: ~2 985 записа остават неопределени само заради липсващ `parent`.

**Р8 · Approx пакетът** (8 361, `index.html:5926 = false`). *Препоръка:* остава изключен; при палене минава през същия резолвер.

**Р9 · Ориентир: винаги или само при колизия?** Днес улица се лепи само при сблъсък в СЪЩИЯ написан квартал (`lib_fire_varna_block_labels.mjs:191-199`); само 26 етикета носят улица.
*Препоръка:* **винаги за блокови редове** („много блокове 11 в кв левски не е добре“). Колизионният детектор остава само за да маркира `must_disambiguate` и да храни G-A6б.

**Р9-б · Какво става, когато ориентирите СЪВПАДАТ** (измерено: 24 (gates) / 16 (semantics) неразличими групи; примери: ж.к. Бриз бл. В — 13 групи, „ул. Д-р Петър Скорчев“ 4 пъти; кв. Трошево бл. 5 — две групи „ул. Радост“; кв. Чайка бл. 37 — две групи БЕЗ улица).
*Препоръка:* втора степен на ориентира — **втората по близост различаваща улица**; ако и тя не различава — **разстоянието в метри** („до ул. Радост, 40 m“ / „…, 90 m“); остатъкът след двете степени е **подписан списък изключения** от М0.6, срещу който G-A6б сверява (гейт срещу измерен остатък, не срещу нула).

**Р9-в · Един източник на уличния текст.** С Р9 ориентирът става структурен → Pass C (`:191-199`) **спира** да лепи улица в `label` (иначе „бл. 11, ул. Мир, до ул. Мир“). Цена: ~26 етикета губят суфикса си, който се връща като структурен ориентир; диффът се мери (G-A10). *Алтернатива:* Pass C остава и структурният ориентир се пропуска там — по-малък диф, две правила.

**Р10 · Какво е „собствена улица“ и как се изписва.** Днешният `extractStreet` иска типов опенер (`:39`) → за „Студентска бл. 11“ връща **null** (17,5 % от блоковите `address_line` дават улица), но `tk` на записа НОСИ `studentska`.
*Препоръка (Р10-а):* собствена улица = `extractStreet(addrLine)` **ИЛИ** улично име от речника (1 625 имена), чиито токени са в `tk` на записа. Изписване: собствена → „, ул. Х“; чужда (най-близка) → „, **до** ул. Х“.
*Следствие за подписа:* при Р10-а флагманът се изписва **„кв. Левски, бл. 11, ул. Студентска“** (собствена улица), не „до ул. Студентска“. Ако предпочиташ „до“ — тогава Р10-б: собствена улица САМО по `extractStreet`, и флагманът минава по клона „най-близка“ (52 m). **Един низ, не два** — Р13 се подравнява по избора тук.

**Р11 · Радиус за „най-близка улица“.** Измерено: медиана 36,7 m, p90 93,9 m; 4 243 от 5 567 имат улица ≤ 120 m.
*Препоръка:* **120 m**, детерминистично разкъсване на равенства (по-малко разстояние → по-малък `skel` низ → по-малък `_ord`).

**Р11-б · Качество на ориентира.** 339 от 4 243 са на ≥ 100 m; парсването ражда низове като „ул кк зл пясъци х л вихрен“, „ул жк изгрев“, „ул д р индржишка кръстева“.
*Препоръка:* (1) ≤ 60 m → „до ул. Х“; 60–120 m → „до ул. Х, ~N m“; > 120 m → без ориентир, причина `no_street_within_radius`; (2) **филтър за нелегитимни низове** (токени `жк/кк/зпз/х л`, числови опашки, повече от 4 инициала) → причина `street_string_rejected`; (3) затворен списък допустими причини: `own_street`, `nearest_street`, `no_street_within_radius`, `street_string_rejected`, `no_block_number`.

**Р12 · Къде живее кварталната дума в дисплея.**
- (а) вътре в `label` — тогава display_id пътят (43 099 реда) остава без квартал завинаги;
- **(б) препоръка — структурно поле `q` + топ-ключ `quarter_names[]`** по образеца на `d`/`district_names`; кварталният сегмент напуска `label`; клиентът композира заглавието.
- **Р12-б (НОВО, задължително допълнение):** при (б) заглавието по display_id пътя е `префикс + ', ' + normalized_address`, а самият текст носи квартална дума → **2 775 записа биха се изписали „ж.к. Бриз, акчелар“**. Варианти: (i) **материализира се `label` само за тези 2 775** (байтовете се мерят в М0.10) — препоръка; (ii) амандамент на ADR 007 D2 и нормализация в `build_fire_varna_address_rows.mjs:98` — по-скъпо управленски; (iii) приема се и се обявява. Отделно 11 627 реда с НЕОПРЕДЕЛЕН канон запазват квартална дума в текста си → §2 цел 4 важи с това ограничение, освен ако не изберем (i) и за тях (цената пак е в М0.10).
- **Р12-в · Подписан таван за размера.** Оценките: +1,26 MB (semantics) / +1,54 MB (delivery) само за квартала, преди ориентира и материализацията. *Препоръка:* подписваш число `N` байта за СБОРА на двата lazy payload-а (днес 15,57 MiB); гейт G-B3 го чете от `expectations.json`; надвишаване = СПИРАЙ.

**Р13 · Точните низове (за дословен подпис, след избора по Р10 и М0.12):**
1. заглавие с квартал и собствена улица: `кв. Левски, бл. 11, ул. Студентска` *(при Р10-а)* **или** `кв. Левски, бл. 11, до ул. Студентска` *(при Р10-б)*;
2. заглавие без квартал: `бл. 11, до ул. Студентска` + втори ред `район Приморски`;
3. адресен ред извън всички полигони: `ул. Битоля 13` + `район Приморски` (**не Одесос** — v1 сгреши; `d=4` = Приморски, `district_names` проверен);
4. префиксът се взима **дословно** от `name` на полигона, с типовата представка, без превод.

**Р14 · Гардът на свидетеля.**
*Препоръка:* (а) `wtk` = написаните токени **МИНУС** каноничните на същия запис (иначе инвариантът `wtk ∩ qtk = ∅` пада на първия билд — ~4 588 записа имат съгласна дума); (б) речникът за „изричен квартален филтър“ се строи от **`quarter_names` (всичките 60 канонични имена)**, не от наблюдаваните `qtk` — иначе кварталите, които не са раздали нито едно име, нямат гард и „ж.к. Дружба, бл. 11“ остава пълно съвпадение през свидетеля.
**Р14-б · Обхват на гарда:** гардът гаси свидетеля САМО за записи с **`q != null`** (има канон, който му противоречи). Записите с неопределен канон (в т.ч. Р5-д) запазват силата на свидетеля, но с демотиране `wdem`. Така „чайка студентска бл 11“ не е пълно съвпадение, а „бл 11 левски“ все пак връща блока на бул. Царевец.

**Р15 · Ориентирът е СТРУКТУРЕН, не в `label` и не в `stk`.**
*Довод 1:* `resolveC2BlockLabel` (`:609-619`) е fail-closed по `s9Inconsistency`, а „до“ **не е в `TYPEWORDS` (`:457-458`)** → етикет „бл. 11, до ул. Мир“ с чужда улица дава `streetMissing === streetTotal` → `token_inconsistent` → етикетът се ИЗХВЪРЛЯ. *Довод 2:* `entryTokenSet` (`:481-487`) чете геокодерния `e`, а `o.stk` се пише на `:723` върху публичния обект — спасяването „през stk“ на v1 не работи без мутиране на `e`. *Довод 3:* `_areaVocab` (`:5151`) се храни от `stk` → ~306 нови улични имена биха превключили цяло семейство заявки в груповия блоков клон (`:5278-5288`).
*Препоръка:* ново поле `o` (индекс в топ-ключ `orientations[]`) + нови токени в **`otk`** (в postings и vocab, **НЕ в `_areaVocab`**), с демотер `otdem = 1`, ако поне един токен на заявката е съвпаднал **само** през `otk` (per-token, не `matchedCore === 0` — иначе демотерът е мъртъв, както е `sdem` при блокови заявки). Така: (1) `label` не се пипа → C2/S9 остават непокътнати; (2) ориентирът стига и до двата дисплей пътя (включително 205-те блокови реда без `label`); (3) „студентска бл 11“ не сменя клона на рендера.

**Р16 · Каноничните токени.** Правилото „skel(name без представка), разделено на думи“ дава голи цифри `1`,`2`,`3`,`4` (Младост 1/2, Възраждане 1–4 — проверено в имената) и къси `sv`, `rid`, `mak`.
*Препоръка:* числов или ≤ 2-знаков суфикс НЕ влиза самостоятелно в `qtk` (само биграмата „mladost 1“); токени с дължина ≤ 2 и чисти числа се изхвърлят. Делтата в подредбата (`:5252-5253`) се мери.

**Р17 · Как двете доставки стават ЕДНА публикация.** *Препоръка:* Б3 се комитва ПРЪВ, от твоята ръка (данните са твои), после върви адресният лот; подпис и замразяване **само когато и двете са в HEAD** (проверка 1 чете работното дърво, проверка 6 — блоба на HEAD).

**Р18 · G-B1 и `ALLOWED_NEW`.** Адресният лот добавя ≥ 4 нови проследени файла; `gates/probe/b3_g11.py:40-46` е затворена седморка и е част от стейджнатия Б3.
*Препоръка:* лотът получава **свой** пробен файл `gates/probe/addr_g11.py` (копие на механиката със свой `ALLOWED_NEW`), за да не пипаме Б3-евия артефакт. Алтернатива: разширяваш `ALLOWED_NEW` с четирите пътя — тогава §0.10 се амандира за този един ред.

---

## 4 · Write-set по репа

### 4.1 `C:/git/Varna_buildings` (Executor комитва)

**НОВ · `tools/build_signed_quarter_index.py`** — Python пре-стъпка (прецедент `tools/build_quarname_enclosures.py`).
- Вход: блобът на полигоните, прочетен **в Python** (`git cat-file blob <OID>`, никакви пренасочвания) + `config/quarter_registry.json` само за четене.
- Проверява `OID` и sha256 срещу пиновете от М0.1/М0.2 → несъответствие = throw, нищо не се пише.
- EPSG:4326 → 32635; за всеки полигон: външен пръстен, `band_m = max(50, precision_m)`, bbox; **изчислява и таблица „кой полигон е конкурент на кого“ само за ЛЕДЖЕРА** (никога за публичния изход).
- Изход: `output/signed_quarters_baked.json` (частен) + `output/signed_quarters_baked_schema.json` (tracked по изключението `!output/*_schema.json`).
- Забрана: нищо извън `output/` (образец `_assert_private_out`, `tools/build_number_pins.py:883-896`).

**НОВ · `js/lib_signed_quarters.mjs`** — резолверът (НЕ в `lib_quarter_registry.mjs` — Д10, `js/test_quarter_registry.mjs:189-200`).
- `loadSignedQuarters(path)` — сверява `source_oid`/`source_sha256` с пинатите константи, проверява 60 полигона и `band_policy`, иначе throw с инструкция (образец `loadVinitsaZone`, `:158-186`).
- `resolveQuarter(model, pin)` → `{code, display, tokens, verdict, band_m, d_edge_own, nearest_other}`; `verdict ∈ inside_clear | inside_band | overlap_child | overlap_unproven | overlap_incomparable | outside_near_one | outside`.
- Правилата по подписания Р5/Р5-д; **`d_edge_own` и `nearest_other` се връщат САМО за леджера и никога не влизат в `o`.**
- `overlap_child` изисква геометрично доказано `дете ⊆ родител` в буфера (ADR 010 D8); недоказан parent → `overlap_unproven`.
- **Никакъв fallback по най-близък полигон — забранено на ниво код и на ниво тест.**
- `tokens` по Р16.

**НОВ · `js/lib_block_orientation.mjs`** — ориентирът (B): собствена улица по Р10, най-близка ≤ R по Р11 с филтъра на Р11-б, втора степен и разстояние по Р9-б, затворен списък причини.

**НОВ · `js/test_signed_quarter_resolver.mjs`** (G-A3) · **НОВ · `js/test_block_orientation.mjs`** (G-A6) · **НОВ · `js/test_quarter_ledger.mjs`** (G-A5) · **НОВ · `js/test_fire_varna_determinism.mjs`** (G-A8).

**ПРОМЯНА · `js/build_fire_varna_search_index.mjs`**
1. `main()`: зарежда `SIGNED_QUARTERS` + `ORIENTATION_MODEL` до `loadVinitsaZone`.
2. Pass 2, **`:701`**: `o.qtk` вече не се преписва от геокодера. Ново:
 - `const sq = resolveQuarter(SIGNED_QUARTERS, o.pin);`
 - `o.qtk = sq.tokens` и `o.q = quarterNameIndex(sq.display)` **само** при присъда с канон;
 - **`o.wtk = написаните токени МИНУС `o.qtk`** (Р14-а); празен масив не се пише;
 - `o.otk` = токените на ориентира (собствена улица НЕ дублира `tk`; чуждата влиза само тук), `o.o` = индекс в `orientations[]`.
3. **`:743` C2 и `:826-842` F3 не се пипат**; `label` вече не носи квартален сегмент (т. 5) и не носи улица (Р9-в) → рискът `token_inconsistent` не расте; броячът `c2ResByReason` се сравнява преди/след (G-A9).
4. **`:873-922` Р38** се обвива в `if (!sq.hasCanon)`; добавеният токен отива в `wtk`.
5. `stripQuarterSegment(label)` — само първият сегмент, само при `looksLikeQuarterSegment` (образец `lib_quarter_registry.mjs:220-229`); прилага се СЛЕД регистъра (`:857-871`), преди push.
6. **Материализация на `label`** за подписаното подмножество по Р12-б (2 775 + евентуално 11 627) — само там, само с изчистения текст, с ледгер ред за всеки.
7. Нови топ-ключове `quarter_names` (≤ 60) и `orientations` (сортиран, дедупликиран); `index_schema_version` `"2.0"` → **`"3.0"`**.
8. `vocab` (`:956-965`) се разширява с `wtk` и `otk`.
9. Нов частен изход `output/quarter_polygon_ledger.json`: старо име + **`source` (kais/osm) + `mode` + `confidence` + `distance_m` на написания свидетел**, ново име, присъда, `d_edge_own`, `nearest_other`, ориентир + причина, `complex_id`.
10. Отчетът (`:1071-1159`) получава броячи по присъда, по клас на несъгласие, по причина за ориентира, `blockGroups/collisionPairs/disambiguated` и `c2ResByReason` **преди и след**.
11. Забрана: `d_edge_own`, `nearest_other`, `competitors` не влизат в `o` при никакви обстоятелства.

**ПРОМЯНА · `js/lib_fire_varna_block_labels.mjs`** — Pass A `:168` остава свидетел; Pass B `:183` базата става `бл. ${rec.n}`; **Pass C `:191-199` спира да лепи улица** (Р9-в), само маркира `must_disambiguate`; нови stats `orientationOwn/Nearest/None/Rejected/collisionUnresolved`.

**ПРОМЯНА · `js/test_fire_varna_publish_gate.mjs`**
- `ALLOWED_ENTRY_KEYS` (`:56-59`) += `"q"`, `"wtk"`, `"otk"`, `"o"`; `TOKEN_FIELDS` (`:110`) += `"wtk"`, `"otk"`.
- **Затворен набор ТОП-ключове** (днес топ-нивото е отворено, `:128-147`) + забранени имена `dist_edge_m`, `edge_m`, `poly`, `ring`, `geometry`, `coordinates`, `geometries` навсякъде в документа.
- `quarter_names` / `orientations`: масиви от низове, без mojibake/каднум/цифрова серия ≥ 5; `q` и `o` — цели числа в обхват; **всеки `qtk` токен ∈ речника от `quarter_names`**; `wtk ∩ qtk = ∅`.
- **НОВ вход: `output/signed_quarters_baked.json`** — гейтът сам преизчислява присъдата за **всеки** запис с `q` и пада при разминаване (това е G-A4; без този вход фикстурата „`qtk:["chaika"]` при пин в Левски“ е зелена, защото „chaika“ Е валидно канонично име).
- Отровени фикстури, всяка задължително падаща: (ф1) `coordinates` в НОВ топ-ключ; (ф2) `q` извън обхвата; (ф3) `qtk` с неканоничен токен; (ф4) `wtk ∩ qtk ≠ ∅`; (ф5) `quarter_names` с не-низ; (ф6) **запис с `q` = Чайка при пин вътре в кв. Левски**; (ф7) `o` без съответен ред в `orientations`.


 succeeded in 493ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
106	24	index.html

 succeeded in 749ms:
    // section_cadnum determinism tie-breaks -> a stable runtime `_ord`; the inverted
    // index + area-vocab are rebuilt CLIENT-SIDE (payload omits inverted); dropped
    // fields (life_safety_rank / physical_building_id / quarter_assignment_trust /
    // odem) are absent, leaving their comparator/dedup slots inert (null-safe).
    // Result rows carry ONLY safe fields + label/display_id for resolution.
    const SEARCH_LIMIT = 8;

    // Build vocab (if absent), the inverted index, the area-vocab, and stamp a stable
    // `_ord` on every entry. Called ONCE after the payload loads.
    function prepareIndex(index){
      if (!index || !Array.isArray(index.entries)) return index;
      for (let i = 0; i < index.entries.length; i++) index.entries[i]._ord = i;
      if (!Array.isArray(index.vocab)) {
        const set = new Set();
        for (const e of index.entries) for (const f of ['tk','qtk','alias_tk','dtk','stk']) { const a = e[f]; if (a) for (const t of a) if (t) set.add(t); }
        index.vocab = Array.from(set).sort();
      }
      const postings = new Map();
      for (let i = 0; i < index.entries.length; i++) {
        const e = index.entries[i];
        let toks = e.tk || [];
        if (e.qtk) toks = toks.concat(e.qtk);
        if (e.alias_tk) toks = toks.concat(e.alias_tk);
        if (e.dtk) toks = toks.concat(e.dtk);
        if (e.stk) toks = toks.concat(e.stk);
        for (const t of toks) { let ids = postings.get(t); if (!ids) postings.set(t, (ids = [])); if (ids[ids.length-1] !== i) ids.push(i); }
      }
      const inverted = {};
      for (const t of index.vocab) inverted[t] = postings.get(t) || [];
      index.inverted = inverted;
      const av = new Set();
      for (const e of index.entries) for (const f of ['dtk','qtk','stk']) { const a = e[f]; if (a) for (const t of a) if (t) av.add(t); }
      index._areaVocab = av;
      return index;
    }

    function runGeocoderSearch(query, index){
      if (!index || !Array.isArray(index.entries)) return [];
      const qn = norm(query);
      if (qn.length < 1) return [];
      const rawToks = qn.split(/\s+/).filter(Boolean);
      const toks = rawToks.map(skel);
      if (toks.length === 0) return [];

      const blIdx = toks.indexOf('bl');
      const qBlk = blIdx >= 0 && blIdx+1 < toks.length ? toks[blIdx+1] : null;
      const qBlkDisplay = blIdx >= 0 && blIdx+1 < rawToks.length ? rawToks[blIdx+1] : null;
      const av = index._areaVocab || new Set();
      const areaPresent = qBlk != null && toks.some(function (t) { return t !== 'bl' && t !== 'vh' && t !== qBlk && av.has(t); });
      const areaBlockTyped = qBlk != null && areaPresent;
      const bareBlockTyped = qBlk != null && !areaPresent && !toks.includes('vh') && toks.every(function (t) { return t === 'bl' || t === qBlk; });
      const blockTyped = areaBlockTyped;

      // F1 (search-quality cycle, frame §6 2026-07-02; ported from searchLogic.js) —
      // entrance-TYPED query detection: an EXPLICIT вх/vh token FOLLOWED by an
      // entrance designator (a number "9"/"11", number+letter "1а", or a single
      // letter "а"/"b"). A dangling "вх" or "вх <word>" is NOT entrance-typed.
      // Consumed ONLY by comparator slot (4) below: an entrance-typed query ranks
      // the matched entrance child ABOVE an equal-relevance non-entrance row, so
      // Enter on "бл 307 вх 9" selects the вход child, not the "вх 9-11" адрес row.
      // Every other query keeps slot (4) byte-identical.
      const vhIdx = toks.indexOf('vh'); // skel('вх') === skel('vh') === 'vh'
      const entranceTyped =
        vhIdx >= 0 && vhIdx + 1 < rawToks.length &&
        /^(?:[0-9]+[a-zа-я]?|[a-zа-я])$/.test(rawToks[vhIdx + 1]);

      let vocab = index.vocab;
      if (!Array.isArray(vocab)) { const set = new Set(); for (const e of index.entries) for (const t of (e.tk||[])) if (t) set.add(t); vocab = Array.from(set); }
      const inverted = index.inverted && typeof index.inverted === 'object' ? index.inverted : null;

      const ms = toks.map(function (t) { return matchKindSet(t, vocab); });
      const numericTok = toks.map(function (t) { return /^[0-9]+$/.test(t); });

      let candidateIds = null;
      if (inverted) { candidateIds = new Set(); for (const m of ms) { for (const vt in m) { const ids = inverted[vt]; if (ids) for (let i = 0; i < ids.length; i++) candidateIds.add(ids[i]); } } }

      const scored = [];
      const scoreEntry = function (e) {
        if (!e) return;
        let matched = 0, exactName = 0, exactNum = 0, prefix = 0, fuzzy = 0, matchedCore = 0, matchedViaDtk = 0, matchedViaStk = 0;
        let qBlkMatched = false, all = true;
        const tk = e.tk || [], qtk = e.qtk || null, atk = e.alias_tk || null, dtk = e.dtk || null, stk = e.stk || null;
        for (let qi = 0; qi < toks.length; qi++) {
          const m = ms[qi]; let best = 0;
          for (let ti = 0; ti < tk.length; ti++) { const k = m[tk[ti]]||0; if (k > best) { best = k; if (best === 3) break; } }
          if (atk && best < 3) { for (let ti = 0; ti < atk.length; ti++) { const k = m[atk[ti]]||0; if (k > best) { best = k; if (best === 3) break; } } }
          if (best > 0) matchedCore += 1;
          if (qtk && best < 3) { for (let ti = 0; ti < qtk.length; ti++) { const k = m[qtk[ti]]||0; if (k > best) { best = k; if (best === 3) break; } } }
          if (dtk && best < 3) { for (let ti = 0; ti < dtk.length; ti++) { const k = m[dtk[ti]]||0; if (k > best) { best = k; matchedViaDtk += 1; if (best === 3) break; } } }
          if (stk && best < 3) { for (let ti = 0; ti < stk.length; ti++) { const k = m[stk[ti]]||0; if (k > best) { best = k; matchedViaStk += 1; if (best === 3) break; } } }
          if (best === 0) { all = false; continue; }
          matched += 1;
          if (blockTyped && toks[qi] === qBlk) qBlkMatched = true;
          if (best === 3) { if (numericTok[qi]) exactNum += 1; else exactName += 1; } else if (best === 2) prefix += 1; else fuzzy += 1;
        }
        if (matched > 0) {
          const dem = e.quarter_assignment_trust === 'conflicted' && matchedCore === 0 ? 1 : 0;
          const ddem = matchedCore === 0 && matchedViaDtk > 0 ? 1 : 0;
          const odem = e.odem ? 1 : 0;
          const sdem = matchedCore === 0 && matchedViaStk > 0 ? 1 : 0;
          const bmatch = blockTyped && (e.btk || []).includes(qBlk) ? 1 : 0;
          scored.push({ e: e, matched: matched, exactName: exactName, exactNum: exactNum, prefix: prefix, fuzzy: fuzzy, all: all, dem: dem, ddem: ddem, sdem: sdem, odem: odem, bmatch: bmatch, qBlkMatched: qBlkMatched ? 1 : 0, bdem: 0 });
        }
      };
      if (candidateIds) { for (const id of candidateIds) scoreEntry(index.entries[id]); }
      else { for (const e of index.entries) scoreEntry(e); }

      const existsBtkHolder = blockTyped && scored.some(function (s) { return s.bmatch === 1; });
      if (existsBtkHolder) { for (const s of scored) s.bdem = (s.qBlkMatched === 1 && s.bmatch === 0) ? 1 : 0; }

      scored.sort(function (a, b) {
        if (a.all !== b.all) return a.all ? -1 : 1;
        if (b.matched !== a.matched) return b.matched - a.matched;
        if (b.exactName !== a.exactName) return b.exactName - a.exactName;
        if (b.exactNum !== a.exactNum) return b.exactNum - a.exactNum;
        if (b.prefix !== a.prefix) return b.prefix - a.prefix;
        if (a.bdem !== b.bdem) return a.bdem - b.bdem;
        if (a.dem !== b.dem) return a.dem - b.dem;
        if (a.ddem !== b.ddem) return a.ddem - b.ddem;
        if (a.sdem !== b.sdem) return a.sdem - b.sdem;
        if (a.odem !== b.odem) return a.odem - b.odem;
        const aRank = a.e.life_safety_rank == null ? 2 : a.e.life_safety_rank;
        const bRank = b.e.life_safety_rank == null ? 2 : b.e.life_safety_rank;
        if (aRank !== bRank) return aRank - bRank;
        const aEnt = a.e.en !== undefined, bEnt = b.e.en !== undefined;
        // F1 — direction-gated slot (4): typed-entrance queries rank the entrance
        // child first at equal relevance; all other queries keep the pre-existing
        // "precise before entrance" demotion byte-identical.
        if (aEnt !== bEnt) {
          if (entranceTyped) return aEnt ? -1 : 1;
          return aEnt ? 1 : -1;
        }
        const al = (a.e.tk||[]).length + (a.e.qtk ? a.e.qtk.length : 0);
        const bl = (b.e.tk||[]).length + (b.e.qtk ? b.e.qtk.length : 0);
        if (al !== bl) return al - bl;
        return (a.e._ord||0) - (b.e._ord||0); // determinism (cadnum dropped)
      });

      // physical_building dedup: physical_building_id is DROPPED -> pbid always null
      // -> every row passes through (the block is inert but preserved verbatim).
      const isEntranceQuery = toks.includes('vh');
      let ranked = scored;
      if (!isEntranceQuery) {
        const reps = index.physical_building_reps && typeof index.physical_building_reps === 'object' ? index.physical_building_reps : {};
        const rankOf = function (s) { return s.e.life_safety_rank == null ? 2 : s.e.life_safety_rank; };
        const trueTie = function (a, b) { return a.all === b.all && a.matched === b.matched && a.exactName === b.exactName && a.exactNum === b.exactNum && a.prefix === b.prefix && a.bdem === b.bdem && a.dem === b.dem && a.ddem === b.ddem && a.sdem === b.sdem && a.odem === b.odem && rankOf(a) === rankOf(b); };
        const keptPos = new Map(); ranked = [];
        for (const s of scored) {
          const pbid = s.e.physical_building_id;
          if (pbid == null || s.e.en !== undefined) { ranked.push(s); continue; }

codex
HEAD е `f745349`; планът и двата адресни файла нямат разлика спрямо него. `index.html` има стейджнати промени от Б3, затова ще проверя матчера и спрямо посочения комит. В плана вече личи важен риск: грешно присвоен квартал може чрез Р14 да потисне търсенето по познатото име.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$t=Get-Content -LiteralPath '"'index.html' -Encoding UTF8; "'$t[5268..5320]' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 'function (norm|skel|matchKindSet)|function initAddressSearch' index.html" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$t=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md' -Encoding UTF8; "'$t[300..449]' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import json,sys,collections
sys.stdout.reconfigure(encoding='utf-8')
for f in ['data/search_index.json','data/address_rows.json','scratch/boundary_gallery/granitsi_preview_05.09/adresi_proposal_08.09.json']:
 d=json.load(open(f,encoding='utf-8')); print(f)
 if isinstance(d,dict):
  print('keys',list(d))
  for k,v in d.items():
   if not isinstance(v,list): print(k,str(v)[:2500])
   else: print(k,'len',len(v),'sample',str(v[:1])[:3000])
 else: print('len',len(d),'sample',d[:1])
'@ | python -B -" in C:\git\Fire_Varna
 succeeded in 673ms:
index.html

 succeeded in 887ms:
**ПРОМЯНА · `package.json`** — `build:signed-quarters`, `test:signed-quarters`, `test:block-orientation`, `test:fire-varna-determinism`; **`build:fire-varna` (подразбиращият се път, който пише в `../Fire_Varna/data` и НЕ строи манифеста) се обявява за забранен** — доставя се само през `:staging` + ръчно копиране на трите файла заедно.

**НОВ · `docs/decisions/064_signed_quarter_polygons_decide_the_public_quarter.md`** — ADR (кондензиран шаблон) + ред в `docs/decisions/README.md`; изрично: кои клаузи на ADR 006/007 се вдигат, кои разминавания с ADR 010 се обявяват (Р6-б), че `sw.js` и съдържанието на `address_rows.json` остават недосегаеми; `docs/activeContext.md` + `docs/unknowns.md` в същия ред.

### 4.2 `C:/git/varna_3d`
**Нула промени, нула комита.** Само четене на блоба по OID (М0.1).

### 4.3 `C:/git/Fire_Varna` (Executor комитва кода; данните — Петър)

**ПРОМЯНА · `index.html`:**
1. `:5134` и `:5140-5145` — `wtk` и `otk` влизат в резервния vocab и в postings.
2. `:5151` `_areaVocab` остава `['dtk','qtk','stk']` — **`wtk` и `otk` НЕ влизат** (иначе „студентска бл 11“ сменя клона на рендера, `:5168-5171` → `:5278-5288`).
3. След `:5152`: `index._signedQuarterVocab` = множеството токени, произведени от **`quarter_names`** (Р14-б), не от наблюдаваните `qtk`.
4. След `:5185`: `qFilterTok[qi] = _signedQuarterVocab.has(toks[qi])`.
5. `scoreEntry` **след `:5209`**: клон за `wtk` — при `qFilterTok[qi] === true` **И** `e.q != null` свидетелят се пропуска изцяло (`best` остава 0 → `all=false`); иначе важи с `matchedViaWitness += 1`. Отделен клон за `otk` с `matchedViaOtkOnly`.
6. `:5216-5221`: `wdem = matchedViaWitness > 0 && matchedCore === 0 ? 1 : 0`; **`otdem = matchedViaOtkOnly > 0 ? 1 : 0`** (per-token, съзнателно различно от `sdem`, който е мъртъв при блокови заявки, защото `bl`/номерът винаги удрят `tk`); нови редове в компаратора между `:5239` и `:5240` и в `trueTie` (`:5265`).
7. `:5252-5253` подредбата остава `tk.length + qtk.length` — `wtk`/`otk` не се броят; делтата от смяната на `qtk` се обяснява в replay-а.
8. `baseAddressLabel` (`:4881-4892`) остава само адрес; нови `quarterPrefix(hit)` от `quarter_names[hit.q]` и `orientationSuffix(hit)` от `orientations[hit.o]`; `formatAddressHit` (`:4893-4897`) композира `prefix + ', ' + base + suffix` (липсващ `q`/`o` → съответната част отпада).
9. `dedupeDisplayRows` (`:5088-5100`): ключът става `norm(label) + '||' + (g ?? '') + '||' + (q ?? '') + '||' + (o ?? '')`.
10. Двете проекции (`:5303`, `:5313`) получават `q` и `o`.
11. `buildExactItem` (`:5411-5423`): заглавието минава през `formatAddressHit`; редът „район X“ (`:5420`) остава непроменен; класът `.asr-item` не се пипа.
12. `ctx` при избор (`≈:5858-5866`) и заглавието на панела (`≈:5648`) взимат същия композиран низ.
13. **`validateSearchPayload(idx, rowsPayload)` — нова функция ВЪТРЕ в среза** (Р0-б флагът я не изключва), викана от `ensureSearchData` преди `searchIndex = idx` (`:5364`): `index_schema_version === '3.0'`; всяко `q`/`o` резолвира; `idx.address_row_count === rowsPayload.rows.length`. Отказ = цялата доставка се отхвърля.
14. `:5327` `SEARCH_CACHE` → `'fire-varna-search-v3'` в СЪЩИЯ комит с payload-а. **`sw.js` не се пипа** (§0.12); старият кеш `fire-varna-search-v2` остава да лежи — записва се като дълг (§9).
15. Маркери за среза: `// ---- ADDR slice start` … `// ---- ADDR slice end` около `norm/skel/matchKindSet/prepareIndex/runGeocoderSearch/scoreEntry/formatAddressHit/dedupeDisplayRows` **и около `validateSearchPayload`** (иначе G-B5 е неизпълним). Липсващ маркер = `AssertionError`.
16. Не се пипат: `'Няма съвпадения'` (`:5430`), `APPROX_ADDRESS_SEARCH_ENABLED` (`:5926`), PLACES клонът.

**НОВ · `tests/address_replay.mjs`** — изрязва среза по маркерите и го изпълнява в Node със стъбове (модел `tests/granitsi_client_probe.mjs`), с флага `ADDRESS_PATH_V2` в двете положения.
**НОВ · `scratch/places_search/address_corpus_build.py`** — **детерминистичен селектор** на корпуса (сортиран обход на класовете, фиксирано правило „първите N по нарастващ `_ord`“, без произволност, без seed) → пише кандидата в temp и, само с `--freeze`, проследената референция.
**НОВ · `scratch/places_search/address_replay_rows.json`** — замразеният корпус, сверяван като **блоб** (`git show HEAD:`; готовата проверка е `worktree_differs`, `gates/release.py:313`). Стратификация ≥ 8 заявки на клас: съгласни · несъгласни (Виница-зона, Колхозен пазар, Цветен квартал, Чайка/Студентска, микрорайон) · вътре без дума · извън всички · **извън, но в лентата на един** · parent/child · несравними · в лентата · блокови колизии · вход · координатен клон · **display_id път**. Всеки ред носи кой дисплей път е дал текста.
**НОВ · `tests/test_address_replay.py`** — обвивката; чете очакванията от нова секция `address_replay` в `expectations.json` („No number below is typed by an agent“ — числата идват от `--freeze`).
**НОВ · `tests/test_address_generation.py`** — сверява `data/generation_manifest.json` (`sha256/bytes/entry_count/address_row_count/max_display_id`) срещу блобовете в СЪЩАТА снимка (`git show :<path>` / `HEAD:<path>`) + подписания таван от Р12-в.
**НОВ · `gates/probe/addr_g11.py`** — по Р18 (или разширяване на `ALLOWED_NEW`, ако Петър избере другия вариант).
**ПРОМЯНА · `gates/run_gates.py`** — `PUBLIC_BLOBS` (`:82-87`) += двата адресни блоба; **проверка 3 се пренаписва:** чете блоба (`git show :<path>`), а **липсващ файл от списъка става ЧЕРВЕН, не тих пропуск** (`:188-190`). `SHA_PINS` не се пипа.
**ПРОМЯНА · `tests/test_data_ascii_mojibake.py`** — обхватът включва `quarter_names`, `orientations` и `label`; сигнатури `U+FFFD` и `[Ð Ñ Â][\u0080-\u00FF]`.
**ПРОМЯНА · `docs/decisions/007_address_path_v2.md`** — амандамент (write-set + разпиноване на scorer/comparator + новите гейтове; `address_rows.json` и `sw.js` остават недосегаеми) + `docs/activeContext.md`.

**ДАННИ (комитва Петър):** `data/search_index.json`, `data/address_rows.json`, `data/generation_manifest.json` — трите заедно, в един комит.

---

## 5 · Ред на изпълнение

### 0. Предусловие (ръката на Петър)
Б3 се комитва пръв (данните са негови). След това `git status --porcelain` няма стейджнати `data/` и `index.html` пътища — проверява се от Изпълнителя (М0.11); ако не е така — **СТОП**.

### А. Varna_buildings (Executor, локални комити)
1. **М0** (§1.Б) → `output/addr_quarter_M0.json`. Без него нищо не тръгва.
2. Копира полигоните през Python по OID (никакви `>` и `|`); проверява `git check-ignore -v output/quarters_signed.geojson`.
3. **V1** `tools/build_signed_quarter_index.py` + схемата → `feat(quarters): bake signed quarter polygons into a private resolver input`
4. **V2** `js/lib_signed_quarters.mjs` → `feat(quarters): add lib_signed_quarters resolver with a pinned polygon digest`
5. **V3** `js/test_signed_quarter_resolver.mjs` → `test(quarters): resolver truth gate with poisoned fixtures`
 *Доказателство:* вариант с „най-близък полигон“ трябва да **падне**; изходът се записва.
6. **V4** `js/lib_block_orientation.mjs` → `feat(fire-varna): block orientation model with own and nearest street`
7. **V5** генераторът: `q` + `wtk` + `otk`/`o` + `quarter_names`/`orientations` + schema 3.0 + Р38 подчинение + излизане на квартала от `label` → `feat(fire-varna): canonical quarter q, witness wtk and structural block orientation`
8. **V6** материализацията по Р12-б → `feat(fire-varna): materialise labels where the address text contradicts the signed quarter`
9. **V7** частният леджер + брояците → `feat(fire-varna): private quarter ledger and build-report counters`
10. **V8** публикационният гейт (нови ключове, затворено топ-ниво, полигонният вход, 7 фикстури) → `test(fire-varna): publish gate verifies the quarter against the signed polygons`
11. **V9** ориентирният гейт → `test(fire-varna): block orientation gate with a signed floor and collision fixtures`
12. **V10** детерминизъм → `test(fire-varna): byte-identical rebuild gate`
13. **V11** ADR 064 + индекс + activeContext + unknowns → `docs(adr): ADR 064 signed quarter polygons decide the public quarter word`
14. Билд през staging + гейтовете G-A* (никакъв билд по подразбиращия се път).

### Б. Fire_Varna (Executor, локални комити — само код)
15. **F1** клиентът (16-те точки) + маркерите + `ADDRESS_PATH_V2` → `feat(search): render the canonical quarter and the block orientation from structured fields`
16. **F2** replay двигателят + селекторът на корпуса + `expectations.address_replay` + `tests/test_address_replay.py` → `test(search): address replay gate with a frozen stratified corpus`
17. **F3** `gates/run_gates.py` (блоб-четене + липсващ файл = червено) + `tests/test_address_generation.py` + mojibake обхватът + `gates/probe/addr_g11.py` → `feat(gates): address blobs join the cadastral-id, geometry and manifest checks`
18. **F4** амандаментът на ADR 007 + `docs/activeContext.md` → `docs: ADR 007 amendment for the signed-quarter address delivery`

### В. Доставка на данните
19. Изпълнителят копира трите файла от `output/fire_varna_staging/` в `Fire_Varna/data/` **заедно** и пуска целия набор гейтове. Не комитва.
20. Петър комитва данните (D16/G4).

### Г. Една публикация
Ред: **Б3 (ръката на Петър) → Varna_buildings → varna_3d (нула) → Fire_Varna код → адресните данни (ръката на Петър)**. Подпис и замразяване САМО когато и двете доставки са в HEAD. Една опашка (`ЗА_ПОДПИС_Б3_07.09.md` — адресните редове се ДОБАВЯТ в нея; преименуването на старата опашка е ход на Б3, не на този лот). Един allow-файл (адресният лот не иска нови allow редове). Едно `--freeze` за местата и едно за адресите, и двете СЛЕД подписа, всяко със свой комит. Един назован червен интервал по G20, различим от Б3-евия.

### Д. Командите на Петър (по една на ред, без `&&`; **без `git push`**)

```powershell
cd C:\git\Varna_buildings
npm run build:signed-quarters
npm run test:signed-quarters
npm run test:block-orientation
npm run build:fire-varna:staging
npm run test:fire-varna-publish-gate:staging
npm run test:fire-varna-determinism
cd C:\git\Fire_Varna
git status --porcelain
git add data/search_index.json data/address_rows.json data/generation_manifest.json
git commit -m "data(search): quarter from signed polygons + block orientation"
$env:PYTHONIOENCODING="utf-8"
python -m unittest discover -s tests
python -m gates.run_gates
python gates/probe/addr_g11.py <комитът преди първия ход на лота>
python -m gates.sign R<n> да --queue scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md
git add scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md
git commit -m "sign: address delivery rows"
python scratch/places_search/address_corpus_build.py --freeze
git add scratch/places_search/address_replay_rows.json scratch/places_search/expectations.json
git commit -m "freeze: address replay reference"
python -m unittest discover -s tests
python -m gates.run_gates
```

**ПУБЛИКУВАНЕ — след Gate 2, с отделна твоя дума.** (v1 слагаше `git push` редом с 13 неподписани решения; `python -m gates.sign` без аргументи пада с usage, `gates/sign.py:419-427`; `--freeze` преди комит прави проверка 6 BLOCKED, `gates/release.py:313`.)

---

## 6 · Гейтове

Всеки ред: команда · очакван изход · отрицателна фикстура, която ТРЯБВА да падне.

| # | Гейт | Команда | Изход | Отрицателното (задължително пада) |
|---|---|---|---|---|
| G-A1 | Пинът на полигоните (OID + sha, четени в Python) | `python tools/build_signed_quarter_index.py` | 0 | подменен байт в опечения вход; подаден commit-ish вместо OID |
| G-A2 | Публикационен гейт (разширен) | `npm run test:fire-varna-publish-gate:staging` | 0 | ф1 `coordinates` в нов топ-ключ; ф2 `q` извън обхват; ф3 неканоничен `qtk`; ф4 `wtk∩qtk≠∅`; ф5 не-низ в `quarter_names`; ф7 `o` без ред |
| G-A3 | **Истинност на резолвера** | `node js/test_signed_quarter_resolver.mjs` | 0 | (а) резолвер с „най-близък полигон“; (б) пин в зоната Виница вътре в Манастирски рид, обявен за Виница; (в) недоказан parent, обявен за дете |
| **G-A3-г** | **Флагманът, поименно** | част от G-A3 | 0 | **пинът `[43.22212, 27.9378]` ТРЯБВА да върне присъда, която дава „кв. Левски“** (при подписания Р5); пинът `[43.21976, 27.91949]` ТРЯБВА да върне класа по Р5-д |
| G-A4 | **Свидетелят не е авторитет — върху ДОСТАВЕНИТЕ байтове** | част от G-A2 (с полигонния вход) | 0 | ф6: запис с `q`/`qtk` = Чайка при пин вътре в кв. Левски |
| G-A5 | Пълнота на леджера (вкл. `source`/`mode`/`confidence` на свидетеля) | `node js/test_quarter_ledger.mjs` | 0 | изтрит ред за запис с различен свидетел |
| G-A6а | **Ориентир — подписан ПОД, не дизюнкция** | `node js/test_block_orientation.mjs` | 0 | брой блокови редове с `own`/`nearest` под пода от М0.6 (при валидни причини) → червено; причина извън затворения списък → червено |
| G-A6б | Различимост при колизия | същият | 0 | две групи в една двойка (квартал, блок №) с еднакъв ориентир и **извън** подписания списък изключения |
| G-A6в | Качество на ориентира | същият | 0 | ориентир с отхвърлен низ („ул кк зл пясъци…“); ориентир над подписания праг без бележка за разстояние |
| G-A7 | Р38 подчинение | част от G-A3 | 0 | ред в зоната с подписан фин квартал, префиксиран „кв. Виница“ |
| G-A8 | Два билда байт-идентични | `npm run test:fire-varna-determinism` | 0 | подменен байт в едното копие |
| G-A9 | Дрифт: S9 + C2 | вграден в билда (`:1042-1051`) + брояч | 0 | `tokenInconsistentTotal` > 20 % от 5 828; **`c2ResByReason.token_inconsistent` над подписания таван от М0.7** |
| G-A10 | Бюджет на диффа по етикетите | част от билда | 0 | брой сменени `label` извън подписания интервал (квартален сегмент + махнатия уличен суфикс) |
| G-B1 | Нула геометрия, структурно | `python gates/probe/addr_g11.py <родител>` | 0 | копие с ключ `coordinates`; **нов непосочен проследен файл → изход 1** (истински родител, не `HEAD`, иначе рамото е инертно) |
| G-B2 | Нула кадастрални id в адресните блобове | `python -m gates.run_gates` (проверка 3, вече по блоб) | 0 | посят `10135.1.1005.1` в **блоба**; **преименуван/липсващ файл от `PUBLIC_BLOBS` → червено** |
| G-B3 | Поколение ↔ размер ↔ броеве ↔ таван | `python -m unittest tests.test_address_generation` | 0 | чужд `bytes` в манифеста; `address_row_count ≠ rows.length`; сбор над подписания таван (Р12-в) |
| G-B4 | **Address replay** | `python -m unittest tests.test_address_replay` | 0 | (i) „чайка студентска бл 11“ като ПЪЛНО съвпадение; (ii) ред, назначен по най-близък полигон; (iii) два неразличими „бл 11 левски“; (iv) **заявка, която днес не е `blockTyped`, а утре става**; (v) `ADDRESS_PATH_V2=false`, който не връща базовото поведение |
| G-B5 | **Клиентска fail-closed валидация (собствен ред)** | `python -m unittest tests.test_address_replay -k validate` | 0 | (а) `index_schema_version "2.0"`; (б) `q` извън `quarter_names`; (в) несъвпадащи поколения на двата файла |
| G-B6 | `FORBIDDEN` остава зелен | `python -m unittest tests.test_b3_gates` | без нови червени спрямо М0.9 | забранен низ, вкаран в адресен етикет |
| G-B7 | Mojibake / UTF-8 | `python -m unittest tests.test_data_ascii_mojibake` | 0 | посято `Ð` и `U+FFFD` в `quarter_names`/`orientations` |
| G-B8 | Пълният набор | `python -m unittest discover -s tests` · `python -m gates.run_gates` | 0 червени извън назования интервал; 7/7 след подписа | — |

---

## 7 · STOP — спри и питай Петър

1. М0.1/М0.3/М0.4/М0.5 дават числа, различни от §1.А.
2. **М0.5-б показва за флагмана присъда, различна от подписаната по Р4/Р5** (тогава лотът не решава жалбата и това се казва веднага).
3. **М0.6 се разминава с §1.А** (385 ↔ 91 ↔ 95; 24 ↔ 16; 1 324 ↔ 213).
4. Който и да е гейт е червен и поправката не е очевидно безопасна.
5. Билдът иска промяна в `config/quarter_registry.json`.
6. Блоковите колизии след смяната се променят с > 20 % спрямо М0.7.
7. `c2ResByReason.token_inconsistent` расте над подписания таван (ориентирът яде етикети).
8. S9 `tokenInconsistentTotal` мърда с > 20 % спрямо 5 828.
9. Сборът на двата lazy payload-а мине подписания таван (Р12-в).
10. Резолверът иска ново публично поле извън `q`, `wtk`, `otk`, `o`.

 succeeded in 922ms:
          if (pbid == null || s.e.en !== undefined) { ranked.push(s); continue; }
          if (!keptPos.has(pbid)) { keptPos.set(pbid, ranked.length); ranked.push(s); continue; }
          const pos = keptPos.get(pbid), kept = ranked[pos];
          if (String(s.e._ord) === String(reps[pbid]) && String(kept.e._ord) !== String(reps[pbid]) && trueTie(kept, s)) ranked[pos] = s;
        }
      }

      // area-gated block GROUPING (opaque g instead of bg||complex_id).
      let blockHeader = null;
      if (blockTyped && !isEntranceQuery) {
        const seen = new Set(); const grouped = []; let blockGroups = 0; const districtCount = new Map();
        for (const s of ranked) {
          const key = s.e.g;
          if (key != null) { if (seen.has(key)) continue; seen.add(key); }
          grouped.push(s);
          if (s.all && s.bmatch === 1) { blockGroups += 1; const d = s.e.d; if (d != null) districtCount.set(d, (districtCount.get(d)||0)+1); }
        }
        ranked = grouped;
        if (blockGroups > 0) { let bestD = null, bestN = -1; for (const pair of districtCount) if (pair[1] > bestN) { bestN = pair[1]; bestD = pair[0]; } blockHeader = { block: qBlkDisplay, count: blockGroups, district_enum: bestD }; }
      }

      // bare-block surface (parent/child), grouped by opaque g.
      if (bareBlockTyped) {
        const parentCandidates = [];
        for (const s of ranked) if (s.all && s.e.en === undefined && (s.e.btk || []).includes(qBlk)) parentCandidates.push(s);
        if (parentCandidates.length > 0) {
          const repByGroup = new Map();
          for (const s of parentCandidates) { const key = s.e.g; if (key == null) continue; if (!repByGroup.has(key)) repByGroup.set(key, s); }
          const childrenByGroup = new Map();
          for (const s of ranked) { if (s.e.en === undefined) continue; const key = s.e.g; if (key == null || !repByGroup.has(key)) continue; if (!childrenByGroup.has(key)) childrenByGroup.set(key, []); childrenByGroup.get(key).push(s); }
          const childSort = function (a, b) { const na = /^[0-9]+$/.test(a.e.en) ? parseInt(a.e.en,10) : NaN, nb = /^[0-9]+$/.test(b.e.en) ? parseInt(b.e.en,10) : NaN; const an = !Number.isNaN(na), bn = !Number.isNaN(nb); if (an && bn && na !== nb) return na - nb; if (an !== bn) return an ? -1 : 1; if (a.e.en !== b.e.en) return String(a.e.en).localeCompare(String(b.e.en)); return (a.e._ord||0) - (b.e._ord||0); };
          const bareDistrictCount = new Map(); const groupList = [];
          for (const pair of repByGroup) { const key = pair[0], rep = pair[1]; const children = (childrenByGroup.get(key) || []).slice().sort(childSort); groupList.push({ key: key, rep: rep, children: children }); const d = rep.e.d; if (d != null) bareDistrictCount.set(d, (bareDistrictCount.get(d)||0)+1); }
          groupList.sort(function (a, b) { const da = a.rep.e.d == null ? Infinity : a.rep.e.d, db = b.rep.e.d == null ? Infinity : b.rep.e.d; if (da !== db) return da - db; return (a.rep.e._ord||0) - (b.rep.e._ord||0); });
          const projectRow = function (s, role) { const e = s.e; return { kind: e.kind, en: e.en, pin: e.pin, d: e.d, label: e.label, display_id: e.display_id, g: e.g, allTokens: s.all, matched: s.matched, exact: s.exactName + s.exactNum, prefix: s.prefix, fuzzy: s.fuzzy, bareRole: role, block: qBlkDisplay }; };
          const bareOut = [];
          for (const g of groupList) { bareOut.push(projectRow(g.rep, 'parent')); for (const c of g.children) bareOut.push(projectRow(c, 'child')); }
          bareOut.bareBlockHeader = { block: qBlkDisplay, groups: groupList.length, districts: Array.from(bareDistrictCount, function (p) { return { district_enum: p[0], count: p[1] }; }).sort(function (a, b) { return a.district_enum - b.district_enum; }) };
          return bareOut;
        }
      }

      const out = ranked.slice(0, SEARCH_LIMIT).map(function (s) {
        const e = s.e;
        return { kind: e.kind, en: e.en, pin: e.pin, d: e.d, label: e.label, display_id: e.display_id, g: e.g, allTokens: s.all, matched: s.matched, exact: s.exactName + s.exactNum, prefix: s.prefix, fuzzy: s.fuzzy };
      });
      if (blockHeader) out.blockHeader = blockHeader;
      return out;
    }

    // ---- lazy load + cache (memory for the session + Cache API offline) ----------
    // TWO payloads: the matcher index (search_index.json) + the display rows
    // (address_rows.json). Both lazy-load on first focus, are parsed once, and are

 succeeded in 1096ms:
data/search_index.json
keys ['index_schema_version', 'kind', 'coordinate_order', 'district_names', 'address_row_count', 'entries', 'vocab']
index_schema_version 2.0
kind fire_varna_search_index
coordinate_order [lat,lng]
district_names len 5 sample ['Аспарухово']
address_row_count 80510
entries len 86232 sample [{'kind': 'address', 'pin': [43.22715, 27.87219], 'tk': ['1'], 'd': 2, 'label': 'atanas dalchev|1'}]
vocab len 2889 sample ['/briz/']
data/address_rows.json
keys ['schema_version', 'kind', 'coordinate_order', 'field_order', 'rows']
schema_version 2.0
kind fire_varna_address_rows
coordinate_order [lat,lng]
field_order len 3 sample ['normalized_address']
rows len 80510 sample [['1', 43.22715, 27.87219]]
scratch/boundary_gallery/granitsi_preview_05.09/adresi_proposal_08.09.json
keys ['generated_for', 'entries']
generated_for проба 08.09 — предложение за адресния лот; нищо от това не е в репото
entries len 5274 sample [{'pin': [43.23681, 27.87839], 'no': '14', 'old': 'ж.к. Възраждане, бл. 14', 'witness': 'ж.к. Възраждане', 'new_v1': 'район Младост, бл. 14, до ана феликсова', 'new_v2': 'район Младост, бл. 14, до ана феликсова', 'cls': 'overlap', 'poly': 'ж.к. Възраждане 1 / ж.к. Възраждане', 'edge_m': None, 'band': None, 'district': 'район Младост', 'orient': 'до ана феликсова', 'orient_src': 'най-близка улица 0 m', 'vh': None, 'tk': ['ana', 'feliksova', '18', 'bl', '14', 'vazrazhdane'], 'qtk': None}]

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$t=Get-Content -LiteralPath '"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md' -Encoding UTF8; "'$t[450..599]' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg --max-count 20 --max-columns 200 -n 'function (norm|skel|matchKindSet)|function initAddressSearch' index.html" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import json,sys,collections
sys.stdout.reconfigure(encoding='utf-8'); d=json.load(open('scratch/boundary_gallery/granitsi_preview_05.09/adresi_proposal_08.09.json',encoding='utf-8'))['entries']; print('classes',collections.Counter(e['cls'] for e in d));
for e in d:
 if e['pin']==[43.22212,27.9378] or ('11'==str(e['no']) and ('Студентска' in e['old'] or 'studentska' in e['tk'])):print(e)
'@ | python -B -" in C:\git\Fire_Varna
 succeeded in 807ms:
1828:  function normalizeHydrantRecord(raw) {
4836:  (function initAddressSearch() {
4842:    function norm(s){return (''+(s||'')).toLowerCase().replace(/блок/g,'бл').replace(/вход/g,'вх').replace(/[.№,'"-]/g,' ').replace(/\s+/g,' ').trim();}
4843:[Omitted long matching line]
4848:[Omitted long matching line]
6413:    function norm(s){return (''+(s||'')).toLowerCase().replace(/блок/g,'бл').replace(/вход/g,'вх').replace(/[.№,'"-]/g,' ').replace(/\s+/g,' ').trim();}
6414:[Omitted long matching line]

 succeeded in 1095ms:
11. Появи се нужда да се пипне `data/address_rows.json`, `sw.js` или approx пакетът.
12. Втора опашка `ЗА_ПОДПИС_*` в HEAD или втори json в `gates/allow/`.
13. Някой ход изисква публикуване, remote достъп или `--no-verify`.
14. **`git diff --cached` не е празен преди F1 или преди `gates.sign`** (смесени поколения / чужди хънкове в адресния комит).
15. Пожелано е име за точка, която резолверът е обявил за неопределена („нека все пак сложим нещо“).

---

## 8 · Локален преглед (проби с очакван резултат)

`python -m http.server 8000`, 375 px, ръчно, преди Gate 2:

| # | Заявка | Очаквано |
|---|---|---|
| 1 | `бл 11 левски` | само блокове с пин в полигона кв. Левски **плюс** блокът на бул. Царевец (Р5-д, без квартална дума, демотиран); **всеки ред носи различен ориентир**; групата „N блока № 11“ брои каноничните |
| 2 | `студентска бл 11` | ред 1 = **кв. Левски, бл. 11, ул. Студентска** (Р10-а) или **…, до ул. Студентска** (Р10-б) — точно подписаният низ; „Чайка“ не се появява в заглавието; **рендерът остава в обикновения списък, не в груповия блоков клон** |
| 3 | `чайка студентска бл 11` | блокът **НЕ е пълно съвпадение** (`all=false`); ако излезе, е под редовете с истинска Чайка |
| 4 | `бл 11 чайка` | само блокове в полигоните к.к./кв. Чайка; Студентска бл. 11 не е сред тях |
| 5 | `левски битоля 13` | без квартална дума, вторият ред е **„район Приморски“**; „левски“ не дава пълно съвпадение |
| 6 | `цветен квартал битоля` | намира (свидетелят работи), нито един ред не показва „Цветен квартал“ като квартал |
| 7 | `бреза 6` | заглавие **кв. Левски**, свидетелят остава търсим |
| 8 | `манастирски рид` / `акчелар` / `ален мак` / `бриз` | фините подписани квартали, не „кв. Виница“ |
| 9 | `дълбокото дере` | продължава да намира (Р38 „добавя, никога не реже“) |
| 10 | `27 юли 22` · `алеко константинов 10` | Център (ако вътре) · кв. Тракия |
| 11 | **ред по display_id пътя** (напр. `константин и фружин бл 302`) | заглавието носи квартала И ориентира; при материализация (Р12-б) няма „ж.к. Бриз, акчелар“ |
| 12 | `дружба бл 11` / ТВ кула | по подписания Р5; редът не изчезва |
| 13 | `ADDRESS_PATH_V2 = false` | поведението е базовото; нито един нов низ не се показва |
| 14 | празна проверка | конзолата без грешки; `data/search_index.json` 200; картата под 3 s; трите режима; PLACES взима Enter само при `'Няма съвпадения'` |
| 15 | смяна на поколението | при подменен `address_rows` клиентът **отказва** доставката (fail-closed); стар кеш v2 не се сервира на страницата |

---

## 9 · Рискове и дългове

1. **Смяна на собственика на Enter** — когато свидетелят спре да удовлетворява квартален филтър, някои заявки минават към PLACES (`:7508-7527`). Фикстура в двете посоки в G-B4.
2. **Подредбата ще се раздвижи** (`:5252-5253`) за 19 494 записа; делтата се обяснява в replay-а.
3. **Блоковите колизии се преизчисляват**; М0.7 е задължителната преди/след мярка.
4. **Записи, които губят кварталната си дума** — при Р5(в) са само неопределените класове; при Р5(а) са ~25 613 повече. Съзнателна цена, не изненада.
5. **Латиницата (31 916 етикета)** е отделен лот (ADR 007 D5.2) върху същите редове: първо кварталът, после латиницата.
6. **Регистърът е тесен, не полигоните** — `parent` за 6 от 60; ~2 985 записа остават неопределени заради това. Сутрешен списък.
7. **Полигони, които не раздават нито едно име** — броят зависи от подписания Р5 (при §4.1-строгия прочит на v1 бяха 15, при §2-прочита 11); финалният брой е ПОДПИСАНО очакване от М0.5.
8. **Дупките Център / Цветен квартал / Колхозен пазар** остават отворени.
9. **Replay-ът е нов двигател** — разсинхронизиран срез трябва да пада шумно (`AssertionError`).
10. **Двата адресни блоба нямат sha пин от край до край в клиента**; този лот стеснява дупката през манифеста (G-B3), пълният пин е дълг.
11. **Approx пакетът** ще внесе написаната дума наново, ако бъде запален без резолвера.
12. **Червената база** — днес `run_gates` exit 1 и 24/342 паднали; адресният интервал по G20 трябва да е различим.
13. **`PROTECTED_CACHES` (`sw.js:46`) остава да сочи `fire-varna-search-v2`** — след v3 това е мъртъв ред и старият кеш лежи, докато браузърът не го изчисти. Не се пипа тук (§0.12) → сутрешен списък.
14. **Написаният свидетел е 58 % OSM `nearest_point`** (флагманът — на 707 m). Това е аргумент да не е авторитет никога, и колона `source` в леджера; не е повод да се маха от търсенето.

---

## 10 · Какво НЕ се пипа

- `Varna_buildings/config/quarter_registry.json` и `REGISTRY_SIGNED_SHA256` (`js/lib_quarter_registry.mjs:45-46`); `lib_quarter_registry.mjs` (Д10).
- `Fire_Varna/data/address_rows.json` като съдържание (ADR 007 D2).
- **`Fire_Varna/sw.js`** (недосегаем по `006:158` и `007:13`; освен това промяната е без ефект — `sw.js:104-106`).
- `varna_3d` — нула комита.
- Стейджнатият Б3 write-set (14 пътя, вкл. `gates/probe/b3_g11.py` и `tests/test_b3_gates.py`) — освен ако Петър не подпише Р18 вариант „разширяване на `ALLOWED_NEW`“.
- `PRIVATE_KEYS` (`test_fire_varna_publish_gate.mjs:62-68`) и `FORBIDDEN_SUBSTRINGS` (`:101-104`).
- `SHA_PINS` (`index.html:6291-6293`, `gates/run_gates.py:68-72`); `SIGNABLE` (`gates/release.py:177-185`) — освен новата секция в `expectations.json`.
- `'Няма съвпадения'` (`index.html:5430`), класът `.asr-item`, `APPROX_ADDRESS_SEARCH_ENABLED` (`:5926`).
- Атрибуционните низове и `tests/test_b3_gates.py:43-44`.
- Подразбиращият се път `npm run build:fire-varna`.

---

## 11 · Отхвърлени находки (с измерената причина)

1. **„М0.1 е противоречие 05f485e ↔ 6486b48“ (находка на v1, оборена от gates/semantics/delivery — приема се ОБОРВАНЕТО, отхвърля се находката на v1).** Двамата опровергатели измериха един и същ блоб (`rev-parse` OID `82706fb5fef494175f912db82a871a6c38b4e472`, 301 917 B, sha256 `c1551d24…871b3`) за двата комита. В v2 пинът е OID, а СПИРАЙ по т. 1 отпада.
2. **semantics: „Планът отменя ADR 010 D6/D7/D8“ — ОТХВЪРЛЕНО КАТО ФОРМУЛИРОВКА.** Проверено в `docs/decisions/010_signed_quarter_boundaries.md:48-52`: D6 урежда канала `SIGNED_POLYGON` в `varna_3d/src/fire_varna_locations.py` (между ред 873 и 875) за **375-те места**, с гейтове в `qa_fire_varna_m6.py:304-308`; той не се произнася за адресния индекс, който се строи в друго репо, от друг конвейер, за друга повърхност. Затова „отмяна на подписан прецедент“ не е точно. **Задължението обаче е прието:** ADR 064 изрично изброява трите разминавания и казва, че ADR 010 остава непроменен за местата (Р6-б). D8 (геометрично доказано дете ⊆ родител) се приема ДОСЛОВНО и влиза в резолвера.
3. **semantics, „бонус“ към Битоля: „§1.А твърди, че Битоля носи `qtk = tsveten kvartal`“ — ОТХВЪРЛЕНО.** v1 §1.А цитира СКАУТ 3 §9, който дава ЕДИН пример („ул. Битоля 11, `qtk=tsveten kvartal`“), а не разпределение; същият СКАУТ в §3 брои `tsveten kvartal → кв. Левски` 318. Планът никога не е твърдял „всички Битоля са tsveten kvartal“. **Приета е обаче основната част:** районът в Р13.3/§8-5 е **Приморски**, не Одесос — `district_names` е проверен от Planner-а сега.
4. **gates, ПОПРАВКАТА за G-B2 („мутирай реалния път `data/search_index.json`, върни го след теста“) — ОТХВЪРЛЕНА КАТО МЕТОД.** Проверка 1 чете работното дърво (`run_gates.py:141-147`), а `release.worktree_differs` (`:313`) третира „modified/staged/untracked“ еднакво — мутиране на доставен tracked блоб по време на гейт-кръг може да влезе в подпис. Прието е ТВЪРДЕНИЕТО (фикстурата днес е зелена по конструкция) и е реализирано другояче: проверка 3 чете блоба (`git show :<path>`), списъкът се параметризира за теста, а липсващ файл става червен.
5. **delivery, „G-A1 никога не може да се съгласи с извора“ — ЧАСТИЧНО ОТХВЪРЛЕНО.** Пре-стъпката на v1 вече хвърляше при несъответствие на sha, тоест повреден копие би паднал шумно, а не тихо. Прието е реалното ядро: **пинът, изчислен през PowerShell пайп, е артефакт на обвивката** — затова в v2 всички байтове се четат в Python и пинът е OID.
6. **Числата, които двамата опровергатели дават различно, не са отхвърлени, а изпратени на М0** (11 641 ↔ 11 625; 24 ↔ 16 неразличими групи; 385 ↔ 91 ↔ 95 блока „11“; 1 324 ↔ 213 без улица; +1,26 ↔ +1,54 MB). Планът не може да носи две числа за едно нещо; М0 е единственият им източник, а разминаването е СПИРАЙ (§7 т. 1 и 3).

---

## 12 · Оборване (какво казаха трите опровержения и какво е приложено)

**Опровергател „gates“ — присъда НЕГОДНО.** 8 блокера, 6 мажора, 4 минора.
Приложени блокери: флагманът пада под собствената политика → **нов Р5 с вариантите (в)/(г) + G-A3-г с поименна фикстура**; М0.5 е измеримо днес и оборва Р5в → **фалшивият праг 15 % махнат, вариантите носят измерените си цени**; `wtk ∩ qtk = ∅` срещу „свидетелят винаги“ → **Р14-а (изваждане)**; G-A6а без зъби → **подписан ПОД + затворен списък причини**; G-A6б червен върху данните → **Р9-б (втора степен + подписан списък изключения)**; ориентирът не стига до 205-те реда → **Р15 (структурно поле `o`)**; G-B5 извън среза → **`validateSearchPayload` вътре в среза + собствен гейт-ред**; корпусът без селектор и без freeze → **`address_corpus_build.py --freeze` + команда в §5.Д**.
Приложени мажори: противоречието §2 ↔ §4.1 за `inside_clear` → **една дефиниция в §2 + Р5**; класът „извън, но в лентата на един“ → **Р5-д + Р14-б**; фикстурите на G-B2/G-A2 ф1 → **блоб-четене, липсващ файл = червено, затворено топ-ниво, фикстура на топ ниво**; `stk` пренарежда груповия режим → **`otk`, извън `_areaVocab`**; гардът от наблюдавани `qtk` → **речник от `quarter_names`**; §0.10 ↔ §5.Г → **изравнени (Б3 се комитва пръв)**; G-B1 → **Р18 (собствен пробен файл) + истински родител**. Минорите за качеството на ориентира (Р11-б), фантомния М0.1, `git push` и регистрите по display_id пътя — също приложени.

**Опровергател „semantics“ — присъда НЕГОДНО.** 5 блокера, 8 мажора, 3 минора.
Приложени: флагманът (дублира gates) → същият Р5/G-A3-г; „Р5в е мъртъв при раждане“ → **преписан Р5**; **вторият дисплей път пак показва противоречивата дума (2 775 реда) → нов Р12-б с материализация и измерена цена** — това беше най-скъпата пропусната пробойна на v1; G-A4 без зъби (публикационният гейт не чете полигони) → **полигонният вход влиза в гейта + ф6**; G-A6б неизпълним → Р9-б.
Мажори: собствената улица не се извлича за 82,5 % (`STREET_TYPE_RE:39`, `extractStreet:106-126` — проверено) → **Р10 с две дефиниции и подравнен Р13**; `_areaVocab` 88 → ~600 → Р15; Р12 занижен размер → **Р12-в с подписан таван**; грешният район на Битоля → **Приморски**; ориентирът и 581-те реда → Р15; отношението към ADR 010 → **Р6-б (с корекция на формулировката, §11.2)**; свидетелят не е „кадастралната дума“, а 58 % OSM `nearest_point` (флагманът на 707 m) → **преименуван навсякъде + колона `source` в леджера**; G-B1 → Р18; `sw.js` промяната без ефект → **`sw.js` изобщо не се пипа**. Минори: М0.1, М0.3 (четири дефиниции), голите цифри в каноничните токени → **Р16** (проверено срещу 60-те имена).

**Опровергател „delivery“ — присъда НЕГОДНО.** 4 блокера, 9 мажора, 2 минора.
Приложени блокери: **лотът е забранен от ПРИЕТ ADR 006 D12 и разрешен само от НЕПОДПИСАН ADR 007, а v1 не искаше този подпис → нов Р0 + Р0-б (kill switch)** — това е най-тежката управленска пробойна на v1; PowerShell разваля байтовете (`>` → UTF-16LE) → **пин по OID, четене в Python**; `python -m gates.sign` без аргументи пада, а редът подпис→freeze→run_gates дава червена проверка 6 → **пренаписан §5.Д**; ориентирът убива C2 етикета (`TYPEWORDS:457-458` няма „do“; `resolveC2BlockLabel:617` е fail-closed; `entryTokenSet:481-487` чете `e`, не `o`) → **Р15: ориентирът напуска `label` изцяло**.
Мажори: подписваният низ ≠ низът на Р10 → **Р10 + Р13 подравнени**; базата зад Р11 е сгрешена → **М0.6 + СПИРАЙ**; `_areaVocab` флип → Р15 + фикстура (iv) в G-B4; 205-те реда → Р15; **`git add index.html` би внесъл хънковете на Б3 → §5.0 + STOP т. 14**; `sw.js` недосегаем → §0.12; Р12 занижен размер → Р12-в; G-B1 → Р18. Минори: М0.1; преименуването на опашката е ход на Б3 (проверено: `b3_g11.py:44` вече изброява `архив/АРХИВ_A_05.09.md`) → §5.Г.

**Общо:** приети 17 блокера (след сливане на дублиращите се), 23 мажора; отхвърлени/преформулирани 5 находки и 1 предложена поправка (§11); 6 числови разминавания са изпратени на М0 с изричен СПИРАЙ.

---

**Gate 1:** планът чака думата на Петър по **Р0–Р18** и по класа 🔴. Без подпис Изпълнителят не пише нито ред. Публикуването е негово.

 succeeded in 1063ms:
classes Counter({'inside': 2431, 'edge': 1738, 'overlap': 606, 'outside': 499})
{'pin': [43.22212, 27.9378], 'no': '11', 'old': 'кв. Чайка, бл. 11', 'witness': 'кв. Чайка', 'new_v1': 'район Приморски, бл. 11, до ул. студентска', 'new_v2': 'кв. Левски, бл. 11, до ул. студентска', 'cls': 'edge', 'poly': 'кв. Левски', 'edge_m': 59, 'band': 100, 'district': 'район Приморски', 'orient': 'до ул. студентска', 'orient_src': 'най-близка улица 52 m', 'vh': None, 'tk': ['studentska', 'bl', '11'], 'qtk': ['chaika']}
{'pin': [43.22212, 27.93779], 'no': '11', 'old': 'кв. Чайка, бл. 11', 'witness': 'кв. Чайка', 'new_v1': 'район Приморски, бл. 11, до ул. студентска, вх. А', 'new_v2': 'кв. Левски, бл. 11, до ул. студентска, вх. А', 'cls': 'edge', 'poly': 'кв. Левски', 'edge_m': 59, 'band': 100, 'district': 'район Приморски', 'orient': 'до ул. студентска', 'orient_src': 'най-близка улица 51 m', 'vh': 'А', 'tk': ['studentska', 'bl', '11', 'vh', 'a'], 'qtk': ['chaika']}

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$t=Get-Content -LiteralPath '"'index.html' -Encoding UTF8; "'$t[4835..4880]' in C:\git\Fire_Varna
 succeeded in 810ms:
  (function initAddressSearch() {
    const inputEl = document.getElementById('addrSearchInput');
    const resultsEl = document.getElementById('addrSearchResults');
    if (!inputEl || !resultsEl) return; // header markup missing -> no-op

    // ---- skeleton primitives (verbatim from app/modules/search/skeleton.js) ----
    function norm(s){return (''+(s||'')).toLowerCase().replace(/блок/g,'бл').replace(/вход/g,'вх').replace(/[.№,'"-]/g,' ').replace(/\s+/g,' ').trim();}
    function skel(w){w=w.toLowerCase();var C={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'};var o='';for(var i=0;i<w.length;i++){o+=(C[w[i]]!==undefined?C[w[i]]:w[i]);}return o.replace(/[yj]/g,'i').replace(/(\D)\1+/g,'$1');}
    function lev(a,b,cap){var la=a.length,lb=b.length;if(Math.abs(la-lb)>cap)return cap+1;var prev=[];for(var j=0;j<=lb;j++)prev[j]=j;for(var i=1;i<=la;i++){var cur=[i],best=i;for(var j=1;j<=lb;j++){var v=Math.min(prev[j]+1,cur[j-1]+1,prev[j-1]+(a[i-1]===b[j-1]?0:1));cur[j]=v;if(v<best)best=v;}if(best>cap)return cap+1;prev=cur;}return prev[lb];}
    // ADR 032 A2 per-(query token) match-KIND classifier (verbatim from
    // searchLogic.js): 3 exact / 2 prefix / 1 within-cap fuzzy. The geocoder route
    // ranks on match KIND, so a binary matchSet is insufficient.
    function matchKindSet(qt, VOCAB){var s={},cap=qt.length>=7?2:1;for(var i=0;i<VOCAB.length;i++){var v=VOCAB[i],k=0;if(v===qt)k=3;else if(qt.length<=1)k=0;else if(v.indexOf(qt)===0)k=2;else if(qt.length<=3)k=0;else if(lev(qt,v,cap)<=cap)k=1;if(k)s[v]=k;}return s;}

    // ---- display payload (address_rows.json) + label resolution ----------------
    // The matcher index carries NO display string for the 48k entries with no
    // addr_key; their text is the source row's normalized_address, looked up by the
    // hit's display_id in the SEPARATE address_rows.json. These closure vars are set
    // by ensureSearchData() after both payloads load.
    let addressRows = null;   // array of [normalized_address, lat, lng] by row id
    let addrFieldIdx = null;  // { normalized_address, lat, lng } column indices
    let districtNames = [];   // район display-enum table (search_index.district_names)

    // Schema-driven address-row layout (M1 plan: never hardcode a column). Derive
    // each needed field position from the payload's field_order.
    function buildAddressFieldIndex(payload){
      const order = payload && Array.isArray(payload.field_order) ? payload.field_order : null;
      if (!order) throw new Error('address_rows.json missing field_order');
      const idx = {};
      ['normalized_address', 'lat', 'lng'].forEach(function (name) {
        const i = order.indexOf(name);
        if (i === -1) throw new Error('address_rows.json field_order missing "' + name + '"');
        idx[name] = i;
      });
      return idx;
    }

    // formatAddressHit — label resolution chain (privacy-safe):
    //   (1) the public geocoder `label` (= cleaned addr_key) when present;
    //   (2) else addressRows[display_id].normalized_address (the separate display
    //       payload, indexed by the source row id);
    //   (3) else the район name; NEVER a cadnum / section / complex id (the index
    //       carries none). An entrance (kind:"mf" + en) appends " · вх. <en>" to its
    //       parent building's resolved address.
    function prettyKey(s){ return String(s).replace(/\|/g, ' ').replace(/\s+/g, ' ').trim(); }
    function baseAddressLabel(hit){

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'

const fs=require('fs'),vm=require('vm'),cp=require('child_process');
const html=fs.readFileSync('index.html','utf8'),head=cp.execFileSync('git',['show','f745349:index.html'],{encoding:'utf8'});
function slice(h){let a=h.indexOf('    function norm(s)',h.indexOf('(function initAddressSearch'));let b=h.indexOf('    // ---- display payload',a);let c=h.indexOf('    const SEARCH_LIMIT = 8',b);let d=h.indexOf('    // ---- lazy load + cache',c);return h.slice(a,b)+h.slice(c,d);}
let original=slice(html); console.log('matcher_equals_HEAD',original.replace(/\\r/g,'')===slice(head).replace(/\\r/g,''));
let source=original.replace('      const out = ranked.slice','      trace = {ranked,blockTyped,blockHeader};\\n      const out = ranked.slice');
function engine(s){let ctx={trace:null};vm.createContext(ctx);vm.runInContext(s+'\\nthis.api={norm,skel,prepareIndex,runGeocoderSearch};',ctx);return ctx;}
const base=JSON.parse(fs.readFileSync('data/search_index.json','utf8')),rows=JSON.parse(fs.readFileSync('data/address_rows.json','utf8')).rows,preview=JSON.parse(fs.readFileSync('scratch/boundary_gallery/granitsi_preview_05.09/adresi_proposal_08.09.json','utf8')).entries;
const old=engine(source);old.api.prepareIndex(base);
const qs=['чайка студентска бл 11','бл 11 левски','бл 11 чайка','студентска бл 11'];
function compact(ctx,q,idx){let out=ctx.api.runGeocoderSearch(q,idx),t=ctx.trace; return {query:q,blockTyped:t.blockTyped,header:out.blockHeader,full:t.ranked.filter(s=>s.all).length,top:out.map(e=>({text:e._p?.new_v2||e.label||rows[e.display_id]?.[0],pin:e.pin,g:e.g,all:e.allTokens})),flagship:t.ranked.filter(s=>s.e.g==='b6797e83ec13fe798').map(s=>({rank:t.ranked.indexOf(s)+1,all:s.all,wdem:s.wdem,core:s.matchedCore,q:s.e.q,qtk:s.e.qtk,wtk:s.e.wtk}))};}
console.log('BASELINE_FULL',JSON.stringify(qs.map(q=>compact(old,q,base))));
const dict=new Map();for(let i=0;i<base.entries.length;i++){let e=base.entries[i],k=JSON.stringify([e.pin,e.label,e.en??null]);if("'!dict.has(k))dict.set(k,[]);dict.get(k).push(e);}
let unmatched=0,entries=[];
for(let p of preview){let bucket=dict.get(JSON.stringify([p.pin,p.old,p.vh??null])),e=bucket?.[0];if(!e){unmatched++;continue;} e=JSON.parse(JSON.stringify(e));e._p=p;entries.push(e);}
console.log('"'proposal_join',entries.length,unmatched);
let names=[...new Set(preview.filter(p=>['edge','inside'].includes(p.cls)).map(p=>p.poly))].sort();
function toks(s){return old.api.norm(s.replace(/"'^(?:кв'"\\.|ж\\.к\\.|к\\.к\\.|м\\.|местност)\\s*/i,'')).split(' ').map(old.api.skel).filter(t=>t.length>2&&"'!/''^'"\\d+"'$/.test(t));}
for(let e of entries){let p=e._p;let canon=['"'edge','inside'].includes(p.cls);let qtk=canon?toks(p.poly):[];e.wtk=(e.qtk||[]).filter(t=>"'!qtk.includes(t));e.qtk=qtk;if(canon)e.q=names.indexOf(p.poly);e.otk=toks((p.orient||'"'').replace(/"'^до'"\\s+(?:ул\\.\\s*)?/i,'')).filter(t=>"'!(e.tk||[]).includes(t));}
let updated=source
.replace("if (e.qtk) toks = toks.concat(e.qtk);","if (e.qtk) toks = toks.concat(e.qtk); if(e.wtk)toks=toks.concat(e.wtk); if(e.otk)toks=toks.concat(e.otk);")
.replace("['"'tk','qtk','alias_tk','dtk','stk']\",\"['tk','qtk','alias_tk','dtk','stk','wtk','otk']\")
.replace('index._areaVocab = av;','index._areaVocab = av; index._signedQuarterVocab = new Set((index.quarter_names||[]).flatMap(quarterToks));')
.replace('matchedViaStk = 0;','matchedViaStk = 0, matchedViaWitness=0, matchedViaOtkOnly=0;')
.replace(\"          if (best === 0) { all = false; continue; }\",
\"          if (e.wtk && best<3 && "'!(index._signedQuarterVocab.has(toks[qi]) && e.q!=null)){for(const t of e.wtk){const k=m[t]||0;if(k>best){best=k;matchedViaWitness++;if(best===3)break;}}}'"\\n\"+
\"          if (e.otk && best<3){for(const t of e.otk){const k=m[t]||0;if(k>best){best=k;matchedViaOtkOnly++;if(best===3)break;}}}\\n\"+
\"          if (best === 0) { all = false; continue; }\")
.replace('scored.push({ e: e,','scored.push({ e: e, matchedCore, wdem: matchedViaWitness>0 && matchedCore===0?1:0, otdem:matchedViaOtkOnly>0?1:0,')
.replace('        if (a.odem "'!== b.odem)'"', '        if (a.wdem "'!== b.wdem) return a.wdem-b.wdem; if(a.otdem!==b.otdem)return a.otdem-b.otdem;'"\\n        if (a.odem "'!== b.odem)'"');
let ctx={trace:null,quarterToks:toks};vm.createContext(ctx);vm.runInContext(updated+'\\nthis.api={norm,skel,prepareIndex,runGeocoderSearch};',ctx);
let candidate={entries,quarter_names:names};ctx.api.prepareIndex(candidate);
console.log('SIM_V2_PREVIEW_SCOPE',JSON.stringify([...qs,'чаика студентска бл 11','чай студентска бл 11','бл 11 цветен'].map(q=>compact(ctx,q,candidate))));

'@ | node -" in C:\git\Fire_Varna
 exited 1 in 551ms:
[stdin]:18
function toks(s){return old.api.norm(s.replace(/^(?:??\.|?\.?\.|?\.?\.|?\.|????????)\s*/i,'')).split(' ').map(old.api.skel).filter(t=>t.length>2&&!/^\d+$/.test(t));}
                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SyntaxError: Invalid regular expression: /^(?:??\.|?\.?\.|?\.?\.|?\.|????????)\s*/i: Nothing to repeat
    at makeContextifyScript (node:internal/vm:185:14)
    at compileScript (node:internal/process/execution:383:10)
    at evalTypeScript (node:internal/process/execution:266:24)
    at node:internal/main/eval_stdin:53:5
    at Socket.<anonymous> (node:internal/process/execution:201:5)
    at Socket.emit (node:events:531:35)
    at endReadableNT (node:internal/streams/readable:1698:12)
    at process.processTicksAndRejections (node:internal/process/task_queues:90:21)

Node.js v22.19.0

codex
Открихме два съществени пропуска: предложеното демотиране на свидетеля се изключва, щом „бл“ или номерът съвпаднат; стари квартални думи има и в основните `tk` токени, които гардът не проверява. Пробата също съдържа ориентири като „до жк младост 1“ — затова броим различимостта отново след филтъра за допустими улици.

2026-09-07T22:32:22.978474Z ERROR codex_models_manager::manager: failed to refresh available models: timeout waiting for child process to exit
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [System.Text.UTF8Encoding]::new()
@'"'

const fs=require('fs'),vm=require('vm'),cp=require('child_process');
const html=fs.readFileSync('index.html','utf8'),head=cp.execFileSync('git',['show','f745349:index.html'],{encoding:'utf8'});
function slice(h){let a=h.indexOf('    function norm(s)',h.indexOf('(function initAddressSearch'));let b=h.indexOf('    // ---- display payload',a);let c=h.indexOf('    const SEARCH_LIMIT = 8',b);let d=h.indexOf('    // ---- lazy load + cache',c);return h.slice(a,b)+h.slice(c,d);}
let original=slice(html); console.log('matcher_equals_HEAD',original.replace(/\\r/g,'')===slice(head).replace(/\\r/g,''));
let source=original.replace('      const out = ranked.slice','      trace = {ranked,blockTyped,blockHeader};\\n      const out = ranked.slice');
function engine(s){let ctx={trace:null};vm.createContext(ctx);vm.runInContext(s+'\\nthis.api={norm,skel,prepareIndex,runGeocoderSearch};',ctx);return ctx;}
const base=JSON.parse(fs.readFileSync('data/search_index.json','utf8')),rows=JSON.parse(fs.readFileSync('data/address_rows.json','utf8')).rows,preview=JSON.parse(fs.readFileSync('scratch/boundary_gallery/granitsi_preview_05.09/adresi_proposal_08.09.json','utf8')).entries;
const old=engine(source);old.api.prepareIndex(base);
const qs=['чайка студентска бл 11','бл 11 левски','бл 11 чайка','студентска бл 11'];
function compact(ctx,q,idx){let out=ctx.api.runGeocoderSearch(q,idx),t=ctx.trace; return {query:q,blockTyped:t.blockTyped,header:out.blockHeader,full:t.ranked.filter(s=>s.all).length,top:out.map(e=>({text:e._p?.new_v2||e.label||rows[e.display_id]?.[0],pin:e.pin,g:e.g,all:e.allTokens})),flagship:t.ranked.filter(s=>s.e.g==='b6797e83ec13fe798').map(s=>({rank:t.ranked.indexOf(s)+1,all:s.all,wdem:s.wdem,core:s.matchedCore,q:s.e.q,qtk:s.e.qtk,wtk:s.e.wtk}))};}
console.log('BASELINE_FULL',JSON.stringify(qs.map(q=>compact(old,q,base))));
const dict=new Map();for(let i=0;i<base.entries.length;i++){let e=base.entries[i],k=JSON.stringify([e.pin,e.label,e.en??null]);if("'!dict.has(k))dict.set(k,[]);dict.get(k).push(e);}
let unmatched=0,entries=[];
for(let p of preview){let bucket=dict.get(JSON.stringify([p.pin,p.old,p.vh??null])),e=bucket?.[0];if(!e){unmatched++;continue;} e=JSON.parse(JSON.stringify(e));e._p=p;entries.push(e);}
console.log('"'proposal_join',entries.length,unmatched);
let names=[...new Set(preview.filter(p=>['edge','inside'].includes(p.cls)).map(p=>p.poly))].sort();
function toks(s){return old.api.norm(s.replace(/"'^(?:кв'"\\.|ж\\.к\\.|к\\.к\\.|м\\.|местност)\\s*/i,'')).split(' ').map(old.api.skel).filter(t=>t.length>2&&"'!/''^'"\\d+"'$/.test(t));}
for(let e of entries){let p=e._p;let canon=['"'edge','inside'].includes(p.cls);let qtk=canon?toks(p.poly):[];e.wtk=(e.qtk||[]).filter(t=>"'!qtk.includes(t));e.qtk=qtk;if(canon)e.q=names.indexOf(p.poly);e.otk=toks((p.orient||'"'').replace(/"'^до'"\\s+(?:ул\\.\\s*)?/i,'')).filter(t=>"'!(e.tk||[]).includes(t));}
let updated=source
.replace("if (e.qtk) toks = toks.concat(e.qtk);","if (e.qtk) toks = toks.concat(e.qtk); if(e.wtk)toks=toks.concat(e.wtk); if(e.otk)toks=toks.concat(e.otk);")
.replace("['"'tk','qtk','alias_tk','dtk','stk']\",\"['tk','qtk','alias_tk','dtk','stk','wtk','otk']\")
.replace('index._areaVocab = av;','index._areaVocab = av; index._signedQuarterVocab = new Set((index.quarter_names||[]).flatMap(quarterToks));')
.replace('matchedViaStk = 0;','matchedViaStk = 0, matchedViaWitness=0, matchedViaOtkOnly=0;')
.replace(\"          if (best === 0) { all = false; continue; }\",
\"          if (e.wtk && best<3 && "'!(index._signedQuarterVocab.has(toks[qi]) && e.q!=null)){for(const t of e.wtk){const k=m[t]||0;if(k>best){best=k;matchedViaWitness++;if(best===3)break;}}}'"\\n\"+
\"          if (e.otk && best<3){for(const t of e.otk){const k=m[t]||0;if(k>best){best=k;matchedViaOtkOnly++;if(best===3)break;}}}\\n\"+
\"          if (best === 0) { all = false; continue; }\")
.replace('scored.push({ e: e,','scored.push({ e: e, matchedCore, wdem: matchedViaWitness>0 && matchedCore===0?1:0, otdem:matchedViaOtkOnly>0?1:0,')
.replace('        if (a.odem "'!== b.odem)'"', '        if (a.wdem "'!== b.wdem) return a.wdem-b.wdem; if(a.otdem!==b.otdem)return a.otdem-b.otdem;'"\\n        if (a.odem "'!== b.odem)'"');
let ctx={trace:null,quarterToks:toks};vm.createContext(ctx);vm.runInContext(updated+'\\nthis.api={norm,skel,prepareIndex,runGeocoderSearch};',ctx);
let candidate={entries,quarter_names:names};ctx.api.prepareIndex(candidate);
console.log('SIM_V2_PREVIEW_SCOPE',JSON.stringify([...qs,'чаика студентска бл 11','чай студентска бл 11','бл 11 цветен'].map(q=>compact(ctx,q,candidate))));

'@ | node -" in C:\git\Fire_Varna
 succeeded in 1054ms:
matcher_equals_HEAD true
BASELINE_FULL [{"query":"чайка студентска бл 11","blockTyped":true,"header":{"block":"11","count":1,"district_enum":4},"full":1,"top":[{"text":"кв. Чайка, бл. 11","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":true},{"text":"кв. Чайка, бл. 12","pin":[43.22169,27.93735],"g":"bfc13610787b1d2de","all":false},{"text":"кв. Чайка, бл. 13","pin":[43.22127,27.93691],"g":"bf71303b13d244260","all":false},{"text":"кв. Чайка, бл. 14","pin":[43.22228,27.93573],"g":"beec83b13d70c8ce8","all":false},{"text":"кв. Чайка, бл. 11","pin":[43.21487,27.93338],"g":"b613967ebcc8f1438","all":false},{"text":"кв чайка бл 11","pin":[43.21465,27.93392],"all":false},{"text":"dobri voinikov|11","pin":[43.21209,27.9283],"g":"bdc93818958826c65","all":false},{"text":"d r basanovich|11","pin":[43.21678,27.92964],"g":"bb9054d64de9c88fd","all":false}],"flagship":[{"rank":1,"all":true,"qtk":["chaika"]}]},{"query":"бл 11 левски","blockTyped":true,"header":{"block":"11","count":3,"district_enum":4},"full":29,"top":[{"text":"кв. Левски, бл. 11, бул. Васил Левски","pin":[43.22017,27.92848],"g":"b620d9a87b225989d","all":true},{"text":"кв. Левски, бл. 11, бул. Царевец","pin":[43.21976,27.91949],"g":"b79191957abcb5ea2","all":true},{"text":"кв. Левски, бл. 11","pin":[43.22513,27.92315],"g":"bba00138230d589b0","all":true},{"text":"batova|11","pin":[43.22298,27.91935],"g":"b6b0623ec48de51d9","all":true},{"text":"elitsa|11","pin":[43.22214,27.93095],"g":"b23434aa2e14f14bf","all":true},{"text":"roshtok|11","pin":[43.22205,27.93009],"g":"b9fb39b7712d03419","all":true},{"text":"бул царевец 11","pin":[43.21973,27.9192],"g":"b48c0dad360ae2207","all":true},{"text":"evlogi georgiev|11","pin":[43.22171,27.92059],"g":"b28b80f7d080645de","all":true}],"flagship":[{"rank":708,"all":false,"qtk":["chaika"]}]},{"query":"бл 11 чайка","blockTyped":true,"header":{"block":"11","count":2,"district_enum":4},"full":18,"top":[{"text":"кв. Чайка, бл. 11","pin":[43.21487,27.93338],"g":"b613967ebcc8f1438","all":true},{"text":"кв. Чайка, бл. 11","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":true},{"text":"кв чайка бл 11","pin":[43.21465,27.93392],"all":true},{"text":"dobri voinikov|11","pin":[43.21209,27.9283],"g":"bdc93818958826c65","all":true},{"text":"d r basanovich|11","pin":[43.21678,27.92964],"g":"bb9054d64de9c88fd","all":true},{"text":"feliks kanits|11","pin":[43.21196,27.92836],"g":"b13e8431c6b605157","all":true},{"text":"tsani ginchev|11","pin":[43.21207,27.9267],"g":"b85fa79757be121c8","all":true},{"text":"vasil kanchev|11","pin":[43.21307,27.92699],"g":"bb3f6cff9397656e5","all":true}],"flagship":[{"rank":2,"all":true,"qtk":["chaika"]}]},{"query":"студентска бл 11","blockTyped":false,"full":2,"top":[{"text":"кв. Чайка, бл. 11","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":true},{"text":"кв. Чайка, бл. 11","pin":[43.22212,27.93779],"g":"b6797e83ec13fe798","all":true},{"text":"студентска бл 14","pin":[43.22189,27.93642],"all":false},{"text":"студентска бл 14","pin":[43.22239,27.93454],"all":false},{"text":"studentska|1","pin":[43.2243,27.9305],"g":"ba14b5ab8f1e92f3f","all":false},{"text":"studentska|6","pin":[43.22434,27.92617],"g":"b6b3773104db4840a","all":false},{"text":"кв. Левски, бл. 7","pin":[43.22472,27.92567],"g":"bf3a06a54b63d090e","all":false},{"text":"кв. Чайка, бл. 12","pin":[43.22169,27.93735],"g":"bfc13610787b1d2de","all":false}],"flagship":[{"rank":1,"all":true,"qtk":["chaika"]},{"rank":2,"all":true,"qtk":["chaika"]}]}]
proposal_join 4783 491
SIM_V2_PREVIEW_SCOPE [{"query":"чайка студентска бл 11","blockTyped":true,"full":0,"top":[{"text":"кв. Чайка, бл. 11","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":false},{"text":"кв. Чайка, бл. 11","pin":[43.21487,27.93338],"g":"b613967ebcc8f1438","all":false},{"text":"кв. Чайка, бл. 118","pin":[43.21372,27.92639],"g":"b298ae2163521522a","all":false},{"text":"кв. Чайка, бл. 40","pin":[43.21097,27.92883],"g":"b99fdda4194c0b482","all":false},{"text":"кв. Чайка, бл. 24","pin":[43.21343,27.92943],"g":"bdd2debac5bd3adeb","all":false},{"text":"кв. Чайка, бл. 25","pin":[43.2129,27.9298],"g":"b64b4edeab0ccc458","all":false},{"text":"кв. Чайка, бл. 26","pin":[43.2124,27.93015],"g":"bd445b3e25e70efd3","all":false},{"text":"кв. Чайка, бл. 208","pin":[43.21693,27.94499],"g":"b6180b66169c56908","all":false}],"flagship":[{"rank":1,"all":false,"wdem":0,"core":3,"q":22,"qtk":["levski"],"wtk":["chaika"]}]},{"query":"бл 11 левски","blockTyped":true,"header":{"block":"11","count":5,"district_enum":4},"full":6,"top":[{"text":"кв. Левски, бл. 11, бул. Царевец","pin":[43.21976,27.91949],"g":"b79191957abcb5ea2","all":true},{"text":"Цветен квартал, бл. 11","pin":[43.22615,27.91075],"g":"b77bcb56eec95837e","all":true},{"text":"кв. Чайка, бл. 11","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":true},{"text":"кв. Левски, бл. 11, бул. Васил Левски","pin":[43.22017,27.92848],"g":"b620d9a87b225989d","all":true},{"text":"кв. Левски, бл. 11","pin":[43.22513,27.92315],"g":"bba00138230d589b0","all":true},{"text":"кв. Левски, бл. 31","pin":[43.22327,27.91994],"g":"b60e750c9d551ce54","all":true},{"text":"кв. Левски, бл. 3","pin":[43.21797,27.92045],"g":"bc259f641b7198204","all":false},{"text":"кв. Левски, бл. 2","pin":[43.21719,27.92262],"g":"be05e1f9b924eaffa","all":false}],"flagship":[{"rank":3,"all":true,"wdem":0,"core":2,"q":22,"qtk":["levski"],"wtk":["chaika"]}]},{"query":"бл 11 чайка","blockTyped":true,"header":{"block":"11","count":1,"district_enum":4},"full":2,"top":[{"text":"кв. Чайка, бл. 11","pin":[43.21487,27.93338],"g":"b613967ebcc8f1438","all":true},{"text":"кв. Чайка, бл. 118","pin":[43.21372,27.92639],"g":"b298ae2163521522a","all":true},{"text":"кв. Чайка, бл. 40","pin":[43.21097,27.92883],"g":"b99fdda4194c0b482","all":false},{"text":"кв. Чайка, бл. 24","pin":[43.21343,27.92943],"g":"bdd2debac5bd3adeb","all":false},{"text":"кв. Чайка, бл. 25","pin":[43.2129,27.9298],"g":"b64b4edeab0ccc458","all":false},{"text":"кв. Чайка, бл. 26","pin":[43.2124,27.93015],"g":"bd445b3e25e70efd3","all":false},{"text":"кв. Чайка, бл. 208","pin":[43.21693,27.94499],"g":"b6180b66169c56908","all":false},{"text":"кв. Чайка, бл. 197","pin":[43.21758,27.93431],"g":"bcc432fa5b758b73e","all":false}],"flagship":[{"rank":121,"all":false,"wdem":0,"core":2,"q":22,"qtk":["levski"],"wtk":["chaika"]}]},{"query":"студентска бл 11","blockTyped":false,"full":2,"top":[{"text":"кв. Чайка, бл. 11","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":true},{"text":"кв. Чайка, бл. 11","pin":[43.22212,27.93779],"g":"b6797e83ec13fe798","all":true},{"text":"кв. Левски, бл. 7","pin":[43.22472,27.92567],"g":"bf3a06a54b63d090e","all":false},{"text":"кв. Чайка, бл. 12","pin":[43.22169,27.93735],"g":"bfc13610787b1d2de","all":false},{"text":"кв. Чайка, бл. 13","pin":[43.22127,27.93691],"g":"bf71303b13d244260","all":false},{"text":"кв. Чайка, бл. 14","pin":[43.22228,27.93573],"g":"beec83b13d70c8ce8","all":false},{"text":"кв. Левски, бл. 3","pin":[43.22345,27.93083],"g":"b21c23d397612d97a","all":false},{"text":"кв. Левски, бл. 3","pin":[43.22364,27.93024],"g":"b21c23d397612d97a","all":false}],"flagship":[{"rank":1,"all":true,"wdem":0,"core":3,"q":22,"qtk":["levski"],"wtk":["chaika"]},{"rank":2,"all":true,"wdem":0,"core":3,"q":22,"qtk":["levski"],"wtk":["chaika"]}]},{"query":"чаика студентска бл 11","blockTyped":true,"full":0,"top":[{"text":"кв. Чайка, бл. 11","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":false},{"text":"кв. Чайка, бл. 11","pin":[43.21487,27.93338],"g":"b613967ebcc8f1438","all":false},{"text":"кв. Чайка, бл. 118","pin":[43.21372,27.92639],"g":"b298ae2163521522a","all":false},{"text":"кв. Чайка, бл. 40","pin":[43.21097,27.92883],"g":"b99fdda4194c0b482","all":false},{"text":"кв. Чайка, бл. 24","pin":[43.21343,27.92943],"g":"bdd2debac5bd3adeb","all":false},{"text":"кв. Чайка, бл. 25","pin":[43.2129,27.9298],"g":"b64b4edeab0ccc458","all":false},{"text":"кв. Чайка, бл. 26","pin":[43.2124,27.93015],"g":"bd445b3e25e70efd3","all":false},{"text":"кв. Чайка, бл. 208","pin":[43.21693,27.94499],"g":"b6180b66169c56908","all":false}],"flagship":[{"rank":1,"all":false,"wdem":0,"core":3,"q":22,"qtk":["levski"],"wtk":["chaika"]}]},{"query":"чай студентска бл 11","blockTyped":false,"full":2,"top":[{"text":"кв. Чайка, бл. 11","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":true},{"text":"кв. Чайка, бл. 11","pin":[43.22212,27.93779],"g":"b6797e83ec13fe798","all":true},{"text":"кв. Чайка, бл. 12","pin":[43.22169,27.93735],"g":"bfc13610787b1d2de","all":false},{"text":"кв. Чайка, бл. 13","pin":[43.22127,27.93691],"g":"bf71303b13d244260","all":false},{"text":"кв. Чайка, бл. 14","pin":[43.22228,27.93573],"g":"beec83b13d70c8ce8","all":false},{"text":"кв. Чайка, бл. 12","pin":[43.22173,27.93742],"g":"bfc13610787b1d2de","all":false},{"text":"кв. Чайка, бл. 13","pin":[43.22129,27.93692],"g":"bf71303b13d244260","all":false},{"text":"кв. Чайка, бл. 14","pin":[43.22223,27.93687],"g":"beec83b13d70c8ce8","all":false}],"flagship":[{"rank":1,"all":true,"wdem":0,"core":3,"q":22,"qtk":["levski"],"wtk":["chaika"]},{"rank":2,"all":true,"wdem":0,"core":3,"q":22,"qtk":["levski"],"wtk":["chaika"]}]},{"query":"бл 11 цветен","blockTyped":false,"full":3,"top":[{"text":"Цветен квартал, бл. 11","pin":[43.22615,27.91075],"g":"b77bcb56eec95837e","all":true},{"text":"Цветен квартал, бл. 11","pin":[43.22614,27.91075],"g":"b77bcb56eec95837e","all":true},{"text":"Цветен квартал, бл. 2","pin":[43.21789,27.91043],"g":"bd145856c26414be3","all":true},{"text":"Цветен квартал, бл. 1","pin":[43.21738,27.91607],"g":"b1be5e90ca330036f","all":false},{"text":"Цветен квартал, бл. 1","pin":[43.21687,27.91134],"g":"b536fb333a2fc1de2","all":false},{"text":"Цветен квартал, бл. 1","pin":[43.21687,27.91134],"g":"b536fb333a2fc1de2","all":false},{"text":"Цветен квартал, бл. 1","pin":[43.21702,27.91114],"g":"b536fb333a2fc1de2","all":false},{"text":"Цветен квартал, бл. 1","pin":[43.21713,27.91094],"g":"b536fb333a2fc1de2","all":false}],"flagship":[{"rank":201,"all":false,"wdem":0,"core":2,"q":22,"qtk":["levski"],"wtk":["chaika"]},{"rank":243,"all":false,"wdem":0,"core":2,"q":22,"qtk":["levski"],"wtk":["chaika"]}]}]

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [System.Text.UTF8Encoding]::new()
@'"'

const fs=require('fs'),vm=require('vm'),cp=require('child_process');
const html=fs.readFileSync('index.html','utf8'),head=cp.execFileSync('git',['show','f745349:index.html'],{encoding:'utf8'});
function slice(h){let a=h.indexOf('    function norm(s)',h.indexOf('(function initAddressSearch'));let b=h.indexOf('    // ---- display payload',a);let c=h.indexOf('    const SEARCH_LIMIT = 8',b);let d=h.indexOf('    // ---- lazy load + cache',c);return h.slice(a,b)+h.slice(c,d);}
let original=slice(html); console.log('matcher_equals_HEAD',original.replace(/\\r/g,'')===slice(head).replace(/\\r/g,''));
let source=original.replace('      const out = ranked.slice','      trace = {ranked,blockTyped,blockHeader};\\n      const out = ranked.slice');
function engine(s){let ctx={trace:null};vm.createContext(ctx);vm.runInContext(s+'\\nthis.api={norm,skel,prepareIndex,runGeocoderSearch};',ctx);return ctx;}
const base=JSON.parse(fs.readFileSync('data/search_index.json','utf8')),rows=JSON.parse(fs.readFileSync('data/address_rows.json','utf8')).rows,preview=JSON.parse(fs.readFileSync('scratch/boundary_gallery/granitsi_preview_05.09/adresi_proposal_08.09.json','utf8')).entries;
const old=engine(source);old.api.prepareIndex(base);
const qs=['чайка студентска бл 11','бл 11 левски','бл 11 чайка','студентска бл 11'];
function compact(ctx,q,idx){let out=ctx.api.runGeocoderSearch(q,idx),t=ctx.trace; return {query:q,blockTyped:t.blockTyped,header:out.blockHeader,full:t.ranked.filter(s=>s.all).length,top:t.ranked.slice(0,8).map(s=>({text:s.e._p?.new_v2||s.e.label||rows[s.e.display_id]?.[0],pin:s.e.pin,g:s.e.g,all:s.all,wdem:s.wdem,q:s.e.q,len:(s.e.tk||[]).length+(s.e.qtk||[]).length})),flagship:t.ranked.filter(s=>s.e.g==='b6797e83ec13fe798').map(s=>({rank:t.ranked.indexOf(s)+1,all:s.all,wdem:s.wdem,core:s.matchedCore,q:s.e.q,qtk:s.e.qtk,wtk:s.e.wtk}))};}

const dict=new Map();for(let i=0;i<base.entries.length;i++){let e=base.entries[i],k=JSON.stringify([e.pin,e.tk]);if("'!dict.has(k))dict.set(k,[]);dict.get(k).push(e);}
let unmatched=0,entries=[];
for(let p of preview){let bucket=dict.get(JSON.stringify([p.pin,p.tk])),e=bucket?.[0];if(!e){unmatched++;continue;} e=JSON.parse(JSON.stringify(e));e._p=p;entries.push(e);}
console.log('"'proposal_join',entries.length,unmatched);
let names=[...new Set(preview.filter(p=>['edge','inside'].includes(p.cls)).map(p=>p.poly))].sort();
function toks(s){return old.api.norm(s.replace(/"'^(?:кв'"\\.|ж\\.к\\.|к\\.к\\.|м\\.|местност)\\s*/i,'')).split(' ').map(old.api.skel).filter(t=>t.length>2&&"'!/''^'"\\d+"'$/.test(t));}
for(let e of entries){let p=e._p;let canon=['"'edge','inside'].includes(p.cls);let qtk=canon?toks(p.poly):[];e.wtk=(e.qtk||[]).filter(t=>"'!qtk.includes(t));e.qtk=qtk;if(canon)e.q=names.indexOf(p.poly);e.otk=toks((p.orient||'"'').replace(/"'^до'"\\s+(?:ул\\.\\s*)?/i,'')).filter(t=>"'!(e.tk||[]).includes(t));}
let updated=source
.replace("if (e.qtk) toks = toks.concat(e.qtk);","if (e.qtk) toks = toks.concat(e.qtk); if(e.wtk)toks=toks.concat(e.wtk); if(e.otk)toks=toks.concat(e.otk);")
.replace("['"'tk','qtk','alias_tk','dtk','stk']\",\"['tk','qtk','alias_tk','dtk','stk','wtk','otk']\")
.replace('index._areaVocab = av;','index._areaVocab = av; index._signedQuarterVocab = new Set((index.quarter_names||[]).flatMap(quarterToks));')
.replace('matchedViaStk = 0;','matchedViaStk = 0, matchedViaWitness=0, matchedViaOtkOnly=0;')
.replace(\"          if (best === 0) { all = false; continue; }\",
\"          if (e.wtk && best<3 && "'!(index._signedQuarterVocab.has(toks[qi]) && e.q!=null)){for(const t of e.wtk){const k=m[t]||0;if(k>best){best=k;matchedViaWitness++;if(best===3)break;}}}'"\\n\"+
\"          if (e.otk && best<3){for(const t of e.otk){const k=m[t]||0;if(k>best){best=k;matchedViaOtkOnly++;if(best===3)break;}}}\\n\"+
\"          if (best === 0) { all = false; continue; }\")
.replace('scored.push({ e: e,','scored.push({ e: e, matchedCore, wdem: matchedViaWitness>0 && matchedCore===0?1:0, otdem:matchedViaOtkOnly>0?1:0,')
.replace('        if (a.odem "'!== b.odem)'"', '        if (a.wdem "'!== b.wdem) return a.wdem-b.wdem; if(a.otdem!==b.otdem)return a.otdem-b.otdem;'"\\n        if (a.odem "'!== b.odem)'"');
let ctx={trace:null,quarterToks:toks};vm.createContext(ctx);vm.runInContext(updated+'\\nthis.api={norm,skel,prepareIndex,runGeocoderSearch};',ctx);
let candidate={entries,quarter_names:names};ctx.api.prepareIndex(candidate);
console.log('SIM_V2_PREVIEW_SCOPE',JSON.stringify([...qs,'чай студентска бл 11','бл 11 цветен'].map(q=>compact(ctx,q,candidate))));

'@ | node -" in C:\git\Fire_Varna
 succeeded in 932ms:
matcher_equals_HEAD true
proposal_join 5274 0
SIM_V2_PREVIEW_SCOPE [{"query":"чайка студентска бл 11","blockTyped":true,"full":0,"top":[{"text":"кв. Левски, бл. 11, до ул. студентска","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":false,"wdem":0,"q":22,"len":4},{"text":"кв. Чайка, бл. 11, до кв чайка","pin":[43.21487,27.93338],"g":"b613967ebcc8f1438","all":false,"wdem":0,"q":27,"len":5},{"text":"район Приморски, бл. 4, до бул. 8 ми приморски полк","pin":[43.21372,27.92639],"g":"b298ae2163521522a","all":false,"wdem":0,"len":8},{"text":"район Приморски, бл. 40, до васил друмев","pin":[43.21097,27.92883],"g":"b99fdda4194c0b482","all":false,"wdem":0,"len":4},{"text":"район Приморски, бл. 24, до морска сирена","pin":[43.21343,27.92943],"g":"bdd2debac5bd3adeb","all":false,"wdem":0,"len":4},{"text":"район Приморски, бл. 25, до морска сирена","pin":[43.2129,27.9298],"g":"b64b4edeab0ccc458","all":false,"wdem":0,"len":4},{"text":"район Приморски, бл. 26, до морска сирена","pin":[43.2124,27.93015],"g":"bd445b3e25e70efd3","all":false,"wdem":0,"len":4},{"text":"кв. Чайка, бл. 208, до рупи","pin":[43.21693,27.94499],"g":"b6180b66169c56908","all":false,"wdem":0,"q":27,"len":4}],"flagship":[{"rank":1,"all":false,"wdem":0,"core":3,"q":22,"qtk":["levski"],"wtk":["chaika"]}]},{"query":"бл 11 левски","blockTyped":true,"header":{"block":"11","count":5,"district_enum":4},"full":6,"top":[{"text":"район Приморски, бл. 11, бул. Царевец","pin":[43.21976,27.91949],"g":"b79191957abcb5ea2","all":true,"wdem":0,"len":4},{"text":"кв. Левски, бл. 11, до карамфил","pin":[43.22615,27.91075],"g":"b77bcb56eec95837e","all":true,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 11, до ул. студентска","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":true,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 11, бул. Васил Левски","pin":[43.22017,27.92848],"g":"b620d9a87b225989d","all":true,"wdem":0,"q":22,"len":6},{"text":"кв. Левски, бл. 11, до доктор иван басанович","pin":[43.22513,27.92315],"g":"bba00138230d589b0","all":true,"wdem":0,"q":22,"len":6},{"text":"кв. Левски, бл. 31, до емануил манолов","pin":[43.22327,27.91994],"g":"b60e750c9d551ce54","all":true,"wdem":0,"q":22,"len":6},{"text":"район Приморски, бл. 3, до баучер","pin":[43.21797,27.92045],"g":"bc259f641b7198204","all":false,"wdem":0,"len":3},{"text":"район Приморски, бл. 2, до баучер","pin":[43.21719,27.92262],"g":"be05e1f9b924eaffa","all":false,"wdem":0,"len":3}],"flagship":[{"rank":3,"all":true,"wdem":0,"core":2,"q":22,"qtk":["levski"],"wtk":["chaika"]}]},{"query":"бл 11 чайка","blockTyped":true,"header":{"block":"11","count":1,"district_enum":4},"full":2,"top":[{"text":"кв. Чайка, бл. 11, до кв чайка","pin":[43.21487,27.93338],"g":"b613967ebcc8f1438","all":true,"wdem":0,"q":27,"len":5},{"text":"район Приморски, бл. 4, до бул. 8 ми приморски полк","pin":[43.21372,27.92639],"g":"b298ae2163521522a","all":true,"wdem":0,"len":8},{"text":"район Приморски, бл. 40, до васил друмев","pin":[43.21097,27.92883],"g":"b99fdda4194c0b482","all":false,"wdem":0,"len":4},{"text":"район Приморски, бл. 24, до морска сирена","pin":[43.21343,27.92943],"g":"bdd2debac5bd3adeb","all":false,"wdem":0,"len":4},{"text":"район Приморски, бл. 25, до морска сирена","pin":[43.2129,27.9298],"g":"b64b4edeab0ccc458","all":false,"wdem":0,"len":4},{"text":"район Приморски, бл. 26, до морска сирена","pin":[43.2124,27.93015],"g":"bd445b3e25e70efd3","all":false,"wdem":0,"len":4},{"text":"кв. Чайка, бл. 208, до рупи","pin":[43.21693,27.94499],"g":"b6180b66169c56908","all":false,"wdem":0,"q":27,"len":4},{"text":"кв. Чайка, бл. 197, до чайка","pin":[43.21758,27.93431],"g":"bcc432fa5b758b73e","all":false,"wdem":0,"q":27,"len":4}],"flagship":[{"rank":121,"all":false,"wdem":0,"core":2,"q":22,"qtk":["levski"],"wtk":["chaika"]}]},{"query":"студентска бл 11","blockTyped":false,"full":2,"top":[{"text":"кв. Левски, бл. 11, до ул. студентска","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":true,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 11, до ул. студентска, вх. А","pin":[43.22212,27.93779],"g":"b6797e83ec13fe798","all":true,"wdem":0,"q":22,"len":6},{"text":"кв. Левски, бл. 7, до студентска","pin":[43.22472,27.92567],"g":"bf3a06a54b63d090e","all":false,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 12, до ул. студентска","pin":[43.22169,27.93735],"g":"bfc13610787b1d2de","all":false,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 13, до димитър икономов","pin":[43.22127,27.93691],"g":"bf71303b13d244260","all":false,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 14, до димитър икономов","pin":[43.22228,27.93573],"g":"beec83b13d70c8ce8","all":false,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 3, до ул. студентска","pin":[43.22345,27.93083],"g":"b21c23d397612d97a","all":false,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 3, до мир","pin":[43.22364,27.93024],"g":"b21c23d397612d97a","all":false,"wdem":0,"q":22,"len":4}],"flagship":[{"rank":1,"all":true,"wdem":0,"core":3,"q":22,"qtk":["levski"],"wtk":["chaika"]},{"rank":2,"all":true,"wdem":0,"core":3,"q":22,"qtk":["levski"],"wtk":["chaika"]}]},{"query":"чай студентска бл 11","blockTyped":false,"full":2,"top":[{"text":"кв. Левски, бл. 11, до ул. студентска","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":true,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 11, до ул. студентска, вх. А","pin":[43.22212,27.93779],"g":"b6797e83ec13fe798","all":true,"wdem":0,"q":22,"len":6},{"text":"кв. Левски, бл. 12, до ул. студентска","pin":[43.22169,27.93735],"g":"bfc13610787b1d2de","all":false,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 13, до димитър икономов","pin":[43.22127,27.93691],"g":"bf71303b13d244260","all":false,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 14, до димитър икономов","pin":[43.22228,27.93573],"g":"beec83b13d70c8ce8","all":false,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 12, до ул. студентска, вх. А","pin":[43.22173,27.93742],"g":"bfc13610787b1d2de","all":false,"wdem":0,"q":22,"len":6},{"text":"кв. Левски, бл. 13, до димитър икономов, вх. 1","pin":[43.22129,27.93692],"g":"bf71303b13d244260","all":false,"wdem":0,"q":22,"len":6},{"text":"кв. Левски, бл. 14, до ул. студентска, вх. А","pin":[43.22223,27.93687],"g":"beec83b13d70c8ce8","all":false,"wdem":0,"q":22,"len":6}],"flagship":[{"rank":1,"all":true,"wdem":0,"core":3,"q":22,"qtk":["levski"],"wtk":["chaika"]},{"rank":2,"all":true,"wdem":0,"core":3,"q":22,"qtk":["levski"],"wtk":["chaika"]}]},{"query":"бл 11 цветен","blockTyped":false,"full":3,"top":[{"text":"кв. Левски, бл. 11, до карамфил","pin":[43.22615,27.91075],"g":"b77bcb56eec95837e","all":true,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 11, до карамфил, вх. 1","pin":[43.22614,27.91075],"g":"b77bcb56eec95837e","all":true,"wdem":0,"q":22,"len":6},{"text":"район Приморски, бл. 2, до чавдар войвода, вх. 11","pin":[43.21789,27.91043],"g":"bd145856c26414be3","all":true,"wdem":0,"len":6},{"text":"район Приморски, бл. 1, до брегалница","pin":[43.21738,27.91607],"g":"b1be5e90ca330036f","all":false,"wdem":0,"len":3},{"text":"район Приморски, бл. 1, до прилеп","pin":[43.21687,27.91134],"g":"b536fb333a2fc1de2","all":false,"wdem":0,"len":3},{"text":"район Приморски, бл. 1, до прилеп","pin":[43.21702,27.91114],"g":"b536fb333a2fc1de2","all":false,"wdem":0,"len":3},{"text":"район Приморски, бл. 1, до прилеп","pin":[43.21713,27.91094],"g":"b536fb333a2fc1de2","all":false,"wdem":0,"len":3},{"text":"район Приморски, бл. 1, до прилеп","pin":[43.21725,27.91077],"g":"b536fb333a2fc1de2","all":false,"wdem":0,"len":3}],"flagship":[{"rank":210,"all":false,"wdem":0,"core":2,"q":22,"qtk":["levski"],"wtk":["chaika"]},{"rank":265,"all":false,"wdem":0,"core":2,"q":22,"qtk":["levski"],"wtk":["chaika"]}]}]

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [System.Text.UTF8Encoding]::new()
@'"'

const fs=require('fs'),vm=require('vm'),cp=require('child_process');
const html=fs.readFileSync('index.html','utf8'),head=cp.execFileSync('git',['show','f745349:index.html'],{encoding:'utf8'});
function slice(h){let a=h.indexOf('    function norm(s)',h.indexOf('(function initAddressSearch'));let b=h.indexOf('    // ---- display payload',a);let c=h.indexOf('    const SEARCH_LIMIT = 8',b);let d=h.indexOf('    // ---- lazy load + cache',c);return h.slice(a,b)+h.slice(c,d);}
let original=slice(html); console.log('matcher_equals_HEAD',original.replace(/\\r/g,'')===slice(head).replace(/\\r/g,''));
let source=original.replace('      const out = ranked.slice','      trace = {ranked,blockTyped,blockHeader};\\n      const out = ranked.slice');
function engine(s){let ctx={trace:null};vm.createContext(ctx);vm.runInContext(s+'\\nthis.api={norm,skel,prepareIndex,runGeocoderSearch};',ctx);return ctx;}
const base=JSON.parse(fs.readFileSync('data/search_index.json','utf8')),rows=JSON.parse(fs.readFileSync('data/address_rows.json','utf8')).rows,preview=JSON.parse(fs.readFileSync('scratch/boundary_gallery/granitsi_preview_05.09/adresi_proposal_08.09.json','utf8')).entries;
const old=engine(source);old.api.prepareIndex(base);
const qs=['чайка студентска бл 11','бл 11 левски','бл 11 чайка','студентска бл 11'];
function compact(ctx,q,idx){let out=ctx.api.runGeocoderSearch(q,idx),t=ctx.trace; return {query:q,blockTyped:t.blockTyped,header:out.blockHeader,full:t.ranked.filter(s=>s.all).length,top:t.ranked.slice(0,8).map(s=>({text:s.e._p?.new_v2||s.e.label||rows[s.e.display_id]?.[0],pin:s.e.pin,g:s.e.g,all:s.all,wdem:s.wdem,q:s.e.q,len:(s.e.tk||[]).length+(s.e.qtk||[]).length})),flagship:t.ranked.filter(s=>s.e.g==='b6797e83ec13fe798').map(s=>({rank:t.ranked.indexOf(s)+1,all:s.all,wdem:s.wdem,core:s.matchedCore,q:s.e.q,qtk:s.e.qtk,wtk:s.e.wtk}))};}

const dict=new Map();for(let i=0;i<base.entries.length;i++){let e=base.entries[i],k=JSON.stringify([e.pin,e.tk]);if("'!dict.has(k))dict.set(k,[]);dict.get(k).push(e);}
let unmatched=0,entries=[];
for(let p of preview){let bucket=dict.get(JSON.stringify([p.pin,p.tk])),e=bucket?.[0];if(!e){unmatched++;continue;} e=JSON.parse(JSON.stringify(e));e._p=p;entries.push(e);}
console.log('"'proposal_join',entries.length,unmatched);
let names=[...new Set(preview.filter(p=>['edge','inside'].includes(p.cls)).map(p=>p.poly))].sort();
function toks(s){return old.api.norm(s.replace(/"'^(?:кв'"\\.|ж\\.к\\.|к\\.к\\.|м\\.|местност)\\s*/i,'')).split(' ').map(old.api.skel).filter(t=>t.length>2&&"'!/''^'"\\d+"'$/.test(t));}
for(let e of entries){let p=e._p;let canon=['"'edge','inside'].includes(p.cls);let qtk=canon?toks(p.poly):[];e.wtk=(e.qtk||[]).filter(t=>"'!qtk.includes(t));e.qtk=qtk;if(canon)e.q=names.indexOf(p.poly);e.otk=toks((p.orient||'"'').replace(/"'^до'"\\s+(?:ул\\.\\s*)?/i,'')).filter(t=>"'!(e.tk||[]).includes(t));}
let updated=source
.replace("if (e.qtk) toks = toks.concat(e.qtk);","if (e.qtk) toks = toks.concat(e.qtk); if(e.wtk)toks=toks.concat(e.wtk); if(e.otk)toks=toks.concat(e.otk);")
.replace("['"'tk','qtk','alias_tk','dtk','stk']\",\"['tk','qtk','alias_tk','dtk','stk','wtk','otk']\")
.replace('index._areaVocab = av;','index._areaVocab = av; index._signedQuarterVocab = new Set((index.quarter_names||[]).flatMap(quarterToks));')
.replace('matchedViaStk = 0;','matchedViaStk = 0, matchedViaWitness=0, matchedViaOtkOnly=0;')
.replace(\"          if (best === 0) { all = false; continue; }\",
\"          if (e.wtk && best<3 && "'!(index._signedQuarterVocab.has(toks[qi]) && e.q!=null)){for(const t of e.wtk){const k=m[t]||0;if(k>best){best=k;matchedViaWitness++;if(best===3)break;}}}'"\\n\"+
\"          if (e.otk && best<3){for(const t of e.otk){const k=m[t]||0;if(k>best){best=k;matchedViaOtkOnly++;if(best===3)break;}}}\\n\"+
\"          if (best === 0) { all = false; continue; }\")
.replace('scored.push({ e: e,','scored.push({ e: e, matchedCore, wdem: matchedViaWitness>0 && matchedCore===0?1:0, otdem:matchedViaOtkOnly>0?1:0,')
.replace('        if (a.odem "'!== b.odem)'"', '        if (a.wdem "'!== b.wdem) return a.wdem-b.wdem; if(a.otdem!==b.otdem)return a.otdem-b.otdem;'"\\n        if (a.odem "'!== b.odem)'"');
let ctx={trace:null,quarterToks:toks};vm.createContext(ctx);vm.runInContext(updated+'\\nthis.api={norm,skel,prepareIndex,runGeocoderSearch};',ctx);
let candidate={entries,quarter_names:names};ctx.api.prepareIndex(candidate);

let before=compact(ctx,'бл 11 левски',candidate);
let fixedSrc=updated.replace('matchedViaWitness>0 && matchedCore===0?1:0','matchedViaWitness>0?1:0');
let fx={trace:null,quarterToks:toks};vm.createContext(fx);vm.runInContext(fixedSrc+'\\nthis.api={norm,skel,prepareIndex,runGeocoderSearch};',fx);fx.api.prepareIndex(candidate);let after=compact(fx,'бл 11 левски',candidate);
console.log('wdem_per_token_counterfactual',JSON.stringify({before:before.top.slice(0,5),after:after.top.slice(0,5),header:after.header}));
for (const q of ['бл 11 цветен','левски студентска бл 11']){let b=compact(old,q,base),c=compact(ctx,q,candidate);console.log('extra',JSON.stringify({q,baseline:{blockTyped:b.blockTyped,flagship:b.flagship},sim:{blockTyped:c.blockTyped,flagship:c.flagship}}));}
let x=base.entries.find(e=>e.display_id===1319);let leak=engine(updated);leak.quarterToks=toks;let li={entries:[{...x,q:0,qtk:['briz'],wtk:[]}],quarter_names:['ж.к. Бриз','м. Акчелар']};leak.api.prepareIndex(li);console.log('tk_guard_leak',JSON.stringify({entry:x,result:leak.api.runGeocoderSearch('акчелар',li)}));


'@ | node -" in C:\git\Fire_Varna
 succeeded in 1081ms:
matcher_equals_HEAD true
proposal_join 5274 0
wdem_per_token_counterfactual {"before":[{"text":"район Приморски, бл. 11, бул. Царевец","pin":[43.21976,27.91949],"g":"b79191957abcb5ea2","all":true,"wdem":0,"len":4},{"text":"кв. Левски, бл. 11, до карамфил","pin":[43.22615,27.91075],"g":"b77bcb56eec95837e","all":true,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 11, до ул. студентска","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":true,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 11, бул. Васил Левски","pin":[43.22017,27.92848],"g":"b620d9a87b225989d","all":true,"wdem":0,"q":22,"len":6},{"text":"кв. Левски, бл. 11, до доктор иван басанович","pin":[43.22513,27.92315],"g":"bba00138230d589b0","all":true,"wdem":0,"q":22,"len":6}],"after":[{"text":"кв. Левски, бл. 11, до карамфил","pin":[43.22615,27.91075],"g":"b77bcb56eec95837e","all":true,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 11, до ул. студентска","pin":[43.22212,27.9378],"g":"b6797e83ec13fe798","all":true,"wdem":0,"q":22,"len":4},{"text":"кв. Левски, бл. 11, бул. Васил Левски","pin":[43.22017,27.92848],"g":"b620d9a87b225989d","all":true,"wdem":0,"q":22,"len":6},{"text":"кв. Левски, бл. 11, до доктор иван басанович","pin":[43.22513,27.92315],"g":"bba00138230d589b0","all":true,"wdem":0,"q":22,"len":6},{"text":"район Приморски, бл. 11, бул. Царевец","pin":[43.21976,27.91949],"g":"b79191957abcb5ea2","all":true,"wdem":1,"len":4}],"header":{"block":"11","count":5,"district_enum":4}}
extra {"q":"бл 11 цветен","baseline":{"blockTyped":true,"flagship":[{"rank":465,"all":false,"qtk":["chaika"]}]},"sim":{"blockTyped":false,"flagship":[{"rank":210,"all":false,"wdem":0,"core":2,"q":22,"qtk":["levski"],"wtk":["chaika"]},{"rank":265,"all":false,"wdem":0,"core":2,"q":22,"qtk":["levski"],"wtk":["chaika"]}]}}
extra {"q":"левски студентска бл 11","baseline":{"blockTyped":true,"flagship":[{"rank":9,"all":false,"qtk":["chaika"]}]},"sim":{"blockTyped":true,"flagship":[{"rank":1,"all":true,"wdem":0,"core":3,"q":22,"qtk":["levski"],"wtk":["chaika"]}]}}
tk_guard_leak {"entry":{"kind":"address","pin":[43.2221,27.94855],"tk":["akchelar"],"d":4,"display_id":1319,"_ord":1339},"result":[{"kind":"address","pin":[43.2221,27.94855],"d":4,"display_id":1319,"allTokens":true,"matched":1,"exact":1,"prefix":0,"fuzzy":0}]}

codex
Симулацията вече възпроизвежда дефекта: за „бл 11 левски“ неопределеният блок на Царевец излиза пред каноничните, а броячът го включва като пълно съвпадение. „чайка студентска бл 11“ става `all=false`, но Студентска остава първи резултат. Проверяваме и картончето: според предложеното пренасяне на полетата районът ще се вижда в списъка, но ще се губи след избора.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git diff --name-only f745349 -- data/search_index.json data/address_rows.json 'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md' index.html" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p=@('"'scratch/boundary_gallery/granitsi_preview_05.09/quarters_signed_08.09.geojson','scratch/boundary_gallery/granitsi_preview_05.09/address_rows_08.09.json'); "'$p | Sort-Object | ForEach-Object { $f=Get-Item -LiteralPath $_; '"'{0} {1} B' -f "'$_,$f.Length }' in C:\git\Fire_Varna
 succeeded in 395ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
index.html

 succeeded in 587ms:
scratch/boundary_gallery/granitsi_preview_05.09/address_rows_08.09.json 5073137 B
scratch/boundary_gallery/granitsi_preview_05.09/quarters_signed_08.09.geojson 301917 B

codex
**НЕГОДНО за подпис.**

База: `f745349`; 86 232 индексни записа, 80 510 адресни реда, 5 567 блокови записа/1 353 различни `g`. Прочетени: [планът](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md), `index.html`, двата адресни JSON-а, пробата и местното копие на подписаните полигони. Полигонният SHA съвпада с пина. Матчерът е еднакъв в HEAD и работното дърво въпреки стейджнатия Б3. Нищо не е променяно.

**S33-1 — Р5 смесва увереността в квартала с намирането на блока.**  
(в) запазва повече полезни попадения, но грешката при ръба чрез Р14 може да потисне правилната заявка. Цената не е непременно отклонение ≤100 m: пожарникарят може да избере друг едноименен блок. Леджерът не помага при това действие.

(г) отнема канон на **2 703 адресни реда**, включително **107 блокови реда/34 `g`**. Запазва Студентска, но отнема Левски на бл.11 при Карамфил: собствен ръб **56,57 m**, чужд **49,18 m**. Следователно не е универсално по-добър.

**Поправка:** отделни правила за канонично показване и за ясно означени алтернативни попадения. Предпочитам (в) само с такава защита на намирането. Пробата също трябва да се преизчисли: **219** нейни „edge“ реда с еднозначно съдържание реално са над 100 m; флагманът показва **59 вместо 67,52 m**.

**S33-2 — Р14 демотирането и обещаната подредба не работят.**  
Изпълних реалните JavaScript функции; добавките на v2 симулирах в паметта върху 5 274-те пробни реда:

| Заявка | Моделен резултат |
|---|---|
| `чайка студентска бл 11` | Студентска е `all=false`, **но остава първи** |
| `бл 11 левски` | Неопределеният Царевец е **първи**, пред каноничните |
| `бл 11 чайка` | Студентска отпада от първите осем |
| `студентска бл 11` | Студентска е първи, `all=true`; обикновеният списък се запазва |

Причина: `bl`/номерът правят `matchedCore>0`, следователно **`wdem=0`**. Премахнатият `qtk` допълнително скъсява неопределения ред в `tk.length+qtk.length`. Броячът показва **5**, включвайки Царевец, вместо четирите канонични блока.

**Поправка:** демотиране по свидетелния токен независимо от останалите основни съвпадения; отделен клас за противоречащ квартал преди общия скоринг; брояч само за каноничните. При тази поправка Царевец слиза от първо на пето място. Добавете регресия за `бл 11 цветен`: преместването в `wtk` променя `blockTyped` от true на false.

**S33-3 — Гардът има обходи.**  
`display_id=1319–1321` носят `tk:["akchelar"]`, но са в **ж.к. Бриз**; първите два са над 448 m навътре. С нов канон заявката „акчелар“ остава `all=true` през `tk`. **169** записа дублират стар квартален токен в `tk`. Префиксът „чай студентска бл 11“ също заобикаля точното `_signedQuarterVocab.has()`.

**Поправка:** квартална семантика по произход във всички токенови канали и общо разпознаване на кварталните фрази/префикси; без механично изтриване на едноименни улици.

**S33-4 — Р10-а допуска измислена „собствена улица“.**  
Реални адресни редове: `50852="ул бл 1 28"`, `74696="ул студентска бл 4"`, `70841="ул радост гараж 12"`. След отделяне на номера предложените забрани оставят „ул бл“. Подмножеството на `tk` тогава я признава за собствена улица на **всичките 5 567 блока**; **4 098** имат множество кандидати.

**Поправка:** определен и валидиран парсер, обработка на `бл/вх/гараж`, правило за многозначност и доказана адресна принадлежност. Само наличието на `studentska` не оправдава „ул. Студентска“; при недоказана принадлежност — „до…“. Метри до адресна точка не бива да се представят като метри до улицата.

**S33-5 — Двете степени не гарантират различимост.**  
Контрапроба върху всички блокови редове: `ул/бул/пл`, отделяне при първа цифра, без начално числови имена, предложения филтър, 120 m, две различни имена, цели метри до първата:

- първа улица: **42 колизионни ключа**;
- плюс втора: **22**;
- плюс метри: **13 ключа / 38 реда / 29 `g`**;
- без ориентир: **1 355 реда**, 191 изцяло непокрити `g`.

Чайка бл.37 има две групи без улица; Трошево бл.5 остава със същите имена и еднаквите **22 m**. Това е условен модел, защото планът не определя окончателния парсер/закръгляне.

**Поправка:** подпишете алгоритъма и остатъка върху крайните видими заглавия по различни `g`, след валидиране на улиците.

**S33-6 — Р12 достига редовете, но оставя противоречив дисплей.**  
Структурните `q/o` покриват **43 099 ефективни** `display_id` реда; останалите 196 имат приоритетен `label`. Но материализация само на противоречията оставя поне **1 053** повторения като „м-т Акчелар, акчелар“. Самият Р12-б допуска 11 627 неопределени реда със стара квартална дума.

**Поправка:** почистена адресна основа за съгласни, противоречащи и неопределени случаи.

**S33-7 — Р1–Р3/Р7 и картончето оставят оперативна дупка.**  
Пробата оставя **1 105 блокови реда** без канон: 606 припокривания и 499 извън. „Район Приморски“ е приемлив резервен контекст само с различаващ ориентир и видима неопределеност. По предложения път районът остава в списъка, но **се губи след избор**, защото `ctx` пренася само заглавието.

**Поправка:** районът и неопределеността да присъстват и в картончето/popup; задължителни заявки и прегледани остатъчни колизии за всички дупки и припокривания.
tokens used
100,464
**НЕГОДНО за подпис.**

База: `f745349`; 86 232 индексни записа, 80 510 адресни реда, 5 567 блокови записа/1 353 различни `g`. Прочетени: [планът](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md), `index.html`, двата адресни JSON-а, пробата и местното копие на подписаните полигони. Полигонният SHA съвпада с пина. Матчерът е еднакъв в HEAD и работното дърво въпреки стейджнатия Б3. Нищо не е променяно.

**S33-1 — Р5 смесва увереността в квартала с намирането на блока.**  
(в) запазва повече полезни попадения, но грешката при ръба чрез Р14 може да потисне правилната заявка. Цената не е непременно отклонение ≤100 m: пожарникарят може да избере друг едноименен блок. Леджерът не помага при това действие.

(г) отнема канон на **2 703 адресни реда**, включително **107 блокови реда/34 `g`**. Запазва Студентска, но отнема Левски на бл.11 при Карамфил: собствен ръб **56,57 m**, чужд **49,18 m**. Следователно не е универсално по-добър.

**Поправка:** отделни правила за канонично показване и за ясно означени алтернативни попадения. Предпочитам (в) само с такава защита на намирането. Пробата също трябва да се преизчисли: **219** нейни „edge“ реда с еднозначно съдържание реално са над 100 m; флагманът показва **59 вместо 67,52 m**.

**S33-2 — Р14 демотирането и обещаната подредба не работят.**  
Изпълних реалните JavaScript функции; добавките на v2 симулирах в паметта върху 5 274-те пробни реда:

| Заявка | Моделен резултат |
|---|---|
| `чайка студентска бл 11` | Студентска е `all=false`, **но остава първи** |
| `бл 11 левски` | Неопределеният Царевец е **първи**, пред каноничните |
| `бл 11 чайка` | Студентска отпада от първите осем |
| `студентска бл 11` | Студентска е първи, `all=true`; обикновеният списък се запазва |

Причина: `bl`/номерът правят `matchedCore>0`, следователно **`wdem=0`**. Премахнатият `qtk` допълнително скъсява неопределения ред в `tk.length+qtk.length`. Броячът показва **5**, включвайки Царевец, вместо четирите канонични блока.

**Поправка:** демотиране по свидетелния токен независимо от останалите основни съвпадения; отделен клас за противоречащ квартал преди общия скоринг; брояч само за каноничните. При тази поправка Царевец слиза от първо на пето място. Добавете регресия за `бл 11 цветен`: преместването в `wtk` променя `blockTyped` от true на false.

**S33-3 — Гардът има обходи.**  
`display_id=1319–1321` носят `tk:["akchelar"]`, но са в **ж.к. Бриз**; първите два са над 448 m навътре. С нов канон заявката „акчелар“ остава `all=true` през `tk`. **169** записа дублират стар квартален токен в `tk`. Префиксът „чай студентска бл 11“ също заобикаля точното `_signedQuarterVocab.has()`.

**Поправка:** квартална семантика по произход във всички токенови канали и общо разпознаване на кварталните фрази/префикси; без механично изтриване на едноименни улици.

**S33-4 — Р10-а допуска измислена „собствена улица“.**  
Реални адресни редове: `50852="ул бл 1 28"`, `74696="ул студентска бл 4"`, `70841="ул радост гараж 12"`. След отделяне на номера предложените забрани оставят „ул бл“. Подмножеството на `tk` тогава я признава за собствена улица на **всичките 5 567 блока**; **4 098** имат множество кандидати.

**Поправка:** определен и валидиран парсер, обработка на `бл/вх/гараж`, правило за многозначност и доказана адресна принадлежност. Само наличието на `studentska` не оправдава „ул. Студентска“; при недоказана принадлежност — „до…“. Метри до адресна точка не бива да се представят като метри до улицата.

**S33-5 — Двете степени не гарантират различимост.**  
Контрапроба върху всички блокови редове: `ул/бул/пл`, отделяне при първа цифра, без начално числови имена, предложения филтър, 120 m, две различни имена, цели метри до първата:

- първа улица: **42 колизионни ключа**;
- плюс втора: **22**;
- плюс метри: **13 ключа / 38 реда / 29 `g`**;
- без ориентир: **1 355 реда**, 191 изцяло непокрити `g`.

Чайка бл.37 има две групи без улица; Трошево бл.5 остава със същите имена и еднаквите **22 m**. Това е условен модел, защото планът не определя окончателния парсер/закръгляне.

**Поправка:** подпишете алгоритъма и остатъка върху крайните видими заглавия по различни `g`, след валидиране на улиците.

**S33-6 — Р12 достига редовете, но оставя противоречив дисплей.**  
Структурните `q/o` покриват **43 099 ефективни** `display_id` реда; останалите 196 имат приоритетен `label`. Но материализация само на противоречията оставя поне **1 053** повторения като „м-т Акчелар, акчелар“. Самият Р12-б допуска 11 627 неопределени реда със стара квартална дума.

**Поправка:** почистена адресна основа за съгласни, противоречащи и неопределени случаи.

**S33-7 — Р1–Р3/Р7 и картончето оставят оперативна дупка.**  
Пробата оставя **1 105 блокови реда** без канон: 606 припокривания и 499 извън. „Район Приморски“ е приемлив резервен контекст само с различаващ ориентир и видима неопределеност. По предложения път районът остава в списъка, но **се губи след избор**, защото `ctx` пренася само заглавието.

**Поправка:** районът и неопределеността да присъстват и в картончето/popup; задължителни заявки и прегледани остатъчни колизии за всички дупки и припокривания.
