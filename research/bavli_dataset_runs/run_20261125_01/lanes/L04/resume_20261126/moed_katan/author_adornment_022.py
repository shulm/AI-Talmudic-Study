"""Direct source reading9b:10–21 with sewing/bed continuation read through10b."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r022');c=a.claim;e=a.e
refs=['9b:'+str(i) for i in range(10,22)]
def q(*args,**kwargs):
    v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial'
    a.rows[-1]['uncertainty'].append('Only represented source-supported replies; no exhaustive inventory or downstream eligibility.')
    return v
a.structure('adornment',refs[:8],'Adornment, age, temporary discomfort and later happiness')
a.structure('cosmetics',refs[8:],'Reported cosmetics, explanations and contrasting family narratives')
base=c('cosmetics','9b:10','כוחלת ופוקסת ומעבירה (סרק) על פניה','The baraita lists eye coloring, פוקסת, and applying the parenthetically printed cosmetic to the face.',composition='composite',scope='Festival adornment baraita; פוקסת retained without selecting a disputed technical gloss')
alt=c('distinction','9b:10','ואיכא דאמרי מעברת סרק על פניה של מטה','An alternative version describes application to the lower face.',scope='Alternative textual report, euphemism retained')
e('alt_version',alt,base,'distinction','9b:10')
narr=c('wife','9b:11','דביתהו דרב חסדא מקשטא באנפי כלתה','Rav Hisda’s wife adorned herself in the presence of her daughter-in-law.',scope='Narrative circumstance')
young=c('young','9b:11','יתיב רב הונא בר חיננא קמיה דרב חסדא ויתיב וקאמר לא שנו אלא ילדה אבל זקנה לא','Rav Huna bar Hinnana, sitting before Rav Hisda, restricts the permission to a young woman and excludes an old woman.',candidates=['רב הונא בר חיננא'],conditions=['young woman versus old woman'],mode='challenged',composition='composite')
old=c('old','9b:12','א"ל האלהים אפילו אמך ואפילו אימא דאימך ואפילו עומדת על קברה','The reply insists that even his mother, grandmother, or one standing at the grave is included.',candidates=['רב חסדא'],naming_refs=['9b:11'],scope='Contextual identification of the reply to Rav Huna bar Hinnana',uncertainty=['The reply says א"ל rather than repeating the speaker’s name.'],composition='composite')
proverb=c('proverb','9b:12','דאמרי אינשי בת שיתין כבת שית לקל טבלא רהטא','A popular saying compares a woman of sixty to a girl of six running toward the drum’s sound.',scope='Quoted proverb supporting the response; not a medical generalization')
e('old_corrects',old,young,'correction','9b:12');e('proverb_support',proverb,old,'support','9b:12')
lime=c('lime','9b:13','אשה לא תסוד מפני שניוול הוא לה','Rabbi Yehuda prohibits lime application because it disfigures her.',candidates=['רבי יהודה'],scope='Quoted baraita, with the following removable-during-festival exception')
remove=c('remove','9b:13','ומודה ר\' יהודה בסיד שיכולה לקפלו במועד שטופלתו במועד','Rabbi Yehuda concedes permission when the lime can be removed during the festival.',candidates=['רבי יהודה'],conditions=['lime removable during the festival'])
happy=c('happy','9b:13','שאע"פ שמצירה היא עכשיו שמחה היא לאחר זמן','The explanation weighs present distress against later happiness.',scope='Reason for the removable-lime concession')
e('remove_qualifies',remove,lime,'qualification','9b:13');e('happy_reason',happy,remove,'support','9b:13')
challenge=q('challenge','9b:14','ומי אית ליה לרבי יהודה האי סברא','Does Rabbi Yehuda accept this reasoning?')
collect=c('collect','9b:15','רבי יהודה אומר נפרעין מהן מפני שמצר','The cited ruling permits collecting from them because collection causes distress.',candidates=['רבי יהודה'],scope='Quoted comparison with collection law; the excerpt does not itself state every surrounding condition')
reply=c('collection_reply','9b:15','אמרו לו אע"פ שמצר עכשיו שמח הוא לאחר זמן','His interlocutors object that present distress is followed by later happiness.',scope='Anonymous plural interlocutors in the cited collection dispute')
e('collection_objection',reply,collect,'objection','9b:15');e('comparison_challenge',challenge,happy,'objection','9b:15')
festival=c('festival','9b:16','אמר רב נחמן בר יצחק הנח להלכות מועד דכולהו מצר עכשיו ושמח לאחר זמן נינהו','Rav Nahman bar Yitzhak distinguishes festival laws, characterized here by present distress and later happiness.',candidates=['רב נחמן בר יצחק'],scope='Local resolution of the apparent inconsistency')
repay=c('repayment','9b:17','רבינא אמר כותי לענין פרעון לעולם מצר','Ravina answers that the person printed as כותי remains distressed over repayment.',candidates=['רבינא'],scope='Alternative local resolution; preserve printed כותי without harmonizing textual history')
e('festival_answer',festival,challenge,'answer','9b:16');e('repay_answer',repay,challenge,'answer','9b:17');e('answers_alternative',repay,festival,'distinction','9b:17')
for key,quote,text in [('poor','עניות טופלות אותן בסיד','Poor girls were treated with lime.'),('rich','עשירות טופלות אותן בסולת','Rich girls were treated with fine flour.'),('royal','בנות מלכים בשמן המור','Royal daughters were treated with myrrh oil.')]:
    c(key,'9b:18',quote,text,candidates=['רב יהודה'],conditions=['בנות ישראל שהגיעו לפירקן ולא הגיעו לשנים'],scope='Rav Yehuda’s reported custom, not advice to apply these substances',uncertainty=['Age/development phrase retained without supplying a precise numerical age.'])
verse=c('esther','9b:18','שנאמר (אסתר ב, יב) ששה חדשים בשמן המור','The source adduces Esther’s six months with myrrh oil.')
e('esther_support',verse,'mk.r022.royal.c','support','9b:18')
oilq=q('oil_q','9b:19','מאי שמן המור','What is myrrh oil?')
stacte=c('stacte','9b:19','רב הונא בר חייא אמר סטכת','Rav Huna bar Hiyya identifies it as סטכת.',candidates=['רב הונא בר חייא'])
olive=c('olive','9b:19','רב ירמיה בר אמי אמר שמן זית שלא הביא שליש','Rav Yirmeya bar Ami identifies it as oil from olives that have not reached one third.',candidates=['רב ירמיה בר אמי'])
e('stacte_answer',stacte,oilq,'answer','9b:19');e('olive_answer',olive,oilq,'answer','9b:19');e('oil_alternatives',olive,stacte,'distinction','9b:19')
bar=c('anpikinon','9b:20','רבי יהודה אומר אנפיקינון שמן זית שלא הביא שליש','Rabbi Yehuda identifies anpikinon as oil from olives not yet one third grown.',candidates=['רבי יהודה'])
why=q('why','9b:20','ולמה סכין אותו','Why is it used for anointing?')
use=c('use','9b:20','שמשיר את השער ומעדן את הבשר','The explanation says it removes hair and softens the flesh.',composition='composite',scope='Reported ancient explanation, not efficacy or safety advice')
e('use_answer',use,why,'answer','9b:20')
bibi=c('bibi','9b:21','רב ביבי הוה ליה ברתא טפלה אבר אבר שקל בה ד\' מאה זוזי','Rav Bibi treated his daughter limb by limb and received four hundred zuz in connection with her.',scope='Reported narrative; transaction details not expanded beyond the source')
neighbor=c('neighbor','9b:21','הוה ההוא כותי בשבבותיה דה"ל ברתא טפלה בחד זמנא ומתה','A neighboring man, printed as כותי, treated his daughter all at once and she died.',scope='Contrasting narrative retained, without silently changing printed identity')
blame=c('blame','9b:21','אמר קטלא ביבי לברתי','The neighbor blamed Bibi for his daughter’s death.',candidates=['unnamed neighbor'],mode='challenged',scope='Quoted accusation, not the narrator’s adjudicated causation')
nahman=c('nahman','9b:21','אמר רב נחמן רב ביבי דשתי שיכרא בעיין בנתיה טפלא אנן דלא שתינן שיכרא לא בעיין בנתין טפלא','Rav Nahman contrasts Bibi, who drinks beer and whose daughters need treatment, with his own non-beer-drinking group whose daughters do not.',candidates=['רב נחמן'],composition='composite',scope='Source’s reported explanation, not a general medical claim')
e('nahman_reply',nahman,blame,'qualification','9b:21')
for row in a.rows:
    if row['layer']=='edges' and row['id'].endswith(('answers_alternative','oil_alternatives')):
        row['content']['explicitness']='editorial_reconstruction'
        row['uncertainty'].append('Editorial linkage of adjacent named alternative explanations; no source assertion that these are exhaustive.')
a.save_window(refs,'resume_moed_katan_adornment022c.json','Direct reading of every segment9b:10–21 with continuation through10b. Preserve versions, age restriction/rebuttal, temporary-discomfort conditions, anonymous interlocutors, two resolutions, customs and death narrative; retain printed identities and supported uncertainty.','d3ceaedc2fdda6cc2913a765e5e9594a9740a69fd1ac2452488c21537983bd5e')
