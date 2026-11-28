import json, hashlib, re, sys
from pathlib import Path
OUT=Path(__file__).parent
JOB=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/jobs/bavli_nedarim_delegated118.json')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8'))
j=read(JOB)
assert sha(JOB)=='8f07dcf5fef312f9054fb9c4937879a1375ce65fb3e7362fb77651a967cd68a1'
for x in [j['source'],j['original_source_schema']]+j['common_documents']: assert sha(x['path'])==x['sha256']
source=read(j['source']['path']); schema=read(j['common_documents'][1]['path'])
def txt(ref):
 m=re.fullmatch(r'Nedarim (\d+)([ab]):(\d+)',ref); d,side,n=m.groups()
 return source['text'][(int(d)-1)*2+(side=='b')][int(n)-1]
def ref(r): return 'Nedarim '+r
context=['20b:14','21a:1','21b:5','21b:6','21b:7','22b:7','22b:11','23a:1','23a:2','23b:4','24b:7','25a:1','25a:2','25a:13','25a:14']
refs=j['core_refs']+[ref(r) for r in context]
records=[]; units={}; labels={}; qs={}
layers=['structure','utterances','claims','attributions','questions','positions','edges']
def ev(r,q=None):
 r=ref(r) if not r.startswith('Nedarim ') else r; t=txt(r); q=t if q is None else q
 assert q and q in t,(r,q)
 a=t.index(q); return {'segment_id':r,'start_char':a,'end_char':a+len(q),'quote':q}
def add(layer,e,content,origin='source_paraphrase',uncertainty=None,links=None):
 i=f'nd118.{layer}.{sum(x["layer"]==layer for x in records)+1:03d}'
 records.append(dict(id=i,layer=layer,evidence=e,content=content,origin=origin,uncertainty=uncertainty or [],links=links or [])); return i
def C(key,r,q,p,who='',conditions=None,mode='asserted',question=None,status='Text-attested local statement; no inference to later practical halakha.',unc=None,role='assertion',chain=None):
 e=[ev(r,q)]; conditions=conditions or []; holders=[who] if who else []
 u=add('utterances',e,dict(textual_voice=who or 'anonymous',discourse_role=role,composition='atomic'),uncertainty=unc)
 c=add('claims',e,dict(proposition=p,conditions=conditions,scope=ref(r),assertion_mode=mode),uncertainty=unc,links=[u]); labels[key]=c
 a=add('attributions',e,dict(surface=who,role='speaker' if who else 'anonymous',candidates=holders,scope=c,transmission_chain=chain or []),uncertainty=unc,links=[u,c])
 if chain:
  add('attributions',e,dict(surface=chain[-1],role='quoted_authority',candidates=[chain[-1]],scope=c,transmission_chain=chain),links=[c])
  for x in chain[:-1]: add('attributions',e,dict(surface=x,role='transmitter',candidates=[x],scope=c,transmission_chain=chain),links=[c])
 if question:
  qi=add('questions',e,dict(formulation=question,question_origin='explicit',conditions=conditions,answer_set_status='partial'),links=[u,c]); qs[key]=qi
 add('positions',e,dict(holder_candidates=([chain[-1]] if chain else holders),claim_id=c,question_id=qs.get(key),conditions=conditions,local_status=status),uncertainty=unc,links=[c]+([qs[key]] if key in qs else []))
 units.setdefault(ref(r),[]).append(key)
 return c
def E(a,b,rel,r,q=None,explicit='source_explicit'):
 aa=labels.get(a,qs.get(a,a)); bb=labels.get(b,qs.get(b,b))
 return add('edges',[ev(r,q)],dict(source_id=aa,target_id=bb,relation=rel,explicitness=explicit),links=[aa,bb])

def build():
 for r in refs:
  boundary='closed'
  if r in ['Nedarim 20b:14','Nedarim 21a:7','Nedarim 22b:11','Nedarim 23a:9','Nedarim 24b:7','Nedarim 25a:2']: boundary='open_right'
  if r in ['Nedarim 21a:1','Nedarim 21b:1','Nedarim 23a:1','Nedarim 23a:2','Nedarim 23a:3','Nedarim 23b:1','Nedarim 25a:1','Nedarim 25a:3']: boundary='open_left'
  labels['S'+r.split(' ')[1]]=add('structure',[ev(r)],dict(title='Source segment '+r,primary=True,boundary=boundary,legacy_ids=[]),'editorial_inference')
 C('four','20b:14',None,'The sages permitted inducement, exaggeration, inadvertent and forced vows.',role='mishna rule')
 C('bargain','20b:14','נדרי זרוזין כיצד היה מוכר חפץ ואמר קונם שאיני פוחת לך מן הסלע והלה אומר קונם שאיני מוסיף לך על השקל','Inducement-vow example: seller vows not below a sela and buyer not above a shekel.',role='mishna case')
 C('three','21a:1',None,'Both intend three dinars.',role='mishna case continuation')
 C('author','21a:2',None,'Rabbi Abba bar Mamal recalls Rabbi Ami reporting Rabbi Yehuda Nesia that the four-vow mishnah is Rabbi Yehuda, who reports Rabbi Tarfon: neither conditional contender is a nazir because nezirut requires explicit determination.','רבי אבא בר ממל',chain=['רבי אבא בר ממל','רבי אמי','רבי יהודה נשיאה'],unc=['Rabbi Yehuda citing Rabbi Tarfon is a nested authority chain, separately recorded.'])
 C('nazir','21a:2','רבי יהודה היא דאמר משום רבי טרפון לעולם אין אחד מהן נזיר לפי שלא ניתנה נזירות אלא להפלאה','Neither is a nazir; nezirut requires explicit determination.','רבי יהודה',chain=['רבי יהודה','רבי טרפון'],conditions=['The conditional contenders referenced by this citation; their underlying case is not supplied in this segment.'])
 C('rava','21a:3',None,'The mishnah can also accord with the Rabbis: it says both presently want, not that both wanted.','רבא',status='Alternative attribution of mishnah; does not assign Rabbis Rabbi Tarfon’s general principle.')
 C('doubt','21a:4',None,'Ravina asks Rav Ashi whether a seller saying more than a sela and a buyer less than a shekel create a vow or inducement.','רבינא',question='Vow or inducement when stated bounds exceed the normal bargaining bounds?',mode='queried')
 C('meal','21a:5',None,'Rav Ashi adduces a teaching: one pressed to dine who prohibits entering the inviter’s house or tasting cold water may do both, since he intended only eating and drinking.','רב אשי',conditions=['Refusal of pressure to eat at the other’s house.'],unc=['Rav Ashi as respondent is inferred from preceding Ravina-to-Rav-Ashi dialogue. Quoted teaching is anonymous.'])
 C('dropq','21a:6','ואמאי והא טיפת צונן קאמר','Why allow cold water when a drop was expressly prohibited?',question='Does saying a drop of cold water exclude the proposed limitation?',mode='queried')
 C('idiom','21a:6','אלא משתעי איניש הכי הכא נמי משתעי איניש הכי','People speak this way; the same idiomatic reading is proposed for the bargaining case.',mode='challenged',status='Proposed analogy distinguished immediately afterward.')
 C('reply','21a:7',None,'The source introduces a reply; its content follows across the page boundary.',role='dialogue framing',unc=['No independent doctrinal assertion here; claimant record preserves the narrative introduction.'])
 C('dist','21b:1',None,'The comparison is rejected: regarding cold water, righteous people promise little and do much.','רבינא',unc=['Responding voice inferred from alternating dialogue, not explicitly renamed.'],question='Are the meal and bargaining cases comparable?',mode='challenged')
 C('loose','21b:2','הכא ספיקא הוא דלמא פחות מסלע ויותר על שקל קאמר וזירוזין הוי','Perhaps he means less than a sela and more than a shekel, making the vow inducement.',mode='hypothetical')
 C('strict','21b:2','או דלמא דווקא קאמר ונידרא הוי תיבעי','Perhaps the bounds are literal and it is a vow; the question remains unresolved.',mode='unresolved',status='Explicit תיבעי: unresolved locally.')
 C('ask','21b:3','אמר רב יהודה אמר רב אסי ארבעה נדרים הללו צריכין שאלה לחכם','The four vows require consultation with a sage.','רב יהודה',chain=['רב יהודה','רב אסי'],status='First report; objected to by Shmuel; alternative version follows.')
 C('shmuel','21b:3','כי אמריתא קמיה דשמואל אמר תנא תני ארבעה נדרים התירו חכמים ואת אמרת צריכין שאלה לחכם','Shmuel objects that the tanna says the sages permitted these four vows, whereas this report requires consultation.','שמואל',mode='challenged',question='How can consultation be required when the tanna says these vows were permitted?',unc=['First-person reporter is Rav Yehuda by narrative continuation. No Rav attribution.'])
 C('alt','21b:4','רב יוסף מתני לה להא שמעתא בהאי לישנא אמר רב יהודה אמר רב אסי אין חכם רשאי להתיר אלא כעין ארבעה נדרים הללו','Rav Yosef recites an alternative version: a sage may annul only vows resembling these four.','רב יוסף',chain=['רב יוסף','רב יהודה','רב אסי'],status='Alternative wording, not a second cumulative rule or a retraction explicitly made by Rav Asi.')
 C('regret','21b:4','קסבר אין פותחין בחרטה','The anonymous explanation attributes rejection of opening with regret to this view.',conditions=['Rav Yosef’s version of Rav Asi’s rule.'])
 C('hunaq','21b:5','אמר ליה ליבך עלך','Rav Huna asks the applicant whether his original heart is still upon him.','רב הונא',question='Do you retain your original resolve?',mode='queried')
 C('hunaa','21b:5','אמר ליה לא ושרייה','Applicant answers no; Rav Huna permits the vow.',role='narrative outcome',conditions=['Negative answer to Rav Huna’s question.'])
 C('rabbaq','21b:6','אמר ליה אילו היו עשרה בני אדם שיפייסוך באותה שעה מי נדרת','Rabba bar Rav Huna asks whether the applicant would have vowed had ten people appeased him then.','רבה בר רב הונא',question='Would you have vowed if ten people had appeased you then?',mode='queried')
 C('rabbaa','21b:6','אמר ליה לא והתירו','The applicant answers no and is released.',conditions=['Negative answer to the appeasement counterfactual.'],role='narrative outcome')
 C('ry','21b:7','תניא רבי יהודה אומר אומרים לו לאדם לב זה עליך אם אמר לאו מתירין אותו','Ask whether this heart is still upon him; if no, release him.','רבי יהודה',conditions=['Applicant answers no.'])
 C('riy','21b:7','רבי ישמעאל ברבי יוסי אומר משום אביו אומרים לו לאדם אילו היו עשרה בני אדם שיפייסוך באותה שעה מי נדרת אם אמר לאו מתירין אותו','Ask whether ten appeasers then would have prevented the vow; if the applicant answers no to whether he would vow, release him.','רבי ישמעאל ברבי יוסי',chain=['רבי ישמעאל ברבי יוסי','רבי יוסי'],conditions=['Counterfactual appeasement at vow time; answer no.'])
 C('later','22b:7',None,'Rava reports Rav Nachman’s halakhic ruling: one opens with regret and attends to an oath by the God of Israel.','רבא',chain=['רבא','רב נחמן'],status='Later original-source local ruling; intervening material not fully inventoried.')
 C('shimon','22b:11',None,'Rabbi Shimon berabbi comes to the sages for release; repeatedly answers yes to whether he vowed with proposed circumstances in mind.',role='narrative')
 C('heat','23a:1',None,'The sages suffer moving from sun to shade and back.',role='narrative continuation')
 C('heatvar','23a:2',None,'An alternative wording repeats the affirmative answers and the sages’ discomfort moving between sun and shade.',role='alternative narrative version')
 C('batq','23a:3','אמר ליה בטנית בריה דאבא שאול בן בטנית מי נדרת אדעתא דמצערי רבנן מטולא לשימשא ומשימשא לטולא','Batnit son of Abba Shaul ben Batnit asks whether he vowed contemplating the sages’ discomfort.','בטנית בריה דאבא שאול בן בטנית',question='Did you vow contemplating the sages’ discomfort?',mode='queried')
 C('bata','23a:3','אמר לא ושריוה','Rabbi Shimon berabbi answers no; they release him.',role='narrative outcome',conditions=['Did not contemplate the sages’ discomfort.'],unc=['Identity recovered from 22b:11, not Rabbi Yishmael in next segment.'])
 C('yishcase','23a:4','רבי ישמעאל בר רבי יוסי הוה ליה נדרא למישרא אתא לקמייהו דרבנן אמרו ליה נדרת אדעתא דהכי אמר להו אין נדרתא אדעתא דהכי אמר להו אין כמה זימנין','Rabbi Yishmael bar Rabbi Yosi seeks release and repeatedly answers yes to suggested circumstances.',role='narrative with repeated question and answer',question='Did you vow with these circumstances in mind?')
 C('laundry','23a:4','כיוון דחזא ההוא קצרא דמצטערי רבנן מחייה באוכלא דקצרי','A launderer, seeing the sages’ discomfort, strikes him with a laundering implement.',role='narrative')
 C('self','23a:4','אמר אדעתא דמחי לי קצרא לא נדרי ושריה לנפשיה','He says he did not vow contemplating a launderer striking him; the text says he released it for himself.','רבי ישמעאל בר רבי יוסי',role='narrative outcome',unc=['Preserve ושריה לנפשיה; do not silently replace with a tribunal act or derive a general self-annulment rule.'])
 C('nolad','23a:5','אמר ליה רב אחא מדיפתי לרבינא האי נולד הוא דלא מסיק אדעתיה דמחי ליה קצרא ותנינא אין פותחין לו בנולד','Rav Acha of Difti objects: an unforeseen launderer’s blow is a newly arising event and the teaching forbids opening with such an event.','רב אחא מדיפתי',mode='challenged',question='Is this not an impermissible opening with a newly arising event?')
 C('common','23a:5','אמר ליה האי לאו נולד הוא דשכיחי אפיקורי דמצערי רבנן','Ravina answers that it is not a newly arising event because insolent people who trouble sages are common.','רבינא',status='Local answer to objection; respondent recovered from dialogue.')
 C('marriage','23a:6','דביתהו דאביי הוה לה ההיא ברתא הוא אמר לקריבאי היא אמרה לקריבה','Abaye and his wife disagree over marrying her daughter to his relative or hers.',role='narrative')
 C('ban','23a:6','אמר לה תיתסרא הנאתי עלך אי עברת אדעתאי ומינסבת לה לקריבך','Abaye prohibits his benefit to his wife if she defies his will and marries the daughter to her relative.','אביי',conditions=['Wife defies his choice and marries the daughter to her relative.'],role='conditional vow',mode='conditional')
 C('defy','23a:6','אזלת ועברת על דעתיה ואינסבא לקריבה','She defies him and marries the daughter to her relative.',role='narrative')
 C('josephq','23a:6','אתא לקמיה דרב יוסף אמר ליה אילו הוה ידעת דעברת על דעתך ומנסבא לה לקריבה מי אדרתה','Rav Yosef asks Abaye whether he would have imposed the vow if he had known she would defy him.','רב יוסף',question='Would you have vowed knowing she would marry the daughter to her relative?',mode='queried')
 C('josepha','23a:6','אמר לא ושרייה רב יוסף','He answers no and Rav Yosef releases him.',conditions=['Negative answer to the defiance counterfactual.'],role='narrative outcome')
 C('permittedq','23a:7','ומי שרי כי האי גוונא','The anonymous discussion asks whether such release is permissible.',mode='queried',question='Is release in such circumstances permitted?')
 C('pilgrim','23a:7','אין והתניא מעשה באדם אחד שהדיר את אשתו מלעלות לרגל ועברה על דעתו ועלתה לרגל','The affirmative answer cites a man who vowed against his wife’s pilgrimage, but she defied him and went.',role='supporting narrative')
 C('yosiq','23a:7','ובא לפני רבי יוסי אמר לו ואילו היית יודע שעוברת על דעתך ועולה לרגל כלום הידרתה','Rabbi Yosi asks whether he would have vowed had he known she would defy him and go.','רבי יוסי',mode='queried',question='Would you have vowed if you had known she would defy you and go on pilgrimage?')
 C('yosia','23a:7','אמר לו לא והתירו רבי יוסי','He answers no and Rabbi Yosi releases him.',conditions=['Negative answer to the defiance counterfactual.'],role='narrative outcome')
 C('mish','23a:8',None,'Rabbi Eliezer ben Yaakov’s transmitted mishnah joins inviting a friend by vow to declaring future vows void, provided he remembers at vow time.','רבי אליעזר בן יעקב',conditions=['Remembrance at vow time in the transmitted wording.'],status='Mishnah surface; subsequently reconstructed, then qualified differently by Abaye and Rava.')
 C('hear','23a:9',None,'If the friend hears that all future vows are void, he will not heed the inviter or accompany him.',question='How does prior cancellation induce the friend to come?',mode='challenged')
 C('induce','23b:1','חסורי מיחסרא והכי קתני הרוצה שיאכל אצלו חבירו ומסרב בו ומדירו נדרי זירוזין הוא','The anonymous reconstruction distinguishes an invitation under pressure with a vow as an inducement vow.',status='Explicit חסורי מיחסרא reconstruction of Rabbi Eliezer ben Yaakov’s mishnah.')
 C('annual','23b:1','והרוצה שלא יתקיימו נדריו כל השנה יעמוד בראש השנה ויאמר כל נדר שאני עתיד לידור יהא בטל ובלבד שיהא זכור בשעת הנדר','One wishing his vows not to stand throughout the year declares at Rosh Hashanah that future vows are void, provided he remembers at vow time.',conditions=['Annual declaration; transmitted remembrance proviso.'],status='Reconstructed mishnah; remembrance proviso challenged and explained in next two segments.')
 C('rememberq','23b:2','אי זכור עקריה לתנאיה וקיים ליה לנדריה','If he remembers, making the vow cancels his stipulation and confirms the vow.',mode='challenged',question='Does remembered stipulation not become canceled by the subsequent vow?')
 C('abaye','23b:2','אמר אביי תני ובלבד שלא יהא זכור בשעת הנדר','Abaye reads: provided he does not remember at vow time.','אביי',conditions=['Does not remember stipulation at vow time.'],status='Abaye’s textual correction; distinct from Rava’s retained wording.')
 C('ravaset','23b:3','רבא אמר לעולם כדאמרינן מעיקרא הכא במאי עסקינן כגון שהתנה בראש השנה ולא ידע במה התנה והשתא קא נדר','Rava retains the original wording for one who stipulated at Rosh Hashanah but does not know what he stipulated and now vows.','רבא',conditions=['Prior Rosh Hashanah stipulation; does not know its content.'])
 C('ravayes','23b:3','אי זכור בשעת הנדר ואמר על דעת הראשונה אני נודר נדריה לית ביה ממשא','If he remembers at vow time and says he vows on the basis of the first intention, the vow has no force.','רבא',conditions=['Prior stipulation with forgotten content.','Remembers at vow time and expressly invokes the first intention.'])
 C('ravano','23b:3','לא אמר על דעת הראשונה אני נודר עקריה לתנאיה וקיים לנדריה','Without declaring the first intention, he cancels the stipulation and confirms his vow.','רבא',conditions=['Rava’s specified case.','Does not say he vows according to the first intention.'])
 C('lecture','23b:4','רב הונא בר חיננא סבר למידרשיה בפירקא','Rav Huna bar Chinena considers publicly teaching this.',role='narrative intention')
 C('conceal','23b:4','אמר ליה רבא תנא קא מסתים לה סתומי כדי שלא ינהגו קלות ראש בנדרים ואת דרשת ליה בפירקא','Rava objects to public exposition: the tanna concealed it to prevent treating vows lightly.','רבא',mode='challenged',question='Should you teach publicly what the tanna concealed to prevent levity about vows?')
 C('ants','24b:7',None,'Ravina asks Rav Ashi whether the man saw an ant nest, privately called its ants those leaving Egypt, and swore truthfully.','רבינא',mode='queried',question='Could a private name make this exaggerated oath true?')
 C('ourmind','25a:1',None,'Rav Ashi answers that the swearer swears according to our understanding and we do not conceive ants.','רב אשי',unc=['Respondent inferred from 24b:7 dialogue.'])
 C('privateq','25a:2','ועל דעתא דנפשיה לא עביד איניש דמשתבע','The anonymous discussion challenges whether someone cannot swear on his own private understanding.',mode='queried',question='Does a person not swear on his own understanding?')
 C('court','25a:2','והתניא כשהן משביעין אותו אומרים לו הוי יודע שלא על תנאי שבלבך אנו משביעין אותך אלא על דעתינו ועל דעת בית דין','A baraita instructs the swearer that the oath is according to those administering it and the court, not his private condition.',role='quoted baraita')
 C('chips','25a:2','לאפוקי מאי לאו לאפוקי דאסיק להו לאיסקונדרי ואסיק להון שמא זוזי','The proposed purpose is excluding a private renaming of wooden pieces as coins.',mode='hypothetical',question='Does the instruction exclude renaming wooden pieces coins?')
 C('infer','25a:3',None,'From the phrase according to our understanding, the objection infers that people do swear on private understanding.',mode='challenged',status='Inference under challenge; next answer offers a different need for the instruction.')
 C('caneex','25a:4','לא לאפוקי מקניא דרבא','The answer says the instruction excludes the cane incident before Rava.',status='Rejects the renaming inference, not the occurrence of literal deceptive delivery.')
 C('debt','25a:4','דההוא גברא דהוה מסיק בחבריה זוזי אתא לקמיה דרבא אמר ליה ללווה זיל פרע לי','A creditor with money owed by another comes before Rava and demands payment.',role='narrative',unc=['The unmarked speaker of the payment demand is not explicitly named; likely creditor from wording לי.'])
 C('paid','25a:4','אמר ליה פרעתיך','The debtor claims he has repaid.',role='reported claim',status='Debtor’s claim in litigation, not narrator certification.')
 C('swear','25a:4','אמר ליה רבא אם כן זיל אישתבע ליה דפרעתיה','Rava instructs the debtor to swear that he has repaid.','רבא',conditions=['Debtor asserts repayment.'],role='judicial instruction')
 C('hide','25a:5','אזל ואייתי קניא ויהיב זוזי בגויה והוה מסתמיך ואזיל ואתי עליה לבי דינא','The debtor puts coins inside a cane and comes to court leaning on it.',role='narrative')
 C('hold','25a:5','אמר ליה למלוה נקוט האי קניא בידך','The debtor asks the creditor to hold the cane.',role='narrative speech')
 C('oath','25a:5','נסב ספר תורה ואישתבע דפרעיה כל מה דהוה ליה בידיה','He takes a Torah scroll and swears he has repaid everything owed.',role='reported oath',conditions=['Creditor holds the cane containing the money.'])
 C('break','25a:6','ההוא מלוה רגז ותברה לההוא קניא ואישתפך הנהו זוזי לארעא','The angry creditor breaks the cane and the money spills out.',role='narrative')
 C('true','25a:6','ואישתכח דקושטא אישתבע','The narrative concludes that his oath proved literally true.',role='narrative evaluation',status='Literal truth of the trick; not moral approval or a general ruling permitting deception.')
 C('mosesq','25a:7','ואכתי לא עביד דמישתבע אדעתא דנפשיה','The discussion renews the objection to denying private-understanding oaths.',question='Still, does no one swear on private understanding?',mode='queried')
 C('moses','25a:7','והתניא וכן מצינו במשה רבינו כשהשביע את ישראל בערבות מואב אמר להם הוו יודעים שלא על דעתכם אני משביע אתכם אלא על דעתי ועל דעת המקום שנאמר ולא אתכם לבדכם וגו\' (דברים כט יג)','A baraita reports Moses telling Israel in Moab that he adjures them according to his and God’s understanding, not theirs, citing ולא אתכם לבדכם.','משה רבינו',role='reported speech in baraita',unc=['Biblical reference retained as supplied by this edition; not independently emended.'])
 C('mosesinf','25a:8','מאי אמר להו משה לישראל לאו הכי קאמר להו דלמא עבידתון מילי ואמריתון על דעתינו משום הכי אמר להו על דעתי','The objection proposes that Moses prevents them from later claiming to act on their own understanding.',mode='hypothetical',question='What did Moses intend to exclude?')
 C('idolrename','25a:8','לאפוקי מאי לאו לאפוקי דאסיקו שמא לעבודת כוכבים אלוה מכלל דעביד איניש דמשתבע אדעתא דנפשיה','It proposes private naming of idolatry as god, inferring that private-understanding oaths occur.',mode='challenged',status='Proposed inference rejected by next answer.')
 C('idolname','25a:9',None,'The answer rejects that inference: idolatry is already called god, as in the gods of Egypt.',status='Ordinary scriptural naming, not a new private designation.')
 C('commandq','25a:10','ולשבע יתהון דמקיימיתון מצוות','Why not adjure them to keep commandments?',question='Why not use commandments as the oath’s object?',mode='queried')
 C('command','25a:10','משמע מצוַת המלך','Commandments can mean the king’s command.',status='Ambiguity defeating proposed wording.')
 C('allq','25a:11','ולשבע יתהון דמקיימיתון כל מצוות','Why not adjure them to keep all commandments?',question='Why not specify all commandments?',mode='queried')
 C('tzitzit','25a:11','משמע מצוַת ציצית','All commandments can mean the commandment of fringes.',status='Ambiguity defeating proposed wording.')
 C('master','25a:11','דאמר מר שקולה מצוַת ציצית כנגד כל מצוות שבתורה','An unnamed authority says fringes are equal in weight to all Torah commandments.',role='quoted authority',unc=['אמר מר does not identify a named scholar.'])
 C('torahq','25a:12','ולשבע יתהון דמקיימיתון תורה','Why not adjure them to keep Torah?',question='Why not use Torah?',mode='queried')
 C('one','25a:12','משמע תורה אחת','Torah can mean one law.',status='Ambiguity defeating proposed wording.')
 C('torotq','25a:12','ולשבע יתהון דמקיימיתון תורות','Why not adjure them to keep torot?',question='Why not use plural torot?',mode='queried')
 C('offerings','25a:12','משמע תורת מנחה תורת חטאת תורת אשם','Torot can mean laws of the meal, sin and guilt offerings.',status='Ambiguity defeating proposed wording.')
 C('bothq','25a:12','ולשבע יתהון דמקיימיתון [תורות] ומצוות','Why not adjure them to keep torot and commandments?',question='Why not combine torot and commandments?',mode='queried',unc=['Bracketed תורות retained exactly; no silent textual repair.'])
 C('both','25a:12','[תורות] משמע תורת המנחה מצוות משמע מצות המלך','Torot can mean the meal-offering law and commandments the king’s command.',status='Ambiguities defeating combined wording.',unc=['Bracketed word retained as source markup.'])
 C('wholeq','25a:13','ולשבע יתהון דמקיימיתון תורה כולה','Why not adjure them to keep the whole Torah?',question='Why not specify the whole Torah?',mode='queried')
 C('whole','25a:13','תורה כולה משמע עבודת כוכבים','The whole Torah can denote the matter of idolatry.',status='Ambiguity of oath wording in the ensuing cited rationale.')
 C('deny','25a:13','דתניא חמורה עבודת כוכבים שכל הכופר בה כאילו מודה בתורה כולה','A baraita teaches the gravity of idolatry: denying it is as acknowledging the whole Torah.',role='quoted baraita')
 C('finalq','25a:14','ולשבע יתהון דמקיימיתון עבודת כוכבים ותורה כולה אי נמי שש מאות ושלוש עשרה מצוות','Why not adjure them about idolatry and the whole Torah, or alternatively 613 commandments?',question='Why not use either unambiguous longer formulation?',mode='queried')
 C('ease','25a:14','אלא משה רבינו מילתא דלא טריחא נקט:','The conclusion is that Moses chose wording that was not burdensome.',status='Explicit local אלא resolution of wording objections; not proof that every proposed longer formula is ambiguous.')

 for a,b,rel,r in [('three','bargain','continuation','21a:1'),('rava','author','objection','21a:3'),('meal','doubt','answer','21a:5'),('idiom','dropq','answer','21a:6'),('dist','idiom','distinction','21b:1'),('strict','doubt','unresolved_outcome','21b:2'),('loose','strict','distinction','21b:2'),('shmuel','ask','objection','21b:3'),('alt','ask','correction','21b:4'),('regret','alt','qualification','21b:4'),('hunaa','hunaq','answer','21b:5'),('rabbaa','rabbaq','answer','21b:6'),('later','regret','objection','22b:7'),('bata','batq','answer','23a:3'),('heatvar','heat','quotation','23a:2'),('nolad','self','objection','23a:5'),('common','nolad','answer','23a:5'),('josepha','josephq','answer','23a:6'),('pilgrim','permittedq','answer','23a:7'),('yosia','yosiq','answer','23a:7'),('yosia','josepha','support','23a:7'),('hear','mish','objection','23a:9'),('induce','hear','answer','23b:1'),('annual','mish','correction','23b:1'),('rememberq','annual','objection','23b:2'),('abaye','annual','correction','23b:2'),('ravaset','rememberq','answer','23b:3'),('ravayes','ravaset','qualification','23b:3'),('ravano','ravaset','qualification','23b:3'),('conceal','lecture','objection','23b:4'),('ourmind','ants','answer','25a:1'),('privateq','ourmind','objection','25a:2'),('court','privateq','support','25a:2'),('infer','ourmind','objection','25a:3'),('caneex','infer','answer','25a:4'),('true','caneex','support','25a:6'),('mosesq','ourmind','objection','25a:7'),('moses','mosesq','support','25a:7'),('idolname','idolrename','answer','25a:9'),('command','commandq','answer','25a:10'),('tzitzit','allq','answer','25a:11'),('master','tzitzit','support','25a:11'),('one','torahq','answer','25a:12'),('offerings','torotq','answer','25a:12'),('both','bothq','answer','25a:12'),('whole','wholeq','answer','25a:13'),('deny','whole','support','25a:13'),('ease','finalq','local_resolution','25a:14')]:
  if rel=='continuation': E('S20b:14','S21a:1',rel,r)
  else: E(a,b,rel,r,explicit='editorial_reconstruction' if a in ['later','heatvar','alt','yosia'] else 'source_explicit')
 for a,b in [('21a:7','21b:1'),('22b:11','23a:1'),('23a:1','23a:3'),('23a:9','23b:1'),('24b:7','25a:1'),('25a:2','25a:3')]: E('S'+a,'S'+b,'continuation',b)
 coverage=[]
 for r in refs:
  for layer in layers+['reconciliation']:
   ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==r for e in x['evidence'])]
   rationale='Read original segment and relevant dialogue continuation; source-based omission pass checked narrative, anonymous reasoning, qualifications and attribution.' if layer=='reconciliation' else ('Source-only pass; records preserve local assertions and uncertainties.' if ids else 'Source-only pass found no independently evidenced '+layer+' record in this segment; surrounding context retained separately.')
   coverage.append(dict(segment_id=r,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
 return dict(schema_version='2.0.0-production',tractate='Nedarim',owner='source_only_nd118',epoch=1,source_sha256=j['source']['sha256'],protocol_sha256=j['common_documents'][0]['sha256'],schema_sha256=j['common_documents'][1]['sha256'],execution=dict(route='interactive_agent',agent_id='/root/nd_source_review118',model_id=None),records=records,coverage=coverage,open_tails=['source-only:Nedarim 21b:7: further regret-opening narratives are outside the fully inventoried scope; the later ruling 22b:7 is separately reviewed, not a claim of intervening coverage.','source-only:Nedarim 23b:4: later inquiry into Rabbi Eliezer ben Yaakov and the Rabbis is outside the reviewed question of annual cancellation.','source-only:Nedarim 24b:7: prior formulation of exaggerated oaths is not fully inventoried here.'])

def write(name,obj):
 p=OUT/name
 assert not p.exists(), 'Frozen artifact already exists: '+str(p)
 p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 return p
def validate(d):
 import jsonschema
 jsonschema.validate(d,schema)
 ids={x['id']:x for x in d['records']}; assert len(ids)==len(d['records'])
 for x in d['records']:
  for e in x['evidence']:
   assert e['segment_id'] in refs
   assert txt(e['segment_id'])[e['start_char']:e['end_char']]==e['quote']
  for l in x['links']: assert l in ids
  c=x['content']
  if x['layer']=='positions':
   assert ids[c['claim_id']]['layer']=='claims'
   if c['question_id']: assert ids[c['question_id']]['layer']=='questions'
  if x['layer']=='attributions': assert ids[c['scope']]['layer']=='claims'
  if x['layer']=='edges':
   assert c['source_id'] in ids and c['target_id'] in ids
   if c['relation']=='continuation': assert all(ids[c[k]]['layer']=='structure' for k in ['source_id','target_id'])
   else: assert all(ids[c[k]]['layer'] in ['claims','questions','positions','utterances'] for k in ['source_id','target_id'])
  identity_fields=['holder_candidates','candidates','transmission_chain']
  for k in identity_fields:
   for identity in c.get(k,[]): assert not any(ch in identity for ch in '[](){};:'),identity
 for r in refs:
  spans=sorted((e['start_char'],e['end_char']) for x in d['records'] if x['layer']=='structure' and x['content']['primary'] for e in x['evidence'] if e['segment_id']==r)
  cur=0
  for a,b in spans: assert a==cur and b>a; cur=b
  assert cur==len(txt(r))
  for layer in layers+['reconciliation']:
   rows=[x for x in d['coverage'] if x['segment_id']==r and x['layer']==layer]; assert len(rows)==1 and rows[0]['extraction_state']=='completed'
   for i in rows[0]['record_ids']: assert ids[i]['layer']==layer and any(e['segment_id']==r for e in ids[i]['evidence'])
 return {l:sum(x['layer']==l for x in d['records']) for l in layers}

if __name__=='__main__':
 if '--verify-only' in sys.argv:
  for p in [OUT/'reading.json',OUT/'exposure.json',Path(__file__),OUT/'validation_receipt.json']:
   assert sha(p)==Path(str(p)+'.sha256').read_text().split()[0],str(p)
  d=read(OUT/'reading.json'); counts=validate(d); exp=read(OUT/'exposure.json')
  assert exp['fully_reviewed_core_refs']==j['core_refs'] and exp['fully_reviewed_context_refs']==[ref(r) for r in context]
  print(json.dumps(dict(status='PASS',counts=counts,core_count=30,context_count=len(context),reading_sha256=sha(OUT/'reading.json')))); sys.exit()
 d=build(); counts=validate(d); write('reading.json',d)
 displayed=[]
 for page in [39,40,41,43,44,45,47,48,49]:
  for n,t in enumerate(source['text'][page]):
   r=f'Nedarim {page//2+1}{"a" if page%2==0 else "b"}:{n+1}'
   if r not in refs: displayed.append(r)
 write('exposure.json',dict(job_id=j['job_id'],job_sha256=sha(JOB),source_binding=j['source'],source_schema_binding=j['original_source_schema'],common_documents=j['common_documents'],fully_reviewed_core_refs=j['core_refs'],fully_reviewed_context_refs=[ref(r) for r in context],incidental_display_only_refs=displayed,blind_per_reviewed_ref={r:True for r in refs},production_exposure=False,prior_reading_exposure=False,comparison_performed=False,production_adapter_compatible=False,segment_id_convention='Human-readable original Sefaria reference used as source-only segment_id; no production ID mapping or adapter compatibility claim.',open_tail_convention='Source-only descriptive strings identifying unreviewed continuation boundaries, not production structure IDs. Primary partitions cover source segments, not inferred complete sugyot. Open boundaries describe cross-segment dialogue, even when both endpoints are reviewed.',restriction='AI provisional source-only reading. Not human certification, production acceptance, ML qualification, or a comparison. Original frozen artifacts must never be edited after comparison.',source_metadata={k:v for k,v in source.items() if k!='text'},reconciliation_notes=['Re-read every core against original text; preserved narrative events and speech instead of only halakhic statements.','Preserved Rav Asi separately from Rav, and Rav Yosef alternative report separately from Shmuel objection.','Abaye correction and Rava conditional retained wording are separate; remembered stipulation alone is insufficient in Rava’s stated case.','25a dialogue continues through 25a:14 local ease-of-wording conclusion; did not stop at 25a:12.','Context 22b:7 records later ruling but does not falsely mark intervening 21b:9–22b:6 fully reviewed.','Structural whole-segment ownership is intentionally coarser than utterance/claim segmentation; no production mapping asserted.']))
 receipt=dict(status='PASS',validation='jsonschema plus exact Python Unicode spans, complete primary partitions, unique IDs, link existence, typed position/attribution/edge FKs, structure-only continuation endpoints, coverage and identity qualifier checks',core_count=30,fully_reviewed_context_count=len(context),incidental_display_only_count=len(displayed),record_counts=counts,files={name:sha(OUT/name) for name in ['reading.json','exposure.json','build_reading.py']},job_sha256=sha(JOB),source_sha256=j['source']['sha256'],semantic_validation_limit='Checks mechanical fidelity only; independent AI source reading is provisional.',production_adapter_compatible=False)
 write('validation_receipt.json',receipt)
 for name in ['reading.json','exposure.json','build_reading.py','validation_receipt.json']:
  p=OUT/name; Path(str(p)+'.sha256').write_text(sha(p)+'  '+name+'\n',encoding='ascii')
 print(json.dumps(receipt))
