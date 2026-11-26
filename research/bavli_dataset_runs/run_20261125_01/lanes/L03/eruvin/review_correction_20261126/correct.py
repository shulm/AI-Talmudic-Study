"""Source-checked doorway reading linkage; no new coverage or acceptance."""
import sys,json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[7];sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
OUT=Path(__file__).parent;JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin')
base='4ce45b2ad3cccff73f11ce5fd4a2a59b41550959f029b587d33e20f22c42c042';s=runner.current(JOB);assert runner.sha(runner.encoded(s))==base
j,ss=runner.load(JOB);runner.authorize(JOB,'L03/eruvin',2)
root=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
inputs=[('comparison_frozen.json','comparisons/eruvin_batch001_exact_version.json','019e1b313538c18de5ee3c10a48684f9013a70fefd7fc6b26904789f8404e115'),('verdict_frozen.json','verdicts/eruvin_batch001_v2_verdict.json','0a4c23c83ea42cd84fd9c4f452f8558e54eab1a908f438857dc7412aa2950b5f'),('reader_frozen.json','readings/eruvin_batch001.json','54b0d0919bbfd68d73e0a407a7764102958a157f9f45382a96c12a01dc642c4e')]
for name,path,h in inputs:
 b=(root/path).read_bytes();assert runner.sha(b)==h;runner.immutable(OUT/name,b)
old={r['id']:r for r in s['records'] if r['release_state']=='valid'};new=[];rev={}
claim='er.opening.001.width.form';position='er.opening.001.p.width.form';correction='er.objections.001.claims.form.rav.correction'
def revise(oid):
 r=copy.deepcopy(old[oid])
 for k in ['release_state','review_state','ml_eligible']:r.pop(k,None)
 r['id']='er.review20261126.'+oid;r['supersedes']=oid;rev[oid]=r['id'];new.append(r);return r
r=revise(claim)
r['content']['scope']='Printed opening Mishnah reading at 2a:2. Rav’s reported instruction at 2b:15 gives the contrary wording צריך למעט; preserve both textual readings, not a universal settled ruling.'
r['links']=[correction];r['uncertainty'].append('Opening printed exception conflicts with Rav’s reported teaching correction at 2b:15; neither reading is silently overwritten.')
r=revise(position);r['content']['claim_id']=rev[claim];r['content']['local_status']='Printed anonymous Mishnah reading; Rav’s distinct reported correction at 2b:15 requires reduction. This position is not a universal settled outcome.';r['links']=[rev[claim],correction];r['evidence']+=copy.deepcopy(old[correction]['evidence']);r['uncertainty'].append('Retrieve with Rav’s separately attributed correction; do not infer that the printed Mishnah was erased.')
r=revise('er.opening.001.e.width.exception');r['content']['source_id']=rev[claim];r['links']=[rev[claim],'er.opening.001.width.reduce'];r['uncertainty'].append('Qualification belongs to the printed opening reading; Rav’s contrary teaching is linked separately.')
new.append(dict(id='er.review20261126.reported_textual_correction',layer='edges',evidence=copy.deepcopy(old[correction]['evidence']),content=dict(source_id=correction,target_id=rev[claim],relation='correction',explicitness='source_explicit'),links=[correction,rev[claim]],origin='source_paraphrase',uncertainty=['A reported textual correction by Rav in the teaching scene, not a global replacement or final halachic ruling. Rav Yehuda teaches Hiyya bar Rav before Rav.']))
active=[r for oid,r in old.items() if oid not in rev]+new;affected={e['segment_id'] for r in new for e in r['evidence']};coverage=[]
for cell in s['coverage']:
 if cell['segment_id'] not in affected:continue
 c=copy.deepcopy(cell);c.pop('proposal_execution',None);c['record_ids']=[r['id'] for r in active if (c['layer']=='reconciliation' or r['layer']==c['layer']) and any(e['segment_id']==c['segment_id'] for e in r['evidence'])];c['extraction_result']='records_found' if c['record_ids'] else 'none_found_after_pass';c['rationale']='Targeted source reread links printed 2a:2 doorway exception to Rav’s contrary wording in 2b:15; preserves distinct attribution, recipient and local status. No new coverage.';coverage.append(c)
p=dict(schema_version=runner.VERSION,tractate=j['tractate'],owner='L03/eruvin',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=new,coverage=coverage,open_tails=s['open_tails'])
runner.validate_apply(s,p,ss,j);runner.immutable(OUT/'proposal.json',runner.encoded(p));result=runner.submit(JOB,OUT/'proposal.json','L03/eruvin',2);replay=runner.replay(JOB);assert all(x==110 for x in replay['completed_by_layer'].values())
final={r['id']:r for r in runner.current(JOB)['records'] if r['release_state']=='valid'}
assert correction in final[rev[claim]]['links'] and correction in final[rev[position]]['links'];assert final[correction]==old[correction]
export=JOB.parent/'er_export_review_20261126_001';runner.export(JOB,export);m=json.loads((export/'MANIFEST.json').read_text())
for f,h in m['files'].items():assert runner.sha((export/f).read_bytes())==h
comparison=json.loads((OUT/'comparison_frozen.json').read_text())
response=dict(status='PRODUCER_CORRECTION_PENDING_INDEPENDENT_VERIFICATION',base_snapshot=base,**result,revision_map=rev,new_records=len(new),superseded=len(rev),comparison_sha256=inputs[0][2],verdict_sha256=inputs[1][2],reader_sha256=inputs[2][2],disposition={'ER-WIDTH-CONTEXT':'Opening claim and position explicitly link unchanged Rav correction; position status distinguishes printed Mishnah from reported contrary wording. Added reported textual correction edge and revised printed-reading qualification dependency.'},regression_checks={'opening_retrieval_links_correction':True,'position_retrieval_links_correction':True,'reported_correction_preserved_exactly':True,'coverage_unchanged':True},reader_corrections_preserved=comparison['reader_corrections'],uncertainties_preserved=comparison['uncertainties_preserved'],limits=['Ten opening cores compared; twenty probability cores still unprocessed','No whole-tractate admission or independent correction acceptance','No new source coverage or task qualification'],export_manifest_path=str(export/'MANIFEST.json'),export_manifest_sha256=runner.sha((export/'MANIFEST.json').read_bytes()))
runner.immutable(OUT/'RESPONSE.json',runner.encoded(response));runner.immutable(OUT/'replay.json',runner.encoded(replay));print(json.dumps(dict(snapshot=result['snapshot_sha256'],proposal=result['proposal_sha256'],receipt=runner.sha((OUT/'RESPONSE.json').read_bytes())),indent=2))
