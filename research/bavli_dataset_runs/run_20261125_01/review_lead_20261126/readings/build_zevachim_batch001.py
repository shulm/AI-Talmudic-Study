import json, hashlib, re
from pathlib import Path

root=Path(__file__).resolve().parent.parent
jpath=root/'jobs/bavli_zevachim.json'
j=json.loads(jpath.read_text(encoding='utf-8'))
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
bindings={}
for name,d in [('source',j['source']),('original_source_schema',j['original_source_schema']),('frozen_plan',j['frozen_plan'])]+[(Path(d['path']).name,d) for d in j['common_documents']]:
    assert digest(d['path'])==d['sha256'],name
    bindings[name]={**d,'verified':True}
bindings['job_descriptor']={'path':str(jpath),'sha256':digest(jpath)}
p=json.loads(Path(j['frozen_plan']['path']).read_text(encoding='utf-8'))
q={k:v for k,v in p.items() if k!='plan_sha256'}
assert hashlib.sha256(b'bavli-source-only-review-plan-v1\0'+json.dumps(q,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()==p['plan_sha256']==j['plan_sha256']
s=json.loads(Path(j['source']['path']).read_text(encoding='utf-8'))
texts={f'Zevachim {i//2+1}{"a" if i%2==0 else "b"}:{n+1}':t for i,page in enumerate(s['text']) for n,t in enumerate(page)}
blocks=p['review_blocks'][:3]; core=[x['ref'] for b in blocks for x in b['spans']]
for b in blocks:
    for x in b['spans']:
        t=s['text'][x['page_index']][x['segment_index']]; assert texts[x['ref']]==t
        a,z=x['offsets_codepoints']; assert hashlib.sha256(t[a:z].encode()).hexdigest()==x['span_sha256_utf8']
def ev(ref,quote=None):
    ref='Zevachim '+ref if not ref.startswith('Zevachim ') else ref
    t=texts[ref]; quote=t if quote is None else quote; a=t.index(quote)
    return {'source_ref':ref,'start':a,'end':a+len(quote),'quote':quote}
F=[]
def c(id,ref,claim,holder='anonymous discussion',status='asserted locally',conditions=None,quote=None,chain=None):
    F.append({'id':id,'kind':'atomic_claim','proposition':claim,'origin':'source_paraphrase','holders':[holder],'transmission_chain':chain or [],'conditions':conditions or [],'local_status':status,'evidence':[ev(ref,quote)],'cohort':'core' if 'Zevachim '+ref in core else 'context'})
c('C01','2a:1','Sacrifices slaughtered under another designation remain valid, apart from the stated exceptions.','anonymous Mishnah',conditions=['Slaughter שלא לשמן','Exceptions: Paschal offering at its appointed time; sin offering at any time'])
c('C02','2a:1','These otherwise valid offerings do not discharge the owners’ obligation.','anonymous Mishnah',conditions=['Slaughter שלא לשמן','Offering not within invalidating exceptions'])
c('C03','2a:1','The Paschal offering is invalid under another designation at its appointed time.','anonymous Mishnah',conditions=['בזמנו','שלא לשמו'])
c('C04','2a:1','A sin offering is invalid under another designation at any time.','anonymous Mishnah',conditions=['שלא לשמה'])
c('C05','2a:2','A guilt offering too is invalid under another designation at any time.','רבי אליעזר',conditions=['שלא לשמו'])
c('C06','2a:2','The guilt offering’s coming for sin grounds its analogy to the sin offering.','רבי אליעזר',status='stated argument for C05')
c('C07','2a:3','Offerings slaughtered for the designation of a Paschal or sin offering are invalid.','יוסי בן חוני',conditions=['Intended designation לשם פסח or לשם חטאת'])
c('C08','2a:4','Slaughter for a higher sanctity designation is valid.','שמעון אחי עזריה',conditions=['לשם גבוה מהן'])
c('C09','2a:4','Slaughter for a lower sanctity designation is invalid.','שמעון אחי עזריה',conditions=['לשם נמוך מהן'])
c('C10','2a:5','Most holy offerings slaughtered as offerings of lesser sanctity are invalid.','שמעון אחי עזריה',conditions=['קדשי קדשים לשם קדשים קלים'])
c('C11','2a:5','Offerings of lesser sanctity slaughtered as most holy offerings are valid.','שמעון אחי עזריה',conditions=['קדשים קלים לשם קדשי קדשים'])
c('C12','2a:5','Firstborn and tithe offerings slaughtered as peace offerings are valid.','שמעון אחי עזריה',conditions=['בכור or מעשר לשם שלמים'])
c('C13','2a:5','Peace offerings slaughtered as firstborn or tithe offerings are invalid.','שמעון אחי עזריה',conditions=['שלמים לשם בכור or מעשר'])
c('C14','2a:7','Non-discharge of the obligation does not remove the offering’s sanctity.')
c('C15','2a:7','Changing the remaining service’s designation is prohibited even after the initial incorrect designation.')
c('C16','2a:8','After slaughtering a burnt offering under another designation one may not sprinkle its blood under another designation.','רבא',conditions=['עולה ששחטה שלא לשמה'])
c('C17','2a:9','A prior alteration is no reason to continue altering the offering.',status='first alternative rationale for prohibition')
c('C18','2b:1','Performance in accord with the vow counts as the vow; otherwise the offering counts as voluntary.',status='second alternative scriptural rationale; sentence begins 2a:10')
c('C19','2b:2','Voluntary-offering status does not permit changing its designation.',status='rhetorical-question assertion')
c('C20','4a:16','The reception verse uses bringing language so conveying the blood remains within reception’s rule of proper designation.',chain=['אמר מר: identification of limb conveyance','תניא: identification of blood reception'])
c('C21','4a:18','The thanksgiving verse supplies the requirement of the proper owner in slaughter through אם אינו ענין.','רב פנחס בריה דרב אמי')
c('C22','4a:19','A thanksgiving offering slaughtered as a peace offering is valid.','רבי אליעזר',conditions=['תודה לשם שלמים'],chain=['אבא חנין','רבי אליעזר'])
c('C23','4a:19','A peace offering slaughtered as thanksgiving is invalid.','רבי אליעזר',conditions=['שלמים לשם תודה'],chain=['אבא חנין','רבי אליעזר'])
c('C24','4a:19','Thanksgiving is called peace offering, whereas a peace offering is not called thanksgiving.','רבי אליעזר',chain=['אבא חנין','רבי אליעזר'])
c('C25','4a:20','The owner-designation derivation is specifically from זבח.',status='answer to competing use of verse')
c('C26','4a:21','זבח is also needed to include sin and guilt offerings.',status='competing-use objection')
c('C27','4a:22','The wording permits both derivations.',status='answer preserving C21 despite C26')
c('C28','4a:24','Direct inference from slaughter to other services is vulnerable because slaughter uniquely invalidates a Paschal offering for unintended eaters.',status='objection to proposed direct inference')
c('C29','4a:25','The shared mention of slaughter in change of sanctity and change of owner could extend the latter to other services.',status='proposed analogy; challenged in 4a:26–4b:3, replaced by subsequent derivations')
c('C30','4a:26','Change of sanctity is proposed to differ by being intrinsic and applying in all four services.',status='objection; intrinsic-disqualification distinction rejected at 4b:2')
c('C31','4a:27','Change of sanctity is proposed to differ by applying after death and to communal as well as individual offerings.',status='objection; after-death distinction is not available under Rav Pinchas bar Rav Mari at 4b:3')
c('C32','4b:2','Both kinds of incorrect intention are mental acts that invalidate once intended.',status='rejects the intrinsic-versus-mental distinction')
c('C33','4b:3','Change of owner applies after death.','רב פנחס בריה דרב מרי',status='cited position; two other objections to C29 remain')
c('C34','4b:4','ונרצה לו לכפר supplies atonement for this owner and not another.','רב אשי',status='replacement derivation for blood application; clarified at 4b:7')
c('C35','4b:10','The Nazirite ram’s עשייה wording extends proper owner designation to the other services.','רב אשי',status='replacement derivation; defended in ensuing discussion')
c('C36','4b:12','An incomplete generalization is not treated under general-and-particular interpretation.',status='answer to Rav Acha bar Abba’s challenge to Rava; no explicit speaker tag in this segment')
c('C37','4b:13','General-and-particular interpretation does apply, but ולה adds another generalization.','רבינא',status='alternative interpretive answer')
c('C38','4b:18','The two balanced possible service comparisons allow both to enter.',status='local answer; alternate wording חדא חדא תיקו במילתא is preserved rather than collapsed')
c('C39','4b:19','Blood application can alternatively be derived from Rav Ashi’s earlier exposition.',status='alternative answer')
c('C40','4b:22','The plural שלמים extends the Nazirite ram derivation to all peace offerings.')
c('C41','4b:25','זאת התורה compares the listed offerings to peace offerings for both sanctity and owner designation requirements.')
c('C42','4b:27','Incorrect designation leaves a voluntary offering rather than automatically invalidating the offering.',status='answer to invalidation inference')
c('C43','5a:1','Both זאת התורה and מוצא שפתיך are needed: the former defines the offerings covered and the latter blocks invalidity.')
c('C44','6a:13','Like a sin offering, a burnt offering might atone only for pre-designation transgressions.',status='hypothetical side of open inquiry',conditions=['Violation of positive command after designation'])
c('C45','6a:14','Because one burnt offering covers multiple positive-command transgressions, it might cover post-designation ones too.',status='alternative hypothetical side of open inquiry')
c('C46','6a:15','Blood, rather than laying hands, effects atonement.','cited anonymous teaching')
c('C47','6a:15','Neglecting laying hands is treated as though one did not atone, yet one did atone.','cited anonymous teaching',conditions=['סמיכה treated as שירי מצוה'])
c('C48','6a:16','The teaching might mean atonement for pre-designation commands but not for omitted laying hands after designation.',status='proposed proof; applicability rejected by Rava')
c('C49','6a:17','The obligation to lay hands remains performable until slaughter; its violation occurs only afterward.','רבא',status='answer excluding proof from present inquiry')
c('C50','6a:17','Post-slaughter transgression is outside the question being asked.','רבא')
c('C51','6a:18','The teaching may mean the person has atonement but lacks atonement before Heaven.','רב הונא בר יהודה',status='alternative interpretation posed to Rava; continued at 6b:1')
F[-1]['evidence'].append(ev('6b:1'))
c('C52','6b:2','Applying the remaining oil brings atonement; omitting it does not.','רבי עקיבא',conditions=['Remaining oil on leper’s head'])
c('C53','6b:2','The remaining oil is a remainder of the command: atonement occurs whether applied or omitted.','רבי יוחנן [בן נורי]',conditions=['Remaining oil on leper’s head'])
c('C54','6b:2','Despite that atonement, omission is reckoned as though there were no atonement.','רבי יוחנן [בן נורי]',conditions=['Omitted remaining oil'])
c('C55','6b:3','The apparent lack of atonement cannot require another offering after the teaching expressly says atonement occurred.',status='argument for person/before-Heaven distinction')
c('C56','6b:4','The oil teaching can instead distinguish atonement of thumb/toe applications from absent head applications.',status='counter-interpretation; preceding interpretation not conclusively established')
c('C57','6b:6','The question must concern Shavuot goats, not lambs, since its lambs are peace offerings.',status='explicit correction to quoted question at 6b:5')
c('C58','6b:7','Shavuot goats atone for impurity of the sanctuary and sacred things.','רבי שמעון',status='corrected citation continuing 6b:5–6')
c('C59','6b:8','After blood of the first is applied, the second addresses impurity occurring between them.','רבי שמעון')
c('C60','6b:8','Israel could fittingly offer at every moment, but scripture spared that burden.','רבי שמעון')
c('C61','6b:9','The goat example appears to show atonement for post-designation transgression.',status='proposed proof, not final conclusion')
c('C62','6b:10','The proof can be avoided by construing the two goats as designated successively.',status='proposed deflection; challenged at 6b:11')
c('C63','6b:12','For communal offerings the court’s stipulation can account for designation.','רב פפא',status='deflection; applicability to Rabbi Shimon challenged at 6b:13–7a:1')
c('C64','6b:12','The knife determines communal offerings for what they are.','שמואל',status='cited support for Rav Pappa',chain=['רב יהודה','שמואל'])
c('C65','7a:1','According to Rabbi Shimon, surplus daily offerings cannot be redeemed unblemished.','רבי יוחנן reporting רבי שמעון',chain=['רב אידי בר אבין','רב עמרם','רבי יצחק','רבי יוחנן'])
F[-1]['evidence'].insert(0,ev('6b:13'))
c('C66','7a:1','According to the Sages, surplus daily offerings may be redeemed unblemished.','רבי יוחנן reporting חכמים',chain=['רב אידי בר אבין','רב עמרם','רבי יצחק','רבי יוחנן'])
F[-1]['evidence'].insert(0,ev('6b:13'))
c('C67','7a:3','The question about two received cups apparently presupposes post-designation atonement while asking only about post-slaughter atonement.',status='inference from Rabbi Yirmeya’s question to Rabbi Zeira at 7a:2')
c('C68','7a:4','That question may have been asked only conditionally, if post-designation atonement is assumed.',status='deflection; main inquiry remains unresolved locally')

Q=[]
def question(id,refs,text,conditions=None): Q.append({'id':id,'formulation':text,'question_origin':'explicit','conditions':conditions or [],'evidence':[ev(r) for r in refs]})
question('Q01',['2a:6'],'Why does the Mishnah say אלא שלא עלו rather than ולא עלו?')
question('Q02',['4a:14'],'What is the source that conveying requires proper designation?')
question('Q03',['4a:17'],'What is the source for proper owner designation?')
question('Q04',['4a:23'],'How does the owner-designation requirement extend beyond slaughter?')
question('Q05',['6a:12'],'Does the burnt offering atone for positive-command transgressions after designation?', ['After designation but before slaughter; post-slaughter excluded by Rava'])
question('Q06',['6b:5','6b:6'],'What do the Shavuot goats come for? The initial lamb reading is explicitly corrected.')
question('Q07',['7a:2'],'With blood received in two cups, what does the second goat address after application of the first?')
A=[{'question_id':'Q01','claim_ids':['C14','C15'],'comparability':'same wording question; complementary explanatory claims'},
{'question_id':'Q02','claim_ids':['C20'],'comparability':'direct derivation'},
{'question_id':'Q03','claim_ids':['C21','C25','C27'],'comparability':'derivation and defenses; not opposed rulings'},
{'question_id':'Q04','claim_ids':['C29','C34','C35','C36','C37','C38','C39'],'comparability':'C29 challenged; replacement derivations and alternative interpretive routes do not create a ruling dispute'},
{'question_id':'Q05','claim_ids':['C44','C45','C48','C49','C50','C51','C55','C56','C61','C62','C63','C67','C68'],'comparability':'yes/no hypotheses and attempted proofs; rebuttals about applicability are not maintained no answers','local_outcome':'unresolved'},
{'question_id':'Q06','claim_ids':['C57','C58','C59'],'comparability':'corrected subject; same textual question only after correction'},
{'question_id':'Q07','claim_ids':['C67','C68'],'comparability':'conditional question blocks conclusive answer to Q05'}]
R=[]
def relation(a,b,typ,refs,note):R.append({'source_id':a,'target_id':b,'relation':typ,'explicitness':'source_explicit','explanation':note,'evidence':[ev(r) for r in refs]})
relation('C05','C01','qualification',['2a:2'],'Rabbi Eliezer adds guilt offering to exceptions.')
relation('C06','C05','support',['2a:2'],'Both offerings come for sin.')
relation('C16','C15','support',['2a:8'],'Rava cited as matching prohibition.')
relation('C17','C16','support',['2a:9'],'Rational alternative.')
relation('C18','C16','support',['2a:10','2b:1','2b:2'],'Scriptural alternative completed across page.')
relation('C25','C21','answer',['4a:19','4a:20'],'Different word supplies derivation despite Abba Chanin citation.')
relation('C27','C26','answer',['4a:22'],'Both uses retained.')
relation('C30','C29','objection',['4a:26','4a:27','4b:1'],'Four differences proposed; two suffice.')
relation('C32','C30','correction',['4b:2'],'Intrinsic distinction is not sound.')
relation('C33','C31','qualification',['4b:3'],'After-death distinction unavailable to this authority.')
relation('C34','C29','correction',['4b:4'],'New derivation introduced by אלא.')
relation('C37','C36','qualification',['4b:13'],'Different interpretive method supports derivation, not opposite legal conclusion.')
relation('C49','C48','objection',['6a:17'],'Laying hands fails only after slaughter, outside inquiry.')
relation('C51','C48','qualification',['6a:18','6b:1'],'Alternative explanation of כיפר ולא כיפר.')
relation('C53','C52','qualification',['6b:2'],'Explicit disagreement on consequence of omitted remaining oil.')
relation('C55','C51','support',['6b:2','6b:3'],'Analogy offered from oil.')
relation('C56','C55','objection',['6b:4'],'Alternative interpretation avoids conclusion.')
relation('C57','Q06','correction',['6b:5','6b:6'],'Lambs replaced by goats.')
relation('C62','C61','objection',['6b:10'],'Successive designation proposed.')
relation('C64','C63','support',['6b:12'],'Shmuel transmitted by Rav Yehuda; no Rav–Shmuel dispute.')
relation('C65','C63','objection',['6b:13','7a:1'],'Rav Yosef son of Rav Shmuel challenges applicability of stipulation to Rabbi Shimon.')
relation('C68','C67','objection',['7a:4'],'Conditional question does not settle premise.')

def rr(page,a,b):return [f'Zevachim {page}:{n}' for n in range(a,b+1)]
relevant=rr('2a',1,10)+rr('2b',1,2)+rr('4a',1,27)+rr('4b',1,28)+rr('5a',1,1)+rr('6a',12,18)+rr('6b',1,13)+rr('7a',1,4)
context=[r for r in relevant if r not in core]
read_all=[r for r in texts if any(r.startswith('Zevachim '+pg+':') for pg in ['2a','2b','3b','4a','4b','5a','6a','6b','7a'])]
o={'artifact_kind':'independent_source_only_reading','reading_id':'zevachim_batch001','tractate':'Zevachim','status':'FROZEN_SOURCE_FIRST_READING_BOUNDED_BATCH','bindings':bindings,'plan_sha256':p['plan_sha256'],
'launch_provenance':{'agent_id':'/root/reader_zevachim_wave2','model_id':None,'route':'interactive_agent','fresh_source_only_context':True,'producer_annotations_seen':False,'other_readings_seen':False,'input_allowlist':'neutral descriptor, pinned original source/schema, frozen neutral plan, common documents only','AGENT_HANDOFF_read':False,'reason':'Specific source-only blind-reader delegation; lead handles handoff','blindness_scope':core,'producer_comparison_performed':False},
'edition':{k:s[k] for k in ['versionTitle','versionSource','license','versionNotes']},'selected_blocks':blocks,'core_refs':core,'context_refs':context,'incidental_original_source_refs_read':[r for r in read_all if r not in relevant],
'boundaries':[{'core_block':'block_000000','local_scope':'2a:1–2b:2','note':'Mishnah 2a:1–5; opening explanation 2a:6–2b:2. Later explanations of individual tannaim are outside bounded admission.'},{'core_block':'block_000008','local_scope':'4a:1–5a:1','note':'Proper designation derivation, owner designation and extension to services; final validity clarification closes at 5a:1.'},{'core_block':'block_000017','local_scope':'6a:12–7a:4','note':'Post-designation atonement question; several attempted proofs; conditional deflection leaves inquiry unresolved.'}],
'findings':F,'questions':Q,'answer_sets':A,'relations':R,
'uncertainties':[{'scope':'6b:2','text':'The pinned edition brackets בן נורי; preserve this surface attribution rather than silently equating with the amora Rabbi Yochanan.'},{'scope':'4b:18','text':'לישנא אחרינא retained as a textual alternative; no unwarranted doctrinal disagreement inferred.'},{'scope':'4b:12','text':'Answer follows Rav Acha bar Abba addressing Rava; explicit name absent in answer, so no confident named attribution asserted.'},{'scope':'6a:12–7a:4','text':'Attempted proofs do not establish a final yes/no outcome.'}],
'coverage':{'probability':{'blocks_read':2,'core_segments_read':20,'plan_blocks':39,'plan_core_segments':390},'endpoint':{'blocks_read':1,'core_segments_read':10,'plan_blocks':2,'plan_core_segments':17},'overlap':{'blocks':0,'core_segments':0},'unique_core_segments':30,'context_expansion_segments':len(context),'incidental_source_segments_read':len(read_all)-len(relevant),'claim_count':len(F),'counts_are_occurrences_not_unique_topics':True,'core_reading':'all 30 selected source segments read with necessary local continuations','semantic_extraction':'substantive atomic claims and argument links recorded; not a production-schema submission or exhaustive full-tractate extraction','structure':'boundaries recorded; no claim of complete character partition for production structure pass','reconciliation':'source omission pass against every core: isolated questions at 2a:6,4a:17,4a:23 mapped to Q; alternatives and corrections retained; no core skipped','human_review':False,'ml_eligible':False},
'next_coordinates':{'next_review_block_index_zero_based':3,'block_id':p['review_blocks'][3]['block_id'],'refs':[x['ref'] for x in p['review_blocks'][3]['spans']]},'admission':'No tractate acceptance, producer comparison, accuracy estimate, or downstream eligibility granted.'}
count=0
def validate(x):
 global count
 if isinstance(x,dict):
  if {'source_ref','start','end','quote'}<=x.keys():
   assert texts[x['source_ref']][x['start']:x['end']]==x['quote'];count+=1
  for y in x.values():validate(y)
 elif isinstance(x,list):
  for y in x:validate(y)
validate(o)
o['mechanical_validation']={'source_and_input_hashes':'all matched','canonical_plan_hash':'matched','all_30_core_span_hashes':'matched','evidence_slices_validated':count,'offset_unit':'original Unicode codepoints, half-open; markup retained'}
out=root/'readings/zevachim_batch001.json'
with out.open('x',encoding='utf-8',newline='\n') as f:json.dump(o,f,ensure_ascii=False,indent=2);f.write('\n')
h=digest(out)
with out.with_suffix('.sha256').open('x',encoding='ascii') as f:f.write(h+'  '+out.name+'\n')
print(json.dumps({'path':str(out),'sha256':h,'findings':len(F),'questions':len(Q),'relations':len(R),'validated_spans':count,'context_segments':len(context),'next':o['next_coordinates']}))
