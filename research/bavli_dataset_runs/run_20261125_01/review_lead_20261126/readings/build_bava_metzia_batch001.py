import json, hashlib
from pathlib import Path
B=Path(__file__).resolve().parent.parent
j=json.loads((B/'jobs/bavli_bava_metzia.json').read_text(encoding='utf-8'))
p=json.loads(Path(j['frozen_plan']['path']).read_text(encoding='utf-8'))
s=json.loads(Path(j['source']['path']).read_text(encoding='utf-8'))
checks=[]
for d in j['common_documents']+[j['source'],j['frozen_plan'],j['original_source_schema']]:
 h=hashlib.sha256(Path(d['path']).read_bytes()).hexdigest();assert h==d['sha256'];checks.append(dict(path=d['path'],sha256=h,verified=True))
pc={k:v for k,v in p.items() if k!='plan_sha256'}
assert hashlib.sha256(b'bavli-source-only-review-plan-v1\0'+json.dumps(pc,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()==p['plan_sha256']
texts={f'Bava Metzia {i//2+1}{"a" if i%2==0 else "b"}:{k+1}':t for i,page in enumerate(s['text']) for k,t in enumerate(page)}
blocks=p['review_blocks'][:2];core=[x['ref'] for b in blocks for x in b['spans']]
for b in blocks:
 for x in b['spans']:
  t=texts[x['ref']];assert hashlib.sha256(t.encode()).hexdigest()==x['span_sha256_utf8'];assert x['offsets_codepoints']==[0,len(t)]
context=[f'Bava Metzia 2a:{k}' for k in [11,12]]+[f'Bava Metzia 2b:{k}' for k in range(1,15)]+[f'Bava Metzia 3a:{k}' for k in range(1,14)]+[f'Bava Metzia 11a:{k}' for k in list(range(5,12))+[22]]+[f'Bava Metzia 11b:{k}' for k in range(1,12)]+[f'Bava Metzia 12a:{k}' for k in range(1,6)]
findings=[]
def ev(ref,q=None):
 ref='Bava Metzia '+ref if not ref.startswith('Bava') else ref;t=texts[ref];q=t if q is None else q;a=t.index(q);return dict(ref=ref,start_char=a,end_char=a+len(q),quote=q)
def add(id,ref,interpretation,holder='anonymous dialectic',conditions=None,status='asserted',q=None,kind='claim',**kw):
 findings.append(dict(id=id,kind=kind,interpretation=interpretation,origin='source_paraphrase',evidence=[ev(ref,q)],attribution={'holder':holder,'transmission_chain':[]},conditions=conditions or [],local_status=status,uncertainty=[],**kw));return id
add('c01','2a:1','Each claimant swears he owns no less than half.', 'anonymous Mishnah',['Two jointly hold a garment; each claims all'])
add('c02','2a:1','The claimants divide equally.','anonymous Mishnah',['Two jointly hold a garment; each claims all'])
add('c03','2a:2','The whole claimant swears to at least three quarters.','anonymous Mishnah',['One claims all; the other half'])
add('c04','2a:2','The half claimant swears to at least one quarter.','anonymous Mishnah',['One claims all; the other half'])
add('c05','2a:2','The whole claimant takes three quarters.','anonymous Mishnah',['One claims all; the other half'])
add('c06','2a:2','The half claimant takes one quarter.','anonymous Mishnah',['One claims all; the other half'])
add('c07','2a:3','Each swears to at least half the animal.','anonymous Mishnah',['Both ride or one rides and one leads; both claim all'])
add('c08','2a:3','They divide the animal equally.','anonymous Mishnah',['Both ride or one rides and one leads; both claim all'])
add('c09','2a:4','They divide without an oath.','anonymous Mishnah',['They agree or have witnesses'])
add('c10','2a:5','The two phrases are provisionally construed as one combined assertion: I found it and it is all mine.',status='rejected')
add('c11','2a:6','Seeing alone does not acquire the found object; the added whole-ownership wording is proposed to teach this.',status='asserted')
add('c12','2a:7','The scriptural term ומצאתה implies that the object has come into one’s hand.','Ravnai')
add('c13','2a:8','Scriptural finding implies possession, while ordinary speech can call seeing finding.')
add('c14','2a:8','The whole-ownership wording prevents the proposed inference that mere seeing acquires.',status='conditional',conditions=['Under the provisional combined-clause interpretation'])
add('c15','2a:9','The apparently redundant finding/ownership pair is proposed to exclude acquisition by sight elsewhere.',status='conditional',conditions=['Under the provisional combined-clause interpretation'])
add('q01','2a:5','Why repeat finding and whole ownership?',kind='question',status='answered')
add('q02','2a:6','Why not state only finding?',kind='question',status='answered provisionally')
add('q03','2a:7','Can finding mean seeing given Ravnai’s exposition?',kind='question',status='answered')
add('q04','2a:9','Why not state only whole ownership?',kind='question',status='answered provisionally')
add('q05','2a:10','The repeated this one/that one wording challenges the single-clause interpretation.',kind='question',status='objection sustained by replacement explanation')
add('x01','2a:11','The first clause concerns finding; the second purchase.','Rav Pappa OR Rav Shimi bar Ashi OR unattributed',status='local replacement answer',attribution_uncertainty='Explicit variant attributions; do not pick by order.')
add('x02','2b:1','A finder might rationalize seizing a share because his fellow paid nothing; an oath is imposed.',conditions=['Finding'])
add('x03','2b:2','A purchaser might rationalize taking the item because both pay and he needs it now; an oath is imposed.',conditions=['Purchase'])
add('x04','2b:3','The purchase case involves payment accepted from both, one willingly and one unwillingly, with the intended purchaser unknown.',status='local qualification')
add('c16','11a:12','A sheaf forgotten from the outset in the field is forgotten produce.',conditions=['Owner is in the field; initial forgetting'])
add('c17','11a:12','A remembered sheaf subsequently forgotten is not forgotten produce.',conditions=['Owner stands beside it'])
add('c18','11a:12','The adjacent owner’s courtyard acquires the remembered sheaf for him.',conditions=['Owner stands beside it; remembered before later forgetting'])
add('c19','11a:13','Even a remembered sheaf subsequently forgotten counts as forgotten produce.',conditions=['Owner in town, absent from field'])
add('c20','11a:13','Absence prevents courtyard acquisition in this case.',conditions=['Owner not alongside field'])
add('c21','11a:14','Perhaps a scriptural decree makes forgetting effective in the field but not the town.',status='challenged alternative')
add('c22','11a:15','לא תשוב לקחתו is proposed to include forgetting in town.',status='superseded derivation')
add('c23','11a:16','That wording is needed for a prohibition.',status='objection')
add('c24','11a:17','The extra return wording rather than merely take is proposed to include urban forgetting.',status='challenged answer')
add('c25','11a:18','Produce ahead is not forgotten produce.','quoted anonymous Mishnah',['Produce remains ahead'])
add('c26','11a:18','Produce behind is forgotten produce.','quoted anonymous Mishnah',['Taking would require returning'])
add('c27','11a:19','The general criterion is whether taking falls under the return prohibition.','quoted anonymous Mishnah',['Within the stated forgetting case'])
add('c28','11a:20','יהיה includes forgetting in town.','Rav Ashi',status='local resolution')
add('c29','11a:21','Acquisition requires standing beside one’s field.','Ulla',['Unprotected field; finding context'])
add('c30','11a:21','Acquisition requires standing beside one’s field.','Rabba bar bar Hana',['Unprotected field; finding context'])
add('q06','11a:14','Does the baraita really establish the proposed courtyard distinction, rather than a special decree?',kind='question',status='answered by final derivation')
add('q07','11a:16','Is the proposed proof wording already required for a prohibition?',kind='question',status='answered then further challenged')
add('q08','11a:18','Is return wording already required for the before/behind rule?',kind='question',status='answered by alternate verse')
add('x05','11a:6','Standing beside the field is required.','Shmuel',['Finding in an unprotected field'],transmitter='Rav Yehuda')
findings[-1]['attribution']['transmission_chain']=['Rav Yehuda','Shmuel']
add('x06','11a:7','A courtyard acquires without its owner’s awareness.','Rabbi Yose bar Hanina')
add('x07','11a:8','Acquisition without presence applies to a protected courtyard; an unprotected courtyard requires presence.',conditions=['Protection status distinguishes cases'])
add('x08','11b:4','Rabban Gamliel transferred movables together with land.','unnamed scholar at Sura',status='accepted by Rabbi Zeira; not accepted by Rabbi Abba')
add('x09','11b:5','Benefit of choosing recipients is not money for acquisition by exchange.','Rava')
add('x10','11b:5','Likewise benefit of choosing recipients is not money for acquisition with land.','Rava',status='rejected by anonymous continuation')
add('x11','11b:6','Exchange is sale-like whereas transfer with land is a strong giving; priestly gifts require giving.',status='rejection of Rava’s analogy')
add('x12','11b:7','Another mind transferring ownership distinguishes the gift case.','Rav Pappa',status='qualified by continuation')
add('x13','11b:8','For found animals the pursuer must be able to catch them.','Rabbi Yohanan',conditions=['Finding'],transmitter='Rabbi Yirmeya')
findings[-1]['attribution']['transmission_chain']=['Rabbi Yirmeya','Rabbi Yohanan']
add('x14','11b:8','In a gift, acquisition can occur even if pursuit cannot catch the animals.','Rabbi Abba bar Kahana',conditions=['Gift'],status='received response to Rabbi Yirmeya’s question')
add('x15','11b:9','A divorce document still requires standing beside house or courtyard.','Ulla',conditions=['Divorce document'],status='quoted objection by Rav Shimi to Rav Pappa')
add('x16','11b:9','Divorce differs because it can be against her will.',status='challenged answer')
add('x17','11b:10','If forced divorce requires presence, voluntary gifting should all the more require it.','Rav Sheshet son of Rav Idi',status='objection')
add('x18','12a:1','Courtyard is extended from hand but is no worse than agency.','Rav Ashi',status='local resolution; attribution begins at 11b:11')
findings[-1]['evidence'].append(ev('11b:11'))
add('x19','12a:1','A harmful divorce cannot be acquired for a person in her absence.','Rav Ashi',['Divorce classified as disadvantage'])
add('x20','12a:1','A beneficial gift may be acquired for a person in his absence.','Rav Ashi',['Gift classified as benefit'])
add('x21','12a:3','Whether a purse passing through courtyard air without resting is acquired is asked.','Rava',status='unresolved in read continuation',kind='question')
add('x22','12a:5','Rolling is treated as resting, so the animal/gift example does not resolve the airborne purse question.','Rava',status='analogy distinguished')
add('x23','3a:2','The oath is a rabbinic enactment against seizing another’s garment and claiming it.','Rabbi Yohanan',status='local compatibility answer concerning Sumakhos')
add('x24','3a:7','The Mishnah may fit Rabbi Yose because here both may have lifted it together and no cheat is certain.',status='retained answer')
add('x25','3a:8','An alternative penalty-to-induce-admission rationale is suggested.',status='rejected at 3a:9 for purchase case')
findings[-1]['evidence'].append(ev('3a:9'))
edges=[]
def edge(a,b,r,ref):edges.append(dict(id='e'+str(len(edges)+1).zfill(2),source_id=a,target_id=b,relation=r,evidence=[ev(ref)],explicitness='source_explicit'))
for a,b,r,ref in [('c10','q01','answer','2a:5'),('c11','q02','answer','2a:6'),('c12','c11','objection','2a:7'),('c13','q03','answer','2a:8'),('c15','q04','answer','2a:9'),('q05','c10','objection','2a:10'),('x01','q01','answer','2a:11'),('c18','c17','support','11a:12'),('c20','c19','support','11a:13'),('q06','c18','objection','11a:14'),('c22','q06','answer','11a:15'),('c23','c22','objection','11a:16'),('c24','q07','answer','11a:17'),('q08','c24','objection','11a:18'),('c28','q08','answer','11a:20'),('x11','x10','objection','11b:6'),('x15','x12','objection','11b:9'),('x17','x16','objection','11b:10'),('x18','x17','answer','12a:1'),('x22','x21','distinction','12a:5')]:edge(a,b,r,ref)
answers=[dict(id='a1',question='q01',members=['c10','x01'],comparability='Same wording question; c10 displaced, not two maintained scholar positions.'),dict(id='a2',question='q02',members=['c11'],comparability='Provisional wording analysis.'),dict(id='a3',question='q03',members=['c13'],comparability='Distinguishes biblical and colloquial usage.'),dict(id='a4',question='q04',members=['c15'],comparability='Provisional wording analysis.'),dict(id='a5',question='q06',members=['c22','c24','c28'],comparability='Successive scriptural derivations, with objections; final derivation by Rav Ashi.'),dict(id='a6',question='q08',members=['c28'],comparability='Alternate proof rather than opposed legal ruling.')]
def inc(f,refs):return any(e['ref'] in refs for e in f['evidence'])
def denom(refs):
 fs=[f for f in findings if f['kind']=='claim' and inc(f,refs)]
 return dict(independently_found_claims=len(fs),claim_ids=[f['id'] for f in fs],attributable_claims=sum(f['attribution']['holder']!='anonymous dialectic' for f in fs),attribution_definition='Includes explicitly anonymous Mishnah as a textual collective; excludes anonymous dialectical voice.',condition_bearing_claims=sum(bool(f['conditions']) for f in fs),proposed_answer_sets=sum(any(f['id']==a['question'] and inc(f,refs) for f in findings) for a in answers),edges=sum(inc(e,refs) for e in edges))
o=dict(artifact_kind='immutable_source_only_reading',job_id=j['job_id'],batch_id='batch001',execution=dict(agent_id='/root/reader_bava_metzia',route='interactive_agent',model_id=None),fresh_context={'fork_turns':'none','producer_labels_exposed':False},producer_labels_exposed=False,frozen_before_comparison=True,source_sha256=j['source']['sha256'],plan_file_sha256=j['frozen_plan']['sha256'],plan_sha256=p['plan_sha256'],hash_checks=checks,core_refs=core,context_refs=context,cohorts=[dict(block_id=b['block_id'],roles=b['roles'],core_refs=[x['ref'] for x in b['spans']],denominators=denom([x['ref'] for x in b['spans']])) for b in blocks],core_denominators=denom(core),context_denominators=denom(context),findings=findings,proposed_answer_sets=answers,directed_relations=edges,boundaries=[dict(core='2a:1–10',discussion='Mishnah 2a:1–4; wording discussion 2a:5–2b:3; compatibility continuations read to 3a:13.',local_status='Single-clause account displaced by finding/purchase account; alternative attribution retained. Mishnah is not an enduring attribution to named amoraim.'),dict(core='11a:12–21',discussion='Unprotected courtyard acquisition 11a:5–12a:1; repeated pursuit/gift application and airborne purse question read 12a:2–5.',local_status='Rav Ashi replaces earlier proof for urban forgetting; later gift/divorce distinction qualifies presence requirement. Airborne purse question not settled by rejected rolling analogy.')],uncertainty=['AI provisional; not human scholarly certification or tractate verdict.','Granularity of the general before/behind rule could be split into two conditional atoms; retained as one equivalence in c27, distinct from quoted examples.','Attributable denominator includes anonymous Mishnah; named-authority core claims alone are c12,c28,c29,c30.','Context findings are selective aids to core interpretation, not an exhaustive extraction of every context claim.','No inferred Rav–Shmuel dispute; Rav Yehuda is Shmuel’s transmitter here.'],reconciliation='Reread all 20 cores; separately preserved oath and allocation atoms, hypothetical/rejected derivations, repeat occurrences, and presence conditions inherited from preceding courtyard discussion.',next_selected_block=p['review_blocks'][2]['block_id'],comparison_performed=False,ml_eligible=False)
for obj in findings+edges:
 for e in obj['evidence']:assert texts[e['ref']][e['start_char']:e['end_char']]==e['quote']
o['validation']={'all_evidence_slices_match':True,'unicode_offsets':'Python code points, half-open, raw markup retained','core_segment_count':len(core),'context_segment_count':len(context),'evidence_span_count':sum(len(f['evidence']) for f in findings+edges)}
out=B/'readings/bava_metzia_batch001.json';data=(json.dumps(o,ensure_ascii=False,indent=2)+'\n').encode();out.parent.mkdir(exist_ok=True)
with out.open('xb') as f:f.write(data)
h=hashlib.sha256(data).hexdigest()
with out.with_suffix('.sha256').open('x',encoding='ascii') as f:f.write(h+'  '+out.name+'\n')
print(json.dumps({'path':str(out),'sha256':h,'denominators':o['core_denominators'],'validation':o['validation']},ensure_ascii=True))
