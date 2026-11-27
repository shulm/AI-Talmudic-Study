import json,pathlib,hashlib,collections
HERE=pathlib.Path(__file__).resolve().parent
INPUT=HERE.parent/"eruvin/review_correction_20261126"
JOB=pathlib.Path("F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin")
SHA="6d0d2c6635723481dec4f853702b48908057bbb439c18c8734000dd9f0766680"
def load(p):return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def canon(o):return hashlib.sha256(json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
r=load(INPUT/"RESPONSE.json");p=load(INPUT/"proposal.json")
assert sha(INPUT/"RESPONSE.json")=="b37eeb7b0c00dd72bc95d1d7a29e0f41aad83a07d3b1456cfdf13c1743d24d96"
for name,key in [("proposal.json","proposal_sha256"),("reader_frozen.json","reader_sha256"),("comparison_frozen.json","comparison_sha256"),("verdict_frozen.json","verdict_sha256")]:assert sha(INPUT/name)==r[key]
sp=JOB/"snapshots"/(SHA+".json");assert sha(sp)==SHA
bp=JOB/"snapshots"/(r["base_snapshot"]+".json");assert sha(bp)==r["base_snapshot"]
s=load(sp);b=load(bp);rows={x["id"]:x for x in s["records"]};old={x["id"]:x for x in b["records"]}
sourcepath=pathlib.Path("F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Moed/Eruvin/Hebrew/Wikisource Talmud Bavli.json")
assert sha(sourcepath)==p["source_sha256"]
raw=load(sourcepath)["text"];inventory=load(JOB/"source_inventory.json");segs={x["id"]:x for x in inventory};refs={x["ref"]:x for x in inventory}
for x in inventory:
 i,j=x["source_index"];assert x["text"]==raw[i][j];assert hashlib.sha256(raw[i][j].encode()).hexdigest()==x["text_sha256"]
def evidence(e):
 x=segs[e["segment_id"]];i,j=x["source_index"];assert raw[i][j][e["start_char"]:e["end_char"]]==e["quote"];assert 0<=e["start_char"]<e["end_char"]<=len(raw[i][j])
 return dict(e,ref=x["ref"],source_index=x["source_index"])
assert len(p["records"])==4
assert set(rows)-set(old)=={x["id"] for x in p["records"]}
superseded={x["supersedes"] for x in p["records"] if "supersedes" in x};assert len(superseded)==3
for x in p["records"]:
 for k,v in x.items():assert rows[x["id"]][k]==v
for key in old:
 before=dict(old[key]);after=dict(rows[key]);before.pop("release_state",None);after.pop("release_state",None);assert before==after
for key in superseded:assert rows[key]["release_state"]=="superseded"
count=0
for x in rows.values():
 for e in x["evidence"]:evidence(e);count+=1
 for link in x.get("links",[]):assert link in rows
newspans=[evidence(e) for x in p["records"] for e in x["evidence"]]
correction="er.objections.001.claims.form.rav.correction"
assert rows[correction]==old[correction]
for key in ["er.review20261126.er.opening.001.width.form","er.review20261126.er.opening.001.p.width.form"]:assert correction in rows[key]["links"]
for x in p["records"]:
 for f in ["claim_id","source_id","target_id"]:
  if x["content"].get(f):assert rows[x["content"][f]]["release_state"]=="valid"
for c in s["coverage"]:
 for i in c["record_ids"]:assert i in rows and rows[i]["release_state"]=="valid"
oldcov={(c["segment_id"],c["layer"]) for c in b["coverage"] if c["extraction_state"]=="completed"};newcov={(c["segment_id"],c["layer"]) for c in s["coverage"] if c["extraction_state"]=="completed"};assert oldcov==newcov
checks=dict(snapshot_sha256=SHA,source_sha256=sha(sourcepath),proposal_sha256=sha(INPUT/"proposal.json"),inventory_segments_verified=len(inventory),snapshot_records=len(rows),snapshot_evidence_spans_verified=count,new_rows=4,new_evidence_spans_verified=len(newspans),superseded_rows_preserved=3,original_correction_unchanged=True,opening_claim_and_position_link_correction=True,active_typed_dependencies_valid=True,coverage_references_active=True,coverage_unchanged=True,completed_per_layer=dict(collections.Counter(l for _,l in newcov)),source_and_frozen_artifact_hashes_verified=True)
if __name__=="__main__":print(json.dumps(checks,ensure_ascii=False,indent=2))
