# -*- coding: utf-8 -*-
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
d=json.load(open("C:/git/Varna_buildings/output/block_identity_sidecar.json",encoding='utf-8'))
bg=d["block_groups"]
CAD=["10135.xxxx","10135.xxxx","10135.xxxx","10135.xxxx","10135.xxxx","10135.xxxx","10135.xxxx","10135.xxxx"]
for c in CAD:
    v=bg.get(c)
    if v is None:
        hit=[k for k,x in bg.items() if c in (x.get("members") or [])]
        v=bg.get(hit[0]) if hit else None
    if v: print(c, "block_id=",v.get("block_id"),"btk=",v.get("btk"),"raion=",v.get("raion"),"parcel=",v.get("parcel"),"pin=",v.get("pin"),"ap=",v.get("ap"),"fl=",v.get("fl"))
    else: print(c,"-- not in block_groups")
print()
print("counts:",json.dumps(d.get("counts"),ensure_ascii=False)[:600])
