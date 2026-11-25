import json, hashlib
from pathlib import Path
root=Path.cwd(); job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot'); out=root/'research/bavli_dataset_runs/run_20261125_01/lanes/L03/yevamot'
contract=json.loads((root/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json').read_text())
for f,h in contract['production_files'].items():
 assert hashlib.sha256((root/f).read_bytes()).hexdigest()==h, f
assert json.loads((job/'OWNER.json').read_text())=={'owner':'L03/yevamot','epoch':2}
w=json.loads((job/'window001.json').read_text(encoding='utf-8')); seg=w['segments']; p={k:w['job'][k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/yevamot',epoch=2,execution={'route':'interactive_agent','agent_id':'/root/yevamot','model_id':None},records=[],coverage=[],open_tails=[])
def ev(i,quote=None):
 s=seg[i]; t=s['text']; a=0 if quote is None else t.index(quote); b=len(t) if quote is None else a+len(quote);return {'segment_id':s['id'],'start_char':a,'end_char':b,'quote':t[a:b]}
def rec(key,layer,indices,content,links=[],uncertainty=[],origin='source_paraphrase'):
 rid='yev001.'+key; evid=[ev(i) if isinstance(i,int) else ev(*i) for i in indices];p['records'].append(dict(id=rid,layer=layer,evidence=evid,content=content,origin=origin,uncertainty=uncertainty,links=links));return rid
def claim(key,inds,prop,conditions=[],mode='asserted',scope='Opening Mishnah: exemption of co-wives in levirate marriage'):
 c=rec(key,'claims',inds,dict(proposition=prop,conditions=conditions,scope=scope,assertion_mode=mode));rec(key+'.pos','positions',inds,dict(holder_candidates=['anonymous Mishnah'],claim_id=c,question_id=None,conditions=conditions,local_status='Mishnaic ruling; later Gemara not yet fully processed'),[c]);return c
def edge(key,inds,src,tgt,rel):return rec(key,'edges',inds,dict(source_id=src,target_id=tgt,relation=rel,explicitness='source_explicit'),[src,tgt])
rec('mishnah','structure',list(range(12)),dict(title='Fifteen forbidden relatives: exemption of co-wives, iterations and exceptions',primary=True,boundary='closed',legacy_ids=[]))
for key,inds,role in [('rule',list(range(5)),'General exemption and fifteen-category inventory'),('exceptions',[5,6,7],'Conditional permission and exclusions from two exception branches'),('iteration',[8,9],'Question and illustrative two-stage exemption'),('death',[10],'Question and chronological permission example'),('minor',[11],'Qualification for unexercised refusal')]:
 rec('u.'+key,'utterances',inds,dict(textual_voice='anonymous Mishnah',discourse_role=role,composition='composite'))
 rec('a.'+key,'attributions',inds,dict(surface='מתני׳' if key=='rule' else 'anonymous continuation of Mishnah',role='anonymous',candidates=[],scope=role,transmission_chain=[]))
general=claim('exemption',[0,4],'The fifteen specified forbidden relatives exempt their co-wives and recursively their co-wives from both halitzah and yibbum without a terminal generation.',['One of the listed relatives is married to the deceased brother; relationship is relative to the surviving brother'])
cats=[(1,'בתו','his daughter'),(1,'בת בתו','his daughter’s daughter'),(1,'בת בנו','his son’s daughter'),(1,'בת אשתו','his wife’s daughter'),(2,'בת בנה','his wife’s son’s daughter'),(2,'בת בתה','his wife’s daughter’s daughter'),(2,'חמותו','his mother-in-law'),(2,'אם חמותו','his mother-in-law’s mother'),(2,'אם חמיו','his father-in-law’s mother'),(3,'אחותו מאמו','his maternal sister'),(3,'אחות אמו','his mother’s sister'),(3,'אחות אשתו','his wife’s sister'),(3,'אשת אחיו מאמו','his maternal brother’s wife'),(4,'אשת אחיו שלא היה בעולמו','wife of his brother who was not alive contemporaneously with him'),(4,'כלתו','his daughter-in-law')]
for n,(i,word,label) in enumerate(cats,1):
 c=claim('category'+str(n),[0,(i,word)],label+' is included among the fifteen relatives whose co-wives are exempt.',['Relationship measured relative to the surviving brother']);edge('category'+str(n)+'.spec',[(i,word)],c,general,'qualification')
exceptions=claim('permission',[5,6],'The co-wives are permitted when the forbidden relative died, refused the marriage, was divorced, or was found to be an aylonit.',['One of the four stated alternatives applies; death/divorce chronology is specified in the later example'],mode='conditional')
edge('permission.qual',[5,6],exceptions,general,'qualification')
exclude=claim('exclude',[7],'The mother-in-law, her mother and the father-in-law’s mother cannot be cases of discovery as an aylonit or of refusal.',['Only the aylonit and mi’un alternatives are excluded here'])
edge('exclude.qual',[7],exclude,exceptions,'qualification')
q=rec('q.how','questions',[(8,'כיצד פוטרות צרותיהן')],dict(formulation='How do the specified relatives exempt their co-wives?',question_origin='explicit',conditions=[],answer_set_status='partial'))
c1=claim('firstcase',[8],'When a brother married the daughter or another listed forbidden relative together with a second wife and then died, the co-wife is exempt just as the forbidden relative is exempt.',['Listed relative and co-wife are wives of the deceased brother at his death'])
c2=claim('secondcase',[8],'If the exempt co-wife of the daughter marries the second brother alongside another wife, and he dies, that further co-wife is exempt just as the original co-wife is exempt.',['Successive marriage to second brother and his death'])
edge('firstcase.answer',[8],c1,q,'answer');edge('secondcase.answer',[8],c2,q,'answer');edge('firstcase.analogy',[8],c2,c1,'analogy')
c3=claim('hundred',[8,9],'The recursive exemption still applies even through one hundred such wives.',['Continuation of the successive co-wife example'])
edge('hundred.qual',[9],c3,c2,'qualification')
q2=rec('q.death','questions',[(10,'כיצד אם מתו צרותיהן מותרות')],dict(formulation='How does the death of the forbidden relative leave the co-wife permitted?',question_origin='explicit',conditions=['Death exception'],answer_set_status='partial'))
c4=claim('chronology',[10],'If the daughter or listed relative dies or is divorced before her husband, the brother, dies, her former co-wife is permitted.',['Relative’s death or divorce precedes brother’s death'])
edge('chronology.answer',[10],c4,q2,'answer');edge('chronology.qual',[10],c4,exceptions,'qualification')
c5=claim('unexercised_refusal',[11],'If a relative could have refused the marriage but did not, her co-wife performs halitzah and may not undergo yibbum.',['Refusal was possible but was not exercised'])
edge('refusal.qual',[11],c5,exceptions,'qualification')
notes={0:'General rule reread with fifteen-item list, recursive example and exception clauses.',1:'Four categories read in continuous list; daughter and wife’s daughter kept distinct.',2:'Five categories read in continuous list; mother-in-law generations and exception limitation retained.',3:'Four categories read; maternal brother and maternal sister not generalized to paternal relatives.',4:'Final two categories and repeated general rule retained; no skipped-page renumbering.',5:'Incomplete conditional read together with 2b:3; death and mi’un retained.',6:'Divorce and aylonit complete prior conditional; no standalone unconditional permission.',7:'Both impossibilities scoped to three named maternal-in-law relationships.',8:'Both successive examples and explicit כיצד extracted separately.',9:'Hundred is a continuation of preceding recursive example, not a new subject.',10:'Death/divorce precedes brother’s death; both chronology and question retained.',11:'Unexercised refusal distinguished from completed refusal; halitzah required, yibbum excluded.'}
layers=['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']
for i in range(12):
 for layer in layers:
  ids=[r['id'] for r in p['records'] if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  rationale=notes[i] if layer=='reconciliation' else 'Source-based '+layer+' pass: '+notes[i]
  if not ids:rationale+=' No explicit '+layer+' item in this segment after reading the complete Mishnah and opening Gemara context.'
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
(out/'proposal001.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('records',len(p['records']),'coverage',len(p['coverage']))
