"""Tests for src/utils.py."""
import unittest
from src.utils import parse_commit, bump_version


class TestParseCommit(unittest.TestCase):
    def test_feat(self):
        r = parse_commit("feat(auth): add OAuth2 login")
        self.assertEqual(r["type"], "feat")
        self.assertFalse(r["breaking"])

    def test_breaking(self):
        r = parse_commit("feat(ci)!: switch to GitHub Actions")
        self.assertTrue(r["breaking"])

    def test_unrecognised(self):
        r = parse_commit("random commit message")
        self.assertEqual(r["type"], "other")


class TestBumpVersion(unittest.TestCase):
    def test_patch(self):
        self.assertEqual(bump_version("1.2.3", False, False), "1.2.4")

    def test_minor(self):
        self.assertEqual(bump_version("1.2.3", False, True), "1.3.0")

    def test_major(self):
        self.assertEqual(bump_version("1.2.3", True, False), "2.0.0")


if __name__ == "__main__":
    unittest.main()
