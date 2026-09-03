import sys
sys.path.insert(0, r'C:/git/Fire_Varna/scratch/places_search')
import recall_sweep as R
Q=['кардиолайф','диализен център','диализа','диализен','хоспис надежда','еврохоспитал',
   'дкц еквита','дкц младост-м','лисичкова','доц георгиев','света клементина',
   'хоспис света магдалена','дкц св марина','дкц свети иван рилски','виртус медикал',
   'проф ненов','хипократ','болница младост','мк младост']
for q in Q:
    rows,branch=R.search(q)
    nm=[getattr(r,'name',str(r)) for r in rows][:3]
    zn=[getattr(r,'zone','') for r in rows][:3]
    print('%-24s n=%-3d %-14s %s' % (q,len(rows),branch,' || '.join('%s [%s]'%(a[:46],b) for a,b in zip(nm,zn))))
