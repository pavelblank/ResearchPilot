# SYSTEM MANIFEST - PORTABILITY GUIDE
Project Root: /mnt/c/F- Drive/MYWORK-Research1
Owner: MRBLANK
System: AI Research Assistant (MRBLANK_RA) V5.2

## ARCHITECTURE
- INPUT_ZONE/: All new data enters here. Use DOCLING to convert PDFs to .md.
- sub-projects/: Each project is a self-contained unit.
- Library Logic: Reference library is global; summaries are project-specific but cross-linked.

## FOLDER MEANINGS
- /reading/unread: New sources to be analyzed.
- /analysis/cross_reference: Synthesis of multiple papers.
- /writing/outlines: Structural planning before drafting.
- /research/queries: Log of search terms for reproducibility.

## INITIALIZATION TRIGGER
To start: "RA, Initialize [Project Name]"
Action: Load profile.md -> Load global/rules.md -> Load project/SESSION-SUMMARY.md.

## RECOVERY
This system is designed to be AI-agnostic. Any LLM with filesystem access can resume work by reading this manifest.

---

## Metadata
**System**: AI Research Assistant (MRBLANK_RA) V5.2
**Copyright**: 2026 Mr. Blank Research. All rights reserved.
