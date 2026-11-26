"""Read-only checkpoint capture after batch024; no semantic extraction."""
import pathlib,sys,json,hashlib,collections,re
ROOT=pathlib.Path(__file__).resolve().parents[7];sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
JOB=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_taanit');j,ss=runner.load(JOB);state=runner.current(JOB)
expected='32bcf629046f104ec121ba829715249cb950f910fccadc3d989be9ea6592d300';assert runner.read(JOB/'CURRENT.json')['snapshot_sha256']==expected
assert runner.read(JOB/'OWNER.json')==dict(owner='L04/taanit_resume_20261126',epoch=3)
contract=runner.read(ROOT/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json')
for name,digest in contract['production_files'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
export=JOB/'exports/resume_20261126_324_32bcf629';m=runner.read(export/'manifest.json')
for name,digest in m['files'].items():assert hashlib.sha256((export/name).read_bytes()).hexdigest()==digest
base=runner.read(JOB/'snapshots/9936408e656e02d42c8df7d80f8803e7f37cc0565ec53449e03056cad69ab017.json');byid={r['id']:r for r in state['records']}
for r in base['records']:assert byid[r['id']]==r
active=[r for r in state['records'] if r['release_state']=='valid'];ids={r['id'] for r in active};stale=[]
for r in active:
 for link in r['links']:
  if link not in ids:stale.append([r['id'],link])
 if r['layer']=='attributions':
  for old in state['records']:
   if old['release_state']=='superseded' and re.match(re.escape(old['id'])+r'(?=$|[;,:\s])',r['content']['scope']):stale.append([r['id'],r['content']['scope']])
assert not stale,stale
out=runner.read(pathlib.Path(__file__).with_name('CHECKPOINT_020.json'))
out.update(snapshot_sha256=expected,completed_per_layer=m['completed_by_layer'],next_reference='Taanit 12b:9',last_completed_reference='Taanit 12b:8',remaining_per_layer=571,new_segments=121,new_records=len(state['records'])-len(base['records']),active_records=len(active),preserved_total_records=len(state['records']),active_records_by_layer=dict(collections.Counter(r['layer'] for r in active)),open_tails=state['open_tails'],export_directory=str(export),manifest_sha256=hashlib.sha256((export/'manifest.json').read_bytes()).hexdigest(),proposal_chain=state['proposals'],all_baseline_records_byte_equivalent=True,independent_review_of_new_source=False,producer_active_after_handoff=False,model_id=None,context_handoff=True)
out['attempt_notes']+=['Batch024 pre-staging draft used unsupported unresolved attribution role, corrected to speaker with two candidates. A duplicate local edge ID was detected and renamed before staging; no rejected proposal was accepted.']
out['answer_set_policy']='Read coordinator additive policy 001. New batch022–024 question records explicitly limit partial to their represented local answers, without choice-task eligibility. Earlier questions remain unreviewed; no bulk relabelling.'
out['prior_correction_recheck']=dict(path='F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261126_resume/taanit_frozen_comparison/correction013_independent_recheck.json',sha256='b54b1d57d15b6c63d48c1e66a0f378545d0ea82c8eb9698c4df648cc6dc88eaf',scope='Correction013 only; no acceptance of new source rows inferred.')
out['unresolved_cases_examples']=['9a:2–4 unnamed dialogue turns retain unresolved personal allocation.','9b:6 printed רבי יוסי (בר) חנינא preserved without silent normalization.','10b:3–4 compact תלמיד עושה syntax retained.','11a:13 printed parenthetical judgment wording remains uncertain.','11b:2 printed חסיד/[צ"ל חסד] correction retained.','12a:8 Hiyya/Shimon Berabbi ייסר/יאסר allocations unresolved.','12b:5–6 Shmuel versions remain separate, not retraction.']
runner.immutable(pathlib.Path(__file__).with_name('CHECKPOINT_024.json'),runner.encoded(out));print(json.dumps({k:out[k] for k in ['snapshot_sha256','active_records','preserved_total_records','new_records','manifest_sha256']},indent=2))
