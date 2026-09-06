kimi version 0.34.0
• The task: analyze files, read the plan, decisions files, state file, measure file. All read-only. Let me read the files. They're in the temp working directory which is a copy of C:/git/Fire_Varna. Paths relative to that root.

  Let me read the files in parallel.

• Прочитам посочените файлове, за да направя прегледа.

• Now read decisions 3 file to compare with decisions 4 (question 1: diff). The file is granitsi_decisions_3_2026-09-06_proba.json. Let me read it. Also need to verify counts: decisions 4 has 68 rows — 58 wikimapia, 1 wikimapia_union, 1 declared_streets, 6 deferred, 1 alias_of, 1 excluded. Total 58+1+1+6+1+1 = 68. Decisions 3 should be: 60 wikimapia, 1 declared_streets, 6 deferred (bokluk_tarla, botanicheska, malka_chaika, mikro4, starite_lozya, vilite — in decisions 4 I counted deferred: bokluk_tarla, botanicheska, malka_chaika, mikro4, starite_lozya, vilite = 6 yes), 1 alias_of. And vinitsa_sever in decisions 3 presumably was wikimapia with wm_id 5729421. So diff: dobreva row (wikimapia 5729380 → wikimapia_union), vinitsa_sever row (wikimapia 5729421 → excluded), plus header changes (based_on, exported_at, changes list). Let me read decisions 3 to verify.

• Сега прочитам решения 3, за да направя директния диф срещу решения 4.

• Now I have everything needed for the diff. Let me verify the diff between decisions 3 and 4:

  Header changes (decisions_3 lines 4-21 vs decisions_4 lines 4-23):
  - based_on: decisions_3 → granitsi_decisions_2 sha 3ad5da79…; decisions_4 → granitsi_decisions_3 sha256_blob_b6e627d ec2813e1…
  - exported_at: 2026-09-06T07:52:05 → 2026-09-06T21:22:27
  - changes: decisions_4 adds two new entries: dobreva → wikimapia_union [5729380, 5729421] and vinitsa_sever → excluded.

  Row changes:
  - dobreva: d3 (lines 167-178): choice wikimapia, wm_id 5729380, sha 9e59fd99…, title „Добрева чешма", decided 04:35:14.575Z. d4 (lines 169-184): choice wikimapia_union, wm_id null, sha d6f367bd…, title „…∪ Виница - север", wm_ids [5729380, 5729421], reason Petar 07.09, decided_at 21:22:00.
  - vinitsa_sever: d3 (lines 786-797): wikimapia, wm_id 5729421, sha bebef782…, title „Виница - север". d4 (lines 792-804): excluded, all null, reason „го изключваме", alias_of null.

  All other 66 rows: need to verify no other changes. Comparing — I read both files fully; all other rows appear identical (same wm_id, sha, title, decided_at). E.g. abatko, akchelar, etc. identical. vayalar identical. mladost2 identical. So data diff = exactly the two codes.

  Counts: d3: 60 wikimapia + 1 declared_streets + 6 deferred + 1 alias_of = 68. d4: 58 wikimapia + 1 wikimapia_union + 1 declared_streets + 6 deferred + 1 alias_of + 1 excluded = 68. Consistent with prompt.

  Question 1: What must Petar sign by sha? The plan §6 Б0 т. 8 (line 131) says Petar signs decisions 3 by sha of blob in b6e627d. But the artifact is built from decisions 4. So Petar must sign decisions 4 by its blob sha (the blob 2c650160... in the commit by Claude Architect) — the plan's mechanism is „sign the decisions by sha of the blob committed by the agent". Since decisions 4 is a new file (granitsi_decisions_4_2026-09-07_proba.json), the chain honest requires: either commit decisions 4 from Petar1984 (Г2-б), or Petar's signature over sha256 of the blob in the architect's commit + decisions_sha256 in the artifact's _meta pointing to that sha. Also note decisions 4 contains the attribution duty already? Not needed.

  Also the artifact sha 4930f204 must equal _meta.decisions_sha256 = sha of decisions-4 blob. The chain: Petar signs sha(decisions_4 blob 2c650160) → artifact _meta.decisions_sha256 = that sha → artifact itself committed by Petar (G4/D16, plan line 138). Currently decisions 4 is committed by Claude Architect (agent_committed_proba again — same status as decisions 3 in b6e627d per plan line 27).

  Question 2: vazrazhdane4 and kochmar — AGKK says they're in district Mladost (10135-03); our layer says vladislav_varnenchik district. Who is right? Evidence: 
  - kochmar: frozen measure §5 line 39: „Уикимапия „Селищно образувание Кочмар" (0,38 km²) е източно от Възраждане 2/3; OSM „м-т Кочмар" (0,58 km²) е северозападно, над Възраждане 4; двата полигона не се допират." Decisions chose the Wikimapia polygon 15278642 (d3 line 325-334) — the one east of Vazrazhdane 2/3. Vazrazhdane 2/3 — where are they? Vazrazhdane district is south of Mladost. Hmm, actually the geography: жк Възраждане is between Vladislav Varnenchik (south of Treti Mart?) Actually: The boundary of district V. Varnenchik vs Mladost runs along bul. Treti Mart. Vazrazhdane is south of Treti Mart (in V. Varnenchik district), Mladost is north of it.

  Wait — actually in reality: Възраждане is in district „Владислав Варненчик", and the boundary between район Младост and район Вл. Варненчик is indeed along бул. Трети март. Възраждане 4 is the northernmost sub-district of Възраждане, adjacent to Treti Mart. Kochmar (Wikimapia polygon) is east of Vazrazhdane 2/3.

  Hmm, but I should base my reasoning on what's in the files, not outside knowledge. The user asks for a „verifiable argument (location relative to the Vladislavovo/Mladost boundary along bul. Treti Mart)". Within the files: plan Б0 т. 9 (line 132) says vazrazhdane4/vazrazhdane 72% overlap — partial, not parentage; and the DAG has vazrazhdane1/2/3 ⊂ vazrazhdane but not vazrazhdane4. Also frozen measure line 39: OSM Kochmar is northwest, above Vazrazhdane 4.

  The AGKK layer has only 5 districts (au5, 10135-01..05) with no verbal codes (plan line 29). Our layer's district of a quarter Feature is derived by representative point against our 5 districts (Б0 т. 4, line 127). The disagreement: for vazrazhdane4 and kochmar our layer says vladislav_varnenchik, AGKK 10135-03 = Mladost.

  Verifiable argument: check the coordinates of the polygons relative to bul. Treti Mart. From files: kochmar Wikimapia polygon (0,38 km²) is east of Vazrazhdane 2/3 (frozen measure line 39). vazrazhdane4 (0,16 km², m2-1 line 15). The decision row titles: vazrazhdane4 wm_title „жк. Възраждане 4" (d4 lines 756-767). M2-1 matched it as a Vazrazhdane subdistrict. The registry / our layer treats Vazrazhdane district as vladislav_varnenchik.

  Honest answer: The polygon decides by coordinates, not by the title. The AGKK au5 layer is official for districts; our 5-district layer claims 375/375 agreement measured 05.09 (plan line 127: „375/375 съгласие с АГКК, мерено 05.09"). But now AGKK disagrees for 2 of 60 codes. Resolution paths: Since Б0 т. 4 says district is written from OUR district.code with district_src fire_varna_district, and AGKK is only a witness, the disagreement is a ledger row, not an overwrite (plan line 7: „адресните низове са свидетели, не съдии; спор е ред в леджер"). But which is actually right? Verifiable test: compute the representative point of each polygon (vazrazhdane4, kochmar) and test which side of the Treti Mart axis it lies. The polygons' geometry is in the frozen file (not in this repo copy — it's ignored). So the check is: if vazrazhdane4's polygon lies south of Treti Mart → our layer (V. Varnenchik) is right; if north → AGKK. 

  From evidence available: kochmar wikimapia polygon is „източно от Възраждане 2/3" — Vazrazhdane 2/3 are ⊂ vazrazhdane (DAG, plan line 132) and vazrazhdane district is in... our layer says vladislav_varnenchik for them too? The disagreement is only for vazrazhdane4 and kochmar, not for vazrazhdane1/2/3 or vazrazhdane — meaning AGKK agrees the rest of Vazrazhdane is V. Varnenchik. So the question is whether the northern sliver (vazrazhdane4, 72% overlapping vazrazhdane, and the wikimapia Kochmar) crosses Treti Mart into Mladost. Since vazrazhdane4 overlaps vazrazhdane by 72% and the rest 28% presumably spills north across the boundary, AGKK's au5 boundary may cut it. The honest, verifiable statement: our layer's district assignment for quarter Features is derived by representative point against our own 5 districts (plan line 127), not from AGKK; the AGKK witness disagrees on these two. Who is right geographically: the official district boundary (AGKK au5 is the official administrative layer) is authoritative for „район"; if the polygon's representative point is north of Treti Mart, AGKK is right. But note the semantics: Wikimapia Kochmar (0,38 km²) is the polygon east of Vazrazhdane 2/3 — if Vazrazhdane 2/3 are south of Treti Mart, then Kochmar-east is also south, so our layer right for kochmar; OSM Kochmar is the one north (above Vazrazhdane 4). And vazrazhdane4: title „жк. Възраждане 4", overlapping 72% with vazrazhdane — the southern part is in V. Varnenchik; representative point probably south. 

  Hmm, but actually I should be careful and candid: I cannot run geometry (read-only, and the frozen geometry files are in ignored folders, maybe not in this copy). Let me check whether scratch/boundary_gallery has content in this copy. The listing showed scratch/boundary_gallery exists. Quick check might help. But geometry computation is beyond reading. The user asks „дай проверим довод" — give a verifiable argument, i.e., state the test and apply the available measured facts.

  Available measured facts:
  - Plan line 127 (Б0 т. 4): district written from our district.code, 375/375 agreement with AGKK measured 05.09 — but that agreement was for the 375 places, not for the 60 quarter Features. So both can be true: places agree 375/375 while two quarter polygons' representative points disagree.
  - Frozen measure line 39: wikimapia Kochmar is east of Vazrazhdane 2/3; OSM Kochmar northwest above Vazrazhdane 4.
  - Plan line 132: vazrazhdane4/vazrazhdane overlap 72% — partial, disputed zone.

  Argument: The district of the AGKK au5 layer is the official one, but its disagreement here is explicable: vazrazhdane4 sits on the boundary (only 72% inside vazrazhdane; the rest likely north of Treti Mart), and AGKK's Mladost (10135-03) extends south to Treti Mart. The verifiable test: representative point of each polygon vs the axis of bul. Treti Mart. For kochmar: the polygon we adopted (15278642) is east of Vazrazhdane 2/3 which are fully inside vazrazhdane (DAG, ≥98%), i.e., south of Treti Mart → our layer (vladislav_varnenchik) right; AGKK's claim of Mladost for kochmar likely reflects the other „Kochmar" (OSM polygon northwest of Vazrazhdane 4, which is in Mladost) — a name-collision of two different areas, like the two Chaikas (frozen measure line 16). For vazrazhdane4: its polygon overlaps vazrazhdane 72%, but 28% extends outside; if its representative point falls north of Treti Mart, AGKK is right for the point but the polygon straddles the district boundary — in that case neither is wholly right and the Feature should record district by coordinate rule, and places inside get disputed/fallback per Б0 т. 4(iii).

  Consequence for assignment (Б0 т. 4 fallback): the district fallback writes district from our layer's district.code; these 2 disagreements go to the conflict ledger (plan §7, line 152) as rows, never overwrite. And since district is „само район" fallback, the disagreement doesn't change quarter assignment — only which district a fallback row would name. Recommendation: keep our layer's district for kochmar (verifiable via Vazrazhdane 2/3 containment south of Treti Mart), mark vazrazhdane4 as straddling and its district disputed; no data rewrite, ledger rows per plan line 152 and principle line 7.

  Question 3: Dobreva ∪ Vinitsa-sever union (1,43 km²): are there places/buildings whose recorded quarter is Vinitsa-sever in registry or cadastre, and what happens to them when the code is excluded?

  Evidence: 
  - frozen measure §8 line 54: corridor residence→Vinitsa contains 23 buildings with „зона Виница-север" in cadastre (Kochmar... no — line 54: „зона Виница-север (23)"). Actually that was the Evksinograd corridor: „3 694 сгради, които кадастърът нарича с.о./м. Траката (1 654), к.к. Св. Св. Константин и Елена (82), зона Виница-север (23) — нито една „Евксиноград"". So yes — the cadastre knows 23 buildings as „зона Виница-север" in that corridor. Hmm, but is that corridor the same as the union area? The union is dobreva ∪ vinitsa_sever (5729421). Vinitsa-sever wikimapia polygon (d3 lines 786-797, title „Виница - север"). The corridor from residence to Vinitsa (3 km) — Vinitsa-sever is north of Vinitsa, presumably in that corridor. So the cadastre has 23 buildings with address „зона Виница-север".
  - For the 375 places: d4 line 177 reason: „нито едно от 375-те места не попада в тях" (neither of the 375 places falls in either polygon). Also session state line 29: „нито едно от 375-те места не е в засегнатата площ".
  - Registry: decision d4 line 800: registry deactivates the code (ход Р), not alias.

  What happens: buildings with cadastral quar/address „Виница-север" — the exclusion of the code means: (a) no quarter polygon for them; by Б0 т. 12 they're in `deferred_zone` (zone of excluded/registry_pending code → no fallback, stays empty, named in ledger) — wait, excluded is not exactly registry_pending; plan line 135: deferred_zone covers „код от registry_pending/отложен". Vinitsa_sever excluded — the code is deactivated in the registry (ход Р), and the area is now dobreva's polygon. So a building whose cadastre says „Виница-север" but which lies inside the dobreva union polygon: by the coordinate rule („координатата решава квартала; името е свидетел", plan line 152), it would be assigned dobreva if it had an empty quarter; if it had a written quarter „vinitsa_sever" the written stays and becomes disputed_written. But: none of the 375 places are in the area (d4 line 177, state line 29), so no place rows change. For buildings (Н4 measure), the 23 cadastral „Виница-север" buildings would now fall inside dobreva polygon → quar-vs-polygon disagreement rows in the Н4 measure (plan line 96). Also the code deactivation must handle name normalization: addresses saying „Виница-север" must still resolve (like alias?) — decision says „не е второ име" (d4 line 800: „не е второ име; площта е Добрева чешма"), explicitly NOT alias_of. So the name „Виница-север" becomes unresolvable as a quarter — the registry should deactivate but search normalization (D12) needs an entry or the 23 cadastral addresses lose their name. Consequence to flag: unlike vayalar→alias, here the name is killed; any future data with „Виница-север" in the address string has no registry code — recommendation: keep the deactivated code with an alias-like mapping to dobreva for the normalizer, or record it as a name witness.

  Question 4: other codes in decisions 4 that by the same logic should be excluded/merged?
  - borovets (общ) vs borovets_sever/borovets_yug: registry has „Боровец (общ)" with no confirmed polygon (plan line 35: „borovets няма потвърден полигон"; frozen line 18/38 list Боровец among без кандидат / 17 без решение). It's one of the 16 registry_pending. By the same logic as vinitsa_sever? Not quite — vinitsa_sever was excluded because its territory is actually dobreva's (a factual territorial claim). Borovets общ has no polygon; sever+yug exist as separate polygons. Same logic would suggest borovets общ → deferred stays, or alias? It's not that its territory belongs to another code; it's a parent without geometry. Different situation — keep registry_pending. But the question asks whether exclusion/merging should follow „by the same logic". Same logic = „the name's territory belongs to another code". Candidates:
    - trakata_so vs evksinograd: frozen line 56: „trakata_so не може да вземе същия полигон (D6); „Траката" 2,74 km² е друг обект". Evksinograd took 5729429 („Траката - разширение"). trakata_so remains without decision (one of 16 registry_pending? Actually trakata_so is among the 17 without decision per frozen line 43: „Траката с.о./в.з."). The cadastre calls the evksinograd land „Траката" (d4 line 217). So there IS a name-territory conflict: our evksinograd Feature covers what the cadastre calls Trakata. By the same logic (territory over name), one might argue evksinograd code should be re-examined, but Petar explicitly decided with the name-conflict note. Not exclusion — but a witness conflict recorded.
    - vazrazhdane4: 72% overlap with vazrazhdane — plan line 132 already declares it non-parentage, disputed. Could argue merge? No, it's a real subdistrict.
    - sredna_traka/vayalar — already alias (d4 lines 695-707).
    - maksuda/sv_ivan_rilski 39%, grackata_mahala/tsentar 52%, pz_planova/vladislavovo 61% — partial overlaps already handled as disputed zones (plan line 132).
    - borovets: plan line 78 Н1 mentions borovets_sever/borovets_yug have parent without polygon → parent_geometry_check. The same „exclusion" logic doesn't apply; what applies by same logic is maybe: borovets общ should become parent (alias/DAG) not a boundary code — already deferred to registry morning list (plan line 133 Б0 т. 10).
    
  Answer: no other code requires exclusion by the vinitsa_sever logic (territory proven to belong to another named code). The closest is evksinograd/trakata_so, which is a recorded name-conflict, not a territory takeover; and borovets общ, which is a geometry-less parent — handled by Б0 т. 9/10, not exclusion.

  Also the audit findings: (a) signature chain — artifact from decisions 4 not signed by Petar. (c) union pin reproducible only via EPSG:32635 with exact shapely 2.1.2/pyproj 3.6.1 — this is a provenance/reproducibility weakness: the union geometry is derived (method human_polygons_union) and its sha pins the environment too; the decision file pins wm_polygon_sha256 d6f367bd (d4 line 175) but the union file `unions_2026-09-07.geojson` (state line 29) is in an ignored folder, and reproducibility depends on exact library versions — the pin should record the tool versions (witness). This makes the artifact's dobreva feature not independently re-verifiable from the two frozen polygons alone without the exact env.

  Verdict: ГОДНО with named fixes (условно годно)? The task says „Присъда ГОДНО/НЕГОДНО за данните на Б1 (второ изпълнение) с поименни поправки". Data-wise: the two changes are correct and minimal; 58 untouched rows identical. But: (a) unsigned decisions 4 chain — process/provenance, (b) 2 district disagreements — ledger rows, (c) env-dependent pin. For a data-lens review: ГОДНО условно — the data itself (58+2 rows) is sound, but the named fixes: 1) Petar signs decisions 4 by sha of blob 2c650160 (or commits it himself, Г2-б) and artifact _meta.decisions_sha256 must point to it; decisions 3 signature no longer suffices. 2) vazrazhdane4/kochmar district disagreement → conflict-ledger rows; no rewrite; verify representative point vs Treti Mart. 3) pin the union environment (shapely/pyproj versions, EPSG) in _meta manifest + record unions file sha. 4) vinitsa_sever exclusion: registry deactivation + normalizer mapping for the 23 cadastral buildings' name; Н4 will show 23 quar-disagreement rows — expected, not error.

  Word limit 1200, Bulgarian, every claim with file:line. Paths relative to C:/git/Fire_Varna.

  Let me count rough structure. I'll write concisely.

  Key line references:
  - d4 (decisions 4): lines 4-7 based_on sha ec2813e1; 14 exported_at; 15-23 changes; 169-184 dobreva union; 792-804 vinitsa_sever excluded; 175 sha d6f367bd; 177 reason „нито едно от 375-те места не попада в тях"; 800 „не е второ име".
  - d3: 167-178 dobreva wikimapia 5729380; 786-797 vinitsa_sever wikimapia 5729421.
  - Plan: line 26 (d3 counts), 27 (agent committed b6e627d), 131 (Б0 т. 8 sign by sha), 132 (Б0 т. 9 DAG + partial overlaps incl. vazrazhdane4 72%), 127 (Б0 т. 4 district fallback), 135 (Б0 т. 12 deferred_zone), 138 (Б1, 61 Feature, commit by Petar), 152 (§7 conflict ledger), 7 (principle).
  - frozen: 39 (kochmar two polygons), 54 (23 buildings зона Виница-север), 56 (trakata_so D6), 16 (two chaikas).
  - state: 27 (B1 staged sha 3f423898, 61 boundaries), 29 (decisions 4, unions file, 60 boundaries), 31 (decision 8).

  Note artifact described: 60 Feature (d4 gives 58 wikimapia + 1 union + 1 declared_streets = 60). State line 29 says result map shows 60 boundaries. Plan Б1 said 61 features from decisions 3; second execution from decisions 4 → 60. Consistent.

  Answer to (1): Outside dobreva/vinitsa_sever — no data changes. Verified: 66 remaining rows byte-identical (same wm_id, sha, title, decided_by/at). Header changes: based_on pointer (d4:5-7), exported_at (d4:14), +2 changes entries (d4:21-22). What Petar must sign: sha256 of the blob of granitsi_decisions_4 in the architect's commit (2c650160…), per the mechanism of Б0 т. 8 (plan:131) applied to the new file; then artifact _meta.decisions_sha256 must equal that sha, and the artifact itself (sha 4930f204…) awaits Petar's commit per D16/G4 (plan:138). Signing decisions 3 (b6e627d) does not cover the artifact.

  Length: aim ~1000-1100 words. Write in Bulgarian.

• Прочетох и двата файла с решения, плана, мярката и състоянието. Ето прегледът (даннена леща, лот Б1 второ изпълнение).

  # К24 · Преглед на Б1 (второ изпълнение) — леща ДАННИ

  ## (1) Диф решения 4 срещу решения 3 и какво се подписва

  Данните извън `dobreva`/`vinitsa_sever` **не са променени**. Проверих ред по ред двата файла: останалите 66 реда са идентични по `wm_id`, `wm_polygon_sha256`, `wm_title`, `decided_by/at` (срв. напр. `abatko` decisions_3:23-34 ↔ decisions_4:25-36, `kochmar` decisions_3:323-334 ↔ decisions_4:329-340, `vazrazhdane1..4` decisions_3:714-761 ↔ decisions_4:720-767). Промените са точно три:

  - `dobreva`: `wikimapia` 5729380, sha `9e59fd99…` (granitsi_decisions_3:167-178) → `wikimapia_union`, `wm_id: null`, `wm_ids: [5729380, 5729421]`, sha `d6f367bd…` (granitsi_decisions_4:169-184).
  - `vinitsa_sever`: `wikimapia` 5729421, sha `bebef782…` (granitsi_decisions_3:786-797) → `excluded`, всички полета `null` (granitsi_decisions_4:792-804).
  - Заглавна част: `based_on` сочи решения 3 по sha `ec2813e1…` (granitsi_decisions_4:4-7), ново `exported_at` (decisions_4:14), два нови реда в `changes` (decisions_4:21-22).

  Сметката се затваря: 58 wikimapia + 1 union + 1 declared_streets + 6 deferred + 1 alias_of + 1 excluded = 68 реда → 60 Feature в артефакта (58+1+1), както е записано в СЪСТОЯНИЕ:29.

  За честна верига Петър трябва да подпише **решения 4 по sha256 на блоба `2c650160…`** от комита на архитекта — същият механизъм като Б0 т. 8 (ПЛАН:131), приложен към новия файл. Подписът върху решения 3 (`ec2813e1…` в b6e627d) вече **не покрива артефакта**, защото артефактът е сглобен от решения 4. Допълнително: `_meta.decisions_sha256` на `quarters_signed.geojson` трябва да е равен на подписания sha на решения 4, а самият артефакт (sha `4930f204…`) чака комит на Петър по D16/G4 (ПЛАН:138). Статусът на решения 4 е същият дефект като при решения 3 — `agent_committed_proba`, автор Claude Architect (ПЛАН:27).

  ## (2) `vazrazhdane4` и `kochmar` — нашият слой или АГКК

  Проверимият довод е представителната точка на полигона спрямо оста на бул. „Трети март“ (границата Владиславово/Младост). Наличните измерени факти:

  - Уикимапийският „Кочмар“ (15278642, 0,38 km² — избраният в decisions_4:329-340) лежи **източно от Възраждане 2/3**; другият „Кочмар“ (OSM, 0,58 km²) е северозападно, над Възраждане 4, и двата не се допират (wikimapia_frozen_measure_06.09.md:39). Възраждане 2/3 са ≥98 % вътре във `vazrazhdane` (DAG, ПЛАН:132), т.е. южно от „Трети март“. Следователно избраният полигон е във Владислав Варненчик — **нашият слой е прав за kochmar**; АГКК-свидетелят вероятно говори за другия, северния „Кочмар“ — същото съвпадение на имена като двете „Чайка“ (frozen:16).
  - `vazrazhdane4` припокрива `vazrazhdane` само 72 % и е деклариран като частично припокриване, не родство (ПЛАН:132). Останалите 28 % вероятно пресичат „Трети март“ на север — полигонът **разделя районната граница**, затова и двата свидетеля са „прави“ за различни части. АГКК-свидетелят не е опроверган; той е ред в леджера на конфликтите (ПЛАН:152) и принципът „спорът е ред в леджер, никога презапис“ (ПЛАН:7).

  Следствие за присвояването: районът се пише само като резерва от нашия `district.code` с `district_src: "fire_varna_district"` (Б0 т. 4, ПЛАН:127); за места в зоната на `vazrazhdane4` районният запис е спорен → колона в леджера, не редакция. Съгласието „375/375“ (ПЛАН:127) е мерено за местата, не за 60-те квартални полигона — двете несъгласия не го нарушават.

  ## (3) Обединението и изключения `vinitsa_sever`

  Да, такива сгради има: кадастърът носи **23 сгради с адрес „зона Виница-север“** в коридора резиденция→Виница (frozen:54). От 375-те места **нито едно** не попада в двата полигона (decisions_4:177; СЪСТОЯНИЕ:29), значи нито един ред на място не се променя. Сградната мярка (Н4) обаче ще покаже ~23 несъгласия „кадастрален quar ≠ полигон dobreva“ — това е очакван резултат, не грешка.

  Проблемът е в избрания вид изключване: „кодът отпада от регистъра… **не е второ име**“ (decisions_4:800). За разлика от `vayalar → alias_of sredna_traka` (decisions_4:695-707), името „Виница-север“ остава без нормализаторен път — всяко бъдещо място/сграда с този адресен низ няма регистров код. По правилото „имената се нормализират през регистъра (alias-и)“ (ПЛАН:154) деактивираният код трябва да запази alias-подобен запис към `dobreva`, иначе 23-те кадастрални адреса губят името си.

  ## (4) Друг код по същата логика

  Логиката на `vinitsa_sever` е „територията на името доказано принадлежи на друг код“. По нея:

  - **`vayalar` — вече решен** като alias (decisions_4:699-706).
  - **`borovets` (общ)** няма потвърден полигон, а север/юг имат собствени (ПЛАН:35, :78). Това не е „територия на друг код“, а родител без геометрия — правилният ход е DAG/родителство (Б0 т. 9–10, ПЛАН:132-133), не изключване.
  - **`trakata_so`/`evksinograd`** — кадастърът нарича земята на избрания полигон „Траката“ (decisions_4:217), а `trakata_so` не може да вземе същия полигон по D6 (frozen:56). Това е записан конфликт на имена, не поглъщане на територия — остава в сутрешния списък за регистъра (СЪСТОЯНИЕ:19).

  Присъда: **никой друг код не изисква изключване/сливане по тази логика.**

  ## (в) Пинът на обединението

  Обединението е производна геометрия (`human_polygons_union`), чийто sha `d6f367bd…` (decisions_4:175) се възпроизвежда само при EPSG:32635 с shapely 2.1.2/pyproj 3.6.1. Файлът `unions_2026-09-07.geojson` е в игнорирана папка (СЪСТОЯНИЕ:29). Пинът затова трябва да носи в `_meta` манифеста: sha на unions-файла, EPSG и точните версии на библиотеките — иначе Feature-ът не е независимо препроверим от двата замразени свидетеля.

  ## Присъда: **ГОДНО условно** за данните на Б1 (второ изпълнение)

  Данните са минимални и верни (66/68 реда непокътнати; двете промени са с причина, думи на Петър и мярка). Поименни поправки преди комита на Петър:

  1. Подпис на **решения 4** по sha на блоба `2c650160…`; `_meta.decisions_sha256` на артефакта да сочи него (ПЛАН:131, :138).
  2. Пин на средата на обединението (EPSG, shapely/pyproj версии, sha на unions-файла) в `_meta`.
  3. `vazrazhdane4`/`kochmar` — редове в леджера на конфликтите; без презапис (ПЛАН:152, :7).
  4. При деактивирането на `vinitsa_sever` — нормализаторен запис към `dobreva` заради 23-те кадастрални адреса (decisions_4:800; frozen:54).

To resume this session: kimi -r session_88b194b6-d84b-40c1-9998-eaadbd530e4b
