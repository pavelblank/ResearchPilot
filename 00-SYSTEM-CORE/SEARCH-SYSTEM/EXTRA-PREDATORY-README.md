# EXTRA-PREDATORY-TEMPLATE.json

User-supplied predatory journals / websites to ADD to the built-in Beall's List.

## What this does

The built-in `00-SYSTEM-CORE/predatory_journals.json` (244 entries from Beall's List) is always loaded. Pass a JSON array of additional entries via the `-ExtraPredatoryPath` parameter to extend the blocklist for your discipline.

## How it works

- Match is **case-insensitive substring**: `"international journal of advanced"` matches `"International Journal of Advanced Research in Computer Science"`.
- Entries can be **journal name fragments** (e.g., `"global journal of engineering"`) or **domains** (e.g., `"academia.edu"`, `"researchgate.net"`).
- Tier 4 (predatory) is still **HIDDEN by default**. Use `-ShowPredatory` to expose them with a red "Flagged: Possible Predatory" badge.

## Usage

```powershell
# 1. Copy the template
Copy-Item EXTRA-PREDATORY-TEMPLATE.json my-predatory-list.json

# 2. Edit my-predatory-list.json - add/remove entries as needed

# 3. Pass it to any entry point
.\EVALUATE-RESULT.ps1 -PaperFile paper.meta.json -ExtraPredatoryPath "my-predatory-list.json"
.\EVALUATE-INCOMING.ps1 -FilePath paper.md -Project P1-HEI-CULTURE -MetadataJson paper.meta.json -ExtraPredatoryPath "my-predatory-list.json"
.\FILTER-PAPERS.ps1 -InputText "..." -Folder "C:\papers" -EnableQualityFilter -ExtraPredatoryPath "my-predatory-list.json"
```

## File format

A flat JSON array of strings. NO comments, NO metadata — just strings.

```json
[
  "international journal of advanced engineering research",
  "iosrjournals.org",
  "academia.edu"
]
```

## When to use it

- Your discipline has a known **blacklist beyond Beall's** (e.g., conference proceedings your field considers predatory)
- You want to flag specific **domains** you don't trust (preprint archives, paper mills, etc.)
- You're working in a region-specific context where local predatory venues aren't in Beall's
