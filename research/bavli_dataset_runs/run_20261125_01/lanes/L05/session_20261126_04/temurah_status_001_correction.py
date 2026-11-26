"""Bounded reviewer-requested correction; no new source coverage."""
import copy,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_temurah')
REVIEW=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
bindings=[(REVIEW/'verdicts/temurah_batch001_v2_verdict.json','f3966a45abaf547fde32914d77b8e473b5652d1feeda45161d55393ebd69c37e'),(REVIEW/'comparisons/temurah_batch001_exact_version.json','38fd3353a4635d764a9d13887a5dbeb60ce9c5d244741b4fd809c2816e051d11')]
for p,h in bindings:assert hashlib.sha256(p.read_bytes()).hexdigest()==h
assert json.loads((JOB/'OWNER.json').read_text())=={'owner':'L05/temurah','epoch':2}
oldhash='7d4de3664fbc1bdf7ce11b65101c779855788ef7521677f0091d113963ed0ec2'
state=json.loads((JOB/'snapshots'/f'{oldhash}.json').read_text(encoding='utf-8'))
assert hashlib.sha256((JOB/'snapshots'/f'{oldhash}.json').read_bytes()).hexdigest()==oldhash
inv=json.loads((JOB/'source_inventory.json').read_text(encoding='utf-8'));meta=json.loads((JOB/'JOB.json').read_text())
byid={r['id']:r for r in state['records']}
def ev(ii):return [dict(segment_id=inv[i]['id'],start_char=0,end_char=len(inv[i]['text']),quote=inv[i]['text']) for i in ii]
def revise(k):
 r={a:copy.deepcopy(b) for a,b in byid[k].items() if a not in ['release_state','review_state','ml_eligible']}
 r['id']=k+'_review001_v2';r['supersedes']=k;r['evidence']=ev([40,65,66,67,68,69,70,71]);return r
c=revise('tem_open_c_c40c')
c['content']=dict(proposition='Rabbi Yose son of Rabbi Hanina’s addition concerning terumah before first fruits is finally interpreted as an exemption from lashes, not an additional liability exception.',conditions=['Terumah separated before first fruits'],scope='Final contextual interpretation of Temurah 3a:18 at 4a:4–4b:1: the first proposed liability assignment is overturned by the second proof assigning liability to Rabbi Elazar; 4a:9 and 4b:1 complete the exemption reading.',assertion_mode='reconciled')
c['uncertainty']=['The initial liability reading is preserved separately as a rejected provisional inference; final names follow the continuation, not their order in חד אמר.']
p=revise('tem_open_pc_c40c');p['content'].update(claim_id=c['id'],conditions=['Terumah separated before first fruits'],local_status='Final contextual exemption from lashes after reversal of initial assignment; no liability position inferred from name order.');p['links']=[c['id']]
a=revise('tem_open_c_a40h2');a['content']['scope']='Quoted Rabbi Yose son of Rabbi Hanina: phrase אף המקדים תרומה לביכורים ultimately attaches to the exemption rule, as resolved by אפטורא קאי at 4b:1 after the 4a:5–7 proof.'
initial=dict(id='tem_status001_initial_liability_inference',layer='claims',evidence=ev([40,65]),content=dict(proposition='The first inference tentatively identifies Rabbi Yose son of Rabbi Hanina as the one imposing lashes, based on reading his addition as liability.',conditions=['Terumah separated before first fruits','First proposed resolution of unnamed חד אמר alternatives'],scope='Provisional inference at 4a:4, overturned at 4a:5–7 and reinterpreted at 4a:9–4b:1.',assertion_mode='rejected'),origin='source_paraphrase',uncertainty=[],links=[])
initial_p=dict(id='tem_status001_initial_liability_position',layer='positions',evidence=ev([40,65]),content=dict(holder_candidates=['Rabbi Yose son of Rabbi Hanina'],claim_id=initial['id'],question_id=None,conditions=['Terumah separated before first fruits'],local_status='Provisional attribution in the first inference; rejected by subsequent proof, not the final held position.'),origin='source_paraphrase',uncertainty=[],links=[initial['id']])
pair=dict(id='tem_status001_final_pairing',layer='claims',evidence=ev([40,65,66,67,68,69,70,71]),content=dict(proposition='The second proof identifies Rabbi Elazar as imposing lashes and Rabbi Yose son of Rabbi Hanina as exempting; the latter’s earlier addition is consequently read as referring to exemption.',conditions=['Terumah before first fruits dispute','Attribution established by Rabbi Elazar’s explicit ruling in the two-basket analogy'],scope='Context for correcting the completed 3a:18 core; not a completed extraction pass over 4a:4–4b:1.',assertion_mode='reconciled'),origin='source_paraphrase',uncertainty=[],links=[])
edge=dict(id='tem_status001_attribution_reversal',layer='edges',evidence=ev([40,65,66,67,68,69,70,71]),content=dict(source_id=pair['id'],target_id=initial['id'],relation='correction',explicitness='source_explicit'),origin='source_paraphrase',uncertainty=[],links=[pair['id'],initial['id']])
records=[c,p,a,initial,initial_p,pair,edge]
mapping={r['supersedes']:r['id'] for r in records if r.get('supersedes')}
# Existing graph has only the revised position depending on the corrected claim.
for r in state['records']:
 if r['release_state']=='valid' and r['id'] not in mapping:
  deps=r['links']+[r['content'][k] for k in ['claim_id','question_id','source_id','target_id'] if r['content'].get(k)]
  assert not set(deps)&set(mapping),(r['id'],deps)
coverage=[]
sid=inv[40]['id']
for old in state['coverage']:
 if old['segment_id']!=sid or old['layer'] not in ['claims','positions','attributions','edges','reconciliation']:continue
 cc={k:copy.deepcopy(v) for k,v in old.items() if k!='proposal_execution'}
 cc['record_ids']=[mapping.get(i,i) for i in cc['record_ids']]
 for r in records:
  if not r.get('supersedes') and (cc['layer']=='reconciliation' or cc['layer']==r['layer']):cc['record_ids'].append(r['id'])
 cc['extraction_result']='records_found' if cc['record_ids'] else 'none_found_after_pass'
 cc['rationale']+=' Targeted review temurah_status_001: reread 3a:18 and full 4a:4–4b:1 continuation; preserved provisional liability inference and final exemption after reversal. Context-only evidence adds zero completed segments.'
 coverage.append(cc)
proposal={k:meta[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']}
proposal.update(owner='L05/temurah',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=records,coverage=coverage,open_tails=state['open_tails'])
out=HERE/'temurah_status_001_proposal.json';blob=(json.dumps(proposal,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
if out.exists():assert out.read_bytes()==blob
else:out.write_bytes(blob)
print(json.dumps(dict(path=str(out),sha256=hashlib.sha256(blob).hexdigest(),records=len(records),coverage_updates=len(coverage),new_completed_segments=0)))
