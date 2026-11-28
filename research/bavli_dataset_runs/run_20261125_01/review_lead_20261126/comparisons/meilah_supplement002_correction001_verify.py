"""Additive nonblind correction audit; exact proposal-prefix replay, no production writes."""
from meilah_supplement002_inspect import *
import hashlib
sha=lambda f:hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest()
bind=lambda f:dict(path=str(pathlib.Path(f).resolve()),sha256=sha(f))
rh=lambda x:m.sha(m.encoded(x))
newhash='0263df2af59e595ea64c433d210aeee2b9bda623a074860da093be284df2a445'
ph='e068ee80b7b7c7a340ac60340047e6b01ad71d660839bb9aa49c3b58bc5b5248'
nf=J/'snapshots'/f'{newhash}.json';pf=J/'proposals'/f'{ph}.json'
assert sha(nf)==newhash and sha(pf)==ph
new=read(nf);proposal=read(pf)
initialpath=B/'comparisons/meilah_supplement002_exact_version.json';initial=read(initialpath)
assert sha(initialpath)=='7b67e72832a17b63ec4aea7efe34de5b3592c4dc9b627f91172457f760ece89b'
assert initial['bindings']['snapshot']['sha256']==H
assert new['proposals'][:len(p['proposals'])]==p['proposals'] and new['proposals'][-1]==ph
state=m.empty()
for h in new['proposals']:
 if h==ph:before_correction=state
 f=J/'proposals'/f'{h}.json';assert sha(f)==h;previous=state['proposals'];state=m.validate_apply(state,read(f),segs,j);state['proposals']=previous+[h]
assert m.encoded(state)==m.encoded(new) and m.sha(m.encoded(state))==newhash
oldrecords={x['id']:x for x in p['records']};newrecords={x['id']:x for x in new['records']}
assert all(newrecords[k]==v for k,v in oldrecords.items())
before_records={x['id']:x for x in before_correction['records']}
assert all(newrecords[k]==v for k,v in before_records.items())
added=set(newrecords)-set(before_records);assert added=={x['id'] for x in proposal['records']} and len(added)==6
assert sum(newrecords[k]['layer']=='edges' for k in added)==5
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
counts=dict(initial_comparison_slices=evcheck(initial),added_record_slices=evcheck([newrecords[k] for k in added]),corrected_snapshot_all_slices=evcheck(new))
oldcov={(x['segment_id'],x['layer']):x for x in before_correction['coverage']};newcov={(x['segment_id'],x['layer']):x for x in new['coverage']}
assert set(oldcov)==set(newcov)
assert all(oldcov[k]['extraction_state']==newcov[k]['extraction_state'] for k in oldcov)
assert all(newrecords[k]['release_state']=='valid' for k in added)
reasons={
 'MS02-P01':'The source explicitly raises Ulla’s handful/slaughter-equivalence objection after Rabbi Abba’s sprinkling qualification. The edge correctly targets that premise, not Ulla’s substantive teaching; the later precursor-pigul response is retained.',
 'MS02-P02':'Ravina’s והאמר אילפא challenges the preceding precursor/completed-pigul explanation. The link to that explanation is supported by the question and the sprinkling-revelation answer. The target is a local premise, not a final rejection of Ilfa or Rava.',
 'MS02-P03':'מתקיף לה רב יוסף introduces the washing parallel as a challenge to the inference from precise invalid-person wording. The edge reaches that inference, while the later restoration of meilah precision and remnants qualification remain unchanged.',
 'MS02-P04':'The new composite utterance isolates the anonymous outer quotation objection at5b5–7. Its objection edge targets the prior general remnants claim. It explicitly distinguishes this use from Resh Lakish’s original genuine inquiry, and leaves the inclusion reply and impurity-versus-other-invalid distinction in place.',
 'MS02-P05':'ומי אמר רב אסי הכי challenges the initial lost/burned report reading using the earlier poured-blood exchange. The edge targets that report without assigning the challenge to Rav Asi himself. Rava’s correction to material destined for loss/burning remains active.'}
outcomes=[]
for issue in initial['required_changes']:
 key=issue['id'];edge=newrecords['l06.mei.review002.e.'+key]
 expected_source=issue['source_record'] if key!='MS02-P04' else 'l06.mei.review002.u.outer_remnants_objection'
 assert edge['content']==dict(explicitness='source_explicit',relation='objection',source_id=expected_source,target_id=issue['target_record'])
 assert all(newrecords[k]['release_state']=='valid' for k in edge['links'])
 outcomes.append(dict(id=key,disposition='RESOLVED_AT_EXACT_VERSION',reason=reasons[key],initial_finding=issue,correction_record=dict(record=edge,sha256=rh(edge)),endpoint_records=[dict(record=newrecords[k],sha256=rh(newrecords[k])) for k in edge['links']]))
core=set(a['core_refs_read']);done={l:{segs[x['segment_id']]['ref'] for x in new['coverage'] if x['layer']==l and x['extraction_state']=='completed'} for l in m.LAYERS}
assert all(core<=v for v in done.values())
bindings=dict(initial_comparison=bind(initialpath),initial_verdict=bind(B/'verdicts/meilah_supplement002_v2_verdict.json'),base_reading=bind(B/'readings/meilah_supplement002.json'),reader_completion=bind(B/'readings/meilah_supplement002_completion001.json'),prior_snapshot=bind(J/'snapshots'/f'{H}.json'),correction_snapshot=bind(nf),correction_proposal=bind(pf),source=bind(a['source']['path']),runner=bind(runner),schema=bind(runner.parent/'schema.json'),protocol=bind(runner.parent/'PROTOCOL.md'),verification_script=bind(__file__),inspection_script=bind(pathlib.Path(__file__).parent/'meilah_supplement002_inspect.py'),proposal_prefix=[bind(J/'proposals'/f'{h}.json') for h in new['proposals']])
out=dict(artifact_kind='nonblind_exact_version_targeted_correction_receipt',verdict='ACCEPT_TARGETED_CORRECTIONS_PROVISIONALLY',comparator=dict(agent='/root/compare_zevachim_wave2',blind=False,fresh_source_only_reading=False),bindings=bindings,scope=dict(inherited_compared_core_segments=128,corrections_reviewed=5,resolved=5,unresolved=0,added_edges=5,added_outer_quotation_utterances=1,producer_completed_per_layer={k:len(v) for k,v in done.items()},new_source_reading_credit=0,new_comparison_coverage_credit=0,new_probability_credit=0),outcomes=outcomes,qa=dict(readonly_prefix_replay_exact=True,proposal_count=len(new['proposals']),replayed_snapshot_sha256=newhash,all_evidence_slices_exact=True,slice_counts=counts,all_prior_records_byte_semantics_unchanged=True,coverage_coordinate_layer_keys_unchanged=True,coverage_completion_states_unchanged=True),preserved_reader_corrections=initial['reader_corrections'],preserved_uncertainties=initial['uncertainties_and_limits'],limitations=['Only MS02-P01–P05 corrections adjudicated, not a new exhaustive128-core re-review.','Source-explicit labels accepted for overt objection relations; endpoint interpretation remains local and carries original qualification notes.','P04 is an outer anonymous objection through quoted exchange, not a reassignment of the genuine questioner’s role.','Original reader errors, uncertainty, first comparison and verdict preserved.','No further production-version inheritance; no full admission, practical halakhic determination or task eligibility.'],task_eligibility={k:False for k in initial['task_eligibility']},tractate_accepted=False,full_review_receipt=False,human_certification=False,production_modified=False)
f=B/'comparisons/meilah_supplement002_correction001.json';assert not f.exists();f.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps(dict(artifact=bind(f),scope=out['scope'],qa=out['qa']),ensure_ascii=False))
