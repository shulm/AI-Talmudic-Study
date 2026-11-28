import json,hashlib,subprocess
from pathlib import Path
root=Path.cwd();lane=root/'research/bavli_dataset_runs/run_20261125_01/lanes/L03';out=Path(__file__).parent;b=lane/'tamid/correction_006_20261127';job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');r=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();sha='ca7b86f00e4ee8fc4a5392ec7edee933d7eb3d52ad48b37b4fdc90eb15951c1e';assert h(job/'snapshots'/(sha+'.json'))==sha;state=r(job/'snapshots'/(sha+'.json'));p=r(b/'PROPOSAL.json');assert h(b/'PROPOSAL.json')=='e6d1d574239caf9c187dc2490ddfe2097860bb912fe367744df5fe443d692968';reading=r(out.parent/'SOURCE_READING.json');assert h(out.parent/'SOURCE_READING.json')=='7a90eb3991e76abdd02f5c543d32db5bc8cb9775410f7b567003df132eb66091';raw=r(Path(reading['source']['path']))['text'];assert h(Path(reading['source']['path']))==reading['source']['sha256'];inv=r(job/'source_inventory.json');by={s['id']:s for s in inv};active={x['id']:x for x in state['records'] if x['release_state']!='superseded'};spans=0
for x in p['records']:
 for e in x['evidence']:
  s=by[e['segment_id']];i,j=s['source_index'];assert raw[i][j]==s['text'];assert s['text'][e['start_char']:e['end_char']]==e['quote'];spans+=1
for x in active.values():
 for k in x['links']:assert k in active
 for key in ['claim_id','question_id','source_id','target_id']:
  if x['content'].get(key):assert x['content'][key] in active
for c in state['coverage']:
 for k in c['record_ids']:assert k in active and any(e['segment_id']==c['segment_id'] for e in active[k]['evidence'])
for name,hs in r(b/'MANIFEST.json')['files'].items():assert h(b/name)==hs
ex=r(b/'EXPORT.json');exp=Path('F:/Sefaria_QA/bavli_l03_exports_20261127/tamid_006_corrected')
for name,hs in ex['files'].items():assert h(exp/name)==hs
rp=json.loads(subprocess.check_output(['python','research/bavli_production_v1/runner.py','replay','--job-dir',str(job)]));assert rp['replay_pass'] and rp['snapshot_sha256']==sha;assert set(rp['completed_by_layer'].values())=={90};(out/'REPLAY.json').write_text(json.dumps(rp,indent=2)+'\n',encoding='utf-8')
assert len(p['records'])==8 and all('supersedes' in x for x in p['records']);oldsha='ba1f70d54bbedde5f67dd7abae5927dee2afdfb0dfbe50dea41d556d7c278995';old=r(job/'snapshots'/(oldsha+'.json'));mp={x['supersedes']:x['id'] for x in p['records']};now={x['id']:x for x in state['records']}
for x in old['records']:
 y=now[x['id']];assert all(y[k]==val for k,val in x.items() if k!='release_state');assert y['release_state']==('superseded' if x['id'] in mp else x['release_state'])
assert active['tam006fix.yehuda.a']['content']['surface']=='א"ר יהודה'
for k in ['tam006fix.hot_water','tam006fix.hot_water.p','tam006fix.yehuda.a','tam006fix.u78','tam006fix.frame78']:assert active[k]['uncertainty']
assert {(x['segment_id'],x['layer']) for x in old['coverage']}=={(x['segment_id'],x['layer']) for x in state['coverage']}
v=dict(verdict='ACCEPT_BOUNDED_WITH_LIMITATIONS',reviewer='/root/yevamot',snapshot_sha256=sha,proposal_sha256=h(b/'PROPOSAL.json'),receipt_sha256=h(b/'RECEIPT.json'),producer_manifest_sha256=h(b/'MANIFEST.json'),initial_verdict_sha256=h(out.parent/'comparison/VERDICT.json'),resolved=['T006-01'],findings=[],judgment='Exact raw abbreviation retained; expanded identity explicitly unresolved in claim/position/attribution/frame/utterance and dependent edges revised. Reader initial Rabbi expansion remains preserved but disclaimed in comparison; neither title is now asserted as established.',integrity=dict(revised_rows=8,source_spans=spans,old_bytes_preserved_except_release_state=True,source_offsets_indices=True,live_dependencies=True,coverage_refs=True,coverage_domain_unchanged=True,exact_replay=True,export_files=len(ex['files']),completed_by_layer=rp['completed_by_layer']),exposure='Nonblind exact correction recheck informed by prior frozen findings; no fresh or random cohort',next_ref='Tamid29a8',open_tails=state['open_tails'],ml_eligible=False,tractate_acceptance=False,resume='Bounded repaired version accepted with prior context and identity limitations.117segments per pass remain; coordinator controls subsequent production.')
(out/'VERDICT.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(out/'MANIFEST.json').write_text(json.dumps({f.name:h(f) for f in out.iterdir() if f.is_file() and f.name!='MANIFEST.json'},indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(verdict=h(out/'VERDICT.json'),manifest=h(out/'MANIFEST.json'))))
