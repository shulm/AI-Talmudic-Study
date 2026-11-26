from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.conduct.20261126e5.'
assert r.sha(r.encoded(state))=='d3a207e44527805bb0c0b2dc0deb89f9949956d50bfd6a857a8eb01c2c509c3f'
refs=['6b:'+str(i) for i in range(18,38)]
for k,ns,title in [('behind',range(18,21),'Prayer behind synagogue and orientation'),('value',range(21,26),'Lofty things and dependence on others'),('times',range(26,29),'Care with afternoon, evening and morning prayer'),('wedding',range(29,34),'Gladdening bridegroom and its rewards'),('fear',range(34,37),'Fear of Heaven and the purpose of humanity'),('greeting',range(37,38),'Initiating and returning greetings')]:add('s'+k,'structure',['6b:'+str(i) for i in ns],dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices={18:'Rav Huna',19:'Abaye',20:'Narrator and Elijah disguised as an Arab',21:'Alternative reports of questioner and respondent',22:'Respondent in the alternative dialogue',23:'Rabbi Yohanan and Rabbi Eleazar jointly',24:'Anonymous question; Rav Dimi',25:'Rabbi Ammi and Rabbi Assi jointly',26:'Rabbi Helbo reporting Rav Huna',27:'Expository continuation',28:'Rabbi Yohanan; Rav Nahman bar Yitzhak',29:'Rabbi Helbo reporting Rav Huna',30:'Anonymous question; Rabbi Yehoshua ben Levi',31:'Anonymous objection',32:'Anonymous answer',33:'Rabbi Abbahu; Rav Nahman bar Yitzhak',34:'Rabbi Helbo reporting Rav Huna',35:'Anonymous question; Rabbi Eleazar quoting God',36:'Rabbi Abba bar Kahana; Rabbi Shimon ben Azzai or Rabbi Shimon ben Zoma',37:'Rabbi Helbo reporting Rav Huna'}
for n in range(18,38):add('u'+str(n),'utterances',['6b:'+str(n)],dict(textual_voice=voices[n],discourse_role='Local teaching, dialogue or narrative',composition='composite'))
def claim(k,n,text,holders,cond=(),status='Reported locally',unc=()):
 ref='6b:'+str(n);c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('18',18,'Rav Huna calls one praying behind the synagogue wicked, citing the wicked walking around.',['Rav Huna'],cond=['Praying behind synagogue'],unc=['Orientation is qualified by Abaye in6b19.'])
claim('19away',19,'Abaye limits the criticism to one who does not turn toward the synagogue.',['Abaye'],cond=['Behind synagogue','Not facing synagogue'])
claim('19toward',19,'If he turns toward the synagogue, there is no objection.',['Abaye'],cond=['Behind synagogue','Facing synagogue'])
claim('20',20,'The narrative describes a man praying behind the synagogue without facing it. Elijah appears as an Arab, rebukes how he stands before his Master, draws a sword and kills him.',['Anonymous narrator','Elijah as dialogue speaker'],status='Narrative, not an independent legal permission')
q('q21','6b:21','What does kerum zullut li-vnei adam mean?')
claim('22',22,'The respondent explains it as things standing at the height of the world which people treat lightly.',['Rav Bibi bar Abaye','Rav Nahman bar Yitzhak'],status='Answer with alternative dialogue attribution',unc=['Version1 unnamed scholar asks Rav Bibi; version2 Rav Bibi asks Rav Nahman bar Yitzhak. Respondent varies with version; no joint assertion.','The terse answer does not expressly name prayer.'])
claim('23',23,'Rabbi Yohanan and Rabbi Eleazar jointly say one needing other people has a face changing like kerum.',['Rabbi Yohanan','Rabbi Eleazar'],cond=['Needs support from other people'])
q('q24','6b:24','What is kerum?')
claim('24',24,'Rav Dimi reports a bird in the cities of the sea named kerum whose colors change when the sun shines.',['Rav Dimi'])
claim('25',25,'Rabbi Ammi and Rabbi Assi jointly compare dependence on others to judgment by both fire and water.',['Rabbi Ammi','Rabbi Assi'],cond=['Needs other people; carried from prior discussion'])
claim('26',26,'Rabbi Helbo reports Rav Huna urging care with afternoon prayer, since Elijah was answered at the afternoon offering.',['Rav Huna'])
claim('27fire',27,'Elijah’s first answer me is interpreted as asking for fire to descend from heaven.',['Expository continuation'])
claim('27magic',27,'The second answer me is interpreted as asking that people not call it sorcery.',['Expository continuation'])
claim('28evening',28,'Rabbi Yohanan adds care with evening prayer, citing prayer as incense and uplifted hands as the evening offering.',['Rabbi Yohanan'],status='Additional prayer time, not exclusion of afternoon')
claim('28morning',28,'Rav Nahman bar Yitzhak adds morning prayer, citing hearing and arranging prayer in the morning.',['Rav Nahman bar Yitzhak'],status='Additional prayer time')
claim('29',29,'Rabbi Helbo reports Rav Huna that one benefiting from a bridegroom’s feast without gladdening him transgresses five voices.',['Rav Huna'],cond=['Benefits from wedding feast','Does not gladden bridegroom'])
q('q30','6b:30','If he gladdens him, what is his reward?')
claim('30',30,'Rabbi Yehoshua ben Levi says he merits Torah, which was given with five voices.',['Rabbi Yehoshua ben Levi'],cond=['Gladdens bridegroom'])
q('q31','6b:31','Does the verse all the people saw the voices introduce additional voices against the five count?')
claim('32',32,'The answer identifies those as the voices before the giving of Torah.',['Anonymous Gemara'],status='Resolution of count objection')
claim('33thanks',33,'Rabbi Abbahu says it is as if he offered a thanksgiving sacrifice, citing bringing thanksgiving to God’s house.',['Rabbi Abbahu'],cond=['Gladdens bridegroom'])
claim('33build',33,'Rav Nahman bar Yitzhak says it is as if he built one of Jerusalem’s ruins, citing restoring the land.',['Rav Nahman bar Yitzhak'],cond=['Gladdens bridegroom'])
claim('34',34,'Rabbi Helbo reports Rav Huna that the words of one with fear of Heaven are heard.',['Rav Huna'],cond=['Has fear of Heaven'])
q('q35','6b:35','What does for this is all of man mean?')
claim('35',35,'Rabbi Eleazar represents God as saying the whole world was created only for this person.',['Rabbi Eleazar'],cond=['Person with fear of Heaven from prior teaching'])
claim('36equal',36,'Rabbi Abba bar Kahana says this person is equivalent to the whole world.',['Rabbi Abba bar Kahana'],cond=['Person with fear of Heaven'])
claim('36company',36,'Rabbi Shimon ben Azzai, alternatively Rabbi Shimon ben Zoma, says the whole world was created only to accompany this person.',['Rabbi Shimon ben Azzai','Rabbi Shimon ben Zoma'],cond=['Person with fear of Heaven'],status='Unresolved alternative attribution')
claim('37first',37,'Rabbi Helbo reports Rav Huna that one knowing a friend regularly greets him should greet first, citing seeking peace.',['Rav Huna'],cond=['Knows friend normally greets him'])
claim('37return',37,'If greeted and failing to return the greeting, he is called a robber, citing robbery of the poor.',['Rav Huna'],cond=['Receives greeting','Fails to return it'])
for k,n,surface,names in [('18',18,'רב הונא',['רב הונא']),('19',19,'אביי',['אביי']),('23',23,"ר' יוחנן ור' אלעזר",['רבי יוחנן','רבי אלעזר']),('24',24,'רב דימי',['רב דימי']),('25',25,"ר' אמי ור' אסי",['רבי אמי','רבי אסי']),('28y',28,"ר' יוחנן",['רבי יוחנן']),('28n',28,'רב נחמן בר יצחק',['רב נחמן בר יצחק']),('30',30,'רבי יהושע בן לוי',['רבי יהושע בן לוי']),('33a',33,'רבי אבהו',['רבי אבהו']),('33n',33,'רב נחמן בר יצחק',['רב נחמן בר יצחק']),('35',35,'ר אלעזר',['רבי אלעזר']),('36a',36,'רבי אבא בר כהנא',['רבי אבא בר כהנא'])]:att('a'+k,'6b:'+str(n),surface,'speaker',names,'Local teaching')
att('a21','6b:21','רב ביבי לרב נחמן בר יצחק','speaker',['Unnamed scholar to Rav Bibi bar Abaye','Rav Bibi bar Abaye to Rav Nahman bar Yitzhak'],'Alternative dialogue pairings',unc=['Preserve the two complete pairings, not independent candidate mixing.'])
att('a36','6b:36',"ר' שמעון בן עזאי אומר ואמרי לה ר' שמעון בן זומא",'speaker',['רבי שמעון בן עזאי','רבי שמעון בן זומא'],pre+'c36company',unc=['Explicit alternative attribution, unresolved.'])
for n in [26,29,34,37]:att('a'+str(n),'6b:'+str(n),'חלבו אמר רב הונא','transmitter',['רבי חלבו'],'Reported Rav Huna teaching',chain=['רבי חלבו','רב הונא'])
for k,n,a,b,rel in [('19a',19,'c19away','c18','qualification'),('19b',19,'c19toward','c18','qualification'),('22',22,'c22','q21','answer'),('24',24,'c24','q24','answer'),('24s',24,'c24','c23','support'),('27f',27,'c27fire','c26','support'),('27m',27,'c27magic','c26','support'),('28e',28,'c28evening','c26','qualification'),('28m',28,'c28morning','c26','qualification'),('30',30,'c30','q30','answer'),('31',31,'q31','c30','objection'),('32',32,'c32','q31','answer'),('33t',33,'c33thanks','q30','answer'),('33b',33,'c33build','q30','answer'),('35',35,'c35','q35','answer'),('36e',36,'c36equal','q35','answer'),('36c',36,'c36company','q35','answer')]:edge('e'+k,'6b:'+str(n),a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local moral, narrative and exegetical teachings. Additional reward/time descriptions do not by themselves establish mutually exclusive disputes.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read6b18–7a36; reread core6b18–37 for orientation exception, narrative status, complete alternative dialogue pairings, joint assertions, additive prayer times/rewards, voices objection resolution, Ben Azzai/Ben Zoma alternative, and two greeting conditions. Completed '+layer+' pass; no additional record where none listed.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch04_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch04_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch04_receipt.json',r.encoded(out));print(r.encoded(out).decode())
