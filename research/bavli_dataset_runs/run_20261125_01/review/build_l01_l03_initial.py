import json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
manifest=ROOT/'research/bavli_sugya_corpus_v1/source_manifest.json'
m=json.loads(manifest.read_text(encoding='utf-8-sig'))
texts={}; sources={}
for x in m['tractates']:
 if x['title'] in ['Berakhot','Rosh Hashanah']:
  p=Path('F:/Sefaria-Export-master')/x['source_path']; h=hashlib.sha256(p.read_bytes()).hexdigest(); assert h==x['source_sha256']
  sources[x['title']]={'source_path':str(p),'source_sha256':h}
  d=json.loads(p.read_text(encoding='utf-8-sig'))
  for pi in [2,3]:
   for i,t in enumerate(d['text'][pi]): texts[f"{x['title']} {pi//2+1}{'a' if pi%2==0 else 'b'}:{i+1}"]=t
R=[]
def add(id,layer,ref,quote,content,origin='source_paraphrase',**kw):
 ref=('Berakhot ' if id.startswith('b') else 'Rosh Hashanah ')+ref
 t=texts[ref]; q=t if quote is None else quote; start=t.index(q)
 r=dict(id=id,layer=layer,origin=origin,evidence=[dict(segment_id=ref,start_char=start,end_char=start+len(q),quote=q)],content=content,**kw); R.append(r); return id
def c(id,ref,q,p,conditions=[],mode='asserted'):return add(id,'claims',ref,q,dict(proposition=p,conditions=conditions,assertion_mode=mode))
def qu(id,ref,q,p):return add(id,'questions',ref,q,dict(formulation=p,question_origin='explicit'))
def edge(id,ref,q,s,t,rel):return add(id,'edges',ref,q,dict(source_id=s,target_id=t,relation=rel,explicitness='source_explicit'))
def att(id,ref,q,holder,role='position_holder',scope=None):return add(id,'attributions',ref,q,dict(surface=q,candidates=holder,role=role,scope=scope,transmission_chain=[]))
def pos(id,ref,q,holders,claim,question=None,status='asserted',conditions=[]):return add(id,'positions',ref,q,dict(holder_candidates=holders,claim_id=claim,question_id=question,local_status=status,conditions=conditions))

# All findings were formulated against original source before any producer comparison.
qu('bq1','2a:1','מאימתי</strong></big> קורין את שמע בערבין','When does evening Shema begin?')
c('bc1','2a:1','משעה שהכהנים נכנסים לאכול בתרומתן','Evening Shema begins when priests enter to eat their terumah.')
c('bc2','2a:1','עד סוף האשמורה הראשונה דברי רבי אליעזר','Rabbi Eliezer gives the end of the first watch as the endpoint.')
c('bc3','2a:2',None,'The sages give midnight as the endpoint.')
c('bc4','2a:3',None,'Rabban Gamliel gives dawn as the endpoint.')
att('ba1','2a:1','דברי רבי אליעזר',['רבי אליעזר'],scope='bc2')
att('ba2','2a:2','וחכמים אומרים',['חכמים'],'collective','bc3')
att('ba3','2a:3','רבן גמליאל אומר',['רבן גמליאל'],scope='bc4')
for n,ref,q,h in [(2,'2a:1','עד סוף האשמורה הראשונה דברי רבי אליעזר',['רבי אליעזר']),(3,'2a:2',None,['חכמים']),(4,'2a:3',None,['רבן גמליאל'])]:pos('bp'+str(n),ref,q,h,'bc'+str(n),status='Mishnah endpoint; do not infer final practical ruling')
add('ba4','attributions','2a:4','אמרו לו לא קרינו את שמע',dict(surface='אמרו לו',role='speaker',candidates=['בני רבן גמליאל'],scope='their report that they did not recite Shema',transmission_chain=[]))
c('bc5','2a:4','לא קרינו את שמע','The sons report they did not recite Shema.')
c('bc6','2a:4','אם לא עלה עמוד השחר חייבין אתם לקרות','They remain obligated to recite Shema.',['Dawn has not risen','Sons returning from the banquet have not recited'], 'conditional')
att('ba5','2a:4','אמר להם',['רבן גמליאל'],'speaker','bc6; antecedent resolved from 2a:3–4')
pos('bp6','2a:4','אמר להם אם לא עלה עמוד השחר חייבין אתם לקרות',['רבן גמליאל'],'bc6',conditions=['Dawn has not risen'])
c('bc7','2a:4','כל מה שאמרו חכמים עד חצות מצותן עד שיעלה עמוד השחר','Everything for which sages said until midnight has its mitzvah time until dawn.')
c('bc8','2a:5','הקטר חלבים ואברים מצותן עד שיעלה עמוד השחר','Burning fats and limbs has its mitzvah time until dawn.')
c('bc9','2a:5','וכל הנאכלים ליום אחד מצותן עד שיעלה עמוד השחר','Offerings eaten for one day have their mitzvah time until dawn.')
qu('bq2','2a:5','אם כן למה אמרו חכמים עד חצות','Why did the sages say until midnight?')
c('bc10','2a:5','כדי להרחיק אדם מן העבירה','The midnight limit serves to distance a person from transgression.')
edge('be1','2a:5','כדי להרחיק אדם מן העבירה','bc10','bq2','answer')
add('ba6','attributions','2a:4','ולא זו בלבד אמרו אלא כל מה שאמרו חכמים',dict(surface='ולא זו בלבד אמרו',role='anonymous',candidates=[],scope='bc7–bc10; continuation of Mishnah, not explicitly reintroduced as named speech',transmission_chain=[]),uncertainty=['Possible continuation of Rabban Gamliel’s speech; explicit attribution boundary is absent.'])
qu('bq3','2a:6','תנא היכא קאי דקתני מאימתי','On what prior text does the tanna stand when asking from when?')
qu('bq4','2a:7',None,'Why teach evening first rather than morning?')
c('bc11','2a:8','תנא אקרא קאי דכתיב בשכבך ובקומך','The tanna stands on the verse when you lie down and when you rise.')
c('bc12','2a:8','והכי קתני זמן קריאת שמע דשכיבה אימת משעה שהכהנים נכנסין לאכול בתרומתן','The Mishnah asks when the lying-down Shema time starts and answers with priestly entry to eat terumah.')
c('bc13','2a:9',None,'Alternatively the order derives from creation: evening precedes morning.')
edge('be2','2a:8','תנא אקרא קאי דכתיב בשכבך ובקומך','bc11','bq3','answer')
edge('be3','2a:8','בשכבך ובקומך','bc11','bq4','answer')
edge('be4','2a:9',None,'bc13','bq4','answer')
qu('bq5','2a:10',None,'If so why does the later blessing Mishnah teach morning before evening?')
c('bc14','2a:10','בשחר מברך שתים לפניה ואחת לאחריה','The quoted later Mishnah prescribes two blessings before and one after morning Shema.')
c('bc15','2a:10','ובערב מברך שתים לפניה ושתים לאחריה','The quoted later Mishnah prescribes two blessings before and two after evening Shema.')
c('bc16','2a:11',None,'Having opened with evening then moved to morning, the tanna elaborates morning while on it and then evening.')
edge('be5','2a:11',None,'bc16','bq5','answer')
edge('be6','2a:10','אי הכי','bq5','bc13','objection')
add('bn1','reconciliation','2a:10',None,{'finding':'The objection can address the prior ordering rationale generally; its attachment exclusively to creation is not forced. Preserve bq5 and both earlier answers; do not manufacture a named dispute.'},'editorial_inference')

qu('rq1','2a:5','למלכים למאי הלכתא','What legal purpose has the New Year for kings?')
c('rc1','2a:5','אמר רב חסדא לשטרות','Rav Hisda explains that the kings’ New Year is relevant to documents.')
att('ra1','2a:5','רב חסדא',['רב חסדא'],scope='rc1')
pos('rp1','2a:5','אמר רב חסדא לשטרות',['רב חסדא'],'rc1','rq1')
edge('re1','2a:5','אמר רב חסדא לשטרות','rc1','rq1','answer')
c('rc2','2a:6','שטרי חוב המוקדמין פסולין','Predated debt documents are invalid.')
c('rc3','2a:6','והמאוחרין כשרין','Postdated debt documents are valid.')
edge('re2','2a:6',None,'rc2','rc1','support')
edge('re3','2a:6',None,'rc3','rc1','support')
c('rc4','2a:7','מלך שעמד בעשרים ותשעה באדר כיון שהגיע אחד בניסן עלתה לו שנה','A year is credited when Nisan 1 arrives.',['King began reign on Adar 29'])
c('rc5','2a:7','ואם לא עמד אלא באחד בניסן אין מונין לו שנה עד שיגיע ניסן אחר','No year is credited until the next Nisan.',['King began reign on Nisan 1'])
c('rc6','2b:1','דניסן ר"ה למלכים','Nisan is the New Year for kings.')
c('rc7','2b:1','ויום אחד בשנה חשוב שנה','One day in a year counts as a year.')
edge('re4','2b:1','קמ"ל דניסן ר"ה למלכים ויום אחד בשנה חשוב שנה','rc4','rc7','support')
qu('rq2','2b:1','ואם לא עמד אלא באחד בניסן אין מונין לו שנה עד שיגיע ניסן אחר פשיטא','Is it not obvious that accession on Nisan 1 requires the following Nisan?')
c('rc8','2b:2','לא צריכא דאימנו עליה מאדר','The case is needed where they appointed/agreed upon him already in Adar.',['Actual reign began on Nisan 1'])
c('rc9','2b:2','מהו דתימא נימנו ליה תרתין שנין קמ"ל','Counting two years on account of Adar appointment is a rejected hypothetical.',['Adar appointment','Nisan accession'],'rejected')
edge('re5','2b:2',None,'rc8','rq2','answer')
edge('re6','2b:2',None,'rc8','rc5','qualification')
c('rc10','2b:3','מת באדר ועמד אחר תחתיו באדר מונין שנה לזה ולזה','A year is counted for each king.',['Predecessor died in Adar','Successor began in that Adar'])
c('rc11','2b:3','מת בניסן ועמד אחר תחתיו בניסן מונין שנה לזה ולזה','A year is counted for each king.',['Predecessor died in Nisan','Successor began in that Nisan'])
c('rc12','2b:3','מת באדר ועמד אחר תחתיו בניסן מונין ראשונה לראשון ושניה לשני','The first year is counted to the first king, the second to the second.',['Predecessor died in Adar','Successor began in Nisan'])
qu('rq3','2b:4','פשיטא','Why must the same-Adar succession rule be taught?')
c('rc13','2b:4','מהו דתימא שתא לבי תרי לא מנינן קמ"ל','The possibility of refusing to count one year to two kings is rejected.',['Same-Adar succession'],'rejected')
edge('re7','2b:4','מהו דתימא שתא לבי תרי לא מנינן קמ"ל','rc13','rq3','answer')
qu('rq4','2b:5','פשיטא','Why must the same-Nisan succession rule be taught?')
c('rc14','2b:5','מהו דתימא כי אמרינן יום אחד בשנה חשוב שנה בסוף שנה אבל בתחלת שנה לא אמרינן קמ"ל','Restricting one-day-as-year to the end of the year and excluding the beginning is rejected.',['Same-Nisan succession'],'rejected')
c('rc15','2b:5','אבל בתחלת שנה לא אמרינן קמ"ל','One day at the beginning of a year also counts as a year.',['Predecessor died in Nisan; context of same-Nisan succession'])
edge('re8','2b:5','מהו דתימא כי אמרינן יום אחד בשנה חשוב שנה בסוף שנה אבל בתחלת שנה לא אמרינן קמ"ל','rc14','rq4','answer')
qu('rq5','2b:6','פשיטא','Why must the Adar-death/Nisan-successor distinction be taught?')
c('rc16','2b:6','לא צריכא דאימנו עליה מאדר ומלך בן מלך הוא','The needed case combines prior Adar appointment with the successor being a king’s son.',['Predecessor died in Adar','Successor began reign in Nisan'])
c('rc17','2b:6','מהו דתימא נימנו לי\' תרתין שנין קמ"ל','Counting two years to the successor is rejected even with both prior appointment and hereditary status.',['Adar appointment','Son of a king','Actual accession in Nisan'],'rejected')
edge('re9','2b:6','לא צריכא דאימנו עליה מאדר ומלך בן מלך הוא','rc16','rq5','answer')
edge('re10','2b:6','לא צריכא דאימנו עליה מאדר ומלך בן מלך הוא','rc16','rc12','qualification')
for id,ref,q,claims in [('ra2','2a:6','דתנן',['rc2','rc3']),('ra3','2a:7','תנו רבנן',['rc4','rc5']),('ra4','2b:3','ת"ר',['rc10','rc11','rc12'])]:
 att(id,ref,q,[],'quoted_authority',claims)
for n in [4,5,10,11,12]:
 rr=next(r for r in R if r['id']=='rc'+str(n));ev=rr['evidence'][0];pos('rp'+str(n),ev['segment_id'].split(' ',2)[2],ev['quote'],[],rr['id'],status='Anonymous baraita; no named holder supplied',conditions=rr['content']['conditions'])

core=[f'Berakhot 2a:{i}' for i in range(1,12)]+[f'Rosh Hashanah 2a:{i}' for i in range(5,9)]+[f'Rosh Hashanah 2b:{i}' for i in range(1,7)]
# These full-segment structures assert interval ownership, not that source segments are inherently sugyot.
for i,ref in enumerate(core):
 pref='b' if ref.startswith('Berakhot') else 'r';short=ref[len('Berakhot ' if pref=='b' else 'Rosh Hashanah '):]
 group=('Mishnah evening Shema' if pref=='b' and int(short.split(':')[1])<=5 else 'Explanation of Mishnah ordering') if pref=='b' else ('Purpose of kings New Year' if short in ['2a:5','2a:6'] else 'Regnal-year cases and anonymous analysis')
 add(f'{pref}s{i}','structure',short,None,dict(title=group,primary=True,boundary='open_both' if short in ['2a:8','2b:1'] and pref=='r' else 'closed',legacy_ids=[]),'editorial_inference')
 voice=('Mishnah narrator and quoted named/collective positions' if int(short.split(':')[1])<=5 else 'Anonymous Gemara') if pref=='b' else ('Anonymous Gemara with Rav Hisda answer' if short=='2a:5' else 'Anonymous Gemara quoting tannaitic material and analyzing it')
 add(f'{pref}u{i}','utterances',short,None,dict(textual_voice=voice,discourse_role='See separately anchored atomic claims, questions, attribution and edges',composition='composite' if len([r for r in R if r['layer'] in ['claims','questions'] and r['evidence'][0]['segment_id']==ref])>1 else 'atomic'))
add('rn1','structure','2a:8',None,dict(title='Baraita repetition and explanation crosses folio: final הא joins קמ״ל at 2b:1',primary=False,boundary='open_right',legacy_ids=[]),'editorial_inference')
edge('re11','2b:1','קמ"ל דניסן ר"ה למלכים ויום אחד בשנה חשוב שנה','rn1','rc7','continuation')

omissions=[
 ('bomit1','2a:1','Do not collapse onset and three endpoints into a single proposition or invent an explicit endpoint question; bq1 asks מאימתי.'),
 ('bomit2','2a:4','Keep sons’ report, conditional obligation and generalized midnight/dawn statement separate. Named attribution of the generalized tail is less certain than the explicit אמר להם answer.'),
 ('bomit3','2a:5','Keep burning and eating claims separate; the text’s rationale is a safeguard. Do not infer that burning itself was subjected to a midnight decree merely from proximity.'),
 ('bomit4','2a:8','The verse answer addresses textual presupposition and ordering; creation is an alternative ordering answer. Neither is a named amoraic dispute.'),
 ('bomit5','2a:10','Embedded blessing numbers are source claims in a quoted Mishnah, alongside an objection; preserve both contexts.'),
 ('romit1','2a:5','Rav Hisda is not Rav. No transmitter chain or Rav–Shmuel dispute is present.'),
 ('romit2','2a:8','הא at the page end is syntactically incomplete; continue through קמ״ל in 2b:1. Do not assert a closed argument boundary at the page break.'),
 ('romit3','2b:2','Prior Adar appointment differs from actual Nisan accession; hypothetical two-year counting is rejected, not a second accepted position.'),
 ('romit4','2b:5','Preserve beginning-versus-end-of-year distinction and rejection of restricting the rule to year end.'),
 ('romit5','2b:6','Both prior appointment and son-of-king conditions belong to the answer; neither may disappear. Same-Adar, same-Nisan and cross-month cases remain separate occurrences.')]
for id,ref,note in omissions:add(id,'reconciliation',ref,None,dict(finding=note),'editorial_inference')

out=dict(artifact_type='frozen_source_first_targeted_initial_review',reviewer_agent_id='/root/review_l01_l03',model_id=None,route='interactive_agent',status='AI provisional; not human verified; not eligible for ML',manifest_sha256=hashlib.sha256(manifest.read_bytes()).hexdigest(),sources=sources,core_refs=core,context_refs_read=[k for k in texts if k not in core],context_note='Original 2a and 2b of each tractate read. Context is not a complete semantic review of those pages. Rosh Hashanah 2b:7 introduces subsequent derivation; selected succession cohort resolves at 2b:6. Berakhot 2a:12 opens next wording inquiry.',scope_note='Targeted opening/risk cohorts only; neither full probability sample nor full-tractate completion.',independence=dict(producer_artifacts_read_before_freeze=False,exposure=['AGENTS.md','production schema.json','production PROTOCOL.md','pinned source_manifest.json','original source arrays','First 45 lines AGENT_HANDOFF.md as required by direct user AGENTS instruction; unrelated prior index/model overview, no current producer records']),findings=R,omission_pass=dict(performed=True,method='Reread every core segment against independently enumerated atomic claims, speech/quotation boundaries, anonymous reasoning, conditions and response directions; retain warnings as evidence-anchored reconciliation records.',limitations=['Utterances use segment-level composite envelopes with separately anchored components; not a claim of exhaustive utterance-span atomization.','No exhaustive outside-core chain or tractate conclusions.']))
ids={r['id'] for r in R};assert len(ids)==len(R)
for r in R:
 for e in r['evidence']:assert texts[e['segment_id']][e['start_char']:e['end_char']]==e['quote']
 if r['layer']=='edges':assert r['content']['source_id'] in ids and r['content']['target_id'] in ids
p=Path(__file__).with_name('l01_l03_initial.json');assert not p.exists();p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(len(R),hashlib.sha256(p.read_bytes()).hexdigest())

