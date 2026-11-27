"""Manual clothing-intent and upper-story readings."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r058.';a.OUTPUT='continuation_058.json'
c=a.c;e=a.edge;q=b.q
a.structure('clothing',['55b:'+str(i) for i in range(5,10)],'Clothing categories, rain coverings and circumstances of the vow')
a.structure('house',['56a:'+str(i) for i in range(1,5)],'House/upper-story terminology and two attribution challenges')
cloth=c('cloth','55b:5','הנודר מן הכסות מותר בשק וביריעה ובחמילה','A clothing vow permits sackcloth, a sheet and חמילה.',composition='composite',scope='Three named exclusions; precise textile label preserved')
wool=c('wool','55b:5','אמר קונם צמר עולה עלי מותר להתכסות בגיזי צמר','A vow against wool coming upon oneself permits covering with wool fleeces.',scope='Mishnah wording before circumstance-dependent explanations')
flax=c('flax','55b:5','הפשתן עולה עלי מותר להתכסות באניצי פשתן','A vow against flax coming upon oneself permits covering with flax bundles.',scope='Parallel raw-material exclusion')
principle=c('principle','55b:6','ר\' יהודה אומר הכל לפי הנודר','Rabbi Yehuda says everything depends on the person making the vow.',holder="ר' יהודה",scope='Context-sensitive interpretation principle')
burden=c('burden','55b:6','טען והזיע והיה ריחו קשה אמר קונם צמר ופשתים עולה עלי מותר להתכסות ואסור להפשיל לאחוריו','Where carrying caused sweat and offensive odor, a vow against wool/flax coming upon oneself permits wearing but prohibits carrying behind oneself.',holder="ר' יהודה",composition='composite',scope='Explicit contextual trigger and two different uses')
barpermit=c('barpermit','55b:7','תניא הנודר מן הכסות מותר בשק וביריעה ובחמילה','The baraita repeats the three permitted textile categories.',composition='composite',scope='Separate repeated occurrence')
barforbid=c('barforbid','55b:7','ואסור בפונדא ובפסקיא ובסקורטיא ובקטבליא ואנפליא ופליניא ומכנסים וכובע','It prohibits פונדא, פסקיא, סקורטיא, קטבליא, אנפליא, פליניא, trousers and a cap.',composition='composite',scope='Complete eight-item garment inventory; untranslated technical labels retained')
leatherq=q('leatherq','55b:7','מאי איסקורטי','What is איסקורטי?')
leather=c('leather','55b:7','אמר רבה בר בר חנה כיתונא דצלא','Rabbah bar bar Hana defines it as a leather tunic.',holder='רבה בר בר חנה',scope='Full patronymic retained; not Rabbah alone')
e('leather.answer',leather,leatherq,'answer','55b:7')
rain=c('rain','55b:8','תניא יוצאין בשק עבה ובסגוס עבה וביריעה ובחמילה מפני הגשמים','The baraita permits going out protected from rain in thick sackcloth, a thick סגוס, a sheet or חמילה.',composition='composite',scope='Four explicitly permitted rain coverings in going-out rule')
boxes=c('boxes','55b:8','אבל לא בתיבה ולא בקופה ולא במחצלת מפני הגשמים','It excludes a chest, a basket and a mat as rain coverings for going out.',composition='composite',scope='Three excluded objects contrasted with clothing')
shepherd=c('shepherd','55b:8','הרועים יוצאין בשקים ולא רועים בלבד אמרו אלא כל אדם אלא שדברו חכמים בהווה','Shepherds may go out in sacks, and this applies to everyone; shepherds are mentioned as the usual case.',composition='composite',scope='Explicit rejection of an occupational restriction')
wear=c('wear','55b:9','תניא כיצד א"ר יהודה הכל לפי הנודר היה לבוש צמר והצר ואמר קונם צמר עולה עלי אסור ללבוש ומותר לטעון','The baraita illustrates Yehuda: discomfort while wearing wool yields a vow prohibiting wearing but permitting carrying.',holder='רבי יהודה',composition='composite',scope='Wearing-triggered interpretation and both outcomes')
carry=c('carry','55b:9','היה טעון פשתן והזיע ואמר קונם פשתן עולה עלי מותר ללבוש ואסור לטעון','Sweating while carrying flax yields a vow permitting wearing but prohibiting carrying.',holder='רבי יהודה',composition='composite',scope='Carrying-triggered interpretation and reversed outcomes')
meir=c('meir','56a:1','הנודר מן הבית מותר בעלייה דברי רבי מאיר','Rabbi Meir permits an upper story under a house vow.',holder='רבי מאיר',scope='House-category scope')
sages=c('sages','56a:1','וחכמים אומרים עלייה בכלל הבית','The sages include the upper story in the house.',holder='חכמים',scope='Explicit contrary category inclusion')
reverse=c('reverse','56a:1','הנודר מן עלייה מותר בבית','An upper-story vow permits the house.',scope='Reverse direction separately stated')
e('sages.objection',sages,meir,'objection','56a:1')
tannaq=q('tannaq','56a:2','מאן תנא (ויקרא יד, לה) בבית לרבות את היציע בבית לרבות את העלייה','Which tanna requires the verse בבית to include a gallery and an upper story?')
hisda=c('hisda','56a:2','אמר רב חסדא רבי מאיר היא דאי רבנן האמרי רבנן עלייה בכלל הבית למה לי קרא בבית לריבויא','Rav Hisda identifies Rabbi Meir, reasoning that the sages already include an upper story and would not need the verse.',holder='רב חסדא',composition='composite',scope='Proposed attribution and rationale, challenged by following alternative')
abaye=c('abaye','56a:3','אביי אמר אפי\' תימא רבנן בעיא קרא','Abaye says even the sages require the verse.',holder='אביי',scope='Alternative attribution, not denial that verse includes upper story')
attached=c('attached','56a:3','דסלקא דעתך אמינא (ויקרא יד, לד) בבית ארץ אחזתכם כתיב דמחבר בארעא שמיה בית עלייה הא לא מחבר בארעא','One might have read the land-of-your-possession wording to include only ground-attached houses, excluding an upper story.',mode='rejected',composition='composite',scope='Abaye’s hypothetical reading explains why inclusion verse is needed; not final exclusion')
e('hisda.answer',hisda,tannaq,'answer','56a:2');e('abaye.answer',abaye,tannaq,'answer','56a:3');e('abaye.objection',abaye,hisda,'objection','56a:3');e('attached.support',attached,abaye,'support','56a:3')
sale=c('sale','56a:4','הא דאמר רב הונא בר חייא משמיה דעולא בית בביתי אני מוכר לך מראהו עלייה','Rav Huna bar Hiyya reports Ulla: a seller saying a house among my houses may show the buyer an עלייה.',holder='עולא',scope='Reported sale wording; ambiguous עלייה is reinterpreted at end of segment')
inference=c('inference','56a:4','טעמא דא"ל בית שבביתי אני מוכר לך אבל בית סתם אינו מראהו עלייה','The proposed inference says only the qualified sale formula permits an upper story; a simple house sale does not.',mode='challenged',composition='composite',scope='Proposed upper-story interpretation deflected by wordplay at end')
saleq=q('saleq','56a:4','לימא רבי מאיר היא','Should Ulla’s sale rule therefore be identified with Rabbi Meir?')
best=c('best','56a:4','אפילו תימא רבנן מאי עלייה מעולה שבבתים','The answer allows the sages too, interpreting עלייה as the best of the houses.',scope='Explicit reinterpretation, not an unconditional equation of upper story with best house')
e('best.answer',best,saleq,'answer','56a:4');e('best.qualification',best,sale,'qualification','56a:4');e('best.correction',best,inference,'correction','56a:4')
a.notes={
'55b:5':'Reread clothing three exclusions and separate raw wool/flax permissions.',
'55b:6':'Reread Yehuda intention principle, sweat/odor carrying context and wearing/carrying contrast.',
'55b:7':'Reread all three permissions and eight prohibited garments plus Rabbah bar bar Hana leather definition.',
'55b:8':'Reread four rain coverings, three excluded containers/mat and explicit shepherds-as-usual-case generalization.',
'55b:9':'Reread complete Yehuda wearing-versus-carrying triggers and all four outcomes.',
'56a:1':'Reread Meir/sages upper-story dispute and reverse permission.',
'56a:2':'Reread gallery/upper-story inclusion verse question and Hisda Meir attribution rationale.',
'56a:3':'Reread Abaye sages alternative and rejected ground-attachment hypothesis motivating verse.',
'56a:4':'Reread Huna bar Hiyya/Ulla report, proposed upper-story inference, Meir attribution question and final best-house reinterpretation.'}
if __name__=='__main__':a.save()
