from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.shunammite.20261126e5.'
assert r.sha(r.encoded(state))=='bbc4a021539ae17dff212339a4d163fd7446d8471db0eb430b143a350969d828'
refs=['10b:'+str(i) for i in range(14,37)]
for k,ns,title in [('room',range(14,22),'Upper room alternatives and receiving support'),('holy',range(22,26),'Recognition of holiness and hosting scholars'),('prayer',range(26,31),'Low place, feet alignment and prayer before eating'),('late',range(31,37),'Shema deadline, blessings after time and two report versions')]:add('s'+k,'structure',['10b:'+str(i) for i in ns],dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices={14:'Scriptural lemma',15:'Rav and Shmuel, unassigned views',16:'Anonymous question',17:'Anonymous answer',18:'Anonymous question',19:'Anonymous answer',20:'Scriptural furnishing lemma',21:'Abaye or Rabbi Yitzhak; Rabbi Yohanan citation',22:'Rabbi Yose bar Hanina',23:'Anonymous question; Rav and Shmuel unassigned',24:'Rabbi Yose bar Hanina',25:'Rabbi Yose bar Hanina reporting Rabbi Eliezer ben Yaakov',26:'Same transmission',27:'Supporting baraita',28:'Same transmission',29:'Parenthetical Rabbi Yitzhak/Rabbi Yohanan and Rabbi Yose bar Hanina/Rabbi Eliezer ben Yaakov reports',30:'Parenthetical alternative-version marker and multiple printed authorities',31:'Mishnah lemma; Rav Yehuda reporting Shmuel',32:'Mishnah lemma',33:'Rav Hisda reporting Mar Uqva, first version',34:'Anonymous baraita objection and refutation',35:'Alternative Rav Hisda/Mar Uqva report and supporting baraita',36:'Rabbi Mani'}
for n in range(14,37):add('u'+str(n),'utterances',['10b:'+str(n)],dict(textual_voice=voices[n],discourse_role='Lemma, exposition or legal discussion',composition='composite'))
def claim(k,n,text,holders,cond=(),status='Reported locally',unc=()):
 ref='10b:'+str(n);c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('15upper',15,'One of Rav and Shmuel says it was an uncovered upper room and they roofed it.',['Rav','Shmuel'],status='Unassigned member of explicit pair',unc=['No speaker assignment by name order; later answers identify positions but not names.'])
claim('15porch',15,'The other says it was a large portico divided into two.',['Rav','Shmuel'],status='Other unassigned member of pair')
q('q16','10b:16','The portico view explains wall; what explains wall under the upper-room view?')
claim('17',17,'The answer reads wall as they roofed it.',['Anonymous Gemara'])
q('q18','10b:18','The upper-room view explains aliyah; what explains it under the portico view?')
claim('19',19,'The answer reads it as the finest of the rooms.',['Anonymous Gemara'])
claim('21receive',21,'Abaye, alternatively Rabbi Yitzhak, permits one wishing to receive benefit to do so like Elisha.',['Abaye','Rabbi Yitzhak'],cond=['Wishes to receive support'],status='Alternative attribution unresolved')
claim('21decline',21,'One not wishing to receive may decline like Samuel of Ramah.',['Abaye','Rabbi Yitzhak'],cond=['Does not wish to receive support'],status='Complementary permission, not opposing obligation')
claim('21home',21,'Rabbi Yohanan interprets Samuel’s home as accompanying him wherever he went.',['Rabbi Yohanan'])
claim('22',22,'Rabbi Yose bar Hanina derives from the woman recognizing the holy guest that a woman recognizes guests better than a man.',['Rabbi Yose bar Hanina'])
q('q23','10b:23','How did she know he was holy?')
claim('23fly',23,'One of Rav and Shmuel says she saw no fly pass over his table.',['Rav','Shmuel'],status='Unassigned first view')
claim('23sheet',23,'The other says she placed a linen sheet on his bed and saw no seminal emission upon it.',['Rav','Shmuel'],status='Unassigned second view')
claim('24holy',24,'Rabbi Yose bar Hanina says he is holy but his servant is not.',['Rabbi Yose bar Hanina'])
claim('24gehazi',24,'He explains Gehazi’s pushing her as grasping the splendor of her beauty.',['Rabbi Yose bar Hanina'],unc=['The euphemism בהוד יפיה is retained in exact evidence; no added anatomical description.'])
claim('25',25,'Rabbi Yose bar Hanina reports Rabbi Eliezer ben Yaakov that hosting a Torah scholar and benefiting him from one’s property is credited like offering regular sacrifices.',['Rabbi Eliezer ben Yaakov'],cond=['Hosts Torah scholar at home','Benefits scholar from property'])
claim('26',26,'The same chain forbids standing in a high place to pray and requires a low place, citing from the depths.',['Rabbi Eliezer ben Yaakov'])
claim('27',27,'A supporting baraita forbids prayer on a chair, stool or high place, requires a low place, and explains that there is no loftiness before God.',['Unnamed baraita'])
claim('28',28,'The same chain requires aligning the feet in prayer, citing their feet a straight foot.',['Rabbi Eliezer ben Yaakov'])
claim('29',29,'Do not eat over the blood is interpreted as not eating before praying concerning one’s blood.',['Rabbi Eliezer ben Yaakov through Rabbi Yose bar Hanina; parenthetical additional report'],cond=['Before prayer'],unc=['Source parenthesizes Rabbi Yitzhak reporting Rabbi Yohanan before the main chain; retain textual attribution ambiguity.'])
claim('30',30,'Eating and drinking before prayer is read as casting God behind one’s pride: after becoming proud this person accepted divine kingship.',['Authority attribution unresolved among printed reports'],cond=['Eats and drinks before prayer'],unc=['Printed (א"ד) and concatenated Rabbi Yitzhak/Rabbi Yohanan/Rabbi Yose bar Hanina/Rabbi Eliezer ben Yaakov names are not silently converted into one historical chain.'])
claim('31',31,'Rav Yehuda reports Shmuel ruling like Rabbi Yehoshua’s three-hour limit.',['Shmuel'],status='Explicit reported ruling')
claim('33',33,'In the first report Rav Hisda through Mar Uqva qualifies late reading by not saying Yotzer Or.',['Mar Uqva'],cond=['Shema read after its time'],status='First report explicitly refuted at10b34')
claim('34baraita',34,'The baraita says late reading retains Torah-reading value and the reader blesses twice before and once after.',['Unnamed baraita'],cond=['Late Shema recitation'])
claim('34refute',34,'The discussion declares Rav Hisda’s first report refuted.',['Anonymous Gemara'],status='Explicit תיובתא')
claim('35',35,'An alternative report has Rav Hisda through Mar Uqva explain not lost as not losing the blessings; the same baraita supports it.',['Mar Uqva'],cond=['Late Shema recitation'],status='Alternative report supported, not silently overwriting first version')
claim('36',36,'Rabbi Mani infers timely Shema is greater than Torah study because only late reading is compared to reading Torah.',['Rabbi Mani'])
att('a15','10b:15','רב ושמואל חד אמר','speaker',['רב','שמואל'],'Upper-room and portico alternatives',unc=['View holders remain unidentified.'])
att('a21','10b:21',"אביי ואיתימא ר' יצחק",'speaker',['אביי','רבי יצחק'],'Support reception alternatives',unc=['Unresolved ואיתימא.'])
att('a21y','10b:21',"ר יוחנן",'quoted_authority',['רבי יוחנן'],pre+'c21home')
att('a22','10b:22',"ר יוסי בר' חנינא",'speaker',['רבי יוסי בר חנינא'],pre+'c22')
att('a23','10b:23','רב ושמואל חד אמר','speaker',['רב','שמואל'],'Holiness signs',unc=['Unassigned pair; no correlation to the assignments of10b15 asserted.'])
att('a24','10b:24',"ר יוסי בר' חנינא",'speaker',['רבי יוסי בר חנינא'],'Holiness and servant interpretation')
for n in [25,26,28]:att('a'+str(n),'10b:'+str(n),"ר יוסי בר' חנינא",'transmitter',['רבי יוסי בר חנינא'],'Teaching of Rabbi Eliezer ben Yaakov',chain=['רבי יוסי בר חנינא','רבי אליעזר בן יעקב'])
att('a29','10b:29','(א"ר יצחק א"ר יוחנן)','transmitter',['רבי יצחק','רבי יוחנן'],'Parenthetical report alongside Yose/Eliezer chain',unc=['Do not concatenate the parenthetical and following chains as established historical transmission.'])
att('a30','10b:30','(א"ד) א"ר יצחק א"ר יוחנן א"ר יוסי','transmitter',['רבי יצחק','רבי יוחנן','רבי יוסי בר חנינא'],'Printed alternative/concatenated report',unc=['Segmentation and authority attachment unresolved in unannotated source; literal evidence preserved.'])
att('a31','10b:31','רב יהודה אמר שמואל','transmitter',['רב יהודה'],pre+'c31',chain=['רב יהודה','שמואל'])
for n in [33,35]:att('a'+str(n),'10b:'+str(n),'רב חסדא אמר מר עוקבא','transmitter',['רב חסדא'],'Version-specific late-reading report',chain=['רב חסדא','מר עוקבא'])
att('a36','10b:36','ר מני','speaker',['רבי מני'],pre+'c36')
for k,n,a,b,rel in [('15',15,'c15upper','c15porch','distinction'),('17',17,'c17','q16','answer'),('19',19,'c19','q18','answer'),('21',21,'c21home','c21decline','support'),('23f',23,'c23fly','q23','answer'),('23s',23,'c23sheet','q23','answer'),('23d',23,'c23fly','c23sheet','distinction'),('24',24,'c24gehazi','c24holy','support'),('27',27,'c27','c26','support'),('34',34,'c34baraita','c33','objection'),('34r',34,'c34refute','c33','correction'),('35',35,'c34baraita','c35','support'),('35d',35,'c35','c33','distinction')]:edge('e'+k,'10b:'+str(n),a,b,rel)
for x in rows:
 if x['id'] in [pre+'e15',pre+'e23d',pre+'e35d']:x['uncertainty'].append('Textual alternatives; arrow does not assign a historical objection direction or resolve unnamed holders.')
 if x['layer']=='claims':x['content']['scope']='Local exegesis and prayer rulings; two Rav–Shmuel pairs stay unassigned, parenthetical chains remain uncertain, and refuted versus supported report versions remain separate.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read10b14–41; reread core10b14–36 for both unassigned Rav/Shmuel pairs, word explanations, optional receiving support, holiness/hosting, prayer posture and food rules with uncertain chains, three-hour ruling, first-version refutation and supported alternative. Scriptural and Mishnah lemmas14/20/32 are not additional claims. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch16_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch16_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch16_receipt.json',r.encoded(out));print(r.encoded(out).decode())
