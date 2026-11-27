"""Intake085: one capped manual window,61b5–62b4; all new records unreviewed."""
import author_continuation_024 as b
from pathlib import Path
import hashlib,json
a=b.a;r=a.r;HERE=Path(__file__).resolve().parent
BASE='26acf7ff70ba33f249b8e3f957edac6a932ce1d32c7e84996ad3b239e74bab01'
assert r.read(a.JOB/'CURRENT.json')['snapshot_sha256']==BASE
assert r.read(a.JOB/'OWNER.json')=={'epoch':3,'owner':'L04/nedarim_resume_20261126'}
start=r.read(HERE/'START_INTAKE085_066.json')
for name,digest in start['actual_nine_file_hashes'].items():assert hashlib.sha256((a.ROOT.parent/name).read_bytes()).hexdigest()==digest
assert a.meta['source_sha256']==start['source_sha256']
a.records=[];a.notes={};a.PREFIX='nd.r066.';a.OUTPUT='continuation_066b.json'
c=a.c;e=a.edge;q=b.q
def attributed(key,role='quoted_authority',chain=()):
    row=next(x for x in a.records if x['id']==a.PREFIX+key+'.a')
    row['content']['role']=role;row['content']['transmission_chain']=list(chain)
a.structure('harvest',['61b:'+str(i) for i in range(5,10)]+['62a:1','62a:2','62a:3'],'Seasonal vow endpoints and post-harvest fruit: rules and narrated applications')
a.structure('crown',['62a:'+str(i) for i in range(4,12)],'Tarfon narrative, Torah honor and contextual self-identification')
a.structure('privileges',['62a:12']+['62b:'+str(i) for i in range(1,5)],'Scholarly priority, tax statements and wood-sale objection')

harvest=c('harvest','61b:5','עד הקציר עד הבציר עד המסיק אינו אסור אלא עד שיגיע','Until grain harvest, grape harvest or olive harvest prohibits only until the named harvest begins.',composition='composite',scope='Three expressly listed harvest-event formulas')
fixed=c('fixed','61b:5','זה הכלל כל שזמנו קבוע ואמר עד שיגיע אסור עד שיגיע אמר עד שיהא אסור עד שיצא','For a fixed-time event, until it arrives ends at arrival, whereas until it shall be continues until departure.',composition='composite',scope='Two formulations and endpoints under explicit fixed-time condition')
unfixed=c('unfixed','61b:5','וכל שאין זמנו קבוע בין אמר עד שיהא בין אמר עד שיגיע אינו אסור אלא עד שיגיע','For an event without a fixed time, either formula prohibits only until its arrival.',composition='composite',scope='Both formulations under contrasting unfixed-time condition')
e('unfixed.distinction',unfixed,fixed,'distinction','61b:5','וכל שאין זמנו קבוע בין אמר עד שיהא בין אמר עד שיגיע אינו אסור אלא עד שיגיע')
summer=c('summer','61b:6','עד הקיץ עד שיהא הקיץ עד שיתחילו העם להכניס בכלכלות','Until summer or until summer shall be lasts until people begin bringing produce in baskets.',composition='composite',scope='Two קיץ formulas with shared activity-based endpoint')
summerend=c('summerend','61b:6','עד שיעבור הקיץ עד שיקפילו המקצועות','Until summer passes lasts until the מקצועות are folded away.',scope='Exact implement term retained, without choosing a modern technical identification')
figbasket=c('figbasket','61b:7','תנא כלכלה שאמרו כלכלה של תאנים ולא כלכלה של ענבים','An anonymous teaching specifies fig baskets, not grape baskets.',composition='composite',scope='Anonymous quoted authority; no named citing teacher supplied')
figs=c('figs','61b:7','תניא הנודר מפירות הקיץ אין אסור אלא בתאנים','The anonymous baraita limits a vow against summer fruit to figs.',scope='Distinct fruit-category rule, not identical to the preceding temporal endpoint')
grapes=c('grapes','61b:7','רשב"ג אומר ענבים בכלל תאנים','Rabban Shimon ben Gamliel includes grapes with figs.',holder='רשב"ג',scope='Named contrary inclusion in summer-fruit category')
attributed('grapes')
e('basket.qualification',figbasket,summer,'qualification','61b:7','תנא כלכלה שאמרו כלכלה של תאנים ולא כלכלה של ענבים');e('grapes.objection',grapes,figs,'objection','61b:7','רשב"ג אומר ענבים בכלל תאנים')
whyfig=q('whyfig','61b:8','מאי טעמא דתנא קמא','What is the first tanna’s reason?')
hand=c('hand','61b:8','קסבר תאנים מיקצצן בידא ענבים לא מיקצצן בידא','The first tanna distinguishes figs cut by hand from grapes not cut by hand.',holder='תנא קמא',composition='composite',scope='Anonymous tanna identified only by local discourse role')
grapehand=c('grapehand','61b:8','רשב"ג סבר ענבים נמי כי מירדדן מיקצצן בידא','Rabban Shimon ben Gamliel says grapes too are cut by hand when מירדדן.',holder='רשב"ג',scope='Conditional hand-picking rationale; exact qualifying term retained without overtranslation')
attributed('hand');attributed('grapehand')
e('hand.answer',hand,whyfig,'answer','61b:8','קסבר תאנים מיקצצן בידא ענבים לא מיקצצן בידא');e('grapehand.support',grapehand,grapes,'support','61b:8','רשב"ג סבר ענבים נמי כי מירדדן מיקצצן בידא')
repeated=c('repeated','61b:9','עד שיעבור הקיץ עד שיכפלו המקצועות','The discussion repeats the summer-end rule using folding of the מקצועות.',scope='Distinct repeated Mishnah lemma occurrence, not deduplicated into61b6')
majority=c('majority','61b:9','תנא עד שיכפילו רוב המקצועות','An anonymous teaching specifies folding most of the מקצועות.',scope='Majority threshold, not all implements required')
e('repeated.quotation',repeated,summerend,'quotation','61b:9','עד שיעבור הקיץ עד שיכפלו המקצועות');e('majority.qualification',majority,repeated,'qualification','61b:9','תנא עד שיכפילו רוב המקצועות')
theft=c('theft','62a:1','תנא הוקפלו רוב המקצועות מותרות משום גזל','An anonymous teaching permits taking the remaining fruit without theft after most מקצועות are folded.',conditions=['Most מקצועות have been folded'],scope='Permission with respect to theft, not an unrestricted all-purpose exemption')
tithe=c('tithe','62a:1','ופטורות מן המעשרות','That remaining fruit is exempt from tithes.',conditions=['Most מקצועות have been folded'],scope='Second outcome under the preceding condition',extra=[('62a:1','הוקפלו רוב המקצועות')])
visit=c('visit','62a:2','רבי ורבי יוסי בר רבי יהודה איקלעו לההוא אתרא בזמן שהוקפלו רוב המקצועות','Rabbi and Rabbi Yosei son of Rabbi Yehuda arrive where most מקצועות have been folded.',composition='composite',scope='Named participants and seasonal condition in narrative')
eat=c('eat','62a:2','רבי הוה קא אכיל רבי יוסי בר ר\' יהודה לא אכיל','Rabbi eats, while Rabbi Yosei son of Rabbi Yehuda does not.',composition='composite',scope='Explicit named divergent practices; no name-order inference')
ownerq=q('ownerq','62a:2','אתא מרהון אמר להו אמאי לא אכלי רבנן','The owner arrives and asks why the sages do not eat.',voice='anonymous owner')
ownreason=c('ownreason','62a:2','הוקפלו רוב המקצועות הוא','The owner states that most מקצועות have already been folded.',scope='Owner’s stated seasonal reason for inviting them to eat')
refusal=c('refusal','62a:2','ואף על פי כן לא אכיל ר\' יוסי בר ר\' יהודה','Rabbi Yosei son of Rabbi Yehuda nevertheless continues not to eat.',scope='Narrated refusal despite the owner’s words')
facesave=c('facesave','62a:2','קסבר משום סניות מילתא הוא דקאמר הדין גברא','He understands the owner as speaking because the situation is embarrassing.',holder="ר' יוסי בר ר' יהודה",scope='Narrator’s explanation of Yosei’s suspicion; not a proven statement of the owner’s actual intent')
e('facesave.answer',facesave,ownerq,'answer','62a:2','קסבר משום סניות מילתא הוא דקאמר הדין גברא');e('facesave.support',facesave,refusal,'support','62a:2','קסבר משום סניות מילתא הוא דקאמר הדין גברא')
hama=c('hama','62a:3','רבי חמא בר רבי חנינא איקלע לההוא אתרא בזמן שהוקפלו רוב המקצועות הוה קאכיל יהיב לשמעיה לא אכיל','Rabbi Hama son of Rabbi Hanina eats in such a place and offers fruit to his attendant, who does not eat.',composition='composite',scope='Separate narrative with same majority-folding condition; no conflation with preceding pair')
urge=c('urge','62a:3','אמר ליה אכול','Hama tells the attendant to eat.',holder='רבי חמא בר רבי חנינא',scope='Speaker of the immediate instruction, not original authority of quoted rule')
yoseitheft=c('yoseitheft','62a:3','כך אמר לי רבי ישמעאל בר רבי יוסי משום אביו הוקפלו רוב המקצועות מותרות משום גזל','Hama cites Rabbi Yishmael son of Rabbi Yosei reporting his father: after most מקצועות are folded, the fruit is permitted with respect to theft.',holder='רבי יוסי',conditions=['Most מקצועות have been folded'],scope='Quoted original authority Rabbi Yosei, transmitted by his son to Hama')
yoseitithe=c('yoseitithe','62a:3','ופטורות מן המעשר','The same report exempts the fruit from tithe.',holder='רבי יוסי',conditions=['Most מקצועות have been folded'],scope='Continuation of explicitly transmitted rule',extra=[('62a:3','כך אמר לי רבי ישמעאל בר רבי יוסי משום אביו הוקפלו רוב המקצועות')])
for key in ['yoseitheft','yoseitithe']:attributed(key,chain=['רבי חמא בר רבי חנינא','רבי ישמעאל בר רבי יוסי','רבי יוסי'])
e('yosei.support',yoseitheft,urge,'support','62a:3','כך אמר לי רבי ישמעאל בר רבי יוסי משום אביו הוקפלו רוב המקצועות מותרות משום גזל')

capture=c('capture','62a:4','ר\' טרפון אשכחיה ההוא גברא בזמן שהוקפלו המקצועות דקאכיל אחתיה בשקא ושקליה ואמטייה למשדיה בנהרא','A man finds Rabbi Tarfon eating after the מקצועות are folded, puts him in a sack and carries him to throw him into the river.',composition='composite',scope='Narrative threat; motive clarified62a6, not assumed legitimate theft punishment')
cry=c('cry','62a:4','אמר לו אוי לו לטרפון שזה הורגו','Tarfon cries that this man is killing Tarfon.',holder="ר' טרפון",scope='Self-identifying speech in danger')
escape=c('escape','62a:4','שמע ההוא גברא שבקיה וערק','Hearing this, the man releases him and flees.',composition='composite',scope='Narrated response to recognition')
regret=c('regret','62a:4','אמר רבי אבהו משום ר\' חנניה בן גמליאל כל ימיו של אותו צדיק היה מצטער על דבר זה','Rabbi Abbahu reports Rabbi Hananya ben Gamliel that Tarfon regretted the incident all his life.',holder="ר' חנניה בן גמליאל",scope='Explicit reported biographical claim, not Abbahu as original holder')
attributed('regret',chain=['רבי אבהו',"ר' חנניה בן גמליאל"])
crowncry=c('crowncry','62a:4','אמר אוי לי שנשתמשתי בכתרה של תורה','Tarfon says he regrets using the crown of Torah.',holder="ר' טרפון",scope='Tarfon’s quoted regret within Abbahu/Hananya report')
attributed('crowncry',chain=['רבי אבהו',"ר' חנניה בן גמליאל","ר' טרפון"])
crown=c('crown','62a:5','ואמר רבה בר בר חנה אמר ר\' יוחנן כל המשתמש בכתרה של תורה נעקר מן העולם','Rabbi Yohanan, reported by Rabbah bar bar Hana, says that one exploiting Torah’s crown is uprooted from the world.',holder="ר' יוחנן",scope='Attributed ethical warning; transmitter is not independent original holder')
attributed('crown',chain=['רבה בר בר חנה',"ר' יוחנן"])
vessels=c('vessels','62a:5','קל וחומר ומה בלשצר שנשתמש בכלי קודש שנעשו כלי חול','The argument begins with Belshazzar using sacred vessels that had become profane.',holder="ר' יוחנן",scope='First premise of the reported a-fortiori argument')
profanation=c('profanation','62a:5','שנאמר (יחזקאל ז, כב) ובאו בה פריצים וחיללוה כיון שפרצום נעשו חול','The Ezekiel citation is interpreted to mean that intrusion by profaners made the vessels profane.',holder="ר' יוחנן",scope='Scriptural explanation within reported argument, not modern property advice')
killed=c('killed','62a:5','נעקר מן העולם דכתיב (דניאל ה, ל) בה בליליא קטיל בלשצר','The argument cites Daniel’s report of Belshazzar being killed that night.',holder="ר' יוחנן",scope='Reported scriptural consequence supporting ethical analogy')
greater=c('greater','62a:5','המשתמש בכתרה של תורה שהוא חי וקיים לעולם על אחת כמה וכמה','It infers all the more against exploiting Torah’s crown, which endures forever.',holder="ר' יוחנן",scope='A-fortiori conclusion and stated greater sanctity premise')
for key in ['vessels','profanation','killed','greater']:attributed(key,chain=['רבה בר בר חנה',"ר' יוחנן"])
e('vessels.support',vessels,greater,'support','62a:5','קל וחומר ומה בלשצר שנשתמש בכלי קודש שנעשו כלי חול');e('killed.support',killed,greater,'support','62a:5','נעקר מן העולם דכתיב (דניאל ה, ל) בה בליליא קטיל בלשצר');e('greater.support',greater,crown,'support','62a:5','המשתמש בכתרה של תורה שהוא חי וקיים לעולם על אחת כמה וכמה')
attackq=q('attackq','62a:6','ורבי טרפון כיון דכי אכיל דהוקפלו רוב המקצועות הוה אמאי צעריה ההוא גברא','Why did the man threaten Tarfon if most מקצועות had already been folded?')
mistake=c('mistake','62a:6','משום דההוא הוו גנבי ליה ענבי כולה שתא וכיון דאשכחיה לר\' טרפון סבר היינו דגנבן','Grapes had been stolen from the man throughout the year, and he mistook Tarfon for the thief.',composition='composite',scope='Narrative explanation distinguishes mistaken identity from the seasonal permission')
regretq=q('regretq','62a:6','אי הכי אמאי ציער נפשיה','Why then did Tarfon reproach himself?')
wealth=c('wealth','62a:6','משום דרבי טרפון עשיר גדול הוה והוה ליה לפייסו בדמים','The reply says Tarfon was very wealthy and could have appeased the man with money.',composition='composite',scope='Specific alternate means of escape in narrative, not general prohibition of self-identification')
e('mistake.answer',mistake,attackq,'answer','62a:6','משום דההוא הוו גנבי ליה ענבי כולה שתא וכיון דאשכחיה לר\' טרפון סבר היינו דגנבן');e('wealth.answer',wealth,regretq,'answer','62a:6','משום דרבי טרפון עשיר גדול הוה והוה ליה לפייסו בדמים')
motives=c('motives','62a:7','תניא (דברים ל, כ) לאהבה את ה\' אלהיך לשמוע בקולו ולדבקה בו שלא יאמר אדם אקרא שיקראוני חכם אשנה שיקראוני רבי אשנן שאהיה זקן ואשב בישיבה','An anonymous baraita forbids making study a means to be called wise, called Rabbi, or become an elder seated in the academy, citing love of God.',composition='composite',scope='All three explicitly listed prestige motives; anonymous quoted authority retained')
love=c('love','62a:8','אלא למד מאהבה וסוף הכבוד לבא','The baraita instructs study from love, with honor eventually following.',composition='composite',scope='Positive motive and promised consequence in anonymous teaching')
finger=c('finger','62a:8','שנאמר (משלי ז, ג) קשרם על אצבעותיך כתבם על לוח לבך','It cites binding the teachings on the fingers and writing them on the heart.',composition='composite',scope='First of three scriptural support occurrences')
pleasant=c('pleasant','62a:8','ואומר (משלי ג, יז) דרכיה דרכי נועם','It also cites the ways of pleasantness verse.',scope='Second support occurrence')
tree=c('tree','62a:8','ואומר (משלי ג, יח) עץ חיים היא למחזיקים בה ותומכיה מאושר','It cites Torah as a tree of life and its supporters as fortunate.',composition='composite',scope='Third support occurrence, both clauses retained')
for key,ident,quote in [('finger',finger,'שנאמר (משלי ז, ג) קשרם על אצבעותיך כתבם על לוח לבך'),('pleasant',pleasant,'ואומר (משלי ג, יז) דרכיה דרכי נועם'),('tree',tree,'ואומר (משלי ג, יח) עץ חיים היא למחזיקים בה ותומכיה מאושר')]:e(key+'.support',ident,love,'support','62a:8',quote)
purpose=c('purpose','62a:9','רבי אליעזר בר ר\' צדוק אומר עשה דברים לשם פעלם ודבר בהם לשמם','Rabbi Eliezer son of Rabbi Tzadok instructs doing deeds for their Maker and discussing them for their own sake.',holder="רבי אליעזר בר ר' צדוק",composition='composite',scope='Two explicitly paired purpose instructions')
tools=c('tools','62a:9','אל תעשם עטרה להתגדל בהם ואל תעשם קורדום להיות עודר בו','He prohibits making them a crown for self-aggrandizement or a spade for material use.',holder="רבי אליעזר בר ר' צדוק",composition='composite',scope='Two source metaphors preserved as attributed instruction')
belsh=c('belsh','62a:9','וקל וחומר ומה בלשצר שלא נשתמש אלא בכלי קדש שנעשו כלי חול נעקר מן העולם המשתמש בכתרה של תורה על אחת כמה וכמה','His a-fortiori argument again contrasts Belshazzar’s fate for using desacralized vessels with exploiting Torah’s crown.',holder="רבי אליעזר בר ר' צדוק",composition='composite',scope='Separate repeated analogy occurrence and explicitly different quoted authority')
for key in ['purpose','tools','belsh']:attributed(key)
e('belsh.support',belsh,tools,'support','62a:9','וקל וחומר ומה בלשצר שלא נשתמש אלא בכלי קדש שנעשו כלי חול נעקר מן העולם המשתמש בכתרה של תורה על אחת כמה וכמה')
identify=c('identify','62a:10','אמר רבא שרי ליה לאיניש לאודועי נפשיה באתרא דלא ידעי ליה','Rava permits a person to identify himself where he is unknown.',holder='רבא',conditions=['Place where the person is not known'],scope='Contextual permission, not unrestricted self-praise')
ovadya=c('ovadya','62a:10','דכתיב (מלכים א יח, יב) ועבדך ירא את ה\' מנעוריו','Rava cites your servant has feared God from youth.',holder='רבא',scope='Rava’s act of citing support; quoted biblical speaker is not being identified as Rava')
tarfonq=c('tarfonq','62a:10','אלא קשיא דר\' טרפון','Tarfon’s incident is presented as a difficulty for the self-identification permission.',mode='challenged',scope='Explicit difficulty statement, not converted into a source-explicit interrogative')
againwealth=c('againwealth','62a:10','דעשיר גדול היה והוה ליה לפייסיה בדמים','The reply again cites Tarfon’s wealth and ability to appease with money.',composition='composite',scope='Separate repeated limitation; does not revoke Rava’s general unknown-place permission')
e('ovadya.support',ovadya,identify,'support','62a:10','דכתיב (מלכים א יח, יב) ועבדך ירא את ה\' מנעוריו');e('againwealth.answer',againwealth,tarfonq,'answer','62a:10','דעשיר גדול היה והוה ליה לפייסיה בדמים')
verseq=c('verseq','62a:11','רבא רמי כתיב ועבדך ירא את ה\' מנעוריו וכתיב (משלי כז, ב) יהללך זר ולא פיך','Rava sets self-identification as God-fearing against the command that another praise you, not your own mouth.',holder='רבא',mode='challenged',composition='composite',scope='Explicit two-verse contradiction statement; not labeled as an explicit interrogative')
known=c('known','62a:11','הא באתרא דידעי ליה הא באתרא דלא ידעי ליה','The reply distinguishes a place where he is known from one where he is unknown.',composition='composite',scope='Known place forbids self-praise; unknown place allows identification as stated62a10; no name-order mapping')
e('known.answer',known,verseq,'answer','62a:11','הא באתרא דידעי ליה הא באתרא דלא ידעי ליה')

priority=c('priority','62a:12','אמר רבא שרי ליה לצורבא מרבנן למימר צורבא מרבנן אנא שרו לי תיגראי ברישא','Rava permits a scholar to identify himself and request that his litigation be handled first.',holder='רבא',scope='Specific judicial-priority request, not permission to influence the merits')
priestanalogy=c('priestanalogy','62a:12','דכתיב (שמואל ב ח, יח) ובני דוד כהנים היו מה כהן נוטל בראש אף תלמיד חכם נוטל בראש','Rava’s derivation cites David’s sons as priests and analogizes scholarly priority to priestly priority.',holder='רבא',composition='composite',scope='Rava’s stated analogy, not a literal historical priesthood claim about David’s lineage')
priestq=q('priestq','62a:12','וכהן מנא לן','Where is priestly priority derived?')
sanctify=c('sanctify','62a:12','דכתיב (ויקרא כא, ח) וקדשתו כי את לחם (ה\') אלהיך הוא מקריב','The discussion cites sanctifying the priest because he offers God’s food.',scope='Anonymous derivation answer; parenthetical divine-name wording preserved')
school=c('school','62a:12','ותנא דבי רבי ישמעאל וקדשתו לכל דבר שבקדושה','The school of Rabbi Yishmael teaches that sanctify him applies to every sacred matter.',holder='תנא דבי רבי ישמעאל',scope='Quoted teaching authority distinguished from Rava’s earlier argument')
first=c('first','62b:1',None,'The school’s teaching specifies opening first, blessing first and taking a choice portion first.',holder='תנא דבי רבי ישמעאל',composition='composite',scope='Three explicit priority acts in cross-folio continuation',extra=[('62a:12','ותנא דבי רבי ישמעאל וקדשתו לכל דבר שבקדושה')])
attributed('school');attributed('first')
e('priestanalogy.support',priestanalogy,priority,'support','62a:12','דכתיב (שמואל ב ח, יח) ובני דוד כהנים היו מה כהן נוטל בראש אף תלמיד חכם נוטל בראש');e('sanctify.answer',sanctify,priestq,'answer','62a:12','דכתיב (ויקרא כא, ח) וקדשתו כי את לחם (ה\') אלהיך הוא מקריב');e('school.answer',school,priestq,'answer','62a:12','ותנא דבי רבי ישמעאל וקדשתו לכל דבר שבקדושה')
tax=c('tax','62b:2','אמר רבא שרי ליה לצורבא מרבנן למימר לא יהיבנא אכרגא','Rava permits a scholar to say he will not pay the tax.',holder='רבא',scope='Source’s legal claim in its historical context, not contemporary tax advice')
ezra=c('ezra','62b:2','דכתיב (עזרא ז, כד) מנדה בלו והלך לא שליט למירמא עליהון','Rava’s supporting citation prohibits imposing מנדה, בלו and הלך on them.',scope='Quoted biblical support; anonymous quotation distinct from Rava as citing authority')
kingtax=c('kingtax','62b:2','וא"ר יהודה מנדה זו מנת המלך','The speaker printed ר יהודה interprets מנדה as the king’s levy.',holder='ר יהודה',scope='Abbreviated title preserved without forcing Rav/Rabbi; first tax mapping')
headtax=c('headtax','62b:2','בלו זו כסף גולגלתא','The same speaker interprets בלו as the poll tax.',holder='ר יהודה',scope='Second tax mapping',extra=[('62b:2','וא"ר יהודה')])
arnona=c('arnona','62b:2','והלך זו ארנונא','The same speaker interprets הלך as ארנונא.',holder='ר יהודה',scope='Third tax mapping; technical levy name retained',extra=[('62b:2','וא"ר יהודה')])
for key in ['kingtax','headtax','arnona']:attributed(key)
e('ezra.support',ezra,tax,'support','62b:2','דכתיב (עזרא ז, כד) מנדה בלו והלך לא שליט למירמא עליהון')
fire=c('fire','62b:3','ואמר רבא שרי ליה לצורבא מרבנן למימר עבדא דנורא אנא לא יהיבנא אכרגא','Rava permits a scholar to say I am a servant of fire; I do not pay the tax.',holder='רבא',scope='Exact historically situated formula; not an assertion that the scholar actually worships fire')
fireq=q('fireq','62b:3','מ"ט','What is the reason for allowing this statement?')
lion=c('lion','62b:3','לאברוחי אריא מיניה קאמר','The answer interprets it as a statement intended to drive a lion away from himself.',scope='Source’s threat-avoidance metaphor explains permission; no unstated details of threat supplied')
e('lion.answer',lion,fireq,'answer','62b:3','לאברוחי אריא מיניה קאמר');e('lion.support',lion,fire,'support','62b:3','לאברוחי אריא מיניה קאמר')
wood=c('wood','62b:4','רב אשי הוה ליה ההוא אבא זבניה לבי נורא','Rav Ashi sells a woodland he owns to the house of fire.',composition='composite',scope='Narrated sale to בי נורא; not a general sale permission without the ensuing qualification')
objection=c('objection','62b:4','א"ל רבינא לרב אשי האיכא (ויקרא יט, יד) לפני עור לא תתן מכשול','Ravina challenges Rav Ashi with the prohibition against placing a stumbling block before the blind.',holder='רבינא',mode='challenged',scope='Source-explicit objection preserved as objection claim, without inventing a separate interrogative formulation')
heat=c('heat','62b:4','א"ל רוב עצים להסקה ניתנו','Rav Ashi replies that most wood is used for heating.',holder='רב אשי',scope='Majority-use answer to this sale objection, not a claim that no wood serves worship')
e('heat.answer',heat,objection,'answer','62b:4','א"ל רוב עצים להסקה ניתנו')

a.notes={
'61b:5':'Reread three harvest formulas and both fixed/unfixed-time rules with all arrival/departure conditions.',
'61b:6':'Reread both summer-arrival formulas and distinct summer-end implement-folding endpoint.',
'61b:7':'Reread fig-not-grape baskets, anonymous summer-fruit rule and Gamliel contrary grape inclusion.',
'61b:8':'Reread explicit reason question and both hand-picking explanations, preserving מירדדן qualifier.',
'61b:9':'Reread repeated summer-end lemma and explicit majority refinement as separate occurrence.',
'62a:1':'Reread anonymous majority-folding rule; theft permission and tithe exemption separate.',
'62a:2':'Reread both named visitors/practices, owner question/reason, continued refusal and Yosei inferred face-saving motive.',
'62a:3':'Reread Hama/attendant narrative and explicit Hama→Yishmael son of Yosei→Yosei chain for both legal outcomes; citer not original holder.',
'62a:4':'Reread capture/threat, Tarfon identification and release, Abbahu/Hananya report and embedded Tarfon lifelong regret quotation.',
'62a:5':'Reread Rabbah bar bar Hana/Yohanan transmission, warning, profaned-vessel premise, both biblical citations and a-fortiori conclusion.',
'62a:6':'Reread both why questions, mistaken grape-thief explanation and wealthy-ransom alternative.',
'62a:7':'Reread anonymous baraita, Deuteronomy citation and all three prestige motives.',
'62a:8':'Reread love-based study and eventual honor, all three Proverbs supports and each quoted clause.',
'62a:9':'Reread Eliezer son of Tzadok two purpose instructions, crown/spade metaphors and separate repeated Belshazzar argument.',
'62a:10':'Reread Rava unknown-place permission and biblical support, Tarfon challenge and repeated wealth limitation.',
'62a:11':'Reread Rava two-verse tension and known/unknown locality resolution using previous explicit context, not word-order inference.',
'62a:12':'Reread Rava judicial-priority request, David-priest analogy, explicit derivation question, sanctification verse and distinct school-of-Yishmael quoted authority.',
'62b:1':'Reread all three priority acts continuing the school baraita across folio.',
'62b:2':'Reread Rava tax statement, Ezra support and all three printed ר יהודה mappings; historical context and abbreviated title retained.',
'62b:3':'Reread Rava exact servant-of-fire formula, reason question and lion-avoidance answer without inventing actual worship.',
'62b:4':'Reread Ashi woodland sale, Ravina stumbling-block objection and majority-heating answer; next62b5 starts a new Mishnah.'}
if __name__=='__main__':
    assert len(a.notes)==21<=30
    a.save()
    proposal=r.read(a.JOB/'staging'/a.OUTPUT);before=r.current(a.JOB)
    assert r.sha(r.encoded(before))==BASE
    after=r.validate_apply(before,proposal,a.ss,a.meta)
    previous={x['id']:x for x in before['records']};updated={x['id']:x for x in after['records']}
    assert all(updated[k]==v for k,v in previous.items())
    assert all(not x['ml_eligible'] for x in after['records'])
    for row in after['records']:
        if row['release_state']=='valid' and row['layer']=='attributions' and row['content']['scope'] in updated:
            assert updated[row['content']['scope']]['release_state']=='valid'
    report=r.report(after,a.ss)
    assert set(report['completed_by_layer'].values())=={1083}
    assert set(report['next_unprocessed_by_layer'].values())=={'Nedarim 62b:5'}
    receipt=dict(status='PREVALIDATED_UNREVIEWED_CAPPED_WINDOW',base_snapshot=BASE,proposal_sha256=r.sha(r.encoded(proposal)),new_segments=21,scope=['Nedarim 61b:5','Nedarim 62b:4'],new_records=len(proposal['records']),all_prior_records_unchanged=True,schema_exact_source_spans_graph_and_embedded_scope_closure=True,all_eight_layers=1083,next='Nedarim 62b:5',all_ml_eligible_false=True,independent_review_inherited=False,freeze_after_this_proposal=True)
    r.immutable(HERE/'PREVALIDATION_INTAKE085_066b.json',r.encoded(receipt));print(json.dumps(receipt,indent=2))
