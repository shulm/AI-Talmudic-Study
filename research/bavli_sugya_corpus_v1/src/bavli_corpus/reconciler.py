"""Global cross-window and cross-daf sugya boundary reconciler."""
from __future__ import annotations

from typing import Any

from . import SCHEMA_VERSION, SOURCE_VERSION_ID
from .normalization import sha256_str, tractate_slug


def make_sugya_id(slug: str, start_seg: dict[str, Any], end_seg: dict[str, Any], sub_tag: str | None = None) -> str:
    s_coord = f"{start_seg['daf']}:{start_seg['segment_num']}"
    e_coord = f"{end_seg['daf']}:{end_seg['segment_num']}"
    if sub_tag:
        return f"subsugya:bavli:{slug}:{s_coord}__{e_coord}:{sub_tag}"
    return f"sugya:bavli:{slug}:{s_coord}__{e_coord}"


def make_lineage_id(slug: str, founding_segment_id: str, level: str = "top", sub_tag: str | None = None) -> str:
    seed = f"{slug}|{level}|{founding_segment_id}|{sub_tag or ''}"
    return f"lin:{sha256_str(seed)[:12]}"


def reconcile_window_boundaries(
    target_segments: list[dict[str, Any]],
    window_proposals: list[dict[str, Any]],
    review_status_default: str = "provisional_ai_single",
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    """Stitch windowed sugya boundary proposals across amud/daf/window transitions.

    Each window_proposal dict has:
      - window_id: str
      - units: list of dicts with:
          local_key, segment_ids, continues_from_prev_window (bool), continues_into_next_window (bool),
          sugya_type, mishna_gemara_relation, topic_tags, summary_paraphrase_en,
          boundary_start_cue, boundary_end_cue, boundary_status, uncertainty_notes,
          candidate_boundary_interpretations (optional), parallel_family_ids (optional),
          redirects_from (optional), sub_units (optional list)

    Returns:
      (sugya_records, local_key_to_sugya_id_map)
    """
    if not target_segments:
        return [], {}

    seg_by_id = {s["segment_id"]: s for s in target_segments}
    tractate = target_segments[0]["tractate"]
    slug = tractate_slug(tractate)

    merged_units: list[dict[str, Any]] = []
    pending_open: dict[str, Any] | None = None

    for w_prop in window_proposals:
        for u in w_prop["units"]:
            u_segs = list(u["segment_ids"])
            if not u_segs:
                raise ValueError(f"Empty segment_ids in window {w_prop['window_id']} unit {u.get('local_key')}")
            if u.get("continues_from_prev_window"):
                if pending_open is None:
                    raise ValueError(
                        f"Unit {u.get('local_key')} in {w_prop['window_id']} marked continues_from_prev_window "
                        f"but no previous open continuation exists."
                    )
                pending_open["segment_ids"].extend(u_segs)
                pending_open["local_keys"].append(u["local_key"])
                pending_open["boundary_end_cue"] = u["boundary_end_cue"]
                for tag in u.get("topic_tags", []):
                    if tag not in pending_open["topic_tags"]:
                        pending_open["topic_tags"].append(tag)
                for pf in u.get("parallel_family_ids", []):
                    if pf not in pending_open["parallel_family_ids"]:
                        pending_open["parallel_family_ids"].append(pf)
                pending_open["sub_units"].extend(u.get("sub_units", []))
                if u.get("uncertainty_notes"):
                    prev_n = pending_open.get("uncertainty_notes") or ""
                    pending_open["uncertainty_notes"] = (
                        f"{prev_n}; {u['uncertainty_notes']}".strip("; ")
                    )
                if not u.get("continues_into_next_window"):
                    # Continuation resolved! Upgrade window_edge_pending to final boundary_status
                    pending_open["boundary_status"] = u.get("boundary_status", "clear")
                    merged_units.append(pending_open)
                    pending_open = None
            else:
                if pending_open is not None:
                    raise ValueError(
                        f"Previous window left unclosed pending unit {pending_open['local_keys']}, "
                        f"but next unit {u.get('local_key')} did not continue it."
                    )
                new_unit = {
                    "local_keys": [u["local_key"]],
                    "segment_ids": u_segs,
                    "sugya_type": u["sugya_type"],
                    "mishna_gemara_relation": u["mishna_gemara_relation"],
                    "topic_tags": list(u.get("topic_tags", [])),
                    "summary_paraphrase_en": u.get("summary_paraphrase_en", ""),
                    "boundary_start_cue": u["boundary_start_cue"],
                    "boundary_end_cue": u["boundary_end_cue"],
                    "boundary_status": (
                        "window_edge_pending"
                        if u.get("continues_into_next_window")
                        else u.get("boundary_status", "clear")
                    ),
                    "review_status": u.get("review_status", review_status_default),
                    "uncertainty_notes": u.get("uncertainty_notes"),
                    "candidate_boundary_interpretations": list(
                        u.get("candidate_boundary_interpretations", [])
                    ),
                    "parallel_family_ids": list(u.get("parallel_family_ids", [])),
                    "redirects_from": list(u.get("redirects_from", [])),
                    "sub_units": list(u.get("sub_units", [])),
                }
                if u.get("continues_into_next_window"):
                    pending_open = new_unit
                else:
                    merged_units.append(new_unit)

    if pending_open is not None:
        # Legitimate when a pilot slice ends mid-sugya (e.g., Berakhot 5a:24 or Bava Metzia 22b:16)
        pending_open["boundary_status"] = "window_edge_pending"
        merged_units.append(pending_open)

    # Verify exact partition of target_segments
    expected_ids = [s["segment_id"] for s in target_segments]
    observed_ids = [sid for mu in merged_units for sid in mu["segment_ids"]]
    if observed_ids != expected_ids:
        missing = set(expected_ids) - set(observed_ids)
        extra = set(observed_ids) - set(expected_ids)
        raise ValueError(
            f"Reconciled top-level sugyot do not form an exact ordered partition of target segments! "
            f"missing={sorted(missing)[:5]}, extra={sorted(extra)[:5]}, "
            f"len_obs={len(observed_ids)} vs len_exp={len(expected_ids)}"
        )

    top_records: list[dict[str, Any]] = []
    sub_records: list[dict[str, Any]] = []
    key_map: dict[str, str] = {}

    for mu in merged_units:
        s_objs = [seg_by_id[sid] for sid in mu["segment_ids"]]
        start_s, end_s = s_objs[0], s_objs[-1]
        sugya_id = make_sugya_id(slug, start_s, end_s)
        lineage_id = make_lineage_id(slug, start_s["segment_id"], level="top")

        daf_span: list[str] = []
        folios: set[int] = set()
        ch_nums: list[int] = []
        for so in s_objs:
            if so["daf"] not in daf_span:
                daf_span.append(so["daf"])
            folios.add(so["folio_num"])
            if so["chapter_num"] not in ch_nums:
                ch_nums.append(so["chapter_num"])

        rec = {
            "record_type": "sugya",
            "schema_version": SCHEMA_VERSION,
            "source_version_id": SOURCE_VERSION_ID,
            "sugya_id": sugya_id,
            "lineage_id": lineage_id,
            "redirects_from": mu["redirects_from"],
            "tractate": tractate,
            "level": "top",
            "parent_sugya_id": None,
            "ordered_segment_ids": mu["segment_ids"],
            "start_ref": start_s["ref"],
            "end_ref": end_s["ref"],
            "chapter_nums": ch_nums,
            "daf_span": daf_span,
            "crosses_amud": len(daf_span) > 1,
            "crosses_daf": len(folios) > 1,
            "sugya_type": mu["sugya_type"],
            "mishna_gemara_relation": mu["mishna_gemara_relation"],
            "topic_tags": mu["topic_tags"],
            "summary_paraphrase_en": mu["summary_paraphrase_en"],
            "is_annotator_paraphrase": True,
            "boundary_start_cue": mu["boundary_start_cue"],
            "boundary_end_cue": mu["boundary_end_cue"],
            "candidate_boundary_interpretations": mu["candidate_boundary_interpretations"],
            "adjacent_prev_sugya_id": None,
            "adjacent_next_sugya_id": None,
            "parallel_family_ids": mu["parallel_family_ids"],
            "boundary_status": mu["boundary_status"],
            "review_status": mu["review_status"],
            "uncertainty_notes": mu["uncertainty_notes"],
        }
        top_records.append(rec)
        for lk in mu["local_keys"]:
            key_map[lk] = sugya_id

        for su in mu["sub_units"]:
            su_s_objs = [seg_by_id[sid] for sid in su["segment_ids"]]
            su_start, su_end = su_s_objs[0], su_s_objs[-1]
            sub_tag = su["sub_tag"]
            sub_id = make_sugya_id(slug, su_start, su_end, sub_tag=sub_tag)
            sub_dafs: list[str] = []
            sub_folios: set[int] = set()
            sub_chs: list[int] = []
            for so in su_s_objs:
                if so["daf"] not in sub_dafs:
                    sub_dafs.append(so["daf"])
                sub_folios.add(so["folio_num"])
                if so["chapter_num"] not in sub_chs:
                    sub_chs.append(so["chapter_num"])
            sub_rec = {
                "record_type": "sugya",
                "schema_version": SCHEMA_VERSION,
                "source_version_id": SOURCE_VERSION_ID,
                "sugya_id": sub_id,
                "lineage_id": make_lineage_id(slug, su_start["segment_id"], level="sub", sub_tag=sub_tag),
                "redirects_from": [],
                "tractate": tractate,
                "level": "sub",
                "parent_sugya_id": sugya_id,
                "ordered_segment_ids": su["segment_ids"],
                "start_ref": su_start["ref"],
                "end_ref": su_end["ref"],
                "chapter_nums": sub_chs,
                "daf_span": sub_dafs,
                "crosses_amud": len(sub_dafs) > 1,
                "crosses_daf": len(sub_folios) > 1,
                "sugya_type": su["sugya_type"],
                "mishna_gemara_relation": su["mishna_gemara_relation"],
                "topic_tags": su.get("topic_tags", []),
                "summary_paraphrase_en": su.get("summary_paraphrase_en", ""),
                "is_annotator_paraphrase": True,
                "boundary_start_cue": su["boundary_start_cue"],
                "boundary_end_cue": su["boundary_end_cue"],
                "candidate_boundary_interpretations": [],
                "adjacent_prev_sugya_id": None,
                "adjacent_next_sugya_id": None,
                "parallel_family_ids": su.get("parallel_family_ids", []),
                "boundary_status": su.get("boundary_status", "clear"),
                "review_status": su.get("review_status", review_status_default),
                "uncertainty_notes": su.get("uncertainty_notes"),
            }
            sub_records.append(sub_rec)
            if "local_key" in su:
                key_map[su["local_key"]] = sub_id

    for idx, rec in enumerate(top_records):
        if idx > 0:
            rec["adjacent_prev_sugya_id"] = top_records[idx - 1]["sugya_id"]
        if idx + 1 < len(top_records):
            rec["adjacent_next_sugya_id"] = top_records[idx + 1]["sugya_id"]

    return top_records + sub_records, key_map
