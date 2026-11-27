import json, hashlib, pathlib, collections
ROOT=pathlib.Path(__file__).parent
JOB=pathlib.Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/jobs/bavli_makkot_delegated020.json')
j=json.loads(JOB.read_text(encoding='utf8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(JOB.read_bytes())=='28dd9bbc133fc362589dc3a4e5959886c99012d83724d25ea8e533b1b7feeded'
bindings=[]
for x in [j['source'],*j['common_documents'],j['frozen_plan'],j['original_source_schema']]:
    actual=sha(pathlib.Path(x['path']).read_bytes());assert actual==x['sha256'];bindings.append(dict(x,actual_sha256=actual,validated=True))
plan=json.loads(pathlib.Path(j['frozen_plan']['path']).read_text(encoding='utf8'))
unhashed={k:v for k,v in plan.items() if k!='plan_sha256'}
assert sha(b'bavli-source-only-review-plan-v1\0'+json.dumps(unhashed,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode())==j['plan_sha256']
source=json.loads(pathlib.Path(j['source']['path']).read_text(encoding='utf8'))
texts={f'Makkot {(i+2)//2}{"a" if i%2==0 else "b"}:{n+1}':t for i,p in enumerate(source['text']) for n,t in enumerate(p)}
cores=j['core_refs']; rec=[]; claims={}; questions={}
def ev(ref,quote=None):
    if not ref.startswith('Makkot '):ref='Makkot '+ref
    t=texts[ref];quote=t if quote is None else quote;start=t.index(quote)
    return dict(segment_id=ref,start_char=start,end_char=start+len(quote),quote=quote)
def add(id,layer,evidence,content,origin='source_paraphrase',uncertainty=None,links=None):
    assert id not in {r['id'] for r in rec}
    rec.append(dict(id=id,layer=layer,evidence=evidence,content=content,origin=origin,uncertainty=uncertainty or [],links=links or []));return id
def c(id,ref,quote,prop,holder='anonymous sugya',mode='asserted',conditions=None,uncertainty=None,chain=None):
    e=[ev(ref,quote)];conditions=conditions or []
    add(id,'claims',e,dict(proposition=prop,conditions=conditions,scope='Local source discussion; no later practical ruling inferred',assertion_mode=mode),uncertainty=uncertainty)
    add(id+'.u','utterances',e,dict(textual_voice=holder,discourse_role=mode,composition='atomic'),uncertainty=uncertainty)
    add(id+'.a','attributions',e,dict(surface=holder,role='anonymous' if holder.startswith('anonymous') else 'position_holder',candidates=[] if holder.startswith('anonymous') else [holder],scope=id,transmission_chain=chain or []),uncertainty=uncertainty)
    add(id+'.p','positions',e,dict(holder_candidates=[] if holder.startswith('anonymous') else [holder],claim_id=id,question_id=None,conditions=conditions,local_status=mode),links=[id],uncertainty=uncertainty)
    claims[id]=ref
def q(id,ref,quote,form,answers=None,conditions=None):
    add(id,'questions',[ev(ref,quote)],dict(formulation=form,question_origin='explicit',conditions=conditions or [],answer_set_status='topic_inventory' if answers else 'none'),links=answers or [])
    add(id+'.u','utterances',[ev(ref,quote)],dict(textual_voice='anonymous sugya',discourse_role='question',composition='atomic'))
    add(id+'.a','attributions',[ev(ref,quote)],dict(surface='anonymous sugya',role='anonymous',candidates=[],scope=id,transmission_chain=[]),links=[id])
    questions[id]=ref
def edge(id,s,t,rel,ref,quote=None,explicit='source_explicit'):
    add(id,'edges',[ev(ref,quote)],dict(source_id=s,target_id=t,relation=rel,explicitness=explicit),links=[s,t])

# Human-readable authored semantic inventory. All Hebrew snippets are matched to pinned original strings.
c('c01','4a:6','לרב פפא מיבעיא ליה','Rav Pappa remains uncertain which wording Rav taught and consequently whose view Rav follows.','רב פפא','unresolved')
c('c02','4a:6','לרבא פשיטא ליה','Rava has a definite interpretation; the contrast does not settle Rav Pappa\'s question for him.','רבא',uncertainty=['Content of Rava\'s certainty is supplied by 3b:17: distinction between R. Yohanan ben Nuri and the rabbis, not automatically the following recollection.'])
c('c03','4a:7','אמר רב יוסף לא שמיעא לי הא שמעתא','Rav Yosef says he has not heard this teaching.','רב יוסף')
c('c04','4a:7','אמר ליה אביי את אמרת לה ניהלן והכי אמרת ניהלן','Abaye reminds Rav Yosef that he himself taught this to them.','אביי')
c('c05','4a:7','דרב לא תני חסר קורטוב ברישא','According to Abaye\'s recollection of Rav Yosef, Rav did not teach less one kortov in the opening case.','רב',chain=['אביי','רב יוסף','רב'])
c('c06','4a:7','ורבי יוחנן אסיפא פליג','In that recalled interpretation R. Yohanan [ben Nuri from context] disputes the latter case.','רבי יוחנן בן נורי',chain=['אביי','רב יוסף'],uncertainty=['Short surface רבי יוחנן resolved from 4a:2–5; not the amora by same name.'])
c('c07','4a:7','ורב דאמר כדברי הכל','In that recalled reading Rav\'s ruling accords with all parties.','anonymous interpretation reported by Abaye',chain=['אביי','רב יוסף'])
c('c08','4a:8','ואמר רב יהודה אמר רב חבית מליאה מים שנפלה לים הגדול הטובל שם לא עלתה לו טבילה','Immersion at the site of a barrel of water that fell into the great sea does not count.','רב',conditions=['Barrel full of water fell into the great sea','Immersion there'],chain=['רב יהודה','רב'])
c('c09','4a:8','חיישינן לשלשה לוגין שלא יהו במקום אחד','Concern is that three log remain together at one location.','רב',conditions=['Same barrel and immersion case'],chain=['רב יהודה','רב'],uncertainty=['Literal שלא יהו preserved; explanatory paraphrase follows concern construction, without emending source.'])
c('c10','4a:8','ודוקא לים הגדול דקאי וקיימא אבל נהרא בעלמא לא','The restriction applies specifically to the stationary great sea, not an ordinary river.','anonymous limiting gloss',conditions=['Stationary sea versus flowing river'],uncertainty=['Limit follows report without a fresh named speaker; not confidently assigned to Rav himself.'])
c('c11','4a:9','תניא נמי הכי חבית מליאה יין שנפלה לים הגדול הטובל שם לא עלתה לו טבילה','A baraita likewise invalidates immersion where a barrel full of wine fell into the great sea.','anonymous baraita',conditions=['Barrel full of wine','Immersion at that site'],uncertainty=['Source says יין here, מים in preceding report; retain both without harmonizing.'])
c('c12','4a:9','חיישינן לשלשה לוגין שאובין שלא יהו במקום אחד','The baraita explains concern for three log of drawn liquid together.','anonymous baraita',conditions=['Same case'],uncertainty=['Wine wording beside שאובין retained as printed.'])
c('c13','4a:9','וכן ככר של תרומה שנפל שם טמא','A loaf of terumah that fell there is impure.','anonymous baraita',conditions=['Same site as barrel fall'])
q('q01','4a:10','מאי וכן','What does the added likewise teach?',['c14','c15'])
c('c14','4a:10','מהו דתימא התם אוקי גברא אחזקיה הכא אוקי תרומה אחזקה','One might preserve the person\'s prior impurity but preserve terumah\'s prior purity, distinguishing the cases.','anonymous sugya','rejected')
c('c15','4a:10','קמ"ל','The terumah clause rejects that proposed distinction and applies impurity there too.','anonymous sugya')
c('c16','4a:11','מעידין אנו באיש פלוני שחייב לחבירו מאתים זוז ונמצאו זוממין לוקין ומשלמין','Witnesses refuted as zomemim after testifying to a 200-zuz debt both receive lashes and pay.','רבי מאיר',conditions=['Debt testimony: 200 zuz','Witnesses become zomemim'])
c('c17','4a:11','שלא השם המביאן לידי מכות מביאן לידי תשלומין דברי ר\' מאיר','The grounds bringing lashes differ from the grounds bringing payment.','רבי מאיר',conditions=['Same monetary false-testimony case'])
c('c18','4a:11','וחכ"א כל המשלם אינו לוקה','Whoever pays does not also receive lashes.','חכמים',conditions=['Same liability discussion'])
c('c19','4a:12','מעידין אנו באיש פלוני שהוא חייב מלקות ארבעים ונמצאו זוממין לוקין שמונים','Witnesses made zomemim after alleging liability for forty lashes receive eighty.','רבי מאיר',conditions=['Original allegation: forty lashes'])
c('c20','4a:12','משום (שמות כ, יג) לא תענה ברעך עד שקר ומשום (דברים יט, יט) ועשיתם לו כאשר זמם דברי ר\' מאיר','The two sets derive from false testimony and reciprocal plotting punishment.','רבי מאיר',conditions=['Same forty-lash allegation'])
c('c21','4a:12','וחכ"א אין לוקין אלא ארבעים','Only forty lashes are administered.','חכמים',conditions=['Same forty-lash allegation'])
c('c22','4b:1','כדי רשעתו כתיב משום רשעה אחת אתה מחייבו ואי אתה מחייבו משום שתי רשעיות','The rabbis derive liability for one wickedness rather than two from כדי רשעתו.','anonymous explanation of חכמים')
q('q02','4b:1','אלא רבי מאיר מ"ט','What is R. Meir\'s rationale?',['c23','c25'])
c('c23','4b:2','אמר עולא גמר ממוציא שם רע מה מוציא שם רע לוקה ומשלם אף כל לוקה ומשלם','Ulla explains R. Meir by analogy to the slanderer, who both receives lashes and pays.','עולא',conditions=['First placement of Ulla\'s teaching: explaining R. Meir'])
c('c24','4b:2','מה למוציא שם רע שכן קנס','The analogy is challenged because the slanderer\'s payment is a fine.','anonymous sugya','challenged')
c('c25','4b:2','סבר לה כר\' עקיבא דאמר עדים זוממין קנסא הוא','The answer makes R. Meir agree with R. Akiva that zomemim liability is a fine.','anonymous explanation of רבי מאיר',conditions=['First Ulla version'])
c('c26','4b:3','איכא דמתני להא דעולא אהא דתניא','An alternative transmission places Ulla\'s statement on the following baraita, not on R. Meir.','anonymous alternative transmitters')
c('c27','4b:3','בא הכתוב ליתן עשה אחר ל"ת לומר שאין לוקין עליו דברי ר\' יהודה','The positive command after the prohibition against leaving paschal meat explains why no lashes apply.','רבי יהודה',conditions=['לא תותירו and its following positive command'])
c('c28','4b:4','ר\' עקיבא אומר לא מן השם הוא זה אלא משום דה"ל לאו שאין בו מעשה','R. Akiva rejects that rationale and explains the exemption by absence of an act.','רבי עקיבא',conditions=['Leaving paschal meat'])
c('c29','4b:4','וכל לאו שאין בו מעשה אין לוקין עליו','A prohibition without an act does not incur lashes.','רבי עקיבא')
c('c30','4b:4','מכלל דר\' יהודה סבר לאו שאין בו מעשה לוקין עליו','The discussion infers that R. Judah allows lashes for a prohibition without an act.','anonymous inference about רבי יהודה')
q('q03','4b:4','מנא ליה','What is the source for the inferred R. Judah rule?',['c31','c33','c36'])
c('c31','4b:5','אמר עולא גמר ממוציא שם רע מה מוציא שם רע לאו שאין בו מעשה לוקין עליו אף כל לאו שאין בו מעשה לוקין עליו','In the alternative transmission Ulla derives the no-act lashes rule from the slanderer.','עולא','challenged',conditions=['Explaining R. Judah, alternative placement'])
c('c32','4b:5','מה למוציא שם רע שכן לוקה ומשלם','Objection: the slanderer is distinctive in both being lashed and paying.','anonymous sugya','challenged')
c('c33','4b:6','אלא אמר ריש לקיש גמר מעדים זוממין מה עדים זוממין לאו שאין בו מעשה לוקין עליו אף כל לאו שאין בו מעשה לוקין עליו','Resh Lakish instead derives the no-act lashes rule from zomemim.','ריש לקיש','challenged',conditions=['Explaining R. Judah'])
c('c34','4b:6','מה לעדים זוממין שכן אין צריכין התראה','Objection: zomemim are distinctive in not requiring prior warning.','anonymous sugya','challenged')
c('c35','4b:7','מוציא שם רע יוכיח','The slanderer counters the warning-based objection.','anonymous sugya')
c('c36','4b:7','וחזר הדין לא ראי זה כראי זה ולא ראי זה כראי זה הצד השוה שבהן לאו שאין בו מעשה ולוקין עליו אף כל לאו שאין בו מעשה לוקין עליו','A common-feature argument from both cases yields lashes for no-act prohibitions.','anonymous sugya',conditions=['R. Judah\'s derivation; no one exemplar alone suffices'])
c('c37','4b:8','מה להצד השוה שבהן שכן קנס','Objection: the common feature includes a fine.','anonymous sugya','rejected')
c('c38','4b:8','הא לא קשיא רבי יהודה לא סבר לה כרבי עקיבא','That objection fails because R. Judah does not agree with R. Akiva\'s fine classification of zomemim.','anonymous explanation of רבי יהודה')
c('c39','4b:9','אלא מה להצד השוה שבהן שכן יש בהן צד חמור','Alternative objection: each exemplar has a special stringency.','anonymous sugya','challenged')
c('c40','4b:9','ורבי יהודה צד חמור לא פריך','R. Judah does not treat special stringency as a valid objection to this common-feature derivation.','anonymous explanation of רבי יהודה')
q('q04','4b:10','ורבנן האי (שמות כ, יג) לא תענה ברעך עד שקר מאי דרשי ביה','How do the rabbis use לא תענה?',['c41'])
c('c41','4b:11','ההוא מיבעי ליה לאזהרה לעדים זוממין','The rabbis need לא תענה as the prohibition for zomemim.','anonymous explanation of חכמים')
q('q05','4b:11','ורבי מאיר אזהרה לעדים זוממין מנא ליה','What is R. Meir\'s source for the prohibition for zomemim?',['c42'])
c('c42','4b:11','אמר רבי ירמיה נפקא ליה (דברים יט, כ) מוהנשארים ישמעו ויראו ולא יוסיפו עוד','R. Jeremiah explains R. Meir\'s prohibition source as והנשארים ישמעו ויראו ולא יוסיפו עוד.','רבי ירמיה',conditions=['Explanation of רבי מאיר, not an independent attribution of R. Meir\'s words'])
c('c43','4b:12','ורבנן ההוא מיבעי ליה','The rabbis need that other verse for public proclamation (sentence completed at 5a:1).','anonymous explanation of חכמים')
rec[-4]['evidence'].append(ev('5a:1','להכרזה'))
c('c44','5a:1','ורבי מאיר הכרזה מישמעו ויראו נפקא','R. Meir derives proclamation specifically from ישמעו ויראו.','anonymous explanation of רבי מאיר')
c('c45','5a:2','משלשין בממון ואין משלשין במכות','Monetary liability is apportioned among the witnesses; lashes are not apportioned.','anonymous Mishnah')
c('c46','5a:2','כיצד העידוהו שהוא חייב לחבירו מאתים זוז ונמצאו זוממין משלשין ביניהם','For false testimony alleging a 200-zuz debt, zomemim divide the monetary payment among themselves.','anonymous Mishnah',conditions=['200-zuz allegation','Zomemim'])
c('c47','5a:2','אבל אם העידוהו שהוא חייב מלקות ארבעים ונמצאו זוממין כל אחד ואחד לוקה ארבעים','For false testimony alleging forty lashes, every zomem witness receives forty.','anonymous Mishnah',conditions=['Forty-lash allegation','Zomemim'])
q('q06','5a:3','מנא ה"מ','What establishes that lashes are not divided?',['c48','c49'])
c('c48','5a:3','אמר אביי נאמר (דברים כה, ב) רשע בחייבי מלקיות ונאמר (במדבר לה, לא) רשע בחייבי מיתות ב"ד מה להלן אין מיתה למחצה אף כאן אין מלקות למחצה','Abaye connects רשע in lashes and death: as there is no partial death, there are no partial lashes.','אביי')
c('c49','5a:4','רבא אמר בעינן (דברים יט, יט) כאשר זמם לעשות לאחיו וליכא','Rava requires fulfillment of the intended harm; divided lashes fail that condition.','רבא')
q('q07','5a:4','אי הכי ממון נמי','Should that reasoning not also prevent dividing monetary liability?',['c50','c51'])
c('c50','5a:4','ממון מצטרף','Money paid by separate witnesses combines into the full intended sum.','anonymous response')
c('c51','5a:4','מלקות לא מצטרף','Lashes on different witnesses do not combine.','anonymous response')
c('c52','5a:5','אין העדים נעשים זוממין עד שיזימו את עצמן','Witnesses become zomemim only when the refutation targets the witnesses themselves.','anonymous Mishnah',uncertainty=['את עצמן does not mean confession; the following examples specify their whereabouts.'])
c('c53','5a:6','כיצד אמרו מעידין אנו באיש פלוני שהרג את הנפש אמרו להם היאך אתם מעידין שהרי נהרג זה או ההורג זה היה עמנו אותו היום במקום פלוני אין אלו זוממין','Contradicting the location of the alleged victim or murderer does not make the original witnesses zomemim.','anonymous Mishnah',conditions=['Original murder testimony','Countertestimony puts victim OR murderer elsewhere that day'])
c('c54','5a:6','אבל אמרו להם היאך אתם מעידין שהרי אתם הייתם עמנו אותו היום במקום פלוני הרי אלו זוממין ונהרגין על פיהם','Countertestimony that the witnesses themselves were elsewhere that day makes them zomemim and they are executed on that testimony.','anonymous Mishnah',conditions=['Original murder testimony','Alibi targets original witnesses themselves'])
c('c55','5a:7','באו אחרים והזימום באו אחרים והזימום אפי\' מאה כולם יהרגו','Even when further groups are refuted, up to a hundred, all the refuted groups are executed.','anonymous Mishnah',conditions=['Repeated hazamah groups'],uncertainty=['Compressed repeated-group wording interpreted with 5b:1–7; avoid inventing a new separate chain of counter-witnesses.'])
c('c56','5a:7','רבי יהודה אומר איסטטית היא זו ואינו נהרג אלא כת הראשונה בלבד','R. Judah calls this איסטטית and says only the first group is executed.','רבי יהודה','unresolved',conditions=['Repeated-group case'],uncertainty=['Continuation 5b:1–2 challenges coherence; Rava\'s reading leaves קשיא. Do not present unqualified settled rule.'])
q('q08','5a:8','מנא הני מילי','What is the scriptural source for targeting witnesses themselves?',['c57','c58'])
c('c57','5a:8','אמר רב אדא דאמר קרא (דברים יט, יח) והנה עד שקר העד שקר ענה עד שתשקר גופה של עדות','Rav Adda derives the requirement from והנה עד שקר העד: falsification must target the body of testimony.','רב אדא')
c('c58','5a:9','דבי ר\' ישמעאל תנא (דברים יט, טז) לענות בו סרה עד שתסרה גופה של עדות','The school of R. Ishmael teaches the requirement from לענות בו סרה, removing the body of testimony.','דבי רבי ישמעאל',uncertainty=['School teaching, not necessarily R. Ishmael personally speaking.'])
c('c59','5a:10','אמר רבא באו שנים ואמרו במזרח בירה הרג פלוני את הנפש ובאו שנים ואמרו והלא במערב בירה עמנו הייתם חזינן אי כדקיימי במערב בירה מיחזא חזו למזרח בירה אין אלו זוממין','Rava: witnesses alleging murder east of the building who are placed west are not zomemim if east can be seen from west.','רבא',conditions=['Two original witnesses','Two counter-witnesses place them west','East visible from west'])
c('c60','5a:10','ואם לאו הרי אלו זוממין','If the east cannot be seen from the west, the witnesses are zomemim.','רבא',conditions=['Same east/west case','No ordinary line of sight'])
q('q09','5a:11','פשיטא','Why is Rava\'s visibility rule not obvious?',['c61','c62'])
c('c61','5a:11','מהו דתימא ליחוש לנהורא בריא','One might allow for unusually strong sight.','anonymous sugya','rejected',conditions=['Ordinary visibility absent'])
c('c62','5a:11','קמשמע לן','The rule teaches not to assume extraordinary eyesight to defeat hazamah.','anonymous sugya')
c('c63','4b:2','כר\' עקיבא דאמר עדים זוממין קנסא הוא','R. Akiva classifies the payment of zomemim as a fine.','רבי עקיבא',conditions=['Cited to explain R. Meir in first Ulla version'])

# Necessary source-only context, separately scoped and never credited as sampled cores.
c('x01','3b:17','אמר רבא לא קשיא הא רבי יוחנן בן נורי הא רבנן','Rava reconciles the contrasting immersion teachings as R. Yohanan ben Nuri versus the rabbis.','רבא','reconciled')
c('x02','4a:3','רב תני חסר קורטוב ברישא','First possibility in Rav Pappa\'s inquiry: Rav teaches less one kortov in the opening case.','רב פפא','hypothetical')
c('x03','4a:3','ורב אומר כר\' יוחנן בן נורי','On that first possibility Rav follows R. Yohanan ben Nuri.','רב פפא','hypothetical')
c('x04','4a:4','או דלמא רב לא תני חסר קורטוב ברישא ור\' יוחנן בן נורי כי פליג אסיפא הוא דפליג','Alternative: Rav omits less one kortov; R. Yohanan ben Nuri disputes only the final case.','רב פפא','hypothetical')
c('x05','4a:5','ורב דאמר כדברי הכל','On that alternative Rav agrees with everyone.','רב פפא','hypothetical')
q('xq1','5b:1','אי איסטטית היא זו אפי\' כת ראשונה נמי לא','If the refuting group is suspect, why execute even the first group?',['x06','x07'])
c('x06','5b:1','אמר ר\' אבהו שקדמו והרגו','R. Abbahu proposes that they already executed the first group.','רבי אבהו','rejected')
q('xq2','5b:2','מאי דהוה הוה','What relevance has an execution already performed?',['x07'])
c('x07','5b:2','אלא אמר רבא הכי קאמר אם אינה אלא כת אחת נהרגת אי איכא טפי אין נהרגין','Rava reformulates R. Judah: if there is just one group it is executed, but if more none are executed.','רבא','challenged',conditions=['Interpretation of רבי יהודה, not independent new Mishnah text'])
c('x08','5b:2','הא בלבד קאמר קשיא','The wording only [the first] resists Rava\'s reconstruction; difficulty remains.','anonymous sugya','unresolved')
c('x09','5b:3','ההיא איתתא דאתאי סהדי ואישתקור אייתי סהדי ואישתקור אזלה אייתי סהדי אחריני דלא אישתקור','A woman brought two successive groups exposed as false, then another not exposed as false.','anonymous narrator')
c('x10','5b:3','אמר ריש לקיש הוחזקה זו','Resh Lakish treats the woman as established in producing false witnesses.','ריש לקיש',conditions=['Narrated repeated false groups'])
c('x11','5b:3','א"ל ר\' אלעזר אם היא הוחזקה כל ישראל מי הוחזקו','R. Eleazar objects that her established unreliability does not establish all Israel\'s unreliability.','רבי אלעזר')
c('x12','5b:4','אמר ריש לקיש הוחזקה זו א"ל רבי יוחנן אם הוחזקה זו כל ישראל מי הוחזקו','In a similar case before R. Yohanan, Resh Lakish repeats his ruling and R. Yohanan voices the same objection.','anonymous narrator',uncertainty=['Separate narrative occurrence from 5b:3 retained.'])
c('x13','5b:4','הדר חזיה לרבי אלעזר בישות אמר ליה שמעת מילי מבר נפחא ולא אמרת לי משמיה','Resh Lakish reproaches R. Eleazar for not reporting the teaching in Bar Nappaha\'s name.','ריש לקיש',uncertainty=['Report of reproach; does not independently prove what R. Eleazar had previously heard. בר נפחא contextually רבי יוחנן.'])
q('xq3','5b:5','לימא ריש לקיש דאמר כרבי יהודה ורבי יוחנן דאמר כרבנן','Must Resh Lakish align with R. Judah and R. Yohanan with the rabbis?',['x14','x15'])
c('x14','5b:6','אמר לך ריש לקיש אנא דאמרי לך אפי\' לרבנן עד כאן לא קא אמרי רבנן התם דליכא דקא מהדר אבל הכא איכא הא דקא מהדרא','A reconstructed reply for Resh Lakish permits agreement even with the rabbis: here the woman actively seeks witnesses.','anonymous reconstruction for ריש לקיש','reconciled',conditions=['Woman seeks repeated witnesses; unlike Mishnah'])
c('x15','5b:7','ורבי יוחנן אמר לך אנא דאמרי אפי\' לרבי יהודה עד כאן לא קאמר רבי יהודה התם דאמרינן אטו כולי עלמא גבי הני הוו קיימי אבל הכא הני ידעי בסהדותא והני לא ידעי בסהדותא:','A reconstructed reply for R. Yohanan permits agreement even with R. Judah: the Mishnah asks whether everyone was with these refuters; here some know the facts and others do not.','anonymous reconstruction for רבי יוחנן','reconciled')

for id,s,t,rel,ref,quote in [
('e01','c02','c01','distinction','4a:6',None),('e02','c04','c03','correction','4a:7',None),
('e03','c07','c05','continuation','4a:7',None),('e04','c10','c08','qualification','4a:8',None),
('e05','c11','c08','support','4a:9','תניא נמי הכי'),('e06','c09','c08','support','4a:8',None),('e07','c12','c11','support','4a:9',None),
('e08','c15','c14','correction','4a:10',None),('e09','c15','q01','answer','4a:10',None),
('e10','c17','c16','support','4a:11',None),('e11','c18','c16','objection','4a:11',None),
('e12','c20','c19','support','4a:12',None),('e13','c21','c19','objection','4a:12',None),
('e14','c22','c18','support','4b:1',None),('e15','c23','q02','answer','4b:2',None),
('e16','c24','c23','objection','4b:2',None),('e17','c25','c24','answer','4b:2',None),
('e18','c26','c23','qualification','4b:3',None),('e19','c28','c27','objection','4b:4',None),
('e20','c29','c28','support','4b:4',None),('e21','c30','c27','continuation','4b:4',None),
('e22','c31','q03','answer','4b:5',None),('e23','c32','c31','objection','4b:5',None),
('e24','c33','c31','correction','4b:6',None),('e25','c34','c33','objection','4b:6',None),
('e26','c35','c34','answer','4b:7',None),('e27','c36','q03','answer','4b:7',None),
('e28','c37','c36','objection','4b:8',None),('e29','c38','c37','answer','4b:8',None),
('e30','c39','c36','objection','4b:9',None),('e31','c40','c39','answer','4b:9',None),
('e32','c41','q04','answer','4b:11',None),('e33','c42','q05','answer','4b:11',None),
('e34','c43','c42','distinction','4b:12',None),('e35','c44','c43','distinction','5a:1',None),
('e36','c48','q06','answer','5a:3',None),('e37','c49','q06','answer','5a:4',None),
('e38','q07','c49','objection','5a:4',None),('e39','c50','q07','answer','5a:4',None),('e40','c51','c50','distinction','5a:4',None),
('e41','c53','c52','qualification','5a:6',None),('e42','c54','c53','distinction','5a:6',None),
('e43','c56','c55','objection','5a:7',None),('e44','c57','q08','answer','5a:8',None),('e45','c58','q08','answer','5a:9',None),
('e46','c60','c59','distinction','5a:10',None),('e47','c62','c61','correction','5a:11',None),('e48','c62','q09','answer','5a:11',None),
('e49','x01','c02','support','3b:17',None),('e50','x04','x02','distinction','4a:4',None),('e51','c05','x04','support','4a:7',None),
('e52','xq1','c56','objection','5b:1',None),('e53','x06','xq1','answer','5b:1',None),('e54','xq2','x06','objection','5b:2',None),
('e55','x07','x06','correction','5b:2',None),('e56','x08','x07','unresolved_outcome','5b:2',None),('e57','x08','c56','unresolved_outcome','5b:2',None),
('e58','x11','x10','objection','5b:3',None),('e59','x13','x12','continuation','5b:4',None),
('e60','x14','xq3','answer','5b:6',None),('e61','x15','xq3','answer','5b:7',None)
]:edge(id,s,t,rel,ref,quote)

# Explicit transmission-role records keep reporters distinct from holders.
for id,ref,quote,surface,role,chain,links in [
('a_rav_report','4a:8','ואמר רב יהודה אמר רב','רב יהודה','transmitter',['רב יהודה','רב'],['c08','c09']),
('a_abaye_report','4a:7','אמר ליה אביי את אמרת לה ניהלן','אביי','speaker',['אביי','רב יוסף'],['c04','c05','c06','c07']),
('a_yosef_report','4a:7','את אמרת לה ניהלן','רב יוסף','transmitter',['אביי','רב יוסף'],['c05','c06','c07']),
('a_akiva_fine','4b:2','כר\' עקיבא דאמר עדים זוממין קנסא הוא','רבי עקיבא','quoted_authority',[],['c25']),
('a_meir_jeremiah','4b:11','ורבי מאיר אזהרה לעדים זוממין מנא ליה אמר רבי ירמיה','רבי מאיר','position_holder',['רבי ירמיה'],['c42']),
('a_school','5a:9','דבי ר\' ישמעאל תנא','דבי רבי ישמעאל','collective',[],['c58'])
]:add(id,'attributions',[ev(ref,quote)],dict(surface=surface,role=role,candidates=[surface],scope=', '.join(links),transmission_chain=chain),links=links)

# Every original core character owned exactly once, including markup and page-split sentence.
titles={**{r:'Immersion, appearance, recollection and retained local alternatives' for r in cores[:5]},**{r:'False witnesses: cumulative penalties and alternative derivations' for r in cores[5:20]},**{r:'Apportionment of monetary payment and lashes' for r in cores[20:23]},**{r:'Hazamah targets witnesses; repeated groups and visibility' for r in cores[23:]}}
for n,r in enumerate(cores):
    add(f's{n+1:02d}','structure',[ev(r)],dict(title=titles[r],primary=True,boundary='open_both',legacy_ids=[]),origin='editorial_inference')

# Second reading reconciliation notes, authored per original core rather than inferred from records.
notes=[
'Retained distinct Rav Pappa uncertainty and Rava certainty; checked 3b:17 and 4a:3–5; no false resolution by name order.',
'Included Rav Yosef memory report, Abaye corrective recollection, Rav textual version, R. Yohanan ben Nuri scope and all-party agreement; differentiated speaker/transmitter/holder.',
'Included Rav via Rav Judah, three-log concern, sea-only qualification and river exception; anonymous gloss not automatically Rav.',
'Included baraita immersion and terumah outcomes and reason; preserved wine versus preceding water wording.',
'Included explicit question, rejected presumption-based distinction and teaching that defeats it.',
'Included R. Meir double penalty and differing grounds, plus sages payment/no lashes.',
'Included R. Meir eighty, both scriptural grounds and sages forty; Gemara markup retained in ownership.',
'Included sages one-wickedness rationale and question concerning R. Meir.',
'Included Ulla analogy, fine objection, R. Meir alignment and quoted R. Akiva classification.',
'Included alternative placement notice and R. Judah positive-command rationale; does not merge both Ulla contexts.',
'Included R. Akiva rejection/rationale/general rule, anonymous inference about R. Judah and source question.',
'Included alternate Ulla no-act derivation and double-penalty objection; challenged rather than silently accepted.',
'Included Resh Lakish replacement derivation and lack-of-warning objection.',
'Included slanderer rejoinder, reciprocal failure of single analogies and common-feature conclusion.',
'Included proposed fine objection and rejection through R. Judah disagreement with R. Akiva.',
'Included special-stringency objection and R. Judah rejection of this objection type.',
'Question-only core: no independent asserted proposition invented; answer anchored next core.',
'Included sages prohibition use, R. Meir source question and R. Jeremiah explanation; holder distinct from explaining amora.',
'Page-split proposition completed with 5a:1; not treated as an empty fragment or free-standing unknown teaching.',
'Included proclamation completion for sages and R. Meir subphrase derivation.',
'Included general distribution rule plus separate monetary and lashes examples with amount and per-person condition.',
'Included question and Abaye death/lashes verbal analogy; does not assign it to Rava.',
'Included Rava intended-harm rationale, monetary objection and two-part money/lashes distinction.',
'Included body-of-witnesses requirement; self-refutation wording resolved through next-core examples, not confession.',
'Included both victim/murderer-location alternatives as alternatives within negative rule, and witnesses-location positive execution rule.',
'Included both repeated-group rulings; expanded to 5b:1–7, preserved rejected Abbahu answer, challenged Rava reconstruction and unresolved difficulty.',
'Included source question, Rav Adda and exact scriptural derivation.',
'Included school-level attribution and alternative verse, not R. Ishmael personally speaking.',
'Included Rava full east/west setting and both visibility branches.',
'Included obviousness question, rejected extraordinary eyesight possibility and concluding exclusion.'
]
assert len(notes)==30
layers=['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']
coverage=[]
for r,note in zip(cores,notes):
    for layer in layers:
        ids=[v['id'] for v in rec if v['layer']==layer and any(e['segment_id']==r for e in v['evidence'])]
        if layer=='reconciliation':ids=[v['id'] for v in rec if any(e['segment_id']==r for e in v['evidence'])]
        rationale=note if layer=='reconciliation' else ('Source pass complete; recorded all identified local units for this layer.' if ids else {'questions':'No further explicit question in this core; alternative statements retained as claims.','claims':'This core contains only an explicit question, recorded in questions.','positions':'No independent asserted answer or holder-position beyond the question.','utterances':'Question utterance represented by the explicit question record.','attributions':'Anonymous question voice, no named authority in this core.','edges':'No separate argument edge asserted in this segment; surrounding edges remain in their evidence segments.'}.get(layer,'No additional unit identified after source reading.'))
        coverage.append(dict(segment_id=r,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
proposal=dict(schema_version='2.0.0-production',tractate='Makkot',owner='/root/makkot_source_review020',epoch=1,source_sha256=j['source']['sha256'],protocol_sha256=j['common_documents'][0]['sha256'],schema_sha256=j['common_documents'][1]['sha256'],execution=dict(route='interactive_agent',agent_id='/root/makkot_source_review020',model_id=None),records=rec,coverage=coverage,open_tails=['R. Judah repeated-group ruling: 5b:2 ends קשיא; unresolved textual interpretation, not an unread continuation.','Rav Pappa retains uncertainty even though a different reported interpretation is definite.','Wine/water contrast preserved without source emendation.'])
context_read=[f'Makkot 3b:{n}' for n in range(1,18)]+[f'Makkot 4a:{n}' for n in range(1,6)]+[f'Makkot 5a:{n}' for n in range(12,21)]+[f'Makkot 5b:{n}' for n in range(1,26)]
out=dict(artifact_kind='immutable_source_only_independent_review',job_id=j['job_id'],reviewer_agent_id='/root/makkot_source_review020',model_id=None,blindness=dict(production_inspected=False,prior_annotations_inspected=False,handoff_inspected=False,scope=cores),job_sha256=sha(JOB.read_bytes()),bindings=bindings,plan_sha256=j['plan_sha256'],core_refs=cores,core_count=30,selected_blocks=j['selected_blocks'],context_read_refs=context_read,context_core_credit=0,context_policy='Read all listed original context; structured context records focus on dependencies needed for assigned cores, not claimed exhaustive context extraction.',source_attribution={k:source[k] for k in ['title','versionTitle','versionSource','license']},coordinate_contract='segment_id is canonical source ref; offsets Python Unicode codepoints, half-open in untouched original strings; no normalization',proposal=proposal,reconciliation_pass=dict(completed=True,method='A second source-to-inventory read of each core checked alternatives, amounts, conditional branches, narratives, quoted authority, and continuation outcomes; notes attached to each reconciliation row.',notes=notes),review_status='SOURCE_ONLY_FROZEN_NOT_COMPARED',scholarly_status='AI provisional independent reading; not human certification',ml_eligible=False)

# Mechanical validation of evidence, immutable bindings, IDs, relations, coverage and primary ownership.
import jsonschema
schema=json.loads(pathlib.Path(j['common_documents'][1]['path']).read_text(encoding='utf8'))
jsonschema.Draft202012Validator(schema).validate(proposal)
ids={v['id'] for v in rec};assert len(ids)==len(rec)
for v in rec:
    assert all(a in ids for a in v['links'])
    for e in v['evidence']:assert texts[e['segment_id']][e['start_char']:e['end_char']]==e['quote']
for r in cores:
    spans=sorted((e['start_char'],e['end_char']) for v in rec if v['layer']=='structure' and v['content']['primary'] for e in v['evidence'] if e['segment_id']==r)
    assert spans==[(0,len(texts[r]))]
assert len(coverage)==240 and len({(x['segment_id'],x['layer']) for x in coverage})==240
for block in plan['review_blocks']:
    if block['block_id'] in [b['block_id'] for b in j['selected_blocks']]:
        for s in block['spans']:assert sha(texts[s['ref']].encode())==s['span_sha256_utf8']
target=ROOT/'makkot_delegated020.json'
data=(json.dumps(out,ensure_ascii=False,indent=2)+'\n').encode('utf8')
if target.exists():
    assert target.read_bytes()==data, 'Frozen artifact differs: never overwrite'
else:
    with target.open('xb') as f:f.write(data)
digest=sha(data)
sidecar=ROOT/'makkot_delegated020.json.sha256'
sidecar_text=digest+'  '+target.name+'\n'
if sidecar.exists():assert sidecar.read_text(encoding='utf8')==sidecar_text
else:
    with sidecar.open('x',encoding='utf8') as f:f.write(sidecar_text)
receipt=dict(artifact=str(target),sha256=digest,agent_id='/root/makkot_source_review020',schema_validation='passed',binding_hash_validation='passed',plan_canonical_hash_validation='passed',exact_evidence_validation='passed',link_validation='passed',primary_partition_validation='passed',coverage_rows=240,cores=30,context_core_credit=0,records_by_layer=dict(collections.Counter(v['layer'] for v in rec)),source_only=True,producer_comparison_performed=False,author_script_sha256=sha(pathlib.Path(__file__).read_bytes()))
with (ROOT/'makkot_delegated020_validation_receipt.json').open('x',encoding='utf8') as f:json.dump(receipt,f,ensure_ascii=False,indent=2)
print(json.dumps(receipt,ensure_ascii=False,indent=2))
