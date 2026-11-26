import json,hashlib,re
from pathlib import Path
root=Path(__file__).parent
source=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Nashim/Ketubot/Hebrew/Wikisource Talmud Bavli.json')
raw=source.read_bytes(); h=hashlib.sha256(raw).hexdigest()
assert h=='f736ba10fa498bbe884bd4243f334fec4b8ccd2161b6a29cbe8cc58649451d4a'
d=json.loads(raw)
def get(ref):
 m=re.fullmatch(r'(\d+)([ab]):(\d+)',ref); i=(int(m[1])-1)*2+(m[2]=='b');j=int(m[3])-1
 return i,j,d['text'][i][j]
def ev(ref,q=None):
 i,j,s=get(ref);q=s if q is None else q;a=s.index(q)
 return dict(ref='Ketubot '+ref,raw_page_index=i,raw_segment_index=j,start=a,end=a+len(q),quote=q)
claims=[]
def add(id,ref,kind,holder,quote,meaning,conditions='',status='locally_asserted',transmission=None):
 claims.append(dict(id=id,evidence=ev(ref,quote),cohort='core' if ref.startswith('3b:') else 'context',kind=kind,holder=holder,transmission=transmission or [],explanation=meaning,conditions=conditions,local_status=status))
# Independent atomic inventory; Hebrew strings are evidence, English strings reviewer explanation.
rows='''
c01|3b:1|rule|anonymous baraita|בתולה נשאת ליום הרביעי|Virgin marries Wednesday.|ordinary schedule
c02|3b:1|reason|anonymous baraita|שאם היה לו טענת בתולים היה משכים לב"ד|Allows prompt next-morning resort to court.|husband has virginity claim
q01|3b:1|question|anonymous baraita|ותנשא באחד בשבת|Why not marry Sunday instead?|court next day
c03|3b:1|reason|anonymous baraita|שקדו חכמים על תקנת בנות ישראל שיהא אדם טורח בסעודה שלשה ימים אחד בשבת ושני בשבת ושלישי בשבת וברביעי כונסה|Three days' feast preparation Sunday through Tuesday underlies Wednesday wedding.|ordinary case
c04|3b:2|practice|anonymous baraita|ומסכנה ואילך נהגו העם לכנוס בשלישי|From danger onward people married Tuesday.|danger period
c05|3b:2|response|anonymous baraita|ולא מיחו בידם חכמים|Sages did not protest the Tuesday practice.|c04 circumstances
c06|3b:2|rule|anonymous baraita|ובשני לא יכנוס|Do not marry Monday.|ordinary exception to Wednesday
c07|3b:2|exception|anonymous baraita|ואם מחמת האונס מותר|Compulsion permits it.|Monday marriage; nature of compulsion discussed below
c08|3b:2|rule|anonymous baraita|ומפרישין את החתן מן הכלה לילי שבת תחלה|Separate bridegroom and bride on Sabbath night initially.|initial intercourse
c09|3b:2|reason|anonymous baraita|מפני שהוא עושה חבורה|Reason given is making a wound.|c08
q02|3b:3|question|anonymous discussion|מאי סכנה|What danger is meant?|
h01|3b:3|hypothesis|anonymous discussion|אילימא דאמרי בתולה הנשאת ליום הרביעי תיהרג|Proposed decree: a virgin marrying Wednesday is killed.|rejected hypothetical
q03|3b:3|objection|anonymous discussion|נהגו לגמרי ניעקריה|Mere tolerated custom would be inadequate; abolish the rule entirely.|h01
c10|3b:4|interpretation|Rabbah (רבה)|אמר רבה דאמרי בתולה הנשאת ביום הרביעי תיבעל להגמון תחלה|Decree requires Wednesday bride first be subjected to intercourse by the governor.|interpretation of danger
q04|3b:4|objection|anonymous discussion|האי סכנה אונס הוא|That is coercion rather than danger.|c10
c11|3b:4|answer|anonymous discussion|משום דאיכא צנועות דמסרן נפשייהו לקטלא ואתיין לידי סכנה|Some modest women risk death resisting, explaining danger.|c10
q05|3b:5|question|anonymous discussion|ולידרוש להו דאונס שרי|Why not teach that coercion is permitted?|scope of permission not spelled out here
c12|3b:5|answer|anonymous discussion|איכא פרוצות|Presence of licentious women prevents that proposed solution.|q05
c13|3b:5|answer|anonymous discussion|ואיכא נמי כהנות|There are also kohanot.|q05; practical consequence implicit rather than expanded in source
q06|3b:6|question|anonymous discussion|וליעקריה|Why not abolish the enactment?|
c14|3b:6|reason|anonymous discussion|גזירה עבידא דבטלא|The decree is liable to cease.|
c15|3b:6|answer|anonymous discussion|ותקנתא דרבנן מקמי גזירה לא עקרינן|Do not uproot rabbinic enactment because of such a decree.|c14
q07|3b:6|objection|anonymous discussion|אי הכי בשלישי נמי אתי ובעיל|Governor could also come on Tuesday.|Tuesday workaround
c16|3b:6|answer|anonymous discussion|מספיקא לא עקר נפשיה|He will not exert himself on a doubt.|Tuesday wedding not certain
q08|3b:7|question|anonymous discussion|מאי אונס|What compulsion permits Monday?|
h02|3b:7|hypothesis|anonymous discussion|אילימא הא דאמרן|Perhaps the previously described decree.|rejected hypothetical
q09|3b:7|objection|anonymous discussion|התם קרי ליה סכנה והכא קא קרי ליה אונס|Terminology differs: danger there, compulsion here.|h02
q10|3b:7|objection|anonymous discussion|ותו התם נהגו הכא מותר|There it is customary practice, here explicit permission.|h02
c17|3b:8|interpretation|Rava (רבא)|אמר רבא דאמרי שר צבא בא לעיר|The army commander is coming to town.|explanation of compulsion
q11|3b:8|question|anonymous discussion|אי דאתי וחליף ליעכב|If merely passing through, why not delay?|
c18|3b:8|answer|anonymous discussion|לא צריכא דאתי וקבע|He comes and stays.|c17 qualification
q12|3b:8|objection|anonymous discussion|בג' מיהא לכנוס|Still marry Tuesday.|
c19|3b:8|answer|anonymous discussion|אספרווא דידיה בג' קאתו|His advance personnel arrive Tuesday.|c17 qualification; exact personnel role not expanded
c20|3b:9|alternative_interpretation|anonymous discussion|ואיבעית אימא מאי מחמת האונס כדתני'|Alternative compulsion explanation introduces a baraita.|alternative to c17
c21|3b:9|rule|anonymous baraita|מכניסין את המת לחדר|Put deceased in a room.|bread baked, meat slaughtered, wine mixed; groom's father or bride's mother died
c22|3b:9|rule|anonymous baraita|ואת החתן ואת הכלה לחופה|Bring bride and groom to wedding canopy.|same prepared-feast and bereavement conditions as c21
x01|3a:12|rule|Rav Shmuel bar Yitzhak|לא שנו אלא מתקנת עזרא ואילך שאין בתי דינין קבועין אלא בשני ובחמישי|Wednesday restriction applies under post-Ezra Monday/Thursday court schedule.|not Rav or Shmuel
x02|3a:12|rule|Rav Shmuel bar Yitzhak|אבל קודם תקנת עזרא שבתי דינין קבועין בכל יום אשה נשאת בכל יום|Daily courts allow marriage any day.|pre-Ezra schedule
xq01|3a:13|objection|anonymous discussion|קודם תקנת עזרא מאי דהוה הוה|Why discuss the past?|
x03|3a:13|interpretation|anonymous discussion|אי איכא בתי דינין דקבועין האידנא כקודם תקנת עזרא אשה נשאת בכל יום|Applies now if courts sit daily.|
xq02|3a:14|objection|anonymous discussion|הא בעינן שקדו|Preparation requirement still applies.|
x04|3a:14|answer|anonymous discussion|דטריח ליה|Case where he has already prepared.|daily-court flexibility
x05|4a:1|rule|anonymous baraita|ובועל בעילת מצוה ופורש|Consummates and separates.|continuation of prepared-feast bereavement case
x06|4a:1|rule|anonymous baraita|ונוהג שבעת ימי המשתה ואחר כך נוהג שבעת ימי אבילות|Seven wedding days precede seven mourning days.|same case
x07|4a:1|rule|anonymous baraita|וכל אותן הימים הוא ישן בין האנשים והיא ישנה בין הנשים|Separate supervised sleeping throughout those days.|same case; continuation qualifies scope
x08|4a:1|rule|anonymous baraita|ואין מונעין תכשיטין מן הכלה כל שלשים יום|Do not withhold bridal adornments for thirty days.|
x09|4a:2|qualification|anonymous discussion|ודוקא אביו של חתן או אמה של כלה דליכא איניש דטרח להו|Applies specifically to groom's father or bride's mother because no replacement prepares.|prepared-feast case
x10|4a:2|exclusion|anonymous discussion|אבל איפכא לא|Reverse parent cases excluded.|bride's father or groom's mother inferred from contrast
x11|4a:3|qualification|Rav Hisda|לא שנו אלא שנתן מים על גבי בשר|Applies when water already placed on meat.|reported by Rafram bar Pappa
x12|4a:3|reason|Rav Hisda|אבל לא נתן מים על גבי בשר מזדבן|Without water, meat can be sold.|reported by Rafram bar Pappa
x13|4a:4|qualification|Rava|ובכרך אע"פ שנתן מים על גבי בשר מזדבן|In a city meat sells even after water.|prepared-feast urgency restricted
x14|4a:4|qualification|Rav Pappa|ובכפר אע"פ שלא נתן מים על גבי בשר לא מזדבן|In village meat will not sell even without water.|
xq03|4a:4|question|anonymous discussion|ואלא דרב חסדא היכי משכחת לה|Where does Rav Hisda's distinction apply?|
x15|4a:4|answer|Rav Ashi|כגון מתא מחסיא דמפקא מכרך ומפקא מכפר|Intermediate town such as Mata Mehasya.|neither city nor village
x16|4a:5|supporting_baraita|anonymous baraita|ונתן מים על גבי בשר|Repeated bereavement baraita explicitly includes water on meat.|support for Rav Hisda; preserve distinct occurrence
x17|4a:6|rule|anonymous baraita|וכן מי שפירסה אשתו נדה הוא ישן בין האנשים והיא ישנה בין הנשים|Separate sleeping when wife becomes menstruant.|later narrowed to no prior intercourse
x18|4a:6|rule|anonymous baraita|ואין מונעין תכשיטין מן הכלה כל ל' יום|Repeated thirty-day adornment rule.|distinct occurrence
x19|4a:6|rule|anonymous baraita|בין כך ובין כך לא יבעול לא בערב שבת ולא במוצ"ש|No initial intercourse on Sabbath eve or Saturday night.|both stated cases
x20|4a:7|rule|Rabbi Yohanan|אע"פ שאמרו אין אבילות במועד אבל דברים של צינעא נוהג|Though no festival mourning, private mourning observances apply.|separate sleeping cited as support
x21|4a:8|qualification|Rava|ל"ש אלא שלא בעל|Separation qualification applies if no intercourse occurred.|Rav Yosef son of Rava expounds in Rava's name; initially scope uncertain
x22|4a:8|rule|Rava|אבל בעל אשתו ישנה עמו|If intercourse occurred wife sleeps with him.|same transmission; subsequently scoped to menstruation
xq04|4a:9|objection|anonymous discussion|והא הכא דבבעל עסקינן וקתני הוא ישן בין האנשים והיא ישנה בין הנשים|Bereavement case already includes intercourse but requires separation.|
x23|4a:9|scope_answer|anonymous discussion|כי קאמר אפירסה אשתו נדה|Rava's qualification concerns menstruation.|
xq05|4a:10|objection|anonymous discussion|הא וכן קתני|But baraita says likewise.|
x24|4b:1|restatement|anonymous discussion|וכן מי שפירסה אשתו נדה ולא בעל|Restates menstruation rule as before intercourse.|limits analogy
xq06|4b:2|question|anonymous discussion|למימרא דאבילות קילא ליה מנדה|Does this imply mourning is treated more lightly than menstruation?|
x25|4b:3|rule|Rav Huna|כל מלאכות שאשה עושה לבעלה נדה עושה לבעלה|Menstruant wife performs ordinary services.|reported by Rabbi Yitzhak bar Hanina
x26|4b:3|exception|Rav Huna|חוץ ממזיגת הכוס והצעת המטה והרחצת פניו ידיו ורגליו|Except pouring cup, making bed, washing his face/hands/feet.|same transmission
x27|4b:3|rule|anonymous baraita|אין אדם רשאי לכוף את אשתו להיות כוחלת ולהיות פוקסת|Cannot compel wife to apply cosmetics.|mourning
x28|4b:3|rule|anonymous baraita|מוזגת לו הכוס ומצעת לו המטה ומרחצת לו פניו ידיו ורגליו|Cup, bed and washing permitted in mourning.|challenging relative-leniency inference
x29|4b:4|reconciliation|anonymous discussion|כאן באבילות דידיה כאן באבילות דידה|Distinguish his mourning and hers.|which clause maps where inferred from continuation, not explicit in this string
xq07|4b:5|objection|anonymous discussion|והא אביו של חתן או אמה של כלה קתני|Earlier baraita includes both spouses' bereavement.|
x30|4b:5|answer|anonymous discussion|כי קתני אשארא|That phrase refers to other provisions.|separation scope not both cases under this answer
x31|4b:6|baraita|anonymous baraita|מי שמת חמיו או חמותו אינו יכול לכוף את אשתו להיות כוחלת ולהיות פוקסת|On wife's bereavement husband cannot compel cosmetics.|
x32|4b:6|baraita|anonymous baraita|אלא כופה מטתו ונוהג עמה אבילות|He overturns bed and observes mourning with her.|
x33|4b:6|baraita|anonymous baraita|וכן היא שמת חמיה או חמותה אינה רשאה להיות כוחלת ולהיות פוקסת|On husband's bereavement wife must not apply cosmetics.|
x34|4b:6|baraita|anonymous baraita|אלא כופה מטתה ונוהגת עמו אבילות|She overturns bed and mourns with him.|challenges husband/wife distinction
x35|4b:7|restatement|anonymous discussion|תני באבילות דידיה הוא ישן בין האנשים ואשתו ישנה בין הנשים|Read separation provision as his mourning.|
x36|4b:7|scope_answer|anonymous discussion|כי קתני אכיחול ואפירכוס|Likewise concerns cosmetics.|
x37|4b:7|interpretation|anonymous discussion|לא עמו בבית|With him means in house rather than bed.|answer to inferred shared bed
x38|4b:7|instruction|Rav|באפה נהוג אבילותא דלא באפה לא תנהוג אבילותא|Observe mourning in her presence, not outside it.|addressed to his son Hiyya
x39|4b:8|alternative_reconciliation|Rav Ashi|אבילותא דעלמא חמיר ולא אתי לזלזולי ביה|Ordinary mourning treated seriously; no concern of disregard.|
x40|4b:8|reason|Rav Ashi|אבילות דהכא כיון דאקילו רבנן אתי לזלזולי ביה|Here rabbinic leniency risks disregard.|special wedding bereavement
xq08|4b:9|question|anonymous discussion|מאי קולא|Which leniency?|
xh01|4b:9|hypothesis|anonymous discussion|אילימא דקתני בועל בעילת מצוה ופורש|Perhaps permission to consummate and separate.|rejected
x41|4b:9|rejection|anonymous discussion|התם משום דלא חל עליו אבילותא|Mourning has not yet begun then.|rejects xh01
x42|4b:9|timing|Rabbi Eliezer|עד שיצא מפתח הבית|Mourning onset at leaving house entrance.|cited alternative authority
x43|4b:9|timing|Rabbi Yehoshua|עד שיסתם הגולל|Mourning onset at closing burial covering.|cited alternative authority
x44|4b:10|answer|anonymous discussion|נוהג שבעת ימי המשתה ואח"כ נוהג שבעת ימי אבילות|Leniency is postponing mourning until after wedding week.|
x45|4b:11|reason|anonymous discussion|בשלמא בערב שבת משום חבורה|Sabbath-eve reason understood as wound.|
xq09|4b:11|question|anonymous discussion|אלא במוצאי שבת אמאי לא|Why prohibit Saturday night?|
x46|5a:1|reason|Rabbi Zeira|משום חשבונות|Because of calculations.|speaker introduced at 4b:12; rejected below
xq10|5a:2|objection|Abaye|וחשבונות של מצוה מי אסירי|Are mitzvah calculations forbidden?|
x47|5a:2|rule|Rav Hisda and Rav Hamnuna jointly|חשבונות של מצוה מותר לחשבן בשבת|Mitzvah calculations permitted on Sabbath.|
x48|5a:2|rule|Rabbi Elazar|פוסקין צדקה לעניים בשבת|Pledge charity for poor on Sabbath.|
x49|5a:2|rule|Rabbi Yohanan|הולכין לבתי כנסיות ולבתי מדרשות לפקח על עסקי רבים בשבת|Attend synagogues/study halls to oversee public affairs on Sabbath.|reported by Rabbi Yaakov
x50|5a:2|rule|Rabbi Yohanan|מפקחין פיקוח נפש בשבת|Attend to saving life on Sabbath.|reported by Rabbi Yaakov bar Idi
x51|5a:3|rule|Rabbi Yonatan|הולכין לטרטייאות ולקרקייאות לפקח על עסקי רבים בשבת|Go to theaters/circuses for public affairs on Sabbath.|reported by Rav Shmuel bar Nahmani
x52|5a:3|rule|school of Menashya|משדכין על התינוקת ליארס בשבת|Arrange girl's betrothal on Sabbath.|
x53|5a:3|rule|school of Menashya|ועל התינוק ללמדו ספר וללמדו אומנות|Arrange child's literacy and trade instruction on Sabbath.|
x54|5a:4|replacement_reason|Rabbi Zeira|גזירה שמא ישחוט בן עוף|Decree lest he slaughter a young bird.|replaces calculations reason
xq11|5a:4|objection|Abaye|יום הכפורים שחל להיות בשני בשבת ידחה גזירה שמא ישחוט בן עוף|Then defer Monday Yom Kippur because of same concern?|
x55|5a:4|answer|anonymous discussion|התם דלנפשיה לא טריד הכא דלאחרים טריד|Own preparation less distracting than preparation for others.|Yom Kippur versus wedding
x56|5a:4|alternative_answer|anonymous discussion|אי נמי התם אית ליה רווחא הכא לית ליה רווחא|Alternatively there time is available, here not.|same challenge; precise time explanation not elaborated
x57|5a:5|extension|anonymous discussion|ערב שבת נמי גזירה שמא ישחוט בן עוף|Slaughter concern applies also on Sabbath eve.|in light of replacement explanation
'''
for line in rows.strip().splitlines():
 fields=line.split('|'); assert len(fields)==7,line
 add(*fields)
for c in claims:
 if c['id'] in ['h01','h02','xh01']:c['local_status']='rejected_hypothesis'
 if c['id']=='x46':c['local_status']='superseded_reason'
 if c['kind'] in ['question','objection']:c['local_status']='posed_not_holder_position'
chains={'x11':['Rafram bar Pappa','Rav Hisda'],'x12':['Rafram bar Pappa','Rav Hisda'],'x21':['Rav Yosef son of Rava','Rava'],'x22':['Rav Yosef son of Rava','Rava'],'x25':['Rabbi Yitzhak bar Hanina','Rav Huna'],'x26':['Rabbi Yitzhak bar Hanina','Rav Huna'],'x49':['Rabbi Yaakov','Rabbi Yohanan'],'x50':['Rabbi Yaakov bar Idi','Rabbi Yohanan'],'x51':['Rav Shmuel bar Nahmani','Rabbi Yonatan']}
for c in claims:
 c['transmission']=chains.get(c['id'],[])
 if c['id']=='x46':c['additional_evidence']=[ev('4b:12')]
# Repeated baraita actions remain distinct occurrences, not silently collapsed.
for n,(quote,meaning) in enumerate([
 ('מכניסין את המת לחדר','Put deceased in room.'),('ואת החתן ואת הכלה לחופה','Bring bride and groom to canopy.'),('ובועל בעילת מצוה ופורש','Consummate and separate.'),('ונוהג שבעת ימי המשתה ואח"כ נוהג שבעת ימי אבילות','Wedding week precedes mourning week.'),('וכל אותן הימים הוא ישן בין האנשים ואשתו ישנה בין הנשים','Separate supervised sleeping during those days.')],1):
 add('repeat'+str(n),'4a:5','repeated_rule','anonymous baraita',quote,meaning,'Prepared feast, water on meat, groom father or bride mother died.')
edges=[]
def edge(a,b,t):edges.append(dict(source=a,target=b,type=t,evidence=next(c['evidence'] for c in claims if c['id']==a)))
for a,b,t in [
 ('c02','c01','supports'),('q01','c01','challenges'),('c03','q01','answers'),('q03','h01','rejects'),('c10','q02','answers'),('q04','c10','challenges'),('c11','q04','answers'),('c12','q05','answers'),('c13','q05','answers'),('c14','c15','supports'),('c15','q06','answers'),('q07','c04','challenges'),('c16','q07','answers'),('q09','h02','rejects'),('q10','h02','rejects'),('c17','q08','answers'),('q11','c17','challenges'),('c18','q11','answers'),('q12','c18','challenges'),('c19','q12','answers'),('c20','q08','alternative_answer'),('x03','xq01','answers'),('x04','xq02','answers'),('x09','c21','qualifies'),('x11','c21','qualifies'),('x13','x11','qualifies'),('x14','x11','qualifies'),('x15','xq03','answers'),('x16','x11','supports'),('x07','x20','supports'),('xq04','x22','challenges'),('x23','xq04','answers'),('x24','xq05','answers'),('x28','xq06','challenges_inference'),('x29','x28','reconciles'),('x30','xq07','answers'),('x34','x29','challenges'),('x35','x34','reconciles'),('x38','x37','supports'),('x40','xq06','alternative_reconciliation'),('x41','xh01','rejects'),('x42','x41','supports'),('x43','x41','supports'),('x44','xq08','answers'),('x46','xq09','initial_answer'),('xq10','x46','challenges'),('x47','xq10','supports'),('x48','xq10','supports'),('x49','xq10','supports'),('x50','xq10','supports'),('x51','xq10','supports'),('x52','xq10','supports'),('x53','xq10','supports'),('x54','x46','replaces'),('xq11','x54','challenges'),('x55','xq11','answers'),('x56','xq11','alternative_answer'),('x57','x54','extends')]:edge(a,b,t)
core=[f'3b:{j}' for j in range(1,10)]
context=[f'3a:{j}' for j in range(12,15)]+[f'4a:{j}' for j in range(1,11)]+[f'4b:{j}' for j in range(1,13)]+[f'5a:{j}' for j in range(1,6)]
units=[
 dict(id='u1',start='3a:12',end='3b:1',topic='Wedding day, court schedule and preparation',note='3b:1 begins backward explanatory question מאי שקדו; baraita runs onward. Preparatory requirement is not a named dispute.'),
 dict(id='u2',start='3b:2',end='3b:6',topic='Danger and Tuesday custom',note='3b:2 is composite: Monday compulsion and Sabbath clause are subsequently resumed separately. No whole-segment exclusive semantic ownership asserted.'),
 dict(id='u3',start='3b:7',end='3b:8',topic='Monday compulsion: military arrival',note='Rava differs in name and explanatory target from Rabbah in 3b:4.'),
 dict(id='u4',start='3b:9',end='4b:10',topic='Alternative compulsion: prepared wedding and bereavement',note='Cross-page baraita and mourning/menstruation continuations essential; internal subunits on meat sale 4a:2–5 and separate sleeping 4a:7–4b:10.'),
 dict(id='u5',start='4b:11',end='5a:5',topic='Resumed Sabbath eve and Saturday-night restriction',note='Resumes 4a:6 and ultimately 3b:2. 4b:12 speaker and 5a:1 content are one utterance. 5a:6 opens a different explicit question; read as stop sentinel.')]
comparability=[
 dict(question='q02',alternatives=['h01','c10'],status='hypothesis rejected, not two maintained named opinions'),
 dict(question='q08',alternatives=['c17','c20'],status='two alternative explanations of same clause; only first attributed to Rava'),
 dict(question='meat resale',alternatives=['x11','x13','x14','x15'],status='contextual locality distinctions; not unconditional contradiction'),
 dict(question='relative mourning/menstruation stringency',alternatives=['x29','x39','x40'],status='anonymous husband/wife distinction versus Rav Ashi special-case distinction; no automatic rejection of former asserted'),
 dict(question='mourning onset',alternatives=['x42','x43'],status='comparable differing timing, cited to reject supposed leniency; not this sugya practical adjudication'),
 dict(question='q09',alternatives=['x46','x54'],status='same Rabbi Zeira replaces his initial reason; not two enduring personal positions'),
 dict(question='q11',alternatives=['x55','x56'],status='anonymous alternative reconciliations')]
uncertainties=[
 'Requested Ketubot 3b:10 is absent: raw page index 5 has nine segments. No invented segment or substitution of 4a:1.',
 'Rabbah (רבה) at 3b:4 explains danger; Rava (רבא) at 3b:8 explains compulsion. Their neighboring appearances are not evidence of a pairwise disagreement.',
 'Anonymous give-and-take following named statements is not automatically attributed to the last named speaker.',
 'דאונס שרי and כהנות in 3b:5 are terse. No imported commentary used to expand exact permission, identity or legal consequences; likely implications remain explanatory inference, not explicit claims.',
 'אספרווא at 3b:8 is represented conservatively as advance personnel, without asserting a lexical identification unsupported by this source.',
 '3b:9 alternatives continue onto 4a and 4b: isolated 3b reading would lose consummation, postponement, parental/financial conditions, supervision and qualifications.',
 'The husband/wife mourning distinction at 4b:4–7 contains scope revisions. Do not flatten the initial analogy or apply Rava menstruation qualification to bereavement.',
 '4b:9 timing alternatives are attributed citations, not an independently adjudicated halachic conclusion.',
 'The first Rabbi Zeira rationale (4b:12–5a:1) is superseded at 5a:4; 5a:5 extends slaughter concern to Sabbath eve without an explicit denial of wound concern.',
 'No human certification; one source-only AI reading, no producer comparison or full required tractate review. Atomicity and structure are reviewer analytical choices.'
]
out=dict(schema='independent_source_reading.custom.v1',created='2026-11-26',job='L01',review_scope='Ketubot 3b:1–9 with continuations',cohort='targeted_continuation_not_probability_sample',exposure=dict(source_only=True,statement='Fresh assigned context; inspected original pinned source, AGENTS.md, general AGENT_HANDOFF.md, INDEPENDENT_REVIEW_PROMPT.md, QA_AND_RELEASE.md and neutral assignment/source-coordinate messages only. No producer proposals, snapshots, labels, comparisons, generated reader or parent history inspected.',human_certification=False,producer_comparison_performed=False),source=dict(path=str(source),sha256=h,metadata={k:v for k,v in d.items() if k!='text'},offset_basis='original Python Unicode codepoints, zero-based half-open; markup preserved; no normalization',reference_mapping='i//2+1, a if even i else b; j+1'),requested_core='Ketubot 3b:1–10',absent_requested_refs=['Ketubot 3b:10'],core=[ev(r) for r in core],context=[ev(r) for r in context],stop_sentinel=ev('5a:6'),additional_source_read_disclosure='Original source 3a:1 through 5a:14 displayed and read for orientation. Formal contextual inventory limited to listed 30 segments; surrounding orientation is not core coverage.',units=units,claims=claims,argument_relations=edges,answer_comparability=comparability,uncertainties=uncertainties,eligibility=dict(ml_eligible=False,reason='Independent first reading only; no exact-version comparison/adjudication or task qualification'),omission_baseline=dict(definition='All independently identified core atomic claims and questions listed here; no worker-row denominator and no omission rate before comparison.',core_claim_ids=[c['id'] for c in claims if c['cohort']=='core' and c['kind'] not in ['question','objection']],core_question_ids=[c['id'] for c in claims if c['cohort']=='core' and c['kind'] in ['question','objection']],note='Context inventory includes repeated occurrences and key qualifications; no assertion of exhaustive whole-tractate extraction. Composite preparation reasons retained as single rationale, enumerated conditions explicitly.'),counts=dict(core_segments=len(core),context_segments=len(context),core_codepoints=sum(len(get(r)[2]) for r in core),context_codepoints=sum(len(get(r)[2]) for r in context),atomic_records=len(claims),core_atomic_records=sum(c['cohort']=='core' for c in claims),context_atomic_records=sum(c['cohort']=='context' for c in claims),supported_edges=len(edges),independent_units=len(units),answer_comparability_sets=len(comparability)),validation={})
def walk(x):
 if isinstance(x,dict):
  if all(k in x for k in ['ref','start','end','quote','raw_page_index','raw_segment_index']):
   s=d['text'][x['raw_page_index']][x['raw_segment_index']];assert s[x['start']:x['end']]==x['quote'];return 1
  return sum(walk(v) for v in x.values())
 if isinstance(x,list):return sum(walk(v) for v in x)
 return 0
ids={c['id'] for c in claims};assert len(ids)==len(claims)
assert all(e['source'] in ids and e['target'] in ids for e in edges)
out['validation']=dict(evidence_spans_exact=walk(out),claim_ids_unique=True,edge_endpoints_valid=True,source_hash_verified=True)
target=root/'ketubot_3b1_10.json'
assert not target.exists(),'Frozen artifact already exists; no overwriting'
target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
digest=hashlib.sha256(target.read_bytes()).hexdigest()
(root/'ketubot_3b1_10.sha256').write_text(digest+'  ketubot_3b1_10.json\n',encoding='ascii')
print(json.dumps(dict(path=str(target),sha256=digest,counts=out['counts'],validation=out['validation']),indent=2))
