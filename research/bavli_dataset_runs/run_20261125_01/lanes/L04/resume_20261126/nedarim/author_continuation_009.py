"""Manual wicked/righteous formulation unit and its narrative/ascetic continuations."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r009.';a.OUTPUT='continuation_009b.json'
c=a.c;q=a.q;e=a.edge
a.structure('formulas',['9a:'+str(i) for i in range(1,6)],'Vows like those of wicked and righteous people; contextual formula requirements')
scope=['9a:'+str(i) for i in range(6,9)]+['9b:'+str(i) for i in range(1,12)]+['10a:'+str(i) for i in range(1,11)]
a.structure('voluntary',scope,'Vows versus voluntary offerings, approved nazirite motives, and criticism of ascetic deprivation')
a.add('southern.story','structure',dict(title='Shimon’s account of the southern nazirite and the nazirite’s embedded explanation',primary=False,boundary='closed',legacy_ids=[]),[a.ev('9b:'+str(i)) for i in range(5,8)],origin='editorial_inference')
wicked=c('wicked','9a:1','כנדרי רשעים נדר בנזיר ובקרבן ובשבועה.','כנדרי רשעים can create nazirite, offering and oath commitments.',composition='composite',scope='Mishnah’s three-category rule; qualifications supplied in9a:2–5')
good=c('good','9a:1','כנדרי כשרים לא אמר כלום','כנדרי כשרים has no effect.',conditions=['כנדרי כשרים'],scope='Mishnah')
gift=c('gift','9a:1','כנדבותם נדר בנזיר ובקרבן','כנדבותם can create nazirite and offering commitments.',conditions=['referring to righteous people’s voluntary dedications'],composition='composite',scope='Mishnah’s two-category rule; printed נדר is discussed later')
negative=q('negative','9a:2','ודלמא הכי קאמר כנדרי רשעים לא נדרנא','Perhaps the speaker means that he will not vow like the wicked?')
supplied=c('supplied','9a:2','אמר שמואל באומר כנדרי רשעים הריני עלי והימנו','Shmuel specifies a case adding הריני, עלי or הימנו after כנדרי רשעים.',holder='שמואל',composition='composite',scope='Explicit formula qualification')
naz=c('naz','9a:2','הריני בנזירות','הריני corresponds to naziriteship.',scope='Formula mapping in Shmuel explanation; context refined next')
off=c('off','9a:2','עלי בקרבן','עלי corresponds to an offering commitment.',scope='Formula mapping')
oath=c('oath','9a:2','הימנו בשבועה','הימנו corresponds to an oath.',scope='Formula mapping, clarified9a:4')
e('supplied.answer',supplied,negative,'answer','9a:2');e('supplied.qualification',supplied,wicked,'qualification','9a:2')
fastq=q('fastq','9a:3','הריני נזירות דלמא הריני בתענית קאמר','Might הריני instead refer to a fast?')
passing=c('passing','9a:3','אמר שמואל כשהיה נזיר עובר לפניו','Shmuel specifies a nazirite passing before the speaker.',holder='שמואל',conditions=['nazirite passing before speaker'],scope='Contextual clarification of הריני')
e('passing.answer',passing,fastq,'answer','9a:3');e('passing.qualification',passing,naz,'qualification','9a:3')
eatq=q('eatq','9a:4','הימנו בשבועה דלמא הימנו דאכילנא קאמר','Might הימנו mean that he will eat of it?')
not_eat=c('not','9a:4','אמר רבא דאמר הימנו שלא אוכל','Rava specifies that he says הימנו שלא אוכל.',holder='רבא',conditions=['explicit שלא אוכל'],scope='Qualification of oath reading')
e('not.answer',not_eat,eatq,'answer','9a:4');e('not.qualification',not_eat,oath,'qualification','9a:4')
obvious=q('obvious','9a:5','אי הכי מאי למימרא','If so, what does the Mishnah teach?')
word=c('word','9a:5','מהו דתימא הא לא מפיק שבועה מפומיה','One might have denied effect because the speaker did not utter the word שבועה.',mode='rejected',scope='Excluded assumption explaining novelty')
effect=c('effect','9a:5','קא משמע לן הדין','The teaching gives effect despite the absence of the explicit word שבועה.',conditions=['qualified formula just described'],scope='Local answer, not every bare intention effective')
e('word.answer',word,obvious,'answer','9a:5');e('effect.correction',effect,word,'correction','9a:5')
who=q('who','9a:6','מאן תנא דשאני ליה בין נדר לנדבה לימא לא רבי מאיר ולא רבי יהודה','Which tanna distinguishes vow and voluntary dedication—is it neither Rabbi Meir nor Rabbi Yehuda?')
meir=c('meir','9a:7','טוב מזה ומזה שאינו נודר כל עיקר דברי רבי מאיר','Rabbi Meir considers not vowing at all better than the alternatives.',holder='רבי מאיר',scope='Quoted baraita interpreting טוב אשר לא תדור; vow/voluntary scope refined next')
yehuda=c('yehuda','9a:7','רבי יהודה אומר טוב מזה ומזה נודר ומשלם','Rabbi Yehuda says vowing and paying is better than the alternatives.',holder='רבי יהודה',scope='Quoted printed formulation, later reread as voluntary dedication')
candidate=c('candidate','9a:8',None,'The Mishnah can be assigned even to Rabbi Meir.',scope='First proposed tanna-compatible interpretation')
limit=c('limit','9b:1','כי קאמר רבי מאיר בנדר בנדבה לא קאמר','Rabbi Meir’s criticism concerns vows, not voluntary dedications.',scope='Anonymous scope qualification of quoted view')
textq=q('textq','9b:1','והא קתני כנדבותם, נדר בנזיר ובקרבן','But the Mishnah uses נדר for the voluntary-dedication case?')
read=c('read','9b:1','תני נדב בנזיר ובקרבן','The reply reads the clause as נדב in nazirite and offering cases.',scope='Explicit proposed reading, not an alteration of pinned source')
e('candidate.answer',candidate,who,'answer','9a:8');e('limit.qualification',limit,meir,'qualification','9b:1');e('read.answer',read,textq,'answer','9b:1')
risk=q('risk','9b:2',None,'If vows risk a transgression, why do voluntary dedications not carry the same risk?')
hillel=c('hillel','9b:3','כהלל הזקן דתניא אמרו על הלל הזקן שלא מעל אדם בעולתו כל ימיו','The answer cites the report that nobody misappropriated Hillel the elder’s burnt offering throughout his life.',scope='Narrated outcome of the procedure that follows, not a quantified external historical audit')
bring=c('bring','9b:3','מביאה כשהיא חולין לעזרה ומקדישה,','He brought the animal unconsecrated into the courtyard and consecrated it there.',composition='composite',scope='Narrated sequence avoids a long interval of consecration')
slaughter=c('slaughter','9b:3','וסומך עליה ושוחטה','He then laid hands on it and slaughtered it.',composition='composite',scope='Remaining narrated procedure')
e('hillel.answer',hillel,risk,'answer','9b:3');e('bring.support',bring,hillel,'support','9b:3');e('slaughter.support',slaughter,hillel,'support','9b:3')
nq=q('nq','9b:4','הניחא נדבה דקרבנות נדבה דנזירות מאי איכא למימר','That explains voluntary offerings, but how is voluntary naziriteship justified?')
shimon=c('shimon','9b:4','סבר לה כשמעון הצדיק','The answer invokes the view of Shimon the righteous.',scope='Proposed compatibility, supported by the ensuing narrative')
e('shimon.answer',shimon,nq,'answer','9b:4')
only=c('only','9b:5','דתניא אמר (רבי) שמעון הצדיק מימי לא אכלתי אשם נזיר טמא אלא אחד','Shimon the righteous reports eating the guilt offering of an impure nazirite only once.',holder='שמעון הצדיק',scope='First-person reported practice, with explicit single exception')
south=c('south','9b:5','פעם אחת בא אדם אחד נזיר מן הדרום','On that occasion a nazirite came from the south.',scope='Narrative event in Shimon’s account')
beauty=c('beauty','9b:5','וראיתיו שהוא יפה עינים וטוב רואי וקווצותיו סדורות לו תלתלים','Shimon describes the man as beautiful-eyed, handsome and with arranged curls.',holder='שמעון הצדיק',composition='composite',scope='Reported physical description, not inferred psychological motive')
hairq=q('hairq','9b:5','אמרתי לו בני מה ראית להשחית את שערך זה הנאה','Shimon asks why the man chose to destroy his beautiful hair.',voice='שמעון הצדיק')
shepherd=c('shepherd','9b:6','אמר לי רועה הייתי לאבא בעירי','The nazirite says he had been a shepherd for his father in his town.',holder='unnamed southern nazirite',scope='Embedded first-person response, not Shimon’s biography')
reflection=c('reflection','9b:6','הלכתי למלאות מים מן המעיין ונסתכלתי בבבואה שלי','He went to draw spring water and looked at his reflection.',holder='unnamed southern nazirite',composition='composite',scope='Reported event sequence')
urge=c('urge','9b:6','ופחז עלי יצרי ובקש לטורדני מן העולם','He describes his impulse as rushing upon him and seeking to drive him from the world.',holder='unnamed southern nazirite',scope='Self-reported internal experience explicitly in source, not annotator’s inferred motive')
rebuke=c('rebuke','9b:6','אמרתי לו רשע למה אתה מתגאה בעולם שאינו שלך במי שהוא עתיד להיות רימה ותולעה','He reports rebuking his impulse for pride in a world not its own and in a body destined for decay.',holder='unnamed southern nazirite',composition='composite',scope='Embedded self-address with rhetorical question; no separate historical addressee invented')
rebukeq=q('rebukeq','9b:6','למה אתה מתגאה בעולם שאינו שלך במי שהוא עתיד להיות רימה ותולעה','Why take pride in a world not your own and in a body destined for decay?',voice='unnamed southern nazirite')
vow=c('vow','9b:6','העבודה שאגלחך לשמים','He vowed to shave for heaven.',holder='unnamed southern nazirite',scope='Reported declaration explaining the nazirite undertaking')
e('vow.answer',vow,hairq,'answer','9b:6')
kiss=c('kiss','9b:7','מיד עמדתי ונשקתיו על ראשו.','Shimon reports immediately standing and kissing the man’s head.',holder='שמעון הצדיק',composition='composite',scope='Narrated response, not a legal requirement')
bless=c('bless','9b:7','אמרתי לו בני כמוך ירבו גוזרי נזירות בישראל','Shimon wishes that nazirite undertakers like this man should multiply in Israel.',holder='שמעון הצדיק',scope='Approval scoped to this described undertaking')
verse=c('verse','9b:7',"עליך הכתוב אומר איש כי יפליא לנדור נדר נזיר להזיר לה'",'Shimon applies the verse נזיר להזיר לה׳ to this man.',holder='שמעון הצדיק',scope='Narrative scriptural endorsement')
e('bless.support',bless,shimon,'support','9b:7');e('verse.support',verse,bless,'support','9b:7')
mani=q('mani','9b:8',None,'Rabbi Mani asks why only an impure nazirite guilt offering is avoided for coming from sin, since all guilt offerings come from sin.',voice='רבי מני')
regret=c('regret','9b:9','אמר ליה רבי יונה היינו טעמא כשהן תוהין נוזרין וכשהן מטמאין ורבין עליהן ימי נזירות מתחרטין בהן','Rabbi Yona explains that they undertake naziriteship amid regret, then regret the undertaking when impurity increases its days.',holder='רבי יונה',conditions=['impurity prolongs naziriteship'],composition='composite',scope='Source’s stated causal account, not inferred individual psychology')
ordinary=c('ordinary','9b:9','ונמצאו מביאין חולין לעזרה','Consequently their offerings amount to bringing unconsecrated animals into the courtyard.',holder='רבי יונה',scope='Consequence in Rabbi Yona’s explanation; no independent adjudication of all vow-regret mechanisms')
e('regret.answer',regret,mani,'answer','9b:9');e('regret.support',regret,ordinary,'support','9b:9')
pureq=q('pureq','9b:10','אי הכי אפילו נזיר טהור נמי','Should this not also apply to a pure nazirite?')
estimate=c('estimate','9b:10','נזיר טהור לא דאמודי אמיד נפשיה דיכול לנדור','The pure nazirite has assessed his ability to undertake the vow, so the stated concern does not apply.',conditions=['pure nazirite','original undertaking not prolonged by impurity'],scope='Local distinction in answer')
e('pureq.objection',pureq,regret,'objection','9b:10');e('estimate.answer',estimate,pureq,'answer','9b:10')
alternate=c('alternate','9b:11',None,'Alternatively the Mishnah can fit Rabbi Yehuda, whose approval concerns voluntary dedication rather than vows.',extra=[('10a:1',None)],composition='composite',scope='Cross-page alternative interpretation of tanna and scope')
e('alternate.answer',alternate,who,'answer','10a:1')
yq=q('yq','10a:2','והקתני טוב מזה ומזה נודר ומקיים','But the teaching says that vowing and fulfilling is better?')
yread=c('yread','10a:2','תני נודב ומקיים','The reply reads the praise as voluntary dedication and fulfillment.',scope='Proposed baraita reading, not silent source emendation')
e('yread.answer',yread,yq,'answer','10a:2');e('alternate.qualification',alternate,yehuda,'qualification','10a:1')
risk2=q('risk2','10a:3',None,'Why do voluntary dedications escape the same transgression risk as vows?')
lamb=c('lamb','10a:4',None,'Rabbi Yehuda’s own view permits bringing a lamb into the courtyard, consecrating it, laying hands and slaughtering it there.',holder='רבי יהודה',composition='composite',scope='Ordered sacrificial procedure supplied as answer to risk')
e('lamb.answer',lamb,risk2,'answer','10a:4')
nq2=q('nq2','10a:5',None,'That explains voluntary offerings, but what about voluntary naziriteship?')
desire=c('desire','10a:6','רבי יהודה לטעמיה דתניא רבי יהודה אומר חסידים הראשונים היו מתאווין להביא קרבן חטאת','Rabbi Yehuda says the early pious people desired to bring a sin offering.',holder='רבי יהודה',scope='Reported religious aspiration explicitly in source')
protect=c('protect','10a:6','לפי שאין הקדוש ברוך הוא מביא תקלה על ידיהם','He gives the reason that God does not bring transgression through them.',holder='רבי יהודה',scope='Source’s account of those pious people, not an empirical certification')
whatq=q('whatq','10a:6','מה היו עושין','What did those pious people do?')
undertake=c('undertake','10a:6','עומדין ומתנדבין נזירות למקום כדי שיתחייב קרבן חטאת למקום','They voluntarily undertook naziriteship for God to become obligated in a sin offering.',holder='רבי יהודה',scope='Reported means and explicit purpose')
e('undertake.answer',undertake,whatq,'answer','10a:6');e('undertake.answer2',undertake,nq2,'answer','10a:6')
deny=c('deny','10a:7','רבי שמעון אומר לא נדרו בנזיר','Rabbi Shimon says they did not undertake nazirite vows.',holder='רבי שמעון',scope='Contrasting account of early pious people')
olah=c('olah','10a:7','אלא הרוצה להביא עולה מתנדב ומביא','One desiring a burnt offering could dedicate and bring it voluntarily.',holder='רבי שמעון',conditions=['desire to bring burnt offering'])
peace=c('peace','10a:7','שלמים מתנדב ומביא','One could voluntarily bring a peace offering.',holder='רבי שמעון',scope='Alternative voluntary offering')
thanks=c('thanks','10a:7','תודה וארבעה מיני לחמה מתנדב ומביא','One could voluntarily bring a thanksgiving offering with its four kinds of bread.',holder='רבי שמעון',scope='Alternative offering and its expressly enumerated bread requirement')
sinner=c('sinner','10a:7','אבל בנזירות לא התנדבו כדי שלא יקראו חוטאין שנאמר וכפר עליו מאשר חטא על הנפש','They avoided voluntary naziriteship so as not to be called sinners, supported by the verse about atonement for sin against the soul.',holder='רבי שמעון',composition='composite',scope='Explicit reason and scriptural support in contrasting account')
e('deny.objection',deny,undertake,'objection','10a:7');e('sinner.support',sinner,deny,'support','10a:7')
group=c('group','10a:8','אמר אביי שמעון הצדיק ורבי שמעון ורבי אלעזר הקפר כולן שיטה אחת הן דנזיר חוטא הוי','Abaye groups Shimon the righteous, Rabbi Shimon and Rabbi Elazar HaKappar as sharing the view that a nazirite is a sinner.',holder='אביי',composition='composite',scope='Abaye’s explicit classification of three authorities, not proof their every condition and ruling are identical')
already2=c('already2','10a:8','שמעון הצדיק ורבי שמעון הא דאמרן','The discussion points to the foregoing accounts for Shimon the righteous and Rabbi Shimon.',scope='Explicit backward reference, no external harmonization')
elazarq=q('elazarq','10a:9','וכי באיזו נפש חטא זה','Against which soul has this nazirite sinned?',voice='רבי אלעזר הקפר ברבי')
wine=c('wine','10a:9','אלא שציער עצמו מן היין','Rabbi Elazar HaKappar explains the sin as depriving himself of wine.',holder='רבי אלעזר הקפר ברבי',scope='Interpretation of the quoted atonement verse')
more=c('more','10a:9','והלא דברים קל וחומר ומה זה שלא ציער עצמו אלא מן היין נקרא חוטא המצער עצמו מכל דבר, על אחת כמה וכמה','His a-fortiori argument applies all the more to one who deprives himself of everything.',holder='רבי אלעזר הקפר ברבי',conditions=['deprivation beyond wine'],scope='Source’s explicit inference, not blanket health guidance')
fast=c('fast','10a:9','מכאן כל היושב בתענית נקרא חוטא','The teaching concludes that one who fasts is called a sinner.',holder='רבי אלעזר הקפר ברבי',scope='Conclusion of this quoted interpretive position; no later halakhic reconciliation inferred')
a.add('kappar.authority','attributions',dict(surface='רבי אלעזר הקפר ברבי',role='quoted_authority',candidates=['רבי אלעזר הקפר ברבי'],scope=wine,transmission_chain=[]),[a.ev('10a:9','דתניא רבי אלעזר הקפר ברבי אומר')],[wine])
e('wine.answer',wine,elazarq,'answer','10a:9');e('wine.support',wine,more,'support','10a:9');e('more.support',more,fast,'support','10a:9');e('wine.supportgroup',wine,group,'support','10a:9')
impure=q('impure','10a:10','והדין קרא בנזיר טמא כתיב','But this verse concerns an impure nazirite?')
repeatSin=c('repeatSin','10a:10','משום דשנה בחטא הוא','The reply says that he repeated the sin.',scope='Local answer for the verse’s impure-nazirite setting; no unexpressed mechanism specified')
e('impure.objection',impure,wine,'objection','10a:10');e('repeatSin.answer',repeatSin,impure,'answer','10a:10')
a.notes={
'9a:1':'Reread three Mishnah formulations and distinct category counts; source HTML retained in ownership only.',
'9a:2':'Reread negation possibility, Shmuel supplements and three mappings.',
'9a:3':'Reread fasting alternative and passing-nazirite condition.',
'9a:4':'Reread eating alternative and Rava’s explicit שלא אוכל qualification.',
'9a:5':'Reread novelty question, absent explicit oath-word and effective abbreviated formulation.',
'9a:6':'Reread tanna-identification question; both proposed identifications examined through10a:10.',
'9a:7':'Reread Rabbi Meir/Rabbi Yehuda contrast without prematurely substituting later readings.',
'9a:8':'Reread Rabbi Meir possibility continuing9b:1.',
'9b:1':'Reread vow/voluntary scope and explicit נדב rereading, preserving original נדר.',
'9b:2':'Reread shared-risk objection.',
'9b:3':'Reread Hillel outcome and full consecrate/lay-hands/slaughter sequence.',
'9b:4':'Reread nazirite extension question and Shimon invocation.',
'9b:5':'Reread exception to avoidance, southern origin, appearance and direct question; narrative split into supported units.',
'9b:6':'Reread shepherd’s nested speech, spring/reflection event, reported impulse, rebuke and vow; speaker never confused with Shimon.',
'9b:7':'Reread kiss, blessing and scriptural endorsement as distinct narrative actions/utterances.',
'9b:8':'Reread Rabbi Mani’s all-guilt-offerings challenge.',
'9b:9':'Reread Rabbi Yona’s stated regret/prolongation rationale and unconsecrated-animal consequence.',
'9b:10':'Reread pure-nazirite challenge and assessed-ability distinction.',
'9b:11':'Reread transition together with10a:1 rather than invent a stand-alone claim.',
'10a:1':'Reread alternative Rabbi Yehuda compatibility and voluntary-only scope.',
'10a:2':'Reread printed נודר objection and explicit נודב rereading.',
'10a:3':'Reread repeated risk question as separate occurrence.',
'10a:4':'Reread Rabbi Yehuda’s full offering procedure.',
'10a:5':'Reread nazirite question, distinct repeated occurrence.',
'10a:6':'Reread pious-person desire, protective premise, question, and stated purpose of nazirite undertaking.',
'10a:7':'Reread Rabbi Shimon’s denial and all three offering alternatives including four bread kinds; avoidance reason and proof retained.',
'10a:8':'Reread Abaye’s three-authority classification without flattening all positions; backward reference preserved.',
'10a:9':'Reread Rabbi Elazar HaKappar question, wine-deprivation claim, a-fortiori inference and fasting conclusion.',
'10a:10':'Reread impure-nazirite verse objection and repeated-sin answer, leaving unexpressed detail unstated.'}
# This locally described speaker has no proper name in the source. Preserve the
# narrative role without passing an English description off as a Hebrew mention.
for key in ['shepherd','reflection','urge','rebuke','vow','rebukeq']:
    row=next(x for x in a.records if x['id']=='nd.r009.'+key+'.a')
    row['content']['surface']='';row['uncertainty']=['Unnamed southern nazirite identified by the narrative frame, not a resolved named person.']
if __name__=='__main__':a.save()
