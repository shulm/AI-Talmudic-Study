"""Source reading9a:20–9b:9: farewells, study and enigmatic blessings."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r021');c=a.claim;e=a.e
def q(*args,**kwargs):
    v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial'
    a.rows[-1]['uncertainty'].append('Represented narrative reply or local resolution only, not exhaustive alternatives or task eligibility.')
    return v
refs=['9a:'+str(i) for i in range(20,25)]+['9b:'+str(i) for i in range(1,10)]
a.structure('farewell',['9a:20','9a:21','9a:22'],'Students’ repeated farewell and the two departure-date verses')
a.structure('study',['9a:23','9a:24','9b:1','9b:2','9b:3'],'Seeking a blessing: paired verse discussions on study and other obligations')
a.structure('blessings',['9b:'+str(i) for i in range(4,8)],'Seemingly adverse wishes explained as blessings')
a.structure('shame',['9b:8','9b:9'],'A second farewell and the blessing against shame')
pair=['רבי יונתן בן עסמיי','רבי יהודה בן גרים']
study=c('study','9a:20','ר\' יונתן בן עסמיי ורבי יהודה בן גרים תנו פרשת נדרים בי ר\' שמעון בן יוחי','Rabbi Yonatan ben Asmai and Rabbi Yehuda ben Gerim studied פרשת נדרים with Rabbi Shimon ben Yohai.',scope='Anonymous narrative; source calls the material פרשת נדרים without a forced modern tractate/section identification')
farewell=c('farewell','9a:20','איפטור מיניה באורתא לצפרא הדור וקא מפטרי מיניה','They took leave in the evening and returned to take leave again in the morning.',scope='Narrative sequence')
repeatq=q('repeat_q','9a:20','אמר להו ולאו איפטריתו מיני באורתא','Rabbi Shimon ben Yohai asks whether they had not already taken leave the previous evening.',candidates=['רבי שמעון בן יוחאי'])
rule=c('rule','9a:21','אמרו ליה למדתנו רבינו תלמיד שנפטר מרבו ולן באותה העיר צריך ליפטר ממנו פעם אחרת','They answer that their teacher taught a student who takes leave but stays overnight in the same city must take leave again.',candidates=pair,conditions=['student has taken leave','stays overnight in the same city'],scope='Joint quoted reply recalling their teacher’s instruction')
verses=c('verses','9a:21','שנאמר ביום השמיני שלח את העם ויברכו את המלך וכתיב (דברי הימים ב ז, י) וביום עשרים ושלשה לחדש השביעי שלח את העם','They cite the eighth-day departure and the twenty-third-day departure verses.',candidates=pair,scope='Paired scriptural evidence for the repeated farewell rule',composition='composite')
conclusion=c('conclusion','9a:22','אלא מכאן לתלמיד הנפטר מרבו ולן באותה העיר צריך ליפטר ממנו פעם אחרת','The passage concludes the repeated-farewell obligation for an overnight stay in the same city.',conditions=['student took leave','overnight stay in same city'],scope='Conclusion of the cited argument; no independently named additional speaker')
e('rule_answer',rule,repeatq,'answer','9a:21');e('verses_support',verses,rule,'support','9a:21');e('conclusion_support',verses,conclusion,'support','9a:22')
send=c('send','9a:23','א"ל לבריה בני אדם הללו אנשים של צורה הם זיל גביהון דליברכוך','Rabbi Shimon ben Yohai tells his son that these are distinguished people and sends him to receive their blessing.',candidates=['רבי שמעון בן יוחאי'],naming_refs=['9a:20'],scope='Narrative instruction; the son’s personal name is not supplied here',composition='composite')
arrive=c('arrive','9a:23','אזל אשכחינהו דקא רמו קראי אהדדי','The son finds them contrasting scriptural verses.',scope='Anonymous narrative continuation')
pathq=q('path_q','9a:23','כתיב (משלי ד, כו) פלס מעגל רגלך וכל דרכיך יכונו וכתיב (משלי ה, ו) אורח חיים פן תפלס','How are the instruction to weigh one’s path and the verse אורח חיים פן תפלס reconciled?',candidates=pair,composition='composite')
possible=c('possible','9a:24','לא קשיא כאן במצוה שאפשר לעשותה ע"י אחרים','The reply distinguishes an obligation that can be performed by others.',conditions=['obligation can be performed by others'],scope='First case of the paired reconciliation; source does not label each interlocutor')
impossible=c('impossible','9b:1','כאן במצוה שא"א לעשותה ע"י אחרים','The counterpart is an obligation that cannot be performed by others.',conditions=['obligation cannot be performed by others'],scope='Second case completing the cross-page reconciliation')
e('possible_answer',possible,pathq,'answer','9a:24');e('impossible_answer',impossible,pathq,'answer','9b:1')
studyq=q('study_q','9b:2','כתיב (משלי ג, טו) יקרה היא מפנינים וכל חפציך לא ישוו בה הא חפצי שמים ישוו בה וכתיב (משלי ח, יא) כל חפצים לא ישוו בה דאפילו חפצי שמים לא ישוו בה','How can one verse imply that heavenly concerns compare with Torah while another excludes even heavenly concerns?',candidates=pair,composition='composite',uncertainty=['The text says they again raise the question together; no individual allocation of its parts is imposed.'])
dist=c('study_distinction','9b:3','כאן במצוה שאפשר לעשותה ע"י אחרים כאן במצוה שאי אפשר לעשותה ע"י אחרים','The second reconciliation again distinguishes obligations that others can perform from those others cannot perform.',conditions=['whether the obligation can be performed by others'],composition='composite')
e('study_answer',dist,studyq,'answer','9b:3')
wantq=q('want_q','9b:4','אמרו ליה מאי בעית הכא','The two teachers ask what the son seeks there.',candidates=pair)
request=c('request','9b:4','אמר להו דאמר לי אבא זיל גבייהו דליברכוך','The unnamed son says his father sent him to receive their blessing.',candidates=['unnamed son of Rabbi Shimon ben Yohai'],scope='Narrative speaker identified relationally, not assigned an unprinted personal name')
e('request_answer',request,wantq,'answer','9b:4')
wishes=[('sow','יהא רעוא דתזרע ולא תחצד','May you sow and not reap.'),('bring','תעייל ולא תיפוק','May you bring in and not send out.'),('sendout','תיפוק ולא תעייל','May you send out and not bring in.'),('house','ליחרוב ביתך וליתוב אושפיזך','May your house be ruined and your lodging inhabited.'),('table','לבלבל פתורך','May your table be confused.'),('year','ולא תחזי שתא חדתא','May you not see a new year.')]
for key,quote,text in wishes:
    c(key,'9b:4',quote,text,candidates=pair,mode='hypothetical',scope='Quoted enigmatic blessing, not a predicted harmful event; meanings explained by the father below')
complaint=c('complaint','9b:5','א"ל לא מבעיא דברוכי לא בירכן אבל צעורי צעורן','The son tells his father that they failed to bless him and instead distressed him.',candidates=['unnamed son of Rabbi Shimon ben Yohai'],scope='Character’s initial interpretation, corrected by his father',mode='challenged')
whatq=q('what_q','9b:5','א"ל מאי אמרו לך','His father asks what they said.',candidates=['רבי שמעון בן יוחאי'],naming_refs=['9a:20','9a:23'])
report=c('report','9b:5','הכי והכי אמרו לי','The son reports their words.',candidates=['unnamed son of Rabbi Shimon ben Yohai'],scope='Deictic narrative report; preceding quoted wishes supply the content, not a new verbatim repetition')
bless=c('bless','9b:5','א"ל הנך כולהו ברכתא נינהו','The father explains that all the statements are blessings.',candidates=['רבי שמעון בן יוחאי'],naming_refs=['9a:20','9a:23'])
e('report_answer',report,whatq,'answer','9b:5');e('bless_corrects',bless,complaint,'correction','9b:5')
interpretations=[
('sons','9b:5','תזרע ולא תחצד תוליד בנים ולא ימותו','Sowing without reaping means having children who do not die.'),
('daughtersinlaw','9b:5','תעייל ולא תיפוק תעייל כלתא ולא לימותו בנך דליפקון','Bringing in without sending out means bringing daughters-in-law whose husbands, one’s sons, do not die and cause them to leave.'),
('daughters','9b:5','תיפוק ולא תעייל תוליד בנתא ולא ימותו גוברייהו וליהדרו לותיך','Sending out without bringing in means marrying off daughters whose husbands do not die and cause them to return.'),
('worlds','9b:6','ליחרוב ביתך וליתוב אושפיזך דהאי עלמא אושפיזך וההיא עלמא ביתא','The house/lodging wish means that this world is temporary lodging and the other world is one’s permanent house.'),
('children','9b:7','לבלבל פתורך בבני ובנתא','A confused table means a table full of sons and daughters.'),
('wife','9b:7','ולא תיחזי שתא חדתא דלא תמות אנתך ולא תנסב אינתתא אחריתי','No new year means that one’s wife does not die and one does not marry another wife.')]
for key,ref,quote,text in interpretations:
    cl=c(key,ref,quote,text,candidates=['רבי שמעון בן יוחאי'],naming_refs=['9a:20','9a:23'],scope='Father’s positive interpretation of the quoted wishes; not a separate practical ruling',composition='composite' if key in ['daughtersinlaw','daughters','worlds','wife'] else 'atomic')
    e(key+'_supports',cl,bless,'support',ref)
graveverse=c('graveverse','9b:6','דכתיב (תהלים מט, יב) קרבם בתימו לעולם אל תקרי קרבם אלא קברם','The father adduces an interpretation reading קברם in place of קרבם to explain the permanent-house metaphor.',candidates=['רבי שמעון בן יוחאי'],naming_refs=['9a:23'],scope='Scriptural wordplay within the blessing interpretation')
e('graveverse_support',graveverse,'mk.r021.worlds.c','support','9b:6')
second=c('second','9b:8','ר\' שמעון בן חלפתא אפטר מיניה דרב','The source reports Rabbi Shimon ben Halafta taking leave of Rav.',scope='Separate narrative, retained with its printed names',uncertainty=['No chronological or textual harmonization of the printed narrative is imposed.'])
father=c('father','9b:8','א"ל (אבוה) זיל לגביה דליברכך','An instruction, attributed parenthetically to his father, sends him for a blessing.',candidates=['unnamed father (parenthetical attribution)'],uncertainty=['Source prints (אבוה); personal identity is not supplied or emended.'])
shame=c('shame','9b:8','א"ל יהא רעוא דלא תבייש ולא תתבייש','The blessing wishes that he neither shame others nor be ashamed.',candidates=['רב'],naming_refs=['9b:8'],mode='hypothetical',scope='Blessing in the separate farewell narrative, not a guarantee of future events')
fatherq=q('father_q','9b:8','א"ל מאי אמר לך','The father asks what he was told.',candidates=['unnamed father (parenthetical attribution)'])
little=c('little','9b:8','א"ל מילין בעלמא הוא דאמר לי','The recipient dismisses the blessing as mere words.',candidates=['רבי שמעון בן חלפתא'],mode='challenged',scope='Recipient’s reaction, corrected by the father')
great=c('great','9b:9','א"ל ברכך ברכתא דברכן קודשא בריך הוא לישראל ותנא בה','The father says he received a blessing that God blessed Israel with and repeated.',candidates=['unnamed father (parenthetical attribution)'],scope='Narrative interpretation, not identification of the father as a named amora')
verses2=c('verses2','9b:9','דכתיב (יואל ב, כו) ואכלתם אכול ושבוע והללתם וגו\' ולא יבושו עמי לעולם וידעתם כי בקרב ישראל אני וגו\' ולא יבושו עמי לעולם','The father cites two occurrences of ולא יבושו עמי לעולם in Joel.',candidates=['unnamed father (parenthetical attribution)'],scope='Repeated biblical blessing used as evidence',composition='composite')
e('little_answer',little,fatherq,'answer','9b:8');e('great_corrects',great,little,'correction','9b:9');e('verses2_support',verses2,great,'support','9b:9')
a.save_window(refs,'resume_moed_katan_blessings021.json','Read complete farewell and blessing narratives through9b:9 with subsequentadornment context. Preserve unnamed son/father, sourceparenthesis and printednames, wholepairedverse reconciliations, six wishes and six interpretations, initialcomplaints and corrections; do not flatten narratives into rulings.','4f5caa36135fbe2a30f310834fd12c38e53595bb2fabbfcdd84d18c526eea5c1')
