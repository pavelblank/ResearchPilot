# ResearchPilot — Web System

## Access
Open any browser on your computer:
- **This PC**: http://localhost:8000

---

## Start the Server

**Double-click**: `START-SERVER.bat`

Or from terminal:
```
cd web-app
python main.py
```

## Auto-Start at Login
Run `REGISTER-AUTOSTART.bat` once (as admin) to make the system start automatically every time Windows boots.

---

## AI Engine Setup

The system auto-switches:
1. **Ollama (local, free)** — install from https://ollama.com then run `ollama pull llama3`
2. **Gemini API (cloud)** — get free key at https://aistudio.google.com/app/apikey

### To set Gemini key:
1. Copy `.env.example` → `.env`
2. Uncomment and paste your key: `GEMINI_API_KEY=your_key_here`
3. Restart server

---

## Folder Map
```
web-app/
  main.py            ← FastAPI backend
  static/index.html  ← Full web UI
  START-SERVER.bat   ← Launch script
  REGISTER-AUTOSTART.bat ← Auto-start setup
  .env               ← Your API keys (create from .env.example)
  requirements.txt   ← Python deps

99-SYSTEM-BACKEND/
  chats/             ← All chat sessions (.md) — add to Obsidian vault
```

## Obsidian Integration
Vault the entire ResearchPilot folder in Obsidian.
All chats saved to `99-SYSTEM-BACKEND/chats/` as `.md` files.
Full memory, searchable, linked — no forgetting.

---

## Feature Checklist
- [x] PDF upload → project library
- [x] 12-point AI extraction per paper
- [x] AI chat (scoped to project + PDF context)
- [x] Chat history saved as Obsidian-compatible `.md`
- [x] Library browser with search
- [x] Extraction viewer
- [x] Master Knowledge Base viewer
- [x] Dashboard with live stats
- [x] Auto AI engine switching (Ollama → Gemini)
