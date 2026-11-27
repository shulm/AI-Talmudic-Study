import json, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
JOB=ROOT/'jobs/bavli_meilah_supplement002.json'
job=json.loads(JOB.read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(job['source']['path'])==job['source']['sha256']
for d in job['common_documents']: assert sha(d['path'])==d['sha256']
source=json.loads(Path(job['source']['path']).read_text(encoding='utf-8-sig'))
segments={f'Meilah {i//2+1}{"a" if i%2==0 else "b"}:{j+1}':s for i,a in enumerate(source['text']) for j,s in enumerate(a)}
records=[]; byref={}; labels={}
def ev(ref):
    s=segments[ref];return {'segment_id':ref,'start_char':0,'end_char':len(s),'quote':s}
def add(layer,ref,content,links=None,origin='source_paraphrase',uncertainty=None):
    ident=f'meilah_supplement002.{layer}.{len(records)+1:04d}'
    records.append(dict(id=ident,layer=layer,evidence=[ev(ref)],content=content,origin=origin,uncertainty=uncertainty or [],links=links or []))
    byref.setdefault(ref,[]).append(ident);return ident

# Each line is a fresh source reading, not text-derived semantic classification.
# Semicolon-separated propositions are individually recorded atomic claims.
# Columns: ref | local voice/holder | assertion mode | local conditions | propositions.
DATA='''
3b:8|רב via רב גידל|asserted|זריקת פיגול|Pigul sprinkling does not remove meilah from most-holy offerings;Pigul sprinkling does not introduce meilah into lesser-holy offerings
3b:9|רב פפא challenges אביי citing anonymous teaching|asserted|Thanksgiving slaughter inside, bread outside wall|The bread is not consecrated
3b:10|anonymous quoted teaching|asserted|Thanksgiving bread and slaughter|Slaughter before bread crusts does not consecrate the bread;Even one loaf without a crust prevents bread consecration;Slaughter with outside-time intention consecrates the bread;Slaughter with outside-place intention consecrates the bread
3b:11|anonymous objection to אביי|challenged|Reading bread consecration as meilah consecration|Pigul would introduce meilah;Abaye is silent in response
3b:12|רבי אבא|asserted|Distinction between slaughter and sprinkling|The reported rule concerns sprinkling
3b:13|עולא quoted by רב אשי to רבא|asserted|Pigul handful brought onto altar|Its pigul lapses from it
3b:14|anonymous continuation of objection|asserted|Handful-taking compared with slaughter|Taking the handful corresponds to slaughter
3b:15|unnamed respondent to רב אשי|reconciled|Meaning of pigul in the cited statement|The expression means a prohibition that leads to pigul
4a:1|anonymous cited objection|challenged|Cited a-fortiori formulation|If it brings others into pigul, all the more it itself should be pigul
4a:2|anonymous answer|reconciled|Meaning of pigul in the objection|This too refers to a prohibition leading to pigul
4a:3|אילפא quoted by רבינא to רב אשי|asserted|Mixed intentions dispute|The dispute concerns two services
4a:4|אילפא quoted in continuation|asserted|First slaughter-sign outside-time, second outside-place|This is an example of the two-services dispute;In one service all agree that the intentions are mixed
4a:5|anonymous response|conditional|Subsequent sprinkling|Sprinkling reveals whether the case is one service or two
4a:6|anonymous objection|queried|Thanksgiving case under preceding explanation|Bread consecration should similarly await sprinkling
4a:7|anonymous resolution|reconciled|Meaning of consecrated bread in cited teaching|Consecrated means rendered susceptible to disqualification;Such bread requires burning
4a:8|anonymous proposed proof|hypothetical|Pigul always subject to meilah; assumption that blood was sprinkled|The teaching would support Rav Giddel's rule after sprinkling
4a:9|anonymous answer and objection|challenged|Alternative that blood was not sprinkled|The teaching may concern unsprinkled blood;Under that restriction the teaching would seem obvious
4a:10|anonymous alternative and objection|challenged|Blood sprinkled, offering interpreted as burnt offering|The teaching can instead concern a burnt offering after sprinkling;This reading seems obvious because the burnt offering is wholly for the altar
4b:1|anonymous quoted continuation|asserted|Blood remained overnight and was later sprinkled|Meilah still applies
4b:2|anonymous argument|conditional|Teaching concerns a sin offering|The continuation is intelligible on the sin-offering reading
4b:3|anonymous objection|challenged|Teaching concerns a burnt offering|Its continued meilah would need no teaching
4b:4|anonymous provisional proof|hypothetical|Relation between teaching's opening and ending|The ending certainly supports the rule;Support from the ending is proposed as support from the opening too
4b:5|anonymous qualification|challenged|Overnight delay caused by action|The overnight-delay case does not establish the thought-only pigul case;Sprinkling does not remove meilah in the overnight-delay case
4b:6|anonymous alternative|hypothetical|Pigul intention without physical action|Sprinkling may remove meilah where the defect is thought
4b:7|anonymous proposed proof and answer|challenged|Pigul of most-holy offerings|The statement that meilah applies might cover sprinkled blood and support Rav;It may instead concern blood not sprinkled
4b:8|anonymous objection|hypothetical|Suppose sprinkling removes meilah in most-holy pigul|Then the ending's switch to lesser-holy offerings requires explanation;The ending says lesser-holy pigul is not subject to meilah
4b:9|anonymous argument|asserted|Alternative division before and after sprinkling|The text could have divided the most-holy case by sprinkling;The stated ending certainly supports the rule concerning lesser-holy offerings
4b:10|anonymous qualification|reconciled|Attempt to extend ending's proof to opening|The lesser-holy ruling is categorical;The most-holy case is not categorical
4b:11|רבי יהושע|asserted|Whether offering ever had a period permitted to priests|An offering that had a period of priestly permission is not subject to meilah;An offering without such a period is subject to meilah
4b:12|quoted teaching of רבי יהושע|asserted|Examples of a prior period permitted to priests|An offering subsequently left overnight had a permitted period;An offering subsequently impure had a permitted period;An offering subsequently taken out had a permitted period
4b:13|quoted teaching of רבי יהושע|asserted|Examples without a permitted period|Outside-time slaughter had no permitted period;Outside-place slaughter had no permitted period;Disqualified persons receiving and sprinkling blood is listed as lacking a permitted period
4b:14|בר קפרא addressing בר פדת|queried|Interpretation of permission to priests|Permission from slaughter is one candidate interpretation
5a:1|חזקיה;רבי יוחנן;anonymous alternatives|asserted|Interpretation of permission to priests|Permission for sprinkling is another candidate interpretation;Permission to eat is another candidate interpretation;Hezekiah interprets the rule as permission from slaughter;Rabbi Yohanan interprets it as permission to eat
5a:2|רבי זירא|asserted|Precision of the mishnah|The mishnah does not precisely support either Hezekiah or Rabbi Yohanan
5a:3|anonymous inference|hypothetical|Assume overnight refers to blood|The mishnah denies meilah even when the blood remained overnight
5a:4|anonymous inference|hypothetical|Overnight blood and absence of meilah|The criterion would be permission for sprinkling
5a:5|anonymous answer|reconciled|Overnight refers to meat, blood already sprinkled|The mishnah's absence of meilah is explained by prior sprinkling
5a:6|anonymous quoted mishnah|asserted|No permitted period for priests|Outside-time slaughter is listed;Outside-place slaughter is listed;Disqualified reception and sprinkling is listed
5a:7|anonymous objection|challenged|Both reception and sprinkling performed by disqualified persons|Both defects would appear unnecessary
5a:8|anonymous inference|hypothetical|Disqualified reception followed by valid persons sprinkling|The mishnah would still impose meilah
5a:9|anonymous inference|hypothetical|No fit reception despite valid slaughter|Permission for sprinkling would be the criterion
5a:10|רב יוסף|challenged|Proposed precise division of mishnah's paired verbs|The parallel washing-of-blood mishnah challenges that precision
5a:11|anonymous quoted mishnah|asserted|Disqualified sin offering|Its blood does not require washing when it once had fitness;Its blood does not require washing when it never had fitness
5a:12|anonymous quoted mishnah|asserted|Examples of prior fitness followed by disqualification|Overnight is an example;Impurity is an example;Exit is an example
5a:13|anonymous quoted mishnah|asserted|Examples without prior fitness|Outside-place slaughter is an example;Outside-time slaughter is an example;Disqualified reception and sprinkling is an example
5a:14|רב יוסף's argument continued anonymously|hypothetical|Read disqualified reception and sprinkling as a precise pair|One would infer that blood received and sprinkled by valid persons requires washing
5a:15|anonymous scriptural objection and answer|reconciled|Blood already sprinkled|The washing verse excludes blood already sprinkled;The washing mishnah's paired verbs are not precise
5b:1|anonymous analogy;רב אסי challenge|challenged|Apply nonprecision to meilah mishnah too|The meilah wording could likewise be nonprecise;Rav Assi objects that both teachings would then be redundant
5b:2|anonymous resolution|asserted|Meilah mishnah contrasted with washing mishnah|The meilah formulation is precise
5b:3|anonymous explanation|asserted|Disqualified service and remaining blood|A disqualified person can make the remaining blood residual
5b:4|anonymous explanation|asserted|Disqualified person receives and sprinkles, then valid person receives and sprinkles|The later valid service is ineffective;The remaining blood is residual
5b:5|ריש לקיש asks רבי יוחנן|queried|Disqualified person performing service|Whether a disqualified person makes residual blood is questioned
5b:6|רבי יוחנן answering ריש לקיש|asserted|Reported answer about making residual blood|Only outside-time and outside-place are stated to make residual blood;Their efficacy regarding pigul explains this
5b:7|anonymous interpretation and correction|challenged|Scope of the reported exclusion|The statement might exclude a disqualified person;The response includes a disqualified person
5b:8|anonymous objection|challenged|Literal exclusive phrase אין לך|The wording appears exclusive
5b:9|anonymous reconciliation|reconciled|Service not acceptable for community contrasted with impure priest acceptable publicly|Outside-time and outside-place uniquely make residual blood among what cannot be accepted publicly;An impure priest makes residual blood because impurity has communal allowance
5b:10|anonymous qualification|asserted|Other disqualified persons with no communal allowance|They do not make residual blood
5b:11|anonymous cited proof|asserted|Pigul|Meilah applies always according to the cited teaching
5b:12|anonymous inference|hypothetical|Assume the pigul case lacks sprinkling|The criterion would be permission for sprinkling
5b:13|anonymous answer|reconciled|Read with following segment|The case instead involves sprinkling
5b:14|רב via רב גידל quoted by anonymous explanation|asserted|Pigul sprinkling and meaning of always|Pigul sprinkling does not remove meilah;Pigul sprinkling does not introduce meilah;Always teaches Rav Giddel's rule
6a:1|רבי שמעון quoted by anonymous proof|asserted|Notar|Some notar is subject to meilah;Some notar is not subject to meilah
6a:2|רבי שמעון quoted continuation|asserted|Overnight before or after sprinkling|Overnight before sprinkling leaves meilah;Overnight after sprinkling has no meilah
6a:3|anonymous inference|hypothetical|Assume there was time to sprinkle beforehand|Meilah remains despite the prior opportunity to sprinkle
6a:4|anonymous inference|hypothetical|Meilah despite opportunity to sprinkle|Permission to eat would be the criterion
6a:5|anonymous answer|reconciled|Reception near sunset without time to sprinkle|The case need not have had an opportunity to sprinkle
6a:6|anonymous objection|hypothetical|There was time to sprinkle|The alternative implies absence of meilah
6a:7|anonymous objection|challenged|Before/after sprinkling wording under opportunity reading|The teaching should instead divide before and after sunset
6a:8|anonymous interpretive response|reconciled|Before/after interpreted as suitability|The teaching means before becoming fit for sprinkling and after becoming fit
6a:9|רבי שמעון quoted by anonymous proof|asserted|Pigul|Some pigul is subject to meilah;Some pigul is not subject to meilah
6a:10|רבי שמעון quoted continuation|asserted|Before or after sprinkling|Before sprinkling meilah applies;After sprinkling meilah does not apply
6a:11|anonymous inference|hypothetical|Assume opportunity to sprinkle before actual sprinkling|Meilah remains despite opportunity;Permission to eat would be the criterion
6a:12|anonymous answer and implication|reconciled|No opportunity to sprinkle; contrasting case with opportunity|The case lacked opportunity to sprinkle;With opportunity it would leave meilah on this reading
6a:13|anonymous objection|challenged|Wording after sprinkling under opportunity reading|The teaching should divide before and after sunset
6a:14|anonymous interpretive response|reconciled|Before/after interpreted as suitability|The teaching means before and after fitness for sprinkling
6a:15|anonymous proof and answer|challenged|Pigul in most-holy offerings|Meilah applies in the cited teaching;Assuming actual sprinkling would support the permission-to-eat criterion;The answer restricts the case to no sprinkling
6a:16|anonymous objection|hypothetical|Suppose actual sprinkling removes meilah|The ending about lesser-holy offerings needs explanation
6a:17|anonymous objection|challenged|Alternative division within most-holy offerings|The teaching could divide before and after sprinkling
6a:18|anonymous resolution|asserted|Introducing meilah|Proper sprinkling introduces meilah
6a:19|anonymous resolution|asserted|Removing meilah|Even improper sprinkling removes meilah
6b:1|anonymous mishnah framing|asserted|Meat of most-holy offerings exited before blood sprinkling|The following disagreement concerns exited most-holy meat
6b:2|רבי אליעזר|asserted|Most-holy meat exited before sprinkling|Meilah applies;Pigul liability does not apply;Notar liability does not apply;Impurity liability does not apply
6b:3|רבי עקיבא|asserted|Most-holy meat exited before sprinkling|Meilah does not apply;Pigul liability applies;Notar liability applies;Impurity liability applies
6b:4|רבי עקיבא|hypothetical|Sin offering lost, substitute designated, first recovered, both standing|The two sin offerings are the comparison case
6b:5|רבי עקיבא|asserted|The two sin offerings of the comparison|One offering's blood exempts its own meat from meilah;Its blood also exempts the other offering's meat
6b:6|רבי עקיבא|asserted|A fortiori from exempting other offering's meat|Its blood should exempt its own exited meat
6b:7|anonymous mishnah framing|asserted|Sacrificial fats of lesser-holy offerings exited before sprinkling|The following disagreement concerns exited lesser-holy fats
6b:8|רבי אליעזר;רבי עקיבא|asserted|Lesser-holy fats exited before sprinkling|Rabbi Eliezer denies meilah;Rabbi Eliezer denies pigul liability;Rabbi Eliezer denies notar liability;Rabbi Eliezer denies impurity liability;Rabbi Akiva imposes meilah;Rabbi Akiva imposes pigul liability;Rabbi Akiva imposes notar liability;Rabbi Akiva imposes impurity liability
6b:9|anonymous question|queried|Two mishnah clauses|Both cases require justification
6b:10|anonymous counterfactual about רבי אליעזר|hypothetical|Had only most-holy case been stated|Rabbi Eliezer might require proper sprinkling to remove meilah;Improper sprinkling might fail to remove it
6b:11|anonymous counterfactual about רבי אליעזר|hypothetical|Introducing meilah in lesser-holy case|Rabbi Eliezer might agree with Akiva that improper sprinkling introduces meilah
6b:12|anonymous counterfactual about רבי עקיבא|hypothetical|Had only lesser-holy case been stated|Akiva might allow improper sprinkling to introduce meilah
6b:13|anonymous counterfactual and conclusion|rejected|Removing meilah in most-holy case|Akiva might have denied removal through improper sprinkling;The paired teaching rejects that restriction
6b:14|רבי יוחנן|asserted|Interpreting Akiva on sprinkling benefiting exited flesh|Akiva's rule applies when only some exited;Akiva did not state it when all exited
6b:15|רב אסי reporting חבירי שבגולה|asserted|Challenge to Rabbi Yohanan continued in 7a:1|Rav Assi cites teaching learned from colleagues in the diaspora
7a:1|חבירי שבגולה via רב אסי|asserted|Lost or burned matter|Intention concerning the lost is effective;Intention concerning the burned is effective
7a:2|רב אסי's challenge continued anonymously|challenged|Lost and burned matter no longer exists|The teaching permits intention despite absence
7a:3|anonymous challenge reporting רב אסי to רבי יוחנן|queried|Intention concerning blood being spilled, for tomorrow|Rav Assi previously asked about this intention
7a:4|רבי זירא|asserted|Analogy with אלל lacking substance|The previously taught אלל does not receive impurity because it lacks substance
7a:5|anonymous continuation of רבי זירא's reasoning|asserted|Blood going to waste|Intention is ineffective for blood destined for loss
7a:6|רבא answering anonymous objection|reconciled|Interpretation of lost and burned in cited teaching|Lost means standing to be lost;Burned means standing to be burned
7a:7|רב פפא|asserted|Akiva's exited-material rule|Sprinkling benefits when flesh exited;Sprinkling does not benefit when blood exited
7a:8|anonymous baraita|asserted|Slaughter without expressed intention, blood exited then was sprinkled|The sprinkling is ineffective;Most-holy offerings remain subject to meilah;Lesser-holy offerings do not enter meilah
7a:9|quoted רבי עקיבא heading|asserted|Return to Akiva's analogy|Akiva introduces an analogy
7a:10|רבי אלעזר|asserted|Akiva's two-offering analogy|The rule applies simultaneously;The rule does not apply successively
7a:11|רבי שמעון narrating elder and Galilean colleagues|asserted|Report of Akiva's exited-material rule|An elder in Kefar Pani asked whether Akiva held sprinkling benefits exited material;Rabbi Shimon affirmed that report;Galilean colleagues objected that the material is invalid and cannot be accepted
7a:12|רבי עקיבא reported by רבי שמעון|asserted|Lost sin offering replaced, original found, both standing|Both offerings are subject to meilah;After both slaughtered and their blood held in cups, both remain subject to meilah
7b:1|רבי עקיבא reported by רבי שמעון|asserted|Blood of one of the two offerings sprinkled|Its blood exempts its own meat from meilah;Its blood exempts the other's meat from meilah
7b:2|רבי עקיבא reported by רבי שמעון|asserted|Other offering's invalid meat exempted by blood|A fortiori its own exited meat is exempted
7b:3|רב אושעיא via ריש לקיש|challenged|Akiva's answer to the student|Akiva gave a concealed/inadequate answer;It works simultaneously;It does not work successively
7b:4|anonymous explanation of criticism|challenged|Invalidity of the comparison offering|If invalidity is the reason, simultaneity versus succession should make no difference
7b:5|רבי יוחנן to ריש לקיש|challenged|Reish Lakish's own commitments|Rabbi Yohanan argues that Reish Lakish himself recognizes the distinction
7b:6|רבי יוחנן|hypothetical|Two guilt offerings designated for responsibility, both slaughtered, one offering's fats placed before sprinkling|Reish Lakish would concede that the raised fats descend
7b:7|עולא quoted in רבי יוחנן's argument|asserted|Lesser-holy fats raised before blood sprinkling|They do not descend;They become the altar's bread;Treating the two offerings as one body would conflict with the conceded descent
7b:8|anonymous narration;רבי יוחנן|asserted|Response to Rabbi Yohanan's challenge|Reish Lakish is silent;Rabbi Yohanan claims argumentative victory
7b:9|anonymous mishnah|asserted|Effects of blood service|For most-holy offerings blood service has lenient effects;For most-holy offerings blood service has stringent effects;For lesser-holy offerings blood service's effects are stringent
7b:10|anonymous mishnah|asserted|Most-holy offerings before/after blood sprinkling|Before sprinkling sacrificial fats are subject to meilah;Before sprinkling meat is subject to meilah;After sprinkling sacrificial fats remain subject to meilah;After sprinkling meat is not subject to meilah
7b:11|anonymous mishnah|asserted|Both fats and meat after blood service|Pigul liability applies to both;Notar liability applies to both;Impurity liability applies to both;Thus blood service in most-holy offerings has lenient and stringent effects
7b:12|anonymous mishnah|asserted|Lesser-holy offerings before/after sprinkling|Before sprinkling fats are not subject to meilah;Before sprinkling meat is not subject to meilah;After sprinkling fats are subject to meilah;After sprinkling meat is not subject to meilah
7b:13|anonymous mishnah|asserted|Both fats and meat after blood service in lesser-holy offerings|Pigul liability applies to both;Notar liability applies to both;Impurity liability applies to both;Blood service's effects are stringent in lesser-holy offerings
7b:14|anonymous inference and objection|challenged|No meilah in most-holy meat after sprinkling|The wording could imply a remaining prohibition;This is challenged because the meat is priestly property
7b:15|anonymous answer|reconciled|Mishnah's negative meilah wording|No meilah is stylistically paired with the earlier meilah ruling
7b:16|anonymous quoted mishnah|asserted|Lesser-holy meat and fats before/after sprinkling|Before sprinkling meat has no meilah;Before sprinkling fats have no meilah;Before sprinkling there is no pigul liability;Before sprinkling there is no notar liability;Before sprinkling there is no impurity liability;After sprinkling fats have meilah;After sprinkling meat has no meilah
7b:17|anonymous inference and objection|challenged|Lesser-holy meat after sprinkling|The wording could imply a remaining prohibition;This is challenged because the meat is the owners' property
7b:18|רבי חנינא|reconciled|Interpreting the cited mishnah|It concerns exited material;It follows Rabbi Akiva
7b:19|anonymous explanatory continuation|asserted|Akiva's sprinkling-benefits-exit rule|The benefit concerns burning
8a:1|anonymous explanatory continuation|asserted|Exited material after sprinkling|Sprinkling does not permit its eating
'''

parsed={}
for line in DATA.strip().splitlines():
    loc,voice,mode,conditions,props=line.split('|')
    parsed['Meilah '+loc]=(voice,mode,conditions,props.split(';'))
assert set(parsed)==set(job['core_refs'])-{'Meilah 8a:2'}

QUESTIONS={
'3b:9':'Does the thanksgiving-bread teaching refute Rav Giddel in the name of Rav?',
'3b:13':'How can Ulla call the handful pigul already, if its taking corresponds to slaughter?',
'4a:1':'Does the cited a-fortiori formulation require pigul itself rather than a precursor prohibition?',
'4a:3':'How does Ilfa’s distinction between one and two services fit the preceding account?',
'4a:6':'Should thanksgiving-bread consecration likewise await sprinkling?',
'4a:8':'Does “pigul always has meilah” support Rav Giddel’s rule?',
'4a:9':'If no sprinkling occurred, what does the teaching add?',
'4a:10':'If the offering is wholly an olah, what does continued meilah teach?',
'4b:3':'Why teach the overnight-blood case if it is an olah?',
'4b:4':'Does support from the ending establish support from the opening?',
'4b:7':'Does the teaching about most-holy pigul establish continued meilah after sprinkling?',
'4b:8':'If sprinkling removes meilah, why switch the ending to lesser-holy offerings?',
'4b:10':'Does the lesser-holy ending prove the most-holy opening?',
'4b:14':'Does the mishnah mean permission from slaughter, permission for sprinkling, or permission to eat?',
'5a:3':'Does overnight refer to the blood and establish permission for sprinkling?',
'5a:7':'Why would both invalid reception and invalid sprinkling be needed?',
'5a:10':'Can the paired verbs be read precisely given the parallel washing mishnah?',
'5a:14':'Would the inference about valid reception and sprinkling wrongly require washing already-sprinkled blood?',
'5b:1':'Why teach the paired formulation twice if neither occurrence is precise?',
'5b:5':'Does a disqualified person make remaining blood residual?',
'5b:7':'Does Rabbi Yohanan’s formulation exclude disqualified persons?',
'5b:8':'How can inclusion be reconciled with the exclusive אין לך?',
'5b:11':'Does always-meilah for pigul determine the permission criterion?',
'6a:1':'Does Rabbi Shimon’s notar distinction establish permission to eat as the criterion?',
'6a:6':'Would prior opportunity to sprinkle eliminate meilah on the alternative reading?',
'6a:7':'Why not formulate the distinction by sunset?',
'6a:9':'Does Rabbi Shimon’s pigul distinction establish permission to eat as the criterion?',
'6a:13':'Why not divide the pigul case by sunset?',
'6a:15':'Does most-holy pigul meilah establish the permission-to-eat criterion?',
'6a:16':'Why switch to lesser-holy offerings rather than divide before/after sprinkling?',
'6b:9':'Why are both most-holy flesh and lesser-holy fats disputes needed?',
'7a:2':'Does effective intention for nonexistent lost/burned material undermine the partial-exit restriction?',
'7a:3':'Did Rav Assi maintain this, given his question about blood destined for spilling?',
'7a:6':'How can the teaching concerning lost and burned material stand?',
'7a:11':'How can sprinkling secure acceptance for invalid exited material?',
'7b:4':'Why distinguish simultaneous and successive cases if the other offering is invalid?',
'7b:5':'Does Reish Lakish himself concede a distinction in the two-guilt-offering case?',
'7b:7':'If the offerings are one body, why should the raised fats descend?',
'7b:14':'Why imply a prohibition in meat that belongs to priests?',
'7b:17':'Why imply a prohibition in meat that belongs to owners?'
}
SPECIAL={
('5a:1',0):['anonymous candidate'],('5a:1',1):['anonymous candidate'],('5a:1',2):['חזקיה'],('5a:1',3):['רבי יוחנן'],
('5b:1',0):['anonymous'],('5b:1',1):['רב אסי'],
('6b:8',0):['רבי אליעזר'],('6b:8',1):['רבי אליעזר'],('6b:8',2):['רבי אליעזר'],('6b:8',3):['רבי אליעזר'],
('6b:8',4):['רבי עקיבא'],('6b:8',5):['רבי עקיבא'],('6b:8',6):['רבי עקיבא'],('6b:8',7):['רבי עקיבא'],
('7a:11',0):['unnamed elder in כפר פאני'],('7a:11',1):['רבי שמעון'],('7a:11',2):['חבירי שבגליל'],
('7b:7',2):['רבי יוחנן'],('7b:8',0):['anonymous narrator'],('7b:8',1):['רבי יוחנן']}
CHAIN={'3b:8':['רב גידל','רב'],'5b:14':['רב גידל','רב'],'3b:13':['רב אשי','עולא'],'4a:3':['רבינא','אילפא'],'4a:4':['רבינא','אילפא'],'6b:15':['רב אסי','חבירי שבגולה'],'7a:1':['רב אסי','חבירי שבגולה'],'7a:12':['רבי שמעון','רבי עקיבא'],'7b:1':['רבי שמעון','רבי עקיבא'],'7b:2':['רבי שמעון','רבי עקיבא'],'7b:3':['ריש לקיש','רב אושעיא'],'7b:7':['רבי יוחנן','עולא']}
STATUS={
'3b:8':'asserted report; attempted proofs qualified; separate contrary anonymous strand at 6a:18–19 preserved',
'3b:11':'objection followed by silence, then slaughter/sprinkling distinction and bread-burning reinterpretation; not a maintained refutation',
'4b:4':'provisional proof, qualified by action/thought distinction in 4b:5–6',
'4b:5':'printed parenthetic (לאו) retained; do not flatten wording into categorical proof',
'5a:1':'named positions retained; middle candidate is not assigned to a named sage merely by sequence',
'5a:4':'inference blocked by 5a:5',
'5a:9':'inference challenged through the washing parallel; subsequent precision debate retained',
'5b:3':'qualified in 5b:9–10 to impure priest; not all disqualified persons',
'5b:4':'qualified in 5b:9–10 to impure priest; not all disqualified persons',
'5b:6':'exclusive surface formulation is reinterpreted in 5b:9–10',
'5b:13':'read as לא, זרקה by following explicit explanation; original spacing is preserved and no normalization applied',
'6a:4':'proposed inference resisted by sunset/opportunity interpretation',
'6a:11':'proposed inference resisted by sunset/opportunity interpretation',
'6a:18':'local anonymous answer; no silent harmonization with 3b:8',
'6a:19':'local anonymous answer permits improper sprinkling to remove meilah; tension with Rav report remains explicit',
'6b:11':'counterfactual, not Rabbi Eliezer’s actual concession',
'6b:12':'counterfactual restriction, not Akiva’s final limited position',
'6b:14':'restriction challenged by lost/burned analogy; analogy reinterpreted as material still present',
'7a:1':'literal lost/burned formulation reinterpreted at 7a:6 as destined for loss/burning',
'7a:10':'simultaneity restriction retained; precise event denoted by simultaneity is not expanded beyond source',
'7b:3':'criticism answered by Rabbi Yohanan; silence follows, not an explicit named retraction',
'7b:8':'narrated silence and self-assessed victory; no express universal halakhic verdict',
'7b:19':'qualified by 8a:1: burning benefit does not authorize eating'
}
qids={}; cids={}; aids={}
for ref in job['core_refs']:
    loc=ref.split(' ')[1]
    add('structure',ref,dict(title='chapter closing marker' if loc=='8a:2' else 'original segment; local discussion continues across source boundaries',primary=True,boundary='closed' if loc=='8a:2' else 'open_both',legacy_ids=[]),origin='editorial_inference')
    if loc=='8a:2':continue
    voice,mode,cond,props=parsed[ref]
    add('utterances',ref,dict(textual_voice=voice,discourse_role=mode,composition='composite' if len(props)>1 or ';' in voice else 'atomic'))
    if loc in QUESTIONS:
        qids[loc]=add('questions',ref,dict(formulation=QUESTIONS[loc],question_origin='explicit',conditions=[cond],answer_set_status='partial'))
    aids[loc]=add('attributions',ref,dict(surface=voice,role='transmitter' if loc in CHAIN else ('anonymous' if voice.startswith('anonymous') else 'speaker'),candidates=[voice],scope='segment; atom-level holders recorded in positions',transmission_chain=CHAIN.get(loc,[])),origin='editorial_inference',uncertainty=['English labels describe discourse roles; surface is not asserted as a literal Hebrew personal name.'])
    cids[loc]=[]
    for n,prop in enumerate(props):
        cid=add('claims',ref,dict(proposition=prop,conditions=[cond],scope='local passage only',assertion_mode=mode),links=[aids[loc]])
        cids[loc].append(cid)
        holders=SPECIAL.get((loc,n),[CHAIN[loc][-1]] if loc in CHAIN else [voice])
        if loc=='5a:1' and n<2: status='candidate alternative only, not a named sage’s asserted ruling'
        else:status=STATUS.get(loc,mode+' within local argument; not an enduring or practical halakhic ruling')
        add('positions',ref,dict(holder_candidates=holders,claim_id=cid,question_id=qids.get(loc),conditions=[cond],local_status=status),links=[cid]+([qids[loc]] if loc in qids else []),origin='editorial_inference')

# Source-grounded directed relations; every edge anchored in the answering/challenging segment.
EDGES='''
3b:11|3b:8|objection
3b:12|3b:11|answer
3b:13|3b:12|objection
3b:14|3b:13|support
3b:15|3b:13|answer
4a:1|3b:15|objection
4a:2|4a:1|answer
4a:3|3b:15|objection
4a:4|4a:3|continuation
4a:5|4a:3|answer
4a:6|4a:5|objection
4a:7|4a:6|answer
4a:7|3b:10|qualification
4a:8|3b:8|support
4a:9|4a:8|objection
4a:10|4a:9|answer
4b:1|4a:10|objection
4b:2|4b:1|support
4b:3|4a:10|objection
4b:4|3b:8|support
4b:5|4b:4|qualification
4b:6|4b:5|distinction
4b:7|3b:8|support
4b:8|4b:7|objection
4b:9|4b:8|continuation
4b:10|4b:9|qualification
4b:12|4b:11|qualification
4b:13|4b:11|qualification
5a:1|4b:14|continuation
5a:2|5a:1|objection
5a:4|5a:3|support
5a:5|5a:4|answer
5a:7|5a:6|objection
5a:8|5a:7|answer
5a:9|5a:8|continuation
5a:10|5a:9|objection
5a:14|5a:13|objection
5a:15|5a:14|answer
5b:1|5a:15|analogy
5b:2|5b:1|answer
5b:3|5b:2|continuation
5b:4|5b:3|continuation
5b:5|5b:3|objection
5b:6|5b:5|answer
5b:7|5b:6|qualification
5b:8|5b:7|objection
5b:9|5b:8|answer
5b:10|5b:3|qualification
5b:12|5b:11|continuation
5b:13|5b:12|answer
5b:14|5b:11|answer
5b:14|3b:8|quotation
6a:2|6a:1|qualification
6a:3|6a:2|continuation
6a:4|6a:3|continuation
6a:5|6a:4|answer
6a:6|6a:5|objection
6a:7|6a:5|objection
6a:8|6a:7|answer
6a:10|6a:9|qualification
6a:11|6a:10|continuation
6a:12|6a:11|answer
6a:13|6a:12|objection
6a:14|6a:13|answer
6a:16|6a:15|objection
6a:17|6a:16|continuation
6a:18|6a:17|answer
6a:19|6a:18|distinction
6b:5|6b:4|continuation
6b:6|6b:3|support
6b:6|6b:5|analogy
6b:10|6b:9|answer
6b:11|6b:10|continuation
6b:12|6b:9|answer
6b:13|6b:12|qualification
6b:14|6b:3|qualification
6b:15|6b:14|objection
7a:1|6b:15|continuation
7a:2|6b:14|objection
7a:3|7a:2|objection
7a:4|7a:3|answer
7a:5|7a:4|analogy
7a:6|7a:1|correction
7a:7|6b:3|qualification
7a:8|7a:7|support
7a:10|6b:5|qualification
7a:12|7a:11|answer
7b:1|7a:12|continuation
7b:2|7b:1|analogy
7b:3|7b:2|objection
7b:4|7b:3|continuation
7b:5|7b:3|objection
7b:6|7b:5|continuation
7b:7|7b:6|support
7b:8|7b:5|local_resolution
7b:10|7b:9|qualification
7b:11|7b:10|continuation
7b:12|7b:9|qualification
7b:13|7b:12|continuation
7b:14|7b:10|objection
7b:15|7b:14|answer
7b:17|7b:16|objection
7b:18|7b:17|answer
7b:19|7b:18|qualification
8a:1|7b:19|qualification
'''
for row in EDGES.strip().splitlines():
    a,b,rel=row.split('|')
    add('edges','Meilah '+a,dict(source_id=cids[a][0],target_id=qids.get(b,cids[b][0]),relation=rel,explicitness='editorial_reconstruction'),links=[cids[a][0],qids.get(b,cids[b][0])],origin='editorial_inference',uncertainty=['Relation is between local argument units; provisional proofs and rejected alternatives retain their claim/position status.'])

context=[f'Meilah 3a:{j}' for j in range(1,10)]+[f'Meilah 3b:{j}' for j in range(1,8)]+[f'Meilah 8a:{j}' for j in range(3,7)]
coverage=[]
for ref in job['core_refs']:
    for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
        ids=[r['id'] for r in records if r['layer']==layer and any(e['segment_id']==ref for e in r['evidence'])]
        # Full reading is distinct from exhaustive atom/edge adjudication. Do not certify completeness.
        complete=layer=='structure' or ref=='Meilah 8a:2'
        coverage.append(dict(segment_id=ref,layer=layer,extraction_state='completed' if complete else 'in_progress',extraction_result='records_found' if ids else ('not_applicable' if ref=='Meilah 8a:2' else None),record_ids=ids,rationale='Exact full original segment primary ownership.' if layer=='structure' else ('Chapter closing marker; no doctrinal claims.' if ref=='Meilah 8a:2' else 'Full source segment read; source-only semantic inventory recorded, but exhaustive atom-level omission/reconciliation certification is not claimed.')))

result=dict(artifact_kind='frozen_source_only_independent_reading',job_id=job['job_id'],tractate='Meilah',cohort=job['cohort'],schema_version='2.0.0-production_record_shapes_with_review_envelope',source=job['source'],job={'path':str(JOB),'sha256':sha(JOB)},common_documents=job['common_documents'],execution={'route':'interactive_agent','agent_id':'/root/reader_meilah_supplement002','model_id':None},provenance={'source_only':True,'producer_material_accessed':False,'prior_readings_accessed':False,'context_inherited_labels':False,'source_hash_verified':True,'normalization':'none','offset_unit':'Python Unicode code points, half-open, includes original markup','source_attribution':{k:source.get(k) for k in ['title','versionTitle','versionSource','license']},'read_scope_note':'Read every listed core and context segment in original source. Context entries evidence actual reading but are not fully annotated. No web or outside commentary consulted.'},core_refs_read=job['core_refs'],context_refs_read=context,context_evidence=[ev(r) for r in context],records=records,coverage=coverage,review_status='source_reading_complete_semantic_inventory_provisional_not_exhaustiveness_certified',open_tails=['The three permission criteria are retained separately; do not assign the middle alternative by name order.','The final anonymous 6a:18–19 formulation is preserved alongside Rav’s 3b:8 report without inventing a harmonization.','5b:13 punctuation is inferred from the next segment: לא, זרקה; original quote stays unchanged.','4b:5 includes original parenthetic (לאו); local proof status remains qualified.','7a:10 simultaneity restriction is not expanded into an unsupported precise chronology.','7b:7 argument about two guilt offerings and one body is retained as Rabbi Yohanan’s argument; no external reconstruction certifies its full rationale.','All semantic layers remain in progress for exhaustive omission review; zero rows in a layer do not certify absence.'],ml_eligible=False,human_scholarly_certification=False)
result['counts']={'core_segments_read':len(job['core_refs']),'context_segments_read':len(context),'records':len(records),'by_layer':{layer:sum(r['layer']==layer for r in records) for layer in ['structure','utterances','claims','attributions','questions','positions','edges']},'fully_certified_semantic_segments':0}
for r in records:
    for e in r['evidence']:assert segments[e['segment_id']][e['start_char']:e['end_char']]==e['quote']
known={r['id'] for r in records}
assert all(x in known for r in records for x in r['links'])
out=ROOT/'readings/meilah_supplement002.json'
assert not out.exists(), 'Frozen reading must not be overwritten'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
digest=sha(out)
out.with_suffix('.json.sha256').write_text(digest+'  '+out.name+'\n',encoding='ascii')
print(json.dumps({'path':str(out),'sha256':digest,'counts':result['counts']},ensure_ascii=True))
