# Independent check against the SIGNED reference implementation (no main(), no writes).
import sys, json, hashlib, pathlib
REF = pathlib.Path('C:/git/Fire_Varna/scratch/places_search')
sys.path.insert(0, str(REF))
rows_file = REF / 'recall_sweep_rows.json'
before = hashlib.sha256(rows_file.read_bytes()).hexdigest()
import recall_sweep as R
for q in ['ГРАДИНА', 'градина', 'хотел градина', 'градин', 'детска градина']:
    rows, cat, has_key = (R.search(q) + (None, None, None))[:3] if isinstance(R.search(q), tuple) else (R.search(q), None, None)
    names = [r.name for r in rows] if rows and hasattr(rows[0], 'name') else [str(x) for x in (rows or [])]
    has = 'ГРАДИНА' in [n for n, r in zip(names, rows)] if rows else False
    idx = next((i + 1 for i, r in enumerate(rows) if getattr(r, 'name', '') == 'ГРАДИНА'
                and getattr(r, 'kind', '') == 'Хотел'), None)
    print(q, '| n=', len(rows), '| cat=', cat, '| hasKey=', has_key, '| ГРАДИНА rank=', idx,
          '| first3=', names[:3])
after = hashlib.sha256(rows_file.read_bytes()).hexdigest()
print('recall_sweep_rows.json sha before == after :', before == after, before[:16])
