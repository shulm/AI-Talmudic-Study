"""Serialize manually source-read annotations; no semantic retrieval/classification."""
import json
from pathlib import Path
ROOT=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03')
packet=json.loads((ROOT/'rh_packet_next.json').read_text(encoding='utf-8'))
segments={s['ref'].removeprefix('Rosh Hashanah '):s for s in packet['segments']}
job=packet['job']
p={k:job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']}
p.update(owner='L03/rosh_hashanah',epoch=3,execution={'route':'interactive_agent','agent_id':'/root/rosh_hashanah','model_id':None},records=[],coverage=[],open_tails=[])
def ev(ref,quote=None):
 s=segments[ref]; text=s['text']; quote=text if quote is None else quote; start=text.index(quote)
 return {'segment_id':s['id'],'start_char':start,'end_char':start+len(quote),'quote':quote}
def add(key,layer,ref,content,quote=None,links=(),uncertainty=(),origin='source_paraphrase'):
 rid='rh.e3.b005.'+key
 p['records'].append(dict(id=rid,layer=layer,evidence=[ev(ref,quote)],content=content,origin=origin,uncertainty=list(uncertainty),links=list(links)))
 return rid
claims={}; questions={}
def q(key,ref,text,quote=None):
 questions[key]=add(key,'questions',ref,{'formulation':text,'question_origin':'explicit','conditions':[],'answer_set_status':'partial'},quote)
 return questions[key]
def c(key,ref,text,quote=None,mode='asserted',holder='anonymous Gemara',conditions=(),status='asserted locally',uncertainty=()):
 rid=add(key,'claims',ref,{'proposition':text,'conditions':list(conditions),'scope':'Local derivation of the royal and Exodus year counts; no historical verification beyond this source','assertion_mode':mode},quote,uncertainty=uncertainty)
 claims[key]=rid
 add(key+'.pos','positions',ref,{'holder_candidates':[holder],'claim_id':rid,'question_id':None,'conditions':list(conditions),'local_status':status},quote,links=[rid],uncertainty=uncertainty)
 return rid
def a(key,ref,surface,role,scope,quote=None,chain=(),candidates=None):
 return add(key,'attributions',ref,{'surface':surface,'role':role,'candidates':[surface] if candidates is None else candidates,'scope':scope,'transmission_chain':list(chain)},quote)
def e(key,ref,source,target,relation,quote=None):
 return add(key,'edges',ref,{'source_id':source,'target_id':target,'relation':relation,'explicitness':'source_explicit'},quote,links=[source,target])
refs=['2b:'+str(i) for i in range(7,14)]+['3a:'+str(i) for i in range(1,14)]
structure=add('s','structure','2b:7',{'title':'Deriving Nisan as the royal-year boundary: Exodus chronology, rejected alternatives, and supporting baraita','primary':True,'boundary':'closed','legacy_ids':[]})
p['records'][-1]['evidence']=[ev(r) for r in refs]
voices={
'2b:7':('רבי יוחנן','Question, scriptural citation and analogical derivation'),
'2b:8':('anonymous Gemara','Challenge to premise; alternative Tishrei hypothesis'),
'2b:9':('anonymous Gemara quoting Numbers and Deuteronomy','Rejection of Tishrei by paired chronological evidence'),
'2b:10':('anonymous Gemara','Challenge to the epoch assumed for Deuteronomy'),
'2b:11':('anonymous Gemara invoking רב פפא','Analogical application of a verbal-equivalence method'),
'2b:12':('anonymous Gemara','Challenge to chronological order'),
'2b:13':('anonymous Gemara quoting Deuteronomy','Reply whose proof continues across folio boundary'),
'3a:1':('anonymous Gemara quoting Numbers','Embedded question and narrative exegesis continuing the proof'),
'3a:2':('רבי אבהו; ריש לקיש quoted separately','Alternative reading and supporting lexical teaching'),
'3a:3':('anonymous Gemara; unnamed tanna; alternative anonymous report','Identity objection and two preserved versions of name interpretation'),
'3a:4':('anonymous Gemara','Iyyar alternative'),
'3a:5':('anonymous Gemara quoting Exodus and Numbers','Rejection of Iyyar'),
'3a:6':('anonymous Gemara quoting Exodus','Sivan alternative and rejection'),
'3a:7':('anonymous Gemara','Three remaining alternatives challenge adequacy of derivation'),
'3a:8':('ר״א','Replacement derivation from Chronicles with interpretive question'),
'3a:9':('רבינא then anonymous Gemara','Objection and reply'),
'3a:10':('anonymous Gemara','Weekday alternative and two replies'),
'3a:11':('anonymous Gemara introducing baraita','Baraita supports Rabbi Yohanan; proof citation chain begins'),
'3a:12':('baraita continuation','Chronological scriptural evidence continues'),
'3a:13':('baraita continuation','Final three scriptural references close proof chain')}
for ref,(voice,role) in voices.items():
 add('u.'+ref,'utterances',ref,{'textual_voice':voice,'discourse_role':role,'composition':'composite' if ref not in ['2b:8','2b:10','2b:12','3a:4','3a:7'] else 'atomic'})
q('q1','2b:7','What is the source that royal years are counted only from Nisan?','מנין למלכים שאין מונין להם אלא מניסן')
c('c1','2b:7','Solomon’s regnal count is compared with the Exodus count and therefore begins in Nisan.','מקיש מלכות שלמה ליציאת מצרים מה יציאת מצרים מניסן אף מלכות שלמה מניסן',holder='רבי יוחנן',status='Derivation challenged on its Exodus premise; baraita later supports it')
a('a1','2b:7','רבי יוחנן','speaker','Question and derivation in this segment','א"ר יוחנן')
e('e1','2b:7',claims['c1'],questions['q1'],'answer')
q('q2','2b:8','How is an Exodus epoch beginning in Nisan established rather than Tishrei?')
c('c2','2b:8','The Exodus years might be counted from Tishrei.','דילמא מתשרי מנינן',mode='hypothetical',status='Alternative rejected by subsequent chronological argument')
e('e2','2b:8',questions['q2'],claims['c1'],'objection')
c('c3','2b:9','Aaron’s death in Av is dated to year forty from the Exodus.',"ויעל אהרן הכהן אל הר ההר על פי ה' וימת שם בשנת הארבעים לצאת בני ישראל מארץ מצרים בחדש החמישי באחד לחדש",holder='Numbers 33:38 as quoted')
c('c4','2b:9','Moses’ speech in Shevat is likewise dated to year forty.',"ויהי בארבעים שנה בעשתי עשר חדש באחד לחדש דבר משה וגו'",holder='Deuteronomy 1:3 as quoted')
c('c5','2b:9','Av and the following Shevat within year forty exclude Tishrei as its boundary.','מדקאי באב וקרי לה שנת ארבעים וקאי בשבט וקרי לה שנת ארבעים מכלל דר"ה לאו תשרי הוא',conditions=['Both dates use Exodus years','Av event precedes Shevat event'],status='Premises challenged and defended in following exchange')
e('e3','2b:9',claims['c5'],claims['c2'],'objection')
e('e4','2b:9',claims['c3'],claims['c5'],'support')
e('e5','2b:9',claims['c4'],claims['c5'],'support')
q('q3','2b:10','Why assume Moses’ year forty uses the Exodus epoch rather than erection of the tabernacle?')
c('c6','2b:10','Moses’ year forty could instead be counted from erection of the tabernacle.','דילמא להקמת המשכן',mode='hypothetical',status='Rejected by verbal equivalence reply')
e('e6','2b:10',questions['q3'],claims['c5'],'objection')
c('c7','2b:11','Matching “year forty” expressions establish that both passages use the Exodus epoch.','הכא נמי שנת ארבעים שנת ארבעים לגזרה שוה מה כאן ליציאת מצרים אף כאן ליציאת מצרים')
a('a2','2b:11','רב פפא','quoted_authority','The year-twenty verbal equivalence is invoked as an analogy; this is not direct attribution to him of the year-forty application','כדאמר רב פפא שנת עשרים שנת עשרים לגזרה שוה')
e('e7','2b:11',claims['c7'],questions['q3'],'answer')
q('q4','2b:12','How is it known that the Av event preceded the Shevat event rather than the reverse?')
c('c8','2b:12','The Shevat event might precede the Av event.','דילמא מעשה דשבט קדים',mode='hypothetical',status='Rejected in continuation')
e('e8','2b:12',questions['q4'],claims['c5'],'objection')
c('c9','2b:13','Moses’ speech occurred after Sihon’s defeat; Sihon was still alive when Aaron died.','אחרי הכותו את סיחון וכי נח נפשיה דאהרן אכתי הוה סיחון קיים',status='Chronological reply; identification with Canaan/Arad challenged and defended in 3a:3')
e('e9','2b:13',claims['c9'],questions['q4'],'answer')
q('q5','3a:1','What report did the Canaanite king of Arad hear?','מה שמועה שמע')
c('c10','3a:1','He heard of Aaron’s death and departure of the clouds of glory.','שמע שמת אהרן ונסתלקו ענני כבוד')
c('c11','3a:1','The king supposed that he now had permission to fight Israel.','וכסבור ניתנה רשות להלחם בישראל',holder='Canaanite king of Arad as represented by the exposition',status='Attributed supposition, not endorsement of permission')
e('e10','3a:1',claims['c10'],questions['q5'],'answer')
e('e11','3a:1',claims['c10'],claims['c9'],'support')
c('c12','3a:2','Rabbi Abbahu reads the verse as “they were seen” (וייראו), rather than ויראו.','אל תקרי ויראו אלא וייראו',holder='רבי אבהו',uncertainty=['Vocalization is not encoded in these consonantal evidence strings.'])
c('c13','3a:2','Resh Lakish gives four meanings of כי: if, perhaps, rather, because.','כי משמש בד\' לשונות אי דילמא אלא דהא',holder='ריש לקיש')
a('a3','3a:2','רבי אבהו','speaker','Alternate reading','וא"ר אבהו')
a('a4','3a:2','ריש לקיש','quoted_authority','Four lexical senses of כי only','כדריש לקיש דאמר ר"ל')
e('e12','3a:2',claims['c13'],claims['c12'],'support')
q('q6','3a:3','How can the proof about Canaan establish the chronology of Sihon?','מי דמי התם כנען הכא סיחון')
c('c14','3a:3','An unnamed tannaitic teaching identifies Sihon, Arad and Canaan as the same person.','תנא הוא סיחון הוא ערד הוא כנען',holder='unnamed tanna')
c('c15','3a:3','In the first version, Sihon describes resemblance to a desert foal, Canaan names his kingdom, and his personal name is Arad.','סיחון שדומה לסייח במדבר כנען על שם מלכותו ומה שמו ערד שמו',holder='first anonymous transmitted version',status='Version retained alongside alternative, not resolved')
c('c16','3a:3','In the alternative version, Arad describes resemblance to a desert wild ass, Canaan names his kingdom, and his personal name is Sihon.','איכא דאמרי ערד שדומה לערוד במדבר כנען על שם מלכותו ומה שמו סיחון שמו',holder='alternative anonymous transmitted version',status='Version retained alongside first, not resolved')
a('a5','3a:3','תנא','anonymous','Identity teaching; no named tanna supplied','תנא הוא סיחון הוא ערד הוא כנען',candidates=[])
a('a6','3a:3','איכא דאמרי','anonymous','Alternative etymological report','איכא דאמרי',candidates=[])
e('e13','3a:3',questions['q6'],claims['c9'],'objection')
e('e14','3a:3',claims['c14'],questions['q6'],'answer')
q('q7','3a:4','Could Iyyar be the new year?')
c('c17','3a:5','The tabernacle was erected in Nisan of the second year.','ויהי בחדש הראשון בשנה השנית באחד לחדש הוקם המשכן',holder='Exodus 40:17 as quoted')
c('c18','3a:5','The cloud rose from the tabernacle in Iyyar of the second year.','ויהי בשנה השנית בחדש השני נעלה הענן מעל משכן העדות',holder='Numbers 10:11 as quoted')
c('c19','3a:5','Both Nisan and Iyyar are called the second year, excluding Iyyar as new year.','מדקאי בניסן וקרי לה שנה שנית וקאי באייר וקרי לה שנה שני\' מכלל דר"ה לאו אייר הוא')
e('e15','3a:5',claims['c19'],questions['q7'],'answer')
e('e16','3a:5',claims['c17'],claims['c19'],'support')
e('e17','3a:5',claims['c18'],claims['c19'],'support')
q('q8','3a:6','Could Sivan be the new year?','ואימא ר"ה סיון')
c('c20','3a:6','If Sivan began the year, the verse’s third month after the Exodus should be called the second year; its wording excludes that suggestion.','לא ס"ד דכתיב (שמות יט, א) בחדש השלישי לצאת בני ישראל מארץ מצרים ואם איתא בחדש השלישי בשנה השנית לצאת וגו\' מיבעי ליה')
e('e18','3a:6',claims['c20'],questions['q8'],'answer')
q('q9','3a:7','Could the year instead begin in Tammuz, Av, or Adar?')
c('c21','3a:8','The second “second” in Chronicles denotes the second month relative to the month used to count the king’s reign.','מאי שני לאו שני לירח שמונין בו למלכותו',holder='ר״א (unexpanded)',status='Replacement derivation; challenged then defended',uncertainty=['Source abbreviation ר״א is preserved without choosing a full name.'])
q('q10','3a:8','Does the second “second” mean second to the month from which royal years are counted?','מאי שני לאו שני לירח שמונין בו למלכותו')
a('a7','3a:8','ר״א','speaker','Replacement derivation introduced by אלא אמר ר"א','אלא אמר ר"א',candidates=['ר״א (unexpanded)'])
e('e19','3a:8',claims['c21'],questions['q9'],'answer')
q('q11','3a:9','Could “second” instead mean the second day of the month?','ואימא שני בחדש')
a('a8','3a:9','רבינא','speaker','Day-of-month challenge; following reply is anonymous','מתקיף לה רבינא')
c('c22','3a:9','A day-of-month reading would require the word “month” next to the second occurrence of “second”.','א"כ שני בחדש בהדיה הוה כתיב ביה')
e('e20','3a:9',questions['q11'],claims['c21'],'objection')
e('e21','3a:9',claims['c22'],questions['q11'],'answer')
q('q12','3a:10','Could “second” refer to the second weekday?','ואימא בשני בשבת')
c('c23','3a:10','The first reply is that a scriptural “second weekday” expression is not found.','חדא דלא אשכחן שני בשבת דכתיב')
c('c24','3a:10','The later “second” is compared with the earlier “second”; just as the earlier denotes a month, so does the later.','ועוד מקיש שני בתרא לשני קמא מה שני קמא חדש אף שני בתרא חדש')
e('e22','3a:10',questions['q12'],claims['c21'],'objection')
e('e23','3a:10',claims['c23'],questions['q12'],'answer')
e('e24','3a:10',claims['c24'],questions['q12'],'answer')
c('c25','3a:11','The cited baraita teaches Nisan-based royal years and is introduced as support for Rabbi Yohanan.','תניא כוותיה דר\' יוחנן מניין שאין מונין להם למלכים אלא מניסן',holder='anonymous baraita')
a('a9','3a:11','baraita','anonymous','Tannaitic parallel cited in support of Rabbi Yohanan',"תניא כוותיה דר' יוחנן",candidates=[])
q('q13','3a:11','What is the scriptural source for counting royal years only from Nisan, in the baraita’s formulation?','מניין שאין מונין להם למלכים אלא מניסן')
e('e25','3a:11',claims['c25'],claims['c1'],'support')
c('c26','3a:12','The baraita joins the defeat of Sihon, the Canaanite report, the sight of Aaron’s death, and the Nisan erection of the tabernacle as chronological evidence.',holder='anonymous baraita',status='Cited proof chain; abbreviated verses remain abbreviated')
c('c27','3a:13','The baraita concludes its proof chain with the second-month departure, third-month Exodus passage, and Solomon’s construction passage.',holder='anonymous baraita',status='Cited proof chain; abbreviated verses remain abbreviated')
e('e26','3a:12',claims['c26'],claims['c25'],'support')
e('e27','3a:13',claims['c27'],claims['c25'],'support')
e('e28','3a:13',claims['c27'],questions['q13'],'answer')
for ref in refs:
 sid=segments[ref]['id']
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if r['layer']==layer and any(v['segment_id']==sid for v in r['evidence'])]
  rationale='Source reread with overlapping 2b:1–3b:10 context. Questions, alternatives, repeated proof occurrences, attribution scope, and cross-folio continuation retained.'
  if layer=='reconciliation': rationale='Second source-based omission pass checked this segment against recorded clauses; no additional independent claim omitted. Kept alternative etymologies, rhetorical questions, and abbreviation uncertainty. Review remains independent and unfinished.'
  elif not ids: rationale={'attributions':'No named speaker or transmitter asserted in this segment; anonymous voice retained in utterance and local positions.','questions':'No explicit question in this segment after source pass.','claims':'Question-only segment proposes alternatives without asserting them as conclusions; question records preserve all named alternatives.','positions':'Question-only segment; no asserted holder position to add.','edges':'No independent directed edge originates in this segment; incoming replies remain represented on their own evidence.'}.get(layer,rationale)
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p['open_tails']=[] # This derivation closes at 3a:13; resume notes are not structure IDs.
out=Path(__file__).with_name('proposal_005.json')
out.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'proposal':str(out),'records':len(p['records']),'segments':len(refs)}))
