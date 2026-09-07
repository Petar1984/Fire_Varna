Reading additional input from stdin...
OpenAI Codex v0.153.3
--------
workdir: C:\git\varna_3d
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: ultra
reasoning summaries: none
session id: 01a079f7-af2c-7642-b37c-9e6440fbbd01
--------
user
S27 · Повторна проверка на Б2 след S26 (леща механика), read-only. Контекст: твоята присъда S26 (C:/git/Fire_Varna/scratch/places_search/granitsi_b2_astra_S26_07.09.md, последният блок) беше НЕГОДНО с три условия: (1) src/qa_fixed_point.py в C:/git/varna_3d нормализираше JSON и без --ignore (false pass срещу A3); (2) unittest наборът не беше потвърден; (3) комит-текстовете на Петър да са дословните по §6 на амандамент 3. Какво е направено: (1) комит 0ba2e9d в C:/git/varna_3d (Claude Executor): без --ignore гейтът сравнява СУРОВИ байтове (Path.read_bytes), с --ignore пази нормализацията на A3 само за назованите ключове; scratch/granitsi/fixed_point_negatives.py има нова секция 5 (леджер с indent=2 → червено; леджер със CRLF → червено; местата с indent=2 и --ignore → зелено); (2) в главната сесия python -B -m unittest discover -s tests даде 'Ran 16 tests OK' без промени по проследени файлове; (3) трите файла C:/git/varna_3d/scratch/granitsi/COMMIT_MSG_b2_{1_identity,2_exports,3_ledger}.txt имат дословните subject-редове от §6 (ред 63-68 на амандамента), тяло с подписните sha. Задачата ти: измери сам (а) git show 0ba2e9d — само двата файла, автор/committer Claude Executor, кодът наистина чете сурови байтове без --ignore; (б) пусни python -B scratch/granitsi/fixed_point_negatives.py и трите реални сравнения (ledger_run1 срещу леджера сурово; places_run1/hotels_run1 срещу data износите с --ignore _meta.generated) — изходни кодове; (в) провери, че стейджнатите 7 блоба са непокътнати (git cat-file blob :path | sha256sum: 4819ab3e, c7450ded, 3dffc264, eb8fa85c, 9064705a, bb04640e, 5ec64c68) и че 0ba2e9d не съдържа нито един от тях; (г) провери трите комит-текста срещу §6 дословно. Не пипай нищо, не комитвай, никаква команда към отдалечено хранилище. Присъда: ГОДНО за трите комита на Петър или НЕГОДНО с точната причина, кратко (до 400 думи), с измерените изходи.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя локално поправката, изходните кодове, стейджнатите блобове и комит-текстовете. Ще работя само за четене, без комити и без команди към отдалечено хранилище.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "if (Test-Path -LiteralPath 'docs/activeContext.md') { Get-Content -LiteralPath 'docs/activeContext.md' -TotalCount 150 } elseif (Test-Path -LiteralPath 'docs/СЪСТОЯНИЕ.md') { Get-Content -LiteralPath 'docs/СЪСТОЯНИЕ.md' -TotalCount 150 } else { Get-Content -LiteralPath 'СЪСТОЯНИЕ.md' -TotalCount 150 }" in C:\git\varna_3d
 succeeded in 0ms:
# Varna 3D â€” Ð²Ñ…Ð¾Ð´Ð½Ð° Ñ‚Ð¾Ñ‡ÐºÐ°

**Ð”Ð°Ñ‚Ð°:** 02.09.2026 Â· **Ð¿Ð¾ÑÐ»ÐµÐ´Ð½Ð¾ ÑÐ²ÐµÑ€ÐµÐ½Ð¾ ÑÑ€ÐµÑ‰Ñƒ ÐºÐ¾Ð¼Ð¸Ñ‚** 9f55c08 (`rezhimi`; Ð½Ð°Ð¿Ñ€ÐµÐ´ ÑÐ¿Ñ€ÑÐ¼Ð¾ `origin/rezhimi` Ñ ÐºÐ¾Ð¼Ð¸Ñ‚Ð¸Ñ‚Ðµ Ð½Ð° Ð¿Ð»Ð°Ð½Ð° Ð¾Ñ‚ 01.09 Ð´Ð¾ Ð¿ÑƒÑˆÐ° Ð½Ð° ÐŸÐµÑ‚ÑŠÑ€ â€” Ñ‚Ð°Ð±Ð»Ð¸Ñ†Ð°Ñ‚Ð°) Â· ÑÐ²ÐµÑ€Ð¸Ð»: Opus (executor), Ð¾Ð´Ð¸Ñ‚Ð¸Ñ€Ð°Ð»: <Ð¾Ð´Ð¸Ñ‚Ð¾Ñ€> Â· Ð¿Ð¾Ð´Ð¿Ð¸Ñ: __
> Ð’ÑÑÐºÐ¾ Ñ‡Ð¸ÑÐ»Ð¾ Ñ‚ÑƒÐº Ðµ Ð¸Ð·Ñ…Ð¾Ð´ÑŠÑ‚ Ð½Ð° ÐºÐ¾Ð¼Ð°Ð½Ð´Ð°Ñ‚Ð° Ð´Ð¾ Ð½ÐµÐ³Ð¾, Ð¿ÑƒÑÐ½Ð°Ñ‚Ð° Ð½Ð° Ð´Ð°Ñ‚Ð°Ñ‚Ð° Ð³Ð¾Ñ€Ðµ (`verify_numbers.py` Ð³Ð¾ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÑÐ²Ð°). Ð§Ð¸ÑÐ»Ð¾ Ð±ÐµÐ· ÐºÐ¾Ð¼Ð°Ð½Ð´Ð° Ð½Ðµ Ð²Ð»Ð¸Ð·Ð°.
> Ð¥Ñ€Ð¾Ð½Ð¸ÐºÐ°Ñ‚Ð° Ð¿Ð¾ Ð´Ð°Ñ‚Ð¸ Ðµ Ð·Ð°Ð¼Ñ€Ð°Ð·ÐµÐ½Ð° Ð² [Ð¡ÐªÐ¡Ð¢ÐžÐ¯ÐÐ˜Ð•.md](Ð¡ÐªÐ¡Ð¢ÐžÐ¯ÐÐ˜Ð•.md) (Ð´Ð¾ 01.09.2026). Ð˜Ð·Ð²Ð¾Ñ€Ð¸Ñ‚Ðµ ÑÐ° Ð¾Ð¿Ð¸ÑÐ°Ð½Ð¸ Ð² [../DATA.md](../DATA.md) (Ð¼ÐµÑ€ÐµÐ½Ð¸ 30.07.2026).

## ÐšÐ°ÐºÐ²Ð¾ Ðµ Ñ‚Ð¾Ð²Ð°
Ð¢Ñ€Ð¸Ð¸Ð·Ð¼ÐµÑ€ÐµÐ½ Ð¼Ð¾Ð´ÐµÐ» Ð½Ð° Ð’Ð°Ñ€Ð½Ð° Ð¾Ñ‚ ÐšÐÐ˜Ð¡ â€žÐžÑ‚Ð²Ð¾Ñ€ÐµÐ½Ð¸ Ð´Ð°Ð½Ð½Ð¸" â€” ÑÑ‚Ð¾Ð¸ ÐÐÐ” `Varna_buildings` (Ð´Ð°Ð½Ð½Ð¸Ñ‚Ðµ Ð·Ð° ÑÐ³Ñ€Ð°Ð´Ð¸Ñ‚Ðµ) Ð¸ `Fire_Varna` (Ñ…Ð¸Ð´Ñ€Ð°Ð½Ñ‚Ð¸Ñ‚Ðµ), Ñ‡ÐµÑ‚Ðµ Ñ‚ÐµÑ…Ð½Ð¸Ñ‚Ðµ Ð¸Ð·Ñ…Ð¾Ð´Ð¸, Ð½Ðµ Ð³Ð¸ Ð¿Ð¸Ð¿Ð°. ÐŸÑƒÐ±Ð»Ð¸ÐºÑƒÐ²Ð°Ð½Ð¾Ñ‚Ð¾ Ðµ `web/` (ÐºÐ°Ñ€Ñ‚Ð°: `Varna 3D.bat` â†’ http://127.0.0.1:8791).

## Ð¡Ñ‚Ð²Ð¾Ð»ÑŠÑ‚
- Ð Ð°Ð±Ð¾Ñ‚ÐµÐ½ ÐºÐ»Ð¾Ð½: `rezhimi`. ÐšÐ»Ð¾Ð½ÑŠÑ‚ Ð¿Ð¾ Ð¿Ð¾Ð´Ñ€Ð°Ð·Ð±Ð¸Ñ€Ð°Ð½Ðµ Ð² GitHub: `main` (Ð¸Ð·Ñ€Ð°Ð²Ð½ÐµÐ½ Ñ `origin/rezhimi` Ð² Ð›ÐžÐ¢ 3 Ð½Ð° Ð¿Ð»Ð°Ð½Ð° Ð¾Ñ‚ 01.09; Ð¿Ñ€Ð¾ÑÐ»ÐµÐ´ÑÐ²Ð° `origin/main`; Ð·Ð°Ð½Ð°Ð¿Ñ€ÐµÐ´ â€” Ð’-1/Ð -12).

## Ð¢ÐµÐ¼Ð° â€žÑ‚ÑŠÑ€Ð³Ð¾Ð²ÑÐºÐ¾-Ð¾Ð±Ñ‰ÐµÑÑ‚Ð²ÐµÐ½Ð¸Ñ‚Ðµ ÑÐ³Ñ€Ð°Ð´Ð¸" (03.09.2026, ÑÐµÑÐ¸Ñ git-65 / Fable) â€” ÑÑƒÑ€Ð¾Ð²Ð¸ Ð´Ð°Ð½Ð½Ð¸ Ð²ÑŠÐ² Ñ„Ð°Ð¹Ð», Ð½Ð¸Ñ‰Ð¾ Ð² ÐºÐ°Ñ€Ñ‚Ð°Ñ‚Ð°
- **Ð¡ÑŠÑÑ‚Ð¾ÑÐ½Ð¸Ðµ:** Ð¤0 Ð¼ÑÑ€ÐºÐ° (`b8141ec`) â†’ Ð¿Ð»Ð°Ð½ v1.1 Ð¿Ð¾Ð´Ð¿Ð¸ÑÐ°Ð½ Ð¿Ð¾ Ð´ÑƒÐ¼Ð¸Ñ‚Ðµ Ð½Ð° ÐŸÐµÑ‚ÑŠÑ€ (`docs/plans/ÐŸÐ›ÐÐ_Ñ‚ÑŠÑ€Ð³Ð¾Ð²ÑÐºÐ¾-Ð¾Ð±Ñ‰ÐµÑÑ‚Ð²ÐµÐ½Ð¸.md`, Â§11 Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚Ð¸) â†’ Ð»Ð¾Ñ‚Ð¾Ð²Ðµ Ð0/Ð1 (`c74bad0`, `a7f1a68`), Ð4 (`0ccc525`), Ð3 (`12b082f`), Ð5 + Ð±Ð¾Ñ€Ð´ÑŠÑ‚ (`7a4bed5`). ÐŸÐ¾ Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚ â„–1 (â€žÐ·Ð° ÑÐµÐ³Ð° Ð¸Ð½Ñ„Ð¾Ñ‚Ð¾ Ð½Ð° Ñ„Ð°Ð¹Ð»") `build_places.py` ÐÐ• Ðµ Ð¿ÑƒÑÐºÐ°Ð½, Ð¸Ð·Ð½Ð¾Ñ ÐºÑŠÐ¼ Fire_Varna Ð½ÑÐ¼Ð°; Ð2/Ð6/Ð‘/Ð’ Ñ‡Ð°ÐºÐ°Ñ‚ Ð¿Ñ€ÐµÑ†ÐµÐ½ÐºÐ°Ñ‚Ð° Ð½Ð° ÐŸÐµÑ‚ÑŠÑ€. Ð”Ð¾ÐºÐ»Ð°Ð´ÑŠÑ‚: [audits/Ð”ÐžÐšÐ›ÐÐ”_03.09_Ñ‚ÑŠÑ€Ð³Ð¾Ð²ÑÐºÐ¾-Ð¾Ð±Ñ‰ÐµÑÑ‚Ð²ÐµÐ½Ð¸.md](audits/Ð”ÐžÐšÐ›ÐÐ”_03.09_Ñ‚ÑŠÑ€Ð³Ð¾Ð²ÑÐºÐ¾-Ð¾Ð±Ñ‰ÐµÑÑ‚Ð²ÐµÐ½Ð¸.md); Ð±Ð¾Ñ€Ð´ÑŠÑ‚: [audits/Ð‘ÐžÐ Ð”_Ñ‚ÑŠÑ€Ð³Ð¾Ð²ÑÐºÐ¾-Ð¾Ð±Ñ‰ÐµÑÑ‚Ð²ÐµÐ½Ð¸_2026-09-03.md](audits/Ð‘ÐžÐ Ð”_Ñ‚ÑŠÑ€Ð³Ð¾Ð²ÑÐºÐ¾-Ð¾Ð±Ñ‰ÐµÑÑ‚Ð²ÐµÐ½Ð¸_2026-09-03.md).
- **Ð–Ð¸Ð²Ð¸ Ñ‡Ð¸ÑÐ»Ð° Ð½Ð° Ñ‚ÐµÐ¼Ð°Ñ‚Ð°** (03.09.2026):

| ÐšÐ°ÐºÐ²Ð¾ | Ð¡Ñ‚Ð¾Ð¹Ð½Ð¾ÑÑ‚ | ÐšÐ¾Ð¼Ð°Ð½Ð´Ð° |
|---|---|---|
| OSM Ð¼ÐµÑÑ‚Ð° (ÑÑƒÑ€Ð¾Ð²Ð¸) | 1848 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_public_osm_places.json',encoding='utf-8'))['places']))"` |
| ÐÐ¢Ð  Ð—Ð¥Ð  Ð¼ÐµÑÑ‚Ð° (ÑÑƒÑ€Ð¾Ð²Ð¸) | 373 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_ntr_zhr_places.json',encoding='utf-8'))['places']))"` |
| Wikidata Ð¼ÐµÑÑ‚Ð° (ÑÑƒÑ€Ð¾Ð²Ð¸) | 44 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_wikidata_places.json',encoding='utf-8'))['places']))"` |
| Ð¾Ñ„Ð¸Ñ†Ð¸Ð°Ð»Ð½Ð¸ ÑÐ°Ð¹Ñ‚Ð¾Ð²Ðµ (Ð¡Ð¾Ð», ÑÑƒÑ€Ð¾Ð²Ð¸) | 5 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_web_places.json',encoding='utf-8'))['places']))"` |
| Ñ‚ÐµÐ»Ð° Ð² Ð³ÐµÐ¾Ñ„Ð°Ð¹Ð»Ð° / Ñ Ð¸Ð¼Ðµ | 10367 / 1538 | `PYTHONIOENCODING=utf-8 python src/build_public_buildings_geojson.py \| grep '^bodies'` (Ð¸Ð·Ñ…Ð¾Ð´ÑŠÑ‚ Ðµ Ð² `output/`, Ð¸Ð·Ð²ÑŠÐ½ git) |
| Ð¼Ð°ÑÑ‚ÐµÑ€ÑŠÑ‚ `places.json` Ð½ÐµÐ´Ð¾ÐºÐ¾ÑÐ½Ð°Ñ‚ Ð¾Ñ‚ Ñ‚ÐµÐ¼Ð°Ñ‚Ð° | 576 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/places.json',encoding='utf-8'))['places']))"` |

## Ð¢ÐµÐ¼Ð° â€žÐ›ÐžÐ¢ 1Ð² Ð·Ð° Fire_Varna" (04.09.2026, ÑÐµÑÐ¸Ñ git-08) â€” Ð¸Ð¼ÐµÐ½Ð°Ñ‚Ð°, Ð°Ð´Ñ€ÐµÑÐ¸Ñ‚Ðµ, ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð»Ð¸Ñ‚Ðµ
- **Ð¡ÑŠÑÑ‚Ð¾ÑÐ½Ð¸Ðµ:** Ð»Ð¾Ñ‚ Ð (Ð¿ÑÐµÐ²Ð´Ð¾Ð½Ð¸Ð¼Ð¸Ñ‚Ðµ Ñ Ð¸Ð·Ð²Ð¾Ñ€, `1d5ec9a`, `859dbe5`) â†’ Ð»Ð¾Ñ‚ Ð‘ (Ð°Ð´Ñ€ÐµÑÑŠÑ‚ Ñ Ð¸Ð·Ð²Ð¾Ñ€ Ð½Ð° Ð²ÑÐµÐºÐ¸ Ð·Ð°Ð¿Ð¸Ñ, `25a6d79`) â†’ **Ð»Ð¾Ñ‚ Ð’ (P6): ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð»ÑŠÑ‚, Ñ€Ð°Ð¹Ð¾Ð½ÑŠÑ‚ Ð¸ Ð´Ð¾Ð¿ÑŠÐ»Ð½Ð¸Ñ‚ÐµÐ»Ð½Ð¾Ñ‚Ð¾ Ñ Ð¸Ð·Ð²Ð¾Ñ€.** ÐŸÐ»Ð°Ð½ÑŠÑ‚ Ð¸ Ð¿Ð¾Ð´Ð¿Ð¸ÑÑŠÑ‚ ÑÐ° Ð½Ð° Fire_Varna: `Fire_Varna/docs/plans/ÐŸÐ›ÐÐ_Ð›ÐžÐ¢1Ð²-Ð’_ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð»Ð¸Ñ‚Ðµ.md` (Gate 1-Ð’ Ð¿Ð¾Ð´Ð¿Ð¸ÑÐ°Ð½, Â§3Ð·); ADR `Fire_Varna/docs/decisions/008_places_aliases_and_addresses.md`. Ð’ÑŠÐ² Fire_Varna Ð½Ðµ Ðµ Ð¿Ð¸Ð¿Ð°Ð½Ð¾ Ð½Ð¸Ñ‰Ð¾ Ð¾Ñ‚Ñ‚ÑƒÐº â€” Ð¿Ñ€Ð°Ð²Ð¸ ÑÐµ Ð¡ÐÐœÐž Ð°Ñ€Ñ‚ÐµÑ„Ð°ÐºÑ‚ÑŠÑ‚.
- **ÐŸÑ€Ð°Ð²Ð¸Ð»Ð¾Ñ‚Ð¾ (Â§3Ð³, Ð¿Ð¾Ð´Ð¿Ð¸ÑÐ°Ð½Ð¾):** ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð»ÑŠÑ‚ Ðµ Ð¡ÐÐœÐž Ð¶Ð¸Ð»Ð¸Ñ‰Ð½Ð¾ Ð½Ð¸Ð²Ð¾ Ð¿Ð¾ Ñ€ÐµÐ³Ð¸ÑÑ‚ÑŠÑ€Ð° Ð½Ð° ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð»Ð¸Ñ‚Ðµ Ð¸ Ð¡ÐÐœÐž Ñ Ñ‡Ð¾Ð²ÐµÑˆÐºÐ¸ Ð½Ð°Ð¿Ð¸ÑÐ°Ð½ Ð¸Ð·Ð²Ð¾Ñ€ â€” Ñ€ÐµÐ³Ð¸ÑÑ‚Ñ€Ð¾Ð²Ð¸ÑÑ‚ Ð°Ð´Ñ€ÐµÑÐµÐ½ ÑÐµÐ³Ð¼ÐµÐ½Ñ‚ (`REG`) Ð¸Ð»Ð¸ ÐºÐ°Ð´Ð°ÑÑ‚Ñ€Ð°Ð»Ð½Ð¸ÑÑ‚ ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð» Ð½Ð° Ð·Ð°ÐºÐ¾Ñ‚Ð²ÐµÐ½Ð¾Ñ‚Ð¾ Ñ‚ÑÐ»Ð¾ (`KAIS`); Ð±ÐµÐ· Ð¸Ð·Ð²Ð¾Ñ€ â†’ Ñ‡ÐµÑÑ‚Ð½Ð¾ â€žÑ€Ð°Ð¹Ð¾Ð½ X". Ð Ð°Ð¹Ð¾Ð½ÑŠÑ‚ Ð¸Ð´Ð²Ð° Ð¡ÐÐœÐž Ð¾Ñ‚ ÐšÐÐ˜Ð¡ `reg` (Ð¿ÐµÑ‚Ñ‚Ðµ Ð³Ñ€Ð°Ð´ÑÐºÐ¸ Ñ€Ð°Ð¹Ð¾Ð½Ð°, Ð·Ð°Ñ‚Ð²Ð¾Ñ€ÐµÐ½ ÑÐ¿Ð¸ÑÑŠÐº). Ð”Ð¾Ð¿ÑŠÐ»Ð½Ð¸Ñ‚ÐµÐ»Ð½Ð¾Ñ‚Ð¾ (`locality`) Ð½Ð¾ÑÐ¸ Ð¿Ñ€Ð¾Ð¼Ð¸ÑˆÐ»ÐµÐ½Ð¸Ñ‚Ðµ Ð·Ð¾Ð½Ð¸, Ð¿Ð°Ñ€ÐºÐ¾Ð²ÐµÑ‚Ðµ Ð¸ Ð¼ÐµÑÑ‚Ð½Ð¾ÑÑ‚Ð¸Ñ‚Ðµ. **ÐÐ¸Ñ‰Ð¾ Ð½Ð°Ñ€Ð¸ÑÑƒÐ²Ð°Ð½Ð¾ Ð¸ Ð½Ð¸Ñ‰Ð¾ OSM-Ð¿Ñ€Ð¾Ð¸Ð·Ð²Ð¾Ð´Ð½Ð¾ Ð½Ðµ Ñ€ÐµÑˆÐ°Ð²Ð°** â€” Ð¾Ð±Ð²Ð¸Ð²ÐºÐ¸Ñ‚Ðµ, ÐµÑ‚Ð¸ÐºÐµÑ‚-Ñ‚Ð¾Ñ‡ÐºÐ¸Ñ‚Ðµ Ð¸ Ñ€Ð°Ð¹Ð¾Ð½Ð½Ð¸ÑÑ‚ Ð¿Ð¾Ð»Ð¸Ð³Ð¾Ð½ ÑÐ° ÑÐ°Ð¼Ð¾ ÑÑ€Ð°Ð²Ð½Ð¸Ñ‚ÐµÐ»Ð½Ð¸ ÐºÐ¾Ð»Ð¾Ð½Ð¸ Ð² Ð¼Ð°ÑÐºÐ¸Ñ€Ð°Ð½Ð¸Ñ ledger `../scratch/refactor/_addr/lot1v_locations_375.json`.
- **Ð˜Ð·Ð¾Ð»Ð°Ñ†Ð¸Ñ:** Ð½Ð¾Ð²Ð°Ñ‚Ð° ÑÑ‚ÑŠÐ»Ð±Ð° (`src/fire_varna_locations.py`) Ðµ Fire-export-only. Ð“Ð»Ð¾Ð±Ð°Ð»Ð½Ð°Ñ‚Ð° `src/place_zones.py`, Ð¼Ð°Ð¹ÑÑ‚Ð¾Ñ€ÑŠÑ‚ Ð¸ Ð°Ñ€Ñ‚ÐµÑ„Ð°ÐºÑ‚Ð¸Ñ‚Ðµ Ð½Ð° Ð¿Ð°Ñ€Ð°Ð»ÐµÐ»Ð½Ð°Ñ‚Ð° Ñ‚ÐµÐ¼Ð° Ð½Ðµ Ð¼ÑŠÑ€Ð´Ð°Ñ‚ â€” Ð´Ð¾ÐºÐ°Ð·Ð²Ð° Ð³Ð¾ `src/qa_fire_varna_location_isolation.py` (G-ISO) ÑÑ€ÐµÑ‰Ñƒ Ð·Ð°ÐºÐ¾Ð²Ð°Ð½Ð¸Ñ‚Ðµ Ð²Ñ…Ð¾Ð´Ð¾Ð²Ðµ `data/fire_varna_location_inputs.json`.
- **Ð§Ð°ÐºÐ° Ð¿Ð¾Ð´Ð¿Ð¸Ñ:** Ð¼Ð°Ð½Ð¸Ñ„ÐµÑÑ‚ÑŠÑ‚ old â†’ new (209 Ñ€ÐµÐ´Ð°) Ð¿Ñ€ÐµÐ´Ð¸ Ð·Ð°Ð¼Ñ€Ð°Ð·ÑÐ²Ð°Ð½ÐµÑ‚Ð¾ Ð½Ð° Ñ€ÐµÑ„ÐµÑ€ÐµÐ½Ñ†Ð¸ÑÑ‚Ð° Ð²ÑŠÐ² Fire_Varna; Ñ„Ð¸ÐºÑ-Ð¸Ð·Ð²Ð°Ð´ÐºÐ°Ñ‚Ð° Ð·Ð° Ð¾ÐºÐ¾Ñ‚Ð¾ Ð½Ð° ÐŸÐµÑ‚ÑŠÑ€ Ðµ Ð² ledger-Ð°.
- **Ð¥Ð¸Ð³Ð¸ÐµÐ½Ð° ÑÐ»ÐµÐ´ Ð¾Ð´Ð¸Ñ‚Ð° Ð½Ð° Ð»Ð¾Ñ‚ Ð’ (P6-Ð±):** SHA-Ñ‚Ð¾ Ð½Ð° Ð´Ð¾ÑÑ‚Ð°Ð²ÐºÐ° ÑÐµ ÑÐ¼ÑÑ‚Ð° Ð²ÑŠÑ€Ñ…Ñƒ LF-Ð½Ð¾Ñ€Ð¼Ð°Ð»Ð¸Ð·Ð¸Ñ€Ð°Ð½Ð¸ Ð±Ð°Ð¹Ñ‚Ð¾Ð²Ðµ â€” Ñ‚Ð¾ÐµÑÑ‚ Ðµ SHA-Ñ‚Ð¾ Ð½Ð° Ð±Ð»Ð¾Ð±Ð° (`git show HEAD:<Ð¿ÑŠÑ‚>`), Ð½Ðµ Ð½Ð° Ð±Ð°Ð¹Ñ‚Ð¾Ð²ÐµÑ‚Ðµ Ð½Ð° Ñ‚Ð¾Ð·Ð¸ Ð´Ð¸ÑÐº (Ð¿Ñ€ÑÑÐ½Ð¾ Ð·Ð°Ð¿Ð¸ÑÐ°Ð½Ð¸ÑÑ‚ Ð¸Ð·Ð½Ð¾Ñ Ðµ CRLF, Ð¿Ñ€ÑÑÐ½Ð¾ Ð¸Ð·Ñ‚ÐµÐ³Ð»ÐµÐ½Ð¸ÑÑ‚ â€” LF); Ð·Ð°Ñ‚Ð¾Ð²Ð° Ð³ÐµÐ¹Ñ‚ÑŠÑ‚ (g) Ð½Ð° `qa_place_zone_aliases.py` Ð¸ G-ISO Ð¾Ñ‚Ð³Ð¾Ð²Ð°Ñ€ÑÑ‚ ÐµÐ´Ð½Ð°ÐºÐ²Ð¾ Ð² Ñ€Ð°Ð±Ð¾Ñ‚Ð½Ð¾Ñ‚Ð¾ Ð´ÑŠÑ€Ð²Ð¾ Ð¸ Ð² Ñ‡Ð¸ÑÑ‚ worktree. `data/registry_manifest.json` Ðµ ÐºÐ¾Ð¼Ð¸Ñ‚Ð½Ð°Ñ‚ (22 ÑÑ‚Ð¾Ð¹Ð½Ð¾ÑÑ‚Ð¸ `zone` Ð² `grandfathered`/`board_queue`; ÑÐµÐºÑ†Ð¸ÑÑ‚Ð° `rows` Ðµ Ð¸Ð´ÐµÐ½Ñ‚Ð¸Ñ‡Ð½Ð° Ñ P6), Ð·Ð°Ñ‚Ð¾Ð²Ð° Ð¿Ð¸Ð½ÑŠÑ‚ Ð¼Ñƒ Ð²ÐµÑ‡Ðµ ÑÐ¾Ñ‡Ð¸ Ð±Ð»Ð¾Ð± Ð¾Ñ‚ Ð¸ÑÑ‚Ð¾Ñ€Ð¸ÑÑ‚Ð°. Ledger-ÑŠÑ‚ Ð½Ð¾ÑÐ¸ `_meta.fix_sample_why` (Ð´Ð¾Ð²Ð¾Ð´Ð¸Ñ‚Ðµ ÑÐµ Ð˜Ð—Ð’Ð•Ð–Ð”ÐÐ¢ Ð¾Ñ‚ Ð¿Ð¾Ð»ÐµÑ‚Ð°Ñ‚Ð° Ð½Ð° Ñ€ÐµÐ´Ð°) Ð¸ `_meta.open_question_map_label`: 6 Ñ€ÐµÐ´Ð° Ð³ÑƒÐ±ÑÑ‚ ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð»Ð° ÑÐ¸ Ð¿Ð¾ `map_label:false`, 5 Ð¾Ñ‚ Ñ‚ÑÑ… Ñ Ñ‡Ð¾Ð²ÐµÑˆÐºÐ¸ Ð½Ð°Ð¿Ð¸ÑÐ°Ð½ Ñ€ÐµÐ³Ð¸ÑÑ‚Ñ€Ð¾Ð² ÑÐµÐ³Ð¼ÐµÐ½Ñ‚ (Ð”Ð“ 32, Ð”Ð“ 36) â€” Ð·Ð° Ñ€ÐµÑˆÐµÐ½Ð¸Ðµ Ð½Ð° ÐŸÐµÑ‚ÑŠÑ€.
- **Ð–Ð¸Ð²Ð¸ Ñ‡Ð¸ÑÐ»Ð° Ð½Ð° Ñ‚ÐµÐ¼Ð°Ñ‚Ð°** (04.09.2026):

| ÐšÐ°ÐºÐ²Ð¾ | Ð¡Ñ‚Ð¾Ð¹Ð½Ð¾ÑÑ‚ | ÐšÐ¾Ð¼Ð°Ð½Ð´Ð° |
|---|---|---|
| Ð´Ð¾ÑÑ‚Ð°Ð²ÐµÐ½Ð¸ Ð·Ð°Ð¿Ð¸ÑÐ° (Ð¼ÐµÑÑ‚Ð° + Ñ…Ð¾Ñ‚ÐµÐ»Ð¸) | 375 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
| Ñ ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð» (REG 34 Â· KAIS 94 Â· Ð¿Ð¾Ð´Ð¿Ð¸ÑÐ°Ð½ override 12) | 140 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
| Ñ Ð´Ð¾Ð¿ÑŠÐ»Ð½Ð¸Ñ‚ÐµÐ»Ð½Ð¾ Ð¼ÐµÑÑ‚Ð¾Ð¿Ð¾Ð»Ð¾Ð¶ÐµÐ½Ð¸Ðµ | 8 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
| Ñ Ñ€Ð°Ð¹Ð¾Ð½ (100 % Ð¿Ð¾ÐºÑ€Ð¸Ñ‚Ð¸Ðµ, Ð½ÑƒÐ»Ð° ÐºÐ°Ñ€Ð°Ð½Ñ‚Ð¸Ð½Ð°) | 375 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
| ÑÐ¼ÐµÐ½ÑÑ‚ Ð·Ð¾Ð½Ð° ÑÐ¿Ñ€ÑÐ¼Ð¾ Ð´Ð¾ÑÑ‚Ð°Ð²ÐµÐ½Ð¾Ñ‚Ð¾ (Ð¼Ð°Ð½Ð¸Ñ„ÐµÑÑ‚ÑŠÑ‚) | 209 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| tail -1` |
| G-ISO: Ð³Ð»Ð¾Ð±Ð°Ð»Ð½Ð°Ñ‚Ð° ÑÑ‚ÑŠÐ»Ð±Ð° Ð¸ Ñ‡ÑƒÐ¶Ð´Ð°Ñ‚Ð° Ñ‚ÐµÐ¼Ð° Ð½ÐµÐ¿Ð¾ÐºÑŠÑ‚Ð½Ð°Ñ‚Ð¸ | Ð¼Ð¸Ð½Ð°Ð²Ð° | `PYTHONIOENCODING=utf-8 python src/qa_fire_varna_location_isolation.py \| tail -1` |
| ÑÐ°Ð¼Ð¾Ð»Ð¸Ñ‡Ð½Ð¾ÑÑ‚Ð¸ Ñ Ð½ÐµÐ¿Ñ€Ð¾Ð¼ÐµÐ½ÐµÐ½ `place_id` | 375 (0 Ð½Ð¾Ð²Ð¸) | `PYTHONIOENCODING=utf-8 python src/place_identity.py \| grep 'Ð¾Ð±ÐµÐºÑ‚Ð°'` |

## ÐžÑ‚Ð²Ð¾Ñ€ÐµÐ½Ð° Ñ‚ÐµÐ¼Ð° (ÐºÑŠÐ¼ 01.09.2026, Ð¿Ð¾ Ð¡ÐªÐ¡Ð¢ÐžÐ¯ÐÐ˜Ð•.md Â§ 01.09)
- **Ð¡ÐµÐºÑ†Ð¸Ð¸ Ð¾Ñ‚ Ð°Ð¿Ð°Ñ€Ñ‚Ð°Ð¼ÐµÐ½Ñ‚Ð¸ v1.3** â€” Ð¾Ð´Ð¸Ñ‚ Ð“ÐžÐ”ÐÐž, **Ñ‡Ð°ÐºÐ° Gate 2** Ð²ÑŠÑ€Ñ…Ñƒ [Ð¸Ð·Ð²Ð°Ð´ÐºÐ°Ñ‚Ð°](../scratch/refactor/_addr/ÐŸÐ Ð•Ð“Ð›Ð•Ð”_Ð¸Ð·Ð²Ð°Ð´ÐºÐ°_ÑÐµÐºÑ†Ð¸Ð¸_01.09.md) (Ð±Ñ€Ð¾ÑÑ‚ Ð¼ÐµÑÑ‚Ð° Ðµ Ð¿Ð¾ Ð´Ð¾ÐºÑƒÐ¼ÐµÐ½Ñ‚Ð°; Ð½ÐµÐ¿Ñ€Ð¾Ð²ÐµÑ€ÐµÐ½Ð¾ 01.09.2026); ÑÐ»ÐµÐ´ â€žÐ´Ð°Ð²Ð°Ð¹" â€” Ð¤4-ÑÐ»Ð¸Ð²Ð°Ð½Ðµ. Ð”Ð°Ð»Ð¸ Gate 2 Ðµ Ð´Ð°Ð´ÐµÐ½ ÑÐ»ÐµÐ´ 01.09: Ð½ÐµÐ¿Ñ€Ð¾Ð²ÐµÑ€ÐµÐ½Ð¾ (01.09.2026), Ð’-2.
- **Ð’Ñ…Ð¾Ð´Ð¾Ð²Ðµ Ð±ÐµÐ· Ñ€ÐµÐ³Ð¸ÑÑ‚ÑŠÑ€ v2.1** â€” Ð¿Ð¾Ð´Ð¿Ð¸ÑÐ°Ð½; [Ð±Ð¾Ñ€Ð´ÑŠÑ‚](../scratch/refactor/_addr/Ð‘ÐžÐ Ð”_Ð¸Ð·Ð²ÐµÐ´ÐµÐ½Ð¸_Ð²Ñ…Ð¾Ð´Ð¾Ð²Ðµ_66.md) (ÑÐ³Ñ€Ð°Ð´Ð¸/Ð²Ñ…Ð¾Ð´Ð¾Ð²Ðµ Ð¿Ð¾ Ð·Ð°Ð³Ð»Ð°Ð²Ð¸ÐµÑ‚Ð¾ Ð½Ð° Ð´Ð¾ÐºÑƒÐ¼ÐµÐ½Ñ‚Ð°; Ð½ÐµÐ¿Ñ€Ð¾Ð²ÐµÑ€ÐµÐ½Ð¾ 01.09.2026) Ñ‡Ð°ÐºÐ° Ð²Ð¸Ð·ÑƒÐ°Ð»Ð½Ð°Ñ‚Ð° Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° Ð½Ð° ÐŸÐµÑ‚ÑŠÑ€. ÐÐµÐ¿Ñ€Ð¾Ð²ÐµÑ€ÐµÐ½Ð¾ ÑÐ»ÐµÐ´ 01.09 (Ð’-2).
- **Ð Ð¸Ð¼ÑÐºÐ¸ Ñ†Ð¸Ñ„Ñ€Ð¸ Ð² Ð¸Ð¼ÐµÐ½Ð°Ñ‚Ð°** â€” [ÐŸÐ›ÐÐ_Ñ€Ð¸Ð¼ÑÐºÐ¸_Ñ†Ð¸Ñ„Ñ€Ð¸.md](plans/ÐŸÐ›ÐÐ_Ñ€Ð¸Ð¼ÑÐºÐ¸_Ñ†Ð¸Ñ„Ñ€Ð¸.md) v1.1: Ð¼ÑÑ€ÐºÐ°Ñ‚Ð° (11/370 poi, 3/576 Ð¼ÐµÑÑ‚Ð°, 8 Ð² Ñ€ÐµÐ³Ð¸ÑÑ‚ÑŠÑ€Ð° Ð½Ð° ÐœÐžÐ; Ð¿Ñ€Ð°Ð²Ð¸Ð»Ð¾Ñ‚Ð¾ ÐÐ• Ð² `skel` â€” 1 872 Ð°Ð´Ñ€ÐµÑÐ½Ð¸ â€žÐ¸â€œ), Ð¡Ð¾Ð» ÑÑŠÐ±Ð¾Ñ€Ð¸ v1 (4 Ð±Ð»Ð¾ÐºÐµÑ€Ð°) â€” Ñ‡Ð°ÐºÐ° Ð¿Ð¾Ð¿Ñ€Ð°Ð²ÐµÐ½ Ð¿Ð»Ð°Ð½ + Ð¿Ð¾Ð´Ð¿Ð¸Ñ; Ð½Ðµ Ðµ Ð¸Ð·Ð¿ÑŠÐ»Ð½ÑÐ²Ð°Ð½Ð¾.
- **Ð¤Ð°Ð·Ð° 2 Ð½Ð° Ð¼ÐµÑÑ‚Ð°Ñ‚Ð° Ð·Ð° Fire_Varna** (ÑƒÑ‡Ð¸Ð»Ð¸Ñ‰Ð°/ÑƒÐ½Ð¸Ð²ÐµÑ€ÑÐ¸Ñ‚ÐµÑ‚Ð¸/Ð±Ð¾Ð»Ð½Ð¸Ñ†Ð¸/Ð”ÐšÐ¦/Ñ…Ð¾ÑÐ¿Ð¸ÑÐ¸/Ð´ÐµÑ‚ÑÐºÐ¸ Ð³Ñ€Ð°Ð´Ð¸Ð½Ð¸) â€” Ð˜Ð—ÐŸÐªÐ›ÐÐ•ÐÐ: Ð¸Ð·Ð½Ð¾ÑÑŠÑ‚ `data/fire_varna_places.json` (135 Ð¼ÐµÑÑ‚Ð°, 74 Ð¸Ð·ÐºÐ»ÑŽÑ‡ÐµÐ½Ð¸ Ð¿Ð¾Ð¸Ð¼ÐµÐ½Ð½Ð¾; ff760e3) Ð¸ ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð»ÑŠÑ‚/Ñ€Ð°Ð¹Ð¾Ð½ÑŠÑ‚ Ð¿Ð¾ ÑÑ‚ÑŠÐ»Ð±Ð°Ñ‚Ð° Ð·Ð° Ð¼ÐµÑÑ‚Ð°Ñ‚Ð° Ð¸ Ñ…Ð¾Ñ‚ÐµÐ»Ð¸Ñ‚Ðµ (ba78a25); Ð¿Ð»Ð°Ð½ÑŠÑ‚ v1.5 Ðµ ÐºÐ¾Ð¿Ð¸Ðµ Ð½Ð° `Fire_Varna/docs/plans/places_phase2_plan.md` ([ÐŸÐ›ÐÐ_Ñ„Ð°Ð·Ð°2_Ð¼ÐµÑÑ‚Ð°.md](plans/ÐŸÐ›ÐÐ_Ñ„Ð°Ð·Ð°2_Ð¼ÐµÑÑ‚Ð°.md)); Ð¼ÑÑ€ÐºÐ°Ñ‚Ð° Ð½Ð° Ñ„ÑƒÐ½Ð¸ÑÑ‚Ð° Ð² [../scratch/refactor/_addr/Ð¤Ð£ÐÐ˜Ð¯_Ñ„Ð°Ð·Ð°2_02.09.md](../scratch/refactor/_addr/Ð¤Ð£ÐÐ˜Ð¯_Ñ„Ð°Ð·Ð°2_02.09.md). ÐžÑ‚Ð²Ð¾Ñ€ÐµÐ½Ð¾ Ð·Ð° Ð¿Ð¾Ð´Ð¿Ð¸Ñ (Â§10): ÐŸ7 â€” ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð»Ð½Ð¸Ñ‚Ðµ Ð¿ÑÐµÐ²Ð´Ð¾Ð½Ð¸Ð¼Ð¸ Ð¾Ñ‚ Ñ€ÐµÐ³Ð¸ÑÑ‚ÑŠÑ€Ð° Ð² `data/place_categories.json` (`build_place_categories.py`, ÐºÐ»ÑŽÑ‡ `zones`); Ð»Ð¾Ñ‚ Ð”5 â€” 53-Ñ‚Ðµ Ð¾Ð±Ñ‰Ð¸Ð½ÑÐºÐ¸ Ð´ÐµÑ‚ÑÐºÐ¸ Ð³Ñ€Ð°Ð´Ð¸Ð½Ð¸ Ð¾Ñ‚ Ð¸Ð·Ð²Ð°Ð´ÐºÐ°Ñ‚Ð° 19.08 Ð²ÑŠÑ€Ñ…Ñƒ ÐšÐÐ˜Ð¡-Ð¿Ð°Ñ€Ñ†ÐµÐ»Ð¸Ñ‚Ðµ (Ð’Ð»Ð°Ð´Ð¸ÑÐ»Ð°Ð²Ð¾Ð²Ð¾: 2 Ð¾Ñ‚ Ð¿Ð¾Ð½Ðµ 5 Ð² Ð´Ð¾ÑÑ‚Ð°Ð²ÐºÐ°Ñ‚Ð°). Ð ÐµÑˆÐµÐ½Ð¸ÑÑ‚Ð° Ð½Ð° ÐŸÐµÑ‚ÑŠÑ€ (Ð»Ð¸Ñ†ÐµÐ½Ð·ÑŠÑ‚ Ð½Ð° Ñ€ÐµÐ³Ð¸ÑÑ‚Ñ€Ð¸Ñ‚Ðµ, ODbL Ð²ÑŠÑ€Ñ…Ñƒ bundle-Ð°, ÐœÐ¦ Ð²ÑŠÐ½/Ð²ÑŠÑ‚Ñ€Ðµ) â€” Ð² Ð´Ð¾ÐºÐ»Ð°Ð´Ð° Ð½Ð° Fire_Varna.

## Ð§Ð°ÐºÐ° Ð¿Ð¾Ð´Ð¿Ð¸Ñ / Ð¿Ñ€ÐµÐ³Ð»ÐµÐ´
- Gate 2 Ð½Ð° ÑÐµÐºÑ†Ð¸Ð¸Ñ‚Ðµ (Ð³Ð¾Ñ€Ðµ) Â· Ð²Ð¸Ð·ÑƒÐ°Ð»Ð½Ð°Ñ‚Ð° Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° Ð½Ð° Ð²Ñ…Ð¾Ð´Ð¾Ð²ÐµÑ‚Ðµ (Ð³Ð¾Ñ€Ðµ) Â· Ð½ÐµÐ¿ÑƒÑˆÐ½Ð°Ñ‚Ð¸Ñ‚Ðµ ÐºÐ¾Ð¼Ð¸Ñ‚Ð¸ (Ñ‡Ð¸ÑÐ»Ð°Ñ‚Ð° Ð´Ð¾Ð»Ñƒ) â€” Ð¿ÑƒÑˆÑŠÑ‚ Ðµ Ð½Ð° ÐŸÐµÑ‚ÑŠÑ€.

## ÐŸÐ¾ÑÐ»ÐµÐ´Ð½Ð¸ÑÑ‚ Ð´Ð¾ÐºÐ»Ð°Ð´
- [audits/Ð”ÐžÐšÐ›ÐÐ”_01.09_ÑÐµÐºÑ†Ð¸Ð¸_Ð¸_Ð²Ñ…Ð¾Ð´Ð¾Ð²Ðµ.md](audits/Ð”ÐžÐšÐ›ÐÐ”_01.09_ÑÐµÐºÑ†Ð¸Ð¸_Ð¸_Ð²Ñ…Ð¾Ð´Ð¾Ð²Ðµ.md)

## Ð–Ð¸Ð²Ð¸ Ñ‡Ð¸ÑÐ»Ð°
| ÐšÐ°ÐºÐ²Ð¾ | Ð¡Ñ‚Ð¾Ð¹Ð½Ð¾ÑÑ‚ | ÐšÐ¾Ð¼Ð°Ð½Ð´Ð° |
|---|---|---|
| ÐºÐ¾Ð¼Ð¸Ñ‚Ð¸ Ð½Ð° `rezhimi` | 469 | `git rev-list --count rezhimi` |
| Ð¿Ð¾ÑÐ»ÐµÐ´ÐµÐ½ Ð¿ÑƒÑˆÐ½Ð°Ñ‚ ÐºÐ¾Ð¼Ð¸Ñ‚ | 1a8e170 2026-08-31 | `git log -1 --format='%h %cs' origin/rezhimi` |
| Ð½ÐµÐ¿ÑƒÑˆÐ½Ð°Ñ‚Ð¸ ÐºÑŠÐ¼ `origin/rezhimi` | 15 | `git rev-list --count origin/rezhimi..rezhimi` |
| Ð¿ÑƒÐ±Ð»Ð¸ÐºÑƒÐ²Ð°Ð½Ð¾ Ð¿Ð¾ÐºÐ¾Ð»ÐµÐ½Ð¸Ðµ Ð½Ð° ÐºÐ°Ð´Ð°ÑÑ‚ÑŠÑ€Ð° | 24.07.2026 | `PYTHONIOENCODING=utf-8 python -c "import json;print(json.load(open('web/varna_buildings_3d.manifest.json',encoding='utf-8'))['generation']['buildings'])"` |
| ÑÐ³Ñ€Ð°Ð´Ð¸ Ð² Ð¿ÑƒÐ±Ð»Ð¸ÐºÑƒÐ²Ð°Ð½Ð¸Ñ ÑÐ»Ð¾Ð¹ | 80497 | `PYTHONIOENCODING=utf-8 python -c "import json;print(json.load(open('web/varna_buildings_3d.manifest.json',encoding='utf-8'))['buildings'])"` |
| ÑÐµÐºÑ†Ð¸Ð¸ (3D) | 2101 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('web/varna_sections_3d.geojson',encoding='utf-8'))['features']))"` |
| Ð¸Ð·Ð²ÐµÐ´ÐµÐ½Ð¸ Ð²Ñ…Ð¾Ð´Ð¾Ð²Ðµ | 11748 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('web/varna_entrances_derived.geojson',encoding='utf-8'))['features']))"` |
| Ð¼ÐµÑÑ‚Ð° (`places.json`) | 576 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/places.json',encoding='utf-8'))['places']))"` |
| Ð³ÐµÐ¹Ñ‚ â€žÐ½ÑƒÐ»Ð° ÐºÐ°Ð´Ð°ÑÑ‚Ñ€Ð°Ð»Ð½Ð¸ Ð¸Ð´ÐµÐ½Ñ‚Ð¸Ñ„Ð¸ÐºÐ°Ñ‚Ð¾Ñ€Ð¸" | Ð¼Ð¸Ð½Ð°Ð²Ð° | `PYTHONIOENCODING=utf-8 python src/qa_no_cad_ids.py \| tail -1 \| cut -d' ' -f1` |

> Ð”Ð²Ð°Ñ‚Ð° Ñ€ÐµÐ´Ð° Ð·Ð° Ð±Ñ€Ð¾Ð¹ ÐºÐ¾Ð¼Ð¸Ñ‚Ð¸ (â€žÐºÐ¾Ð¼Ð¸Ñ‚Ð¸ Ð½Ð° `rezhimi`â€œ Ð¸ â€žÐ½ÐµÐ¿ÑƒÑˆÐ½Ð°Ñ‚Ð¸ ÐºÑŠÐ¼ `origin/rezhimi`â€œ) Ð¼ÑŠÑ€Ð´Ð°Ñ‚ Ñ +1 Ð¿Ñ€Ð¸ Ð²ÑÐµÐºÐ¸ ÐºÐ¾Ð¼Ð¸Ñ‚ â€” Ð²ÐºÐ»ÑŽÑ‡Ð¸Ñ‚ÐµÐ»Ð½Ð¾ Ñ‚Ð¾Ð·Ð¸, ÐºÐ¾Ð¹Ñ‚Ð¾ Ð´Ð¾Ð±Ð°Ð²Ñ Ñ„Ð°Ð¹Ð»Ð°; ÑÐ²ÐµÑ€ÐºÐ°Ñ‚Ð° Ðµ ÑÐ¿Ñ€ÑÐ¼Ð¾ ÐºÐ¾Ð¼Ð¸Ñ‚Ð° Ð² Ñ€ÐµÐ´ 3 (= `git rev-parse --short HEAD~1` Ð²ÐµÐ´Ð½Ð°Ð³Ð° ÑÐ»ÐµÐ´ ÐºÐ¾Ð¼Ð¸Ñ‚Ð° Ð½Ð° Ð›ÐžÐ¢ 5). Ð—Ð°Ñ‚Ð¾Ð²Ð° `verify_numbers.py` Ð²ÑŠÑ€Ñ…Ñƒ ÐºÐ¾Ð¼Ð¸Ñ‚Ð½Ð°Ñ‚Ð¸Ñ Ñ„Ð°Ð¹Ð» Ð¿Ð¾ÐºÐ°Ð·Ð²Ð° Ñ‚Ð¾Ñ‡Ð½Ð¾ Ñ‚ÐµÐ·Ð¸ Ð´Ð²Ð° Ñ€ÐµÐ´Ð° Ñ +1.

> Ð”Ð¾ÑÑ‚Ð°Ð²ÐºÐ°Ñ‚Ð° `fire_varna_hotels.json` Ðµ Ð¿Ð¾Ñ‚Ñ€ÐµÐ±ÐµÐ½Ð° Ð¾Ñ‚ Fire_Varna ÐºÐ°Ñ‚Ð¾ Ð¿Ñ€Ð¾ÑÐ»ÐµÐ´ÐµÐ½Ð¸Ñ LF-blob Ð½Ð° HEAD 9f55c08 (OID `4c5d72c4â€¦`, 78 601 B) â€” ÐºÐ¾Ð¼Ð°Ð½Ð´Ð°Ñ‚Ð°: `git rev-parse HEAD:data/fire_varna_hotels.json`

## Ð—Ð°Ð±Ñ€Ð°Ð½ÐµÐ½Ð¾ Ñ‚ÑƒÐº
- `git push` â€” ÑÐ°Ð¼Ð¾ ÐŸÐµÑ‚ÑŠÑ€. ÐšÐ°Ð´Ð°ÑÑ‚Ñ€Ð°Ð»ÐµÐ½ Ð¸Ð´ÐµÐ½Ñ‚Ð¸Ñ„Ð¸ÐºÐ°Ñ‚Ð¾Ñ€ Ð¸Ð·Ð²ÑŠÐ½ `C:\git\m6000_private` â€” Ð³ÐµÐ¹Ñ‚ÑŠÑ‚ `src/qa_no_cad_ids.py`. OSM Ð´Ð°Ð½Ð½Ð¸ Ð² Ð¼Ð¾Ð´ÐµÐ»Ð° â€” ÑÐ°Ð¼Ð¾ ÑÑ€Ð°Ð²Ð½ÑÐ²Ð°Ñ‚ (Ð¤ÐÐ—Ð_0, ÑƒÑÐ»Ð¾Ð²Ð¸Ðµ 4). `git checkout main` / `clean -fd` / `reset --hard`, Ð´Ð¾ÐºÐ°Ñ‚Ð¾ Ð¸Ð¼Ð° Ð½ÐµÑÐ»ÐµÐ´ÐµÐ½Ð¸ Ñ„Ð°Ð¹Ð»Ð¾Ð²Ðµ. Ð”Ð°Ð½Ð½Ð¸ Ð² git â€” `.gitignore` Ñ€ÐµÐ´ 1 (Ð¸Ð·ÐºÐ»ÑŽÑ‡ÐµÐ½Ð¸ÑÑ‚Ð° ÑÐ° Ð¸Ð·Ð±Ñ€Ð¾ÐµÐ½Ð¸ Ñ‚Ð°Ð¼).

## ÐšÑŠÐ´Ðµ ÑÐ° Ð½ÐµÑ‰Ð°Ñ‚Ð°
- `docs/plans` Â· `docs/audits` Â· `docs/sessions` Â· `docs/research` Â· `docs/decisions` (+ Ð¸Ð½Ð´ÐµÐºÑ) Â· `docs/measurement` Â· `docs/Ð¡ÐªÐ¡Ð¢ÐžÐ¯ÐÐ˜Ð•.md` â€” Ð¿Ð¾ Ð¿Ð»Ð°Ð½Ð° Ð¾Ñ‚ 01.09 (Ð›ÐžÐ¢ 4). `docs/sessions/ÐŸÐ ÐžÐœÐŸÐ¢_20.08.md` Ðµ Ð¸Ð·Ð²ÑŠÐ½ git (Ð -4: Ð½Ð¾ÑÐ¸ ÐºÐ°Ð´Ð°ÑÑ‚Ñ€Ð°Ð»ÐµÐ½ Ð¸Ð´ÐµÐ½Ñ‚Ð¸Ñ„Ð¸ÐºÐ°Ñ‚Ð¾Ñ€). `ÐŸÐ›ÐÐ_ÐŸ2Ð²_Ñ‚ÐµÑ€ÐµÐ½Ð°.md` Ð¾ÑÑ‚Ð°Ð²Ð° Ð² ÐºÐ¾Ñ€ÐµÐ½Ð°: Ð²Ñ…Ð¾Ð´ Ð½Ð° ÐºÐ¾Ð½Ð²ÐµÐ¹ÐµÑ€Ð° (`src/qa_no_extrude.py`).
- `scratch/refactor/_addr/` â€” Ð´Ð¾ÐºÐ°Ð·Ð°Ñ‚ÐµÐ»ÑÑ‚Ð²ÐµÐ½Ð°Ñ‚Ð° Ð±Ð°Ð·Ð° (Ð¼ÐµÑ€ÐºÐ¸, Ð±Ð¾Ñ€Ð´Ð¾Ð²Ðµ, Ñ€Ð°Ð·ÑÐ»ÐµÐ´Ð²Ð°Ð½Ð¸Ñ, Ð°Ñ‚Ð°ÐºÐ¸Ñ‚Ðµ Ð½Ð° Kimi/Sol); `scratch/web_probes/` â€” Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ°Ñ‚Ð° Ð¿Ñ€ÐµÐ· Ð¸ÑÑ‚Ð¸Ð½ÑÐºÐ¸ Chrome (README Ð²ÑŠÑ‚Ñ€Ðµ).
- Ð˜Ð·Ð²ÑŠÐ½ git: `C:\git\m6000_private\` (Ð½Ð¾ÑÐ¸ ÐºÐ°Ð´Ð°ÑÑ‚Ñ€Ð°Ð»Ð½Ð¸ Ð¸Ð´ÐµÐ½Ñ‚Ð¸Ñ„Ð¸ÐºÐ°Ñ‚Ð¾Ñ€Ð¸ â€” Ð¿Ð¾ Ð·Ð°Ð¼Ð¸ÑÑŠÐ»); `C:\git\bridge\` (ÐºÐ°Ð½Ð°Ð»ÑŠÑ‚ ÐºÑŠÐ¼ Sol); `C:\git\Varna_buildings\output\` Ð¸ `data\extracted\` (Ð¸Ð·Ð²Ð¾Ñ€Ð¸Ñ‚Ðµ, Ð²Ð¸Ð¶ DATA.md).

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'C:/git/Fire_Varna/scratch/places_search/granitsi_b2_astra_S26_07.09.md' -Encoding UTF8 -Tail 130" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'AGENTS.md' -Encoding UTF8 -TotalCount 150" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git --no-optional-locks -c core.quotepath=false status --porcelain=v1 -uno' in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git --no-optional-locks -c core.quotepath=false show --format=fuller --stat 0ba2e9d' in C:\git\varna_3d
 succeeded in 0ms:
git commit -F scratch/granitsi/COMMIT_MSG_b2_2_exports.txt -- data/fire_varna_places.json data/fire_varna_hotels.json data/place_categories.json
git commit -F scratch/granitsi/COMMIT_MSG_b2_3_ledger.txt -- scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json
```

**Механична уговорка:** `git commit -- paths` взема избраните **worktree contents**, като изключва останалите staged файлове. Затова непосредствено преди всеки комит: `git diff --exit-code -- <същите paths>` трябва да е `0`, плюс за всеки path **в Git Bash**:

```bash
git cat-file blob :path | sha256sum
```

Проверените index SHA256 са:

| Файл | SHA256 |
|---|---|
| identity | `4819ab3e1d74f516de051b5f05abf4721c6f8c42cf2c5c2a293ba95eedc7d0c2` |
| inputs | `c7450ded1b8ade5bdb3b63924971d2be0d9b9ea1a792175df0331526ed4679ee` |
| places | `3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66` |
| hotels | `eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51` |
| categories | `9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231` |
| manifest | `bb04640e9762a12a5028b99ee70b1053687cfa4ed55b6e7e2f4c2e191b114abb` |
| ledger | `5ec64c682a46463c1f4890510736a13a5766ada61fcc757af281f6c82d3a7d94` |

Hotels/categories имат CRLF в worktree, но LF-normalized bytes съвпадат с index; текущият `git diff` е `0`.

За последващата публикация: [ledger:6](C:/git/varna_3d/scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json:6) изрично е **частен**; `qa_no_cad_ids=0` не разрешава публичност на целия repo. Repo `.gitignore:79` освобождава `scratch/refactor/`; ignored-path твърдението не се потвърди, а глобалният ignore е недостъпен. Dirty `qa_place_bodies.md` остава извън трите комита: `2633e165…`, 153+/153−; възстановяване/регенериране решава Петър по [State:49](C:/git/Fire_Varna/docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:49).
tokens used
78,798
**НЕГОДНО за комит сега.** Staged данните издържат проверките, но гейтът за неподвижната точка нарушава A3, а пълният `unittest` набор не е потвърден в тази read-only сесия. HEAD остана `1217dc494ebd1ce16f1cbd90e73f202dec206b1e`; index не е променян.

**Блокерът:** [qa_fixed_point.py:95](C:/git/varna_3d/src/qa_fixed_point.py:95) нормализира JSON и без `--ignore`. Проба с различни сурови байтове, но еднакъв JSON, връща `0`; [A3:100](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:100) изисква директно byte comparison за ledger-а. Реалните ledger файлове са byte-equal; това не отстранява false-pass дефекта на гейта.

Проверени са всичките **17 комита** след `6486b48`. Шестте пълни съобщения съвпадат дословно с [§3:32](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:32). Първите 16 имат author **и committer** `Claude Executor <executor@local>`; последният — `Claude Architect <architect@local>`.

| SHA | Проверен write-set и основание |
|---|---|
| `3de6661` | `qa_identity_refresh.py`; предходен Б2-0а, State:42 |
| `5c6fdd0` | `place_identity.py`, `qa_place_identity_coords.py`; Б2-0, State:43 |
| `da77ff2` | `fire_varna_locations.py`, `qa_p8a.py`; първият Б2, изрично запазен, State:44 |
| `0ecd814` | categories builder, двата exporters и двата export QA; същият предходен Б2 |
| `a28edc2` | `place_identity.py`, `place_addresses.py`; **§3/1, дословно** |
| `8a60972` | `qa_identity_rekey.py`; **§3/2, дословно** |
| `7bac5e5` | `qa_identity_refresh.py`; **§3/3, дословно** |
| `bb09535` | `fire_varna_locations.py`; **§3/6, дословно**; ранното изпълнение съответства на A1/A7 |
| `4bdcc7c` | rekey/refresh negative harnesses и rekey QA; довършва §3/2–3 |
| `36e8513` | двата harnesses, двата identity QA, замразената fixture; §3/2, A2/A7 |
| `679451d` | `fire_varna_locations.py`; **§3/4, дословно**, A6 |
| `2624218` | `qa_fire_varna_m6.py`; **§3/5, дословно**, A6 |
| `822656d` | comparator и negatives; A3, с установения дефект |
| `bd00c2c` | categories builder, `zone_alias_overrides.json`; решение 5/П3 |
| `0c1ed71` | alias QA и negatives; П2 |
| `26da605` | P8-а QA и negatives; П4 |
| `1217dc4` | само `.gitignore`; изключението на [ред 238](C:/git/varna_3d/.gitignore:238) |

Допълнителните изпълнителски комити са обосновани от подписаните условия; отделните им съобщения не са предписани дословно. `.gitignore` остава ограничено процедурно отклонение извън write-set-а, отчетено в [State:53](C:/git/Fire_Varna/docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:53).

**Исторически твърдението „няма agent canonical-data commits“ е невярно:** `58c75ed6` и `85ef6368` съдържат `place_identity.json`, SHA256 `1141bbc2…`, от Executor. Последващите resets са записани като Petar1984 ([reflog:78](C:/git/varna_3d/.git/logs/HEAD:78), [reflog:85](C:/git/varna_3d/.git/logs/HEAD:85)). Те и `95414d3`/`85bb4fd` нямат съдържащи refs; обикновен branch push не ги включва. Текущата ancestry няма комити на седемте canonical payloads.

Реално измерените QA резултати са:

| Команда/проверка | Exit |
|---|---:|
| `python -B src/qa_p8a.py` | 0 |
| `python -B src/qa_fire_varna_places_export.py` | 0 |
| `python -B src/qa_place_zone_aliases.py` | 0 |
| `python -B src/qa_no_cad_ids.py` | 0 |
| `qa_fixed_point.py` — трите сравнения | 0/0/0 |
| `qa_identity_rekey.py` — документираните аргументи | 0 |
| `qa_fire_varna_m6.py --ledger scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` | **3**, fails **0** |
| `unittest discover -s tests`, под read-only защита | **1**, 0 tests, setup ERROR |

Rekey използва fixture `tests/fixtures/identity_rekey_base_2026-09-07.json`, двата `scratch/granitsi/place_identity.rekey{,.run2}.json` кандидата и очакван SHA `1141bbc2f6ffd8795155728798132f0aff2e79ac53dd8aa4b9285c95b0bd9761`, съгласно [докстринга:17](C:/git/varna_3d/src/qa_identity_rekey.py:17). Fixed-point сравнява `scratch/granitsi/fixpoint/{places,hotels,ledger}_run1.json` с окончателните файлове; само exports ползват `--ignore _meta.generated`.

M6 потвърди точно осемте IDs от [PENDING_EXPECTED:95](C:/git/varna_3d/src/qa_fire_varna_m6.py:95): ДАЛИЯ ГАРДЪН, МАГНОЛИЯ 1 И 2, Маяк, НЕПТУН, РУСАЛКА, Романтика, СТРАНДЖА, Фрегата.

`unittest` setup опитва `shutil.rmtree(FIXTURES)` ([test:157](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:157)); защитата го спря преди промяна. Това е ограничение на изпълнението, не доказан дефект на тестовете. Нужен е успешен прогон в разрешено изолирано копие.

Независимата проверка на данните потвърди:

- **G17: 201/201** quarter JSON tokens byte-equal срещу `8d60aebb:…/lot1v_locations_375.json`, SHA `d5050f1c…`.
- **П4: 57 = 42 places + 15 hotels**, всички сред 174 празни квартала; нула върху написаните.
- **375/375 place_id** срещу fixture; само `key×375`, `zone×57`, `_meta.rule_key`; координатите, `sites` и осемте retired са запазени.
- Manifest: само **9 zone стойности = 3 grandfathered + 6 board_queue**, по решение 6.
- [Inputs:51](C:/git/varna_3d/data/fire_varna_location_inputs.json:51) и [:55](C:/git/varna_3d/data/fire_varna_location_inputs.json:55) пинват staged identity/manifest. [:96](C:/git/varna_3d/data/fire_varna_location_inputs.json:96) сочи новия ledger; [:99](C:/git/varna_3d/data/fire_varna_location_inputs.json:99) съдържа SHA на **базовия** ledger. Собственият нов SHA не е поле в този договор.
- Двата реални ledger файла са директно byte-equal: **965388 B**, `5ec64c68…`.

След поправката и зелените гейтове трите комита на Петър трябва да използват следните message-file текстове, в реда на [§6/A7](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:104):

```text
data: place coordinates from KAIS bodies (Б0 т. 11) and identity re-keyed without the zone (375 place_id unchanged), inputs pinned

57 identity zones refreshed; registry manifest accepted and pinned (decision 6: 9 zone rows, 3 grandfathered + 6 board_queue).
```

```text
data: places and hotels with quarter by signed polygon, search dictionary regenerated
```

```text
data: p8a quarter assignment ledger 07.09
```

Готовите `COMMIT_MSG_b2_2_exports.txt` и `COMMIT_MSG_b2_3_ledger.txt` съдържат парафрази; трябва да получат горните дословни текстове. Командите са:

```bash
git commit -F scratch/granitsi/COMMIT_MSG_b2_1_identity.txt -- data/place_identity.json data/fire_varna_location_inputs.json data/registry_manifest.json
git commit -F scratch/granitsi/COMMIT_MSG_b2_2_exports.txt -- data/fire_varna_places.json data/fire_varna_hotels.json data/place_categories.json
git commit -F scratch/granitsi/COMMIT_MSG_b2_3_ledger.txt -- scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json
```

**Механична уговорка:** `git commit -- paths` взема избраните **worktree contents**, като изключва останалите staged файлове. Затова непосредствено преди всеки комит: `git diff --exit-code -- <същите paths>` трябва да е `0`, плюс за всеки path **в Git Bash**:

```bash
git cat-file blob :path | sha256sum
```

Проверените index SHA256 са:

| Файл | SHA256 |
|---|---|
| identity | `4819ab3e1d74f516de051b5f05abf4721c6f8c42cf2c5c2a293ba95eedc7d0c2` |
| inputs | `c7450ded1b8ade5bdb3b63924971d2be0d9b9ea1a792175df0331526ed4679ee` |
| places | `3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66` |
| hotels | `eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51` |
| categories | `9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231` |
| manifest | `bb04640e9762a12a5028b99ee70b1053687cfa4ed55b6e7e2f4c2e191b114abb` |
| ledger | `5ec64c682a46463c1f4890510736a13a5766ada61fcc757af281f6c82d3a7d94` |

Hotels/categories имат CRLF в worktree, но LF-normalized bytes съвпадат с index; текущият `git diff` е `0`.

За последващата публикация: [ledger:6](C:/git/varna_3d/scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json:6) изрично е **частен**; `qa_no_cad_ids=0` не разрешава публичност на целия repo. Repo `.gitignore:79` освобождава `scratch/refactor/`; ignored-path твърдението не се потвърди, а глобалният ignore е недостъпен. Dirty `qa_place_bodies.md` остава извън трите комита: `2633e165…`, 153+/153−; възстановяване/регенериране решава Петър по [State:49](C:/git/Fire_Varna/docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:49).

 succeeded in 0ms:
# AGENTS.md — governance for Varna 3D

Same pipeline as `Varna_buildings`. This file is the short version; the
machine-wide invariants live in `~/.claude/CLAUDE.md` and take precedence over
anything here.

## What this repo is

Varna 3D sits ABOVE `Varna_buildings` and `Fire_Varna`: they decide *where the
address is*, this one decides *what the city looks like*. Nothing that already
exists is touched — Varna 3D is a consumer of their outputs, not their heir.
(Translated from `README.md`, lines 5–7, which are in Bulgarian.)

## The trunk

- Working branch: `rezhimi`. Every commit of the running cycles lands there.
- GitHub's default branch is `main`
  (`git symbolic-ref refs/remotes/origin/HEAD`). It is a strict ancestor of
  `rezhimi` (`git merge-base --is-ancestor main rezhimi`, plus a non-zero
  `git rev-list --count main..rezhimi`); the profile-ordering plan of
  01.09.2026 (`C:\git\plan.md` today; LOT 4 brings it into `docs/plans/`)
  brings `main` level with `origin/rezhimi` in its LOT 3.
- Which of the two is the trunk from here on is Petar's open question В-1 of
  that plan. Until he answers: work on `rezhimi`, push nothing (hard rule 1).

## Entry point

`docs/activeContext.md` — the state of the repo, one truth per document. LOT 5
of the 01.09 plan writes it and freezes the chronicle. Until then the state is
`СЪСТОЯНИЕ.md` in the repo root, which LOT 4 moves to `docs/СЪСТОЯНИЕ.md`.
Read whichever of the two exists before anything else here.

## Live numbers

**No state number enters this file** — no record counts, no file counts, no
commit counts, no byte sizes, no "last updated" dates. Every one of them lives
in the entry point above. Until LOT 5 the entry point is a dated chronicle, not
a number-to-command table: a number read from it is re-measured with the
command beside it (hard rule 5). Numbers that are **rules** — an EPSG code, a
read cap, a byte ceiling — stay here, because a rule is not state.

## Roles

| Role | Who | Does | Never |
|---|---|---|---|
| **Planner** | Claude Code (read-only) | measures, architects, drafts `ПЛАН_<тема>.md` (there is no `plan.md` here — one plan file per theme; `git ls-files \| grep "ПЛАН_"`) | edits, commits |
| **Researcher** | Sol (`codex exec`, via `C:\git\bridge`) | external evidence with citations | decides |
| **Executor** | Claude Code | implements a signed plan, local commits | plans, expands scope, pushes |
| **Auditor** | Claude Code (read-only, adversarial) | refutes the Executor's claims | edits |
| **Orchestrator** | **Petar** | signs plans (Gate 1), reviews diffs (Gate 2), pushes | — |

## Hard rules

1. **Never `git push`.** Petar pushes. No exceptions, no "just this once".
2. **No cadastral identifiers leave `C:\git\m6000_private`.** A 3D scene carries
   geometry + floor counts, never `cadnum`. Any scene that could be shared is
   anonymous by construction: the `cadnum` column is never read into the mesh,
   and the `no_cadastral_identifier` entry in the gates of `src/build_lod1.py`
   records that as a declared invariant (`"pass": True`), not as a check —
   the check over everything git tracks is `python src/qa_no_cad_ids.py`.
   Tracked evidence files were not anonymous: the audit of 21.08
   found the rule broken there, and `src/scrub_cad_ids.py` cleaned them
   afterwards. The code exceptions it deliberately leaves are named in its own
   docstring.
3. **BGS2005 vs WGS84 must be explicit** in every coordinate that touches disk.
   KAIS is BGS2005 (≈EPSG:7801); web output is WGS84; metric work is EPSG:32635.
   Mixing them silently is the single largest correctness risk inherited from
   `Varna_buildings`.
4. **Phase 0 (licensing) gates everything.** No mesh is built for public use
   before the licence question is answered in writing with citations.
5. **Measure before you claim.** Every number in a document carries the date it
   was measured and the command that produced it.
6. **Never modify `Varna_buildings` or `Fire_Varna` from here.** This project
   reads their outputs. Changes there go through their own pipelines.
7. **Fail loud.** A reprojection that lands outside the Varna bounding box stops
   the build; it does not write output and hope.

## Gates

- **Gate 1 — signed plan.** Petar signs before any build step runs.
- **Gate 2 — diff review.** Petar reads the diff before it is committed upstream.
- **Acceptance is machine-checkable.** "Looks right" is not a gate. The gates
  `src/build_lod1.py` evaluates before a single byte is written are
  `building_count`, `reprojection_in_varna_bbox`, `no_cadastral_identifier`,
  `built_volume_Mm3`, `tallest_building_m` and `no_osm_artifacts`, plus the
  terrain gate of the run — `seated_on_terrain` and
  `terrain_covers_every_building` under `--seat`, otherwise `mesh_sits_on_zero`
  (list them from the source, not from memory:
  `awk '/^    gates = \{/{f=1} /^    metrics/{f=0} f' src/build_lod1.py | grep -oE '^        "[A-Za-z0-9_]+"|gates\["[A-Za-z0-9_]+"\]' | grep -oE '"[A-Za-z0-9_]+"' | sort -u`).
  One failing gate stops the build and writes no product — only
  `varna_lod1_metrics.json` with the verdicts (`grep -n -A2 'STOPPED' src/build_lod1.py`).
  Vertex count is **not** a gate — it is only reported (in `metrics` and in the console log)
  (`git grep -n -iE 'vertex|vertices' -- src/build_lod1.py`) — and a
  reprojection-residual check does not exist at all
  (`git grep -n -i -E 'reproject.{0,25}residual|residual.{0,25}reproject' -- src`
  returns nothing).

## The repo's gates

These scripts guard the repo itself, not the model of the city. Names and what
they protect only — the counts they print are state and live in the entry point.

- `src/qa_no_cad_ids.py` — the gate behind hard rule 2: ZERO cadastral
  identifiers in every file git tracks, not only in the published output. The
  exceptions are enumerated with their reason in its `ALLOW` block.
- `src/qa_no_extrude.py` — judges `data/no_extrude_verdicts.json`, the one
  place that tells the web page which cadastral bodies NOT to draw; the three
  classes of verdict are judged separately, by the strength of their grounds.
- `src/scrub_cad_ids.py` — a cleaner, not a gate: it replaces a cadastral
  identifier in tracked evidence files with a per-file serial while keeping the
  audit trail. Without `--apply` it only reports. It never touches code.
- The build's own gates are in `src/build_lod1.py` and are evaluated before a
  single byte is written (see § Gates).
- The rest of the family: `ls src/qa_*.py`.

## Scratch and artefacts

- Generated meshes, DEM tiles, and textures are **never** committed. See
  `.gitignore`. Two families were force-added past those rules and are tracked
  today: `.png` probe screenshots under `scratch/web_probes/`, and the tracked
  reports, the dry-run JSON files and the dry-run GeoJSON under `output/` (`git ls-files | grep -icE "\.png$"`;
  `git ls-files output`). `git add -f` is a signed decision, not a routine
  command; how many there are is state and lives in the entry point.
- Session-temp scripts start with `_` and are meant to be deleted by the
  session that made them once their findings are written down. The tree does
  not match that rule: `_`-files accumulate, and a large batch of them entered
  git as evidence with the LOT 1 commit of the 01.09 plan
  (`git log --format='%h %s' --grep='ЛОТ 1 (загуба)'`). Today's
  count: `git ls-files | awk -F/ '{print $NF}' | grep -c "^_"`.

## Where the documents live

The project's documents live under `docs/` (LOT 4 of the 01.09 plan moved them
there from the repo root with `git mv`, so history follows — `git log --follow <file>`);
working material under `scratch/` and generated reports under `output/` stay where
they are. The root keeps `README.md`, `AGENTS.md`, `CLAUDE.md`, `DATA.md` and
`ПЛАН_П2в_терена.md` (`git ls-files | grep -E '^[^/]+\.md$'`); `docs/Наредба_7_2003_МРРБ.pdf`
sits beside the sub-folders (`ls docs/`):

| Pattern | Lives in |
|---|---|
| `ПЛАН_*.md` | `docs/plans/` |
| `ДОКЛАД_*.md` | `docs/audits/` |
| `ПРОМПТ_*.md` | `docs/sessions/` |
| research write-ups | `docs/research/` |
| decision documents | `docs/decisions/` (index: `docs/decisions/README.md`) |
| `МЯРКА_*.md` | `docs/measurement/` |
| `СЪСТОЯНИЕ.md` | `docs/` |

Under Р-9 (а) of the 01.09 plan (signed 02.09), `ПЛАН_П2в_терена.md` stays in the root: it is pipeline input, read by

 succeeded in 0ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
M  data/fire_varna_hotels.json
M  data/fire_varna_location_inputs.json
M  data/fire_varna_places.json
M  data/place_categories.json
M  data/place_identity.json
M  data/registry_manifest.json
 M scratch/place_bodies/qa_place_bodies.md
A  scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json

 succeeded in 0ms:
commit 0ba2e9d20fdf9ec8a3e03ecb31890cd24150e088
Author:     Claude Executor <executor@local>
AuthorDate: Mon Sep 7 06:42:44 2026 +0300
Commit:     Claude Executor <executor@local>
CommitDate: Mon Sep 7 06:42:44 2026 +0300

    gates: qa_fixed_point compares raw bytes when no key is forgiven (amendment 3 A3, S26)

 scratch/granitsi/fixed_point_negatives.py | 31 ++++++++++++++++-
 src/qa_fixed_point.py                     | 56 ++++++++++++++++++++++---------
 2 files changed, 70 insertions(+), 17 deletions(-)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'src/qa_fixed_point.py' -Encoding UTF8 -TotalCount 150" in C:\git\varna_3d
 succeeded in 0ms:
"""Неподвижната точка (амандамент №3 §4 т. 6 · A3): два прогона, едни байтове.

Присвояването на квартал пише в `data/place_identity.json` (зоната), а
самоличността е ВХОД на същото присвояване.  Такъв кръг е здрав само ако е
НЕПОДВИЖНА ТОЧКА: вторият прогон върху освежената самоличност трябва да върне
СЪЩИЯ резултат.  Ако не го връща, конвейерът има памет — а памет, която никой
не е обявил, е дефект.

Сравнението прави ГЕЙТЪТ, не окото, и има ДВА режима, дословно по A3:

    БЕЗ `--ignore` → СУРОВИТЕ БАЙТОВЕ, директно: `Path.read_bytes()` срещу
    `Path.read_bytes()`, без JSON parse, без преподреждане и без изравняване
    на краищата на редовете.  Нищо не се прощава, защото нищо не е назовано.

    С `--ignore a.b.c` → нормализацията на A3: JSON parse → изтриване САМО на
    изрично назованите ключове (`--ignore _meta.generated`) →
    `json.dumps(doc, ensure_ascii=False, indent=1) + "\\n"` → UTF-8 →
    сравнение на БАЙТОВЕ.

Масивите пазят реда си: пренареден масив НЕ е същият документ.  Леджерът се
сравнява ДИРЕКТНО, без нито едно изключение — `_meta`-то му няма часовник, и
точно затова няма какво да му се прощава; при него „същият JSON, но други сурови
байтове“ (друг `indent`, CRLF) е ЧЕРВЕНО.  Двата износа носят стенен часовник в
`_meta.generated` (записан дълг 07.09) и това е ЕДИНСТВЕНИЯТ назован ключ, който
се маха; нормализацията е за тях и само за тях.  Всяка друга разлика е червено.

    python src/qa_fixed_point.py --a <път> --b <път>
    python src/qa_fixed_point.py --a <път> --b <път> --ignore _meta.generated

Изход 0 = байт-еднакви (сурово, а при назован ключ — след нормализацията) ·
1 = различни (с първата разлика поименно) · 2 = липсващ вход.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def drop(doc, dotted: str) -> bool:
    """Изтрива ЕДИН назован ключ по път `a.b.c`; връща дали го е намерил.

    Никакви шаблони и никакво „по подразбиране“: гейт, който сам решава кое да
    прости, не е гейт.  Пътят се изрича на командния ред.
    """
    parts = dotted.split(".")
    node = doc
    for p in parts[:-1]:
        if not isinstance(node, dict) or p not in node:
            return False
        node = node[p]
    if isinstance(node, dict) and parts[-1] in node:
        del node[parts[-1]]
        return True
    return False


def normalise(path: Path, ignore: list[str]) -> tuple[bytes, list[str]]:
    doc = json.loads(path.read_text(encoding="utf-8"))
    dropped = [key for key in ignore if drop(doc, key)]
    text = json.dumps(doc, ensure_ascii=False, indent=1) + "\n"
    return text.encode("utf-8"), dropped


def first_difference(a: bytes, b: bytes) -> str:
    """Първата различна позиция, показана като редове — не като байтова каша.

    Суровият режим подава каквото пише на диска: може да не е валиден UTF-8 и
    може да се различава само по краищата на редовете.  Затова декодирането е с
    `errors="replace"` (гейтът не бива да пада с изключение вместо с присъда), а
    последната дума — когато редовете съвпадат — е за самите байтове.
    """
    la = a.decode("utf-8", errors="replace").splitlines()
    lb = b.decode("utf-8", errors="replace").splitlines()
    for n, (x, y) in enumerate(zip(la, lb), start=1):
        if x != y:
            return f"ред {n}:\n    A: {x.strip()[:200]}\n    B: {y.strip()[:200]}"
    if len(la) != len(lb):
        return f"еднакви до ред {min(len(la), len(lb))}, но A има {len(la)} " \
               f"реда, а B — {len(lb)}"
    at = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y),
              min(len(a), len(b)))
    return (f"еднакви редове, но различни сурови байтове: първата разлика при "
            f"байт {at} (A: {len(a)} B: {len(b)} байта) — краища на редове или "
            f"невидими знаци")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(
        description="неподвижната точка: два документа, едни байтове (A3)")
    ap.add_argument("--a", required=True, help="първият прогон")
    ap.add_argument("--b", required=True, help="вторият прогон")
    ap.add_argument("--ignore", action="append", default=[],
                    metavar="a.b.c",
                    help="ЕДИН назован ключ, който се маха преди сравнението "
                         "(например _meta.generated); може да се повтори")
    ap.add_argument("--label", default="", help="име за печата")
    a = ap.parse_args(argv)

    pa, pb = Path(a.a), Path(a.b)
    for p in (pa, pb):
        if not p.exists():
            print(f"ГРЕШКА: липсва {p}", file=sys.stderr)
            return 2

    label = a.label or f"{pa.name} ↔ {pb.name}"
    if a.ignore:
        # Назован ключ → нормализацията на A3, и то само заради него.
        ba, dropped_a = normalise(pa, a.ignore)
        bb, dropped_b = normalise(pb, a.ignore)
        said = " · махнати ключове: " + ", ".join(
            sorted(set(dropped_a + dropped_b)))
    else:
        # Нищо назовано → нищо простено: суровите байтове, както са на диска.
        # Нормализация тук би обявила „същият JSON“ за „същите байтове“ и би
        # пропуснала друг `indent` или CRLF — точно дупката, която A3 забранява.
        ba, bb = pa.read_bytes(), pb.read_bytes()
        said = " · сурови байтове, без изключения (директно сравнение)"
    if ba == bb:
        print(f"  ok    неподвижна точка · {label} · {len(ba)} байта{said}")
        return 0
    print(f"ПАДА   неподвижна точка · {label}{said}")
    print("       " + first_difference(ba, bb))
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'scratch/granitsi/fixed_point_negatives.py' -Encoding UTF8 -TotalCount 150" in C:\git\varna_3d
 succeeded in 0ms:
"""Отрицателните фикстури на `src/qa_fixed_point.py` (амандамент №3 A3).

Компараторът на неподвижната точка твърди „същите байтове“.  Твърдение без
падаща фикстура е обещание, затова тук се доказва и обратното:

  1. подменен РЕД при ЕДНАКЪВ часовник → червено (главната фикстура на §5);
  2. пренареден масив при иначе еднакво съдържание → червено (редът е част от
     документа, не украса);
  3. изтрит ключ → червено;
  4. същият документ при РАЗЛИЧЕН `_meta.generated` → ЗЕЛЕНО, но само когато
     ключът е назован на командния ред; без `--ignore` същата двойка е червена;
  5. СЪЩИЯТ JSON, но различни сурови байтове (друг `indent`; CRLF краища) →
     червено без `--ignore`, защото там се сравняват байтовете, а не документът
     (измереното от Astra S26 фалшиво „ok“); контролът отсреща: същата смяна на
     `indent` ПРИ назован ключ е зелена — нормализацията по A3 е за износите.

    python scratch/granitsi/fixed_point_negatives.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent.parent
GATE = ROOT / "src" / "qa_fixed_point.py"
PLACES = ROOT / "data" / "fire_varna_places.json"
LEDGER = (ROOT / "scratch" / "refactor" / "_addr"
          / "lot1v_locations_375_p8a_07.09.json")
OUT = Path(__file__).resolve().parent / "_fixed_point_neg"

fails: list[str] = []


def run(args: list[str]) -> int:
    got = subprocess.run([sys.executable, str(GATE), *args], cwd=str(ROOT),
                         capture_output=True, text=True, encoding="utf-8",
                         errors="replace")
    return got.returncode


def expect(label: str, want_red: bool, args: list[str]) -> None:
    code = run(args)
    ok = (code != 0) if want_red else (code == 0)
    print(("  ✓ " if ok else "  ✗ ")
          + f"{label} → изход {code} ({'червено' if want_red else 'зелено'} "
            f"се искаше)")
    if not ok:
        fails.append(label)


def write(name: str, doc) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n",
                    encoding="utf-8")
    return path


def write_text(name: str, text: str, newline: str = "\n") -> Path:
    """Пише ТОЧНО подадените байтове — краищата на редовете са част от пробата."""
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    path.write_bytes(text.replace("\n", newline).encode("utf-8"))
    return path


def main() -> int:
    places = json.loads(PLACES.read_text(encoding="utf-8"))
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    same = write("places_copy.json", places)

    print("=== контрол ===")
    expect("копие срещу оригинал", False,
           ["--a", str(PLACES), "--b", str(same), "--ignore", "_meta.generated"])

    print("\n=== 1 · подменен ред при ЕДНАКЪВ часовник ===")
    doc = json.loads(json.dumps(places, ensure_ascii=False))
    doc["places"][0]["zone"] = "кв. Измислено"
    expect("подменена зона на един ред", True,
           ["--a", str(PLACES), "--b", str(write("neg_row.json", doc)),
            "--ignore", "_meta.generated"])

    doc = json.loads(json.dumps(ledger, ensure_ascii=False))
    doc["rows"][0]["new_zone"] = "кв. Измислено"
    expect("подменен ред в леджера (без изключения)", True,
           ["--a", str(LEDGER), "--b", str(write("neg_ledger.json", doc))])

    print("\n=== 2 · пренареден масив ===")
    doc = json.loads(json.dumps(places, ensure_ascii=False))
    doc["places"] = list(reversed(doc["places"]))
    expect("обърнат ред на местата", True,
           ["--a", str(PLACES), "--b", str(write("neg_order.json", doc)),
            "--ignore", "_meta.generated"])

    print("\n=== 3 · изтрит ключ ===")
    doc = json.loads(json.dumps(places, ensure_ascii=False))
    doc["places"][0].pop("zone", None)
    expect("липсващ ключ в един ред", True,
           ["--a", str(PLACES), "--b", str(write("neg_missing.json", doc)),
            "--ignore", "_meta.generated"])

    print("\n=== 4 · различен часовник ===")
    doc = json.loads(json.dumps(places, ensure_ascii=False))
    doc["_meta"]["generated"] = "1970-01-01T00:00:00"
    clock = write("neg_clock.json", doc)
    expect("само часовникът, с --ignore", False,
           ["--a", str(PLACES), "--b", str(clock),
            "--ignore", "_meta.generated"])
    expect("същата двойка БЕЗ --ignore", True,
           ["--a", str(PLACES), "--b", str(clock)])

    print("\n=== 5 · същият JSON, различни сурови байтове ===")
    wide = json.dumps(ledger, ensure_ascii=False, indent=2) + "\n"
    expect("леджерът наново с indent=2 (същият документ), БЕЗ --ignore", True,
           ["--a", str(LEDGER),
            "--b", str(write_text("neg_indent2.json", wide))])

    lf_text = LEDGER.read_text(encoding="utf-8")
    expect("леджерът със CRLF краища (същият документ), БЕЗ --ignore", True,
           ["--a", str(LEDGER),
            "--b", str(write_text("neg_crlf.json", lf_text, newline="\r\n"))])

    wide_places = json.dumps(places, ensure_ascii=False, indent=2) + "\n"
    expect("местата наново с indent=2, С --ignore _meta.generated", False,
           ["--a", str(PLACES),
            "--b", str(write_text("ctl_indent2.json", wide_places)),
            "--ignore", "_meta.generated"])

    print()
    if fails:
        print(f"ПАДА: {len(fails)}")
        for f in fails:
            print(f"    {f}")
        return 1
    print("минава — компараторът вижда разликата и прощава само назованото")
    return 0


if __name__ == "__main__":
    sys.exit(main())

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'AGENTS.md' -Encoding UTF8 | Select-Object -Skip 150 -First 100" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'rg --files --hidden --max-count 20 --max-columns 200 -g AGENTS.md -g CLAUDE.md src scratch tests' in C:\git\varna_3d
 exited 1 in 0ms:
 succeeded in 0ms:
`src/qa_no_extrude.py` and by the generation tools `src/gen_rekey.py`, `src/gen_promote.py`, `src/gen_archive.py`
(`git grep -n 'ПЛАН_П2в_терена.md' -- src`).

**A decision is a file, never an ad-hoc change.** An architecture or scope
decision becomes its own document under `docs/decisions/`, on the model of
`C:\git\Varna_buildings\CLAUDE.md` § "ADR & scratch hygiene": an accepted
decision is never rewritten (status stamps only), the status vocabulary is
closed, and the index row is updated in the same commit as the decision.

**Commit messages.** The subject line is ≤ 72 characters. The recorded exception is the
commits of the 01.09 plan, whose subjects start with `ЛОТ ` or `docs: 71` (`git log --format=%s | grep -cE '^(ЛОТ |docs: 71)'`) —
their texts were fixed in the plan before each commit. Older subjects average far above
72 characters (`git log -50 --format=%s | python -c "import sys;L=[len(x) for x in sys.stdin.read().splitlines()];print(sum(L)/len(L))"` — characters, not bytes). The narrative belongs
in the body of the commit or in the document, not in the subject.

## Output budget (token discipline)

Context cost here is dominated by tool output, not by files or prompts.
Hard rules:

1. **Search capped.** `rg` always with `--max-count 20 --max-columns 200`.
   Start with `rg -l` (file list only), then read matches selectively.
2. **Read ranges, never whole files.** Use `sed -n 'A,Bp'`, `head -n 100`,
   or `Get-Content -TotalCount 100`. Max 150 lines per read; for a large
   file, read only the range you need.
3. **Data and logs are size-gated.** `head`/`tail` samples of data files
   are fine; never output a whole file over 1 MB (`*.log`, `*.jsonl`,
   `*.db`, `*.csv`, binaries), and never read `.git/`, the generated meshes
   and tiles under `output/`, or the probe screenshots under
   `scratch/web_probes/` — the tracked reports under `output/` are documents,
   not build output, and are readable. There is no `node_modules/` in this
   repo: the vendored web libraries are in `web/vendor/`. A log check is
   `tail -n 50`, once.
4. **One question per command.** If a capped result is insufficient,
   refine ONCE with a narrower query — never re-run with broader flags
   or raised caps. Still insufficient → state what is missing in your
   answer instead of searching further.
5. **Prefer what is already in context** over re-reading the same file.
6. **Escape hatch:** if the task explicitly names a file or module for
   exhaustive review, sequential ranged reads of the whole target are
   allowed.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git --no-optional-locks show --format= --unified=3 0ba2e9d -- src/qa_fixed_point.py scratch/granitsi/fixed_point_negatives.py' in C:\git\varna_3d
 succeeded in 0ms:
diff --git a/scratch/granitsi/fixed_point_negatives.py b/scratch/granitsi/fixed_point_negatives.py
index a63b2b2..f36dac3 100644
--- a/scratch/granitsi/fixed_point_negatives.py
+++ b/scratch/granitsi/fixed_point_negatives.py
@@ -8,7 +8,11 @@
      документа, не украса);
   3. изтрит ключ → червено;
   4. същият документ при РАЗЛИЧЕН `_meta.generated` → ЗЕЛЕНО, но само когато
-     ключът е назован на командния ред; без `--ignore` същата двойка е червена.
+     ключът е назован на командния ред; без `--ignore` същата двойка е червена;
+  5. СЪЩИЯТ JSON, но различни сурови байтове (друг `indent`; CRLF краища) →
+     червено без `--ignore`, защото там се сравняват байтовете, а не документът
+     (измереното от Astra S26 фалшиво „ok“); контролът отсреща: същата смяна на
+     `indent` ПРИ назован ключ е зелена — нормализацията по A3 е за износите.
 
     python scratch/granitsi/fixed_point_negatives.py
 """
@@ -57,6 +61,14 @@ def write(name: str, doc) -> Path:
     return path
 
 
+def write_text(name: str, text: str, newline: str = "\n") -> Path:
+    """Пише ТОЧНО подадените байтове — краищата на редовете са част от пробата."""
+    OUT.mkdir(parents=True, exist_ok=True)
+    path = OUT / name
+    path.write_bytes(text.replace("\n", newline).encode("utf-8"))
+    return path
+
+
 def main() -> int:
     places = json.loads(PLACES.read_text(encoding="utf-8"))
     ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
@@ -102,6 +114,23 @@ def main() -> int:
     expect("същата двойка БЕЗ --ignore", True,
            ["--a", str(PLACES), "--b", str(clock)])
 
+    print("\n=== 5 · същият JSON, различни сурови байтове ===")
+    wide = json.dumps(ledger, ensure_ascii=False, indent=2) + "\n"
+    expect("леджерът наново с indent=2 (същият документ), БЕЗ --ignore", True,
+           ["--a", str(LEDGER),
+            "--b", str(write_text("neg_indent2.json", wide))])
+
+    lf_text = LEDGER.read_text(encoding="utf-8")
+    expect("леджерът със CRLF краища (същият документ), БЕЗ --ignore", True,
+           ["--a", str(LEDGER),
+            "--b", str(write_text("neg_crlf.json", lf_text, newline="\r\n"))])
+
+    wide_places = json.dumps(places, ensure_ascii=False, indent=2) + "\n"
+    expect("местата наново с indent=2, С --ignore _meta.generated", False,
+           ["--a", str(PLACES),
+            "--b", str(write_text("ctl_indent2.json", wide_places)),
+            "--ignore", "_meta.generated"])
+
     print()
     if fails:
         print(f"ПАДА: {len(fails)}")
diff --git a/src/qa_fixed_point.py b/src/qa_fixed_point.py
index 55ecc2e..11c7b1f 100644
--- a/src/qa_fixed_point.py
+++ b/src/qa_fixed_point.py
@@ -6,23 +6,29 @@
 СЪЩИЯ резултат.  Ако не го връща, конвейерът има памет — а памет, която никой
 не е обявил, е дефект.
 
-Сравнението прави ГЕЙТЪТ, не окото, и правилото е дословно това на A3:
+Сравнението прави ГЕЙТЪТ, не окото, и има ДВА режима, дословно по A3:
 
-    JSON parse → изтриване САМО на изрично назованите ключове
-    (`--ignore _meta.generated`) → `json.dumps(doc, ensure_ascii=False,
-    indent=1) + "\\n"` → UTF-8 → сравнение на БАЙТОВЕ.
+    БЕЗ `--ignore` → СУРОВИТЕ БАЙТОВЕ, директно: `Path.read_bytes()` срещу
+    `Path.read_bytes()`, без JSON parse, без преподреждане и без изравняване
+    на краищата на редовете.  Нищо не се прощава, защото нищо не е назовано.
+
+    С `--ignore a.b.c` → нормализацията на A3: JSON parse → изтриване САМО на
+    изрично назованите ключове (`--ignore _meta.generated`) →
+    `json.dumps(doc, ensure_ascii=False, indent=1) + "\\n"` → UTF-8 →
+    сравнение на БАЙТОВЕ.
 
 Масивите пазят реда си: пренареден масив НЕ е същият документ.  Леджерът се
 сравнява ДИРЕКТНО, без нито едно изключение — `_meta`-то му няма часовник, и
-точно затова няма какво да му се прощава.  Двата износа носят стенен часовник в
+точно затова няма какво да му се прощава; при него „същият JSON, но други сурови
+байтове“ (друг `indent`, CRLF) е ЧЕРВЕНО.  Двата износа носят стенен часовник в
 `_meta.generated` (записан дълг 07.09) и това е ЕДИНСТВЕНИЯТ назован ключ, който
-се маха; всяка друга разлика е червено.
+се маха; нормализацията е за тях и само за тях.  Всяка друга разлика е червено.
 
     python src/qa_fixed_point.py --a <път> --b <път>
     python src/qa_fixed_point.py --a <път> --b <път> --ignore _meta.generated
 
-Изход 0 = байт-еднакви след нормализацията · 1 = различни (с първата разлика
-поименно) · 2 = липсващ вход.
+Изход 0 = байт-еднакви (сурово, а при назован ключ — след нормализацията) ·
+1 = различни (с първата разлика поименно) · 2 = липсващ вход.
 """
 from __future__ import annotations
 
@@ -61,16 +67,26 @@ def normalise(path: Path, ignore: list[str]) -> tuple[bytes, list[str]]:
 
 
 def first_difference(a: bytes, b: bytes) -> str:
-    """Първата различна позиция, показана като редове — не като байтова каша."""
-    la = a.decode("utf-8").splitlines()
-    lb = b.decode("utf-8").splitlines()
+    """Първата различна позиция, показана като редове — не като байтова каша.
+
+    Суровият режим подава каквото пише на диска: може да не е валиден UTF-8 и
+    може да се различава само по краищата на редовете.  Затова декодирането е с
+    `errors="replace"` (гейтът не бива да пада с изключение вместо с присъда), а
+    последната дума — когато редовете съвпадат — е за самите байтове.
+    """
+    la = a.decode("utf-8", errors="replace").splitlines()
+    lb = b.decode("utf-8", errors="replace").splitlines()
     for n, (x, y) in enumerate(zip(la, lb), start=1):
         if x != y:
             return f"ред {n}:\n    A: {x.strip()[:200]}\n    B: {y.strip()[:200]}"
     if len(la) != len(lb):
         return f"еднакви до ред {min(len(la), len(lb))}, но A има {len(la)} " \
                f"реда, а B — {len(lb)}"
-    return "различни байтове при еднакви редове (край на файла)"
+    at = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y),
+              min(len(a), len(b)))
+    return (f"еднакви редове, но различни сурови байтове: първата разлика при "
+            f"байт {at} (A: {len(a)} B: {len(b)} байта) — краища на редове или "
+            f"невидими знаци")
 
 
 def main(argv: list[str]) -> int:
@@ -92,10 +108,18 @@ def main(argv: list[str]) -> int:
             return 2
 
     label = a.label or f"{pa.name} ↔ {pb.name}"
-    ba, dropped_a = normalise(pa, a.ignore)
-    bb, dropped_b = normalise(pb, a.ignore)
-    said = (" · махнати ключове: " + ", ".join(sorted(set(dropped_a + dropped_b)))
-            if a.ignore else " · без изключения (директно сравнение)")
+    if a.ignore:
+        # Назован ключ → нормализацията на A3, и то само заради него.
+        ba, dropped_a = normalise(pa, a.ignore)
+        bb, dropped_b = normalise(pb, a.ignore)
+        said = " · махнати ключове: " + ", ".join(
+            sorted(set(dropped_a + dropped_b)))
+    else:
+        # Нищо назовано → нищо простено: суровите байтове, както са на диска.
+        # Нормализация тук би обявила „същият JSON“ за „същите байтове“ и би
+        # пропуснала друг `indent` или CRLF — точно дупката, която A3 забранява.
+        ba, bb = pa.read_bytes(), pb.read_bytes()
+        said = " · сурови байтове, без изключения (директно сравнение)"
     if ba == bb:
         print(f"  ok    неподвижна точка · {label} · {len(ba)} байта{said}")
         return 0

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import hashlib, json, subprocess
from pathlib import Path
def git(*args):
    return subprocess.check_output([\"git\",\"--no-optional-locks\",*args])
paths=git(\"diff\",\"--cached\",\"--name-only\",\"-z\").decode().rstrip(\"\\0\").split(\"\\0\")
snapshot={
  \"head\":git(\"rev-parse\",\"HEAD\").decode().strip(),
  \"index_entries_sha256\":hashlib.sha256(git(\"ls-files\",\"--stage\",\"-z\")).hexdigest(),
  \"tracked_worktree\":{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in git(\"ls-files\",\"-z\").decode().split(\"\\0\") if p and Path(p).is_file()},
  \"staged\":{}
}
expected={
\"data/place_identity.json\":\"4819ab3e1d74f516de051b5f05abf4721c6f8c42cf2c5c2a293ba95eedc7d0c2\",
\"data/fire_varna_location_inputs.json\":\"c7450ded1b8ade5bdb3b63924971d2be0d9b9ea1a792175df0331526ed4679ee\",
\"data/fire_varna_places.json\":\"3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66\",
\"data/fire_varna_hotels.json\":\"eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51\",
\"data/place_categories.json\":\"9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231\",
\"data/registry_manifest.json\":\"bb04640e9762a12a5028b99ee70b1053687cfa4ed55b6e7e2f4c2e191b114abb\",
\"scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json\":\"5ec64c682a46463c1f4890510736a13a5766ada61fcc757af281f6c82d3a7d94\"}
for p in paths:
    raw=git(\"cat-file\",\"blob\",\":\"+p)
    sha=hashlib.sha256(raw).hexdigest()
    snapshot[\"staged\"][p]={\"sha256\":sha,\"bytes\":len(raw),\"matches_expected\":expected.get(p)==sha}
snapshot[\"staged_paths_exact\"]=set(paths)==set(expected)
changed=git(\"diff-tree\",\"--no-commit-id\",\"--name-only\",\"-r\",\"0ba2e9d\").decode().splitlines()
snapshot[\"commit_changed_paths\"]=changed
snapshot[\"payload_commit_overlap\"]=sorted(set(changed)&set(expected))
snapshot[\"tracked_worktree_sha256\"]=hashlib.sha256(json.dumps(snapshot.pop(\"tracked_worktree\"),sort_keys=True).encode()).hexdigest()
print(json.dumps(snapshot,ensure_ascii=True,indent=2))
'@ | python -B -" in C:\git\varna_3d
 succeeded in 320ms:
{
  "head": "0ba2e9d20fdf9ec8a3e03ecb31890cd24150e088",
  "index_entries_sha256": "3eb1bb714d56edeb0dccbe9c08c442394c1e949840b28c859f723dcf00c144a1",
  "staged": {
    "data/fire_varna_hotels.json": {
      "sha256": "eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51",
      "bytes": 151263,
      "matches_expected": true
    },
    "data/fire_varna_location_inputs.json": {
      "sha256": "c7450ded1b8ade5bdb3b63924971d2be0d9b9ea1a792175df0331526ed4679ee",
      "bytes": 65111,
      "matches_expected": true
    },
    "data/fire_varna_places.json": {
      "sha256": "3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66",
      "bytes": 128401,
      "matches_expected": true
    },
    "data/place_categories.json": {
      "sha256": "9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231",
      "bytes": 77998,
      "matches_expected": true
    },
    "data/place_identity.json": {
      "sha256": "4819ab3e1d74f516de051b5f05abf4721c6f8c42cf2c5c2a293ba95eedc7d0c2",
      "bytes": 228980,
      "matches_expected": true
    },
    "data/registry_manifest.json": {
      "sha256": "bb04640e9762a12a5028b99ee70b1053687cfa4ed55b6e7e2f4c2e191b114abb",
      "bytes": 142309,
      "matches_expected": true
    },
    "scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json": {
      "sha256": "5ec64c682a46463c1f4890510736a13a5766ada61fcc757af281f6c82d3a7d94",
      "bytes": 965388,
      "matches_expected": true
    }
  },
  "staged_paths_exact": true,
  "commit_changed_paths": [
    "scratch/granitsi/fixed_point_negatives.py",
    "src/qa_fixed_point.py"
  ],
  "payload_commit_overlap": [],
  "tracked_worktree_sha256": "2fc477e310681c278490009421c0006f5541015800315086af64a9a00379aaf2"
}

codex
Поправката е потвърдена: `0ba2e9d` променя само двата заявени файла, с author и committer `Claude Executor`. Без `--ignore` кодът сравнява `read_bytes()`, а седемте стейджнати SHA256 съвпадат изцяло със S26. Отрицателният тест записва фикстури в scratch; проверявам изпълнението му в ограниченията на тази read-only сесия.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'python -B scratch/granitsi/fixed_point_negatives.py' in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'python -B src/qa_fixed_point.py --a scratch/granitsi/fixpoint/ledger_run1.json --b scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json' in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'python -B src/qa_fixed_point.py --a scratch/granitsi/fixpoint/places_run1.json --b data/fire_varna_places.json --ignore _meta.generated' in C:\git\varna_3d
 exited 1 in 0ms:
Traceback (most recent call last):
  File "C:\git\varna_3d\scratch\granitsi\fixed_point_negatives.py", line 145, in <module>
    sys.exit(main())
  File "C:\git\varna_3d\scratch\granitsi\fixed_point_negatives.py", line 75, in main
    same = write("places_copy.json", places)
  File "C:\git\varna_3d\scratch\granitsi\fixed_point_negatives.py", line 59, in write
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n",
  File "C:\Program Files\Python310\lib\pathlib.py", line 1154, in write_text
    with self.open(mode='w', encoding=encoding, errors=errors, newline=newline) as f:
  File "C:\Program Files\Python310\lib\pathlib.py", line 1119, in open
    return self._accessor.open(self, mode, buffering, encoding, errors,
PermissionError: [Errno 13] Permission denied: 'C:\\git\\varna_3d\\scratch\\granitsi\\_fixed_point_neg\\places_copy.json'

 succeeded in 0ms:
  ok    неподвижна точка · ledger_run1.json ↔ lot1v_locations_375_p8a_07.09.json · 965388 байта · сурови байтове, без изключения (директно сравнение)

 succeeded in 0ms:
  ok    неподвижна точка · places_run1.json ↔ fire_varna_places.json · 128321 байта · махнати ключове: _meta.generated

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'python -B src/qa_fixed_point.py --a scratch/granitsi/fixpoint/hotels_run1.json --b data/fire_varna_hotels.json --ignore _meta.generated' in C:\git\varna_3d
 succeeded in 14ms:
  ok    неподвижна точка · hotels_run1.json ↔ fire_varna_hotels.json · 151183 байта · махнати ключове: _meta.generated

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git --no-optional-locks diff --exit-code -- data/place_identity.json data/fire_varna_location_inputs.json data/registry_manifest.json data/fire_varna_places.json data/fire_varna_hotels.json data/place_categories.json scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json' in C:\git\varna_3d
 succeeded in 0ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import copy, hashlib, json, os, subprocess, sys
from pathlib import Path
root = Path.cwd()
out = root / \"scratch/granitsi/_fixed_point_neg\"
places_path = root / \"data/fire_varna_places.json\"
ledger_path = root / \"scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json\"
places = json.loads(places_path.read_text(encoding=\"utf-8\"))
ledger = json.loads(ledger_path.read_text(encoding=\"utf-8\"))
def encoded(doc, indent=1, newline=os.linesep):
    return (json.dumps(doc, ensure_ascii=False, indent=indent) + \"\\n\").replace(\"\\n\", newline).encode(\"utf-8\")
cases = []
def add(label, a, fixture, expected_bytes, ignore, want):
    cases.append((label, a, out / fixture, expected_bytes, ignore, want))
add(\"control copy\", places_path, \"places_copy.json\", encoded(places), True, 0)
doc = copy.deepcopy(places)
doc[\"places\"][0][\"zone\"] = \"\\u043a\\u0432. \\u0418\\u0437\\u043c\\u0438\\u0441\\u043b\\u0435\\u043d\\u043e\"
add(\"changed row\", places_path, \"neg_row.json\", encoded(doc), True, 1)
doc = copy.deepcopy(ledger)
doc[\"rows\"][0][\"new_zone\"] = \"\\u043a\\u0432. \\u0418\\u0437\\u043c\\u0438\\u0441\\u043b\\u0435\\u043d\\u043e\"
add(\"changed ledger\", ledger_path, \"neg_ledger.json\", encoded(doc), False, 1)
doc = copy.deepcopy(places)
doc[\"places\"] = list(reversed(doc[\"places\"]))
add(\"array order\", places_path, \"neg_order.json\", encoded(doc), True, 1)
doc = copy.deepcopy(places)
doc[\"places\"][0].pop(\"zone\", None)
add(\"missing key\", places_path, \"neg_missing.json\", encoded(doc), True, 1)
doc = copy.deepcopy(places)
doc[\"_meta\"][\"generated\"] = \"1970-01-01T00:00:00\"
add(\"clock ignored\", places_path, \"neg_clock.json\", encoded(doc), True, 0)
add(\"clock raw\", places_path, \"neg_clock.json\", encoded(doc), False, 1)
add(\"ledger indent=2 raw\", ledger_path, \"neg_indent2.json\", encoded(ledger, 2, \"\\n\"), False, 1)
add(\"ledger CRLF raw\", ledger_path, \"neg_crlf.json\", ledger_path.read_text(encoding=\"utf-8\").replace(\"\\n\", \"\\r\\n\").encode(\"utf-8\"), False, 1)
add(\"places indent=2 ignored\", places_path, \"ctl_indent2.json\", encoded(places, 2, \"\\n\"), True, 0)
for label, a, b, expected, ignore, want in cases:
    if not b.is_file() or b.read_bytes() "'!= expected:
        print(label + ": existing fixture missing or differs from exact harness-generated bytes")
        sys.exit(2)
print("Existing fixtures: 10/10 cases match exact harness-generated bytes; no files written.")
failed = 0
for label, a, b, expected, ignore, want in cases:
    argv = [sys.executable, "-B", "src/qa_fixed_point.py", "--a", str(a), "--b", str(b)]
    if ignore:
        argv += ["--ignore", "_meta.generated"]
    result = subprocess.run(argv, capture_output=True, encoding="utf-8", errors="replace")
    ok = result.returncode == want
    failed += not ok
    print(f"{label}: exit={result.returncode} expected={want} {'"'PASS' if ok else 'FAIL'}\")
print(f\"Read-only replay: {len(cases)-failed}/{len(cases)} passed\")
sys.exit(1 if failed else 0)
'@ | python -B -" in C:\git\varna_3d
 succeeded in 637ms:
Existing fixtures: 10/10 cases match exact harness-generated bytes; no files written.
control copy: exit=0 expected=0 PASS
changed row: exit=1 expected=1 PASS
changed ledger: exit=1 expected=1 PASS
array order: exit=1 expected=1 PASS
missing key: exit=1 expected=1 PASS
clock ignored: exit=0 expected=0 PASS
clock raw: exit=1 expected=1 PASS
ledger indent=2 raw: exit=1 expected=1 PASS
ledger CRLF raw: exit=1 expected=1 PASS
places indent=2 ignored: exit=0 expected=0 PASS
Read-only replay: 10/10 passed

codex
Трите реални сравнения върнаха `0/0/0`. Самият negative harness спря с `PermissionError` при запис на фикстура. Проверих съществуващите фикстури байт по байт спрямо генерирането в скрипта и изпълних всичките 10 сравнения само за четене: всички дадоха очакваните кодове, включително `1/1/0` за новата секция 5. Независимата проверка на трите комит-текста също мина.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import hashlib, json, subprocess
def git(*args):
    return subprocess.check_output([\"git\",\"--no-optional-locks\",*args])
staged=git(\"diff\",\"--cached\",\"--name-only\",\"-z\").decode().rstrip(\"\\0\").split(\"\\0\")
entries=git(\"ls-files\",\"--stage\",\"-z\")
entries_sha=hashlib.sha256(entries).hexdigest()
expected_index=\"3eb1bb714d56edeb0dccbe9c08c442394c1e949840b28c859f723dcf00c144a1\"
commit_oids={line.split()[2] for line in git(\"ls-tree\",\"-r\",\"0ba2e9d\").decode().splitlines()}
overlap=[]
for p in staged:
    oid=git(\"rev-parse\",\":\"+p).decode().strip()
    if oid in commit_oids:
        overlap.append(p)
print(json.dumps({
\"HEAD\":git(\"rev-parse\",\"HEAD\").decode().strip(),
\"index_entries_sha256\":entries_sha,
\"index_unchanged\":entries_sha==expected_index,
\"staged_blob_objects_present_in_0ba2e9d_tree\":overlap,
\"staged_paths\":len(staged)},indent=2))
assert entries_sha==expected_index and not overlap and len(staged)==7
'@ | python -B -" in C:\git\varna_3d
 succeeded in 161ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
{
  "HEAD": "0ba2e9d20fdf9ec8a3e03ecb31890cd24150e088",
  "index_entries_sha256": "3eb1bb714d56edeb0dccbe9c08c442394c1e949840b28c859f723dcf00c144a1",
  "index_unchanged": true,
  "staged_blob_objects_present_in_0ba2e9d_tree": [],
  "staged_paths": 7
}

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git --no-optional-locks -c core.quotepath=false status --porcelain=v1 -uno' in C:\git\varna_3d
 succeeded in 0ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
M  data/fire_varna_hotels.json
M  data/fire_varna_location_inputs.json
M  data/fire_varna_places.json
M  data/place_categories.json
M  data/place_identity.json
M  data/registry_manifest.json
 M scratch/place_bodies/qa_place_bodies.md
A  scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json

codex
**ГОДНО за трите комита на Петър** в провереното състояние на 07.09.2026, със следната отчетена особеност на тестовото изпълнение.

- **Комитът:** `git show 0ba2e9d` → **0**. Променя само `src/qa_fixed_point.py` и `scratch/granitsi/fixed_point_negatives.py`. Author **и** committer са `Claude Executor <executor@local>`. Без `--ignore` сравнението действително използва `Path.read_bytes()`; нормализацията се изпълнява само при назовани ключове.

- **Отрицателните проверки:** точната команда `python -B scratch/granitsi/fixed_point_negatives.py` → **1**, поради `PermissionError` при запис на `places_copy.json`, преди тестовете. Затова проверих наличните фикстури срещу точните генерирани байтове и пуснах компаратора директно, без записи: **10/10 очаквани резултата**, общ изход **0**. Новата секция 5 даде **1 / 1 / 0**: ledger с `indent=2`, ledger с CRLF, places с `indent=2` и `--ignore`.

- **Реалните сравнения** чрез `python -B src/qa_fixed_point.py`:

  | Сравнение | Режим | Exit |
  |---|---|---:|
  | `ledger_run1` ↔ окончателния ledger | сурови байтове, 965388 B | **0** |
  | `places_run1` ↔ data износа | `--ignore _meta.generated` | **0** |
  | `hotels_run1` ↔ data износа | `--ignore _meta.generated` | **0** |

- **Стейджнатите блобове:** SHA256 върху суровия `git cat-file blob :path` потвърди **7/7 пълни хеша**: `4819ab3e…`, `c7450ded…`, `3dffc264…`, `eb8fa85c…`, `9064705a…`, `bb04640e…`, `5ec64c68…`. Нито един от тези blob objects присъства в дървото на `0ba2e9d`. `git diff --exit-code` за седемте пътя → **0**.

- **Комит-текстовете:** независима проверка → **0**; трите subject реда съвпадат дословно с §6, включително подписания документ в `4e9606c`. Телата съдържат **7/7 подписни SHA256**.

`Ran 16 tests OK` приемам като предоставения от теб резултат от главната сесия; не го представям като мой прогон. HEAD, index и `git status` останаха непроменени. Няма редакции, комити или remote команди.
tokens used
60,703
**ГОДНО за трите комита на Петър** в провереното състояние на 07.09.2026, със следната отчетена особеност на тестовото изпълнение.

- **Комитът:** `git show 0ba2e9d` → **0**. Променя само `src/qa_fixed_point.py` и `scratch/granitsi/fixed_point_negatives.py`. Author **и** committer са `Claude Executor <executor@local>`. Без `--ignore` сравнението действително използва `Path.read_bytes()`; нормализацията се изпълнява само при назовани ключове.

- **Отрицателните проверки:** точната команда `python -B scratch/granitsi/fixed_point_negatives.py` → **1**, поради `PermissionError` при запис на `places_copy.json`, преди тестовете. Затова проверих наличните фикстури срещу точните генерирани байтове и пуснах компаратора директно, без записи: **10/10 очаквани резултата**, общ изход **0**. Новата секция 5 даде **1 / 1 / 0**: ledger с `indent=2`, ledger с CRLF, places с `indent=2` и `--ignore`.

- **Реалните сравнения** чрез `python -B src/qa_fixed_point.py`:

  | Сравнение | Режим | Exit |
  |---|---|---:|
  | `ledger_run1` ↔ окончателния ledger | сурови байтове, 965388 B | **0** |
  | `places_run1` ↔ data износа | `--ignore _meta.generated` | **0** |
  | `hotels_run1` ↔ data износа | `--ignore _meta.generated` | **0** |

- **Стейджнатите блобове:** SHA256 върху суровия `git cat-file blob :path` потвърди **7/7 пълни хеша**: `4819ab3e…`, `c7450ded…`, `3dffc264…`, `eb8fa85c…`, `9064705a…`, `bb04640e…`, `5ec64c68…`. Нито един от тези blob objects присъства в дървото на `0ba2e9d`. `git diff --exit-code` за седемте пътя → **0**.

- **Комит-текстовете:** независима проверка → **0**; трите subject реда съвпадат дословно с §6, включително подписания документ в `4e9606c`. Телата съдържат **7/7 подписни SHA256**.

`Ran 16 tests OK` приемам като предоставения от теб резултат от главната сесия; не го представям като мой прогон. HEAD, index и `git status` останаха непроменени. Няма редакции, комити или remote команди.
