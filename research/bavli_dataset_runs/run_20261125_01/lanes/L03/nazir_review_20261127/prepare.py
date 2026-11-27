import json,hashlib
from pathlib import Path
OUT=Path(__file__).parent
R=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/readings/nazir_batch001.json')
sha=lambda b:hashlib.sha256(b).hexdigest()
RH='889d6858cc400a0ea3e3dd70d4615adf4f62b46707353b3e81bcf735c14de52c'
assert sha(R.read_bytes())==RH
d=json.loads(R.read_text(encoding='utf-8'))
for pin in [d['source'],d['original_source_schema'],d['frozen_plan']]+d['common_documents']:
 assert sha(Path(pin['path']).read_bytes())==pin['sha256']
t=json.loads(Path(d['source']['path']).read_text(encoding='utf-8'))['text']
evidence=[]
for i in range(2,6):
 for j,s in enumerate(t[i]):
  if i==5 and j>=8:break
  evidence.append({'ref':f'Nazir {i//2+1}{"a" if i%2==0 else "b"}:{j+1}','source_index':[i,j],'text':s,'role':'core' if i==2 and j<10 else 'context'})
out={'artifact_kind':'comparator_source_preparation_before_producer_access','reviewer':'/root/rosh_hashanah','prior_exposure':'No Nazir production authored or viewed. Existing frozen central reader read before this preparation; no new blind-cohort claim. Comparator will be nonblind comparison of that separately frozen source-first reading.','reader_path':str(R),'reader_sha256':RH,'source':d['source'],'core_refs':d['core_refs'][:10],'other_frozen_cores_pending_production':d['core_refs'][10:],'source_evidence':evidence,'independent_checks_to_apply':['Preserve nine individual formulas at 2a:2, not one generic formula claim. Aha requires passing nazir and intended personal naziriteship; aha naeh, mesalsel and mekhalkel require holding hair; like this requires passing nazir. Conditions established in context do not count as new production cores.','Separate R. Meir and Sages on birds. Preserve distinct Resh Lakish adjacency explanation and R. Yohanan concern plus passing pure nazir qualifications; no falsely universal birds undertaking.','Rava or Kedi variant remains uncertain attribution; no Rav-versus-Shmuel dispute from the unrelated lexical Rav report at3a:5.','The 2a:8 last-mentioned-first explanation is initial. Counterexamples2a:11–12 and2a:13 show no universal order;2b:2–3 gives dearer derived handles versus principal opening. Supporting examples remain true even when proposed universal inference fails.','Repeated aha at2a:2 and2a:7 are distinct occurrences;2a:7 reconstruction is not silently substituted into original source.','Wine/sotah rationale is source discourse, not an externally established causal or normative claim.'],'reader_caveats':['c013 is an explicit question, c016 an objection; do not force both into asserted claims.','c011/c012 holder lists contain both sides; propositions correctly distinguish them. Keep narrow named attribution.','c002–c010 generic conditions field does not encode actual continuation conditions; comparator must inspect source and producer conditions independently.'],'status':'SOURCE_PREPARED_WAITING_FOR_PROMOTED_PIN','qualification':{'ml_eligible':False,'new_blind_cohort':False}}
b=json.dumps(out,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
p=OUT/'SOURCE_PREPARATION.json'
if p.exists():assert p.read_bytes()==b
else:p.write_bytes(b)
print(json.dumps({'reader_sha256':RH,'source_preparation_sha256':sha(b),'core_segments':10,'context_segments':len(evidence)-10}))
