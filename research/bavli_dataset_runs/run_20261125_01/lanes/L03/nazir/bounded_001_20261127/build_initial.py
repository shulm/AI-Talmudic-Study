import json,hashlib
from pathlib import Path
root=Path.cwd();job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_nazir');out=Path(__file__).parent
read=lambda f:json.loads(f.read_text(encoding='utf-8-sig'));sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
assert read(job/'OWNER.json')=={'owner':'/root/lead_l01_l03','epoch':1};assert not (job/'CURRENT.json').exists()
a=read(root/'research/bavli_dataset_runs/ACTIVE_RUN.json');cp=root/a['contract_path'];assert sha(cp)==a['contract_sha256'];contract=read(cp)
for f,h in contract['production_files'].items():assert sha(root/f)==h,f
src=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Nashim/Nazir/Hebrew/Wikisource Talmud Bavli.json');ss=Path('F:/Sefaria-Export-master/schemas/Nazir.json')
assert sha(src)=='29a2a4347221c24b248de9b131523cb8354dcbf78d7975167c12ab7c13d43bef';assert sha(ss)=='addbcf44299407f22ded320e47a3521024d796c3526aa96283f69cddc68c34df'
assert sha(root/'research/bavli_sugya_corpus_v1/source_manifest.json')==contract['source_manifest_sha256']
schema=read(root/'research/bavli_production_v1/schema.json');assert len(schema['properties']['records']['items']['allOf'])==7
pins=dict(run_id=a['run_id'],contract_sha256=sha(cp),production_git_commit=contract['production_git_commit'],schema_sha256=contract['schema_sha256'],protocol_sha256=contract['annotation_protocol_sha256'],source_path=str(src),source_sha256=sha(src),source_schema_path=str(ss),source_schema_sha256=sha(ss),source_manifest_sha256=contract['source_manifest_sha256'],owner=read(job/'OWNER.json'),delegation='L03 lead delegates exactly one bounded batch under unchanged historical owner; actual agent /root/yevamot',initial_current_exists=False,independence='No frozen central Nazir reading or review labels accessed.')
(out/'PINS.json').write_text(json.dumps(pins,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
w=read(job/'context_bounded001_20261127.json');extra=read(job/'context_forms_bounded001_20261127.json');seg=w['segments']+extra['segments'][1:];byref={s['ref']:i for i,s in enumerate(seg)}
p={k:w['job'][k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='/root/lead_l01_l03',epoch=1,execution={'route':'interactive_agent','agent_id':'/root/yevamot','model_id':None},records=[],coverage=[],open_tails=['naz001.order'])
def ev(i,q=None):
 if isinstance(i,str):i=byref[i]
 s=seg[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=[],u=[],origin='source_paraphrase'):
 rid='naz001.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(i) if isinstance(i,(int,str)) else ev(*i) for i in inds],content=c,links=links,uncertainty=u,origin=origin));return rid
def claim(k,inds,prop,mode='asserted',cond=[],holder='anonymous Gemara',u=[]):
 c=rec(k,'claims',inds,dict(proposition=prop,conditions=cond,scope='Opening Mishnah formulations and opening editorial discussion; continuation qualifiers explicitly identified',assertion_mode=mode),u=u)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=cond,local_status=mode+' at this source stage; later explanations separately retained'),[c],u);return c
def q(k,inds,text):return rec(k,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,inds,x,y,rel):return rec(k,'edges',inds,dict(source_id=x,target_id=y,relation=rel,explicitness='source_explicit'),[x,y])
for k,inds,title,boundary in [('mishnah',[0,1,2],'Substitute nazirite formulations, incomplete declarations and birds dispute','closed'),('placement',[3,4],'Nazir in Seder Nashim: sotah and abstention from wine','closed'),('order',[5,6,7,8,9],'Kinuyim/yadot wording and proposed exposition order; core ends within examples','open_right')]:rec(k,'structure',inds,dict(title=title,primary=True,boundary=boundary,legacy_ids=[]),origin='editorial_inference')
roles={0:'General Mishnah rule for substitute nazirite terms',1:'Nine formula occurrences yielding nazirite status; later conditions read separately',2:'Bird declaration: Rabbi Meir versus sages',3:'Question why Nazir appears in Seder Nashim',4:'Verse-based placement rationale and sotah/wine exhortation',5:'Challenge: opens with kinuyim but explains yadot',6:'Rava or unresolved כדי alternative: חסורי מיחסרא reconstruction',7:'Question why not explain kinuyim first; proposed reverse-order principle and lighting example',8:'Insulation example supports proposed reverse-order principle',9:'Woman going out example supports proposed reverse-order principle'}
for i,role in roles.items():rec('u'+str(i),'utterances',[i],dict(textual_voice='anonymous Mishnah' if i<3 else 'anonymous Gemara / scoped attribution below',discourse_role=role,composition='atomic' if i in [0,3,5] else 'composite'))
for i,role in roles.items():
 if i==6:continue
 rec('a'+str(i),'attributions',[i],dict(surface='מתני׳' if i==0 else ('anonymous Mishnah frame' if i<3 else 'anonymous Gemara'),role='anonymous',candidates=[],scope=role+'; named views separately scoped',transmission_chain=[]))
for k,surf,can,scope in [('meir','ר"מ',['Rabbi Meir'],'Bird declaration establishes nazirite status'),('sages','חכמים',['sages'],'Bird declaration does not establish nazirite status')]:rec(k,'attributions',[2],dict(surface=surf,role='collective' if k=='sages' else 'position_holder',candidates=can,scope=scope,transmission_chain=[]))
rec('rava_variant','attributions',[6],dict(surface='אמר רבא ואיתימא כדי',role='speaker',candidates=['Rava'],scope='חסורי מיחסרא reconstruction; Rava is one reported attribution, alternative כדי left unresolved',transmission_chain=[]),u=['ואיתימא כדי preserved verbatim. No named identity or anonymous gloss for כדי forced from this source alone.'])
general=claim('substitutes',[0],'All substitute expressions for naziriteship have the effect of naziriteship.',holder='anonymous Mishnah')
forms=[('aha','אהא'),('beautiful','אהא נאה'),('nazik','נזיק'),('naziah','נזיח'),('paziah','פזיח'),('like_this','הריני כזה'),('mesalsel','הריני מסלסל'),('mekalkel','הריני מכלכל'),('pera','הרי עלי לשלח פרע')];fc={}
for k,formula in forms:
 fc[k]=claim('form.'+k,[(1,formula)],'The Mishnah states that saying '+formula+' establishes nazirite status as specified by its subsequent interpretation.',holder='anonymous Mishnah',u=['Bare Mishnah wording retained; context conditions and alternative interpretations are not erased.'] if k in ['aha','beautiful','like_this','mesalsel','mekalkel'] else [])
 # Scope relation, not a fabricated dialogue or personal dispute.
 if k in ['nazik','naziah','paziah']:edge('substitute.'+k,[0,(1,formula)],fc[k],general,'qualification')
m=claim('birds_meir',[2],'Saying הרי עלי ציפורים establishes nazirite status according to Rabbi Meir.',cond=['Bird formulation'],holder='Rabbi Meir',u=['Resh Lakish and Rabbi Yohanan later explain the basis differently; no single rationale assigned here.'])
s=claim('birds_sages',[2],'Saying הרי עלי ציפורים does not establish nazirite status according to the sages.',cond=['Bird formulation'],holder='sages')
# Two reported positions are preserved; no explicit challenge/reply invented between their holders.
qplace=q('placement_q',[3],'Why does the tanna teach Nazir within Seder Nashim?')
cverse=claim('verse_basis',[4],'The tanna’s placement is tied to Deuteronomy 24:1 and its reference to sexual misconduct.')
wine=claim('wine_cause',[4],'The exposition identifies wine as the cause of her transgression.',u=['Attributed to the local exposition, not asserted as a general psychological fact.'])
abstain=claim('sotah_abstain',[4],'Whoever sees a sotah in her disgrace should abstain from wine.',cond=['Seeing the sotah in her disgrace'])
edge('placement_answer',[4],cverse,qplace,'answer');edge('wine_reason',[4],wine,abstain,'support');edge('placement_link',[4],abstain,qplace,'answer')
qorder=q('kinuyim_yadot',[5],'Why open with kinuyim but explain yadot?')
reconstruct=claim('reconstruction',[6],'The transmitted Mishnah is reconstructed to include both kinuyim and yadot as effective naziriteship, followed by examples of yadot.',holder='Rava, with unresolved alternative attribution כדי')
yadot=claim('yadot_rule',[6],'Incomplete nazirite declarations are effective naziriteship in the reconstructed wording.',holder='Rava, with unresolved alternative attribution כדי')
ahayad=claim('aha_yad',[6],'אהא is presented as an example of a yad in that reconstruction.',holder='Rava, with unresolved alternative attribution כדי')
edge('reconstruct_answer',[6],reconstruct,qorder,'answer');edge('reconstruct_content',[6],yadot,reconstruct,'qualification');edge('aha_example',[6],ahayad,yadot,'qualification')
qfirst=q('kinuyim_first',[(7,'ולפרוש כינויי ברישא')],'Why not explain kinuyim first?')
lastfirst=claim('last_first',[(7,'תנא מההוא דסליק ההוא מפרש ברישא')],'The proposed explanation is that the tanna first explains the subject last mentioned.','challenged',u=['Continuation at 2a:11–13 gives counterexamples and abandons a universal ordering rule; 2b:2–3 supplies the local reason.'])
edge('order_answer',[7],lastfirst,qfirst,'answer')
examples=[('lighting',7,'במה מדליקין ובמה אין מדליקין ומפרש אין מדליקין ברישא','The lighting Mishnah announces permitted and prohibited materials, then explains prohibited materials first.'),('insulation',8,None,'The insulation Mishnah announces permitted and prohibited materials, then explains prohibited materials first.'),('goingout',9,None,'The woman-going-out Mishnah announces permission and prohibition, then begins with what she may not wear out.')]
for k,i,quote,prop in examples:
 inds=[(i,quote)] if quote else [i];cid=claim('example.'+k,inds,prop);edge('example_support.'+k,inds,cid,lastfirst,'support')
# Limited continuation-derived qualifications, not blanket extraction of context.
# Coverage remains restricted to the ten core segments.
for k,ref,prop,holder in [('aha','Nazir 2b:4','Shmuel construes אהא where a nazirite is passing before the speaker.','Shmuel'),('beautiful','Nazir 2b:9','Shmuel construes the beauty declaration while the speaker grasps his hair.','Shmuel'),('like_this','Nazir 3a:2','Shmuel construes הריני כזה where a nazirite passes before him.','Shmuel'),('mesalsel','Nazir 3a:4','Shmuel construes הריני מסלסל while the speaker grasps his hair, answering the Torah alternative.','Shmuel'),('mekalkel','Nazir 3a:6','Shmuel construes הריני מכלכל while the speaker grasps his hair, answering the sustenance alternative.','Shmuel')]:
 cid=claim('context.'+k,[ref],prop,holder=holder);edge('qualify.'+k,[1,ref],cid,fc[k],'qualification');rec('attribution.context.'+k,'attributions',[ref],dict(surface='אמר שמואל',role='speaker',candidates=['Shmuel'],scope=prop,transmission_chain=[]))
intent=claim('context.intent',['Nazir 2b:6','Nazir 2b:7'],'The אהא case includes nazirite intent in the speaker’s heart; the Gemara distinguishes it from paying another’s offerings and explains that the abbreviated words suffice in this context.',u=['No general waiver of speech/intention congruence beyond the stated abbreviated declaration is inferred.']);edge('intent_qualification',[1,'Nazir 2b:6','Nazir 2b:7'],intent,fc['aha'],'qualification')
varorder=claim('context.variable',['Nazir 2a:11','Nazir 2a:12','Nazir 2a:13'],'Animal-going-out and inheritance examples show both ordering patterns occur; the universal last-mentioned-first explanation is rejected.');edge('order_correction',[7,'Nazir 2a:11','Nazir 2a:12','Nazir 2a:13'],varorder,lastfirst,'correction')
localreason=claim('context.localreason',['Nazir 2b:2','Nazir 2b:3'],'Yadot are explained first because they are derived by exposition and valued; the opening nevertheless begins with the primary offering formulation.');edge('local_reason',[7,'Nazir 2b:2','Nazir 2b:3'],localreason,qfirst,'answer')
pera=claim('context.pera',['Nazir 3a:7','Nazir 3a:8','Nazir 3a:9','Nazir 3a:10'],'The growth reading of לשלח פרע is supported by פרע analogy; alternatively the water-sending verse also denotes growth.');edge('pera_support',[1,'Nazir 3a:9','Nazir 3a:10'],pera,fc['pera'],'support')
# Preserve contested later explanations as uncertainty rather than assigning the tannaitic dispute by mere proximity.
for r in p['records']:
 if r['id'] in [m,m+'.p',s,s+'.p']:
  r['uncertainty'].append('Context 3a:11–3b:8 read: Resh Lakish uses adjacent-word interpretation; Rabbi Yohanan instead gives concern for impure-nazirite bird acceptance and refines to a passing pure nazirite. These are separate explanatory readings; central review not accessed.')
notes={0:'General kinuyim rule distinguished from the later reconstructed yadot clause.',1:'All nine formula occurrences separately preserved; אהא נאה is one formula, following נזיר is its result; Shmuel’s later context conditions attached without counting context coverage.',2:'Rabbi Meir and sages remain distinct contrary positions; no final pesak or single later explanatory rationale forced.',3:'Explicit placement question retained without an invented legal dispute.',4:'Verse, wine rationale and conditional sotah exhortation kept distinct and attributed to exposition.',5:'Implicit interrogative challenge about kinuyim/yadot preserved.',6:'חסורי מיחסרא is Gemara reconstruction, not silent alteration of source Mishnah; ואיתימא כדי unresolved.',7:'First-last ordering answer and lighting support preserved as challenged in light of continuation; later correction attached.',8:'Insulation example is support for an interim generalization, not a new binding halakhic rule.',9:'Woman-going-out example is support; next source supplies counterexamples. Core boundary is not semantic closure.'}
for i in range(10):
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  rationale=notes[i]+' Continuation read through 4a:1; only ten core segments count. '+('Source-based omission and continuation reconciliation reread completed.' if layer=='reconciliation' else ('Actual '+layer+' pass found no separate item.' if not ids else 'Completed '+layer+' pass.'))
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
f=out/'INITIAL_PROPOSAL.json';assert not f.exists();f.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'sha256':sha(f),'records':len(p['records']),'coverage_rows':len(p['coverage'])}))
