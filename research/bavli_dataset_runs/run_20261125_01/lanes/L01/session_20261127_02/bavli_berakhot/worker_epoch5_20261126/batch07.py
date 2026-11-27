from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.ancestors.20261126e5.'
assert r.sha(r.encoded(state))=='d967d935cb7297f6f476587940f607872771b46fbaf60c5ee0c8ca1652fe8eb3'
refs=['7b:'+str(i) for i in range(1,27)]
for k,ns,title in [('lord',range(1,4),'Abraham calling God Lord and Daniel’s answer'),('anger',range(4,5),'Repeated appeasement teaching under different authority'),('thanks',range(5,9),'Leah’s thanks and Reuben’s name'),('ruth',range(9,11),'Ruth and names as causes'),('house',range(11,15),'Household rebellion and David’s psalm'),('wicked',range(15,23),'Provoking the wicked: objections and alternative distinctions'),('place',range(23,26),'Fixed prayer place and enemies'),('service',range(26,27),'Serving Torah greater than learning')]:add('s'+k,'structure',['7b:'+str(i) for i in ns],dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices={1:'Rabbi Yohanan reporting Rabbi Shimon ben Yohai',2:'Rav',3:'Continuation of Rav exposition',4:'Rabbi Yohanan reporting Rabbi Shimon ben Yohai',5:'Rabbi Yohanan reporting Rabbi Shimon ben Yohai',6:'Rabbi Eleazar representing Leah’s speech',7:'Continuation of proof',8:'Continuation of Leah comparison',9:'Anonymous question and Rabbi Yohanan',10:'Anonymous question and Rabbi Eliezer',11:'Rabbi Yohanan reporting Rabbi Shimon ben Yohai',12:'Anonymous objection',13:'Rabbi Shimon ben Avishalom',14:'Parable application',15:'Rabbi Yohanan reporting Rabbi Shimon ben Yohai',16:'Baraita of Rabbi Dostai bar Matun',17:'Additional cited verse',18:'Anonymous objection quoting Rabbi Yitzhak',19:'Anonymous first distinction',20:'Anonymous alternative distinction',21:'Anonymous alternative distinction citing Rav Huna',22:'Anonymous alternative answer',23:'Rabbi Yohanan reporting Rabbi Shimon ben Yohai',24:'Rav Huna',25:'Resolution of verse contrast',26:'Rabbi Yohanan reporting Rabbi Shimon ben Yohai'}
for n in range(1,27):add('u'+str(n),'utterances',['7b:'+str(n)],dict(textual_voice=voices[n],discourse_role='Teaching, objection or exposition',composition='composite'))
def claim(k,n,text,holders,cond=(),status='Reported locally',unc=()):
 ref='7b:'+str(n);c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('1',1,'Rabbi Yohanan reports Rabbi Shimon ben Yohai that Abraham was the first since creation to call God Lord.',['Rabbi Shimon ben Yohai'])
claim('2',2,'Rav says Daniel too was answered only on Abraham’s account, citing for the sake of the Lord rather than for Your sake.',['Rav'])
claim('3',3,'The wording is interpreted as for Abraham who called You Lord.',['Rav, continuation'])
claim('4',4,'Rabbi Yohanan reports Rabbi Shimon ben Yohai that one does not appease a person at the time of anger, citing My face will go and I will give you rest.',['Rabbi Shimon ben Yohai'],cond=['Person is angry'],unc=['Parallel to7a5 but with Rabbi Shimon ben Yohai rather than Rabbi Yose as source authority; retain both occurrences.'])
claim('5',5,'Rabbi Yohanan reports Rabbi Shimon ben Yohai that Leah was the first since creation to thank God, saying this time I thank the Lord.',['Rabbi Shimon ben Yohai'])
claim('6name',6,'Rabbi Eleazar interprets Reuben through Leah saying: see the difference between my son and my father-in-law’s son.',['Rabbi Eleazar'])
claim('6esau',6,'Esau willingly sold his birthright yet hated Jacob.',['Leah represented by Rabbi Eleazar'],status='First side of comparison')
claim('7',7,'The additional verse depicts Esau complaining that Jacob supplanted him twice.',['Continuation of represented comparison'])
claim('8',8,'Reuben lost the birthright to Joseph against his will yet did not envy him and rescued him from his brothers.',['Leah represented by Rabbi Eleazar'],status='Second side of comparison')
q('q9','7b:9','What is the meaning of Ruth’s name?')
claim('9',9,'Rabbi Yohanan interprets Ruth by her meriting David, who satiated God with songs and praises.',['Rabbi Yohanan'])
q('q10','7b:10','From where do we know a name has an effect?')
claim('10',10,'Rabbi Eliezer rereads the Psalm’s shamot as names to support names having an effect.',['Rabbi Eliezer'],unc=['The printed unvocalized שמות forms are identical; no invented vocalized source quotation.'])
claim('11',11,'Rabbi Yohanan reports Rabbi Shimon ben Yohai that bad upbringing within one’s house is harder than Gog and Magog’s war: the psalm about Absalom says how numerous my foes, unlike the other psalm.',['Rabbi Shimon ben Yohai'])
q('q12','7b:12','Why a psalm of David fleeing Absalom rather than a lament?')
claim('13',13,'Rabbi Shimon ben Avishalom offers a debtor parable: before paying the debt he grieves; after paying he rejoices.',['Rabbi Shimon ben Avishalom'])
claim('14fear',14,'David grieved at the promised evil from his own house, fearing a slave or mamzer who would have no mercy on him.',['Parable application'])
claim('14joy',14,'Seeing that it was Absalom, he rejoiced and therefore called it a psalm.',['Parable application'],unc=['The text supplies the prior feared lack of mercy; no claim that Absalom was harmless or the rebellion good.'])
claim('15',15,'Rabbi Yohanan reports Rabbi Shimon ben Yohai that it is permitted to provoke the wicked in this world, citing keepers of Torah striving against them.',['Rabbi Shimon ben Yohai'],unc=['Qualified by ensuing alternative resolutions; not an unqualified final recommendation.'])
claim('16rule',16,'The supporting baraita of Rabbi Dostai bar Matun permits provoking the wicked in this world from the same verse.',['Rabbi Dostai bar Matun'])
q('q16','7b:16','If someone objects from do not contend with evildoers or envy wrongdoers, how should one answer?')
claim('16meaning',16,'The baraita rejects that objection and reads the prohibition as becoming like evildoers or wrongdoers.',['Rabbi Dostai bar Matun'])
claim('17',17,'The verse against envying sinners but urging fear of God supports that interpretation.',['Baraita continuation'])
q('q18','7b:18','How can provocation be permitted given Rabbi Yitzhak’s prohibition when fortune favors the wicked?')
claim('18avoid',18,'Rabbi Yitzhak says not to provoke a wicked person whose time prospers.',['Rabbi Yitzhak'],cond=['Wicked person presently prospers'])
claim('18court',18,'Such a person additionally succeeds in judgment, supported by the cited psalm.',['Rabbi Yitzhak'],cond=['Wicked person presently prospers'])
claim('18enemies',18,'He additionally prevails over adversaries, as all his enemies are blown away.',['Rabbi Yitzhak'],cond=['Wicked person presently prospers'])
claim('19',19,'The first answer distinguishes personal matters from heavenly matters.',['Anonymous Gemara'],status='First alternative resolution',unc=['Personal matters are the restricted case and heavenly matters the permission by contextual mapping; raw clauses simply contrast הא/הא.'])
claim('20',20,'Another answer keeps both in heavenly matters and distinguishes a prosperous wicked person from one not prosperous.',['Anonymous Gemara'],status='Alternative resolution',unc=['Do not combine this with the first answer into one silently unified ruling.'])
claim('21dist',21,'Another answer keeps both with a prosperous wicked person and distinguishes wholly righteous from not wholly righteous opponents.',['Anonymous Gemara'],status='Alternative resolution')
q('q21','7b:21','Rav Huna asks how the wicked can swallow one more righteous, given verses of protection for the righteous.')
claim('21relative',21,'The explanation permits swallowing one more righteous than the wicked person.',['Rav Huna exposition'],cond=['Relatively righteous, not wholly righteous'])
claim('21whole',21,'A wholly righteous person is not swallowed.',['Rav Huna exposition'],cond=['Wholly righteous'])
claim('22',22,'Another answer treats the case of prospering fortune as different.',['Anonymous Gemara'],status='Final alternative answer',unc=['The terse answer qualifies the preceding protective account; do not silently erase its tension with the wholly-righteous distinction.'])
claim('23',23,'Rabbi Yohanan reports Rabbi Shimon ben Yohai that enemies fall beneath one who fixes a place for prayer, citing planting Israel in a place without further affliction.',['Rabbi Shimon ben Yohai'],cond=['Fixed place for prayer'])
q('q24','7b:24','Rav Huna juxtaposes the wording to afflict him and to destroy him.')
claim('25',25,'The answer distinguishes initially to afflict him and subsequently to destroy him.',['Resolution of Rav Huna contrast'],unc=['The brief clause does not spell out historical stages or invert the verbs; preserve its actual wording.'])
claim('26',26,'Rabbi Yohanan reports Rabbi Shimon ben Yohai that service of Torah is greater than learning, inferred from Elisha pouring water on Elijah’s hands rather than being described as having learned.',['Rabbi Shimon ben Yohai'])
for n in [1,4,5,11,15,23,26]:
 surface=by['7b:'+str(n)]['text'].split('מיום')[0] if n in [1,5] else None
 # Keep a compact exact transmitter name; source authority and chain explicit in structured fields.
 att('a'+str(n),'7b:'+str(n),'ר"י' if n==5 else 'יוחנן','transmitter',['רבי יוחנן'],'Teaching of Rabbi Shimon ben Yohai',chain=['רבי יוחנן','רבי שמעון בן יוחאי'])
for k,n,surface,name in [('2',2,'רב','רב'),('6',6,'ר אלעזר','רבי אלעזר'),('9',9,'ר יוחנן','רבי יוחנן'),('10',10,'רבי אליעזר','רבי אליעזר'),('13',13,"ר' שמעון בן אבישלום",'רבי שמעון בן אבישלום'),('16',16,"רבי דוסתאי בר' מתון",'רבי דוסתאי בר מתון'),('18',18,"ר' יצחק",'רבי יצחק'),('21',21,'רב הונא','רב הונא'),('24',24,'רב הונא','רב הונא')]:att('a'+k,'7b:'+str(n),surface,'speaker',[name],'Local teaching')
for k,n,a,b,rel in [('3',3,'c3','c2','support'),('7',7,'c7','c6esau','support'),('8',8,'c8','c6esau','distinction'),('9',9,'c9','q9','answer'),('10',10,'c10','q10','answer'),('13',13,'c13','q12','answer'),('14',14,'c14joy','q12','answer'),('16s',16,'c16rule','c15','support'),('16a',16,'c16meaning','q16','answer'),('17',17,'c17','c16meaning','support'),('18',18,'c18avoid','c15','objection'),('19',19,'c19','q18','answer'),('20',20,'c20','q18','answer'),('21',21,'c21dist','q18','answer'),('21r',21,'c21relative','q21','answer'),('21w',21,'c21whole','q21','answer'),('21s',21,'c21whole','c21dist','support'),('22',22,'c22','c21whole','qualification'),('25',25,'c25','q24','answer')]:edge('e'+k,'7b:'+str(n),a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local exegetical and moral teachings; alternatives remain alternatives and repeated occurrences retain distinct attributions.'
 if x['id']==pre+'e8':x['uncertainty'].append('Comparison in Leah’s represented speech; not a dispute between the sons.')
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read7b1–28; reread core7b1–26 for repeated teaching/different authority, Reuben comparison, unvocalized name wordplay, debtor parable, all four provocation resolutions including final qualification, fixed-place verses and service greater than study. Core ends before new dialogue7b27. Completed '+layer+' pass; no additional record where none listed.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch07_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch07_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch07_receipt.json',r.encoded(out));print(r.encoded(out).decode())
