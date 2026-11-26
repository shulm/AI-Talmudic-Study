import json, hashlib
from pathlib import Path
ROOT=Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study')
OUT=Path(__file__).parent
def sha(b): return hashlib.sha256(b).hexdigest()
manifest=ROOT/'research/bavli_sugya_corpus_v1/source_manifest.json'
assert sha(manifest.read_bytes())=='11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c'
M=json.loads(manifest.read_text())
def setup(title,start,end,lo,hi):
 t=next(x for x in M['tractates'] if x['title']==title)
 p=Path('F:/Sefaria-Export-master')/t['source_path']; assert sha(p.read_bytes())==t['source_sha256']
 a=[(i,j,s) for i,page in enumerate(json.loads(p.read_text())['text']) for j,s in enumerate(page) if s]
 planp=ROOT/f'research/bavli_dataset_runs/run_20261125_01/review_plans/bavli_{title.lower()}.json';plan=json.loads(planp.read_text())
 block=next(b for b in plan['review_blocks'] if b['spans'][0]['nonempty_ordinal']==start)
 evidence=[]
 for n in range(lo,hi):
  i,j,s=a[n];r=dict(id=f's{n}',nonempty_ordinal=n,ref=f'{title} {i//2+1}{"a" if i%2==0 else "b"}:{j+1}',page_index=i,segment_index=j,offsets_codepoints=[0,len(s)],quote=s,span_sha256_utf8=sha(s.encode()),cohort='probability_core' if start<=n<end else 'context_expansion')
  evidence.append(r)
 for b in block['spans']:
  e=next(e for e in evidence if e['nonempty_ordinal']==b['nonempty_ordinal']);assert all(e[k]==b[k] for k in ['ref','page_index','segment_index','offsets_codepoints','span_sha256_utf8'])
 return dict(review_id=f'L04_{title.lower()}_continuation_source_only_20261126',source_file=str(p),source_sha256=t['source_sha256'],source_manifest_sha256=sha(manifest.read_bytes()),source_edition='Wikisource Talmud Bavli',seed=20261125,plan_file_sha256=sha(planp.read_bytes()),plan_sha256=plan['plan_sha256'],selected_block_id=block['block_id'],inclusion_probability=block['inclusion_probability'],core_ordinals_half_open=[start,end],context_ordinals=[n for n in range(lo,hi) if not start<=n<end],core_characters=sum(len(a[n][2]) for n in range(start,end)),core_segments=end-start,context_segments=hi-lo-(end-start),evidence=evidence,independence={'production_interpretations_seen':False,'production_proposals_seen':False,'production_checkpoints_seen':False,'prior_reviewer_readings_seen':False,'method':'Direct pinned originals only; project instructions, contract, manifest, and source-coordinate plan read. No model-memory supplementation. AGENT_HANDOFF administrative status read as required.'},records=[],edges=[],uncertainties=[],boundaries=[])
def record(d,id,kind,ords,reading,speaker='anonymous discussion',status='locally asserted',conditions=None,transmission=None):
 d['records'].append(dict(id=id,kind=kind,evidence=[f's{n}' for n in ords],cohort='probability_core' if any(d['core_ordinals_half_open'][0]<=n<d['core_ordinals_half_open'][1] for n in ords) else 'context_expansion',reading_paraphrase=reading,speaker=speaker,local_status=status,conditions=conditions or [],transmission=transmission or []))
def edge(d,source,target,relation,ords):d['edges'].append(dict(source=source,target=target,relation=relation,evidence=[f's{n}' for n in ords]))
m=setup('Makkot',20,30,14,31)
record(m,'m0','claim',[14],'Baraita: conspiring witnesses are not sold as Hebrew slaves; in Rabbi Akiva’s name, they also do not pay on their own admission.','baraita; Rabbi Akiva for final clause',transmission=['unspecified reporters: משום ר"ע אמרו'])
record(m,'m1','claim',[20],'Rav Hamnuna initially proposes limiting the no-sale rule to where the accused has property; if the accused has none, witnesses would be sold even if they have property.','Rav Hamnuna','provisional, challenged', ['accused has property: no sale','accused lacks property: proposed sale even if witnesses possess property'])
record(m,'m2','objection',[21],'Witnesses can respond: had you possessed property you would not be sold; we likewise should not be sold.','(Rava), printed parenthetically','objection to m1')
record(m,'m3','claim',[21],'Revised Rav Hamnuna proposal: no sale if either accused or witnesses have property; sale if both lack property.','Rav Hamnuna','provisional, rejected',['neither accused nor witnesses have property'])
record(m,'m4','rebuttal',[21],'Rava cites ונמכר בגנבתו and excludes sale for plotting: בגנבתו ולא בזממו.','Rava','locally resolving rejection of sale for witnesses')
record(m,'m5','question',[22],'Why does Rabbi Akiva exempt payment on self-admission?')
record(m,'m6','claim',[22],'Explanation of Rabbi Akiva: the liability is a fine and a fine is not paid on self-admission.','anonymous explanation of Rabbi Akiva',conditions=['self-admission'])
record(m,'m7','support',[22],'Rabbah supports fine characterization: witnesses did no act yet [are put to death] and pay. Preserve square-bracketed ונהרגים.','Rabbah')
record(m,'m8','support',[22],'Rav Nahman: property remains in owners’ hands yet witnesses pay.','Rav Nahman','initially separately phrased support')
record(m,'m9','reformulation',[23],'Anonymous continuation asks whether this is precisely Rabbah’s no-act argument; reformulates as וכן אמר ר"נ. It unifies the supports, not a dispute.','anonymous discussion','local reformulation')
record(m,'m10','claim',[24],'A conspiring witness pays according to his share.','Rav',transmission=['Rav Yehuda said in the name of Rav'])
record(m,'m11','question',[24],'If the statement merely means half each, the rule is already taught: divide monetary payment, not lashes.','anonymous discussion','rejects trivial interpretation')
record(m,'m12','interpretation',[25],'Alternative: only one of the pair was exposed as conspiring and pays his half.','anonymous discussion','rejected interpretation',['only one witness exposed'])
record(m,'m13','objection',[25],'Baraita says no monetary payment until both witnesses are exposed as conspiring.','anonymous discussion citing baraita','rejects m12', ['both witnesses must be exposed'])
record(m,'m14','interpretation',[26],'Rava proposes a witness saying: I testified falsely.','Rava','challenged interpretation')
record(m,'m15','objection',[26],'Can he do that? Once testimony is given, he cannot retract and give contrary testimony.','anonymous discussion','rejects m14')
record(m,'m16','interpretation',[27],'Revised case: admission that we testified and were exposed as conspiring in a specified court.','anonymous discussion','challenged interpretation')
record(m,'m17','objection',[27],'That would not accord with Rabbi Akiva, who exempts payment upon self-admission.','anonymous discussion','rejects m16 as sufficient explanation')
record(m,'m18','interpretation',[28],'Final case adds: we were adjudged liable to pay money in that court.','anonymous discussion','local accepted interpretation',['admission of testimony, exposure, and prior monetary judgment'])
record(m,'m19','claim',[29],'One might think that inability to obligate the other witness also exempts the admitting witness; teaching establishes his own liability.','anonymous discussion','rejected supposition followed by lesson',['admission cannot itself impose liability on companion'])
for s,t,r,o in [('m2','m1','objects_to',[21]),('m3','m1','revises',[21]),('m4','m3','rejects',[21]),('m6','m5','answers',[22]),('m7','m6','supports',[22]),('m8','m6','supports',[22]),('m9','m8','reformulates_as_parallel_to_m7',[23]),('m11','m10','questions_interpretation',[24]),('m12','m10','proposed_interpretation',[25]),('m13','m12','rejects',[25]),('m14','m10','proposed_interpretation',[26]),('m15','m14','rejects',[26]),('m16','m14','revises',[27]),('m17','m16','objects_to',[27]),('m18','m16','revises',[28]),('m19','m18','explains_novelty',[29])]:edge(m,s,t,r,o)
m['boundaries']=[{'after_ordinal':21,'description':'Sale exemption closes; Rabbi Akiva self-admission rationale opens at 22.'},{'after_ordinal':23,'description':'Rav monetary-share teaching opens at 24; retains conceptual connection with Rabbi Akiva self-admission.'},{'after_ordinal':29,'description':'New mishnah begins at 30; sampled monetary-share discussion reaches closure.'}]
m['uncertainties']=['First objection attribution is printed parenthetically (א"ל רבא); retain variant status rather than silently normalizing it. Later א"ל רבא is unparenthesized.','[ונהרגים] is square-bracketed in the exact source and must remain so; no manuscript conclusion is made.','Final case at ordinals 28–29 is anonymous; attribution of all revisions to Rava would exceed explicit text.','Ordinals 15–19 supplied previous-discussion context only; no full semantic extraction or counted core review is claimed for that surrounding kofer discussion.']
n=setup('Nedarim',30,40,22,53)
record(n,'n0','source_rule',[22,23,24],'Baraita establishes yadot through Nazir language and links vows/Nazir by hekesh, extending bal yahel, bal teaher, and paternal/spousal annulment.','baraita')
record(n,'n1','question',[29],'For the Torah-speaks-human-language position deriving yadot from nazir lehazir: if repeated Nazir vows take effect, whence that rule?','anonymous discussion',conditions=['position that Nazir vows take effect upon existing Nazir vows'])
record(n,'n2','answer',[30],'The wording להזיר rather than ליזור supports both derivations.','anonymous discussion')
record(n,'n3','transmission',[31],'In the West they report one tanna deriving yadot from לנדור נדר and another from כל היוצא מפיו יעשה. Names are not supplied.','במערבא אמרי',transmission=['Western reporters -> unnamed tanna A / unnamed tanna B'])
record(n,'n4','claim',[32],'Bal yahel for vows is illustrated by vowing to eat this loaf and failing to eat it.','anonymous discussion',conditions=['says ככר זו אוכל','fails to eat'])
record(n,'n5','question',[33],'How does Nazir bal yahel apply, since eating/drinking already incurs Nazir-specific prohibitions?')
record(n,'n6','answer',[33],'Rava: he transgresses two prohibitions.','Rava','local answer')
record(n,'n7','question',[34],'How can Nazir bal teaher occur if declaring oneself a Nazir immediately establishes Nazir status?')
record(n,'n8','interpretation',[34],'Proposal: when I wish I will be a Nazir; rejected because if conditioned on wishing there is no bal teaher.','anonymous discussion','proposed then rejected',['לכשארצה'])
record(n,'n9','answer',[35],'Rava gives the case: I will not depart the world before becoming a Nazir; immediate obligation is explained by possibility of death at any moment.','Rava','local answer', ['לא איפטר מן העולם עד שאהא נזיר'])
record(n,'n10','analogy',[35],'A wife given a get effective one hour before the husband’s death is immediately forbidden terumah, due to possible imminent death; analogically Nazir cannot postpone.','Rava within his answer',conditions=['get one hour before death'])
record(n,'n11','answer',[36],'Rav Aha bar Yaakov gives vowing while in a cemetery as bal teaher case.','Rav Aha bar Yaakov','subsequently qualified',['vows while in cemetery'])
record(n,'n12','objection',[37],'Objection: works if Nazir status does not immediately apply, but if it does, where is delay? Further, Mar bar Rav Ashi says it applies immediately and the dispute concerns lashes.','anonymous discussion citing Mar bar Rav Ashi','challenges unqualified reading of n11')
record(n,'n13','claim',[37],'Mar bar Rav Ashi: Nazir status applies immediately; disagreement is about lashes.','Mar bar Rav Ashi',conditions=['cemetery-vow context'])
record(n,'n14','answer',[38],'Nevertheless bal teaher applies because he delays Nazir status in purity.','anonymous discussion','local qualification of n11')
record(n,'n15','inference',[38],'Rav Ashi infers that a Nazir who intentionally defiles himself violates bal teaher of pure Nazir observance.','Rav Ashi','local inference',['intentional self-defilement'])
record(n,'n16','answer',[39],'Rav Aha son of Rav Ika: bal teaher concerns delay of shaving.','Rav Aha son of Rav Ika','local answer',['delay of shaving'])
record(n,'n17','qualification',[40],'Even if shaving is not indispensable, its commandment remains unfulfilled; the answer works for both views.','anonymous discussion','context qualification of sampled claim')
record(n,'n18','answer',[41],'Mar Zutra son of Rav Mari: delay concerns sacrifices.','Mar Zutra son of Rav Mari','context alternative',['delay of sacrifices'])
record(n,'n19','question',[42],'Why derive this here when כי דרוש ידרשנו already includes sin and guilt offerings?','anonymous discussion')
record(n,'n20','proposal',[43,44],'Nazir novelty might warrant exclusion; first suggestion that Nazir sin offering cannot be separately vowed is challenged by ordinary sin offering.','anonymous discussion','challenged')
record(n,'n21','proposal',[45,46],'Another suggested novelty: Nazir from even one grape seed extends to all; challenged by Rabbi Shimon requiring all, and because this is a stringent novelty.','anonymous discussion','rejected')
record(n,'n22','answer',[47,48],'Alternative novelty: shaving upon one of three sacrifices suffices, so one might exempt delay; teaching rejects that exemption.','anonymous discussion','context answer')
record(n,'n23','answer',[49,50],'Alternative returns to inability to vow the sin offering separately, distinguishing ordinary sin offering as atonement and childbirth offering as permitting sacred food.','anonymous discussion','alternative context answer')
record(n,'n24','question',[51,52],'Why need hekesh for Nazir annulment rather than analogy to vows? Fixed Nazir duration could have led to excluding annulment; hekesh teaches otherwise.','anonymous discussion','separate next subsection')
for s,t,r,o in [('n2','n1','answers',[30]),('n6','n5','answers',[33]),('n8','n7','rejected_answer',[34]),('n9','n7','answers',[35]),('n10','n9','supports_by_analogy',[35]),('n11','n7','alternative_answer',[36]),('n12','n11','objects_to',[37]),('n13','n12','supports_objection',[37]),('n14','n12','answers',[38]),('n15','n14','extends',[38]),('n16','n7','alternative_answer',[39]),('n17','n16','qualifies',[40]),('n18','n7','alternative_answer',[41]),('n19','n18','questions_need_for_derivation',[42]),('n20','n19','challenged_answer',[43,44]),('n21','n19','rejected_answer',[45,46]),('n22','n19','answers',[47,48]),('n23','n19','alternative_answer',[49,50])]:edge(n,s,t,r,o)
n['boundaries']=[{'after_ordinal':30,'description':'Closes specific dual-derivation question; Western tannaitic alternatives at 31.'},{'after_ordinal':31,'description':'אמר מר returns to quoted baraita for bal yahel analysis.'},{'after_ordinal':33,'description':'Moves from bal yahel to bal teaher; core ends before all answers complete.'},{'after_ordinal':50,'description':'End of sacrifice-delay alternatives; next subsection concerns annulment hekesh.'},{'after_ordinal':52,'description':'Annulment hekesh answer closes; 53 begins Mishnah wording discussion (seen only as boundary marker, not counted).'}]
n['uncertainties']=['Ordinal 35 literally says הוה ליה נזיר and לאלתר הוי נזיר. Exact text is retained; the paraphrase immediate obligation does not settle broader legal mechanics of commencement versus duty to commence.','The unnamed תנא alternatives at 31 cannot be assigned names or aligned to named authorities by sequence.','Mar bar Rav Ashi at 37 and Rav Ashi at 38 are distinct attributions, not a harmonized identity.','Bal teaher answers are alternative explanatory cases; no unsupported binary disagreement is inferred between their named proponents.','Context ordinals 22–29 and 51–52 are supporting context; no comprehensive standalone extraction claim for all preceding interpretive derivations.']
for d in [m,n]:
 d['status']='FROZEN_SOURCE_ONLY_BEFORE_COMPARISON'
 d['limitations']=['AI source reading, not human scholarly certification.','Unreviewed later probability blocks are pending review, not established production omissions.','Only core semantic records contribute to sampled independent-extraction counts; context expansions are separate.']
 target=OUT/(d['review_id']+'.json'); assert not target.exists()
 target.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(target,sha(target.read_bytes()))
