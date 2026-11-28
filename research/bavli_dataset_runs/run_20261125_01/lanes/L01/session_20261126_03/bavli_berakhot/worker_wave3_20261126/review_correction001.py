from pathlib import Path
import sys,copy
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1')
import runner as r
HERE=Path(__file__).resolve().parent;JOB=HERE.parent;j,ss=r.load(JOB);s=r.current(JOB)
assert r.sha(r.encoded(s))=='cab98d439137c44996726e24faa6aaa565721a96eb970763f59530e458e945f1'
by={x['ref']:x for x in ss.values()};pre='bk.sufferings.20261126w3.'
ev=[]
for ref in ['Berakhot 5a:14','Berakhot 5a:15']:
 x=by[ref];ev.append(dict(segment_id=x['id'],start_char=0,end_char=len(x['text']),quote=x['text']))
e=dict(id=pre+'e14_15_contrast',layer='edges',evidence=ev,content=dict(source_id=pre+'c14',target_id=pre+'c15',relation='distinction',explicitness='source_explicit'),origin='source_paraphrase',links=[pre+'c14',pre+'c15'],uncertainty=['Schema distinction represents explicitly stated disagreement between criteria; arrow order follows textual first/second, not an inferred historical objection direction. Neither criterion is assigned to a named member of the pair.'])
cov=[]
for old in s['coverage']:
 if old['segment_id'] in {x['segment_id'] for x in ev} and old['layer']=='edges':
  x={k:copy.deepcopy(v) for k,v in old.items() if k!='proposal_execution'};x['record_ids']=x['record_ids']+[e['id']];x['extraction_result']='records_found';x['rationale']='Frozen source-only comparison w3-sufferings-F01: represent explicit contrast of criteria with schema-supported distinction edge; textual direction only, unidentified holders preserved.';cov.append(x)
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_berakhot_correction',epoch=4,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=[e],coverage=cov,open_tails=s['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(s,p,ss,j);r.immutable(HERE/'review_correction001_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'review_correction001_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'review_correction001_receipt.json',r.encoded(out));print(out['snapshot_sha256'])
