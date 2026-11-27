import json,hashlib,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
sha=lambda b:hashlib.sha256(b).hexdigest();read=lambda p:json.loads(p.read_text(encoding='utf-8'))
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');P=OUT.parent.parent/'tamid/review_correction_20261127'
BASE='2c734e3e48f6686ab6cece6bd52141c56d7b5c3e5dbe71a485262c5642a83c3b';HEAD='82d494b4dd71ba8c26cd774abe128eabab1dc84cbdd79561bba5e92b5543dcc2';PH='309a1a796445af9cb6e10fc9e5a0fec640afa5061da244005ffc211c0f7a21c0'
assert sha((P/'VALIDATED_PROPOSAL.json').read_bytes())==PH
for h in [BASE,HEAD]:assert sha((J/'snapshots'/f'{h}.json').read_bytes())==h
base=read(J/'snapshots'/f'{BASE}.json');head=read(J/'snapshots'/f'{HEAD}.json');p=read(P/'VALIDATED_PROPOSAL.json');job,segs=runner.load(J)
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
assert len(p['records'])==23 and sum(bool(r.get('supersedes')) for r in p['records'])==7
response=read(P/'RESPONSE.json');assert sha((P/'RESPONSE.json').read_bytes())=='33b87c6977f345cba94308b30da9159a0a28445bfe6c03aee6cb958033c61d4a'
ep=Path(response['export_path']);assert sha((ep/'manifest.json').read_bytes())==response['export_manifest_sha256']
for n,h in read(ep/'manifest.json')['files'].items():assert sha((ep/n).read_bytes())==h
for k,h in [('nonmixed','anonymous Gemara'),('stiff','Rav Ashi'),('felt','Rav Huna son of Rav Yehoshua')]:assert active['tam001.r1.'+k+'.p']['content']['holder_candidates']==[h]
assert active['tam001.r1.count_inference']['origin']=='editorial_inference'
out={'verdict':'ACCEPT_PARTIAL_WITH_EXCEPTIONS','verification_scope':'Targeted T01/T02 correction and dependency regression only; original10core comparison remains preserved','base_snapshot_sha256':BASE,'snapshot_sha256':HEAD,'proposal_sha256':PH,'original_verdict_sha256':sha((OUT.parent/'VERDICT.json').read_bytes()),'response_sha256':sha((P/'RESPONSE.json').read_bytes()),'source_sha256':job['source_sha256'],'findings':[{'id':'T01','disposition':'verified corrected','evidence':'27b4 anonymous nonmixed, Rav Ashi stiffness and Rav Huna son of Rav Yehoshua felt precedent now separate claims/holders; support/qualification and original transmission retained.'},{'id':'T02','disposition':'verified corrected','evidence':'26a7 verse separation, Aaron one, sons two distinct; numerical sum clearly editorial with two premises and total-three support; parent argument remains open.'},{'id':'T03','disposition':'retained limitation','evidence':'Benefit QA/argument outcome not qualified.'},{'id':'T04','disposition':'retained limitation','evidence':'No comparable lottery shared-question admission.'}],'checks':{'replay_exact':True,'coverage_unchanged_all8passes':10,'new_records':23,'superseded_records':7,'active_record_references_valid':True,'export_all_bytes':True,'raw_indices_preserved':True},'reader_method':'Nonblind changed-record verification, no new source-first cohort','qualification':{'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0},'tractate_acceptance':False,'next_source':'Tamid26a:8','remaining_per_layer':197}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));manifest={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(manifest));print(json.dumps({'verdict_sha256':manifest['VERDICT.json'],'manifest_sha256':sha((OUT/'MANIFEST.json').read_bytes())}))
