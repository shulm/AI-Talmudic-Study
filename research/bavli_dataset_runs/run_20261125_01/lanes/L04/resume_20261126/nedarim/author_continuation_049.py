"""Manual source reading of cooked-food terminology and its local usage."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r049.';a.OUTPUT='continuation_049.json'
c=a.c;e=a.edge;q=b.q
a.structure('food',['49a:'+str(i) for i in range(1,11)]+['49b:1','49b:2'],'Cooked food wording, local usage and the soft-food gloss')
m=c('m','49a:1','מן המבושל מותר בצלי ובשלוק','A vow against cooked food permits roasted and thoroughly boiled food.',scope='Mishnah wording; local usage qualification follows')
soft=c('soft','49a:1','אמר קונם תבשיל שאיני טועם אסור במעשה קדרה רך ומותר בעבה','A vow against tavshil prohibits soft pot food and permits thick pot food.',composition='composite',scope='Two contrasted textures under the named formula')
egg=c('egg','49a:1','ומותר בביצה טורמוטא ובדלעת הרמוצה','The Mishnah permits ביצה טורמוטא and דלעת הרמוצה.',composition='composite',scope='Two named preparations retained without importing a later definition')
pot=c('pot','49a:1','הנודר ממעשה קדרה אין אסור אלא ממעשה רתחתה','A vow against מעשה קדרה prohibits only מעשה רתחתה.',scope='Exact technical food categories retained')
descend=c('descend','49a:1','אמר קונם היורד לקדרה שאיני טועם אסור בכל המתבשלין בקדרה','A vow against what goes into the pot prohibits all foods cooked in a pot.',scope='Distinct wider formula')
y=c('y','49a:2','תניא ר\' יאשיה אוסר','Rabbi Yoshiya prohibits roasted food under the cooked-food vow.',holder="ר' יאשיה",scope='Object supplied by the immediately preceding Mishnah comparison')
verse=c('verse','49a:2','ואע"פ שאין ראיה לדבר זכר לדבר שנא\' (דברי הימים ב לה, יג) ויבשלו את הפסח באש כמשפט','The baraita cites cooking the Passover offering in fire as a reminder, expressly not a proof.',scope='Explicit limitation on the cited verse’s evidential force')
e('y.objection',y,m,'objection','49a:2');e('verse.support',verse,y,'support','49a:2')
theory=q('theory','49a:3',None,'Does Yoshiya follow Torah usage while the Mishnah follows ordinary speech?')
rejected=c('rejected','49a:3',None,'The proposed allocation makes Yoshiya follow Torah language and the Mishnah ordinary speech.',mode='rejected',composition='composite',scope='Explicit proposed explanation rejected by the following לא')
allusage=c('allusage','49a:4','לא דכולי עלמא בנדרים הלך אחר לשון בני אדם','The answer says all parties follow ordinary speech in vows.',scope='Rejects proposed methodological disagreement')
local=c('local','49a:4','מר כי אתריה ומר כי אתריה באתרא דתנא דילן לצלי קרו ליה צלי ולמבושל קרו ליה מבושל באתרא דר\' יאשיה אפילו צלי קרו מבושל','The Mishnah’s locality distinguishes roasted from cooked, while Yoshiya’s locality also calls roasted food cooked.',composition='composite',scope='Explicit local terminology explanation for differing rulings')
e('usage.answer',allusage,theory,'answer','49a:4');e('usage.correct',allusage,rejected,'correction','49a:4');e('local.distinction',local,y,'distinction','49a:4')
verseq=q('verseq','49a:5','והא קרא נסיב לה','Why then did Yoshiya invoke a verse?')
asmakhta=c('asmakhta','49a:5','אסמכתא בעלמא','The verse is only an asmakhta.',scope='Explicit answer, not independent scriptural derivation')
e('asmakhta.answer',asmakhta,verseq,'answer','49a:5');e('asmakhta.qualification',asmakhta,verse,'qualification','49a:5')
textureq=q('textureq','49a:6','והא מתבשיל נדר','Why distinguish textures when he vowed against tavshil?')
abaye=c('abaye','49a:7','אמר אביי האי תנא כל מידי דמתאכל ביה ריפתא תבשיל קרו ליה','Abaye explains that this tanna calls anything eaten with bread tavshil.',holder='אביי',scope='Usage explanation of the soft-food category')
bar=c('bar','49a:7','והתניא הנודר מן התבשיל אסור בכל מיני תבשיל ואסור בצלי ובשלוק ובמבושל','The supporting baraita includes all kinds of tavshil, including roasted, thoroughly boiled and cooked foods.',composition='composite',scope='Explicit listed applications of the bread-accompaniment usage')
gourd=c('gourd','49a:7','ואסור בהיטריות רכות שהחולין אוכלין בהן פיתן','The baraita also prohibits soft היטריות with which the חולין eat their bread.',scope='Printed labels retained; ensuing discussion disputes how to understand the consumers')
e('abaye.answer',abaye,textureq,'answer','49a:7');e('bar.support',bar,abaye,'support','49a:7')
doctorq=q('doctorq','49a:8','איני','Is the baraita’s association of this food with the ill plausible?')
visit=c('visit','49a:8','והא רבי ירמיה חלש על לגביה ההוא אסיא לאסיוה חזא קרא דמחת בביתיה שבקיה ונפק','The narrative reports that a physician visiting the ill Rabbi Yirmeya left after seeing a gourd in his house.',composition='composite',scope='Reported incident used as an objection, not modern medical guidance')
doctor=c('doctor','49a:8','אמר מלאך מותא אית ליה לדין בביתיה ואנא איעול לאסאה יתיה','The physician protests that Yirmeya has the angel of death in his house while expecting treatment.',scope='Anonymous physician’s reported rhetorical evaluation, not narrator’s medical endorsement')
first=c('first','49a:9','לא קשיא הא ברכיכי הא באשוני','The first answer distinguishes soft from hard gourds.',composition='composite',scope='Two food conditions reconcile the baraita and incident')
second=c('second','49a:9','רבא בר עולא אמר הא בקרא גופיה והא בגוויה דקרא','Rava bar Ulla instead distinguishes the gourd itself from its interior.',holder='רבא בר עולא',composition='composite',scope='Alternate distinction, not attributed to Rava without patronymic')
tendrils=c('tendrils','49a:9','דאמר רב יהודה לוליבא דקרא בסילקא לוליבא דכיתנא בכותחא','Rav Yehuda describes gourd shoots with beets and flax shoots with kutah.',holder='רב יהודה',composition='composite',scope='Two attributed food pairings, not Rav himself')
restrict=c('restrict','49a:9','ודבר זה אסור לאומרו בפני עם הארץ','The statement adds that this matter must not be told before an am haaretz.',scope='Source’s restriction preserved without supplying an unstated rationale')
rava=c('rava','49a:10','רבא אמר מאן חולין רבנן','Rava interprets the baraita’s חולין as sages.',holder='רבא',scope='Alternative interpretation of the consumer label')
prayer=c('prayer','49b:1','כמאן מצלינן על קצירי ועל מריעי [כמאן כר\' יוסי]','Rava’s cited prayer discussion associates praying for קצירי and מריעי with Rabbi Yosei in the printed bracketed wording.',holder='רבא',scope='Cross-segment attribution from49a:10; bracketed textual status retained',extra=[('49a:10','רבא לטעמיה דאמר רבא')])
dist=c('dist','49b:1','מדאמר קצירי ומריעי שמע מינה קצירי קצירי ממש מריעי רבנן','The distinction between the prayer’s two labels is read as literal sick people and sages respectively.',holder='רבא',composition='composite',scope='Explicit two-label interpretation under cross-segment Rava attribution',extra=[('49a:10','רבא לטעמיה דאמר רבא')])
e('visit.objection',visit,gourd,'objection','49a:8');e('first.answer',first,doctorq,'answer','49a:9');e('second.answer',second,doctorq,'answer','49a:9');e('rava.answer',rava,doctorq,'answer','49a:10');e('dist.support',dist,rava,'support','49b:1')
babylon=c('babylon','49b:2','מתני\' דלא כבבלאי','The Mishnah’s thick-food permission does not fit Babylonian eating practice.',scope='Local dietary usage qualification of this wording')
zeira=c('zeira','49b:2','דאמר ר\' זירא בבלאי טפשאי דאכלי לחמא בלחמא','Rabbi Zeira disparages Babylonians for eating bread with bread.',holder="ר' זירא",scope='Attributed polemical characterization in the food-usage discussion, not endorsed stereotype')
e('babylon.qualification',babylon,soft,'qualification','49b:2');e('zeira.support',zeira,babylon,'support','49b:2')
a.notes={
'49a:1':'Reread all five vow formulas/categories, contrasting soft/thick, roast/boiled and special preparations; no definition imported from later discussion.',
'49a:2':'Reread Yoshiya prohibition and explicit reminder-not-proof qualification on Chronicles.',
'49a:3':'Reread proposed Torah/ordinary speech allocation as rejected in next segment.',
'49a:4':'Reread unanimous ordinary usage and both locality-specific naming practices.',
'49a:5':'Reread verse objection and asmakhta-only answer.',
'49a:6':'Reread repeated Mishnah lemma and texture question.',
'49a:7':'Reread Abaye bread-accompaniment explanation and full supporting baraita including soft food consumer label.',
'49a:8':'Reread physician narrative and quoted rhetorical objection without endorsing medical claims.',
'49a:9':'Reread anonymous and Rava bar Ulla alternative distinctions, both Rav Yehuda pairings and disclosure restriction.',
'49a:10':'Reread Rava alternative sages interpretation and cross-folio transmission introducing prayer statement.',
'49b:1':'Reread prayer wording including bracketed Yosei and separate literal-ill/sages interpretation.',
'49b:2':'Reread thick-food lemma, Babylonian local usage exception and attributed Zeira polemic.'}
if __name__=='__main__':a.save()
