"""Manual continuation through 4a:4: preserve reported narratives and ambiguity."""
from author_opening_001 import *
records.clear()
prior=['3a:'+str(i) for i in range(10,15)]+['3b:'+str(i) for i in range(1,10)]
new=['3b:'+str(i) for i in range(10,15)]+['4a:'+str(i) for i in range(1,5)]
st=add('b4.language','structure',dict(title='Refined language, concise and indirect speech, and narrative inferences from wording',primary=True,boundary='closed',legacy_ids=[]),[ev(x) for x in prior+new],origin='editorial_inference',uncertainty=['The last two tribal-origin anecdotes are adjacent thematic examples; not legal proof of historical genealogy.'])
records[-1]['supersedes']='pe.r001.b3.language'
claim('b4.aramean','3b:10','ההוא ארמאה דהוה סליק ואכיל פסחים בירושלים','An Aramean used to go up and eat Passover offerings in Jerusalem.',scope='Narrator’s report, not independently verified history')
boast=claim('b4.boast','3b:10','אמר כתיב (שמות יב, מג) כל בן נכר לא יאכל בו (שמות יב, מח) כל ערל לא יאכל בו ואנא הא קאכילנא משופרי שופרי','He boasts that despite the scriptural prohibitions he eats the best portions.',holder='unnamed Aramean',scope='Reported boast with embedded biblical citations')
for key,quote,prop in [('foreign','כל בן נכר לא יאכל בו','The cited verse excludes a foreigner from eating the Passover offering.'),('uncircumcised','כל ערל לא יאכל בו','The cited verse excludes an uncircumcised person from eating it.')]:
    claim('b4.'+key,'3b:10',quote,prop,scope='Biblical prohibition quoted within the Aramean speech',role='biblical quotation')
q=question('b4.tail.q','3b:11','מי קא ספו לך מאליה','Do they feed you from the fat tail?')
no=claim('b4.tailno','3b:11','אמר ליה לא','He answers no.',holder='unnamed Aramean',scope='Reply to Rabbi Yehuda ben Beteira')
edge('b4.tailno.answer',no,q,'answer','3b:11','אמר ליה לא')
plan=claim('b4.tailplan','3b:11','כי סלקת להתם אימא להו ספו לי מאליה','Rabbi Yehuda ben Beteira instructs him to ask for the fat tail next time he goes there.',holder='רבי יהודה בן בתירא',conditions=['next visit'],scope='Narrative instruction, not dietary permission')
request=claim('b4.tailrequest','3b:11','כי סליק אמר להו מאליה ספו לי','On going up he asks to be given fat tail.',holder='unnamed Aramean',scope='Narrated request implementing the instruction')
altar=claim('b4.tailaltar','3b:11','אמרו ליה אליה לגבוה סלקא','They tell him that the fat tail goes to the Most High.',holder='unnamed Jerusalem interlocutors',scope='Narrative reply about the sacrificial portion')
edge('b4.tailaltar.answer',altar,request,'answer','3b:11','אמרו ליה אליה לגבוה סלקא')
who=question('b4.who.q','3b:12','מאן אמר לך הכי','Who told you this?')
name=claim('b4.name','3b:12','אמר להו רבי יהודה בן בתירא','He names Rabbi Yehuda ben Beteira as the source of the instruction.',holder='unnamed Aramean',scope='Identification of the adviser')
edge('b4.name.answer',name,who,'answer','3b:12','אמר להו רבי יהודה בן בתירא')
question('b4.suspicion.q','3b:12','מאי האי דקמן','What is happening before us?')
investigation=claim('b4.investigation','3b:12','בדקו בתריה ואשכחוהו דארמאה הוא וקטלוהו','They investigate, find that he is an Aramean, and kill him.',scope='Narrator reports a sequence; no universal rule or modern normative instruction inferred')
message=claim('b4.message','3b:12',"שלחו ליה לרבי יהודה בן בתירא שלם לך ר' יהודה בן בתירא דאת בנציבין ומצודתך פרוסה בירושלים",'They send Rabbi Yehuda ben Beteira a greeting: he is in Netzivin but his net is spread in Jerusalem.',holder='unnamed senders from Jerusalem',scope='Narrative message praising remote intervention')
ill=claim('b4.ill','3b:13','רב כהנא חלש','Rav Kahana becomes ill.',scope='Narrative frame')
mission=claim('b4.mission','3b:13',"שדרוה רבנן לר' יהושע בריה דרב אידי אמרו ליה זיל בדוק מאי דיניה",'The rabbis send Rabbi Yehoshua son of Rav Idi to check his condition.',holder='רבנן',scope='Narrative mission; messenger distinct from patient')
death=claim('b4.death','3b:13','אתא אשכחיה דנח נפשיה','The messenger arrives and finds that Rav Kahana has died.',scope='Narrator’s report')
tear=claim('b4.tear','3b:13','קרעיה ללבושיה ואהדריה לקרעיה לאחוריה ובכי ואתי','He tears his garment, turns the tear to the back, and comes weeping.',scope='Narrated actions of Rabbi Yehoshua son of Rav Idi')
dq=question('b4.death.q','3b:13','אמרו ליה נח נפשיה','They ask whether he has died.')
indirect=claim('b4.indirect','3b:13','אמר להו אנא לא קאמינא (משלי י, יח) ומוציא דבה הוא כסיל','He declines to say it himself, citing the verse about one who brings an evil report being a fool.',holder='רבי יהושע בריה דרב אידי',scope='Indirect death report; no denial of the narrated death')
edge('b4.indirect.answer',indirect,dq,'answer','3b:13','אמר להו אנא לא קאמינא (משלי י, יח) ומוציא דבה הוא כסיל')
journey=claim('b4.journey','3b:14','יוחנן חקוקאה נפק לקרייתא','Yohanan Hakkukaah goes out to the villages.',scope='Narrative frame; not silently identified with another Yohanan')
wq=question('b4.wheat.q','3b:14','חיטין נעשו יפות','Has the wheat grown well?')
barley=claim('b4.barley','3b:14','אמר להם שעורים נעשו יפות','He replies that the barley has grown well.',holder='יוחנן חקוקאה',scope='Indirect answer to a wheat question')
rebuke=claim('b4.rebuke','3b:14','אמרו ליה צא ובשר לסוסים ולחמורים דכתיב (מלכים א ה, ח) השעורים והתבן לסוסים ולרכש','They tell him to bring that news to horses and donkeys, citing the verse about barley and straw for horses.',holder='unnamed interlocutors',scope='Narrative criticism of wording')
edge('b4.barley.answer',barley,wq,'answer','3b:14');edge('b4.rebuke.objection',rebuke,barley,'objection','3b:14')
aq=question('b4.alternative.q','3b:14','מאי הוי ליה למימר','What should he have said?')
lastyear=claim('b4.lastyear','3b:14','אשתקד נעשו חיטין יפות','One suggested answer is that last year the wheat grew well.',mode='hypothetical',scope='Anonymous suggested wording, not reported agricultural fact')
lentils=claim('b4.lentils','3b:14','אי נמי עדשים נעשו יפות','Another suggested answer is that the lentils grew well.',mode='hypothetical',scope='Alternative suggested wording, not reported crop measurement')
edge('b4.lastyear.answer',lastyear,aq,'answer','3b:14','אשתקד נעשו חיטין יפות');edge('b4.lentils.answer',lentils,aq,'answer','3b:14','אי נמי עדשים נעשו יפות')
kin=claim('b4.kin','4a:1',"רב בר אחוה דר' חייא ובר אחתיה",'Rav is described as the son of Rabbi Hiyya’s brother and of his sister.',scope='Narrative kinship statement; no expanded family tree supplied')
exchange=add('b4.exchange.u','utterances',dict(textual_voice='Rav and Rabbi Hiyya in a reported exchange',discourse_role='indirect family death report',composition='composite'),[ev('4a:1','כי סליק להתם אמר ליה אייבו קיים אמר ליה אימא קיימת אמר ליה אימא קיימת אמר ליה אייבו קיים')],uncertainty=['Printed pronouns and repeated questions do not explicitly name each speaker; preserve literal sequence.'])
add('b4.exchange.a','attributions',dict(surface='אמר ליה',role='speaker',candidates=['רב','רבי חייא'],scope=exchange+'; dialogue sequence with unprinted names',transmission_chain=[]),[ev('4a:1')],[exchange],uncertainty=['Speaker mapping should be reviewed before person-specific use.'])
for key,quote,form in [('ibo','אייבו קיים','Is Aivo alive?'),('mother','אימא קיימת','Is mother alive?')]:
    # Repeated surface: exact first and second occurrences preserved separately.
    text=refs['4a:1']['text'];start=0
    for i in range(2):
        at=text.index(quote,start);start=at+len(quote)
        e=dict(segment_id=refs['4a:1']['id'],start_char=at,end_char=start,quote=quote)
        add('b4.'+key+'.q'+str(i),'questions',dict(formulation=form,question_origin='explicit',conditions=[],answer_set_status='none'),[e],[exchange],uncertainty=['Indirect dialogue; occurrence retained without converting a question into a literal affirmative answer.'])
action=claim('b4.action','4a:2','אמר ליה לשמעיה חלוץ לי מנעלי והוליך כלי אחרי לבית המרחץ','He tells his attendant to remove his shoes and take his belongings after him to the bathhouse.',scope='Narrative consequence; contextual actor Rabbi Hiyya',uncertainty=['Subject is not named in this segment; dependent on preceding dialogue.'])
for key,quote,prop in [('shoes','ש"מ אבל אסור בנעילת הסנדל','A mourner is forbidden to wear sandals.'),('distant','ושמע מינה שמועה רחוקה אינה נוהגת אלא יום אחד','Distant news of death requires mourning for only one day.'),('partial','ושמע מינה מקצת היום ככולו','Part of a day counts as the whole day.')]:
    c=claim('b4.'+key,'4a:2',quote,prop,scope='One of three explicit anonymous inferences from the narrative')
    edge('b4.'+key+'.support',action,c,'support','4a:2',quote)
danquote=claim('b4.danquote','4a:3','ההוא דאמר דונו דיני','A man repeatedly says: judge my case.',holder='unnamed man',scope='Narrative wording')
dan=claim('b4.dan','4a:3','אמרי שמע מינה מדן קאתי דכתיב (בראשית מט, טז) דן ידין עמו כאחד שבטי ישראל','They infer he descends from Dan, citing Dan judging his people.',holder='unnamed observers',scope='Text-reported tribal inference; not independent genealogy')
edge('b4.dan.support',danquote,dan,'support','4a:3')
sea=claim('b4.sea','4a:4','ההוא דהוה קא אזיל ואמר אכיף ימא אסיסני ביראתא','Another man repeatedly speaks of placing his dwellings at the seashore.',holder='unnamed man',scope='Reported expression; translation provisional')
zeb=claim('b4.zeb','4a:4','בדקו ואשכחוהו דמזבולן קאתי דכתיב (בראשית מט, יג) זבולון לחוף ימים ישכון','They investigate and find him descended from Zebulun, citing the seashore verse.',scope='Narrative finding; not externally verified ancestry')
edge('b4.zeb.support',sea,zeb,'support','4a:4')
notes4={
'3b:10':'Read narrative, boast and both embedded prohibitions; retain reported eating without treating the boast as permission.',
'3b:11':'Read question, negative reply, instruction, request and sacrificial-fat answer; narrative instruction distinguished from normative rule.',
'3b:12':'Read two questions, adviser identification, investigation/death sequence and greeting message; no general execution rule inferred.',
'3b:13':'Read illness, messenger mission, death, garment actions, question and indirect reply; verse citation is not an identified person.',
'3b:14':'Read journey, wheat question, barley reply, criticism and both proposed alternatives, which remain hypothetical.',
'4a:1':'Read kinship and complete repeated dialogue; each repeated question has exact separate offsets. Speaker ambiguity retained; no affirmative answer fabricated.',
'4a:2':'Read servant instruction and all three stated inferences; actor depends on previous context.',
'4a:3':'Read repeated phrase, observers’ inference and verse; no independently certified genealogy.',
'4a:4':'Read shore phrase, reported investigation and verse; narrative remains in the corpus despite no decision alternatives.'}
coverage=[]
for ref,note in notes4.items():
    sid=refs[ref]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=note+' Source-based '+layer+' pass; '+('records listed.' if ids else 'no further independent object found.')))
for ref in prior:
    coverage.append(dict(segment_id=refs[ref]['id'],layer='structure',extraction_state='completed',extraction_result='records_found',record_ids=[st],rationale='Completed narrative continuation through 4a:4; preserve earlier structure in revision lineage.'))
p=dict(schema_version=r.VERSION,tractate='Pesachim',owner='L04/pesachim_resume_20261126',epoch=3,source_sha256=meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
out=JOB/'staging'/'narratives_004.json';r.immutable(out,r.encoded(p));print(out)
