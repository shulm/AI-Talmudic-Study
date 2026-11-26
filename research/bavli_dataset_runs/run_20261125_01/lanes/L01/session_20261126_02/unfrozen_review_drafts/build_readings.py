import json, hashlib, re
from pathlib import Path

OUT=Path(__file__).parent
SRC=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Zeraim/Berakhot/Hebrew/Wikisource Talmud Bavli.json')
PLAN=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/frozen_plans/bavli_berakhot.json')
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(SRC.read_bytes())=='dd24d48aef18159564471380f7ba200302cc9889b22380aef724d2fb086a9d38'
assert sha(PLAN.read_bytes())=='4cb5b9baad10bc4fe7ff90f860e5d7716d90833248040e51a66c9dda4be5b3d1'
source=json.loads(SRC.read_text('utf8')); plan=json.loads(PLAN.read_text('utf8'))

def anchor(ref, quote=None):
    m=re.fullmatch(r'(\d+)([ab]):(\d+)',ref)
    p=(int(m[1])-1)*2+(m[2]=='b'); s=int(m[3])-1
    raw=source['text'][p][s]
    start=0 if quote is None else raw.index(quote)
    q=raw if quote is None else quote
    assert raw[start:start+len(q)]==q
    return dict(ref='Berakhot '+ref,page_index=p,segment_index=s,offsets_codepoints=[start,start+len(q)],quote=q,span_sha256_utf8=sha(q.encode()))

def refs(page,lo,hi):return [f'{page}:{i}' for i in range(lo,hi+1)]

def begin(number,context,structures,uncertainties):
    bid=f'block_{number:06d}'
    b=next(x for x in plan['review_blocks'] if x['block_id']==bid)
    core=[]
    for s in b['spans']:
        a=anchor(s['ref'].removeprefix('Berakhot '))
        for k in ['page_index','segment_index','offsets_codepoints','span_sha256_utf8']: assert a[k]==s[k]
        core.append(a)
    return dict(schema='independent-source-reading-wave2-v1',block_id=bid,reader='fresh independent source-only AI reviewer /root/berakhot_reader_wave2',source_path=str(SRC),source_sha256=sha(SRC.read_bytes()),source_metadata={k:v for k,v in source.items() if k!='text'},plan_path=str(PLAN),plan_file_sha256=sha(PLAN.read_bytes()),plan_embedded_sha256=plan['plan_sha256'],cohort='probability_sample',inclusion_probability=b['inclusion_probability'],seed='20261125',blindness={'production_annotations_seen':False,'production_comparison_performed':False,'scope':'all assigned cores and their source-only context','disclosure':'Read project AGENT_HANDOFF.md as required; it contains historical pair-index research, including Berakhot 10b unnamed Rav/Shmuel cautions outside these cores, but no current production annotations. No current production labels/proposals/comparisons viewed.'},text_basis='original unnormalized JSON strings; half-open Unicode codepoint offsets, not UTF-16',core=core,context=[anchor(r) for r in context],claims=[],questions=[],relations=[],comparable_sets=[],structures=structures,uncertainties=uncertainties,limitations=['One independent AI source reading; no human scholarly certification.','No commentary or alternate textual witness checked.','Narrative and aggadic statements recorded as textual claims, not empirical verification or later halachic rulings.','Context is separate from the ten-segment probability core.'])

def claim(d,id,ref,text,holder,kind='atomic',status='locally_asserted',quote=None,conditions=None,transmission=None,parts=None):
    a=anchor(ref,quote)
    cohort='core' if any(x['ref']==a['ref'] for x in d['core']) else 'context'
    assert any(x['ref']==a['ref'] for x in d[cohort])
    d['claims'].append(dict(id=id,scope=cohort,evidence=[a],explanation=text,holder=holder,transmission=transmission or [],kind=kind,local_status=status,conditions=conditions or [],atomic_components=parts or []))

def question(d,id,ref,text,asker='anonymous discussion',quote=None):
    d['questions'].append(dict(id=id,evidence=[anchor(ref,quote)],question=text,asker=asker))

def edge(d,src,rel,tgt,ref,note=''):
    d['relations'].append(dict(source=src,type=rel,target=tgt,evidence=[anchor(ref)],explanation=note))

def freeze(d):
    ids={x['id'] for x in d['claims']+d['questions']}
    assert len(ids)==len(d['claims'])+len(d['questions'])
    for e in d['relations']:assert e['source'] in ids and e['target'] in ids
    d['counts']={'core_segments':len(d['core']),'core_codepoints':sum(a['offsets_codepoints'][1] for a in d['core']),'context_segments':len(d['context']),'context_codepoints':sum(a['offsets_codepoints'][1] for a in d['context']),'core_atomic_claims':sum(c['scope']=='core' and c['kind']=='atomic' for c in d['claims']),'core_composite_claims':sum(c['scope']=='core' and c['kind']=='composite' for c in d['claims']),'context_claim_records':sum(c['scope']=='context' for c in d['claims']),'questions':len(d['questions']),'directed_relations':len(d['relations'])}
    blob=(json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode()
    p=OUT/(d['block_id']+'.source_reading.v1.json')
    with p.open('xb') as f:f.write(blob)
    p.chmod(0o444)
    r={'path':str(p),'sha256':sha(blob),'counts':d['counts']}
    print(json.dumps(r,ensure_ascii=False));return r

# First reading, block 17: Rav Huna's narrative tail; Abba Binyamin anthology;
# the last core starts the demon discussion, so its continuation is read.
d=begin(17,refs('5b',17,19)+refs('6a',3,6),[
 {'range':'5b:17–20','role':'narrative; core contains conclusion only','boundary':'ends before תניא at 5b:21'},
 {'range':'5b:21–24','role':'two practices, with separate prayer interpretation and bed-orientation elaboration'},
 {'range':'5b:25–6a:1','role':'leaving/waiting for fellow worshipper, question answered across page boundary'},
 {'range':'6a:2–6','role':'demon visibility and presence; new תניא at 6a:7 is stopping boundary'}
],['5b:17 has alternative visitor attribution: Rav Yehuda brother of Rav Sala Hasida and rabbis OR Rav Adda bar Ahava and rabbis. Keep both.','5b:21 prayer-wall report has alternative attribution Rav Yehuda reporting Rav OR R. Yehoshua b. Levi; do not collapse to a certain Rav-only report.','סמוך למטתי replaces spatial לפני מטתי; whether this denotes immediately after rising is interpretation beyond the quoted wording, not imposed here.','6a:6 procedural passage is grammatically unmarked after Rava; possible inherited attribution is not certain.'])
claim(d,'17c01','5b:17','Four hundred barrels of Rav Huna’s wine soured; visiting rabbis urge examination of conduct.','narrator',kind='composite',transmission=['visitor alternatives explicitly retained'])
claim(d,'17c02','5b:18','Visitors report Rav Huna withheld vine shoots from his sharecropper.','visiting rabbis',status='reported_accusation')
claim(d,'17c03','5b:19','Rav Huna defends withholding by alleging the sharecropper steals all of it.','Rav Huna',status='defense_subsequently_rebuked')
claim(d,'17a01','5b:20','Visitors rebuke retaliatory theft through a proverb.','visiting rabbis',quote='אמרו ליה היינו דאמרי אינשי בתר גנבא גנוב וטעמא טעים')
claim(d,'17a02','5b:20','Rav Huna undertakes to give the sharecropper his due.','Rav Huna',quote='אמר להו קבילנא עלי דיהיבנא ליה')
claim(d,'17a03','5b:20','One version says the vinegar became wine again.','anonymous narrator, version A',status='alternative_narrative',quote='איכא דאמרי הדר חלא והוה חמרא')
claim(d,'17a04','5b:20','Another version says vinegar rose in price and sold for wine’s price.','anonymous narrator, version B',status='alternative_narrative',quote='ואיכא דאמרי אייקר חלא ואיזדבן בדמי דחמרא')
claim(d,'17a05','5b:21','Abba Binyamin was lifelong concerned that his prayer be לפני מטתי.','Abba Binyamin',quote='על תפלתי שתהא לפני מטתי',transmission=['baraita'])
claim(d,'17a06','5b:21','Abba Binyamin was lifelong concerned that his bed lie north–south.','Abba Binyamin',quote='ועל מטתי שתהא נתונה בין צפון לדרום',transmission=['baraita'])
claim(d,'17a07','5b:21','Literal prayer in front of the bed is the initial interpretation.','anonymous discussion',status='rejected_interpretation',quote='אילימא לפני מטתי ממש')
claim(d,'17a08','5b:21','A person praying should have no object between himself and the wall.','Rav OR R. Yehoshua b. Levi',quote='והאמר רב יהודה אמר רב ואיתימא ריב"ל מנין למתפלל שלא יהא דבר חוצץ בינו לבין הקיר',conditions=['while praying'],transmission=['Rav Yehuda → Rav; alternative attribution ריב״ל'])
claim(d,'17a09','5b:21','Read סמוך למטתי in place of לפני מטתי.','anonymous discussion',status='local_resolution',quote='לא תימא לפני מטתי אלא אימא סמוך למטתי')
claim(d,'17a10','5b:23','Placing the bed north–south brings male children.','R. Yitzhak',conditions=['bed north–south'],transmission=['R. Hama b. R. Hanina → R. Yitzhak'])
claim(d,'17a11','5b:24','Additionally, his wife does not miscarry.','Rav Nahman b. Yitzhak',conditions=['inherited bed north–south condition'],quote='רב נחמן בר יצחק אמר אף אין אשתו מפלת נפלים')
claim(d,'17a12','5b:25','The first finisher who leaves without waiting has his prayer torn before him.','Abba Binyamin',conditions=['two entered to pray','one finished first','left without waiting'],transmission=['baraita'])
claim(d,'17a13','5b:26','Such leaving also causes the Shekhinah to depart from Israel.','Abba Binyamin, inherited baraita',quote='ולא עוד אלא שגורם לשכינה שתסתלק מישראל',conditions=['same conditions as 17a12'])
claim(d,'17a14','5b:26','צור in the cited verse denotes God.','baraita/expository continuation',quote='ואין צור אלא הקב"ה שנאמר (דברים לב, יח) צור ילדך תשי')
claim(d,'17a15','6a:1','One who waits merits the cited blessings of peace, righteousness and offspring.','R. Yose b. R. Hanina',kind='composite',conditions=['waiting for fellow worshipper'],parts=['peace like a river','righteousness like sea waves','offspring like sand'],quote='זוכה לברכות הללו שנאמר (ישעיהו מח, יח) לוא הקשבת למצותי ויהי כנהר שלומך וצדקתך כגלי הים ויהי כחול זרעך וצאצאי מעיך וגו׳' if False else None)
claim(d,'17a16','6a:2','Were the eye permitted to see, no creature could endure the demons.','Abba Binyamin',conditions=['counterfactual permission for eye to see'],transmission=['baraita'])
claim(d,'17c04','6a:3','Demons are more numerous than humans and surround them like a bank around a bed.','Abaye',kind='composite')
claim(d,'17c05','6a:4','Each person has a thousand at the left and ten thousand at the right.','Rav Huna',kind='composite')
claim(d,'17c06','6a:5','Demons cause assembly crowding, tired knees, worn scholars’ clothes and injured feet.','Rava',kind='composite',parts=['crowding','tired knees','worn clothes','injured feet'])
claim(d,'17c07','6a:6','The passage gives procedures for detecting and seeing demons, with protective measures.','unmarked continuation; possible inherited Rava attribution uncertain',kind='composite',conditions=['desire to detect/see demons'])
claim(d,'17c08','6a:6','Rav Bibi bar Abaye followed the procedure, saw and was harmed; rabbis prayed and he recovered.','narrator',kind='composite',quote='רב ביבי בר אביי עבד הכי חזא ואתזק בעו רבנן רחמי עליה ואתסי:')
question(d,'17q01','5b:21','What does לפני מטתי mean?')
question(d,'17q02','5b:27','What is the reward if he waits for his fellow?')
edge(d,'17a01','rebuts','17c03','5b:20');edge(d,'17a02','accepts_rebuke','17a01','5b:20')
edge(d,'17a04','alternative_version_of','17a03','5b:20')
edge(d,'17a08','objection_to','17a07','5b:21');edge(d,'17a09','answers','17q01','5b:21');edge(d,'17a09','replaces','17a07','5b:21')
edge(d,'17a10','supports_practice','17a06','5b:23');edge(d,'17a11','adds_to','17a10','5b:24','אף, not contradiction')
edge(d,'17a13','adds_consequence_to','17a12','5b:26');edge(d,'17a14','supports','17a13','5b:26');edge(d,'17a15','answers','17q02','6a:1')
edge(d,'17c04','elaborates','17a16','6a:3');edge(d,'17c05','elaborates','17a16','6a:4');edge(d,'17c06','elaborates','17a16','6a:5');edge(d,'17c08','illustrates_risk_of','17c07','6a:6')
d['comparable_sets']=[{'members':['17a03','17a04'],'type':'alternative narrative outcomes; do not assert both happened'},{'members':['17a07','17a09'],'type':'initial vs corrected interpretation, not maintained scholar disagreement'},{'members':['17a10','17a11'],'type':'compatible addition, not opposed positions'}]
manifest=[freeze(d)]
