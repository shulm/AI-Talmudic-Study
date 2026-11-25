"""Focused queue-integrity tests; no corpus or external service is required."""
import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import build_jobs as builder


def fixtures():
    titles = ["Berakhot", "Example", "Rosh Hashanah", "Taanit", "Bava Metzia"]
    counts = [2749, 12, 1025, 895, 3660]
    sources, histories = [], []
    for ordinal, (title, count) in enumerate(zip(titles, counts), 1):
        pilot_count, source_hash = builder.PILOTS.get(title, (0, builder.digest(title.encode())))
        sources.append({"ordinal": ordinal, "title": title, "he_title": "דוגמה",
                        "source_path": f"json/{title}/Hebrew/{builder.EDITION}.json",
                        "source_sha256": source_hash, "schema_path": f"schemas/{title}.json",
                        "schema_sha256": builder.digest((title + " schema").encode()),
                        "source_segments": count, "nonempty_segments": count, "page_slots": 100,
                        "first_nonempty_ref": title + " 2a:1",
                        "metadata": {"title": title, "versionTitle": builder.EDITION,
                                     "language": "he", "license": "CC-BY-SA"}})
        histories.append({"ordinal": ordinal, "tractate": title, "source_segments": count,
                          "pilot_segments": pilot_count, "primary_sugyot": 0, "statements": 0,
                          "questions": 0, "positions": 0, "uncertain_records": 0,
                          "completed_masechet": False,
                          "status": "pilot_partial_semantics" if pilot_count else "inventory_only"})
    return ({"edition": builder.EDITION, "source_toc_sha256": "a" * 64, "tractates": sources},
            {"completed_masechtot": 0, "tractates": histories})


def encoded(value):
    return json.dumps(value, ensure_ascii=False).encode()


class QueueIntegrityTests(unittest.TestCase):
    def test_determinism_order_provenance_and_no_false_execution(self):
        source, progress = fixtures()
        a = builder.build_queue(encoded(source), encoded(progress))
        b = builder.build_queue(encoded(source), encoded(progress))
        self.assertEqual(builder.encode_queue(a), builder.encode_queue(b))
        self.assertEqual([j["tractate"] for j in a["jobs"]],
                         ["Berakhot", "Bava Metzia", "Rosh Hashanah", "Taanit", "Example"])
        self.assertEqual(a["source_manifest_sha256"], builder.digest(encoded(source)))
        self.assertEqual(a["historical_pilot_source_segments"], 215)
        self.assertEqual(a["runtime_initialization_template"]["processed_source_segments"], 0)
        self.assertEqual(a["input_provenance"]["status"], "unverified_metadata_inputs")
        self.assertIsNone(a["base_commit"])
        for job in a["jobs"]:
            initial = job["runtime_initialization_template"]
            self.assertEqual(initial["status"], "queued_unclaimed")
            self.assertIsNone(initial["owner_agent"])
            self.assertFalse(initial["completed_tractate"])
            self.assertFalse(initial["source_bytes_verified"])
            self.assertEqual(initial["model_calls_made"], 0)
            self.assertIsNone(job["base_commit"])

    def test_inherited_tail_and_interior_pilot_are_distinct(self):
        source, progress = fixtures()
        jobs = {j["tractate"]: j for j in builder.build_queue(encoded(source), encoded(progress))["jobs"]}
        berakhot = jobs["Berakhot"]["continuation_plan"]
        self.assertEqual(berakhot["inherited_open_sugya_id"], "sug_9a1c712c3a26fe45003b")
        self.assertEqual(berakhot["inherited_open_sugya_start_ref"], "Berakhot 5a:24")
        self.assertEqual(berakhot["resume_core_start_ref"], "Berakhot 5b:1")
        metzia = jobs["Bava Metzia"]["continuation_plan"]
        self.assertEqual(metzia["resume_core_start_ref"], "Bava Metzia 2a:1")
        self.assertTrue(metzia["must_process_before_and_after_pilot"])

    def test_refuses_duplicate_identities_and_mixed_editions(self):
        mutations = [
            lambda s, p: s["tractates"][1].update(title="Berakhot"),
            lambda s, p: s["tractates"][1].update(source_path=s["tractates"][0]["source_path"]),
            lambda s, p: s["tractates"][1].update(source_sha256=s["tractates"][0]["source_sha256"]),
            lambda s, p: p["tractates"].append(copy.deepcopy(p["tractates"][0])),
            lambda s, p: s["tractates"][1]["metadata"].update(versionTitle="Other Edition"),
            lambda s, p: s["tractates"][1].update(source_path="../outside.json"),
            lambda s, p: s["tractates"][1].update(source_sha256="not-a-hash"),
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                source, progress = fixtures()
                mutation(source, progress)
                with self.assertRaises(builder.InputError):
                    builder.build_queue(encoded(source), encoded(progress))

    def test_refuses_bad_denominators_counts_and_false_completion(self):
        mutations = [
            lambda s, p: s["tractates"][1].update(source_segments=True),
            lambda s, p: s["tractates"][1].update(source_segments=-1),
            lambda s, p: p["tractates"][1].update(source_segments=13),
            lambda s, p: p["tractates"][1].update(pilot_segments=13),
            lambda s, p: p["tractates"][1].update(completed_masechet=True),
            lambda s, p: s.update(total_source_segments=1),
            lambda s, p: p["tractates"].pop(),
            lambda s, p: s["tractates"][0].update(source_sha256="b" * 64),
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                source, progress = fixtures()
                mutation(source, progress)
                with self.assertRaises(builder.InputError):
                    builder.build_queue(encoded(source), encoded(progress))

    def test_invalid_inputs_leave_existing_output_untouched(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, progress = fixtures()
            source["tractates"][0]["source_sha256"] = "wrong"
            (root / "source.json").write_bytes(encoded(source))
            (root / "progress.json").write_bytes(encoded(progress))
            (root / "jobs.json").write_bytes(b"previous queue")
            with contextlib.redirect_stderr(io.StringIO()) as stderr:
                status = builder.main(["--manifest", str(root / "source.json"),
                                       "--progress", str(root / "progress.json"),
                                       "--output", str(root / "jobs.json")])
            self.assertEqual(status, 2)
            self.assertIn("REFUSED", stderr.getvalue())
            self.assertEqual((root / "jobs.json").read_bytes(), b"previous queue")

    def test_cli_refuses_self_consistent_wrong_baseline(self):
        source, progress = fixtures()
        self.assertEqual(builder.build_queue(encoded(source), encoded(progress))["tractate_count"], 5)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "source.json").write_bytes(encoded(source))
            (root / "progress.json").write_bytes(encoded(progress))
            with contextlib.redirect_stderr(io.StringIO()) as stderr:
                status = builder.main(["--manifest", str(root / "source.json"),
                                       "--progress", str(root / "progress.json"),
                                       "--output", str(root / "jobs.json")])
            self.assertEqual(status, 2)
            self.assertIn("pinned historical baseline", stderr.getvalue())
            self.assertFalse((root / "jobs.json").exists())

    def test_cli_verified_replay_and_differing_output_protection(self):
        source, progress = fixtures()
        source_bytes, progress_bytes = encoded(source), encoded(progress)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "source.json").write_bytes(source_bytes)
            (root / "progress.json").write_bytes(progress_bytes)
            output = root / "jobs.json"
            arguments = ["--manifest", str(root / "source.json"),
                         "--progress", str(root / "progress.json"), "--output", str(output)]
            with mock.patch.object(builder, "PINNED_MANIFEST_SHA256", builder.digest(source_bytes)), \
                 mock.patch.object(builder, "PINNED_PROGRESS_SHA256", builder.digest(progress_bytes)), \
                 contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(builder.main(arguments), 0)
                content, stamp = output.read_bytes(), output.stat().st_mtime_ns
                queue = json.loads(content)
                self.assertEqual(queue["input_provenance"]["status"], "verified_pinned_metadata_baseline")
                self.assertEqual(queue["base_commit"], builder.BASE_COMMIT)
                self.assertTrue(all(j["base_commit"] == builder.BASE_COMMIT for j in queue["jobs"]))
                with mock.patch.object(builder.os, "link", side_effect=AssertionError("replay attempted publication")):
                    self.assertEqual(builder.main(arguments), 0)
                self.assertEqual((output.read_bytes(), output.stat().st_mtime_ns), (content, stamp))
                output.write_bytes(b"other frozen specification")
                with contextlib.redirect_stderr(io.StringIO()) as stderr:
                    self.assertEqual(builder.main(arguments), 2)
                self.assertIn("existing job specification differs", stderr.getvalue())
                self.assertEqual(output.read_bytes(), b"other frozen specification")

    def test_failed_flush_leaves_no_final_path_and_race_preserves_winner(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "jobs.json"
            with mock.patch.object(builder.os, "fsync", side_effect=OSError("injected flush failure")):
                with self.assertRaises(OSError):
                    builder.publish_frozen(output, b"candidate")
            self.assertFalse(output.exists())
            self.assertEqual(list(root.iterdir()), [])

            def competitor_wins(source, target):
                Path(target).write_bytes(b"winning specification")
                raise FileExistsError("injected publication race")

            with mock.patch.object(builder.os, "link", side_effect=competitor_wins):
                with self.assertRaises(builder.InputError):
                    builder.publish_frozen(output, b"losing specification")
            self.assertEqual(output.read_bytes(), b"winning specification")
            self.assertEqual(list(root.iterdir()), [output])


if __name__ == "__main__":
    unittest.main()
