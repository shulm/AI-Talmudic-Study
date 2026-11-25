"""Synthetic-only contract tests; no real tractate is annotated or reviewed."""
import hashlib
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import make_review_plan as planner
from make_review_plan import make_plan, plan_digest


class ReviewPlanTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name) / "source.json"

    def write_source(self, pages, title="Synthetic", version="Wikisource Talmud Bavli", language="he"):
        payload = json.dumps({"title": title, "versionTitle": version,
                              "text": pages, "language": language}, ensure_ascii=False).encode("utf-8")
        self.source.write_bytes(payload)
        return hashlib.sha256(payload).hexdigest()

    def build(self, pages, seed=7, block_size=10):
        sha = self.write_source(pages)
        return make_plan(self.source, "Synthetic", sha, seed, block_size)

    def test_source_hash_mismatch_refused(self):
        self.write_source([["text"]])
        with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
            make_plan(self.source, "Synthetic", "0" * 64, 7)

    def test_version_title_language_and_duplicate_keys_refused(self):
        sha = self.write_source([["text"]], version="Another edition")
        with self.assertRaisesRegex(ValueError, "versionTitle"):
            make_plan(self.source, "Synthetic", sha, 7)
        sha = self.write_source([["text"]], title="Another tractate")
        with self.assertRaisesRegex(ValueError, "title"):
            make_plan(self.source, "Synthetic", sha, 7)
        sha = self.write_source([["text"]], language="en")
        with self.assertRaisesRegex(ValueError, "language"):
            make_plan(self.source, "Synthetic", sha, 7)
        self.write_source([["text"]])
        raw = self.source.read_bytes().replace(b'"text":', b'"title":"Synthetic","text":')
        self.source.write_bytes(raw)
        with self.assertRaisesRegex(ValueError, "Duplicate JSON key"):
            make_plan(self.source, "Synthetic", hashlib.sha256(raw).hexdigest(), 7)

    def test_initial_gaps_internal_empty_page_and_blank_positions(self):
        pages = [[] for _ in range(65)]
        pages[61] = ["אבּ ג", "", "second"]
        pages[63] = ["\t\n", "third"]
        pages[64] = ["fourth"]
        plan = self.build(pages, block_size=2)
        inventory = plan["source_inventory"]
        self.assertEqual(inventory["nonempty_segments"], 5)
        self.assertEqual(inventory["segment_positions"], 6)
        self.assertEqual(len(inventory["empty_segment_positions"]), 1)
        self.assertEqual(len(inventory["whitespace_only_nonempty_positions"]), 1)
        self.assertEqual(plan["source_language"], "he")
        self.assertIn(62, inventory["empty_page_indices"])
        spans = [s for b in plan["review_blocks"] for s in b["spans"]]
        self.assertEqual([s["ref"] for s in spans],
                         ["Synthetic 31b:1", "Synthetic 31b:3",
                          "Synthetic 32b:1", "Synthetic 32b:2", "Synthetic 33a:1"])
        for span in spans:
            raw = pages[span["page_index"]][span["segment_index"]]
            start, end = span["offsets_codepoints"]
            self.assertEqual((start, end), (0, len(raw)))
            self.assertEqual(span["span_sha256_utf8"],
                             hashlib.sha256(raw[start:end].encode("utf-8")).hexdigest())
        self.assertNotIn("אבּ ג", json.dumps(plan, ensure_ascii=False))

    def test_small_tractate_samples_all_and_deduplicates_endpoints(self):
        plan = self.build([["one", "two"]])
        self.assertEqual(plan["sampling"]["sampled_blocks"], 1)
        self.assertEqual(plan["coverage"]["unique_review_nonempty_segments"], 2)
        self.assertEqual(len(plan["review_blocks"]), 1)
        self.assertEqual(plan["review_blocks"][0]["roles"],
                         ["probability_sample", "opening_check", "closing_check"])
        self.assertEqual(plan["endpoint_checks"]["unique_added_block_ids"], [])

    def test_determinism_sampling_fraction_and_endpoint_union(self):
        pages = [[f"segment-{i}" for i in range(405)]]
        first = self.build(pages, seed=19, block_size=1)
        second = make_plan(self.source, "Synthetic", first["source_sha256"], 19, 1)
        self.assertEqual(first, second)
        self.assertEqual(first["plan_sha256"], plan_digest(first))
        self.assertEqual(first["sampling"]["sampled_blocks"], 41)
        sampled = set(first["sampling"]["probability_sample_block_ids"])
        endpoints = {first["endpoint_checks"]["opening_block_id"],
                     first["endpoint_checks"]["closing_block_id"]}
        selected = {b["block_id"] for b in first["review_blocks"]}
        self.assertEqual(selected, sampled | endpoints)
        self.assertEqual(first["coverage"]["unique_review_blocks"], len(selected))
        for block in first["review_blocks"]:
            self.assertEqual(block["inclusion_probability"], 41 / 405)
        third = make_plan(self.source, "Synthetic", first["source_sha256"], 20, 1)
        self.assertNotEqual(first["sampling"]["probability_sample_block_ids"],
                            third["sampling"]["probability_sample_block_ids"])
        second["tractate"] = "changed"
        self.assertNotEqual(first["plan_sha256"], plan_digest(second))

    def test_invalid_source_shapes_and_empty_source_refused(self):
        for pages in (["not-an-array"], [[None]], [[[]]], []):
            sha = self.write_source(pages)
            with self.subTest(pages=pages), self.assertRaises(ValueError):
                make_plan(self.source, "Synthetic", sha, 7)
        sha = self.write_source([["text"]])
        for seed, size in ((True, 10), (7, True), ("7", 10), (7, 0), (7, 1.5)):
            with self.subTest(seed=seed, size=size), self.assertRaises(ValueError):
                make_plan(self.source, "Synthetic", sha, seed, size)

    def cli(self, output):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return planner.main(["--source", str(self.source), "--tractate", "Synthetic",
                                 "--expected-sha256", hashlib.sha256(self.source.read_bytes()).hexdigest(),
                                 "--seed", "7", "--output", str(output)])

    def test_cli_source_cannot_be_overwritten(self):
        self.write_source([["text"]])
        before = self.source.read_bytes()
        with self.assertRaises(SystemExit):
            self.cli(self.source)
        self.assertEqual(self.source.read_bytes(), before)

    def test_cli_identical_output_is_idempotent_and_different_output_refused(self):
        self.write_source([["text"]])
        output = self.source.parent / "plan.json"
        self.cli(output)
        before, inode = output.read_bytes(), output.stat().st_ino
        self.cli(output)
        self.assertEqual((output.read_bytes(), output.stat().st_ino), (before, inode))
        output.write_bytes(b"another frozen plan")
        with self.assertRaises(SystemExit):
            self.cli(output)
        self.assertEqual(output.read_bytes(), b"another frozen plan")
        self.assertEqual(len(list(self.source.parent.iterdir())), 2)

    def test_cli_interruption_before_publication_leaves_no_final(self):
        self.write_source([["text"]])
        output = self.source.parent / "plan.json"
        with patch("make_review_plan.os.link", side_effect=KeyboardInterrupt), self.assertRaises(KeyboardInterrupt):
            self.cli(output)
        self.assertFalse(output.exists())
        self.assertEqual(list(self.source.parent.iterdir()), [self.source])

    def test_cli_competing_final_path_is_not_overwritten(self):
        self.write_source([["text"]])
        output = self.source.parent / "plan.json"

        def competing_publish(temporary, final):
            self.assertTrue(Path(temporary).read_bytes())
            Path(final).write_bytes(b"competing publisher")
            raise FileExistsError("simulated publication race")

        with patch("make_review_plan.os.link", side_effect=competing_publish), self.assertRaises(SystemExit):
            self.cli(output)
        self.assertEqual(output.read_bytes(), b"competing publisher")
        self.assertEqual(len(list(self.source.parent.iterdir())), 2)


if __name__ == "__main__":
    unittest.main()
