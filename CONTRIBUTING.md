# Contributing to MyHub Pipeline

Thank you for your interest in contributing! 🙌

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Make your changes following the code standards below
4. Open a pull request against `main`

## Code Standards

- **Style**: PEP8, max line length 120 (enforced by `.flake8`)
- **Commits**: [Conventional Commits](https://www.conventionalcommits.org/) format required
  - `feat:` new feature · `fix:` bug fix · `chore:` maintenance · `ci:` CI changes
- **Tests**: add or update tests for every change (`tests/`)
- **Security**: no hardcoded credentials — use environment variables only
- **Docs**: update relevant `.md` files if your change affects behaviour

## Pull Request Checklist

All items in `.github/PULL_REQUEST_TEMPLATE.md` must be completed before requesting review.

## Branch Protection

`main` is fully protected — all PRs require:
- 1 approving review (CODEOWNERS auto-assigns reviewers)
- All 4 CI checks passing (pytest · flake8 · bandit · build)
- Branch up to date with `main`

## Local Development

```bash
git clone https://github.com/LIN4CRE/myhub-pipeline
cd myhub-pipeline
pip install -r requirements.txt -r requirements-dev.txt
pytest tests/ -v
flake8 src/ tests/ scripts/
bandit -r src/ -ll
```

## Reporting Issues

Use the [bug report template](https://github.com/LIN4CRE/myhub-pipeline/issues/new?template=bug_report.md).
