from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.benefit.20261126w3.'
assert r.sha(r.encoded(state))=='abffed147d2a19d6b213dccb748dd16df4204de45271c0bcc5fdb0e304b1889e'
refs=['9b:'+str(n) for n in range(3,19)]
add('s','structure',refs,dict(title='Benefit from unredeemed firstborn donkey: Ulla’s rationales and alternative verse dispute',primary=True,boundary='closed',legacy_ids=[]))
for n,v,role in [(3,'Anonymous Gemara','Why separate a lamb retained by owner'),(4,'Anonymous Gemara and baraita','Rabbi Yehuda prohibition versus Rabbi Shimon permission'),(5,'Ulla and anonymous objections','Redemption rationale revised'),(6,'Anonymous Gemara citing Rav Nehemya son of Rav Yosef','Equal-value redemption exception'),(7,'Anonymous Gemara citing Rabbi Yehuda','Second-tithe betrothal objection'),(8,'Anonymous Gemara citing Rabbi Elazar','Known redemption conditions'),(9,'Anonymous Gemara','Donkey value differential betrothal'),(10,'Ulla','Rabbi Shimon rationale'),(11,'Anonymous Gemara','Seventh-year produce counterexample'),(12,'Anonymous answer citing unnamed authority','Last exchange retains prohibition'),(13,'Alternative baraita: Rabbi Yehuda','Initial joint-ownership exemption reading'),(14,'Rabbi Shimon','Human work and donkey shearing exceptions'),(15,'Anonymous Gemara','Two difficulties for initial Rabbi Yehuda formulation'),(16,'Anonymous correction','Common human exemption and Rabbi Yehuda joint-ownership reading'),(17,'Anonymous exposition of Rabbi Shimon','Joint-ownership exemption leaves sheep term for donkey'),(18,'Anonymous Gemara','Possessive wording challenge unresolved')]:add('u'+str(n),'utterances',['9b:'+str(n)],dict(textual_voice=v,discourse_role=role,composition='composite'))
q('q3','9b:3','Why separate a lamb when the owner retains it?')
c('c3','9b:3','The separation removes the donkey’s prohibition.')
c('c4infer','9b:4','The passage infers that before redemption benefit is prohibited and assigns the Mishnah to Rabbi Yehuda.')
c('c4y','9b:4','The baraita’s first view prohibits benefit from a firstborn donkey, identified here as Rabbi Yehuda.')
c('c4s','9b:4','Rabbi Shimon permits benefit from it.')
q('q5','9b:5','What is Rabbi Yehuda’s reason?')
c('c5initial','9b:5','Ulla initially argues that something requiring redemption cannot be permitted beforehand.',mode='challenged')
c('c5human','9b:5','The objection gives human firstborn as requiring redemption while remaining permitted.')
c('c5seh','9b:5','The revised argument focuses on the Torah’s insistence on a seh for redemption.')
q('q6','9b:6','Does the Torah insist on a seh, given redemption with cooked vegetables at equivalent value?')
c('c6case','9b:6','Rav Nehemya son of Rav Yosef redeemed a firstborn donkey with cooked vegetables at its value.')
c('c6value','9b:6','The answer excludes equal-value redemption from the insistence argument.')
c('c6below','9b:6','The insistence on a seh concerns release from prohibition when redeeming below the donkey’s value.',cond=['Redemption not at equal value'])
c('c7coin','9b:7','The objection notes the Torah’s insistence on Tyrian money for second tithe.')
c('c7betrothal','9b:7','It cites Rabbi Yehuda’s view that intentional betrothal with second tithe takes effect.',cond=['Intentional use of second tithe for betrothal'])
c('c8donkey','9b:8','The answer says betrothal with the firstborn donkey can also take effect.')
c('c8elazar','9b:8','Rabbi Elazar explains that a woman knows second tithe is not desacralized through her acceptance and goes to eat it in Jerusalem.')
c('c9knows','9b:9','Analogously the woman knows the firstborn donkey bears a prohibition.')
c('c9redeem','9b:9','She redeems it with a seh.')
c('c9difference','9b:9','The betrothal takes effect through the remaining value difference after redemption.')
q('q10','9b:10','What is Rabbi Shimon’s reason?')
c('c10','9b:10','Ulla argues that an object whose redemption substitute is permitted should not itself be forbidden.')
c('c11','9b:11','The objection proposes seventh-year produce as forbidden while its exchanged value is permitted.',mode='challenged')
c('c12','9b:12','The answer rejects that premise: each final exchange value of seventh-year produce remains prohibited.')
c('c13work','9b:13','The alternative baraita initially reads Rabbi Yehuda’s ox verse as allowing work with jointly owned animals.',mode='challenged',cond=['Yours and others’ joint ownership'])
c('c13shear','9b:13','It initially reads his sheep verse as allowing shearing jointly owned animals.',mode='challenged',cond=['Yours and others’ joint ownership'])
c('c14human','9b:14','Rabbi Shimon reads the ox verse as permitting work with a human firstborn.')
c('c14donkey','9b:14','He reads the sheep verse as permitting shearing a firstborn donkey.')
q('q15two','9b:15','Why would Rabbi Yehuda need two verses for the same joint-ownership exclusion?')
q('q15human','9b:15','Would Rabbi Yehuda then prohibit work with a human firstborn?')
c('c16common','9b:16','The corrected account says all agree the ox term excludes human firstborn from the prohibition.')
c('c16yliable','9b:16','Rabbi Yehuda holds gentile joint ownership liable in firstborn status.')
c('c16ypermit','9b:16','For him the sheep term is needed to permit shearing and work in the joint-ownership case.',cond=['Gentile joint ownership'])
c('c17sexempt','9b:17','Rabbi Shimon holds gentile joint ownership exempt from firstborn status.')
c('c17sunneeded','9b:17','For him no verse is needed to permit shearing and work of that exempt joint-ownership case.')
c('c17sdonkey','9b:17','He therefore uses the sheep term for firstborn donkey.')
c('c18y','9b:18','For Rabbi Yehuda the sheep possessive is needed and the ox possessive follows its wording.')
q('q18','9b:18','For Rabbi Shimon why are the possessive your ox and your sheep needed?')
c('c18unresolved','9b:18','The passage leaves that wording difficulty unresolved.',mode='unresolved')
for k,ref,surf,role,cands,scope in [('a4y','9b:4',"ר' יהודה",'position_holder',['רבי יהודה'],'Benefit prohibition'),('a4s','9b:4','רבי שמעון','speaker',['רבי שמעון'],'Benefit permission'),('a5','9b:5','עולא','speaker',['עולא'],'RabbiYehuda rationale'),('a6','9b:6','רב נחמיה בריה דרב יוסף','quoted_authority',['רב נחמיה בריה דרב יוסף'],'Equivalent-value vegetable redemption'),('a7','9b:7','רבי יהודה','quoted_authority',['רבי יהודה'],'Second-tithe betrothal'),('a8','9b:8','רבי אלעזר','quoted_authority',['רבי אלעזר'],'Woman knows second-tithe restrictions'),('a10','9b:10','עולא','speaker',['עולא'],'RabbiShimon rationale'),('a12','9b:12','מר','anonymous',[],'Last seventh-year exchange prohibition'),('a13','9b:13',"ר' יהודה",'quoted_authority',['רבי יהודה'],'First verse reading subsequently corrected'),('a14','9b:14',"ר' שמעון",'speaker',['רבי שמעון'],'Human/donkey exceptions')]:att(k,ref,surf,role,cands,scope)
for k,ref,cl,h,st,qu in [('p3','9b:3','c3',['Anonymous Gemara'],'Redemption purpose','q3'),('p4y','9b:4','c4y',['רבי יהודה'],'Benefit prohibition before redemption',None),('p4s','9b:4','c4s',['רבי שמעון'],'Benefit permission before neck-breaking; continuation qualifies',None),('p5','9b:5','c5initial',['עולא'],'Initial rationale challenged','q5'),('p6','9b:6','c6below',['עולא rationale as clarified by Gemara'],'Revised scoped rationale','q5'),('p7','9b:7','c7betrothal',['רבי יהודה'],'Cited conditional ruling',None),('p9','9b:9','c9difference',['Anonymous Gemara'],'Betrothal through surplus value',None),('p10','9b:10','c10',['עולא'],'Rationale for RabbiShimon','q10'),('p13w','9b:13','c13work',['רבי יהודה'],'Initial reading corrected at9b16',None),('p13s','9b:13','c13shear',['רבי יהודה'],'Initial reading later scoped',None),('p14h','9b:14','c14human',['רבי שמעון'],'Human exception',None),('p14d','9b:14','c14donkey',['רבי שמעון'],'Donkey exception',None),('p16','9b:16','c16ypermit',['רבי יהודה'],'Corrected joint-ownership explanation',None),('p17','9b:17','c17sdonkey',['רבי שמעון'],'Donkey explanation',None),('p18','9b:18','c18unresolved',['Anonymous Gemara'],'Explicit unresolved difficulty','q18')]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,st,qu,cr['content']['conditions'])
for k,ref,a,b,rel in [('e3','9b:3','c3','q3','answer'),('e4','9b:4','c4s','c4y','distinction'),('e5','9b:5','c5initial','q5','answer'),('e5h','9b:5','c5human','c5initial','objection'),('e5r','9b:5','c5seh','c5initial','correction'),('e6q','9b:6','q6','c5seh','objection'),('e6v','9b:6','c6value','q6','answer'),('e6b','9b:6','c6below','c5seh','qualification'),('e7','9b:7','c7betrothal','c6below','objection'),('e8','9b:8','c8donkey','c7betrothal','answer'),('e9','9b:9','c9difference','c8donkey','support'),('e9a','9b:9','c8elazar','c9knows','analogy'),('e10','9b:10','c10','q10','answer'),('e11','9b:11','c11','c10','objection'),('e12','9b:12','c12','c11','objection'),('e15t','9b:15','q15two','c13work','objection'),('e15h','9b:15','q15human','c13work','objection'),('e16','9b:16','c16common','c13work','correction'),('e16h','9b:16','c16common','q15human','answer'),('e16p','9b:16','c16yliable','c16ypermit','support'),('e17p','9b:17','c17sexempt','c17sunneeded','support'),('e17d','9b:17','c17sunneeded','c17sdonkey','support'),('e18','9b:18','c18unresolved','q18','unresolved_outcome')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local pre-redemption benefit dispute and alternative derivation routes. Initial Ulla and verse formulations are preserved with corrections; equal-value redemption and value-difference betrothal scoped separately. Read neck-breaking continuation9b19–10a12 before treating RabbiShimon permission as unrestricted.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read9b3–10a12 and omission reread9b3–18. Redemption-value conditions, second-tithe analogy, seventh-year objection, alternative verse route and corrected shared human exemption retained. Final possessive-wording difficulty explicitly unresolved. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch22_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch22_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch22_receipt.json',r.encoded(out));print(r.encoded(out).decode())
