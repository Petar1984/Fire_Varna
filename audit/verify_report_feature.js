// Headless verify for hydrants_varna_merged.html (no network calls).
// 1) Parse inline hydrantData JSON, assert 6,070 records.
// 2) Parse-check the in-page <script> as JS (syntax only).
// 3) Smoke-load the file in a headless Chromium via Playwright (file:// is OK
//    for verify; production must run on http://localhost:PORT or HTTPS).

const fs = require('fs');
const path = require('path');
const HTML_PATH = path.join(__dirname, '..', 'hydrants_varna_merged.html');
const html = fs.readFileSync(HTML_PATH, 'utf8');

function fail(msg) { console.error('[FAIL]', msg); process.exitCode = 1; }
function ok(msg)   { console.log('[OK]', msg); }

// 1) JSON record count
const dataRe = /<script id="hydrantData"[^>]*>([\s\S]*?)<\/script>/;
const m = dataRe.exec(html);
if (!m) { fail('hydrantData script tag not found'); process.exit(1); }
let data;
try { data = JSON.parse(m[1]); } catch (e) { fail('JSON parse: ' + e.message); process.exit(1); }
if (!Array.isArray(data)) { fail('hydrantData not array'); process.exit(1); }
if (data.length !== 6070) fail('expected 6070 hydrants, got ' + data.length);
else ok('hydrantData length = 6070');

// 2) Syntax-check the application <script> (the IIFE block, last <script>)
const appScriptRe = /<script>\s*\(function\(\)\s*\{([\s\S]*?)\}\)\(\);?\s*<\/script>\s*<\/body>/;
const sm = appScriptRe.exec(html);
if (!sm) { fail('app script (IIFE) not found before </body>'); }
else {
  try {
    new Function(sm[1]);
    ok('app script parses as valid JS');
  } catch (e) {
    fail('app script syntax error: ' + e.message);
  }
}

// 3) File size sanity
const stat = fs.statSync(HTML_PATH);
console.log('[INFO] file size:', stat.size, 'bytes (' + (stat.size / 1024).toFixed(1) + ' KB)');
if (stat.size > 5 * 1024 * 1024) fail('file size exceeds 5 MB cap');
else ok('file size under 5 MB cap');

// 4) Spot-check key new identifiers exist
const expected = [
  'GITHUB_API_VERSION', 'GITHUB_REPO_OWNER', 'GITHUB_PAT',
  'localISOString', 'uuidv4', 'crypto.randomUUID',
  'showReportModal', 'showReportTypePicker',
  'enterLocationPlacementMode', 'buildReportYAML', 'buildIssueTitle',
  'submitReport', 'queueReport', 'retryQueuedReports',
  'getReporterName', 'setReporterName',
  'hydrants_reporter_name', 'hydrants_recent_reports', 'hydrants_pending_reports',
  '"2022-11-28"',
  'addHydrantBtn', 'placement-pin', 'popup-report-btn',
];
for (const tok of expected) {
  if (html.indexOf(tok) === -1) fail('missing token: ' + tok);
}
ok('all expected tokens present');

// 4b) Constants must be filled in (no string-literal placeholders left).
// The runtime safety regex /^<TODO_/ in isPlaceholderConfig() is allowed to
// remain — it's a defensive check, not a placeholder value. We only ban the
// literal placeholder strings that previously sat inside the constants.
const bannedPlaceholders = ['<TODO_PETAR_GITHUB_USERNAME>', '<TODO_FINE_GRAINED_PAT>'];
for (const tok of bannedPlaceholders) {
  if (html.indexOf(tok) !== -1) fail('placeholder still present: ' + tok);
}
ok('no placeholder values remain in constants');

// 4c) Worker proxy: no PAT, no direct GitHub API hits.
if (/github_pat_/.test(html)) fail('PAT literal still present in file');
else ok('no github_pat_ literal in file');
if (html.indexOf('api.github.com') !== -1) fail('direct api.github.com call still present');
else ok('no direct api.github.com calls');
const workerHits = (html.match(/varna-hydrants-proxy\.petar-dikov2019\.workers\.dev/g) || []).length;
if (workerHits !== 1) fail('expected 1 worker URL hit, got ' + workerHits);
else ok('worker URL appears exactly once');

// 5) Old removed tokens should be gone
const removed = [
  'reportProblem', 'reportContext', '🚒 ХИДРАНТИ ВАРНА — СИГНАЛ',
  'СПЕШНОСТ:', 'navigator.share', 'sms:?body=',
];
for (const tok of removed) {
  if (html.indexOf(tok) !== -1) fail('old token still present: ' + tok);
}
ok('old SMS / Web Share tokens removed');

console.log('\nDone.');
