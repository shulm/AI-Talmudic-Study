from pathlib import Path
exec((Path(__file__).parent.parent/'worker_20261126/batch001.py').read_text(encoding='utf-8').split("add('s.baraita'")[0])
prefix='kt.wave2.b1.'
core=['4b:11','4b:12']+['5a:'+str(n) for n in range(1,6)]
add('s.evenings','structure',core,dict(title='Sabbath-adjacent intercourse: accounting explanation rejected, slaughter concern substituted',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('4b:11','anonymous discussion quoting baraita','restriction, accepted Friday rationale and Saturday-night question'),('4b:12','Rabbi Zeira','speaker introduction continuing into5a:1'),('5a:1','Rabbi Zeira','initial rationale subsequently replaced'),('5a:2','Abaye quoting named authorities','objection and permitted Sabbath public/mitzvah activities'),('5a:3','continuation of Abaye’s quoted authorities','further permitted Sabbath mitzvah activities'),('5a:4','Rabbi Zeira, Abaye, and anonymous responses','revised rationale, objection, two answers'),('5a:5','anonymous discussion','extension of revised rationale to Sabbath eve')]:
 add('u.'+ref,'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='atomic' if ref in ['4b:12','5a:1'] else 'composite'))
cf=claim('friday_wound','4b:11','בשלמא בערב שבת משום חבורה','The discussion initially accepts wounding as the reason to prohibit initial intercourse on Sabbath eve.',['Initial intercourse on Sabbath eve'],status='Accepted at this stage; an additional rationale is supplied at5a:5')
qnight=q('saturday','4b:11','אלא במוצאי שבת אמאי לא','Why prohibit initial intercourse on Saturday night?',['Initial intercourse on Saturday night'])
cacc=claim('accounts','5a:1','משום חשבונות','Rabbi Zeira initially explains the Saturday-night restriction by concern over accounts.',['Saturday-night wedding preparations and Sabbath accounts'],mode='retracted',holder=['רבי זירא'],status='Initial explanation replaced at5a:4 after Abaye’s objection')
# Attribution evidence spans the actual page break rather than guessing from proximity.
add('a.zeira_initial','attributions',['4b:12','5a:1'],dict(surface='אמר רבי זירא ... משום חשבונות',role='speaker',candidates=['רבי זירא'],scope='Initial accounting rationale across page break',transmission_chain=[]))
edge('accounts_answer','5a:1','משום חשבונות',cacc,qnight,'answer')
qacc=q('mitzvah_accounts','5a:2','אמר ליה אביי וחשבונות של מצוה מי אסירי','Abaye asks whether accounts for a mitzvah are prohibited.',['Sabbath mitzvah-related accounts'])
attr('abaye_accounts','5a:2','אמר ליה אביי','אביי','speaker',['אביי'],'Objection to accounting rationale')
cpermit=claim('accounts_permitted','5a:2','רב חסדא ורב המנונא דאמרי תרוייהו חשבונות של מצוה מותר לחשבן בשבת','Rav Hisda and Rav Hamnuna both permit calculating accounts for a mitzvah on Sabbath.',['Accounts for a mitzvah','Sabbath'],holder=['רב חסדא','רב המנונא'])
for key,name in [('hisda','רב חסדא'),('hamnuna','רב המנונא')]:attr(key,'5a:2','רב חסדא ורב המנונא דאמרי תרוייהו',name,'quoted_authority',[name],'Joint permission of mitzvah accounts on Sabbath')
cc=claim('charity','5a:2','וא"ר אלעזר פוסקין צדקה לעניים בשבת','Rabbi Elazar permits allocating charity for the poor on Sabbath.',['Charity for poor','Sabbath'],holder=['רבי אלעזר'])
attr('elazar','5a:2','וא"ר אלעזר','רבי אלעזר','quoted_authority',['רבי אלעזר'],'Charity allocation')
cp=claim('public','5a:2','ואמר ר\' יעקב אמר ר\' יוחנן הולכין לבתי כנסיות ולבתי מדרשות לפקח על עסקי רבים בשבת','Rabbi Yaakov reports Rabbi Yohanan: one may visit synagogues and study houses to attend to public affairs on Sabbath.',['Public affairs','Sabbath'],holder=['רבי יוחנן'])
attr('yaakov','5a:2','ר\' יעקב אמר ר\' יוחנן','רבי יעקב','transmitter',['רבי יעקב'],'Public affairs',['רבי יעקב','רבי יוחנן'])
attr('yohanan_public','5a:2','ר\' יעקב אמר ר\' יוחנן','רבי יוחנן','quoted_authority',['רבי יוחנן'],'Public affairs',['רבי יעקב','רבי יוחנן'])
cl=claim('life','5a:2','ואמר רבי יעקב בר אידי אמר רבי יוחנן מפקחין פיקוח נפש בשבת','Rabbi Yaakov bar Idi reports Rabbi Yohanan: one attends to preservation of life on Sabbath.',['Preservation of life','Sabbath'],holder=['רבי יוחנן'])
attr('yaakov_idi','5a:2','רבי יעקב בר אידי אמר רבי יוחנן','רבי יעקב בר אידי','transmitter',['רבי יעקב בר אידי'],'Preservation of life',['רבי יעקב בר אידי','רבי יוחנן'])
attr('yohanan_life','5a:2','רבי יעקב בר אידי אמר רבי יוחנן','רבי יוחנן','quoted_authority',['רבי יוחנן'],'Preservation of life',['רבי יעקב בר אידי','רבי יוחנן'])
ct=claim('venues','5a:3','הולכין לטרטייאות ולקרקייאות לפקח על עסקי רבים בשבת','Rabbi Yonatan, reported by Rav Shmuel bar Nahmani, permits going to the named public entertainment venues to attend to public affairs on Sabbath.',['Public affairs','Sabbath'],holder=['רבי יונתן'],status='Names טרטייאות/קרקייאות retained in evidence; no venue-specific legal extension')
attr('shmuel','5a:3','ואמר רב שמואל בר נחמני אמר רבי יונתן','רב שמואל בר נחמני','transmitter',['רב שמואל בר נחמני'],'Public affairs at named venues',['רב שמואל בר נחמני','רבי יונתן'])
attr('yonatan','5a:3','ואמר רב שמואל בר נחמני אמר רבי יונתן','רבי יונתן','quoted_authority',['רבי יונתן'],'Public affairs at named venues',['רב שמואל בר נחמני','רבי יונתן'])
cm=claim('matchmaking','5a:3','ותנא דבי מנשיא משדכין על התינוקת ליארס בשבת','The school of Menashya teaches that one may arrange a girl’s betrothal on Sabbath.',['Arranging betrothal','Sabbath'],holder=['תנא דבי מנשיא'])
ce=claim('education','5a:3','ועל התינוק ללמדו ספר וללמדו אומנות','The same teaching permits arranging a boy’s instruction in Scripture and a trade.',['Arranging instruction','Sabbath'],holder=['תנא דבי מנשיא'])
attr('menashya','5a:3','ותנא דבי מנשיא','תנא דבי מנשיא','collective',['תנא דבי מנשיא'],'Matchmaking and educational arrangements')
edge('abaye_objection','5a:2','וחשבונות של מצוה מי אסירי',qacc,cacc,'objection')
for key,ref,quote,c in [('accounts','5a:2','חשבונות של מצוה מותר לחשבן בשבת',cpermit),('charity','5a:2','פוסקין צדקה לעניים בשבת',cc),('public','5a:2','הולכין לבתי כנסיות ולבתי מדרשות לפקח על עסקי רבים בשבת',cp),('life','5a:2','מפקחין פיקוח נפש בשבת',cl),('venues','5a:3','לפקח על עסקי רבים בשבת',ct),('match','5a:3','משדכין על התינוקת ליארס בשבת',cm),('education','5a:3','ועל התינוק ללמדו ספר וללמדו אומנות',ce)]:edge('support_'+key,ref,quote,c,qacc,'support')
cb=claim('bird','5a:4','אלא אמר רבי זירא גזירה שמא ישחוט בן עוף','Rabbi Zeira substitutes a decree against the risk of slaughtering a young bird.',['Sabbath preparations for Saturday-night wedding'],holder=['רבי זירא'],status='Revised rationale after accounting objection')
attr('zeira_revised','5a:4','אלא אמר רבי זירא','רבי זירא','speaker',['רבי זירא'],'Revised slaughter rationale')
edge('replace_accounts','5a:4','אלא אמר רבי זירא',cb,cacc,'correction');edge('bird_answer','5a:4','גזירה שמא ישחוט בן עוף',cb,qnight,'answer')
qyk=q('kippur','5a:4','א"ל אביי אלא מעתה יום הכפורים שחל להיות בשני בשבת ידחה גזירה שמא ישחוט בן עוף','Abaye asks whether Yom Kippur falling Monday should then be postponed because of the same slaughter risk.',['Yom Kippur on Monday','Analogy to pre-event preparations'])
attr('abaye_kippur','5a:4','א"ל אביי','אביי','speaker',['אביי'],'Yom Kippur objection')
cs=claim('self_other','5a:4','התם דלנפשיה לא טריד הכא דלאחרים טריד','For Yom Kippur he prepares for himself and is not preoccupied; here he prepares for others and is preoccupied.',['Comparison of pre-Yom-Kippur meal and wedding for others'],status='First anonymous distinction')
ctime=claim('time','5a:4','אי נמי התם אית ליה רווחא הכא לית ליה רווחא','Alternatively, the Yom Kippur case leaves time, whereas the wedding case does not.',['Comparison of preparations in the two cases'],status='Alternative anonymous distinction; not combined into a single necessary condition')
edge('kippur_objection','5a:4','אלא מעתה יום הכפורים שחל להיות בשני בשבת ידחה',qyk,cb,'objection');edge('self_answer','5a:4','התם דלנפשיה לא טריד הכא דלאחרים טריד',cs,qyk,'answer');edge('time_answer','5a:4','אי נמי התם אית ליה רווחא הכא לית ליה רווחא',ctime,qyk,'answer')
cfr=claim('friday_bird','5a:5','השתא דאתית להכי ערב שבת נמי גזירה שמא ישחוט בן עוף','The discussion extends the bird-slaughter concern to Sabbath eve as well.',['Initial intercourse on Sabbath eve'],status='Additional rationale following revised explanation')
edge('extension','5a:5','ערב שבת נמי גזירה שמא ישחוט בן עוף',cfr,cf,'qualification')
for x in records:
 if x['layer']=='claims':x['content']['scope']='Sabbath-adjacent wedding preparation argument, Ketubot4b:11–5a:5'
coverage=[]
for ref in core:
 sid=byref[ref]['id']
 for layer in r.LAYERS:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  rationale='Manual '+layer+' pass over '+ref+'; '+('reread page-crossing speaker, replaced rationale, named transmission chains, seven counterexamples, and alternative replies; no additional omitted local unit identified' if layer=='reconciliation' else 'source-local units and required continuation read through5a:5; new topic begins5a:6')
  if not ids:rationale+='; no separate record in this layer (speaker stub at4b:12 is not an independent claim)' if ref=='4b:12' else '; no additional supported finding in this layer'
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=r.current(job)['open_tails'])
r.validate_apply(r.current(job),p,segments,j);path=out/'batch001_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'batch001_receipt.json',r.encoded(receipt));print(receipt)
