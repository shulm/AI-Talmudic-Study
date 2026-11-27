import copy,json,sys
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');base=runner.current(job)
assert runner.sha(runner.encoded(base))=='ca7b86f00e4ee8fc4a5392ec7edee933d7eb3d52ad48b37b4fdc90eb15951c1e';runner.authorize(job,'/root/lead_l01_l03',1);j,src=runner.load(job);seg=list(src.values());old={r['id']:r for r in base['records'] if r['release_state']=='valid'}
coord=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study');active=runner.read(coord/'research/bavli_dataset_runs/ACTIVE_RUN.json');contract=runner.read(coord/active['contract_path']);assert runner.sha((coord/active['contract_path']).read_bytes())==active['contract_sha256']
for f,h in contract['production_files'].items():assert runner.sha((root/f).read_bytes())==h
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='/root/lead_l01_l03',epoch=1,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=[],coverage=[],open_tails=[]);repl={}
def ev(i):
 s=seg[i];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(k,l,inds,c,links=None,u=None,origin='source_paraphrase',sup=None):
 rid='tam007.'+k;r=dict(id=rid,layer=l,evidence=[ev(i) for i in inds],content=c,links=links or [],uncertainty=u or [],origin=origin)
 if sup:r['supersedes']=sup;repl[sup]=rid
 p['records'].append(r);return rid
def cl(k,inds,txt,holder='anonymous Gemara',cond=None,mode='asserted',u=None,sup=None):
 c=rec(k,'claims',inds,dict(proposition=txt,conditions=cond or [],scope='Local exaggeration, altar wood, or fire-arrangement discussion; textual assertion, not external historical validation',assertion_mode=mode),u=u,sup=sup)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder] if holder else [],claim_id=c,question_id=None,conditions=cond or [],local_status=mode+' at cited stage'),[c],u,sup=sup+'.p' if sup and sup+'.p' in old else None);return c
def q(k,inds,txt):return rec(k,'questions',inds,dict(formulation=txt,question_origin='explicit',conditions=[],answer_set_status='partial'))
def e(k,inds,a,b,rel='support'):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
def at(k,inds,surface,who,scope,role='speaker',chain=None,u=None):return rec(k,'attributions',inds,dict(surface=surface,role=role,candidates=who,scope=scope,transmission_chain=chain or []),u=u)
def clean(r):return {k:copy.deepcopy(v) for k,v in r.items() if k not in ['release_state','review_state','ml_eligible']}
closed=clean(old['tam006.exaggeration_structure']);closed.update(id='tam007.exaggeration_closed',supersedes='tam006.exaggeration_structure');closed['evidence'] += [ev(i) for i in range(90,99)];closed['content']['boundary']='closed';p['records'].append(closed);repl['tam006.exaggeration_structure']=closed['id']
for k,inds,title in [('woods_structure',list(range(99,107)),'Wood exclusions, alternative reasons and fruitless-tree explanation'),('orientation_structure',[107,108],'Two unnamed orientation reasons and multiple lighting places'),('chapter_marker',[109],'Preserved chapter-end heading')]:rec(k,'structure',inds,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
roles={90:'Torah heaven-height exaggeration example and rhetorical question',91:'Repeated sages examples: mound and gold cup',92:'Prophetic earth-splitting example',93:'Shmuel transmitted three-case list',94:'Explicit exclusion of Rava gold-cup claim and wealth maxim',95:'Golden vine installation and donation sentence begins',96:'Donation alternatives and Elazar son of Tzadok report',97:'Curtain construction and transmission chain',98:'Curtain measurements, production frequency and immersion number',99:'Wood-exclusion question and two named explanations',100:'Baraita wood-quality objection and definition',101:'Repeated usual woods and Eliezer additional species',102:'Internal/external knots distinction explains disagreement',103:'Land-settlement challenge from date palm',104:'Counterchallenge from fig and fruitless-tree reconciliation',105:'Existence of fruitless fig questioned; Rahava technique begins',106:'Crossfolio cultivation technique and timber outcome',107:'Arrangement orientation question; unnamed Huna/Hisda alternatives',108:'Lighting-gap objection and multiple-place answer',109:'Nonempty chapter-end heading; no legal claim'}
for i,role in roles.items():
 rec('u'+str(i),'utterances',[i],dict(textual_voice='Chapter heading' if i==109 else 'Gemara, quoted Mishnah or baraita; named voices separately attributed',discourse_role=role,composition='atomic' if i==109 else 'composite'))
 if i!=109:at('frame'+str(i),[i],'anonymous framing',[],role,'anonymous')
# Already reviewed contextual claims and transmissions are reused rather than recreated.
heavenq=q('heaven_q',[90],'Could the fortified cities literally reach the heavens?');e('heaven_answer',[90],'tam006.heaven_hyper',heavenq,'answer')
prophet=cl('prophetic_hyper',[92],'The prophetic earth-splitting expression is an example of exaggeration.','Rabbi Ami’s classification as illustrated by the Gemara');e('earth_hyper',[92],prophet,'tam006.earth_verse','qualification');e('prophet_example',[92],prophet,'tam006.ami_prophets')
for k,txt,inds in [('vine_gold','A golden vine stood at the entrance of the sanctuary.',[95]),('vine_trellis','The vine was trained over poles.',[95]),('donate_leaf','One who donated a leaf brought it and hung it on the vine.',[95,96]),('donate_grape','One who donated a grape brought it and hung it on the vine.',[96]),('donate_cluster','One who donated a cluster brought it and hung it on the vine.',[96])]:cl(k,inds,txt,'quoted baraita')
for k,txt,inds in [('curtain_thick','The curtain was one handbreadth thick.',[97]),('curtain_strands','It was woven on seventy-two strands.',[97]),('curtain_threads','Each strand had twenty-four threads.',[97]),('curtain_length','Its length was forty cubits.',[98]),('curtain_width','Its width was twenty cubits.',[98]),('curtain_amount','The account says ומשמונים ושתים ריבוא נעשית.',[98]),('curtain_year','Two curtains were made each year.',[98])]:cl(k,inds,txt,'Rabban Shimon ben Gamliel reporting Rabbi Shimon the deputy',u=['The unit or referent of eighty-two myriads is not specified in this local phrase; no cost or worker count inferred.'] if k=='curtain_amount' else None)
# New wood-quality proof and full conditional contrast; retain source terms where gloss uncertain.
woodverse=cl('wood_verse',[100],'The baraita interprets על העצים אשר על האש as wood suitable to become fire.','quoted baraita')
woodquality=q('wood_quality_q',[100],'What wood is meant by the baraita’s description?')
skewer=cl('skewer_wood',[100],'The answer identifies דוקרי שפוד without internal קטרי that smoke from within.','anonymous Gemara',u=['Source terminology retained; no botanical species identification added.'])
e('wood_quality_answer',[100],skewer,woodquality,'answer')
woodrepeat=cl('wood_repeat',[101],'The cited baraita repeats that all woods are suitable except olive and vine.','quoted baraita',cond=['Later fruitless-tree explanation qualifies land-settlement rationale'])
e('wood_repetition',[84,101],woodrepeat,'tam006.all_woods','quotation')
for k,oldkey,txt in [('fig_repeat','fig_usual','Fig branches are among the customary woods.'),('nut_repeat','nut_usual','Nut-tree branches are among the customary woods.'),('oil_repeat','oil_usual','Etz shemen branches are among the customary woods.')]:
 c=cl(k,[101],txt,'quoted baraita',u=['Repeated baraita occurrence retained separately; not an additional unique rule.']);e(k+'_quotation',[84,101],c,'tam006.'+oldkey,'quotation')
for k,raw in [('maish','מייש'),('oak','אלון'),('palm','דקל'),('carob','חרוב'),('sycamore','שקמה')]:cl('eliezer_'+k,[101],'Rabbi Eliezer adds '+raw+' to the woods used.','Rabbi Eliezer',u=['Hebrew species name retained without an external botanical identification.'])
at('eliezer.a',[101],'רבי אליעזר',['Rabbi Eliezer'],'Additional species in baraita','quoted_authority')
restrict=cl('external_knots_restrict',[102],'The restrictive explanation excludes wood with external קטרי even when it lacks internal קטרי.','restrictive view in baraita explanation',cond=['No internal קטרי','External קטרי'],u=['The two מר סבר clauses are kept by condition; no unsupported name-order assignment.'])
permit=cl('external_knots_permit',[102],'The permissive explanation allows wood without internal קטרי even if external קטרי are present.','permissive view in baraita explanation',cond=['No internal קטרי','External קטרי'],u=['Source conditional contrast retained without resolving botanical effects.'])
e('wood_conditional_difference',[102],permit,restrict,'distinction');e('knot_explanation',[99,102],'tam006.wood_knots',restrict);e('knot_explanation_second',[99,102],'tam006.wood_knots',permit)
palmq=q('palm_q',[103],'Under the land-settlement explanation, does palm not also matter to settlement of the Land of Israel?')
palmproblem=cl('palm_settlement',[103],'Palm use presents a difficulty for the land-settlement explanation.','anonymous Gemara',mode='challenged');e('palm_objection',[103],palmproblem,'tam006.wood_settlement','objection')
figq=q('fig_q',[104],'By that reasoning, does fig not also matter to settlement of the Land of Israel?')
fruitfig=cl('fruitless_fig',[104],'The fig trees used in this explanation are those that do not produce fruit.','reply defending land-settlement explanation',cond=['Explanation of fig use'],sup='tam006.fruitless')
fruitpalm=cl('fruitless_palm',[104],'The palm trees used in this explanation likewise do not produce fruit.','reply defending land-settlement explanation',cond=['Explanation of palm use'])
e('fig_answer',[104],fruitfig,figq,'answer');e('palm_answer',[104],fruitpalm,palmq,'answer');e('palm_qualifies',[101,104],fruitpalm,'tam007.eliezer_palm','qualification');e('palm_settlement_scope',[104],fruitpalm,'tam006.wood_settlement','qualification');e('fig_repeated_scope',[101,104],fruitfig,'tam007.fig_repeat','qualification')
exists=q('fruitless_exists',[105],'Do fig trees that produce no fruit exist?')
yes=cl('fruitless_exists_yes',[105],'The answer affirms their existence by citing Rahava’s method.','anonymous Gemara')
e('exists_answer',[105],yes,exists,'answer')
at('rahava.a',[105,106],'רחבה דאמר רחבה',['Rahava (רחבה as printed)'],'Reported cultivation procedure; not Rabbah','quoted_authority')
for k,txt,inds in [('white_fig','Rahava describes bringing white fig plants.',[105]),('rope','They apply a palm-fibre rope to which seed adheres.',[106]),('bury','They bury them where the sea deposits alluvium.',[106]),('timber','The resulting growth produces timber.',[106]),('no_fruit','It does not produce fruit.',[106]),('camel','A camel cannot carry three beams from such growth.',[106])]:cl(k,inds,txt,'Rahava',u=['Local account retained as reported source, not independently verified cultivation or load measurement.'])
e('no_fruit_proof',[105,106],'tam007.no_fruit',yes);e('timber_fig',[106],'tam007.timber',fruitfig,'support')
# Existing wind/kindling alternatives, question, multiple-places answer and unresolved attribution reused.
at('orientation_unassigned',[107],'חד אמר ... וחד אמר',['Rav Huna','Rav Hisda'],'No named assignment for either wind or kindling reason; continuation does not settle it',u=['Candidate pair is not a claim that both taught both reasons.'])
def remap(v):
 if isinstance(v,str):return repl.get(v,v)
 if isinstance(v,list):return [remap(x) for x in v]
 if isinstance(v,dict):return {k:remap(x) for k,x in v.items()}
 return v
while True:
 changed=False
 for oid,r in old.items():
  if oid in repl:continue
  if remap(r['links'])!=r['links'] or remap(r['content'])!=r['content']:
   n=clean(r);n.update(id='tam007.dep.'+oid,supersedes=oid);p['records'].append(n);repl[oid]=n['id'];changed=True
 if not changed:break
for r in p['records']:r['links']=remap(r['links']);r['content']=remap(r['content'])
live={rid:r for rid,r in old.items() if rid not in repl};live.update({r['id']:r for r in p['records']})
for cell in base['coverage']:
 ids=sorted(rid for rid,r in live.items() if (cell['layer']=='reconciliation' or r['layer']==cell['layer']) and any(e['segment_id']==cell['segment_id'] for e in r['evidence']))
 if set(ids)!=set(cell['record_ids']):
  n={k:copy.deepcopy(v) for k,v in cell.items() if k!='proposal_execution'};n['record_ids']=ids;n['rationale']+=' New continuation closes exaggeration unit and separates fruitless fig/palm scopes.';p['coverage'].append(n)
for i in range(90,110):
 for layer in runner.LAYERS:
  ids=[rid for rid,r in live.items() if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else ('not_applicable' if i==109 else 'none_found_after_pass'),record_ids=ids,rationale=roles[i]+'. Actual '+layer+' pass and raw omission reread through chapter boundary30a4; nextMishnah30a5–7 inspected. Prior context reused; fruitless fig/palm atomized with immutable revisions. Twenty original cores including heading, no shifted references.'))
runner.validate_apply(base,p,src,j);runner.immutable(out/'PROPOSAL.json',runner.encoded(p));runner.immutable(out/'PINS.json',runner.encoded(dict(base_snapshot=runner.sha(runner.encoded(base)),active_run=active,contract_sha256=active['contract_sha256'],production_git_commit=contract['production_git_commit'],source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],owner=runner.read(job/'OWNER.json'),core_refs=[seg[90]['ref'],seg[109]['ref']],core_indices=[seg[90]['source_index'],seg[109]['source_index']],next_ref=seg[110]['ref'],new_rows=len(p['records']),replacements=repl,exposure='Root ongoing producer; earlier006context openly reused. Independent007 source reading remains unopened before initial freeze.')))
print(json.dumps(dict(proposal=runner.sha((out/'PROPOSAL.json').read_bytes()),rows=len(p['records']),superseded=len(repl))))
