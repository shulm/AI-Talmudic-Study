"""CLI entrypoint for configurable block-by-block Bavli sugya corpus continuation."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pipeline as p
import make_schema_v1_1
import continuation as c
import export_reader as er


def update_delivery_manifest(base_dir: Path) -> dict:
    old = p.read(base_dir / "delivery_manifest.json") if (base_dir / "delivery_manifest.json").exists() else {}
    files: dict[str, str] = {}
    for fp in sorted(base_dir.rglob("*")):
        if not fp.is_file():
            continue
        rel = fp.relative_to(base_dir).as_posix()
        if (
            rel == "delivery_manifest.json"
            or rel.startswith("local_data/")
            or "__pycache__" in rel
            or rel.endswith(".pyc")
        ):
            continue
        files[rel] = p.sha(fp.read_bytes())
    manifest = {
        "schema_version": "1.1.0",
        "previous_pilot_delivery_commit": "ef29310b50575ac2441ce59d0c68d58424f4b823",
        "note": old.get(
            "note",
            "Byte hashes of public deliverables; mechanical integrity only, not semantic certification.",
        ),
        "files": files,
    }
    p.write(base_dir / "delivery_manifest.json", manifest)
    return manifest


def main() -> None:
    ap = argparse.ArgumentParser(description="Safe block-by-block continuation CLI (v1.1.0)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_prep = sub.add_parser("prepare")
    p_prep.add_argument("--source-root", type=Path, default=p.DEFAULT)
    p_prep.add_argument("--block-id", required=True)
    p_prep.add_argument("--tractate", required=True)
    p_prep.add_argument("--core-start", required=True)
    p_prep.add_argument("--core-end", required=True)
    p_prep.add_argument("--context-before", type=int, default=1)
    p_prep.add_argument("--context-after", type=int, default=1)
    p_prep.add_argument("--out", type=Path, required=True)

    p_apply = sub.add_parser("apply")
    p_apply.add_argument("--source-root", type=Path, default=p.DEFAULT)
    p_apply.add_argument("--block-dir", type=Path, required=True)

    p_val = sub.add_parser("validate")
    p_val.add_argument("--source-root", type=Path, default=p.DEFAULT)
    p_val.add_argument("--public-only", action="store_true")

    sub.add_parser("export")
    sub.add_parser("update-manifest")

    args = ap.parse_args()
    base = p.HERE

    if args.cmd == "prepare":
        pkt = c.prepare_block_input(
            base,
            args.source_root,
            args.block_id,
            args.tractate,
            args.core_start,
            args.core_end,
            args.context_before,
            args.context_after,
        )
        p.write(args.out, pkt)
        print(json.dumps(pkt["counts"], ensure_ascii=False))
    elif args.cmd == "apply":
        make_schema_v1_1.make_v1_1()
        pkt = p.read(args.block_dir / "input_packet.json")
        prop = p.read(args.block_dir / "proposal.json")
        ind_path = args.block_dir / "independent_review_initial.json"
        ind = p.read(ind_path) if ind_path.exists() else None
        res = c.apply_continuation_block(base, args.source_root, pkt, prop, ind)
        print(json.dumps(res, ensure_ascii=False))
    elif args.cmd == "validate":
        res = c.validate_v1_1(
            base,
            source_root=None if args.public_only else args.source_root,
            check_source=not args.public_only,
        )
        print(json.dumps(res, ensure_ascii=False))
    elif args.cmd == "export":
        res = er.build_berakhot_exports(base)
        print(json.dumps(res, ensure_ascii=False))
    elif args.cmd == "update-manifest":
        m = update_delivery_manifest(base)
        print(json.dumps({"public_files_hashed": len(m["files"])}))


if __name__ == "__main__":
    main()
