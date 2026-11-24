"""Unit and adversarial rabbinic safeguard tests for Bavli Sugya Corpus v1."""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from research.bavli_sugya_corpus_v1.src.bavli_corpus import SCHEMA_VERSION, SOURCE_VERSION_ID
from research.bavli_sugya_corpus_v1.src.bavli_corpus.annotation_runner import (
    BudgetAuthorizationError,
    run_gemini_api_guarded,
)
from research.bavli_sugya_corpus_v1.src.bavli_corpus.normalization import (
    build_anchor,
    normalize_with_offset_map,
    project_canon_span_to_raw,
    sha256_str,
)
from research.bavli_sugya_corpus_v1.src.bavli_corpus.reconciler import reconcile_window_boundaries
from research.bavli_sugya_corpus_v1.src.bavli_corpus.scanner import (
    daf_str_to_page_index,
    page_index_to_daf,
)
from research.bavli_sugya_corpus_v1.src.bavli_corpus.validators import validate_tractate_bundle


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _make_fixture_env(tmp_path: Path) -> tuple[Path, list[dict], dict[str, dict]]:
    """Create a minimal synthetic 2-amud crossing tractate bundle for adversarial testing."""
    (tmp_path / "schemas").mkdir(parents=True)
    (tmp_path / "schemas" / "schema_v1.json").write_text(
        (PROJECT_ROOT / "schemas" / "schema_v1.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    t_dir = tmp_path / "tractates" / "berakhot"
    t_dir.mkdir(parents=True)

    raw_texts = [
        ("2a", 2, 0, "<big><strong>מאימתי</strong></big> קורין את שמע בערבין"),
        ("2a", 2, 1, "אמר רב יהודה אמר שמואל הלכה כרבי אליעזר וחד אמר כרבנן"),
        ("2b", 3, 0, "רבה אמר טעמא דקרא ורבא אמר לא פליגי כאן קודם חצות כאן לאחר חצות איפוך תיובתא"),
    ]
    repo_segs = []
    local_map = {}
    for ord_i, (daf, p_idx, s_idx, raw_t) in enumerate(raw_texts):
        canon_t, omap = normalize_with_offset_map(raw_t)
        sid = f"seg:bavli:berakhot:{daf}:{s_idx+1}"
        rec = {
            "record_type": "segment",
            "schema_version": SCHEMA_VERSION,
            "source_version_id": SOURCE_VERSION_ID,
            "segment_id": sid,
            "tractate": "Berakhot",
            "tractate_he": "ברכות",
            "seder": "Seder Zeraim",
            "chapter_num": 1,
            "chapter_title_en": "Chapter 1",
            "chapter_title_he": "מאימתי",
            "daf": daf,
            "folio_num": 2,
            "amud": daf[-1],
            "segment_num": s_idx + 1,
            "ordinal_in_tractate": ord_i,
            "ref": f"Berakhot {daf}:{s_idx+1}",
            "he_ref": f"ברכות ב:{s_idx+1}",
            "raw_array_index": [p_idx, s_idx],
            "source_file_rel": "json/Talmud/Bavli/Seder Zeraim/Berakhot/Hebrew/William Davidson Edition - Aramaic.json",
            "source_file_sha256": "a" * 64,
            "license": "CC-BY-NC",
            "redistribution_status": "local_only_cc_by_nc",
            "raw_sha256": sha256_str(raw_t),
            "canonical_sha256": sha256_str(canon_t),
            "raw_char_len": len(raw_t),
            "canonical_char_len": len(canon_t),
            "normalization_spec_id": "canon_strip_html_collapse_ws_v1",
            "offset_map": omap,
            "raw_text": None,
            "canonical_text": None,
        }
        repo_segs.append(rec)
        local_map[sid] = {**rec, "raw_text": raw_t, "canonical_text": canon_t}

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "source_version_id": SOURCE_VERSION_ID,
        "tractate": "Berakhot",
        "tractate_he": "ברכות",
        "slug": "berakhot",
        "toc_order": 1,
        "seder": "Seder Zeraim",
        "source_file_rel": "x",
        "source_file_sha256": "a" * 64,
        "license": "CC-BY-NC",
        "start_ref": "Berakhot 2a:1",
        "end_ref": "Berakhot 2b:1",
        "total_tractate_segments": 3,
        "segment_inventory_sha256": "b" * 64,
        "chapters": [],
        "annotation_scope": {
            "mode": "full_tractate",
            "covered_daf_range": "2a-2b",
            "covered_dafs": ["2a", "2b"],
            "covered_segment_ids_count": 3,
            "tractate_completion_status": "PROVISIONAL_TRACTATE_COMPLETE",
        },
    }
    (t_dir / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    (t_dir / "segments.jsonl").write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in repo_segs) + "\n", encoding="utf-8"
    )

    # Reconcile cross-amud sugya spanning 2a:2 -> 2b:1
    win_props = [
        {
            "window_id": "w1",
            "units": [
                {
                    "local_key": "m1",
                    "segment_ids": ["seg:bavli:berakhot:2a:1"],
                    "continues_from_prev_window": False,
                    "continues_into_next_window": False,
                    "sugya_type": "mishnah",
                    "mishna_gemara_relation": "mishnah_text",
                    "topic_tags": ["shema"],
                    "summary_paraphrase_en": "Opening mishnah",
                    "boundary_start_cue": {
                        "cue_type": "mishnah_opening",
                        "description": "Opening",
                        "anchor": build_anchor(
                            "seg:bavli:berakhot:2a:1",
                            local_map["seg:bavli:berakhot:2a:1"]["canonical_text"],
                            "מאימתי קורין",
                        ),
                    },
                    "boundary_end_cue": {
                        "cue_type": "sugya_conclusion",
                        "description": "End",
                        "anchor": build_anchor(
                            "seg:bavli:berakhot:2a:1",
                            local_map["seg:bavli:berakhot:2a:1"]["canonical_text"],
                            "בערבין",
                        ),
                    },
                },
                {
                    "local_key": "g1_part1",
                    "segment_ids": ["seg:bavli:berakhot:2a:2"],
                    "continues_from_prev_window": False,
                    "continues_into_next_window": True,
                    "sugya_type": "halakhic_dialectic",
                    "mishna_gemara_relation": "direct_mishnah_commentary",
                    "topic_tags": ["halakha"],
                    "summary_paraphrase_en": "Cross-amud gemara",
                    "boundary_start_cue": {
                        "cue_type": "gemara_opening",
                        "description": "Start",
                        "anchor": build_anchor(
                            "seg:bavli:berakhot:2a:2",
                            local_map["seg:bavli:berakhot:2a:2"]["canonical_text"],
                            "אמר רב יהודה",
                        ),
                    },
                    "boundary_end_cue": {
                        "cue_type": "continuation_across_daf",
                        "description": "Cont",
                    },
                },
            ],
        },
        {
            "window_id": "w2",
            "units": [
                {
                    "local_key": "g1_part2",
                    "segment_ids": ["seg:bavli:berakhot:2b:1"],
                    "continues_from_prev_window": True,
                    "continues_into_next_window": False,
                    "sugya_type": "halakhic_dialectic",
                    "mishna_gemara_relation": "direct_mishnah_commentary",
                    "boundary_start_cue": {"cue_type": "continuation_across_daf", "description": "Cont"},
                    "boundary_end_cue": {
                        "cue_type": "sugya_conclusion",
                        "description": "End",
                        "anchor": build_anchor(
                            "seg:bavli:berakhot:2b:1",
                            local_map["seg:bavli:berakhot:2b:1"]["canonical_text"],
                            "תיובתא",
                        ),
                    },
                }
            ],
        },
    ]
    sugyot, _ = reconcile_window_boundaries(repo_segs, win_props)
    assert sugyot[1]["crosses_amud"] is True
    (t_dir / "sugyot.jsonl").write_text(
        "\n".join(json.dumps(s, ensure_ascii=False) for s in sugyot) + "\n", encoding="utf-8"
    )
    for empty_f in ("statements.jsonl", "questions.jsonl", "positions.jsonl", "relations.jsonl", "review_queue.jsonl"):
        (t_dir / empty_f).write_text("", encoding="utf-8")

    scholars = [
        {
            "record_type": "scholar",
            "schema_version": SCHEMA_VERSION,
            "scholar_id": "scholar:amora:rav",
            "canonical_name_he": "רב",
            "canonical_name_en": "Rav",
            "entity_kind": "individual_scholar",
            "orthographic_variants": ["רב"],
            "era": "amora_bavli",
            "identity_status": "well_attested",
            "distinct_from_ids": ["scholar:amora:rav_yehuda"],
            "disambiguation_notes": "Standalone Rav only.",
        },
        {
            "record_type": "scholar",
            "schema_version": SCHEMA_VERSION,
            "scholar_id": "scholar:amora:rav_yehuda",
            "canonical_name_he": "רב יהודה",
            "canonical_name_en": "Rav Yehuda",
            "entity_kind": "individual_scholar",
            "orthographic_variants": ["רב יהודה"],
            "era": "amora_bavli",
            "identity_status": "well_attested",
            "distinct_from_ids": ["scholar:amora:rav"],
            "disambiguation_notes": "Distinct from standalone Rav.",
        },
        {
            "record_type": "scholar",
            "schema_version": SCHEMA_VERSION,
            "scholar_id": "scholar:amora:shmuel",
            "canonical_name_he": "שמואל",
            "canonical_name_en": "Shmuel",
            "entity_kind": "individual_scholar",
            "orthographic_variants": ["שמואל"],
            "era": "amora_bavli",
            "identity_status": "well_attested",
            "disambiguation_notes": "First-gen Bavli Amora.",
        },
        {
            "record_type": "scholar",
            "schema_version": SCHEMA_VERSION,
            "scholar_id": "scholar:amora:rabbah",
            "canonical_name_he": "רבה",
            "canonical_name_en": "Rabbah",
            "entity_kind": "individual_scholar",
            "orthographic_variants": ["רבה"],
            "era": "amora_bavli",
            "identity_status": "well_attested",
            "distinct_from_ids": ["scholar:amora:rava"],
            "disambiguation_notes": "Never merge with Rava.",
        },
        {
            "record_type": "scholar",
            "schema_version": SCHEMA_VERSION,
            "scholar_id": "scholar:amora:rava",
            "canonical_name_he": "רבא",
            "canonical_name_en": "Rava",
            "entity_kind": "individual_scholar",
            "orthographic_variants": ["רבא"],
            "era": "amora_bavli",
            "identity_status": "well_attested",
            "distinct_from_ids": ["scholar:amora:rabbah"],
            "disambiguation_notes": "Never merge with Rabbah.",
        },
    ]
    return tmp_path, scholars, local_map


def test_daf_and_reversible_offset_map():
    assert page_index_to_daf(2) == (2, "a", "2a")
    assert page_index_to_daf(3) == (2, "b", "2b")
    assert page_index_to_daf(49) == (25, "b", "25b")  # Tamid start
    assert daf_str_to_page_index("2a") == 2
    assert daf_str_to_page_index("25b") == 49

    raw = "  <big><strong>מאימתי</strong></big>   קורין את שמע  "
    canon, omap = normalize_with_offset_map(raw)
    assert canon == "מאימתי קורין את שמע"
    anc = build_anchor("seg:bavli:berakhot:2a:1", canon, "קורין את")
    r_s, r_e = project_canon_span_to_raw(omap, anc["start_char"], anc["end_char"])
    assert raw[r_s:r_e] == "קורין את"


def test_adversarial_rabbinic_safeguards(tmp_path: Path):
    env_root, scholars, local_map = _make_fixture_env(tmp_path)
    t_dir = env_root / "tractates" / "berakhot"

    # Baseline clean validation passes
    res0 = validate_tractate_bundle(env_root, "berakhot", scholars, local_map)
    assert res0["valid"], res0["errors"]

    c_2a2 = local_map["seg:bavli:berakhot:2a:2"]["canonical_text"]
    c_2b1 = local_map["seg:bavli:berakhot:2b:1"]["canonical_text"]

    # 1. Adversarial: Rabbah vs Rava confusion ("רבה אמר טעמא דקרא" assigned to Rava!)
    bad_rava_stmt = {
        "record_type": "statement",
        "schema_version": SCHEMA_VERSION,
        "source_version_id": SOURCE_VERSION_ID,
        "statement_id": "stmt:bavli:berakhot:2b:1:s01",
        "sugya_id": "sugya:bavli:berakhot:2a:2__2b:1",
        "source_spans": [build_anchor("seg:bavli:berakhot:2b:1", c_2b1, "רבה אמר טעמא דקרא")],
        "source_quote": "רבה אמר טעמא דקרא",
        "alignment_status": "exact",
        "speaker_kind": "named_scholar",
        "speaker_id": "scholar:amora:rava",
        "reported_by_id": None,
        "attributed_to_ids": ["scholar:amora:rava"],
        "attribution_type": "explicit_direct",
        "speech_act": "explanation",
        "interpretation_status": "asserted",
    }
    (t_dir / "statements.jsonl").write_text(json.dumps(bad_rava_stmt, ensure_ascii=False) + "\n", encoding="utf-8")
    res_rava = validate_tractate_bundle(env_root, "berakhot", scholars, local_map)
    assert not res_rava["valid"]
    assert any("rabbah_rava" in e for e in res_rava["errors"])

    # 2. Adversarial: Compound name "רב יהודה" falsely assigned to standalone "רב"
    bad_rav_stmt = copy.deepcopy(bad_rava_stmt)
    bad_rav_stmt["statement_id"] = "stmt:bavli:berakhot:2a:2:s01"
    bad_rav_stmt["source_spans"] = [build_anchor("seg:bavli:berakhot:2a:2", c_2a2, "אמר רב יהודה אמר שמואל")]
    bad_rav_stmt["source_quote"] = "אמר רב יהודה אמר שמואל"
    bad_rav_stmt["speaker_id"] = "scholar:amora:rav"
    bad_rav_stmt["attributed_to_ids"] = ["scholar:amora:rav"]
    (t_dir / "statements.jsonl").write_text(json.dumps(bad_rav_stmt, ensure_ascii=False) + "\n", encoding="utf-8")
    res_rav = validate_tractate_bundle(env_root, "berakhot", scholars, local_map)
    assert not res_rav["valid"]
    assert any("rav_compound" in e for e in res_rav["errors"])

    # 3. Adversarial: Quoted transmission conflating transmitter (רב יהודה) with authority (שמואל)
    bad_trans_stmt = copy.deepcopy(bad_rav_stmt)
    bad_trans_stmt["speaker_id"] = "scholar:amora:rav_yehuda"
    bad_trans_stmt["reported_by_id"] = "scholar:amora:rav_yehuda"
    bad_trans_stmt["attributed_to_ids"] = ["scholar:amora:rav_yehuda", "scholar:amora:shmuel"]
    bad_trans_stmt["attribution_type"] = "explicit_transmitted"
    (t_dir / "statements.jsonl").write_text(json.dumps(bad_trans_stmt, ensure_ascii=False) + "\n", encoding="utf-8")
    res_trans = validate_tractate_bundle(env_root, "berakhot", scholars, local_map)
    assert not res_trans["valid"]
    assert any("transmission" in e for e in res_trans["errors"])

    # 4. Adversarial: Unresolved חד אמר assigning named scholar by order
    bad_chad = copy.deepcopy(bad_rava_stmt)
    bad_chad["statement_id"] = "stmt:bavli:berakhot:2a:2:s02"
    bad_chad["source_spans"] = [build_anchor("seg:bavli:berakhot:2a:2", c_2a2, "וחד אמר כרבנן")]
    bad_chad["source_quote"] = "וחד אמר כרבנן"
    bad_chad["speaker_kind"] = "unresolved_chad_amar"
    bad_chad["speaker_id"] = None
    bad_chad["attribution_type"] = "unresolved_chad_amar"
    bad_chad["attributed_to_ids"] = ["scholar:amora:rav"]
    (t_dir / "statements.jsonl").write_text(json.dumps(bad_chad, ensure_ascii=False) + "\n", encoding="utf-8")
    res_chad = validate_tractate_bundle(env_root, "berakhot", scholars, local_map)
    assert not res_chad["valid"]
    assert any("chad_amar" in e for e in res_chad["errors"])

    # 5. Adversarial: Anonymous Stam falsely assigned to nearby Amora
    bad_stam = copy.deepcopy(bad_rava_stmt)
    bad_stam["source_spans"] = [build_anchor("seg:bavli:berakhot:2b:1", c_2b1, "איפוך תיובתא")]
    bad_stam["source_quote"] = "איפוך תיובתא"
    bad_stam["speaker_kind"] = "anonymous_stam"
    bad_stam["attribution_type"] = "anonymous_stam"
    bad_stam["speaker_id"] = "scholar:amora:rava"
    bad_stam["attributed_to_ids"] = ["scholar:amora:rava"]
    (t_dir / "statements.jsonl").write_text(json.dumps(bad_stam, ensure_ascii=False) + "\n", encoding="utf-8")
    res_stam = validate_tractate_bundle(env_root, "berakhot", scholars, local_map)
    assert not res_stam["valid"]
    assert any("stam" in e for e in res_stam["errors"])

    # 6. Adversarial: Refuted תיובתא statement recorded as accepted 'asserted' position + silence imputation
    refuted_stmt = {
        "record_type": "statement",
        "schema_version": SCHEMA_VERSION,
        "source_version_id": SOURCE_VERSION_ID,
        "statement_id": "stmt:bavli:berakhot:2b:1:s03",
        "sugya_id": "sugya:bavli:berakhot:2a:2__2b:1",
        "source_spans": [build_anchor("seg:bavli:berakhot:2b:1", c_2b1, "רבה אמר טעמא דקרא")],
        "source_quote": "רבה אמר טעמא דקרא",
        "alignment_status": "exact",
        "speaker_kind": "named_scholar",
        "speaker_id": "scholar:amora:rabbah",
        "reported_by_id": None,
        "attributed_to_ids": ["scholar:amora:rabbah"],
        "attribution_type": "explicit_direct",
        "speech_act": "explanation",
        "interpretation_status": "refuted_tiyuvta",
    }
    q_rec = {
        "record_type": "question",
        "schema_version": SCHEMA_VERSION,
        "source_version_id": SOURCE_VERSION_ID,
        "question_id": "q:bavli:berakhot:2b:1:q01",
        "sugya_id": "sugya:bavli:berakhot:2a:2__2b:1",
        "neutral_question_he": "מהו טעם הדין בקריאת שמע?",
        "prerequisites_conditions_he": [],
        "question_scope": "scriptural_derivation",
        "answer_set_type": "open_explanatory",
        "candidate_alternatives": [],
        "source_explicit_status": "editor_reconstructed_from_positions",
        "evidence_statement_ids": ["stmt:bavli:berakhot:2b:1:s03"],
        "source_spans": refuted_stmt["source_spans"],
        "ml_prediction_eligible": False,
        "ml_eligibility_rationale": "Single refuted proposal.",
        "parallel_family_id": "pfam:test_01",
    }
    bad_pos = {
        "record_type": "position",
        "schema_version": SCHEMA_VERSION,
        "source_version_id": SOURCE_VERSION_ID,
        "position_id": "pos:bavli:berakhot:2b:1:p01",
        "question_id": "q:bavli:berakhot:2b:1:q01",
        "sugya_id": "sugya:bavli:berakhot:2a:2__2b:1",
        "statement_ids": ["stmt:bavli:berakhot:2b:1:s03"],
        "holder_kind": "named_scholar",
        "holder_ids": ["scholar:amora:rabbah", "scholar:amora:shmuel"],  # Shmuel unmentioned!
        "semantic_position_he": "טעמא דקרא",
        "position_status": "asserted",  # Invalid on refuted_tiyuvta!
        "source_spans": refuted_stmt["source_spans"],
    }
    (t_dir / "statements.jsonl").write_text(json.dumps(refuted_stmt, ensure_ascii=False) + "\n", encoding="utf-8")
    (t_dir / "questions.jsonl").write_text(json.dumps(q_rec, ensure_ascii=False) + "\n", encoding="utf-8")
    (t_dir / "positions.jsonl").write_text(json.dumps(bad_pos, ensure_ascii=False) + "\n", encoding="utf-8")
    res_pos = validate_tractate_bundle(env_root, "berakhot", scholars, local_map)
    assert not res_pos["valid"]
    assert any("rejected_status" in e for e in res_pos["errors"])
    assert any("no_silence_imputation" in e for e in res_pos["errors"])


def test_budget_guard_blocks_unapproved_paid_calls():
    dry = run_gemini_api_guarded(dry_run=True)
    assert dry["external_calls_made"] == 0
    with pytest.raises(BudgetAuthorizationError):
        run_gemini_api_guarded(authorized_budget_usd=0.0, dry_run=False)


def test_real_pilot_bundles_and_idempotency():
    """Verify actual materialized Berakhot & Bava Metzia pilot slices, CC-BY-NC safety, and queries."""
    from research.bavli_sugya_corpus_v1.src.bavli_corpus.annotation_runner import (
        compile_tractate_annotations_from_spec,
    )
    from research.bavli_sugya_corpus_v1.src.bavli_corpus.double_review import (
        compute_double_review_agreement,
    )
    from research.bavli_sugya_corpus_v1.src.bavli_corpus.queries import (
        derive_eligible_qa_candidates,
        find_scholar_statements,
        reconstruct_sugya,
    )
    from research.bavli_sugya_corpus_v1.src.bavli_corpus.validators import load_jsonl

    scholars = load_jsonl(PROJECT_ROOT / "scholars.jsonl")
    assert len(scholars) >= 40

    for slug, expected_target_segs in [("berakhot", 151), ("bava_metzia", 64)]:
        t_dir = PROJECT_ROOT / "tractates" / slug
        # Check repo-facing segments.jsonl never leaks CC-BY-NC full text
        repo_segs = load_jsonl(t_dir / "segments.jsonl")
        assert all(s["raw_text"] is None and s["canonical_text"] is None for s in repo_segs)

        local_cache = PROJECT_ROOT / "local_source_cache" / slug / "segments.local_fulltext.jsonl"
        local_map = (
            {s["segment_id"]: s for s in load_jsonl(local_cache)} if local_cache.exists() else None
        )
        res = validate_tractate_bundle(PROJECT_ROOT, slug, scholars, local_fulltext_by_id=local_map)
        assert res["valid"], f"Validation errors in {slug}: {res['errors']}"
        assert res["metrics"]["target_covered_segments"] == expected_target_segs

        # Verify byte-for-byte idempotency when local cache is available
        if local_cache.exists():
            before_bytes = (t_dir / "sugyot.jsonl").read_bytes()
            spec = json.loads(
                (PROJECT_ROOT / "model_outputs" / "pass1_3_pilot" / f"{slug}_spec.json").read_text(
                    encoding="utf-8"
                )
            )
            compile_tractate_annotations_from_spec(PROJECT_ROOT, slug, spec)
            after_bytes = (t_dir / "sugyot.jsonl").read_bytes()
            assert before_bytes == after_bytes

    # Check query helpers: Rabbah vs Rava separation!
    rabbah_q = find_scholar_statements(PROJECT_ROOT, "scholar:amora:rabbah")
    rava_q = find_scholar_statements(PROJECT_ROOT, "scholar:amora:rava")
    assert rabbah_q["held_statements_count"] >= 2
    assert rava_q["held_statements_count"] >= 4
    rabbah_ids = {s["statement_id"] for s in rabbah_q["held_statements"]}
    rava_ids = {s["statement_id"] for s in rava_q["held_statements"]}
    assert rabbah_ids.isdisjoint(rava_ids)

    recon = reconstruct_sugya(PROJECT_ROOT, "bava_metzia", "sugya:bavli:bava_metzia:21a:19__22b:10")
    assert recon["sugya"]["crosses_daf"] is True
    assert len(recon["ordered_segments"]) == 40

    qa_items = derive_eligible_qa_candidates(PROJECT_ROOT)
    assert len(qa_items) >= 7
    # Ensure unresolved חד אמר and תיקו questions are excluded from ML-eligible view
    eligible_qids = {item["evaluator_only_grounding"]["question_id"] for item in qa_items}
    assert "q:bavli:berakhot:4a:8:q01" not in eligible_qids
    assert "q:bavli:berakhot:5a:14:q01" not in eligible_qids
    assert "q:bavli:bava_metzia:21a:14:q01" not in eligible_qids

    agree = compute_double_review_agreement(PROJECT_ROOT)
    assert agree["overall"]["slot_agreement_rate"] >= 0.95

