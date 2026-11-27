"""Explicit source-reread corrections, preserving complete dependency lineage.

No semantic heuristics: all changed interpretation fields are listed below.
Graph traversal only propagates new record IDs to their dependent records.
"""
from author_remaining_openings_001 import r,Reading
from copy import deepcopy
import sys

slug=sys.argv[1];title={'moed_katan':'Moed Katan','makkot':'Makkot','nedarim':'Nedarim'}[slug]
a=Reading(slug,title,{'moed_katan':'mk.r001','makkot':'ma.r001','nedarim':'nd.r001'}[slug]);state=r.current(a.job)
active={x['id']:x for x in state['records'] if x['release_state']=='valid'};changed={}
def edit(id):
    if id not in changed:changed[id]=deepcopy(active[id])
    return changed[id]
def narrow(id,quote,voice=None):
    row=edit(id);e=row['evidence'][0];s=a.source[e['segment_id']];text=s['text'];assert text.count(quote)==1,(id,quote);start=text.index(quote)
    row['evidence']=[dict(segment_id=s['id'],start_char=start,end_char=start+len(quote),quote=quote)]
    row['content']['composition']='atomic'
    if voice:row['content']['textual_voice']=voice
# Broad source-context utterances are not certified atomic speech units.
# Keep normalized propositions separately; narrower atomic units need later work.
for id,row in active.items():
    if row['layer']=='utterances' and row['content']['composition']=='atomic':
        out=edit(id);out['content']['composition']='composite';out['uncertainty']=out['uncertainty']+['Evidence span retains broader discourse context; do not use as a certified atomic utterance boundary.']
        if row['content']['textual_voice']=='anonymous discussion':out['content']['textual_voice']='anonymous discourse framing, including embedded quotations where present'
if slug=='moed_katan':
    spans={
    'channelzea':"ר' אלעזר בן עזריה אומר אין עושין את האמה בתחילה במועד ובשביעית",
    'channelsages':'וחכמים אומרים עושין את האמה בתחילה בשביעית',
    'repair':'ומתקנין את המקולקלות במועד',
    'huna':"אמר רב הונא ר' אליעזר בן יעקב היא",
    'tree':'דתנן רבי אליעזר בן יעקב אומר מושכין את המים מאילן לאילן ובלבד שלא ישקה את השדה כולה',
    'pappa':'אלא אמר רב פפא הא מני רבי יהודה היא',
    'meir':'דתניא מעיין היוצא בתחילה משקין ממנו אפילו שדה בית הבעל דברי רבי מאיר',
    'yehuda':'רבי יהודה אומר אין משקין אלא שדה בית השלחין שחרבה',
    'azar':'רבי אלעזר בן עזריה אומר לא כך ולא כך',
    'redirect':'יתר על כן אמר רבי יהודה לא יפנה אדם אמת המים וישקה לגינתו ולחורבתו בחולו של מועד',
    'abaye':'אמר אביי שחרבה ממעיין זה ויצא לה מעיין אחר'}
    for key,quote in spans.items():narrow('mk.r001.'+key+'.u',quote)
    edit('mk.r001.huna.c')['content']['assertion_mode']='rejected'
    edit('mk.r001.huna.p')['content']['local_status']='Proposed identification rejected and replaced by Rav Pappa at2a:12; the quoted Rabbi Eliezer ben Yaakov irrigation rule is preserved.'
    edit('mk.r001.huna.u')['content']['discourse_role']='rejected identification proposal'
    edit('mk.r001.result.u')['content']['textual_voice']='anonymous resolution attributing a view to Rabbi Yehuda'
    edit('mk.r001.result.a')['content']['role']='position_holder'
    edit('mk.r001.azarclar.u')['content']['textual_voice']='anonymous clarification of Rabbi Elazar ben Azarya’s quoted position'
    edit('mk.r001.azarclar.a')['content']['role']='position_holder'
elif slug=='makkot':
    narrow('ma.r001.pada.u','בר פדא אומר ק"ו ומה המחלל אינו מתחלל הבא לחלל ולא חילל אינו דין שלא יתחלל')
    narrow('ma.r001.ravina.u','מתקיף לה רבינא אם כן בטלת תורת עדים זוממין')
    narrow('ma.r001.lakish.u','אמר ר"ל דאמר קרא (דברים יט, ה) הוא ינוס אל אחת הערים הוא ולא זוממין')
    narrow('ma.r001.ulla.u','אמר עולא רמז לעדים זוממין מן התורה מנין','עולא')
    out=edit('ma.r001.ulla.a');out['content'].update(surface='אמר עולא',role='speaker',candidates=['עולא'])
    edit('ma.r001.ulla.q')['uncertainty'].append('Ulla’s initial question is clarified by the anonymous discussion as concerning lashes; do not attribute the anonymous clarification itself as a separate verbatim Ulla speech.')
    narrow('ma.r001.verse.u','דכתיב (דברים כה, א) והצדיקו את הצדיק והרשיעו את הרשע (דברים כה, ב) והיה אם בן הכות הרשע','Scriptural derivation presented for Ulla’s clarified question')
    edit('ma.r001.seed.u')['content']['textual_voice']='Named attribution with unresolved printed parenthetical variant; see linked attribution record'
# Remove the broad-span caution when an actual narrow span has just been supplied.
for row in changed.values():
    if row['layer']=='utterances' and row['content']['composition']=='atomic':row['uncertainty']=[x for x in row['uncertainty'] if not x.startswith('Evidence span retains broader')]
def dependencies(row):
    out=list(row['links']);c=row['content']
    if row['layer']=='positions':out += [c['claim_id']]+([c['question_id']] if c['question_id'] else [])
    if row['layer']=='edges':out += [c['source_id'],c['target_id']]
    return out
again=True
while again:
    again=False
    for id,row in active.items():
        if id not in changed and any(x in changed for x in dependencies(row)):edit(id);again=True
mapping={id:id+'.scope002' for id in changed};new=[]
for old,row in changed.items():
    for k in ['release_state','review_state','ml_eligible']:row.pop(k,None)
    row['id']=mapping[old];row['supersedes']=old;row['links']=[mapping.get(x,x) for x in row['links']];c=row['content']
    if row['layer']=='positions':c['claim_id']=mapping.get(c['claim_id'],c['claim_id']);c['question_id']=mapping.get(c['question_id'],c['question_id'])
    if row['layer']=='edges':
        for key in ['source_id','target_id']:c[key]=mapping.get(c[key],c[key])
    new.append(row)
if slug=='moed_katan':
    new.append(dict(id='mk.r002.pappa_replaces_huna',layer='edges',content=dict(source_id=mapping.get('mk.r001.pappa.c','mk.r001.pappa.c'),target_id=mapping['mk.r001.huna.c'],relation='correction',explicitness='source_explicit'),evidence=[a.evidence('2a:12')],links=[mapping.get('mk.r001.pappa.c','mk.r001.pappa.c'),mapping['mk.r001.huna.c']],uncertainty=[],origin='source_paraphrase'))
cov=[]
for row in state['coverage']:
    row=deepcopy(row);row.pop('proposal_execution',None);row['record_ids']=[mapping.get(x,x) for x in row['record_ids']]
    if slug=='moed_katan' and row['segment_id']==a.refs['2a:12']['id'] and row['layer']=='edges':row['record_ids'].append('mk.r002.pappa_replaces_huna')
    row['rationale']+=' Source reread scope correction: broad-span utterances declared composite, named multi-speaker spans narrowed where explicitly listed; full dependency lineage retained.'
    cov.append(row)
p=dict(schema_version=r.VERSION,tractate=title,owner='L04/'+slug+'_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=new,coverage=cov,open_tails=[mapping.get(x,x) for x in state['open_tails']])
out=a.job/'staging'/'scope_correction_002.json';r.immutable(out,r.encoded(p));print(out)
