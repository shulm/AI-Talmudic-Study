"""Manual overlapping naziriteships/oaths, unresolved challenge, and alternate formulation."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r017.';a.OUTPUT='continuation_017.json'
c=a.c;q=a.q;e=a.edge
scope=['17a:3','17a:4','17a:5']+['17b:'+str(i) for i in range(1,9)]+['18a:'+str(i) for i in range(1,11)]
a.structure('overlap',scope,'Overlapping nazirite undertakings and oaths; conditions, objections and first-oath release')
nv=c('nv','17a:3','יש נדר בתוך נדר','A vow can take effect within a vow.',scope='Mishnah heading, illustrated by repeated nazirite undertakings')
no=c('no','17a:3','ואין שבועה בתוך שבועה','An oath does not take effect within an oath in the stated overlapping case.',scope='Mishnah heading, liability and residual existence distinguished later')
repeatn=c('repeatn','17a:3','כיצד אמר הריני נזיר אם אוכל הריני נזיר אם אוכל ואכל חייב על כל אחת ואחת','Repeating the conditional nazirite undertaking and eating yields liability for each.',conditions=['two הריני נזיר אם אוכל declarations','then eating'],scope='Mishnah example')
repeato=c('repeato','17a:3','שבועה שלא אוכל שבועה שלא אוכל ואכל אינו חייב אלא אחת:','Repeating an oath not to eat and then eating yields only one liability.',conditions=['two שבועה שלא אוכל declarations','then eating'],scope='Mishnah example; not equated with nonexistence of second oath')
huna=c('huna','17a:4','אמר רב הונא לא שנו אלא דאמר הריני נזיר היום הריני נזיר למחר דמיגו דקא מיתוסף יומא יתירא חיילא נזירות על נזירות','Rav Huna restricts overlapping naziriteship to today followed by tomorrow, whose additional day permits the second undertaking to take effect.',holder='רב הונא',conditions=['הריני נזיר היום then הריני נזיר למחר'],scope='Restriction of Mishnah')
same=c('same','17a:4','אבל אמר הריני נזיר היום הריני נזיר היום אין חלה נזירות על נזירות','Rav Huna denies a second naziriteship for two repeated today declarations.',holder='רב הונא',conditions=['הריני נזיר היום twice'],mode='challenged',scope='Named view with unresolved structural objection below')
shmuel=c('shmuel','17a:4','ושמואל אמר אפילו אמר הריני נזיר היום הריני נזיר היום חלה נזירות עליה','Shmuel allows the second naziriteship even for two today declarations.',holder='שמואל',conditions=['הריני נזיר היום twice'],scope='Explicit disagreement with Rav Huna, not Rav himself')
why=q('why','17a:5',None,'According to Rav Huna, why does the Mishnah contrast oaths rather than distinguish today/tomorrow nazirite vows from today/today vows?')
hard=c('hard','17b:1',None,'The proposed missing today/today contrast remains a difficulty.',mode='unresolved',scope='End of cross-page objection; explicit קשיא retained',uncertainty=['No answer to this particular formulation objection is supplied in the inspected unit.'])
e('why.objection',why,huna,'objection','17a:5')
different=q('different','17b:2',None,'If the Mishnah’s naziriteship case is today/tomorrow, its oath parallel would be figs then grapes; why would the second oath not take effect?')
samecase=c('samecase','17b:3',None,'The objection instead matches repeated identical fig oaths with repeated today naziriteships and infers a difficulty for Rav Huna.',mode='challenged',composition='composite',scope='Argument from supposedly corresponding cases, answered next')
e('samecase.objection',samecase,huna,'objection','17b:3')
combined=c('combined','17b:4',None,'The reply in Rav Huna’s voice retains today/tomorrow naziriteship and parallels it with an oath against figs followed by an oath against figs and grapes, which he holds does not take effect on the prior prohibition.',holder='רב הונא',composition='composite',scope='Precisely combined second oath, not independent fig/grape oaths')
e('combined.answer',combined,different,'answer','17b:4');e('combined.answer2',combined,samecase,'answer','17b:4')
rabbah=c('rabbah','17b:5',None,'Rabbah says that after fig and then fig-and-grape oaths, eating figs and separating an offering, followed by eating grapes, leaves the grapes a half-measure for which no offering is brought.',holder='רבה',conditions=['specified two-oath sequence','figs eaten','offering separated','then grapes eaten'],composition='composite',scope='Quoted conditional liability account; רבה retained distinct from רבא')
extension=c('extension','17b:6','אלמא היכא דאמר שבועה שלא אוכל תאנים וחזר ואמר שבועה שלא אוכל תאנים וענבים מיגו דחל שבועה על ענבים חיילא נמי על תאנים','The discussion infers that the second oath extends from grapes to figs as well.',conditions=['figs then figs-and-grapes oaths'],scope='Inference from Rabbah’s reported ruling')
disagree=c('disagree','17b:6','רב הונא לא סבירא ליה כרבה','Rav Huna does not hold like Rabbah.',scope='Explicit nonagreement resolves this objection, not a retraction of Rav Huna')
e('rabbah.support',rabbah,extension,'support','17b:5');e('extension.objection',extension,combined,'objection','17b:6');e('disagree.answer',disagree,extension,'answer','17b:6')
annul=c('annul','17b:7',None,'A teaching says that one who undertook two naziriteships, counted the first, separated its offering and obtained release from it has the second count in place of the first.',conditions=['two undertakings','first count completed','offering separated','release from first'],composition='composite',scope='Quoted sequence used to challenge Rav Huna')
extra=q('extra','17b:8','היכי דמי אילימא דאמר הריני נזיר היום הריני נזיר למחר אמאי עלתה לו שניה בראשונה הא איכא יומא יתירא','If the declarations were today/tomorrow, how can the second count replace the first when there is an extra day?')
identical=c('identical','17b:8','אלא פשיטא דאמר הריני נזיר היום הריני נזיר היום','The objection therefore infers identical today declarations, contradicting Rav Huna.',extra=[('18a:1',None)],mode='rejected',scope='Cross-page inference deflected next')
e('identical.objection',identical,same,'objection','18a:1')
less=c('less','18a:2','לא לעולם הריני נזיר היום הריני נזיר למחר ומאי עלתה לו לבר מההוא יומא יתירא','The first answer retains today/tomorrow and understands replacement except for the extra day.',conditions=['one day remains additional'],scope='First deflection of annulment proof')
joint=c('joint','18a:2','אי נמי כגון שקיבל שתי נזירות בבת אחת','Alternatively the two naziriteships were accepted simultaneously.',conditions=['simultaneous acceptance'],scope='Second deflection, distinct from successive identical declarations')
e('less.correction',less,identical,'correction','18a:2');e('joint.correction',joint,identical,'correction','18a:2')
hamnuna=c('hamnuna','18a:3','מתיב רב המנונא נזיר להזיר מכאן שהנזירות חל על הנזירות','Rav Hamnuna objects from a teaching deriving overlapping naziriteship from נזיר להזיר.',holder='רב המנונא',scope='Presenter of quoted derivation, not asserted original tanna')
afort=c('afort','18a:3','שיכול והלא דין הוא ומה שבועה חמורה אין שבועה חלה על שבועה נזירות קלה לא כל שכן','Without the verse, one could argue from stricter oaths not overlapping that lighter naziriteship should not overlap.',mode='rejected',scope='Explicit excluded a-fortiori inference')
verse=c('verse','18a:3','תלמוד לומר נזיר להזיר מכאן שהנזירות חלה על הנזירות','The verse establishes that naziriteship can overlap naziriteship.',scope='Quoted teaching’s conclusion; case still at issue')
e('verse.correction',verse,afort,'correction','18a:3')
needq=q('needq','18a:4','היכי דמי אילימא דאמר הריני נזיר היום הריני נזיר למחר הא קרא בעיא','Would today/tomorrow really require a verse?')
identical2=c('identical2','18a:4','אלא לאו דאמר הריני נזיר היום הריני נזיר היום וקתני נזירות חל על נזירות','The objection infers that the verse instead establishes overlap for identical today declarations.',mode='rejected',scope='Proposed proof against Rav Huna, answered by simultaneous acceptance')
joint2=c('joint2','18a:5',None,'The answer again places the teaching in simultaneous acceptance of two naziriteships.',conditions=['simultaneous acceptance'],scope='Repeated deflection, retained separately')
e('identical2.objection',identical2,same,'objection','18a:4');e('joint2.correction',joint2,identical2,'correction','18a:5')
strictq=q('strictq','18a:6','ומאי חומרא דשבועה מנדר','In what respect are oaths stricter than vows?')
intangible=c('intangible','18a:6','אילימא משום דחיילא אפילו על דבר שאין בו ממש','The first suggested stringency is application to intangible matters.',mode='rejected',scope='Insufficient comparison when vows have their own stringency')
command=c('command','18a:6','נדר נמי חמור שכן חל על המצווה כרשות','Vows likewise have a stringency: applying to commandments as to optional matters.',scope='Counterweight to proposed comparison')
clean=c('clean','18a:6','אלא משום דכתיב בה בשבועה לא ינקה','The final explanation cites לא ינקה in connection with oaths.',scope='Source’s chosen basis for relative severity')
e('command.objection',command,intangible,'objection','18a:6');e('clean.answer',clean,strictq,'answer','18a:6')
rava=c('rava','18a:7','אמר רבא אם נשאל על הראשונה שניה חלה עליו','Rava says release from the first oath allows the second to take effect.',holder='רבא',conditions=['two repeated eating oaths','first annulled by release'],scope='Second-oath activation, distinct from Rabbah earlier')
how=q('how','18a:7','ממאי','From where is this inferred?')
wording=c('wording','18a:7','מדלא קתני אינו אלא אחת וקתני אינו חייב אלא אחת רווחא הוא דלית לה כי מיתשיל על חבירתה חיילא','The proof distinguishes “only one” from “liable only once”: the second lacks room until the first is released.',composition='composite',scope='Anonymous wording argument supporting Rava')
e('wording.answer',wording,how,'answer','18a:7');e('wording.support',wording,rava,'support','18a:7')
alt=c('alt','18a:8','לישנא אחרינא חיובא הוא דליכא הא שבועה איכא','An alternative wording infers that liability is absent but the second oath exists.',scope='Explicit alternative version, not duplicate to discard')
use=q('use','18a:8','למאי הלכתא','For what practical consequence does the second oath exist?')
rava2=c('rava2','18a:8','לכדרבא דאמר רבא נשאל על הראשונה עלתה לו שניה תחתיה','The alternative version cites Rava: when the first is released, the second replaces it.',holder='רבא',conditions=['release from first oath'],scope='Repeated report in alternate formulation')
e('rava2.answer',rava2,use,'answer','18a:8')
support=c('support','18a:9',None,'A support proposal repeats the two-nazirite-undertaking case where release from the first lets the second count in its place.',mode='challenged',composition='composite',scope='Explicit proposed support for Rava, not final confirmation')
deflect=c('deflect','18a:10',None,'The response again places that teaching in simultaneous acceptance of two naziriteships.',conditions=['simultaneous acceptance'],scope='Deflects proposed support from the nazirite case to successive oaths')
e('support.support',support,rava,'support','18a:9');e('deflect.objection',deflect,support,'objection','18a:10')
a.notes={
'17a:3':'Reread two headings and repeated conditional-nazirite/oath examples, distinguishing liability from existence.',
'17a:4':'Reread Rav Huna today/tomorrow restriction, identical-day exclusion and Shmuel explicit disagreement.',
'17a:5':'Reread structural why-not-intra-vow contrast question through17b:1.',
'17b:1':'Reread explicit קשיא ending, retained unresolved rather than concealed by later answers to different objections.',
'17b:2':'Reread independent fig/grape oath comparison objection.',
'17b:3':'Reread identical-case mapping and challenge to Rav Huna.',
'17b:4':'Reread combined figs-and-grapes response, not the independent-fruit case.',
'17b:5':'Reread Rabbah exact name and eat/separate/eat sequence yielding half-measure result.',
'17b:6':'Reread extension inference and explicit Rav Huna nonagreement with Rabbah.',
'17b:7':'Reread complete two-undertaking/count/offer/release teaching.',
'17b:8':'Reread extra-day question and identical-day inference across18a:1.',
'18a:1':'Reread contradiction completion connected to prior inference.',
'18a:2':'Reread both answers: extra day excepted, or simultaneous undertaking.',
'18a:3':'Reread Rav Hamnuna presentation, excluded a-fortiori and verse conclusion.',
'18a:4':'Reread verse-necessity question and challenged identical-day inference.',
'18a:5':'Reread repeated simultaneous-acceptance deflection.',
'18a:6':'Reread severity question, rejected intangible criterion, vow counterweight and לא ינקה answer.',
'18a:7':'Reread Rava activation rule and liability-versus-existence wording proof.',
'18a:8':'Reread explicit alternate version, practical-consequence question and repeated Rava report.',
'18a:9':'Reread offered nazirite support with all sequential conditions, as challenged proposal.',
'18a:10':'Reread final simultaneous-acceptance deflection; no final new support claimed.'}
if __name__=='__main__':a.save()
