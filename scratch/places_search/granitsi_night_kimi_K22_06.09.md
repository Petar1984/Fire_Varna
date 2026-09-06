kimi version 0.34.0
• I need to analyze files. Let me read the relevant files first. Working directory is a temp copy of C:/git/Fire_Varna. Files to read:

  - docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md
  - docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md
  - docs/decisions/010_signed_quarter_boundaries.md
  - scratch/places_search/wikimapia_frozen_measure_06.09.md
  - scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md

  Read them in parallel.

• Прочитам целевите и контекстните файлове паралелно.

• Now I need to write the К22 verdict (оборване) with lens: ДАННИ, ЛИЦЕНЗ, КОНФЛИКТИ. Questions (а)-(е), verdict ГОДНО/НЕГОДНО for А and Б separately, named fixes, ≤1400 words, every claim with file:line or URL, in Bulgarian. Cite paths relative to C:/git/Fire_Varna root.

  Let me work through each question.

  (а) Б0 т. 1 (нощен план :107): scheme for imported geometry — 7 D1 fields become null (drawn_by, drawn_at, basemap, viewport, visible_layers, screenshot_sha256, approval_digest). Is this honest w.r.t. D1/D2 and К21, or license laundering under another name?

  D1 (ADR :38) requires all 21 fields; "липсващо поле = STOP". Amendment №2 §4 (:93) already prescribes drawn_by/drawn_at/viewport/screenshot_sha256 = null for imported geometry, with mutual exclusivity gate — so Б0 т.1 is consistent with the amendment's §4 and §7 т. 2 (ревизия, :125). The plan explicitly declares it as "промяна на D1, обявена" and requires Petar's signature. That is not laundering — laundering would be hiding the nulls or relabeling source. Key honesty checks: license laundering = relabeling origin (e.g. declared_local_knowledge, rejected in §3.7 :67). Б0 т.1 keeps source: "wikimapia" honest, licence label per К21 condition 3–4 (Н1 :61 quotes the licence string with "версия непосочена"). witnesses[] gets real values. One wrinkle: approval_digest = null — D1's digest binds approval to geometry; replacing it with "signed_by valid via plan signature by sha of decisions" (Б0 т.8) is a declared mechanism. Potential issue: approved_at = decided_at from decisions — the decisions file is agent_committed_proba by Claude Architect, not Petar; but Б0 т.8 addresses signature by sha. Also `decided_by` field in decisions is "Petar via Claude Architect" per frozen measure :48 — the provenance chain is honest as long as the signature happens. Also note: "7 полета стават null" — actually list has 7 fields: drawn_by, drawn_at, basemap, viewport, visible_layers, screenshot_sha256, approval_digest. D1's set is 21 fields; amendment §4 (:93) names only 4 as null (drawn_by/drawn_at/viewport/screenshot_sha256) — Б0 т.1 adds basemap, visible_layers, approval_digest. approval_digest null is new and weaker than amendment — but replaces with sha-chain of decisions; must be named. Verdict on (а): honest, provided it's signed (it is gated on Б0 signature) and the delta vs amendment §4 is declared. Small fix: name the three extra nulled fields explicitly in the plan as deviation from amendment §4.

  (б) Б0 т.3 (:109) Mladost 2 from OSM axes, ODbL + т.5 (:111) one quarter_attribution map for Wikimapia and ODbL — compatible with ODbL §4.3 (produced work) and ToS §1.G in one public row?

  ODbL §4.3: Produced Work must carry notice "Contains information from DATABASE(s) which is licensed under the ODbL" or similar, reasonably calculated to make recipients aware. Actually ODbL 1.0 §4.3: "If You Publicly Use a Produced Work, You must include a notice associated with the Produced Work reasonably calculated to make any Person that uses... aware that Content was obtained from the Database...". OSM attribution guideline: "© OpenStreetMap contributors". ToS §1.G of Wikimapia requires link to original object URL + "Wikimapia.org" link.

  Б0 т.5's UI string: „квартал по Wikimapia.org · обектът" — only for codes with entry in the map; map is source-independent {code:{src,url,label,licence}}. So for mladost2 the entry would be src: osm, label „© OpenStreetMap contributors". Is that compatible? ODbL §4.3 requires attribution notice for Produced Work. The published row {name, code, src} for mladost2 — name "Младост 2" is a registry name (not OSM data; OSM has no Mladost 2 polygon — actually the geometry is derived from OSM ways: street axes). The polygon is derived from OSM database → the resulting boundary is a Derivative Database; but geometry is never published (private). The produced work: the published assignment "this place is in Mladost 2" — arguably produced work from the derivative database. ODbL §4.3 demands attribution on produced works. The quarter_attribution map can carry {src:"openstreetmap", url: osm.org/copyright, label: "© OpenStreetMap contributors"} — mechanically the same map works. Potential issue: the UI string in т.5 is hard-coded „квартал по Wikimapia.org · обектът" — if rendered for mladost2 with the map entry for OSM, fine, but the plan says "UI низът: ... само за кодове с запис в картата" — the string template mentions Wikimapia; needs label-driven rendering, not a fixed Wikimapia string. That's a named fix. Compatibility verdict: compatible IF label comes from map (not fixed string) and OSM attribution links osm.org/copyright. One public row showing name+code+src for both sources is fine because geometry never published and attribution notices coexist. Also note §1.G applies only to Wikimapia rows; ODbL §4.3 only to OSM-derived rows. No conflict.

  (в) Б0 т.4 (:110) district from our district.code (375/375 agreement) — does it avoid G22 or bypass it?

  G22 (ADR :136): gates Feature with source agkk_inspire_gn — requires _meta.agkk_terms populated. G22 is about AGKK Geo_Names features in quarters_signed. Writing district from our own district.code doesn't use AGKK data — it's our data, validated 375/375 against AGKK AU5 (ADR :32, measured). G23 is the control gate (AU5 ↔ district.code agreement). So using our district code avoids G22 legitimately — it doesn't consume AGKK licensed data, it consumes our own field which merely agrees with AGKK. This is avoidance in the legitimate sense (не използваш лицензираните данни), not circumvention. But note: the measure "375/375 съгласие" itself was computed against AGKK AU5 — fine as verification. Also §4 запрет "низът 10135 в публична доставка" (:88) — district codes are verbal from DISTRICT_CODES, not 10135. OK. Verdict: избягва законно; condition: G23 stays as control gate and if agreement breaks → STOP (D0 :36 says "всяко бъдещо разминаване = STOP"). The plan Н1 :61 says "за всеки кандидат кой nationalcode го съдържа" — that's measure in private, allowed per §4 ("в частния провенанс и в мярката е позволен").

  (г) §7 conflict ledger and principle "координатата решава, името е свидетел" — is there a conflict class this rule resolves wrongly?

  Examples asked: pin on wrong building; resort/quarter with one name; boulevard named after quarter. Cases:

  1. Pin on wrong building: if the coordinate itself is wrong (pin placed on wrong building), coordinate decides wrongly. Н2-0 derives coords from site_id/kais_i representative point of a body in varna_buildings_3d.geojson (:66) — if the linkage is wrong, the coordinate is a wrong witness treated as judge. But: the ledger is measure-only, resolution column doesn't overwrite; D6 disputed is ledger-only. The principle governs assignment for empty rows (Б2). A wrong pin writes a wrong quarter into an empty row — and the rule has no detector for "pin is wrong" except edge bands. So yes: class "грешен пин" is resolved wrongly (silently written, not disputed). Named fix: witness-agreement check — if written address string (REG/KAIS quarter field) disagrees with polygon, dispute even for empty quarter? Actually empty quarter means no written witness. For 159 rows with no channel id there is no other witness — coordinate is the only evidence; risk acknowledged.

  2. Resort/quarter with one name: Чайка кв vs кк — two codes one name; the coordinate actually resolves this correctly (coordinate decides which polygon). Fine. But "Комплекс Чайка" ambiguity was matcher issue; coordinate rule is good here.

  3. Boulevard with quarter's name: "бул. Владислав Варненчик" ≠ кв. Владиславово — §7 explicitly parses this (:133): address string is a witness; if a place's address is the boulevard, the string witness says "Владиславово" wrongly; coordinate rule correctly overrides. Good — this class the rule resolves correctly BECAUSE names lie.

  The genuinely wrong class: coordinate error itself (wrong pin, wrong representative point of building body, e.g. body centroid outside the actual parcel near edges). Also systematic offset in web/varna_buildings_3d.geojson. Another class: MultiPolygon edge/buffer — handled by edge_pending. Also: вложени полигони без родство → disputed, fine. So answer: yes — the class where the coordinate is the false witness (wrong pin/centroid), plus "курорт/квартал с едно име" is actually fine for the coordinate rule but bad for name-witness (handled). Also "parent_vs_child" where undeclared — handled as disputed.

  Also: representative point of body ≠ entrance/address point — for a place near a border the centroid may land in the wrong quarter while address is right; but D6 says written quarter never changes → disputed only, no overwrite; for empty rows, wrong write possible. Mitigation: трите ленти 50/100/250 m and edge_pending catch border cases partially.

  (д) Б2 (:122): "само празен квартал се пише; без полигон → районът" — can DISTRICT_FALLBACK overwrite something that per D6 must stay empty, or hide a dispute?

  Б0 т.4 (:110): fallback writes quarter = {name: district name, code: verbal code from DISTRICT_CODES, src: DISTRICT_FALLBACK}. Concerns:

  1. D6 (:48): "Полигон-местност никога не пълни quarter — classify(code) == field". District codes are in DISTRICT_CODES (locality class? index.html :6315) — writing district name into the quarter field changes the class semantics: quarter field now holds a district-class value. D3 publishes quarter: {name, code, src} — row keys stay 13/17, but quarter.code would be a district code — QUARTER_BY_SRC test and LOCATION_COUNTS {quarter 20, district 5, locality 5} pin counts (D13 :62) — writing districts as quarters changes quarter counts → breaks pinned expectations unless pins updated (planned in D13 delivery, but this is a semantic change needing explicit approval). Also "само празен квартал се пише" — fallback writes into empty quarter, ok. But can it hide a dispute? D6: dispute written≠polygon is ledger-only, row untouched — fallback only writes empty rows, so no overwrite of written. But: a place with written quarter=null that lies in a disputed/edge zone? Rule: "без полигон → районът" — if the place is in NO polygon, there's no dispute by definition of polygons. However: pin_outside_all could itself be a conflict signal (pin wrong). Fallback writes district confidently, masking the fact that pin is outside all polygons (which §7 lists as conflict_kind pin_outside_all). If the pin is wrong, fallback legitimizes it silently in public data. Also places in deferred codes (Mladost 2, 16 undecided): "няма полигон → районът" — places inside Mladost area would get district instead of remaining empty pending decision → hides a deferred decision, and when Mladost 2 gets a polygon, the row is no longer empty → new polygon can't write it (само празен се пише) → fallback creates lock-in that blocks future signed polygon writes. That's a real defect: fallback write is treated as "written quarter" then protected by G17/D18? G17 protects written quarters in old ledger-blob; new fallback rows would become "written" for next versions → a future polygon for a deferred quarter cannot override a DISTRICT_FALLBACK. Named fix: fallback rows must stay revisable — mark src: DISTRICT_FALLBACK as lower precedence, allow signed polygon to overwrite fallback rows in a future version (or don't write fallback for codes pending decision). Also question whether fallback should be written at all vs district field. D6's declared deviation (К2): "падане до район би изтрило написан от по-силен канал квартал" — that was reason NOT to fall back for disputed rows; fallback only for empty is consistent.

  So (д): yes, two risks: (i) locks deferred/undecided areas into district values that block future polygon writes (G17/D18 protection of "written"), (ii) pin_outside_all conflict becomes invisible in public row. Fix: DISTRICT_FALLBACK rows excluded from "written" protection (revisable), and conflict ledger marks pin_outside_all.

  (е) ЧАСТ А: is there a measure that secretly changes data?

  Scan: Н0 pins — writes noshtna_pins_06.09.json, qa script; gate fixture does `git add -f` върху копие в еднократно worktree (:58) — that's a deliberate test write in a throwaway worktree, declared. Н1: writes candidate file (ignored, not staged) + two src scripts in varna_3d — commits them ("малки, обратими комити"). Hmm: ЧАСТ А says "but шест лота, които четат" (:139) — yet Н0, Н1, Н3-а commit files. They commit measure scripts/outputs, not data. Н2: reads blob, doesn't touch ledger; gates check sha256 identical before/after. Н3-а: adds test fixtures + fixture json to Fire_Varna tests — writes tests, not data; but "фиксира ДНЕШНОТО поведение" — adding tests changes the repo state that gates see; declared. Н4: stdout only. Н5: report.

  Sneaky data changes? Check Н1: "parent от регистъра след явна стъпка дисплей→код с гейт" — reads registry, fine. Н2-0 reads place_identity.json, doesn't touch. One subtle: Н0 gate fixture requires a G29 gate that fails in a worktree — creating worktree writes .git metadata — declared, reversible. Another: Н3-а gate requires `python -m gates.run_gates` без червено — but today ahead 37 with unpushed; fine.

  Potential hidden change: Н1 commits `src/build_quarters_candidate.py` into varna_3d repo — ЧАСТ А was advertised as "нощ от мерки... шест лота, които четат" — committing code is a write, but declared in write-set table (:41-49). Not secret.

  One more: §0 червен ред 2 "Нула геометрия в проследен файл на Fire_Varna" — Н3-а fixture json `granitsi_fixtures_06.09.json` — must contain no coordinates; fixture parent_child uses mladost/mladost2 — registered relation; ok as long as no coords. Fine.

  Anything else secretly changing data: Н2's measure uses `base_rev` = exact commit — but §1 :32 says `_meta.base_rev` doesn't exist in today's ledger, D18/G17 read git show <base_rev>. Н0 pins base_rev — declared fix.

  Verdict: ЧАСТ А — ГОДНО (measures only, all writes declared in write-sets, data hashes gated before/after). ЧАСТ Б — conditionally: I'd say ГОДНО с поименни поправки or НЕГОДНО? Given fixes needed: (а) declare the 3 extra null fields; (б) label-driven UI string instead of fixed Wikimapia string; (д) fallback revisability + deferred-area exclusion. These are substantive but fixable; verdict could be "ГОДНО при поименните поправки". The task asks ГОДНО/НЕГОДНО за А и за Б поотделно, с поименни поправки. I'll give А = ГОДНО; Б = ГОДНО при условие (or НЕГОДНО до поправки?). The fallback lock-in (д) is a real data-semantics defect that could persist wrong values — I'd call Б = НЕГОДНО в текущия вид, годно след трите поправки. Let me be decisive: Б: НЕГОДНО за подпис в сегашния вид — три поименни поправки, after which годно.

  Word limit ≤1400. Write in Bulgarian, cite file:line. Paths relative to C:/git/Fire_Varna.

  Let me draft.

  Citations shorthand:
  - Нощен план: docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:N → cite as НОЩЕН:N maybe with full path at least once.
  - Амандамент: docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:N
  - ADR: docs/decisions/010_signed_quarter_boundaries.md:N
  - Мярка: scratch/places_search/wikimapia_frozen_measure_06.09.md:N
  - К21: scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md:N
  - ODbL URL: https://opendatacommons.org/licenses/odbl/1.0/ §4.3

  Check К21 file lines: conditions listed at :49-57; §1.G analysis :61-67. Amendment ToS §1.G quote at :60. ToS §1.G text: ":60" in amendment (§3.5). wikimapia_terms file not read here but quoted in amendment.

  ODbL §4.3 text: "You must include a notice... reasonably calculated to make any Person aware that Content was obtained from the [Database]... and that it is available under this License" — cite URL.

  Count words — aim ~1100-1300.

  Structure:
  - Резюме/присъди up top
  - (а)...(е)
  - Поименни поправки list

  Write the reply now. No tool calls needed — pure analysis, and I'm forbidden from creating files anyway. The verdict is delivered as text reply (user said "САМО АНАЛИЗИРАЙ... опиши вместо да направиш"). The plan file asks verdicts to be recorded in files but I must not write. So deliver in reply.

• # К22 · Оборване на нощния план — леща ДАННИ / ЛИЦЕНЗ / КОНФЛИКТИ

  **Присъда: ЧАСТ А — ГОДНО. ЧАСТ Б — НЕГОДНО за подпис в сегашния вид; става годно с три поименни поправки (П1–П3 по-долу).**

  Позовавания: `нощен` = docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md, `ам2` = docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md (рев. 2б), `ADR` = docs/decisions/010_signed_quarter_boundaries.md, `мярка` = scratch/places_search/wikimapia_frozen_measure_06.09.md, `К21` = scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md.

  ## (а) Б0 т. 1 — честна схема, не пране, с една непълнота

  Лицензно пране би било преименуване на произхода — точно това ам2 §3.7 (`ам2:67`) отхвърля (`declared_local_knowledge` „сменя етикета, не произхода“), а нощният план го затваря с гейт „Feature със `source: "declared_local_knowledge"` → ✗“ (`нощен:63`). Б0 т. 1 (`нощен:107`) прави обратното на пране: `source` остава честно `"wikimapia"`, лицензът е дословно този от К21 условие 4 (`К21:36`, пренесен в `нощен:61` — „версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели“), `witnesses[]` носи реален обект с `raw_response_sha256`, а null-ването е **обявено като промяна на D1 и оставено на подпис**. Също е наследено от ам2 §4 (`ам2:93`), не измислено нощта.

  Непълнотата: ам2 §4 null-ва **четири** полета (`drawn_by/drawn_at/viewport/screenshot_sha256`); Б0 т. 1 добавя още три — `basemap`, `visible_layers`, **`approval_digest`**. Последното не е козметика: дайджестът е механизмът, с който D1 (`ADR:38`) връзва одобрението към байтовете. Заместникът е веригата „подпис по sha на решенията“ (Б0 т. 8, `нощен:114`), която е работеща, но разликата спрямо ам2 §4 никъде не е назована като отклонение. Второ: `approved_at = decided_at` идва от файл, чието състояние самият план нарича `agent_committed_proba (b6e627d, Claude Architect)` (`нощен:61`), а подписите в решенията са „Petar via Claude Architect“ (`мярка:48`) — веригата става честна едва след Б0 т. 8, което планът правилно прави предусловие. → **П1: в Б0 т. 1 да се запише изрично „делта спрямо ам2 §4: +`basemap`, +`visible_layers`, +`approval_digest`; дайджестът се замества от sha-веригата на т. 8“.**

  ## (б) Б0 т. 3 + т. 5 — съвместими, но UI низът е грешно кацнал

  ODbL §4.3 иска при Produced Work бележка, „reasonably calculated“ да уведоми получателя, че съдържанието е от базата и под какъв лиценз е (https://opendatacommons.org/licenses/odbl/1.0/ §4.3); ToS §1.G иска връзка към обекта + „Wikimapia.org“ с връзка (`ам2:60`; анализът, че §1.G е договорна и независима от CC-въпроса — `К21:63-67`). Една публична редица може да носи и двете: геометрията никога не се публикува (`ADR:42`, `ам2:48`), а атрибуциите са per-код в картата `{code:{src,url,label,licence}}` (`нощен:111`) — за `mladost2` записът е `{src: openstreetmap, url: osm.org/copyright, label: "© OpenStreetMap contributors"}` и удовлетворява §4.3; уикимапийските кодове носят своя §1.G ред. Няма клауза, която да забранява съжителството.

  Дефектът е механичен: UI низът в Б0 т. 5 е **хардкоднат** — „квартал по Wikimapia.org · обектът … само за кодове с запис в картата“ (`нощен:111`). Ако картата носи и ODbL (което е смисълът ѝ), низът трябва да се рендерира от `label`/`url` на записа, не от фиксиран низ с „Wikimapia“ — иначе Младост 2 или ще покаже Wikimapia-атрибуция върху OSM данни (лъжа), или няма да покаже нищо (пропуск на §4.3). → **П2: низът се строи от `label`+`url` на записа в `quarter_attribution`; фикстура: код с `src: openstreetmap` → показва OSM низа.**

  ## (в) Б0 т. 4 — избягва G22 законно, не го заобикаля

  G22 (`ADR:136`) гейтира Feature със `source: "agkk_inspire_gn"` — тоест **употреба** на АГКК геометрия. Б0 т. 4 (`нощен:110`) не внася нищо от АГКК: пише нашето `district.code`, чието съвпадение 375/375 с АГКК AU5 е **проверка**, не извличане (`ADR:32`). Разликата „избягване/заобикаляне“ е точно това: не консумираш лицензирания актив, а ползваш собствено поле, валидирано срещу него. Две условия пазят честността и са в плана: G23 остава контролен гейт със STOP при бъдещо разминаване (`ADR:36`), и низът `10135` е забранен в публичната доставка, позволен само в частния провенанс и мярката (`нощен:88`) — словесните кодове идват от `DISTRICT_CODES` (`нощен:29`). Чисто е.

  ## (г) „Координатата решава“ — да, има клас, който решава грешно: грешният пин

  Принципът (`нощен:7`, `:133`) е правилен за класовете, в които **името** лъже: булевард с името на квартала („бул. Владислав Варненчик“ ≠ кв. Владиславово, изрично парсиран `нощен:133`) и курорт/квартал с едно име (Чайка кв/кк, `мярка:16`) — там координатата е единственият надежден свидетел. Но правилото третира координатата като непогрешима, а тя самата е производна: Н2-0 я извежда от `site_id`/`kais_i` → представителна точка на тяло в `web/varna_buildings_3d.geojson` (`нощен:66`). Класове, които губят:

  - **Пин/центроид на грешна сграда или грешна връзка `kais_i`** — за 159-та реда без нито един канален свидетел (`ADR:24`) няма втори глас; грешната координата пише грешен квартал в празен ред и леджерът го отбелязва най-много `none`.
  - **Представителна точка ≠ адресна точка край граница** — центроидът на тялото може да падне в съседния полигон; лентите 50/100/250 m (`нощен:69`) хващат само близост до ръба, не и системен offset.

  Смекчаващо: за **написаните** редове правилото не може да навреди — D6/D18 правят спора леджер-само (`ADR:48`, `:72`). Рискът е само при писане в празно (Б2). → **П3: ред, чийто пин е `pin_outside_all` или пада в полигон, несъвместим с **всеки** наличен низов свидетел (вкл. кадастрален `quar` на тялото), отива в `disputed`, не в `written`, дори кварталът да е празен.**

  ## (д) DISTRICT_FALLBACK — да, може да скрие спор и да заключи отложено решение

  Два конкретни механизма в Б0 т. 4/Б2 (`нощен:110`, `:122`):

  1. **Заключване на отложените.** Местата в зони с `deferred` код (16-те без решение, Ваялар, Младост 2 до подписания ключ) нямат полигон → fallback им пише район. При следваща версия с полигон редът вече не е празен, а Б2 пише „само ПРАЗЕН квартал“ и G17/D18 пазят написаното (`нощен:122`, `ADR:72`) — **fallback-стойността блокира бъдещия подписан полигон**. Това е презапис на нещо, което по D6 трябва да остане отворено.
  2. **Скриване на спор.** `pin_outside_all` е клас конфликт в собствения леджер на плана (`нощен:133`); fallback го превръща в чист публичен ред `{район, DISTRICT_FALLBACK}` — спорът изчезва от потребителското око точно когато е най-подозрителен (възможно грешен пин).

  Допълнително: писането на районен код в полето `quarter` мърда пиннатите броячи `LOCATION_COUNTS {quarter 20, district 5…}` и `QUARTER_BY_SRC` (`ADR:62`) — планирано е в доставката на D13, но семантичната промяна („quarter понякога е район“) иска изрично „да“, не само преизмерени пинове. → **П3 включва и: fallback-редовете носят `src: DISTRICT_FALLBACK` и се **изключват** от защитата „написаното не се променя“ — подписан полигон в бъдеща версия може да ги замести; зони с `deferred`/`registry_pending` код не получават fallback тази нощ.**

  ## (е) ЧАСТ А — не, няма мярка, която тайно променя данни

  Проверих лот по лот срещу write-set таблицата (`нощен:41-49`): Н2/Н4 са read-only с sha256-преди/след върху леджера и данните (`нощен:69`, `:79`); Н2-0 пише само в `scratch/` (`нощен:66`); комитите на Н0/Н1/Н3-а/Н5 са скриптове, фикстури и доклад — всички назовани в таблицата. Единственото писане извън очевидното е `git add -f` в **еднократно worktree** като отрицателна фикстура (`нощен:58`) — обявено и обратимо. Твърдението „шест лота, които четат“ (`нощен:139`) е леко пресилено (три лота комитват код/документи), но нищо не е скрито — write-set-овете са изчерпателни и одиторът ги сверява (`нощен:82`).

  ## Поименни поправки (условие за „ГОДНО“ на Б)

  - **П1** (Б0 т. 1): изрична делта спрямо ам2 §4 — трите допълнителни null-полета и заместването на `approval_digest` с sha-веригата от т. 8.
  - **П2** (Б0 т. 5): UI низът се рендерира от `label`/`url` на записа в `quarter_attribution`; отрицателна фикстура за OSM код с Wikimapia-низ.
  - **П3** (Б0 т. 4/Б2): DISTRICT_FALLBACK е заместим от бъдещ подписан полигон (извън D18-защитата), не се пише в зони с `deferred`/`registry_pending`, и `pin_outside_all`/конфликт с кадастралния `quar` → `disputed`, не писане.

  ЧАСТ А не зависи от П1–П3 и е **ГОДНО** за подпис довечера.

To resume this session: kimi -r session_0ad573c7-3c66-4018-be9f-5713def40830
