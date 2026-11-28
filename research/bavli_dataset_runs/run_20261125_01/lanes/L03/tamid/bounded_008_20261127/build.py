import copy,json,sys
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');base=runner.current(job)
assert runner.sha(runner.encoded(base))=='35bb1acb1f779ee16a8009686c416cc82473636665062f23710af1119073745e';runner.authorize(job,'/root/lead_l01_l03',1);j,src=runner.load(job);seg=list(src.values());old={r['id']:r for r in base['records'] if r['release_state']=='valid'}
coord=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study');active=runner.read(coord/'research/bavli_dataset_runs/ACTIVE_RUN.json');contract=runner.read(coord/active['contract_path']);assert runner.sha((coord/active['contract_path']).read_bytes())==active['contract_sha256']
for f,h in contract['production_files'].items():assert runner.sha((root/f).read_bytes())==h
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='/root/lead_l01_l03',epoch=1,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=[],coverage=[],open_tails=['tam008.slaughter_structure']);repl={}
def ev(i):
 s=seg[i];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(k,l,inds,c,links=None,u=None,origin='source_paraphrase',sup=None):
 rid='tam008.'+k;r=dict(id=rid,layer=l,evidence=[ev(i) for i in inds],content=c,links=links or [],uncertainty=u or [],origin=origin)
 if sup:r['supersedes']=sup;repl[sup]=rid
 p['records'].append(r);return rid
def cl(k,inds,txt,holder='anonymous Gemara',cond=None,mode='asserted',u=None,sup=None):
 c=rec(k,'claims',inds,dict(proposition=txt,conditions=cond or [],scope='Local daily-offering procedure and source reports; not external historical validation',assertion_mode=mode),u=u,sup=sup)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder] if holder else [],claim_id=c,question_id=None,conditions=cond or [],local_status=mode+' at cited stage'),[c],u,sup=sup+'.p' if sup and sup+'.p' in old else None);return c
def q(k,inds,txt):return rec(k,'questions',inds,dict(formulation=txt,question_origin='explicit',conditions=[],answer_set_status='partial'))
def e(k,inds,a,b,rel='support'):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
def at(k,inds,surface,who,scope,role='speaker',chain=None,u=None):return rec(k,'attributions',inds,dict(surface=surface,role=role,candidates=who,scope=scope,transmission_chain=chain or []),u=u)
def clean(r):return {k:copy.deepcopy(v) for k,v in r.items() if k not in ['release_state','review_state','ml_eligible']}

for k,inds,title,bound in [('preparation_structure',list(range(110,127)),'Lottery, preparation, Temple entry and cleaning procedures','closed'),('heading',[127],'Chapter-end heading retained','closed'),('slaughter_structure',[128,129],'Binding, slaughter position and ensuing dissection; context read through31b14','open_right')]:rec(k,'structure',inds,dict(title=title,primary=True,boundary=bound,legacy_ids=[]),origin='editorial_inference')
roles={110:'Officer summons lottery for distinct duties',111:'Lottery portions and accompanying offerings',112:'Lottery result',113:'Dawn inspection and Matya ben Shmuel formulation',114:'Lamb retrieval and four chambers',115:'Ninety-three silver/gold vessels and drinking cup begins',116:'Gold cup continuation; repeat inspection despite evening examination',117:'Early cleaning workers, four tools and two key operations',118:'Northern wicket access; southern closure and Ezekiel quotation',119:'Opening route and prerequisite for slaughter',120:'Five Jericho sound reports',121:'Additional sounds, repeated song occurrence and some-say high-priest voice',122:'Incense smell and Elazar ben Diglai report',123:'Lamb movement, companions and slaughterhouse fittings',124:'Inner altar ash removal sequence',125:'Conditional lamp cleaning and rekindling sequence',126:'Three-step stone and vessel placement',127:'Chapter-end heading',128:'Binding distinction, holders and orientation',129:'Morning versus afternoon slaughter location'}
for i,role in roles.items():
 rec('u'+str(i),'utterances',[i],dict(textual_voice='Chapter heading' if i==127 else 'Mishnah with scoped named and anonymous reported voices',discourse_role=role,composition='atomic' if i==127 else 'composite'))
 if i!=127:at('frame'+str(i),[i],'anonymous Mishnah',[],role,'anonymous')
def m(k,inds,t,cond=None,u=None):return cl(k,inds,t,'anonymous Mishnah',cond=cond,u=u)
for k,t in [('slaughter','slaughtering'),('sprinkle','sprinkling blood'),('inner_ash','removing ashes from the inner altar'),('lamps','cleaning the menorah'),('limbs','bringing limbs up to the ramp')]:m('lot_'+k,[110],'The officer summons a lottery assigning '+t+'.')
for k,t in [('head_rightleg','head and right hind leg'),('forelegs','two forelegs'),('tail_leftleg','tail and left hind leg'),('chest_neck','chest and neck portion'),('sides','two sides'),('innards','innards'),('flour','fine flour'),('griddle','griddle cakes'),('wine','wine')]:m('lotportion_'+k,[111],'The allocation list includes '+t+'.')
m('lot_result',[112],'They hold the lottery and the winner receives the allotted duty.')
m('dawn_check',[113],'The officer sends them to see whether the time for slaughter has arrived.')
m('barkai',[113],'When the time has arrived, the observer says ברקאי.',['Time for slaughter has arrived'])
matya=cl('matya_dawn',[113],'Matya ben Shmuel says: the face of the entire east has lit as far as Hebron.','Matya ben Shmuel',u=['Preserve formulation; do not infer identity of the responding person.'])
at('matya.a',[113],'מתיא בן שמואל',['Matya ben Shmuel'],'Alternative dawn-check formulation','quoted_authority')
m('dawn_yes',[113],'The account adds והוא אומר הן, an affirmative response.',['Within dawn check'],u=['The local pronoun is not assigned to a named individual.'])
m('bring_lamb',[114],'The officer directs retrieval of a lamb from the lamb chamber.',u=['Parenthetical לי והוציאו is preserved in evidence without selecting an edition.'])
m('lamb_chamber',[114],'The lamb chamber is situated in the northwestern corner.');m('four_chambers',[114],'There were four chambers there.')
for k,t in [('lamb','lambs'),('seals','seals'),('fire','Beit Hamoked'),('bread','making the showbread')]:m('chamber_'+k,[114],'One of the four chambers is for '+t+'.')
m('vessels',[115],'They enter the vessel chamber and take out ninety-three silver and gold vessels.',u=['Ninety-three is the total expressed; no separate metal subtotals inferred.'])
m('gold_cup',[115,116],'They give the daily-offering lamb drink from a gold cup.',u=['Cup material crosses original folio boundary; no reference shift.'])
m('reinspect',[116],'Although examined the previous evening, the lamb is examined again by torchlight.',['Prior evening examination does not remove this inspection'])
m('cleaners_early',[117],'The winners of inner-altar and menorah cleaning go ahead early.');m('four_tools',[117],'They carry four tools: טני, כוז and two keys.')
m('teni_shape',[117],'The טני resembles a gold תרקב.');m('teni_capacity',[117],'The טני holds two and a half kav.');m('kuz_shape',[117],'The כוז resembles a large gold jug.')
m('key_down',[117],'One key is described as יורד באמת השחי.',u=['Exact operation wording retained without speculative mechanical reconstruction.'])
m('key_direct',[117],'The other key is described as פותח כיון.',u=['Source wording retained; precise mechanism unresolved locally.'])
m('north_wicket',[118],'The worker comes to the northern wicket.');m('two_wickets',[118],'The great gate has two wickets, one north and one south.')
south=m('south_unused',[118],'No person enters the southern wicket.')
verse=cl('ezekiel_closed',[118],'The Ezekiel quotation says the gate stays shut, is not opened, and no person enters because the God of Israel entered it.','Ezekiel quotation',u=['Scope is the source’s application to southern wicket, not an independently reconstructed building plan.'])
at('ezekiel.a',[118],'עליו הוא מפורש ע״י יחזקאל',['Ezekiel'],'Scriptural quotation applied to closed southern wicket','quoted_authority');e('southern_proof',[118],verse,south)
for k,t in [('wicket_open','He takes the key and opens the wicket.'),('route','He passes from the wicket into the cell and from the cell into the sanctuary, reaching the great gate.'),('gate_open','At the great gate he removes the bolt and fastenings and opens it.')]:m(k,[119],t)
m('slaughter_wait',[119],'The slaughterer does not slaughter until hearing the great gate opened.',['Audible gate opening precedes slaughter'])
for i,items in [(120,[('gate','great gate opening'),('magrefa','מגריפה'),('song','song'),('arza','Ben Arza striking the cymbal'),('flute','flute')]),(121,[('gevini','Gevini the herald'),('katin','wooden mechanism Ben Katin made for the laver'),('song_repeat','song'),('shofar','shofar')])]:
 for k,t in items:m('jericho_'+k,[i],'From Jericho they heard the sound of '+t+'.',u=['Reported source occurrence, not independently verified acoustic distance.']+(['Repeated song occurrence preserved; no second unique sound inferred.'] if k=='song_repeat' else []))
cl('jericho_high_priest',[121],'Some say even the high priest’s voice when pronouncing the Name on Yom Kippur was heard from Jericho.','some say',cond=['At pronouncing the Name on Yom Kippur'],u=['Alternative additional report, not universal consensus.'])
at('some_say.a',[121],'וי״א',[],'Additional high-priest voice report','anonymous')
m('jericho_incense',[122],'From Jericho they smelled the incense compound.',u=['Source report, not independent geographic validation.'])
cl('goats',[122],'Elazar ben Diglai reports that his father had goats in the towns of Mikhvar which sneezed from the incense smell.','Elazar ben Diglai',u=['Name and place follow this source; no normalization to other witnesses.'])
at('diglai.a',[122],'א״ר אלעזר בן דגלאי',['Elazar ben Diglai'],'First-person father’s goats report','quoted_authority')
m('lamb_lead',[123],'The winner of the daily offering leads the lamb to the slaughterhouse.');m('limb_companions',[123],'The winners of the limbs accompany him.')
for k,t in [('north_altar','The slaughterhouse is north of the altar.'),('eight_posts','There are eight dwarf posts.'),('cedar','Cedar blocks lie on the posts.'),('hooks','Iron hooks are fixed in them.'),('three_rows','There are three rows for each.'),('hang_skin','They hang and flay using these fittings.'),('marble','Marble tables stand between the posts.')]:m(k,[123],t)
for k,t in [('teni_before','The inner-altar cleaner enters, takes the טני and places it before him.'),('ash_hands','He scoops ashes by hand into it.'),('ash_sweep','Finally he sweeps the remainder into it.'),('ash_leave','He leaves it and exits.')]:m(k,[124],t)
for k,t,cond in [('lamps_rest','He cleans the remaining lamps.','The two lamps described מזרחית מערבית are burning'),('lamps_leave','He leaves those two burning in place.','The two lamps described מזרחית מערבית are burning'),('lamps_out_clean','He cleans those two lamps.','He finds those two extinguished'),('lamps_relight','He lights them from the burning lamps.','He finds those two extinguished'),('lamps_after','After relighting them he cleans the rest.','He finds those two extinguished')]:m(k,[125],t,[cond],u=['Printed מזרחית מערבית retained without deciding textual or geometric interpretation.'])
for k,t in [('stone','A stone stands before the menorah.'),('three_steps','The stone has three steps.'),('priest_stands','The priest stands on it to tend the lamps.'),('kuz_second','He leaves the כוז on the second step and exits.')]:m(k,[126],t)
no_bind=m('not_bind',[128],'They do not bind the lamb in the manner termed כופתין.');akeda=m('akeda',[128],'Instead they bind it in the manner termed מעקידין.',u=['Continuation specifies hand and foot; no unsupported modern restraint procedure supplied.'])
m('limb_holders',[128],'Those who won the limbs hold the lamb.')
for k,t in [('head_south','The lamb’s head is toward the south.'),('face_west','Its face is toward the west.'),('slaughterer_east','The slaughterer stands in the east.'),('slaughterer_west','The slaughterer faces west.')]:m(k,[128],t)
m('morning_position',[129],'The morning offering is slaughtered at the northwestern corner on the second ring.',['Morning offering'])
m('afternoon_position',[129],'The afternoon offering is slaughtered at the northeastern corner on the second ring.',['Afternoon offering'])
# Read the complete following Mishnah through31b3 and the binding explanation31b4–6.
cl('context.hand_foot',[143],'The teaching describes a hand and foot, like the binding of Isaac son of Abraham.','cited teaching');e('context.binding_explained',[128,143],'tam008.context.hand_foot',akeda,'qualification')
why=q('context.binding_why',[144],'Why did they not bind the lamb in the prohibited manner?')
at('context.pair',[144],'רב הונא ורב חסדא חד אמר ... וחד אמר',['Rav Huna','Rav Hisda'],'Unassigned alternatives for restraint rationale; continuation does not identify speakers',u=['Do not assign by name order or infer both held both.'])
dignity=cl('context.dignity',[144],'One explanation avoids disgrace to sacred offerings.','one of Rav Huna / Rav Hisda',u=['Named identity unresolved.'])
custom=cl('context.custom',[144],'The other explanation avoids following gentile customs.','other of Rav Huna / Rav Hisda',u=['Named identity unresolved.'])
e('context.dignity_answer',[144],dignity,why,'answer');e('context.custom_answer',[144],custom,why,'answer')
diff=q('context.difference',[145],'What practical difference separates the two explanations?')
for k,t in [('silk','Binding with silk is given as a difference.'),('gold','Alternatively binding with הוצא דדהבא is given as a difference.')]:
 c=cl('context.'+k,[145],t,'anonymous Gemara',u=['Do not invent an explicit named mapping or expand material term beyond source.']);e('context.'+k+'_answer',[145],c,diff,'answer')

marbleq=q('context.marble_q',[150],'Since there is no poverty in a place of wealth, why marble rather than silver or gold tables?')
heat=cl('context.heat',[150],'The reply explains that the alternative material heats the contents.','Rav Hinena in the name of Rabbi Asi, in the name of Rabbi Shmuel bar Rav Yitzhak',u=['Local thermal rationale reported, not independent experimental verification.'])
at('context.heat_chain',[150],'רב חיננא בשם רבי אסי ורבי אסי בשם רבי שמואל בר רב יצחק',['Rav Hinena','Rabbi Asi','Rabbi Shmuel bar Rav Yitzhak'],'Explicit two-link report of heating rationale','transmitter',chain=['Rav Hinena','Rabbi Asi','Rabbi Shmuel bar Rav Yitzhak'])
e('context.marble_answer',[150],heat,marbleq,'answer');e('context.marble_reason',[123,150],heat,'tam008.marble','support')
cl('context.morning_lemma',[151],'The Gemara opening lemma prints the morning offering at the northeastern corner.','quoted lemma',u=['Conflicts with morning northwestern in Mishnah30b14 and baraita31b14; preserve printed reading without harmonization.'])
locationq=q('context.location_q',[151],'From where are these slaughter locations derived?')
day=cl('context.day',[151],'Rav Hisda interprets שנים ליום as opposite the day/sun.','Rav Hisda',u=['Source phrase כנגד היום retained; no detailed astronomy added.'])
at('context.hisda',[151],'אמר רב חסדא',['Rav Hisda'],'Explicit location derivation; does not identify prior unassigned binding view','speaker')
e('context.location_answer',[151],day,locationq,'answer')
bar=cl('context.baraita_day',[152],'The baraita also interprets שנים ליום as opposite the day/sun.','cited baraita')
alt=q('context.day_alt',[152],'Could שנים ליום mean only the daily obligation instead?')
obligation=cl('context.obligation',[152],'The morning and afternoon verse already states the daily obligation.','baraita argument')
e('context.day_alt_answer',[152],obligation,alt,'answer');e('context.day_remaining',[152],obligation,bar,'support');e('context.baraita_support',[151,152],bar,day,'support')
for k,t,orig in [('morning','The baraita specifies morning slaughter at the northwestern corner on the second ring.','morning_position'),('afternoon','The baraita specifies afternoon slaughter at the northeastern corner on the second ring.','afternoon_position')]:
 c=cl('context.'+k,[153],t,'cited baraita',u=['Repeated location occurrence retained; morning lemma31b12 conflict remains unresolved.']);e('context.'+k+'_repeat',[129,153],c,'tam008.'+orig,'quotation');e('context.'+k+'_application',[152,153],bar,c,'support')

live=dict(old);live.update({r['id']:r for r in p['records']})
for i in range(110,130):
 for layer in runner.LAYERS:
  ids=[rid for rid,r in live.items() if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else ('not_applicable' if i==127 else 'none_found_after_pass'),record_ids=ids,rationale=roles[i]+'. Actual '+layer+' pass with raw-source omission check; continuation through31b14 read and binding reasons extracted without context coverage. Original positions and chapter heading retained. No invented questions or argument edges for procedural lists.'))
runner.validate_apply(base,p,src,j);runner.immutable(out/'PROPOSAL.json',runner.encoded(p));runner.immutable(out/'PINS.json',runner.encoded(dict(base_snapshot=runner.sha(runner.encoded(base)),active_run=active,contract_sha256=active['contract_sha256'],production_git_commit=contract['production_git_commit'],source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],owner=runner.read(job/'OWNER.json'),core_refs=[seg[110]['ref'],seg[129]['ref']],core_indices=[seg[110]['source_index'],seg[129]['source_index']],next_ref=seg[130]['ref'],new_rows=len(p['records']),replacements=repl,exposure='Root ongoing producer; earlier gold-cup contextual evidence openly known. Independent008 reading not opened before initial freeze.')))
print(json.dumps(dict(proposal=runner.sha((out/'PROPOSAL.json').read_bytes()),rows=len(p['records']))))
