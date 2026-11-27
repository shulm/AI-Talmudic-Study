from pathlib import Path
exec((Path(__file__).parent.parent/'worker_20261126/batch001.py').read_text(encoding='utf-8').split("add('s.baraita'")[0])
prefix='kt.wave3.b3.';core=['12a:'+str(n) for n in range(7,14)]
add('s.custom','structure',core,dict(title='Judean and Galilean marriage customs and three readings of the claim restriction',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('12a:7','Mishnah','Judean seclusion and loss of claim'),('12a:8','anonymous discussion, Abaye, quoted Rabbi Yehuda','regional inference and prior-seclusion practice'),('12a:9','quoted baraita','two attendants inspect bridegroom and bride'),('12a:10','quoted baraita','attendants sleep in the couple’s house'),('12a:11','quoted baraita and anonymous question','ambiguous condition and first-clause objection'),('12a:12','anonymous discussion','last-clause wording objection'),('12a:13','Abaye, Rava, Rav Ashi','competing emendations and regional interpretation')]:add('u.'+ref,'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
cm=claim('mishnah','12a:7','האוכל אצל חמיו ביהודה שלא בעדים אינו יכול לטעון טענת בתולים מפני שמתייחד עמה','One dining at his father-in-law’s in Judea without witnesses cannot raise a virginity claim because he secluded himself with her.',['Judea','Dining at father-in-law’s without witnesses'],holder=['Mishnah'])
cl=claim('localities','12a:8','אמר אביי ש"מ ביהודה נמי מקומות מקומות יש','Abaye infers that Judea itself contains different local practices.',['Mishnah says the one who dines, implying some do not'],holder=['אביי'])
edge('locality_inference','12a:8','מדקתני האוכל מכלל דאיכא דוכתא ביהודה נמי דלא אכיל',cm,cl,'support')
cs=claim('seclusion','12a:8','ביהודה בראשונה היו מייחדין את החתן ואת הכלה שעה אחת קודם כניסתן לחופה כדי שיהא לבו גס בה','Rabbi Yehuda reports that originally in Judea the couple were secluded for an hour before huppah so that he would be familiar with her.',['Original Judean custom'],holder=['רבי יהודה'])
cg=claim('no_seclusion','12a:8','ובגליל לא היו עושין כן','Galilee did not practice that prior seclusion.',['Galilean practice','Prior seclusion before huppah'],holder=['רבי יהודה'])
ca=claim('attendants','12a:9','ביהודה בראשונה היו מעמידין להם שני שושבינין אחד לו ואחד לה כדי למשמש את החתן ואת הכלה בשעת כניסתן לחופה','Originally in Judea two attendants, one for each party, inspected bridegroom and bride on entering huppah.',['Original Judean custom'],holder=['quoted baraita'])
cga=claim('no_attendants','12a:9','ובגליל לא היו עושין כן','Galilee did not use that inspection practice.',['Galilean practice','Two-attendant inspection'],holder=['quoted baraita'])
csleep=claim('sleep','12a:10','ביהודה בראשונה היו שושבינין ישנים בבית שחתן וכלה ישנים בה','Originally in Judea attendants slept in the house where the couple slept.',['Original Judean custom'],holder=['quoted baraita'])
cgsleep=claim('no_sleep','12a:10','ובגליל לא היו עושין כן','Galilee did not use that attendants’ sleeping practice.',['Galilean practice','Attendants sleeping in the couple’s house'],holder=['quoted baraita'])
cc=claim('ambiguous_condition','12a:11','וכל שלא נהג כמנהג הזה אינו יכול לטעון טענת בתולים','The baraita’s received wording denies the claim to one who did not follow this custom; the referent and wording are then disputed.',['Unresolved referent of this custom'],mode='unresolved',holder=['quoted baraita'],status='Wording interpreted or emended in three ways below')
qr=q('referent','12a:11','אהייא','Which earlier clause does the concluding condition concern?')
qfirst=q('first_wording','12a:11','אילימא ארישא כל שנהג מיבעי ליה','If it concerns the first clause, should it not say whoever followed the custom?',['First clause: prior seclusion'])
qlast=q('last_wording','12a:12','אלא אסיפא כל שלא מושמש מיבעי ליה','If it concerns the last portion, should it not say whoever was not inspected?',['Inspection portion'])
edge('first_objection','12a:11','כל שנהג מיבעי ליה',qfirst,cc,'objection');edge('last_objection','12a:12','כל שלא מושמש מיבעי ליה',qlast,cc,'objection')
cab=claim('abaye','12a:13','אמר אביי לעולם ארישא ותני כל שנהג','Abaye applies the condition to the first clause and emends it to whoever followed the custom.',['Prior-seclusion clause','Emended wording'],holder=['אביי'],status='Proposed reading challenged by Rava; not silently substituted into the quotation')
qrv=q('rava_text','12a:13','אמר ליה רבא והא כל שלא נהג קתני','Rava objects that the baraita actually says whoever did not follow.',['Abaye’s emendation'])
crv=claim('rava','12a:13','כל שלא נהג מנהג גליל בגליל אלא מנהג יהודה בגליל אינו יכול לטעון טענת בתולים','Rava reads the condition as someone in Galilee following Judean rather than Galilean custom; that person cannot raise the virginity claim.',['In Galilee','Follows Judean instead of Galilean custom'],holder=['רבא'],status='Regional interpretation preserving the negative wording')
cash=claim('ashi','12a:13','רב אשי אמר לעולם אסיפא ותני כל שלא מושמש','Rav Ashi applies it to the latter portion and emends the condition to whoever was not inspected.',['Inspection portion','Emended wording'],holder=['רב אשי'],status='Alternative textual reading; no explicit final selection among readings')
edge('abaye_answer','12a:13','לעולם ארישא',cab,qr,'answer');edge('abaye_correction','12a:13','ותני כל שנהג',cab,cc,'correction')
edge('rava_objection','12a:13','והא כל שלא נהג קתני',qrv,cab,'objection');edge('rava_answer','12a:13','אלא אמר רבא הכי קאמר',crv,qr,'answer')
edge('ashi_answer','12a:13','לעולם אסיפא',cash,qr,'answer');edge('ashi_correction','12a:13','ותני כל שלא מושמש',cash,cc,'correction')
attr('abaye_inference','12a:8','אמר אביי','אביי','speaker',['אביי'],'Inference of diverse Judean localities')
attr('yehuda','12a:8','א"ר יהודה','רבי יהודה','quoted_authority',['רבי יהודה'],'Quoted baraita of original regional practices; Rabbi Yehuda, not Rav Yehuda')
attr('abaye_reading','12a:13','אמר אביי','אביי','speaker',['אביי'],'First-clause textual correction')
attr('rava','12a:13','אמר ליה רבא','רבא','speaker',['רבא'],'Objection to Abaye and subsequent regional interpretation')
attr('ashi','12a:13','רב אשי אמר','רב אשי','speaker',['רב אשי'],'Inspection-clause textual correction')
for x in records:
 if x['layer']=='claims':x['content']['scope']='Regional marriage customs and claim restrictions, Ketubot12a:7–13'
coverage=[]
for ref in core:
 sid=byref[ref]['id']
 for layer in r.LAYERS:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  rationale='Manual '+layer+' pass over '+ref+'; '+('reread local diversity, seclusion, inspection and sleeping customs separately, the ambiguous concluding condition, both wording objections and all three readings through the closed ending' if layer=='reconciliation' else 'conditions and competing readings preserved without selecting a final ruling')
  if not ids:rationale+='; no additional supported finding in this layer'
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=r.current(job)['open_tails'])
r.validate_apply(r.current(job),p,segments,j);path=out/'batch003_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'batch003_receipt.json',r.encoded(receipt));print(receipt)
