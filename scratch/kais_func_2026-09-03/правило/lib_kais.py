# -*- coding: utf-8 -*-
"""Shared loaders for the KAIS-function audit (read-only).

Everything here is deterministic: same inputs -> same numbers.
Projection: local equirectangular around LAT0/LON0, metres.  The same
approximation that build_poi_names.py / export_fire_varna_places.py use
(111320 m per degree, cos(lat) on x) so distances are comparable to the
thresholds already in the pipeline (NEAR_M = 60 m).
"""
from __future__ import annotations
import json, math, sys, os

G = 'C:/git/'
LAT0, LON0 = 43.22, 27.92
MPD = 111320.0
KX = MPD * math.cos(math.radians(LAT0))


def to_m(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * MPD)


def load_info():
    d = json.load(open(G + 'varna_3d/web/varna_buildings_info.json', encoding='utf-8'))
    cols = {c: i for i, c in enumerate(d['columns'])}
    return d, cols


def field(d, cols, row, name):
    """Decoded value of a column for one row (None when empty)."""
    v = row[cols[name]]
    if name in d['dict']:
        if not isinstance(v, int) or v < 0 or v >= len(d['dict'][name]):
            return None
        return d['dict'][name][v]
    return v


def load_geoms():
    """Returns (polys_m, bboxes) indexed by building index i."""
    from shapely.geometry import Polygon
    gj = json.load(open(G + 'varna_3d/web/varna_buildings_3d.geojson', encoding='utf-8'))
    n = len(gj['features'])
    polys = [None] * n
    for feat in gj['features']:
        i = feat['properties']['i']
        rings = feat['geometry']['coordinates']
        shell = [to_m(x, y) for x, y in rings[0]]
        holes = [[to_m(x, y) for x, y in r] for r in rings[1:]]
        polys[i] = Polygon(shell, holes)
    return polys


def load_delivered():
    """The 361 delivered records, one shape: id/name/kind/lat/lon/zone/src/file."""
    out = []
    p = json.load(open(G + 'Fire_Varna/data/places.json', encoding='utf-8'))
    for k, r in enumerate(p['places']):
        out.append(dict(rid='P%03d' % k, file='places.json', name=r['name'],
                        kind=r['kind'], lat=r['lat'], lon=r['lon'],
                        zone=r.get('zone', ''), src=r.get('src', ''),
                        status=r.get('status', ''), old_names=r.get('old_names') or []))
    h = json.load(open(G + 'Fire_Varna/data/hotels.json', encoding='utf-8'))
    for k, r in enumerate(h['hotels']):
        out.append(dict(rid='H%03d' % k, file='hotels.json', name=r['name'],
                        kind=r['kind'], lat=r['lat'], lon=r['lon'],
                        zone=r.get('zone', ''), src=r.get('src', ''),
                        status=r.get('status', ''), old_names=r.get('old_names') or [],
                        beds=r.get('beds'), cat=r.get('cat')))
    return out
