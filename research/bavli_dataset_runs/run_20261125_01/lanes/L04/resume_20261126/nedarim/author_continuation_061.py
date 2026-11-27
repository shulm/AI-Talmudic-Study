"""Manual sabbatical-onion inquiry with successive proof failures and final distinction."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r061.';a.OUTPUT='continuation_061.json'
c=a.c;e=a.edge;q=b.q
a.structure('onion',['57b:'+str(i) for i in range(2,9)]+['58a:'+str(i) for i in range(1,7)]+['58b:'+str(i) for i in range(1,6)]+['59a:1'],'Sabbatical onion growth: alternative authorities, failed proofs and ground-based cancellation')
setting=c('setting','57b:2','ישמעאל איש כפר ימא ואמרי לה איש כפר דימא העלה בידו בצל שעקרו בשביעית ונטעו בשמינית ורבו גידוליו על עיקרו','Yishmael of Kefar Yama, alternatively Kefar Dima, considers an onion uprooted in the seventh year and replanted in the eighth, whose new growth exceeds its original part.',composition='composite',scope='Both place-name versions and all agricultural conditions retained')
main=q('main','57b:2','והכי קא מיבעיא ליה גידוליו היתר ועיקרו אסור כיון דרבו גידוליו מעיקרו אותן גידולי היתר מעלין את האיסור או לא','Do the predominant permitted growths cancel the prohibited original onion?',voice='ישמעאל איש כפר ימא / איש כפר דימא')
noanswer=c('noanswer','57b:2','אתא לקמיה דרבי אמי לא הוה בידיה','Rabbi Ami initially has no answer when approached.',scope='Initial state only; he later offers proofs, not a claim of permanent ignorance')
yanai=c('yanai','57b:3','אתא לקמיה דרבי יצחק נפחא פשט ליה מן הדא דאמר רבי חנינא תריתאה אמר רבי ינאי בצל של תרומה שנטעו ורבו גידוליו על עיקרו מותר','Rabbi Yitzhak Nappaha answers from Rabbi Hanina Terita’a reporting Rabbi Yannai: a replanted teruma onion whose growth exceeds its original part is permitted.',holder='רבי ינאי',composition='composite',scope='Full transmission and proof use; teruma ruling subsequently opposed by two authorities')
twoq=q('twoq','57b:3','א"ל ר\' ירמיה ואיתימא רבי זריקא שביק מר תרין ועביד כחד','Rabbi Yirmeya, alternatively Rabbi Zerika, objects: why abandon two authorities and follow one?',voice='רבי ירמיה / רבי זריקא')
who=q('who','57b:4','מאן נינהו תרין','Who are the two authorities?')
young=c('young','57b:4','דא"ר אבהו א"ר יוחנן ילדה שסיבכה בזקינה ובה פירות אע"פ שהוסיפה מאתים אסור','Rabbi Abbahu reports Rabbi Yohanan that fruit on a young tree grafted into an old tree remains prohibited even after increasing two hundredfold.',holder='רבי יוחנן',scope='Orla-context proof: original fruit present when grafted; exact multiplier retained')
vine=c('vine','57b:5','וא"ר שמואל בר רבי נחמני א"ר יונתן בצל שנטעו בכרם ונעקר הכרם אסור','Rabbi Shmuel son of Rabbi Nahmani reports Rabbi Yonatan that an onion planted in a vineyard remains prohibited after the vineyard is uprooted.',holder='רבי יונתן',scope='Vineyard-mixture counterexample; no attribution to Shmuel without patronymic')
e('yanai.answer',yanai,main,'answer','57b:3');e('young.answer',young,who,'answer','57b:4');e('vine.answer',vine,who,'answer','57b:5');e('young.objection',young,yanai,'objection','57b:4');e('vine.objection',vine,yanai,'objection','57b:5');e('young.answertwo',young,twoq,'answer','57b:4')
tithe=c('tithe','57b:6','הדר אתא לקמיה דר\' אמי ופשיט ליה מן הדא דאמר ר\' יצחק אמר ר\' יוחנן ליטרא בצלים שתיקנה וזרעה מתעשרת לפי כולה','Returning to Ami, he receives a proof from Rabbi Yitzhak reporting Yohanan: a litra of tithed onions replanted is tithed according to the whole resulting crop.',holder='רבי יוחנן',composition='composite',scope='Ami’s second-stage proof; transmission and original tithed status explicit')
cancel=c('cancel','57b:6','אלמא אותן גידולין מבטלין עיקר','The proposed inference is that growths cancel the original part.',mode='challenged',scope='Inference immediately limited by possible stringency-only operation')
strict=c('strict','57b:7','דלמא לחומרא שאני','The reply suggests stringent cancellation may differ.',mode='hypothetical',scope='Deflects a proof of permissive cancellation, not a final blanket denial')
e('tithe.support',tithe,cancel,'support','57b:6');e('strict.objection',strict,cancel,'objection','57b:7')
permittable=c('permittable','58a:1','כל דבר שיש לו מתירין כגון טבל ומעשר שני והקדש וחדש לא נתנו בהן חכמים שיעור','Rabbi Shimon says items with a route to permission—tevel, second tithe, consecrated property and new grain—have no fixed cancellation ratio.',holder='רבי שמעון',composition='composite',scope='Cross-folio baraita attribution; all four examples retained',extra=[('57b:8','אלא מן הדא דתניא רבי שמעון אומר')])
fixed=c('fixed','58a:1','וכל דבר שאין לו מתירין כגון תרומה ותרומת מעשר וחלה וערלה וכלאי הכרם נתנו בהם חכמים שיעור','Items without such a route—teruma, tithe-teruma, halla, orla and vineyard mixtures—have a cancellation ratio.',holder='רבי שמעון',composition='composite',scope='All five examples; no unstated one-size-fits-all numeric ratio supplied')
seventhq=q('seventhq','58a:2','אמרו לו והלא שביעית אין לה מתירין ולא נתנו בה חכמים שיעור דתנן השביעית אוסרת כל שהוא במינה','The respondents object that sabbatical produce lacks a route to permission yet prohibits any amount in its own kind.')
removal=c('removal','58a:2','אמר להן אף אני לא אמרתי אלא לביעור','Rabbi Shimon limits the no-ratio sabbatical rule to removal.',holder='רבי שמעון',scope='ביור versus eating distinction continued next segment')
flavor=c('flavor','58a:3','אבל לאכילה בנותן טעם','For eating, flavor contribution determines prohibition.',holder='רבי שמעון',scope='Complement to removal-only no-ratio statement')
strictagain=c('strictagain','58a:3','ודלמא הא נמי לחומרא שאני','The discussion again suggests this proof concerns stringency rather than permissive cancellation.',mode='hypothetical',scope='Second proof deflection retained separately')
e('removal.answer',removal,seventhq,'answer','58a:2');e('flavor.answer',flavor,seventhq,'answer','58a:3');e('strictagain.objection',strictagain,flavor,'objection','58a:3')
rain=c('rain','58a:4','אלא מן הדא פשטה דתנן בצלים שירדו עליהם גשמים וצמחו אם היו עלין שלהן שחורין אסורין הוריקו מותרין','The next proof cites onions growing after rainfall: dark leaves signify prohibition, green/pale leaves permission.',composition='composite',scope='Two source-stated leaf conditions; no modern botanical validation')
pull=c('pull','58a:5','ר\' חנניא בן אנטיגנוס אומר אם יכולין ליתלש בעלין שלהן אסורין','Rabbi Hananya ben Antigonus prohibits where the onions can be pulled out by their leaves.',holder="ר' חנניא בן אנטיגנוס",scope='Alternative growth-strength criterion in cited Mishnah')
after=c('after','58a:5','וכנגדן למוצאי שביעית מותרין','The corresponding cases after the seventh year are permitted.',scope='Baraita/Mishnah continuation used to infer permitted growth cancels prior prohibition')
infer=c('infer','58a:5','למימרא דגידולי היתר מעלין את האיסור','The proposed deduction is that permitted growth cancels prohibition.',mode='challenged',scope='Third proposed proof before crushed-onion deflection')
crushed=c('crushed','58a:5','ודלמא במדוכנין','The reply proposes that the case may involve crushed onions.',mode='hypothetical',scope='Deflects inference about an intact original onion')
e('after.support',after,infer,'support','58a:5');e('crushed.objection',crushed,infer,'objection','58a:5')
weeder=c('weeder','58b:1','המנכש עם הכותי בחסיות אוכל מהן אכילת עראי ומעשרן ודאי','One weeding bulb crops with a Samaritan may eat incidentally and must tithe them as certainly untithed.',composition='composite',scope='Two outcomes in next baraita, introduced58a6; source term כותי retained in evidence',extra=[('58a:6','אלא מן הדא דתניא')])
suspect=c('suspect','58b:2','רבי שמעון בן אלעזר אומר אם ישראל חשוד על השביעית למוצאי שביעית מותר','Rabbi Shimon ben Elazar permits produce after the seventh year when the Israelite grower is suspected of violating sabbatical restrictions.',holder='רבי שמעון בן אלעזר',scope='Bulb-weeding context retained; source-supported proof of permitted new growth')
inference=c('inference','58b:2','למימרא דגידולי היתר מעלין את האיסור','This is taken to show permitted growth cancels the prohibition.',scope='Proof survives following three alternative-case deflections, then narrowed to sabbatical produce')
seedq=q('seedq','58b:2','ודלמא בדבר שזרעו כלה','Might this concern a plant whose seed is consumed?')
bulbs=c('bulbs','58b:2','הא תניא אלו הן חסיות כגון הלוף השום והבצלים','The reply identifies חסיות as לוף, garlic and onions.',composition='composite',scope='Three persistent-bulb examples exclude proposed consumed-seed case')
crushq=q('crushq','58b:3','ודלמא במדוכנין','Might these bulbs have been crushed?')
suspectreply=c('suspectreply','58b:3','חשוד על השביעית קתני','The reply stresses that the grower is suspected of sabbatical violations.',scope='Rejects assuming the special crushed-bulb case')
mixtureq=q('mixtureq','58b:3','ודלמא בתערובת','Might the permission concern a mixture?')
weedreply=c('weedreply','58b:3','המנכש קתני','The reply stresses the person is weeding.',scope='Growing-in-place context rejects proposed mixture')
e('bulbs.answer',bulbs,seedq,'answer','58b:2');e('suspectreply.answer',suspectreply,crushq,'answer','58b:3');e('weedreply.answer',weedreply,mixtureq,'answer','58b:3');e('inference.answer',inference,main,'answer','58b:2')
refuteq=q('refuteq','58b:4','לימא תיהוי תיובתיה דרבי יוחנן ודרבי יונתן','Does this refute Rabbi Yohanan and Rabbi Yonatan?')
ground=c('ground','58b:4','אמר רבי יצחק שניא שביעית הואיל ואיסורה ע"י קרקע בטילתה נמי ע"י קרקע','Rabbi Yitzhak distinguishes sabbatical produce: its prohibition arises through the ground and can be canceled through the ground.',holder='רבי יצחק',scope='Limits permissive growth cancellation to sabbatical case; preserves prior orla/vineyard rulings')
e('ground.answer',ground,refuteq,'answer','58b:4');e('ground.qualification',ground,inference,'qualification','58b:4')
maaserq=q('maaserq','58b:5','הרי מעשר דאיסורו ע"י קרקע ואין בטילתו על ידי קרקע','But does tithe not arise through the ground while remaining uncanceled by the ground?')
ten=c('ten','58b:5','דתניא ליטרא מעשר טבל שזרעה בקרקע והשביחה והרי היא כעשר ליטרין חייבת במעשר ובשביעית ואותה ליטרא מעשר עליה ממקום אחר לפי חשבון','The baraita describes one litra of untithed tithe replanted and grown to ten: the crop owes tithe and sabbatical observance, while the original litra requires proportionate tithing from elsewhere.',composition='composite',scope='Exact original/new quantities and all three stated obligations')
heap=c('heap','59a:1','אמרי מעשר דיגון הוא דקא גרים ליה','The reply says tithe is caused by heaping the produce.',scope='Processing trigger distinguishes tithe from directly ground-generated sabbatical prohibition')
e('ten.support',ten,maaserq,'support','58b:5');e('heap.answer',heap,maaserq,'answer','59a:1')
a.notes={
'57b:2':'Reread two Yishmael place-name versions, uprooting/replanting years and predominant growth conditions, main inquiry and Ami initial nonanswer.',
'57b:3':'Reread Yitzhak Nappaha/Hanina Teritaa/Yannai transmission and alternate Yirmeya/Zerika objection attribution.',
'57b:4':'Reread two-authority question and Abbahu/Yohanan young-tree fruit counterexample including two-hundred increase.',
'57b:5':'Reread full Shmuel son of Nahmani/Yonatan onion-vineyard transmission.',
'57b:6':'Reread return to Ami, Yitzhak/Yohanan tithed-onion proof and inferred cancellation.',
'57b:7':'Reread stringency-only deflection of second proof.',
'57b:8':'Reread introduction assigning following baraita to Rabbi Shimon; cross-folio source anchor included.',
'58a:1':'Reread both cancellation categories and all four/five example lists.',
'58a:2':'Reread sabbatical no-ratio objection and Shimon removal-only response.',
'58a:3':'Reread eating flavor criterion and renewed stringency-only deflection.',
'58a:4':'Reread rainfall onion proof and both leaf-color outcomes.',
'58a:5':'Reread Hananya pulling criterion, post-sabbatical permission, proposed cancellation and crushed-case deflection.',
'58a:6':'Reread next baraita introduction linked to58b1.',
'58b:1':'Reread Samaritan bulb-weeding incidental eating and definite-tithe obligations.',
'58b:2':'Reread Shimon ben Elazar suspected-grower permission, cancellation inference, consumed-seed objection and all three bulb examples.',
'58b:3':'Reread both crushed/mixture proposals and their separate suspected-grower/weeding rebuttals.',
'58b:4':'Reread proposed refutation of Yohanan/Yonatan and Yitzhak sabbatical-specific ground distinction.',
'58b:5':'Reread tithe counterexample, one-to-ten quantities and all obligations including original-litra external separation.',
'59a:1':'Reread heaping-processing trigger answer distinguishing tithe.'}
if __name__=='__main__':a.save()
