"""Manual substitute expressions, lexical ambiguity, and competing explanations."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r010.';a.OUTPUT='continuation_010.json'
c=a.c;q=a.q;e=a.edge
scope=['10a:'+str(i) for i in range(11,15)]+['10b:'+str(i) for i in range(1,12)]
a.structure('substitutes',scope,'Substitute expressions, their origin, secondary substitutes, and unresolved lexical forms')
off=c('off','10a:11','קונם קונח קונס הרי אלו כינויין לקרבן','קונם, קונח and קונס are substitutes for offering language.',composition='composite',scope='Mishnah’s three-item lexical category')
herem=c('herem','10a:11','חרק חרך חרף הרי אלו כינויין לחרם','חרק, חרך and חרף are substitutes for herem language.',composition='composite',scope='Mishnah’s three-item category')
naz=c('naz','10a:11','נזיק נזיח פזיח הרי אלו כינויין לנזירות','נזיק, נזיח and פזיח are substitutes for nazirite language.',composition='composite',scope='Mishnah category; exact printed spellings preserved')
oath=c('oath','10a:11','שבותה שקוקה נודר במוהי הרי אלו כינויין לשבועה:','שבותה, שקוקה and נודר במוהי are listed as oath substitutes.',composition='composite',scope='Mishnah list; במוהי qualified at10b:11')
yohanan=c('yohanan','10a:12','רבי יוחנן אמר לשון אומות הן','Rabbi Yohanan says these substitutes are languages of the nations.',holder='רבי יוחנן',scope='Account of their origin')
lakish=c('lakish','10a:12','רבי שמעון בן לקיש אמר לשון שבדו להם חכמים להיות נודר בו','Rabbi Shimon ben Lakish says the sages devised these expressions for vowing.',holder='רבי שמעון בן לקיש',scope='Alternative account')
invent=c('invent','10a:12','וכן הוא אומר בחדש אשר בדא מלבו','The discussion cites בחדש אשר בדא מלבו for the language of devising.',scope='Lexical citation following Lakish, not evidence of contemporary language history')
e('invent.support',invent,lakish,'support','10a:12')
why=q('why','10a:13','וטעמא מאי תקינו רבנן כינויין','Why did the sages institute substitute expressions?')
avoid=c('avoid','10a:13','דלא לימא קרבן','To avoid saying קרבן.',scope='Initial answer in the staged explanation')
whyoffer=q('whyoffer','10a:13',('ולימא קרבן',0),'Why not simply say קרבן?')
name=c('name','10a:13',"דילמא אמר קרבן לה'",'He might say קרבן לה׳.',mode='hypothetical',scope='First risk in the staged rationale')
whyname=q('whyname','10a:13',"ולימא קרבן לה'",'Why not say קרבן לה׳?')
empty=c('empty','10a:13',"דילמא אמר לה' ולא אמר קרבן וקא מפיק שם שמים לבטלה",'He might utter לה׳ without completing קרבן, thereby uttering the divine name in vain.',mode='hypothetical',composition='composite',scope='Explicit feared sequence supporting substitute expressions')
e('avoid.answer',avoid,why,'answer','10a:13');e('name.answer',name,whyoffer,'answer','10a:13');e('empty.answer',empty,whyname,'answer','10a:13')
order=c('order','10a:14',None,'Rabbi Shimon teaches not to place לה׳ before the offering names עולה, מנחה, תודה or שלמים, deriving the order from קרבן לה׳.',holder='רבי שמעון',extra=[('10b:1',None)],composition='composite',scope='Cross-page quotation with four explicitly listed offering formulations')
stronger=c('stronger','10b:2',None,'If even intended sacrificial mention requires placing קרבן first, purposeless divine-name utterance is all the more excluded.',scope='Baraita’s explicit a-fortiori argument',composition='composite')
e('order.support',order,empty,'support','10b:1');e('stronger.support',stronger,empty,'support','10b:2')
parallel=q('parallel','10b:3','לימא כתנאי','Does the origin dispute parallel a tannaitic dispute?')
shammai=c('shammai','10b:3','בית שמאי אומרים כינויי כינויין אסורין','Beit Shammai hold secondary substitutes prohibitory.',holder='בית שמאי',conditions=['כינויי כינויין'],scope='Quoted tannaitic rule')
hillel=c('hillel','10b:3','ובית הלל אומרים כינויי כינויין מותרין','Beit Hillel hold secondary substitutes permitted.',holder='בית הלל',conditions=['כינויי כינויין'],scope='Quoted contrasting rule')
map1=c('map1','10b:4','מאי לאו מאן דאמר כינויי כינויין אסורין קסבר (כינויי) כינויין לשון אומות הן,','The proposed alignment makes the restrictive school treat substitutes as foreign languages.',mode='rejected',scope='Suggested explanation, not final identification')
map2=c('map2','10b:4','ולמאן דאמר מותרים קסבר לשון שבדו להן חכמים','The permissive school would then treat substitutes as language devised by the sages.',mode='rejected',scope='Second branch of proposed alignment')
shared=c('shared','10b:5','לא דכולי עלמא כינויין לשון אומות הן','The first reply allows both schools to hold that substitutes are foreign-language expressions.',scope='Alternative explanation of tannaitic dispute, not a global resolution of Yohanan/Lakish')
used=c('used','10b:5','ובית שמאי סברי בהני נמי משתעי אומות','Beit Shammai then regard the secondary expressions as also spoken by the nations.',holder='בית שמאי',scope='First alternative reconstruction of rationale')
unused=c('unused','10b:5','ובית הלל סברי בהני לא משתעי אומות','Beit Hillel then regard those secondary forms as not spoken by the nations.',holder='בית הלל',scope='Same alternative reconstruction')
e('shared.correction',shared,map1,'correction','10b:5');e('shared.correction2',shared,map2,'correction','10b:5');e('used.support',used,shammai,'support','10b:5');e('unused.support',unused,hillel,'support','10b:5')
decree=c('decree','10b:6','ואיבעית אימא בית שמאי סברי גזרינן כינויי כינויין משום כינויין','Alternatively Beit Shammai impose a decree on secondary substitutes because of primary substitutes.',holder='בית שמאי',scope='Second alternative explanation, not combined with first as one certain motive')
nodecree=c('nodecree','10b:6','ובית הלל סברי לא גזרינן כינויי כינויין משום כינויין','Beit Hillel do not impose that decree.',holder='בית הלל',scope='Second alternative explanation')
e('decree.support',decree,shammai,'support','10b:6');e('nodecree.support',nodecree,hillel,'support','10b:6')
formsq=q('formsq','10b:7','היכי דמי כינויי כינויין דנדרים','What are secondary substitutes for vows?')
forms=c('forms','10b:7','תני רב יוסף מקנמנא מקנחנא מקנסנא','Rav Yosef recites מקנמנא, מקנחנא and מקנסנא as the secondary vow forms.',holder='רב יוסף',composition='composite',scope='Teacher of lexical list; no claim he originated the forms')
hq=q('hq','10b:7','היכי דמי כינויי כינויין דחרם','What are secondary substitutes for herem?')
hforms=c('hforms','10b:7','תני מפשאה חרקים חרכים חרפים','The text reports מפשאה reciting חרקים, חרכים and חרפים.',holder='מפשאה',composition='composite',scope='Printed teacher label retained; historical identity unresolved')
nforms=c('nforms','10b:7','כינויי כינויין דנזירות תני רב יוסף מחזקנא מנזחנא מפיחנא','Rav Yosef recites מחזקנא, מנזחנא and מפיחנא as secondary nazirite forms.',holder='רב יוסף',composition='composite',scope='Exact lexical list, no normalization to nearby variants')
e('forms.answer',forms,formsq,'answer','10b:7');e('hforms.answer',hforms,hq,'answer','10b:7')
q('mif','10b:8','איבעיא להו מיפחזנא מאי','What is the status of מיפחזנא?')
q('mit','10b:8','מיתחזנא מאי','What is the status of מיתחזנא?')
q('miz','10b:8','מיתעזנא מאי','What is the status of מיתעזנא?')
kin=q('kin','10b:8','אמר ליה רבינא לרב אשי קינמא (קינמא) מאי קונם קאמר, או דילמא קינמן בשם קאמר','Ravina asks Rav Ashi whether קינמא means קונם or the spice cinnamon.',voice='רבינא')
kin2=q('kin2','10b:9','אמר ליה רב אחא בריה דרב חייא לרב אשי קינה מאי קינה של תרנגולין קאמר או דילמא לשון דקונם','Rav Aha son of Rav Hiyya asks Rav Ashi whether קינה means a hen’s nest or a form of קונם.',voice='רב אחא בריה דרב חייא')
unresolved=c('unresolved','10b:9','תיבעי','The question is left unresolved.',mode='unresolved',scope='Explicit ending of קינה question; earlier lexical questions have no supplied answer here')
oq=q('oq','10b:10','כינויי כינויין דשבועה היכי דמי','What are secondary oath substitutes?')
olist=c('olist','10b:10','שבואל שבותיאל שקוקאל','The initial list offers שבואל, שבותיאל and שקוקאל.',mode='challenged',composition='composite',scope='Initial reading; first item corrected next')
person=c('person','10b:10','שבואל שבואל בן גרשום משמע','The objection reads שבואל as the personal name Shvuel son of Gershom.',scope='Lexical objection, not a vow-holder identity claim')
amend=q('amend','10b:10','אלא שבובאל שבותיאל שקוקאל מהו','Instead, what is the status of שבובאל, שבותיאל and שקוקאל?')
e('olist.answer',olist,oq,'answer','10b:10');e('person.objection',person,olist,'objection','10b:10')
for key,quote,form in [('ashiv','אמר שמואל אמר אשיבתא לא אמר כלום','אשיבתא'),('ashik','אשקיקא לא אמר כלום','אשקיקא'),('karin','קרינשא לא אמר כלום','קרינשא')]:
    c(key,'10b:10',quote,'Shmuel says '+form+' has no effect.',holder='שמואל',conditions=[form],scope='Named ruling on this particular form; do not silently equate with every previously queried form')
bare=c('bare','10b:11','תניא רבן שמעון בן גמליאל אומר האומר במוהי לא אמר כלום','Rabban Shimon ben Gamliel says bare במוהי has no effect.',holder='רבן שמעון בן גמליאל',conditions=['במוהי alone'],scope='Qualification of Mishnah formula')
full=c('full','10b:11','במומתא דאמר מוהי הרי אלו כינויין לשבועה:','במומתא דאמר מוהי is an oath substitute.',holder='רבן שמעון בן גמליאל',conditions=['full specified expression'],scope='Positive qualification, preserving exact source words')
e('bare.qualification',bare,oath,'qualification','10b:11');e('full.distinction',full,bare,'distinction','10b:11')
a.notes={
'10a:11':'Reread four lexical categories and every listed form; grouped lists explicitly composite.',
'10a:12':'Reread Yohanan/Lakish origin accounts and biblical lexical citation.',
'10a:13':'Reread all three staged questions and answers culminating in incomplete divine-name utterance risk.',
'10a:14':'Reread Rabbi Shimon introduction jointly with10b:1.',
'10b:1':'Reread four offering formulations and prescribed name order; no missing cross-page attribution.',
'10b:2':'Reread explicit a-fortiori argument about purposeless utterance.',
'10b:3':'Reread tannaitic-comparison question and both schools’ positions.',
'10b:4':'Reread tentative two-branch origin alignment as rejected.',
'10b:5':'Reread shared-language explanation and distinct lexical-usage accounts.',
'10b:6':'Reread alternative decree/nondecree account; alternatives not conflated.',
'10b:7':'Reread all nine lexical forms, two questions and printed teacher labels; no external identity guess for מפשאה.',
'10b:8':'Reread three separate unresolved forms and Ravina’s קונם/cinnamon question.',
'10b:9':'Reread Rav Aha son of Rav Hiyya’s hen-nest/קונם question and unresolved ending.',
'10b:10':'Reread initial list, personal-name objection, amended open question and three distinct Shmuel rulings.',
'10b:11':'Reread bare/full במוהי contrast and Rabban Shimon ben Gamliel attribution.'}
if __name__=='__main__':a.save()
