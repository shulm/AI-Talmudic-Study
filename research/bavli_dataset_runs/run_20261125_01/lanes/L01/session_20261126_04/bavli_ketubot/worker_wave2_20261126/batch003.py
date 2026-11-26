from pathlib import Path
exec((Path(__file__).parent.parent/'worker_20261126/batch001.py').read_text(encoding='utf-8').split("add('s.baraita'")[0])
prefix='kt.wave2.b3.';core=['5a:11','5a:12','5a:13','5a:14','5b:1','5b:2']
add('s.righteous','structure',['5a:11','5a:12','5a:13'],dict(title='Bar Kappara: righteous deeds, creation, and scriptural hand language',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
add('s.ears','structure',['5a:14','5b:1','5b:2'],dict(title='Homilies on fingers, ears, and avoiding improper speech',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('5a:11','Bar Kappara','homiletic comparison supported by verses'),('5a:12','Rabbi Hiyya, anonymous replies/questions, Rav Nahman bar Yitzhak','scriptural objections and interpretations'),('5a:13','anonymous discussion','scriptural objection and interpretive reply'),('5a:14','Bar Kappara','ear homily continuing across page'),('5b:1','Bar Kappara continuation; Rabbi Elazar; anonymous discussion','ear instruction and finger-form question'),('5b:2','anonymous interpretation; school of Rabbi Yishmael; quoted sages','finger and earlobe explanations, warning against idle speech')]:add('u.'+ref,'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
cg=claim('greater','5a:11','דרש בר קפרא גדולים מעשה צדיקים יותר ממעשה שמים וארץ','Bar Kappara teaches that the deeds of the righteous exceed the making of heaven and earth.',holder=['בר קפרא'],status='Homiletic teaching, not a legal conclusion')
cc=claim('creation_verse','5a:11','דאילו במעשה שמים וארץ כתיב (ישעיהו מח, יג) אף ידי יסדה ארץ וימיני טפחה שמים','The creation proof cites Isaiah48:13, describing earth founded by a hand and heaven spread by the right hand.',holder=['בר קפרא'],status='Scriptural argument as presented in this passage')
ct=claim('temple_verse','5a:11','ואילו במעשה ידיהם של צדיקים כתיב (שמות טו, יז) מכון לשבתך פעלת ה\' מקדש אדני כוננו ידיך','For righteous handiwork the proof cites Exodus15:17 describing the sanctuary established by hands.',holder=['בר קפרא'],status='Scriptural argument as presented')
attr('kappara_greater','5a:11','דרש בר קפרא','בר קפרא','speaker',['בר קפרא'],'Comparison of righteous work and creation')
edge('creation_support','5a:11','דאילו במעשה שמים וארץ כתיב',cc,cg,'support');edge('temple_support','5a:11','ואילו במעשה ידיהם של צדיקים כתיב',ct,cg,'support')
qhands=q('hands','5a:12','השיב בבלי אחד ור\' חייא שמו (תהלים צה, ה) ויבשת ידיו יצרו','Rabbi Hiyya objects from Psalm95:5, which speaks of hands forming dry land.')
attr('hiyya','5a:12','השיב בבלי אחד ור\' חייא שמו','רבי חייא','speaker',['רבי חייא'],'Babylonian named Rabbi Hiyya objects with Psalm95:5')
cone=claim('written_hand','5a:12','ידו כתיב','The anonymous reply says that the written form is singular, his hand.',status='Textual reply within the sugya; not an independent manuscript collation')
qp=q('plural_verb','5a:12','והכתיב יצרו','Does the verse not use the plural verb formed?')
cf=claim('fingers','5a:12','א"ר נחמן בר יצחק יצרו אצבעותיו כדכתיב (תהלים ח, ד) כי אראה שמיך מעשה אצבעותיך ירח וכוכבים אשר כוננת','Rav Nahman bar Yitzhak explains the plural as fingers forming, supported by Psalm8:4’s work of fingers.',holder=['רב נחמן בר יצחק'])
attr('nahman','5a:12','א"ר נחמן בר יצחק','רב נחמן בר יצחק','speaker',['רב נחמן בר יצחק'],'Plural verb interpreted as fingers')
edge('hiyya_objection','5a:12','השיב בבלי אחד',qhands,cg,'objection');edge('singular_answer','5a:12','ידו כתיב',cone,qhands,'answer');edge('plural_objection','5a:12','והכתיב יצרו',qp,cone,'objection');edge('fingers_answer','5a:12','יצרו אצבעותיו',cf,qp,'answer')
qr=q('firmament','5a:13','מיתיבי (תהלים יט, ב) השמים מספרים כבוד אל ומעשה ידיו מגיד הרקיע','An objection cites Psalm19:2: the firmament declares the work of His hands.')
cr=claim('rain','5a:13','הכי קאמר מעשה ידיהם של צדיקים מי מגיד הרקיע ומאי ניהו מטר','The reply reads the verse as the firmament declaring the righteous persons’ handiwork through rain.',status='Homiletic reinterpretation answering objection')
qrain=q('what_declares','5a:13','ומאי ניהו','What is the firmament’s declaration in this interpretation?')
edge('firmament_objection','5a:13','מיתיבי',qr,cg,'objection');edge('rain_reply','5a:13','הכי קאמר',cr,qr,'answer');edge('rain_identification','5a:13','מטר',cr,qrain,'answer')
qh=q('peg_verse','5a:14','דרש בר קפרא מאי דכתיב (דברים כג, יד) ויתד תהיה לך על אזנך','Bar Kappara asks what Deuteronomy23:14’s peg instruction means in this homily.')
cword=claim('ear_reading','5a:14','אל תקרי אזנך אלא על אוזנך','Bar Kappara homiletically reads the word as referring to one’s ear.',holder=['בר קפרא'],status='Al-tiqre homily; not a replacement of the original source text')
add('c.ear_instruction','claims',['5a:14','5b:1'],dict(proposition='If a person hears an improper matter, he should put his finger into his ears.',conditions=['Hearing an improper matter'],scope='Bar Kappara’s ear homily continuing across page',assertion_mode='conditional'))
add('p.ear_instruction','positions',['5a:14','5b:1'],dict(holder_candidates=['בר קפרא'],claim_id=prefix+'c.ear_instruction',question_id=None,conditions=['Hearing an improper matter'],local_status='Homiletic ethical instruction'),links=[prefix+'c.ear_instruction'])
attr('kappara_ears','5a:14','דרש בר קפרא','בר קפרא','speaker',['בר קפרא'],'Peg/ear homily continued at5b:1')
edge('homily_answer','5a:14','אל תקרי אזנך אלא על אוזנך',cword,qh,'answer');edge('homily_instruction','5b:1','יניח אצבעו באזניו',prefix+'c.ear_instruction',cword,'local_resolution')
qf=q('finger_form','5b:1','והיינו דאמר ר\' אלעזר מפני מה אצבעותיו של אדם דומות ליתידות','Rabbi Elazar asks why human fingers resemble pegs.')
attr('elazar','5b:1','דאמר ר\' אלעזר','רבי אלעזר','quoted_authority',['רבי אלעזר'],'Finger shape question')
qdivision=q('separation','5b:1','מאי טעמא אילימא משום דמחלקן','Is the question about why fingers are divided?')
cfunctions=claim('functions','5b:1','כל חדא וחדא למילתיה עבידא דאמר מר זו זרת זו קמיצה זו אמה זו אצבע זה גודל','Each finger already has its distinct function, with the cited list: little finger, kemitzah finger, middle finger, index finger, thumb.',status='Reply rejecting division as the intended shape question; no unstated ritual functions imported')
edge('division_answer','5b:1','כל חדא וחדא למילתיה עבידא',cfunctions,qdivision,'answer')
qpoint=q('pointed','5b:2','אלא מה טעם משופות כיתידות','Rather, why are fingers tapered like pegs?')
cear=claim('finger_plugs','5b:2','שאם ישמע אדם דבר שאינו הגון יניח אצבעותיו באזניו','Their peg-like shape enables putting fingers in the ears upon hearing an improper matter.',['Hearing an improper matter'],status='Answer interpreting Rabbi Elazar’s question')
edge('question_refine','5b:2','אלא מה טעם משופות כיתידות',qpoint,qf,'correction');edge('point_answer','5b:2','שאם ישמע אדם דבר שאינו הגון יניח אצבעותיו באזניו',cear,qpoint,'answer')
qlobe=q('soft_lobe','5b:2','תנא דבי רבי ישמעאל מפני מה אוזן כולה קשה והאליה רכה','The school of Rabbi Yishmael asks why the ear is hard but its lobe is soft.')
clobe=claim('lobe_plug','5b:2','שאם ישמע אדם דבר שאינו הגון יכוף אליה לתוכה','Upon hearing an improper matter one can fold the earlobe inward.',['Hearing an improper matter'],holder=['תנא דבי רבי ישמעאל'])
attr('yishmael','5b:2','תנא דבי רבי ישמעאל','תנא דבי רבי ישמעאל','collective',['תנא דבי רבי ישמעאל'],'Soft earlobe instruction')
cidle=claim('idle_speech','5b:2','ת"ר אל ישמיע אדם לאזניו דברים בטלים','The sages teach that one should not let one’s ears hear idle matters.',holder=['quoted sages'])
cburn=claim('ears_first','5b:2','מפני שהן נכוות תחלה לאיברים','The supplied reason is that ears are burned before the other limbs.',holder=['quoted sages'],status='Source’s ethical warning, not an empirical physiology assertion')
edge('lobe_answer','5b:2','יכוף אליה לתוכה',clobe,qlobe,'answer');edge('warning_reason','5b:2','מפני שהן נכוות תחלה לאיברים',cburn,cidle,'support')
for x in records:
 if x['layer']=='claims':x['content']['scope']='Homiletic and ethical discourse, Ketubot5a:11–5b:2; no later legal or empirical inference'
coverage=[]
for ref in core:
 sid=byref[ref]['id']
 for layer in r.LAYERS:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  rationale='Manual '+layer+' pass over '+ref+'; '+('reread verse citations, textual/homiletic replies, page-crossing instruction, finger function and shape distinction, lobe and idle-speech warning; no further local unit omitted' if layer=='reconciliation' else 'source-explicit homiletic voices, questions, and replies retained separately from editorial explanation')
  if not ids:rationale+='; no separate finding in this layer'
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=r.current(job)['open_tails'])
r.validate_apply(r.current(job),p,segments,j);path=out/'batch003_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'batch003_receipt.json',r.encoded(receipt));print(receipt)
