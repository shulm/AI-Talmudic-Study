import json,pathlib,hashlib,copy
B=pathlib.Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
def rd(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def freeze(name,x):
 p=B/name;b=(json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
 if p.exists():assert p.read_bytes()==b
 else:p.write_bytes(b)
 side=p.with_name(p.name+'.sha256');sb=(sha(b)+'  '+p.name+'\n').encode()
 if side.exists():assert side.read_bytes()==sb
 else:side.write_bytes(sb)
 return {'path':str(p),'sha256':sha(b)}
c=rd(B/'comparison.json'); v=rd(B/'v2_verdict.json'); f=next(x for x in c['findings'] if x['id']=='TA101-09')
f['reader_records']=[c['exact_reader_record_inventory'][x] for x in ['ta101.attributions.0091','ta101.positions.0059','ta101.positions.0060']]
c['revision']={'supersedes_comparison_sha256':sha((B/'comparison.json').read_bytes()),'reason':'Correct auxiliary record IDs for unresolved TA101-09: .0058 referred to ki senses; intended inherited baraita positions are .0059 (both return) and .0060 (Moses death). No semantic finding, scope or counts changed. Originals retained.'}
cb=freeze('comparison_revision2.json',c);v['comparison']=cb;v['revision']=c['revision']; vb=freeze('v2_verdict_revision2.json',v)
checks=rd(B/'comparison_validation.json');checks['comparison_sha256']=cb['sha256'];checks['revision_auxiliary_reference_check']='PASS: TA101-09 positions .0059/.0060 refer to claims .0069/.0070'
assert f['reader_records'][1]['content']['claim_id']=='ta101.claims.0069'
assert f['reader_records'][2]['content']['claim_id']=='ta101.claims.0070'
freeze('comparison_validation_revision2.json',checks)
freeze('reading_helper_verify_only_receipt.json',{'status':'PASS_READ_ONLY','command':'python -X utf8 inherited/l04_ta101_source_capture040/build_reading.py --verify-only','records':503,'evidence_intervals':524,'core_segments':30,'core_layer_cells':240,'context_segments':4,'context_layer_cells':32,'limitations':'Original helper does not enforce production open_tails compatibility. See separately preserved validation failure and diagnostic adapter.'})
# Sidecars bind all deliverables including source-writing/verification helpers; never overwrite differing bytes.
for p in sorted(B.iterdir()):
 if p.is_file() and p.suffix!='.sha256' and p.name!='FINAL_RECEIPT.json':
  sb=(sha(p.read_bytes())+'  '+p.name+'\n').encode(); side=p.with_name(p.name+'.sha256')
  if side.exists():assert side.read_bytes()==sb
  else:side.write_bytes(sb)
files=[{'path':str(p),'sha256':sha(p.read_bytes())} for p in sorted(B.iterdir()) if p.is_file() and not p.name.startswith('FINAL_RECEIPT')]
receipt={'status':'FROZEN_REWORK_TARGETED','effective_comparison':cb,'effective_v2_verdict':vb,'validation':{'path':str(B/'validation.json'),'sha256':sha((B/'validation.json').read_bytes())},'comparison_validation':{'path':str(B/'comparison_validation_revision2.json'),'sha256':sha((B/'comparison_validation_revision2.json').read_bytes())},'files':files,'source_reader_claims':81,'core_refs_compared':30,'context_refs_compared':4,'production_changes':0,'eligibility_changes':0,'new_window_credit':0,'chronology':'Pins before semantic inspection; replay after semantic inspection before initial freeze; one auxiliary reader-ID erratum frozen in revision2 after initial freeze. Original artifacts preserved.','finding_summary':'One shared mistranslation, three producer speaker-layer omissions, one producer relation omission. Reader errors, scope uncertainties, reasonable granularity and reader-to-production tail-adapter failure separately recorded.'}
print(freeze('FINAL_RECEIPT.json',receipt));print(cb);print(vb)
