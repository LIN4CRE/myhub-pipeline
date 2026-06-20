# Contributing to MyHub Pipeline

## Getting Started
1. Fork the repo
2. `git checkout -b feat/your-feature`
3. Follow code standards below
4. Open a PR against `main`

## Code Standards
- PEP8, max line 120 (.flake8 enforced)
- Conventional Commits required
- No hardcoded credentials — env vars only

## Local Setup
```bash
pip install -r requirements.txt -r requirements-dev.txt
pytest tests/ -v
flake8 src/ tests/ scripts/
bandit -r src/ -ll
```
