from pathlib import Path
exec((Path(__file__).parent.parent/'worker_20261126/batch001.py').read_text(encoding='utf-8').split("add('s.baraita'")[0])
prefix='kt.wave3.b4.';core=['12a:14','12a:15','12a:16','12b:1','12b:2','12b:3','12b:4']
add('s.amount','structure',core[:4],dict(title='Priestly widow amounts across successive enactments',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
add('s.families','structure',core[4:],dict(title='Distinguished Israelite families and priestly settlement custom',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('12a:14','Mishnah','widow amounts and priestly court practice'),('12a:15','quoted teaching and anonymous objection','conflicting widow amounts'),('12a:16','Rav Ashi','successive enactments and original amounts'),('12b:1','continuation of Rav Ashi’s explanation','increase and restoration with social reasons'),('12b:2','Rav Yehuda reporting Shmuel','extension beyond priestly court'),('12b:3','quoted teaching and anonymous inference','mixed-marriage examples raised as restriction'),('12b:4','anonymous reply','a fortiori inclusion and anticipated elevation argument')]:add('u.'+ref,'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
cwi=claim('widow_israel','12a:14','אחת אלמנת ישראל ואחת אלמנת כהנים כתובתה מנה','An Israelite widow’s settlement is a maneh.',['Israelite widow'],holder=['Mishnah'])
cwp=claim('widow_priest','12a:14','אחת אלמנת ישראל ואחת אלמנת כהנים כתובתה מנה','A priestly widow’s settlement is likewise a maneh.',['Priestly widow'],holder=['Mishnah'])
cv=claim('virgin_priest','12a:14','בית דין של כהנים היו גובין לבתולה ארבע מאות זוז','The priestly court collected four hundred zuz for a virgin.',['Priestly court practice','Virgin'],holder=['Mishnah'])
cn=claim('nonprotest','12a:14','ולא מיחו בידם חכמים','The sages did not protest the priestly court’s practice.',['Four-hundred-zuz settlement for a virgin'],holder=['Mishnah'])
ct=claim('teaching_200','12a:15','תנא ואלמנת כהנים כתובתה מאתים','A quoted teaching gives a priestly widow two hundred.',['Priestly widow'],holder=['quoted teaching'],status='Reconciled with the Mishnah through different enactment stages')
qc=q('contradiction','12a:15','והאנן תנן אחת אלמנת ישראל ואחת אלמנת כהנים כתובתן מנה','How does two hundred fit the Mishnah’s maneh for both kinds of widow?')
edge('amount_objection','12a:15','והאנן תנן',qc,ct,'objection')
cst=claim('stages','12a:16','אמר רב אשי שתי תקנות הוו','Rav Ashi explains that there were two enactments.',['Different amounts occur at different stages'],holder=['רב אשי'])
civ=claim('initial_virgin','12a:16','מעיקרא תקינו לבתולה ארבע מאות זוז','The original enactment assigned a virgin four hundred zuz.',['Original priestly enactment','Virgin'],holder=['רב אשי'])
ciw=claim('initial_widow','12a:16','ולאלמנה מנה','The original widow amount was a maneh.',['Original priestly enactment','Widow'],holder=['רב אשי'])
cup=claim('widow_increase','12b:1','כיון דחזו דמזלזלי בהו תקינו להו מאתן','Seeing that the widows were treated with contempt, they raised their settlement to two hundred.',['Priestly widows','Intermediate enactment after contempt'],holder=['Rav Ashi’s explanation'])
cback=claim('widow_restore','12b:1','כיון דחזו דקא פרשין מינייהו דאמרי עד דנסבינן אלמנת כהנים ניזיל ניסיב בתולה בת ישראל אהדרינהו למלתייהו','When suitors avoided them, preferring an Israelite virgin at that price, they restored the widow amount to its former level.',['Priestly widows','Later restoration after suitors avoided them'],holder=['Rav Ashi’s explanation'])
edge('stages_answer','12a:16','שתי תקנות הוו',cst,qc,'answer');edge('increase_change','12b:1','תקינו להו מאתן',cup,ciw,'correction');edge('restoration_change','12b:1','אהדרינהו למלתייהו',cback,cup,'correction')
attr('court','12a:14','בית דין של כהנים','בית דין של כהנים','collective',['בית דין של כהנים'],'Court collecting the increased virgin settlement')
attr('sages','12a:14','חכמים','חכמים','collective',['חכמים'],'Nonprotest at priestly practice')
attr('ashi','12a:16','אמר רב אשי','רב אשי','speaker',['רב אשי'],'Successive-enactment reconciliation continuing into12b:1')
ce=claim('extension','12b:2','לא ב"ד של כהנים בלבד אמרו אלא אפי\' משפחות המיוחסות בישראל אם רצו לעשות כדרך שהכהנים עושין עושין','Shmuel, reported by Rav Yehuda, extends permission to distinguished Israelite families wishing to follow priestly practice.',['Distinguished Israelite family','Wishes to adopt priestly practice'],holder=['שמואל'])
attr('shmuel','12b:2','אמר רב יהודה אמר שמואל','שמואל','speaker',['שמואל'],'Permission for distinguished Israelite families',chain=['רב יהודה','שמואל'])
attr('yehuda','12b:2','אמר רב יהודה','רב יהודה','transmitter',['רב יהודה'],'Reports Shmuel; not Rav himself',chain=['רב יהודה','שמואל'])
cmix1=claim('mixed_woman_israel','12b:3','כגון בת ישראל לכהן ובת כהן לישראל עושין','The cited teaching permits an Israelite woman marrying a priest to adopt the practice.',['Israelite woman','Priest husband'],holder=['quoted teaching'])
cmix2=claim('mixed_woman_priest','12b:3','כגון בת ישראל לכהן ובת כהן לישראל עושין','The cited teaching also permits a priestly woman marrying an Israelite to adopt the practice.',['Priestly woman','Israelite husband'],holder=['quoted teaching'])
qex=q('restrictive_inference','12b:3','בת ישראל לכהן ובת כהן לישראל הוא דאיכא צד כהונה אבל בת ישראל לישראל לא','Do the mixed-marriage examples restrict the permission to a marriage having a priestly side, excluding Israelite-to-Israelite marriages?',['Inference from quoted examples'])
edge('restriction_objection','12b:3','אבל בת ישראל לישראל לא',qex,ce,'objection')
cplain=claim('pure_israelite','12b:4','לא מבעיא בת ישראל לישראל דלא מצי אמר לה עלויי קא מעלינן ליך','The reply treats an Israelite-to-Israelite marriage as the obvious permitted case: he cannot claim to elevate her status.',['Israelite woman','Israelite husband'],holder=['anonymous reply'])
chyp=claim('elevation_hypothesis','12b:4','אבל בת ישראל לכהן דמצי אמר לה עלויי קא מעלינן ליך אימא לא','One might have excluded an Israelite woman marrying a priest because he could claim that he elevates her status.',['Israelite woman','Priest husband'],mode='rejected',holder=['anonymous anticipated objection'],status='Hypothesis rejected by the teaching’s inclusion')
cinclude=claim('mixed_included','12b:4','אימא לא קמ"ל','The teaching specifically includes that mixed marriage despite the anticipated elevation argument.',['Israelite woman','Priest husband'],holder=['anonymous reply'])
edge('plain_answer','12b:4','לא מבעיא קאמר',cplain,qex,'answer');edge('mixed_answer','12b:4','קמ"ל',cinclude,qex,'answer');edge('hypothesis_reject','12b:4','קמ"ל',cinclude,chyp,'objection')
for x in records:
 if x['layer']=='claims':x['content']['scope']='Priestly settlement amounts and adoption by distinguished Israelite families, Ketubot12a:14–12b:4'
coverage=[]
for ref in core:
 sid=byref[ref]['id']
 for layer in r.LAYERS:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  rationale='Manual '+layer+' pass over '+ref+'; '+('reread original/increased/restored widow amounts, virgin amount separately, nonprotest, explicit Shmuel transmission, both mixed-marriage examples, rejected restrictive inference and elevation hypothesis through final reply' if layer=='reconciliation' else 'amounts, chronology, family and marriage conditions kept separate')
  if not ids:rationale+='; no additional supported finding in this layer'
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=r.current(job)['open_tails'])
r.validate_apply(r.current(job),p,segments,j);path=out/'batch004_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'batch004_receipt.json',r.encoded(receipt));print(receipt)
