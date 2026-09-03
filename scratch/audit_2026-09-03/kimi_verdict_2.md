# Кими · атака върху ПРЕПОРЪКИ v1 + кандидатите (03.09.2026; git.kimi.log ред 4390)

Прочети изцяло Fire_Varna/scratch/audit_2026-09-03/kimi_brief_2.md и изпълни задачата в него: атака върху данните на препоръките v1 по десетте въпроса, само четене, отговор на български в таблици.
──────────── ОТГОВОР НА KIMI ────────────
kimi version 0.34.0
Read the brief file first.I need to read many files. Let me read them all. Start with the audit folder files and the kais_func summaries.

Прочитам всички посочени файлове, след което отговарям по десетте въпроса.

Now read the kais_func summaries and sources.Now read the sources: kimi_obrazovanie.txt, sol_lechebni.txt, places.json, hotels.json, quarter_registry.json. These may be large. Let me check sizes and read selectively. The brief says read them as sources. I need mainly to verify claims: register rows for Vladislavovo, ДЯ addresses, private schools, hospitals, МК Младост rows, etc. Much is already quoted in the summaries. Let me check file sizes and read relevant portions.  1308 varna_3d/scratch/refactor/_addr/kimi_obrazovanie.txt
 717 varna_3d/scratch/refactor/_addr/sol_lechebni.txt
1219 Varna_buildings/config/quarter_registry.json
3244 total
---
-rw-r--r-- 1 Petar 197121 78491 Sep  3 11:20 Fire_Varna/data/hotels.json
-rw-r--r-- 1 Petar 197121 61170 Sep  3 11:20 Fire_Varna/data/places.json
Wait, hotels.json only 78KB for 226 hotels? Possible. places.json 61KB for 135 places.

Read kimi_obrazovanie.txt (1308 lines, 2 reads), sol_lechebni.txt (717 lines, 1 read). places.json and hotels.json — I'll grep for relevant entries rather than read fully. quarter_registry.json — read relevant parts (vladislavovo entry).The file is large. I need the register contents. Read via output_path pagination. Read the saved file at specific line offsets. Let me read the full file from the output path, lines ~380-720 and 1100-1308.I have the DG and ясли lists. Now I need the schools list, ЦПЛР, and private schools (lines 1117-1200 in the original file, which is ~945 lines in the dump because of truncation? The output file has 945 lines displayed but the tool said "Total lines in file: 1308" for the original; the output_path file has 945 lines — wait, "Total lines in file: 945" for the dump? The status said "Total lines in file: 1308" for the source, and the output_path shows 945 lines because lines were truncated but each line still present. Actually output_size 85KB but total file 1308 lines — the preview said "945 lines read ... Max 1000 lines reached". Hmm, the dump file might have all 1308 lines. The Read at offset 380 said "Total lines in file: 945"? No — it said "340 lines read from line 380. Total lines in file: 945." Wait, that's odd: output_size_chars 85144 vs original 102KB — truncated lines replaced? Anyway the dump has 945 lines. Original file has 1308 lines. So the dump dropped some content? The dump maps original lines? It showed line numbers doubled ("380\t380\t...") — the dump preserves original content with its own numbering. Total 945 in dump vs 1308 original — meaning the dump is itself truncated? No, the dump is the full tool output, which was capped... Actually the tool output preview was the first ~1000 lines; the output_path contains full output of the Read tool, which was itself limited to 1000 lines/100KB. The original file is 1308 lines; Read showed "945 lines read... Max 1000 lines reached" — hmm, 945 < 1000, probably byte cap hit at line 945. So lines 946-1308 of the original weren't in the dump.

I need lines 1100-1308 of the original (schools table, ЦПЛР, conclusions). Read the original file directly at offset 946+.Now sol_lechebni.txt (717 lines). Read it — may exceed 50KB. Let me read directly; if too big, page.Now the remaining sources: places.json, hotels.json, quarter_registry.json. I should verify key claims: Кардиолайф pin in places.json, Аджибадем/Майчин дом entries, 25 delivered places without register row, private schools delivered (3: Екзюпери, Монтесори, Първа частна търговска гимназия/Конто Трейд), universities, Военно-морска болница, ДГ12/Ян Бибиян rows, ОДЗ Чайка, 20 Логопедична, Жирафче etc. Let me grep places.json.

Сега изворите-доставки: places.json, hotels.json, quarter_registry.json.

Continue reading places.json from 1000 to end (1905 lines). Also need hotels.json (partial) and quarter_registry.json relevant part. Let me set a todo list mentally — this is a long analysis; a todo list could help but it's mostly reading + answering. I'll just continue.I now have the full places.json. Note key facts:

- Кардиолайф pin: 43.213541, 27.91808 — exactly same coords as СБАЛК „Специализирана болница за активно лечение по кардиология Варна" ЕАД (43.213541, 27.91808) — 0.0 m, zone кв. Чайка. Wait — v1 says Кардиолайф is 3 748 m from its register address (МЦ Младост, бул. Република) and lies on СБАЛК at 0.0 m. places.json confirms: Кардиолайф lat/lon = 43.213541, 27.91808, same as СБАЛК. Its register address is бул. Република, МЦ Младост, бл. А. ✓ Consistent.

- Аджибадем: kind болница, src OSM, м-т Шашкъна 43.217378, 27.916067. Register: ИАМН row 56 = МЦ. ✓
- Майчин дом: kind болница, src OSM; register row 43 МЦ, ул. Мир 1. ✓
- Военно-морска болница: src OSM, no register row (not in МЗ/ИАМН civilian register). ✓
- Universities: 7, all src OSM. ✓
- Private schools delivered: ЧСУ Монтесори Варна (register src), Частна профилирана гимназия "Антонан дьо Сент-Екзюпери" (OSM, with typo „Антонан"), Първа частна търговска гимназия (OSM). Also ЧОУ „Феникс 2020" (OSM) — that's a delivered school without register row! Interesting for Q8. Also „бивше ОУ Д-р Никола Димитров" status бивш. „3 ОУ Ангел Кънчев", „8 СОУПЧЕ", „ОУ Г.С.Раковски", „ОУ Христо Ботев" etc.

Wait — register has III ОУ „Ангел Кънчев" ул. Роза 23 — delivered „3 ОУ Ангел Кънчев" at кв. Изгрев 43.224764, 27.91491. Is that the register row? summary_регистри §6 lists „3 ОУ Ангел Кънчев" among the 25 delivered without register row... probably because geocode of register row is far. Note.

- „ОУ Христо Ботев" delivered at кв. Аспарухово — register №25 ОУ „Христо Ботев" кв. Аспарухово ✓ so it has a register twin but is listed as no-register-row (probably due to name mismatch/geocode).

- ЦПЛР: excluded section has „ЦПЛР – Средношколско общежитие „Михаил Колони"" kind училище, src МОН register, why: общежитие не училище — въпреки регистровия двойник. So currently excluded; решение 12 makes it a new kind „общежитие".

- ДГ12 „Ян Бибиян" register address ул. Дойран 9; delivered „3 ЦДГ Ян Бибиян" at 43.217812, 27.920193, кв. Изгрев, OSM. summary_парцели says „Ян Бибиян" OSM POI at 43.216013, 27.914677 = parcel #55, addr ул. ДОЙРАН 9 — that's the ДГ12 spot. Wait, but places.json „3 ЦДГ Ян Бибиян" is at 43.217812, 27.920193 — different location (~500 m away). Hmm, v1 §11 says „3 ЦДГ Ян Бибиян" lies at 1.4 m from a body „детско заведение" (ул. Добруджа 3). So the delivered pin at 27.920193 is near Добруджа 3, which is a different institution (old ДГ3? „13 ЦДГ Звездичка" is ДГ3 at 27.910455... hmm). Actually per judges: „3 ЦДГ Ян Бибиян" carries a wrong number — it's a different заведение. The parcel at Дойран 9 (783 m², 1 body) has OSM POI „Ян Бибиян" (excluded) — matches ДГ12 register address. So new row ДГ№12 on Дойран 9 is confirmed by register address + КАИС addr + excluded OSM POI name. Good.

- ДГ16 „Слънчева дъга" register ул. Уйлям Гладстон 5; delivered? places.json excluded: „Слънчева дъга" OSM К4 точка без сграда. Parcel #59 „Слънчева дъга" OSM POI (excluded) at 43.218435, 27.921554, addr ГЛАДСТОН. So ДГ16 → free parcel „Гладстон" — confirmed by OSM excluded name + register address street.

- „4 ОДЗ Чайка" at 43.217222, 27.934486 кв. Чайка OSM — 3.9 m from детско заведение body. Register ДГ18 „Чайка" до бл. 3 and ДГ21 „Калина Малина" до бл. 40 both geocode to parcel at 43.21764, 27.93840 (1471 m²). „4 ОДЗ Чайка" is ~370 m from that. So ДГ18/21 share one spot per register geocoding; the ОДЗ Чайка pin is a different body. v1 §11 says „Ян Бибиян и 4 ОДЗ Чайка НЕ се местят" — because they're different заведения per КАИС func. Hmm wait — 4 ОДЗ Чайка at 27.934486; parcel 43.21764, 27.93840 is ~350 m east. And there's also „Калина Малина" excluded (точка без сграда). OK.

Now hotels.json and quarter_registry.json. I mainly need: hotel channel facts (226, 213 УИН, 5 hotels with 382 beds + Спортпалас for decision 13, the 12-hotel strip 43.2733–43.2780, ГРАДИНА two УИН, Явор/Голдън Лайн). quarter_registry: vladislavovo alias, kaisieva parents. Grep both.Hotels.json seems larger than 78KB? The grep shows line 4393 — so hotels.json is ~4400+ lines but 78KB? That can't be — 78KB/4400 lines ≈ 18 bytes/line. Possible with short lines. OK.

I need a few more facts from hotels.json: ГРАДИНА two УИНs (line ~715-730), Спортпалас (excluded, 151 beds), the 5 hotels 382 beds claim for decision 13, the strip 12 hotels. Let me read the ГРАДИНА entry and the excluded section header, and check meta. Also decision 13: „5-те хотела с 382 легла + Спортпалас през хотелския канал" — which 5? Probably from the audit. Let me read hotels.json head (_meta + excluded) and the ГРАДИНА entry fully.Good. Now I have nearly everything. A few more checks:

1. Decision 13: „5-те хотела с 382 легла + Спортпалас през хотелския канал" — the 5 hotels without... this refers to some audit finding about 5 hotels missing with 382 beds. I don't have the audit file docs/audits/ОДИТ_03.09_система.md in the brief's read list... Actually the brief says read ПРЕПОРЪКИ, judges_summary, kimi_verdict, three kais_func summaries, and sources. The audit file wasn't required. I can answer based on data: Спортпалас excluded with УИН and 151 beds; the 5 hotels 382 beds — I can't verify which 5 from these files directly, but I can note. Actually let me check the judges_summary remainder (I read only first ~10 lines of preview). Let me page through judges_summary.txt fully — 221 lines, 90KB. I got the preview only (first 10 lines). Need the rest, especially the „цялост на данните" lens. Let me read from the output_path.

Остава да дочета `judges_summary.txt` (221 реда) — взимам го на части от записания изход.

Continue reading judges_summary from line 130 to 221.I have now read all required material. I still need some verification for specific questions:

Q3: 24 missing with unambiguous body (summary_регистри §4) — I have the full table. Confirm row-by-row: ДГ 11 rows (6, 11, 12, 18, 19, 21, 22, 25, 34, 41, 53), ясли 1 (ДЯ6), частни ДГ 3 (Малкият принц, Монтесори, Мелита), училища 4 (Иван Вазов, Св. Климент Охридски, ПГЕ, ПГТМД), болници/ДКЦ/хосписи 5 (Лисичкова, ДКЦ Младост-М, хосписи Надежда/Медицинска грижа/Мария Магдалена). Total 11+1+3+4+5=24. ✓

Checks to make:
- ДГ18/21 на едно място — summary says both geocode to same parcel 43.21764, 27.93840 (Чайка). Register: ДГ18 до бл. 3, ДГ21 до бл. 40 — different blocks but geocoder returns almost same point. The brief asks потвърди/отхвърли. Note: summary_парцели §12 lists ДГ№21 „Калина Малина" 43.7 m → parcel 63 (1471 m², 7 bodies, ж.к. ЧАЙКА №98) and ДГ18 at 48 m same parcel. Hmm — actually in §4 summary_регистри ДГ№18 at 48 m and №21 at 51 m to same place. But note parcel #63 was also candidate named „Калина Малина" via excluded OSM POI (1.6 m). So ДГ18's assignment to the same parcel is weaker: register says ДГ18 до бл. 3, parcel is ж.к. ЧАЙКА №98... The OSM name on the parcel is „Калина Малина" (= ДГ21's name). So actually evidence favors: parcel = ДГ21 Калина Малина; ДГ18 Чайка is elsewhere (possibly where „4 ОДЗ Чайка" sits — 3.9 m from a детско заведение body!). Indeed: „4 ОДЗ Чайка" delivered at 43.217222, 27.934486 — 3.9 m from a ДЗ body. Old numbering: ОДЗ 4 → maybe ДГ18? Hmm, register ДГ18 „Чайка" до бл. 3. The v1 decision 11 says „4 ОДЗ Чайка НЕ се мести" (it's a different заведение). But summary_регистри §4 assigns ДГ18 AND ДГ21 both to parcel at 43.21764/27.93840, marked ⚠ same place. My data verdict: ДГ21 confirmed by OSM name (Калина Малина excluded POI at 1.6 m on parcel 63 — same coords 43.217674, 27.938428). ДГ18's body assignment is not provable — and there is a competing candidate: the body under „4 ОДЗ Чайка" (3.9 m). So for Q3: ДГ18/ДГ21 на едно място — отхвърлям като „еднозначно"; ДГ21 → парцел 63 (име от OSM), ДГ18 → неразрешено (двама кандидата: тялото на ОДЗ Чайка и парцел 63).

- ОУ Иван Вазов/ПГЕ на един адрес — register confirms ул. Върба 24 for both (rows 12 and 48). Both missing, one parcel 2147 m². Two institutions, one address — either shared site declared or one parcel with 2 rows. Data: confirm as shared-address, needs declared обща площадка (like МК Младост) — 2 rows on one pin only with declaration.

- МК Младост 5 rows on one building бул. Република 91/15 — summary §4: 5 rows (Лисичкова №91 + ДКЦ Младост-М №15 + 3 хосписа №15) all geocode to same КАИС place 43.23086, 27.87875, 6 bodies, КАИС addr бул. Република 91. Plus Царица Елеонора without street. And Кардиолайф бл. А. Interesting: КАИС address is „бул. Република 91" — the same number as Лисичкова. So the complex's КАИС address is №91, while most register rows say №15. Note: kimi_verdict said 6 rows with №15 + 6 more without number = 12; Лисичкова №91. Data-wise: confirmed one КАИС place (3096 m², 7 et, private) — one pin, N rows only as declared shared site.

- ЧДГ Мелита върху двора на ДГ6 — summary: Мелита ул. Тодор Влайков бл. 7 → same parcel as ДГ6 (Тодор Влайков 71), 706 m², геокод улица 34 m. Register ЧДГ Мелита = „ул. Тодор Влайков бл.7" (detskitegradini 2022, secondary source!). Note this is from the 2022 secondary source — weak. And it's the same yard as ДГ6 Палечко. Verdict: suspicious — block 7 vs №71; Улица-level geocode (негоден за присъда per §7.2). Should be board, not auto-included.

Q4: Решение 11 new form. Check data:
- „3 ЦДГ Ян Бибиян" at 43.217812, 27.920193 — 1.4 m from ДЗ body with addr ул. Добруджа 3. Register ДГ12 Ян Бибиян ул. Дойран 9. So the OSM pin „3 ЦДГ Ян Бибиян" sits on a different ДЗ body. Two different заведения claim: parcel #55 „Ян Бибиян" excluded OSM POI at 43.216013, 27.914677, addr ул. ДОЙРАН 9 — matches register ДГ12! Wait — the excluded OSM POI „Ян Бибиян" IS at Дойран 9. So there are two OSM records: delivered „3 ЦДГ Ян Бибиян" (Добруджа 3 area) and excluded „Ян Бибиян" (Дойран 9). The excluded one's why: „К4: без тип и номер — условно, за борда". So ДГ№12 new row on Дойран 9: register address + КАИС parcel 783 m² with func ДЗ + OSM name Ян Бибиян on it (excluded, 0.0 m). Strong. ✓
- ДГ16 „Слънчева дъга" ул. Гладстон 5: parcel #59 „Слънчева дъга" excluded OSM POI at 4.9 m, addr ГЛАДСТОН, 624 m². ✓ Confirmed by name+street.
- Ян Бибиян/4 ОДЗ Чайка не се местят: „4 ОДЗ Чайка" 3.9 m from ДЗ body in ж.к. Чайка — it is a real ДЗ body; but which institution? Register ДГ18 „Чайка" до бл. 3! Hmm — this cuts against v1: „4 ОДЗ Чайка" might actually BE ДГ18 „Чайка" (old numbering ОДЗ 4?). v1 treats it as „неразрешена OSM самоличност (носи чужд номер)" for the board. Similarly „3 ЦДГ Ян Бибиян" on Добруджа 3 — no register row at Добруджа 3... Actually is there? Register list: nothing on Добруджа. So „3 ЦДГ Ян Бибиян" location has no register counterpart → board. OK, consistent with v1: not moved, go to board. But note the alternative: ОДЗ Чайка could be ДГ18's true location — which would contradict assigning ДГ18 to parcel 63 with ДГ21. Data: the parcel-63 assignment of ДГ18 is geocode-only (block centroid); the „4 ОДЗ Чайка" body is a live alternative. So v1's decision 11 (ДГ18 stays... wait does v1 place ДГ18? v1 §11 mentions only Ян Бибиян/ОДЗ Чайка not moved, ДГ12 new row, ДГ16 Гладстон. ДГ18 is in the 24-row list (§4). Hmm, Q4 asks only about the listed items.

Data check on „4 ОДЗ Чайка" distance: judges say 3.9 m from ДЗ body in ж.к. Чайка. Delivered at 43.217222, 27.934486. Parcel 63 (ДГ21/18) at 43.21764, 27.93840 — distance ~330 m. So they're distinct places. OK.

Q5: ясли as class. Register: 12 ясли (Я1). Delivered in places.json as kind „детска градина": ДЯ №11 Иглика, ДЯ №13 Русалка, ДЯ №14 Звънче, ДЯ №4 Приказен свят (register src), plus OSM ones: „9. Детска ясла Детелина", „Детска Ясла №2 Моряче", „Детска ясла № 7 Роза", „Детска ясла (ДЯ) №3 Зайо Байо". That's 8 of 12. Missing: ДЯ1 Щастливо детство (ул. Славянска 21), ДЯ5 Чуден свят (Димитър Полянов 3), ДЯ6 Мечо Пух (Ниш 29), ДЯ8 Щурче (Евлоги Георгиев 28/228). ✓ matches claim ДЯ 1/5/6/8 missing. Note summary_регистри §3 says ясли: 12 rows, 9 delivered, 1 missing-unambiguous, 1 без тяло, 1 негеокодируем... Wait: §3 says детски ясли 12 | доставени 9 | ЛИПСВА еднозначно 1 | спорно 0 | без тяло 1 | негеокод 1. Delivered 9? places.json shows 8 ясли... Hmm: ДЯ2, ДЯ3, ДЯ4, ДЯ7, ДЯ9, ДЯ11, ДЯ13, ДЯ14 = 8. What's the 9th? Maybe ДГ6's яслена група or „1 ЦДГ"? Or summary counts differently (delivered place ≤60m not held by others — e.g., ДЯ1 Щастливо детство could be near some delivered place). Actually „доставено" in §3 = same name OR ≤60m unclaimed. So ДЯ1 may be ≤60 m from a delivered place. Missing with unambiguous body: ДЯ6 (1). без тяло: ДЯ8. негеокодируем: ДЯ5 (resolved later via address text: ул. ДИМИТЬР ПОЛЯНОВ 5). Hmm §5 lists ДЯ5 „Чуден свят" as негеокодируем but resolved via addr text, and ДЯ8 „Щурче" as без тяло.

Note discrepancy: brief says „ДЯ №1/5/6/8 липсващи". §3 says 9 delivered (incl. by proximity), 3 missing (6, 8, 5). The brief's „липсващи" comes from kimi_verdict §14 (4 missing: ДЯ1, 5, 6, 8) — by name. Both consistent: ДЯ1 missing by name but has a place ≤60m? Actually careful — ДЯ1 Щастливо детство ул. Славянска 21; there is excluded OSM „Щастливо детсво" (typo, К4 частна ДГ без номер — профил на домашен адрес). Hmm, that excluded row could be at Славянска 21? Unknown. I'll note: by name 4 missing; by the measure's „доставено" definition 3.

ДЯ8 address contradiction: register Евлоги Георгиев 28 vs varna.bg/2214 №228 — confirmed in kimi_obrazovanie.txt:1270 and :1052. ✓

Q6: Решение 12: 7 общински + 8 частни училища. Register: 69 schools = 45 общински + 12 държавни + 12 частни. Delivered училище: 60. Register table §3: училища 69 rows, доставени 50, ЛИПСВА еднозначно 4, спорно 1, без тяло 9, села 2, негеокод 3. Hmm 4+1+9+2+3 = 19 missing; 50+19=69 ✓. „7 общински" missing? Which 7: from §4 училища 4 (Иван Вазов[общ], Св. Климент Охридски[общ], ПГЕ[държ], ПГТМД[държ]) + спорно 1 (ЧОУ Демократично — частно) + без тяло 9 + села 2 + негеокод 3. v1 says „7 общински + 8 частни". Where does 7 общински come from? Not directly visible in the summaries. Hmm. Let me think: maybe from the audit §7 decision 12 — „7 общински + 9 частни". Judges corrected to 8 частни (Талант out). The 7 общински — possibly: ОУ Иван Вазов, СУ Св. Климент Охридски, I ОУ Борис, ОУ Стоян Михайловски, ОУ Раковски, ГПЧЕ, IV ЕГ? From §5: без тяло include I ОУ „Св. княз Борис І", ОУ „Стоян Михайловски" (м.р. addresses), ОУ „Г. С. Раковски" and ГПЧЕ „Йоан Екзарх" (кв. Чайка only). Негеокодируеми: IV ЕГ (сп. Почивка), ЧОУ Монтесори Варна (ул. липсва), ЧОУ Талант. Села 2: Добри Войников, Христо Смирненски (and ОУ Св. Климент Охридски Константиново — that's 3 schools in villages actually; kimi_obrazovanie says 3: Каменар, Константиново, Тополи. But §3 says села 2 — hmm, and СУ „Свети Климент Охридски" ул. Михаил Колони 10 is a DIFFERENT school (№35, city) vs ОУ „Св. Климент Охридски" (№19, Константиново). OK.)

So missing schools by class: общински missing = 19 total missing − частни (which are: ЧОУ Демократично [спорно], ЧОУ Монтесори Варна [негеокод], ЧОУ Талант [негеокод], plus in §4: ЧПГ по инженеринг [№68? no that's ЧПГ — wait §4 училища lists only 4: Иван Вазов, Св.Климент Охридски СУ, ПГЕ, ПГТМД. Where are ЧСУ Мечтатели and ЧПГ инженеринг? kimi_verdict said Мечтатели (рег 64) and ЧПГ инженеринг (рег 68) have unambiguous КАИС spots. §12 of summary_парцели lists ЧПГ по инженеринг (86.2 m → parcel 51) and ЧОУ Демократично (87.6 m → parcel 69). But summary_регистри §4 училища — only 4 rows. Hmm, and ЧСУ Мечтатели — not in §4? §5 спорно includes ЧОУ „Демократично образование Варна". Where's Мечтатели? Not mentioned in §4/§5 — maybe counted among доставени by proximity (ул. Евлоги Георгиев 24 near delivered?). Unclear.

Counting „7 общински": без тяло 9 (which classes?) + ... I can't fully re-derive 7 from the summaries. The v1 claim: 7 общински + 8 частни = 15 new schools. Data: 19 missing register rows total (incl. 2 села, Талант, etc.). 8 частни = 11 действащи − 3 покрити ✓ (Мечтатели, Демократично, Монтесори Варна ЧОУ, Аз съм българче, Малкият принц, Прогресивно 2, Джордж Байрон, + ЧПГ инженеринг = 8? Let's count: 12 listed − Талант = 11 действащи; covered 3 (Екзюпери, ЧСУ Монтесори, Конто Трейд) → missing 8: Монтесори Варна ЧОУ (58), Малкият принц (59), Прогресивно (60), Демократично (61), Аз съм българче (63), Мечтатели (64), Джордж Байрон (66), ЧПГ инженеринг (68). ✓ = 8. Good, v1's „8 частни" checks out.

7 общински: 45 общински − 2 села (Добри Войников Каменар, Христо Смирненски Тополи are общински; Св.Климент Охридски ОУ Константиново also общинско → 3 села общински!). Hmm §3 села 2 for училища. kimi says 3 schools in villages. Discrepancy to note. Missing общински candidates: Иван Вазов (12), СУ Св. Климент Охридски (35), Борис I (2), Стоян Михайловски (24), Раковски (8), ГПЧЕ (41), IV ЕГ (40)... that's 7! Иван Вазов, Св. Климент Охридски (СУ, city), I ОУ Борис, ОУ Стоян Михайловски, ОУ Раковски, ГПЧЕ Йоан Екзарх, IV ЕГ Жолио-Кюри = 7 общински. And държавни missing: ПГЕ (48), ПГТМД (51) = 2 (both in §4). Hmm but v1 says „7 общински + 8 частни" — excludes the 2 държавни (ПГЕ, ПГТМД)? ПГТМД is handled in decision 10 (pin fixes). ПГЕ — on Върба 24 shared with Иван Вазов. So maybe counted within решение 10/общ адрес. I'll note: data support 7 общински + 8 частни + 2 държавни (ПГЕ, ПГТМД) + села = the full missing set; v1's „7+8" is consistent if ПГЕ/ПГТМД are counted elsewhere (ПГТМД in решение 10, ПГЕ shares Върба 24 with Иван Вазов).

Михаил Колони общежитие as new kind: register ЦПЛР row 73, бул. Цар Освободител 150; excluded today with „общежитие, не училище — въпреки регистровия двойник"; КАИС has func „Общежитие" (46 bodies); parcel #29 общежитие named „ЦПЛР – Средношколско общежитие „Михаил Колони"" via excluded OSM POI at 6.0 m, addr бул. цар ОСВОБОДИТЕЛ 0 · ул. ДОЙРАН 17 · 19. Interesting: the КАИС parcel address is NOT Цар Освободител 150 — geocode trap confirmed (the 2225 m scatter key). Data supports new kind + manual pin. ✓

Q7: Decisions 7/9. Аджибадем (ИАМН 56 МЦ) and Майчин дом (ИАМН 43 МЦ) both delivered as „болница", src OSM. Register confirms both are МЦ. ✓ removal correct. Note: Майчин дом register address ул. Мир 1; delivered pin at 43.220199, 27.9265 кв. Изгрев — fine. Аджибадем lies on жилищна сграда (0.0 m) per summary_правило §3 Г2-ГРЕШКА? No wait, Аджибадем at ok_d... In §8 of summary_парцели: Аджибадем болница on Жилищна многофамилна 0.0 m. Judges: „картата губи Аджибадем (чийто пин лежи върху жилищна сграда)". So removal loses a place that has спешно per OSM — v1 says new class if wanted. Data verdict: ДА.

Кардиолайф: register МЗ row 7 СБАЛ, бул. Република МЦ Младост бл. А. Delivered pin = exact same coords as СБАЛК Варна (Цар Освободител 100). 3748 m. Гасене + полагане на МК Младост ✓. Note: both from ИАМН export (register-born duplicate) — гейт 4 при експорта. ✓

МК Младост = declared site with N rows: 5 rows geocode to same КАИС place + Царица Елеонора (no street) + Кардиолайф (бл. А) + Кехайови (МК Младост ет.2), Терапия 2007 (корпус В), АКЕРР (тяло А), Давидков (ж.к. Младост бул. Република ет.2)... kimi_verdict: 6 on №15 + 6 more in complex = 12; Лисичкова on №91 — and КАИС addr of the place is бул. Република 91! So №15 and №91 might be the same complex with two numbers. v1 says „МК Младост = декларирана площадка с N реда". Data: ✓ but N is ambiguous: 5 with unambiguous body, up to 12 register rows (incl. МЦ which are out of scope), 6 non-МЦ on №15 (ДКЦ Младост-М, хосписи Надежда/Медицинска грижа/Мария Магдалена + Св. Стилиян-Младост МЦ + МЦ Младост Варна)... For in-scope kinds (болница/ДКЦ/хоспис): Лисичкова (болница), ДКЦ Младост-М, 4 хосписа (Надежда, Медицинска грижа, Мария Магдалена, Царица Елеонора), Кардиолайф (болница) = 7 rows. v1's „N реда" should be pinned: 5–7 depending on whether Царица Елеонора (no street) and Кардиолайф counted. Note for verdict.

Q8: 25 delivered without register row (§6). From the summary:
- училище 14: OSM duplicates/old numbering — ПГТМД two pins, 3 ОУ Ангел Кънчев, ОУ Г.С.Раковски, бивше ОУ Д-р Никола Димитров (status бивш), ПГ ИТOK Екзюпери & Френско училище without КАИС body in 80 m. 
- болница 5: Аджибадем (no КАИС здравно body in 80m), Военно-морска, Майчин дом, Онкологична-Марко Антонов, +? (5 listed: those 4 named... „5" — likely also Eurohospital? places.json has „Eurohospital" src OSM — register МЗ row 2 Еврохоспитал! So Eurohospital HAS a register twin by legal name. Hmm §6 says 5 болница: Аджибадем, Военно-морска, Майчин дом, Онкологична Марко Антонов — that's 4 named. Eurohospital = register row 2 (МБАЛ Еврохоспитал, кв. Виница, ул. Найден Райков 2а). Delivered Eurohospital at 43.240808, 27.981249 кв. Виница ✓ matches. So it may count as delivered-without-row due to name mismatch. 

Which are legitimate? Частни: ЧОУ Феникс 2020 (delivered, OSM, Приморски — not in the 12-list! suspicious — not in register at all), Първа частна търговска гимназия (= Конто Трейд reg 69, per kimi_verdict ≈ by position 5m), Екзюпери (reg 67 covered but with typo „Антонан"), ЧСУ Монтесори (has src register actually — so not in the 25). Universities 1: Медицински университет (no university register in scope — legitimate, universities have no register; all 7 universities are src OSM). Военно-морска болница — outside civilian register — legitimate (MoD hospital, real). 

Suspicious: „ЧОУ Феникс 2020" — private school name not in the register list of 12. „8 СОУПЧЕ" (Спортно училище? actually 8 СОУПЧЕ = средно общообразователно училище с природо...? It's OSM; register №55 is СУ Георги Бенковски спортно ул. Рупи 1; 8 СОУПЧЕ at Морска градина... hmm „СОУПЧЕ" = училище с преподаване на чужд език? There's СУЕО Пушкин. 8 СОУПЧЕ — not in register → suspicious). „ОУ Христо Ботев" — register №25 exists (Аспарухово) → has twin, just name mismatch. „ДГ-4 Теменужка Филиал 1" — register ДГ4 Теменужка ул. Шейново 18 — филиал not in register → suspicious-ish. „ЦДГ Пушкин (филиал)" — ДГ7 Пушкин's second row (корира 35 уникални номера). „20 Логопедична ЦДГ" — no КАИС body in 80 m, on „Друг вид сграда за обитаване" 400 m from true body — suspicious (kimi_verdict: covered „по положение"). „4 ОДЗ Чайка", „Детска градина Жирафче" (not in register — suspicious, maybe private unregistered), „3 ЦДГ Ян Бибиян" (wrong number — board per v1).

I have enough to classify. The §6 list says 25: 14 училище + 5 болница + 3 ДГ + 2 ДКЦ + 1 университет. Let me enumerate училище 14 from places.json by excluding src-register rows: OSM-src училища: 3 ОУ Ангел Кънчев, 8 СОУПЧЕ, бивше ОУ Д-р Никола Димитров, Екзюпери (typo), ЧОУ Феникс 2020, I ЕГ, Математическа гимназия Берон, Международното Френско училище, Морска гимназия, НУИ Добри Христов, НУ Васил Левски, ОУ Черноризец Храбър, ОУ Добри Чинтулов, ОУ Г.С.Раковски, ОУ Христо Ботев, ОУ Йордан Йовков, ОУ Капитан Петко Войвода, ОУ Арабаджиев (OSM one), ОУ Отец Паисий, ОУ П.Р.Славейков, ОУ Панайот Волов, ОУ Патриарх Евтимий, ОУ Стефан Караджа, ОУ Стоян Михайловски, ОУ Св.св. Кирил и Методий, ОУ Цар Симеон I, ОУ Васил Априлов, ОУ Васил Друмев, ОУ Захари Стоянов, Първа частна търговска гимназия, ПГ ИТOK Екзюпери, ПГКМКС Сендов, ПГ Кольо Фичето, ПГСАГ Васил Левски, ПГ текстил Вилите, ПГе electrotexnika, ПГХХВТ Менделеев, ПГТМД Чайка, ПТГ, Спортно Бенковски, СУ Елин Пелин, СУ Гео Милев, СУУНЗ Шишманов... that's way more than 14. So §6's 25 isn't „OSM src" — it's „no register row near the pin by the measure's rule". Fine — I don't need to enumerate all 25 myself; I classify per §6's description.

Legitimate (per data): 
- частни училища с регистров двойник по положение/име: Първа частна търговска гимназия (≈Конто Трейд), Екзюпери (рег 67), Международно Френско училище — не е в регистъра на 12-те (не е в списъка!) — actually Френското училище isn't among the 12 private. Hmm. It's „Международно частно..." — not in varna.bg/302 list. So it has no register row — suspicious per the measure, but it may be registered under another name. Note it.
- университет МУ Стоянов — legitimate (no university register in task; 7 universities all OSM).
- Военно-морска болница — legitimate (military, outside МЗ/ИАМН civilian).
- Онкологична Марко Антонов = register row 8 СБАЛОЗ „Д-р Марко Антонов Марков" — legal name twin → legitimate name variant, should carry register name.
- Eurohospital = МЗ row 2 → twin.

Suspicious:
- „ЧОУ Феникс 2020" — not in the 12-register → no register row, OSM-only, kind училище.
- „8 СОУПЧЕ" — не съвпада с регистров ред (register has no №8 school; СУЕО Пушкин is the ЕО school).
- „бивше ОУ Д-р Никола Димитров" — status бивш, no live register row → per rule should arguably stay with status or go to board.
- „20 Логопедична ЦДГ" — no КАИС body ≤80 m (on „Друг вид сграда за обитаване"), no register row (регистърът няма „20 Логопедична"; ДГ20 е „Бриз" м. Салтанат 83 — delivered pin is at м-т Салтанат 43.21283, 27.947946... ДГ20 Бриз register м. Салтанат №83! So „20 Логопедична ЦДГ" could be old name of ДГ20 „Бриз"? kimi_verdict said „46 = 34 общински + 2 по положение (1 ЦДГ, 20 Логопедична ЦДГ)". Hmm, so 1 ЦДГ and 20 Логопедична cover ДГ1 and ДГ20 by position. But now with func data: 20 Логопедична sits 400 m from true ДЗ body (§3 Г2-ГРЕШКА table: 400.2 m). So its pin is suspicious.)
- „Детска градина Жирафче" — no register row; кв. Изгрев; near ДГ17 Петър Берон? (delivered 43.217801, 27.92736 vs ДГ17 43.2167, 27.924116 — ~300 m). Suspicious — private? not in the 11-list.
- „ДГ-4 Теменужка Филиал 1" — register ДГ4 Шейново 18; „филиал" без документ.
- ДКЦ 3/ДКЦ 4 — wait those ARE register-linked by name; §6 says they fall out only because register geocode is far. Delivered „ДКЦ 3 – Варна" has src register! (places.json: „ДКЦ 3 – Варна" ЕООД src ИАМН). Hmm §6 says „ДКЦ 3" и „ДКЦ 4" — вързани по име в регистъра, изпадат само защото геокодът на регистровия ред е далече. So they're fine.

OK. Now Q9: src for rows with register name placed by КАИС body: src = register row (one of the documented 4: „Регистър на училищата и детските заведения (Община Варна)", „Регистър на училищата (МОН/НЕИСПУО), одобрено 21.08", „Регистър на лечебните заведения (ИАМН)", НТР for hotels) — because src is the source of the NAME (summary_правило §6.3). Coordinate from КАИС is already covered by ADR 006 D7 licence line (КАИС Отворени данни) — no new licence row needed; marking via... summary_правило says for form Ф src = „КАИС адресно поле" which SRC_LINE already accepts. For register-named rows placed by КАИС: src stays register; the КАИС origin of coordinates documented in licence_registry meta (already says „Координатите: собствена геолокация върху отворените данни на КАИС"). places.json _meta.licence_registry indeed says coordinates from КАИС open data. ✓ So: name→src register; coordinate→covered by ADR 006 D7; per-row traceability via exporter's named table (REG rows) — and the placement rule (КАИС body used) documented in the поименна таблица.

Q10: what's wrong/missing in v1 — compile:
Wrong:
1. §0.1/rule: „Сграда за детско заведение = 74 площадки, 32 свободни" vs summary_правило §4: 74 площадки, непокрити ≤60 m = 32 ✓ consistent. OK.
2. v1 §0.2: „регистърът за район Владислав Варненчик дава 6 общински градини + 1 ясла" ✓ (RAJON_ID 6: ДГ37-42 + ДЯ6) confirmed.
3. v1 решение 11: „ДГ№3 Звездичка на 9,9 m, ДГ№10 Карамфилче на 9,1 m" — from kimi_verdict ✓.
4. v1 §11 says „регистровият адрес на ДГ№12 е ул. Дойран 9 — там има СВОБОДНА площадка с функцията" ✓ (parcel 55, 783 m², addr ДОЙРАН 9, OSM Ян Бибиян excluded at 0.0 m).
5. Errors: v1 решение 8 says „5 регистрови реда върху 4-те свободни площадки + Ниш 29". But the four control points include Ниш 29 as one of the four free parcels! summary_правило §5: „Свободните площадки са четири: (а) Шести септември 6, (б) Вл. Варненчик, (в) Валненчик, (г) Ниш 29". So „4-те свободни площадки + Ниш 29" double-counts: Ниш 29 IS one of the four. Correct: 5 register rows (ДГ37, 40, 41, 42, ДЯ6) onto 4 free parcels (Шести септември=ДГ40, Ниш 29=ДЯ6, +2 block parcels ДГ37/41) + Георги Минков 2 question for ДГ42. Actually that's 5 rows but only 4 parcels with assignments ДГ40→(а), ДЯ6→(г), ДГ41→(б), ДГ37→(в); ДГ42 has NO parcel (Маргаритка/Българче share Минков 2). So „5 регистрови реда върху 4-те свободни площадки" is only achievable if ДГ42 goes on Минков 2 (which is occupied by Маргаритка). Data says: 4 free parcels, 5 missing rows; one row (ДГ42) has no free parcel. v1's phrasing is loose; data verdict: ДГ42 = board.
6. v1 §2: „регистровият ред (общински ДГ 53 · ясли 12 · училища 69 · МЗ/ИАМН болници 18, ДКЦ 9, хосписи 7...)" — omits 11 частни ДГ and 7 ЦПЛР which ARE in places_registers.json (186 total). Also the count: 53+12+69+18+9+7 = 168, but register file has 186 (incl. частни ДГ 11 + ЦПЛР 7). v1's §2 omits them though решение 12 covers ЦПЛР and частни училища. Missing: 11 частни ДГ not mentioned in v1's per-class plan (§3 summary_регистри: частни ДГ 11 rows, delivered 1, missing 10!). v1 решение 8/12 don't address private ДГ. That's a gap: ЧДГ Малкият принц, Монтесори, Мелита have unambiguous bodies per §4 but v1 doesn't schedule them.
7. v1 §0.1: „КАИС адресът носи име в 1 от 19 813 стойности" ✓ confirmed by measure (10 institutional strings, 1 ДЗ).
8. v1 §0.1 says „две свободни площадки са в к.к. Златни пясъци" — summary_парцели §7 без име ДЗ: Златни ×2 + Ален Мак ×1 ✓.
9. v1 §0.1: „ул. Ниш 29 НЕ е без име: това е ДЯ №6 Мечо Пух" ✓.
10. Missing in v1: 
   - ДГ18/ДГ21 collision (same parcel) not mentioned in v1 (регистър §4 ⚠).
   - ЧДГ Мелита on ДГ6's yard — collision of private with municipal.
   - ОУ Иван Вазов/ПГЕ shared address — needs declared shared site, v1 doesn't mention (решение 12 mentions only counts).
   - ДЯ1/5/8 placement: v1 says ясли = new kind but doesn't list which ясли enter ЛОТ 1 (ДЯ6 yes via Владиславово; ДЯ5 resolved by addr text; ДЯ1, ДЯ8 без тяло → board). v1 §2 mentions ясли class but not the per-row disposition.
   - „Военно-морска болница" and universities have no register — under §0.1 rule „регистърът казва колко и как се казва" they fall out of the model entirely: no register → can't count them. v1 doesn't say how these 25 delivered-without-row rows are governed (they're currently kept by OSM). The rule „свободна площадка без регистров двойник = борд" applies to new rows; existing OSM rows without register (Военно-морска, университети, частни) need explicit grandfathering. v1 doesn't state it. Gap.
   - The register addresses for ДГ18/21: address machine returns nearly same point for different blocks — block geocode weakness (mediana 88 m, 0/9 ≤60 m per §7.2) — v1 §2 says „блок → блока в квартала" but block geocode is proven weak for placement (only 7/9 ≤150 m).
   - ДГ51 село misclassification was fixed earlier (kimi_verdict) — v1 §0.2 counts 6+1 for Владиславово ✓ fine.
   - v1 §2 „QA: всяко ново място лежи върху НЯКОЕ тяло ≤10 m (червено)" vs summary_правило §2: gate „d>60 m = error; 30-60 flag; 10-30 note" — v1's 10 m red gate is stricter than measured practice (51 records at ≤10 m are facade offsets; кампуси up to 46.8 m). For NEW rows it's fine as gate, but ПГТМД оцелелия пин is 35.2 m извън всяка сграда (kimi_verdict §4) — decision 10 says „оцелелият ляга на тяло (иначе 14 го хваща наново)". Consistent.

Wrong numbers check in v1:
- Решение 12: „7 общински + 8 частни" ✓ (with the note about 2 държавни ПГЕ/ПГТМД handled elsewhere).
- Решение 7: „ИАМН ги води като МЦ (№56, №43)" ✓.
- Решение 9: „Кардиолайф ... 3 748 m ... върху СБАЛК (0,0 m)" ✓ confirmed places.json identical coords.
- Решение 13: „5-те хотела с 382 легла + Спортпалас" — Спортпалас excluded with 151 beds and УИН ✓; the 5 hotels/382 beds I can't identify from hotels.json directly (probably 5 no_uin hotels with known beds from audit). Skip detail.
- §0.1 „9 от 135 доставени места нямат тяло с вярна функция" — summary_правило §3: 55 на друга функция; ok_d>60: двор 1+1, друга 20+10... hmm „9-те >60 m от вярно тяло" (решение 14): judges said 9 records >60 m from true body. summary_правило §3 table: друга function rows with ok_d ≤200: 20, >200: 10; помощна: 1+1. Total ok_d>200: 10+1=11? The „9" from решение 14's „9-те >60 m от вярно тяло всъщност лежат на ≤14,2 m от НЯКОЕ тяло". Consistent with judges. Fine.
- v1 §1 решение 14: „днес 0 случая" for „не лежи върху НИКОЕ тяло ≤10 m" — summary_правило §2: 287 inside + 51 ≤10 m = 338; so 23 записа are >10 m from any body! Wait: „вътре 287, ≤10 m 51 → 338 (93.6 %)". So records NOT within 10 m of any body = 361−338 = 23. But решение 14 says „червено = не лежи върху НИКОЕ тяло ≤10 m (днес 0 случая)". Contradiction! Judges lens 3 [14]: „Червено = „не лежи върху НИКОЕ тяло ≤10 m" (днес: 0 случая)" — hmm the judge ALT says 0 cases. But summary_правило §2 measures 23 records beyond 10 m from ANY body (19 at ≤30, 4 at ≤60). So „днес 0 случая" is WRONG per the measure: there are 23 (4 of which >30 m, all campuses). Unless „≤10 m" gate refers to... §2 table: вътре+≤10 = 338. So 23 records would fail a 10 m red gate, incl. ПГЕ (46.8), ТУ (37.4), ПГТМД (35.3), ВВМУ (31.1). v1's parenthetical „(днес 0 случая)" contradicts the measure — that's a data error in v1 to flag. The правило summary proposes 60 m red / 30 flag / 10 note precisely because of this. Good catch for Q10.

Wait — re-read v1 решение 14: „червено = „не лежи върху НИКОЕ тяло ≤10 m" (днес 0 случая); „вярна функция" = предупреждение". And judges [14] ALT proposed exactly that with „днес: 0 случая". But the measure (summary_правило §2) says 51 records are in ≤10 m band and 287 inside — meaning 23 beyond 10 m. So „0 случая" is wrong — unless the judge meant 0 cases beyond... no. Data verdict: v1 решение 14's parenthetical is wrong; actual = 23 records >10 m from any body (19 at 10–30 m, 4 at 30–60 m, 0 beyond 60 m). A red gate at 10 m would fire 23 times. This matters.

Also v1 §2 QA says „всяко ново място лежи върху НЯКОЕ тяло ≤10 m (червено)" — for new rows OK.

Q1: §0.1 reversed direction — agree? Data strongly support: КАИС addr has name 1/19813; func overcounts (74 parcels vs ~18 missing); func by designation not use (55 delivered on other-func bodies). Register gives names/counts. Where the rule errs: 
- private institutions outside register: частни ДГ register exists (11, detskitegradini 2022 secondary, no license, outdated) — the „register" for private ДГ is weak/secondary. 
- universities: NO register in the data set — 7 universities all src OSM; the rule „регистърът казва колко" can't count them (summary_регистри §2: „липсва регистър на висшите училища").
- Военно-морска болница: outside civilian register.
- Полицейска академия, Приют за бездомни, домове (социални грижи) — no register rows in scope.
So verdict: ДА with conditions (the rule holds for the 186-row register scope; outside it — universities, military hospital, private unregistered — the rule is silent, needs an explicit „no register exists" annex).

Q2: Владиславово assignments verdicts:
- #27 Ниш 29 = ДЯ6 Мечо Пух: ДА, влиза, no caveat (2 channels, 2 m). kind детска ясла.
- #25 Шести септември 6 = ДГ40 Детски свят: УСЛОВНО — влиза с бележка „по адресен низ, геометрично непотвърдено (регистърът пише до бл. 9, адресната машина няма такъв блок)". Two independent signals (unique street both sides). I'd say ДА с бележка.
- #24 розови тела = ДГ41 Първи юни: УСЛОВНО — 151/117-133 m, block geocode, 2.5× margin, single channel, „до бл. 309" key at 48.8 m from the parcel (summary_правило §5). Reasonable but eye of Петър.
- #23 Валненчик = ДГ37 Пламъче: УСЛОВНО — 152-156 m (just beyond 150 m threshold!), single channel, 3.0× margin. Eye of Петър.
- Маргаритка/Българче Минков 2 (4 clusters): НЕ се разграничава — ДГ38 delivered (ОДЗ Маргаритка), ДГ42 has no own parcel → board/eye of Петър.

Note distances differ slightly between summaries (117.3 vs 133 m; 137.1 vs 152 m) — different anchor (geocode point vs parcel). Both reported.

Q3 row-by-row: 24 rows.
ДГ (11):
- ДГ6 Палечко — ДА (точен геокод 15-28 m, 2 тела, addr match Тодор Влайков 71). Note: яслена група on 65А separate address — not tracked.
- ДГ11 Незабравка — ДА (block 20-28 m; excluded OSM „ЦДГ Незабравка" 0.0 m on parcel 50, addr ЕВЛОГИ ГЕОРГИЕВ) — second channel via excluded POI. ✓
- ДГ12 Ян Бибиян — ДА (точен 11 m; Дойран 9 parcel + excluded OSM „Ян Бибиян" 0.0 m).
- ДГ18 Чайка — НЕ/ОТХВЪРЛЯМ като еднозначно: same parcel as ДГ21; OSM name on parcel is „Калина Малина" (=ДГ21); alternative body under „4 ОДЗ Чайка" (3.9 m). За борда.
- ДГ19 Славейче — ДА (точен 2.1-15 m, addr Студентска 7 matches).
- ДГ21 Калина Малина — ДА (51 m block geocode, parcel 63, excluded OSM „Калина Малина" at 1.6 m — second channel).
- ДГ22 Мечо Пух — УСЛОВНО (92-94 m block geocode only, Чайка бл.43; parcel 65 ж.к. ЧАЙКА №98). Single channel. Note name collision: ДГ22 „Мечо Пух" vs ДЯ6 „Мечо Пух" — same name different institutions.
- ДГ25 Златното зрънце — УСЛОВНО→ДА? 51.8-62 m block; parcel 18 has excluded OSM „ЦДГ Зрънчо" 0.0 m — second channel (name variant). ДА с бележка (OSM excluded name).
- ДГ34 Лястовичка — ДА (79.8-83 m, block Възраждане-1 бл. 3; single channel but no competitor; margin?). УСЛОВНО (block geocode, single channel).
- ДГ41 Първи юни — УСЛОВНО (as Q2).
- ДГ53 Слънчево зайче — ДА (точен 43-44 m, addr Капитан Райчо 103А matches parcel 19 без име 539 m² — address string match).
Ясли (1): ДЯ6 — ДА.
Частни ДГ (3):
- ЧДГ Малкият принц — УСЛОВНО (block geocode 75 m, Чайка до бл. 19; parcel 1 100 m²; note: source is 2022 secondary; also „ПГ ИТOK Екзюпери" OSM at 0.0 m on same parcel 64 — collision! parcel #64 „ПГ ИТOK Екзюпери" 43.215086, 27.936242 1100 m² 5 bodies = same coords as Малкият принц 43.21511, 27.93625. Yes collision with delivered Екзюпери). So ЧДГ Малкият принц parcel is occupied by delivered ПГ ИТOK Екзюпери → dispute → board.
- ЧДГ Монтесори — НЕ (квартал geocode 116 m — слабо, само квартал; excluded OSM „ЧДГ Монтесори" at 6.4 m on parcel 70 Изгрев-1 159 m² — second channel exists actually. But 159 m² is tiny; register address УПИ-V-1529 кв.50. Verdict: УСЛОВНО/борд. Note also excluded „ЧДГ Монтесори" why: „частна ДГ без номер — профил на домашен адрес").
- ЧДГ Мелита — НЕ/борд (same yard as ДГ6; улица geocode 34 m — street-level, негоден; source 2022 secondary).
Училища (4):
- ОУ Иван Вазов — ДА (точен 3.1-5 m, Върба 24, 2147 m²) but shares address with ПГЕ → declared shared site, 1 pin 2 rows.
- СУ Св. Климент Охридски — ДА (точен 12 m, Михаил Колони 10).
- ПГЕ — ДА as second row on same declared site (Върба 24).
- ПГТМД — УСЛОВНО (улица geocode 144 m — слабо; but decision 10 already fixes ПГТМД pin: delivered Чайка pin at 977 m from register key, 35.2 m out of buildings, lies on campus; the parcel at 43.20740, 27.91931 1222 m²... hmm §4 gives ПГТМД body at 43.20740, 27.91931 which differs from delivered pin 43.213581, 27.924630. Distance between: ~(0.00617° lat ×110574)=682 m... that's not matching decision 10 which keeps the Чайка pin. Note tension: §4's „unambiguous body" for ПГТМД contradicts v1 решение 10 keeping the delivered pin + lying on body. Actually решение 10 says оцелелият ляга на тяло — the §4 body could be that тяло. Delivered pin 43.213581/27.924630 vs §4 body 43.20740/27.91931 — 700+ m apart. So not the same. Mark: ПГТМД §4 entry is слабо (144 m, улица) and conflicts with решение 10 — board.
Болници/ДКЦ/хосписи (5): all МК Младост complex — ДА as declared shared site with register rows; note КАИС addr says Република 91 (matches Лисичкова's №91, not №15) — the complex carries two numbers; single pin, N rows, „входове не се различават".

Q4: as analyzed — v1's decision 11 new form is ДА by data, with caveat: „4 ОДЗ Чайка" might actually be ДГ18 „Чайка" (register до бл. 3) — the data don't refute that; v1 sends it to board, which is the right disposition, but the same logic weakens §4's assignment of ДГ18 to ДГ21's parcel. Consistent story: ДГ18 unresolved → board.

Also note: „3 ЦДГ Ян Бибиян" delivered pin sits on ДЗ body at Добруджа 3 — no register institution there; OSM name carries wrong number 3 (ДГ3 is Звездичка, delivered separately „13 ЦДГ Звездичка" 9.9 m from its register spot). So board as unresolved OSM identity ✓.

ДГ12 new row Дойран 9: ДА — register address exact + parcel + excluded OSM name.
ДГ16 Гладстон: ДА — register ул. Гладстон 5; parcel 59 addr ГЛАДСТОН + excluded OSM „Слънчева дъга" 4.9 m. Note parcel addr is just „ГЛАДСТОН" (no number); single channel-ish but OSM excluded name = second channel. ДА.

Q5: ДА — register has 12 ясли as separate system (Я1, newkg.uslugi.io), distinct from DG register; delivered today as kind детска градина (8 rows: 4 register-src + 4 OSM). „с яслена група" as field not second record: register lists 18 ДГ with ЯГ as attribute of the same ДГ row (HAVE_INFANT_GROUP=True / infant reception list) — so поле, не запис ✓. Missing ДЯ1/5/6/8 by name ✓. ДЯ8 contradiction ✓ (28 vs 228). Note: ДЯ5 resolved via addr text (ДИМИТЬР ПОЛЯНОВ 5, 488 m²). ДЯ1 (Славянска 21) — no body → board. ДЯ8 — без тяло → board.

Q6: ДА/УСЛОВНО — 7+8 confirmed derivable; note 2 държавни (ПГЕ, ПГТМД) outside the 7+8 — ПГТМД via решение 10, ПГЕ via shared Върба 24. Еко детско селце извън общината ✓ (с. Зорница, община Аксаково). Талант ✓. Общежитие Колони new kind ✓ (func „Общежитие" exists, 46 bodies; excluded row exists with register twin).

Q7: ДА per data; caveats: (1) removal of Аджибадем loses the only delivered place at Шашкъна medical cluster and OSM says спешно — v1 covers with „new class if wanted"; (2) МК Младост N: data show 5 rows with unambiguous geocode to the complex + Царица Елеонора (no street, board) + Кардиолайф (бл. А, after гасене) — N = 5–7, must be pinned by named list, not „N"; КАИС address of the complex is бул. Република 91 — matches Лисичкова's register address, so Лисичкова joins the same pin even though her number differs from the others' №15.

Q8: classify the 25. Legitimate:
- Военно-морска болница (military, no civilian register) — keep, src OSM, note.
- Медицински университет (universities have no register in scope; all 7 universities OSM) — keep.
- Онкологична Марко Антонов / Eurohospital — OSM names of register rows (МЗ 8, МЗ 2) — legitimate twins, should get register names (решение 10 pattern).
- ДКЦ 3/ДКЦ 4 delivered — register-linked, fall out only by geocode distance — legitimate.
- Първа частна търговска гимназия ≈ Конто Трейд (reg 69) — legitimate by position (5 m).
- Екзюпери (reg 67) — legitimate, typo to fix („Антонан" → „Антоан").
- ОУ Христо Ботев, 3 ОУ Ангел Кънчев, ОУ Г.С.Раковски, I ЕГ, МГ Берон, Морска гимназия, НУИ Добри Христов, НУ Васил Левски, ОУ Черноризец Храбър... — these are OSM-name variants of register rows (register covers them by name but geocode far). Legitimate as twins — the 14 „училище" in §6 are mostly old-numbering/name variants.
Suspicious:
- ЧОУ Феникс 2020 — no register row among 12 частни; OSM only.
- 8 СОУПЧЕ — no register equivalent.
- Детска градина Жирафче — no register row, not in private list.
- 20 Логопедична ЦДГ — 400 m from true ДЗ body; possibly old name of ДГ20 Бриз — needs proof.
- ДГ-4 Теменужка Филиал 1, ЦДГ Пушкин (филиал) — „филиал" without document.
- бивше ОУ Д-р Никола Димитров — status бивш, no live row — keep with status or board.
- 3 ЦДГ Ян Бибиян, 4 ОДЗ Чайка — wrong-number OSM identities → board (v1 решение 11).
- ПГ текстил Вилите pin — гаси се (решение 10).

Q9: src = the register (one of existing 4 documented rows; ADR 006 D7 carries the КАИС licence line for coordinates; no new licence row). Marking КАИС-origin coordinate: places.json _meta.licence_registry already states coordinates = own geolocation over КАИС open data; per-row: exporter's поименна таблица (REG row → КАИС body id + distance + geocode class) as the audit artifact; don't put „КАИС" in src (src = source of the NAME). For form Ф rows (no register name) src = „КАИС адресно поле" (already accepted by SRC_LINE, index.html:6276) + status „без регистров двойник" — but wait status only allows „" or „бивш" per summary_правило §6.3 (STATUSES). Judges' gate suggested status „без регистров двойник" but schema forbids — so the marker must live in the exporter's board table, not in status. Flag this tension.

Q10: compile wrong + missing (as analyzed above).

Wrong in v1:
1. Решение 14 „(днес 0 случая)" — мярката дава 23 записа на >10 m от всяко тяло (19 при ≤30, 4 при ≤60 — кампусите). A 10 m red gate would fire 23×.
2. Решение 8/§0.2 „5 регистрови реда върху 4-те свободни площадки + Ниш 29" — Ниш 29 IS one of the four; 5 rows vs 4 parcels: ДГ42 Българче has no free parcel (Минков 2 occupied by Маргаритка). One row too many for the parcels.
3. §2 „регистровият ред (общински ДГ 53 · ясли 12 · училища 69 · болници 18, ДКЦ 9, хосписи 7)" = 168 — пропуска 11 частни ДГ + 7 ЦПЛР от places_registers.json (общо 186); частните ДГ нямат лот никъде в v1 (10 от 11 липсват, 3 с „еднозначно тяло").
4. МК Младост „N реда" — неуточнено N; данните дават 5 еднозначни + Царица Елеонора (без улица) + Кардиолайф (след гасене); и КАИС адресът на комплекса е „бул. Република 91" — т.е. Лисичкова (№91) и останалите (№15) са едно място с два номера.
5. §4's 24-row list internally: ДГ18/ДГ21 на едно място — не е еднозначно (OSM името на парцела е „Калина Малина" = ДГ21); ЧДГ Малкият принц съвпада с доставения ПГ ИТOK Екзюпери (същият парцел); ЧДГ Мелита върху двора на ДГ6; ПГТМД 144 m уличен геокод срещу решение 10.

Missing in v1:
- Университети/Военно-морска/частни извън регистрите: §0.1 rule has no authority for them; 25-те доставени без регистров ред нямат режим (grandfathering) в ЛОТ 1.
- Ясли per-row: само ДЯ6 е назована; ДЯ5 (решима по адресен текст), ДЯ1 и ДЯ8 (без тяло → борд) липсват от плана; ДЯ8 адресното противоречие (28/228).
- ДГ18 срещу „4 ОДЗ Чайка": възможно ОДЗ Чайка да е истинското място на ДГ18 — v1 го праща на борда, но тогава §4 редът „ДГ18 → парцел 63" трябва да падне.
- Блоковият геокод е слаб (медиана 88 m, 0/9 ≤60 m) — v1 §2 полага блокови адреси без диференциран праг/статус.
- „с яслена група" ДГ6 на втори адрес (Тодор Влайков 65А) — яслената група на ДГ6 е друга сграда; политиката „поле, не запис" я покрива, но вторият корпус остава без пин — съзнателно ли?
- Гейтът на бройката по квартал изисква семейството на квартала — П7 е неподписан (judges hole); v1 §2 го ползва („бройката по квартал = регистровите редове в семейството") — липсва отбелзка, че зависи от П7/регистъра на кварталите (които са подписани — vladislavovo alias exists in quarter_registry ✓ so partially covered).
- status schema: няма стойност „без регистров двойник" — маркерът за бордови/форма-Ф редове няма къде да живее в схемата.

Length: this is a lot. Format: tables per question, verdict ДА/НЕ/УСЛОВНО with довод. Write in Bulgarian, cite paths relative to C:/git. Be concise but complete. 10 sections.

Let me write the final answer.

Прочетох всичко от брифа: `Fire_Varna/scratch/audit_2026-09-03/ПРЕПОРЪКИ_v1.md`, `judges_summary.txt` (221 реда), `kimi_verdict.md`, трите `Fire_Varna/scratch/kais_func_2026-09-03/summary_*.md`, изворите `varna_3d/scratch/refactor/_addr/kimi_obrazovanie.txt` (1308 реда) и `sol_lechebni.txt` (717 реда), `Fire_Varna/data/places.json` (135 места, целия), `Fire_Varna/data/hotels.json` (целеви редове) и `Varna_buildings/config/quarter_registry.json`. Нищо не е пипано. Присъдите по десетте въпроса:

## 1 · §0.1 — обърнатата посока (регистър = колко/как се казва; КАИС = къде)

| твърдение в §0.1 | сверка | изход |
|---|---|---|
| КАИС `addr` носи име в 1 от 19 813 | `summary_парцели.md` §5а: 10 институционални низа, от тях 1 ДЗ („ЦДГ 10 - ПРИКАЗКА“), и той противоречи на регистъра (тялото е на ДГ№39, а ДГ№10 е „Карамфилче“) | потвърдено |
| функцията е по предназначение, не по ползване | `summary_правило.md` §3: 55 от 361 пина върху тяло с ДРУГА функция (хоспис върху „Хотел“, гимназия върху жилищна) | потвърдено |
| функцията надброява | 74 детски площадки / 32 свободни срещу ~18 липсващи институции; 2 свободни в к.к. Златни пясъци + 1 в с.о. Ален Мак, без регистров ред | потвърдено |

**Присъда: ДА, с условия.** Правилото е вярно за 186-те регистрови реда. Къде греши или мълчи:

| случай | проблем по данните |
|---|---|
| частни заведения извън регистъра | „регистърът“ за частни ДГ е detskitegradini 2022 — вторичен, без лиценз, остарял (`kimi_obrazovanie.txt:1278`); за 12-те частни училища регистър е varna.bg/302. Правилото наследява слабостта на извора си |
| университетски корпуси | регистър на висшите НЯМА в данните изобщо — и 7-те доставени университета са `src: OSM` (`Fire_Varna/data/places.json`); „регистърът казва колко“ е празен за този клас (`summary_регистри.md` §2 го казва: „липсва регистър на висшите училища, не имена“) |
| Военно-морска болница | извън гражданския МЗ/ИАМН регистър — по §0.1 тя е „без регистров двойник“ → борд, а е реална, доставена, критична |
| свободна площадка = борд | вярно, но само с доказан отрицателен резултат (гейтът на съдията по данни) — иначе Златни/Ален Мак биха родили фантоми |

## 2 · Владиславово — присвояванията

| парцел | присвояване | доказателства | присъда |
|---|---|---|---|
| #27 ул. Ниш 29 | ДЯ №6 „Мечо Пух“ | 2 m срещу 393 m за втория; ДВА независими канала (геокод на регистровия адрес + КАИС `addr` = „ул. НИШ 29“); точен ключ, 0.0–7 m | **ДА** — влиза, без бележка; `kind: детска ясла` |
| #25 ул. Шести септември 6 | ДГ№40 „Детски свят“ | уникалност и от двете страни (единствен регистров ред на „6-ти септември“ И единствен ДЗ парцел с тази улица в `addr` в целия град); но регистърът пише „до бл. 9“, а адресната машина няма такъв блок — 231–260 m, геометрично непотвърдено | **УСЛОВНО** — влиза с бележка „по адресен низ, не по геокод“; за окото на Петър във фикс-извадката |
| #24 розовите тела | ДГ№41 „Първи юни“ | 117–151 m, следващият на 380 m (2.5×); ключ `бул владислав варненчик бл 309` на 48.8 m от площадката; ЕДИН канал (блоков геокод — медиана 88 m по `summary_регистри.md` §7.2) | **УСЛОВНО** — вероятно, не доказано; за окото |
| #23 „Валненчик“ | ДГ№37 „Пламъче“ | 152–156 m — **точно извън прага 150 m**; следващият на 470 m (3.0×); единствено място от класа в 400 m; един канал | **УСЛОВНО** — най-слабото от четирите; за окото |
| ул. Георги Минков 2 (4 клъстера, 5+3+1+1 тела, 220 m ивица) | ДГ№38 „Маргаритка“ + ДГ№42 „Българче“ | 157 m срещу 169 m (1.08×) — не се разграничава; „ОДЗ Маргаритка“ стои на 0.0 m върху най-големия клъстер → ДГ№38 покрита, **ДГ№42 няма свой парцел** | **НЕ** — за борда/окото на Петър; или делят двор (тогава декларирана обща площадка), или „Българче“ е върху тяло с друга функция |

Важна рамка: районът има 23 тела „детско заведение“, 4 свободни площадки, а регистърът дава 6+1 институции, доставени 2 → **5 реда срещу 4 площадки** — математически поне един ред няма свободна площадка (виж въпрос 10).

## 3 · 24-те липсващи с еднозначно тяло — ред по ред

**Общински ДГ (11):**

| ред | d / геокод | присъда | довод |
|---|---|---|---|
| ДГ№6 „Палечко“ (Тодор Влайков 71) | точен, 15–28 m | **ДА** | КАИС `addr` на парцела е същата улица+номер; бележка: яслената група е на ДРУГ адрес (65А, `kimi_obrazovanie.txt:575`) — не се следи |
| ДГ№11 „Незабравка“ (Евлоги Георгиев до бл. 25) | блок, 20–28 m | **ДА** | втори канал: изключеният OSM „ЦДГ Незабравка“ стои на 0.0 m върху парцел #50 |
| ДГ№12 „Ян Бибиян“ (Дойран 9) | точен, 11 m | **ДА** | парцелът носи `addr` „ул. ДОЙРАН 9“ + изключен OSM „Ян Бибиян“ на 0.0 m — три съвпадения |
| ДГ№18 „Чайка“ (до бл. 3) | блок, 48 m | **НЕ** | отхвърлям „еднозначно“: сочи СЪЩИЯ парцел като ДГ№21, а OSM името върху парцела е „Калина Малина“ (= ДГ№21); конкуриращо тяло има под „4 ОДЗ Чайка“ (3.9 m) → борд |
| ДГ№19 „Славейче“ (Студентска 7) | точен, 2.1–15 m | **ДА** | адресен низ съвпада дословно |
| ДГ№21 „Калина Малина“ (Чайка до бл. 40) | блок, 43.7–51 m | **ДА** | втори канал: изключен OSM „Калина Малина“ на 1.6 m върху парцел #63 |
| ДГ№22 „Мечо Пух“ (Чайка до бл. 43) | блок, 92–94 m | **УСЛОВНО** | един канал; плюс колизия на имената с ДЯ №6 „Мечо Пух“ — двете да се различават в речника |
| ДГ№25 „Златното зрънце“ (Младост до бл. 127) | блок, 52–62 m | **ДА с бележка** | втори канал: изключен OSM „ЦДГ Зрънчо“ на 0.0 m върху парцел #18 |
| ДГ№34 „Лястовичка“ (Възраждане-1 до бл. 3) | блок, 80–83 m | **УСЛОВНО** | един канал, без конкурент наблизо |
| ДГ№41 „Първи юни“ | 117–151 m | **УСЛОВНО** | вж. въпрос 2 |
| ДГ№53 „Слънчево зайче“ (Капитан Райчо Николов 103А) | точен, 43–44 m | **ДА** | безименният парцел #19 носи точно този `addr` |

**Ясли (1):** ДЯ №6 „Мечо Пух“ — **ДА** (вж. въпрос 2).

**Частни ДГ (3):**

| ред | присъда | довод |
|---|---|---|
| ЧДГ „Малкият принц“ (Чайка до бл. 19) | **НЕ** | парцелът (1100 m², 43.21511/27.93625) е ЗАЕТ от доставения „ПГ ИТOK „Екзюпери““ (0.0 m, същите координати) — спор, не еднозначност; изворът е вторичен 2022 |
| ЧДГ „Д-р Мария Монтесори“ (Изгрев, УПИ-V-1529) | **УСЛОВНО** | квартален геокод 116 m = слабо; втори канал има (изключен OSM „ЧДГ Монтесори“ 6.4 m), но парцелът е 159 m² и конвейерът вече я е отсъдил „профил на домашен адрес“ → борд |
| ЧДГ „Мелита“ (Тодор Влайков бл. 7) | **НЕ** | уличен геокод (негоден по §7.2) върху двора на ДГ№6; единствен извор — вторичният списък 2022 → борд |

**Училища (4):**

| ред | присъда | довод |
|---|---|---|
| ОУ „Иван Вазов“ (Върба 24) | **ДА** | точен, 3.1–5 m, 2147 m² — но адресът е ОБЩ с ПГЕ в самия регистър (редове 12 и 48) → декларирана обща площадка, 1 пин / 2 реда, не 2 пина |
| СУ „Свети Климент Охридски“ (Михаил Колони 10) | **ДА** | точен, 12 m |
| ПГЕ (Върба 24) | **ДА** | вторият ред на общата площадка с Иван Вазов; на място доставената „Професионална гимназия по електротехника“ (OSM) е на 46.8–53 m — кое име на кой корпус не се измерва |
| ПГТМД (Осми приморски полк 113) | **НЕ тук** | „еднозначното“ тяло е на 144 m с УЛИЧЕН геокод (негоден) и е на ~700 m от оцелелия Чайка-пин, който решение 10 запазва — редът си противоречи с решение 10 → решава се в 10, не в §4 |

**Болници/ДКЦ/хосписи (5):** и петте сочат едно КАИС място (43.23086/27.87875, 6 тела, 3096 m², `addr` „бул. Република **91**“):

| ред | присъда | довод |
|---|---|---|
| СБАЛДБ „Лисичкова“ (Република 91) | **ДА** | точен, 8 m; КАИС `addr` потвърждава №91 — т.е. №91 и №15 са един и същ комплекс с два номера |
| ДКЦ Младост-М + хосписи Надежда / Медицинска грижа / Мария Магдалена (Република 15) | **ДА** | един пин, N реда САМО като декларирана обща площадка; „Хоспис Царица Елеонора“ (без улица в адреса) и Кардиолайф (бл. А, след гасенето) са отделни редове на същия обект — N трябва да е поименно, не буква |

## 4 · Решение 11 в новия вид

| елемент | сверка | присъда |
|---|---|---|
| „3 ЦДГ Ян Бибиян“ НЕ се мести | пинът (43.217812/27.920193) е на 1.4 m от ДЗ тяло с `addr` „ул. Добруджа 3“ — там регистърът няма нищо; носи чужд номер (ДГ№3 е „Звездичка“, тя си е на мястото на 9.9 m) | **ДА** — остава + на борда като неразрешена OSM самоличност |
| „4 ОДЗ Чайка“ НЕ се мести | на 3.9 m от ДЗ тяло в ж.к. Чайка; регистровите кандидати (ДГ№18 бл. 3, ДГ№21 бл. 40) геокодират другаде | **ДА** — на борда; бележка: данните НЕ отхвърлят хипотезата, че това е истинското място на ДГ№18 — затова и ДГ№18 в §4 падна (въпрос 3) |
| ДГ№12 нов ред на Дойран 9 | регистров адрес + парцел 783 m² с функцията + изключен OSM „Ян Бибиян“ на 0.0 m | **ДА** |
| ДГ№16 на „Гладстон“ | регистър: ул. „Уйлям Гладстон“ №5; парцел #59 с `addr` „ГЛАДСТОН“ + изключен OSM „Слънчева дъга“ (= името на ДГ№16) на 4.9 m | **ДА** — два независими канала (уличен текст + OSM име) |
| преименуване само при съвпадащ КАИС адрес (ДГ№3, ДГ№10) | 9.9 m / 9.1 m от регистровите адреси — потвърдени в `kimi_verdict.md` §7 | **ДА** |

## 5 · Яслите

| въпрос | присъда | довод |
|---|---|---|
| ясла = отделен клас „детска ясла“ | **ДА** | регистърът ги държи като ОТДЕЛНА система (newkg.uslugi.io, `kimi_obrazovanie.txt:551-563`) — 12 реда, различни от ДГ-регистъра; днес 8 са доставени под `kind: детска градина` (4 регистрови + 4 OSM); КАИС функцията НЕ различава ясла от градина — kind може да дойде само от регистъра, както в v1 |
| „с яслена група“ = поле, не втори запис | **ДА** | в регистъра това е атрибут на същия ред (`HAVE_INFANT_GROUP: true` / reception=infant, 18 ДГ); втори запис би дублирал 18 институции. Изключение за борда: ДГ№6 има ЯГ на ДРУГ адрес (65А) — полето не покрива втори корпус |
| ДЯ №1/5/6/8 липсват | **ДА** | по име липсват точно тези 4; по мярката §3 (≤60 m невзет) ДЯ №1 се води „покрита по близост“ — да се реши кое броене влиза в гейта |
| ДЯ №8 противоречие | **ДА** | регистър: Евлоги Георгиев **28**; varna.bg/2214: **228** (`kimi_obrazovanie.txt:1270`) — и няма тяло на ≤150 m → борд, не пин |
| ДЯ №5 „Чуден свят“ | допълнение | формално „негеокодируема“, но се разрешава по адресен текст: КАИС „ул. ДИМИТЬР ПОЛЯНОВ 5“ (Ь = грешка в КАИС), 488 m² — кандидат за ЛОТ 1, в v1 липсва |

## 6 · Решение 12 — числата

| число в v1 | сверка | присъда |
|---|---|---|
| 8 частни (не 9) | **ДА** | 12 листнати − Талант = 11 действащи; покрити 3 (Екзюпери рег. 67, ЧСУ Монтесори рег. 65, Конто Трейд ≈ рег. 69) → 8 липсващи: Монтесори Варна ЧОУ, Малкият принц, Прогресивно 2, Демократично, Аз съм българче, Мечтатели, Джордж Байрон, ЧПГ по инженеринг |
| Талант вън | **ДА** | „НЕ провежда учебен процес (2020/21), без адрес“ — дословно в извора (`kimi_obrazovanie.txt:1178`); записва се като съзнателно изключен |
| Еко детско селце извън общината | **ДА** | с. Зорница е извън община Варна (`kimi_obrazovanie.txt:1054, 1290`) |
| 7 общински | **УСЛОВНО** | изводимо: Иван Вазов, СУ Св. Кл. Охридски, I ОУ Борис, ОУ Стоян Михайловски, ОУ Раковски, ГПЧЕ, IV ЕГ = 7. НО мълчаливо изключва 2-те ДЪРЖАВНИ (ПГЕ — общ адрес с Иван Вазов; ПГТМД — в решение 10) и 3-те селски училища (Каменар, Константиново, Тополи — `summary_регистри.md` §3 брои само 2 села при училищата, изворът дава 3 — незатворена сметка). Гейтът трябва да изброи 7-те поименно |
| общежитие „Михаил Колони“ = нов вид | **ДА** | КАИС има функция „Общежитие“ (46 тела); парцел #29 носи името от изключен OSM POI на 6.0 m; днес редът е поименно изключен „въпреки регистровия двойник“ (`places.json:457-461`) — влизането е смяна на подписано правило, не добавка; геокод-капанът Цар Освободител 150 (разсейване 2225 m, `summary_регистри.md` §7.1) налага ръчен пин. Бележка: КАИС `addr` на парцела е „Цар Освободител **0** · Дойран 17/19“ — не 150 |

## 7 · Решения 7/9

| елемент | присъда | довод |
|---|---|---|
| Аджибадем излиза (= изтрива се) | **ДА** | ИАМН ред 56, вид МЦ (`sol_lechebni.txt:430`); пинът лежи върху жилищна многофамилна (0.0 m); цената е казана открито в v1 (няма kind МЦ). Условието за OSM_OUT с регистровия ред като довод — задължително |
| „Майчин дом“ излиза | **ДА** | ИАМН ред 43, вид МЦ, ул. Мир 1 (`sol_lechebni.txt:417`) |
| Кардиолайф се гаси/мести | **ДА** | в `places.json:1266-1285` Кардиолайф и СБАЛК „Варна“ имат БАЙТОВО еднакви координати (43.213541/27.91808) — 0.0 m; регистровият адрес е бул. Република, МЦ „Младост“, бл. А → 3748 m; и двата реда са от ИАМН износа — дублетът е регистров, не OSM → гейт при експорта |
| МК „Младост“ = декларирана площадка с N реда | **УСЛОВНО** | мярката: 5 регистрови реда с еднозначно тяло + Царица Елеонора (адрес без улица) + Кардиолайф след гасене = 5–7 реда, ЕДИН пин. „N“ трябва да стане поименен списък със стабилен ключ (не индекс+име — Сол/съдията), иначе гейт 4 и решение 9(г) се блокират взаимно завинаги |

## 8 · 25-те доставени без регистров ред

| група | оценка | редове |
|---|---|---|
| **легитимни — регистърът ги покрива по друго име/положение** | запазват се, сливане по модела на решение 10 | „Онкологична болница-Марко Антонов“ (= МЗ №8), „Eurohospital“ (= МЗ №2 Еврохоспитал, Виница ✓), „Първа частна търговска гимназия“ (≈ Конто Трейд, рег. 69), „Екзюпери“ (рег. 67 — с правописна грешка „Антонан“ в доставката), „ДКЦ 3“/„ДКЦ 4“ (регистрови по име, изпадат само от далечен геокод), OSM вариантите на стара номерация (3 ОУ Ангел Кънчев, ОУ Христо Ботев и пр.) |
| **легитимни — извън обхвата на регистрите** | запазват се, но §0.1 трябва да ги назове изрично | „Военно-морска болница“ (военна, извън МЗ/ИАМН), „Медицински университет“ и изобщо университетите (регистър на висшите липсва в данните) |
| **съмнителни** | борд | „ЧОУ „Феникс 2020““ (няма го сред 12-те частни в регистъра), „8 СОУПЧЕ“ (няма регистров еквивалент), „Детска градина „Жирафче““ (нито общинска, нито в списъка на частните), „20 Логопедична ЦДГ“ (на 400 m от вярно ДЗ тяло; възможно старо име на ДГ№20 „Бриз“ — недоказано), „ДГ-4 „Теменужка“ Филиал 1“ и „ЦДГ Пушкин (филиал)“ („филиал“ без документ), „бивше ОУ „Д-р Никола Димитров““ (status бивш — остава със статуса или на борда), „3 ЦДГ Ян Бибиян“ / „4 ОДЗ Чайка“ (чужди номера — вече покрити от решение 11) |

## 9 · Произход (`src`) на регистрово име върху КАИС тяло

| елемент | присъда | какво трябва да пише |
|---|---|---|
| `src` = регистърът | **ДА** | `src` е изворът на ИМЕТО (`summary_правило.md` §6.3) — една от четирите документирани стойности („Регистър на училищата и детските заведения (Община Варна)“, „…(МОН/НЕИСПУО), одобрено 21.08“, „Регистър на лечебните заведения (ИАМН)“; за хотелите НТР). Нов лицензен ред не влиза — ADR 006 D7 вече носи КАИС реда за координати |
| отбелязване на КАИС-координатата | **УСЛОВНО** | пакетно вече е покрито: `_meta.licence_registry` в `places.json` казва „Координатите: собствена геолокация върху отворените данни на КАИС“. Редово — в поименната таблица на износителя (регистров ред → КАИС тяло `i` + разстояние + клас на геокода), НЕ в `src`. Дупка: съдията иска маркер „без регистров двойник“, но `STATUSES` позволява само `""`/`"бивш"` — маркерът няма поле в схемата; да живее в борда, или схемата да се отвори съзнателно |
| форма Ф (без регистрово име) | бележка | само тогава `src` = „КАИС адресно поле“ — стойност, която `SRC_LINE` вече приема; и само след доказан отрицателен резултат (гейтът на съдията) |

## 10 · Какво в v1 е ГРЕШНО и какво ЛИПСВА

**Грешно:**

| # | място в v1 | какво казват данните |
|---|---|---|
| 1 | решение 14: червен гейт „не лежи върху НИКОЕ тяло ≤10 m (**днес 0 случая**)“ | `summary_правило.md` §2: 287 вътре + 51 на ≤10 m = 338 → **23 записа са на >10 m от всяко тяло** (19 на 10–30 m, 4 кампуса на 31–47 m). Гейтът би гръмнал 23 пъти още днес; правилният червен праг по мярката е 60 m (0 случая), 30 m флаг, 10 m забележка |
| 2 | §0.2/решение 8: „5 регистрови реда върху 4-те свободни площадки **+ Ниш 29**“ | Ниш 29 Е една от четирите (`summary_правило.md` §5: свободните са (а)(б)(в)(г)=Ниш 29). Реално: 5 реда срещу 4 площадки — ДГ№42 „Българче“ няма свободна площадка (Минков 2 е зает от „Маргаритка“) и трябва изрично да отиде на борда, не „върху 4-те + Ниш“ |
| 3 | §2: изворът = „общински ДГ 53 · ясли 12 · училища 69 · болници 18, ДКЦ 9, хосписи 7“ (= 168) | `places_registers.json` носи **186** реда — пропуснати са 11 частни ДГ и 7 ЦПЛР; за частните ДГ (10 липсващи, 3 с кандидат-тяло) в v1 няма нито лот, нито дума |
| 4 | решение 9(г): „МК „Младост“ = декларирана площадка с N реда“ | N не е число; данните дават 5 еднозначни + 2 условни, и КАИС адресът на комплекса е „Република 91“ — т.е. редът на Лисичкова (№91) и четирите на №15 са едно място с два номера; това трябва да е записано в декларацията |
| 5 | (наследено от §4 на мярката, не поправено в v1) | ДГ№18/№21 на едно място и ЧДГ „Мелита“ върху двора на ДГ№6 не са „еднозначни“ — вж. въпрос 3 |

**Липсва:**

| # | какво | довод |
|---|---|---|
| 1 | режим за доставените БЕЗ регистър (25-те) | §0.1 дефинира правило само за нови редове; университети, Военно-морска, частни без регистров ред остават без „дедо-гейт“ — всеки следващ одит ще ги „открива“ наново (същата грешка, за която Аджибадем отива в OSM_OUT) |
| 2 | яслите поименно | v1 назовава само ДЯ №6; ДЯ №5 (разрешима по адресен текст, 488 m²), ДЯ №1 (без тяло) и ДЯ №8 (без тяло + противоречие 28/228) нямат съдба в ЛОТ 1 |
| 3 | връзката ДГ№18 ↔ „4 ОДЗ Чайка“ | ако ОДЗ Чайка е истинското място на ДГ№18, решение 11 („на борда“) и §4 („ДГ№18 → парцел 63“) не могат да стоят едновременно — да се каже кое |
| 4 | диференциран праг за блоков геокод | §7.2 на мярката: блок „до бл. N“ — медиана 88 m, 0/9 под 60 m; v1 §2 полага такива адреси със същия гейт като точните — новите редове с блоков геокод трябва да носят класа на увереността си в таблицата на износителя |
| 5 | зависимостта от П7 | „броят по квартал = регистровите редове в семейството на квартала“ ползва семействата на кварталния регистър; `quarter_registry.json` покрива Владиславово (alias + parent на Кайсиева ✓), но П7 като цяло е неподписан (съдията по данни, hole) — да се отбележи като предусловие |
| 6 | поле за „без регистров двойник“ | схемата (8 ключа, `STATUSES` = „“/„бивш“) няма къде да пази този маркер — вж. въпрос 9 |

**Присъди в един ред:** (1) ДА с условия · (2) Ниш 29 — ДА; Шести септември/Първи юни/Пламъче — УСЛОВНО за окото; Минков 2 — НЕ, борд · (3) 17 ДА / 4 УСЛОВНО / 3 НЕ (ДГ18, Малкият принц, Мелита) + ПГТМД — в решение 10 · (4) ДА · (5) ДА · (6) УСЛОВНО — 8 частни ДА, „7 общински“ да се изброи, селските 2-срещу-3 незатворени · (7) ДА за 7 и гасенето на Кардиолайф; УСЛОВНО за „N реда“ — поименно · (8) разделени на три групи по-горе · (9) ДА — `src` = регистър, КАИС-отбелезката в таблицата на износителя, не в схемата · (10) 5 грешни + 6 липсващи, по-горе.

