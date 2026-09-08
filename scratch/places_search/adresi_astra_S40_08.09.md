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
session id: 01a0808c-d73a-7901-8cfa-c1cf5b6c37f5
--------
user
S40 · Външно око (леща механика + одит на плана): ПЛАН „Картата imot“, подлот И-А — C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md (редакция 4 + сверка ИА-О30 на Архитекта след 5 одиторски кръга; протоколът на опровергателите: scratch/places_search/karta_imot_plan_reviews_08.09.md; канон: docs/decisions/011_kartata_imot.md; тялото с решенията: scratch/places_search/imot_decisions_1_2026-09-08_draft.json; контекст: docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md банер + §20). Решението на Петър (08.09 вечер): плочката на imot.bg (95 полигона, 0 застъпвания, 97 % от адресните точки) е НАШАТА квартална карта; старите Wikimapia полигони и поправки са отменени; изпълнение на две стъпки (1: полигоните + местата/хотелите; 2: адресите на всички сгради). И-А = само varna_3d (нов строител build_quarters_signed_imot.py със схемата на v1, собствен гейт qa_quarters_signed_imot.py, архив на v1, замразеният вход става проследен във varna_3d, данните ги комитва Петър) + три документа във Fire_Varna; И-Б (Fire Б4 върху стейджнатия Б3) е отделен план. Въпроси: (1) изпълним ли е планът от Изпълнител без въпроси — кои редове са неизпълними или двусмислени (посочи ред/секция); (2) гейтовете: има ли гейт, който е обещание, червен по конструкция без STOP, или с отрицателна половина, която командата не чете; (3) редът на комитите и идентичностите (агентите — код/документи; Петър — данни/геометрия/.gitignore) — пропуски; (4) приватност: излиза ли нещо частно в проследен файл на публичното Fire_Varna (геометрия, обяви, хешове на сурови отговори, координати вкл. с десетична запетая); (5) съгласуваност с ADR 011 (И-D1…И-D7) и с ADR 010 (D3/D6/D8/D9/D13/D14/D16/D18); (6) какво липсва за подпис на Петър сутринта — таблицата §9 пълна ли е (обекти, села, трите без полигон, район→кв/мр, precision_m, vinitsa_sever, архивни пътища, source_terms с три ключа). Не пипай нищо. До 800 думи: присъда ГОДНО/НЕГОДНО с блокери и бележки, с ред/секция.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя плана спрямо канона и посочените доказателства, само с четене. Ще разделя независимата проверка между механиката на гейтовете и съгласуваността на решенията, а аз ще проследя приватността, комитите и таблицата за подпис.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -TotalCount 110" in C:\git\Fire_Varna
 succeeded in 476ms:
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status -sb' in C:\git\Fire_Varna
 succeeded in 355ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 140, behind 3]
M  data/hotels.json
M  data/place_categories.json
M  data/places.json
A  gates/probe/b3_g11.py
M  index.html
D  scratch/places_search/granitsi_fixtures_06.09.json
A  scratch/places_search/granitsi_fixtures_07.09.json
 M scratch/places_search/karta_imot_plan_reviews_08.09.md
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
?? scratch/places_search/adresi_astra_S40_08.09.md
?? scratch/places_search/cleanup_brief_astra.md
?? scratch/places_search/cleanup_brief_kimi.md
?? scratch/places_search/golden_brief_kimi.md
?? scratch/places_search/golden_brief_sol.md
?? scratch/places_search/granitsi_brief_astra.md
?? scratch/places_search/granitsi_brief_kimi.md
?? scratch/places_search/karta_imot_plan_IA_r5_raw_08.09.md
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
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-ChildItem -LiteralPath 'docs/plans/ПЛАН_Картата_imot_И-А_08.09.md','scratch/places_search/karta_imot_plan_reviews_08.09.md','docs/decisions/011_kartata_imot.md','scratch/places_search/imot_decisions_1_2026-09-08_draft.json','docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md' | Sort-Object FullName | Select-Object FullName,Length; Get-ChildItem -LiteralPath 'docs/decisions' -Filter '010*' | Select-Object FullName,Length; Get-ChildItem -LiteralPath . -Filter 'AGENTS.md' | Select-Object FullName,Length" in C:\git\Fire_Varna
 succeeded in 565ms:

FullName                                                                       Length
--------                                                                       ------
C:\git\Fire_Varna\docs\decisions\011_kartata_imot.md                            16548
C:\git\Fire_Varna\docs\plans\ПЛАН_Картата_imot_И-А_08.09.md                    167782
C:\git\Fire_Varna\docs\sessions\СЪСТОЯНИЕ_Границите_06.09.md                   114196
C:\git\Fire_Varna\scratch\places_search\imot_decisions_1_2026-09-08_draft.json  53115
C:\git\Fire_Varna\scratch\places_search\karta_imot_plan_reviews_08.09.md       320010
C:\git\Fire_Varna\docs\decisions\010_signed_quarter_boundaries.md               53242
C:\git\Fire_Varna\AGENTS.md                                                     27909



exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$paths=@('"'AGENTS.md','docs/plans/ПЛАН_Картата_imot_И-А_08.09.md','scratch/places_search/karta_imot_plan_reviews_08.09.md','docs/decisions/011_kartata_imot.md','scratch/places_search/imot_decisions_1_2026-09-08_draft.json','docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md','docs/decisions/010_signed_quarter_boundaries.md'); foreach("'$p in $paths){ '"'{0} | lines={1}' -f "'$p, @(Get-Content -LiteralPath $p -Encoding UTF8).Count }; git rev-parse HEAD' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Картата_imot_И-А_08.09.md'; "'$n=0; Get-Content -LiteralPath $p -Encoding UTF8 | ForEach-Object { $n++; if ($_ -match '"'"'^#{1,4} '"'){ '{0}: {1}' -f "'$n,$_ }}' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -Encoding UTF8 -TotalCount 32" in C:\git\Fire_Varna
 succeeded in 562ms:
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


 succeeded in 625ms:
AGENTS.md | lines=407
docs/plans/ПЛАН_Картата_imot_И-А_08.09.md | lines=630
scratch/places_search/karta_imot_plan_reviews_08.09.md | lines=428
docs/decisions/011_kartata_imot.md | lines=58
scratch/places_search/imot_decisions_1_2026-09-08_draft.json | lines=1841
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md | lines=173
docs/decisions/010_signed_quarter_boundaries.md | lines=142
b07b8ba62e7404ed6e6c9858fbc49278cb0c6069

 succeeded in 625ms:
1: # ПЛАН · Картата imot — под-лот **И-А** (varna_3d + документи)
13: ## 0 · Червени редове
32: ## 1 · Мярка (всичко мерено 08.09; нула редакции)
34: ### 1.1 · Състояние на репата
53: ### 1.2 · Базата на `varna_3d` е ЗЕЛЕНА (за разлика от Fire_Varna) — **девет реда**
79: ### 1.3 · Схемата на v1 (какво трябва да възпроизведе v2, ключ по ключ)
94: ### 1.4 · Замразеният снапшот на imot.bg (входът)
110: ### 1.5 · Адресните точки — маската, затворена и сверена
129: ### 1.6 · Тялото с решенията (черновата днес, **след комит 7556227**)
148: ### 1.7 · Кодовете, регистърът и районът (върху ДОСТАВЯНИТЕ 84)
181: ### 1.8 · Пиновете, които сочат v1 — изчерпателно, мерено с `git grep`
210: ### 1.9 · Механиката на `.gitignore` във `varna_3d` (М)
219: ## 2 · Обявени отклонения
252: ## 3 · Write-set с котви (изчерпателен — път извън тази таблица = ИА-STOP 1)
254: ### 3.А · `varna_3d` — нови файлове
273: ### 3.Б · `varna_3d` — точкови редакции (**архивният път е един и същ навсякъде**: `docs/archive/quarters_signed_v1_2026-09-06.geojson`)
297: ### 3.В · `Ф7` (подписаното тяло) срещу черновия блоб `8626ad43…` — **точно ДЕСЕТ разлики, нула други**
316: ### 3.Г · Правилата на новия билдър (`Ф1`) — дословно, без празни места
385: ### 3.Д · `Fire_Varna` — три проследени документа и един игниран файл
398: ## 4 · Ред на изпълнение
426: ## 5 · Гейтове
477: ## 6 · Комити
511: ## 7 · STOP
535: ## 8 · Локален преглед (кои проби гледа Петър)
547: ## 9 · Решения за Петър (Gate 1) — **двайсет и едно**
577: ## 10 · Какво НЕ се пипа
594: ## 11 · Пренесено към И-Б (измерени дефекти, които И-А не докосва)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/decisions/011_kartata_imot.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 1..58 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Картата_imot_И-А_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 1..52 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Картата_imot_И-А_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 385..476 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 515ms:
1: # ADR 011 · Картата на кварталите = плочката на imot.bg; регистър на отменените решения
2: 
3: **Статус:** Proposed — чернова на Claude Architect, чака подписа на Петър (Gate 1). · **Дата:** 08.09.2026 · **Отменя/изменя:** ADR 010 (`010_signed_quarter_boundaries.md`) в частта за ГЕОМЕТРИЯТА; всичко друго от ADR 010 остава. · **Планът:** `docs/plans/ПЛАН_Картата_imot_08.09.md` (чернова). · **Състояние:** `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` §16–§20.
4: 
5: ## Контекст
6: 
7: Думите на Петър, 08.09.2026 вечер, дословно: „страхотна е !!!!! ТОВА Е НАШАТА КАРТА — ДАВАЙ ДА ИМПЛЕМЕНТИРАМЕ“ (за пробата `scratch/boundary_gallery/granitsi_preview_05.09/imot_city_08.09.html`: 95-те полигона на районите на Варна, както ги чертае imot.bg) и „СТАРИТЕ ПОПРАВКИ НЕ ВАЖАТ — ПОЛЗВАМЕ ТЕЗИ ПОЛИГОНИ, МОЛЯ ПРЕГЛЕДАЙ ЗА СТАРИ РЕШЕНИЯ ОТНОСНО ПОЛИГОНИТЕ И ГИ ОТМЕНИ — ИСКАМ ДА ВКАРАМЕ И РЕД ЗА ДА НЕ СЕ БЪРКАМЕ“. По-рано същия ден: „тези на центъра са супер — ползваме тях“.
8: 
9: Какво е плочката (мерено 08.09, §18–§19): imot.bg има речник от **98 района** за град Варна (`api.imot.bg/mob_api/dictionary/search/1?town=5`) и чертае собствен полигон за всеки; полигонът се получава без вход от `mob_api/details?id=<обява>` (поле `points`, когато `coordinates` завършва с флаг 0). Взети са **95** (трите без обяви нямат полигон: Северна промишлена зона 5866, Електроразпределение Варна 5848, Малка Чайка 6294). **0 застъпвания помежду им, съседите споделят върхове, всички валидни преди поправка, 93,03 km² (EPSG:32635), 97,2 % от 80 510 частни адресни точки вътре**; 2 274 точки извън всеки полигон. Провенанс по полигон в `imot_bg_varna_polygons_08.09.geojson` (частна папка): обява, SHA-256 на суровия отговор, време, речник и хешът му. Втори свидетел mirela.bg (73 полигона, 49 застъпвания) — само за сверка. Досегашната основа: 60 полигона от Wikimapia, потвърдени от Петър по борд 06–07.09 (Б1), покриващи 84,9 % от точките, 61,7 km², с 61 спорни двойки при разделяне.
10: 
11: ## Решения
12: 
13: **И-D1 · Геометрията на кварталите на Варна е плочката на imot.bg.** Каноничният файл остава `varna_3d/data/quarters_signed.geojson` (ADR 010 D3), но версия 2 се СТРОИ от снапшота на imot.bg (08.09.2026) + един подписан файл с решенията (И-D3), а не от Wikimapia. Стълбата на изворите за ГЕОМЕТРИЯ от ADR 010 D0 — (1) официален полигон на АГКК и (4) деклариран/Wikimapia полигон — се заменя с: **(1) плочката на imot.bg** (единствен извор на геометрия за квартал/район/местност/к.к./село), **(2) ръчна поправка от Петър върху плочката** (само като нова версия по D9, с довод). Написаните извори (REG/KAIS/НТР) остават свидетели за ИМЕТО и за 375-те места (D6), не за геометрията.
14: 
15: **И-D2 · Записът на новия извор.** Всеки Feature носи полетата от ADR 010 D1 със стойности: `source: "imot_bg_tiling"`, `method: "external_tiling"`, `drawn_by: "imot.bg (речник на районите, mob_api)"`, `geometry_origin: "imot_bg_points"`, `witnesses[]` = { `kind: "imot_bg_details"`, `advert_id`, `raw_response_sha256`, `fetched_at`, `raion_num` } + { `kind: "imot_bg_dictionary"`, `sha256`, `fetched_at`, `n: 98` }, `precision_m` = премерено (мярка в плана; под на ADR 010 D7 = 50 m), `approved_by: Petar`, `signed_by: Petar`, `version: 2`. В `_meta`: `source_terms` = { `url: "https://www.imot.bg/obshti-uslovia"`, `checked_at` } (поле за попълване, не тема за обсъждане), `publication` = G29 (геометрията НИКОГА не пътува публично; публично излизат само име, код, `src` и редът за атрибуция), `dictionary_sha256`, `snapshot_date`, `decisions_sha256`, `parent_child` (И-D4), `signature`. Редът за атрибуция в приложението (И11) се преписва за новия извор (дословният текст — решение на Петър в плана §9).
16: 
17: **И-D3 · Един каноничен файл с решенията за плочката.** `scratch/places_search/imot_decisions_1_2026-09-08.json` (подписва Петър; хешът му влиза в `_meta.decisions_sha256`): за всеки от 98-те района — `raion_num`, `code` (съществуващ id от `Varna_buildings/config/quarter_registry.json`, където името съвпада; иначе нов код по К37), `name` (както imot го изписва, с префикса на регистъра), `kind`, `district` (свидетел АГКК AU5 по центроид, G23), `parent` (И-D4), `class` ∈ {квартал/район, зона, м-т, к.к., село, обект}, `include` (да/не/отложено с довод), `note`. Обектите (Гранд Мол, Бизнес хотел, Летище, Пристанище Варна, Бизнес парк Варна) и селата са редове със същото поле `include` — решение на Петър, не автоматика. Промяна на снапшота = нов файл с решения + нова версия по D9.
18: 
19: **И-D4 · Йерархията върху плочката.** Плочката е листовият слой: всяка точка е в най-много един полигон. Родителите, които imot няма като полигон (Левски, Владиславово, Възраждане, Младост, Победа), са **виртуални обединения на поименно подписани деца** (Левски = Левски 1 + Левски 2 + Цветен квартал + Базар Левски; Владиславово = Владислав Варненчик 1 + 2 + Кайсиева градина + Боклук Тарла + Планова промишлена зона; Възраждане = 1–4; Младост = 1 + 2; Победа = Победа + Конфуто) — с рецепта и версия в `_meta.parent_child`; D8 е изпълнен по конструкция (детето е клетка на родителя). Родства извън плочката не се въвеждат в този лот; старите деца/изключения (Максуда, Средна Трака, Розова долина, Дружба, Абатко, Горчивата чешма, Св. Иван Рилски като отделен полигон) НЕ се пренасят — могат да се върнат само като ново изрично решение на Петър.
20: 
21: **И-D5 · Регистърът на отменените решения (редът, който Петър поиска).**
22: 
23: | Старо решение / артефакт | Статус от 08.09 вечер | Заменено от |
24: |---|---|---|
25: | ADR 010 D0 — стълбата за ГЕОМЕТРИЯ: (1) АГКК INSPIRE полигони, (4) декларирани/Wikimapia полигони | ОТМЕНЕНО за геометрията | И-D1 (плочката на imot.bg; ръчна поправка само като нова версия) |
26: | ADR 010 D2 — лицензната таблица по `method` (по памет/огради/сгради/улици) и забраната за Esri подложка | ЗАМЕНЕНО за новия извор | И-D2 (`source_terms`, G29) |
27: | ADR 010 D11 — инструментът „режим граница“ за ръчно чертане | ОТЛОЖЕНО (не е нужен за плочката; остава за бъдещи поправки по И-D1 (2)) | — |
28: | ADR 010 D1, D3, D4, D5, D6, D7, D8, D9, D10, D12, D13, D14, D15, D16, D17, D18, D19, D20; G22, G23, G29 | ОСТАВАТ непроменени | — |
29: | Б1 — `varna_3d/data/quarters_signed.geojson` v1 (60 Wikimapia полигона), `granitsi_decisions_2/3/4_*.json`, `board.html` изборите 06–07.09, `_meta.parent_child` (11 родства), висящият родител „borovets“ | ОТМЕНЕНИ; файловете → архив (git mv, никога изтриване) | v2 по И-D1–И-D4 |
30: | Б2 — данните на varna_3d (комити на Петър c1bb9dc, d17de0d, 05f485e: места/хотели с квартал по v1; p8a леджер) | ЗАМЕНЯТ СЕ с регенерация по v2 (данните ги комитва Петър, D16/G4) | планът, лот И3 |
31: | Б3 — стейджнатата доставка във Fire_Varna: механизмът (QUARTER_SRC, SIGNED_POLYGON/DISTRICT_FALLBACK, валидатори, пинове по блоб, проба, гейт b3_g11) | ОСТАВА | — |
32: | Б3 — данните (три блоба от 05f485e), `QUARTER_CODES` (28), 11-те фикстури, И11 Wikimapia атрибуцията | ПРЕБАЗИРАТ СЕ (Б4) | планът, лот И4 |
33: | Пробите 08.09: разширеният Център (`tsentar_extended`), decisions-5 (20 Wikimapia кандидата за дупките), Цветен квартал-кандидатът (wm 6805503), разделянето v2 (дете изрязва родител; 13 спорни двойки; 49 ивици), четирите ориентира-сгради (Опера/Община/Стадион/кино), предложените родства от К35 (Възраждане 4, ПЗ Планова), предложението „адресите по полигон“ по старите полигони (§12) | ОТМЕНЕНИ като предложения (остават като история в игнорираната папка) | плочката (imot има Център, Цветен квартал, Стадион Спартак, Операта, ВИНС-Червен площад, Окръжна болница-Генерали…) |
34: | Докладът „кварталната каша“ и отчетът-прекласификация (08.09): мерките | ОСТАВАТ като история и база за сравнение | — |
35: | Решение А (речник зона → квартал; кадастър/OSM = свидетели) и решение В (канонът = полигонът + гейт при билд) | ОСТАВАТ (не зависят от извора) | прилагат се към плочката |
36: | Решение Б (границите/родствата/покритието/точността по борд върху Wikimapia) | ОТМЕНЕНО | И-D1, И-D3, И-D4 |
37: | Присъдите на панела съдии (raioni_judges_08.09.md: „нашият остава“ за 20-те спорни) и препоръките S39/К38 за изключения | ИСТОРИЯ, не решения (Петър реши иначе) | — |
38: | План „Адресите по полигон“ v3 (`ПЛАН_Адресите_по_полигон_08.09.md`) | ОСТАВА като следващ лот; референцията към полигоните се сменя към v2 | лот И5 |
39: | Регистърът `Varna_buildings/config/quarter_registry.json` (84 записа, подписан 12.08) | ОСТАВА; допълва се с нови кодове/алиаси само по предложение, което Петър прилага (D14) | планът, лот И2 |
40: 
41: **И-D6 · Редът на изпълнение и подписите.** Непроменени: D13 (тройката Varna_buildings → varna_3d → Fire_Varna), D14 (регистърът е подписано тяло), D16 (идентичности; данните ги комитва Петър). Планировчик (Opus, само четене) пише плана → Кими и Astra → подпис на Петър → Изпълнител → Одитор → локален преглед → публикуване от Петър. Нищо не се редактира преди подписа на плана.
42: 
43: **И-D7 · Какво НЕ се променя.** D6 — писмените свидетели пазят приоритета си за `quarter` на 375-те места; D12 — правилата на търсенето; G29 — геометрията никога публично; release-машината (гейтове 1–7, опашката, allow-файловете); границите на плана „Изчистване“ (Фаза A) и всичко извън темата „Границите“.
44: 
45: ## Последствия
46: 
47: - Покритието на адресните точки с квартална дума: 84,9 % → 97,2 % (при пълна плочка); остават 2 274 точки за маска и класификация (порт, промзона, село, грешна координата) — гейт „всяка точка отчетена“, не насилствен квартал.
48: - Думата на около 18 280 адреса се променя спрямо старите полигони (§19) — това е СЪЗНАТЕЛНО, по решението на Петър; дифът се измерва и се показва в плана, не се крие.
49: - Три района от речника нямат полигон днес — решение: чакане на обява с флаг 0, или ръчно очертаване от Петър по И-D1 (2), или `no_boundary` по D4.
50: - Кодовете: ~38 от 60-те досегашни остават 1:1, ~30 нови, ~10 села/местности с 0 сгради — включване по И-D3.
51: 
52: ## Гейтове (държат се от плана; тук само имената)
53: 
54: Валидност преди поправка · 0 застъпвания и споделени ръбове · всички 98 id отчетени · всяка частна адресна точка в точно една клетка или в остатъчната маска с клас · D8 по конструкция за виртуалните родители · пинове по БЛОБ (`git show`) · два билда → едни байтове · сканиране за геометрия и кадастрални идентификатори в проследените файлове на Fire_Varna (0 попадения) · редът за атрибуция присъства · фикстурите с доказано падаща отрицателна половина.
55: 
56: ## Какво НЕ е
57: 
58: Не е публикуване на геометрия. Не е промяна на адресния резолвер (следващ лот). Не е връщане на нито едно старо изключение „по удобство“. Не е автоматично приемане на нов снапшот на imot.bg — всеки нов снапшот е кандидат с диф и нов подпис (D9).

 succeeded in 505ms:
1: # ПЛАН · Картата imot — под-лот **И-А** (varna_3d + документи)
2: 
3: `Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md` · 08.09.2026 · **редакция 4** (след шест одиторски кръга: два общи + „И-А кръг 1“, „И-А кръг 2“ и двата кръга върху редакция 3) · Планировчик (Opus, само четене) → **подпис на Петър (Gate 1)** → Изпълнител → Одитор → локален преглед → **Gate 2 и пуш от Петър**
4: 
5: **Какво прави този лот.** Прави плочката на imot.bg **канонична геометрия** в частното репо `varna_3d` — замразеният вход, подписаното тяло с решенията, нов билдър, негов собствен гейт, архив на v1 — и допълва три документа във Fire_Varna. **Нищо във Fire_Varna освен тези три проследени документа и един поименно обявен ИГНОРИРАН файл за преглед не се пипа.** Живата карта, доставката Б3, `index.html`, `data/`, `tests/`, `gates/` на Fire_Varna остават непроменени и си остават работа на **И-Б**.
6: 
7: **Предшественик.** `docs/plans/ПЛАН_Картата_imot_08.09.md` (редакция 4, **156 024 B, 735 реда, непроследен** — М: `wc -c -l` → `735 156024`; `git ls-files --error-unmatch` → `did not match any file`). Този под-лот **изпълнява** неговите §3 И-А, §5.А и Приложение Б; всяко място, където се разминава с него, е ред в §2. Планът v4 остава на диска като предшественик и **не се изтрива**.
8: 
9: Всяко число долу носи котва: **(Ч)** = `файл:ред`, **(М)** = командата, която пуснах, и изходът ѝ. Числа без котва в този план няма. Всяко число на редакция 3, което този кръг обори, е поправено ТУК с нова мярка и е назовано поименно на мястото си.
10: 
11: ---
12: 
13: ## 0 · Червени редове
14: 
15: 1. **Нищо не се редактира преди подписа.** Първата команда на Изпълнителя е `git status --porcelain`, не `Write`. **Единственото изключение, обявено поименно:** файлът `Д1` — самият този план — се записва на диска СЛЕД подписа и ПРЕДИ `К1`, защото файлът, който лежи там днес, е **друга редакция** (М: 109 670 B, 536 реда, заглавен ред „редакция 2 (след два одиторски кръга)“, непроследен). Записът на подписания текст **не е редакция на подписано тяло** — той Е тялото (стъпка 2, ИА-О22).
16: 2. **Никакъв `git push`.** Пушът е само на Петър (универсален инвариант №1).
17: 3. **Данните и геометрията ги комитва Петър** (ADR 010 D16, Ч `010_signed_quarter_boundaries.md:68`). Агентът ги оставя стейджнати с изричен pathspec.
18: 4. **Fire_Varna: САМО три ПРОСЛЕДЕНИ документа (Д1, Д2, Д3) + един поименно обявен ИГНОРИРАН файл за преглед (Д4).** Никакъв ред в `index.html`, `data/`, `tests/`, `gates/`, `scratch/places_search/*.py|*.json`. Докосване на пети път във Fire_Varna = STOP.
19: 5. **Нула квартална геометрия и нула суров провенанс в проследен файл на Fire_Varna.** Геометрията, `advert_id`, `raw_sha256`, `points` и **всяка координата** живеят само в **частното** репо `varna_3d` и в игнорираната папка на Fire_Varna (М: `git check-ignore -v scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson` → `.gitignore:64:/scratch/boundary_gallery/`). **Този план е проследен файл на Fire_Varna — затова в текста му няма нито една двойка `lat/lon`; навсякъде, където предишна редакция цитираше координата, стои „(координата в частния файл)“. Спазването се съди механично от ИА-19.** Обобщени производни (площи, брой върхове, хистограма на ръба, хешове) **не са координати** и остават позволени — обявено в ИА-О24, дългът за правило и гейт е ИБ-18.
20: 6. **Гейт, чиято команда не може да върне ≠ 0, не е гейт.** Всяка обявена отрицателна половина ТРЯБВА да е тичала и да е паднала с записан изход; „ще падне“ не е доказателство (поука `gates-lie-more-than-code`). **Ред, за който предварително се знае, че няма да падне, НЕ стои в колоната „отрицателна половина“** — той е мярка и се записва в отчета.
21: 7. **Нула регресии.** Всеки от деветте измерени изхода на **§1.2** се запазва — **със заявената в §5 команда за съответната фаза** (преди и след преместването на v1 командата е РАЗЛИЧНА; изходът е същият). Различен изход = STOP.
22: 8. **Подписано тяло не се редактира на място.** Нова версия — нов файл, стар в архива, никога `git rm`.
23: 9. **Кодът е на латиница.** Имена на модули и коментари на английски; на български остават документите и текстовете за човек (поука `code-in-english`).
24: 10. **Собствени пространства на номерата — затворени и без сблъсък по азбука.** Гейтове **ИА-1 … ИА-19**, отклонения **ИА-О1 … ИА-О24**, спирачки **ИА-STOP 1 … 17**, файлове **Ф1 … Ф10**, точкови редакции **Т1 … Т15**, разлики в подписаното тяло **Х1 … Х10**, пинове **П1 … П18**, база **Н1 … Н9**, решения **Р1 … Р21**, комити **К1 … К9**, дългове към И-Б **ИБ-1 … ИБ-18**. (М: `grep -rIl "ИА-[0-9]" C:/git/Fire_Varna/docs C:/git/varna_3d/src C:/git/varna_3d/docs` → **0 файла извън самия този план**.)
25:    **Пространството `Б` НЕ се използва от този план в нито един вид.** Кръг 3 намери, че `Б1…Б15` (точкови редакции) и `Б-1…Б-16` (дългове) се различаваха само по тире, а „Б1“ и „Б3“ вече значат живи лотове в кода (М: `build_quarters_signed.py:1408` `"lot": "Б1"`, `:1563` `fail("червена черта", …лот Б1…)`, `qa_quarters_signed.py:1197` „Gate Б1“) и живата доставка Б3. Затова редакциите станаха **Т**, дълговете — **ИБ**. Никакъв `G4`, `G11`, `G15`, `G17`, `G21`, `G22`, `G23`, `G29`; никакъв гол `О7`/`О8`/`О16` — те са заети в `ПЛАН_Б3_07.09.md:240`, `:241`, `:249` (Ч), а пространството `О` там стига до **О30** (Ч `:263`). **Латинско `A` не се използва никъде.**
26: 11. **Лицензът не е тема.** Дословният низ за атрибуция се **попълва** по решение Р10; не се обсъжда, не се проучва.
27: 12. **Sha на доставка = блобът.** Във Fire_Varna работното копие ≠ блоб. Във **varna_3d разлика няма**: `.gitattributes:4` е `* text=auto eol=lf` (Ч), М: `git check-attr -a data/quarters_signed.geojson` → `eol: lf`, и работното копие, и блобът дават `c1551d24…`, 301 917 B. Правилото пак е „чети блоба“; varna_3d просто няма как да те излъже.
28: 13. **Блоб се адресира стабилно, не през HEAD.** Навсякъде, където се чете блоб, ревизията се взема с `git -C <репо> log -1 --format=%H -- <път>` (М днес за черновата с решенията → `7556227…`; за `district_resolutions_2026-09-07.json` → `e6c706d…`; HEAD на Fire_Varna е `7556227` — съвпадението с първия е случайно и **не се ползва**). **Вход, който НЕ живее в никое git-репо, не може да се адресира по това правило и се пинва по sha256 на прочетените байтове** — това е точно случаят на слоя с петте района (Р21, ИА-О23).
29: 
30: ---
31: 
32: ## 1 · Мярка (всичко мерено 08.09; нула редакции)
33: 
34: ### 1.1 · Състояние на репата
35: 
36: | | стойност | котва |
37: |---|---|---|
38: | `varna_3d` HEAD | `05f485e` · `Petar1984` · 2026-09-07 · „data: p8a quarter assignment ledger 07.09“ | (М) `git -C C:/git/varna_3d log -1 --pretty='%h %an %ad %s' --date=short` |
39: | `varna_3d` клон | `rezhimi` | (М) `git branch --show-current` |
40: | `varna_3d` ahead от `origin/main` | **74** | (М) `git rev-list --count origin/main..HEAD` |
41: | `varna_3d` мръсни проследени | **1** — `scratch/place_bodies/qa_place_bodies.md` | (М) `git status --porcelain \| grep -v '^??'` |
42: | `varna_3d` непроследени | **41** | (М) `git status --porcelain \| grep -c '^??'` |
43: | `varna_3d` `core.autocrlf` / `.gitattributes` | `true` / `* text=auto eol=lf` (Ч `:4`) → **работно копие = блоб** | (М) `git config core.autocrlf`, `git check-attr -a` |
44: | `Fire_Varna` HEAD | **`7556227`** · `Claude Architect` · „docs: decisions draft — kind_registry mapping onto the closed KIND_NORM table …“ | (М) `git log -1 --pretty='%h %an %s'` |
45: | `Fire_Varna` ahead | **138** | (М) `git rev-list --count origin/main..HEAD` |
46: | `Fire_Varna` стейджнати пътища (Б3) | **14** (`M` places/hotels/place_categories/index.html/probe_places_fv.mjs/recall_sweep.py/test_granitsi_fixtures/test_hotels_public_bundle/test_places_public_bundle · `A` b3_g11.py/granitsi_fixtures_07.09.json/granitsi_client_probe.mjs/test_b3_gates.py · `D` granitsi_fixtures_06.09.json) | (М) `git diff --cached --name-status` |
47: | `Fire_Varna` мръсни НЕстейджнати | **3** — `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md`, `scratch/places_search/lot1v_v_reference_manifest.json`, `scratch/places_search/probe_out/token_parity.json` | (М) `git status --porcelain` |
48: | `Fire_Varna` приватностен гейт | `{"scope": 19, "geo_hits": [], "unreadable": [], "stray_new": []}` · **изход 0** | (М) `python gates/probe/b3_g11.py HEAD --cached` |
49: | **`Д1` на диска ДНЕС** | **109 670 B, 536 реда, непроследен, заглавен ред „редакция 2“**; носи **три двойки координати** (М: `grep -nE '4[23]\.[0-9]{4,}\|2[78]\.[0-9]{4,}'` → редове `:104`, `:474`, `:510`) | (М) — затова червен ред 1 има своето единствено изключение и затова съществува ИА-19 |
50: 
51: > Заб.: HEAD-ът на Fire_Varna мърда сам (Петър приема доклади за хидранти). **Нито един гейт и нито един STOP тук не пинва HEAD на Fire_Varna** — само блобове, адресирани по правилото на червен ред 13.
52: 

 succeeded in 514ms:
385: ### 3.Д · `Fire_Varna` — три проследени документа и един игниран файл
386: 
387: | # | път | какво |
388: |---|---|---|
389: | **Д1** | `docs/plans/ПЛАН_Картата_imot_И-А_08.09.md` | **този текст, редакция 4, както го подписва Петър** — записва се на диска на стъпка 2 върху лежащата там редакция 2 (ИА-О22). **Нула координати в текста** (червен ред 5, съди се от ИА-19). |
390: | **Д2** | `docs/decisions/011_kartata_imot.md` | **ред-статус** („И-А изпълнен; тялото и геометрията са в varna_3d; И-Б отворен“) + поправките: **И-D3 (`:17`) — каноничният път става `varna_3d/data/quarters_decisions_imot_2026-09-08.json`** · **И-D2 (`:15`)** `drawn_by` → `null`, `raw_response_sha256` → обявеното съответствие с `provenance.raw_sha256`, `source_terms` от два на **шест** ключа, и изричното потвърждение, че `dictionary_sha256` + `snapshot_date` СА в `_meta` · **И-D4 (`:19`)**: виртуалните родители СА Feature-и (84 = 79 + 5) · **И-D5**: нови редове за архива на v1, за преместеното тяло, за копирания снапшот, **за обръщането на `vinitsa_sever` (Р17)**, **за амандамента на ADR 010 D0/G23 (Р19)** и **за пина по байтове на слоя с районите (Р21)** · **„Последствия“ (`:47`)**: `97,2 %` → **95,90 % за доставката (79 клетки) / 97,18 % при включени обекти**; `:48` „около 18 280 сменят думата“ → измереното **17 982 сменени · 935 изгубени · 9 832 спечелени** (при обявеното правило Р20); площите `61,7 km²` → **61,597 обединение / 66,886 сбор** за v1 и **74,615 / 82,908** за v2. **Статусът остава `Proposed`** (Ч `011:3`). |
391: | **Д3** | `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` | **§21** — „Под-лот И-А затворен“: какво е построено, къде живее, кои гейтове са зелени, какво чака И-Б, входна точка за следващата сесия. **Файлът пристига мръсен; К9 носи и този хънк** (ИА-О19). |
392: | **Д4** | `scratch/boundary_gallery/granitsi_preview_05.09/imot_v2_review_08.09.html` | **пробата за окото на Петър** (§8 т. 3). **ИГНОРИРАН** (М: `.gitignore:64:/scratch/boundary_gallery/`), никога проследен, никога комитван. Изброен ТУК поименно, защото червен ред 4 забранява ДОКОСВАНЕ, не проследеност — без този ред §8 искаше нарушение (кръг 3, ГОЛЯМ). |
393: 
394: **Механичната червена черта:** след всеки от трите комита се пуска `python gates/probe/b3_g11.py HEAD --cached`. Мерено защо това е безопасно: `changed()` (Ч `:70-83`) събира `new` от `git diff --cached --diff-filter=AMR HEAD`, тоест **от ИНДЕКСА срещу новия HEAD** — комитнатият файл вече е в HEAD и не е в дифа, значи `stray_new` остава `[]`, а **`ALLOWED_NEW` (Ч `:40-46`, седем записа; `LEGACY` е `:39`, `GEO` е `:37`) не се пипа**. `inventory()` (Ч `:84-93`) гледа само `data/*.json`, а **обхватът е Ч `:105-106`** (`scope = sorted(set(tracked) | set(f for f in touched if f.lower().endswith((".json", ".geojson"))))`; `tracked` идва от `:98`, `touched` — от `:104`) — **трите документа са `.md` и не влизат в него.** *(Редакции 2 и 3 цитираха `:104-108` и `:109-111`; и двете са грешни — `:109-111` е тялото на цикъла по `scope`. Поправено на двете места, където се ползва: тук и в ИБ-4.)*
395: 
396: ---
397: 
398: ## 4 · Ред на изпълнение
399: 
400: | стъпка | кой | какво | спирачка |
401: |---|---|---|---|
402: | 0 | Изп | Пълната мярка на §1 **без нито една редакция**. Записва OID-ите на 14-те стейджнати пътя (`git ls-files -s -- <14-те>`), деветте изхода Н1–Н9, **16-те идентификатора на тестовете** и **дословно мръсния хънк на Д3**. | разлика = **ИА-STOP 2** |
403: | 1 | **Петър** | **Gate 1** — подписва този план и **двайсет и едното** решения на §9. | без подпис нищо не тръгва |
404: | 2 | Изп | **Записва подписания текст като `Д1`** (върху редакция 2, ИА-О22) → пуска **ИА-19** върху Д1 → `git add -- docs/plans/ПЛАН_Картата_imot_И-А_08.09.md` → комит **К1** → `b3_g11.py HEAD --cached` = 0 | ИА-19 ≠ 0 = **ИА-STOP 17**; b3_g11 ≠ 0 = **ИА-STOP 9** |
405: | 3 | Изп | Копира Ф5, Ф6 в `varna_3d/data/`; прави **единствената** редакция Т1; `git check-ignore -v` за Ф5, Ф6 → **нищо**; `git add -- data/imot_bg_varna_polygons_08.09.geojson data/imot_bg_varna_dictionary_08.09.json .gitignore`. **Не комитва.** | игниран вход = **ИА-STOP 11** |
406: | 4 | **Петър** | Комит **К2** (замразеният вход + `.gitignore` — **и четирите unignore реда, включително този за архива, са в ТОЗИ комит**). | — |
407: | 5 | Изп | Пише Ф1, Ф2, Ф3. Още нищо не се стартира срещу истински данни. | — |
408: | 6 | Изп | Подготвя **Ф7** в `varna_3d/data/`; пуска **ИА-16** (десетте разлики срещу черновия блоб) **без позиционен път** (ИА-О22) и отпечатва sha-то на записаното. `git add -- data/quarters_decisions_imot_2026-09-08.json`. **Не комитва.** | разлика извън списъка = **ИА-STOP 3** |
409: | 7 | **Петър** | Комит **К3** — подписаното тяло. | — |
410: | 8 | Изп | Строи в `%TEMP%/ia_build_a` и `%TEMP%/ia_build_b` → `cmp` (ИА-10). | различни байтове = **ИА-STOP 6** |
411: | 9 | Изп | Пуска Ф2 върху `<tmp>` артефакта: **ИА-1 … ИА-11, ИА-14 … ИА-17**. После **ИА-13 в двете си половини, с `--diff data/quarters_signed.geojson`** — v1 още стои там. **ИА-12 НЕ се пуска тук: командата му сочи архивния път, който още не съществува** (М: `qa_quarters_signed.py:1214-1216` `if not path.exists(): return 1`). | ≠ очакваното = **ИА-STOP 3** |
412: | 10 | Изп | `--make-fixtures --fixtures-dir %TEMP%/ia_fixtures` **върху построения артефакт**. **Причината стъпката да е ТУК е една: преди билда артефакт няма.** *(Не е вярно, че `make_fixtures` мутира документа — `clone()` на `:929-930` е дълбоко копие, М.)* Прогонва всяка фикстура с нейния `--only` и записва **истинския ѝ изходен код** и първия ред от изхода. Двете временни дървета се вдигат и се махат по ИА-О18. | фикстура с изход 0 = **ИА-STOP 5** |
413: | 11 | Изп | Комит **К4** (билдър, гейт, тест). **Фикстури НЕ се комитват** (ИА-О20). | — |
414: | 12 | Изп | Редакции Т2, Т4, Т5, Т7, Т9, Т11, Т13, **Т14**; подготвя **Т15 (двете места)**. `git mv data/quarters_signed.geojson docs/archive/quarters_signed_v1_2026-09-06.geojson`. Копира артефакта от `%TEMP%/ia_build_a` в `data/quarters_signed.geojson`. `git add --` изричните пътища. | — |
415: | 13 | Изп | **Пълният §5 върху новите пътища**: ИА-1 … ИА-19 (сега ИА-12 и ИА-13 сочат `docs/archive/…`) и **Н1′–Н9′**. Произвежда **Д4**. | всяко отклонение = **ИА-STOP 4** |
416: | 14 | Изп | Комит **К5** (кодът + Ф9). **`.gitignore` НЕ е тук** — вече е в К2. | — |
417: | 15 | **Петър** | Комит **К6** — v2 + `git mv` на v1 + `fire_varna_location_inputs.json`. | — |
418: | 16 | Изп | Комит **К7** (предложението за регистъра). | — |
419: | 17 | Изп | Комити **К8** и **К9** във Fire_Varna → **ИА-19 върху Д2 и Д3 преди всеки** → `b3_g11.py HEAD --cached` = 0 след всеки. | ИА-19 ≠ 0 = **ИА-STOP 17**; b3_g11 ≠ 0 = **ИА-STOP 9** |
420: | 18 | Изп | Пуска §5 наново, **отгоре докрай, върху комитнатото състояние**, и записва всеки изход дословно. Проверява `git worktree list` в **двете** репа и `git status --short` — **нула остатъци от `%TEMP%`, нула временни дървета**. | остатък = **ИА-STOP 1** |
421: | 19 | **Одитор** | Независим преглед на дифа срещу този план, ред по ред. | НЕГОДНО = **ИА-STOP 8** |
422: | 20 | **Петър** | §8 локален преглед → **Gate 2** → пуш (varna_3d `rezhimi`, Fire_Varna `main`). | — |
423: 
424: ---
425: 
426: ## 5 · Гейтове
427: 
428: **Кой гейт от кого се изпълнява (обявено, защото кръг 3 намери, че Ф2 „покрива ИА-1…ИА-18“, а две от тях не са в него):**
429: **Ф2** → ИА-1 … ИА-11, ИА-13 … ИА-17. **Старият гейт `src/qa_quarters_signed.py`** → ИА-12. **Ф3 (unittest)** → ИА-18. **Обявена команда с grep** → ИА-19.
430: 
431: **Как се чупи вход.** Четири механики, защото входовете са четири вида:
432: 
433: 1. **Файл на диска** (снапшот, речник, `address_rows`, слоят с районите): счупено копие в `%TEMP%/ia_broken/`, гейтът се вика с път към него.
434: 2. **Блоб на Fire_Varna** (`district_resolutions`, черновата за ИА-16): `git -C C:/git/Fire_Varna worktree add --detach C:/Users/Petar/AppData/Local/Temp/ia_neg_fv HEAD` → счупва се копието ТАМ → `git -C <wt> add -f -- <път>` → **`git -C <wt> -c user.name=… commit`** (детачнат HEAD, дангълинг комит, реалните клонове не мърдат) → гейтът се вика с `--resolutions-repo <wt> --resolutions-rev HEAD` (или `--draft-repo <wt>`) → **задължително** `git -C C:/git/Fire_Varna worktree remove --force <wt> && git -C C:/git/Fire_Varna worktree prune`.
435: 3. **Блоб на varna_3d** (Ф7): **ВТОРО, отделно дърво** `git -C C:/git/varna_3d worktree add --detach C:/Users/Petar/AppData/Local/Temp/ia_neg_v3 HEAD`, същата процедура, `--decisions-repo <wt> --decisions-rev HEAD`, махане с `git -C C:/git/varna_3d worktree remove --force`. **Едно дърво не стига: Ф7 живее във varna_3d и този път просто НЕ СЪЩЕСТВУВА в дърво на Fire_Varna** (кръг 3, БЛОКЕР).
436: 4. **Артефакт** (v2) и **проза** (за ИА-19): счупено копие в `%TEMP%`, гейтът се вика с него.
437: 
438: **Само `git add -f` НЕ стига** — мерено на цитирания образец (Ч `scratch/places_search/qa_night_pins.py:15-20`, `:111`, `:118`, `:171-175`): той доказва проследеност и сверява `worktree_sha256`, **но не подменя съдържание на блоб**. **Никой от тези пътища не е път от write-set-а** (ИА-О18).
439: 
440: **Всяка отрицателна половина се вика така, че да пада по СВОЯТА проверка.** Гейтът приема `--only <ИА-номер>`, който изключва останалите. Всяка се записва с: командата, счупения вход, `--only`, **истинския изходен код** и първия ред от изхода.
441: 
442: | # | гейт | команда · кога | очаквано | отрицателна половина (ТРЯБВА да даде ≠ 0) |
443: |---|---|---|---|---|
444: | **ИА-1** | валидност ПРЕДИ поправка | Ф2, `<артефакт> --tiling …` · стъпки 9, 13, 18 | 0; „95 входни полигона · **0 невалидни преди поправка** · 79 доставяни клетки · **0 невалидни след канонизация**“ (М) | копие на снапшота с пръстен „папийонка“ (самопресичане) → 1 |
445: | **ИА-2** | 0 застъпвания сред клетките · споделени ръбове | Ф2 · 9, 13, 18 | 0; **0 застъпващи се двойки > 0 m² сред 79-те клетки** · **712 споделени отсечки** · **2 849 върха** · **2 137 различни отсечки** (М) | копие на снапшота, в което една клетка е **буферирана с +0,0002°** → застъпване с всеки съсед → 1. (**Не „изместен връх“** — изместване навън прави процеп и гейтът остава 0.) |
446: | **ИА-3** | всеки от 98-те реда има точно един дом | Ф2 · 9, 13, 18 | 0; **98 = 79 Feature + 10 excluded_rows + 6 deferred + 3 no_boundary**; `len(_meta.excluded) == 11`; всяко id от речника точно веднъж; **`_meta.counts` (15 полета) съвпада дума по дума с преброеното**; **84 Feature-а = 79 + 5** | (блоб varna_3d) копие на Ф7 с махнат ред → „id без дом“ → 1; копие на артефакта с ръчно пипнат `counts.cells` → 1; копие с `counts.excluded_rows = 11` → 1 |
447: | **ИА-4** | застъпванията в артефакта са САМО родител–дете | Ф2 · 9, 13, 18 | 0; **17 двойки > 1 m², всичките в `_meta.parent_child`, всяка равна на пълната площ на детето; нула други** (М). Сбор на площите **82,908 km²**, обединение **74,615 km²** | копие на артефакта, в което геометрията на един родител е свита → двойката вече не е „дете ⊆ родител“ → 1 |
448: | **ИА-5** | D8 по конструкция | Ф2 · 9, 13, 18 | 0; всеки от **5**-те родителя е точно обединението на изброените си деца (17 общо), дете ⊆ родител, DAG без цикъл, `parent_child` = **17** двойки | (блоб varna_3d) копие на Ф7 с махнато дете от `children` → „родителят не е обединението“ → 1 |
449: | **ИА-6** | схемата | Ф2 · 9, 13, 18 | 0; **3 върхови ключа · 3 Feature ключа · 41 `properties` ключа** дословно по §1.3; **`_meta` = ЗАТВОРЕНИТЕ 41 имена на §3.Г.8**; **десетте нулирани полета са `null` по всичките 84**; **`rows_without_feature` носи точно кофите `deferred` и `no_boundary`** (ИА-О21) | копие с махнат `wm_polygon_sha256` → 1; копие с добавен `n_pts` в `properties` → 1; копие с добавен 42-ри `_meta` ключ → 1; копие без `snapshot_date` → 1; копие с кофа `alias_of` → 1 |
450: | **ИА-7** | **приватност — САМО файлове с ДАННИ** | Ф2, `--privacy-scope <път>` (в CLI-договора на Ф2, §3.А) · 9, 13, 18 | 0. **Обхватът е ЕДИН път: `Ф7`** — единственият файл с данни, който този лот създава или мени и който е тяло, а не геометрия. **Ф10, Д1, Д2, Д3 са ПРОЗА и са извън обхвата по конструкция — тях ги съди ИА-19** (ИА-О24); `data/quarters_signed.geojson` и `data/imot_bg_varna_polygons_08.09.geojson` са извън обхвата по конструкция — те СА геометрията в частното репо. По имена на ключове: `advert_id, raw_sha256, raw_response_sha256, points, raion_points, localid, cadnum, center, coordinates, geometry, centroid, polygon, bbox` → **0** и **0 float-а в кутията на Варна** (М днес върху блоба `8626ad43…`: 0 и 0; подниз `advert` = 98 от `n_adverts` и НЕ се брои) | копие на `Ф7` с добавен ключ `"advert_id"` → 1; копие на `Ф7` с ключ `"center"` и двойка числа в кутията на Варна → 1 |
451: | **ИА-8** | `source_terms` + атрибуция | Ф2 · 9, 13, 18 | 0; `_meta.source_terms.imot_bg` носи **ТОЧНО трите** ключа `url, recorded_on, position` (Р10; **ИА-О30: отклонение от шесткльчовия образец C9 на v1** — `quote/terms/verdict/checked_on` НЕ се пишат, защото никой не е отварял страницата и датата на „проверка“ би била атестация за нещо, което не се е случило); `len(_meta.licences) == 1`; всеки от 84-те носи непразни `license`, `license_terms`, `license_label`, `attribution` и **`url` == `https://www.imot.bg/obiavi/prodazhbi/grad-varna`** (чистият адрес, §3 ред `url`) | копие с празен `position` → 1; копие с четвърти ключ `checked_on` в `source_terms.imot_bg` → 1; копие с Feature, чийто `license` е голо „CC BY-SA“ → 1; копие, в което `url` носи опашката „(95 with adverts, counts)“ → 1 |
452: | **ИА-9** | **шестте входа са пиннати и сверени по прочетени байтове** | Ф2 · 9, 13, 18 | 0; `_meta.inputs` носи **точно шест** записа (§3.Г.7); блобовите три се четат по `git log -1 --format=%H -- <път>` в СВОЕТО репо; файловите три се хешват от диска; **шестият носи `note` за живота си извън git**. Записва се и мярката „varna_3d е `eol=lf`: работно копие = блоб“ (М) — **доказан капан, не отрицателна половина** | копие на артефакта с подменен `decisions_sha256` → 1; копие на снапшота с един променен байт при непроменен пин → 1; **(блоб Fire_Varna, дърво `ia_neg_fv`) копие на `district_resolutions` с трета резолюция, подадено с `--resolutions-repo/--resolutions-rev` → 1**; копие на слоя с районите с изтрит район → 1 |
453: | **ИА-10** | **два билда → едни байтове** | `Ф1 --out %TEMP%/ia_build_a/q.geojson && Ф1 --out %TEMP%/ia_build_b/q.geojson && cmp` · 8, 13, 18 | `cmp` мълчи, изход 0 | **`%TEMP%/ia_builder_nd.py`** — копие на Ф1 с една стойност от `datetime.now()` — пуснато два пъти → `cmp` → 1. *(„Билд с подменен снапшот“ НЕ е половината на този гейт: по Г.7 подмененият вход спира билда на пина, файл не се пише и `cmp` пада с „No such file“ — доказва пина, не детерминизма.)* |
454: | **ИА-11** | всяка адресна точка отчетена | Ф2, `--address-rows C:/git/Fire_Varna/data/address_rows.json` · 9, 13, 18 | 0; гейтът **преизчислява** и сравнява със записаното в `_meta.mask`: **80 510 = 77 210 (`in_one_cell`) + 1 (`tie_break`, развързан по Р6) + 3 299**; маската е **затворена тройка**: `outside_all_95` **2 274** · `excluded_cell` **1 025** (вътре в някоя от **десетте** изключени клетки; поименно 355/354/274/26/16 и 0 за петте села) · `deferred_cell` **0** (вътре в някоя от **шестте** отложени с вид); `address_rows_sha256` == sha на прочетения блоб (`2a4766bd…`) | копие на артефакта с `mask.in_one_cell` = 77 211 → преизчисленото не съвпада → 1; копие с четвърти клас в маската → „клас извън затворената тройка“ → 1. (**Не „махни клетка“** — точките само се местят и сборът остава 80 510.) |
455: | **ИА-12** | **нерегрес: v1 още се съди от своя гейт** | `python src/qa_quarters_signed.py docs/archive/quarters_signed_v1_2026-09-06.geojson --registry …` · **само 13 и 18** (преди стъпка 12 архивният път не съществува, Ч `qa_quarters_signed.py:1214-1216`) | **0**, същите 20 проверки, същите числа като Н1 | копие на архива с махнат Feature → 1 |
456: | **ИА-13** | **D9 / G15 — дифът, в ДВЕ половини** | (а) `Ф2 <артефакт> --diff <v1>` · (б) същата + `--diff-signed "Р18"`. **`<v1>` = `data/quarters_signed.geojson` на стъпка 9, `docs/archive/quarters_signed_v1_2026-09-06.geojson` на 13 и 18** | (а) **изход 2** и ред „над праговете на D9: **17 982** места > 2 · площ **+21,1 %** > 10 % — иска подпис“ — **това е G15, изпълнен, не отменен, и се записва в ОТЧЕТА като мярка**; (б) **0**, при което `_meta.diff_v1_v2` носи и гейтът **преизмерва**: 60 → **84** Feature · сбор 66,886 → **82,908 km²** · обединение 61,597 → **74,615 km²** · застъпвания **извън `_meta.parent_child`** **40 → 0** · **51 → 17** двойки · **51 общи кода** · **9 изчезващи, поименно** · **33 нови** · покритие **84,85 % → 95,90 %** · по адресна точка **49 397 / 17 982 / 935 / 9 832 / 2 364** при `tie_break_v1 = "азбучно най-малък код"` (Р20) | **половина (а) НЕ е отрицателната половина** — тя е гейт върху истински вход и мястото ѝ е в отчета (червен ред 6). Отрицателната половина е: копие на артефакта, в което едно от деветте изчезващи имена липсва от списъка → 1 при (б); и копие с `tie_break_v1` = друг низ при непроменени числа → 1 |
457: | **ИА-14** | регистърът и видовете | Ф2 · 9, 13, 18 | 0; **всеки от 84-те кода е или в регистъра (84 записа), или поименно в `_meta.registry_pending_new` (28)**; `_meta.registry_pending` == `set(registry) − 84-те` (**28**); **четирите жилищни кода без Feature (`druzhba, rozova_dolina, sv_ivan_rilski, trakia`) са изброени поименно с довод** (ИА-О17); **`kind` на всеки от 84-те е ключ на `KIND_NORM`** (М: 84/84); **`"TBD"` като код = червено; нула повтарящи се кодове** | копие с върнат `"code": "TBD"` → 1; копие с два реда на един код → 1; копие с код нито в регистъра, нито в `registry_pending_new` → 1; копие с `kind: "обект"` → 1; копие с `kind: "район"` (суровият imot-вид) → 1 |
458: | **ИА-15** | районът | Ф2 · 9, 13, 18 | 0; всичките 84 имат `district` от затворената петорка; **0 клетки „да“ без район** (М); `_meta.district_witness_disputes` носи **точно 5** реда (`vazrazhdane4, kochmar, so_planova, salzitsa` с `delivered: true`; `pristanishte_varna` с `delivered: false`), първите два със `resolution: "petar_agkk"` от блоба `d494d4d256ae…`, следващите два с `"pending_petar"`; `perchemliyata` носи `fire_varna_district` и бележка към подписаната резерва (Ч `qa_place_zone_aliases.py:74`); **знаменателят на свидетеля е 82 = 77 + 5**, а по доставяните клетки — **74 съгласия от 78** | копие с изтрит ред от `district_witness_disputes` → 1; копие с `district` извън петорката → 1; копие с `delivered: true` за `pristanishte_varna` → 1 |
459: | **ИА-16** | **`Ф7` срещу черновия блоб** | `Ф2 --decisions-diff --draft-repo C:/git/Fire_Varna --draft-path scratch/places_search/imot_decisions_1_2026-09-08_draft.json` — **без позиционен път** (ИА-О22) · 6, 13, 18 | 0; ревизията се намира с `git log -1 --format=%H -- <път>` (**`7556227…`**), sha-то на блоба е **`8626ad43…`**, 51 275 B; дифът е **точно десетте разлики Х1–Х10, нула други**; отпечатва sha на `Ф7` за Gate 2 | (блоб Fire_Varna, дърво `ia_neg_fv`) копие на черновата с единайсета разлика → 1; копие, в което Х4 е върнато на `"TBD"` → 1 |
460: | **ИА-17** | **изключените редове** | Ф2 · 9, 13, 18 | 0; `_meta.excluded` носи **11** записа **с петорката на v1 `{code, display, kind, registry_action, why}` + `delivered`** (ИА-О30: никакъв ключ `reason` — доводът живее в `why`, както старият C7 го съди, Ч `qa_quarters_signed.py:320-322`): **десетте с `kind_registry = null`, всеки с `delivered: false` и `why` = дословният `kind_note`**, плюс **един със `status: "reinstated"`, `delivered: true`** (`vinitsa_sever`, старият довод дословно в `why`, „Р17“). **Биекция: `kind_registry = null` ⇔ запис с `delivered: false`.** Запис с `delivered: true` иска ред в `_meta.declared_deviations` | копие на артефакта с махнат ред от `excluded` → „ред с null вид без запис“ → 1; копие без реда `vinitsa_sever` → „подписано изключване обърнато без запис“ → 1; копие с `delivered: true` без ред в `declared_deviations` → 1 |
461: | **ИА-18** | **мета-гейт: половините са тичали** | `python -m unittest discover -s tests` (частта `test_quarters_signed_imot_fixtures.py`) · 13, 18 | 0; тестът **ражда фикстурите в `%TEMP%/ia_fixtures`** и **прогонва всяка** с нейния `--only`, настоявайки за изход ≠ 0 **по своя номер** | фикстура, нарочно направена валидна → тестът пада → 1 |
462: | **ИА-19** | **прозата не носи координати** | `grep -nE '\b(4[23]\|2[78])[.,][0-9]{3,}\b' docs/plans/ПЛАН_Картата_imot_И-А_08.09.md docs/decisions/011_kartata_imot.md docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` · **преди К1, преди К8, преди К9, и на 18** | **0 попадения** (`grep` изход 1 = няма съвпадение = ЗЕЛЕНО; изход 0 = ЧЕРВЕНО; **ИА-STOP 17 се задейства при изход 0**). Изразът хваща и **българската десетична запетая** (ИА-О30, кръг 5: ширина, записана с запетая, е координата колкото записаната с точка) и три и повече знака след разделителя. Обхватът е **само трите проследени `.md` на този лот**; Д4 е игниран и не се съди. М (Архитект, 08.09 нощ, след изчистването в `146beac`): **0** попадения и в трите | копие на Д1 в `%TEMP%/ia_docs/` с една добавена двойка координати с ТОЧКА → `grep` намира → **ИА-19 червен**; второ копие с двойка със ЗАПЕТАЯ → **червен**. **Двете половини са задължителни: доказват, че изразът хваща и двете нотации** |
463: 
464: **Н1′–Н9′ · нерегрес на базата** — командите **се менят на стъпка 12**, изходите **не**:
465: 
466: | # | команда ПРЕДИ стъпка 12 | команда СЛЕД стъпка 12 | изход |
467: |---|---|---|---|
468: | Н1′ | `qa_quarters_signed.py data/quarters_signed.geojson --registry …` | **`qa_quarters_signed.py docs/archive/quarters_signed_v1_2026-09-06.geojson --registry …`** (= ИА-12) | **0** |
469: | Н2′ | `qa_p8a.py --ledger …` | същата (пътят е по подразбиране, пренасочен от Т7) | **0** |
470: | Н3′–Н6′ | четирите гейта | същите (константите пренасочени от Т9, Т11) | **0** ×4 |
471: | Н7′ | `unittest discover -s tests` | същата; сверява се по **16-те идентификатора**, не по броя | **0** |
472: | Н8′ | `qa_fire_varna_m6.py` | същата | **3**, същите **8** реда |
473: | Н9′ | `scratch/granitsi/zone_alias_negatives.py` | същата (харнесът П13, пренасочен от Т14) | **0** |
474: 
475: ---
476: 

codex
Планът вече описва проверка и за координати с десетична запетая. Проверявам дали тя спира при грешка на самата команда и дали комитите запазват непокътнат стейджнатия Б3. Текущият HEAD е `b07b8ba`, а част от началните мерки в плана още сочат по-ранно състояние.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Картата_imot_И-А_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 398..425 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 489ms:
398: ## 4 · Ред на изпълнение
399: 
400: | стъпка | кой | какво | спирачка |
401: |---|---|---|---|
402: | 0 | Изп | Пълната мярка на §1 **без нито една редакция**. Записва OID-ите на 14-те стейджнати пътя (`git ls-files -s -- <14-те>`), деветте изхода Н1–Н9, **16-те идентификатора на тестовете** и **дословно мръсния хънк на Д3**. | разлика = **ИА-STOP 2** |
403: | 1 | **Петър** | **Gate 1** — подписва този план и **двайсет и едното** решения на §9. | без подпис нищо не тръгва |
404: | 2 | Изп | **Записва подписания текст като `Д1`** (върху редакция 2, ИА-О22) → пуска **ИА-19** върху Д1 → `git add -- docs/plans/ПЛАН_Картата_imot_И-А_08.09.md` → комит **К1** → `b3_g11.py HEAD --cached` = 0 | ИА-19 ≠ 0 = **ИА-STOP 17**; b3_g11 ≠ 0 = **ИА-STOP 9** |
405: | 3 | Изп | Копира Ф5, Ф6 в `varna_3d/data/`; прави **единствената** редакция Т1; `git check-ignore -v` за Ф5, Ф6 → **нищо**; `git add -- data/imot_bg_varna_polygons_08.09.geojson data/imot_bg_varna_dictionary_08.09.json .gitignore`. **Не комитва.** | игниран вход = **ИА-STOP 11** |
406: | 4 | **Петър** | Комит **К2** (замразеният вход + `.gitignore` — **и четирите unignore реда, включително този за архива, са в ТОЗИ комит**). | — |
407: | 5 | Изп | Пише Ф1, Ф2, Ф3. Още нищо не се стартира срещу истински данни. | — |
408: | 6 | Изп | Подготвя **Ф7** в `varna_3d/data/`; пуска **ИА-16** (десетте разлики срещу черновия блоб) **без позиционен път** (ИА-О22) и отпечатва sha-то на записаното. `git add -- data/quarters_decisions_imot_2026-09-08.json`. **Не комитва.** | разлика извън списъка = **ИА-STOP 3** |
409: | 7 | **Петър** | Комит **К3** — подписаното тяло. | — |
410: | 8 | Изп | Строи в `%TEMP%/ia_build_a` и `%TEMP%/ia_build_b` → `cmp` (ИА-10). | различни байтове = **ИА-STOP 6** |
411: | 9 | Изп | Пуска Ф2 върху `<tmp>` артефакта: **ИА-1 … ИА-11, ИА-14 … ИА-17**. После **ИА-13 в двете си половини, с `--diff data/quarters_signed.geojson`** — v1 още стои там. **ИА-12 НЕ се пуска тук: командата му сочи архивния път, който още не съществува** (М: `qa_quarters_signed.py:1214-1216` `if not path.exists(): return 1`). | ≠ очакваното = **ИА-STOP 3** |
412: | 10 | Изп | `--make-fixtures --fixtures-dir %TEMP%/ia_fixtures` **върху построения артефакт**. **Причината стъпката да е ТУК е една: преди билда артефакт няма.** *(Не е вярно, че `make_fixtures` мутира документа — `clone()` на `:929-930` е дълбоко копие, М.)* Прогонва всяка фикстура с нейния `--only` и записва **истинския ѝ изходен код** и първия ред от изхода. Двете временни дървета се вдигат и се махат по ИА-О18. | фикстура с изход 0 = **ИА-STOP 5** |
413: | 11 | Изп | Комит **К4** (билдър, гейт, тест). **Фикстури НЕ се комитват** (ИА-О20). | — |
414: | 12 | Изп | Редакции Т2, Т4, Т5, Т7, Т9, Т11, Т13, **Т14**; подготвя **Т15 (двете места)**. `git mv data/quarters_signed.geojson docs/archive/quarters_signed_v1_2026-09-06.geojson`. Копира артефакта от `%TEMP%/ia_build_a` в `data/quarters_signed.geojson`. `git add --` изричните пътища. | — |
415: | 13 | Изп | **Пълният §5 върху новите пътища**: ИА-1 … ИА-19 (сега ИА-12 и ИА-13 сочат `docs/archive/…`) и **Н1′–Н9′**. Произвежда **Д4**. | всяко отклонение = **ИА-STOP 4** |
416: | 14 | Изп | Комит **К5** (кодът + Ф9). **`.gitignore` НЕ е тук** — вече е в К2. | — |
417: | 15 | **Петър** | Комит **К6** — v2 + `git mv` на v1 + `fire_varna_location_inputs.json`. | — |
418: | 16 | Изп | Комит **К7** (предложението за регистъра). | — |
419: | 17 | Изп | Комити **К8** и **К9** във Fire_Varna → **ИА-19 върху Д2 и Д3 преди всеки** → `b3_g11.py HEAD --cached` = 0 след всеки. | ИА-19 ≠ 0 = **ИА-STOP 17**; b3_g11 ≠ 0 = **ИА-STOP 9** |
420: | 18 | Изп | Пуска §5 наново, **отгоре докрай, върху комитнатото състояние**, и записва всеки изход дословно. Проверява `git worktree list` в **двете** репа и `git status --short` — **нула остатъци от `%TEMP%`, нула временни дървета**. | остатък = **ИА-STOP 1** |
421: | 19 | **Одитор** | Независим преглед на дифа срещу този план, ред по ред. | НЕГОДНО = **ИА-STOP 8** |
422: | 20 | **Петър** | §8 локален преглед → **Gate 2** → пуш (varna_3d `rezhimi`, Fire_Varna `main`). | — |
423: 
424: ---
425: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Картата_imot_И-А_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 477..546 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 510ms:
477: ## 6 · Комити
478: 
479: **Идентичности** (ADR 010 D16, Ч `010:68`): `Claude Executor <executor@local>` за код и документи; `Petar1984 <petar.dikov2019@gmail.com>` за данни, геометрия и подписи.
480: 
481: **Задължителната двойка команди** (мерено: `git commit -m "…" -- b.txt` върху непроследен файл дава `error: pathspec … did not match any file(s) known to git`, **изход 1**; след `git add -- b.txt` същият комит минава с изход 0):
482: 
483: ```
484: git add -- <изричните пътища>
485: git -c user.name="Claude Executor" -c user.email="executor@local" \
486:     commit -m "<точното съобщение>" -- <изричните пътища>
487: ```
488: 
489: Никакъв `git add -A`, никакъв `git add .`, никакъв `--no-verify`. Всяко съобщение завършва с реда `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`. Тема **≤ 72 знака** (Ч `varna_3d/AGENTS.md:160`), **на английски, без кирилица** — дължините са премерени поименно (М).
490: 
491: | # | стъпка | репо / ръка | съобщение (дословно) | зн. (М) | пътища |
492: |---|---|---|---|---|---|
493: | **К1** | 2 | Fire_Varna · Изп | `docs(plan): sub-lot I-A plan for the imot.bg tiling` | **51** | `docs/plans/ПЛАН_Картата_imot_И-А_08.09.md` |
494: | **К2** | 4 | varna_3d · **Петър** | `data: frozen imot.bg tiling snapshot 08.09, 95 polygons` | **55** | `data/imot_bg_varna_polygons_08.09.geojson`, `data/imot_bg_varna_dictionary_08.09.json`, `.gitignore` (**и четирите unignore реда**) |
495: | **К3** | 7 | varna_3d · **Петър** | `data: signed decisions for the imot.bg tiling` | **45** | `data/quarters_decisions_imot_2026-09-08.json` |
496: | **К4** | 11 | varna_3d · Изп | `feat(quarters): imot.bg tiling builder and its own gate` | **55** | `src/build_quarters_signed_imot.py`, `src/qa_quarters_signed_imot.py`, `tests/test_quarters_signed_imot_fixtures.py` — **без фикстури** (ИА-О20) |
497: | **К5** | 14 | varna_3d · Изп | `chore(quarters): v1 readers follow it to docs/archive` | **53** | `src/fire_varna_locations.py`, `src/qa_fire_varna_places_export.py`, `src/qa_p8a.py`, `src/qa_place_zone_aliases.py`, `tests/test_quarters_signed_fixtures.py`, `scratch/granitsi/zone_alias_negatives.py`, `docs/archive/РЕГИСТЪР_архив.md` |
498: | **К6** | 15 | varna_3d · **Петър** | `data: quarters_signed v2; v1 archived, never deleted` | **52** | `data/quarters_signed.geojson`, `docs/archive/quarters_signed_v1_2026-09-06.geojson` (`git mv`), `data/fire_varna_location_inputs.json` |
499: | **К7** | 16 | varna_3d · Изп | `docs: registry proposal for 28 codes outside the registry` | **57** | `docs/decisions/ПРЕДЛОЖЕНИЕ_регистър_imot_08.09.md` |
500: | **К8** | 17 | Fire_Varna · Изп | `docs(adr): ADR 011 status line and the 08.09 corrections` | **56** | `docs/decisions/011_kartata_imot.md` |
501: | **К9** | 17 | Fire_Varna · Изп | `docs(state): section 21 - sub-lot I-A closed, I-B open` | **54** | `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` (**носи и мръсния хънк на §20 — ИА-О19**) |
502: 
503: **Няма капан на реда.** В И-А **нито един sha на v2 не се пинва в код** — всичките осемнайсет пина гледат v1 по непроменените си стойности. Затова К5 може да предхожда К6, а К6 не иска препинване след себе си. Пинът на решенията живее в `_meta.decisions_sha256` и се сверява **по време на прогона** срещу блоба, не като литерал в код (Р9).
504: 
505: **Следпроверка след всеки комит:** `git status --short` (само планираните пътища), `git log -1 --pretty='%h %an %s'` (правилната ръка), `git log -1 --pretty=%s | awk '{print length}'` ≤ 72; за Fire_Varna — `python gates/probe/b3_g11.py HEAD --cached` = 0.
506: 
507: **Котвата за стейджнатия Б3.** OID-ите на 14-те пътя се записват на стъпка 0 и се сверяват след К1, К8 и К9. **В И-А те не мърдат нито веднъж.** Разлика = **ИА-STOP 7**.
508: 
509: ---
510: 
511: ## 7 · STOP
512: 
513: | # | условие | действие |
514: |---|---|---|
515: | **ИА-STOP 1** | пипнат е път извън §3, **или е останал ефемерен път/временно дърво след стъпка 18** (пътищата под `%TEMP%` по ИА-О18 НЕ са пътища от write-set-а, докато лотът тече) | спри, покажи `git status --short` и `git worktree list` за двете репа, питай |
516: | **ИА-STOP 2** | някой от Н1–Н9, 16-те идентификатора или мръсният хънк на Д3 се различават на стъпка 0 | спри — базата не е тази, за която е писан планът |
517: | **ИА-STOP 3** | Ф2 или ИА-16 дават изход, различен от очаквания в §5 (за ИА-13 очакваното е **2** без подпис и **0** с него), и находката НЕ е в §9 | спри, покажи находките дословно |
518: | **ИА-STOP 4** | някой от Н1′–Н9′ сменя изхода си (вкл. броя 8 на Н8′) | спри — регресия |
519: | **ИА-STOP 5** | обявена отрицателна половина **не падна** (изход 0), или падна с чужд номер въпреки `--only` | спри — по червен ред 6 това е по-лошо от липсващ гейт |
520: | **ИА-STOP 6** | двата билда не са байт-еднакви | спри — билдът не е детерминиран |
521: | **ИА-STOP 7** | OID на някой от 14-те стейджнати пътя на Fire_Varna се е сменил | спри — доставката Б3 е пипната |
522: | **ИА-STOP 8** | одиторът връща НЕГОДНО | спри, върни се при Петър |
523: | **ИА-STOP 9** | `b3_g11.py HEAD --cached` ≠ 0 след Fire_Varna комит | спри — приватностният гейт е червен |
524: | **ИА-STOP 10** | измерено число се разминава с §1 | спри и питай — **не** „поправяй“ числото в плана |
525: | **ИА-STOP 11** | `git check-ignore` показва, че някой от Ф5, Ф6, Ф7, Ф8 е игниран след Т1 | спри — архив и вход, които git не вижда, не са архив и вход |
526: | **ИА-STOP 12** | иска се `git rm`, `git checkout`, `git stash`, `git reset` или изтриване на подписано тяло | спри — никога |
527: | **ИА-STOP 13** | появи се нужда от ред в `Fire_Varna/index.html`, `data/`, `tests/`, `gates/`, или в **пети** път на Fire_Varna извън Д1–Д4 | спри — това е И-Б |
528: | **ИА-STOP 14** | появи се нужда от ред в `Varna_buildings` | спри — това е ръката на Петър по D14 |
529: | **ИА-STOP 15** | Петър не е подписал някое от **двайсет и едното** решения на §9 | спри — не се подразбира |
530: | **ИА-STOP 16** | блобът на черновата вече не е `8626ad43…`, **или** блобът на `district_resolutions_2026-09-07.json` вече не е `d494d4d256ae…`, **или** sha на слоя с районите вече не е `26e39b00…` | спри — основата на Ф7 или решаващ вход се е сменил |
531: | **ИА-STOP 17** | ИА-19 намери координатна двойка в Д1, Д2 или Д3 | спри — червен ред 5 е нарушен в проследен файл на публично репо |
532: 
533: ---
534: 
535: ## 8 · Локален преглед (кои проби гледа Петър)
536: 
537: Всички проби са **в игнорираната папка** на Fire_Varna и не пътуват никъде:
538: 
539: 1. `scratch/boundary_gallery/granitsi_preview_05.09/imot_city_08.09.html` — **95-те полигона**. На око: Чайка, Левски, Владиславово, Аспарухово, Галата седят там, където Петър ги очаква.
540: 2. `…/imot_decisions_sign_08.09.html` — **страницата за подпис**: 98-те реда с `include`, кода, вида, **`kind_registry`** и района. Тук се вземат Р2–Р5, Р7, Р15, Р16, Р17.
541: 3. **Д4** — `…/imot_v2_review_08.09.html`, произведен от Изпълнителя на стъпка 13 (**обявен поименно в §3.Д, игниран, никога проследен**): **84-те Feature-а** върху подложката, оцветени клетка/родител, **плюс 3 299-те точки на маската** в два цвята (2 274 `outside_all_95` и 1 025 `excluded_cell`), **плюс деветте изчезващи имена** върху старите им места и **935-те адреса, които губят дума**.
542: 4. Извадка от **6 конкретни места** за сверка на око (правилото „примери за поправка“): `avtogara` (район→кв, Р15) · двойката на общия ръб `chaika_kk` / `alen_mak` (Р6) · `perchemliyata` (единственият „да“ без свидетел АГКК) · `so_planova` и `salzitsa` (двата нови спора) · **`vinitsa_sever`** (изключеният от 07.09, който v2 връща — Р17) · **`pobeda_group`** (единственият виртуален родител, който v1 не познава, и единственият вид без извор — Р16).
543: 5. **Живата карта НЕ се пипа и НЕ се гледа** — тя е на старите данни; това е И-Б.
544: 
545: ---
546: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Картата_imot_И-А_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 94..147 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 494ms:
94: ### 1.4 · Замразеният снапшот на imot.bg (входът)
95: 
96: | | стойност | котва |
97: |---|---|---|
98: | `imot_bg_varna_polygons_08.09.geojson` | 175 736 B · sha256 `77b405640000a304ec5dca94f4865cc1b5a4d552c0edfc4847fa4663e6662a1f` | (М) |
99: | `imot_bg_varna_dictionary_08.09.json` | 6 274 B · sha256 **`feba76e3c816a3e313d8ace0dcb373b4a1ee4ecb9b6356a122254d4846d22fdf`** · списък от **98** `{id, name}` | (М) |
100: | `_meta` на снапшота | 12 ключа: `crs, dictionary_endpoint, dictionary_missing_polygons, dictionary_n, dictionary_sha256, fetched, list_endpoint, missing, n, raw_kept, source, tools`; `fetched = "2026-09-08"`, `n = 95`, `missing = []`, `dictionary_n = 98` | (М) |
101: | **`_meta.list_endpoint` — ДОСЛОВНО** | **`https://www.imot.bg/obiavi/prodazhbi/grad-varna (95 with adverts, counts)`** — **с опашката**. **`url` в артефакта = точно този низ** (Р10) | (М) |
102: | **`_meta.dictionary_sha256` ВЪТРЕ в снапшота** | **`6fa3b07007203c5a5787d0af3e0d63c03d3a625dd741ab34c8dabe1965cbf38f`** — **НЕ е** sha на файла-речник. Това е хешът на **суровия отговор** на `dictionary_endpoint` (`https://api.imot.bg/mob_api/dictionary/search/1?town=5`), а суровият отговор е „scratchpad (private), not in the repo“ (Ч `_meta.raw_kept`). **Авторитетът за гейта е sha-то на ФАЙЛА (`feba76e3…`); вграденото число се записва като свидетел, който никой не сверява.** | (М) |
103: | Feature-и | **95**, всички `Polygon`, по 1 пръстен | (М) |
104: | свойства на Feature | `center, fetched, n_adverts, n_pts, name, provenance, raion, raion_num, slug, src`; `provenance = {endpoint, advert_id, raw_sha256, raw_bytes, fetched_local, field}` — **низът `raw_response_sha256` се среща 0 пъти**; `properties.fetched` има **една** стойност `"2026-09-08"` | (М) |
105: | **знаци след точката — ПОПРАВЕНО** | **7 640 числа** в `coordinates`, хистограма **{5: 7, 6: 53, 7: 642, 8: 6938}** — **кофа с 2 знака НЯМА**. (Контрола: 7 640 / 2 = **3 820** = сборът на `n_pts` в тялото с решенията.) *(Редакция 3 казваше „2, 5, 6, 7, 8 · 1/19/195/653/6963“ — нито едно от петте числа не съвпада; оборено и заменено.)* | (М) |
106: | и двата файла | **игнорирани** — `.gitignore:64:/scratch/boundary_gallery/` | (М) `git check-ignore -v` |
107: 
108: **Върху 79-те доставяни клетки (не върху 95-те), след канонизацията по D1:** **0 невалидни преди поправка** · **0 невалидни след канонизация** · **0 застъпващи се двойки с площ > 0** · **2 849 върха** · **2 137 различни отсечки** · **712 споделени отсечки** · дължина на ръба (EPSG:32635): медиана **96,5 m**, средна **130,4**, p10 **37,0**, p90 **257,5**, max **1 484,3**, min **8,92** · площ **74,615 km²** (М; редакция 3 даваше p10 37,1 / p90 257,4 / min 8,97 — премерено наново върху канонизираните клетки).
109: 
110: ### 1.5 · Адресните точки — маската, затворена и сверена
111: 
112: `Fire_Varna/data/address_rows.json`: **80 510** реда, `coordinate_order = "[lat,lng]"`, 5 073 137 B, sha256 **`2a4766bd474f34817081e2d4e49b0ab2abbe54080c809b0402e079e1b9a0904a`** (М, върху **блоба** на HEAD).
113: 
114: | клас (затворен набор от 3, плюс двата отчетни) | брой | котва |
115: |---|---|---|
116: | **`in_one_cell`** — в точно една клетка „да“ (канонизирани) | **77 210** | (М) |
117: | **`tie_break`** — на общия ръб на две клетки „да“ | **1** — една точка в район Приморски **(координата в частния файл)**, между **5055 `chaika_kk`** и **5053 `alen_mak`** | (М) |
118: | **М1 · `outside_all_95`** — извън всичките 95 полигона | **2 274** | (М) |
119: | **М2 · `excluded_cell`** — вътре в клетка, **която v2 изключва: десетте реда с `kind_registry = null` (петте „обекта“ И петте села)** | **1 025** = `pristanishte_varna` 355 · `biznes_hotel` 354 · `grand_mol` 274 · `biznes_park_varna` 26 · `letishte` 16 · петте села **0** | (М) |
120: | **М3 · `deferred_cell`** — вътре в **отложена клетка С ВИД** (шестте: `pz_topoli`, `vz_zvezditsa`, `krushkite`, `lazur`, `orehcheto`, `pripek`) | **0** | (М) |
121: | **сбор** | 77 210 + 1 + **3 299** = **80 510** | (М) |
122: 
123: > **Дефиницията, поправена след кръг 3:** `excluded_cell` покрива **десет** клетки, не пет — точно клетките, чиито редове отиват в `_meta.excluded` по §3.Г.1; `deferred_cell` покрива **шест** — точно клетките в `rows_without_feature.deferred`. Числово нищо не се мени (селата и отложените хващат 0 точки), но **дефиницията в §1.5 и дефиницията в §3.Г.1 вече са една и съща**, иначе ИА-11 не може да бъде написан еднозначно. Полето `mask.in_cell` от отрицателната половина на стар ИА-11 **не съществува** и е махнато; закотвените имена са `in_one_cell`, `tie_break`, `outside_all_95`, `excluded_cell`, `deferred_cell`, `address_rows_sha256`, `outside_note`, `tie_break_rule`.
124: 
125: - **Покритие на доставката: 77 211 / 80 510 = 95,90 %.** Ако петте „обекта“ влязат: 78 236 = **97,18 %** — това и е числото „97,2 %“ в ADR 011 (Ч `011_kartata_imot.md:47`). Двете се поправят в комит К8.
126: - **Дифът v1 → v2 по адресна точка — ПОПРАВЕН и възпроизводим.** Кръг 3 обори двойката „49 926 / 17 453“: тя не следва от никое обявено правило, защото **4 517 от 80 510-те точки попадат в ≥ 2 полигона на v1** (М), а правило за развръзка на страната v1 нямаше. **Обявено правило (Р20): за v1 печели азбучно най-малкият код; за v2 — най-малкият `raion_num` (Р6).** При него (М): същата дума **49 397** · сменена **17 982** · изгубена **935** · спечелена **9 832** · без дума и преди, и сега **2 364**. Сборът е 80 510; 49 397 + 17 982 + 935 = **68 314** (v1) ✔; 49 397 + 17 982 + 9 832 = **77 211** (v2) ✔. Правилото се записва дословно в `_meta.diff_v1_v2.tie_break_v1` и се преизмерва от ИА-13.
127: - Речникът на ADR 011 за М1 („порт, промзона, село, грешна координата“, Ч `011:47`) се записва в `_meta.mask.outside_note` **дословно**; той е бележка, не клас, и никой гейт не го съди.
128: 
129: ### 1.6 · Тялото с решенията (черновата днес, **след комит 7556227**)
130: 
131: `Fire_Varna/scratch/places_search/imot_decisions_1_2026-09-08_draft.json` — **проследен и чист**. Стабилна ревизия: `git log -1 --format=%H -- <път>` → **`755622726bac3e8b977f9fd484b2e2d164661267`** (`Claude Architect`). **Блоб `sha256 = 8626ad43aea7a02d132f1e16ccc3b755ab782a87773d55f83eab51fc348fcaf8`, 51 275 B** (М).
132: 
133: - Върхови ключове: `_meta`, `rows`, `virtual_parents`. **`_meta` — 9 ключа** (М): `what, snapshot, dictionary_n, polygons, rule, signed_by, privacy, kind_registry_rule, decisions_open`.
134: - **98 реда, 16 ключа** (М): `area_km2, buildings, cls, code, code_src, district_agkk, imot_name, include, kind, kind_note, kind_registry, n_adverts, n_pts, parent, raion_num, slug`. **Няма ключ `display`.**
135: - `include` (М): **79 „да“ · 11 „отложено (0 сгради)“ · 5 „решение“ · 3 „решение (няма полигон…)“**.
136: - **`_meta.kind_registry_rule` — дословно** (Ч): „imot вид → вид от затворената таблица `KIND_NORM` (`varna_3d/src/fire_varna_locations.py:150-154`): `кв.→кв` · `ж.к./подрайон→жк` · `район→кв` (**ДА СЕ ПОДПИШЕ**; алтернатива `мр`) · `м-т→м-т` (клас locality) · `к.к.→кк` · `в.з.→вз` · промишлена зона→`пз` · Метро/Завод Дружба→`зона` · с./обект → без вид (не влизат в v2)“. **Котвата `:150-154` е ГРЕШНА** (М: `git grep -n KIND_NORM` → `src/fire_varna_locations.py:152`; таблицата е `:152-155`) — поправя се в самото тяло с разлика **Х9**, не само в плана.
137: - **`_meta.decisions_open` — 7 отворени решения** (Ч, дословно): „район→кв или мр“ · „5 обекта: точка/alias, не клетка“ · „3 района без полигон: чакане/ръчно/no_boundary“ · „11 отложени (0 сгради)“ · „**13** без район по АГКК → район по решение“ · „precision_m за плочката“ · „низът за атрибуция“. **Числото 13 е ГРЕШНО** (М: редовете без `district_agkk` са **16** = 98 − 82) — поправя се в тялото с разлика **Х10**. **Всичките седем са покрити от §9** (Р15/Р16 · Р3 · Р4 · Р7 · Р14 · Р8 · Р10).
138: - **`kind_registry` по 98-те реда** (М): `кв 34 · м-т 31 · жк 10 · пз 5 · кк 4 · зона 2 · вз 2 · **null 10**`.
139: - **`kind_registry` по 79-те „да“** (М): `кв 32 · м-т 27 · жк 10 · кк 4 · пз 3 · зона 2 · вз 1` = 79. **Нула стойности извън `KIND_NORM`.** (Суровият imot-вид по същите 79 е `м-т 27 · район 19 · кв. 13 · ж.к./подрайон 10 · зона 5 · к.к. 4 · в.з. 1` — 46 от тях са извън `KIND_NORM`; **точно това преобразуване е решено в самия файл, не се измисля от Изпълнителя**.)
140: - **Десетте реда с `kind_registry = null`** (М, поименно, с довода от `kind_note`): пет **обекта** — 5841 `biznes_park_varna`, 6183 `biznes_hotel`, 5847 `grand_mol`, 6134 `letishte`, 5864 `pristanishte_varna` („обект: не е клетка → без вид“); пет **села** — 740 `zvezditsa`, 751 `kazashko`, 755 `kamenar`, 764 `konstantinovo`, 821 `topoli` („село: няма вид в `KIND_NORM` → отложено“). **Null вид ⇔ ред в `_meta.excluded` с `delivered: false`: не влиза в v2 и се изброява поименно с довода си.**
141: - **Деветте НЕдоставяни реда С ВИД** (М): шест отложени — 6293 `pz_topoli`(пз), 6296 `vz_zvezditsa`(вз), 6299 `krushkite`, 6300 `lazur`, 6301 `orehcheto`, 6302 `pripek` (м-т); три без полигон — 5848 (кв), 6294 `malka_chaika` (кв), 5866 (пз). 79 + 10 + 9 = **98** ✔
142: - **`virtual_parents` е ОТДЕЛЕН списък от 5**, всеки `{code, name, kind, children}`; **нито един от петте не е ред в `rows`** (М). Децата са **17**, всичките `include = "да"` (М): `kv_levski` 4 (`bazar_levski, levski1, levski2, tsveten_kvartal`) · `vladislavovo` 5 (`vladislav_varnenchik1, vladislav_varnenchik2, kaisieva, pz_planova, bokluk_tarla`) · `vazrazhdane` 4 · `mladost` 2 · `pobeda_group` 2 (`konfuto, pobeda`).
143: - **Петте `virtual_parents` НЯМАТ `kind_registry`**; полето им `kind` е прозата „виртуален родител = обединение на децата“ (М). Дупката се запълва **без измисляне**: четирите вече съществуват в **подписания регистър** — `kv_levski → кв`, `vladislavovo → кв`, `vazrazhdane → жк`, `mladost → жк` (М: и регистърът, и v1 дават същото); само `pobeda_group` няма ред никъде и е **решение Р16** (предложение `кв` — двете му деца са `кв`).
144: - **97 различни кода за 98 реда** — `"TBD"` два пъти: 5848 „Електроразпределение Варна“ и 5866 „Северна промишлена зона“ (М). **След Х4: 98 различни в `rows`; с петте виртуални родителя — 103 различни в цялото тяло; доставяни — 84.**
145: - **Приватност (М, върху БЛОБА `8626ad43…`, по имена на ключове):** `advert_id, raw_sha256, raw_response_sha256, points, raion_points, localid, cadnum, center, coordinates, geometry, centroid, polygon, bbox` → **по 0 попадения**; float-ове в кутията на Варна → **0**. Подниз `advert` → **98**, всичките от `n_adverts` — затова сканът е **закотвен по име на ключ**.
146: - **Остава производно на частната геометрия:** `n_pts` (98 реда, сбор **3 820**) и `area_km2` (**95** реда) — вж. ИА-О9 и ИБ-15.
147: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Картата_imot_И-А_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 219..251 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 489ms:
219: ## 2 · Обявени отклонения
220: 
221: | № | Отклонение | Защо |
222: |---|---|---|
223: | **ИА-О1** | **Планът v4 СЪЩЕСТВУВА** (156 024 B, 735 реда, непроследен) и е суровината на този под-лот. | STOP по „измерено число се разминава“ важи първо за §2. |
224: | **ИА-О2** | **v2 носи 84 Feature-а — 79 клетки + 5 виртуални родителя.** | Мерено: обединенията на 17-те деца дават **5 единични `Polygon` без вътрешни пръстени, всичките валидни**. Друго решение би оставило 17 деца със `parent`, сочещ код без геометричен носител, и четирите оцелели родителски кода щяха да изчезнат от артефакта (изчезващите щяха да станат 13, не 9). |
225: | **ИА-О3** | **Тялото с решенията се МЕСТИ в `varna_3d`** (`data/quarters_decisions_imot_2026-09-08.json`). Черновата във Fire_Varna **остава на място непокътната**. Решение Р1. | ADR 011 И-D3 (Ч `011:17`) днес назовава път във Fire_Varna — **това решение се обръща с ред в комит К8, не мълчаливо** (инвариант 7). |
226: | **ИА-О4** | **Замразеният вход СЕ КОПИРА в `varna_3d/data/`** и става проследен там (Р13). | Иначе каноничният артефакт стъпва на файл, който **никое репо не носи**. `varna_3d` е частно, а червен ред 5 изрично разрешава суровия провенанс там. |
227: | **ИА-О5** | **v1 се архивира в `docs/archive/`, не в `data/archive/`.** | `data/*` е ПАПКОВО изключване; връщане назад е механично невъзможно (§1.9). |
228: | **ИА-О6** | **Осемнайсетте пина към v1 се пренасочват към архивния път** вместо да бъдат пребазирани към v2. Пиновете по sha (`c1551d24…`, 60, 301 917 B) **не се пипат**; П16 и П17 остават с нула байта. | Така целият стълб на `varna_3d` остава ЗЕЛЕН, а v2 се съди само от собствения си гейт. |
229: | **ИА-О7** | **`build_quarters_signed.py` и `qa_quarters_signed.py` не се пипат нито с един байт.** Пише се НОВ билдър и НОВ гейт. | §1.8, последният блок: това не е смяна на константи, а друг конвейер — старият гейт дори не може да ПРОЧЕТЕ новото тяло (`:1230` иска ключ `decisions`). |
230: | **ИА-О8** | **`--diff` СЕ ДОБАВЯ — но в НОВИЯ гейт.** ADR 010 D9 (Ч `010:54`) и G15 (Ч `010:129`) са регистрирани и **важат**: v2 е точно случаят над праговете (**17 982** сменени места при праг > 2; обединената площ 61,597 → 74,615 km² = **+21,1 %** при праг > 10 %). Затова **ИА-13 има две половини**: без `--diff-signed` → **изход 2**, с `--diff-signed "Р18"` → 0 плюс двоен запис и пълно преизмерване. | Нищо не се отменя: G15 се **изпълнява** в новия конвейер, а ADR 010 не се пипа. |
231: | **ИА-О9** | **`n_pts` (сбор 3 820) и `area_km2` (95 реда) остават в проследената чернова на Fire_Varna за целия интервал И-А → И-Б.** | Днес: `advert_id`, `raw_sha256`, координати → **0 попадения** (М). Изчистването/архивирането на черновата е И-Б (ИБ-15); тук се записва като **датиран дълг**, не се премълчава. |
232: | **ИА-О10** | **`_meta` на v2 е ЗАТВОРЕН набор от 41 имена** = 36-те на v1 **∪** двете, които ADR 011 И-D2 изисква и които v1 няма (`dictionary_sha256`, `snapshot_date`) **∪** трите обявени нови (`diff_v1_v2`, `mask`, `registry_pending_new`). `decisions_sha256` и `source_terms` **вече са сред 36-те** (М, поименно) и не се броят два пъти. Пълният списък е в §3.Г.8. ИА-6 съди срещу **тези 41**. | Срещу 36 гейтът е червен по конструкция (ИА-13 иска `diff_v1_v2`); срещу 39 два ADR-задължителни ключа стават червени. |
233: | **ИА-О11** | **`_meta.lot = "И-А"`, `_meta.plan.file = "Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md"`.** | ИА-6 сверява ИМЕНАТА на ключовете; съдържанието е на новия лот. |
234: | **ИА-О12** | **ИА-11 чете `Fire_Varna/data/address_rows.json` по sha на ПРОЧЕТЕНИЯ файл, не по литерал.** | HEAD-ът на Fire_Varna мърда сам. Човешката котва (80 510 / 77 210 / 1 / 3 299) стои в §1.5 и в отчета за Gate 2. |
235: | **ИА-О13** | **Изход 3 на Н8 се приема като база**, а не се „поправя“. | Ч `qa_fire_varna_m6.py:526`. |
236: | **ИА-О14** | **`scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json:19` НЕ се пипа.** | Подписано тяло от 07.09 и **исторически запис**; `qa_p8a` не го чете (М). Червен ред 8 забранява редакция на място. |
237: | **ИА-О15** | **`vinitsa_sever`: подписаното изключване на v1 се ОБРЪЩА.** v2 го доставя. Обратът стои като **ред в `_meta.excluded` със `status: "reinstated"` и `delivered: true`**, носещ дословно стария довод, номера на решението (Р17) и датата — **и в `declared_deviations[]`**. | Изпразването на `excluded[]` изтрива записа на подписано решение; червен ред 8 и §10 т. 5 забраняват точно това. |
238: | **ИА-О16** | **`d1_schema.nulled_on_import` расте от 7 на 10** — при извор без уикимапийски обект нулирани са и `wm_id`, `wm_ids`, `wm_title`. v1 не се пипа; v2 носи собствения си, честен списък. | „Копирай `d1_schema` дословно от v1“ прави ключа описание, което не описва артефакта. |
239: | **ИА-О17** | **Твърдото правило на C8 („жилищен код без ред в решенията = червено“, Ч `qa_quarters_signed.py:338-340`) в НОВИЯ гейт става „изброени поименно с довод“** за четирите (`druzhba, rozova_dolina, sv_ivan_rilski, trakia`). | Намаляване на строгостта върху подписан регистър е ОТКЛОНЕНИЕ и мястото му е тук. Старият C8 остава непокътнат и продължава да съди v1 (ИА-12). |
240: | **ИА-О18** | **ВСИЧКИ ефемерни пътища на лота живеят ИЗВЪН двете репа, под `%TEMP%`, и не са пътища от write-set-а.** Изчерпателно: `…/ia_build_a` и `…/ia_build_b` (двата билда за ИА-10) · `…/ia_broken/*` (счупените копия на входове и на артефакта — механики 1 и 4) · `…/ia_fixtures` (отрицателните фикстури) · `…/ia_builder_nd.py` (нарочно недетерминираният вариант на билдъра, половината на ИА-10) · `…/ia_docs/*` (счупените копия за ИА-19) · `…/ia_neg_fv` и `…/ia_neg_v3` (двете временни git-дървета). М: `%TEMP%` = `C:\Users\Petar\AppData\Local\Temp`. Всичко се маха на стъпка 18 и се сверява с `git worktree list` в **двете** репа + `git status --short`. | Кръг 3: ИА-STOP 1 и 13 спираха Изпълнителя върху собствената му машинария, защото ИА-О18 покриваше само дървото. Сега покрива **всяка** ефемерна пътека. |
241: | **ИА-О19** | **`docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` пристига МРЪСЕН** (дневникът на §20 от днес, писан от Архитекта). **К9 носи и този хънк, и новия §21**, и Изпълнителят го показва дословно на стъпка 0. | Иначе `git status --short` след К9 „изчиства“ чужд ред, който никой не е обявил. |
242: | **ИА-О20** | **Отрицателните фикстури НЕ са път от write-set-а и НЕ се комитват.** „Ф4“ отпада като файл; номерацията Ф1…Ф10 остава непроменена, за да не се разчита таблицата наново. Фикстурите се раждат в `%TEMP%/ia_fixtures` от Ф2 и се съдят от Ф3. | М: `.geojson` под `tests/fixtures/` е игниран (`.gitignore:23`), нито един съществуващ фикстурен `.geojson` не е проследен, и `tests/test_quarters_signed_fixtures.py:21-22` казва точно това. Комит на `.geojson` фикстури би искал ПЕТИ ред в `.gitignore` — файл, който Т1 обявява за пипнат ВЕДНЪЖ и вече е в К2 — и би бил геометрия с ръката на Изпълнителя срещу D16. |
243: | **ИА-О21** | **`_meta.rows_without_feature` на v2 носи ДРУГ набор кофи от v1** — v1 има `alias_of` + `deferred` (М, дословно), v2 има `deferred` + `no_boundary`. | Един и същ ключ с различна структура е скрита схемна смяна; влиза поименно в `declared_deviations[]` и в §3.Г.1. |
244: | **ИА-О22** | **Ф2 приема позиционния път като НЕЗАДЪЛЖИТЕЛЕН (`nargs="?"`)** и в режим `--decisions-diff` (ИА-16) работи без артефакт. Освен това самият **Д1 се записва на диска след подписа и преди К1**. | Образецът `qa_quarters_signed.py:1198` прави пътя задължителен; при пренасяне ИА-16 щеше да пада с argparse-грешка (изход 2), която ИА-STOP 3 чете като червено. А файлът Д1 на диска днес е **редакция 2 с три координатни двойки** — да го комитнеш „дословно“ означава да внесеш координати в проследен файл на публичното репо (М, §1.1). |
245: | **ИА-О23** | **Слоят с петте района се пинва по sha256 на прочетените байтове (`26e39b00…`, 201 130 B), не по блоб.** | М: `C:/git/m6000_private` не е git репо. Решаващ вход извън `_meta.inputs` противоречи на D10 — затова той Е шестият вход, а невъзможността да се версионира е записана като дълг ИБ-17, не като мълчание. Решение Р21. |
246: | **ИА-О24** | **Обобщените производни (площи, брой върхове/отсечки, хистограма на ръба, Hausdorff, хешове на частни файлове) СТОЯТ в трите проследени документа на Fire_Varna.** Обхватът на ИА-7 (данни) и на ИА-19 (проза) е обявен така: **ИА-7 гледа само файлове с данни, ИА-19 гледа само координати в проза.** | Червен ред 5 забранява геометрия, суров провенанс и **координати**; агрегатът не е нито едно от трите. Че дупката „производни в проза“ е реална, а не теоретична, е измерено (ИБ-4/ИБ-18) — но затварянето ѝ иска правило И гейт, а те са И-Б. Тук се обявява, не се премълчава. |
247: 
248: ---
249: 
250: | **ИА-О30** | **Сверка на Архитекта след кръг 5 (08.09 нощ), с която пространството на отклоненията се затваря на ИА-О30.** Шест поправки, всяка отбелязана на мястото си с „ИА-О30“: (1) `--privacy-scope <път>` влиза в CLI-договора на Ф2 (§3.А), защото ИА-7 го ползва; (2) `url` в артефакта = **чистият** адрес `https://www.imot.bg/obiavi/prodazhbi/grad-varna` — описателната опашка на `_meta.list_endpoint` не е URL (§3 ред `url`, ИА-8, Р10); (3) `_meta.source_terms.imot_bg` = **три** ключа `{url, recorded_on, position}` — отклонение от шесткльчовия образец C9 на v1, защото за imot.bg не е правена работа по условията и никой не е отварял страницата; ИА-8 съди трите (Р10 дава алтернативата с шест само по изрична дума на Петър); (4) записите в `_meta.excluded` носят петорката на v1 `{code, display, kind, registry_action, why}` + `delivered`/`status`, без ключ `reason` (ИА-17); (5) ИА-19 хваща и българската десетична запетая и има две отрицателни половини (точка и запетая); (6) ИА-19 → ИА-STOP 17 при изход 0 на `grep` (полярността е записана изрично). Числата в §1.4, §1.5, §1.7, Х5 и §5 остават тези на редакция 4; Р15/Р17 казват какво се преизмерва при „мр“ / „не“. | Петър подписва редакцията с тези шест; кръгове 1–5 на опровергателите са в `scratch/places_search/karta_imot_plan_reviews_08.09.md`. |
251: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Картата_imot_И-А_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 426..463 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 498ms:
426: ## 5 · Гейтове
427: 
428: **Кой гейт от кого се изпълнява (обявено, защото кръг 3 намери, че Ф2 „покрива ИА-1…ИА-18“, а две от тях не са в него):**
429: **Ф2** → ИА-1 … ИА-11, ИА-13 … ИА-17. **Старият гейт `src/qa_quarters_signed.py`** → ИА-12. **Ф3 (unittest)** → ИА-18. **Обявена команда с grep** → ИА-19.
430: 
431: **Как се чупи вход.** Четири механики, защото входовете са четири вида:
432: 
433: 1. **Файл на диска** (снапшот, речник, `address_rows`, слоят с районите): счупено копие в `%TEMP%/ia_broken/`, гейтът се вика с път към него.
434: 2. **Блоб на Fire_Varna** (`district_resolutions`, черновата за ИА-16): `git -C C:/git/Fire_Varna worktree add --detach C:/Users/Petar/AppData/Local/Temp/ia_neg_fv HEAD` → счупва се копието ТАМ → `git -C <wt> add -f -- <път>` → **`git -C <wt> -c user.name=… commit`** (детачнат HEAD, дангълинг комит, реалните клонове не мърдат) → гейтът се вика с `--resolutions-repo <wt> --resolutions-rev HEAD` (или `--draft-repo <wt>`) → **задължително** `git -C C:/git/Fire_Varna worktree remove --force <wt> && git -C C:/git/Fire_Varna worktree prune`.
435: 3. **Блоб на varna_3d** (Ф7): **ВТОРО, отделно дърво** `git -C C:/git/varna_3d worktree add --detach C:/Users/Petar/AppData/Local/Temp/ia_neg_v3 HEAD`, същата процедура, `--decisions-repo <wt> --decisions-rev HEAD`, махане с `git -C C:/git/varna_3d worktree remove --force`. **Едно дърво не стига: Ф7 живее във varna_3d и този път просто НЕ СЪЩЕСТВУВА в дърво на Fire_Varna** (кръг 3, БЛОКЕР).
436: 4. **Артефакт** (v2) и **проза** (за ИА-19): счупено копие в `%TEMP%`, гейтът се вика с него.
437: 
438: **Само `git add -f` НЕ стига** — мерено на цитирания образец (Ч `scratch/places_search/qa_night_pins.py:15-20`, `:111`, `:118`, `:171-175`): той доказва проследеност и сверява `worktree_sha256`, **но не подменя съдържание на блоб**. **Никой от тези пътища не е път от write-set-а** (ИА-О18).
439: 
440: **Всяка отрицателна половина се вика така, че да пада по СВОЯТА проверка.** Гейтът приема `--only <ИА-номер>`, който изключва останалите. Всяка се записва с: командата, счупения вход, `--only`, **истинския изходен код** и първия ред от изхода.
441: 
442: | # | гейт | команда · кога | очаквано | отрицателна половина (ТРЯБВА да даде ≠ 0) |
443: |---|---|---|---|---|
444: | **ИА-1** | валидност ПРЕДИ поправка | Ф2, `<артефакт> --tiling …` · стъпки 9, 13, 18 | 0; „95 входни полигона · **0 невалидни преди поправка** · 79 доставяни клетки · **0 невалидни след канонизация**“ (М) | копие на снапшота с пръстен „папийонка“ (самопресичане) → 1 |
445: | **ИА-2** | 0 застъпвания сред клетките · споделени ръбове | Ф2 · 9, 13, 18 | 0; **0 застъпващи се двойки > 0 m² сред 79-те клетки** · **712 споделени отсечки** · **2 849 върха** · **2 137 различни отсечки** (М) | копие на снапшота, в което една клетка е **буферирана с +0,0002°** → застъпване с всеки съсед → 1. (**Не „изместен връх“** — изместване навън прави процеп и гейтът остава 0.) |
446: | **ИА-3** | всеки от 98-те реда има точно един дом | Ф2 · 9, 13, 18 | 0; **98 = 79 Feature + 10 excluded_rows + 6 deferred + 3 no_boundary**; `len(_meta.excluded) == 11`; всяко id от речника точно веднъж; **`_meta.counts` (15 полета) съвпада дума по дума с преброеното**; **84 Feature-а = 79 + 5** | (блоб varna_3d) копие на Ф7 с махнат ред → „id без дом“ → 1; копие на артефакта с ръчно пипнат `counts.cells` → 1; копие с `counts.excluded_rows = 11` → 1 |
447: | **ИА-4** | застъпванията в артефакта са САМО родител–дете | Ф2 · 9, 13, 18 | 0; **17 двойки > 1 m², всичките в `_meta.parent_child`, всяка равна на пълната площ на детето; нула други** (М). Сбор на площите **82,908 km²**, обединение **74,615 km²** | копие на артефакта, в което геометрията на един родител е свита → двойката вече не е „дете ⊆ родител“ → 1 |
448: | **ИА-5** | D8 по конструкция | Ф2 · 9, 13, 18 | 0; всеки от **5**-те родителя е точно обединението на изброените си деца (17 общо), дете ⊆ родител, DAG без цикъл, `parent_child` = **17** двойки | (блоб varna_3d) копие на Ф7 с махнато дете от `children` → „родителят не е обединението“ → 1 |
449: | **ИА-6** | схемата | Ф2 · 9, 13, 18 | 0; **3 върхови ключа · 3 Feature ключа · 41 `properties` ключа** дословно по §1.3; **`_meta` = ЗАТВОРЕНИТЕ 41 имена на §3.Г.8**; **десетте нулирани полета са `null` по всичките 84**; **`rows_without_feature` носи точно кофите `deferred` и `no_boundary`** (ИА-О21) | копие с махнат `wm_polygon_sha256` → 1; копие с добавен `n_pts` в `properties` → 1; копие с добавен 42-ри `_meta` ключ → 1; копие без `snapshot_date` → 1; копие с кофа `alias_of` → 1 |
450: | **ИА-7** | **приватност — САМО файлове с ДАННИ** | Ф2, `--privacy-scope <път>` (в CLI-договора на Ф2, §3.А) · 9, 13, 18 | 0. **Обхватът е ЕДИН път: `Ф7`** — единственият файл с данни, който този лот създава или мени и който е тяло, а не геометрия. **Ф10, Д1, Д2, Д3 са ПРОЗА и са извън обхвата по конструкция — тях ги съди ИА-19** (ИА-О24); `data/quarters_signed.geojson` и `data/imot_bg_varna_polygons_08.09.geojson` са извън обхвата по конструкция — те СА геометрията в частното репо. По имена на ключове: `advert_id, raw_sha256, raw_response_sha256, points, raion_points, localid, cadnum, center, coordinates, geometry, centroid, polygon, bbox` → **0** и **0 float-а в кутията на Варна** (М днес върху блоба `8626ad43…`: 0 и 0; подниз `advert` = 98 от `n_adverts` и НЕ се брои) | копие на `Ф7` с добавен ключ `"advert_id"` → 1; копие на `Ф7` с ключ `"center"` и двойка числа в кутията на Варна → 1 |
451: | **ИА-8** | `source_terms` + атрибуция | Ф2 · 9, 13, 18 | 0; `_meta.source_terms.imot_bg` носи **ТОЧНО трите** ключа `url, recorded_on, position` (Р10; **ИА-О30: отклонение от шесткльчовия образец C9 на v1** — `quote/terms/verdict/checked_on` НЕ се пишат, защото никой не е отварял страницата и датата на „проверка“ би била атестация за нещо, което не се е случило); `len(_meta.licences) == 1`; всеки от 84-те носи непразни `license`, `license_terms`, `license_label`, `attribution` и **`url` == `https://www.imot.bg/obiavi/prodazhbi/grad-varna`** (чистият адрес, §3 ред `url`) | копие с празен `position` → 1; копие с четвърти ключ `checked_on` в `source_terms.imot_bg` → 1; копие с Feature, чийто `license` е голо „CC BY-SA“ → 1; копие, в което `url` носи опашката „(95 with adverts, counts)“ → 1 |
452: | **ИА-9** | **шестте входа са пиннати и сверени по прочетени байтове** | Ф2 · 9, 13, 18 | 0; `_meta.inputs` носи **точно шест** записа (§3.Г.7); блобовите три се четат по `git log -1 --format=%H -- <път>` в СВОЕТО репо; файловите три се хешват от диска; **шестият носи `note` за живота си извън git**. Записва се и мярката „varna_3d е `eol=lf`: работно копие = блоб“ (М) — **доказан капан, не отрицателна половина** | копие на артефакта с подменен `decisions_sha256` → 1; копие на снапшота с един променен байт при непроменен пин → 1; **(блоб Fire_Varna, дърво `ia_neg_fv`) копие на `district_resolutions` с трета резолюция, подадено с `--resolutions-repo/--resolutions-rev` → 1**; копие на слоя с районите с изтрит район → 1 |
453: | **ИА-10** | **два билда → едни байтове** | `Ф1 --out %TEMP%/ia_build_a/q.geojson && Ф1 --out %TEMP%/ia_build_b/q.geojson && cmp` · 8, 13, 18 | `cmp` мълчи, изход 0 | **`%TEMP%/ia_builder_nd.py`** — копие на Ф1 с една стойност от `datetime.now()` — пуснато два пъти → `cmp` → 1. *(„Билд с подменен снапшот“ НЕ е половината на този гейт: по Г.7 подмененият вход спира билда на пина, файл не се пише и `cmp` пада с „No such file“ — доказва пина, не детерминизма.)* |
454: | **ИА-11** | всяка адресна точка отчетена | Ф2, `--address-rows C:/git/Fire_Varna/data/address_rows.json` · 9, 13, 18 | 0; гейтът **преизчислява** и сравнява със записаното в `_meta.mask`: **80 510 = 77 210 (`in_one_cell`) + 1 (`tie_break`, развързан по Р6) + 3 299**; маската е **затворена тройка**: `outside_all_95` **2 274** · `excluded_cell` **1 025** (вътре в някоя от **десетте** изключени клетки; поименно 355/354/274/26/16 и 0 за петте села) · `deferred_cell` **0** (вътре в някоя от **шестте** отложени с вид); `address_rows_sha256` == sha на прочетения блоб (`2a4766bd…`) | копие на артефакта с `mask.in_one_cell` = 77 211 → преизчисленото не съвпада → 1; копие с четвърти клас в маската → „клас извън затворената тройка“ → 1. (**Не „махни клетка“** — точките само се местят и сборът остава 80 510.) |
455: | **ИА-12** | **нерегрес: v1 още се съди от своя гейт** | `python src/qa_quarters_signed.py docs/archive/quarters_signed_v1_2026-09-06.geojson --registry …` · **само 13 и 18** (преди стъпка 12 архивният път не съществува, Ч `qa_quarters_signed.py:1214-1216`) | **0**, същите 20 проверки, същите числа като Н1 | копие на архива с махнат Feature → 1 |
456: | **ИА-13** | **D9 / G15 — дифът, в ДВЕ половини** | (а) `Ф2 <артефакт> --diff <v1>` · (б) същата + `--diff-signed "Р18"`. **`<v1>` = `data/quarters_signed.geojson` на стъпка 9, `docs/archive/quarters_signed_v1_2026-09-06.geojson` на 13 и 18** | (а) **изход 2** и ред „над праговете на D9: **17 982** места > 2 · площ **+21,1 %** > 10 % — иска подпис“ — **това е G15, изпълнен, не отменен, и се записва в ОТЧЕТА като мярка**; (б) **0**, при което `_meta.diff_v1_v2` носи и гейтът **преизмерва**: 60 → **84** Feature · сбор 66,886 → **82,908 km²** · обединение 61,597 → **74,615 km²** · застъпвания **извън `_meta.parent_child`** **40 → 0** · **51 → 17** двойки · **51 общи кода** · **9 изчезващи, поименно** · **33 нови** · покритие **84,85 % → 95,90 %** · по адресна точка **49 397 / 17 982 / 935 / 9 832 / 2 364** при `tie_break_v1 = "азбучно най-малък код"` (Р20) | **половина (а) НЕ е отрицателната половина** — тя е гейт върху истински вход и мястото ѝ е в отчета (червен ред 6). Отрицателната половина е: копие на артефакта, в което едно от деветте изчезващи имена липсва от списъка → 1 при (б); и копие с `tie_break_v1` = друг низ при непроменени числа → 1 |
457: | **ИА-14** | регистърът и видовете | Ф2 · 9, 13, 18 | 0; **всеки от 84-те кода е или в регистъра (84 записа), или поименно в `_meta.registry_pending_new` (28)**; `_meta.registry_pending` == `set(registry) − 84-те` (**28**); **четирите жилищни кода без Feature (`druzhba, rozova_dolina, sv_ivan_rilski, trakia`) са изброени поименно с довод** (ИА-О17); **`kind` на всеки от 84-те е ключ на `KIND_NORM`** (М: 84/84); **`"TBD"` като код = червено; нула повтарящи се кодове** | копие с върнат `"code": "TBD"` → 1; копие с два реда на един код → 1; копие с код нито в регистъра, нито в `registry_pending_new` → 1; копие с `kind: "обект"` → 1; копие с `kind: "район"` (суровият imot-вид) → 1 |
458: | **ИА-15** | районът | Ф2 · 9, 13, 18 | 0; всичките 84 имат `district` от затворената петорка; **0 клетки „да“ без район** (М); `_meta.district_witness_disputes` носи **точно 5** реда (`vazrazhdane4, kochmar, so_planova, salzitsa` с `delivered: true`; `pristanishte_varna` с `delivered: false`), първите два със `resolution: "petar_agkk"` от блоба `d494d4d256ae…`, следващите два с `"pending_petar"`; `perchemliyata` носи `fire_varna_district` и бележка към подписаната резерва (Ч `qa_place_zone_aliases.py:74`); **знаменателят на свидетеля е 82 = 77 + 5**, а по доставяните клетки — **74 съгласия от 78** | копие с изтрит ред от `district_witness_disputes` → 1; копие с `district` извън петорката → 1; копие с `delivered: true` за `pristanishte_varna` → 1 |
459: | **ИА-16** | **`Ф7` срещу черновия блоб** | `Ф2 --decisions-diff --draft-repo C:/git/Fire_Varna --draft-path scratch/places_search/imot_decisions_1_2026-09-08_draft.json` — **без позиционен път** (ИА-О22) · 6, 13, 18 | 0; ревизията се намира с `git log -1 --format=%H -- <път>` (**`7556227…`**), sha-то на блоба е **`8626ad43…`**, 51 275 B; дифът е **точно десетте разлики Х1–Х10, нула други**; отпечатва sha на `Ф7` за Gate 2 | (блоб Fire_Varna, дърво `ia_neg_fv`) копие на черновата с единайсета разлика → 1; копие, в което Х4 е върнато на `"TBD"` → 1 |
460: | **ИА-17** | **изключените редове** | Ф2 · 9, 13, 18 | 0; `_meta.excluded` носи **11** записа **с петорката на v1 `{code, display, kind, registry_action, why}` + `delivered`** (ИА-О30: никакъв ключ `reason` — доводът живее в `why`, както старият C7 го съди, Ч `qa_quarters_signed.py:320-322`): **десетте с `kind_registry = null`, всеки с `delivered: false` и `why` = дословният `kind_note`**, плюс **един със `status: "reinstated"`, `delivered: true`** (`vinitsa_sever`, старият довод дословно в `why`, „Р17“). **Биекция: `kind_registry = null` ⇔ запис с `delivered: false`.** Запис с `delivered: true` иска ред в `_meta.declared_deviations` | копие на артефакта с махнат ред от `excluded` → „ред с null вид без запис“ → 1; копие без реда `vinitsa_sever` → „подписано изключване обърнато без запис“ → 1; копие с `delivered: true` без ред в `declared_deviations` → 1 |
461: | **ИА-18** | **мета-гейт: половините са тичали** | `python -m unittest discover -s tests` (частта `test_quarters_signed_imot_fixtures.py`) · 13, 18 | 0; тестът **ражда фикстурите в `%TEMP%/ia_fixtures`** и **прогонва всяка** с нейния `--only`, настоявайки за изход ≠ 0 **по своя номер** | фикстура, нарочно направена валидна → тестът пада → 1 |
462: | **ИА-19** | **прозата не носи координати** | `grep -nE '\b(4[23]\|2[78])[.,][0-9]{3,}\b' docs/plans/ПЛАН_Картата_imot_И-А_08.09.md docs/decisions/011_kartata_imot.md docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` · **преди К1, преди К8, преди К9, и на 18** | **0 попадения** (`grep` изход 1 = няма съвпадение = ЗЕЛЕНО; изход 0 = ЧЕРВЕНО; **ИА-STOP 17 се задейства при изход 0**). Изразът хваща и **българската десетична запетая** (ИА-О30, кръг 5: ширина, записана с запетая, е координата колкото записаната с точка) и три и повече знака след разделителя. Обхватът е **само трите проследени `.md` на този лот**; Д4 е игниран и не се съди. М (Архитект, 08.09 нощ, след изчистването в `146beac`): **0** попадения и в трите | копие на Д1 в `%TEMP%/ia_docs/` с една добавена двойка координати с ТОЧКА → `grep` намира → **ИА-19 червен**; второ копие с двойка със ЗАПЕТАЯ → **червен**. **Двете половини са задължителни: доказват, че изразът хваща и двете нотации** |
463: 

codex
Намерих противоречия, останали след ИА-О30: строителят още трябва да пише шест ключа в `source_terms` и поле `reason`, а гейтът вече изисква три ключа и забранява `reason`. Има и конкретен пропуск в приватността: планът съдържа хеш на суров отговор, който проверката за координати не чете.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Картата_imot_И-А_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 547..576 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 469ms:
547: ## 9 · Решения за Петър (Gate 1) — **двайсет и едно**
548: 
549: Всяко решение има **предложение по подразбиране**. „Да“ на плана без възражение = приемане на предложенията. **Седемте отворени точки, които самото тяло изброява в `_meta.decisions_open` (Ч), са покрити от Р15/Р16, Р3, Р4, Р7, Р14, Р8, Р10.**
550: 
551: | # | Въпрос | Измереното | **Предложение по подразбиране** |
552: |---|---|---|---|
553: | **Р1** | **Къде живее подписаното тяло?** | Днес е `Fire_Varna/scratch/places_search/imot_decisions_1_2026-09-08_draft.json` (проследен, публично репо, блоб `8626ad43…`, 51 275 B). Носи `n_pts` (3 820) и `area_km2` (95 реда). Машинарията за подпис във Fire_Varna е ЧЕРВЕНА (ИБ-1); varna_3d е ЗЕЛЕНА (§1.2). | **МЕСТИ се в `varna_3d/data/quarters_decisions_imot_2026-09-08.json`.** Черновата остава непокътната; архивирането ѝ е И-Б. **ADR 011 И-D3 се поправя с изричен ред в К8.** |
554: | **Р2** | **Виртуалните родители Feature-и ли са?** | И-D4 (Ч `011:19`) ги иска като обединения; v1 носи 4 от 5 като Feature-и; М: и петте обединения дават **единичен валиден `Polygon` без вътрешни пръстени**. | **ДА — 84 Feature-а (79 + 5).** Иначе 17 деца сочат родител без геометричен носител, а списъкът „изчезващи“ скача от 9 на 13. |
555: | **Р3** | **Петте „обекта“** | Тялото им дава **`kind_registry = null`** с довод „обект: не е клетка → без вид“ (Ч). И петте имат полигон и сгради; и петте **липсват от регистъра**. **Държат 1 025 адресни точки** (355/354/274/26/16, М). С тях покритието е 97,18 %, без тях — 95,90 %. | **ИЗКЛЮЧЕНИ.** Стоят поименно в **`_meta.excluded[]`** с `delivered: false` и довода си дословно; точките им са клас `excluded_cell`. **Цената е назована: 1 025 адреса (1,27 %) остават без квартална дума.** |
556: | **Р4** | **Трите без полигон** — 5848, 5866, 6294 | Речникът ги знае, imot няма полигон; `buildings = null`, `area_km2 = null` (М). `malka_chaika` е в регистъра като `м-т`, а тялото му дава `kind_registry = "кв"` (М) — разминаване, което днес не удря гейт, защото редът е `no_boundary`. | **`no_boundary` — БЕЗ Feature.** Изброяват се в `_meta.rows_without_feature.no_boundary[]` с довод. **Не** се прави Feature с `geometry: null`. Разминаването по `malka_chaika` влиза в Ф10. |
557: | **Р5** | **Двата кода `"TBD"`** | М: 98 реда → 97 различни кода. | **`elektrorazpredelenie_varna` и `severna_promishlena_zona`.** Реални, уникални, по правилото К37 (slug). ИА-14 прави `"TBD"` и повтарящ се код червено. |
558: | **Р6** | **Точката на общия ръб** (една) | Върху **суровите** полигони — **0** двойни попадения; след канонизацията по D1 — **1**, между **5055 к.к. Чайка** и **5053 м-т Ален мак** (М). **(Координатата ѝ живее в частния файл и не се преписва тук.)** | **Развръзка по най-малък `raion_num`.** Записва се в `_meta.mask.tie_break` и `tie_break_rule`, проверява се от ИА-11. Тук печели **5053 „м-т Ален мак“**. |
559: | **Р7** | **Единайсетте отложени** | Шест носят вид; **пет са села с `kind_registry = null`**. И единайсетте имат **0 сгради**, нито един няма район, и **не хващат нито една адресна точка** (М). Сумарно 10,691 km². | **Разделят се по вида.** Шестте с вид → `rows_without_feature.deferred[]`. **Петте села → `_meta.excluded[]`** (null вид = изключен ред). И двете поименно, с довод. |
560: | **Р8** | **`precision_m` за плочката** | Медианата на ръба на **79-те канонизирани клетки** е **96,5 m** (М). v1 дава 100 за `human_polygon`, 50 за `street_bounded_face`; подът по D7 е **50** (Ч `010:50`). | **`precision_m = 100` за всичките 84.** Измерената рисувателна стъпка е под 100 и над пода 50. |
561: | **Р9** | **Как се пинва тялото?** | Литерал `DECISIONS_BLOB_SHA256` в гейта трябва да е написан **преди** комита К3, който ражда блоба — капанът, който събори кръгове v2–v5. | **Без литерал.** Гейтът чете `_meta.decisions_sha256` и настоява да е равно на `sha256(git show <rev>:<път>)` на файла, който наистина е прочел. **Човешката котва за Gate 2 е изходът на ИА-16** („десет наименувани разлики, нула други“) плюс отпечатаното sha. |
562: | **Р10** | **Атрибуцията и `source_terms`** (попълва се, не се обсъжда) | C9 иска на извор **шест** ключа (Ч `qa_quarters_signed.py:362`); ADR 011 И-D2 дава два — поправя се в К8. **`_meta.list_endpoint` е с опашката** (М). | **`_meta.attribution` и `properties.attribution`:** „Кварталните граници в този файл са районите на imot.bg (© imot.bg), снапшот 08.09.2026. Геометрия НИКОГА не пътува публично.“ · **`license_label`:** „граница по районите на imot.bg (район `<raion_num>`, свалена 2026-09-08) — извор на всекидневната употреба, не официален кадастър“ · **`url` = чистият адрес `https://www.imot.bg/obiavi/prodazhbi/grad-varna`** (без описателната опашка на `_meta.list_endpoint`) · **`_meta.source_terms.imot_bg` = ТОЧНО ТРИ ключа:** `{url: "https://www.imot.bg/obshti-uslovia", recorded_on: "2026-09-08", position: "Публично пътуват само име, код и src на квартала; геометрията остава в частното репо."}` — **без `quote`, `terms`, `verdict`, `checked_on`**: никой не е отварял страницата, а дата на „проверка“ в подписан артефакт би била атестация за нещо, което не се е случило (ИА-О30). Докато присъда няма, **нищо от този артефакт не пътува публично** — записва се в `_meta.publication`; дългът е ИБ-20. **Алтернатива само с изрична твоя дума:** Изпълнителят отваря страницата, преписва абзаца дословно в `quote`, вписва `checked_on` и `terms`, ти подписваш присъдата с ред в опашката — тогава ключовете стават шест и ИА-8 се пренаписва за тях. |
563: | **Р11** | **Архивните пътища** | `data/archive/` е **механично невъзможен** (М, §1.9); `docs/archive/` вече съществува и е проследен (М). | **`docs/archive/quarters_signed_v1_2026-09-06.geojson`** (+ ред `!…` в блока на Т1) и **`docs/archive/РЕГИСТЪР_архив.md`**. Старите `granitsi_decisions_2/3/4_*.json` **не се местят в И-А** — те са пиннати от `build_quarters_signed.py:89` и от `Fire_Varna/tests/test_b3_gates.py:34`; преместването им е И-Б. |
564: | **Р12** | **Двата нови спора за район** — `so_planova`, `salzitsa` | `kochmar` и `vazrazhdane4` вече имат подписано решение (блоб `d494d4d256ae…`, ревизия `e6c706d…`, М). Знаменателят на свидетеля е **82** (77 + 5). | **Нашият слой печели; спорът се ЗАПИСВА, не се решава.** `district_src = "fire_varna_district"`, двата влизат в `_meta.district_witness_disputes` с `resolution: "pending_petar"`. |
565: | **Р13** | **Къде живее замразеният вход?** | Днес и двата файла са само в **игнорираната** папка на **публичното** репо (М). Никое репо не ги носи. | **Копират се в `varna_3d/data/` и стават проследени там** (Ф5, Ф6; комит на Петър). Иначе v2 не е възпроизводим от нито едно репо. |
566: | **Р14** | **Шестнайсетте кода без район от АГКК** | 11 отпадат по Р7, `letishte` по Р3, трите без полигон по Р4, `perchemliyata` е покрит от вече подписаната поименна резерва (Ч `qa_place_zone_aliases.py:74`) и получава `primorski` от нашия слой (М). Всичките **79 клетки „да“ имат район** (М). **Черновата казва „13“; вярното е 16** — поправя се с Х10. | **Не искат отделно решение** — този ред е за да го видиш и да кажеш „да“ веднъж. |
567: | **Р15** | **`район` → `кв` или `мр`?** (19 клетки) | Тялото само го маркира „**ДА СЕ ПОДПИШЕ**“ (Ч). `мр` е в `KIND_NORM`, но `KIND_CLASS` го праща в **locality** (Ч `fire_varna_locations.py:156-160`), а по D6 locality **никога не пълни `quarter`** — 19-те най-всекидневни имена (Автогара, ЖП гара, Операта, Гръцката махала…) биха останали без квартална дума. | **`район` → `кв`.** Записва се в `_meta.kind_registry_decisions` (Х7). Алтернатива `мр` — само с изрична твоя дума, и тогава И-Б трябва да отвори `LOCALITY_CODES`. |
568: | **Р16** | **Видът на петте виртуални родителя** | Полето им `kind` е проза (М). Четирите съществуват в **подписания регистър** и във v1 с един и същ вид (М). `pobeda_group` няма ред никъде; двете му деца са `кв` (М). | **Четирите се преписват от регистъра; `pobeda_group → "кв"`.** Три от четирите стойности имат два независими извора. |
569: | **Р17** | **`vinitsa_sever` — обръщане на подписано изключване** | v1 `_meta.excluded` носи един ред за него (Ч дословно); черновата го дава като клетка 6295, `include = "да"`, `kind_registry = "вз"`, 294 сгради, 0,303 km² (М). | **Обръща се съзнателно: v2 го доставя.** Записва се като **единайсети** запис в `_meta.excluded` със `status: "reinstated"`, `delivered: true`, стария довод дословно и „Р17“, плюс ред в `declared_deviations` и в И-D5. **Ако кажеш „не“ — редът излиза от 79-те и v2 става 78 + 5 = 83; всяко число в §1.5, §1.7 и §5 се преизмерва преди изпълнението.** |
570: | **Р18** | **D9 / G15 — дифът е над праговете** | Ч `010:54` и `:129`. Мерено: **17 982** места сменят думата, обединената площ расте с **21,1 %**. | **Подписваш дифа.** ИА-13 (а) тича без подпис и връща **2**; ИА-13 (б) тича с `--diff-signed "Р18"`, преизмерва всичко и връща 0. **G15 не се отменя — изпълнява се.** |
571: | **Р19** | **Амандамент на ADR 010 D0/G23** | Ч `010:36`: „всяко бъдещо разминаване АГКК ↔ `district.code` = STOP“; Ч `:137` регистрира G23. М: `varna_3d/src/qa_district_official.py` **не съществува**. Плочката ражда два нови спора (Р12). | **Ред в ADR 011 И-D5** (не в ADR 010, който е извън write-set-а): за плочката АГКК AU5 е **независим свидетел**; разминаване, **записано поименно** с `resolution` (подписан) или `"pending_petar"`, не е STOP; разминаване **без запис** е STOP. ИА-15 го изпълнява; дългът е ИБ-16. |
572: | **Р20** | **Правилото за развръзка на страната v1 в дифа** | М: **4 517** от 80 510-те точки попадат в ≥ 2 полигона на v1 — без обявено правило числата „същата/сменена дума“ не са възпроизводими (кръг 3 обори двойката 49 926/17 453). Четири правила дават четири различни резултата (М: по реда на файла 49 925/17 454; азбучно 49 397/17 982; най-малка площ 50 100/17 279; най-голяма площ 48 662/18 717). | **Азбучно най-малкият код печели.** Довод: детерминизъм, независим от реда на файла — същият клас правило като Р6. Записва се в `_meta.diff_v1_v2.tie_break_v1` и се преизмерва от ИА-13. Числата: **49 397 / 17 982 / 935 / 9 832 / 2 364**. |
573: | **Р21** | **Слоят с петте района — вход, който git не вижда** | М: `C:/git/m6000_private` **не е git репо**; файлът е 201 130 B, sha256 `26e39b00…`, дава точно 5 района с `authority == "osm"`. Той решава `district` на всичките 84 Feature-а. | **Влиза като ШЕСТИ вход в `_meta.inputs`, пиннат по sha256 на прочетените байтове**, с `note` защо не е блоб. Алтернатива: да се копира и във `varna_3d/data/` — **не се предлага в И-А**, защото е чужд слой и иска отделно решение за собственост; дългът е **ИБ-17**. |
574: 
575: ---
576: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$paths=@('"'docs/plans/ПЛАН_Картата_imot_И-А_08.09.md','docs/decisions/011_kartata_imot.md','docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md'); foreach("'$p in $paths){ $s=[System.IO.File]::ReadAllText((Join-Path (Get-Location) $p),[System.Text.Encoding]::UTF8); '"'{0}: coordinate_regex_hits={1}; raw_dictionary_hash_mentions={2}; mojibake_hits={3}' -f "'$p,[regex]::Matches($s,'"'\\b(4[23]|2[78])[.,][0-9]{3,}\\b').Count,[regex]::Matches("'$s,'"'6fa3b07007203c5a5787d0af3e0d63c03d3a625dd741ab34c8dabe1965cbf38f').Count,[regex]::Matches("'$s,'"'[\\u00D0\\u00D1\\u00C2][\\u0080-\\u00FF]').Count }; git ls-files --error-unmatch -- docs/plans/ПЛАН_Картата_imot_И-А_08.09.md docs/decisions/011_kartata_imot.md docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'scratch/places_search/karta_imot_plan_reviews_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; $n=0; $a | ForEach-Object { $n++; if($_ -match '"'"'^#{1,4} '"'){'{0}: {1}' -f "'$n,$_ }}' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/decisions/010_signed_quarter_boundaries.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 40..72 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 519ms:
1: # Опровергатели на ПЛАН_Картата_imot (workflow, 08.09) — 2 лещи Opus
3: ## Леща 1 · гейтове и отрицателни половини
46: ## Леща 2 · privacy, ред, обхват, регистър на отмяната
96: # Опровергатели на ПЛАН_Картата_imot (workflow, 08.09) — кръгове v1→v2→v3, две лещи Opus
98: ## Кръг v2 · леща 1 · присъда НЕГОДНО
116: ## Кръг v2 · леща 2 · присъда НЕГОДНО
134: ## Кръг v3 · леща 1 · присъда НЕГОДНО
152: ## Кръг v3 · леща 2 · присъда НЕГОДНО
172: ## Кръг v4 · леща 1 · присъда НЕГОДНО
190: ## Кръг v4 · леща 2 · присъда НЕГОДНО
208: ## Кръг v5 · леща 1 · присъда НЕГОДНО
226: ## Кръг v5 · леща 2 · присъда НЕГОДНО
246: # Опровергатели на ПЛАН_Картата_imot_И-А (подлот varna_3d + документи)
248: ## И-А кръг 1 · леща 1 · присъда НЕГОДНО
266: ## И-А кръг 1 · леща 2 · присъда НЕГОДНО
284: ## И-А кръг 2 · леща 1 · присъда НЕГОДНО
302: ## И-А кръг 2 · леща 2 · присъда НЕГОДНО
322: ## И-А кръг 3 · леща 1 · присъда НЕГОДНО
338: ## И-А кръг 3 · леща 2 · присъда НЕГОДНО
354: ## И-А кръг 4 · леща 1 · присъда НЕГОДНО
371: ## И-А кръг 4 · леща 2 · присъда НЕГОДНО
391: ## И-А кръг 5 · леща 1 · присъда НЕГОДНО
393: ### Блокери
397: ### Бележки
409: ## И-А кръг 5 · леща 2 · присъда НЕГОДНО
411: ### Блокери
417: ### Бележки

 succeeded in 509ms:
40: **D2 · Лицензът се решава ТУК (К4).** Таблица `method` → лиценз, проверявана за СЪГЛАСИЕ: „по памет“ / „по огради“ → **CC0-1.0**; „по сгради“ → **КАИС „Отворени данни“, атрибуция АГКК, CC0 не се твърди — ЗАКЛЮЧЕН, докато `_meta.faza0_signed` не е `true`, а той не може да е `true`, докато `ФАЗА_0_лицензи.md:4` носи „чака подпис“ (G21)**; „по улици“ → **ЗАКЛЮЧЕН винаги** (нарушава условие 4, `ФАЗА_0_лицензи.md:25-26`), отключва се само с изричен подписан ключ. **Лицензът на ФАЙЛА е най-строгият участник.** Подложка: нашата PMTiles основа (ADR 002 D8) или КАИС; **никога Esri** — инструментът отказва връх, докато `map.getLayoutProperty("sat","visibility") === "visible"` (`varna_3d/web/index.html:880`), проверено от G18.
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

 succeeded in 540ms:
docs/plans/ПЛАН_Картата_imot_И-А_08.09.md: coordinate_regex_hits=0; raw_dictionary_hash_mentions=1; mojibake_hits=0
docs/decisions/011_kartata_imot.md: coordinate_regex_hits=0; raw_dictionary_hash_mentions=0; mojibake_hits=0
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md: coordinate_regex_hits=0; raw_dictionary_hash_mentions=0; mojibake_hits=0
docs/decisions/011_kartata_imot.md
docs/plans/ПЛАН_Картата_imot_И-А_08.09.md
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'scratch/places_search/karta_imot_plan_reviews_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 391..428 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 482ms:
391: ## И-А кръг 5 · леща 1 · присъда НЕГОДНО
392: 
393: ### Блокери
394: - БЛОКЕР 1 · Флаг, който гейт ползва, но договорът не го носи. `C:\git\Fire_Varna\docs\plans\ПЛАН_Картата_imot_И-А_08.09.md:448` вика ИА-7 като „Ф2, `--privacy-scope`“, а изчерпателният CLI-договор на Ф2 на `:268` изброява 17 флага и `--privacy-scope` НЕ е между тях (М: `grep -n -- "--privacy-scope"` → едно-единствено попадение, ред 448). Изпълнителят пише Ф2 по договора → argparse отказва непознатия флаг с изход 2 → ИА-7 изглежда червен → ИА-STOP 3 и спиране. Това е точно класът дефект, който самият план обяви за БЛОКЕР в кръг 3 за `--resolutions-*` (`:269`). Поправка: или флагът влиза в договора на `:268`, или ИА-7 се вика без него и обхватът (единственият път Ф7) се зашива в гейта.
395: - БЛОКЕР 2 · Гейт, червен по конструкция срещу поръчания артефакт. ИА-8 (`…И-А_08.09.md:449`) иска `_meta.source_terms.imot_bg` да носи ШЕСТТЕ ключа `url, checked_on, quote, terms, verdict, position` по образеца C9 (Ч `C:\git\varna_3d\src\qa_quarters_signed.py:362` — измерено, шестте ключа са там, цикълът обаче обхожда само `wikimapia` и `openstreetmap`) и настоява `verdict ∈ {allowed, allowed_with_conditions}`. Решение Р10 на кръг 5 поръчва ТОЧНО ТРИ ключа (`url, recorded_on, position`) и изрично забранява `quote`, `terms`, `verdict`, `checked_on`. Изпълнителят строи по Р10 → ИА-8 пада → ИА-STOP 3 → спиране. Същият конфликт е и в реда за Д2 (`:388`), който нарежда в ADR 011 И-D2 „`source_terms` от два на ШЕСТ ключа“. Едното от двете трябва да падне; докато и двете стоят, лотът не може да завърши. (Забележка към двата блокера: те са проверени срещу редакция 4 — единствената, която лежи на диска и в HEAD `146beac`; §0–§8 на кръг 5 не ми бяха подадени. Ако кръг 5 е пренаписал §3 и §5 в същия ход, и двата отпадат — но това трябва да се покаже, не да се предположи.)
396: 
397: ### Бележки
398: - Мерено наново и възпроизведено ТОЧНО (собствена точка-в-полигон върху `data/address_rows.json`, 80 510 реда, срещу замразения снапшот): петте обекта държат **1 025** адресни точки, поименно 355/354/274/26/16 (Р3) · 79-те клетки покриват **77 211** = 77 210 уникални + 1 върху общия ръб (ИА-11, Р6) · единайсетте отложени хващат **0** (Р7) · извън всичките 95 → **2 274** (ИА-11) · покритие **95,90 %** и **97,18 %** (Р3) · v1 покрива **84,85 %**, а **4 517** точки падат в ≥ 2 полигона на v1 (Р20). Измерителният слой на плана е здрав.
399: - Мерено и потвърдено буквално: базата на Fire_Varna е червена — 342 теста / 24 паднали, `run_gates` 1, `release` 6, `coverage` 4 (ИБ-1) · `expectations.json`: тяло 55cbf2c7f8f2 ≠ ред R8 f8c4e43f5e85 и двигател a73fa006ab0b ≠ 61967588780f (ИБ-2) · places 127/91/44/44/8, hotels 199/167/39/11/7, „coverage изход 2 — 30 непокрити“ (ИБ-3) · `b3_g11.py HEAD --cached` = 0, обхват 19 · стейджнати 14 · черновият блоб е 51 275 B / `8626ad43…` (работното копие е 53 115 B заради CRLF — точно капанът, който червен ред 12 назовава).
400: - Всички котви `файл:ред`, които проверих, са верни: `gates/probe/b3_g11.py:37/:39/:40-46/:105-106` · `gates/release.py:189/:437` · `gates/coverage.py:87/:96` · `tests/test_b3_gates.py:34/:90-91/:172/:174/:194/:197` · ADR 010 `:36/:50/:54/:68/:74/:129/:137` · `qa_place_zone_aliases.py:74` · `qa_p8a.py:60-66` · `fire_varna_locations.py:93-94/:150-161` · `build_quarters_signed.py:89/:123/:1562-1563` · регистърът 84 записа, `schema_version 1.1`, съюзът на ключовете на записите = **15**, ревизия `627b240` · `qa_district_official.py` НЕ съществува (Р19) · `C:\git\m6000_private` не е репо, 201 130 B / `26e39b00…` · слоят AU5 61 469 B / `78a2de5960…` на двата игнорирани пътя.
401: - ИБ-4 · числото „84 от 245 проследени `.md`“ е ГРЕШНО. С образеца на самия план (§1.1: `4[23]\.[0-9]{4,}|2[78]\.[0-9]{4,}`) измервам **72 от 245**. Че образецът е правилният, се вижда от другото число в същия ред — 1 902 попадения в `docs/audits/h2_kmz_consolidation_dry_run.md` съвпадат байт в байт. 84 не се получава от нищо: varna_3d добавя още 58 (общо 130), а 3-знаковият вариант дава 75. Изводът на ИБ-4 (дупката е реална и голяма) остава; числото се поправя.
402: - Р15, алтернативата „мр“ · „менят се **19** от 98-те реда“ е подценено: измервам **21** реда с `kind: "район"` → `kind_registry: "кв"` — деветнайсетте доставяни плюс `TBD`/район 5848 и `malka_chaika`/район 6294 (и двата са от тримата без полигон). При „мр“ се менят 21 реда на Ф7, а бележката за `malka_chaika` в Р4 (регистър `м-т` срещу тяло `кв`) сменя знака си заедно с тях. Клаузата за преизмерване го покрива, но числото, което Петър подписва, трябва да е 21.
403: - Р3 и Р7 стъпват на една и съща колона · в черновата `imot_decisions_1_2026-09-08_draft.json` полето се казва `buildings`, а стойностите му за петте обекта (26/354/274/16/355) съвпадат ТОЧНО с моето броене на адресни точки. Тоест „0 сгради“ и „не хващат нито една адресна точка“ в Р7 не са два независими свидетеля, а един. Или колоната е кръстена грешно, или съвпадението иска дума — в подписвано тяло това се назовава.
404: - ИА-19 е гейт с обърната полярност: `grep` изход 1 = ЗЕЛЕНО, изход 0 = ЧЕРВЕНО (`:460`). Обявено е, ИА-STOP 17 му пасва по знак — но е единственият ред в §5, където „изход 0“ значи провал; струва си да стои като изрична бележка до командата, за да не го прочете Изпълнителят по навик. Днес и трите документа са чисти: 0 попадения в Д1, Д2 и Д3 (М).
405: - ИА-10 е единствената отрицателна половина, която чупи ПРОГРАМАТА, а не вход: `%TEMP%/ia_builder_nd.py` е копие на Ф1 с `datetime.now()`. За гейт за детерминизъм това е защитимо (счупен вход спира билда на пина и `cmp` пада с „No such file“ — планът сам го казва), но правилото „отрицателната половина е счупен ВХОД“ има точно това изключение и то трябва да е обявено като изключение. Отделно: Ф1 няма обявен CLI-договор, а ИА-10 го вика с `--out` два пъти.
406: - Базата под краката на плана е мръднала след редакция 4: HEAD вече е `146beac`, мръсният хънк на §20 в Д3 е КОМИТНАТ, и днес мръсни нестейджнати проследени файла са **два** (`scratch/places_search/lot1v_v_reference_manifest.json`, `scratch/places_search/probe_out/token_parity.json`), не три. §10 т. 4 на кръг 5 вече го отразява — но ИА-О19, К9 (`:487`) и ИА-STOP 2 (`:512`) в редакция 4 още очакват мръсния хънк; ако не са пипнати, ИА-STOP 2 гърми на стъпка 0.
407: - Пространствата на номерата не са затворени в редакция 4: §0 т. 10 обявява `ИА-О1 … ИА-О24`, а текстът ползва `ИА-О25` на `:302`. Текстът на кръг 5, който получих, ползва `ИА-20`, `ИА-О25`, `ИА-О30`, `ИБ-19`, `ИБ-20` — все извън обявените в редакция 4 обхвати. Понеже §0–§8 на кръг 5 не ми бяха подадени, лещите „всеки гейт = скрипт или ред от write-set + комит“, „полярност на всеки STOP“, „комити: агент код/документи, Петър данни/геометрия/.gitignore“ и „затворени номерации“ можах да проверя само срещу редакция 4. Двата блокера горе излизат оттам. Проверено и вярно в редакция 4: К2/К3/К6 са ръката на Петър и носят `.gitignore`, данните и геометрията; К1/К4/К5/К7/К8/К9 са на Изпълнителя и са само код и документи; отрицателните дървета `ia_neg_fv` и `ia_neg_v3` са под `%TEMP%`, извън двете репа, и се махат с `worktree remove --force` + `prune`. Емпирично проверих и Н2′: `qa_p8a.py --signed <архивен път>` върху байтово копие дава изход **0** — пренасочването към архива не чупи пина, защото `:318` хешира файла, не пътя.
408: 
409: ## И-А кръг 5 · леща 2 · присъда НЕГОДНО
410: 
411: ### Блокери
412: - ПРИВАТНОСТ · ИА-19 е сляп за българската десетична запетая — гейтът, който пази червен ред 5, е fail-open. Мерено: обявената команда на ИА-19 е `grep -nE '(4[23]|2[78])\.[0-9]{4,}'` (Ч C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:460, същият образец на :49) — САМО с точка. `git grep -lE '4[23]\.[0-9]{4,}|2[78]\.[0-9]{4,}' -- '*.md'` → 72 файла; `git grep -lE '4[23][.,][0-9]{4,}|2[78][.,][0-9]{4,}' -- '*.md'` → ТОЧНО 84 — числото, което ИБ-4/ИБ-18 цитират. Значи собствената ви мярка е правена със запетая-вариант, а гейтът — без него. Дупката не е теоретична: 20 проследени `.md` вече носят варненски ширини във вида `43,2780`, `43,2733`, `43,2463`, `43,1968` (мерено), а самите три документа пишат десетичните с запетая навсякъде („10,691 km²“, „96,5 m“, „97,18 %“). Изпълнител, който напише координата по български, минава ИА-19 зелен и я комитва в публичното репо. Поправката е един символен клас: `[.,]`. Отрицателната половина също трябва да ражда двойката със запетая, иначе не доказва нищо.
413: - Р10 · `url` = ДОСЛОВНО `_meta.list_endpoint` записва низ, който НЕ е URL, в 84 Feature-а. Мерено в снапшота (C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson): `_meta.list_endpoint = "https://www.imot.bg/obiavi/prodazhbi/grad-varna (95 with adverts, counts)"`. Планът сам казва „е с опашката“ и въпреки това нарежда „ДОСЛОВНО“. Във v1 `properties.url` е връзка към конкретния обект (Ч data/quarters_signed.geojson, 60/60 Feature-а), а `_meta.attribution` на v1 препраща към него („връзка към обекта в полето url“). Изпълнителят ще произведе 84 полета с паразитен текст в URL. Освен това не е казано КОЕ `url` — `properties.url`, `licences[].url` или `source_terms.imot_bg.url` (последното е друга стойност: `https://www.imot.bg/obshti-uslovia`). Напишете точния литерал, който да се запише, и мястото му.
414: - Р3/Р7/Р17 · ключът на `excluded[]` се разминава с петорката на v1. Мерено: v1 `_meta.excluded[0]` носи точно `['code','display','kind','registry_action','why']` — доводът живее в **`why`**. Гейтът ИА-17 обаче настоява за „`delivered: false` и **`reason`** = дословният `kind_note`“ (Ч ПЛАН_Картата_imot_И-А_08.09.md:458). Двете не могат да са верни едновременно: пише ли Изпълнителят `why` — ИА-17 е червен; пише ли `reason` — счупена е декларацията „с петорката на v1“ и биекцията с v1 пада. Кажете поименно кой е ключът (препоръка: `why`, както е v1) и какво носят `kind` и `registry_action` за десетте реда, които изобщо ги няма в регистъра (`kind_registry = null`).
415: - СЪГЛАСУВАНОСТ · четири решения от кръг 5 местят числа, които редакция 4 е заковала ВЪТРЕ в гейт-редове и в затворени набори; в подадения ми текст няма нито един ред, който да ги пресича наново. Всяко неотрязано място е гейт, червен по конструкция → Изпълнителят спира. Мерено срещу C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md (редакция 4, = HEAD 146beac): (1) Р21 прави входовете ОСЕМ, а §3.Г.7 е озаглавен „Входовете по sha — ШЕСТ“ и ИА-9 иска „`_meta.inputs` носи **точно шест** записа“ (Ч :362, :450); (2) Р4 пинва `registry_pending` = 27 и въвежда НОВИЯ ключ `registry_without_feature` = 28, а Х5 брои `registry_pending: 28` (Ч :305), ИА-14 твърди „`_meta.registry_pending == set(registry) − 84-те` (28)“ (Ч :455), и Г.8 е ЗАТВОРЕН набор от 41 имена, в който `registry_without_feature` го няма, а ИА-6 съди срещу него (Ч :375, :232); (3) Р12 брои свидетеля „84 попадения, 80 съгласия, 4 спора“, а ИА-15 пинва „знаменателят на свидетеля е 82 = 77 + 5“ и „74 съгласия от 78“ (Ч :456); (4) Р10 дава на `source_terms.imot_bg` ТРИ ключа, а Г.8 казва „`source_terms.imot_bg` = **шестте** ключа на Р10“ (Ч :379). Числата на кръг 5 са ВЕРНИТЕ — проверих ги: регистър − доставени = 28, регистър без ред в тялото = 27 (единствената разлика е `malka_chaika`, точно както казва Р4), а центроидът на `perchemliyata` пада в АГКК AU5 `10135-02 primorski`, тоест всичките 79 клетки + 5 родителя = 84 попадения. Тоест не числата трябва да се пипат, а гейт-редовете и затворените набори — в същия кръг.
416: 
417: ### Бележки
418: - Р20 · „по реда на файла“ НЕ е четвърто правило. Мерено: 60-те Feature-а на v1 стоят подредени азбучно по `code` (`codes == sorted(codes)` → True), тоест „по реда на файла“ и „азбучно най-малкият код“ са едно и също правило и не могат да дадат различни резултати. Пресметнах и четирите: file 49 398/17 981 · alpha 49 398/17 981 · най-малка площ 50 101/17 278 · най-голяма площ 48 663/18 716. Пиннатата в плана двойка за реда на файла (49 925/17 454) не се възпроизвежда. Изборът и петте пиннати числа НЕ страдат — но доводът „четири правила дават четири различни резултата“ е верен само за ТРИ.
419: - Р20 · трите производни числа излизат ТОЧНО: `lost 935`, `gained 9 832`, `neither 2 364`, и `4 517` точки в ≥2 полигона на v1 — мерено независимо върху блобовете (80 510 реда в C:/git/Fire_Varna/data/address_rows.json, 60-те полигона на v1, 79-те клетки на снапшота). `same/changed` ми дават 49 398/17 981 срещу пиннатите 49 397/17 982 — разликата е ТОЧНО една точка и се обяснява с Р6 (аз мерих върху суровите полигони, където двойни попадения са 0; след канонизацията едно попадение става двойно и отива при 5053). Тоест числата предполагат канонизираните клетки — ИА-13 трябва да го каже изрично, иначе е ±1 червен.
420: - Р20 · страната v1 е добре дефинирана само по развръзката, не по ОБХВАТА. Измерих цената: с всичките 60 Feature-а на v1 (включително седемте родителя в `_meta.parent_child`) многократните попадения са 4 517 — числото, което Р20 пинва; ако някой приложи `leaf_cells_only` симетрично и на страната v1, попаденията стават 904, а петте числа — 42 761/15 370/698/19 080/2 601. Добавете едно изречение: „страната v1 = всичките 60 Feature-а, родителите ВКЛЮЧЕНИ“.
421: - Р15 · „менят се 19 от 98-те реда“ е вярно за КЛЕТКИТЕ, не за редовете. Мерено в C:/git/Fire_Varna/scratch/places_search/imot_decisions_1_2026-09-08_draft.json: `kind == 'район'` носят 21 реда, от които 19 са клетки „да“; другите два са `malka_chaika` и единият `TBD` — и двата с `kind_registry = "кв"`. Ако Ф7 пази `kind_registry` за всичките 98 реда, алтернативата „мр“ мени 21 реда, а `malka_chaika` губи своето „кв“ — точно стойността, върху която стъпва доводът на Р4.
422: - Р15 · разпределенията са проверени и излизат до едно: 79-те клетки дават кв 32 · м-т 27 · жк 10 · кк 4 · пз 3 · зона 2 · вз 1; с петте родителя (kv_levski кв, vladislavovo кв, vazrazhdane жк, mladost жк, pobeda_group кв) става кв 35 · м-т 27 · жк 12 · кк 4 · пз 3 · зона 2 · вз 1 = 84, класове 52/32, а при „мр“ — 16/19/… и 33/51. Р16 също е верен байт по байт: четирите родителя са в регистъра И във v1 с ЕДИН И СЪЩ вид, `pobeda_group` го няма никъде.
423: - `registry_pending` = 27 всъщност ЗАПАЗВА семантиката на v1 (регистров код без ред в тялото с решенията — v1: 16 такива, с довод „регистров код без ред в решенията към 06.09“). Мерено: регистър − (редове на Ф7 ∪ виртуални родители) = 27, а регистър − доставени = 28. Това е добрата новина; лошата е, че кръг 5 никъде не КАЗВА определението с думи — стои само в скоба вътре в Р4. Напишете двете определения в §2/Г.8, за да не се чете 16 → 27 като тиха смяна.
424: - Р10 · `recorded_on` е ново име за поле, което v1 нарича `checked_on` (Ч и в образеца C9: `qa_quarters_signed.py:362` иска `url, checked_on, quote, terms, verdict, position`). Логиката ви е права — да няма `checked_on` за страница, която никой не е отварял — но новото име заслужава ред в Х-пространството, за да не се съди срещу шестицата на v1.
425: - Р18 vs ADR 010 D9 · `--diff-signed` прави над-прагов диф зелен, а D9 казва дословно „`--diff <предишна>` е ГЕЙТ с изход ≠ 0 над праговете (G15)“ (Ч C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:54). Р19 вече има механизма — ред в ADR 011 И-D5 за D0/G23; направете същото и за D9/G15, иначе Одиторът остава да тълкува „G15 не се отменя — изпълнява се“ срещу артефакт с 17 982 сменени думи и +21,1 % площ (двете преизмерени от мен: 21,14 %).
426: - ИБ-14 пропуска едно място: `G29` живее и в ПОДПИСАНИЯ артефакт — `_meta.publication` на v1 („Геометрия НИКОГА не пътува публично (G29)“), при `grep -c G29 010_signed_quarter_boundaries.md` → 0 (проверено). Текстът на `_meta.publication` за v2 по Р10 не бива да наследява името на нерегистриран гейт.
427: - Всичко останало, което успях да меря, излиза ТОЧНО и заслужава да се знае преди подписа: 79 клетки / 5 обекта / 5 села / 6 отложени; 1 025 адреса в петте обекта, всичките извън всяка клетка → 77 211 покрити от 80 510 = 95,90 %, с обектите 78 236 = 97,18 %; 10,691 km² сумарна площ на отложените; медиана на ръба 96,48 m; 16 кода без стойност в колоната АГКК (черновата казва 13 — Х10 е прав); 98 реда → 97 кода, двата `TBD` са 5848 и 5866; регистърът е 84 записа, `schema_version 1.1`, 15 ключа, sha `7d217401…`, ревизия `627b240b`; 245 проследени `.md`, `"advert_id"` в 4 от тях (два са самите планове), 1 902 попадения в `h2_kmz_consolidation_dry_run.md`; `b3_g11.py` GEO `:37`, LEGACY `:39`, ALLOWED_NEW `:40-46` (7 записа), обхватът `:105-106` наистина е сляп за `.md`; `qa_district_official.py` го няма; `data/archive/` наистина не съществува, `docs/archive/` е проследена. И трите проследени документа днес носят НУЛА координати — проверих с точка И със запетая.
428: 

codex
Проверката на реда на комитите намери още един блокер: К5 пренасочва четците към архив, който влиза в историята чак с К6. Таблицата §9 покрива всички изброени от вас решения, но липсват дословните стойности за `license` и `license_terms`, които строителят трябва да вземе от нея.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Картата_imot_И-А_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 254..272 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 472ms:
254: ### 3.А · `varna_3d` — нови файлове
255: 
256: | # | път | какво | комит |
257: |---|---|---|---|
258: | **Ф1** | `src/build_quarters_signed_imot.py` | **НОВ билдър** — правилата в §3.Г | **К4** |
259: | **Ф2** | `src/qa_quarters_signed_imot.py` | **НОВИЯТ ГЕЙТ** — реализира **ИА-1 … ИА-11, ИА-13 … ИА-17**, всяка проверка написана ТУК наново, нищо внесено от `qa_quarters_signed.py`. **CLI-договорът е обявен изчерпателно долу.** | **К4** |
260: | **Ф3** | `tests/test_quarters_signed_imot_fixtures.py` | **реализира ИА-18**: ражда фикстурите в `%TEMP%/ia_fixtures`, прогонва всяка с нейния `--only`, настоява за изход ≠ 0 **по своя номер**; проверява, че гейтът е зелен върху истинския v2 и че двата билда са байт-еднакви | **К4** |
261: | ~~Ф4~~ | — | **ОТПАДА** (ИА-О20): фикстурите са `.geojson`, игнорирани от `.gitignore:23`, и по установената практика на репото **никога не се комитват**. Номерът се оставя празен, за да не мърда останалата номерация. | — |
262: | **Ф5** | `data/imot_bg_varna_polygons_08.09.geojson` | **байтово копие** на снапшота (175 736 B, `77b40564…`) | **К2 · Петър** |
263: | **Ф6** | `data/imot_bg_varna_dictionary_08.09.json` | **байтово копие** на речника (6 274 B, `feba76e3…`) | **К2 · Петър** |
264: | **Ф7** | `data/quarters_decisions_imot_2026-09-08.json` | **каноничното подписано тяло** (Р1) — блобът `8626ad43…` плюс изброените в §3.В **десет** разлики и нищо друго | **К3 · Петър** |
265: | **Ф8** | `docs/archive/quarters_signed_v1_2026-09-06.geojson` | v1, **`git mv`**, байт за байт (301 917 B, `c1551d24…`) | **К6 · Петър** |
266: | **Ф9** | `docs/archive/РЕГИСТЪР_архив.md` | регистърът на архива: `стар път → нов път → комит → защо → кой го чете сега`; първи ред v1, втори ред „черновата с решенията — архивиране в И-Б“, трети ред „`granitsi_decisions_2/3/4` — отменени, физически архивирани в И-Б“ | **К5** |
267: | **Ф10** | `docs/decisions/ПРЕДЛОЖЕНИЕ_регистър_imot_08.09.md` | **само предложение** за `Varna_buildings/config/quarter_registry.json`. Схемата на записа е **измерената**: `id, display, kind, aliases, why` **плюс `parents`** — точно **17** от 28-те нови кода са деца на петте виртуални родителя (М), а йерархията в регистъра се носи от `parents` (М: 6 записа днес го носят). Съдържа: **28**-те нови кода, **28**-те регистрови кода без Feature, отделно четирите жилищни, деветте изчезващи, и **бележка за `malka_chaika`** (регистърът го дава като `м-т`, тялото му дава `kind_registry = "кв"`; редът е `no_boundary`, затова разминаването днес не удря гейт). **Нищо не се прилага.** | **К7** |
268: 
269: **CLI-договорът на Ф2 (обявен, защото три отрицателни половини зависят от него):**
270: `path` — **позиционен, `nargs="?"`** (ИА-О22) · `--registry` · `--tiling <снапшот>` · `--dictionary <речник>` · `--address-rows <път>` · `--districts <слой>` · `--decisions-repo/--decisions-rev/--decisions-path` (**Ф7 във varna_3d**) · `--resolutions-repo/--resolutions-rev/--resolutions-path` (**`district_resolutions_2026-09-07.json` във Fire_Varna**) · `--draft-repo/--draft-rev/--draft-path` (**черновата във Fire_Varna, само за `--decisions-diff`**) · `--diff <път до v1>` · `--diff-signed <низ>` · `--only <ИА-номер>` · `--make-fixtures --fixtures-dir <път>` · `--decisions-diff` · `--privacy-scope <път>` (обхватът на ИА-7: по подразбиране Ф7; повтаря се за всеки допълнителен файл с данни) · `--out <път>`. **(Сверка на Архитекта след кръг 5, ИА-О30: флагът `--privacy-scope` беше ползван от ИА-7, но липсваше тук.)**
271: **Без `--resolutions-*` отрицателната половина на ИА-9 не може да се напише: гейтът би прочел истинския файл и би върнал 0** (кръг 3, БЛОКЕР).
272: 

codex
**НЕГОДНО за подпис в този вид.** ИА-О30 поправя намерението, но оставя противоречив изпълним договор. Одитът е само с четене; нищо не е променяно. Редовете по-долу са от [плана](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md).

Блокери:

1. **Частен провенанс вече стои в проследения план — ред 102.** Цитиран е пълният SHA-256 на **суровия отговор** на речника. Това нарушава червен ред 5, независимо от разрешените обобщени производни в ИА-О24. ИА-7 проверява Ф7, ИА-19 проверява координати, а `b3_g11` пропуска документите: никоя от тези команди не чете този теч. Моят скан на трите документа намира **0 координатни попадения с точка/запетая**, но потвърждава суровия хеш.

2. **Строителят и гейтът изискват несъвместими структури.** Редове **381 и 390** още поръчват шест ключа в `source_terms`, включително такава поправка на ADR 011; **250/451/562** изискват точно три. Ред **321** поръчва `excluded.reason`; **460** го забранява и изисква `why`, `display`, `registry_action`. Следване на строителния раздел произвежда червен гейт. Стойността на `registry_action` за десетте изключени реда също не е определена.

3. **Р10 не дава всички текстове за подпис.** Ред **348** препраща за `license` и `license_terms` „дословно по Р10“, но **562** не съдържа стойностите им; ИА-8 (**451**) ги изисква непразни. Изпълнителят трябва да измисля или пита. Допълнително **381** разрешава публични производни, а **562** блокира публикацията до присъда и сочи несъществуващ **ИБ-20** — §11 завършва с ИБ-18.

4. **ИА-19 има противоположни спирачки.** Ред **462** правилно приема `grep` изход **1** за чист документ. Стъпки 2/17 (**404/419**) още нареждат `ИА-19 ≠ 0 → STOP`. Отрицателна проба с намерени координати връща **0**, а общият STOP 5 (**519**) третира точно това като провал на отрицателната половина. Нужна е единна полярност, включително STOP при грешка на командата.

5. **Две начални операции не изпълняват обещаното.** Стъпка 3 (**405**) очаква `git check-ignore -v` да мълчи след `!` правила; провереният аналог отпечатва разрешаващото правило и връща 0. Стъпка 0 (**402**, Н7) обещава нула редакции, но съществуващият [тест](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:156) изтрива и регенерира фикстури вътре в репото, преди подписа и извън `%TEMP%`. Затова не го стартирах.

6. **К5 е негоден самостоятелен комит — 497–503.** Той пренасочва четците към архив, който влиза чак с К6. Проверката на работното дърво вижда предварително стейджнатия архив и прикрива липсата му в самия К5. Това нарушава изискването за проверими междинни комити. Разделението на ръцете иначе е ясно: **К2/К3/К6 — Петър**, включително `.gitignore`; останалите — код/документи.

7. **ИА-10 доказва повторяемост, но не идентичност на доставката — 260/414/453.** Сравняват се два временни билда, без задължително сравнение с комитвания артефакт. Подменен Feature-хеш при запазена геометрия не е покрит от описаните проверки на входните хешове, схемата и броевете.

8. **Остава необявена промяна на канона.** [ADR 010 D4](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:44) определя `no_boundary` като Feature с `geometry:null`; ADR 011 го оставя непроменен. Р4 (**556**) изрично забранява такъв Feature. ИА-14 (**457**) също допуска четири жилищни кода само „с довод“, извън задължителните множества на D4. Предписаният амандамент на **390** не поправя това.

За сутрешния подпис **§9 покрива всички поисканите теми**: обекти Р3, села Р7, трите без полигон Р4, район→кв/мр Р15, точност Р8, `vinitsa_sever` Р17, архиви Р11, трите ключа Р10. Липсват завършените договори по-горе, а не още общи въпроси към Петър. Нужна е и свежа начална мярка: Д3 вече е чист, докато **402/516** още изискват стария мръсен хънк и задействат STOP още на стъпка 0.
tokens used
76,187
**НЕГОДНО за подпис в този вид.** ИА-О30 поправя намерението, но оставя противоречив изпълним договор. Одитът е само с четене; нищо не е променяно. Редовете по-долу са от [плана](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md).

Блокери:

1. **Частен провенанс вече стои в проследения план — ред 102.** Цитиран е пълният SHA-256 на **суровия отговор** на речника. Това нарушава червен ред 5, независимо от разрешените обобщени производни в ИА-О24. ИА-7 проверява Ф7, ИА-19 проверява координати, а `b3_g11` пропуска документите: никоя от тези команди не чете този теч. Моят скан на трите документа намира **0 координатни попадения с точка/запетая**, но потвърждава суровия хеш.

2. **Строителят и гейтът изискват несъвместими структури.** Редове **381 и 390** още поръчват шест ключа в `source_terms`, включително такава поправка на ADR 011; **250/451/562** изискват точно три. Ред **321** поръчва `excluded.reason`; **460** го забранява и изисква `why`, `display`, `registry_action`. Следване на строителния раздел произвежда червен гейт. Стойността на `registry_action` за десетте изключени реда също не е определена.

3. **Р10 не дава всички текстове за подпис.** Ред **348** препраща за `license` и `license_terms` „дословно по Р10“, но **562** не съдържа стойностите им; ИА-8 (**451**) ги изисква непразни. Изпълнителят трябва да измисля или пита. Допълнително **381** разрешава публични производни, а **562** блокира публикацията до присъда и сочи несъществуващ **ИБ-20** — §11 завършва с ИБ-18.

4. **ИА-19 има противоположни спирачки.** Ред **462** правилно приема `grep` изход **1** за чист документ. Стъпки 2/17 (**404/419**) още нареждат `ИА-19 ≠ 0 → STOP`. Отрицателна проба с намерени координати връща **0**, а общият STOP 5 (**519**) третира точно това като провал на отрицателната половина. Нужна е единна полярност, включително STOP при грешка на командата.

5. **Две начални операции не изпълняват обещаното.** Стъпка 3 (**405**) очаква `git check-ignore -v` да мълчи след `!` правила; провереният аналог отпечатва разрешаващото правило и връща 0. Стъпка 0 (**402**, Н7) обещава нула редакции, но съществуващият [тест](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:156) изтрива и регенерира фикстури вътре в репото, преди подписа и извън `%TEMP%`. Затова не го стартирах.

6. **К5 е негоден самостоятелен комит — 497–503.** Той пренасочва четците към архив, който влиза чак с К6. Проверката на работното дърво вижда предварително стейджнатия архив и прикрива липсата му в самия К5. Това нарушава изискването за проверими междинни комити. Разделението на ръцете иначе е ясно: **К2/К3/К6 — Петър**, включително `.gitignore`; останалите — код/документи.

7. **ИА-10 доказва повторяемост, но не идентичност на доставката — 260/414/453.** Сравняват се два временни билда, без задължително сравнение с комитвания артефакт. Подменен Feature-хеш при запазена геометрия не е покрит от описаните проверки на входните хешове, схемата и броевете.

8. **Остава необявена промяна на канона.** [ADR 010 D4](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:44) определя `no_boundary` като Feature с `geometry:null`; ADR 011 го оставя непроменен. Р4 (**556**) изрично забранява такъв Feature. ИА-14 (**457**) също допуска четири жилищни кода само „с довод“, извън задължителните множества на D4. Предписаният амандамент на **390** не поправя това.

За сутрешния подпис **§9 покрива всички поисканите теми**: обекти Р3, села Р7, трите без полигон Р4, район→кв/мр Р15, точност Р8, `vinitsa_sever` Р17, архиви Р11, трите ключа Р10. Липсват завършените договори по-горе, а не още общи въпроси към Петър. Нужна е и свежа начална мярка: Д3 вече е чист, докато **402/516** още изискват стария мръсен хънк и задействат STOP още на стъпка 0.
