"""Manually read festival liability, year calculations, heirs, women and firstborn clocks."""
from pathlib import Path
helper=Path(__file__).with_name('build_batch_005.py').read_text(encoding='utf-8').split("refs=['2b:'")[0]
exec(compile(helper.replace('rh_packet_next.json','rh_packet_009.json').replace('rh.e3.b005.','rh.e3.b009.'),str(__file__),'exec'))
refs=['6a:'+str(i) for i in range(16,20)]+['6b:'+str(i) for i in range(1,19)]+['7a:1','7a:2']
add('s','structure','6a:16',{'title':'Timing and subjects of delay liability, with firstborn year commencement','primary':True,'boundary':'closed','legacy_ids':[]})
p['records'][-1]['evidence']=[ev(r) for r in refs]
voices={
'6a:16':('רבא','Positive-command liability after one festival'),
'6a:17':('anonymous objection citing רבי יהושע and רבי פפייס','Offspring testimony and narrative counterexample'),
'6a:18':('anonymous Gemara','Shavuot delay difficulty'),
'6a:19':('רב זביד reporting רבא','Reply begins, continues across folio'),
'6b:1':('רבא via רב זביד; רב אשי','Illness and alternative festival interpretation'),
'6b:2':('anonymous presentation of opposing reply','Terminological objection to Shavuot reading'),
'6b:3':('רבא; anonymous objector citing baraita','Daily liability and threshold countertext'),
'6b:4':('anonymous question; רב כהנא','Explanation of force of objection'),
'6b:5':('anonymous reply for other side','Baraita’s limited scope'),
'6b:6':('anonymous Gemara','Repeat baraita and annual-threshold case question'),
'6b:7':('anonymous Gemara','Distinguishes ordered/unordered festival theories'),
'6b:8':('anonymous Gemara; רבי quoted','Leap-year solution and solar-year measure'),
'6b:9':('חכמים quoted; anonymous Gemara','Lunar-year measure, Rebbe example, and sages difficulty'),
'6b:10':('רב שמעיה quoted','Variable Shavuot date teaching'),
'6b:11':('anonymous Gemara; אחרים quoted','Contrary fixed weekday-shift view'),
'6b:12':('רבי זירא','Heir question with two textual alternatives'),
'6b:13':('anonymous Gemara citing רבי חייא','Heir exclusion'),
'6b:14':('anonymous Gemara','Competing verse use and dual reading'),
'6b:15':('רבי זירא','Woman’s delay liability question'),
'6b:16':('אביי; anonymous Gemara','Reply on joy, objection from husband’s role, and interlocutor-relative answer'),
'6b:17':('anonymous inquiry; אביי; רב אחא בר יעקב','Firstborn year commencement answers'),
'6b:18':('anonymous Gemara','Explicit reconciliation begins'),
'7a:1':('anonymous Gemara','Blemished case completes reconciliation'),
'7a:2':('anonymous Gemara','Premature animal objection and full-gestation qualification')}
for ref,(voice,role) in voices.items():add('u.'+ref,'utterances',ref,{'textual_voice':voice,'discourse_role':role,'composition':'composite'})
c('c1','6a:16','After one festival passes, one violates the positive command to bring the obligation.',holder='רבא',conditions=['One festival passed'])
a('a1','6a:16','רבא','speaker','One-festival positive command','אמר רבא')
c('c2','6a:17','Rabbi Yehoshua and Rabbi Pappias testified that the offspring of a peace offering is offered as a peace offering.','העיד ר\' יהושע ור\' פפייס על ולד שלמים שיקרב שלמים',holder='רבי יהושע and רבי פפייס')
c('c3','6a:17','Rabbi Pappias testifies that their peace-offering cow was eaten at Passover and its offspring as a peace offering at the festival.','אמר ר\' פפייס אני מעיד שהיתה לנו פרה של זבחי שלמים ואכלנוה בפסח ואכלנו ולדה שלמים בחג',holder='רבי פפייס',status='Festival reference interpreted differently by subsequent replies')
a('a2','6a:17','רבי יהושע ורבי פפייס','collective','Joint testimony about offspring','העיד ר\' יהושע ור\' פפייס')
a('a3','6a:17','רבי פפייס','speaker','Personal testimony narrative','אמר ר\' פפייס')
q('q1','6a:18','Why delay the offspring past Shavuot and violate a positive command?','אלא ולדה בעצרת היכי משהי לה ועברי עליה בעשה')
c('c4','6a:18','Its not being offered at Passover can be explained by its being too young.','בשלמא בפסח לא אקרבוה אימור דמחוסר זמן הוה',mode='hypothetical',status='Possible explanation, not asserted birth chronology')
e('e1','6a:18',questions['q1'],claims['c1'],'objection')
c('c5','6b:1','Rav Zevid reports Rava’s explanation that the offspring was ill at Shavuot.','שהיה חולה בעצרת',holder='רבא',conditions=['Offspring ill at Shavuot'],status='Case explanation allowing festival to denote Sukkot')
p['records'][-2]['evidence'].insert(0,ev('6a:19'));p['records'][-1]['evidence'].insert(0,ev('6a:19'))
a('a4','6a:19','רב זביד','transmitter','Illness reply completed in next segment','אמר רב זביד משמיה דרבא',chain=['רב זביד','רבא'])
a('a5','6a:19','רבא','quoted_authority','Illness reply','משמיה דרבא',chain=['רב זביד','רבא'])
c('c6','6b:1','Rav Ashi interprets the festival in Pappias’s testimony as Shavuot itself.','רב אשי אמר מאי ואכלנו ולדה שלמים בחג דקתני חג השבועות',holder='רב אשי')
a('a6','6b:1','רב אשי','speaker','Shavuot reading','רב אשי אמר')
e('e2','6b:1',claims['c5'],questions['q1'],'answer');e('e3','6b:1',claims['c6'],questions['q1'],'answer')
c('c7','6b:2','The other side objects that when the text names Passover it calls Shavuot Atzeret, rather than simply the festival.',holder='other side of local exchange',status='Terminological defense of illness reply; anonymous narrator supplies argument')
e('e4','6b:2',claims['c7'],claims['c6'],'objection')
c('c8','6b:3','After three festivals, each subsequent day entails a delay violation.','(אמר) רבא כיון שעברו עליו ג\' רגלים בכל יום ויום עובר בבל תאחר',holder='רבא',conditions=['Three festivals passed'])
c('c9','6b:3','The baraita states delay liability for firstborn and all consecrated offerings when a year passes without festivals or festivals pass without a year.','אחד בכור ואחד כל הקדשים כיון שעברו עליהם שנה בלא רגלים רגלים בלא שנה עובר בבל תאחר',holder='anonymous baraita')
a('a7','6b:3','רבא','speaker','Daily delay liability','(אמר) רבא')
e('e5','6b:3',claims['c9'],claims['c8'],'objection')
q('q2','6b:4','How does that baraita constitute an objection?','והאי מאי תיובתיה')
c('c10','6b:4','Rav Kahana says the objection is sound: since the tanna discusses prohibitions it should state the daily violation.','אמר רב כהנא מאן דקא מותיב שפיר קא מותיב מכדי תנא אלאוי קא מהדר ליתני בכל יום ויום עובר בבל תאחר',holder='רב כהנא')
a('a8','6b:4','רב כהנא','speaker','Explains objection from omission','אמר רב כהנא')
e('e6','6b:4',claims['c10'],questions['q2'],'answer')
c('c11','6b:5','The reply limits the baraita to establishing entry into the prohibition, not counting additional violations.',holder='other side of local exchange')
e('e7','6b:5',claims['c11'],claims['c10'],'answer')
c('c12','6b:6','The baraita is repeated: either a year without festivals or festivals without a year produces delay liability.','אחד בכור ואחד כל הקדשים כיון שעברו עליהם שנה בלא רגלים רגלים בלא שנה עובר בבל תאחר',holder='anonymous baraita',status='Separate source occurrence retained')
q('q3','6b:6','How can a year pass without the requisite festivals?','אלא שנה בלא רגלים היכי משכחת לה')
c('c13','6b:7','The year-without-festivals case works for the position requiring an ordered sequence.','הניחא למאן דאית ליה כסדרן משכחת לה',conditions=['Requires ordered festivals'])
q('q4','6b:7','How can it work for the position that does not require festival order?','אלא למאן דלית ליה כסדרן היכי משכחת לה')
c('c14','6b:8','Rebbe defines a full year as 365 days, the solar-year measure.','רבי אומר מונה ג\' מאות וששים וחמשה יום כמנין ימות החמה',holder='רבי',status='Teaching invoked to construct leap-year example')
a('a9','6b:8','רבי','quoted_authority','365-day year definition','רבי אומר')
c('c15','6b:9','The sages count twelve months from day to day, adding the intercalated month when the year is intercalated.','וחכ"א מונה י"ב חדש מיום ליום ואם נתעברה שנה נתעברה לו',holder='חכמים',conditions=['Intercalation extends the year when present'])
c('c16','6b:9','For Rebbe, consecrating after Passover in a leap-year setting yields a full year by the end of the second Adar before the required festivals have passed.','משכחת לה לרבי דאקדשה בתר חג המצות דכי מטא שילהי אדר בתראה שנה מליא רגלים לא מלו',conditions=['Rebbe 365-day measure','Consecrated after Passover','Intercalated year'])
a('a10','6b:9','חכמים','collective','Month-based year definition','וחכ"א')
q('q5','6b:9','How can the case occur under the sages’ month-based year measure?','אלא לרבנן היכי משכחת לה')
e('e8','6b:9',claims['c16'],questions['q4'],'answer')
c('c17','6b:10','Rav Shemaya teaches that Shavuot may be on the fifth, sixth, or seventh: fifth if both preceding months are full, seventh if both deficient, sixth if one of each.',holder='רב שמעיה',status='Used to answer the annual-threshold question; omitted calendrical construction not invented as explicit source')
a('a11','6b:10','רב שמעיה','quoted_authority','Variable Shavuot-date teaching','כדתני רב שמעיה')
e('e9','6b:10',claims['c17'],questions['q5'],'answer')
q('q6','6b:11','Which tanna disagrees with Rav Shemaya?','ומאן תנא דפליג עליה דרב שמעיה')
c('c18','6b:11','Others allow only four weekdays between successive Shavuot dates or successive New Years, and five in a leap year.','אחרים אומרים אין בין עצרת לעצרת אין בין ר"ה לר"ה אלא ד\' ימים בלבד ואם היתה שנה מעוברת חמשה',holder='אחרים',conditions=['Leap year shifts five days; ordinary year four'])
a('a12','6b:11','אחרים','collective','Fixed annual weekday-shift teaching','אחרים אומרים')
e('e10','6b:11',claims['c18'],questions['q6'],'answer')
q('q7','6b:12','Does an heir incur the prohibition against delay?','בעי ר\' זירא יורש מהו בבל תאחר')
c('c19','6b:12','One alternative exempts the heir because “when you vow” refers to a vow he did not make.','כי תדור נדר אמר רחמנא והא לא נדר',mode='hypothetical',holder='רבי זירא’s inquiry',status='Alternative tested by next teaching')
c('c20','6b:12','The other alternative obligates the heir because he must come and bring.','או דלמא (דברים יב, ה) ובאת שמה והבאתם שמה והא מיחייב',mode='hypothetical',holder='רבי זירא’s inquiry',status='Delay inference excluded next; no denial of separate bringing obligation')
a('a13','6b:12','רבי זירא','speaker','Heir inquiry',"בעי ר' זירא")
c('c21','6b:13','Rabbi Hiyya’s teaching excludes the heir through “from you”.',holder='רבי חייא',conditions=['Heir rather than original vower'])
a('a14','6b:13','רבי חייא','quoted_authority','Heir exclusion','דתני רבי חייא')
e('e11','6b:13',claims['c21'],questions['q7'],'answer')
q('q8','6b:14','Is “from you” not needed for gleanings, forgotten sheaves and field corners?','והאי מעמך מיבעי ליה זה לקט שכחה ופאה')
c('c22','6b:14','Reading both עמך and מעמך supports both the agricultural-gift inclusion and heir exclusion.','קרי ביה עמך וקרי ביה מעמך')
e('e12','6b:14',questions['q8'],claims['c21'],'objection');e('e13','6b:14',claims['c22'],questions['q8'],'answer')
q('q9','6b:15','Does a woman incur delay liability, given exemption from appearance but involvement in rejoicing?')
a('a15','6b:15','רבי זירא','speaker','Woman’s liability inquiry',"בעי ר' זירא")
c('c23','6b:15','The exemption possibility rests on her not being obligated in appearance.','מי אמרינן הא לא מיחייבא בראיה',mode='hypothetical',holder='רבי זירא’s inquiry')
c('c24','6b:15','The liability possibility rests on her being included in rejoicing.','או דלמא הא איתה בשמחה',mode='hypothetical',holder='רבי זירא’s inquiry')
c('c25','6b:16','Abaye answers on Rabbi Zeira’s premises that her inclusion in rejoicing suffices.','א"ל אביי ותיפוק ליה דהא איתה בשמחה',holder='אביי',conditions=['On Rabbi Zeira’s rejoicing premise'],status='Interlocutor-relative response, not unqualified statement of Abaye’s own obligation theory')
q('q10','6b:16','Does Abaye himself say this, given his statement that a woman’s husband makes her rejoice?','ומי אמר אביי הכי והאמר אביי אשה בעלה משמחה')
c('c26','6b:16','Abaye’s own quoted statement assigns the act of making a woman rejoice to her husband.','והאמר אביי אשה בעלה משמחה',holder='אביי')
c('c27','6b:16','The narrator resolves the tension by saying Abaye was speaking according to Rabbi Zeira’s view.','לדבריו דר\' זירא קאמר')
a('a16','6b:16','אביי','speaker','Interlocutor-relative reply and separately quoted rejoicing statement','א"ל אביי')
e('e14','6b:16',claims['c25'],questions['q9'],'answer');e('e15','6b:16',claims['c27'],questions['q10'],'answer');e('e16','6b:16',claims['c27'],claims['c25'],'qualification')
q('q11','6b:17','From when is a firstborn’s year counted?','איבעי\' להו בכור מאימתי מונין לו שנה')
c('c28','6b:17','Abaye counts from birth.','אביי אמר משעה שנולד',holder='אביי',conditions=['Blemished firstborn, as continuation reconciles','Known full gestation, per 7a:2'],status='Explicitly reconciled with alternative, not a dispute')
c('c29','6b:17','Rav Aha bar Jacob counts from fitness for sacrificial acceptance.','רב אחא בר יעקב אמר משעה שנראה להרצאה',holder='רב אחא בר יעקב',conditions=['Unblemished firstborn, as continuation reconciles'],status='Explicitly reconciled with Abaye')
a('a17','6b:17','אביי','speaker','Birth answer','אביי אמר');a('a18','6b:17','רב אחא בר יעקב','speaker','Fitness answer','רב אחא בר יעקב אמר')
e('e17','6b:17',claims['c28'],questions['q11'],'answer');e('e18','6b:17',claims['c29'],questions['q11'],'answer')
c('c30','6b:18','The answers do not disagree: the fitness answer concerns an unblemished firstborn, and the birth answer a blemished one.',status='Explicit לא פליגי reconciliation')
p['records'][-2]['evidence'].append(ev('7a:1'));p['records'][-1]['evidence'].append(ev('7a:1'))
e('e19','6b:18',claims['c30'],claims['c29'],'distinction');e('e20','7a:1',claims['c30'],claims['c28'],'distinction')
q('q12','7a:2','Can a blemished firstborn already be eaten at birth?','בעל מום מי מצי אכיל ליה')
c('c31','7a:2','The case is one whose completed gestation is known.','דקים ליה ביה שכלו לו חדשיו',conditions=['Known full gestation'])
e('e21','7a:2',questions['q12'],claims['c28'],'objection');e('e22','7a:2',claims['c31'],questions['q12'],'answer')
for r in p['records']:
 if r['layer']=='claims':r['content']['scope']='Delay thresholds, annual calculation, heir/woman liability and firstborn year commencement in this local discussion'
for ref in refs:
 sid=segments[ref]['id']
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if r['layer']==layer and any(v['segment_id']==sid for v in r['evidence'])]
  rationale='Read through 7b:12; preserved testimonial detail, transmission chains, interlocutor-relative Abaye reply and explicit no-dispute reconciliation.'
  if layer=='reconciliation':rationale='Second source-based omission check covered both festival replies, yearly-calendar alternatives, heir and woman cases, and firstborn conditions. No invented calendrical expansion or dispute. Independent review unfinished.'
  elif not ids:rationale={'attributions':'No new named role in this anonymous continuation; voices retained in utterances.','questions':'No explicit question after source pass.','claims':'Question or transmission connective only; proposition retained across folio in continuation.','positions':'No distinct asserted position in this connective/question segment.','edges':'No separate supported relation beyond following continuation evidence.'}.get(layer,rationale)
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p['open_tails']=[]
out=Path(__file__).with_name('proposal_009.json');out.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'proposal':str(out),'records':len(p['records']),'segments':len(refs)}))
