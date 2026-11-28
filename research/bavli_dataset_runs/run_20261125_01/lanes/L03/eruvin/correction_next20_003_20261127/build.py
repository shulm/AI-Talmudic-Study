import copy,json,sys
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;lane=out.parents[1];job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin');base=runner.current(job)
assert runner.sha(runner.encoded(base))=='5b4f960d585e827735da16439a30e2218ea2378fc2fe1ed29e56225297b507c5';runner.authorize(job,'L03/eruvin',2);j,src=runner.load(job)
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/eruvin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=[],coverage=[],open_tails=base['open_tails'])
oid='er023.yehoshua.a';r={k:copy.deepcopy(v) for k,v in next(r for r in base['records'] if r['id']==oid).items() if k not in ['release_state','review_state','ml_eligible']};r.update(id='er023fix.yehoshua.a',supersedes=oid);r['content'].update(role='quoted_authority',scope='Anonymous Gemara identifies the choice position as Rabbi Yehoshua’s; Rabbi Yehoshua is not speaking directly in this sentence.');p['records']=[r]
for cell in base['coverage']:
 if oid in cell['record_ids']:
  n={k:copy.deepcopy(v) for k,v in cell.items() if k!='proposal_execution'};n['record_ids']=[r['id'] if x==oid else x for x in n['record_ids']];n['rationale']+=' ER003 role repair distinguishes anonymous attribution from direct speech.';p['coverage'].append(n)
runner.validate_apply(base,p,src,j);runner.immutable(out/'PROPOSAL.json',runner.encoded(p));runner.immutable(out/'LINEAGE.json',runner.encoded(dict(base_snapshot=runner.sha(runner.encoded(base)),review_verdict_sha256=runner.sha((lane/'eruvin_next20_003_review_20261127/comparison/VERDICT.json').read_bytes()),new_rows=1,superseded=1,new_core_coverage=0)))
print(runner.sha((out/'PROPOSAL.json').read_bytes()))
