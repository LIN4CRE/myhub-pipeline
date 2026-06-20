# Deployment Guide — MyHub Pipeline
> v1.2.0 · 2026-06-20 20:22 UTC

---

## 1. Prerequisites

- Python 3.11+
- GitHub account with a Personal Access Token (PAT)
- Zerve account (for canvas-based orchestration)

---

## 2. GitHub Token Setup

### Minimum required scopes
```
repo          (full repository access)
workflow      (trigger GitHub Actions)
```

### Create a fine-grained PAT
1. Go to https://github.com/settings/personal-access-tokens/new
2. Set expiry (90 days recommended)
3. Grant: Contents (read/write), Actions (read/write), Pull Requests (read/write), Secrets (read/write)

### Set in Zerve
```
Zerve → Settings → Environment Variables → Add PIPELINE_TOKEN=<your_token>
```

### Set for local use
```bash
export PIPELINE_TOKEN=your_github_pat_here
```

---

## 3. Install Dependencies

### Runtime
```bash
pip install -r requirements.txt
# requests pandas matplotlib packaging
```

### Development & CI
```bash
pip install -r requirements-dev.txt
# pytest pytest-cov bandit flake8 pip-tools
```

---

## 4. Run the Pipeline

### Option A — Zerve canvas (recommended)
1. Open the **Perfect Homepage Builder** canvas in Zerve
2. Click **Run All** — blocks execute in dependency order automatically
3. All 48 blocks complete in ~2 minutes

### Option B — Trigger via GitHub CLI
```bash
gh workflow run ci.yml --repo LIN4CRE/myhub-pipeline
```

### Option C — Python entrypoint
```python
from src.pipeline import run_stage
from src.utils import parse_commit, bump_version
result, duration = run_stage("test", lambda: "ok")
```

---

## 5. Launch the Dashboard

The MyHub Workstation is deployed as a Zerve Dash app.

```bash
# Local development
pip install dash plotly pandas requests
python app/main.py
# Opens at http://localhost:8050
```

**Tabs available:**
- ⚡ Live Dashboard — CI badge, health cards, benchmark/quality/test charts
- 📈 History — health score, CI duration, pass rate trend lines
- 🤖 AI & DORA — DORA KPIs, predictive failure, sprint velocity, cost/carbon
- 🔒 Security — token audit, readiness gauge, security scan, fleet health
- 🔔 Webhooks — live event feed from repo
- 🎬 Demo — video script + screenshot manifest

---

## 6. Configure Multi-Repo Monitoring

Edit the `REPOS` list in the **Multi-Repo Fleet Config** block:

```python
REPOS = [
    {"slug": "LIN4CRE/myhub-pipeline", "name": "MyHub Pipeline"},
    {"slug": "LIN4CRE/another-repo",   "name": "Another Repo"},
    {"slug": "myorg/backend-api",      "name": "Backend API"},
]
```

Re-run **Multi-Repo Fleet Config** → **Fleet Health Check** (auto-fans) → **Fleet Health Aggregator**.

---

## 7. Enable Notifications

### Discord
```bash
export DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR/WEBHOOK
```

### Email (SMTP)
```bash
export SMTP_HOST=smtp.gmail.com
export SMTP_USER=you@gmail.com
export SMTP_PASS=your_app_password
export NOTIFY_EMAIL_TO=you@yourcompany.com
```

Notifications fire on: CI failure · health degraded ≥10% · new release published.

---

## 8. Troubleshooting

### ❌ `401 Unauthorized` from GitHub API
**Fix:** Token expired or wrong scopes. Generate a new token with `repo` + `workflow` scopes and update `PIPELINE_TOKEN`.

### ❌ Branch protection blocks file push
**Fix:** The pipeline temporarily relaxes protection for each push and restores immediately after. If a block fails mid-push, run the affected block again — it will restore protection on the next run.

### ❌ CI runs failing on `Security (bandit)` job
**Fix:** Add `bandit>=1.7.0` to `requirements-dev.txt` and push. The pipeline currently uses a regex fallback when bandit is not installed.

### ❌ `pytest-cov` not installed — coverage shows 0%
**Fix:** Add `pytest-cov>=4.1.0` to `requirements-dev.txt`. The Coverage Enforcement block will switch from estimation to exact measurement.

### ❌ Anomaly Detection shows "Need ≥3 runs"
**Fix:** Normal behaviour on a fresh repo. Run the full pipeline 2 more times to build history. The block activates automatically at 3 snapshots.

---

## 9. File Structure

```
myhub-pipeline/
├── .github/
│   ├── CODEOWNERS
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── dependabot.yml
│   ├── labeler.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── workflows/
│       ├── ci.yml          ← 4 parallel jobs: pytest flake8 bandit build
│       ├── auto-label.yml
│       └── webhook_relay.yml
├── docs/
│   ├── BLOCK_REFERENCE.md
│   ├── DEMO_SCRIPT.md
│   └── DEPLOYMENT_GUIDE.md
├── scripts/
│   └── quality_check.py
├── src/
│   ├── __init__.py
│   ├── pipeline.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_pipeline.py
│   └── test_utils.py
├── .flake8
├── conftest.py
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── ARCHITECTURE.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── README.md
└── VERSION
```

---

*Auto-generated by MyHub Pipeline · 2026-06-20 20:22 UTC*
