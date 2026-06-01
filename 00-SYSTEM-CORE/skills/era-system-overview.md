# Skill: ResearchPilot System Overview

The ResearchPilot V5.2 is structured as follows:

## Folder Structure
- **00-SYSTEM-CORE/**: System brain — protocols, knowledge base, researcher profile
- **01-PROJECTS/P1-HEI-CULTURE/**: HEI Cybersecurity Culture study (PhD primary)
- **01-PROJECTS/P2-YEAHIA-BACKBONE/**: Infrastructure & collaboration research
- **01-PROJECTS/00-TEMPLATE/**: Blueprint for new projects
- **INCOMING/**: Landing zone for new PDFs
- **99-SYSTEM-BACKEND/**: System logs, settings, backups, chats
- **web-app/**: FastAPI web server with GUI interface

## Each Project Has:
- **01-LIBRARY/**: Source PDFs and converted markdown
- **02-EXTRACTIONS/**: 12-point deep analysis files
- **03-MANUSCRIPTS/**: Draft writing and outlines
- **99-META/**: Project manifest, reference library, session summaries

## Workflow
1. Drop PDF in INCOMING/
2. Move to project library + convert to .md
3. Run 12-point extraction
4. Update Master Knowledge Base
5. Draft manuscripts using extractions

## AI Engines (priority order)
1. Ollama (local, free)
2. Gemini Flash (free tier)
3. Claude (API)
4. OpenRouter (free models)
