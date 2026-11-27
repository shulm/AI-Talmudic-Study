import json,hashlib,copy,subprocess
from pathlib import Path
root=Path.cwd();out=Path(__file__).parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin');r=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();review=root/'research/bavli_dataset_runs/run_20261125_01/lanes/L03/kiddushin_next20_review_20261127/comparison/VERDICT.json';assert h(review)=='726cc37003c0f0bd3d8ff8bfeb9f1f8c444d4e62a0e3b26ee90f30d8d7841ae9';v=r(review);cur=r(job/'CURRENT.json')['snapshot_sha256'];assert cur==v['snapshot_sha256'];assert r(job/'OWNER.json')=={'owner':'/root/lead_l01_l03','epoch':1};base=out.parent/'bounded_002_20261127';initial=r(base/'INITIAL_PROPOSAL.json');pins=r(base/'PINS.json')['pins'];assert h(Path(pins['source_path']))==pins['source_sha256'];assert h(Path(pins['source_schema_path']))==pins['source_schema_sha256'];a=r(root/'research/bavli_dataset_runs/ACTIVE_RUN.json');cp=root/a['contract_path'];assert h(cp)==a['contract_sha256'];contract=r(cp)
for f,sha in contract['production_files'].items():assert h(root/f)==sha
state=r(job/'snapshots'/(cur+'.json'));gone={x['supersedes'] for x in state['records'] if 'supersedes'in x};rows={x['id']:x for x in state['records'] if x['id'] not in gone};inv=r(job/'source_inventory.json');raw=r(Path(pins['source_path']))['text'];p={k:copy.deepcopy(val) for k,val in initial.items() if k not in ['records','coverage']};p.update(records=[],coverage=[]);changes={}
def rev(k):
 if k not in changes:
  x={f:copy.deepcopy(rows[k][f]) for f in ['id','layer','evidence','content','origin','uncertainty','links']};x['id']='kidfix002.'+k.removeprefix('kid002.');x['supersedes']=k;changes[k]=x
 return changes[k]
def subst(x):
 if isinstance(x,str):return x.replace('Rabbi Eliezer','ר״א (unresolved printed abbreviation)')
 if isinstance(x,list):return [subst(y) for y in x]
 if isinstance(x,dict):return {k:subst(y) for k,y in x.items()}
 return x
for k,x in rows.items():
 if 'Rabbi Eliezer' in json.dumps([x['content'],x['uncertainty']],ensure_ascii=False):
  n=rev(k);n['content']=subst(n['content']);n['uncertainty']=subst(n['uncertainty'])+['Exact source prints ר״א; no categorical expansion is supported by this pinned evidence.']
n=rev('kid002.eliezer');n['content'].update(surface='ר״א אומר',candidates=['ר״א'],scope='Printed abbreviation of the authority saying etrog is like a tree לכל דבר; expansion unresolved')
local=['intercourse_way','money_deed_wording','means_intercourse','etrog_ending_wording']
for k in local:
 n=rev('kid002.'+k+'.p');n['content']['local_status']='Earlier local explanation of wording; final אלא criterion at3a:3 replaces its sufficiency as the general account, without rejecting the underlying substantive statement.'
for k in ['ways_criterion','things_criterion']:
 n=rev('kid002.'+k+'.p');n['content']['local_status']='Final general wording account introduced by אלא at3a:3; supersedes earlier local accounts as sufficient general explanation.'
n=rev('kid002.man_seeks.p');n['content']['local_status']='Rabbi Shimon alternative wording explanation introduced by ואי בעית אימא at2b:13; later final אלא criterion supplies general account. Courtship statement/analogy is not rejected.';n['content']['conditions']=['Alternative explanatory stage at2b:13, not final general דרכים/דברים criterion']
# Transitive closure and exact replacement of all dependent links/content/coverage.
def strings(x):
 if isinstance(x,str):return {x}
 if isinstance(x,list):return set().union(*(strings(y) for y in x)) if x else set()
 if isinstance(x,dict):return strings(list(x.values()))
 return set()
while True:
 more=[k for k,x in rows.items() if k not in changes and strings([x['content'],x['links']])&set(changes)]
 if not more:break
 for k in more:rev(k)
mp={k:x['id'] for k,x in changes.items()}
def replace(x):
 if isinstance(x,str):return mp.get(x,x)
 if isinstance(x,list):return [replace(y) for y in x]
 if isinstance(x,dict):return {k:replace(y) for k,y in x.items()}
 return x
for x in changes.values():x['content']=replace(x['content']);x['links']=replace(x['links']);p['records'].append(x)
def ev(i):
 s=inv[i];a,b=s['source_index'];assert raw[a][b]==s['text'];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
for k,i in [('intercourse_way',14),('money_deed_wording',15),('means_intercourse',16),('etrog_ending_wording',19),('etrog_water',20),('etrog_tithe',20),('man_seeks',17)]:
 target=mp.get('kid002.'+k,'kid002.'+k);p['records'].append(dict(id='kidfix002.final_scope.'+k,layer='edges',evidence=[ev(i),ev(22)],content=dict(source_id='kid002.ways_criterion',target_id=target,relation='qualification',explicitness='source_explicit'),origin='source_paraphrase',links=['kid002.ways_criterion',target],uncertainty=['Qualification applies only to this statement serving as a sufficient general explanation of דרכים. The final אלא account replaces that explanatory sufficiency; substantive law, observation or analogy is not declared false.']+(['Rabbi Shimon remains an alternative explanation at its earlier source stage.'] if k=='man_seeks' else [])))
for c in state['coverage']:
 n=replace({k:copy.deepcopy(val) for k,val in c.items() if k!='proposal_execution'});extra=[x['id'] for x in p['records'] if x['id'].startswith('kidfix002.final_scope.') and x['layer']==c['layer'] and any(e['segment_id']==c['segment_id'] for e in x['evidence'])]
 if extra:n['record_ids']+=extra;n['extraction_result']='records_found'
 if n['record_ids']!=c['record_ids']:n['rationale']+=' Immutable K01/K02 repair: printed identity and final versus earlier explanatory scope preserved.';p['coverage'].append(n)
combined={k:x for k,x in rows.items() if k not in changes};combined.update({x['id']:x for x in p['records']})
for x in combined.values():assert not strings([x['content'],x['links']])&set(changes)
assert all('Rabbi Eliezer' not in json.dumps([x['content'],x['uncertainty']],ensure_ascii=False) for x in combined.values())
(out/'PROPOSAL.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');result=json.loads(subprocess.check_output(['python','research/bavli_production_v1/runner.py','submit','--job-dir',str(job),'--owner','/root/lead_l01_l03','--epoch','1','--proposal',str(out/'PROPOSAL.json')]));(out/'SUBMIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
replay=json.loads(subprocess.check_output(['python','research/bavli_production_v1/runner.py','replay','--job-dir',str(job)]));assert replay['replay_pass'] and set(replay['completed_by_layer'].values())=={30};(out/'REPLAY.json').write_text(json.dumps(replay,indent=2)+'\n',encoding='utf-8');exp=job/'exports/correction_002_20261127';ex=json.loads(subprocess.check_output(['python','research/bavli_production_v1/runner.py','export','--job-dir',str(job),'--output',str(exp)]));(out/'EXPORT.json').write_text(json.dumps(ex,indent=2)+'\n',encoding='utf-8')
receipt=dict(status='K01_K02_REPAIR_AWAITING_RECHECK',snapshot_sha256=result['snapshot_sha256'],proposal_sha256=h(out/'PROPOSAL.json'),review_sha256=h(review),initial_snapshot=cur,revision_map=mp,new_scope_edges=7,coverage_increase=0,completed_by_layer=replay['completed_by_layer'],source_segments=2406,next_ref='Kiddushin3b:4',open_tails=[],source_sha256=pins['source_sha256'],owner=r(job/'OWNER.json'),execution=p['execution'],replay_pass=True,export_directory=str(exp),export_files={str(f.relative_to(exp)):h(f) for f in exp.rglob('*') if f.is_file()},ml_eligible=False,tractate_delivered=False,resume='Independent recheck K01 identity and K02 argument scope at this exact snapshot; earlier source facts remain intact. No more production here until instruction;30core coverage unchanged.')
(out/'RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(out/'MANIFEST.json').write_text(json.dumps({f.name:h(f) for f in out.iterdir() if f.is_file() and f.name!='MANIFEST.json'},indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(snapshot=result['snapshot_sha256'],proposal=h(out/'PROPOSAL.json'),receipt=h(out/'RECEIPT.json'),revisions=len(mp))))
