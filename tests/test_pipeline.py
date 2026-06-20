"""Integration-style tests for src/pipeline.py."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import unittest
from src.pipeline import run_stage


class TestRunStage(unittest.TestCase):
    def test_returns_result_and_duration(self):
        result, duration = run_stage("test", lambda: 42)
        self.assertEqual(result, 42)
        self.assertGreaterEqual(duration, 0)

    def test_duration_is_float(self):
        _, duration = run_stage("noop", lambda: None)
        self.assertIsInstance(duration, float)

    def test_args_forwarded(self):
        result, _ = run_stage("add", lambda a, b: a + b, 3, 4)
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
