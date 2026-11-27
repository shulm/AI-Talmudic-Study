import json,sys
from pathlib import Path
D=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04');r=json.loads((D/'review_20261127_delegated047/moed_katan_delegated047.json').read_text('utf8'));s=json.loads((D/'bavli_moed_katan/snapshots/e5f88150985e9541e2f1a5def9b2975ab102767f3a5b5b2fe05770b5d3ae12e0.json').read_text('utf8'));inv={x['id']:x['ref'] for x in json.loads((D/'bavli_moed_katan/source_inventory.json').read_text('utf8'))}
for ref in r['core_refs'][int(sys.argv[1]):int(sys.argv[2])]:
 print('\nREF',ref)
 for name,rows in [('R',r['proposal']['records']),('P',s['records'])]:
  for x in rows:
   if x['layer'] in sys.argv[3:] and any(inv.get(e['segment_id'],e['segment_id'])==ref for e in x['evidence']):print(name,x['id'],x['layer'],json.dumps(x['content'],ensure_ascii=False),('UNC '+str(x['uncertainty'])) if x['uncertainty'] else '')
