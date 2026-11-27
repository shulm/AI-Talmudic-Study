from pathlib import Path
exec((Path(__file__).parent.parent/'worker_20261126/batch001.py').read_text(encoding='utf-8').split("add('s.baraita'")[0])
prefix='kt.wave3.b8.';core=['13b:'+str(n) for n in range(11,17)]
add('s.majority','structure',['13b:11'],dict(title='Credibility positions persist across opposite majorities',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
add('s.child','structure',core[1:],dict(title='Woman and daughter presumptions; shetuki without general disqualification',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('13b:11','anonymous question and Rabbi Yehoshua ben Levi','majority distinction and both tannaitic positions'),('13b:12','Rabbi Yohanan and Rabbi Eleazar','daughter-status disagreement'),('13b:13','Rabbah','different presumptions for mother and daughter'),('13b:14','Rabbi Eleazar to Rabbi Yohanan and reply','shetuki objection and eligible interpretation'),('13b:15','anonymous question and Shmuel quotation','eligible shetuki example'),('13b:16','anonymous analysis and scriptural derivation','inheritance reading rejected and priestly status restriction')]:add('u.'+ref,'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
qmaj=q('majority','13b:11','ותיפוק ליה דהתם רוב פסולין אצלה והכא רוב כשרין אצלה','Why not distinguish captivity’s ineligible majority from the present case’s eligible majority?')
cmv=claim('validate_majority','13b:11','לדברי המכשיר מכשיר אפילו ברוב פסולין','Rabbi Yehoshua ben Levi says the validating position validates even where most are ineligible for her.',['Validating tannaitic position','Majority ineligible for her'],holder=['רבי יהושע בן לוי'])
cmd=claim('reject_majority','13b:11','לדברי הפוסל פוסל אפילו ברוב כשרים','He says the disqualifying position disqualifies even where most are eligible for her.',['Disqualifying tannaitic position','Majority eligible for her'],holder=['רבי יהושע בן לוי'])
edge('majority_validate_answer','13b:11','מסייע ליה לרבי יהושע בן לוי',cmv,qmaj,'answer');edge('majority_reject_answer','13b:11','פוסל אפילו ברוב כשרים',cmd,qmaj,'answer')
cyv=claim('yohanan_validate','13b:12','לדברי המכשיר בה מכשיר בבתה','Rabbi Yohanan says the position validating the mother validates her daughter.',['Mother validated'],holder=['רבי יוחנן'])
cyd=claim('yohanan_reject','13b:12','לדברי הפוסל בה פוסל בבתה','Rabbi Yohanan says the position disqualifying the mother disqualifies her daughter.',['Mother disqualified'],holder=['רבי יוחנן'])
ced=claim('eleazar_child','13b:12','ורבי אלעזר אומר לדברי המכשיר בה פוסל בבתה','Rabbi Eleazar says even the position validating the mother disqualifies her daughter.',['Mother validated'],holder=['רבי אלעזר'])
qwhy=q('eleazar_reason','13b:13','מ"ט דר"א','Rabbah asks the reason for Rabbi Eleazar’s view.')
cmother=claim('mother_presumption','13b:13','בשלמא איהי אית לה חזקה דכשרות','The mother has a prior presumption of eligibility.',['Mother'],holder=['רבה'],status='Rabbah’s explanation of Rabbi Eleazar')
cdaughter=claim('daughter_no_presumption','13b:13','בתה לית לה חזקה דכשרות','The daughter lacks that prior presumption of eligibility.',['Daughter'],holder=['רבה'],status='Rabbah’s explanation of Rabbi Eleazar')
edge('mother_reason','13b:13','איהי אית לה חזקה דכשרות',cmother,qwhy,'answer');edge('daughter_reason','13b:13','בתה לית לה חזקה דכשרות',cdaughter,qwhy,'answer');edge('daughter_support','13b:13','בתה לית לה חזקה דכשרות',cdaughter,ced,'support')
cquote=claim('shetuki_quote','13b:14','בד"א בעדות אשה בגופה אבל עדות אשה בבתה דברי הכל הולד שתוקי','Rabbi Eleazar quotes the teaching that limits the dispute to the woman and calls the child a shetuki according to all.',['Woman’s testimony about her child'],holder=['quoted teaching'],status='Repeated source occurrence used as objection')
qbad=q('shetuki_disqualified','13b:14','מאי לאו שתוקי ופסול','Does shetuki here not mean disqualified?')
cgood=claim('shetuki_eligible','13b:14','לא שתוקי וכשר','The reply interprets the child as shetuki yet eligible.',['Interpretation of quoted teaching'],holder=['reply to רבי אלעזר'],status='Defends Rabbi Yohanan; eligibility not equated with unrestricted priestly status')
edge('child_objection','13b:14','איתיביה ר"א לרבי יוחנן',cquote,cyv,'objection');edge('eligible_answer','13b:14','לא שתוקי וכשר',cgood,qbad,'answer')
qexists=q('eligible_possible','13b:15','ומי איכא שתוקי כשר','Can there be an eligible shetuki?')
cexample=claim('ten_priests','13b:15','עשרה כהנים עומדים ופירש אחד מהם ובעל הולד שתוקי','Shmuel describes ten priests, one of whom separated and had intercourse: the child is termed shetuki.',['Ten priests','One unidentified priest separates and has intercourse'],holder=['שמואל'],status='Example supporting eligibility despite unidentified paternal identity')
edge('example_answer','13b:15','אין כדשמואל',cexample,qexists,'answer')
qmeaning=q('shetuki_meaning','13b:16','מאי שתוקי','What restriction does shetuki denote in that example?')
cinherit=claim('inheritance_hypothesis','13b:16','אילימא שמשתיקין אותו מנכסי אביו','A proposed reading would silence the child’s claim to the father’s estate.',['Unidentified father among ten priests'],mode='rejected',holder=['anonymous hypothesis'],status='Rejected as the informative meaning because the father’s identity is unknown anyway')
qobvious=q('inheritance_obvious','13b:16','פשיטא ומי ידעינן אבוה מנו','Would that not be obvious, since the father is unknown?')
cpriest=claim('priesthood','13b:16','אלא שמשתיקין אותו מדין כהונה','Instead, the child is excluded from priestly status.',['Father known only as one of ten priests','No identified paternal lineage'],holder=['anonymous explanation'])
cverse=claim('identified_lineage','13b:16','מי שזרעו מיוחס אחריו יצא זה שאין זרעו מיוחס אחריו','The discussion derives the restriction from the priestly covenant verse: the offspring must be identifiable as following its father, excluding this case.',['Priestly status','Identified paternal lineage required in this derivation'],holder=['anonymous scriptural derivation'])
edge('inheritance_objection','13b:16','פשיטא ומי ידעינן אבוה מנו',qobvious,cinherit,'objection');edge('priesthood_answer','13b:16','אלא שמשתיקין אותו מדין כהונה',cpriest,qmeaning,'answer');edge('verse_support','13b:16','דכתיב (במדבר כה, יג)',cverse,cpriest,'support')
for key,ref,quote,surf,role,scope in [('ybl','13b:11','רבי יהושע בן לוי','רבי יהושע בן לוי','speaker','Majority-independent scope of both tannaitic positions; not Rabbi Yehoshua'),('yohanan','13b:12','רבי יוחנן','רבי יוחנן','speaker','Mother/daughter status follows same ruling'),('eleazar','13b:12','רבי אלעזר','רבי אלעזר','speaker','Daughter disqualified even when mother validated'),('rabbah','13b:13','אמר רבה','רבה','speaker','Presumption distinction; Rabbah not Rava'),('eleazar_objection','13b:14','איתיביה ר"א לרבי יוחנן','רבי אלעזר','speaker','Objection to Rabbi Yohanan'),('shmuel','13b:15','דאמר שמואל','שמואל','quoted_authority','Ten-priests example')]:attr(key,ref,quote,surf,role,[surf],scope)
for x in records:
 if x['layer']=='claims':x['content']['scope']='Majority conditions and daughter/shetuki eligibility, Ketubot13b:11–16'
coverage=[]
for ref in core:
 sid=byref[ref]['id']
 for layer in r.LAYERS:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  rationale='Manual '+layer+' pass over '+ref+'; '+('reread both majority directions, mother/daughter disagreement and presumption distinction, repeated shetuki teaching, eligible interpretation, ten-priests example and rejected inheritance versus priesthood conclusion' if layer=='reconciliation' else 'eligibility and priestly status not conflated; explicit conditions preserved')
  if not ids:rationale+='; no additional supported finding in this layer'
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=r.current(job)['open_tails'])
r.validate_apply(r.current(job),p,segments,j);path=out/'batch008_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'batch008_receipt.json',r.encoded(receipt));print(receipt)
