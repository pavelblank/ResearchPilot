# Changelog

## v5.3.0 — Stability, Performance, Security, UX, Quality, Features
A consolidated release with improvements across all system layers. No breaking changes — fully backward-compatible with v5.2.

**Stability & errors**
- Rotating file logger (`server.log`, 2 MB × 4 backups)
- Global FastAPI exception handler returns clean JSON 500, no stack-trace leakage
- `GET /api/health` endpoint for uptime monitors

**Performance**
- RAG context retrieval cached for 45 s — cold 469 ms → warm 0 ms on repeat queries
- `scan_keywords` skips 7 system dirs (`.obsidian`, `graphify-out`, `.claude`, `__pycache__`, `.git`, `node_modules`, `.vscode`)

**Security**
- API keys already encrypted at rest with Fernet (AES-128-CBC + HMAC-SHA256)
- In-memory rate limiter: 240 req / 60 s per IP, returns 429
- `audit()` helper + dedicated `audit.log` (2 MB × 2) — wired into `settings.save`, `project.delete`, `file.delete`, `lit_review.export`
- Comprehensive `.gitignore` covers all personal paths, log files, debug files, IDE folders

**UX/UI**
- Keyboard shortcuts: `1-9` switch tabs, `/` focus chat, `Esc` close modal (shortcut-only, no visible hint)

**Code quality**
- 13-test smoke suite (`python test_smoke.py`) covers encryption, RAG cache, audit log, rate limiter, health, exception handler, keyword discard rules, Graphify filter

**New features**
- `GET /api/export/lit-review?project=X` — bundle all 12-point extractions into a single downloadable markdown file
- Keyword auto-link on manual re-add: when a previously-discarded keyword is manually restored, the system scans research files and populates the `files` list automatically (so it shows up in Graphify)

## v5.3 — System enhancement, version bump, gitignore hardening
ResearchPilot version bumped to V5.3. Gitignore updated to exclude all research paper files (*.pdf, *.epub, INCOMING/). System files version-synced across all modules.

## v5.2 — Graph overhaul, multi-layer filters, calendar, timezone
Graph edges: keyword (blue dotted) + project (gray dashed) merged into one line per paper pair, color-coded by shared keyword count. Multi-layer filter parser fixed for AND/OR. Context-aware sub-filter dropdowns (year → author shows only authors of that year). Calendar widget, timezone selector, timezone-aware clock. Google Scholar year filter infinite loop fixed.

## v5.1 — Google Scholar integration
Added Google Scholar search via scholarly library (free, no API key). Removed ArXiv (preprints not needed for research). Updated README.

## v5.0 — ArXiv + multi-source search
Added ArXiv, PubMed, CrossRef, OpenAlex, and Semantic Scholar search sources. Graphify knowledge graph engine with node/edge visualization.

## v4.0 — ResearchPilot rename
Renamed system from MRBLANK_RA-Research-Assistant to ResearchPilot. Updated screenshots and documentation.

## v3.0 — Library management
Paper library with metadata extraction, 12-point analysis protocol, library browsing with file viewer.

## v2.0 — Web application
Flask web UI with project management, chat interface, system memory viewer.

## v1.0 — Initial release
Basic research assistant with Obsidian integration and file management.
