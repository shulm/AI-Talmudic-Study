"""Idempotent, checkpointed annotation runner with budget guard and offline replay."""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import DEFAULT_MODEL_CARBON, SCHEMA_VERSION, SOURCE_VERSION_ID
from .normalization import build_anchor, sha256_str, tractate_slug
from .reconciler import reconcile_window_boundaries
from .validators import load_jsonl
from .window_manager import build_overlapping_windows, filter_segments_by_daf_range


class BudgetAuthorizationError(RuntimeError):
    """Raised when paid external API execution is requested without explicit owner budget."""


def write_jsonl_deterministic(path: Path, records: list[dict[str, Any]], pk_field: str) -> None:
    """Idempotently deduplicate by primary key while preserving deterministic order."""
    seen: set[str] = set()
    deduped: list[dict[str, Any]] = []
    for rec in records:
        pk = rec[pk_field]
        if pk in seen:
            continue
        seen.add(pk)
        deduped.append(rec)
    path.parent.mkdir(parents=True, exist_ok=True)
    content = "\n".join(json.dumps(r, ensure_ascii=False) for r in deduped)
    path.write_text((content + "\n") if content else "", encoding="utf-8")


def compile_tractate_annotations_from_spec(
    project_root: Path,
    tractate_slug_str: str,
    spec_bundle: dict[str, Any],
) -> dict[str, Any]:
    """Compile audited window & pass specifications against frozen local segments into JSONL layers.

    Idempotent: re-running produces byte-identical JSONL files and updates checkpoint state.
    """
    t_dir = project_root / "tractates" / tractate_slug_str
    local_cache_path = (
        project_root / "local_source_cache" / tractate_slug_str / "segments.local_fulltext.jsonl"
    )
    if not local_cache_path.exists():
        raise FileNotFoundError(
            f"Local full-text cache missing at {local_cache_path}; run `cli scan` first."
        )

    all_local_segs = load_jsonl(local_cache_path)
    local_by_id = {s["segment_id"]: s for s in all_local_segs}

    start_daf = spec_bundle["start_daf"]
    end_daf = spec_bundle["end_daf"]
    review_status_default = spec_bundle.get("review_status_default", "provisional_ai_double")

    target_segs = filter_segments_by_daf_range(all_local_segs, start_daf=start_daf, end_daf=end_daf)
    windows = build_overlapping_windows(all_local_segs, start_daf=start_daf, end_daf=end_daf)

    # Save deterministic window plan for audit
    win_dir = project_root / "model_outputs" / "windows"
    win_dir.mkdir(parents=True, exist_ok=True)
    (win_dir / f"{tractate_slug_str}_{start_daf}_{end_daf}_windows.json").write_text(
        json.dumps([w.to_dict() for w in windows], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Resolve cue anchors inside window proposals
    resolved_window_proposals: list[dict[str, Any]] = []
    for wp in spec_bundle["window_proposals"]:
        units_out: list[dict[str, Any]] = []
        for u in wp["units"]:
            u_copy = dict(u)
            for cue_k in ("boundary_start_cue", "boundary_end_cue"):
                cue = dict(u_copy[cue_k])
                if "quote" in cue and "segment_id" in cue:
                    seg_id = cue.pop("segment_id")
                    q_txt = cue.pop("quote")
                    cue["anchor"] = build_anchor(
                        seg_id, local_by_id[seg_id]["canonical_text"], q_txt
                    )
                u_copy[cue_k] = cue

            resolved_subs: list[dict[str, Any]] = []
            for su in u_copy.get("sub_units", []):
                su_copy = dict(su)
                for cue_k in ("boundary_start_cue", "boundary_end_cue"):
                    cue = dict(su_copy[cue_k])
                    if "quote" in cue and "segment_id" in cue:
                        seg_id = cue.pop("segment_id")
                        q_txt = cue.pop("quote")
                        cue["anchor"] = build_anchor(
                            seg_id, local_by_id[seg_id]["canonical_text"], q_txt
                        )
                    su_copy[cue_k] = cue
                resolved_subs.append(su_copy)
            u_copy["sub_units"] = resolved_subs
            units_out.append(u_copy)
        resolved_window_proposals.append({"window_id": wp["window_id"], "units": units_out})

    sugyot_records, key_to_sugya_id = reconcile_window_boundaries(
        target_segs, resolved_window_proposals, review_status_default=review_status_default
    )

    # Pass 2: Statements
    statements_out: list[dict[str, Any]] = []
    stmt_anchor_by_id: dict[str, list[dict[str, Any]]] = {}
    for st_spec in spec_bundle.get("statements", []):
        sugya_id = key_to_sugya_id.get(st_spec["sugya_key"], st_spec["sugya_key"])
        sub_id = (
            key_to_sugya_id.get(st_spec["sub_sugya_key"], st_spec["sub_sugya_key"])
            if st_spec.get("sub_sugya_key")
            else None
        )
        spans: list[dict[str, Any]] = []
        for sp in st_spec["spans"]:
            spans.append(
                build_anchor(
                    sp["segment_id"],
                    local_by_id[sp["segment_id"]]["canonical_text"],
                    sp["quote"],
                    occurrence=sp.get("occurrence", 0),
                    allow_unaligned=sp.get("allow_unaligned", False),
                )
            )
        align_status = (
            "unaligned_needs_review"
            if any(a["alignment_status"] == "unaligned_needs_review" for a in spans)
            else "exact"
        )
        primary_seg = local_by_id[spans[0]["segment_id"]]
        stid = st_spec.get("statement_id") or (
            f"stmt:bavli:{tractate_slug_str}:{primary_seg['daf']}:{primary_seg['segment_num']}:s{st_spec['seq']:02d}"
        )
        stmt_anchor_by_id[stid] = spans
        statements_out.append(
            {
                "record_type": "statement",
                "schema_version": SCHEMA_VERSION,
                "source_version_id": SOURCE_VERSION_ID,
                "statement_id": stid,
                "sugya_id": sugya_id,
                "sub_sugya_id": sub_id,
                "source_spans": spans,
                "source_quote": " ... ".join(a["quote"] for a in spans),
                "alignment_status": align_status,
                "speaker_kind": st_spec["speaker_kind"],
                "speaker_id": st_spec.get("speaker_id"),
                "reported_by_id": st_spec.get("reported_by_id"),
                "transmission_chain_ids": st_spec.get("transmission_chain_ids", []),
                "quoted_source_type": st_spec.get("quoted_source_type", "none"),
                "attributed_to_ids": st_spec.get("attributed_to_ids", []),
                "attribution_type": st_spec["attribution_type"],
                "speech_act": st_spec["speech_act"],
                "interpretation_status": st_spec["interpretation_status"],
                "annotator_paraphrase": st_spec.get("annotator_paraphrase"),
                "is_annotator_paraphrase": True if st_spec.get("annotator_paraphrase") else False,
                "textual_variant_notes": st_spec.get("textual_variant_notes"),
            }
        )

    # Pass 3: Questions, Positions, Relations, Reviews
    questions_out: list[dict[str, Any]] = []
    for q_spec in spec_bundle.get("questions", []):
        sugya_id = key_to_sugya_id.get(q_spec["sugya_key"], q_spec["sugya_key"])
        ev_ids = q_spec["evidence_statement_ids"]
        q_spans = [a for sid in ev_ids for a in stmt_anchor_by_id[sid]]
        alts = [
            {
                "alternative_id": a["alternative_id"],
                "neutral_text_he": a["neutral_text_he"],
                "content_sha256": sha256_str(a["neutral_text_he"]),
            }
            for a in q_spec.get("candidate_alternatives", [])
        ]
        questions_out.append(
            {
                "record_type": "question",
                "schema_version": SCHEMA_VERSION,
                "source_version_id": SOURCE_VERSION_ID,
                "question_id": q_spec["question_id"],
                "sugya_id": sugya_id,
                "neutral_question_he": q_spec["neutral_question_he"],
                "is_annotator_paraphrase": True,
                "prerequisites_conditions_he": q_spec.get("prerequisites_conditions_he", []),
                "question_scope": q_spec["question_scope"],
                "answer_set_type": q_spec["answer_set_type"],
                "candidate_alternatives": alts,
                "source_explicit_status": q_spec["source_explicit_status"],
                "evidence_statement_ids": ev_ids,
                "source_spans": q_spans,
                "ml_prediction_eligible": q_spec["ml_prediction_eligible"],
                "ml_eligibility_rationale": q_spec["ml_eligibility_rationale"],
                "parallel_family_id": q_spec["parallel_family_id"],
            }
        )

    positions_out: list[dict[str, Any]] = []
    for p_spec in spec_bundle.get("positions", []):
        sugya_id = key_to_sugya_id.get(p_spec["sugya_key"], p_spec["sugya_key"])
        st_ids = p_spec["statement_ids"]
        p_spans = [a for sid in st_ids for a in stmt_anchor_by_id[sid]]
        positions_out.append(
            {
                "record_type": "position",
                "schema_version": SCHEMA_VERSION,
                "source_version_id": SOURCE_VERSION_ID,
                "position_id": p_spec["position_id"],
                "question_id": p_spec["question_id"],
                "sugya_id": sugya_id,
                "statement_ids": st_ids,
                "holder_kind": p_spec["holder_kind"],
                "holder_ids": p_spec.get("holder_ids", []),
                "transmitted_via_ids": p_spec.get("transmitted_via_ids", []),
                "alternative_id": p_spec.get("alternative_id"),
                "semantic_position_he": p_spec["semantic_position_he"],
                "is_annotator_paraphrase": True,
                "conditions_he": p_spec.get("conditions_he", []),
                "position_status": p_spec["position_status"],
                "reason_statement_ids": p_spec.get("reason_statement_ids", []),
                "source_spans": p_spans,
            }
        )

    relations_out: list[dict[str, Any]] = []
    for r_spec in spec_bundle.get("relations", []):
        sugya_id = key_to_sugya_id.get(r_spec["sugya_key"], r_spec["sugya_key"])
        if "spans" in r_spec:
            r_spans = [
                build_anchor(
                    sp["segment_id"],
                    local_by_id[sp["segment_id"]]["canonical_text"],
                    sp["quote"],
                    occurrence=sp.get("occurrence", 0),
                )
                for sp in r_spec["spans"]
            ]
        else:
            r_spans = list(stmt_anchor_by_id[r_spec["evidence_statement_id"]])
        relations_out.append(
            {
                "record_type": "relation",
                "schema_version": SCHEMA_VERSION,
                "source_version_id": SOURCE_VERSION_ID,
                "sugya_id": sugya_id,
                "relation_id": r_spec["relation_id"],
                "from_id": r_spec["from_id"],
                "to_id": r_spec["to_id"],
                "relation_type": r_spec["relation_type"],
                "source_spans": r_spans,
                "relation_status": r_spec["relation_status"],
                "rationale": r_spec.get("rationale", ""),
            }
        )

    reviews_out: list[dict[str, Any]] = []
    for rv_spec in spec_bundle.get("reviews", []):
        target_id = key_to_sugya_id.get(rv_spec["target_id"], rv_spec["target_id"])
        reviews_out.append(
            {
                "record_type": "review",
                "schema_version": SCHEMA_VERSION,
                "source_version_id": SOURCE_VERSION_ID,
                "review_id": rv_spec["review_id"],
                "target_id": target_id,
                "issue_type": rv_spec["issue_type"],
                "status": rv_spec["status"],
                "evidence_refs": rv_spec["evidence_refs"],
                "review_level": rv_spec.get("review_level", "ai_independent_double"),
                "history": rv_spec["history"],
            }
        )

    write_jsonl_deterministic(t_dir / "sugyot.jsonl", sugyot_records, "sugya_id")
    write_jsonl_deterministic(t_dir / "statements.jsonl", statements_out, "statement_id")
    write_jsonl_deterministic(t_dir / "questions.jsonl", questions_out, "question_id")
    write_jsonl_deterministic(t_dir / "positions.jsonl", positions_out, "position_id")
    write_jsonl_deterministic(t_dir / "relations.jsonl", relations_out, "relation_id")
    write_jsonl_deterministic(t_dir / "review_queue.jsonl", reviews_out, "review_id")

    # Update manifest annotation_scope & checkpoint
    manifest_path = t_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    covered_dafs: list[str] = []
    for s in target_segs:
        if s["daf"] not in covered_dafs:
            covered_dafs.append(s["daf"])
    is_full = len(target_segs) == manifest["total_tractate_segments"]
    manifest["annotation_scope"] = {
        "mode": "full_tractate" if is_full else "pilot_daf_slice",
        "covered_daf_range": f"{start_daf}-{end_daf}",
        "covered_dafs": covered_dafs,
        "covered_segment_ids_count": len(target_segs),
        "unannotated_remaining_segments": manifest["total_tractate_segments"] - len(target_segs),
        "tractate_completion_status": (
            "PROVISIONAL_TRACTATE_COMPLETE" if is_full else "PILOT_SLICE_PROVISIONAL_COMPLETE"
        ),
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    ckpt_dir = project_root / "checkpoints"
    ckpt_dir.mkdir(parents=True, exist_ok=True)
    ckpt = {
        "tractate_slug": tractate_slug_str,
        "covered_daf_range": f"{start_daf}-{end_daf}",
        "completed_windows": [w.window_id for w in windows],
        "sugyot_count": len(sugyot_records),
        "statements_count": len(statements_out),
        "questions_count": len(questions_out),
        "positions_count": len(positions_out),
        "relations_count": len(relations_out),
        "reviews_count": len(reviews_out),
        "updated_at": "2026-11-24T23:30:00+02:00",
    }
    (ckpt_dir / f"{tractate_slug_str}.checkpoint.json").write_text(
        json.dumps(ckpt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return ckpt


def run_gemini_api_guarded(
    model: str = DEFAULT_MODEL_CARBON,
    authorized_budget_usd: float = 0.0,
    dry_run: bool = True,
) -> dict[str, Any]:
    """Budget-guarded entry point for external paid Gemini API bulk passes."""
    if dry_run:
        return {
            "mode": "dry_run",
            "model": model,
            "authorized_budget_usd": authorized_budget_usd,
            "external_calls_made": 0,
            "estimated_cost_usd": 0.0,
        }
    if authorized_budget_usd <= 0.0:
        raise BudgetAuthorizationError(
            "Refusing to make paid external Gemini API calls: --authorized-budget-usd is 0.0. "
            "Pass an explicit owner-authorized budget after pilot gate sign-off."
        )
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise BudgetAuthorizationError(
            "GEMINI_API_KEY / GOOGLE_API_KEY is not set in environment."
        )
    return {
        "mode": "gemini_api_ready",
        "model": model,
        "authorized_budget_usd": authorized_budget_usd,
    }
