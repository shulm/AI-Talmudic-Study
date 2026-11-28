import copy,json,sys
from pathlib import Path
sys.path.insert(0,'research/bavli_production_v1');import runner
out=Path(__file__).resolve().parent;lane=out.parents[1];prod=lane/'kiddushin/bounded_004_20261127';job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin');sha=lambda p:runner.sha(p.read_bytes())
reading=runner.read(out.parent/'SOURCE_READING.json');assert sha(out.parent/'SOURCE_READING.json')=='93d000027af132f2679a19ef1a9ff5e16c4de81774f89ecd5f8b5bf551930546'
receipt=runner.read(prod/'RECEIPT.json');version='a1a0d044030d74c61d84376a6feb004f2dec4a8fb36d6c246fd326013859742b';raw=(job/'snapshots'/f'{version}.json').read_bytes();assert runner.sha(raw)==version;state=json.loads(raw)
j,src=runner.load(job);assert j['source_sha256']==reading['source_sha256'] and len(src)==2406
proposal=runner.read(prod/'INITIAL_PROPOSAL.json');assert sha(prod/'INITIAL_PROPOSAL.json')==receipt['proposal_sha256'];base=runner.read(job/'snapshots'/f"{receipt['parent_snapshot']}.json")
now={r['id']:r for r in state['records']};live={k:r for k,r in now.items() if r['release_state']=='valid'};revisions={r['supersedes'] for r in proposal['records'] if r.get('supersedes')};assert len(proposal['records'])==166 and len(revisions)==20
for r in base['records']:
 expected=copy.deepcopy(r)
 if r['id'] in revisions:expected['release_state']='superseded'
 assert now[r['id']]==expected
spans=0
for r in proposal['records']:
 for ev in r['evidence']:
  assert src[ev['segment_id']]['text'][ev['start_char']:ev['end_char']]==ev['quote'];spans+=1
for r in live.values():
 c=r['content'];deps=list(r['links'])
 if r['layer']=='positions':deps+=[c['claim_id']]+([c['question_id']] if c['question_id'] else [])
 if r['layer']=='edges':deps+=[c['source_id'],c['target_id']]
 assert all(x in live for x in deps)
for c in state['coverage']:assert all(x in live for x in c['record_ids'])
replayed=runner.empty()
for h in state['proposals']:
 b=(job/'proposals'/f'{h}.json').read_bytes();assert runner.sha(b)==h;prev=replayed['proposals'];replayed=runner.validate_apply(replayed,json.loads(b),src,j);replayed['proposals']=prev+[h]
assert runner.encoded(replayed)==raw;rp=runner.report(state,src);assert set(rp['completed_by_layer'].values())=={70}
ex=runner.read(prod/'EXPORT.json');assert ex['snapshot_sha256']==version
for f,h in ex['files'].items():assert sha(Path(receipt['export_directory'])/f)==h
groups=[['kid003.context.rabbah','kid003.rabbah_answer'],['kid003.context.resident','kid003.context.hired'],['kid004.resident_only_q','kid003.context.shorter_af'],['kid004.revised.kid003.context.resident_misread','kid004.permanent_eats_hyp','kid004.permanent_not_eat','kid004.revised.kid003.context.hired_clarifies'],['kid003.context.abaye_objection','kid004.revised.kid003.context.two_bodies','kid004.write_af'],['kid003.context.one_body','kid003.context.abaye_objection'],['kid003.context.aylonit_release'],['kid004.revised.kid003.context.aylonit_no_exit_hyp'],['kid003.context.mar_objection','kid004.revised.kid003.context.signs','kid004.signs_master','kid003.context.maturity_father','kid003.context.maturity_af'],['kid003.context.aylonit_sale','kid004.revised.kid003.context.no_sale_hyp','kid004.no_signs_no_sale'],['kid003.context.aylonit_sale','kid004.revised.kid003.sale_corrects'],['kid003.context.why_not_write_af','kid004.no_alternative_af','kid004.revised.kid003.context.prefer_other'],['kid004.money_take','kid004.taking_money','kid004.take_source'],['kid004.money_af_q','kid004.maid_no_intercourse','kid004.maid_money','kid004.wife_intercourse_premise','kid004.wife_money_af'],['kid004.yevamah_intercourse','kid004.yevamah_no_money','kid004.yevamah_no_deed','kid004.wife_deed'],['kid004.money_verse_need','kid004.money_initial_objection','kid004.rav_ashi'],['kid004.money_from_where','kid004.maid_money_exit','kid004.wife_no_money_exit','kid004.exit_refutes'],['kid004.both_verses','kid004.daughter_money_hyp','kid004.father_money_from_exit'],['kid004.female_transfer_hyp','kid004.man_takes','kid004.not_woman_takes'],['kid004.intercourse_verse','kid004.intercourse_af_q','kid004.wife_intercourse_af','kid004.context.bond_refutation']]
assert len(groups)==20;mapping=[]
for n,(f,ids) in enumerate(zip(reading['findings'][:20],groups),1):
 assert all(x in live for x in ids);mapping.append(dict(reader_id=f['id'],producer_ids=ids,disposition='targeted_relation_repair' if n==11 else 'represented',finding_id='K004-01' if n==11 else None))
checks=dict(proposal_rows=166,proposal_spans=spans,superseded_rows=20,source_inventory=2406,all_prior_bytes_preserved_except_release_state=True,live_dependencies_valid=True,exact_replay=True,export_files=len(ex['files']),coverage_each_layer=70)
verdict=dict(verdict='REWORK_TARGETED',reader='/root',comparator='/root',producer='/root/yevamot',snapshot_sha256=version,proposal_sha256=receipt['proposal_sha256'],source_reading_sha256=sha(out.parent/'SOURCE_READING.json'),source_first_core_findings=20,core_findings_represented_without_repair=19,core_findings_needing_targeted_repair=1,mapping=mapping,required_repairs=[runner.read(out/'FINDING.json')],checks=checks,context_scope='Relevant intercourse-proof continuation4b11–13 represented and uncounted. Later document/chuppah/mixed-action units inspected as context/boundaries; no requirement to annotate their complete future cores in this batch.',limitations=['Root previously reviewed003 context now promoted in004; exposure disclosed, not fresh blind cohort.','Positive signs-valid-sale branch is part of proposed restriction, not an actually refuted validity rule; correction endpoint must target negative no-signs branch.','No final practical halakhic conclusion, whole-tractate completion, or ML eligibility.'],next_ref=rp['next_unprocessed_by_layer']['claims'],open_tails=state['open_tails'],tractate_delivered=False,ml_eligible=False)
for name,value in [('CHECKS.json',checks),('REPLAY.json',dict(snapshot_sha256=version,replay_pass=True,**rp)),('VERDICT.json',verdict)]:runner.immutable(out/name,runner.encoded(value))
runner.immutable(out/'MANIFEST.json',runner.encoded(dict(files={p.name:sha(p) for p in out.iterdir() if p.is_file() and p.name!='MANIFEST.json'})))
print(json.dumps(dict(verdict=sha(out/'VERDICT.json'),manifest=sha(out/'MANIFEST.json'),checks=checks)))
