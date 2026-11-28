import copy,json,sys,hashlib
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;lane=out.parents[1];job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=runner.current(job);assert runner.sha(runner.encoded(base))=='35b7ebfcb7db5043158ff0c726dcc652b35c89703a6622f26fea2383c8faa007'
runner.authorize(job,'L03/eruvin',2);j,src=runner.load(job);seg=list(src.values());old={r['id']:r for r in base['records'] if r['release_state']=='valid'}
active=runner.read(root/'research/bavli_dataset_runs/ACTIVE_RUN.json');contract=runner.read(root/active['contract_path']);assert sha(root/active['contract_path'])==active['contract_sha256']
for f,h in contract['production_files'].items():assert sha(root/f)==h
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/eruvin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=[],coverage=[],open_tails=base['open_tails'])
replacements={};added={}
def ev(i):
 s=seg[i];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def add(k,layer,inds,content,links=None,uncertainty=None,origin='source_paraphrase',supersedes=None):
 rid='er.fix20.'+k;r=dict(id=rid,layer=layer,evidence=[ev(i) for i in inds],content=content,links=links or [],uncertainty=uncertainty or [],origin=origin)
 if supersedes:r['supersedes']=supersedes;replacements[supersedes]=rid
 p['records'].append(r);added[rid]=r;return rid
def cl(k,inds,txt,holder='anonymous Gemara',conditions=None,mode='asserted',supersedes=None,uncertainty=None):
 c=add(k,'claims',inds,dict(proposition=txt,conditions=conditions or [],scope='Local explanation or projecting-lehi ruling; continuation qualifications separately linked',assertion_mode=mode),uncertainty=uncertainty,supersedes=supersedes)
 pos=old.get(supersedes+'.p') if supersedes else None
 add(k+'.p','positions',inds,dict(holder_candidates=[holder] if holder else [],claim_id=c,question_id=None,conditions=conditions or [],local_status=mode+' at this argument stage'),[c],uncertainty,supersedes=pos['id'] if pos else None)
 return c
def edge(k,inds,a,b,rel='qualification',supersedes=None,explicitness='source_explicit'):
 return add(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness=explicitness),[a,b],supersedes=supersedes)
def oid(k):return 'er.next20.'+k
# ER01: distinguish explanatory reconstruction from the explicit quantitative question.
eq=add('explanation_q','questions',[111,114,115,116],dict(formulation='What explains the differing required widths of the raised floor area?',question_origin='editorial_reconstruction',conditions=['Width dispute; alternative explanations retained separately'],answer_set_status='partial'),origin='editorial_inference',uncertainty=['Editorial formulation of the explanatory issue, not a verbatim interrogative.'])
for k,c,i,premise in [('first_heker','recognition',114,'all_permit'),('first_partition','partition',114,'all_permit'),('second_same','same_recognition',115,'all_recognition'),('second_different','different_recognition',115,'all_recognition'),('third_decree','diminish',116,'all_equate')]:
 edge(k,[i],oid(c),eq,'answer',supersedes=oid(k),explicitness='editorial_reconstruction')
 edge(k+'.premise',[i],oid(premise),oid(c))
# ER02: retain individual hypothetical alignments and conditional outcomes.
ay=cl('alignment_yosef',[119],'The proposed explanation has Rav Yosef accepting Rabbi Ami’s reported rule.',conditions=['Proposed alignment only'],mode='hypothetical',supersedes=oid('alignment_hyp'))
aa=cl('alignment_abaye',[119],'The proposed explanation has Abaye rejecting Rabbi Ami’s reported rule.',conditions=['Proposed alignment only; Abaye’s following reply avoids this disagreement'],mode='hypothetical')
edge('align_correct',[120,119],oid('existing_new'),aa,'correction',supersedes=oid('align_correct'))
for stem,i,short in [('project_short',125,True),('project_four',125,False),('repeat_short',128,True),('repeat_four',128,False)]:
 cond=['Projection from alley wall','Projection below four cubits' if short else 'Projection four cubits']
 classification='The projection is classified as a lehi.' if short else 'The projection is classified as an alley.'
 cl(stem+'_classification',[i],classification,'Rav Huna (reported by Rami bar Hama)',cond,supersedes=oid(stem))
 cl(stem+'_obligation',[i],'No additional lehi is required.' if short else 'An additional lehi is required at this statement stage.','Rav Huna (reported by Rami bar Hama)',cond,uncertainty=[] if short else ['Later seven/eight and Rav Ashi qualifications remain separately linked.'])
for stem in ['short','four']:
 edge('repeat_obligation_'+stem,[125,127,128],'er.fix20.repeat_'+stem+'_obligation','er.fix20.project_'+stem+'_obligation','quotation')
# The proof uses classification; quotation edges will follow the immutable replacements.
eight=cl('eight_context',[131],'The additional-lehi requirement applies in the eight-unit alley according to Rav Huna son of Rav Yehoshua.','Rav Huna son of Rav Yehoshua',['Eight-unit alley'],supersedes=oid('seven_context'),uncertainty=['5b7–8 identifies this as his own reasoning; not Rav Huna’s.'])
seven=cl('seven_permission',[131],'The seven-unit alley is permitted by standing wall exceeding the breach.','Rav Huna son of Rav Yehoshua',['Seven-unit alley','Standing wall exceeds breach'])
ashi=cl('ashi_no_extra',[136],'Rav Ashi says even the eight-unit alley needs no additional lehi.','Rav Ashi',['Eight-unit alley; alternative relative-width branches follow'],supersedes=oid('ashi_context'))
standing=cl('ashi_standing',[136],'The alley is permitted by standing wall exceeding the breach.','Rav Ashi',['Eight-unit alley','Standing wall exceeds breach'])
breach=cl('ashi_breach',[136],'The projection is classified as a lehi.','Rav Ashi',['Eight-unit alley','Breach exceeds standing wall'])
edge('ashi_standing_support',[136],standing,ashi,'support');edge('ashi_breach_support',[136],breach,ashi,'support')
for occurrence in ['project','repeat']:
 target='er.fix20.'+occurrence+'_four_obligation'
 edge('seven_'+occurrence,[131],seven,target)
 edge('eight_'+occurrence,[131],eight,target)
 edge('ashi_'+occurrence,[136],ashi,target)
# Old qualification edges targeted bundled rules: supersede them toward obligation, not classification.
for name,source,occurrence,i in [('seven_first',eight,'project',131),('seven_repeat',eight,'repeat',131),('ashi_first',ashi,'project',136),('ashi_repeat',ashi,'repeat',136)]:
 edge(name+'.revision',[i],source,'er.fix20.'+occurrence+'_four_obligation',supersedes=oid(name))
# ER03: source-explicit continuation restricts the earlier teaching to wall remnants.
rem=cl('remnants',[147,148],'The Rabbi Ami/Rav Asi case is distinguished as having remaining wall remnants (gidudi).',conditions=['Earlier reported side-breach teaching'],uncertainty=['Source says גידודי; no additional geometric dimensions inferred.'])
none=cl('no_remnants',[147,148],'The contrasting Rav Huna case has no remaining wall remnants (gidudi).',conditions=['Rav Huna breach ruling in the continuation'],uncertainty=['Rav Huna is not Rav Huna son of Rav Yehoshua.'])
edge('remnant_distinction',[147,148],rem,none,'distinction')
for k in ['strip_four','no_strip_under','no_strip_three']:
 edge('remnants_'+k,[118 if k=='strip_four' else 119,147,148],rem,oid(k))
# Revise every live dependency transitively; preserve all initial records.
def clean(r):return {k:copy.deepcopy(v) for k,v in r.items() if k not in ['review_state','release_state','ml_eligible']}
def remap(v):
 if isinstance(v,str):return replacements.get(v,v)
 if isinstance(v,list):return [remap(x) for x in v]
 if isinstance(v,dict):return {k:remap(x) for k,x in v.items()}
 return v
while True:
 changed=False
 for rid,r in old.items():
  if rid in replacements:continue
  if remap(r['links'])!=r['links'] or remap(r['content'])!=r['content']:
   n=clean(r);n['id']='er.fix20.dependent.'+rid;n['supersedes']=rid;n['links']=remap(n['links']);n['content']=remap(n['content']);replacements[rid]=n['id'];p['records'].append(n);added[n['id']]=n;changed=True
 if not changed:break
for r in p['records']:r['links']=remap(r['links']);r['content']=remap(r['content'])
live={k:v for k,v in old.items() if k not in replacements};live.update(added)
for c in base['coverage']:
 n={k:copy.deepcopy(v) for k,v in c.items() if k!='proposal_execution'}
 ids=[rid for rid,r in live.items() if (n['layer']=='reconciliation' or r['layer']==n['layer']) and any(e['segment_id']==n['segment_id'] for e in r['evidence'])]
 if set(ids)!=set(n['record_ids']):
  n['record_ids']=sorted(ids);n['extraction_result']='records_found' if ids else 'none_found_after_pass';n['rationale']+=' Independent ER01–03 repair: scoped explanatory issue, atomic conditional rules, and source-backed gidudi continuation. No new source coverage.';p['coverage'].append(n)
runner.validate_apply(base,p,src,j)
def save(name,v):runner.immutable(out/name,runner.encoded(v))
save('PROPOSAL.json',p)
save('LINEAGE.json',dict(base_snapshot=runner.sha(runner.encoded(base)),replacements=replacements,new_rows=len(p['records']),coverage_cells_refreshed=len(p['coverage']),review_verdict_sha256=sha(lane/'eruvin_next20_source_review_20261127/comparison/VERDICT.json'),source_sha256=j['source_sha256'],contract_sha256=active['contract_sha256'],owner=runner.read(job/'OWNER.json')))
print(json.dumps(dict(proposal_sha256=sha(out/'PROPOSAL.json'),new_rows=len(p['records']),superseded=len(replacements),coverage_cells=len(p['coverage']))))
