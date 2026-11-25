"""Safe, staging-validated, transactional block continuation engine for Bavli Sugya Corpus.

Builds directly on PR #10 (ef29310, Wikisource Talmud Bavli edition, existing stable IDs).
Preserves all unaffected 1.0.0 pilot records byte-for-byte and keeps historical ML/expansion gates false.
"""
from __future__ import annotations

import copy
import json
import os
import re
import shutil
import uuid
from pathlib import Path
from typing import Any

import jsonschema
import pipeline as p
import make_schema_v1_1


DAF_RE = re.compile(r"^(\d+)([ab])$")


class SourceIntegrityError(RuntimeError):
    """Raised when source files, TOC, or segment hashes diverge from pinned source_manifest.json."""


class ConflictingBlockError(RuntimeError):
    """Raised when a block conflicts with an already-accepted block or overlapping core coverage."""


class ValidationGateError(RuntimeError):
    """Raised when staged cumulative outputs fail schema, byte-preservation, lineage, or span-review checks."""


def daf_to_page_index(daf_or_idx: str | int) -> int:
    if isinstance(daf_or_idx, int):
        return daf_or_idx
    s = str(daf_or_idx).strip()
    if s.isdigit():
        return int(s)
    m = DAF_RE.fullmatch(s)
    if not m:
        raise ValueError(f"Invalid daf or page index: {daf_or_idx!r}")
    folio, side = int(m.group(1)), m.group(2)
    if folio < 2:
        raise ValueError(f"Invalid Bavli folio < 2: {daf_or_idx!r}")
    return (folio - 1) * 2 + (1 if side == "b" else 0)


def page_index_to_daf(idx: int) -> str:
    return f"{idx // 2 + 1}{'a' if idx % 2 == 0 else 'b'}"


def canon_json_bytes(rec: dict[str, Any]) -> bytes:
    return (json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")


def rec_sha256(rec: dict[str, Any]) -> str:
    return p.sha(canon_json_bytes(rec))


def ensure_ledger(base_dir: Path) -> dict[str, Any]:
    ledger_path = base_dir / "block_ledger.json"
    if ledger_path.exists():
        return p.read(ledger_path)
    segs = p.rows(base_dir / "data/segments.jsonl")
    sugs = p.rows(base_dir / "data/sugyot.jsonl")
    open_tails = [
        {
            "id": g["id"],
            "authoring_key": g["authoring_key"],
            "tractate": g["tractate"],
            "start_ref": g["start_ref"],
            "end_ref": g["end_ref"],
            "boundary_status": g["boundary_status"],
        }
        for g in sugs
        if g["level"] == "primary" and g["boundary_status"] in ("open_right", "open_left", "open_both")
    ]
    ledger = {
        "ledger_schema_version": "1.1.0",
        "baseline_commit": "ef29310b50575ac2441ce59d0c68d58424f4b823",
        "edition": p.VERSION,
        "historical_pilot_gates": {
            "semantic_completeness_pass": False,
            "expansion_gate_pass": False,
            "ml_eligible_records": 0,
            "note": "Historical full-semantics/ML gate from PR #10 remains false; current phase is provisional sugya segmentation only.",
        },
        "blocks": [
            {
                "block_id": "pilot_baseline_ef29310",
                "phase": "bounded_pilot_v1",
                "tractates": {"Berakhot": "2a-5a", "Bava Metzia": "21a-22b"},
                "core_segments_added": len(segs),
                "cumulative_core_segments": len(segs),
                "open_tails_after_block": open_tails,
                "accepted": True,
            }
        ],
    }
    p.write(ledger_path, ledger)
    return ledger


def build_reading_packets(ordered_segments: list[dict[str, Any]], max_segs: int = 10, max_chars: int = 8000) -> list[dict[str, Any]]:
    packets: list[dict[str, Any]] = []
    start = 0
    while start < len(ordered_segments):
        end = start
        size = 0
        while end < len(ordered_segments) and (end - start) < max_segs and (
            size + len(ordered_segments[end]["text"]) <= max_chars or end == start
        ):
            size += len(ordered_segments[end]["text"])
            end += 1
        selected = ordered_segments[start:end]
        packets.append(
            {
                "packet_index": len(packets) + 1,
                "segment_ids": [r["id"] for r in selected],
                "start_ref": selected[0]["ref"],
                "end_ref": selected[-1]["ref"],
                "characters": size,
                "oversized_atomic_segment": size > max_chars,
            }
        )
        if end == len(ordered_segments):
            break
        start = max(start + 1, end - 2)
    return packets


def prepare_block_input(
    base_dir: Path,
    source_root: Path,
    block_id: str,
    tractate: str,
    core_start: str | int,
    core_end: str | int,
    context_before_pages: int = 1,
    context_after_pages: int = 1,
) -> dict[str, Any]:
    """Build immutable block input packet, automatically extending back to cover full inherited open-tail spans."""
    manifest = p.read(base_dir / "source_manifest.json")
    toc_bytes = (source_root / manifest["source_toc_path"]).read_bytes()
    if p.sha(toc_bytes) != manifest["source_toc_sha256"]:
        raise SourceIntegrityError("TOC SHA-256 mismatch against pinned source_manifest.json")

    meta = next((m for m in manifest["tractates"] if m["title"] == tractate), None)
    if meta is None:
        raise ValueError(f"Unknown tractate: {tractate!r}")

    src_path = source_root / meta["source_path"]
    if not src_path.exists():
        raise SourceIntegrityError(f"Pinned Wikisource file missing: {src_path}")
    src_bytes = src_path.read_bytes()
    if p.sha(src_bytes) != meta["source_sha256"]:
        raise SourceIntegrityError(f"Source SHA-256 mismatch for {tractate}!")

    raw_doc = p.read(src_path)
    lo = daf_to_page_index(core_start)
    hi = daf_to_page_index(core_end)
    if not (2 <= lo <= hi < len(raw_doc["text"])):
        raise ValueError(f"Invalid core page range [{lo}, {hi}] for {tractate}")

    existing_segs = {s["id"]: s for s in p.rows(base_dir / "data/segments.jsonl")}
    existing_ctx = {s["id"]: s for s in p.rows(base_dir / "context/segments.jsonl")}
    existing_sugs = p.rows(base_dir / "data/sugyot.jsonl")

    # Find inherited open_right / open_both unit in this tractate ending immediately before `lo`
    prev_nonempty_idx = max((i for i in range(0, lo) if raw_doc["text"][i]), default=None)
    inherited_open_tail: dict[str, Any] | None = None
    earliest_needed_page = max(2, lo - context_before_pages)

    if prev_nonempty_idx is not None:
        last_prev_ref = p.address(tractate, prev_nonempty_idx, len(raw_doc["text"][prev_nonempty_idx]) - 1)
        for g in existing_sugs:
            if (
                g["tractate"] == tractate
                and g["level"] == "primary"
                and g["end_ref"] == last_prev_ref
                and g["boundary_status"] in ("open_right", "open_both")
            ):
                tail_segs = [existing_segs[sid] for sid in g["segment_ids"]]
                tail_start_page = tail_segs[0]["source_index"][0]
                # CRITICAL RULE: Always read the full inherited open-tail source span,
                # even when it begins before the default preceding context!
                earliest_needed_page = min(earliest_needed_page, tail_start_page)
                inherited_open_tail = {
                    "id": g["id"],
                    "authoring_key": g["authoring_key"],
                    "start_ref": g["start_ref"],
                    "end_ref": g["end_ref"],
                    "start_page_index": tail_start_page,
                    "extended_before_default_context": tail_start_page < max(2, lo - context_before_pages),
                    "segment_ids": list(g["segment_ids"]),
                    "boundary_status": g["boundary_status"],
                }
                break

    latest_context_page = min(len(raw_doc["text"]) - 1, hi + context_after_pages)
    inherited_ids = set(inherited_open_tail["segment_ids"]) if inherited_open_tail else set()

    packet_segments: list[dict[str, Any]] = []
    for i in range(earliest_needed_page, latest_context_page + 1):
        for j, txt in enumerate(raw_doc["text"][i]):
            sid = p.stable("seg", tractate, p.VERSION, str(i), str(j))
            ref = p.address(tractate, i, j)
            txt_hash = p.sha(txt.encode("utf-8"))
            if sid in existing_segs:
                if lo <= i <= hi:
                    raise ConflictingBlockError(f"Core segment {ref} ({sid}) is already in processed data/segments.jsonl!")
                if existing_segs[sid]["text_sha256"] != txt_hash:
                    raise SourceIntegrityError(f"Existing segment hash mismatch at {ref}")
            if sid in existing_ctx and existing_ctx[sid]["text_sha256"] != txt_hash:
                raise SourceIntegrityError(f"Existing context segment hash mismatch at {ref}")

            role = (
                "inherited_open_tail"
                if sid in inherited_ids
                else ("preceding_context" if i < lo else ("core" if i <= hi else "following_context"))
            )
            packet_segments.append(
                {
                    "id": sid,
                    "tractate": tractate,
                    "ref": ref,
                    "source_index": [i, j],
                    "role_in_block": role,
                    "previously_in": (
                        "processed_segments"
                        if sid in existing_segs
                        else ("context_only" if sid in existing_ctx else "unextracted")
                    ),
                    "text": txt,
                    "plain_reading_text": p.plain(txt),
                    "text_sha256": txt_hash,
                    "source_sha256": meta["source_sha256"],
                }
            )

    packets = build_reading_packets(packet_segments)
    return {
        "packet_schema_version": "1.1.0",
        "block_id": block_id,
        "tractate": tractate,
        "edition": p.VERSION,
        "source_sha256": meta["source_sha256"],
        "core_page_indices": list(range(lo, hi + 1)),
        "core_daf_range": f"{page_index_to_daf(lo)}-{page_index_to_daf(hi)}",
        "preceding_context_page_indices": list(range(earliest_needed_page, lo)),
        "following_context_page_indices": list(range(hi + 1, latest_context_page + 1)),
        "inherited_open_tail": inherited_open_tail,
        "counts": {
            "inherited_open_tail_segments": sum(s["role_in_block"] == "inherited_open_tail" for s in packet_segments),
            "preceding_context_segments": sum(s["role_in_block"] == "preceding_context" for s in packet_segments),
            "core_segments": sum(s["role_in_block"] == "core" for s in packet_segments),
            "following_context_segments": sum(s["role_in_block"] == "following_context" for s in packet_segments),
            "promoted_from_previous_context_only": sum(
                s["role_in_block"] == "core" and s["previously_in"] == "context_only"
                for s in packet_segments
            ),
            "sequential_reading_packets": len(packets),
        },
        "sequential_reading_packets": packets,
        "segments": packet_segments,
    }


def validate_v1_1(
    base_dir: Path,
    source_root: Path | None = None,
    check_source: bool = True,
) -> dict[str, Any]:
    """Validate cumulative dataset (pilot 1.0.0 + continuation 1.1.0) fail-closed."""
    schema_path = base_dir / "schema_v1_1.json"
    schema = p.read(schema_path)
    jsonschema.Draft202012Validator.check_schema(schema)

    data = {t: p.rows(base_dir / "data" / f"{t}.jsonl") for t in p.TABLES}
    contexts = p.rows(base_dir / "context/segments.jsonl")

    ids: dict[str, tuple[str, dict[str, Any]]] = {}
    for table, records in data.items():
        v = jsonschema.Draft202012Validator(
            {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": "#/$defs/" + table}
        )
        for rec in records:
            v.validate(rec)
            if rec["id"] in ids:
                raise ValidationGateError(f"Duplicate ID across tables: {rec['id']}")
            ids[rec["id"]] = (table, rec)
            if table != "segments":
                if rec.get("ml_eligible") is not False:
                    raise ValidationGateError(f"Record {rec['id']} violates ml_eligible=False!")
                if rec.get("review_status") != "ai_provisional":
                    raise ValidationGateError(f"Record {rec['id']} violates review_status='ai_provisional'!")

    seg_by_id = {s["id"]: s for s in data["segments"]}
    ctx_by_id = {s["id"]: s for s in contexts}
    if set(seg_by_id) & set(ctx_by_id):
        raise ValidationGateError(
            f"Context segment(s) simultaneously in data/segments.jsonl and context/segments.jsonl: {set(seg_by_id) & set(ctx_by_id)}"
        )
    allseg = {**seg_by_id, **ctx_by_id}

    manifest = p.read(base_dir / "source_manifest.json")
    meta = {m["title"]: m for m in manifest["tractates"]}
    if check_source and source_root is not None:
        if p.sha((source_root / manifest["source_toc_path"]).read_bytes()) != manifest["source_toc_sha256"]:
            raise SourceIntegrityError("TOC hash mismatch")
        originals = {}
        for m in meta.values():
            if p.sha((source_root / m["source_path"]).read_bytes()) != m["source_sha256"]:
                raise SourceIntegrityError(f"Source file hash mismatch: {m['title']}")
            if p.sha((source_root / m["schema_path"]).read_bytes()) != m["schema_sha256"]:
                raise SourceIntegrityError(f"Schema file hash mismatch: {m['title']}")
            originals[m["title"]] = p.read(source_root / m["source_path"])
        for s in allseg.values():
            i, j = s["source_index"]
            if s["text"] != originals[s["tractate"]]["text"][i][j]:
                raise SourceIntegrityError(f"Segment text altered at {s['ref']}")

    for s in allseg.values():
        i, j = s["source_index"]
        if s["ref"] != p.address(s["tractate"], i, j):
            raise ValidationGateError(f"Address offset error at {s['id']}: {s['ref']}")
        if s["id"] != p.stable("seg", s["tractate"], p.VERSION, str(i), str(j)):
            raise ValidationGateError(f"Unstable segment ID at {s['ref']}")
        if p.sha(s["text"].encode("utf-8")) != s["text_sha256"]:
            raise ValidationGateError(f"text_sha256 mismatch at {s['ref']}")
        if s["source_sha256"] != meta[s["tractate"]]["source_sha256"]:
            raise ValidationGateError(f"source_sha256 mismatch at {s['ref']}")

    if len({s["ref"] for s in seg_by_id.values()}) != len(seg_by_id):
        raise ValidationGateError("Duplicate segment ref in data/segments.jsonl")

    # Primary sugya exact partition + contiguity check
    groups = {g["id"]: g for g in data["sugyot"]}
    covered_counts: dict[str, int] = {}
    for g in groups.values():
        ss = [seg_by_id[sid] for sid in g["segment_ids"]]
        if not ss or len({s["tractate"] for s in ss}) != 1:
            raise ValidationGateError(f"Invalid segment_ids on sugya {g['id']}")
        if ss[0]["ref"] != g["start_ref"] or ss[-1]["ref"] != g["end_ref"]:
            raise ValidationGateError(f"start_ref/end_ref mismatch on sugya {g['id']}")
        expected = [
            s["id"]
            for s in sorted(
                (x for x in data["segments"] if x["tractate"] == g["tractate"]),
                key=lambda r: r["source_index"],
            )
            if ss[0]["source_index"] <= s["source_index"] <= ss[-1]["source_index"]
        ]
        if expected != g["segment_ids"]:
            raise ValidationGateError(f"Non-contiguous sugya segments on {g['id']}")
        if g["level"] == "primary":
            if g["parent_id"] is not None:
                raise ValidationGateError(f"Primary sugya {g['id']} has parent_id")
            for sid in g["segment_ids"]:
                covered_counts[sid] = covered_counts.get(sid, 0) + 1
        else:
            if g["parent_id"] not in groups or not (
                set(g["segment_ids"]) <= set(groups[g["parent_id"]]["segment_ids"])
            ):
                raise ValidationGateError(f"Sub-sugya {g['id']} outside parent")

        # Validate v1.1.0 sugya extra invariants (name_mentions, review_item_ids, pending_continuation)
        if g["schema_version"] == "1.1.0":
            for r_id in g["review_item_ids"]:
                if r_id not in ids or ids[r_id][0] != "review_queue":
                    raise ValidationGateError(f"Sugya {g['id']} links missing review_item_id {r_id}")
            pc = g["pending_continuation"]
            if (g["boundary_status"] in ("open_right", "open_left", "open_both")) != pc["is_open"]:
                raise ValidationGateError(f"Sugya {g['id']} boundary_status conflicts with pending_continuation.is_open")
            for nm in g["name_mentions"]:
                if nm["scholar_id"] is not None and (
                    nm["scholar_id"] not in ids or ids[nm["scholar_id"]][0] != "scholars"
                ):
                    raise ValidationGateError(f"Sugya {g['id']} name_mention has invalid scholar_id {nm['scholar_id']}")
                for tid in nm["transmitter_ids"] + nm["candidate_ids"]:
                    if tid not in ids or ids[tid][0] != "scholars":
                        raise ValidationGateError(f"Sugya {g['id']} name_mention has invalid chain/candidate {tid}")
                if nm["candidate_ids"] and nm["scholar_id"] is not None:
                    raise ValidationGateError(f"Sugya {g['id']} assigns scholar_id on unresolved candidate group!")
                for ev in nm["evidence"]:
                    s = allseg[ev["segment_id"]]
                    if s["text"][ev["start_char"] : ev["end_char"]] != ev["quote"]:
                        raise ValidationGateError(f"Name mention quote mismatch on {g['id']}")

    if set(covered_counts) != set(seg_by_id) or any(c != 1 for c in covered_counts.values()):
        raise ValidationGateError("Primary sugya coverage has gap or overlap!")

    # Evidence substring & graph link checks across all 8 tables
    related_sugya_segs: dict[str, set[str]] = {}
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
                if e["segment_id"] not in allseg:
                    raise ValidationGateError(f"Unknown evidence segment_id {e['segment_id']} on {r['id']}")
                s = allseg[e["segment_id"]]
                if e["ref"] != s["ref"] or e["source_sha256"] != s["source_sha256"]:
                    raise ValidationGateError(f"Evidence ref/hash mismatch on {r['id']}")
                if not (0 <= e["start_char"] < e["end_char"] <= len(s["text"])):
                    raise ValidationGateError(f"Evidence char bounds invalid on {r['id']}")
                if s["text"][e["start_char"] : e["end_char"]] != e["quote"]:
                    raise ValidationGateError(f"Quote provenance mismatch on {r['id']}")
                evidence_count += 1
            if table in ("statements", "questions", "positions"):
                if r["sugya_id"] not in groups:
                    raise ValidationGateError(f"{table} {r['id']} unknown sugya_id")
            if table == "statements":
                for k in ("speaker_id", "attributed_authority_id", "quoted_authority_id"):
                    if r[k] is not None and (r[k] not in ids or ids[r[k]][0] != "scholars"):
                        raise ValidationGateError(f"Statement {r['id']} invalid {k}")
                for k in ("transmitter_ids", "speaker_candidates"):
                    for val in r[k]:
                        if val not in ids or ids[val][0] != "scholars":
                            raise ValidationGateError(f"Statement {r['id']} invalid {k}")
                if r["speaker_candidates"] and (
                    r["attributed_authority_id"] is not None
                    or r["attribution_status"] != "unresolved_alternatives"
                ):
                    raise ValidationGateError(f"Statement {r['id']} assigns speaker to unresolved חד אמר / variant!")
                if not any(e["segment_id"] in groups[r["sugya_id"]]["segment_ids"] for e in r["evidence"]):
                    raise ValidationGateError(f"Statement {r['id']} lacks local sugya anchor evidence")
                if not all(
                    e["segment_id"] in groups[r["sugya_id"]]["segment_ids"]
                    or e["segment_id"] in related_sugya_segs.get(r["sugya_id"], set())
                    or allseg[e["segment_id"]]["scope"] == "context_only"
                    for e in r["evidence"]
                ):
                    raise ValidationGateError(f"Statement {r['id']} cites unlinked out-of-sugya processed segment")
            if table == "relations":
                endpoint = "sugyot" if r["relation_type"] == "related_topic" else "statements"
                for ep_k in ("source_id", "target_id"):
                    if r[ep_k] not in ids or ids[r[ep_k]][0] != endpoint:
                        raise ValidationGateError(f"Relation {r['id']} invalid {ep_k}")
            if table == "review_queue":
                for tid in r["target_ids"]:
                    if tid not in ids:
                        raise ValidationGateError(f"Review {r['id']} invalid target_id {tid}")

    # Every processed segment lacking a statement record must have an open semantic_extraction_pending review record!
    stmt_covered_segs = {e["segment_id"] for s in data["statements"] for e in s["evidence"]} & set(seg_by_id)
    pending_extraction_segs = {
        tid
        for r in data["review_queue"]
        if r["issue_type"] == "semantic_extraction_pending" and r["status"] == "open"
        for tid in r["target_ids"]
    }
    uncovered_without_pending = set(seg_by_id) - stmt_covered_segs - pending_extraction_segs
    if uncovered_without_pending:
        raise ValidationGateError(
            f"Segments lack both statements and open semantic_extraction_pending review: {sorted(uncovered_without_pending)[:5]}"
        )

    return {
        "schema_contract_version": "1.1.0",
        "mechanical_pass": True,
        "records": {t: len(rr) for t, rr in data.items()},
        "processed_source_segments": len(seg_by_id),
        "pilot_v1_segments": sum(s["scope"] == "pilot" for s in data["segments"]),
        "continuation_core_segments": sum(s["scope"] == "core" for s in data["segments"]),
        "context_only_segments": len(contexts),
        "primary_sugyot": sum(g["level"] == "primary" for g in groups.values()),
        "sub_sugyot": sum(g["level"] == "sub_sugya" for g in groups.values()),
        "evidence_spans_checked": evidence_count,
        "primary_coverage_segments": len(covered_counts),
        "source_text_errors": 0,
        "reference_errors": 0,
        "duplicate_ids": 0,
        "uncovered_segments": 0,
        "segments_with_selected_statements": len(stmt_covered_segs),
        "segments_deferred_qa_extraction": len(pending_extraction_segs),
        "open_review_records": sum(r["status"] == "open" for r in data["review_queue"]),
        "ml_eligible_records": 0,
        "human_expert_reviews": 0,
        "semantic_completeness_pass": False,
        "expansion_gate_pass": False,
        "provisional_segmentation_phase_active": True,
        "source_files_checked": 37 if (check_source and source_root is not None) else 0,
        "scope_note": "Provisional sugya segmentation continuation; historical full-semantics/ML gate remains false.",
    }


def apply_continuation_block(
    base_dir: Path,
    source_root: Path,
    input_packet: dict[str, Any],
    proposal: dict[str, Any],
    independent_review: dict[str, Any] | None = None,
    _inject_fault_after_writes: int | None = None,
) -> dict[str, Any]:
    """Compile cumulative state into staging, verify all invariants & byte-preservation, then promote atomically."""
    block_id = input_packet["block_id"]
    if proposal.get("block_id") != block_id:
        raise ConflictingBlockError("proposal.block_id does not match input_packet.block_id")

    input_hash = p.sha(json.dumps(input_packet, ensure_ascii=False, sort_keys=True).encode("utf-8"))
    prop_hash = p.sha(json.dumps(proposal, ensure_ascii=False, sort_keys=True).encode("utf-8"))
    rev_hash = (
        p.sha(json.dumps(independent_review, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        if independent_review is not None
        else None
    )

    ledger = ensure_ledger(base_dir)
    for existing_blk in ledger["blocks"]:
        if existing_blk["block_id"] == block_id:
            if (
                existing_blk.get("input_packet_sha256") == input_hash
                and existing_blk.get("proposal_sha256") == prop_hash
            ):
                return {"status": "already_applied_idempotent", "block_id": block_id}
            raise ConflictingBlockError(
                f"Block {block_id} already exists in ledger with conflicting input/proposal hashes!"
            )

    # Verify source hashes against source_manifest.json before staging
    manifest = p.read(base_dir / "source_manifest.json")
    tractate = input_packet["tractate"]
    t_meta = next(m for m in manifest["tractates"] if m["title"] == tractate)
    live_bytes = (source_root / t_meta["source_path"]).read_bytes()
    if p.sha(live_bytes) != t_meta["source_sha256"] or input_packet["source_sha256"] != t_meta["source_sha256"]:
        raise SourceIntegrityError("Source file SHA-256 mismatch before staging!")
    live_doc = p.read(source_root / t_meta["source_path"])

    # Determine exact set of refs covered by independent review (for span_review_status truth check!)
    reviewed_refs: set[str] = set()
    if independent_review is not None:
        all_pkt_refs = [s["ref"] for s in input_packet["segments"]]
        ref_pos = {r: idx for idx, r in enumerate(all_pkt_refs)}
        for u in independent_review.get("units", []):
            sr, er = u["start_ref"], u["end_ref"]
            if sr in ref_pos and er in ref_pos:
                for idx in range(ref_pos[sr], ref_pos[er] + 1):
                    reviewed_refs.add(all_pkt_refs[idx])

    # Load current live tables to preserve unaffected records byte-for-byte
    old_tables = {t: p.rows(base_dir / "data" / f"{t}.jsonl") for t in p.TABLES}
    old_bytes_by_id = {
        t: {r["id"]: canon_json_bytes(r) for r in rows_t} for t, rows_t in old_tables.items()
    }
    old_ctx = p.rows(base_dir / "context/segments.jsonl")
    old_revisions_ledger = (
        p.rows(base_dir / "revisions_ledger.jsonl")
        if (base_dir / "revisions_ledger.jsonl").exists()
        else []
    )

    # 1. Build new segments & context tables
    core_pkt_segs = [s for s in input_packet["segments"] if s["role_in_block"] == "core"]
    follow_pkt_segs = [s for s in input_packet["segments"] if s["role_in_block"] == "following_context"]

    existing_seg_ids = {s["id"] for s in old_tables["segments"]}
    for cs in core_pkt_segs:
        if cs["id"] in existing_seg_ids:
            raise ConflictingBlockError(f"Core segment {cs['ref']} already in data/segments.jsonl!")
        i, j = cs["source_index"]
        if live_doc["text"][i][j] != cs["text"]:
            raise SourceIntegrityError(f"Packet text mismatch against raw Wikisource at {cs['ref']}")

    new_core_seg_rows = [
        {
            "schema_version": "1.1.0",
            "id": cs["id"],
            "tractate": cs["tractate"],
            "ref": cs["ref"],
            "source_index": cs["source_index"],
            "text": cs["text"],
            "text_sha256": cs["text_sha256"],
            "source_sha256": cs["source_sha256"],
            "version_title": p.VERSION,
            "scope": "core",
            "block_id": block_id,
            "promoted_from_context": cs["previously_in"] == "context_only",
        }
        for cs in core_pkt_segs
    ]
    staged_segments = list(old_tables["segments"]) + new_core_seg_rows

    promoted_ids = {cs["id"] for cs in core_pkt_segs}
    # Keep context from OTHER tractates (e.g., Bava Metzia 20b & 23a) untouched, replace this tractate's context with new following context (plus any preceding_context still outside processed segments)
    kept_ctx = [
        c for c in old_ctx if c["id"] not in promoted_ids and c["tractate"] != tractate
    ]
    processed_all_ids = {s["id"] for s in staged_segments}
    new_tractate_ctx = [
        {
            "schema_version": "1.0.0",
            "id": fs["id"],
            "tractate": fs["tractate"],
            "ref": fs["ref"],
            "source_index": fs["source_index"],
            "text": fs["text"],
            "text_sha256": fs["text_sha256"],
            "source_sha256": fs["source_sha256"],
            "version_title": p.VERSION,
            "scope": "context_only",
        }
        for fs in follow_pkt_segs
        if fs["id"] not in processed_all_ids
    ]
    staged_ctx = kept_ctx + new_tractate_ctx

    # Lookup map by ref across all processed + context segments
    seg_lookup_by_ref = {s["ref"]: s for s in staged_segments + staged_ctx}
    tractate_ordered_segs = sorted(
        [s for s in staged_segments if s["tractate"] == tractate],
        key=lambda r: r["source_index"],
    )
    tractate_pos = {s["ref"]: idx for idx, s in enumerate(tractate_ordered_segs)}

    def full_seg_ev(ref: str) -> dict[str, Any]:
        s = seg_lookup_by_ref[ref]
        return {
            "segment_id": s["id"],
            "ref": ref,
            "start_char": 0,
            "end_char": len(s["text"]),
            "quote": s["text"],
            "source_sha256": s["source_sha256"],
        }

    def sub_ev(ref: str, quote: str | None = None) -> dict[str, Any]:
        s = seg_lookup_by_ref[ref]
        if quote is None:
            return full_seg_ev(ref)
        idx = s["text"].find(quote)
        if idx == -1:
            raise ValidationGateError(f"Exact substring {quote!r} not found in raw {ref}: {s['text']!r}")
        return {
            "segment_id": s["id"],
            "ref": ref,
            "start_char": idx,
            "end_char": idx + len(quote),
            "quote": quote,
            "source_sha256": s["source_sha256"],
        }

    def span_between(start_ref: str, end_ref: str) -> list[dict[str, Any]]:
        lo_i = tractate_pos[start_ref]
        hi_i = tractate_pos[end_ref]
        if hi_i < lo_i:
            raise ValidationGateError(f"Invalid sugya span {start_ref}..{end_ref}")
        return tractate_ordered_segs[lo_i : hi_i + 1]

    # 2. Scholars helper (preserve all existing scholars byte-for-byte; append only brand-new textual labels)
    staged_scholars = copy.deepcopy(old_tables["scholars"])
    scholar_id_by_name = {s["name_he"]: s["id"] for s in staged_scholars}

    def ensure_scholar(name_he: str, ev_obj: dict[str, Any]) -> str:
        if name_he in scholar_id_by_name:
            return scholar_id_by_name[name_he]
        sid = p.stable("sch", name_he)
        scholar_id_by_name[name_he] = sid
        staged_scholars.append(
            {
                "schema_version": "1.1.0",
                "id": sid,
                "review_status": "ai_provisional",
                "ml_eligible": False,
                "block_id": block_id,
                "name_he": name_he,
                "aliases": [],
                "external_authority_id": None,
                "identity_status": "textual_label_only_person_disambiguation_pending",
                "evidence": [ev_obj],
            }
        )
        return sid

    # 3. Process sugyot, statements, relations, review_queue, and explicit revision ledger
    intentionally_revised_ids: set[str] = set()
    new_revision_entries: list[dict[str, Any]] = []

    staged_sugyot = copy.deepcopy(old_tables["sugyot"])
    staged_statements = copy.deepcopy(old_tables["statements"])
    staged_questions = copy.deepcopy(old_tables["questions"])
    staged_positions = copy.deepcopy(old_tables["positions"])
    staged_relations = copy.deepcopy(old_tables["relations"])
    staged_reviews = copy.deepcopy(old_tables["review_queue"])

    sugya_idx_by_id = {g["id"]: idx for idx, g in enumerate(staged_sugyot)}
    review_idx_by_id = {r["id"]: idx for idx, r in enumerate(staged_reviews)}

    def compute_span_review_status(seg_refs: list[str], requested_status: str) -> str:
        if independent_review is None:
            if requested_status != "constructed_unreviewed":
                raise ValidationGateError("Cannot claim independent review when independent_review is None!")
            return "constructed_unreviewed"
        covered_n = sum(r in reviewed_refs for r in seg_refs)
        if covered_n == 0:
            if requested_status != "constructed_unreviewed":
                raise ValidationGateError(f"Span {seg_refs[0]}..{seg_refs[-1]} has 0 reviewed refs!")
            return "constructed_unreviewed"
        if covered_n < len(seg_refs):
            # CRITICAL INVARIANT: Review status must reflect the WHOLE revised source span!
            if requested_status in ("independent_source_reviewed", "independent_source_reviewed_with_disagreement"):
                raise ValidationGateError(
                    f"Span {seg_refs[0]}..{seg_refs[-1]} only partially covered by independent review "
                    f"({covered_n}/{len(seg_refs)} refs); must use 'partial_span_reviewed'!"
                )
            return "partial_span_reviewed"
        return requested_status

    statement_covered_seg_ids: set[str] = {
        e["segment_id"] for s in staged_statements for e in s["evidence"]
    }

    for u_spec in proposal["units"]:
        key = u_spec["authoring_key"]
        covered = span_between(u_spec["start_ref"], u_spec["end_ref"])
        covered_refs = [s["ref"] for s in covered]
        extends_id = u_spec.get("extends_inherited_id")
        gid = extends_id if extends_id else p.stable("sug", key)

        # Build source-grounded name_mentions
        mentions_out: list[dict[str, Any]] = []
        for nm in u_spec.get("name_mentions", []):
            ev_obj = sub_ev(nm["ref"], nm.get("quote"))
            auth_id = ensure_scholar(nm["name_he"], ev_obj) if nm.get("scholar_label") else None
            trans_ids = [ensure_scholar(tn, ev_obj) for tn in nm.get("transmitters", [])]
            cand_ids = [ensure_scholar(cn, ev_obj) for cn in nm.get("candidates", [])]
            mentions_out.append(
                {
                    "scholar_id": auth_id,
                    "name_he": nm["name_he"],
                    "role": nm["role"],
                    "attribution_status": nm["attribution_status"],
                    "transmitter_ids": trans_ids,
                    "candidate_ids": cand_ids,
                    "note_he": nm.get("note_he"),
                    "evidence": [ev_obj],
                }
            )

        # Boundary & context evidence
        ev_list = [full_seg_ev(covered[0]["ref"]), full_seg_ev(covered[-1]["ref"])]
        for ctx_ref in u_spec.get("context_preview_refs", []):
            ev_list.append(full_seg_ev(ctx_ref))

        b_status = u_spec["boundary_status"]
        is_open = b_status in ("open_right", "open_left", "open_both")
        direction = (
            "right"
            if b_status == "open_right"
            else ("left" if b_status == "open_left" else ("both" if b_status == "open_both" else "none"))
        )
        span_rev_status = compute_span_review_status(covered_refs, u_spec["span_review_status"])

        # Prepare review items linked to this sugya
        review_ids_for_unit: list[str] = []
        boundary_rev_id = p.stable("rev", gid, "boundary")
        boundary_desc = u_spec.get(
            "boundary_review_description_he",
            "גבול סוגיה זמני בשלב המשך מסכת ברכות; פירוק טענות אטומיות ושאלות השוואתיות נדחה לשלב נפרד.",
        )

        if extends_id:
            if extends_id not in sugya_idx_by_id:
                raise ConflictingBlockError(f"extends_inherited_id {extends_id} not found in data/sugyot.jsonl")
            old_sugya = staged_sugyot[sugya_idx_by_id[extends_id]]
            old_sugya_sha = rec_sha256(old_sugya)
            intentionally_revised_ids.add(extends_id)

            new_sugya = {
                "schema_version": "1.1.0",
                "id": gid,
                "review_status": "ai_provisional",
                "ml_eligible": False,
                "authoring_key": key,
                "block_id": block_id,
                "tractate": tractate,
                "title_he": u_spec["title_he"],
                "summary_he": u_spec["summary_he"],
                "summary_origin": "editorial_paraphrase",
                "level": "primary",
                "parent_id": None,
                "segment_ids": [s["id"] for s in covered],
                "start_ref": covered[0]["ref"],
                "end_ref": covered[-1]["ref"],
                "boundary_status": b_status,
                "pending_continuation": {
                    "is_open": is_open,
                    "direction": direction,
                    "next_unprocessed_ref": u_spec.get("next_unprocessed_ref"),
                    "context_preview_refs": u_spec.get("context_preview_refs", []),
                    "note_he": u_spec.get("continuation_note_he"),
                },
                "boundary_rationale": u_spec["boundary_rationale"],
                "conditions": u_spec.get("conditions", []),
                "family_id": old_sugya["family_id"],
                "family_status": old_sugya["family_status"],
                "annotation_completeness": "minimal_sugya_layer_qa_deferred",
                "construction_status": "provisional_extended_open_tail",
                "extraction_status": u_spec.get("extraction_status", "selected_claims_and_names_qa_deferred"),
                "span_review_status": span_rev_status,
                "uncertainty_notes_he": u_spec.get("uncertainty_notes_he", []),
                "review_item_ids": [boundary_rev_id],
                "name_mentions": mentions_out,
                "lineage": {
                    "origin_block_id": "pilot_baseline_ef29310",
                    "updated_in_block_id": block_id,
                    "previous_record_sha256": old_sugya_sha,
                    "supersedes_ids": [],
                },
                "evidence": ev_list,
            }

            # Also update B24's boundary review item so its evidence spans the whole revised sugya
            if boundary_rev_id in review_idx_by_id:
                old_rev = staged_reviews[review_idx_by_id[boundary_rev_id]]
                old_rev_sha = rec_sha256(old_rev)
                intentionally_revised_ids.add(boundary_rev_id)
                updated_rev = {
                    **old_rev,
                    "schema_version": "1.1.0",
                    "block_id": block_id,
                    "description_he": boundary_desc,
                    "evidence": [full_seg_ev(covered[0]["ref"]), full_seg_ev(covered[-1]["ref"])],
                }
                staged_reviews[review_idx_by_id[boundary_rev_id]] = updated_rev
                new_revision_entries.append(
                    {
                        "revision_id": p.stable("chg", block_id, boundary_rev_id),
                        "block_id": block_id,
                        "table": "review_queue",
                        "record_id": boundary_rev_id,
                        "reason": "Updated boundary review evidence to cover full extended B24 span.",
                        "previous_record_sha256": old_rev_sha,
                        "new_record_sha256": rec_sha256(updated_rev),
                        "previous_record": old_rev,
                    }
                )
            review_ids_for_unit.append(boundary_rev_id)

            for extra_rv in u_spec.get("extra_reviews", []):
                er_id = p.stable("rev", gid, extra_rv["tag"])
                review_ids_for_unit.append(er_id)
                staged_reviews.append(
                    {
                        "schema_version": "1.1.0",
                        "id": er_id,
                        "review_status": "ai_provisional",
                        "ml_eligible": False,
                        "block_id": block_id,
                        "target_ids": [gid],
                        "issue_type": extra_rv["issue_type"],
                        "severity": "blocks_ml",
                        "status": "open",
                        "description_he": extra_rv["description_he"],
                        "evidence": [full_seg_ev(r) for r in extra_rv["evidence_refs"]],
                    }
                )
            new_sugya["review_item_ids"] = review_ids_for_unit
            staged_sugyot[sugya_idx_by_id[extends_id]] = new_sugya
            new_revision_entries.append(
                {
                    "revision_id": p.stable("chg", block_id, gid),
                    "block_id": block_id,
                    "table": "sugyot",
                    "record_id": gid,
                    "reason": f"Extended inherited open_right sugya {key} ({old_sugya['start_ref']}..{old_sugya['end_ref']} -> {new_sugya['start_ref']}..{new_sugya['end_ref']}).",
                    "previous_record_sha256": old_sugya_sha,
                    "new_record_sha256": rec_sha256(new_sugya),
                    "previous_record": old_sugya,
                }
            )
        else:
            staged_reviews.append(
                {
                    "schema_version": "1.1.0",
                    "id": boundary_rev_id,
                    "review_status": "ai_provisional",
                    "ml_eligible": False,
                    "block_id": block_id,
                    "target_ids": [gid],
                    "issue_type": "open_tail_continuation_pending" if is_open else "boundary_and_family_review",
                    "severity": "blocks_ml",
                    "status": "open",
                    "description_he": boundary_desc,
                    "evidence": ev_list,
                }
            )
            review_ids_for_unit.append(boundary_rev_id)

            for extra_rv in u_spec.get("extra_reviews", []):
                er_id = p.stable("rev", gid, extra_rv["tag"])
                review_ids_for_unit.append(er_id)
                staged_reviews.append(
                    {
                        "schema_version": "1.1.0",
                        "id": er_id,
                        "review_status": "ai_provisional",
                        "ml_eligible": False,
                        "block_id": block_id,
                        "target_ids": [gid],
                        "issue_type": extra_rv["issue_type"],
                        "severity": "blocks_ml",
                        "status": "open",
                        "description_he": extra_rv["description_he"],
                        "evidence": [full_seg_ev(r) for r in extra_rv["evidence_refs"]],
                    }
                )

            new_sugya = {
                "schema_version": "1.1.0",
                "id": gid,
                "review_status": "ai_provisional",
                "ml_eligible": False,
                "authoring_key": key,
                "block_id": block_id,
                "tractate": tractate,
                "title_he": u_spec["title_he"],
                "summary_he": u_spec["summary_he"],
                "summary_origin": "editorial_paraphrase",
                "level": "primary",
                "parent_id": None,
                "segment_ids": [s["id"] for s in covered],
                "start_ref": covered[0]["ref"],
                "end_ref": covered[-1]["ref"],
                "boundary_status": b_status,
                "pending_continuation": {
                    "is_open": is_open,
                    "direction": direction,
                    "next_unprocessed_ref": u_spec.get("next_unprocessed_ref"),
                    "context_preview_refs": u_spec.get("context_preview_refs", []),
                    "note_he": u_spec.get("continuation_note_he"),
                },
                "boundary_rationale": u_spec["boundary_rationale"],
                "conditions": u_spec.get("conditions", []),
                "family_id": p.stable("fam", key),
                "family_status": "provisional_single_occurrence_not_split_ready",
                "annotation_completeness": "minimal_sugya_layer_qa_deferred",
                "construction_status": "provisional_open_tail" if is_open else "provisional_segmented",
                "extraction_status": u_spec.get("extraction_status", "minimal_sugya_layer_only_qa_deferred"),
                "span_review_status": span_rev_status,
                "uncertainty_notes_he": u_spec.get("uncertainty_notes_he", []),
                "review_item_ids": review_ids_for_unit,
                "name_mentions": mentions_out,
                "lineage": {
                    "origin_block_id": block_id,
                    "updated_in_block_id": block_id,
                    "previous_record_sha256": None,
                    "supersedes_ids": [],
                },
                "evidence": ev_list,
            }
            staged_sugyot.append(new_sugya)

        # Sub-sugyot if specified
        for sub_spec in u_spec.get("sub_units", []):
            sub_cov = span_between(sub_spec["start_ref"], sub_spec["end_ref"])
            sub_id = p.stable("sug", sub_spec["authoring_key"])
            staged_sugyot.append(
                {
                    "schema_version": "1.1.0",
                    "id": sub_id,
                    "review_status": "ai_provisional",
                    "ml_eligible": False,
                    "authoring_key": sub_spec["authoring_key"],
                    "block_id": block_id,
                    "tractate": tractate,
                    "title_he": sub_spec["title_he"],
                    "summary_he": sub_spec["summary_he"],
                    "summary_origin": "editorial_paraphrase",
                    "level": "sub_sugya",
                    "parent_id": gid,
                    "segment_ids": [s["id"] for s in sub_cov],
                    "start_ref": sub_cov[0]["ref"],
                    "end_ref": sub_cov[-1]["ref"],
                    "boundary_status": "provisional",
                    "pending_continuation": {
                        "is_open": False,
                        "direction": "none",
                        "next_unprocessed_ref": None,
                        "context_preview_refs": [],
                        "note_he": None,
                    },
                    "boundary_rationale": sub_spec["boundary_rationale"],
                    "conditions": [],
                    "family_id": p.stable("fam", key),
                    "family_status": "provisional_single_occurrence_not_split_ready",
                    "annotation_completeness": "minimal_sugya_layer_qa_deferred",
                    "construction_status": "provisional_segmented",
                    "extraction_status": "minimal_sugya_layer_only_qa_deferred",
                    "span_review_status": span_rev_status,
                    "uncertainty_notes_he": [],
                    "review_item_ids": [],
                    "name_mentions": [],
                    "lineage": {
                        "origin_block_id": block_id,
                        "updated_in_block_id": block_id,
                        "previous_record_sha256": None,
                        "supersedes_ids": [],
                    },
                    "evidence": [full_seg_ev(sub_cov[0]["ref"]), full_seg_ev(sub_cov[-1]["ref"])],
                }
            )

        # Optional selected statements (without forcing Q-A/positions!)
        for st_spec in u_spec.get("selected_statements", []):
            ev_s = sub_ev(st_spec["ref"], st_spec.get("quote"))
            st_id = p.stable("stm", st_spec["authoring_key"])
            auth_id = ensure_scholar(st_spec["authority"], ev_s) if st_spec.get("authority") else None
            chain_ids = [ensure_scholar(tn, ev_s) for tn in st_spec.get("transmitters", [])]
            cand_ids = [ensure_scholar(cn, ev_s) for cn in st_spec.get("candidates", [])]
            staged_statements.append(
                {
                    "schema_version": "1.1.0",
                    "id": st_id,
                    "review_status": "ai_provisional",
                    "ml_eligible": False,
                    "block_id": block_id,
                    "authoring_key": st_spec["authoring_key"],
                    "sugya_id": gid,
                    "role": st_spec["role"],
                    "summary_he": st_spec["summary_he"],
                    "summary_origin": "editorial_paraphrase",
                    "source_reasoning": st_spec.get("source_reasoning", "source_explicit"),
                    "narrator": "anonymous_talmudic_redactor",
                    "speaker_id": chain_ids[0] if chain_ids else auth_id,
                    "attributed_authority_id": auth_id,
                    "transmitter_ids": chain_ids,
                    "quoted_authority_id": auth_id if chain_ids else None,
                    "attribution_status": (
                        "unresolved_alternatives"
                        if cand_ids
                        else ("explicit_name" if auth_id else "anonymous_or_continuation")
                    ),
                    "speaker_candidates": cand_ids,
                    "position_status": st_spec["position_status"],
                    "evidence": [ev_s],
                }
            )
            statement_covered_seg_ids.add(ev_s["segment_id"])
            if cand_ids:
                staged_reviews.append(
                    {
                        "schema_version": "1.1.0",
                        "id": p.stable("rev", st_id, "attribution"),
                        "review_status": "ai_provisional",
                        "ml_eligible": False,
                        "block_id": block_id,
                        "target_ids": [st_id],
                        "issue_type": "unresolved_attribution",
                        "severity": "blocks_ml",
                        "status": "open",
                        "description_he": "חילופי גירסה או ייחוס בלתי מוכרע במקור; אין להכריע על פי סדר השמות.",
                        "evidence": [ev_s],
                    }
                )

    # Mark every new core segment without an explicit statement as semantic_extraction_pending
    for cs in new_core_seg_rows:
        if cs["id"] not in statement_covered_seg_ids:
            staged_reviews.append(
                {
                    "schema_version": "1.1.0",
                    "id": p.stable("rev", cs["id"], "extraction"),
                    "review_status": "ai_provisional",
                    "ml_eligible": False,
                    "block_id": block_id,
                    "target_ids": [cs["id"]],
                    "issue_type": "semantic_extraction_pending",
                    "severity": "blocks_ml",
                    "status": "open",
                    "description_he": "הקטע שויך לסוגיה בשלב החלוקה הראשונית; פירוק מלא לטענות ושאלות שמור לשלב נפרד.",
                    "evidence": [full_seg_ev(cs["ref"])],
                }
            )

    # Optional related_topic sugya relations
    sugya_by_key = {g["authoring_key"]: g for g in staged_sugyot}
    for left_k, right_k in proposal.get("related_topic_links", []):
        gl, gr = sugya_by_key[left_k], sugya_by_key[right_k]
        staged_relations.append(
            {
                "schema_version": "1.1.0",
                "id": p.stable("rel", left_k, "related_topic", right_k),
                "review_status": "ai_provisional",
                "ml_eligible": False,
                "block_id": block_id,
                "source_id": gl["id"],
                "target_id": gr["id"],
                "relation_type": "related_topic",
                "origin": "editorial_relation_supported_by_source",
                "evidence": [gl["evidence"][0], gr["evidence"][0]],
            }
        )

    # Rebuild reading windows across all tractates with extracted segments
    staged_windows: list[dict[str, Any]] = []
    for m_tr in manifest["tractates"]:
        tr_name = m_tr["title"]
        tr_all = sorted(
            [r for r in staged_segments + staged_ctx if r["tractate"] == tr_name],
            key=lambda r: r["source_index"],
        )
        if not tr_all:
            continue
        start = 0
        while start < len(tr_all):
            end = start
            size = 0
            while end < len(tr_all) and end - start < 10 and (
                size + len(tr_all[end]["text"]) <= 8000 or end == start
            ):
                size += len(tr_all[end]["text"])
                end += 1
            sel = tr_all[start:end]
            staged_windows.append(
                {
                    "id": p.stable("win", tr_name, sel[0]["id"], sel[-1]["id"]),
                    "tractate": tr_name,
                    "segment_ids": [r["id"] for r in sel],
                    "start_ref": sel[0]["ref"],
                    "end_ref": sel[-1]["ref"],
                    "characters": size,
                    "oversized_atomic_segment": size > 8000,
                    "role": "reading_context_not_semantic_segmentation",
                }
            )
            if end == len(tr_all):
                break
            start = max(start + 1, end - 2)

    # 4. Write all cumulative artifacts into an isolated staging directory and validate!
    staging_root = base_dir / "local_data" / "staging" / f"{block_id}_{uuid.uuid4().hex[:8]}"
    staging_root.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(base_dir / "source_manifest.json", staging_root / "source_manifest.json")
    if not (base_dir / "schema_v1_1.json").exists():
        make_schema_v1_1.make_v1_1()
    shutil.copyfile(base_dir / "schema_v1_1.json", staging_root / "schema_v1_1.json")

    staged_map = {
        "segments": staged_segments,
        "sugyot": staged_sugyot,
        "scholars": staged_scholars,
        "statements": staged_statements,
        "questions": staged_questions,
        "positions": staged_positions,
        "relations": staged_relations,
        "review_queue": staged_reviews,
    }

    # Verify byte-for-byte preservation of ALL unaffected old records BEFORE writing!
    for table, old_id_bytes in old_bytes_by_id.items():
        new_by_id = {r["id"]: r for r in staged_map[table]}
        for oid, obytes in old_id_bytes.items():
            if oid not in new_by_id:
                raise ValidationGateError(f"Previously accepted record {oid} disappeared from {table}!")
            if oid not in intentionally_revised_ids:
                if canon_json_bytes(new_by_id[oid]) != obytes:
                    raise ValidationGateError(
                        f"Unaffected record {oid} in {table} mutated without explicit revision!"
                    )

    for table, rows_t in staged_map.items():
        p.jsonl(staging_root / "data" / f"{table}.jsonl", rows_t)
    p.jsonl(staging_root / "context/segments.jsonl", staged_ctx)
    p.jsonl(staging_root / "context/windows.jsonl", staged_windows)

    staged_revisions_ledger = old_revisions_ledger + new_revision_entries
    p.jsonl(staging_root / "revisions_ledger.jsonl", staged_revisions_ledger)

    # Run full fail-closed validator on staging_root!
    qa_report = validate_v1_1(staging_root, source_root=source_root, check_source=True)

    # Compute updated progress_manifest.json & updated ledger in staging
    progress_rows = []
    for m_tr in manifest["tractates"]:
        w = m_tr["title"]
        sg = [s for s in staged_segments if s["tractate"] == w]
        sg_ids = {s["id"] for s in sg}
        gg = [g for g in staged_sugyot if g["tractate"] == w]
        gg_ids = {g["id"] for g in gg}
        prim_gg = [g for g in gg if g["level"] == "primary"]
        closed_prim = [g for g in prim_gg if g["boundary_status"] == "provisional"]
        open_prim = [g for g in prim_gg if g["boundary_status"] != "provisional"]
        progress_rows.append(
            {
                "ordinal": m_tr["ordinal"],
                "tractate": w,
                "source_segments": m_tr["source_segments"],
                "pilot_segments": sum(s["scope"] == "pilot" for s in sg),
                "processed_segments": len(sg),
                "primary_sugyot": len(prim_gg),
                "statements": sum(s["sugya_id"] in gg_ids for s in staged_statements),
                "questions": sum(q["sugya_id"] in gg_ids for q in staged_questions),
                "positions": sum(po["sugya_id"] in gg_ids for po in staged_positions),
                "uncertain_records": sum(
                    r["status"] == "open" and any(e["segment_id"] in sg_ids for e in r["evidence"])
                    for r in staged_reviews
                ),
                "last_closed_ref": closed_prim[-1]["end_ref"] if closed_prim else None,
                "open_tail_ids": [g["id"] for g in open_prim],
                "status": (
                    "provisional_sugya_continuation_active"
                    if any(s["scope"] == "core" for s in sg)
                    else ("pilot_partial_semantics" if sg else "inventory_only")
                ),
                "completed_masechet": False,
            }
        )

    staged_progress = {
        "schema_version": "1.1.0",
        "completed_masechtot": 0,
        "historical_pilot_expansion_gate_pass": False,
        "provisional_segmentation_continuation": True,
        "tractates": progress_rows,
    }
    p.write(staging_root / "qa_report.json", qa_report)
    p.write(staging_root / "progress_manifest.json", staged_progress)

    open_tails_after = [
        {
            "id": g["id"],
            "authoring_key": g["authoring_key"],
            "tractate": g["tractate"],
            "start_ref": g["start_ref"],
            "end_ref": g["end_ref"],
            "boundary_status": g["boundary_status"],
        }
        for g in staged_sugyot
        if g["level"] == "primary" and g["boundary_status"] in ("open_right", "open_left", "open_both")
    ]
    tr_prog = next(x for x in progress_rows if x["tractate"] == tractate)
    next_unproc_ref = follow_pkt_segs[0]["ref"] if follow_pkt_segs else None

    new_ledger = copy.deepcopy(ledger)
    new_ledger["blocks"].append(
        {
            "block_id": block_id,
            "phase": "provisional_sugya_continuation_v1_1",
            "tractate": tractate,
            "core_daf_range": input_packet["core_daf_range"],
            "input_packet_sha256": input_hash,
            "proposal_sha256": prop_hash,
            "independent_review_sha256": rev_hash,
            "core_segments_added": len(new_core_seg_rows),
            "promoted_from_context_count": sum(s["promoted_from_context"] for s in new_core_seg_rows),
            "cumulative_tractate_segments": tr_prog["processed_segments"],
            "cumulative_total_segments": len(staged_segments),
            "revised_record_ids": sorted(intentionally_revised_ids),
            "new_sugya_ids": [
                p.stable("sug", u["authoring_key"])
                for u in proposal["units"]
                if not u.get("extends_inherited_id")
            ],
            "last_closed_ref": tr_prog["last_closed_ref"],
            "next_unprocessed_ref": next_unproc_ref,
            "open_tails_after_block": open_tails_after,
            "accepted": True,
        }
    )
    p.write(staging_root / "block_ledger.json", new_ledger)

    # 5. Atomic promotion from staging_root to base_dir with write-ahead backup & rollback on interruption!
    rel_targets = (
        [f"data/{t}.jsonl" for t in p.TABLES]
        + [
            "context/segments.jsonl",
            "context/windows.jsonl",
            "revisions_ledger.jsonl",
            "qa_report.json",
            "progress_manifest.json",
            "block_ledger.json",
        ]
    )

    backup_dir = base_dir / "local_data" / "tx_backup" / f"{block_id}_{uuid.uuid4().hex[:8]}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    existed_before: dict[str, bool] = {}
    for rel in rel_targets:
        dst = base_dir / rel
        existed_before[rel] = dst.exists()
        if dst.exists():
            bk = backup_dir / rel
            bk.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(dst, bk)

    writes_done = 0
    try:
        for rel in rel_targets:
            if _inject_fault_after_writes is not None and writes_done >= _inject_fault_after_writes:
                raise IOError(f"Simulated interrupted write after {writes_done} files!")
            src_f = staging_root / rel
            dst_f = base_dir / rel
            dst_f.parent.mkdir(parents=True, exist_ok=True)
            tmp_dst = dst_f.with_suffix(dst_f.suffix + ".tmp_promote")
            shutil.copyfile(src_f, tmp_dst)
            os.replace(tmp_dst, dst_f)
            writes_done += 1
    except Exception:
        # Roll back every touched file so previous checkpoint remains 100% intact and usable!
        for rel in rel_targets:
            dst_f = base_dir / rel
            tmp_dst = dst_f.with_suffix(dst_f.suffix + ".tmp_promote")
            if tmp_dst.exists():
                tmp_dst.unlink()
            if existed_before[rel]:
                shutil.copyfile(backup_dir / rel, dst_f)
            elif dst_f.exists():
                dst_f.unlink()
        shutil.rmtree(backup_dir, ignore_errors=True)
        shutil.rmtree(staging_root, ignore_errors=True)
        raise

    shutil.rmtree(backup_dir, ignore_errors=True)
    shutil.rmtree(staging_root, ignore_errors=True)
    return {
        "status": "accepted",
        "block_id": block_id,
        "qa_report": qa_report,
        "ledger_entry": new_ledger["blocks"][-1],
    }
