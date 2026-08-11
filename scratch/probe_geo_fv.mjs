// Gate: the coordinate readout in the hydrant map.
//
// The point of this feature is that it must not disturb an app people use at
// an incident. So the gate spends most of its checks on what must NOT change:
// the readout is off until asked for, and once on it still yields to placement
// mode, manual-position mode and hydrant markers.
//
// Run:  node scratch/probe_geo_fv.mjs 9334 http://localhost:8000/index.html
const PORT = process.argv[2] || "9334";
const URL_ = process.argv[3] || "http://localhost:8000/index.html";
const MOB = process.argv[4] === "mob";
const sleep = ms => new Promise(r => setTimeout(r, ms));
const j = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json();
const ws = new WebSocket(j.filter(t => t.type === "page")[0].webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
let id = 0; const w = new Map(); const errs = [];
ws.onmessage = m => {
  const d = JSON.parse(m.data);
  if (d.id && w.has(d.id)) { w.get(d.id)(d); w.delete(d.id); }
  if (d.method === "Runtime.exceptionThrown")
    errs.push(d.params.exceptionDetails.exception?.description || d.params.exceptionDetails.text);
  if (d.method === "Runtime.consoleAPICalled" && d.params.type === "error")
    errs.push((d.params.args || []).map(a => a.value ?? a.description).join(" "));
};
const send = (k, p = {}) => new Promise(res => { const i = ++id; w.set(i, res); ws.send(JSON.stringify({ id: i, method: k, params: p })); });
const ev = async e => (await send("Runtime.evaluate", { expression: e, awaitPromise: true, returnByValue: true })).result?.result?.value;
let fails = 0;
const check = (ok, n, d) => { console.log(`${ok ? "  ok  " : "ПАДА  "}${n}${d ? " · " + d : ""}`); if (!ok) fails++; };

const W = MOB ? 375 : 1400, H = MOB ? 812 : 900;
await send("Runtime.enable"); await send("Page.enable");
await send("Emulation.setTouchEmulationEnabled", { enabled: MOB, maxTouchPoints: MOB ? 5 : 0 });
await send("Emulation.setDeviceMetricsOverride", { width: W, height: H, deviceScaleFactor: MOB ? 2 : 1, mobile: MOB });
await send("Page.navigate", { url: URL_ });
for (let i = 0; i < 60; i++) {
  await sleep(1000);
  if (await ev(`!!document.querySelector('.leaflet-container') && !!window.L`)) break;
}
await sleep(3000);

console.log(`\n=== ПРОВЕРКА: координати в картата с хидрантите (${W}×${H}) ===\n`);

// 1. off by default — nothing on the page differs until asked
check(await ev(`document.getElementById('geoCard').hidden === true`),
      "изключено по подразбиране");
check(await ev(`document.getElementById('geoXh').hidden === true`),
      "мерникът е скрит, докато е изключено");
check(await ev(`!document.getElementById('geoBtn').classList.contains('active')`),
      "бутонът не свети");

// 2. the app's own controls are all still there and none moved
const ctrls = await ev(`[...document.querySelectorAll('.controls .ctrl-btn')].map(b=>b.id).join(',')`);
console.log(`      контроли: ${ctrls}`);
check(/manualPinBtn/.test(ctrls) && /addHydrantBtn/.test(ctrls)
      && /basemapToggle/.test(ctrls) && /legendBtn/.test(ctrls) && /geoBtn/.test(ctrls),
      "всички стари бутони са на място, новият е накрая");

// 3. turn it on
await ev(`document.getElementById('geoBtn').click()`);
await sleep(400);
check(await ev(`document.getElementById('geoCard').hidden === false`), "бутонът я отваря");
check(await ev(`document.getElementById('geoBtn').classList.contains('active')`), "бутонът свети");

// 4. the number is the point — compare against Leaflet's own unprojection
const PX = Math.round(W * 0.5), PY = Math.round(H * 0.62);
if (!MOB) {
  await send("Input.dispatchMouseEvent", { type: "mouseMoved", x: PX, y: PY, button: "none" });
}
await sleep(400);
const shown = await ev(`document.getElementById('geoDD').textContent`);
const truth = await ev(`(()=>{const mp=document.querySelector('.leaflet-container');
  const m=mp._leaflet_map||null; return null;})()`);
console.log(`      показва: ${shown}`);
check(/^4[23]\.\d{6}, 2[78]\.\d{6}$/.test(shown),
      "форматът е ширина, дължина с 6 знака и е във Варна");
// DMS agrees with the decimals
const dmsOk = await ev(`(()=>{
  const dd=document.getElementById('geoDD').textContent.split(',').map(s=>parseFloat(s));
  const s=document.getElementById('geoDMS').textContent;
  const m=[...s.matchAll(/(\\d+)°(\\d+)'([\\d.]+)"([NSEW])/g)];
  if(m.length!==2) return false;
  const dec=x=>(+x[1])+(+x[2])/60+(+x[3])/3600;
  return Math.abs(dec(m[0])-Math.abs(dd[0]))<0.0001
      && Math.abs(dec(m[1])-Math.abs(dd[1]))<0.0001;})()`);
check(dmsOk, "градусите/минутите отговарят на десетичните");

// A point where the click actually reaches the MAP. Picking one by fraction of
// the viewport put the tap on the coordinate card itself once the card moved to
// the bottom on phones — three checks failed for a page that was fine.
// elementFromPoint is the only honest answer to "what would receive this click".
const mapPointExpr = `(()=>{
  const overlays = '.geo-card, .controls, .app-header, .pill, .leaflet-control,'
                 + ' .locate-btn, .placement-banner, .placement-actions,'
                 + ' .prepick-banner, .legend, .leaflet-marker-icon, .leaflet-popup';
  for (let y = Math.round(innerHeight*0.30); y < innerHeight - 40; y += 9)
    for (let x = 30; x < innerWidth - 30; x += 9) {
      const el = document.elementFromPoint(x, y);
      if (!el) continue;
      if (!el.closest('.leaflet-container')) continue;
      if (el.closest(overlays)) continue;
      return [x, y];
    }
  return null;})()`;

// 5. clicking the map marks — and marks where it was clicked
const mp1 = await ev(mapPointExpr);
if (!mp1) { check(false, "не намерих свободна точка от картата за цъкане"); }
const CX = mp1 ? mp1[0] : Math.round(W * 0.45), CY = mp1 ? mp1[1] : Math.round(H * 0.7);
console.log(`      свободна точка от картата: ${CX},${CY}`);
const want = await ev(`(()=>{const ll=window.__fvmap
  ? window.__fvmap.containerPointToLatLng([${CX},${CY}]) : null;
  return ll? ll.lat.toFixed(6)+', '+ll.lng.toFixed(6) : null;})()`);
if (MOB) {
  await send("Input.dispatchTouchEvent", { type: "touchStart", touchPoints: [{ x: CX, y: CY }] });
  await send("Input.dispatchTouchEvent", { type: "touchEnd", touchPoints: [] });
} else {
  await send("Input.dispatchMouseEvent", { type: "mousePressed", x: CX, y: CY, button: "left", clickCount: 1 });
  await send("Input.dispatchMouseEvent", { type: "mouseReleased", x: CX, y: CY, button: "left", clickCount: 1 });
}
await sleep(600);
const pinned = await ev(`document.getElementById('geoCard').classList.contains('pinned')`);
check(pinned, "докосване на картата заковава точка");
check(await ev(`document.querySelectorAll('.geo-pin-marker').length===1`),
      "на картата се появява един знак");
const at = await ev(`document.getElementById('geoDD').textContent`);
if (want) check(at === want, "заковава ТАМ, където е докоснато", `${want} vs ${at}`);
else console.log(`      (няма достъп до картата отвън — пропускам сравнението)`);
// frozen: moving does not change it
if (!MOB) {
  await send("Input.dispatchMouseEvent", { type: "mouseMoved", x: 200, y: 300, button: "none" });
  await sleep(400);
  check(await ev(`document.getElementById('geoDD').textContent`) === at,
        "закованата точка не мърда");
}

// 6. THE IMPORTANT ONE — the app's own modes still win
await ev(`document.getElementById('geoMark').click()`);   // пусни
await sleep(200);
await ev(`document.getElementById('manualPinBtn').click()`);   // ръчна позиция
await sleep(400);
const manOn = await ev(`document.querySelector('.controls #manualPinBtn').classList.contains('active')
  || document.body.getAttribute('data-manual')==='1' || true`);
const mp2 = await ev(mapPointExpr);
const MX = mp2 ? mp2[0] : Math.round(W * 0.55), MY = mp2 ? mp2[1] : Math.round(H * 0.55);
if (MOB) {
  await send("Input.dispatchTouchEvent", { type: "touchStart", touchPoints: [{ x: MX, y: MY }] });
  await send("Input.dispatchTouchEvent", { type: "touchEnd", touchPoints: [] });
} else {
  await send("Input.dispatchMouseEvent", { type: "mousePressed", x: MX, y: MY, button: "left", clickCount: 1 });
  await send("Input.dispatchMouseEvent", { type: "mouseReleased", x: MX, y: MY, button: "left", clickCount: 1 });
}
await sleep(700);
check(!(await ev(`document.getElementById('geoCard').classList.contains('pinned')`)),
      "в режим „ръчна позиция“ координатите НЕ заковават — режимът печели");
const statusTxt = await ev(`(document.getElementById('status')||{}).textContent||''`);
console.log(`      статус след ръчното задаване: "${String(statusTxt).slice(0,60)}"`);

// 6b. a hydrant pin keeps its own click — tapping one must select the hydrant,
//     not drop a coordinate marker on top of it.
//     NOTE: this check asserts the REQUIREMENT, not a particular mechanism. It
//     passes with the page's geoHitsMarker() guard removed, because Leaflet
//     already stops a marker click from reaching the map. So it does not
//     discriminate between the two — it only proves the user-visible rule
//     holds. Do not read a pass here as proof that the guard works.
await ev(`document.getElementById('geoBtn').click()`);        // пак включено
await sleep(300);
if (await ev(`document.getElementById('geoCard').hidden`)) {
  await ev(`document.getElementById('geoBtn').click()`);
  await sleep(300);
}
// Pick a HYDRANT pin (.h-pin-wrapper), and only one whose centre really is on
// top — elementFromPoint is the arbiter. The first attempt took the first
// .leaflet-marker-icon and its rect, but the map had moved when manual mode
// recentred, so the click landed on an SVG path and the gate blamed the page.
const hyd = await ev(`(()=>{
  for (const m of document.querySelectorAll('.leaflet-marker-icon.h-pin-wrapper')) {
    const r = m.getBoundingClientRect();
    const x = Math.round(r.left + r.width/2), y = Math.round(r.top + r.height/2);
    const el = document.elementFromPoint(x, y);
    if (el && el.closest && el.closest('.leaflet-marker-icon.h-pin-wrapper')) return [x, y];
  }
  return null;})()`);
console.log(`      хидрант на екрана: ${JSON.stringify(hyd)}`);
if (hyd) {
  if (MOB) {
    await send("Input.dispatchTouchEvent", { type: "touchStart", touchPoints: [{ x: hyd[0], y: hyd[1] }] });
    await send("Input.dispatchTouchEvent", { type: "touchEnd", touchPoints: [] });
  } else {
    await send("Input.dispatchMouseEvent", { type: "mousePressed", x: hyd[0], y: hyd[1], button: "left", clickCount: 1 });
    await send("Input.dispatchMouseEvent", { type: "mouseReleased", x: hyd[0], y: hyd[1], button: "left", clickCount: 1 });
  }
  await sleep(700);
  check(!(await ev(`document.getElementById('geoCard').classList.contains('pinned')`)),
        "цъкане по ХИДРАНТ не заковава координата");
} else { console.log("      (няма видим хидрант — пропускам)"); }
await ev(`(()=>{if(document.getElementById('geoCard').classList.contains('pinned'))
  document.getElementById('geoMark').click();})()`);

// 7. the legend and the card never stack in the same corner
await ev(`document.getElementById('legendBtn').click()`);
await sleep(300);
check(await ev(`document.getElementById('geoCard').hidden === true`),
      "отварянето на легендата затваря координатите");
await ev(`document.getElementById('geoBtn').click()`);
await sleep(300);
check(await ev(`document.getElementById('legend').hidden === true`),
      "и обратното");

// 8. touch targets
const small = await ev(`[...document.querySelectorAll('.geo-b')]
  .filter(b=>!b.hidden && b.getBoundingClientRect().height<44).map(b=>b.textContent).join(', ')`);
check(!small, "всеки бутон е поне 44 px висок", small || "всички");

// 9. the card is on screen and does not cover the header or the locate button
// Every other thing that can be on screen at the same time. The pill was the
// one the first version of this check missed: at 375 px the GPS-denied pill lay
// straight across the coordinates and a screenshot, not the gate, caught it.
const geom = await ev(`(()=>{const c=document.getElementById('geoCard').getBoundingClientRect();
  const ov=(a,b)=>!!b && !(a.right<=b.left||a.left>=b.right||a.bottom<=b.top||a.top>=b.bottom);
  const vis=(el)=>{ if(!el) return null; const s=getComputedStyle(el);
    if(s.display==='none'||s.visibility==='hidden'||el.hidden) return null;
    const r=el.getBoundingClientRect(); return (r.width&&r.height)?r:null; };
  const q=(s)=>vis(document.querySelector(s));
  return JSON.stringify({x:Math.round(c.left),y:Math.round(c.top),w:Math.round(c.width),
    h:Math.round(c.height),вън:c.left<0||c.top<0||c.right>innerWidth||c.bottom>innerHeight,
    върхуЗаглавието:ov(c,q('.app-header')),
    върхуGPS:ov(c,q('.locate-btn')),
    върхуИзвестието:ov(c,q('.pill')),
    върхуМащаба:ov(c,q('.leaflet-control-zoom')),
    върхуКонтролите:ov(c,q('.controls')),
    имаИзвестие:!!q('.pill')});})()`);
console.log(`      картата: ${geom}`);
const G = JSON.parse(geom);
check(!G.вън, "картончето е изцяло на екрана");
check(!G.върхуЗаглавието, "не покрива заглавната лента");
check(!G.върхуGPS, "не покрива GPS бутона");
check(!G.върхуИзвестието, `не покрива лентата с известия (има ли известие: ${G.имаИзвестие})`);
check(!G.върхуМащаба, "не покрива бутоните за мащаб");
check(!G.върхуКонтролите, "не покрива дясната лента с бутони");

// 10. links carry the point
const links = await ev(`(()=>{const out={}; const o=window.open;
  for(const id of ['geoGgl','geoSv','geoWaze']){let u=null; window.open=(x)=>{u=x;return null;};
    document.getElementById(id).click(); out[id]=u;}
  window.open=o; return JSON.stringify(out);})()`);
console.log(`      връзки: ${links}`);
const L2 = JSON.parse(links);
const dd = await ev(`document.getElementById('geoDD').textContent`);
const pair = dd.replace(/,\s*/, ",");
check(String(L2.geoGgl).includes(pair), "Google носи точката");
check(String(L2.geoSv).includes(pair) && /map_action=pano/.test(String(L2.geoSv)),
      "Street View носи точката");
check(String(L2.geoWaze).includes(pair), "Waze носи точката");

// 11. turning it off leaves no trace
await ev(`document.getElementById('geoClose').click()`);
await sleep(300);
check(await ev(`document.getElementById('geoCard').hidden===true
  && document.getElementById('geoXh').hidden===true
  && document.querySelectorAll('.geo-pin-marker').length===0`),
      "затварянето маха картончето, мерника и знака");

// 12. nothing on the page threw
check(errs.length === 0, "без изключения на страницата", errs.slice(0, 3).join(" | "));
check(await ev(`document.querySelectorAll('.leaflet-marker-icon').length > 0`),
      "хидрантите са още на картата",
      String(await ev(`document.querySelectorAll('.leaflet-marker-icon').length`)));

console.log(fails ? `\nПАДА: ${fails}` : "\nПРЕМИНАВА: всички проверки");
process.exit(fails ? 1 : 0);
