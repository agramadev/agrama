**TL;DR – read this once, refer to it daily.**
AGENT.md is the *single source-of-truth* for how humans (junior ↔ senior) and autonomous AI contributors collaborate on Agrama. It codifies the project’s values (safety, correctness, speed), the exact toolchain (Valkey 8.1, Faiss 1.11, Pyrefly type-checker, Ruff/Black, pytest-benchmark), and the end-to-end workflow from ticket ➜ PR ➜ main ➜ release. Follow every rule here and your code will ship; skip a rule and CI or the reviewer (human or agent) will bounce your patch.

---

## 1 · Core Philosophy

1. **Fail fast, fail locally** – run the full `make check` suite (lint + type + unit) before you push.
2. **Typed Python is mandatory** – uncompilable code is dead code; Pyrefly must pass green in CI and locally. ([Engineering at Meta][1])
3. **Benchmarks are tests** – a 10 % latency regression breaks the build just like a failing unit test.
4. **AI ≠ autopilot** – any code written by agents *must* be reviewed by a senior engineer before merge.

---

## 2 · Roles & Expectations

| Actor               | Responsibilities                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| **Junior Engineer** | Implement tickets, write unit tests, keep docs current, request review when CI is green.          |
| **Senior Engineer** | Architectural decisions, review & merge, mentor juniors, approve agent PRs.                       |
| **AI Agent**        | Generate scaffolds, refactors, or docs *on request*; must attach reasoning log in PR description. |

A **CODEOWNERS** file routes reviews to domain experts and AI reviewers automatically. ([GitHub Docs][2])

---

## 3 · Toolchain & Local Setup

```bash
git clone git@github.com:agramadev/agrama.git
make dev          # builds Valkey 8.1, Faiss 1.11, Ollama
make check        # ruff + pyrefly + unit tests
make tui          # launch Textual UI
```

* Install **Pyrefly** (`pip install pyrefly && pyrefly init`) to get instant type feedback in VS Code or PyCharm. ([pyrefly.org][3])
* Lint & format via **Ruff** (`ruff check . --fix`) and **Black** – both run in pre-commit hooks.

---

## 4 · Branching & Commit Rules

1. **Trunk-based**: work in short-lived branches named `<type>/<ticket>-<slug>` (e.g. `feat/123-vector-hybrid`).

2. **Conventional Commits** for every commit:

   ```
   feat(vector): add cosine metric to hybrid search
   ```

   ([conventionalcommits.org][4])

3. **One logical change per PR**; squash-merge with `--ff`.

4. **Semantic Versioning**: we tag releases `MAJOR.MINOR.PATCH` following semver 2.0.0. ([Semantic Versioning][5])

---

## 5 · Coding Standards

| Topic               | Rule                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| **Types**           | 100 % functions & public attrs have explicit type annotations; Pyrefly errors ⟹ no merge. ([GitHub][6]) |
| **Imports**         | Use absolute imports inside `agrama.*`; never use `from x import *`.                                    |
| **Function length** | ≤ 40 lines; split helpers if longer.                                                                    |
| **Docstrings**      | Google-style, include Args / Returns / Raises.                                                          |
| **Logging**         | Use `structlog`; no bare `print`.                                                                       |
| **Secrets**         | Load from env vars; never commit secrets. ([GitHub Docs][7])                                            |

---

## 6 · Test & Benchmark Matrix

| Layer     | Min Coverage            | Framework                          |
| --------- | ----------------------- | ---------------------------------- |
| Unit      | 90 % lines              | `pytest`, `hypothesis`             |
| Component | CRUD, search, summarise | `pytest-asyncio` w/ docker-compose |
| Bench     | p99 GET < 1 ms          | `pytest-benchmark` compare mode    |
| Load      | < 1 % errors @ 100 RPS  | `k6` smoke script                  |

`pytest-benchmark compare` aborts CI if mean latency regresses > 10 % versus `main`.

---

## 7 · Pull-Request Checklist

* [ ] Branch up-to-date with `main`.
* [ ] `make check` passes locally.
* [ ] Added/updated unit + component tests.
* [ ] Updated `CHANGELOG.md` and API docs if endpoints changed.
* [ ] Benchmarks unchanged or improved.
* [ ] PR description includes **context, design & trade-offs**; AI-generated code includes reasoning log.
* [ ] At least **one human senior** + optional AI reviewer approved.
* [ ] No new TODO/FIXME without linked issue.

---

## 8 · AI-Specific Guidelines

1. **Transparent provenance** – AI commits must add a trailer `Signed-off-by: <agent-name>`.
2. **Determinism** – use `PYTHONHASHSEED=0` and seed random libs for reproducible runs.
3. **Citation duty** – if an AI agent copied/adapted public code, cite the source in the PR.
4. **Self-review** – run `pyrefly check` & `ruff --fix`; attach the diff before/after to the PR.
5. **Limit scope** – AI patches ≤ 400 LOC; bigger changes need human pair-programming.

---

## 9 · Documentation

* **Docstrings** generate API docs via `sphinx-build`.
* Update `docs/architecture/**` diagrams (PlantUML) when data-flow or key-schema changes.
* Keep AGENT.md, CONTRIBUTING.md, and README cohesive—README is for users; AGENT.md is for builders. ([GitHub Docs][8])

---

## 10 · Security & Compliance

* Enforce Dependabot PRs weekly.
* GitHub Actions run with the least-privilege PAT; fork PRs use read-only tokens. ([GitHub Docs][7])
* Report vulnerabilities via `SECURITY.md`; patch in < 48 h for HIGH severity.

---

## 11 · Releases

1. Draft release notes from the **Conventional Commit** log (`cz changelog`).
2. Tag (`vX.Y.Z`); GitHub Action builds multi-arch images (`linux/amd64`, `linux/arm64`) and attaches SBOM.
3. After release, cut a new `docs/{version}` branch for any hot-fix docs.

---

## 12 · Pyrefly Integration Details

* **Pre-commit** – `pyrefly lint --output facebook` fails on any type error.
* **IDE** – install Pyrefly VS Code extension for inline diagnostics.
* **Performance** – Pyrefly checks \~1.8 M LOC/s on 10-core laptop, 5-6× faster than Pyright. ([pyrefly.org][3])
* **Config** – see `pyrefly.yaml` in repo root for strict mode toggles.

---

Happy coding, and remember: **green CI, typed code, reproducible speed**—or it doesn’t merge.
