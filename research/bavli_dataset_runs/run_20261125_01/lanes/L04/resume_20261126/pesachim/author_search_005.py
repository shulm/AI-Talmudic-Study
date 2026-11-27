"""Manual source reading, 4a:5–4b:7; source-bound proposals only."""
from author_opening_001 import *
records.clear()
groups=[('timing',['4a:'+str(i) for i in range(5,9)],'Why search at night and avoid study at that time'),('renter',['4a:9','4a:10'],'Landlord or tenant: key-transfer boundary'),('presumption',['4a:11','4a:12']+['4b:'+str(i) for i in range(1,6)],'Presumed search and trust in reported rabbinic search'),('mistake',['4b:6','4b:7'],'Lease on a searched-house assumption when the house was not searched')]
for key,scope,title in groups: add('b5.'+key,'structure',dict(title=title,primary=True,boundary='closed',legacy_ids=[]),[ev(x) for x in scope],origin='editorial_inference')
ag=claim('b5.agreement','4a:5','והשתא דקיימא לן דלכולי עלמא אור אורתא הוא','The discussion resumes from the established result that all agree אור means night.',mode='reconciled',scope='Explicit recall of 3a:9')
time=claim('b5.time','4a:5',"מכדי בין לרבי יהודה ובין לר' מאיר חמץ אינו אסור אלא משש שעות ולמעלה",'The premise here is that for both Rabbi Yehuda and Rabbi Meir leaven is prohibited only from six hours upward.',scope='Premise for search-time question; exact source time expression retained')
q6=question('b5.six.q','4a:5','ונבדוק בשית','Why not search in the sixth hour?')
zealous=claim('b5.zealous','4a:6','וכי תימא זריזין מקדימין למצות','A proposed explanation invokes the zealous hastening to commandments.',mode='hypothetical',scope='Tentative reason for earlier search')
morning=question('b5.morning.q','4a:6','נבדוק מצפרא','Why not search in the morning?')
circum=claim('b5.circum','4a:6','דכתיב (ויקרא יב, ג) וביום השמיני ימול בשר ערלתו ותניא כל היום כולו כשר למילה','The eighth-day circumcision verse and teaching permit circumcision throughout the day.',conditions=['eighth-day circumcision'],scope='Cited example, not search rule')
early=claim('b5.early','4a:6','אלא שזריזין מקדימים למצות שנאמר (בראשית כב, ג) וישכם אברהם בבקר','The zealous nevertheless act early, as supported by Abraham rising early in the morning.',scope='Cited diligence principle')
edge('b5.early.support',early,zealous,'support','4a:6');edge('b5.morning.objection',morning,zealous,'objection','4a:6')
home=claim('b5.home','4a:7','אמר רב נחמן בר יצחק בשעה שבני אדם מצויין בבתיהם','Rav Nahman bar Yitzhak explains that people are at home then.',holder='רב נחמן בר יצחק',conditions=['night search time'],scope='First reason for nighttime search')
light=claim('b5.light','4a:7','ואור הנר יפה לבדיקה','Candlelight is good for the search then.',holder='רב נחמן בר יצחק',conditions=['night search time'],scope='Second reason for nighttime search')
edge('b5.home.answer',home,morning,'answer','4a:7');edge('b5.light.answer',light,q6,'answer','4a:7')
study=claim('b5.study','4a:8','אמר אביי הילכך האי צורבא מרבנן לא לפתח בעידניה באורתא דתליסר דנגהי ארבסר','Abaye consequently directs a scholar not to begin the regular study session on the night leading into the fourteenth.',holder='אביי',conditions=['scholar at the night leading into the fourteenth'],scope='Protecting the scheduled search')
delay=claim('b5.delay','4a:8','דלמא משכא ליה שמעתיה ואתי לאימנועי ממצוה','The concern is that study may extend and cause the commandment to be missed.',holder='אביי',mode='hypothetical',conditions=['study continues too long'],scope='Stated rationale for the precaution')
edge('b5.delay.support',delay,study,'support','4a:8');edge('b5.study.qualification',study,home,'qualification','4a:8')
rentq=question('b5.rent.q','4a:9','המשכיר בית לחברו בארבעה עשר על מי לבדוק','When a house is rented on the fourteenth, who must search?',conditions=['lease on the fourteenth'],status='unreviewed_alternatives')
land=claim('b5.land','4a:9','על המשכיר לבדוק דחמירא דידיה הוא','One proposed reason puts the search on the landlord because the leaven is his.',mode='queried',conditions=['lease on the fourteenth'],scope='Anonymous alternative submitted to Rav Nahman bar Yitzhak')
tenant=claim('b5.tenant','4a:9','או דלמא על השוכר לבדוק דאיסורא ברשותיה קאי','The other proposed reason puts it on the tenant because the prohibited item is in his domain.',mode='queried',conditions=['lease on the fourteenth'],scope='Anonymous alternative; not a maintained named position')
mez=claim('b5.mez','4a:9','ת"ש המשכיר בית לחברו על השוכר לעשות לו מזוזה','A quoted rule obligates the tenant to install a mezuzah.',conditions=['rented dwelling'],scope='Proposed analogous evidence')
edge('b5.mez.analogy',mez,tenant,'analogy','4a:9')
resident=claim('b5.resident','4a:10','התם הא אמר רב משרשיא מזוזה חובת הדר היא','Rav Mesharshiya’s statement identifies mezuzah as the resident’s obligation, distinguishing that case.',holder='רב משרשיא',scope='Reported statement about mezuzah; not answerer of the search question')
edge('b5.resident.distinction',resident,mez,'distinction','4a:10','התם הא אמר רב משרשיא מזוזה חובת הדר היא')
question('b5.here.q','4a:10','הכא מאי','What is the rule here for the leaven search?')
before=claim('b5.before','4a:10','אמר להו רב נחמן בר יצחק תנינא המשכיר בית לחברו אם עד שלא מסר לו מפתחות חל ארבעה עשר על המשכיר לבדוק','Rav Nahman bar Yitzhak cites a teaching obligating the landlord if the fourteenth arrives before transfer of the keys.',holder='רב נחמן בר יצחק',conditions=['fourteenth arrives before keys are transferred'],scope='Citation of unnamed teaching, not claimed original authorship')
after=claim('b5.after','4a:10','ואם משמסר לו מפתחות חל ארבעה עשר על השוכר לבדוק','If the fourteenth arrives after keys are transferred, the tenant must search.',holder='רב נחמן בר יצחק',conditions=['fourteenth arrives after keys are transferred'],scope='Continuation of quoted teaching')
edge('b5.before.answer',before,rentq,'answer','4a:10');edge('b5.after.answer',after,rentq,'answer','4a:10');edge('b5.after.distinction',after,before,'distinction','4a:10')
presq=question('b5.pres.q','4a:11','המשכיר בית לחברו בארבעה עשר חזקתו בדוק או אין חזקתו בדוק','Is a house rented on the fourteenth presumed searched?',conditions=['lease on the fourteenth'],status='unreviewed_alternatives')
question('b5.difference.q','4a:11','למאי נ"מ','What practical difference does the presumption make?')
ask=claim('b5.ask','4a:11','לישייליה','The discussion suggests asking the landlord.',mode='hypothetical',scope='Proposed direct information route')
absent=claim('b5.absent','4a:11','דליתיה להאי דלשיוליה','The case is where he is absent and cannot be asked.',conditions=['landlord unavailable'],scope='Question narrowed to missing direct information')
question('b5.burden.q','4a:11','לאטרוחי להאי מאי','Must the tenant be burdened with searching in that case?',conditions=['landlord unavailable'])
edge('b5.absent.qualification',absent,ask,'qualification','4a:11')
trust=claim('b5.trust','4a:12','אמר להו רב נחמן בר יצחק תניתוה הכל נאמנים על ביעור חמץ אפילו נשים אפילו עבדים אפילו קטנים','Rav Nahman bar Yitzhak cites a teaching that everyone is trusted concerning leaven removal, including women, slaves and minors.',holder='רב נחמן בר יצחק',scope='Quoted trust rule; conditional application clarified at4b:5')
whytrust=question('b5.whytrust.q','4a:12','מאי טעמא מהימני','Why are they trusted?')
presinfer=claim('b5.presinfer','4b:1','לאו משום דחזקתו בדוק דקסבר הכל חברים הם אצל בדיקת חמץ','The proposed explanation is a presumption of prior search, treating everyone as reliable in leaven searching.',mode='challenged',scope='Tentative inference, not yet established from this teaching')
chaver=claim('b5.chaver','4b:1','דתניא חבר שמת והניח מגורה מליאה פירות אפי\' הן בני יומן הרי הן בחזקת מתוקנים','A quoted teaching presumes produce left by a deceased haver to be properly prepared even if it is only a day old.',conditions=['deceased haver left a storeroom full of produce'],scope='Analogical example supporting presumed compliance')
edge('b5.chaver.analogy',chaver,presinfer,'analogy','4b:1');edge('b5.presinfer.answer',presinfer,whytrust,'answer','4b:1')
question('b5.howknow.q','4b:2','וממאי','How is that inference established?')
said=claim('b5.said','4b:2','דילמא שאני הכא משום דקאמרי הני','Perhaps this case differs because these persons actually say it was searched.',mode='hypothetical',conditions=['they explicitly report searching'],scope='Alternative explanation of trust teaching')
sq=question('b5.speech.q','4b:2','אטו אמירה דהני מידי מששא אית ביה','Does the statement of these persons have weight?')
edge('b5.said.objection',said,presinfer,'objection','4b:2')
wording=claim('b5.wording','4b:3','אלא מאי דחזקתו בדוק האי הכל נאמנים כל הבתים בחזקת בדוקין בארבעה עשר מיבעי ליה','If a search presumption were the point, the teaching should say all houses are presumed searched, rather than everyone is trusted.',mode='challenged',scope='Objection to deriving the presumption from wording')
edge('b5.wording.objection',wording,presinfer,'objection','4b:3')
negative=claim('b5.negative','4b:4','אלא מאי משום אמירה דהני הא לא אמרי הני לא תפשוט מיניה דאין חזקתו בדוק','If their statement is essential, one might infer there is no presumption when they do not speak.',mode='rejected',conditions=['no such report'],scope='Tentative converse inference denied next')
edge('b5.negative.objection',negative,presinfer,'objection','4b:4')
notproof=claim('b5.notproof','4b:5','לא לעולם אימא לך חזקתו בדוק','The reply says one may still maintain the search presumption.',mode='hypothetical',scope='Compatibility answer; does not prove the general presumption from this source')
known=claim('b5.known','4b:5','והכא במאי עסקינן דמוחזק לן דלא בדק וקאמרי הני בדקיניה','The trust teaching is explained as a house known not to have been searched, where these persons say they searched it.',conditions=['known initially unsearched','explicit report that they performed the search'],scope='Narrowed case of the quoted trust teaching')
weak=claim('b5.weak','4b:5','מהו דתימא לא להימנינהו רבנן','One might have thought the rabbis would not trust them.',mode='rejected',conditions=['known initially unsearched house'],scope='Rejected expectation')
rab=claim('b5.rab','4b:5','קמ"ל כיון דבדיקת חמץ מדרבנן הוא','The answer relies on the search being rabbinic.',scope='Reason for the trust allowance')
nullify=claim('b5.nullify','4b:5','דמדאורייתא בביטול בעלמא סגי ליה','At the Torah level mere nullification suffices.',scope='Stated premise for rabbinic status of the search')
accepted=claim('b5.accepted','4b:5','הימנוהו רבנן בדרבנן','The rabbis trust them for this rabbinic requirement.',conditions=['known initially unsearched house','report by the listed persons that they searched'],scope='Local trust resolution')
edge('b5.notproof.answer',notproof,negative,'answer','4b:5');edge('b5.known.qualification',known,trust,'qualification','4b:5');edge('b5.nullify.support',nullify,rab,'support','4b:5');edge('b5.rab.support',rab,accepted,'support','4b:5');edge('b5.accepted.answer',accepted,sq,'answer','4b:5')
mistake=question('b5.mistake.q','4b:6','המשכיר בית לחבירו בחזקת בדוק ומצאו שאינו בדוק מהו מי הוי כמקח טעות או לא','If a house was rented on the assumption that it was searched but is found unsearched, is this a mistaken transaction?',conditions=['rental on searched-house assumption','house in fact unsearched'],status='unreviewed_alternatives')
body=claim('b5.body','4b:7','תא שמע דאמר אביי לא מיבעיא באתרא דלא יהבי אגרא ובדקו דניחא ליה לאיניש לקיומי מצוה בגופיה','Abaye says that where people do not pay for the search, one is willing to fulfill the commandment personally.',holder='אביי',conditions=['local practice does not pay for searching','rented house unexpectedly unsearched'],scope='Answer against mistaken-transaction claim in this case, not general personal motivation')
money=claim('b5.money','4b:7','אלא אפילו באתרא דיהבי אגרא ובדקו דניחא ליה לאיניש לקיומי מצוה בממוניה','Even where people pay for the search, one is willing to fulfill the commandment with one’s money.',holder='אביי',conditions=['local practice pays for searching','rented house unexpectedly unsearched'],scope='Extension of the same local answer, not a universal psychological model')
edge('b5.body.answer',body,mistake,'answer','4b:7');edge('b5.money.answer',money,mistake,'answer','4b:7');edge('b5.money.qualification',money,body,'qualification','4b:7')
notes5={
'4a:5':'Retained recalled agreement, both named tannaitic premise references and sixth-hour question.',
'4a:6':'Retained hypothetical diligence explanation, morning challenge and circumcision/diligence citations.',
'4a:7':'Separated Rav Nahman bar Yitzhak two reasons: presence at home and candlelight.',
'4a:8':'Retained Abaye precaution and possible study-delay rationale with night condition.',
'4a:9':'Retained two anonymous rental alternatives and proposed mezuzah analogy, not assigned to question recipient.',
'4a:10':'Distinguished Rav Mesharshiya from Rav Nahman bar Yitzhak and retained both key-transfer conditions.',
'4a:11':'Retained presumption question, practical question, asking option and absent-landlord restriction.',
'4a:12':'Retained trust teaching with all three listed groups and explicit why question.',
'4b:1':'Retained tentative presumption explanation and deceased-haver analogy with fresh-produce condition.',
'4b:2':'Retained explicit-report alternative and challenge to report weight.',
'4b:3':'Retained wording objection against proving a house presumption from trusted-person language.',
'4b:4':'Retained tentative negative converse inference, rejected next.',
'4b:5':'Retained compatibility answer without falsely proving general presumption; known-unsearched case, rejected expectation, rabbinic premise, nullification premise and trust resolution.',
'4b:6':'Retained mistaken-transaction question with assumption and discovered-fact conditions.',
'4b:7':'Retained unpaid and paid local practices separately; local Abaye rationale not generalized into enduring preference.'}
coverage=[]
for ref,note in notes5.items():
    sid=refs[ref]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=note+' Source-based '+layer+' pass; '+('records listed.' if ids else 'no further independent object found.')))
p=dict(schema_version=r.VERSION,tractate='Pesachim',owner='L04/pesachim_resume_20261126',epoch=3,source_sha256=meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
out=JOB/'staging'/'search_005.json';r.immutable(out,r.encoded(p));print(out)
