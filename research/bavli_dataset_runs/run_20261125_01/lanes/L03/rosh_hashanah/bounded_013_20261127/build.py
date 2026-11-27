"""Serialize a manual source reading; no semantic heuristics or paid APIs."""
import json,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah')
BASE='afd5ec0fbdf7ce7635e917a1068ac649193a5f9db692d1ac1b5e2925617e7557'
job,allsegs=runner.load(J);assert runner.sha(runner.encoded(runner.current(J)))==BASE
assert json.loads((J/'OWNER.json').read_text())=={'owner':'L03/rosh_hashanah','epoch':3}
segments={s['ref'].removeprefix('Rosh Hashanah '):s for s in allsegs.values()}
p={k:job[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']}
p.update(owner='L03/rosh_hashanah',epoch=3,execution={'route':'interactive_agent','agent_id':'/root/rosh_hashanah','model_id':None},records=[],coverage=[],open_tails=[])
prefix='rh.e3.b013.';C={};Q={}
def ev(ref,quote=None):
 s=segments[ref];t=s['text'];quote=t if quote is None else quote;i=t.index(quote)
 return dict(segment_id=s['id'],start_char=i,end_char=i+len(quote),quote=quote)
def add(k,l,r,c,quote=None,links=(),unc=(),origin='source_paraphrase'):
 rid=prefix+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(r,quote)],content=c,links=list(links),uncertainty=list(unc),origin=origin));return rid
def claim(k,r,prop,quote=None,holder='anonymous Gemara',cond=(),mode='asserted',status='Asserted at local source stage; no external halakhic qualification',unc=()):
 C[k]=add(k,'claims',r,dict(proposition=prop,conditions=list(cond),scope='Sabbatical/Jubilee calendar, added sacred time and Jubilee prerequisites; source interpretation only',assertion_mode=mode),quote,unc=unc)
 add(k+'.p','positions',r,dict(holder_candidates=[holder],claim_id=C[k],question_id=None,conditions=list(cond),local_status=status),quote,links=[C[k]],unc=unc);return C[k]
def question(k,r,form,quote=None):Q[k]=add(k,'questions',r,dict(formulation=form,question_origin='explicit',conditions=[],answer_set_status='partial'),quote);return Q[k]
def edge(k,r,s,t,rel,quote=None):return add(k,'edges',r,dict(source_id=s,target_id=t,relation=rel,explicitness='source_explicit'),quote,links=[s,t])
def attribution(k,r,surface,role,scope,quote=None,chain=(),candidates=None):return add(k,'attributions',r,dict(surface=surface,role=role,candidates=[surface] if candidates is None else candidates,scope=scope,transmission_chain=list(chain)),quote)
refs=['8b:'+str(i) for i in range(6,13)]+['9a:'+str(i) for i in range(1,9)]+['9b:'+str(i) for i in range(1,6)]
for key,rr,title,bound in [('s1',refs[:2],'Tishrei derivation for sabbatical years','closed'),('s2',refs[2:8],'Jubilee opening, release stages and year-fifty boundary','closed'),('s3',refs[8:16],'Adding ordinary time to sacred time and ninth-day eating credit','closed'),('s4',refs[16:],'Which Jubilee acts are indispensable? Core ends within Rabbi Yose’s explanation','open_right')]:
 add(key,'structure',rr[0],dict(title=title,primary=True,boundary=bound,legacy_ids=[]));p['records'][-1]['evidence']=[ev(r) for r in rr]
p['open_tails']=[prefix+'s4']
roles=['Sabbatical year source question and year/year analogy','Nisan alternative rejected by months-context distinction','Jubilee Tishrei versus Yom Kippur objection','Named tannaitic attribution and sanctification-from-start derivation','Interim slave status then shofar, slave release and fields return','Sages alternative use: sanctify years, not months','Second baraita rejects holiness extending to year51','Sages year-count reading opposes Rabbi Yehudah double counting','Source question for adding ordinary to sacred time','Rabbi Aqiva agriculture interpretation with two boundary cases','Rabbi Yishmael optional-harvest analogy and omer exception','Rabbi Yishmael source; ninth/evening alternatives resolved','Extension at ending derived','Shabbat and festivals derived separately; general rule','Rabbi Aqiva alternative use; Hiyya bar Rav of Difti teaching begins','Cross-folio completion of eating/drinking credit','Rabbi Yehudah Jubilee requirements','Rabbi Yose alternative Jubilee requirements','Rabbi Yose explains feasible absence of slaves versus shofar','Second reason distinguishes court responsibility']
voices=['anonymous Gemara']*20
for i,v in {3:'anonymous Gemara citing Rabbi Yishmael son of Rabbi Yohanan ben Beroka',4:'Rabbi Yishmael son of Rabbi Yohanan ben Beroka',5:'sages as explained',6:'second anonymous baraita',7:'sages as explained; Rabbi Yehudah quoted',9:'Rabbi Aqiva in baraita',10:'Rabbi Yishmael in baraita (surface name only)',11:'anonymous Gemara explaining Rabbi Yishmael through baraita',12:'cited baraita continuation',13:'cited baraita continuation',14:'anonymous Gemara explaining Rabbi Aqiva; Hiyya bar Rav of Difti quoted',15:'Hiyya bar Rav of Difti teaching continued',16:'Rabbi Yehudah in baraita',17:'Rabbi Yose in baraita',18:'Rabbi Yose explanation continued',19:'Rabbi Yose alternative reason continued'}.items():voices[i]=v
for r,v,role in zip(refs,voices,roles):add('u.'+r,'utterances',r,dict(textual_voice=v,discourse_role=role,composition='composite'))
question('q1','8b:6','What establishes the Tishrei boundary for sabbatical years?','ולשמיטין: מנלן')
claim('shemitah','8b:6','The sabbatical year is linked by שנה שנה to the Tishrei-year verse.','וגמר שנה שנה מתשרי דכתיב (דברים יא, יב) מראשית השנה')
edge('e1','8b:6',C['shemitah'],Q['q1'],'answer')
question('q2','8b:7','Why not derive שנה שנה from the Nisan verse mentioning months?','ולגמור שנה שנה מניסן דכתיב (שמות יב, ב) ראשון הוא לכם לחדשי השנה')
claim('without_months','8b:7','A year not accompanied by months is compared to a year not accompanied by months.','דנין שנה שאין עמה חדשים משנה שאין עמה חדשים')
claim('not_with_months','8b:7','A year without months is not derived from a year accompanied by months.','ואין דנין שנה שאין עמה חדשים משנה שיש עמה חדשים:')
edge('e2','8b:7',C['without_months'],Q['q2'],'answer');edge('e3','8b:7',C['not_with_months'],C['shemitah'],'support')
question('q3','8b:8','How can Jubilee begin at Tishrei1 when its shofar is on Yom Kippur, Tishrei10?')
claim('yom_kippur_shofar','8b:8','The Jubilee shofar verse specifies Yom Kippur.','דכתיב (ויקרא כה, ט) ביום הכפורים תעבירו שופר',holder='Leviticus as quoted')
claim('identified','8b:9','The Mishnah is assigned to Rabbi Yishmael son of Rabbi Yohanan ben Beroka.','הא מני רבי ישמעאל בנו של רבי יוחנן בן ברוקא היא')
claim('only_yk_hyp','8b:9','One might think Jubilee sanctity begins only from Yom Kippur.','יכול לא תהא מתקדשת אלא מיוה"כ ואילך',holder='baraita hypothetical',mode='rejected',status='Rejected by whole-year sanctification reading')
claim('from_start','8b:9','Sanctify the fiftieth year teaches that Jubilee is sanctified from its beginning.','ת"ל וקדשתם את שנת החמשים מלמד שמתקדשת והולכת מתחילתה',holder='Rabbi Yishmael son of Rabbi Yohanan ben Beroka as cited')
attribution('a1','8b:9','רבי ישמעאל בנו של רבי יוחנן בן ברוקא','quoted_authority','Start-of-year Jubilee sanctification and ensuing baraita','רבי ישמעאל בנו של רבי יוחנן בן ברוקא')
edge('e4','8b:9',C['identified'],Q['q3'],'answer');edge('e5','8b:9',C['from_start'],C['only_yk_hyp'],'correction');edge('e6','8b:9',C['from_start'],Q['q3'],'answer')
claim('no_home_yet','8b:10','From New Year until Yom Kippur slaves did not yet depart to their homes.','מר"ה עד יוה"כ לא היו עבדים נפטרין לבתיהן',holder='Rabbi Yishmael son of Rabbi Yohanan ben Beroka',cond=['New Year through pre-Yom-Kippur Jubilee interval'])
claim('no_service','8b:10','During that interval slaves did not serve their masters.','ולא משתעבדין לאדוניהם',holder='Rabbi Yishmael son of Rabbi Yohanan ben Beroka',cond=['Same New Year–Yom Kippur interval'])
claim('festive_interval','8b:10','During the interval they ate, drank and rejoiced with crowns on their heads.','אלא אוכלין ושותין ושמחין ועטרותיהן בראשיהן',holder='Rabbi Yishmael son of Rabbi Yohanan ben Beroka',cond=['Same interval'],status='Composite description of interim conduct, not independently verified historical reconstruction')
claim('court_blast','8b:10','When Yom Kippur arrived the court sounded the shofar.','כיון שהגיע יוה"כ תקעו ב"ד בשופר',holder='Rabbi Yishmael son of Rabbi Yohanan ben Beroka',cond=['Jubilee Yom Kippur'])
claim('slaves_home','8b:10','Following that shofar event the slaves departed home.','נפטרו עבדים לבתיהן',holder='Rabbi Yishmael son of Rabbi Yohanan ben Beroka',cond=['Yom Kippur court shofar stage'])
claim('fields_return','8b:10','The fields returned to their owners.','ושדות חוזרות לבעליהן',holder='Rabbi Yishmael son of Rabbi Yohanan ben Beroka',cond=['Jubilee Yom Kippur stage'])
attribution('a2','8b:10','רבי ישמעאל בנו של רבי יוחנן בן ברוקא','position_holder','Interim slave state and release sequence','ר\' ישמעאל בנו של ר\' יוחנן בן ברוקא')
edge('e7','8b:10',C['no_service'],C['from_start'],'support');edge('e8','8b:10',C['slaves_home'],C['no_home_yet'],'distinction')
claim('sanctify_years','8b:11','The sages read the verse as sanctifying years.','ורבנן שנים אתה מקדש',holder='sages as explained')
claim('not_months','8b:11','In this derivation one does not sanctify months.','ואי אתה מקדש חדשים',holder='sages as explained',status='Local verse interpretation; no external calendar-law synthesis')
attribution('a3','8b:11','רבנן','collective','Alternative use of sanctification verse','ורבנן')
question('q4','8b:12','What does יובל היא teach?','יובל היא מה תלמוד לומר')
claim('extend_end_hyp','8b:12','One might extend Jubilee holiness at its end just as it is sanctified from its beginning.','יכול כשם שמתקדשת והולכת מתחילתה כך מתקדשת והולכת בסופה',holder='second baraita hypothetical',mode='rejected',status='Rejected extension beyond fiftieth year')
claim('addition_premise','8b:12','The possibility invokes the practice of adding ordinary time to sacred time.','ואל תתמה שהרי מוסיפין מחול על קדש',holder='second baraita')
claim('fifty_only','8b:12','The fiftieth year is sanctified.','שנת החמשים אתה מקדש',holder='second anonymous baraita')
claim('not_fiftyone','8b:12','The fifty-first year is not sanctified as an extension of this Jubilee.','ואי אתה מקדש שנת החמשים ואחת',holder='second anonymous baraita')
edge('e9','8b:12',C['addition_premise'],C['extend_end_hyp'],'support');edge('e10','8b:12',C['not_fiftyone'],C['extend_end_hyp'],'correction');edge('e11','8b:12',C['not_fiftyone'],Q['q4'],'answer')
claim('rabbis_count','9a:1','The sages use the fiftieth-year wording for counting fifty and not fifty-one.','ורבנן שנת חמשים אתה מונה ואי אתה מונה שנת חמשים ואחת',holder='sages as explained',status='Counting formula interpreted by the following explicit contrast; not extra sanctification claim')
claim('yehuda_overlap','9a:1','Rabbi Yehudah says the fiftieth year counts toward both cycles.','דר\' יהודה דאמר שנת חמשים עולה לכאן ולכאן',holder='Rabbi Yehudah as quoted')
claim('no_overlap','9a:1','The sages reject the fiftieth year counting toward both cycles.','לאפוקי מדר\' יהודה דאמר שנת חמשים עולה לכאן ולכאן קא משמע לן דלא',holder='sages as explained')
attribution('a4','9a:1','רבנן','collective','Year-count interpretation','ורבנן');attribution('a5','9a:1','רבי יהודה','quoted_authority','Fiftieth year counts both ways',"דר' יהודה דאמר")
edge('e12','9a:1',C['no_overlap'],C['yehuda_overlap'],'distinction');edge('e13','9a:1',C['rabbis_count'],C['no_overlap'],'support')
question('q5','9a:2','What is the source for adding ordinary time to sacred time?')
claim('aqiva_not_redundant','9a:3','Rabbi Aqiva says the plowing/harvesting verse is not needed for seventh-year agricultural work already prohibited by another verse.','ר"ע אומר אינו צריך לומר חריש וקציר של שביעית שהרי כבר נאמר (ויקרא כה, ד) שדך לא תזרע וגו\'',holder='Rabbi Aqiva')
claim('pre_plowing','9a:3','He applies it to plowing before the seventh year which enters the seventh year.','אלא חריש של ערב שביעית הנכנס לשביעית',holder='Rabbi Aqiva',cond=['Pre-seventh-year plowing entering seventh-year scope'])
claim('post_harvest','9a:3','He applies it to seventh-year harvesting extending into the time after the seventh year.','וקציר של שביעית היוצא למוצאי שביעית',holder='Rabbi Aqiva',cond=['Seventh-year harvest extending after that year'])
attribution('a6','9a:3','רבי עקיבא','position_holder','Plowing/harvesting interpretation','ר"ע אומר')
edge('e14','9a:3',C['pre_plowing'],Q['q5'],'answer');edge('e15','9a:3',C['post_harvest'],Q['q5'],'answer')
claim('optional_harvest','9a:4','Rabbi Yishmael compares optional plowing with optional harvesting.','מה חריש רשות אף קציר רשות',holder='רבי ישמעאל (surface name without patronymic)',unc=['Do not equate this surface automatically with the earlier full patronymic.'])
claim('omer_exception','9a:4','The obligatory omer harvest is excluded from this optional-harvest restriction.','יצא קציר העומר שהוא מצוה',holder='רבי ישמעאל (surface name without patronymic)',cond=['Omer harvesting is a mitzvah'])
attribution('a7','9a:4','רבי ישמעאל','position_holder','Optional-harvest analogy; no forced identity merger with8b9 patronymic',"ר' ישמעאל אומר")
edge('e16','9a:4',C['optional_harvest'],C['omer_exception'],'support')
question('q6','9a:5','From where does Rabbi Yishmael derive added sacred time?','ורבי ישמעאל מוסיפין מחול על קדש מנ"ל')
claim('ninth_day_hyp','9a:5','One might understand the affliction command to mean the ninth day itself.','יכול בתשעה',holder='cited baraita hypothetical',mode='rejected',status='בערב corrects this interpretation')
claim('night_only_hyp','9a:5','One might then begin only once it is dark.','אי בערב יכול משתחשך',holder='cited baraita hypothetical',mode='rejected',status='בתשעה excludes waiting until darkness')
claim('daylight_fast','9a:5','The two expressions are reconciled by beginning the fast while it is still day.','הא כיצד מתחיל ומתענה מבעוד יום',holder='baraita cited for Rabbi Yishmael')
claim('add_entry','9a:5','This teaches adding ordinary time to sacred time at entry.','מלמד שמוסיפין מחול על קדש',holder='baraita cited for Rabbi Yishmael')
edge('e17','9a:5',C['daylight_fast'],C['ninth_day_hyp'],'correction');edge('e18','9a:5',C['daylight_fast'],C['night_only_hyp'],'correction');edge('e19','9a:5',C['add_entry'],Q['q6'],'answer');edge('e20','9a:5',C['daylight_fast'],C['add_entry'],'support')
question('q7','9a:6','What establishes adding time at departure as well as entry?','אין לי אלא בכניסתו ביציאתו מנין')
claim('add_departure','9a:6','מערב עד ערב supplies addition at departure.','ת"ל (ויקרא כג, לב) מערב עד ערב',holder='cited baraita')
edge('e21','9a:6',C['add_departure'],Q['q7'],'answer')
question('q8','9a:7','How is this extended from Yom Kippur to Shabbat?','אין לי אלא יוה"כ שבתות מנין')
claim('shabbat','9a:7','תשבתו extends added sacred time to Shabbat.','ת"ל תשבתו',holder='cited baraita')
question('q9','9a:7','How are festivals included?','ימים טובים מנין')
claim('festivals','9a:7','שבתכם extends it to festivals.','ת"ל שבתכם',holder='cited baraita')
claim('all_rest','9a:7','Wherever there is cessation, ordinary time is added to sacred time.','הא כיצד כל מקום שיש בו שבות מוסיפין מחול על קדש',holder='cited baraita',cond=['A place/time with source-described שבות'])
edge('e22','9a:7',C['shabbat'],Q['q8'],'answer');edge('e23','9a:7',C['festivals'],Q['q9'],'answer')
question('q10','9a:8','How does Rabbi Aqiva use the ninth-day affliction wording?','ור"ע האי ועניתם את נפשותיכם בתשעה מאי עביד ליה')
claim('aqiva_hiyya','9a:8','Rabbi Aqiva uses it for the teaching transmitted by Hiyya bar Rav of Difti.','מיבעי ליה לכדתני חייא בר רב מדפתי',holder='anonymous explanation of Rabbi Aqiva')
question('q11','9a:8','Do people fast on the ninth when the fast is on the tenth?','וכי בתשעה מתענין והלא בעשירי מתענין')
claim('ninth_credit','9a:8','Scripture credits one who eats and drinks on the ninth as though he fasted on both ninth and tenth.','אלא לומר לך כל האוכל ושותה בתשיעי מעלה עליו הכתוב',holder='Hiyya bar Rav of Difti as cited',cond=['Eating and drinking on ninth'],status='Textual religious credit, not a claim of actual two-day fasting')
for r in p['records'][-2:]:r['evidence'].append(ev('9b:1'))
attribution('a8','9a:8','חייא בר רב מדפתי','quoted_authority','Ninth-day eating/drinking teaching; father component is not an asserted Rav transmission chain','דתני חייא בר רב מדפתי')
edge('e24','9a:8',C['aqiva_hiyya'],Q['q10'],'answer');edge('e25','9b:1',C['ninth_credit'],Q['q11'],'answer');edge('e26','9b:1',C['ninth_credit'],C['aqiva_hiyya'],'support')
for key,ref,holder,quote,prop,cond in [
 ('yehuda_land','9b:2','Rabbi Yehudah','אע"פ שלא שמטו','Jubilee applies even if they did not perform שמטו (land release).',['Failure of land release does not itself invalidate Jubilee']),
 ('yehuda_blast','9b:2','Rabbi Yehudah','אע"פ שלא תקעו','Jubilee applies even without the shofar blast.',['Failure to sound shofar does not itself invalidate Jubilee']),
 ('yehuda_slaves','9b:2','Rabbi Yehudah','יכול אע"פ שלא שלחו ת"ל היא','Sending the slaves free is indispensable for Jubilee.',['Slaves must be sent free']),
 ('yose_land','9b:3','Rabbi Yose','אע"פ שלא שמטו','Jubilee applies even if they did not perform שמטו (land release).',['Failure of land release does not itself invalidate Jubilee']),
 ('yose_slaves','9b:3','Rabbi Yose','אע"פ שלא שלחו','Jubilee applies even without sending slaves free.',['Failure to send slaves free does not itself invalidate Jubilee']),
 ('yose_blast','9b:3','Rabbi Yose','יכול אע"פ שלא תקעו ת"ל היא','Sounding the shofar is indispensable for Jubilee.',['Shofar must be sounded'])]:claim(key,ref,prop,quote,holder=holder,cond=cond)
attribution('a9','9b:2','רבי יהודה','position_holder','Jubilee invalidated by absence of slave release, not the other two acts','דברי רבי יהודה')
attribution('a10','9b:3','רבי יוסי','position_holder','Shofar indispensable, unlike land/slave release','רבי יוסי אומר')
question('q12','9b:4','Given inclusion and exclusion, why treat slave release as dispensable and shofar as indispensable?','וכי מאחר שמקרא אחד מרבה ומקרא אחד ממעיט מפני מה אני אומר יובל היא אע"פ שלא שלחו ואין יובל אא"כ תקעו')
claim('no_slaves_possible','9b:4','A world without slave release is possible.','לפי שאפשר לעולם בלא שילוח עבדים',holder='Rabbi Yose explanation',status='First rationale; potential challenge to its premise addressed in9b6')
claim('no_blast_not_possible','9b:4','The account contrasts this with a world without the shofar blast being impossible.','ואי אפשר לעולם בלא תקיעת שופר',holder='Rabbi Yose explanation',status='Argument about practicable Jubilee requirement, not independent empirical assertion')
edge('e27','9b:4',C['no_slaves_possible'],Q['q12'],'answer');edge('e28','9b:4',C['no_blast_not_possible'],C['yose_blast'],'support')
claim('court_responsibility','9b:5','The second rationale assigns the shofar act to the court.','זו מסורה לב"ד',holder='Rabbi Yose alternative rationale',unc=['זו resolved by preceding shofar/slave contrast and9b6 repetition.'])
claim('not_court_responsibility','9b:5','Slave release is not entrusted to the court in the same way.','וזו אינה מסורה לבית דין',holder='Rabbi Yose alternative rationale')
edge('e29','9b:5',C['court_responsibility'],Q['q12'],'answer');edge('e30','9b:5',C['not_court_responsibility'],C['yose_slaves'],'support')
# Context is attached only where it qualifies core interpretations; zero added coverage.
question('q13','9b:6','Why is a second reason needed?','מאי דבר אחר')
claim('slave_exists_hyp','9b:6','One might object that somewhere there is inevitably a slave to be sent free.','וכי תימא אי אפשר דליכא חד בסוף העולם דלא משלח',mode='hypothetical',status='Hypothetical challenge motivating the second reason')
edge('e31','9b:6',C['slave_exists_hyp'],C['no_slaves_possible'],'objection');edge('e32','9b:6',C['court_responsibility'],Q['q13'],'answer')
claim('yehuda_derivation','9b:7','Rabbi Yehudah derives his indispensable slave-release condition from וקראתם דרור בארץ.','אמר קרא (ויקרא כה, י) וקראתם דרור בארץ',holder='Rabbi Yehudah as explained')
claim('yehuda_scope','9b:7','His interpretation applies the exclusion to the preceding clause, not the clause before that.','וקסבר מקרא נדרש לפניו ולא לפני פניו',holder='Rabbi Yehudah as explained')
edge('e33','9b:7',C['yehuda_derivation'],C['yehuda_slaves'],'support');edge('e34','9b:7',C['yehuda_scope'],C['yehuda_slaves'],'support')
claim('sages_all_three','9b:9','Rabbi Yohanan, reported by Rabbi Hiyya bar Abba, distinguishes the sages: all three acts are indispensable.',holder='sages reported by Rabbi Yohanan through Rabbi Hiyya bar Abba',cond=['Land release, shofar sounding and sending slaves free all required'],status='Third account, not erasure of Rabbi Yehudah and Rabbi Yose')
attribution('a11','9b:9','רבי חייא בר אבא','transmitter','Reports Rabbi Yohanan distinguishing sages from two named views','אמר ר\' חייא בר אבא א"ר יוחנן',chain=['רבי חייא בר אבא','רבי יוחנן'])
attribution('a12','9b:9','רבי יוחנן','quoted_authority','Report of sages requiring all three acts','א"ר יוחנן',chain=['רבי חייא בר אבא','רבי יוחנן'])
edge('e35','9b:9',C['sages_all_three'],C['yehuda_blast'],'distinction');edge('e36','9b:9',C['sages_all_three'],C['yose_slaves'],'distinction')
claim('sages_scope','9b:9','The sages interpret the verse across preceding, earlier-preceding and following clauses.','קסברי מקרא נדרש לפניו ולפני פניו ולאחריו',holder='sages as explained')
edge('e37','9b:9',C['sages_scope'],C['sages_all_three'],'support')
claim('outside_when_inside','9b:10','Jubilee freedom operates outside the land when it operates in the land.','בזמן שנוהג דרור בארץ נוהג בחוצה לארץ',cond=['Freedom operative in the land'],status='Context interpretation of יובל and בארץ')
claim('outside_not_without','9b:10','When it does not operate in the land, it does not operate outside the land.','בזמן שאינו נוהג בארץ אינו נוהג בחוצה לארץ',cond=['Freedom not operative in the land'])
# Reconcile each core against exact evidence and the full relevant continuation.
rationales={
 '8b:6':'Question, sabbatical verse and year/year derivation recorded; no calendar shift.',
 '8b:7':'Nisan counterproposal and positive/negative matching criterion separated.',
 '8b:8':'First-versus-tenth objection retained; resolved by sanctification/release stages.',
 '8b:9':'Full patronymic, rejected Yom-Kippur-only onset, start-of-year derivation retained.',
 '8b:10':'Separate no-home, no-service, festive conduct, court blast, slave departure and field return stages.',
 '8b:11':'Both years-positive and months-negative readings preserved; no external law harmonization.',
 '8b:12':'Extension hypothesis, addition premise and fifty/not-fifty-one scope preserved.',
 '9a:1':'Sages counting formula and Rabbi Yehudah overlap separately recorded; not holiness claim.',
 '9a:2':'Source question answered by ensuing cited interpretations.',
 '9a:3':'Redundancy premise and two agricultural boundary cases independently represented.',
 '9a:4':'Optional-work analogy and mitzvah omer exclusion; surface Yishmael not merged with patronymic.',
 '9a:5':'Two rejected timing hypotheses, daylight start and addition conclusion preserved.',
 '9a:6':'Departure question and evening-to-evening proof preserved.',
 '9a:7':'Shabbat/festival questions and textual answers separate plus general cessation rule.',
 '9a:8':'Aqiva alternative verse use, Hiyya identity, rhetorical question and credit claim continuing9b1.',
 '9b:1':'Sentence completion attached to both prior claim and position; no duplicate occurrence invented.',
 '9b:2':'Three Rabbi Yehudah action requirements separately extracted; reason9b7 read and attached.',
 '9b:3':'Three Rabbi Yose requirements separately extracted; no silent merger with Yehudah or sages.',
 '9b:4':'Inclusion/exclusion query and two feasibility premises;9b6 challenge preserved.',
 '9b:5':'Court/noncourt responsibilities separated, second reason explained9b6; third sages account9b9 attached.'}
for ref in refs:
 sid=segments[ref]['id']
 for layer in runner.LAYERS:
  ids=[r['id'] for r in p['records'] if r['layer']==layer and any(v['segment_id']==sid for v in r['evidence'])]
  reason=rationales[ref]
  if layer=='reconciliation':reason='Source omission reread: '+reason+' Read continuation through9b10; context-only annotations do not add core coverage.'
  elif not ids:reason+=' No additional '+layer+' record supported here after pass; anonymous/inherited voices and cross-segment answers retained in their own evidence.'
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=reason))
runner.immutable(OUT/'INITIAL_PROPOSAL.json',runner.encoded(p))
runner.immutable(OUT/'SOURCE_RECONCILIATION.json',runner.encoded(dict(base_snapshot=BASE,core_refs=refs,core_indices=[segments[r]['source_index'] for r in refs],context_read=['8b:3–5','9b:6–12'],omission_rationales=rationales,uncertainties=['Unpatronymic רבי ישמעאל not automatically merged with8b9 full name.','Court pronouns interpreted through local contrast; no free-standing identity inference.','Requirement positions are provisional; no demanding task qualification.'],open_tail=prefix+'s4',next_source='Rosh Hashanah 9b:6')))
runner.validate_apply(runner.current(J),p,allsegs,job)
print(json.dumps({'records':len(p['records']),'cores':len(refs),'proposal_sha256':runner.sha(runner.encoded(p))}))
