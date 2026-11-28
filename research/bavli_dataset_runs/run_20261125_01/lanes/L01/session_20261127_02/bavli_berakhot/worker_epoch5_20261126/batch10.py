from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.shema_versions.20261126e5.'
assert r.sha(r.encoded(state))=='57492f73b120f3f3b48ef0a8f1593a2bb1f97e7116a2b4fec8bf613d5a5b4b5b'
refs=['8b:'+str(i) for i in range(17,24)]+['9a:'+str(i) for i in range(1,11)]
for k,rr,title in [('gamliel',refs[:1],'Ruling like Rabban Gamliel'),('dawn',refs[1:5],'Two night recitations on opposite sides of dawn'),('sunrise',refs[5:11],'Alternative report on two day recitations and exigency'),('sons',refs[11:14],'Sons ask whether sages disagree'),('extension',refs[14:],'Even sages’ midnight limit is a fence')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Rav Yehuda reporting Shmuel','Baraita of Rabbi Shimon ben Yohai','Anonymous internal objection','Anonymous resolution','Rav Aha bar Hanina reporting Rabbi Yehoshua ben Levi','Alternative placement of report; Rabbi Shimon ben Yohai reporting Rabbi Akiva','Anonymous internal objection','Anonymous resolution','Rabbi Aha bar Hanina reporting Rabbi Yehoshua ben Levi; Rabbi Zeira','Rav Yitzhak bar Yosef','Narrative and Rabbi Yehoshua ben Levi','Mishnah lemma','Anonymous question','Reconstructed sons/father dialogue','Mishnah lemma','Anonymous question','Anonymous reconstruction of Rabban Gamliel reply']
assert len(voices)==len(refs)
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Lemma or local legal discussion',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('17','8b:17','Rav Yehuda reports Shmuel ruling like Rabban Gamliel.',['Shmuel'],status='Explicit reported halakhic ruling',unc=['The lemma refers back to Rabban Gamliel’s evening-Shema limit; no new time is written in this line.'])
claim('18before','8b:18','Rabbi Shimon ben Yohai permits a pair described as twice at night: one Shema before dawn fulfills the night obligation.',['Rabbi Shimon ben Yohai'],cond=['Recitation before dawn in described pair'])
claim('18after','8b:18','The recitation after dawn in that pair fulfills the day obligation.',['Rabbi Shimon ben Yohai'],cond=['Recitation after dawn in described pair'])
q('q19','8b:19','How can after dawn be called night in the opening and day in fulfillment of the day obligation?')
claim('20night','8b:20','The answer retains night as the classification.',['Anonymous Gemara'],status='Local resolution of first baraita wording')
claim('20rise','8b:20','It is called day for the obligation because some people rise at that time.',['Anonymous Gemara'],cond=['Some people rise at that time'])
claim('21','8b:21','Rav Aha bar Hanina reports Rabbi Yehoshua ben Levi ruling like Rabbi Shimon ben Yohai.',['Rabbi Yehoshua ben Levi'],status='First placement of reported halakhic statement',unc=['A following alternative report places this statement on a different baraita; do not merge their settings.'])
claim('22placement','8b:22','An alternative version teaches Rav Aha bar Hanina’s report concerning the following baraita.',['Anonymous alternative report'],status='Alternative placement, not an additional cumulative ruling')
claim('22before','8b:22','Rabbi Shimon ben Yohai reports Rabbi Akiva describing two recitations by day: one before sunrise fulfills the night obligation.',['Rabbi Akiva'],cond=['Recitation before sunrise in described pair'])
claim('22after','8b:22','The recitation after sunrise fulfills the day obligation.',['Rabbi Akiva'],cond=['Recitation after sunrise in described pair'])
q('q23','8b:23','How can before sunrise be called day in the opening but count for the night obligation?')
claim('1day','9a:1','The answer retains day as the classification in this second baraita.',['Anonymous Gemara'])
claim('1sleep','9a:1','It is called night for the obligation because some people sleep at that time.',['Anonymous Gemara'],cond=['Some people sleep at that time'])
claim('2rule','9a:2','Rabbi Aha bar Hanina reports Rabbi Yehoshua ben Levi ruling like Rabbi Shimon who spoke in Rabbi Akiva’s name.',['Rabbi Yehoshua ben Levi'],status='Reported halakhic statement later qualified as inferred')
claim('2hash','9a:2','Rabbi Zeira qualifies this by omitting Hashkivenu.',['Rabbi Zeira'],cond=['Application of preceding night-Shema-after-dawn teaching'],unc=['Do not apply the qualification indiscriminately to every Shema recitation.'])
claim('3','9a:3','Rav Yitzhak bar Yosef reports that this statement of Rabbi Yehoshua ben Levi via Rabbi Aha was not explicit but inferred.',['Rav Yitzhak bar Yosef'],status='Correction of provenance, not denial of the incident')
claim('4event','9a:4','Two sages became drunk at Rabbi Yehoshua ben Levi’s son’s wedding and came before him.',['Anonymous narrator'],status='Narrative setting for inference')
claim('4ruling','9a:4','Rabbi Yehoshua ben Levi said Rabbi Shimon is worthy of reliance in exigent circumstances.',['Rabbi Yehoshua ben Levi'],cond=['Exigent circumstances'],status='Explicit incident-based permission underlying inference')
q('q6','9a:6','Had Rabban Gamliel’s sons not heard his ruling until then?')
claim('7dispute','9a:7','The sons’ reconstructed first possibility is that sages disagree, in which case the law follows the many against the individual.',['Sons as reconstructed by anonymous discussion'],status='Question alternative, not final claim that sages disagree')
claim('7fence','9a:7','Their other possibility is that sages agree in substance and midnight is only a safeguard from transgression.',['Sons as reconstructed by anonymous discussion'],status='Question alternative subsequently accepted')
claim('7answer','9a:7','Rabban Gamliel answers that sages agree with him, the sons remain obligated, and midnight is a safeguard.',['Rabban Gamliel as reconstructed by anonymous discussion'],status='Local answer')
q('q9','9a:9','Did Rabban Gamliel himself say until midnight, so that not this alone they said is appropriate?')
claim('10','9a:10','His reply is reconstructed as: even according to sages who say midnight, the mitzvah extends until dawn, with midnight safeguarding against transgression.',['Rabban Gamliel as reconstructed by anonymous discussion'])
att('a17','8b:17','רב יהודה אמר שמואל','transmitter',['רב יהודה'],pre+'c17',chain=['רב יהודה','שמואל'])
att('a18','8b:18','ר"ש בן יוחי','quoted_authority',['רבי שמעון בן יוחאי'],'First baraita')
att('a21','8b:21','רב אחא בר חנינא אמר רבי יהושע בן לוי','transmitter',['רב אחא בר חנינא'],pre+'c21',chain=['רב אחא בר חנינא','רבי יהושע בן לוי'])
att('a22','8b:22',"רבי שמעון בן יוחי אומר משום ר' עקיבא",'transmitter',['רבי שמעון בן יוחאי'],'Second baraita',chain=['רבי שמעון בן יוחאי','רבי עקיבא'])
att('a2rule','9a:2','רבי אחא ברבי חנינא אמר רבי יהושע בן לוי','transmitter',['רבי אחא ברבי חנינא'],pre+'c2rule',chain=['רבי אחא ברבי חנינא','רבי יהושע בן לוי'])
att('a2z','9a:2','רבי זירא','speaker',['רבי זירא'],pre+'c2hash')
att('a3','9a:3','רב יצחק בר יוסף','speaker',['רב יצחק בר יוסף'],pre+'c3')
att('a4','9a:4','ריב"ל','speaker',['רבי יהושע בן לוי'],pre+'c4ruling')
att('a10','9a:10','ר"ג לבניה','speaker',['רבן גמליאל'],'Reconstructed reply to sons')
for k,ref,a,b,rel in [('19','8b:19','q19','c18after','objection'),('20n','8b:20','c20night','q19','answer'),('20r','8b:20','c20rise','q19','answer'),('22p','8b:22','c22placement','c21','distinction'),('23','8b:23','q23','c22before','objection'),('1d','9a:1','c1day','q23','answer'),('1s','9a:1','c1sleep','q23','answer'),('2h','9a:2','c2hash','c2rule','qualification'),('3','9a:3','c3','c2rule','correction'),('4','9a:4','c4ruling','c3','support'),('7','9a:7','c7answer','q6','answer'),('7d','9a:7','c7answer','c7dispute','objection'),('7f','9a:7','c7answer','c7fence','support'),('10','9a:10','c10','q9','answer')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['id']==pre+'e22p':x['uncertainty'].append('Alternative report placement; textual direction does not imply historical disagreement between reporters.')
 if x['layer']=='claims':x['content']['scope']='Local Shema timing discussion; distinguish dawn and sunrise baraitot, alternative report placement, exigency-limited incident, and anonymous reconstructions of Mishnah dialogue.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read8b17–9b31; reread core8b17–9a10 for two nonmerged baraitot, day/night classifications versus sleep/rising, alternative placement, Hashkivenu scope, explicit-to-inferred correction and exigency condition, sons’ question alternatives and fence resolution. Lemmas9a5/8 are not additional claims. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch10_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch10_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch10_receipt.json',r.encoded(out));print(r.encoded(out).decode())
