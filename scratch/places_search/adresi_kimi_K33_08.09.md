kimi version 0.34.0
• Let me read the files. The working directory is the temp folder, but I should cite paths relative to the "kimi_depth" root. Let me read the four files.

• Ще прочета четирите файла, за да анализирам проблема.

• Now the JSON files. bridge_sample_1500.json — random sample of 1500 clusters with fields. adresi_bridge_depth_08.09.json — same table + top 40 disagreements. Let me check sizes first, then read strategically. Actually I need to analyze distribution of distance_m and margin_ratio by confidence from the sample. I can do that with... "САМО АНАЛИЗИРАЙ. Не изпълнявай команди, които пишат по диска" — running read-only commands is fine. I can use node/python one-liners to compute stats without writing files. jq might be available. Let me check file sizes first.

• Прочетох мярката и полигоните. Сега ще разгледам JSON данните и извадката.  4391 adresi_bridge_depth_08.09.json
496290 bridge_sample_1500.json
500681 total
{
 "by_key": {
  "osm|nearest_point|low": {
   "outside": 3649,
   "agree_edge": 2244,
   "disagree_edge": 1402,
   "agree": 1776,
   "disagree": 1221,
   "overlap": 507
  },
  "kais|-|kais": {
   "overlap": 462,
   "agree_edge": 6094,
   "agree": 7070,
   "disagree": 4449,
   "outside": 3710,
   "disagree_edge": 3765
  },
  "osm|nearest_point|high": {
   "agree": 6265,
   "disagree": 859,
   "agree_edge": 2947,
   "overlap": 842,
   "disagree_edge": 1095,
   "outside": 527
  },
  "osm|nearest_point|medium": {
   "agree_edge": 2421,
   "disagree_edge": 1278,
   "overlap": 420,
   "agree": 2728,
   "disagree": 834,
   "outside": 754
  },
  "osm|polygon_cover|high": {
   "disagree_edge": 363,
   "disagree": 761,
   "outside": 268,
   "overlap": 246,
   "agree_edge": 139,
   "agree": 89,
   "no_word": 10
  },
  "osm|nearest_point|flagged": {
   "disagree_edge": 408,
   "outside": 347,
   "agree_edge": 160,
   "agree": 64,
   "disagree": 434,
   "overlap": 6
  }
 },
 "disagree_top": [
  [
   "кв. \"ГАЛАТА\"",
   "с.о. Боровец-юг",
   1293
  ],
  [
   "кв. Розова долина",
   "кв. Аспарухово",
   771
  ],
  [
   "с.о.\"Траката\"",
   "Евксиноград",
   649
  ],
  [
   "ж.к. БРИЗ",
   "м-т Свети Никола",
   560
  ],
  [
   "8 микрорайон",
   "Център",
   466
  ],
  [
   "Цветен квартал",
   "к
[{"label": "кв. Левски, ул. \"Топра Хисар\" №22", "address_line": "ул. \"Топра Хисар\" №22", "pin": [27.91764, 43.21683], "word": "кв. Левски", "source": "osm", "mode": "nearest_point", "confidence": "low", "distance_m": 808.414916913685, "margin_ratio": 1.0395493043156878, "second": "Цветен квартал"}, {"label": "Максуда, ул. \"САМАРСКО ЗНАМЕ\" №32", "address_line": "ул. \"САМАРСКО ЗНАМЕ\" №32", "pin": [27.8908, 43.21347], "word": "Максуда", "source": "osm", "mode": "nearest_point", "confidence": "medium", "distance_m": 332.8830259391849, "margin_ratio": 1.336045399876184, "second": "ж.к. Св. Иван Рилски"}, {"label": "м-т Кокарджа, ФРАНГА ДЕРЕ И КОКАРДЖА", "address_line": "ФРАНГА ДЕРЕ И КОКАРДЖА", "pin": [27.90642, 43.23553], "word": "м-т Кокарджа", "source": "osm", "mode": "nearest_point", "confidence": "high", "distance_m": 78.05403966560067, "margin_ratio": 1.694458098412325, "second": "Голяма Кокарджа"}, {"label": "Адрес: гр варна район аспарухово южна промишлена зона", "address_line": "ЮЖНА ПРОМИШЛЕНА ЗОНА", "pin": [27.89263, 43.20051], "word": "ЮЖНА ПРОМИШЛЕНА ЗОНА", "source": "kais", "mode": null, "confidence": "kais", "distance_m": null, "margin_ratio": null, "second": null}, {"label": "м-т Сотира, гр. Варна, район Приморски", "address_line": "гр. Варна, район Приморски", "pin": [27.93117, 43.23299], "word": "м-т Сотира", "source": "osm", "mode": "nearest_point", "confidence": "low", "distance_m": 797.3815818102955, "margin_ratio": 1.0598720788142124, "second": "кв. Изгрев"}, {"label": "Галата, ул. ФИЧОЗА №10", "address_line": "ул. ФИЧОЗА №10", "pin": [27.93426, 43.161], "word": "Галата", "sourc


• Now compute stats from bridge_sample_1500.json: distribution of distance_m and margin_ratio by confidence for osm nearest_point, plus how often second_choice equals the polygon... wait, sample doesn't include polygon-under-pin? Let me check fields. The sample has label, address_line, pin, word, source, mode, confidence, distance_m, margin_ratio, second. No polygon field apparently. Let me check the rest of the depth JSON (top 40 disagreements) and run stats via python/node one-liner (read-only, no disk writes).['by_key', 'disagree_top', 'n']
['кв. "ГАЛАТА"', 'с.о. Боровец-юг', 1293]
['кв. Розова долина', 'кв. Аспарухово', 771]
['с.о."Траката"', 'Евксиноград', 649]
['ж.к. БРИЗ', 'м-т Свети Никола', 560]
['8 микрорайон', 'Център', 466]
['Цветен квартал', 'кв. Левски', 458]
['Колхозен пазар', 'кв. Тракия', 291]
['кв. ВИНИЦА', 'с.о. Манастирски рид', 238]
['кв. ВИНИЦА', 'м-т Акчелар', 224]
['8 микрорайон', 'Гръцката махала', 209]
['м. ТРАКАТА', 'Средна Трака', 195]
['Максуда', 'кв. Св. Иван Рилски', 181]
['ж.к. "ВЛАДИСЛАВ ВАРНЕНЧИК"', 'кв. Владиславово', 162]
['ж.к. Св. Иван Рилски', 'Западна промишлена зона', 153]
['Гръцката махала', 'Център', 152]
['с.о. Ален Мак', 'к.к. Златни пясъци', 128]
['ж.к. Дружба', 'кв. Аспарухово', 119]
['м-т Кокарджа', 'с.о. Пчелина', 119]
['кв. Чайка', 'кв. Левски', 115]
['в.з. Варна', 'Евксиноград', 93]
['ж.к. Младост 1', 'Западна промишлена зона', 84]
['м. "ВИЛИТЕ"', 'кв. Аспарухово', 73]
['с.о. Ален Мак', 'к.к. Чайка', 64]
['ж.к. Възраждане 3', 'с.о. Пчелина', 63]
['4-ти микрорайон', 'Център', 58]
['кв. Левски', 'кв. Изгрев', 57]
['Рибарско селище Карантината', 'кв. Аспарухово', 55]
['ж.к. Младост 1', 'кв. Трошево', 54]
['кв. "ГАЛАТА"', 'м-т Фичоза', 54]
['"Вилна зона"', 'Евксиноград', 53]
['к.к "Св.св. Константин и Елена"', 'Евксиноград', 52]
['кв. "ГАЛАТА"', 'м-т Зеленика', 50]
['Западна промишлена зона', 'ж.к. Младост 2', 46]
['м. ТРАКАТА', 'с.о. Горна Трака', 46]
['Голяма Кокарджа', 'кв. Изгрев', 43]
['м-т Сотира', 'кв. Изгрев', 42]
['м. Св. Никола', 'ж.к. Бриз', 41]
['кв. ВИНИЦА', 'с.о. Перчемлията', 41]
['с.о. "Траката"', 'Евксиноград', 41]
['кв. Владиславово', 'с.о. Ментеше', 36]
n= 1500 keys= ['address_line', 'confidence', 'distance_m', 'label', 'margin_ratio', 'mode', 'pin', 'second', 'source', 'word']
('kais', None, 'kais') 633
('osm', 'nearest_point', 'high') 314
('osm', 'nearest_point', 'low') 278
('osm', 'nearest_point', 'medium') 200
('osm', 'polygon_cover', 'high') 39
('osm', 'nearest_point', 'flagged') 36
Now compute distance_m / margin_ratio distributions per confidence for osm nearest_point. Also examine second-choice relationship: does second choice equal the signed polygon? The sample doesn't have polygon-under-pin field. But margin_ratio semantics: likely distance to second / distance to first? Let me compute stats.high     n= 314 dist med=    235 p75=    313 p90=    370 max=    399 | margin med=3.00 p25=2.06 p10=1.70 min=1.51
medium   n= 200 dist med=    470 p75=    516 p90=    548 max=    594 | margin med=1.51 p25=1.35 p10=1.25 min=1.20
low      n= 278 dist med=    706 p75=    828 p90=    986 max=   1197 | margin med=1.18 p25=1.08 p10=1.04 min=1.00
flagged  n=  36 dist med=   1521 p75=   2467 p90=   4075 max=   4116 | margin med=1.13 p25=1.10 p10=1.03 min=1.01
high dist<100: 29 <250: 171 <500: 314 >=500: 0
medium dist<100: 0 <250: 4 <500: 132 >=500: 68
low dist<100: 0 <250: 4 <500: 51 >=500: 227
flagged dist<100: 0 <250: 0 <500: 0 >=500: 36
high margin<1.1: 0 1.1-1.3: 0 >=1.3: 314
medium margin<1.1: 0 1.1-1.3: 32 >=1.3: 168
low margin<1.1: 80 1.1-1.3: 108 >=1.3: 90
flagged margin<1.1: 13 1.1-1.3: 17 >=1.3: 6
Confidence is clearly a deterministic function of distance: high <400m, medium 400–600m, low 600–1200m, flagged >1200m (approx thresholds; let me verify exact cut points). high max=399, medium min ~400? low min ~600? flagged min ~1200? Let me check min/max boundaries precisely.

  Also: how often does second_choice equal the signed polygon under the pin? The sample lacks polygon field, so can't directly. But the md table gives agree/disagree per confidence. I can also check from sample: share where second is the "real" answer — can't verify without polygons. Skip; use md §8 numbers.

  Check confidence thresholds precisely and polygon_cover distance availability.low 207.7 1197.4
medium 209.4 594.4
high 31.5 399.2
flagged 1229.7 4116.3
kais with distance: 0
polygon_cover with distance: 0 of 39
low n: 278
Interesting: low min is 207.7, medium min 209.4, high max 399.2. So confidence isn't purely distance: high ≤400; medium/low overlap in 200–600 range. Probably confidence = f(distance, margin_ratio): e.g., high if dist<400 and margin≥1.5? Check: low rows with dist<400 — what's their margin? And medium rows with margin<1.3.high
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
TypeError: '<' not supported between instances of 'NoneType' and 'float'
Some rows have distance_m None but confidence high? Probably polygon_cover rows have confidence high too — but I filtered by confidence only, not mode. Fix: filter mode == nearest_point.high n= 314
   32 18.46 | кв. Христо Ботев | 2nd: Максуда
   33 48.16 | Боровец | 2nd: Кантара
   35 17.7 | Колхозен пазар | 2nd: кв. Христо Ботев
   398 1.78 | Галата | 2nd: Зеленика
   399 1.55 | кв. Христо Ботев | 2nd: Колхозен пазар
   399 1.51 | Колхозен пазар | 2nd: кв. Христо Ботев
medium n= 200
   209 1.41 | ж.к. Св. Иван Рилски | 2nd: Максуда
   223 1.38 | ж.к. Св. Иван Рилски | 2nd: Максуда
   244 1.49 | Максуда | 2nd: кв. Христо Ботев
   594 1.21 | Дълбокото дере | 2nd: Средна Трака
   594 1.74 | кв. Кайсиева градина | 2nd: кв. Владиславово
   594 2.55 | Боровец | 2nd: Чигана
low n= 278
   208 1.17 | Голяма Кокарджа | 2nd: м-т Кокарджа
   232 1.14 | м-т Пчелина | 2nd: Малка Кокарджа
   245 1.14 | Максуда | 2nd: ж.к. Св. Иван Рилски
   1166 1.08 | Боровец | 2nd: Кантара
   1169 1.1 | Боровец | 2nd: Кантара
   1197 1.2 | Манастирски рид | 2nd: кв. Виница
flagged n= 36
   1230 1.06 | кв. Владиславово | 2nd: кв. Кайсиева градина
   1242 1.13 | Боровец | 2nd: Кантара
   1249 1.96 | кв. Владиславово | 2nd: кв. Кайсиева градина
   4096 1.1 | с.о. Ален Мак | 2nd: Чайка
   4112 1.1 | с.о. Ален Мак | 2nd: Чайка
   4116 1.1 | с.о. Ален Мак | 2nd: Чайка
So confidence rule: high = dist<400 AND margin≥1.5 (roughly); medium = dist<600 AND margin ≥ ~1.2; low = otherwise (margin <~1.2 or dist 600–1200); flagged = dist>1200. Boundary: high max 399 with margin 1.51; medium min 209 with margin 1.41 (<1.5); low min 208 with margin 1.17 (<1.2). So likely: high if d<400 and margin≥1.5; medium if d<600 and margin≥1.2; flagged if d>1200; else low. Good.

  Now agreement rates by confidence from §8 table (adresi_bridge_depth_08.09.json by_key):
  - high: agree 6265, agree_edge 2947, disagree 859+1095=1954, outside 527, overlap 842; total 12535. "съгласни общо" = agree+agree_edge = 9212 (73.5%); disagree incl edge = 1954 (15.6%).
  - medium: agree 2728+2421=5149 (61%); disagree 834+1278=2112 (25%); outside 754; overlap 420.
  - low: agree 1776+2244=4020 (37%); disagree 1221+1402=2623 (24%); outside 3649 (34%); overlap 507.
  - flagged: agree 64+160=224 (16%); disagree 434+408=842 (59%); outside 347; overlap 6.
  - polygon_cover high: agree 89+139=228 (12%); disagree 761+363=1124 (60%); outside 268; overlap 246; no_word 10.
  - kais: agree 7070+6094=13164 (51.5%); disagree 4449+3765=8214 (32%); outside 3710; overlap 462.

  Note the md §8 text says "Несъгласието НЕ е само при OSM: и кадастралните думи (KAIS 25 550) са несъгласни в 8 214 случая" — matches disagree+disagree_edge. Overall: съгласни 31 997 (53%), несъгласни 16 869 (28%), извън 9 255 (15%), припокриване 2 483 (4%).

  Also interesting: "edge" (в лентата) — пинът на <max(50, precision_m) от ръба. Since all polygons except mladost2 are precision 100, band = 100m. Agree in band is huge: 14 005 of 31 997 agreements (44%) are within 100m of the edge — token agreement near an edge is weak evidence (could be coincidence/neighbour name). Also note edge classification: "съгл. в лентата" is separate from "съгласни" — 17 992 interior agree + 14 005 edge agree = 31 997.

  Task (1) classification:
  (a) word error (OSM nearest point at hundreds of meters, low confidence, second candidate = correct): examples: Студентска бл. 11 → "кв. Чайка" at 707m low, second м-т Сотира (§7). From sample: "кв. Левски, ул. Топра Хисар №22" word кв. Левски low 808m, second Цветен квартал. м-т Сотира at 797m low, second кв. Изгрев. flagged: с.о. Ален Мак at 4.1 km — total failure. Scale: low nearest_point 10 799 (36% outside polygon!), flagged 1 419.
  (b) naming system difference: KAIS disagreements 8 214 — ГАЛАТА (1293 → Боровец-юг + 54 Фичоза + 50 Зеленика ≈ 1 397), ВИНИЦА (238+224+41+... ≈ 500+ in bridge table; in address-level measure 5 333 total), Траката (649+41+46 ≈ 736), 8 микрорайон (466+209 = 675), Максуда 181, 4-ти микрорайон 58, Цветен квартал 458, Розова долина 771 (Розова долина IS a signed polygon itself! word "кв. Розова долина" → polygon кв. Аспарухово — that's a polygon question: rozova_dolina polygon exists; why are 771 points labeled Розова долина inside Аспарухово polygon? Either KAIS word covers both, or Аспарухово polygon covers Розова долина area. Similarly ж.к. Дружба → кв. Аспарухово 119 — druzhba has parent asparuhovo; smallest-containing should pick Дружба... unless Дружба polygon doesn't cover those points, i.e. Дружба polygon is too small or points outside). Interesting: "ж.к. Младост 1 → Западна промишлена зона 84" and "ж.к. Възраждане 3 → с.о. Пчелина 63" — children with parents; smallest-containing logic should have caught the child if covered.
  (c) polygon question: ГАЛАТА→Боровец-юг 1 293 (Галата кадастрална зона spans Боровец/Фичоза/Зеленика — but is this polygon or word issue? The md flags it as possibly polygon). ж.к. БРИЗ → м-т Свети Никола 560: Briz polygon signed, but 560 Briz-word points fall in Свети Никола polygon → either Свети Никола polygon was drawn over Briz, or Briz word used loosely. Also Гръцката махала → Център 152, кв. Чайка → кв. Левски 115 (Чайка кв vs Чайка кк confusion + Левски edge), с.о. Ален Мак → Златни пясъци 128/Чайка кк 64.

  Task (2): nearest_point reliability by confidence:
  - high (d<400, margin≥1.5): 73.5% token agreement, 15.6% disagree, 4.2% outside. But agreement ≠ truth (see б).
  - medium (d<600, margin≥1.2): 61% agree, 25% disagree, 9% outside.
  - low (d 600–1200 or margin<1.2): 37% agree, 24% disagree, 34% outside — coin flip.
  - flagged (d>1200): 16% agree, 59% disagree, 24% outside — garbage.
  - Agreement skew: of agreed, the share "in band" (<100m of edge): high 2947/9212=32%, medium 47%, low 56%, flagged 71%. So even "agreement" for low/flagged is mostly near-edge coincidence.
  Prag: nearest_point high is acceptable as WITNESS (свидетел), not canon; medium borderline (only with margin≥1.5?); low/flagged must not be used even as witness for the word — only distance recorded. As canon: 0.

  Actually a threshold suggestion: distance<400m AND margin≥1.5 (the "high" rule itself) is where the heuristic was reliable (89% non-disagree among inside-polygon). Below that it degrades monotonically.

  Task (3): what Petar must decide for 9 255 outside + 2 483 overlap:
  - Outside: 3 649 of them are low-confidence OSM nearest_point (word from a node hundreds of meters away) — these mostly need coverage, not cleanup. Missing polygons per §3 of address measure and polygons list: Център exists! But 8 810 without word + 753 tsentar outside Център polygon → Център polygon too small / holes. Missing words entirely: Цветен квартал (197 outside + 458 disagreements onto Левски), Колхозен пазар exists as polygon but 490 outside, Левски 478 outside, Гръцка махала 410, Чайка 219, Трошево 22, Победа 54, Виница 1 461 outside (Виница зона covers Акчелар/Ален Мак/Св. Никола/Сотира/Перчемлията/Евксиноград/Горна Трака/Манастирски рид — those exist as polygons; 1 461 points still outside all). Missing relations (parent): polygons with parent: borovets_sever/yug→borovets (no borovets polygon exists! parent references a nonexistent code — dangling parent), druzhba→asparuhovo, kaisieva→vladislavovo, mladost1→mladost, vazrazhdane1-4? no—vazrazhdane1/2 have no parent; mladost1 parent mladost but mladost2 has parent null (inconsistent). Missing parents that would help smallest-containing: e.g., Владислав ВарненчИК жк has no polygon (disagreement 162 → Владиславово). Kinds present: парк (Морска градина), пз, зона — precision 100 for all except mladost2 (50). Precision 100 for all 59 human polygons means band = 100m for every edge decision → 14 005 + 8 311 edge cases; precision should reflect actual drawing confidence, uniform 100 hides quality differences.
  - Overlap 2 483: which polygons overlap — e.g., Розова долина vs Аспарухово (771!), Дружба vs Аспарухово (parent relation exists → smallest-containing resolves if nesting is clean, but 119 disagreements suggest Дружба polygon not containing those points), ЗПЗ vs Младост 1/2 (84+46), Св. Иван Рилски vs ЗПЗ 153. Petar must decide: is Розова долина inside Аспарухово (then parent + no overlap) or adjacent (then fix Аспарухово boundary)? Same Дружба. That's a board decision, not automation.

  Task (4): gate "веднъж завинаги" per build:
  - canon comes only from signed polygon under pin (smallest containing). Metrics per build: % clusters with canon word (target: growing to ~100), nearest_point-as-canon = 0 (hard fail if >0), unresolved/outside count (target decreasing; fail if increases vs baseline), overlap count unresolved = 0 (must be resolved by parent/smallest rule deterministically), disagreement between canon and KAIS word reported but non-blocking (witness), new tokens not in lexicon = 0 or review list. Threshold that stops the build: any cluster labeled by nearest_point; any increase in outside-count; any duplicate label (квартал+бл. without street — the Чайка бл.11 case). Deterministic: same inputs → same labels.

  Task (5): method biases of the measure:
  - Token agreement bias: word "кв. Левски" ∩ tokens of "кв. Левски" — but "кв." token shared; if matching uses any token, "Чайка" matches both chaika_kk and chaika_kv (two polygons share the token Чайка!) — agreement can be counted toward the wrong Чайка. Also "Боровец" word vs Боровец-север/юг tokens.
  - Smallest containing polygon: penalizes big polygons (ЗПЗ, Център) — points inside both Център and Гръцката махала resolve to the smaller; disagreement "Гръцката махала → Център 152" then... wait, smallest-containing would pick Гръцката махала. But table says word Гръцката махала → polygon Център, meaning the point is inside Център but NOT inside Гръцката махала polygon → so smallest-containing fine there. The bias: smallest-containing assumes nesting is intentional; with overlaps from sloppy borders it picks the smaller even if wrong.
  - Band: fixed max(50, precision_m) with precision 100 everywhere → band useless as quality signal; also edge-agreement counted separately but "в лентата" agreement still counts as agreement in the 53% headline — inflates agreement.
  - Token agreement doesn't normalize kind prefixes (кв./ж.к./м-т/с.о.) — "м. Св. Никола" vs "м-т Свети Никола" presumably matches; but "8 микрорайон" has no polygon token at all → always disagreement even when location right. This conflates "wrong place" with "untranslatable name system": 28% disagreement ≠ 28% wrong location.
  - Also: agreement measure uses the word from the same bridge being evaluated — circular for OSM rows (word vs polygon), fine as consistency check but not truth.
  - The 60 polygons cover only part of the city: 15% outside is partly coverage, not error; measure counts them as failures of the word.

  Verdict: structural. Evidence: 3 independent causes (heuristic source, naming-system mismatch, polygon completeness) each with thousands of cases; the same bug produces downstream duplicate labels (Чайка бл. 11 ×2); fixing one-by-one won't converge because KAIS "zones" and OSM nodes systematically diverge from the polygon system. ~47% of clusters (28 617 = 16 869 disagree + 9 255 outside + 2 483 overlap) lack trustworthy canon.

  Word limit 900 Bulgarian words. Paths cited relative to kimi_depth root: just file names (files are at root). E.g. `adresi_po_poligon_measure_08.09.md` §8, `adresi_bridge_depth_08.09.json`, `bridge_sample_1500.json`, `polygons_props_no_geometry.json`.

  Write the answer now, ≤900 words, with numbers.

• Анализът е готов. По-долу е присъдата — само четене, нищо не е пипано.

  # К33 · Дълбочина на проблема с кварталните думи

  **Присъда: СТРУКТУРЕН проблем.** Не е нито повърхностен („няколко грешни етикета"), нито среден („един бъгав модул"). Три независими причини — извор-евристика, несъвместима система от имена, непълнота/спорност на полигоните — всяка с хиляди случая, и 47 % от 60 614 клъстера (16 869 несъгласни + 9 255 извън + 2 483 припокриване, `adresi_bridge_depth_08.09.json`) нямат надежден канон. Доказателство за структурност: бъгът вече е произвел недопустим страничен ефект — два физически блока с идентичен етикет „кв. Чайка, бл. 11" (`adresi_po_poligon_measure_08.09.md` §7). Поправка „1 по 1" не може да конвергира, защото кадастралните зони и OSM възлите системно се разминават с полигоналната система.

  ## 1 · Видове несъгласия

  **(а) Грешка на думата (OSM nearest_point на далечни метри).** nearest_point low: 10 799 клъстера, от тях 3 649 извън всеки полигон и 2 623 несъгласни — 58 % непотвърдени. flagged: 1 419, съгласие 16 %. Примери от `bridge_sample_1500.json`: „кв. Левски, ул. Топра Хисар №22" — дума Левски от възел на 808 m, low, margin 1.04, втори кандидат Цветен квартал; „м-т Сотира" от 797 m, втори кандидат кв. Изгрев; flagged екстремум: „с.о. Ален Мак" от възел на 4 116 m. Плюс каноничния §7 случай: Студентска бл. 11 → „кв. Чайка" от 707 m.

  **(б) Разлика в системите от имена.** KAIS (кадастър) е несъгласен в 8 214 от 25 550 (32 %) — не защото е грешен, а защото „зона" ≠ „квартал": ГАЛАТА 1 397 (Боровец-юг 1 293 + Фичоза 54 + Зеленика 50), ВИНИЦА 503+ (Манастирски рид 238, Акчелар 224, Перчемлията 41), Траката 736, 8 микрорайон 675, Цветен квартал 458, 4-ти микрорайон 58. Това е преводимост на речници, не локация.

  **(в) Въпрос към полигона.** ж.к. БРИЗ → м-т Свети Никола 560 (думата Бриз седи върху чужд полигон — или Свети Никола е разширен върху Бриз, или обратното); кв. Розова долина → кв. Аспарухово 771 (и двата полигона са подписани — или Аспарухово гълта Розова долина, или липсва parent); ж.к. Дружба → кв. Аспарухово 119 (parent съществува, но точките не попадат в Дружба); Гръцката махала → Център 152; с.о. Ален Мак → Златни пясъци 128 / к.к. Чайка 64. Това е борд-решение, не автоматика.

  ## 2 · Кога nearest_point е бил надежден

  От извадката правилото за увереност се вижда чисто: high = dist < 400 m и margin ≥ 1.5 (медиана 235 m, margin 3.0); medium = dist < 600 и margin ≥ ~1.2 (медиана 470 m, margin 1.51); low = останалите до ~1 200 m (медиана 706 m, margin 1.18); flagged = над 1 200 m (медиана 1 521 m, до 4 116 m). Съгласие по клас: high 73,5 % (15,6 % несъгласни), medium 61 % (25 %), low 37 % (24 %, плюс 34 % извън), flagged 16 %. Още по-лошо: дялът на „съгласието" само в 100-метровата лента по ръба расте с несигурността — high 32 %, medium 47 %, low 56 %, flagged 71 % — тоест „съгласията" при low/flagged са до голяма степен ръбови съвпадения, не потвърждение. **Праг като СВИДЕТЕЛ: само high (dist < 400 m и margin ≥ 1.5). Medium — граничен, low/flagged — дори не свидетел за думата, само метрики в леджера. Като канон: 0 завинаги.**

  ## 3 · Решенията за 9 255 извън и 2 483 припокриване

  От извън-полигон 3 649 са low nearest_point — там проблемът е покритие, не дума. Липсващи полигони/дупки: Цветен квартал (197 извън + 458 върху Левски), ж.к. Владислав Варненчик (162 върху Владиславово), 8 810 без дума с центроид в центъра — Център и Левски имат по 753/478 извън собствените си полигони (полигонът е тесен или с дупки). Липсващи/висящи родства в `polygons_props_no_geometry.json`: `borovets_sever`/`borovets_yug` имат parent `borovets`, който **не съществува** като полигон (висяща връзка); `mladost1` има parent `mladost`, но `mladost2` няма — непоследователно; `vazrazhdane1`/`vazrazhdane2` без parent, докато Възраждане 3/4 ги няма като родител. Розова долина и Дружба трябва да получат parent Аспарухово или границите да се разминат. **Всички 59 ръчни полигона са precision_m 100** (само mladost2 е 50, метод street_bounded_face) — единното 100 означава, че лентата max(50, precision) е навсякъде 100 m и прецизността не носи информация; Петър трябва да реши реална прецизност по полигон, иначе 14 005 + 8 311 ръбови случая остават неразличими.

  ## 4 · „Гейтът веднъж завинаги"

  При всеки билд, от едни и същи входове — детерминистично:

  - **канон = само най-малък съдържащ подписан полигон; дял nearest_point като канон = 0 → ако > 0, билдът спира** (твърд праг);
  - брой неопределени (извън полигон) — падащо число; **всяко увеличение спрямо базовата линия спира билда**;
  - припокривания, нерешени от правилото parent/най-малък = 0;
  - съгласие по извор (kais / osm-свидетел) — отчетно число, растящо, но не блокиращо (свидетел, не канон);
  - **дублиран етикет (квартал + бл. без улица) = 0 → спира билда** (случаят Чайка бл. 11);
  - нови думи извън речника на полигоните → списък за преглед, не тихо приемане.

  ## 5 · Изкривявания на самата мярка

  - **Токенното съгласие е двусмислено:** „Чайка" е токен и на `chaika_kv`, и на `chaika_kk` — съгласие може да се отчете към грешния полигон; същото „Боровец" срещу Боровец-север/юг.
  - **28 % несъгласие ≠ 28 % грешна локация:** „8 микрорайон" няма токен в нито един полигон — винаги „несъгласен", дори когато е на правилното място. Мярката бърка „непреводимо име" с „грешно място".
  - **Най-малкият съдържащ полигон** предполага, че влагането е умишлено; при припокриване от неточни граници избира по-малкия дори когато е грешен (случаи Розова долина/Дружба/ЗПЗ).
  - **Лентата е беззъба:** при precision 100 навсякъде „в лентата" не разделя качествени от слаби полигони, а 14 005 лентови съгласия влизат в главното 53 % — числото е завишено.
  - **Циркуларност:** за OSM редовете думата и оценката идват от същия мост — мярката проверява вътрешна консистентност, не истина. И 15 % „извън" е отчасти липса на покритие, не грешка на думата.

  Извод: поправката не е „разреши 16 869 спора", а три решения на борда (речник кадастър→квартали, полигонални граници/родства, гейт по канон) — след това споровете изчезват клас по клас, не един по един.

To resume this session: kimi -r session_daf8a641-7737-4595-86a5-50d4126ae9ea
