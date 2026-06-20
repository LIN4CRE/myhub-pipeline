"""Code quality check — run by CI to detect hardcoded secrets in src/."""
import os, re, sys

PATTERNS = [
    (re.compile(r"(password|secret|api_key|token)\s*=\s*['\"][^'\"]{8,}", re.I), "HIGH", "possible hardcoded credential"),
    (re.compile(r"^from\s+\S+\s+import\s+\*", re.M), "MEDIUM", "wildcard import"),
]

issues = []
for root, _, files in os.walk("src"):
    for f in files:
        if not f.endswith(".py"):
            continue
        path = os.path.join(root, f)
        src = open(path, encoding="utf-8").read()
        for pat, severity, msg in PATTERNS:
            if pat.search(src):
                issues.append(f"{severity}: {msg} in {path}")

if issues:
    print("\n".join(issues))
    sys.exit(1)

print(f"✅  Code quality OK — scanned {sum(1 for r,_,fs in os.walk('src') for f in fs if f.endswith('.py'))} files, 0 issues.")
