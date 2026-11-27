"""Explicit human-readable agent readings for Moed Katan and Makkot openings.

The class only serializes the individually authored statements below. It does
not classify source or alter the frozen common production implementation.
"""
import importlib.util
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
spec=importlib.util.spec_from_file_location('r',ROOT/'bavli_production_v1/runner.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
class Reading:
    def __init__(self,slug,title,prefix):
        self.slug=slug;self.title=title;self.prefix=prefix;self.job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04')/('bavli_'+slug)
        self.meta,self.source=r.load(self.job);self.refs={x['ref'][len(title)+1:]:x for x in self.source.values()};self.rows=[];self.notes={}
    def evidence(self,ref):
        x=self.refs[ref];return dict(segment_id=x['id'],start_char=0,end_char=len(x['text']),quote=x['text'])
    def add(self,key,layer,content,refs,links=(),uncertainty=(),origin='source_paraphrase'):
        id=self.prefix+'.'+key;self.rows.append(dict(id=id,layer=layer,content=content,evidence=[self.evidence(x) for x in refs],links=list(links),uncertainty=list(uncertainty),origin=origin));return id
    def voice(self,key,ref,holder,role,composition='atomic'):
        u=self.add(key+'.u','utterances',dict(textual_voice=holder or 'anonymous discussion',discourse_role=role,composition=composition),[ref])
        self.add(key+'.a','attributions',dict(surface=holder or '',role='speaker' if holder else 'anonymous',candidates=[holder] if holder else [],scope=u,transmission_chain=[]),[ref],[u]);return u
    def c(self,key,ref,text,holder=None,mode='asserted',conditions=(),uncertainty=(),scope='Local opening discussion',composition='atomic'):
        u=self.voice(key,ref,holder,mode,composition);c=self.add(key+'.c','claims',dict(proposition=text,conditions=list(conditions),scope=scope,assertion_mode=mode),[ref],[u],uncertainty)
        self.add(key+'.p','positions',dict(holder_candidates=[holder] if holder else [],claim_id=c,question_id=None,conditions=list(conditions),local_status=mode+' locally; not a later practical ruling'),[ref],[c],uncertainty);return c
    def q(self,key,ref,text):
        u=self.voice(key,ref,None,'explicit question');return self.add(key+'.q','questions',dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='none'),[ref],[u])
    def e(self,key,a,b,rel,ref):return self.add(key,'edges',dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[ref],[a,b])
    def structure(self,key,refs,title):return self.add(key,'structure',dict(title=title,primary=True,boundary='closed',legacy_ids=[]),refs,origin='editorial_inference')
    def save(self):
        cov=[]
        for ref,note in self.notes.items():
            sid=self.refs[ref]['id']
            for layer in r.LAYERS:
                ids=[x['id'] for x in self.rows if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
                cov.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=note+' Direct source '+layer+' reread; '+('records retained.' if ids else 'no additional independent object found.')))
        p=dict(schema_version=r.VERSION,tractate=self.title,owner='L04/'+self.slug+'_resume_20261126',epoch=3,source_sha256=self.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=self.rows,coverage=cov,open_tails=[])
        out=self.job/'staging'/'opening_001.json';r.immutable(out,r.encoded(p));print(out)

def moed():
    a=Reading('moed_katan','Moed Katan','mk.r001');c=a.c;q=a.q;e=a.e
    assert a.meta['source_sha256']=='b067f3555fa8981f4ff950347cfd2fc30a727bca74c626a63fa91e4a880482b7'
    a.structure('mishnah',['2a:1','2a:2','2a:3'],'Irrigation, channels and public works during the festival and sabbatical year')
    a.structure('explanation',['2a:'+str(i) for i in range(4,16)]+['2b:1','2b:2'],'Irrigation field types, effort and attribution of the Mishnah rule')
    irrigate=c('irrigate','2a:1','One may irrigate a dependent irrigated field on the intermediate festival days and in the sabbatical year.',conditions=['בית השלחין','festival intermediate days or sabbatical year'],scope='Mishnah irrigation permission')
    c('springs','2a:1','Both a newly emerged spring and an established spring may be used.',conditions=['בית השלחין'],scope='Mishnah permitted sources')
    c('rain','2a:1','Rainwater may not be used for the irrigation described here.',conditions=['irrigation in the stated Mishnah setting'],scope='Mishnah excluded water source')
    c('drawn','2a:1','מי הקילון may not be used for this irrigation.',conditions=['irrigation in the stated Mishnah setting'],scope='Mishnah excluded water source; preserve term without unverified apparatus details')
    c('basins','2a:2','One may not make עוגיות for vines.',scope='Mishnah vine irrigation work; later explanation pending')
    c('channelzea','2a:2','Rabbi Elazar ben Azarya prohibits making a new channel on the intermediate festival days and in the sabbatical year.',holder='רבי אלעזר בן עזריה',conditions=['new channel','festival or sabbatical year'])
    c('channelsages','2a:2','The sages allow making a new channel in the sabbatical year.',holder='חכמים',conditions=['new channel','sabbatical year'])
    c('repair','2a:2','The sages allow repairing damaged channels during the festival.',holder='חכמים',conditions=['damaged existing channels','festival'])
    for key,text in [('waterrepair','Repair public water-system damage.'),('clear','Clear out the public water channels.'),('roads','Repair roads.'),('streets','Repair streets.'),('mikvaot','Repair water immersion pools.'),('public','Perform communal needs.'),('graves','Mark graves.'),('mixed','Go out to inspect mixed species.')]:c(key,'2a:3',text,scope='Mishnah public works permission/list; no fabricated private-work generalization')
    redundancy=q('redundancy','2a:4','If the unstable new spring is allowed, why also state the stable established spring?')
    risk=c('risk','2a:4','A newly emerged spring may collapse, whereas an established spring is not subject to that stated concern.',scope='Premise of the redundancy question')
    hypothesis=c('hypothesis','2a:5','If only the new spring were listed, one might restrict dependent fields only there because of instability, while allowing a rain-fed field with an established spring.',mode='rejected',conditions=['hypothetical omission of the established-spring clause'],composition='composite')
    strict=c('strict','2a:6','For both new and established springs, irrigation is permitted for בית השלחין but not בית הבעל.',conditions=['same Mishnah irrigation context'],mode='asserted')
    e('strict.answer',strict,redundancy,'answer','2a:6');e('strict.correction',strict,hypothesis,'correction','2a:6')
    shq=q('shlahin','2a:7','How does בית השלחין signify thirst/dryness?')
    sh=c('shproof','2a:7','The explanation compares משלהי in the translation of weary/faint with the field term.',scope='Source’s lexical comparison, not a modern etymological claim')
    e('sh.answer',sh,shq,'answer','2a:7')
    bq=q('baal','2a:8','How does בית הבעל signify a settled condition?')
    bp=c('baalproof','2a:8','The explanation uses the translated settlement language attached to the marriage verse.',scope='Source’s lexical explanation with Isaiah translation')
    e('baal.answer',bp,bq,'answer','2a:8')
    who=q('who','2a:9','Which tanna permits loss prevention but not gain, and disallows burdensome effort even to prevent loss?')
    policy=c('policy','2a:9','The question reads the Mishnah as allowing loss prevention, excluding gain and limiting effort even for loss prevention.',scope='Anonymous interpretation of the Mishnah, not a named independent ruling',composition='composite')
    huna=c('huna','2a:10','Rav Huna proposes Rabbi Eliezer ben Yaakov as the tanna.',holder='רב הונא',mode='challenged',scope='Proposed identification, not a dispute about the quoted wording')
    tree=c('tree','2a:10','Rabbi Eliezer ben Yaakov permits drawing water from tree to tree provided the whole field is not irrigated.',holder='רבי אליעזר בן יעקב',conditions=['do not irrigate the whole field'],scope='Quoted Mishnah evidence')
    e('huna.answer',huna,who,'answer','2a:10');e('tree.support',tree,huna,'support','2a:10')
    challenge=q('effort','2a:11','The no-gain view is known, but where did he prohibit effort when loss is at stake?')
    e('effort.objection',challenge,huna,'objection','2a:11')
    pappa=c('pappa','2a:12','Rav Pappa instead identifies the Mishnah with Rabbi Yehuda.',holder='רב פפא',scope='Replacement identification supported by the following teaching')
    e('pappa.answer',pappa,who,'answer','2a:12')
    meir=c('meir','2a:12','Rabbi Meir allows irrigation from a new spring even for a rain-fed field.',holder='רבי מאיר',conditions=['new spring','even בית הבעל'],scope='Quoted baraita')
    yehuda=c('yehuda','2a:12','Rabbi Yehuda permits only a dependent irrigated field that has become חרבה.',holder='רבי יהודה',conditions=['בית השלחין שחרבה'],scope='Quoted baraita; חרבה explained next')
    azar=c('azar','2a:12','Rabbi Elazar ben Azarya permits neither of these new-spring cases.',holder='רבי אלעזר בן עזריה',conditions=['new spring'],scope='Quoted baraita')
    redirect=c('redirect','2a:12','Rabbi Yehuda further prohibits redirecting a water channel to irrigate one’s garden or ruin on the intermediate festival days.',holder='רבי יהודה',conditions=['festival intermediate days','redirecting channel'],scope='Additional stated effort restriction')
    e('yehuda.support',yehuda,pappa,'support','2a:12');e('redirect.support',redirect,pappa,'support','2a:12')
    hq=q('harva','2a:13','What does חרבה mean, and why water a literally ruined field?')
    abaye=c('abaye','2a:13','Abaye explains that the field lost its original spring and another spring emerged.',holder='אביי',conditions=['original spring dried','replacement spring emerged'],scope='Interpretation of Rabbi Yehuda’s condition')
    e('abaye.answer',abaye,hq,'answer','2a:13');e('abaye.qualification',abaye,yehuda,'qualification','2a:13')
    azarclar=c('azarclar','2a:14','Rabbi Elazar ben Azarya excludes the new spring whether or not the previous spring dried.',holder='רבי אלעזר בן עזריה',conditions=['new spring'],scope='Anonymous clarification of the quoted position')
    e('azarclar.qualification',azarclar,azar,'qualification','2a:14')
    limit=c('limit','2a:15','Perhaps Rabbi Yehuda restricts rain-fed fields only for a newly emerged spring.',mode='rejected',scope='Challenge continued next segment')
    old=c('old','2b:1','Perhaps an established spring, without collapse risk, would permit even the rain-fed field.',mode='rejected',conditions=['established spring'],scope='Continuation of hypothetical challenge')
    e('limit.objection',limit,pappa,'objection','2a:15')
    ownerq=q('owner','2b:2','If so, to whom could the Mishnah be assigned?')
    result=c('result','2b:2','The resolution attributes to Rabbi Yehuda the same dependent-field restriction for both new and established springs.',holder='רבי יהודה',mode='reconciled',conditions=['either spring type'],scope='Anonymous resolution of the tanna-identification argument')
    strong=c('strong','2b:2','The baraita specifies the new spring to display the extent of Rabbi Meir’s permission even for a rain-fed field.',scope='Explanation of the baraita’s selected case')
    e('result.correction',result,old,'correction','2b:2');e('result.answer',result,ownerq,'answer','2b:2');e('strong.support',strong,result,'support','2b:2')
    a.notes={x:'Reread this original segment and continuation through2b:2. Preserve spring type, dependent/rain-fed field, effort and loss conditions; tanna-identification hypotheses have explicit local status.' for x in ['2a:'+str(i) for i in range(1,16)]+['2b:1','2b:2']}
    a.notes['2a:2']='Reread distinct channel rules, both festival and sabbatical conditions, and named sages; no harmonization of their disagreement.'
    a.notes['2a:3']='Reread and separately retained every public-works item, including graves and mixed-species inspection.'
    a.save()

def makkot():
    a=Reading('makkot','Makkot','ma.r001');c=a.c;q=a.q;e=a.e
    assert a.meta['source_sha256']=='ca2b205e20bd401000af94a7f6d9da4ba9fa5208b9a0f78c5f50aa2bda618efd'
    a.structure('mishnah',['2a:1','2a:2'],'False witnesses receive lashes rather than priestly-status disqualification or exile')
    a.structure('meaning',['2a:3','2a:4','2a:5'],'Mishnah wording relates to exceptions to ordinary retaliation')
    a.structure('priest',['2a:6','2a:7','2b:1'],'Source for not imposing priestly-status disqualification on false witnesses')
    a.structure('exile',['2b:2','2b:3','2b:4'],'Source for not exiling false witnesses')
    a.structure('lashes',['2b:5','2b:6','2b:7'],'Scriptural basis for lashes rather than ordinary false-testimony prohibition')
    c('priestm','2a:1','When witnesses falsely testify that a man is a son of a divorcee or a halutza, their punishment is not to acquire that status but forty lashes.',conditions=['witnesses are established as zomemim for this testimony'],scope='Mishnah special sanction; both statuses retained',composition='composite')
    c('exilem','2a:2','When witnesses falsely testify that a man must go into exile, they are not exiled in his place but receive forty lashes.',conditions=['witnesses are established as zomemim for this testimony'],scope='Mishnah exile exception',composition='composite')
    wording=q('wording','2a:3','Should the heading not say how witnesses do not become zomemim, given the later explicit case of witnesses located elsewhere?')
    later=c('later','2a:3','The later Mishnah calls them zomemim when others locate the witnesses with themselves elsewhere on that day.',scope='Quoted contrast about witnessing location, not mere contradiction of event testimony')
    ordinary=c('ordinary','2a:4','The explanation refers back to the rule of the corresponding death penalty, with the priest’s daughter/adulterer witness exception to a different death.',scope='Cross-Mishnah context, not an exhaustive reconstruction of the prior sugya',composition='composite')
    special=c('special','2a:5','Other zomemim receive no matching retaliatory sanction at all, but forty lashes; priestly-status testimony is such a case.',scope='Explanation of opening classification')
    e('special.answer',special,wording,'answer','2a:5')
    sourceq=q('source','2a:6','What is the source for the priestly-status exception?')
    seed=c('seed','2a:6','The verse לו is read as applying to the witness himself, not to his descendants.',scope='Scriptural derivation; printed attribution contains parenthetical variant',uncertainty=['Source prints Rabbi Yehoshua ben Levi with parenthetical אמר ריש לקיש. Do not silently pick one authority or invent a transmission chain.'])
    for row in a.rows:
        if row['id']=='ma.r001.seed.a':row['content']=dict(surface='א"ר יהושע בן לוי (אמר ר"ש בן לקיש)',role='quoted_authority',candidates=['רבי יהושע בן לוי','ריש לקיש'],scope=seed+'; printed attribution variant unresolved',transmission_chain=[]);row['uncertainty']=['Parenthetical variant preserved; candidates are alternatives, not joint authors.']
        if row['id']=='ma.r001.seed.p':row['content']['holder_candidates']=['רבי יהושע בן לוי','ריש לקיש']
    selfq=q('self','2a:6','Why not disqualify only the witness while sparing his descendants?')
    mismatch=c('mismatch','2a:6','That would not fulfill the requirement to do as the witness planned, so this disqualification is not imposed.',scope='Reply about mismatch of retaliatory effect')
    e('seed.answer',seed,sourceq,'answer','2a:6');e('mismatch.answer',mismatch,selfq,'answer','2a:6')
    pada=c('pada','2a:7','Bar Padda proposes an a-fortiori argument: one who actually causes disqualification is not himself disqualified, so one who sought but failed to cause it should not be.',holder='בר פדא',mode='rejected',scope='Proposed inference, rejected by Ravina’s reductio',composition='composite')
    ravina=c('ravina','2a:7','Ravina objects that this argument would annul the law of conspiring witnesses.',holder='רבינא',scope='Objection whose explanation continues next segment')
    e('pada.answer',pada,sourceq,'answer','2a:7');e('ravina.objection',ravina,pada,'objection','2a:7')
    stoning=c('stoning','2b:1','The parallel argument would exempt those who planned stoning without accomplishing it because witnesses whose act already caused stoning are not stoned.',mode='rejected',scope='Ravina reductio continued; not an accepted exemption for an unexecuted conspiracy',composition='composite')
    original=c('original','2b:1','The discussion returns to the original scriptural explanation as the clear answer.',mode='reconciled',scope='Explicit preference for the initial derivation')
    e('stoning.support',stoning,ravina,'support','2b:1');e('original.resolution',original,seed,'local_resolution','2b:1')
    exileq=q('exilesource','2b:2','What is the source for not exiling these witnesses?')
    lakish=c('lakish','2b:2','Resh Lakish reads הוא ינוס as he, but not conspiring witnesses, shall flee.',holder='ריש לקיש',scope='Explicit verse derivation for exile exception')
    e('lakish.answer',lakish,exileq,'answer','2b:2')
    yohanan=c('yohanan','2b:3','Rabbi Yohanan argues a fortiori from one who intentionally committed the act and is not exiled to witnesses who did not commit the act.',holder='רבי יוחנן',mode='rejected',scope='Proposed inference subsequently reversed; not the maintained conclusion',composition='composite')
    e('yohanan.answer',yohanan,exileq,'answer','2b:3')
    reverse=c('reverse','2b:4','The same consideration can reverse the argument: the deliberate actor is denied exile’s atonement, whereas witnesses who did not commit the act might receive it.',mode='hypothetical',scope='Counterargument undermining the a-fortiori proof, not a final exile rule',composition='composite')
    final=c('final','2b:4','The discussion prefers Resh Lakish’s derivation as the clear explanation.',mode='reconciled',scope='Explicit local conclusion')
    e('reverse.objection',reverse,yohanan,'objection','2b:4');e('final.resolution',final,lakish,'local_resolution','2b:4')
    uq=q('ulla','2b:5','Ulla asks for a Torah indication for conspiring witnesses; the question is clarified as an indication that they receive lashes.')
    explicit=c('explicit','2b:5','The general conspiring-witness rule already appears in כאשר זמם, so the question must concern lashes.',scope='Anonymous clarification of Ulla’s wording')
    verse=c('verse','2b:5','The proposed basis joins והצדיקו את הצדיק והרשיעו את הרשע with והיה אם בן הכות הרשע.',holder='עולא',scope='Ulla’s proposed scriptural basis as presented by the discussion')
    qlink=q('link','2b:5','Does merely justifying the righteous and condemning the wicked entail lashes?')
    scenario=c('scenario','2b:6','The verse is read as witnesses first condemning an innocent person, then other witnesses vindicating that person and establishing the first witnesses as wicked, followed by the lashes clause.',scope='Anonymous explanatory scenario connecting the verses',composition='composite')
    e('scenario.answer',scenario,qlink,'answer','2b:6');e('scenario.support',scenario,verse,'support','2b:6')
    falseq=q('false','2b:7','Why not derive lashes from לא תענה?')
    noact=c('noact','2b:7','That prohibition lacks an act, and a prohibition without an act does not ordinarily incur lashes in this argument.',conditions=['prohibition without an act'],scope='Reason לא תענה does not supply these lashes')
    e('noact.answer',noact,falseq,'answer','2b:7')
    a.notes={x:'Reread original text and complete local continuation. Preserve witness conditions, explicit local rejection/resolution, and exact named or unresolved attribution; no practical ruling beyond this source.' for x in ['2a:'+str(i) for i in range(1,8)]+['2b:'+str(i) for i in range(1,8)]}
    a.notes['2a:6']='Read printed Rabbi Yehoshua ben Levi / parenthetical Resh Lakish attribution without selecting one; retain descendant limitation, self-only question and mismatch answer.'
    a.notes['2a:7']='Read Bar Padda proposal and Ravina objection together with2b:1 reductio; mark proposed proof rejected.'
    a.notes['2b:4']='Read reversal of Rabbi Yohanan proof and explicit preference for Resh Lakish, not a maintained two-position exile dispute.'
    a.notes['2b:5']='Read Ulla initial question, anonymous clarification, verse proposal and causal-link objection as separate discourse acts.'
    a.save()

if __name__=='__main__':
    {'moed_katan':moed,'makkot':makkot}[sys.argv[1]]()
