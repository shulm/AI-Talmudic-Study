from pathlib import Path
exec((Path(__file__).parent/'batch001.py').read_text(encoding='utf-8').split("add('s.baraita'")[0])
prefix='kt.resume26.b2.'
add('s.army','structure',['3b:7','3b:8'],dict(title='Coercion: army commander arriving and staying',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
tail=add('s.mourning','structure',['3b:9']+['4a:'+str(n) for n in range(1,7)],dict(title='Alternative coercion: prepared feast and bereavement; discussion continues',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('3b:7','anonymous discussion quoting baraita','question and rejected identification'),('3b:8','Rava and anonymous discussion','interpretation, conditions, objections and replies'),('3b:9','anonymous alternative quoting baraita','alternative interpretation of coercion'),('4a:1','quoted baraita','intercourse, celebration, mourning, separation and adornments'),('4a:2','anonymous discussion','restriction by identity of deceased and preparation assistance'),('4a:3','Rafram bar Pappa reporting Rav Hisda','qualification by meat preparation'),('4a:4','Rava, Rav Pappa, anonymous question, and Rav Ashi','urban/rural market distinctions'),('4a:5','anonymous introduction quoting baraita','support for Rav Hisda and repeated mourning rules'),('4a:6','quoted baraita','menstrual separation, adornments, timing restrictions')]:
 add('u.'+ref,'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
qo=q('coercion','3b:7','מאי אונס','What coercion permits Monday marriage?',['Monday exception in baraita'])
ch=claim('same_danger','3b:7','אילימא הא דאמרן','The previously described danger is proposed, then rejected as the meaning of coercion here.',mode='rejected',status='Rejected identification')
qn=q('terminology','3b:7','התם קרי ליה סכנה והכא קא קרי ליה אונס','Why call the same event danger there but coercion here?',['Proposed same-event interpretation'])
qm=q('permission','3b:7','ותו התם נהגו הכא מותר','Why is it tolerated practice there but explicit permission here?',['Proposed same-event interpretation'])
edge('terminology','3b:7','התם קרי ליה סכנה והכא קא קרי ליה אונס',qn,ch,'objection');edge('permission','3b:7','ותו התם נהגו הכא מותר',qm,ch,'objection')
cc=claim('commander','3b:8','אמר רבא דאמרי שר צבא בא לעיר','Rava interprets coercion as the announced arrival of an army commander in the city.',holder=['רבא'],status='First interpretation; further qualified locally')
attr('rava','3b:8','אמר רבא','רבא','speaker',['רבא'],'Army commander interpretation; Rava distinct from earlier Rabbah')
qp=q('passing','3b:8','ה"ד אי דאתי וחליף ליעכב','If the commander merely passes through, why not wait?',['Commander only passing through'])
cs=claim('stays','3b:8','לא צריכא דאתי וקבע','The case is one in which the commander comes and stays.',['Commander coming and staying'])
qt=q('tuesday','3b:8','בג\' מיהא לכנוס','Why not at least marry Tuesday?',['Commander comes and stays'])
ct=claim('entourage','3b:8','אספרווא דידיה בג\' קאתו','The commander’s entourage arrives on Tuesday.',['Commander comes and stays; entourage arrives Tuesday'])
edge('commander','3b:8','אמר רבא דאמרי שר צבא בא לעיר',cc,qo,'answer');edge('passing','3b:8','אי דאתי וחליף ליעכב',qp,cc,'objection');edge('stays','3b:8','לא צריכא דאתי וקבע',cs,qp,'answer');edge('entourage','3b:8','אספרווא דידיה בג\' קאתו',ct,qt,'answer')
cond=['Bread baked, animal slaughtered, wine mixed','Groom’s father or bride’s mother has died','Further locality/meat qualifications at 4a:2–4']
cd=claim('death_alternative','3b:9','ואיבעית אימא מאי מחמת האונס כדתני\'','An alternative interpretation of coercion invokes the bereavement baraita that follows.',['Bereavement after wedding feast preparation'],status='Alternative to army-commander interpretation, not a retraction')
edge('alternative','3b:9','ואיבעית אימא מאי מחמת האונס',cd,qo,'answer')
cb=claim('chamber','3b:9','מכניסין את המת לחדר ואת החתן ואת הכלה לחופה','The deceased is placed in a room and the bridegroom and bride are brought to the wedding canopy.',cond,holder=['quoted baraita'])
ci=claim('intercourse','4a:1','ובועל בעילת מצוה ופורש','The bridegroom performs the initial mitzvah intercourse, then separates.',cond,holder=['quoted baraita'])
cf=claim('order','4a:1','ונוהג שבעת ימי המשתה ואחר כך נוהג שבעת ימי אבילות','Seven days of celebration precede seven days of mourning.',cond,holder=['quoted baraita'])
csleep=claim('sleep','4a:1','וכל אותן הימים הוא ישן בין האנשים והיא ישנה בין הנשים','Throughout those days he sleeps among men and she among women.',cond+['Celebration and mourning days in this case'],holder=['quoted baraita'],status='Mourning separation; later discussion qualifies relation to menstrual case')
cad=claim('adorn','4a:1','ואין מונעין תכשיטין מן הכלה כל שלשים יום','The bride is not deprived of adornments for thirty days.',cond,holder=['quoted baraita'])
cwho=claim('parent_identity','4a:2','ודוקא אביו של חתן או אמה של כלה דליכא איניש דטרח להו אבל איפכא לא','The concession specifically concerns the groom’s father or bride’s mother, because no one else will prepare for them; the converse parental deaths do not qualify.',cond[:2],status='Local restriction of bereavement concession')
edge('parent_restrict','4a:2','ודוקא אביו של חתן או אמה של כלה דליכא איניש דטרח להו אבל איפכא לא',cwho,cb,'qualification')
cw=claim('water','4a:3','לא שנו אלא שנתן מים על גבי בשר אבל לא נתן מים על גבי בשר מזדבן','Rav Hisda limits the concession to meat on which water was put; without water the meat can be sold.',cond[:2]+['Market locality clarified at 4a:4','Water placed on meat'],holder=['רב חסדא'])
attr('rafram','4a:3','אמר רפרם בר פפא אמר רב חסדא','רפרם בר פפא','transmitter',['רפרם בר פפא'],'Water-on-meat restriction',['רפרם בר פפא','רב חסדא'])
attr('hisda','4a:3','אמר רב חסדא','רב חסדא','quoted_authority',['רב חסדא'],'Water-on-meat restriction',['רפרם בר פפא','רב חסדא'])
edge('water_restrict','4a:3','לא שנו אלא שנתן מים על גבי בשר אבל לא נתן מים על גבי בשר מזדבן',cw,cb,'qualification')
cu=claim('city','4a:4','אמר רבא ובכרך אע"פ שנתן מים על גבי בשר מזדבן','Rava says that in a large city meat can be sold even after water was put on it.',['Large city','Water already put on meat'],holder=['רבא'])
cv=claim('village','4a:4','אמר רב פפא ובכפר אע"פ שלא נתן מים על גבי בשר לא מזדבן','Rav Pappa says that in a village meat cannot be sold even before water is put on it.',['Village','No water put on meat'],holder=['רב פפא'])
ql=q('locality','4a:4','ואלא דרב חסדא היכי משכחת לה','Where does Rav Hisda’s distinction apply?',['Contrasted city and village markets'])
cma=claim('mehasya','4a:4','אמר רב אשי כגון מתא מחסיא דמפקא מכרך ומפקא מכפר','Rav Ashi locates Rav Hisda’s rule in a place like Mata Mehasya, intermediate between large city and village.',['Intermediate locality such as Mata Mehasya'],holder=['רב אשי'])
for key,quote,name in [('rava_city','אמר רבא','רבא'),('pappa','אמר רב פפא','רב פפא'),('ashi','אמר רב אשי','רב אשי')]:attr(key,'4a:4',quote,name,'speaker',[name],'Locality qualification of marketability')
edge('city','4a:4','ובכרך אע"פ שנתן מים על גבי בשר מזדבן',cu,cw,'qualification');edge('village','4a:4','ובכפר אע"פ שלא נתן מים על גבי בשר לא מזדבן',cv,cw,'qualification');edge('mehasya','4a:4','כגון מתא מחסיא דמפקא מכרך ומפקא מכפר',cma,ql,'answer')
cond2=['Bread baked, animal slaughtered, wine mixed','Water put on meat','Groom’s father or bride’s mother has died','Read with locality distinction at 4a:4']
cproof=claim('baraita_support','4a:5','תניא כוותיה דרב חסדא','A baraita is introduced as supporting Rav Hisda’s restriction.',status='Explicit source support claim')
edge('baraita_support','4a:5','תניא כוותיה דרב חסדא',cproof,cw,'support')
for key,quote,text in [('chamber_repeat','מכניסין את המת לחדר ואת החתן ואת הכלה לחופה','The deceased goes to a room and the couple to the wedding canopy.'),('intercourse_repeat','ובועל בעילת מצוה ופורש','Initial mitzvah intercourse is followed by separation.'),('order_repeat','ונוהג שבעת ימי המשתה ואח"כ נוהג שבעת ימי אבילות','Seven celebration days precede seven mourning days.'),('sleep_repeat','וכל אותן הימים הוא ישן בין האנשים ואשתו ישנה בין הנשים','Throughout those days he sleeps among men and his wife among women.')]:
 claim(key,'4a:5',quote,text,cond2,holder=['quoted supporting baraita'],status='Parallel occurrence retained; continued qualifications discussed below')
cn=claim('niddah','4a:6','וכן מי שפירסה אשתו נדה הוא ישן בין האנשים והיא ישנה בין הנשים','When the wife becomes menstruant, he sleeps among men and she among women.',['Wife has become menstruant','Restricted later at 4a:8–4b:1 to no prior intercourse'],holder=['quoted baraita'],status='Initial baraita formulation; later no-prior-intercourse qualification preserved here')
claim('adorn_repeat','4a:6','ואין מונעין תכשיטין מן הכלה כל ל\' יום','The bride is not deprived of adornments for thirty days.',['Bride in the baraita’s cases'],holder=['quoted baraita'])
claim('evenings','4a:6','בין כך ובין כך לא יבעול לא בערב שבת ולא במוצ"ש','In either case first intercourse is not to occur on Sabbath eve or Saturday night.',['Initial intercourse','Both cases referenced by baraita'],holder=['quoted baraita'],status='Rationale discussed beginning 4b:11; not completed by this extraction core')
core=['3b:7','3b:8','3b:9']+['4a:'+str(n) for n in range(1,7)];coverage=[]
for ref in core:
 sid=byref[ref]['id']
 for layer in r.LAYERS:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  rationale='Manual '+layer+' pass over '+ref+'; '+('source reread for omitted repeated rules, conditions, alternative explanation, authority/transmitter distinction, and 4b continuation; open mourning discussion retained' if layer=='reconciliation' else 'source-local units and repeated occurrences retained; downstream qualifications read through 4b:12')
  if not ids and layer!='reconciliation':rationale+='; no additional supported '+layer+' unit identified'
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=r.current(job)['open_tails']+[tail])
r.validate_apply(r.current(job),p,segments,j);path=out/'batch002_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'batch002_receipt.json',r.encoded(receipt));print(receipt)
