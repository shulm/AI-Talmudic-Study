"""Documented provisional contract, explicitly authorized because attachment was absent."""
import pipeline as p
S={'type':'string'};N={'type':['string','null']};A={'type':'array','items':S}
E={'type':'array','minItems':1,'items':{'type':'object','additionalProperties':False,'required':['segment_id','ref','start_char','end_char','quote','source_sha256'],'properties':{'segment_id':S,'ref':S,'start_char':{'type':'integer','minimum':0},'end_char':{'type':'integer','minimum':0},'quote':S,'source_sha256':{'type':'string','pattern':'^[a-f0-9]{64}$'}}}}
def obj(properties):return dict(type='object',additionalProperties=False,required=list(properties),properties=properties)
def record(extra):return obj(dict(schema_version={'const':'1.0.0'},id=S,review_status={'const':'ai_provisional'},ml_eligible={'const':False},**extra))
def make():
    defs={
    'segments':obj(dict(schema_version={'const':'1.0.0'},id=S,tractate=S,ref=S,source_index={'type':'array','prefixItems':[{'type':'integer','minimum':0},{'type':'integer','minimum':0}],'minItems':2,'maxItems':2},text=S,text_sha256=S,source_sha256=S,version_title=S,scope={'enum':['pilot','context_only']})),
    'sugyot':record(dict(authoring_key=S,tractate=S,title_he=S,level={'enum':['primary','sub_sugya']},parent_id=N,segment_ids=A,start_ref=S,end_ref=S,boundary_status={'enum':['provisional','open_left','open_right','open_both']},boundary_rationale=S,conditions=A,family_id=S,family_status=S,annotation_completeness={'const':'selected_claims_only'},evidence=E)),
    'scholars':record(dict(name_he=S,aliases=A,external_authority_id=N,identity_status={'const':'textual_label_only_person_disambiguation_pending'},evidence=E)),
    'statements':record(dict(authoring_key=S,sugya_id=S,role=S,summary_he=S,summary_origin={'const':'editorial_paraphrase'},source_reasoning={'enum':['source_explicit','gemara_reconstruction']},narrator={'const':'anonymous_talmudic_redactor'},speaker_id=N,attributed_authority_id=N,transmitter_ids=A,quoted_authority_id=N,attribution_status={'enum':['unresolved_alternatives','explicit_name','anonymous_or_continuation']},speaker_candidates=A,position_status={'enum':['asserted','conditional','rejected','retracted','reconciled','unresolved']},evidence=E)),
    'questions':record(dict(sugya_id=S,question_he=S,origin={'enum':['editorial_reconstruction','source_explicit_question_paraphrased']},conditions=A,candidate_position_ids=A,evidence=E)),
    'positions':record(dict(sugya_id=S,question_id=S,statement_id=S,scholar_id=N,scholar_candidates=A,proposition_he=S,status={'enum':['asserted','conditional','rejected','retracted','reconciled','unresolved']},conditions=A,attribution_mode={'enum':['unresolved','transmitted','direct_named']},historical_observation_status={'const':'text_attested_provisional_not_behavioral_observation'},evidence=E)),
    'relations':record(dict(source_id=S,target_id=S,relation_type={'enum':['answers','objects_to','rejects','alternative_version_of','alternative_to','qualifies','reframes','leaves_unresolved','supports','related_topic']},origin={'const':'editorial_relation_supported_by_source'},evidence=E)),
    'review_queue':record(dict(target_ids=A,issue_type={'enum':['semantic_extraction_pending','boundary_and_family_review','unresolved_attribution']},severity={'const':'blocks_ml'},status={'const':'open'},description_he=S,evidence=E))}
    schema={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'urn:ai-talmudic-study:bavli-sugya:1.0.0','title':'Provisional Bavli pilot contract; not the missing attachment','$defs':defs,'oneOf':[{'$ref':'#/$defs/'+t} for t in p.TABLES]}
    p.write(p.HERE/'schema_v1.json',schema)
if __name__=='__main__':make()
