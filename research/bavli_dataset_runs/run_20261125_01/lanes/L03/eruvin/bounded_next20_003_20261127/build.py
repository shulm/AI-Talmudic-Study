import copy,json,sys
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin');base=runner.current(job)
assert runner.sha(runner.encoded(base))=='cb92523c062f1452d686f8be68d35ca9a4961aeadbd0a9603eba66f356f625b2';runner.authorize(job,'L03/eruvin',2);j,src=runner.load(job);seg=list(src.values());old={r['id']:r for r in base['records'] if r['release_state']=='valid'}
coord=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study');active=runner.read(coord/'research/bavli_dataset_runs/ACTIVE_RUN.json');contract=runner.read(coord/active['contract_path']);assert runner.sha((coord/active['contract_path']).read_bytes())==active['contract_sha256']
for f,h in contract['production_files'].items():assert runner.sha((root/f).read_bytes())==h
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/eruvin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=[],coverage=[],open_tails=['er023.combination_structure']);repl={}
def ev(i):
 s=seg[i];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(k,l,inds,c,links=None,u=None,origin='source_paraphrase',sup=None):
 rid='er023.'+k;r=dict(id=rid,layer=l,evidence=[ev(i) for i in inds],content=c,links=links or [],uncertainty=u or [],origin=origin)
 if sup:r['supersedes']=sup;repl[sup]=rid
 p['records'].append(r);return rid
def cl(k,inds,txt,holder='anonymous Gemara',cond=None,mode='asserted',u=None,sup=None):
 c=rec(k,'claims',inds,dict(proposition=txt,conditions=cond or [],scope='Local enclosure or authority-combination discussion; distinct stages and reported versions',assertion_mode=mode),u=u,sup=sup)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder] if holder else [],claim_id=c,question_id=None,conditions=cond or [],local_status=mode+' at cited stage; later qualifications separately linked'),[c],u,sup=sup+'.p' if sup and sup+'.p' in old else None);return c
def q(k,inds,txt):return rec(k,'questions',inds,dict(formulation=txt,question_origin='explicit',conditions=[],answer_set_status='partial'))
def e(k,inds,a,b,rel='support'):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
def at(k,inds,surface,who,scope,role='speaker',chain=None,u=None):return rec(k,'attributions',inds,dict(surface=surface,role=role,candidates=who,scope=scope,transmission_chain=chain or []),u=u)
def clean(r):return {k:copy.deepcopy(v) for k,v in r.items() if k not in ['release_state','review_state','ml_eligible']}
closed=clean(old['er022.public_structure']);closed.update(id='er023.public_closed',supersedes='er022.public_structure');closed['evidence'] += [ev(i) for i in range(150,160)];closed['content']['boundary']='closed';p['records'].append(closed);repl['er022.public_structure']=closed['id']
rec('combination_structure','structure',list(range(160,170)),dict(title='Nehardea combined rulings, consistent authority and alternative resolutions; continuation follows',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference')
roles={150:'Public-domain enclosure challenge; quoted Yehuda introduction crosses folio',151:'Two-house paired lehi/beam options and sages objection',152:'Door hypothesis challenged by Yohanan Jerusalem report',153:'Ulla Mehoza parallel counterfactual',154:'Rav Yehuda corrects baraita to open-through alleys',155:'Rav first-tanna versus Shmuel Hananya rulings',156:'Locking question, two Shmuel reports and Matna incident variant',157:'Rav Anan asked and cites Shmuel non-objection to buried gates',158:'Rav Kahana closed-gate qualification',159:'Rav Nahman clearing dirt; actual locking distinguished from capability',160:'Nehardea combined stringencies and Rav first-tanna objection',161:'Shmuel Hananya explanation challenged by his closed-alley rule',162:'Combining stringencies question and consistent-school baraita',163:'Internal contradiction in always-Beit-Hillel versus choice',164:'Before/after heavenly voice resolution',165:'Alternative both-after-voice interpretation begins',166:'Crossfolio alternative is Rabbi Yehoshua ignoring heavenly voice',167:'Alternative generalization to two disputing tannaim or amoraim',168:'Original combined-stringency difficulty remains',169:'Nahman bar Yitzhak all-Rav resolution via Huna no-public-instruction version'}
for i,role in roles.items():
 rec('u'+str(i),'utterances',[i],dict(textual_voice='Gemara or quoted baraita with separate named voices',discourse_role=role,composition='composite'));at('frame'+str(i),[i],'anonymous framing',[],role,'anonymous')
# Refine promoted context without discarding its initial records.
rawu=['Quoted baraita prints א"ר יהודה; a Rabbi Yehuda expansion follows tannaitic context but is not independently pinned. Retain raw title and distinguish explicit Rav Yehuda at6b4.']
lehi=cl('yehuda_lehi',[150,151],'The quoted speaker א"ר יהודה permits carrying between opposite houses using a lehi at each end.','יהודה (quoted baraita; title abbreviated)',cond=['Two houses across public domain'],u=rawu,sup='er022.ry_public')
beam=cl('yehuda_beam',[150,151],'The quoted speaker א"ר יהודה permits carrying between opposite houses using a beam at each end.','יהודה (quoted baraita; title abbreviated)',cond=['Two houses across public domain'],u=rawu)
at('yehuda_baraita',[150,151],'א"ר יהודה',['יהודה (quoted baraita; title abbreviated)'],'Two alternative enclosure devices; no identity collapse with Rav Yehuda','quoted_authority',u=rawu)
e('beam_sages_objection',[151],'er022.sages_public',beam,'objection')
doorq=q('public_door_q',[152],'Could doors enclose public domain, though lehi or beam cannot?');e('jerusalem_door_answer',[152],'er022.jerusalem',doorq,'objection');e('mehoza_door_answer',[153],'er022.mehoza',doorq,'objection')
corrected_remedy=cl('corrected_remedy',[154],'For the corrected case of alleys opening onto public domain, use an entrance-form at one end and a lehi or beam at the other.','Rav Yehuda',cond=['Corrected baraita domain','Later road/plaza/field scope retained'])
e('remedy_repeats',[149,154],corrected_remedy,'er022.first_tanna','quotation')
for key in ['street_scope','plaza_scope','street_field','field_field']:e('remedy_scope_'+key,[154,177,178],'er022fix.'+key,corrected_remedy,'qualification')
at('rav_ruling',[155],'רב אמר',['Rav'],'Rules first tanna');at('shmuel_ruling',[155],'שמואל אמר',['Shmuel'],'Rules Hananya')
matna_case=cl('matna_personal_case',[156],'In the alternative version, Rav Matna says the case happened to him and Shmuel told him no locking was required.','Rav Matna',cond=['איכא דאמרי reporting variant'])
e('matna_same_ruling',[156],matna_case,'er022.shmuel_no_lock','quotation')
annanq=q('annan_q',[157],'They asked Rav Anan whether locking was required.');e('annan_answer',[157],'er022.annan_observation',annanq,'answer');at('annan.a',[157],'רב ענן',['Rav Anan'],'Responds by observed gates and Shmuel non-objection')
kahana=cl('kahana_closed',[158],'Rav Kahana says those gates were closed (מגופות).','Rav Kahana',u=['Closed is not equated here with locked; the qualification does not erase the later capability requirement.'],sup='er022.kahana_qualification')
at('kahana.a',[158],'רב כהנא',['Rav Kahana'],'Closed-gate qualification')
nahmanq=q('nahman_lock_q',[159],'Does Rav Nahman’s dirt-clearing order imply that actual locking is required?');e('nahman_answer',[159],'er022.capable_lock',nahmanq,'answer');at('nahman.a',[159],'רב נחמן',['Rav Nahman'],'Dirt-clearing order, not Rav Nahman bar Yitzhak')
ravq=q('rav_consistency_q',[160],'How can the doors requirement be Rav’s stringency when Rav rules according to the first tanna?')
shmuelq=q('shmuel_consistency_q',[161],'How can the doors requirement be attributed to Shmuel when he treats a bent alley as closed?')
doors_from_shmuel=cl('doors_shmuel',[161],'The doors requirement is assigned to Shmuel’s Hananya ruling in the combined account.')
through_from_rav=cl('through_rav',[161],'The through-alley treatment is assigned to Rav in the combined account.')
e('rav_consistency_answer',[161],doors_from_shmuel,ravq,'answer');e('shmuel_consistency_answer',[161],through_from_rav,shmuelq,'answer')
e('doors_combined',[160,161],doors_from_shmuel,'er022.nehardea_combined');e('through_combined',[160,161],through_from_rav,'er022.nehardea_combined')
bh=cl('always_bh',[162],'The baraita states that the law always follows Beit Hillel.','quoted baraita',cond=['Timing and alternate interpretations below qualify application'])
choosebs=cl('choose_bs',[162],'The baraita permits one who wishes to act according to Beit Shammai to do so.','quoted baraita',cond=['Consistent leniencies and stringencies; timing/interpretation alternatives follow'])
choosebh=cl('choose_bh',[162],'The baraita permits one who wishes to act according to Beit Hillel to do so.','quoted baraita',cond=['Consistent leniencies and stringencies'])
mixlen=cl('mixed_leniencies',[162],'The baraita calls one combining both schools’ leniencies wicked.','quoted baraita')
mixstrict=cl('mixed_strict',[162],'The baraita applies the fool-walking-in-darkness verse to combining both schools’ stringencies.','quoted baraita',cond=['Later contradictory-stringency limitation retained'])
consbs=cl('consistent_bs',[162],'One following Beit Shammai should follow its leniencies and stringencies.','quoted baraita')
consbh=cl('consistent_bh',[162],'One following Beit Hillel should follow its leniencies and stringencies.','quoted baraita')
e('baraita_mix_objection',[162],mixstrict,'er022.nehardea_combined','objection')
internal=q('internal_q',[163],'How does always following Beit Hillel fit the permission to choose Beit Shammai?')
e('choice_tension',[163],choosebs,bh,'objection')
before=cl('before_voice',[164],'The permission to choose applies before the heavenly voice.','anonymous Gemara',cond=['First reconciliation'])
after=cl('after_voice',[164],'The always-Beit-Hillel rule applies after the heavenly voice.','anonymous Gemara',cond=['First reconciliation'])
e('before_scope',[164],before,choosebs,'qualification');e('after_scope',[164],after,bh,'qualification');e('time_answer',[164],before,internal,'answer')
both_after=cl('both_after',[165,166],'An alternative places both clauses after the heavenly voice and identifies the choice position with Rabbi Yehoshua.','anonymous Gemara',cond=['Alternative reconciliation'])
ignore=cl('yehoshua_ignores',[166],'Rabbi Yehoshua does not heed the heavenly voice.','Rabbi Yehoshua as characterized by the Gemara')
e('ignore_reason',[165,166],ignore,both_after);e('both_after_answer',[165,166],both_after,internal,'answer');at('yehoshua.a',[166],'רבי יהושע',['Rabbi Yehoshua'],'Alternative after-voice reconciliation')
general=cl('two_authorities',[167],'Another interpretation applies the consistent-choice rule generally to two disagreeing tannaim or amoraim analogous to Beit Shammai and Beit Hillel.','anonymous Gemara',cond=['Third interpretation'])
general_len=cl('general_no_len',[167],'In that two-authority setting one must not combine the leniencies of each.','anonymous Gemara',cond=['Third interpretation'])
general_strict=cl('general_no_strict',[167],'In that two-authority setting one must not combine the stringencies of each.','anonymous Gemara',cond=['Third interpretation; later noncontradictory exception retained'])
general_one=cl('general_one',[167],'One should act according to one authority’s leniencies and stringencies.','anonymous Gemara',cond=['Either authority consistently'])
e('general_answer',[167],general,internal,'answer');e('general_len_scope',[167],general,general_len,'qualification');e('general_strict_scope',[167],general,general_strict,'qualification')
still=q('still_q',[168],'Nevertheless, how is the combined Nehardea stringency justified?');e('allrav_still_answer',[169],'er022.all_rav',still,'answer')
at('nahman_yitzhak.a',[143,169],'ר"נ בר יצחק',['Rav Nahman bar Yitzhak'],'All-Rav account; full name explicit earlier at6a5',u=['Abbreviation at7a4 is linked to explicit earlier name, not conflated with Rav Nahman.'])
for key in ['mixed_strict','general_no_strict']:
 e(key+'_contradiction_scope',[171],'er022.contradict_strict','er023.'+key,'qualification');e(key+'_compatible_scope',[174],'er022.compatible_strict','er023.'+key,'qualification')
adaq=q('ada_q',[170],'How is the case explained under Rav Ada bar Ahava’s version that Rav permits public instruction?');e('shizbi_ada_answer',[171,174],'er022.contradict_strict',adaq,'answer')
# Retain source examples needed to understand contradictory stringencies, without counting them as cores.
for k,txt,holder,cond in [('spine_bs','The spinal deficiency threshold is two vertebrae.','Beit Shammai',['Spinal deficiency']),('spine_bh','The spinal deficiency threshold is one vertebra.','Beit Hillel',['Spinal deficiency']),('skull_bs','The skull deficiency threshold is a drill-hole size.','Beit Shammai',['Skull deficiency']),('skull_bh','The skull deficiency threshold is an amount whose removal from a living being would cause death.','Beit Hillel',['Skull deficiency'])]:cl(k,[172],txt,holder,cond)
terefah=cl('terefah',[173],'Shmuel’s reported teaching applies the same distinctions to terefah.','Shmuel reported by Rav Yehuda')
at('terefah_chain',[173],'רב יהודה אמר שמואל',['Rav Yehuda'],'Parallel terefah application','transmitter',['Rav Yehuda','Shmuel'])
akivaq=q('akiva_q',[175],'If contradictory stringencies are forbidden, how did Rabbi Akiva take two tithes for the etrog gathered on the first of Shevat?');e('akiva_answer',[176],'er022.akiva_uncertainty',akivaq,'answer')
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
   n=clean(r);n.update(id='er023.dep.'+oid,supersedes=oid);p['records'].append(n);repl[oid]=n['id'];changed=True
 if not changed:break
for r in p['records']:r['links']=remap(r['links']);r['content']=remap(r['content'])
live={rid:r for rid,r in old.items() if rid not in repl};live.update({r['id']:r for r in p['records']})
for cell in base['coverage']:
 ids=sorted(rid for rid,r in live.items() if (cell['layer']=='reconciliation' or r['layer']==cell['layer']) and any(e['segment_id']==cell['segment_id'] for e in r['evidence']))
 if set(ids)!=set(cell['record_ids']):
  n={k:copy.deepcopy(v) for k,v in cell.items() if k!='proposal_execution'};n['record_ids']=ids;n['rationale']+=' Promoted context split into distinct devices and qualified abbreviated attribution; dependencies preserved.';p['coverage'].append(n)
for i in range(150,170):
 for layer in runner.LAYERS:
  ids=[rid for rid,r in live.items() if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=roles[i]+'. Actual '+layer+' pass and omission reread. Mixed-stringency continuation through7a11, road/plaza/field scope through7a15 and later alley discussion through8b5 inspected; only twenty original cores counted. Prior context reused; individual alternatives and transmissions preserved.'))
runner.validate_apply(base,p,src,j);runner.immutable(out/'PROPOSAL.json',runner.encoded(p));runner.immutable(out/'PINS.json',runner.encoded(dict(base_snapshot=runner.sha(runner.encoded(base)),active_run=active,contract_sha256=active['contract_sha256'],production_git_commit=contract['production_git_commit'],source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],owner=runner.read(job/'OWNER.json'),core_refs=[seg[150]['ref'],seg[169]['ref']],core_indices=[seg[150]['source_index'],seg[169]['source_index']],next_ref=seg[170]['ref'],new_rows=len(p['records']),replacements=repl,exposure='Root ongoing producer; prior002context openly reused. Independent003 source reading remains unopened before initial freeze.')))
print(json.dumps(dict(proposal=runner.sha((out/'PROPOSAL.json').read_bytes()),rows=len(p['records']),superseded=len(repl))))
