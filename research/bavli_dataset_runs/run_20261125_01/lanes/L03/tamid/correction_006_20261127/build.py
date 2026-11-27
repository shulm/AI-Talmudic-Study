import copy,json,sys
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;lane=out.parents[1];job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');base=runner.current(job)
assert runner.sha(runner.encoded(base))=='ba1f70d54bbedde5f67dd7abae5927dee2afdfb0dfbe50dea41d556d7c278995';runner.authorize(job,'/root/lead_l01_l03',1);j,src=runner.load(job)
old={r['id']:r for r in base['records'] if r['release_state']=='valid'}
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='/root/lead_l01_l03',epoch=1,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=[],coverage=[],open_tails=base['open_tails'])
repl={};uncertainty='Pinned witness prints abbreviated א"ר יהודה. Rav/Rabbi expansion is not independently established here; preserve the local name and uncertainty rather than selecting an expanded identity.'
def clean(r):return {k:copy.deepcopy(v) for k,v in r.items() if k not in ['release_state','review_state','ml_eligible']}
for key in ['hot_water','hot_water.p','yehuda.a','u78','frame78']:
 oid='tam006.'+key;r=clean(old[oid]);r.update(id='tam006fix.'+key,supersedes=oid);r['uncertainty'].append(uncertainty);c=r['content']
 if key=='hot_water':c['proposition']='The speaker printed as א"ר יהודה explains the earlier action as heating water for the scalding preparation.'
 if key=='hot_water.p':c['holder_candidates']=['יהודה (abbreviated א"ר יהודה; title unresolved)']
 if key=='yehuda.a':c['surface']='א"ר יהודה';c['candidates']=['יהודה (title unresolved)'];c['scope']='Heating-water answer with unexpanded local abbreviation; no external identity pin supplied'
 for k,v in list(c.items()):
  if isinstance(v,str):c[k]=v.replace('Rav Yehuda hot-water answer','א"ר יהודה hot-water answer (title unresolved)')
 repl[oid]=r['id'];p['records'].append(r)
def remap(v):
 if isinstance(v,str):return repl.get(v,v)
 if isinstance(v,list):return [remap(x) for x in v]
 if isinstance(v,dict):return {k:remap(x) for k,x in v.items()}
 return v
while True:
 changed=False
 for oid,r in old.items():
  if oid in repl:continue
  if remap(r['links'])!=r['links'] or remap(r['content'])!=r['content']:
   n=clean(r);n.update(id='tam006fix.dep.'+oid,supersedes=oid);repl[oid]=n['id'];p['records'].append(n);changed=True
 if not changed:break
for r in p['records']:r['links']=remap(r['links']);r['content']=remap(r['content'])
live={rid:r for rid,r in old.items() if rid not in repl};live.update({r['id']:r for r in p['records']})
for cell in base['coverage']:
 ids=sorted(rid for rid,r in live.items() if (cell['layer']=='reconciliation' or r['layer']==cell['layer']) and any(e['segment_id']==cell['segment_id'] for e in r['evidence']))
 if set(ids)!=set(cell['record_ids']) or 'Rav Yehuda hot-water' in cell['rationale']:
  n={k:copy.deepcopy(v) for k,v in cell.items() if k!='proposal_execution'};n.update(record_ids=ids);n['rationale']=n['rationale'].replace('Rav Yehuda hot-water answer','א"ר יהודה hot-water answer (title unresolved)')+' T006-01 preserves raw abbreviation and discloses unresolved expansion. No new core coverage.';p['coverage'].append(n)
runner.validate_apply(base,p,src,j);runner.immutable(out/'PROPOSAL.json',runner.encoded(p));runner.immutable(out/'LINEAGE.json',runner.encoded(dict(base_snapshot=runner.sha(runner.encoded(base)),finding_sha256=runner.sha((lane/'tamid_next20_006_review_20261127/comparison/FINDING_ATTRIBUTION.json').read_bytes()),replacements=repl,new_rows=len(p['records']),new_core_coverage=0,source_sha256=j['source_sha256'],owner=runner.read(job/'OWNER.json'))))
print(json.dumps(dict(proposal=runner.sha((out/'PROPOSAL.json').read_bytes()),rows=len(p['records']),superseded=len(repl))))
