"""Manually read festival deadlines, make-up offerings, and Paschal-offering qualification."""
from pathlib import Path
helper=Path(__file__).with_name('build_batch_005.py').read_text(encoding='utf-8').split("refs=['2b:'")[0]
exec(compile(helper.replace('rh_packet_next.json','rh_packet_007.json').replace('rh.e3.b005.','rh.e3.b007.'),str(__file__),'exec'))
refs=['4a:'+str(i) for i in range(12,16)]+['4b:'+str(i) for i in range(1,17)]+['5a:'+str(i) for i in range(1,10)]+['5b:1']
add('s','structure','4a:12',{'title':'Festival order and delay of obligations, with make-up offerings and Paschal qualification','primary':True,'boundary':'closed','legacy_ids':[]})
p['records'][-1]['evidence']=[ev(r) for r in refs]
voices={
'4a:12':('anonymous Gemara; רב חסדא','Calendar objection and interpretive answer'),
'4a:13':('anonymous Gemara; anonymous baraita','Legal consequence and first three-festival rule'),
'4a:14':('רבי שמעון; רבי שמעון בן יוחי','Ordered festivals and three concrete timing cases'),
'4a:15':('anonymous baraita','Obligation list continuing across folio'),
'4b:1':('anonymous baraita; רבי שמעון','List completion, general rule and ordered-festival qualification'),
'4b:2':('רבי מאיר; רבי אליעזר בן יעקב; רבי אלעזר ברבי שמעון','Three distinct deadline positions'),
'4b:3':('anonymous Gemara','First tanna derivation'),
'4b:4':('רבי שמעון','Sukkot as final festival derivation'),
'4b:5':('anonymous Gemara','Rabbi Meir derivation'),
'4b:6':('רבנן as reported anonymously','Alternative positive-command reading'),
'4b:7':('רבי מאיר as explained anonymously','Delay prohibition inferred from failure to bring'),
'4b:8':('anonymous Gemara','Rabbi Eliezer ben Jacob derivation'),
'4b:9':('רבנן; רבי יונה cited','Alternative common atonement interpretation'),
'4b:10':('anonymous Gemara; רבי אלעזר ברבי שמעון quoted','Sukkot as decisive festival derivation'),
'4b:11':('anonymous Gemara; רבי אלעזר reporting רבי אושעיא','Question about alternate verse use and seven-day Shavuot completion teaching'),
'4b:12':('anonymous Gemara','Sukkot analogy objection and initial Shemini reply'),
'4b:13':('anonymous Gemara','Restriction of independent-festival answer'),
'4b:14':('quoted Mishnah','Shemini completion evidence'),
'4b:15':('anonymous Gemara','Smaller inference principle'),
'4b:16':('anonymous Gemara','Question and alternate Sukkot analogy, continuing into 5a'),
'5a:1':('anonymous Gemara','Sukkot overnight-stay inference'),
'5a:2':('anonymous Gemara','Source of Passover overnight-stay requirement'),
'5a:3':('anonymous Gemara','Other tannaim source for Shavuot make-up period'),
'5a:4':('רבה בר שמואל cited','Days/counting analogy'),
'5a:5':('anonymous Gemara; רבא','One-day objection and week-counting reply'),
'5a:6':('anonymous Gemara','Paschal offering deadline objection'),
'5a:7':('רב חסדא','Paschal item dismissed as incidental'),
'5a:8':('רב ששת','Paschal item read as peace offering derived from Passover'),
'5a:9':('anonymous Gemara','Redundancy objection and reason for distinct peace-offering cases'),
'5b:1':('anonymous Gemara','Completion and rejection of Paschal-equivalence hypothesis')}
for ref,(voice,role) in voices.items(): add('u.'+ref,'utterances',ref,{'textual_voice':voice,'discourse_role':role,'composition':'composite'})
q('q1','4a:12','How can the festival new year be Nisan 1 when the festival is Nisan 15?','רגלים באחד בניסן הוא בחמשה עשר בניסן הוא')
c('c1','4a:12','The festival occurring in Nisan is the beginning of the festival sequence.','אמר רב חסדא רגל שבו ראש השנה לרגלים',holder='רב חסדא')
a('a1','4a:12','רב חסדא','speaker','Interpretation of festival new year','אמר רב חסדא')
e('e1','4a:12',claims['c1'],questions['q1'],'answer')
c('c2','4a:13','The practical consequence concerns when a person who made a vow incurs the prohibition against delay; this reading follows Rabbi Shimon.','נפקא מינה לנודר למיקם עליה בבל תאחר ורבי שמעון היא')
c('c3','4a:13','The first baraita imposes delay liability after three festivals on one who vows, consecrates, or undertakes a valuation.','דתניא אחד הנודר ואחד המקדיש ואחד המעריך כיון שעברו עליו ג\' רגלים עובר בבל תאחר',holder='anonymous first tanna',conditions=['Three festivals have passed'])
c('c4','4a:14','Rabbi Shimon requires three festivals in order beginning with Passover.','ר"ש אומר ג\' רגלים כסדרן וחג המצות תחילה',holder='רבי שמעון',conditions=['Three ordered festivals','Passover first'])
c('c5','4a:14','A vow before Passover reaches the deadline after three festivals.','נדר לפני הפסח ג\'',holder='רבי שמעון בן יוחי',conditions=['Vow before Passover'])
c('c6','4a:14','A vow before Shavuot reaches the deadline after five festivals.','לפני עצרת חמשה',holder='רבי שמעון בן יוחי',conditions=['Vow before Shavuot'])
c('c7','4a:14','A vow before Sukkot reaches the deadline after four festivals.','לפני החג ארבעה',holder='רבי שמעון בן יוחי',conditions=['Vow before Sukkot'])
a('a2','4a:14','רבי שמעון','position_holder','Ordered-festival rule','ר"ש אומר')
a('a3','4a:14','רבי שמעון בן יוחי','quoted_authority','Three/four/five timing formulation','וכן היה ר"ש בן יוחי אומר')
e('e2','4a:14',claims['c4'],claims['c2'],'support')
for n in [5,6,7]: e('e.case'+str(n),'4a:14',claims['c'+str(n)],claims['c4'],'qualification')
c('c8','4a:15','The next baraita enumerates monetary and fixed valuations, devoted and consecrated property, sin and guilt offerings, burnt and peace offerings, charity, tithes, firstborn, animal tithe and Passover as obligations under discussion.',holder='anonymous baraita',status='List continues at 4b:1; inclusion of Passover is later disputed')
c('c9','4b:1','The list also includes gleanings, forgotten sheaves and field-corners; the first tanna imposes delay liability after three festivals.','לקט שכחה ופאה כיון שעברו עליהן שלשה רגלים עובר בבל תאחר',holder='anonymous first tanna',conditions=['One of the obligations listed in 4a:15–4b:1','Three festivals passed'])
p['records'][-2]['evidence'].append(ev('4a:15'))
c('c10','4b:1','In this baraita too Rabbi Shimon requires three festivals in order with Passover first.','רבי שמעון אומר שלשה רגלים כסדרן וחג המצות תחלה',holder='רבי שמעון',conditions=['Three ordered festivals','Passover first'])
a('a4','4b:1','רבי שמעון','position_holder','Second occurrence of ordered-festival rule','רבי שמעון אומר')
c('c11','4b:2','Rabbi Meir imposes delay liability after one festival.','ר\' מאיר אומר כיון שעבר עליהן רגל אחד עובר בבל תאחר',holder='רבי מאיר',conditions=['One festival passed'])
c('c12','4b:2','Rabbi Eliezer ben Jacob imposes delay liability after two festivals.','רבי אליעזר בן יעקב אומר כיון שעברו עליהן שני רגלים עובר בבל תאחר',holder='רבי אליעזר בן יעקב',conditions=['Two festivals passed'])
c('c13','4b:2','Rabbi Elazar son of Rabbi Shimon imposes delay liability once Sukkot has passed.','רבי אלעזר ברבי שמעון אומר כיון שעבר עליהן חג הסוכות עובר עליהן בבל תאחר',holder='רבי אלעזר ברבי שמעון',conditions=['Sukkot passed'])
for key,name,quote in [('a5','רבי מאיר',"ר' מאיר אומר"),('a6','רבי אליעזר בן יעקב','רבי אליעזר בן יעקב אומר'),('a7','רבי אלעזר ברבי שמעון','רבי אלעזר ברבי שמעון אומר')]: a(key,'4b:2',name,'position_holder','Festival deadline stated in own clause',quote)
q('q2','4b:3','Why does the first tanna require three festivals?','מאי טעמא דתנא קמא')
q('q3','4b:3','Why repeat all three festival names after the surrounding passage already discussed them?','מכדי מינייהו סליק למה לי למהדר ומיכתב')
c('c14','4b:3','The repetition of Passover, Shavuot and Sukkot is taken as the source for the delay deadline.','בחג המצות ובחג השבועות ובחג הסוכות שמע מינה לבל תאחר',holder='anonymous explanation of first tanna')
e('e3','4b:3',claims['c14'],questions['q2'],'answer');e('e4','4b:3',claims['c14'],questions['q3'],'answer');e('e5','4b:3',claims['c14'],claims['c9'],'support')
q('q4','4b:4','Why mention Sukkot again when the text already concerns it?','למה נאמר')
c('c15','4b:4','For Rabbi Shimon the repeated Sukkot name marks it as the final festival.','לומר שזה אחרון',holder='רבי שמעון')
a('a8','4b:4','רבי שמעון','speaker','Final-festival interpretation','ורבי שמעון אומר')
e('e6','4b:4',claims['c15'],claims['c10'],'support'); e('e7','4b:4',claims['c15'],questions['q4'],'answer')
q('q5','4b:5','What is Rabbi Meir’s source?','ורבי מאיר מ"ט')
c('c16','4b:5','Rabbi Meir derives his deadline from the adjacent commands to come there and bring there.','דכתיב (דברים יב, ה) ובאת שמה והבאתם שמה',holder='anonymous explanation of רבי מאיר')
e('e8','4b:5',claims['c16'],questions['q5'],'answer')
c('c17','4b:6','The other sages use that verse for a positive command, not this negative-prohibition deadline.',holder='רבנן')
a('a9','4b:6','רבנן','collective','Alternative use of coming/bringing verse','ורבנן')
e('e9','4b:6',claims['c17'],claims['c16'],'distinction')
c('c18','4b:7','For Rabbi Meir, failure to bring when commanded itself entails the prohibition against delay.',holder='רבי מאיר as explained anonymously',conditions=['Commanded to bring','Did not bring'])
e('e10','4b:7',claims['c18'],claims['c11'],'support')
q('q6','4b:8','What is Rabbi Eliezer ben Jacob’s source?','ורבי אליעזר בן יעקב מאי טעמא')
c('c19','4b:8','The plural “your festivals” has a minimum of two.','דכתיב (במדבר כט, לט) אלה תעשו לה\' במועדיכם מיעוט מועדים שנים',holder='anonymous explanation of רבי אליעזר בן יעקב')
e('e11','4b:8',claims['c19'],questions['q6'],'answer');e('e12','4b:8',claims['c19'],claims['c12'],'support')
c('c20','4b:9','The other sages use this verse for Rabbi Yonah’s teaching that the festivals are compared because all atone for impurity of the sanctuary and its sacred things.',holder='רבנן citing רבי יונה')
a('a10','4b:9','רבי יונה','quoted_authority','Festival atonement analogy','דאמר רבי יונה')
e('e13','4b:9',claims['c20'],claims['c19'],'distinction')
q('q7','4b:10','What is Rabbi Elazar son of Rabbi Shimon’s source?','ורבי אלעזר ברבי שמעון מאי טעמא')
c('c21','4b:10','He interprets the redundant mention of Sukkot as making Sukkot itself decisive.','למה נאמר לומר שזה גורם',holder='רבי אלעזר ברבי שמעון')
a('a11','4b:10','רבי אלעזר ברבי שמעון','quoted_authority','Sukkot decisive-event derivation',"דתניא רבי אלעזר בר' שמעון אומר")
e('e14','4b:10',claims['c21'],questions['q7'],'answer');e('e15','4b:10',claims['c21'],claims['c13'],'support')
q('q8','4b:11','What do Rabbi Meir and Rabbi Eliezer ben Jacob derive from the three named festivals?','ורבי מאיר ורבי אליעזר בן יעקב האי בחג המצות ובחג השבועות ובחג הסוכות מאי דרשו ביה')
q('q9','4b:11','What establishes a seven-day make-up period for Shavuot?','מניין לעצרת שיש לה תשלומין כל שבעה')
c('c22','4b:11','Rabbi Elazar reports Rabbi Oshaya’s derivation that Shavuot has seven days for make-up offerings by comparison with Passover.','מקיש חג השבועות לחג המצות מה חג המצות יש לו תשלומין כל שבעה אף חג השבועות יש לו תשלומין כל שבעה',holder='רבי אושעיא')
a('a12','4b:11','רבי אלעזר','transmitter','Reports make-up teaching from Rabbi Oshaya',"דאמר ר' אלעזר אמר ר' אושעיא",chain=['רבי אלעזר','רבי אושעיא'])
a('a13','4b:11','רבי אושעיא','quoted_authority','Seven-day make-up teaching',"אמר ר' אושעיא",chain=['רבי אלעזר','רבי אושעיא'])
e('e16','4b:11',claims['c22'],questions['q8'],'answer');e('e17','4b:11',claims['c22'],questions['q9'],'answer')
q('q10','4b:12','Why not compare Shavuot with Sukkot to give eight days?','וליקש לחג הסוכות מה להלן שמונה אף כאן שמונה')
c('c23','4b:12','The initial reply calls the eighth day a separate festival.','שמיני רגל בפני עצמו הוא',mode='challenged',status='Insufficient for make-up offerings, as next objection explains')
e('e18','4b:12',questions['q10'],claims['c22'],'objection');e('e19','4b:12',claims['c23'],questions['q10'],'answer')
c('c24','4b:13','The eighth day is separate for the mnemonic פז״ר קש״ב, but all agree it serves as make-up for the first day’s offering.',status='Restricts prior separate-festival claim; mnemonic preserved without unsupported expansion')
e('e20','4b:13',claims['c24'],claims['c23'],'qualification')
c('c25','4b:14','The Mishnah allows someone who did not bring the festival offering on Sukkot’s first day to bring it throughout the festival and on its last festival day.',holder='quoted anonymous Mishnah',conditions=['Did not bring festival offering on first day'])
e('e21','4b:14',claims['c25'],claims['c24'],'support')
c('c26','4b:15','The smaller inference is secure where the larger one is not; the make-up derivation therefore takes seven rather than eight.',status='Hermeneutic answer, not denial of Shemini’s make-up role')
e('e22','4b:15',claims['c26'],questions['q10'],'answer')
q('q11','4b:16','For what legal consequence is Sukkot included in this verse?','אלא למאי הלכתא כתביה רחמנא לחג הסוכות')
c('c27','5a:1','Sukkot requires an overnight stay by comparison with Passover.')
p['records'][-2]['evidence'].insert(0,ev('4b:16','לאקושיה לחג המצות'))
e('e23','5a:1',claims['c27'],questions['q11'],'answer')
q('q12','5a:2','What establishes the overnight-stay requirement there, at Passover?','והתם מנלן')
c('c28','5a:2','The instruction to turn in the morning and go to one’s tents establishes the overnight stay.','דכתיב (דברים טז, ז) ופנית בבקר והלכת לאהליך')
e('e24','5a:2',claims['c28'],questions['q12'],'answer');e('e25','5a:2',claims['c28'],claims['c27'],'support')
q('q13','5a:3','From where do the first tanna and the named Rabbi Shimon formulation obtain Shavuot make-up days?')
p['records'][-1]['uncertainty']=['Source prints רבי שמעון (בן אלעזר); retain parenthetical wording without silently harmonizing it with preceding named tannaim.']
c('c29','5a:4','Rabbah bar Shmuel teaches an analogy between counting days for a month and counting for Shavuot: the sanctified period follows the counted unit.',holder='רבה בר שמואל',status='Questioned as possibly one day; clarified by Rava')
a('a14','5a:4','רבה בר שמואל','quoted_authority','Counting-unit analogy','דתני רבה בר שמואל')
e('e26','5a:4',claims['c29'],questions['q13'],'answer')
q('q14','5a:5','Could this give Shavuot only one make-up day?','אימא עצרת חד יומא')
q('q15','5a:5','Do we count only days for Shavuot and not also weeks?','אטו עצרת יומי מנינן שבועי לא מנינן')
c('c30','5a:5','Rava responds that counting includes weeks as well as days.','אמר רבא אטו עצרת יומי מנינן שבועי לא מנינן',holder='רבא')
c('c31','5a:5','A cited teaching requires counting both days and weeks.','והאמר מר מצוה למימני יומי ומצוה למימני שבועי',holder='anonymous cited teaching')
c('c32','5a:5','The written name “festival of weeks” provides an additional ground for the weekly unit.','ועוד חג שבועות כתיב',holder='רבא')
a('a15','5a:5','רבא','speaker','Week-counting reply','אמר רבא')
e('e27','5a:5',questions['q14'],claims['c29'],'objection');e('e28','5a:5',claims['c30'],questions['q14'],'answer');e('e29','5a:5',claims['c31'],claims['c30'],'support');e('e30','5a:5',claims['c32'],claims['c30'],'support')
q('q16','5a:6','Can the Paschal offering be offered on later festivals when it has a fixed time?','ופסח בר מיקרב ברגלים הוא')
c('c33','5a:6','The Paschal offering has a fixed time; if not offered then it is deferred rather than retained for the general festival deadline.','פסח זימנא קביעא ליה אי אקרביה אקרביה ואי לא אקרביה אידחי ליה')
e('e31','5a:6',questions['q16'],claims['c8'],'objection')
c('c34','5a:7','Rav Hisda says the Passover item was included incidentally and is not operative here.',holder='רב חסדא',status='Alternative to Rav Sheshet’s interpretation, not a jointly held rule')
a('a16','5a:7','רב חסדא','speaker','Incidental-list-item answer','אמר רב חסדא')
e('e32','5a:7',claims['c34'],questions['q16'],'answer')
c('c35','5a:8','Rav Sheshet interprets Passover here as peace offerings derived from the Paschal offering.',holder='רב ששת')
a('a17','5a:8','רב ששת','speaker','Paschal peace-offering interpretation','רב ששת אמר')
e('e33','5a:8',claims['c35'],questions['q16'],'answer')
q('q17','5a:9','If so, is this not already included under peace offerings?','אי הכי היינו שלמים')
c('c36','5a:9','The list separately teaches peace offerings derived from Passover and peace offerings designated independently.','תנא שלמים הבאין מחמת פסח ותנא שלמים הבאין מחמת עצמן')
c('c37','5a:9','One might have treated offerings derived from Passover as still equivalent to Passover; the separate listing rejects that inference.','סלקא דעתך אמינא הואיל ומחמת פסח קאתו',mode='rejected',status='Explicit hava-amina rejection completed at 5b:1')
p['records'][-2]['evidence'].append(ev('5b:1'))
p['records'][-1]['evidence'].append(ev('5b:1'))
e('e34','5a:9',questions['q17'],claims['c35'],'objection');e('e35','5a:9',claims['c36'],questions['q17'],'answer');e('e36','5b:1',claims['c36'],claims['c37'],'correction')
for r in p['records']:
 if r['layer']=='claims': r['content']['scope']='Festival sequence, delay prohibition, make-up offerings, and Paschal-derived peace offerings in this local discussion'
for ref in refs:
 sid=segments[ref]['id']
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if r['layer']==layer and any(v['segment_id']==sid for v in r['evidence'])]
  rationale='Read through 5b:15 with overlaps; preserved separate festival deadlines, conditions, transmission, cross-folio lists, and rejected make-up inference.'
  if layer=='reconciliation': rationale='Second omission pass checked every clause against source, including three/four/five festival cases, both peace-offering origins, mnemonic limits, and textual parenthesis. Required independent review not yet complete.'
  elif not ids: rationale={'attributions':'No new named speaker or transmission in this anonymous continuation; quoted/anonymous voices retained in utterance.','questions':'No explicit question after reading this segment and continuation.','claims':'Question or connective scope only; substantive proposition carried in linked continuation.','positions':'No distinct asserted holder position in this question/connective segment.','edges':'No additional supported relation originates here; relation evidence is attached to the answer or proof.'}.get(layer,rationale)
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p['open_tails']=[]
out=Path(__file__).with_name('proposal_007.json');out.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'proposal':str(out),'records':len(p['records']),'segments':len(refs)}))
