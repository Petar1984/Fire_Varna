    function norm(s){return (''+(s||'')).toLowerCase().replace(/блок/g,'бл').replace(/вход/g,'вх').replace(/[.№,'"-]/g,' ').replace(/\s+/g,' ').trim();}
    function skel(w){w=w.toLowerCase();var C={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'};var o='';for(var i=0;i<w.length;i++){o+=(C[w[i]]!==undefined?C[w[i]]:w[i]);}return o.replace(/[yj]/g,'i').replace(/(\D)\1+/g,'$1');}
    function lev(a,b,cap){var la=a.length,lb=b.length;if(Math.abs(la-lb)>cap)return cap+1;var prev=[];for(var j=0;j<=lb;j++)prev[j]=j;for(var i=1;i<=la;i++){var cur=[i],best=i;for(var j=1;j<=lb;j++){var v=Math.min(prev[j]+1,cur[j-1]+1,prev[j-1]+(a[i-1]===b[j-1]?0:1));cur[j]=v;if(v<best)best=v;}if(best>cap)return cap+1;prev=cur;}return prev[lb];}
    // ADR 032 A2 per-(query token) match-KIND classifier (verbatim from
    // searchLogic.js): 3 exact / 2 prefix / 1 within-cap fuzzy. The geocoder route
    // ranks on match KIND, so a binary matchSet is insufficient.
    function matchKindSet(qt, VOCAB){var s={},cap=qt.length>=7?2:1;for(var i=0;i<VOCAB.length;i++){var v=VOCAB[i],k=0;if(v===qt)k=3;else if(qt.length<=1)k=0;else if(v.indexOf(qt)===0)k=2;else if(qt.length<=3)k=0;else if(lev(qt,v,cap)<=cap)k=1;if(k)s[v]=k;}return s;}
    function buildAddressFieldIndex(payload){
      const order = payload && Array.isArray(payload.field_order) ? payload.field_order : null;
      if (!order) throw new Error('address_rows.json missing field_order');
      const idx = {};
      ['normalized_address', 'lat', 'lng'].forEach(function (name) {
        const i = order.indexOf(name);
        if (i === -1) throw new Error('address_rows.json field_order missing "' + name + '"');
        idx[name] = i;
      });
      return idx;
    }

    // formatAddressHit — label resolution chain (privacy-safe):
    //   (1) the public geocoder `label` (= cleaned addr_key) when present;
    //   (2) else addressRows[display_id].normalized_address (the separate display
    //       payload, indexed by the source row id);
    //   (3) else the район name; NEVER a cadnum / section / complex id (the index
    //       carries none). An entrance (kind:"mf" + en) appends " · вх. <en>" to its
    //       parent building's resolved address.
    function prettyKey(s){ return String(s).replace(/\|/g, ' ').replace(/\s+/g, ' ').trim(); }
    function baseAddressLabel(hit){
      if (hit.label) return prettyKey(hit.label);
      if (hit.display_id != null && addressRows && addrFieldIdx) {
        const row = addressRows[hit.display_id];
        if (Array.isArray(row)) {
          const na = row[addrFieldIdx.normalized_address];
          if (na) return na;
        }
      }
      if (hit.d != null && districtNames[hit.d]) return districtNames[hit.d];
      return '(адрес)';
    }
    function formatAddressHit(hit){
      const base = baseAddressLabel(hit);
      const isEntrance = hit.kind === 'mf' && hit.en != null && hit.en !== undefined;
      return isEntrance ? base + ' · вх. ' + hit.en : base;
    }
    // dedupeDisplayRows/labelBlockNumber) — dropdown DISPLAY dedup, applied by
    // renderResults over the RANKED rows. Fixes two display defects without touching
    // the matcher: (a) identical rows — an entrance-token query bypasses grouping,
    // so one block's N footprint sections render N identical rows; key =
    // (normalized rendered label, g-or-null), first (highest-ranked) wins. Distinct
    // groups with a colliding bare label have distinct g and never fold. (b) a
    // redundant адрес row (no g, never consolidated) is suppressed ONLY when a
    // сграда row (mf, no en) whose label carries the SAME block number is present in
    // the same list. Block extraction mirrors the producer's canon(): norm -> skel,
    // the token after "bl" holding a digit — Cyrillic and Latin labels judge alike.
    function labelBlockNumber(label) {
      const toks = norm(String(label == null ? '' : label)).split(/\s+/).filter(Boolean).map(skel);
      const i = toks.indexOf('bl');
      const nx = i >= 0 && i + 1 < toks.length ? toks[i + 1] : null;
      return nx && /[0-9]/.test(nx) ? nx : null;
    }
    function dedupeDisplayRows(rows) {
      if (!Array.isArray(rows) || rows.length === 0) return rows;
      const labels = rows.map(function (r) { return String(formatAddressHit(r)); });
      const sgradaBlocks = new Set();
      for (let i = 0; i < rows.length; i++) {
        const r = rows[i];
        if (r && r.kind === 'mf' && (r.en == null || r.en === undefined)) {
          const bn = labelBlockNumber(labels[i]);
          if (bn != null) sgradaBlocks.add(bn);
        }
      }
      const seen = new Set();
      const out = [];
      for (let i = 0; i < rows.length; i++) {
        const r = rows[i];
        if (r && r.kind === 'address') {
          const bn = labelBlockNumber(labels[i]);
          if (bn != null && sgradaBlocks.has(bn)) continue; // same-block сграда present
        }
        const key = norm(labels[i]) + '||' + (r && r.g != null ? String(r.g) : '');
        if (seen.has(key)) continue;                        // identical rendered row
        seen.add(key);
        out.push(r);
      }
      if (rows.blockHeader) out.blockHeader = rows.blockHeader;
      if (rows.bareBlockHeader) out.bareBlockHeader = rows.bareBlockHeader;
      return out;
    }
    // ---- ported runGeocoderSearch (public-safe geocoder route) ------------------
    // Transplanted from Varna_buildings app/modules/search/searchLogic.js. The ONLY
    // adaptations: the group key `bg||complex_id` -> the opaque `g`; the cadnum /
    // section_cadnum determinism tie-breaks -> a stable runtime `_ord`; the inverted
    // index + area-vocab are rebuilt CLIENT-SIDE (payload omits inverted); dropped
    // fields (life_safety_rank / physical_building_id / quarter_assignment_trust /
    // odem) are absent, leaving their comparator/dedup slots inert (null-safe).
    // Result rows carry ONLY safe fields + label/display_id for resolution.
    const SEARCH_LIMIT = 8;

    // Build vocab (if absent), the inverted index, the area-vocab, and stamp a stable
    // `_ord` on every entry. Called ONCE after the payload loads.
    function prepareIndex(index){
      if (!index || !Array.isArray(index.entries)) return index;
      for (let i = 0; i < index.entries.length; i++) index.entries[i]._ord = i;
      if (!Array.isArray(index.vocab)) {
        const set = new Set();
        for (const e of index.entries) for (const f of ['tk','qtk','alias_tk','dtk','stk']) { const a = e[f]; if (a) for (const t of a) if (t) set.add(t); }
        index.vocab = Array.from(set).sort();
      }
      const postings = new Map();
      for (let i = 0; i < index.entries.length; i++) {
        const e = index.entries[i];
        let toks = e.tk || [];
        if (e.qtk) toks = toks.concat(e.qtk);
        if (e.alias_tk) toks = toks.concat(e.alias_tk);
        if (e.dtk) toks = toks.concat(e.dtk);
        if (e.stk) toks = toks.concat(e.stk);
        for (const t of toks) { let ids = postings.get(t); if (!ids) postings.set(t, (ids = [])); if (ids[ids.length-1] !== i) ids.push(i); }
      }
      const inverted = {};
      for (const t of index.vocab) inverted[t] = postings.get(t) || [];
      index.inverted = inverted;
      const av = new Set();
      for (const e of index.entries) for (const f of ['dtk','qtk','stk']) { const a = e[f]; if (a) for (const t of a) if (t) av.add(t); }
      index._areaVocab = av;
      return index;
    }

    function runGeocoderSearch(query, index){
      if (!index || !Array.isArray(index.entries)) return [];
      const qn = norm(query);
      if (qn.length < 1) return [];
      const rawToks = qn.split(/\s+/).filter(Boolean);
      const toks = rawToks.map(skel);
      if (toks.length === 0) return [];

      const blIdx = toks.indexOf('bl');
      const qBlk = blIdx >= 0 && blIdx+1 < toks.length ? toks[blIdx+1] : null;
      const qBlkDisplay = blIdx >= 0 && blIdx+1 < rawToks.length ? rawToks[blIdx+1] : null;
      const av = index._areaVocab || new Set();
      const areaPresent = qBlk != null && toks.some(function (t) { return t !== 'bl' && t !== 'vh' && t !== qBlk && av.has(t); });
      const areaBlockTyped = qBlk != null && areaPresent;
      const bareBlockTyped = qBlk != null && !areaPresent && !toks.includes('vh') && toks.every(function (t) { return t === 'bl' || t === qBlk; });
      const blockTyped = areaBlockTyped;

      // F1 (search-quality cycle, frame §6 2026-07-02; ported from searchLogic.js) —
      // entrance-TYPED query detection: an EXPLICIT вх/vh token FOLLOWED by an
      // entrance designator (a number "9"/"11", number+letter "1а", or a single
      // letter "а"/"b"). A dangling "вх" or "вх <word>" is NOT entrance-typed.
      // Consumed ONLY by comparator slot (4) below: an entrance-typed query ranks
      // the matched entrance child ABOVE an equal-relevance non-entrance row, so
      // Enter on "бл 307 вх 9" selects the вход child, not the "вх 9-11" адрес row.
      // Every other query keeps slot (4) byte-identical.
      const vhIdx = toks.indexOf('vh'); // skel('вх') === skel('vh') === 'vh'
      const entranceTyped =
        vhIdx >= 0 && vhIdx + 1 < rawToks.length &&
        /^(?:[0-9]+[a-zа-я]?|[a-zа-я])$/.test(rawToks[vhIdx + 1]);

      let vocab = index.vocab;
      if (!Array.isArray(vocab)) { const set = new Set(); for (const e of index.entries) for (const t of (e.tk||[])) if (t) set.add(t); vocab = Array.from(set); }
      const inverted = index.inverted && typeof index.inverted === 'object' ? index.inverted : null;

      const ms = toks.map(function (t) { return matchKindSet(t, vocab); });
      const numericTok = toks.map(function (t) { return /^[0-9]+$/.test(t); });

      let candidateIds = null;
      if (inverted) { candidateIds = new Set(); for (const m of ms) { for (const vt in m) { const ids = inverted[vt]; if (ids) for (let i = 0; i < ids.length; i++) candidateIds.add(ids[i]); } } }

      const scored = [];
      const scoreEntry = function (e) {
        if (!e) return;
        let matched = 0, exactName = 0, exactNum = 0, prefix = 0, fuzzy = 0, matchedCore = 0, matchedViaDtk = 0, matchedViaStk = 0;
        let qBlkMatched = false, all = true;
        const tk = e.tk || [], qtk = e.qtk || null, atk = e.alias_tk || null, dtk = e.dtk || null, stk = e.stk || null;
        for (let qi = 0; qi < toks.length; qi++) {
          const m = ms[qi]; let best = 0;
          for (let ti = 0; ti < tk.length; ti++) { const k = m[tk[ti]]||0; if (k > best) { best = k; if (best === 3) break; } }
          if (atk && best < 3) { for (let ti = 0; ti < atk.length; ti++) { const k = m[atk[ti]]||0; if (k > best) { best = k; if (best === 3) break; } } }
          if (best > 0) matchedCore += 1;
          if (qtk && best < 3) { for (let ti = 0; ti < qtk.length; ti++) { const k = m[qtk[ti]]||0; if (k > best) { best = k; if (best === 3) break; } } }
          if (dtk && best < 3) { for (let ti = 0; ti < dtk.length; ti++) { const k = m[dtk[ti]]||0; if (k > best) { best = k; matchedViaDtk += 1; if (best === 3) break; } } }
          if (stk && best < 3) { for (let ti = 0; ti < stk.length; ti++) { const k = m[stk[ti]]||0; if (k > best) { best = k; matchedViaStk += 1; if (best === 3) break; } } }
          if (best === 0) { all = false; continue; }
          matched += 1;
          if (blockTyped && toks[qi] === qBlk) qBlkMatched = true;
          if (best === 3) { if (numericTok[qi]) exactNum += 1; else exactName += 1; } else if (best === 2) prefix += 1; else fuzzy += 1;
        }
        if (matched > 0) {
          const dem = e.quarter_assignment_trust === 'conflicted' && matchedCore === 0 ? 1 : 0;
          const ddem = matchedCore === 0 && matchedViaDtk > 0 ? 1 : 0;
          const odem = e.odem ? 1 : 0;
          const sdem = matchedCore === 0 && matchedViaStk > 0 ? 1 : 0;
          const bmatch = blockTyped && (e.btk || []).includes(qBlk) ? 1 : 0;
          scored.push({ e: e, matched: matched, exactName: exactName, exactNum: exactNum, prefix: prefix, fuzzy: fuzzy, all: all, dem: dem, ddem: ddem, sdem: sdem, odem: odem, bmatch: bmatch, qBlkMatched: qBlkMatched ? 1 : 0, bdem: 0 });
        }
      };
      if (candidateIds) { for (const id of candidateIds) scoreEntry(index.entries[id]); }
      else { for (const e of index.entries) scoreEntry(e); }

      const existsBtkHolder = blockTyped && scored.some(function (s) { return s.bmatch === 1; });
      if (existsBtkHolder) { for (const s of scored) s.bdem = (s.qBlkMatched === 1 && s.bmatch === 0) ? 1 : 0; }

      scored.sort(function (a, b) {
        if (a.all !== b.all) return a.all ? -1 : 1;
        if (b.matched !== a.matched) return b.matched - a.matched;
        if (b.exactName !== a.exactName) return b.exactName - a.exactName;
        if (b.exactNum !== a.exactNum) return b.exactNum - a.exactNum;
        if (b.prefix !== a.prefix) return b.prefix - a.prefix;
        if (a.bdem !== b.bdem) return a.bdem - b.bdem;
        if (a.dem !== b.dem) return a.dem - b.dem;
        if (a.ddem !== b.ddem) return a.ddem - b.ddem;
        if (a.sdem !== b.sdem) return a.sdem - b.sdem;
        if (a.odem !== b.odem) return a.odem - b.odem;
        const aRank = a.e.life_safety_rank == null ? 2 : a.e.life_safety_rank;
        const bRank = b.e.life_safety_rank == null ? 2 : b.e.life_safety_rank;
        if (aRank !== bRank) return aRank - bRank;
        const aEnt = a.e.en !== undefined, bEnt = b.e.en !== undefined;
        // F1 — direction-gated slot (4): typed-entrance queries rank the entrance
        // child first at equal relevance; all other queries keep the pre-existing
        // "precise before entrance" demotion byte-identical.
        if (aEnt !== bEnt) {
          if (entranceTyped) return aEnt ? -1 : 1;
          return aEnt ? 1 : -1;
        }
        const al = (a.e.tk||[]).length + (a.e.qtk ? a.e.qtk.length : 0);
        const bl = (b.e.tk||[]).length + (b.e.qtk ? b.e.qtk.length : 0);
        if (al !== bl) return al - bl;
        return (a.e._ord||0) - (b.e._ord||0); // determinism (cadnum dropped)
      });

      // physical_building dedup: physical_building_id is DROPPED -> pbid always null
      // -> every row passes through (the block is inert but preserved verbatim).
      const isEntranceQuery = toks.includes('vh');
      let ranked = scored;
      if (!isEntranceQuery) {
        const reps = index.physical_building_reps && typeof index.physical_building_reps === 'object' ? index.physical_building_reps : {};
        const rankOf = function (s) { return s.e.life_safety_rank == null ? 2 : s.e.life_safety_rank; };
        const trueTie = function (a, b) { return a.all === b.all && a.matched === b.matched && a.exactName === b.exactName && a.exactNum === b.exactNum && a.prefix === b.prefix && a.bdem === b.bdem && a.dem === b.dem && a.ddem === b.ddem && a.sdem === b.sdem && a.odem === b.odem && rankOf(a) === rankOf(b); };
        const keptPos = new Map(); ranked = [];
        for (const s of scored) {
          const pbid = s.e.physical_building_id;
          if (pbid == null || s.e.en !== undefined) { ranked.push(s); continue; }
          if (!keptPos.has(pbid)) { keptPos.set(pbid, ranked.length); ranked.push(s); continue; }
          const pos = keptPos.get(pbid), kept = ranked[pos];
          if (String(s.e._ord) === String(reps[pbid]) && String(kept.e._ord) !== String(reps[pbid]) && trueTie(kept, s)) ranked[pos] = s;
        }
      }

      // area-gated block GROUPING (opaque g instead of bg||complex_id).
      let blockHeader = null;
      if (blockTyped && !isEntranceQuery) {
        const seen = new Set(); const grouped = []; let blockGroups = 0; const districtCount = new Map();
        for (const s of ranked) {
          const key = s.e.g;
          if (key != null) { if (seen.has(key)) continue; seen.add(key); }
          grouped.push(s);
          if (s.all && s.bmatch === 1) { blockGroups += 1; const d = s.e.d; if (d != null) districtCount.set(d, (districtCount.get(d)||0)+1); }
        }
        ranked = grouped;
        if (blockGroups > 0) { let bestD = null, bestN = -1; for (const pair of districtCount) if (pair[1] > bestN) { bestN = pair[1]; bestD = pair[0]; } blockHeader = { block: qBlkDisplay, count: blockGroups, district_enum: bestD }; }
      }

      // bare-block surface (parent/child), grouped by opaque g.
      if (bareBlockTyped) {
        const parentCandidates = [];
        for (const s of ranked) if (s.all && s.e.en === undefined && (s.e.btk || []).includes(qBlk)) parentCandidates.push(s);
        if (parentCandidates.length > 0) {
          const repByGroup = new Map();
          for (const s of parentCandidates) { const key = s.e.g; if (key == null) continue; if (!repByGroup.has(key)) repByGroup.set(key, s); }
          const childrenByGroup = new Map();
          for (const s of ranked) { if (s.e.en === undefined) continue; const key = s.e.g; if (key == null || !repByGroup.has(key)) continue; if (!childrenByGroup.has(key)) childrenByGroup.set(key, []); childrenByGroup.get(key).push(s); }
          const childSort = function (a, b) { const na = /^[0-9]+$/.test(a.e.en) ? parseInt(a.e.en,10) : NaN, nb = /^[0-9]+$/.test(b.e.en) ? parseInt(b.e.en,10) : NaN; const an = !Number.isNaN(na), bn = !Number.isNaN(nb); if (an && bn && na !== nb) return na - nb; if (an !== bn) return an ? -1 : 1; if (a.e.en !== b.e.en) return String(a.e.en).localeCompare(String(b.e.en)); return (a.e._ord||0) - (b.e._ord||0); };
          const bareDistrictCount = new Map(); const groupList = [];
          for (const pair of repByGroup) { const key = pair[0], rep = pair[1]; const children = (childrenByGroup.get(key) || []).slice().sort(childSort); groupList.push({ key: key, rep: rep, children: children }); const d = rep.e.d; if (d != null) bareDistrictCount.set(d, (bareDistrictCount.get(d)||0)+1); }
          groupList.sort(function (a, b) { const da = a.rep.e.d == null ? Infinity : a.rep.e.d, db = b.rep.e.d == null ? Infinity : b.rep.e.d; if (da !== db) return da - db; return (a.rep.e._ord||0) - (b.rep.e._ord||0); });
          const projectRow = function (s, role) { const e = s.e; return { kind: e.kind, en: e.en, pin: e.pin, d: e.d, label: e.label, display_id: e.display_id, g: e.g, allTokens: s.all, matched: s.matched, exact: s.exactName + s.exactNum, prefix: s.prefix, fuzzy: s.fuzzy, bareRole: role, block: qBlkDisplay }; };
          const bareOut = [];
          for (const g of groupList) { bareOut.push(projectRow(g.rep, 'parent')); for (const c of g.children) bareOut.push(projectRow(c, 'child')); }
          bareOut.bareBlockHeader = { block: qBlkDisplay, groups: groupList.length, districts: Array.from(bareDistrictCount, function (p) { return { district_enum: p[0], count: p[1] }; }).sort(function (a, b) { return a.district_enum - b.district_enum; }) };
          return bareOut;
        }
      }

      const out = ranked.slice(0, SEARCH_LIMIT).map(function (s) {
        const e = s.e;
        return { kind: e.kind, en: e.en, pin: e.pin, d: e.d, label: e.label, display_id: e.display_id, g: e.g, allTokens: s.all, matched: s.matched, exact: s.exactName + s.exactNum, prefix: s.prefix, fuzzy: s.fuzzy };
      });
      if (blockHeader) out.blockHeader = blockHeader;
      return out;
    }

    // ---- lazy load + cache (memory for the session + Cache API offline) ----------
    // TWO payloads: the matcher index (search_index.json) + the display rows
    // (address_rows.json). Both lazy-load on first focus, are parsed once, and are
    // persisted to the Cache API so a return visit works offline. The index is only
    // published to `searchIndex` AFTER prepareIndex() finishes (so a racing query
    // never sees a half-built inverted index).
    const SEARCH_INDEX_URL = 'data/search_index.json';
    const ADDRESS_ROWS_URL = 'data/address_rows.json';
    const SEARCH_CACHE = 'fire-varna-search-v2'; // v2 = geocoder payload (v1 was section_units)