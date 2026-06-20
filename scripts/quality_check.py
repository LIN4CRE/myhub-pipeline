"""quality_check.py — called by CI to enforce code standards."""
import os
import re
import sys

# Patterns that must NOT appear in source code
_SECRET_RE  = re.compile(r"ghp_[A-Za-z0-9]{36,}", re.IGNORECASE)
_WILDCARD_RE = re.compile(r"^from\s+\S+\s+import\s+\*", re.MULTILINE)

issues = []
for root, _dirs, files in os.walk("src"):
    for fname in files:
        if not fname.endswith(".py"):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath) as fh:
            src = fh.read()
        if _SECRET_RE.search(src):
            issues.append(f"HIGH: possible hardcoded secret in {fpath}")
        if _WILDCARD_RE.search(src):
            issues.append(f"MEDIUM: wildcard import in {fpath}")

if issues:
    print("\n".join(issues))
    sys.exit(1)
print(f"quality_check: {sum(1 for _ in os.walk('src'))} dirs scanned — 0 issues")
