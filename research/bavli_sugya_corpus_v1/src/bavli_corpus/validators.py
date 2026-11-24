"""JSON Schema + semantic & rabbinic attribution validator for Bavli Sugya Corpus v1."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from .normalization import project_canon_span_to_raw, sha256_str


COMPOUND_RAV_NAMES = (
    "רב יהודה",
    "רב אסי",
    "רב הונא",
    "רב חסדא",
    "רב נחמן",
    "רב ששת",
    "רב יוסף",
    "רב פפא",
    "רב זביד",
    "רב אשי",
    "רב כהנא",
    "רב יצחק",
    "רב מתנה",
    "רב דימי",
    "רב המנונא",
    "רב גידל",
    "רב קטינא",
    "רב עמרם",
    "רב ביבי",
    "רב הונא בר חיננא",
    "רב נחמן בר יצחק",
)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        s = line.strip()
        if not s:
            continue
        try:
            rows.append(json.loads(s))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON at {path}:{line_no}: {exc}") from exc
    return rows


def load_schema_validator(project_root: Path) -> Draft202012Validator:
    schema_path = project_root / "schemas" / "schema_v1.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def _has_standalone_rav(text: str) -> bool:
    """Return True if text mentions standalone 'רב' (not only compound 'רב פלוני')."""
    masked = text
    for cname in COMPOUND_RAV_NAMES:
        masked = masked.replace(cname, "___")
    return bool(re.search(r"(?<![א-ת])(ד?ל?כ?ו?ב?מ?רב)(?![א-ת])", masked))


def validate_tractate_bundle(
    project_root: Path,
    tractate_slug: str,
    scholars: list[dict[str, Any]],
    local_fulltext_by_id: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Validate all JSONL layers, exact character offsets, and rabbinic safeguards for a tractate."""
    validator = load_schema_validator(project_root)
    errors: list[str] = []
    warnings: list[str] = []

    t_dir = project_root / "tractates" / tractate_slug
    manifest = json.loads((t_dir / "manifest.json").read_text(encoding="utf-8"))
    segments = load_jsonl(t_dir / "segments.jsonl")
    sugyot = load_jsonl(t_dir / "sugyot.jsonl")
    statements = load_jsonl(t_dir / "statements.jsonl")
    questions = load_jsonl(t_dir / "questions.jsonl")
    positions = load_jsonl(t_dir / "positions.jsonl")
    relations = load_jsonl(t_dir / "relations.jsonl")
    reviews = load_jsonl(t_dir / "review_queue.jsonl")

    # 1. JSON Schema validation across all records
    for layer_name, recs in [
        ("scholars", scholars),
        ("segments", segments),
        ("sugyot", sugyot),
        ("statements", statements),
        ("questions", questions),
        ("positions", positions),
        ("relations", relations),
        ("reviews", reviews),
    ]:
        for idx, rec in enumerate(recs):
            for err in validator.iter_errors(rec):
                errors.append(f"[schema:{layer_name}[{idx}]] {err.message}")

    # 2. Scholar registry invariants (Anonymous Stam is NEVER a named scholar)
    scholar_by_id: dict[str, dict[str, Any]] = {}
    for sc in scholars:
        sid = sc["scholar_id"]
        if sid in scholar_by_id:
            errors.append(f"[scholars] Duplicate scholar_id: {sid}")
        scholar_by_id[sid] = sc
        if "stam" in sid.lower() or sc["canonical_name_he"].strip() in ("סתמא דגמרא", "סתם"):
            errors.append(f"[scholars] Anonymous Stam must not be registered as a scholar: {sid}")

    # 3. Segment inventory completeness & reversible offset_map check
    if len(segments) != manifest["total_tractate_segments"]:
        errors.append(
            f"[segments] Count {len(segments)} != manifest.total_tractate_segments {manifest['total_tractate_segments']}"
        )
    seg_by_id: dict[str, dict[str, Any]] = {}
    for expected_ord, seg in enumerate(segments):
        sid = seg["segment_id"]
        if sid in seg_by_id:
            errors.append(f"[segments] Duplicate segment_id: {sid}")
        if seg["ordinal_in_tractate"] != expected_ord:
            errors.append(f"[segments] Non-contiguous ordinal on {sid}: {seg['ordinal_in_tractate']} != {expected_ord}")
        if seg.get("raw_text") is not None or seg.get("canonical_text") is not None:
            errors.append(f"[segments] Repo-facing segments.jsonl must omit CC-BY-NC full text on {sid}")
        seg_by_id[sid] = seg

        if local_fulltext_by_id and sid in local_fulltext_by_id:
            lseg = local_fulltext_by_id[sid]
            raw_t = lseg["raw_text"]
            canon_t = lseg["canonical_text"]
            if sha256_str(raw_t) != seg["raw_sha256"]:
                errors.append(f"[segments] raw_sha256 mismatch on {sid}")
            if sha256_str(canon_t) != seg["canonical_sha256"]:
                errors.append(f"[segments] canonical_sha256 mismatch on {sid}")
            try:
                r_s, r_e = project_canon_span_to_raw(seg["offset_map"], 0, len(canon_t))
                if not (0 <= r_s < r_e <= len(raw_t)):
                    errors.append(f"[segments] Reversible offset_map out of bounds on {sid}")
            except ValueError as exc:
                errors.append(f"[segments] offset_map failure on {sid}: {exc}")

    # Determine target annotated segment IDs from manifest.annotation_scope
    scope = manifest.get("annotation_scope", {})
    scope_mode = scope.get("mode", "source_inventory_only")
    if scope_mode == "source_inventory_only":
        return {
            "tractate": manifest["tractate"],
            "mode": scope_mode,
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
        }

    covered_dafs = set(scope.get("covered_dafs", []))
    target_segments = (
        [s for s in segments if s["daf"] in covered_dafs]
        if scope_mode == "pilot_daf_slice"
        else list(segments)
    )
    target_seg_ids = [s["segment_id"] for s in target_segments]
    target_seg_set = set(target_seg_ids)

    # Index review queue targets for unaligned spans & unresolved chad_amar checks
    open_review_targets = {
        rv["target_id"] for rv in reviews if rv.get("status") in ("open", "escalated")
    }
    all_review_targets = {rv["target_id"] for rv in reviews}

    # Check review queue human-vs-AI truthfulness
    for rv in reviews:
        if rv.get("review_level") in ("human_reviewed", "human_independent_double"):
            has_human = any(h.get("actor_type") == "human_expert" for h in rv.get("history", []))
            if not has_human:
                errors.append(f"[reviews] {rv['review_id']} claims human review without human_expert history")

    # Helper to validate anchor list
    def check_anchors(owner_id: str, anchors: list[dict[str, Any]]) -> None:
        for anc in anchors:
            asid = anc["segment_id"]
            if asid not in seg_by_id:
                errors.append(f"[anchor:{owner_id}] Unknown segment_id {asid}")
                continue
            seg_meta = seg_by_id[asid]
            a_status = anc.get("alignment_status", "exact")
            s_c, e_c = anc["start_char"], anc["end_char"]
            q_str = anc.get("quote")
            q_hash = anc.get("quote_sha256")
            if q_str is not None and q_hash is not None and sha256_str(q_str) != q_hash:
                errors.append(f"[anchor:{owner_id}] quote_sha256 mismatch on {asid}")
            if a_status == "unaligned_needs_review":
                if s_c is not None or e_c is not None:
                    errors.append(
                        f"[anchor:{owner_id}] unaligned_needs_review must set start_char=null, end_char=null (no pseudo-precise offsets)"
                    )
                if owner_id not in open_review_targets:
                    errors.append(
                        f"[anchor:{owner_id}] unaligned anchor must have an open review_queue record"
                    )
            else:
                if s_c is None or e_c is None or not (0 <= s_c < e_c <= seg_meta["canonical_char_len"]):
                    errors.append(
                        f"[anchor:{owner_id}] Invalid char span [{s_c}, {e_c}) vs canonical_char_len={seg_meta['canonical_char_len']} on {asid}"
                    )
                    continue
                if q_str is not None and len(q_str) != (e_c - s_c):
                    errors.append(
                        f"[anchor:{owner_id}] Quote length {len(q_str)} != span length {e_c - s_c} on {asid}"
                    )
                if local_fulltext_by_id and asid in local_fulltext_by_id:
                    canon_t = local_fulltext_by_id[asid]["canonical_text"]
                    actual_sub = canon_t[s_c:e_c]
                    if q_str is not None and actual_sub != q_str:
                        errors.append(
                            f"[anchor:{owner_id}] Substring mismatch on {asid}[{s_c}:{e_c}]: got {actual_sub!r} != {q_str!r}"
                        )
                    # Verify reversible projection to raw_text
                    try:
                        project_canon_span_to_raw(seg_meta["offset_map"], s_c, e_c)
                    except ValueError as exc:
                        errors.append(f"[anchor:{owner_id}] Raw projection error on {asid}: {exc}")

    # 4. Sugya partition & hierarchy invariants
    sugya_by_id: dict[str, dict[str, Any]] = {}
    top_sugyot: list[dict[str, Any]] = []
    sub_sugyot: list[dict[str, Any]] = []
    for sg in sugyot:
        sgid = sg["sugya_id"]
        if sgid in sugya_by_id:
            errors.append(f"[sugyot] Duplicate sugya_id: {sgid}")
        sugya_by_id[sgid] = sg
        if sg["review_status"] in ("human_reviewed", "scholarly_confirmed"):
            errors.append(f"[sugyot] AI-only run cannot claim {sg['review_status']} on {sgid}")
        if sg["level"] == "top":
            top_sugyot.append(sg)
            if sg["parent_sugya_id"] is not None:
                errors.append(f"[sugyot] Top-level sugya {sgid} must have parent_sugya_id=null")
        else:
            sub_sugyot.append(sg)

        sids = sg["ordered_segment_ids"]
        for sid in sids:
            if sid not in seg_by_id:
                errors.append(f"[sugyot] Unknown segment_id {sid} in {sgid}")
        if all(sid in seg_by_id for sid in sids):
            ords = [seg_by_id[sid]["ordinal_in_tractate"] for sid in sids]
            if ords != list(range(ords[0], ords[0] + len(ords))):
                errors.append(f"[sugyot] Non-contiguous segments in {sgid}")
            if seg_by_id[sids[0]]["ref"] != sg["start_ref"]:
                errors.append(f"[sugyot] start_ref mismatch on {sgid}")
            if seg_by_id[sids[-1]]["ref"] != sg["end_ref"]:
                errors.append(f"[sugyot] end_ref mismatch on {sgid}")
        for cue_k in ("boundary_start_cue", "boundary_end_cue"):
            anc = sg[cue_k].get("anchor")
            if anc:
                check_anchors(sgid, [anc])

    partition_sids = [sid for sg in top_sugyot for sid in sg["ordered_segment_ids"]]
    if partition_sids != target_seg_ids:
        errors.append(
            f"[sugyot] Top-level sugyot do not exactly partition target segments "
            f"(got {len(partition_sids)} segs vs expected {len(target_seg_ids)})"
        )

    for sub in sub_sugyot:
        pid = sub["parent_sugya_id"]
        if pid not in sugya_by_id or sugya_by_id[pid]["level"] != "top":
            errors.append(f"[sugyot] Sub-sugya {sub['sugya_id']} has invalid parent {pid}")
        else:
            parent_set = set(sugya_by_id[pid]["ordered_segment_ids"])
            if not set(sub["ordered_segment_ids"]).issubset(parent_set):
                errors.append(f"[sugyot] Sub-sugya {sub['sugya_id']} escapes parent {pid}")

    # 5. Statements & rabbinic attribution safeguards
    stmt_by_id: dict[str, dict[str, Any]] = {}
    for st in statements:
        stid = st["statement_id"]
        if stid in stmt_by_id:
            errors.append(f"[statements] Duplicate statement_id: {stid}")
        stmt_by_id[stid] = st
        if st["sugya_id"] not in sugya_by_id:
            errors.append(f"[statements] {stid} references unknown sugya_id {st['sugya_id']}")
        if st.get("sub_sugya_id") and st["sub_sugya_id"] not in sugya_by_id:
            errors.append(f"[statements] {stid} references unknown sub_sugya_id {st['sub_sugya_id']}")

        check_anchors(stid, st["source_spans"])
        if st["alignment_status"] == "unaligned_needs_review" and stid not in open_review_targets:
            errors.append(f"[statements] Unaligned statement {stid} missing from open review_queue")

        # Validate scholar references
        for ref_sid in (
            ([st["speaker_id"]] if st["speaker_id"] else [])
            + ([st["reported_by_id"]] if st["reported_by_id"] else [])
            + st.get("transmission_chain_ids", [])
            + st["attributed_to_ids"]
        ):
            if ref_sid not in scholar_by_id:
                errors.append(f"[statements] {stid} references unknown scholar_id {ref_sid}")

        # Safeguard A: Anonymous Stam must never have named speaker/authority
        if st["speaker_kind"] == "anonymous_stam" or st["attribution_type"] == "anonymous_stam":
            if st["speaker_id"] is not None or st["attributed_to_ids"]:
                errors.append(
                    f"[rabbinic:stam] {stid} assigns named speaker/holder to anonymous_stam"
                )

        # Safeguard B: Unresolved chad_amar must not assign named views by order
        if (
            st["speaker_kind"] == "unresolved_chad_amar"
            or st["attribution_type"] == "unresolved_chad_amar"
        ):
            if st["attributed_to_ids"]:
                errors.append(
                    f"[rabbinic:chad_amar] {stid} assigns named attributed_to_ids on unresolved chad_amar"
                )
            if stid not in all_review_targets and st["sugya_id"] not in all_review_targets:
                errors.append(
                    f"[rabbinic:chad_amar] {stid} unresolved chad_amar must appear in review_queue"
                )

        # Safeguard C: Transmission role separation
        if st["attribution_type"] == "explicit_transmitted":
            if not st["reported_by_id"]:
                errors.append(
                    f"[rabbinic:transmission] {stid} has explicit_transmitted without reported_by_id"
                )
            elif st["reported_by_id"] in st["attributed_to_ids"]:
                errors.append(
                    f"[rabbinic:transmission] {stid} conflates transmitter {st['reported_by_id']} with attributed authority"
                )

        # Safeguard D: Homonym & orthography collision checks on direct speaker_id
        q = st["source_quote"]
        direct_ids = [st["speaker_id"]] if st["speaker_id"] else []
        if "scholar:amora:rava" in direct_ids and "רבה" in q and "רבא" not in q:
            if st["attribution_type"] != "textual_variant" or not st.get("textual_variant_notes"):
                errors.append(
                    f"[rabbinic:rabbah_rava] {stid} assigns Rava (רבא) to quote mentioning only רבה without textual_variant note"
                )
        if "scholar:amora:rabbah" in direct_ids and "רבא" in q and "רבה" not in q:
            if st["attribution_type"] != "textual_variant" or not st.get("textual_variant_notes"):
                errors.append(
                    f"[rabbinic:rabbah_rava] {stid} assigns Rabbah (רבה) to quote mentioning only רבא without textual_variant note"
                )
        if "scholar:amora:rav" in direct_ids and "רב" in q and not _has_standalone_rav(q):
            errors.append(
                f"[rabbinic:rav_compound] {stid} assigns standalone Rav to a compound name ({q!r})"
            )
        if "scholar:amora:rabbi_yohanan" in (direct_ids + st["attributed_to_ids"]) and "יוחנן הסנדלר" in q:
            errors.append(
                f"[rabbinic:yohanan_hasandlar] {stid} conflates Rabbi Yohanan HaSandlar with Amora Rabbi Yohanan"
            )

    # 6. Questions & Positions invariants
    q_by_id: dict[str, dict[str, Any]] = {}
    for qu in questions:
        qid = qu["question_id"]
        if qid in q_by_id:
            errors.append(f"[questions] Duplicate question_id: {qid}")
        q_by_id[qid] = qu
        if qu["sugya_id"] not in sugya_by_id:
            errors.append(f"[questions] {qid} unknown sugya_id {qu['sugya_id']}")
        for esid in qu["evidence_statement_ids"]:
            if esid not in stmt_by_id:
                errors.append(f"[questions] {qid} unknown evidence_statement_id {esid}")
        check_anchors(qid, qu["source_spans"])
        # ML source-blinded eligibility check: neutral_question_he must not leak explicit daf ref
        if qu["ml_prediction_eligible"]:
            if len(qu["candidate_alternatives"]) < 2:
                errors.append(
                    f"[questions:ml] {qid} marked ml_prediction_eligible=True with <2 candidate_alternatives"
                )

    pos_by_id: dict[str, dict[str, Any]] = {}
    for po in positions:
        pid = po["position_id"]
        if pid in pos_by_id:
            errors.append(f"[positions] Duplicate position_id: {pid}")
        pos_by_id[pid] = po
        qid = po["question_id"]
        if qid not in q_by_id:
            errors.append(f"[positions] {pid} references unknown question_id {qid}")
        else:
            valid_alts = {a["alternative_id"] for a in q_by_id[qid]["candidate_alternatives"]}
            if po.get("alternative_id") and po["alternative_id"] not in valid_alts:
                errors.append(
                    f"[positions] {pid} alternative_id {po['alternative_id']} not in {qid} alternatives"
                )
        if po["sugya_id"] not in sugya_by_id:
            errors.append(f"[positions] {pid} unknown sugya_id {po['sugya_id']}")
        check_anchors(pid, po["source_spans"])

        for h_id in po["holder_ids"] + po.get("transmitted_via_ids", []):
            if h_id not in scholar_by_id:
                errors.append(f"[positions] {pid} unknown scholar_id {h_id}")

        if po["holder_kind"] == "unresolved_chad_amar" and po["holder_ids"]:
            errors.append(f"[rabbinic:chad_amar] {pid} assigns holder_ids to unresolved_chad_amar")
        if po["holder_kind"] == "anonymous_stam" and po["holder_ids"]:
            errors.append(f"[rabbinic:stam] {pid} assigns holder_ids to anonymous_stam")

        linked_stmts: list[dict[str, Any]] = []
        for stid in po["statement_ids"] + po.get("reason_statement_ids", []):
            if stid not in stmt_by_id:
                errors.append(f"[positions] {pid} references unknown statement_id {stid}")
            elif stid in po["statement_ids"]:
                linked_stmts.append(stmt_by_id[stid])

        # Safeguard E: No unmentioned scholar imputed from silence
        if po["holder_ids"] and linked_stmts:
            mentioned_scholars = set()
            for ls in linked_stmts:
                mentioned_scholars.update(ls["attributed_to_ids"])
                if ls["speaker_id"]:
                    mentioned_scholars.add(ls["speaker_id"])
            unjustified = set(po["holder_ids"]) - mentioned_scholars
            if unjustified:
                errors.append(
                    f"[rabbinic:no_silence_imputation] {pid} assigns holder_ids {sorted(unjustified)} not grounded in linked statements"
                )

        # Safeguard F: Refuted/retracted statements cannot yield 'asserted' position_status
        if linked_stmts and all(
            ls["interpretation_status"] in ("refuted_tiyuvta", "retracted_hadar_beh")
            for ls in linked_stmts
        ):
            if po["position_status"] == "asserted":
                errors.append(
                    f"[rabbinic:rejected_status] {pid} marks refuted/retracted statement as accepted 'asserted' position"
                )

        # Safeguard G: Hilkheta conclusion is not automatically a scholar's personal asserted view
        if linked_stmts and all(
            ls["interpretation_status"] == "halakhic_conclusion_hilkheta"
            and ls["speaker_kind"] == "anonymous_stam"
            for ls in linked_stmts
        ):
            if po["holder_ids"] and po["position_status"] != "halakhic_ruling":
                errors.append(
                    f"[rabbinic:hilkheta] {pid} conflates anonymous hilkheta conclusion with personal scholar assertion"
                )

    # 7. Relations invariants
    valid_entity_ids = set(stmt_by_id) | set(pos_by_id) | set(sugya_by_id) | set(q_by_id)
    rel_ids: set[str] = set()
    for rl in relations:
        rid = rl["relation_id"]
        if rid in rel_ids:
            errors.append(f"[relations] Duplicate relation_id: {rid}")
        rel_ids.add(rid)
        if rl["from_id"] not in valid_entity_ids:
            errors.append(f"[relations] {rid} unknown from_id {rl['from_id']}")
        if rl["to_id"] not in valid_entity_ids:
            errors.append(f"[relations] {rid} unknown to_id {rl['to_id']}")
        check_anchors(rid, rl["source_spans"])

    # Compute summary denominators
    ambig_sugyot = sum(
        1
        for s in top_sugyot
        if s["boundary_status"] in ("ambiguous", "unresolved_pending_adjudication", "window_edge_pending")
    )
    named_stmts = sum(1 for st in statements if st["attributed_to_ids"])
    ambig_stmts = sum(
        1
        for st in statements
        if st["attribution_type"] in ("unresolved_chad_amar", "disputed_inversion", "textual_variant")
    )

    return {
        "tractate": manifest["tractate"],
        "slug": tractate_slug,
        "mode": scope_mode,
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "metrics": {
            "total_tractate_segments": len(segments),
            "target_covered_segments": len(target_seg_ids),
            "top_level_sugyot": len(top_sugyot),
            "sub_sugyot": len(sub_sugyot),
            "cross_amud_top_sugyot": sum(1 for s in top_sugyot if s["crosses_amud"]),
            "cross_daf_top_sugyot": sum(1 for s in top_sugyot if s["crosses_daf"]),
            "uncertain_or_edge_boundary_sugyot": ambig_sugyot,
            "uncertain_boundary_fraction": round(ambig_sugyot / len(top_sugyot), 4) if top_sugyot else 0.0,
            "statements_count": len(statements),
            "named_authority_statements": named_stmts,
            "anonymous_stam_statements": sum(1 for st in statements if st["speaker_kind"] == "anonymous_stam"),
            "ambiguous_or_variant_statements": ambig_stmts,
            "questions_count": len(questions),
            "ml_eligible_questions": sum(1 for q in questions if q["ml_prediction_eligible"]),
            "positions_count": len(positions),
            "relations_count": len(relations),
            "review_queue_count": len(reviews),
            "open_reviews_count": sum(1 for r in reviews if r["status"] == "open"),
        },
    }
