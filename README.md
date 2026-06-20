# MyHub Dev Pipeline 🚀

[![Record Demo](https://img.shields.io/badge/▶%20Demo%20Video-coming%20soon-555555?style=for-the-badge&logo=youtube)](https://github.com/LIN4CRE/myhub-pipeline/blob/main/docs/DEMO_SCRIPT.md)
[![CI](https://github.com/LIN4CRE/myhub-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/LIN4CRE/myhub-pipeline/actions/workflows/ci.yml)
[![Version](https://img.shields.io/badge/version-v1.2.0-6c63ff?style=flat)](https://github.com/LIN4CRE/myhub-pipeline/releases)
[![Health](https://img.shields.io/badge/health-100%25-17b26a?style=flat)](https://github.com/LIN4CRE/myhub-pipeline)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat)](LICENSE)
[![Deploy Freq](https://img.shields.io/badge/Deploy__Freq-0.23%2Fwk-ffd400?style=flat&colorA=1D1D20)](https://github.com/LIN4CRE/myhub-pipeline/blob/main/ARCHITECTURE.md)
[![Failure Risk](https://img.shields.io/badge/Failure__Risk-0%25-8DE5A1?style=flat&colorA=1D1D20)](https://github.com/LIN4CRE/myhub-pipeline/blob/main/pipeline_history.json)
[![YouTube](https://img.shields.io/badge/YouTube-@Minibooks1-ff0000?style=flat&logo=youtube)](https://www.youtube.com/@Minibooks1)

> **Fully automated SDLC pipeline** — CI/CD, code quality, security scanning, AI auto-fix,
> DORA metrics, anomaly detection, predictive failure, and a live portfolio dashboard.
> Built as a portfolio project by [David Linacre](https://github.com/LIN4CRE).

---

## 🎬 Demo Video

> **Recording in progress** — follow the [9-scene script](docs/DEMO_SCRIPT.md) with Loom or OBS.
> Once recorded, paste the URL here and re-run this block to embed automatically.

| Step | Link |
|------|------|
| 📋 Demo Script (9 scenes, 60s) | [docs/DEMO_SCRIPT.md](docs/DEMO_SCRIPT.md) |
| 🎥 YouTube Channel | [@Minibooks1](https://www.youtube.com/@Minibooks1) |
| 📐 Architecture Diagram | [ARCHITECTURE.md](ARCHITECTURE.md) |
| 📦 Golden Release v1.2.0 | [Releases](https://github.com/LIN4CRE/myhub-pipeline/releases) |

---

## What is this?

A production-grade DevOps pipeline built entirely in Python, controlled from a Zerve canvas.
It manages a GitHub repository end-to-end: from code quality checks and CI runs to release
automation, AI-powered PR review, and a live public portfolio dashboard.

**49 blocks · 35+ automated checks · 0 manual steps after initial token setup.**

---

## DORA Metrics  *(last 30 days)*

| Metric | Value | Band |
|--------|-------|------|
| 🚀 Deployment Frequency | `0.23/wk` | 🔴 Low |
| ⏱ Lead Time for Changes | `0.0h` | ⚡ Elite |
| 🔴 Change Failure Rate | `12.0%` | 🟡 Medium |
| 🔧 MTTR | `0.0h` | ⚡ Elite |

---

## AI Features

| Feature | What it does |
|---------|-------------|
| **AI PR Reviewer** | Reviews open PRs, assigns risk score (LOW/MEDIUM/HIGH), posts comments |
| **AI Auto-Fix** | Opens a PR with a security patch when scan finds HIGH/MEDIUM issues |
| **Predictive Failure** | RandomForest model predicts CI failure probability. Current: **0% (✅ VERY LOW RISK)** |
| **Anomaly Detection** | 2σ statistical bounds on CI duration + pass rate — flags regressions |
| **Flaky Test Detector** | Alternation-score analysis — auto-opens GitHub issues for flaky tests |

---

## Security & Governance

- Branch protection on `main`: PR required · 1 approval · CODEOWNERS · stale review dismissal
- All 4 CI checks must pass before merge (pytest · flake8 · bandit · build)
- No hardcoded credentials — all auth via `PIPELINE_TOKEN` Actions secret
- Weekly Dependabot updates · PAT scope audit on every run
- Immutable audit log in `pipeline_history.json`

---

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full Mermaid block dependency diagram.

```
GitHub Integration ──► Code Quality ──► Benchmark ──► CI Tests ──► Release Automation
        │                   │                                  │            │
        ▼                   ▼                                  ▼            ▼
  Fleet Monitor       Security Scan                    State Persistence  DORA Metrics
        │                   │                                  │            │
        ▼                   ▼                                  ▼            ▼
  Fleet Aggregator    AI Auto-Fix                      History Charts   Sprint Analytics
                                                              │
                                                              ▼
                                           Anomaly Detection · Flaky Tests · Predictive Failure
```

---

## Quick Start

```bash
export PIPELINE_TOKEN=your_github_pat_here
# Then: Zerve canvas → Run All   (or trigger via GitHub Actions UI)
gh workflow run ci.yml --repo LIN4CRE/myhub-pipeline
```

---

## Links

| Resource | URL |
|----------|-----|
| 📦 Repo | https://github.com/LIN4CRE/myhub-pipeline |
| 🎥 YouTube | https://www.youtube.com/@Minibooks1 |
| 📋 Docs | https://github.com/LIN4CRE/myhub-pipeline/tree/main/docs |
| 🏗 Architecture | https://github.com/LIN4CRE/myhub-pipeline/blob/main/ARCHITECTURE.md |
| 📝 CHANGELOG | https://github.com/LIN4CRE/myhub-pipeline/blob/main/CHANGELOG.md |
| 🚀 Releases | https://github.com/LIN4CRE/myhub-pipeline/releases |

---

*README auto-generated by MyHub pipeline · 2026-06-20 21:58 UTC*
