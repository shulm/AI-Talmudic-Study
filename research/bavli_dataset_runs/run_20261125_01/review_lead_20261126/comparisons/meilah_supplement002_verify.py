"""Exact frozen-version audit. Never loads CURRENT or writes production."""
from meilah_supplement002_inspect import *
import hashlib,collections
sha=lambda path:hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
bind=lambda path:dict(path=str(pathlib.Path(path).resolve()),sha256=sha(path))
rh=lambda x:m.sha(m.encoded(x))
base=B/'readings/meilah_supplement002.json';add=B/'readings/meilah_supplement002_completion001.json'
assert sha(base)=='3b264d8bd1e4f1e0d4f7c26f4e47d6f2031cc1c5c395693eb10407bc2c2f5994'
assert sha(add)=='1b8afde95786b2c7cd45ec27b1906717321f6d3639eaab061bee0d1eb5929750'
assert sha(J/'snapshots'/f'{H}.json')==H
assert len(allr)==len(a['records'])+len(c['records'])
assert set(c['effective_record_ids'])==(set(allr)-set(c['supersession_map']))
assert len(c['effective_record_ids'])==len(set(c['effective_record_ids']))==1066
for old,new in c['supersession_map'].items():assert old in allr and new in allr and new not in c['supersession_map']
assert not c['remaining_unprocessed_core_coordinates'] and not c['remaining_unprocessed_core_layers']
def checkbindings(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x:assert sha(x['path'])==x['sha256']
  for v in x.values():checkbindings(v)
 elif isinstance(x,list):
  for v in x:checkbindings(v)
for data in [a,c]:
 for key in ['source','job','common_documents','base_artifact']:checkbindings(data.get(key,{}))
def evcheck(x):
 n=0
 if isinstance(x,dict):
  if 'quote' in x and 'start_char' in x:
   t=texts[x['ref']] if 'ref' in x else (texts[x['segment_id']] if x['segment_id'].startswith('Meilah ') else segs[x['segment_id']]['text'])
   assert t[x['start_char']:x['end_char']]==x['quote'];n+=1
  for v in x.values():n+=evcheck(v)
 elif isinstance(x,list):
  for v in x:n+=evcheck(v)
 return n
slice_counts={k:evcheck(v) for k,v in [('base',a),('addendum',c),('effective_records',r),('production_snapshot',p)]}
s=m.empty()
for ph in p['proposals']:
 f=J/'proposals'/f'{ph}.json';assert sha(f)==ph;prev=s['proposals'];s=m.validate_apply(s,read(f),segs,j);s['proposals']=prev+[ph]
assert m.encoded(s)==m.encoded(p) and m.sha(m.encoded(s))==H
core=set(a['core_refs_read']);assert len(core)==128
assert core==set(read(B/'jobs/bavli_meilah_supplement002.json')['core_refs'])
done={l:{segs[z['segment_id']]['ref'] for z in p['coverage'] if z['layer']==l and z['extraction_state']=='completed'} for l in m.LAYERS}
comp=set.intersection(core,*done.values());assert comp==core
active=[x for x in p['records'] if x['release_state']=='valid'];pr={x['id']:x for x in active};rr={x['id']:x for x in r}
scoped=[x for x in active if set(refs(x))&core]
prior=read(B/'comparisons/meilah_batch001_exact_version.json');priorread=read(B/'readings/meilah_batch001.json');priorcores=set(priorread['core_refs']);priorcomp=set(prior['compared_core_refs'])
plan=read(B/'frozen_plans/bavli_meilah.json');prob={z['ref'] for block in plan['review_blocks'] if 'probability_sample' in block['roles'] for z in block['spans']};endpoints={z['ref'] for block in plan['review_blocks'] if any(role in block['roles'] for role in ['opening_check','closing_check']) for z in block['spans']}
newread=core-priorcores
assert len(core&priorcores)==19 and len(newread)==109 and not comp&priorcomp
assert len(newread&prob)==39 and len(newread-prob)==70 and not core&endpoints
def evidence(rs):return [dict(ref=ref,start_char=0,end_char=len(texts[ref]),quote=texts[ref]) for ref in rs]
prefix='meilah_supplement002_completion001.'
def rid(short):return prefix+short
issues=[]
def issue(i,rs,source,target,reader,reason,repair):
 assert source in pr and target in pr
 assert not any(x['layer']=='edges' and x['content'].get('relation')=='objection' and x['content'].get('source_id')==source and x['content'].get('target_id')==target for x in active)
 issues.append(dict(id=i,classification='confirmed_typed_relation_omission',refs=rs,source_record=source,target_record=target,reader_record=reader,reason=reason,repair=repair,evidence=evidence(rs),content_missing=False))
issue('MS02-P01',['Meilah 3b:12','Meilah 3b:13','Meilah 3b:14'],'l06.mei.pigul.q.ulla','l06.mei.pigul.c.abaarrow',rid('edges.0428'),'Rav Ashi’s Ulla objection challenges restricting completed pigul to sprinkling. Producer retains the question, Ashi claim, quoted Ulla support and answer, but no typed objection connects them to the preceding sprinkling qualification.','Add scoped objection link to the sprinkling premise, or an editorially isolated premise if the terse בזריקה requires it; do not reject Ulla’s rule.')
issue('MS02-P02',['Meilah 3b:15','Meilah 4a:2','Meilah 4a:3','Meilah 4a:4','Meilah 4a:5'],'l06.mei.pigul.q.ilfa','l06.mei.pigul.c.potential',rid('edges.0430'),'Ravina’s והאמר אילפא challenges the preliminary-versus-completed-pigul explanation. Question and answer are represented, but the challenge to that explanation is absent in edges.','Add a conservatively scoped objection to the explanation/presupposition; retain one/two-service distinction and sprinkling revelation answer.')
issue('MS02-P03',['Meilah 5a:8','Meilah 5a:9','Meilah 5a:10','Meilah 5a:14','Meilah 5a:15'],'l06.mei.permission.q.wash','l06.mei.permission.c.received',rid('edges.0432'),'מתקיף לה רב יוסף explicitly attacks the precision inference through the washing parallel. Producer has the question and downstream analogy rebuttal, but lacks the direct typed challenge to the initial inference.','Connect the washing objection to the inference or an isolated precision premise, preserving later restoration of meilah precision.')
issue('MS02-P04',['Meilah 5b:3','Meilah 5b:4','Meilah 5b:5','Meilah 5b:6','Meilah 5b:7'],'l06.mei.permission.q.remnants','l06.mei.permission.c.remnants',rid('edges.0435'),'והא בעא מיניה introduces a quoted exchange as challenge to the preceding general invalid-performer-remnants claim. The embedded question/answer and final qualifications exist, but their objection role against that claim lacks an edge.','Represent the outer objection using the quoted exchange and initial exclusion reading, not a bare claim that every genuine question is an objection; retain impurity/other-invalid-person qualifications.')
issue('MS02-P05',['Meilah 7a:1','Meilah 7a:2','Meilah 7a:3','Meilah 7a:4','Meilah 7a:5','Meilah 7a:6'],'l06.mei.yotze.q.asi','l06.mei.yotze.c.diaspora','meilah_supplement002.questions.0648','ומי אמר רב אסי הכי challenges the attributed lost/burned reading through Rav Asi’s earlier question and reply. Producer retains the question and eventual correction but no typed challenge connects the two reports.','Add scoped objection to the initial nonexistent-material reading/report, preserving Rava’s eventual destined-for-loss interpretation. Do not mark the corrected report finally rejected.')
reader_errors=[]
for num,targets,reason,rs in [
 ('0690',['claims.0472','claims.0473'],'Burning qualification applies to bread consecrated by outside-time/place intention, not the no-crust non-consecration claim.',['Meilah 3b:10','Meilah 4a:7']),
 ('0706',['claims.0518','claims.0519'],'Zeira names Hezekiah and Yohanan; the compressed sentence does not object to the unnamed middle sprinkling candidate. Preserve syntax uncertainty instead of this target.',['Meilah 5a:1','Meilah 5a:2']),
 ('0709',['claims.0525'],'The objection concerns requiring both invalid reception and sprinkling, not outside-time slaughter.',['Meilah 5a:6','Meilah 5a:7']),
 ('0712',['claims.0537'],'The tested inference concerns the compound invalid-person clause, not outside-place slaughter.',['Meilah 5a:13','Meilah 5a:14']),
 ('0755',['claims.0626'],'Blood-exit baraita directly supports failure for exited blood; it does not directly prove the positive flesh-exit clause.',['Meilah 7a:7','Meilah 7a:8']),
 ('0767',['claims.0655'],'Priestly-property objection concerns no meilah in meat after sprinkling, not meilah in fats before sprinkling.',['Meilah 7b:10','Meilah 7b:14']),
 ('0769',['claims.0676'],'Owners-property objection concerns no meilah in meat after sprinkling, not before-sprinkling meat.',['Meilah 7b:16','Meilah 7b:17'])]:
 reader_errors.append(dict(id='MS02-R'+num,classification='reader_relation_target_error',reader_record=rid('edges.'+num),relevant_target_candidates=[rid(t) for t in targets],reason=reason,evidence=evidence(rs)))
reader_errors.append(dict(id='MS02-RCOND',classification='reader_condition_error',reader_record=rid('claims.0483'),reason='The single-service agreement inherits the conditions for first and second slaughter-sign intentions, which the preceding clause presents as the two-services example. Separate the one-service branch condition.',evidence=evidence(['Meilah 4a:4'])))
limits=[
 'Reader claims0168 and0581 repeat the no-sprinkling response at6a15 with different local status labels; 242 is effective-record count, not unique semantic topics.',
 'Reader 7a11 declarative elder report versus producer interrogative paraphrase remains a wording alternative; אמרתי לו הן supports an exchange but no punctuation mandates interrogative syntax. No source-content omission inferred.',
 'Producer typed elder/embedded Akiva occurrence roles are coarser than reader nested attribution inventory; narrative content and Rabbi Shimon transmitter remain present. Do not convert granularity difference into missing whole content.',
 'Quoted authority chains in reader for Ravina/Ilfa and Rav Ashi/Ulla need not assert direct teacher transmission. Producer separate speaker/quoted-authority records are acceptable.',
 'Producer generic asserted-discourse-stage status does not imply accepted legal result where proposition explicitly describes challenge, hypothetical or quoted premise.',
 'Reader quoted-premise statuses at4b4–8 and6a15 can inherit hypothetical/challenged from surrounding argument; preserve premise versus inference distinction.',
 'Eight reader editorial comparison questions for6b2–8 are analytical axes, not eight explicit source questions absent from producer. Named opposing answers are present in compound producer claims.',
 'Neither silence at3b11 nor7b8 is an express retraction; reader local_resolution edge0440 must be read with explicit silence caveat.',
 'Rav Giddel/Rav at3b8 and5b14 and anonymous6a18–19 remain different local formulations. No invented harmonization, named-order assignment or practical halakhic verdict.',
 'Continuation restricts invalid performer to communal impurity allowance; Akiva exit rule to partial flesh exit and burning, not permission to eat. Both versions preserve these qualifications.',
 'No statistical error rate or new probability draw inferred from supplemental coordinates. No later-snapshot inheritance or full tractate admission.'
]
cohorts=dict(core_read=128,completed_compared_unique=128,pending=0,prior_direct_reading_overlap=19,new_direct_reading=109,prior_exact_comparison_overlap=0,new_exact_compared_segments=128,original_probability_plan_coordinate_overlap=len(core&prob),new_reading_probability_plan_coordinate_overlap=39,new_reading_outside_probability_plan=70,endpoint_overlap=0,selection='supplemental_coordinate_review_not_probability_sample',probability_sample_credit=0)
bindings=dict(base_reading=bind(base),completion=bind(add),neutral_job=bind(B/'jobs/bavli_meilah_supplement002.json'),source=bind(a['source']['path']),source_schema=bind('F:/Sefaria-Export-master/schemas/Meilah.json'),snapshot=bind(J/'snapshots'/f'{H}.json'),runner=bind(runner),schema=bind(runner.parent/'schema.json'),protocol=bind(runner.parent/'PROTOCOL.md'),inspection_script=bind(pathlib.Path(__file__).parent/'meilah_supplement002_inspect.py'),verification_script=bind(__file__),prior_comparison=bind(B/'comparisons/meilah_batch001_exact_version.json'),prior_reading=bind(B/'readings/meilah_batch001.json'),frozen_plan=bind(B/'frozen_plans/bavli_meilah.json'),policy=bind(B/'POLICY_IMPACT_006.json'),proposals=[bind(J/'proposals'/f'{ph}.json') for ph in p['proposals']])
groups=[('pigul','3b:8','4b:10','Pigul sprinkling, bread, quoted objections, repeated proof and noncategorical support.'),('permission','4b:11','5b:10','Three permission candidates, Hezekiah/Yohanan named answers, washing precision and narrowed remnants.'),('permissionproofs','5b:11','6a:19','Repeated notar/pigul proofs, time-to-sprinkle versus actual sprinkling, local final asymmetry.'),('yotze','6b:1','7a:8','Both offering categories, four liability axes, both counterfactual explanations and exit qualifications.'),('pair','7a:9','7b:8','Simultaneous/sequential scope, nested Shimon/elder/Akiva report, Hoshaya via Resh Lakish, silence.'),('effects','7b:9','8a:2','Before/after and meat/fats distinctions, property objections, Hanina attribution, burning not eating, chapter closure.')]
ordered=a['core_refs_read'];group_rows=[]
for name,start,end,note in groups:
 rs=ordered[ordered.index('Meilah '+start):ordered.index('Meilah '+end)+1]
 group_rows.append(dict(group=name,core_refs=rs,semantic_review='complete_with_findings_and_limits_below',assessment=note,reader_claims=[x['id'] for x in r if x['layer']=='claims' and set(refs(x))&set(rs)],producer_claims=[x['id'] for x in scoped if x['layer']=='claims' and set(refs(x))&set(rs)]))
assert set().union(*(set(g['core_refs']) for g in group_rows))==core
coordinate_rows=[dict(ref=ref,source=evidence([ref])[0],reader_record_ids=[x['id'] for x in r if ref in refs(x)],producer_record_ids=[x['id'] for x in scoped if ref in refs(x)],assessment='Source and semantic inventories compared within group; shared coordinate is evidence alignment, not automatic record equivalence.') for ref in ordered]
layerden=dict(reader_effective=collections.Counter(x['layer'] for x in r),producer_active_core_evidence_overlap=collections.Counter(x['layer'] for x in scoped),producer_completed_per_layer={k:len(v) for k,v in done.items()},compared_completed_per_layer={k:len(v&core) for k,v in done.items()},reader_source_reconciliation_entries=len(c['reconciliation']))
out=dict(artifact_kind='nonblind_exact_version_supplemental_comparison',verdict='REWORK_TARGETED',comparator=dict(agent='/root/compare_zevachim_wave2',blind=False,base_and_completion_frozen_before_comparison=True),bindings=bindings,cohorts=cohorts,denominators=layerden,source_derived_whole_content_omissions=0,confirmed_typed_relation_omissions=5,reader_confirmed_relation_target_errors=7,reader_condition_errors=1,merge=dict(base_records=len(a['records']),additive_records=len(c['records']),superseded_base_records=len(c['supersession_map']),effective_records=len(r),supersession_map=c['supersession_map'],effective_record_ids=c['effective_record_ids'],no_double_count=True),preserved_initial_reading=dict(binding=bindings['base_reading'],initial_status=a['review_status'],initial_counts=a['counts']),preserved_completion=dict(binding=bindings['completion'],counts=c['counts'],unresolved_interpretations=c['unresolved_interpretations'],comparable_answer_sets=c['comparable_answer_sets']),groups=group_rows,coordinate_comparisons=coordinate_rows,effective_reader_records=[dict(record=x,sha256=rh(x)) for x in r],producer_compared_records=[dict(record=x,sha256=rh(x)) for x in scoped],required_changes=issues,reader_corrections=reader_errors,uncertainties_and_limits=limits,qa=dict(all_evidence_slices_exact=True,slice_counts=slice_counts,readonly_prefix_replay_exact=True,proposal_count=len(p['proposals']),replayed_snapshot_sha256=H,no_current_or_lock_or_submit=True),task_eligibility={k:False for k in ['ml','scholar_choice','attribution','retrieval','qa','argument_extraction','segmentation']},tractate_accepted=False,full_review_receipt=False,human_certification=False)
for x in issues+reader_errors:evcheck(x)
cp=B/'comparisons/meilah_supplement002_exact_version.json';assert not cp.exists();cp.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
verdict=dict(verdict=out['verdict'],bindings=bindings,comparison=bind(cp),scope=cohorts,layer_matrix=layerden,required_changes=issues,reader_corrections=reader_errors,exceptions=limits,task_eligibility=out['task_eligibility'],tractate_accepted=False,full_review_receipt=False,human_certification=False,admission_owner='global coordinator',remaining='Repair five explicit relation gaps and recheck exact new snapshot; original source readings and this verdict remain immutable.')
vp=B/'verdicts/meilah_supplement002_v2_verdict.json';assert not vp.exists();vp.write_text(json.dumps(verdict,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(comparison=bind(cp),verdict=bind(vp),cohorts=cohorts,denominators=layerden,qa=out['qa']),ensure_ascii=False))
