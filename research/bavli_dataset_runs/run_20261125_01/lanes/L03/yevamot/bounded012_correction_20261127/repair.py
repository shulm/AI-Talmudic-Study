import json,hashlib,copy,subprocess
from pathlib import Path
root=Path.cwd();out=Path(__file__).parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');r=lambda f:json.loads(f.read_text(encoding='utf-8-sig'));h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest();review=root/'research/bavli_dataset_runs/run_20261125_01/lanes/L03/yevamot_next20_012_review_20261127/comparison/VERDICT.json';assert h(review)=='85900e7e2f4cde9dec6cc75891e99fb4e42b2d8320204dc2972c189a2bdada98';v=r(review);cur=r(job/'CURRENT.json')['snapshot_sha256'];assert cur==v['snapshot_sha256'];assert r(job/'OWNER.json')=={'owner':'L03/yevamot','epoch':2};base=out.parent/'bounded012_20261127';initial=r(base/'VALIDATION_REVISED_PROPOSAL.json');pins=r(base/'PINS.json');src=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Nashim/Yevamot/Hebrew/Wikisource Talmud Bavli.json');assert h(src)==pins['source_sha256'];a=r(root/'research/bavli_dataset_runs/ACTIVE_RUN.json');cp=root/a['contract_path'];assert h(cp)==a['contract_sha256'];contract=r(cp)
for f,sha in contract['production_files'].items():assert h(root/f)==sha
state=r(job/'snapshots'/(cur+'.json'));gone={x['supersedes'] for x in state['records'] if 'supersedes'in x};old={x['id']:x for x in state['records'] if x['id'] not in gone};inv=r(job/'source_inventory.json');raw=r(src)['text'];p={k:copy.deepcopy(val) for k,val in initial.items() if k not in ['records','coverage']};p.update(records=[],coverage=[]);changes={}
def ev(i):
 s=inv[i];a,b=s['source_index'];assert raw[a][b]==s['text'];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rev(k):
 if k not in changes:
  x={f:copy.deepcopy(old[k][f]) for f in ['id','layer','evidence','content','origin','uncertainty','links']};x['id']='yvfix012.'+k;x['supersedes']=k;changes[k]=x
 return changes[k]
def rec(key,layer,inds,content,links=None):
 rid='yvfix012.'+key;p['records'].append(dict(id=rid,layer=layer,evidence=[ev(i) for i in inds],content=content,origin='source_paraphrase',uncertainty=[],links=list(links or [])));return rid
def cl(key,inds,text,holder='anonymous Gemara',mode='asserted',conditions=None):
 c=list(conditions or []);rid=rec(key,'claims',inds,dict(proposition=text,conditions=c,scope='Local interpretive branch; not adjudicated practical law',assertion_mode=mode));rec(key+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=rid,question_id=None,conditions=c,local_status=mode),[rid]);return rid
def q(key,inds,text):return rec(key,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'))
def ed(key,inds,x,y,rel):return rec(key,'edges',inds,dict(source_id=x,target_id=y,relation=rel,explicitness='source_explicit'),[x,y])
newparts=[]
specs=[
('yev011.context.abaye_exclusion','Abaye excludes the noncontemporary-brother case because his interpretation avoids disputed cases.','abaye_shimon','The noncontemporary-brother configuration can be realized according to Rabbi Shimon.',[219],['Abaye interpretation']),
('yev011.context.ashi_rules','Rav Ashi says Rabbi does not accept these general rules.','ashi_disputed','Rav Ashi says Rabbi does discuss disputed cases.',[225],['Rav Ashi alternative to Rava-reported explanation']),
('yev012.negative_commandment_eligibility','Those subject to negative-commandment prohibitions are candidates for chalitzah in this argument.','yibbum_option','Those subject to negative-commandment prohibitions are candidates for yibbum in this argument.',[236,237],['Alternative procedural categories, not simultaneous duties or unrestricted practical permission']),
('yev012.context.rl_cowife','The chalitzah performer is liable to karet for the co-wife under Resh Lakish’s view.','rl_brother_cowife','The other brothers are liable to karet for the co-wife under Resh Lakish’s view.',[239],['After chalitzah; Resh Lakish’s branch']),
('yev012.context.yohanan_chalutzah','The chalitzah performer is not liable to karet for the chalutzah under Rabbi Yohanan’s view.','yh_brother_chalutzah','The other brothers are not liable to karet for the chalutzah under Rabbi Yohanan’s view.',[240],['After chalitzah; Rabbi Yohanan’s branch']),
('yev012.context.yohanan_cowife','The chalitzah performer is not liable to karet for the co-wife under Rabbi Yohanan’s view.','yh_brother_cowife','The other brothers are not liable to karet for the co-wife under Rabbi Yohanan’s view.',[240],['After chalitzah; Rabbi Yohanan’s branch']),
('yev012.context.performer_only','The chalitzah performer stands under לא יבנה in Resh Lakish’s interpretation.','rl_brothers_prior','The other brothers remain in their prior prohibition status in Resh Lakish’s interpretation.',[241],['Resh Lakish’s limiting interpretation']),
('yev012.context.chalutzah_only','לא יבנה applies to the chalutzah in Resh Lakish’s interpretation.','rl_cowife_prior','The co-wife remains in her prior prohibition status in Resh Lakish’s interpretation.',[242],['Resh Lakish’s limiting interpretation'])]
for oid,t1,key,t2,inds,conditions in specs:
 n=rev(oid);n['content']['proposition']=t1;n['content']['conditions']=list(conditions);n['evidence']=copy.deepcopy(old[oid]['evidence']);pos=rev(oid+'.p');pos['content']['conditions']=list(conditions);pos['evidence']=copy.deepcopy(n['evidence']);holder=pos['content']['holder_candidates'][0];nid=cl(key,inds,t2,holder,conditions=conditions);newparts.append((oid,nid,inds))
no=cl('abaye_sages',[219],'The noncontemporary-brother configuration cannot be realized according to the sages.','Abaye',conditions=['Abaye explanation of his exclusion']);ed('abaye_dispute_reason',[219],no,changes['yev011.context.abaye_exclusion']['id'],'support');ed('abaye_shimon_reason',[219],'yvfix012.abaye_shimon',changes['yev011.context.abaye_exclusion']['id'],'support')
qa=q('abaye_why',[218],'Why does Abaye exclude the noncontemporary-brother case?');ed('abaye_answer',[218,219],changes['yev011.context.abaye_exclusion']['id'],qa,'answer')
qr=q('rebuke_why',[225],'On Rav Ashi’s explanation, what did Rabbi mean by rebuking Levi as though he lacked a brain?');ed('rebuke_answer',[225,226],'yev011.context.judah_identification',qr,'answer')
qm=q('mother_duplication',[227],'What is the mother in the list: if she is the father’s married wife, is that not already the father’s-wife category?')
six=cl('six_severe',[227],'The cited Mishnah lists six relatives more severe than these.','quoted anonymous Mishnah');others=cl('others_marriage',[227],'The cited six are married to others in the Mishnah’s stated explanation.','quoted anonymous Mishnah');permitted=cl('cowives_permitted',[227],'Their co-wives are permitted in the cited Mishnah.','quoted anonymous Mishnah',conditions=['Six severe relatives married to others, as the source states'])
for key,text in [('mother','Mother is separately named in the six-relatives list.'),('father_wife','Father’s wife is separately named in the six-relatives list.'),('father_sister','Father’s sister is separately named in the six-relatives list.')]:cl('list_'+key,[227],text,'quoted anonymous Mishnah')
hyp=cl('married_mother_hypothesis',[227],'The proposed reading identifies mother as the father’s married wife.','anonymous argument','rejected');dup=cl('duplicate_category',[227],'Reading mother as father’s married wife duplicates the separately listed father’s-wife category.');rape=cl('rape_mother',[228],'The argument instead reads mother as the father’s rape victim.','anonymous argument',conditions=['Rav Ashi interpretation of the Mishnah']);other_allowed=cl('others_yes',[228],'The argument reads the cited marriage description as allowing others in this construction.','anonymous argument',conditions=['Local reading of לאחרים']);bro=cl('brothers_no',[228],'The argument excludes marriage to brothers in this construction.','anonymous argument',conditions=['Local inference לאחרים אין לאחין לא']);judah=cl('judah_rape_prohibition',[228],'Rabbi Yehuda prohibits the father’s rape victim.','Rabbi Yehuda');identify=cl('judah_identification',[228],'The exclusion of brothers identifies this Mishnah’s view with Rabbi Yehuda.','anonymous argument',conditions=['Rav Ashi branch'])
ed('dup_objection',[227],dup,hyp,'objection');ed('dup_support',[227,228],dup,rape,'support');ed('rape_answer',[227,228],rape,qm,'answer');ed('others_inference',[227,228],others,other_allowed,'support');ed('brothers_inference',[227,228],others,bro,'support');ed('identification_support',[228],bro,identify,'support');ed('judah_rule_support',[228],judah,identify,'support');ed('summary_support',[226,228],identify,'yev011.context.judah_identification','support');ed('rape_qualification',[228],rape,bro,'qualification');ed('cowife_conditions',[227],others,permitted,'qualification')
# Preserve dependent identities and all split source-supported relations.
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
 if isinstance(x,dict):return {k:repl(v) for k,v in x.items()}
 return x
for x in changes.values():p['records'].append(x)
for x in p['records']:x['content']=repl(x['content']);x['links']=repl(x['links'])
# Existing edges revised to primary atoms; replicate relations to complementary atoms where their original scope covered both.
for oid,nid,inds in newparts:
 if oid in ['yev011.context.abaye_exclusion','yev012.context.performer_only','yev012.context.chalutzah_only']:continue
 for x in old.values():
  if x['layer']!='edges':continue
  c=x['content']
  if oid not in [c['source_id'],c['target_id']]:continue
  nc=repl(copy.deepcopy(c));nc['source_id']=nid if c['source_id']==oid else nc['source_id'];nc['target_id']=nid if c['target_id']==oid else nc['target_id'];rec('split_edge.'+nid+'.'+x['id'],'edges',sorted(set(inds+[next(i for i,s in enumerate(inv) if s['id']==e['segment_id']) for e in x['evidence']])),nc,[nc['source_id'],nc['target_id']])
# Split prior-status claims, rather than positive לא יבנה cells, supply exclusion support.
for oid,newsource in [('yev012.context.man_support','yvfix012.rl_brothers_prior'),('yev012.context.woman_support','yvfix012.rl_cowife_prior')]:
 n=changes[oid];n['content']['source_id']=newsource;n['links']=[newsource,n['content']['target_id']]
ed('cowife_other_prior_support',[239,242],'yvfix012.rl_cowife_prior','yvfix012.rl_brother_cowife','support')
active={k:x for k,x in old.items() if k not in changes};active.update({x['id']:x for x in p['records']})
for c in state['coverage']:
 n=repl({k:copy.deepcopy(val) for k,val in c.items() if k!='proposal_execution'});extras=[x['id'] for x in p['records'] if x.get('supersedes') is None and (x['layer']==c['layer'] or (c['layer']=='reconciliation' and x['layer'] in ['claims','edges','questions'])) and any(e['segment_id']==c['segment_id'] for e in x['evidence'])];n['record_ids']+=list(dict.fromkeys(k for k in extras if k not in n['record_ids']))
 if n['record_ids']!=c['record_ids']:n['extraction_result']='records_found';n['rationale']+=' Y012 explicit question/argument omissions and atomic branch correction; no new source coverage.';p['coverage'].append(n)
for x in active.values():
 assert not strings([x['content'],x['links']])&set(changes)
 for k in x['links']:assert k in active
for c in p['coverage']:
 for k in c['record_ids']:assert any(e['segment_id']==c['segment_id'] for e in active[k]['evidence'])
(out/'PROPOSAL.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(proposal=h(out/'PROPOSAL.json'),records=len(p['records']),revisions=len(changes))))


