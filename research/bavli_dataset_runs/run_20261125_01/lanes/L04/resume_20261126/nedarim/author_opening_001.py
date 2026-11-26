"""Manually authored Nedarim opening; serializers do not infer semantics."""
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
spec=importlib.util.spec_from_file_location('r',ROOT/'bavli_production_v1/runner.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_nedarim');meta,ss=r.load(JOB)
assert meta['source_sha256']=='52a452f67441cc435f1908275e349834ddc53a2add513905d52e6a0a186e85a1'
refs={s['ref'].split(' ',1)[1]:s for s in ss.values()};records=[]
def ev(ref,quote=None):
    s=refs[ref];t=s['text'];q=t if quote is None else quote;assert t.count(q)==1,(ref,q);a=t.index(q)
    return dict(segment_id=s['id'],start_char=a,end_char=a+len(q),quote=q)
def add(key,layer,content,e,links=(),uncertainty=(),origin='source_paraphrase'):
    id='nd.r001.'+key;records.append(dict(id=id,layer=layer,content=content,evidence=e,links=list(links),uncertainty=list(uncertainty),origin=origin));return id
def speech(key,ref,quote,voice='anonymous discussion',role='assertion',composition='atomic'):
    e=[ev(ref,quote)];u=add(key+'.u','utterances',dict(textual_voice=voice,discourse_role=role,composition=composition),e)
    add(key+'.a','attributions',dict(surface=voice if voice!='anonymous discussion' else '',role='speaker' if voice!='anonymous discussion' else 'anonymous',candidates=[voice] if voice!='anonymous discussion' else [],scope=u,transmission_chain=[]),e,[u]);return u
def c(key,ref,quote,text,mode='asserted',holder=None,conditions=(),uncertainty=(),scope='Local explanation of Mishnah arrangement'):
    e=[ev(ref,quote)];u=speech(key,ref,quote,holder or 'anonymous discussion',mode)
    x=add(key+'.c','claims',dict(proposition=text,conditions=list(conditions),scope=scope,assertion_mode=mode),e,[u],uncertainty)
    add(key+'.p','positions',dict(holder_candidates=[holder] if holder else [],claim_id=x,question_id=None,conditions=list(conditions),local_status=mode+' in local discourse; no final practical ruling inferred'),e,[x],uncertainty)
    return x
def q(key,ref,quote,text):
    u=speech(key,ref,quote,role='question');return add(key+'.q','questions',dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='none'),[ev(ref,quote)],[u])
def edge(key,a,b,rel,ref,quote=None):return add(key,'edges',dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[ev(ref,quote)],[a,b])
opening=['2a:'+str(i) for i in range(1,5)];arrange=['2b:'+str(i) for i in range(1,15)]+['3a:'+str(i) for i in range(1,5)]
add('mishnah','structure',dict(title='Equivalent vow expressions, abbreviated formulations and cautious ban wording',primary=True,boundary='closed',legacy_ids=[]),[ev(x) for x in opening],origin='editorial_inference')
add('arrangement','structure',dict(title='Why categories and abbreviated formulas occur in this Mishnah order',primary=True,boundary='closed',legacy_ids=[]),[ev(x) for x in arrange],origin='editorial_inference')
c('vows','2a:1','כינויי נדרים כנדרים','Substitute expressions for vows have the force of vows.',scope='Mishnah category equivalence; nature of substitutes disputed later')
for key,quote,text in [('herem','וחרמים כחרמים','Substitute expressions for herem declarations have their force.'),('oaths','ושבועות כשבועות','Substitute expressions for oaths have the force of oaths.'),('nazir','ונזירות כנזירות','Substitute expressions for naziriteship have its force.')]:c(key,'2a:2',quote,text,scope='Mishnah category equivalence')
formula=c('formula','2a:3',None,'The Mishnah lists מודרני, מופרשני and מרוחקני together with שאני אוכל לך and שאני טועם לך and states prohibition.',conditions=['the listed relational and eating/tasting formulations'],scope='Printed Mishnah formulas, not a resolved interpretation of independent versus combined sufficiency',uncertainty=['Shmuel’s multiple formulations and objections at4b:6 onward were read as context. Combination/scope must remain unresolved here; do not turn the list into independent binary choices.'])
c('akiva','2a:4',None,'For מנודה אני לך Rabbi Akiva leans toward stringency.',holder='רבי עקיבא',conditions=['formula מנודה אני לך'],mode='unresolved',scope='Mishnah cautious tendency, not an unqualified prohibition')
why=q('categories','2b:1',None,'Why does Nazir omit the full category list whereas Nedarim includes all categories?')
pair=c('pair','2b:2','משום דנדר ושבועה כתיבי גבי הדדי תני תרתין','Vow and oath are written together, so both are taught.')
allc=c('all','2b:2','וכיון דתני תרתין תני לכולהו','Once two categories are taught, all are taught.')
edge('pair.answer',pair,why,'answer','2b:2');edge('all.support',pair,allc,'support','2b:2')
oathq=q('oathorder','2b:3','וליתני כינוי שבועות בתר נדרים','Why not list oath expressions immediately after vows?')
objectvow=c('objectvow','2b:3','איידי דתנא נדרים דמיתסר חפצא עליה','A vow prohibits the object to the person.')
objectherem=c('objectherem','2b:3','תנא נמי חרמים דמיתסר חפצא עליה','Herem likewise prohibits the object to the person, explaining its placement next to vows.')
personoath=c('personoath','2b:3','לאפוקי שבועה דקאסר נפשיה מן חפצא','An oath instead prohibits the person with respect to the object.')
edge('herem.answer',objectherem,oathq,'answer','2b:3');edge('oath.distinction',personoath,objectvow,'distinction','2b:3')
orderq=q('order','2b:4','פתח בכינויין  כל כנויי נדרים ומפרש ידות  האומר לחבירו מודר אני ממך','Why begin with substitute expressions but explain abbreviated formulations?')
missingq=q('missing','2b:4','ותו  ידות אינשי','Have abbreviated formulations been omitted from the opening?')
reconstruct=c('reconstruct','2b:5',None,'The response supplies missing wording: both substitutes and abbreviated vow formulas have the force of vows.',scope='Explicit חסורי מיחסרא reconstruction; preserve printed original separately')
edge('reconstruct.answer',reconstruct,missingq,'answer','2b:5');edge('reconstruct.order',reconstruct,orderq,'answer','2b:5')
firstq=q('first','2b:6',None,'Why not explain substitute expressions first?')
last=c('last','2b:7','ההוא דסליק מיניה ההוא מפרש ברישא','The initial explanation says the most recently mentioned category is explained first.',mode='challenged')
edge('last.answer',last,firstq,'answer','2b:7')
examples=[]
for key,ref,quote,text in [
('lighting','2b:7',"כדתנן  במה מדליקין ובמה אין מדליקין  אין מדליקין כו'",'The lighting Mishnah first explains prohibited lighting materials after listing permitted then prohibited.'),
('insulation','2b:8',"במה טומנין ובמה אין טומנין אין  טומנין כו'",'The insulation Mishnah first explains prohibited insulation after listing permitted then prohibited.'),
('woman','2b:8','במה אשה יוצאה ובמה אינה יוצאה  לא תצא אשה','The woman-going-out Mishnah first explains what she may not wear after listing both headings.')]:
    x=c(key,ref,quote,text,scope='Quoted editorial-order example, not extraction of the entire cited law');edge(key+'.support',x,last,'support',ref,quote);examples.append(x)
alwaysq=q('always','2b:9','וכל היכא דפתח לא מפרש ברישא','Is the category mentioned first never explained first?')
counter=[]
for key,ref,quote,text in [
('inherit','2b:9','והתנן  יש נוחלין ומנחילין נוחלין ולא מנחילין ואלו נוחלין ומנחילין','Inheritance categories are followed by an explanation of the category listed first.'),
('wives','2b:10',None,'The husband/levir permission categories are followed by the category listed first.'),
('oil','2b:11','יש טעונות שמן ולבונה שמן ולא לבונה ואלו טעונות שמן ולבונה','Oil-and-frankincense categories are followed by the category listed first.'),
('presentation','2b:11','יש טעונות הגשה ואין טעונות תנופה תנופה ולא הגשה ואלו טעונות הגשה','Presentation/waving categories are followed by presentation, mentioned first.'),
('firstborn','2b:12',None,'Inheritance/priestly firstborn categories are followed by the category mentioned first.')]:
    x=c(key,ref,quote,text,scope='Counterexample about exposition order; complete cited laws not inferred');edge(key+'.objection',x,last,'objection',ref,quote);counter.append(x)
many=c('many','2b:13',None,'The proposed distinction says those examples have many categories, so the first category is explained first.',mode='rejected',conditions=['many categories'],scope='Attempted editorial explanation, rejected by the next short example')
edge('many.answer',many,counter[0],'answer','2b:13')
animal=c('animal','2b:14',None,'The animal-going-out Mishnah has few categories but starts with the permitted camel case, contradicting the proposed distinction.')
edge('animal.objection',animal,many,'objection','2b:14')
flexible=c('flexible','3a:1','אלא לאו דווקא זימנין מפרש ההוא דפתח ברישא זימנין ההוא דסליק מפרש ברישא','The resolution is that the order is not fixed: sometimes the first category is explained first, sometimes the last.',mode='reconciled')
derived=c('derived','3a:1','ואיבעית אימא  ידות איידי דאתיין מדרשא מפרש להון ברישא','Alternatively, abbreviated formulas are explained first because they are derived by exposition.',scope='Explicit alternative explanation, not cumulative with fixed-order rule')
edge('flexible.correction',flexible,last,'correction','3a:1');edge('flexible.answer',flexible,alwaysq,'answer','3a:1');edge('derived.answer',derived,firstq,'answer','3a:1')
beginq=q('begin','3a:2','וליפתח הדין ברישא','Why not also begin with abbreviated formulas?')
direct=c('direct','3a:2','מיפתח פתח בכינויין דאורייתא ברישא והדר מפרש ידות דאתיין ליה מדרשא','The reply begins with substitutes regarded as Torah-level wording, then explains the abbreviated formulas derived by exposition.',mode='challenged',scope='Explanation subsequently tested against two accounts of substitutes')
edge('direct.answer',direct,beginq,'answer','3a:2')
foreign=c('foreign','3a:3','הניחא למאן דאמר  כינויין לשון נכרים הן','The explanation works for the view that substitutes are foreign-language expressions.',conditions=['substitutes are foreign-language expressions'],scope='Unnamed doctrinal alternative; no holder assigned')
invented=c('invented','3a:3',"אלא למ''ד  לשון שבדו להן חכמים להיות נודר בו",'Another unnamed view treats substitutes as expressions invented by the sages for making vows.',scope='Unnamed alternative; no name-order attribution')
inventq=q('inventedquestion','3a:3','מאי איכא למימר','What explains the ordering on the invented-expression view?')
edge('invented.objection',invented,direct,'objection','3a:3')
printed=q('printed','3a:4','מי קתני ידות  ולאו חסורי קא מחסרת לה','Does the printed Mishnah say abbreviated formulas, or are you supplying missing wording?')
reorder=c('reorder','3a:4','אקדים נמי ותני ידות  כל ידות נדרים כנדרים וכל כינויי נדרים כנדרים','Since missing wording is supplied, the reconstruction may put abbreviated formulas first and substitutes afterward.',scope='Alternative reconstructed wording, not an emendation of original source bytes')
definition=c('definition','3a:4','ואלו הן ידות  האומר לחבירו ואלו הן כינויין  קונם קונח קונס','In that reconstructed order the relational formulas exemplify abbreviated vows, while קונם, קונח and קונס exemplify substitutes.',scope='Reconstructed category examples; preserves exact three printed forms')
edge('reorder.answer',reorder,inventq,'answer','3a:4');edge('definition.support',definition,reorder,'support','3a:4')
notes={
'2a:1':'Retained vow substitute equivalence; nature of substitutes not silently resolved.',
'2a:2':'Separated herem, oath and naziriteship category equivalences.',
'2a:3':'Retained complete formula list and prohibition with combination ambiguity; later Shmuel continuation read as context but not counted as extracted.',
'2a:4':'Retained Rabbi Akiva cautious stringency as unresolved inclination, not absolute prohibition.',
'2b:1':'Retained category-list contrast question and its anonymous voice.',
'2b:2':'Separated paired-scripture explanation from all-category expansion.',
'2b:3':'Retained order question and object/person distinction for three categories.',
'2b:4':'Retained both mismatch and omitted-formula questions.',
'2b:5':'Retained explicit supplied-wording reconstruction without changing source.',
'2b:6':'Retained standalone order question as utterance and question, no invented answer here.',
'2b:7':'Retained tentative last-first explanation and lighting example.',
'2b:8':'Retained both insulation and woman-clothing order examples.',
'2b:9':'Retained universal challenge and inheritance counterexample.',
'2b:10':'Retained husband/levir category-order counterexample.',
'2b:11':'Retained two distinct offering-category counterexamples.',
'2b:12':'Retained firstborn counterexample without deriving missing substantive laws.',
'2b:13':'Retained many-category attempted distinction as rejected in continuation.',
'2b:14':'Retained short animal example defeating many-category explanation.',
'3a:1':'Retained flexible-order resolution and separate derivation-priority alternative.',
'3a:2':'Retained why-not-begin question and tentative Torah/derivation response.',
'3a:3':'Retained both unnamed accounts of substitutes and challenge; no person attribution invented.',
'3a:4':'Retained textual-reconstruction question, alternative order and explicit examples; no source-byte emendation.'}
coverage=[]
for ref,note in notes.items():
    sid=refs[ref]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=note+' Direct source '+layer+' pass; '+('records listed.' if ids else 'no additional independent object after rereading.')))
p=dict(schema_version=r.VERSION,tractate='Nedarim',owner='L04/nedarim_resume_20261126',epoch=3,source_sha256=meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
out=JOB/'staging'/'opening_001.json';r.immutable(out,r.encoded(p));print(out)
