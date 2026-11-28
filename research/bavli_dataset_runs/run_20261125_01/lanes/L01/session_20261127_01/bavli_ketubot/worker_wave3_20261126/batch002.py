from pathlib import Path
exec((Path(__file__).parent.parent/'worker_20261126/batch001.py').read_text(encoding='utf-8').split("add('s.baraita'")[0])
prefix='kt.wave3.b2.';core=['11b:16']+['12a:'+str(n) for n in range(1,7)]
add('s.parallel','structure',core,dict(title='Prior marriage without consummation: Rabbah/Rav Ashi and two placement traditions',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('11b:16','quoted baraita','second husband’s claim excluded despite witnesses'),('12a:1','Rabbah and Rav Ashi','general inference versus special prior-marriage case'),('12a:2','anonymous question and Rav Sheravya','during-betrothal concern and immediacy answer'),('12a:3','alternative transmission on Mishnah; anonymous clarification','Mishnah rule and unconsummated huppah case'),('12a:4','Rabbah and Rav Ashi in alternative placement','parallel disagreement preserved'),('12a:5','anonymous question and Rav Sheravya in alternative placement','parallel immediacy answer'),('12a:6','anonymous comparison','asymmetry between baraita-based and Mishnah-based versions')]:add('u.'+ref,'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
cond=['First husband entered marriage','Witnesses establish no seclusion, or seclusion too brief for intercourse','Second husband’s virginity claim']
cbar=claim('baraita','11b:16','ת"ר כנסה ראשון לשום נישואין ויש לה עדים שלא נסתרה אי נמי נסתרה ולא שהתה כדי ביאה אין השני יכול לטעון טענת בתולים שהרי כנסה ראשון','The baraita denies the second husband a virginity claim even with witnesses to no adequate opportunity for consummation, because the first entered marriage.',cond,holder=['quoted baraita'])
cr=claim('rabbah_inference','12a:1','אמר רבה זאת אומרת כנסה בחזקת בתולה ונמצאת בעולה יש לה כתובה מנה','Rabbah infers that marriage under a virginity presumption followed by discovery of nonvirginity still leaves a maneh.',['Presumed virgin at marriage','Found nonvirgin'],holder=['רבה'],status='Inference from baraita; opposed by Rav Ashi’s distinction')
ca=claim('ashi_general','12a:1','רב אשי אמר בעלמא לעולם אימא לך לית לה כלל','Rav Ashi allows that in the general presumed-virgin case she has nothing.',['General case, without special first marriage'],holder=['רב אשי'],status='Distinguishes baraita rather than conceding Rabbah’s inference')
cspecial=claim('ashi_special','12a:1','ושאני הכא שהרי כנסה ראשון','Here is different because the first husband had entered marriage.',['Prior marriage in baraita'],holder=['רב אשי'])
attr('rabbah','12a:1','אמר רבה','רבה','speaker',['רבה'],'Maneh inference; Rabbah not Rava')
attr('ashi','12a:1','רב אשי אמר','רב אשי','speaker',['רב אשי'],'General/special distinction')
edge('baraita_support','12a:1','זאת אומרת',cbar,cr,'support');edge('ashi_distinguish','12a:1','ושאני הכא',cspecial,cr,'distinction')
qinterval=q('interval','12a:2','וניחוש שמא תחתיו זינתה','Should there not be concern that the event occurred during his betrothal?',['Second husband’s claim'])
cnow=claim('immediate','12a:2','אמר רב שרביא כגון שקידש ובעל לאלתר','Rav Sheravya specifies immediate intercourse after betrothal, eliminating the intervening period.',['Betrothal immediately followed by intercourse'],holder=['רב שרביא'])
attr('sheravya','12a:2','אמר רב שרביא','רב שרביא','speaker',['רב שרביא'],'Immediate sequence restriction')
edge('interval_objection','12a:2','וניחוש',qinterval,cbar,'objection');edge('immediate_reply','12a:2','כגון שקידש ובעל לאלתר',cnow,qinterval,'answer')
cmamount=claim('mishnah_amount','12a:3','בתולה אלמנה גרושה חלוצה מן הנישואין כתובתן מנה','In the alternative placement, the Mishnah’s virgin prior-marriage cases receive a maneh.',['Virgin widow/divorcee/halitzah case from prior marriage'],holder=['quoted Mishnah'],status='Repeated source occurrence under alternative teaching placement')
cmclaim=claim('mishnah_no_claim','12a:3','ואין להן טענת בתולין','Those prior-marriage cases do not admit a virginity claim.',['Cases quoted in alternative Mishnah placement'],holder=['quoted Mishnah'])
qvir=q('virgin_marriage','12a:3','בתולה מן הנישואין היכי משכחת לה','How is a virgin from a prior marriage possible?')
chu=claim('huppah_no_intercourse','12a:3','כגון שנכנסה לחופה ולא נבעלה','She entered the wedding canopy but did not consummate.',['Prior huppah','No prior consummation'],status='Case defining virgin from marriage')
edge('huppah_answer','12a:3','כגון שנכנסה לחופה ולא נבעלה',chu,qvir,'answer')
cr2=claim('rabbah_repeat','12a:4','אמר רבה זאת אומרת כנסה בחזקת בתולה ונמצאת בעולה כתובתה מנה','Rabbah again infers a maneh in the presumed-virgin/found-nonvirgin case.',['Presumed virgin','Found nonvirgin','Mishnah placement tradition'],holder=['רבה'],status='Parallel occurrence not deduplicated')
ca2=claim('ashi_general_repeat','12a:4','רב אשי אמר לעולם אימא לך בעלמא לית לה כלל','Rav Ashi again allows no entitlement in the general case.',['General presumed-virgin case','Mishnah placement tradition'],holder=['רב אשי'])
cs2=claim('ashi_huppah','12a:4','ושאני הכא שהרי נכנסה לחופה','The special case differs because she entered a prior wedding canopy.',['Prior huppah','Mishnah placement tradition'],holder=['רב אשי'])
attr('rabbah_repeat','12a:4','אמר רבה','רבה','speaker',['רבה'],'Parallel inference on Mishnah')
attr('ashi_repeat','12a:4','רב אשי אמר','רב אשי','speaker',['רב אשי'],'Parallel special-case distinction')
edge('mishnah_support','12a:4','זאת אומרת',cmamount,cr2,'support');edge('huppah_distinguish','12a:4','ושאני הכא',cs2,cr2,'distinction')
qi2=q('interval_repeat','12a:5','וליחוש שמא תחתיו זינתה','Should the intervening-betrothal concern not arise in this version too?')
cn2=claim('immediate_repeat','12a:5','אמר רב שרביא כגון שקידש ובעל לאלתר','Rav Sheravya again specifies immediate intercourse after betrothal.',['Betrothal immediately followed by intercourse','Mishnah placement tradition'],holder=['רב שרביא'],status='Parallel occurrence retained')
attr('sheravya_repeat','12a:5','אמר רב שרביא','רב שרביא','speaker',['רב שרביא'],'Repeated immediacy answer')
edge('interval_repeat_objection','12a:5','וליחוש',qi2,cmclaim,'objection');edge('immediate_repeat_reply','12a:5','כגון שקידש ובעל לאלתר',cn2,qi2,'answer')
cforward=claim('baraita_implies_mishnah','12a:6','מאן דמתני לה אברייתא כל שכן אמתניתין','A transmitter attaching the discussion to the baraita would all the more apply it to the Mishnah.',['Baraita placement tradition'],holder=['anonymous comparison'])
creverse=claim('mishnah_not_baraita','12a:6','ומאן דמתני לה אמתני\' אבל אברייתא לא משום דמצי אמר לה אנא אעדים סמכי','A transmitter attaching it to the Mishnah need not apply it to the baraita, because the husband could say he relied on the witnesses.',['Mishnah placement tradition','Baraita has witnesses'],holder=['anonymous comparison'])
edge('version_distinction','12a:6','משום דמצי אמר לה אנא אעדים סמכי',creverse,cforward,'distinction')
for x in records:
 if x['layer']=='claims':x['content']['scope']='Prior marriage and virginity-claim discussion, Ketubot11b:16–12a:6; both placement versions retained'
coverage=[]
for ref in core:
 sid=byref[ref]['id']
 for layer in r.LAYERS:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  rationale='Manual '+layer+' pass over '+ref+'; '+('reread no-seclusion/short-seclusion witnesses, Rabbah/Rav Ashi general-versus-special distinction, both immediate-sequence answers, full repeated Mishnah placement and witness-reliance asymmetry' if layer=='reconciliation' else 'parallel occurrences and their distinct conditions retained; no forced single case or adjudicated winner')
  if not ids:rationale+='; no additional supported finding in this layer'
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=r.current(job)['open_tails'])
r.validate_apply(r.current(job),p,segments,j);path=out/'batch002_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'batch002_receipt.json',r.encoded(receipt));print(receipt)
