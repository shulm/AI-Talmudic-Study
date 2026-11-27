from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.audibility_megillah.20261127e5.'
assert r.sha(r.encoded(state))=='98a399595c2c59cb505df23a1681c1b0c1ab6f6e2b9b40c65e13d031a33d4173'
refs=['15a:'+str(i) for i in range(24,27)]+['15b:'+str(i) for i in range(1,19)]
for k,rr,title in [('megillah',refs[:14],'Megillah eligibility and alternative tannaitic assignments'),('law',refs[14:17],'Initial audibility duty with retrospective validity'),('joseph',refs[17:],'Correction of Rav Yosef’s other-commandments report')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Megillah Mishnah citation','Rav Mattana attribution and cited Shema dispute','Anonymous challenge begins','Alternative Rabbi Yehuda attribution','Anonymous rebuttal by grouping','Anonymous counterpossibility','Anonymous rebuttal from Rabbi Yehuda’s final clause','Proposed reconstructed Mishnah with two minors','Challenge from terumah baraita','Incompatibility under assumed positions','Revised assumption and blessing-after-meals challenge','Incompatibility under revised positions','Teacher/student reconciliation with Rabbi Meir reply','Alternative reconciliation','Rav Hisda reporting Rav Shila','Explanation of first ruling’s necessity','Explanation of second ruling’s necessity','Initial Rav Yosef report','Objection and explicitly corrected Rav Yosef report','Anonymous verse objection','Anonymous Torah-study distinction']
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Dialectical attribution, ruling or correction',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('24first','15a:24','The cited Mishnah permits all to read Megillah except a deaf person, a person lacking legal competence and a minor.',['Anonymous Megillah Mishnah'])
claim('24yehuda','15a:24','Rabbi Yehuda permits a minor to read Megillah.',['Rabbi Yehuda'])
q('q25','15a:25','Who is the tanna invalidating the deaf reader even after the fact?')
claim('25','15a:25','Rav Mattana identifies Rabbi Yose by the Shema dispute over hearing one’s own recitation.',['Rav Mattana'],status='Attribution proposal questioned next')
q('q26','15a:26','Why assume Rabbi Yose and invalidity even after the fact?')
claim('1','15b:1','The counterproposal identifies Rabbi Yehuda and construes the ban as only initial, with retrospective validity.',['Anonymous Gemara'],status='Proposed alternative')
claim('2','15b:2','The rebuttal equates deafness with the listed legally incompetent person and minor, who are invalid even after the fact.',['Anonymous Gemara'],status='Argument against initial-only reading')
claim('3','15b:3','A counterpossibility lets each listed case have its own legal scope.',['Anonymous Gemara'],status='Defends possible differentiated list')
q('q4','15b:4','If the final clause explicitly says Rabbi Yehuda permits a minor, does that not imply the first clause is not Rabbi Yehuda?')
claim('5','15b:5','A proposed missing-language reconstruction assigns the whole Mishnah to Rabbi Yehuda, distinguishing a minor below education age from one who has reached it, the latter valid even initially.',['Anonymous Gemara'],status='Possible reconstructed attribution, not unequivocal final Mishnah identity',cond=['Minor below versus at education age'])
claim('6','15b:6','Rabbi Yehuda son of Rabbi Shimon ben Pazi’s baraita permits a deaf person who speaks but cannot hear to separate terumah initially.',['Rabbi Yehuda son of Rabbi Shimon ben Pazi'],status='Repeated baraita occurrence challenging provisional assignment')
q('q7','15b:7','Who fits this baraita if Rabbi Yehuda allows only after the fact and Rabbi Yose invalidates even after the fact?')
claim('8','15b:8','The discussion reconsiders Rabbi Yehuda as permitting initially but then cites the baraita forbidding grace after meals in the heart while validating it retrospectively.',['Anonymous Gemara'],status='Changed provisional assumption with new counterexample')
q('q9','15b:9','Who fits initial prohibition with retrospective validity under those assumed Rabbi Yehuda and Rabbi Yose positions?')
claim('10own','15b:10','One reconciliation gives Rabbi Yehuda his own initially permissive view and his teacher a requirement to make Shema audible.',['Anonymous Gemara'],status='Teacher/student distinction as one retained solution')
claim('10teacher','15b:10','Rabbi Yehuda reports Rabbi Eleazar ben Azariah requiring the Shema reader to make the words audible to the ear.',['Rabbi Eleazar ben Azariah'])
claim('10meir','15b:10','Rabbi Meir responds from upon your heart that matters follow the heart’s intention.',['Rabbi Meir'])
claim('11','15b:11','Alternatively Rabbi Yehuda may follow his teacher, with the conflicting traditions assigned to Rabbi Yehuda and Rabbi Meir.',['Anonymous Gemara'],status='Alternative solution, not erasure of first solution')
claim('12teacher','15b:12','Rav Shila through Rav Hisda rules like Rabbi Yehuda’s report of Rabbi Eleazar ben Azariah.',['Rav Shila'],status='Initial audibility duty clarified13')
claim('12yehuda','15b:12','The same chain also rules like Rabbi Yehuda himself.',['Rav Shila'],status='Retrospective validity clarified14')
claim('13','15b:13','Without the teacher-report ruling, Rabbi Yehuda’s ruling might be understood to permit initially; both are needed to prevent that inference.',['Anonymous Gemara'])
claim('14','15b:14','Without Rabbi Yehuda’s own ruling, the audibility requirement might be understood to leave no remedy; the second ruling establishes retrospective validity.',['Anonymous Gemara'])
claim('15','15b:15','The initial report has Rav Yosef place disagreement in Shema but unanimous invalidity in other commandments, citing hasket u-shema.',['Rav Yosef'],status='Explicitly corrected report; not final attributed teaching')
claim('16baraita','15b:16','The baraita of grace after meals in the heart, forbidden initially but valid if done, objects to universal invalidity for other commandments.',['Anonymous Gemara citing baraita'],status='Counterexample to initial report')
claim('16correct','15b:16','The corrected report has Rav Yosef locate the dispute in Shema because it says Shema Israel, but unanimous validity in other commandments.',['Rav Yosef'],status='Explicit corrected formulation; validity not initial permission')
q('q17','15b:17','What about hasket u-shema Israel?')
claim('18','15b:18','That verse concerns Torah study.',['Anonymous Gemara'])
for k,ref,surface,name in [('24','15a:24','רבי יהודה','רבי יהודה'),('25','15a:25','רב מתנה','רב מתנה'),('10m','15b:10',"ר' מאיר",'רבי מאיר'),('15','15b:15','רב יוסף','רב יוסף'),('16','15b:16','רב יוסף','רב יוסף')]:att('a'+k,ref,surface,'speaker',[name],'Named rule, attribution or explicitly corrected report')
att('a6','15b:6',"ר"+'"'+"י בריה דר' שמעון בן פזי",'transmitter',['רבי יהודה בריה דרבי שמעון בן פזי'],'Baraita reciter; not automatically original position holder')
att('a10','15b:10',"ר יהודה משום ר' אלעזר בן עזריה",'transmitter',['רבי יהודה'],'Teacher report',chain=['רבי יהודה','רבי אלעזר בן עזריה'])
att('a12','15b:12','ר חסדא אמר רב שילא','transmitter',['רב חסדא'],'Two complementary rulings',chain=['רב חסדא','רב שילא'])
for k,ref,a,b,rel in [('24','15a:24','c24yehuda','c24first','qualification'),('25','15a:25','c25','q25','answer'),('26','15a:26','q26','c25','objection'),('1','15b:1','c1','q26','answer'),('2','15b:2','c2','c1','objection'),('3','15b:3','c3','c2','objection'),('4','15b:4','q4','c1','objection'),('5','15b:5','c5','q4','answer'),('7','15b:7','q7','c1','objection'),('7s','15b:7','c6','q7','support'),('8','15b:8','c8','q7','answer'),('9','15b:9','q9','c8','objection'),('10','15b:10','c10own','q9','answer'),('10s','15b:10','c10teacher','c10own','support'),('10m','15b:10','c10meir','c10teacher','distinction'),('11','15b:11','c11','c10own','distinction'),('13','15b:13','c13','c12teacher','support'),('14','15b:14','c14','c12yehuda','support'),('16b','15b:16','c16baraita','c15','objection'),('16c','15b:16','c16correct','c15','correction'),('17','15b:17','q17','c16correct','objection'),('18','15b:18','c18','q17','answer')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Repeated audibility dialectic in Megillah context, complementary practical rulings and corrected Rav Yosef report. Retain each occurrence and provisional attribution without collapsing into a single asserted tannaitic identity.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read15a24–16a23; reread core15a24–15b18 for deaf/minor initial-versus-retrospective distinction, two-age reconstructed Mishnah, repeated terumah and blessing counterexamples, both teacher/student solutions, complementary Rav Shila rulings and exact reversal of Rav Yosef report with Torah-study verse distinction. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch29_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch29_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch29_receipt.json',r.encoded(out));print(r.encoded(out).decode())
