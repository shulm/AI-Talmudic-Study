"""Fail-closed mechanical validation supporting both baseline 1.0.0 and cumulative 1.1.0 checkpoints."""
import argparse
from collections import Counter
from pathlib import Path
import jsonschema
import pipeline as p


def load_data():
    return {t: p.rows(p.HERE / "data" / f"{t}.jsonl") for t in p.TABLES}


def validate(data, root=p.DEFAULT, check_source=True):
    has_v1_1 = (p.HERE / "schema_v1_1.json").exists() and any(
        r.get("schema_version") == "1.1.0" for rr in data.values() for r in rr
    )
    schema = p.read(p.HERE / ("schema_v1_1.json" if has_v1_1 else "schema_v1.json"))
    jsonschema.Draft202012Validator.check_schema(schema)
    ids = {}
    for table, records in data.items():
        v = jsonschema.Draft202012Validator(
            {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": "#/$defs/" + table}
        )
        for rec in records:
            v.validate(rec)
            assert rec["id"] not in ids, ("duplicate_id", rec["id"])
            ids[rec["id"]] = (table, rec)
    seg = {s["id"]: s for s in data["segments"]}
    contexts = p.rows(p.HERE / "context/segments.jsonl")
    assert not (set(seg) & {s["id"] for s in contexts}), "context overlap with processed segments"
    allseg = {**seg, **{s["id"]: s for s in contexts}}
    manifest = p.read(p.HERE / "source_manifest.json")
    meta = {m["title"]: m for m in manifest["tractates"]}
    if check_source:
        assert p.sha((root / manifest["source_toc_path"]).read_bytes()) == manifest["source_toc_sha256"]
        assert [n["title"] for n in p.toc_leaves(p.read(root / manifest["source_toc_path"]))] == list(meta)
        originals = {}
        for m in meta.values():
            assert p.sha((root / m["source_path"]).read_bytes()) == m["source_sha256"]
            assert p.sha((root / m["schema_path"]).read_bytes()) == m["schema_sha256"]
            originals[m["title"]] = p.read(root / m["source_path"])
        expected = {
            (w, i, j)
            for w, (lo, hi) in p.PILOTS.items()
            for i in range(lo, hi + 1)
            for j, _ in enumerate(originals[w]["text"][i])
        }
        if has_v1_1 and (p.HERE / "block_ledger.json").exists():
            ledger = p.read(p.HERE / "block_ledger.json")
            for blk in ledger["blocks"]:
                if blk.get("core_daf_range") and blk.get("tractate"):
                    import continuation as cont
                    s_daf, e_daf = blk["core_daf_range"].split("-")
                    lo_b, hi_b = cont.daf_to_page_index(s_daf), cont.daf_to_page_index(e_daf)
                    w = blk["tractate"]
                    for i in range(lo_b, hi_b + 1):
                        for j, _ in enumerate(originals[w]["text"][i]):
                            expected.add((w, i, j))
        assert {(s["tractate"], *s["source_index"]) for s in seg.values()} == expected, "coverage differs from source"
    for s in allseg.values():
        i, j = s["source_index"]
        assert s["ref"] == p.address(s["tractate"], i, j), "address offset"
        assert s["id"] == p.stable("seg", s["tractate"], p.VERSION, str(i), str(j)), "unstable source ID"
        assert p.sha(s["text"].encode()) == s["text_sha256"]
        assert s["source_sha256"] == meta[s["tractate"]]["source_sha256"]
        if check_source:
            assert s["text"] == originals[s["tractate"]]["text"][i][j], "source altered"
    assert len({s["ref"] for s in seg.values()}) == len(seg)
    coverage = Counter()
    groups = {g["id"]: g for g in data["sugyot"]}
    for g in groups.values():
        ss = [seg[i] for i in g["segment_ids"]]
        assert ss and len({s["tractate"] for s in ss}) == 1
        assert ss[0]["ref"] == g["start_ref"] and ss[-1]["ref"] == g["end_ref"]
        expected_ids = [
            s["id"]
            for s in sorted(
                (x for x in data["segments"] if x["tractate"] == g["tractate"]),
                key=lambda r: r["source_index"],
            )
            if ss[0]["source_index"] <= s["source_index"] <= ss[-1]["source_index"]
        ]
        assert expected_ids == g["segment_ids"], "noncontiguous sugya"
        if g["level"] == "primary":
            assert g["parent_id"] is None
            coverage.update(g["segment_ids"])
        else:
            assert g["parent_id"] in groups and set(g["segment_ids"]) <= set(groups[g["parent_id"]]["segment_ids"])
    assert set(coverage) == set(seg) and all(n == 1 for n in coverage.values()), "primary coverage gap or overlap"

    def link(value, table):
        assert value in ids and ids[value][0] == table, ("invalid link", value, table)

    related_sugya_segs = {}
    for rel in data["relations"]:
        if (
            rel.get("relation_type") == "related_topic"
            and rel.get("source_id") in groups
            and rel.get("target_id") in groups
        ):
            s_id, t_id = rel["source_id"], rel["target_id"]
            related_sugya_segs.setdefault(s_id, set()).update(groups[t_id]["segment_ids"])
            related_sugya_segs.setdefault(t_id, set()).update(groups[s_id]["segment_ids"])

    evidence_count = 0
    for table, rr in data.items():
        for r in rr:
            for e in r.get("evidence", []):
                s = allseg[e["segment_id"]]
                assert e["ref"] == s["ref"] and e["source_sha256"] == s["source_sha256"]
                assert 0 <= e["start_char"] < e["end_char"] <= len(s["text"])
                assert s["text"][e["start_char"] : e["end_char"]] == e["quote"], "quote provenance error"
                evidence_count += 1
            if table in ["statements", "questions", "positions"]:
                link(r["sugya_id"], "sugyot")
            if table == "statements":
                for k in ["speaker_id", "attributed_authority_id", "quoted_authority_id"]:
                    if r[k] is not None:
                        link(r[k], "scholars")
                for k in ["transmitter_ids", "speaker_candidates"]:
                    for value in r[k]:
                        link(value, "scholars")
                if r["speaker_candidates"]:
                    assert r["attributed_authority_id"] is None and r["attribution_status"] == "unresolved_alternatives"
                assert any(e["segment_id"] in groups[r["sugya_id"]]["segment_ids"] for e in r["evidence"])
                assert all(
                    e["segment_id"] in groups[r["sugya_id"]]["segment_ids"]
                    or e["segment_id"] in related_sugya_segs.get(r["sugya_id"], set())
                    or allseg[e["segment_id"]]["scope"] == "context_only"
                    for e in r["evidence"]
                )
            if table == "questions":
                for x in r["candidate_position_ids"]:
                    link(x, "positions")
            if table == "positions":
                link(r["statement_id"], "statements")
                link(r["question_id"], "questions")
                st = ids[r["statement_id"]][1]
                assert r["scholar_id"] == st["attributed_authority_id"] and r["status"] == st["position_status"]
                if r["scholar_id"]:
                    link(r["scholar_id"], "scholars")
            if table == "relations":
                endpoint = "sugyot" if r["relation_type"] == "related_topic" else "statements"
                link(r["source_id"], endpoint)
                link(r["target_id"], endpoint)
            if table == "review_queue":
                for x in r["target_ids"]:
                    assert x in ids
    covered = {e["segment_id"] for s in data["statements"] for e in s["evidence"]} & set(seg)
    pending = {
        i
        for r in data["review_queue"]
        if r["issue_type"] == "semantic_extraction_pending" and r["status"] == "open"
        for i in r["target_ids"]
    }
    assert set(seg) - covered <= pending
    return dict(
        schema_contract_version="1.1.0" if has_v1_1 else "1.0.0",
        mechanical_pass=True,
        records={t: len(rr) for t, rr in data.items()},
        processed_source_segments=len(seg),
        pilot_v1_segments=sum(s["scope"] == "pilot" for s in data["segments"]),
        continuation_core_segments=sum(s["scope"] == "core" for s in data["segments"]),
        context_only_segments=len(contexts),
        primary_sugyot=sum(g["level"] == "primary" for g in groups.values()),
        sub_sugyot=sum(g["level"] == "sub_sugya" for g in groups.values()),
        evidence_spans_checked=evidence_count,
        primary_coverage_segments=len(coverage),
        source_text_errors=0,
        reference_errors=0,
        duplicate_ids=0,
        uncovered_segments=0,
        segments_with_selected_statements=len(covered),
        segments_deferred_qa_extraction=len(pending),
        open_review_records=sum(r["status"] == "open" for r in data["review_queue"]),
        ml_eligible_records=0,
        human_expert_reviews=0,
        semantic_completeness_pass=False,
        expansion_gate_pass=False,
        provisional_segmentation_phase_active=has_v1_1,
        source_files_checked=37 if check_source else 0,
        scope_note="Provisional sugya segmentation continuation; historical full-semantics/ML gate remains false.",
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, default=p.DEFAULT)
    ap.add_argument("--public-only", action="store_true")
    a = ap.parse_args()
    data = load_data()
    report = validate(data, a.source_root, not a.public_only)
    if not a.public_only:
        p.write(p.HERE / "qa_report.json", report)
        if report["schema_contract_version"] == "1.0.0":
            progress = []
            for m in p.read(p.HERE / "source_manifest.json")["tractates"]:
                w = m["title"]
                sg = {s["id"] for s in data["segments"] if s["tractate"] == w}
                gg = {s["id"] for s in data["sugyot"] if s["tractate"] == w}
                progress.append(
                    dict(
                        ordinal=m["ordinal"],
                        tractate=w,
                        source_segments=m["source_segments"],
                        pilot_segments=len(sg),
                        primary_sugyot=sum(g["id"] in gg and g["level"] == "primary" for g in data["sugyot"]),
                        statements=sum(s["sugya_id"] in gg for s in data["statements"]),
                        questions=sum(s["sugya_id"] in gg for s in data["questions"]),
                        positions=sum(s["sugya_id"] in gg for s in data["positions"]),
                        uncertain_records=sum(
                            any(e["segment_id"] in sg for e in r["evidence"]) for r in data["review_queue"]
                        ),
                        status="pilot_partial_semantics" if sg else "inventory_only",
                        completed_masechet=False,
                    )
                )
            p.write(p.HERE / "progress_manifest.json", dict(schema_version="1.0.0", completed_masechtot=0, tractates=progress))
    print(report)


if __name__ == "__main__":
    main()
