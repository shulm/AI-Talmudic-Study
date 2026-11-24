"""Serialize curated source readings; never infer attribution from nearby names."""
import annotation_initial as a
import annotation_completion as completion
import pipeline as p

def compile_data():
    segments=p.rows(p.HERE/'data/segments.jsonl');lookup={s['ref']:s for s in segments+p.rows(p.HERE/'context/segments.jsonl')};order={s['id']:i for i,s in enumerate(segments)}
    revisions=p.read(p.HERE/'revisions.json')
    def full(ref):return ('Berakhot '+ref[1:]) if ref.startswith('B') else ('Bava Metzia '+ref[1:])
    def ev(ref):
        s=lookup[ref];return dict(segment_id=s['id'],ref=ref,start_char=0,end_char=len(s['text']),quote=s['text'],source_sha256=s['source_sha256'])
    def between(work,lo,hi):
        left=order[lookup[work+' '+lo]['id']];right=order[lookup[work+' '+hi]['id']]
        return [s for s in segments if s['tractate']==work and left<=order[s['id']]<=right]
    base=dict(schema_version='1.0.0',review_status='ai_provisional',ml_eligible=False)
    data={t:[] for t in p.TABLES if t!='segments'};gids={};owner={};questions={}
    for key,work,lo,hi,title,question,conditions in a.GROUPS:
        covered=between(work,lo,hi);gid=p.stable('sug',key);gids[key]=gid
        for s in covered:assert s['id'] not in owner;owner[s['id']]=gid
        boundary='open_left' if key=='M01' else 'open_right' if key in ['B24','M05'] else 'provisional'
        data['sugyot'].append(dict(**base,id=gid,authoring_key=key,tractate=work,title_he=title,level='primary',parent_id=None,segment_ids=[s['id'] for s in covered],start_ref=covered[0]['ref'],end_ref=covered[-1]['ref'],boundary_status=boundary,boundary_rationale='AI topic boundary from sequential discussion, not a daf break; see initial reading and review.',conditions=[conditions],family_id=p.stable('fam',key),family_status='provisional_single_occurrence_not_split_ready',annotation_completeness='selected_claims_only',evidence=[ev(covered[0]['ref']),ev(covered[-1]['ref'])]))
        qid=p.stable('que',key,'main');questions[gid]=qid
        data['questions'].append(dict(**base,id=qid,sugya_id=gid,question_he=question,origin='editorial_reconstruction',conditions=[conditions],candidate_position_ids=[],evidence=[ev(covered[0]['ref'])]))
    assert set(owner)=={s['id'] for s in segments}
    for key,parent,lo,hi,title in a.SUBGROUPS:
        ss=between('Bava Metzia',lo,hi)
        data['sugyot'].append(dict(**base,id=p.stable('sug',key),authoring_key=key,tractate='Bava Metzia',title_he=title,level='sub_sugya',parent_id=gids[parent],segment_ids=[s['id'] for s in ss],start_ref=ss[0]['ref'],end_ref=ss[-1]['ref'],boundary_status='provisional',boundary_rationale='Argument stage within continuous parent; not additional coverage.',conditions=[],family_id=p.stable('fam',parent),family_status='provisional_single_occurrence_not_split_ready',annotation_completeness='selected_claims_only',evidence=[ev(ss[0]['ref']),ev(ss[-1]['ref'])]))
    names={};statements={};claimkeys={};covered=set()
    def scholar(name,evidence):
        if name not in names:
            sid=p.stable('sch',name);names[name]=sid
            data['scholars'].append(dict(**base,id=sid,name_he=name,aliases=[],external_authority_id=None,identity_status='textual_label_only_person_disambiguation_pending',evidence=[evidence]))
        return names[name]
    for key,short,role,authority,summary,status,transmitters,candidates in a.CLAIMS+completion.CLAIMS:
        for change in revisions['changes']:
            if change.get('key')==key:
                if change['field']=='authority':assert authority==change['old'];authority=change['new']
                elif change['field']=='position_status':assert status==change['old'];status=change['new']
                elif change['field']=='summary_he':assert summary==change['old'];summary=change['new']
        ref=full(short);e=ev(ref);gid=owner[e['segment_id']];sid=p.stable('stm',key);covered.add(e['segment_id'])
        auth=scholar(authority,e) if authority else None;chain=[scholar(n,e) for n in transmitters];poss=[scholar(n,e) for n in candidates]
        rec=dict(**base,id=sid,authoring_key=key,sugya_id=gid,role=role,summary_he=summary,summary_origin='editorial_paraphrase',source_reasoning='gemara_reconstruction' if role=='reconstruction' else 'source_explicit',narrator='anonymous_talmudic_redactor',speaker_id=chain[0] if chain else auth,attributed_authority_id=auth,transmitter_ids=chain,quoted_authority_id=auth if chain else None,attribution_status='unresolved_alternatives' if poss else 'explicit_name' if auth else 'anonymous_or_continuation',speaker_candidates=poss,position_status=status,evidence=[e])
        rec['evidence'] += [ev(r) for r in revisions['context_evidence'].get(key,[])]
        data['statements'].append(rec);statements[key]=rec;claimkeys[key]=sid
        if role=='question':
            qid=p.stable('que',key);data['questions'].append(dict(**base,id=qid,sugya_id=gid,question_he=summary,origin='source_explicit_question_paraphrased',conditions=[],candidate_position_ids=[],evidence=[e]))
        if (auth or poss) and role not in ['question','speaker_introduction','structural_marker','mnemonic','argument_marker','lemma']:
            pid=p.stable('pos',key);data['positions'].append(dict(**base,id=pid,sugya_id=gid,question_id=questions[gid],statement_id=sid,scholar_id=auth,scholar_candidates=poss,proposition_he=summary,status=status,conditions=next(g['conditions'] for g in data['sugyot'] if g['id']==gid),attribution_mode='unresolved' if poss else 'transmitted' if chain else 'direct_named',historical_observation_status='text_attested_provisional_not_behavioral_observation',evidence=[e]))
            next(q for q in data['questions'] if q['id']==questions[gid])['candidate_position_ids'].append(pid)
    for source,kind,target in a.EDGES+revisions.get('additional_edges',[]):
        for change in revisions['changes']:
            if change.get('edge')==[source,kind,target]:source,kind,target=change['replacement']
        data['relations'].append(dict(**base,id=p.stable('rel',source,kind,target),source_id=claimkeys[source],target_id=claimkeys[target],relation_type=kind,origin='editorial_relation_supported_by_source',evidence=statements[source]['evidence']+statements[target]['evidence']))
    # Related topics are not certified parallel families or duplicate decisions.
    for left,right in [('B01','B14'),('B05','B08'),('B18','B20'),('B22','B23')]:
        gl=next(g for g in data['sugyot'] if g['id']==gids[left]);gr=next(g for g in data['sugyot'] if g['id']==gids[right])
        data['relations'].append(dict(**base,id=p.stable('rel',left,'related_topic',right),source_id=gids[left],target_id=gids[right],relation_type='related_topic',origin='editorial_relation_supported_by_source',evidence=[gl['evidence'][0],gr['evidence'][0]]))
    # All extraction omissions remain visible, not fictional anonymous claims.
    for s in segments:
        if s['id'] not in covered:
            data['review_queue'].append(dict(**base,id=p.stable('rev',s['id'],'extraction'),target_ids=[s['id']],issue_type='semantic_extraction_pending',severity='blocks_ml',status='open',description_he='הקטע נקרא ומשויך לסוגיה; פירוק לטענות אטומיות וייחוסים טרם הושלם.',evidence=[ev(s['ref'])]))
    for g in data['sugyot']:
        if g['level']=='primary':
            data['review_queue'].append(dict(**base,id=p.stable('rev',g['id'],'boundary'),target_ids=[g['id']],issue_type='boundary_and_family_review',severity='blocks_ml',status='open',description_he='נדרש עיון בגבול, במקבילות ובפירוק טענות מורכבות. אין אישור מומחה, אישור השוואת חלופות או היתר לפיצול אימון ובדיקה.',evidence=g['evidence']))
    for s in data['statements']:
        if s['speaker_candidates']:
            data['review_queue'].append(dict(**base,id=p.stable('rev',s['id'],'attribution'),target_ids=[s['id']],issue_type='unresolved_attribution',severity='blocks_ml',status='open',description_he='אין לשייך חלופה על סמך סדר השמות; הייחוס נשאר בלתי מוכרע.',evidence=s['evidence']))
    for table,rr in data.items():p.jsonl(p.HERE/'data'/f'{table}.jsonl',rr)
    p.write(p.HERE/'annotation_manifest.json',dict(schema_version='1.0.0',annotation_source='annotation_initial.py',annotation_sha256=p.sha((p.HERE/'annotation_initial.py').read_bytes()),revision_inputs={f:p.sha((p.HERE/f).read_bytes()) for f in ['annotation_completion.py','revisions.json']},annotator='current Codex model; Gemini substitution explicitly authorized by user',model_identifier='not exposed as an exact API model identifier',settings='interactive current session; temperature and token accounting not exposed',api_calls=0,incremental_paid_api_cost=0,token_usage=None,token_usage_note='No per-task usage meter available; not estimated or represented as zero.',read_ranges=['Berakhot 2a–3a','Berakhot 3a–4a','Berakhot 4a–5b','Bava Metzia 20b–21b','Bava Metzia 21b–23a'],all_semantics_provisional=True,counts={t:len(rr) for t,rr in data.items()}))
    print({t:len(rr) for t,rr in data.items()})
if __name__=='__main__':compile_data()
