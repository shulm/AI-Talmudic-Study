import json,hashlib,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
sha=lambda b:hashlib.sha256(b).hexdigest();read=lambda p:json.loads(p.read_text(encoding='utf-8'))
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_nazir');P=OUT.parent.parent/'nazir/correction_001_20261127'
BASE='8bd40f418bf725a9ec2ed2957ca54163ee40bb6cbac9103429b4ca47cd4c4ee1';HEAD='e2896b8c1d248f54ff5e233460c4fd5183f6c31e18302f425f262828d0e4a486';PH='83d804b00c4251ac6e2e002f2702dd52c9909afca7f5935da851875d41b99c2f'
assert sha((P/'PROPOSAL.json').read_bytes())==PH
for h in [BASE,HEAD]:assert sha((J/'snapshots'/f'{h}.json').read_bytes())==h
base=read(J/'snapshots'/f'{BASE}.json');head=read(J/'snapshots'/f'{HEAD}.json');p=read(P/'PROPOSAL.json');job,segs=runner.load(J)
rebuilt=runner.validate_apply(base,p,segs,job);rebuilt['proposals']=base['proposals']+[PH];assert runner.encoded(rebuilt)==runner.encoded(head)
assert runner.report(base,segs)['completed_by_layer']==runner.report(head,segs)['completed_by_layer']=={k:10 for k in runner.LAYERS}
rows={r['id']:r for r in head['records']};active={i:r for i,r in rows.items() if r['release_state']=='valid'}
def strings(v):
 if isinstance(v,str):yield v
 elif isinstance(v,dict):
  for x in v.values():yield from strings(x)
 elif isinstance(v,list):
  for x in v:yield from strings(x)
assert not [(i,s) for i,r in active.items() for s in strings([r['content'],r['links']]) if s in rows and s not in active]
assert len(p['records'])==76 and sum(bool(r.get('supersedes')) for r in p['records'])==58
assert not [r['id'] for r in active.values() if any('Context 3a:11' in u for u in r['uncertainty'])]
assert not [r['id'] for r in active.values() if len(r['uncertainty'])!=len(set(r['uncertainty']))]
original=read(OUT.parent/'VERDICT.json');polluted=original['findings'][0]['producer_ids'];assert len(polluted)==34
assert all(i not in active for i in polluted)
response=read(P/'RECEIPT.json');assert sha((P/'RECEIPT.json').read_bytes())=='a2b215c164bcbdbb1fd0ccdf03857d073e59497fd00fe8a9bc05893a3ec3de91'
ep=Path(response['export_directory']);assert sha((ep/'manifest.json').read_bytes())==response['export_manifest_sha256']
for n,h in response['export_files'].items():assert sha((ep/n).read_bytes())==h
for i in ['lakish_qualifier','yohanan_qualifier','yohanan_scope','lakish_scope']:assert active['nazfix001.context.'+i]['content']['target_id']=='nazfix001.birds_meir'
out={'verdict':'ACCEPT_PARTIAL_WITH_EXCEPTIONS','verification_scope':'Targeted N01/N02 correction and dependent regression only, not new coverage or full tractate acceptance','base_snapshot_sha256':BASE,'snapshot_sha256':HEAD,'proposal_sha256':PH,'original_verdict_sha256':sha((OUT.parent/'VERDICT.json').read_bytes()),'producer_receipt_sha256':sha((P/'RECEIPT.json').read_bytes()),'source_sha256':job['source_sha256'],'findings':[{'id':'N01','disposition':'verified corrected','evidence':'All34 unrelated polluted records superseded; active rows have no old bird-context note or duplicate uncertainty;58 revisions include dependent links.'},{'id':'N02','disposition':'verified corrected','evidence':'Rabbi Meir positive claim/position now explicitly condition interpretation on distinct accounts. Resh Lakish adjacency and sages rejection, Rabbi Yohanan all-reject adjacency and pure-passing-nazir qualification, and3b6 different explicit-wording requirements separately source-anchored with scoped qualification edges. Rabbi Yohanan condition is not imposed on Resh Lakish.'},{'id':'N03','disposition':'retained limitation','evidence':'Shared editorial question/comparable scholar-choice admission deferred.'}],'caveats':['Condition lists include explicitly named alternative branches; they must not be treated as conjunctive shared requirements.','Context explanation records still contain explanatory subclaims; this bounded recheck does not qualify automated argument or scholar-choice use.','No selection of Resh Lakish versus Rabbi Yohanan; no blanket normative claim.'],'checks':{'replay_exact':True,'coverage_unchanged_all8passes':10,'new_records':76,'superseded_records':58,'active_records':len(active),'active_record_references_valid':True,'export_all_bytes':True},'reader_method':'Nonblind changed-record verification; no new independent-source cohort','qualification':{'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0},'tractate_acceptance':False,'next_source':'Nazir2a:11','remaining_per_layer':1289}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));manifest={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(manifest));print(json.dumps({'verdict_sha256':manifest['VERDICT.json'],'manifest_sha256':sha((OUT/'MANIFEST.json').read_bytes())}))
