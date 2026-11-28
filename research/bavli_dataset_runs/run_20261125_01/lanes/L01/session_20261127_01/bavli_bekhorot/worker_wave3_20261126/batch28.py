from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.sacredseventh.20261126w3.'
assert r.sha(r.encoded(state))=='1fa44e77a1be0ea874d275dfef40c022824363619ac66fdc5ac773fc9487f47f'
refs=['12a:'+str(n) for n in range(20,26)]+['12b:'+str(n) for n in range(1,16)]
add('s1','structure',refs[:7],dict(title='Redeeming with disqualified sacred animals: initially scoped inquiry, general exclusion',primary=True,boundary='closed',legacy_ids=[]))
add('s2','structure',refs[7:19],dict(title='Seventh-year animal redemption, firstborn exemption, gifts and dough challenge',primary=True,boundary='closed',legacy_ids=[]))
add('s3','structure',refs[19:],dict(title='Giving the donkey to a priest requires observed redemption',primary=True,boundary='closed',legacy_ids=[]))
q('q20','12a:20','May disqualified sacred animals be used for firstborn-donkey redemption?')
c('c21s','12a:21','The initial analysis treats the inquiry as unnecessary for Rabbi Shimon because he permits benefit from the donkey and treats it as ordinary.',mode='challenged')
c('c21y','12a:21','It initially confines the inquiry to Rabbi Yehuda’s benefit prohibition.')
c('c22','12a:22','One branch invokes prohibition not taking effect upon an existing prohibition.',mode='hypothetical')
c('c23','12a:23','The other branch treats donkey redemption as merely removing prohibition because the substitute does not acquire the donkey’s prohibition.',mode='hypothetical')
c('c24','12a:24','Rav Mari son of Rav Kahana excludes disqualified sacred animals by their scriptural comparison to deer and gazelle, which cannot redeem a donkey.')
c('c25intro','12a:25','The Gemara extends the consequence of that new reason.')
c('c1','12b:1','The same deer-and-gazelle wording excludes these animals for Rabbi Shimon as well.')
q('q2','12b:2','May an animal with seventh-year sanctity be used for redemption?')
c('c3definite','12b:3','For a definite firstborn donkey the answer is no, because the seventh-year produce is for eating rather than commerce.')
c('c3doubt','12b:3','The question concerns a doubtful firstborn donkey.')
c('c4s','12b:4','Under Rabbi Shimon the doubtful case does not raise this redemption inquiry because he has no required doubtful-case release from benefit prohibition.')
c('c4y','12b:4','The inquiry is under Rabbi Yehuda.')
c('c5eat','12b:5','One branch treats the separated lamb retained by the owner as for eating.',mode='hypothetical')
c('c5trade','12b:5','The alternative treats removal of the donkey’s prior prohibition as commerce.',mode='hypothetical')
c('c6definite','12b:6','Rav Hisda prohibits using a seventh-year animal to redeem a definite firstborn donkey.',cond=['Definite firstborn donkey'])
c('c6doubt','12b:6','Rav Hisda permits using it to redeem a doubtful firstborn donkey.',cond=['Doubtful firstborn donkey'])
c('c7first','12b:7','Rav Hisda exempts a seventh-year animal from firstborn liability.')
c('c7gifts','12b:7','He requires the priestly animal gifts from it.')
c('c8burn','12b:8','Firstborn exemption follows from for eating and not for burning.')
c('c8eat','12b:8','The animal gifts remain for eating, explaining their liability.')
c('c9','12b:9','The objection cites liability to death for eating seventh-year dough before its hallah is removed.')
q('q10','12b:10','Why does hallah apply when it would require burning if it became impure, contrary to for eating rather than burning?')
c('c11','12b:11','The answer invokes throughout your generations for hallah.')
c('c12','12b:12','A supporting baraita derives that liability for seventh-year dough from throughout your generations.')
q('q13','12b:13','Why not derive firstborn liability from hallah as well?')
c('c13hallah','12b:13','The answer distinguishes hallah as primarily for eating.')
c('c13first','12b:13','It distinguishes the firstborn case here as primarily for burning.')
c('c14','12b:14','An Israelite may not give his firstborn donkey to a priest who promises to redeem it unless redemption is performed in the Israelite’s presence.',cond=['Priest asks to receive donkey and promises redemption'])
c('c15suspect','12b:15','Rav Nahman reports Rabba bar Avuha inferring that priests are suspected regarding firstborn donkeys.')
c('c15narrow','12b:15','One might limit suspicion to a priest known to act improperly.',mode='hypothetical')
c('c15general','12b:15','The teaching applies the concern even without that prior knowledge, because the priest may rationalize permission.')
for ref,v,role in [('12a:20','Anonymous Gemara','Disqualified sacred-animal inquiry'),('12a:21','Anonymous analysis','Initial tannaitic scope'),('12a:22','Anonymous analysis','Prohibition-on-prohibition branch'),('12a:23','Anonymous analysis','Release-only alternative'),('12a:24','Rav Mari son of Rav Kahana','Deer/gazelle exclusion'),('12a:25','Anonymous Gemara','Extension begins'),('12b:1','Anonymous Gemara','RabbiShimon also excluded'),('12b:2','Anonymous Gemara','Seventh-year animal inquiry'),('12b:3','Anonymous Gemara','Definite versus doubtful case'),('12b:4','Anonymous Gemara','Tannaitic scope'),('12b:5','Anonymous Gemara','Eating versus commerce alternatives'),('12b:6','Rav Hisda','Definite prohibited/doubtful permitted'),('12b:7','Rav Hisda','Firstborn exemption and gifts liability'),('12b:8','Anonymous explanation','Eating versus burning reasons'),('12b:9','Anonymous objection citing baraita','Seventh-year dough liability'),('12b:10','Anonymous objection','Potential burning challenge'),('12b:11','Anonymous answer','Generations wording'),('12b:12','Supporting baraita','Generations derivation'),('12b:13','Anonymous exchange','Hallah/firstborn distinction'),('12b:14','Baraita','Observed redemption before giving to priest'),('12b:15','Rav Nahman reporting Rabba bar Avuha; anonymous explanation','Priestly suspicion not limited to known offender')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
for k,ref,surf,role,cands,scope,chain in [('a21s','12a:21','ר"ש','position_holder',['רבי שמעון'],'Benefit premise',[]),('a21y','12a:21','רבי יהודה','position_holder',['רבי יהודה'],'Benefit premise',[]),('a24','12a:24','רב מרי בריה דרב כהנא','speaker',['רב מרי בריה דרב כהנא'],'Deer/gazelle exclusion',[]),('a6','12b:6','חסדא','quoted_authority',['רב חסדא'],'Seventh-year redemption',[]),('a7','12b:7','רב חסדא','speaker',['רב חסדא'],'Firstborn and gifts',[]),('a15n','12b:15','נחמן','transmitter',['רב נחמן'],'Priestly suspicion',['רב נחמן','רבה בר אבוה']),('a15r','12b:15','רבה בר אבוה','quoted_authority',['רבה בר אבוה'],'Priestly suspicion',['רב נחמן','רבה בר אבוה'])]:att(k,ref,surf,role,cands,scope,chain)
for k,ref,cl,h,st,qu in [('p21','12a:21','c21s',['Initial anonymous analysis'],'Initial scope displaced by new reason','q20'),('p22','12a:22','c22',['Anonymous Gemara'],'Inquiry branch','q20'),('p23','12a:23','c23',['Anonymous Gemara'],'Inquiry branch','q20'),('p24','12a:24','c24',['רב מרי בריה דרב כהנא'],'Exclusion by different ground','q20'),('p1','12b:1','c1',['Anonymous Gemara'],'Exclusion also under RabbiShimon','q20'),('p5e','12b:5','c5eat',['Anonymous Gemara'],'Inquiry branch','q2'),('p5t','12b:5','c5trade',['Anonymous Gemara'],'Inquiry branch','q2'),('p6d','12b:6','c6definite',['רב חסדא'],'Definite prohibited','q2'),('p6s','12b:6','c6doubt',['רב חסדא'],'Doubtful permitted','q2'),('p7f','12b:7','c7first',['רב חסדא'],'Firstborn exemption',None),('p7g','12b:7','c7gifts',['רב חסדא'],'Gifts liability',None),('p11','12b:11','c11',['Anonymous Gemara'],'Hallah exception source','q10'),('p14','12b:14','c14',['Anonymous baraita'],'Observed redemption condition',None),('p15','12b:15','c15general',['Anonymous Gemara'],'Suspicion scope',None)]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,st,qu,cr['content']['conditions'])
for k,ref,a,b,rel in [('e21','12a:21','c21y','q20','qualification'),('e22','12a:22','c22','q20','answer'),('e23','12a:23','c23','q20','answer'),('e24','12a:24','c24','q20','answer'),('e1','12b:1','c1','c21s','correction'),('e3','12b:3','c3doubt','q2','qualification'),('e4','12b:4','c4y','q2','qualification'),('e5e','12b:5','c5eat','q2','answer'),('e5t','12b:5','c5trade','q2','answer'),('e6d','12b:6','c6definite','q2','answer'),('e6s','12b:6','c6doubt','q2','answer'),('e8b','12b:8','c8burn','c7first','support'),('e8e','12b:8','c8eat','c7gifts','support'),('e9','12b:9','c9','c7first','objection'),('e11','12b:11','c11','q10','answer'),('e12','12b:12','c12','c11','support'),('e13h','12b:13','c13hallah','q13','answer'),('e13f','12b:13','c13first','q13','answer'),('e15','12b:15','c14','c15suspect','support'),('e15g','12b:15','c15general','c15narrow','objection')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Disqualified sacred and seventh-year redemption cases; initial tannaitic scope corrected by new deer/gazelle ground. Definite/doubtful redemption, firstborn status, priestly gifts and hallah are separate predicates. Priestly suspicion is the source’s stated concern, not an independent generalization about people.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read12a20–13a26 and omission reread12a20–12b15. Cross-page corrected scope, definite/doubtful conditions, eating/burning/commerce grounds, hallah challenge and restricted analogy, observed redemption and suspicion qualification preserved. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch28_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch28_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch28_receipt.json',r.encoded(out));print(r.encoded(out).decode())
