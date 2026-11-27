import json,hashlib
from pathlib import Path
D=Path(__file__).parent
initial=D/'l01_l03_initial.json'
assert hashlib.sha256(initial.read_bytes()).hexdigest()=='f6adc3a4ad004ac5fdf231e0cee2b906f61880c7e437eca22d678810741394ca'
i=json.loads(initial.read_text(encoding='utf-8')); ir={r['id']:r for r in i['findings']}
raw={r['evidence'][0]['segment_id']:r['evidence'][0]['quote'] for r in i['findings'] if r['layer']=='structure' and r['content']['primary']}
snapshots={};records={};mapping={};validation=[]
for title,lane,slug,h,prefixes in [('Berakhot','L01','bavli_berakhot','debfcb90f8d5e77e1d690fd9b3553b26ec8914d446c638173a850c423558954d',('bk.opening.','bk.order.')),('Rosh Hashanah','L03','bavli_rosh_hashanah','43b129227acc4beeca9ac053abc23a39dbde17b689b77ceb72c6683200cec828',('rh.kings.',))]:
 p=Path('F:/Sefaria_QA/bavli_production_run_20261125_01')/lane/slug/'snapshots'/f'{h}.json';assert hashlib.sha256(p.read_bytes()).hexdigest()==h
 s=json.loads(p.read_text(encoding='utf-8')); snapshots[title]={'path':str(p),'sha256':h}
 rr=[r for r in s['records'] if r['release_state']=='valid' and r['id'].startswith(prefixes)]
 for r in rr:
  records[r['id']]=r
  if r['layer']=='structure' and r['content']['primary']:
   for e in r['evidence']:
    matches=[ref for ref,t in raw.items() if ref.startswith(title+' ') and t==e['quote'] and e['start_char']==0 and e['end_char']==len(t)]
    assert len(matches)==1;mapping[e['segment_id']]=matches[0]
 for r in rr:
  for e in r['evidence']:
   ref=mapping[e['segment_id']];assert raw[ref][e['start_char']:e['end_char']]==e['quote']
 validation.append({'tractate':title,'active_core_records':len(rr),'exact_offset_check':'passed','primary_partition_check':'complete core full segments, no overlaps'})

findings=[]
def f(id,category,severity,ids,initial_ids,description,action):
 ev=[]
 for rid in initial_ids:
  for e in ir[rid]['evidence']:
   if e not in ev:ev.append(e)
 findings.append(dict(id=id,category=category,severity=severity,producer_record_ids=ids,initial_finding_ids=initial_ids,evidence=ev,description=description,action=action))
f('L01-C01','granularity','targeted_exception',['bk.order.pass2.c.later','bk.order.pass2.p.later'],['bc14','bc15'],'Both blessing prescriptions are accurately preserved, but one claim bundles morning and evening prescriptions despite the atomic-claim requirement. This is not a wrong quotation or wrong law.','Split into morning and evening claims/positions with exact clause evidence; preserve their shared quotation role and support to the ordering objection. Supersede the composite claim and update dependent edges.')
f('L01-C02','attribution_uncertainty','targeted_exception',['bk.opening.pass1.p.general','bk.opening.pass1.u.4'],['ba6','bc7'],'The generalized midnight/dawn tail is assigned to Rabban Gamliel in narrative continuation with no uncertainty entry. This is a plausible reading, not a confirmed attribution error, but the source has no fresh named speech marker at ולא זו בלבד.','Record the attribution-boundary uncertainty explicitly or represent the holder as Mishnah continuation with Rabban Gamliel as a possible continuation. Retain the explicit named attribution of אמר להם for the sons’ obligation.')
f('L01-C03','edge_scope_uncertainty','targeted_exception',['bk.order.pass2.edge.objection'],['bn1','bq5'],'The edge attaches אי הכי exclusively to the creation answer. The local adjacency supports this, but the objection can challenge evening-first ordering generally, also addressed by the scripture answer. The frozen independent review itself retains this provisional edge plus an explicit warning.','Add scope uncertainty or model the common ordering rationale; do not present exclusive target selection as settled by the source.')
f('L03-C01','graph_omission','targeted_exception',['rh.kings.pass1.c.son','rh.kings.pass1.p.son','rh.kings.pass1.answer_split','rh.kings.pass1.son'],['rc16','re9','re10'],'The prior-Adar-appointment and king’s-son answer is accurately extracted, with both conditions retained, and qualifies c.split. However no answer edge or position question_id connects c.son to q.split. The existing answer edge uses the rejected hypothetical c.hyp_split. This leaves the explicit לא צריכא answer disconnected from its question.','Add c.son → q.split answer edge and bind p.son.question_id to q.split; keep the existing hypothetical rationale and qualification edge.')
f('L03-C02','graph_omission','targeted_exception',['rh.kings.pass1.c.appointment','rh.kings.pass1.c.nisan','rh.kings.pass1.appointment'],['rc8','re6'],'The prior appointment condition is retained and linked as an answer to q.obvious1. The graph lacks a qualification edge from that condition record to the Nisan-accession rule it restricts. This is missing graph structure, not missing textual content.','Add c.appointment → c.nisan qualification edge with 2b:2 evidence.')
f('L03-C03','attribution_scope_omission','targeted_exception',['rh.kings.pass1.mishnah','rh.kings.pass1.baraita1','rh.kings.pass1.baraita2'],['ra2','ra3','ra4'],'Each quotation attribution scopes only the first claim: Mishnah only c.early, first baraita only c.adar, second baraita only c.both_adar. Later claims retain correct quoted holders in positions/utterances, so the identities are not lost globally. Attribution-layer scope is nonetheless incomplete for c.late, c.nisan, c.both_nisan and c.split.','Supply attribution records scoped to the remaining claims, or scope the quotation attribution to a shared utterance/group covering all quoted claims. Do not invent named transmitters.')
f('L03-C04','structured_condition_granularity','advisory',['rh.kings.pass1.c.hyp_adar','rh.kings.pass1.c.hyp_nisan','rh.kings.pass1.c.hyp_split','rh.kings.pass1.p.hyp_adar','rh.kings.pass1.p.hyp_nisan','rh.kings.pass1.p.hyp_split'],['rc13','rc14','rc17'],'Rejected hypotheticals have empty conditions arrays. The propositions preserve the important content, and c.son retains the hereditary/appointment condition, so this is not substantive condition deletion. Consumers relying only on typed conditions cannot recover all case restrictions directly.','Populate conditions arrays for same-Adar, same-Nisan, and cross-month appointment/heredity cases, preserving rejected assertion status.')

# Mapping is semantic, not a record-count agreement statistic.
claims={
'bc1':'bk.opening.pass1.c.start','bc2':'bk.opening.pass1.c.re','bc3':'bk.opening.pass1.c.sages','bc4':'bk.opening.pass1.c.rg','bc5':'bk.opening.pass1.c.sons','bc6':'bk.opening.pass1.c.duty','bc7':'bk.opening.pass1.c.general','bc8':'bk.opening.pass1.c.fats','bc9':'bk.opening.pass1.c.eaten','bc10':'bk.opening.pass1.c.safeguard','bc11':'bk.order.pass2.c.scripture','bc12':'bk.order.pass2.c.restatement','bc13':'bk.order.pass2.c.creation','bc14':'bk.order.pass2.c.later','bc15':'bk.order.pass2.c.later','bc16':'bk.order.pass2.c.sequence',
'rc1':'rh.kings.pass1.c.documents','rc2':'rh.kings.pass1.c.early','rc3':'rh.kings.pass1.c.late','rc4':'rh.kings.pass1.c.adar','rc5':'rh.kings.pass1.c.nisan','rc6':'rh.kings.pass1.c.newyear','rc7':'rh.kings.pass1.c.day','rc8':'rh.kings.pass1.c.appointment','rc9':'rh.kings.pass1.c.hyp_two','rc10':'rh.kings.pass1.c.both_adar','rc11':'rh.kings.pass1.c.both_nisan','rc12':'rh.kings.pass1.c.split','rc13':'rh.kings.pass1.c.hyp_adar','rc14':'rh.kings.pass1.c.hyp_nisan','rc15':'rh.kings.pass1.c.hyp_nisan','rc16':'rh.kings.pass1.c.son','rc17':'rh.kings.pass1.c.hyp_split'}
questionmap={'bq1':'bk.opening.pass1.q.time','bq2':'bk.opening.pass1.q.midnight','bq3':'bk.order.pass2.q.foundation','bq4':'bk.order.pass2.q.order','bq5':'bk.order.pass2.q.objection','rq1':'rh.kings.pass1.q.application','rq2':'rh.kings.pass1.q.obvious1','rq3':'rh.kings.pass1.q.adar','rq4':'rh.kings.pass1.q.nisan','rq5':'rh.kings.pass1.q.split'}
for rid in list(claims.values())+list(questionmap.values()):assert rid in records
for entry in findings:
 for rid in entry['producer_record_ids']:assert rid in records
out=dict(artifact_type='hash_bound_targeted_independent_comparison',reviewer_agent_id='/root/review_l01_l03',model_id=None,initial_review_sha256=hashlib.sha256(initial.read_bytes()).hexdigest(),producer_snapshots=snapshots,manifest_sha256=i['manifest_sha256'],source_hashes={k:v['source_sha256'] for k,v in i['sources'].items()},core_refs=i['core_refs'],decision='ACCEPT_PARTIAL_WITH_EXCEPTIONS',full_tractate_certification=False,whole_probability_sample_complete=False,ml_eligible=False,summary='The 21-segment targeted cohorts preserve the main source propositions, named speakers, alternatives, rejected suppositions, and critical conditions. No confirmed wrong substantive law or named-speaker substitution found. Exceptions concern atomic granularity, uncertainty and graph/attribution completeness; they must not be treated as fully qualified data until addressed.',confirmed_semantic_errors=[],exceptions=findings,claim_correspondence=claims,question_correspondence=questionmap,comparison_notes=[
'Rosh Hashanah beginning-of-year positive consequence (initial rc15) is preserved through rejection of the end-only distinction in c.hyp_nisan, with c.both_nisan and reject_nisan. A separate positive claim is an optional granularity choice, not a confirmed omission.',
'Primary producer structure spans 2a:8–2b:1 within one larger unit; it does not close at the page break. The initial per-segment ownership envelopes differ in granularity only.',
'Conditional duty is marked asserted in producer but includes the if-dawn condition in both proposition and conditions; no false unconditional duty was introduced.',
'Empty candidates arrays with a named surface label do not prove identity loss when positions explicitly preserve the named holder; no invented canonical identity required.',
'No named transmission chain appears in these core ranges. Rav Hisda is correctly kept distinct from Rav.',
'An initial unfiltered snapshot display exposed outside-core B24 and RH opening records after authorized unblinding; those records are excluded from every finding, count and decision here.'
],validation=validation,producer_segment_ref_mapping=mapping,limitations=['Targeted opening/risk review only, no full tractate or sample certification.','Comparison is AI provisional, not human scholarly validation.','No producer mutation, qualification promotion or commit performed.'])
p=D/'l01_l03_comparison.json';assert not p.exists();p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(hashlib.sha256(p.read_bytes()).hexdigest(),validation)
