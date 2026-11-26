import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b20.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='a4c6116c2691a3c671cfbce32a1a2ba68829483869495bdefa378395fe4669d5'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','19a:3','quoted Mishnah','A priest with an injured finger may wrap a reed around it in the Temple.','asserted',['Injured finger; reed; Temple'],'Quoted permission'),
('2','19a:3','quoted Mishnah','That reed wrapping is not permitted outside the Temple.','asserted',['Injured finger; reed; outside Temple'],'Distinct location restriction'),
('3','19a:3','quoted Mishnah','If intended to extract blood, it is prohibited in the Temple.','asserted',['Intention to draw blood; Temple'],'Exception to permission'),
('4','19a:3','quoted Mishnah','If intended to extract blood, it is prohibited outside the Temple.','asserted',['Intention to draw blood; outside Temple'],'Same prohibition, separate location condition'),
('5','19a:4','Rabbi Yehuda son of Rabbi Hiyya','The permission concerns a reed; a small belt counts as excess garments.','asserted',['First version; small belt wrapping'],'Restricts quoted permission'),
('6','19a:4','Rabbi Yohanan','Excess garments applies only where garments are worn.','asserted',['First version; garment location'],'Disagrees with broad excess-garment classification'),
('7','19a:4','Rabbi Yohanan','Away from the garment location there is no excess-garment status.','asserted',['First version; outside garment location'],'Distinct negative rule'),
('8','19a:5','anonymous','Why is the wrapping not disqualified as an interposition?','queried',['Wrapping on injured finger'],'Independent objection'),
('9','19a:5','anonymous','The case can involve the left hand.','conditional',['Left-hand finger; no service contact'],'Alternative reply'),
('10','19a:5','anonymous','Alternatively it is away from the place used in service.','conditional',['Wrapping not at service-contact location'],'Alternative reply'),
('11','19a:6','Rav Hisda','At the garment location even a single thread interposes.','asserted',['First-version cited report; garment location'],'Rava reports Rav Hisda'),
('12','19a:6','Rav Hisda','Away from the garment location a three-by-three piece interposes.','asserted',['First-version cited report; outside garment location; three by three'],'Rava reports Rav Hisda'),
('13','19a:6','Rav Hisda','Away from the garment location less than three by three does not interpose.','asserted',['First-version cited report; outside garment location; below three by three'],'Rava reports Rav Hisda'),
('14','19a:7','anonymous','This certainly disagrees with Rabbi Yohanan.','asserted',['First version; Rav Hisda report and Yohanan outside-garment rule'],'Explicit disagreement'),
('15','19a:7','anonymous','Must it also disagree with Rabbi Yehuda son of Rabbi Hiyya?','queried',['Small belt below standard cloth size'],'Possible disagreement only'),
('16','19a:8','anonymous','A small belt is different because it is significant.','asserted',['Small belt significance'],'Reconciles possible disagreement; not categorical dispute'),
('17','19a:9','Rabbi Yehuda son of Rabbi Hiyya','The reed permission excludes a small belt, which interposes.','asserted',['Alternative version; small belt'],'Interposition wording, preserved separately from first version'),
('18','19a:9','Rabbi Yohanan','Interposition smaller than three by three applies at the garment location.','asserted',['Alternative version; garment location'],'Second-version rule'),
('19','19a:9','Rabbi Yohanan','Away from the garment location a three-by-three piece interposes.','asserted',['Alternative version; outside garment location; three by three'],'Agrees with Rava report of Rav Hisda'),
('20','19a:9','Rabbi Yohanan','Away from the garment location less than three by three does not interpose.','asserted',['Alternative version; outside garment location; below three by three'],'Agrees with Rava report of Rav Hisda'),
('21','19a:9','anonymous','This alternative version of Yohanan agrees with Rava report of Rav Hisda.','asserted',['Alternative version only'],'Explicit agreement; do not collapse with first-version disagreement'),
('22','19a:10','anonymous','Does the size rule disagree with Rabbi Yehuda son of Rabbi Hiyya?','queried',['Alternative version; small belt significance'],'Potential disagreement'),
('23','19a:10','anonymous','A small belt is different because it is significant.','asserted',['Alternative version; small belt'],'Reconciliation repeated in second version'),
('24','19a:11','anonymous','For Rabbi Yohanan why teach a reed rather than even a small belt?','queried',['Reed choice in cited Mishnah'],'Question on narrow example'),
('25','19a:11','anonymous','It incidentally teaches that a reed heals.','asserted',['Medicinal property of reed'],'Explains choice without invalidating small belt under his rule')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'rule_or_argument',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Two versions of finger wrapping, excess garments and interposition',assertion_mode=mode),['u'+k])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode!='queried':rec('p'+k,'positions',refs,dict(holder_candidates=[] if v in ['anonymous','quoted Mishnah'] else [v],claim_id=prefix+'c'+k,question_id=None,conditions=conds,local_status=status),['c'+k])
for k,refs,surface,cands,role,chain,links in [('yehuda1',['19a:4'],'Rabbi Yehuda son of Rabbi Hiyya',['Rabbi Yehuda son of Rabbi Hiyya'],'speaker',[],['c5']),('yohanan1',['19a:4'],'Rabbi Yohanan',['Rabbi Yohanan'],'speaker',[],['c6','c7']),('hisda',['19a:6'],'Rava said Rav Hisda',['Rava'],'transmitter',['Rava','Rav Hisda'],['c11','c12','c13']),('yehuda2',['19a:9'],'Rabbi Yehuda son of Rabbi Hiyya',['Rabbi Yehuda son of Rabbi Hiyya'],'speaker',[],['c17']),('yohanan2',['19a:9'],'Rabbi Yohanan',['Rabbi Yohanan'],'speaker',[],['c18','c19','c20']),('hisda2',['19a:9'],'Rava said Rav Hisda',['Rava'],'transmitter',['Rava','Rav Hisda'],['c21'])]:rec('a'+k,'attributions',refs,dict(surface=surface,role=role,candidates=cands,scope='Local report version retained in linked claim conditions',transmission_chain=chain),links)
for a,b,rel in [('3','1','qualification'),('5','1','qualification'),('7','5','objection'),('8','1','objection'),('9','8','answer'),('10','8','answer'),('14','7','objection'),('12','14','support'),('15','5','objection'),('16','15','answer'),('17','1','qualification'),('21','19','support'),('21','20','support'),('22','17','objection'),('23','22','answer'),('25','24','answer')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['19a:'+str(i) for i in range(3,12)]
rec('s1','structure',refs,dict(title='Injured finger: two report versions distinguish excess garments and interposition',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through19a11 and next Rava interposition questions19a12 onward. Keep first and alternative versions separate, explicit disagreement vs agreement, significant-small-belt reconciliation and exact location/size conditions.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_19a3_19a11.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch20.json',r.encoded(res));print(res)
