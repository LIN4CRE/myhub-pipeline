"""quality_check.py — CI code standards checker."""
import os
import re
import sys

_SECRET_RE   = re.compile(r"ghp_[A-Za-z0-9]{36,}", re.IGNORECASE)
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
            issues.append(f"HIGH: hardcoded secret in {fpath}")
        if _WILDCARD_RE.search(src):
            issues.append(f"MEDIUM: wildcard import in {fpath}")

if issues:
    print("\n".join(issues))
    sys.exit(1)
print("quality_check: 0 issues")
