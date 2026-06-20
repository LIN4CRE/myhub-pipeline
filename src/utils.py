"""Utility helpers for the myhub pipeline."""
import re

COMMIT_RE = re.compile(
    r"^(?P<type>feat|fix|chore|docs|refactor|perf|test|ci|build|style)"
    r"(?:\((?P<scope>[^)]+)\))?(?P<breaking>!)?:\s*(?P<desc>.+)$",
    re.IGNORECASE,
)

def parse_commit(msg: str) -> dict:
    """Parse a Conventional Commit message into a structured dict."""
    m = COMMIT_RE.match(msg)
    if m:
        return {
            "type":     m.group("type").lower(),
            "scope":    m.group("scope") or "",
            "breaking": bool(m.group("breaking")),
            "desc":     m.group("desc").strip(),
        }
    return {"type": "other", "scope": "", "breaking": False, "desc": msg}

def bump_version(version: str, breaking: bool, has_feat: bool) -> str:
    """Bump a semver string given the nature of changes."""
    major, minor, patch = map(int, version.split("."))
    if breaking:
        return f"{major + 1}.0.0"
    if has_feat:
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"
