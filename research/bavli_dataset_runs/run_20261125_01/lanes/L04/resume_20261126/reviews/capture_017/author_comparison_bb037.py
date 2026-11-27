from audit_bb037 import *
rid={x['id'].split('.',1)[1]:x for x in rr}
mapping={
'lodging':'lodge','manure':'manure','lodgingbar':'barlodge','obstruction':'block','distance':'longer',
'outerall':'outer','outerself':'outer','secondall':'second','secondself':'second','secondouter':'second','innerself':'inner','innerall':'inner',
'tannaitic':'tannaim','reroute':'rebchange','reopen':'reopen','shared':'shared','missingtext':'restore','rabbiouterall':'rebgraded','rabbiouterself':'rebgraded','shared11':'sharedrepeat',
'reopenquote':None,'frameintact':'retained','framebroken':'removed','house4':'closed','house0':'nopost','tombclosed':'tomb','tombbroken':'tomb','impurityhouse':'houseclean','impuritybroken':'houseimpure','othercity':'city','noroute':'alternate','withroute':'alternate'}
assert {x['id'] for x in rc if x['layer']=='claims'}=={'bb037r2.'+k for k in mapping}
claims=[]
for k,v in mapping.items():
 ids=['bb.r032.'+v+'.c'] if v else []
 for z in ids:assert z in lookup
 status='represented'
 note='Source proposition, local stage and conditions represented; holder and transmission checked separately.'
 if k in ['outerall','outerself','secondall','secondself','secondouter','innerself','innerall','rabbiouterall','rabbiouterself','noroute','withroute']:
  status='reasonable_granularity';note='Multiple reader units map to the stated combined producer proposition; no omitted substantive branch.'
 if k in ['tombclosed','tombbroken']:
  status='coarse_representation_with_restriction';note='Both clauses and removed-plus-reclosed condition retained in evidence and expressly non-atomic combined record. Summary does not spell out which branch imparts impurity; cannot serve as a condition-to-outcome answer without refinement.'
 if k=='reopenquote':status='confirmed_occurrence_omission';note='The earlier 11b:10 proposition exists as bb.r032.reopen.c; the quoted 11b:12 occurrence has no separate utterance/claim/quotation edge. Whole structure evidence and Rava evidence preserve the words but not their occurrence annotation.'
 claims.append(dict(reader_id=rid[k]['id'],producer_ids=ids,assessment=status,note=note,source_evidence=rid[k]['evidence']))
edge_specs={
'lodginganswer':(['lodge_answer'],'represented','Same claim-to-question answer.'),
'lodgingsupp':(['lodge_support'],'represented','Same baraita-to-answer support.'),
'dialoguecontinuation':([],'reasonable_granularity','Inherited dialogue identity is explicit in producer scope; optional editorial continuation edge not present.'),
'distancerationale':(['longer_support'],'represented','Same rationale-to-obstruction support.'),
'objection':(['outer_objection'],'represented','Producer combined outer claim contains reader outerself; same challenged Rav Huna claim.'),
'innercontinuation':([],'reasonable_granularity','Continuation is retained in one graded-use source bundle; explicit separate continuation edge absent, no claim omitted.'),
'reconcile':(['tannaim_resolution'],'reasonable_granularity','Reader targets reconstructed objection question, producer targets objection-bearing claim; both resolve local challenge, not the existence of the graded rule.'),
'sharedsupport':([],'uncertainty','Source תנאי היא supports this editorial alignment; producer preserves tannaitic distinction and resolution, but no direct R. Shimon-to-Rav Huna support edge. Do not certify equivalence of typed inventories.'),
'reconstructionanswer':(['restore_answer'],'represented','Same reconstruction answer to missing-courtyards question.'),
'repair':([],'reader_error','The correction is to the incomplete quoted formulation, not to R. Shimon shared-use proposition which is repeated unchanged. Retarget to quotation/reconstruction structure, or narrow the relation scope.'),
'rabbiattribution':([],'reasonable_granularity','Producer separately attributes reconstructed graded clause to Rabbi. No direct quotation edge connects earlier anonymous formulation; source reconstruction relation is not a new named original speaker event.'),
'reopenquotation':([],'confirmed_producer_omission','Quoted 11b:12 occurrence and its quotation relation are missing.'),
'qualify':(['retained_qualification'],'represented_with_occurrence_gap','Correct earlier reopening claim targeted; missing repeated occurrence separately logged.'),
'contrast':(['removed_distinction'],'represented','Same removed-versus-retained condition distinction.'),
'supportframe':(['closed_support'],'represented','Baraita supports retained-post case, Abaye is introducer rather than baraita author.'),
'supportbroken':(['nopost_support'],'represented','Baraita supports removed-post case.'),
'housesdistinction':([],'confirmed_producer_omission','Both conditional four-cubit claims exist, but no typed distinction connects them. Support edges to Rava do not replace this within-baraita distinction.'),
'tombdistinction':([],'restricted_granularity','Two branches are one expressly non-atomic claim, so a typed two-endpoint distinction is unavailable; coarse inventory not suitable for atomic relation tasks.'),
'impuritydistinction':(['impurity_distinction'],'represented','Correct distinct house claims and condition directions.'),
'impurityanalogy':([],'uncertainty','Reader labels analogy editorial. Adjacent baraita material does not explicitly assert this analogy; optional reconstruction, not confirmed producer omission.'),
'evenalternative':(['alternate_qualification'],'reasonable_granularity','Reader relates stronger to easy branch; producer combined branches qualify general city rule. Typed topology differs but source conditions and stronger case retained.')}
assert {x['id'] for x in rc if x['layer']=='edges'}=={'bb037r2.'+k for k in edge_specs}
edges=[]
for k,(vs,ass,note) in edge_specs.items():
 ps=[lookup['bb.r032.'+v] for v in vs]
 edges.append(dict(reader_id=rid[k]['id'],reader_content=rid[k]['content'],source_evidence=rid[k]['evidence'],producer_ids=[x['id'] for x in ps],producer_contents=[x['content'] for x in ps],assessment=ass,note=note))
def discrepancy(key,cat,ks,ps,note,action,severity='localized'):
 return dict(id=key,category=cat,reader_ids=[rid[k]['id'] for k in ks],producer_ids=ps,source_evidence=[e for k in ks for e in rid[k]['evidence']],finding=note,required_action=action,severity=severity,resolution_state='open_additive_review_only')
disagreements=[
discrepancy('BB037-P001','confirmed_producer_occurrence_omission',['reopenquote','reopenquotation'],['bb.r032.reopen.c','bb.r032.retained_qualification'],'Repeated אמר מר lemma at 11b:12 is absent as an utterance/claim/quotation occurrence, though words survive in structural evidence. Earlier claim cannot count twice automatically.','Add source-anchored repeated lemma with quoted authority distinct from anonymous citing voice and quotation edge; retain original IDs and qualify with Rava.'),
discrepancy('BB037-P002','confirmed_producer_typed_edge_omission',['housesdistinction'],['bb.r032.closed.c','bb.r032.nopost.c','bb.r032.closed_support','bb.r032.nopost_support'],'Within-baraita retained/lost four-cubit distinction is not in producer edge inventory.','Add distinction from no-post/no-four-cubit claim to closed-house/four-cubit claim with exact 12a:1 evidence; support edges remain.'),
discrepancy('BB037-R001','reader_error',['repair'],['bb.r032.restore.c','bb.r032.shared.c','bb.r032.sharedrepeat.c'],'Reader correction targets the R. Shimon shared-use claim; source repairs missing courtyard clause, without correcting that unchanged claim.','Preserve reader r2; add a correction event that changes endpoint/scope to the incomplete quotation rather than shared-use proposition.'),
discrepancy('BB037-G001','reasonable_granularity_with_restricted_eligibility',['tombclosed','tombbroken','tombdistinction'],['bb.r032.tomb.c','bb.r032.tomb.p','bb.r032.tomb.u'],'Parenthetical tomb clauses are preserved explicitly as a non-atomic paired formulation. Summary lacks outcome polarity and a separate typed branch relation. Not a false assertion or lost source wording.','Before atomic QA/argument use, split or explicitly state both outcomes and retain וסתמו condition unique to parenthetical tomb wording; currently no such eligibility.',severity='task_restriction'),
discrepancy('BB037-U001','unresolved_attribution_boundary',['noroute','withroute'],['bb.r032.alternate.a','bb.r032.alternate.c','bb.r032.city.a'],'Reader provisionally extends Yohanan holder over explanatory branches with uncertainty; producer marks explanatory voice anonymous. Source has no explicit boundary marker.','Retain report-holder Yohanan and reporter Rabbah bar bar Hana; preserve uncertainty about explanation voice without forcing a named attribution.',severity='uncertainty')]
pos={x['content']['claim_id']:x for x in rc if x['layer']=='positions'}
named=[];attributable=[];conditions=[]
for x in rc:
 if x['layer']!='claims':continue
 h=pos[x['id']]['content']['holder_candidates']
 if h:attributable.append(x['id'])
 if h and not all('anonymous' in v for v in h):named.append(x['id'])
 if x['content']['conditions']:conditions.append(x['id'])
questions=[dict(reader_id=rid['lodgingq']['id'],producer_ids=['bb.r032.lodge_q.q'],answer_claims=[rid['lodging']['id']],comparison='Persons versus entrances is a question alternative, not two named maintained positions. Actual answer persons supported by baraita; partial inventory.'),dict(reader_id=rid['objectionq']['id'],producer_ids=['bb.r032.outer_objection','bb.r032.tannaim_resolution'],answer_claims=[rid['tannaitic']['id']],comparison='Editorially reconstructed objection question; producer typed objection/resolution represents function without a duplicate question. No competing scholar-answer set certified.'),dict(reader_id=rid['courtyardq']['id'],producer_ids=['bb.r032.missing_q.q'],answer_claims=[rid['missingtext']['id']],comparison='One local missing-text reconstruction answer; not an exhaustive alternative inventory.')]
prior_files=list((R/'comparisons').glob('*.json'))+list(T.parent.glob('**/comparisons/*.json'))
prior=[]
for p in prior_files:
 if O in p.parents:continue
 try:x=read(p)
 except Exception:continue
 def declared_refs(z):
  out=set()
  if isinstance(z,dict):
   for k,v in z.items():
    if k in ['compared_core_refs','core_refs'] and isinstance(v,list):out.update(t for t in v if isinstance(t,str))
    else:out.update(declared_refs(v))
  elif isinstance(z,list):
   for v in z:out.update(declared_refs(v))
  return out
 ov=core&declared_refs(x)
 if ov:prior.append(dict(artifact=bind(p),overlap_refs=sorted(ov)))
layer_notes={
'structure':'Producer four multi-segment primary bundles versus ten per-core reader units; exact full character partitions pass. Boundary granularity reasonable; 11b:12–12a:2 continuation retained.',
'utterances':'Named speech, supporting baraita and reconstruction distinguished. Repeated אמר מר occurrence missing (P001). Tomb is explicitly composite, not certified atomic.',
'claims':'All 32 independently found core claim occurrences mapped; one repeated occurrence omission. Ten-plus reader units legitimately share coarse producer claims; tomb summary restricted.',
'attributions':'Rabbi Ami/Rav Huna inherited dialogue verified at11b:5. Rabbi versus R. Shimon reconstruction verified. Rava is not Rabbah. Abaye introduces anonymous baraita. Yohanan holder and Rabbah bar bar Hana transmitter retained; anonymous explanation boundary unresolved.',
'questions':'Two explicit questions plus one editorial objection question; all three functions represented. No exhaustive or comparable scholar-choice inventory certified.',
'positions':'Generic asserted labels read with scope and argument relations. תנאי היא resolves local objection without retracting Rav Huna; reopening rule qualified by retained posts. No practical halakhic finality.',
'edges':'21 independent core-evidence edge candidates assessed individually with typed endpoints; missing repeated quotation and four-cubit distinction recorded. Reader correction endpoint error retained; optional editorial analogy/support not forced.',
'reconciliation':'Independent source omission check covers both lodging/manure allocations, all five-courtyard branches, original and reconstructed repeated formulations, reopening/post conditions, both tomb/house variants, alternative-route strength and Rav rationale in context.'}
doc=dict(artifact_kind='exact_version_nonblind_comparison',agent_id='/root/bb_compare037',provenance=dict(role='NONBLIND comparator, not fresh source-only reading',launch='fresh fork:none per parent dispatch',distinct_from_producer_and_reader=True,reader_agent='/root/bb_source_review037',model_id=None,sequence_disclosure='Inspected frozen source-only reader and exact producer excerpts during setup before completion of independent replay; no verdict or output issued before PASS. NONBLIND throughout.'),bindings=bindings,validation=bind(O/'validation_replay_bb037.json'),author_helper=bind(Path(__file__)),compared_core_refs=j['core_refs'],cohort=j['cohort'],selected_blocks=j['selected_blocks'],sampled_core_count=10,context_refs_read=['Bava Batra 11b:5','Bava Batra 12a:4','Bava Batra 12a:5'],context_not_extra_cores=True,prior_comparison_overlap=dict(search_roots=[str(R/'comparisons'),str(T.parent)],files_inspected=len(prior_files),matched_artifacts=prior,overlap_core_refs=sorted({v for a in prior for v in a['overlap_refs']})),new_reading_credit=0,comparison_credit_pending_root_intake=10,layer_matrix=[dict(layer=l,producer_completed_core_segments=obs['coverage'][l],compared_core_segments=10,assessment=layer_notes[l]) for l in m.LAYERS],independent_denominators=dict(core_claim_occurrences=32,context_claim_occurrences=2,attributable_core_claims=len(attributable),attributable_definition='Reader holder_candidates nonempty, including anonymous baraita as quoted authority; not equivalent to a named scholar.',attributable_ids=attributable,named_attributable_core_claims=len(named),named_attributable_ids=named,condition_bearing_core_claims=len(conditions),condition_bearing_ids=conditions,condition_definition='Independent reader explicit conditions nonempty; implicit settings separately reviewed, not claimed exhaustive atomic ontology.',proposed_answer_inventories=3,explicit_questions=2,editorial_questions=1,certified_comparable_exhaustive_scholar_answer_sets=0,core_argument_edge_candidates=21,context_edge_candidates=2,uncertainty='Denominators are frozen independent reading units; coarse producer counts are not accuracy denominators.'),claim_mapping=claims,question_answer_review=questions,edge_mapping=edges,discrepancy_ledger=disagreements,context_review=['11b:5 establishes Huna asks Ami; no attribution by mere order.','12a:4 Yehuda transmits Rav; parenthetical Giddel is separate. Producer public_support targets general city rule and reader targets stronger alternative-route branch: reasonable scope difference. Giddel nested support differs but no forced Rav/Shmuel dispute.','12a:5 begins Anan/Shmuel public-domain doors report, a separate subject. It is context only, not sampled or newly admitted.'],additional_source_checks=['The initial reader repeated-substring lodging evidence error was corrected before producer exposure; preserved initial/r2 hashes, not producer defect or new credit.','Parenthetical tomb wording includes וסתמו; unparenthesized house clause does not. Producer records preserve the distinction.','Tannaitic shared use and graded use are real local alternatives; no speculative permanent named positions for anonymous objections.','Producer-only allocation_distinction correctly distinguishes manure from lodging rather than opposing speakers; restored_content support and shared_distinction correctly preserve reconstruction and tannaitic contrast.'],versions=dict(reader=[dict(id=x['id'],sha256=hashlib.sha256(m.encoded(x)).hexdigest()) for x in rr],producer=[dict(id=x['id'],sha256=hashlib.sha256(m.encoded(x)).hexdigest(),release_state=x['release_state'],supersedes=x.get('supersedes')) for x in pc]),verdict='REWORK_TARGETED',limits=['Historical310 snapshot only; newer317 window12b:9–13a:1 excluded/unreviewed.','No whole-tractate or whole-snapshot admission; 310 production cores is not independent coverage.','No release015 changes, paid APIs, production/common/root artifacts or preserved reader bytes modified.','No human certification, new task eligibility, later-version inheritance, or replacement of reader disagreement history.','Prior overlap search limited to declared core coordinates in available root/L04 comparison JSONs; root reconciles other ledgers.'],task_eligibility={k:False for k in ['segmentation','retrieval','attribution','argument_extraction','qa','scholar_choice','ml']},tractate_accepted=False,later_versions_inherit_review=False)
cp=put('bb037_exact_version_comparison.json',doc)
vp=put('bb037_v2_verdict.json',dict(artifact_kind='v2_exact_version_review_verdict',verdict='REWORK_TARGETED',agent_id=doc['agent_id'],role='NONBLIND',comparison=cp,bindings=bindings,validation=doc['validation'],compared_core_refs=j['core_refs'],cohort=j['cohort'],layer_matrix=doc['layer_matrix'],independent_denominators=doc['independent_denominators'],required_producer_changes=disagreements[:2],reader_corrections=[disagreements[2]],granularity_and_uncertainty=disagreements[3:],task_eligibility=doc['task_eligibility'],limits=doc['limits'],tractate_accepted=False,human_certification=False,current_release015_unchanged=True,later_versions_inherit_review=False,admission_owner='root review lead; no automatic admission'))
for p in [Path(__file__),O/'audit_bb037.py']:
 q=p.with_suffix(p.suffix+'.sha256');t=sha(p)+'  '+p.name+'\n'
 if q.exists():assert q.read_text()==t
 else:q.write_text(t,encoding='ascii')
assert sha(RP)==bindings['effective_reading']['sha256'] and sha(S)==bindings['snapshot']['sha256']
print(json.dumps(dict(comparison=cp,verdict=vp,denominators=doc['independent_denominators'],overlap=doc['prior_comparison_overlap']),ensure_ascii=False))
