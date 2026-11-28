from pathlib import Path
exec((Path(__file__).parent/'batch001.py').read_text(encoding='utf-8').split("add('s.baraita'")[0])
prefix='kt.resume26.b3.'
state=r.current(job);old=next(x for x in state['records'] if x['id']=='kt.resume26.b2.s.mourning')
revised={k:v for k,v in old.items() if k not in ['release_state','review_state','ml_eligible']};revised=dict(revised,id=prefix+'s.bereavement_closed',supersedes=old['id'],content=dict(old['content'],boundary='closed',title='Prepared-feast bereavement baraita and market qualifications'))
records.append(revised)
core=['4a:'+str(n) for n in range(7,11)]+['4b:'+str(n) for n in range(1,11)]
ss=add('s.separation','structure',core,dict(title='Mourning and menstrual separation: private mourning, spouses, and exceptional leniency',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
add('e.continuation','edges',['4a:7'],dict(source_id=ss,target_id=revised['id'],relation='continuation',explicitness='editorial_reconstruction'),links=[ss,revised['id']],origin='editorial_inference')
for ref,voice,role in [('4a:7','anonymous discussion and Rabbi Yohanan','cited rule and supporting inference'),('4a:8','Rav Yosef son of Rava reporting Rava','qualification subsequently assigned to menstruation'),('4a:9','anonymous discussion','objection and restriction of reported rule'),('4a:10','anonymous discussion','objection from parallel wording'),('4b:1','anonymous discussion','interpretive restatement'),('4b:2','anonymous discussion','inference posed for challenge'),('4b:3','Rabbi Yitzhak bar Hanina reporting Rav Huna; anonymous quoted baraita','contrasting restrictions'),('4b:4','anonymous discussion','distinction between spouses’ mourning'),('4b:5','anonymous discussion','objection and restricted reading'),('4b:6','anonymous discussion quoting baraita','challenge to spouse distinction'),('4b:7','anonymous discussion and Rav addressing Hiyya his son','revised reading, objections and replies, illustrative instruction'),('4b:8','Rav Ashi','alternative distinction'),('4b:9','anonymous discussion citing Rabbi Eliezer and Rabbi Yehoshua','question and rejected identification of leniency'),('4b:10','anonymous discussion','identification of leniency')]:
 add('u.'+ref,'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
cj=claim('private','4a:7','דאמר רבי יוחנן אע"פ שאמרו אין אבילות במועד אבל דברים של צינעא נוהג','Rabbi Yohanan says that although mourning is not practiced during a festival, private matters of mourning are observed.',['During a festival','Private mourning matters'],holder=['רבי יוחנן'])
attr('yohanan','4a:7','דאמר רבי יוחנן','רבי יוחנן','quoted_authority',['רבי יוחנן'],'Private mourning during festival')
edge('support_private','4a:7','מסייע ליה לרבי יוחנן', 'kt.resume26.b2.c.sleep_repeat',cj,'support')
cn=claim('notconsummated','4a:8','ל"ש אלא שלא בעל אבל בעל אשתו ישנה עמו','Rava’s reported restriction requires separate sleeping only before consummation; after intercourse his wife sleeps with him.',['Menstrual case, as explicitly limited in 4a:9','Intercourse has already occurred for the permission'],holder=['רבא'],status='Initially unstated referent resolved in continuation to menstruation')
attr('yosef','4a:8','דרש רב יוסף בריה דרבא משמיה דרבא','רב יוסף בריה דרבא','transmitter',['רב יוסף בריה דרבא'],'Prior-intercourse qualification',['רב יוסף בריה דרבא','רבא'])
attr('rava','4a:8','משמיה דרבא','רבא','quoted_authority',['רבא'],'Prior-intercourse qualification',['רב יוסף בריה דרבא','רבא'])
qo=q('consummated','4a:9','והא הכא דבבעל עסקינן וקתני הוא ישן בין האנשים והיא ישנה בין הנשים','Does the bereavement case not already involve intercourse yet require separate sleeping?',['Proposed application of Rava’s statement to bereavement'])
ca=claim('menstrual_referent','4a:9','כי קאמר אפירסה אשתו נדה','The reported qualification concerns a wife who becomes menstruant.',['Referent of Rava’s prior-intercourse qualification'])
edge('prior_objection','4a:9','והא הכא דבבעל עסקינן וקתני הוא ישן בין האנשים והיא ישנה בין הנשים',qo,cn,'objection');edge('menstrual_answer','4a:9','כי קאמר אפירסה אשתו נדה',ca,qo,'answer');edge('menstrual_scope','4a:9','כי קאמר אפירסה אשתו נדה',ca,cn,'qualification')
qv=q('likewise','4a:10','הא וכן קתני','Does the baraita not say likewise, equating the cases?',['Proposed menstruation-only restriction'])
edge('likewise','4a:10','הא וכן קתני',qv,ca,'objection')
cr=claim('restate','4b:1','הכי קאמר וכן מי שפירסה אשתו נדה ולא בעל הוא ישן בין האנשים ואשתו ישנה בין הנשים','The baraita is read as requiring separate sleeping in the menstrual case when intercourse has not yet occurred.',['Wife became menstruant','No prior intercourse'],status='Interpretive restatement of baraita')
edge('restate','4b:1','הכי קאמר',cr,qv,'answer');edge('qualify_niddah','4b:1','ולא בעל',cr,'kt.resume26.b2.c.niddah','qualification')
ql=q('lenient','4b:2','למימרא דאבילות קילא ליה מנדה','Does this imply that mourning is treated more lightly than menstruation?',['Separation despite prior intercourse in mourning, but not menstruation'])
ch=claim('niddah_work','4b:3','כל מלאכות שאשה עושה לבעלה נדה עושה לבעלה חוץ ממזיגת הכוס והצעת המטה והרחצת פניו ידיו ורגליו','Rav Huna permits a menstruant wife’s ordinary services except pouring the cup, preparing the bed, and washing the husband’s face, hands and feet.',['Wife menstruant'],holder=['רב הונא'])
attr('yitzhak','4b:3','אמר רבי יצחק בר חנינא אמר רב הונא','רבי יצחק בר חנינא','transmitter',['רבי יצחק בר חנינא'],'Menstruant wife’s services',['רבי יצחק בר חנינא','רב הונא'])
attr('huna','4b:3','אמר רב הונא','רב הונא','quoted_authority',['רב הונא'],'Menstruant wife’s services',['רבי יצחק בר חנינא','רב הונא'])
cbeauty=claim('no_compel','4b:3','אע"פ שאמרו אין אדם רשאי לכוף את אשתו להיות כוחלת ולהיות פוקסת','One may not compel one’s wife to apply kohl or adorn her hair during the cited mourning context.',['Mourning context; spouse distinction subsequently debated'],holder=['quoted baraita'])
cs=claim('mourning_service','4b:3','באמת אמרו מוזגת לו הכוס ומצעת לו המטה ומרחצת לו פניו ידיו ורגליו','The mourning baraita nevertheless permits pouring the cup, preparing the bed, and washing his face, hands and feet.',['Mourning context; subsequent distinctions retained'],holder=['quoted baraita'])
edge('services_objection','4b:3','ואילו גבי אבילות תניא',cs,ql,'objection')
cd=claim('spouses','4b:4','לא קשיא כאן באבילות דידיה כאן באבילות דידה','The anonymous answer distinguishes his mourning from hers.',['His mourning versus hers'],status='First attempted distinction; challenged and clarified below')
edge('spouses_answer','4b:4','לא קשיא',cd,ql,'answer')
qp=q('bothparents','4b:5','והא אביו של חתן או אמה של כלה קתני','Does the first baraita not include both the groom’s father and bride’s mother?',['Proposed difference between his and her mourning'])
cother=claim('rest','4b:5','כי קתני אשארא','The mention of both parental deaths applies to the other provisions.',['Reading under the spouse distinction; not all provisions equally apply'],status='Restricted reading; later objection retained')
edge('parents','4b:5','והא אביו של חתן או אמה של כלה קתני',qp,cd,'objection');edge('rest','4b:5','כי קתני אשארא',cother,qp,'answer')
qd=q('different','4b:6','ומי שאני בין אבילות דידיה לאבילות דידה','Is there really a difference between his mourning and hers?')
cwife=claim('wife_parent','4b:6','מי שמת חמיו או חמותו אינו יכול לכוף את אשתו להיות כוחלת ולהיות פוקסת אלא כופה מטתו ונוהג עמה אבילות','When his father-in-law or mother-in-law dies, he cannot compel his wife’s cosmetics; he overturns his bed and observes mourning with her.',['Wife’s father or mother dies'],holder=['quoted baraita'])
chus=claim('husband_parent','4b:6','וכן היא שמת חמיה או חמותה אינה רשאה להיות כוחלת ולהיות פוקסת אלא כופה מטתה ונוהגת עמו אבילות','When her father-in-law or mother-in-law dies, she may not apply the cited cosmetics; she overturns her bed and observes mourning with him.',['Husband’s father or mother dies'],holder=['quoted baraita'])
edge('spouse_challenge','4b:6','ומי שאני בין אבילות דידיה לאבילות דידה',qd,cd,'objection');edge('symmetry','4b:6','וכן היא שמת חמיה או חמותה',chus,qd,'support')
csep=claim('his_separate','4b:7','תני באבילות דידיה הוא ישן בין האנשים ואשתו ישנה בין הנשים','The baraita is recited with separate sleeping in the husband’s mourning.',['His mourning'],status='Proposed recitation/reading in first resolution')
qagain=q('likewise_again','4b:7','הא וכן קתני','Does likewise not equate the wife’s mourning to his in this baraita?')
ccos=claim('cosmetic_referent','4b:7','כי קתני אכיחול ואפירכוס','Likewise applies to cosmetics, rather than all sleeping arrangements.',['Scope of likewise in the quoted baraita'])
qwith=q('with','4b:7','והא עמו קתני מאי לאו עמו במטה','Does mourning with him not mean with him in bed?')
chome=claim('house','4b:7','לא עמו בבית','With him means in the house, not in the bed.',['Meaning of with him in mourning baraita'])
cRav=claim('rav_son','4b:7','וכדאמר ליה רב לחייא בריה באפה נהוג אבילותא דלא באפה לא תנהוג אבילותא','Rav instructed Hiyya his son to observe mourning in her presence but not outside her presence.',['Wife’s presence versus absence','Spousal mourning context'],holder=['רב'])
attr('rav','4b:7','דאמר ליה רב לחייא בריה','רב','speaker',['רב'],'Instruction to Hiyya his son; Hiyya is addressee, not inferred position holder')
edge('separate_reading','4b:7','תני באבילות דידיה',csep,qd,'answer');edge('again','4b:7','הא וכן קתני',qagain,csep,'objection');edge('cosmetics','4b:7','כי קתני אכיחול ואפירכוס',ccos,qagain,'answer');edge('with','4b:7','לא עמו בבית',chome,qwith,'answer');edge('rav_example','4b:7','וכדאמר ליה רב לחייא בריה',cRav,chome,'support')
cA=claim('ashi_distinction','4b:8','רב אשי אמר מי קמדמית אבילותא דהכא לאבילותא דעלמא אבילותא דעלמא חמיר ולא אתי לזלזולי ביה אבילות דהכא כיון דאקילו רבנן אתי לזלזולי ביה','Rav Ashi distinguishes ordinary mourning, whose severity prevents laxity, from this exceptional mourning case, where rabbinic leniency risks laxity.',['Exceptional wedding-bereavement case versus ordinary mourning'],holder=['רב אשי'],status='Alternative resolution; not harmonized into the prior spouse distinction')
attr('ashi','4b:8','רב אשי אמר','רב אשי','speaker',['רב אשי'],'Alternative exceptional-versus-ordinary mourning distinction')
edge('ashi_answer','4b:8','מי קמדמית אבילותא דהכא לאבילותא דעלמא',cA,ql,'answer')
qk=q('leniency','4b:9','מאי קולא','What leniency in this case creates the risk?')
cx=claim('intercourse_rejected','4b:9','אילימא דקתני בועל בעילת מצוה ופורש התם משום דלא חל עליו אבילותא','Initial intercourse is rejected as the relevant leniency, since mourning has not yet begun.',['Proposed identification of exceptional leniency'],mode='rejected',status='Rejection of proposed rationale, not rejection of permitted initial intercourse')
ce=claim('eliezer','4b:9','אי לרבי אליעזר עד שיצא מפתח הבית','For Rabbi Eliezer mourning begins when the deceased leaves the house doorway.',['Onset of mourning'],holder=['רבי אליעזר'])
cy=claim('yehoshua','4b:9','אי לרבי יהושע עד שיסתם הגולל','For Rabbi Yehoshua mourning begins when the grave-cover is closed.',['Onset of mourning'],holder=['רבי יהושע'])
attr('eliezer','4b:9','לרבי אליעזר','רבי אליעזר','position_holder',['רבי אליעזר'],'Onset of mourning');attr('yehoshua','4b:9','לרבי יהושע','רבי יהושע','position_holder',['רבי יהושע'],'Onset of mourning')
edge('onset_e','4b:9','אי לרבי אליעזר עד שיצא מפתח הבית',ce,cx,'support');edge('onset_y','4b:9','אי לרבי יהושע עד שיסתם הגולל',cy,cx,'support')
cl=claim('delayed_mourning','4b:10','אלא דקתני נוהג שבעת ימי המשתה ואח"כ נוהג שבעת ימי אבילות','The relevant leniency is placing seven days of celebration before seven days of mourning.',['Exceptional prepared-feast bereavement case'],status='Accepted local identification of leniency in Rav Ashi’s explanation')
edge('leniency_answer','4b:10','אלא דקתני',cl,qk,'answer');edge('leniency_support','4b:10','נוהג שבעת ימי המשתה ואח"כ נוהג שבעת ימי אבילות',cl,cA,'support')
for x in records:
 if x['layer']=='claims':x['content']['scope']='Wedding bereavement and related mourning/menstruation argument, Ketubot 4a–4b'
coverage=[]
for c in state['coverage']:
 if old['id'] in c['record_ids']:
  coverage.append({k:v for k,v in dict(c,record_ids=[revised['id'] if a==old['id'] else a for a in c['record_ids']],rationale='Continuation through 4b:10 read and encoded; prior structure closed with explicit revision lineage').items() if k!='proposal_execution'})
for ref in core:
 sid=byref[ref]['id']
 for layer in r.LAYERS:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  rationale='Manual '+layer+' pass over '+ref+'; '+('reread contrasting menstrual/mourning rules, spouse distinction and Rav Ashi alternative, rhetorical questions and rejected leniency; no further omitted local unit identified' if layer=='reconciliation' else 'explicit local findings retained; identities and transmission separated; no independent-review claim')
  if not ids and layer!='reconciliation':rationale+='; no additional '+layer+' finding after pass'
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=[x for x in state['open_tails'] if x!=old['id']])
r.validate_apply(state,p,segments,j);path=out/'batch003_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'batch003_receipt.json',r.encoded(receipt));print(receipt)
