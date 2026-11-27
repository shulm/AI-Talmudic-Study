"""Direct source reading11b:1–13 with contractor continuation through12b."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r029');c=a.claim;e=a.e
refs=['11b:'+str(i) for i in range(1,14)]
def q(*args,**kwargs):
 v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Source-present replies only; no exhaustive alternatives or certification.');return v
a.structure('olives',refs[:4],'Mishnah of prepared olives and mourning versus festival work')
a.structure('baraita',refs[4:11],'Work performed for mourners, exceptions and employment arrangements')
a.structure('partners',refs[11:],'Partnership animal stopped during mourning and distinguished personal status')
y=c('yehuda','11b:1',"שהפך את זיתיו ואירעו אבל או אונס או שהטעוהו פועלים טוען קורה ראשונה ומניחה לאחר המועד דברי ר' יהודה",'For prepared olives interrupted by mourning, unavoidable circumstances or failed workers, Rabbi Yehuda allows a first press beam and leaves the rest until after the festival.',candidates=['רבי יהודה'],conditions=['olives already turned','mourning, unavoidable event or workers failed him'],composition='composite')
yose=c('yose','11b:2','רבי יוסי אומר זולף וגומר וגף כדרכו','Rabbi Yose permits drawing off, completing and sealing in the usual way.',candidates=['רבי יוסי'],composition='composite',scope='Same Mishnah circumstances')
opening=q('opening','11b:3','פתח באבל וסיים במועד','Why does the Mishnah begin with mourning and end with the festival?')
shisha=c('shisha','11b:3','אמר רב שישא בריה דרב אידי זאת אומרת דברים המותרין במועד אסורים בימי אבלו','Rav Shisha son of Rav Idi infers that work permitted during the festival is prohibited during mourning.',candidates=['רב שישא בריה דרב אידי'],scope='Interpretation of Mishnah wording; baraita below supplies work done by others and exceptions')
ashi=c('ashi','11b:4','רב אשי אמר לא מיבעיא קאמר','Rav Ashi reads the Mishnah as a not-only formulation.',candidates=['רב אשי'])
mourning=c('mourning','11b:4','לא מיבעיא בימי אבלו דמדרבנן הוא ושרי','Rav Ashi says permission in mourning is unsurprising because its work restriction is rabbinic.',candidates=['רב אשי'],scope='Premise of Rav Ashi’s explanation, not a consensus statement about every mourning rule')
festival=c('festival','11b:4','אלא אפילו במועד דאיסור מלאכה מדאורייתא במקום פסידא שרו רבנן','He adds that even festival labor, described here as prohibited by Torah law, is permitted by the sages in a case of loss.',candidates=['רב אשי'],conditions=['loss'],scope='Rav Ashi’s own formulation preserved, not harmonized with later views')
e('shisha_answer',shisha,opening,'answer','11b:3');e('ashi_answer',ashi,opening,'answer','11b:4');e('mourning_reason',mourning,ashi,'support','11b:4');e('festival_reason',festival,ashi,'support','11b:4')
barintro=c('barintro','11b:5','תניא כוותיה דרב שישא בריה דרב אידי','A baraita is introduced as supporting Rav Shisha son of Rav Idi.')
e('bar_support',barintro,shisha,'support','11b:5')
for key,quote,text in [('olives','זיתיו הפוכין טוענין לו','Others press his prepared olives.'),('seal','וכדו לגוף','Others seal his jar.'),('flax','ופשתנו להעלות מן המשרה','Others remove his flax from soaking.'),('wool','וצמרו להעלות מן היורה','Others remove his wool from the vat.'),('field','ומרביצים שדהו משתגיע עונת המים שלו','Others irrigate his field when his water turn arrives.')]:
 c(key,'11b:5',quote,text,conditions=['for a mourner during mourning']+(['his allotted water turn has arrived'] if key=='field' else []),scope='Baraita explicitly describes work performed for the mourner')
sow=c('sow','11b:6',"ר' יהודה אומר אף זורעין לו שדה ניר ושדה העומדת לפשתן",'Rabbi Yehuda also allows sowing his ploughed field and a field intended for flax.',candidates=['רבי יהודה'],conditions=['work done for mourner'],composition='composite')
late=c('late','11b:6','אמרו לו אם לא תזרע בבכיר תזרע באפל','The respondents say that if early sowing is missed, late sowing is possible.',scope='Anonymous plural response')
other=c('other','11b:6','אם לא תזרע פשתן תזרע ממין אחר','They add that if flax is not sown, another crop can be sown.',scope='Second anonymous objection rationale')
e('late_objection',late,sow,'objection','11b:6');e('other_objection',other,sow,'objection','11b:6')
for key,quote,text in [('olives_self','זיתיו הפוכין ואין שם אומן אלא הוא','Prepared olives when the mourner is the only available skilled worker.'),('jar_self','כדו לגוף ואין שם אומן אלא הוא','Sealing his jar when he alone is available.'),('fiber_self','פשתנו להעלות מן המשרה וצמרו להעלות מן היורה ואין שם אומן אלא הוא','Removing flax from soaking and wool from the vat when he alone is available.')]:
 c(key,'11b:7',quote,text,candidates=['רבן שמעון בן גמליאל'],conditions=['no other skilled worker'],scope='Cases for the following permission to work privately',composition='composite' if key=='fiber_self' else 'atomic')
private=c('private','11b:7','הרי זה יעשה בצינעא','Rabban Shimon ben Gamliel permits the mourner to do the listed work privately.',candidates=['רבן שמעון בן גמליאל'],conditions=['listed loss-related operations','no other skilled worker','in private'])
public=c('public','11b:8','אם היה אומן לרבים וספר ובלן לרבים והגיע עת הרגל ואין שם אומן אלא הוא הרי זה יעשה','Rabban Shimon ben Gamliel additionally permits work by a public artisan, barber or bath attendant when the festival has arrived and no other skilled worker is available.',candidates=['רבן שמעון בן גמליאל'],conditions=['serves the public','festival time','no other skilled worker'],composition='composite')
farms=c('farms','11b:9','האריסין והחכירין והקבלנין הרי אלו יעשו אחרים בשבילן','For sharecroppers, tenants and contractors, others perform the work for them.',composition='composite',scope='Mourning employment rules')
transport=c('transport','11b:9','החמרין הגמלין והספנין הרי אלו לא יעשו','Donkey drivers, camel drivers and sailors do not work.',composition='composite',scope='Mourning employment rules, qualified by following hired/leased arrangement')
hired=c('hired','11b:9','ואם היו מוחכרין או מושכרין אצל אחרים הרי אלו יעשו','If hired or leased to others, work is performed.',conditions=['hired or leased to others'],composition='composite')
e('hired_exception',hired,transport,'qualification','11b:9')
day=c('day','11b:9','שכיר יום אפילו בעיר אחרת לא יעשה','A day laborer does not work even in another city.',conditions=['day laborer','even another city'])
others=c('others','11b:9','היתה מלאכת אחרים בידו אע"פ שבקיבולת לא יעשה','For another person’s work in his possession, the initial wording prohibits even contracted work.',scope='Initial even-contracted wording corrected next')
why=q('why','11b:10','אף על פי שבקיבולת ולא מיבעיא שאינה קיבולת','Does even-contracted imply that non-contracted work is more obviously prohibited?')
reverse=c('reverse','11b:10','אדרבה קיבולת כדידיה דמי','The objection is that contracted work instead resembles his own work.')
reword=c('reword','11b:10','אלא אימא בין קיבולת בין שאינה קיבולת לא יעשה','The wording is corrected to prohibit both contracted and non-contracted work.',composition='composite')
e('reverse_objection',reverse,others,'objection','11b:10');e('reword_answer',reword,why,'answer','11b:10');e('reword_corrects',reword,others,'correction','11b:10')
home=c('home','11b:11','היתה מלאכתו ביד אחרים בביתו לא יעשו','If his work is held by others, they do not perform it in his house.',conditions=['his work held by others','in his house'])
elsewhere=c('elsewhere','11b:11','בבית אחר יעשו','They may perform it in another house.',conditions=['his work held by others','another house'])
partners=c('partners','11b:12','מריון בריה דרבין ומר בריה דרב אחא בריה דרבא הוה להו ההוא גמלא דתורא בהדי הדדי','Maryon son of Ravin and Mar son of Rav Aha son of Rava jointly held a גמלא דתורא.',scope='Partnership narrative; technical animal designation preserved',composition='composite')
stopped=c('stopped','11b:12','איתרעא ביה מילתא במר בריה דרב אחא בריה דרבא ופסקיה לגמליה','Mar son of Rav Aha son of Rava suffered bereavement and stopped his animal’s work.',scope='Narrative action')
greatq=q('great_q','11b:12','אמר רב אשי גברא רבה כמר בריה דרב אחא עביד הכי','Rav Ashi asks whether a great person like Mar son of Rav Aha acts this way.',candidates=['רב אשי'])
otherq=q('other_q','11b:12','נהי דלפסידא דידיה לא חייש אדאחרים לא חייש','Even if unconcerned about his own loss, is he unconcerned about others’ loss?',candidates=['רב אשי'])
proof=c('proof','11b:12','והא תניא אם היו מושכרין או מוחכרין אצל אחרים הרי אלו יעשו','Rav Ashi cites the permission for hired or leased work involving others.',candidates=['רב אשי'],role='quoted_authority',scope='Baraita cited against the stoppage')
important=c('important','11b:13','והוא סבר אדם חשוב שאני','The narrative explains that the actor regarded an important person as different.',scope='Anonymous account of Mar’s rationale; not an explicit later consensus')
e('proof_objection',proof,stopped,'objection','11b:12');e('important_answer',important,greatq,'answer','11b:13');e('important_answer2',important,otherq,'answer','11b:13')
a.save_window(refs,'resume_moed_katan_mourners029.json','Read11b with continuation through12b. Preserve lists, mourning/festival distinction, two readings, anonymity, no-other-worker/private/public conditions, employment and location categories, corrected wording and partnership narrative with actor-specific important-person explanation.','36054a317a76bfb04699b333a3af0ac8993ef5653b5c8290dbb1bdfa1f29da96')
