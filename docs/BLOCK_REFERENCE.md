# Block Reference — MyHub Pipeline
> Auto-generated 2026-06-20 20:22 UTC · v1.2.0

Every block in the pipeline, its upstream dependencies, key exports, and what consumes them.

---

## Infrastructure & Auth

### GitHub Integration
| | |
|---|---|
| **Inputs** | `PIPELINE_TOKEN` env var |
| **Exports** | `GITHUB_TOKEN`, `REPO_SLUG`, `DEFAULT_BR`, `REPO_URL`, `REPO_OWNER`, `REPO_NAME`, `gh_get/post/put/patch/delete`, `push_file`, `config_result` |
| **Downstream** | All blocks |
| **Trigger** | Manual / Run All |

### GitHub Secrets Setup
| | |
|---|---|
| **Inputs** | `GITHUB_TOKEN` |
| **Exports** | `secrets_setup_result` |
| **Downstream** | Update CI Workflow |

### Multi-Repo Fleet Config
| | |
|---|---|
| **Inputs** | `GITHUB_TOKEN` |
| **Exports** | `REPOS` list |
| **Downstream** | Fleet Health Check (spread) |

---

## Repository Setup

### Scaffold & Push
| | |
|---|---|
| **Inputs** | `GITHUB_TOKEN`, `REPO_SLUG`, `DEFAULT_BR` |
| **Exports** | `scaffold_result` |
| **Downstream** | Code Quality & Security |

### GitHub Automation Files
| | |
|---|---|
| **Inputs** | `GITHUB_TOKEN`, `REPO_SLUG`, `DEFAULT_BR` |
| **Exports** | `automation_files_result` |
| **Downstream** | Repo Hardening & Config Fixes |
| **What it pushes** | dependabot.yml, issue templates, auto-labeler, labeler.yml |

### CODEOWNERS Setup
| | |
|---|---|
| **Inputs** | `GITHUB_TOKEN`, `REPO_SLUG`, `DEFAULT_BR` |
| **Exports** | `codeowners_result` |
| **Downstream** | CODEOWNERS Audit, PR Template Setup |

### Repo Hardening & Config Fixes
| | |
|---|---|
| **Inputs** | `automation_files_result`, `GITHUB_TOKEN` |
| **Exports** | `hardening_result` |
| **Downstream** | Demo Video Script |
| **What it pushes** | ci.yml, webhook_relay.yml, .flake8, pyproject.toml, conftest.py, requirements-dev.txt, CONTRIBUTING.md, CODE_OF_CONDUCT.md |

---

## Quality & Security

### Code Quality & Security
| | |
|---|---|
| **Inputs** | `scaffold_result` |
| **Exports** | `quality_report` (DataFrame), `quality_stage_time` |
| **Downstream** | Benchmark Harness, Security Scan |

### Security Scan
| | |
|---|---|
| **Inputs** | `quality_report` |
| **Exports** | `security_scan_report` (DataFrame), `security_scan_chart` |
| **Downstream** | AI Auto-Fix |

### AI Auto-Fix
| | |
|---|---|
| **Inputs** | `security_scan_report`, `GITHUB_TOKEN` |
| **Exports** | `autofix_result` |
| **Trigger** | Runs on HIGH/MEDIUM findings; opens PRs automatically |

### Coverage Enforcement
| | |
|---|---|
| **Inputs** | `test_results` |
| **Exports** | `coverage_result` |
| **Note** | Requires `pytest-cov` for exact measurement |

---

## CI & Testing

### Benchmark Harness
| | |
|---|---|
| **Inputs** | `quality_report`, `quality_stage_time` |
| **Exports** | `benchmark_df` |
| **Downstream** | CI / Testing Automation |

### CI / Testing Automation
| | |
|---|---|
| **Inputs** | `benchmark_df` |
| **Exports** | `test_results` (DataFrame: file, passed, failed, returncode, status) |
| **Downstream** | Coverage Enforcement, Release Automation, DORA Metrics, Sprint & Velocity, Cost & Carbon, Pipeline State Persistence |

### Pipeline Health Monitor
| | |
|---|---|
| **Inputs** | `GITHUB_TOKEN`, `REPO_SLUG` |
| **Exports** | `health_report` (dict: overall_health_pct, checks, …) |
| **Downstream** | Pipeline State Persistence, Deployment Readiness Score |

---

## Release & Changelog

### Release Automation
| | |
|---|---|
| **Inputs** | `test_results` |
| **Exports** | `release_notes`, `new_version`, `commits_df`, `changelog_md`, `CURRENT_VER` |
| **Downstream** | Changelog Quality, Deployment Readiness, Pipeline Dashboard, Notifications, README & Architecture |

### Changelog Quality
| | |
|---|---|
| **Inputs** | `release_notes` |
| **Exports** | `changelog_quality_report`, `enriched_changelog_md` |

---

## Observability & AI

### Pipeline State Persistence
| | |
|---|---|
| **Inputs** | `health_report`, `test_results` |
| **Exports** | `pipeline_history` (list of snapshots) |
| **Downstream** | Notifications, Flaky Test Detector, Predictive Failure, Pipeline History Charts |
| **Side effect** | Appends to `pipeline_history.json` in repo |

### Pipeline History Charts
| | |
|---|---|
| **Inputs** | `pipeline_history` |
| **Exports** | `health_history_chart`, `duration_history_chart`, `passrate_history_chart` |
| **Downstream** | Anomaly Detection |

### Anomaly Detection
| | |
|---|---|
| **Inputs** | `pipeline_history` |
| **Exports** | `anomaly_report`, `anomaly_chart` |
| **Activates** | ≥3 pipeline runs |

### DORA Metrics
| | |
|---|---|
| **Inputs** | `test_results` |
| **Exports** | `dora_metrics`, `dora_chart` |
| **Downstream** | README & Architecture |

### Sprint & Velocity Analytics
| | |
|---|---|
| **Inputs** | `test_results` |
| **Exports** | `sprint_df`, `sprint_chart` |

### Cost & Carbon Estimator
| | |
|---|---|
| **Inputs** | `test_results` |
| **Exports** | `cost_report`, `cost_chart` |

### Predictive Failure
| | |
|---|---|
| **Inputs** | `pipeline_history` |
| **Exports** | `prediction_result`, `prediction_chart` |
| **Downstream** | README & Architecture |

### Flaky Test Detector
| | |
|---|---|
| **Inputs** | `pipeline_history` |
| **Exports** | `flaky_report` |
| **Side effect** | Auto-opens GitHub issue if flakiness_score > 0.3 |

### AI PR Reviewer
| | |
|---|---|
| **Inputs** | `GITHUB_TOKEN` |
| **Exports** | `pr_review_results` |
| **Side effect** | Posts review comments to open PRs |

### Notifications
| | |
|---|---|
| **Inputs** | `pipeline_history`, `release_notes` |
| **Exports** | `notification_result` |
| **Channels** | Discord (`DISCORD_WEBHOOK_URL`), Email (`SMTP_HOST/USER/PASS/NOTIFY_EMAIL_TO`) |

---

## Portfolio & Output

### Deployment Readiness Score
| | |
|---|---|
| **Inputs** | `health_report`, `release_notes`, `quality_report`, `test_results` |
| **Exports** | `deployment_readiness`, `deployment_readiness_chart` |

### README & Architecture
| | |
|---|---|
| **Inputs** | `dora_metrics`, `release_notes`, `health_report`, `prediction_result` |
| **Exports** | `architecture_md` |
| **Side effect** | Pushes README.md + ARCHITECTURE.md to repo |

### Demo Video Script & Screenshots
| | |
|---|---|
| **Inputs** | `architecture_md`, `hardening_result` |
| **Exports** | `demo_script_md`, `demo_screenshots` |
| **Side effect** | Pushes docs/DEMO_SCRIPT.md to repo |

### Final Smoke Test
| | |
|---|---|
| **Inputs** | All terminal block outputs |
| **Exports** | `smoke_test_results` (DataFrame), `smoke_test_passed` (bool) |

### Final Health Report *(this block's downstream)*
| | |
|---|---|
| **Inputs** | `smoke_test_results`, `smoke_test_passed` + all block outputs |
| **Exports** | `final_report`, `release_url` |
| **Side effect** | Pushes final_summary.md, creates GitHub Release v1.2.0 |

---

## Fleet

### Multi-Repo Fleet Config → Fleet Health Check → Fleet Health Aggregator
| | |
|---|---|
| **Fleet pattern** | `spread()` per repo → slicer checks CI/issues/protection → AGGREGATOR collects |
| **Exports** | `fleet_health_df`, `fleet_health_chart` |

---

*Generated by MyHub Pipeline · 2026-06-20 20:22 UTC*
