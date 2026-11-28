import sys,json
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');P=OUT.parent.parent/'yevamot/bounded013_20261127';HEAD='a5c5e81fa42b10012a6703b1aa4da19dc823fe98e027b01a674a6258870a5514';PH='041505230af0f05713ead36e4b9f6ce33e243908e5dc7a3969a0f5267181830e'
prep=read(OUT.parent/'SOURCE_READING.json');assert sha((OUT.parent/'SOURCE_READING.json').read_bytes())=='42dbb09bcb1714fc039fe0dde3fd50dabc6792473af73f9d61477cb20c1dd8d4'
assert sha((P/'INITIAL_PROPOSAL.json').read_bytes())==PH
assert sha((P/'RECEIPT.json').read_bytes())=='683ff398506118d14b786e182e6c75b46a8ce929bd97b86e8b1fdff6e01132e9'
assert sha((P/'MANIFEST.json').read_bytes())=='5fe040a350c2d85a429e90b9d68fd4bcc91c0ec3dbc15e99331cc5a8579c3f8e'
for n,h in read(P/'MANIFEST.json').items():assert sha((P/n).read_bytes())==h
receipt=read(P/'RECEIPT.json');job,segs=runner.load(J);assert job['source_sha256']==prep['source_sha256'];runner.authorize(J,'L03/yevamot',2)
for f in prep['findings']:
 for e in f['evidence']:
  s=segs[e['segment_id']];assert s['ref']==f['ref'] and s['source_index']==f['source_index'];assert s['text'][e['start_char']:e['end_char']]==e['quote']
head=read(J/'snapshots'/f'{HEAD}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
s=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 prev=s['proposals'];s=runner.validate_apply(s,json.loads(b),segs,job);s['proposals']=prev+[h]
assert runner.encoded(s)==runner.encoded(head)
p=read(P/'INITIAL_PROPOSAL.json');assert len(p['records'])==179;revised={r['supersedes'] for r in p['records'] if 'supersedes' in r};assert len(revised)==1
rows={r['id']:r for r in head['records']};active={k for k,r in rows.items() if r['release_state']=='valid'};base=read(J/'snapshots'/(receipt['parent_snapshot']+'.json'))
for r in base['records']:
 expected=dict(r)
 if r['id'] in revised:expected['release_state']='superseded'
 assert rows[r['id']]==expected

def strings(v):
 if isinstance(v,str):yield v
 elif isinstance(v,list):
  for x in v:yield from strings(x)
 elif isinstance(v,dict):
  for x in v.values():yield from strings(x)
assert not [(k,x) for k in active for x in strings([rows[k]['content'],rows[k].get('links',[])]) if x in rows and x not in active]
report=runner.report(head,segs);assert report['completed_by_layer']=={k:258 for k in runner.LAYERS}
ep=J/'exports/bounded013_20261127';em=read(ep/'manifest.json')
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
names=['yev012.context.rl_self','yev012.context.rl_brothers','yvfix012.yev012.context.rl_cowife','yvfix012.rl_brother_cowife','yvfix012.yev012.context.yohanan_chalutzah','yvfix012.yh_brother_chalutzah','yvfix012.yev012.context.yohanan_cowife','yvfix012.yh_brother_cowife','yev012.context.rl_reason yev012.context.no_rebuild','yvfix012.yev012.context.performer_only yvfix012.rl_brothers_prior','yvfix012.yev012.context.chalutzah_only yvfix012.rl_cowife_prior','yev012.context.yohanan_objection yev013.initial_men_choice yev013.initial_women_choice','yev012.context.brother_agency','yev012.context.cowife_agency','yev013.baraita_first yev013.yohanan_challenge','yev013.yohanan_baraita_fit','yev013.rl_baraita_challenge','yev013.baraita_ending','yev013.yohanan_ending_challenge','yev013.sheshet_ending yev013.akiva_nonattachment','yev013.akiva_missing_notice','yev013.sheshet_difficulty','yev013.ashi_rl yev013.ashi_shimon','yev013.ravina_yohanan yev013.ravina_sages','yev013.ashi_which_brothers yev013.ashi_yeludim','yev013.ashi_yeludim','yev013.ashi_noladim','yev013.ravina_noladim yev013.ravina_which_brothers','yev013.ravina_yeludim','yev013.yibbum_karet yev013.aha_ravina','yev013.yibbum_karet yev013.yibbum_positive','yev013.karet_rl yev013.positive_yohanan','yev013.sotah_cowife yev013.rav_chain','yev013.context.torah_qualification yev013.context.certain_qualifies','yev013.context.sotah_impurity','yev013.context.shimon_intercourse yev013.context.shimon_chalitzah','yev013.context.torah_scope yev013.context.rabbinic_countercase','yev013.context.hisda_reason yev013.context.rabbinic_model','yev013.context.doubt_home yev013.context.doubt_terumah yev013.context.doubt_chalitzah','yev013.context.doubt_no_yibbum yev013.context.certain_scope','yev013.context.doubt_impurity_q','yev013.context.yosi_married yev013.context.yosi_betrothed yev013.context.yosi_chain','yev013.context.sages_married yev013.context.sages_betrothed yev013.context.sages_seclusion','yev013.context.seclusion_euphemism yev013.context.impurity_extra','yev013.context.additional_negative yev013.context.yosi_no_this_negative','yev013.context.marriage_words']
assert len(names)==46
mapping=[]
for f,ns in zip(prep['findings'],names):
 ids=ns.split();assert all(k in active for k in ids),(f['id'],ids)
 mapping.append({'reader_id':f['id'],'scope':f['scope'],'producer_ids':ids,'disposition':'represented'})
assert rows['yev013.sheshet_ending']['content']['assertion_mode']=='challenged'
assert rows['yev013.sheshet_difficulty']['content']['assertion_mode']=='unresolved'
assert rows['yev013.rav_chain']['content']['transmission_chain']==['Rav Yehuda','Rav']
for k,term in [('ashi_yeludim','הילודים'),('ashi_noladim','הנולדים'),('ravina_noladim','הנולדים'),('ravina_yeludim','הילודים')]:assert term in rows['yev013.'+k]['content']['proposition']
for k in ['karet_rl','positive_yohanan']:assert 'not speaker identification' in rows['yev013.'+k]['content']['conditions'][0]
out={'verdict':'ACCEPT_BOUNDED','snapshot_sha256':HEAD,'proposal_sha256':PH,'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'producer_receipt_sha256':sha((P/'RECEIPT.json').read_bytes()),'producer_manifest_sha256':sha((P/'MANIFEST.json').read_bytes()),'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'source_sha256':job['source_sha256'],'reviewer':'/root/rosh_hashanah','method':prep['exposure']+' Exact-version comparison is nonblind; no new independent cohort credit.','scope':prep['scope'],'mapping':mapping,'source_findings':{'core':34,'context':12,'represented':46},'required_repairs':[],'findings':[{'id':'Y013-01','status':'pass','judgment':'Corrected liability matrix and agency context reused. Baraita first/ending challenges, Sheshet Aqiva explanation, explicit missing-attribution objection and unresolved קשיא preserved. Ashi/Ravina reconstructions remain distinct with exact הילודים/הנולדים terms and branch-specific scope links.'},{'id':'Y013-02','status':'pass','judgment':'Aha/Ravina karet versus positive-commandment views remain unassigned by names. Alignment with RL/Yohanan does not claim name identification. RavYehudah→Rav chain retained. Rav sotah claim carries Torah/certain qualifiers and relevant context replies, preserving rabbinic-model objection rationale.'},{'id':'Y013-03','status':'limitation','judgment':'Born-brothers chronology deliberately not normalized beyond exact printed categories. Context11a10–11b6 has selected semantic records but is uncounted; this bounded acceptance is not certification of every future core question/occurrence pass.'}],'checks':{'exact_full_replay':True,'source_offsets_indices':True,'export_files':True,'prior_records_preserved':True,'active_dependencies':True,'primary_partition_validation':True},'proposal_rows':179,'superseded_records':1,'completed_by_layer':report['completed_by_layer'],'remaining_per_layer':3611,'next_source':'Yevamot11a:10','open_tails':head['open_tails'],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'fresh_blind_cohort_credit':0,'random_cohort_credit':0,'tractate_acceptance':False,'resume':'Resume under coordinator instructions at11a10, reusing context, completing future eight passes and preserving supplied Rav-reply markers and uncertain birth-category normalization.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))
