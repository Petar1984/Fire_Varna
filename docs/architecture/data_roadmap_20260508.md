# Data Roadmap 2026-05-08

> **Audience:** Petar и AI agents (Codex, Claude Code, Claude chat) при бъдещи sprint-овете.
> **Purpose:** Стратегически документ записващ архитектурните decisions за data layer-а. Не е implementation plan — е reference за бъдещи sprints.
> **Status:** Draft pre-launch. Decisions могат да се ревизират преди broad launch.
> **Source evidence:** All findings cite `docs/audits/data_architecture_audit_20260508.md` and `docs/audits/issue_ingest_plan_20260508.md`.

---

## 1. Current State

### Data inventory

Repo съдържа three layers of hydrant data:

**Sources (untracked, baseline от 2026-05-04):**
- 5 VIK KMZ files (DEVNIa, DOLNI_ChIFLIK, PROVADIIa, VARNA_IZTOK, VARNA_ZAPAD) — 3,934 records total
- NAT WFS bundle (geo_fire_hydrants.json/kml/shp/dbf/prj/shx) — 17,962 records covering whole Bulgaria
- 1 manual KML ("Първа РС сев от бул Левски 23.06.25г.kml") — 654 records, field-survey from 1-ва РС Варна

**Runtime dataset:**
- `data/hydrants.json` — 6,082 records (3,661 vik + 2,407 national + 14 field_report)
- `field_reports.json` — 14 records (canonical field report state)

**Reference artifact:**
- `hydrants_varna.json` — 3,934 records (subset of data/hydrants.json, kept as KMZ-derived reference)

### Five fundamental issues identified by 2026-05-08 audit

**1. data/hydrants.json е merge target, не independent source.**
Audit confirmed чрез pairwise distance analysis: hydrants_varna.json е напълно contained в data/hydrants.json (3,936 zero-meter pairs). Five VIK KMZ files contributed 98-1,278 records each into data/hydrants.json. Direct edits към data/hydrants.json **се губят** ако не са reflected в source data + merge logic. Cleanup трябва да rebuild data/hydrants.json от sources, не да edit-ва directly.

**2. 609 zero-meter intra-file duplicates в data/hydrants.json.**
Examples: `VIK-VARNA_IZTOK-0003` и `VIK-VARNA_ZAPAD-0017` съществуват с identical coordinates. VIK regional namespaces се припокриват в boundary zones между Изток и Запад. Plus 200 cross-pattern numeric collisions (`10122` присъства като `10122-DC` и `10122-DV`). Все same physical hydrant с multiple ID forms.

**3. NAT CRS handling differs between raw source and runtime.**

- **Raw source files** (`geo_fire_hydrants.*`): `.prj` sidecar declares EPSG:3857, but raw values require inverse EPSG:3857 **plus axis swap** to resolve to Bulgaria. Only 4 of 17,962 source records pass Bulgaria envelope check without the axis-swap fix.
- **Runtime data** (`data/hydrants.json` NAT records): the 2,407 NAT records currently shipped are already correctly transformed — original ingest applied the axis swap. Standard inverse only is needed when reading them back.
- **Future re-imports from source** must replicate the axis-swap step per `docs/audits/data_architecture_audit_20260508.md` § 6 NAT CRS empirical check.

**4. NAT scope filter recovered: regions 71-79 + Varna-side 81 + 2 null-region exceptions.**
Original filter logic не беше в repo. Codex post-audit reconstruction: not a bounding box, а administrative filter using `geo_region` codes plus manual curation на boundary cases (Обзор/Бургас side excluded). Documented for cleanup sprint replication. See § 2.4 — filter rule pending Codex investigation 2026-05-09.

**5. Address coverage е asymmetric across sources.**
- NAT records have rich addresses (99.99% populated `name` field, full Bulgarian street format)
- VIK records have empty `a` field в runtime (KMZ source `adres` field also mostly empty)
- Field reports have descriptions, not addresses
- Първа РС file has Bulgarian addresses embedded в placemark NAMES, not address field

### Two bugs identified during 2026-05-08 issue ingest

**6. Polling dedupe ID format mismatch.**
Polling logic compares full UUID (from issue body) against truncated `field_<8chars>` (in data file). Mismatch creates duplicate pins. Fixable с 1-line patch в polling code (`index.html` ~line 3045). Issues #29-#36 ingested in commit 2dcab73 but remain open on GitHub per `docs/activeContext.md`. Bug will manifest on next polling cycle until issues closed or fix applied.

**7. Card/row UI does not display hydrant type field 't'.**
Universal across vik/national/field_report. `hydrantTypeLabel(t)` helper exists but invoked only в report modal. Reusing it в `updateCardInfo` and `renderList` closes the gap.

---

## 2. Architectural Decisions

### 2.1 ID Format

**Decision:** Coordinate + neighborhood hybrid.

```
HYD-{NEIGHBORHOOD_SLUG}-{LON×10000}-{LAT×10000}
```

Examples:
```
HYD-CHAIKA-279300-432100
HYD-DEVNIa-274200-432200
HYD-VARNA-279500-432500    (rural, no neighborhood)
HYD-UNKNOWN-280000-432000  (outside known areas)
```

**Fallback hierarchy за neighborhood slug:**
1. OSM Nominatim suburb/neighbourhood (e.g., "Чайка" → "CHAYKA")
2. If absent → village/town (e.g., "Девня" → "DEVNYA")
3. If absent → admin region (e.g., "Варна" → "VARNA")
4. If absent → "UNKNOWN"

**Coordinate precision:** 4 decimals (~10m resolution). Stable за typical GPS noise; ID changes only on coord corrections >10m.

**Latin transliteration в code, Cyrillic in UI display:**
- Code: `HYD-CHAYKA-...`
- UI render: "Чайка" via lookup table `NEIGHBORHOOD_DISPLAY`
- Same pattern за hydrant types (`надземен` etc.)

**Trade-offs accepted:**
- ✅ Auto-generated, idempotent
- ✅ No migration when adding new sources
- ✅ Searchable by neighborhood
- ❌ ID changes if coord corrected >10m (rare; preserve mapping)
- ❌ Boundary hydrants get arbitrary neighborhood assignment
- ❌ One-off batch processing cost (~6,082 Nominatim calls)

**Migration path:**
- Build mapping `old_id → new_id` during cleanup
- Save as `data/id_migration_20260508.json` (or similar)
- Preserve old IDs as `aliases: []` in records
- Backward compatibility for any external references

#### ID Generation Rules

**Coordinate rounding:** Truncate toward zero (floor for positive coords).
- Example: 27.93005 → 27.9300, NOT 27.9301
- Deterministic regardless of locale or floating-point library
- Implementation: `int(coord * 10000) / 10000`

**Transliteration:** ISO 9 (1995) standard, output all uppercase Latin.
- Examples: Чайка → CHAYKA, Девня → DEVNYA, Аспарухово → ASPARUHOVO
- Special handling: ь/ъ → empty, й → J, щ → SHH, ю → YU, я → YA
- Reference table: `scripts/transliteration_table.json` (created during cleanup sprint)
- Existing inconsistent examples (DEVNIa, etc.) become aliases only

**Slug normalization:**
- Spaces → underscore: "Св. св. Константин и Елена" → "SV_SV_KONSTANTIN_I_ELENA"
- Strip: apostrophes, periods, punctuation
- Collapse multiple underscores → single
- Maximum length: 30 chars (truncate if longer)

**Collision handling:**
- If two neighborhoods slugify identically → append `-2`, `-3` suffix
- Mapping recorded in `scripts/neighborhood_slug_collisions.json`

**Coordinate format:** Zero-padded for consistency.
- Bulgaria coords always 6 digits after truncation
- Example: 27.9300 → "279300", 43.2100 → "432100"
- Negative coords (none in Varna) would prefix with "N"

### 2.2 Source Priority

**Decision:** VIK wins on conflict; NAT contributes addresses; field reports override coordinates.

When multiple sources reference the same physical hydrant (same coordinates within tolerance — see § 2.8):

| Conflict type | Winner | Rationale |
|---|---|---|
| Coordinates | VIK | Local water utility, more current |
| Type (надземен/подземен) | VIK if populated, else NAT | VIK is operational data |
| Status / state | VIK | NAT data is static archive |
| Address (`a` field) | NAT.name \|\| Nominatim reverse geocode | VIK has empty addresses |
| Notes / description | Merged from all sources | Audit trail value |
| Field report wrong_location | Field report | Recent ground truth |

### 2.3 Source Archive Provenance

**Decision:** Direct git commit of source archives (~30MB total).

- Sources committed to `sources/` directory
- `.gitattributes` policy: binary archives tracked directly, no LFS yet
- `sources/acquisition_log.md` documents provenance per file (capture date 2026-05-04 baseline, CRS, schema notes, who acquired)
- **Migration trigger to git LFS:** if total `sources/` size exceeds 100MB, evaluate LFS migration in a separate sprint. Not anticipated soon.

This makes data layer reproducible. Without committed sources, future rebuild becomes impossible if originals lost.

### 2.4 NAT Scope Filter

**Decision:** Replicate documented filter rule when rebuilding NAT subset.

**Status:** Investigation delegated to Codex 2026-05-09 to identify exact filter rule. Roadmap will be updated when results return.

Per Codex 2026-05-08 reconstruction (preliminary):
- `geo_region` codes 71-79 (Varna oblast administrative codes)
- Plus subset of region 81 (Varna-side only, exclude Обзор/Бургас-side)
- Plus 2 null-region records (manually included; preserve)
- Apply standard EPSG:3857 inverse (no axis swap needed for runtime; only required when reading raw source files — see § 1 finding #3)

**Open Questions added (will move to § 7 Open Questions):**
- Q8: Precise region 81 split rule (coordinate cutoff? polygon? manual ID list?)
- Q9: Identification of 2 null-region records currently included (which IDs?)
- Q10: Should boundary-area NAT records (currently excluded) be reviewed for inclusion?

Until investigation completes, cleanup sprint **must not** rebuild NAT subset.

Cleanup sprint will encode this as `scripts/build_nat_subset.py` with full filter logic versioned in code.

### 2.5 Wrong-Location Correction Preservation

**Decision:** Preserve existing wrong_location corrections during rebuild.

Audit found `NAT-14277` differs от source by ~20m due to applied wrong_location report. Rebuild process must:
- Load existing corrections from `field_reports.json`
- Apply corrections after source merge
- Document each correction в commit message

### 2.6 Address Strategy

**Decision:** Multi-source address resolution with Nominatim fallback.

Per-record address resolution priority:
1. **Existing `a` field if populated** (preserve manual entries)
2. **NAT `name` field if origin=national** (already address-formatted Bulgarian)
3. **Nominatim reverse geocode** (for VIK + field_reports without addresses)
4. **Fallback:** empty string + show "Координати: lat, lon" в UI

For field reports submitted via app:
- **Auto-fill on submit** (Option B in earlier discussion):
  - Worker calls Nominatim before creating GitHub issue
  - Address embedded in issue body
  - Reporter sees address pre-filled, can correct before submit
- Implementation: Worker enhancement, separate sprint after cleanup

#### Nominatim Usage Policy

**Decision:** Nominatim approved as runtime dependency per AGENTS.md § Hard Constraints exception.

**Usage policy (binding for all Nominatim calls):**

- **Rate limit:** 1 request per second (Nominatim public API policy)
- **User-Agent:** `Fire_Varna/1.0 (contact: [Petar email — TBD])`
- **Cache:** Persistent file-based cache `data/nominatim_cache.json`
  - Key: rounded coords (4 decimals)
  - Value: full Nominatim response
  - Hit on cached → no API call
- **Retry:** 3 attempts with exponential backoff (1s, 2s, 4s)
- **Fallback on rejection:** empty address field, log to `data/nominatim_failures.log`
- **Privacy:** Coordinates only; no user identity transmitted to Nominatim
- **Offline behavior:** App must degrade gracefully if Nominatim unreachable

**Approval scope:**
- Reverse geocode batch (one-off ~6,082 calls during cleanup)
- Reverse geocode on report submit (Worker-side, future sprint)
- Forward geocode on dispatcher search (recurring, app-side, future sprint)

Same policy applies to all three usage paths.

### 2.7 Address Search (forward geocoding)

**Decision:** Hybrid approach for dispatcher search.

User flow: "Find hydrants on ул. Цар Симеон":
1. Forward geocode user query via Nominatim → coords
2. Existing nearest-hydrant logic returns hydrants near those coords
3. Plus: filter by neighborhood slug if address contains neighborhood

Nominatim usage governed by § 2.6 Nominatim Usage Policy — no separate policy needed.

Implementation: ~50 lines JS in `index.html`. Separate sprint after schema additions.

### 2.8 Merge Tolerance

**Decision:** 5m automatic merge threshold; 5-15m manual review; >15m kept separate.

When two records from different sources reference physical hydrants at near-identical coordinates:

| Distance | Action | Rationale |
|---|---|---|
| 0m exact | Auto-merge | Confirmed dedup (609 known cases) |
| 0.1-1m | Auto-merge | GPS noise / coordinate precision artifact |
| 1-5m | Auto-merge | Within typical GPS error |
| 5-15m | Flag for manual review | Could be different fixtures on same building |
| >15m | Keep separate | Different physical hydrants |

Implementation: cleanup script outputs `flagged_for_review.json` for the 5-15m bucket. Petar reviews before cleanup commit.

---

## 3. Schema Additions

Decisions documented but **not yet implemented**. Implementation in cleanup sprint.

### 3.1 New flat fields

**`operational_status`** (string)
- Values: `"operational"`, `"non_operational"`, `"unknown"`, `"under_maintenance"`
- Distinct from existing `status` (visual state) and `st` (raw source status)
- Defaults to `"unknown"` for existing records

**`last_inspection_date`** (ISO string, nullable)
- Format: `"2026-05-08"` or null
- Updated when field report confirms hydrant
- Useful for inspection scheduling

**`neighborhood`** (string)
- Latin slug (matches ID component)
- Cached from Nominatim reverse geocode
- Avoids re-querying for display

**`aliases`** (array of strings)
- Old IDs after rebuild
- Enables backward compatibility
- Example: `["10122-DV", "VIK-VARNA_ZAPAD-0098"]`

### 3.2 Nested report history

**Decision:** Separate file, not nested in main array.

Storing report history per record would balloon `data/hydrants.json` (1MB → multi-MB). Instead:

- New file: `data/report_history.json`
- Structure: `{ "HYD-CHAYKA-279300-432100": [report1, report2, ...] }`
- Each report: `{ timestamp, type, status_change, issue_url, ... }`
- Loaded lazily in app (only when user taps a hydrant)
- Keeps first-load size unchanged

> **Note on `reporter`:** Reporter persistence governed by Q3; until resolved, reporter is captured in GitHub issue body only, not in `report_history.json`.

### 3.3 Schema Version Tracking

**Decision:** Schema version metadata in separate file, not wrapped around records.

`data/hydrants.json` shape: **unchanged** — remains top-level JSON array. App code (`JSON.parse(...).length`) continues to work without modification.

New file: `data/hydrants.meta.json`:
```json
{
  "schema_version": "2.0",
  "generated_at": "2026-05-08T...",
  "source_versions": {
    "vik_kmz": "2026-05-04",
    "nat_wfs": "2026-05-04",
    "field_reports": "2026-05-08"
  },
  "record_count": 6082,
  "build_script_version": "1.0"
}
```

**Loading strategy:** App optionally fetches meta file. If incompatible `schema_version` detected, show user-friendly warning. If meta file missing, app continues normally (backward compatible).

**Future migration to wrapped format (Schema 2.x):** mechanical transformation, ~30 minutes of work, reversible. Not blocked by current decision.

---

## 4. Cleanup Sprint Topology

High-level steps for cleanup sprint. Codex will produce detailed plan against this when sprint begins.

### Stage 0 — Integrate pending data drops

Per `docs/activeContext.md`, integrate any pending hydrant data drops before dedup/ID normalization. Cleanup sprint must not begin Stage 2 rebuild until all known sources are committed to repo.

### Stage 1 — Foundation
- Commit sources to `sources/` with `acquisition_log.md`
- Create `scripts/` directory for build scripts
- Document NAT CRS transformation in reusable function
- Document NAT scope filter в script

### Stage 2 — Rebuild data/hydrants.json
- Read VIK KMZs → parse description tables → normalize
- Read NAT (CRS fix + Varna filter) → normalize
- Read field_reports + Първа РС → normalize
- Apply ID generation (HYD-{slug}-{lon}-{lat})
- Cross-source dedup with priority rules (§ 2.2) and merge tolerance (§ 2.8)
- Apply wrong_location corrections
- Address resolution (existing → NAT → Nominatim)
- Generate с new schema (`schema_version` 2.0 in `data/hydrants.meta.json`)
- Save mapping `old_id → new_id`

### Stage 3 — Update app code
- Update `index.html` to optionally consume `data/hydrants.meta.json`
- Fix polling dedupe bug (issue #6 in Section 1)
- Fix card/row type rendering (issue #7 in Section 1)
- Add `aliases` lookup for backward compatibility
- Update tests / verification

### Stage 4 — Verification
- Compare new dataset to old dataset (record count, coord stability)
- Test live app on phone
- Sample manual verification (10 random hydrants)
- Roll back if issues; otherwise commit

### Stage 5 — Address features (separate sprint)
- Reverse geocode batch for existing records
- Address auto-fill on report submission (Worker enhancement)
- Forward geocoding search UI

---

## 5. Bug Fix Priority

Independent of cleanup sprint:

**Priority 1 — Polling dedupe** (Issue #6)
- Active impact на recurring ingest cycles
- Single-line fix
- Fix immediately, не wait for cleanup

**Priority 2 — Card/row type rendering** (Issue #7)
- User-facing UX gap
- Small change в `updateCardInfo` and `renderList`
- Could combine с Priority 1 в single bug-fix commit

Both fixes touch only `index.html`. No data file changes. Safe to do before cleanup.

---

## 6. Worker Enhancements (post-cleanup sprint)

- `POST /close-issue` endpoint — automated issue closing after ingest
- Address auto-fill on `POST /` (Worker calls Nominatim before issue creation)
- Worker source extraction to `worker/` directory (commit 17 TODO)

---

## 7. Open Questions

Decisions deferred — need future input:

**Q1.** Schema migration triggers — how does app detect "1.0" vs "2.0" data and refuse to load incompatible? Soft fail or hard fail? (Note: § 3.3 separate-meta-file decision reduces urgency — app no longer loads a wrapped object — but mismatch detection still useful.)

**Q2.** When old IDs (aliases) are referenced from external sources (printed maps, manual records), should app accept them as input in search? Yes/no policy.

**Q3.** Field report submitter identity — currently captured in GitHub issue body but not stored в data. Should it be persisted? Privacy implications for non-firefighter contributors.

**Q4.** Hydrant type backfill from missing/exists_confirmed reports — when reporter provides `hydrant_type_at_location`, should it back-populate canonical record's `t` field? (Open Question from issue ingest plan.)

**Q5.** What constitutes "neighborhood boundary"? Hydrant exactly between Чайка and Аспарухово — which slug wins? First Nominatim match or rule-based?

**Q6.** Inspection scheduling — should app surface "hydrants not inspected in >X months"? Drives need for `last_inspection_date` but also UI.

**Q7.** Multi-language support — fixed Bulgarian-only for now per AGENTS.md, but Cyrillic display + Latin code makes future English layer easier. Document this design intent.

**Q8.** NAT region 81 split rule (precise cutoff for Varna-side vs Burgas-side).

**Q9.** Two null-region NAT records — which IDs are currently included?

**Q10.** Nominatim contact email for User-Agent header — Petar to provide.

**Q11.** Source priority conflict matrix for all report types (missing, damaged, exists_confirmed, wrong_location, new_hydrant). Codex audit § 7 raised this; needs explicit decision before cleanup.

**Q12.** `operational_status` default mapping from existing VIK status field — does VIK status map to new field, or all records start as "unknown"?

**Q13.** Notes merge format — when multiple sources have notes for same hydrant, separator/dedup/order policy.

**Q14.** Wrong-location corrections inventory — full list of NAT/VIK records currently differing from source coords. NAT-14277 is one example; investigation needed for completeness.

**Q15.** Source archive size monitoring — when does git repo cross 100MB threshold and trigger LFS evaluation?

---

## 8. Document Lifecycle

**Updates required when:**
- Architectural decision changes (update relevant section + add changelog entry)
- New question surfaces (add to Section 7)
- Question resolves (move from Section 7 to relevant section, mark "Resolved YYYY-MM-DD")

**Frozen after:**
- Broad launch — post-launch changes need migration plan, not just doc edit

**Reference target:**
- AGENTS.md should link to this document under § Data Model
- New Codex/Claude Code sessions read this after AGENTS.md and activeContext.md

---

## 9. Decision Ledger

| Decision | Source | Evidence | Reversibility | Approval |
|---|---|---|---|---|
| Coord rounding: truncate | Petar 2026-05-09 | Determinism critical for ID stability | Reversible (re-run script) | Approved |
| Transliteration: ISO 9 uppercase | Petar 2026-05-09 | Inconsistent existing examples (DEVNIa vs CHAIKA) | Reversible via lookup table | Approved |
| Merge tolerance: 5m auto, 5-15m review | Petar 2026-05-09 | Audit § 3 distance distribution | Reversible (rebuild) | Approved |
| Schema versioning: separate meta file | Petar 2026-05-09 | Avoids breaking `JSON.parse(...).length` | Reversible (mechanical migration) | Approved |
| Source archives: direct git commit | Petar 2026-05-09 | ~30MB acceptable for current repo | Reversible (LFS migration if needed) | Approved |
| Nominatim approved with usage policy | Petar 2026-05-09 | AGENTS.md dependency approval gate | Reversible (remove dependency) | Approved |
| NAT scope: investigation delegated to Codex | Petar 2026-05-09 | Discovery task, not policy decision | N/a | Delegated |
| `reporter` removed from report_history | Petar 2026-05-09 | Privacy concern (Q3) | Reversible if Q3 resolves yes | Approved |
| Stage 0 added to cleanup topology | Petar 2026-05-09 | activeContext pending data drop gate | Reversible (skip if N/A) | Approved |
| Polling dedupe bug status corrected | Auto-fix | activeContext.md ground truth | N/a | Fact-driven |
| Markdown escapes removed | Auto-fix | GitHub render correctness | N/a | Cosmetic |
| Record count verified empirical | Auto-fix | Codex 2026-05-08 verified | N/a | Fact-driven |

---

## Changelog

- **2026-05-08:** Initial draft. Section 1 evidence from `data_architecture_audit_20260508.md`. Decisions in Sections 2-3 ratified by Petar in chat 2026-05-08. Bug findings from `issue_ingest_plan_20260508.md` + chat investigation.
- **2026-05-09:** v2 revision. Addressed 2026-05-08 reviews from Codex (10 findings) and Claude Code (5 blocking + 8 smaller gaps). Ratifications by Petar 2026-05-09. See § Decision Ledger.
