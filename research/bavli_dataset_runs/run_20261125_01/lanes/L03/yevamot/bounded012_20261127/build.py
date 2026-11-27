import json,hashlib,copy
from pathlib import Path
root=Path.cwd();out=Path(__file__).parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');r=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();a=r(Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_dataset_runs/ACTIVE_RUN.json'));cp=root/a['contract_path'];assert h(cp)==a['contract_sha256'];contract=r(cp)
for f,sha in contract['production_files'].items():assert h(root/f)==sha
assert r(job/'OWNER.json')=={'owner':'L03/yevamot','epoch':2};cur=r(job/'CURRENT.json')['snapshot_sha256'];assert cur=='2a6cbf49cca3c418dcdf5ae8299d5ed2ffdbddc626cbffdbbd456f73ae83d058';assert h(job/'snapshots'/(cur+'.json'))==cur;state=r(job/'snapshots'/(cur+'.json'));assert state['open_tails']==['yev011.sixteenth'];src=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Nashim/Yevamot/Hebrew/Wikisource Talmud Bavli.json');ss=Path('F:/Sefaria-Export-master/schemas/Yevamot.json');assert h(src)=='e3f2ddea9c75119de9dd032ca9cf91108d55c332ca8eeab4fb0997ed1eca5a07';assert h(ss)=='e3dd6cc777b473fbe6e45be722dd0294885429ea29215fb776cfb3e09a948e23';inv=r(job/'source_inventory.json');raw=r(src)['text'];core=inv[218:238]
for s in inv[218:257]:i,j=s['source_index'];assert raw[i][j]==s['text']
meta=r(job/'JOB.json');p={k:meta[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/yevamot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/yevamot',model_id=None),records=[],coverage=[],open_tails=['yev012.chalitzah_dialogue'])
def ev(i,q=None):
 s=inv[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=None,u=None,origin='source_paraphrase'):
 rid='yev012.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(*i) if isinstance(i,tuple) else ev(i) for i in inds],content=c,origin=origin,links=list(links or []),uncertainty=list(u or [])));return rid
def claim(k,inds,text,cond=None,holder='anonymous Gemara',mode='asserted',u=None):
 cid=rec(k,'claims',inds,dict(proposition=text,conditions=list(cond or []),scope='Local dialogue or marked continuation interpretation; unresolved alternatives preserved',assertion_mode=mode),u=u);rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond or []),local_status=mode+' at this stage; explicit later alternatives remain distinct'),[cid],u);return cid
def q(k,inds,text):return rec(k,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,inds,x,y,rel):return rec(k,'edges',inds,dict(source_id=x,target_id=y,relation=rel,explicitness='source_explicit'),[x,y])
def attr(k,inds,surface,role,candidates,scope,chain=None):return rec(k,'attributions',inds,dict(surface=surface,role=role,candidates=list(candidates),scope=scope,transmission_chain=list(chain or [])))
gone={x['supersedes'] for x in state['records'] if 'supersedes'in x};old={x['id']:x for x in state['records'] if x['id'] not in gone};changes={}
def rev(k):
 if k not in changes:
  n={f:copy.deepcopy(old[k][f]) for f in ['id','layer','evidence','content','origin','uncertainty','links']};n['id']='yev012.revised.'+k;n['supersedes']=k;changes[k]=n
 return changes[k]
s=rev('yev011.sixteenth');s['evidence']=[ev(i) for i in range(203,234)];s['content'].update(boundary='closed',title='Levi sixteenth case, alternative explanations of Rabbi and distinct mother-marriage histories through10b1');s['uncertainty']=['Competing interpretations retained; Levi addition is not an attributed retraction by Rabbi.']
rec('chalitzah_dialogue','structure',list(range(234,238)),dict(title='Levi addition leads to chalitzah-remarriage proposed exemption; Yohanan answers on Resh Lakish assumptions, dispute developed in continuation',primary=True,boundary='open_right',legacy_ids=[]),u=['Continuation through11a8 read; not counted as core. Detailed later baraita reconciliations remain for next batch.'],origin='editorial_inference')
roles=['Abaye includes daughter from rape','Abaye excludes disputed noncontemporary brother','Rav Safra includes case under Rabbi Shimon','Six-brother mnemonic crosses folio','Rava report answers Rabbi rules question','Two sisters positive/negative configuration','Two unrelated women positive/negative configuration','Rav Ashi alternative Rabbi interpretation','Rabbi Yehuda identification','Mother versus father-wife duplication question','Rape mother reading supports identification','Ravina transgression objection and exclusion','Rav Ashi proposed daughter-in-law construction','Lawful sister restriction; Levi adds nevertheless','Levi no-exemption marriage history','Levi exemption rape history','Levi sixteenth conclusion and Resh Lakish additional case','Yohanan co-wife-of-co-wife answer','Anonymous negative-commandment objection','Answer scoped to interlocutor premise']
for i,role in zip(range(218,238),roles):
 if not any(x['layer']=='utterances' and any(e['segment_id']==inv[i]['id'] for e in x['evidence']) for x in old.values()):rec('u'+str(i),'utterances',[i],dict(textual_voice='Gemara dialogue; named reports separately scoped',discourse_role=role,composition='composite'))
 if not any(x['layer']=='attributions' and any(e['segment_id']==inv[i]['id'] for e in x['evidence']) for x in old.values()):attr('anon'+str(i),[i],'anonymous framing','anonymous',[],role+'; named holder roles retained separately')
levi=claim('sixteenth_conclusion',[234],'Levi’s teaching adds a sixteenth case despite the fifteen listed by the sages.',['Conclusion of Levi’s distinct added teaching'],'Levi');edge('levi_completion',[233,234],'yvfix011.context.levi_exemption',levi,'support')
ask=q('additional_case',[234],'Resh Lakish asks Rabbi Yohanan: since Levi includes transgressive constructions, why not list a man who performed chalitzah, betrothed the same woman again, and died childless, so her prohibition would also prohibit her co-wife?');attr('rl_question',[234],'א״ל ר״ל לרבי יוחנן','speaker',['Resh Lakish'],'Question to Rabbi Yohanan, not transmission');attr('yohanan_answer',[234,235],'א״ל','speaker',['Rabbi Yohanan'],'Reply to Resh Lakish in the continuing dialogue')
co=claim('no_further_cowife',[235],'The proposed chalitzah-remarriage case does not yield the co-wife-of-co-wife case.',['Response on Resh Lakish’s premise, as explicitly qualified at10b5'],'Rabbi Yohanan');edge('case_answer',[234,235],co,ask,'answer')
why=q('negative_commandment_objection',[236],'Why not answer that these are negative-commandment prohibitions and remain subject to chalitzah and yibbum?');edge('answer_objection',[235,236],why,co,'objection')
own=claim('yohanan_own_classification',[237],'Rabbi Yohanan’s own view classifies the women here under negative-commandment prohibition.',['His own view, distinct from the premise he uses in answering'],'Rabbi Yohanan');eligible=claim('negative_commandment_eligibility',[236,237],'Those under negative-commandment prohibition are subject to chalitzah and yibbum in this argument.',['This passage’s classification; do not infer an unqualified practical permission'],'Rabbi Yohanan');onpremise=claim('interlocutor_premise',[237],'Rabbi Yohanan answers on Resh Lakish’s premise that these are karet prohibitions.',['Argument addressed to Resh Lakish, not Rabbi Yohanan endorsing the classification'],'anonymous explanation of Rabbi Yohanan','conditional');edge('scope_answer',[237],onpremise,why,'answer');edge('qualify_earlier_answer',[235,237],onpremise,co,'qualification');edge('own_vs_conceded',[237],own,onpremise,'distinction');edge('own_reason',[236,237],eligible,why,'support')
# Minimal substantive context needed to disambiguate the conceded premise.
rlself=claim('context.rl_self',[238],'The chalitzah-performing man is not liable to karet for the woman who received his chalitzah.',['After chalitzah in the stated remarriage discussion'],'Resh Lakish')
rlbro=claim('context.rl_brothers',[239],'The other brothers are liable to karet for the woman who received chalitzah.',['Resh Lakish’s distinction between performer and other brothers'],'Resh Lakish')
rlco=claim('context.rl_cowife',[239],'Both the performer and his brothers are liable to karet for her co-wife.',['Resh Lakish’s distinction between chalutzah and co-wife'],'Resh Lakish')
yh=claim('context.yohanan_chalutzah',[240],'Neither the performer nor his brothers are liable to karet for the chalutzah.',['Rabbi Yohanan’s competing view'],'Rabbi Yohanan');yhc=claim('context.yohanan_cowife',[240],'Neither the performer nor his brothers are liable to karet for the co-wife.',['Rabbi Yohanan’s competing view'],'Rabbi Yohanan')
attr('context.rl',[238,239],'אמר ר״ל','position_holder',['Resh Lakish'],'Performer, brothers, chalutzah and co-wife liability distinctions');attr('context.yohanan',[240],'ורבי יוחנן אמר','position_holder',['Rabbi Yohanan'],'Competing no-karet view')
qreason=q('context.rl_reason',[240],'What is Resh Lakish’s reason?');verse=claim('context.no_rebuild',[240],'אשר לא יבנה is read: having not built, he may no longer build.',['Derivation of the prohibition following chalitzah'],'Resh Lakish');man=claim('context.performer_only',[241],'The performer stands under לא יבנה; the brothers remain in their earlier prohibition status.',['Resh Lakish’s limiting interpretation'],'Resh Lakish');woman=claim('context.chalutzah_only',[242],'לא יבנה applies to the chalutzah in this reading; her co-wife remains in the earlier status.',['Resh Lakish’s limiting interpretation'],'Resh Lakish');edge('context.reason',[240],verse,qreason,'answer');edge('context.man_support',[239,241],man,rlbro,'support');edge('context.woman_support',[239,242],woman,rlco,'support')
qagency=q('context.yohanan_objection',[243],'How can karet arise now when previously either brother could perform chalitzah and either woman could receive it?');edge('context.liability_objection',[239,243],qagency,rlbro,'objection');edge('context.cowife_objection',[239,243],qagency,rlco,'objection')
agentman=claim('context.brother_agency',[244],'The performing brother acts on behalf of the brothers.',['Rabbi Yohanan’s explanation of chalitzah effect'],'Rabbi Yohanan');agentwoman=claim('context.cowife_agency',[244],'The chalutzah acts on behalf of the co-wife.',['Rabbi Yohanan’s explanation of chalitzah effect'],'Rabbi Yohanan');edge('context.agency_answer',[243,244],agentman,qagency,'answer');edge('context.agency_cowife_answer',[243,244],agentwoman,qagency,'answer');edge('context.brother_no_karet',[240,244],agentman,yh,'support');edge('context.cowife_no_karet',[240,244],agentwoman,yhc,'support');edge('context.own_view_support',[237,240],yh,own,'continuation')

def strings(x):
 if isinstance(x,str):return {x}
 if isinstance(x,list):return set().union(*(strings(y) for y in x)) if x else set()
 if isinstance(x,dict):return strings(list(x.values()))
 return set()
while True:
 more=[k for k,x in old.items() if k not in changes and strings([x['content'],x['links']])&set(changes)]
 if not more:break
 for k in more:rev(k)
mp={k:x['id'] for k,x in changes.items()}
def repl(x):
 if isinstance(x,str):return mp.get(x,x)
 if isinstance(x,list):return [repl(y) for y in x]
 if isinstance(x,dict):return {k:repl(y) for k,y in x.items()}
 return x
for x in changes.values():x['content']=repl(x['content']);x['links']=repl(x['links']);p['records'].append(x)
for c in state['coverage']:
 if set(c['record_ids'])&set(changes):p['coverage'].append(repl({k:copy.deepcopy(v) for k,v in c.items() if k!='proposal_execution'}))
active={k:x for k,x in old.items() if k not in changes};active.update({x['id']:x for x in p['records']})
for s,role in zip(core,roles):
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  matches=[x['id'] for x in active.values() if x['layer']==layer and any(e['segment_id']==s['id'] for e in x['evidence'])]
  if layer=='reconciliation':matches=[x['id'] for x in active.values() if x['layer'] in ['claims','edges','structure'] and any(e['segment_id']==s['id'] for e in x['evidence'])]
  p['coverage'].append(dict(segment_id=s['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if matches else 'none_found_after_pass',record_ids=matches,rationale=role+'. Full source/continuation read through11a8; prior accepted context218–233 reused. Counterclaims, named transmission, alternatives and omission check retained. '+('Evidence-bearing '+layer+' rows.' if matches else 'No explicit '+layer+' finding after pass; no fabricated findings.')))
for x in p['records']:
 for e in x['evidence']:
  s=next(s for s in inv if s['id']==e['segment_id']);assert s['text'][e['start_char']:e['end_char']]==e['quote']
 for k in x['links']:assert k in active
for c in p['coverage']:
 for k in c['record_ids']:assert any(e['segment_id']==c['segment_id'] for e in active[k]['evidence'])
(out/'INITIAL_PROPOSAL.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(out/'PINS.json').write_text(json.dumps(dict(parent_snapshot=cur,contract_sha256=h(cp),production_git_commit=contract['production_git_commit'],schema_sha256=contract['schema_sha256'],protocol_sha256=contract['annotation_protocol_sha256'],source_sha256=h(src),source_schema_sha256=h(ss),owner=r(job/'OWNER.json'),core_refs=[s['ref'] for s in core],core_indices=[s['source_index'] for s in core],revision_map=mp,independent_reading_seen=False,context_through='Yevamot11a8; direct liability context238–244 extracted, later baraita alternatives read but remain next-core work',uncertainties=['Prior Abaye/Rav Safra/Rava/Rav Ashi alternatives retained without new duplicate claims.','Rabbi Yohanan own classification differs from argument on Resh Lakish premise.','Context chalitzah liability is a local dispute, not adjudicated halakhah.','Full continuation through11a8 read: Rav Sheshet explanation challenged, Rav Ashi and Ravina alternate baraita readings; exact born-brothers terms reserved for next core rather than guessed.','Rav Aha/Ravina positions at11a7–8 remain unassigned by name order.','Context238–244 uncounted; open yev012.chalitzah_dialogue.']),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(proposal=h(out/'INITIAL_PROPOSAL.json'),records=len(p['records']),revisions=len(changes))))
