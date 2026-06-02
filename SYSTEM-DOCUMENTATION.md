# ResearchPilot: Complete System Documentation

> **A Self-Hosted, AI-Native Research Operating System for PhD-Level Academic Workflows**
> Version: 2.0 | System Architecture: ResearchPilot V5.3 | Built: May–June 2026

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [Architecture & Folder Structure](#2-architecture--folder-structure)
3. [Backend Server — FastAPI (main.py)](#3-backend-server--fastapi-mainpy)
4. [Frontend — Single-Page Application (index.html)](#4-frontend--single-page-application-indexhtml)
5. [Multi-AI Engine Router](#5-multi-ai-engine-router)
6. [RAG Context Retrieval System](#6-rag-context-retrieval-system)
7. [Universal File Ingestion Pipeline](#7-universal-file-ingestion-pipeline)
8. [The 12-Point Elite Extraction Protocol](#8-the-12-point-elite-extraction-protocol)
9. [Knowledge Graph & Graphify Engine](#9-knowledge-graph--graphify-engine)
10. [Multi-Source Academic Web Search](#10-multi-source-academic-web-search)
11. [Chat Persistence & Session System](#11-chat-persistence--session-system)
12. [Project Management System](#12-project-management-system)
13. [Keywords & Auto-Scan Engine](#13-keywords--auto-scan-engine)
14. [Predatory Journal Filter](#14-predatory-journal-filter)
15. [Plugin Architecture](#15-plugin-architecture)
16. [Author Profile & Admin Security](#16-author-profile--admin-security)
17. [Obsidian Integration](#17-obsidian-integration)
18. [Skills System](#18-skills-system)
19. [Windows Auto-Start & Scheduled Tasks](#19-windows-auto-start--scheduled-tasks)
20. [Innovation Claims](#20-innovation-claims)
21. [Limitations & Future Work](#21-limitations--future-work)
22. [Full API Endpoint Reference](#22-full-api-endpoint-reference)

---

## 1. System Overview

### 1.1 What Is ResearchPilot?

ResearchPilot is a **self-hosted, AI-native research operating system** that provides a complete workflow for academic research: discovering papers, ingesting them, extracting structured insights via AI, visualizing knowledge relationships, and writing with RAG-powered assistance — all without requiring a traditional software development background.

### 1.2 Core Philosophy

- **Zero Hallucination**: All AI claims are grounded in the user's actual research library files. The AI is equipped with 10 file-access tools and *must* use them rather than generate fake citations.
- **Local-First**: All data stays on the user's machine. AI engines can be fully local (Ollama, LM Studio) or cloud-based (Gemini, Claude, OpenRouter).
- **Researcher-as-Architect**: The system is designed so that a PhD researcher with no coding background can build, extend, and control a production-grade research tool through AI-assisted development.
- **Obsidian-Compatible**: Every chat, extraction, and note is saved as plain Markdown (`.md`) — the native format of Obsidian vaults.

### 1.3 Key Innovations

| Innovation | Description |
|------------|-------------|
| **AI-Native Development** | Entire 3200+ line codebase built through OpenCode, an AI coding agent — zero hand-written code |
| **Multi-AI Failover Router** | 8 engine types with priority-based failover; system never stops if one engine goes down |
| **RAG Without Vector DB** | Keyword-scoring context retrieval across all research files, no embeddings/vector store needed |
| **Multi-Layer Knowledge Graph** | 7-dimension filterable graph (Author, Year, Journal, Quartile, Method, Framework, Keyword) with AND/OR logic |
| **12-Point Automated Extraction** | Full academic paper analysis pipeline from PDF ingestion to structured research output |
| **5-Source Web Discovery** | Simultaneous search across OpenAlex, Crossref, Semantic Scholar, ArXiv, PubMed with auto-deduplication |
| **Graphify AST Engine** | Code-level Abstract Syntax Tree graph generation for visualizing the system's own codebase |

---

## 2. Architecture & Folder Structure

### 2.1 Top-Level Directory

```
C:\F- Drive\MYWORK-Research1\
├── 00-SYSTEM-CORE/              # Centralized intelligence & system governance
│   ├── MASTER-KNOWLEDGE-BASE.md # Synthesis of all 24+ papers
│   ├── SYSTEM-PROTOCOLS.md      # 5 operational protocols
│   ├── ResearchPilot-SYSTEM-SPECIFICATION.md  # Definitive system manual
│   ├── RESEARCHER-PROFILE.md    # AI assistant memory & preferences
│   ├── GLOBAL-CONNECTIONS.md    # Cross-paper theoretical mapping
│   ├── PUBLISHING-ROADMAP.md    # PhD-to-publication strategy
│   ├── keywords.json            # Auto-extracted keyword index
│   ├── discarded_keywords.json   # User-deleted keywords (never re-add)
│   ├── predatory_journals.json  # Filtered journal blacklist
│   ├── versions.json            # System changelog
│   ├── skills/                  # Reusable skill markdown files
│   └── plugins/                 # External plugin API key storage
│
├── 01-PROJECTS/                 # Active research publication modules
│   ├── 00-TEMPLATE/             # Project blueprint (4 subfolders)
│   ├── P1-HEI-CULTURE/         # HEI Cybersecurity Culture Study
│   │   ├── 01-LIBRARY/         # Source PDFs (Foshay, Alyami, Bansal)
│   │   ├── 02-EXTRACTIONS/     # 24 x 12-point analyses (P001–P024)
│   │   ├── 03-MANUSCRIPTS/     # Drafts, outlines, sections, final
│   │   └── 99-META/            # Manifest, citations, connections, queries
│   ├── P2-YEAHIA-BACKBONE/     # Infrastructure research
│   ├── CO--EZAZ-PROJECT/       # Collaborative project
│   └── CO-NAZMUL-PROJECT/      # Collaborative project
│
├── 99-SYSTEM-BACKEND/          # System logs, automation, settings
│   ├── settings.json           # All persistent configuration
│   ├── chats/                  # All chat sessions (.md format)
│   ├── SYSTEM-MANIFEST.md      # Portability guide for AI recovery
│   ├── SYSTEM-OVERVIEW.md      # High-level system summary
│   ├── AUTOMATION-REPORT.md    # Batch processing logs
│   └── plugins/                # Plugin API key JSON files
│
├── INCOMING/                   # Landing zone for new papers
│   └── UNREAD-WEB/             # Web-imported papers (PDF + .md)
│
├── web-app/                    # FastAPI server + frontend
│   ├── main.py                 # ~3227-line Python backend
│   ├── static/
│   │   └── index.html          # ~2400-line SPA frontend
│   ├── .env                    # Environment variables (gitignored)
│   ├── .env.example            # Template for .env
│   ├── requirements.txt        # Python dependencies
│   ├── START-SERVER.bat        # Windows server launcher
│   └── test_final.py           # Test suite
│
├── graphify-out/               # AST cache for knowledge graph
├── start-research.bat          # One-click system launcher
├── CLAUDE.md                   # AI behaviour instructions
├── README.md                   # Project overview
├── LICENSE                     # MIT License
├── LICENSE-APACHE              # Apache License 2.0
└── SYSTEM-DOCUMENTATION.md     # This file
```

### 2.2 Protocol 2: Project Standardization

Every research project is initialized with exactly 4 folders:

| Folder | Purpose |
|--------|---------|
| `01-LIBRARY` | Source PDFs and auto-converted markdown |
| `02-EXTRACTIONS` | 12-point deep analyses for manuscript evidence |
| `03-MANUSCRIPTS` | Active writing: drafts, outlines, sections, final |
| `99-META` | Project-specific logs, manifests, connections |

### 2.3 System Operational Flow

```
Discovery (Web Search) → Import (PDF/.md download)
    ↓
INCOMING/ folder
    ↓
Upload/Move → Project 01-LIBRARY/
    ↓
12-Point AI Extraction → Project 02-EXTRACTIONS/
    ↓
Synthesis → 00-SYSTEM-CORE/MASTER-KNOWLEDGE-BASE.md
    ↓
Manuscript Drafting → Project 03-MANUSCRIPTS/
```

---

## 3. Backend Server — FastAPI (main.py)

### 3.1 Technology Stack

- **Framework**: FastAPI (Python 3.10+)
- **Server**: Uvicorn ASGI server
- **File Handling**: PyMuPDF (fitz), python-docx, python-pptx, html2text, Docling
- **Async HTTP**: httpx with AsyncClient
- **Serialization**: Pydantic models, json

### 3.2 Application Bootstrap

```python
# File: web-app/main.py — 3227 lines total
```

The server initializes by:

1. **Loading `.env`** — reads environment variables from the parent directory
2. **Importing optional dependencies** — Docling (`docling`), DOCX (`python-docx`), PPTX (`python-pptx`), Anthropic SDK (`anthropic`) — all with graceful fallback if not installed
3. **Setting up paths** — `BASE`, `PROJECTS`, `CORE`, `BACKEND`, `INCOMING`, `CHATS_DIR`, `SKILLS_DIR`, `PLUGINS_DIR`, `SETTINGS_F`
4. **Loading plugin API keys** — scans `99-SYSTEM-BACKEND/plugins/*.json` and injects keys into environment
5. **Creating directories** — ensures all required folders exist
6. **Loading default settings** — 8 pre-configured AI engines with priority ordering

### 3.3 Security Measures

| Measure | Implementation |
|---------|----------------|
| Path Traversal Protection | `resolve_era_path()` — resolves relative paths and verifies they stay within BASE |
| Sanitized Filenames | `sanitize_filename()` — strips `..`, `~`, and special chars `<>:"/\\|?*` |
| HTML Injection | `strip_html()` — replaces `<` and `>` with HTML entities in settings |
| File Size Limit | `MAX_UPLOAD_SIZE = 500MB` |
| Local Host Binding | Server binds to `127.0.0.1` by default |
| Password Hashing | `hashlib.sha256` for admin panel (not bcrypt — lightweight local setup) |

### 3.4 Key Classes and Models

```python
class ChatReq(BaseModel):
    session_id: str
    message: str
    project: Optional[str] = None
    pdf_context: Optional[str] = None
    skills: Optional[List[str]] = None
    exclude_summary: Optional[bool] = False

class ExtractReq(BaseModel):
    project: str
    filename: str

class ToolExecReq(BaseModel):
    tool: str
    args: dict = {}
```

---

## 4. Frontend — Single-Page Application (index.html)

### 4.1 Technology

- Pure HTML/CSS/JavaScript (no framework — ~2400 lines)
- **vis-network** library from CDN for graph visualization
- All CSS custom properties (CSS variables) for theming
- Fully responsive (3 breakpoints: 768px, 480px)

### 4.2 UI Structure

The interface is organized into 10 tabs:

| Tab | Purpose |
|-----|---------|
| **Home** | Dashboard with project stats, file counts, extraction counts |
| **Chat** | AI chat with RAG context, project/file/skill selectors, session management |
| **Upload** | Drag-and-drop file upload with auto-conversion to .md |
| **Web Research** | Multi-source academic paper search with download + AI analysis |
| **Library** | Searchable table of all files across all projects |
| **Memory** | All .md files (library + extractions) in one searchable view |
| **Plugins** | AI engine plugin connections (Claude, Gemini, Ollama) |
| **Graph** | Multi-layer filterable knowledge graph with 7 dimensions |
| **Obsidian** | Vault integration info and launch buttons |
| **Settings** | AI engines, skills, projects, KB, keywords, predatory journals, author, changelog |

### 4.3 Key Frontend Functions

| Function | Lines | Purpose |
|----------|-------|---------|
| `boot()` | ~10 | Initializes all data, starts clock, polls AI status |
| `send()` | ~20 | Sends chat messages with RAG context, skills, PDF context |
| `searchWebResearch()` | ~50 | Orchestrates multi-source academic search |
| `loadGraph()` | ~100 | Builds vis-network graph with filter layers |
| `runGraphify()` | ~5 | Triggers AST-based graph refresh |
| `renderKeywords()` | ~40 | Renders keyword list with multi-select, editing, deletion |
| `scanKeywords()` | ~15 | Auto-scans all .md files for keyword extraction |

### 4.4 Color Theme System

```css
:root {
  --bg: #0d0f14;
  --surface: #151820;
  --panel: #1c2030;
  --card: #202438;
  --border: #2a2f45;
  --accent: #6c63ff;
  --a2: #00d4aa;
  --gold: #f5c518;
  --red: #ff4d6d;
  --text: #e8eaf0;
  --muted: #8892a4;
}
```

---

## 5. Multi-AI Engine Router

### 5.1 Architecture

The router is the system's most architecturally significant component. It implements a **priority-based failover chain**:

```python
ENGINE_HANDLERS = {
    "ollama": _try_ollama,
    "openai_compat": _try_openai_compat,
    "gemini": _try_gemini,
    "anthropic": _try_anthropic,
    "claude_plugin": _try_claude_plugin,
}
```

### 5.2 Engine Resolution Flow

```
User sends message
    ↓
build_rag_prompt() — injects relevant research context
    ↓
Engines sorted by priority (1 = highest)
    ↓
For each enabled engine:
    ├── Call handler(engine, messages)
    ├── If success → return (text, engine_name, tool_uses)
    └── If failure → log error, try next engine
    ↓
If ALL fail → return error message listing which engines were tried
```

### 5.3 Engine Type Details

#### 5.3.1 Ollama (Local)
- **Type**: `ollama`
- **Protocol**: Custom Ollama API (`/api/chat`)
- **Tool Support**: Yes — sends `ResearchPilot_TOOLS` definitions on first request
- **Context Window Detection**: Queries model metadata via `/api/show` to detect `num_ctx`
- **Tool Loop**: Up to 3 iterations of tool-calling before final response
- **Default Model**: `llama3`

#### 5.3.2 OpenAI-Compatible (OpenRouter, LM Studio, Custom)
- **Type**: `openai_compat`
- **Protocol**: OpenAI Chat Completions API (`/chat/completions`)
- **Tool Support**: Yes — same tool definitions
- **Identity Headers**: Sets `HTTP-Referer` and `X-Title` for OpenRouter identification
- **Default Models**: `mistralai/mistral-7b-instruct:free` (OpenRouter), `local-model` (LM Studio)

#### 5.3.3 Gemini (Google)
- **Type**: `gemini`
- **Protocol**: Google Generative Language API (`generateContent`)
- **Tool Support**: No — direct text generation only
- **Authentication**: API key via `GEMINI_API_KEY` env var or settings
- **Default Model**: `gemini-1.5-flash` (free tier)

#### 5.3.4 Anthropic (Claude API)
- **Type**: `anthropic`
- **Protocol**: Anthropic Messages API (`/v1/messages`)
- **Tool Support**: No — direct text only
- **System Prompt**: Extracted from messages and passed as `system` parameter
- **Default Model**: `claude-sonnet-4-20250514`

#### 5.3.5 Claude Plugin (CLI + SDK Fallback)
- **Type**: `claude_plugin`
- **Strategy**: Tries two methods:
  1. **Claude CLI**: Runs `claude -p "prompt"` as subprocess
  2. **Anthropic SDK**: Falls back to Python SDK if CLI unavailable
- **Purpose**: Allows users with a paid Claude account to use it without API keys

### 5.4 Tool Calling System

The AI is equipped with **10 research tools** defined in `ResearchPilot_TOOLS`:

| Tool | Description |
|------|-------------|
| `read_file(path)` | Read any file in the research system |
| `search_files(query)` | Search all files for matching text |
| `list_directory(path)` | List files in any directory |
| `get_project_list()` | List projects with stats |
| `read_knowledge_base()` | Read Master Knowledge Base |
| `read_extractions_list(project)` | List extraction files |
| `read_extraction(project, filename)` | Read specific extraction |
| `read_project_manifest(project)` | Read project manifest |
| `get_system_structure()` | Get folder structure overview |
| `read_system_core(filename)` | Read any system file |

Each tool:
1. Accepts string arguments from the AI
2. Validates paths against BASE directory (security)
3. Returns JSON with either `content` or `error`
4. Is executed via `execute_tool(name, args)` — an async function with try/except for every tool

### 5.5 Tool Execution Loop

```
AI Request → messages → LLM
    ↓
Response contains tool_calls?
    ├── NO → Return content (final response)
    └── YES →
        For each tool_call:
            ├── Execute tool with arguments
            └── Append tool result to messages
        ↓
        Send back to LLM (up to 3 iterations)
```

---

## 6. RAG Context Retrieval System

### 6.1 Design

Unlike conventional RAG systems that use vector embeddings and vector databases, ResearchPilot implements a **keyword-scoring retrieval** approach — no embeddings, no vector store, no GPU needed.

### 6.2 Retrieval Algorithm

```python
def retrieve_relevant_context(query, project=None, max_chars=25000):
```

**Step 1**: Extract query words (length > 3 characters).

**Step 2**: Score each file across 5 categories:

| Source | Weight | Max Chars |
|--------|--------|-----------|
| Extraction files (.md) | 1 pt/word, +3 title bonus | 8,000 |
| Master Knowledge Base | 2 pts/word (doubled) | 10,000 |
| Library markdown files | 1 pt/word, +2 title bonus | 6,000 |
| System core files (.md, .json) | 1 pt/word | 5,000 |
| Project manifests | 1 pt/word | 3,000 |

**Step 3**: Sort by score descending, truncate to `max_chars`.

**Step 4**: Format as `## RELEVANT RESEARCH CONTENT` section injected into the system prompt.

### 6.3 Key Advantage

This approach:
- Requires **zero** setup (no embedding model, no vector DB)
- Runs on **any hardware** (no GPU needed)
- Works with **any AI engine** (no special API needed)
- Is **fully transparent** (users can see exactly which files matched)
- Is **instant** (file reading, not vector computation)

---

## 7. Universal File Ingestion Pipeline

### 7.1 Supported Formats

| Format | Parser | Fallback |
|--------|--------|----------|
| PDF | Docling (preferred) | PyMuPDF (fitz) |
| DOCX/DOC | python-docx | — |
| PPTX/PPT | python-pptx | — |
| HTML/HTM | html2text | — |
| TXT, MD, CSV, JSON, YAML | Direct read | — |

### 7.2 Conversion Function

```python
def file_to_markdown(path: Path) -> str:
```

The function dispatches based on file extension:

1. **PDF**: Tries Docling (preserves structure, tables, headings) → falls back to PyMuPDF (page-level text extraction)
2. **DOCX/DOC**: Extracts paragraphs with heading level detection
3. **PPTX/PPT**: Extracts text per-slide with slide numbering
4. **HTML/HTM**: Converts to markdown preserving links
5. **Plain text**: Direct file read

### 7.3 Save Pipeline

```python
def save_as_md(source_path, dest_folder, extra_meta=""):
```

Generates a markdown file with:
- H1 title (filename stem)
- Source attribution (`*Source: \`filename\` | Imported: timestamp*`)
- Optional extra metadata
- Content separator `---`
- Full converted text

### 7.4 Upload Flow

```
User drops file(s) → /api/upload
    ↓
File saved to destination (INCOMING or project library)
    ↓
Auto-converted to .md in same folder
    ↓
(Optional) Auto-extract via 12-point AI analysis
```

---

## 8. The 12-Point Elite Extraction Protocol

### 8.1 Protocol Definition (from SYSTEM-PROTOCOLS.md)

```
Protocol 1: The 12-Point Elite Extraction
1. APA Reference     — Full academic citation
2. DOI               — Digital Object Identifier
3. Journal Name      — Full name and ranking
4. Quartile Ranking  — Q1/Q2 status via Scopus/SJR
5. Indexing          — Scopus, Web of Science, etc.
6. Research Method   — Quantitative, Qualitative, Mixed, or Review
7. Theoretical Framework — Primary theories used
8. Exact Relevance   — Specific utility for the current PhD project
9. Section Support   — Which chapter or section it informs
10. Key Contribution — The "One Big Insight"
11. Limitations      — Critical gaps identified by authors
12. Classification   — (Behaviour, Governance, Technical, or Essential)
```

### 8.2 AI-Driven Extraction

When the user triggers extraction via UI or API:

1. PDF text is read (up to 40,000 chars)
2. A detailed prompt instructs the AI to produce structured 12-point analysis
3. The AI's response is saved as a new extraction file with auto-incrementing ID
4. The PDF is automatically moved from INCOMING to the project's 01-LIBRARY

```python
# Extraction ID generation
code = f"P{(max(existing, default=0) + 1):03d}"  # P001, P002, ...
out = ext_dir / f"{code} - {pdf_path.stem}.md"
```

### 8.3 Automated 12-Point from Web Search

For papers discovered via web search that are NOT Open Access, the system generates a 12-point analysis from the abstract/metadata alone using the `_12_POINT_SYSTEM` prompt template:

```python
_12_POINT_SYSTEM = """You are an expert academic research analyst...
1. The Problem  2. The Gap  3. The Research Question(s)
4. The Purpose / Objective  5. The Theory or Framework
6. The Methodology  7. The Key Findings  8. The Contribution
9. The Limitations  10. The Implications  11. Key Citations
12. Your Critical Position"""
```

### 8.4 Extraction Storage Format

Each extraction file follows this template:

```markdown
# P001 — Author et al. (Year)
*Extracted: 2026-05-08 14:30 | Engine: DeepSeek Chat (Priority 1)*

#### 1. APA Reference
Full citation text...

#### 2. DOI
10.xxxx/xxxxx

#### 3. Journal Name
Journal Name (Q1 / Scopus)

[Points 4–12 follow the same structure...]

#### 📜 Exact Quotes
- *"Verbatim quote from paper"*

#### 🔬 Section-by-Section Details
- **Introduction**: ...
- **Method**: ...
```

---

## 9. Knowledge Graph & Graphify Engine

### 9.1 Overview

The Knowledge Graph visualizes research relationships across 7 dimensions with multi-layer filtering, built on the **vis-network** JavaScript library. Additionally, **Graphify** provides an AST-based code visualization layer.

### 9.2 Graph Data Sources

The graph combines data from two sources:

#### 9.2.1 Research File Metadata (All .md files)

Every `.md` file in the system is scanned and categorized:

```python
def _cat(filepath):
    if "chats" in path: return "chat"
    if "02-extractions" in path: return "extraction"
    if "01-library" in path: return "research"
    if "00-system-core" in path: return "system"
    if "99-system-backend" in path: return "system"
    if extension in (.py, .js, .json): return "code"
    if extension == ".md": return "research"
    return "other"
```

Metadata is extracted from extraction files via regex:

```python
def _parse_metadata(text):
    # Extracts: author, year, journal, quartile, method, framework, keyword
    regex patterns for each field
```

#### 9.2.2 Graphify AST Cache (`graphify-out/cache/ast/`)

Graphify generates **Abstract Syntax Tree** nodes for all code files in the project:

| Category | Source | Example Nodes |
|----------|--------|---------------|
| code | `web-app/` | Python functions, classes, imports |
| system | `graphify-out/`, `.claude/` | Cache entries |
| research | `.md` files | Paper nodes |
| extraction | `02-EXTRACTIONS/` | Analysis nodes |
| chat | `99-SYSTEM-BACKEND/chats/` | Session nodes |
| keyword | Keywords index | Tag nodes |

### 9.3 Edge Generation

Three types of edges connect nodes:

| Edge Type | Weight | Logic |
|-----------|--------|-------|
| **same_project** | 0.3 | Files in same project connect to first file |
| **shared_keywords** | 0.05–5.0 | Files with ≥5 shared keywords, scored by Jaccard similarity |
| **dimension_filter** | 0.5/1.0 | Explicit filter connections (author, year, journal, etc.) |

### 9.4 Multi-Layer Filter System

Users can apply up to 4 filter layers with AND/OR logic:

```
Layer 1: Author="Bhuiyan"  (no operator, implicitly AND)
Layer 2: Year="2026"       AND
Layer 3: Method="Review"   OR
Layer 4: Keyword="privacy" AND
```

The filter URL encodes as: `author:Bhuiyan|AND:year:2026|OR:method:Review`

Filter resolution:
```python
matched_files = None  # No constraint
For each layer:
    layer_matched = files_matching(dimension, value)
    if matched_files is None: matched_files = layer_matched
    elif op == "AND": matched_files &= layer_matched
    else: matched_files |= layer_matched
```

### 9.5 Graph Visual Properties

Each file type gets a distinct color and shape in vis-network:

| Category | Color | Shape |
|----------|-------|-------|
| research | Purple | dot |
| extraction | Blue | dot |
| chat | Green | dot |
| code | Orange | square |
| system | Red | diamond |
| keyword | Gold | star |

### 9.6 Graphify Refresh

The `runGraphify()` function in the UI triggers a complete re-scan of all `.md` files, re-extracting keywords and rebuilding the metadata cache.

---

## 10. Multi-Source Academic Web Search

### 10.1 Architecture

The web search engine queries **5 academic databases simultaneously** using their free REST APIs:

| Source | API Endpoint | Free Tier Limit |
|--------|-------------|-----------------|
| **OpenAlex** | `api.openalex.org/works` | Unlimited |
| **Crossref** | `api.crossref.org/works` | Unlimited |
| **Semantic Scholar** | `api.semanticscholar.org/graph/v1/paper/search` | 100 req/min |
| **ArXiv** | `export.arxiv.org/api/query` | Unlimited |
| **PubMed** | `eutils.ncbi.nlm.nih.gov/entrez/eutils/` | Unlimited |

### 10.2 Search Flow

```
User enters query → selects sources, year range, sort order
    ↓
ALL selected sources queried in parallel via asyncio.gather()
    ↓
Results from each source normalized into uniform schema
    ↓
Deduplication by DOI and title (fuzzy 60-char match)
    ↓
Predatory journal filter (case-insensitive partial match)
    ↓
Sorting (citations ↓, date ↓, or relevance)
    ↓
Return deduped, filtered, sorted results
```

### 10.3 Result Schema

Every paper from every source is normalized to:

```python
{
    "title": str,
    "authors": [str],
    "year": str,
    "journal": str,
    "doi": str,
    "abstract": str (800 chars),
    "citations": int,
    "is_oa": bool,
    "oa_url": str,
    "pdf_url": str,
    "source": str,
    "is_predatory": bool
}
```

### 10.4 Import Actions

For each search result, users can:

| Action | Description |
|--------|-------------|
| **Read** | Preview full metadata + abstract in modal |
| **Open** | Navigate to paper's URL in browser |
| **Download PDF** (OA only) | Download PDF → auto-convert to .md via Docling → save to UNREAD-WEB |
| **Download .md with 12-Point** (non-OA) | Save metadata + AI-generated 12-point analysis to UNREAD-WEB |
| **Import** (PDF + .md) | Combined: download PDF + generate analysis + save both |

### 10.5 PDF Download Pipeline

```python
# 1. Try OA URL
async with httpx.AsyncClient(follow_redirects=True) as c:
    r = await c.get(oa_url)
    if "application/pdf" in content-type → save as .pdf

# 2. If OA fails, try alternative sources
for try_url in [doi.org, sci-hub.se, unpaywall.org]:
    attempt download

# 3. Convert PDF to .md via Docling
md_fulltext = file_to_markdown(pdf_path)
```

### 10.6 Deduplication Algorithm

```python
def _dedup_results(results):
    seen_dois = set()
    seen_titles = set()
    for r in results:
        doi_key = r["doi"].lower().strip()
        title_key = r["title"].lower().strip()[:60]
        if doi_key in seen_dois: skip
        if title_key in seen_titles: skip
        add to deduped list
```

### 10.7 Predatory Journal Filtering

```python
predatory = _load_predatory()  # Set of lowercase journal name fragments
for r in deduped:
    journal = r["journal"].lower().strip()
    r["is_predatory"] = any(p in journal for p in predatory)
    if not is_predatory: keep
```

---

## 11. Chat Persistence & Session System

### 11.1 Storage Format

Every chat session is saved as a `.md` file in `99-SYSTEM-BACKEND/chats/`:

```markdown
# ResearchPilot Chat: 2026-06-01-14-30-00
*Started: 2026-06-01 14:30:00*
*Project: P1-HEI-CULTURE*
Tags: #ResearchPilot #research #chat #P1-HEI-CULTURE

---

### 👤 You
*2026-06-01 14:30:05*

What is the key finding of Foshay et al.?

---

### 🤖 ResearchPilot (DeepSeek Chat)
*2026-06-01 14:30:12*

The key finding is...
```

### 11.2 Chat Parsing

Messages are parsed from the `.md` file using role markers:

| Marker | Role |
|--------|------|
| `### 👤 You` | user |
| `### 🤖 ResearchPilot (...)` | assistant |
| `### 🤖 AI Research Assistant` | assistant (legacy) |
| `### 🤖 ERA` | assistant (legacy) |

### 11.3 Session Management

```
/api/chat/new                          → Create session ID (timestamp)
/api/chat POST                         → Send message, get AI response
/api/chats GET                         → List all sessions
/api/chat/{session_id} GET             → Load session messages
/api/chat/{session_id} DELETE          → Delete session
/api/chat/{session_id}/clear POST      → Archive + clear session
```

### 11.4 RAG Injection in Chat

Each chat message goes through the full RAG pipeline:

1. User sends message with optional `project`, `pdf_context`, `skills`
2. `build_rag_prompt()` retrieves relevant context from research files
3. `/skillname` commands in the message auto-load matching skill files
4. If `pdf_context` is set, the full PDF text is prepended to the message
5. If `exclude_summary` is set, the AI is instructed to give comprehensive responses

---

## 12. Project Management System

### 12.1 CRUD Operations

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/projects` | GET | List all projects with paper/extraction counts |
| `/api/projects` | POST | Create new project (auto-generates 4 subfolders + manifest) |
| `/api/projects/{id}` | DELETE | Delete project and all files |
| `/api/projects/{id}` | PUT | Rename project + update keyword file paths |

### 12.2 Project Creation

```python
def create_project(data):
    name = sanitize(data["name"])  # alphanumeric + hyphens
    for folder in ["01-LIBRARY", "02-EXTRACTIONS", "03-MANUSCRIPTS", "99-META"]:
        (PROJECTS / name / folder).mkdir(parents=True)
    # Write PROJECT-MANIFEST.md with focus, goal, and phase checklist
```

### 12.3 Project Manifest Template

```markdown
# Project: P3-CYBERSECURITY
Created: 2026-06-01
Focus: [description]
Goal: [publication target]

## Status
- [ ] Phase 1: Library
- [ ] Phase 2: Extractions
- [ ] Phase 3: Drafting
- [ ] Phase 4: Submit
```

### 12.4 File Library Management

`/api/library` returns all files across all projects with:
- Filename, extension, size
- Whether a `.md` companion exists
- Last modified date
- Move-to-project actions

`/api/library/move` moves a file AND its `.md` companion between projects.
`/api/library/{project}/{filename}` DELETE removes both file and `.md`.

---

## 13. Keywords & Auto-Scan Engine

### 13.1 Data Storage

Keywords are stored in `00-SYSTEM-CORE/keywords.json`:

```json
{
  "cybersecurity": {
    "files": ["01-PROJECTS/P1-HEI-CULTURE/02-EXTRACTIONS/P001 - ..."],
    "note": "auto (score: 47)"
  },
  "qualitative": {
    "files": [...],
    "note": "auto (score: 23)"
  }
}
```

### 13.2 Auto-Scan Algorithm

```python
def scan_keywords():
    word_counter = Counter()
    stopwords = {"the", "this", "that", ...}  # 80+ English stopwords
    special_terms = {"q1", "q2", "scopus", "heis", "p1", "ai", "rag", ...}
    
    For every .md file:
        extract words (3+ chars, lowercase)
        weight = 5 if special_term else 1
        word_counter[word] += weight
    
    For top 200 words (score >= 2):
        add to keywords.json with file list
```

### 13.3 Discarded Keywords

When the user deletes a keyword, it's added to `discarded_keywords.json` — the auto-scan will never re-add it.

### 13.4 Keyword Search

`/api/keywords/search?q=privacy` returns all files matching a keyword, enabling quick cross-referencing.

---

## 14. Predatory Journal Filter

### 14.1 Data Source

A set of journal name fragments stored in `00-SYSTEM-CORE/predatory_journals.json`.

### 14.2 Fetch Online

The system fetches from public predator lists:
```python
urls = [
    "https://raw.githubusercontent.com/nicole-richey/predatory-journals/main/predatory-journals.json",
    "https://raw.githubusercontent.com/stop-predatory-journals/..."
]
```

### 14.3 Matching Logic

```python
# Case-insensitive partial match
is_pred = any(fragment in journal.lower() for fragment in predatory_set)
```

Example: `"waset"` matches `"WASET Journal of Engineering"`.

---

## 15. Plugin Architecture

### 15.1 Plugin Registry

```python
PLUGIN_REGISTRY = {
    "claude": { "name": "Claude AI", "icon": "🤖", "type": "anthropic" },
    "claude_login": { "name": "Claude Login", "icon": "🔐", "type": "claude_plugin" },
    "gemini": { "name": "Google Gemini", "icon": "🔮", "type": "gemini" },
    "ollama": { "name": "Ollama (Local)", "icon": "🦙", "type": "ollama" },
}
```

### 15.2 API Key Storage

Plugin API keys are stored in two ways:
1. `99-SYSTEM-BACKEND/plugins/*.json` — loaded at boot into environment
2. `settings.json` — managed through the web UI

### 15.3 Connect/Disconnect Flow

```
Connect:
    1. User pastes API key in UI
    2. POST /api/plugins/{id}/connect
    3. API key saved to settings.json
    4. Corresponding engine enabled
    
Disconnect:
    1. POST /api/plugins/{id}/disconnect
    2. Engine disabled, API key cleared
```

---

## 16. Author Profile & Admin Security

### 16.1 Author Data

Stored in `00-SYSTEM-CORE/author.json`:

```json
{
    "name": "Md Yeahia Bhuiyan",
    "title": "Researcher, Educator and AI Enthusiast",
    "phd": "Information Technology, Cybersecurity",
    "masters": "Information Security",
    "copyright": "© 2026 Md Yeahia Bhuiyan. All rights reserved.",
    "_password_hash": "sha256hash..."
}
```

### 16.2 Password Protection

The Author settings page is protected by an admin password:

```python
# Password verification
stored_hash = existing.get("_password_hash", "")
if hashlib.sha256(pw.encode()).hexdigest() != stored_hash:
    raise HTTPException(403, "Incorrect admin password")
```

The password is:
- Hashed with SHA-256 before storage
- Never returned in API responses (the `_password_hash` field is stripped)
- Verified via separate `/verify` endpoint (no data saved)

---

## 17. Obsidian Integration

### 17.1 Design Philosophy

The entire ResearchPilot folder IS an Obsidian vault. Every file — chats, extractions, library conversions, manifests — is stored as `.md` with frontmatter-compatible metadata.

### 17.2 Automatic Graph

Because Obsidian builds its graph from internal `[[wikilinks]]`, `#tags`, and folder structure, opening the ResearchPilot root in Obsidian immediately creates a rich knowledge graph:

- **Chats** are tagged `#ResearchPilot #research #chat #ProjectName`
- **Extractions** are tagged by project
- **All files** are searchable via Obsidian's built-in search

### 17.3 Launch Buttons

The Obsidian tab provides:
- **Open Vault**: Opens the ResearchPilot root in Obsidian
- **Open Graph**: Opens Obsidian's built-in graph view
- **Vault Statistics**: Shows `.md` file counts, project counts, chat counts

---

## 18. Skills System

### 18.1 What Are Skills?

Skills are reusable markdown instruction files stored in `00-SYSTEM-CORE/skills/`. They are injected into every AI chat to shape its behavior.

### 18.2 Example Skills

| Skill | Content |
|-------|---------|
| `APA-Citation-Style.md` | "Always use APA 7th edition citation format..." |
| `Critical-Reviewer.md` | "When analyzing papers, focus on methodological weaknesses..." |
| `Extraction-Format.md` | "Always output the 12-point analysis with the following format..." |

### 18.3 Skill Loading

Skills are loaded via:
1. **Chat toolbar**: Multi-select dropdown in the chat UI
2. **Slash commands**: `/skillname` in the chat message auto-loads matching skill file
3. **API**: POST `/api/chat` with `skills: [list]`

```python
# Slash command parsing
for match in re.finditer(r'/([\w\-]+)', message):
    skill_file = SKILLS_DIR / f"{cmd}.md"
    if skill_file.exists():
        skill_names.add(skill_file.name)
```

---

## 19. Windows Auto-Start & Scheduled Tasks

### 19.1 Mechanism

The system can auto-start on Windows login via two methods:

1. **Scheduled Task** (primary): `schtasks /create /tn "ResearchPilot-ResearchAssistant" /tr "start-research.bat" /sc ONLOGON`
2. **Startup Folder**: Creates a `.lnk` shortcut in the Windows Startup folder

### 19.2 Implementation

```python
if enabled:
    bat_path = str(BASE / "start-research.bat")
    subprocess.run(["schtasks", "/create", "/tn", "ResearchPilot...",
                   "/tr", bat_path, "/sc", "ONLOGON", "/ru", username, "/f"])
```

---

## 20. Innovation Claims

### 20.1 AI-Native Development

**Claim**: ResearchPilot is one of the first documented production-grade software systems built entirely through AI-assisted development (via OpenCode), with zero manual coding by a non-programmer domain expert.

**Evidence**:
- ~3,227 lines of Python backend (FastAPI)
- ~2,400 lines of HTML/CSS/JavaScript frontend
- Built by a PhD cybersecurity researcher, not a software engineer
- All code generated, reviewed, and refined through AI chat sessions

### 20.2 Zero-Configuration RAG

**Claim**: The keyword-scoring RAG system achieves relevant context retrieval without requiring any of: vector database, embedding model, GPU, API service, or configuration.

| Traditional RAG | ResearchPilot RAG |
|-----------------|-------------------|
| Requires embedding model | Zero ML dependencies |
| Requires vector DB (Pinecone, Chroma, etc.) | Flat file scan |
| GPU recommended | CPU only |
| Opaque relevance scores | Transparent keyword match |
| Average 2-5 second latency | <1 second (file read) |

### 20.3 Multi-AI Failover Architecture

**Claim**: The priority-based engine router guarantees uninterrupted AI service. If any engine fails (rate limit, outage, key expiry), the next engine in priority order handles the request transparently.

### 20.4 No-Spend Academic Search

**Claim**: The system can search 5 major academic databases (OpenAlex, Crossref, Semantic Scholar, ArXiv, PubMed) simultaneously — all free APIs with no API keys required — deduplicating results across all sources.

### 20.5 Portable Research Operating System

**Claim**: The entire system is AI-agnostic and designed for portability. The SYSTEM-MANIFEST.md allows any AI model with filesystem access to resume operations — no specific platform required.

---

## 21. Limitations & Future Work

### 21.1 Current Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| No vector embeddings | Less semantically accurate than embedding-based RAG | Keyword scoring with title bonus compensates |
| Single-user (no login system) | Not suitable for team use | Designed for solo PhD researcher |
| Windows-centric auto-start | Linux/macOS users must manually start | Manual start via Python works on all platforms |
| No HTTPS by default | Not suitable for network exposure | Binds to localhost only |
| SHA-256 password (not bcrypt) | Less secure than adaptive hashing | Acceptable for local single-user setup |
| SHA-256 password hashing | Weaker than bcrypt/argon2 | Acceptable for local single-user setup with no network exposure |
| No concurrent user sessions | Only one browser can connect | Adequate for single researcher workflow |
| Large paper volumes (>500 files) | Graph and keyword scans may slow | Pagination and caching could be added |
| No native mobile interface | Desktop-only currently | Responsive CSS provides basic mobile support |

### 21.2 Future Roadmap

| Feature | Priority | Description |
|---------|----------|-------------|
| Vector DB integration | Medium | Optional Chroma/FAISS for semantic RAG |
| Collaborative projects | Low | Multi-user login and shared libraries |
| Zotero/Mendeley import | Medium | Auto-import library metadata |
| Automated paper summaries | Low | Daily digest of new relevant papers |
| Literature review generator | High | Auto-generate lit review sections from extractions |
| Citation graph (citation.network) | Medium | Show how papers cite each other visually |
| PDF annotation viewer | Low | In-browser PDF reader with highlights |
| AI-powered writing suggestions | Medium | Context-aware sentence completion from papers |

### 21.3 Research Integrity

The system's zero-hallucination directive is enforced through:
1. **Tool-required prompts**: The AI is instructed to use file tools for ALL factual claims
2. **Source transparency**: Every tool call is logged and visible in chat
3. **Quote verification**: Extractions store exact quotes with page/section references
4. **No outside knowledge**: The system prompt explicitly forbids using external knowledge for research claims

---

## 22. Full API Endpoint Reference

### 22.1 Settings

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/settings` | GET | Load all settings |
| `/api/settings` | POST | Save all settings |
| `/api/settings/author` | GET | Get author profile |
| `/api/settings/author` | POST | Save author profile (with password verification) |
| `/api/settings/author/verify` | POST | Verify admin password |
| `/api/settings/versions` | GET | Get version changelog |
| `/api/settings/versions` | POST | Add/remove version entries |
| `/api/auto-start` | GET | Check auto-start status |
| `/api/auto-start` | POST | Enable/disable Windows auto-start |

### 22.2 AI Engines & Status

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/status` | GET | Check AI engine status (online/offline) |
| `/api/plugins` | GET | List available plugins |
| `/api/plugins/{id}/connect` | POST | Connect plugin (save API key) |
| `/api/plugins/{id}/disconnect` | POST | Disconnect plugin |

### 22.3 Projects

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/projects` | GET | List all projects |
| `/api/projects` | POST | Create new project |
| `/api/projects/{id}` | DELETE | Delete project |
| `/api/projects/{id}` | PUT | Rename project |

### 22.4 Library & Files

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/library` | GET | List all files |
| `/api/library/move` | POST | Move file + .md to another project |
| `/api/library/{project}/{filename}` | DELETE | Delete file + .md |
| `/api/upload` | POST | Upload single file |
| `/api/upload-folder` | POST | Upload multiple files as new project |
| `/api/file/{project}/{filename}` | GET | Read file content |

### 22.5 Extractions

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/extractions` | GET | List all extractions |
| `/api/extraction/{project}/{filename}` | GET | Read extraction content |
| `/api/extraction/{project}/{filename}` | DELETE | Delete extraction |
| `/api/extract` | POST | Run 12-point extraction on PDF |

### 22.6 Chat

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/chat` | POST | Send message, get AI response |
| `/api/chat/new` | POST | Create new session |
| `/api/chats` | GET | List all sessions |
| `/api/chat/{id}` | GET | Load session messages |
| `/api/chat/{id}` | DELETE | Delete session |
| `/api/chat/{id}/clear` | POST | Archive + clear session |

### 22.7 Knowledge Graph

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/graph` | GET | Get graph data (nodes + edges) |
| `/api/graph/filters` | GET | Get available filter dimensions |
| `/api/graph/file` | GET | Get file content by relative path |
| `/api/graph/refresh` | POST | Re-scan all files, rebuild cache |

### 22.8 Web Research

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/research/search` | GET | Search across all sources |
| `/api/research/import` | POST | Import paper (with PDF download) |
| `/api/research/save-md` | POST | Save paper metadata as .md |
| `/api/research/save-md-with-analysis` | POST | Save .md + 12-point AI analysis |
| `/api/research/download-pdf` | POST | Download OA PDF + auto-convert |
| `/api/research/papers` | GET | List UNREAD-WEB papers |
| `/api/research/pdf/{filename}` | GET | Serve PDF file |
| `/api/research/file/{filename}` | GET | Serve .md file |
| `/api/research/move-to-project` | POST | Move paper from UNREAD-WEB to project |
| `/api/research/paper/{filename}` | DELETE | Delete paper from UNREAD-WEB |

### 22.9 Keywords

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/keywords` | GET | List all keywords |
| `/api/keywords` | POST | Add/remove/edit/batch-remove keywords |
| `/api/keywords/scan` | POST | Auto-scan all .md files |
| `/api/keywords/search` | GET | Search by keyword |
| `/api/keywords/discarded` | GET | Get discarded keywords |
| `/api/keywords/discarded` | POST | Restore discarded keyword |

### 22.10 Predatory Journals

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/predatory` | GET | List all filtered journals |
| `/api/predatory` | POST | Add/remove/set journal list |
| `/api/predatory/online` | GET | Fetch latest online lists |

### 22.11 Tools & Knowledge Base

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/tools` | GET | List all available tools |
| `/api/tools/execute` | POST | Execute a tool directly |
| `/api/knowledge-base` | GET | Read Master Knowledge Base |
| `/api/memory` | GET | List all .md files |
| `/api/skills` | GET | List all skills |
| `/api/skills` | POST | Save new skill |
| `/api/skills/{name}` | DELETE | Delete skill |

---

## Technical Appendix

### A.1 Deployment Requirements

| Component | Requirement |
|-----------|-------------|
| Python | 3.10+ |
| RAM | 512 MB (min), 2 GB (recommended) |
| Disk | ~500 MB for dependencies + paper library |
| OS | Windows 10+, Linux, macOS |
| Optional | Ollama (for fully local AI), Obsidian (for graph view) |

### A.2 Python Dependencies

```txt
fastapi>=0.100.0      # Web framework
uvicorn>=0.23.0       # ASGI server
python-multipart>=0.0.6  # File uploads
pymupdf>=1.23.0       # PDF extraction (fallback)
httpx>=0.25.0         # Async HTTP client
aiofiles>=23.0.0      # Async file operations
html2text>=2024.0.0   # HTML→Markdown conversion
docling>=2.0.0         # PDF→Markdown (preferred)
# Optional: python-docx, python-pptx, anthropic
```

### A.3 Startup Commands

```bash
# Start server
cd web-app
python main.py
# Open: http://127.0.0.1:8000

# Windows batch
start-research.bat
```

### A.4 License

ResearchPilot is dual-licensed under **MIT OR Apache 2.0**:
- `LICENSE` — MIT License (Copyright 2026 Md Yeahia Bhuiyan)
- `LICENSE-APACHE` — Apache License, Version 2.0 (Copyright 2026 Md Yeahia Bhuiyan)

---

*Document generated: June 1, 2026 | System: ResearchPilot V5.3 | Backend: 3,227 lines Python + 2,400 lines HTML/CSS/JS | Build tool: OpenCode AI Assistant*
