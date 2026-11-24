"""Query and export utilities: sugya reconstruction, scholar history H_s, and caveated ML Q-A views."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .validators import load_jsonl


def reconstruct_sugya(
    project_root: Path,
    tractate_slug: str,
    sugya_id: str,
) -> dict[str, Any]:
    """Reconstruct a complete sugya with its ordered segments, sub-sugyot, statements, Q-A, and relations."""
    t_dir = project_root / "tractates" / tractate_slug
    sugyot = {s["sugya_id"]: s for s in load_jsonl(t_dir / "sugyot.jsonl")}
    if sugya_id not in sugyot:
        # Check lineage redirects
        for s in sugyot.values():
            if sugya_id in s.get("redirects_from", []):
                sugya_id = s["sugya_id"]
                break
        else:
            raise KeyError(f"Sugya {sugya_id} not found in {tractate_slug}")

    sugya = sugyot[sugya_id]
    local_cache_path = project_root / "local_source_cache" / tractate_slug / "segments.local_fulltext.jsonl"
    seg_path = local_cache_path if local_cache_path.exists() else (t_dir / "segments.jsonl")
    seg_by_id = {s["segment_id"]: s for s in load_jsonl(seg_path)}

    ordered_segs = [seg_by_id[sid] for sid in sugya["ordered_segment_ids"]]
    sub_units = [s for s in sugyot.values() if s.get("parent_sugya_id") == sugya_id]
    statements = [st for st in load_jsonl(t_dir / "statements.jsonl") if st["sugya_id"] == sugya_id]
    questions = [q for q in load_jsonl(t_dir / "questions.jsonl") if q["sugya_id"] == sugya_id]
    positions = [p for p in load_jsonl(t_dir / "positions.jsonl") if p["sugya_id"] == sugya_id]
    relations = [r for r in load_jsonl(t_dir / "relations.jsonl") if r.get("sugya_id") == sugya_id]
    target_ids = {sugya_id} | {s["statement_id"] for s in statements} | {q["question_id"] for q in questions} | {p["position_id"] for p in positions}
    reviews = [rv for rv in load_jsonl(t_dir / "review_queue.jsonl") if rv["target_id"] in target_ids]

    return {
        "sugya": sugya,
        "local_fulltext_available": local_cache_path.exists(),
        "ordered_segments": [
            {
                "segment_id": s["segment_id"],
                "ref": s["ref"],
                "canonical_sha256": s["canonical_sha256"],
                "canonical_text": s.get("canonical_text"),
            }
            for s in ordered_segs
        ],
        "sub_sugyot": sub_units,
        "statements": statements,
        "questions": questions,
        "positions": positions,
        "relations": relations,
        "reviews": reviews,
    }


def find_scholar_statements(
    project_root: Path,
    scholar_id: str,
) -> dict[str, Any]:
    """Find all justified statements and positions for a scholar across all processed tractates.

    Strictly separates:
      - held_statements (scholar in attributed_to_ids: actual holder of the claim/ruling)
      - transmitted_only_statements (scholar in reported_by_id / transmission_chain_ids, NOT holder)
      - positions_by_status (asserted vs conditional vs rejected/inverted/variant)
    """
    scholars = {s["scholar_id"]: s for s in load_jsonl(project_root / "scholars.jsonl")}
    if scholar_id not in scholars:
        raise KeyError(f"Unknown scholar_id: {scholar_id}")

    held_statements: list[dict[str, Any]] = []
    transmitted_only: list[dict[str, Any]] = []
    scholar_positions: list[dict[str, Any]] = []

    tractates_root = project_root / "tractates"
    for t_dir in sorted(tractates_root.iterdir()):
        if not t_dir.is_dir():
            continue
        for st in load_jsonl(t_dir / "statements.jsonl"):
            is_holder = scholar_id in st["attributed_to_ids"]
            is_transmitter = (
                st.get("reported_by_id") == scholar_id
                or scholar_id in st.get("transmission_chain_ids", [])
            ) and not is_holder
            if is_holder:
                held_statements.append(st)
            elif is_transmitter:
                transmitted_only.append(st)

        for po in load_jsonl(t_dir / "positions.jsonl"):
            if scholar_id in po["holder_ids"]:
                scholar_positions.append(po)

    return {
        "scholar": scholars[scholar_id],
        "held_statements_count": len(held_statements),
        "transmitted_only_count": len(transmitted_only),
        "positions_count": len(scholar_positions),
        "held_statements": held_statements,
        "transmitted_only_statements": transmitted_only,
        "positions": scholar_positions,
        "caveat": (
            "Provisional AI-annotated corpus slice; check interpretation_status and position_status "
            "(rejected, inverted_candidate, conditional, reconciled_compatible) before treating any "
            "entry as an accepted personal decision in H_s."
        ),
    }


def derive_eligible_qa_candidates(project_root: Path) -> list[dict[str, Any]]:
    """Derive source-blinded ML candidate Q-A items alongside separate evaluator-only evidence & caveats."""
    derived: list[dict[str, Any]] = []
    tractates_root = project_root / "tractates"
    for t_dir in sorted(tractates_root.iterdir()):
        if not t_dir.is_dir():
            continue
        questions = load_jsonl(t_dir / "questions.jsonl")
        positions_by_q: dict[str, list[dict[str, Any]]] = {}
        for po in load_jsonl(t_dir / "positions.jsonl"):
            positions_by_q.setdefault(po["question_id"], []).append(po)

        for q in questions:
            if not q["ml_prediction_eligible"]:
                continue
            q_positions = positions_by_q.get(q["question_id"], [])
            # Sort alternatives deterministically by content_sha256 so option order never encodes scholar order
            sorted_alts = sorted(q["candidate_alternatives"], key=lambda a: a["content_sha256"])
            derived.append(
                {
                    "parallel_family_id": q["parallel_family_id"],
                    "learner_blinded_input": {
                        "opaque_case_key": q["content_case_key"]
                        if "content_case_key" in q
                        else q["parallel_family_id"],
                        "neutral_question_he": q["neutral_question_he"],
                        "prerequisites_conditions_he": q["prerequisites_conditions_he"],
                        "answer_set_type": q["answer_set_type"],
                        "candidate_alternatives": sorted_alts,
                    },
                    "evaluator_only_grounding": {
                        "question_id": q["question_id"],
                        "sugya_id": q["sugya_id"],
                        "source_explicit_status": q["source_explicit_status"],
                        "justified_positions": [
                            {
                                "position_id": p["position_id"],
                                "holder_kind": p["holder_kind"],
                                "holder_ids": p["holder_ids"],
                                "alternative_id": p["alternative_id"],
                                "position_status": p["position_status"],
                                "conditions_he": p.get("conditions_he", []),
                                "statement_ids": p["statement_ids"],
                            }
                            for p in q_positions
                        ],
                        "caveats": [
                            "Provisional AI double-reviewed annotation; not human-expert certified.",
                            "Group by parallel_family_id before any train/dev/test split.",
                            "Literary memorization risk remains until evaluated against source-recognition controls.",
                        ],
                    },
                }
            )
    return derived
