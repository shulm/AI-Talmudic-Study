from verify_queue007_assigned import *
x,r,s,segs,runner=load('avodah_zarah'); core=set(x['compared_core_refs']); assert len(core)==10
records={v['id']:v for v in s['records'] if v['release_state']=='valid'}
mapping={1:['c01a','c01b','c01c','c01d'],2:['c02','c03'],3:['c04'],4:['c05','c06','c07'],5:['c08'],6:['c09'],7:['c10'],8:['c11'],9:['c12','c13','c14'],10:['c15'],11:['c16','c17'],12:['c18','c19'],13:['c21','c22','c23'],14:['c26'],15:['c24','c25']}
findings=[f for f in r['findings'] if any(e['ref'] in core for e in f['evidence'])];assert len(findings)==15
sid={v['id'] for v in segs.values() if v['ref'] in core}
selected=[v for v in records.values() if any(e['segment_id'] in sid for e in v['evidence'])]
cc=[]
for f in findings:
 n=int(f['id'].split('c')[-1]); ids=['az.'+i for i in mapping[n]]
 ids+= [v['id'] for v in selected if v['layer']=='positions' and v['content']['claim_id'] in ids]
 note='Source content, conditions and local status represented; attribution checked against original.'
 if n==1:note='Reader bundles all transaction types; producer separates four paired categories with three-day restriction. Granularity difference is not missing content; full atomic retrievability is not certified.'
 if n==2:note='Reader omits inherited festival restriction from conditions; producer retains before-festival condition and separate rationale. Three days inherited from Mishnah, not unlimited collection permission.'
 if n==4:note='Both variants and unresolved Rav/Shmuel assignment preserved. Anonymous appraisal that neither is mistaken is separated from named candidate holders; neither may be assigned by name order.'
 if n==6:note='Initial proof is explicitly rejected, with replacement at2a6; not an endorsed proof.'
 if n==9:note='Anonymous objection and quoted R. Yehoshua ben Levi exposition are separated by producer. Reader compresses these voices; objection must not be silently attributed to the named authority.'
 if n==11:note='Alternative homilist attribution retained in az.a12; divine speech holder in c17/p11 is embedded in that homily, not a competing attribution. Torah engagement condition retained.'
 cc.append({'independent_finding':f,'producer_record_ids':ids,'assessment':note})
x.update(artifact_kind='independent_exact_version_comparison_v2',semantic_verdict='ACCEPT_PARTIAL_WITH_EXCEPTIONS',omission_count=0)
x['bindings']['semantic_script']=bind(Path(__file__))
x['claim_comparison']=cc
x['question_comparison']=[{'independent_question':r['questions'][0],'producer_ids':['az.q04','az.c12','az.c13','az.c14','az.c15'],'assessment':'Exact verse-reference question answered by Israel referent, supported by RYBL; replacement proof is a distinct correction, not a competing answer about the same verse.'}]
x['answer_sets']=[a for a in r['answer_sets'] if a['question_id']=='avodah_zarah.q001']
x['relation_comparison']=[{'independent_relation':a,'producer_ids':ids,'assessment':note} for a,ids,note in zip(r['relations'][:3],[['az.e04'],['az.e10','az.e11'],['az.e13']],['Objection to Rabbi Judah permission retained.','Anonymous objection plus quoted support decomposes reader composite; rejected-proof target correct.','Corrects the initial proof, not the unresolved identity of variant holder.'])]
x['producer_records']=[{'sha256':hashlib.sha256(runner.encoded(v)).hexdigest(),'record':v} for v in selected]
x['source_context']=[v for v in segs.values() if v['ref'].split()[2].split(':')[0] in ['2a','2b','3a','6a','6b','7a']]
x['reader_corrections']=[{'id':'AZ-READER-SCOPE','finding':'c002 inherits three-day pre-festival context despite empty conditions. c009 compresses anonymous objection and RYBL proof; distinguish speech roles. c011 lists alternative homilists while producer separates homilist from divine quoted speaker. Preserve original; these are refinements, not producer omissions.'}]
x['producer_issues']=[]
x['exceptions']=['Only10 opening-check cores;20 probability cores unprocessed.','Bundled reader units are not a certified atomic denominator; no claim of exhaustive production review.','Opening Mishnah rules remain locally attributed.6a13 confirms three days exclusive of festival;6b5 restricts transaction cases;6b7–15 distinguishes direction/rationales;6b16–7a2 preserves loan-type qualification and ruling for RYBK. No final practical-law admission from opening scope.','Candidate answer inventories do not grant scholar-choice eligibility; none alone would not establish a source omission.']
x['scope_note']='Exact10 completed opening cores2a1–2b2 only. Original relevant continuation read through homily3a and transactional analysis6a–7a; context contributes no extra core. No alternative-lane reader inspected.'
matrix={'unique_core_segments_compared':10,'probability_core_segments_compared':0,'endpoint_core_segments_compared':10,'overlap_core_segments':0,'independently_read_core_segments':30,'unprocessed_independent_core_refs':x['unprocessed_core_refs'],'producer_completed_per_layer':x['completed_counts_by_layer'],'source_segments_total':len(segs),'risk_reviewed':0,'independent_core_denominators':{'independent_completed_core_finding_units':15,'atomic_claim_denominator_certified':False,'raw_content_missing_findings':0,'core_anchored_question_groups':1,'core_anchored_answer_sets':1,'core_anchored_relations':3}}
x['layer_matrix']=matrix
def publish(p,o):
 with p.open('x',encoding='utf8',newline='\n') as f: json.dump(o,f,ensure_ascii=False,sort_keys=True,indent=2);f.write('\n')
 return bind(p)
c=publish(BASE/'comparisons/avodah_zarah_batch001_exact_version.json',x)
v={'verdict':x['semantic_verdict'],'bindings':x['bindings'],'comparison':c,'scope':x['scope_note'],'layer_matrix':matrix,'required_changes':[],'reader_corrections':x['reader_corrections'],'exceptions':x['exceptions'],'tractate_accepted':False,'full_review_receipt':False,'human_certification':False,'admission_owner':'global coordinator','task_eligibility':{k:False for k in ['argument_extraction','attribution','ml','qa','retrieval','scholar_choice','segmentation']},'remaining':'Continue frozen independent sample and production; no inheritance to later snapshots.'}
print(json.dumps({'comparison':c,'verdict':publish(BASE/'verdicts/avodah_zarah_batch001_v2_verdict.json',v)}))
