# Сол · атака върху ПРЕПОРЪКИ v1 (03.09.2026; git.gpt.log от ред 219909)

## Обща присъда

| № | Тежест | Присъда | Какво чупи |
|---:|---|---|---|
| 1 | **БЛОКЕР** | „Пълна зонова фраза“ и prepend-ът не са специфицирани еднозначно. Твърдението „3/103“ е невярно за комбинираните решения. | Няма еднозначен код, branch и reference gate. |
| 2 | **ГОЛЯМА** | `old_names` е безопасен само при ясно ограничен M1 обхват. Глобалното му участие отваря допълнителни резултати. | Еталонът става минимум 5/103 променен; dedupe не е проверим между билдове. |
| 3 | **БЛОКЕР** | Няма стабилен ключ за място/обща площадка. | Allowlist може да се прехвърли към друг обект след reorder или корекция. |
| 4 | **БЛОКЕР** | ЛОТ 3 няма подписуем ADR write-set, flag semantics, anchor contract или честен `N`. | `false` може да изключи адресната търсачка; G3 не знае кои разлики са допустими. |
| 5 | **БЛОКЕР** | ЛОТ 2 не е „един ред“ и има предварително измерени регресии. | 11 813 надписа стават по-къси; 17 се свеждат до стойности като „1“, „2“, „10“. |
| 6 | **БЛОКЕР** | Името `pb` не прави стойността private-safe; липсват value validator, representative map и partition gate. | Потенциален кадастрален теч и тихо прегрупиране между билдове. |
| 7 | **БЛОКЕР** | Count/PiP/reference gates са самореферентни, липсващи или циклични. | Планът не може fail-loud да докаже пълнота, положение или очакван recall diff. |
| 8 | **БЛОКЕР** | Нито един от трите лота не е подписуем в този вид. | Одобрението би подписало неизвестни или вече опровергани ефекти. |

## 1 · Канонична зонова фраза + prepend

| Елемент | Подписуемо точно правило |
|---|---|
| Остатък | След `placeTokens()` и `splitKeys()` първият населен ключ определя класа; `R` е подреденият остатък. Текущият клон е в [index.html:6655](/C:/git/Fire_Varna/index.html:6655). |
| Legacy A3′ | Сегашният A3′ без именна колизия остава непроменен; иначе контролът `хотел златни` може да падне от 85. |
| Пълна зонова фраза | `R` трябва да е точна подредена token-последователност на цялата значеща част на каноничен `zone` или на приета P7 форма. Без prefix/fuzzy/подмножества; типовите думи се махат само по подписан списък. |
| Представяне | Нужен е phrase index `zoneFormsByRecord`. Сегашният P7 flatten към `ztk/zkset` в [index.html:6478](/C:/git/Fire_Varna/index.html:6478) губи границите и реда на фразите. |
| Collision override | Само ако сегашното class-wide name veto блокира валидна пълна зонова фраза, се прави per-record зонова селекция. |
| A3 prepend | `R` трябва да е точна подредена последователност в едно текущо име/разрешен alias — никога сбор от различни aliases, prefix или fuzzy. Резултатът е `nameRows + zoneRows`, stable-unique по самия `rec` object, без повторно общо сортиране. |
| M1 prepend | Отделно правило: при `R=[]` цялата заявка трябва да съвпада с цялото точно име. Връща `exactRows + вече подредения categoryRows`; не преизчислява общия ред. |

| Заявка | Сега | Резултат по точното правило | Контрол |
|---|---:|---:|---|
| `хотел одесос` | 1 | **23** = ПАРК ХОТЕЛ ОДЕСОС + 22 зонови | Именният ред е извън зоната. |
| `хотел одес` | 2 | **2** | Частична фраза: няма override. |
| `хотел морска градина` | 3 | **18** | Двутокенова пълна зона; широк `runScored()` prepend погрешно би дал 21. |
| `училище морска градина` | 1 | **6** | Няма отделна строга именна опашка. |
| `хотел владиславово` | 2 | **2** | Само чрез изрично приетата P7 форма. |
| `хотел градина` | 1 | **1** | `градина` не е пълната зона `морска градина`. |

| Трите A3′ реда | Текущ еталон | Нов еталон |
|---|---|---|
| [`gate_p7[11]` · `хотел приморски`](/C:/git/Fire_Varna/scratch/places_search/recall_sweep_rows.json:6395) | M2, `n=1` | **A3′, `n=5`**: ПРИМОРСКИ + Маргарита, Вемара сити, Траката, Еллинис |
| [`gate_p7[14]` · `училище свети никола`](/C:/git/Fire_Varna/scratch/places_search/recall_sweep_rows.json:6458) | M2, `n=8` | **A3′, `n=1`**: ПГХХТ „Д. И. Менделеев“ |
| [`gate_p7[16]` · `хотел зеленика`](/C:/git/Fire_Varna/scratch/places_search/recall_sweep_rows.json:6512) | M2, `n=1` | **A3′, `n=2`**: Зеленика, Джоя; Зеленика се дедупира по identity |

| Контраатака срещу „3/103“ | Резултат |
|---|---|
| Само изолираният A3′ контрафакт | 3/103 |
| A3′ + задължителният M1 prepend от решение 2 | Минимум **4/103**: [`градина`](/C:/git/Fire_Varna/scratch/places_search/recall_sweep_rows.json:4114) става `46→47`. |
| Ако `old_names` prepend важи и извън M1 | Минимум **5/103**: [`хотел варненчик`](/C:/git/Fire_Varna/scratch/places_search/recall_sweep_rows.json:6525) става `2→3`, добавяйки КАРНИВАЛ от old name „Варненчик“. |

| Цена | Реалистична мярка |
|---|---:|
| M1 exact-current-name + identity concat | 15–25 JS реда |
| `old_names` provenance/precedence | още 10–20 |
| Phrase index + A3′ override | още 20–30 |
| Общо в `initPlacesSearch` | **45–70 JS реда** |
| Reference parity и целеви gates | още **35–60 Python/JS реда** |
| Адресен код | 0 реда |

## 2 · `old_names`, identity и DOM

| Тежест | Находка | Какво чупи |
|---|---|---|
| **ГОЛЯМА** | `old_names` вече участват в A6 чрез `aset` в [index.html:6515](/C:/git/Fire_Varna/index.html:6515). `Явор` не е категориен M1 ключ; текущо дава 3 реда. | Аргументът „трябва в exact index заради решение 10“ не следва от механиката. |
| **ГОЛЯМА** | Измерени са 54 записа с 59 old names, но **0** old-name ключа съвпадат с населен категориен ключ. | В текущия snapshot old names не носят M1 полза. |
| **ГОЛЯМА** | Глобален exact alias индекс внезапно активира кратки aliases като `ИУ` и `МУ`, които сега дават 0. | Неподписана промяна на обикновените M2/M3/A6 заявки. |
| **ГОЛЯМА** | Клиентският dedupe може да е `Set(rec)`, но публичните редове нямат стабилен `id`, а reference пази само `{name,zone}`. | Междубилдово identity доказателство липсва; име/зона/пин могат да слеят различни места. |

| Проверка на `градина` | Точен резултат |
|---|---|
| `search().rows` | **47**: хотел ГРАДИНА + същите 46 детски градини |
| Подредба | `rows[1:]` трябва да е identity-equal със старите 46; общо повторно `orderCategory()` е забранено. |
| Видими `.pl-item` | **9** = 1 хотел + 8 детски градини |
| Tail | **`…и още 38`** |
| Буквални DOM деца | **12** = 2 headers + 9 items + tail; „1+8+tail“ е семантично, не буквален брой nodes. Renderer-ът е в [index.html:6742](/C:/git/Fire_Varna/index.html:6742). |

## 3 · Декларирана обща площадка

| Кандидат за ключ | Присъда |
|---|---|
| Array/регистров индекс + име | **НЕ** — exporter-ът сам го нарича крехък в [export_fire_varna_places.py:18](/C:/git/varna_3d/src/export_fire_varna_places.py:18); текущите таблици са точно такива в [export_fire_varna_places.py:114](/C:/git/varna_3d/src/export_fire_varna_places.py:114). |
| Номер на ред в регистъра | **НЕ**, освен ако изворът изрично гарантира постоянен record ID. Insert/reorder го сменя. |
| Хеш на име+адрес | **НЕ** — корекция на правопис или адрес сменя ключа; стойността е и лесно отгатваема. |
| НТР УИН | **ДА като `place_id` за хотел**, но не е универсален и не е `site_id`. |
| OSM type/id | **ДА като provenance/place identity**, но не е универсален site key. |
| Подписуем вариант | Постоянен private `place_id` за всеки обект и отделен, веднъж присвоен непрозрачен UUID `site_id`; имената, адресите, УИН и OSM ref са evidence, не идентичност. |

| Gate | Механика |
|---|---|
| Обхват | Тича върху финалното обединение `places + hotels`; отделен exporter gate ще пропусне Явор/Голдън Лайн. |
| Pair rule | Всяка двойка `<5.0 m` трябва да има един и същ деклариран `site_id` и двата `place_id` да фигурират в exact member list. |
| Referential integrity | Fail при unknown/missing/stale member, член в две площадки, празна площадка или недеклариран близък pair. |
| Baseline proof | Преди декларациите gate-ът трябва да падне върху трите известни двойки; след подписаните решения трябва да мине. |
| Negative test | Нарочно копие с допълнителен недеклариран ред на `<5 m` трябва задължително да падне. |
| Build stability | Два билда с еднакви входове дават byte-identical `place_id/site_id` mapping. |

## 4 · ЛОТ 3

| Подточка | Тежест | Атака и необходима корекция | Какво чупи |
|---|---|---|---|
| а · ADR | **БЛОКЕР** | ADR 006 забранява както функции/CSS на адресния път в [D4](/C:/git/Fire_Varna/docs/decisions/006_places_in_search.md:94), така и `search_index.json` и всички функции на `initAddressSearch` в [D12](/C:/git/Fire_Varna/docs/decisions/006_places_in_search.md:157). Следователно амандментът е нужен **преди ЛОТ 2**, не само за ЛОТ 3. | ЛОТ 2 сам нарушава действащия ADR. |
| б · Flag | **БЛОКЕР** | `ADDRESS_PATH_V2` стои непосредствено пред/в началото на IIFE, но е selector, не early-return guard. `false` инициализира целия legacy адресен път. | Ранен `return` при [началото на IIFE](/C:/git/Fire_Varna/index.html:4833) премахва адресната търсачка. „~2 реда“ е невярно за шестте use-site клона. |
| в · 18→мярка→3 | **ГОЛЯМА** | Замразеният одит има 545 далечни label keys; текущият snapshot има **547**. Read-only counterfactual: само 1/547 съдържа same-`pb` редове, маха се един ред, но **547/547 остават >200 m**. Физическите групи са максимум 125 m. | №18 не свива причинно проблема на №3 и не е предпоставка за него. |
| в · №18 contract | **БЛОКЕР** | Кодът очаква и ID, и representative map в [index.html:5260](/C:/git/Fire_Varna/index.html:5260); v1 доставя само entry `pb`. Нужна е safe карта `pbr: pb→public _ord` или еквивалентен representative marker. | Без нея „първият след sort“ заменя подписаното max-appcount tie правило. |
| г · Разстояние | **БЛОКЕР** | Източникът трябва да е snapshot на оперативната котва `lastFix` — GPS, ръчен пин или предишно избран адрес. Без котва суфиксът се пропуска; `map.getCenter()` не е допустим fallback. | Сегашният G3 отказва geolocation и клика последователно редовете в [probe_places_fv.mjs:598](/C:/git/Fire_Varna/scratch/places_search/probe_places_fv.mjs:598), т.е. предишният клик замърсява следващата заявка. |
| д · №15 | **БЛОКЕР при безусловно изрязване** | Само raw query; никога index/label. `Адрес:` и `·` се чистят преди legacy `norm→skel`. Типовете се пробват като втори fallback само ако legacy няма чист all-token hit. Текущият ред е [index.html:5153](/C:/git/Fire_Varna/index.html:5153). | Безусловното махане прави `кв. Чайка` и `к.к. Чайка` една заявка. Измерени са 17 такива различия; без структурирано `area_type` типът не може после да бъде възстановен. |
| е · Tail | **БЛОКЕР** | Сега cap-ът е в [index.html:5308](/C:/git/Fire_Varna/index.html:5308), а dedupe е чак в [renderResults:5425](/C:/git/Fire_Varna/index.html:5425). Renderer-ът няма честен total. | `N` не може да се изчисли от capped масива. |

### Минимален ADR договор

| Част | Минимален текст |
|---|---|
| Изключение | „D4/D12 остават в сила извън изрично изброения write-set. Амандментът влиза преди ЛОТ 2.“ |
| Data write-set | Builder-ът и publish gate-ът във Varna_buildings плюс генерираният `Fire_Varna/data/search_index.json`. `address_rows.json`, `sw.js`, worker и hydrant/report/compass пътищата остават недосегаеми. |
| Address write-set | Само новият flag/helpers и `dedupeDisplayRows`, `runGeocoderSearch`, `buildExactItem`, `renderResults`, `renderCombined`, query dispatch и точно именувания block-warning renderer. |
| Заковани функции | Scorer/comparator, `selectResult`, click/Enter navigation, detail fetch, exact coordinates и останалите функции/селектори остават забранени. |
| Flag off | „При `ADDRESS_PATH_V2=false` DOM, backing identity, selection и failure/race поведението са byte-equal на подписания post-ЛОТ-2 baseline.“ |
| Flag on | „Позволени са само поименно описаните differential G3 разлики; всяка друга разлика е STOP.“ |

| G3 повърхност | Единствено разрешена разлика |
|---|---|
| №18 | Сгъване само на members на подписана `pb` група до подписания representative. |
| №3 | Поява на същия label/g при различен точен pin; относителният ред на старите identities се пази. |
| №15 | Само exact подписан diff при задействан fallback; контролите `кв. Чайка`/`к.к. Чайка` са отделни. |
| №16 | Само deterministic meta text; rank, identity, click, Enter и navigation не се променят. Anchor се инжектира наново преди всяка headless заявка; отделна no-fix серия очаква нула суфикси. |
| №17 | `R` = пълният ranked набор след physical/block grouping; `D=dedupeV2(R)`; `V=D.slice(0,limit)`; **`N=|D|−|V|`**. Tail няма `data-idx`, не влиза в `currentResults` и не е selectable. |
| Корпус | Фиксирани payload hashes, browser/viewport, cache state, WGS84 anchor и старите девет G3 заявки; плюс 3470-row engine corpus и целеви `pb`, >200 m, Чайка, bare-block/entrance и no-GPS случаи. |
| DOM доказателство | Full `outerHTML` + backing identity, pin, `g`, nav coordinates, popup title и selection side effects. |

## 5 · ЛОТ 2 и ред 806

| Мярка/механика | Резултат | Какво чупи |
|---|---:|---|
| Текущи entries | 86 232 | — |
| `label` only | 42 937 | Включва 970 parcel rows без `display_id`. |
| `display_id` only | 43 099 | Текущата стъпка 2. |
| И двете | **196** | Всички са `mf`: 52 секции + 144 входа. |
| Label-bearing `address/mf`, върху които реално действа „display винаги, label никога“ | **42 163** | Много повече от посочените 31 916 латински етикета. |
| По-къси резултати | **11 813** | Предложеният gate „нищо по-късо“ пада предварително. |
| ≤3 знака без букви | **17** | Примери: `ж.к. Бриз, бл. В → 2`, `atanas dalchev\|1 → 1`, `priboi 31 va\|10 → 10`. |
| Размер | 11 242 756 → 10 659 864 B | −582 892 B raw, но само **−20 223 B gzip**, не реална mobile печалба ~0,7 MB. |

| Тежест | Атака |
|---|---|
| **БЛОКЕР** | Махането само на `&& !o.label` от [builder:806](/C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs:806) единствено добавя `display_id`; UI продължава да предпочита `label` в [baseAddressLabel](/C:/git/Fire_Varna/index.html:4878), следователно payload-ът расте и видимото поведение не се променя. |
| **БЛОКЕР** | За реално махане на label е нужна късна pass след F3 и останалите промени до ред 922. F3 нарочно добавя block identity след ред 806 и пази `display_id` в [builder:826](/C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs:826). |
| **ГОЛЯМА** | Стъпка 1 използва `prettyKey`; стъпка 2 връща суров `normalized_address`. Днес няма `\|` в `address_rows`, но бъдещият gate трябва да го забранява. |
| **БЛОКЕР** | Промяната на label не е presentation-only: [dedupeDisplayRows](/C:/git/Fire_Varna/index.html:5104) дедупира по показвания текст и може да смени брой, identity и top-8. |
| **БЛОКЕР** | In-memory трансформираният payload минава текущия publish validator с **0 violations**. Значи gate-ът проверява privacy/schema, но не четимост. |

| Необходим gate преди ЛОТ 2 | Изискване |
|---|---|
| Ledger | Exact old→new ledger за всички засегнати private entry identities. |
| Field invariants | `kind/pin/tk/qtk/dtk/stk/btk/g/en` и ranking inputs са byte-equal; `display_id` е валиден и очакван. |
| UI differential | Подредба, backing identities, nav coordinates и selection са равни; само подписаните текстови промени са разрешени. |
| Quality | Fail при празен, letterless/≤3, загубен блок/номер/вход или по-малко информативен надпис. |
| F3 | 196-те block labels се запазват, освен ако поименно не е подписана по-добра замяна. |
| Governance | ADR 006 трябва да е изменен преди този лот, защото D12 изрично заковава `search_index.json`. |

## 6 · `pb`: privacy и churn

| Тежест | Находка | Какво чупи |
|---|---|---|
| **БЛОКЕР** | `ALLOWED_ENTRY_KEYS` допуска само името на полето; regex има единствено за `g` в [publish gate:81](/C:/git/Varna_buildings/js/test_fire_varna_publish_gate.mjs:81). След добавяне в allowlist стойност `pb:"not-a-bd-key"` би дала 0 violations. | Няма доказателство, че стойността е opaque или валидна. |
| **БЛОКЕР** | Суровият `physical_building_id` е `min(member cadnum)` в [physical_building.py:176](/C:/git/Varna_buildings/src/pipeline/physical_building.py:176), тоест кадастрален идентификатор. Rename към `pb` не го обезличава. | Raw rename изтича private identity; обикновен SHA е enumerable. |
| **ГОЛЯМА** | `FORBIDDEN_SUBSTRINGS` в [publish gate:101](/C:/git/Varna_buildings/js/test_fire_varna_publish_gate.mjs:101) хваща буквения ключ, не семантиката на стойността. | „Пакетът не съдържа низа physical_building“ е недостатъчен privacy gate. |
| **БЛОКЕР** | Snapshot: **483 stamped rows / 198 groups**, 420 `mf` + 63 `address`, без entrances/parcel. Исторически вече има churn от 473/194 към 483/198. | Split/merge може да смени group key и навигационния representative без аларма. |

| Подписуем договор | Точно правило |
|---|---|
| Публичен ключ | `pb = HMAC-SHA256(secret, "vpb1|"+private_pbid)`, например `b` + 16 lowercase hex. Отделен domain от `g`; не bare hash. |
| Validator | Отделен `PB_KEY_RE`, type/shape check, dotted-cadnum poison fixtures и exact cardinality/coverage. |
| Representative | Public-safe `pbr: pb→_ord` или marker върху representative row, с referential-integrity gate. |
| Snapshot gate | Точно 483 rows/198 keys, само очакваните 420 `mf` + 63 `address`, никога `en` или parcel. |
| Determinism | Два билда с еднакви входове са byte-identical. |
| Churn | Сравняват се private сортираните member sets. Unchanged set ⇒ същия public key; split/merge/member migration/create/delete/representative change ⇒ STOP до подписан migration manifest. |

## 7 · Гейтовете на ЛОТ 1

| Подточка | Тежест | Атака | Подписуем gate |
|---|---|---|---|
| Family count | **БЛОКЕР** | P7 класифицира вече експортирани `zone` низове; суровият регистър няма независимо `family`. Има **7 unmatched zones / 94 rows**: Аспарухово/Галата 1, Виница/север 3, Изгрев 1, к.з. Прибой 1, к.к. Св. Константин 40, район Одесос 42, район Приморски 6. | Подписан независим manifest `registry_row_id → {kind,family,status}`. Всеки ред е точно `placed(pin)` или `unplaced(reason)`; output+board трябва да са биекция с manifest-а. |
| Board срещу search count | **БЛОКЕР** | v1 казва, че редът може да е само „без положение“ на борда, но после изисква query count да е равен на всички регистрови редове. | Search count може да е равен само на `placed`; unplaced трябва да се отчита отделно или да се проектира като изрично ненавигируем UI ред. |
| PiP/≤10 m | **БЛОКЕР като acceptance gate** | Final exporter-ът проверява само име/kind/src/BBOX/дубликати в [export_fire_varna_places.py:544](/C:/git/varna_3d/src/export_fire_varna_places.py:544). Final PiP gate няма. Аритметичен exterior centroid може да е извън вдлъбнат polygon. | В EPSG:32635: `distance(point, polygon) ≤ 10.0 m`; `0` означава inside/covered. За генериран пин — `representative_point()`. Negative fixture на >10 m задължително пада. Ако изискването е строго „върху“, то трябва да е `polygon.covers(point)`, не ≤10 m. |
| Reference преди изпълнение | **БЛОКЕР** | Reference е 103 заявки = 62+10+31, но `recall_sweep.py` main overwrite-ва каноничния файл в [recall_sweep.py:1641](/C:/git/Fire_Varna/scratch/places_search/recall_sweep.py:1641). Exact diff не съществува преди кандидатните данни. | G1a: report-only/in-memory симулация върху frozen candidate overlay, без overwrite; Петър подписва exact ordered 103-row diff. G1b: старият reference първо трябва да падне; update в отделен commit; новият после минава. |

## 8 · Какво не бива да се подписва

| Неподписваемо твърдение във v1 | Причина | Условие за нов подпис |
|---|---|---|
| „Решения 1+2 сменят 3/103“ | Минимум 4/103; при широк `old_names` — минимум 5/103. | Exact M1/A3/alias правила и пълен reference diff. |
| „Обща площадка със стабилен регистров ред“ | Такъв стабилен ID не е дефиниран. | Persistent `place_id/site_id` registry и cross-file `<5 m` gate. |
| „Само ЛОТ 3 иска ADR“ | ЛОТ 2 променя закован `search_index.json`. | ADR amendment преди ЛОТ 2. |
| „ЛОТ 2 = един ред, ~−0,7 MB, без влошени етикети“ | Един ред не маха labels; реалният ефект засяга 42 163 rows, скъсява 11 813 и дава 17 нискоинформативни стойности. | Късна селективна pass, F3 carve-out и подписан quality ledger. |
| „`pb` в allowlist + липса на private substring доказва privacy“ | Няма value shape/provenance check; липсва representative contract. | HMAC, `PB_KEY_RE`, poison tests, `pbr` и partition churn gate. |
| „18 стеснява 545-те преди 3“ | Текущо не разрешава нито една от 547-те далечни групи. | Решения 3 и 18 да се оценят независимо върху един и същ frozen snapshot. |
| „Текущият G3 фиксира центъра“ | Geolocation е denied, кликовете сменят оперативната котва, reset между заявките няма. | Fixed-anchor и no-fix серии с reset преди всяка заявка. |
| „Tail е само renderer промяна“ | Точният total е изгубен преди renderer-а. | Full-set dedupe преди cap и изрична позволена G3 ranking разлика. |
| „Exact family count“ | Denominator-ът се извежда от същия речник/изход, който се проверява; unplaced rows противоречат на search count. | Независим registry-family manifest и отделни placed/unplaced инварианти. |
| „Reference се подписва преди изпълнение“ | Без candidate overlay няма числа; текущият main презаписва доказателството. | Предварителна report-only симулация и двустепенен fail→update→pass gate. |
| **Финално** | **ЛОТ 1, ЛОТ 2 и ЛОТ 3 не трябва да се подписват в текущия вид.** | Нова v2 с горните договори, измерен exact diff и ADR преди първата архитектурна промяна. |

| Режим на проверката | Състояние |
|---|---|
| Файлова система | Само четене; няма редакции, комити или превключване на клон. |
| Repository | `main`, HEAD `1ca8186`; предварително наличният dirty state е останал непроменен. |
| Опасен reference run | `recall_sweep.py main()` не е пускан. |
