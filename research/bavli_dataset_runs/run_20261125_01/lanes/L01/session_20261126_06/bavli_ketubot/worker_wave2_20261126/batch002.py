from pathlib import Path
exec((Path(__file__).parent.parent/'worker_20261126/batch001.py').read_text(encoding='utf-8').split("add('s.baraita'")[0])
prefix='kt.wave2.b2.';core=['5a:'+str(n) for n in range(6,11)]
add('s.days','structure',core,dict(title='Consummation days: cooling resolve, blessings, and three days with a widow',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('5a:6','anonymous inquiry','two alternatives about Wednesday consummation'),('5a:7','anonymous proof citing Bar Kappara','schedule, blessing rationales, and inference'),('5a:8','anonymous discussion','challenge and preference for human blessing'),('5a:9','anonymous alternative citing baraita','three-day companionship rationale'),('5a:10','anonymous discussion','practical differences between rationales')]:add('u.'+ref,'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
qq=q('cooling','5a:6','איבעיא להו בתולה נשאת ברביעי ונבעלת ברביעי ולא חיישינן לאיקרורי דעתא או דלמא בתולה נשאת ברביעי ונבעלת בחמישי דחיישינן לאיקרורי דעתא','May a virgin marry and consummate Wednesday without concern that his resolve will cool, or must consummation wait until Thursday because of that concern?',['Virgin marrying Wednesday','Concern about delay before presenting a virginity claim'])
cw=claim('wed_option','5a:6','בתולה נשאת ברביעי ונבעלת ברביעי ולא חיישינן לאיקרורי דעתא','The inquiry proposes Wednesday consummation with no concern about cooling resolve.',['Virgin married Wednesday'],mode='queried',status='First inquiry alternative, not an adopted ruling')
ct=claim('thu_option','5a:6','או דלמא בתולה נשאת ברביעי ונבעלת בחמישי דחיישינן לאיקרורי דעתא','The inquiry alternatively proposes Thursday consummation because of concern about cooling resolve.',['Virgin married Wednesday'],mode='queried',status='Second inquiry alternative, not an adopted ruling')
cv=claim('virgin_schedule','5a:7','בתולה נשאת ברביעי ונבעלת בחמישי הואיל ונאמרה בו ברכה לדגים','Bar Kappara teaches marriage of a virgin Wednesday and consummation Thursday because the fish received a blessing that day.',['Virgin marriage'],holder=['בר קפרא'],status='Teaching cited as proof; stated rationale is blessing')
cd=claim('widow_schedule','5a:7','אלמנה נשאת בחמישי ונבעלת בששי הואיל ונאמרה בו ברכה לאדם','Bar Kappara teaches a widow’s marriage Thursday and consummation Friday because humanity received a blessing that day.',['Widow marriage'],holder=['בר קפרא'])
attr('kappara','5a:7','דתני בר קפרא','בר קפרא','quoted_authority',['בר קפרא'],'Marriage and consummation days with blessing rationales')
ci=claim('no_cooling','5a:7','טעמא משום ברכה אבל משום איקרורי דעתא לא חיישינן','The discussion infers that blessing is the reason for Thursday consummation, with no concern about cooling resolve.',['Inference from Bar Kappara’s stated rationale'],status='Local inference from cited teaching')
edge('inference_support','5a:7','טעמא משום ברכה',cv,ci,'support');edge('cooling_answer','5a:7','אבל משום איקרורי דעתא לא חיישינן',ci,qq,'answer')
qw=q('widow_thursday','5a:8','אי הכי אלמנה נמי תיבעל בחמישי הואיל ונאמרה בו ברכה לדגים','Why should a widow not also consummate Thursday, the day of the blessing to fish?',['Blessing rationale for consummation'])
cp=claim('human_preference','5a:8','ברכה דאדם עדיפא ליה','The blessing to humanity is preferable for him.',['Widow’s consummation and comparison of blessings'])
edge('widow_challenge','5a:8','אי הכי אלמנה נמי תיבעל בחמישי',qw,cd,'objection');edge('human_reply','5a:8','ברכה דאדם עדיפא ליה',cp,qw,'answer')
qwhy=q('widow_reason','5a:9','מפני מה אמרו אלמנה נשאת בחמישי ונבעלת בששי','Why did they prescribe a widow’s marriage Thursday and consummation Friday?',['Widow marriage'])
cwork=claim('departure','5a:9','שאם אתה אומר תיבעל בחמישי למחר משכים לאומנתו והולך לו','If consummation were Thursday, he would arise early Friday and depart to his occupation.',['Thursday consummation','Husband with an occupation'],mode='hypothetical',holder=['quoted baraita'])
cjoy=claim('companionship','5a:9','שקדו חכמים על תקנת בנות ישראל שיהא שמח עמה שלשה ימים חמישי בשבת וערב שבת ושבת','The sages provided that he rejoice with her for three days: Thursday, Friday, and Sabbath.',['Widow’s marriage schedule'],holder=['חכמים'],status='Alternative shakedu rationale, not combined as necessary with blessing rationale')
attr('sages','5a:9','שקדו חכמים','חכמים','collective',['חכמים'],'Three days of companionship')
edge('departure_support','5a:9','למחר משכים לאומנתו והולך לו',cwork,cjoy,'support');edge('companionship_answer','5a:9','שקדו חכמים על תקנת בנות ישראל',cjoy,qwhy,'answer');edge('alternative_answer','5a:9','ואי נמי משום שקדו',cjoy,qw,'answer')
qd=q('difference','5a:10','מאי איכא בין ברכה לשקדו','What practical difference is there between blessing and shakedu rationales?')
cb=claim('idle','5a:10','איכא בינייהו אדם בטל','An idle man is a case distinguishing the rationales.',['Husband without occupation'],status='Text identifies distinguishing case; no explicit detailed outcome sentence imported')
ch=claim('festival','5a:10','אי נמי יום טוב שחל להיות בערב שבת','Alternatively, a festival falling Friday distinguishes the rationales.',['Festival on Friday'],status='Second distinguishing case')
edge('idle_answer','5a:10','איכא בינייהו אדם בטל',cb,qd,'answer');edge('festival_answer','5a:10','אי נמי יום טוב שחל להיות בערב שבת',ch,qd,'answer')
for x in records:
 if x['layer']=='claims':x['content']['scope']='Consummation schedule and widow companionship, Ketubot5a:6–10'
coverage=[]
for ref in core:
 sid=byref[ref]['id']
 for layer in r.LAYERS:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  rationale='Manual '+layer+' pass over '+ref+'; '+('reread inquiry alternatives, blessing proof and inference, widow objection, alternative preparation rationale and two distinguishing cases; no further local omission found' if layer=='reconciliation' else 'local explicit units retained without turning queried alternatives into rulings')
  if not ids:rationale+='; no separate finding in this layer'
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=r.current(job)['open_tails'])
r.validate_apply(r.current(job),p,segments,j);path=out/'batch002_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'batch002_receipt.json',r.encoded(receipt));print(receipt)
