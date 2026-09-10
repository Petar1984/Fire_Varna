#!/usr/bin/env python3
"""Build the moderation dashboard for every hydrant report ever filed.

Reads the issues straight from the GitHub API (public repo, no auth) and writes
a single self-contained HTML page: the figures, when reports come in by day and
by hour, the split by report type, the roster of reporters, and a searchable log
of all of them with their notes. Each row links to its issue and to the hydrant
on the live map.

Run at the END of a /firehydrants cycle, after the issues are closed, so the
page reflects the cycle that just landed:

    python scripts/build_reports_dashboard.py --out <path>/dash.html

Then republish that file to the SAME artifact URL so Petar keeps one link.

Deliberately NOT committed to the site: the page names all 35 reporters, and
the project's PII gate keeps reporter identities out of anything published from
the repo (`reporters_private.md` is gitignored for the same reason). The page is
generated on demand and published as a private artifact instead.
"""
from __future__ import annotations
import argparse, collections, datetime, io, json, re, sys, urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

API = "https://api.github.com/repos/Petar1984/Fire_Varna/issues"


def fetch_issues():
    """Every issue, open and closed, oldest page last. 100 per request."""
    out = {}
    for page in range(1, 40):
        url = "%s?state=all&per_page=100&page=%d" % (API, page)
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "fire-varna-dashboard/1.0",
        })
        with urllib.request.urlopen(req, timeout=60) as resp:
            batch = json.loads(resp.read().decode("utf-8"))
        if not batch:
            break
        for i in batch:
            if "pull_request" not in i:
                out[i["number"]] = i
        if len(batch) < 100:
            break
    if not out:
        raise SystemExit("GitHub returned no issues - rate limited?")
    return out


def field(body, key):
    m = re.search(r"^" + key + r":\s*(.*)$", body or "", re.M)
    if not m:
        return None
    v = m.group(1).strip()
    if v in ("null", "~", ""):
        return None
    return v.strip('"').replace('\\"', '"')


def normalise(issues):
    rows = []
    for n, i in sorted(issues.items()):
        b = i.get("body") or ""
        note = None
        for k in ("damage_description", "description", "terrain_description", "free_text"):
            v = field(b, k)
            if v:
                note = v
                break
        if not field(b, "report_type"):
            # Not a field report. #1-#7 were opened when the repo was set up and
            # their titles are the label names themselves ("report",
            # "new-hydrant", ...); they carry no body at all. Counting them
            # inflates the total and shows seven hydrants with no location that
            # never had one.
            continue
        rows.append({"n": n, "t": field(b, "report_type"), "who": field(b, "reporter") or "?",
                     "ts": field(b, "timestamp") or i["created_at"], "created": i["created_at"],
                     "note": note, "type": field(b, "type"),
                     "op": field(b, "operational_status"), "ref": field(b, "hydrant_ref")})
    return rows


TYPE_BG = {
    "exists_confirmed": "Хидрантът е там",
    "new_hydrant": "Нов хидрант",
    "wrong_location": "Грешна локация",
    "missing": "Липсва",
    "damaged": "Повреден",
    None: "—",
}

def local(ts):
    """Every stamp is normalised to Bulgarian time (+03:00).

    131 of the reports arrive stamped -07:00 or -08:00: that is the device
    clock behind Petar's satellite link, not the hour anyone stood at a
    hydrant. Charting the raw hour would mix two clocks and invent a spike
    after midnight, so the offset is applied and +03:00 put back on.
    """
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})[T ](\d{2}):(\d{2})(?::\d{2})?"
                 r"(Z|[+-]\d{2}:\d{2})?", ts or "")
    if not m:
        return None
    y, mo, d, h, mi = (int(x) for x in m.groups()[:5])
    off = m.group(6)
    dt = datetime.datetime(y, mo, d, h, mi)
    if off and off != "Z":
        sign = 1 if off[0] == "+" else -1
        dt -= datetime.timedelta(hours=sign * int(off[1:3]), minutes=sign * int(off[4:6]))
    dt += datetime.timedelta(hours=3)          # Europe/Sofia, the field clock
    return dt.year, dt.month, dt.day, dt.hour, dt.minute


HTML = """<title>Дневник на хидрантните доклади</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
<style>
:root{
  --bg:#f6f5f2; --surface:#fffefc; --raised:#f0eeea;
  --ink:#1a1e21; --muted:#6d7278; --faint:#9aa0a5; --line:#e2dfd9;
  --accent:#0d6a66; --accent-soft:#d6e8e6;
  --ok:#2f7d4f; --onsite:#b4432f; --dead:#24282c; --flag:#c07d16; --grey:#9aa0a5;
  --shadow:0 1px 2px rgba(26,30,33,.06), 0 8px 24px -12px rgba(26,30,33,.18);
}
:root:not([data-theme="light"]){ @media (prefers-color-scheme: dark){
  --bg:#131618; --surface:#1b1f22; --raised:#23282c;
  --ink:#e9e6e1; --muted:#9aa0a5; --faint:#6d7278; --line:#2c3236;
  --accent:#4fb5ac; --accent-soft:#1d3a38;
  --ok:#5aab77; --onsite:#d9705c; --dead:#c3c8cc; --flag:#d9a03f; --grey:#767c82;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px -12px rgba(0,0,0,.6);
}}
:root[data-theme="dark"]{
  --bg:#131618; --surface:#1b1f22; --raised:#23282c;
  --ink:#e9e6e1; --muted:#9aa0a5; --faint:#6d7278; --line:#2c3236;
  --accent:#4fb5ac; --accent-soft:#1d3a38;
  --ok:#5aab77; --onsite:#d9705c; --dead:#c3c8cc; --flag:#d9a03f; --grey:#767c82;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px -12px rgba(0,0,0,.6);
}
*{box-sizing:border-box}
body{
  background:var(--bg); color:var(--ink); margin:0;
  font-family:"IBM Plex Sans","Segoe UI",system-ui,sans-serif;
  font-size:15px; line-height:1.5; -webkit-font-smoothing:antialiased;
}
.wrap{max-width:1180px; margin:0 auto; padding:28px 20px 72px}
h1{font-size:26px; font-weight:600; margin:0; letter-spacing:-.01em; text-wrap:balance}
.sub{color:var(--muted); font-size:13.5px; margin:6px 0 0}
.mono{font-family:"IBM Plex Mono",ui-monospace,monospace; font-variant-numeric:tabular-nums}
.lab{
  font-size:10.5px; font-weight:600; letter-spacing:.09em; text-transform:uppercase;
  color:var(--faint);
}
header{
  display:flex; flex-wrap:wrap; gap:16px; align-items:flex-end;
  justify-content:space-between; padding-bottom:20px; border-bottom:2px solid var(--ink);
}
.stamp{text-align:right; font-size:12px; color:var(--muted)}

/* ---- instrument row: the numbers, unboxed, separated by rules ---- */
.figures{display:flex; flex-wrap:wrap; gap:0; margin:22px 0 30px}
.fig{padding:2px 26px; border-left:1px solid var(--line); flex:0 0 auto}
.fig:first-child{padding-left:0; border-left:0}
.fig b{display:block; font-family:"IBM Plex Mono",monospace; font-size:30px;
  font-weight:500; letter-spacing:-.02em; line-height:1.15}
.fig span{display:block; margin-top:2px}

section{margin:34px 0 0}
.head{display:flex; align-items:baseline; gap:12px; margin-bottom:14px}
.head h2{font-size:15px; font-weight:600; margin:0}
.head p{margin:0; color:var(--muted); font-size:13px}

.panels{display:grid; grid-template-columns:1.55fr 1fr; gap:24px; align-items:start}
@media (max-width:820px){ .panels{grid-template-columns:1fr} }
.panel{
  background:var(--surface); border:1px solid var(--line); border-radius:10px;
  padding:18px 18px 14px; box-shadow:var(--shadow);
}

/* ---- day bars ---- */
.days{display:flex; align-items:flex-end; gap:2px; height:132px; overflow-x:auto; padding-bottom:2px}
.day{flex:1 0 7px; min-width:7px; background:var(--accent); border-radius:2px 2px 0 0;
  opacity:.82; position:relative}
.day:hover{opacity:1}
.axis{display:flex; justify-content:space-between; margin-top:8px; font-size:11px; color:var(--faint)}

/* ---- hour clock ---- */
.hours{display:grid; grid-template-columns:repeat(24,1fr); gap:2px; align-items:end; height:96px}
.hr{background:var(--accent); opacity:.28; border-radius:2px 2px 0 0; min-height:2px}
.hr.peak{opacity:1}
.hticks{display:grid; grid-template-columns:repeat(24,1fr); gap:2px; margin-top:6px;
  font-size:9.5px; color:var(--faint); text-align:center}

/* ---- type split ---- */
.types{display:flex; flex-direction:column; gap:9px; margin-top:2px}
.trow{display:grid; grid-template-columns:118px 1fr 52px; align-items:center; gap:10px; font-size:13px}
.bar{height:9px; border-radius:5px; background:var(--raised); overflow:hidden}
.bar i{display:block; height:100%; border-radius:5px}
.t-exists_confirmed i{background:var(--ok)} .t-new_hydrant i{background:var(--accent)}
.t-wrong_location i{background:var(--flag)} .t-missing i{background:var(--onsite)}
.t-damaged i{background:var(--dead)} .t- i{background:var(--grey)}

/* ---- tables ---- */
.scroll{overflow-x:auto; border:1px solid var(--line); border-radius:10px; background:var(--surface)}
table{border-collapse:collapse; width:100%; font-size:13.5px}
th{
  text-align:left; padding:10px 12px; border-bottom:1px solid var(--line);
  font-size:10.5px; font-weight:600; letter-spacing:.09em; text-transform:uppercase;
  color:var(--faint); white-space:nowrap; background:var(--surface); position:sticky; top:0;
}
td{padding:9px 12px; border-bottom:1px solid var(--line); vertical-align:top}
tbody tr:last-child td{border-bottom:0}
tbody tr:hover{background:var(--raised)}
.num{font-family:"IBM Plex Mono",monospace; font-variant-numeric:tabular-nums; white-space:nowrap}
.note{color:var(--muted); max-width:460px}
a{color:var(--accent)}
.pill{
  display:inline-block; padding:1px 8px; border-radius:999px; font-size:11.5px;
  font-weight:500; white-space:nowrap; border:1px solid transparent;
}
.p-exists_confirmed{color:var(--ok); border-color:var(--ok); background:transparent}
.p-new_hydrant{color:var(--accent); border-color:var(--accent)}
.p-wrong_location{color:var(--flag); border-color:var(--flag)}
.p-missing{color:var(--onsite); border-color:var(--onsite)}
.p-damaged{color:var(--dead); border-color:var(--dead)}
.p-{color:var(--grey); border-color:var(--grey)}

/* ---- filters ---- */
.filters{display:flex; flex-wrap:wrap; gap:8px; margin-bottom:12px; align-items:center}
input,select{
  font:inherit; font-size:13.5px; color:var(--ink); background:var(--surface);
  border:1px solid var(--line); border-radius:7px; padding:7px 10px;
}
input:focus-visible,select:focus-visible,button:focus-visible{
  outline:2px solid var(--accent); outline-offset:1px;
}
input[type=search]{min-width:230px; flex:1 1 230px}
button{
  font:inherit; font-size:13px; cursor:pointer; color:var(--ink);
  background:var(--surface); border:1px solid var(--line); border-radius:7px; padding:7px 12px;
}
button:hover{background:var(--raised)}
.count{color:var(--muted); font-size:13px; margin-left:auto}
footer{margin-top:44px; padding-top:18px; border-top:1px solid var(--line);
  color:var(--muted); font-size:12.5px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
</style>

<div class="wrap">
<header>
  <div>
    <h1>Дневник на хидрантните доклади</h1>
    <p class="sub">Всеки сигнал, подаден през приложението — кой, кога, какво е видял.</p>
  </div>
  <div class="stamp">
    <div class="lab">Снимка към</div>
    <div class="mono" id="stamp"></div>
  </div>
</header>

<div class="figures" id="figures"></div>

<section>
  <div class="head"><h2>Кога се докладва</h2><p>по дни, и по час от денонощието</p></div>
  <div class="panels">
    <div class="panel">
      <div class="lab">Доклади на ден</div>
      <div class="days" id="days"></div>
      <div class="axis"><span id="d0"></span><span id="d1"></span></div>
    </div>
    <div class="panel">
      <div class="lab">Час на подаване</div>
      <div class="hours" id="hours"></div>
      <div class="hticks" id="hticks"></div>
    </div>
  </div>
</section>

<section>
  <div class="head"><h2>Какво се докладва</h2><p>по вид сигнал</p></div>
  <div class="panel"><div class="types" id="types"></div></div>
</section>

<section>
  <div class="head"><h2>Кой докладва</h2><p id="repcount"></p></div>
  <div class="scroll"><table id="reps">
    <thead><tr>
      <th>Докладчик</th><th class="num">Доклади</th><th class="num">Бележки</th>
      <th>Първи</th><th>Последен</th><th>Най-често</th>
    </tr></thead><tbody></tbody>
  </table></div>
</section>

<section>
  <div class="head"><h2>Всички доклади</h2><p>търси в бележките, филтрирай по човек или вид</p></div>
  <div class="filters">
    <input type="search" id="q" placeholder="Търси в бележки, ID, име…">
    <select id="fr"><option value="">Всички докладчици</option></select>
    <select id="ft"><option value="">Всички видове</option></select>
    <select id="fn"><option value="">Всички</option><option value="1">Само с бележка</option></select>
    <button id="clear">Изчисти</button>
    <span class="count" id="cnt"></span>
  </div>
  <div class="scroll"><table id="log">
    <thead><tr>
      <th class="num">#</th><th>Дата</th><th class="num">Час</th><th>Докладчик</th>
      <th>Вид</th><th>Хидрант</th><th>Бележка</th>
    </tr></thead><tbody></tbody>
  </table></div>
</section>

<footer id="foot"></footer>
</div>

<script id="payload" type="application/json">__DATA__</script>
<script>
(function(){
  var D = JSON.parse(document.getElementById('payload').textContent);
  var R = D.rows, L = D.labels;
  var N=0,T=1,WHO=2,DATE=3,HOUR=4,NOTE=5,TYP=6,OP=7,REF=8;
  document.getElementById('stamp').textContent = D.generated;

  function bg(t){ return L[t] || t || '—'; }
  function esc(s){ return String(s).replace(/[&<>"]/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }

  /* ---- figures ---- */
  var reps = {}, notes = 0;
  R.forEach(function(r){ reps[r[WHO]]=(reps[r[WHO]]||0)+1; if(r[NOTE]) notes++; });
  var span = D.span, d0 = span[0].split('-'), d1 = span[1].split('-');
  var daysSpan = Math.round((new Date(span[1]) - new Date(span[0]))/864e5) + 1;
  var figs = [
    [R.length, 'подадени сигнала'],
    [Object.keys(reps).length, 'докладчици'],
    [notes, 'с бележка'],
    [daysSpan, 'дни кампания'],
    [(R.length/daysSpan).toFixed(1), 'средно на ден']
  ];
  document.getElementById('figures').innerHTML = figs.map(function(f){
    return '<div class="fig"><b>'+f[0]+'</b><span class="lab">'+f[1]+'</span></div>'; }).join('');

  /* ---- per-day bars ---- */
  var byDay = {}; R.forEach(function(r){ byDay[r[DATE]]=(byDay[r[DATE]]||0)+1; });
  var all=[], cur=new Date(span[0]+'T00:00:00'), end=new Date(span[1]+'T00:00:00');
  while(cur<=end){ var k=cur.toISOString().slice(0,10); all.push([k, byDay[k]||0]);
    cur.setDate(cur.getDate()+1); }
  var mx = Math.max.apply(null, all.map(function(a){return a[1];}));
  document.getElementById('days').innerHTML = all.map(function(a){
    var h = a[1] ? Math.max(3, Math.round(a[1]/mx*128)) : 2;
    return '<div class="day" style="height:'+h+'px'+(a[1]?'':';opacity:.13')+'" title="'+
      a[0]+' — '+a[1]+' доклада"></div>'; }).join('');
  function bgDate(s){ var p=s.split('-'); return p[2]+'.'+p[1]+'.'+p[0]; }
  document.getElementById('d0').textContent = bgDate(span[0]);
  document.getElementById('d1').textContent = bgDate(span[1]) + ' · връх ' + mx + ' за ден';

  /* ---- hour histogram ---- */
  var hrs = new Array(24).fill(0);
  R.forEach(function(r){ hrs[r[HOUR]]++; });
  var hmx = Math.max.apply(null, hrs);
  document.getElementById('hours').innerHTML = hrs.map(function(v,i){
    return '<div class="hr'+(v===hmx?' peak':'')+'" style="height:'+
      Math.max(2, Math.round(v/hmx*92))+'px" title="'+i+':00 — '+v+' доклада"></div>'; }).join('');
  document.getElementById('hticks').innerHTML = hrs.map(function(v,i){
    return '<span>'+(i%6===0?i:'')+'</span>'; }).join('');

  /* ---- type split ---- */
  var byType = {}; R.forEach(function(r){ byType[r[T]]=(byType[r[T]]||0)+1; });
  var tks = Object.keys(byType).sort(function(a,b){ return byType[b]-byType[a]; });
  var tmx = byType[tks[0]];
  document.getElementById('types').innerHTML = tks.map(function(k){
    var v=byType[k];
    return '<div class="trow t-'+k+'"><span>'+esc(bg(k))+'</span>'+
      '<span class="bar"><i style="width:'+(v/tmx*100)+'%"></i></span>'+
      '<span class="num">'+v+'</span></div>'; }).join('');

  /* ---- reporters ---- */
  var rmap = {};
  R.forEach(function(r){
    var o = rmap[r[WHO]] || (rmap[r[WHO]] = {n:0, notes:0, first:r[DATE], last:r[DATE], t:{}});
    o.n++; if(r[NOTE]) o.notes++;
    if(r[DATE] < o.first) o.first = r[DATE];
    if(r[DATE] > o.last) o.last = r[DATE];
    o.t[r[T]] = (o.t[r[T]]||0)+1;
  });
  var rnames = Object.keys(rmap).sort(function(a,b){ return rmap[b].n - rmap[a].n; });
  document.getElementById('repcount').textContent = rnames.length + ' души са подали поне един сигнал';
  document.querySelector('#reps tbody').innerHTML = rnames.map(function(name){
    var o = rmap[name];
    var top = Object.keys(o.t).sort(function(a,b){ return o.t[b]-o.t[a]; })[0];
    return '<tr><td>'+esc(name)+'</td><td class="num">'+o.n+'</td><td class="num">'+
      (o.notes||'—')+'</td><td class="num">'+bgDate(o.first)+'</td><td class="num">'+
      bgDate(o.last)+'</td><td><span class="pill p-'+top+'">'+esc(bg(top))+'</span></td></tr>';
  }).join('');

  /* ---- the log ---- */
  var fr=document.getElementById('fr'), ft=document.getElementById('ft'),
      fn=document.getElementById('fn'), q=document.getElementById('q'),
      tb=document.querySelector('#log tbody'), cnt=document.getElementById('cnt');
  rnames.forEach(function(n){ var o=document.createElement('option');
    o.value=n; o.textContent=n+' ('+rmap[n].n+')'; fr.appendChild(o); });
  tks.forEach(function(k){ var o=document.createElement('option');
    o.value=k; o.textContent=bg(k)+' ('+byType[k]+')'; ft.appendChild(o); });

  function row(r){
    var ref = r[REF] ? '<a href="https://petar1984.github.io/Fire_Varna/?h='+
      encodeURIComponent(r[REF])+'" target="_blank" rel="noopener" class="num">'+
      esc(r[REF])+'</a>' : '<span class="num" style="color:var(--faint)">нов</span>';
    var extra = [r[TYP], r[OP]==='works'?'работи':(r[OP]==='not_working'?'не работи':'')]
      .filter(Boolean).join(' · ');
    return '<tr><td class="num"><a href="https://github.com/Petar1984/Fire_Varna/issues/'+
      r[N]+'" target="_blank" rel="noopener">'+r[N]+'</a></td>'+
      '<td class="num">'+bgDate(r[DATE])+'</td>'+
      '<td class="num">'+String(r[HOUR]).padStart(2,'0')+':00</td>'+
      '<td>'+esc(r[WHO])+'</td>'+
      '<td><span class="pill p-'+r[T]+'">'+esc(bg(r[T]))+'</span>'+
      (extra?'<div class="lab" style="margin-top:3px">'+esc(extra)+'</div>':'')+'</td>'+
      '<td>'+ref+'</td>'+
      '<td class="note">'+(r[NOTE]?esc(r[NOTE]):'')+'</td></tr>';
  }
  function draw(){
    var s=q.value.trim().toLowerCase(), a=fr.value, b=ft.value, c=fn.value;
    var out = R.filter(function(r){
      if(a && r[WHO]!==a) return false;
      if(b && r[T]!==b) return false;
      if(c && !r[NOTE]) return false;
      if(s){ return (r[NOTE]+' '+r[WHO]+' '+r[REF]+' '+r[N]).toLowerCase().indexOf(s)>=0; }
      return true;
    }).sort(function(x,y){ return y[N]-x[N]; });
    cnt.textContent = out.length===R.length ? out.length+' доклада'
      : out.length+' от '+R.length+' доклада';
    tb.innerHTML = out.length ? out.map(row).join('')
      : '<tr><td colspan="7" style="padding:22px;color:var(--muted)">Нищо не отговаря на филтъра.</td></tr>';
  }
  [q,fr,ft,fn].forEach(function(el){ el.addEventListener('input', draw); });
  document.getElementById('clear').addEventListener('click', function(){
    q.value=''; fr.value=''; ft.value=''; fn.value=''; draw(); });
  draw();

  document.getElementById('foot').innerHTML =
    'Снимка на '+R.length+' доклада от GitHub, '+D.generated+'. Номерът води към самия сигнал, '+
    'ID-то на хидранта — към точката на живата карта. Часът е местният, който докладчикът е '+
    'подал на място.';
})();
</script>
"""



def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True, help="path to write the HTML page to")
    args = ap.parse_args()

    global rows, compact, days, first, last, by_rep, by_type, notes, data
    rows = normalise(fetch_issues())

    compact = []
    for r in rows:
        p = local(r["ts"]) or local(r["created"])
        if not p:
            continue
        y, mo, d, h, mi = p
        compact.append([r["n"], r["t"] or "", r["who"], "%04d-%02d-%02d" % (y, mo, d), h,
                        r["note"] or "", r["type"] or "", r["op"] or "", r["ref"] or ""])
    if not compact:
        raise SystemExit("no parseable reports")

    days = sorted({c[3] for c in compact})
    data = {"rows": compact, "labels": {k or "": v for k, v in TYPE_BG.items()},
            "generated": datetime.datetime.now().strftime("%d.%m.%Y, %H:%M"),
            "span": [days[0], days[-1]]}

    io.open(args.out, "w", encoding="utf-8").write(
        HTML.replace("__DATA__", json.dumps(data, ensure_ascii=False, separators=(",", ":"))))

    reps = collections.Counter(c[2] for c in compact)
    types = collections.Counter(c[1] for c in compact)
    print("reports %d | reporters %d | with notes %d | %s .. %s"
          % (len(compact), len(reps), sum(1 for c in compact if c[5]), days[0], days[-1]))
    print("by type: %s" % dict(types.most_common()))
    print("wrote %s" % args.out)


if __name__ == "__main__":
    main()
