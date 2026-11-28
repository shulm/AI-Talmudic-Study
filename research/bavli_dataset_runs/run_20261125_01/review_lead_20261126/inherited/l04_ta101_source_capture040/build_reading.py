import json, hashlib, pathlib, sys, collections
import jsonschema
OUT=pathlib.Path(__file__).resolve().parent
JOB=pathlib.Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/jobs/bavli_taanit_delegated101.json')
JHASH='4429756dfd1d57fbbf1d56e9d6454ee8ac25e33cfde11819f42156bae4d922e4'
AGENT='/root/ta_source_review101'
def sha(b): return hashlib.sha256(b).hexdigest()
def read(p): return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
job=read(JOB)
inputs=[{'path':str(JOB),'sha256':JHASH},job['source'],*job['common_documents'],job['frozen_plan'],job['original_source_schema']]
for inp in inputs: assert sha(pathlib.Path(inp['path']).read_bytes())==inp['sha256'],inp
source=read(job['source']['path']); schema=read(job['common_documents'][1]['path']); plan=read(job['frozen_plan']['path'])
canon=dict(plan);canon.pop('plan_sha256')
assert sha(b'bavli-source-only-review-plan-v1\0'+json.dumps(canon,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode())==job['plan_sha256']==plan['plan_sha256']
texts={f'Taanit {(p+2)//2}{"a" if p%2==0 else "b"}:{s+1}':t for p,page in enumerate(source['text']) for s,t in enumerate(page)}
cores=job['core_refs']; ctx=['Taanit 9b:1','Taanit 9b:3','Taanit 9b:4','Taanit 9b:5']
reviewed=cores+ctx
for jb in job['selected_blocks']:
 pb=next(b for b in plan['review_blocks'] if b['block_id']==jb['block_id'])
 assert [s['ref'] for s in pb['spans']]==jb['core_refs'] and 'probability_sample' in pb['roles']
 for s in pb['spans']:
  t=source['text'][s['page_index']][s['segment_index']]
  assert texts[s['ref']]==t and s['offsets_codepoints']==[0,len(t)] and sha(t.encode())==s['span_sha256_utf8']
assert len(cores)==len(set(cores))==30
R=[]; counts=collections.Counter(); keys={}; notes={}
def ev(ref,start=None,end=None):
 ref=ref if ref.startswith('Taanit ') else 'Taanit '+ref;t=texts[ref]
 a=0 if start is None else t.index(start);b=len(t) if end is None else t.index(end,a+1)
 return {'segment_id':ref,'start_char':a,'end_char':b,'quote':t[a:b]}
def add(layer,e,content,links=(),unc=(),origin='source_paraphrase',key=None):
 counts[layer]+=1;i=f'ta101.{layer}.{counts[layer]:04}'
 R.append(dict(id=i,layer=layer,evidence=e if isinstance(e,list) else [e],content=content,origin=origin,uncertainty=list(unc),links=list(links)))
 if key: keys[key]=i
 return i
def edge(a,b,relation,e,explicit=True):
 return add('edges',e,dict(source_id=a,target_id=b,relation=relation,explicitness='source_explicit' if explicit else 'editorial_reconstruction'),[a,b],origin='source_paraphrase' if explicit else 'editorial_inference')
def unit(ref,start,end,voice,role,claims=(),conditions=(),mode='asserted',key=None,chain=(),unc=(),position=True):
 e=ev(ref,start,end); holders=voice if isinstance(voice,list) else ([voice] if voice else [])
 u=add('utterances',e,dict(textual_voice=' / '.join(holders) if holders else 'anonymous',discourse_role=role,composition='composite' if len(claims)>1 else 'atomic'),unc=unc,key=key)
 add('attributions',e,dict(surface=' / '.join(holders) if holders else '',role='anonymous' if not holders else ('collective' if voice in ['תנא דבי רבי ישמעאל',"תנא דבי ר\' ישמעאל",'ת"ר'] else 'speaker'),candidates=holders,scope=u,transmission_chain=list(chain)),[u],unc)
 if chain:
  for transmitter in chain[:-1]:add('attributions',e,dict(surface=transmitter,role='transmitter',candidates=[transmitter],scope=u,transmission_chain=list(chain)),[u],unc)
 ids=[]
 for n,claim in enumerate(claims):
  c=add('claims',e,dict(proposition=claim,conditions=list(conditions),scope=role,assertion_mode=mode),[u],unc,key=f'{key}.c{n}' if key else None);ids.append(c)
  if position:
   add('positions',e,dict(holder_candidates=holders,claim_id=c,question_id=None,conditions=list(conditions),local_status=mode+'; local passage only'),[c],unc)
 return u,ids
def q(ref,start,end,text,key,conditions=(),unc=()):
 e=ev(ref,start,end);u,_=unit(ref,start,end,None,'explicit question',unc=unc)
 return add('questions',e,dict(formulation=text,question_origin='explicit',conditions=list(conditions),answer_set_status='partial'),[u],unc,key=key)
def proof(ref,start,end,target,voice=None):
 e=ev(ref,start,end);u,_=unit(ref,start,end,voice,'cited scripture / textual derivation',position=False)
 edge(u,keys[target] if target in keys else target,'support',e)
 return u
titles={
'7b:6':'Withholding rain for neglected tithes and seasonal exegesis','7b:7':'Withholding rain for slander','7b:8':'Impudence, withholding rain and past versus future sin','7b:9':'Calling the brazen wicked and hating them','7b:10':'Torah neglect and exegetical poverty','7b:11':'Alternative proof for Torah neglect and clouds cleared away','7b:12':'Robbery as cause of withheld rain','7b:13':'Prayer as remedy','7b:14':'Ironlike sky and corrupted deeds','7b:15':'Prayer and prior rectification','8b:12':'Sabbath sunshine and blessing of money in rain','8b:13':'Blessing in hidden things','8b:14':'Prayer before, during and after measuring grain','8b:15':'Mnemonic and comparison to ingathering','8b:16':'Armies and unfulfilled charity pledges','8b:17':'Opening attribution and question continued on next page','9a:1':'Tithe to become wealthy','9a:2':'First encounter with Resh Lakish’s child','9a:3':'Testing God: objection and tithe exception','9a:4':'Until lips wear out and child’s reply','9a:5':'Second encounter: the child quotes Proverbs','9a:6':'Torah antecedent of the Proverbs statement','9a:7':'Gaze, removal and mother’s warning','9a:8':'Rain for an individual; sustenance for many','9a:9':'Objection: three leaders and gifts; Miriam’s well','9a:10':'Aaron’s death and the clouds','9a:11':'Fear reading and four functions of כי','9a:12':'Moses’s merit and simultaneous loss of gifts','9a:13':'Objection articulated; Moses counts as many','9a:14':'Three pupils’ gestures hurt Rav Pappa','9b:1':'Dream and farewell complete the pupils narrative','9b:3':'Resh Lakish likewise: rain for an individual','9b:4':'Rain narrowed to field and grass','9b:5':'Rav Daniel’s selectively watered garden'}
for ref in reviewed:
 short=ref.split(' ')[1];boundary='open_both' if short in ['7b:11','9a:9','9a:10','9a:11','9a:12'] else 'open_right' if short in ['7b:12','7b:14','8b:17','9a:2','9a:3','9a:5','9a:6','9a:8','9a:14','9b:3','9b:4'] else 'open_left' if short in ['7b:13','7b:15','9a:1','9a:4','9a:7','9a:13','9b:1','9b:5'] else 'closed'
 add('structure',ev(ref),dict(title=titles[short],primary=True,boundary=boundary,legacy_ids=[]),key='s'+short)

# Hand-authored source-only semantic inventory. No worker data or semantic extraction heuristics.
unit('7b:6',None,'שנאמר','רב חסדא','causal teaching',['Rain is withheld because terumot and tithes are neglected.'],key='tithes')
proof('7b:6','שנאמר','מאי משמע','tithes.c0')
q('7b:6','מאי משמע','תנא דבי','How does the verse imply this?','tithes.q')
unit('7b:6','תנא דבי',None,'תנא דבי רבי ישמעאל','seasonal interpretation',['Because commands for summer were not performed, winter snow water is taken away.'],key='season')
edge(keys['season.c0'],keys['tithes.q'],'answer',ev('7b:6','תנא דבי'))
edge(keys['season.c0'],keys['tithes.c0'],'support',ev('7b:6','תנא דבי'))
unit('7b:7',None,'שנאמר','רבי שמעון בן פזי','causal teaching',['Rain is withheld because of speakers of slander.'],key='slander')
proof('7b:7','שנאמר',None,'slander.c0')
unit('7b:8',None,'שנאמר','רב המנונא','causal teaching',['Rain is withheld because of brazen people.'],key='brazenrain',chain=['רב סלא','רב המנונא'])
proof('7b:8','שנאמר','ואמר רב סלא','brazenrain.c0')
unit('7b:8','ואמר רב סלא','שנאמר ומצח','רב המנונא','future consequence',['A brazen person will eventually stumble in transgression.'],key='future',chain=['רב סלא','רב המנונא'])
proof('7b:8','שנאמר ומצח','רב נחמן אמר','future.c0')
unit('7b:8','רב נחמן אמר','שנאמר היה','רב נחמן','alternative temporal position',['A brazen person is known already to have stumbled in transgression.'],key='past')
proof('7b:8','שנאמר היה',None,'past.c0')
edge(keys['past.c0'],keys['future.c0'],'objection',ev('7b:8','רב נחמן אמר'),False)
unit('7b:9',None,'שנאמר','רבה בר רב הונא','permission',['One may call a brazen person wicked.'],key='wicked')
proof('7b:9','שנאמר','רב נחמן בר יצחק','wicked.c0')
unit('7b:9','רב נחמן בר יצחק','שנאמר (קהלת','רב נחמן בר יצחק','permission',['One may hate a brazen person.'],key='hate')
proof('7b:9','שנאמר (קהלת',None,'hate.c0')
unit('7b:10',None,'שנאמר','רב קטינא','causal teaching',['Rain is withheld because Torah study is neglected.'],key='torah')
unit('7b:10','שנאמר',None,None,'verse and word interpretations',['The verse בעצלתים ימך המקרה is interpreted through Israel’s idleness in Torah study.','The euphemistic שונאו של הקב"ה becomes poor in this exposition.','מך means poor, supported by Leviticus 27:8.','מקרה refers to the Holy One, supported by Psalms 104:3.'],key='torahproof',unc=['Continuation follows Rav Qetina; individual explanatory clauses have no separately repeated named speaker.'])
edge(keys['torahproof'],keys['torah.c0'],'support',ev('7b:10','שנאמר'))
unit('7b:11',None,'תנא דבי','רב יוסף','alternative proof',['Job 37:21 provides another proof for the preceding teaching.','אור is interpreted as Torah, supported by Proverbs 6:23.'],key='joseph',unc=['The causal topic is inherited from 7b:10; this is an alternative proof, not a stated rejection.'])
edge(keys['joseph'],keys['torah.c0'],'support',ev('7b:11',None,'תנא דבי'))
unit('7b:11','תנא דבי',None,"תנא דבי ר' ישמעאל",'cloud interpretation',['Even when the sky has formations ready to bring dew and rain, the wind passes and clears them.'],key='clear')
edge(keys['clear.c0'],keys['joseph.c0'],'support',ev('7b:11','תנא דבי'))
unit('7b:12',None,'שנאמר',"ר' אמי",'causal teaching',['Rain is withheld because of robbery.'],key='robbery')
unit('7b:12','שנאמר',None,None,'scriptural derivation',['כפים is interpreted as violence, supported by Jonah 3:8.','אור is interpreted as rain, supported by Job 37:11.','Job 36:32 is read as covering light because of the sin of hands.'],key='robberyproof')
edge(keys['robberyproof'],keys['robbery.c0'],'support',ev('7b:12','שנאמר'))
q('7b:13',None,'ירבה','What is the remedy?','robbery.q')
unit('7b:13','ירבה','שנאמר',None,'remedy',['Increase prayer.'],conditions=['Rain withheld in preceding robbery discussion.'],key='prayer',unc=['No new explicit speaker; do not turn inherited discussion into explicit named attribution.'])
edge(keys['prayer.c0'],keys['robbery.q'],'answer',ev('7b:13','ירבה','שנאמר'))
proof('7b:13','שנאמר',None,'prayer.c0')
q('7b:14','מאי דכתיב','אם ראית','What is meant by Ecclesiastes 10:10?','iron.q')
unit('7b:14','אם ראית',None,"ר' אמי",'conditional interpretation',['If the sky is dull as iron and withholds dew and rain, the generation’s corrupted deeds are the cause.'],conditions=['Sky appears like iron, withholding dew and rain.'],mode='conditional',key='iron')
edge(keys['iron.c0'],keys['iron.q'],'answer',ev('7b:14'))
q('7b:15',None,'יתגברו','What is their remedy?','ironremedy.q')
unit('7b:15','יתגברו','ויתרון',None,'remedy',['They should strengthen their pleas for mercy, as וחילים יגבר is read.'],key='mercy')
edge(keys['mercy.c0'],keys['ironremedy.q'],'answer',ev('7b:15','יתגברו','ויתרון'))
unit('7b:15','ויתרון',None,None,'a fortiori preference',['All the more so if their deeds had been proper from the outset.'],key='priorgood')
edge(keys['priorgood.c0'],keys['mercy.c0'],'qualification',ev('7b:15','ויתרון'))

unit('8b:12',None,'שנאמר','רבי יצחק','sunshine teaching',['Sabbath sunshine is charity to the poor.'],key='sun')
proof('8b:12','שנאמר','ואמר רבי יצחק','sun.c0')
unit('8b:12','ואמר רבי יצחק','שנאמר (דברים','רבי יצחק','rain blessing',['The day of rain is great: even a coin in one’s purse is blessed.'],key='coin')
proof('8b:12','שנאמר (דברים',None,'coin.c0')
unit('8b:13',None,'שנאמר','רבי יצחק','hidden blessing',['Blessing is found only in what is hidden from the eye.'],key='hidden')
proof('8b:13','שנאמר','תנא דבי','hidden.c0')
unit('8b:13','תנא דבי','שנאמר יצו',"תנא דבי ר' ישמעאל",'parallel hidden blessing',['Blessing is found only in what the eye does not control.'],key='unseen')
proof('8b:13','שנאמר יצו',None,'unseen.c0')
unit('8b:14',None,'התחיל למוד','ת"ר','prayer before measuring',['On entering to measure one’s threshing floor, ask God to send blessing to the work of our hands.'],conditions=['Before beginning measurement.'],key='before')
unit('8b:14','התחיל למוד','מדד ואח','ת"ר','prayer while measuring',['Once measurement has begun, say: Blessed is He who sends blessing into this heap.'],conditions=['Measurement begun.'],key='during')
unit('8b:14','מדד ואח','לפי שאין','ת"ר','prayer after measuring',['A blessing uttered after measuring is a vain prayer.'],conditions=['Measurement already completed.'],key='after')
unit('8b:14','לפי שאין',None,'ת"ר','reason for timing',['Blessing is not found in something weighed.','Blessing is not found in something measured.','Blessing is not found in something counted.','Blessing is found in something hidden from the eye.'],key='measured')
edge(keys['measured'],keys['after.c0'],'support',ev('8b:14','לפי שאין'))
unit('8b:15',None,'אמר רבי יוחנן',None,'mnemonic; parenthetical מעשה preserved',position=False,key='mnemonic')
unit('8b:15','אמר רבי יוחנן','שנאמר','רבי יוחנן','rain comparison',['The day of rain is as great as the day of ingathering exiles.'],key='gather')
proof('8b:15','שנאמר',None,'gather.c0')
unit('8b:16',None,'שנאמר','רבי יוחנן','rain benefit',['The day of rain is great because even armies cease on it.'],key='army')
proof('8b:16','שנאמר','ואמר רבי יוחנן','army.c0')
unit('8b:16','ואמר רבי יוחנן','שנאמר (משלי','רבי יוחנן','withheld rain',['Rain is withheld because people publicly pledge charity and fail to give.'],conditions=['Public charity pledge not fulfilled.'],key='charity')
proof('8b:16','שנאמר (משלי',None,'charity.c0')
unit('8b:17',None,None,'רבי יוחנן','attribution and opening question continued across page',key='titheopen')
add('questions',[ev('8b:17'),ev('9a:1',None,'עשר בשביל')],dict(formulation='What is meant by עשר תעשר?',question_origin='explicit',conditions=[],answer_set_status='partial'),[keys['titheopen']],key='tithemeaning.q')
unit('9a:1',None,'עשר בשביל',None,'scripture quoted under preceding question',position=False,key='titheverse')
unit('9a:1','עשר בשביל',None,'רבי יוחנן','inherited answer',['Tithe so that you become wealthy.'],key='enrich',unc=['Named attribution is in 8b:17, not repeated here.'])
edge(keys['enrich.c0'],keys['tithemeaning.q'],'answer',[ev('8b:17'),ev('9a:1')])
unit('9a:2',None,'אמר ליה',None,'narrative',['Rabbi Yoḥanan encountered Resh Lakish’s child.'],key='meet',position=False)
D=['רבי יוחנן','ינוקא דריש לקיש']; du=['Repeated אמר ליה does not explicitly name each turn. Candidate identities kept unresolved rather than assigned by order.']
unit('9a:2','אמר ליה אימא','א"ל עשר תעשר',D,'request for recited verse',['A dialogue participant asks the child to recite his verse.'],key='recite',unc=du,position=False)
unit('9a:2','א"ל עשר תעשר','א"ל ומאי',D,'verse response',['The verse recited is עשר תעשר.'],key='recited',unc=du,position=False)
q('9a:2','א"ל ומאי','א"ל עשר בשביל','What is meant by עשר תעשר?','childmeaning.q',unc=du)
unit('9a:2','א"ל עשר בשביל','אמר ליה מנא',D,'explanation in dialogue',['Tithe so that you become wealthy.'],key='childenrich',unc=du)
edge(keys['childenrich.c0'],keys['childmeaning.q'],'answer',ev('9a:2','א"ל עשר בשביל','אמר ליה מנא'))
q('9a:2','אמר ליה מנא','א"ל זיל','Whence do you know this?','whence.q',unc=du)
unit('9a:2','א"ל זיל',None,D,'invitation to test',['Go and test it.'],key='test',unc=du)
edge(keys['test.c0'],keys['whence.q'],'answer',ev('9a:2','א"ל זיל'))
q('9a:3',None,'א"ל הכי','Is testing the Holy One permitted, given לא תנסו?','testing.q',unc=du)
edge(keys['testing.q'],keys['test.c0'],'objection',ev('9a:3',None,'א"ל הכי'))
unit('9a:3','א"ל הכי','שנאמר','רבי הושעיא','exception reported in dialogue',['The tithe case is excepted from the prohibition on testing God.'],conditions=['Testing the promise concerning tithing.'],key='exception',unc=['The immediate reporter is one of the dialogue participants, not explicitly named in this turn.'])
add('attributions',ev('9a:3','א"ל הכי','שנאמר'),dict(surface='א"ל',role='transmitter',candidates=D,scope=keys['exception'],transmission_chain=['רבי הושעיא']),[keys['exception']],du)
proof('9a:3','שנאמר',None,'exception.c0')
edge(keys['exception.c0'],keys['testing.q'],'answer',ev('9a:3','א"ל הכי'))
q('9a:4',None,'אמר רמי','What is meant by עד בלי די?','enough.q')
unit('9a:4','אמר רמי','א"ל אי','רב','verse interpretation',['Until your lips wear out from saying enough.'],key='enough',chain=['רמי בר חמא','רב'])
edge(keys['enough.c0'],keys['enough.q'],'answer',ev('9a:4','אמר רמי','א"ל אי'))
unit('9a:4','א"ל אי',None,D,'dialogue reply',['Had I reached that verse, I would not have needed you and Hoshaya your teacher.'],key='reply',unc=['Address to your teacher supports identifying the respondent as the child, but this is inference; candidate set preserved.'],position=False)
unit('9a:5',None,'דיתיב ואמר',None,'second encounter narrative',['Rabbi Yoḥanan again encountered Resh Lakish’s child.'],key='meet2',position=False)
unit('9a:5','דיתיב ואמר',None,'ינוקיה דריש לקיש','child recites scripture',['A person’s folly distorts his way, while his heart rages against God.'],key='folly',position=False)
unit('9a:6',None,'אמר מי',None,'narrative',['Rabbi Yoḥanan sat wondering.'],position=False)
q('9a:6','אמר מי','א"ל אטו','Is anything written in Writings not alluded to in Torah?','torahhint.q')
add('attributions',ev('9a:6',None,'א"ל אטו'),dict(surface='רבי יוחנן',role='speaker',candidates=['רבי יוחנן'],scope=keys['torahhint.q'],transmission_chain=[]),[keys['torahhint.q']])
unit('9a:6','א"ל אטו',None,'ינוקיה דריש לקיש','counter-question and cited Torah antecedent',['Genesis 42:28, where the brothers ask what God has done to them, supplies a Torah allusion to the Proverbs teaching.'],key='hint',unc=['Child identified by dialogue context; no new proper name in the turn.'])
q('9a:6','א"ל אטו','והכתיב','Is this not alluded to in Torah?','hint.q')
edge(keys['hint.c0'],keys['torahhint.q'],'answer',ev('9a:6','א"ל אטו'))
edge(keys['hint.c0'],keys['folly.c0'],'support',[ev('9a:5','דיתיב ואמר'),ev('9a:6','א"ל אטו')])
unit('9a:7',None,'אמרה ליה',None,'narrative',['He raised his eyes and looked at him.','The child’s mother came and took him away.'],key='remove',unc=['Gaze subject is understood contextually as Rabbi Yoḥanan; no explicit name in this segment.'],position=False)
unit('9a:7','אמרה ליה',None,'אימיה','mother’s warning',['Come away from him lest he do to you as he did to your father.'],key='warning',unc=['Passage does not here narrate what happened to the father; no external explanation supplied.'],position=False)

unit('9a:8',None,'מטר בשביל יחיד דכתיב','רבי יוחנן','rain and sustenance distinction',['Rain can come for an individual.','Sustenance comes for many.'],key='rainmany',unc=['Opening parenthesis is preserved in evidence, not silently emended.'])
proof('9a:8','מטר בשביל יחיד דכתיב','פרנסה בשביל רבים דכתיב','rainmany.c0')
proof('9a:8','פרנסה בשביל רבים דכתיב',None,'rainmany.c1')
unit('9a:9',None,'ר\' יוסי',None,'objection introduction',position=False,key='objectionintro')
unit('9a:9',"ר' יוסי",'מתה מרים',"ר' יוסי בר' יהודה",'baraita offered as objection',['Three good leaders arose for Israel: Moses, Aaron and Miriam.','Three gifts were given through them: well, cloud and manna.','The well was in Miriam’s merit.','The cloud pillar was in Aaron’s merit.','Manna was in Moses’s merit.'],key='gifts')
edge(keys['gifts.c4'],keys['rainmany.c1'],'objection',ev('9a:9'))
unit('9a:9','מתה מרים',None,"ר' יוסי בר' יהודה",'baraita continuation',['When Miriam died, the well disappeared, as adjoining verses about her death and the lack of water indicate.','The well returned in the merit of the other two.'],key='miriam',unc=['Attribution inherited from opening baraita.'])
unit('9a:10',None,'שנאמר',"ר' יוסי בר' יהודה",'baraita continuation',['When Aaron died, the clouds of glory disappeared.'],key='aaron',unc=['Attribution inherited from opening baraita.'])
unit('9a:10','שנאמר','והיינו דכתיב',None,'scriptural exposition',['The king of Arad heard that Aaron died and the clouds had disappeared.','He supposed permission had been given him to wage war against Israel.'],key='arad')
q('9a:10','מה שמועה שמע','שמע שמת','What report did the king hear?','heard.q')
edge(keys['arad.c0'],keys['heard.q'],'answer',ev('9a:10','שמע שמת','והיינו דכתיב'))
proof('9a:10','והיינו דכתיב',None,'aaron.c0')
unit('9a:11',None,'כדדריש',"ר' אבהו",'alternate reading',['Read וייראו, they feared, rather than ויראו, they saw.'],key='fear')
edge(keys['fear.c0'],keys['aaron.c0'],'support',[ev('9a:10','והיינו דכתיב'),ev('9a:11',None,'כדדריש')])
unit('9a:11','כדדריש',None,'ר"ל','lexical teaching',['כי functions with four senses: אי, דלמא, אלא, דהא.'],key='ki')
edge(keys['ki.c0'],keys['fear.c0'],'support',ev('9a:11','כדדריש'))
unit('9a:12',None,'שנאמר',"ר' יוסי בר' יהודה",'baraita continuation',['Both the well and clouds returned through Moses’s merit.','When Moses died all the gifts disappeared.'],key='moses',unc=['Baraita resumed after named exegetical interjection; exact voice layering is editorial segmentation.'])
unit('9a:12','שנאמר','וכי',None,'Zechariah prooftext',['Zechariah 11:8 says the three shepherds were removed in one month.'],key='shepherds',position=False)
q('9a:12','וכי','אלא מלמד','Did they die in a single month, when Miriam died in Nisan, Aaron in Av, Moses in Adar?','months.q')
unit('9a:12','והלא','אלא מלמד',None,'chronological objection',['Miriam died in Nisan.','Aaron died in Av.','Moses died in Adar.'],key='dates')
edge(keys['dates'],keys['shepherds.c0'],'objection',ev('9a:12','וכי','אלא מלמד'))
unit('9a:12','אלא מלמד',None,None,'resolution of verse',['The three good gifts given through them were all removed in a single month.'],key='giftmonth',mode='reconciled')
edge(keys['giftmonth.c0'],keys['months.q'],'answer',ev('9a:12','אלא מלמד'))
edge(keys['giftmonth.c0'],keys['moses.c1'],'support',ev('9a:12','אלא מלמד'))
unit('9a:13',None,'שאני משה',None,'objection inference',['Thus sustenance is found to come for an individual.'],key='single',mode='challenged')
edge(keys['moses.c0'],keys['single.c0'],'support',[ev('9a:12',None,'שנאמר'),ev('9a:13',None,'שאני משה')])
edge(keys['single.c0'],keys['rainmany.c1'],'objection',ev('9a:13',None,'שאני משה'))
unit('9a:13','שאני משה',None,None,'distinction resolving objection',['Moses is different: since he sought for the many, he counts as many.'],key='distinction',mode='reconciled',conditions=['Moses requests sustenance for the many.'])
edge(keys['distinction.c0'],keys['single.c0'],'local_resolution',ev('9a:13','שאני משה'))
edge(keys['distinction.c0'],keys['rainmany.c1'],'qualification',ev('9a:13','שאני משה'))
unit('9a:14',None,'כל אימת',None,'narrative',['Rav Huna bar Manoaḥ, Rav Shemuel bar Idi and Rav Ḥiyya of Vastanya regularly attended Rava.','After Rava’s death they came to Rav Pappa.'],key='pupils',position=False)
unit('9a:14','כל אימת',None,None,'narrative',['When Rav Pappa taught something they found unconvincing, they gestured to each other.','This distressed him.'],key='gestures',position=False)
unit('9b:1',None,'למחר',None,'dream narrative',['In his dream the verse ואכחיד את שלשת הרועים was read to him.'],key='dream',unc=['Subject inherited as Rav Pappa; the dream reader is unspecified.'],position=False)
unit('9b:1','למחר','אמר להו',None,'farewell narrative',['The next day, when they departed from him, he spoke to them.'],position=False)
unit('9b:1','אמר להו',None,'רב פפא','farewell',['Let the rabbis go in peace.'],key='farewell',unc=['Speaker inherited from narrative, not explicitly renamed here. No deaths or expulsion asserted.'],position=False)
unit('9b:3',None,'דאמר ר"ל',None,'editorial agreement',['Resh Lakish too holds that rain may come for an individual.'],key='agreement')
q('9b:3','מנין','דכתיב','Whence is rain for an individual derived?','rainindividual.q')
unit('9b:3','דאמר ר"ל','דכתיב','ר"ל','rain for individual',['Rain can come for an individual.'],key='rlrain')
proof('9b:3','דכתיב',None,'rlrain.c0')
edge(keys['rlrain.c0'],keys['rainindividual.q'],'answer',ev('9b:3','דאמר ר"ל'))
edge(keys['rlrain.c0'],keys['rainmany.c0'],'support',ev('9b:3'))
unit('9b:4',None,'ותניא',None,'scriptural delimitation',['The possibility that rain must be for everyone is excluded by לאיש.'],key='all',mode='rejected')
unit('9b:4','ותניא','אי שדה',None,'baraita delimitation',['The possibility that all one’s fields must receive rain is excluded by שדה.'],key='fields',mode='rejected')
unit('9b:4','אי שדה',None,None,'baraita delimitation',['The possibility that the entire field must receive rain is excluded by עשב.'],key='grass',mode='rejected')
for k in ['all','fields','grass']:edge(keys[k+'.c0'],keys['rlrain.c0'],'qualification',next(r['evidence'] for r in R if r['id']==keys[k]))
unit('9b:5',None,'אמר הא',None,'garden narrative',['Rav Daniel bar Qetina had a garden and inspected it every day.'],key='garden',position=False)
unit('9b:5','אמר הא','ואתא','רב דניאל בר קטינא','garden assessment',['This bed needs water, while that bed does not.'],key='beds',position=False)
unit('9b:5','ואתא',None,None,'garden narrative',['Rain came and watered wherever water was needed.'],key='selective',position=False)
edge(keys['selective.c0'],keys['grass.c0'],'support',ev('9b:5'))

for a,b in [('7b:10','7b:11'),('7b:12','7b:13'),('7b:14','7b:15'),('8b:17','9a:1'),('9a:2','9a:3'),('9a:3','9a:4'),('9a:5','9a:6'),('9a:6','9a:7'),('9a:8','9a:9'),('9a:9','9a:10'),('9a:10','9a:11'),('9a:11','9a:12'),('9a:12','9a:13'),('9a:14','9b:1'),('9b:3','9b:4'),('9b:4','9b:5')]:
 edge(keys['s'+a],keys['s'+b],'continuation',[ev(a),ev(b)])

notes={
'7b:6':'Cause, proof, explicit interpretive question and school answer separately inventoried.',
'7b:7':'Slander cause and cited support; no explicit question or alternatives.',
'7b:8':'Reporter Rav Sala distinguished from Rav Hamnuna; Rav Naḥman’s past sin alternative preserved without announcing a final resolution.',
'7b:9':'Two permissions retained; no invented dispute between permission to call wicked and permission to hate.',
'7b:10':'Torah neglect, euphemistic wording and two lexical derivations retained; interpretation versus explicit attribution separated.',
'7b:11':'Rav Joseph’s alternative proof retained with school continuation; not represented as rejecting the preceding cause.',
'7b:12':'Robbery, hands/violence and light/rain equivalences retained; remedy in next core.',
'7b:13':'Remedy question, prayer answer and scriptural derivation retained; anonymous immediate voice.',
'7b:14':'Opening named attribution, question and conditional corrupted-deeds interpretation retained.',
'7b:15':'Remedy, mercy and a fortiori prior good deeds retained.',
'8b:12':'Two distinct Rabbi Isaac teachings and their proofs retained.',
'8b:13':'Both formulations and separate authority occurrences retained; no asserted disagreement.',
'8b:14':'Before/during/after measuring conditions, vain prayer and weighed/measured/counted/hidden reason retained.',
'8b:15':'Mnemonic including parenthetical מעשה retained as non-propositional utterance; ingathering comparison and proof retained.',
'8b:16':'Armies cessation and public unfulfilled charity pledge causes separately retained.',
'8b:17':'Attribution/question fragment continued to 9a:1, never treated as an independent complete claim.',
'9a:1':'Verse and enriching-tithe answer joined to prior attribution with explicit cross-segment evidence.',
'9a:2':'Narrative, verse request/response, meaning question, enrichment answer, source question and testing invitation retained. Repeated anonymous dialogue markers retain two identity candidates.',
'9a:3':'Testing prohibition objection, Hoshaya exception and Malachi proof retained. Unnamed reporter not silently identified.',
'9a:4':'Inserted Rav teaching via Rami bar Ḥama, explicit question and final dialogue reply distinguished.',
'9a:5':'Second meeting and child’s quoted Proverbs statement retained.',
'9a:6':'Rabbi Yoḥanan’s wondering/question, child’s counter-question and Genesis answer retained.',
'9a:7':'Gaze, mother’s removal and warning retained; father’s fate not reconstructed from outside sources.',
'9a:8':'Individual rain versus collective sustenance, two separate proofs and original parenthesis retained. Later challenge and resolution read.',
'9a:9':'Objection baraita, three leaders, gifts, merits, death, loss and restoration of well retained.',
'9a:10':'Clouds, report, king’s supposition and verse retained; permission is his supposition, not narrator endorsement.',
'9a:11':'Abbahu reading distinguished from Resh Lakish lexical authority; all four כי senses retained.',
'9a:12':'Both restorations, Moses’s death, three dates, objection to single-month reading and resolution concerning gifts retained.',
'9a:13':'Objection inference remains a challenged stage; Moses-for-many resolution qualifies sustenance generalization.',
'9a:14':'Three separately named attendees, Rava’s death, Rav Pappa teaching, gestures and distress retained; dream/farewell reviewed in 9b:1.',
'9b:1':'Context-only completion of dream and peaceful farewell; no claimed execution or death.',
'9b:3':'Context-only corroboration by Resh Lakish; same rain position, no invented dispute.',
'9b:4':'Context-only three rejected broad scopes and their delimiters retained.',
'9b:5':'Context-only garden narrative, assessment and selective rain illustrate narrow scope.'}
layers=['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']
C=[]
for ref in reviewed:
 for layer in layers:
  ids=[r['id'] for r in R if (r['layer']==layer or layer=='reconciliation') and any(e['segment_id']==ref for e in r['evidence'])]
  rationale=notes[ref.split(' ')[1]]
  if not ids:rationale+=' Source-based pass found no separate '+layer+' record here; no implicit question, position or edge invented.'
  C.append(dict(segment_id=ref,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
reading=dict(schema_version='2.0.0-production',tractate='Taanit',owner='isolated-source-only-review101',epoch=1,source_sha256=job['source']['sha256'],protocol_sha256=job['common_documents'][0]['sha256'],schema_sha256=job['common_documents'][1]['sha256'],execution=dict(route='interactive_agent',agent_id=AGENT,model_id=None),records=R,coverage=C,open_tails=[])

def validate(obj):
 jsonschema.Draft202012Validator(schema).validate(obj)
 byid={r['id']:r for r in obj['records']};assert len(byid)==len(obj['records'])
 n_ev=0
 for r in obj['records']:
  for e in r['evidence']:
   assert e['segment_id'] in reviewed
   t=texts[e['segment_id']];a=e['start_char'];b=e['end_char'];assert 0<=a<b<=len(t) and t[a:b]==e['quote'];n_ev+=1
  assert all(x in byid for x in r['links'])
  c=r['content']
  if r['layer']=='positions':
   assert byid[c['claim_id']]['layer']=='claims' and c['claim_id'] in r['links']
   assert c['question_id'] is None or byid[c['question_id']]['layer']=='questions'
  if r['layer']=='attributions': assert c['scope'] in byid and c['scope'] in r['links']
  if r['layer']=='edges':
   a=byid[c['source_id']]['layer'];b=byid[c['target_id']]['layer']
   assert c['source_id'] in r['links'] and c['target_id'] in r['links']
   assert (a==b=='structure') if c['relation']=='continuation' else (a in ['claims','utterances','questions','positions'] and b in ['claims','utterances','questions','positions'])
 for ref in reviewed:
  iv=sorted((e['start_char'],e['end_char']) for r in obj['records'] if r['layer']=='structure' and r['content']['primary'] for e in r['evidence'] if e['segment_id']==ref)
  assert iv and iv[0][0]==0 and iv[-1][1]==len(texts[ref])
  assert all(a[1]==b[0] for a,b in zip(iv,iv[1:]))
  cv=[c for c in obj['coverage'] if c['segment_id']==ref];assert len(cv)==8 and {c['layer'] for c in cv}==set(layers)
  for c in cv:
   assert c['extraction_state']=='completed' and c['rationale'] and all(i in byid for i in c['record_ids'])
   expected={r['id'] for r in obj['records'] if (r['layer']==c['layer'] or c['layer']=='reconciliation') and any(e['segment_id']==ref for e in r['evidence'])}
   assert set(c['record_ids'])==expected
 assert len([c for c in obj['coverage'] if c['segment_id'] in cores])==240
 assert set(c['segment_id'] for c in obj['coverage'])==set(reviewed)
 return dict(records=len(obj['records']),counts_by_layer=dict(collections.Counter(r['layer'] for r in obj['records'])),evidence_intervals=n_ev,core_segments=30,core_layer_cells=240,context_fully_reviewed_segments=len(ctx),context_layer_cells=len(ctx)*8,checks=['pinned input hashes','canonical plan hash','schema Draft202012','sample membership and raw span hashes','exact Unicode codepoint evidence','unique record IDs','all links','typed position claim/question foreign keys','attribution scope foreign keys','typed argument endpoints','complete gapless primary partitions','exact per-layer coverage inventories'])

def write_once(name,obj):
 b=json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2).encode('utf-8')+b'\n';p=OUT/name
 if p.exists(): assert p.read_bytes()==b, 'immutable file differs: '+str(p)
 else:
  with p.open('xb') as f:f.write(b)
 side=p.with_suffix(p.suffix+'.sha256');data=(sha(b)+'  '+name+'\n').encode()
 if side.exists():assert side.read_bytes()==data
 else:
  with side.open('xb') as f:f.write(data)
 return sha(b)

if __name__=='__main__':
 result=validate(reading)
 if '--verify-only' in sys.argv:
  frozen=read(OUT/'reading.json');assert frozen==reading;result=validate(frozen)
  for p in OUT.glob('*.sha256'):
   h,name=p.read_text().strip().split('  ',1);assert sha((OUT/name).read_bytes())==h
  print(json.dumps(dict(status='PASS_READ_ONLY',**result),ensure_ascii=False));sys.exit()
 h=write_once('reading.json',reading)
 incidental=[f'Taanit 7b:{i}' for i in [1,2,3,4,5,16]]+[f'Taanit 8b:{i}' for i in range(1,12)]+['Taanit 9b:2']+[f'Taanit 9b:{i}' for i in range(6,17)]
 exposure=dict(agent_id=AGENT,model_id=None,reading_sha256=h,job_id=job['job_id'],job_sha256=JHASH,pinned_inputs=inputs,plan_sha256=job['plan_sha256'],core_refs=cores,fully_reviewed_context_refs=ctx,incidental_original_display_refs=incidental,source_only=True,producer_annotation_exposure=False,prior_reading_exposure=False,handoff_exposure=False,source_metadata={k:source[k] for k in ['title','versionTitle','versionSource','license','language']},limitations=['Independent AI provisional source-only reading; no human scholarly certification.','No producer comparison, adjudication, production admission or promotion performed.','Speaker assignment in the first child dialogue remains uncertain where only אמר ליה occurs.','Context displayed outside the 34 fully inventoried segments does not count as reviewed coverage.','Local interpretation does not establish practical halakhah.','Owner and epoch identify only isolated output, not production authority.'])
 eh=write_once('exposure.json',exposure)
 helperhash=sha(pathlib.Path(__file__).read_bytes());p=OUT/'build_reading.py.sha256'
 if not p.exists():p.write_text(helperhash+'  build_reading.py\n',encoding='utf-8')
 else:assert p.read_text().startswith(helperhash)
 receipt=dict(status='PASS',reading_sha256=h,exposure_sha256=eh,helper_sha256=helperhash,**result)
 write_once('validation_receipt.json',receipt)
 print(json.dumps(receipt,ensure_ascii=False))
