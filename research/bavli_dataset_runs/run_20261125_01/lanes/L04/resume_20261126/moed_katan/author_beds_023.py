"""Source reading10a:1–10, both bed-weaving reports and unresolved challenge."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r023');c=a.claim;e=a.e
refs=['10a:'+str(i) for i in range(1,11)]
def q(*args,answered=True,**kwargs):
    v=a.question(*args,**kwargs)
    if answered:a.rows[-1]['content']['answer_set_status']='partial'
    a.rows[-1]['uncertainty'].append('Represented local reply only; not an exhaustive set or task qualification.' if answered else 'The local challenge remains קשיא; no answer fabricated.')
    return v
a.structure('sewing',refs[:2],'Definitions of unskilled sewing and the artisan’s altered stitch')
a.structure('beds',refs[2:],'Rav Dimi and Ravin reports, corrections, and the scope of bed work')
lay=q('lay_q','10a:1','היכי דמי הדיוט','Who counts as unskilled?')
needle=c('needle','10a:1','אמרי דבי רבי ינאי כל שאינו יכול להוציא מלא מחט בבת אחת','The school of Rabbi Yannai defines the unskilled person as one unable to draw out a needleful in one operation.',candidates=['דבי רבי ינאי'])
hem=c('hem','10a:1','רבי יוסי בר חנינא אמר כל שאינו יכול לכוין אימרא בחפת חלוקו','Rabbi Yose bar Hanina defines the unskilled person by inability to align the edging at the garment opening.',candidates=['רבי יוסי בר חנינא'],uncertainty=['Technical garment terms are paraphrased conservatively; no reconstructed sewing diagram.'])
e('needle_answer',needle,lay,'answer','10a:1');e('hem_answer',hem,lay,'answer','10a:1')
stitch=q('stitch_q','10a:2','מאי מכליב','What does מכליב mean?')
spaced=c('spaced','10a:2','רבי יוחנן אמר מפסיע','Rabbi Yohanan explains it as spaced stitching.',candidates=['רבי יוחנן'])
teeth=c('teeth','10a:2','רבה בר שמואל אמר שיני כלבתא','Rabbah bar Shmuel explains it as stitches like a dog’s teeth.',candidates=['רבה בר שמואל'],uncertainty=['Do not identify רבה בר שמואל with Rav or Shmuel.'])
e('spaced_answer',spaced,stitch,'answer','10a:2');e('teeth_answer',teeth,stitch,'answer','10a:2')
bedq=q('bed_q','10a:3','מאי מסרגין ומאי ממתחין','What do מסרגין and ממתחין mean?',composition='composite')
report=c('dimi_report','10a:3',"כי אתא רב דימי אמר פליגי בה ר' חייא בר אבא ור' אסי ותרוייהו משמיה דחזקיה ור' יוחנן",'Rav Dimi reports disagreement involving Rabbi Hiyya bar Abba and Rabbi Asi, both transmitting in the names of Hizkiya and Rabbi Yohanan.',candidates=['רב דימי'],scope='Transmission report; the following anonymous pair is not allocated by name order',composition='composite',uncertainty=['No one-to-one assignment of the two formulations to the named transmitters or authorities is supplied.'])
first=c('first','10a:3','חד אמר מסרגין שתי וערב וממתחין שתי בלא ערב','One account defines מסרגין as warp and weft and ממתחין as warp without weft.',candidates=['unassigned member of reported pair'],composition='composite',scope='Rav Dimi’s first unassigned formulation')
second=c('second','10a:3','וחד אמר מסרגין שתי בלא ערב וממתחין שאם היה רפוי ממתחו','The other defines מסרגין as warp without weft and ממתחין as tightening what was loose.',candidates=['unassigned member of reported pair'],composition='composite',mode='challenged',scope='Rav Dimi’s second unassigned formulation; later challenged, not silently erased')
e('first_answer',first,bedq,'answer','10a:3');e('second_answer',second,bedq,'answer','10a:3')
rope=c('rope','10a:4','והא תני רב תחליפא בר שאול ושוין שאין מפשילין חבלים לכתחלה','Rav Tahlifa bar Shaul teaches agreement that ropes may not be newly twisted.',candidates=['רב תחליפא בר שאול'],conditions=['initial production of ropes'],role='quoted_authority')
fit=c('fit','10a:4','בשלמא למאן דאמר מסרגין שתי וערב וממתחין שתי בלא ערב','The discussion finds this intelligible under the warp-and-weft definition of מסרגין.',scope='Compatibility observation concerning the first report')
need=q('need','10a:5','השתא שתי וערב אמרת לא חבלים לכתחלה מיבעיא','If even warp and weft are excluded, is an exclusion of new ropes necessary?',answered=False)
remain=c('remain','10a:5','קשיא','This challenge is left difficult.',mode='unresolved',scope='Local outcome for the challenged Rav Dimi formulation')
e('need_objection',need,second,'objection','10a:5');e('remain_outcome',remain,need,'unresolved_outcome','10a:5')
anyq=q('any','10a:6','מי איכא למאן דאמר מסרגין שתי בלא ערב','Is there anyone who defines מסרגין as warp without weft?',candidates=['רב נחמן בר יצחק'])
meir=c('meir','10a:6','והתנן רבי מאיר אומר המטה משיסרוג בה שלשה בתים','Rav Nahman bar Yitzhak addresses Rabbi Hiyya bar Avin and cites Rabbi Meir’s three interlaced spaces in the bed.',candidates=['רבי מאיר'],role='quoted_authority',chain=['רב נחמן בר יצחק','רבי מאיר'],scope='Quoted Mishnah used against the warp-only definition')
e('meir_objection',meir,second,'objection','10a:6')
ravin=c('ravin','10a:7','אלא כי אתא רבין אמר במסרגין כולי עלמא לא פליגי דשתי וערב','Ravin instead reports agreement that מסרגין means warp and weft.',candidates=['רבין'],scope='Alternative corrected transmission, not proof of a personal retraction by Rav Dimi')
warp=c('warp','10a:7','מר סבר ממתחין שתי בלא ערב','One unassigned authority defines ממתחין as warp without weft.',candidates=['unassigned member of reported pair'],scope='Ravin’s report')
tight=c('tight','10a:7','ומר סבר שאם היה רפוי ממתחו','The other defines it as tightening a loose bed.',candidates=['unassigned member of reported pair'],scope='Ravin’s report')
e('ravin_corrects',ravin,second,'correction','10a:7');e('ravin_answer',ravin,anyq,'answer','10a:7');e('warp_answer',warp,bedq,'answer','10a:7');e('tight_answer',tight,bedq,'answer','10a:7')
permit=c('permit','10a:8',"מסרגין את המטה ואין צריך לומר שממתחין דברי ר' מאיר",'Rabbi Meir permits מסרגין and, all the more, ממתחין.',candidates=['רבי מאיר'],composition='composite')
yose=c('yose','10a:8',"ר' יוסי אומר ממתחין אבל לא מסרגין",'Rabbi Yose permits ממתחין but excludes מסרגין.',candidates=['רבי יוסי'],composition='composite')
others=c('others','10a:8','וי"א אין ממתחין כל עיקר','The anonymous other opinion disallows ממתחין altogether.',candidates=['יש אומרים'])
fit2=c('fit2','10a:9','בשלמא למאן דאמר ממתחין שתי בלא ערב היינו דאתו יש אומרים לאיפלוגי','The discussion finds the other opinion intelligible if ממתחין means warp without weft.')
looseq=q('loose_q','10a:9','אלא למאן דאמר שאם היה רפוי ממתחו ליש אומרים ממתחו נמי לא','On the tightening interpretation, do the others exclude even tightening a loose bed?')
clothes=c('clothes','10a:10','אין כיון דאפשר לממלייה במאני לא טרחינן','Yes: because the bed can be filled with clothes, the work is not undertaken.',conditions=['possible to fill the bed with clothes'],scope='Answer defending the restrictive other opinion; no attribution by anonymous-pair order')
e('loose_challenge',looseq,tight,'objection','10a:9');e('clothes_answer',clothes,looseq,'answer','10a:10');e('clothes_support',clothes,others,'support','10a:10')
a.save_window(refs,'resume_moed_katan_beds023.json','Direct reading10a:1–10 with subsequent mills and work context. Preserve named transmitters, both unassigned pairs, Ravin alternative report, local unresolved קשיא, three baraita opinions and clothing condition. No assignment by name order or later practical ruling.','09908653624cc6ad0a45a5261a2ffa41b90fb6a681708943a5aedb814801304b')
