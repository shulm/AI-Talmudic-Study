from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.morning_prayer.20261126e5.'
assert r.sha(r.encoded(state))=='8535f81c096e1e98ea23c7db32f4bb12e04fbfb931c9c163916bee22486db78a'
refs=['9b:'+str(i) for i in range(9,32)]+['10a:1']
for k,rr,title in [('mishna',refs[:2],'Morning Shema onset and deadlines'),('recognition',refs[2:7],'Recognition tests and vatikin practice'),('adjacency',refs[7:16],'Redemption adjacent to prayer and intervening verses'),('psalms',refs[16:],'Placement of concluding verse and psalm enumeration')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices={9:'Mishnah: anonymous teaching, Rabbi Eliezer and Rabbi Yehoshua',10:'Mishnah continuation',11:'Anonymous clarification',12:'Baraita: Rabbi Meir, Rabbi Akiva and Others',13:'Rav Huna; Abaye citing Rabbi Yohanan',14:'Supporting baraita',15:'Rabbi Zeira',16:'Rabbi Yose ben Elyakim in name of Jerusalem holy congregation',17:'Rabbi Zeira, anonymous respondent and Rabbi Yohanan quotation',18:'Rabbi Ilaa to Ulla about Rav Berona',19:'Anonymous objection citing Rabbi Yohanan',20:'Rabbi Eleazar',21:'Anonymous objection citing Rabbi Yohanan',22:'Rabbi Eleazar revised answer',23:'Rav Ashi',24:'Supporting analogy',25:'Anonymous question',26:'Rabbi Yehuda son of Rabbi Shimon ben Pazi',27:'Anonymous counting objection',28:'Anonymous answer',29:'Rabbi Yehuda son of Rabbi Shimon ben Pazi',30:'Anonymous count and inference',31:'Rabbi Shmuel bar Nahmani reporting Rabbi Yohanan'}
for n in range(9,32):add('u'+str(n),'utterances',['9b:'+str(n)],dict(textual_voice=voices[n],discourse_role='Mishnah' if n<11 else 'Legal or exegetical discussion',composition='composite'))
add('u10a1','utterances',['10a:1'],dict(textual_voice='Completion of Rabbi Yohanan teaching transmitted by Rabbi Shmuel bar Nahmani',discourse_role='Psalm framing exposition',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
q('q9','9b:9','From when is morning Shema recited?')
claim('9bluewhite','9b:9','The Mishnah’s first onset is distinguishing blue from white.',['Anonymous Mishnah'])
claim('9bluegreen','9b:9','Rabbi Eliezer gives distinguishing blue from leek-green.',['Rabbi Eliezer'])
claim('9sunrise','9b:9','The Mishnah says to finish by sunrise.',['Mishnah deadline clause'],unc=['Printed parenthetical וגומרה follows Rabbi Eliezer; do not infer a fresh named holder beyond the local clause.'])
claim('9three','9b:9','Rabbi Yehoshua permits until three hours because kings rise then.',['Rabbi Yehoshua'])
claim('10','9b:10','Reciting thereafter does not lose the value of reading Torah.',['Mishnah continuation'],cond=['Recitation after stated time'],unc=['Not a claim of timely Shema fulfillment.'])
q('q11','9b:11','What is meant by distinguishing blue and white?')
claim('11hyp','9b:11','Separate white and blue bundles cannot be intended, since these are distinguishable at night.',['Anonymous Gemara'],status='Rejected interpretation')
claim('11','9b:11','The answer is blue within it from white within it.',['Anonymous Gemara'],unc=['The object referred to by שבה is not explicitly named in this sentence; no external identification imported.'])
claim('12wolf','9b:12','Rabbi Meir gives recognition between wolf and dog.',['Rabbi Meir'])
claim('12donkey','9b:12','Rabbi Akiva gives recognition between donkey and wild ass.',['Rabbi Akiva'])
claim('12friend','9b:12','Others give seeing and recognizing one’s fellow four cubits away.',['Others'])
claim('13huna','9b:13','Rav Huna rules like Others.',['Rav Huna'],status='Explicit halakhic report')
claim('13tefillin','9b:13','Abaye applies Others to tefillin.',['Abaye'])
claim('13shema','9b:13','For Shema Abaye gives the vatikin practice, with Yohanan reporting their completion at sunrise.',['Abaye','Rabbi Yohanan as cited authority'])
claim('14','9b:14','The supporting baraita says vatikin completed Shema at sunrise to connect redemption to prayer and pray in daytime.',['Unnamed baraita'])
q('q15','9b:15','Rabbi Zeira asks which verse supports this.')
claim('15','9b:15','He cites fearing You with the sun and before the moon through generations.',['Rabbi Zeira'])
claim('16','9b:16','Rabbi Yose ben Elyakim testifies in the name of Jerusalem’s holy congregation that one adjoining redemption to prayer is not harmed all day.',['Holy congregation of Jerusalem'],cond=['Adjoins redemption to prayer'])
q('q17','9b:17','Rabbi Zeira objects that he adjoined them and was harmed; the respondent asks what harm occurred.')
claim('17harm','9b:17','The reported harm was bringing myrtle to the royal house.',['Rabbi Zeira’s case in dialogue'])
claim('17value','9b:17','The reply says he should even have paid to see the king’s face.',['Anonymous respondent'],status='Rejects characterization as harm')
claim('17kings','9b:17','Rabbi Yohanan urges running to see Israelite and even gentile kings, so that if merited one may distinguish between them.',['Rabbi Yohanan'])
claim('18request','9b:18','Rabbi Ilaa asks Ulla to greet his brother Rav Berona before the whole group, calling him great and joyful in mitzvot.',['Rabbi Ilaa'])
claim('18joy','9b:18','He recounts Rav Berona once adjoining redemption to prayer and smiling all day.',['Rabbi Ilaa’s report'])
q('q19','9b:19','How can they be adjoining when Yohanan says to begin with Lord open my lips and end with May the words of my mouth be acceptable?')
claim('19verses','9b:19','Rabbi Yohanan prescribes the opening and closing verses of prayer.',['Rabbi Yohanan'])
claim('20','9b:20','Rabbi Eleazar first locates the verse instruction in evening prayer.',['Rabbi Eleazar'],status='Initial answer rejected by continuation')
claim('21','9b:21','Rabbi Yohanan also promises the world to come to one adjoining evening redemption to evening prayer.',['Rabbi Yohanan'],status='Objection to evening-only solution')
claim('22','9b:22','Rabbi Eleazar revises the answer to afternoon prayer.',['Rabbi Eleazar'],status='Explicit revised answer')
claim('23','9b:23','Rav Ashi permits applying it to all prayers: since sages fixed the verse in prayer, it is like an extended prayer.',['Rav Ashi'],status='Alternative inclusive resolution')
claim('24hash','9b:24','The evening Hashkivenu blessing is analogously an extended redemption because sages instituted it.',['Argument supporting Rav Ashi'])
claim('24verse','9b:24','Likewise the fixed opening verse is an extended prayer.',['Argument supporting Rav Ashi'])
q('q25','9b:25','If May the words be acceptable can refer to past or intended words, why did sages place it after eighteen blessings rather than before?')
claim('26','9b:26','Rabbi Yehuda son of Rabbi Shimon ben Pazi says David said it only after eighteen psalm sections, so sages fixed it after eighteen blessings.',['Rabbi Yehuda son of Rabbi Shimon ben Pazi'])
q('q27','9b:27','Are these eighteen sections not nineteen?')
claim('28','9b:28','Ashrei ha-Ish and Lamah Ragshu Goyim are one section.',['Anonymous Gemara'])
claim('29','9b:29','Rabbi Yehuda son of Rabbi Shimon ben Pazi says David spoke 103 sections before Hallelujah, until seeing the fall of the wicked.',['Rabbi Yehuda son of Rabbi Shimon ben Pazi'])
q('q30','9b:30','Are these 103 not 104?')
claim('30','9b:30','The count again implies Ashrei ha-Ish and Lamah Ragshu Goyim are one section.',['Anonymous Gemara'])
claim('10a1','10a:1','Rabbi Yohanan via Rabbi Shmuel bar Nahmani says David framed beloved sections with ashrei, illustrated by the beginning of Psalm1 and end of Psalm2.',['Rabbi Yohanan'],unc=['Speaker prefix is9b31 and predicate10a1; retain folio continuation.'])
for k,ref,surface,name in [('9e','9b:9',"ר' אליעזר",'רבי אליעזר'),('9y','9b:9',"ר' יהושע",'רבי יהושע'),('12m','9b:12','רבי מאיר','רבי מאיר'),('12a','9b:12','ר"ע','רבי עקיבא'),('12o','9b:12','אחרים','אחרים'),('13h','9b:13','רב הונא','רב הונא'),('13a','9b:13','אביי','אביי'),('13y','9b:13',"ר' יוחנן",'רבי יוחנן'),('15','9b:15','ר זירא','רבי זירא'),('17','9b:17','ר זירא','רבי זירא'),('17y','9b:17',"ר יוחנן",'רבי יוחנן'),('18','9b:18','רבי אלעא','רבי אלעא'),('20','9b:20',"ר' אלעזר",'רבי אלעזר'),('23','9b:23','רב אשי','רב אשי'),('26','9b:26',"ר יהודה בריה דר' שמעון בן פזי",'רבי יהודה בריה דרבי שמעון בן פזי'),('29','9b:29',"ר' יהודה בריה דרבי שמעון בן פזי",'רבי יהודה בריה דרבי שמעון בן פזי')]:
 assert surface in by[ref]['text'],(k,ref,surface)
 att('a'+k,ref,surface,'speaker',[name],'Local teaching or dialogue')
att('a16','9b:16','ר"י בן אליקים','transmitter',['רבי יוסי בן אליקים'],'Testimony of holy congregation',chain=['רבי יוסי בן אליקים','קהלא קדישא דבירושלים'],unc=['Printed abbreviation ר"י retained in evidence; expansion provisional.'])
att('a31','9b:31',"ר' שמואל בר נחמני אמר רבי יוחנן",'transmitter',['רבי שמואל בר נחמני'],pre+'c10a1',chain=['רבי שמואל בר נחמני','רבי יוחנן'])
for k,ref,a,b,rel in [('9a','9b:9','c9bluewhite','q9','answer'),('9b','9b:9','c9bluegreen','q9','answer'),('9t','9b:9','c9three','c9sunrise','distinction'),('11','9b:11','c11','q11','answer'),('11h','9b:11','c11hyp','q11','answer'),('13t','9b:13','c13tefillin','c13huna','qualification'),('13s','9b:13','c13shema','c13huna','qualification'),('14','9b:14','c14','c13shema','support'),('15','9b:15','c15','q15','answer'),('17','9b:17','q17','c16','objection'),('17v','9b:17','c17value','c17harm','objection'),('17k','9b:17','c17kings','c17value','support'),('20','9b:20','c20','q19','answer'),('21','9b:21','c21','c20','objection'),('22','9b:22','c22','c20','correction'),('22a','9b:22','c22','q19','answer'),('23','9b:23','c23','q19','answer'),('24','9b:24','c24hash','c23','support'),('24v','9b:24','c24verse','c23','support'),('26','9b:26','c26','q25','answer'),('27','9b:27','q27','c26','objection'),('28','9b:28','c28','q27','answer'),('30q','9b:30','q30','c29','objection'),('30','9b:30','c30','q30','answer'),('10a1','10a:1','c10a1','c30','support')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local morning Shema and prayer discussion; preserve initial/revised resolutions, narrative harm dispute, Mishnah wording uncertainty and combined psalm-count logic.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read9b9–10a32; reread core9b9–10a1 for all recognition tests and deadlines, tefillin/Shema split, vatikin purpose, rejected harm characterization, rejected evening and revised afternoon answer, Rav Ashi inclusive resolution, both psalm counts, and9b31 speaker continuation. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch13_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch13_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch13_receipt.json',r.encoded(out));print(r.encoded(out).decode())
