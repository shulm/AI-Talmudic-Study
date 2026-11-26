import json,hashlib,copy
from pathlib import Path
base=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04');out=base/'review_20261126_resume/moed_extended_source_only';sha=lambda b:hashlib.sha256(b).hexdigest()
def get(tr,folder,h):
 p=base/tr/folder/(h+'.json');b=p.read_bytes();assert sha(b)==h;return json.loads(b)
old=get('bavli_moed_katan','snapshots','5fac8984798328adcb8844f711954a943836d40eaad6e6bf605f1589d98cbfaf')
mk=get('bavli_moed_katan','snapshots','bab8114c03ace3430edf6834035c39aaa70169cf0a34da93c34ec07efe7d39cd');mp=get('bavli_moed_katan','proposals','80a0c4d5c3aa7ba443d7c674b102f22dfab2623decd0089197630d250862e924')
a={r['id']:r for r in old['records']};b={r['id']:r for r in mk['records']};edge=b['mk.r009.majority_contrast']
assert edge['content']=={'explicitness':'source_explicit','relation':'distinction','source_id':'mk.r007.ashi_pool.c','target_id':'mk.r007.pappa.c'}
assert edge['links']==['mk.r007.ashi_pool.c','mk.r007.pappa.c']
for id in edge['links']+['mk.r007.pappa_qualifies','mk.r007.ashi_qualifies','mk.r007.time.c','mk.r007.time_support']:assert a[id]==b[id] and b[id]['release_state']=='valid'
rawpath=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Moed/Moed Katan/Hebrew/Wikisource Talmud Bavli.json');raw=rawpath.read_bytes();assert sha(raw)==mp['source_sha256'];t=json.loads(raw)['text'][6][16];e=edge['evidence'][0];assert t[e['start_char']:e['end_char']]==e['quote'];assert e['start_char']==0 and e['end_char']==166
assert len(mp['records'])==1 and mp['records'][0]['id']==edge['id'];assert '80a0c4d5c3aa7ba443d7c674b102f22dfab2623decd0089197630d250862e924' in mk['proposals']
assert any(c['layer']=='edges' and edge['id'] in c['record_ids'] and c['segment_id']==e['segment_id'] for c in mk['coverage'])
ma=get('bavli_makkot','snapshots','4d303ae0cd52352256d5f5b72b0987ab993503d7bae57c18ed40142674fe5cff');ap=get('bavli_makkot','proposals','4952ae9c784c905d6e011b9523144e3628c1c3dfecff5fe390152d4d3ee40e69');m={r['id']:r for r in ma['records']};prev=m['ma.r001.seed.a.scope002'];new=m['ma.r001.seed.a.scope012']
assert new['supersedes']==prev['id'] and new['release_state']=='valid' and prev['release_state']=='superseded'
assert prev['content']['scope']=='ma.r001.seed.c; printed attribution variant unresolved'
assert new['content']['scope']=='ma.r001.seed.c.scope002; printed attribution variant unresolved'
for key in prev:
 if key in ['id','release_state','supersedes','content']:continue
 assert prev[key]==new[key],key
pc=copy.deepcopy(prev['content']);nc=copy.deepcopy(new['content']);del pc['scope'];del nc['scope'];assert pc==nc
assert m[new['content']['scope'].split(';',1)[0]]['release_state']=='valid'
assert len(ap['records'])==1 and ap['records'][0]['id']==new['id'];assert all(m[x]['release_state']=='valid' for x in new['links'])
assert any(new['id'] in c['record_ids'] and c['layer']=='attributions' for c in ma['coverage'])
# Preserve all earlier frozen review artifacts exactly.
assert sha((out/'source_reading_frozen.json').read_bytes())=='70716a6ff353ec78e66b6dac340dd2184312bdb089ec8a367c39867bd3477b95'
assert sha((out/'comparison_5fac8984.json').read_bytes())=='523ce261690a1690a8defe25d5233bb181fd7e2374cc7b98eab86ef8d69665ab'
res={'artifact_type':'additive_targeted_repair_verification','moed_katan':{'snapshot_sha256':'bab8114c03ace3430edf6834035c39aaa70169cf0a34da93c34ec07efe7d39cd','proposal_sha256':'80a0c4d5c3aa7ba443d7c674b102f22dfab2623decd0089197630d250862e924','finding':'F01','original_finding_retained':True,'status':'TARGETED_REPAIR_VERIFIED','scope':'Moed Katan 4a:17 only','verified_edge':edge['id'],'conclusion':'The distinction edge explicitly links Rav Ashi’s even-without-majority position to Rav Pappa’s majority requirement. Direction and evidence fit the source. Its uncertainty explains that distinction encodes contrast without asserting retraction/adjudication. This satisfies F01 under the shared relation vocabulary.','checks':['snapshot/proposal hashes exact','pinned source hash exact','raw 4a:17 span 0:166 equal','both endpoint claims valid and unchanged','previous qualification edges and rationale unchanged','new edge appears in segment edge coverage','proposal adds exactly one record'],'exclusions':['Intervening production through5a:12 is not independently reviewed or accepted by this check.','No new source-blindness claim; this is targeted adjudication after production exposure.']},'makkot':{'snapshot_sha256':'4d303ae0cd52352256d5f5b72b0987ab993503d7bae57c18ed40142674fe5cff','proposal_sha256':'4952ae9c784c905d6e011b9523144e3628c1c3dfecff5fe390152d4d3ee40e69','status':'MECHANICAL_POINTER_REPAIR_VERIFIED','prior_id':prev['id'],'replacement_id':new['id'],'scope_before':prev['content']['scope'],'scope_after':new['content']['scope'],'conclusion':'Embedded ID before the semicolon now targets the valid revised claim. The suffix, candidates, role, surface, chain, raw evidence, uncertainty, links and other non-lineage fields remain identical. Supersession and coverage point to the replacement. No semantic change detected in this record pair.','exclusions':['No independent Makkot source reading or tractate semantic review claimed.','This is a record-pair mechanical check, not verification of the entire snapshot.']},'prior_frozen_artifacts_unchanged':True,'production_writes':False}
p=out/'targeted_repairs_bab8114c_4d303ae0.json';assert not p.exists();p.write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(out/'targeted_repairs_bab8114c_4d303ae0.sha256').write_text(sha(p.read_bytes())+'  '+p.name+'\n',encoding='ascii');print(sha(p.read_bytes()))
