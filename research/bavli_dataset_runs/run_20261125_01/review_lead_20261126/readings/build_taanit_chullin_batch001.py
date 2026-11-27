"""Source-only reader's explicit interpretations; immutable output, no producer input."""
import json, hashlib, pathlib, datetime
B=pathlib.Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def begin(t):
 global J,P,S,R,F,Q,E
 J=json.loads((B/'jobs'/('bavli_'+t+'.json')).read_text(encoding='utf8'))
 for x in [J['source'],J['frozen_plan'],J['original_source_schema'],*J['common_documents']]: assert sha(x['path'])==x['sha256'],x['path']
 P=json.loads(pathlib.Path(J['frozen_plan']['path']).read_text(encoding='utf8'))
 S=json.loads(pathlib.Path(J['source']['path']).read_text(encoding='utf8'))
 R={f"{J['tractate']} {i//2+1}{'a' if i%2==0 else 'b'}:{n+1}":v for i,a in enumerate(S['text']) for n,v in enumerate(a)}
 for x in P['review_blocks'][0]['spans']:
  v=S['text'][x['page_index']][x['segment_index']]; assert v==R[x['ref']];assert hashlib.sha256(v.encode()).hexdigest()==x['span_sha256_utf8']
 F=[];Q=[];E=[]
def ev(ref,quote=None):
 ref=J['tractate']+' '+ref if not ref.startswith(J['tractate']) else ref
 s=R[ref]; quote=s if quote is None else quote; start=s.index(quote)
 return {'ref':ref,'start_char':start,'end_char':start+len(quote),'quote':quote}
def claim(id,ref,text,holder='anonymous',conditions=(),status='asserted',quote=None,chain=(),uncertainty=()):
 F.append({'id':id,'kind':'atomic_claim','origin':'source_paraphrase','interpretation':text,'holder':holder,'transmission_chain':list(chain),'conditions':list(conditions),'local_status':status,'uncertainty':list(uncertainty),'evidence':[ev(ref,quote)]})
def context(id,refs,text,uncertainty=()):
 F.append({'id':id,'kind':'context_interpretation','origin':'source_paraphrase','interpretation':text,'uncertainty':list(uncertainty),'evidence':[ev(r) for r in refs]})
def question(id,refs,text,answers,comparability,status='locally answered'):
 Q.append({'id':id,'formulation':text,'origin':'explicit','answer_claim_ids':answers,'comparability':comparability,'local_status':status,'evidence':[ev(r) for r in refs]})
def edge(id,a,b,rel,refs,text):
 E.append({'id':id,'source_id':a,'target_id':b,'relation':rel,'explicitness':'source_explicit','interpretation':text,'evidence':[ev(r) for r in refs]})
def finish(t,context_refs,boundaries,notes):
 core=J['selected_blocks'][0]['core_refs'];core_set=set(core)
 for f in F+Q+E:f['cohort']='core' if any(x['ref'] in core_set for x in f['evidence']) else 'context_expansion'
 cs=[f for f in F if f['kind']=='atomic_claim' and f['cohort']=='core']
 qs=[q for q in Q if q['cohort']=='core']; es=[e for e in E if e['cohort']=='core']
 ids=[f['id'] for f in F+Q+E];assert len(ids)==len(set(ids))
 for q in Q: assert set(q['answer_claim_ids'])<=set(ids)
 for e in E:assert e['source_id'] in ids and e['target_id'] in ids
 checked=0
 for f in F+Q+E:
  for e in f['evidence']:
   assert R[e['ref']][e['start_char']:e['end_char']]==e['quote'];checked+=1
 out={'artifact_kind':'frozen_source_only_opening_block_reading','job_id':J['job_id'],'tractate':J['tractate'],'batch':'batch001','execution':{'agent_id':'/root/reader_taanit_chullin','route':'interactive_agent','model_id':None},'context_isolation':{'fork_turns':'none','producer_labels_exposed':False,'handoff':'Root read required handoff; reader excluded under current source-only isolation instruction because handoff includes annotated results.'},'producer_labels_exposed':False,'frozen_before_comparison':True,'source_sha256':J['source']['sha256'],'source_path':J['source']['path'],'plan_file_sha256':J['frozen_plan']['sha256'],'plan_sha256':P['plan_sha256'],'common_document_hashes':J['common_documents'],'source_metadata':{k:S[k] for k in ['versionTitle','versionSource','license']},'review_block_id':'block_000000','core_refs':core,'context_refs':[J['tractate']+' '+r for r in context_refs],'cohorts':{'roles':J['selected_blocks'][0]['roles'],'probability_core_segments':10 if 'probability_sample' in J['selected_blocks'][0]['roles'] else 0,'endpoint_core_segments':10,'overlap_core_segments':10 if 'probability_sample' in J['selected_blocks'][0]['roles'] else 0,'unique_core_segments':10,'context_segments':len(context_refs),'probability_inclusion_probability':J['selected_blocks'][0]['inclusion_probability'],'review_union_inclusion_probability':1.0},'boundaries':boundaries,'findings':F,'questions_and_answer_sets':Q,'supported_edges':E,'core_denominators':{'independently_found_atomic_claims':len(cs),'attributable_claims':sum(f['holder']!='anonymous' for f in cs),'condition_bearing_claims':sum(bool(f['conditions']) for f in cs),'questions':len(qs),'answer_sets':sum(bool(q['answer_claim_ids']) for q in qs),'supported_edges':len(es)},'denominator_definition':'Claims count independently enumerated atomic propositions, including asserted quotations, hypothetical challenges and rejected proposals; attributable means a named or explicitly quoted collective textual holder, excluding anonymous discourse. Condition-bearing counts explicit scope/if restrictions. Answer sets count questions with locally identified answer claims; no pairing by mere adjacency. Context findings do not inflate core denominators. Quoted verse propositions are counted only where independently used in argument. These operational boundaries remain contestable scholarly granularity.','limitations':['Opening block only; no producer comparison, no full-tractate verdict, no human scholarly certification.','Context read to resolve core interpretation; context findings are selective and do not claim complete context extraction.','No production schema validation claimed for this separate review artifact.'],'notes':notes,'validation':{'source_hash_verified':True,'frozen_plan_hash_verified':True,'common_documents_hash_verified':True,'original_source_schema_hash_verified':True,'core_span_hashes_verified':10,'evidence_spans_validated':checked,'offset_contract':'Original Unicode codepoint half-open; includes markup; no normalization','id_links_validated':True},'next_review_block':J['selected_blocks'][1],'frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 path=B/'readings'/(t+'_batch001.json');path.parent.mkdir(exist_ok=True)
 with path.open('x',encoding='utf8',newline='\n') as f:json.dump(out,f,ensure_ascii=False,indent=2);f.write('\n')
 h=sha(path)
 with path.with_suffix('.json.sha256').open('x',encoding='ascii') as f:f.write(h+'  '+path.name+'\n')
 print(t,h,json.dumps(out['core_denominators']), 'evidence',checked)

begin('taanit')
claim('t01','2a:1','Rain powers are mentioned beginning with the first festival day of Sukkot.','Rabbi Eliezer',['beginning of Sukkot'])
claim('t02','2a:1','Rain powers are mentioned beginning with the last festival day of Sukkot.','Rabbi Yehoshua',['last festival day of Sukkot'])
claim('t03','2a:2','Rain during the festival is a sign of curse.','Rabbi Yehoshua',['during Sukkot'])
claim('t04','2a:2','The proposed early practice is mention, not requesting rain.','Rabbi Eliezer',['early festival practice'],'qualification')
claim('t05','2a:2','The mention describes wind and rain in their proper season.','Rabbi Eliezer',['rain in its season'])
claim('t06','2a:2','On that reasoning mention should be permissible all year.','Rabbi Yehoshua',status='challenged consequence; not maintained independent ruling')
claim('t07','2a:3','Rain is requested only close to the rainy season.',conditions=['near rainy season'])
claim('t08','2a:3','On the final festival day the later prayer leader mentions rain.','Rabbi Yehuda',['last festival day; later leader'])
claim('t09','2a:3','On the final festival day the first prayer leader does not mention rain.','Rabbi Yehuda',['last festival day; first leader'])
claim('t10','2a:3','On the first Passover festival day the first prayer leader mentions rain.','Rabbi Yehuda',['first Passover day; first leader'])
claim('t11','2a:3','On the first Passover festival day the later prayer leader does not mention rain.','Rabbi Yehuda',['first Passover day; later leader'])
claim('t12','2a:4','The opening timing question depends on the earlier prayer Mishnah.',status='proposed then displaced at 2a:7')
claim('t13','2a:5','Rain powers are mentioned in the resurrection blessing.','quoted Mishnah',['prayer blessing placement'])
claim('t14','2a:5','Rain requests belong in the years blessing.','quoted Mishnah',['prayer blessing placement'])
claim('t15','2a:5','Havdalah belongs in the knowledge blessing.','quoted Mishnah',['prayer blessing placement'])
claim('t16','2a:7','Judgment concerning water occurs at the festival.','quoted Mishnah',['Sukkot'])
claim('t17','2a:7','The tractate begins from Rosh Hashanah discussion of judgment on water.',status='local replacement explanation')
claim('t18','2a:8','Rain is called powers because it descends with power.','Rabbi Yohanan')
claim('t19','2a:9','The shared word חקר connects rain to creation for the power derivation.','Rabbah bar Shila')
context('tc01',['2a:10'],'The scriptural chain quotes Job on unfathomable works, Isaiah on creation and Psalms on strength. It supports the preceding derivation, not an additional independently named speaker.')
context('tc02',['2b:3','2b:4','2b:5','2b:6'],'The day/night question for Eliezer is resolved by Rabbi Abbahu: derived from lulav. His access is given in two versions, received tradition or heard baraita; these are transmission alternatives, not rival positions on timing.')
context('tc03',['2b:8','2b:10','2b:11'],'Eliezer expressly permits mention throughout the year by analogy with resurrection; the editorial answer on Yehoshua’s behalf distinguishes resurrection, always timely, from out-of-season rain. The Mishnah rejoinder at 2a:2 must not become Yehoshua’s positive year-round ruling.')
context('tc04',['2b:9','3a:8','3a:9','3a:10','3a:11','3a:12'],'Yehuda’s report is identified by Rav Nahman bar Yitzhak as Rabbi Yehoshua ben Beteira, whose naming varies before/after ordination. Do not merge that authority with Rabbi Yehoshua of the Mishnah or Rabbi Yehuda ben Beteira. The anonymous Mishnah’s Rabbi Yehuda remains the stated holder there.')
context('tc05',['4a:14','4a:15','4a:16','4b:1'],'One version has Rava suggest Yehoshua on the assumption request and mention coincide and Abaye distinguish them, allowing Eliezer. Another version gives Rava the distinction. Preserve versions; attribution and discarded assumption differ.')
context('tc06',['4b:3','4b:4','4b:5','4b:6','4b:7','4b:8','4b:9','4b:10','4b:11'],'Contradictory end-of-Passover reports of Yehuda: Rav Hisda’s request/mention split is objected to by Ulla; Rav Yosef’s first leader gloss and Rabbah’s slaughter-time gloss are challenged. Local resolution twice favors Ulla’s two tannaim reporting Yehuda, not harmonization as a single unqualified view.')
context('tc07',['4b:12','4b:13','4b:14','4b:15','4b:16'],'Rabbi Asi transmits Rabbi Yohanan’s halacha as Yehuda. Initial challenge cites Rabbi Elazar for Rabban Gamliel; anonymous answers distinguish different authorities, then request versus mention, then place, finally Temple-present versus absent for the same locale. These are successive proposals, not all simultaneous established distinctions.')
context('tc08',['4b:17','4b:18','5a:1','5a:2'],'Two festival days: Rav initially starts at musaf, stops at minha/evening/morning then resumes musaf; Shmuel objects to making holy profane and includes minha before stopping. Rava and Rav Sheshet say never stop after beginning. Rav explicitly retracts, transmitted by Rav Hananel in Rav’s name; the concluding halakha is never to stop. The initial Rav–Shmuel disagreement is historical, not Rav’s final stance.')
question('tq1',['2a:1'], 'When does mention of rain begin?', ['t01','t02'],'Direct competing answers to same start-date question; later baraita refines Eliezer daytime and separates Yehoshua ben Beteira.')
question('tq2',['2a:2'],'Why mention rain during the cursed festival rain season?', ['t04','t05','t06'],'Mention/request distinction answers objection; year-round consequence is Yehoshua’s counterargument.', 'answered and counterchallenged')
question('tq3',['2a:4','2a:6'],'Where does the opening timing question take its starting point, and why is it here?', ['t12','t17'],'Prayer-Mishnah premise displaced by Rosh Hashanah linkage.')
question('tq4',['2a:8'],'Why call rainfall powers?', ['t18'],'Lexical explanation, not disagreement.')
question('tq5',['2a:9'],'How do the verses imply power?', ['t19'],'Derivation through creation, supported by following verse chain.')
edge('te1','t03','t01','objection',['2a:2'],'Yehoshua challenges festival mention by cursed rain.')
edge('te2','t04','t03','answer',['2a:2'],'Eliezer distinguishes mention from request.')
edge('te3','t06','t04','objection',['2a:2'],'Yehoshua tests the distinction by all-year consequence.')
edge('te4','t17','t12','correction',['2a:6','2a:7'],'Anonymous challenge leads to replacement tractate-context explanation.')
edge('te5','t16','t17','support',['2a:7'],'Water judgment supplies topical link.')
edge('te6','t18','tq4','answer',['2a:8'],'Yohanan explains the word powers.')
edge('te7','t19','t18','support',['2a:9','2a:10'],'Rabbah bar Shila and scriptural chain substantiate power.')
tctx=[]
for ref in R:
 if ref in J['selected_blocks'][0]['core_refs']:continue
 page=ref.split()[1].split(':')[0]
 if page in ['2a','2b','3a','3b','4a','4b'] or ref in ['Taanit 5a:1','Taanit 5a:2']:tctx.append(ref.split(' ',1)[1])
finish('taanit',tctx,[{'core':'2a:1–3','unit':'Mishnah: seasonal mention and request','continuations':'2b:3–3a:12; 4a:14–5a:2'},{'core':'2a:4–7','unit':'Anonymous tractate-order explanation','closure':'2a:7'},{'core':'2a:8–10','unit':'Meaning and scriptural derivation of rain powers','closure':'2a:10'}],['Incidental adjacent context was read but is not comprehensively extracted. No additional core claims inferred merely from later material.','Counts distinguish Rabbah bar Shila, Rabbah, Rava, Rav, Rav Yosef and other named speakers.'])

begin('chullin')
claim('c01','2a:1','The included class may slaughter.','anonymous Mishnah',['subject to stated exclusions'],'asserted; scope disputed by later interpretations')
claim('c02','2a:1','Slaughter of the included class is valid.','anonymous Mishnah',['subject to stated exclusions'])
claim('c03','2a:1','A deaf-mute is excluded from unsupervised slaughter.','anonymous Mishnah',['deaf-mute; without observers'])
claim('c04','2a:1','A person lacking legal mental competence is excluded from unsupervised slaughter.','anonymous Mishnah',['שוטה; without observers'])
claim('c05','2a:1','A minor is excluded from unsupervised slaughter.','anonymous Mishnah',['minor; without observers'])
claim('c06','2a:1','The exclusions reflect concern they will spoil slaughter.','anonymous Mishnah',['excluded slaughterers'])
claim('c07','2a:1','Slaughter is valid when others observe the act.','anonymous Mishnah',['others observing'],'asserted; antecedent of וכולן disputed in interpretation',uncertainty=['Do not silently fix וכולן to excluded three: ensuing amoraic readings explicitly dispute its syntactic attachment.'])
claim('c08','2a:2','הכל שוחטין is read as permission in advance.',status='initial reading defended at 2b:5')
claim('c09','2a:2','שחיטתן כשרה is read as validity after the act.',status='initial reading retained')
claim('c10','2a:3','Both men and women fall under the formula הכל ממירין.','quoted Mishnah')
claim('c11','2a:3','Substitution of a sacrificial animal is prohibited.','quoted Torah',status='asserted as Rav Aha son of Rava’s counterexample')
claim('c12','2a:4','A person is not authorized to substitute.','quoted explanation')
claim('c13','2a:4','If substitution was performed, it takes effect.','quoted explanation',['substitution already performed'])
claim('c14','2a:4','The person who substitutes receives forty lashes.','quoted explanation',['substitution performed'])
claim('c15','2a:5','All may be valuation declarants.','quoted Mishnah')
claim('c16','2a:5','All may be subjects of valuations.','quoted Mishnah')
claim('c17','2a:5','All may vow monetary dedication.','quoted Mishnah')
claim('c18','2a:5','All may be subjects of monetary dedication vows.','quoted Mishnah')
claim('c19','2a:5','Refraining from vows incurs no sin.','quoted Torah',['refrains from vows'])
claim('c20','2a:6','Not vowing is better than vowing and not paying.','quoted Ecclesiastes',['vow unpaid'])
claim('c21','2a:6','Not vowing at all is best.','Rabbi Meir')
claim('c22','2a:6','Vowing and paying is best.','Rabbi Yehuda',['vow fulfilled; contextual restriction to הרי זו'])
claim('c23','2a:6','Even Yehuda’s approval is limited to designating this object (הרי זו).',conditions=['הרי זו'],status='anonymous qualification of Yehuda')
claim('c24','2b:1','Yehuda’s approval does not extend to undertaking a personal obligation (הרי עלי).',conditions=['הרי עלי'],status='anonymous qualification; continues previous segment')
claim('c25','2b:2','All are obligated in sukkah.','quoted Mishnah')
claim('c26','2b:2','All are obligated in tzitzit.','quoted Mishnah')
claim('c27','2b:3','The lexical challenge excludes formulations saying חייבין.',status='anonymous reply; exact interlocutor not marked')
claim('c28','2b:3','The cited semikha formula includes men and women.','quoted formula',uncertainty=['Quote exactly as this edition; no external correction of wording.'])
claim('c29','2b:3','Laying hands is positively commanded.','quoted Torah',status='counterexample to universal after-the-fact reading')
claim('c30','2b:4','Some הכל formulations permit or prescribe action in advance.')
claim('c31','2b:4','Some הכל formulations describe only validity after the fact.')
claim('c32','2b:4','The slaughter opening could itself be read after the fact, avoiding the alleged tension.',status='hypothetical challenge; answered at 2b:5')
context('cc01',['2b:5'],'The reply explains that redundant after-the-fact clauses would be unnecessary: שחיטתן כשרה therefore indicates that the first clause is in advance. This closes the core lexical question without the false general rule that every הכל is permission in advance.')
context('cc02',['2b:6','2b:7','2b:8','2b:9','2b:10','2b:11','2b:12','2b:13','2b:14','3a:1','3a:2'],'Rabbah bar Ulla reads a tamei slaughterer: ordinary meat maintained to sacred purity is treated like sacred, using a long knife; for actual offerings no initial slaughter lest contact occur, but a post-act claim of no contact suffices. Others observing substitutes when the slaughterer is absent for inquiry. The duplicate Mishnah is explained in two directions. Sheretz impurity or corpse impurity with a checked reed shard answers knife impurity. Do not confuse Rabbah bar Ulla with Rav.')
context('cc03',['3a:3','3a:4','3a:5','3a:6','3a:7','3a:8','3a:9','3a:10','3a:11','3a:12'],'Abaye reads a Samaritan under continuous Jewish supervision; intermittent entry is insufficient in advance, with post-act eating test. Rava initially objects by a case whose wording only shows post-fact permission, then cites an explicit intermittent-watch allowance and offers the more lenient intermittent-supervision reading. Both readings leave וכולן with קשיא; do not label either an unqualified final resolution.')
context('cc04',['3a:13','3b:1','3b:2','3b:3'],'Rav Ashi reads an Israelite apostate who eats neveilah for appetite, invoking Rava: checked knife first allows slaughter, otherwise subsequent knife inspection controls permission. The וכולן clause remains קשיא because observing slaughter cannot establish a missing knife’s quality.')
context('cc05',['3b:4','3b:5','3b:6','3b:7'],'First Ravina version: known competence suffices without established resistance to fainting. Unknown competence precludes initial slaughter; after the act examination may validate. Observers replace unavailable post-act examination when the person is absent.')
context('cc06',['3b:8','3b:9','3b:10'],'Second Ravina version: established non-fainting suffices even without known expertise. Prior two/three observed slaughters establish this; otherwise no initial permission, with post-act assurance of no fainting sufficient. Observers address the absent slaughterer. Keep this alternative separate from Ravina’s first version.')
context('cc07',['3b:11','3b:12','3b:13','3b:14','3b:15'],'The comparison explains why Ravina/Rabbah bar Ulla reject the other readings (וכולן difficulty), why others reject Rabbah bar Ulla’s redundancy or sacred-purity premise, and why others reject each Ravina version (most slaughterers expert; no fainting concern). These are explanations of interpretive choices, not one unanimous ruling.')
context('cc08',['3b:16','3b:17','3b:18','3b:19'],'Rava rejects Abaye per his objection; Abaye distinguishes contact. Rav Ashi treats Samaritans as lion-converts. Abaye rejects Rava’s apostate statement. Rava’s Samaritan interpretation is explicitly only according to Abaye’s premises, not Rava’s own belief; preserve לדבריו דאביי ... וליה לא סבירא ליה.')
question('cq1',['2a:2','2a:3','2a:4','2a:5','2b:2','2b:3','2b:4'],'Does הכל uniformly mean permission in advance?', ['c30','c31'],'Counterexamples address a lexical generalization, not direct legal disputes between adjoining authorities.')
question('cq2',['2a:6'],'Which vow practice is preferable?', ['c21','c22'],'Meir and Yehuda compete on ideal practice, but anonymous limitation restricts Yehuda to הרי זו; do not universalize to הרי עלי.')
question('cq3',['2b:4','2b:5'],'Why read this slaughter הכל as in advance?', ['c08','c09','c32'],'Possible post-act reading challenged by redundancy; final lexical answer is in 2b:5.')
edge('ce1','c11','c08','objection',['2a:3'],'Substitution counters inference from every הכל; c08 alone is not refuted.')
edge('ce2','c12','cq1','answer',['2a:4'],'Substitution text explicitly disallows initial action.')
edge('ce3','c19','cq1','objection',['2a:5'],'Vow text supplies further counterexample to universal initial permission.')
edge('ce4','c23','c22','qualification',['2a:6'],'Approval limited to הרי זו.')
edge('ce5','c24','c22','qualification',['2a:6','2b:1'],'Personal-obligation vows excluded.')
edge('ce6','c25','cq1','objection',['2b:2'],'Positive obligation counters universal after-the-fact reading.')
edge('ce7','c27','ce6','answer',['2b:3'],'Reply excludes חייבין expressions from the challenge.')
edge('ce8','c29','cq1','objection',['2b:3'],'Semikha command supplies non-חייבין counterexample.')
edge('ce9','c30','cq1','local_resolution',['2b:4'],'The formula admits in-advance usage.')
edge('ce10','c31','cq1','local_resolution',['2b:4'],'The formula also admits post-act usage.')
edge('ce11','c32','c08','objection',['2b:4'],'Permission cannot be inferred from הכל alone.')
edge('ce12','cc01','c32','answer',['2b:5'],'Redundancy between first and second clauses resolves local reading.')
cctx=[]
for ref in R:
 page=ref.split()[1].split(':')[0];n=int(ref.split(':')[1])
 if ref not in J['selected_blocks'][0]['core_refs'] and (page in ['2b','3a'] or page=='3b' and n<=19):cctx.append(ref.split(' ',1)[1])
finish('chullin',cctx,[{'core':'2a:1','unit':'Mishnah slaughter permission and validity','interpretive_continuation':'2b:6–3b:19'},{'core':'2a:2–2b:4','unit':'Lexical הכל challenge and vow citation','closure':'2b:5'}],['Named challenge speaker at 2a:3 is Rav Aha son of Rava addressing Rav Ashi. Later unlabeled dialogue turns are left anonymous rather than mechanically assigned.','The anonymous Mishnah and explicitly quoted authorities count as attributable textual holders in the stated operational denominator; they are not named amoraic persons.','Comparability is constrained by priori/posteriori validity, supervision, knife knowledge, competence, fainting and alternative reports; adjacent citations alone are not disputes.'])
