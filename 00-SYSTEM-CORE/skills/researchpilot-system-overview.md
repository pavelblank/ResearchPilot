# Skill: ResearchPilot System Overview

When a user asks "how does this work?" or "what is ResearchPilot?", provide this overview.

## Architecture
ResearchPilot is a self-hosted research operating system with 4 sub-systems:

- **00-SYSTEM-CORE/** — system brain (protocols, skills, reference data)
- **01-PROJECTS/** — research projects (each with 4 subfolders: LIBRARY, EXTRACTIONS, MANUSCRIPTS, META)
- **99-SYSTEM-BACKEND/** — settings, logs, encrypted API keys, chat history
- **web-app/** — FastAPI server + single-page UI (HTML/CSS/JS, no React, no build step)

## Each Project's 4 Subfolders
- `01-LIBRARY/` — uploaded PDFs (auto-converted to .md)
- `02-EXTRACTIONS/` — 12-point analysis per paper
- `03-MANUSCRIPTS/` — drafts and writing
- `99-META/` — project notes, AI context

## Workflow
1. Drop PDF in INCOMING/ or upload via web UI (Upload tab)
2. System converts to markdown and stores in project's 01-LIBRARY/
3. AI performs 12-point extraction → 02-EXTRACTIONS/
4. Knowledge graph visualizes 7 dimensions (Author, Year, Journal, Quartile, Method, Framework, Keyword)
5. RAG chat pulls context from extractions + library (keyword-scored, no vector DB)
6. Manuscript drafting with AI assistance (03-MANUSCRIPTS/)

## AI Engines (12 supported types)
- **Local (free)**: Ollama, LM Studio, Jan, LocalAI
- **Cloud (free tier)**: Gemini Flash, OpenRouter free models, NVIDIA NIM
- **Cloud (paid)**: Claude, OpenAI, Custom APIs

Engines have priority-based failover — if one fails, the next takes over automatically.

## File Formats Supported
PDF, DOCX, PPTX, HTML, TXT, MD, CSV, JSON, YAML — all auto-converted to markdown on upload.

## Web UI Tabs
1. Home — system pulse, quote of the day, stats
2. Web Research — 5-source academic search
3. Upload — drag-and-drop PDF upload
4. Projects — project management
5. Library — browse all extractions
6. Knowledge Graph — multi-dimensional filter
7. Chat — RAG-powered AI chat
8. Manuscripts — view and edit drafts
9. Settings — AI engines, skills, keywords, audit log, etc.

## The Golden Rules
- **Zero Hallucination** — only use content from the user's library
- **Elite Standards** — every paper gets a 12-point deep analysis
- **Local-First** — data never leaves the user's machine
- **Encrypted at Rest** — API keys Fernet-encrypted
