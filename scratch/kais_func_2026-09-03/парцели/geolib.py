# -*- coding: utf-8 -*-
"""Deterministic planar geometry helpers (local equirectangular metres, Varna)."""
import math

LAT0 = 43.21
LON0 = 27.90
MY = 110574.0
MX = 111320.0 * math.cos(math.radians(LAT0))   # 81185.6 m per degree of longitude


def to_xy(lon, lat):
    return ((lon - LON0) * MX, (lat - LAT0) * MY)


def dist_pt(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def seg_pt_dist(a, b, p):
    ax, ay = a; bx, by = b; px, py = p
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    if L2 == 0.0:
        return math.hypot(px - ax, py - ay)
    t = ((px - ax) * dx + (py - ay) * dy) / L2
    if t < 0.0: t = 0.0
    elif t > 1.0: t = 1.0
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))


def _orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def seg_seg_intersect(a, b, c, d):
    o1 = _orient(a, b, c); o2 = _orient(a, b, d)
    o3 = _orient(c, d, a); o4 = _orient(c, d, b)
    return (o1 > 0) != (o2 > 0) and (o3 > 0) != (o4 > 0)


def seg_seg_dist(a, b, c, d):
    if seg_seg_intersect(a, b, c, d):
        return 0.0
    return min(seg_pt_dist(a, b, c), seg_pt_dist(a, b, d),
               seg_pt_dist(c, d, a), seg_pt_dist(c, d, b))


def pt_in_ring(p, ring):
    """Ray casting; ring is a closed list of (x, y)."""
    x, y = p
    inside = False
    n = len(ring)
    j = n - 1
    for i in range(n):
        xi, yi = ring[i]; xj, yj = ring[j]
        if (yi > y) != (yj > y):
            xint = (xj - xi) * (y - yi) / (yj - yi) + xi
            if x < xint:
                inside = not inside
        j = i
    return inside


def pt_ring_dist(p, ring):
    """0 if inside, else min distance to the boundary."""
    if pt_in_ring(p, ring):
        return 0.0
    best = float('inf')
    for i in range(len(ring) - 1):
        d = seg_pt_dist(ring[i], ring[i + 1], p)
        if d < best: best = d
    return best


def bbox(ring):
    xs = [p[0] for p in ring]; ys = [p[1] for p in ring]
    return (min(xs), min(ys), max(xs), max(ys))


def bbox_gap(b1, b2):
    dx = max(0.0, max(b1[0] - b2[2], b2[0] - b1[2]))
    dy = max(0.0, max(b1[1] - b2[3], b2[1] - b1[3]))
    return math.hypot(dx, dy)


def ring_ring_dist(r1, r2, b1=None, b2=None, cutoff=None):
    """Minimum distance between two closed rings, 0 when they touch/overlap."""
    if b1 is None: b1 = bbox(r1)
    if b2 is None: b2 = bbox(r2)
    g = bbox_gap(b1, b2)
    if cutoff is not None and g > cutoff:
        return g
    if pt_in_ring(r1[0], r2) or pt_in_ring(r2[0], r1):
        return 0.0
    best = float('inf')
    for i in range(len(r1) - 1):
        a, b = r1[i], r1[i + 1]
        for j in range(len(r2) - 1):
            d = seg_seg_dist(a, b, r2[j], r2[j + 1])
            if d < best:
                best = d
                if best == 0.0:
                    return 0.0
    return best


class UF:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, a):
        p = self.p
        while p[a] != a:
            p[a] = p[p[a]]; a = p[a]
        return a
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb: self.p[rb] = ra
