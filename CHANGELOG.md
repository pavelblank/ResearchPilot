# Changelog

## v5.3.1 — GitHub-ready bootstrap, cross-platform setup
**Branch:** `feature/v5.3.1-github-bootstrap` · A user-facing release that fixes the broken-on-fresh-clone bug and adds the cross-platform setup experience. Recommended for `main`.

**Bootstrap fix (critical)**
- `web-app/main.py` — folder creation moved before logger/audit registration
- Fresh GitHub clones no longer crash on first run when `99-SYSTEM-BACKEND/` and `INCOMING/` are absent (those folders hold user-specific data and are gitignored)
- Audit log, server log, `.token`, `.settings_key`, default `settings.json` all auto-create cleanly

**GitHub-ready folder scaffolding** (no personal data, no API keys)
- `01-PROJECTS/00-TEMPLATE/` — blueprint project with README in each of 4 subfolders + a sample `PROJECT-MANIFEST.md` so new users see the project structure
- `99-SYSTEM-BACKEND/{,chats/,plugins/}` — `.gitkeep` files with explanations
- `INCOMING/{,UNREAD-WEB/}` — `.gitkeep` files with explanations
- `.gitignore` updated with selective exceptions — user projects, papers, and personal JSON files remain gitignored

**Setup experience**
- New `SETUP.md` — 10-minute beginner guide for Windows / macOS / Linux
- New `web-app/START-SERVER.sh` — macOS / Linux launcher (auto-installs deps, opens browser)
- New `web-app/install-{windows,mac}.{bat,sh}` — one-time setup wizards
- New `web-app/uninstall-{windows,mac}.{bat,sh}` — clean removal
- `web-app/START-SERVER.bat`, `web-app/REGISTER-AUTOSTART.bat`, `start-research.bat` — rewritten to be self-locating (no more hardcoded install path)
- `web-app/main.py` — `BASE` path auto-detects from `__file__`; `RESEARCHPILOT_HOME` env var override
- `README.md` — self-contained Quick Start (Python install → clone → deps → run, all visible without clicking through)

**Quality**
- `web-app/test_smoke.py` — the discard-list test now self-primes (works on fresh installs)
- 13/13 smoke tests pass on a clean clone

**Branch policy**
- `main` = previous public version (v5.3.0)
- `feature/v5.3.1-*` = work-in-progress; merge to `main` only after review

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
