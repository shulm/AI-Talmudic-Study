"""NONBLIND manual semantic comparison; no production mutation or auto semantic scoring."""
import json,hashlib,collections
from pathlib import Path
D=Path(__file__).parent;R=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126');P=D.parent.parent/'bavli_taanit'
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p):return dict(path=str(p),sha256=sha(p))
def canon(x):return hashlib.sha256((json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
def write(name,data):
 p=D/name
 with p.open('x',encoding='utf8') as f:json.dump(data,f,ensure_ascii=False,indent=2);f.write('\n')
 with Path(str(p)+'.sha256').open('x') as f:f.write(sha(p)+'  '+p.name+'\n')
 return bind(p)
rd=read(D.parent/'taanit_delegated055.json');j=read(R/'jobs/bavli_taanit_delegated055.json');sp=P/'snapshots/ac7c9ec619b963f05c6dc32c42e16511808f6256dea63937f5b5f8e5e96e5cf4.json';s=read(sp);inv=read(P/'source_inventory.json');bi={r['id']:r for r in inv};br={r['ref']:r for r in inv};core=set(j['core_refs']);ri={r['id']:r for r in rd['records']};pi={r['id']:r for r in s['records'] if r['release_state']=='valid'};cr=[r for r in rd['records'] if any(e['segment_id'] in core for e in r['evidence'])];active=[r for r in pi.values() if any(bi[e['segment_id']]['ref'] in core for e in r['evidence'])]
pre=read(D/'preflight062.json');assert pre['result']=='PASS' and pre['exact_readonly_replay']
for b in pre['bindings']+pre['proposal_bindings']:assert sha(b['path'])==b['sha256']
extra=[(D.parent/'validation_ta055_initialfreeze_20261127.json','14fe9b22cc6ccff26486c71a34ff953461a87c59faef0dacbc54cf126da41890'),(D.parent/'author_validate055.py','e74f592fd93e1b9b9f268d9fcd910373b05b04abf91b3d9b99e94c84dc703243')]
for p,h in extra:assert sha(p)==h
# Manual reading-to-producer alignment, independent of textual similarity heuristics.
raw='''0009 008.vows.rule
0015 008.zevid.olives
0023 008.gifts.leket
0028 008.gifts.grapes
0032 008.gifts.olives
0040 008.nemushot.yohanan.tf013
0045 008.nemushot.lakish
0050 008.papa.paths
0055 008.paths.rule
0060 008.nahman.burn
0068 008.straw.rule
0077 008.animal.available
0082 008.animal.exhausted
0091 009.revia.name
0096 009.rain.spouse
0101 009.first.amount
0105 009.second.amount
0109 009.jar.notwithheld
0113 009.before.notwithheld
0117 009.abaye.evening
0122 009.abaye.morning
0144 010.scholar.fit.dew
0126 009.morning.clouds
0149 010.scholar.unfit.rain
0154 010.lishmah.life
0158 010.nonlishmah.death
0162 010.arifah.killing
0169 010.zeira.weak
0182 010.fit.tree
0187 010.unfit.tree
0196 010.iron.scholars
0200 010.iron.scholars
0209 010.fire.solitary
0213 010.fire.solitary
0222 010.solitary.sword
0227 010.solitary.foolish
0232 010.solitary.sin
0236 010.sin.proof1
0240 010.sin.proof2
0249 010.small.sharpens
0253 010.small.sharpens
0259 010.hanina.learning
0263 010.hanina.learning
0267 010.hanina.learning
0275 010.water.fit
0280 010.water.unfit
0288 010.springs.fit
0293 010.springs.unfit
0301 010.water.humility
0305 010.water.humility
0314 010.vessels.humility
0318 010.vessels.humility
0324 010.daughter.insult
0333 010.gold.silver.advice
0337 010.wine.sours
0340 010.wine.sours
0343 010.advice.identity.q
0349 010.daughter.identifies
0353 010.emperor.why.q
0359 010.yehoshua.retort
0368 010.ugly.morelearned
0373 010.attention.liquids
0377 010.attention.liquids
0383 011.creation.rain
0387 011.creation.singular
0392 011.salvation.grows
0396 011.forgiveness.rain
0400 011.zeiri.forgiveness
0406 011.destruction.drought
0410 011.zeiri.destruction'''
cm={'ta055.claims.'+a:'ta.resume'+b for a,b in (line.split() for line in raw.splitlines())};assert set(cm)=={r['id'] for r in cr if r['layer']=='claims'}
qraw='''0020 008.gifts.threshold.q
0037 008.nemushot.q
0065 008.straw.until.q
0074 008.seventh.reason.q
0088 009.revia.name.q
0141 010.rain.dew.q
0176 010.human.tree.q
0179 010.tree.verses.q
0193 010.iron.q
0206 010.fire.q
0219 010.badim.q
0246 010.wood.q
0272 010.water.approach.q
0285 010.springs.q
0298 010.water.humility.q
0311 010.three.liquids.q
0327 010.wine.vessel.q
0330 010.wine.alternative.q
0346 010.advice.identity.q
0356 010.emperor.why.q
0364 010.handsome.scholars.q'''
qm={'ta055.questions.'+a:'ta.resume'+b for a,b in (line.split() for line in qraw.splitlines())};assert set(qm)=={r['id'] for r in cr if r['layer']=='questions'}
mapping=cm|qm|{'ta055.claims.0004':'ta.resume008.zeira.vows','ta055.questions.0001':'ta.resume008.second.use.q'}
proofmap={'0415':'008.animal.verse','0419':'009.isaiah.birth','0422':'009.hosea.clouds','0425':'010.life.verse.tree','0428':'010.life.verse.healing','0431':'010.life.verse.finding','0434':'010.arifah.killing','0437':'010.arifah.killing','0440':'010.tree.verses.q','0444':'010.fire.q','0447':'010.solitary.foolish','0450':'010.wood.q','0453':'010.water.humility.q','0456':'010.liquids.verses','0459':'011.creation.verse','0463':'011.salvation.verse','0466':'011.forgiveness.psalm','0469':'011.destruction.job'}
mapping.update({'ta055.utterances.'+a:'ta.resume'+b for a,b in proofmap.items()})
assert all(v in pi for v in mapping.values())
def evidence(ref,quote):
 t=br[ref]['text'];a=t.index(quote);return dict(ref=ref,segment_id=br[ref]['id'],start_char=a,end_char=a+len(quote),quote=quote)
issues=[]
def issue(key,category,ref,quote,reader_ids,producer_ids,finding,action,severity='medium'):
 issues.append(dict(id=key,category=category,severity=severity,evidence=[evidence(ref,quote)],reader_ids=reader_ids,producer_ids=producer_ids,reader_original=[ri[i] for i in reader_ids],producer_original=[pi[i] for i in producer_ids],finding=finding,proposed_action=action,resolution_state='frozen_finding_no_mutation'))
analogy_rows=[('7a:8','0205','010.iron.scholars','מה ברזל זה אחד מחדד את חבירו אף שני תלמידי חכמים מחדדין זה את זה בהלכה'),('7a:9','0218','010.fire.solitary','מה אש אינו דולק יחידי אף דברי תורה אין מתקיימין ביחידי'),('7a:12','0258','010.small.sharpens','מה עץ קטן מדליק את הגדול אף תלמידי חכמים קטנים מחדדים את הגדולים'),('7a:15','0310','010.water.humility','מה מים מניחין מקום גבוה והולכין למקום נמוך אף דברי תורה אין מתקיימין אלא במי שדעתו שפלה'),('7a:16','0323','010.vessels.humility','מה שלשה משקין הללו אין מתקיימין אלא בפחות שבכלים אף דברי תורה אין מתקיימין אלא במי שדעתו שפלה'),('7b:1','0382','010.attention.liquids','מה שלשה משקין הללו אין נפסלין אלא בהיסח הדעת אף דברי תורה אין משתכחין אלא בהיסח הדעת')]
for n,(ref,rid,pid,quote) in enumerate(analogy_rows,1):
 issue('TA062-GRAPH-A'+str(n),'confirmed_producer_typed_relation_omission','Taanit '+ref,quote,['ta055.edges.'+rid],['ta.resume'+pid],'The producer preserves the analogy in a composite proposition but has no distinct premise/conclusion endpoints and no typed analogy edge for this source-explicit מה/אף relation. This is not a missing prose proposition.','Add separate source-anchored premise/conclusion nodes and analogy edge through additive revisions; recheck holder and dependent answer edge.')
for n,(ref,rid,pid,quote) in enumerate([('7a:9','0446','010.fire.q',"שנאמר (ירמיהו כג, כט) הלא כה דברי כאש נאם ה'"),('7a:10','0449','010.solitary.foolish','שנאמר ונואלו'),('7a:12','0452','010.wood.q','שנאמר (משלי ג, יח) עץ חיים היא למחזיקים בה'),('7a:15','0455','010.water.humility.q','דכתיב הוי כל צמא לכו למים')],1):
 issue('TA062-GRAPH-B'+str(n),'confirmed_producer_typed_proof_basis_omission','Taanit '+ref,quote,['ta055.edges.'+rid],['ta.resume'+pid],'Quoted basis survives as evidence attached to a question or conclusion, but no typed quoted-authority/basis node and support relation represent this proof step. For metaphor passages the verse establishes the comparison basis, not by itself the downstream pedagogical conclusion.','Add a quoted-source basis and scoped support edge; retain the reader original while refining its direct-to-conclusion target where necessary.')
issue('TA062-ENDPOINT','confirmed_producer_relation_endpoint_error','Taanit 7a:17','כדאמרה ליה ברתיה דקיסר',['ta055.edges.0363'],['ta.resume010.narrative.illustrates','ta.resume010.daughter.insult','ta.resume010.vessels.humility'],'כדאמרה introduces a narrative illustration. The daughter’s taunt alone is not the full premise showing lowly vessels preserve contents; its current edge endpoint narrows the story to a taunt and labels that relation source_explicit. The reader’s souring-to-vessels link is explicitly editorial and better scoped.','Anchor illustration to the complete narrative or the wine outcome with appropriate editorial scope; preserve taunt as narrated speech.')
issue('TA062-ONLY-VESSELS','confirmed_producer_condition_scope_loss','Taanit 7a:16','מה שלשה משקין הללו אין מתקיימין אלא בפחות שבכלים',['ta055.claims.0314'],['ta.resume010.vessels.humility'],'The producer says the liquids keep in lowly vessels, losing the premise’s only/אין...אלא restriction. It retains only for the Torah conclusion. A condition list saying humble disposition does not restore the premise quantifier.','Preserve the premise as liquids keep only in lowly vessels, explicitly within this analogy rather than empirical certification.')
issue('TA062-ONLY-ATTENTION','confirmed_producer_condition_scope_loss','Taanit 7b:1','מה שלשה משקין הללו אין נפסלין אלא בהיסח הדעת אף דברי תורה אין משתכחין אלא בהיסח הדעת',['ta055.claims.0373','ta055.claims.0377'],['ta.resume010.attention.liquids'],'Producer wording through inattention preserves a causal association but loses only through inattention on both premise and conclusion. The untyped inattention condition does not state necessity.','Retain both necessary-condition restrictions; keep the anonymous דבר אחר alternative and do not assign it uniquely to Oshaya.')
issue('TA062-READER-GLOSS','reader_unverified_lexical_expansion','Taanit 6b:3','סבי דאזלי אתיגרא',['ta055.claims.0040'],['ta.resume008.nemushot.yohanan.tf013'],'Reader proposition asserts walking with support while its uncertainty admits the gloss is not established. Producer historical revision retains אתיגרא without asserting the gloss. No new lexical source was consulted; this is not adjudication of the correct dictionary translation.','For standalone use retain the Aramaic or mark the gloss as an unresolved editorial possibility. No mutation to frozen reading.','low')
issue('TA062-READER-SOIL','reader_unmarked_explanatory_expansion','Taanit 6b:8','שניה כדי לגוף בה פי חבית',['ta055.claims.0105'],['ta.resume009.second.amount'],'Reader adds resulting soil without a local uncertainty note; producer explicitly notes source does not give the soil/moisture gloss. Plausible explanation is not an exact source statement.','Mark the soil gloss editorial or use the literal sealing measure; retain original reading.','low')
issue('TA062-OBJECTION-SCOPE','unresolved_editorial_relation_scope','Taanit 7a:18','והא איכא שפירי דגמירי',['ta055.edges.0367'],['ta.resume010.handsome.scholars.q','ta.resume010.vessels.humility'],'Reader targets humility proposition with the handsome-learners objection. Local challenge directly addresses the physical ugliness implication of the narrative analogy; physical beauty is not identical to pride. Reader correctly labels editorial reconstruction, and no unique speaker is asserted by producer.','Keep objection attested but scope target to the narrative implication or preserve ambiguity; do not force a definitive objection-to-humility edge.','low')
# Every independent core edge receives a typed-endpoint assessment, including reasonable consolidations.
edge_rows=[];pedges=[r for r in pi.values() if r['layer']=='edges']
issue_edges={i for x in issues for i in x['reader_ids'] if '.edges.' in i}
for r in cr:
 if r['layer']!='edges':continue
 c=r['content'];a=mapping.get(c['source_id']);b=mapping.get(c['target_id']);matches=[p['id'] for p in pedges if p['content']['source_id']==a and p['content']['target_id']==b and p['content']['relation']==c['relation']]
 if matches:status='typed_correspondence'
 elif r['id'] in issue_edges:status='see_discrepancy_ledger'
 elif r['id']=='ta055.edges.0081':status='reasonable_answer_inventory_granularity_positive_branch_is_preserved_but_only_exhaustion_linked'
 elif r['id'] in ['ta055.edges.0436','ta055.edges.0439']:status='reasonable_consolidation_arifah_derivation_and_proof_verses_in_one_node'
 elif r['id'] in ['ta055.edges.0442','ta055.edges.0443']:status='proof_basis_in_question_not_a_distinct_typed_support_edge_restricted_graph_use'
 elif r['id']=='ta055.edges.0458':status='reader_direct_to_conclusion_is_overcompressed_producer_basis_to_comparison_question_is_reasonable'
 elif r['id']=='ta055.edges.0462':status='reasonable_transitive_support_via_singular_inference'
 else:status='unresolved_endpoint_granularity_no_exact_typed_correspondence'
 edge_rows.append(dict(reader_id=r['id'],reader_edge=c,reader_evidence=r['evidence'],mapped_source=a,mapped_target=b,producer_edge_ids=matches,assessment=status))
# Distinguish inventories and condition cases from forced mutually-exclusive choices.
question_rows=[]
for rid,pid in qm.items():
 ref=ri[rid]['evidence'][0]['segment_id'];pe=[p for p in pedges if p['content']['relation']=='answer' and p['content']['target_id']==pid];re=[r for r in rd['records'] if r['layer']=='edges' and r['content']['relation']=='answer' and r['content']['target_id']==rid]
 assessment='Local explanatory or narrative response inventory; no scholar-choice eligibility.'
 if ref=='Taanit 6b:3':assessment='Two named definitions answer same question; no local choice or winner; lexical gloss unresolved.'
 if ref in ['Taanit 7a:4','Taanit 7a:7','Taanit 7a:13','Taanit 7a:14']:assessment='Complementary conditional cases, not opposing scholars or mutually-exclusive same-condition answers.'
 if ref=='Taanit 7a:16':assessment='Humility and anonymous דבר אחר inattention answer common comparison question; alternatives not declared mutually exclusive; latter quantifier defect applies.'
 if ref=='Taanit 7a:17' and rid.endswith('0327'):assessment='Rhetorical vessel question followed by counterquestion; no forced yes/no answer inventory.'
 question_rows.append(dict(reader_id=rid,producer_id=pid,ref=ref,reader_answer_ids=[r['content']['source_id'] for r in re],producer_answer_ids=[r['content']['source_id'] for r in pe],reader_status=ri[rid]['content']['answer_set_status'],producer_status=pi[pid]['content']['answer_set_status'],assessment=assessment,comparable_exhaustive_choice_certified=False))
claim_rows=[]
for rid,pid in cm.items():
 ps=[r for r in pi.values() if r['layer']=='positions' and r['content']['claim_id']==pid];ats=[r for r in pi.values() if r['layer']=='attributions' and r['content']['scope']==pid]
 issues_here=[x['id'] for x in issues if rid in x['reader_ids'] or pid in x['producer_ids']]
 claim_rows.append(dict(reader_id=rid,producer_ids=[pid],reader_evidence=ri[rid]['evidence'],reader_claim=ri[rid]['content'],producer_content=pi[pid]['content'],producer_layer=pi[pid]['layer'],producer_position_ids=[r['id'] for r in ps],producer_attribution_ids=[r['id'] for r in ats],assessment='substance_present_in_producer; typed graph/quantifier/reader qualifications apply' if issues_here else 'substance_present; bundling allowed without claiming atomic equivalence',exceptions=issues_here))
named=[];ambiguous=[];anonymous=[]
for r in cr:
 if r['layer']!='claims':continue
 attrs=[x for x in cr if x['layer']=='attributions' and x['content']['scope']==r['content']['proposition']]
 if any(x['content']['role']=='position_holder' for x in attrs):
  (ambiguous if r['id'] in ['ta055.claims.0196','ta055.claims.0200'] else named).append(r['id'])
 else:anonymous.append(r['id'])
condition_ids=[r['id'] for r in cr if r['layer']=='claims' and r['content']['conditions']];source_condition_ids=condition_ids+['ta055.claims.0314','ta055.claims.0373']
assert len(condition_ids)==32 and len(set(source_condition_ids))==34
pcov={l:len({bi[c['segment_id']]['ref'] for c in s['coverage'] if c['layer']==l and c['extraction_state']=='completed'}&core) for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']};assert set(pcov.values())=={30}
notes={
'6b:1':'Anonymous Mishnah endpoint; both unpunctuated formulations preserved; inherited Zeira application in6a13 is separate.',
'6b:2':'All three agricultural endpoints preserved; Zevid application distinct from quoted Mishnah. Positive noun list not missing claims.',
'6b:3':'Yohanan and Resh Lakish same-question definitions, no resolution; reader gloss restricted, producer tf013 preserved.',
'6b:4':'Pappa application versus anonymous אמר מר; private/permissive gloss not a new halakhic rule.',
'6b:5':'Nahman bar Yitzhak application, straw benefit/burning rule and endpoint preserved.',
'6b:6':'Both availability and exhaustion conditions preserved. Single producer answer edge from exhaustion is inventory granularity; positive branch also present. Source-explicit support and reader editorial support differ in explicitness, not conclusion.',
'6b:7':'Abbahu etymology, Yehuda metaphor, Isaiah authority distinguished; no Rav himself substitution.',
'6b:8':'Both measures and Hisda consequence retained; reader soil gloss marked for qualification.',
'6b:9':'General local stage retained; Abaye restriction linked, no silently normalized final rule.',
'6b:10':'Evening/morning contrast retained;6b11 objection and anonymous cloud reconciliation inspected, restrict standalone morning claim.',
'7a:4':'Rava two conditions, not competing positions; imagery not a practical sanction.',
'7a:5':'Benaah baraita and both motive conditions retained. Three life proofs separate; arifah combines death and calf proof, reasonable prose granularity.',
'7a:6':'Yirmiyah requests and Zeira weakness retained. Zeira transmitter, Yohanan authority; producer explicit chains correct.',
'7a:7':'Inherited Yohanan conditions preserved; two questions related. Scripture basis embedded in question; direct proof edges not separately represented.',
'7a:8':'Attribution parenthesis unresolved on both sides. Bundled analogy requires typed endpoint repair.',
'7a:9':'Rabbah bar bar Hanah identified; fire analogy and scriptural basis graph deficiencies, source substance present.',
'7a:10':'Yosi bar Hanina, sword and foolishness distinct; quoted ונואלו proof basis graph absent.',
'7a:11':'Sin inherited; two anonymous proof variants not competing claims or retraction.',
'7a:12':'Nahman bar Yitzhak versus Hanina testimony preserved; three comparisons bundled reasonably. Analogy and verse-basis graph gaps.',
'7a:13':'Hanina bar Pappa, worthy/unworthy cases preserved; no false neighboring dispute.',
'7a:14':'Hanina bar Hama distinguished; outward/retained teaching conditions preserved.',
'7a:15':'Hanina bar Idi and humility necessary condition preserved. Water analogy and verse-basis graph gaps.',
'7a:16':'Oshaya attribution preserved; three liquids verse basis preserved, premise-only quantifier lost and analogy edge absent.',
'7a:17':'Narrative taunt, questions, ironic advice preserved; illustration edge endpoint too narrow.',
'7a:18':'Relaying/souring bundled; report and summons embedded in question formulations (not substantive omissions). Reader objection-to-humility target uncertain; reply continued on7b1.',
'7b:1':'Counterfactual and anonymous alternative separated; only-through-inattention quantifiers lost in producer paraphrase, typed analogy absent.',
'7b:2':'Hama bar Hanina comparison; singular inference and verse support retained, no imported contradiction with7a2-3.',
'7b:3':'Oshaya and Tanhum bar Hanilai distinct, salvation and forgiveness claims separate; only-when condition preserved.',
'7b:4':'Zeiri speaker, Ravina recipient; alternate proof not rejection; historical place identity unresolved.',
'7b:5':'Tanhum son of Hiyya of Kefar Akko distinct, euphemism and necessary condition retained; Zeiri alternate proof, no local choice/repeal in continuation.'}
layer_notes={'structure':'Exact primary partition passes; producer multi-segment units versus reader per-segment boundaries are reasonable granularity. Closed units can have cross-unit relations.','utterances':'Narrative and quoted voices checked; bundling of proofs/analogies means typed graph inventory is not certified complete.','claims':'All70 reader core units have semantic counterparts; quantified scope losses in two producer composite records remain. No claim-level completeness percentage.','attributions':'Named holder/transmitter distinctions checked; no confirmed false named attribution. Parenthetical7a8 and anonymous7b1 remain unresolved. Quoted basis representation gaps follow graph ledger.','questions':'All21 core questions mapped; inventories inspected without turning conditional cases or alternative proofs into forced scholar choices.','positions':'Conditions and local stages checked; generic local labels require linked context6b11 and narrative reading. Null question_id is schema-valid because answer edges encode association.','edges':'75 source-reader core edges independently checked; six explicit analogy omissions, four proof-basis omissions and one producer narrative endpoint defect. Other endpoint granularities are preserved separately.','reconciliation':'Completed cells are producer claims of a pass, not accuracy certification; comparator source-based omission review found targeted defects.'}
layer_rows=[dict(ref=ref,layer=l,reviewed=True,producer_extraction_completed=True,assessment=layer_notes[l],core_note=notes[ref.split(' ',1)[1]],finding_ids=[x['id'] for x in issues if any(e['ref']==ref for e in x['evidence'])]) for ref in j['core_refs'] for l in pcov]
assert len(layer_rows)==240
den=dict(core_claim_units=70,claim_units_with_named_or_identifiable_narrative_speaker=len(named),named_claim_ids=named,ambiguous_named_claim_units=len(ambiguous),ambiguous_named_claim_ids=ambiguous,anonymous_or_narrator_claim_units=len(anonymous),anonymous_claim_ids=anonymous,reader_condition_field_units=32,source_derived_condition_bearing_units=34,condition_bearing_ids=source_condition_ids,core_questions=21,proposed_core_answer_inventories=21,core_argument_edges=75,context_claim_units=2,context_questions=2,context_edges=4,whole_reader_records=503,core_reader_records=len(cr),atomic_exhaustiveness_certified=False,definition='Claim units are frozen reader units, including narrative facts and analogy premises. Attribution counts distinguish identifiable voices from unresolved names and anonymous/narrator. Condition denominator adds two source-explicit only clauses absent from reader condition arrays. Denominators are separate and not accuracy rates.')
binding=pre['bindings']+[bind(p) for p,h in extra]+[bind(R/'TA055_READING_INTAKE_062.json'),bind(R/'TA062_ACTUAL_LAUNCH_065.json'),bind(R/'TA055_QUEUED_SOURCE_SCOPE.json'),bind(R/'L04_COMPARISON_RESERVATION_027.json'),bind(D/'preflight062.json'),bind(D/'audit062.py'),bind(D/'inspect062.py'),bind(Path(__file__))]
doc=dict(artifact_kind='immutable_exact_version_nonblind_comparison',comparison_id='TA055_TA062',execution=dict(agent_id='/root/ta_compare062',fork_turns='none',role='NONBLIND',fresh_comparator=True,distinct_from_reader_and_producer=True,source_only_reading_credit=False,intake062_completed_before_launch=True),bindings=binding,proposal_bindings=pre['proposal_bindings'],source_edition=j['source'],core_refs=j['core_refs'],selected_blocks=j['selected_blocks'],cohort='original_probability_sample',prior_compared_core_overlap=0,overlap_basis='TA055_QUEUED_SOURCE_SCOPE root reservation; no independent exhaustive scan of all private historical comparisons claimed',compared_unique_cores=30,probability_core_segments=30,endpoint_core_segments=0,context_read_refs=rd['context_read_refs'],context_annotated_refs=rd['context_annotated_refs'],context_additional_core_credit=0,independent_denominators=den,claim_mapping=claim_rows,question_answer_inventory=question_rows,edge_review=edge_rows,discrepancy_ledger=issues,layer_matrix=layer_rows,producer_completed_core_cells=pcov,reader_total_coverage_cells=256,reader_core_coverage_cells=240,reader_context_coverage_cells=16,root_preflight_correction_preserved=True,source_omission_audit='All30 original cores and34 listed context originals read; all70 source-reader claims mapped including report/summons in question prose. Verse premises, conditions, names, dialogue, alternative proofs and typed relations independently reconciled. No whole-source atomic completeness certified.',reader_record_versions=[dict(id=r['id'],layer=r['layer'],canonical_sha256=canon(r)) for r in rd['records']],producer_record_versions=[dict(id=r['id'],layer=r['layer'],canonical_sha256=canon(r),supersedes=r.get('supersedes')) for r in active],producer_active_core_records_by_layer=dict(collections.Counter(r['layer'] for r in active)),semantic_scope_notes=list(notes.values()),verdict='REWORK_TARGETED',full_admission=False,task_eligibility={k:False for k in ['retrieval','segmentation','attribution','argument_extraction','qa','scholar_choice','ml']},newer_production=dict(prefix=712,new_segments=15,reviewed=False,later_version_inheritance=False),production_modified=False,reading_modified=False,prior_artifacts_modified=False,current015_changed=False,human_certification=False)
cb=write('ta055_comparison062.json',doc)
verdict={k:doc[k] for k in ['comparison_id','execution','bindings','core_refs','cohort','prior_compared_core_overlap','compared_unique_cores','independent_denominators','task_eligibility','full_admission','newer_production','human_certification']}
verdict.update(artifact_kind='exact_version_v2_verdict',verdict='REWORK_TARGETED',comparison=cb,required_producer_findings=[x['id'] for x in issues if x['category'].startswith('confirmed_producer')],reader_qualifications=[x['id'] for x in issues if x['category'].startswith('reader_')],unresolved_findings=[x['id'] for x in issues if x['category'].startswith('unresolved')],scope='Historical697 only, blocks13/15/16; useful preserved source substance with targeted graph and condition repairs. Freeze findings and stop; no correction execution authorized by this receipt.',full_review_receipt=False,admission_owner='global coordinator')
vb=write('ta055_v2_verdict062.json',verdict)
audit=dict(result='PASS_MECHANICAL_SEMANTIC_REWORK',comparison=cb,verdict=vb,preflight=bind(D/'preflight062.json'),input_hashes_rechecked=True,core_refs=30,core_layer_rows=240,total_reader_rows=256,context_rows=16,reader_evidence=503,manual_claim_map=70,manual_question_map=21,manual_edge_review=75,ledger_counts=dict(collections.Counter(x['category'] for x in issues)),edge_assessment_counts=dict(collections.Counter(x['assessment'] for x in edge_rows)),producer_evidence_slices=sum(len(r['evidence']) for r in s['records']),exact_prefix_proposals=len(s['proposals']),source_inventory_records=895,unchanged_reading_sha256=sha(D.parent/'taanit_delegated055.json'),unchanged_snapshot_sha256=sha(sp),limitations='Mechanical replay and exact slices do not establish scholarly correctness. No later-version admission, no eligibility and no full tractate review.',helpers=[bind(D/'audit062.py'),bind(D/'inspect062.py'),bind(Path(__file__))])
ab=write('validation062.json',audit)
for p in [D/'audit062.py',D/'inspect062.py',Path(__file__)]:
 with Path(str(p)+'.sha256').open('x') as f:f.write(sha(p)+'  '+p.name+'\n')
print(json.dumps(dict(comparison=cb,verdict=vb,validation=ab,denominators=den,ledger=audit['ledger_counts'],edge_counts=audit['edge_assessment_counts']),ensure_ascii=False))
