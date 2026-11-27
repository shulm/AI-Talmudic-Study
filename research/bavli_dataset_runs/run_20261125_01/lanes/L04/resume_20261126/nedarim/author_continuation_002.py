"""Individually authored source readings. No semantic extraction automation."""
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
spec=importlib.util.spec_from_file_location('r',ROOT/'bavli_production_v1/runner.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_nedarim')
meta,ss=r.load(JOB)
assert meta['source_sha256']=='52a452f67441cc435f1908275e349834ddc53a2add513905d52e6a0a186e85a1'
refs={s['ref'].split(' ',1)[1]:s for s in ss.values()}
records=[]
PREFIX='nd.r002.'
OUTPUT='continuation_002.json'
def ev(ref,quote=None):
    s=refs[ref];t=s['text'];q=t if quote is None else quote
    if isinstance(q,tuple):
        q,occurrence=q;starts=[];offset=0
        while True:
            found=t.find(q,offset)
            if found<0:break
            starts.append(found);offset=found+1
        a=starts[occurrence]
    else:
        assert t.count(q)==1,(ref,q)
        a=t.index(q)
    return dict(segment_id=s['id'],start_char=a,end_char=a+len(q),quote=q)
def add(key,layer,content,e,links=(),uncertainty=(),origin='source_paraphrase'):
    ident=PREFIX+key
    records.append(dict(id=ident,layer=layer,content=content,evidence=e,links=list(links),uncertainty=list(uncertainty),origin=origin))
    return ident
def speech(key,e,voice,role,composition='atomic'):
    u=add(key+'.u','utterances',dict(textual_voice=voice or 'anonymous discussion',discourse_role=role,composition=composition),e)
    add(key+'.a','attributions',dict(surface=voice or '',role='speaker' if voice else 'anonymous',candidates=[voice] if voice else [],scope=u,transmission_chain=[]),e,[u])
    return u
def c(key,ref,quote,text,mode='asserted',holder=None,conditions=(),scope='Local derivation discussion',extra=(),composition='atomic',uncertainty=()):
    e=[ev(ref,quote)]+[ev(*x) for x in extra];u=speech(key,e,holder,mode,composition)
    x=add(key+'.c','claims',dict(proposition=text,conditions=list(conditions),scope=scope,assertion_mode=mode),e,[u],uncertainty)
    add(key+'.p','positions',dict(holder_candidates=[holder] if holder else [],claim_id=x,question_id=None,conditions=list(conditions),local_status=mode+' in local discourse; no later practical ruling inferred'),e,[x],uncertainty)
    return x
def q(key,ref,quote,text,conditions=(),voice=None):
    e=[ev(ref,quote)];u=speech(key,e,voice,'explicit question')
    return add(key+'.q','questions',dict(formulation=text,question_origin='explicit',conditions=list(conditions),answer_set_status='none'),e,[u])
def edge(key,a,b,rel,ref,quote=None):
    return add(key,'edges',dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[ev(ref,quote)],[a,b])
def structure(key,scope,title,boundary='closed'):
    return add(key,'structure',dict(title=title,primary=True,boundary=boundary,legacy_ids=[]),[ev(x) for x in scope],origin='editorial_inference')

scope=['3a:'+str(i) for i in range(5,11)]+['3b:'+str(i) for i in range(1,5)]
structure('derivation',scope,'Derivation of abbreviated vows and naziriteship; alternative allocations of doubled biblical language')
origin=q('origin','3a:5','וידות היכא כתיב','Where are abbreviated vow formulations written in Scripture?')
sub=c('sub','3a:5','ותניא  נזיר להזיר לעשות כינויי נזירות כנזירות','The cited teaching derives the force of substitute nazirite expressions from נזיר להזיר.',scope='Anonymous quoted teaching; derivation wording preserved without supplying a named tanna')
hand=c('hand','3a:5','וידות נזירות כנזירות','The same cited teaching gives abbreviated nazirite expressions the force of naziriteship.',scope='Continuation of cited derivation from נזיר להזיר')
edge('hand.answer',hand,origin,'answer','3a:5')
vowq=q('vowq','3a:6',"אין לי אלא בנזירות בנדרים מנין",'How is the rule established for vows, beyond naziriteship?')
compare=c('compare','3a:6',"ת''ל איש כי יפליא לנדור נדר נזיר להזיר לה' מקיש נזירות לנדרים ונדרים לנזירות",'The cited verse juxtaposes vows and naziriteship, supporting comparison in both directions.',scope='Quoted baraita interpretation')
vow=c('vow','3a:6','מה נזירות עשה בו ידות נזירות כנזירות אף נדרים עשה בהם ידות נדרים כנדרים','Abbreviated vows have the force of vows, by comparison with abbreviated nazirite formulations.',scope='Quoted baraita inference')
edge('vow.answer',vow,vowq,'answer','3a:6');edge('compare.support',compare,vow,'support','3a:6')
violate=c('violate','3a:7','ומה נדרים עובר בבל יחל ובבל תאחר אף נזירות עובר בבל יחל ובבל תאחר','The baraita transfers the prohibitions בל יחל and בל תאחר from vows to naziriteship.',composition='composite',scope='Explicit paired prohibition derivation; how each applies is discussed at3b:5–4b:3')
father=c('father','3a:7','ומה נדרים האב מיפר נדרי בתו','The baraita uses a father’s annulment of his daughter’s vows as a premise.',scope='Premise for the following analogy, not a statement of all annulment conditions')
husband=c('husband','3a:7','ובעל מיפר נדרי אשתו','The baraita uses a husband’s annulment of his wife’s vows as a premise.',scope='Annulment analogy premise; not every type of vow unrestrictedly')
nfather=c('nfather','3a:7','אף נזירות האב מיפר נזירות בתו','The baraita extends paternal annulment to a daughter’s naziriteship.',scope='Comparison with the preceding vow-annulment premise')
nhusband=c('nhusband','3a:7','ובעל מיפר נזירות אשתו','The baraita extends spousal annulment to a wife’s naziriteship.',scope='Comparison with the preceding vow-annulment premise')
edge('father.analogy',father,nfather,'analogy','3a:7');edge('husband.analogy',husband,nhusband,'analogy','3a:7')
why=q('why','3a:8',None,'Why require the comparison when vows also have doubled language לנדור נדר, as naziriteship has נזיר להזיר?')
counter=c('counter','3a:9','אי כתב נדר לנדור כדכתב נזיר להזיר כדקאמרת לא צריך היקישא','If vows were worded נדר לנדור like נזיר להזיר, the comparison would indeed be unnecessary.',mode='hypothetical',conditions=['counterfactual noun–infinitive order נדר לנדור'])
idiom=c('idiom','3a:9','השתא דכתיב לנדור נדר דברה תורה כלשון בני אדם','The actual wording לנדור נדר can be ordinary human idiom, so the comparison is needed.',scope='Answer under the ordinary-language hermeneutic, qualified by next segment')
edge('idiom.answer',idiom,why,'answer','3a:9');edge('counter.distinction',counter,idiom,'distinction','3a:9')
other=q('other','3a:10',"הניחא למאן דאית ליה דברה תורה כלשון בני אדם אלא למאן דלית ליה דברה תורה כלשון בני אדם האי לנדור נדר מאי עביד ליה",'What does the school rejecting the ordinary-language interpretation derive from לנדור נדר?',conditions=['school not applying דברה תורה כלשון בני אדם here'])
reverse=c('reverse','3a:10','דריש ליה  לעשות ידות נדרים כנדרים','That school derives abbreviated vows directly from לנדור נדר.',conditions=['alternative hermeneutic just posed'])
reversecompare=c('reversecompare','3a:10','ומקיש נזירות לנדרים','It then derives the corresponding nazirite rule by comparison with vows.',conditions=['alternative hermeneutic just posed'])
stack=c('stack','3a:10','נזיר להזיר דריש ליה  מלמד','It uses נזיר להזיר to teach that naziriteship can take effect upon naziriteship.',conditions=['alternative allocation of derivations'],extra=[('3b:1',None)],scope='Sentence continues across daf boundary; no quantitative duration supplied')
edge('reverse.answer',reverse,other,'answer','3a:10');edge('reversecompare.support',reverse,reversecompare,'support','3a:10')
stackq=q('stackq','3b:2',None,'If one uses נזיר להזיר for abbreviated naziriteship and nevertheless holds that naziriteship takes effect upon naziriteship, where is the latter derived?',conditions=['ordinary-language hermeneutic','holds naziriteship can take effect upon naziriteship'])
nostack=c('nostack','3b:2',"הניחא אי ס''ל כמ''ד אין נזירות חל על נזירות",'The source poses no derivation difficulty if that school holds that naziriteship does not take effect upon naziriteship.',mode='conditional',conditions=['ordinary-language school also denies superimposed naziriteship'],scope='Conditional branch, not assignment of the view to a named scholar')
both=c('both','3b:3',None,'The distinction between the possible ליזור and actual להזיר yields both derivations.',scope='Reply permits both abbreviated naziriteship and naziriteship upon naziriteship')
edge('both.answer',both,stackq,'answer','3b:3')
west1=c('west1','3b:4','במערבא אמרי  אית תנא דמפיק ליה לידות מן לנדור נדר','In the West they report one tanna deriving abbreviated formulations from לנדור נדר.',holder='במערבא אמרי',scope='Collective reporting voice; underlying tanna unnamed')
west2=c('west2','3b:4','ואית תנא דמפיק ליה מן (במדבר ל ג) כל היוצא מפיו יעשה','The same Western report describes another tanna deriving abbreviated formulations from כל היוצא מפיו יעשה.',holder='במערבא אמרי',scope='Collective reporting voice; other tanna unnamed')

notes={
'3a:5':'Reread question, verse and quoted teaching; retained substitutes and abbreviated expressions separately without naming the tanna.',
'3a:6':'Reread direct-versus-analogical derivation; retained both-direction comparison and resulting vow rule.',
'3a:7':'Reread prohibition pair and four father/husband vow/nazirite annulment clauses; paired prohibition claim expressly composite. Continuation read through4b:5.',
'3a:8':'Reread full comparative objection; no anonymous school assigned by name.',
'3a:9':'Reread counterfactual word order and actual idiom response; statuses differentiated.',
'3a:10':'Reread alternative school, reversed derivation and sentence continuing3b:1; no separate invented claim at dangling מלמד.',
'3b:1':'Reread cross-page sentence and anchored its completion to3a:10; no duplicated proposition.',
'3b:2':'Reread both conditional schools and open derivation demand; denial retained as conditional premise rather than final outcome.',
'3b:3':'Reread ליזור/להזיר response supplying both derivations; linked to question.',
'3b:4':'Reread collective Western report and both unnamed tannaitic sources; reporters not treated as the original tannaim.'}
def save():
    coverage=[]
    for ref,note in notes.items():
        sid=refs[ref]['id']
        for layer in r.LAYERS:
            ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
            coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=note+' Actual source reread for '+layer+'; '+('objects retained.' if ids else 'no separate additional object found.')))
    p=dict(schema_version=r.VERSION,tractate='Nedarim',owner='L04/nedarim_resume_20261126',epoch=3,source_sha256=meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/nedarim_continuation',model_id=None),records=records,coverage=coverage,open_tails=[])
    out=JOB/'staging'/OUTPUT;r.immutable(out,r.encoded(p));print(out)
if __name__=='__main__':save()
