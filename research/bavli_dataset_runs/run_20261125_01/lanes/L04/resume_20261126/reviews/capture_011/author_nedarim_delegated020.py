import json, hashlib, re
from pathlib import Path
BASE=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
OUT=Path(__file__).parent
JOB=BASE/'jobs/bavli_nedarim_delegated020.json'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
j=read(JOB); bindings=[]
assert sha(JOB)=='2898ad593643dba3600a208619ddf81dc1191ce673dd83ee9c401ceacf6883ff'
for x in [j['source'],j['original_source_schema'],j['frozen_plan']]+j['common_documents']:
 actual=sha(x['path']); assert actual==x['sha256'];bindings.append(dict(path=x['path'],sha256=actual,verified=True))
plan=read(j['frozen_plan']['path']); pp=dict(plan);pp.pop('plan_sha256')
assert hashlib.sha256(b'bavli-source-only-review-plan-v1\0'+json.dumps(pp,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()==j['plan_sha256']
src=read(j['source']['path']);schema=read(j['common_documents'][1]['path']);cores=j['core_refs']; R=[]; labels={}; contexts=set()
def ref(x): return x if x.startswith('Nedarim ') else 'Nedarim '+x
def text(x):
 m=re.fullmatch(r'Nedarim (\d+)([ab]):(\d+)',ref(x));return src['text'][int(m[1])*2-2+(m[2]=='b')][int(m[3])-1]
def ev(x,q=None):
 s=text(x);q=s if q is None else q;a=s.index(q);return {'segment_id':ref(x),'start_char':a,'end_char':a+len(q),'quote':q}
def add(layer,x,c,key=None,quote=None,origin='source_paraphrase',unc=None,links=None):
 rid='nd020.'+str(len(R)+1).zfill(4);R.append(dict(id=rid,layer=layer,evidence=[ev(x,quote)],content=c,origin=origin,uncertainty=unc or [],links=links or []));
 if key: labels[key]=rid
 if ref(x) not in cores:contexts.add(ref(x))
 return rid
def claim(x,key,holder,p,status='asserted',conditions=None,unc=None,voice=None):
 cid=add('claims',x,dict(proposition=p,conditions=conditions or [],scope=ref(x),assertion_mode=status),key,unc=unc)
 add('utterances',x,dict(textual_voice=voice or holder,discourse_role=status+' proposition',composition='atomic'),links=[cid])
 add('attributions',x,dict(surface=holder,role='anonymous' if holder.startswith('anonymous') else 'position_holder',candidates=[holder],scope=cid,transmission_chain=[]),links=[cid])
 add('positions',x,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=conditions or [],local_status=status),links=[cid])
 return cid
def question(x,key,p,conditions=None,status='topic_inventory'):
 return add('questions',x,dict(formulation=p,question_origin='explicit',conditions=conditions or [],answer_set_status=status),key)
def edge(x,a,b,rel,explicit=True):
 return add('edges',x,dict(source_id=labels[a],target_id=labels[b],relation=rel,explicitness='source_explicit' if explicit else 'editorial_reconstruction'),links=[labels[a],labels[b]])

# Manually authored independent semantic inventory, never inferred from producer rows.
claim('5b:4','rava_m','רבא','The Mishnah’s repeated לך in שאני אוכל לך / שאני טועם לך indicates that demonstrative handles are required; this explains Shmuel’s restrictive interpretation.',voice='רבא')
question('5b:4','q_why','Why does the Mishnah teach לך instead of merely שאני אוכל / שאני טועם?')
edge('5b:4','rava_m','q_why','answer')
claim('5b:5','abaye','אביי','Non-demonstrative handles count as handles.')
claim('5b:5','rava','רבא','Non-demonstrative handles do not count as handles.')
claim('5b:5','deriv','רבי אידי','The verse נזיר להזיר לי״י compares handles of naziriteship to naziriteship: both require explicit articulation.',voice='רבא reporting רבי אידי',unc=['Source prints לי\'\'י; normalized divine-name typography here is paraphrase only. Literal evidence retains original.'])
add('attributions','5b:5',dict(surface='אמר רבא  רבי אידי אסברה לי',role='transmitter',candidates=['רבא'],scope=labels['deriv'],transmission_chain=['רבי אידי','רבא']),quote='אמר רבא  רבי אידי אסברה לי',links=[labels['deriv']])
edge('5b:5','deriv','rava','support')
question('5b:6','q_align','Do Abaye and Rava dispute in the tannaitic dispute of R. Judah and the Rabbis?')
claim('5b:6','get_r','anonymous Mishnah / Rabbis','The essential get wording is הרי את מותרת לכל אדם.')
claim('5b:6','get_j','רבי יהודה','R. Judah adds ודין דיהוי ליכי מינאי ספר תירוכין וגט פטורין ואיגרת שבוקין to the get wording.')
claim('5b:6','align_a','anonymous dialectic','Proposed alignment: Abaye follows the Rabbis.',status='rejected',unc=['Rejected as necessary alignment, not as impossibility of agreement; Abaye’s broader compatibility is later retracted.'])
claim('5b:6','align_r','anonymous dialectic','Proposed alignment: Rava follows R. Judah.',status='rejected',unc=['Rava denies exclusive dependence on R. Judah.'])
claim('5b:7','a_compat','אביי in reconstructed reply','Abaye’s rule can agree even with R. Judah: Judah requires demonstrative wording specifically for a get because severance is otherwise lacking.',status='retracted',conditions=['Get requires כריתות.'],unc=['אמר לך is a dialectically supplied response; 6a:6 explicitly says הדר ביה.'])
question('5b:7','q_j_general','Have you heard R. Judah require demonstrative handles outside a get?',status='partial')
edge('5b:7','a_compat','align_a','objection')
claim('5b:8','r_compat','רבא','Rava’s rule can agree even with the Rabbis; their leniency is specific to a get.',conditions=['Reason completes in 6a:1.'])
claim('6a:1','r_reason','רבא, continued','A man does not divorce his fellow’s wife, so a get is already contextually demonstrative; no general leniency outside a get follows.',conditions=['Get context.'])
question('6a:1','q_r_general','Have you heard the Rabbis dispense with demonstrative handles outside a get?',status='partial')
edge('6a:1','r_reason','r_compat','continuation');edge('6a:1','r_compat','align_r','objection')
claim('6a:2','bar_hand','anonymous baraita','הרי הוא עלי / הרי זה [עלי] is prohibited because it is a handle for a sacrifice.',conditions=['עלי is said.'])
claim('6a:2','inf_no','anonymous objection','The baraita is initially inferred to permit the object when עלי is omitted; this challenges Abaye.',status='challenged',conditions=['Omission of עלי.'])
question('6a:2','q_obj_a','Does the baraita’s limitation to עלי refute Abaye?')
edge('6a:2','inf_no','abaye','objection')
claim('6a:3','a_first','אביי in reconstructed reply','Without עלי, הרי הוא could mean ownerless property or charity.',status='rejected',conditions=['הרי הוא without עלי.'])
question('6a:3','q_wording','But does the baraita not explicitly say it is a handle for a sacrifice?')
edge('6a:3','a_first','inf_no','answer');edge('6a:3','q_wording','a_first','objection')
claim('6a:4','a_revised1','anonymous revised reply for Abaye','With עלי, the speaker is prohibited and his fellow is permitted.',status='reconciled',conditions=['הרי הוא עלי.'])
claim('6a:4','a_revised2','anonymous revised reply for Abaye','Without עלי, both are prohibited because הרי הוא may mean consecration.',status='reconciled',conditions=['הרי הוא without עלי.'])
edge('6a:4','a_revised1','a_first','correction');edge('6a:4','a_revised2','inf_no','answer')
claim('6a:5','chatat_no','anonymous baraita','הרי זו חטאת / הרי זו אשם accomplishes nothing even when the speaker owes that sacrifice.',conditions=['No possessive suffix.','Speaker may owe a sin or guilt offering.'])
claim('6a:5','chatat_yes','anonymous baraita','הרי זו חטאתי / הרי זו אשמי is effective if the speaker owes the offering.',conditions=['Possessive suffix.','Speaker owes the relevant offering.'])
question('6a:5','q_final_a','Does this sacrificial designation baraita refute Abaye?')
edge('6a:5','chatat_no','abaye','objection')
claim('6a:6','a_ret','anonymous dialectic / reply for Abaye','The baraita is R. Judah; Abaye retracts his prior claim to agree even with R. Judah.',status='retracted',unc=['Retraction concerns compatibility with R. Judah, not abandonment of Abaye’s own non-demonstrative-hand rule.'])
edge('6a:6','a_ret','a_compat','retraction');edge('6a:6','a_ret','q_final_a','answer')
claim('6a:8','r_retained','רבא in reconstructed reply','Rava still agrees even with the Rabbis: their get ruling relies on the fact that a man does not divorce his fellow’s wife; elsewhere demonstrative handles are required.')
edge('6a:8','r_retained','r_compat','support')

claim('10a:8','ab_group','אביי','Shimon the Righteous, R. Shimon and R. Eleazar HaKappar share a position that a nazir is a sinner.',unc=['This is Abaye’s grouping; earlier statements concern different circumstances. It does not erase those conditions.'])
claim('10a:8','backrefs','anonymous continuation','The cited positions of Shimon the Righteous and R. Shimon are the preceding reports.',voice='anonymous continuation of Abaye attribution')
claim('10a:9','el_wine','רבי אלעזר הקפר ברבי','The nazir’s sin against the soul is self-affliction by abstaining from wine.')
question('10a:9','q_soul','Against which soul did this nazir sin?')
claim('10a:9','el_all','רבי אלעזר הקפר ברבי','If abstaining only from wine is called sin, one who afflicts himself by abstaining from everything is all the more a sinner.')
claim('10a:9','el_fast','רבי אלעזר הקפר ברבי / baraita continuation','Hence everyone who fasts is called a sinner.',unc=['Final מכאן continues the cited passage; no separately named speaker is supplied.'])
edge('10a:9','el_wine','q_soul','answer');edge('10a:9','el_all','el_wine','analogy');edge('10a:9','el_fast','el_all','local_resolution');edge('10a:9','el_wine','ab_group','support')
question('10a:10','q_impure','But is this verse not written concerning a defiled nazir?')
claim('10a:10','repeat','anonymous answer','The verse singles out the defiled nazir because he repeated the sin.',unc=['The core says only שנה בחטא; renewed abstention is an explanatory inference, not an explicit new quotation.'])
edge('10a:10','q_impure','el_wine','objection');edge('10a:10','repeat','q_impure','answer')
for key,p in [('kin_car','קונם קונח קונס are substitutes for קרבן.'),('kin_cher','חרק חרך חרף are substitutes for חרם.'),('kin_naz','נזיק נזיח פזיח are substitutes for naziriteship.'),('kin_oath','שבותה שקוקה נודר במוהי are substitutes for an oath.')]:claim('10a:11',key,'anonymous Mishnah',p)
claim('10a:12','y_lang','רבי יוחנן','Kinuyim are expressions of the nations’ languages.')
claim('10a:12','l_invent','רבי שמעון בן לקיש','Kinuyim are expressions invented by the Sages for making vows.')
claim('10a:12','bada','anonymous scriptural citation','בחדש אשר בדא מלבו is cited as an example of the sense of בדא, inventing.',unc=['The citation explains the wording; it is not evidence that this verse directly legislated kinuyim.'])
edge('10a:12','bada','l_invent','support')
question('10a:13','q_institute','Why did the Rabbis institute kinuyim?')
claim('10a:13','avoid_car','anonymous answer','Kinuyim prevent saying קרבן.',conditions=['Explanation of the Sages-invented account.'])
question('10a:13','q_car','Why not simply say קרבן?')
claim('10a:13','fear_car','anonymous answer','One might say קרבן לה׳.')
question('10a:13','q_divine','Why not say קרבן לה׳?')
claim('10a:13','fear_vain','anonymous answer','One might utter לה׳ and fail to say קרבן, thus uttering the divine name in vain.')
edge('10a:13','avoid_car','q_institute','answer');edge('10a:13','fear_car','q_car','answer');edge('10a:13','fear_vain','q_divine','answer')
add('utterances','10a:14',dict(textual_voice='anonymous baraita introducer',discourse_role='Introduces R. Shimon; content continues in 10b:1–2.',composition='atomic'))
add('attributions','10a:14',dict(surface='רבי שמעון',role='quoted_authority',candidates=['רבי שמעון'],scope='Nedarim 10b:1–2',transmission_chain=[]),quote='רבי שמעון')
claim('10b:1','s_order','רבי שמעון','Do not say לה׳ עולה / לה׳ מנחה / לה׳ תודה / לה׳ שלמים; קרבן לה׳ teaches putting the offering first.',conditions=['Sacrificial declaration.'])
question('10b:1','q_order','What is the source for not putting the divine name before the offering?')
edge('10b:1','s_order','q_order','answer')
claim('10b:2','s_vain','רבי שמעון, continued','If even one intending only to mention God’s name over an offering must say קרבן לה׳, needless utterance is all the more prohibited.')
edge('10b:2','s_vain','s_order','analogy');edge('10b:2','s_order','fear_vain','support')
question('10b:3','q_tannaim','Is the dispute over the origin of kinuyim a tannaitic dispute?')
claim('10b:3','bs_prohib','בית שמאי','Substitutes of substitutes are prohibited / effective vow expressions.')
claim('10b:3','bh_permit','בית הלל','Substitutes of substitutes are permitted / ineffective as vow expressions.')
claim('10b:4','align_bs','anonymous proposed alignment','The prohibiting position would hold that kinuyim are nations’ languages.',status='rejected')
claim('10b:4','align_bh','anonymous proposed alignment','The permitting position would hold that kinuyim were invented by the Sages.',status='rejected')
claim('10b:5','all_lang','anonymous first alternative','Both schools may hold kinuyim are nations’ languages.',status='hypothetical')
claim('10b:5','bs_speak','בית שמאי in first alternative','The nations use these secondary expressions too.',status='hypothetical')
claim('10b:5','bh_no','בית הלל in first alternative','The nations do not use these secondary expressions.',status='hypothetical')
edge('10b:5','all_lang','align_bh','objection');edge('10b:5','all_lang','q_tannaim','answer');edge('10b:5','bs_speak','bs_prohib','support');edge('10b:5','bh_no','bh_permit','support')
claim('10b:6','bs_decree','בית שמאי in alternative explanation','A decree prohibits secondary expressions on account of primary kinuyim.',status='hypothetical')
claim('10b:6','bh_nodecree','בית הלל in alternative explanation','No such decree is made for secondary expressions on account of primary kinuyim.',status='hypothetical')
edge('10b:6','bs_decree','bs_prohib','support');edge('10b:6','bh_nodecree','bh_permit','support')
for key,holder,p in [('v_sec','רב יוסף','Vow secondary expressions: מקנמנא מקנחנא מקנסנא.'),('c_sec','מפשאה','Cherem secondary expressions: חרקים חרכים חרפים.'),('n_sec','רב יוסף','Nazir secondary expressions: מחזקנא מנזחנא מפיחנא.')]:
 cid=claim('10b:7',key,'anonymous transmitted teaching',p,voice=holder+' reciting a teaching')
 add('attributions','10b:7',dict(surface=holder,role='transmitter',candidates=[holder],scope=cid,transmission_chain=[holder]),links=[cid])
question('10b:7','q_examples','What are secondary expressions for vows, cherem, and naziriteship?')
for k in ['v_sec','c_sec','n_sec']:edge('10b:7',k,'q_examples','answer')
for key,term in [('mif','מיפחזנא'),('mit','מיתחזנא'),('mita','מיתעזנא')]:question('10b:8','q_'+key,'What is the status of '+term+'?',status='none')
question('10b:8','q_kinma','Ravina asks Rav Ashi: does קינמא mean קונם or cinnamon spice?',status='none')
claim('10b:8','kinma_v','anonymous alternatives in Ravina question','קינמא might mean קונם.',status='queried')
claim('10b:8','kinma_sp','anonymous alternatives in Ravina question','קינמא might mean cinnamon spice.',status='queried')
add('attributions','10b:8',dict(surface='רבינא',role='speaker',candidates=['רבינא'],scope=labels['q_kinma'],transmission_chain=[]),links=[labels['q_kinma']])
question('10b:9','q_kina','Rav Aha son of Rav Hiyya asks Rav Ashi: does קינה mean a chicken nest or a form of קונם?',status='none')
claim('10b:9','kina_nest','alternatives in רב אחא בריה דרב חייא question','קינה might refer to a chicken nest.',status='unresolved')
claim('10b:9','kina_v','alternatives in רב אחא בריה דרב חייא question','קינה might be an expression of קונם.',status='unresolved')
add('attributions','10b:9',dict(surface='רב אחא בריה דרב חייא',role='speaker',candidates=['רב אחא בריה דרב חייא'],scope=labels['q_kina'],transmission_chain=[]),links=[labels['q_kina']])
question('10b:10','q_oath_sec','What are secondary oath expressions?')
claim('10b:10','oath_initial','anonymous dialectic','Initial proposed forms are שבואל שבותיאל שקוקאל.',status='rejected')
claim('10b:10','shebuel','anonymous objection','שבואל signifies Shvuel son of Gershom.')
claim('10b:10','oath_correct','anonymous correction','The corrected first form is שבובאל, with שבותיאל and שקוקאל.',status='queried',unc=['מהו leaves status queried; do not convert the corrected list into an unequivocal final ruling.'])
question('10b:10','q_oath_correct','What is the status of שבובאל שבותיאל שקוקאל?',status='partial')
for key,word in [('ashiv','אשיבתא'),('ashk','אשקיקא'),('kar','קרינשא')]:claim('10b:10',key,'שמואל',word+' accomplishes nothing as an oath expression.')
edge('10b:10','shebuel','oath_initial','objection');edge('10b:10','oath_correct','oath_initial','correction')
claim('10b:11','mohi_repeat','anonymous Mishnah quotation','נדר במוהי is listed as an oath substitute.')
claim('10b:11','g_no','רבן שמעון בן גמליאל','Saying במוהי alone accomplishes nothing.')
claim('10b:11','g_yes','רבן שמעון בן גמליאל','במומתא דאמר מוהי is an oath substitute.',conditions=['The fuller expression במומתא דאמר מוהי.'])
edge('10b:11','g_yes','mohi_repeat','qualification',False)
for key,word in [('lch','לחולין שאוכל לך'),('kosher','לא כשר'),('dachi','לא דכי'),('tahor','טהור'),('tame','וטמא'),('notar','נותר'),('pigul','ופיגול')]:claim('10b:12',key,'anonymous Mishnah','The Mishnah lists '+word+' among the prohibited expressions.',conditions=['In the eating-vow formula of this Mishnah.'],unc=['Preserve the printed list: punctuation and inherited לא/contrast are interpretive.','11a:1–6 discusses the first formula and competing R. Judah attributions.'])
for key,word in [('imra','כאימרא'),('dir','כדירים'),('wood','כעצים'),('fire','כאשים'),('altar','כמזבח'),('temple','כהיכל'),('jeru','כירושלים')]:claim('10b:13',key,'anonymous Mishnah','The expression '+word+' is listed as an effective sacrificial comparison.',conditions=['Vow formula; supplied eating context.'])
claim('10b:13','service','anonymous Mishnah','A vow by any altar service object is a sacrificial vow even without explicitly mentioning קרבן.')
claim('10b:13','judah_jer','רבי יהודה','Saying ירושלים accomplishes nothing.',conditions=['The quoted core says ירושלים, without כ.'],unc=['11a:5 presents R. Judah also invalidating כירושלים unless one vows by an offering in Jerusalem; 11a:6 resolves through two tannaim reporting R. Judah.'])
claim('11a:1','lch_interp','anonymous initial interpretation','לחולין is initially read as not ordinary, but rather a sacrifice.',status='hypothetical')
claim('11a:4','all_j','anonymous reconciliation','The Mishnah can all be R. Judah, with the ending read as explaining his position.',status='reconciled')
claim('11a:5','j_other','רבי יהודה in baraita','Even כירושלים accomplishes nothing unless one vows by something offered in Jerusalem.')
claim('11a:6','two_j','anonymous resolution','There are two tannaitic reports of R. Judah.',status='reconciled')
edge('11a:1','lch_interp','lch','qualification');edge('11a:5','j_other','jeru','objection');edge('11a:6','two_j','j_other','local_resolution')

# Core boundaries are exact raw segment partitions; discourse-level continuation stays explicit.
for x in cores:
 boundary='open_both' if x in ['Nedarim 5b:8','Nedarim 6a:1','Nedarim 10a:14','Nedarim 10b:1','Nedarim 10b:2'] else 'closed'
 add('structure',x,dict(title='Independent source segment '+x,primary=True,boundary=boundary,legacy_ids=[]),origin='literal')

NOTES={
'5b:4':'Checked the rhetorical omission of לך and inference; Shmuel is the interpreted authority in left context, not the direct speaker here.',
'5b:5':'Both named positions and verse analogy retained; R. Idi original explanation vs Rava reporting retained.',
'5b:6':'Both get formulations and proposed alignments retained; not final exclusive pairings.',
'5b:7':'Compatibility argument retained with explicit later retraction at 6a:6.',
'5b:8':'Incomplete argument joined to 6a:1; Rava compatibility survives 6a:8.',
'6a:1':'Rava continuation, not anonymous new doctrine; rhetorical question retained.',
'6a:2':'Baraita, inference, and objection separately retained.',
'6a:3':'Rejected ownerless/charity explanation and objection from wording retained.',
'6a:4':'Revised one-person vs both-person scope and possible consecration retained.',
'6a:5':'Both sacrificial formulas and owed-offering condition retained; retraction context inspected.',
'10a:8':'Abaye grouping and backward references retained; Shimon the Righteous narrative read at 9b:5–10, R. Shimon at 10a:7.',
'10a:9':'Wine abstention, a-fortiori universal affliction, fasting conclusion and question retained.',
'10a:10':'Impure-nazir objection and repeated-sin answer retained; no invented details of repetition.',
'10a:11':'Four independent kinuy families retained without collapsing oath/nazir/vow/cherem.',
'10a:12':'Both origin theories and lexical verse citation retained.',
'10a:13':'Three successive questions and three answers retained.',
'10a:14':'Introduction only; no independent proposition completed here. Authority and forward scope retained.',
'10b:1':'All four divine-name-first examples retained in proposition and literal evidence; R. Shimon attribution inherited.',
'10b:2':'A-fortiori against vain utterance retained; inherited baraita attribution.',
'10b:3':'School positions and proposed tannaitic alignment question retained.',
'10b:4':'Both initial origin alignments retained as rejected necessary mappings.',
'10b:5':'Shared origin proposal and school-specific usage claims retained as first alternative.',
'10b:6':'Distinct decree alternative retained; not harmonized into usage account.',
'10b:7':'All nine expressions and three categories retained; Rav Yosef and מפשאה treated as reciters, not invented original holders.',
'10b:8':'Three individual nazir questions plus Ravina’s two-way lexical question retained unresolved; Rav Ashi is addressee, no answer attributed.',
'10b:9':'Both lexical possibilities and explicit תיבעי retained; Rav Aha is questioner, Rav Ashi addressee.',
'10b:10':'Initial/corrected lists, objection identifying Shvuel, question and all three Shmuel rulings retained. No unjustified equation of forms.',
'10b:11':'Mishnah repetition, R. Shimon ben Gamliel negative short form and positive fuller form retained.',
'10b:12':'All seven printed formulas retained; shared negative scope deliberately flagged; 11b:7–13a:7 checked for later sacrificial-comparison issue.',
'10b:13':'All seven comparisons, general altar-object rule, and R. Judah Jerusalem rule retained; two tannaim in his name preserved.'}

context_read=[]
for pg in [8,9,10,11,17,18,19,20,21,22,23,24]:
 for n,s in enumerate(src['text'][pg],1):
  rr=f'Nedarim {(pg+2)//2}{"a" if pg%2==0 else "b"}:{n}'
  if rr not in cores:context_read.append(rr)
coverage=[]
for x in cores:
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if r['layer']==layer and any(e['segment_id']==x for e in r['evidence'])]
  reason=NOTES[x.split(' ',1)[1]]
  if not ids and layer!='reconciliation':reason+=' No additional standalone '+layer+' item found after source pass; introduction-only or no explicit local question/edge as applicable.'
  coverage.append(dict(segment_id=x,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=reason))
payload={'artifact_kind':'immutable_source_only_independent_reading','job_id':j['job_id'],'execution':{'route':'interactive_agent','agent_id':'/root/nedarim_source_review020','model_id':None},'blindness':{'producer_annotations_read':False,'source_only_until_freeze':True,'annotated_handoff_read':False},'bindings':bindings,'job_sha256':sha(JOB),'plan_sha256':j['plan_sha256'],'core_refs':cores,'core_count':len(cores),'context_read_refs':context_read,'context_counts_as_core':False,'records':R,'coverage':coverage,'omission_reconciliation':NOTES,'unresolved_cases':['10b:8–9 lexical questions remain unresolved, including all three nazir forms.','10b:10 corrected oath forms have מהו; relation of Shmuel’s differently worded negatives to them is not forced.','10b:12 exact inherited negation and lexical punctuation require further scholarly interpretation; literal list preserved.','10b:13 / 11a:6 two tannaitic reports in R. Judah’s name, not a unified Jerusalem formulation.'],'context_outcomes':['6a:6 explicitly retracts Abaye’s compatibility with R. Judah; 6a:8 reiterates Rava’s compatibility with Rabbis.','9b:5–10 narrative describes one nazir accepted by Shimon the Righteous, temptation and vow; R. Yonah explains regret after impurity and extension. Context does not grant extra core credit.','10a:6–7 contrasts R. Judah’s early pious nazir practice with R. Shimon’s denial; Abaye groups the latter with sinner positions.','11a:1–6 discusses לחולין and the Mishnah’s R. Judah attribution; 11b:1–6 differentiates formulations and condition logic.','11b:7–13a:7 examines attachment to initial or permitted sacrificial state; proof attempts from notar, memorial fasts, thanksgiving terumah and firstborn are qualified or rejected. No decisive resolution imported into core Mishnah.','13a:8–12 repeats comparison formulas and differentiates לא אימרא / לאימרא.'],'scholarly_status':'AI provisional; source-only reading, not comparison or human certification','ml_eligible':False,'production_comparison_performed':False,'source_metadata':{k:v for k,v in src.items() if k!='text'}}

# Mechanical validation is separate from semantic reading.
ids={r['id'] for r in R};assert len(ids)==len(R)
import jsonschema
rs=schema['properties']['records']['items'];cs=schema['properties']['coverage']['items']
for r in R:
 jsonschema.validate(r,rs)
 for e in r['evidence']:assert text(e['segment_id'])[e['start_char']:e['end_char']]==e['quote']
 assert all(i in ids for i in r['links'])
for c in coverage:jsonschema.validate(c,cs)
for x in cores:
 spans=sorted((e['start_char'],e['end_char']) for r in R if r['layer']=='structure' and r['content']['primary'] for e in r['evidence'] if e['segment_id']==x)
 assert spans==[(0,len(text(x)))]
assert len(coverage)==240 and len(set(cores))==30
for b in j['selected_blocks']:
 p=next(p for p in plan['review_blocks'] if p['block_id']==b['block_id'])
 assert [s['ref'] for s in p['spans']]==b['core_refs']
 for s in p['spans']:assert hashlib.sha256(text(s['ref']).encode()).hexdigest()==s['span_sha256_utf8']
target=OUT/'nedarim_delegated020.json';raw=(json.dumps(payload,ensure_ascii=False,indent=2)+'\n').encode();digest=hashlib.sha256(raw).hexdigest()
with target.open('xb') as f:f.write(raw)
with target.with_suffix('.sha256').open('x',encoding='ascii') as f:f.write(digest+'  '+target.name+'\n')
receipt={'artifact':str(target),'sha256':digest,'author_script_sha256':sha(__file__),'agent_id':'/root/nedarim_source_review020','source_hash_verified':True,'all_bound_hashes_verified':True,'canonical_plan_hash_verified':True,'record_count':len(R),'core_count':30,'coverage_cells':240,'exact_evidence_valid':True,'unique_ids_links_valid':True,'typed_record_schema_valid':True,'structure_partition_valid':True,'sample_span_hashes_valid':True,'semantic_certification':False,'production_comparison':False}
with (OUT/'validation_receipt.json').open('x',encoding='utf-8') as f:json.dump(receipt,f,indent=2)
print(json.dumps(receipt,indent=2))
