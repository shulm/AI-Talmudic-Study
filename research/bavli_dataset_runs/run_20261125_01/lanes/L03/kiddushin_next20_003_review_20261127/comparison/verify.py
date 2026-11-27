import sys,json
from pathlib import Path
sys.path.insert(0,'research/bavli_production_v1');import runner
out=Path(__file__).resolve().parent;lane=out.parents[1];prod=lane/'kiddushin/bounded_003_20261127';job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin');sha=lambda p:runner.sha(p.read_bytes())
reading=runner.read(out.parent/'SOURCE_READING.json');assert sha(out.parent/'SOURCE_READING.json')=='4f0b0222efebf96af9a7c072b934809466458b5564e85e737e911e09370d506e'
receipt=runner.read(prod/'RECEIPT.json');version='5120405f3ba10a4a6863730b405cad2496965e0638120ed57a3b9eddc2f8976d';state=runner.current(job);assert runner.sha(runner.encoded(state))==version
j,src=runner.load(job);assert j['source_sha256']==reading['source_sha256'] and len(src)==2406
proposal=runner.read(prod/'INITIAL_PROPOSAL.json');assert sha(prod/'INITIAL_PROPOSAL.json')==receipt['proposal_sha256'];assert len(proposal['records'])==209
base=runner.read(job/'snapshots'/f"{receipt['parent_snapshot']}.json");now={r['id']:r for r in state['records']};live={k:r for k,r in now.items() if r['release_state']=='valid'}
assert not any(r.get('supersedes') for r in proposal['records'])
for r in base['records']:assert now[r['id']]==r
spans=0
for r in proposal['records']:
 for e in r['evidence']:
  t=src[e['segment_id']]['text'];assert t[e['start_char']:e['end_char']]==e['quote'];spans+=1
for r in live.values():
 c=r['content'];deps=list(r['links'])
 if r['layer']=='positions':deps += [c['claim_id']]+([c['question_id']] if c['question_id'] else [])
 if r['layer']=='edges':deps += [c['source_id'],c['target_id']]
 assert all(x in live for x in deps)
for c in state['coverage']:assert all(x in live for x in c['record_ids'])
rp=runner.replay(job);assert rp['snapshot_sha256']==version and set(rp['completed_by_layer'].values())=={50}
ex=runner.read(prod/'EXPORT.json');assert ex['snapshot_sha256']==version
dirs=[p.parent for p in (job/'exports').rglob('manifest.json') if runner.read(p).get('snapshot_sha256')==version];assert dirs
for f,h in ex['files'].items():assert sha(dirs[0]/f)==h
groups=[
['money_source','father_source','father_right.money','father_right.deed','father_right.intercourse'],
['rav_report','no_master_money','other_master'],['daughter_money','father_accepts','father_not_daughter'],
['minor_adolescent','minor_premise','adolescent_hyp'],['youth_benefits','annulment_correction'],
['rav_huna_report','maid_earnings','daughter_earnings','maid_analogy'],['labor_redundancy','labor_objection'],
['annulment_context','money_not_prohibition','financial_inference_block'],['fine_alternative','money_not_fine'],['shame_damage_alternative','father_in_damage'],
['comparable_exit'],['comparable_exit','exit_father_answer'],['exit_difference','master_complete_exit','chuppah_pending'],['annulment_exit','joint_annulment','partial_exit_answer'],
['free_verse_use'],['maturity_release','adolescent_release'],['ravina','ravina_yod','yod_answer'],['yod_method','offspring_base'],
['grandchildren_initial'],['disqualified_offspring'],['double_yod'],['grandchildren_children','invalid_allocation','grandchildren_reallocation'],
['tanna_orthography','maan_spellings','yod_derash'],['both_needed','betrothal_no_labor','earnings_hers_hyp'],['earnings_support_hyp','betrothal_hers_hyp','both_needed'],
['maturity_release','adolescent_release','exit_baraita'],['maturity_redundancy'],['context.rabbah','rabbah'],
['context.resident','context.hired'],['context.shorter_af'],['context.resident_misread','context.hired_clarifies'],
['context.abaye_objection','context.two_bodies'],['context.one_body','abaye_objection'],['context.aylonit_release','abaye'],
['context.aylonit_no_exit_hyp'],['context.mar_objection','context.signs','context.maturity_father','context.maturity_af'],
['context.aylonit_sale','context.no_sale_hyp','mar'],['context.aylonit_sale','sale_corrects'],['context.why_not_write_af','context.prefer_other','prefer_answer']]
assert len(groups)==len(reading['findings'])==39;mapping=[]
for f,ids in zip(reading['findings'],groups):
 ids=['kid003.'+x for x in ids];assert all(x in live for x in ids);mapping.append(dict(reader_id=f['id'],scope=f['scope'],ref=f['ref'],producer_ids=ids,disposition='represented'))
# Explicitly confirm repeated age-verse occurrences and cross-folio source anchors.
for key in ['maturity_release','adolescent_release']:
 refs={src[e['segment_id']]['ref'] for e in live['kid003.'+key]['evidence']};assert {'Kiddushin 4a:3','Kiddushin 4a:11'}<=refs
refs={src[e['segment_id']]['ref'] for e in live['kid003.comparable_exit']['evidence']};assert {'Kiddushin 3b:12','Kiddushin 4a:1'}<=refs
assert live['kid003.rav_report']['content']['transmission_chain']==['Rav Yehuda','Rav']
assert live['kid003.rav_huna_report']['content']['transmission_chain']==['Rav Huna','Rav']
checks=dict(source_inventory=2406,new_records=209,evidence_spans=spans,old_records_unchanged=True,live_dependencies_valid=True,replay_pass=True,export_files_verified=len(ex['files']),repeated_source_occurrences_retained=True,cross_folio_comparable_exit_preserved=True,coverage_per_layer=50)
verdict=dict(verdict='ACCEPT_BOUNDED_WITH_LIMITATIONS',reader='/root',comparator='/root',producer='/root/yevamot',source_reading_sha256=sha(out.parent/'SOURCE_READING.json'),snapshot_sha256=version,proposal_sha256=receipt['proposal_sha256'],scope='20 original cores Kiddushin3b4–4a11; continuation4a12–4b2 represented but uncounted',core_findings_represented=27,context_findings_represented=12,mapping=mapping,required_repairs=[],limitations=['Same-reader previous002 exposure disclosed; no random/fresh-cohort credit.','Rav/Rav Yehuda/Rav Huna and Rabbah/Mar bar Rav Ashi are kept distinct. No attribution by ordering.','Repeated age-release claims share record IDs with two exact source occurrences; occurrence counts must use evidence locations, not unique claim count.','Aylonit adolescence-versus-maturity statements are rejected or challenged hypotheses; never read them as actual acquisition of adolescent signs.','Context comparative premises remain grouped where they constitute the explicit contrast, with component words and conditions preserved; this does not establish task-specific fully atomic retrieval eligibility.','No final practical halakhic ruling, whole-tractate acceptance, or ML qualification is granted.'],coverage=rp['completed_by_layer'],next_ref='Kiddushin4a12',open_tails=state['open_tails'],tractate_delivered=False,ml_eligible=False)
for name,value in [('CHECKS.json',checks),('REPLAY.json',rp),('VERDICT.json',verdict)]:runner.immutable(out/name,runner.encoded(value))
runner.immutable(out/'MANIFEST.json',runner.encoded(dict(files={p.name:sha(p) for p in sorted(out.iterdir()) if p.is_file() and p.name!='MANIFEST.json'})))
print(json.dumps(dict(verdict_sha256=sha(out/'VERDICT.json'),manifest_sha256=sha(out/'MANIFEST.json'),checks=checks)))
