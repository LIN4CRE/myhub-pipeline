import os
import re
import sys

# Flag only bare quoted-string assignments (not env-var reads).
# Matches:  token = 'abc...'   but NOT:  TOKEN = os.environ.get('...')
HARDCODE_RE = re.compile(
    r"(?:password|secret|api_key|token)\s*=\s*['\"][^'\"]{8,}['\"]",
    re.IGNORECASE,
)
WILDCARD_RE = re.compile(r"^from\s+\S+\s+import\s+\*", re.M)

issues = []
for root, _, files in os.walk("src"):
    for fname in files:
        if not fname.endswith(".py"):
            continue
        fpath = os.path.join(root, fname)
        code = open(fpath, encoding="utf-8").read()
        if HARDCODE_RE.search(code):
            issues.append("HIGH: hardcoded credential in " + fpath)
        if WILDCARD_RE.search(code):
            issues.append("MEDIUM: wildcard import in " + fpath)

if issues:
    for issue in issues:
        print(issue)
    sys.exit(1)

count = sum(1 for r, _, fs in os.walk("src") for fn in fs if fn.endswith(".py"))
print("Code quality OK - scanned " + str(count) + " files, 0 issues.")
