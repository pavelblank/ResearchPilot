# ResearchPilot <sub>V5.3</sub>

> **AI-native research infrastructure for academics or students.**  
> Ingest papers, extract insights via AI, search across 5 academic databases, visualise knowledge graphs, and write with RAG-powered chat — all self-hosted, all local-first.

---

> `CLAUDE.md` contains AI behaviour instructions for Claude Code integration — optional, safe to ignore.

##  Overview

ResearchPilot is a self-hosted research assistant that connects to multiple AI backends (Ollama, Gemini, Claude, OpenRouter, etc.) and provides a complete workflow for academic research:

- **Ingest** any file (PDF, DOCX, PPTX, HTML, TXT, MD) — auto-converts to Markdown
- **Extract** papers using the 12-point Elite Extraction Protocol via AI
- **Search** across 5 academic databases (OpenAlex, Crossref, Semantic Scholar, ArXiv, PubMed)
- **Visualize** research with a multi-dimension knowledge graph
- **Chat** with AI using your research library as RAG context
- **Track** keywords, predatory journals, and version changelog
- **Dashboard** — live System Pulse graph with animated nodes, Quote of the Day (365 quotes)
- **Quick Notes** — persistent CRUD notes stored server-side in `99-SYSTEM-BACKEND/notes.json`
- **Multi-AI Engine Router** — unlimited engines with priority-based failover

---

## 📸 Screenshots (V5.3)

<div align="center">
  <table>
    <tr>
      <td><img src="5.3.0-%20Home%20page%20dashbard%20.png" alt="Home Dashboard" width="300"></td>
      <td><img src="5.3.0-%20Web%20Research%20page.png" alt="Web Research" width="300"></td>
      <td><img src="5.3.0-%20Knowledge%20Graph%20page.png" alt="Knowledge Graph" width="300"></td>
    </tr>
    <tr>
      <td align="center"><b>🏠 Home Dashboard</b></td>
      <td align="center"><b>🔍 Web Research</b></td>
      <td align="center"><b>🕸 Knowledge Graph</b></td>
    </tr>
  </table>
</div>

---

##  Prerequisites

| Requirement | Minimum |
|-------------|---------|
| **Python** | 3.10+ (tested on 3.11) |
| **OS** | Windows 10+ / Linux / macOS |
| **Ollama** (optional) | Install from [ollama.com](https://ollama.com) and pull a model (`ollama pull llama3`) |
| **Disk space** | ~500 MB for dependencies + your papers |

---

##  Quick Start

### 1. Install

```bash
# Clone or download
cd ResearchPilot/web-app

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure AI

Copy and edit the environment file:

```bash
cp .env.example .env
```

Set at least one AI key (or use local Ollama):

| Engine | How to Get |
|--------|-----------|
| **Ollama** (free, local) | Install from [ollama.com](https://ollama.com), pull a model like `llama3` |
| **Gemini** (free tier) | Get key at [aistudio.google.com](https://aistudio.google.com/app/apikey) |
| **Claude** | API key from [console.anthropic.com](https://console.anthropic.com) |
| **OpenRouter** (free models) | Key from [openrouter.ai](https://openrouter.ai) |

### 3. Run

```bash
python main.py
```

Open **http://127.0.0.1:8000** in your browser.

>  **Windows users:** Double-click `START-SERVER.bat`

---

##  Features

###  Universal File Ingestion
| Format | Auto-converts to .md |
|--------|:---:|
| PDF | ✅ (via PyMuPDF or Docling) |
| DOCX / DOC | ✅ |
| PPTX / PPT | ✅ |
| HTML / HTM | ✅ |
| TXT / CSV / JSON | ✅ |

###  Multi-AI Engine Router
Tries enabled engines in priority order. First one that responds wins — **your AI never stops**. Supports any number of engines with auto-failover, per-engine enable/disable, and dynamic priority ordering.

Supported types: `OpenAI-compatible (OpenRouter, Jan, LocalAI)` · `Ollama (local)` · `Gemini` · `Claude API` · `Claude CLI (login)` · `Custom Plugin`

Includes auto-failover on empty content, tool calling, and model-level configuration per engine.

###  Academic Web Search
Search across 5 sources simultaneously:

- **OpenAlex** — 250M+ works
- **Crossref** — scholarly publishing metadata
- **Semantic Scholar** — AI-powered paper discovery
- **PubMed** — biomedical literature
- **Google Scholar** — broad academic search (via scholarly)

With automatic predatory journal filtering, PDF download, and 12-point AI analysis.

###  Knowledge Graph
Visualize your research across 7 dimensions:

`Author` · `Year` · `Journal` · `Quartile` · `Method` · `Framework` · `Keyword`

Multi-layer filtering with AND/OR logic. Built-in Obsidian vault integration.

**Graphify** — built-in code-level AST graph engine. Annotates every source file, class, and function with semantic metadata. Renders an interactive visual code-map alongside your paper graph, powered by `graphify-out/cache/`.

###  12-Point Elite Extraction Protocol
Every paper is analyzed through:

1. **APA Reference** — Full academic citation
2. **DOI** — Digital Object Identifier
3. **Journal Name** — Full name and ranking
4. **Quartile Ranking** — Q1/Q2 verified via Scopus/SJR
5. **Indexing** — Scopus, Web of Science confirmation
6. **Research Method** — Quantitative, Qualitative, Mixed, or Review
7. **Theoretical Framework** — Primary theories used
8. **Exact Relevance** — Specific utility for the PhD project
9. **Section Support** — Which chapter or section it informs
10. **Key Contribution** — The "One Big Insight"
11. **Limitations** — Critical gaps identified by authors
12. **Classification** — Behaviour, Governance, Technical, or Essential

###  Chat with RAG
Chat with any enabled AI engine. Automatically injects relevant context from your research library — no manual file selection needed.

###  System Pulse Dashboard
Live animated graph with 6 interconnected nodes: **ResearchPilot** (center), AI Engine, Library, Chat, Extractions, and Knowledge Graph — each with pulsing status dots and real-time counts.

###  Quote of the Day
365+ inspiring quotes from Einstein, Curie, Sagan, Feynman, Tesla, Rumi, Mandela, and more — rotates by day of year with a refresh button for random picks. No network fetch needed (all embedded client-side).

###  Quick Notes
Persistent sticky notes with full CRUD (Create, Read, Update, Delete). Stored server-side in `99-SYSTEM-BACKEND/notes.json` — survives browser clears and reboots. Accessible from sidebar, max 3 visible with scroll.

---

##  Project Structure

```
ResearchPilot/
├── web-app/                          # FastAPI web application
│   ├── main.py                       # Server + all API endpoints (~3100 lines)
│   ├── requirements.txt              # Python dependencies
│   ├── .env.example                  # Environment template
│   ├── static/
│   │   └── index.html               # Single-page frontend (~3800 lines)
│   ├── START-SERVER.bat             # Windows launcher
│   └── test_final.py                # Test suite
├── 00-SYSTEM-CORE/                   # System protocols, master knowledge base
├── 01-PROJECTS/                      # Research projects (P1, P2, ...)
├── 99-SYSTEM-BACKEND/               # Chats, logs, notes, automation reports
│   └── notes.json                   # Quick Notes persistent storage
├── INCOMING/                         # Landing zone for new papers
├── graphify-out/                    # Graphify AST cache (knowledge graph engine)
├── .gitignore
└── README.md                        # This file
```

---

##  Settings

Accessible from the UI: **⚙️ Settings →**  

| Section | Purpose |
|---------|---------|
| General | Context size, auto-extract, auto-start, timezone |
| AI Engines | Add, configure, enable/disable, and reorder AI backends |
| Skills | Custom markdown instructions injected with every chat |
| Knowledge Base | Read-only view of the master synthesis |
| Keywords | Auto-scan and track research keywords |
| Predatory Journals | Manage filtered journal list |
| Author | Display information |
| Plugins | View and manage installed Python plugins |
| Obsidian | Connect to Obsidian vault for bidirectional sync |
| Changelog | Record version history |

---

##  Security Notes

- Server binds to `127.0.0.1` by default (localhost only)
- API keys are stored locally in `settings.json` (excluded from git)
- Uploaded files are sanitized and limited to 500MB
- Path traversal is blocked on all file endpoints

---

## 🤖 Built With AI

ResearchPilot was developed entirely using **[OpenCode](https://opencode.ai)** —
a free, local AI coding agent — with no manual coding involved. Every component,
from the FastAPI backend to the single-page frontend, was built through
AI-assisted development.

This project demonstrates that researchers and academics can build
production-grade tools without a traditional software development background,
using AI as the development engine.

---

##  Author

**Md Yeahia Bhuiyan**
*AI Enthusiast*

I am a researcher and educator specialising in cybersecurity behaviour, organisational culture, and privacy mental models in Higher Education Institutions. My work bridges qualitative academic research and applied AI systems design.

ResearchPilot was built as part of a broader effort to construct portable, AI-assisted research infrastructure — systems that reduce cognitive overhead, preserve research continuity, and support publication-quality output across long-term academic projects.

**Research Interests**
Cybersecurity behaviour · Privacy mental models · Organisational culture · Protection Motivation Theory · AI-assisted academic workflows

**Connect**
- GitHub: [pavelblank]
- Institution: [skip]
- Contact: mrblank1010ai@gmail.com

---


