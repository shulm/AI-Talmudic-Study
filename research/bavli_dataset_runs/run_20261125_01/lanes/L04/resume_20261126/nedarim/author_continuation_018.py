"""Manual uncertain vows and locality; alternative attributions are not silently unified."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r018.';a.OUTPUT='continuation_018.json'
c=a.c;q=a.q;e=a.edge
scope=['18b:'+str(i) for i in range(1,10)]+['19a:'+str(i) for i in range(1,13)]+['19b:'+str(i) for i in range(1,12)]
a.structure('uncertain',scope,'Ambiguous vows, doubtful naziriteship, voluntary and automatic sanctity, and regional usage')
general=c('general','18b:1','סתם נדרים להחמיר ופירושם להקל','The Mishnah treats unspecified vows stringently while their specified interpretation can be lenient.',scope='Heading qualified by subsequent examples')
peace=c('peace','18b:1','כיצד אמר הרי עלי כבשר מליח כיין נסך אם בשל שלמים נדר אסור','For salted-meat or libation-wine language, a sacrificial referent prohibits.',conditions=['stated salted-meat/libation-wine comparison','sacrificial reference'],composition='composite',scope='Printed בשל שלמים category retained')
idol=c('idol','18b:2','אם בשל עבודה זרה נדר מותר','If the reference is to idolatry, the vow comparison is permitted.',conditions=['idolatrous referent'],scope='Continuation of same two expressions')
unspec=c('unspec','18b:2','ואם סתם אסור','If unspecified, that comparison prohibits.',conditions=['unspecified reference'],scope='Same preceding formulas')
heaven=c('heaven','18b:3','הרי עלי כחרם אם כחרם של שמים אסור','כחרם prohibits if referring to a heavenly dedication.',conditions=['חרם של שמים'])
priest=c('priest','18b:3','ואם כחרם של כהנים מותר','A priestly herem reference is permitted.',conditions=['חרם של כהנים'])
hunknown=c('hunknown','18b:3','ואם סתם אסור','Unspecified כחרם prohibits.',conditions=['unspecified herem referent'])
animal=c('animal','18b:4','הרי עלי כמעשר אם כמעשר בהמה נדר  אסור','כמעשר prohibits if it refers to animal tithe.',conditions=['מעשר בהמה'])
grain=c('grain','18b:4','ואם של גורן מותר','Grain tithe as referent is permitted.',conditions=['tithe of threshing floor'])
munknown=c('munknown','18b:4','ואם סתם אסור','Unspecified כמעשר prohibits.',conditions=['unspecified tithe referent'])
chamber=c('chamber','18b:5','הרי עלי כתרומה אם כתרומת הלשכה נדר  אסור','כתרומה prohibits if it refers to the chamber contribution.',conditions=['תרומת הלשכה'],scope='Mishnah series ending with Rabbi Meir attribution')
produce=c('produce','18b:5','ואם של גורן מותר','Threshing-floor terumah as referent is permitted.',conditions=['תרומת גורן'],scope='Same series')
tunknown=c('tunknown','18b:5','ואם סתם  אסור דברי רבי מאיר','Rabbi Meir prohibits an unspecified terumah comparison.',holder='רבי מאיר',conditions=['unspecified terumah'],scope='Explicit closing attribution; earlier anonymous cases remain separately evidenced')
judea=c('judea','18b:6','רבי יהודה אומר סתם תרומה ביהודה אסורה בגליל מותרת שאין אנשי גליל מכירין את תרומת הלשכה','Rabbi Yehuda prohibits unspecified terumah in Judea but permits it in Galilee, whose people do not recognize the chamber contribution.',holder='רבי יהודה',conditions=['regional recognition distinction'],composition='composite',scope='Named regional terumah rule and explicit rationale')
regional=c('regional','18b:6','סתם חרמים ביהודה מותרין בגליל אסורין שאין אנשי גליל מכירין את חרמי הכהנים','The printed continuation permits unspecified herem in Judea but prohibits it in Galilee, whose people do not recognize priestly herem.',composition='composite',scope='Continuation initially read with Rabbi Yehuda, but Abaye reattributes it to Rabbi Elazar ben Rabbi Tzadok at19b:11',uncertainty=['Do not carry preceding Rabbi Yehuda attribution over this clause as a settled view; explicit correction below.'])
lenient=c('lenient','18b:7','והתנן ספק נזירות להקל','A cited Mishnah treats doubtful naziriteship leniently.',scope='Contrasting rule triggering discussion')
e('lenient.objection',lenient,general,'objection','18b:7')
zera=c('zera','18b:8','אמר רבי זירא לא קשיא הא רבי אליעזר הא רבנן','Rabbi Zeira distinguishes Rabbi Eliezer from the sages to explain the differing uncertainty rules.',holder='רבי זירא',mode='challenged',scope='Initial tannaitic allocation, abandoned later in the sequence')
koi=c('koi','18b:8','דתניא המקדיש חייתו ובהמתו הקדיש את הכוי','The cited anonymous teaching includes the koy when one consecrates both wild and domestic animals.',conditions=['consecration of חייתו ובהמתו'],scope='Quoted property-uncertainty case')
eliezer=c('eliezer','18b:8','רבי אליעזר אומר לא הקדיש את הכוי','Rabbi Eliezer excludes the koy from that consecration.',holder='רבי אליעזר',conditions=['same declaration'],scope='Printed אליעזר; later source prints אלעזר, not silently normalized')
yesrisk=c('yesrisk','18b:9','מאן דאמר ממונו מעייל לספיקא גופיה נמי מעייל','The explanation infers that one who includes uncertain property also includes personal uncertainty.',scope='First link from property rule to personal vow uncertainty')
norisk=c('norisk','18b:9','ומאן דאמר ממונו לא מעייל לספיקא גופיה (נמי)','Conversely, if one does not include uncertain property, all the more one does not include oneself in uncertainty.',extra=[('19a:1',None)],scope='Cross-page second inference')
e('zera.answer',zera,lenient,'answer','18b:8');e('koi.support',koi,yesrisk,'support','18b:8');e('eliezer.support',eliezer,norisk,'support','18b:8')
abaye=c('abaye','19a:2',None,'Abaye objects that the same source’s doubtful firstborn rules—human and animal, pure and impure—place the burden of proof on the claimant.',holder='אביי',composition='composite',scope='Objection to assigning lenient doubtful naziriteship to Rabbi Eliezer; several firstborn categories explicitly included')
shear=c('shear','19a:3',None,'An accompanying teaching nevertheless prohibits shearing and work with the doubtful firstborn animal.',composition='composite',scope='Religious prohibitions retained despite civil burden-of-proof rule')
automatic=q('automatic','19a:4',None,'Why compare sanctity arising automatically with sanctity created by human action?')
e('abaye.objection',abaye,zera,'objection','19a:2');e('shear.support',shear,abaye,'support','19a:3');e('automatic.answer',automatic,abaye,'answer','19a:4')
liquids=c('liquids','19a:5',None,'The sharper challenge cites Rabbi Meir’s rule that doubtful liquids are impure themselves but pure for transmitting impurity, with Rabbi Elazar also agreeing.',composition='composite',scope='Quoted impurity distinction; source prints רבי אלעזר, retained alongside earlier אליעזר without asserting historical identity',uncertainty=['The inspected edition alternates אליעזר/אלעזר in this discussion; no witness-based normalization performed.'])
impureq=q('impureq','19a:6',None,'Does Rabbi Elazar really regard the liquids themselves as impure?')
none=c('none','19a:7','והתניא רבי אלעזר אומר אין טומאה למשקין כל עיקר','Another teaching has Rabbi Elazar deny impurity to liquids entirely.',holder='רבי אלעזר',scope='Printed name and categorical statement, interpretation disputed next')
testimony=c('testimony','19a:7','תדע שהרי העיד יוסי בן יועזר איש צרידה על איל קמצא דכן ועל משקין בית מטבחיא דכן','The proof cites Yosei ben Yoezer of Tzereda’s testimony that איל קמצא and slaughterhouse liquids are דכן.',holder='יוסי בן יועזר איש צרידה',composition='composite',scope='Two testimony items preserved; untranslated איל קמצא not identified from memory')
shmuel=c('shmuel','19a:8',None,'Shmuel interprets דכן as unable to transmit impurity while retaining their own impurity, fitting the earlier distinction.',holder='שמואל',composition='composite',scope='Reported interpretation of testimony')
ravq=q('ravq','19a:9',None,'But under Rav’s interpretation of דכן as entirely pure, how can the earlier attribution stand?')
rav=c('rav','19a:9','לרב דאמר דכן ממש','Rav interprets דכן as actually pure.',holder='רב',scope='Explicit alternative interpretation, genuine disagreement with Shmuel on meaning')
e('none.support',none,impureq,'support','19a:7');e('testimony.support',testimony,none,'support','19a:7');e('ravq.objection',ravq,zera,'objection','19a:9')
replace=c('replace','19a:10',None,'The discussion instead distinguishes Rabbi Yehuda and Rabbi Shimon.',scope='Replacement allocation of uncertainty rules')
e('replace.correction',replace,zera,'correction','19a:10')
yehuda=c('yehuda','19a:11','דתניא הריני נזיר אם יש בכרי הזה מאה כור והלך ומצאו שנגנב או שאבד רבי יהודה מתיר','For conditional naziriteship if a heap contains one hundred kor, when the heap is stolen or lost before verification, Rabbi Yehuda permits.',holder='רבי יהודה',conditions=['הריני נזיר אם יש בכרי הזה מאה כור','heap stolen or lost'],scope='Unverifiable quantity case')
shimon=c('shimon','19a:11','ורבי שמעון אוסר','Rabbi Shimon prohibits in that same uncertain-heap case.',holder='רבי שמעון',conditions=['same lost/stolen heap condition'])
e('yehuda.support',yehuda,replace,'support','19a:11');e('shimon.support',shimon,replace,'support','19a:11')
conflict=q('conflict','19a:12','ורמי דרבי יהודה אדרבי יהודה מי אמר רבי יהודה לא מעייל איניש נפשיה לספיקא','Does Rabbi Yehuda deny that a person enters uncertainty, given his own regional terumah rule?')
known=c('known','19a:12','טעמא דאין מכירין','The objection infers that if people do recognize the chamber contribution, unspecified terumah is prohibited.',extra=[('19b:1',None)],scope='Cross-page inference from Rabbi Yehuda regional reason')
e('known.support',known,conflict,'support','19b:1')
harder=c('harder','19b:2',None,'Rava explains that in the heap case uncertainty is worse than certainty: a certain nazirite can shave and bring an edible offering, whereas the doubtful one cannot shave; a person avoids that uncertainty.',holder='רבא',conditions=['doubt harsher than certainty'],composition='composite',scope='Reason distinguishing doubtful naziriteship from ordinary ambiguous vows')
e('harder.answer',harder,conflict,'answer','19b:2')
lifelong=q('lifelong','19b:3',None,'Rav Huna bar Yehuda asks Rava about a lifelong nazirite undertaking.',voice='רב הונא בר יהודה')
lifeanswer=c('lifeanswer','19b:4',None,'Rava answers that lifelong doubt is also worse: the certain nazirite may lighten heavy hair with a razor and bring three animals, whereas the doubtful one cannot.',holder='רבא',conditions=['lifelong naziriteship','hair has become heavy'],composition='composite',scope='Specific certain/doubtful contrast')
e('lifeanswer.answer',lifeanswer,lifelong,'answer','19b:4')
samson=q('samson','19b:5',None,'What about an undertaking of Samson-type naziriteship?',voice='רב הונא בר יהודה')
notaught=c('notaught','19b:6','אמר ליה נזיר שמשון לא תניא','Rava replies that Samson-type naziriteship was not taught in that rule.',holder='רבא',mode='retracted',scope='Claim about baraita scope, yielded when a contrary report is cited')
ada=c('ada','19b:6','אמר ליה והאמר רב אדא בר אהבה תניא נזיר שמשון','The interlocutor cites Rav Adda bar Ahava reporting that Samson-type naziriteship was taught.',scope='Reported counterevidence, not a new argument invented for Rav Adda')
yieldc=c('yield','19b:6','אמר ליה אי תניא תניא','Rava accepts the report conditionally: if it was taught, it was taught.',holder='רבא',mode='unresolved',scope='Concession about report; no replacement explanation supplied for Samson case',uncertainty=['Rava’s harsher-doubt rationale is not resolved for the reported Samson case here.'])
e('notaught.answer',notaught,samson,'answer','19b:6');e('ada.objection',ada,notaught,'objection','19b:6');e('yield.correction',yieldc,notaught,'correction','19b:6')
tarfon=c('tarfon','19b:7',None,'Rav Ashi assigns the heap teaching to Rabbi Yehuda in Rabbi Tarfon’s name: none becomes a nazirite without explicit determination.',holder='רב אשי',composition='composite',scope='Alternative explanation using a transmitted tannaitic position, not Rabbi Yehuda’s unqualified personal view')
a.add('tarfon.chain','attributions',dict(surface='רבי יהודה משום רבי טרפון',role='transmitter',candidates=['רבי יהודה'],scope=tarfon,transmission_chain=['רבי יהודה','רבי טרפון']),[a.ev('19b:7',('רבי יהודה משום רבי טרפון',0))],[tarfon])
whyheap=q('whyheap','19b:8','אי הכי מאי איריא שנגנב או שאבד','If so, why specify that the heap was stolen or lost?')
strength=c('strength','19b:8','אלא להודיעך כוחו דרבי שמעון דאף על גב דנגנב או שאבד קסבר מעייל איניש נפשיה לספיקא','That case displays Rabbi Shimon’s stringency: even theft or loss does not prevent a person entering the uncertainty.',scope='Explanation of baraita’s chosen case')
e('tarfon.answer',tarfon,conflict,'answer','19b:7');e('strength.answer',strength,whyheap,'answer','19b:8')
strict=c('strict','19b:9',None,'The terumah regional rule implies stringency where both meanings are recognized.',scope='Revisited inference from the first regional clause')
lenient2=c('lenient2','19b:10',None,'The herem regional rule implies leniency where priestly herem is recognized, apparently conflicting with that stringency.',composition='composite',scope='Second regional clause, initially associated with the same named view')
abaye2=c('abaye2','19b:11','אמר אביי סיפא רבי אלעזר ברבי צדוק היא','Abaye assigns the latter clause to Rabbi Elazar son of Rabbi Tzadok.',holder='אביי',scope='Explicit reassignment of herem clause')
bara1=c('bara1','19b:11','דתניא רבי יהודה אומר סתם תרומה ביהודה אסורה','A baraita assigns unspecified terumah prohibition in Judea to Rabbi Yehuda.',holder='רבי יהודה',conditions=['unspecified terumah in Judea'],scope='Supporting attribution evidence')
bara2=c('bara2','19b:11','רבי אלעזר ברבי צדוק אומר סתם חרמים בגליל אסורין','The baraita assigns unspecified herem prohibition in Galilee to Rabbi Elazar ben Rabbi Tzadok.',holder='רבי אלעזר ברבי צדוק',conditions=['unspecified herem in Galilee'],scope='Distinct named position, correcting conflation with Rabbi Yehuda')
e('lenient2.objection',lenient2,strict,'objection','19b:10');e('abaye2.answer',abaye2,lenient2,'answer','19b:11');e('bara2.support',bara2,abaye2,'support','19b:11');e('abaye2.qualification',abaye2,regional,'qualification','19b:11')
a.notes={
'18b:1':'Reread heading and paired salted-meat/libation reference with sacrificial case.',
'18b:2':'Reread idolatry and unspecified branches.',
'18b:3':'Reread heavenly/priestly/unspecified herem branches separately.',
'18b:4':'Reread animal/grain/unspecified tithe branches.',
'18b:5':'Reread chamber/grain/unspecified terumah branches and explicit Rabbi Meir attribution.',
'18b:6':'Reread both regional rules and recognition reasons, with later Abaye correction preventing attribution carryover.',
'18b:7':'Reread opposing doubtful-nazirite rule.',
'18b:8':'Reread Rabbi Zeira allocation and koy consecration positions, retaining אליעזר spelling.',
'18b:9':'Reread both property-to-person inferences, second continues19a:1.',
'19a:1':'Reread cross-page all-the-more inference.',
'19a:2':'Reread Abaye objection and every human/animal/pure/impure firstborn category.',
'19a:3':'Reread shearing/work restrictions alongside burden-of-proof rule.',
'19a:4':'Reread automatic/human-created sanctity distinction.',
'19a:5':'Reread liquid self/transmitted impurity distinction and אלעזר spelling uncertainty.',
'19a:6':'Reread explicit consistency question.',
'19a:7':'Reread no-impurity statement and both Yosei ben Yoezer testimony items without species identification from memory.',
'19a:8':'Reread Shmuel’s transmission-only purity interpretation.',
'19a:9':'Reread Rav’s actual-purity interpretation and resulting objection, a real interpretive contrast.',
'19a:10':'Reread replacement tannaitic allocation.',
'19a:11':'Reread exact quantity condition, theft/loss and opposing Rabbi Yehuda/Rabbi Shimon outcomes.',
'19a:12':'Reread Rabbi Yehuda inconsistency and inference completed19b:1.',
'19b:1':'Reread recognized-meaning prohibition inference.',
'19b:2':'Reread Rava harsher-doubt rationale and specific shaving/offering consequences.',
'19b:3':'Reread Rav Huna bar Yehuda lifelong question.',
'19b:4':'Reread hair-weight, razor, three-animals and doubtful exclusion conditions.',
'19b:5':'Reread Samson-type question separately.',
'19b:6':'Reread not-taught claim, Rav Adda counterreport and conditional concession; no fabricated answer.',
'19b:7':'Reread Rav Ashi alternative and Rabbi Yehuda-in-Rabbi Tarfon transmission.',
'19b:8':'Reread theft/loss specificity question and Rabbi Shimon-strength answer.',
'19b:9':'Reread renewed terumah stringency inference.',
'19b:10':'Reread apparent herem leniency contrast.',
'19b:11':'Reread Abaye reassignment and supporting two-authority baraita.'}
if __name__=='__main__':a.save()
