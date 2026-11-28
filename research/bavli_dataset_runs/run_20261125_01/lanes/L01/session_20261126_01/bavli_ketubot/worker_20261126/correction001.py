from pathlib import Path
import sys
sys.path.insert(0,'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1')
import runner as r
out=Path(__file__).parent;job=out.parent;review=job.parent/'review/source_only_20261126'
expected='72d359ca695d32950f278848c8cf05592a497d4768b08badab9730fe8885b2b1'
comparison_sha='02a60854f3ef474d5b37924caef3a3bfec0f062ac754008251f5edb106dad486'
verdict_sha='e210a56a06da0b163314b5e162d5e4e1e2607b9969ea3b1f26f6cfd6309878c7'
assert r.sha((review/'ketubot_72d359ca_comparison.json').read_bytes())==comparison_sha
assert r.sha((review/'ketubot_72d359ca_verdict.json').read_bytes())==verdict_sha
j,segs=r.load(job);state=r.current(job);assert r.sha(r.encoded(state))==expected
r.authorize(job,'/root/ketubot_resume',3)
records=[];coverage=[];decisions=[]
for finding,ref,quote,source,target,key,note in [
 ('K3B-G1','Ketubot 3b:1','ותנשא באחד בשבת ואם היה לו טענת בתולים היה משכים לב"ד','kt.resume26.b1.q.sunday','kt.resume26.b1.c.court','sunday_court','The Sunday proposal challenges the sufficiency of the court rationale for choosing Wednesday, not the factual possibility of Wednesday court access. The later composite preparation answer is not the objection endpoint.'),
 ('K3B-G2','Ketubot 3b:8',"בג' מיהא לכנוס",'kt.resume26.b2.q.tuesday','kt.resume26.b2.c.stays','tuesday_stays','The Tuesday proposal challenges the sufficiency of the staying-commander explanation for marrying as early as Monday; the entourage answer remains separately encoded.')]:
  s=next(x for x in segs.values() if x['ref']==ref);start=s['text'].index(quote)
  rid='kt.resume26.corr1.e.'+key
  records.append(dict(id=rid,layer='edges',evidence=[dict(segment_id=s['id'],start_char=start,end_char=start+len(quote),quote=quote)],content=dict(source_id=source,target_id=target,relation='objection',explicitness='source_explicit'),origin='source_paraphrase',uncertainty=[],links=[source,target]))
  for layer in ['edges','reconciliation']:
   old=next(c for c in state['coverage'] if c['segment_id']==s['id'] and c['layer']==layer)
   c={k:v for k,v in old.items() if k!='proposal_execution'}
   if layer=='edges':c['record_ids']=old['record_ids']+[rid];c['extraction_result']='records_found'
   c['rationale']='Bounded source reinspection for '+finding+' after frozen comparison '+comparison_sha+': previously omitted directed challenge added as '+rid+'. Existing source/claim/question/answer rows preserved. '+note
   coverage.append(c)
  decisions.append(dict(finding_id=finding,status='supported_graph_omission_corrected_pending_independent_verification',new_record_id=rid,endpoint_rationale=note,source_ref=ref))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=state['open_tails'])
r.validate_apply(state,p,segs,j);path=out/'correction001_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch'])
r.immutable(out/'correction001_receipt.json',r.encoded(receipt))
replay=r.replay(job);r.immutable(out/'correction001_replay.json',r.encoded(replay))
ex=r.export(job,out/'export_68_corrected')
decision=dict(original_snapshot_sha256=expected,corrected_snapshot_sha256=receipt['snapshot_sha256'],comparison_sha256=comparison_sha,verdict_sha256=verdict_sha,decisions=decisions,scope='Two directed relation additions only; zero source expansion, unchanged 68 completed segments per layer.',qualification='Initial independent review covers 9 source cores only; corrections await exact-version verification. No full-tractate, probability-sample, human-certification or ML-eligibility claim.')
r.immutable(out/'correction001_decisions.json',r.encoded(decision))
resume=r.read(out/'RESUME_68.json');resume.update(snapshot_sha256=receipt['snapshot_sha256'],supersedes_resume_sha256=r.sha((out/'RESUME_68.json').read_bytes()),bounded_correction=decision,export_manifest_sha256=r.sha((out/'export_68_corrected/manifest.json').read_bytes()),replay_sha256=r.sha((out/'correction001_replay.json').read_bytes()),stopped_reason='Bounded review corrections completed; no further production expansion authorized in this worker turn.')
resume['proposals']=resume['proposals']+[dict(file=path.name,sha256=receipt['proposal_sha256'])]
resume['qualifications']['independent_review_of_new_scope']='Nine cores 3b:1–9 compared against predecessor; two graph corrections awaiting independent verification; other new cores unreviewed.'
r.immutable(out/'RESUME_68_corrected.json',r.encoded(resume))
files={p.relative_to(out).as_posix():r.sha(p.read_bytes()) for p in sorted(out.rglob('*')) if p.is_file() and p.name!='HASHES_68_corrected.json'}
r.immutable(out/'HASHES_68_corrected.json',r.encoded(dict(snapshot_sha256=receipt['snapshot_sha256'],files=files)))
print(dict(snapshot_sha256=receipt['snapshot_sha256'],proposal_sha256=receipt['proposal_sha256'],replay_pass=replay['replay_pass'],resume_sha256=r.sha((out/'RESUME_68_corrected.json').read_bytes()),manifest_sha256=r.sha((out/'HASHES_68_corrected.json').read_bytes()),export_manifest_sha256=resume['export_manifest_sha256'],decisions_sha256=r.sha((out/'correction001_decisions.json').read_bytes())))
