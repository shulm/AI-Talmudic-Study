import json,pathlib,hashlib
out=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261126_resume/source_only')
repo=pathlib.Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
def sha(b): return hashlib.sha256(b).hexdigest()
def freeze(job,title,seder,blocks,read,claims,questions,edges,bounds,notes,nextwork):
 p=pathlib.Path('F:/Sefaria-Export-master/json/Talmud/Bavli')/seder/title/'Hebrew/Wikisource Talmud Bavli.json'; raw=p.read_bytes(); d=json.loads(raw)
 planpath=repo/'research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/frozen_plans'/f'{job}.json'; plan=json.loads(planpath.read_text()); selected=[b for b in plan['review_blocks'] if b['block_id'] in blocks]
 rows=[(i,j,t) for i,pg in enumerate(d['text']) for j,t in enumerate(pg) if t]; cores={s['nonempty_ordinal'] for b in selected for s in b['spans']}; refs={k:f'{title} {i//2+1}{chr(97+i%2)}:{j+1}' for k,(i,j,t) in enumerate(rows)}
 def evidence(k):
  i,j,t=rows[k]; return dict(nonempty_ordinal=k,ref=refs[k],page_index=i,segment_index=j,start_char=0,end_char=len(t),quote=t,quote_sha256=sha(t.encode()))
 cs=[]
 for num,(k,holder,prop,cond,status) in enumerate(claims,1): cs.append(dict(id=f'C{num:03}',evidence=[evidence(k)],position_holder=holder,proposition_paraphrase=prop,conditions=cond,local_status=status,cohort='core' if k in cores else 'context',ml_eligible=False))
 qs=[dict(id=f'Q{n:03}',evidence=[evidence(k)],question_paraphrase=q,voice=v) for n,(k,q,v) in enumerate(questions,1)]
 es=[dict(id=f'E{n:03}',source_ordinal=a,target_ordinal=b,relation=r,explanation=x,evidence=[evidence(a),evidence(b)]) for n,(a,b,r,x) in enumerate(edges,1)]
 obj=dict(format='independent-source-reading-v1',reviewer='/root/source_review',model_id=None,blindness='Source-first; no production annotations, proposals, snapshots, comparisons or other readings viewed.',job=job,source_path=str(p),source_sha256=sha(raw),edition=d['versionTitle'],license=d.get('license'),plan_file_sha256=sha(planpath.read_bytes()),plan_sha256=plan['plan_sha256'],selected_blocks=selected,contract_sha256={n:sha((repo/'research/bavli_production_v1'/n).read_bytes()) for n in ['schema.json','PROTOCOL.md']},scope=dict(total_nonempty_segments=len(rows),core_ordinals=sorted(cores),context_only_ordinals=sorted(set(read)-cores),core_segments=len(cores),core_characters=sum(len(rows[k][2]) for k in cores),context_only_segments=len(set(read)-cores),context_only_characters=sum(len(rows[k][2]) for k in set(read)-cores),probability_core_segments=len({s['nonempty_ordinal'] for b in selected if 'probability_sample' in b['roles'] for s in b['spans']}),endpoint_core_segments=len({s['nonempty_ordinal'] for b in selected if 'opening_check' in b['roles'] or 'closing_check' in b['roles'] for s in b['spans']})),source_read=[evidence(k) for k in read],claims=cs,questions=qs,edges=es,boundaries=[dict(start_ordinal=a,end_ordinal_exclusive=b,description=x,status=s) for a,b,x,s in bounds],attribution_and_uncertainty_notes=notes,measurement_denominators=dict(independent_core_claims=sum(c['cohort']=='core' for c in cs),independent_context_claims=sum(c['cohort']=='context' for c in cs),claims_with_conditions=sum(bool(c['conditions']) for c in cs),questions=len(qs),directed_edges=len(es),boundary_opportunities=len(bounds)),next_work=nextwork,qualification='Partial independent AI reading only; no comparison, acceptance, human certification or task eligibility. Plans elsewhere remain unread, and context is not promoted to sampled core.')
 for span in [e for c in cs for e in c['evidence']]+obj['source_read']:
  assert rows[span['nonempty_ordinal']][2][span['start_char']:span['end_char']]==span['quote']
 b=(json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode(); f=out/f'{job}_batch01.json'; f.open('xb').write(b); (out/f'{job}_batch01.sha256').open('x').write(sha(b)+'  '+f.name+'\n'); print(f.name,sha(b),obj['scope'],obj['measurement_denominators'])
freeze('bavli_taanit','Taanit','Seder Moed',['block_000004','block_000005'],list(range(37,60)),[
(40,'רבי יהודה reporting בן בתירה','The latter prayer leader on final festival day mentions rain.', ['יום טוב האחרון של חג','האחרון'], 'reported; holder identification questioned'),
(41,'רב נחמן בר יצחק','The authority is Rabbi Yehoshua ben Beteira.', [], 'local identification'),
(41,'רב נחמן בר יצחק','Personal and patronymic naming reflect before/after ordination.', [], 'reconciliation; do not infer chronology beyond text'),
(42,'anonymous tanna','Sages did not require mention of dew.', [], 'asserted'),
(42,'anonymous tanna','Sages did not require mention of winds.', [], 'asserted'),
(42,'anonymous tanna','Voluntary mention is permitted.', ['person wishes to mention dew/wind'], 'asserted'),
(42,'רבי חנינא','Dew and winds are not withheld.', [], 'reason; qualified by continuation'),
(43,'anonymous','God promises restoration of rain without mentioning dew.', ['Elijah narrative'], 'scriptural evidence'),
(44,'anonymous','Elijah meant that even blessed dew would not come.', ['scope of oath'], 'distinction'),
(44,'anonymous','Restoration of blessed dew was not stated because it is not discernible.', [], 'reply'),
(45,'רבי יהושע בן לוי','The world cannot exist without winds.', [], 'verse interpretation'),
(45,'רבי יהושע בן לוי','The world cannot exist without Israel.', [], 'verse analogy'),
(46,'רבי חנינא','Saying משיב הרוח does not require repetition.', ['summer'], 'asserted'),
(46,'רבי חנינא','Saying מוריד הגשם requires repetition.', ['summer'], 'asserted'),
(47,'רבי חנינא; continued speech','Omitting משיב הרוח does not require repetition.', ['rainy season'], 'asserted'),
(47,'רבי חנינא; continued speech','Omitting מוריד הגשם requires repetition.', ['rainy season'], 'asserted'),
(47,'רבי חנינא; continued speech','Even saying מעביר הרוח ומפריח הטל does not require repetition.', ['rainy season inherited context'], 'asserted'),
(48,'anonymous tanna','Mention of clouds is not obligatory.', [], 'asserted'),
(48,'anonymous tanna','Mention of winds is not obligatory.', [], 'asserted'),
(48,'anonymous tanna','Voluntary mention is allowed.', ['clouds/winds'], 'asserted'),
(49,'baraita transmitted by רב יוסף','ועצר את השמים concerns clouds and winds.', ['rain already specified separately'], 'challenge evidence; not necessarily Rav Yosef personal ruling'),
(50,'anonymous','Cloud statements concern חרפי and אפלי respectively.', ['different cloud classes'], 'reconciled; exact meteorological gloss not settled here'),
(51,'anonymous','Wind statements distinguish common and uncommon wind.', ['common wind unwithheld; uncommon wind may stop'], 'reconciled'),
(51,'anonymous','Winnowing can use fans.', ['uncommon wind useful for threshing absent'], 'reply to functional objection'),
(52,'anonymous tanna','Clouds and winds rank next to rain.', [], 'asserted, qualified'),
(52,'עולא or רבי יהודה','The beneficial case is after rain.', ['clouds/winds after rain'], 'alternative attribution printed רבי יהודה'),
(52,'עולא or רב יהודה','The dust-and-earth curse is wind after rain.', [], 'alternative attribution; challenge evidence'),
(53,'anonymous','Gentle and forceful wind distinguish the cases.', ['post-rain wind'], 'first reconciliation'),
(53,'anonymous','Dust-raising and non-dust-raising wind distinguish the cases.', ['post-rain wind'], 'alternative reconciliation'),
(54,'רב יהודה','Wind after rain is like rain.', ['post-rain; earlier distinctions retained'], 'asserted'),
(54,'רב יהודה','Cloud after rain is like rain.', ['post-rain'], 'asserted'),
(54,'רב יהודה','Sun after rain is like two rains.', ['post-rain'], 'asserted'),
(54,'anonymous','The comparison excludes גילהי דליליא and שמשא דביני קרחי.', [], 'scope exclusion; leave technical gloss open'),
(55,'רבא','Snow benefits mountains like five rains benefit land.', [], 'asserted; verse support'),
(56,'רבא','Snow is beneficial for mountains.', [], 'asserted'),
(56,'רבא','Forceful rain is beneficial for trees.', [], 'asserted'),
(56,'רבא','Gentle rain is beneficial for fruit.', [], 'asserted'),
(57,'continued anonymous textual clause; likely inherited רבא','עורפילא benefits even a seed beneath a clod.', [], 'asserted; inheritance noted'),
(57,'רבא','A young scholar resembles a seed under a clod: once sprouted, it sprouts.', [], 'analogy'),
(58,'רבא','Torah causes a young scholar to become heated.', ['scholar anger'], 'explanation, not unrestricted permission'),
(58,'רב אשי','A scholar who is not hard as iron is no scholar.', [], 'asserted'),
(59,'רבי אבא addressing רב אשי','Our derivation uses אבניה read as בוניה.', [], 'alternative proof, not opposing substantive ruling'),
(59,'רבינא','Nevertheless one should train oneself in gentleness.', [], 'qualification of preceding anger/hardness statements')
],[(40,'Which Ben Beteira, given Rabbi Yehuda ben Beteira begins on day two?','anonymous'),(43,'How do we know dew is not withheld?','anonymous'),(44,'Why did Elijah swear about dew?','anonymous'),(44,'Why not restore blessed dew explicitly?','anonymous'),(45,'How do we know winds are not withheld?','anonymous'),(49,'Does the withholding verse not include clouds/winds?','anonymous via Rav Yosef baraita'),(51,'Is uncommon wind not useful for threshing?','anonymous'),(52,'How can post-rain wind be good given curse verse?','anonymous'),(54,'What is excluded by these comparisons?','anonymous'),(57,'What is עורפילא?','anonymous')],[(41,40,'reply','Identifies Yehoshua ben Beteira without merging him with Yehuda ben Beteira.'),(43,42,'support','Omission of dew in restoration promise supports dew not withheld.'),(44,43,'qualification','Blessed dew distinguished from dew simpliciter.'),(49,48,'objection','Baraita appears to contradict inability to withhold clouds/winds.'),(50,49,'distinction','Cloud categories reconcile apparent contradiction.'),(51,49,'distinction','Common/uncommon wind reconciles contradiction.'),(53,52,'reply','Two distinct resolutions of curse versus benefit.'),(59,58,'qualification','Gentleness remains required despite scholarly hardness.')],[(37,42,'Identification of Yehoshua/Ben Beteira; pre-core context retained.','closed local unit'),(42,48,'Dew/wind mention and seasonal prayer errors.','closed'),(48,52,'Cloud/wind mention and withholding distinctions.','closed'),(52,57,'Benefits of weather and post-rain distinctions.','transition crosses segment 57'),(57,60,'Seed metaphor and scholar disposition.','start inside segment 57; closes before new report at 60')],['41 must not identify רבי יהושע בן בתירה as רבי יהודה בן בתירה.','52 prints רבי יהודה in the first alternative attribution and רב יהודה in the second; preserve both source surfaces rather than silently normalize.','50 חרפי/אפלי recorded without imposing unverified external gloss.','57 comprises weather continuation, lexical explanation, and a new scholar analogy: segment boundary alone is not a semantic boundary.','Whole-segment evidence is exact but may include surrounding clauses; paraphrases explicitly separate reviewer interpretation.'],'Next frozen probability block block_000010, Taanit 5a:10–5b:5; retrieve surrounding original source before extracting. Opening block not reread in this batch.')
