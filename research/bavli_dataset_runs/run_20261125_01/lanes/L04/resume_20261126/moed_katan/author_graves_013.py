"""Source reading: marking rules, field categories, boundary evidence5b:2–6a:8."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r013');c=a.claim;e=a.e
def q(*args,**kwargs):
    result=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial'
    a.rows[-1]['uncertainty'].append('Source-present reply retained; no exhaustive alternative inventory or answer-set eligibility asserted.')
    return result
refs=['5b:'+str(i) for i in range(2,21)]+['6a:'+str(i) for i in range(1,9)]
a.structure('rules',['5b:'+str(i) for i in range(2,6)],'Objects and uncertainty warranting grave markers; precise olive-size exception')
a.structure('fields',['5b:'+str(i) for i in range(6,21)]+['6a:'+str(i) for i in range(1,4)],'Canopies, protrusions and grave fields; field identification and communal responsibility')
a.structure('stones',['6a:'+str(i) for i in range(4,9)],'Marked stones and boundaries: lime, ploughing, and location of impurity')
for key,quote,text,condition in [
('olive','אין מציינין לא על כזית מן המת','The baraita does not require marking an olive-size portion of a corpse.','olive-size portion; subsequently limited to exactly that size'),
('bone','ולא על עצם כשעורה','The baraita does not require marking a barley-size bone.','barley-size bone'),
('no_tent','ולא על דבר שאינו מטמא באהל','The baraita does not require marking an object that does not impart tent impurity.','no tent impurity'),
('spine','אבל מציינין על השדרה','The baraita requires marking a spine.','spine'),
('skull','ועל הגולגולת','The baraita requires marking a skull.','skull'),
('build','על רוב בנין','The baraita requires marking most of the bodily structure.','most of bodily structure'),
('number','ועל רוב מנין המת','The baraita requires marking most of the corpse’s bone count.','majority by count')]:
    c(key,'5b:2',quote,text,conditions=[condition],scope='Anonymous quoted baraita')
known=c('known','5b:3','ואין מציינין על הוודאות','Certain impurity is not marked under the cited rule.',conditions=['certain impurity'],scope='Quoted marking rule; no added unstated rationale')
doubt=c('doubt','5b:3','אבל מציינין על הספיקות','Doubtful impurity is marked.',conditions=['doubtful impurity'])
kinds=c('doubt_kinds','5b:3','ואלו הן הספיקות סככות ופרעות ובית הפרס','The listed doubtful cases are overhangs, protrusions, and beit hapras.',composition='composite')
at=c('not_at','5b:3','ואין מעמידין ציון במקום טומאה שלא להפסיד את הטהרות','A marker is not placed at the impurity itself, to avoid loss of pure things.',conditions=['location of marker'],composition='composite')
far=c('not_far','5b:3','ואין מרחיקין ציון ממקום טומאה שלא להפסיד את ארץ ישראל','A marker is not placed far from the impurity, to avoid unnecessary loss of land in Israel.',conditions=['distance of marker'],composition='composite')
oq=q('olive_q','5b:4','וכזית מן המת אינו מטמא באהל','Does an olive-size portion of a corpse not impart tent impurity?')
proof=c('olive_tent','5b:4','והא (תניא) אלו שמטמאין באהל כזית מן המת','A cited teaching includes an olive-size portion among objects imparting tent impurity.')
e('olive_challenge',oq,'mk.r013.olive.c','objection','5b:4');e('olive_proof',proof,oq,'support','5b:4')
exact=c('exact','5b:5','אמר רב פפא הכא בכזית מצומצם עסקינן דסוף סוף מיחסר חסר','Rav Pappa limits the unmarked case to exactly an olive’s size, which will eventually diminish.',candidates=['רב פפא'],conditions=['exactly an olive-size portion'],composition='composite')
cost=c('cost','5b:5','מוטב ישרפו עליו תרומה וקדשים לפי שעה ואל ישרפו עליו לעולם','The explanation prefers temporary burning of terumah and sacred food because of that impurity over indefinite burning because of a lasting marker.',candidates=['רב פפא'],naming_refs=['5b:5'],scope='Continuation of Rav Pappa’s explanation; cost comparison, not denial of present impurity')
e('exact_answer',exact,oq,'answer','5b:5');e('cost_support',cost,exact,'support','5b:5')
repeat=c('repeat','5b:6','ואלו הן הספיקות סככות ופרעות','The discussion repeats the baraita’s overhang and protrusion categories.',composition='composite',scope='Repeated lemma, retained as a parallel source occurrence')
canopy=c('canopy','5b:7','סככות אילן המיסך על הארץ','Overhangs are defined as a tree spreading over the ground.')
protrude=c('protrude','5b:8','פרעות אבנים פרועות היוצאות מן הגדר','Protrusions are defined as stones projecting from a wall.')
plough=c('plough','5b:9','בית הפרס כדתנן החורש את הקבר הרי הוא עושה בית הפרס','A quoted Mishnah calls the area made by ploughing a grave beit hapras.')
measureq=q('measure_q','5b:9','וכמה הוא עושה','How large an area does this create?')
measure=c('measure','5b:9','מלא מענה מאה אמה','The cited measure is a full furrow, one hundred cubits.')
e('measure_answer',measure,measureq,'answer','5b:9')
tentq=q('field_q','5b:10','ובית הפרס מי מטמא באהל','Does beit hapras impart tent impurity?')
blow=c('blow','5b:10','והאמר רב יהודה אמר שמואל מנפח אדם בית הפרס והולך','Rav Yehuda reports Shmuel permitting a person to blow over beit hapras and proceed.',candidates=['שמואל'],role='quoted_authority',chain=['רב יהודה','שמואל'])
trodden=c('trodden','5b:11','ורב יהודה בר אמי משמיה דעולא אמר בית הפרס שנידש טהור','Rav Yehuda bar Ammi reports Ulla that a trampled beit hapras is pure.',candidates=['עולא'],role='quoted_authority',chain=['רב יהודה בר אמי','עולא'],conditions=['field trampled'])
e('blow_support',blow,tentq,'support','5b:10');e('trodden_support',trodden,tentq,'support','5b:11');e('field_challenge',tentq,plough,'objection','5b:10')
dist=c('distinguish','5b:12','אמר רב פפא לא קשיא כאן בשדה שאבד בה קבר כאן בשדה שנחרש בה קבר','Rav Pappa distinguishes a field containing a lost grave from a field where a grave was ploughed: the latter explains the permissive reports, while the lost grave explains the marking context.',candidates=['רב פפא'],conditions=['lost grave versus ploughed grave'],composition='composite')
e('dist_answer',dist,tentq,'answer','5b:12')
termq=q('term_q','5b:13','ושדה שנחרש בה קבר בית הפרס קרי ליה','Is a field where a grave was ploughed called beit hapras?')
yes=c('term_yes','5b:13','אין והתנן שלשה בית הפרס הן שדה שנאבד בה קבר ושדה שנחרש בה קבר ושדה בוכין','Yes: a quoted Mishnah lists a field with a lost grave, a field with a ploughed grave, and a mourning field as three beit hapras categories.',composition='composite',uncertainty=['Preserves the printed question about the ploughed field even though the preceding citation already used that term; no silent emendation to lost grave.'])
e('term_answer',yes,termq,'answer','5b:13')
mournq=q('mourn_q','5b:14','מאי שדה בוכין','What is a mourning field?')
mourn=c('mourn','5b:14','רב יהושע בר אבא משמיה דעולא אמר שדה שמפטירין בה מתים','Rav Yehoshua bar Abba reports Ulla: it is a field where the dead are sent off.',candidates=['עולא'],role='quoted_authority',chain=['רב יהושע בר אבא','עולא'],scope='Technical description retained without adding an unstated burial practice')
e('mourn_answer',mourn,mournq,'answer','5b:14')
why=q('mourn_why','5b:15','וטעמא מאי','What is the reason for the mourning field’s status?')
despair=c('despair','5b:15','אמר אבימי משום יאוש בעלים נגעו בה','Avimi explains it in terms of the owners’ abandonment.',candidates=['אבימי'],uncertainty=['The terse phrase does not spell out its full legal mechanism; no additional mechanism is fabricated.'])
e('despair_answer',despair,why,'answer','5b:15')
markq=q('plough_mark_q','5b:16','ושדה שנחרש בה קבר לא בעי ציון','Does a field with a ploughed grave not require marking?')
trees=c('trees','5b:16','מצא שדה מצויינת ואין ידוע מה טיבה יש בה אילנות בידוע שנחרש בה קבר','A cited baraita identifies an already marked field with trees as one where a grave was ploughed.',conditions=['field already marked','its nature unknown','trees present'])
notrees=c('no_trees','5b:16','אין בה אילנות בידוע שאבד בה קבר','Without trees the cited baraita identifies the marked field as one containing a lost grave.',conditions=['field already marked','its nature unknown','trees absent'])
elder=c('elder','5b:17','ר\' יהודה אומר עד שיהא שם זקן או תלמיד לפי שאין הכל בקיאין בדבר','Rabbi Yehuda requires an elder or student to be present because not everyone is expert in the matter.',candidates=['רבי יהודה'],role='quoted_authority',conditions=['knowledgeable elder or student present'],composition='composite')
e('trees_support',trees,markq,'support','5b:16');e('elder_qualifies',elder,trees,'qualification','5b:17')
history=c('history','5b:18','אמר רב פפא כי תניא ההיא בשדה שאבד בה קבר דציינוה','Rav Pappa places the baraita in a field originally marked because a grave was lost there.',candidates=['רב פפא'],conditions=['original marking for a lost grave'])
treehistory=c('tree_history','5b:18','יש בה אילנות בידוע שנחרש בה קבר אין בה אילנות בידוע שאבד בה קבר','Under that history, trees indicate that a grave was subsequently ploughed; their absence indicates the lost-grave condition.',candidates=['רב פפא'],naming_refs=['5b:18'],conditions=['previously marked because of a lost grave'],composition='composite')
e('history_answer',history,markq,'answer','5b:18');e('history_qualifies',treehistory,trees,'qualification','5b:18')
innerq=q('inner_q','5b:19','וליחוש דלמא אילנות מגואי וקבר מבראי','Should we not worry that the trees are inside and the grave outside?')
border=c('border','5b:20','כדאמר עולא בעומדין על הגבולין הכא נמי בעומדין על הגבולין','The discussion applies Ulla’s boundary-tree explanation here as well.',candidates=['עולא'],role='quoted_authority',conditions=['trees stand on boundaries'],uncertainty=['Ulla is the cited authority for the analogous explanation; the anonymous application here is not asserted as his own direct speech.'])
e('inner_challenge',innerq,treehistory,'objection','5b:19');e('border_answer',border,innerq,'answer','5b:20')
outerq=q('outer_q','6a:1','ודלמא טומאה מגואי ואילנות מבראי','Perhaps the impurity is inside and the trees outside?')
interlace=c('interlace','6a:2','במסובכין','One reply places the case where the trees are interlaced.',conditions=['interlaced trees'])
near=c('near','6a:2','ואיבעית אימא הא אמרן אין מרחיקין ציון ממקום טומאה שלא להפסיד את א"י','An alternative invokes the rule against placing markers far from impurity, to avoid unnecessary loss of land in Israel.',conditions=['markers placed near impurity'])
e('outer_challenge',outerq,border,'objection','6a:1');e('interlace_answer',interlace,outerq,'answer','6a:2');e('near_answer',near,outerq,'answer','6a:2');e('near_repeat',far,near,'support','6a:2')
elderrepeat=c('elder_repeat','6a:3','ר\' יהודה אומר עד שיהא שם זקן או תלמיד לפי שאין הכל בקיאין בדבר','The discussion repeats Rabbi Yehuda’s expert-presence requirement.',candidates=['רבי יהודה'],role='quoted_authority',conditions=['elder or student present'],scope='Repeated source occurrence, not a new independent ruling')
ab=c('abaye','6a:3','אמר אביי שמע מינה צורבא מרבנן דאיכא במתא כל מילי דמתא עליה רמיא','Abaye infers that a scholar residing in a town bears responsibility for all the town’s affairs.',candidates=['אביי'],conditions=['scholar residing in the town'])
e('abaye_support',elderrepeat,ab,'support','6a:3')
one=c('stone_one','6a:4','אמר רב יהודה מצא אבן מצויינת תחתיה טמא','Rav Yehuda says that beneath a marked stone is impure.',candidates=['רב יהודה'],conditions=['one marked stone'])
lime=c('stone_lime','6a:4','שתים אם יש סיד ביניהן ביניהן טמא','For two marked stones, lime between them indicates impurity between them.',candidates=['רב יהודה'],conditions=['two marked stones','lime between them'])
nolime=c('stone_no_lime','6a:4','ואם אין סיד ביניהן ביניהן טהור','Without lime between the two stones, the intervening area is pure.',candidates=['רב יהודה'],conditions=['two marked stones','no lime between'])
ploughq=q('stone_q','6a:5','ואע"ג דליכא חורש','Does that hold even without ploughing?')
barone=c('baraita_one','6a:5','מצא אבן אחת מצויינת תחתיה טמא','A cited baraita likewise declares the ground beneath one marked stone impure.',conditions=['one marked stone'])
barpl=c('baraita_plough','6a:5','שתים אם יש חורש ביניהן ביניהן טהור','For two marked stones, the baraita declares the intervening area pure if ploughing lies between them.',conditions=['two marked stones','intervening ploughing'])
barnopl=c('baraita_no_plough','6a:5','ואם לאו ביניהן טמא','Without intervening ploughing, the baraita declares the area between them impure.',conditions=['two marked stones','no intervening ploughing'])
e('stone_challenge',ploughq,nolime,'objection','6a:5');e('baraita_support',barnopl,ploughq,'support','6a:5')
spread=c('spread','6a:6','אמר רב פפא הכא כשהסיד שפוך על ראשיהן ומרודה לכאן ולכאן','Rav Pappa explains the baraita as lime poured on the stones’ tops and spreading to either side.',candidates=['רב פפא'],conditions=['lime on tops spreading to sides'])
shift=c('shift','6a:6','אי איכא חורש ביניהן ביניהן טהור דאימור מחמת חורש הוא דאיקפל','With intervening ploughing the area is pure, because the lime may have been dislodged by ploughing.',candidates=['רב פפא'],conditions=['spreading lime','intervening ploughing'],composition='composite')
intent=c('intent','6a:6','ואי לא סיד דביני ביני הוא וטמא','Without ploughing the lime marks the intervening area as impure.',candidates=['רב פפא'],conditions=['spreading lime','no intervening ploughing'])
e('spread_answer',spread,ploughq,'answer','6a:6');e('shift_qualifies',shift,barpl,'qualification','6a:6');e('intent_qualifies',intent,barnopl,'qualification','6a:6')
for key,quote,count,text in [
('boundary1','א"ר אסי מצר אחד מצוין הוא טמא וכל השדה כולה טהורה',1,'One marked boundary is impure, while the entire field is pure.'),
('boundary2','שנים הם טמאין וכל השדה כולה טהורה',2,'Two marked boundaries are impure, while the entire field is pure.'),
('boundary3','שלשה הם טמאין וכל השדה כולה טהורה',3,'Three marked boundaries are impure, while the entire field is pure.'),
('boundary4','ארבעה הן טהורין וכל השדה כולה טמאה',4,'Four marked boundaries are pure, while the entire field is impure.')]:
    cl=c(key,'6a:7',quote,'Rav Asi teaches: '+text,candidates=['רב אסי'],conditions=[str(count)+' marked boundaries'],composition='composite')
reason=c('boundary_reason','6a:8','דאמר מר אין מרחיקין ציון ממקום טומאה שלא להפסיד את א"י','The explanation cites the rule against distancing markers from impurity, to avoid unnecessary loss of land in Israel.',scope='Anonymous explanatory continuation')
e('boundary_support',reason,'mk.r013.boundary4.c','support','6a:8')
a.save_window(refs,'resume_moed_katan_graves013.json','Original5b:2–6a:8 read with continuation through6b:16. Conditions and repeated sources retained; printed5b:13 tension flagged rather than emended; explicit replies recorded as partial without exhaustive inventory.','849a65e15c05ec5ea4dc6c6d82462aef15507e8d6c2a4b59c8fe8141681b7e1c')
