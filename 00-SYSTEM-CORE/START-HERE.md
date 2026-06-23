# ResearchPilot V5.3.1 — Quick Start

> **For users:** see [README.md](../README.md) for install + run instructions and [SETUP.md](../SETUP.md) for the full cross-platform guide.
>
> **This file** is for the **system itself** — it explains what `00-SYSTEM-CORE/` is and how the four sub-systems fit together.

## What This Folder Is

`00-SYSTEM-CORE/` is the **brain** of ResearchPilot. It contains only **public, system-level** files:

- **System specification** — what this software is and how it works
- **System protocols** — standards every AI engine must follow
- **Skills** — markdown instructions injected into every AI conversation
- **Reference data** — predatory-journal list, version history

Your **personal data** lives elsewhere:
- `01-PROJECTS/` — your research projects
- `99-SYSTEM-BACKEND/` — your settings, audit log, encrypted API keys, chat history
- `INCOMING/` — PDFs waiting to be sorted into a project

## The Four Sub-Systems

| Sub-system | Folder | Purpose |
|---|---|---|
| **System Core** | `00-SYSTEM-CORE/` | Brain: protocols, skills, reference data (this folder) |
| **Projects** | `01-PROJECTS/` | Your research projects — each has 4 subfolders |
| **Backend** | `99-SYSTEM-BACKEND/` | Settings, logs, encrypted API keys, chats |
| **Web App** | `web-app/` | FastAPI server + single-page UI (HTML/CSS/JS) |

## How to Use the System

1. **Start the server** — see [SETUP.md](../SETUP.md) for one-time install:
   - 🪟 Windows: double-click `web-app/START-SERVER.bat`
   - 🍎 macOS: run `web-app/START-SERVER.sh`
   - 🐧 Linux: run `web-app/START-SERVER.sh`
2. **Open** <http://127.0.0.1:8000> in your browser
3. **Create a project** in Settings → Projects
4. **Upload PDFs** via the Upload tab (drag-and-drop)
5. **Chat with the AI** — it can read any file in your system using built-in tools

## The Golden Rules

- **Zero Hallucination** — the AI only uses content from your library
- **Elite Standards** — every paper gets a 12-point deep analysis
- **Local-First** — your data never leaves your machine
- **Encrypted at Rest** — API keys are Fernet-encrypted (AES-128-CBC + HMAC-SHA256)

## File Reference

- [SYSTEM-SPECIFICATION.md](SYSTEM-SPECIFICATION.md) — what this software is and how it works
- [SYSTEM-PROTOCOLS.md](SYSTEM-PROTOCOLS.md) — standards every AI engine follows
- [skills/12-point-extraction.md](skills/12-point-extraction.md) — the 12-point analysis protocol
- [skills/academic-writing.md](skills/academic-writing.md) — citation and writing standards
- [skills/researchpilot-system-overview.md](skills/researchpilot-system-overview.md) — system overview (for AI context)
- [predatory_journals.json](predatory_journals.json) — 244+ flagged publishers (auto-filtered from web search)
- [versions.json](versions.json) — version history

---

**Version:** V5.3.1 · **Last Updated:** 2026-06-04
