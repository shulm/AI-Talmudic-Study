"""Bounded source-checked Yevamot corrections; accepted inputs remain immutable."""
import sys,json,copy,hashlib,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[7];sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
OUT=Path(__file__).parent; JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot')
BASE='d2e871c3e71086468534d07c26eda7351bc26789286d55d371a5b95016a22821'
j,ss=runner.load(JOB);state=runner.current(JOB);assert runner.sha(runner.encoded(state))==BASE
runner.authorize(JOB,'L03/yevamot',2)
review=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
inputs=[('comparison_frozen.json',review/'comparisons/yevamot_batch001_exact_version.json','39e77331d9c3a8505a34f29fab1e889d75478811503cf760677ddc349fcdfc9b'),('reader_frozen.json',review/'readings/yevamot_batch001.json','a804e597b4942e1b1d2c60321f1131d07148e812208dff0acb8e1a41d59fbc1f'),('verdict_frozen.json',review/'verdicts/yevamot_batch001_v2_verdict.json','72b5c2f5a876ba878561e198889bc8f8ac1b8d4679537443e6d88a188a9619e1')]
for name,path,h in inputs:
 b=path.read_bytes();assert runner.sha(b)==h;runner.immutable(OUT/name,b)
comparison=json.loads((OUT/'comparison_frozen.json').read_text())
old={r['id']:r for r in state['records'] if r['release_state']=='valid'}
byref={r['ref'].removeprefix('Yevamot '):r for r in ss.values()};new=[];split={};rev={}
def clean(r):
 r=copy.deepcopy(r)
 for k in ['release_state','review_state','ml_eligible','supersedes']:r.pop(k,None)
 return r
def evidence(ref):
 s=byref[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def add(key,layer,refs,content,links=(),origin='source_paraphrase',uncertainty=()):
 rid='yev.review20261126.'+key
 new.append(dict(id=rid,layer=layer,evidence=[evidence(r) for r in refs],content=content,links=list(links),origin=origin,uncertainty=list(uncertainty)));return rid
def split_claim(oid,items):
 ids=[]
 for index,(suffix,text,conditions) in enumerate(items):
  r=clean(old[oid]);r['id']='yev.review20261126.'+suffix;r['content'].update(proposition=text,conditions=conditions)
  if index==0:r['supersedes']=oid;rev[oid]=r['id']
  if suffix in ['permission.miun','permission.aylonit']:r['uncertainty'].append('This opening passage does not fully adjudicate timing for this case; do not inherit the death/divorce chronology. The unexercised-refusal qualification remains separate.')
  new.append(r);ids.append(r['id'])
 split[oid]=ids
conditions=['Listed prohibited relation to surviving brother','Listed relative married to deceased brother with co-wife']
split_claim('yev001.exemption',[
 ('exemption.halitzah','The fifteen listed prohibited relations exempt their co-wives from halitzah.',conditions),
 ('exemption.yibum','The fifteen listed prohibited relations exempt their co-wives from yibum.',conditions),
 ('exemption.recursion','The exemption extends to successive co-wives without a terminal generation.',['Initial co-wife subsequently marries another brother who has a further wife and dies'])])
split_claim('yev001.permission',[
 ('permission.death','The co-wife is permitted when the prohibited relative died.',['Prohibited relative dies before the brother, as the example at 2b:7 clarifies']),
 ('permission.miun','The co-wife is permitted when the prohibited relative exercised mi’un.',['Actual mi’un, not merely eligibility to refuse']),
 ('permission.divorce','The co-wife is permitted when the prohibited relative was divorced.',['Divorce before the brother dies, as the example at 2b:7 clarifies']),
 ('permission.aylonit','The co-wife is permitted when the prohibited relative was found to be an aylonit.',['Discovery as an aylonit; particulars not fully adjudicated in this opening'])])
split_claim('yev001.exclude',[
 ('exclude.aylonit','Mother-in-law, her mother, and father-in-law’s mother cannot be cases of discovery as an aylonit.',['The three specified maternal relatives','Aylonit alternative']),
 ('exclude.miun','Mother-in-law, her mother, and father-in-law’s mother cannot be cases of mi’un.',['The three specified maternal relatives','Mi’un alternative'])])
for oid,who,permit in [('yev004.father_permission','father',True),('yev004.son_permission','son',True),('yev004.father_prohibition','father',False)]:
 split_claim(oid,[(oid.split('.')[-1]+'.'+act,f'A man may {"" if permit else "not "}marry a woman {act} by his {who}.',[f'Woman {act} by his {who}']) for act in ['raped','seduced']])
split_claim('yev004.awaiting',[
 ('awaiting.scope','For the Sages the verse concerns a woman awaiting yibum.',['Sages’ interpretation of the verse']),
 ('awaiting.prohibitions','The Sages’ reading adds transgression of two prohibitions.',['Woman awaiting yibum in this verse’s case'])])
rejection=add('judah.reject_adjacency','claims',['4a:6'],dict(proposition='Rabbi Yehudah rejects mere adjacency as a sufficient basis for imposing stoning in this case.',conditions=['Proposed adjacency derivation of the witch’s penalty'],scope='Rhetorical rejection of the derivation; not rejection of stoning itself.',assertion_mode='asserted'))
add('judah.reject_position','positions',['4a:6'],dict(holder_candidates=['Rabbi Yehudah'],claim_id=rejection,question_id='yev004.judah_objection',conditions=['Proposed adjacency derivation'],local_status='Rejects this derivation; maintains stoning through the alternative derivation at 4a:7'),[rejection,'yev004.judah_objection'])
ben=add('benazzai.derivation','claims',['4a:5'],dict(proposition='Ben Azzai uses adjacency to the animal-intercourse passage as the basis for the witch’s stoning penalty.',conditions=[],scope='Derivational basis only; the penalty is shared with Rabbi Yehudah.',assertion_mode='asserted'))
judah=add('judah.derivation','claims',['4a:7'],dict(proposition='Rabbi Yehudah uses ov and yidoni being singled out from sorcerers to derive the witch’s stoning penalty.',conditions=[],scope='Alternative derivational basis only; no retraction of Ben Azzai’s maintained position is claimed.',assertion_mode='asserted'))
for key,ref,cid,holder in [('benazzai','4a:5',ben,'Ben Azzai'),('judah','4a:7',judah,'Rabbi Yehudah')]:
 add(key+'.derivation.position','positions',[ref],dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=[],local_status='Distinct basis for the same stoning outcome'),[cid])
r=clean(old['yev004.alternative_derivation']);r['id']='yev.review20261126.derivation_objection';r['supersedes']='yev004.alternative_derivation';r['content'].update(source_id=rejection,target_id=ben,relation='objection');r['links']=[rejection,ben];r['evidence']=[evidence('4a:6')];new.append(r);rev[r['supersedes']]=r['id']
add('judah.derivation_distinction','edges',['4a:7'],dict(source_id=judah,target_id=ben,relation='distinction',explicitness='source_explicit'),[judah,ben])
q=add('question.judah_reason','questions',['4a:9'],dict(formulation='What is Rabbi Yehudah’s reason for prohibiting the father’s raped or seduced woman?',question_origin='explicit',conditions=['Rabbi Yehudah’s ruling at 4a:8'],answer_set_status='partial'))
add('answer.judah_reason','edges',['4a:9'],dict(source_id='yev004.father_skirt',target_id=q,relation='answer',explicitness='source_explicit'),['yev004.father_skirt',q])
add('question.judah_reason.transmission','attributions',['4a:9'],dict(surface='ואמר רב גידל אמר רב',role='transmitter',candidates=['רב גידל'],scope='Rav Giddel transmits Rav’s explanation of Rabbi Yehudah; no independent adoption of the ruling is inferred.',transmission_chain=['רב גידל','רב']),[q,'yev004.father_skirt'])
# Positions are split with the claims; their conditions are copied from each new atom.
claims={r['id']:r for r in new if r['layer']=='claims'}
for oid,r0 in old.items():
 if r0['layer']!='positions' or r0['content']['claim_id'] not in split:continue
 for n,cid in enumerate(split[r0['content']['claim_id']]):
  r=clean(r0);r['id']='yev.review20261126.position.'+oid+'.'+str(n);r['content']['claim_id']=cid;r['content']['conditions']=claims[cid]['content']['conditions'];r['links']=[cid if x==r0['content']['claim_id'] else x for x in r['links']]
  if n==0:r['supersedes']=oid;rev[oid]=r['id']
  new.append(r)
# Explicitly scope dependencies rather than projecting every condition to every split.
edge_pairs={
 'yev001.chronology.qual':[(None,0),(None,2)],
 'yev001.exclude.qual':[(0,3),(1,1)],
 'yev001.refusal.qual':[(None,1)],
 'yev004.father_dispute':[(0,0),(1,1)],
 'yev004.sages_interpretation':[(0,None)]}
for oid,r0 in old.items():
 if r0['layer']!='edges' or oid in rev:continue
 c=r0['content'];a=split.get(c['source_id'],[c['source_id']]);b=split.get(c['target_id'],[c['target_id']])
 if c['source_id'] not in split and c['target_id'] not in split:continue
 pairs=edge_pairs.get(oid,list(itertools.product(range(len(a)),range(len(b)))))
 for n,(i,k) in enumerate(pairs):
  x=a[i if i is not None else 0];y=b[k if k is not None else 0];r=clean(r0);r['id']='yev.review20261126.edge.'+oid+'.'+str(n);r['content'].update(source_id=x,target_id=y);r['links']=[x,y]
  if n==0:r['supersedes']=oid;rev[oid]=r['id']
  new.append(r)
# Any other typed dependencies receive a revision with the primary split successor.
while True:
 changed=False
 for oid,r0 in old.items():
  if oid in rev:continue
  c=r0['content'];deps=r0['links']+[c[k] for k in ['source_id','target_id','claim_id','question_id'] if c.get(k)]
  if not any(x in rev for x in deps):continue
  r=clean(r0);r['id']='yev.review20261126.dependent.'+oid;r['supersedes']=oid;r['links']=[rev.get(x,x) for x in r['links']]
  for k in ['source_id','target_id','claim_id','question_id','scope']:
   if isinstance(r['content'].get(k),str):r['content'][k]=rev.get(r['content'][k],r['content'][k])
  new.append(r);rev[oid]=r['id'];changed=True
 if not changed:break
active=[r for r in old.values() if r['id'] not in rev]+new
affected={e['segment_id'] for r in new for e in r['evidence']}
coverage=[]
for cell in state['coverage']:
 if cell['segment_id'] not in affected and not any(x in rev for x in cell['record_ids']):continue
 c=copy.deepcopy(cell);c.pop('proposal_execution',None)
 c['record_ids']=[r['id'] for r in active if (c['layer']=='reconciliation' or r['layer']==c['layer']) and any(e['segment_id']==c['segment_id'] for e in r['evidence'])]
 c['extraction_result']='records_found' if c['record_ids'] else 'none_found_after_pass';c['rationale']='Bounded source reread after independent comparison: split distinct conditions/outcomes; death/divorce chronology not extended to miun/aylonit; rhetorical rejection and explicit question retained; derivation dispute does not change shared stoning outcome.';coverage.append(c)
p=dict(schema_version=runner.VERSION,tractate=j['tractate'],owner='L03/yevamot',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=new,coverage=coverage,open_tails=state['open_tails'])
runner.validate_apply(state,p,ss,j)
runner.immutable(OUT/'proposal.json',runner.encoded(p));result=runner.submit(JOB,OUT/'proposal.json','L03/yevamot',2);replay=runner.replay(JOB)
assert all(n==178 for n in replay['completed_by_layer'].values())
export=JOB.parent/'yv_export_review_20261126_001';runner.export(JOB,export)
manifest=json.loads((export/'MANIFEST.json').read_text())
for f,h in manifest['files'].items():assert runner.sha((export/f).read_bytes())==h
response=dict(status='PRODUCER_CORRECTION_PENDING_INDEPENDENT_VERIFICATION',base_snapshot=BASE,**result,split_lineage=split,revision_map=rev,new_records=len(new),superseded=len(rev),coverage_cells=len(coverage),comparison_sha256=inputs[0][2],reader_sha256=inputs[1][2],verdict_sha256=inputs[2][2],issues={'YV-ATOMIC':'Separated halitzah, yibum, recursion; four release cases; two exception classes; father/son rape/seduction; awaiting-yibum scope and two prohibitions. Added rhetorical rejection claim. Preserved old question and source attribution.','YV-QUESTION':'Added explicit 4a:9 reason question and answer from existing Rav explanation, retaining Rav Giddel transmission.','YV-DERIVATION-SCOPE':'Replaced ambiguous correction edge with rejection of adjacency basis and distinct derivation endpoints; no penalty reversal.'},reader_corrections_preserved=comparison['reader_corrections'],uncertainties_preserved=comparison['uncertainties_preserved'],limits=['No new source coverage','No independent acceptance or task eligibility','Schema has one primary supersedes; complete split lineage supplied separately','Thirty-core comparison is not full-tractate review'],export_manifest_path=str(export/'MANIFEST.json'),export_manifest_sha256=runner.sha((export/'MANIFEST.json').read_bytes()))
runner.immutable(OUT/'RESPONSE.json',runner.encoded(response));runner.immutable(OUT/'replay.json',runner.encoded(replay))
print(json.dumps(dict(result=result,records=len(new),superseded=len(rev),response_sha256=runner.sha((OUT/'RESPONSE.json').read_bytes())),indent=2))
