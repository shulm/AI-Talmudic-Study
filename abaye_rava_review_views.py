import json
from pathlib import Path
p=Path('abaye_rava_results')
a=json.loads((p/'candidates.json').read_text(encoding='utf-8'))
for i,r in enumerate(a,1):
 r['review_id']=i
 if len(r['anchors'])==2:
  pos=r['anchors'][1]['offset']-r['start']
  r['review']=r['evidence'][:min(pos,100)].replace('\n',' ')+' // '+r['evidence'][pos:pos+140].replace('\n',' ')
 else:r['review']=r['evidence'][:240].replace('\n',' ')
(p/'review_candidates.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
d=[r for r in a if r['kind']=='direct_pair']
for r in d[:70]:print(r['review_id'],r['ref'],r['review'])
