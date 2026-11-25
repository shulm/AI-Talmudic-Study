#!/usr/bin/env python3
"""Build a deterministic, unclaimed job queue; never run annotations or models.

The CLI accepts only the exact pinned historical inventory/progress metadata.
It does not verify original text bytes or execute/update runtime progress.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import tempfile

BASE_COMMIT = "ef29310b50575ac2441ce59d0c68d58424f4b823"
PINNED_MANIFEST_SHA256 = "11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c"
PINNED_PROGRESS_SHA256 = "a3e1fd409ba1ed43d3f3fd5c98fbf9bdfde66b76c2fe8b57285d3942e15dc602"
PROTOCOL_VERSION = "2.0.0-design"
EDITION = "Wikisource Talmud Bavli"
FIRST_WAVE = ("Berakhot", "Bava Metzia", "Rosh Hashanah", "Taanit")
PILOTS = {
    "Berakhot": (151, "dd24d48aef18159564471380f7ba200302cc9889b22380aef724d2fb086a9d38"),
    "Bava Metzia": (64, "2ba697d1185eaf618c5e99fc254d849744375cfcd03ddbbd1d46751a2fb4b84b"),
}


class InputError(ValueError):
    """Input metadata cannot safely define this queue."""


def require(condition, message):
    if not condition:
        raise InputError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def integer(value, label, minimum=0):
    require(type(value) is int and value >= minimum, f"{label}: expected integer >= {minimum}")
    return value


def string(value, label):
    require(isinstance(value, str) and bool(value.strip()), f"{label}: expected nonempty string")
    return value


def sha256(value, label):
    require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value),
            f"{label}: expected lowercase SHA-256")


def relative_path(value, label):
    string(value, label)
    require("\\" not in value and ":" not in value and
            not PurePosixPath(value).is_absolute() and
            all(part not in ("", ".", "..") for part in value.split("/")),
            f"{label}: expected canonical relative POSIX path")


def parse_json(data, label):
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"{label}: duplicate JSON key {key!r}")
            result[key] = value
        return result
    try:
        result = json.loads(data.decode("utf-8-sig"), object_pairs_hook=unique_keys)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise InputError(f"{label}: invalid UTF-8 JSON: {exc}") from exc
    require(isinstance(result, dict), f"{label}: expected JSON object")
    return result


def continuation_plan(source, historical):
    title = source["title"]
    plan = {"whole_tractate_target": True,
            "first_source_ref": source["first_nonempty_ref"],
            "must_reverify_historical_pilot_before_reuse": True,
            "mode": "process_full_source_from_beginning",
            "resume_core_start_ref": source["first_nonempty_ref"]}
    if title in PILOTS:
        count, expected_sha = PILOTS[title]
        require(historical["pilot_segments"] == count and source["source_sha256"] == expected_sha,
                f"{title}: pilot lineage requires the pinned source hash and historical count")
    if title == "Berakhot":
        plan.update(mode="preserve_prefix_pilot_and_extend_open_tail",
                    prior_pilot_covered=151,
                    prior_pilot_end_ref="Berakhot 5a:24",
                    resume_core_start_ref="Berakhot 5b:1",
                    inherited_open_sugya_authoring_key="B24",
                    inherited_open_sugya_id="sug_9a1c712c3a26fe45003b",
                    inherited_open_sugya_start_ref="Berakhot 5a:24",
                    inherited_tail_requires_full_original_evidence=True)
    elif title == "Bava Metzia":
        plan.update(mode="interior_pilot_requires_prefix_and_suffix",
                    prior_pilot_covered=64,
                    historical_pilot_amud_range="Bava Metzia 21a–22b",
                    inherited_open_tail_source_range="Bava Metzia 22b:11–16",
                    inherited_tail_continues_into_amud="Bava Metzia 23a",
                    must_process_before_and_after_pilot=True,
                    do_not_treat_pilot_as_completed_prefix=True)
    return plan


def build_queue(manifest_bytes, progress_bytes):
    """Check consistency; fixture/external inputs remain explicitly unverified."""
    manifest = parse_json(manifest_bytes, "source manifest")
    progress = parse_json(progress_bytes, "progress manifest")
    require(manifest.get("edition") == EDITION, "source manifest: unexpected/mixed edition")
    sha256(manifest.get("source_toc_sha256"), "source_toc_sha256")
    sources = manifest.get("tractates")
    histories = progress.get("tractates")
    require(isinstance(sources, list) and sources, "source manifest: tractates must be a nonempty list")
    require(isinstance(histories, list), "progress manifest: tractates must be a list")
    titles, slugs, paths, source_hashes, ordinals = set(), set(), set(), set(), set()
    for source in sources:
        require(isinstance(source, dict), "source manifest: tractate row must be an object")
        title = string(source.get("title"), "tractate title")
        slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
        require(slug and title not in titles and slug not in slugs, f"duplicate tractate/slug: {title}")
        titles.add(title)
        slugs.add(slug)
        ordinal = integer(source.get("ordinal"), f"{title}.ordinal", 1)
        require(ordinal not in ordinals, f"duplicate TOC ordinal: {ordinal}")
        ordinals.add(ordinal)
        for key in ("source_path", "schema_path"):
            relative_path(source.get(key), f"{title}.{key}")
        require(source["source_path"] not in paths, f"duplicate source path: {source['source_path']}")
        paths.add(source["source_path"])
        for key in ("source_sha256", "schema_sha256"):
            sha256(source.get(key), f"{title}.{key}")
        require(source["source_sha256"] not in source_hashes, f"duplicate source hash: {title}")
        source_hashes.add(source["source_sha256"])
        count = integer(source.get("source_segments"), f"{title}.source_segments", 1)
        nonempty = integer(source.get("nonempty_segments"), f"{title}.nonempty_segments", 1)
        require(nonempty <= count, f"{title}: nonempty_segments exceeds source_segments")
        integer(source.get("page_slots"), f"{title}.page_slots", 1)
        first_ref = string(source.get("first_nonempty_ref"), f"{title}.first_nonempty_ref")
        require(first_ref.startswith(title + " "), f"{title}: mismatched first source reference")
        metadata = source.get("metadata")
        require(isinstance(metadata, dict), f"{title}: metadata missing")
        require(metadata.get("title") == title and metadata.get("versionTitle") == EDITION and
                metadata.get("language") == "he", f"{title}: mismatched source identity/edition/language")
        string(metadata.get("license"), f"{title}.metadata.license")
    require([s["ordinal"] for s in sources] == list(range(1, len(sources) + 1)),
            "source manifest: rows must preserve contiguous pinned TOC order")
    historical_by_title = {}
    source_by_title = {s["title"]: s for s in sources}
    for historical in histories:
        require(isinstance(historical, dict), "progress manifest: tractate row must be an object")
        title = string(historical.get("tractate"), "progress tractate")
        require(title not in historical_by_title, f"duplicate progress tractate: {title}")
        require(title in source_by_title, f"unknown progress tractate: {title}")
        source = source_by_title[title]
        for key in ("ordinal", "source_segments", "pilot_segments", "primary_sugyot",
                    "statements", "questions", "positions", "uncertain_records"):
            integer(historical.get(key), f"{title}.historical.{key}")
        require(historical["ordinal"] == source["ordinal"] and
                historical["source_segments"] == source["source_segments"],
                f"{title}: source/progress denominator or ordinal mismatch")
        require(historical["pilot_segments"] <= source["source_segments"],
                f"{title}: pilot count exceeds source denominator")
        require(historical.get("completed_masechet") is False,
                f"{title}: this builder requires the incomplete historical pilot baseline")
        expected_status = "pilot_partial_semantics" if historical["pilot_segments"] else "inventory_only"
        require(historical.get("status") == expected_status, f"{title}: inconsistent historical status")
        historical_by_title[title] = historical
    require(set(historical_by_title) == titles, "source/progress tractate sets differ")
    require(type(progress.get("completed_masechtot")) is int and progress["completed_masechtot"] == 0,
            "progress manifest: historical completed_masechtot must equal zero")
    total = sum(s["source_segments"] for s in sources)
    for obj, label in ((manifest, "source"), (progress, "progress")):
        if "total_source_segments" in obj:
            require(integer(obj["total_source_segments"], label + ".total_source_segments") == total,
                    f"{label}: total_source_segments does not match rows")
    ordered = [source_by_title[t] for t in FIRST_WAVE if t in source_by_title]
    ordered.extend(s for s in sources if s["title"] not in FIRST_WAVE)
    jobs = []
    for priority, source in enumerate(ordered, 1):
        title = source["title"]
        historical = historical_by_title[title]
        slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
        jobs.append({
            "job_id": "bavli_" + slug,
            "protocol_version": PROTOCOL_VERSION,
            "base_commit": None,
            "queue_priority": priority,
            "first_wave": title in FIRST_WAVE,
            "pinned_toc_ordinal": source["ordinal"],
            "tractate": title,
            "tractate_he": source.get("he_title"),
            "edition": EDITION,
            "source_path": source["source_path"],
            "expected_source_sha256": source["source_sha256"],
            "source_schema_path": source["schema_path"],
            "source_schema_sha256": source["schema_sha256"],
            "expected_total_source_segments": source["source_segments"],
            "source_license_metadata": source["metadata"]["license"],
            "historical_pilot": dict(historical),
            "continuation_plan": continuation_plan(source, historical),
            "runtime_initialization_template": {
                "status": "queued_unclaimed", "owner_agent": None,
                "source_bytes_verified": False, "processed_source_segments": 0,
                "independently_reviewed_source_segments": 0, "completed_tractate": False,
                "model_calls_made": 0, "ml_eligible_records": 0},
            "readiness": "requires_original_source_and_implemented_production_driver",
        })
    return {
        "queue_contract_version": PROTOCOL_VERSION,
        "project": "shulm/AI-Talmudic-Study",
        "artifact_kind": "deterministic_job_specifications_not_execution",
        "base_commit": None,
        "historical_template_commit": BASE_COMMIT,
        "input_provenance": {"status": "unverified_metadata_inputs",
                             "verified_against_commit": None,
                             "original_source_files_verified": False},
        "source_manifest_sha256": digest(manifest_bytes),
        "progress_manifest_sha256": digest(progress_bytes),
        "source_toc_sha256": manifest["source_toc_sha256"],
        "source_root_hint": manifest.get("source_root_hint"),
        "edition": EDITION,
        "tractate_count": len(jobs),
        "total_source_segments": total,
        "historical_pilot_source_segments": sum(h["pilot_segments"] for h in histories),
        "runtime_initialization_template": {"processed_source_segments": 0,
                                            "completed_tractates": 0,
                                            "source_bytes_verified": False},
        "first_wave_order": [t for t in FIRST_WAVE if t in titles],
        "authorization": {"new_paid_api_budget_usd": 0, "merge_allowed": False},
        "jobs": jobs,
    }


def encode_queue(queue):
    return (json.dumps(queue, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def build_pinned_queue(manifest_bytes, progress_bytes):
    require(digest(manifest_bytes) == PINNED_MANIFEST_SHA256,
            "source manifest differs from the pinned historical baseline")
    require(digest(progress_bytes) == PINNED_PROGRESS_SHA256,
            "progress manifest differs from the pinned historical baseline")
    queue = build_queue(manifest_bytes, progress_bytes)
    queue["base_commit"] = BASE_COMMIT
    queue["input_provenance"]["status"] = "verified_pinned_metadata_baseline"
    queue["input_provenance"]["verified_against_commit"] = BASE_COMMIT
    for job in queue["jobs"]:
        job["base_commit"] = BASE_COMMIT
    return queue


def publish_frozen(output_path, content):
    """Publish complete bytes atomically without replacing any existing file."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.exists():
        require(output_path.read_bytes() == content,
                "existing job specification differs; choose a new output path")
        return
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(mode="wb", dir=output_path.parent,
                                         prefix=f".{output_path.name}.", suffix=".tmp",
                                         delete=False) as handle:
            temporary_path = Path(handle.name)
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.link(temporary_path, output_path)
        except FileExistsError:
            require(output_path.read_bytes() == content,
                    "existing job specification differs; choose a new output path")
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--progress", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        require(args.output.resolve() not in (args.manifest.resolve(), args.progress.resolve()),
                "output must not overwrite either input manifest")
        output = encode_queue(build_pinned_queue(args.manifest.read_bytes(), args.progress.read_bytes()))
        publish_frozen(args.output, output)
    except (InputError, OSError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 2
    queue = json.loads(output)
    print(json.dumps({"jobs": len(queue["jobs"]), "source_segments": queue["total_source_segments"],
                      "historical_pilot_segments": queue["historical_pilot_source_segments"],
                      "runtime_initialization_only": True,
                      "input_provenance": queue["input_provenance"]["status"],
                      "jobs_sha256": digest(output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
