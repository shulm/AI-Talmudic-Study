import json,pathlib,hashlib,collections
HERE=pathlib.Path(__file__).resolve().parent
INPUT=HERE.parent/"rosh_hashanah/review_delta_20261127"
PRIOR=HERE.parent/"review_correction_verification_20261126/RH_VERDICT.json"
JOB=pathlib.Path("F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah")
def load(p):return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def canonical(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
r=load(INPUT/"RESPONSE.json");proposal=load(INPUT/"proposal.json");assert sha(INPUT/"proposal.json")==r["proposal_sha256"]
assert r["snapshot_sha256"]=="70289b2e7db5c109fda8a29821a7a52a08d0e08d1dcce54c1811c223a2a2958c"
assert sha(PRIOR)==r["review_verdict_sha256"]
def snapshot(digest):
 p=JOB/"snapshots"/(digest+".json");assert sha(p)==digest;return load(p)
s=snapshot(r["snapshot_sha256"]);b=snapshot(r["base_snapshot"]);old=snapshot(r["reviewed_prior_snapshot"])
rows={x["id"]:x for x in s["records"]};base={x["id"]:x for x in b["records"]};prior={x["id"]:x for x in old["records"]}
assert len(proposal["records"])==1
new=proposal["records"][0];assert set(rows)-set(base)=={new["id"]}
for k,v in new.items():assert rows[new["id"]][k]==v
for i,x in base.items():
 y=rows[i]
 if i==new["supersedes"]:
  assert y["release_state"]=="superseded";x=dict(x);y=dict(y);x.pop("release_state");y.pop("release_state")
 assert x==y
priorids=[x["record_id"] for x in load(PRIOR)["new_row_reviews"]];assert len(priorids)==72
for i in priorids:
 x=prior[i];y=rows[i]
 if i==new["supersedes"]:
  x=dict(x);y=dict(y);x.pop("release_state");y.pop("release_state")
 assert x==y
assert rows[r["retained_support_edge"]]==prior[r["retained_support_edge"]]
sp=pathlib.Path("F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Moed/Rosh Hashanah/Hebrew/Wikisource Talmud Bavli.json")
assert sha(sp)==proposal["source_sha256"]
source=load(sp)["text"];inv={x["id"]:x for x in load(JOB/"source_inventory.json")}
evidence=[]
for e in new["evidence"]:
 x=inv[e["segment_id"]];i,j=x["source_index"];assert source[i][j][e["start_char"]:e["end_char"]]==e["quote"];evidence.append(dict(e,ref=x["ref"],source_index=x["source_index"]))
for key in ["source_id","target_id"]:assert rows[new["content"][key]]["release_state"]=="valid"
oldcov={(x["segment_id"],x["layer"]) for x in b["coverage"] if x["extraction_state"]=="completed"};newcov={(x["segment_id"],x["layer"]) for x in s["coverage"] if x["extraction_state"]=="completed"};assert oldcov==newcov
for cell in s["coverage"]:
 for i in cell["record_ids"]:assert rows[i]["release_state"]=="valid"
checks=dict(snapshot_sha256=r["snapshot_sha256"],base_snapshot_sha256=r["base_snapshot"],prior_reviewed_snapshot_sha256=r["reviewed_prior_snapshot"],proposal_sha256=r["proposal_sha256"],source_sha256=sha(sp),new_rows=1,new_evidence_spans_verified=len(evidence),prior_bounded_rows_checked=72,prior_bounded_rows_byte_content_unchanged=71,prior_bounded_row_status_only_change=1,all_other_base_records_unchanged=True,correct_last_to_eighth_support_unchanged=True,active_endpoints_and_coverage_references_valid=True,coverage_added_by_delta=0,completed_per_layer=dict(collections.Counter(l for _,l in newcov)),newer_batches010_011_semantically_reviewed=False)
if __name__=="__main__":print(json.dumps(checks,indent=2))
