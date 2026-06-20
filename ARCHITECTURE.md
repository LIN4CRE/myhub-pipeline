# MyHub Pipeline — Architecture
> v1.2.0 · Auto-generated 2026-06-20 20:22 UTC

---

## Full Pipeline Diagram

```mermaid
flowchart TD
    %% ── INFRASTRUCTURE (blue) ─────────────────────────────────────────────
    GI[🔵 GitHub Integration\nauth + retry + token]
    GS[🔵 GitHub Secrets Setup]
    MF[🔵 Multi-Repo Fleet Config]

    %% ── REPO SETUP (teal) ──────────────────────────────────────────────────
    SP[🔵 Scaffold & Push\nrepo files via API]
    AF[🔵 GitHub Automation Files\ndependabot + labeler]
    CO[🔵 CODEOWNERS Setup\n12 path rules]
    RH[🔵 Repo Hardening\n14 config fixes]
    PR[🔵 PR Template Setup\n29-item checklist]

    %% ── CI / CD (green) ─────────────────────────────────────────────────
    QS[🟢 Code Quality & Security\nstatic analysis]
    BH[🟢 Benchmark Harness\nstage timing]
    CI[🟢 CI / Testing Automation\n9 tests via API]
    CV[🟢 Coverage Enforcement\n80 pct threshold]
    RA[🟢 Release Automation\nCC to semver]
    CQ[🟢 Changelog Quality\nCC coverage]
    PD[🟢 Pipeline Dashboard\n3 charts]

    %% ── SECURITY (red) ──────────────────────────────────────────────────
    SS[🔴 Security Scan\nbandit + CVE check]
    SA[🔴 Secrets & Token Audit\nPAT scope check]
    AF2[🔴 AI Auto-Fix\nPR with patch]

    %% ── INTELLIGENCE (yellow) ───────────────────────────────────────────
    PF[🟡 Predictive Failure\nRandomForest]
    FT[🟡 Flaky Test Detector\nalternation score]
    AD[🟡 Anomaly Detection\n2sigma bounds]
    AR[🟡 AI PR Reviewer\nrisk score + comment]

    %% ── OBSERVABILITY (purple) ──────────────────────────────────────────
    HM[🟣 Pipeline Health Monitor\nCI + protection audit]
    PS[🟣 Pipeline State Persistence\nhistory JSON]
    HC[🟣 Pipeline History Charts\n3 time-series]
    DM[🟣 DORA Metrics\nDF LT CFR MTTR]
    SV[🟣 Sprint & Velocity\nPR throughput]
    CC[🟣 Cost & Carbon\ndollar + CO2]
    NT[🟣 Notifications\nDiscord email]
    DR[🟣 Deployment Readiness\ncomposite A-F]

    %% ── FLEET (orange) ──────────────────────────────────────────────────
    FC[🟠 Fleet Health Check\nper-slice]
    FA[🟠 Fleet Health Aggregator\nhealth pct bar]

    %% ── PORTFOLIO (white) ────────────────────────────────────────────────
    RD[⬜ README & Architecture\nbadges + Mermaid]
    DV[⬜ Demo Video Script\n9-scene 60s narration]
    ST[⬜ Final Smoke Test\n20 checks]
    FR[⬜ Final Health Report\nmaster report + release]

    %% ── EDGES ────────────────────────────────────────────────────────────
    GI --> SP & AF & CO & MF & SA & AR & HM & GS
    GS --> CI
    SP --> QS
    AF --> RH
    CO --> PR
    RH --> DV
    QS --> BH & SS
    BH --> CI
    SS --> AF2
    CI --> CV & RA & DM & SV & CC & PS
    RA --> CQ & DR & PD & NT & RD
    HM --> PS & DR
    PS --> NT & FT & PF & HC
    HC --> AD
    DM --> RD
    PF --> RD
    MF --> FC --> FA
    RH --> ST
    AF2 --> ST
    NT --> ST
    SV --> ST
    CC --> ST
    FT --> ST
    CV --> ST
    DV --> ST
    ST --> FR
```

---

## Data Flow (Left → Right)

```
Auth & Config
  └─► Repo Setup (scaffold, automation, CODEOWNERS, protection)
        └─► Quality Gates (static analysis, security scan, benchmark)
              └─► CI / Testing (9 tests, coverage enforcement)
                    └─► Release Management (semver, CHANGELOG, GitHub Release)
                          └─► Observability (DORA, history, anomaly, predictions)
                                └─► Portfolio (README, demo script, smoke test, final report)
```

---

## What Runs When

| Block | Trigger |
|-------|---------|
| GitHub Integration | Manual / Run All |
| Scaffold & Push | Downstream of GitHub Integration |
| GitHub Automation Files | Downstream of GitHub Integration |
| CODEOWNERS Setup | Downstream of GitHub Integration |
| Repo Hardening & Config Fixes | Downstream of GitHub Automation Files |
| Pipeline Health Monitor | Downstream of GitHub Integration |
| Code Quality & Security | Downstream of Scaffold & Push |
| Security Scan | Downstream of Code Quality |
| AI Auto-Fix | Downstream of Security Scan (fires only on HIGH/MEDIUM findings) |
| Benchmark Harness | Downstream of Code Quality |
| CI / Testing Automation | Downstream of Benchmark Harness |
| Release Automation | Downstream of CI / Testing |
| DORA Metrics | Downstream of CI / Testing |
| Sprint & Velocity | Downstream of CI / Testing |
| Cost & Carbon | Downstream of CI / Testing |
| Coverage Enforcement | Downstream of CI / Testing |
| Pipeline State Persistence | Downstream of Health Monitor + CI |
| Pipeline History Charts | Downstream of State Persistence |
| Anomaly Detection | Downstream of History Charts (≥3 runs) |
| Flaky Test Detector | Downstream of State Persistence |
| Predictive Failure | Downstream of State Persistence |
| Notifications | On CI failure / health degraded / new release |
| Deployment Readiness Score | Downstream of Health Monitor + Release |
| README & Architecture | Downstream of DORA + Release + Predictive Failure |
| Demo Video Script | Downstream of README & Architecture |
| Final Smoke Test | Downstream of all terminal blocks |
| Final Health Report | Downstream of Smoke Test |
| Fleet Health Check | Per-repo slice (spread) |
| Fleet Health Aggregator | Aggregator for fleet slices |
| CI Workflow (GitHub Actions) | On push/PR to main — 4 parallel jobs |
| Webhook Relay | On any GitHub event to main |

---

## Colour Key

| Colour | Category |
|--------|----------|
| 🔵 Blue | Infrastructure & Auth |
| 🟢 Green | CI/CD & Quality Gates |
| 🔴 Red | Security |
| 🟡 Yellow | AI & Intelligence |
| 🟣 Purple | Observability |
| 🟠 Orange | Fleet Monitoring |
| ⬜ White | Portfolio & Output |

---

*Auto-generated by MyHub Pipeline · 2026-06-20 20:22 UTC*
