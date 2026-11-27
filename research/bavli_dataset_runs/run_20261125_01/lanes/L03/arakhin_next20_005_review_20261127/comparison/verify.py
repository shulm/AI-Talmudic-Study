import copy,json,sys
from pathlib import Path
sys.path.insert(0,'research/bavli_production_v1');import runner
out=Path(__file__).resolve().parent;lane=out.parents[1];prod=lane/'arakhin/bounded_005_20261127';job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_arakhin');sha=lambda p:runner.sha(p.read_bytes())
reading=runner.read(out.parent/'SOURCE_READING.json');assert sha(out.parent/'SOURCE_READING.json')=='dbfe11c774331a9f395da7f42ea6e90f6b0987a808738e7bc5d509a5d8cfeca4'
receipt=runner.read(prod/'RECEIPT.json');version='323eb4bd621eff893cfd37c67016897d4a4af087b547a7e497b8858a60cab768';raw=(job/'snapshots'/f'{version}.json').read_bytes();assert runner.sha(raw)==version;state=json.loads(raw)
j,src=runner.load(job);assert j['source_sha256']==reading['source_sha256'] and len(src)==1183
proposal=runner.read(prod/'PROPOSAL.json');assert sha(prod/'PROPOSAL.json')==receipt['proposal_sha256'];base=runner.read(job/'snapshots'/f"{receipt['base_snapshot_sha256']}.json")
now={r['id']:r for r in state['records']};live={k:r for k,r in now.items() if r['release_state']=='valid'};assert len(proposal['records'])==241
for r in base['records']:assert now[r['id']]==r
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
assert runner.encoded(replayed)==raw
rp=runner.report(state,src);assert set(rp['completed_by_layer'].values())=={90}
ex=runner.read(prod/'EXPORT.json');assert ex['snapshot_sha256']==version
for f,h in ex['files'].items():assert sha(Path(receipt['export_path'])/f)==h
groups=[['megillah_priest','megillah_levite','megillah_israel','megillah_q','suspend_priest','suspend_levite','suspend_israel'],['shmuel','suspend_priest','suspend_levite','suspend_israel'],['zimmun_priest','zimmun_levite','zimmun_israel','zimmun_q'],['atonement_food','no_zimmun_hyp'],['satiation','satiation_correct','zimmun_answer'],['zimmun_join_priest','zimmun_join_levite','zimmun_join_israel','teruma_meal','sacred_meal'],['outsider_cannot','priest_can','no_join_hyp','join_correct'],['valuation_priest','valuation_levite','valuation_israel','valuation_q','rava_bukhri'],['bukhri_pay','bukhri_testimony'],['rybz_nonpay','bukhri_dispute','rybz'],['priest_offering'],['ownership_omer','ownership_two_loaves','ownership_showbread'],['unconsecrated_q','bukhri_exempt'],['public_transfer','public_answer'],['shekel_dependency','priest_no_value_shekel','shekel_hyp_support'],['min_sela','abaye_first','minimum_objection'],['redemption_dependency','priest_no_value_redemption','abaye_second'],['asham_q','asham_absurd_tumtum','asham_absurd_androgynos','asham_objection_tumtum','asham_objection_androgynos'],['priest_before_priest','alternate_speaker','priest_answer','final_rationale'],['disfigured','afflicted','inclusion_source','disfigured_derivation','afflicted_derivation'],['unspecified','whole','not_limbs'],['vital_q','vital','vital_qualifies','dead'],['moribund_q','moribund','standing_yes','standing_no','dead_standing'],['single','hundred_q','hundred','hundred_qualification'],['man_man','man_woman','woman_man','woman_woman','women_q','woman_man_qualification','woman_woman_qualification']]
mapping=[]
for n,(f,ids) in enumerate(zip(reading['findings'][:25],groups),1):
 ids=['ar.e1.b005.'+x for x in ids];assert all(x in live for x in ids);mapping.append(dict(reader_id=f['id'],producer_ids=ids,disposition='targeted_rework' if n in [9,12] else 'represented',finding_id={9:'AR005-02',12:'AR005-01'}.get(n)))
context=[]
for n,f in enumerate(reading['findings'][25:],26):
 context.append(dict(reader_id=f['id'],scope='uncounted_context',disposition='Relevant continuation qualifications represented: inclusion, means versions, standing derivation and balanced-case allocation; new-unit/full-context extraction not required by this bounded core.'))
checks=dict(proposal_rows=241,proposal_spans=spans,source_inventory=1183,old_records_unchanged=True,live_dependencies_valid=True,exact_replay=True,export_files=len(ex['files']),coverage_each_layer=90)
verdict=dict(verdict='REWORK_TARGETED',reader='/root',comparator='/root',producer='/root/blind_review',snapshot_sha256=version,proposal_sha256=receipt['proposal_sha256'],source_reading_sha256=sha(out.parent/'SOURCE_READING.json'),source_first_core_findings=25,core_findings_represented_without_repair=23,core_findings_needing_targeted_repair=2,mapping=mapping,context_dispositions=context,required_repairs=runner.read(out/'FINDINGS.json')['findings'],checks=checks,limitations=['Prior source/review exposure disclosed in source freeze; no fresh random cohort.','Reader initial Rabbi expansion in finding009 also needs contextual-inference qualification, not historical certainty.','Reader finding005 says cross-folio-style to describe a short continuation;4a3–4a4 are on the same page. Original indices remain authoritative.','No full-tractate completeness or ML eligibility.'],next_ref=rp['next_unprocessed_by_layer']['claims'],open_tails=state['open_tails'],tractate_delivered=False,ml_eligible=False)
for name,value in [('CHECKS.json',checks),('REPLAY.json',dict(snapshot_sha256=version,replay_pass=True,**rp)),('VERDICT.json',verdict)]:runner.immutable(out/name,runner.encoded(value))
runner.immutable(out/'MANIFEST.json',runner.encoded(dict(files={p.name:sha(p) for p in out.iterdir() if p.is_file() and p.name!='MANIFEST.json'})))
print(json.dumps(dict(verdict=sha(out/'VERDICT.json'),manifest=sha(out/'MANIFEST.json'),checks=checks)))
