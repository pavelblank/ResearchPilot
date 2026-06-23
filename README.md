<div align="center">

# 🔬 ResearchPilot V5.5.0

**AI-native research platform for academics and PhD students. Self-hosted. Local-first.**

Ingest papers · Extract insights · Search 5 academic databases · Build knowledge graphs · Write with RAG chat

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi)
![License](https://img.shields.io/badge/License-Apache%202.0%20%7C%20MIT-blue?style=flat-square)
![Self-Hosted](https://img.shields.io/badge/Deployment-Self--Hosted-orange?style=flat-square)
![AI-Native](https://img.shields.io/badge/AI-12%20Engine%20Failover-purple?style=flat-square)
![Offline](https://img.shields.io/badge/Works-Offline-green?style=flat-square)

**[Features](#-features-in-detail) · [Quick Start](#-quick-start) · [Prerequisites](#-prerequisites) · [Security](#-security) · [License](#-license)**

</div>

---

## 📸 Screenshots

<table>
  <tr>
    <td align="center" width="50%">
      <img src="5.5%20Home%20Dashboard.png" alt="Dashboard" width="100%"/>
      <br/><b>🏠 Home Dashboard</b> — System Pulse, quotes, stats, quick notes
    </td>
    <td align="center" width="50%">
      <img src="5.5%20Web%20Research.png" alt="Web Research" width="100%"/>
      <br/><b>🔍 Web Research</b> — 5 academic sources, NLP scoring, journal tier filter
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="5.5%20Knowledge%20Graph.png" alt="Knowledge Graph" width="100%"/>
      <br/><b>🕸 Knowledge Graph</b> — 7 dimensions, AND/OR filters, cluster mode
    </td>
    <td align="center" width="50%">
      <img src="5.5%20RAG%20Chat.png" alt="RAG Chat" width="100%"/>
      <br/><b>💬 RAG Chat</b> — answers grounded in your library, zero hallucination
    </td>
  </tr>
</table>

---

## ✨ Why ResearchPilot?

- **100% local:** papers, extractions, chat history and AI keys never leave your machine.
- **12-engine AI failover:** Ollama, Gemini, Claude, OpenRouter, NVIDIA and more — if one fails, the next takes over automatically.
- **Universal file ingestion:** PDF · DOCX · PPTX · HTML · TXT · MD · CSV · JSON, all auto-converted to Markdown.
- **12-Point Elite Extraction:** every paper analysed via APA, DOI, Quartile, Method, Framework, Limitations and more.
- **5-source academic search:** OpenAlex · Crossref · Semantic Scholar · PubMed · Google Scholar with predatory-journal filtering.
- **Multi-dimensional knowledge graph:** filter by Author, Year, Journal, Quartile, Method, Framework or Keyword (AND/OR logic).
- **RAG-powered chat:** no vector DB, no embeddings, no GPU — keyword-scored context retrieval across your entire library.
- **Obsidian-compatible:** the entire folder is a valid Obsidian vault with an instant knowledge graph.
- **Encrypted at rest:** API keys stored using Fernet (AES-128-CBC + HMAC-SHA256) — keys never leave your machine.
- **Rate-limited + audit-logged:** 240 req/min/IP, every sensitive action recorded in `audit.log`.

---

## 📋 Prerequisites

| Requirement | Minimum | Notes |
|---|---|---|
| Python | 3.10+ | 3.11 recommended |
| OS | Windows 10+ / macOS / Linux | Any platform Python runs on |
| RAM | 4 GB | 8 GB recommended for local AI |
| Disk | ~200 MB + papers | Grows with your library |
| AI (optional) | Any OpenAI-compatible API | Ollama works offline and is free |

---

## 🚀 Quick Start

### 1. Install Python

Skip if `python --version` already prints 3.10+. Otherwise download from [python.org](https://www.python.org/downloads/) and tick **"Add python.exe to PATH"** on Windows.

### 2. Clone the repository

```bash
git clone https://github.com/pavelblank/ResearchPilot.git
cd ResearchPilot
```

### 3. Install dependencies

```bash
pip install -r 99-SYSTEM-BACKEND/requirements.txt
```

### 4. Run the app

**Windows:** double-click `start-research.bat`

**macOS / Linux:**
```bash
python 99-SYSTEM-BACKEND/main.py
```

### 5. Open in your browser

```
http://localhost:8000
```

### 6. Add an AI engine

Go to **Settings → AI Engines** and add your preferred provider:

| Engine | Notes |
|---|---|
| Ollama (local) | Free, runs offline. Install from [ollama.com](https://ollama.com) |
| OpenAI (GPT-4o) | Requires an API key |
| Anthropic (Claude) | Requires an API key |
| OpenRouter | Access 100+ models with one key |
| NVIDIA NIM | GPU-accelerated inference |

---

## 🔥 Features in Detail

### 📚 Paper Ingestion

- Drop PDFs into the `INCOMING/` folder and tell ResearchPilot to process them.
- Papers are moved to your project library and run through the **12-Point Extraction Protocol**: APA citation, DOI, journal quartile, research method, theoretical framework, key findings, limitations, future work and more.
- Supports PDF · DOCX · PPTX · HTML · TXT · MD · CSV · JSON.

### 🔍 Web Research

- Input-driven: paste your research question and get results from 5 academic databases simultaneously.
- NLP extraction pipeline: trigram/bigram scoring + journal-quality tier filter (Q1–Q4 + peer-review).
- No project config required — works from a single search query.

### 🕸 Knowledge Graph

- Visualise your entire library as an interactive graph.
- Filter by 7 dimensions: Author · Year · Journal · Quartile · Method · Framework · Keyword.
- AND/OR logic for complex queries.
- Cluster mode: group papers by dimension with a central hub node — mix with filters in one view.

### 💬 RAG Chat

- Ask questions about your entire library in plain English.
- No vector DB or GPU required — keyword-scored retrieval with 45-second result cache.
- Answers grounded strictly in your papers — zero hallucination policy.
- Chat history persisted locally.

### 🧠 Smart Keyword System

- Auto-scans your library and suggests keywords.
- Manual deletes are remembered permanently — deleted keywords never re-appear on auto-scan.
- Re-adding a deleted keyword restores it until you delete it again.

### 🔒 Security

- **Encrypted API keys:** Fernet encryption (AES-128-CBC + HMAC-SHA256) — keys never leave your machine.
- **Rate limiting:** 240 req/min per IP.
- **Audit log:** every sensitive action (settings save, project delete, file delete, tool call) recorded.
- **Prompt-injection hardened:** Pydantic v2 schema + orchestration interceptor block unknown tool names, path traversal and oversized args.
- **SSRF guard:** private-IP engine URLs rejected at validation time.
- **No telemetry:** zero external calls except to whichever AI provider you configure.

---

## 📁 Project Structure

```
ResearchPilot/
├── 00-SYSTEM-CORE/         # System specs, protocols, master knowledge base
├── 01-PROJECTS/            # Your research projects (P1, P2, ...)
│   └── P1/
│       ├── 01-LIBRARY/     # Papers (PDF + Markdown)
│       └── 02-EXTRACTIONS/ # 12-point extraction files
├── 99-SYSTEM-BACKEND/      # FastAPI app, requirements, logs
│   ├── main.py
│   └── requirements.txt
├── INCOMING/               # Drop new PDFs here
├── start-research.bat      # Windows launcher
├── SETUP.md
├── CHANGELOG.md
└── README.md
```

---

## 🔄 Updating

```bash
git pull
pip install -r 99-SYSTEM-BACKEND/requirements.txt --upgrade
```

Restart the app afterwards.

---

## 🤝 Contributing

Issues and pull requests are welcome. Fork the repo, create a feature branch, and describe what changed and why in your PR.

---

## 🤖 Built With AI

ResearchPilot was built entirely using **Claude Code** (Anthropic), demonstrating that a production-grade academic research platform can be created through AI-assisted development with no traditional software background required.

---

## 📜 License

Apache License 2.0 · MIT License. Free to use, modify and distribute. See [LICENSE](LICENSE) for details.

---

<div align="center">

*Self-hosted. Local-first. Your research, your machine, your keys.*

</div>
