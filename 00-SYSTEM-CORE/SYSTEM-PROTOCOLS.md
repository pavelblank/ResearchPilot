# ResearchPilot V5.3.3 — System Protocols

These are the standards every AI engine in the system must follow. They are enforced through the `00-SYSTEM-CORE/skills/` markdown files, which are automatically injected into every AI conversation.

## Protocol 1: The 12-Point Elite Extraction

When a paper is extracted (via the Upload tab or `POST /api/extract`), the result is stored in `01-PROJECTS/[Project]/02-EXTRACTIONS/` and must contain all 12 sections:

1. **APA Reference** — full academic citation
2. **DOI** — Digital Object Identifier
3. **Journal Name** — full name
4. **Quartile Ranking** — Q1/Q2 verified via Scopus/SJR
5. **Indexing** — Scopus, Web of Science confirmation
6. **Research Method** — Quantitative, Qualitative, Mixed, or Review
7. **Theoretical Framework** — primary theories used
8. **Exact Relevance** — specific utility for the active project
9. **Section Support** — which chapter or section it informs
10. **Key Contribution** — the "One Big Insight"
11. **Limitations** — critical gaps identified by authors
12. **Classification** — Behaviour, Governance, Technical, or Essential

## Protocol 2: Project Standardization

Every research project is initialized with 4 subfolders (created automatically when you make a new project via Settings → Projects):

1. **01-LIBRARY/** — uploaded PDFs (auto-converted to `.md` on ingest)
2. **02-EXTRACTIONS/** — 12-point analysis for every paper
3. **03-MANUSCRIPTS/** — your drafts and writing
4. **99-META/** — project notes and AI context (helps the AI understand the project)

See `01-PROJECTS/00-TEMPLATE/README.md` for the blueprint.

## Protocol 3: Web Research

When searching for papers, the system queries 5 sources in parallel:

- **OpenAlex** (250M+ works)
- **Crossref** (scholarly publishing metadata)
- **Semantic Scholar** (AI-powered discovery)
- **PubMed** (biomedical literature)
- **Google Scholar** (broad academic search)

Results are deduplicated and filtered against the predatory-journals list (`00-SYSTEM-CORE/predatory_journals.json`, 244+ entries).

## Protocol 4: Data Integrity (Zero Hallucination)

- AI answers must cite specific extractions (e.g., `[P001, 2024]`)
- DOIs are verified before adding to the library
- Inferences are flagged as `[inferred]` vs. `[stated]`
- When evidence is missing, the system says so explicitly — never invents

## Protocol 5: RAG Chat

The chat assistant uses **keyword-scored context retrieval** (no vector DB, no embeddings, no GPU):

- Indexes all `.md` files in projects, extractions, and manuscripts
- Scores by keyword overlap
- Caches results for 45 seconds
- Returns the top matches with file references

This means:

- Works with any AI engine (Ollama, Gemini, Claude, etc.)
- No GPU required
- < 1s latency on most queries
- Fully transparent (you can see which files matched)

## Protocol 6: Security

- API keys are Fernet-encrypted at rest (AES-128-CBC + HMAC-SHA256)
- Master key in `99-SYSTEM-BACKEND/.settings_key` is gitignored
- In-memory rate limiter: 240 req/min/IP, returns 429
- Audit log records sensitive operations (settings save, project delete, file delete, lit-review export)
- Localhost-only binding by default (`127.0.0.1`)

See [SECURITY.md](../SECURITY.md) for the full security policy.

## Protocol 7: Filename Standardization

Every paper artifact (extractions, library PDFs, web imports, summaries, details, any new notes) follows the canonical form:

```
{AuthorLastName}_{Year}[_{note}][_{disambiguator}].{ext}
```

- **Extractions** preserve the P-code prefix used in `[P001, 2024]` citations: `P001_Foshay_2015.md`
- **Library PDFs** use the bare author-year form: `Foshay_2015.pdf`
- **Web imports** (`.md` and `.pdf`) use the same author-year form
- **Note suffix** is optional and only used for disambiguation (`_summary`, `_details`, `_notes`, etc.)
- **Disambiguator** (`_2`, `_3`, ...) is appended only on collision with an existing file

Sanitization rules (applied by `web-app/_filename_utils.py`):
- Apostrophes → underscores (`O'Brien` → `O_Brien`)
- Spaces and other unsafe characters → underscores
- The first author only is kept (`Alyami et al. - 2023.pdf` → `Alyami_2023.pdf`; `Bansal and Axelton - 2024.pdf` → `Bansal_2024.pdf`)
- Maximum name length is 100 characters

The 12-Point prompt (Protocol 1) requires the AI to emit the APA reference as the first line of every extraction, so the filename builder can always recover the canonical name.

A one-shot migration script (`web-app/migrate_filename_format.py`) renames existing legacy files. It is **opt-in** — defaults to dry-run — and writes a full plan to `99-SYSTEM-BACKEND/migration_plan_YYYYMMDD_HHMMSS.json` before any rename. Backups go to `99-SYSTEM-BACKEND/filename_migration_backup/`. Re-run with `--apply` to commit, `--backup` to copy originals first.

---

**Version:** V5.3.3 · **Last Updated:** 2026-06-04
