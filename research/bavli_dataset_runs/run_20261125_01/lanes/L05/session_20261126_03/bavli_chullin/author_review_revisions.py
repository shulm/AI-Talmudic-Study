import json,pathlib,hashlib,copy
W=pathlib.Path('F:/Sefaria_QA/worktrees/bavli-l05-production-20261126');O=W/'research/bavli_dataset_runs/run_20261125_01/lanes/L05/session_20261126_03/bavli_chullin';J=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_chullin');meta=json.loads((J/'JOB.json').read_text());inv=json.loads((J/'source_inventory.json').read_text());sha=json.loads((J/'CURRENT.json').read_text())['snapshot_sha256'];state=json.loads((J/'snapshots'/(sha+'.json')).read_text());active={r['id']:r for r in state['records'] if r['release_state']=='valid'};rows=[];mapping={}
def ev(n,q):
 s=inv[n];a=s['text'].index(q);return dict(segment_id=s['id'],start_char=a,end_char=a+len(q),quote=q)
def add(id,layer,e,content,links=[],unc=[]):
 rid='ch04_'+id;rows.append(dict(id=rid,layer=layer,evidence=e,content=content,origin='source_paraphrase',uncertainty=unc,links=links));return rid
def claim(id,n,q,prop,cond=[],mode='asserted',scope='Quoted source within lexical argument; not a universal practical ruling'):
 c=add(id,'claims',[ev(n,q)],dict(proposition=prop,conditions=cond,scope=scope,assertion_mode=mode));add(id+'_p','positions',[ev(n,q)],dict(holder_candidates=[],claim_id=c,question_id=None,conditions=cond,local_status='quoted proposition in anonymous discussion; source authority not a resolved historical holder'),[c]);return c
def revise(id,content=None,e=None):
 old=active[id];r={k:copy.deepcopy(old[k]) for k in ['id','layer','evidence','content','origin','uncertainty','links']};r['id']=id+'_rev04';r['supersedes']=id
 if content:r['content'].update(content)
 if e:r['evidence']=e
 rows.append(r);mapping[id]=r['id'];return r
# Recover four valuation/vow roles and the three other cited classes.
for id,q,prop in [('valuers','הכל מעריכין','All may undertake valuation vows.'),('valued','ונערכין','All may be subjects of valuation vows.'),('vowers','נודרין','All may make vows.'),('vowed','ונידרין','All may be subjects of vows.')]:claim(id,4,q,prop)
claim('sukkah',7,'הכל חייבים בסוכה','All are obligated in sukkah under the quoted Mishnah generality; class scope is not expanded here.')
claim('tzitzit',7,'הכל חייבין בציצית','All are obligated in tzitzit under the quoted Mishnah generality; class scope is not expanded here.')
claim('semikhah',8,'הכל סומכין אחד האנשים ואחד הנשים','The quoted formulation includes both men and women in laying hands; retain as quotation used in lexical argument.')
# Split bundled opening assertions and reason, without erasing original readings.
revise('ch01_c_all',dict(proposition='The Mishnah states that all slaughter, subject to its explicit exclusions.',conditions=['subject to explicitly excluded classes']),[ev(0,'הכל</strong></big> שוחטין')])
claim('m_valid',0,'ושחיטתן כשרה','Their slaughter is valid under the Mishnah stated qualifications.',['subject to exclusions and subsequent supervision clause'],scope='Opening Mishnah')
revise('ch01_c_ex',dict(proposition='Deaf-mute, mentally incompetent person and minor are excluded from unsupervised slaughter.',conditions=['unsupervised slaughter']),[ev(0,'חוץ מחרש שוטה וקטן')])
reason=claim('m_risk',0,'שמא יקלקלו את שחיטתן','The excluded persons may spoil their slaughter.',mode='hypothetical',scope='Reason for opening exclusion')
revise('ch01_c_mixed',dict(proposition='Some occurrences of הכל concern initial action.'),[ev(9,'אין איכא הכל לכתחלה')]);claim('lex_post',9,'ואיכא הכל דיעבד','Some occurrences of הכל concern after-the-fact effect.',scope='Lexical conclusion')
revise('ch01_c_notperm',dict(proposition='A person is not permitted to make sacrificial substitution.',conditions=[],assertion_mode='asserted'),[ev(3,'לא שהאדם רשאי להמיר')])
claim('tem_effect',3,'אלא שאם המיר מומר','If substitution was performed, it takes effect.',['Substitution was performed'],'conditional')
for name,conditions in [('ch01_p_watch',['Others observe the slaughter']),('ch01_p_lashes',['Substitution was performed']),('ch01_p_zeh',['Declaration is הרי זו rather than personal obligation הרי עלי']),('ch01_p_all',['subject to explicitly excluded classes']),('ch01_p_ex',['unsupervised slaughter'])]:revise(name,dict(conditions=conditions))
gen=claim('lex_generalization',2,'וכל הכל לכתחלה הוא','Does every occurrence of הכל imply initial permission?',mode='queried',scope='Rav Aha challenge to universal lexical inference, not rejection of local ruling')
for name in ['ch01_e_counter','ch01_e_vowcounter']:revise(name,dict(target_id=gen))
revise('ch01_c_initial',dict(scope='Initial local interpretation; challenged via a proposed universal lexical inference, then supported locally by redundancy at 2b:5',assertion_mode='asserted'))
revise('ch01_p_initial',dict(local_status='Initial local interpretation restored by redundancy at 2b:5; failure of universal inference does not reject the local reading'))
# Recursively re-version dependent records and links, preserving exact graph closure.
def replace(v):
 if isinstance(v,str):return mapping.get(v,v)
 if isinstance(v,list):return [replace(x) for x in v]
 if isinstance(v,dict):return {k:replace(x) for k,x in v.items()}
 return v
while True:
 todo=[rid for rid,r in active.items() if rid not in mapping and (replace(r['content'])!=r['content'] or replace(r['links'])!=r['links'])]
 if not todo:break
 for rid in todo:revise(rid)
for r in rows:r['content']=replace(r['content']);r['links']=replace(r['links'])
allrows=[r for rid,r in active.items() if rid not in mapping]+rows;coverage=[]
for c in state['coverage']:
 if any(rid in mapping for rid in c['record_ids']) or c['segment_id'] in {e['segment_id'] for r in rows for e in r['evidence']}:
  c={k:copy.deepcopy(v) for k,v in c.items() if k!='proposal_execution'}
  c['record_ids']=[r['id'] for r in allrows if (r['layer']==c['layer'] or c['layer']=='reconciliation') and any(e['segment_id']==c['segment_id'] for e in r['evidence'])]
  c['extraction_result']='records_found' if c['record_ids'] else 'none_found_after_pass';c['rationale']='Source reread for exact-version review CH-ATOMIC, CH-COND, CH-GRAPH. Added quoted atomic propositions, split combined clauses, retained conditions and restored lexical/local distinction. CH-ROLE quarantine explicitly remains uncleared.';coverage.append(c)
p=dict(schema_version=meta['schema_version'],tractate='Chullin',owner='L05/chullin',epoch=2,source_sha256=meta['source_sha256'],protocol_sha256=meta['protocol_sha256'],schema_sha256=meta['schema_sha256'],execution=dict(route='interactive_agent',agent_id='/root/chullin',model_id=None),records=rows,coverage=coverage,open_tails=state['open_tails']);f=O/'ch04_review_revisions.json';assert not f.exists();f.write_text(json.dumps(p,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8');print(len(rows),f)
