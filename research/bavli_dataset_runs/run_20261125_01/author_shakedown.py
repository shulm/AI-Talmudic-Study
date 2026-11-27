"""Serialize the coordinator's source reading, not automatic semantic extraction.

The propositions below were authored after reading original source with continuation.
This file makes span anchoring reproducible; only frozen proposals are replay inputs.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent / 'proposals'
SOURCE = Path('F:/Sefaria-Export-master')
MANIFEST = json.loads((ROOT/'research/bavli_sugya_corpus_v1/source_manifest.json').read_text('utf-8'))
LAYERS = ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']
def sha(b): return hashlib.sha256(b).hexdigest()

class Reading:
    def __init__(self, name, prefix):
        self.name,self.prefix,self.records = name,prefix,[]
        self.meta=next(t for t in MANIFEST['tractates'] if t['title']==name)
        raw=(SOURCE/self.meta['source_path']).read_bytes()
        assert sha(raw)==self.meta['source_sha256']
        self.text=json.loads(raw)['text']
    def ev(self, ref, phrase=None):
        daf, n=ref.split(':'); i=(int(daf[:-1])-1)*2+(daf[-1]=='b'); j=int(n)-1
        text=self.text[i][j]; start=text.index(phrase) if phrase else 0; quote=phrase or text
        return dict(segment_id='seg_'+sha('|'.join([self.name,'Wikisource Talmud Bavli',str(i),str(j)]).encode())[:20],start_char=start,end_char=start+len(quote),quote=quote)
    def add(self,key,layer,refs,content,origin='source_paraphrase',links=None,uncertainty=None):
        evidence=[self.ev(*r) if isinstance(r,tuple) else self.ev(r) for r in refs]
        rid=self.prefix+'.'+key
        self.records.append(dict(id=rid,layer=layer,evidence=evidence,content=content,origin=origin,links=links or [],uncertainty=uncertainty or []))
        return rid
    def claim(self,key,refs,text,conditions=None,mode='asserted'):
        return self.add(key,'claims',refs,dict(proposition=text,conditions=conditions or [],scope='Local passage; no later practical ruling inferred',assertion_mode=mode))
    def attribution(self,key,refs,surface,role,scope,chain=None,candidates=None):
        return self.add(key,'attributions',refs,dict(surface=surface,role=role,candidates=candidates or [],scope=scope,transmission_chain=chain or []))
    def position(self,key,refs,holder,claim,question=None,conditions=None):
        return self.add(key,'positions',refs,dict(holder_candidates=holder,claim_id=claim,question_id=question,conditions=conditions or [],local_status='Reported in this passage; no ruling beyond local text asserted'),links=[claim]+([question] if question else []))
    def edge(self,key,refs,a,b,relation):
        return self.add(key,'edges',refs,dict(source_id=a,target_id=b,relation=relation,explicitness='source_explicit'),links=[a,b])
    def save(self,refs,filename):
        coverage=[]
        for ref in refs:
            sid=self.ev(ref)['segment_id']
            for layer in LAYERS:
                ids=[r['id'] for r in self.records if r['layer']==layer and any(e['segment_id']==sid for e in r['evidence'])]
                rationale=('Source reread against all seven extraction layers; retained conditions, textual roles, and open questions without imposing an answer set.' if layer=='reconciliation' else 'Direct source reading over this segment and surrounding continuation; findings anchored below.' if ids else 'Source pass found no separate '+layer+' object in this segment; no artificial object supplied.')
                coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
        proposal=dict(schema_version='2.0.0-production',tractate=self.name,owner='GLOBAL_COORDINATOR_BOOTSTRAP',epoch=1,source_sha256=self.meta['source_sha256'],schema_sha256=sha((ROOT/'research/bavli_production_v1/schema.json').read_bytes()),protocol_sha256=sha((ROOT/'research/bavli_production_v1/PROTOCOL.md').read_bytes()),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=self.records,coverage=coverage,open_tails=[])
        raw=(json.dumps(proposal,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
        OUT.mkdir(parents=True,exist_ok=True); path=OUT/filename
        if path.exists(): assert path.read_bytes()==raw, 'Frozen proposal differs; create new attempt, never overwrite'
        else: path.write_bytes(raw)
        print(filename,sha(raw),len(self.records),len(coverage))

def berakhot():
    r=Reading('Berakhot','bk.b24.semantic1'); refs=['5a:24','5b:1','5b:2','5b:3']
    r.add('s','structure',refs,dict(title='כפרה בתורה ובגמילות חסדים ובקבורת בנים',primary=True,boundary='closed',legacy_ids=['sug_9a1c712c3a26fe45003b']),origin='editorial_inference',uncertainty=['Uses the already extended B24 boundary; does not replace inherited version or later B71 continuation.'])
    u1=r.add('u1','utterances',refs[:2],dict(textual_voice='Anonymous reciter before Rabbi Yohanan',discourse_role='Teaching',composition='composite'))
    u2=r.add('u2','utterances',['5b:2'],dict(textual_voice='Rabbi Yohanan',discourse_role='Accepts scriptural explanation of first clauses and asks source for remaining clause',composition='composite'))
    u3=r.add('u3','utterances',['5b:3'],dict(textual_voice='Unnamed elder reporting Rabbi Shimon ben Yohai',discourse_role='Answer by verbal analogy',composition='composite'))
    c1=r.claim('c1',refs[:2],'The recited teaching promises forgiveness of all sins to the person described as engaging in Torah and acts of kindness and burying his children.',conditions=['The teaching lists Torah study, acts of kindness, and burying children; no independent legal conditions beyond its wording are supplied.'])
    c2=r.claim('c2',['5b:2'],'Rabbi Yohanan accepts the Torah and kindness clauses as explained by the verse בחסד ואמת יכופר עון.')
    c3=r.claim('c3',[('5b:2','חסד זו גמילות חסדים')],'חסד is interpreted here as acts of kindness.')
    c4=r.claim('c4',[('5b:2','אמת זו תורה')],'אמת is interpreted here as Torah.')
    c5=r.claim('c5',['5b:3'],'The elder reports in Rabbi Shimon ben Yohai’s name a verbal analogy עון–עון linking the atonement verse and the verse about fathers’ sin reaching their children.',conditions=['This is the reported derivation for the clause about burying children; no moral motive or later ruling inferred.'])
    q=r.add('q','questions',[('5b:2','אלא קובר את בניו מנין')],dict(formulation='What is the source for the clause about one who buries his children?',question_origin='explicit',conditions=[],answer_set_status='partial'))
    r.attribution('a1',[('5a:24',"תני תנא קמיה דר' יוחנן")],'תנא','speaker',u1)
    r.attribution('a2',[('5b:2','אמר ליה רבי יוחנן')],'רבי יוחנן','speaker',u2,candidates=['רבי יוחנן (textual label; person identity not separately certified)'])
    r.attribution('a3',[('5b:3',"תנא ליה ההוא סבא משום ר' שמעון בן יוחאי")],'ההוא סבא','transmitter',c5,chain=['ההוא סבא',"ר' שמעון בן יוחאי"])
    r.attribution('a4',[('5b:3',"משום ר' שמעון בן יוחאי")],"ר' שמעון בן יוחאי",'quoted_authority',c5)
    r.position('p1',refs[:2],['Anonymous reciter'],c1)
    r.position('p2',['5b:2'],['רבי יוחנן'],c2)
    r.position('p3',['5b:3'],["ר' שמעון בן יוחאי (reported by unnamed elder)"],c5,q)
    r.edge('e1',['5b:2'],c2,c1,'support')
    r.edge('e2',['5b:3'],c5,q,'answer')
    r.edge('e3',['5b:2'],c3,c2,'support')
    r.edge('e4',['5b:2'],c4,c2,'support')
    r.save(refs,'berakhot_b24_initial.json')

def rosh_hashanah():
    r=Reading('Rosh Hashanah','rh.opening1'); refs=['2a:1','2a:2','2a:3','2a:4']
    r.add('s','structure',refs,dict(title='ארבעה ראשי שנים',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference',uncertainty=['Mishnah unit closes at 2a:4; its later Gemara explanations are not claimed processed.'])
    for n,ref in enumerate(refs,1):
        r.add('u'+str(n),'utterances',[ref],dict(textual_voice='Mishnah; named views retained separately',discourse_role='Calendar thresholds and disputed dates',composition='composite'))
    entries=[('count','2a:1','The Mishnah enumerates four New Year dates.','Mishnah anonymous voice',[]),
      ('kings','2a:1','The first of Nisan is the New Year for kings.','Mishnah anonymous voice',[]),
      ('festivals','2a:1','The first of Nisan is the New Year for festivals.','Mishnah anonymous voice',[]),
      ('animal','2a:2','The first of Elul is the New Year for animal tithe.','Mishnah anonymous first opinion',[]),
      ('animal_alt','2a:2','The first of Tishrei is the New Year for animal tithe.','רבי אלעזר ורבי שמעון',[]),
      ('years','2a:3','The first of Tishrei is the New Year for years.','Mishnah anonymous voice',[]),
      ('sabbatical','2a:3','The first of Tishrei is the New Year for sabbatical years.','Mishnah anonymous voice',[]),
      ('jubilee','2a:3','The first of Tishrei is the New Year for jubilees.','Mishnah anonymous voice',[]),
      ('planting','2a:3','The first of Tishrei is the New Year for planting.','Mishnah anonymous voice',[]),
      ('vegetables','2a:3','The first of Tishrei is the New Year for vegetables.','Mishnah anonymous voice',[]),
      ('tree_bs','2a:4','The first of Shevat is the New Year for the tree, according to Beit Shammai.','בית שמאי',[]),
      ('tree_bh','2a:4','The fifteenth of Shevat is the New Year for the tree, according to Beit Hillel.','בית הלל',[])]
    for key,ref,text,holder,conditions in entries:
        c=r.claim('c.'+key,[ref],text,conditions)
        r.position('p.'+key,[ref],[holder],c,conditions=conditions)
    r.attribution('a.anonymous',['2a:1','2a:2','2a:3'],'Unattributed Mishnah voice','anonymous','Unattributed calendar thresholds; not assigned to a named tanna')
    r.attribution('a.es',[('2a:2',"ר' אלעזר ור\"ש אומרים")],"ר' אלעזר ור\"ש",'collective','Animal tithe alternative date',candidates=['רבי אלעזר and רבי שמעון; abbreviations retained, no patronymic identity inferred'])
    r.attribution('a.bs',[('2a:4','כדברי בית שמאי')],'בית שמאי','collective','Tree date: first Shevat')
    r.attribution('a.bh',[('2a:4','בית הלל אומרים')],'בית הלל','collective','Tree date: fifteenth Shevat')
    r.save(refs,'rosh_hashanah_opening_initial.json')

if __name__=='__main__': berakhot(); rosh_hashanah()
