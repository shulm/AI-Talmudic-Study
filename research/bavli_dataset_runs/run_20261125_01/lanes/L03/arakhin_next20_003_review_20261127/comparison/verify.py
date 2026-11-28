import sys,json,copy
from pathlib import Path
sys.path.insert(0,'research/bavli_production_v1');import runner
out=Path(__file__).resolve().parent;lane=out.parents[1];prod=lane/'arakhin/bounded_003_20261127';job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_arakhin');sha=lambda p:runner.sha(p.read_bytes())
reading=runner.read(out.parent/'SOURCE_READING.json');assert sha(out.parent/'SOURCE_READING.json')=='d5fb6ef762f3341628ccf07deddcc789a244f3e141554e0d7a9c7f26abb57ea1'
receipt=runner.read(prod/'RECEIPT.json');version='aedce52cf49aaef99ee1e1ae26584edf8cbcbd3df0c86637a959ad2c778fe658';s=runner.current(job);assert runner.sha(runner.encoded(s))==version
j,src=runner.load(job);assert j['source_sha256']==reading['source_sha256'];assert len(src)==1183
proposal=runner.read(prod/'INITIAL_PROPOSAL.json');assert sha(prod/'INITIAL_PROPOSAL.json')==receipt['proposal_sha256']
base=runner.read(job/'snapshots'/f"{receipt['base_snapshot_sha256']}.json");before={r['id']:r for r in base['records']};now={r['id']:r for r in s['records']};live={k:r for k,r in now.items() if r['release_state']=='valid'}
sup={r['supersedes'] for r in proposal['records'] if r.get('supersedes')};assert len(sup)==7
for rid,r in before.items():
 expected=copy.deepcopy(r)
 if rid in sup:expected['release_state']='superseded'
 assert now[rid]==expected
spans=0
for r in proposal['records']:
 for e in r['evidence']:
  t=src[e['segment_id']]['text'];assert t[e['start_char']:e['end_char']]==e['quote'];spans+=1
for r in live.values():
 deps=list(r['links']);c=r['content']
 if r['layer']=='positions':deps += [c['claim_id']]+([c['question_id']] if c['question_id'] else [])
 if r['layer']=='edges':deps += [c['source_id'],c['target_id']]
 assert all(x in live for x in deps)
for c in s['coverage']:
 assert all(x in live for x in c['record_ids'])
rp=runner.replay(job);assert rp['snapshot_sha256']==version and set(rp['completed_by_layer'].values())=={50}
ex=runner.read(prod/'EXPORT.json');assert ex['snapshot_sha256']==version
exdirs=[p.parent for p in (job/'exports').rglob('manifest.json') if runner.read(p).get('snapshot_sha256')==version];assert exdirs
exdir=exdirs[0]
for f,h in ex['files'].items():assert sha(exdir/f)==h
prefix='ar.e1.b003.'
groups=[
['ar.e1.r002.initial'],['no_slave_marriage','no_free_marriage','master_only'],['creation','idle'],['compel_free','debt'],['ar.e1.r002.retraction','ar.e1.r002.initial.retracted','ar.e1.r002.chronology.context'],
['shofar_q','shofar_minor'],['shofar_allow','shofar_proof'],['megillah_q','women_eligible'],['women_obligated','rybl'],['miracle','miracle_reason'],
['zim_q','women_zim','slaves_zim'],['women_zim','slaves_zim'],['join_q','minor_join'],['nahman','minor_join'],
['zivah_q','infant_zivah'],['ish_double','judah_zivah','zivah_proof'],['proof_unneeded','yishmael','proof_alternative'],['male_all','female_all'],['human_language','language_a'],
['minor_corpse'],['corpse_exclude','nefashot','corpse_correct'],['ish_exclude','minor_karet'],['minor_lesion','lesion_exclude'],['perhaps_exclude','adam','adam_proof'],
['ish_need','woman_source','woman_lesion'],['man_hair','man_tear','woman_nohair','woman_notear'],
['inspect_q','nonexpert'],['noexpert_quote','inspect_conflict'],['ravina','understands','no_understand','understand_scope','no_understand_scope'],
['sanctify_q','judah_minor','sages_woman'],['sages_no_deaf','sages_no_incompetent','sages_no_minor'],['judah_minor','judah_nowoman','judah_noandrogynos'],['sprinkle_q','uncircumcised'],['elazar','uncircumcised']]
assert len(groups)==len(reading['findings'])==34
mapping=[]
for f,ids in zip(reading['findings'],groups):
 ids=[x if x.startswith('ar.') else prefix+x for x in ids];assert all(x in live for x in ids)
 mapping.append(dict(reader_id=f['id'],ref=f['ref'],producer_ids=ids,disposition='represented'))
checks=dict(source_inventory=1183,proposal_records=len(proposal['records']),proposal_evidence_spans=spans,superseded=7,old_rows_unchanged_except_declared_release_state=True,active_dependencies_valid=True,coverage_per_layer=50,replay_pass=True,export_files_verified=len(ex['files']),source_first_reading_precedes_dispatch=True)
verdict=dict(verdict='ACCEPT_BOUNDED_WITH_LIMITATIONS',reader='/root',comparator='/root',producer='/root/blind_review',snapshot_sha256=version,proposal_sha256=receipt['proposal_sha256'],source_reading_sha256=sha(out.parent/'SOURCE_READING.json'),scope='20 original cores Arakhin2b14–3a15, not all50 production cores freshly reviewed',mapping=mapping,findings_represented=34,required_repairs=[],limitations=['Prior contextual2b14–16 exposure and earlier review preserved; not fresh blindness or random cohort.','Initial alternating-day arrangement is retained as one relational schedule, with Beit Hillel retraction explicitly linked.','Lesion-inspection initial inclusion is stored with final Ravina condition; raw contrary teaching and objection, local-stage notes and reconciliation remain. Do not treat final qualified inclusion and provisional exclusion as a lasting dispute.','Normal source abbreviation Rabbi Elazar is resolved by explicit same-segment name; no external identity matching claimed.','This bounded acceptance grants no whole-tractate acceptance or ML/task qualification.'],coverage=rp['completed_by_layer'],next_ref='Arakhin3a16',open_tails=s['open_tails'],ml_eligible=False,tractate_delivered=False)
for name,value in [('CHECKS.json',checks),('REPLAY.json',rp),('VERDICT.json',verdict)]:runner.immutable(out/name,runner.encoded(value))
runner.immutable(out/'MANIFEST.json',runner.encoded(dict(files={p.name:sha(p) for p in sorted(out.iterdir()) if p.is_file() and p.name!='MANIFEST.json'})))
print(json.dumps(dict(verdict_sha256=sha(out/'VERDICT.json'),manifest_sha256=sha(out/'MANIFEST.json'),checks=checks)))
