import json,pathlib,hashlib,datetime
out=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261126_resume/avodah_source_only');root=pathlib.Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study');plan=json.loads((root/'research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/frozen_plans/bavli_moed_katan.json').read_text(encoding='utf8'));src=pathlib.Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Moed/Moed Katan/Hebrew/Wikisource Talmud Bavli.json');assert hashlib.sha256(src.read_bytes()).hexdigest()==plan['source_sha256'];a=[(i,j,t) for i,pg in enumerate(json.loads(src.read_bytes())['text']) for j,t in enumerate(pg) if t]
def anc(n):
 i,j,t=a[n];return dict(ordinal=n,ref='Moed Katan %d%s:%d'%(i//2+1,'a' if i%2==0 else 'b',j+1),page_index=i,segment_index=j,start_char=0,end_char=len(t),quote=t)
rows='''0|סתם משנה|משקים בית השלחין במועד ובשביעית.|ממעיין שיצא בתחילה או שלא יצא בתחילה|asserted
0|סתם משנה|אין משקים ממי גשמים או מי קילון.|מועד/שביעית כפי הקשר המשנה; טעמי ההבדל בהמשך|asserted
1|סתם משנה|אין עושין עוגיות לגפנים.|בהקשר מועד|asserted
1|רבי אלעזר בן עזריה|אין עושין אמה בתחילה במועד ובשביעית.||asserted
1|חכמים|עושים אמה בתחילה בשביעית.||asserted
1|חכמים|מתקנים אמות מקולקלות במועד.|תיקון ולא עשייה חדשה|asserted
2|סתם משנה|מתקנים קלקולי מים שברשות הרבים וחוטטים אותם.|צורכי רבים|asserted
2|סתם משנה|מתקנים דרכים ורחובות.|צורכי רבים|asserted
2|סתם משנה|מתקנים מקוות מים.|צורכי רבים|asserted
2|סתם משנה|עושים כל צורכי הרבים.||asserted
2|סתם משנה|מציינים קברות.||asserted
2|סתם משנה|יוצאים אף על הכלאים.||asserted
3|סתם|מעיין חדש עשוי ליפול ומעיין ישן אינו עשוי ליפול.|הנחת קושיית הייתור|asserted
4|סתם בהוה אמינא|אילו הוזכר רק מעיין חדש היה אפשר להתיר בית הבעל במעיין ישן.|הוה אמינא שנשללת|rejected
5|סתם|בין מעיין חדש ובין ישן: בית השלחין מותר, בית הבעל לא.|מסקנת צריכותא|asserted
6|סתם|בית השלחין לשון צחותא, בהשוואה לתרגום עיף ויגע.|דרשה לשונית, לא הוכחה היסטורית אטימולוגית|asserted
7|סתם|בית הבעל לשון מייתבותא, בהשוואה לתרגום יבעל בחור בתולה.|דרשה לשונית|asserted
8|סתם|המשנה מתירה למניעת הפסד אך לא להרווחה ואינה מתירה טורח אף במקום הפסד.|קריטריונים בזיהוי התנא|asserted
9|רב הונא|תנא המשנה הוא רבי אליעזר בן יעקב.|הצעה שנדחית ב2a:11–12, לא זיהוי סופי|rejected
9|רבי אליעזר בן יעקב במשנה מצוטטת|מושכים מים מאילן לאילן ובלבד שלא ישקה את השדה כולה.|הגבלת היקף ההשקאה|asserted'''
cs=[]
for line in rows.splitlines():
 n,h,v,c,m=line.split('|');cs.append(dict(id=f'mk_r1_c{len(cs)+1:03}',evidence=[anc(int(n))],holder=h,proposition=v,conditions=[c] if c else [],assertion_mode=m,origin='source_paraphrase'))
qs=[dict(id=f'mk_r1_q{k+1:03}',evidence=[anc(n)],formulation=q,origin='explicit') for k,(n,q) in enumerate([(3,'אם מותר מעיין חדש מה צורך בישן?'),(6,'מנין שבית השלחין לשון צחותא?'),(7,'מנין שבית הבעל לשון מייתבותא?'),(8,'מיהו התנא שמתיר פסידא ולא הרווחה ואף בפסידא אוסר טורח?')])]
edges=[dict(id=f'mk_r1_e{k+1:03}',source_ordinal=x,target_ordinal=y,relation=r,evidence=[anc(x),anc(y)],note=note) for k,(x,y,r,note) in enumerate([(4,3,'answer','counterfactual explains old spring mention'),(5,4,'local_resolution','reject old-spring rain-field permission'),(9,8,'answer','Rav Huna candidate'),(10,9,'objection','cited authority proves no gain, not no toil under loss'),(11,9,'correction','Rav Pappa substitutes Rabbi Yehuda'),(12,11,'qualification','חרבה means its spring dried, not destroyed field'),(13,11,'qualification','Rabbi Elazar ben Azarya bars new spring both cases'),(14,11,'objection','perhaps Rabbi Yehuda only bars rain-field with new spring'),(16,14,'answer','Mishnah attribution forces old/new equivalence; new highlights Rabbi Meir')])]
o=dict(review_schema='source-only-independent-reading-v1',tractate='Moed Katan',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),blind=True,producer_labels_seen=False,source_path=str(src),source_sha256=plan['source_sha256'],plan_sha256=plan['plan_sha256'],core_blocks=['block_000000'],core_ordinals=list(range(10)),context_read_ordinals=list(range(10,24)),claims=cs,questions=qs,edges=edges,boundaries=[dict(start=0,end=2,material='Mishnah work/watering/public needs',status='closed textual unit; internal clauses distinct'),dict(start=3,end=5,material='new/old spring redundancy',status='closed'),dict(start=6,end=7,material='field-name lexical explanations',status='closed'),dict(start=8,end=16,material='identifying tanna with loss/no gain/no toil criteria',status='closed only in context 2b:2'),dict(start=17,end=23,material='Shabbat weeding/watering classification',status='context only; open right')],attribution_notes=['רבי אלעזר בן עזריה in Mishnah is not רבי אליעזר בן יעקב proposed by Rav Huna.','Rav Huna is reporter of identification; Rabbi Eliezer b. Yaakov quoted ruling remains valid text after proposed identification rejected.','Rav Pappa identification of Rabbi Yehuda is downstream context necessary for sampled-core local status.'],counts=dict(core_segments=10,endpoint_segments=10,probability_segments=0,context_segments=14,claims=len(cs),questions=len(qs),edges=len(edges)),limitations=['No full tractate or task qualification','Detailed later Mishnah interpretation not fully read; context outcome limited to first tanna-identification discussion'])
p=out/'moed_katan_opening_frozen.json';p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf8');h=hashlib.sha256(p.read_bytes()).hexdigest();(out/'moed_katan_opening_frozen.sha256').write_text(h+'  '+p.name+'\n');print(h)
