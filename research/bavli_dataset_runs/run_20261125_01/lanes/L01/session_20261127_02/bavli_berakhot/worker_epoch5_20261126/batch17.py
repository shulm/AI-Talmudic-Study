from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.shema_posture.20261126e5.'
assert r.sha(r.encoded(state))=='76dce5b59989d29465778977b9949c490dd00a6313bc3fe60c467f1294b40255'
refs=['10b:'+str(i) for i in range(37,42)]+['11a:'+str(i) for i in range(1,24)]
for k,rr,title in [('mishna',refs[:5],'Beit Shammai and Beit Hillel on Shema posture'),('derivation',refs[5:19],'Posture versus time and exemptions for mitzvah engagement'),('reclining',refs[19:23],'Deliberate posture change and misleading students'),('validity',refs[23:],'Three evaluations of acting like Beit Shammai')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Mishnah Beit Shammai','Mishnah Beit Hillel','Mishnah rationale','Rabbi Tarfon narrative','Mishnah response']+[('Anonymous discussion' if n not in [6,10,15,16,19,20,21,22,23] else {6:'Rav Pappa',10:'Anonymous objection citing Rabbi Abba bar Zavda reporting Rav',15:'Baraita and Rabbi Yishmael/Rabbi Eleazar ben Azariah narrative',16:'Rabbi Yishmael',19:'Rav Yehezkel',20:'Rav Yosef quoting sukkah Mishnah',21:'Beit Hillel’s account of visit',22:'Beit Shammai’s counteraccount',23:'Rav Nahman bar Yitzhak'}[n]) for n in range(1,24)]
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Mishnah or legal argument',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('37evening','10b:37','Beit Shammai require reclining to recite in the evening.',['Beit Shammai'],cond=['Evening Shema'])
claim('37morning','10b:37','They require standing in the morning, reading when lying and rising as posture.',['Beit Shammai'],cond=['Morning Shema'])
claim('38','10b:38','Beit Hillel permit each person to read in the usual manner, citing walking on the way.',['Beit Hillel'])
q('q39','10b:39','Why then does the verse say when lying and rising?')
claim('39','10b:39','Beit Hillel interpret these as times when people lie down and rise.',['Beit Hillel'])
claim('40','10b:40','Rabbi Tarfon recounts reclining on a journey to follow Beit Shammai and endangering himself because of robbers.',['Rabbi Tarfon'],status='Narrated conduct')
claim('41','10b:41','The reply says he deserved liability for his life because he transgressed Beit Hillel’s words.',['Mishnah respondents'])
q('q1','11a:1','Why do Beit Shammai not accept Beit Hillel’s explanation?')
claim('2','11a:2','They argue the verse could say morning/evening; lying/rising instead requires literal postures at those times.',['Beit Shammai as represented in discussion'])
q('q3','11a:3','What do Beit Shammai do with walking on the way?')
claim('4engaged','11a:4','The baraita reads sitting in your house as excluding one engaged in a mitzvah.',['Cited baraita'])
claim('4groom','11a:4','Walking on your way excludes a bridegroom.',['Cited baraita'])
claim('4virgin','11a:4','One marrying a virgin is therefore exempt, while one marrying a widow is obligated.',['Cited baraita'])
q('q5','11a:5','How is this exclusion indicated?')
claim('6','11a:6','Rav Pappa analogizes to a way undertaken voluntarily: the obligation applies to voluntary matters.',['Rav Pappa'])
q('q7','11a:7','Could the verse not concern a journey for a mitzvah yet still require recitation?')
claim('7','11a:7','The possessive your sitting and your walking, rather than sitting/walking alone, marks personal activity as obligated and mitzvah activity as exempt.',['Anonymous Gemara'])
q('q8','11a:8','If so, why is one marrying a widow not exempt too?')
claim('9','11a:9','The answer distinguishes the preoccupied groom from the one not preoccupied.',['Anonymous Gemara'])
q('q10','11a:10','If preoccupation suffices, would even one whose ship sank be exempt, contrary to the mourner’s obligations?')
claim('10rav','11a:10','Rav via Rabbi Abba bar Zavda obligates a mourner in all commandments except tefillin, which are called splendor.',['Rav'],cond=['Mourner'],status='Quoted counterexample to unrestricted preoccupation exemption')
claim('11','11a:11','The answer distinguishes mitzvah-related preoccupation from voluntary-matter preoccupation.',['Anonymous Gemara'])
q('q12','11a:12','What is the corresponding Beit Shammai explanation?')
claim('13','11a:13','They require the phrase to exclude mitzvah messengers.',['Beit Shammai as represented in discussion'])
claim('14','11a:14','Beit Hillel say one also learns incidentally that Shema can be read while on the way.',['Beit Hillel as represented in discussion'])
claim('15forms','11a:15','The baraita allows standing, sitting, reclining, walking and working while reciting according to Beit Hillel.',['Beit Hillel in baraita'])
claim('15change','11a:15','Rabbi Yishmael was reclining and Rabbi Eleazar ben Azariah upright; at Shema time Eleazar reclined and Yishmael straightened.',['Narrator'],status='Narrative conduct')
claim('15challenge','11a:15','Rabbi Eleazar challenges Yishmael’s contrary posture change with the beard parable and observes his reversal when Eleazar reclined.',['Rabbi Eleazar ben Azariah'])
claim('16hillel','11a:16','Yishmael says he followed Beit Hillel while Eleazar followed Beit Shammai.',['Rabbi Yishmael'])
claim('16students','11a:16','He adds concern that students might see and establish this as law for generations.',['Rabbi Yishmael'])
q('q17','11a:17','Why the additional reason?')
claim('18','11a:18','Although Beit Hillel allow reclining, that is when already reclining; a deliberate change from upright at this moment suggests Beit Shammai and may mislead students.',['Anonymous exposition of Yishmael’s concern'],cond=['Previously upright and newly reclines at Shema time'])
claim('19shammai','11a:19','Rav Yehezkel teaches that one who acts like Beit Shammai has acted validly.',['Rav Yehezkel'])
claim('19hillel','11a:19','He likewise validates acting like Beit Hillel.',['Rav Yehezkel'])
claim('20','11a:20','Rav Yosef says acting like Beit Shammai accomplishes nothing.',['Rav Yosef'])
claim('20sukkah','11a:20','His cited Mishnah has Beit Shammai invalidate and Beit Hillel validate sitting with head and most of body in a sukkah but table in the house.',['Beit Shammai','Beit Hillel'],status='Quoted analogical dispute, two opposed group positions')
claim('21','11a:21','Beit Hillel cite elders of both groups visiting Rabbi Yohanan ben ha-Horanit in that arrangement without saying anything.',['Beit Hillel'],status='Contested account in argument')
claim('22','11a:22','Beit Shammai reply that the elders did say: if this was your practice, you never fulfilled sukkah.',['Beit Shammai'],status='Counteraccount, not harmonized silently with prior account')
claim('23','11a:23','Rav Nahman bar Yitzhak says acting like Beit Shammai incurs death liability, citing Tarfon’s incident and the Mishnah’s response.',['Rav Nahman bar Yitzhak'])
for k,ref,surface,names in [('37','10b:37','בית שמאי',['בית שמאי']),('38','10b:38','בית הלל',['בית הלל']),('40','10b:40','ר טרפון',['רבי טרפון']),('6','11a:6','רב פפא',['רב פפא']),('15y','11a:15','רבי ישמעאל',['רבי ישמעאל']),('15e','11a:15',"ר' אלעזר בן עזריה",['רבי אלעזר בן עזריה']),('19','11a:19','רב יחזקאל',['רב יחזקאל']),('20','11a:20','רב יוסף',['רב יוסף']),('23','11a:23','רב נחמן בר יצחק',['רב נחמן בר יצחק'])]:att('a'+k,ref,surface,'speaker',names,'Local legal stance or dialogue')
att('a10','11a:10','ר אבא בר זבדא אמר רב','transmitter',['רבי אבא בר זבדא'],pre+'c10rav',chain=['רבי אבא בר זבדא','רב'])
for k,ref,a,b,rel in [('38','10b:38','c38','c37evening','distinction'),('39','10b:39','c39','q39','answer'),('41','10b:41','c41','c40','objection'),('2','11a:2','c2','q1','answer'),('4','11a:4','c4groom','q3','answer'),('6','11a:6','c6','q5','answer'),('7','11a:7','c7','q7','answer'),('9','11a:9','c9','q8','answer'),('10','11a:10','c10rav','c9','objection'),('11','11a:11','c11','q10','answer'),('13','11a:13','c13','q12','answer'),('14','11a:14','c14','c13','distinction'),('16','11a:16','c16hillel','c15challenge','answer'),('16s','11a:16','c16students','c15challenge','answer'),('18','11a:18','c18','q17','answer'),('20','11a:20','c20','c19shammai','objection'),('20s','11a:20','c20sukkah','c20','support'),('22','11a:22','c22','c21','objection'),('22s','11a:22','c22','c20','support'),('23','11a:23','c23','c19shammai','objection')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local posture dispute, exemptions and evaluation of following Beit Shammai. Preserve contested narratives and distinguish validity/no-effect/death-liability positions; no inferred binary reduction.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read10b37–11b23; reread core10b37–11a23 for both Mishnah postures and timing explanation, engagement/preoccupation distinctions, mourner counterexample, deliberate reclining and student concern, three amoraic evaluations, and contested elders’ visit. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch17_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch17_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch17_receipt.json',r.encoded(out));print(r.encoded(out).decode())
