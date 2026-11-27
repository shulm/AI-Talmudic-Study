from validate_comparison import *
ss=module(B/'bavli_production_v1/runner.py','r').load(P/'job')[1];s=read(P/'job/snapshots'/f'{H}.json');rd=read(R/'reading.json');exp=read(R/'exposure.json');active=[r for r in s['records'] if r.get('release_state','valid')=='valid'];pi={r['id']:r for r in active};ri={r['id']:r for r in rd['records']}
def write(n,x):
 p=O/n;assert not p.exists();p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Explicit reviewed semantic correspondence, not automated matching.
names='''r021.four.c;r021.seller.c,r021.buyer.c;r021.three.c;r021.report.c,r021.tarfon.c;r021.tarfon.c;r021.rava.c;r021.extended.q;r021.invitation.c,r021.permitted.c;r021.why.q;r021.idiom.c;r021.unlike.u;r021.unlike.c;r021.open.c;r021.open.c;r021.asi.c;r021.shmuel.q;r021.alt.c;r021.regret.c;r021.hunaq.q;r021.hunar.c;r021.rabbahq.q;r021.rabbahr.c;r021.yehuda.c;r021.yosei.c;r023.regret.c,r023.name.c;r023.shimon.c,r023.againq.q,r023.yes.c;r023.sun.c;r023.alternate.c;r023.batnit.q;r023.free.c;r023.yishmael.c,r023.questions.c;r023.launderer.c;r023.wouldnot.c,r023.free2.c;r023.novelq.q;r023.common.c;r023.daughter.c;r023.condition.c;r023.did.c;r023.anticipated.q;r023.abayeNo.c;r023.allowedq.q;r023.pilgrim.c;r023.pilgrimq.q;r023.pilgrimNo.c;r024.m.c;r024.ob.q;r024.urge.c;r024.annual.c,r024.remember.c;r024.memory.q;r024.abaye.c;r024.rava.c;r024.invoke.c;r024.omit.c;r024.public.c;r024.oppose.c;r025.ants.q;r025.common.c;r025.private.q;r025.court.c;r025.sticks.q;r025.infer.c;r025.cane.c;r025.debt.c,r025.pay.c;r025.paid.c;r025.swear.c;r025.hide.c,r025.lean.c;r025.hold.c;r025.oath.c;r025.break.c,r025.spill.c;r025.literal.c;r025.mosesq.q;r025.moses.c;;r025.idols.q,r025.inferred.c;r025.normal.c;r025.commands.q;r025.royal.c;r025.allq.q;r025.fringes.c;r025.equal.c;r025.torahq.q;r025.one.c;r025.pluralq.q;r025.offerings.c;r025.bothq.q;r025.both.c;r025.wholeq.q;r025.idolonly.c;r025.denial.c;r025.explicit.q;r025.brief.c'''.split(';')
assert len(names)==91
mapping=[]
for i,ns in enumerate(names,1):
 r=ri[f'nd118.claims.{i:03}'];targets=['nd.'+n for n in ns.split(',') if n];assert all(t in pi for t in targets)
 mapping.append(dict(reader=r,producer_records=[pi[t] for t in targets],assessment='source_premise_omitted' if i==73 else 'metatext_vs_cross_segment_utterance_granularity' if i==11 else 'substance_preserved_with_typed_defects_or_uncertainty_detailed_in_report',cohort='core' if r['evidence'][0]['segment_id'] in exp['fully_reviewed_core_refs'] else 'fully_reviewed_context'))
write('claim_correspondence.json',mapping)
notes={
'21a:2':'D3: nested report and Tarfon principle preserved in prose; typed anonymous report and missing Yehuda-to-Tarfon transmission.',
'21a:3':'Rava alternative attribution and objection preserved.',
'21a:4':'Question preserved; none answer-set field is not by itself a defect; unresolved endpoint21b:2 retained.',
'21a:5':'D3: Rav Ashi citing teaching survives prose but typed voice anonymous; analogy preserved.',
'21a:6':'Proposed idiom answer and later challenge preserved; U1 none with explicit answer edge.',
'21a:7':'Cross-page utterance preserved; reader metatext claim versus producer combined span is granularity.',
'21b:1':'Distinction preserved as objection; reader challenged mode conflates an act of challenge with challenged status (U3); separate rhetorical-question node optional.',
'21b:2':'Both hypotheses and explicit unresolved תיבעי preserved together; splitting alternatives reasonable.',
'21b:3':'Rav Asi is not Rav; Rav Yehuda transmitter and Shmuel objection preserved.',
'21b:4':'Alternative Rav Yosef chain and inferred no-regret view preserved; source does not certify historical retraction.',
'23a:3':'Named question, no and plural release preserved; U1 answer-set field.',
'23a:4':'D1 repeated explicit question lacks typed question; D3 named Yishmael speech marked anonymous. Self-release wording cautiously preserved.',
'23a:5':'Foreseeability objection and reply preserved; U1 answer-set field.',
'23a:6':'Conditional vow, wife’s fulfillment, counterfactual question and release preserved; U1 answer-set field.',
'23a:7':'Parallel pilgrimage story kept distinct; explicit yes/no answer and analogy preserved; U1 fields; reader answer edge unnecessarily editorial.',
'23a:8':'Transmitted remembrance proviso retained; no silent Abaye substitution.',
'23a:9':'Explicit objection question retained; missing typed objection-to-Mishnah edge (D4).',
'23b:1':'Two reconstructed clauses and remembered proviso preserved in separate records; correction and answer retained.',
'23b:2':'Abaye non-remembrance correction retained; U2 comparable answer question_id absent despite edge.',
'23b:3':'Rava remembered stipulation with unknown content and explicit invocation/omission branches correctly preserved; U2 position links.',
'25a:3':'Challenged private-intention inference retained; missing objection edge back to25a:1 (D4).',
'25a:4':'Cane deflection, debtor assertion and Rava oath direction retained; creditor demand speaker prudently unresolved.',
'25a:5':'All cane actions, temporary holding and oath preserved; narrative granularity acceptable.',
'25a:6':'Anger, breaking, spill and literal truth preserved; no endorsement inferred.',
'25a:7':'Moses baraita and renewed private-intention question retained; missing support/objection relation pair (D4).',
'25a:8':'D2 first premise of proposed explanation lacks utterance/claim; private naming question and inference remain.',
'25a:9':'Ordinary scriptural name defeats private-renaming inference; answer/correction retained.',
'25a:10':'Commandments/king-command question-answer retained.',
'25a:11':'All-commandments/fringes and unnamed authority support retained.',
'25a:12':'Three separate wording questions/answers retained, bracketed תורות preserved.',
'20b:14':'Four categories and two bargaining formulas preserved; source-only combined seller/buyer versus separate production records acceptable.',
'21a:1':'Present desire for three dinars retained; grouping versus explicit continuation edge acceptable.',
'21b:5':'Huna question/no/release preserved; U1 answer-set field.',
'21b:6':'Rabba bar Rav Huna distinct; ten appeasers/no/release preserved; U1 answer-set field.',
'21b:7':'Both baraita rules and Yishmael reporting father Yosei preserved.',
'22b:7':'Rava-to-Rav Nachman and both local ruling clauses preserved; generic position local_status less informative than correct claim.',
'22b:11':'R1 reader omits typed repeated question; producer has it and answer; U1 producer field.',
'23a:1':'Sages’ sun/shade distress preserved.',
'23a:2':'Alternative version retained as separate occurrence, not duplicate event asserted.',
'23b:4':'Intended public lecture and Rava objection preserved; reader rhetorical question versus objection claim is granularity.',
'24b:7':'Ant-renaming question preserved; surrounding unreviewed prior material not certified.',
'25a:1':'Rav Ashi shared-understanding answer preserved.',
'25a:2':'Court formula, private-understanding question and sticks/coins hypothesis preserved; support/objection edges missing (D4).',
'25a:13':'Whole-Torah/idolatry answer and baraita rationale retained.',
'25a:14':'Final explicit formulations and non-cumbersome-wording conclusion retained; no false rejection of all formulations.'}
layers=['structure','utterances','claims','attributions','questions','positions','edges','reconciliation'];matrix=[]
for cohort,refs in [('core',exp['fully_reviewed_core_refs']),('fully_reviewed_context',exp['fully_reviewed_context_refs'])]:
 for ref in refs:
  sid=next(k for k,v in ss.items() if v['ref']==ref)
  for layer in layers:
   rr=[r for r in rd['records'] if r['layer']==layer and any(e['segment_id']==ref for e in r['evidence'])];pr=[r for r in active if r['layer']==layer and any(e['segment_id']==sid for e in r['evidence'])]
   matrix.append(dict(ref=ref,cohort=cohort,layer=layer,reader_record_ids=[r['id'] for r in rr],producer_record_ids=[r['id'] for r in pr],reader_coverage=[c for c in rd['coverage'] if c['segment_id']==ref and c['layer']==layer],producer_coverage=[c for c in s['coverage'] if c['segment_id']==sid and c['layer']==layer],review='compared; see per-ref assessment and bounded findings, not blanket PASS',ref_assessment=notes[ref.split()[1]]))
write('layer_comparison.json',matrix)
write('scope_and_adapter.json',dict(core_refs=exp['fully_reviewed_core_refs'],fully_reviewed_context_refs=exp['fully_reviewed_context_refs'],incidental_display_only_refs=exp['incidental_display_only_refs'],adapter={ref:next(k for k,v in ss.items() if v['ref']==ref) for ref in exp['fully_reviewed_core_refs']+exp['fully_reviewed_context_refs']},adapter_kind='Read-only coordinate correspondence, not a submitted adapted proposal',reader_open_tails=rd['open_tails'],production_adapter_compatible=False,no_expansion_credit=True,ml_eligible=False))
unc=[]
for q in active:
 if q['layer']=='questions' and q['content']['answer_set_status']=='none' and any(e['segment_id'] in {next(k for k,v in ss.items() if v['ref']==ref) for ref in notes.keys()} for e in []):pass
scope={k for k,v in ss.items() if v['ref'] in exp['fully_reviewed_core_refs']+exp['fully_reviewed_context_refs']}
for q in active:
 if q['layer']=='questions' and q['content']['answer_set_status']=='none' and any(e['segment_id'] in scope for e in q['evidence']):
  edges=[e for e in active if e['layer']=='edges' and e['content']['relation']=='answer' and e['content']['target_id']==q['id']]
  if edges:unc.append(dict(question=q,answer_edges=edges,answers=[pi[e['content']['source_id']] for e in edges]))
assert len(unc)==9
write('answer_status_uncertainty.json',unc)
print('written:91 claim correspondences,360 layer comparisons,45 ref adapter,9 bounded field uncertainties')
