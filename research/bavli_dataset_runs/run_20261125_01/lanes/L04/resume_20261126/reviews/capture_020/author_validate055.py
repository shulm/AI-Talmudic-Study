import json, hashlib, pathlib, re, sys, collections
sys.stdout.reconfigure(encoding='utf8')
D=pathlib.Path(__file__).resolve().parent
J=pathlib.Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/jobs/bavli_taanit_delegated055.json')
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def read(p): return json.loads(pathlib.Path(p).read_text(encoding='utf-8-sig'))
j=read(J)
assert sha(J)=='56b184adee73bf0bb185586419c42f72b395a9a761ede0d2fd8645b70d5ba81b'
bindings=[j['source'],j['original_source_schema'],j['frozen_plan']]+j['common_documents']
for b in bindings: assert sha(b['path'])==b['sha256'],b
plan=read(j['frozen_plan']['path']); canon={k:v for k,v in plan.items() if k!='plan_sha256'}
assert hashlib.sha256(b'bavli-source-only-review-plan-v1\0'+json.dumps(canon,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()==j['plan_sha256']==plan['plan_sha256']
src=read(j['source']['path']); schema=read(j['common_documents'][1]['path'])
def raw(ref):
 m=re.fullmatch(r'(?:Taanit )?(\d+)([ab]):(\d+)',ref); return src['text'][2*(int(m[1])-1)+(m[2]=='b')][int(m[3])-1]
def ref(r): return r if r.startswith('Taanit ') else 'Taanit '+r
cores=j['core_refs']; selected=[]
for block in j['selected_blocks']:
 pb=next(b for b in plan['review_blocks'] if b['block_id']==block['block_id'])
 assert pb['roles']==block['roles'] and [s['ref'] for s in pb['spans']]==block['core_refs']
 for s in pb['spans']:
  t=raw(s['ref']); assert t==src['text'][s['page_index']][s['segment_index']]
  assert s['offsets_codepoints']==[0,len(t)] and hashlib.sha256(t.encode()).hexdigest()==s['span_sha256_utf8']
 selected+=pb['spans']
assert [s['ref'] for s in selected]==cores and len(set(cores))==30
R=[]; names={}; notes={}; questions={}
def ev(r,q=None):
 r=ref(r); t=raw(r); q=t if q is None else q; a=t.index(q); return {'segment_id':r,'start_char':a,'end_char':a+len(q),'quote':q}
def rec(layer,r,q,content,unc=None,links=None,origin='source_paraphrase'):
 rid='ta055.'+layer+'.'+str(len(R)+1).zfill(4)
 R.append(dict(id=rid,layer=layer,evidence=[ev(r,q)],content=content,origin=origin,uncertainty=unc or [],links=links or [])); return rid
def attr(r,q,holder,scope,role='position_holder',chain=None,unc=None):
 return rec('attributions',r,q,dict(surface=q or raw(r),role=role,candidates=[holder] if holder else [],scope=scope,transmission_chain=chain or []),unc)
def u(r,q,holder,role='teaching',unc=None):
 return rec('utterances',r,q,dict(textual_voice=holder,discourse_role=role,composition='atomic'),unc)
def qn(key,r,q,form,holder='anonymous editorial voice'):
 z=rec('questions',r,q,dict(formulation=form,question_origin='explicit',conditions=[],answer_set_status='topic_inventory')); questions[key]=z;u(r,q,holder,'question');attr(r,q,holder,form,'anonymous' if holder.startswith('anonymous') else 'speaker');return z
def edge(a,b,relation,r,q=None,explicit=True):
 return rec('edges',r,q,dict(source_id=a,target_id=b,relation=relation,explicitness='source_explicit' if explicit else 'editorial_reconstruction'),links=[a,b])
def c(key,r,q,p,holder='anonymous editorial voice',conditions=None,mode='asserted',status='Locally stated; no practical ruling inferred',question=None,unc=None,role='teaching',pos=True):
 z=rec('claims',r,q,dict(proposition=p,conditions=conditions or [],scope=ref(r)+'; '+role,assertion_mode=mode),unc)
 names[key]=z;u(r,q,holder,role,unc);attr(r,q,holder,p,'anonymous' if holder.startswith('anonymous') else 'position_holder',unc=unc)
 if pos: rec('positions',r,q,dict(holder_candidates=[holder],claim_id=z,question_id=questions.get(question),conditions=conditions or [],local_status=status),unc,links=[z]+([questions[question]] if question else []))
 if question:edge(z,questions[question],'answer',r,q)
 return z
def link(a,b,rel,r,q=None,explicit=True): return edge(names[a],names[b],rel,r,q,explicit)
# Only source-authored semantic specifications below; helper performs coordinates, not semantic extraction.
qn('second','6a:13','שניה למאי','What practical consequence attaches to the second reviyah?')
c('zeira','6a:13','אמר ר\' זירא לנדרים','The second reviyah matters for vows.','ר\' זירא',question='second')
c('vows','6b:1',None,'The quoted vow formulation עד הגשמים / משירדו גשמים has the endpoint of the second reviyah.','anonymous quoted Mishnah',conditions=['Vow formulated concerning the rains'],unc=['Punctuation is absent; preserve both surface formulations without imposing an unquoted distinction.'],role='Mishnah quotation')
link('vows','zeira','support','6b:1')
attr('6a:13','אמר ר\' זירא לנדרים דתנן','ר\' זירא','Introduces the Mishnah quotation continued in 6b:1','speaker')
c('olives','6b:2','רב זביד אמר לזיתים','Second reviyah governs olive gleaning availability.','רב זביד',question='second')
qn('glean','6b:2','מאימתי כל אדם מותרין בלקט בשכחה ובפאה','When may everyone take leket, shikhehah, and peah?','anonymous quoted Mishnah')
c('namush','6b:2','משילכו הנמושות','Leket, shikhehah and peah become available to everyone after the namushot have gone.','anonymous quoted Mishnah',conditions=['After namushot have passed'],question='glean',role='Mishnah quotation')
c('grape','6b:2','בפרט ובעוללות משילכו עניים בכרם ויבואו','Peret and olelot become available after the poor have gone through the vineyard and returned.','anonymous quoted Mishnah',conditions=['Poor have traversed the vineyard and returned'],role='Mishnah quotation')
c('oliveend','6b:2','בזיתים משתרד רביעה שניה','For olives the endpoint is the second reviyah.','anonymous quoted Mishnah',conditions=['Second reviyah has fallen'],role='Mishnah quotation')
link('oliveend','olives','support','6b:2')
qn('namushdef','6b:3','מאי נמושות','What does namushot mean?')
c('old','6b:3','אמר ר\' יוחנן סבי דאזלי אתיגרא','Namushot means old people walking with support.','ר\' יוחנן',question='namushdef',unc=['אתיגרא retained; exact lexical rendering not settled by this passage.'])
c('gleaners','6b:3','ר"ל אמר לקוטי בתר לקוטי','Namushot means gleaners following other gleaners.','ריש לקיש',question='namushdef',status='Alternative explanation; no resolution selecting one here')
c('paths','6b:4','רב פפא אמר כדי להלך בשבילי הרשות','Second reviyah sets the limit for using permitted private paths.','רב פפא',question='second')
c('pathrule','6b:4','דאמר מר מהלכין כל אדם בשבילי הרשות עד שתרד רביעה שניה','Everyone may use the permission paths until the second reviyah.','anonymous quoted authority',conditions=['Until second reviyah'],role='אמר מר quotation')
link('pathrule','paths','support','6b:4')
c('biur','6b:5','רב נחמן בר יצחק אמר לבער פירות שביעית','Second reviyah matters for removal of seventh-year produce.','רב נחמן בר יצחק',question='second')
qn('straw','6b:5','עד מתי נהנין ושורפין בתבן ובקש של שביעית','Until when may one benefit from and burn seventh-year straw/stubble?','anonymous quoted Mishnah')
c('strawend','6b:5','עד שתרד רביעה שניה','Benefit and burning of seventh-year straw/stubble last until second reviyah.','anonymous quoted Mishnah',conditions=['Seventh-year straw/stubble','Until second reviyah'],question='straw',role='Mishnah quotation')
link('strawend','biur','support','6b:5')
qn('biurwhy','6b:6','מאי טעמא','What is the basis for the removal rule?')
c('field','6b:6','כל זמן שחיה אוכלת בשדה האכל לבהמתך בבית','While wild animals eat in the field one may feed domestic animals at home.',conditions=['The species remains available to wild animals in field'],mode='conditional',question='biurwhy')
c('gone','6b:6','כלה לחיה מן השדה כלה לבהמתך מן הבית','When it is exhausted for wild animals in the field remove it from domestic animals at home.',conditions=['The species is exhausted in the field'],mode='conditional',question='biurwhy')
link('gone','strawend','support','6b:6',explicit=False)
qn('rev','6b:7','מאי לשון רביעה','What does the name reviyah express?','רבי אבהו')
c('cover','6b:7','דבר שרובע את הקרקע','Reviyah denotes that which mates with the soil.','רבי אבהו',question='rev')
c('husband','6b:7','דאמר רב יהודה מיטרא בעלה דארעא הוא','Rain is the husband of the earth.','רב יהודה')
link('husband','cover','analogy','6b:7','כדרב יהודה דאמר רב יהודה מיטרא בעלה דארעא הוא')
c('first','6b:8','רביעה ראשונה כדי שתרד בקרקע טפח','First reviyah requires penetration of one handbreadth into the ground.','רבי אבהו')
c('secondmeasure','6b:8','שניה כדי לגוף בה פי חבית','Second reviyah is enough to seal a barrel mouth with the resulting soil.','רבי אבהו')
c('seal','6b:8','אמר רב חסדא גשמים שירדו כדי לגוף בהן פי חבית אין בהן משום ועצר','Rain sufficient for sealing a barrel mouth does not count as the withholding sign ועצר.','רב חסדא',conditions=['Rain sufficient for barrel-mouth sealing'])
c('before','6b:9',None,'Rain before the recitation point ועצר does not fall under ועצר.','רב חסדא',conditions=['Rain before ועצר'],status='Qualified by Abaye in 6b:10',unc=['Prayer-time reference is explanatory expansion; surface says קודם ועצר.'])
c('evening','6b:10','אמר אביי לא אמרן אלא קודם ועצר דאורתא','The exemption is restricted to before the evening ועצר.','אביי',conditions=['Before evening ועצר'],mode='conditional')
link('evening','before','qualification','6b:10')
c('morning','6b:10','אבל קודם ועצר דצפרא יש בהן משום ועצר','Before morning ועצר it can count as withholding.','אביי',conditions=['Before morning ועצר'],mode='conditional',status='Objection and cloud-type distinction follow in context 6b:11')
c('cloud','6b:10','דאמר רב יהודה בר יצחק הני ענני דצפרא לית בהו מששא','Morning clouds have no substance.','רב יהודה בר יצחק',conditions=['Morning clouds'],status='Used as basis for Abaye; qualified by ensuing cloud distinction')
link('cloud','morning','support','6b:10')
qn('proverb','6b:11','והא אמרי אינשי במפתח בבי מיטרא בר חמרא מוך שקך וגני','Does not the proverb promise reliable morning rain when opening the doors?','רב פפא')
edge(questions['proverb'],names['morning'],'objection','6b:11')
c('cloudtypes','6b:11','לא קשיא הא דקטיר בעיבא הא דקטיר בענני','No contradiction: the cases differ between clouding with עיבא and with ענני.',conditions=['Different cloud formations'],mode='reconciled',question='proverb',unc=['Anonymous reply after Rav Pappa addresses Abaye; no named reply forced. Exact physical mapping of cloud terms not fixed without commentary.'])
link('cloudtypes','cloud','distinction','6b:11')
qn('rain-dew','7a:4','רבא רמי כתיב יערף כמטר לקחי וכתיב תזל כטל אמרתי','How reconcile teaching as forceful rain with speech as dew?','רבא')
c('worthydew','7a:4','אם תלמיד חכם הגון הוא כטל','For a worthy scholar, respond as dew.','רבא',conditions=['Scholar is worthy'],mode='conditional',question='rain-dew')
c('unworthyrain','7a:4','ואם לאו עורפהו כמטר','For an unworthy scholar, עורפהו כמטר.','רבא',conditions=['Scholar is not worthy'],mode='conditional',question='rain-dew',unc=['Metaphorical severity preserved; not converted into an executable physical sanction.'])
c('life','7a:5','כל העוסק בתורה לשמה תורתו נעשית לו סם חיים','Torah studied for its own sake becomes an elixir of life.','ר\' בנאה',conditions=['Torah studied לשמה'],mode='conditional',role='baraita teaching')
c('death','7a:5','וכל העוסק בתורה שלא לשמה נעשית לו סם המות','Torah studied not for its own sake becomes an elixir of death.','ר\' בנאה',conditions=['Torah studied שלא לשמה'],mode='conditional',role='baraita teaching')
c('arifah','7a:5','ואין עריפה אלא הריגה','Arifah is interpreted as killing.','ר\' בנאה',role='lexical scriptural argument')
link('arifah','death','support','7a:5')
u('7a:6','א"ל ר\' ירמיה לר\' זירא ליתי מר ליתני','ר\' ירמיה','request to teach');attr('7a:6','א"ל ר\' ירמיה לר\' זירא','ר\' ירמיה','Request addressed to R. Zeira','speaker')
c('weak','7a:6','א"ל חלש לבאי ולא יכילנא','R. Zeira reports weakness and inability to teach.','ר\' זירא',role='narrative reply',pos=False)
u('7a:6','לימא מר מילתא דאגדתא','ר\' ירמיה','request for aggadah');attr('7a:6','לימא מר מילתא דאגדתא','ר\' ירמיה','Dialogue turn inferred from adjacent exchange','speaker')
attr('7a:6','א"ל הכי אמר ר\' יוחנן','ר\' זירא','Transmits R. Yohanan teaching continued in 7a:7','transmitter',['ר\' זירא','ר\' יוחנן'])
attr('7a:6','ר\' יוחנן','ר\' יוחנן','Original authority for man/tree teaching','quoted_authority')
qn('tree','7a:6','וכי אדם עץ שדה הוא','Is a person a tree of the field?','ר\' יוחנן via ר\' זירא')
qn('treeverses','7a:7','הא כיצד','How do the preserve/eat and destroy/cut verses fit?','ר\' יוחנן via ר\' זירא')
c('eat','7a:7','אם ת"ח הגון הוא ממנו תאכל ואותו לא תכרת','Learn from and preserve a worthy scholar.','ר\' יוחנן',conditions=['Scholar is worthy'],mode='conditional',question='treeverses',status='Teaching transmitted by R. Zeira; not attributed to transmitter as originator')
c('cut','7a:7','ואם לאו אותו תשחית וכרת','Apply destroy/cut imagery to an unworthy scholar.','ר\' יוחנן',conditions=['Scholar is unworthy'],mode='conditional',question='treeverses',unc=['Destruction imagery retained within aggadic exposition.'])
edge(names['eat'],questions['tree'],'answer','7a:7')
qn('iron','7a:8','מאי דכתיב (משלי כז, יז) ברזל בברזל יחד','What does iron sharpens iron teach?','רבי חמא (אמר רבי) חנינא')
c('ironsharp','7a:8','מה ברזל זה אחד מחדד את חבירו','Iron sharpens other iron.','רבי חמא (אמר רבי) חנינא',unc=['Source has parenthetical (אמר רבי); unresolved whether transmission or damaged naming; do not normalize to an unambiguous person.'],role='analogy premise')
c('twoscholars','7a:8','אף שני תלמידי חכמים מחדדין זה את זה בהלכה','Two scholars sharpen each other in halakhah.','רבי חמא (אמר רבי) חנינא',question='iron',unc=['Exact surface attribution retained; parenthetical transmission uncertainty.'])
link('ironsharp','twoscholars','analogy','7a:8')
qn('fire','7a:9','למה נמשלו דברי תורה כאש','Why is Torah likened to fire?','רבה בר בר חנה')
c('firealone','7a:9','מה אש אינו דולק יחידי','Fire does not burn alone.','רבה בר בר חנה',role='analogy premise')
c('torahalone','7a:9','אף דברי תורה אין מתקיימין ביחידי','Torah does not endure with a solitary learner.','רבה בר בר חנה',question='fire')
link('firealone','torahalone','analogy','7a:9')
qn('sword','7a:10','מאי דכתיב (ירמיהו נ, לו) חרב אל הבדים ונואלו','How is sword against the solitary and foolishness interpreted?','רבי יוסי בר חנינא')
c('swords','7a:10','חרב על שונאיהן של תלמידי חכמים שעוסקין בד בבד בתורה','Sword is invoked against solitary Torah scholars using the euphemism שונאיהן.','רבי יוסי בר חנינא',conditions=['Study Torah alone'],question='sword')
c('fool','7a:10','ולא עוד אלא שמטפשין','Solitary study also brings foolishness.','רבי יוסי בר חנינא',conditions=['Study Torah alone'])
link('swords','torahalone','support','7a:10','והיינו דאמר רבי יוסי בר חנינא')
c('sin','7a:11','ולא עוד אלא שחוטאין','Solitary learners also sin.','רבי יוסי בר חנינא',conditions=['Study Torah alone'],unc=['Continuation inherits the preceding teaching; anonymous alternative proof is separately recorded.'])
c('sinproof1','7a:11','כתיב הכא ונואלו וכתיב התם (במדבר יב, יא) אשר נואלנו ואשר חטאנו','The repeated root נואל links foolishness to sin via Numbers 12:11.',role='scriptural derivation')
c('sinproof2','7a:11','ואיבעית אימא מהכא (ישעיהו יט, יג) נואלו שרי צוען [וגו\'] והתעו את מצרים','Alternatively Isaiah 19:13 links foolishness with misleading Egypt.',role='alternative scriptural derivation')
link('sinproof1','sin','support','7a:11');link('sinproof2','sin','support','7a:11')
qn('wood','7a:12','למה נמשלו דברי תורה כעץ','Why is Torah compared to wood/tree?','רב נחמן בר יצחק')
c('smallwood','7a:12','מה עץ קטן מדליק את הגדול','Small wood kindles large wood.','רב נחמן בר יצחק',role='analogy premise')
c('smallwise','7a:12','אף תלמידי חכמים קטנים מחדדים את הגדולים','Junior scholars sharpen senior scholars.','רב נחמן בר יצחק',question='wood')
link('smallwood','smallwise','analogy','7a:12')
c('teachers','7a:12','הרבה למדתי מרבותי','R. Hanina learned much from his teachers.','ר\' חנינא',role='personal testimony')
c('peers','7a:12','ומחבירי יותר מרבותי','He learned more from his peers than his teachers.','ר\' חנינא',role='personal testimony')
c('pupils','7a:12','ומתלמידי יותר מכולן','He learned most from his students.','ר\' חנינא',role='personal testimony')
link('pupils','smallwise','support','7a:12','והיינו דאמר ר\' חנינא הרבה למדתי מרבותי ומחבירי יותר מרבותי ומתלמידי יותר מכולן')
qn('thirst','7a:13','רבי חנינא בר פפא רמי כתיב (ישעיהו כא, יד) לקראת צמא התיו מים וכתיב (ישעיהו נה, א) הוי כל צמא לכו למים','Why bring water to the thirsty in one verse but have them approach in another?','רבי חנינא בר פפא')
c('bring','7a:13','אם תלמיד הגון הוא לקראת צמא התיו מים','For a worthy student bring teaching toward the thirsty.','רבי חנינא בר פפא',conditions=['Student worthy'],mode='conditional',question='thirst')
c('come','7a:13','ואי לא הוי כל צמא לכו למים','Otherwise the student must come to the water.','רבי חנינא בר פפא',conditions=['Student not worthy'],mode='conditional',question='thirst')
qn('springs','7a:14','רבי חנינא בר חמא רמי כתיב (משלי ה, טז) יפוצו מעינותיך חוצה וכתיב (משלי ה, יז) יהיו לך לבדך','How reconcile spreading springs outward with keeping them for oneself?','רבי חנינא בר חמא')
c('spread','7a:14','אם תלמיד הגון הוא יפוצו מעינותיך חוצה','Teach outward when the student is worthy.','רבי חנינא בר חמא',conditions=['Student worthy'],mode='conditional',question='springs')
c('retain','7a:14','ואם לאו יהיו לך לבדך','Keep teaching to yourself when the student is unworthy.','רבי חנינא בר חמא',conditions=['Student unworthy'],mode='conditional',question='springs')
qn('water','7a:15','למה נמשלו דברי תורה למים','Why is Torah compared to water?','רבי חנינא בר אידי')
c('waterlow','7a:15','מה מים מניחין מקום גבוה והולכין למקום נמוך','Water leaves high places for low places.','רבי חנינא בר אידי',role='analogy premise')
c('humblewater','7a:15','אף דברי תורה אין מתקיימין אלא במי שדעתו שפלה','Torah endures only in one of humble disposition.','רבי חנינא בר אידי',conditions=['Humble disposition'],question='water')
link('waterlow','humblewater','analogy','7a:15')
qn('liquids','7a:16','למה נמשלו דברי תורה לשלשה משקין הללו במים וביין ובחלב','Why compare Torah to water, wine and milk?','רבי אושעיא')
c('vessels','7a:16','מה שלשה משקין הללו אין מתקיימין אלא בפחות שבכלים','The three liquids keep only in lowly vessels.','רבי אושעיא',role='analogy premise')
c('humbleliquid','7a:16','אף דברי תורה אין מתקיימין אלא במי שדעתו שפלה','Torah endures only in a humble person.','רבי אושעיא',conditions=['Humble disposition'],question='liquids')
link('vessels','humbleliquid','analogy','7a:16')
c('insult','7a:17','אי חכמה מפוארה בכלי מכוער','Caesar’s daughter juxtaposes beautiful wisdom with an ugly vessel.','ברתיה דקיסר',role='narrative taunt',pos=False)
qn('clay','7a:17','אמר לה אביך רמי חמרא במני דפחרא','Your father stores wine in earthenware?','ר\' יהושע בן חנניה')
qn('whatvessel','7a:17','אמרה ליה אלא במאי נירמי','In what else should we store it?','ברתיה דקיסר')
c('gold','7a:17','אמר לה אתון דחשביתו רמו במאני דהבא וכספא','He suggests that distinguished people store wine in gold/silver.','ר\' יהושע בן חנניה',question='whatvessel',role='ironic narrative instruction',pos=False,status='Ironic demonstration, not general storage advice')
c('told','7a:18','אזלה ואמרה ליה לאבוה','The daughter relays the advice to her father.','anonymous narrator',role='narrative event',pos=False)
c('spoiled','7a:18','רמייא לחמרא במני דהבא וכספא ותקיף','The wine is put in precious vessels and sours.','anonymous narrator',role='narrative event',pos=False)
c('reported','7a:18','אתו ואמרו ליה','Unidentified people report the outcome to Caesar.','anonymous narrator',role='narrative event',pos=False)
qn('who','7a:18','אמר לה לברתיה מאן אמר לך הכי','Who told you to do this?','קיסר')
c('identified','7a:18','אמרה ליה רבי יהושע בן חנניה','The daughter identifies R. Yehoshua ben Hananiah.','ברתיה דקיסר',question='who',role='narrative reply',pos=False)
c('summon','7a:18','קריוהו','He is summoned.','anonymous narrator',role='narrative event',pos=False)
qn('whyadvice','7a:18','אמר ליה אמאי אמרת לה הכי','Why did you tell her this?','קיסר')
c('retort','7a:18','אמר ליה כי היכי דאמרה לי אמרי לה','He replies that he spoke to her as she had spoken to him.','ר\' יהושע בן חנניה',question='whyadvice',role='narrative reply',pos=False)
link('spoiled','vessels','support','7a:18',explicit=False)
qn('handsome','7a:18','והא איכא שפירי דגמירי','But there are handsome people who learn!','anonymous objection (possibly dialogue continuation)')
edge(questions['handsome'],names['humbleliquid'],'objection','7a:18',explicit=False)
c('uglier','7b:1','אי הוו סנו טפי הוו גמירי','If they were ugly they would learn more.','anonymous reply (possibly R. Yehoshua dialogue continuation)',conditions=['Counterfactual lack of beauty'],mode='hypothetical',question='handsome',unc=['No explicit speaker attached to this reply; do not force narrative versus editorial voice.'])
c('neglectliquid','7b:1','דבר אחר מה שלשה משקין הללו אין נפסלין אלא בהיסח הדעת','Alternative analogy: these three liquids spoil only through inattention.','anonymous alternative exposition',role='analogy premise')
c('forget','7b:1','אף דברי תורה אין משתכחין אלא בהיסח הדעת','Torah is forgotten only through inattention.','anonymous alternative exposition',conditions=['Inattention'],question='liquids',unc=['דבר אחר introduces alternative explanation; attribution to R. Oshaya is not restated, so left anonymous.'])
link('neglectliquid','forget','analogy','7b:1')
c('creation','7b:2','גדול יום הגשמים כיום שנבראו שמים וארץ','The day of rain is as great as creation of heaven and earth.','רבי חמא בר\' חנינא')
c('singular','7b:2','בראתים לא נאמר אלא בראתיו','The verse says singular בראתיו rather than plural בראתים.','רבי חמא בר\' חנינא',role='scriptural wording inference')
link('singular','creation','support','7b:2')
c('salvation','7b:3','גדול יום הגשמים שאפי\' ישועה פרה ורבה בו','Rain day is great because even salvation grows on it.','רב אושעיא')
c('forgiven','7b:3','אין הגשמים יורדים אלא א"כ נמחלו עונותיהן של ישראל','Rain descends only when Israel’s sins have been forgiven.','רבי תנחום בר חנילאי',conditions=['Israel’s sins forgiven'])
c('altforgive','7b:4',None,'Zeiri of Dihavat tells Ravina their tradition derives the forgiveness teaching from Kings I 8:34 instead of the prior Psalm proof.','זעירי מדיהבת',role='alternative proof tradition',unc=['Alternative source, not a rejection of the proposition; exact geographical vocalization left unresolved.'])
attr('7b:4','א"ל זעירי מדיהבת לרבינא','זעירי מדיהבת','Addresses Ravina; Ravina is recipient, not originator','speaker')
link('altforgive','forgiven','support','7b:4')
c('annihilate','7b:5','אין הגשמים נעצרין אא"כ נתחייבו שונאיהן של ישראל כליה','Rain is withheld only when Israel, phrased euphemistically as its enemies, has incurred annihilation.','ר\' תנחום בריה דרבי חייא איש כפר עכו',conditions=['Liability to annihilation'],unc=['This R. Tanhum is distinct from R. Tanhum bar Hanilai in 7b:3.'])
c('altannihilate','7b:5','א"ל זעירי מדיהבת לרבינא אתון מהכא מתניתו לה אנן מהכא מתנינן לה (דברים יא, יז) ועצר את השמים ואבדתם מהרה','Zeiri tells Ravina their tradition uses Deuteronomy 11:17 for withholding and destruction.','זעירי מדיהבת',role='alternative proof tradition')
link('altannihilate','annihilate','support','7b:5')
# Explicit quoted evidence and argument links, independently identified in the source pass.
proofs=[
('6b:6','דכתיב (ויקרא כה, ז) ולבהמתך ולחיה אשר בארצך',['field','gone']),
('6b:7','שנאמר (ישעיהו נה, י) כי כאשר ירד הגשם והשלג מן השמים ושמה לא ישוב כי אם הרוה את הארץ והולידה והצמיחה',['husband']),
('6b:10','דכתיב (הושע ו, ד) מה אעשה לך אפרים מה אעשה לך יהודה וחסדכם כענן בקר וגו\'',['cloud']),
('7a:5','שנאמר (משלי ג, יח) עץ חיים היא למחזיקים בה',['life']),
('7a:5','ואומר (משלי ג, ח) רפאות תהי לשרך',['life']),
('7a:5','ואומר (משלי ח, לה) כי מוצאי מצא חיים',['life']),
('7a:5','שנאמר יערף כמטר לקחי',['death']),
('7a:5','שנאמר (דברים כא, ד) וערפו שם את העגלה בנחל',['arifah']),
('7a:7','משום דכתיב (דברים כ, יט) כי ממנו תאכל ואותו לא תכרת וכתיב אותו תשחית וכרת',['eat','cut']),
('7a:9','שנאמר (ירמיהו כג, כט) הלא כה דברי כאש נאם ה\'',['torahalone']),
('7a:10','שנאמר ונואלו',['fool']),
('7a:12','שנאמר (משלי ג, יח) עץ חיים היא למחזיקים בה',['smallwise']),
('7a:15','דכתיב הוי כל צמא לכו למים',['humblewater']),
('7a:16','דכתיב הוי כל צמא לכו למים וכתיב (ישעיהו נה, א) לכו שברו ואכלו ולכו שברו בלא כסף ובלא מחיר יין וחלב',['humbleliquid']),
('7b:2','שנאמר (ישעיהו מה, ח) הרעיפו שמים ממעל ושחקים יזלו צדק תפתח ארץ ויפרו ישע וצדקה תצמיח יחד אני ה\' בראתיו',['singular','creation']),
('7b:3','שנאמר תפתח ארץ ויפרו ישע',['salvation']),
('7b:3','שנאמר (תהלים פה, ב) רצית ה\' ארצך שבת שבות יעקב נשאת עון עמך כסית כל חטאתם סלה',['forgiven']),
('7b:5','שנאמר (איוב כד, יט) ציה גם חום יגזלו מימי שלג שאול חטאו',['annihilate'])]
for r,quote,targets in proofs:
 z=u(r,quote,'quoted Scripture','scriptural proof quotation')
 attr(r,quote,'Scripture','Quoted textual authority, distinct from the amora citing it','quoted_authority')
 for target in targets: edge(z,names[target],'support',r,quote)
# Segments read for boundary control, distinct from fully annotated necessary context.
read_context=['Taanit 6a:'+str(i) for i in range(1,14)]+['Taanit 6b:'+str(i) for i in range(11,18)]+['Taanit 7a:'+str(i) for i in range(1,4)]+['Taanit 7b:'+str(i) for i in range(6,17)]
annotated_context=['Taanit 6a:13','Taanit 6b:11']
audit={
'6b:1':'Checked inherited R. Zeira framing, anonymous Mishnah voice, two unpunctuated vow formulations, endpoint and supporting link; not a Rav/Shmuel dispute.',
'6b:2':'All three quoted agricultural endpoints inventoried, with Rav Zevid application separate from Mishnah authority; alternatives answer inherited question without forced exclusion.',
'6b:3':'Both namushot definitions and both named holders retained; no local decision.',
'6b:4':'Rav Pappa application separate from anonymous אמר מר path rule; until second reviyah retained.',
'6b:5':'Rav Nahman bar Yitzhak application and quoted benefit/burning endpoint retained; no practical ruling beyond local text.',
'6b:6':'Both availability and exhaustion conditions plus Leviticus proof retained; anonymous explanation, no named originator imposed.',
'6b:7':'R. Abbahu etymology, Rav Yehuda metaphor and Isaiah proof distinguished; Rav Yehuda is not Rav.',
'6b:8':'Both reviyah quantities and Rav Hisda withholding consequence retained separately.',
'6b:9':'Initial general claim linked to Abaye qualification rather than silently rewriting its local stage.',
'6b:10':'Evening/morning contrast, Rav Yehuda bar Yitzhak supporting claim and Hosea proof retained; 6b:11 cloud distinction prevents absolute morning rejection.',
'7a:4':'Verse tension and both conditional responses retained; scholarly worthiness, not chronological name ordering.',
'7a:5':'Both study-motive conditions, all three life proofs, death proof and arifah derivation inventoried; baraita named authority preserved.',
'7a:6':'Dialogue requests and weakness reply retained as narrative; R. Zeira transmitter distinct from R. Yohanan authority; teaching continues next segment.',
'7a:7':'Continuation of R. Yohanan exposition; both tree verses and worthy/unworthy conditions retained.',
'7a:8':'Iron analogy premise and halakhic sharpening claim retained; parenthetical attribution unresolved rather than normalized.',
'7a:9':'Fire premise and non-solitary learning conclusion with Jeremiah proof retained.',
'7a:10':'Sword and foolishness distinct; source linkage to preceding teaching, euphemism and named authority retained.',
'7a:11':'Sin continuation and two alternative derivations retained; alternative proof left anonymous, not a retraction.',
'7a:12':'Small wood analogy and junior scholars, plus three comparative learning testimony clauses retained; R. Hanina distinct from Rav Nahman bar Yitzhak.',
'7a:13':'Two verses and two worthiness cases retained; no forced opposition with neighboring teachings.',
'7a:14':'Outward/retained teaching distinction scoped by student worthiness; R. Hanina bar Hama not other Haninas.',
'7a:15':'Water movement premise, humility conclusion and verse retained; parenthetical ואמר preserved in source evidence.',
'7a:16':'Three liquids, scriptural comparison, low vessels and humility conclusion retained; opens following narrative illustration.',
'7a:17':'Daughter taunt, vessel questions and ironic advice kept as dialogue; not general halakhic instruction.',
'7a:18':'Advice transmission, souring, report, identification, summons, explanation and handsome-learner objection all retained separately; boundary remains open to 7b:1.',
'7b:1':'Counterfactual reply separated from דבר אחר; latter answers three-liquids question; neither speaker nor attribution to R. Oshaya forced.',
'7b:2':'Rain/creation comparison, quoted verse, singular/plural inference retained; no imported disagreement with contextual rain comparisons.',
'7b:3':'Two separate named teachings; salvation and forgiveness claims and proofs retained independently.',
'7b:4':'Zeiri addresses Ravina, who is not position holder; alternate proof is not rejection of forgiveness teaching.',
'7b:5':'Distinct Tanhum identity, euphemism, necessary condition, Job proof and Zeiri alternate Deuteronomy proof retained. 7b:6 onward begins other causes; no local explicit repeal or decision.'}
for rr in cores+annotated_context:
 short=rr.split(' ',1)[1]
 boundary='open_both' if short in ['6b:1','6b:10','7a:6','7a:7','7a:10','7a:11','7a:16','7a:17','7a:18','7b:1','7b:3','7b:4','7b:5','6a:13','6b:11'] else 'closed'
 rec('structure',rr,None,dict(title=audit.get(short,'Necessary original context: inherited question or continuation'),primary=True,boundary=boundary,legacy_ids=[]),origin='editorial_inference')
coverage=[]
layers=['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']
for rr in cores+annotated_context:
 for layer in layers:
  ids=[r['id'] for r in R if r['layer']==layer and any(e['segment_id']==rr for e in r['evidence'])]
  rationale=audit.get(rr.split(' ',1)[1],'Read original context for question scope and qualification; excluded from sampled core denominator.')
  if not ids and layer!='reconciliation':rationale+=' No separate '+layer+' record warranted after source pass; inherited links or narrative function remain in other layers.'
  coverage.append(dict(segment_id=rr,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
artifact=dict(artifact_kind='immutable_independent_source_only_reading',job_id=j['job_id'],schema_contract='2.0.0-production record and coverage schemas; review wrapper is not a production submission',execution=dict(route='interactive_agent',agent_id='/root/ta_source_review055',model_id=None,fork_turns='none',blindness='Fresh source-only; no producer, prior reading or comparison inspected'),bindings=dict(job_path=str(J),job_sha256=sha(J),documents=bindings,plan_sha256=j['plan_sha256']),core_refs=cores,selected_blocks=j['selected_blocks'],core_spans=selected,context_read_refs=read_context,context_annotated_refs=annotated_context,records=R,coverage=coverage,final_semantic_omission_audit=dict(stage='before_initial_freeze',source_based=True,per_core=audit,checks=['Every core re-read for omitted propositions, dialogue turns, conditions, proof variants and scope','All named and anonymous authority distinctions reviewed','No explicit retraction, inversion, or adjudicated choice in assigned cores; preserve local qualifications','No producer comparison performed']),uncertainties=['6b:1 unpunctuated vow formulations','6b:3 אתיגרא precise gloss','6b:9 prayer-time expansion explanatory','6b:11 physical cloud mapping and anonymous reply','7a:8 parenthetical attribution/transmission','7a:11 inherited statement versus anonymous alternative proof','7a:18–7b:1 dialogue/editorial speaker boundary','7b:1 דבר אחר authority not restated','Aggadic severe imagery is not converted into practical sanctions'],release_status=dict(next_release_only=True,current015_unchanged=True,admitted=False,ml_eligible=False,task_eligible=False,human_scholarly_certification=False),edition_attribution={k:src[k] for k in ['title','versionTitle','versionSource','license']})
def validate(a):
 import jsonschema
 ids={r['id'] for r in a['records']}; assert len(ids)==len(a['records'])
 rs=schema['properties']['records']['items']; cs=schema['properties']['coverage']['items']
 for r in a['records']:
  jsonschema.validate(r,rs)
  for e in r['evidence']:assert raw(e['segment_id'])[e['start_char']:e['end_char']]==e['quote'] and e['end_char']>e['start_char']
  assert set(r['links'])<=ids
  if r['layer']=='edges':assert r['content']['source_id'] in ids and r['content']['target_id'] in ids
  if r['layer']=='positions':assert r['content']['claim_id'] in ids and (r['content']['question_id'] is None or r['content']['question_id'] in ids)
 for v in a['coverage']:jsonschema.validate(v,cs);assert set(v['record_ids'])<=ids
 assert len([v for v in a['coverage'] if v['segment_id'] in cores])==240
 for rr in cores+annotated_context:
  assert {v['layer'] for v in a['coverage'] if v['segment_id']==rr}==set(layers)
  spans=sorted((e['start_char'],e['end_char']) for r in a['records'] if r['layer']=='structure' and r['content']['primary'] for e in r['evidence'] if e['segment_id']==rr)
  end=0
  for start,stop in spans:assert start==end;end=stop
  assert end==len(raw(rr))
 return dict(result='PASS',core_count=30,core_layer_rows=240,context_annotated_count=len(annotated_context),context_read_count=len(read_context),record_counts=dict(collections.Counter(r['layer'] for r in a['records'])),evidence_count=sum(len(r['evidence']) for r in a['records']),checks=['all pinned byte hashes','canonical plan hash','selected-block membership and source-span bindings','common per-layer record schema','common coverage schema','exact original Unicode code-point slices','ID uniqueness and all links resolve','30 original cores x 8 layer status','nonoverlapping complete primary structure','context/core separation'],limitations='Mechanical PASS does not certify semantic truth; no production comparison/admission or eligibility.')
v=validate(artifact)
out=D/'taanit_delegated055.json'
data=(json.dumps(artifact,ensure_ascii=False,indent=2)+'\n').encode('utf8')
if '--verify' in sys.argv:
 assert out.read_bytes()==data,'Frozen bytes differ from deterministic reconstruction'
 print(json.dumps(v,ensure_ascii=False));sys.exit()
# Freeze only after all source-based audits and validation; exclusive creation prevents overwrite.
with out.open('xb') as f:f.write(data)
digest=sha(out)
with (D/'taanit_delegated055.json.sha256').open('x',encoding='utf8') as f:f.write(digest+'  taanit_delegated055.json\n')
v.update(artifact_path=str(out),artifact_sha256=digest,helper_path=str(pathlib.Path(__file__).resolve()),helper_sha256=sha(__file__),receipt_id='ta055.initialfreeze.validation.20261127',validation_route='python jsonschema plus independent invariants; deterministic --verify reconstruction')
receipt=D/'validation_ta055_initialfreeze_20261127.json'
with receipt.open('x',encoding='utf8') as f:json.dump(v,f,ensure_ascii=False,indent=2);f.write('\n')
for p in [pathlib.Path(__file__),receipt]:
 with pathlib.Path(str(p)+'.sha256').open('x',encoding='utf8') as f:f.write(sha(p)+'  '+p.name+'\n')
print(json.dumps(v,ensure_ascii=False,indent=2));print('receipt_sha256',sha(receipt))
