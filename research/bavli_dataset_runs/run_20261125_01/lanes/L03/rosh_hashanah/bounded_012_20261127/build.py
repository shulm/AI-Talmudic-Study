"""One manually source-read batch, 8a:4–8b:5, with rejected premises preserved."""
from pathlib import Path
helper=Path(__file__).parent.parent.joinpath('build_batch_005.py').read_text(encoding='utf-8').split("refs=['2b:'")[0]
exec(compile(helper.replace('rh_packet_next.json','rh_packet_012.json').replace('rh.e3.b005.','rh.e3.b012.'),str(__file__),'exec'))
refs=['8a:'+str(i) for i in range(4,18)]+['8b:'+str(i) for i in range(1,6)]
for key,rr,title in [('s1',refs[:6],'Animal-tithe boundary: seasonal derivation challenged and replaced'),('s2',refs[6:],'Tishrei years: documents, seasonal cycle, and judgment')]:
 add(key,'structure',rr[0],dict(title=title,primary=True,boundary='closed',legacy_ids=[]));p['records'][-1]['evidence']=[ev(r) for r in rr]
voices=[('8a:4','רבי יוחנן reporting tannaitic readings','Shared Psalm and Rabbi Meir seasonal account'),('8a:5','רבי אלעזר ורבי שמעון as explained in initial account','Alternative seasonal account'),('8a:6','anonymous Gemara','Two verse objections and early/late cases'),('8a:7','anonymous Gemara','Verse-order objection'),('8a:8','רבא','Replacement account with common Adar premise and tithes verse'),('8a:9','רבי מאיר; רבי אלעזר ורבי שמעון as explained','Two different analogical features'),('8a:10','anonymous question; רב פפא; quoted Mishnah','Document application and validity rules'),('8a:11','anonymous objection citing Mishnah and רב חסדא','Nisan document contradiction'),('8a:12','anonymous Gemara','Israelite/foreign kings distinction'),('8a:13','anonymous Gemara quoting רב חסדא','Redundancy challenge'),('8a:14','anonymous Gemara','Scriptural proof contribution'),('8a:15','anonymous alternative; רבי זירא; ר״א','Seasonal-cycle reading'),('8a:16','רב נחמן בר יצחק','Judgment application'),('8a:17','anonymous Gemara','Tishrei identification question; continuation across folio'),('8b:1','anonymous Gemara','Covered moon identifies New Year; judgment verse'),('8b:2','anonymous baraita','Heavenly court awaits earthly sanctification'),('8b:3','second anonymous baraita','Nations included and Israel judged first'),('8b:4','רב חסדא cited','King precedes public in judgment'),('8b:5','anonymous Gemara','Two alternative reasons for king precedence')]
for ref,voice,role in voices:add('u.'+ref,'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
c('c1','8a:4','The quoted Mishnah places the animal-tithe new year at Tishrei 1 for Rabbi Elazar and Rabbi Shimon.','ר\' אלעזר ור"ש אומרים באחד בתשרי',holder='רבי אלעזר ורבי שמעון')
c('c2','8a:4','Rabbi Yohanan says both positions interpret the same Psalm verse.','א"ר יוחנן ושניהם מקרא אחד דרשו',holder='רבי יוחנן',status='Initial account reconsidered by Rava at 8a:8; no personal retraction by Yohanan asserted')
c('c3','8a:4','The initial account relates Rabbi Meir’s mating-season reading to the valleys being covered with grain in Adar.','ר"מ סבר אימתי לבשו כרים הצאן בזמן שעמקים יעטפו בר ואימתי עמקים יעטפו בר באדר',holder='רבי מאיר as explained in initial account',status='Source-reported seasonal interpretation, not independently verified biology')
c('c4','8a:4','In this account conception in Adar and births in Av lead to an Elul tithe boundary.','מתעברות באדר ויולדות באב ר"ה שלהן אלול',holder='רבי מאיר as explained in initial account',status='Initial rationale; conclusion Elul remains in replacement account')
a('a1','8a:4','רבי יוחנן','speaker','Initial same-verse explanation','א"ר יוחנן');a('a2','8a:4','רבי מאיר','position_holder','Initial Adar/Elul interpretation','ר"מ סבר')
c('c5','8a:5','The initial account associates Rabbi Elazar and Rabbi Shimon’s mating-season reading with ears of grain singing in Nisan.','אימתי לבשו כרים הצאן בזמן שיתרועעו אף ישירו אימתי שבלים אומרות שירה בניסן',holder='רבי אלעזר ורבי שמעון as explained initially',mode='challenged',status='Nisan-as-main-season premise displaced by Rava’s common Adar premise')
c('c6','8a:5','In this initial account conception in Nisan and births in Elul lead to Tishrei as the animal-tithe boundary.','מתעברות בניסן ויולדות באלול ר"ה שלהן תשרי',holder='רבי אלעזר ורבי שמעון as explained initially',mode='challenged',status='Rationale displaced, not their Tishrei conclusion')
a('a3','8a:5','רבי אלעזר ורבי שמעון','collective','Initial alternative seasonal account',"ר' אלעזר ור\"ש אומרים")
q('q1','8a:6','For the first side, does the verse not also say they shout and sing?','ואידך נמי הא כתיב יתרועעו אף ישירו')
c('c7','8a:6','The first reply treats the Nisan animals as late breeders.','ההוא באפלתא דהויין בניסן',holder='anonymous explanation of Rabbi Meir’s side',status='Reply within initial seasonal account')
q('q2','8a:6','For the other side, does the verse not also mention valleys covered with grain?','ואידך נמי הכתיב ועמקים יעטפו בר')
c('c8','8a:6','The second reply treats the Adar animals as early breeders.','ההוא בחרפייתא דאתיין מאדר',holder='anonymous explanation of Rabbi Elazar and Rabbi Shimon’s side',status='Reply within initial seasonal account')
e('e1','8a:6',claims['c7'],questions['q1'],'answer');e('e2','8a:6',claims['c8'],questions['q2'],'answer')
c('c9','8a:7','The written order suits Rabbi Meir’s main Adar season followed by an additional Nisan group.','בשלמא לר"מ כדכתיב לבשו כרים הצאן בזמן שעמקים יעטפו בר ואיכא נמי יתרועעו אף ישירו')
c('c10','8a:7','For the initial Rabbi Elazar/Rabbi Shimon account the verse should reverse the order, making the singing season primary and the covered-valleys group secondary.','אלא לרבי אלעזר ור"ש איפכא מיבעי ליה לבשו כרים הצאן בזמן שיתרועעו אף ישירו ואיכא נמי דעמקים יעטפו בר',status='Objection to seasonal explanation, not to Tishrei outcome')
e('e3','8a:7',claims['c10'],claims['c5'],'objection')
c('c11','8a:8','Rava says all agree that the main mating season corresponds to the valleys covered with grain in Adar.','אלא אמר רבא דכ"ע לבשו כרים הצאן בזמן שעמקים יעטפו בר באדר',holder='רבא',status='Replacement common premise')
c('c12','8a:8','Rava relocates the disagreement to עשר תעשר, interpreted as discussing animal tithe and grain tithe.','והכא בהאי קרא קמיפלגי (דברים יד, כב) עשר תעשר בשני מעשרות הכתוב מדבר אחד מעשר בהמה ואחד מעשר דגן',holder='רבא')
a('a4','8a:8','רבא','speaker','Replacement account; not רבה or רב','אלא אמר רבא');e('e4','8a:8',claims['c11'],claims['c5'],'correction');e('e5','8a:8',claims['c12'],claims['c2'],'correction');e('e6','8a:8',claims['c11'],claims['c10'],'answer')
c('c13','8a:9','Rabbi Meir compares animal tithe with grain tithe in having its tithe time adjacent to completion.','ר"מ סבר מקיש מעשר בהמה למעשר דגן מה מעשר דגן סמוך לגמרו עישורו אף מעשר בהמה סמוך לגמרו עישורו',holder='רבי מאיר as explained by Rava')
c('c14','8a:9','Rabbi Elazar and Rabbi Shimon compare the calendar boundary: grain tithe begins in Tishrei, so animal tithe does too.','ורבי אלעזר ור"ש סברי מקיש מעשר בהמה למעשר דגן מה מעשר דגן ר"ה שלו תשרי אף מעשר בהמה ר"ה שלו תשרי:',holder='רבי אלעזר ורבי שמעון as explained by Rava')
a('a5','8a:9','רבי מאיר','position_holder','Completion-proximity analogy','ר"מ סבר');a('a6','8a:9','רבי אלעזר ורבי שמעון','collective','Tishrei-boundary analogy','ורבי אלעזר ור"ש סברי');e('e7','8a:9',claims['c14'],claims['c1'],'support')
q('q3','8a:10','For what law is Tishrei 1 the new year for years?','באחד בתשרי ר"ה לשנים למאי הלכתא')
c('c15','8a:10','Rav Pappa applies the Tishrei-years boundary to documents.','אמר רב פפא לשטרות',holder='רב פפא',status='Qualified to foreign kings by continuation; alternative applications follow')
c('c16','8a:10','Antedated debt documents are invalid.','דתנן שטרי חוב המוקדמין פסולין',holder='quoted Mishnah')
c('c17','8a:10','Postdated debt documents are valid.','והמאוחרין כשירין',holder='quoted Mishnah')
a('a7','8a:10','רב פפא','speaker','Document application','אמר רב פפא');e('e8','8a:10',claims['c15'],questions['q3'],'answer');e('e9','8a:10',claims['c16'],claims['c15'],'support');e('e10','8a:10',claims['c17'],claims['c15'],'support')
c('c18','8a:11','The earlier Mishnah gives Nisan 1 for kings and Rav Hisda likewise explains its application as documents.',holder='anonymous discussion quoting Mishnah and רב חסדא',status='Apparent contradiction answered next')
a('a8','8a:11','רב חסדא','quoted_authority','Earlier Nisan document application','ואמר רב חסדא לשטרות');e('e11','8a:11',claims['c18'],claims['c15'],'objection')
c('c19','8a:12','The two document boundaries concern Israelite kings and foreign kings respectively.',conditions=['Nisan for Israelite kings','Tishrei for kings of other nations'],status='Reconciliation; no blanket contradiction between Rav Pappa and Rav Hisda')
e('e12','8a:12',claims['c19'],claims['c15'],'qualification');e('e13','8a:12',claims['c19'],claims['c18'],'distinction')
c('c20','8a:13','Rav Hisda’s separately quoted statement limits Nisan to Israelite kings and assigns Tishrei to foreign kings.','הא דאמר רב חסדא לא שנו אלא למלכי ישראל אבל למלכי אומות העולם מתשרי מנינן',holder='רב חסדא as quoted')
q('q4','8a:13','Would Rav Hisda merely be teaching what is already in the Mishnah?','רב חסדא מתניתין אתא לאשמועינן')
c('c21','8a:14','The first reply says Rav Hisda supplies the scriptural proofs.')
e('e14','8a:14',claims['c21'],questions['q4'],'answer')
c('c22','8a:15','An alternative reply says Rav Hisda teaches the Mishnah according to Rabbi Zeira’s seasonal-cycle application.','ואיבעית אימא רב חסדא כרבי זירא מתני לה',status='Alternative reply retained alongside scriptural-proof reply')
c('c23','8a:15','Rabbi Zeira applies the years boundary to the seasonal cycle.','דרבי זירא אמר לתקופה',holder='רבי זירא')
c('c24','8a:15','This application follows ר״א, who says the world was created in Tishrei.','ור"א היא דאמר בתשרי נברא העולם',holder='ר״א (unexpanded)',status='Quoted creation chronology as exegetical premise, not independent historical claim',uncertainty=['Source abbreviation retained; no unsupported full-name normalization.'])
a('a9','8a:15','רבי זירא','quoted_authority','Seasonal-cycle application','דרבי זירא אמר');a('a10','8a:15','ר״א','quoted_authority','Tishrei creation premise','ור"א היא',candidates=['ר״א (unexpanded)']);e('e15','8a:15',claims['c22'],questions['q4'],'answer');e('e16','8a:15',claims['c23'],questions['q3'],'answer');e('e17','8a:15',claims['c24'],claims['c23'],'support')
c('c25','8a:16','Rav Nahman bar Yitzhak applies the years boundary to judgment.','רב נחמן בר יצחק אמר לדין',holder='רב נחמן בר יצחק')
c('c26','8a:16','The beginning-to-end-of-year verse is interpreted to mean that the beginning’s judgment determines what will occur at the end.','מראשית השנה נידון מה יהא בסופה',holder='רב נחמן בר יצחק')
a('a11','8a:16','רב נחמן בר יצחק','speaker','Judgment application','רב נחמן בר יצחק אמר');e('e18','8a:16',claims['c25'],questions['q3'],'answer');e('e19','8a:16',claims['c26'],claims['c25'],'support')
q('q5','8a:17','What establishes that this judgment year begins in Tishrei?','ממאי דתשרי הוא')
q('q6','8a:17','Which festival occurs when the moon is covered?','איזהו חג')
p['records'][-1]['evidence'].append(ev('8b:1','שהחדש מתכסה בו'))
c('c27','8b:1','The festival when the moon is covered is New Year.','שהחדש מתכסה בו הוי אומר זה ר"ה')
c('c28','8b:1','The following Psalm verse links the occasion to a statute for Israel and judgment of Jacob’s God.','וכתיב (תהלים פא, ה) כי חק לישראל הוא משפט לאלהי יעקב',holder='Psalm as quoted')
e('e20','8b:1',claims['c27'],questions['q6'],'answer');e('e21','8b:1',claims['c28'],questions['q5'],'answer')
c('c29','8b:2','The baraita teaches that the heavenly court does not enter judgment until the earthly court has sanctified the month.',holder='anonymous baraita',conditions=['Earthly court has sanctified the month'],status='Source-reported theological teaching')
q('q7','8b:3','If the statute mentions Israel, how are other nations included?','אין לי אלא לישראל לאומות העולם מנין')
c('c30','8b:3','The second baraita includes other nations through משפט לאלהי יעקב.','ת"ל משפט לאלהי יעקב',holder='second anonymous baraita')
q('q8','8b:3','What then does the specific mention of Israel teach?','א"כ מה ת"ל כי חק לישראל')
c('c31','8b:3','Israel enters judgment first.','מלמד שישראל נכנסין תחילה לדין',holder='second anonymous baraita')
e('e22','8b:3',claims['c30'],questions['q7'],'answer');e('e23','8b:3',claims['c31'],questions['q8'],'answer')
c('c32','8b:4','Rav Hisda says that when a king and a public face judgment, the king enters first.','מלך וציבור מלך נכנס תחילה לדין',holder='רב חסדא',conditions=['King and public face judgment'])
c('c33','8b:4','The order of the verse, judgment of the servant before judgment of the people, supports king-first precedence.','שנאמר (מלכים א ח, נט) משפט עבדו ומשפט עמו',holder='רב חסדא as quoted')
a('a12','8b:4','רב חסדא','quoted_authority','King-before-public judgment','דאמר רב חסדא');e('e24','8b:4',claims['c32'],claims['c31'],'analogy');e('e25','8b:4',claims['c33'],claims['c32'],'support')
q('q9','8b:5','Why does the king enter judgment first?','מאי טעמא')
c('c34','8b:5','One reason is that it is not proper to leave the king standing outside.','אי בעית אימא לאו אורח ארעא למיקם מלכא אבראי',status='First alternative reason')
c('c35','8b:5','Another reason is to judge the king before anger increases.','ואיבעית אימא מקמי דליפוש חרון אף:',status='Second alternative reason; not combined into a uniquely asserted cause')
e('e26','8b:5',claims['c34'],questions['q9'],'answer');e('e27','8b:5',claims['c35'],questions['q9'],'answer')
for r in p['records']:
 if r['layer']=='claims':r['content']['scope']='Animal-tithe derivations or Tishrei-year applications in this bounded source; exegesis and quoted theological premises are not external factual verification'
for ref in refs:
 sid=segments[ref]['id']
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if r['layer']==layer and any(e['segment_id']==sid for e in r['evidence'])]
  rationale='Complete bounded reading 8a:4–8b:5, with 8b:6–7 boundary context; no new scope outside the declared batch.'
  if layer=='reconciliation':rationale='Source reread checked initial seasonal account versus Rava replacement, retained calendar outcomes, king distinction, alternative applications, cross-folio question, court condition and two reasons. No omitted claim found in this pass; independent review separate.'
  elif not ids:rationale={'questions':'No explicit question in this segment after continuation reading.','attributions':'Anonymous discussion or already introduced baraita; no additional named attribution supported.','claims':'Question or connective segment; asserted answer appears in continuation.','positions':'No asserted position in this question/connective segment.','edges':'No additional supported directed relation originates here.'}.get(layer,rationale)
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p['open_tails']=[]
out=Path(__file__).with_name('proposal.json');out.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(len(p['records']),len(refs))
