from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.prayer_mercy.20261126e5.'
assert r.sha(r.encoded(state))=='6cc8647a5cb642c7cb23e4f0ef2ad0ee2c18bcc3bb8be30a20e13f210f450d83'
refs=['12a:'+str(i) for i in range(23,29)]+['12b:'+str(i) for i in range(1,14)]
for k,rr,title in [('truth',refs[:1],'Morning truth and evening faithfulness'),('bow',refs[1:7],'Bowing at blessed and rising at divine name'),('king',refs[7:11],'Ten days’ royal blessing formulas'),('friend',refs[11:14],'Prayer for one’s fellow and scholar'),('shame',refs[14:],'Shame for sin and Saul’s forgiveness')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Rabbah bar Hinana the elder reporting Rav','Same chain','Shmuel explaining Rav','Anonymous objection','Anonymous reply','Shmuel to Hiyya son of Rav','Narrator about Rav Sheshet','Rabbah bar Hinana the elder reporting Rav','Rabbi Eleazar','Anonymous question','Rav Yosef and Rabbah; anonymous ruling','Rabbah bar Hinana the elder reporting Rav','Rava','Anonymous proof question and rejected candidate','Same chain reporting Rav','Anonymous objection and Saul narrative proof','Explanation of omission','Proof question and Rabbi Yohanan citation','Sages’ alternative proof']
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Reported rule or argument',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('23','12a:23','Rav via Rabbah bar Hinana the elder says one not saying Emet ve-Yatziv in morning and Emet ve-Emunah in evening has not fulfilled the obligation, citing morning kindness and night faithfulness.',['Rav'])
claim('24bow','12a:24','Rav says to bow at Barukh.',['Rav'])
claim('24rise','12a:24','He says to rise at the divine name.',['Rav'])
q('q25','12a:25','Shmuel asks Rav’s reason.')
claim('25','12a:25','Shmuel cites the Lord straightens the bent.',['Shmuel'],status='Explanation supporting Rav, not dispute')
q('q26','12a:26','Does he was bowed before My name contradict rising at the name?')
claim('27','12a:27','The reply distinguishes before My name from at My name.',['Anonymous Gemara'])
claim('28','12a:28','Shmuel tells Hiyya son of Rav the fine teaching of his father: bow at Barukh and rise at the name.',['Shmuel transmitting Rav'],status='Repeated transmission, not independent opposing ruling')
claim('1','12b:1','Rav Sheshet bowed like a branch and rose like a snake.',['Anonymous narrator'],status='Narrated physical manner',unc=['Comparisons כחיזרא/כחיויא retained; finer movement mechanics not inferred.'])
claim('2year','12b:2','Rav via Rabbah bar Hinana the elder prescribes Ha-El ha-Kadosh and king who loves righteousness and judgment during the year.',['Rav'],cond=['Outside ten days'])
claim('2ten','12b:2','During the ten days between Rosh Hashanah and Yom Kippur he prescribes Ha-Melekh ha-Kadosh and Ha-Melekh ha-Mishpat.',['Rav'],cond=['Ten days from Rosh Hashanah to Yom Kippur'])
claim('3','12b:3','Rabbi Eleazar validates even Ha-El ha-Kadosh, reading Isaiah’s exaltation in judgment as those ten days while it still says the holy God.',['Rabbi Eleazar'],cond=['Ten-day period','Said Ha-El ha-Kadosh'],status='Validity alternative; does not itself specify judgment blessing')
q('q4','12b:4','What was the resolution?')
claim('5yosef','12b:5','Rav Yosef gives Ha-El ha-Kadosh and king who loves righteousness and judgment.',['Rav Yosef'],cond=['Ten-day case under discussion'])
claim('5rabbah','12b:5','Rabbah gives Ha-Melekh ha-Kadosh and Ha-Melekh ha-Mishpat.',['Rabbah'],cond=['Ten-day case under discussion'])
claim('5law','12b:5','The discussion explicitly rules like Rabbah.',['Anonymous Gemara'],status='Explicit local halakhic ruling')
claim('6','12b:6','Rav says one able to seek mercy for a fellow who does not do so is called a sinner, citing Samuel’s refusal to sin by ceasing prayer for the people.',['Rav'],cond=['Able to pray for fellow','Does not pray'])
claim('7','12b:7','Rava says if he is a Torah scholar, one must make oneself ill over him.',['Rava'],cond=['Fellow is a Torah scholar, contextual reading'],unc=['The brief אם ת"ח הוא depends on the preceding fellow-prayer context; no unrelated scholar identity invented.'])
q('q8','12b:8','What supports the heightened requirement?')
claim('8rejected','12b:8','The Saul verse about nobody being ill over him is insufficient because a king might be different.',['Anonymous Gemara'],status='Rejected proof')
claim('8proof','12b:8','The proof instead comes from when they were sick, my clothing was sackcloth.',['Anonymous Gemara'])
claim('9','12b:9','Rav says a person committing a transgression and ashamed of it is forgiven all sins, initially citing Ezekiel’s remembrance, shame and forgiveness.',['Rav'],cond=['Committed transgression','Ashamed of it'])
claim('10reject','12b:10','The discussion rejects relying on that verse alone because the community might be different.',['Anonymous Gemara'],status='Proof scope objection, not rejection of Rav’s claim')
claim('10saul','12b:10','It instead cites Saul mentioning no answer by prophets or dreams but omitting Urim and Tummim.',['Anonymous Gemara citing narrative'])
claim('11','12b:11','The omission is explained by his destruction of Nob, the priestly city.',['Anonymous Gemara'],status='Explanation of ashamed omission')
q('q12','12b:12','How do we know he was forgiven from Heaven?')
claim('12with','12b:12','Samuel’s tomorrow you and your sons are with me supplies the proof.',['Anonymous Gemara citing Samuel'])
claim('12domain','12b:12','Rabbi Yohanan interprets with me as in my domain.',['Rabbi Yohanan'])
claim('13','12b:13','The sages give another proof: at Saul chosen of the Lord, a heavenly voice declared chosen of the Lord.',['Sages'])
for ref in ['12a:23','12a:24','12b:2','12b:6','12b:9']:
 att('a'+ref.replace(':','_'),ref,'רבה בר חיננא','transmitter',['רבה בר חיננא סבא'],'Rav teaching',chain=['רבה בר חיננא סבא','רב'],unc=['סבא is bracketed in12a24 but explicit in the parallel reports.'] if ref=='12a:24' else [])
for k,ref,surface,name in [('25','12a:25','שמואל','שמואל'),('28s','12a:28','שמואל','שמואל'),('28h','12a:28','חייא בר רב','חייא בר רב'),('1','12b:1','רב ששת','רב ששת'),('3','12b:3','רבי אלעזר','רבי אלעזר'),('5y','12b:5','רב יוסף','רב יוסף'),('5r','12b:5','רבה','רבה'),('7','12b:7','רבא','רבא'),('12','12b:12','ר יוחנן','רבי יוחנן')]:att('a'+k,ref,surface,'speaker',[name],'Local rule, explanation or addressed participant')
for k,ref,a,b,rel in [('25','12a:25','c25','q25','answer'),('25s','12a:25','c25','c24rise','support'),('26','12a:26','q26','c24rise','objection'),('27','12a:27','c27','q26','answer'),('28','12a:28','c28','c24rise','support'),('3','12b:3','c3','c2ten','qualification'),('5y','12b:5','c5yosef','q4','answer'),('5r','12b:5','c5rabbah','q4','answer'),('5d','12b:5','c5yosef','c5rabbah','distinction'),('5law','12b:5','c5law','c5rabbah','support'),('7','12b:7','c7','c6','qualification'),('8','12b:8','c8proof','q8','answer'),('8r','12b:8','c8rejected','q8','answer'),('10','12b:10','c10reject','c9','qualification'),('10s','12b:10','c10saul','c9','support'),('11','12b:11','c11','c10saul','support'),('12','12b:12','c12with','q12','answer'),('12s','12b:12','c12domain','c12with','support'),('13','12b:13','c13','q12','answer')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local transmitted Rav teachings, named qualifications and proofs. Distinguish Rav/Shmuel support from dispute, Rabbah from Rava, and rejected proofs from rejected claims.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read12a23–12b28; reread core12a23–12b13 for repeated Rav transmission, bowing lexical distinction, ten-day formulas and explicit Rabbah ruling, fellow/scholar prayer, king/community counterexamples, Saul’s omitted Urim and two forgiveness proofs. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch21_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch21_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch21_receipt.json',r.encoded(out));print(r.encoded(out).decode())
