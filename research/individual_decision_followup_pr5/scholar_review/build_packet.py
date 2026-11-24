"""Prepare review forms from immutable PR5 evidence; no scholarly adjudication."""
import hashlib, json, subprocess
from collections import defaultdict
from pathlib import Path

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[1]/'individual_decision_model_2026-11-24'/'scholar'
ROOT=HERE.parents[2]
REV='6ca2dedc547144d7279696bd5322c1e39c7f03d3'
FILES=['evidence_records.jsonl','evidence_context.jsonl','initial_reviews_round1.jsonl','initial_reviews.jsonl','second_review.jsonl','prediction_inputs.jsonl','review_disagreements.jsonl','manual_family_links.json','occurrence_family_map.jsonl','cross_inventory_overlap.jsonl','feasibility_summary.json','INDEPENDENT_REVIEW.md']
QUESTIONS={
'RS06':'מה פירוש האיסור להשתכר פעמיים בביצים, והאם יש מקור המזהה מי אמר כל פירוש?',
'RS09':'מה דין שכיב מרע שכתב וזיכה לשניים בזה אחר זה, ומה היחס לנוסח החלופי בפומבדיתא?',
'RS10':'מה תוקף מתנת שכיב מרע שכתוב בה קניין, ומה משתנה כשמיפה את כוחו?',
'RS13':'מהו המקרה המדויק בהדלקה מנר לנר: ישירות או על ידי קיסם, ומה מעמד ההסברים בהמשך?',
'RS21':'האם הדרשות על נתינת שלום לפני תפילה מציגות עמדות נבדלות או הנמקות לאותו דין?',
'RS24':'מה פירוש הצלע — פרצוף או זנב — והאם ההמשך או מקבילה מזהים את בעלי הדעות?',
'RS26':'מהי עליית הקיר — עלייה שקירוה או אכסדרה שחלקוה — והאם ניתן לייחס כל פירוש?',
'RS28':'האם ברכות שתיתא הן מחלוקת באותו מקרה, או דינים שונים בעבה וברכה?'}
def read(name): return [json.loads(l) for l in (SOURCE/name).read_text(encoding='utf8').splitlines()]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(path,text): (HERE/path).write_text(text+'\n',encoding='utf8')
def dump(path,data): write(path,json.dumps(data,ensure_ascii=False,indent=2))
def link(name,aid,rows):
    line=next((i+1 for i,r in enumerate(rows) if r.get('attempt_id')==aid),None)
    return f'../../../individual_decision_model_2026-11-24/scholar/{name}'+(f'#L{line}' if line else '')
def main():
    before={name:sha(SOURCE/name) for name in FILES}
    records=read('evidence_records.jsonl'); contexts={r['attempt_id']:r for r in read('evidence_context.jsonl')}; second=read('second_review.jsonl')
    initial1=read('initial_reviews_round1.jsonl'); initial2=read('initial_reviews.jsonl'); disagreements=read('review_disagreements.jsonl')
    groups=defaultdict(list)
    for r in records: groups[r['family_id']].append(r)
    inventory=read('occurrence_family_map.jsonl'); cross=read('cross_inventory_overlap.jsonl'); graph_family={r['occurrence_id']:r['family_id'] for r in inventory}
    manifest=[]
    for name in FILES:
        path=SOURCE/name; rel=path.relative_to(ROOT).as_posix()
        blob=subprocess.check_output(['git','hash-object',str(path)],cwd=ROOT,text=True).strip()
        oldblob=subprocess.check_output(['git','rev-parse',f'{REV}:{rel}'],cwd=ROOT,text=True).strip()
        assert blob==oldblob,(name,'not pinned PR5 bytes')
        manifest.append({'path':rel,'local_sha256':before[name],'git_blob_sha1':blob,'matches_delivery_commit':True})
    for sub in ['sources','annotations']: (HERE/sub).mkdir(exist_ok=True)
    index=['# חבילת עיון אנושית והכרעת משפחות מקורות', '', '**הכנה בלבד — לא בוצעה ביקורת אנושית.** 30 משפחות מועמדות, 32 הופעות שנוסו, 24 שאלות מוקד שמישות באופן זמני ו־6 משפחות ממתינות או מוחרגות. שתי קריאות AI אינן אישור מומחה.', '', 'פתחו תחילה את כרטיס המקור, קראו את ההקשר המלא ורשמו הכרעה עצמאית בטופס. רק לאחר שמירת הקריאה הראשונית פתחו את כרטיס הערות ה־AI. אין להסיק ייחוס מסדר השמות בחד אמר, ואין להסיק עמדה משתיקה.', '', '| משפחה | ניסיונות | מעמד קודם | מקורות | כרטיס מקור | הערות קיימות |', '|---|---|---|---|---|---|']
    families=[]; forms=[]; pending=[]
    for fid,rs in sorted(groups.items(),key=lambda item:min(r['attempt_id'] for r in item[1])):
        aids=[r['attempt_id'] for r in rs]; usable=[r for r in rs if r['eligibility']=='provisional_usable']; state='provisional_usable' if usable else 'pending_or_excluded'
        source_lines=[f'# {fid} — מקור לקריאה עצמאית','','לא מולא אישור אנושי. שאלות העזר שלהלן נוסחו ב־AI; הן אינן קביעה על הייחוס או על נכונות הסיווג. לקבלת קריאה בלתי תלויה התחילו בטקסט, תעדו את השאלה בעצמכם, ופתחו את הערות הקריאות הקודמות רק לאחר שמירה.','']
        spans=[]
        for r in rs:
            aid=r['attempt_id']; q=r.get('question_he') or QUESTIONS[aid]
            source_lines += [f'## {aid} — {r["ref"]}', '',f'**שאלת עזר:** {q}', '',f'[הקשר מקורי מלא ופרטי הגרסה]({link("evidence_context.jsonl",aid,list(contexts.values()))})','']
            ctx=contexts[aid]; units={u['ref']:u for u in ctx['source_units']}; chosen={s['ref'] for s in r.get('evidence_spans',[])}
            sr=next(x for x in second if x['attempt_id']==aid); chosen.update(s['ref'] for s in sr['exact_source_quotations'])
            if not r.get('evidence_spans'):
                at=next(i for i,u in enumerate(ctx['source_units']) if u['ref']==r['ref']); chosen.update(u['ref'] for u in ctx['source_units'][max(0,at-1):at+9])
            for u in ctx['source_units']:
                if u['ref'] in chosen:
                    source_lines += [f'**{u["ref"]}**', '', '> '+u['text'], '']
                    spans.append({'attempt_id':aid,'ref':u['ref'],'json_index':u['json_index'],'text':u['text'],'source_sha256':ctx['source_sha256']})
            source_lines += ['**לבדיקה בעברית:** מה השאלה ותנאיה? האם אלו שתי עמדות באותו מקרה? מי הדובר המדויק? מה משנה ההמשך: איפוך, תסתיים, לא פליגי, לשון אחרת, חזרה או דחייה? האם דרוש מקור נוסף?','']
        write(f'sources/{fid}.md','\n'.join(source_lines))
        prior_families={r['original_provisional_family_id'] for r in rs}; occurrence_ids={x['occurrence_id'] for x in inventory if x['family_id'] in prior_families}
        overlaps=[e for e in cross if e['left'] in occurrence_ids or e['right'] in occurrence_ids]
        review_lines=[f'# {fid} — קריאות AI קודמות; לפתוח לאחר הקריאה העצמאית','','**אין כאן הכרעה אנושית.** יש לשמר את ההכרעה הראשונית גם אם משנים אותה לאחר עיון בהערות.','']
        for r in rs:
            aid=r['attempt_id']; review_lines += [f'## {aid}: {r["ref"]}', '',f'Prior state: `{r["eligibility"]}`; review: `{r["review_level"]}`.', '',r.get('notes',''),'',f'[קריאה ראשונה מקורית]({link("initial_reviews_round1.jsonl",aid,initial1)}) · [הרחבת הקריאה הראשונה]({link("initial_reviews.jsonl",aid,initial2)}) · [קריאה שנייה עצמאית]({link("second_review.jsonl",aid,second)}) · [ראיות והכרעה קודמת]({link("evidence_records.jsonl",aid,records)})','']
            if r.get('candidates'):
                review_lines += ['**נוסח קלט ניטרלי קודם, לבדיקת נאמנות והדלפה:**', '', r['question_he'], '',r['conditions_he'],'']+[f'- `{c["candidate_id"]}`: {c["text_he"]}' for c in r['candidates']]+['', '**ייחוס קודם — אינו אישור אנושי:** `'+json.dumps(r['attribution'],ensure_ascii=False)+'`','']
            for d in disagreements:
                if d['attempt_id']==aid: review_lines += ['**מחלוקת/תיקון שנשמרו:**', '', '```json', json.dumps(d,ensure_ascii=False,indent=2),'```','']
        review_lines += ['## הכרעת משפחה ומקבילות', '', 'האם מדובר באותה שאלה, באותה מסורת, בהמשך רלוונטי או בחפיפה חושפת־תשובה? נושא משותף בלבד אינו ראיה לאיחוד. יש לתעד גם קשר שטרם הוכרע, ולא לפצל אותו למדגם אישור עד להכרעה.', '', f'מספר קשרי חפיפת הקשר מכניים בין אינדקסים: {len(overlaps)}. אלו מועמדים לבדיקה, לא הוכחת שאלות משותפות. הרשימה המדויקת נמצאת ב־`family_packets.json`.', '', 'יש לבדוק מקבילות גם מעבר לחפיפות האוטומטיות; הערות המקור לעיל מציינות קשרים ידועים או חשודים. אין להגדיר אמורא שלא נזכר כבעל עמדה שלילית.']
        write(f'annotations/{fid}.md','\n'.join(review_lines))
        index.append(f'| `{fid}` | {", ".join(aids)} | {state} | {"; ".join(r["ref"] for r in rs)} | [מקור](sources/{fid}.md) | [AI](annotations/{fid}.md) |')
        family={'family_id':fid,'attempt_ids':aids,'prior_status':state,'usable_focal_attempt_ids':[r['attempt_id'] for r in usable],'sources':[r['ref'] for r in rs],'source_card':f'sources/{fid}.md','annotation_card':f'annotations/{fid}.md','exact_excerpt_spans':spans,'mechanical_overlap_candidates':overlaps,'prior_disagreements':[d for d in disagreements if d['attempt_id'] in aids],'human_review_status':'not_performed'}
        families.append(family)
        if not usable: pending.append({'family_id':fid,'attempt_ids':aids,'refs':family['sources'],'prior_reasons':[{'attempt_id':r['attempt_id'],'reason':r.get('reason'),'notes':r.get('notes')} for r in rs],'questions_he':[QUESTIONS[r['attempt_id']] for r in rs]})
        blank={'reviewer_name':None,'expertise':None,'date':None,'read_AI_annotations_before_initial_decision':None,'source_version_checked':None,'full_context_refs_read':[],'question_he':None,'conditions_he':None,'alternatives':[],'named_attributions':None,'attribution_evidence_refs':[],'discussion_status':None,'eligibility_decision':None,'reason_he':None,'parallel_refs':[],'family_merge_or_separate_proposal':None,'grouping_evidence':None,'neutral_input_changes':None,'remaining_uncertainty':None,'signature':None}
        forms.append({'family_id':fid,'attempt_ids':aids,'human_review_status':'not_performed','independent_reader_1':dict(blank),'independent_reader_2':dict(blank),'adjudication':{'adjudicator':None,'date':None,'initial_disagreements':[],'resolution':None,'final_eligibility':None,'final_family_id':None,'signature':None}})
    if (HERE/'human_review_forms.json').exists():
        assert json.loads((HERE/'human_review_forms.json').read_text(encoding='utf8'))==forms, 'Refusing to overwrite changed or filled human review forms'
    write('INDEX.md','\n'.join(index)); dump('family_packets.json',families); dump('pending_families.json',pending); dump('human_review_forms.json',forms)
    pending_md=['# שש המשפחות הממתינות או המוחרגות','','זהו סיכום ההכרעות הקודמות בלבד, ללא הכרעה אנושית חדשה.']
    for f in pending:
        pending_md += ['',f'## {", ".join(f["attempt_ids"])} — {"; ".join(f["refs"])}','',f'[מקור](sources/{f["family_id"]}.md) · [קריאות קודמות](annotations/{f["family_id"]}.md)','']+f['questions_he']
        for reason in f['prior_reasons']: pending_md += ['',f'`{reason["reason"]}`: {reason["notes"]}']
    write('PENDING_FAMILIES.md','\n'.join(pending_md))
    dump('source_manifest.json',{'source_delivery_commit':REV,'source_files':manifest,'human_review_performed':False,'scope':'Review preparation only; no new source attribution, fitting or confirmation scoring','counts':{'candidate_families':len(families),'attempted_occurrences':len(records),'usable_focal_cases':sum(len(f['usable_focal_attempt_ids']) for f in families),'pending_or_excluded_families':len(pending)}})
    assert before=={name:sha(SOURCE/name) for name in FILES},'Prior artifacts were modified'
    print('Prepared 30 families / 24 usable focal cases / 6 pending families; prior hashes unchanged.')
if __name__=='__main__': main()
