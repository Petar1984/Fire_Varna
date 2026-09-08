kimi version 0.34.0
• Read-only analysis. Need to read the JSON files in the working directory (the copy). Let me read them all.

• Чета файловете от копието, за да направя съпоставката.

• I have enough from quarter_registry — the tail has more entries (franga_dere, kv etc.) but not critical. Let me skim the last 220 lines quickly to see remaining ids.Now I have everything. Write the analysis ≤800 words, compact table for (1), verdict + К36-1… numbered proposals. In Bulgarian. Relative paths from kimi_areas root.

  Let me do the 1:1 mapping for all 95 imot.bg areas.

  Our codes (signed60 + partition additions): abatko, akchelar, alen_mak, asparuhovo, balam_dere, borovets_sever, borovets_yug, briz, chaika_kk, chaika_kv, dobreva, dolna_traka, druzhba, evksinograd, fichoza, galata, gorchivata_cheshma, gorna_traka, grackata_mahala, hristo_botev, izgrev_kv, kaisieva, kk_konstantin_elena, kochmar, kokardzha_generic, kolhozen_pazar, kv_levski, maksuda, manastirski_rid, menteshe, mladost, mladost1, mladost2, morska_gradina, pchelina, perchemliyata, pobeda, priboy, pz_planova, rakitnika, rozova_dolina, saltanat, sotira, sredna_traka, sv_ivan_rilski, sveti_nikola, trakia, troshevo, tsentar, tv_kula, vazrazhdane, vazrazhdane1-4, vinitsa, vladislavovo, zelenika, zlatni_pyasatsi, zpz + proposed: fatriko_dere, kantara, salzitsa, pogrebite, generalite, ostrovna_pz, severna_pz, dilber_cheshma, sportna_zala, baba_alino, dabravata, banala_cheshma, zavod_druzhba, kokodiva, sava, byalata_cheshma, chigana, kapelova_gradina, tsveten_kvartal + landmarks: operata, obshtinata, stadion_spartak.

  Registry also has: trakata_so, so_planova, pz_metro, mikro4/8 (dropped), vinitsa_sever, vayalar, deli_sava, botanicheska, malka_chaika, vilite, yuzhna_pz, starite_lozya, bokluk_tarla, golyama/malka_kokardzha, franga stuff, trakata_vz.

  Now map 95 imot areas:

  1. avtogara (53) — NEW. Автогара е в Младост (бул. Вл. Варненчик 158), между Младост 1 и Възраждане? Автогара Варна е в зоната на бул. Владислав Варненчик, между Младост 1 и Трошево... Всъщност е в район Младост, близо до Младост 1. Предложи код avtogara, зона, mladost. Родител — вероятно mladost1 съсед, но като зона самостоятелна. Кандидат за дупка.
  2. asparuhovo (744) — = asparuhovo.
  3. bazar-levski (72) — синоним/дете на kv_levski? „Базар Левски" — пазарът в кв. Левски. Имаме kv_levski alias "Васил Левски". imot има и "Левски 1/2". Базар Левски вероятно е част от Левски 1. Третирай като синоним→kv_levski (или дете/зона). Кажа: синоним на kv_levski (пазарната част).
  4. biznes-park-varna (14) — обект/зона; Бизнес парк Варна е на юг от града, при Аспаруховско шосе, в ЗПЗ? Всъщност е край бул. „Република"... Бизнес парк Варна е в Западната промишлена зона? Не — на изхода към Бургас, в м-т Прибой? Точно не съм сигурен. Обект (комплекс сгради), не район → report-only/обект.
  5. biznes-hotel (37) — обект (Бизнес хотел Варна в центъра). Обект.
  6. briz (902) — = briz.
  7. vinitsa (1413) — = vinitsa.
  8. vins-cherven-ploshtad (85) — НЯМА код (Петър: не виждам ВИНС и Червения площад). NEW: vins_cherven_ploshtad, кв/район, odesos, родител — съсед на Гръцката махала/Център. ВИНС (Икономически университет) и Червения площад са между Гръцка махала и Колхозен пазар/Център. Дупка.
  9. vladislav-varnenchik-1 (911) — синоним→vladislavovo (или дете). Registry влива Вл. Варненчик I/II м.р. във vladislavovo.
  10. vladislav-varnenchik-2 (108) — синоним→vladislavovo (частично kaisieva? Р33: typo до Кайсиева). Влезе в конфликт (3).
  11. vazrazhdane-1..4 — = vazrazhdane1..4.
  12. galata (383) — = galata.
  13. grand-mol (174) — обект (мол в Център, бул. Княз Борис I). Обект, не район; в Център. Може и ориентир-район („при Гранд Мол"), но по Петър: обекти отделно.
  14. gratska-mahala (220) — = grackata_mahala (правопис).
  15. zhp-gara (33) — NEW обект/зона. ЖП гарата е южно от Център, при Гръцката махала/Морска гара. Зона между Център и Аспарухово мост — кандидат дупка (морска гара зоната). Предложи zhp_gara, зона, odesos.
  16. zavod-druzhba (22) — = zavod_druzhba (предложен, partition го има).
  17. zapadna-promishlena-zona (178) — = zpz.
  18. zimno-kino-trakiya (86) — NEW район/ориентир; imot го ползва като район. Registry: trakia се показва през Зимно/Лятно кино. Синоним→trakia? Или нов район zimno_kino_trakia ⊂ trakia. Петър иска райони → район-дете на trakia.
  19. izgrev (436) — = izgrev_kv.
  20. kaysieva-gradina (832) — = kaisieva.
  21. kolhozen-pazar (401) — = kolhozen_pazar.
  22. konfuto (34) — NEW. Конфуто е местност/квартал близо до Летището, западно (м-т Конфуто край Аксаково?). Конфуто е на запад от града край пътя за летището — район mladost? Всъщност Конфуто е при летище Варна, в района на летището (район Приморски административно? Западна част). Не знам със сигурност — маркирай „район на запад, вероятно mladost/vladislav_varnenchik; не знам". Кандидат дупка.
  23. levski-1 (537), levski-2 (161) — при нас един kv_levski (без 1/2) + Цветен квартал като дете. Конфликт (3).
  24. letishte (29) — обект/зона летище Варна (на запад, при Аксаково/Конфуто). Обект, не район.
  25. lyatno-kino-trakiya (277) — landmark съществува като точка; район → дете на trakia, код lyatno_kino_trakia.
  26. maksuda (3) — = maksuda (подписан, но само 3 обяви — бройки в (4)).
  27. metro (17) — pz_metro в registry (ПЗ Метро)! = синоним→pz_metro. Район vladislav_varnenchik.
  28. mladost-1 (431), mladost-2 (169) — = mladost1/2. (imot няма голо „Младост" — при нас mladost е родител-етикет.)
  29. okrazhna-bolnitsa-generali (171) — = generalite (Петър: Генералите сбъркан — конфликт (3)).
  30. operata (84) — съществува като ориентир-СГРАДА; Петър иска РАЙОН. NEW район operata ⊂ tsentar (odesos).
  31. ostrovna-promishlena-zona (8) — = ostrovna_pz.
  32. planova-promishlena-zona (6) — = pz_planova (registry alias „Планова промишлена зона" вече е в pz_planova). Синоним→pz_planova.
  33. pobeda (145) — = pobeda.
  34. pogrebi (357) — = pogrebite (синоним; нашето „Погребите").
  35. pristanishte-varna (5) — обект/зона пристанище (одесос, край морската гара). Обект/зона — вероятно зона pristanishte, odesos.
  36. promishlena-zona-topoli (7) — NEW зона при с. Тополи — asp?? Тополи е село в община Варна, район... с. Тополи е в административен район Аспарухово? Не — с. Тополи е югозападно, в район Аспарухово на община Варна. Да, Тополи е към район Аспарухово. Код pz_topoli, зона, asparuhovo.
  37. sveti-nikola (163) — = sveti_nikola.
  38. sportna-zala (59) — = sportna_zala (предложен вече).
  39. stadion-spartak (4) — landmark сграда; Петър иска район южно от бул. Вл. Левски при стадиона. NEW район stadion_spartak между kv_levski и pobeda, district? Между Левски (primorski) и Победа (mladost) — граница; вероятно mladost или primorski. Кажа „primorski/mladost — спорно, решение на Петър".
  40. troshevo (416) — = troshevo.
  41. festivalen-kompleks (42) — NEW район/обект. Фестивалният комплекс (ДКС) е в Център, ул. Сливница. Обект в Център; imot го ползва като микрорайон. Кандидат: район-дете на tsentar или обект. Подобно на Операта → район.
  42. hei (57) — NEW. ХЕИ (Хидроенергоизчислителен институт?) — „ХЕИ" е квартална зона близо до Христо Ботев/Окръжна болница? ХЕИ е район около бившия институт, между Христо Ботев и... Всъщност ХЕИ е при бул. Цар Освободител, близо до ВИНС? Не съм сигурен. Известно: ХЕИ е кварталче на юг от Трошево? Не знам — маркирай. Всъщност ХЕИ (кв. ХЕИ) е в Младост? Не знам.
  43. hristo-botev (83) — = hristo_botev.
  44. tsveten-kvartal (329) — = tsveten_kvartal (предложен, дете на kv_levski).
  45. tsentralna-poshta (115) — NEW; Централна поща е в Център (ул. Съборни). В decisions tsentar включва „Централна поща" (wm 34598647). → синоним/дете на tsentar.
  46. tsentar (823) — = tsentar.
  47. chayka (187) — двусмислено: coord_rule „чайка" — северно от 43.24 = chaika_kk, южно = chaika_kv. imot отделно има к.к. Чайка (373) → значи голото „Чайка" при тях е градският квартал → chaika_kv.
  48. chataldzha (108) — имаме в block_overrides (Чаталджа, бл.16/18 на 8 м.р.), но НЯМА полигон! NEW район chataldzha, кв, odesos — кандидат дупка (между Център и Колхозен пазар, ул. Д-р Пискюлиев).
  49. v-z-vinitsa-sever (1) — = vinitsa_sever (registry: с.о. Виница-север).
  50. v-z-zvezditsa (10) — с. Звездица също има (108). в.з. Звездица → NEW, дете на zvezditsa? Код vz_zvezditsa, вз, mladost (Звездица е в район Младост? с. Звездица административно е към район Младост, община Варна — да).
  51. k-k-zlatni-pyasatsi (499) — = zlatni_pyasatsi.
  52. k-k-sv-sv-konstantin-i-elena (610) — = kk_konstantin_elena.
  53. k-k-slanchev-den (111) — NEW кк slanchev_den, primorski (между Св. Константин и Златни пясъци). Кандидат дупка (между kk_konstantin_elena и zlatni_pyasatsi).
  54. k-k-chayka (373) — = chaika_kk.
  55. m-t-akchelar (134) — = akchelar.
  56. m-t-alen-mak (573) — = alen_mak.
  57. m-t-atanas-tarla (4) — NEW м-т atanas_tarla — южна местност (Asparuhovo?). Не знам точно; Атанас Тарла е южно от Аспарухово? Не знам.
  58. m-t-balam-dere (20) — = balam_dere (с.о. Балъм дере).
  59. m-t-bokluk-tarla (8) — = bokluk_tarla (registry).
  60. m-t-borovets-sever (104) — = borovets_sever.
  61. m-t-borovets-yug (223) — = borovets_yug.
  62. m-t-gorna-traka (269) — = gorna_traka.
  63. m-t-dobreva-cheshma (62) — = dobreva.
  64. m-t-dolna-traka (225) — = dolna_traka.
  65. m-t-evksinograd (163) — = evksinograd (м. ЕВКСИНОГРАД е alias).
  66. m-t-zelenika (109) — = zelenika.
  67. m-t-kantara (18) — = kantara (предложен).
  68. m-t-kochmar (9) — = kochmar (alias „м-т Кочмар").
  69. m-t-krushkite (10) — NEW м-т krushkite — не знам; вероятно primorski (вила зони към Горна Трака?). Не знам.
  70. m-t-lazur (7) — NEW м-т lazur — Лазур е при к.к. Чайка/Траката? „Лазур" местност край Чайка. Не знам сигурно.
  71. m-t-manastirski-rid (246) — = manastirski_rid.
  72. m-t-mentesheto (34) — = menteshe (правопис „Ментешето").
  73. m-t-orehcheto (10) — NEW м-т orehcheto — не знам.
  74. m-t-perchemliyata (88) — = perchemliyata.
  75. m-t-planova (31) — = so_planova (registry: alias „м-т Планова").
  76. m-t-priboy (119) — = priboy.
  77. m-t-pripek (4) — NEW м-т pripek — южно, не знам.
  78. m-t-pchelina (291) — = pchelina.
  79. m-t-rakitnika (54) — = rakitnika.
  80. m-t-saltanat (22) — = saltanat.
  81. m-t-sotira (76) — = sotira.
  82. m-t-salzitsa (35) — = salzitsa.
  83. m-t-televizionna-kula (2) — = tv_kula.
  84. m-t-fichoza (14) — = fichoza.
  85. m-t-franga-dere (4) — = franga_dere (registry Р23; няма полигон в partition? franga_dere не е в 82-те клетки — местност Франга Дере е в registry но не е подписан полигон). Маркирай: в registry, без полигон в partition.
  86. s-zvezditsa (108) — NEW с. zvezditsa, с., mladost. Извън града (община Варна).
  87. s-kazashko (14) — NEW с. kazashko, с., mladost (Казашко е към район Младост).
  88. s-kamenar (7) — NEW с. kamenar — Каменар е към район Аспарухово? Не — с. Каменар е община Варна, район... Каменар е югозападно, административно район Аспарухово? Всъщност Каменар е в община Варна, район Аспарухово. Не съм сигурен — не знам. Кажи „вероятно asparuhovo, не знам".
  89. s-konstantinovo (61) — NEW с. konstantinovo, vladislav_varnenchik (Константиново е към район Вл. Варненчик).
  90. s-topoli (185) — NEW с. topoli, asparuhovo.

  Districts for села в община Варна: Звездица и Казашко → район Младост; Константиново → Владислав Варненчик; Тополи → Аспарухово; Каменар → Аспарухово. Това е стандартно деление. I'll state with mild confidence, mark Kamenar as uncertain.

  Count check: 95 items — covered.

  ХЕИ: actually ХЕИ — think. „кв. ХЕИ" във Варна... Хидроенергетичен институт? ЕИ = „Енергетичен институт". The area called ХЕИ is near кв. Христо Ботев, около бул. Република? Всъщност спомням си: ХЕИ е районът около Медицински колеж/бившия Хидроенергетичен институт на бул. 3-ти март? Не знам сигурно. Маркирай „не знам; вероятно odesos/mladost". Actually I recall ХЕИ е близо до Окръжна болница/Генералите — т.е. между Христо Ботев и Трошево? ХЕИ = Хидроенергоизчислителен институт, намирал се на бул. Христо Смирненски — това е в района на Червения площад/ВИНС? Хм. I'll say „не знам със сигурност; често се свързва с ивицата Христо Ботев–Трошево, odesos/mladost — проверка".

  Конфуто: местност Конфуто е край летище Варна, западно. Административно летището е в район... на територията на с. Аксаково (община Аксаково). Hmm. Маркирай „на запад при летището; извън петте района (община Аксаково?) — не знам".

  Бройки (4): Стадион Спартак 4, Максуда 3, Планова ПЗ 6 — прагът: под ~10 обяви районът не може да се очертае от обяви (боклук-тарла 8, островна ПЗ 8, тополи ПЗ 7). За обвивка от точки: ≥50 обяви дава смислен convex hull; 50–100 грубо; ≥100 добре. Плътни (≥50): посочи кои: asparuhovo 744, briz 902, vinitsa 1413, vins 85, vlv1 911, vlv2 108, vazr1 409, vazr2 107, vazr3 318, vazr4 135, galata 383, grand-mol 174, grackata 220, zpz 178, zimno kino 86, izgrev 436, kaisieva 832, kolhozen 401, levski1 537, levski2 161, lyatno kino 277, mladost1 431, mladost2 169, generali 171, operata 84, pobeda 145, pogrebi 357, sv.nikola 163, sportna zala 59, troshevo 416, hei 57, botev 83, tsveten 329, poshta 115, tsentar 823, chayka 187, chataldzha 108, zlatni 499, konstantin 610, slanchev den 111, chayka kk 373, akchelar 134, alen mak 573, borovets sever 104, borovets yug 223, gorna traka 269, dobreva 62, dolna traka 225, evksinograd 163, zelenika 109, manastirski 246, perchemliyata 88, priboy 119, pchelina 291, rakitnika 54, sotira 76, ts.poshta... konstantinovo 61, topoli 185, bazar levski 72, avtogara 53. Под 50: konfuto 34, biznes hotel 37, zhp gara 33, metro 17, letishte 29, maksuda 3, stadion 4, ostrovna 8, planova pz 6, pristanishte 5, topoli pz 7, festivalen 42, vz zvezditsa 10, vinitsa sever 1, atanas tarla 4, balam dere 20, bokluk 8, kantara 18, kochmar 9, krushkite 10, lazur 7, mentesheto 34, orehcheto 10, planova 31, pripek 4, salzitsa 35, saltanat 22, tv kula 2, fichoza 14, franga dere 4, kazashko 14, kamenar 7.

  Note: many signed polygons with low listing counts (kochmar 9, tv_kula 2, balam_dere 20) — those are fine since they're signed by parcels; the threshold only matters for NEW areas derived from listings.

  (3) Конфликти:
  - Левски 1/2 vs kv_levski: предложение — приеми levski1/levski2 като деца на kv_levski (като vazrazhdane1-4, mladost1/2) или влей двете в kv_levski. imot данните: 1=537, 2=161. Съвместимо с нашата йерархия: kv_levski родител, levski1/2 деца. Цветен квартал вече дете на kv_levski — припокриване? Цветен квартал е част от Левски 2 вероятно. Предложи: Цветен ⊂ levski2.
  - Вл. Варненчик 1/2 vs vladislavovo+kaisieva: registry влива I и II м.р. във vladislavovo; imot разделя 1 (911) и 2 (108). Предложение: vv1 → vladislavovo (тясно), vv2 ≈ kaisieva? Р33 казва typo е „до Кайсиева". Или деца vv1/vv2 под vladislavovo, с Кайсиева сестра. Решение на Петър.
  - Възраждане 4 без родител: в signed60 _meta.parent_child има само vazrazhdane1-3 → parent vazrazhdane; vazrazhdane4 липсва → добави parent (vazrazhdane). Тривиална липса.
  - Чайка vs к.к. Чайка: coord_rule вече решава (север/юг от 43.24); imot голото „Чайка" (187) + „к.к. Чайка" (373) потвърждава правилото — голото е градският квартал (chaika_kv), защото курортът им е отделен ред.

  (5) Обекти, не райони: biznes-hotel (сграда в Център), grand-mol (мол в Център), letishte (инфраструктура, западно, извън районите), pristanishte-varna (индустриална зона/инфраструктура), biznes-park-varna (комплекс). Третиране: клас „обект" — не влизат в partition; само като точки-ориентири/aliases към домакина (Център, zpz…). Летището и Пристанището може и като зони (инфраструктурни), но НЕ жилищни райони; пристанището вероятно се покрива от zpz/островна? Пристанище Варна е в Източната промишлена зона — край морската гара; остави „зона, odesos, или обект — решение".

  Verdict + К36-1... proposals:
  - К36-1: ~46 от 95 се покриват 1:1/синоним от подписаните+предложените.
  - К36-2: нови райони-кандидати за дупките: obshtinata (район, ⊂ Център), operata (район ⊂ Център), stadion_spartak (район между Левски и Победа), vins_cherven_ploshtad, chataldzha, avtogara, zhp_gara, slanchev_den, tsentralna_poshta (⊂ Център), bazar_levski (⊂ Левски), zimno/lyatno kino (⊂ Тракия), festivalen (⊂ Център), konfuto, hei, pz_topoli, селата (zvezditsa, kazashko, kamenar, konstantinovo, topoli, vz_zvezditsa), дребни м-та (atanas_tarla, krushkite, lazur, orehcheto, pripek — „не знам", ниски бройки).
  - К36-3: конфликти както горе.
  - К36-4: праг ~10 за очертаване; обекти отделно.

  Word limit 800. Table must be compact — 95 rows will be huge. Use very compact table: columns: imot име (n) | статус | наш код / предложен код (вид, район, родител). Combine rows where possible. I'll need to be terse. 95 rows × ~8 words is already ~700 words. Use ultra-compact: `=code` for matches, `→code` synonyms, `**new_code** (вид; район; родител)` for new.

  Maybe group table into sections with shared rows. I'll write abbreviations: район codes od/pri/mla/vlv/asp. Let me write it tightly. Aim ~780 words total including other sections, so table ~500 words. Terse.

• Прочетох и шестте файла. Ето анализът (пътищата са относително корена на копието: `imot_bg_varna_areas_08.09.json`, `signed60_props.json`, `partition_v2_props.json`, `decisions_5_draft_08.09.json`, `landmarks_v2.json`, `quarter_registry.json`).

  ## (1) Съпоставка 1:1 — 95-те района на imot.bg

  Легенда: `=` съвпада с наш код · `→` синоним/правопис към код · `★` НОВ (код; вид; район; родител) · `?` не знам къде е. Райони: od/pri/mla/vlv/asp.

  | imot.bg (n) | статус | код / предложение |
  |---|---|---|
  | Аспарухово 744, Бриз 902, Виница 1413, Галата 383, Изгрев 436, Кайсиева 832, Колхозен пазар 401, Победа 145, Трошево 416, Христо Ботев 83, Център 823, Св. Никола 163, Максуда 3, м-т Акчелар 134, м-т Ален мак 573, Боровец-север 104, Боровец-юг 223, Горна Трака 269, Добрева чешма 62, Долна Трака 225, Зеленика 109, Манастирски рид 246, Перчемлията 88, Прибой 119, Пчелина 291, Ракитника 54, Сотира 76, Сълзица 35, ТВ кула 2, Фичоза 14, Кантара 18, ЗПЗ 178, Островна ПЗ 8, Спортна зала 59, Цветен кв. 329, Завод Дружба 22, к.к. Златни пясъци 499, к.к. Св.Св. К. и Елена 610, к.к. Чайка 373, Възраждане 1–4 (409/107/318/135), Младост 1/2 (431/169) | `=` | същите кодове (Цветен/Кантара/Островна/Спортна/Завод Дружба — от `partition_v2_props.json`, предложени) |
  | Гръцка махала 220 | `→` | `grackata_mahala` |
  | Погреби 357 | `→` | `pogrebite` |
  | Балам Дере 20 | `→` | `balam_dere` (с.о.) |
  | Ментешето 34 | `→` | `menteshe` |
  | м-т Планова 31 | `→` | `so_planova` (регистър, alias „м-т Планова“) |
  | Планова ПЗ 6 | `→` | `pz_planova` (alias вече е в регистъра) |
  | Метро 17 | `→` | `pz_metro` (регистър Р32) |
  | м-т Кочмар 9 | `→` | `kochmar` |
  | м-т Евксиноград 163 | `→` | `evksinograd` |
  | м-т Франга Дере 4 | `→` | `franga_dere` (Р23, в регистъра; без клетка в partition) |
  | м-т Боклук Тарла 8 | `→` | `bokluk_tarla` (регистър Р37) |
  | в.з. Виница-север 1 | `→` | `vinitsa_sever` (регистър Р37) |
  | Чайка 187 | `→` | `chaika_kv` (курортът е отделен ред → голото е градското) |
  | Левски 1 (537) / Левски 2 (161) | конфликт | вж. (3) — `kv_levski` ± деца |
  | Вл. Варненчик 1 (911) / 2 (108) | конфликт | вж. (3) — `vladislavovo` + `kaisieva` |
  | Окръжна болница-Генерали 171 | `=` но сбъркан | `generalite` — вж. (3) |
  | Базар Левски 72 | `→`/дете | `bazar_levski` (зона; pri; `kv_levski`) или чист alias |
  | Лятно кино Тракия 277 | ★ район | `lyatno_kino_trakia` (район; od; `trakia`) — в `landmarks_v2.json` е точка, Петър иска район |
  | Зимно кино Тракия 86 | ★ район | `zimno_kino_trakia` (район; od; `trakia`) |
  | Операта 84 | ★ район | `operata` (район; od; `tsentar`) — сега е сграда-ориентир |
  | Централна поща 115 | ★/дете | `tsentralna_poshta` (зона; od; `tsentar`) — вече е съставка на черновия Център |
  | Фестивален комплекс 42 | ★ район | `festivalen_kompleks` (район; od; `tsentar`) |
  | ВИНС-Червен площад 85 | ★ | `vins_cherven_ploshtad` (кв; od; между `grackata_mahala` и `kolhozen_pazar`) — Петър го търси, липсва |
  | Чаталджа 108 | ★ | `chataldzha` (кв; od; между Център и Колхозен пазар) — в регистъра е само block_override, без полигон |
  | Стадион Спартак 4 | ★ район | `stadion_spartak` (район; pri/mla спорно; между `kv_levski` и `pobeda`) — в момента е сграда в дупка |
  | Автогара 53 | ★ | `avtogara` (зона; mla; при бул. Вл. Варненчик, съсед на `mladost1`/`vazrazhdane`) |
  | ЖП Гара 33 | ★ | `zhp_gara` (зона; od; морска гара, южно от `tsentar`/`grackata_mahala`) |
  | ХЕИ 57 | ★ ? | `hei` (район; od/mla — не знам със сигурност, ивицата Хр. Ботев–Трошево) |
  | Конфуто 34 | ★ ? | `konfuto` (м-т/район; западно при летището — не знам чий район, може и извън петте) |
  | к.к. Слънчев ден 111 | ★ | `slanchev_den` (кк; pri; между `kk_konstantin_elena` и `zlatni_pyasatsi`) — класическа дупка |
  | Пристанище Варна 5, Летище 29, Гранд Мол 174, Бизнес хотел 37, Бизнес парк 14 | обекти | вж. (5) |
  | с. Звездица 108 / в.з. Звездица 10 | ★ | `zvezditsa` (с.; mla) + дете `vz_zvezditsa` (вз) |
  | с. Казашко 14 | ★ | `kazashko` (с.; mla) |
  | с. Константиново 61 | ★ | `konstantinovo` (с.; vlv) |
  | с. Тополи 185 + ПЗ Тополи 7 | ★ | `topoli` (с.; asp) + `pz_topoli` (зона; asp; `topoli`) |
  | с. Каменар 7 | ★ ? | `kamenar` (с.; вероятно asp — не знам сигурно) |
  | м-т Атанас Тарла 4, Припек 4, Орехчето 10, Крушките 10, Лазур 7 | ★ ? | дребни м-та; местоположение — не знам (вероятно asp/pri периферия); под прага за очертаване |

  Общо: ~52 покрити (`=`+`→`), ~30 нови кода, 5 обекта, 3 конфликтни двойки, 6 „не знам“.

  ## (2) Кандидати за дупките

  Сигурни: `stadion_spartak` (дупката Левски–Победа, потвърдена от `landmarks_v2.json`), `slanchev_den` (Константин–Златни), `vins_cherven_ploshtad` и `chataldzha` (одесоската ивица Център–Колхозен пазар–Гръцка махала), `avtogara` (Младост 1–Възраждане), `zhp_gara` (морска гара). Като райони-дъпки в Център: `operata`, `obshtinata` (Общината — район по Петър, днес сграда), `festivalen_kompleks`, `tsentralna_poshta`. Не знам: ХЕИ, Конфуто, Гранд Мол е В Център (обект), Метро=`pz_metro` (покрито), Летището е извън градската мрежа.

  ## (3) Конфликти

  - Левски 1/2: направи `levski1`/`levski2` деца на `kv_levski` (схемата Възраждане/Младост); `tsveten_kvartal` става дете на `levski2`. Алтернатива — вливане, но губиш 537/161 обяви разделение.
  - Вл. Варненчик 1/2: регистърът влива I и II м.р. във `vladislavovo`; imot ги дели. Предложение: `vv1`≈тясно Владиславово, `vv2`≈`kaisieva` (Р33: typo-то е „до Кайсиева“) — дума на Петър.
  - `vazrazhdane4` няма родител в `_meta.parent_child` (signed60) — пропуск; добави `parent: vazrazhdane`, както 1–3.
  - Чайка: `coord_rule` (север/юг от 43.24) е потвърдено от imot.bg — при тях „Чайка“ и „к.к. Чайка“ са отделни редове, голото = `chaika_kv`.

  ## (4) Бройките

  Под ~10 обяви районът не може да се очертае от обяви (Стадион Спартак 4, Максуда 3, Планова ПЗ 6 — но трите вече имат полигони от кадастър/OSM, така че бройката е релевантна само за НОВИ райони). Праг: ≥10 грубо, ≥50 надеждна обвивка. Нови кандидати ≥50: ВИНС 85, Чаталджа 108, Автогара 53, Слънчев ден 111, Операта 84, Поща 115, Зимно кино 86, Лятно кино 277, Константиново 61, Тополи 185, Звездица 108, ХЕИ 57. Под прага: Конфуто 34, ЖП Гара 33, Фестивален 42, ПЗ Тополи 7, с. Каменар 7, в.з. Звездица 10, дребните м-та (2–10) — само от Wikimapia/OSM, не от обяви.

  ## (5) Обекти, не райони

  `biznes_hotel`, `grand_mol` (и двата в Център), `letishte` (инфраструктура, западно извън районите), `pristanishte_varna`, `biznes_park_varna`: клас „обект“ — не влизат в partition; само точка-ориентир + alias към квартала-домакин (като политиката keep_and_report в `quarter_registry.json`). Гранд Мол има 174 обяви — хората търсят „при Гранд Мол“ → alias към `tsentar`, не клетка.

  ## Присъда

  imot.bg потвърждава модела: ~55 % от редовете са вече покрити; дупките на Петър са реални и се пълнят с ~12 нови градски района (ВИНС, Чаталджа, Спартак, Автогара, ЖП гара, Слънчев ден + районните Операта/Общината/Поща/Фестивален/двете кина) и 6 села; 5 имена са обекти и остават извън клетките; трите конфликта се решават с йерархия, не със сливане.

  - К36-1: приеми съпоставката от (1); `vazrazhdane4` получава `parent: vazrazhdane`.
  - К36-2: нови райони-дъпки: `obshtinata`, `operata`, `tsentralna_poshta`, `festivalen_kompleks` (всички ⊂ `tsentar`, od); `zimno_kino_trakia`, `lyatno_kino_trakia` (⊂ `trakia`, od); `vins_cherven_ploshtad`, `chataldzha` (od); `stadion_spartak` (pri/mla — Петър); `avtogara`, `zhp_gara`, `slanchev_den`; села `zvezditsa`+`vz_zvezditsa`, `kazashko` (mla), `konstantinovo` (vlv), `topoli`+`pz_topoli`, `kamenar` (asp?).
  - К36-3: Левски 1/2 и Вл. Варненчик 1/2 като деца по схемата Възраждане/Младост; Генералите преначертава `generalite` по imot-дефиницията „Окръжна болница-Генерали“ (сегашният 4-точков правоъгълник е груб — Петър: „не е идентифициран правилно“).
  - К36-4: праг 10/50 обяви за нови райони от imot; обектите (мол, хотел, летище, пристанище, бизнес парк) → report_only + alias, никога клетки.
  - К36-5: открити въпроси към Петър: ХЕИ и Конфуто (местоположение/район), vv2↔Кайсиева, Спартак pri или mla, Каменар.

To resume this session: kimi -r session_2de3445c-c6a1-4daa-adc9-7a3492c647a5
