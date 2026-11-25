"""Comprehensive continuation safety tests verifying all 6 required checkpoint invariants."""
from __future__ import annotations

import copy
import json
import shutil
import tempfile
from pathlib import Path

import pipeline as p
import make_schema_v1_1
import continuation as c


def _copy_baseline_checkpoint(src_dir: Path, dst_dir: Path) -> None:
    files = [
        "source_manifest.json",
        "schema_v1.json",
        "progress_manifest.json",
        "qa_report.json",
        "revisions.json",
        "context/segments.jsonl",
        "context/windows.jsonl",
    ] + [f"data/{t}.jsonl" for t in p.TABLES]
    for rel in files:
        s = src_dir / rel
        if s.exists():
            d = dst_dir / rel
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(s, d)


def main() -> None:
    source_root = p.DEFAULT
    # Test against a clean temporary copy reconstructed from baseline pilot scripts
    import subprocess, sys

    with tempfile.TemporaryDirectory(prefix="bavli_cont_test_") as tmp_str:
        tmp = Path(tmp_str)
        pilot_build_dir = tmp / "baseline"
        pilot_build_dir.mkdir()
        for f in [
            "pipeline.py",
            "make_schema.py",
            "compile_annotations.py",
            "annotation_initial.py",
            "annotation_completion.py",
            "revisions.json",
            "validate.py",
        ]:
            shutil.copyfile(p.HERE / f, pilot_build_dir / f)
        for cmd in [
            ["pipeline.py", "build", "--source-root", str(source_root)],
            ["make_schema.py"],
            ["compile_annotations.py"],
            ["validate.py", "--source-root", str(source_root)],
        ]:
            res = subprocess.run(
                [sys.executable, "-X", "utf8", *cmd],
                cwd=pilot_build_dir,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            assert res.returncode == 0, res.stderr

        # Generate schema_v1_1.json in temp baseline
        shutil.copyfile(p.HERE / "schema_v1.json", pilot_build_dir / "schema_v1.json")
        (pilot_build_dir / "schema_v1_1.json").write_text(
            (p.HERE / "schema_v1_1.json").read_text(encoding="utf-8"), encoding="utf-8"
        )

        pkt = p.read(p.HERE / "blocks/berakhot_5b_6a/input_packet.json")
        prop = p.read(p.HERE / "blocks/berakhot_5b_6a/proposal.json")
        ind_rev = p.read(p.HERE / "blocks/berakhot_5b_6a/independent_review_initial.json")

        tests_passed: list[str] = []

        # 1. Verify full inherited open-tail extraction even when starting BEFORE default preceding context!
        deep_dir = tmp / "deep_tail"
        _copy_baseline_checkpoint(pilot_build_dir, deep_dir)
        sugs = p.rows(deep_dir / "data/sugyot.jsonl")
        segs = p.rows(deep_dir / "data/segments.jsonl")
        # Artificially make an open_right sugya starting back at 3b:10..5a:24 (pages 5..8) while default context_before=1 (only page 8)!
        ber_segs = [s for s in segs if s["tractate"] == "Berakhot"]
        idx_3b10 = next(idx for idx, s in enumerate(ber_segs) if s["ref"] == "Berakhot 3b:10")
        long_span_ids = [s["id"] for s in ber_segs[idx_3b10:]]
        sugs_mod = [g for g in sugs if not (g["tractate"] == "Berakhot" and set(g["segment_ids"]) & set(long_span_ids))]
        b24_orig = next(g for g in sugs if g["authoring_key"] == "B24")
        sugs_mod.append({
            **b24_orig,
            "segment_ids": long_span_ids,
            "start_ref": "Berakhot 3b:10",
            "end_ref": "Berakhot 5a:24",
            "boundary_status": "open_right",
        })
        p.jsonl(deep_dir / "data/sugyot.jsonl", sugs_mod)
        deep_pkt = c.prepare_block_input(deep_dir, source_root, "test_deep", "Berakhot", "5b", "6a", context_before_pages=1, context_after_pages=1)
        assert deep_pkt["inherited_open_tail"]["extended_before_default_context"] is True
        assert deep_pkt["preceding_context_page_indices"] == [5, 6, 7, 8]
        assert deep_pkt["counts"]["sequential_reading_packets"] >= 10
        tests_passed.append("full_inherited_open_tail_beyond_default_context")

        # 2. Verify interrupted write leaves previous checkpoint 100% byte-identical and usable!
        crash_dir = tmp / "crash_test"
        _copy_baseline_checkpoint(pilot_build_dir, crash_dir)
        (crash_dir / "schema_v1_1.json").write_text(
            (p.HERE / "schema_v1_1.json").read_text(encoding="utf-8"), encoding="utf-8"
        )
        before_snapshots = {
            rel: (crash_dir / rel).read_bytes()
            for rel in [f"data/{t}.jsonl" for t in p.TABLES] + ["context/segments.jsonl", "progress_manifest.json"]
        }
        try:
            c.apply_continuation_block(
                crash_dir, source_root, pkt, prop, ind_rev, _inject_fault_after_writes=3
            )
        except IOError:
            pass
        else:
            raise AssertionError("Expected simulated IOError on interrupted write!")
        for rel, b_bytes in before_snapshots.items():
            assert (crash_dir / rel).read_bytes() == b_bytes, f"Interrupted write corrupted {rel}!"
        assert c.validate_v1_1(crash_dir, source_root=source_root, check_source=True)["mechanical_pass"] is True
        tests_passed.append("interrupted_write_rolls_back_cleanly")

        # 3. Verify partial-review span guard: if independent review omits 5a:24, claiming independent_source_reviewed on extended B24 (5a:24-5b:3) is rejected!
        partial_rev = copy.deepcopy(ind_rev)
        partial_rev["units"][0]["start_ref"] = "Berakhot 5b:1"  # omits 5a:24!
        prop_overclaim = copy.deepcopy(prop)
        prop_overclaim["units"][0]["span_review_status"] = "independent_source_reviewed"
        try:
            c.apply_continuation_block(crash_dir, source_root, pkt, prop_overclaim, partial_rev)
        except c.ValidationGateError:
            tests_passed.append("partial_span_review_overclaim_rejected")
        else:
            raise AssertionError("Accepted overclaimed span_review_status on partially reviewed extended sugya!")

        # 4. Apply actual continuation block cleanly and verify unaffected pilot records are byte-for-byte preserved!
        work_dir = tmp / "apply_test"
        _copy_baseline_checkpoint(pilot_build_dir, work_dir)
        (work_dir / "schema_v1_1.json").write_text(
            (p.HERE / "schema_v1_1.json").read_text(encoding="utf-8"), encoding="utf-8"
        )
        pilot_seg_lines_before = (work_dir / "data/segments.jsonl").read_text(encoding="utf-8").splitlines()
        pilot_sug_by_id_before = {
            r["id"]: c.canon_json_bytes(r) for r in p.rows(work_dir / "data/sugyot.jsonl")
        }

        res1 = c.apply_continuation_block(work_dir, source_root, pkt, prop, ind_rev)
        assert res1["status"] == "accepted"

        seg_lines_after = (work_dir / "data/segments.jsonl").read_text(encoding="utf-8").splitlines()
        assert seg_lines_after[:215] == pilot_seg_lines_before, "First 215 pilot segment lines altered!"
        assert len(seg_lines_after) == 267  # 215 + 52

        sug_after = {r["id"]: r for r in p.rows(work_dir / "data/sugyot.jsonl")}
        for old_id, old_b in pilot_sug_by_id_before.items():
            if old_id == "sug_9a1c712c3a26fe45003b":
                # B24 was intentionally extended: verify ID preserved AND prior SHA256 recorded in lineage & revisions_ledger!
                assert sug_after[old_id]["lineage"]["previous_record_sha256"] == p.sha(old_b)
            else:
                assert c.canon_json_bytes(sug_after[old_id]) == old_b, f"Unaffected sugya {old_id} mutated!"
        tests_passed.append("appending_preserves_unaffected_records_and_b24_lineage")

        # 5. Replaying identical block is an idempotent no-op (zero duplicates!)
        bytes_after_first = {
            t: (work_dir / f"data/{t}.jsonl").read_bytes() for t in p.TABLES
        }
        res_replay = c.apply_continuation_block(work_dir, source_root, pkt, prop, ind_rev)
        assert res_replay["status"] == "already_applied_idempotent"
        for t, b_exp in bytes_after_first.items():
            assert (work_dir / f"data/{t}.jsonl").read_bytes() == b_exp
        tests_passed.append("identical_block_replay_is_idempotent")

        # 6. Conflicting block proposal or altered source hash is rejected!
        bad_prop = copy.deepcopy(prop)
        bad_prop["units"][-1]["title_he"] = "כותרת שונה סותרת"
        try:
            c.apply_continuation_block(work_dir, source_root, pkt, bad_prop, ind_rev)
        except c.ConflictingBlockError:
            tests_passed.append("conflicting_block_proposal_rejected")
        else:
            raise AssertionError("Accepted conflicting block proposal!")

        bad_pkt = copy.deepcopy(pkt)
        bad_pkt["block_id"] = "berakhot_block_003_fake"
        bad_prop2 = copy.deepcopy(prop)
        bad_prop2["block_id"] = "berakhot_block_003_fake"
        bad_pkt["source_sha256"] = "0" * 64
        try:
            c.apply_continuation_block(work_dir, source_root, bad_pkt, bad_prop2, ind_rev)
        except c.SourceIntegrityError:
            tests_passed.append("changed_source_hash_rejected")
        else:
            raise AssertionError("Accepted altered source_sha256!")

    report = {
        "passed": True,
        "continuation_invariants_verified": len(tests_passed),
        "tests": tests_passed,
    }
    p.write(p.HERE / "continuation_test_report.json", report)
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
