"""Source reading: gatehouses, city defenses, residence and alternate assessment reports."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('bava_batra','Bava Batra','bb.r018');c=a.claim;q=a.question;e=a.e
parent='d7718564bcfd1a78624e7f6ba879dc9cc45d38ce0775704567ab5e8718813d89'
assert r.sha(r.encoded(r.current(a.job)))==parent
a.structure('mishnah',['7b:6','7b:7'],'Courtyard and city infrastructure obligations and resident status')
a.structure('gatehouse',['7b:8','7b:9'],'Gatehouse praise challenged by the pious man and Elijah narrative; alternative reconciliations')
a.structure('defense',['7b:10','7b:11'],'Rabban Shimon ben Gamliel and sages on qualifying courtyards and towns')
a.structure('assessment',['7b:12','7b:13'],'Two report versions of Rabbi Elazar asking Rabbi Yohanan about assessment')
gate=c('gate','7b:6','כופין אותו לבנות בית שער ודלת לחצר','A courtyard member is compelled to contribute to a gatehouse and door.',conditions=['shared courtyard member'],scope='Anonymous Mishnah',composition='composite')
rsggate=c('rsg_gate','7b:6','רבן שמעון בן גמליאל אומר לא כל החצרות ראויות לבית שער','Rabban Shimon ben Gamliel says not every courtyard is suitable for a gatehouse.',candidates=['רבן שמעון בן גמליאל'])
city=c('city','7b:6','כופין אותו לבנות לעיר חומה ודלתים ובריח','A city member is compelled to contribute to a wall, gates and bar.',conditions=['city membership'],scope='Anonymous Mishnah',composition='composite')
rsgcity=c('rsg_city','7b:6','רשב"ג אומר לא כל העיירות ראויות לחומה','Rabban Shimon ben Gamliel says not every town is suitable for a wall.',candidates=['רשב"ג'])
e('gate_distinction',rsggate,gate,'distinction','7b:6');e('city_distinction',rsgcity,city,'distinction','7b:6')
resq=q('residence_q','7b:7','כמה יהא בעיר ויהא כאנשי העיר','How long must one reside in the city to be considered a city member?')
year=c('year','7b:7','י"ב חדש','Twelve months of residence confer the stated city membership.',conditions=['residence in the city'])
house=c('house','7b:7','קנה בה בית דירה הרי הוא כאנשי העיר מיד','Purchasing a dwelling in the city confers membership immediately.',conditions=['purchased a dwelling in the city'])
e('year_answer',year,resq,'answer','7b:7');e('house_qualification',house,year,'qualification','7b:7')
goodq=q('good_q','7b:8','למימרא דבית שער מעליותא היא','Does the Mishnah imply that a gatehouse is beneficial?')
visits=c('visits','7b:8','והא ההוא חסידא דהוה רגיל אליהו דהוה משתעי בהדיה','Elijah regularly spoke with a certain pious man.',scope='Narrative report; no independent historical verification')
built=c('built','7b:8','עבד בית שער','The pious man built a gatehouse.',scope='Narrative event')
ceased=c('ceased','7b:8','ותו לא משתעי בהדיה','Afterward Elijah no longer spoke with him.',scope='Narrative sequence as objection to gatehouse benefit; no additional motive invented')
e('ceased_objection',ceased,goodq,'objection','7b:8')
location=c('location','7b:8','לא קשיא הא מגואי הא מבראי','The first reconciliation distinguishes a gatehouse inside from one outside.',conditions=['inside versus outside location'],composition='composite',scope='Anonymous reconciliation; short הא/הא wording retained without assigning its members by order',uncertainty=['Source does not explicitly label which הא refers to which preceding case.'])
door=c('door','7b:9','הא והא מבראי ולא קשיא הא דאית ליה דלת הא דלית ליה דלת','An alternative places both outside and distinguishes having a door from lacking a door.',conditions=['both gatehouses outside','door present versus absent'],composition='composite',uncertainty=['Alternative reconciliation, not an additional universal rule; source case allocation not forced by order.'])
lock=c('lock','7b:9','הא והא דאית ליה דלת ולא קשיא הא דאית ליה פותחת הא דלית ליה פותחת','Another alternative gives both a door and distinguishes having a פותחת from lacking it.',conditions=['both have a door','פותחת present versus absent'],composition='composite',uncertainty=['Retain printed hardware term פותחת without imposing unverified apparatus detail.'])
lockside=c('lockside','7b:9','הא והא דאית ליה פותחת ולא קשיא הא דפותחת דידיה מגואי הא דפותחת דידיה מבראי','Another alternative gives both a פותחת and distinguishes whether it is inside or outside.',conditions=['both have פותחת','inside versus outside placement'],composition='composite')
for i,x in enumerate([location,door,lock,lockside]):e('reconciliation'+str(i),x,goodq,'answer','7b:8' if i==0 else '7b:9')
near=c('near','7b:10','חצר הסמוכה לרשות הרבים ראויה לבית שער','Rabban Shimon ben Gamliel considers a courtyard adjoining the public domain suitable for a gatehouse.',candidates=['רבן שמעון בן גמליאל'],conditions=['courtyard adjoins public domain'],scope='Baraita explaining Mishnah restriction')
far=c('far','7b:10','ושאינה סמוכה לרשות הרבים אינה ראויה לבית שער','He considers a courtyard not adjoining the public domain unsuitable for a gatehouse.',candidates=['רבן שמעון בן גמליאל'],conditions=['courtyard does not adjoin public domain'])
crowd=c('crowd','7b:10','ורבנן זימנין דדחקי בני רשות הרבים ועיילו ואתו','The sages respond that people from the public domain sometimes press inward and enter.',candidates=['רבנן'],scope='Reason against limiting gatehouse obligation to adjacent courtyards')
e('near_qualification',near,rsggate,'qualification','7b:10');e('far_qualification',far,rsggate,'qualification','7b:10');e('crowd_objection',crowd,far,'objection','7b:10');e('crowd_support',crowd,gate,'support','7b:10')
baraita=c('city_baraita','7b:11','(ת"ר כופין אותו לעשות לעיר דלתים ובריח)','The parenthesized baraita compels contribution to city gates and bar.',composition='composite',uncertainty=['Printed parentheses retained as source formatting; no witness-based emendation.'])
border=c('border','7b:11','עיר הסמוכה לספר ראויה לחומה','Rabban Shimon ben Gamliel considers a town near the border suitable for a wall.',candidates=['רבן שמעון בן גמליאל'],conditions=['town near border'])
inland=c('inland','7b:11','ושאינה סמוכה לספר אינה ראויה לחומה','He considers a town not near the border unsuitable for a wall.',candidates=['רבן שמעון בן גמליאל'],conditions=['town not near border'])
raiders=c('raiders','7b:11','ורבנן זימנין דמקרו ואתי גייסא','The sages respond that an armed band may sometimes arrive.',candidates=['רבנן'],scope='Reason against limiting city-wall obligation to border towns')
e('border_qualification',border,rsgcity,'qualification','7b:11');e('inland_qualification',inland,rsgcity,'qualification','7b:11');e('raiders_objection',raiders,inland,'objection','7b:11');e('raiders_support',raiders,city,'support','7b:11')
wealthq=q('wealth_q','7b:12','כשהן גובין לפי נפשות גובין או דילמא לפי שבח ממון גובין','Rabbi Elazar asks Rabbi Yohanan whether collection follows persons or property value.',candidates=['רבי אלעזר'])
wealth=c('wealth','7b:12','אמר ליה לפי ממון גובין','Rabbi Yohanan answers that assessment follows property.',candidates=['רבי יוחנן'],scope='First report version; no reconciliation with next version imposed')
firm=c('wealth_firm','7b:12','ואלעזר בני קבע בה מסמרות','He instructs Elazar his son to establish this firmly.',candidates=['רבי יוחנן'],scope='Source form of address retained; no genealogical inference')
closeq=q('close_q','7b:13','כשהן גובין לפי קירוב בתים הן גובין או דילמא לפי ממון גובין','In another report, Rabbi Elazar asks Rabbi Yohanan whether assessment follows house proximity or wealth.',candidates=['רבי אלעזר'])
close=c('close','7b:13','אמר ליה לפי קירוב בתים הן גובין','In this report Rabbi Yohanan answers that assessment follows house proximity.',candidates=['רבי יוחנן'],scope='Alternative source report, not a retraction attributed to Rabbi Yohanan')
firm2=c('close_firm','7b:13','ואלעזר בני קבע בה מסמרות','This report likewise has the instruction to Elazar to establish it firmly.',candidates=['רבי יוחנן'],scope='Repeat occurrence in alternate version')
e('wealth_answer',wealth,wealthq,'answer','7b:12');e('close_answer',close,closeq,'answer','7b:13');e('assessment_versions',close,wealth,'distinction','7b:13')
a.rows[-1]['uncertainty']=['Explicit איכא דאמרי distinguishes report versions; not two simultaneously maintained competing views assigned to the same authority.']
for row in a.rows:
    if row['layer']=='questions':row['content']['answer_set_status']='partial'
a.save_window(['7b:'+str(i) for i in range(6,14)],'publicworks018.json','Reread source7b:6–16 with all continuations of gatehouse alternatives and assessment variants. Distinguish narrative from inference, preserve case conditions and source versions; reconciliation is producer reread, not independent review.',parent)
