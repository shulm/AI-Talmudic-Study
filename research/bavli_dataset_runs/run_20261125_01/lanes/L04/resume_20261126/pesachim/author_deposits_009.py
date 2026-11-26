"""Explicit source readings 5b:2–6a:10. No automatic extraction."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('pesachim','Pesachim','pe.r009');a.agent_id='/root/pesachim_continuation_2'
def c(k,ref,quote,text,**kw):
    cid=a.claim(k,ref,quote,text,**kw)
    for row in a.rows[-2:]:row['evidence']=[a.span(ref,quote)]
    return cid
def q(k,ref,quote,text):
    qid=a.question(k,ref,quote,text);a.rows[-1]['evidence']=[a.span(ref,quote)];return qid
def e(k,x,y,rel,ref):
    if rel=='answer':
        for row in a.rows:
            if row['id']==y and row['layer']=='questions':
                row['content']['answer_set_status']='partial';row['uncertainty']=['Only actually represented local answers; no exhaustive inventory or choice eligibility.']
    return a.e(k,x,y,rel,ref)
refs=['5b:'+str(i) for i in range(2,19)]+['6a:'+str(i) for i in range(1,11)]
a.structure('deposits',['5b:'+str(i) for i in range(2,19)]+['6a:1'],'Leaven ownership, deposits and accepted liability: baraita and competing interpretations')
a.structure('tax',['6a:'+str(i) for i in range(2,6)],'Two versions of Rava on tax-liable animals, with dough distinction')
a.structure('house',['6a:'+str(i) for i in range(6,11)],'Deposited dough and assigned house: proof attachment and possession')
why=q('why','5b:2',a.refs['5b:2']['text'],'What does the prohibition on leaven being found in houses add to the prohibition on seeing it throughout one’s boundaries?')
own=c('own','5b:3','שלך אי אתה רואה אבל אתה רואה של אחרים ושל גבוה','The teaching reads לך as prohibiting one’s own leaven while allowing that of others and of the sacred domain.',composition='composite',scope='Quoted baraita; later qualified by accepted responsibility for others’ property')
hideq=q('hideq','5b:3','יכול יטמין ויקבל פקדונות מן הנכרי','Might one hide leaven or accept deposits from a gentile?')
hide=c('hide','5b:3','ת"ל לא ימצא','The prohibition לא ימצא excludes hiding and accepting the stated deposits.',composition='composite',scope='Baraita’s additional prohibition; responsibility distinction follows in 5b:14')
e('hide.answer',hide,hideq,'answer','5b:3');e('hide.why',hide,why,'answer','5b:3')
conq=q('conq','5b:4','אין לי אלא בנכרי שלא כיבשתו ואין שרוי עמך בחצר נכרי שכיבשתו ושרוי עמך בחצר מנין','How does the rule extend from a non-subjugated gentile not residing in the courtyard to a subjugated one residing there?')
con=c('con','5b:4','ת"ל לא ימצא בבתיכם','The baraita invokes לא ימצא בבתיכם for the second gentile case.',scope='Direction of this derivation is questioned in 5b:10–12; do not flatten to a final ownership rule',uncertainty=['Abaye reverses the cases; Rava preserves order and attaches this passage to permission. Both interpretations are retained below.'])
e('con.answer',con,conq,'answer','5b:4')
spaceq=q('spaceq','5b:5','אין לי אלא שבבתיכם בבורות בשיחין ובמערות מנין','How are pits, trenches and caves included beyond houses?')
space=c('space','5b:5','ת"ל בכל גבולך','בכל גבולך extends the stated scope beyond houses.',scope='Baraita’s spatial extension')
e('space.answer',space,spaceq,'answer','5b:5')
sep=c('sep','5b:6','ועדיין אני אומר בבתים עובר משום בל יראה ובל ימצא ובל יטמין ובל יקבל פקדונות מן הנכרי בגבולין שלך אי אתה רואה אבל אתה רואה של אחרים ושל גבוה','A provisional reading assigns the four prohibitions to houses and the ownership permission to boundaries.',mode='hypothetical',composition='composite',scope='Provisional asymmetry that the verbal analogy removes')
exchange=q('exchange','5b:6','מניין ליתן את האמור של זה בזה ושל זה בזה','How are the rules of each passage applied to the other?')
analogy=c('analogy','5b:7','ת"ל שאור שאור לגזרה שוה','Repeated שאור supports a verbal analogy between houses and boundaries.',scope='Baraita’s explicit gezerah shavah')
e('analogy.answer',analogy,exchange,'answer','5b:7');e('analogy.correction',analogy,sep,'correction','5b:7')
four=c('four','5b:7','אף שאור האמור בגבולין עובר משום בל יראה ובל ימצא ובל יטמין ובל יקבל פקדונות מן הנכרי','The house prohibitions of seeing, finding, hiding, and receiving the stated deposits also apply throughout the boundaries.',composition='composite',conditions=['relevant leaven ownership/liability conditions clarified below'],scope='Four-item conclusion, not four certified atomic records')
permit=c('permit','5b:8',a.refs['5b:8']['text'],'The permission for others’ and sacred leaven applies within houses as well as within boundaries.',composition='composite',scope='Reciprocal ownership-permission conclusion')
e('four.support',analogy,four,'support','5b:7');e('permit.support',analogy,permit,'support','5b:8')
repeat=c('repeat','5b:9',a.refs['5b:9']['text'],'The discussion repeats the baraita’s two gentile cases and its לא ימצא citation.',composition='composite',scope='Repeated source occurrence preserved separately from 5b:4')
e('repeat.quotation',repeat,con,'quotation','5b:9')
reverseq=q('reverseq','5b:10','כלפי לייא','Does the derivation run in the wrong direction?')
abaye=c('abaye','5b:10','אמר אביי איפוך','Abaye answers by reversing the cases.',candidates=['אביי'],scope='Explicit textual reversal proposal, not silent emendation of original baraita')
e('abaye.answer',abaye,reverseq,'answer','5b:10');e('abaye.correction',abaye,repeat,'correction','5b:10')
rava=c('rava','5b:11',a.refs['5b:11']['text'],'Rava keeps the case order and attaches the derivation to the opening permission to see others’ or sacred leaven, extending it to the subjugated resident gentile.',candidates=['רבא'],composition='composite',scope='Alternative explanation; no final selection between Abaye and Rava is stated')
e('rava.answer',rava,reverseq,'answer','5b:11');e('rava.distinction',rava,abaye,'distinction','5b:11')
permitq=q('permitq','5b:12','והאי תנא מיהדר אהיתירא ונסיב לה קרא לאיסורא','Why would the tanna seek permission but cite wording of prohibition?')
twice=c('twice','5b:12','משום שנאמר לך לך תרי זימני','The answer invokes the doubled לך.',scope='Reply supporting Rava’s permission interpretation')
e('twice.answer',twice,permitq,'answer','5b:12');e('twice.support',twice,rava,'support','5b:12')
contr=q('contr','5b:13',a.refs['5b:13']['text'],'How does the ban on accepting gentile deposits fit the stated permission for others’ and sacred leaven?')
liab=c('liab','5b:14','הא דקביל עליה אחריות','The prohibition concerns accepted responsibility.',conditions=['recipient accepted responsibility'],scope='First side of the anonymous reconciliation')
noliab=c('noliab','5b:14','הא דלא קביל עליה אחריות','The permission concerns no accepted responsibility.',conditions=['recipient did not accept responsibility'],scope='Second side of the anonymous reconciliation')
e('liab.answer',liab,contr,'answer','5b:14');e('noliab.answer',noliab,contr,'answer','5b:14');e('liab.distinction',liab,noliab,'distinction','5b:14')
soldier=c('soldier','5b:15','כי הא דאמר להו רבא לבני מחוזא בעירו חמירא דבני חילא מבתייכו','Rava directs the people of Mehoza to remove the soldiers’ leaven from their houses.',candidates=['רבא'],conditions=['soldiers’ leaven held with the responsibility stated in the continuation'],scope='Reported practical instruction with named audience')
pay=c('pay','5b:15','כיון דאילו מיגנב ואילו מיתביד ברשותייכו קאי ובעיתו לשלומי כדילכון דמי ואסור','Because they must pay if the leaven is stolen or lost, it is treated as theirs and is prohibited.',candidates=['רבא'],conditions=['liability for theft or loss'],scope='Rava’s stated rationale for the Mehoza instruction')
e('pay.support',pay,soldier,'support','5b:15');e('soldier.support',soldier,liab,'support','5b:15')
moneyq=q('moneyq','5b:16',a.refs['5b:16']['text'],'How does this work for the view that something causing monetary liability is not treated as money?')
text=c('text','5b:17','שאני הכא דאמר לא ימצא','The reply distinguishes this case because Scripture says לא ימצא.',scope='First version’s reply; unnamed monetary positions are not assigned to invented speakers')
e('text.answer',text,moneyq,'answer','5b:17')
alt=c('alt','5b:18',a.refs['5b:18']['text'],'An alternative version begins by accepting the need for לא ימצא under the view that monetary consequence does not count as money.',scope='Explicit איכא דאמרי; question continues into 6a:1')
altq=q('altq','6a:1','אלא למאן דאמר כממון דמי לא ימצא למה לי','Under the view that monetary consequence does count as money, why is לא ימצא needed?')
# Alternative-version structure spans both pages; no semantic continuation edge under the common enum.
returnhyp=c('returnhyp','6a:1','סלקא דעתך אמינא הואיל וכי איתיה הדר בעיניה לאו ברשותיה קאי','One might suppose that because the existing object is returned intact it is not in the recipient’s domain.',mode='hypothetical',conditions=['deposit remains intact and is returned in kind'],scope='Rejected supposition explaining need for the verse')
need=c('need','6a:1','איצטריך סלקא דעתך אמינא הואיל וכי איתיה הדר בעיניה לאו ברשותיה קאי קמשמע לן','The verse is still required to exclude that intact-return supposition.',scope='Alternative version’s resolution, completed by קמשמע לן')
e('need.answer',need,altq,'answer','6a:1');e('need.correction',need,returnhyp,'correction','6a:1')
taxq=q('taxq','6a:2','בעו מיניה מרבא בהמת ארנונא חייבת בבכורה או אין חייבת בבכורה','They ask Rava whether an animal subject to arnona is obligated in the firstborn law.')
redeem=c('redeem','6a:2','כל היכא דמצי מסלק ליה בזוזי לא קא מיבעיא לן דחייב','Where the tax interest can be discharged with money, liability in the firstborn law is treated as unquestioned.',conditions=['tax interest redeemable with money'],scope='First version’s framing premise')
noredeemq=q('noredeemq','6a:3','כי קא מיבעיא לן היכא דלא מצי מסלק ליה בזוזי מאי','What is the rule when the tax interest cannot be discharged with money?')
exempt=c('exempt','6a:3','אמר להו פטורה','Rava answers that the animal is exempt.',candidates=['רבא'],naming_refs=['6a:2'],conditions=['tax interest cannot be discharged with money'],scope='First version’s answer only')
e('exempt.answer',exempt,noredeemq,'answer','6a:3');e('exempt.general',exempt,taxq,'answer','6a:3')
baraita=c('baraita','6a:3','והתניא חייבת','A baraita obligating the animal is raised as a challenge.',mode='challenged',scope='Quoted contrary-looking rule')
limited=c('limited','6a:3','התם דמצי מסלק ליה','The baraita concerns a case where the tax interest can be discharged.',conditions=['tax interest redeemable with money'],scope='First version’s anonymous reconciliation')
e('baraita.objection',baraita,exempt,'objection','6a:3');e('limited.answer',limited,baraita,'answer','6a:3')
altanimal=c('altanimal','6a:4','איכא דאמרי אמר רבא בהמת ארנונא פטורה מן הבכורה ואע"ג דמצי מסלק ליה','An alternative report has Rava exempting the arnona animal from firstborn law even when the tax can be discharged.',candidates=['רבא'],conditions=['even redeemable tax interest'],scope='Explicit alternative version, not merged with the first report')
altdough=c('altdough','6a:4','עיסת ארנונא חייבת בחלה ואע"ג דלא מצי מסלק ליה','The alternative report obligates arnona dough in challa even when the tax cannot be discharged.',candidates=['רבא'],conditions=['even nonredeemable tax interest'],scope='Dough clause within the alternative report')
e('altanimal.distinction',altanimal,redeem,'distinction','6a:4');e('altdough.distinction',altdough,altanimal,'distinction','6a:4')
whypublic=q('whypublic','6a:5','מאי טעמא','What explains the animal/dough distinction?')
public=c('public','6a:5','בהמה אית לה קלא עיסה לית לה קלא','The animal’s status is publicized; the dough’s is not.',composition='composite',scope='Anonymous explanation of the alternative version')
e('public.answer',public,whypublic,'answer','6a:5')
visit=c('visit','6a:6','נכרי שנכנס לחצירו של ישראל ובציקו בידו אין זקוק לבער','A gentile entering an Israelite’s courtyard with dough in his hand does not require its removal.',conditions=['dough remains in the visiting gentile’s hand'],scope='Quoted baraita')
deposit=c('deposit','6a:6','הפקידו אצלו זקוק לבער','When deposited with the Israelite the dough requires removal.',conditions=['deposit with the Israelite'],scope='Baraita clause, read in light of the earlier liability distinction')
assigned=c('assigned','6a:6','יחד לו בית אין זקוק לבער','If a house is designated for the gentile’s dough, removal is not required.',conditions=['designated house'],scope='Baraita’s final clause, proof attachment debated next')
attach=q('attach','6a:7','מאי קאמר','To which clause does the baraita’s לא ימצא citation attach?')
pappa=c('pappa','6a:7','אמר רב פפא ארישא קאי והכי קאמר הפקידו אצלו זקוק לבער שנאמר לא ימצא','Rav Pappa attaches the citation to the deposit clause requiring removal.',candidates=['רב פפא'],scope='First proof-attachment interpretation')
e('pappa.answer',pappa,attach,'answer','6a:7');e('pappa.support',pappa,deposit,'support','6a:7')
ashi=c('ashi','6a:8',a.refs['6a:8']['text'],'Rav Ashi attaches the citation to the designated-house exemption: the gentile brings the dough into his own designated house, outside your houses.',candidates=['רב אשי'],scope='Second proof-attachment interpretation; ownership inference challenged next')
e('ashi.answer',ashi,attach,'answer','6a:8');e('ashi.support',ashi,assigned,'support','6a:8');e('ashi.distinction',ashi,pappa,'distinction','6a:8')
leaseq=q('leaseq','6a:9','למימרא דשכירות קניא','Does this imply that rental acquires ownership?')
lease=c('lease','6a:9','והתנן אף במקום שאמרו להשכיר לא לבית דירה אמרו מפני שמכניסין לתוכו ע"ז','A Mishnah forbids renting for residence even where rental is otherwise permitted because the occupant introduces idolatry.',conditions=['rental for residence in the cited legal setting'],scope='Quoted counterexample, not a new comprehensive rental rule')
reductio=c('reductio','6a:9','ואי סלקא דעתך דשכירות קניא כי קא מעייל לביתיה דנפשיה קא מעייל','If rental acquired the house, the occupant would be introducing the idol into his own house.',mode='hypothetical',conditions=['suppose rental acquires ownership'],scope='Counterargument to an ownership inference')
e('lease.objection',lease,ashi,'objection','6a:9');e('reductio.support',reductio,leaseq,'support','6a:9')
found=c('found','6a:10',a.refs['6a:10']['text'],'Leaven is different because לא ימצא refers to what is available in one’s control, excluding what is not.',scope='Availability/control distinction resolves the rental objection without a general acquisition rule')
e('found.answer',found,leaseq,'answer','6a:10');e('found.qualification',found,ashi,'qualification','6a:10')
a.save_window(refs,'pesachim_deposits_009b.json','Reread original 5b:2–6a:10 with later context. Preserve repeated baraita, explicit reversal versus unchanged wording, liability conditions, both versions of arnona, and proof attachment alternatives.',expected_parent='3e4bd6986f4b51b39589084d1bf932dd1f79b642277923a9651cdf711088eabf')


