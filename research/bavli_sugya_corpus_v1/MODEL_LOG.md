# Model, Prompt, and Cost Accounting Log — Bavli Sugya Corpus v1

## 1. Configured Model Policy

| Role | Default Model | Fallback / Bulk Comparison Option | Notes |
|---|---|---|---|
| Source scanning, ref mapping, SHA-256 hashing, offset maps, boundary reconciliation, schema & invariant validation | Deterministic Python 3.12 (`stdlib` + `jsonschema`) | None (never delegated to LLM) | Zero stochasticity; byte-reproducible |
| Primary semantic annotation (Pass 1 sugya windows, Pass 2 speech-acts & attributions, Pass 3 questions/positions/relations) | **Gemini 4 Carbon** (`gemini-4-carbon`, medium reasoning) | Optional bounded comparison with **Gemini 4 Hydrogen** (`gemini-4-hydrogen`) once external API budget is authorized | Structured JSON outputs validated in Python |
| Independent second reading (`ai_independent_double`) on pilot calibration set | **Gemini 4 Carbon** (isolated context without Pass 1–3 annotations) | Human Talmudic domain expert (`human_reviewed`) for future gold certification | AI double review is never labeled `scholarly_confirmed` |

## 2. Paid External API Budget Guard

Per assignment governance:
- **Authorized external paid API budget in current run:** `$0.00 USD` (owner has not yet authorized external Gemini API billing).
- `src/bavli_corpus/annotation_runner.py` enforces `--authorized-budget-usd 0.0` by default and **refuses** to initiate external paid network API calls unless `--mode gemini_api` is explicitly paired with a positive `--authorized-budget-usd` and valid credentials.
- All pilot calibration annotations (`Berakhot 2a–5a` and `Bava Metzia 21a–22b`) and the independent blind second-pass reading (`>= 20` sugyot) were executed directly within the authenticated Antigravity workspace session on **Gemini 4 Carbon** (plus an isolated `research` subagent on the inherited Gemini 4 Carbon model for the blind second reading), incurring **$0.00** in separate external API charges while persisting exact structured JSON window payloads under `model_outputs/` for deterministic replay and audit.

## 3. Recorded Runs Ledger

| Run ID | Timestamp (UTC+02:00) | Stage | Model | Reasoning Setting | Target Scope | External Paid API Calls | External Cost (USD) | Artifact Path |
|---|---|---|---|---|---|---:|---:|---|
| `run-20261124-toc-v1` | `2026-11-24T23:05:00+02:00` | Pass 0: Global 37-tractate TOC & pilot segment manifests | Deterministic Python 3.12 | N/A | All 37 Bavli tractates (`81,793` segments scanned; Berakhot & Bava Metzia manifests frozen) | 0 | `$0.00` | `tractate_progress.json`, `source_version_manifest.json` |
| `run-20261124-pass123-pilot` | `2026-11-24T23:15:00+02:00` | Pass 1–3 windowed annotation + Python reconciliation & span alignment | Gemini 4 Carbon (workspace agent) + Python validator | Medium | `Berakhot 2a:1–5a:24` (`151` segs) & `Bava Metzia 21a:1–22b:16` (`64` segs) | 0 | `$0.00` | `model_outputs/pass1_3_pilot/`, `tractates/{berakhot,bava_metzia}/` |
| `run-20261124-double-review` | `2026-11-24T23:25:00+02:00` | Blind independent AI second reading (`ai_independent_double`) | Gemini 4 Carbon (isolated `research` subagent, source-only prompt) | Medium | Stratified/complete pilot sugyot (`>= 20` sugyot across Berakhot 2a–5a & Bava Metzia 21a–22b) | 0 | `$0.00` | `model_outputs/independent_second_pass/`, `QA_REPORT.md` |
