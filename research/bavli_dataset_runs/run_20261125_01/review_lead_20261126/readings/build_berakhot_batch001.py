import json, hashlib
from pathlib import Path
base=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
pp=base/'research/bavli_dataset_runs/run_20261125_01/review_plans/bavli_berakhot.json'
sp=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Zeraim/Berakhot/Hebrew/Wikisource Talmud Bavli.json')
p=json.loads(pp.read_text('utf-8')); s=json.loads(sp.read_text('utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(sp.read_bytes())==p['source_sha256']
texts={f'Berakhot {i//2+1}{"a" if i%2==0 else "b"}:{j+1}':t for i,page in enumerate(s['text']) for j,t in enumerate(page)}
core=[z['ref'] for b in p['review_blocks'][:3] for z in b['spans']]
def refs(v): return ['Berakhot '+x for x in v.split('|')]
def ev(v):
 return [{'ref':r,'start_char':0,'end_char':len(texts[r]),'quote':texts[r]} for r in refs(v)]
claims=[]
def c(id,r,prop,holder='anonymous Gemara',conditions=None,status='asserted',chain=None,unc=None):
 claims.append(dict(id=id,kind='atomic_claim',origin='source_paraphrase',proposition=prop,holder_candidates=[holder],reporter_or_transmission_chain=chain or [],conditions=conditions or [],local_status=status,evidence=ev(r),core_claim=any(x in core for x in refs(r)),uncertainty=unc or []))
c('C01','2a:1','Evening Shema begins when priests enter to eat terumah.','Mishnah anonymous frame')
c('C02','2a:1','Evening Shema terminus is end of first watch.','Rabbi Eliezer')
c('C03','2a:2','Evening Shema terminus is midnight.','Sages')
c('C04','2a:3','Evening Shema terminus is dawn.','Rabban Gamliel')
c('C05','2a:4','His sons remain obligated to recite Shema.','Rabban Gamliel',['They have not recited','Dawn has not risen'])
c('C06','2a:4','The mitzvah time of the cases called until midnight extends to dawn.','Rabban Gamliel / Mishnah continuation',unc=['Exact transition from reported speech to anonymous Mishnah generalization is not marked.'])
c('C07','2a:5','Burning fats and limbs has a mitzvah period until dawn.','Mishnah continuation')
c('C08','2a:5','Offerings eaten for one day have a mitzvah period until dawn.','Mishnah continuation',['Offerings in the one-day consumption category'])
c('C09','2a:5','The midnight limit distances a person from transgression.','Mishnah continuation')
c('C10','2a:8','The tanna presupposes the verse בשכבך ובקומך; the evening question concerns the time of lying-down Shema.')
c('C11','2a:9','The order evening before morning can alternatively be derived from creation order.',status='alternative answer')
c('C12','2a:11','After opening with evening and then teaching morning, the tanna explains morning while engaged in it and then evening.',status='local answer')
c('C13','3a:15','One does not enter a ruin because of suspicion.','anonymous baraita')
c('C14','3a:15','One does not enter a ruin because of collapse.','anonymous baraita')
c('C15','3a:15','One does not enter a ruin because of harmful beings.','anonymous baraita')
c('C16','3b:1','The suspicion rationale is independently needed for a new ruin.',conditions=['New ruin'],status='qualification')
c('C17','3b:2','The suspicion case is set with two people to remove the ordinary harmful-beings concern.',conditions=['Two people'],status='provisional answer; refined by C18')
c('C18','3b:3','Suspicion still applies with two licentious people.',conditions=['Two people','Licentious people','New ruin inherited from 3b:1'],status='local answer')
c('C19','3b:5','The collapse rationale applies independently with two upright people.',conditions=['Two people','Upright people'],status='local answer')
c('C20','3b:7','The harmful-beings rationale is initially isolated in a new ruin with two upright people.',conditions=['New ruin','Two upright people'],status='challenged and qualified')
c('C21','3b:9','Even with two people, harmful beings are feared in their own place.',conditions=['Their place','Two upright people','New ruin inherited from 3b:7'],status='local answer')
c('C22','3b:9','Alternatively the harmful-beings case is a solitary person in a new rural ruin.',conditions=['One person','New ruin','In the fields'],status='alternative answer')
c('C23','3b:9','Suspicion is absent in that rural case because a woman is not commonly present there.',conditions=['Rural ruin'],status='supporting explanation')
c('C24','3b:10','The night has four watches.','Rabbi',chain=['anonymous baraita','Rabbi'])
c('C25','3b:10','The night has three watches.','Rabbi Natan',chain=['anonymous baraita','Rabbi Natan'])
c('C26','3b:11','A middle watch has one preceding it and one following it.','anonymous tanna in exposition of Rabbi Natan',status='scriptural support')
c('C27','3b:12','The middle watch can mean one of the middle watches.','Rabbi (Gemara reconstruction)',status='answer',unc=['Not a direct named utterance by Rabbi; dialectical attribution.'])
c('C28','3b:13','The verse says middle, not middle among middle watches.','Rabbi Natan (Gemara reconstruction)',status='objection')
c('C29','3b:14','Combining midnight rising with preceding watches supports four watches.','Rabbi Yehoshua ben Levi',chain=['Rav Zerika','Rabbi Ami','Rabbi Yehoshua ben Levi'],status='support for Rabbi')
c('C30','3b:15','Six night hours and two day hours account for two watches under Rabbi Natan.','Rabbi Natan (Gemara reconstruction)',['Following Rabbi Yehoshua on royal rising time'],status='alternative reconciliation')
c('C31','3b:16','One and a half watches may also be called watches.','Rav Ashi',status='alternative reconciliation')
c('C32','5a:24|5b:1','One who studies Torah, practices kindness, and buries his children is forgiven all his sins.','anonymous tanna',chain=['tanna reciting before Rabbi Yohanan'],conditions=['Torah study','Acts of kindness','Burying children'],unc=['Conjunction is preserved; whether each merit suffices independently is not settled by this wording alone.'])
c('C33','5b:2','Kindness in the atonement verse denotes acts of kindness.','Rabbi Yohanan')
c('C34','5b:2','Truth in the atonement verse denotes Torah.','Rabbi Yohanan')
c('C35','5b:3','The repeated word עון supplies the derivation for burying children and forgiveness.','Rabbi Shimon ben Yohai',chain=['unnamed elder','Rabbi Shimon ben Yohai'],status='answer to Rabbi Yohanan')
c('C36','5b:4','Skin afflictions are not afflictions of love.','Rabbi Yohanan',status='asserted; alternative qualifications follow')
c('C37','5b:4','Children-related suffering is not affliction of love.','Rabbi Yohanan',status='qualified by 5b:9')
c('C38','5b:5','Any of the four appearances of skin affliction is an altar of atonement.','anonymous baraita',['One of the four appearances of affliction'])
c('C39','5b:6','Being an altar of atonement does not make these afflictions afflictions of love.',status='first reconciliation')
c('C40','5b:7','Alternatively distinguish our location from theirs.',status='alternative reconciliation',unc=['Bare הא לן והא להו does not expressly map locations to each proposition; no geographical or directional assignment imposed.'])
c('C41','5b:8','Alternatively distinguish private from public affliction.',status='alternative reconciliation',unc=['Bare הא בצנעא הא בפרהסיא does not expressly map each condition to the two propositions.'])
c('C42','5b:9','Rabbi Yohanan refers to a bone of his tenth son.','Rabbi Yohanan',status='reported counterevidence',unc=['The inference to afflictions of love belongs to the Gemara objection, not to the quotation itself.'])
c('C43','5b:9','Distinguish having no children at all from having children who died.',status='local reconciliation',unc=['Context supports restricting the negative claim to never having children; the two cases themselves are explicit, their mapping is reconstructed.'])
questions=[]
def q(id,r,form,answers,comparability): questions.append(dict(id=id,kind='question',origin='source_paraphrase',formulation=form,evidence=ev(r),answer_claim_ids=answers,comparability=comparability))
q('Q01','2a:1','When does evening Shema start?',['C01'],'One start-time answer in core; no full inventory of later alternatives claimed.')
q('Q02','2a:1|2a:2|2a:3','Until when is evening Shema recited?',['C02','C03','C04'],'Three explicit named positions on the same terminus; midnight safeguard explanation prevents flattening all into equivalent absolute-validity claims.')
q('Q03','2a:6|2a:7','What antecedent does the tanna assume and why evening first?',['C10','C11'],'C10 addresses both; C11 is an alternative explanation of order, not an alternative clock time.')
q('Q04','2a:10','Why does the blessings clause put morning first?',['C12'],'Objection to evening-first rationale answered by local teaching order.')
q('Q05','3b:3','With two people, why suspicion?',['C18'],'Refinement inherits prior new-ruin/two-person conditions.')
q('Q06','3b:4','Why list collapse independently of suspicion and harmful beings?',['C19'],'Independence case, not a dispute over the general prohibition.')
q('Q07','3b:6|3b:8','Why list harmful beings independently, and why would two people be at risk?',['C21','C22'],'C20 is challenged intermediate answer; C21 and C22 remain alternative configurations.')
q('Q08','3b:10','How many watches are in the night?',['C24','C25'],'Explicit comparable count disagreement, preserved after continuation to 3b:16.')
q('Q09','3b:11','What supports Rabbi Natan?',['C26'],'C27 responds to that support and C28 objects to C27.')
q('Q10','3b:14','What supports Rabbi?',['C29'],'C30 and C31 explain compatibility of verses with the other count, not a retraction by Rabbi.')
q('Q11','5b:2','Where is burial of children derived as a source of forgiveness?',['C35'],'Torah and kindness accepted separately as interpretable from the verse; the burial derivation is questioned.')
q('Q12','5b:5','How can afflictions be excluded from love if they are an altar of atonement?',['C39','C40','C41'],'Three textual alternatives; do not fuse into a cumulative final rule.')
q('Q13','5b:9','How can children-related suffering be excluded given Rabbi Yohanan’s bone report?',['C43'],'Rejected initial interpretation is having children who died; concluding distinction narrows initial generalization.')
edges=[]
def e(a,b,rel,r,explicit='source_explicit'): edges.append(dict(id=f'E{len(edges)+1:02}',source_id=a,target_id=b,relation=rel,explicitness=explicit,evidence=ev(r)))
for a,b,rel,r in [('C05','C04','support','2a:4'),('C09','C03','qualification','2a:5'),('C10','Q03','answer','2a:8'),('C11','Q03','answer','2a:9'),('Q04','C11','objection','2a:10'),('C12','Q04','answer','2a:11'),('C18','Q05','answer','3b:3'),('C19','Q06','answer','3b:5'),('Q07','C20','objection','3b:8'),('C21','Q07','answer','3b:9'),('C22','Q07','answer','3b:9'),('C23','C22','support','3b:9'),('C26','C25','support','3b:11'),('C27','C26','objection','3b:12'),('C28','C27','objection','3b:13'),('C29','C24','support','3b:14'),('C30','C29','qualification','3b:15'),('C31','C29','qualification','3b:16'),('C35','Q11','answer','5b:3'),('C38','C36','objection','5b:5'),('C39','Q12','answer','5b:6'),('C40','Q12','answer','5b:7'),('C41','Q12','answer','5b:8'),('C42','C37','objection','5b:9'),('C43','C37','qualification','5b:9')]:e(a,b,rel,r)
context=refs('2a:11|3a:15|3b:1|3b:2|3b:13|3b:14|3b:15|3b:16|5a:14|5a:15|5a:16|5a:17|5a:18|5a:19|5a:20|5a:21|5a:22|5a:23|5b:10|5b:11|5b:12|5b:13|5b:14|5b:15|5b:16')
out=dict(artifact_type='independent_source_only_reading',tractate='Berakhot',source_path=str(sp),source_sha256=sha(sp.read_bytes()),plan_file_sha256=sha(pp.read_bytes()),agent_id='/root/reader_berakhot',route='fresh fork_turns=none',model_id=None,producer_labels_exposed=False,frozen_before_comparison=True,status='FROZEN_SOURCE_ONLY_BATCH_NOT_TRACTATE_VERDICT',core_refs=core,context_refs=context,blocks=[dict(block_id=b['block_id'],roles=b['roles'],core_refs=[x['ref'] for x in b['spans']],inclusion_probability=b['inclusion_probability'],review_union_inclusion_probability=b['review_union_inclusion_probability']) for b in p['review_blocks'][:3]],claims=claims,questions=questions,directed_relations=edges)
out['boundaries']=[dict(refs=refs('2a:1|2a:2|2a:3|2a:4|2a:5'),type='Mishnah unit',status='closed locally',note='Starting time, termini, reported incident, generalized dawn limit and safeguard rationale are separable claims.'),dict(refs=refs('2a:6|2a:7|2a:8|2a:9|2a:10|2a:11'),type='Gemara order discussion',status='closed after context expansion'),dict(refs=refs('3a:15|3b:1|3b:2|3b:3|3b:4|3b:5|3b:6|3b:7|3b:8|3b:9'),type='ruins rationale discussion',status='closed after left expansion',note='Three rationales and configurations isolating each; not three opposing holders.'),dict(refs=refs('3b:10|3b:11|3b:12|3b:13|3b:14|3b:15|3b:16'),type='number of watches discussion',status='closed locally after right expansion',note='Later David discussion revisits the cited midnight verses but does not retract this count disagreement in the read continuation.'),dict(refs=refs('5a:24|5b:1|5b:2|5b:3'),type='forgiveness teaching and derivation',status='closed',note='Statement straddles daf boundary. Tanna before Yohanan is not Yohanan as initial holder.'),dict(refs=refs('5b:4|5b:5|5b:6|5b:7|5b:8|5b:9'),type='afflictions of love',status='closed locally; alternatives unresolved',note='Following illness narratives 5b:10–16 preserve rejection of suffering/reward by patients; not formal retraction of the preceding taxonomic claims.')]
out['context_observations']=[dict(origin='source_paraphrase',evidence=ev('5a:14|5a:15|5a:16'),note='The two named disputants have anonymous חד אמר assignments; no mapping imposed. Yohanan is reported through Rabbi Hiyya bar Abba and his son Rabbi Abba as accepting both categories.'),dict(origin='source_paraphrase',evidence=ev('5b:10|5b:11|5b:13|5b:16'),note='The patients reject both sufferings and reward; the anonymous maxim answers why Yohanan needs another healer. These narratives are context only and excluded from core omission denominator.')]
out['uncertainties_and_open_tails']=['No full-tractate claim, no production comparison, no practical halachic ruling.','Core ending 2a:10 has been resolved through 2a:11; subsequent terumah timing sugya is a new boundary and not adjudicated.','3b:12 continues through 3b:16; count disagreement remains, not artificially resolved by Rav Ashi.','5b:7–8 retain alternatives without mapping their pronouns by name/order or external commentary.','5b:9 mapping of never-had children to the negative love classification is contextual inference; literal evidence and inference are kept separate.','No exhaustive claims extraction for expanded narrative context; denominators below concern independently enumerated records, not all context content.']
out['denominators']={'definition':'Explicit record counts; core counts are omission baseline for this batch, not accuracy rates. Attributable means a named/collective identifiable holder, excluding anonymous and uncertain Mishnah continuation.','independently_found_core_claims':sum(c['core_claim'] for c in claims),'all_enumerated_claims':len(claims),'attributable_claims':sum(c['holder_candidates'][0] not in ['anonymous Gemara','anonymous baraita','anonymous tanna','Mishnah anonymous frame','Mishnah continuation','Rabban Gamliel / Mishnah continuation'] for c in claims),'condition_bearing_claims':sum(bool(c['conditions']) for c in claims),'proposed_answer_sets':len(questions),'argument_edges':len(edges),'core_segments_unique':len(core),'context_segments_unique':len(set(context)),'cohorts':{'opening_check_core_segments':10,'probability_sample_core_segments':20,'overlap_segments':0}}
out['next_selected_block']={'block_id':p['review_blocks'][3]['block_id'],'first_ref':p['review_blocks'][3]['spans'][0]['ref'],'last_ref':p['review_blocks'][3]['spans'][-1]['ref'],'roles':p['review_blocks'][3]['roles']}
out['source_attribution']={k:s.get(k) for k in ['title','versionTitle','versionSource','license']}
for record in claims+questions+edges+out['context_observations']:
 for v in record['evidence']: assert texts[v['ref']][v['start_char']:v['end_char']]==v['quote']
out['execution']={'agent_id':'/root/reader_berakhot','route':'interactive_agent','model_id':None}
out['fresh_context']={'fork_turns':'none','producer_labels_exposed':False}
for scope in ['core','context']:
 subset=[c for c in claims if c['core_claim']==(scope=='core')]
 out['denominators'][scope]={'claims':len(subset),'condition_bearing_claims':sum(bool(c['conditions']) for c in subset),'attributable_claims':sum(c['holder_candidates'][0] not in ['anonymous Gemara','anonymous baraita','anonymous tanna','Mishnah anonymous frame','Mishnah continuation','Rabban Gamliel / Mishnah continuation'] for c in subset),'proposed_answer_sets':sum(any(e['ref'] in core for e in q['evidence'])==(scope=='core') for q in questions),'argument_edges':sum(any(e['ref'] in core for e in edge['evidence'])==(scope=='core') for edge in edges)}
dest=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/readings/berakhot_batch001.json')
dest.parent.mkdir(parents=True,exist_ok=True)
with dest.open('x',encoding='utf-8',newline='\n') as f: json.dump(out,f,ensure_ascii=False,indent=2); f.write('\n')
h=sha(dest.read_bytes())
with dest.with_suffix('.sha256').open('x',encoding='ascii') as f:f.write(h+'  '+dest.name+'\n')
print(json.dumps({'file':str(dest),'sha256':h,'denominators':out['denominators'],'next':out['next_selected_block']},ensure_ascii=False))
