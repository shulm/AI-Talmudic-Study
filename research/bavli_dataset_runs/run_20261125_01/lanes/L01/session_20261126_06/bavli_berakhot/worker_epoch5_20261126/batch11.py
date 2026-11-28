from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.pesach_night.20261126e5.'
assert r.sha(r.encoded(state))=='b388a1539c9c7c3a4e976734c601192f5c10ac68c12db6d222b94058f4cc7831'
refs=['9a:'+str(i) for i in range(11,29)]
for k,ns,title in [('end',range(11,23),'Paschal eating: midnight versus dawn and scriptural words'),('parallel',range(23,25),'Parallel tannaitic readings of sacrifice, eating and burning'),('haste',range(25,29),'Agreed redemption and departure times; different haste')]:add('s'+k,'structure',['9a:'+str(i) for i in ns],dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices={11:'Mishnah lemma',12:'Anonymous observation',13:'Anonymous objection citing baraita',14:'Rav Yosef; baraita of Rabbi Eleazar ben Azariah',15:'Rabbi Akiva replying',16:'Continuation of Rabbi Akiva exposition',17:'Anonymous question',18:'Answer for Rabbi Akiva',19:'Anonymous question concerning Rabbi Eleazar ben Azariah',20:'Answer for Rabbi Eleazar ben Azariah',21:'Anonymous representation of Rabbi Akiva’s reasoning',22:'Anonymous representation of Rabbi Eleazar’s reply',23:'Anonymous linkage and cited verse',24:'Baraita of Rabbi Eliezer and Rabbi Yehoshua',25:'Rabbi Abba',26:'Rabbi Abba’s distinction of Rabbi Eleazar ben Azariah view',27:'Continuation distinguishing Rabbi Akiva view',28:'Supporting baraita'}
for n in range(11,29):add('u'+str(n),'utterances',['9a:'+str(n)],dict(textual_voice=voices[n],discourse_role='Lemma or legal exegesis',composition='composite'))
def claim(k,n,text,holders,cond=(),status='Reported locally',unc=()):
 ref='9a:'+str(n);c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('12',12,'The Mishnah does not list eating the paschal offering among all-night mitzvot.',['Anonymous Gemara'],status='Observation about omission')
claim('13',13,'The opposing baraita gives evening Shema, Hallel on Passover nights and eating the paschal offering until dawn.',['Unnamed baraita'])
claim('14resolve',14,'Rav Yosef resolves the sources by distinguishing Rabbi Eleazar ben Azariah and Rabbi Akiva.',['Rav Yosef'],status='Dispute-based resolution',unc=['The following explicit positions identify the midnight account with Rabbi Eleazar ben Azariah and dawn account with Rabbi Akiva; not assignment by simple order alone.'])
claim('14midnight',14,'Rabbi Eleazar ben Azariah derives eating until midnight by linking this night of eating with this night of God passing through Egypt.',['Rabbi Eleazar ben Azariah'])
claim('15haste',15,'Rabbi Akiva replies that in haste already gives until the time of haste.',['Rabbi Akiva'],status='Opposing derivation; later haste distinction identifies the endpoint')
q('q15','9a:15','Given the haste derivation, what does at night teach?')
claim('16hyp',16,'One could otherwise suppose the paschal offering is eaten by day like other sacred offerings.',['Rabbi Akiva exposition'],status='Rejected possibility')
claim('16',16,'At night teaches that it is eaten at night and not by day.',['Rabbi Akiva exposition'])
q('q17','9a:17','Rabbi Eleazar ben Azariah needs this for the verbal analogy; what does Rabbi Akiva do with this?')
claim('18hyp',18,'Because Passover and peace offerings are lesser sancta, one might allow two nights and a day in place of the peace offering’s two days and a night.',['Anonymous explanation for Rabbi Akiva'],status='Rejected proposed analogy')
claim('18',18,'This night excludes eating on a further night.',['Rabbi Akiva as explained anonymously'])
q('q19','9a:19','How does Rabbi Eleazar ben Azariah obtain exclusion of another night?')
claim('20',20,'He derives it from not leaving any until morning.',['Rabbi Eleazar ben Azariah as explained anonymously'])
claim('21',21,'Rabbi Akiva says that from morning alone one might have understood the second morning.',['Rabbi Akiva as explained anonymously'],status='Explains need for additional this-night wording')
claim('22',22,'Rabbi Eleazar replies that every unqualified morning is the first morning.',['Rabbi Eleazar ben Azariah, contextual identity'],unc=['Printed רבי אלעזר here is resolved by the continuing named dispute, not treated as another amora.'])
claim('23',23,'The discussion aligns the preceding tannaim with another tannaitic interpretation of sacrifice at evening, sunset and the time of departure from Egypt.',['Anonymous Gemara'],status='Explicit parallel dispute linkage')
claim('24e',24,'Rabbi Eliezer reads evening as sacrifice, sunset as eating, and the time of departure as burning.',['Rabbi Eliezer'],unc=['The source here says burning at departure; it does not explicitly repeat a midnight eating deadline.'])
claim('24y',24,'Rabbi Yehoshua reads evening as sacrifice, sunset as eating, and permits continuing eating until the departure time.',['Rabbi Yehoshua'])
claim('25redeem',25,'Rabbi Abba says all agree Israel’s redemption began in the evening, citing redemption at night.',['Rabbi Abba'],status='Shared premise, not disputed endpoint')
claim('25depart',25,'All agree their actual departure occurred by day, citing departure on the day after Passover.',['Rabbi Abba'],status='Shared premise')
q('q26','9a:26','What then is the disagreement about?')
claim('26',26,'It concerns the time of haste: Rabbi Eleazar ben Azariah understands Egyptian haste.',['Rabbi Eleazar ben Azariah as reported by Rabbi Abba'])
claim('27',27,'Rabbi Akiva understands Israel’s haste.',['Rabbi Akiva as reported by Rabbi Abba'])
q('q28','9a:28','How can the verse say departure at night when the departure was by day?')
claim('28',28,'The supporting baraita interprets the night verse as redemption beginning in the evening.',['Unnamed baraita'])
att('a14r','9a:14','רב יוסף','speaker',['רב יוסף'],pre+'c14resolve')
att('a14e','9a:14','רבי אלעזר בן עזריה','quoted_authority',['רבי אלעזר בן עזריה'],pre+'c14midnight')
att('a15','9a:15',"ר' עקיבא",'speaker',['רבי עקיבא'],'Opposing reply and derivation')
att('a24e','9a:24',"ר' אליעזר",'speaker',['רבי אליעזר'],pre+'c24e')
att('a24y','9a:24','רבי יהושע','speaker',['רבי יהושע'],pre+'c24y')
att('a25','9a:25','ר אבא','speaker',['רבי אבא'],'Shared premises and dispute explanation')
for k,n,a,b,rel in [('13',13,'c13','c12','objection'),('14r',14,'c14resolve','c13','answer'),('15',15,'c15haste','c14midnight','objection'),('16',16,'c16','q15','answer'),('16h',16,'c16','c16hyp','objection'),('18',18,'c18','q17','answer'),('18h',18,'c18','c18hyp','objection'),('20',20,'c20','q19','answer'),('21',21,'c21','c20','objection'),('22',22,'c22','c21','objection'),('24',24,'c24e','c24y','distinction'),('26',26,'c26','q26','answer'),('27',27,'c27','q26','answer'),('27d',27,'c26','c27','distinction'),('28',28,'c28','q28','answer'),('28s',28,'c28','c25redeem','support')]:edge('e'+k,'9a:'+str(n),a,b,rel)
for x in rows:
 if x['id'] in [pre+'e24',pre+'e27d']:x['uncertainty'].append('Opposed readings; arrow order is textual, not a historical reply assignment.')
 if x['layer']=='claims':x['content']['scope']='Local Paschal eating derivations. Preserve source omission versus baraita, both named disputes, hypothetical second morning/two-night possibilities, and agreed redemption/departure chronology separately.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read9a11–9b31; reread core9a11–28 for omitted Passover item, midnight/haste derivations, night/this/morning allocations, two rejected hypotheses, parallel tannaim, shared chronology and different haste referents.9a11 is a lemma not new claim. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch11_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch11_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch11_receipt.json',r.encoded(out));print(r.encoded(out).decode())
