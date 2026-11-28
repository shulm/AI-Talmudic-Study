import copy,json,sys
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin');base=runner.current(job)
assert runner.sha(runner.encoded(base))=='a78a43540816ccb3736a4215e01527105c3c3602499ea78515bfb7c44901484c';runner.authorize(job,'L03/eruvin',2)
j,src=runner.load(job);seg=list(src.values());old={r['id']:r for r in base['records'] if r['release_state']=='valid'}
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/eruvin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=[],coverage=[],open_tails=base['open_tails'])
def ev(i):
 s=seg[i];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(k,l,inds,c,links=None,u=None):
 rid='er022fix.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(i) for i in inds],content=c,links=links or [],uncertainty=u or [],origin='source_paraphrase'));return rid
def cl(k,inds,txt,cond):
 c=rec(k,'claims',inds,dict(proposition=txt,conditions=cond,scope='Rav Yosef recites Rav Yehuda in Rav’s name before Rav Huna; distinct from following disputed rehava attribution',assertion_mode='asserted'))
 rec(k+'.p','positions',inds,dict(holder_candidates=['Rav (reported by Rav Yehuda, recited by Rav Yosef)'],claim_id=c,question_id=None,conditions=cond,local_status='Continuation qualification of the earlier enclosure dispute'),[c]);return c
def e(k,inds,a,b,rel='qualification'):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
street=cl('street_scope',[177],'The dispute applies when a road is at each end.',['Road at both ends'])
plaza=cl('plaza_scope',[177],'The dispute applies when a plaza is at each end.',['Plaza at both ends'])
sf=cl('street_field',[178],'With road at one end and open field at the other, an entrance-form at one end and a lehi or beam at the other suffices.',['Road / open field'])
ff=cl('field_field',[178],'With open field at both ends, an entrance-form at one end and a lehi or beam at the other suffices.',['Open field / open field'])
clar=cl('clarification',[180],'The road/open-field case is treated like the open-field/open-field case.',['Clarification of apparent redundancy'])
q=rec('redundancy_q','questions',[179],dict(formulation='If the road/open-field case uses this remedy, is the open-field/open-field case not obvious?',question_origin='explicit',conditions=[],answer_set_status='partial'))
e('clar_answer',[179,180],clar,q,'answer');e('clar_sf',[178,180],clar,sf)
rec('transmission','attributions',[177],dict(surface='יתיב רב יוסף קמיה דרב הונא ... אמר רב יהודה אמר רב',role='transmitter',candidates=['Rav Yosef'],scope='Rav Yosef recites Rav Yehuda’s report of Rav before Rav Huna; Rav Huna is the listener, not a transmission link',transmission_chain=['Rav Yosef','Rav Yehuda','Rav']))
for key in ['first_tanna','bs_doors','bs_lock','bh_door','rav_first','shmuel_hananya']:
 target='er022.'+key
 for name,c,inds in [('street',street,[149,177]),('plaza',plaza,[149,177]),('streetfield',sf,[149,178]),('fieldfield',ff,[149,178])]:e(key+'_'+name,inds,c,target)
live=dict(old);live.update({r['id']:r for r in p['records']})
for cell in base['coverage']:
 ids=sorted(rid for rid,r in live.items() if (cell['layer']=='reconciliation' or r['layer']==cell['layer']) and any(x['segment_id']==cell['segment_id'] for x in r['evidence']))
 if set(ids)!=set(cell['record_ids']):
  n={k:copy.deepcopy(v) for k,v in cell.items() if k!='proposal_execution'};n.update(record_ids=ids,extraction_result='records_found' if ids else 'none_found_after_pass');n['rationale']+=' ER002_SCOPE01: retain7a12–15 road/plaza versus field qualifications and transmitted common remedy, no new core coverage.';p['coverage'].append(n)
runner.validate_apply(base,p,src,j);runner.immutable(out/'PROPOSAL.json',runner.encoded(p))
runner.immutable(out/'LINEAGE.json',runner.encoded(dict(base_snapshot=runner.sha(runner.encoded(base)),review_verdict_sha256=runner.sha((out.parents[1]/'eruvin_next20_002_review_20261127/comparison/VERDICT.json').read_bytes()),new_rows=len(p['records']),superseded=0,new_core_coverage=0,source_sha256=j['source_sha256'],owner=runner.read(job/'OWNER.json'))))
print(json.dumps(dict(proposal_sha256=runner.sha((out/'PROPOSAL.json').read_bytes()),rows=len(p['records']),coverage_cells=len(p['coverage']))))
