import re
import unittest
from pathlib import Path

from ops.catalog import CHANNELS, EXCLUDED, summary
from ops.qc import inspect_script
from ops.server import ROOT, schedule_blockers
from ops.videos import VIDEOS

ROOT_SCRIPTS = Path(__file__).resolve().parents[1] / "ops" / "content" / "scripts"


class DeskTests(unittest.TestCase):
    def test_one_hundred_distinct_channels(self):
        self.assertEqual(len(CHANNELS), 100)
        self.assertEqual(len({c["id"] for c in CHANNELS}), 100)
        self.assertEqual(len({c["handle"] for c in CHANNELS}), 100)
        self.assertEqual(len({c["name"] for c in CHANNELS}), 100)
        self.assertEqual({c["market"] for c in CHANNELS}, {"US", "UK"})
        self.assertTrue(all(not c["youtube_created"] for c in CHANNELS))
        self.assertTrue(all(not c["ai_persona_allowed"] for c in CHANNELS))

    def test_scores_are_ranked_and_explained(self):
        scores = [c["score"] for c in CHANNELS]
        self.assertEqual(scores, sorted(scores, reverse=True))
        self.assertTrue(all(0 < c["score"] <= 100 for c in CHANNELS))
        parts = CHANNELS[0]["score_parts"]
        self.assertEqual(sum(parts.values()), CHANNELS[0]["score"])

    def test_launch_batch_is_four_scripted_packages(self):
        launch = [c for c in CHANNELS if c["launch"]]
        self.assertEqual(len(launch), 4)
        self.assertEqual({v["channel_id"] for v in VIDEOS}, {c["id"] for c in launch})
        for video in VIDEOS:
            path = ROOT / video["script"]
            text = path.read_text(encoding="utf-8")
            report = inspect_script(text, title=video["title"], master_path=None, thumbnail_path=None)
            self.assertGreaterEqual(report["word_count"], 700)
            self.assertIn("narration_quality", report["failed"])
            self.assertIn("playback", report["failed"])
            self.assertFalse(report["passed"])
            self.assertEqual(len(video["titles"]), 5)

    def test_schedule_is_refused(self):
        blockers = schedule_blockers("uk-salary-ledger")
        self.assertTrue(blockers)
        self.assertTrue(any("YouTube" in line or "Google" in line for line in blockers))
        self.assertTrue(any("Quality control" in line for line in blockers))

    def test_official_figures_are_in_the_scripts(self):
        salary = (ROOT_SCRIPTS / "uk-salary-ledger.md").read_text(encoding="utf-8")
        self.assertIn("£20,000", salary)
        self.assertIn("6 April 2027", salary)
        self.assertIn("£12,000", salary)
        coverage = (ROOT_SCRIPTS / "us-coverage-map.md").read_text(encoding="utf-8")
        self.assertIn("$8,000", coverage)
        self.assertIn("$2,950", coverage)
        self.assertIn("not medical advice", coverage.lower())

    def test_summary_does_not_invent_published_work(self):
        snap = summary()
        self.assertEqual(snap["youtube_channels_created"], 0)
        self.assertEqual(snap["videos_published"], 0)
        self.assertEqual(snap["weekly_goal"], 400)
        self.assertGreaterEqual(len(EXCLUDED), 8)
        self.assertIn("not a count of finished videos", snap["weekly_goal_note"])

    def test_scripts_do_not_impersonate_reference_creators(self):
        banned = re.compile(r"\b(Damien|James Shack|Humphrey Yang|Tina Huang)\b")
        for path in ROOT_SCRIPTS.glob("*.md"):
            self.assertIsNone(banned.search(path.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
