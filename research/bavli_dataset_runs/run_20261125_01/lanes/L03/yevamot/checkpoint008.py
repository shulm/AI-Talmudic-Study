import json, hashlib
from pathlib import Path
root=Path.cwd(); out=Path(__file__).parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot'); exp=job/'exports/checkpoint008'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
cur=read(job/'CURRENT.json')['snapshot_sha256'];state=read(job/'snapshots'/f'{cur}.json'); replay=read(out/'replay008.json'); manifest=read(exp/'manifest.json')
assert replay['replay_pass'] and replay['snapshot_sha256']==cur
for f,h in manifest['files'].items():assert sha(exp/f)==h,(f,h)
contract_path=root/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'; contract=read(contract_path)
assert sha(contract_path)=='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174'
for f,h in contract['production_files'].items():assert sha(root/f)==h,f
src=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Nashim/Yevamot/Hebrew/Wikisource Talmud Bavli.json');ss=Path('F:/Sefaria-Export-master/schemas/Yevamot.json')
assert sha(src)=='e3f2ddea9c75119de9dd032ca9cf91108d55c332ca8eeab4fb0997ed1eca5a07'
assert sha(ss)=='e3dd6cc777b473fbe6e45be722dd0294885429ea29215fb776cfb3e09a948e23'
receipt=dict(status='PARTIAL_REQUIRED_WORK_REMAINS',run_id='run_20261125_01',lane='L03',job_id='bavli_yevamot',owner=read(job/'OWNER.json'),source_path=str(src),source_sha256=sha(src),source_schema_path=str(ss),source_schema_sha256=sha(ss),contract_sha256=sha(contract_path),production_git_commit=contract['production_git_commit'],schema_sha256=contract['schema_sha256'],protocol_sha256=contract['annotation_protocol_sha256'],source_segments=3869,completed_source_scope={'first':'Yevamot 2a:1','last':'Yevamot 8a:8','segments':158},completed_by_layer=replay['completed_by_layer'],remaining_by_layer={k:3869-v for k,v in replay['completed_by_layer'].items()},next_unprocessed_by_layer=replay['next_unprocessed_by_layer'],semantic_records=1064,snapshot_sha256=cur,snapshot_path=str(job/'snapshots'/f'{cur}.json'),proposal_chain=state['proposals'],open_tails=state['open_tails'],export_directory=str(exp),export_manifest_sha256=sha(exp/'manifest.json'),export_files=manifest['files'],replay_pass=True,independent_review={'status':'NOT_COMPLETED','source_first_packets_received':False,'reviewed_segments':0,'note':'Lead-managed separate source-first reviewer; producer annotations do not establish review.'},task_eligibility={'ml_eligible':False,'evaluation_or_choice_qualification':'none'},tractate_delivered=False,git={'committed':False,'pushed':False,'merged':False},new_metered_api_calls=0,execution={'route':'interactive_agent','agent_id':'/root/yevamot','model_id':None},stop_reason='Lead requested exact session checkpoint after current bounded batch; no background execution claimed.')
(out/'CHECKPOINT008.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
proposals={p.name:sha(p) for p in sorted(out.glob('proposal*.json'))}
(out/'PROPOSALS_MANIFEST.json').write_text(json.dumps(proposals,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'snapshot':cur,'manifest_sha256':sha(exp/'manifest.json'),'receipt_sha256':sha(out/'CHECKPOINT008.json'),'proposal_count':len(proposals),'open_tails':state['open_tails'],'next':replay['next_unprocessed_by_layer'],'semantic_records':replay['semantic_records']},indent=2))
