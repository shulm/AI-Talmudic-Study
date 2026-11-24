"""Reversible canonical text normalization and exact quote-span alignment."""
from __future__ import annotations

import hashlib
import html
import re
from typing import Any


TAG_RE = re.compile(r"<[^>]+>")
ENTITY_RE = re.compile(r"&[a-zA-Z0-9#]+;")


def sha256_str(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def tractate_slug(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", title.strip().lower()).strip("_")


def normalize_with_offset_map(raw_text: str) -> tuple[str, list[list[int]]]:
    """Strip HTML tags and collapse whitespace while maintaining an exact reversible map.

    Returns:
        canonical_text: normalized string
        offset_map: list of [canon_start, canon_end, raw_start, raw_end] contiguous runs.
    """
    n = len(raw_text)
    i = 0
    # Collect (char, raw_start, raw_end) tokens after stripping <...> tags and decoding entities
    tokens: list[tuple[str, int, int]] = []
    while i < n:
        if raw_text[i] == "<":
            m = TAG_RE.match(raw_text, i)
            if m:
                tag_lower = m.group(0).lower()
                if tag_lower.startswith("<br"):
                    tokens.append((" ", i, m.end()))
                i = m.end()
                continue
        if raw_text[i] == "&":
            em = ENTITY_RE.match(raw_text, i)
            if em:
                decoded = html.unescape(em.group(0))
                for ch in decoded:
                    tokens.append((ch, i, em.end()))
                i = em.end()
                continue
        tokens.append((raw_text[i], i, i + 1))
        i += 1

    # Collapse whitespace runs to a single ASCII space and trim leading/trailing whitespace
    collapsed: list[tuple[str, int, int]] = []
    in_ws = True  # True trims leading whitespace
    ws_start = 0
    for ch, r_start, r_end in tokens:
        if ch.isspace():
            if not in_ws:
                ws_start = r_start
                in_ws = True
            ws_end = r_end
        else:
            if in_ws and collapsed:
                collapsed.append((" ", ws_start, ws_end))
            in_ws = False
            collapsed.append((ch, r_start, r_end))

    canon_chars: list[str] = []
    runs: list[list[int]] = []
    for c_idx, (ch, r_start, r_end) in enumerate(collapsed):
        canon_chars.append(ch)
        # Merge contiguous 1-to-1 character runs
        if (
            runs
            and r_end - r_start == 1
            and runs[-1][1] == c_idx
            and runs[-1][3] == r_start
            and (runs[-1][3] - runs[-1][2]) == (runs[-1][1] - runs[-1][0])
        ):
            runs[-1][1] = c_idx + 1
            runs[-1][3] = r_end
        else:
            runs.append([c_idx, c_idx + 1, r_start, r_end])

    return "".join(canon_chars), runs


def project_canon_span_to_raw(
    offset_map: list[list[int]], start_char: int, end_char: int
) -> tuple[int, int]:
    """Map [start_char, end_char) in canonical_text back to bounding [raw_start, raw_end) in raw_text."""
    if start_char < 0 or end_char <= start_char:
        raise ValueError(f"Invalid canonical span: [{start_char}, {end_char})")
    raw_start: int | None = None
    raw_end: int | None = None
    for c_s, c_e, r_s, r_e in offset_map:
        if c_e <= start_char:
            continue
        if c_s >= end_char:
            break
        is_one_to_one = (c_e - c_s) == (r_e - r_s)
        if raw_start is None:
            if start_char >= c_s:
                raw_start = r_s + (start_char - c_s) if is_one_to_one else r_s
            else:
                raw_start = r_s
        if end_char <= c_e:
            raw_end = r_s + (end_char - c_s) if is_one_to_one else r_e
        else:
            raw_end = r_e
    if raw_start is None or raw_end is None or raw_end <= raw_start:
        raise ValueError(f"Span [{start_char}, {end_char}) out of offset_map bounds")
    return raw_start, raw_end


def build_anchor(
    segment_id: str,
    canonical_text: str,
    quote: str,
    occurrence: int = 0,
    allow_unaligned: bool = False,
) -> dict[str, Any]:
    """Locate exact substring `quote` inside `canonical_text` and build a validated anchor."""
    quote_clean = " ".join(quote.split())
    if not quote_clean:
        raise ValueError(f"Empty quote for {segment_id}")

    start = -1
    search_from = 0
    for _ in range(occurrence + 1):
        idx = canonical_text.find(quote_clean, search_from)
        if idx == -1:
            start = -1
            break
        start = idx
        search_from = idx + 1

    if start == -1:
        if not allow_unaligned:
            raise ValueError(
                f"Exact substring alignment failed in {segment_id}: {quote_clean!r} not in {canonical_text!r}"
            )
        return {
            "segment_id": segment_id,
            "start_char": None,
            "end_char": None,
            "quote": quote_clean,
            "quote_sha256": sha256_str(quote_clean),
            "alignment_status": "unaligned_needs_review",
        }

    end = start + len(quote_clean)
    assert canonical_text[start:end] == quote_clean
    return {
        "segment_id": segment_id,
        "start_char": start,
        "end_char": end,
        "quote": quote_clean,
        "quote_sha256": sha256_str(quote_clean),
        "alignment_status": "exact",
    }
