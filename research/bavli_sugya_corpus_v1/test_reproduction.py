"""Rebuild pilot + accepted continuation blocks in an isolated temp dir and compare byte-for-byte."""
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
import pipeline as p


def main():
    start = time.perf_counter()
    inputs = [
        "pipeline.py",
        "make_schema.py",
        "make_schema_v1_1.py",
        "compile_annotations.py",
        "annotation_initial.py",
        "annotation_completion.py",
        "revisions.json",
        "continuation.py",
        "export_reader.py",
        "continue_corpus.py",
        "validate.py",
    ]
    expected = (
        [
            "source_manifest.json",
            "schema_v1.json",
            "schema_v1_1.json",
            "annotation_manifest.json",
            "revisions_ledger.jsonl",
            "block_ledger.json",
            "progress_manifest.json",
            "qa_report.json",
            "exports/berakhot_sugyot_cumulative.jsonl",
            "exports/berakhot_index.json",
            "exports/berakhot_sugya_reader.html",
        ]
        + [f"data/{t}.jsonl" for t in p.TABLES]
        + ["context/segments.jsonl", "context/windows.jsonl"]
    )
    with tempfile.TemporaryDirectory(prefix="bavli_cumulative_reproduction_") as tmp:
        temp = Path(tmp)
        for f in inputs:
            shutil.copyfile(p.HERE / f, temp / f)
        shutil.copytree(p.HERE / "blocks", temp / "blocks")
        for cmd in [
            ["pipeline.py", "build"],
            ["make_schema.py"],
            ["compile_annotations.py"],
            ["continue_corpus.py", "apply", "--block-dir", "blocks/berakhot_5b_6a"],
            ["continue_corpus.py", "export"],
        ]:
            result = subprocess.run(
                [sys.executable, "-X", "utf8", *cmd],
                cwd=temp,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            assert result.returncode == 0, result.stderr
        for f in expected:
            assert (temp / f).read_bytes() == (p.HERE / f).read_bytes(), f + " differs"
    result = dict(
        passed=True,
        byte_identical_outputs=len(expected),
        outputs=expected,
        wall_seconds=time.perf_counter() - start,
        semantic_regeneration=False,
        note="Replays preserved pilot + immutable continuation block artifacts byte-for-byte.",
    )
    p.write(p.HERE / "reproduction_report.json", result)
    print(result)


if __name__ == "__main__":
    main()
