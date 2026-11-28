"""Add atomic child records and direct support edges; keep composite parents and history."""
import copy,json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_yoma')
old='77ea378ff99bf75a36d849e39a9e88ac404114541f33c54a6aa3e516df77f0bf'
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/yoma','epoch':2}
S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());M=json.loads((J/'JOB.json').read_bytes());D={r['id']:r for r in S['records']};R=[];lineage={}
def add(k,l,e,c,links):
 i='yom.s2702.fix.'+k;R.append(dict(id=i,layer=l,evidence=copy.deepcopy(e),content=c,origin='source_paraphrase',uncertainty=[],links=links));return i
for k,parent,prop,cond,holder in [
 ('investiture','invest','Ravina proposes seven-day investiture in vestments as a practical difference: indispensable under the all-written-details view, dispensable under the later-generations criterion.',['Seven-day investiture in inauguration rites'],'רבינא'),
 ('anointing','invest','Ravina proposes seven-day anointing as a practical difference: indispensable under the all-written-details view, dispensable under the later-generations criterion.',['Seven-day anointing in inauguration rites'],'רבינא'),
 ('mixed7and1','mixed','The baraita includes a successor priest invested in vestments for seven days and anointed for one day, through אשר ימשח אותו ואשר ימלא את ידו.',['Successor priest','Seven days investiture','One day anointing'],'Anonymous quoted baraita'),
 ('mixed1and7','mixed','The baraita includes a successor priest invested in vestments for one day and anointed for seven days, through אשר ימשח אותו ואשר ימלא את ידו.',['Successor priest','One day investiture','Seven days anointing'],'Anonymous quoted baraita')]:
  pid='yom.s2701.'+parent;e=D[pid]['evidence']
  cid=add(k,'claims',e,dict(proposition=prop,conditions=cond,scope='Atomic child of '+pid+'; composite parent retained for historical/composite views. Do not double-count child and parent as independent claims.',assertion_mode='asserted'),[pid])
  add(k+'.p','positions',e,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=cond,local_status='Atomic articulation of existing composite finding; no new eligibility or certification.'),[cid,pid])
  lineage[cid]=dict(parent_record_id=pid,relationship='atomic_child_of_retained_composite',supersedes=False)
for k,source,target in [('semikha','semikhastatus','semikha'),('waving','wavestatus','waving'),('separation','prepare','separation')]:
 src='yom.s2701.'+source;dst='yom.s2701.'+target
 add('support.'+k,'edges',D[src]['evidence'],dict(source_id=src,target_id=dst,relation='support',explicitness='source_explicit'),[src,dst])
coverage=[]
for oldc in S['coverage']:
  applicable=[r['id'] for r in R if (oldc['layer']=='reconciliation' or oldc['layer']==r['layer']) and any(e['segment_id']==oldc['segment_id'] for e in r['evidence'])]
  if not applicable:continue
  c={k:copy.deepcopy(v) for k,v in oldc.items() if k!='proposal_execution'}
  c['record_ids']+=applicable;c['extraction_result']='records_found'
  c['rationale']+=' Prior-review bounded qualification repair: explicit atomic children for two duration requirements and two mixed-duration cases, plus direct source-proof support edges for semikha/waving/separation. All earlier composite records retained with explicit parent links; zero new completed segments.'
  coverage.append(c)
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=coverage,open_tails=S['open_tails'])
def write(path,obj):
 b=(json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
 if path.exists():assert path.read_bytes()==b
 else:path.write_bytes(b)
 return hashlib.sha256(b).hexdigest()
sha=write(H/'yoma_atomic_graph_correction.json',P)
write(H/'YOMA_ATOMIC_LINEAGE.json',dict(prior_snapshot_sha256=old,proposal_sha256=sha,lineage=lineage,composite_parents_retained=True,new_completed_segments=0,qualification_changes=False))
print(json.dumps(dict(proposal_sha256=sha,records=len(R))))
