"""Manual reading of special preparations and Rabbi/Bar Kappara narratives."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r052.';a.OUTPUT='continuation_052.json'
c=a.c;e=a.edge;q=b.q
a.structure('egg',['50b:6','50b:7','50b:8','50b:9'],'Egg preparation, Shmuel narrative and fig preparations')
a.structure('feast',['50b:10','50b:11']+['51a:'+str(i) for i in range(1,8)],'Rabbi and Bar Kappara wedding narratives and Ben Elasa haircut')
a.structure('gourd',['51a:8','51a:9'],'Roasted-gourd definition and explicit refutation of Rav Ashi')
eggq=q('eggq','50b:6','מאי ביצה טורמיטא','What is ביצה טורמיטא?')
value=c('value','50b:6','אמר שמואל עבדא דעביד לה שוי אלפא דינרי','Shmuel says a servant who can prepare it is worth a thousand dinars.',holder='שמואל',scope='Attributed valuation of preparation skill')
prepare=c('prepare','50b:6','ומעייל לה אלפא זימני במיא חמימי ואלפא זימני במיא קרירי עד דמתזוטרא כי היכי דבלעיתה','The preparation alternates a thousand immersions in hot water and a thousand in cold until the egg shrinks enough to swallow.',holder='שמואל',composition='composite',scope='Ancient procedure as reported by source, not treatment instructions')
diagnose=c('diagnose','50b:6','ואם אית כיבא סריך עלה וכד נפקא ואתיא ידע אסיא מאי סמא מתבעי ליה ובמאי מתי','The account says an internal lesion adheres to it, enabling a physician after its passage to identify the required medicine and means of healing.',holder='שמואל',composition='composite',scope='Attributed ancient diagnostic explanation; final ובמאי מתי retained in evidence, not modern validation')
e('prepare.answer',prepare,eggq,'answer','50b:6')
selftest=c('selftest','50b:7',None,'Shmuel examines himself using a קולחא, to the point that his household tears its hair over him.',composition='composite',scope='Reported self-examination and family distress; instrument label preserved without clinical recommendation')
figrule=c('figrule','50b:8','תנן התם היה עושה בכלופסין לא יאכל בבנות שבע בבנות שבע לא יאכל בכלופסין','The cited Mishnah prohibits a worker occupied with כלופסין from eating benot sheva, and vice versa.',composition='composite',scope='Two reciprocal fruit-work limitations')
figq=q('figq','50b:8','מאי כלופסין','What are כלופסין?')
fig=c('fig','50b:8','מינא דתאיני דעבדין מנהון לפדי','They are a fig variety used to make לפדי.',scope='Source’s definition; preparation label retained')
e('fig.answer',fig,figq,'answer','50b:8')
training=c('training','50b:9','ההוא גברא דיהב עבדא לחבריה לאגמוריה אלפא מיני לפדי אגמריה תמני מאה אזמניה לדינא לקמיה דרבי','A man commissions training of his servant in a thousand kinds of לפדי; only eight hundred are taught, and he brings suit before Rabbi.',composition='composite',scope='Contract, shortfall and litigation; no unreported adjudication supplied')
loss=c('loss','50b:9','אמר רבי אבותינו אמרו נשינו טובה אנו אפילו בעינינו לא ראינו','Rabbi says earlier generations spoke of forgetting goodness, while his generation has not even seen it.',holder='רבי',composition='composite',scope='Rabbi’s lament, not a ruling on the training contract')
feast=c('feast','50b:10','רבי עבד ליה הלולא לר"ש ברבי כתב על בית גננא עשרין וארבעה אלפין ריבואין דינרין נפקו על בית גננא דין ולא אזמניה לבר קפרא','Rabbi makes a wedding for Rabbi Shimon his son, records expenditure of twenty-four thousand myriads of dinars on the wedding house, and does not invite Bar Kappara.',composition='composite',scope='Narrated occasion, exact magnitude and exclusion')
first=c('first','50b:10','אמר ליה אם לעוברי רצונו כך לעושי רצונו על אחת כמה וכמה','Bar Kappara says that if those who transgress God’s will receive so much, those who fulfill it all the more.',holder='בר קפרא',mode='conditional',scope='Attributed rebuke by a-fortiori rhetoric before invitation')
invite=c('invite','50b:10',('אזמניה',1),'Rabbi then invites Bar Kappara.',scope='Narrative reversal of exclusion; second literal occurrence selected')
second=c('second','50b:10','אמר לעושי רצונו בעולם הזה כך לעוה"ב עאכ"ו','Bar Kappara now says that if those fulfilling God’s will receive so much in this world, all the more in the world to come.',holder='בר קפרא',mode='conditional',scope='Changed a-fortiori formulation after invitation')
e('second.correction',second,first,'correction','50b:10')
laughter=c('laughter','50b:11','יומא דמחייך ביה רבי אתיא פורענותא לעלמא','The narrator says calamity comes to the world on a day Rabbi laughs.',scope='Narrative supernatural premise, not endorsed causal fact')
bargain=c('bargain','50b:11','א"ל לבר קפרא לא תבדיחן ויהיבנא לך ארבעין גריוי חיטי','Rabbi offers Bar Kappara forty measures of wheat if he does not make him laugh.',holder='רבי',mode='conditional',scope='Personal bargain motivated by preceding narrative premise')
measure=c('measure','51a:1','דכל גריוא דבעינא שקילנא','Bar Kappara stipulates that he may take whichever measure he wants.',holder='בר קפרא',scope='Speech continues from50b11 אמר ליה ליחזי מר',extra=[('50b:11','א"ל ליחזי מר')])
basket=c('basket','51a:1','שקל דיקולא רבה חפייה כופרא וסחפיה על רישיה ואזל ואמר ליה ליכיל לי מר ארבעין גריוי חיטי דרשינא בך אחוך רבי','Bar Kappara covers a large basket with pitch, puts it on his head, asks for the promised forty measures, and makes Rabbi laugh.',composition='composite',scope='Comic narrative sequence; explicit requested payment')
warning=q('warning','51a:1','א"ל לאו אזהרתך דלא תבדחן','Did Rabbi not warn him not to make him laugh?',voice='רבי')
pay=c('pay','51a:1','א"ל חיטי דרשינא קא נסיבנא','Bar Kappara replies that he is merely collecting the wheat owed him.',holder='בר קפרא',scope='Comic defense within bargain narrative')
e('pay.answer',pay,warning,'answer','51a:1')
forecast=c('forecast','51a:2','א"ל בר קפרא לברתיה דרבי למחר שתינא חמרא בריקודא דאבוך ובקירקני דאמך','Bar Kappara tells Rabbi’s daughter that tomorrow he will drink wine with her father dancing and her mother attending.',holder='בר קפרא',composition='composite',scope='Narrative forecast; precise בקירקני preserved without over-specific physical description')
elasa=c('elasa','51a:2','בן אלעשה חתניה דרבי הוה ועשיר גדול הוה אזמניה לבי הילולא דרבי שמעון ברבי','Ben Elasa is Rabbi’s wealthy son-in-law and is invited to Rabbi Shimon’s wedding.',composition='composite',scope='Relationship, wealth and occasion explicitly narrated')
toevaq=q('toevaq','51a:3','א"ל בר קפרא לרבי מאי (ויקרא כ, יג) תועבה','Bar Kappara asks Rabbi the meaning of תועבה.',voice='בר קפרא')
reject=c('reject','51a:3','כל דא"ל רבי דהכין הוא תועבה פרכה בר קפרא','Bar Kappara refutes each explanation Rabbi gives.',scope='Answers are not quoted; their content is not invented')
pour=c('pour','51a:3','א"ל פרשיה את א"ל תיתי דביתכי תירמי לי נטלא אתת רמיא ליה א"ל לר\' קום רקוד לי דאימר לך','Rabbi asks Bar Kappara to explain; Bar Kappara demands that Rabbi’s wife pour a cup and Rabbi dance before he gives his explanation.',composition='composite',scope='Explicit exchange and conditions; wife’s pouring occurs in the quoted sequence')
toeva=c('toeva','51a:3','הכי אמר רחמנא תועבה תועה אתה בה','Bar Kappara interprets תועבה as תועה אתה בה, you stray in it.',holder='בר קפרא',scope='Attributed wordplay, not historical etymology')
e('toeva.answer',toeva,toevaq,'answer','51a:3')
tevelq=q('tevelq','51a:4','לכסא אחרינא א"ל מאי (ויקרא יח, כג) תבל','At another cup he asks the meaning of תבל.',voice='בר קפרא')
repeat=c('repeat','51a:4','א"ל כי עניינא קדמאה א"ל עיביד לי דאומר לך עבד','The prior arrangement is invoked again and performed before the explanation.',scope='Narrative repetition of service/dancing condition, details supplied by preceding segment')
tevel=c('tevel','51a:4','אמר ליה תבל הוא תבלין יש בה מי שניא הדא ביאה מן כולהון ביאות','Bar Kappara plays on תבל as seasoning, rhetorically asking what distinguishes this intercourse from others.',holder='בר קפרא',scope='Attributed rhetorical wordplay on the cited prohibition; not permissive ruling')
e('tevel.answer',tevel,tevelq,'answer','51a:4')
zimaq=q('zimaq','51a:5','אמר ליה ומאי (ויקרא יח, יז) זימה','He asks the meaning of זימה.',voice='בר קפרא')
zima=c('zima','51a:5','אמר ליה עיביד כי עניינא קדמאה עבד ואמר ליה זו מה היא','After the prior condition is performed again, Bar Kappara explains זימה through זו מה היא.',holder='בר קפרא',composition='composite',scope='Repeated narrative condition plus exact wordplay; no additional unstated interpretation')
leave=c('leave','51a:5','לא יכיל בן אלעשה למיסבל קם ונפק הוא ואינתתיה מתמן','Ben Elasa cannot bear it and leaves with his wife.',composition='composite',scope='Narrative reaction without inventing specific unstated motive')
e('zima.answer',zima,zimaq,'answer','51a:5')
elasq=q('elasq','51a:6','מאי בן אלעשה','What is the cited matter of Ben Elasa?')
hair=c('hair','51a:6','דתניא לא לחנם פיזר בן אלעשה את מעותיו אלא להראות בהן תספורת של כ"ג','A baraita says Ben Elasa spent his money to display the high priest’s haircut.',scope='Attributed reason for spending; distinct from the wedding departure')
e('hair.answer',hair,elasq,'answer','51a:6')
cut=c('cut','51a:7','דכתיב (יחזקאל מד, כ) כסום יכסמו את ראשיהם תנא כעין לולינית','The teaching cites Ezekiel’s cutting instruction and describes the style as like לולינית.',scope='Scriptural citation and technical style label')
cutq=q('cutq','51a:7','מאי לולינית','What is לולינית?')
yehuda=c('yehuda','51a:7','א"ר יהודה תספרתא יחידתא','The speaker printed as ר יהודה describes it as a distinctive haircut.',holder='ר יהודה',scope='Printed abbreviated title preserved without forcing Rav versus Rabbi')
how=q('how','51a:7','היכי דמי','What does this haircut look like?')
tips=c('tips','51a:7','אמר רבא ראשו של זה בצד עיקרו של זה והיינו תספורת של כהן גדול','Rava describes one hair’s tip alongside another’s root, identifying this as the high priest’s haircut.',holder='רבא',composition='composite',scope='Explicit physical description and identification')
e('yehuda.answer',yehuda,cutq,'answer','51a:7');e('tips.answer',tips,how,'answer','51a:7')
gourdq=q('gourdq','51a:8','מאי דלעת הרמוצה','What is דלעת הרמוצה?')
shmuel=c('shmuel','51a:8','אמר שמואל קרא קרקוזאי','Shmuel identifies it as קרא קרקוזאי.',holder='שמואל',scope='Named gourd variety retained without speculative translation')
ashi=c('ashi','51a:8','רב אשי אמר דלעת הטמונה ברמץ','Rav Ashi identifies it as a gourd buried in hot ashes.',holder='רב אשי',mode='rejected',scope='Explicitly refuted in next segment')
nehemya=c('nehemya','51a:9','איתיביה רבינא לרב אשי רבי נחמיה אומר דלעת ארמית היא דלעת המצרית כלאים עם היונית כלאים עם הרמוצה','Ravina objects to Rav Ashi from Rabbi Nehemya: the Aramean gourd is the Egyptian gourd, and is a mixed species with the Greek and with the remutza.',holder='רבי נחמיה',composition='composite',scope='Three botanical classifications quoted by Ravina, implying remutza is a variety rather than a cooking method')
refute=c('refute','51a:9','תיובתא','The discussion concludes that Rav Ashi’s explanation is refuted.',scope='Explicit local refutation; not a general rejection of every Rav Ashi position')
e('shmuel.answer',shmuel,gourdq,'answer','51a:8');e('ashi.answer',ashi,gourdq,'answer','51a:8');e('nehemya.objection',nehemya,ashi,'objection','51a:9');e('refute.correction',refute,ashi,'correction','51a:9')
a.notes={
'50b:6':'Reread egg lemma/question, Shmuel skill valuation, alternating water procedure and attributed diagnostic rationale.',
'50b:7':'Reread Shmuel self-test and household distress as ancient narrative, not modern advice.',
'50b:8':'Reread reciprocal worker-fruit exclusions and fig definition question/answer.',
'50b:9':'Reread 1000/800 training shortfall and Rabbi lament; no litigation ruling stated.',
'50b:10':'Reread wedding expenditure magnitude, exclusion/invitation and two changed Bar Kappara a-fortiori formulations.',
'50b:11':'Reread calamity premise and forty-measure bargain, following speech continued51a1.',
'51a:1':'Reread chosen measure, pitch basket, comic payment demand, laughter, warning and reply.',
'51a:2':'Reread daughter forecast and Ben Elasa relationship/wealth/wedding invitation.',
'51a:3':'Reread toeva question, unspecified refuted answers, wife pouring/dance demand and exact wordplay.',
'51a:4':'Reread repeated condition and tevel wordplay with rhetorical comparison.',
'51a:5':'Reread zima question, repeated condition, exact wordplay and couple departure.',
'51a:6':'Reread Ben Elasa question and baraita purpose of haircut expenditure.',
'51a:7':'Reread Ezekiel citation, lulinit questions, Yehuda label and Rava tip/root description.',
'51a:8':'Reread Shmuel variety and Ashi hot-ashes definitions; Ashi marked rejected after actual continuation.',
'51a:9':'Reread Ravina quotation of all Nehemya botanical distinctions and explicit תיובתא.'}
if __name__=='__main__':a.save()
