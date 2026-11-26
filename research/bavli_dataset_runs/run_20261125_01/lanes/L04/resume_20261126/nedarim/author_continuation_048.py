"""Communal-property assignment and Beit Horon: alternative Rava versions and conditional transfer."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r048.';a.OUTPUT='continuation_048.json'
c=a.c;q=b.q;e=a.edge
a.structure('community',['47b:5']+['48a:'+str(i) for i in range(1,6)],'Directional bans and national/town property with assignment to president')
a.structure('gift',['48a:'+str(i) for i in range(6,11)]+['48b:'+str(i) for i in range(1,8)],'Genuine gifts, two Beit Horon readings and acquisition for subsequent transfer')
a.structure('end',['48b:8'],'End of partners chapter')
me=c('me','47b:5','הריני עליך חרם המודר אסור','Declaring oneself forbidden to another prohibits the recipient from benefit.',scope='First directional formula')
you=c('you','47b:5','הרי את עלי חרם הנודר אסור','Declaring the other forbidden upon oneself prohibits the speaker.',scope='Reverse formula')
mutual=c('mutual','47b:5','הריני עליך ואת עלי שניהם אסורין','The reciprocal formula prohibits both.',scope='Both-direction case')
national=c('national','47b:5','ושניהם מותרין בדבר של עולי בבל','Both may use property designated for those who came up from Babylonia.',scope='Nationwide category defined next segment')
town=c('town','48a:1','ואסורים בדבר של אותה העיר','Both are forbidden the property of their town.',scope='Contrast with wider communal property')
nationalList=c('nationalList','48a:1','ואיזהו דבר של עולי בבל כגון הר הבית והעזרות והבור שבאמצע הדרך','Examples of the wider category are the Temple Mount, courtyards and roadside well.',composition='composite',scope='Three explicitly listed communal examples')
townList=c('townList','48a:1','ואיזהו דבר של אותה העיר כגון הרחבה והמרחץ ובית הכנסת והתיבה והספרים','Town property includes the public square, bathhouse, synagogue, ark and books.',composition='composite',scope='Five explicitly listed town examples')
write=c('write','48a:1','והכותב חלקו לנשיא','The Mishnah adds assignment of one’s share to the president.',scope='Compressed clause clarified as remedy48a:3, not a new prohibited category')
yehuda=c('yehuda','48a:2',"ר' יהודה אומר אחד כותב לנשיא ואחד כותב להדיוט",'Rabbi Yehuda allows writing the share to either president or private person.',holder="ר' יהודה",scope='Two recipients of assignment')
diffq=q('diffq','48a:2','מה בין כותב לנשיא לכותב להדיוט','How do these recipients differ?')
acquire=c('acquire','48a:2','שהכותב לנשיא אין צריך לזכות להדיוט צריך לזכות','Under Rabbi Yehuda, assignment to the president needs no separate acquisition, whereas assignment to a private person does.',holder="ר' יהודה",composition='composite',scope='Formal acquisition distinction')
sages=c('sages','48a:2','וחכמים אומרים אחד זה ואחד זה צריכין לזכות לא דברו בנשיא אלא בהוה','The sages require acquisition in both cases and say the president is mentioned only as the usual case.',holder='חכמים',composition='composite',scope='Explicit disagreement on formality')
galilee=c('galilee','48a:2','רבי יהודה אומר אין אנשי גליל צריכין לכתוב שכבר כתבו אבותיהן על ידיהן','Rabbi Yehuda exempts Galileans from writing because their ancestors already assigned on their behalf.',holder='רבי יהודה',scope='Source’s historical/legal claim, not general present-day geographic rule')
e('acquire.answer',acquire,diffq,'answer','48a:2');e('sages.objection',sages,acquire,'objection','48a:2')
whyq=q('whyq','48a:3','אמאי מיתסר','Why would assignment to the president be listed as prohibited?')
remedy=c('remedy','48a:3','אמר רב ששת הכי קתני ומה תקנתן יכתבו חלקן לנשיא','Rav Sheshet reads it as the remedy: they should assign their shares to the president.',holder='רב ששת',scope='Explicit reinterpretation of compressed Mishnah clause')
e('remedy.answer',remedy,whyq,'answer','48a:3');e('remedy.qualification',remedy,write,'qualification','48a:3')
repeat=c('repeat','48a:4',None,'The discussion repeats Rabbi Yehuda’s president/private acquisition distinction and the sages’ requirement in both cases.',composition='composite',scope='Repeated full occurrence retained, not a separate newly inferred dispute')
history=c('history','48a:5',"תניא ר' יהודה אומר אנשי גליל קנטרנין היו והיו נודרין הנאה זה מזה עמדו אבותיהם וכתבו חלקיהן לנשיא",'Rabbi Yehuda’s baraita portrays Galileans as disputatious and mutually vowing, prompting their ancestors to assign shares to the president.',holder="ר' יהודה",composition='composite',scope='Attributed historical characterization, not an endorsed stereotype')
third=c('third','48a:6','המודר הנאה מחבירו ואין לו מה יאכל נותנו לאחר לשום מתנה והלה מותר בה','One may give food as a gift to another so the benefit-restricted person lacking food may benefit.',scope='Genuine third-party gift permission')
wedding=c('wedding','48a:6','מעשה באחד בבית חורון שהיה אביו נודר הימנו הנאה והיה משיא את בנו','The Beit Horon story concerns a man whose father was prohibited from his benefit and who was marrying off his son.',composition='composite',scope='Three-generation setting retained')
condition=c('condition','48a:6','ואמר לחברו חצר וסעודה נתונים הינן לפניך אלא כדי שיבא אבא ויאכל עמנו בסעודה','He offers his friend the courtyard and feast only so his father can attend and eat.',composition='composite',scope='Express limiting purpose in narrative gift')
consecrate=c('consecrate','48a:7','אמר אם שלי הם הרי הם מוקדשין לשמים','The friend replies that if the assets are his, they are consecrated to Heaven.',scope='Recipient tests actual ownership')
protest=c('protest','48a:7','א"ל נתתי לך את שלי שתקדישם לשמים','The giver objects to the recipient consecrating what he gave.',scope='Narrative evidence of retained control')
blame=c('blame','48a:7','אמר לו נתת לי את שלך אלא שתהא אתה ואביך אוכלין ושותין ומתרצין זה לזה ויהא עון תלוי בראשו','The recipient objects that the gift merely enables father and son to eat and reconcile while placing transgression on him.',composition='composite',scope='Attributed criticism within narrative')
rule=c('rule','48a:7','אמרו חכמים כל מתנה שאינה שאם הקדישה תהא מקודשת אינה מתנה','The sages declare that a gift whose recipient’s consecration would not take effect is not a gift.',holder='חכמים',scope='General rule derived in this narrative context')
contradict=q('contradict','48a:8','מעשה לסתור','Does this story contradict the stated permission?')
ending=c('ending','48a:8','חסורי מיחסרא והכי קתני ואם הוכיח סופו על תחילתו אסור ומעשה נמי בבית חורון באחד דהוה סופו מוכיח על תחילתו','The reconstructed teaching prohibits where later conduct reveals the initial intent, and the Beit Horon story is such a case.',composition='composite',scope='Explicit חסורי מיחסרא adds condition rather than abolishing third-party gift permission')
e('ending.answer',ending,contradict,'answer','48a:8');e('ending.qualification',ending,third,'qualification','48a:8')
rava1=c('rava1','48a:9',None,'In one report Rava limits the ban to only-so-father-comes wording, allowing the other formulation as leaving attendance to the recipient’s discretion.',holder='רבא',composition='composite',scope='First Rava version, explicit wording distinction')
rava2=c('rava2','48a:10',None,'An alternate Rava report prohibits even the less restrictive wording because the feast itself reveals the intent.',holder='רבא',composition='composite',scope='Explicit לישנא אחרינא, stricter contextual reading; both versions retained')
e('rava2.distinction',rava2,rava1,'distinction','48a:10')
son=c('son','48b:1','ההוא גברא דהוה ליה ברא דהוה שמיט כיפי דכיתנא אסרינהו לנכסיה עליה','A father prohibits his assets to a son described as שמיט כיפי דכיתנא.',scope='Exact conduct expression preserved without supplying unquoted details')
grandq=q('grandq','48b:1','אמרו ליה ואי הואי בר ברך צורבא מרבנן מאי','What if his grandson becomes a Torah scholar?')
transfer=c('transfer','48b:1','אמר להון ליקני הדין ואי הואי בר ברי צורבא מרבנן לקנייה','He directs that this one acquire so a scholar grandson may acquire if that condition occurs.',scope='Conditional acquisition-for-transfer arrangement, not unrestricted benefit for son')
validq=q('validq','48b:1',('מאי',1),'What is the legal effect of that arrangement?')
pumbedita=c('pumbedita','48b:2',None,'The Pumbedita scholars classify it as acquisition solely to transfer onward and deny that this acquires.',holder='פומבדיתאי',scope='Collective position on conditional arrangement')
nahman=c('nahman','48b:3',None,'Rav Nahman validates it by analogy with a cloth used for acquisition-for-transfer.',holder='רב נחמן',scope='Opposing analogy-based position')
clothq=q('clothq','48b:4','אמר רב אשי ומאן לימא לן דסודרא אי תפיס ליה לא מיתפיס','Rav Ashi asks how we know the recipient could not retain the cloth.',voice='רב אשי')
timing=c('timing','48b:4','ועוד סודרא קני על מנת להקנות וקני מן השתא הלין ניכסין דהדין לאימתי קני לכי הוי בר בריה צורבא מרבנן לכי הוה הדר סודרא למריה','Rav Ashi further distinguishes the cloth’s immediate acquisition from these assets’ delayed acquisition when the grandson becomes a scholar, by which time the cloth has returned.',holder='רב אשי',composition='composite',scope='Timing objection to analogy')
e('transfer.answer',transfer,grandq,'answer','48b:1');e('pumbedita.answer',pumbedita,validq,'answer','48b:2');e('nahman.answer',nahman,validq,'answer','48b:3');e('timing.objection',timing,nahman,'objection','48b:4')
horonq=q('horonq','48b:5',None,'Rava asks Rav Nahman why Beit Horon’s acquisition-for-transfer did not acquire.',voice='רבא')
feast=c('feast','48b:6','זימנין אמר ליה משום דסעודתו מוכחת עליו','At times Rav Nahman answers that the feast reveals the intent.',holder='רב נחמן',scope='First reported answer')
el=c('el','48b:6',"וזימנין אמר ליה ר' אליעזר היא דאמר אפילו ויתור אסור במודר הנאה",'At other times he assigns that teaching to Rabbi Eliezer, who prohibits even freely conceded benefit.',holder='רב נחמן',scope='Second reported answer, not flattened into first; embedded legal position attributed to Eliezer')
e('feast.answer',feast,horonq,'answer','48b:6');e('el.answer',el,horonq,'answer','48b:6')
allq=q('allq','48b:7','כל לאיתויי מאי לאו לאתויי הא מילתא דשדיא בכיפי','Does all in the sages’ invalid-gift rule include this flax-related conditional transfer?')
last=c('last','48b:7','לא לאתויי לישנא בתראה דשמעתיה דרבא','The reply instead includes the latter version of Rava’s Beit Horon teaching.',scope='Deflects proposed exclusion of conditional transfer; no explicit final adjudication of all earlier objections')
e('last.answer',last,allq,'answer','48b:7')
for row in a.records:
    if row['id']==clothq:
        row['content']['answer_set_status']='none'
        row['uncertainty']=['Rav Ashi’s cloth-retention objection has no explicit reply here; later Beit Horon replies target a different objection.']
a.add('chapter.u','utterances',dict(textual_voice='anonymous textual marker',discourse_role='chapter conclusion',composition='atomic'),[a.ev('48b:8')])
a.add('chapter.a','attributions',dict(surface='',role='anonymous',candidates=[],scope=a.PREFIX+'chapter.u',transmission_chain=[]),[a.ev('48b:8')],[a.PREFIX+'chapter.u'])
a.notes={
'47b:5':'Reread all three directional formulas and permission for wider communal property.',
'48a:1':'Reread town prohibition, all national/town examples and compressed president-assignment clause.',
'48a:2':'Reread Yehuda recipient/formality distinction, sages disagreement and Galilee historical exemption.',
'48a:3':'Reread prohibition question and Sheshet assignment-as-remedy clarification.',
'48a:4':'Reread full repeated acquisition dispute as separate occurrence.',
'48a:5':'Reread Yehuda attributed Galilee characterization and ancestral assignment rationale.',
'48a:6':'Reread genuine third-party food permission and Beit Horon three-generation narrative/gift limitation.',
'48a:7':'Reread recipient consecration test, giver protest, recipient blame objection and sages general rule.',
'48a:8':'Reread apparent contradiction and explicit later-conduct-reveals-intent reconstruction.',
'48a:9':'Reread first Rava version distinguishing explicit only-purpose from recipient discretion.',
'48a:10':'Reread explicit alternate Rava version making feast context sufficient despite wording.',
'48b:1':'Reread son conduct verbatim, scholar-grandson question, conditional transfer and legal-effect question.',
'48b:2':'Reread collective Pumbedita no-acquisition position.',
'48b:3':'Reread Nahman cloth-based acquisition position.',
'48b:4':'Reread Ashi unanswered cloth-retention objection and separate immediate/delayed timing objection.',
'48b:5':'Reread Rava Beit Horon challenge to Nahman.',
'48b:6':'Reread two alternating Nahman answers, not one harmonized response.',
'48b:7':'Reread all-inclusion challenge and answer targeting latter Rava version, not broad final ruling.',
'48b:8':'Reread partners chapter-ending marker, no legal claim invented.'}
if __name__=='__main__':a.save()
