import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b11.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1',['14a:6'],'רבי שמעון בן לקיש','reported_concession','Resh Lakish says Rabbi Shimon concedes intent invalidates carrying inner-sin-offering blood, because that service cannot be avoided.','asserted',['Rabbi Shimon; inner sin offering; indispensable carrying'],'Reported concession'),
('2',['14a:7'],'anonymous','objection','Rabbi Shimon denies piggul liability for offerings not on the outer altar like peace offerings.','challenged',['Inner sin offering; distinction between invalidity and piggul liability'],'Challenge to reported concession'),
('3',['14a:8'],'רבי יוסי ברבי חנינא','distinction','Rabbi Shimon nevertheless concedes invalidity: wrong-purpose intent valid for peace offerings invalidates sin offerings, so beyond-time intent invalidating peace offerings should invalidate sin offerings.','asserted',['Inner sin offering; invalidity without piggul liability'],'A-fortiori resolves liability/invalidity distinction'),
('4',['14a:9'],'anonymous','question','Beyond-time intent is established; what establishes beyond-place intent?','queried',['Inner sin offering carrying; beyond-place intent'],'Remaining scope question'),
('5',['14a:10'],'anonymous','objection','Beyond-time intent has the distinguishing severity of karet.','challenged',['Proposed inference from beyond time to beyond place'],'Distinguishes proposed source'),
('6',['14a:11'],'anonymous','objection','A proposed inference from wrong-purpose intent is challenged by its operation at a private altar.','challenged',['Proposed wrong-purpose premise; private altar applicability'],'Proposed distinction rejected in next segment'),
('7',['14a:12'],'anonymous','rejection','Wrong-purpose invalidity concerns Paschal and sin offerings, and those are not offered on a private altar.','asserted',['Paschal and sin offerings; claimed private-altar distinction'],'Rejects applicability objection'),
('8',['14a:13'],'anonymous','alternative_derivation','Alternatively a juxtaposition links third day to beyond-time and piggul to beyond-place intent.','asserted',['Beyond-place invalidity; alternative scriptural derivation'],'Alternative proof, not forced rejection of preceding route'),
('9',['14a:14'],'רבא','conditional_geography','If Rabbi Shimon agrees with his son that between the porch and altar counts as north, intent in inner-sin-offering carrying takes effect only from the porch entrance inward.','conditional',['Assume Rabbi Shimon follows his son on north between porch and altar','Inner-sin-offering blood carrying'],'Conditional spatial scope, not established adoption of premise'),
('10',['14a:15'],'רבא continued','conditional_geography','If Rabbi Shimon agrees with Rabbi Yehuda that the court sanctifies, intent in carrying the removed incense bowls takes effect only from the Sanctuary entrance outward.','conditional',['Assume Rabbi Shimon follows Rabbi Yehuda that court sanctifies','Carrying removed incense bowls'],'Separate conditional bowl-carrying case'),
('11',['14a:16'],'רבא continued','conditional_geography','If Sanctuary and porch have one sanctity, effective intent is only from the porch entrance outward.','conditional',['Removed incense bowls','Assume court sanctifies','Assume Sanctuary and porch have one sanctity'],'Further condition on preceding bowl case'),
('12',['14a:17'],'רבא continued','conditional_geography','If the entrance interior counts as inside, effective intent extends not even a step but only the reach of the hand.','conditional',['Removed incense bowls','Assume court sanctifies','Assume Sanctuary and porch have one sanctity','Assume doorway interior counts as inside'],'Further nested spatial restriction'),
('13',['14a:18'],'רבא continued','conditional_geography','If carrying without walking is not carrying, intent does not take effect at all in this residual case.','conditional',['Removed incense bowls','Assume court sanctifies','Assume Sanctuary and porch have one sanctity','Assume doorway interior counts as inside','Assume carrying without walking is not carrying'],'Terminal conditional outcome, not unconditional denial of all carrying intent')]
for key,refs,voice,role,prop,mode,cond,status in D:
 rec('u'+key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['3','9','10','11','12','13'] else 'atomic'))
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Rabbi Shimon inner carrying concession and conditional geography',assertion_mode=mode),['u'+key])
 if key in ['2','4','5','6']:rec('q'+key,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=cond,answer_set_status='partial'),['u'+key])
 if mode!='queried':rec('p'+key,'positions',refs,dict(holder_candidates=[] if voice=='anonymous' else ['רבי שמעון'] if key=='1' else ['רבא'] if voice.startswith('רבא') else [voice],claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status=status),['c'+key])
 if voice!='anonymous':rec('a'+key,'attributions',refs,dict(surface=voice,role='speaker',candidates=['רבא'] if voice.startswith('רבא') else [voice],scope='Local '+role,transmission_chain=[]),['c'+key])
rec('aShimon','attributions',['14a:6'],dict(surface='מודה רבי שמעון',role='quoted_authority',candidates=['רבי שמעון'],scope='Reported concession on indispensable inner carrying',transmission_chain=['רבי שמעון בן לקיש','רבי שמעון']),['c1'])
for a,b,rel in [('2','1','objection'),('3','2','answer'),('4','3','qualification'),('5','4','objection'),('6','4','objection'),('7','6','objection'),('8','4','answer'),('9','1','qualification'),('11','10','qualification'),('12','11','qualification'),('13','12','qualification')]:
 refs=next(x[1] for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['14a:'+str(i) for i in range(6,19)]
rec('s1','structure',refs,dict(title='Inner carrying invalidity without piggul liability and Rava conditional geography',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Reread through14a18 and next14a19 nonpriest inquiry. Preserve invalidity versus piggul liability, rejected private-altar distinction, alternative derivation, and cumulative hypothetical premises for bowl-carrying outcomes rather than unconditional positions.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding; source discourse retained in other layers.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_14a6_14a18.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch11.json',r.encoded(res));print(res)
