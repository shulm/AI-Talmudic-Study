from verify_queue007_assigned import *
x,r,s,segs,runner=load('sotah')
assert x['compared_core_refs']==['Sotah 4a:12']
records={v['id']:v for v in s['records'] if v['release_state']=='valid'}
ids=['sot.open.'+z for z in ['c169','p169','a169','u169','e169','e169b','c168','q169','s21']]
findings=[v for v in r['findings'] if any(e['ref']=='Sotah 4a:12' for e in v['evidence'])]
assert len(findings)==2
x.update(artifact_kind='independent_exact_version_comparison_v2',semantic_verdict='ACCEPT_PARTIAL_WITH_EXCEPTIONS',omission_count=0)
x['bindings']['semantic_script']=bind(Path(__file__))
x['claim_comparison']=[{'independent_finding':f,'producer_record_ids':['sot.open.c169','sot.open.p169','sot.open.a169'],'assessment':'Content, Abaye attribution and reconciliation status supported. The two clauses constitute one paired distinction, not omitted content merely because the reader split them. No conflicting branch conditions. Exact wind-motion boundary remains unresolved at4a13; producer position explicitly preserves that limit.'} for f in findings]
x['source_context']=[v for v in segs.values() if v['ref'].startswith('Sotah 4a:') or v['ref'] in ['Sotah 4b:1','Sotah 4b:2','Sotah 4b:3']]
x['producer_records']=[{'sha256':hashlib.sha256(runner.encoded(records[i])).hexdigest(),'record':records[i]} for i in ids]
x['relation_comparison']=[{'record_id':'sot.open.e169','assessment':'Answer to q169 resolves apparent contradictory attribution of palm timings by distinguishing the meanings; question evidence4a11 is explicit local contradiction.'},{'record_id':'sot.open.e169b','assessment':'Distinction correctly targets c168, the hypothetical equivalence assumption, not a named maintained ruling.'}]
x['reader_corrections']=[]; x['producer_issues']=[]
x['exceptions']=['Only one completed sampled core examined;29 frozen sampled cores unprocessed.','One producer paired distinction versus two reader findings is not an omission.','Context4a13 unresolved wind motion is not extra reviewed core or a resolved practical rule.','No complete comparable scholar-choice answer inventory certified.']
x['scope_note']='Nonblind comparison of frozen source-first findings at Sotah4a12 only, with original4a1–4b3 context. All independent questions, answer sets and relations are outside completed core. Two producer context relations examined to check the core answer and distinction. No other-lane reader inspected.'
matrix={'unique_core_segments_compared':1,'probability_core_segments_compared':1,'endpoint_core_segments_compared':0,'overlap_core_segments':0,'independently_read_core_segments':30,'unprocessed_independent_core_refs':x['unprocessed_core_refs'],'producer_completed_per_layer':x['completed_counts_by_layer'],'source_segments_total':len(segs),'risk_reviewed':0,'independent_core_denominators':{'independent_completed_core_finding_units':2,'atomic_claim_denominator_certified':False,'raw_content_missing_findings':0,'core_anchored_question_groups':0,'core_anchored_answer_sets':0,'core_anchored_relations':0}}
x['layer_matrix']=matrix
def publish(p,o):
 with p.open('x',encoding='utf8',newline='\n') as f: json.dump(o,f,ensure_ascii=False,sort_keys=True,indent=2);f.write('\n')
 return bind(p)
c=publish(BASE/'comparisons/sotah_batch001_exact_version.json',x)
v={'verdict':'ACCEPT_PARTIAL_WITH_EXCEPTIONS','bindings':x['bindings'],'comparison':c,'scope':x['scope_note'],'layer_matrix':matrix,'required_changes':[],'reader_corrections':[],'exceptions':x['exceptions'],'tractate_accepted':False,'full_review_receipt':False,'human_certification':False,'admission_owner':'global coordinator','task_eligibility':{k:False for k in ['argument_extraction','attribution','ml','qa','retrieval','scholar_choice','segmentation']},'remaining':'Continue frozen independent sample and production; no inheritance to later snapshots.'}
print(json.dumps({'comparison':c,'verdict':publish(BASE/'verdicts/sotah_batch001_v2_verdict.json',v)}))
