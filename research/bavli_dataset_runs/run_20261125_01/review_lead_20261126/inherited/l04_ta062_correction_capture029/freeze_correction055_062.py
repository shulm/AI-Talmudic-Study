import json,hashlib
from pathlib import Path
D=Path(__file__).parent;P=D.parent.parent/'bavli_taanit'
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p):return dict(path=str(p),sha256=sha(p))
def canonical(r):return hashlib.sha256((json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
def write(name,obj):
 p=D/name
 with p.open('x',encoding='utf8') as f:json.dump(obj,f,ensure_ascii=False,indent=2);f.write('\n')
 with Path(str(p)+'.sha256').open('x') as f:f.write(sha(p)+'  '+p.name+'\n')
 return bind(p)
audit=read(D/'correction055_preflight062.json');prior=read(D/'ta055_comparison062.json');sp=P/'snapshots/663ea1da0f7ad381ee844fb537869ef1ebce15930d69048be7b85b064f48a086.json';s=read(sp);pi={r['id']:r for r in s['records'] if r['release_state']=='valid'};proposal=read(P/'proposals/feb5147495135f0904423cc5ffc531f093188144ea8123a42cdd7fe75e363f75.json');inv=read(P/'source_inventory.json');bi={r['id']:r for r in inv}
assert audit['result']=='PASS'
for b in audit['bindings']+prior['bindings']:assert sha(b['path'])==b['sha256']
checkpoint=Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/lanes/L04/resume_20261126/taanit/CHECKPOINT_055.json');cp=read(checkpoint);assert cp['snapshot_sha256']==sp.stem
new15=set(audit['newer15_refs'])
for r in s['records']:
 if any(bi[e['segment_id']]['ref'] in new15 for e in r['evidence']):assert r['review_state']=='unreviewed' and r['ml_eligible'] is False
res=[]
def resolved(key,ids,note):
 old=next(x for x in prior['discrepancy_ledger'] if x['id']==key)
 assert all(i in pi for i in ids)
 res.append(dict(finding_id=key,original_category=old['category'],original_evidence=old['evidence'],original_finding=old['finding'],resolution='RESOLVED_IN_EXACT_CORRECTION',corrected_record_ids=ids,corrected_versions=[dict(id=i,canonical_sha256=canonical(pi[i]),record=pi[i]) for i in ids],independent_source_assessment=note))
for n,stem in enumerate(['iron.scholars','fire.solitary','small.sharpens','water.humility','vessels.humility','attention.liquids'],1):
 premise='ta.review062.'+stem+'.premise';conclusion='ta.resume010.'+stem+'.t062055';edge='ta.review062.'+stem+'.analogy'
 assert pi[edge]['content']==dict(explicitness='source_explicit',relation='analogy',source_id=premise,target_id=conclusion)
 resolved('TA062-GRAPH-A'+str(n),[premise,conclusion,edge,premise+'.a',premise+'.p'],['Iron premise and sharpening conclusion are distinct; printed Hama/Hanina uncertainty and empty unique holder retained.','Fire-not-burning-alone premise supports Torah-not-enduring-alone conclusion; Rabbah bar bar Hanah retained.','Small wood and junior/senior scholars are distinct endpoints under Rav Nahman bar Yitzhak; Hanina testimony remains a separate supporting claim.','Water descending from high to low is distinct from humility condition; Hanina bar Idi retained.','Lowly-vessel necessity is distinct from humility necessity; Oshaya retained, without empirical certification.','Inattention premise and forgetting conclusion are distinct; דבר אחר remains anonymous and both necessity restrictions retained.'][n-1])
for n,(stem,target,note) in enumerate([('fire','ta.resume010.fire.q','Jeremiah establishes the fire comparison basis, not by itself the non-solitary conclusion.'),('foolish','ta.resume010.solitary.foolish','Quoted ונואלו supports the foolishness conclusion; Yosi bar Hanina remains the citing teacher, not the quoted-authority node.'),('wood','ta.resume010.wood.q','Proverbs supplies the tree comparison basis; junior/senior inference remains a separate analogy.'),('water','ta.resume010.water.humility.q','Water invitation supplies comparison basis; humility conclusion is supported through water analogy.')],1):
 source='ta.review062.proof.'+stem;edge=source+'.support'
 assert pi[edge]['content']==dict(explicitness='source_explicit',relation='support',source_id=source,target_id=target)
 assert pi[source+'.a']['content']['role']=='quoted_authority'
 resolved('TA062-GRAPH-B'+str(n),[source,source+'.a',source+'.u',edge,target],note)
edge='ta.resume010.narrative.illustrates.t062055';assert pi[edge]['content']==dict(explicitness='editorial_reconstruction',relation='support',source_id='ta.resume010.wine.sours',target_id='ta.review062.vessels.humility.premise')
resolved('TA062-ENDPOINT',[edge,'ta.resume010.wine.sours','ta.review062.vessels.humility.premise'],'Wine-souring outcome now supports the lowly-vessel premise with editorial explicitness and both narrative segments as evidence. Taunt remains narrative speech; no direct beauty/pride equivalence is introduced.')
assert 'only in lowly vessels' in pi['ta.review062.vessels.humility.premise']['content']['proposition']
resolved('TA062-ONLY-VESSELS',['ta.review062.vessels.humility.premise','ta.review062.vessels.humility.premise.p'],'אין מתקיימין אלא בפחות שבכלים is retained as only in lowly vessels in both proposition and necessary-condition description, scoped within the analogy.')
for i in ['ta.review062.attention.liquids.premise','ta.resume010.attention.liquids.t062055']:assert 'only through inattention' in pi[i]['content']['proposition']
resolved('TA062-ONLY-ATTENTION',['ta.review062.attention.liquids.premise','ta.resume010.attention.liquids.t062055','ta.resume010.attention.liquids.a.t062055'],'Both אין...אלא clauses retain only through inattention; anonymous attribution and alternative-explanation scope survive. Conditions explicitly express necessity.')
assert len(res)==13 and {r['finding_id'] for r in res}=={r['id'] for r in prior['discrepancy_ledger'] if r['category'].startswith('confirmed_producer')}
q='ta.resume010.handsome.scholars.q.t062055';assert any('physical beauty is not identical with pride' in x for x in pi[q]['uncertainty'])
preserved=[x for x in prior['discrepancy_ledger'] if not x['category'].startswith('confirmed_producer')]
assert {x['id'] for x in preserved}=={'TA062-READER-GLOSS','TA062-READER-SOIL','TA062-OBJECTION-SCOPE'}
records=[dict(id=r['id'],layer=r['layer'],supersedes=r.get('supersedes'),canonical_sha256=canonical(pi[r['id']])) for r in proposal['records']]
bindings=[bind(D/'correction055_preflight062.json'),bind(D/'ta055_comparison062.json'),bind(D/'ta055_v2_verdict062.json'),bind(D.parent/'taanit_delegated055.json'),bind(checkpoint),bind(D/'recheck055_062.py'),bind(Path(__file__))]+audit['bindings']
receipt=dict(artifact_kind='immutable_bounded_correction_recheck',execution=dict(agent_id='/root/ta_compare062',role='NONBLIND independent original comparator',fresh_source_only=False),status='BOUNDED_13_FINDINGS_RESOLVED_WITH_PRIOR_RESTRICTIONS',bindings=bindings,snapshot_sha256=sp.stem,base_snapshot_sha256='415494e40a79b4f217d5e265c9d5b126e71677af764a9988013249e571b75888',proposal_sha256='feb5147495135f0904423cc5ffc531f093188144ea8123a42cdd7fe75e363f75',findings_rechecked=13,findings_resolved=13,findings_unresolved_in_this_producer_repair_set=0,issue_by_issue=res,reader_and_unresolved_qualifications_preserved=preserved,unresolved_objection_current_question=pi[q],historical_verdict_preserved='REWORK_TARGETED remains the immutable verdict on historical697; this additive receipt records resolution of its13 producer findings only.',remaining_scope_limits=['Reader lexical and soil expansions remain qualified; frozen reader unchanged.','Physical beauty versus humility objection target remains unresolved, now explicitly noted in producer question.','All other original comparison granularity and restriction assessments remain in force, including7a7 proof-basis representation and no exhaustive answer-set certification.','No whole712 or whole697 semantic re-review; no full admission, new task eligibility or human certification.','Newer15 source segments remain byte-equivalent in records and coverage and explicitly UNREVIEWED.'],changed_record_versions=records,supersessions=37,additions=50,completed_segments_per_layer=712,structural_or_review_core_credit_increment=0,new_reading_credit=0,new_compared_core_credit=0,production_modified_by_comparator=False,newer15_reviewed=False,later_versions_inherit_review=False,full_admission=False,task_eligibility=prior['task_eligibility'],source_edition=prior['source_edition'],source_refs_reread=sorted({bi[e['segment_id']]['ref'] for r in proposal['records'] for e in r['evidence']}),dependency_closure='All active links, edge endpoints, position references and record-valued attribution scopes resolve to active IDs; unchanged original records preserved except37 expected release-state transitions. Answer/support dependencies manually checked after splits.')
rb=write('correction055_receipt062.json',receipt)
validation=dict(result='PASS_BOUNDED_RECHECK',receipt=rb,preflight=bind(D/'correction055_preflight062.json'),helper=bind(Path(__file__)),resolved=13,semantic_review='Manual issue-by-issue original-source comparison of all13 producer findings and changed87 records/dependencies; no broad inherited acceptance.',newer15_review_state_checked='unreviewed; ml_eligible=false',unchanged_frozen_reader=sha(D.parent/'taanit_delegated055.json'),exact_new_snapshot=sha(sp),corrected_records=87,source_evidence_slices=audit['corrected_record_exact_evidence'])
vb=write('correction055_validation062.json',validation)
for p in [D/'recheck055_062.py',Path(__file__)]:
 with Path(str(p)+'.sha256').open('x') as f:f.write(sha(p)+'  '+p.name+'\n')
print(json.dumps(dict(receipt=rb,validation=vb,preflight=bind(D/'correction055_preflight062.json'),helpers=[bind(D/'recheck055_062.py'),bind(Path(__file__))])))
