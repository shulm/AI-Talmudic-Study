import copy,json,sys
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;lane=out.parents[1];job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');base=runner.current(job)
assert runner.sha(runner.encoded(base))=='55ad0ef1292bac17b7d14cdd24337f609b6ebed5366aaa3420b0dbaeb1ae7e77';runner.authorize(job,'/root/lead_l01_l03',1);j,src=runner.load(job);s=list(src.values())[101]
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='/root/lead_l01_l03',epoch=1,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=[],coverage=[],open_tails=base['open_tails'])
ev=dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
p['records']=[dict(id='tam007fix.wood_q',layer='questions',evidence=[ev],content=dict(formulation='Are all woods fit for the arrangement, as asked in the repeated baraita?',question_origin='explicit',conditions=['Repeated baraita at29b6; earlier Mishnah question is a separate occurrence'],answer_set_status='partial'),links=[],uncertainty=[],origin='source_paraphrase'),dict(id='tam007fix.wood_answer',layer='edges',evidence=[ev],content=dict(source_id='tam007.wood_repeat',target_id='tam007fix.wood_q',relation='answer',explicitness='source_explicit'),links=['tam007.wood_repeat','tam007fix.wood_q'],uncertainty=[],origin='source_paraphrase')]
for cell in base['coverage']:
 if cell['segment_id']==s['id'] and cell['layer'] in ['questions','edges','reconciliation']:
  n={k:copy.deepcopy(v) for k,v in cell.items() if k!='proposal_execution'};n['record_ids'] += [r['id'] for r in p['records'] if cell['layer']=='reconciliation' or r['layer']==cell['layer']];n['extraction_result']='records_found';n['rationale']+=' T007-01 adds explicit repeated baraita question and existing-answer link; no new coverage.';p['coverage'].append(n)
runner.validate_apply(base,p,src,j);runner.immutable(out/'PROPOSAL.json',runner.encoded(p));runner.immutable(out/'LINEAGE.json',runner.encoded(dict(base_snapshot=runner.sha(runner.encoded(base)),review_verdict_sha256=runner.sha((lane/'tamid_next20_007_review_20261127/comparison/VERDICT.json').read_bytes()),new_rows=2,superseded=0,new_core_coverage=0,lexical_limitation='T007-02 remains a disclosed lexical interpretation limit; no contrary reading established.')))
print(runner.sha((out/'PROPOSAL.json').read_bytes()))
