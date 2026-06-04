# FILTER-PAPERS.ps1 — Quick Reference

The simplest way to filter papers against your search intent. **No project config. No predefined keywords. Just your input.**

## Usage

```powershell
# Filter a folder of papers against a search intent
pwsh FILTER-PAPERS.ps1 `
    -InputText "cybersecurity readiness in higher education considering organisational culture and policy compliance" `
    -Folder "C:\papers\to-review" `
    -OutputCsv "results.csv"

# Auto-move rejected papers to a quarantine folder
pwsh FILTER-PAPERS.ps1 `
    -InputText "AI ethics in education" `
    -Folder "C:\papers\to-review" `
    -OutputCsv "results.csv" `
    -MoveRejects `
    -RejectFolder "C:\papers\_rejected"
```

## What It Does

1. **Extracts** keywords from your input via the 8-step NLP pipeline (no project config).
2. **Scores** each paper in the folder against YOUR extracted keywords:
   - **Trigrams (3-word phrases)** → 4 pts each match (strong signal)
   - **Bigrams (2-word phrases)** → 2 pts each match (medium signal)
   - **Single words** → 1 pt each, capped at 3 total (weak signal)
3. **Decides** ACCEPT / REVIEW / REJECT:
   - ACCEPT HIGHLY: ≥ 2 trigrams matched
   - ACCEPT LIKELY: 1 trigram + score ≥ 6
   - REVIEW: 1 trigram only, or 3+ bigrams, or 1+ bigrams + score ≥ 4
   - REJECT: nothing meaningful matched
4. **Outputs** a CSV log + summary, optionally moves rejected papers.

## Why This Works

- **The keywords come from YOUR input**, not a project config. Type a different topic, get different keywords.
- **Strict matching**: a paper must contain YOUR actual concepts (3-word phrases) to be ACCEPTED. Single-word matches are weak signal only.
- **No project coupling**: works for any research topic — cybersecurity, healthcare, education, anything.

## Output Example

```
[1/3] Extracted keywords from your input:
  PRIMARY (AND-joined):
    "cybersecurity readiness higher education institution" AND "organisational culture policy comply"
  FALLBACK (OR-joined):
    (none)
  READY-TO-PASTE Scopus/WoS query:
    TITLE-ABS-KEY ( "cybersecurity readiness higher education institution" OR "organisational culture policy comply" )

[2/3] Scoring papers...
  (1/3) paper_A.md ...  score=18 -> ACCEPT - HIGHLY RELEVANT
  (2/3) paper_B.md ...  score=8  -> REVIEW MANUALLY
  (3/3) paper_C.md ...  score=2  -> REJECT - LOW RELEVANCE

[3/3] SUMMARY
  ACCEPT: 1  REVIEW: 1  REJECT: 1
```

## Scoring a Single Paper (programmatic)

```powershell
. .\SCORE-AGAINST-INPUT.ps1
$r = Get-PaperScore -InputText "cybersecurity in healthcare" -FilePath "C:\paper.md"
$r.Score       # integer
$r.Decision    # ACCEPT / REVIEW / REJECT
$r.TrigramMatches  # which 3-word phrases matched
$r.BigramMatches   # which 2-word phrases matched
```

## Threshold Tuning

Defaults: ACCEPT ≥ 2 trigrams, REVIEW ≥ 1 trigram or ≥ 3 bigrams, REJECT otherwise.

Override with environment variables:
```powershell
$env:RP_ACCEPT_THRESH = 20
$env:RP_REVIEW_MIN    = 8
$env:RP_REJECT_THRESH = 0
pwsh FILTER-PAPERS.ps1 -InputText "..." -Folder "..."
```
