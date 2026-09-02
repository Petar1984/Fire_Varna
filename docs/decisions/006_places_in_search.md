# ADR 006 — Places (hotels) as a separate result branch in the Fire_Varna search

**Date:** 2026-09-02 · **Status:** Accepted by Petar's signed prompt of 2026-09-02 (Gate 1: `varna_3d/docs/sessions/ПРОМПТ_нощна_смяна_търсачка_02.09.md`); Gate 2 (diff review + push) pending

Supersedes nothing. Materialises Д1–Д12 of the signed plan
[`docs/plans/places_search_plan_2026-09-02.md`](../plans/places_search_plan_2026-09-02.md) —
v2 plus its amendments §10 (v2.1, after the recall sweep over the 226 records),
§11 (v2.2, after the Kimi attack) and §12 (v2.3, after Sol's verdict on the
wiring; where §12 and §2 differ, §12 wins). The plan stays the executable
specification; this ADR records *what was decided and why* and the obligations
that outlive the cycle. It adds one obligation to ADR
[`005_sw_cache_lifecycle.md`](005_sw_cache_lifecycle.md) (D6, `PROTECTED_CACHES`)
and changes nothing in ADR [`001_fire_varna_approx_address_search.md`](001_fire_varna_approx_address_search.md)
or ADR [`002_osm_pmtiles_basemap_offline.md`](002_osm_pmtiles_basemap_offline.md).

## Context

Petar, 02.09.2026 (the commission, verbatim):
„като напиша „хотел адмирал" да ми излизат всички хотели Адмирал (Варна,
Св. Св. Константин и Елена, Златни); училища, университети, болници, детски
градини — професионално и без да чупим нищо работещо; не измисляме нищо; сигурен
механизъм за регресии; първо ЛОКАЛНО да го пробвам, после публикуваме."

Measured before the cycle (plan §1; baseline `scratch/places_search/baseline_02.09.md`,
manifest `scratch/places_search/manifest_before.json`):

- the varna_3d delivery `fire_varna_hotels.json` — **226** records, 83,008 B,
  sha256 `17800b5d23a6097da351b0b45808074ba9a4ab3d9183503d2fbc28a0f05c7f8f`,
  12 keys per record, 10 zones, 3 `src` values (НТР УИН 192 · Sol/OSM
  identification 22 · КАИС address field 12), 0 duplicate (name, zone) pairs,
  all three Admirals present including the registry spelling АМИРАЛ;
- the category dictionary `varna_3d/data/place_categories.json` — 264 forms → 55 chips;
- `index.html` 475,446 B, unchanged since 12.08 (`2dc43aa`); the address search
  lazy-loads `data/search_index.json` (11,242,756 B) + `data/address_rows.json`
  on first focus, under the Cache API namespace `fire-varna-search-v2`;
- test suite: `Ran 126 tests … OK`.

**Why not a minimal branch inside the existing address search.** v1 of the plan
put the hotels inside `resolveAndRender`. The external audit (Sol, 02.09) returned
it on seven measured points, each a consequence of sharing the address code path:

1. `exactComplete` returns before any hotel code could run — for „адмирал", „парк",
   „бриз" the hotels would never be reached at all;
2. `selectResult` has no notion of a hotel row — selection would have to be edited
   inside their closed functions;
3. concatenating the two result arrays loses the group headers;
4. the existing cache helper does `put` before `parse` (a malformed answer poisons
   the good cache), has no timeout, and is written for the old 144/11 delivery;
5. the two result limits collide, and the address matcher's token rules mis-hit a
   place class („блок с" → АРАБЕЛА, „402");
6. a late response can revive a list the human has already dismissed;
7. the selection side effects (`detailAbort`, the standalone popup, Escape bound to
   the input) are not composable from the outside.

Sharing the path therefore meant editing `runGeocoderSearch` / `renderResults` /
`renderCombined` / `resolveAndRender` / `selectResult` / `fetchCachedJson` — the code
a fire crew's address lookup depends on, in an app used at incidents. The decision
below buys the new result class at the price of a second, self-contained code path
instead: **separate branch, own container, own cache, own selection.**

## Decision

**D1 — Two byte-copied data files; nothing is hand-edited in this repo.**
`data/hotels.json` is a byte copy of the delivery (226 records, 83,008 B, sha256
`17800b5d23a6097da351b0b45808074ba9a4ab3d9183503d2fbc28a0f05c7f8f`, 12 keys).
`data/place_categories.json` is a byte copy of `varna_3d/data/place_categories.json`
(264 forms / 55 chips); its sha256 is measured when the copy is made (commit C2) and
**pinned in `tests/test_hotels_public_bundle.py`** (commit C3). Both are lazy —
fetched on the first focus of the search field, never inlined into `index.html`,
never part of the first load. Corrections go back to the source in varna_3d, never
into these copies.

**D2 — Validation fails closed towards absence, never towards a broken session.**
On load: `{_meta, hotels}`, `_meta.count === hotels.length === 226`, exactly the 12
keys per record, finite `lat/lon` inside the delivery box 43.13–43.35 / 27.65–28.10
(the canon of `qa_fire_varna_export.py`), non-empty `name`, `kind` ∈ the four values,
`src` ∈ the three, `status` ∈ {„", „бивш"}, zero matches of the cadastral pattern
`\b\d{4,5}\.\d+\.\d+` in the raw text, non-empty `_meta.licence`; for the dictionary
`_meta.schema === 1` and a `forms` object. An invalid file means *no places for the
moment* plus a retry on the next focus — never a disabled session, and never any
effect on the address results, which by construction call nothing of ours.

**D3 — Own cache helper, own namespace.** `fetchValidatedJson(url, validate)`:
fetch → `text()` → `JSON.parse` → validate → SHA-256 content check against constants
pinned in `index.html` (§12 В7) → **only then** `put`. `AbortController` with an
8,000 ms budget covering both the fetch and the body read; a body over 2,000,000 B is
rejected before parse; every Cache API call is raced with 2 s and is best-effort;
lookups happen only inside the opened namespace (the global `caches.match` is
forbidden — ADR 005 D3); an invalid cache entry is ignored rather than deleted, so
two tabs cannot race. Namespace: **`fire-varna-hotels-v2-226`** — new, and distinct
from `fire-varna-search-v2` and `fire-varna-approx-addresses-v1`. **`sw.js` is not
touched in this cycle** (see Obligations).

**D4 — Own container, own CSS, their code byte-untouched.** A new IIFE
`initPlacesSearch()` immediately after `initAddressSearch()`; one new element,
`<div id="placesSearchResults" class="search-results places-results" role="listbox" aria-label="Хотели">`,
as a sibling **after** `#addrSearchResults`; an own CSS block (`.places-results`,
`.pl-*`, `.place-pin`, `.place-popup`). No `asr-*` / `search-pin*` selector and no
function of `initAddressSearch` is edited — the diff gate G3 and D12 below enforce it.

**D5 — Own positioning, computed from what is visible** (§12 В6): with their list
visible, `top = theirs.offsetTop + theirs.offsetHeight`; otherwise the CSS default
`top: calc(100% - 2px)`; height `= innerHeight − ourRect.top − 12` (a hidden
container measures 0, so 32vh off a hidden sibling was wrong). Re-computed on our
render, on every mutation of `#addrSearchResults`, and on resize; verified at
375×812 in the probe.

**D6 — Exactly one DOM touch inside their container** (§12 В5): when we show at
least one row and their container's only child is `.asr-status` with the text
`Няма съвпадения`, we remove `.visible` from it — the offline message stays visible,
because it is information. The flag `tidiedByUs` is persistent until their next
mutation. We never add or delete a node of theirs.

**D7 — Selection is ours, and it does not restore the query text** (§12 В1). On pick:
hide our list; clear their slot through its **public contract** — a synthetic,
non-bubbling `Escape` keydown on the input, which removes their list, marker, panel,
popup and pending debounce; the field is left empty and unfocused, so every late
`runQuery` / `resolveAndRender` / `tryCoordQuery` / `ensureApproxData` aborts on its
own stale guard. Then `anchorHydrantsAt(lat, lon)` re-ranks the hydrants around the
place (the operational payoff), an own orange `.place-pin` (`L.divIcon`), `setView`
at zoom ≥ 17, and an own popup carrying: the name (+ „ (бивш)"), kind · category ·
beds · zone, the old name („старо: …"), `buildNavActions`, and the **source line**,
verbatim per `src` class:

- НТР → `име: Национален туристически регистър · координати: КАИС Отворени данни (АГКК)`
- КАИС → `име: КАИС адресно поле (АГКК) · координати: КАИС Отворени данни (АГКК)`
- Sol/OSM → `име: публична идентификация (OSM, официални сайтове, общински регистри) · координати: КАИС Отворени данни (АГКК)`

Our popup re-opens itself if something else closes it while our selection is active.

**D8 — Our state is cleared by their actions, not by guesswork** (§12 В2/В3): a
`MutationObserver` on `markerPane` reacting **only** to an added node carrying
`search-pin-wrapper` or `approx-pin-wrapper` (hydrant, user dot and entrance pins do
not trigger it); a capture-phase click on `.asr-item`; their container losing
`.visible` other than by our tidy; a trusted `Escape`; an empty field; a click
outside `.search-bar`. A lazily-attached observer on `#detailSheet` repeats the
synthetic Escape and re-opens our popup if a delayed `/detail/` response shows their
panel over our selection.

**D9 — Enter is ours only when they have already said „Няма съвпадения" for the very
same text** (§12 В4): we record `theirStatusFor` at the moment their container
becomes status-only with exactly that text, and a trusted Enter picks our first row
only if `shownFor === q && theirStatusFor === q`. Otherwise we stay silent — the
address wins. No `stopPropagation` anywhere.

**D10 — Generation and dismissal.** A generation counter bumps on every input; a
render happens only for the current generation and only while not dismissed; every
human-initiated hide sets `dismissed`, the next input clears it. A late answer can
never resurrect a closed list.

**D11 — Fail-soft by construction, and one kill switch.** Every listener body is
wrapped in `try/catch` with a single `console.warn('[places-search] …')`; nothing of
ours is called from their code. The feature is gated by **`HOTELS_SEARCH_ENABLED`**,
signed as `true`; setting it to `false` makes the IIFE return on its first line, and
the app behaves exactly as it does today — the kill switch does not require a revert.

**D12 — Named untouchables.** `data/search_index.json`, `data/address_rows.json`,
`data/hydrants.json`, `data/approx_addresses_v1.json`, `sw.js`, `worker/`, the two
existing feature flags, the hydrant view modes, the report flow, the compass, every
`asr-*` / `search-pin*` selector and every function of `initAddressSearch`. The gate:
the C4 diff contains no line of theirs (`git diff -U0 | grep -c '^-' ≤ 2`, both in
the HTML/CSS wrapper only), and the address-search probe corpus is byte-identical
before and after (G3).

**Matching — "the KEY" (plan §3, as amended by §10 and §11).** A form from the
category dictionary is a *key* only if its class has at least one loaded record;
the leftmost key names the class, further key words are treated as name words.
Inside a class the search is generous (exact 3 / prefix 2 / Levenshtein ≤ 2 for words
of ≥ 4 original characters, any order, one significant word is enough); a zone
distinguishes but never finds on its own; purely numeric tokens never vote alone
without a key; aliases match as tokens minus address markers. The tokenizer is
shared by names and queries, and the three primitives it reuses (`norm`, `skel`,
`lev`) are **verbatim copies** of the address-search ones, gated byte-for-byte by
`tests/test_places_search_primitives.py` (G12а) — the address functions are closed
over their IIFE and must not be exported.

## Licence and privacy position

Q8 answered **YES** by the signature: the НТР facts (name, kind, category, beds,
zone, position) are published in this public repo **without naming a licence** —
they are facts from a public state register, republished with the verbatim
attribution line per `src` class (D7) and with the delivery's own `_meta.licence`
reproduced **byte-equal** in `README.md` (commit C5, gate G9). The bundle carries no
cadnum, no КАИС identifier and no free-text PII; `tests/test_hotels_public_bundle.py`
scans for the cadastral pattern, for PII in free text, and for (name, zone)
uniqueness, and is proven by being made to fail on three deliberately corrupted
copies before it is trusted (G2). Phase 2 does **not** inherit this position: the
varna_3d POI file is ODbL 1.0 with named attribution (§11 Б4(5)), so its records
will need their own source line and their own licence decision.

## Consequences

- A second search code path exists in `index.html`. It duplicates three small
  primitives on purpose (D12 / G12а pins them), and it costs ≤ 300 added lines /
  ≤ 12,000 B for C4 (measured and reported; over budget splits out C4b).
- The address search keeps its exact behaviour, proven per query by the probe
  corpus (G3: full `outerHTML` sequence plus the backing identity of every visible
  row — nav coordinates, `/detail/{g}` URL, popup title — cold and warm cache,
  hotel-first and address-first, 404 / malformed / held body / stale cache).
- First load is unchanged (G6): neither new file is fetched before the first focus.
- **Visible to Petar at Gate 2:** after choosing a place the search field is left
  empty (choosing an *address* leaves the text, as today) — the price of clearing
  their slot through the public Escape contract instead of reaching into their
  closures.
- Known boundaries, stated rather than hidden: the coordinate "stale row" on Enter
  is their pre-existing behaviour and is not touched; a zone without a key finds
  nothing on our side by decision (§11 Б3); the two overlays can overlap for a
  single observer tick in the hotel-first race (recorded by the probe, not gated).
- The hotels are **not** in the offline pack — `sw.js` is untouched, so an offline
  device has the address search and the hydrants but no places. README says this
  plainly (C5).

## Rollback

Per commit, each reverts on its own (`git revert`), and the series is bisectable:

- `git revert C4` (and `C4b`, if it exists) — removes the whole feature: the IIFE,
  the container, the CSS.
- `git revert C3` — removes the two test files.
- `git revert C2` — removes `data/hotels.json` and `data/place_categories.json`.
- `git revert C5` — removes the README section.
- Without any revert: set `HOTELS_SEARCH_ENABLED = false` (D11) — one line, today's
  behaviour, data files inert on disk.
- The revert of the data commit is *proven* before C4 lands, in a throwaway
  worktree (`git worktree add`, `git revert --no-edit`, clean `git status`,
  `git worktree remove`) — never with `amend` / `reset` / `gc` / `push`.
- Publishing to GitHub is irreversible in practice, which is why **no agent pushes**:
  Petar publishes after his own 375 px run (Gate 2).

## Obligations

1. **ADR 005 cycle:** add `fire-varna-hotels-v2-226` to `PROTECTED_CACHES` in `sw.js`
   (ADR 005 D6 today lists only `fire-varna-search-v2` and
   `fire-varna-approx-addresses-v1`). Not done here — `sw.js` is outside this cycle's
   write-set; until then the namespace is deletable by a worker `activate`, which is
   harmless (the file re-fetches) but must not be forgotten when the worker is armed.
2. **Pin the second sha:** `data/place_categories.json`'s sha256 is measured at C2 and
   written into `tests/test_hotels_public_bundle.py` at C3; `index.html` carries
   `HOTELS_SHA256` / `CATS_SHA256` and gate G12г proves the constants equal the files.
3. **README (C5):** the delivery's `_meta.licence` byte-equal, in BG and EN, plus the
   honest note that the places are not part of the offline pack.
4. **Phase 2 (health / education / universities)** stays plan-only until a separate
   signature: the funnel measurement, the chip audit and de-duplication in the source
   (varna_3d, never in the client), the PII filter with its institution exception, the
   ODbL source line, and a licence line per register (МОН, ИАМН/РЗИ, НАОА) — plan §8
   and §11 Б4.
5. **Data corrections** (e.g. the „ГОЛДЪН ЛАЙН/Явор" pair, the double space in
   „ХОТЕЛ  ХЕЛИОС СПА") belong to varna_3d and re-enter here only as a new byte copy
   with a new sha and a new commit.
6. **Gate 2 is still open:** Petar's local run at 375 px (the three hydrant modes,
   the report, follow mode, his own query list) and the push are his alone.
