"""Code quality check — CI step to detect hardcoded secrets in src/."""
import os, re, sys

# Match:  token = 'abc...'   or   secret = "abc..."
# Skip :  TOKEN = os.environ.get(...)  (RHS starts with a letter/call)
HARDCODE_RE = re.compile(
    r"(?:password|secret|api_key|token)\s*=\s*['\"][^'\"]{8,}['\"]",
    re.IGNORECASE,
)
WILDCARD_RE = re.compile(r'^from\s+\S+\s+import\s+\*', re.M)

issues = []
for root, _, files in os.walk('src'):
    for f in files:
        if not f.endswith('.py'):
            continue
        path = os.path.join(root, f)
        src = open(path, encoding='utf-8').read()
        if HARDCODE_RE.search(src):
            issues.append(f'HIGH: hardcoded credential in {path}')
        if WILDCARD_RE.search(src):
            issues.append(f'MEDIUM: wildcard import in {path}')

if issues:
    print('\n'.join(issues))
    sys.exit(1)

_n = sum(1 for r,_,fs in os.walk('src') for fn in fs if fn.endswith('.py'))
print(f'Code quality OK - scanned {_n} files, 0 issues.')
