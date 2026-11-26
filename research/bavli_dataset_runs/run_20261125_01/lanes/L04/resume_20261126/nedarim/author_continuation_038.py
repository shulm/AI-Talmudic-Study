"""Teaching fees, Sabbath lessons and alternative explanations of permitted payment."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r038.';a.OUTPUT='continuation_038.json'
c=a.c;q=b.q;e=a.edge
a.structure('fees',['36b:9']+['37a:'+str(i) for i in range(1,8)]+['37b:'+str(i) for i in range(1,6)],'Teaching fees: supervision versus accent division, Sabbath scheduling and scriptural derivation')
why=q('why','36b:9','מקרא מאי טעמא לא ילמדנו משום דקמהני ליה מדרש נמי קמהני ליה','If Scripture teaching is forbidden because it benefits the student, why is midrash permitted?')
shmuel=c('shmuel','36b:9','אמר שמואל במקום שנוטלין שכר על המקרא ואין נוטלין שכר על המדרש','Shmuel places the case where Scripture teaching is paid and midrash teaching is unpaid.',holder='שמואל',scope='Fee distinction explains benefit-vow rule')
fixed=q('fixed','36b:9','מאי פסקא','Why is that fee distinction fixed?')
law=c('law','37a:1',None,'The answer makes Scripture fees permissible even where charged, while midrash fees are not permissible.',composition='composite',scope='Normative distinction rather than arbitrary local custom')
e('shmuel.answer',shmuel,why,'answer','36b:9');e('law.answer',law,fixed,'answer','37a:1')
free=c('free','37a:2',"מאי שנא מדרש דלא דכתיב (דברים ד, יד) ואותי צוה ה' בעת ההיא ללמד אתכם וכתיב (דברים ד, ה) ראה למדתי אתכם חוקים ומשפטים כאשר צוני ה' מה אני בחנם אף אתם נמי בחנם",'The prohibition of midrash fees is derived from Moses teaching as commanded: as he taught freely, so should the teachers.',composition='composite',scope='Two-verse derivation and quoted principle')
scriptq=q('scriptq','37a:2','מקרא נמי בחנם','Should Scripture teaching likewise be free?')
rav=c('rav','37a:3','רב אמר שכר שימור','Rav identifies the permitted payment as supervision fees.',holder='רב',scope='Payment for ancillary supervision, not Torah content')
yohanan=c('yohanan','37a:3','ורבי יוחנן אמר שכר פיסוק טעמים','Rabbi Yohanan identifies it as payment for division of accents.',holder='רבי יוחנן',scope='Alternative explanation, not Shmuel’s own position')
e('rav.answer',rav,scriptq,'answer','37a:3');e('yohanan.answer',yohanan,scriptq,'answer','37a:3');e('yohanan.distinction',yohanan,rav,'distinction','37a:3')
adultq=q('adultq','37a:4','תנן לא ילמדנו מקרא בשלמא למאן דאמר שכר פיסוק טעמים היינו דלא ילמדנו אלא למאן דאמר שכר שימור גדול בר שימור הוא','How does supervision payment explain forbidding Scripture teaching to an adult, who does not require supervision?')
minor=c('minor','37a:4','בקטן קתני','The first answer makes the student a minor.',scope='Proposed reconstruction, expanded in response to next objection')
e('minor.answer',minor,adultq,'answer','37a:4')
fatherq=q('fatherq','37a:5','אי בקטן אימא סיפא אבל מלמד את בניו מקרא קטן בר בנים הוא','If the student is a minor, how can the latter clause discuss teaching his sons?')
reconstruct=c('reconstruct','37a:5','חסורי מחסרא והכי קתני לא ילמדנו מקרא בקטן אם היה גדול מלמדו לו ולבניו מקרא','The reconstructed Mishnah prohibits teaching the minor, but permits teaching an adult and his sons.',composition='composite',conditions=['supervision-fee explanation'],scope='Explicit חסורי מחסרא, not silent replacement of original Mishnah')
e('reconstruct.answer',reconstruct,fatherq,'answer','37a:5')
sabbath=c('sabbath','37a:6','מיתיבי תינוקות לא קורין בתחילה בשבת אלא שונין בראשון','A teaching forbids children beginning new reading on Sabbath but allows repeating the earlier reading.',scope='Quoted learning schedule rule used to challenge fee explanation')
payq=q('payq','37a:6','בשלמא למאן דאמר שכר פיסוק טעמים היינו דאין קורין בתחילה בשבת אלא למאן דאמר שכר שימור אמאי אין קורין בתחילה בשבת ואמאי שונין בראשון  הא איכא שכר שימור דשבת','Under supervision fees, why distinguish new reading from review when both involve Sabbath supervision pay?')
bundle=c('bundle','37a:7','וליטעמיך שכר פיסוק בשבת מי אסור  הבלעה היא והבלעה מישרא שרי','The reply says accent-division pay would also be bundled, and bundled payment is allowed.',scope='Rejects premise that this Sabbath lesson distinction rests on separately payable Sabbath wages')
daily=c('daily','37a:7','דתניא השוכר את הפועל לשמור את התינוק לשמור את הפרה לשמור את הזרעים אין נותנין לו שכר שבת','A baraita denies separate Sabbath wages for guarding a child, cow or seeds.',composition='composite',scope='Three guarding examples in wage rule')
exempt=c('exempt','37a:7','לפיכך','Consequently, if they are lost, the worker is not liable for them.',extra=[('37b:1','אם אבדו אינו חייב באחריותן')],scope='Cross-page consequence of unpaid Sabbath guarding')
period=c('period','37b:1','ואם היה שכיר שבת שכיר חדש שכיר שנה שכיר שבוע נותן לו שכר שבת לפיכך אם אבדו חייב באחריותן','If hired for a week, month, year or seven-year period, the worker receives bundled Sabbath pay and bears liability if they are lost.',composition='composite',scope='Period-based employment contrasted with separate daily payment')
e('bundle.answer',bundle,payq,'answer','37a:7');e('period.support',period,bundle,'support','37b:1')
parents=c('parents','37b:2','אלא גבי שבת היינו טעמא דאין קוראין בתחילה משום דיפנו אבהתהון דינוקי למצותא דשבתא','The actual Sabbath explanation is to leave the children’s fathers free for Sabbath observance.',scope='First final explanation of no-new-reading schedule')
food=c('food','37b:2','ואיבעית אימא משום דבשבתא אכלין ושתין ויקיר עליהון עלמא','Alternatively, Sabbath eating and drinking makes the children sluggish.',scope='Explicit alternative schedule rationale')
shmuel2=c('shmuel2','37b:2','כדאמר שמואל שינוי וסת תחילת חולי מעיים','Shmuel’s maxim about changed routine and intestinal illness is cited in support.',holder='שמואל',scope='Ancient physiological claim attributed to source, not clinical advice')
e('parents.answer',parents,payq,'answer','37b:2');e('food.answer',food,payq,'answer','37b:2');e('shmuel2.support',shmuel2,food,'support','37b:2')
girlsq=q('girlsq','37b:3','ולמאן דאמר שכר פיסוק טעמים מאי טעמא לא אמר שכר שימור','Why does the accent-division view not use supervision fees?')
girls=c('girls','37b:3','קסבר בנות מי קא בעיין שימור','It reasons that girls do not require that supervision.',scope='Source’s contextual premise explaining fee theory, not a universal assertion about children')
e('girls.answer',girls,girlsq,'answer','37b:3')
accentq=q('accentq','37b:4','ולמאן דאמר שכר שימור מאי טעמא לא אמר שכר פיסוק טעמים','Why does the supervision view not use accent-division fees?')
torah=c('torah','37b:4','קסבר (שכר) פיסוק טעמים דאורייתא הוא','It treats accent division as Torah-authorized.',scope='Printed parenthetical שכר preserved; explanatory status applies to accent division')
e('torah.answer',torah,accentq,'answer','37b:4')
reading=c('reading','37b:5','ויקראו בספר תורת האלהים זה מקרא','Rav interprets reading in the book of God’s Torah as Scripture reading.',holder='רב',scope='Rav Ika bar Avin via Rav Hananel transmits the Nehemiah exposition')
translation=c('translation','37b:5','מפורש זה תרגום','He interprets מפורש as translation.',holder='רב',scope='Second mapping in Nehemiah exposition')
verses=c('verses','37b:5','ושום שכל אלו הפסוקים','He interprets ושום שכל as verse divisions.',holder='רב',scope='Third mapping')
accents=c('accents','37b:5','ויבינו במקרא זה פיסוק טעמים','The first reading of ויבינו במקרא identifies accent division.',holder='רב',scope='Fourth mapping, alternative version follows')
tradition=c('tradition','37b:5','ואמרי לה  אלו המסורות','An alternative identifies the transmitted textual traditions.',scope='Explicit ואמרי לה retained as variant, not collapsed into accent interpretation')
for key,claim in [('reading',reading),('translation',translation),('verses',verses),('accents',accents)]:a.add(key+'.chain','attributions',dict(surface='אמר רב איקא בר אבין אמר רב חננאל אמר רב',role='transmitter',candidates=['רב איקא בר אבין','רב חננאל'],scope=claim,transmission_chain=['רב איקא בר אבין','רב חננאל','רב']),[a.ev('37b:5','אמר רב איקא בר אבין אמר רב חננאל אמר רב')],[claim])
e('accents.support',accents,torah,'support','37b:5');e('tradition.distinction',tradition,accents,'distinction','37b:5')
a.notes={
'36b:9':'Reread benefit objection, Shmuel fee setting and fixed-distinction question.',
'37a:1':'Reread permissibility distinction for Scripture versus midrash fees.',
'37a:2':'Reread both Moses verses, free-teaching derivation and Scripture counterquestion.',
'37a:3':'Reread Rav supervision versus Yohanan accent-division alternatives, not conflated with Shmuel.',
'37a:4':'Reread adult-supervision challenge and minor construction.',
'37a:5':'Reread minor-father challenge and explicit reconstructed two-age Mishnah.',
'37a:6':'Reread new-reading/review Sabbath rule and challenge to supervision-fee explanation.',
'37a:7':'Reread bundled-pay rebuttal, three guarding examples, daily-pay rule and cross-page consequence.',
'37b:1':'Reread unpaid-guard liability completion and four bundled employment periods with liability.',
'37b:2':'Reread both final Sabbath-schedule explanations and attributed Shmuel physiological maxim.',
'37b:3':'Reread why-not-supervision question and source’s girls premise.',
'37b:4':'Reread why-not-accents question, parenthetical wording and Torah-authority rationale.',
'37b:5':'Reread exact Ika/Hananel/Rav chain, all four verse mappings and explicit alternative textual-traditions reading.'}
if __name__=='__main__':a.save()
