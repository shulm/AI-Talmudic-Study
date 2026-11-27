import copy,json,sys
from pathlib import Path
sys.path.insert(0,'research/bavli_production_v1');import runner
out=Path(__file__).resolve().parent;lane=out.parents[1];prod=lane/'kiddushin/bounded_005_20261127';job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin');sha=lambda p:runner.sha(p.read_bytes())
reading=runner.read(out.parent/'SOURCE_READING.json');assert sha(out.parent/'SOURCE_READING.json')=='be0e2d4983de2b87b6652c0bfe95af63f649f2ccb963a69cd8079c1c2668e4e8'
receipt=runner.read(prod/'RECEIPT.json');version='66bd6c70d196f134d85cede76da2543693d7d7f57fb9f62d284b3e54bce052c0';raw=(job/'snapshots'/f'{version}.json').read_bytes();assert runner.sha(raw)==version;state=json.loads(raw)
j,src=runner.load(job);assert j['source_sha256']==reading['source_sha256'] and len(src)==2406
proposal=runner.read(prod/'INITIAL_PROPOSAL.json');assert sha(prod/'INITIAL_PROPOSAL.json')==receipt['proposal_sha256'];base=runner.read(job/'snapshots'/f"{receipt['parent_snapshot']}.json")
now={r['id']:r for r in state['records']};live={k:r for k,r in now.items() if r['release_state']=='valid'};revisions={r['supersedes'] for r in proposal['records'] if r.get('supersedes')};assert len(proposal['records'])==259 and len(revisions)==1
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
assert runner.encoded(replayed)==raw;rp=runner.report(state,src);assert set(rp['completed_by_layer'].values())=={90}
ex=runner.read(prod/'EXPORT.json');assert ex['snapshot_sha256']==version
for f,h in ex['files'].items():assert sha(Path(receipt['export_directory'])/f)==h

# Explicit semantic reconciliation from source-first findings, not inferred from overlap.
groups = [
['kid004.maid_money','kid004.maid_no_intercourse','kid004.context.maid_not_marriage','kid004.context.wife_marriage'],
['kid004.context.intercourse_verse_need','kid004.context.rav_ashi','kid004.context.initial_refutation'],
['kid004.context.yevamah_bound','kid004.context.wife_unbound','kid004.context.bond_refutation','kid004.context.verse_answer'],
['deed_q','money_noexit','money_entry','deed_exit','deed_af'],
['money_redeems_holy','money_redeems_maaser','deed_no_redeem_holy','deed_no_redeem_maaser','redemption_verse','redemption_objection'],
['entry_exit_link','deed_rule','reverse_link_q','money_divorce_hyp'],
['abaye','abaye_advocate','deed_prosecutor_q','abaye_rejects'],
['different_deed_texts','different_coins_q','same_currency','currency_answer'],
['rava','rava_writing','rava_no_money','exclude_deed_entry_q','no_deed_entry_hyp','link_rejects_no_entry'],
['choose_exclusion_q','divorce_context','context_answer'],
['yosi_no_money_q','yosi_book_only','yosi','yosi_answer'],
['sages_severance_q','complete_separation','sages_answer'],
['wine_forever','home_forever','wine_thirty','home_thirty'],
['yosi_lexical','sages_no_lexical','lexical_difference'],
['pair_derivation_q','deed_pair_q','money_intercourse_benefit','deed_pair_block'],
['intercourse_pair_q','money_deed_range','intercourse_pair_block'],
['money_pair_q','intercourse_deed_forced','money_pair_block'],
['maid_forced_q','maid_money_forced','money_not_forced_marriage','marital_answer'],
['huna','huna_canopy','money_no_terumah_hyp','canopy_terumah','canopy_food_af'],
['money_food_q','ulla','ulla_torah','ulla_acquired','ulla_objection'],
['context.decree_q','context.decree','context.torah_qualified'],
['context.money_not_finish','context.corrected_af','context.corrects_food_af'],
['context.canopy_finishes','context.corrected_af','context.redemption_objection','context.intercourse_counter'],
['context.intercourse_yevamah','context.money_counter','context.pair_common'],
['context.benefit_objection','context.deed_counter','context.deed_exit_feature','context.pair_counter'],
['context.three_common','context.three_support'],
['context.forced_objection','context.huna_force_reply','context.force_answer'],
['context.rava_three','context.rava','context.rava_count'],
['context.rava_prior','context.rava_dependency','context.rava_inference'],
['context.abaye_count','context.abaye','context.count_reply'],
['context.money_after_money','context.canopy_after_money','context.abaye_af','context.abaye_dependency_reply'],
[],[],[]]
# Supplemental granular readings recheck the same source propositions independently.
for n in list(range(1,21))+[21,22,28,29,30,31]:
 groups.append(list(groups[n-1]))
assert len(groups)==60
# Supplemental035–059 comprise25: omit duplicated source003, whose002 already follows continuation.
del groups[36]
assert len(groups)==len(reading['findings'])==59
mapping=[]
for f,ids in zip(reading['findings'],groups):
 ids=[x if x.startswith('kid004.') else 'kid005.'+x for x in ids]
 assert all(x in live for x in ids),(f['id'],ids)
 assert src[f['segment_id']]['text']==f['quote']
 mapping.append(dict(reader_id=f['id'],scope=f['scope'],producer_ids=ids,disposition='represented' if ids else 'next_unit_boundary_read_only'))
assert sum(x['scope']=='core' for x in mapping)==39
checks=dict(proposal_rows=259,proposal_spans=spans,superseded_rows=1,source_inventory=2406,all_prior_bytes_preserved_except_release_state=True,live_dependencies_valid=True,exact_replay=True,export_files=len(ex['files']),coverage_each_layer=90)
verdict=dict(verdict='ACCEPT_BOUNDED_WITH_LIMITATIONS',reader='/root',comparator='/root',producer='/root/yevamot',snapshot_sha256=version,proposal_sha256=receipt['proposal_sha256'],source_reading_sha256=sha(out.parent/'SOURCE_READING.json'),source_first_core_findings=39,core_findings_represented=39,context_findings_represented=17,context_boundary_findings=3,mapping=mapping,required_repairs=[],checks=checks,limitations=['Source reading reused earlier004 context with exposure disclosed; not a new blind cohort.','Source-reading019 wording called later canopy argument a boundary;005 includes its opening5a16–17 as core and follows necessary continuation through5b9 without counting context.','Named Ulla teaching is quoted in anonymous challenge; speaker role denotes quoted teaching, not direct presence or invented transmission.','No final unanimous canopy ruling, full tractate delivery, or ML eligibility.'],next_ref=rp['next_unprocessed_by_layer']['claims'],open_tails=state['open_tails'],tractate_delivered=False,ml_eligible=False)
for name,value in [('CHECKS.json',checks),('REPLAY.json',dict(snapshot_sha256=version,replay_pass=True,**rp)),('VERDICT.json',verdict)]:runner.immutable(out/name,runner.encoded(value))
runner.immutable(out/'MANIFEST.json',runner.encoded(dict(files={p.name:sha(p) for p in out.iterdir() if p.is_file() and p.name!='MANIFEST.json'})))
print(json.dumps(dict(verdict=sha(out/'VERDICT.json'),manifest=sha(out/'MANIFEST.json'),checks=checks)))
