"""Visiting sick: scriptural hints, cosmogonic objections and bounded one-sixtieth analogy."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r041.';a.OUTPUT='continuation_041.json'
c=a.c;q=b.q;e=a.edge
a.structure('hint',['39b:'+str(i) for i in range(2,15)],'Visiting hint and Korah-associated cosmological expositions')
a.structure('measure',['39b:15','39b:16','39b:17'],'No measure of visits, one-sixtieth claim and declining-base analogy')
hintq=q('hintq','39b:2','אמר ריש לקיש רמז לביקור חולין מן התורה מנין','Where does Reish Lakish find a Torah hint for visiting the sick?',voice='ריש לקיש')
hint=c('hint','39b:2',"שנאמר (במדבר טז, כט) אם כמות כל האדם ימותון אלה ופקודת כל אדם וגו'",'Reish Lakish cites the ordinary death and visitation phrase in Numbers16.',holder='ריש לקיש',scope='Stated hint, not a comprehensive legal derivation')
meaning=q('meaning','39b:2','מאי משמע','How does that phrase imply sick-visiting?')
rava=c('rava','39b:2',"אמר רבא אם כמות כל האדם ימותון אלה שהן חולים ומוטלים בעריסתן ובני אדם מבקרים אותן מה הבריות אומרים לא ה' שלחני לזה",'Rava reads Moses as contrasting ordinary sickbed death with visitors against the extraordinary sign proving his mission.',holder='רבא',composition='composite',scope='Interpretation of narrative condition, not an assertion that Korah’s group actually died on sickbeds')
e('hint.answer',hint,hintq,'answer','39b:2');e('rava.answer',rava,meaning,'answer','39b:2')
create=c('create','39b:3',None,'Rava expounds Moses’ request as using Gehinnom if already created, otherwise asking God to create it.',holder='רבא',mode='challenged',composition='composite',scope='Initial interpretation revised after creation-before-world objection')
priorq=q('priorq','39b:4','איני והא תניא שבעה דברים נבראו קודם שנברא העולם','How can Gehinnom’s creation be uncertain when a baraita lists seven things created before the world?')
seven=c('seven','39b:4','אלו הן תורה ותשובה גן עדן וגיהנם כסא הכבוד ובית המקדש ושמו של משיח','The list is Torah, repentance, Eden, Gehinnom, the throne of glory, the Temple and Messiah’s name.',composition='composite',scope='Source’s cosmological teaching, not empirical chronology')
for key,ref,text in [
('torah','39b:5','Torah’s precedence is supported by ה׳ קנני ראשית דרכו.'),
('repent','39b:6','Repentance’s precedence is supported by the juxtaposed pre-mountain and return-humanity verses.'),
('eden','39b:7','Eden’s precedence is supported by the planting in Eden מקדם.'),
('hell','39b:8','Gehinnom’s precedence is supported by תפתה prepared מאתמול.'),
('throne','39b:9','The throne’s precedence is supported by נכון כסאך מאז.'),
('temple','39b:10','The Temple’s precedence is supported by כסא כבוד מרום מראשון.'),
('messiah','39b:11','Messiah’s name is supported by יהי שמו לעולם.')]:
    claim=c(key,ref,None,text,scope='Specific prooftext within seven-item cosmological baraita')
    e(key+'.support',claim,seven,'support',ref)
mouth=c('mouth','39b:12',"אלא הכי קאמר אי איברי ליה פומא מוטב ואם לא יברא ה'",'The first correction makes Moses ask about Gehinnom’s opening rather than its existence.',mode='challenged',scope='Intermediate corrected interpretation')
newq=q('newq','39b:12','והכתיב (קהלת א, ט) אין כל חדש תחת השמש','How could a new opening be created, given אין כל חדש תחת השמש?')
near=c('near','39b:12','הכי קאמר אי הכא לא מקרב פומא להכא ליקרב','The final explanation asks that the opening be brought near if it is not nearby.',scope='Relocation rather than new creation')
e('mouth.answer',mouth,priorq,'answer','39b:12');e('mouth.correction',mouth,create,'correction','39b:12');e('near.answer',near,newq,'answer','39b:12');e('near.correction',near,mouth,'correction','39b:12')
sunq=q('sunq','39b:13','מאי דכתיב (חבקוק ג, יא) שמש ירח עמד זבולה שמש וירח בזבול מאי בעיין והא ברקיע קביעי','Why does Habakkuk place sun and moon in Zevul if their station is the firmament?')
sun=c('sun','39b:13','מלמד שעלו שמש וירח מרקיע לזבול ואמרו לפניו רבונו של עולם אם אתה עושה דין לבן עמרם אנו מאירים ואם לאו אין אנו מאירין','The exposition depicts sun and moon ascending to Zevul and conditioning their light on justice for Moses son of Amram.',composition='composite',scope='Aggadic narrative; attributed alternatively to Rava or Rabbi Yitzhak')
a.add('sun.variant','attributions',dict(surface='דרש רבא ואמרי לה אמר רבי יצחק',role='speaker',candidates=['רבא','רבי יצחק'],scope=sun,transmission_chain=[]),[a.ev('39b:13','דרש רבא ואמרי לה אמר רבי יצחק')],[sun],uncertainty=['Explicit alternative attribution; neither named speaker selected as certain.'])
arrows=c('arrows','39b:14','באותה שעה ירה בהן חיצים וחניתות','The narrative describes arrows and spears being shot at them.',scope='Aggadic response, not an astronomical mechanism asserted independently')
honor=c('honor','39b:14','אמר להם בכל יום ויום משתחוים לכם ואתם מאירים בכבודי לא מחיתם בכבוד בשר ודם מחיתם','The divine rebuke contrasts their continuing to shine despite human worship of them with their protest for a human’s honor.',composition='composite',scope='Embedded divine speech in exposition')
daily=c('daily','39b:14',"ובכל יום ויום יורין בהן חיצין וחניתות ומאירים שנאמר (חבקוק ג, יא) לאור חציך יהלכו וגו'",'The exposition depicts daily arrows and spears followed by their shining, interpreting Habakkuk’s light-of-arrows phrase.',scope='Source-attributed cosmic narrative')
e('sun.answer',sun,sunq,'answer','39b:13')
unlimited=c('unlimited','39b:15','תניא ביקור חולים אין לה שיעור','A baraita says visiting the sick has no measure.',scope='Meaning disputed, not yet a claim of infinite duration')
measureq=q('measureq','39b:15','מאי אין לה שיעור','What does no measure mean?')
yosef=c('yosef','39b:15','סבר רב יוסף למימר אין שיעור למתן שכרה','Rav Yosef initially proposes limitless reward.',holder='רב יוסף',mode='rejected',scope='Explicit proposed interpretation rejected by Abaye')
reward=c('reward','39b:15','אמר ליה אביי וכל מצוות מי יש שיעור למתן שכרן והא תנן (משנה אבות ב א) הוי זהיר במצוה קלה כבחמורה שאין אתה יודע מתן שכרן של מצוות','Abaye objects that rewards of all commandments are unknown, citing care for light as for grave commandments.',holder='אביי',scope='Reason the reward reading does not distinguish sick-visiting')
great=c('great','39b:15','אלא אמר אביי אפילו גדול אצל קטן','Abaye interprets it as a great person visiting a lesser person.',holder='אביי',scope='No status threshold for visiting')
hundred=c('hundred','39b:15','רבא אמר אפילו מאה פעמים ביום','Rava interprets it as even one hundred visits in a day.',holder='רבא',scope='Source’s frequency formulation, no claim this is a clinical schedule')
e('yosef.answer',yosef,measureq,'answer','39b:15');e('reward.objection',reward,yosef,'objection','39b:15');e('great.answer',great,measureq,'answer','39b:15');e('hundred.answer',hundred,measureq,'answer','39b:15')
sixty=c('sixty','39b:16','אמר רבי אחא בר חנינא כל המבקר חולה נוטל אחד משישים בצערו','Rabbi Aha bar Hanina says a visitor removes one sixtieth of the patient’s distress.',holder='רבי אחא בר חנינא',scope='Attributed aggadic benefit claim, qualified immediately; not an empirical effect size')
sixtyq=q('sixtyq','39b:16','אמרי ליה אם כן ליעלון שיתין ולוקמוה','Why not then have sixty visitors restore him entirely?')
diminish=c('diminish','39b:16','אמר ליה כעישורייתא דבי רבי','The answer compares the effect to Rabbi’s successive tenths.',scope='Diminishing remainder analogy rather than subtraction from constant original amount')
peer=c('peer','39b:16','ובבן גילו','The statement is limited to a בן גילו visitor.',conditions=['בן גילו'],scope='Exact qualifier retained; no unprovided choice between age/affinity readings')
e('diminish.answer',diminish,sixtyq,'answer','39b:16');e('peer.qualification',peer,sixty,'qualification','39b:16')
tenth=c('tenth','39b:17','דתניא רבי אומר בת הניזונית מנכסי אחין נוטלת עישור נכסים','Rabbi teaches that a daughter maintained from brothers’ estate assets takes a tenth of the property.',holder='רבי',scope='Cited estate rule supplying the numerical analogy')
tenq=q('tenq','39b:17','אמרו לו לרבי לדבריך מי שיש לו עשר בנות ובן אין לו לבן במקום בנות כלום','Would ten daughters then leave nothing for a son?')
remaining=c('remaining','39b:17','אמר להן ראשונה נוטלת עישור נכסים שניה במה ששיירה שלישית במה ששיירה וחוזרות וחולקות בשוה','Rabbi answers that each successive tenth comes from the remainder, and the daughters then pool and divide equally.',holder='רבי',composition='composite',scope='Exact sequential and equalization steps, not ten times one tenth of original estate')
e('remaining.answer',remaining,tenq,'answer','39b:17');e('remaining.analogy',remaining,diminish,'analogy','39b:17')
a.notes={
'39b:2':'Reread Reish Lakish source question, cited verse, meaning question and Rava sickbed-visitor interpretation.',
'39b:3':'Reread initial Rava Gehinnom creation conditional, followed all corrections.',
'39b:4':'Reread prior-creation objection and all seven named items.',
'39b:5':'Reread Torah-specific prooftext.',
'39b:6':'Reread both repentance prooftext clauses.',
'39b:7':'Reread Eden-specific prooftext.',
'39b:8':'Reread Gehinnom-specific prooftext relevant to initial objection.',
'39b:9':'Reread throne-specific prooftext.',
'39b:10':'Reread Temple-specific prooftext.',
'39b:11':'Reread Messiah-name prooftext.',
'39b:12':'Reread opening-creation correction, nothing-new objection and final relocation interpretation.',
'39b:13':'Reread Rava/Yitzhak alternative attribution, Zevul/firmament question and conditional sun/moon narrative.',
'39b:14':'Reread arrows/spears event, divine honor rebuke and daily cosmic interpretation as attributed aggadah.',
'39b:15':'Reread no-measure question, rejected Yosef reward reading, Abaye objection and both final status/frequency readings.',
'39b:16':'Reread one-sixtieth claim, sixty-visitor objection, diminishing-tenths analogy and בן גילו qualifier.',
'39b:17':'Reread Rabbi tenth rule, ten-daughter objection, successive remainder calculation and equal pooling.'}
if __name__=='__main__':a.save()
