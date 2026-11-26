"""Source reading8b:7–9a:7: marriage restriction and the separate celebrations proof."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r018');c=a.claim;e=a.e
def q(*args,**kwargs):
    v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial'
    a.rows[-1]['uncertainty'].append('Local represented source replies only; not exhaustive alternatives or task eligibility.')
    return v
refs=['8b:'+str(i) for i in range(7,13)]+['9a:'+str(i) for i in range(1,8)]
a.structure('mishnah',['8b:7','8b:8'],'Mishnah marriage, adornment, sewing and bed-cord rules')
a.structure('reasons',['8b:'+str(i) for i in range(9,13)]+['9a:1','9a:2','9a:3'],'Reasons against festival marriage and permission on the festival eve')
a.structure('celebrations',['9a:'+str(i) for i in range(4,8)],'Proof against combining celebrations: rejected construction arguments and textual resolution')
marry=c('marry','8b:7','אין נושאין נשים במועד לא בתולות ולא אלמנות','The Mishnah prohibits marrying virgins or widows during the festival.',conditions=['festival','virgin or widow'],composition='composite')
levirate=c('levirate','8b:7','ולא מייבמין','The Mishnah also prohibits levirate marriage during the festival.',conditions=['festival'])
joy=c('joy','8b:7','מפני ששמחה היא לו','The Mishnah gives the person’s joy as the reason for the restriction.',scope='Stated rationale unpacked in the following discussion')
returnwife=c('return','8b:7','אבל מחזיר הוא את גרושתו','The Mishnah permits taking back one’s divorced wife.',conditions=['remarrying one’s divorced wife'])
e('joy_reason',joy,marry,'support','8b:7')
adorn=c('adorn','8b:8','ועושה אשה תכשיטיה במועד','A woman may undertake adornment during the festival.',conditions=['festival'])
lime=c('lime','8b:8','רבי יהודה אומר לא תסוד מפני שניוול הוא לה','Rabbi Yehuda prohibits applying lime because it disfigures her.',candidates=['רבי יהודה'],role='quoted_authority',conditions=['lime application'],composition='composite',scope='Mishnah position; further conditions appear in later discussion, not covered here')
lay=c('lay','8b:8','ההדיוט תופר כדרכו','An unskilled person may sew normally.')
expert=c('expert','8b:8','והאומן מכליב','A skilled worker uses מכליב stitching.',scope='Technical stitching method preserved without importing later explanation')
beds=c('beds','8b:8','ומסרגין את המטות','The Mishnah permits מסרגין bed cords.',scope='Technical verb retained pending later source explanation')
yose=c('yose','8b:8','רבי יוסי אומר ממתחין','Rabbi Yose permits ממתחין bed cords.',candidates=['רבי יוסי'],role='quoted_authority',scope='Technical contrast retained without premature identification of the methods')
e('lime_qualifies',lime,adorn,'qualification','8b:8');e('yose_distinction',yose,beds,'distinction','8b:8')
why=q('why','8b:9','וכי שמחה היא לו מאי הוי','Why should the joy of marriage prevent it?')
shmuel=c('shmuel','8b:9','אמר רב יהודה אמר שמואל','Rav Yehuda reports Shmuel’s explanation that one celebration is not mixed with another.',candidates=['שמואל'],role='quoted_authority',chain=['רב יהודה','שמואל'],scope='Transmission introduction whose explanation follows later in the same segment')
shquote='לפי שאין מערבין שמחה בשמחה'
for row in a.rows:
    if row['id'].startswith('mk.r018.shmuel.'):row['evidence'].append(a.span('8b:9',shquote))
oshaya=c('oshaya','8b:9','וכן אמר רבי אלעזר אמר רבי אושעיא','Rabbi Elazar similarly reports Rabbi Oshaya’s explanation against mixing celebrations.',candidates=['רבי אושעיא'],role='quoted_authority',chain=['רבי אלעזר','רבי אושעיא'],uncertainty=['The following ואמרי לה supplies an alternative transmission through Rabbi Hanina; not two independent endorsements by Rabbi Elazar.'])
hanina=c('hanina','8b:9','ואמרי לה אמר ר\' אלעזר אמר ר\' חנינא','An alternative version has Rabbi Elazar report Rabbi Hanina for the explanation against mixing celebrations.',candidates=['רבי חנינא'],role='quoted_authority',chain=['רבי אלעזר','רבי חנינא'],uncertainty=['Alternative transmission version retained separately.'])
for row in a.rows:
    if row['id'].startswith(('mk.r018.oshaya.','mk.r018.hanina.')):row['evidence'].append(a.span('8b:9',shquote))
for key,cl in [('shmuel',shmuel),('oshaya',oshaya),('hanina',hanina)]:e(key+'_answer',cl,why,'answer','8b:9')
rabbah=c('rabbah','8b:9','רבה בר [רב] הונא אמר מפני שמניח שמחת הרגל ועוסק בשמחת אשתו','Rabbah bar [Rav] Huna explains that the person leaves festival joy to attend to the joy of his wife.',candidates=['רבה בר [רב] הונא'],uncertainty=['Bracketed רב preserved from this edition; no silent name normalization.'])
identify=c('identify','8b:10','אמר ליה אביי לרב יוסף הא דרבה בר [רב] הונא דרב הוא','Abaye tells Rav Yosef that Rabbah bar [Rav] Huna’s explanation is Rav’s.',candidates=['אביי'],scope='Attribution observation addressed to Rav Yosef, not a dispute between them')
ravq=q('rav_q','8b:10','מנין שאין נושאין נשים במועד','From where is the restriction on festival marriage derived?',candidates=['רב'],role='quoted_authority',chain=['רב דניאל בר קטינא','רב'])
rav=c('rav','8b:10','שנאמר (דברים טז, יד) ושמחת בחגך בחגך ולא באשתך','Rav Daniel bar Katina reports Rav interpreting בחגך as festival joy rather than the joy of one’s wife.',candidates=['רב'],role='quoted_authority',chain=['רב דניאל בר קטינא','רב'])
e('rabbah_answer',rabbah,why,'answer','8b:9');e('rav_answer',rav,ravq,'answer','8b:10');e('rav_identification',rav,identify,'support','8b:10')
ulla=c('ulla','8b:11','עולא אמר מפני הטורח','Ulla explains the restriction by the effort involved.',candidates=['עולא'])
yitz=c('yitz','8b:11','רבי יצחק נפחא אמר מפני ביטול פריה ורביה','Rabbi Yitzhak Nappaha explains it by the neglect of procreation.',candidates=['רבי יצחק נפחא'])
e('ulla_answer',ulla,why,'answer','8b:11');e('yitz_answer',yitz,why,'answer','8b:11')
a.speech('challenge_head','8b:12','מיתיבי כל אלו שאמרו אסורין לישא במועד',composition='composite',act='baraita objection continued on next page',uncertainty=['Incomplete objection continued at9a:1; no invented complete answer in this fragment.'])
eve=c('eve','9a:1','מותרין לישא ערב הרגל','Those prohibited from marrying during the festival may marry on its eve.',conditions=['eve of festival'],scope='Cited baraita beginning at8b:12')
evq=q('eve_q','9a:1','קשיא לכולהו','How can the eve-of-festival permission fit all the proposed reasons?')
for row in a.rows:
    if row['id'].startswith(('mk.r018.eve.','mk.r018.eve_q.')):row['evidence'].append(a.evidence('8b:12'))
joyday=c('joy_day','9a:2','לא קשיא למאן דאמר משום שמחה עיקר שמחה חד יומא הוא','For the joy explanation, the principal wedding joy lasts one day.',conditions=['principal wedding joy on first day'])
effortday=c('effort_day','9a:3','למ"ד משום טירחא עיקר טירחא חד יומא הוא','For the effort explanation, the principal effort lasts one day.',conditions=['principal effort on first day'])
delay=c('delay','9a:3','למ"ד משום ביטול פריה ורביה לחד יומא לא משהי איניש נפשיה','For the procreation explanation, a person would not delay marriage for the advantage of one day.',conditions=['one-day opportunity'])
for key,cl,ref in [('joy',joyday,'9a:2'),('effort',effortday,'9a:3'),('delay',delay,'9a:3')]:e(key+'_eve_answer',cl,evq,'answer',ref)
proofq=q('proof_q','9a:4','ודאין מערבין שמחה בשמחה מנלן','From where is the rule against mixing celebrations derived?')
solomon=c('solomon','9a:4','דכתיב (מלכים א ח, סה) ויעש שלמה בעת ההיא את החג וכל ישראל עמו קהל גדול מלבוא חמת עד נחל מצרים [לפני ה\' אלהינו] שבעת ימים ושבעת ימים ארבעה עשר יום','The discussion cites Solomon’s fourteen days of celebration, seven days and seven days.',scope='Biblical event quoted as evidence; Solomon is not projected as an amoraic position holder')
wait=c('wait','9a:4','ואם איתא דמערבין שמחה בשמחה איבעי ליה למינטר עד החג ומיעבד שבעה להכא ולהכא','The first inference says that if celebrations could be combined, Solomon should have waited for the festival and used the same seven days for both.',mode='challenged',scope='Initial proof route, subjected to objections before a replacement textual proof')
maybe=q('maybe','9a:5','ודלמא מינטר לא נטרינן והיכא דאתרמי עבדינן','Perhaps one may not delay but may combine celebrations when they happen to coincide?')
leave=c('leave','9a:5','איבעי ליה לשיורי פורתא','The reply proposes leaving a small amount of construction unfinished.',mode='challenged',scope='Proposed way to synchronize celebrations, rejected below')
noleave=c('no_leave','9a:6','שיורי בנין בהמ"ק לא משיירינן','The answer rejects leaving Temple construction unfinished.')
crow=c('crow','9a:6','איבעי ליה לשיורי באמה כליא עורב','A further proposal would leave the אמה כליא עורב unfinished.',mode='challenged',uncertainty=['Technical Temple feature retained in source wording.'])
crowneed=c('crow_need','9a:7','אמה כליא עורב צורך בנין הבית הוא','The reply treats the אמה כליא עורב as part of the building’s requirements, rejecting that workaround.')
textq=q('text_q','9a:7','שבעת ימים ושבעת ימים למה לי','Given the stated fourteen days, why separately say seven days and seven days?')
separate=c('separate','9a:7','שמע מינה הני לחוד והני לחוד','The replacement proof infers that the two celebrations must be separate.',scope='Accepted local textual inference from repeated seven-day clauses')
e('solomon_support',solomon,wait,'support','9a:4');e('wait_answer',wait,proofq,'answer','9a:4');e('maybe_challenge',maybe,wait,'objection','9a:5');e('leave_answer',leave,maybe,'answer','9a:5');e('no_leave_objection',noleave,leave,'objection','9a:6');e('crow_response',crow,noleave,'objection','9a:6');e('crowneed_objection',crowneed,crow,'objection','9a:7');e('separate_answer',separate,textq,'answer','9a:7');e('separate_main',separate,proofq,'answer','9a:7');e('separate_replaces',separate,wait,'correction','9a:7')
a.save_window(refs,'resume_moed_katan_festive018.json','Read marriage and separate-celebration arguments with continuation through9b:21. Retain complete Mishnah list, explicit transmission variants, bracketed name, fragment/page continuation, defeated construction-proof routes and replacement textual proof.','3dab930ef06d5ab7f8bb28e101b06a43d5f30e7d082ae1960ba075709cebd305')
