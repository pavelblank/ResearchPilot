# Universal Search Strategy - ResearchPilot

> **This is the GENERIC search engine**. Project-specific keywords live in `projects/<ProjectCode>.json`. This file explains the **principles and pipeline** that work for ANY research project.

## The Core Problem
- Searching single keywords (`"cybersecurity"`) returns millions of irrelevant papers
- Search engines treat each word independently unless wrapped in quotes
- **The fix**: anchor every search to a **multi-word noun phrase** that cannot exist in an irrelevant paper

## The 3-Tier Filter Pipeline (engine-agnostic)

### Tier 1 - Stopword & Generic-Word Removal
**KEEP** these POS tags only:
- Nouns (NN, NNS, NNP)
- Adjectives (JJ)
- Main verbs (VB)
- Selective adverbs (RB)

**REMOVE**:
- Articles (`a`, `an`, `the`)
- Pronouns (`it`, `they`, `this`)
- Prepositions (`from`, `in`, `on`, `through`, `between`)
- Auxiliary verbs (`is`, `was`, `have`, `did`)
- Conjunctions (`and`, `or`, `but`)
- Determiners (`any`, `some`, `many`, `each`)
- Generic verbs (`make`, `use`, `show`, `find`, `study`)
- Generic nouns (`paper`, `study`, `framework`, `results`)

### Tier 2 - Lemmatization
Collapse word forms to base form:
```
developed      -> develop
structuring    -> structure
behaviors      -> behaviour  (or behavior -> behavior)
organizational -> organisational
universities   -> university
analyzing      -> analyse
```

The KEYWORD-FILTER.ps1 engine has **default lemmatization** that applies to every project. Project-specific variants go in the config under `lemmatize`.

### Tier 3 - Noun Phrase Extraction (precision layer)
Extract bigrams (2-word) and trigrams (3-word) using POS pattern `(JJ)*(NN|NNS|NNP)+`.

For each project, define:
- **Core constructs** (1-3 central concepts as multi-word phrases)
- **Framework layers** (L1, L2, L3... with phrase lists per layer)
- **Noun phrase dictionary** (flat list with weights)
- **Context anchors** (sector/setting must-have terms)
- **Auto-reject terms** (wrong context signals)
- **Population anchors** (who the study is about)
- **Method anchors** (methodology that boosts relevance)
- **Theory anchors** (theoretical frameworks that boost relevance)

## Search Operator Rules (apply to any web search)

When calling `websearch` / `webfetch` / Scopus / WoS:

1. **ALWAYS wrap multi-word concepts in quotes**:
   - GOOD: `"cybersecurity readiness"`
   - BAD: `cybersecurity readiness`

2. **ALWAYS use `AND` between layers, `OR` within a layer**:
   - `"cybersecurity readiness" AND ("organisational culture" OR "cybersecurity culture") AND "higher education"`

3. **ALWAYS exclude obvious noise with `NOT`**:
   - ... AND NOT ("primary school" OR "k-12" OR "patient" OR "encryption")

4. **PREFER 3-word trigrams** when possible (highest precision):
   - `"cybersecurity culture higher education"` > `"cybersecurity culture"`

5. **YEAR filter is mandatory**:
   - `PUBYEAR > 2019` (Scopus) or `"2020..2026"` (Scholar)

## Scoring Rubric (Universal)

Score each candidate paper 0+. Threshold for inclusion is in the project's config.

| Criterion | Source | Score |
|-----------|--------|-------|
| Title/abstract contains core constructs | `core_constructs.ngrams` | +10 each |
| Noun-phrase dictionary match | `noun_phrases` | +weight each |
| Context anchor matched | `context_anchors.must_have_any` | +3 each |
| Method matches | `method_anchors` | +1 each |
| Theory matches | `theory_anchors` | +1 each |

**Auto-reject** if `context_anchors.must_not_have` or `population_anchors.auto_reject_populations` match.

## Workflow

```
1. Project Owner: Copy SEARCH-CONFIG-TEMPLATE.json
                   to projects/<YourCode>.json (or in your project's 99-META/queries/)
                   Fill in your project's core_constructs, noun_phrases, context_anchors

2. Search Phase:  Use NOUN-PHRASE-INDEX.md (your project's version) to build
                   Boolean search strings. Run them in Scopus, WoS, Google Scholar,
                   or by calling the websearch tool.

3. Pre-Filter:    For each candidate paper, run:
                   .\PRE-FILTER.ps1 -FilePath "paper.md" -Project "YourCode"
                   This tokenizes, removes stopwords, lemmatizes, and scores
                   the paper against your config.

4. Decision:      score >= accept_threshold  -> move to 01-LIBRARY/
                  score >= review_min        -> manual review
                  else                        -> reject (move to _REJECTED/)

5. Extract:       Run the 12-point extraction only on accepted papers.
```

## Failure Recovery (Universal)

If a search returns < 3 relevant papers:
1. **Broaden** by removing the population filter
2. **Run a citation chase** on the 2 most relevant papers found
3. **Check `01-LIBRARY/`** to ensure not a duplicate
4. **Log the failure** in SEARCH-LOG.md

If a search returns > 50 papers (too much noise):
1. **Add another noun phrase anchor** (move from 2-word to 3-word)
2. **Add an exclusion operator**
3. **Filter by journal quality** in Scopus (`SRCTITLE`)

## File Map

| File | Purpose | Owner |
|------|---------|-------|
| `KEYWORD-FILTER.ps1` | The 3-tier filter engine | SYSTEM (don't modify) |
| `PRE-FILTER.ps1` | The INCOMING paper gatekeeper | SYSTEM (don't modify) |
| `SEARCH-STRATEGY.md` | This file - generic strategy | SYSTEM |
| `NOUN-PHRASE-INDEX-TEMPLATE.md` | Template to build per-project phrase index | SYSTEM |
| `SEARCH-LOG-TEMPLATE.md` | Template to log searches | SYSTEM |
| `SEARCH-CONFIG-TEMPLATE.json` | Config schema template | SYSTEM |
| `projects/<ProjectCode>.json` | **Per-project config** | PROJECT OWNER |
| `../../01-PROJECTS/<ProjectCode>/99-META/queries/NOUN-PHRASE-INDEX.md` | Project's filled-in phrase index | PROJECT OWNER |
| `../../01-PROJECTS/<ProjectCode>/99-META/queries/SEARCH-LOG.md` | Project's search log | PROJECT OWNER |
