"""Preserve initial proposal; source-only omission and atomicity follow-up before promotion."""
import json,sys,copy
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah');job,segs=runner.load(J);byref={s['ref']:s for s in segs.values()}
p=json.loads((OUT/'INITIAL_PROPOSAL.json').read_text(encoding='utf-8'));pref='rh.e3.b013.'
def ev(ref,quote):
 s=byref['Rosh Hashanah '+ref];i=s['text'].index(quote);return dict(segment_id=s['id'],start_char=i,end_char=i+len(quote),quote=quote)
for key,prop,condition in [('sages_land','The sages require land release for Jubilee.','Land release must occur'),('sages_shofar','The sages require sounding the shofar for Jubilee.','Shofar must be sounded'),('sages_slaves','The sages require sending the slaves free for Jubilee.','Slaves must be sent free')]:
 r=copy.deepcopy(next(r for r in p['records'] if r['id']==pref+'sages_all_three'));r['id']=pref+key;r['content']['proposition']=prop;r['content']['conditions']=[condition];p['records'].append(r)
 pos=copy.deepcopy(next(r for r in p['records'] if r['id']==pref+'sages_all_three.p'));pos['id']=pref+key+'.p';pos['content']['claim_id']=r['id'];pos['content']['conditions']=[condition];pos['links']=[r['id']];p['records'].append(pos)
 p['records'].append(dict(id=pref+key+'.enumerates',layer='edges',evidence=r['evidence'],content=dict(source_id=r['id'],target_id=pref+'sages_all_three',relation='qualification',explicitness='source_explicit'),links=[r['id'],pref+'sages_all_three'],uncertainty=[],origin='source_paraphrase'))
for key,ref,quote,form,answer in [('q_sanctify','8b:9','מה ת"ל','What does sanctifying the fiftieth year teach?','from_start'),('q_reconcile','9a:5','הא כיצד','How are ninth-day and evening wording reconciled?','daylight_fast')]:
 rid=pref+key;e=ev(ref,quote);p['records'].append(dict(id=rid,layer='questions',evidence=[e],content=dict(formulation=form,question_origin='explicit',conditions=[],answer_set_status='partial'),links=[],uncertainty=[],origin='source_paraphrase'))
 ans=next(r for r in p['records'] if r['id']==pref+answer)
 p['records'].append(dict(id=rid+'.answer',layer='edges',evidence=copy.deepcopy(ans['evidence']),content=dict(source_id=ans['id'],target_id=rid,relation='answer',explicitness='source_explicit'),links=[ans['id'],rid],uncertainty=[],origin='source_paraphrase'))
for coverage in p['coverage']:
 if coverage['layer']=='reconciliation':continue
 coverage['record_ids']=[r['id'] for r in p['records'] if r['layer']==coverage['layer'] and any(e['segment_id']==coverage['segment_id'] for e in r['evidence'])]
 coverage['extraction_result']='records_found' if coverage['record_ids'] else 'none_found_after_pass'
runner.validate_apply(runner.current(J),p,segs,job)
runner.immutable(OUT/'REVIEWED_PROPOSAL.json',runner.encoded(p))
note={'initial_sha256':runner.sha((OUT/'INITIAL_PROPOSAL.json').read_bytes()),'reviewed_sha256':runner.sha(runner.encoded(p)),'changes':['Added explicit what-does-sanctify-teach question8b9 and reconciliation question9a5 with answer edges.','Added three individually recoverable sages action-requirement claims/positions and links to retained aggregate statement9b9. Context coverage remains zero.'],'initial_preserved':True,'independent_reader_seen':False,'records':len(p['records']),'core_segments':20,'expected_completed_per_pass':222}
runner.immutable(OUT/'INTERNAL_REVIEW.json',runner.encoded(note));print(json.dumps(note))
