<!--
  Thanks for contributing to myhub-pipeline! 🎉
  Please fill in every section below before requesting a review.
  Incomplete checklists may delay your PR being approved.
-->

## 📋 Description
<!-- A clear and concise summary of *what* this PR does and *why*. -->

## 🔗 Related Issues / Tickets
<!-- Link any issues this PR closes or references. -->
- Closes #
- Refs #

## 🏷️ Type of Change
<!-- Put an `x` in the boxes that apply. -->
- [ ] 🐛 Bug fix (non-breaking change that fixes an issue)
- [ ] ✨ New feature (non-breaking change that adds functionality)
- [ ] 💥 Breaking change (fix or feature that causes existing functionality to change)
- [ ] 🔒 Security fix / credential rotation
- [ ] ♻️  Refactor / code cleanup (no functional change)
- [ ] 📝 Documentation update
- [ ] 🔧 CI / tooling / configuration change
- [ ] ⬆️  Dependency upgrade

---

## ✅ Pre-Merge Checklist

### Code Quality
- [ ] My code follows the project style guidelines (`flake8` passes locally)
- [ ] I have performed a self-review of my own code
- [ ] I have commented complex or non-obvious logic
- [ ] No hardcoded secrets, tokens, or credentials are present
- [ ] No wildcard imports (`from x import *`) introduced
- [ ] No functions exceed 50 lines without justification

### Tests
- [ ] I have added tests that prove my fix / feature works
- [ ] All existing unit tests pass locally (`pytest tests/`)
- [ ] Test coverage has not decreased for changed modules
- [ ] Edge cases and error paths are covered

### Security
- [ ] `bandit` security scan passes with no medium/high issues
- [ ] No new dependencies added without security review
- [ ] Secrets / tokens are managed via GitHub Actions secrets only
- [ ] CODEOWNERS has been updated if new paths were added

### CI / Checks
- [ ] All 4 CI jobs pass: **Tests (pytest)**, **Lint (flake8)**, **Security (bandit)**, **Build validation**
- [ ] This branch is up to date with `main` (rebase / merge if needed)
- [ ] No unresolved review comments remain

### Documentation
- [ ] `README.md` updated if behaviour / setup changed
- [ ] `CHANGELOG` / release notes updated for significant changes
- [ ] Inline docstrings updated for changed functions/classes
- [ ] `VERSION` bumped if this introduces a release

---

## 🖼️ Screenshots / Evidence
<!-- For UI, chart, or output changes attach before/after screenshots or CI run links. -->
<!-- Delete this section if not applicable. -->

| Before | After |
|--------|-------|
| —      | —     |

## 🧪 How to Test
<!-- Step-by-step instructions for the reviewer to verify this PR works. -->
1.
2.
3.

## ⚠️ Known Limitations / Follow-ups
<!-- Anything deferred, not covered, or that needs a follow-up PR. -->
- None

---
<!-- Auto-reviewer assignment is handled by .github/CODEOWNERS -->
