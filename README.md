<div align="center">

# ResearchPilot <sub>V5.4.0</sub>

**AI-native research infrastructure for academics and PhD students.**

Ingest papers · Extract insights via AI · Search 5 academic databases · Cluster knowledge graphs · Run input-driven web research · Write with RAG-powered chat

[![Version](https://img.shields.io/badge/version-V5.4.0-6c63ff?style=for-the-badge)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-green?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/pavelblank/ResearchPilot?style=for-the-badge&logo=github)](https://github.com/pavelblank/ResearchPilot/stargazers)
[![Self-hosted](https://img.shields.io/badge/self--hosted-local--first-orange?style=for-the-badge)](#-quick-start)
[![AI-Native](https://img.shields.io/badge/built--with-OpenCode%20AI-ff4d6d?style=for-the-badge)](#-built-with-ai)

[Features](#-features) · [Setup Guide](SETUP.md) · [Quick Start](#-quick-start) · [Screenshots](#-screenshots) · [Documentation](SYSTEM-DOCUMENTATION.md) · [Security](#-security)

</div>

---

> **All self-hosted. All local-first. Your research, your machine, your keys.**

ResearchPilot is a complete research operating system that connects to multiple AI backends (Ollama, Gemini, Claude, OpenRouter, NVIDIA, and more) and gives you a full workflow for academic research — from paper discovery and ingestion to AI-powered extraction, multi-dimensional knowledge graphs, and RAG-augmented writing.

---

## 📸 Screenshots

<div align="center">
  <table>
    <tr>
      <td><img src="5.3.0-%20Home%20page%20dashbard%20.png" alt="Home Dashboard" width="320"></td>
      <td><img src="5.3.0-%20Web%20Research%20page.png" alt="Web Research" width="320"></td>
      <td><img src="5.3.0-%20Knowledge%20Graph%20page.png" alt="Knowledge Graph" width="320"></td>
    </tr>
    <tr>
      <td align="center"><b>🏠 Home Dashboard</b><br><sub>System Pulse · Quotes · Stats</sub></td>
      <td align="center"><b>🔍 Web Research</b><br><sub>5 academic sources</sub></td>
      <td align="center"><b>🕸 Knowledge Graph</b><br><sub>7 dimensions · AND/OR filters</sub></td>
    </tr>
  </table>
</div>

---

## ✨ Why ResearchPilot?

- 🧠 **Multi-AI failover router** — 11+ engines, zero downtime. If one engine fails, the next takes over automatically.
- 📚 **Universal file ingestion** — PDF · DOCX · PPTX · HTML · TXT · MD · CSV · JSON, all auto-converted to Markdown.
- 🎓 **12-Point Elite Extraction** — every paper analysed via APA, DOI, Quartile, Method, Framework, Limitations, and more.
- 🌍 **5-source academic search** — OpenAlex · Crossref · Semantic Scholar · PubMed · Google Scholar (with predatory-journal filtering).
- 🔬 **Input-driven web-research engine** (V5.4.0) — 8-step NLP extraction → parallel multi-source search → trigram/bigram scoring → journal-quality tier filter (Q1–Q4 + peer-review). Purely user-input-driven, no project config required. New `00-SYSTEM-CORE/SEARCH-SYSTEM/` folder.
- 🕸 **Multi-dimensional knowledge graph** — filter by Author, Year, Journal, Quartile, Method, Framework, or Keyword (AND/OR logic).
- 🧩 **Graph cluster mode** (V5.4.0) — group papers by Author / Year / Journal / Quartile / Method / Framework without filtering, with a central Category Hub node and direct file-to-file cluster edges. Mix cluster + filter dims in one view.
- 🔒 **Encrypted at rest** — API keys stored using Fernet (AES-128-CBC + HMAC-SHA256); the encryption key never leaves your machine.
- 🛡️ **Rate-limited + audit-logged** — 240 req/min/IP, every sensitive action (settings save, project delete, file delete, tool call) recorded in `audit.log`.
- 🔐 **Prompt-injection & SSRF hardened** — Pydantic v2 `ToolExecReq` schema + orchestration interceptor block unknown tool names, path-traversal, oversized args, and private-IP engine URLs. Validates every LLM tool call before dispatch.
- 💬 **RAG-powered chat** — no vector DB, no embeddings, no GPU. Keyword-scored context retrieval across your entire library, with 45 s result cache.
- 📤 **Literature-review export** — `GET /api/export/lit-review?project=X` bundles all 12-point extractions into a single markdown file.
- 🩺 **Built-in health check** — `GET /api/health` for uptime monitors, plus global exception handler that never leaks stack traces.
- 📊 **System Pulse dashboard** — live animated graph with quote-of-the-day, stats, and quick notes.
- ⌨️ **Keyboard shortcuts** — `1-9` switch tabs, `/` focus chat, `Esc` close modal.
- 🪶 **Obsidian-compatible** — the entire folder is a valid Obsidian vault; open it and you get an instant knowledge graph.
- 🧠 **Smart keyword system** — manual deletes are remembered forever; re-adding a deleted keyword restores it until you delete it again. Auto-scan skips your discard list.
- 🧪 **Smoke-tested** — 30 automated tests cover encryption, RAG cache, audit log, rate limiter, health, exception handler, keyword rules, Graphify filter, SSRF guard, tool-allowlist interceptor, path-traversal, Pydantic schema, security wiring, filename standardisation (Protocol 7), and **graph cluster mode (V5.4.0)**.
- 🤖 **100% AI-built** — every line generated through [OpenCode](https://opencode.ai), a free local AI coding agent.

---

## 📋 Prerequisites

| Requirement | Minimum |
|---|---|
| **Python** | 3.10+ (tested on 3.11) |
| **OS** | Windows 10+ · Linux · macOS |
| **Ollama** (optional) | [ollama.com](https://ollama.com) — `ollama pull llama3` |
| **Disk space** | ~500 MB for dependencies + your papers |
| **RAM** | 512 MB min · 2 GB recommended |

---

## 🚀 Quick Start

**For detailed walkthroughs, troubleshooting, and auto-start setup, see the full [Setup Guide](SETUP.md).**

### Install (one time)

| Step | What to do |
|---|---|
| **1. Get Python 3.10+** | Download from [python.org](https://www.python.org/downloads/). ⚠️ **Windows:** tick "Add Python to PATH" in the installer. |
| **2. Get ResearchPilot** | Download ZIP from the green `<> Code` button above, OR run `git clone https://github.com/pavelblank/ResearchPilot.git` |
| **3. Install dependencies** | Open a terminal in the `web-app` folder and run `pip install -r requirements.txt` |

### Run (every time)

| Platform | How to start |
|---|---|
| **🪟 Windows** | Double-click `web-app/START-SERVER.bat` — auto-installs deps on first run, browser opens automatically |
| **🍎 macOS** | Double-click `web-app/START-SERVER.sh` (or run `./START-SERVER.sh` in Terminal) |
| **🐧 Linux** | Run `./START-SERVER.sh` from the `web-app` folder |
| **⌨️ Any platform** | `cd web-app && python main.py` |

Then open **<http://127.0.0.1:8000>** in your browser.

> 💡 The system auto-creates `99-SYSTEM-BACKEND/`, `INCOMING/`, `01-PROJECTS/`, and the encryption key on first run. **No data is on the server** — everything stays on your machine.

### Configure AI

Add at least one AI key in the UI after first launch (**Settings → AI Engines**), or use local Ollama. Your keys are **encrypted at rest** automatically.

| Engine | Free? | Get it from |
|---|---|---|
| **Ollama** (local) | ✅ | [ollama.com](https://ollama.com) |
| **Gemini Flash** | ✅ tier | [aistudio.google.com](https://aistudio.google.com/app/apikey) |
| **OpenRouter** (free models) | ✅ tier | [openrouter.ai](https://openrouter.ai) |
| **NVIDIA NIM** (free tier) | ✅ | [build.nvidia.com](https://build.nvidia.com) |
| **Claude** | 💳 | [console.anthropic.com](https://console.anthropic.com) |

---

## 🔥 Features in Detail

<details>
<summary><b>📥 Universal File Ingestion</b></summary>

| Format | Parser | Auto .md |
|---|---|:-:|
| PDF | Docling (preferred) → PyMuPDF | ✅ |
| DOCX / DOC | python-docx | ✅ |
| PPTX / PPT | python-pptx | ✅ |
| HTML / HTM | html2text | ✅ |
| TXT · CSV · JSON · YAML | direct read | ✅ |

</details>

<details>
<summary><b>🔀 Multi-AI Engine Router</b></summary>

Supports unlimited engines with priority-based failover, per-engine enable/disable, dynamic reordering, and tool-calling. Falls back transparently when one engine rate-limits or errors.

**Supported types:** OpenAI-compatible (OpenRouter · Jan · LocalAI · LM Studio) · Ollama (local) · Gemini · Claude API · Claude CLI · Custom Plugin

</details>

<details>
<summary><b>🎓 12-Point Elite Extraction Protocol</b></summary>

Every paper is analysed through these 12 dimensions:

1. **APA Reference** — full academic citation
2. **DOI** — Digital Object Identifier
3. **Journal Name** — full name and ranking
4. **Quartile Ranking** — Q1/Q2 verified via Scopus/SJR
5. **Indexing** — Scopus, Web of Science confirmation
6. **Research Method** — Quantitative · Qualitative · Mixed · Review
7. **Theoretical Framework** — primary theories used
8. **Exact Relevance** — specific utility for your project
9. **Section Support** — which chapter or section it informs
10. **Key Contribution** — the "One Big Insight"
11. **Limitations** — critical gaps identified by authors
12. **Classification** — Behaviour · Governance · Technical · Essential

</details>

<details>
<summary><b>🕸 Knowledge Graph</b></summary>

Visualise research across **7 dimensions**: Author · Year · Journal · Quartile · Method · Framework · Keyword.

Multi-layer filtering with AND/OR logic. **Graphify** is a built-in code-level AST engine that annotates every source file, class, and function with semantic metadata.

</details>

<details>
<summary><b>🌍 Academic Web Search</b></summary>

Search 5 sources in parallel, with automatic deduplication and predatory-journal filtering:

- **OpenAlex** — 250M+ works
- **Crossref** — scholarly publishing metadata
- **Semantic Scholar** — AI-powered discovery
- **PubMed** — biomedical literature
- **Google Scholar** — broad academic search

For each result: preview, open, download PDF (OA), or save metadata + 12-point AI analysis.

</details>

<details>
<summary><b>💬 RAG-Powered Chat (No Vector DB)</b></summary>

Unlike conventional RAG, ResearchPilot uses **keyword-scored context retrieval** — no embeddings, no vector store, no GPU, no API service. Works with any AI engine. <1 s latency. Fully transparent (you can see which files matched).

</details>

<details>
<summary><b>📊 Dashboard, Quotes, Quick Notes</b></summary>

- **System Pulse** — live animated graph with 6 nodes (ResearchPilot, AI Engine, Library, Chat, Extractions, Knowledge Graph)
- **Quote of the Day** — 365+ quotes from Einstein, Curie, Sagan, Feynman, Tesla, Rumi, Mandela, and more
- **Quick Notes** — persistent sticky notes with full CRUD, stored server-side

</details>

---

## 📁 Project Structure

```
ResearchPilot/
├── web-app/                          # FastAPI web application
│   ├── main.py                       # Server + all API endpoints
│   ├── requirements.txt              # Python dependencies
│   ├── .env.example                  # Environment template
│   ├── static/
│   │   └── index.html               # Single-page frontend
│   ├── START-SERVER.bat             # Windows launcher (auto-installs deps)
│   ├── START-SERVER.sh              # macOS / Linux launcher
│   ├── install-windows.bat          # One-time Windows setup
│   ├── install-mac.sh               # One-time macOS / Linux setup
│   ├── uninstall-windows.bat        # Clean removal (Windows)
│   ├── uninstall-mac.sh             # Clean removal (macOS / Linux)
│   ├── REGISTER-AUTOSTART.bat       # Optional: start on Windows login
│   ├── test_smoke.py                # 21-test smoke suite
│   └── migrate_encrypt_settings.py  # One-time encryption migration
├── 00-SYSTEM-CORE/                   # Protocols, knowledge base (gitignored: personal)
├── 01-PROJECTS/                      # Research projects (gitignored: personal)
├── 99-SYSTEM-BACKEND/                # Settings, logs, chats (gitignored)
├── INCOMING/                         # New papers (gitignored)
├── graphify-out/                     # AST cache (gitignored)
├── .gitignore
├── LICENSE                           # MIT
├── LICENSE-APACHE                    # Apache 2.0
├── README.md                         # This file
├── SETUP.md                          # Beginner-friendly setup guide
├── SYSTEM-DOCUMENTATION.md           # Full architecture reference
├── SECURITY.md                       # Security policy + key rotation
└── CHANGELOG.md                      # Version history
```

---

## ⚙️ Settings

Accessible from the UI: **⚙️ Settings →**

| Section | Purpose |
|---|---|
| **General** | Context size · auto-extract · auto-start · timezone |
| **AI Engines** | Add, configure, enable/disable, reorder AI backends |
| **Skills** | Custom markdown instructions injected with every chat |
| **Knowledge Base** | Read-only view of the master synthesis |
| **Keywords** | Auto-scan and track research keywords |
| **Predatory Journals** | Manage filtered journal list |
| **Author** | Display information (gitignored) |
| **Plugins** | View and manage installed Python plugins |
| **Obsidian** | Connect to Obsidian vault |
| **Changelog** | Record version history |

---

## 🔒 Security

ResearchPilot is designed for **single-user, local-first** operation.

- 🛡️ **API keys encrypted at rest** with Fernet (AES-128-CBC + HMAC-SHA256); the master key lives in `99-SYSTEM-BACKEND/.settings_key` and is gitignored
- 🚦 **In-memory rate limiter** — 240 req/min/IP via sliding window; returns 429 if exceeded
- 📜 **Audit log** — every sensitive action recorded in `99-SYSTEM-BACKEND/audit.log` (rotating, 2 MB × 2); now also records tool calls (name + key list, never values)
- 🌐 **Localhost-only binding** by default (`127.0.0.1`)
- 🧹 **File sanitization** — filenames stripped of `..`, `~`, `<>:"/\\|?*`
- 🚧 **Path traversal protection** on every file endpoint (`resolve_era_path()` + per-tool Pydantic schema)
- 🛡️ **Prompt-injection & tool-abuse defence** (V5.3.2) — `ToolExecReq` Pydantic v2 schema (`Literal` of 10 allowed tool names) plus an orchestration interceptor that validates every LLM tool call (type, length, path safety, NUL bytes) before dispatch
- 🛡️ **SSRF defence** (V5.3.2) — engine URLs and external fetches validated against private IP ranges (`127.0.0.0/8`, `10/8`, `172.16/12`, `192.168/16`, `169.254/16`) and forbidden schemes (`file://`, `gopher://`, `ftp://`)
- 📁 **Filename standardisation** (V5.3.3) — Protocol 7 enforces `{Author}_{Year}[_{note}][_{N}].{ext}` for every paper artifact (extractions, library PDFs, web imports, summaries). First author only (`Alyami et al. - 2023.pdf` → `Alyami_2023.pdf`), apostrophes sanitised (`O'Brien` → `O_Brien`), collisions auto-disambiguated. Opt-in migration script: `python migrate_filename_format.py` (dry-run) → `--apply --backup` to commit.
- 🔬 **Input-driven web-research engine** (V5.4.0) — New `00-SYSTEM-CORE/SEARCH-SYSTEM/` folder. Purely user-input-driven, no project config required. 8-step NLP extraction → parallel multi-source search (OpenAlex · Crossref · Semantic Scholar with DOI + title-similarity dedupe) → trigram/bigram paper scoring → 4-tier journal quality filter (Tier 1 trusted / Tier 2 DOAJ / Tier 3 unverified / Tier 4 predatory) with Q1–Q4 quartile lookup, peer-review detection, and a user-supplied predatory list via `-ExtraPredatoryPath`.
- 🧩 **Graph cluster mode** (V5.4.0) — Set any graph-filter dim to `__any__` (or click "ALL" in the value dropdown) to group papers by Author / Year / Journal / Quartile / Method / Framework instead of filtering them. A central Category Hub node and per-value cluster nodes connect the files visually. Combine cluster and filter dims in one view (e.g. "show all Q1+Q2 papers clustered by year").
- 📦 **Upload size limit** 500 MB
- 🔐 **Admin SHA-256 password** for sensitive author settings
- 🚫 **Zero telemetry** — no analytics, no phone-home, no remote calls except configured AI engines and academic APIs

See [SECURITY.md](SECURITY.md) for the full security policy, key rotation procedure, threat model, and how to report vulnerabilities.

---

## 🧪 Testing

Run the smoke test suite (no server required, no network calls):

```bash
cd web-app
python test_smoke.py
```

Expected output:

```
[PASS] encryption roundtrip decrypts keys
[PASS] RAG cache warms (warm < cold/5)
[PASS] audit log writes correctly
[PASS] rotating log file present
[PASS] rate limiter configured (240 req / 60s)
[PASS] health endpoint registered
[PASS] global exception handler installed
[PASS] scan_keywords has _SKIP_PARTS guard
[PASS] audit() safe with edge-case input
[PASS] discard list is a set and non-empty
[PASS] manual add removes word from discard list
[PASS] manual remove adds word to discard list (cleaned up after)
[PASS] Graphify filters to research/extraction/chat only
[PASS] SSRF guard rejects private IPs and dangerous schemes
[PASS] interceptor rejects unknown tool names
[PASS] interceptor blocks path-traversal and NUL bytes
[PASS] interceptor caps string lengths and validates types
[PASS] interceptor enforces project/system-file allowlists
[PASS] ToolExecReq Pydantic schema rejects unknown tools + extras
[PASS] interceptor is wired into LLM tool-call loops + API
[PASS] SSRF guard wired into ai_respond and research_web_import
[PASS] filename utilities: canonical naming + disambiguation
[PASS] filename utilities: legacy detection + author-year parsing
[PASS] filename wiring: main.py endpoints + migration script present
[PASS] graph cluster: __any__ marker recognised in filter
[PASS] graph cluster: hub + value nodes created for __any__ dims
[PASS] graph cluster: filter and cluster dims combine correctly
[PASS] graph cluster: ALL placeholder rendered in value dropdown
30/30 passed
```
[PASS] encryption roundtrip decrypts keys
[PASS] RAG cache warms (warm < cold/5)
[PASS] audit log writes correctly
[PASS] rotating log file present
[PASS] rate limiter configured (240 req / 60s)
[PASS] health endpoint registered
[PASS] global exception handler installed
[PASS] scan_keywords has _SKIP_PARTS guard
[PASS] audit() safe with edge-case input
[PASS] discard list is a set and non-empty
[PASS] manual add removes word from discard list
[PASS] manual remove adds word to discard list (cleaned up after)
[PASS] Graphify filters to research/extraction/chat only
[PASS] SSRF guard rejects private IPs and dangerous schemes
[PASS] interceptor rejects unknown tool names
[PASS] interceptor blocks path-traversal and NUL bytes
[PASS] interceptor caps string lengths and validates types
[PASS] interceptor enforces project/system-file allowlists
[PASS] ToolExecReq Pydantic schema rejects unknown tools + extras
[PASS] interceptor is wired into LLM tool-call loops + API
[PASS] SSRF guard wired into ai_respond and research_web_import
[PASS] filename utilities: canonical naming + disambiguation
[PASS] filename utilities: legacy detection + author-year parsing
[PASS] filename wiring: main.py endpoints + migration script present
24/24 passed
```
[PASS] encryption roundtrip decrypts keys
[PASS] RAG cache warms (warm < cold/5)
[PASS] audit log writes correctly
[PASS] rotating log file present
[PASS] rate limiter configured (240 req / 60s)
[PASS] health endpoint registered
[PASS] global exception handler installed
[PASS] scan_keywords has _SKIP_PARTS guard
[PASS] audit() safe with edge-case input
[PASS] discard list is a set and non-empty
[PASS] manual add removes word from discard list
[PASS] manual remove adds to discard list (cleaned up after)
[PASS] Graphify filters to research/extraction/chat only
13/13 passed
```

---

## 📍 Where to Update (V5.4.0)

When extending ResearchPilot, the file you need depends on what you're changing:

| You're changing… | Edit this file / folder | Notes |
|---|---|---|
| **Web-research pipeline** (extraction, scoring, journal quality, search API) | `00-SYSTEM-CORE/SEARCH-SYSTEM/` | Pure PowerShell. Add new entry-point scripts here; update `WEB-SEARCH-WORKFLOW.md` with new rules. |
| **Q1–Q4 lookup or peer-review patterns** | `00-SYSTEM-CORE/SEARCH-SYSTEM/JOURNAL-QUARTILES.json` | Word-boundary match. Edit the JSON directly to add your discipline's journals. |
| **User-supplied predatory list** | `00-SYSTEM-CORE/SEARCH-SYSTEM/EXTRA-PREDATORY-TEMPLATE.json` → save as your own JSON file → pass via `-ExtraPredatoryPath` | See `EXTRA-PREDATORY-README.md`. |
| **Built-in Beall's list** (244 entries) | `00-SYSTEM-CORE/predatory_journals.json` | Loaded automatically; append-only. |
| **Graph layout, filters, or cluster mode** | `web-app/main.py` (Python) + `web-app/static/index.html` (JS) | Add a `__any__` branch in the graph endpoint, then handle the new placeholder in the dropdown. |
| **Filename canonical form** (Protocol 7) | `web-app/_filename_utils.py` | Plus `SYSTEM-PROTOCOLS.md` § Protocol 7. |
| **Auth, settings encryption, audit log, rate limit** | `web-app/main.py` | See `SECURITY.md` for the threat model. |
| **Knowledge-graph schema** (nodes, edges, categories) | `web-app/main.py` `get_graph_data` and `CAT_COLORS` | Hub category was added in V5.4.0 — copy that pattern for new node kinds. |
| **System version bump** | `00-SYSTEM-CORE/versions.json` + `CHANGELOG.md` + `README.md` (badge + features) + `CLAUDE.md` (status line) | All four must move in lockstep. |
| **Project template** (blueprint for new users) | `01-PROJECTS/00-TEMPLATE/` | Gitignored `01-PROJECTS/*` keeps personal projects out of Git. |
| **AI engine / LLM provider** | `web-app/main.py` (engine list + dispatch logic) | Each engine has its own dispatcher; follow the existing pattern. |
| **12-point extraction prompt** | `00-SYSTEM-CORE/skills/12-point-extraction.md` | The canonical source of the extraction template. |
| **Smoke tests** | `web-app/test_smoke.py` | One function per behaviour. Run with `python test_smoke.py` from `web-app/`. |

**One-glance orientation:** the top-level folder is the system. Each numbered folder has a single purpose:
- `00-SYSTEM-CORE/` — system specs, protocols, knowledge base, the new search engine, skill prompts
- `01-PROJECTS/` — per-project folders (gitignored except the template)
- `INCOMING/` — landing zone for new papers
- `99-SYSTEM-BACKEND/` — runtime logs, audit log, settings key (gitignored)
- `web-app/` — the FastAPI server + single-page UI

---

## 📡 New API Endpoints (V5.3+)

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/health` | GET | Liveness probe with service name, version, engine count |
| `/api/export/lit-review?project=X` | GET | Download all 12-point extractions as a single markdown bundle |

---

## 🤖 Built With AI

ResearchPilot was developed **entirely** using **[OpenCode](https://opencode.ai)** — a free, local AI coding agent — with no manual coding. Every component, from the FastAPI backend to the single-page frontend, was built through AI-assisted development.

This project demonstrates that researchers and academics can build production-grade tools without a traditional software background, using AI as the development engine.

---

## 📜 License

Dual-licensed under your choice of:

- [MIT License](LICENSE) — permissive, simple
- [Apache License 2.0](LICENSE-APACHE) — explicit patent grant

---

## 🌟 Star History

If ResearchPilot helps your research, consider giving it a ⭐ on GitHub — it helps others discover the project.

<div align="center">

**[⬆ Back to Top](#researchpilot-subv53sub)**

</div>
