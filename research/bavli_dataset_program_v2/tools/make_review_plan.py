#!/usr/bin/env python3
"""Freeze a source-only audit plan; this does not perform annotation or review."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile

VERSION = "source-only-block-review-v1"
DOMAIN = b"bavli-source-only-review-plan-v1\0"


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(value):
    return hashlib.sha256(value).hexdigest()


def plan_digest(plan):
    """Hash the canonical complete plan except its top-level plan_sha256 field."""
    return digest(DOMAIN + canonical({k: v for k, v in plan.items()
                                      if k != "plan_sha256"}))


def make_plan(source, tractate, expected_sha256, seed, block_size=10):
    if type(seed) is not int or type(block_size) is not int or block_size < 1:
        raise ValueError("seed must be an integer and block-size a positive integer")
    if not isinstance(expected_sha256, str) or len(expected_sha256) != 64 or any(
            c not in "0123456789abcdefABCDEF" for c in expected_sha256):
        raise ValueError("expected-sha256 must contain 64 hexadecimal characters")
    raw = Path(source).read_bytes()
    source_hash = digest(raw)
    if source_hash != expected_sha256.lower():
        raise ValueError("Source byte SHA-256 mismatch")
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    data = json.loads(raw, object_pairs_hook=unique_keys)
    if not isinstance(data, dict):
        raise ValueError("Source JSON must be an object")
    if data.get("versionTitle") != "Wikisource Talmud Bavli":
        raise ValueError("versionTitle must exactly equal Wikisource Talmud Bavli")
    if data.get("title") != tractate:
        raise ValueError("Source title does not exactly match --tractate")
    if data.get("language") != "he":
        raise ValueError("Source language must exactly equal he")
    pages = data.get("text")
    if not isinstance(pages, list):
        raise ValueError("text must be a two-dimensional array of strings")
    spans, empty_positions, empty_pages, whitespace_positions = [], [], [], []
    for page_index, page in enumerate(pages):
        if not isinstance(page, list):
            raise ValueError("Each text page must be an array of strings")
        if not page:
            empty_pages.append(page_index)
        for segment_index, text in enumerate(page):
            if not isinstance(text, str):
                raise ValueError("Each source segment must be a string")
            daf = f"{page_index // 2 + 1}{'a' if page_index % 2 == 0 else 'b'}"
            span = {"ref": f"{tractate} {daf}:{segment_index + 1}",
                    "page_index": page_index, "segment_index": segment_index,
                    "offsets_codepoints": [0, len(text)],
                    "span_sha256_utf8": digest(text.encode("utf-8"))}
            if not text:
                empty_positions.append(span)
            else:
                span["nonempty_ordinal"] = len(spans)
                spans.append(span)
                if not text.strip():
                    whitespace_positions.append(dict(span))
    if not spans:
        raise ValueError("Source contains no nonempty segments; no review plan created")
    blocks = [{"block_id": f"block_{i // block_size:06d}",
               "spans": spans[i:i + block_size]}
              for i in range(0, len(spans), block_size)]
    count = len(blocks)
    sample_size = min(count, max(30, (count + 9) // 10))

    def rank(block):
        return digest(b"bavli-review-block-rank-v1\0" + canonical(
            {"seed": seed, "source_sha256": source_hash,
             "block_id": block["block_id"]}))

    sampled = {b["block_id"] for b in sorted(
        blocks, key=lambda b: (rank(b), b["block_id"]))[:sample_size]}
    endpoints = {blocks[0]["block_id"], blocks[-1]["block_id"]}
    selected = sampled | endpoints
    review_blocks, grid = [], []
    for block in blocks:
        bid, members = block["block_id"], block["spans"]
        grid.append({"block_id": bid, "nonempty_ordinal_start": members[0]["nonempty_ordinal"],
                     "nonempty_ordinal_end_exclusive": members[-1]["nonempty_ordinal"] + 1,
                     "first_ref": members[0]["ref"], "last_ref": members[-1]["ref"],
                     "membership_sha256": digest(canonical(members))})
        if bid in selected:
            roles = (["probability_sample"] if bid in sampled else [])
            if bid == blocks[0]["block_id"]:
                roles.append("opening_check")
            if bid == blocks[-1]["block_id"]:
                roles.append("closing_check")
            review_blocks.append({**block, "roles": roles,
                                  "inclusion_probability": sample_size / count,
                                  "review_union_inclusion_probability":
                                  1.0 if bid in endpoints else sample_size / count})
    plan = {
        "algorithm_version": VERSION, "status": "PLAN_ONLY_NOT_REVIEWED",
        "tractate": tractate, "source_sha256": source_hash,
        "source_version_title": data["versionTitle"], "source_language": data["language"], "seed": seed,
        "coordinate_contract": "Original zero-based array indices; half-open Unicode codepoint offsets; no normalization",
        "empty_rule": "Only raw empty strings are empty (bool(text)==False); whitespace-only raw strings remain nonempty; no normalization or HTML stripping",
        "source_inventory": {"page_positions": len(pages),
                             "segment_positions": len(spans) + len(empty_positions),
                             "nonempty_segments": len(spans),
                             "empty_segment_positions": empty_positions,
                             "whitespace_only_nonempty_positions": whitespace_positions,
                             "empty_page_indices": empty_pages},
        "sampling": {"block_size_nonempty_segments": block_size,
                     "grid_blocks": count, "sampled_blocks": sample_size,
                     "inclusion_probability_numerator": sample_size,
                     "inclusion_probability_denominator": count,
                     "inclusion_probability_scope": "Probability sample only; mandatory endpoint union is recorded separately",
                     "rank_algorithm": "SHA-256(domain NUL + canonical JSON of seed, source_sha256, block_id); ascending digest then block_id",
                     "rank_domain": "bavli-review-block-rank-v1",
                     "probability_sample_block_ids": sorted(sampled)},
        "endpoint_checks": {"opening_block_id": blocks[0]["block_id"],
                            "closing_block_id": blocks[-1]["block_id"],
                            "overlap_with_probability_sample": sorted(endpoints & sampled),
                            "unique_added_block_ids": sorted(endpoints - sampled)},
        "coverage": {"unique_review_blocks": len(selected),
                     "probability_sample_nonempty_segments": sum(len(b["spans"]) for b in blocks if b["block_id"] in sampled),
                     "unique_review_nonempty_segments": sum(len(b["spans"]) for b in review_blocks)},
        "sampling_grid": grid, "review_blocks": review_blocks,
        "reader_context_policy": "Expansion to full discussions is a later, separately logged reader event; context does not inflate sampled core counts",
        "review_policy": "No worker annotations or flags used. No sugya counts exist until independent reading. AI review is not human certification.",
        "plan_hash_contract": {"algorithm": "SHA-256", "domain": DOMAIN[:-1].decode(),
                               "domain_separator": "one NUL byte",
                               "canonicalization": "UTF-8 JSON; sorted keys; compact separators; ensure_ascii=false; no NaN",
                               "excluded_top_level_field": "plan_sha256"}}
    plan["plan_sha256"] = plan_digest(plan)
    return plan


def publish(path, payload):
    """Publish complete bytes atomically without replacing a competing path."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="wb", dir=path.parent,
                                         prefix=f".{path.name}.", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.link(temporary, path)
        except FileExistsError:
            if path.read_bytes() != payload:
                raise ValueError("Existing frozen plan differs; use a new output path")
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--tractate", required=True)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--seed", required=True, type=int)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--block-size", default=10, type=int)
    args = parser.parse_args(argv)
    try:
        if args.source.resolve() == args.output.resolve():
            raise ValueError("Output must not overwrite the source")
        plan = make_plan(args.source, args.tractate, args.expected_sha256,
                         args.seed, args.block_size)
        output = json.dumps(plan, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        publish(args.output, output.encode("utf-8"))
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print(json.dumps({"plan_sha256": plan["plan_sha256"],
                      "status": plan["status"], **plan["coverage"]}))


if __name__ == "__main__":
    main()
