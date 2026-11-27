import json, hashlib
from pathlib import Path

B = Path(__file__).resolve().parent.parent
J = json.loads((B/'jobs/bavli_rosh_hashanah.json').read_text(encoding='utf-8'))
P = json.loads(Path(J['frozen_plan']['path']).read_text(encoding='utf-8'))
S = json.loads(Path(J['source']['path']).read_text(encoding='utf-8'))
texts = {f'Rosh Hashanah {i//2+1}{"a" if i%2==0 else "b"}:{k+1}': t for i,page in enumerate(S['text']) for k,t in enumerate(page)}
core = [x['ref'] for b in P['review_blocks'][:2] for x in b['spans']]
def ev(r, quote=None):
    r = r if r.startswith('Rosh') else 'Rosh Hashanah '+r
    t=texts[r]; quote=t if quote is None else quote; a=t.index(quote)
    return {'ref':r,'start_char':a,'end_char':a+len(quote),'quote':quote}
records=[]
def claim(i,r,meaning,holder=None,conditions=(),status='asserted',quote=None,uncertainty=()):
    records.append({'id':i,'kind':'atomic_claim','origin':'source_paraphrase','interpretation':meaning,'evidence':[ev(r,quote)],'holder':holder,'transmission_chain':[],'conditions':list(conditions),'local_status':status,'uncertainty':list(uncertainty)})

claim('c01','2a:1','There are four new-year dates.','anonymous Mishnah',quote='ארבעה</strong></big> ראשי שנים הם')
claim('c02','2a:1','First Nisan is the new year for kings.','anonymous Mishnah',quote='באחד בניסן ר"ה למלכים ולרגלים',uncertainty=['Scope restricted to Israelite kings by Rav Hisda in 3a:14; exceptional treatment of a foreign king discussed through 4a:11.'])
claim('c03','2a:1','First Nisan designates the new year for festivals.','anonymous Mishnah',quote='באחד בניסן ר"ה למלכים ולרגלים',uncertainty=['4a:12 interprets the festival within this month, not a festival occurring on its first day.'])
claim('c04','2a:2','First Elul is the new year for animal tithe.','anonymous Mishnah',quote='באחד באלול ראש השנה למעשר בהמה')
claim('c05','2a:2','First Tishri is the new year for animal tithe.',"R. Eleazar and R. Shimon",quote='ר\' אלעזר ור"ש אומרים באחד בתשרי')
for i,n in enumerate(['years','sabbatical years','jubilee years','planting','vegetables'],6):
    claim(f'c{i:02}','2a:3',f'First Tishri is the new year for {n}.','anonymous Mishnah')
claim('c11','2a:4','First Shevat is the new year for the tree.','Beit Shammai',quote='באחד בשבט ראש השנה לאילן כדברי בית שמאי')
claim('c12','2a:4','Fifteenth Shevat is the new year for the tree.','Beit Hillel',quote='בית הלל אומרים בחמשה עשר בו:')
claim('c13','2a:5','The practical application of the regnal new year is documents.','Rav Hisda',quote='אמר רב חסדא לשטרות')
claim('c14','2a:6','Antedated debt documents are invalid.','quoted anonymous Mishnah',quote='שטרי חוב המוקדמין פסולין')
claim('c15','2a:6','Postdated debt documents are valid.','quoted anonymous Mishnah',quote='והמאוחרין כשרין')
claim('c16','2a:7','A king is credited with a year on first Nisan.','anonymous baraita',['accession on 29 Adar'],quote='מלך שעמד בעשרים ותשעה באדר כיון שהגיע אחד בניסן עלתה לו שנה')
claim('c17','2a:7','A king is not credited with a year until the next Nisan.','anonymous baraita',['accession on first Nisan'],quote='ואם לא עמד אלא באחד בניסן אין מונין לו שנה עד שיגיע ניסן אחר')
claim('c18','2a:8','The Adar accession rule is repeated as the lemma for analysis.','anonymous baraita quoted by discussion',['accession on 29 Adar'],quote='מלך שעמד בעשרים ותשעה באדר כיון שהגיע אחד בניסן עלתה לו שנה')
claim('c19','2b:1','Nisan is the new year for kings.','anonymous discussion',quote='קמ"ל דניסן ר"ה למלכים')
claim('c20','2b:1','One day within a year counts as a year.','anonymous discussion',quote='ויום אחד בשנה חשוב שנה')
claim('c21','2b:1','The first-Nisan accession rule is repeated for analysis.','anonymous baraita quoted by discussion',['accession on first Nisan'],quote='ואם לא עמד אלא באחד בניסן אין מונין לו שנה עד שיגיע ניסן אחר')
claim('c22','2b:2','The case concerns a king selected in Adar but who acceded only in Nisan.','anonymous discussion',['selection in Adar','accession in Nisan'],'qualification',quote='לא צריכא דאימנו עליה מאדר')
claim('c23','2b:2','One might count two years based on the prior Adar selection.','anonymous discussion',['selection in Adar','accession in Nisan'],'rejected_hypothesis',quote='מהו דתימא נימנו ליה תרתין שנין')
claim('c24','2b:2','The prior selection does not yield the proposed two-year count.','anonymous discussion',['selection in Adar','accession in Nisan'],'local_resolution',quote='מהו דתימא נימנו ליה תרתין שנין קמ"ל')

claim('c25','4b:7','Failure to bring after the commanded occasion entails bal teaher.','R. Meir as explained by anonymous discussion',['a festival passed without bringing'],quote='ורבי מאיר כיון דאמר ליה רחמנא אייתי ולא אייתי ממילא קם ליה בבל תאחר')
claim('c26','4b:8','The plural moadeikhem supplies a minimum of two festivals.','R. Eliezer b. Jacob as explained by discussion',quote='ורבי אליעזר בן יעקב מאי טעמא דכתיב (במדבר כט, לט) אלה תעשו לה\' במועדיכם מיעוט מועדים שנים')
claim('c27','4b:9','The festivals are juxtaposed to one another.','R. Jonah',quote='דאמר רבי יונה הוקשו כל המועדים כולם זה לזה')
claim('c28','4b:9','All festivals provide atonement for impurity of Sanctuary and sacred things.','R. Jonah',quote='שכולן מכפרים על טומאת מקדש וקדשיו')
claim('c29','4b:9','The Rabbis use moadeikhem for the teaching of R. Jonah.','Rabbis as explained by discussion',quote='ורבנן ההוא לכדרבי יונה')
claim('c30','4b:10','The otherwise unnecessary mention of Sukkot identifies it as the cause of bal teaher.','R. Eleazar b. Shimon',['Sukkot passes'],quote='רבי אלעזר בר\' שמעון אומר לא יאמר חג הסוכות שבו דיבר הכתוב למה נאמר לומר שזה גורם')
claim('c31','4b:11','R. Meir and R. Eliezer b. Jacob use the festival list for the Shavuot compensatory period teaching.','R. Meir and R. Eliezer b. Jacob as explained by discussion',quote='ורבי מאיר ורבי אליעזר בן יעקב האי בחג המצות ובחג השבועות ובחג הסוכות מאי דרשו ביה מיבעי להו לכדרבי אלעזר אמר ר\' אושעיא')
claim('c32','4b:11','Shavuot has a compensatory offering period of seven days.','R. Oshaya',quote='דאמר ר\' אלעזר אמר ר\' אושעיא מניין לעצרת שיש לה תשלומין כל שבעה תלמוד לומר בחג המצות ובחג השבועות ובחג הסוכות מקיש חג השבועות לחג המצות מה חג המצות יש לו תשלומין כל שבעה אף חג השבועות יש לו תשלומין כל שבעה')
records[-1]['transmission_chain']=['R. Eleazar','R. Oshaya']
claim('c33','4b:11','Passover has a compensatory period of seven days.','R. Oshaya transmitted by R. Eleazar',quote='מה חג המצות יש לו תשלומין כל שבעה')
claim('c34','4b:12','By comparison to Sukkot Shavuot might have eight compensatory days.','anonymous discussion',status='challenged_alternative',quote='וליקש לחג הסוכות מה להלן שמונה אף כאן שמונה')
claim('c35','4b:12','The eighth day is an independent festival.','anonymous discussion',status='attempted_answer_limited_by_continuation',quote='שמיני רגל בפני עצמו הוא')
claim('c36','4b:13','The eighth day is independent for the matters designated PZR QShB.','anonymous discussion',quote='אימור דאמרינן שמיני רגל בפני עצמו לענין פז"ר קש"ב')
claim('c37','4b:13','For compensation all agree that the eighth day compensates for the first.','anonymous discussion reporting consensus',quote='אבל לעניין תשלומין דברי הכל תשלומין דראשון הוא')
claim('c38','4b:14','One may offer the festival offering throughout Sukkot.','quoted anonymous Mishnah',['did not offer on the first festival day'],quote='מי שלא חג יום טוב הראשון של חג חוגג את כל הרגל')
claim('c39','4b:14','One may offer on the last festival day too.','quoted anonymous Mishnah',['did not offer on the first festival day'],quote='מי שלא חג יום טוב הראשון של חג חוגג את כל הרגל ויום טוב האחרון של חג')
claim('c40','4b:15','Taking the larger amount does not secure the inference.','anonymous discussion',quote='תפשת מרובה לא תפשת')
claim('c41','4b:15','Taking the smaller amount secures the inference.','anonymous discussion',quote='תפשת מועט תפשת')
claim('c42','4b:16','Sukkot is written to compare it with Passover.','anonymous discussion',quote='לאקושיה לחג המצות',uncertainty=['The substantive application, overnight lodging, is in context 5a:1.'])

def finding(i,kind,meaning,refs,**kw):
    records.append({'id':i,'kind':kind,'interpretation':meaning,'origin':'source_paraphrase','evidence':[ev(r) for r in refs],'uncertainty':[],**kw})
finding('ctx01','context_finding','Succession during Adar or Nisan may count a year for both kings; selection in Adar plus royal descent does not replace actual accession in Nisan.',['2b:3','2b:4','2b:5','2b:6'],local_status='cases explained, not a named dispute')
finding('ctx02','context_finding','R. Yohanan derives Nisan counting by analogy of Solomon to the Exodus; the discussion tests alternative epochs and months. R. Eleazar supplies Chronicles; a baraita supports R. Yohanan.',['2b:7','2b:8','2b:11','3a:8','3a:11','3a:13'],local_status='Nisan supported; proof supplemented')
finding('ctx03','context_finding','Rav Hisda restricts the Nisan rule to Israelite kings and counts foreign kings from Tishri. Rav Pappa supplies the twenty-year analogy; do not confuse him with Rav himself.',['3a:14','3b:1'],local_status='explicit scope qualification')
finding('ctx04','context_finding','Rav Joseph objects from Darius. R. Abbahu explains counting Cyrus as Israelite because of fitness; a baraita identifies Cyrus, Darius and Artaxerxes here. R. Isaac distinguishes before and after deterioration.',['3b:7','3b:8','3b:9','3b:10','3b:11'],local_status='chronological reconciliation, not simple opposite rules')
finding('ctx05','context_finding','Rabbah b. Lima transmits Rav on shegal; a later alternative retains the transmitted particular interpretation while permitting the ordinary queen sense. The capped-gift proof is challenged; the text returns to the earlier answer.',['4a:6','4a:9','4a:10','4a:11'],local_status='alternative explanations and rejected last proof',transmission_chain=['Rabbah b. Lima','Rav'],attribution_uncertainty=['The lead proof attribution is Rav Joseph or R. Isaac; preserve the alternative.'])
finding('ctx06','context_finding','Rav Hisda construes the festival in Nisan as the first festival for the bal-teaher cycle, and the passage identifies the Mishnah with R. Shimon. R. Shimon requires ordered festivals beginning with Passover.',['4a:12','4a:13','4a:14'],local_status='interpretation of opening Mishnah; not literal first-Nisan festival')
finding('ctx07','context_finding','The baraita presents three festivals (first tanna), three ordered beginning Passover (R. Shimon), one (R. Meir), two (R. Eliezer b. Jacob), and Sukkot as trigger (R. Eleazar b. Shimon). These are genuinely comparable timing positions; do not merge the two Eliezer/Eleazar names.',['4b:1','4b:2'],local_status='five alternatives preserved')
finding('ctx08','context_finding','The Rabbis read the bring-to-the-place verse as a positive obligation, unlike R. Meir’s negative-prohibition implication.',['4b:5','4b:6','4b:7'],local_status='verse-use disagreement')
finding('ctx09','context_finding','The Sukkot comparison requires overnight lodging, based on Passover and the morning-return verse.',['4b:16','5a:1','5a:2'],local_status='answer completed across page boundary')
finding('ctx10','context_finding','Other tannaim derive Shavuot compensation through Rabbah b. Samuel’s teaching about counting and sanctification. Rava answers the one-day challenge with the week-count and the festival name.',['5a:3','5a:4','5a:5'],local_status='alternative derivation supported',attribution_uncertainty=['5a:3 prints ורבי שמעון (בן אלעזר); retain this literal parenthetical rather than silently standardizing the name.'])

questions=[
('q01','When does animal-tithe year begin?',['2a:2'],['c04','c05'],'editorial_reconstruction','same subject and calendar boundary; no conclusion in opening Mishnah'),
('q02','When does the tree year begin?',['2a:4'],['c11','c12'],'editorial_reconstruction','same subject and date; positions preserved without ruling'),
('q03','What practical law is affected by the regnal new year?',['2a:5','2a:6'],['c13'],'explicit','documents answer, with debt-document support'),
('q04','What does the Adar accession case teach?',['2a:8','2b:1'],['c19','c20'],'editorial_reconstruction','two cumulative teachings, not mutually exclusive answers'),
('q05','Why teach the apparently obvious first-Nisan accession case?',['2b:1','2b:2'],['c22','c24'],'explicit','prior selection is the case condition; two-year hypothesis rejected'),
('q06','How many festivals trigger bal teaher?',['4b:1','4b:2','4b:7','4b:8','4b:10'],['c25','c26','c30','ctx07'],'editorial_reconstruction','five timing alternatives; core includes rationales and context supplies complete answer inventory'),
('q07','What is the use of moadeikhem?',['4b:8','4b:9'],['c26','c29'],'explicit','two-festival minimum versus R. Jonah teaching; shared verse, distinct derivational use'),
('q08','Why seven rather than eight compensatory days for Shavuot?',['4b:11','4b:12','4b:13','4b:14','4b:15'],['c32','c34','c35','c40','c41'],'explicit','eight is challenged proposal; independent-festival answer insufficient; smaller inference locally resolves'),
('q09','Why is Sukkot written in the list?',['4b:16','5a:1','5a:2'],['c42','ctx09'],'explicit','lodging answer completes in context')]
for i,meaning,refs,answers,origin,status in questions:
    finding(i,'question_answer_set',meaning,refs,question_origin=origin,answer_ids=answers,comparability_and_local_status=status)

edges=[
('e01','c14','c13','support',['2a:5','2a:6'],'Debt-document validity explains practical relevance.'),
('e02','c15','c13','support',['2a:5','2a:6'],'Later-dated validity is the complementary quoted case.'),
('e03','c22','q05','answer',['2b:1','2b:2'],'Prior Adar selection supplies non-obvious circumstances.'),
('e04','c24','c23','correction',['2b:2'],'The kamashma-lan rejects two years based on prior selection.'),
('e05','ctx03','c02','qualification',['3a:14'],'Nisan rule restricted to Israelite kings.'),
('e06','ctx06','c03','qualification',['4a:12','4a:13'],'Festival within Nisan is intended.'),
('e07','c25','ctx08','objection',['4b:6','4b:7'],'R. Meir explains why the command also entails negative prohibition.'),
('e08','c29','c26','distinction',['4b:8','4b:9'],'Alternative use of the same verse.'),
('e09','c33','c32','analogy',['4b:11'],'Passover seven-day compensation supports Shavuot seven days.'),
('e10','c34','c32','objection',['4b:12'],'Sukkot offers eight-day comparandum.'),
('e11','c35','c34','answer',['4b:12'],'Initially proposed independent-eighth-day response.'),
('e12','c37','c35','objection',['4b:13'],'Independence does not exclude compensatory relation.'),
('e13','c38','c37','support',['4b:14'],'Quoted offering rule supports compensation for first day.'),
('e14','c39','c37','support',['4b:14'],'Last day expressly included.'),
('e15','c41','q08','local_resolution',['4b:15'],'Smaller secure inference supplies local answer.'),
('e16','ctx09','q09','answer',['4b:16','5a:1','5a:2'],'Overnight lodging completes the cross-page answer.')]
for i,src,tgt,rel,refs,meaning in edges:
    finding(i,'directed_relation',meaning,refs,source_id=src,target_id=tgt,relation=rel,explicitness='source_explicit')

finding('b01','boundary','The opening Mishnah is 2a:1–4; Gemara begins in 2a:5. The accession lemma crosses 2a/2b and the first core closes after its answer, not after the complete kings discussion.',['2a:1','2a:4','2a:5','2a:8','2b:1','2b:2'],local_status='core boundary not sugya boundary')
finding('b02','boundary','Kings discussion continues through 4a:11. Festival lemma begins 4a:12. The second core enters mid-derivation and ends before the lodging answer. Relevant derivational exchange ends at 5a:5 before a new Passover-list issue.',['4a:11','4a:12','4b:7','4b:16','5a:1','5a:5','5a:6'],local_status='expanded context closes affected arguments')

read_refs=[r for r in texts if 2<=int(r.split()[2].split(':')[0][:-1])<=5 and (not r.startswith('Rosh Hashanah 5b:'))]
# Explicit scope actually used for complete kings/festival arguments; 5a:6 is boundary observation.
read_refs=[r for r in read_refs if not r.startswith('Rosh Hashanah 5a:') or int(r.split(':')[-1])<=6]
context=[r for r in read_refs if r not in core]
def den(refs):
    rr=[r for r in records if any(e['ref'] in refs for e in r['evidence'])]
    cc=[r for r in rr if r['kind']=='atomic_claim']
    return {'core_segments':len(refs),'independently_found_claims':len(cc),'attributable_claims':sum(r['holder'] is not None for r in cc),'named_or_named_collective_attributable_claims':sum(not r['holder'].startswith(('anonymous','quoted anonymous')) for r in cc),'condition_bearing_claims':sum(bool(r['conditions']) for r in cc),'proposed_answer_sets':sum(r['kind']=='question_answer_set' for r in rr),'edges':sum(r['kind']=='directed_relation' for r in rr),'claim_ids':[r['id'] for r in cc],'answer_set_ids':[r['id'] for r in rr if r['kind']=='question_answer_set'],'edge_ids':[r['id'] for r in rr if r['kind']=='directed_relation']}
out={'artifact_kind':'frozen_source_only_substantive_reading','job_id':J['job_id'],'batch_id':'rosh_hashanah_batch001','execution':{'agent_id':'/root/reader_rosh_hashanah','route':'interactive_agent','model_id':None},'fresh_context':{'fork_turns':'none','producer_labels_exposed':False},'source_sha256':J['source']['sha256'],'plan_file_sha256':J['frozen_plan']['sha256'],'plan_sha256':P['plan_sha256'],'producer_labels_exposed':False,'frozen_before_comparison':True,'verification':{'all_common_document_hashes_verified':True,'source_schema_hash_verified':True,'source_bytes_hash_verified':True,'plan_file_and_domain_canonical_hash_verified':True,'twenty_selected_span_hashes_verified':True},'core_refs':core,'context_refs':context,'cohorts':{'endpoint_only':{'block_ids':['block_000000'],'core_refs':core[:10],'denominators':den(core[:10])},'probability_only':{'block_ids':['block_000007'],'core_refs':core[10:],'denominators':den(core[10:])},'overlap':{'block_ids':[],'core_refs':[],'denominators':den([])},'context_expansion':{'refs':context,'segment_count':len(context),'not_in_sample_denominator':True}},'core_denominators':den(core),'denominator_policy':'Claims count atomic occurrence records, including repetitions and explicitly marked rejected hypotheses. Attributable includes anonymous textual voices; named subcount is separate. Condition-bearing means explicit nonempty conditions list. Questions/edges counted when any direct evidence is core; cross-core/context edges count once in union. Context summaries are not atomic core claims. This is an independent initial inventory, not exhaustive certification.','records':records,'uncertainties':['Opening Mishnah calendar clauses are faithfully inventoried here; later tractate discussions of animal tithe, years, planting, vegetables and tree dates are outside these two-block argument expansions. Their final halakhic outcomes are not asserted.','R. Eleazar/R. Eliezer name forms preserved locally; no silent identity harmonization.','The production schema was read for semantic categories; this review artifact is not a production proposal and does not claim full character-partition coverage.','No producer comparison, discrepancy findings, ML eligibility, or tractate verdict has been issued.'],'next_selected_block':{'block_id':P['review_blocks'][2]['block_id'],'core_refs':[x['ref'] for x in P['review_blocks'][2]['spans']]},'source_metadata':{k:S[k] for k in ['title','versionTitle','versionSource','license']}}
for r in records:
    for e in r['evidence']:
        assert texts[e['ref']][e['start_char']:e['end_char']]==e['quote']
ids={r['id'] for r in records}
for r in records:
    if r['kind']=='directed_relation':assert r['source_id'] in ids and r['target_id'] in ids
out['verification']['evidence_slices_validated']=sum(len(r['evidence']) for r in records)
dest=B/'readings/rosh_hashanah_batch001.json'
raw=(json.dumps(out,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
with dest.open('xb') as f:f.write(raw)
h=hashlib.sha256(raw).hexdigest()
with dest.with_suffix('.json.sha256').open('x',encoding='ascii') as f:f.write(h+'  '+dest.name+'\n')
print(json.dumps({'path':str(dest),'sha256':h,'records':len(records),'core_denominators':out['core_denominators'],'context_segments':len(context),'evidence_slices':out['verification']['evidence_slices_validated']},ensure_ascii=False))
