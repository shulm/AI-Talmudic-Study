"""Manual rejected release openings, alternate Abaye/Rava reports, and anger narratives."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r022.';a.OUTPUT='continuation_022.json'
c=a.c;q=a.q;e=a.edge
a.structure('openings',['22a:'+str(i) for i in range(2,9)],'Severe anti-vow teachings not used as release openings; alternative reports and local ruling')
a.structure('anger',['22a:'+str(i) for i in range(9,13)]+['22b:1','22b:2','22b:3'],'Anger teachings, Ulla’s dangerous encounter, and a scriptural counterfactual')
grandson=c('grandson','22a:2','בר ברתיה דרבי ינאי סבא אתא לקמיה דרבי ינאי סבא','Rabbi Yannai the elder’s daughter’s son came before him.',scope='Narrative family relation, no unprinted personal name')
book=q('book','22a:2','אמר ליה אילו הוה ידעת דפתחין פינקסך וממשמשין בעובדך מי נדרת','Rabbi Yannai asks whether he would have vowed knowing his record would be opened and his deeds examined.',voice='רבי ינאי סבא')
release=c('release','22a:2','אמר ליה לא ושרייה','He says no and is released.',scope='Narrative outcome, not approval of this opening for subsequent practice')
sourceq=q('sourceq','22a:3','אמר רבי אבא מאי קראה','Rabbi Abba asks for the scriptural support.',voice='רבי אבא')
verse=c('verse','22a:3','ואחר נדרים לבקר','The cited phrase is ואחר נדרים לבקר.',scope='Scriptural basis offered for the narrative opening')
notuse=c('notuse','22a:3','ואף על גב דפתח רבי ינאי ליה אנן לא פתחינן ליה בהא','Despite Rabbi Yannai’s use, the discussion rejects using that opening.',scope='Explicit practice limitation, narrative precedent not treated as operative general permission')
e('release.answer',release,book,'answer','22a:2');e('verse.answer',verse,sourceq,'answer','22a:3');e('notuse.qualification',notuse,release,'qualification','22a:3')
sword=c('sword','22a:4','דאמר רבה בר בר חנה אמר רבי יוחנן מאי פתח ליה רבן גמליאל לההוא סבא יש בוטה כמדקרות חרב ולשון חכמים מרפא כל הבוטה ראוי לדוקרו בחרב; אלא לשון חכמים מרפא.','Rabbah bar bar Hana reports Rabbi Yohanan’s account of Rabban Gamliel using the sword/wise-tongue verse as an opening, portraying vowing as deserving a sword and sages’ speech as healing.',holder='רבי יוחנן',composition='composite',scope='Reported severe rhetorical comparison, not an endorsement of violence')
a.add('yohanan.chain','attributions',dict(surface='רבה בר בר חנה אמר רבי יוחנן',role='transmitter',candidates=['רבה בר בר חנה'],scope=sword,transmission_chain=['רבה בר בר חנה','רבי יוחנן']),[a.ev('22a:4','רבה בר בר חנה אמר רבי יוחנן')],[sword])
notuse2=c('notuse2','22a:4','ולא פתחינן בהדא אחרנייתא','This severe opening likewise is not used.',scope='Explicit present-practice limitation on narrated precedent')
e('notuse2.qualification',notuse2,sword,'qualification','22a:4')
altar=c('altar','22a:5','דתניא רבי נתן אומר הנודר כאילו בנה במה','Rabbi Natan compares one who vows to building a private altar.',holder='רבי נתן',scope='First half of ethical analogy')
offer=c('offer','22a:5','והמקיימו כאילו מקריב עליו קרבן','He compares fulfilling the vow to offering on that altar.',holder='רבי נתן',scope='Second half of ethical analogy')
first=c('first','22a:5','ברישא פתחינן','In the first report, the first half may be used as a release opening.',mode='rejected',scope='First-version common ground, superseded by final ruling below')
abaye=c('abaye','22a:5','בסיפא אביי אמר פתחינן','In that report Abaye permits using the latter half too.',holder='אביי',mode='rejected',scope='First version locates disagreement in latter half')
rava=c('rava','22a:5','רבא אמר לא פתחינן','Rava forbids the latter-half opening in that version.',holder='רבא',scope='First report of disagreement')
kahana=c('kahana','22a:6','רב כהנא מתני לה להא שמעתא בהדין לישנא...','The source introduces Rav Kahana’s transmission with an ellipsis after בהדין לישנא.',scope='Printed incomplete reporting formula; missing words not restored',uncertainty=['The pinned source prints an ellipsis; no absent alternate text reconstructed.'])
last=c('last','22a:6','רב טביומי מתני הכי בסיפא לא פתחינן','Rav Tavyomi’s version makes nonuse of the latter half common ground.',scope='Explicit alternative report')
abaye2=c('abaye2','22a:6','ברישא אביי אמר פתחינן','In this version Abaye permits the first-half opening.',holder='אביי',mode='rejected',scope='Alternative version moves dispute to first half')
rava2=c('rava2','22a:6','רבא אמר לא פתחינן','Rava rejects the first-half opening in this version.',holder='רבא',scope='Alternative report, not silently fused with first')
final=c('final','22a:6','והלכתא לא פתחינן לא ברישא ולא בסיפא','The text’s local ruling permits neither half as an opening.',scope='Explicit והלכתא, distinct from reported disagreement')
e('final.correction',final,first,'correction','22a:6');e('final.correction2',final,abaye,'correction','22a:6');e('final.correction3',final,abaye2,'correction','22a:6')
wicked=c('wicked','22a:7','דשמואל דאמר שמואל אף על פי שמקיימו נקרא רשע','Shmuel calls the vower wicked even if he fulfills the vow.',holder='שמואל',scope='Attributed ethical characterization, not an annotation of a modern person')
notuse3=c('notuse3','22a:7','ולא פתחינן בהא נמי','This statement also is not used as an opening.',scope='Explicit limitation on use of Shmuel teaching')
abahuq=q('abahuq','22a:7','אמר רבי אבהו מאי קרא','Rabbi Abahu asks which verse supports it.',voice='רבי אבהו')
abahu=c('abahu','22a:7','וכי תחדל לנדור לא יהיה בך חטא ויליף חדלה חדלה כתיב הכא כי תחדל לנדור וכתיב התם שם רשעים חדלו רוגז','He compares the shared cessation language in the vow verse and שם רשעים חדלו רוגז.',holder='רבי אבהו',composition='composite',scope='Explicit verbal scriptural analogy')
yosef=c('yosef','22a:8',None,'Rav Yosef also cites the Mishnah contrasting ineffective vows of the righteous with effective vows of the wicked in naziriteship, offerings and oaths.',holder='רב יוסף',composition='composite',scope='Repeated Mishnah proof, all three categories retained')
e('notuse3.qualification',notuse3,wicked,'qualification','22a:7');e('abahu.answer',abahu,abahuq,'answer','22a:7');e('abahu.support',abahu,wicked,'support','22a:7');e('yosef.support',yosef,wicked,'support','22a:8')
anger=c('anger','22a:9','אמר רבי שמואל בר נחמני אמר רבי יונתן כל הכועס כל מיני גיהנם שולטין בו','Rabbi Yonatan, reported by Rabbi Shmuel bar Nahmani, associates anger with all kinds of Gehinnom.',holder='רבי יונתן',scope='Attributed religious/moral teaching')
a.add('yonatan.chain','attributions',dict(surface='אמר רבי שמואל בר נחמני אמר רבי יונתן',role='transmitter',candidates=['רבי שמואל בר נחמני'],scope=anger,transmission_chain=['רבי שמואל בר נחמני','רבי יונתן']),[a.ev('22a:9','אמר רבי שמואל בר נחמני אמר רבי יונתן')],[anger])
evil=c('evil','22a:9',"שנאמר והסר כעס מלבך והעבר רעה מבשרך ואין רעה אלא גיהנם שנאמר כל פעל ה' למענהו וגם רשע ליום רעה",'The exposition links anger and רעה, then identifies רעה with Gehinnom through another verse.',composition='composite',scope='Source’s two-verse interpretive proof')
illness=c('illness','22a:10',"ולא עוד אלא שהתחתוניות שולטות בו שנאמר ונתן ה' לך שם לב רגז וכליון עינים ודאבון נפש",'The teaching also associates anger with תחתוניות and cites the agitated-heart verse.',scope='Attributed ancient illness association, not medical causation established by annotation')
illq=q('illq','22a:10','איזהו דבר שמכלה את העינים ומדאיב את הנפש','What consumes the eyes and pains the soul?')
answer=c('answer','22a:10','הוי אומר אלו התחתוניות','The exposition answers תחתוניות.',scope='Source term retained, not an added clinical diagnosis')
e('evil.support',evil,anger,'support','22a:9');e('answer.answer',answer,illq,'answer','22a:10')
trip=c('trip','22a:11','עולא במיסקיה לארעא דישראל איתלוו ליה תרין בני חוזאי בהדיה','Ulla traveled toward the land of Israel accompanied by two men of Hozae.',scope='Narrative travel setting')
killing=c('killing','22a:11','קם חד שחטיה לחבריה','One killed his companion.',scope='Narrated violent event, not a legal permission')
killerq=q('killerq','22a:11','אמר ליה לעולא יאות עבדי','The killer asks Ulla whether he acted properly.')
ulla=c('ulla','22a:11','אמר ליה אין ופרע ליה בית השחיטה','Ulla gives an affirmative reply and the printed further instruction concerning the wound.',scope='Speech in a dangerous encounter; subsequent explanation is self-preservation, not endorsement of homicide')
concern=q('concern','22a:11','כי אתא לקמיה דרבי יוחנן אמר ליה דילמא חס ושלום אחזיקי ידי עוברי עבירה','On reaching Rabbi Yohanan, Ulla asks whether he may have strengthened a wrongdoer.',voice='עולא')
saved=c('saved','22a:11','אמר ליה נפשך הצלת','Rabbi Yohanan tells Ulla that he saved his own life.',holder='רבי יוחנן',scope='Source-explicit evaluation of Ulla’s response in danger')
e('ulla.answer',ulla,killerq,'answer','22a:11');e('saved.answer',saved,concern,'answer','22a:11');e('saved.qualification',saved,ulla,'qualification','22a:11')
placeq=q('placeq','22a:12',"קא תמה רבי יוחנן מכדי כתיב ונתן ה' לך שם לב רגז בבבל כתיב",'Rabbi Yohanan wonders how this happened, since the agitated-heart verse concerns Babylonia.',voice='רבי יוחנן')
jordan=c('jordan','22a:12','אמר ליה ההוא שעתא','Ulla replies that at that time they had not yet crossed the Jordan.',holder='עולא',extra=[('22b:1',None)],scope='Cross-page temporal/geographic clarification')
e('jordan.answer',jordan,placeq,'answer','22b:1')
presence=c('presence','22b:2','אמר רבה בר רב הונא כל הכועס אפילו שכינה אינה חשובה כנגדו שנאמר רשע כגובה אפו בל ידרוש אין אלהים כל מזמותיו','Rabbah bar Rav Huna says anger makes even the divine presence unimportant to a person, citing the proud-anger verse.',holder='רבה בר רב הונא',scope='Attributed moral judgment and proof',composition='composite')
forget=c('forget','22b:2','רבי ירמיה מדיפתי אמר משכח תלמודו ומוסיף טיפשות שנאמר כי כעס בחיק כסילים ינוח וכתיב וכסיל יפרוש אולת','Rabbi Yirmeya of Difti associates anger with forgetting learning and increasing foolishness, citing two verses.',holder='רבי ירמיה מדיפתי',composition='composite',scope='Attributed moral consequences and scriptural proofs, not measured cognition')
sins=c('sins','22b:2','רב נחמן בר יצחק אמר בידוע שעוונותיו מרובין מזכיותיו שנאמר ובעל חימה רב פשע','Rav Nahman bar Yitzhak says anger indicates more sins than merits, citing בעל חימה רב פשע.',holder='רב נחמן בר יצחק',scope='Attributed religious evaluation')
books=c('books','22b:3','אמר רב אדא ברבי חנינא אלמלא (לא) חטאו ישראל לא ניתן להם אלא חמישה חומשי תורה וספר יהושע בלבד','Rav Adda ben Rabbi Hanina gives the counterfactual that without Israel’s sin they would have received only the five books of Torah and Joshua.',holder='רב אדא ברבי חנינא',mode='hypothetical',scope='Counterfactual teaching; parenthesized לא retained, not an actual alternate canon claim',composition='composite')
land=c('land','22b:3','[מפני] שערכה של ארץ ישראל הוא','Joshua is included because it gives the arrangement of the land of Israel.',scope='Explicit rationale with source bracket retained')
reasonq=q('reasonq','22b:3','מאי טעמא','What is the reason for the larger scriptural corpus in the teaching?')
wisdom=c('wisdom','22b:3','כי ברוב חכמה רב כעס','The explanation cites כי ברוב חכמה רב כעס.',scope='Source’s proof phrase, no external historical canon explanation')
e('wisdom.answer',wisdom,reasonq,'answer','22b:3');e('land.qualification',land,books,'qualification','22b:3')
a.notes={
'22a:2':'Reread Yannai/grandson relation, deeds-examination counterfactual, reply and release.',
'22a:3':'Reread Rabbi Abba verse question and explicit refusal to generalize Yannai precedent.',
'22a:4':'Reread Rabbah bar bar Hana/Yohanan/Gamliel narrative transmission and nonuse of severe sword opening.',
'22a:5':'Reread both Rabbi Natan analogies and first-version placement of Abaye/Rava disagreement.',
'22a:6':'Reread printed Rav Kahana ellipsis, Rav Tavyomi alternative placement and explicit final neither-half ruling.',
'22a:7':'Reread Shmuel ethical label, nonuse as opening and Rabbi Abahu verbal proof.',
'22a:8':'Reread Rav Yosef repeated Mishnah support with all three vow categories.',
'22a:9':'Reread Yonatan transmission and two-verse Gehinnom argument.',
'22a:10':'Reread ancient illness assertion, verse, explicit question and answer without modern diagnosis.',
'22a:11':'Reread full Ulla encounter, both dialogues and self-preservation explanation; affirmative response not generalized into endorsement.',
'22a:12':'Reread geography question and unfinished reply completed22b:1.',
'22b:1':'Reread pre-Jordan clarification, cross-page evidence bound to reply.',
'22b:2':'Reread three named anger teachings and distinct cited proofs.',
'22b:3':'Reread counterfactual canon claim, Joshua-land rationale and wisdom/anger proof, with editorial brackets preserved.'}
if __name__=='__main__':a.save()
