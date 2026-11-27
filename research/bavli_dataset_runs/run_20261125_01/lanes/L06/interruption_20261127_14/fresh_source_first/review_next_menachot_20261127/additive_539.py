import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
p=Path(__file__).parent
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
old_manifest='889e6d5ced7d2250b1fb5b1c8a3375ed9e485609f5f2919c4739ad9508d5836f'
old_reading='c88f15ee93c815ca76e67a66258890659aace14bb86f0af81a9885cfad265e6c'
assert sha(p/'FROZEN_MANIFEST.json')==old_manifest
assert sha(p/'SOURCE_READING.json')==old_reading
prov=json.loads((p/'PROVENANCE.json').read_text(encoding='utf8'))
src=Path(prov['source_path']); assert sha(src)==prov['source_sha256']
t=json.loads(src.read_text(encoding='utf8'))['text'][31][28]
def ev(a=0,b=None):
 b=len(t) if b is None else b
 return dict(ref='Menachot 16b:29',raw_index=539,json_index=[31,28],start_char=a,end_char=b,quote=t[a:b])
def phrase(s):
 a=t.index(s);return ev(a,a+len(s))
def save(name,data):
 f=p/name;assert not f.exists(),f
 f.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
b=t.index(' ומ"ד פסול');c=t.index(' ומאן דאמר כשר')
groups=[('piggul',0,b),('invalid',b,c),('valid',c,len(t))]
claims=[
 ('c539-p-eat','The piggul opinion considers this normal eating.','דרך אכילה בכך','piggul',False),
 ('c539-p-burn','The piggul opinion considers this normal burning.','ודרך הקטרה בכך','piggul',False),
 ('c539-i-eat','The invalid opinion’s eating premise is printed with parenthetical negation; preserve it without resolving the textual alternative.','(אין) דרך אכילה בכך','invalid',True),
 ('c539-i-burn','The invalid opinion considers this not normal burning.','ואין דרך הקטרה בכך','invalid',False),
 ('c539-i-result','For the invalid opinion, it is like a meal offering that was not burned.','והואי לה כמנחה שלא הוקטרה','invalid',False),
 ('c539-v-burn','The valid opinion considers this normal burning.','דרך הקטרה בכך ואין דרך אכילה בכך:','valid',False),
 ('c539-v-eat','The valid opinion considers this not normal eating.','ואין דרך אכילה בכך','valid',False)]
records=[]
for ident,prop,quote,slot,uncertain in claims:
 evidence=phrase(quote)
 if ident=='c539-v-burn':
  a=t.index('דרך הקטרה בכך',c);evidence=ev(a,a+len('דרך הקטרה בכך'))
 records.append(dict(id=ident,evidence=evidence,proposition=prop,conditions=['Repeated sesame-sized burning and thought until the entire handful is finished (16b:23).'],scope=slot,assertion_mode='asserted as anonymous rationale',origin='source_paraphrase',uncertainty=['Parenthetical אין: edition typography retained; no external witness checked.'] if uncertain else []))
inventory=dict(kind='additive independent SOURCE-ONLY completion',authorization='Lead explicitly promoted exactly539 to core; original20-core freeze remains immutable.',producer_material_accessed=False,source_sha256=sha(src),core_added=[539],aggregate_core_count=21,aggregate_core_range=[519,539],aggregate_context_only_count=47,context_promotion='539 removed from context-only count, no duplicate core/context counting',evidence=ev(),structure=dict(primary_partition=[dict(slot=s,evidence=ev(a,z)) for s,a,z in groups],boundary='closed',rationale='Three rationales finish the preceding three-opinion reformulation; closing colon precedes new אמרי unit at16b:30.'),utterances=[dict(slot=s,textual_voice='anonymous expositor of unnamed '+s+' opinion',composition='composite',discourse_role='causal explanation introduced by קסבר',evidence=ev(a,z)) for s,a,z in groups],claims=records,attributions=[dict(slot=s,role='position_holder',surface='מאן דאמר '+{'piggul':'פיגול','invalid':'פסול','valid':'כשר'}[s],holder_candidates=['רב חסדא','רב המנונא','רב ששת'],assignment='unresolved; no ordering inference',evidence=ev(a,z)) for s,a,z in groups],questions=dict(explicit_questions=[],rationale='No explicit new question in this segment; answers the explanation needed after16b:28.',editorial_question='How can each of the three outcomes be compatible with all tannaitic positions?',origin='editorial_reconstruction'),positions=[dict(slot=s,claim_ids=[r['id'] for r in records if r['scope']==s],local_status='anonymous explanation retained; no named assignment or retraction',evidence=ev(a,z)) for s,a,z in groups],edges=[dict(relation='support',from_claims=[r['id'] for r in records if r['scope']==s],to='review-538 '+s+' branch',explicitness='source_explicit causal קסבר; target branch editorial indexing',evidence=ev(a,z)) for s,a,z in groups]+[dict(relation='analogy',from_claim='c539-i-result',to='meal offering not burned',explicitness='source_explicit כמנחה',evidence=phrase('והואי לה כמנחה שלא הוקטרה'))],omission_reconciliation=dict(pass_completed=True,items=['All three outcomes and their independent universality claims retained.','Eating and burning premises separated; invalid-offering analogy retained.','Parenthetical negation preserved rather than normalized.','Repeated normal-burning premises in piggul and valid opinions retained as separate occurrences.','No new named transmitter, explicit question, retraction, or attribution resolution occurs.','Each branch says דברי הכל under its own premises; this is not agreement on all three incompatible verdicts.']),uncertainties=['Parenthetical negation in invalid branch unresolved across textual witnesses.','Named-holder assignment remains unresolved.'],first_reading_and_correction=dict(first_reading='539 was context-only in initial immutable freeze.',correction='Explicit lead scope extension promotes exactly539; no semantic reading or initial artifact is overwritten.'),next_boundary=dict(ref='Menachot 16b:30',raw_index=540,quote='אמרי',continuation='Menachot 17a:1'),actual_blockers=[],qualification='AI provisional; no human certification, whole-tractate completion, producer agreement, or eligibility claim')
def check(x):
 if isinstance(x,dict):
  if 'start_char' in x:assert t[x['start_char']:x['end_char']]==x['quote']
  for v in x.values():check(v)
 elif isinstance(x,list):
  for v in x:check(v)
check(inventory)
assert ''.join(t[a:z] for _,a,z in groups)==t
save('ADDITIVE_539_SOURCE_READING.json',inventory)
save('ADDITIVE_539_VALIDATION.json',dict(exact_slices='PASS',nonoverlapping_primary_partition='PASS',source_hash='PASS',original_manifest_unchanged='PASS',original_reading_unchanged='PASS',aggregate_core=21,aggregate_context_only=47))
save('ADDITIVE_539_FROZEN_MANIFEST.json',dict(frozen_at_utc=datetime.now(timezone.utc).isoformat(),before_producer_comparison=True,producer_material_accessed=False,source_sha256=sha(src),original_manifest_sha256=old_manifest,original_reading_sha256=old_reading,artifacts={f:sha(p/f) for f in ['additive_539.py','ADDITIVE_539_SOURCE_READING.json','ADDITIVE_539_VALIDATION.json']}))
print(json.dumps({f:sha(p/f) for f in ['ADDITIVE_539_SOURCE_READING.json','ADDITIVE_539_FROZEN_MANIFEST.json']},indent=2))
