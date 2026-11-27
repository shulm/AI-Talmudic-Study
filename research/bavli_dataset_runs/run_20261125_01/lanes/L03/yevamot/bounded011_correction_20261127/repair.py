import json,hashlib,copy,subprocess
from pathlib import Path
root=Path.cwd();out=Path(__file__).parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');r=lambda f:json.loads(f.read_text(encoding='utf-8-sig'));h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest();review=root/'research/bavli_dataset_runs/run_20261125_01/lanes/L03/yevamot_next20_011_review_20261127/comparison/VERDICT.json';assert h(review)=='6089c437d26e95118654b54a0dd975d20acb09750886f099114315d155df4e4e';v=r(review);cur=r(job/'CURRENT.json')['snapshot_sha256'];assert cur==v['snapshot_sha256'];assert r(job/'OWNER.json')=={'owner':'L03/yevamot','epoch':2};base=out.parent/'bounded011_20261127';initial=r(base/'INITIAL_PROPOSAL.json');pins=r(base/'PINS.json');src=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Nashim/Yevamot/Hebrew/Wikisource Talmud Bavli.json');assert h(src)==pins['source_sha256'];a=r(root/'research/bavli_dataset_runs/ACTIVE_RUN.json');cp=root/a['contract_path'];assert h(cp)==a['contract_sha256'];contract=r(cp)
for f,sha in contract['production_files'].items():assert h(root/f)==sha
state=r(job/'snapshots'/(cur+'.json'));gone={x['supersedes'] for x in state['records'] if 'supersedes'in x};old={x['id']:x for x in state['records'] if x['id'] not in gone};inv=r(job/'source_inventory.json');raw=r(src)['text'];p={k:copy.deepcopy(val) for k,val in initial.items() if k not in ['records','coverage']};p.update(records=[],coverage=[]);changes={}
def ev(i):
 s=inv[i];a,b=s['source_index'];assert raw[a][b]==s['text'];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rev(k):
 if k not in changes:
  x={f:copy.deepcopy(old[k][f]) for f in ['id','layer','evidence','content','origin','uncertainty','links']};x['id']='yvfix011.'+k.removeprefix('yev011.');x['supersedes']=k;changes[k]=x
 return changes[k]
newparts=[]
specs=[('sister_yibbum','Her sister who is her fellow yevamah may undergo chalitzah in the stated paired configuration.','sister_yibbum_option','Her sister who is her fellow yevamah may undergo yibbum in the stated paired configuration.',[214],[214],['Alternative permitted procedure; not a simultaneous duty with the other option']),('context.two_sisters','If Yaakov raped two sisters, the sister-as-fellow-yevamah configuration can be realized.','context.two_sisters_negative','If Yaakov raped two sisters, the reciprocal forbidden/permitted pattern cannot be realized.',[223],[223],['Constructed two-sisters case in the Rava-reported explanation']),('context.two_unrelated','If Yaakov raped two unrelated women, the reciprocal forbidden/permitted pattern can be realized.','context.two_unrelated_negative','If Yaakov raped two unrelated women, the sister-as-fellow-yevamah configuration cannot be realized.',[224],[224],['Constructed two-unrelated-women case in the Rava-reported explanation']),('context.levi_adds','Levi teaches that a mother married to the father and then to the paternal brother does not exempt her co-wife when that brother dies.','context.levi_exemption','Levi teaches that a mother raped by the father and then married to the paternal brother exempts her co-wife when that brother dies.',[231,232],[233],['Levi’s distinct teaching; each marriage history retains its own outcome'])]
for key,t1,newkey,t2,refs1,refs2,conditions in specs:
 oid='yev011.'+key;n=rev(oid);n['content']['proposition']=t1;n['content']['conditions']=list(conditions);n['evidence']=[ev(i) for i in refs1];pos=rev(oid+'.p');pos['content']['conditions']=list(conditions);pos['evidence']=[ev(i) for i in refs1]
 new={f:copy.deepcopy(n[f]) for f in ['id','layer','evidence','content','origin','uncertainty','links']};new['id']='yvfix011.'+newkey;new['content']['proposition']=t2;new['evidence']=[ev(i) for i in refs2];new['uncertainty']+=['Atomic split from preserved composite '+oid+'; source history retained.'];p['records'].append(new)
 np={f:copy.deepcopy(pos[f]) for f in ['id','layer','evidence','content','origin','uncertainty','links']};np['id']=new['id']+'.p';np['evidence']=copy.deepcopy(new['evidence']);np['content']['claim_id']=new['id'];np['links']=[new['id']];p['records'].append(np);newparts.append((oid,new['id'],refs2))
def strings(x):
 if isinstance(x,str):return {x}
 if isinstance(x,list):return set().union(*(strings(y) for y in x)) if x else set()
 if isinstance(x,dict):return strings(list(x.values()))
 return set()
while True:
 more=[k for k,x in old.items() if k not in changes and strings([x['content'],x['links']])&set(changes)]
 if not more:break
 for k in more:rev(k)
mp={k:x['id'] for k,x in changes.items()}
def repl(x):
 if isinstance(x,str):return mp.get(x,x)
 if isinstance(x,list):return [repl(y) for y in x]
 if isinstance(x,dict):return {k:repl(y) for k,y in x.items()}
 return x
for x in changes.values():x['content']=repl(x['content']);x['links']=repl(x['links']);p['records'].append(x)
# Preserve each split branch’s original supported relation.
for oldid,newid,refs in newparts:
 for x in old.values():
  if x['layer']=='edges' and x['content'].get('source_id')==oldid:
   n={f:copy.deepcopy(x[f]) for f in ['id','layer','evidence','content','origin','uncertainty','links']};n['id']='yvfix011.splitedge.'+x['id'];n['content']=repl(n['content']);n['content']['source_id']=newid;n['links']=[newid,n['content']['target_id']];n['evidence']=[ev(i) for i in refs];p['records'].append(n)
active={k:x for k,x in old.items() if k not in changes};active.update({x['id']:x for x in p['records']});pairs={(x['content'].get('source_id'),x['content'].get('target_id')) for x in active.values() if x['layer']=='edges' and x['content']['relation']=='qualification'}
for scope in ['yev011.rav_yehuda_scope','yev011.first_six_excluded']:
 for target in ['yev011.forbidden_one','yev011.forbidden_other',mp['yev011.sister_yibbum'],'yvfix011.sister_yibbum_option']:
  if (scope,target) in pairs:continue
  rid='yvfix011.scope.'+scope.split('.')[-1]+'.'+target.split('.')[-1];p['records'].append(dict(id=rid,layer='edges',evidence=[ev(214),ev(215),ev(216),ev(217)],content=dict(source_id=scope,target_id=target,relation='qualification',explicitness='source_explicit'),origin='source_paraphrase',links=[scope,target],uncertainty=['Rav Yehuda’s interpretation only; Abaye and Rav Safra alternatives remain distinct. Procedural alternatives are permitted options, not combined duties.']))
active.update({x['id']:x for x in p['records']})
for c in state['coverage']:
 n=repl({k:copy.deepcopy(val) for k,val in c.items() if k!='proposal_execution'});extras=[x['id'] for x in p['records'] if x.get('supersedes') is None and (x['layer']==c['layer'] or (c['layer']=='reconciliation' and x['layer'] in ['claims','edges'])) and any(e['segment_id']==c['segment_id'] for e in x['evidence'])];n['record_ids']+=list(dict.fromkeys(k for k in extras if k not in n['record_ids']))
 if n['record_ids']!=c['record_ids']:n['extraction_result']='records_found';n['rationale']+=' Y011 atomic options/history repair and complete branch-specific scope linkage.';p['coverage'].append(n)
for x in active.values():assert not strings([x['content'],x['links']])&set(changes)
for c in p['coverage']:
 for k in c['record_ids']:assert any(e['segment_id']==c['segment_id'] for e in active[k]['evidence'])
(out/'PROPOSAL.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');res=json.loads(subprocess.check_output(['python','research/bavli_production_v1/runner.py','submit','--job-dir',str(job),'--owner','L03/yevamot','--epoch','2','--proposal',str(out/'PROPOSAL.json')]));(out/'SUBMIT.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8');rp=json.loads(subprocess.check_output(['python','research/bavli_production_v1/runner.py','replay','--job-dir',str(job)]));assert rp['replay_pass'] and set(rp['completed_by_layer'].values())=={218};(out/'REPLAY.json').write_text(json.dumps(rp,indent=2)+'\n',encoding='utf-8');exp=job/'exports/bounded011_correction_20261127';ex=json.loads(subprocess.check_output(['python','research/bavli_production_v1/runner.py','export','--job-dir',str(job),'--output',str(exp)]));(out/'EXPORT.json').write_text(json.dumps(ex,indent=2)+'\n',encoding='utf-8');receipt=dict(status='TARGETED_REPAIR_AWAITING_RECHECK',snapshot_sha256=res['snapshot_sha256'],proposal_sha256=h(out/'PROPOSAL.json'),initial_snapshot=cur,review_sha256=h(review),revision_map=mp,split_successors=newparts,coverage_increase=0,completed_by_layer=rp['completed_by_layer'],source_segments=3869,next_ref='Yevamot9b9',open_tails=p['open_tails'],owner=r(job/'OWNER.json'),execution=p['execution'],replay_pass=True,export_directory=str(exp),export_files={str(f.relative_to(exp)):h(f) for f in exp.rglob('*') if f.is_file()},ml_eligible=False,tractate_delivered=False,resume='Independent recheck Y011-01/02; no furthernewproduction before portablecheckpoint.218corecoverage unchanged. Original composite history retained; context uncounted.');(out/'RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(out/'MANIFEST.json').write_text(json.dumps({f.name:h(f) for f in out.iterdir() if f.is_file() and f.name!='MANIFEST.json'},indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(snapshot=res['snapshot_sha256'],proposal=h(out/'PROPOSAL.json'),receipt=h(out/'RECEIPT.json'),revisions=len(mp))))
