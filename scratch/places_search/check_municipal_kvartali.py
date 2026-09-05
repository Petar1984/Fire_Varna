# -*- coding: utf-8 -*-
"""Check whether the Varna municipality ArcGIS Online layer „Квартали“ is reachable again and,
if so, download it once as GeoJSON (52 polygons, field Name_bg). Read-only against the web;
writes one file under scratch/ (untracked until the licence decision). No emails, no tokens.

    PYTHONIOENCODING=utf-8 python scratch/places_search/check_municipal_kvartali.py
"""
import json, sys, ssl, datetime, pathlib, urllib.request, urllib.parse

ITEM = "ce83fb2fc9d7416c9778d75f9a98e5dc"
SERVICE = "https://services6.arcgis.com/iUyRq1SRpOklUPak/arcgis/rest/services/%D0%9A%D0%B2%D0%B0%D1%80%D1%82%D0%B0%D0%BB%D0%B8/FeatureServer/0"
HUB_DL = f"https://hub.arcgis.com/api/v3/datasets/{ITEM}_0/downloads/geojson?spatialRefId=4326"
OUT_DIR = pathlib.Path(__file__).resolve().parent / "agkk_inspire_2026-09-05"
ctx = ssl.create_default_context()

def get(url, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Fire_Varna research)"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()

def main():
    today = datetime.date.today().isoformat()
    status, raw = get(SERVICE + "?f=pjson")
    text = raw.decode("utf-8", "replace")
    if '"error"' in text[:200]:
        print(f"{today} · service still locked: {text.strip()[:160]}")
    else:
        meta = json.loads(text)
        print(f"{today} · service answers: name={meta.get('name')} geometry={meta.get('geometryType')} fields={[f['name'] for f in meta.get('fields', [])]}")
        q = SERVICE + "/query?" + urllib.parse.urlencode({"where": "1=1", "outFields": "*", "returnGeometry": "true", "outSR": "4326", "f": "geojson"})
        status, gj = get(q, timeout=180)
        if status == 200 and gj[:1] == b"{" and b'"features"' in gj[:200]:
            OUT_DIR.mkdir(parents=True, exist_ok=True)
            out = OUT_DIR / f"varna_municipality_kvartali_{today}.geojson"
            out.write_bytes(gj)
            n = len(json.loads(gj).get("features", []))
            print(f"DOWNLOADED {n} features → {out} (untracked; licence decision pending)")
            return 0
        print(f"query failed: HTTP {status}: {gj[:200]!r}")
    status, raw = get(HUB_DL)
    print(f"hub download: HTTP {status}: {raw[:160].decode('utf-8', 'replace')}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
