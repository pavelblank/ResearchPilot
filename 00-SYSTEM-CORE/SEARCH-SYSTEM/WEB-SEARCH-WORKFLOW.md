# WEB-SEARCH-WORKFLOW.md
# ResearchPilot Universal Web Research Workflow
# The complete flow from USER INPUT -> EXTRACTED KEYWORDS -> SEARCH QUERY -> FILTER

> **The user's input is the source of truth.** Every keyword used in a search is **derived from the input** through the NLP pipeline, not invented or pulled from a project config. The project config is only used AFTER the search to score the results.

## Architectural Rule (CRITICAL)

The system has TWO completely separate stages, each with its own purpose:

| Stage | Script | Uses project config? | Purpose |
|-------|--------|----------------------|---------|
| **EXTRACTION** (search) | `EXTRACT-KEYWORDS.ps1` | **NO** — purely input-driven | Build the search query from user input |
| **SCORING** (filter) | `KEYWORD-FILTER.ps1`, `PRE-FILTER.ps1` | **YES** | Score results against project's known keywords |

**The `-Project` parameter is a no-op in `EXTRACT-KEYWORDS.ps1`.** It is accepted only for script-signature consistency. Pass `-Project P1-HEI-CULTURE` or `-Project DEFAULT` and the extraction is identical.

The only place the project config affects the search output is in `SEARCH.ps1` when building the Scopus exclusion block (`AND NOT TITLE-ABS-KEY ( "primary school" OR "k-12" ... )`). Those are quality filters, not keywords.

---

## The Problem We Solve

User says: `"find papers on cybersecurity readiness in higher education considering mental models of privacy and organisational culture"`

The wrong way:
- Take "cybersecurity" and search for it → 2M+ results, 99% noise
- Take "higher education" and search for it → 5M+ results, mostly irrelevant
- Hard-code a list of keywords from a project config → doesn't adapt to NEW inputs

The right way:
1. **Parse the input** to find what the user is ACTUALLY looking for
2. **Extract noun phrases** from the input (the 2-3 word combinations that capture the concept)
3. **Build a search query** from those noun phrases
4. **Execute the search**
5. **Filter the results** against the project config (or against the input itself if no project)

---

## The Full Pipeline (5 Phases)

### PHASE 1 - User Input
User types something like:
```
"find papers on cybersecurity readiness in higher education considering 
mental models of privacy and organisational culture with policy compliance 
and governance"
```

This is the raw intent. Do NOT search for it as-is.

### PHASE 2 - NLP Keyword Extraction (run EXTRACT-KEYWORDS.ps1)

The script applies the standard NLP pipeline. **The output is determined 100% by the input text.** The project config is not consulted for tier lists, stopwords, or lemmatization — these would bias the extraction toward the project's pre-known keywords.

```
INPUT:  find papers on cybersecurity readiness in higher education considering 
        mental models of privacy and organisational culture with policy compliance 
        and governance

STEP 1 - TOKENIZE:
  find, papers, on, cybersecurity, readiness, in, higher, education, considering,
  mental, models, of, privacy, and, organisational, culture, with, policy, 
  compliance, and, governance

STEP 2 - REMOVE STOPWORDS:
  (removes: find, papers, on, in, considering, of, and, with)
  kept: cybersecurity, readiness, higher, education, mental, model, privacy,
        organisational, culture, policy, compliance, governance

STEP 3 - KEEP NN, NNP, JJ, VB (heuristic POS):
  cybersecurity (NN), readiness (NN), higher (JJ), education (NN),
  mental (JJ), model (NN), privacy (NN), organisational (JJ), culture (NN),
  policy (NN), compliance (NN), governance (NN)

STEP 4 - LEMMATIZE:
  organisational -> organisational
  compliance     -> comply
  (others stay)

STEP 5 - EXTRACT NOUN-PHRASE BIGRAMS & TRIGRAMS:
  mental model privacy
  privacy organisational culture
  cybersecurity readiness higher
  readiness higher education
  organisational culture policy
  policy comply governance
  ... (top 15 by specificity)

STEP 6 - RANK BY SPECIFICITY:
  Trigrams > Bigrams > Single words
  Longer phrases = more specific = higher rank
```

**Output** (the temporary keywords):
```
- privacy organisational culture
- cybersecurity readiness higher
- readiness higher education
- mental model privacy
- organisational culture policy
- policy comply governance
...
```

### PHASE 3 - Search Query Construction

From the extracted keywords, build a search query in multiple formats:

**For Scopus / Web of Science (Boolean TITLE-ABS-KEY)**:
```
TITLE-ABS-KEY ( 
  "mental model privacy" 
  OR "cybersecurity readiness higher" 
  OR "organisational culture policy" 
  OR "readiness higher education" 
  OR "policy comply governance"
)
```

**For Google Scholar (one quoted phrase per line)**:
```
"mental model privacy"
"cybersecurity readiness higher"
"organisational culture policy"
"readiness higher education"
"policy comply governance"
```

**For the `websearch` tool (use as the query string)**:
```
"mental model privacy" OR "cybersecurity readiness" OR "organisational culture" OR "policy compliance"
```

### PHASE 4 - Execute & Filter

1. **Execute** the search using the query built in Phase 3
2. **For each result**, run the `KEYWORD-FILTER.ps1` against its title + abstract
3. **Apply scoring**:
   - If a `projects/<ProjectCode>.json` exists → score against the project's noun_phrases, core_constructs, context_anchors
   - If no project config → score the result against the **extracted input keywords** (do they match the original input?)
4. **Decision**:
   - score >= accept_threshold → ACCEPT, move to `01-LIBRARY/`
   - score in [review_min, accept_threshold) → REVIEW MANUALLY
   - score < reject_threshold OR matches `must_not_have` → REJECT

### PHASE 5 - Journal Quality Scoring (post-filter)

A relevant paper can still be **predatory** or **low quality**. The journal quality layer catches this AFTER relevance scoring.

1. **Inputs** for each candidate paper: `journalName`, `publisher`, `doi`, `citationCount`, `year`, `isOpenAccess`, `isInDoaj`, `isPreprint`, `source` (URL).
2. **Tier classification** (highest priority first):
   - **Tier 4 - Predatory** if journal name matches an entry in `00-SYSTEM-CORE/predatory_journals.json` (Beall's List)
   - **Preprint flag** if source is arXiv, SSRN, bioRxiv, medRxiv, ResearchSquare, or Preprints.org
   - **Tier 1 - Trusted** if publisher matches a known index (Elsevier, Springer, Wiley, IEEE, ACM, SAGE, Oxford, Cambridge, Nature, etc.)
   - **Tier 2 - DOAJ** if `isInDoaj = true` (from OpenAlex) or source is `doaj.org`
   - **Tier 3 - Unverified** if none of the above (NEVER auto-removed, shown with amber warning)
3. **Quality score** is added to the relevance score:
   - Citation bonus: 0=0pts, 1-10=2pts, 11-50=5pts, 51-200=8pts, 201-500=12pts, 500+=15pts
   - Tier bonus: Tier 1=+20, Tier 2=+10, Tier 3=0, Tier 4=-50
   - Open access bonus: +5
   - Recency bonus: last 2y=+3, 2-5y=+5, 5-10y=+2, 10y+=0
4. **Badges** for UI display:
   - **Green** = Scopus / WoS Indexed
   - **Teal** = DOAJ Open Access
   - **Amber** = Unverified Journal
   - **Red** = Flagged: Possible Predatory
   - **Blue** = Open Access PDF
   - **Grey** = Preprint
5. **Final verdict**:
   - Tier 4 (predatory) → REJECT regardless of relevance
   - Tier 3 with negative quality → REVIEW even if relevance says ACCEPT
   - Tier 1 with borderline relevance (5-19) → upgrade to ACCEPT (high quality rescue)
   - Otherwise follow the relevance decision

**Command**:
```powershell
# Single paper (provide metadata)
.\EVALUATE-INCOMING.ps1 -FilePath "..\..\INCOMING\paper.md" -Project "P1-HEI-CULTURE" -MetadataJson "paper.meta.json"

# Single paper (relevance only, no metadata)
.\PRE-FILTER.ps1 -FilePath "..\..\INCOMING\paper.md" -Project "P1-HEI-CULTURE"

# Single paper (quality only, batch mode)
.\EVALUATE-RESULT.ps1 -PaperFile "paper.meta.json"
```

---

## The Five-Command Workflow

The user can run any of these. Each one runs the appropriate part of the pipeline.

### Command 1 - Just extract keywords from input
```powershell
.\EXTRACT-KEYWORDS.ps1 -InputText "your search intent here" -Mode keywords
```
Output: ranked list of noun phrases ready to be used as search anchors.

### Command 2 - Get a ready-to-paste Scopus query
```powershell
$q = .\EXTRACT-KEYWORDS.ps1 -InputText "your search intent" -Mode query -Project "P1-HEI-CULTURE"
# Then paste $q into Scopus TITLE-ABS-KEY field
```

### Command 3 - Get one quoted phrase per line for Google Scholar
```powershell
.\EXTRACT-KEYWORDS.ps1 -InputText "your search intent" -Mode scholar -Project "P1-HEI-CULTURE"
```

### Command 4 - Filter a single candidate paper
```powershell
.\PRE-FILTER.ps1 -FilePath "paper.md" -Project "P1-HEI-CULTURE"
```

### Command 5 - The one-shot full flow (EXTRACT + QUERY)
```powershell
.\SEARCH.ps1 -InputText "find papers on cybersecurity readiness in higher education considering mental models" -Project "P1-HEI-CULTURE" -OutputFormat "all"
```

### Command 6 - Full evaluation of a new paper (RELEVANCE + QUALITY)
```powershell
.\EVALUATE-INCOMING.ps1 -FilePath "..\..\INCOMING\paper.md" -Project "P1-HEI-CULTURE" -MetadataJson "paper.meta.json" [-ShowPredatory]
```
Runs PRE-FILTER for relevance, then JOURNAL-QUALITY-FILTER for quality, then combines into a final verdict. Exits 0 (ACCEPT), 1 (REJECT), or 2 (REVIEW). Pass `-ShowPredatory` to expose Tier 4 papers with a red badge instead of silently rejecting them.

### Command 7 - Journal quality only (batch)
```powershell
Get-ChildItem ..\..\INCOMING\*.meta.json | ForEach-Object {
    .\EVALUATE-RESULT.ps1 -PaperFile $_.FullName [-ShowPredatory]
}
```
Use this when you already have metadata JSON files for a batch of candidate papers and only need the quality tier assignment.

### Command 8 - Project-free universal filter (FOLDER + INPUT)
```powershell
# Relevance only
.\FILTER-PAPERS.ps1 -InputText "cybersecurity readiness in higher education" -Folder "C:\papers"

# With journal-quality + predatory toggle
.\FILTER-PAPERS.ps1 -InputText "..." -Folder "C:\papers" -EnableQualityFilter -ShowPredatory

# Auto-move rejects to a subfolder
.\FILTER-PAPERS.ps1 -InputText "..." -Folder "C:\papers" -MoveRejects -RejectFolder "C:\papers\_rejected"

# Log to CSV
.\FILTER-PAPERS.ps1 -InputText "..." -Folder "C:\papers" -OutputCsv "results.csv"
```
The top-level project-free filter. No project config is consulted. The extracted keywords from the user's input ARE the scoring vocabulary. Reads YAML frontmatter or inline `**Journal:** ...` lines from each `.md` for quality tiering. `-EnableQualityFilter` and `-ShowPredatory` are both opt-in.

### Command 9 - Parallel multi-source web search
```powershell
.\SEARCH-API.ps1 -Query "cybersecurity behaviour higher education" -MaxResults 50 [-NoParallel]
```
Calls OpenAlex, Crossref, and Semantic Scholar **in parallel** via `Start-Job`, dedupes by DOI then title similarity (Jaccard 0.85), and returns a unified JSON array. Pass `-NoParallel` to run sequentially (debug mode).

---

## Key Principle: **EVERY search uses keywords derived from the user's input**

The system NEVER:
- Pulls a hardcoded keyword list from a project config and uses it as the search query
- Invents keywords that weren't in the input
- Uses single words as search anchors (always wraps in quotes for multi-word phrases)

The system ALWAYS:
- Runs the NLP pipeline (tokenize -> stopword -> POS -> lemma -> noun-phrase)
- Outputs the highest-specificity phrases as the search anchor
- Lets the user inspect, refine, and re-run

---

## The Six Filtering Rules

These rules govern the extraction, scoring, and filtering layers. They are **non-negotiable** and supersede any project-level settings.

### Rule 1 - CLEANING (input normalization)

When parsing the user's input, do **not** over-normalize.

- **KEEP loose numbers** as separate tokens. A year like `2024`, `2025`, `2026` is a meaningful filter, not noise.
- **KEEP loosely written symbols**: hyphens in compound words (`policy-compliance`, `higher-education`), em-dashes, slashes, and parentheses around year ranges stay intact.
- **DO NOT** strip punctuation that has meaning, including hyphens in concepts like `cybersecurity-readiness`.
- **Stopwords include academic filler verbs** in addition to standard function words. Recognise and remove: `emerge`, `appear`, `arise`, `imply`, `reveal`, `highlight`, `emphasize`, `note`, `argue`, `claim`, `state`, `demonstrate`, `propose`, `illustrate`, `observe`, `outline`, `report`, `mention`, `refer`, `cite`, `acknowledge`, `conclude`, `summarize`, `assess`, `evaluate`, `interpret`, `identify`, `establish`, `determine`, `contribute`, `offer`. These verbs are noise in search anchors; the *noun phrases they surround* are what matter.
- Past-participle forms of these verbs are also stopwords (`emerged`, `appeared`, `demonstrated`, `proposed`, `identified`, `reported`, `mentioned`, `concluded`, etc.).

### Rule 2 - CLASSIFICATION (Tier A / B / C)

Every kept token is assigned a tier:

| Tier | Definition | Example from input `cybersecurity readiness in higher education considering mental models` |
|------|------------|------|
| **A - Definitive anchor** | Nouns / noun phrases that directly define the topic. These are the search anchors. | `cybersecurity`, `readiness`, `higher education`, `cybersecurity readiness` |
| **B - Likely anchor** | Adjectives / supporting nouns. Useful as FALLBACK search terms, not the primary. | `mental`, `models`, `mental models` |
| **C - Noise / filler** | Academic filler verbs, generic words, function words, broad category names. Drop them from the query. | `considering`, `find`, `papers`, `study` |

- Single words alone are **Tier B or C** — never the primary search anchor.
- The PRIMARY query must be **multi-word noun phrases** (bigrams/trigrams) from Tier A.
- Tier B phrases appear in the FALLBACK query only.

### Rule 3 - PHRASE BUILDING (greedy 5-word merge)

After cleaning and classification, **build phrases by greedily merging adjacent kept tokens**:

1. **Length order**: try 5-word phrases first, then 4, then 3, then 2.
2. **Adjacency only**: phrases are formed from **consecutive kept tokens**. A removed (stopword) token between two kept tokens **breaks the phrase** — never bridge a gap.
3. **Prefer longer**: if a 5-word phrase is valid, do not also emit its 4-word / 3-word sub-phrases as separate items.
4. **Tier B single words are FALLBACK only**: they appear as `OR` in the FALLBACK query, never in PRIMARY.
5. **No anchoring by Tier B**: a Tier B phrase alone is not a valid PRIMARY anchor. The PRIMARY query must contain at least one Tier A phrase as its anchor.

Example:
```
Input:   "cybersecurity readiness in higher education considering mental models of privacy"
Tokens:  cybersecurity, readiness, [STOP: in], higher, education, [STOP: considering], mental, models, [STOP: of], privacy
Phrase 5: not enough kept tokens
Phrase 4: not enough kept tokens
Phrase 3: "cybersecurity readiness higher" — INVALID (gap: "in" was removed between readiness and higher)
Phrase 2: "cybersecurity readiness", "higher education", "mental models"
Phrase 1: (all)
PRIMARY: "cybersecurity readiness" AND "higher education"
FALLBACK: mental models OR privacy
```

### Rule 4 - PREDATORY FILTER (Tier 4 toggle)

- Beall's-list journal matches (244 entries in `00-SYSTEM-CORE/predatory_journals.json`) are classified as **Tier 4 - Predatory**.
- **Default behaviour**: Tier 4 papers are **HIDDEN** from the final output regardless of relevance score. They get a `-50` tier bonus that drags the final score deep negative.
- **`-ShowPredatory` switch**: pass this on `JOURNAL-QUALITY-FILTER.ps1`, `EVALUATE-RESULT.ps1`, `EVALUATE-INCOMING.ps1`, or `FILTER-PAPERS.ps1` to expose Tier 4 papers with a red "Flagged: Possible Predatory" badge for manual inspection.
- The toggle is exposed at every entry point that calls the quality filter; the engine never silently drops a paper the user explicitly asked to see.

### Rule 5 - YEAR FILTER (separate param, not in query)

- The publication year is **never part of the search query string**. It is a separate `YEAR` (or `FromYear`/`ToYear`) parameter sent alongside the query.
- Reason: a year in the query string gets matched against the paper text, not its metadata, and produces false positives (`"2024"` in the body, `"2024"` in the references, etc.).
- The year is applied **after** results come back: filter `result.publication_year` against the user-specified range.
- If the user does not specify a year, the system defaults to **last 5 years** (recency preference) but does not silently extend older than that without explicit consent.
- Year tokens in the input are still extracted and stored (`LooseNumbers`) for the user to see, but never injected into the query.

### Rule 6 - SEARCH SPEED (parallel + dedupe)

- All three source APIs (OpenAlex, Crossref, Semantic Scholar) are called **in parallel** using `Start-Job` (PowerShell 5.1 compatible; `ForEach-Object -Parallel` from PS 7+ would also work but is not portable).
- **Dedupe priority**:
  1. **DOI exact match** (case-insensitive, strip `https://doi.org/` prefix). Two records with the same DOI are the same paper.
  2. **Title similarity** using Jaccard index on lowercased word sets. Threshold: **0.85**. Below 0.85, treat as distinct.
- Per-call timeout: **15 seconds**. Failed calls (timeout, 4xx, 5xx) are logged and skipped; the other sources still return results.
- Default per-source page size: **25**. Total target: 50–100 unique papers per query before the relevance/quality layers run.

---

## Why This Beats Project-Config-Only Search

| Approach | What happens | Result |
|----------|--------------|--------|
| Project config keywords only | Search uses P1's preset "cybersecurity readiness", "cybersecurity culture", etc. | Misses project-specific terms the user typed; ignores new angles |
| Input extraction only (no project) | Search uses whatever noun phrases are in the input | Adapts to any topic, but doesn't leverage the project's known keywords |
| **Both (this system)** | Extract from input, **then** enrich with project nouns during **scoring** | Adapts to any input AND leverages the project's known relevant phrases |

**The two stages serve different purposes:**
- **Search stage** = input-driven (finds papers matching what the user is currently asking about)
- **Scoring stage** = project-driven (decides if a found paper is worth keeping for the project)

This means: if the user asks about a new angle (e.g., "cybersecurity fatigue" wasn't in the original project config), the system can still FIND those papers (via input extraction) and the SCORER will accept them if they mention other P1 concepts.

---

## Worked Example (P1)

**User input**:
> "find papers on the role of security fatigue in academic staff's compliance with cybersecurity policy in universities"

**Phase 1 - Input parsed**: 14 words
**Phase 2 - Stopwords removed**: role, security, fatigue, academic, staff, compliance, cybersecurity, policy, universities
**Phase 2 - Lemmatized**: staff (kept), compliance -> comply, universities -> university
**Phase 2 - POS tagged**: role (NN), security (NN), fatigue (NN), academic (JJ), staff (NN), comply (NN), cybersecurity (NN), policy (NN), university (NN)
**Phase 2 - Bigrams**: security fatigue, fatigue academic, academic staff, staff comply, comply cybersecurity, cybersecurity policy, policy university
**Phase 2 - Trigrams**: security fatigue academic, fatigue academic staff, staff comply cybersecurity, comply cybersecurity policy, cybersecurity policy university
**Phase 2 - Ranked top 5**:
1. `security fatigue academic` (trigram, high specificity)
2. `cybersecurity policy university` (trigram, high specificity)
3. `fatigue academic staff` (trigram)
4. `staff comply cybersecurity` (trigram)
5. `security fatigue` (bigram)

**Phase 3 - Scopus query**:
```
TITLE-ABS-KEY ( 
  "security fatigue academic" 
  OR "cybersecurity policy university" 
  OR "fatigue academic staff" 
  OR "security fatigue" 
  OR "cybersecurity policy"
) 
AND NOT TITLE-ABS-KEY ( "primary school" OR "k-12" OR "patient" )
```

**Phase 4 - Search & Filter**:
- Run the query in Scopus
- For each result, run `PRE-FILTER.ps1 -Project "P1-HEI-CULTURE"`
- Papers with score >= 20 go to `01-PROJECTS/P1-HEI-CULTURE/01-LIBRARY/`
- Papers with score in [10, 20] need human review
- Papers with score < 5 (or matching must_not_have) are rejected

---

## What If the Input Is Too Vague?

If the user types: `"papers on AI"`, the extracted keywords will be:
- `ai` (single word, low specificity)
- Not enough to build a strong query

**Solution**: prompt the user for more context, or auto-suggest expansions based on:
1. The project's `core_constructs` (if a project is specified)
2. Common patterns from the project's noun_phrases dictionary

```powershell
# Auto-suggest expansion
.\SEARCH.ps1 -InputText "papers on AI" -Project "P1-HEI-CULTURE" -SuggestExpansions
```

Output might be:
```
Your input is too short. Suggested expansions based on project P1:
  - "cybersecurity readiness" "AI"
  - "AI" "higher education"
  - "AI" "cybersecurity governance"
```

The user picks one, and the system uses it as the new input.

---

## See Also

- `EXTRACT-KEYWORDS.ps1` - The 8-step NLP pipeline (purely input-driven)
- `KEYWORD-FILTER.ps1` - The 3-tier relevance scoring engine (project-driven, legacy)
- `PRE-FILTER.ps1` - The INCOMING paper gatekeeper (project-driven, with `-ScoreOnly`)
- `SEARCH.ps1` - One-shot wrapper for EXTRACT + QUERY (with project exclusions)
- `EVALUATE-INCOMING.ps1` - One-shot RELEVANCE + QUALITY for new papers (with `-ShowPredatory`)
- `EVALUATE-RESULT.ps1` - Quality filter for a single metadata JSON (with `-ShowPredatory`)
- `JOURNAL-QUALITY-FILTER.ps1` - Tier + quality scorer (with `-ShowPredatory` switch)
- `JOURNAL-TIERS.json` - Tier definitions and publisher patterns
- `SCORE-AGAINST-INPUT.ps1` - **Project-free** scorer; uses trigrams/bigrams/singles from user input
- `FILTER-PAPERS.ps1` - **Top-level project-free filter** for a folder of papers (with `-EnableQualityFilter`, `-ShowPredatory`, `-MoveRejects`)
- `FILTER-PAPERS-README.md` - Quick reference for the project-free flow
- `SEARCH-API.ps1` - Parallel multi-source search (OpenAlex/Crossref/SemanticScholar) with DOI + title dedupe
- `predatory_journals.json` (in `00-SYSTEM-CORE/`) - Beall's List blocklist
- `JOURNAL-QUARTILES.json` - Q1/Q2/Q3/Q4 lookup + peer-review pattern indicators (word-boundary match)
- `EXTRA-PREDATORY-TEMPLATE.json` + `EXTRA-PREDATORY-README.md` - User-supplied predatory list (passed via `-ExtraPredatoryPath`)
- `SEARCH-STRATEGY.md` - Generic strategy
- `SEARCH-CONFIG-TEMPLATE.json` - Project config schema
- `README.md` - Folder overview
