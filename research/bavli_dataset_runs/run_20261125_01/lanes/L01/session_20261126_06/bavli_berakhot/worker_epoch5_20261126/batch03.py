from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.tefillin.20261126e5.'
assert r.sha(r.encoded(state))=='d66e1fe69fc2cc99bd4ce982eacbace92300d4b02f488d8bb4ddf8391219de0c'
refs=['6a:'+str(i) for i in range(17,26)]+['6b:'+str(i) for i in range(1,18)]
for k,rr,title in [('tefillin',refs[:10],'Divine tefillin: derivation, contents and compartment arrangement'),('absent',refs[10:13],'Absence from synagogue and its reason'),('ten',refs[13:14],'God enters without finding ten'),('place',refs[14:17],'Fixed place for prayer'),('run',refs[17:19],'Walking out, running in and running on Sabbath'),('rewards',refs[19:],'Distinct rewards of gatherings and practices')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Rabbi Avin bar Rav Adda reporting Rabbi Yitzhak','Expository continuation','Exposition citing Rabbi Eliezer the Great','Rav Nahman bar Yitzhak and Rav Hiyya bar Avin','Anonymous question and exposition of divine speech','Expository divine speech','Rav Aha son of Rava to Rav Ashi','Rav Ashi','Anonymous objection and arrangement','Continuation of arrangement','Ravin bar Rav Adda reporting Rabbi Yitzhak','Expository qualification','Expository explanation','Rabbi Yohanan','Rabbi Helbo reporting Rav Huna','Continuation of reported teaching','Anonymous proof question and answer','Rabbi Helbo reporting Rav Huna; Abaye','Rabbi Zeira recalling Rabbi Tanhum reporting Rabbi Yehoshua ben Levi','Rabbi Zeira','Abaye','Rava','Rav Pappa','Mar Zutra','Rav Sheshet','Rav Ashi']
assert len(voices)==len(refs)
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Teaching or discussion',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
q('q17','6a:17','What is the proof that God puts on tefillin?')
claim('17','6a:17','Rabbi Avin bar Rav Adda reports Rabbi Yitzhak deriving divine tefillin from God swearing by His right hand and mighty arm.',['Rabbi Yitzhak'])
claim('18right','6a:18','His right hand is interpreted as Torah, citing fiery law from His right.',['Expository continuation'])
claim('18arm','6a:18','His mighty arm is interpreted as tefillin, citing God giving strength to His people.',['Expository continuation'])
q('q19','6a:19','How are tefillin strength for Israel?')
claim('19','6a:19','The verse describing nations seeing God’s name upon Israel and fearing them is linked to Rabbi Eliezer the Great’s identification of this with head tefillin.',['Rabbi Eliezer the Great','Expository continuation'])
q('q20','6a:20','Rav Nahman bar Yitzhak asks Rav Hiyya bar Avin what is written in the Master of the world’s tefillin.')
claim('20','6a:20','Rav Hiyya bar Avin answers: Who is like Your people Israel, one nation on earth.',['Rav Hiyya bar Avin'])
q('q21','6a:21','Does God praise Himself through Israel’s praise?')
claim('21','6a:21','The answer says yes and reads the reciprocal heemarta/heemirkha verses as God saying Israel made Him one distinguished unit and He will do so for Israel.',['Anonymous exposition of divine speech'])
claim('22israel','6a:22','Israel’s making God a single unit is supported by Shema: the Lord our God, the Lord is one.',['Expository continuation'])
claim('22god','6a:22','God’s making Israel a single unit is supported by Who is like Your people Israel, one nation on earth.',['Expository continuation'])
q('q23','6a:23','Rav Aha son of Rava asks Rav Ashi: that accounts for one compartment; what is in the others?')
claim('24','6a:24','Rav Ashi lists the two who-is-a-great-nation verses, Happy are you Israel, Has God attempted, and To set you high.',['Rav Ashi'],status='List subsequently arranged into compartments')
q('q25','6a:25','Would this yield too many compartments?')
claim('25one','6a:25','The two similar who-is-a-great-nation verses share one compartment.',['Anonymous arrangement'])
claim('25two','6a:25','Happy are you Israel and Who is like Your people Israel share one compartment.',['Anonymous arrangement'])
claim('25three','6a:25','Has God attempted occupies one compartment.',['Anonymous arrangement'])
claim('25four','6a:25','To set you high occupies one compartment.',['Anonymous arrangement'])
claim('1','6b:1','All these passages are written in the arm tefillin.',['Continuation of arrangement'],unc=['Continues 6a25; not a new unrelated claim.'])
claim('2','6b:2','Ravin bar Rav Adda reports Rabbi Yitzhak that God inquires after one who regularly comes to synagogue but misses one day.',['Rabbi Yitzhak'],cond=['Regular synagogue attendance','One day absent'])
claim('3mitzvah','6b:3','If the absentee went for a mitzvah, there is light for him.',['Expository continuation'],cond=['Absence for a mitzvah'])
claim('3ordinary','6b:3','If he went for an ordinary matter, there is no light for him.',['Expository continuation'],cond=['Absence for an ordinary matter'])
q('q4','6b:4','Why is trust in God invoked in this case?')
claim('4','6b:4','The explanation says he should have trusted in God and did not.',['Expository continuation'],cond=['Ordinary-matter absence discussed immediately before'])
claim('5','6b:5','Rabbi Yohanan says God immediately becomes angry on entering the synagogue and not finding ten.',['Rabbi Yohanan'],cond=['God enters synagogue','Fewer than ten found'])
claim('6','6b:6','Rabbi Helbo reports Rav Huna that one who fixes a place for prayer has the God of Abraham as help.',['Rav Huna'],cond=['Fixed place for prayer'])
claim('7','6b:7','At that person’s death people call him humble, pious and a disciple of Abraham.',['Continuation of Rav Huna teaching'],cond=['Person with fixed place for prayer dies'])
q('q8','6b:8','Where do we learn that Abraham fixed a place?')
claim('8','6b:8','Abraham rises to the place where he stood; standing is interpreted as prayer through Phinehas standing and praying.',['Anonymous exposition'])
claim('9out','6b:9','Rabbi Helbo reports Rav Huna forbidding a large stride when leaving synagogue.',['Rav Huna'],cond=['Leaving synagogue'])
claim('9in','6b:9','Abaye limits this to leaving: when entering it is a mitzvah to run, citing pursuing knowledge of God.',['Abaye'],cond=['Entering synagogue'])
claim('10first','6b:10','Rabbi Zeira initially thought sages running to the lecture on Sabbath were profaning Sabbath.',['Rabbi Zeira'],status='Initial view explicitly superseded in narrative')
claim('10rule','6b:10','Rabbi Tanhum reports Rabbi Yehoshua ben Levi that one should always run for a matter of halakhah even on Sabbath.',['Rabbi Yehoshua ben Levi'],cond=['Running for a matter of halakhah','Even Sabbath'])
claim('10change','6b:10','After hearing this teaching, Rabbi Zeira himself ran.',['Rabbi Zeira'],status='Explicit change of conduct after teaching')
for n,holder,text,unc in [(11,'Rabbi Zeira','The reward of the lecture is running.',[]),(12,'Abaye','The reward of the kallah gathering is its crowding.',[]),(13,'Rava','The reward of learning a teaching is reasoning.',[]),(14,'Rav Pappa','The reward of the house of mourning is silence.',[]),(15,'Mar Zutra','The reward of a fast is charity.',[]),(16,'Rav Sheshet','The reward of a eulogy is raising the voice.', ['דלויי is terse; raising the voice is contextual paraphrase.']),(17,'Rav Ashi','The reward of a wedding gathering is words.', ['מילי is terse; specific congratulatory or consolatory wording is not supplied.'])]:claim('reward'+str(n),'6b:'+str(n),text,[holder],unc=unc)
for k,ref,surface,cands,chain in [('17','6a:17','אבין בר רב אדא',['רבי אבין בר רב אדא'],['רבי אבין בר רב אדא','רבי יצחק']),('2','6b:2','רבין בר רב אדא',['רבין בר רב אדא'],['רבין בר רב אדא','רבי יצחק']),('6','6b:6','חלבו אמר רב הונא',['רבי חלבו'],['רבי חלבו','רב הונא']),('9','6b:9','חלבו אמר רב הונא',['רבי חלבו'],['רבי חלבו','רב הונא'])]:att('a'+k,ref,surface,'transmitter',cands,'Reported teaching',chain=chain)
att('a17auth','6a:17','ר יצחק','quoted_authority',['רבי יצחק'],pre+'c17')
att('a19','6a:19',"ר' אליעזר הגדול",'quoted_authority',['רבי אליעזר הגדול'],pre+'c19')
for k,ref,surface,name in [('20q','6a:20','רב נחמן בר יצחק','רב נחמן בר יצחק'),('20a','6a:20','רב חייא בר אבין','רב חייא בר אבין'),('23q','6a:23','רב אחא בריה דרבא','רב אחא בריה דרבא'),('23a','6a:23','רב אשי','רב אשי'),('5','6b:5',"ר' יוחנן",'רבי יוחנן'),('9a','6b:9','אביי','אביי'),('10','6b:10','רבי זירא','רבי זירא'),('11','6b:11',"ר' זירא",'רבי זירא'),('12','6b:12','אביי','אביי'),('13','6b:13','רבא','רבא'),('14','6b:14','רב פפא','רב פפא'),('15','6b:15','מר זוטרא','מר זוטרא'),('16','6b:16','רב ששת','רב ששת'),('17last','6b:17','רב אשי','רב אשי')]:att('a'+k,ref,surface,'speaker',[name],'Local utterance')
att('a10chain','6b:10','רבי תנחום א"ר יהושע בן לוי','quoted_authority',['רבי יהושע בן לוי'],pre+'c10rule',chain=['רבי תנחום','רבי יהושע בן לוי'])
for k,ref,a,b,rel in [('17','6a:17','c17','q17','answer'),('18r','6a:18','c18right','c17','support'),('18a','6a:18','c18arm','c17','support'),('19','6a:19','c19','q19','answer'),('20','6a:20','c20','q20','answer'),('21','6a:21','c21','q21','answer'),('22i','6a:22','c22israel','c21','support'),('22g','6a:22','c22god','c21','support'),('24','6a:24','c24','q23','answer'),('3m','6b:3','c3mitzvah','c2','qualification'),('3o','6b:3','c3ordinary','c2','qualification'),('4','6b:4','c4','q4','answer'),('8','6b:8','c8','q8','answer'),('8s','6b:8','c8','c6','support'),('9','6b:9','c9in','c9out','qualification'),('10','6b:10','c10rule','c10first','objection'),('10c','6b:10','c10change','c10first','correction')]:edge('e'+k,ref,a,b,rel)
for k in ['one','two','three','four']:edge('e25'+k,'6a:25','c25'+k,'q25','answer')
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local aggadic and prayer teachings; alternative stages and conditional distinctions preserved, not external legal adjudication.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read through6b37; reread core6a17–6b17 for divine-tefillin content/compartments,6b1 continuation, absence reasons, fixed place, entering/leaving distinction, Zeira retraction and seven distinct reward sayings. Completed '+layer+' pass; no additional record where none listed.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch03_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch03_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch03_receipt.json',r.encoded(out));print(r.encoded(out).decode())
