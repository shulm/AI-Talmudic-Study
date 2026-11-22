import json,re
from pathlib import Path
p=Path('rav_shmuel_results')
a=json.loads((p/'candidates.json').read_text(encoding='utf-8'))
b=json.loads((p/'selected.json').read_text(encoding='utf-8'))
for r in a:
 if 'joint' not in r['why']:continue
 if any(s['work']==r['work'] and r['hit_start']<=s['start']<=r['hit_end']+50 for s in b):continue
 if 'דאמרי תרוייהו' in r['snippet'][:80] or 'תרויהון' in r['snippet'][:80]:continue
 print(r['id'],r['ref'],r['snippet'][:210].replace('\n',' '))
