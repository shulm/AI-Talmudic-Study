"""Command-line interface for Bavli Sugya Corpus v1."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .annotation_runner import compile_tractate_annotations_from_spec
from .queries import derive_eligible_qa_candidates, find_scholar_statements, reconstruct_sugya
from .scanner import materialize_tractate_segments, scan_all_bavli_metadata
from .validators import load_jsonl, validate_tractate_bundle


DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parents[2]


def cmd_scan(args: argparse.Namespace) -> int:
    corpus_root = Path(args.corpus_root)
    project_root = Path(args.project_root)

    global_meta = scan_all_bavli_metadata(corpus_root)
    (project_root / "source_version_manifest.json").write_text(
        json.dumps(global_meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    wanted = {t.lower() for t in args.tractates} if args.tractates else None
    progress_entries = []
    for t_meta in global_meta["tractates"]:
        should_mat = wanted is None or t_meta["tractate"].lower() in wanted or t_meta["slug"] in wanted
        status = "NOT_STARTED"
        annotated_segs = 0
        if should_mat:
            m = materialize_tractate_segments(corpus_root, project_root, t_meta)
            status = m["annotation_scope"]["tractate_completion_status"]
            annotated_segs = m["annotation_scope"]["covered_segment_ids_count"]
        else:
            existing_m = project_root / "tractates" / t_meta["slug"] / "manifest.json"
            if existing_m.exists():
                m = json.loads(existing_m.read_text(encoding="utf-8"))
                status = m["annotation_scope"]["tractate_completion_status"]
                annotated_segs = m["annotation_scope"]["covered_segment_ids_count"]
        progress_entries.append(
            {
                "toc_order": t_meta["toc_order"],
                "seder": t_meta["seder"],
                "tractate": t_meta["tractate"],
                "tractate_he": t_meta["tractate_he"],
                "slug": t_meta["slug"],
                "start_ref": t_meta["start_ref"],
                "end_ref": t_meta["end_ref"],
                "total_segments": t_meta["segment_count"],
                "annotated_segments": annotated_segs,
                "status": status,
            }
        )

    progress_doc = {
        "schema_version": global_meta["schema_version"],
        "source_version_id": global_meta["source_version_id"],
        "total_bavli_tractates": len(progress_entries),
        "total_bavli_segments": global_meta["total_bavli_segments"],
        "completed_full_tractates": sum(
            1 for p in progress_entries if p["status"] == "PROVISIONAL_TRACTATE_COMPLETE"
        ),
        "pilot_slices_active": sum(
            1 for p in progress_entries if p["status"] == "PILOT_SLICE_PROVISIONAL_COMPLETE"
        ),
        "tractates": progress_entries,
    }
    (project_root / "tractate_progress.json").write_text(
        json.dumps(progress_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"SCAN OK: 37 Bavli tractates ({global_meta['total_bavli_segments']} segments); "
        f"materialized={len(wanted) if wanted else 37}"
    )
    return 0


def cmd_build_pilot(args: argparse.Namespace) -> int:
    project_root = Path(args.project_root)
    spec_dir = project_root / "model_outputs" / "pass1_3_pilot"
    for spec_file in sorted(spec_dir.glob("*_spec.json")):
        spec = json.loads(spec_file.read_text(encoding="utf-8"))
        ckpt = compile_tractate_annotations_from_spec(project_root, spec["tractate_slug"], spec)
        print(f"BUILT {spec['tractate_slug']} ({ckpt['covered_daf_range']}): {ckpt['sugyot_count']} sugyot, {ckpt['statements_count']} statements")
    # Refresh tractate_progress.json statuses
    prog_path = project_root / "tractate_progress.json"
    if prog_path.exists():
        prog = json.loads(prog_path.read_text(encoding="utf-8"))
        for entry in prog["tractates"]:
            mp = project_root / "tractates" / entry["slug"] / "manifest.json"
            if mp.exists():
                m = json.loads(mp.read_text(encoding="utf-8"))
                entry["status"] = m["annotation_scope"]["tractate_completion_status"]
                entry["annotated_segments"] = m["annotation_scope"]["covered_segment_ids_count"]
        prog["completed_full_tractates"] = sum(
            1 for p in prog["tractates"] if p["status"] == "PROVISIONAL_TRACTATE_COMPLETE"
        )
        prog["pilot_slices_active"] = sum(
            1 for p in prog["tractates"] if p["status"] == "PILOT_SLICE_PROVISIONAL_COMPLETE"
        )
        prog_path.write_text(json.dumps(prog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    project_root = Path(args.project_root)
    scholars = load_jsonl(project_root / "scholars.jsonl")
    tractates_dir = project_root / "tractates"
    all_ok = True
    results = []
    for t_dir in sorted(tractates_dir.iterdir()):
        if not t_dir.is_dir() or not (t_dir / "manifest.json").exists():
            continue
        slug = t_dir.name
        local_cache = project_root / "local_source_cache" / slug / "segments.local_fulltext.jsonl"
        local_map = (
            {s["segment_id"]: s for s in load_jsonl(local_cache)} if local_cache.exists() else None
        )
        res = validate_tractate_bundle(project_root, slug, scholars, local_fulltext_by_id=local_map)
        results.append(res)
        if not res["valid"]:
            all_ok = False
            print(f"FAIL {slug}:")
            for e in res["errors"]:
                print(f"  - {e}")
        else:
            print(f"PASS {slug} ({res['mode']}): {json.dumps(res.get('metrics', {}), ensure_ascii=False)}")
    return 0 if all_ok else 1


def cmd_demo_queries(args: argparse.Namespace) -> int:
    project_root = Path(args.project_root)
    t_dir = project_root / "tractates" / "bava_metzia"
    sugyot = load_jsonl(t_dir / "sugyot.jsonl")
    top = [s for s in sugyot if s["level"] == "top"]
    recon_public = None
    if top:
        sample_id = "sugya:bavli:bava_metzia:21a:19__22b:10"
        recon = reconstruct_sugya(project_root, "bava_metzia", sample_id)
        print(
            f"1) Reconstructed sugya {sample_id}: {len(recon['ordered_segments'])} segments, "
            f"{len(recon['statements'])} statements, {len(recon['questions'])} questions"
        )
        # Redact full CC-BY-NC segment text to short preview for public Git artifact
        recon_public = {
            **recon,
            "ordered_segments": [
                {
                    "segment_id": s["segment_id"],
                    "ref": s["ref"],
                    "canonical_sha256": s["canonical_sha256"],
                    "preview_48_chars": (s["canonical_text"][:48] + "...")
                    if s.get("canonical_text")
                    else None,
                }
                for s in recon["ordered_segments"]
            ],
        }
    rava = find_scholar_statements(project_root, "scholar:amora:rava")
    rabbah = find_scholar_statements(project_root, "scholar:amora:rabbah")
    print(
        f"2) Scholar lookup {rava['scholar']['canonical_name_he']} (rava): "
        f"held={rava['held_statements_count']}, transmitted_only={rava['transmitted_only_count']}, "
        f"positions={rava['positions_count']} | "
        f"{rabbah['scholar']['canonical_name_he']} (rabbah): held={rabbah['held_statements_count']}"
    )
    qa = derive_eligible_qa_candidates(project_root)
    print(f"3) Derived ML-eligible Q-A candidates (with caveats): {len(qa)}")
    out_demo = project_root / "model_outputs" / "demo_query_outputs.json"
    out_demo.parent.mkdir(parents=True, exist_ok=True)
    out_demo.write_text(
        json.dumps(
            {
                "reconstructed_sugya_example": recon_public,
                "scholar_lookup_rava": rava,
                "scholar_lookup_rabbah": rabbah,
                "eligible_qa_candidates": qa,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Bavli Sugya Corpus v1 CLI")
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT_ROOT))
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_scan = sub.add_parser("scan")
    p_scan.add_argument("--corpus-root", default="F:/Sefaria-Export-master")
    p_scan.add_argument("--tractates", nargs="*")
    p_scan.set_defaults(func=cmd_scan)

    p_build = sub.add_parser("build-pilot")
    p_build.add_argument("--corpus-root", default="F:/Sefaria-Export-master")
    p_build.set_defaults(func=cmd_build_pilot)

    p_val = sub.add_parser("validate")
    p_val.add_argument("--corpus-root", default="F:/Sefaria-Export-master")
    p_val.set_defaults(func=cmd_validate)

    p_demo = sub.add_parser("demo-queries")
    p_demo.add_argument("--corpus-root", default="F:/Sefaria-Export-master")
    p_demo.set_defaults(func=cmd_demo_queries)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
