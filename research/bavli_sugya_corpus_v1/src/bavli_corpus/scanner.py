"""Deterministic Bavli TOC & tractate source scanner with exact daf/chapter mapping."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from . import EDITION_FILENAME, NORMALIZATION_SPEC_ID, SCHEMA_VERSION, SOURCE_VERSION_ID
from .normalization import normalize_with_offset_map, sha256_str, tractate_slug


REF_RANGE_RE = re.compile(
    r"^(?P<title>.+?)\s+(?P<s_daf>\d+)(?P<s_amud>[ab])(?::(?P<s_seg>\d+))?-(?:(?P<e_daf>\d+)(?P<e_amud>[ab]):)?(?P<e_seg>\d+)$"
)
SINGLE_DAF_RE = re.compile(r"^(?P<title>.+?)\s+(?P<daf>\d+)(?P<amud>[ab])(?::(?P<seg>\d+))?$")


def page_index_to_daf(page_idx: int) -> tuple[int, str, str]:
    """Convert 0-based Sefaria Talmud array index to (folio_num, amud, daf_str).

    Index 2 -> (2, 'a', '2a'); index 3 -> (2, 'b', '2b'); index 49 -> (25, 'b', '25b').
    """
    if page_idx < 2:
        raise ValueError(f"Invalid Bavli page_idx < 2: {page_idx}")
    folio = page_idx // 2 + 1
    amud = "a" if page_idx % 2 == 0 else "b"
    return folio, amud, f"{folio}{amud}"


def daf_to_page_index(folio: int, amud: str) -> int:
    if folio < 2 or amud not in ("a", "b"):
        raise ValueError(f"Invalid daf: {folio}{amud}")
    return (folio - 1) * 2 + (1 if amud == "b" else 0)


def daf_str_to_page_index(daf: str) -> int:
    m = re.fullmatch(r"(\d+)([ab])", daf.strip())
    if not m:
        raise ValueError(f"Invalid daf string: {daf!r}")
    return daf_to_page_index(int(m.group(1)), m.group(2))


def hebrew_numeral(num: int) -> str:
    """Standard Hebrew gematria numeral for daf display (2..176)."""
    if num <= 0:
        return str(num)
    hundreds = ["", "ק", "ר", "ש", "ת"]
    tens = ["", "י", "כ", "ל", "מ", "נ", "ס", "ע", "פ", "צ"]
    ones = ["", "א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט"]
    h = hundreds[num // 100]
    rem = num % 100
    if rem == 15:
        return h + "טו"
    if rem == 16:
        return h + "טז"
    return h + tens[rem // 10] + ones[rem % 10]


def load_bavli_toc(corpus_root: Path) -> list[dict[str, Any]]:
    """Extract ordered Bavli tractate list from Sefaria table_of_contents.json."""
    toc_path = corpus_root / "table_of_contents.json"
    toc = json.loads(toc_path.read_text(encoding="utf-8"))
    tractates: list[dict[str, Any]] = []
    order_idx = 0
    for cat in toc:
        if cat.get("category") != "Talmud":
            continue
        for sub in cat.get("contents", []):
            if sub.get("category") != "Bavli":
                continue
            for seder in sub.get("contents", []):
                seder_name = seder.get("category", "")
                if not seder_name.startswith("Seder "):
                    continue
                for item in seder.get("contents", []):
                    if "title" not in item:
                        continue
                    order_idx += 1
                    tractates.append(
                        {
                            "toc_order": order_idx,
                            "seder": seder_name,
                            "seder_he": seder.get("heCategory", ""),
                            "tractate": item["title"],
                            "tractate_he": item.get("heTitle", ""),
                            "slug": tractate_slug(item["title"]),
                        }
                    )
    if len(tractates) != 37:
        raise RuntimeError(f"Expected 37 Bavli tractates in TOC, found {len(tractates)}")
    return tractates


def _parse_whole_ref_bounds(whole_ref: str, title: str, page_lengths: list[int]) -> tuple[tuple[int, int], tuple[int, int]]:
    prefix = title + " "
    if not whole_ref.startswith(prefix):
        raise ValueError(f"Unexpected wholeRef {whole_ref!r} for {title!r}")
    body = whole_ref[len(prefix) :]
    start_part, end_part = body.split("-", 1)
    sm = re.fullmatch(r"(\d+)([ab])(?::(\d+))?", start_part.strip())
    if not sm:
        raise ValueError(f"Cannot parse chapter start {start_part!r} in {whole_ref!r}")
    s_pidx = daf_to_page_index(int(sm.group(1)), sm.group(2))
    s_sidx = (int(sm.group(3)) - 1) if sm.group(3) else 0

    em = re.fullmatch(r"(?:(\d+)([ab]))?(?::?(\d+))?", end_part.strip())
    if not em or (not em.group(1) and not em.group(3)):
        raise ValueError(f"Cannot parse chapter end {end_part!r} in {whole_ref!r}")
    if em.group(1):
        e_pidx = daf_to_page_index(int(em.group(1)), em.group(2))
        e_sidx = (int(em.group(3)) - 1) if em.group(3) else (page_lengths[e_pidx] - 1)
    else:
        e_pidx = s_pidx
        e_sidx = int(em.group(3)) - 1
    return (s_pidx, s_sidx), (e_pidx, e_sidx)


def load_chapter_lookup(corpus_root: Path, title: str, page_lengths: list[int]) -> list[dict[str, Any]]:
    schema_path = corpus_root / "schemas" / f"{title.replace(' ', '_')}.json"
    schema_doc = json.loads(schema_path.read_text(encoding="utf-8"))
    addr_types = schema_doc.get("schema", {}).get("addressTypes", [])
    if addr_types != ["Talmud", "Integer"]:
        raise ValueError(f"Unexpected addressTypes for {title}: {addr_types}")

    nodes = schema_doc.get("alts", {}).get("Chapters", {}).get("nodes", [])
    chapters: list[dict[str, Any]] = []
    for idx, node in enumerate(nodes, 1):
        ch_num = int(node.get("numeric_equivalent") or idx)
        whole_ref = node["wholeRef"]
        start_pos, end_pos = _parse_whole_ref_bounds(whole_ref, title, page_lengths)
        chapters.append(
            {
                "chapter_num": ch_num,
                "title_en": node.get("title"),
                "title_he": node.get("heTitle"),
                "whole_ref": whole_ref,
                "start_pos": start_pos,
                "end_pos": end_pos,
            }
        )
    return chapters


def lookup_chapter(chapters: list[dict[str, Any]], page_idx: int, seg_idx: int) -> tuple[int, str | None, str | None]:
    pos = (page_idx, seg_idx)
    matched: tuple[int, str | None, str | None] | None = None
    for ch in chapters:
        if ch["start_pos"] <= pos <= ch["end_pos"]:
            matched = (ch["chapter_num"], ch["title_en"], ch["title_he"])
    if matched is not None:
        return matched
    # Fallback to nearest preceding chapter if trailing segment exceeds schema node range
    for ch in reversed(chapters):
        if pos >= ch["start_pos"]:
            return (ch["chapter_num"], ch["title_en"], ch["title_he"])
    return (1, chapters[0]["title_en"] if chapters else None, chapters[0]["title_he"] if chapters else None)


def scan_all_bavli_metadata(corpus_root: Path) -> dict[str, Any]:
    """Scan all 37 Bavli tractates in TOC order and build global source & progress manifests."""
    export_ts_path = corpus_root / "last_export.txt"
    export_timestamp = export_ts_path.read_text(encoding="utf-8").strip() if export_ts_path.exists() else "unknown"
    toc_entries = load_bavli_toc(corpus_root)

    tractate_Summaries: list[dict[str, Any]] = []
    total_segments = 0
    for entry in toc_entries:
        rel_path = Path("json") / "Talmud" / "Bavli" / entry["seder"] / entry["tractate"] / "Hebrew" / EDITION_FILENAME
        abs_path = corpus_root / rel_path
        raw_bytes = abs_path.read_bytes()
        file_sha256 = hashlib.sha256(raw_bytes).hexdigest()
        doc = json.loads(raw_bytes)
        text_arr = doc["text"]

        nonempty_pages = [i for i, p in enumerate(text_arr) if any(s.strip() for s in p)]
        if not nonempty_pages:
            raise RuntimeError(f"No non-empty pages in {entry['tractate']}")
        _, _, start_daf = page_index_to_daf(nonempty_pages[0])
        _, _, end_daf = page_index_to_daf(nonempty_pages[-1])
        internal_empty_dafs = [
            page_index_to_daf(i)[2]
            for i in range(nonempty_pages[0], nonempty_pages[-1] + 1)
            if i not in nonempty_pages
        ]
        seg_count = sum(1 for p in text_arr for s in p if s.strip())
        total_segments += seg_count

        # Verify anchor on Berakhot 2a:1
        if entry["tractate"] == "Berakhot":
            canon_open, _ = normalize_with_offset_map(text_arr[2][0])
            if not canon_open.startswith("מאימתי קורין את שמע בערבין"):
                raise RuntimeError(
                    f"CRITICAL ANCHOR FAILURE on Berakhot 2a:1: got {canon_open[:60]!r}"
                )

        tractate_Summaries.append(
            {
                **entry,
                "source_file_rel": rel_path.as_posix(),
                "source_file_sha256": file_sha256,
                "version_title": doc.get("versionTitle"),
                "version_source": doc.get("versionSource"),
                "license": doc.get("license"),
                "start_daf": start_daf,
                "end_daf": end_daf,
                "start_ref": f"{entry['tractate']} {start_daf}:1",
                "end_ref": f"{entry['tractate']} {end_daf}:{len(text_arr[nonempty_pages[-1]])}",
                "nonempty_amud_count": len(nonempty_pages),
                "internal_empty_dafs": internal_empty_dafs,
                "segment_count": seg_count,
            }
        )

    return {
        "schema_version": SCHEMA_VERSION,
        "source_version_id": SOURCE_VERSION_ID,
        "sefaria_export_timestamp": export_timestamp,
        "edition_title": "William Davidson Edition - Aramaic",
        "edition_filename": EDITION_FILENAME,
        "license": "CC-BY-NC",
        "redistribution_policy": "local_only_cc_by_nc_fulltext_excluded_from_git",
        "normalization_spec_id": NORMALIZATION_SPEC_ID,
        "tractate_count": len(tractate_Summaries),
        "total_bavli_segments": total_segments,
        "anchor_checks_passed": {
            "berakhot_2a_1_meimatai": True,
            "tamid_starts_25b_1": any(
                t["tractate"] == "Tamid" and t["start_daf"] == "25b" for t in tractate_Summaries
            ),
            "nazir_33b_empty_amud_recorded": any(
                t["tractate"] == "Nazir" and t["internal_empty_dafs"] == ["33b"]
                for t in tractate_Summaries
            ),
        },
        "tractates": tractate_Summaries,
    }


def materialize_tractate_segments(
    corpus_root: Path,
    project_root: Path,
    tractate_meta: dict[str, Any],
) -> dict[str, Any]:
    """Write deterministic segments.jsonl (repo-safe) + local_source_cache full-text JSONL."""
    title = tractate_meta["tractate"]
    slug = tractate_meta["slug"]
    he_title = tractate_meta["tractate_he"]
    rel_path = tractate_meta["source_file_rel"]
    abs_path = corpus_root / Path(rel_path)
    raw_bytes = abs_path.read_bytes()
    file_sha256 = hashlib.sha256(raw_bytes).hexdigest()
    assert file_sha256 == tractate_meta["source_file_sha256"]

    doc = json.loads(raw_bytes)
    text_arr: list[list[str]] = doc["text"]
    page_lengths = [len(p) for p in text_arr]
    chapters = load_chapter_lookup(corpus_root, title, page_lengths)

    tractate_dir = project_root / "tractates" / slug
    local_cache_dir = project_root / "local_source_cache" / slug
    tractate_dir.mkdir(parents=True, exist_ok=True)
    local_cache_dir.mkdir(parents=True, exist_ok=True)

    repo_segments_path = tractate_dir / "segments.jsonl"
    local_segments_path = local_cache_dir / "segments.local_fulltext.jsonl"

    repo_lines: list[str] = []
    local_lines: list[str] = []
    segment_hashes: list[str] = []
    ordinal = 0

    for page_idx, page in enumerate(text_arr):
        if not page or not any(s.strip() for s in page):
            continue
        folio_num, amud, daf_str = page_index_to_daf(page_idx)
        he_daf = f"{hebrew_numeral(folio_num)} {'ע״א' if amud == 'a' else 'ע״ב'}"
        for seg_idx, raw_seg in enumerate(page):
            if not raw_seg.strip():
                raise RuntimeError(f"Unexpected empty segment at {title} page_idx={page_idx} seg_idx={seg_idx}")
            seg_num = seg_idx + 1
            canon_text, offset_map = normalize_with_offset_map(raw_seg)
            raw_h = sha256_str(raw_seg)
            canon_h = sha256_str(canon_text)
            ch_num, ch_en, ch_he = lookup_chapter(chapters, page_idx, seg_idx)

            seg_id = f"seg:bavli:{slug}:{daf_str}:{seg_num}"
            ref = f"{title} {daf_str}:{seg_num}"
            he_ref = f"{he_title} {he_daf}:{seg_num}"

            base_rec = {
                "record_type": "segment",
                "schema_version": SCHEMA_VERSION,
                "source_version_id": SOURCE_VERSION_ID,
                "segment_id": seg_id,
                "tractate": title,
                "tractate_he": he_title,
                "seder": tractate_meta["seder"],
                "chapter_num": ch_num,
                "chapter_title_en": ch_en,
                "chapter_title_he": ch_he,
                "daf": daf_str,
                "folio_num": folio_num,
                "amud": amud,
                "segment_num": seg_num,
                "ordinal_in_tractate": ordinal,
                "ref": ref,
                "he_ref": he_ref,
                "raw_array_index": [page_idx, seg_idx],
                "source_file_rel": rel_path,
                "source_file_sha256": file_sha256,
                "license": tractate_meta["license"],
                "redistribution_status": "local_only_cc_by_nc",
                "raw_sha256": raw_h,
                "canonical_sha256": canon_h,
                "raw_char_len": len(raw_seg),
                "canonical_char_len": len(canon_text),
                "normalization_spec_id": NORMALIZATION_SPEC_ID,
                "offset_map": offset_map,
                "raw_text": None,
                "canonical_text": None,
            }
            local_rec = {**base_rec, "raw_text": raw_seg, "canonical_text": canon_text}

            repo_lines.append(json.dumps(base_rec, ensure_ascii=False))
            local_lines.append(json.dumps(local_rec, ensure_ascii=False))
            segment_hashes.append(f"{seg_id}:{canon_h}")
            ordinal += 1

    repo_segments_path.write_text("\n".join(repo_lines) + "\n", encoding="utf-8")
    local_segments_path.write_text("\n".join(local_lines) + "\n", encoding="utf-8")

    inventory_digest = sha256_str("\n".join(segment_hashes))
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "source_version_id": SOURCE_VERSION_ID,
        "tractate": title,
        "tractate_he": he_title,
        "slug": slug,
        "toc_order": tractate_meta["toc_order"],
        "seder": tractate_meta["seder"],
        "source_file_rel": rel_path,
        "source_file_sha256": file_sha256,
        "license": tractate_meta["license"],
        "start_ref": tractate_meta["start_ref"],
        "end_ref": tractate_meta["end_ref"],
        "total_tractate_segments": ordinal,
        "segment_inventory_sha256": inventory_digest,
        "chapters": [
            {
                "chapter_num": c["chapter_num"],
                "title_en": c["title_en"],
                "title_he": c["title_he"],
                "whole_ref": c["whole_ref"],
            }
            for c in chapters
        ],
        "annotation_scope": {
            "mode": "source_inventory_only",
            "covered_daf_range": None,
            "covered_segment_ids_count": 0,
            "tractate_completion_status": "SOURCE_COMPLETE_UNANNOTATED",
        },
    }
    manifest_path = tractate_dir / "manifest.json"
    if not manifest_path.exists():
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    else:
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["annotation_scope"] = existing.get("annotation_scope", manifest["annotation_scope"])
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest
