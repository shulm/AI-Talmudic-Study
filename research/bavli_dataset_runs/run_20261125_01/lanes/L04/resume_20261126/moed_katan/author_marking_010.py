"""Manually authored grave-marking derivations and Rabbi Yannai narrative."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r010');c=a.claim;q=a.question;e=a.e
refs=['5a:'+str(i) for i in range(13,25)]+['5b:1']
a.structure('marking',['5a:'+str(i) for i in range(13,23)],'Grave marking: received tradition and alternative scriptural indications')
a.structure('paths',['5a:23','5a:24','5b:1'],'Considering one’s ways: exposition and Rabbi Yannai’s student')
lemma=c('lemma','5a:13','מציינין את הקברות','The Mishnah clause requires marking graves.',scope='Repeated Mishnah lemma')
sq=q('simon_q','5a:13','רמז לציון קברות מן התורה מנין','What is the scriptural indication for grave marking?',candidates=['רבי שמעון בן פזי'])
sc=c('simon','5a:13','תלמוד לומר (יחזקאל לט, טו) וראה עצם אדם ובנה אצלו ציון','Rabbi Shimon ben Pazi adduces Ezekiel’s instruction to build a marker beside a human bone.',candidates=['רבי שמעון בן פזי'],scope='Scriptural indication; its historical relation to received practice is explained below')
e('simon_answer',sc,sq,'answer','5a:13');e('simon_support',sc,lemma,'support','5a:13')
rq=q('ravina_q','5a:14','א"ל רבינא לרב אשי הא מקמי דליתי יחזקאל מאן אמר','Ravina asks Rav Ashi who taught this before Ezekiel came.',candidates=['רבינא'])
e('ravina_challenge',rq,sc,'objection','5a:14')
ch=c('hisda','5a:14','הא דאמר רב חסדא דבר זה מתורת משה רבינו לא למדנו מדברי יחזקאל בן בוזי למדנו (יחזקאל מד, ט) כל בן נכר ערל לב וערל בשר לא יבא אל מקדשי (לשרתני)','The response cites Rav Hisda’s statement that the sanctuary exclusion of the uncircumcised in heart and flesh is learned from Ezekiel rather than the Torah of Moses.',candidates=['רב חסדא'],role='quoted_authority',composition='composite',scope='Quoted analogy in the reply; does not make Rav Hisda the speaker of the surrounding reply')
analog=q('analogy_q','5a:15','מקמי דליתי יחזקאל מאן אמר','The reply asks the same pre-Ezekiel question about the cited sanctuary rule.',uncertainty=['The reply follows an address to Rav Ashi but has no explicit new speaker label; retained as anonymous discussion.'])
trad=c('tradition','5a:15','אלא גמרא גמירי לה ואתא יחזקאל ואסמכה אקרא','The sanctuary rule was received by tradition; Ezekiel subsequently attached it to a verse.',scope='Resolution of the sanctuary-rule analogy')
mark=c('mark_tradition','5a:15','הכא נמי גמרא גמירי לה ואתא יחזקאל ואסמכה אקרא','Likewise grave marking was received by tradition and Ezekiel subsequently attached it to a verse.')
e('analog_support',ch,analog,'support','5a:14');e('trad_answer',trad,analog,'answer','5a:15');e('mark_answer',mark,rq,'answer','5a:15');e('trad_analogy',trad,mark,'support','5a:15')
ab=c('abahu','5a:16','רבי אבהו אמר מהכא (ויקרא יג, מה) וטמא טמא יקרא טומאה קוראה לו ואומרת לו פרוש','Rabbi Abahu reads the impurity call as impurity warning a person to keep away.',candidates=['רבי אבהו'])
uz=c('uzziel','5a:16','וכן אמר רבי עוזיאל בר בריה דרבי עוזיאל רבה טומאה קוראה לו ואומרת לו פרוש','Rabbi Uzziel, grandson of Rabbi Uzziel the Great, likewise interprets impurity as warning a person to keep away.',candidates=['רבי עוזיאל בר בריה דרבי עוזיאל רבה'])
e('abahu_support',ab,lemma,'support','5a:16');e('uzziel_support',uz,lemma,'support','5a:16')
oq=q('purpose_q','5a:17','והאי להכי הוא דאתא','Does this verse serve that purpose?')
pr=c('prayer','5a:17','ההוא מיבעי ליה לכדתניא וטמא טמא יקרא צריך להודיע צערו לרבים ורבים מבקשין עליו רחמים','A baraita requires making one’s distress known publicly so that others pray for mercy.',composition='composite',scope='Cited competing use of the verse')
e('purpose_challenge',oq,ab,'objection','5a:17');e('prayer_support',pr,oq,'support','5a:17')
double=c('double','5a:18','א"כ ליכתוב וטמא יקרא מאי וטמא טמא שמעת מינה תרתי','The repeated word טמא permits both derivations; one word would have sufficed for only one.',scope='Reconciliation retaining warning and public prayer')
e('double_answer',double,oq,'answer','5a:18');e('double_qualifies',double,pr,'qualification','5a:18')
derivations=[
('abaye','5a:19','אביי אמר מהכא (ויקרא יט, יד) ולפני עור לא תתן מכשול','אביי','Abaye adduces the prohibition against placing a stumbling block before the blind.'),
('pappa','5a:19','רב פפא אמר (ישעיהו נז, יד) ואמר סלו סלו פנו דרך','רב פפא','Rav Pappa adduces the instruction to clear a way.'),
('hinna','5a:20','רב חיננא אמר הרימו מכשול מדרך עמי','רב חיננא','Rav Hinna adduces removal of an obstacle from the people’s way.'),
('yehoshua','5a:20','ר\' יהושע בריה דרב אידי אמר (שמות יח, כ) והודעת להם את הדרך (אשר) ילכו בה','רבי יהושע בריה דרב אידי','Rabbi Yehoshua son of Rav Idi adduces making known the way people should walk.'),
('zutra','5a:21','מר זוטרא אמר (ויקרא טו, לא) והזרתם את בני ישראל מטומאתם','מר זוטרא','Mar Zutra adduces separating Israel from impurity.'),
('ashi','5a:21','רב אשי אמר (ויקרא יח, ל) ושמרתם את משמרתי עשו משמרת למשמרתי','רב אשי','Rav Ashi expounds guarding the divine charge as making a safeguard for it.'),
('ravina','5a:22','רבינא אמר (תהלים נ, כג) ושם דרך אראנו בישע אלהים','רבינא','Ravina adduces the verse about ordering a way and seeing divine salvation.')]
for key,ref,quote,name,text in derivations:
    cl=c(key,ref,quote,text,candidates=[name],scope='Alternative scriptural indication for grave marking; no incompatible practical ruling inferred')
    e(key+'_supports',cl,lemma,'support',ref)
levi=c('levi','5a:23','אריב"ל כל השם אורחותיו זוכה ורואה בישועתו של הקדוש ברוך הוא','Rabbi Yehoshua ben Levi says that one who considers one’s ways merits seeing divine salvation.',candidates=['רבי יהושע בן לוי'],conditions=['considering one’s ways'])
verse=c('levi_verse','5a:23','שנאמר ושם דרך אל תקרי ושם אלא ושם דרך אראנו בישע אלהים','Rabbi Yehoshua ben Levi adduces a reading of ושם דרך in support.',candidates=['רבי יהושע בן לוי'],scope='Scriptural exposition',uncertainty=['Unvocalized source prints ושם on both sides of אל תקרי; no unseen vocalization is fabricated.'])
e('levi_support',verse,levi,'support','5a:23')
student=c('student','5a:24','רבי ינאי הוה ליה ההוא תלמידא דכל יומא הוה מקשי ליה בשבתא דריגלא לא הוה מקשי ליה','Rabbi Yannai had a student who ordinarily questioned him but refrained on the festival Sabbath.',conditions=['the festival Sabbath'],scope='Anonymous narrative report, not a general legal rule')
praise=c('praise','5b:1','קרי עליה (תהלים נ, כג) ושם דרך אראנו בישע אלהים','Rabbi Yannai applied the verse ושם דרך אראנו בישע אלהים to the student.',candidates=['רבי ינאי'],naming_refs=['5a:24'],scope='Narrative continuation; Rabbi Yannai’s identity is inherited from the preceding segment')
e('praise_narrative',praise,student,'qualification','5b:1');e('student_example',student,levi,'support','5a:24')
a.save_window(refs,'resume_moed_katan_marking010b.json','Read original derivations and narrative with continuation through5b:20. Named exegetes distinguished from biblical voices; alternatives need not be disputes; anonymous reply and unvocalized ambiguity preserved.','bab8114c03ace3430edf6834035c39aaa70169cf0a34da93c34ec07efe7d39cd')
