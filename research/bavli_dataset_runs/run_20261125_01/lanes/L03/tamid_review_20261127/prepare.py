import json,hashlib
from pathlib import Path
OUT=Path(__file__).parent
R=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/readings/tamid_batch001.json')
sha=lambda b:hashlib.sha256(b).hexdigest()
RH='6c18c9845856d5c04b2e57c0770d79e4a054137abd13eadcaec8264ad3bdc3db'
assert sha(R.read_bytes())==RH
d=json.loads(R.read_text(encoding='utf-8'))
for pin in [d['source'],d['original_source_schema'],d['frozen_plan']]+d['common_documents']:
 assert sha(Path(pin['path']).read_bytes())==pin['sha256']
t=json.loads(Path(d['source']['path']).read_text(encoding='utf-8'))['text']
evidence=[]
for i in range(49,55):
 for j,s in enumerate(t[i]):
  if i==54 and j>=10:break
  ref=f'Tamid {i//2+1}{"a" if i%2==0 else "b"}:{j+1}'
  evidence.append({'ref':ref,'source_index':[i,j],'text':s,'role':'core' if ref in d['core_refs'][:10] else 'context'})
out={'artifact_kind':'comparator_source_preparation_before_producer_access','reviewer':'/root/rosh_hashanah','prior_exposure':'No Tamid production authored or viewed. Existing frozen central reader read before this preparation; no new blind-cohort claim. Comparator is nonblind comparison of separately frozen source-first reading.','reader_path':str(R),'reader_sha256':RH,'source':d['source'],'core_refs':d['core_refs'][:10],'other_frozen_cores_pending_production':d['core_refs'][10:],'source_evidence':evidence,'independent_checks_to_apply':['Preserve raw page49 index for25b; do not count prior empty pages as shifted references.25b3 emission exit continues26a1 below the complex.','Distinct three guard locations, chambers, age distinction, keys and clothing practices; passage/privacy signs and temporal exit after gates open should remain recoverable separately.','Garments under heads is original Mishnah wording, not silently changed.27a15 blocks inference from sleep versus walking;27a16 against heads reading;27b3 mixed fabrics even under ten layers;27b4 alternatives nonmixed garments and Rav Ashi stiff fabric argument with Rav Huna son of Rav Yehoshua support;27b5 ultimately permits benefit within Temple, not outside. Do not turn provisional objection into final universal ban or erase alternatives.','26a3 early immersion and26a4 lottery remain source occurrences;28a6 Abaye separates before/after enactment whereas28a10 Rava reads both after enactment, first clause as desire to enter lottery. Initial apparent no-lottery inference is not retained as universal rule.','26a5 Abaye scriptural derivation,26a6 anonymous objection,26a7 anonymous separated Moses/Aaron-and-sons reading; through26a10 Rav Ashi alternative repeated guarding lexemes, not named Rav. Preserve open discussion at core end.','Core26a3 explicit timing question and26a5 source question must be represented.26a6 objection can be typed question/utterance without false positive assertion.'],'reader_caveats':['Reader c004/c016/c017/c020/c026 combine independently testable details; compare each component rather than treating broad row match as completeness.','Reader generic conditions fields insufficient for the garment and lottery continuations; independently audit producer context qualifications.','First10 are endpoint only. Other20 frozen cores pending production, even when read here as context; no review-core credit.'],'status':'SOURCE_PREPARED_WAITING_FOR_PROMOTED_PIN','qualification':{'ml_eligible':False,'new_blind_cohort':False}}
b=json.dumps(out,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
p=OUT/'SOURCE_PREPARATION.json'
if p.exists():assert p.read_bytes()==b
else:p.write_bytes(b)
print(json.dumps({'reader_sha256':RH,'source_preparation_sha256':sha(b),'core_segments':10,'context_segments':len(evidence)-10}))
