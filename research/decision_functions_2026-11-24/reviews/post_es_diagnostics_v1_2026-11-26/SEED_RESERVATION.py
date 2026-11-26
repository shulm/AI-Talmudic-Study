#!/usr/bin/env python3
"""Reserve deterministic seed integers without instantiating a research RNG.

Example with historical-source validation:
    python SEED_RESERVATION.py --output SEEDS.json \
        --receipt SEED_RESERVATION.json --seed-sources /path/to/source_export.json

The optional source export is a JSON list of {path, ref, content} objects.
Without it, the same bank is produced, but historical disjointness is explicitly
NOT_CHECKED. This program imports no project, NumPy, or model code.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import platform


NAMESPACE = "AI-Talmudic-Study/uncapped_single_history_confirmation_v1/2026-11-26"
WORLD_IDS = tuple(f"U{i:03d}" for i in range(82))
ROLES = ("generator", "label", "mask", "H1_support", "H2_support")
MAIN_REF = "16ef28b105ff6c28ee3f822b1409f076fa895318"
PR18_REF = "cdcafb41726820265bd4e1dea5272702f2663aae"
PR18_PATH = "research/decision_functions_2026-11-24/proposals/short_history_null_control_v1/SEEDS.json"
PR18_INCORRECT_INPUT_PATH = "labs/decision_functions_short_history_null_control_v1/SEEDS.json"
EXPECTED_SOURCES = {
    "labs/decision_functions_diagnostics/synthetic.py": (
        MAIN_REF, "2ab32a9193b0f02cc943591f0c5ba8970ca73e45a585bb93b1176ff2aaecfe24"),
    "research/decision_functions_2026-11-24/runs/evidence_shrinkage_v1/PROTOCOL.json": (
        MAIN_REF, "71db7e5abb779f026a81c670ecf9095cbd2d8630bba17011d29a730f96f0f6f0"),
    "research/decision_functions_2026-11-24/runs/interaction_diagnostics_v2/PROTOCOL.json": (
        MAIN_REF, "5d439d62d17b29bd4224ccf75eb92651868847b516db5d881f72b92f86857f4a"),
    "research/decision_functions_2026-11-24/runs/short_history_v1/PROTOCOL.json": (
        MAIN_REF, "f0c838a2e12734a9fa90c3ea5c56bb1ae141ef183124b4a4a3132af0603ea6fa"),
    PR18_PATH: (
        PR18_REF, "dbfd8042b38de89ed72e9649746b18f4925a55e579da2ddbfd50a95d44cf688a"),
}
SEED_FIELDS = frozenset({
    "seed", "seeds", "generator_seed", "label_seed", "mask_seed",
    "initialization_seeds", "schedule_seed", "schedule_seeds", "history_seed",
})
NONSEED_NUMERIC_FIELDS = frozenset({
    "prior_atoms_per_seed", "DP_columns_per_seed_history", "seed_bank_pairs",
})


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")


def derive_bank() -> tuple[dict, set[int]]:
    rows = []
    all_values = []
    for world in WORLD_IDS:
        row = {"id": world}
        for role in ROLES:
            message = f"{NAMESPACE}/{world}/{role}".encode("utf-8")
            value = int.from_bytes(hashlib.sha256(message).digest()[:8], "big", signed=False)
            row[role] = str(value)
            all_values.append(value)
        rows.append(row)
    duplicates = sorted(value for value, count in Counter(all_values).items() if count != 1)
    require(not duplicates, "Seed collision: stop; changing namespace or redrawing is prohibited")
    require(len(all_values) == 410 and len(set(all_values)) == 410, "Seed-count mismatch")
    require(all(0 <= value < 2**64 for value in all_values), "Non-uint64 seed")
    return {"namespace": NAMESPACE, "roles": list(ROLES), "worlds": rows}, set(all_values)


def numeric_seed_leaves(value: object, location: str) -> list[dict]:
    if isinstance(value, int) and not isinstance(value, bool):
        require(value >= 0, f"Negative seed at {location}")
        return [{"location": location, "value": str(value)}]
    if isinstance(value, list):
        return [entry for i, child in enumerate(value)
                for entry in numeric_seed_leaves(child, f"{location}/{i}")]
    raise ValueError(f"Unsupported structured seed value at {location}")


def json_seed_entries(value: object, location: str = "") -> list[dict]:
    entries = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_location = f"{location}/{key}"
            if key in SEED_FIELDS:
                entries.extend(numeric_seed_leaves(child, child_location))
            else:
                if "seed" in key.lower() and isinstance(child, int) and not isinstance(child, bool):
                    require(key in NONSEED_NUMERIC_FIELDS,
                            f"Unclassified numeric seed-like field: {child_location}")
                entries.extend(json_seed_entries(child, child_location))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            entries.extend(json_seed_entries(child, f"{location}/{i}"))
    return entries


def python_seed_entries(content: str) -> list[dict]:
    """Parse literals only; never import or execute the historical program."""
    entries = []
    for node in ast.walk(ast.parse(content)):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "SEEDS" for target in node.targets
        ):
            entries.extend(numeric_seed_leaves(ast.literal_eval(node.value),
                                              f"line:{node.lineno}/SEEDS"))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in ("default_rng", "PCG64", "RandomState"):
                require(bool(node.args), f"RNG seed not explicit at line {node.lineno}")
                entries.extend(numeric_seed_leaves(ast.literal_eval(node.args[0]),
                                                  f"line:{node.lineno}/{node.func.attr}/arg0"))
    require(len(entries) == 5, "Historical synthetic seed-extraction count changed")
    return sorted(entries, key=lambda entry: entry["location"])


def validate_sources(source_path: Path, new_values: set[int]) -> dict:
    raw = source_path.read_bytes()
    exported = json.loads(raw)
    require(isinstance(exported, list) and len(exported) == 5,
            "Expected exactly five historical source exports")
    records = []
    observed_paths = []
    union = set()
    for item in exported:
        require(isinstance(item, dict) and {"path", "ref", "content"} <= set(item),
                "Malformed historical source export")
        supplied_path = item["path"]
        canonical_path = PR18_PATH if supplied_path == PR18_INCORRECT_INPUT_PATH else supplied_path
        require(canonical_path in EXPECTED_SOURCES, "Unexpected historical source path")
        expected_ref, expected_hash = EXPECTED_SOURCES[canonical_path]
        require(item["ref"] == expected_ref, "Historical source revision mismatch")
        require(isinstance(item["content"], str), "Source content must be a string")
        content = item["content"].encode("utf-8")
        require(sha256(content) == expected_hash, "Historical source content hash mismatch")
        entries = (python_seed_entries(item["content"]) if canonical_path.endswith(".py")
                   else json_seed_entries(json.loads(item["content"])))
        values = {int(entry["value"]) for entry in entries}
        overlap = new_values & values
        require(not overlap, "Historical seed collision: stop; no replacement seed is allowed")
        if canonical_path == PR18_PATH:
            require(len(entries) == len(values) == 216, "PR18 must reserve exactly 216 values")
        observed_paths.append(canonical_path)
        union.update(values)
        records.append({
            "path": canonical_path,
            "supplied_path": supplied_path,
            "path_label_corrected": canonical_path != supplied_path,
            "ref": item["ref"],
            "content_sha256": sha256(content),
            "content_utf8_bytes": len(content),
            "seed_value_occurrences": len(entries),
            "unique_seed_value_count": len(values),
            "extracted_values": [str(value) for value in sorted(values)],
            "extraction_locations": entries,
            "overlap_with_new_bank": [],
        })
    require(len(set(observed_paths)) == 5 and set(observed_paths) == set(EXPECTED_SOURCES),
            "Missing or repeated historical source")
    require(len(union) == 245, "Historical union must contain 245 distinct values")
    return {
        "status": "PASSED_FOR_THE_FIVE_BOUND_SOURCE_EXPORTS",
        "source_export_filename": source_path.name,
        "source_export_sha256": sha256(raw),
        "source_export_bytes": len(raw),
        "source_count": len(records),
        "sources": sorted(records, key=lambda record: record["path"]),
        "all_unique_excluded_values": [str(value) for value in sorted(union)],
        "unique_excluded_count": len(union),
        "pr18_unique_excluded_count": 216,
        "other_sources_unique_excluded_count": 29,
        "overlap_with_new_bank": [],
        "extraction_rule": "Exact listed JSON seed fields and literal SEEDS/default_rng/PCG64/RandomState inputs in the supplied Python source; source code is parsed, never executed.",
        "json_seed_fields": sorted(SEED_FIELDS),
        "nonseed_numeric_fields_excluded": sorted(NONSEED_NUMERIC_FIELDS),
        "coverage_limit": "These five pinned supplied source exports; not an exhaustive repository-wide seed audit or an independent network retrieval.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Explicit seed-bank JSON path")
    parser.add_argument("--receipt", type=Path, required=True, help="Explicit reservation-receipt JSON path")
    parser.add_argument("--seed-sources", type=Path, help="Optional historical {path,ref,content} JSON export")
    args = parser.parse_args()
    targets = {args.output.resolve(), args.receipt.resolve()}
    require(len(targets) == 2, "Output and receipt paths must differ")
    require(Path(__file__).resolve() not in targets, "Cannot overwrite this script")
    if args.seed_sources is not None:
        require(args.seed_sources.resolve() not in targets, "Cannot overwrite historical source input")
    bank, values = derive_bank()
    history = (validate_sources(args.seed_sources, values) if args.seed_sources is not None else {
        "status": "NOT_CHECKED",
        "source_count": 0,
        "overlap_with_new_bank": None,
        "reason": "No --seed-sources supplied; unique deterministic reservation is not evidence of historical disjointness.",
    })
    bank_bytes = json_bytes(bank)
    receipt = {
        "status": "RESERVED_NOT_MATERIALIZED",
        "scope": {
            "research_rng_instances": 0,
            "random_draws": 0,
            "worlds_generated": 0,
            "shared_fits": 0,
            "personal_solves": 0,
            "model_or_data_downloads": 0,
            "project_modules_imported": False,
            "scientific_launch_authorized_by_this_receipt": False,
        },
        "environment": {
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "script_sha256": sha256(Path(__file__).read_bytes()),
            "external_python_dependencies": [],
        },
        "bank_filename": args.output.name,
        "bank_sha256": sha256(bank_bytes),
        "bank_bytes": len(bank_bytes),
        "world_count": len(WORLD_IDS),
        "world_ids": list(WORLD_IDS),
        "roles_in_derivation_order": list(ROLES),
        "seed_count": len(values),
        "unique_seed_count": len(values),
        "internal_collisions": [],
        "derivation": {
            "namespace": NAMESPACE,
            "message": "namespace + '/' + world_id + '/' + role",
            "encoding": "UTF-8",
            "world_id_format": "U followed by exactly three decimal digits, U000 through U081",
            "role_spelling": "Exactly one of generator, label, mask, H1_support, H2_support; case-sensitive",
            "extra_spaces_or_newline": False,
            "hash": "SHA-256",
            "digest_selection": "digest()[0:8] (first eight bytes)",
            "integer_interpretation": "unsigned, big-endian",
            "serialization": "base-10 strings without leading zeros, except zero itself",
            "future_rng": "Separate NumPy PCG64 instance initialized with int(decimal_seed_string) for each world/role",
            "collision_policy": "Stop without changing namespace, selecting a suffix, redrawing, or reserving replacement worlds",
        },
        "historical_validation": history,
        "shared_training_starts_outside_reserved_roles": [11, 29, 47],
        "shared_training_note": "The three inherited training starts are fixed algorithm inputs; the no-overlap check concerns the 410 newly reserved world/role seeds.",
        "independence_statement": "Distinct hashes and seed integers provide deterministic domain separation. Independence of future PCG64 streams is a pseudorandom modeling assumption, not a theorem proved by this reservation; no stream has been instantiated.",
    }
    # Both collision validations finish before either deliverable is written.
    for path, data in ((args.output, bank_bytes), (args.receipt, json_bytes(receipt))):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    print(json.dumps({"status": receipt["status"], "worlds": len(WORLD_IDS),
                      "seeds": len(values), "historical_validation": history["status"],
                      "bank_sha256": receipt["bank_sha256"]}))


if __name__ == "__main__":
    main()
