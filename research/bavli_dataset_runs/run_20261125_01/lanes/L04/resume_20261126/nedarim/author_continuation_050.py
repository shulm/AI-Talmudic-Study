"""Manual reading of dietary and poverty narratives; unassigned speakers retained."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r050.';a.OUTPUT='continuation_050.json'
c=a.c;e=a.edge;q=b.q
a.structure('narratives',['49b:'+str(i) for i in range(3,14)]+['50a:1'],'Food practices, Rabbi Yehuda’s explanations and shared garment narrative')
prayerq=q('prayerq','49b:1','כמאן מצלינן על קצירי ועל מריעי','According to whom do we pray for קצירי and מריעי?',voice='רבא')
e('prayer.answer','nd.r049.prayer.c',prayerq,'answer','49b:1')
porridgeq=a.q('porridgeq','49b:3',None,'Rav Hisda asks the precise eaters of Huzal whether wheat porridge should accompany wheat bread and barley barley, or whether they should be crossed.',voice='רב חסדא')
for row in a.records:
    if row['id']==porridgeq:row['uncertainty'].append('No explicit answer choosing these pairings appears in the read continuation; subsequent anecdotes concern other eating practices.')
rava=c('rava','49b:4','רבא אכליה בחסיסי','Rava ate the porridge with חסיסי.',holder='רבא',scope='Narrated practice; named accompaniment retained without conjectural identification')
huna=c('huna','49b:4',"רבה בר רב הונא אשכחי' לרב הונא דקאכיל דייסא באצבעתיה",'Rabbah bar Rav Huna found Rav Huna eating porridge with his finger.',composition='composite',scope='Distinct son and father in reported encounter')
fingerq=q('fingerq','49b:4','אמאי קאכיל מר בידיה','Why is Rav Huna eating with his hand?',voice='רבה בר רב הונא')
rav=c('rav','49b:4','הכי אמר רב דייסא באצבעתא בסים וכל דכן בתרתין וכל דכן בתלת','Rav Huna reports Rav’s saying that porridge tastes good with one finger, better with two, and better with three.',holder='רב',composition='composite',scope='Explicit Rav saying transmitted by Rav Huna; three comparative steps')
e('rav.answer',rav,fingerq,'answer','49b:4')
travel=c('travel','49b:5','אמר ליה רב לחייא בריה וכן אמר ליה רב הונא לרבה בריה מזמנים לך למיכל דייסא עד פרסה למיכל בישרא דתורא עד תלתא פרסין','Rav tells his son Hiyya, and Rav Huna likewise tells his son Rabbah, to travel up to one parasang for porridge and three for ox meat.',composition='composite',scope='Two expressly parallel father-son transmissions and two distances; no dispute inferred')
spit=c('spit','49b:5','אמר ליה רב לחייא בריה וכן א"ל רב הונא לרבה בריה כל מידעם לא תפלוט קמיה רבך לבר מן קרא ודייסא שהן דומין לפתילתא של אבר ואפילו קמי שבור מלכא פלוט','Both father-son transmissions also prohibit spitting food before one’s teacher except hot gourd and porridge, likened to molten lead; these may be spat out even before King Shapur.',composition='composite',scope='Expressly repeated dual transmission; attributed etiquette and exception, not modern clinical advice')
pair=c('pair','49b:6','רבי יוסי ורבי יהודה חד אכיל דייסא באצבעתיה וחד אכיל בהוצא','Of Rabbi Yosei and Rabbi Yehuda, one ate porridge with his finger and the other with a stick.',composition='composite',scope='חד/חד actors remain unassigned; name order does not identify their practices',uncertainty=('The continuation identifies each speaker by eating method, not personal name.',))
stick=c('stick','49b:6','א"ל דאכיל בהוצא לדאכיל באצבעתיה עד מתי אתה מאכילני צואתך','The stick eater complains that the finger eater feeds him filth.',scope='Rhetorical complaint attributed only by eating method; Yosei/Yehuda name assignment unresolved')
finger=c('finger','49b:6','אמר ליה דאכיל באצבעתיה לדאכיל בהוצא עד מתי אתה מאכילני רוקך','The finger eater counters that the stick eater feeds him saliva.',scope='Rhetorical countercomplaint attributed only by eating method')
e('finger.objection',finger,stick,'objection','49b:6')
serve=c('serve','49b:7','רבי יהודה ורבי שמעון אייתו לקמייהו בלוספיין רבי יהודה אכל ר\' שמעון לא אכל','When בלוספיין were served, Rabbi Yehuda ate and Rabbi Shimon did not.',composition='composite',scope='Explicitly named differing practices; food label retained')
why=q('why','49b:7','א"ל רבי יהודה מאי טעמא לא אכיל מר','Why does Rabbi Shimon not eat?',voice='רבי יהודה')
shimon=c('shimon','49b:7','אמר ליה ר\' שמעון אלו אין יוצאין מבני מעים כל עיקר','Rabbi Shimon says these foods do not leave the intestines at all.',holder="ר' שמעון",scope='Attributed explanation of refusal, not endorsed physiology')
yehuda=c('yehuda','49b:7','אמר ליה רבי יהודה כ"ש שנסמוך עליהן למחר','Rabbi Yehuda replies that all the more they can rely on them tomorrow.',holder='רבי יהודה',scope='Counterevaluation of the same alleged persistence')
e('shimon.answer',shimon,why,'answer','49b:7');e('yehuda.objection',yehuda,shimon,'objection','49b:7')
tarfon=c('tarfon','49b:8','אמר ליה רבי טרפון היום פניך צהובין','Rabbi Tarfon observes that Rabbi Yehuda’s face is bright today.',holder='רבי טרפון',scope='Reported observation during their encounter')
beets=c('beets','49b:8','אמר ליה אמש יצאו עבדיך לשדה והביאו לנו תרדין ואכלנום בלא מלח ואם אכלנום במלח כל שכן שהיו פנינו צהובין','Rabbi Yehuda attributes his appearance to eating field-gathered beets without salt, adding that salt would have increased the effect.',holder='רבי יהודה',composition='composite',scope='Narrative explanation and hypothetical comparison, not nutritional advice')
e('beets.answer',beets,tarfon,'answer','49b:8')
wineacc=c('wineacc','49b:9','אמרה ההיא מטרוניתא לרבי יהודה מורה ורוי','A matron accuses Rabbi Yehuda of being both a teacher and a drunkard.',scope='Anonymous matron’s accusation, subsequently denied')
wine=c('wine','49b:9','אמר לה הימנותא בידא דההיא איתתא אי טעימנא אלא קידושא ואבדלתא וארבעה כסי דפסחא','Rabbi Yehuda insists he tastes wine only for kiddush, havdala and the four Passover cups.',holder='רבי יהודה',composition='composite',scope='Personal denial with three ritual exceptions')
ache=c('ache','49b:9','וחוגרני צידעי מן הפסח עד העצרת','He reports binding his temples from Passover until Shavuot.',holder='רבי יהודה',scope='Personal aftermath of the wine, not a general medical rule')
wisdom=c('wisdom','49b:9','אלא (קהלת ח, א) חכמת אדם תאיר פניו','He instead cites wisdom illuminating a person’s face.',holder='רבי יהודה',scope='Scriptural explanation of appearance in response to accusation')
e('wine.objection',wine,wineacc,'objection','49b:9');e('wisdom.answer',wisdom,wineacc,'answer','49b:9')
sad=c('sad','49b:10','אמר לי\' ההוא צדוקי לרבי יהודה פניך דומין אי כמלוי רבית אי כמגדלי חזירין','A Sadducee compares Rabbi Yehuda’s appearance to that of moneylenders or pig breeders.',composition='composite',scope='Anonymous interlocutor’s two proposed comparisons, not facts about Yehuda')
forbid=c('forbid','49b:10','א"ל ביהודאי תרוייהו אסירן','Rabbi Yehuda replies that both practices are forbidden to Jews.',holder='רבי יהודה',scope='Narrative reply to the two proposed occupations')
privy=c('privy','49b:10','אלא עשרים וארבעה בית הכסא אית לי מן ביתא עד בי מדרשא וכל שעה ושעה אני נכנס לכל אחד ואחד','Rabbi Yehuda instead describes twenty-four privies between his home and study hall and his frequent use of them.',holder='רבי יהודה',composition='composite',scope='Personal explanation in narrative, not medical recommendation')
e('forbid.objection',forbid,sad,'objection','49b:10');e('privy.answer',privy,sad,'answer','49b:10')
laborY=c('laborY','49b:11','ר\' יהודה כד אזיל לבי מדרשא שקיל גולפא על כתפיה אמר גדולה מלאכה שמכבדת את בעליה','Rabbi Yehuda carries a pot on his shoulder to the study hall and says labor is great because it honors its practitioner.',holder="ר' יהודה",composition='composite',scope='First narrated practice and maxim occurrence')
laborS=c('laborS','49b:11','רבי שמעון שקיל צנא על כתפיה אמר גדולה מלאכה שמכבדת את בעליה','Rabbi Shimon carries a basket on his shoulder and repeats the maxim that labor honors its practitioner.',holder='רבי שמעון',composition='composite',scope='Second parallel occurrence retained, not a new unique maxim or dispute')
cloak=c('cloak','49b:12','דביתהו דרבי יהודה נפקת נקטת עמרא עבדה גלימא דהוטבי כד נפקת לשוקא מיכסיא ביה וכד נפיק רבי יהודה לצלויי הוה מיכסי ומצלי','Rabbi Yehuda’s wife makes a wool garment which she wears to market and he wears for prayer.',composition='composite',scope='Shared garment narrative and two separate uses')
bless=c('bless','49b:12','וכד מיכסי ביה הוה מברך ברוך שעטני מעיל','When wearing it he blesses: ברוך שעטני מעיל.',holder='רבי יהודה',scope='Narrative blessing quotation, not an inferred universal liturgical obligation')
fast=c('fast','49b:13','זימנא חדא גזר רבן שמעון בן גמליאל תעניתא ר\' יהודה לא אתא לבי תעניתא אמרין ליה לא אית ליה כסויא','When Rabban Shimon ben Gamliel declares a fast, Rabbi Yehuda is absent and people explain that he lacks a covering.',composition='composite',scope='Declared fast, absence and reported explanation')
reject=c('reject','49b:13','שדר ליה גלימא ולא קביל','A cloak is sent to Rabbi Yehuda, but he does not accept it.',scope='Continuation of fast-day narrative; sender understood from immediately preceding Rabban Shimon ben Gamliel')
mat=c('mat','50a:1','דלי ציפתא ואמר ליה לשלוחא חזי מאי איכא','He lifts a mat and tells the messenger to see what is there.',scope='Source does not name the displayed object in this segment; none supplied')
world=c('world','50a:1','מיהו לא ניחא לי דאיתהני בהדין עלמא','Rabbi Yehuda says he does not wish to benefit in this world.',holder='רבי יהודה',scope='Cross-folio narrative continuation and personal explanation of refusal')
e('world.answer',world,reject,'answer','50a:1')
a.notes={
'49b:3':'Reread Hisda exact same-grain/cross-grain alternatives; no explicit selection in continuation.',
'49b:4':'Reread Rava practice, Rabbah bar Rav Huna question, Huna transmission of Rav and all three finger comparisons.',
'49b:5':'Reread both explicitly duplicated father-son transmissions, travel distances and heat-related etiquette exception.',
'49b:6':'Reread Yosei/Yehuda unassigned one/other methods and reciprocal rhetorical complaints; no named assignment invented.',
'49b:7':'Reread named practices, Yehuda question, Shimon stated reason and Yehuda counterevaluation.',
'49b:8':'Reread Tarfon observation, beet narrative and salt counterfactual as attributed reports.',
'49b:9':'Reread matron accusation, three ritual wine exceptions, temple-binding aftermath and wisdom verse.',
'49b:10':'Reread Sadducee two comparisons, Yehuda prohibition reply and twenty-four privies explanation.',
'49b:11':'Reread separate Yehuda pot and Shimon basket occurrences with identical labor maxim.',
'49b:12':'Reread wife-made shared garment, market/prayer uses and exact blessing.',
'49b:13':'Reread fast declaration, absence explanation and refused cloak; continued into50a1.',
'50a:1':'Reread mat display and personal worldly-benefit refusal; unspecified displayed contents not invented.'}
if __name__=='__main__':a.save()
