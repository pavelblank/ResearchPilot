# ResearchPilot Universal Search System

> **System-wide search engine for ALL research projects.** Project-specific keywords live in `projects/<ProjectCode>.json` (or in the project's own `99-META/queries/` folder). This engine never changes between projects.

## What This Folder Is

This is the **search engine** that powers web research for every project in `01-PROJECTS/`. It implements a 3-tier NLP-style filter pipeline that:

1. **Tokenizes** text (title/abstract of a candidate paper)
2. **Removes stopwords** (articles, pronouns, prepositions, generic verbs)
3. **Lemmatizes** word forms (`developed` -> `develop`, `behaviors` -> `behaviour`)
4. **Extracts noun phrases** (2-3 word combinations)
5. **Scores** against a project-specific JSON config

The result: a precise **relevance score (0-100+)** and a clear **ACCEPT / REVIEW / REJECT** decision.

## Why This Exists

- Web search for `"cybersecurity"` alone returns 2M+ papers, most irrelevant
- A search for `"cybersecurity readiness" "higher education"` is **slightly better** but still includes technical/network papers
- A search for a **3-word trigram** like `"cybersecurity culture higher education"` returns ONLY papers that are actually about your topic
- This system **enforces** the trigram-anchored search AND auto-rejects papers from the wrong sector (e.g., primary school, K-12, hospital)

## File Map

| File | Purpose | Modified per project? |
|------|---------|------------------------|
| `EXTRACT-KEYWORDS.ps1` | The 8-step NLP pipeline (year → stopwords → punct → numbers → Tier ABC → phrases → score → query). **Purely input-driven**; the `-Project` param is a no-op for extraction. | **NO** - system-wide |
| `KEYWORD-FILTER.ps1` | The 3-tier relevance filter engine (project-driven, legacy) | **NO** - system-wide |
| `PRE-FILTER.ps1` | The INCOMING paper gatekeeper (project-driven, with `-ScoreOnly` for programmatic use) | **NO** - system-wide |
| `SEARCH.ps1` | One-shot wrapper (EXTRACT + QUERY, with project exclusions) | **NO** - system-wide |
| `JOURNAL-QUALITY-FILTER.ps1` | Post-results tier + quality scorer; exposes `Get-JournalQuality`; `-ShowPredatory` toggle | **NO** - system-wide |
| `JOURNAL-TIERS.json` | Tier definitions, publisher patterns, scoring config | **NO** - system-wide |
| `EVALUATE-RESULT.ps1` | Quality-only test harness for one paper's metadata (`-ShowPredatory` opt-in) | **NO** - system-wide |
| `EVALUATE-INCOMING.ps1` | One-shot RELEVANCE + QUALITY for new papers (`-ShowPredatory` opt-in) | **NO** - system-wide |
| `SCORE-AGAINST-INPUT.ps1` | **Project-free** scorer; trigrams/bigrams/singles from user input | **NO** - system-wide |
| `FILTER-PAPERS.ps1` | **Top-level project-free filter** for a folder of papers; supports `-EnableQualityFilter`, `-ShowPredatory`, `-MoveRejects` | **NO** - system-wide |
| `FILTER-PAPERS-README.md` | Quick reference for the project-free flow | **NO** |
| `SEARCH-API.ps1` | Parallel multi-source search (OpenAlex/Crossref/SemanticScholar) with DOI + title dedupe; `-NoParallel` for debug | **NO** - system-wide |
| `JOURNAL-QUARTILES.json` | Q1/Q2/Q3/Q4 quartile lookup + peer-review pattern indicators (word-boundary match) | **NO** - system-wide (extend with field-specific journals) |
| `EXTRA-PREDATORY-TEMPLATE.json` | Template for user-supplied predatory list (extensible JSON array) | **NO** - copy & edit |
| `EXTRA-PREDATORY-README.md` | How to add your own predatory journals/websites | **NO** |
| `SEARCH-STRATEGY.md` | Generic strategy documentation | **NO** |
| `WEB-SEARCH-WORKFLOW.md` | Full 5-phase pipeline (input → keywords → search → filter → quality) + **The Six Filtering Rules** | **NO** |
| `NOUN-PHRASE-INDEX-TEMPLATE.md` | Template for per-project phrase index | **NO** |
| `SEARCH-LOG-TEMPLATE.md` | Template for per-project search log | **NO** |
| `SEARCH-CONFIG-TEMPLATE.json` | Config schema template | **NO** |
| `projects/<ProjectCode>.json` | **Per-project keyword config** (legacy, used by KEYWORD-FILTER/PRE-FILTER) | **YES** - by project owner |
| `projects/DEFAULT.json` | Generic fallback config | Optional |
| `projects/TEST-AIEDU.json` | Test config (delete if not needed) | Optional |
| `test-cases/*.json` | Test fixtures for journal quality filter | Optional |
| `test-cases/*.md` | Test fixtures for FILTER-PAPERS paper-text testing | Optional |

## Quick Start

### Step 1 - Create your project's config

Copy `SEARCH-CONFIG-TEMPLATE.json` to `projects/<YourProjectCode>.json` and fill in:
- `core_constructs.ngrams` (1-3 central multi-word concepts)
- `framework_layers` (optional - L1, L2, L3... with phrase lists)
- `noun_phrases` (flat dictionary: phrase -> weight 1-10)
- `context_anchors.must_have_any` (sector/setting must-appear)
- `context_anchors.must_not_have` (wrong context auto-reject)
- `population_anchors.preferred` (who the study is about)
- `population_anchors.auto_reject_populations` (wrong population)
- `scoring.accept_threshold` / `review_min` / `reject_threshold`

### Step 2 - Run the filter on any candidate paper text

```powershell
.\KEYWORD-FILTER.ps1 `
  -InputText "Paste paper title + abstract here" `
  -Mode analyze `
  -Project "P1-HEI-CULTURE"     # <-- the project code in projects/*.json
```

Output:
```
===== KEYWORD FILTER ANALYSIS =====
 Project:     P1 - P1-HEI-CULTURE
 Config:      ...\projects\P1-HEI-CULTURE.json
--------------------------------------
 AUTO-REJECT: False
 SCORE:       39  (accept>=20, review>=10, reject<5)
 DECISION:    ACCEPT - HIGHLY RELEVANT
```

### Step 3 - Gate-keep papers in INCOMING/

```powershell
# Test a single paper
.\PRE-FILTER.ps1 -FilePath "C:\...\INCOMING\Kizilcec_2024.md" -Project "P1-HEI-CULTURE"

# Test a single paper AND move rejects to a quarantine folder
.\PRE-FILTER.ps1 -FilePath "C:\...\INCOMING\Kizilcec_2024.md" -Project "P1-HEI-CULTURE" -MoveRejects
```

Exit codes for pipeline use:
- `0` = ACCEPT
- `2` = REVIEW MANUALLY
- `1` = REJECT

### Step 4 - Loop over all papers in INCOMING/

```powershell
Get-ChildItem "C:\F- Drive\MYWORK-Research1\INCOMING\*.md" | ForEach-Object {
    & "C:\F- Drive\MYWORK-Research1\00-SYSTEM-CORE\SEARCH-SYSTEM\PRE-FILTER.ps1" `
        -FilePath $_.FullName `
        -Project "P1-HEI-CULTURE"
}
```

### Step 5 - Project-free universal filter (no project config)

For a one-off literature scan where you don't want to set up a project config, use `FILTER-PAPERS.ps1`. Keywords come 100% from your input.

```powershell
# Relevance only
.\FILTER-PAPERS.ps1 -InputText "cybersecurity readiness in higher education" -Folder "C:\papers"

# With journal quality + predatory toggle
.\FILTER-PAPERS.ps1 -InputText "..." -Folder "C:\papers" -EnableQualityFilter -ShowPredatory

# Auto-move rejects and log to CSV
.\FILTER-PAPERS.ps1 -InputText "..." -Folder "C:\papers" -MoveRejects -OutputCsv "results.csv"
```

**Metadata for `-EnableQualityFilter`** is read from each paper's YAML frontmatter (preferred) or from inline `**Journal:** ...` lines. Example frontmatter:

```yaml
---
Journal: Computers & Education
Publisher: Elsevier
Year: 2023
Citations: 142
DOI: 10.1016/j.compedu.2023.104990
OpenAccess: true
InDoaj: false
Preprint: false
---
```

See `FILTER-PAPERS-README.md` for the full reference.

## How a Web Search Should Be Built Now

When you call `websearch` or `webfetch`, use this pattern:

```
"<core construct 1>" AND "<context anchor>" AND ("<layer 1 phrase>" OR "<layer 2 phrase>")
```

Example for P1:
```
"cybersecurity readiness" AND "higher education" AND ("organisational culture" OR "cybersecurity culture" OR "policy compliance")
```

Add exclusions:
```
... AND NOT ("primary school" OR "k-12" OR "patient" OR "encryption" OR "firewall")
```

Use 3-word trigrams when possible:
```
"cybersecurity culture higher education"  (very precise)
"cybersecurity readiness university"      (very precise)
```

## See Also

- `WEB-SEARCH-WORKFLOW.md` - Full 5-phase pipeline (input → keywords → search → relevance filter → quality filter)
- `SEARCH-STRATEGY.md` - Detailed strategy documentation
- `SEARCH-CONFIG-TEMPLATE.json` - Full config schema
- `NOUN-PHRASE-INDEX-TEMPLATE.md` - Template for project-specific phrase index
- `SEARCH-LOG-TEMPLATE.md` - Template for tracking searches
- `JOURNAL-TIERS.json` - Tier definitions for the quality filter
- `00-SYSTEM-CORE/predatory_journals.json` - Beall's List blocklist (used by the quality filter)

## When to Add a New Project

When you start a new project (e.g., `P2-HEI-CULTURE` or `CO-NAZMUL-PROJECT`):

1. Copy `SEARCH-CONFIG-TEMPLATE.json` to `projects/<NewCode>.json`
2. Fill in the config
3. Use the same `EXTRACT-KEYWORDS.ps1`, `KEYWORD-FILTER.ps1`, `PRE-FILTER.ps1`, `JOURNAL-QUALITY-FILTER.ps1` and `EVALUATE-INCOMING.ps1` with `-Project "<NewCode>"`
4. Place a copy of the config in `01-PROJECTS/<NewCode>/99-META/queries/` for project-level ownership
5. Build a `NOUN-PHRASE-INDEX.md` and `SEARCH-LOG.md` in the project's queries folder

## Quality Filter Tier Reference

| Tier | Source | Action | Badge |
|------|--------|--------|-------|
| 1 | Trusted publisher (Elsevier, IEEE, Springer, Wiley, etc.) | KEEP | Green: Scopus / WoS Indexed |
| 2 | DOAJ / PMC indexed | KEEP | Teal: DOAJ Open Access |
| 3 | Unverified (no Tier 1/2 match) | REVIEW (never auto-remove) | Amber: Unverified Journal |
| 4 | Beall's List match (244-entry blocklist) | HIDE (allow user override) | Red: Flagged: Possible Predatory |
| Preprint | arXiv, SSRN, bioRxiv, etc. | REVIEW (with grey badge) | Grey: Preprint |

## Quartile + Peer-Review Badges

In addition to the 4 tiers, the quality filter also reports:

- **Quartile (Q1-Q4)** — JCR / Scopus quartile ranking from `JOURNAL-QUARTILES.json`. Word-boundary match, so `"nature"` matches `"Nature"` but not `"Natural Hazards Review"`. Quality-score bonus: Q1=+15, Q2=+10, Q3=+3, Q4=0.
- **Peer-reviewed** — Yes for Tier 1/2 (trusted) journals. No for preprints and working papers. Unknown for unverified Tier 3. Detected by signal patterns in `JOURNAL-QUARTILES.json` (e.g., `journal of`, `review of` = yes; `arxiv`, `ssrn`, `working paper` = no). Quality-score bonus: +5 if yes.

To **add your own Q1-Q4 journals** or change the match logic, edit `JOURNAL-QUARTILES.json` directly. To **add your own predatory list** (in addition to the built-in 244-entry Beall's list), pass `-ExtraPredatoryPath` to any entry-point script. See `EXTRA-PREDATORY-README.md`.
