"""Verify frozen source-first evidence, not semantic correctness or blindness."""
import json,hashlib,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def verify(path):
 raw=path.read_bytes();v=json.loads(raw)
 source_hash=v['source_sha256']
 jobs=[json.loads(p.read_bytes()) for p in (BASE/'jobs').glob('*.json')]
 j=next(j for j in jobs if j['source']['sha256']==source_hash)
 source=json.loads(Path(j['source']['path']).read_bytes())
 assert sha(Path(j['source']['path']).read_bytes())==source_hash
 byref={f"{source['title']} {i//2+1}{'a' if i%2==0 else 'b'}:{k+1}":t for i,page in enumerate(source['text']) for k,t in enumerate(page)}
 assert v['frozen_before_comparison'] is True and v['producer_labels_exposed'] is False
 assert v['execution']['agent_id'] and v['execution']['route']=='interactive_agent'
 core=set(v['core_refs']);assert core and core<=set(byref)
 assert len(core)==len(v['core_refs'])
 findings=v.get('findings') or v.get('records') or v.get('claims',[])+v.get('questions',[])+v.get('directed_relations',[])
 assert findings
 count=0
 def walk(obj):
  nonlocal count
  if isinstance(obj,dict):
   if all(k in obj for k in ['ref','start_char','end_char','quote']):
    t=byref[obj['ref']];a=obj['start_char'];z=obj['end_char']
    assert type(a)==int and type(z)==int and 0<=a<z<=len(t)
    assert t[a:z]==obj['quote'],str((path,obj))
    count+=1
   for val in obj.values():walk(val)
  elif isinstance(obj,list):
   for val in obj:walk(val)
 walk(v)
 plan=json.loads(Path(j['frozen_plan']['path']).read_bytes())
 probability={s['ref'] for b in plan['review_blocks'] if 'probability_sample' in b['roles'] for s in b['spans']}
 endpoints={s['ref'] for b in plan['review_blocks'] if any('check' in role for role in b['roles']) for s in b['spans']}
 return {'path':str(path),'sha256':sha(raw),'source_sha256':source_hash,'core_segments':len(core),'probability_core_segments':len(core&probability),'endpoint_core_segments':len(core&endpoints),'unique_selected_core_segments':len(core&(probability|endpoints)),'evidence_spans':count,'semantic_correctness_certified':False,'human_certification':False}
if __name__=='__main__':
 paths=[Path(p) for p in sys.argv[1:]]
 print(json.dumps([verify(p) for p in paths],ensure_ascii=False,indent=2))
