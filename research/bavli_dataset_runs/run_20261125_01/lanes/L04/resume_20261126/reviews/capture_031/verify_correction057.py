import sys,json,pathlib,hashlib,importlib.util,re,collections
sys.dont_write_bytecode=True
B=pathlib.Path(__file__).resolve().parent
WT=pathlib.Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study'); L=WT/'research/bavli_dataset_runs/run_20261125_01/lanes/L04/resume_20261126/taanit'; PJ=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_taanit'); OLD=pathlib.Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/delegated101/comparisons')
SH='13b774a3766f6b05e5f389181b3c07eebd62a4f48698a95c300b80f64a6d20b9'; PH='22ca61d6af9eebf97d3118c0e2c99966816797a2a6922a210616cc5b662a9bd0'; BH='e85a80cd47c5b5bc79ec9e5b3346d8b58d5dcf7e53a1555e82862972535819d0'
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def enc(x):return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
def freeze(n,x):
 p=B/n;b=(json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
 if p.exists():assert p.read_bytes()==b
 else:p.write_bytes(b)
 side=p.with_name(p.name+'.sha256');sb=(sha(b)+'  '+p.name+'\n').encode()
 if side.exists():assert side.read_bytes()==sb
 else:side.write_bytes(sb)
 return {'path':str(p),'sha256':sha(b)}
bindings=[]
def pin(p,h):
 assert sha(p.read_bytes())==h,str(p);bindings.append({'path':str(p),'sha256':h})
pin(OLD/'comparison_revision2.json','37b5d1ea044a0d5c57a458456ea9c5193be54396775b54f82a60d37e203a5584');pin(OLD/'v2_verdict_revision2.json','c3e3e7178aa9fc250fa2a2ab847860505ecfcb09e6b8a0858bd4b83428f195dd');pin(OLD/'FINAL_RECEIPT.json','bed62d69ad24da4c59307ddd31075109a508f958f4819b1379d9b72f77a813b7');pin(PJ/'snapshots'/f'{SH}.json',SH);pin(PJ/'snapshots'/f'{BH}.json',BH);pin(PJ/'proposals'/f'{PH}.json',PH)
oldfiles={str(p):sha(p.read_bytes()) for p in OLD.iterdir() if p.is_file()}
cp=read(L/'CHECKPOINT_057.json'); closure=read(L/'REVIEW_CORRECTION_057.json')
for name in ['CHECKPOINT_057.json','REVIEW_CORRECTION_057.json','build_review_correction057.py']:bindings.append({'path':str(L/name),'sha256':sha((L/name).read_bytes())})
assert cp['snapshot_sha256']==SH and cp['proposal_sha256']==PH and closure['proposal_sha256']==PH and closure['base_snapshot_sha256']==BH
contractp=WT/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json';pin(contractp,'6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174');contract=read(contractp)
for path,h in contract['production_files'].items():pin(WT/path,h)
comp=read(OLD/'comparison_revision2.json');ce=comp['commentary_evidence'][0];pin(pathlib.Path(ce['path']),ce['sha256']);assert ce['sha256']=='ad17f9782b9a7640aee553eea79e7c54a3cb1808b0b1138c74bb1d53e8c7b1d7'
readingp=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261127_delegated101/reading.json');pin(readingp,comp['bindings']['reading_sha256'])
spec=importlib.util.spec_from_file_location('frozen_runner',WT/'research/bavli_production_v1/runner.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
meta,segs=r.load(PJ);snap=read(PJ/'snapshots'/f'{SH}.json');base=read(PJ/'snapshots'/f'{BH}.json');proposal=read(PJ/'proposals'/f'{PH}.json');assert snap['proposals']==base['proposals']+[PH]
state=r.empty()
for ph in snap['proposals']:
 raw=(PJ/'proposals'/f'{ph}.json').read_bytes();assert sha(raw)==ph;prev=state['proposals'];state=r.validate_apply(state,json.loads(raw),segs,meta);state['proposals']=prev+[ph]
assert r.encoded(state)==r.encoded(snap) and sha(r.encoded(state))==SH
print('exact prefix replay PASS',len(snap['proposals']),flush=True)
A={x['id']:x for x in snap['records'] if x['release_state']=='valid'}; ALL={x['id']:x for x in snap['records']}; PRE={x['id']:x for x in base['records']};mapping=closure['supersession_map'];assert len(mapping)==11 and len(proposal['records'])==14
for old,new in mapping.items():assert ALL[old]['release_state']=='superseded' and A[new]['supersedes']==old
newids=set(ALL)-set(PRE);assert newids==set(mapping.values())|set(closure['new_record_ids'])
for rid,rec in PRE.items():
 if rid not in mapping:assert ALL[rid]==rec
# All typed references, links, embedded attribution scopes and exact ID tokens must close on active versions.
def strings(x):
 if isinstance(x,str):yield x
 elif isinstance(x,list):
  for y in x:yield from strings(y)
 elif isinstance(x,dict):
  for y in x.values():yield from strings(y)
pat=re.compile(r'(?<![A-Za-z0-9_.:-])(?:'+'|'.join(re.escape(i) for i in sorted(mapping,key=len,reverse=True))+r')(?![A-Za-z0-9_.:-])')
for rec in A.values():
 assert all(x in A for x in rec['links'])
 assert not any(pat.search(t) for t in strings([rec['links'],rec['content']]))
 if rec['layer']=='attributions':
  scope=rec['content']['scope']
  if scope.startswith('ta.'):assert scope.split(';')[0].strip() in A,(rec['id'],scope)
rb=r.report(base,segs);rn=r.report(snap,segs);assert rb['completed_by_layer']==rn['completed_by_layer']=={k:721 for k in r.LAYERS}
assert {(x['segment_id'],x['layer']) for x in base['coverage']}=={(x['segment_id'],x['layer']) for x in snap['coverage']}
last9=[x for x in base['records'] if x['id'].startswith('ta.resume056.')];assert len(last9)==182
sids={e['segment_id'] for x in last9 for e in x['evidence']};assert len(sids)==9
for rec in last9:assert A[rec['id']]==rec and rec['review_state']=='unreviewed' and rec['ml_eligible']==False
beforecov=[x for x in base['coverage'] if x['segment_id'] in sids];aftercov=[x for x in snap['coverage'] if x['segment_id'] in sids];assert beforecov==aftercov and len(aftercov)==72
# Exact export manifest and bytes validation, without regenerating exports.
export=pathlib.Path(cp['export_directory']);manifest=read(export/'manifest.json');pin(export/'manifest.json',cp['manifest_sha256']);assert manifest['snapshot_sha256']==SH
for path,h in manifest['files'].items():assert sha((export/path).read_bytes())==h
# Narrow semantic assertions are tied to manual source/adjudication review, not generic semantic validation.
def C(id):return A[id]['content']
assert 'visible/exposed' in C(mapping['ta.resume016.abahu.rereading'])['proposition']
assert C('ta.resume016.ki.support.t105057')['target_id']==mapping['ta.resume016.abahu.rereading']
assert C(mapping['ta.resume016.mother.warning.a'])['candidates']==['Mother of Resh Lakish’s child']
assert C(mapping['ta.resume016.mother.warning.p'])['holder_candidates']==['Mother of Resh Lakish’s child']
assert 'not independent narrator assertion' in C(mapping['ta.resume016.mother.warning.p'])['local_status']
for id in ['ta.resume016.brothers.proof.a.t105057','ta.resume016.hint.challenge.q.a.t105057']:assert C(id)['candidates']==['Resh Lakish’s child']
assert C('ta.resume016.brothers.proof.u')['textual_voice']=='Resh Lakish’s child' and C('ta.resume016.hint.challenge.q.u')['textual_voice']=='Resh Lakish’s child'
assert C('ta.review105.brothers.scripture')['role']=='quoted_authority' and C('ta.resume016.brothers.proof.p.t105057')['holder_candidates']==[]
assert C('ta.review105.folly.reciter')['scope']=='ta.resume016.folly.verse.u' and C('ta.resume016.folly.verse.a')['role']=='quoted_authority'
assert C('ta.review105.deeds.before.qualifies')=={'source_id':'ta.resume011.deeds.before','target_id':'ta.resume011.mercy.strengthen','relation':'qualification','explicitness':'source_explicit'}
findings=[{'id':'TA101-01','status':'RESOLVED_IN_BOUNDED_WRITER_REVISION','judgment':'Exposed/visible explanatory translation corrects shared fear gloss, preserves original unpointed evidence, names added Rashi edition/hash separately. Active dependents and ki-support endpoint revised. Prior shared error remains recorded.','records':[mapping[x] for x in ['ta.resume016.abahu.rereading','ta.resume016.abahu.rereading.a','ta.resume016.abahu.rereading.p','ta.resume016.abahu.rereading.u','ta.resume016.ki.support']]},{'id':'TA101-02','status':'RESOLVED_IN_BOUNDED_WRITER_REVISION','judgment':'Mother now speaker/voice/holder; explicit character-warning epistemic restriction retained.','records':[mapping[x] for x in ['ta.resume016.mother.warning.a','ta.resume016.mother.warning.p','ta.resume016.mother.warning.u']]},{'id':'TA101-03','status':'RESOLVED_IN_BOUNDED_WRITER_REVISION','judgment':'Child contextual speaker retained for reply/counter-question with 9a:5–6 evidence; separate Genesis quoted authority. Existing child utterance voices were already correct and remain unchanged; original authorship not assigned to reciter.','records':['ta.resume016.brothers.proof.a.t105057','ta.resume016.hint.challenge.q.a.t105057','ta.resume016.brothers.proof.p.t105057','ta.review105.brothers.scripture','ta.resume016.brothers.proof.u','ta.resume016.hint.challenge.q.u']},{'id':'TA101-04','status':'RESOLVED_IN_BOUNDED_WRITER_REVISION','judgment':'New child reciter attribution directly scopes quoted utterance; original Proverbs authority remains.','records':['ta.review105.folly.reciter','ta.resume016.folly.verse.a']},{'id':'TA101-05','status':'RESOLVED_IN_BOUNDED_WRITER_REVISION','judgment':'Source-explicit qualification links prior rectification to mercy remedy; exact כל שכן evidence retained.','records':['ta.review105.deeds.before.qualifies']}]
for f in findings:f['exact_records']=[{'record':A[id],'canonical_record_sha256':sha(enc(A[id]))} for id in f['records']]
assert all(sha(pathlib.Path(p).read_bytes())==h for p,h in oldfiles.items())
result={'artifact_kind':'bounded_correction057_independent_recheck','status':'PASS_FIVE_TARGETED_WRITER_FINDINGS','whole_tractate_acceptance':False,'agent':'/root/ta_compare105','snapshot_sha256':SH,'proposal_sha256':PH,'base_snapshot_sha256':BH,'effective_original_comparison_sha256':comp['revision'] and '37b5d1ea044a0d5c57a458456ea9c5193be54396775b54f82a60d37e203a5584','bindings':bindings,'accepted_prefix_proposals':len(snap['proposals']),'exact_replay':'PASS','active_records':len(A),'total_records':len(ALL),'supersessions':len(mapping),'new_ids':closure['new_record_ids'],'findings':findings,'transitive_links_and_content_scope_closure':'PASS','coverage_by_layer':rn['completed_by_layer'],'new_source_segments':0,'last9':{'refs':[segs[s]['ref'] for s in sorted(sids,key=lambda s:segs[s]['source_index'])],'records':182,'coverage_cells':72,'byte_equivalent_records':True,'unchanged_unreviewed':True,'independent_review_credit':0},'commentary_provenance':ce,'preserved_reader_findings':[x for x in comp['findings'] if x['id'] not in ['TA101-01','TA101-02','TA101-03','TA101-04','TA101-05']],'reader_open_tail_adapter_limitation':'24 source-reading open boundaries absent from open_tails; production-proposal adapter fails without explicit mapping. Reader original, source/schema/graph validation and source-only convention remain as previously recorded; not globally invalidated.','chronology':{'original_comparison':comp['chronology'],'original_revision':comp['revision'],'this_recheck':'Checkpoint/closure/proposal semantics inspected, then full exact historical replay, binding/closure/coverage/export checks before recheck freeze. No claim of pre-inspection replay.','initial_output_path_deviation_preserved':str(OLD),'this_output_directory':str(B)},'scope_limit':'Writer correction057 only; no new source-reading window, no reader repair, no whole-tractate admission or eligibility. Last nine produced segments remain UNREVIEWED.','prior_checkout_files_unchanged':True,'production_mutated':False,'CURRENT_read_or_used':False,'eligibility_change':False,'new_window_credit':0,'export_file_hashes':'PASS'}
print(freeze('correction057_recheck.json',result))
