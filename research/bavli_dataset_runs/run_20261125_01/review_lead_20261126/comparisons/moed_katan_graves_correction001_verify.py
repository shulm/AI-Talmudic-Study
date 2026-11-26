import json, hashlib, importlib.util, sys
from pathlib import Path
sys.dont_write_bytecode=True
B=Path(__file__).resolve().parent.parent
L=Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/lanes/L04/resume_20261126/reviews/capture_006/moed_graves_source_only')
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_moed_katan')
R=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1/runner.py')
H='a1975ae0ad304308269faed47845d10a96f9bf34ac97f5b19799169d6a05f09f'
read=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
bind=lambda p:dict(path=str(Path(p).resolve()),sha256=sha(p))
sp=importlib.util.spec_from_file_location('readonly_runner',R);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
j,segs=m.load(J);texts={x['ref']:x['text'] for x in segs.values()}
p=read(J/'snapshots'/f'{H}.json');assert sha(J/'snapshots'/f'{H}.json')==H
s=m.empty()
for ph in p['proposals']:
 f=J/'proposals'/f'{ph}.json';assert sha(f)==ph;prev=s['proposals'];s=m.validate_apply(s,read(f),segs,j);s['proposals']=prev+[ph]
assert m.encoded(s)==m.encoded(p) and m.sha(m.encoded(s))==H
names=['initial_reading.json','FREEZE.json','RECEIPT.json','comparison.json','compared_records.json','correction_recheck_a1975ae0.json']
original={n:read(L/n) for n in names};receipt=original['RECEIPT.json'];initial=original['initial_reading.json'];oldcomp=original['comparison.json']
for n,k in [('initial_reading.json','initial_reading_sha256'),('FREEZE.json','freeze_sha256'),('comparison.json','comparison_sha256'),('compared_records.json','compared_records_sha256')]:assert sha(L/n)==receipt[k]
assert original['FREEZE.json']['initial_reading_sha256']==sha(L/'initial_reading.json')
def slices(x):
 n=0
 if isinstance(x,dict):
  if 'quote' in x and 'start_char' in x:
   t=texts[x['ref']] if 'ref' in x else segs[x['segment_id']]['text'];assert t[x['start_char']:x['end_char']]==x['quote'];n+=1
  for v in x.values():n+=slices(v)
 elif isinstance(x,list):
  for v in x:n+=slices(v)
 return n
counts={n:slices(x) for n,x in original.items()};counts['exact_snapshot_all_records']=slices(p)
core=set(initial['core_refs']);active=[x for x in p['records'] if x['release_state']=='valid'];byid={x['id']:x for x in active}
scoped=[x for x in active if any(segs[e['segment_id']]['ref'] in core for e in x['evidence'])]
done={layer:{segs[x['segment_id']]['ref'] for x in p['coverage'] if x['layer']==layer and x['extraction_state']=='completed'} for layer in m.LAYERS}
assert all(core<=v for v in done.values())
prop=read(J/'proposals/1ce1bc0c08eb1f62229190b9662126420213015f1d6c4e094e66a039e99a5e2e.json')
oldids={x['supersedes'] for x in prop['records'] if 'supersedes' in x}
stale=[]
for x in active:
 deps=set(x.get('links',[]))|{v for v in x['content'].values() if isinstance(v,str)}
 if deps&oldids:stale.append(x['id'])
assert not stale
assert not any(oldids&set(x['record_ids']) for x in p['coverage'])
assert byid['mk.r013.border.p.review019']['content']['holder_candidates']==[]
assert byid['mk.r013.border.a.review019']['content']['role']=='quoted_authority'
assert byid['mk.r013.field_challenge.review019']['content']['target_id']=='mk.r019.tent_assumption'
assert byid['mk.r019.ploughed_objection']['content']['target_id']=='mk.r019.no_marking_consequence'
dest=B/'inherited/moed_katan_graves_capture006';assert not dest.exists();dest.mkdir(parents=True)
for n in names:(dest/n).write_bytes((L/n).read_bytes());assert sha(dest/n)==sha(L/n)
source=Path(j['source_root'])/next(x for x in read(J/'source_manifest.json')['tractates'] if x['title']==j['tractate'])['source_path']
assert sha(source)==initial['source_sha256']
adjudications=[
 dict(id='MG01',status='RESOLVED_AT_EXACT_VERSION',reason='כדאמר עולא cites Ulla while הכא נמי makes the local anonymous application. Corrected voice and empty holder candidates now preserve that distinction; quoted-authority scope is explicit.',remaining_limit='No inference that Ulla personally stated this local application.'),
 dict(id='MG02',status='RESOLVED_AT_EXACT_VERSION',reason='5b:10 objects to tent impurity presupposed by the marked-field context, not the ploughing terminology at5b:9. The new hypothetical editorial target isolates precisely that implication; 5b:12 preserves both field categories.',remaining_limit='The target is reconstructed presupposition, not a separately spoken source claim.'),
 dict(id='MG03',status='RESOLVED_AT_EXACT_VERSION',reason='5b:16 explicitly challenges the inferred no-marking consequence. New objection and editorial scope relation correctly attach it to Rav Pappa’s distinction. 5b:18 answers with the sequence of lost grave, marking, then later ploughing; no unrestricted final prohibition of marking is inferred.',remaining_limit='challenged is a local stage, not a claim that the no-marking implication is finally refuted. Original history answer remains necessary.')]
out=dict(artifact_kind='nonblind_inherited_targeted_correction_recheck',comparator='/root/compare_zevachim_wave2',verdict='ACCEPT_TARGETED_CORRECTIONS_PROVISIONALLY',provenance=dict(fresh_root_reading=False,lane_declared_source_first=True,hidden_context_blindness_verified=False,comparison_blind=False,new_source_only_reading_credit=0),bindings=dict(snapshot=bind(J/'snapshots'/f'{H}.json'),prior_snapshot=bind(J/'snapshots'/f"{oldcomp['snapshot_sha256']}.json"),source=bind(source),runner=bind(R),schema=bind(R.parent/'schema.json'),protocol=bind(R.parent/'PROTOCOL.md'),script=bind(__file__),inherited_originals={n:bind(L/n) for n in names},durable_copies={n:bind(dest/n) for n in names},proposals=[bind(J/'proposals'/f'{ph}.json') for ph in p['proposals']]),scope=dict(inherited_core_refs=initial['core_refs'],inherited_core_segments=27,completed_core_per_layer={k:len(core&v) for k,v in done.items()},targeted_issues=3,targeted_issues_resolved=3,unresolved_targeted_issues=0,active_core_records=len(scoped),active_core_slices=slices(scoped),probability_sample=False,new_independent_sample_segments=0),initial_reading_preserved=initial,prior_comparison_preserved=oldcomp,adjudications=adjudications,corrected_records=[byid[x['id']] for x in prop['records']],continuation_records=[x for x in active if x['id'].startswith(('mk.r013.history','mk.r013.tree_history','mk.r013.interlace','mk.r013.outer','mk.r013.not_far'))],qa=dict(evidence_slices=counts,all_slices_exact=True,readonly_replay_exact=True,proposal_count=len(p['proposals']),stale_active_dependencies=stale,stale_coverage_references=0),limits=['Three inherited reported corrections rechecked; no fresh exhaustive omission pass or whole-tractate review claimed.','Original alternatives and terse5b13–15 uncertainties preserved.','No later snapshot inheritance.','Separate root source-only reader not accessed.'],full_admission=False,new_task_eligibility=False,human_certification=False,production_modified=False)
f=B/'comparisons/moed_katan_graves_correction001.json';assert not f.exists();f.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps(dict(artifact=bind(f),scope=out['scope'],qa=out['qa']),ensure_ascii=False))
