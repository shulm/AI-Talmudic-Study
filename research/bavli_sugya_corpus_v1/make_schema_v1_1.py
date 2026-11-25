"""Operational Schema v1.1.0 generator: backward-compatible extension of PR #10 schema_v1.json (1.0.0).

Preserves schema_v1.json untouched for historical 1.0.0 pilot verification while defining
schema_v1_1.json for cumulative pilot + continuation validation.
"""
from __future__ import annotations

import pipeline as p

S = {"type": "string"}
N = {"type": ["string", "null"]}
B = {"type": "boolean"}
A = {"type": "array", "items": S}

E = {
    "type": "array",
    "minItems": 1,
    "items": {
        "type": "object",
        "additionalProperties": False,
        "required": ["segment_id", "ref", "start_char", "end_char", "quote", "source_sha256"],
        "properties": {
            "segment_id": S,
            "ref": S,
            "start_char": {"type": "integer", "minimum": 0},
            "end_char": {"type": "integer", "minimum": 0},
            "quote": S,
            "source_sha256": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
        },
    },
}

NAME_MENTION = {
    "type": "object",
    "additionalProperties": False,
    "required": ["scholar_id", "name_he", "role", "attribution_status", "transmitter_ids", "candidate_ids", "evidence"],
    "properties": {
        "scholar_id": N,
        "name_he": S,
        "role": {
            "enum": [
                "speaker",
                "attributed_authority",
                "transmitter",
                "quoted_authority",
                "unresolved_candidate_group",
                "interlocutor",
            ]
        },
        "attribution_status": {
            "enum": [
                "explicit_name",
                "transmitted",
                "unresolved_alternatives",
                "variant_attribution",
            ]
        },
        "transmitter_ids": A,
        "candidate_ids": A,
        "note_he": N,
        "evidence": E,
    },
}

PENDING_CONTINUATION = {
    "type": "object",
    "additionalProperties": False,
    "required": ["is_open", "direction", "next_unprocessed_ref", "context_preview_refs", "note_he"],
    "properties": {
        "is_open": B,
        "direction": {"enum": ["none", "left", "right", "both"]},
        "next_unprocessed_ref": N,
        "context_preview_refs": A,
        "note_he": N,
    },
}

LINEAGE = {
    "type": "object",
    "additionalProperties": False,
    "required": ["origin_block_id", "updated_in_block_id", "previous_record_sha256", "supersedes_ids"],
    "properties": {
        "origin_block_id": S,
        "updated_in_block_id": S,
        "previous_record_sha256": N,
        "supersedes_ids": A,
    },
}


def obj(properties: dict, required: list[str] | None = None) -> dict:
    return {
        "type": "object",
        "additionalProperties": False,
        "required": required if required is not None else list(properties),
        "properties": properties,
    }


def make_v1_1() -> dict:
    v1 = p.read(p.HERE / "schema_v1.json")
    v1_defs = v1["$defs"]

    seg_v1_1 = obj(
        {
            "schema_version": {"enum": ["1.0.0", "1.1.0"]},
            "id": S,
            "tractate": S,
            "ref": S,
            "source_index": {
                "type": "array",
                "prefixItems": [{"type": "integer", "minimum": 0}, {"type": "integer", "minimum": 0}],
                "minItems": 2,
                "maxItems": 2,
            },
            "text": S,
            "text_sha256": S,
            "source_sha256": S,
            "version_title": S,
            "scope": {"enum": ["pilot", "core", "context_only"]},
            "block_id": S,
            "promoted_from_context": B,
        },
        required=[
            "schema_version",
            "id",
            "tractate",
            "ref",
            "source_index",
            "text",
            "text_sha256",
            "source_sha256",
            "version_title",
            "scope",
        ],
    )

    sugya_v1_1 = obj(
        {
            "schema_version": {"const": "1.1.0"},
            "id": S,
            "review_status": {"const": "ai_provisional"},
            "ml_eligible": {"const": False},
            "authoring_key": S,
            "block_id": S,
            "tractate": S,
            "title_he": S,
            "summary_he": S,
            "summary_origin": {"const": "editorial_paraphrase"},
            "level": {"enum": ["primary", "sub_sugya"]},
            "parent_id": N,
            "segment_ids": A,
            "start_ref": S,
            "end_ref": S,
            "boundary_status": {"enum": ["provisional", "open_left", "open_right", "open_both"]},
            "pending_continuation": PENDING_CONTINUATION,
            "boundary_rationale": S,
            "conditions": A,
            "family_id": S,
            "family_status": S,
            "annotation_completeness": {
                "enum": ["selected_claims_only", "minimal_sugya_layer_qa_deferred"]
            },
            "construction_status": {
                "enum": [
                    "provisional_segmented",
                    "provisional_extended_open_tail",
                    "provisional_open_tail",
                ]
            },
            "extraction_status": {
                "enum": [
                    "minimal_sugya_layer_only_qa_deferred",
                    "selected_claims_and_names_qa_deferred",
                ]
            },
            "span_review_status": {
                "enum": [
                    "independent_source_reviewed",
                    "independent_source_reviewed_with_disagreement",
                    "partial_span_reviewed",
                    "constructed_unreviewed",
                ]
            },
            "uncertainty_notes_he": A,
            "review_item_ids": A,
            "name_mentions": {"type": "array", "items": NAME_MENTION},
            "lineage": LINEAGE,
            "evidence": E,
        }
    )

    scholar_v1_1 = obj(
        {
            **v1_defs["scholars"]["properties"],
            "schema_version": {"enum": ["1.0.0", "1.1.0"]},
            "block_id": S,
        },
        required=v1_defs["scholars"]["required"],
    )

    statement_v1_1 = obj(
        {
            **v1_defs["statements"]["properties"],
            "schema_version": {"enum": ["1.0.0", "1.1.0"]},
            "block_id": S,
        },
        required=v1_defs["statements"]["required"],
    )

    review_v1_1 = obj(
        {
            "schema_version": {"enum": ["1.0.0", "1.1.0"]},
            "id": S,
            "review_status": {"const": "ai_provisional"},
            "ml_eligible": {"const": False},
            "block_id": S,
            "target_ids": A,
            "issue_type": {
                "enum": [
                    "semantic_extraction_pending",
                    "boundary_and_family_review",
                    "unresolved_attribution",
                    "boundary_disagreement_preserved",
                    "open_tail_continuation_pending",
                    "textual_variant_or_homonym",
                ]
            },
            "severity": {"const": "blocks_ml"},
            "status": {"enum": ["open", "superseded_by_extension"]},
            "description_he": S,
            "evidence": E,
        },
        required=[
            "schema_version",
            "id",
            "review_status",
            "ml_eligible",
            "target_ids",
            "issue_type",
            "severity",
            "status",
            "description_he",
            "evidence",
        ],
    )

    defs = {
        "segments_v1": v1_defs["segments"],
        "sugyot_v1": v1_defs["sugyot"],
        "questions_v1": v1_defs["questions"],
        "positions_v1": v1_defs["positions"],
        "relations_v1": v1_defs["relations"],
        "segments": seg_v1_1,
        "sugyot": {"oneOf": [{"$ref": "#/$defs/sugyot_v1"}, sugya_v1_1]},
        "scholars": scholar_v1_1,
        "statements": statement_v1_1,
        "questions": v1_defs["questions"],
        "positions": v1_defs["positions"],
        "relations": obj(
            {
                **v1_defs["relations"]["properties"],
                "schema_version": {"enum": ["1.0.0", "1.1.0"]},
                "block_id": S,
            },
            required=v1_defs["relations"]["required"],
        ),
        "review_queue": review_v1_1,
    }

    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "urn:ai-talmudic-study:bavli-sugya:1.1.0",
        "title": "Operational Bavli sugya continuation contract v1.1.0 (backward-compatible with pilot v1.0.0)",
        "$defs": defs,
        "oneOf": [{"$ref": "#/$defs/" + t} for t in p.TABLES],
    }
    p.write(p.HERE / "schema_v1_1.json", schema)
    return schema


if __name__ == "__main__":
    make_v1_1()
