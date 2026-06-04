# ResearchPilot V5.3.3 — System Specification

## Purpose

ResearchPilot is a **self-hosted research operating system** for academic researchers and PhD students. It runs entirely on the user's machine, with all data stored locally. The system connects to multiple AI backends (Ollama, Gemini, Claude, OpenRouter, NVIDIA, and more) and provides a complete workflow for academic research — from paper discovery and ingestion to AI-powered extraction, multi-dimensional knowledge graphs, and RAG-augmented writing.

## Design Principles

- **Local-first** — your data never leaves your machine
- **Multi-AI failover** — 12 engine types, priority-based fallback if one fails
- **Zero hallucination** — the AI only uses content from your library
- **Elite standards** — every paper gets a 12-point deep analysis
- **Encrypted at rest** — API keys Fernet-encrypted, master key gitignored
- **Open format** — everything is markdown + JSON, no proprietary database

## Core Architecture — 4-Subfolder System

| Sub-system | Folder | Purpose |
|---|---|---|
| **System Core** | `00-SYSTEM-CORE/` | Brain: protocols, skills, reference data |
| **Projects** | `01-PROJECTS/` | Research projects (papers, extractions, manuscripts) |
| **Backend** | `99-SYSTEM-BACKEND/` | Settings, logs, encrypted API keys, chats |
| **Web App** | `web-app/` | FastAPI server + single-page UI |

### Each Project Has 4 Subfolders

| Subfolder | Purpose |
|---|---|
| `01-LIBRARY/` | Source PDFs (auto-converted to `.md` on upload) |
| `02-EXTRACTIONS/` | 12-point analysis per paper |
| `03-MANUSCRIPTS/` | Drafts, chapters, literature reviews |
| `99-META/` | Project notes and AI context |

## Workflow

1. **Discovery** — Web Research tab searches 5 academic sources in parallel
2. **Ingestion** — PDFs dropped into `INCOMING/` or uploaded via the UI
3. **Extraction** — AI performs 12-point Elite Extraction
4. **Synthesis** — Knowledge graph visualises 7 dimensions (Author, Year, Journal, Quartile, Method, Framework, Keyword)
5. **Manuscript Drafting** — AI chat pulls context from extractions and library, suggests text

## Technical Stack

- **Backend**: Python 3.10+, FastAPI, Uvicorn
- **Storage**: Markdown files + JSON config (no database)
- **AI**: 12 engine types with priority-based failover
- **Search**: Keyword-scored RAG (no vector DB, no embeddings, no GPU)
- **Auth**: Per-install random token stored in `.token` (gitignored)
- **Encryption**: Fernet (AES-128-CBC + HMAC-SHA256) for API keys at rest
- **UI**: Single-page HTML/CSS/JS (no React, no build step)

## Supported File Formats

| Format | Parser | Auto .md |
|---|---|:-:|
| PDF | Docling (preferred) → PyMuPDF | ✅ |
| DOCX / DOC | python-docx | ✅ |
| PPTX / PPT | python-pptx | ✅ |
| HTML / HTM | html2text | ✅ |
| TXT · CSV · JSON · YAML · MD | direct read | ✅ |

## Web UI Tabs

1. **Home** — system pulse, quote of the day, stats
2. **Web Research** — 5-source academic search with predatory-journal filter
3. **Upload** — drag-and-drop PDF upload with auto-conversion
4. **Projects** — create, manage, switch between projects
5. **Library** — browse all extractions in current project
6. **Knowledge Graph** — multi-dimensional filter (7 dimensions, AND/OR)
7. **Chat** — RAG-powered AI chat with full tool access
8. **Manuscripts** — view and edit drafts
9. **Settings** — AI engines, skills, keywords, audit log, etc.

## Security

- API keys encrypted at rest (Fernet AES-128-CBC + HMAC-SHA256)
- Master key in `99-SYSTEM-BACKEND/.settings_key` (gitignored, never committed)
- In-memory rate limiter: 240 req/min/IP
- Audit log for sensitive operations (settings.save, project.delete, file.delete, lit-review.export)
- Localhost-only binding by default (`127.0.0.1`)
- File sanitization on all uploads
- Path-traversal protection on every file endpoint
- Zero telemetry — no analytics, no phone-home, no remote calls except configured AI engines and academic APIs

See [SECURITY.md](../SECURITY.md) for the full security policy and key-rotation procedure.

---

**Version:** V5.3.2 · **Last Updated:** 2026-06-04
