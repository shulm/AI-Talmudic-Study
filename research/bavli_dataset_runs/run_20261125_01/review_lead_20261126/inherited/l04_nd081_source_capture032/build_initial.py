import json,hashlib,pathlib,re,collections
import jsonschema
OUT=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261127_delegated081')
JOB=pathlib.Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/jobs/bavli_nedarim_delegated081.json')
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(JOB.read_bytes())=='011325327ca3a8e64c4c479ebbf75a5f146bba4ee8a68b375a893c13326205dc'
j=json.loads(JOB.read_text(encoding='utf-8-sig'))
for x in [j['source'],j['original_source_schema'],j['frozen_plan']]+j['common_documents']:
 assert sha(pathlib.Path(x['path']).read_bytes())==x['sha256'],x['path']
src=json.loads(pathlib.Path(j['source']['path']).read_text(encoding='utf-8-sig'))
plan=json.loads(pathlib.Path(j['frozen_plan']['path']).read_text(encoding='utf-8-sig'))
payload={k:v for k,v in plan.items() if k!='plan_sha256'}
assert sha(b'bavli-source-only-review-plan-v1\0'+json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode())==j['plan_sha256']==plan['plan_sha256']
def ref(p,i): return f'Nedarim {p//2+1}{"ab"[p%2]}:{i+1}'
texts={ref(p,i):t for p,pg in enumerate(src['text']) for i,t in enumerate(pg)}
def R(short): return 'Nedarim '+short
core=j['core_refs']; assert len(core)==len(set(core))==30
for b in j['selected_blocks']:
 pb=next(z for z in plan['review_blocks'] if z['block_id']==b['block_id'])
 assert b['core_refs']==[z['ref'] for z in pb['spans']]
 assert pb['roles']==b['roles']
 for z in pb['spans']:
  t=src['text'][z['page_index']][z['segment_index']]
  assert ref(z['page_index'],z['segment_index'])==z['ref']
  assert z['offsets_codepoints']==[0,len(t)] and sha(t.encode())==z['span_sha256_utf8']
records=[]; labels={}; counts=collections.Counter()
def ev(r,q=None):
 r=R(r) if not r.startswith('Nedarim ') else r
 t=texts[r]; q=t if q is None else q; start=t.index(q)
 return {'segment_id':r,'start_char':start,'end_char':start+len(q),'quote':q}
def add(layer,label,r,q,content,links=(),unc=(),origin='source_paraphrase'):
 counts[layer]+=1; ident=f'nd081.{layer}.{counts[layer]:04}'
 assert label not in labels
 labels[label]=ident
 records.append({'id':ident,'layer':layer,'evidence':[ev(r,q)],'content':content,'origin':origin,'uncertainty':list(unc),'links':[labels[x] for x in links]})
 return ident
def c(label,r,q,prop,holder='anonymous',cond=(),mode='asserted',status=None,unc=(),chain=()):
 add('claims',label,r,q,{'proposition':prop,'conditions':list(cond),'scope':R(r),'assertion_mode':mode},unc=unc)
 add('utterances',label+'.u',r,q,{'textual_voice':holder,'discourse_role':status or mode,'composition':'atomic'},[label],unc)
 add('attributions',label+'.a',r,q,{'surface':holder,'role':'anonymous' if holder=='anonymous' else 'position_holder','candidates':[] if holder=='anonymous' else [holder],'scope':prop,'transmission_chain':list(chain)},[label],unc)
 add('positions',label+'.p',r,q,{'holder_candidates':[] if holder=='anonymous' else [holder],'claim_id':labels[label],'question_id':None,'conditions':list(cond),'local_status':status or mode},[label],unc)
 if chain:
  for n,name in enumerate(chain[:-1]):
   add('attributions',label+'.tr'+str(n),r,q,{'surface':name,'role':'transmitter','candidates':[name],'scope':prop,'transmission_chain':list(chain)},[label])
def question(label,r,q,form,cond=(),status='partial'):
 add('questions',label,r,q,{'formulation':form,'question_origin':'explicit','conditions':list(cond),'answer_set_status':status})
 add('utterances',label+'.u',r,q,{'textual_voice':'anonymous unless separately specified','discourse_role':'question/objection','composition':'atomic'},[label])
def edge(label,r,q,a,b,rel,explicit=True):
 add('edges',label,r,q,{'source_id':labels[a],'target_id':labels[b],'relation':rel,'explicitness':'source_explicit' if explicit else 'editorial_reconstruction'},[a,b],origin='source_paraphrase' if explicit else 'editorial_inference')
# All semantic selections below are manually source-read; no textual rules infer speakers or semantics.
c('az','18b:2','אם בשל עבודה זרה נדר מותר','The comparison vow is permitted when intended as idolatrous meat/wine.','anonymous',['Mishnah example continues 18b:1; specified idolatrous referent'])
c('stam','18b:2','ואם סתם אסור','Unspecified referent in preceding comparison is forbidden.','anonymous',['No clarification'])
for label,r,obj,a,b in [('cherem','18b:3','חרם','כחרם של שמים','כחרם של כהנים'),('maaser','18b:4','מעשר','כמעשר בהמה נדר ','של גורן'),('terumah','18b:5','תרומה','כתרומת הלשכה נדר ','של גורן')]:
 c(label+'yes',r,'אם '+a+' אסור' if label!='cherem' else 'אם כחרם של שמים אסור',f'Vow comparing to {obj} is prohibited for the sacred referent specified.', 'רבי מאיר' if label=='terumah' else 'anonymous',[a])
 c(label+'no',r,'ואם '+b+' מותר',f'Vow comparing to {obj} is permitted for the other specified referent.','רבי מאיר' if label=='terumah' else 'anonymous',[b])
 q='ואם סתם  אסור' if label=='terumah' else 'ואם סתם אסור'
 c(label+'stam',r,q,f'Unspecified {obj} comparison is forbidden.','רבי מאיר' if label=='terumah' else 'anonymous',['Unspecified'],unc=['Mishnah closes with דברי רבי מאיר; range back through preceding clauses is not explicitly delimited.'] if label=='terumah' else [])
c('tj','18b:6','סתם תרומה ביהודה אסורה','Unspecified terumah is prohibited in Judea.','רבי יהודה',['Judea'])
c('tg','18b:6','בגליל מותרת שאין אנשי גליל מכירין את תרומת הלשכה','Unspecified terumah is permitted in Galilee because people there do not recognize chamber terumah.','רבי יהודה',['Galilee'])
c('cj','18b:6','סתם חרמים ביהודה מותרין','Unspecified charamim are permitted in Judea.','רבי יהודה (surface clause; reassigned by Abaye in 19b:11)',['Judea'],status='surface attribution qualified by continuation',unc=['Abaye assigns latter clause to רבי אלעזר ברבי צדוק; do not retain as unqualified Rabbi Judah position.'])
c('cg','18b:6','בגליל אסורין שאין אנשי גליל מכירין את חרמי הכהנים','Unspecified charamim are forbidden in Galilee because its people do not recognize priestly charamim.','רבי יהודה (surface clause; reassigned by Abaye in 19b:11)',['Galilee'],status='surface attribution qualified by continuation')
question('qnaz','18b:7','והתנן ספק נזירות להקל','How reconcile stringent unspecified vows with lenient doubtful naziriteship?')
c('nazlen','18b:7','ספק נזירות להקל','Doubtful naziriteship is treated leniently.','anonymous quoted Mishnah',status='cited objection')
c('zeira','18b:8','אמר רבי זירא לא קשיא הא רבי אליעזר הא רבנן','Rabbi Zeira distinguishes Rabbi Eliezer from the Rabbis to reconcile the teachings.','רבי זירא',status='initial answer superseded locally by alternative at 19a:10',unc=['Mapping established through ensuing argument and Abaye, not by name order.'])
c('koyyes','18b:8','המקדיש חייתו ובהמתו הקדיש את הכוי','Dedicating one’s wild and domestic animals includes the koy.','רבנן',['Dedicates both חייתו ובהמתו'],status='quoted baraita')
c('koyno','18b:8','רבי אליעזר אומר לא הקדיש את הכוי','Rabbi Eliezer excludes the koy from this dedication.','רבי אליעזר',['Same dedication'],status='quoted baraita')
c('riskyes','18b:9','מאן דאמר ממונו מעייל לספיקא גופיה נמי מעייל','Who includes his property in uncertainty also includes himself.','anonymous',['Property-inclusion view'],status='explanation of initial answer')
c('riskno','18b:9','ומאן דאמר ממונו לא מעייל לספיקא גופיה (נמי)','Who excludes his property from doubt all the more excludes himself (completed next segment).','anonymous',['Property-exclusion view'],status='argument continues 19a:1')
c('risknoend','19a:1','כל שכן דלא מעייל לספיקא','All the more he does not enter uncertainty concerning himself.','anonymous',['Continuation of 18b:9'],status='completion')
question('abayeq','19a:2','במאי אוקימתא לספק נזירות להקל כרבי אליעזר אימא סיפא','Abaye challenges assignment of lenient doubtful naziriteship to Rabbi Eliezer by the sequel.')
add('attributions','abayeq.a','19a:2','אמר ליה אביי',{'surface':'אביי','role':'speaker','candidates':['אביי'],'scope':'abayeq','transmission_chain':[]},['abayeq'])
c('firstborn','19a:2','ספק בכורות אחד בכורי אדם ואחד בכורי בהמה בין טמאה בין טהורה המוציא מחבירו עליו הראייה','For doubtful firstborn human or animal, clean or unclean, claimant must bring proof.','anonymous quoted Mishnah',['Doubtful firstborn; human or animal, clean or unclean'],status='cited objection')
c('shear','19a:3','ואסורים בגיזה ועבודה','These doubtful firstborn animals are prohibited for shearing and work.','anonymous cited supplementary teaching',['Animal cases from preceding firstborn teaching'],status='cited objection')
question('autoq','19a:4','אמאי קא מדמית קדושה הבאה מאליה לקדושה הבאה בידי אדם','Why compare automatically arising sanctity to sanctity created by a person?')
c('autodist','19a:4','קדושה הבאה מאליה לקדושה הבאה בידי אדם','Automatic sanctity differs from sanctity brought about by a person for this objection.','anonymous reply',['Firstborn versus dedication'],mode='reconciled',unc=['Reply is אמר ליה without repeated name; likely respondent Rabbi Zeira but not explicitly named here.'])
c('liquidself','19a:5','ספק משקין ליטמא טמא','Doubtful liquids are impure as to receiving impurity.','רבי מאיר',['Doubtful liquid impurity'],status='quoted alternative objection')
c('liquidothers','19a:5','לטמא אחרים טהור','They are pure for transmitting impurity to others.','רבי מאיר',['Doubtful liquid impurity'],status='quoted alternative objection')
c('elazaragree','19a:5','וכן היה רבי אלעזר אומר כדבריו','Rabbi Elazar agreed with the foregoing liquid-impurity distinction.','רבי אלעזר',status='reported position then challenged',unc=['Source spelling אלעזר here versus אליעזר at 18b:8 is preserved without silently resolving identity.'])
question('elazarq','19a:6','ומי סבירא ליה לרבי אלעזר ליטמא טמא','Does Rabbi Elazar really hold that these liquids themselves are impure?')
c('noliq','19a:7','רבי אלעזר אומר אין טומאה למשקין כל עיקר','Rabbi Elazar says liquids have no impurity at all.','רבי אלעזר',status='counter-cited baraita; reading differentiated under Shmuel versus Rav')
c('kamtza','19a:7','העיד יוסי בן יועזר איש צרידה על איל קמצא דכן','Yosi ben Yoezer of Tzeredah testified that איל קמצא is pure.','יוסי בן יועזר איש צרידה',status='quoted testimony within Rabbi Elazar proof',chain=['רבי אלעזר','יוסי בן יועזר איש צרידה'],unc=['No zoological identification supplied by local source.'])
c('slaughterliq','19a:7','ועל משקין בית מטבחיא דכן','He testified that liquids of the slaughterhouse are pure.','יוסי בן יועזר איש צרידה',status='quoted testimony; sense disputed in continuation',chain=['רבי אלעזר','יוסי בן יועזר איש צרידה'])
c('shmuel','19a:8','לשמואל דאמר דכן מלטמא אחרים אבל טומאת עצמן יש בהן','Shmuel interprets pure as not imparting impurity, while the liquids themselves possess impurity.','שמואל',status='interpretation makes prior distinction workable')
c('rav','19a:9','לרב דאמר דכן ממש','Rav interprets pure as fully pure.','רב',status='interpretation makes prior answer problematic')
question('ravq','19a:9','מאי איכא למימר','What can be said under Rav’s complete-purity interpretation?')
c('replacement','19a:10','אלא הא רבי יהודה והא רבי שמעון','Replace prior tanna distinction with Rabbi Judah and Rabbi Shimon.','anonymous',status='alternative answer',unc=['Lenient/strict mapping follows explicit baraita at 19a:11.'])
c('heapjudah','19a:11','רבי יהודה מתיר','Rabbi Judah permits the doubtful nazirite vow.','רבי יהודה',['Conditional nazirite vow: heap has one hundred kor; heap then found stolen or lost'],status='quoted baraita')
c('heapshimon','19a:11','ורבי שמעון אוסר','Rabbi Shimon prohibits in that case.','רבי שמעון',['Conditional nazirite vow: heap has one hundred kor; heap then found stolen or lost'],status='quoted baraita')
question('judahq','19a:12','מי אמר רבי יהודה לא מעייל איניש נפשיה לספיקא','Does Rabbi Judah hold a person does not put himself into uncertainty, given his terumah ruling?')
c('judahcite','19a:12','רבי יהודה אומר סתם תרומה ביהודה אסורה ובגליל מותרת שאין אנשי הגליל מכירין את תרומת הלשכה','Rabbi Judah’s regional terumah ruling is cited again against his leniency in the heap case.','רבי יהודה',['Regional familiarity'],status='repeat occurrence used as objection')
c('recognition','19a:12','טעמא דאין מכירין','Permission is inferred to depend on nonrecognition; recognition would prohibit (completed 19b:1).','anonymous',['Inference from Galilee rationale'],status='challenging inference',unc=['Not a freestanding enduring rule; reconciliation follows.'])
# Context closes questions without increasing sampled core count.
c('rava','19b:2','אמר רבא גבי כרי קסבר כל שספיקו חמור מוודאי לא מעייל נפשיה לספיקא','Rava limits unwillingness to enter doubt to cases where doubt is more severe than certainty.','רבא',['Heap nazirite case'],mode='reconciled')
c('ravawhy','19b:2','דאילו גבי נזיר ודאי מגלח ומביא קרבן ונאכל על ספיקו לא מצי מגלח','Certain nazirite can shave and bring an edible sacrifice; doubtful one cannot shave.','רבא',['Certain versus doubtful naziriteship'],status='reason')
question('worldq','19b:3','אמר הריני נזיר עולם מאי','What if he said lifelong nazirite?')
c('world','19b:4','נזיר עולם נמי ספיקו חמור מודאי','Lifelong nazirite likewise has doubt more stringent than certainty.','רבא',['Certain can lighten heavy hair with razor and bring three animals; doubtful cannot'])
question('samsonq','19b:5','אמר הריני נזיר שמשון מאי','What if he said Samson nazirite?')
c('samsonnot','19b:6','נזיר שמשון לא תניא','The Samson case is initially said not to be taught.','anonymous respondent (Rava in dialogue)',status='conceded conditionally after contrary report')
c('samsontaught','19b:6','והאמר רב אדא בר אהבה תניא נזיר שמשון','Rav Adda bar Ahavah is reported to teach the Samson case.','רב אדא בר אהבה',status='counterreport')
c('samsonconcede','19b:6','אי תניא תניא','If it is taught, it is taught.','anonymous respondent (Rava in dialogue)',mode='conditional',status='concession; no supplied harmonization')
c('ashi','19b:7','רב אשי אמר ההיא רבי יהודה משום רבי טרפון היא','Rav Ashi explains the lenient teaching as Rabbi Judah in Rabbi Tarfon’s name.','רב אשי',status='alternative explanation')
c('haflaah','19b:7','רבי יהודה משום רבי טרפון אומר אין אחד מהם נזיר לפי שלא ניתנה נזירות אלא להפלאה','None is a nazirite because naziriteship requires explicit determination.','רבי טרפון',chain=['רבי יהודה','רבי טרפון'],status='quoted reason in alternative answer')
question('stolenq','19b:8','מאי איריא שנגנב או שאבד','Then why specifically say stolen or lost?')
c('shimonforce','19b:8','להודיעך כוחו דרבי שמעון דאף על גב דנגנב או שאבד קסבר מעייל איניש נפשיה לספיקא','The wording shows Rabbi Shimon’s strength: he includes himself in uncertainty even after theft/loss.','anonymous',['Rabbi Shimon view'],status='answer')
c('abayeremap','19b:11','אמר אביי סיפא רבי אלעזר ברבי צדוק היא','Abaye assigns latter charamim clause to Rabbi Elazar ben Rabbi Tzadok.','אביי',status='local reassignment')
c('charamtzadok','19b:11','רבי אלעזר ברבי צדוק אומר סתם חרמים בגליל אסורין','Rabbi Elazar ben Rabbi Tzadok forbids unspecified charamim in Galilee.','רבי אלעזר ברבי צדוק',['Galilee'],status='baraita corroborates reassignment')
# Narrative, ethical teaching, evidence, and chapter transition.
c('rebbistory','20b:6','ההיא דאתאי לקמיה דרבי אמרה לו רבי ערכתי לו שולחן והפכו','A woman comes before Rabbi and reports arranging a table which her husband overturned.','anonymous narrator',status='narrative with woman’s reported complaint',unc=['Euphemism preserved; no additional act-specific rule inferred.'])
c('rebbeanswer','20b:6','בתי תורה התירתך ואני מה אעשה ליך','Rabbi replies that Torah permitted her to him and asks what he can do for her.','רבי',status='reported response')
c('ravstory','20b:6','ההיא דאתאי לקמיה דרב אמרה לו רבי ערכתי לו שולחן והפכו','A second woman comes before Rav with the same reported complaint.','anonymous narrator',status='separate narrative occurrence')
c('ravfish','20b:6','מאי שנא מן ביניתא','Rav responds by asking how it differs from a fish.','רב',status='rhetorical analogy to prior permission',unc=['Meaning depends on fish analogy in 20b:4 context.'])
question('fishq','20b:6','מאי שנא מן ביניתא','How does this differ from fish?',status='topic_inventory')
c('cup','20b:7','אל ישתה אדם בכוס זה ויתן עיניו בכוס אחר','A person should not drink from this cup while directing his eyes to another.','רבי',status='euphemistic admonition derived from verse')
c('twowives','20b:7','לא נצרכא אלא דאפילו שתי נשיו','Ravina applies this even to one’s two wives.','רבינא',['Even both women are his wives'],status='scope qualification')
c('nine','20b:8','אמר רבי לוי אלו בני תשע מדות בני אסנ"ת משגע"ח','Rabbi Levi identifies the verse’s rebels/transgressors with offspring of nine measures and supplies a mnemonic.','רבי לוי',unc=['Heading says nine; next segment explicitly lists ten terms. No harmonization is supplied here.'])
for n,term in enumerate(['בני אימה','בני אנוסה','בני שנואה','בני נידוי','בני תמורה','בני מריבה','בני שכרות','בני גרושת הלב','בני ערבוביא','בני חצופה']):
 c('measure'+str(n),'20b:9',term,f'{term} is included in the enumerated offspring categories.','רבי לוי (inherited list)',status='enumeration',unc=['Local passage gives term without defining it; do not invent gloss.'])
question('demandq','20b:10','איני והאמר רבי שמואל בר נחמני אמר רבי יונתן','Challenge to inclusion of בני חצופה from praise of wife-initiated relations.')
c('demandgood','20b:10','כל אדם שאשתו תובעתו הויין לו בנים שאפילו בדורו של משה רבינו לא היו כמותם','One whose wife requests him has sons unmatched even in Moses’s generation.','רבי יונתן',['Wife requests him'],status='reported claim used as objection; qualified in 20b:12',chain=['רבי שמואל בר נחמני','רבי יונתן'])
c('mosesproof','20b:10','הבו לכם אנשים חכמים ונבונים וכתיב ואקח את ראשי שבטיכם ולא כתיב נבונים','Requested wise/discerning men are contrasted with appointment verse omitting discerning.','anonymous citation within report',status='scriptural support')
c('issacharproof','20b:11','וכתיב יששכר חמור גרם וכתיב מבני יששכר יודעי בינה לעתים','Issachar verses connect the example with descendants understanding the times.','anonymous citation within report',status='scriptural support',unc=['Connection to wife’s request is not retold in this passage.'])
c('coax','20b:12','ההיא דמרציא ארצויי','The praised case is where she coaxes/conciliates.','anonymous',['Case of praised request'],mode='reconciled',status='distinguishes earlier condemned category')
for n,k in enumerate(['נדרי זרוזין','נדרי הבאי','נדרי שגגות','נדרי אונסין']):
 c('vow'+str(n),'20b:14',k,f'Sages permitted {k} as one of the four vow classes.','חכמים (anonymous Mishnah)',status='enumerated rule')
c('seller','20b:14','היה מוכר חפץ ואמר קונם שאיני פוחת לך מן הסלע','Seller declares a konam against reducing price below a sela.','anonymous Mishnah',['Bargaining example'],status='quoted hypothetical seller declaration')
c('buyer','20b:14','והלה אומר קונם שאיני מוסיף לך על השקל','Buyer declares a konam against increasing price above a shekel.','anonymous Mishnah',['Same bargaining example'],status='quoted hypothetical buyer declaration')
c('three','21a:1','שניהם רוצין בשלושה דינרין','Both desire a price of three dinars.','anonymous Mishnah',['Seller and buyer declarations in previous segment'],status='operative intent condition for bargaining vows')
c('firsttanna','21a:2','מאן תנא ארבעה נדרים רבי יהודה היא דאמר משום רבי טרפון','Rabbi Abba bar Mamal recalls Rabbi Ami’s report in Rabbi Judah Nesia’s name identifying the four-vow tanna as Rabbi Judah citing Rabbi Tarfon.','רבי יהודה נשיאה',chain=['רבי אבא בר ממל','רבי אמי','רבי יהודה נשיאה'],status='initial identification followed by Rava alternative',unc=['Judah Nesia and Judah citing Tarfon are not collapsed.'])
c('ravavows','21a:3','רבא אמר אפילו תימא רבנן מי קתני שניהן רצו  שניהן רוצין קתני','Rava allows even the Rabbis: text says both presently desire, not that both later desired.','רבא',status='alternative interpretation emphasizing existing intent')
question('priceq','21a:4','אמר לו טפי מסלע והלה אמר בציר משקל נדרא הוי או זירוזין הוי','Ravina asks Rav Ashi whether more-than-sela / less-than-shekel declarations are vows or bargaining pressure.')
c('priceunresolved','21b:2','או דלמא דווקא קאמר ונידרא הוי תיבעי','The stronger-price formulation remains unresolved: perhaps exact wording intended and vow effective.','anonymous',['Different price wording from Mishnah'],mode='unresolved')
# Explicit evidence/relations between independently anchored records.
for args in [
('e1','18b:8','לא קשיא','zeira','qnaz','answer'),
('e2','18b:9','מאן דאמר ממונו מעייל לספיקא גופיה נמי מעייל','riskyes','zeira','support'),
('e3','19a:1','כל שכן','risknoend','riskno','continuation'),
('e4','19a:2','אימא סיפא','firstborn','zeira','objection'),
('e5','19a:3','ותני עלה','shear','firstborn','continuation'),
('e6','19a:4','אמאי קא מדמית','autodist','abayeq','answer'),
('e7','19a:5','אלא אי קשיא הא קשיא','liquidself','zeira','objection'),
('e8','19a:7','והתניא','noliq','elazaragree','objection'),
('e9','19a:7','תדע שהרי העיד','slaughterliq','noliq','support'),
('e10','19a:8','הניחא לשמואל','shmuel','noliq','qualification'),
('e11','19a:9','מאי איכא למימר','ravq','elazaragree','objection'),
('e12','19a:10','אלא','replacement','qnaz','answer'),
('e13','19a:11','דתניא','heapjudah','replacement','support'),
('e14','19a:11','ורבי שמעון אוסר','heapshimon','replacement','support'),
('e15','19a:12','ורמינהי','judahcite','heapjudah','objection'),
('e16','19b:2','אמר רבא גבי כרי','rava','judahq','answer'),
('e17','19b:2','דאילו גבי נזיר','ravawhy','rava','support'),
('e18','19b:4','נזיר עולם נמי','world','worldq','answer'),
('e19','19b:6','והאמר רב אדא בר אהבה','samsontaught','samsonnot','objection'),
('e20','19b:6','אי תניא תניא','samsonconcede','samsonnot','qualification'),
('e21','19b:7','רב אשי אמר','ashi','judahq','answer'),
('e22','19b:8','להודיעך כוחו','shimonforce','stolenq','answer'),
('e23','19b:11','סיפא רבי אלעזר ברבי צדוק היא','abayeremap','cj','correction'),
('e24','19b:11','רבי אלעזר ברבי צדוק אומר','charamtzadok','abayeremap','support'),
('e25','20b:7','לא נצרכא אלא דאפילו שתי נשיו','twowives','cup','qualification'),
('e26','20b:10','איני והאמר','demandgood','measure9','objection'),
('e27','20b:10','שנאמר','mosesproof','demandgood','support'),
('e28','20b:11','וכתיב','issacharproof','demandgood','support'),
('e29','20b:12','ההיא דמרציא ארצויי','coax','demandq','answer'),
('e30','21a:1','שניהם רוצין בשלושה דינרין','three','seller','qualification'),
('e31','21a:3','אפילו תימא רבנן','ravavows','firsttanna','qualification'),
('e32','21b:2','תיבעי','priceunresolved','priceq','unresolved_outcome')]: edge(*args)
# Primary structures partition entire core strings including edition markup.
for r in core:
 short=r.split(' ',1)[1]
 if r=='Nedarim 20b:13': title='Edition chapter-ending colophon, not attributed Talmudic proposition'; boundary='closed'
 elif short.startswith('18b:') and int(short.split(':')[1])<=6: title='Mishnah: ambiguous comparison vows and regional usage'; boundary='open_both'
 elif short.startswith(('18b:','19a:')): title='Gemara: uncertainty, sanctity, liquid impurity, and alternative tannaitic attribution'; boundary='open_both'
 elif r=='Nedarim 20b:6': title='Two distinct reported encounters and replies'; boundary='open_left'
 elif r in ['Nedarim 20b:14','Nedarim 21a:1']: title='New chapter Mishnah: four permitted vow classes and bargaining intent'; boundary='open_both'
 else: title='Ethical teachings, offspring categories and challenge/resolution'; boundary='open_both'
 add('structure','structure.'+short,r,None,{'title':title,'primary':True,'boundary':boundary,'legacy_ids':[]},origin='editorial_inference')
# Context inventory: every original text segment displayed to reader, explicitly distinct from cores.
seen=[ref(p,i) for p in range(34,42) for i in range(len(src['text'][p]))]
# 21b was displayed only through segment 9, but page 41 has nine source strings; assert against accidental claim.
assert len(src['text'][41])==9
context=[r for r in seen if r not in core]
notes={r:'Source-only omission pass checked conditions, holder versus transmitter, explicit and anonymous voices, argument role, and continuation; no name-order attribution.' for r in core}
notes.update({R('18b:2'):'Read 18b:1 to recover the meat/wine antecedent; both specified-idolatry and unspecified alternatives retained.',R('18b:6'):'Regional permission/prohibition and both familiarity rationales retained. Charamim surface attribution explicitly qualified by Abaye 19b:11.',R('18b:9'):'Sentence continues at 19a:1; parenthesized נמי preserved literally.',R('19a:5'):'Elazar spelling preserved rather than silently merged into preceding Eliezer. Two liquid-impurity scopes and reported agreement separately inventoried.',R('19a:7'):'Both Yosi ben Yoezer testimony objects retained; report chain distinguished from Rabbi Elazar proof.',R('19a:12'):'Repeated Judah occurrence retained; continuation contains Rava explanation, Samson concession, and Rav Ashi alternative.',R('20b:6'):'Both separate women/authority narratives retained, including Rabbi and Rav responses, and rhetorical fish question.',R('20b:9'):'All ten lexical list members separately inventoried; inconsistency with nine heading is unresolved, no harmonizing conjecture.',R('20b:13'):'Only HTML breaks and chapter colophon. Full structural ownership; zero semantic/utterance/attribution records intentional, no invented sage.',R('20b:14'):'Four vow classes and both hypothetical declarations retained. Intent appears in next segment and is not omitted.',R('21a:1'):'Joint intent retained; 21a:2–3 supplies initial tanna identification and Rava alternative. More extreme pricing query at 21a:4–21b:2 remains unresolved.'})
coverage=[]
for r in core:
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[z['id'] for z in records if z['layer']==layer and any(e['segment_id']==r for e in z['evidence'])]
  if layer=='reconciliation': result='none_found_after_pass'; rationale=notes[r]+' This is the source-only omission/reconciliation pass, not a producer comparison.'
  elif ids: result='records_found'; rationale=notes[r]
  else: result='not_applicable' if r==R('20b:13') else 'none_found_after_pass'; rationale=notes[r]+f' No independent {layer} record additionally identified in this segment; inherited context is not fabricated as fresh explicit speech.'
  coverage.append({'segment_id':r,'layer':layer,'extraction_state':'completed','extraction_result':result,'record_ids':ids,'rationale':rationale})
reading={'schema_version':'2.0.0-production','tractate':'Nedarim','owner':'independent_source_reader_nd_source_review081','epoch':1,'source_sha256':j['source']['sha256'],'protocol_sha256':j['common_documents'][0]['sha256'],'schema_sha256':j['common_documents'][1]['sha256'],'execution':{'route':'interactive_agent','agent_id':'/root/nd_source_review081','model_id':None},'records':records,'coverage':coverage,'open_tails':['No scholarly certification. Surface Elazar/Eliezer variation retained unresolved.','Nine heading / ten lexical list entries retained without emendation.','Context after 21b:3 begins a new inquiry about release and was incidentally displayed; it is not completed review scope.']}
schema=json.loads(pathlib.Path(j['common_documents'][1]['path']).read_text(encoding='utf-8-sig')); jsonschema.validate(reading,schema)
ids={z['id'] for z in records}; assert len(ids)==len(records)
for z in records:
 assert set(z['links'])<=ids
 for e in z['evidence']: assert texts[e['segment_id']][e['start_char']:e['end_char']]==e['quote']
 if z['layer']=='positions': assert z['content']['claim_id'] in ids
 if z['layer']=='edges': assert {z['content']['source_id'],z['content']['target_id']}<=ids
for r in core:
 spans=sorted((e['start_char'],e['end_char']) for z in records if z['layer']=='structure' and z['content']['primary'] for e in z['evidence'] if e['segment_id']==r)
 assert spans==[(0,len(texts[r]))]
assert len(coverage)==240 and {z['segment_id'] for z in coverage}==set(core)
receipt={'artifact_kind':'frozen_source_only_reading_receipt','reading_id':'bavli_nedarim_delegated081_initial','agent_id':'/root/nd_source_review081','job_sha256':sha(JOB.read_bytes()),'plan_sha256':j['plan_sha256'],'core_refs':core,'core_count':30,'selected_blocks':j['selected_blocks'],'context_read_refs':context,'context_count':len(context),'context_policy':'Only core refs count toward original probability sample. Context records selectively resolve core questions; incidental source display is declared, not claimed completed.','record_counts':dict(counts),'core_record_counts':dict(collections.Counter(z['layer'] for z in records if any(e['segment_id'] in core for e in z['evidence']))),'exposure_declaration':{'producer_outputs_read':False,'prior_readings_read':False,'comparison_outputs_read':False,'handoff_read_by_this_reader':False,'allowed_reads':'Pinned neutral descriptor, common protocol/schema/prompt, frozen source-only plan, original source schema, original source and own helper. Root stated it had satisfied project handoff prerequisite before delegation. Root supplied isolated output path because descriptor lacks it.','other_context':'Inherited user repository accuracy rules only; no source-label interpretation provided before reading.'},'validation':['descriptor and all resource byte hashes','domain-separated canonical plan hash','exact selected block membership/roles and original span hashes','Unicode codepoint half-open spans','schema 2.0.0-production','unique IDs and all links','exact complete core structural ownership','30 unique cores / 240 per-layer coverage rows','context-core disjointness'],'omission_inventory':notes,'limitations':['AI provisional source-only reading; no comparison, adjudication, production admission or eligibility action.','Attributions explicitly inherited or anonymous remain marked; no external commentary consulted.']}
def write(name,obj):
 p=OUT/name; b=json.dumps(obj,ensure_ascii=False,indent=2).encode();
 with p.open('xb') as f:f.write(b)
 with (OUT/(name+'.sha256')).open('x',encoding='ascii') as f:f.write(sha(b)+'  '+name+'\n')
 return sha(b)
receipt['reading_sha256']=write('reading_initial.json',reading)
receipt['helper_sha256']=sha(pathlib.Path(__file__).read_bytes())
write('validation_receipt_initial.json',receipt)
print(json.dumps({'reading_sha256':receipt['reading_sha256'],'helper_sha256':receipt['helper_sha256'],'counts':dict(counts),'context_count':len(context),'core_count':len(core),'coverage_rows':len(coverage)},indent=2))
