"""Source-read obligations, replacements, delayed offerings, coercion, and charity."""
from pathlib import Path
helper=Path(__file__).with_name('build_batch_005.py').read_text(encoding='utf-8').split("refs=['2b:'")[0]
exec(compile(helper.replace('rh_packet_next.json','rh_packet_008.json').replace('rh.e3.b005.','rh.e3.b008.'),str(__file__),'exec'))
refs=['5b:'+str(i) for i in range(2,17)]+['6a:'+str(i) for i in range(1,16)]
add('s1','structure','5b:2',{'title':'Scope of the delay verse: freewill gifts, replacements, and consequences of delay','primary':True,'boundary':'closed','legacy_ids':[]})
p['records'][-1]['evidence']=[ev(r) for r in refs[:19]]
add('s2','structure','6a:5',{'title':'Spoken obligations, court enforcement, and immediate charity deadline','primary':True,'boundary':'closed','legacy_ids':[]})
p['records'][-1]['evidence']=[ev(r) for r in refs[19:]]
voices={
'5b:2':('anonymous Gemara introducing baraita','Source inquiry and freewill-gift question'),
'5b:3':('baraita','Verbal-equivalence inclusion'),
'5b:4':('baraita','Three verse-clause interpretations'),
'5b:5':('baraita','Charity and field gifts plus delayed-offering consequence'),
'5b:6':('anonymous Gemara','Question about replacement exclusion and first rejected candidate'),
'5b:7':('anonymous Gemara','Second rejected candidate and thanksgiving proposal'),
'5b:8':('רבי חייא cited','Unidentifiable thanksgiving/substitution mixture'),
'5b:9':('anonymous Gemara','Exhaustive bread/no-bread dilemma'),
'5b:10':('anonymous Gemara','Redundancy objection to thanksgiving interpretation'),
'5b:11':('רב ששת','Replacement-clock interpretation and rejected cumulative-count hypothesis'),
'5b:12':('anonymous Gemara; רבא','Rabbi Meir compatibility question and within-festival case'),
'5b:13':('anonymous Gemara; אחרים quoted','Redundancy objection and firstborn-invalidity question'),
'5b:14':('אחרים in quoted baraita','Firstborn/tithe analogy'),
'5b:15':('anonymous Gemara','Need for additional sacrificial-acceptance rule'),
'5b:16':('anonymous Gemara','Objection connector continuing across folio'),
'6a:1':('anonymous Gemara; בן עזאי quoted','Alternative source objection continuing into next segment'),
'6a:2':('בן עזאי in baraita','Exclusion of delayed vows from nonacceptance'),
'6a:3':('anonymous Gemara','Reinterpretation concerning wife'),
'6a:4':('anonymous Gemara; רבי יוחנן or רבי אלעזר quoted','Reason for wife exclusion; unresolved named variant'),
'6a:5':('baraita','Clause-by-clause spoken-obligations exegesis'),
'6a:6':('anonymous Gemara','Two duplicate-source questions'),
'6a:7':('anonymous Gemara; baraita quoted','Court-coercion redundancy and willingness qualification'),
'6a:8':('anonymous Gemara','Two unassigned cases distinguish sources'),
'6a:9':('anonymous Gemara','First direction of necessity argument'),
'6a:10':('anonymous Gemara','Converse necessity argument'),
'6a:11':('anonymous Gemara; Mishnah quoted','Freewill-gift objection and vow/gift definitions'),
'6a:12':('quoted Mishnah','Replacement liability distinction'),
'6a:13':('רבא','Vow with express no-liability condition'),
'6a:14':('רבא','Immediate charity deadline and available-poor rationale'),
'6a:15':('anonymous Gemara','Obviousness question and sacrifice analogy rejected')}
for ref,(voice,role) in voices.items():add('u.'+ref,'utterances',ref,{'textual_voice':voice,'discourse_role':role,'composition':'composite'})
q('q1','5b:2','What establishes the listed obligations under the delay prohibition?','מנהני מילי')
q('q2','5b:2','The verse names a vow; how are freewill gifts included?','אין לי אלא נדר נדבה מנין')
c('c1','5b:3','The shared word vow links the delay verse with the passage expressly combining vow and freewill gift, including freewill gifts here.',holder='anonymous baraita')
e('e1','5b:3',claims['c1'],questions['q2'],'answer')
c('c2','5b:4','The phrase “to the Lord your God” includes monetary valuations, fixed valuations, devoted property and consecrations.','לה אלהיך אלו הדמין הערכין והחרמין וההקדשות',holder='anonymous baraita')
c('c3','5b:4','“Do not delay paying it” is read as the original obligation and not its replacements.','לא תאחר לשלמו הוא ולא חילופיו',holder='anonymous baraita',status='Meaning of replacement exclusion is tested and qualified below')
c('c4','5b:4','“He will surely demand it” includes sin, guilt, burnt and peace offerings.','כי דרוש ידרשנו אלו חטאות ואשמות עולות ושלמים',holder='anonymous baraita')
c('c5','5b:5','“The Lord your God” includes charity, tithes and firstborn.','ה\' אלהיך אלו צדקות ומעשרות ובכור',holder='anonymous baraita')
c('c6','5b:5','“From you” includes gleanings, forgotten sheaves and field corners.','מעמך זה לקט שכחה ופאה',holder='anonymous baraita')
c('c7','5b:5','The initial interpretation locates sin in the person, not invalidity in his delayed offering.','והיה בך חטא ולא בקרבנך חטא',holder='anonymous baraita',status='Inference later shown redundant and replaced by wife-related reading of this verse')
for n,ref in [(2,'5b:4'),(4,'5b:4'),(5,'5b:5'),(6,'5b:5')]:e('e.scope'+str(n),ref,claims['c'+str(n)],questions['q1'],'answer')
q('q3','5b:6','Which replacements are excluded?','חילופי מאי')
c('c8','5b:6','Replacements of burnt and peace offerings can themselves be offered.','אי חילופי עולה ושלמים מקרב קרבי',status='Objection to wholesale exclusion; later reply concerns their deadline clock instead')
e('e2','5b:6',claims['c8'],claims['c3'],'objection')
c('c9','5b:7','A replacement sin offering goes to death rather than being offered.','אי חילופי חטאת למיתה אזלא')
c('c10','5b:7','The proposed referent of the replacement exclusion is a thanksgiving replacement.','אלא מאי חילופיו חילופי תודה',mode='rejected',status='Proposal defeated by 5b:10 redundancy objection')
e('e3','5b:7',claims['c10'],questions['q3'],'answer')
c('c11','5b:8','If a thanksgiving animal is mixed with its substituted animal and one dies, the surviving animal cannot be remedied.',holder='רבי חייא',conditions=['Thanksgiving animal mixed with its temurah','One dies','Survivor cannot be identified'])
a('a1','5b:8','רבי חייא','quoted_authority','Mixture rule','דתני רבי חייא')
e('e4','5b:8',claims['c11'],claims['c10'],'support')
q('q4','5b:9','How could the surviving animal be offered?','היכי ליעביד')
c('c12','5b:9','Offering the animal with bread is blocked by the possibility that it is the substituted animal.','ליקרבה וליקריב לחם בהדה דלמא תמורה היא',mode='conditional',conditions=['Survivor may be the substituted animal'])
c('c13','5b:9','Offering it without bread is blocked by the possibility that it is the original thanksgiving animal.','ליקרבה בלא לחם דלמא תודה היא',mode='conditional',conditions=['Survivor may be the original thanksgiving animal'])
e('e5','5b:9',claims['c12'],claims['c11'],'support');e('e6','5b:9',claims['c13'],claims['c11'],'support')
q('q5','5b:10','If it cannot be offered at all, why is a verse required to exclude it from delay?')
e('e7','5b:10',questions['q5'],claims['c10'],'objection')
c('c14','5b:11','Rav Sheshet restores burnt/peace replacements as the referent: after two festivals the original becomes blemished and is redeemed onto another animal, followed by one more festival.','אמר רב ששת לעולם למעוטי חילופי עולה ושלמים והכא במאי עסקינן כגון שעברו עליו שני רגלים והומם וחיללו על אחר ועבר עליו רגל אחד',holder='רב ששת',conditions=['Original passed two festivals','Original became blemished','Redeemed onto another','Replacement passed one festival'])
c('c15','5b:11','The excluded inference would combine the original’s two festivals with the replacement’s one; their derivational connection does not make three festivals pass for the replacement.','סלקא דעתך אמינא הואיל ומכח קמא קאתי כמאן דעברו עליו ג\' רגלים דמי קמ"ל',holder='רב ששת',status='Cumulative-count hypothesis explicitly rejected')
a('a2','5b:11','רב ששת','speaker','Clock-reset case','אמר רב ששת')
e('e8','5b:11',claims['c14'],questions['q3'],'answer');e('e9','5b:11',claims['c15'],claims['c3'],'qualification')
q('q6','5b:12','How does the exclusion work for Rabbi Meir’s one-festival threshold?','ולרבי מאיר דאמר כיון שעבר עליו רגל א\' עובר בבל תאחר מאי איכא למימר')
c('c16','5b:12','Rava sets the case within a festival: the original becomes blemished and is redeemed, and the remainder of that festival passes.','אמר רבא הכא במאי עסקינן כגון שהומם בתוך הרגל וחיללו ועבר עליו הרגל',holder='רבא',conditions=['Rabbi Meir one-festival rule','Blemish and redemption within festival'])
c('c17','5b:12','The replacement is not treated as having passed the whole festival merely because it derives from the original.','סלקא דעתך אמינא הואיל ומכח קמא קאתי כמאן דעבר עליה כוליה רגל דמי קמ"ל',holder='רבא',status='Whole-festival aggregation hypothesis explicitly rejected')
a('a3','5b:12','רבא','speaker','Within-festival replacement case','אמר רבא')
e('e10','5b:12',claims['c16'],questions['q6'],'answer');e('e11','5b:12',claims['c17'],claims['c3'],'qualification')
q('q7','5b:13','Is delayed-offering validity already derived from the teaching of Others?','והא מהכא נפקא מדאחרים נפקא')
q('q8','5b:13','Could a firstborn whose year has passed be invalid like disqualified consecrated animals?','יכול יהא בכור שעברה שנתו כפסולי המוקדשין ויפסל')
a('a4','5b:13','אחרים','collective','Baraita on firstborn validity','דתניא אחרים אומרים')
c('c18','5b:14','Others compare firstborn with tithe: as tithe is not invalidated when one year passes into the next, neither is firstborn.',holder='אחרים',conditions=['Firstborn year passed'])
e('e12','5b:14',claims['c18'],questions['q8'],'answer');e('e13','5b:13',questions['q7'],claims['c7'],'objection')
c('c19','5b:15','An additional rule was thought necessary because firstborn is not an atoning offering, whereas offerings that secure acceptance might otherwise cease to do so after delay.',status='Necessity argument challenged by Ben Azzai teaching',conditions=['Distinguish firstborn from offerings that secure acceptance'])
e('e14','5b:15',claims['c19'],questions['q7'],'answer')
q('q9','6a:1','Is validity despite delay already established by Ben Azzai?','מדבן עזאי נפקא')
p['records'][-1]['evidence'].insert(0,ev('5b:16'))
a('a5','6a:1','בן עזאי','quoted_authority','Restriction using אותו','דתניא בן עזאי אומר')
q('q10','6a:2','What does the restrictive אותו teach?','מה ת"ל')
c('c20','6a:2','Ben Azzai restricts nonacceptance to the offering indicated by אותו; delayed vows are not disqualified from acceptance.','ת"ל אותו אותו בלא ירצה ואין מאחר נדרו בלא ירצה',holder='בן עזאי')
c('c21','6a:2','One might infer from the delay prohibition that delaying a vow also makes the offering unacceptable.','לפי שנא\' (דברים כג, כב) לא תאחר לשלמו שומע אני אף מאחר נדרו בבל ירצה',holder='Ben Azzai’s presented hypothesis',mode='rejected',status='Excluded by אותו')
e('e15','6a:1',questions['q9'],claims['c19'],'objection');e('e16','6a:2',claims['c20'],questions['q10'],'answer');e('e17','6a:2',claims['c20'],claims['c21'],'correction')
c('c22','6a:3','The verse is instead interpreted as locating the sin in the delayer, not his wife.',status='Replacement interpretation of בך חטא')
e('e18','6a:3',claims['c22'],claims['c7'],'correction')
c('c23','6a:4','Rabbi Yohanan, or alternatively Rabbi Elazar, is reported as saying a man’s wife dies only when money is demanded from him and he has none.','אין אשתו של אדם מתה אא"כ מבקשין ממנו ממון ואין לו',holder='רבי יוחנן or רבי אלעזר (unresolved variant)',conditions=['Money demanded','He has none'],status='Quoted aggadic statement, not a verified general causal claim',uncertainty=['Alternative speaker attribution is explicit.'])
c('c24','6a:4','The imagined extension that his wife dies for his delay violation is rejected.','אימא בהאי עון דבל תאחר נמי אשתו מתה קמ"ל',mode='rejected',status='Explains need for wife-related exclusion')
a('a6','6a:4','רבי יוחנן ואי תימא רבי אלעזר','quoted_authority','Money-demand statement; no forced resolution','וא"ר יוחנן ואי תימא ר\' אלעזר',candidates=['רבי יוחנן','רבי אלעזר'])
e('e19','6a:4',claims['c22'],claims['c24'],'correction')
c('c25','6a:5','“What leaves your lips” establishes a positive command.','מוצא שפתיך זו מצות עשה',holder='anonymous baraita')
c('c26','6a:5','“Guard” establishes a negative command.','תשמור זו מצות לא תעשה',holder='anonymous baraita')
c('c27','6a:5','“Do” instructs the court to compel performance.','ועשית אזהרה לב"ד שיעשוך',holder='anonymous baraita')
c('c28','6a:5','“As you vowed” refers to a vow.','כאשר נדרת זה נדר',holder='anonymous baraita')
c('c29','6a:5','“To the Lord your God” includes sin, guilt, burnt and peace offerings.','לה\' אלהיך אלו חטאות ואשמות עולות ושלמים',holder='anonymous baraita')
c('c30','6a:5','“Freewill gift” has its ordinary meaning.','נדבה כמשמעו',holder='anonymous baraita')
c('c31','6a:5','“Which you spoke” includes sanctities dedicated to temple maintenance.','אשר דברת אלו קדשי בדק הבית',holder='anonymous baraita')
c('c32','6a:5','“With your mouth” includes charity.','בפיך זו צדקה',holder='anonymous baraita')
q('q11','6a:6','Why derive the positive command here when coming and bringing already establish it?','מוצא שפתיך זו מצות עשה למה לי (דברים יב, ה) מובאת שמה והבאתם שמה נפקא')
q('q12','6a:6','Why derive the negative command here when the explicit prohibition of delay already establishes it?','תשמור זו מצות לא תעשה למה לי מלא תאחר לשלמו נפקא')
e('e20','6a:6',questions['q11'],claims['c25'],'objection');e('e21','6a:6',questions['q12'],claims['c26'],'objection')
q('q13','6a:7','Why derive court compulsion here when יקריב אותו already teaches it?','ועשית אזהרה לב"ד שיעשוך למה לי מיקריב אותו נפקא')
q('q14','6a:7','Could offering be compelled against his will?','יכול בעל כרחו')
q('q15','6a:7','How are coercion and willingness reconciled?','הא כיצד')
c('c33','6a:7','The baraita reads יקריב אותו as permitting coercion and לרצונו as requiring willingness; he is compelled until he says “I want to”.','דתניא (ויקרא א, ג) יקריב אותו מלמד שכופין אותו יכול בעל כרחו ת"ל (ויקרא א, ג) לרצונו הא כיצד כופין אותו עד שיאמר רוצה אני',holder='anonymous baraita',conditions=['He eventually says רוצה אני'])
e('e22','6a:7',questions['q13'],claims['c27'],'objection');e('e23','6a:7',claims['c33'],questions['q15'],'answer')
c('c34','6a:8','The duplicate sources cover two cases: one spoke but did not designate, and one designated but did not offer.',status='Sources not individually assigned by their order',conditions=['Spoken promise without designation OR designation without offering'])
for n in [11,12,13]:e('e.dup'+str(n),'6a:8',claims['c34'],questions['q'+str(n)],'answer')
c('c35','6a:9','If only unfulfilled speech were taught, designation without offering might be exempt on the theory that the object is already in God’s treasury wherever located.',mode='rejected',conditions=['Designated but did not offer'],status='Hypothetical exemption rejected by the need for both cases')
c('c36','6a:10','If only withholding a designated offering were taught, a mere spoken promise might be treated as insignificant.',mode='rejected',conditions=['Spoke but did not designate'],status='Converse hypothetical exemption rejected')
e('e24','6a:9',claims['c35'],claims['c34'],'support');e('e25','6a:10',claims['c36'],claims['c34'],'support')
q('q16','6a:11','Can the passage concern speech without designation when it expressly includes a freewill gift?','ומי מצית אמרת דאמר ולא אפריש והא נדבה כתיבא')
c('c37','6a:11','The Mishnah defines a vow as “a burnt offering is incumbent on me”.','אי זהו נדר האומר הרי עלי עולה',holder='quoted Mishnah')
c('c38','6a:11','It defines a freewill gift as “this is a burnt offering”.','ואי זו היא נדבה האומר הרי זו עולה',holder='quoted Mishnah')
e('e26','6a:11',questions['q16'],claims['c34'],'objection')
q('q17','6a:12','What distinguishes a vow from a freewill gift?','ומה בין נדר לנדבה')
c('c39','6a:12','For a vow, if the animal dies or is stolen the donor remains responsible for replacement.','נדר מת או נגנב חייב באחריותו',holder='quoted Mishnah',conditions=['Vow','Animal died or stolen'])
c('c40','6a:12','For a freewill gift, if the animal dies or is stolen there is no replacement liability.','נדבה מתה או נגנבה אינו חייב באחריותה',holder='quoted Mishnah',conditions=['Freewill gift','Animal died or stolen'])
e('e27','6a:12',claims['c39'],questions['q17'],'answer');e('e28','6a:12',claims['c40'],questions['q17'],'answer')
c('c41','6a:13','Rava supplies a spoken obligation expressly conditioned on no replacement liability: a burnt offering is incumbent on me provided I am not responsible for it.',holder='רבא',conditions=['Explicit stipulation of no replacement liability'])
a('a7','6a:13','רבא','speaker','Qualified הרי עלי formulation','אמר רבא')
e('e29','6a:13',claims['c41'],questions['q16'],'answer')
c('c42','6a:14','Rava says charity becomes due immediately because poor recipients are present.','אמר רבא וצדקה מיחייב עלה לאלתר מ"ט דהא קיימי עניים',holder='רבא',conditions=['Poor recipients available'])
q('q18','6a:14','Why is charity due immediately?','מ"ט')
a('a8','6a:14','רבא','speaker','Immediate charity deadline','אמר רבא')
e('e30','6a:14',claims['c42'],questions['q18'],'answer')
q('q19','6a:15','Is the immediate charity deadline not obvious?','פשיטא')
c('c43','6a:15','One might have imposed the three-festival sacrificial deadline on charity because they appear in the same passage.','מהו דתימא כיון דבעניינא דקרבנות כתיבא עד דעברי עלה ג\' רגלים כקרבנות',mode='rejected',status='Sacrificial analogy rejected')
c('c44','6a:15','The Torah ties sacrifices to festivals, but charity is not delayed that way because poor recipients are available.','קמ"ל התם הוא דתלינהו רחמנא ברגלים אבל הכא לא דהא שכיחי עניים',conditions=['Poor recipients available'])
e('e31','6a:15',claims['c44'],claims['c43'],'distinction');e('e32','6a:15',claims['c43'],questions['q19'],'answer')
for r in p['records']:
 if r['layer']=='claims':r['content']['scope']='Local exegesis of delayed obligations, replacement clocks, sacrificial acceptance, compulsion and charity; quoted aggadah retains source status'
for ref in refs:
 sid=segments[ref]['id']
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if r['layer']==layer and any(v['segment_id']==sid for v in r['evidence'])]
  rationale='Source read through 6b:15. Continuations, rejected replacements, liability conditions, quoted aggadah and alternative attribution kept separate.'
  if layer=='reconciliation':rationale='Second source-based omission pass checked verse clauses, full bread dilemma, both replacement clocks, redundant-source corrections, liability conditions and immediate charity qualification. Review remains unfinished.'
  elif not ids:rationale={'attributions':'No new named attribution in this anonymous or continued baraita segment; voice represented in utterances.','questions':'No explicit question after source reading.','claims':'Question or cross-folio connector only; proposition in continuation.','positions':'No distinct asserted position in this connector/question segment.','edges':'No further directed relation originates here; continuation relations carried by following evidence.'}.get(layer,rationale)
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p['open_tails']=[]
out=Path(__file__).with_name('proposal_008.json');out.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'proposal':str(out),'records':len(p['records']),'segments':len(refs)}))
