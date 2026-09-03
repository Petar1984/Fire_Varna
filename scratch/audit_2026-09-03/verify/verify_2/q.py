import sys, io, json
sys.path.insert(0, r'C:/git/Fire_Varna/scratch/places_search')
import recall_sweep as R
Q=['кардиолайф','диализен център','диализа','хоспис надежда','хоспис','еврохоспитал',
   'дкц еквита','дкц младост','лисичкова','доц георгиев','света клементина','мануш войвода',
   'хоспис света магдалена','дкц св марина','иван рилски']
for q in Q:
    res=R.search(q)
    rows=res.get('rows') if isinstance(res,dict) else res
    br=res.get('branch') if isinstance(res,dict) else '?'
    names=[ (r.get('name') if isinstance(r,dict) else str(r)) for r in (rows or [])][:3]
    print('%-24s n=%-4d branch=%-18s %s' % (q, len(rows or []), br, ' | '.join(n[:44] for n in names)))
