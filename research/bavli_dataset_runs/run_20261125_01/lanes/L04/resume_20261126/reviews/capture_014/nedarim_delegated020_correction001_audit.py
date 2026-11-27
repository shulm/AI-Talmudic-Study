import json,hashlib,sys,importlib.util,re
from pathlib import Path
from collections import Counter
sys.dont_write_bytecode=True
O=Path(__file__).parent;T=O.parents[1]/'bavli_nedarim';C=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
P=Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/lanes/L04/resume_20261126/nedarim')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text(encoding='utf8'))
def bind(p):return dict(path=str(p),sha256=sha(p))
snap=T/'snapshots/26acf7ff70ba33f249b8e3f957edac6a932ce1d32c7e84996ad3b239e74bab01.json';prop=T/'proposals/60bb54136fc328b83eea0b8cad77d934ad47e94696c29a85f80719d195cfb0ac.json'
base=T/'snapshots/5e76010e8585d01a7ede4e1c6924d085ffad622bd6e9bac0ecfd6200861e9b1b.json'
for p in [snap,prop,base]:assert sha(p)==p.stem
s=read(snap);q=read(prop);b=read(base);assert s['proposals']==b['proposals']+[prop.stem]
orig=O/'nedarim_delegated020_exact_version.json';verdict=O/'nedarim_delegated020_v2_verdict.json';adj=O/'nedarim_delegated020_additive_adjudication.json'
for p in [orig,verdict,adj]:assert sha(p)==Path(str(p)+'.sha256').read_text().split()[0]
prior=read(orig)
for z in [prior['bindings']['reading'],prior['bindings']['snapshot'],prior['bindings']['runner'],prior['bindings']['schema'],prior['bindings']['protocol']]+prior['bindings']['common']:assert sha(z['path'])==z['sha256']
inv=read(T/'source_inventory.json');bi={x['id']:x for x in inv};src=read(prior['bindings']['source']['path'])
for x in inv:assert src['text'][x['source_index'][0]][x['source_index'][1]]==x['text']
slice_count=0;duplicate_evidence=[]
for x in s['records']:
 seen=set()
 for e in x['evidence']:
  assert bi[e['segment_id']]['text'][e['start_char']:e['end_char']]==e['quote'];slice_count+=1
  key=(e['segment_id'],e['start_char'],e['end_char'])
  if key in seen and x['id'] in {z['id'] for z in q['records']}:duplicate_evidence.append(dict(record_id=x['id'],span=key))
  seen.add(key)
runner=Path(prior['bindings']['runner']['path']);sys.path.insert(0,str(runner.parent));spec=importlib.util.spec_from_file_location('nd_fix020_runner',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);job,segs=m.load(T);state=m.empty()
for h in s['proposals']:
 p=T/'proposals'/f'{h}.json';assert sha(p)==h;old=state['proposals'];state=m.validate_apply(state,read(p),segs,job);state['proposals']=old+[h]
assert m.encoded(state)==m.encoded(s)
active={x['id']:x for x in s['records'] if x['release_state']=='valid'};allr={x['id']:x for x in s['records']};oldr={x['id']:x for x in b['records']}
for x in active.values():
 for z in x.get('links',[]):assert z in active,(x['id'],z)
 for k in ['source_id','target_id','claim_id','question_id']:
  z=x['content'].get(k)
  if z:assert z in active,(x['id'],k,z)
 scope=x['content'].get('scope','')
 for z in re.findall(r'\bnd\.[A-Za-z0-9_.:-]+',scope):assert z.rstrip('.,:;') in active,(x['id'],z)
for row in s['coverage']:
 for z in row['record_ids']:assert z in active,(row['segment_id'],z)
sup={x['supersedes']:x['id'] for x in q['records'] if x.get('supersedes')};assert len(sup)==5
for id,x in oldr.items():
 y=allr[id]
 if id in sup:
  assert x['release_state']=='valid' and y['release_state']=='superseded'
  assert {k:v for k,v in x.items() if k!='release_state'}=={k:v for k,v in y.items() if k!='release_state'}
 else:assert x==y
for id in ['nd.r010.amend.q.unc013','nd.r005.aboth.answer','nd.r005.rboth.answer','nd.r005.map.c']:assert active[id]==oldr[id]
coverage=lambda st:{l:len({x['segment_id'] for x in st['coverage'] if x['layer']==l and x['extraction_state']=='completed'}) for l in {x['layer'] for x in st['coverage']}}
assert coverage(b)==coverage(s) and set(coverage(s).values())=={1062}
assert active['nd.r010.stronger.a.fix020']['content']['candidates']==['רבי שמעון'];assert active['nd.r010.stronger.p.fix020']['content']['holder_candidates']==['רבי שמעון']
assert active['nd.fix020.verse.answer']['content']==dict(explicitness='source_explicit',relation='answer',source_id='nd.fix020.verse.c',target_id='nd.fix020.derivation.q')
assert active['nd.fix020.amend.correction']['content']==dict(explicitness='source_explicit',relation='correction',source_id='nd.r010.amend.q.unc013',target_id='nd.r010.olist.c')
assert active['nd.fix020.lemma.quotation']['content']['target_id']=='nd.r010.oath.c';assert active['nd.fix020.bare.qualification']['content']['target_id']=='nd.fix020.lemma.c'
refs=['Nedarim 10a:11','Nedarim 10a:14','Nedarim 10b:1','Nedarim 10b:2','Nedarim 10b:3','Nedarim 10b:8','Nedarim 10b:9','Nedarim 10b:10','Nedarim 10b:11']
receipt=dict(artifact_kind='immutable_independent_targeted_correction001_receipt',execution=dict(agent_id='/root/nedarim_compare020',role='NONBLIND independent comparator, original reviewer',route='interactive_agent',model_id=None),verdict='FOUR_OPERATIVE_CORRECTIONS_VERIFIED_WITH_LIMITATIONS',bindings=dict(corrected_snapshot=bind(snap),repair_proposal=bind(prop),immediate_baseline=bind(base),original_comparison=bind(orig),original_verdict=bind(verdict),mandatory_adjudication=bind(adj),runner=bind(runner),audit_script=bind(__file__),producer_prevalidation=bind(P/'REPAIR_DELEGATED020_065_PREVALIDATION.json'),producer_closure=bind(P/'REPAIR_DELEGATED020_065_CLOSURE.json'),original_source=prior['bindings']['source'],frozen_reading=prior['bindings']['reading']),source_refs_checked=refs,source_evidence=[dict(ref=x['ref'],start_char=0,end_char=len(x['text']),quote=x['text']) for x in inv if x['ref'] in refs],issue_results=[dict(id='ND020-P01',result='corrected',reason='Named baraita introducer10a:14 governs10b:1 and uninterrupted a-fortiori continuation10b:2; five supersessions preserve quoted authority and all dependent typed pointers.'),dict(id='ND020-P02',result='corrected',reason='Explicit מניין question with cited תלמוד לומר answer is typed, attributed to quoted Rabbi Shimon; partial answer inventory does not certify exhaustive alternatives.'),dict(id='ND020-P03',result='corrected',reason='Correction edge changes initial list stage to revised question while existing unresolved question is byte-semantically unchanged; no Shmuel answer inferred.'),dict(id='ND020-P05',result='corrected',reason='Repeated10b:11 lemma has distinct claim/utterance and quotation to10a:11; local bare-expression qualification points to repeated occurrence.'),dict(id='ND020-P04',result='withdrawn_unchanged',reason='Mandatory prior adjudication remains operative; no duplicate challenge edges required.')],replay=dict(exact_prefix_match=True,proposal_count=len(s['proposals']),source_inventory_segments=len(inv),exact_snapshot_evidence_slices=slice_count,no_CURRENT_used=True),closure=dict(active_records=len(active),all_active_links_content_ids_embedded_scopes_closed=True,coverage_references_closed=True,five_supersessions=sup,previous_records_preserved_except_release_states=True,coverage_before=coverage(b),coverage_after=coverage(s)),nonblocking_observations=[dict(kind='duplicate_evidence_entries',details=duplicate_evidence,note='Three derivation records repeat identical10a:14 introducer evidence three times. Valid exact slices, no additional source credit; deduplicate in a future additive cleanup, not a semantic blocker.'),dict(kind='inherited_coverage_rationale',note='Question coverage rationale retains earlier no separate additional object found wording followed by explicit repair explanation and added IDs. Current IDs/result are correct; clean stale prose in a future additive revision.')],scope_limits=['Four fixes only; original30-core review denominator unchanged.','Immediate baseline5e76010e is newer than originald34c7be2; replay integrity does not certify intervening semantic content.','All original reader errors, unresolved source ambiguity and task restrictions remain.','No new core credit, no full tractate admission, no task eligibility, no automatic acceptance of later snapshots.'],new_core_credit=0,task_eligibility=False,whole_snapshot_semantic_admission=False,producer_modified=False)
out=O/'nedarim_delegated020_correction001_receipt.json';assert not out.exists();out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
for p in [out,Path(__file__)]:Path(str(p)+'.sha256').write_text(sha(p)+'  '+p.name+'\n',encoding='ascii')
print(json.dumps(dict(receipt=bind(out),audit=bind(__file__),replay=receipt['replay'],closure=receipt['closure']),ensure_ascii=False))
