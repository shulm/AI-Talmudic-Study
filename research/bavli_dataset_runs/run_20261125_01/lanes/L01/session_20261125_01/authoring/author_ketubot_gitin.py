"""Manual source reading of the two Rava report versions, serialized with shared schema."""
from pathlib import Path
helpers=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/author_ketubot_opening.py').read_text(encoding='utf-8').split('# Primary ownership')[0]
exec(helpers.replace('kt.open1.','kt.gitin1.'))
prefix='kt.gitin1.'
refs1=[f'2b:{i}' for i in range(5,15)]+[f'3a:{i}' for i in range(1,5)]
refs2=[f'3a:{i}' for i in range(5,12)]
for key,refs,title in [('s.first',refs1,'First Rava report: no involuntary-impediment defense for conditional divorce'),('s.alternative',refs2,'Alternative Rava report: involuntary-impediment defense and replies to objections')]:
    add(key,'structure',refs,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
# Each entry is individually authored; exact source spans are retained alongside paraphrases.
data=[
('rava1',['2b:5'],'Rava says divorce is different; the discussion infers that he denies an involuntary-impediment defense in conditional divorce.','asserted',[], 'Rava in first report','reported rule; opposite alternative retained'),
('dead1',['2b:6'],'A quoted Mishnah invalidates a conditional divorce if he dies within the twelve months stipulated for his nonreturn.','asserted',['no return within twelve months','death within the period'],'quoted Mishnah','quoted law'),
('ill_infer1',['2b:6'],'The discussion proposes inferring from the death case that illness would leave the divorce valid.','challenged',['illness prevents return'],'anonymous proposed inference','rejected as a necessary inference'),
('ill_possible1',['2b:7'],'Illness could also invalidate the divorce; the death case may teach that divorce cannot take effect after death.','hypothetical',['illness prevents return'],'anonymous counterreading','undercuts proposed proof'),
('no_postdeath',['2b:7'],'A divorce cannot take effect after death.','asserted',[],'quoted Mishnah as interpreted','proposed teaching of cited case'),
('death_formulas',['2b:8'],'The earlier clause already says that a divorce expressed as if I die, from this illness, or after death has no effect.','asserted',['the three quoted formulations'],'quoted Mishnah','quoted earlier law; redundancy objection'),
('exclude_teachers',['2b:9'],'The later death clause may exclude the Teachers’ contrary permission to remarry.','hypothetical',[],'anonymous counterreading','alternative purpose of the clause'),
('teachers_allow',['2b:9'],'The Teachers permitted the woman to remarry in the referenced case.','asserted',['referenced conditional-divorce case'],'רבותינו','quoted alternative'),
('teachers_identity',['2b:9'],'Rav Yehuda reports Shmuel identifying the Teachers as the court that permitted oil.','asserted',[],'Shmuel through Rav Yehuda','textual identification; no additional historical identity supplied'),
('date_proves',['2b:9'],'That court follows Rabbi Yose’s view that a document’s date demonstrates its intended effect.','asserted',[],'Rabbi Yose as cited','principle invoked to explain Teachers; scope not generalized beyond source'),
('fromnow_dead',['2b:10'],'The later clause validates divorce stated from now if he does not return within twelve months and dies during them.','asserted',['from-now formulation','death within twelve months'],'quoted Mishnah','quoted law'),
('fromnow_ill',['2b:10'],'The discussion proposes extending that validity from death to illness.','challenged',['from-now formulation','illness'],'anonymous inference','proof rejected as necessary'),
('death_specific',['2b:11'],'Death may be a special case because he does not want her to fall before a levir.','hypothetical',['death rather than illness'],'anonymous counterreading','source-explicit rationale; not an inferred personal biography'),
('ferry_case',['2b:12'],'A man conditioned divorce on not arriving within thirty days; a ferry impeded him at the end despite his repeated announcement that he had come.','asserted',['thirty-day condition','ferry prevented arrival'],'reported case','narrative occurrence'),
('shmuel_arrival',['2b:12'],'Shmuel said that the reported approach did not constitute arrival.','asserted',['the ferry case'],'שמואל','reported ruling'),
('common_impediment',['2b:13'],'A common impediment may be different: he should have stipulated an exception and his failure to do so causes his own loss.','hypothetical',['common impediment','no protective stipulation'],'anonymous distinction','limits inference from ferry ruling'),
('rava_reason',['2b:14'],'Rava’s first-version rule is his own reasoning, for the sake of the modest and the unrestrained women.','asserted',['first version'],'Rava as explained by discussion','rationale after attempted textual proofs fail'),
('modest',['2b:14','3a:1'],'If involuntary impediment invalidated divorce, a cautious woman might wrongly suppose an impediment when there was none and remain unable to remarry.','hypothetical',['no actual impediment','mistaken belief that impediment occurred'],'anonymous explanation of Rava’s rationale','policy risk, not an assertion about a particular woman'),
('unrestrained',['3a:1'],'An unrestrained woman might deny an actual impediment, remarry on an invalid divorce, and have children classified as mamzerim.','hypothetical',['actual impediment','false denial','remarriage'],'anonymous explanation of Rava’s rationale','policy risk, not a description of an actual person'),
('annulment',['3a:3'],'The answer says every betrothal is made on the Sages’ terms and the Sages annulled this betrothal.','asserted',['rabbinic treatment under discussion'],'anonymous answer','local explanation of authority; not unrestricted annulment claim'),
('money_ok',['3a:4'],'Ravina’s challenge accepts that the explanation works for betrothal by money, but asks about intercourse.','hypothetical',['money betrothal as contrasted with intercourse'],'רבינא','concession within objection'),
('intercourse_answer',['3a:4'],'The reply says the Sages rendered the intercourse nonmarital.','asserted',['intercourse betrothal in this argument'],'reply after Ravina addresses Rav Ashi','answer’s immediate attribution is contextual, not a new explicit אמר רב אשי'),
('rava2',['3a:5'],'In another report Rava says divorce is likewise, and the discussion infers that he recognizes an involuntary-impediment defense.','asserted',['alternative report'],'Rava in alternative report','opposite report retained without harmonizing'),
('dead2',['3a:6'],'The same Mishnah death case is now quoted as an objection to the alternative report.','asserted',['death within twelve-month nonreturn condition'],'quoted Mishnah','separate source occurrence retained'),
('ill_infer2',['3a:6'],'The objection again infers divorce validity in the illness case from the death-only wording.','challenged',['illness prevents return'],'anonymous objection','answered in next segment'),
('ill_possible2',['3a:7'],'The answer maintains that illness too may invalidate divorce and that the clause teaches no divorce after death.','hypothetical',['illness prevents return'],'anonymous answer','counterreading answering objection'),
('redundancy2',['3a:8'],'The earlier clause already taught no postmortem divorce.','asserted',[],'anonymous objection','repeat argument, separate occurrence'),
('teachers2',['3a:8'],'The answer again suggests excluding the Teachers’ position.','hypothetical',[],'anonymous answer','repeat counterreading'),
('fromnow_law2',['3a:9'],'The quoted Mishnah validates a from-now conditional divorce when he dies within the twelve-month period.','asserted',['from-now formulation','death within twelve months'],'quoted Mishnah','quoted law; separate occurrence retained'),
('fromnow2',['3a:9'],'The discussion proposes extending the from-now death case to illness.','challenged',['from-now formulation','illness proposed as parallel to death'],'anonymous objection','illness inference challenged; quoted death law remains asserted'),
('death_specific2',['3a:9'],'The reply restricts the case to death because he does not want her to face levirate marriage.','hypothetical',['death'],'anonymous reply','rejects necessity of illness extension'),
('ferry2',['3a:10'],'The ferry-impeded thirty-day case and Shmuel’s nonarrival ruling recur as an objection.','asserted',['thirty-day condition','ferry impediment'],'reported case and Shmuel ruling','separate textual occurrence'),
('common2',['3a:11'],'The reply distinguishes a common impediment, for which he should have stipulated an exception.','asserted',['common impediment','no exception stipulated'],'anonymous answer','local answer; alternative Rava report remains distinct')]
for key,refs,text,mode,conditions,holder,status in data:
    claim('c.'+key,refs,text,conditions,mode,scope='Conditional divorce; first and alternative reports kept separate')
    position('p.'+key,refs,holder,'c.'+key,conditions,status)
for ref in refs1+refs2:
    voice={'2b:5':'Rava, followed by anonymous inference','2b:9':'anonymous discussion quoting Teachers and Rav Yehuda reporting Shmuel','2b:12':'anonymous case report quoting Shmuel','3a:4':'Ravina addresses Rav Ashi; reply follows','3a:5':'alternative report of Rava with anonymous inference','3a:10':'anonymous case report quoting Shmuel'}.get(ref,'anonymous discussion and embedded quotations')
    add('u.'+ref,'utterances',[ref],dict(textual_voice=voice,discourse_role='argument step; see linked claim/question records for local status',composition='composite'))
questions=[
('basis',['2b:6'],'What is Rava’s source for the first-version rule?',[]),
('redundancy',['2b:8'],'Was no postmortem divorce not already taught?',[]),
('teachers',[('2b:9','מאן רבותינו')],'Who are the Teachers?',[]),
('authority',['3a:2'],'Can rabbinic concerns permit a married woman when Torah law would not recognize this divorce?',['policy concerns described for first version']),
('intercourse',['3a:4'],'How can the explanation work if betrothal was by intercourse?',['money betrothal conceded']),
('redundancy2',['3a:8'],'Was no postmortem divorce not already taught?',[]),
('ill2',['3a:9'],'Does the from-now death ruling not also apply to illness?',['from-now conditional divorce'])]
for key,refs,text,conditions in questions: question('q.'+key,refs,text,conditions,status='partial')
attr('a.rava1',[('2b:5','אמר רבא')],'רבא','speaker','first report: divorce is different')
attr('a.rava2',[('3a:5','איכא דאמרי אמר רבא וכן לענין גיטין')],'רבא','speaker','alternative report: divorce is likewise')
attr('a.yehuda',[('2b:9','אמר רב יהודה אמר שמואל')],'רב יהודה','transmitter','identification of Teachers',['רב יהודה','שמואל'])
attr('a.shmuel_id',[('2b:9','אמר רב יהודה אמר שמואל')],'שמואל','quoted_authority','identification of Teachers',['רב יהודה','שמואל'])
attr('a.teachers',[('2b:9','ורבותינו התירוה להנשא')],'רבותינו','collective','permission to remarry')
attr('a.yose',[('2b:9','כרבי יוסי דאמר זמנו של שטר מוכיח עליו')],'רבי יוסי','quoted_authority','document-date principle')
attr('a.shmuel1',[('2b:12','אמר שמואל לאו שמיה מתיא')],'שמואל','speaker','ferry case nonarrival ruling')
attr('a.shmuel2',[('3a:10','ואמר שמואל לא שמיה מתיא')],'שמואל','speaker','repeated ferry case ruling')
attr('a.ravina',[('3a:4','אמר ליה רבינא לרב אשי')],'רבינא','speaker','intercourse-betrothal challenge addressed to Rav Ashi')
# Do not mislabel Rav Ashi the addressee as a quoted authority: schema lacks that role.
records[-1]['uncertainty']=['Rav Ashi is explicitly the addressee. Frozen schema has no addressee role; that fact is preserved in scope and utterance, without a false role record.']
relations=[
('illproof',['2b:6'],'c.ill_infer1','c.rava1','support'),
('illreply',['2b:7'],'c.ill_possible1','c.ill_infer1','objection'),
('priorlaw',['2b:8'],'c.death_formulas','c.ill_possible1','objection'),
('teachersanswer',['2b:9'],'c.exclude_teachers','q.redundancy','answer'),
('identity',['2b:9'],'c.teachers_identity','q.teachers','answer'),
('date',['2b:9'],'c.date_proves','c.teachers_allow','support'),
('fromnowproof',['2b:10'],'c.fromnow_ill','c.rava1','support'),
('deathreply',['2b:11'],'c.death_specific','c.fromnow_ill','objection'),
('ferryproof',['2b:12'],'c.shmuel_arrival','c.rava1','support'),
('ferrylimit',['2b:13'],'c.common_impediment','c.shmuel_arrival','qualification'),
('ownbasis',['2b:14'],'c.rava_reason','q.basis','answer'),
('modest',['2b:14','3a:1'],'c.modest','c.rava_reason','support'),
('unrestrained',['3a:1'],'c.unrestrained','c.rava_reason','support'),
('authority',['3a:2'],'q.authority','c.rava_reason','objection'),
('annul',['3a:3'],'c.annulment','q.authority','answer'),
('intercourse',['3a:4'],'q.intercourse','c.annulment','objection'),
('answer',['3a:4'],'c.intercourse_answer','q.intercourse','answer'),
('alternative',['3a:5'],'c.rava2','c.rava1','unresolved_outcome'),
('objection2',['3a:6'],'c.ill_infer2','c.rava2','objection'),
('reply2',['3a:7'],'c.ill_possible2','c.ill_infer2','answer'),
('redundant2',['3a:8'],'c.redundancy2','c.ill_possible2','objection'),
('teachersreply2',['3a:8'],'c.teachers2','q.redundancy2','answer'),
('fromnowobjection2',['3a:9'],'c.fromnow2','c.rava2','objection'),
('deathreply2',['3a:9'],'c.death_specific2','q.ill2','answer'),
('ferryobjection2',['3a:10'],'c.ferry2','c.rava2','objection'),
('commonreply2',['3a:11'],'c.common2','c.ferry2','answer')]
for key,refs,src,target,relation in relations:
    edge('e.'+key,refs,src,target,relation,editorial=(key=='alternative'))
# Re-read all twenty-one source segments after drafting, tracking failed proofs and repetition.
coverage=[]
for ref in refs1+refs2:
    sid=byref[ref]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=f'Original {ref} re-read with 2b:5–3a:11 full two-version continuation and 3a:12 boundary. '+('Omission pass checked condition wording, failed inference versus quoted law, named roles, repetition, and alternative Rava versions; serialized findings retained, no further claim found.' if layer=='reconciliation' else f'{layer} pass retained the listed source-backed objects; no further independent object found where list empty.')))
p=dict(schema_version=r.VERSION,tractate='Ketubot',owner='/root/l01_ketubot',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
r.validate_apply(r.current(job),p,rows,j)
out=base/'ketubot_proposals'/'gitin_002.json'; r.immutable(out,r.encoded(p))
print(json.dumps(dict(path=str(out),sha256=r.sha(out.read_bytes()),records=len(records),segments=len(refs1+refs2))))
