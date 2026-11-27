import json,sys
from pathlib import Path
def read(p):return json.loads(Path(p).read_text(encoding='utf8'))
D=Path(__file__).parent;P=D.parent.parent/'bavli_taanit';rd=read(D.parent/'taanit_delegated055.json');s=read(P/'snapshots/ac7c9ec619b963f05c6dc32c42e16511808f6256dea63937f5b5f8e5e96e5cf4.json');inv=read(P/'source_inventory.json');bi={r['id']:r for r in inv};br={r['ref']:r for r in inv}
assert read(D/'preflight062.json')['result']=='PASS'
start=int(sys.argv[1]);end=int(sys.argv[2]);layers=sys.argv[3:]
for ref in rd['core_refs'][start:end]:
 print('\nSOURCE',ref,br[ref]['text'])
 for label,rows in [('READER',rd['records']),('PRODUCER',s['records'])]:
  for r in rows:
   if label=='PRODUCER' and r['release_state']!='valid':continue
   refs=[e['segment_id'] if label=='READER' else bi[e['segment_id']]['ref'] for e in r['evidence']]
   if ref in refs and r['layer'] in layers:print(label,r['id'],r['layer'],json.dumps(r['content'],ensure_ascii=False),json.dumps(r.get('uncertainty',[]),ensure_ascii=False))
if start==-1:
 for ref in rd['context_read_refs']:print(ref,br[ref]['text'])
