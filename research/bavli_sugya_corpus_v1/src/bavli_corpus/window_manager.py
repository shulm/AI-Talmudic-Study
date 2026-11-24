"""Bounded overlapping amud-window slicer for deterministic, resumable sugya partitioning."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .normalization import tractate_slug
from .scanner import daf_str_to_page_index


@dataclass(frozen=True)
class AnnotationWindow:
    window_id: str
    tractate: str
    central_dafs: list[str]
    preceding_context_dafs: list[str]
    following_context_dafs: list[str]
    central_segment_ids: list[str]
    preceding_segment_ids: list[str]
    following_segment_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "window_id": self.window_id,
            "tractate": self.tractate,
            "central_dafs": self.central_dafs,
            "preceding_context_dafs": self.preceding_context_dafs,
            "following_context_dafs": self.following_context_dafs,
            "central_segment_ids": self.central_segment_ids,
            "preceding_segment_ids": self.preceding_segment_ids,
            "following_segment_ids": self.following_segment_ids,
        }


def filter_segments_by_daf_range(
    segments: list[dict[str, Any]], start_daf: str | None = None, end_daf: str | None = None
) -> list[dict[str, Any]]:
    s_idx = daf_str_to_page_index(start_daf) if start_daf else 0
    e_idx = daf_str_to_page_index(end_daf) if end_daf else 10**9
    return [
        seg
        for seg in segments
        if s_idx <= seg["raw_array_index"][0] <= e_idx
    ]


def build_overlapping_windows(
    all_tractate_segments: list[dict[str, Any]],
    start_daf: str | None = None,
    end_daf: str | None = None,
    central_amudim: int = 2,
    context_before_amudim: int = 1,
    context_after_amudim: int = 1,
) -> list[AnnotationWindow]:
    """Partition target segments into bounded windows of `central_amudim` with context overlap."""
    if not all_tractate_segments:
        return []
    tractate = all_tractate_segments[0]["tractate"]
    slug = tractate_slug(tractate)

    # Group all tractate segments by ordered daf appearance so surrounding context outside slice is also available!
    ordered_dafs: list[str] = []
    by_daf: dict[str, list[dict[str, Any]]] = {}
    for seg in all_tractate_segments:
        d = seg["daf"]
        if d not in by_daf:
            ordered_dafs.append(d)
            by_daf[d] = []
        by_daf[d].append(seg)

    s_pidx = daf_str_to_page_index(start_daf) if start_daf else 0
    e_pidx = daf_str_to_page_index(end_daf) if end_daf else 10**9
    target_daf_indices = [
        idx
        for idx, d in enumerate(ordered_dafs)
        if s_pidx <= daf_str_to_page_index(d) <= e_pidx
    ]
    if not target_daf_indices:
        raise ValueError(f"No segments found in {tractate} for range {start_daf}..{end_daf}")

    windows: list[AnnotationWindow] = []
    win_num = 0
    for pos in range(0, len(target_daf_indices), central_amudim):
        win_num += 1
        c_indices = target_daf_indices[pos : pos + central_amudim]
        first_i, last_i = c_indices[0], c_indices[-1]
        prev_indices = list(range(max(0, first_i - context_before_amudim), first_i))
        next_indices = list(
            range(last_i + 1, min(len(ordered_dafs), last_i + 1 + context_after_amudim))
        )

        c_dafs = [ordered_dafs[i] for i in c_indices]
        p_dafs = [ordered_dafs[i] for i in prev_indices]
        n_dafs = [ordered_dafs[i] for i in next_indices]

        win_id = f"win:bavli:{slug}:w{win_num:03d}:{c_dafs[0]}_{c_dafs[-1]}"
        windows.append(
            AnnotationWindow(
                window_id=win_id,
                tractate=tractate,
                central_dafs=c_dafs,
                preceding_context_dafs=p_dafs,
                following_context_dafs=n_dafs,
                central_segment_ids=[s["segment_id"] for d in c_dafs for s in by_daf[d]],
                preceding_segment_ids=[s["segment_id"] for d in p_dafs for s in by_daf[d]],
                following_segment_ids=[s["segment_id"] for d in n_dafs for s in by_daf[d]],
            )
        )
    return windows
