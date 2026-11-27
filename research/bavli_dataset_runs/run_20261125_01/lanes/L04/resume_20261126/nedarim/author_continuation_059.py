"""Manual bed-construction proof sequence and city/house boundary reading."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r059.';a.OUTPUT='continuation_059.json'
c=a.c;e=a.edge;q=b.q
a.structure('bed',['56a:5','56a:6','56a:7']+['56b:'+str(i) for i in range(1,6)],'Dargesh definition, successive objections and mourning rules')
a.structure('boundary',['56b:'+str(i) for i in range(6,11)],'City extension and house threshold boundary proofs')
meir=c('meir','56a:5','הנודר מן המטה מותר בדרגש דברי רבי מאיר','Rabbi Meir permits a דרגש under a bed vow.',holder='רבי מאיר',scope='Category distinction before object definition')
sages=c('sages','56a:5','וחכ"א דרגש בכלל מטה','The sages include דרגש in the bed category.',holder='חכמים',scope='Explicit contrary inclusion')
reverse=c('reverse','56a:5','הנודר מן הדרגש מותר במטה','A דרגש vow permits an ordinary bed.',scope='Reverse category direction')
e('sages.objection',sages,meir,'objection','56a:5')
what=q('what','56a:6','מאי דרגש','What is a דרגש?')
ulla=c('ulla','56a:6','אמר עולא ערסא דגדא','Ulla identifies it as ערסא דגדא, a bed associated with fortune.',holder='עולא',mode='rejected',scope='Initial definition survives first two objections but fails strap objection56b2')
king=c('king','56a:6','הא דתנן כשהן מברין אותו כל העם מסובין על הארץ והוא מיסב על הדרגש','The cited mourning meal rule seats everyone on the ground while he reclines on the דרגש.',scope='Quoted rule; referent is not named inside this local quotation')
yearq=q('yearq','56a:6','כולה שתא לא יתיב עלה ההוא יומא יתיב עלה','The sages ask Ulla why someone who never sits on it during the year would do so on that day.')
ravina=c('ravina','56a:6','מתקיף לה רבינא מידי דהוה אבשר ויין דכולה שתא אי בעי אכיל ואי בעי לא אכיל ההוא יומא אנן יהבינן ליה','Ravina counters by analogy to meat and wine: optional during the year, supplied to him on that day.',holder='רבינא',composition='composite',scope='Deflects first objection to Ulla rather than endorsing his definition permanently')
e('ulla.answer',ulla,what,'answer','56a:6');e('ravina.answer',ravina,yearq,'answer','56a:6')
upright=c('upright','56a:7','דתניא דרגש לא היה כופהו אלא זוקפו','A baraita says the דרגש is stood upright rather than overturned.',scope='Mourning treatment used in second objection')
allbeds=c('allbeds','56a:7','והתניא הכופה את מטתו לא מטתו בלבד הוא כופה אלא כל מטות שיש לו בתוך הבית הוא כופה','Another baraita requires overturning all beds in the house, not only one’s own bed.',scope='General mourning bed rule cited against Ulla')
overturnq=q('overturnq','56a:7','ואי אמרת ערסא דגדא הוא','If it is the fortune bed, why would it escape the requirement applying to all beds?')
objects=c('objects','56b:1','מידי דהוה אמטה המיוחדת לכלים דתניא אם היתה מטה המיוחדת לכלים אין צריך לכפותה','The reply analogizes to a bed dedicated to objects, which need not be overturned.',scope='Cross-folio answer deflecting second objection')
e('objects.answer',objects,overturnq,'answer','56b:1')
straps=c('straps','56b:2','דתניא רשב"ג אומר דרגש מתיר קרביטיו והוא נופל מאליו','Rabban Shimon ben Gamliel says to loosen the דרגש straps so it falls by itself.',holder='רשב"ג',scope='Third proof text, later explicit ruling follows it')
strapq=q('strapq','56b:2','ואי דרגש ערסא דגדא הוא קרביטין מי אית ליה','If the דרגש is a fortune bed, does it have these straps?')
leather=c('leather','56b:2','כי אתא רבין אמר שאילתיה לההוא מרבנן ורב תחליפא בר מערבא שמיה דהוה שכיח בשוקא דצלעי ואמר לי מאי דרגש ערסא דצלא','Ravin reports asking Rav Tahlifa bar Maarava, familiar with the leather market, who defines דרגש as a leather bed.',holder='רב תחליפא בר מערבא',composition='composite',scope='Named expert, market context and definition transmitted by Ravin')
e('straps.objection',straps,ulla,'objection','56b:2');e('leather.answer',leather,strapq,'answer','56b:2');e('leather.answerwhat',leather,what,'answer','56b:2');e('leather.correction',leather,ulla,'correction','56b:2')
howq=q('howq','56b:3','איתמר איזהו מטה ואיזהו דרגש','How are an ordinary bed and a דרגש distinguished?')
yirmeya=c('yirmeya','56b:3','אמר רבי ירמיה מטה מסרגין אותה על גבה דרגש מסרגין אותו מגופו','Rabbi Yirmeya says a bed is woven over its top and a דרגש through its frame.',holder='רבי ירמיה',mode='rejected',composition='composite',scope='Initial construction distinction corrected in next segment')
smooth=c('smooth','56b:3','מיתיבי כלי עץ מאימתי מקבלין טומאה המטה והעריסה משישופם בעור הדג','The objection cites wooden beds and cradles becoming susceptible to impurity after smoothing with fish skin.',scope='Cited completion criterion for vessels')
smoothq=q('smoothq','56b:3','ואי מטה מסתרגת על גבה למה לי שיפת עור הדג','If the bed is woven over its top, why smooth it with fish skin?')
through=c('through','56b:4','אלא הא והא מגופן מטה אעולי ואפוקי בבזיני דרגש אעולי ואפוקי באבקתא','The correction weaves both through their frames: the bed through holes and the דרגש through loops.',composition='composite',scope='Explicit replacement distinction with both attachment methods')
e('yirmeya.answer',yirmeya,howq,'answer','56b:3');e('through.answer',through,howq,'answer','56b:4');e('through.answerob',through,smoothq,'answer','56b:4');e('through.correction',through,yirmeya,'correction','56b:4')
posts=c('posts','56b:5','א"ר יעקב בר אחא אמר רבי מטה שנקליטיה יוצאין זוקפה ודיו','Rabbi Yaakov bar Aha reports Rabbi that a bed with projecting posts may simply be stood upright.',holder='רבי',scope='Explicit transmission and exceptional mourning treatment')
halakha=c('halakha','56b:5','א"ר יעקב בר אידי אמר ר\' יהושע בן לוי הלכה כרשב"ג','Rabbi Yaakov bar Idi reports Rabbi Yehoshua ben Levi that the halakha follows Rabban Shimon ben Gamliel.',holder="ר' יהושע בן לוי",scope='Explicit ruling on the preceding דרגש strap procedure')
e('halakha.support',halakha,straps,'support','56b:5')
city=c('city','56b:6','הנודר מן העיר מותר ליכנס לתחומה של עיר ואסור ליכנס לעיבורה','A city vow permits entering its outlying limit but prohibits entering its adjoining extension.',composition='composite',scope='תחום versus עיבור boundary distinction')
house=c('house','56b:6','אבל הנודר מן הבית אסור מן האגף ולפנים','A house vow prohibits entry from the door-stop inward.',scope='Precise האגף boundary retained; no numeric distance invented')
cityq=q('cityq','56b:7','מנלן דעיבורא דמתא כמתא דמי','How do we know a city’s extension counts as the city?')
yohanan=c('yohanan','56b:7','א"ר יוחנן דאמר קרא (יהושע ה, יג) ויהי בהיות יהושע ביריחו וגו\'','Rabbi Yohanan cites Joshua being in Jericho.',holder='רבי יוחנן',scope='Scriptural support for inclusion of adjoining extension')
literalq=q('literalq','56b:7','מאי ביריחו אילימא ביריחו ממש והכתיב (יהושע ו, א) ויריחו סוגרת ומסוגרת','How could Joshua literally be in Jericho when the city was shut tight?')
extension=c('extension','56b:7','אלא ש"מ בעיבורה','The deduction places him in its adjoining extension.',scope='Explicit local inference from two verses')
limitq=q('limitq','56b:8','אימא אפי\' בתחומה','Why not include even the city’s outlying limit?')
outside=c('outside','56b:8','הא כתיב בתחומה (במדבר לה, ה) ומדותם מחוץ לעיר','The reply cites measuring the limit outside the city.',scope='Textual exclusion of תחום while retaining עיבור inclusion')
e('yohanan.answer',yohanan,cityq,'answer','56b:7');e('extension.answer',extension,literalq,'answer','56b:7');e('outside.answer',outside,limitq,'answer','56b:8')
threshold=c('threshold','56b:9','הנודר מן הבית אינו אסור אלא מן האגף ולפנים: אבל מן האגף ולחוץ לא','The discussion repeats that only inward of the door-stop is prohibited, implying the outside is permitted.',composition='composite',scope='Repeated lemma and explicit inference')
priestq=q('priestq','56b:9','מתיב רב מרי (ויקרא יד, לח) ויצא הכהן מן הבית','Rav Mari challenges from the priest’s instruction to leave the afflicted house.',voice='רב מרי')
home=c('home','56b:9','יכול ילך לביתו ויסגיר ת"ל (ויקרא יד, לח) אל פתח הבית','The baraita rejects going to his own home before closing it because the verse specifies the house entrance.',mode='rejected',scope='Rejected proposed initial procedure, contrasted with later validity despite deviation')
lintel=c('lintel','56b:9','אי אל פתח הבית יכול יעמוד תחת המשקוף ויסגיר תלמוד לומר מן הבית עד שיצא מן הבית כולו','It also rejects standing beneath the lintel initially: leaving the house means leaving it entirely.',mode='rejected',scope='Rejected initial-position proposal; reason explicitly broadens exit requirement')
proper=c('proper','56b:10','הא כיצד עומד בצד המשקוף ויסגיר','The prescribed position is beside the lintel while closing the house.',scope='Baraita’s affirmative procedural answer')
validq=q('validq','56b:10','ומנין שאם הלך לביתו והסגיר או שעמד תחת השקוף והסגיר שהסגירו מוסגר','How do we know closure nevertheless works if he went home or stood under the lintel?')
valid=c('valid','56b:10','ת"ל (ויקרא יד, לח) והסגיר את הבית מכל מקום','The phrase and he shall close the house establishes validity regardless of those positions.',scope='After-the-fact validity, not permission to ignore initial procedure')
special=c('special','56b:10','שאני גבי בית דכתיב מן הבית עד שיצא מן הבית כולו','The answer distinguishes this house-purity passage: its wording requires exiting the entire house.',scope='Deflects Rav Mari’s challenge to ordinary vow boundary by special scriptural wording')
e('valid.answer',valid,validq,'answer','56b:10');e('special.answer',special,priestq,'answer','56b:10')
a.notes={
'56a:5':'Reread Meir/sages bed-dargesh dispute and reverse permission.',
'56a:6':'Reread Ulla definition, mourning-meal proof, annual-use objection and Ravina meat/wine deflection.',
'56a:7':'Reread upright rule, all-beds overturning rule and second objection continued next folio.',
'56b:1':'Reread object-dedicated-bed exemption as second objection deflection.',
'56b:2':'Reread Gamliel strap rule, decisive strap objection and Ravin/Tahlifa leather-market definition with full transmission.',
'56b:3':'Reread Yirmeya initial weaving distinction, fish-skin completion criterion and objection.',
'56b:4':'Reread explicit both-through-frame correction and holes/loops distinction.',
'56b:5':'Reread both Yaakov transmissions separately: projecting-post exception and Yehoshua ben Levi ruling for Gamliel.',
'56b:6':'Reread city limit/extension distinction and house door-stop boundary.',
'56b:7':'Reread Yohanan Joshua proof, closed-Jericho obstacle and extension inference.',
'56b:8':'Reread outlying-limit challenge and outside-the-city verse answer.',
'56b:9':'Reread repeated house lemma, Mari objection and both rejected initial priest positions with verses.',
'56b:10':'Reread proper beside-lintel position, both after-the-fact cases and validity verse, then special-exit wording deflection.'}
if __name__=='__main__':a.save()
