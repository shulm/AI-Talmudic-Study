import json,hashlib
from pathlib import Path
root=Path(__file__).parent
base=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot')
review=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
hashes={}
def read(p,expected=None):
 b=p.read_bytes();h=hashlib.sha256(b).hexdigest();hashes[str(p)]=h
 if expected:assert h==expected,(p,h,expected)
 return json.loads(b)
oldh='03622eb5170ef5507fa5846f93156fe872c2bd99f326f7d6c7641ade69050f1e'
newh='1cb99b6538dd9323c93dc54ef524320400ec7ea4a10bcfabad9657d35f66a817'
proph='a6aaf8c1f102b1636acb0daee1b81db66e7ca2d6618afaad49e889339783551d'
reading=read(review/'readings/berakhot_batch001.json','583a9532d6b54631eafbe19fd941281d222e1fa43089537645fa7c95ad3436fb')
comparison=read(review/'comparisons/berakhot_03622eb5_batch001.json','51067df028d991c8750c6e08387174dba22d930e10e73c827591c64edcd07ade')
verdict=read(review/'verdicts/berakhot_03622eb5.json')
old=read(base/f'snapshots/{oldh}.json',oldh);new=read(base/f'snapshots/{newh}.json',newh);proposal=read(base/f'proposals/{proph}.json',proph)
src=read(Path(reading['source_path']),reading['source_sha256'])
inventory=read(base/'source_inventory.json');seg={s['id']:s for s in inventory}
for s in inventory:
 i,j=s['source_index'];assert src['text'][i][j]==s['text']
 assert s['ref']==f'Berakhot {i//2+1}{"ab"[i%2]}:{j+1}'
om={r['id']:r for r in old['records']};nm={r['id']:r for r in new['records']}
assert set(om)<=set(nm)
added=set(nm)-set(om);assert added=={r['id'] for r in proposal['records']}
changed={k for k in om if om[k]!=nm[k]};replaced={nm[k]['supersedes'] for k in added}
assert changed==replaced and len(added)==8
for k in om:
 a=dict(om[k]);b=dict(nm[k]);a.pop('release_state',None);b.pop('release_state',None);assert a==b
for k in replaced:assert nm[k]['release_state']=='superseded'
assert new['proposals']==old['proposals']+[proph]
span_count=0
for r in new['records']:
 assert r['ml_eligible'] is False
 for e in r.get('evidence',[]):
  i,j=seg[e['segment_id']]['source_index'];s=src['text'][i][j]
  assert 0<=e['start_char']<=e['end_char']<=len(s)
  assert s[e['start_char']:e['end_char']]==e['quote'],r['id'];span_count+=1
assert new['ml_eligible'] is False
def refs(r):
 out=list(r.get('links',[]))
 for k in ['claim_id','question_id','source_id','target_id','scope']:
  v=r.get('content',{}).get(k)
  if isinstance(v,str) and v in nm:out.append(v)
 return out
active=[r for r in new['records'] if r['release_state']=='valid']
stale=[(r['id'],x) for r in active for x in refs(r) if x in replaced]
assert not stale,stale
for r in active:
 for x in r.get('links',[]):assert x in nm,x
def cov(s):return {(c['segment_id'],c['layer']):(c['extraction_state'],c['extraction_result']) for c in s['coverage']}
assert cov(old)==cov(new)
completed=lambda s:{c['segment_id'] for c in s['coverage'] if c['layer']=='claims' and c['extraction_state']=='completed'}
assert completed(old)==completed(new) and len(completed(new))==71
for c in new['coverage']:
 for k in c.get('record_ids',[]):assert k in nm and k not in replaced,(c,k)
suffix='.review20261126'
for k in ['bk.opening.pass1.c.duty','bk.opening.pass1.p.duty']:
 assert nm[k+suffix]['content']['conditions']==['The sons have not yet recited Shema','Dawn has not risen']
 assert len(nm[k+suffix]['evidence'])==2
for k in ['bk.watch_dispute.20261125.p10n','bk.watch_dispute.20261125.p10r']:
 assert nm[k+suffix]['content']['question_id'] is None
 assert nm[k+suffix]['links']==[nm[k+suffix]['content']['claim_id']]
for k in ['bk.watch_dispute.20261125.e15','bk.watch_dispute.20261125.e16']:
 assert nm[k+suffix]['content']==om[k]['content']
 assert any('qualification' in u and 'before adjudication' in u for u in nm[k+suffix]['uncertainty'])
def source_span(i,j):
 s=src['text'][i][j];return dict(ref=f'Berakhot {i//2+1}{"ab"[i%2]}:{j+1}',start_char=0,end_char=len(s),quote=s)
findings=[
 dict(id='BR-COND-001',initial_state='proposed_correction_pending',verification='CORRECTION_VERIFIED_IN_SNAPSHOT',evidence=[source_span(2,3)],explanation='Both explicit premises are now structured in claim and position: sons have not recited and dawn has not risen. Attribution scope and support-edge target point to corrected claim. Original incomplete fields remain in preserved superseded records.',replacement_ids=[k for k in sorted(added) if k.startswith('bk.opening.')]),
 dict(id='BR-QUESTION-002',initial_state='unresolved_representation_alternative',verification='RESTRICTION_VERIFIED_NULL_QUESTION_LINKS',evidence=[source_span(5,9),source_span(5,10),source_span(5,13)],explanation='Three/four count positions retain proper holders and claim references. Both question_id fields are null, and q11/q14 why-question links removed. Source contains a comparable count disagreement, but no new editorial count question or qualified QA answer set is asserted. Historical discourse-association alternative preserved.',replacement_ids=[k for k in sorted(added) if '.p10' in k]),
 dict(id='BR-EDGE-003',initial_state='unresolved_supported_alternatives',verification='ALTERNATIVES_AND_RESTRICTION_PRESERVED_NOT_ADJUDICATED',evidence=[source_span(5,13),source_span(5,14),source_span(5,15)],explanation='Both readings undermine necessity of four-watch inference by alternative interpretation; objection versus qualification remains a supported labeling difference. Edges retain original direction and objection label, adding explicit qualification alternative and prohibition on demanding edge-label eligibility before adjudication. No retraction or exact-label agreement claimed.',replacement_ids=[k for k in sorted(added) if '.e15' in k or '.e16' in k])]
out=dict(artifact_type='nonblind_correction_verification',created='2026-11-26',agent='/root/source_reader_20261126',tractate='Berakhot',source_only=False,exposure_statement='Nonblind correction check: read existing independent first reading, comparison, verdict, producer correction proposal and old/new snapshots before source verification. Does not enlarge or reclassify the initial blind reading. Ketubot labels were not accessed.',status='BOUNDED_CORRECTION_VERIFIED_WITH_EDGE_ALTERNATIVE_UNRESOLVED',snapshot_sha256=newh,prior_snapshot_sha256=oldh,proposal_sha256=proph,artifact_hashes=hashes,findings=findings,mechanical_checks=dict(source_hash_verified=True,inventory_rows_exact=len(inventory),all_snapshot_evidence_spans_verified=span_count,original_record_ids_preserved=len(om),new_record_ids=len(added),original_record_contents_preserved=True,original_changes_only_release_state=True,replacement_lineage_valid=True,active_reference_to_replaced_records=stale,coverage_record_references_valid=True,coverage_layer_state_result_pairs_unchanged=True,completed_claim_pass_segments_before=71,completed_claim_pass_segments_after=71,all_snapshot_records_ml_eligible_false=True,snapshot_ml_eligible_false=True,proposal_history_preserved=True),coverage_statement='No new independently blind source cores or extraction coverage; this is a targeted nonblind verification of three existing findings. Original reviewed batch and full-tractate limitations remain.',preservation=dict(original_reading_hash_unchanged=True,original_comparison_hash_unchanged=True,old_snapshot_hash_unchanged=True,prior_initial_findings_retained=True,ketubot_frozen_reading_untouched=True),limitations=['Not full required review, probability-sample completion, tractate admission, or human certification.','This verifies authoritative snapshot dependencies and coverage references, not an independently regenerated exported reader or downstream task view. All ML eligibility stays false.','BR-EDGE-003 remains unresolved and cannot enter demanding edge-label evaluation without adjudication.','Original REWORK_TARGETED report retained as historical verdict; this bounded event does not retroactively rewrite it.'],human_certification=False,whole_tractate_admission=False,new_task_eligible_records=0)
# Recheck all hashed inputs after computation; never mutate production.
for p,h in hashes.items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
p=root/'berakhot_1cb99b65_correction_verification.json';assert not p.exists()
p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');h=hashlib.sha256(p.read_bytes()).hexdigest()
(root/'berakhot_1cb99b65_correction_verification.sha256').write_text(h+'  '+p.name+'\n',encoding='ascii')
print(json.dumps(dict(path=str(p),sha256=h,checks=out['mechanical_checks']),indent=2))
