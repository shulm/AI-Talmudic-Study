from pathlib import Path
exec((Path(__file__).parent.parent/'worker_20261126/batch001.py').read_text(encoding='utf-8').split("add('s.baraita'")[0])
prefix='kt.wave2.b9.';core=['8a:'+str(n) for n in range(10,16)]+['8b:1','8b:2','8b:3']
add('s.practice','structure',core[:5],dict(title='Wedding rejoicing formulas over time, preparations and rejected practices',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
add('s.quorum','structure',core[5:],dict(title='Bridegrooms and mourners in the quorum: grace, row and square distinctions',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('8a:10','narrator concerning Rav Ashi','first-day and later new-face/no-new-face practices'),('8a:11','anonymous rule','time and invitation conditions for rejoicing formula'),('8a:12','anonymous questions; Rav Pappi reporting Rava; Rav Pappa','time bounds and betrothal exception'),('8a:13','narrator concerning Ravina and Rav Tahlifa; anonymous conclusion','failed prediction and rejected long-blessing practice'),('8a:14','narrator concerning Rav Haviva; anonymous conclusion','circumcision rejoicing formula rejected'),('8a:15','Rav Nahman reporting Rav; Rabbi Yitzhak reporting Rabbi Yohanan; anonymous objections','quorum conflict in two transmissions'),('8b:1','anonymous reply','grace versus condolence row distinction'),('8b:2','anonymous objection citing Rabbi Yitzhak/Rabbi Yohanan','row interpretation rejected for square blessing'),('8b:3','anonymous objection citing Rabbi Yitzhak/Rabbi Yohanan','seven days qualified by new faces')]:add('u.'+ref,'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
cfirst=claim('first_day','8a:10','רב אשי איקלע לבי רב כהנא יומא קמא בריך כולהו','Rav Ashi visited Rav Kahana’s house and recited all the blessings on the first day.',['First wedding day'],holder=['narrator concerning רב אשי'])
cfaces=claim('later_faces','8a:10','מכאן ואילך אי איכא פנים חדשות בריך כולהו','Thereafter he recited all the blessings when new faces were present.',['After first day within wedding period','New faces present'],holder=['narrator concerning רב אשי'])
cnof=claim('later_no_faces','8a:10','ואי לא אפושי שמחה בעלמא הוא מברך שהשמחה במעונו ואשר ברא','Without new faces the gathering is additional rejoicing, and the formulas recited are שהשמחה במעונו and אשר ברא.',['After first day within wedding period','No new faces'],holder=['narrator concerning רב אשי'],status='Two jointly specified formulas for this branch; not a claim of full sequence')
attr('ashi','8a:10','רב אשי איקלע','רב אשי','position_holder',['רב אשי'],'Reported first-day/later blessing practice')
c30=claim('through30','8a:11','משבעה ועד שלשים בין אמר להו מחמת הלולא ובין לא אמר להו מחמת הלולא מברך שהשמחה במעונו','From after the seven-day period through thirty days, שהשמחה במעונו is recited whether or not the invitation states it is because of the wedding.',['After seven-day period through thirty days'],status='Anonymous temporal rule')
cafter=claim('after30_yes','8a:11','מכאן ואילך אי אמר להו מחמת הלולא מברך שהשמחה במעונו','Afterward the formula is recited if the invitation states it is because of the wedding.',['After thirty days','Wedding purpose explicitly stated','Upper limit clarified at8a:12 as twelve months'])
cafter_no=claim('after30_no','8a:11','ואי לא לא','Afterward, without that stated wedding purpose, the formula is not recited.',['After thirty days','Wedding purpose not stated'])
qend=q('until','8a:12','וכי א"ל מחמת הלולא עד אימת','When the wedding purpose is stated, until when does the rule apply?')
cyear=claim('year','8a:12','אמר רב פפי משמיה דרבא עד תריסר ירחי שתא','Rav Pappi reports Rava: until twelve months of the year.',['Invitation explicitly because of wedding','Time limit for שהשמחה במעונו'],holder=['רבא'])
attr('pappi','8a:12','רב פפי משמיה דרבא','רב פפי','transmitter',['רב פפי'],'Twelve-month limit',['רב פפי','רבא'])
attr('rava','8a:12','משמיה דרבא','רבא','quoted_authority',['רבא'],'Twelve-month limit',['רב פפי','רבא'])
qstart=q('start','8a:12','ומעיקרא מאימת','From when before the wedding may the formula begin?')
cbarley=claim('barley','8a:12','אמר רב פפא מכי רמו שערי באסינתא','Rav Pappa gives the starting point as placing barley in the vat.',['Pre-wedding preparations'],holder=['רב פפא'],status='Preparation marker preserved literally, without expanded custom theory')
qear=q('early_pappa','8a:12','איני והא רב פפא איעסק לאבא מר בריה ובריך משעת אירוסין','But did Rav Pappa not recite it from betrothal when arranging his son Abba Mar’s marriage?')
cprep=claim('already_prepared','8a:12','שאני רב פפא דהוה טריח ליה','Rav Pappa’s case was different because the preparations had been made for him.',['Rav Pappa’s specific marriage arrangement'],status='Exception to preparation marker; not blanket permission from every betrothal')
attr('pappa','8a:12','אמר רב פפא','רב פפא','speaker',['רב פפא'],'Preparation starting point; distinct from Rav Pappi')
edge('year_answer','8a:12','עד תריסר ירחי שתא',cyear,qend,'answer');edge('year_limit','8a:12','עד תריסר ירחי שתא',cyear,cafter,'qualification');edge('barley_answer','8a:12','מכי רמו שערי באסינתא',cbarley,qstart,'answer');edge('pappa_challenge','8a:12','איני והא רב פפא',qear,cbarley,'objection');edge('prepared_reply','8a:12','שאני רב פפא דהוה טריח ליה',cprep,qear,'answer')
cravina=claim('ravina_practice','8a:13','רבינא איעסק ליה לבריה בי רב חביבא ובריך משעת אירוסין','Ravina arranged his son’s marriage with Rav Haviva’s household and recited from betrothal.',holder=['narrator concerning רבינא'],status='Practice followed by failed expectation; not general approval')
cconf=claim('ravina_confidence','8a:13','אמר קים לי בגוייהו דלא הדרי בהו','Ravina said he trusted they would not withdraw.',holder=['רבינא'],status='Reported confidence, subsequently contradicted by event')
cwithdraw=claim('withdrawal','8a:13','לא אסתייע מילתא והדרי בהו','The arrangement failed and they withdrew.',holder=['narrator'],status='Outcome defeating Ravina’s expectation')
attr('ravina','8a:13','רבינא איעסק','רבינא','speaker',['רבינא'],'Betrothal practice and confidence claim')
clong=claim('six_long','8a:13','רב תחליפא בר מערבא איקלע לבבל בריך שית אריכתא','Rav Tahlifa from the West came to Babylonia and recited six long blessings.',holder=['narrator concerning רב תחליפא בר מערבא'],status='Reported practice rejected by ensuing conclusion')
clong_no=claim('not_long','8a:13','ולית הלכתא כוותיה','The law does not follow Rav Tahlifa’s practice.',holder=['anonymous conclusion'],status='Express rejection of six-long-blessing practice')
attr('tahlifa','8a:13','רב תחליפא בר מערבא','רב תחליפא בר מערבא','position_holder',['רב תחליפא בר מערבא'],'Six-long-blessing practice')
edge('withdrawal_correction','8a:13','לא אסתייע מילתא והדרי בהו',cwithdraw,cconf,'correction');edge('long_reject','8a:13','ולית הלכתא כוותיה',clong_no,clong,'local_resolution')
cmila=claim('circumcision','8a:14','רב חביבא איקלע לבי מהולא בריך שהשמחה במעונו','Rav Haviva attended a circumcision and recited שהשמחה במעונו.',holder=['narrator concerning רב חביבא'],status='Practice rejected in continuation')
cmila_no=claim('circumcision_no','8a:14','ולית הלכתא כוותיה משום דטרידי דאית ליה צערא לינוקא','The law does not follow that practice because the attendees are troubled by the infant’s pain.',['Circumcision celebration'],holder=['anonymous conclusion'])
attr('haviva','8a:14','רב חביבא איקלע','רב חביבא','position_holder',['רב חביבא'],'Circumcision formula practice')
edge('mila_reject','8a:14','ולית הלכתא כוותיה',cmila_no,cmila,'local_resolution')
cg=claim('rav_groom','8a:15','א"ר נחמן אמר רב חתנים מן המנין','Rav, reported by Rav Nahman, counts bridegrooms in the quorum.',['Blessing quorum in this discussion'],holder=['רב'])
cm=claim('rav_mourner','8a:15','ואין אבלים מן המנין','Rav’s report excludes mourners from the quorum.',['Mourning quorum in this report'],holder=['רב'],status='Baraita challenges this; first reply recognizes Rav’s tannaitic standing')
qbar=q('rav_baraita','8a:15','מיתיבי חתנים ואבלים מן המנין','A baraita challenges by counting both bridegrooms and mourners.')
ctanna=claim('rav_tanna','8a:15','מתניתא קא רמית עליה דרב רב תנא הוא ופליג','The reply says Rav has tannaitic standing and may disagree with the baraita.',status='Resolution by acknowledged disagreement, not forced harmony')
cjg=claim('yohanan_groom','8a:15','אמר ר\' יצחק א"ר יוחנן חתנים מן המנין','Rabbi Yitzhak reports Rabbi Yohanan counting bridegrooms in the quorum.',['Blessing quorum'],holder=['רבי יוחנן'])
cjm=claim('yohanan_mourner','8a:15','ואין אבלים מן המנין','Rabbi Yohanan’s report excludes mourners from the quorum.',['Quorum ultimately explained as blessing in the square at8b:2'],holder=['רבי יוחנן'],status='Final scope supplied by subsequent discussion')
# The repeated identical clause is disambiguated by its second original offset.
for x in records:
 if x['id'] in [cjm,prefix+'p.yohanan_mourner']:
  text=byref['8a:15']['text'];quote='ואין אבלים מן המנין';a=text.rindex(quote);x['evidence']=[dict(segment_id=byref['8a:15']['id'],start_char=a,end_char=a+len(quote),quote=quote)]
qbar2=add('q.yohanan_baraita','questions','8a:15',dict(formulation='The same baraita counting both bridegrooms and mourners challenges Rabbi Yohanan’s report.',question_origin='explicit',conditions=['Rabbi Yohanan report'],answer_set_status='partial'))
for key,quote,name,role,chain in [('nahman','א"ר נחמן אמר רב','רב נחמן','transmitter',['רב נחמן','רב']),('rav','א"ר נחמן אמר רב','רב','quoted_authority',['רב נחמן','רב']),('yitzhak','אמר ר\' יצחק א"ר יוחנן','רבי יצחק','transmitter',['רבי יצחק','רבי יוחנן']),('yohanan','אמר ר\' יצחק א"ר יוחנן','רבי יוחנן','quoted_authority',['רבי יצחק','רבי יוחנן'])]:attr(key,'8a:15',quote,name,role,[name],'Quorum reports',chain)
edge('rav_objection','8a:15','מיתיבי חתנים ואבלים מן המנין',qbar,cm,'objection');edge('rav_status_reply','8a:15','רב תנא הוא ופליג',ctanna,qbar,'answer');edge('yohanan_objection','8a:15',byref['8a:15']['text'],qbar2,cjm,'objection')
cgrace=claim('grace','8b:1','כי תניא ההיא בברכת המזון','The baraita counting mourners concerns grace after meals.',['Grace after meals'],status='Distinction retained through later clarification')
crow=claim('row','8b:1','כי קאמר רבי יוחנן בשורה','The initial reply locates Rabbi Yohanan’s exclusion in the condolence row.',['Initial interpretation'],mode='retracted',status='Replaced by square-blessing interpretation next')
edge('grace_reply','8b:1','כי תניא ההיא בברכת המזון',cgrace,qbar2,'answer');edge('row_reply','8b:1','כי קאמר רבי יוחנן בשורה',crow,qbar2,'answer')
qrow=q('row_blessing','8b:2','ברכה בשורה מי איכא','Is there a blessing in the condolence row?',['Cited Rabbi Yohanan report explicitly speaks of ten for wedding and mourning blessings'])
csquare=claim('square','8b:2','אלא כי קאמר רבי יוחנן ברחבה','Rabbi Yohanan’s exclusion concerns the blessing in the square.',['Mourning blessing in the square'],status='Revised interpretation')
cmt=claim('mourning_ten','8b:2','וברכת אבלים בעשרה ואין אבלים מן המנין','The report requires ten for the mourning blessing and excludes mourners from that number.',['Mourning blessing in square, as clarified'],holder=['רבי יוחנן'])
edge('row_challenge','8b:2','ברכה בשורה מי איכא',qrow,crow,'objection');edge('square_reply','8b:2','אלא כי קאמר רבי יוחנן ברחבה',csquare,qrow,'answer');edge('square_correct','8b:2','אלא כי קאמר',csquare,crow,'correction');edge('mourner_scope','8b:2','ברחבה',csquare,cjm,'qualification')
qseven=q('square_seven','8b:3','ברכת רחבה כל שבעה מי איכא','Is the square blessing recited throughout all seven days?',['Report extends mourning blessing to seven days'])
cseven=claim('mourning_seven','8b:3','וברכת אבלים בעשרה כל שבעה ואין אבלים מן המנין','The report specifies the mourning blessing for seven days with ten excluding mourners.',['Square blessing','New faces present as clarified next'],holder=['רבי יוחנן'])
cnew=claim('mourning_new','8b:3','משכחת לה בפנים חדשות','The seven-day case occurs when new faces are present.',['New faces present'],status='Qualification answering the duration challenge')
edge('seven_objection','8b:3','ברכת רחבה כל שבעה מי איכא',qseven,cseven,'objection');edge('new_reply','8b:3','משכחת לה בפנים חדשות',cnew,qseven,'answer');edge('new_qualify','8b:3','בפנים חדשות',cnew,cseven,'qualification')
for x in records:
 if x['layer']=='claims':x['content']['scope']='Wedding formula occasions and mourning quorum, Ketubot8a:10–8b:3'
coverage=[]
for ref in core:
 sid=byref[ref]['id']
 for layer in r.LAYERS:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  rationale='Manual '+layer+' pass over '+ref+'; '+('reread timeline branches, actual failed expectation, rejected practices, Rav versus Rabbi Yohanan responses, repeated clause offsets, and row-to-square revision; ensuing mourning illustration read through8b:14' if layer=='reconciliation' else 'distinct conditions, reports and explicit negative outcomes retained; no blanket marriage/mourning ruling inferred')
  if not ids:rationale+='; no additional supported finding in this layer'
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=r.current(job)['open_tails'])
r.validate_apply(r.current(job),p,segments,j);path=out/'batch009_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'batch009_receipt.json',r.encoded(receipt));print(receipt)
