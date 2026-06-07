# ResearchPilot — Help & FAQ

> This file is the canonical knowledge base for the **Help bot** (the floating **?** button).
> The Help bot is **view-only** — it never edits, creates, or deletes files. It only guides you.
> Every `### heading` is a question. The paragraph below it is the answer.

---

## 💡 Identity & Basics

### What is ResearchPilot?
ResearchPilot is a self-hosted AI research workspace for academics and PhD students. You drop papers in, the AI extracts key findings, you search across 5 academic databases, visualise a knowledge graph, and write with RAG-powered chat. Everything stays on your own machine as plain Markdown files.

### What can the Help bot do?
I can guide you around any part of the ResearchPilot app — tabs, settings, workflows, and common problems. I am read-only and cannot create, move, or delete files. For research questions about your own papers, use the **Chat** tab.

### Who built ResearchPilot?
ResearchPilot was designed and developed by Md Yeahia Bhuiyan, a PhD researcher and educator specialising in cybersecurity behaviour and AI-assisted academic workflows. It was built entirely using AI coding agents (OpenCode + Claude).

### What day is today? What time is it?
Open the **Dashboard** tab. There is a live calendar and clock widget at the top left of the page.

### Is my data private?
Yes. Everything is stored locally on your machine as Markdown files. Nothing is sent to any server unless you connect your own AI engine (API key). Your keys are encrypted at rest using AES-128.

### Where are my API keys stored?
Your keys are stored in `99-SYSTEM-BACKEND/settings.json`, encrypted with Fernet (AES-128-CBC + HMAC-SHA256). The encryption key never leaves your machine and is never uploaded anywhere.

### Can I use ResearchPilot offline?
The web app runs locally. AI engines need internet unless you use local Ollama. Everything else — uploads, library, graph, memory — works fully offline.

### What version is this?
Open **Settings → Version Details** to see the full version history with dates and descriptions.

### Where is the source code / GitHub repo?
The official repository is at https://github.com/pavelblank/ResearchPilot. You can fork it, report issues, or read the full README there.

### Can I contribute or fork the project?
Yes. The project is MIT OR Apache-2.0 licensed. Fork it, star it, or extend it freely. See the README for contribution guidelines.

---

## 🚀 Getting Started

### How do I get started with ResearchPilot?
Three steps: 1. Open **Settings → AI Engines** and add at least one API key. 2. Use the **Upload** tab to drop in a PDF or DOCX. 3. Open **Chat** and ask the AI about your paper. That is the core loop.

### How do I set up my first AI engine?
Open **Settings**, then click **AI Engines** in the left sidebar. Pick the engine type (Claude API, OpenAI, Gemini, Ollama, OpenRouter, or Custom). Paste your API key and click **Save AI Settings**.

### How do I add Claude as my AI engine?
In **Settings → AI Engines**, choose **Claude API**. Get your key from https://console.anthropic.com. Paste it and save. Claude is best for long-context academic analysis.

### How do I add OpenAI or GPT-4?
In **Settings → AI Engines**, choose **OpenAI Compatible**. Get your key from https://platform.openai.com/api-keys. Works with GPT-4o, GPT-4-turbo, and any OpenAI-format endpoint.

### How do I use OpenRouter (free models)?
In **Settings → AI Engines**, choose **OpenAI Compatible**. Set the base URL to `https://openrouter.ai/api/v1` and paste your OpenRouter key. OpenRouter gives access to many free and paid models.

### How do I use Gemini?
In **Settings → AI Engines**, choose **Gemini**. Get your key from https://aistudio.google.com/app/apikey. Gemini Flash has a free tier.

### How do I use Ollama (local, no internet)?
Install Ollama from https://ollama.com, then run `ollama pull llama3` (or any model). In **Settings → AI Engines**, choose **Ollama**. The system connects automatically at `http://localhost:11434`. No API key needed.

### How do I configure a custom AI endpoint?
In **Settings → AI Engines**, choose **Custom API**. Paste your OpenAI-compatible endpoint URL (e.g. from Jan, LM Studio, LocalAI) and optionally a key. Any OpenAI-format API works here.

### What happens if one AI engine fails?
The system automatically fails over to the next enabled engine in priority order. If Claude is down, it tries OpenAI, then Gemini, then Ollama, and so on. Your AI never stops completely.

### How do I create a new project?
Open the **Projects** tab, then click **+ New Project**. Use the ID format `P1-NAME` (e.g. `P1-CYBERSEC`, `P2-PRIVACY`). Set a focus and goals — the AI uses these when answering questions about that project.

---

## 🏠 Dashboard

### What is on the Dashboard?
The Dashboard shows: a live calendar + clock, a motivational quote, system stats (papers, projects, engines), quick notes, a countdown timer, and four System Pulse icons linking to the main tabs.

### What are the four System Pulse icons?
The four icons link to: **Upload** (add papers), **Chat** (AI conversation), **Web Research** (search databases), and **Knowledge Graph** (visualise your library). Click any to open that tab.

### What is the System Pulse?
The System Pulse is an animated live graph on the Dashboard that displays your system activity and health. It also shows your paper count, project count, and active AI engines at a glance.

### How do I use Quick Notes on the Dashboard?
Click the notes widget on the left sidebar of the Dashboard. Type anything — meeting notes, reminders, ideas. Notes auto-save as you type and persist across sessions.

### How do I use the countdown timer?
Click the timer widget on the Dashboard sidebar. Set a duration and click Start. Useful for Pomodoro-style work sessions or tracking time on a task.

---

## 💬 Chat Tab

### What can I do in the Chat tab?
Chat lets you talk to the AI about your research. Ask it to analyse papers, write literature reviews, compare findings, extract themes, or draft text. The AI uses your project files as context automatically.

### How do I focus the chat on a specific project?
In the Chat toolbar, open the **Project** dropdown and select a project. The AI will use that project's files as its knowledge context when answering.

### How do I focus the chat on one specific file?
In the Chat toolbar, open the **File** dropdown and pick a file. The AI reads that file and answers based only on its content.

### Does the chat save automatically?
Yes. Every session is auto-saved as a Markdown file in `99-SYSTEM-BACKEND/chats/`. Click **Save** in the toolbar to save manually and start a fresh session.

### How do I use skills in chat?
Type `/skillname` in your message (e.g. `/extract`, `/review`, `/summarize`). The AI loads that skill's instructions and applies them to your question. See **Settings → Skills** to view or add skills.

### What is RAG in the chat?
RAG (Retrieval-Augmented Generation) means the AI automatically injects relevant content from your research library into every message. No vector database is needed — it uses keyword scoring to find the most relevant files.

### Can the Chat AI create projects or move files for me?
Yes. The main Chat AI can take actions. Ask naturally: "Create a new project called P5-BRAIN" or "Move this paper to P3-EEG". An **Action card** appears and you can **Undo** any action.

### How do I clear the chat?
Click **Clear** or **New Chat** in the Chat toolbar. The current session is saved before clearing if you have unsaved messages.

### How do I use keyboard shortcuts in Chat?
Press `/` from anywhere on the Chat tab to jump focus to the chat input. Press `Esc` to close any open modal.

### What is the context size setting?
In **Settings → General**, you can set how many characters of your library the AI loads per message. Larger = more context but slower. Default is suitable for most sessions.

---

## 📤 Upload Tab

### How do I upload a paper?
Open the **Upload** tab. Drag and drop a file onto the drop zone, or click to browse. Choose a destination project (or INCOMING). Click **Upload**.

### What file formats can I upload?
Supported formats: PDF, DOCX, DOC, PPTX, PPT, HTML, TXT, CSV, JSON, MD. All are auto-converted to Markdown after upload.

### What is INCOMING?
INCOMING is a landing folder for new papers you have not yet sorted into a project. Use it when you are not sure which project a paper belongs to yet. Move files out of INCOMING using **Web Research → Imported Papers** or the **Memory** tab.

### Where do uploaded files go?
Files are auto-converted to Markdown and stored in the chosen project's `01-LIBRARY/` folder, or in `INCOMING/UNREAD-WEB/` if you did not specify a project.

### What is auto-conversion?
When you upload a file, the app automatically converts it to Markdown (.md) so the AI can read it. PDFs are parsed using PyMuPDF. DOCX and PPTX are converted using python-docx and python-pptx.

### What is the maximum upload file size?
500 MB per file. Files larger than this are rejected at the upload endpoint.

### Can I upload multiple files at once?
Yes. Select multiple files in the file browser or drag and drop several at once. Each file is processed and converted in sequence.

### What happens after I upload?
The file is converted to Markdown and placed in your chosen folder. If you enabled **Auto-Extract** in Settings → General, the AI immediately runs a 12-point analysis on the paper.

---

## 🔍 Web Research Tab

### How do I search for academic papers online?
Open the **Web Research** tab. Type a detailed query — full sentences work better than one or two keywords. Set a year range, choose sources, pick a sort order, then click **Search**.

### What academic sources are available?
Five sources: **OpenAlex** (250M+ works, always free), **Crossref** (scholarly metadata), **Semantic Scholar** (AI-powered discovery), **PubMed** (biomedical), and **Google Scholar** (experimental). Toggle each on or off before searching.

### Which source should I use?
For general academic work, use **OpenAlex** and **Semantic Scholar** together. For biomedical topics, add **PubMed**. For broader coverage, add **Crossref**. Google Scholar is experimental — results may vary.

### How do I download a paper?
For Open Access (OA) papers, click **Download PDF**. The PDF and a Markdown analysis are saved. For non-OA papers, click **Download .md (12-Point)** — the AI generates a 12-point analysis stub from the abstract.

### What is Open Access?
Open Access papers are freely and legally downloadable. The system detects whether a paper has an open-access PDF link and shows the **Download PDF** button only when one is available.

### How do I move an imported paper into a project?
In **Web Research → Imported Papers**, select a project from the dropdown next to the paper, then click **Move**. The file is moved to that project's `01-LIBRARY/` folder.

### What is the 12-point extraction?
A structured AI analysis of a paper covering: The Problem, The Gap, Research Questions, Purpose, Theory/Framework, Methodology, Key Findings, Contribution, Limitations, Implications, Key Citations, and Critical Position.

### What does "Download .md (12-Point)" mean?
It downloads an analysis-only Markdown file. The AI reads the abstract and metadata to fill in all 12 points of the extraction protocol. No PDF is saved — only the analysis.

### What is predatory journal filtering?
The system checks every search result against a list of known predatory publishers. Papers from those journals are flagged with a warning so you can choose to skip them.

### How does the web research input work?
The system runs an 8-step NLP pipeline on your query: extracts key phrases, removes stop words, generates bigrams and trigrams, scores results against your query, and filters by journal quality tier (Q1–Q4).

---

## 📁 Projects & Library

### What is a project?
A project is a research folder under `01-PROJECTS/` with a clear focus. It contains your papers in `01-LIBRARY/`, 12-point analyses in `02-EXTRACTIONS/`, drafts in `03-MANUSCRIPTS/`, and a project manifest.

### What is the project manifest?
The file `99-META/PROJECT-MANIFEST.md` inside each project. It records the project title, focus, goals, and research questions. The AI uses this when answering project-specific questions.

### What is the folder structure of a project?
Each project has: `01-LIBRARY/` (your papers as .md), `02-EXTRACTIONS/` (12-point analyses), `03-MANUSCRIPTS/` (writing drafts), `99-META/` (manifest and metadata).

### How do I read a paper in the library?
Open the **Library** tab (accessible from the Projects view), pick a project, then click **Read** on any file. A modal opens with the full Markdown content.

### How do I rename a project?
Use the **Projects** tab → find the project → click the rename/edit icon. Or ask the Chat AI: "Rename project P2-OLD to P2-NEW."

### How do I delete a project?
In the **Projects** tab, click the delete icon next to the project. Deleted projects go to **Settings → Trash** where you can restore them for 30 days.

### How many projects can I have?
Unlimited. The system creates folders on disk — there is no cap. Performance stays fast even with dozens of projects.

### What does the P1, P2 naming mean?
It is a convention, not a requirement. `P1-NAME` means Project 1 with that name. Use any prefix you like. Consistent naming (P1, P2, P3) makes sorting and AI context easier.

---

## 🕸️ Knowledge Graph

### What is the knowledge graph?
A visual map of all your research files — papers, extractions, notes, chats — connected by shared keywords, project membership, and references. Built with D3.js, fully interactive.

### What dimensions can I filter by?
Seven dimensions: **Author**, **Year**, **Journal**, **Quartile**, **Method**, **Framework**, and **Keyword**. Combine any of them with AND/OR logic.

### How do I add a filter layer?
Click **+ Add Layer** in the Graph toolbar. Pick a dimension and value. Stack up to 4 layers. All active layers are applied simultaneously.

### What is cluster mode?
Cluster mode groups nodes by a category (Author, Year, Journal, etc.) without filtering them out. Papers cluster around a central category hub. You can mix cluster mode with filter layers.

### How do I refresh the graph?
Click **Refresh** in the Graph tab header. This re-scans all your project files and rebuilds the node/edge network from scratch.

### What are nodes and edges?
Each **node** is a paper, extraction, note, or keyword. **Edges** connect nodes that share keywords, belong to the same project, or reference each other. Thicker edges = stronger connection.

### How do I open a file from the graph?
Click a node. A tooltip appears with the file name and metadata. Click **Open** in the tooltip to read the file in a modal.

### Why is my graph empty?
Click **Refresh**. If still empty, make sure your projects have files in `01-LIBRARY/`. Empty files and folders with no content are ignored by the graph builder.

---

## 🧠 Memory Tab & Settings › Memory

### What is the Memory tab?
Memory shows every `.md` file anywhere in the system — chats, papers, extractions, notes, drafts, across all projects. It is a global file browser, not limited to one project.

### What is the difference between Memory and Library?
**Library** shows only the papers inside one specific project's `01-LIBRARY/` folder. **Memory** shows every `.md` file system-wide, including chats, notes, and drafts from all projects.

### How do I view a file in Memory?
Find the file in the Memory table, then click **👁 Read**. A modal opens with the full content.

### How do I delete a file in Memory?
Click the **🗑 Delete** button next to the file. Deleted files move to **Settings → Trash** and can be restored.

### What files appear in Memory?
All `.md` files the system knows about: papers from INCOMING, extractions, chat logs, notes, drafts, and manifest files.

### What is Settings › Trash?
Trash holds recently deleted files. Files stay here for 30 days. Click **Restore** to bring a file back to its original location. Click **Delete Forever** to permanently remove it.

### What is Settings › Chats?
Chats lists all saved chat sessions (stored as `.md` files in `99-SYSTEM-BACKEND/chats/`). You can read, download, or delete old sessions from here.

---

## ⚙️ Settings — All Sections

### What does Settings › General do?
General controls: timezone, theme (dark/light), context window size for AI, auto-extract on upload toggle, and auto-start server on login.

### How do I change the theme (dark/light)?
Open **Settings → General**. Toggle the **Theme** switch between dark and light. The change applies instantly across the whole app.

### What are AI Engines in Settings?
AI Engines is where you configure every AI backend the system can use: Claude API, OpenAI, Gemini, Ollama, OpenRouter, custom endpoints. Each engine has a priority order — lower number = tried first.

### How many AI engines can I configure?
Unlimited. You can enable as many as you like. The failover router tries them in priority order. Having multiple engines means the AI never goes down completely.

### What are Skills in Settings?
Skills are reusable Markdown instruction files the AI loads when you type `/skillname` in chat. Think of them as saved prompt templates. Add your own in `00-SYSTEM-CORE/skills/` or via **Settings → Skills → + Add Skill**.

### How do I add a custom skill?
In **Settings → Skills**, click **+ Add Skill**. Give it a name and paste the instruction text. Save. Use it in chat by typing `/yourskillname`. The AI applies those instructions to your message.

### What is the Learned Profile (Settings › Learned Profile)?
The Learned Profile is an auto-built cross-project synthesis stored in `00-SYSTEM-CORE/MASTER-KNOWLEDGE-BASE.md`. The AI uses it to give answers that draw on your whole research history, not just one project.

### How do Keywords work?
Keywords are important terms extracted from your `.md` files. Click **Auto-Scan** to refresh them. Add or delete manually — deleted keywords are remembered forever and never re-added automatically.

### What is Settings › Predatory Journals?
A blocklist of known predatory publishers. The system checks every Web Research result against this list and flags matches. Click **Fetch Latest Online** to update the list from a public blocklist source.

### What is Settings › Author?
Your name, institution, email, and ORCID. The system uses this when generating paper metadata, citations, and extraction headers.

### What is Settings › Plugins?
Plugins lets you install third-party AI engine extensions (`.py` files). Drop them into `00-SYSTEM-CORE/plugins/` or use the plugin installer in this section.

### What is Settings › Obsidian?
Click **Open Vault** to launch Obsidian pointed at your entire ResearchPilot folder. The folder is a standard Obsidian vault — your chats, extractions, and notes are all readable and linkable there. Click **Open Graph** to open the Obsidian graph view directly.

### What is Settings › Version Details?
Version Details shows the full version history of ResearchPilot — each release with its date, version number, and a description of what changed. Click any version to expand its notes.

---

## 🧩 Skills & Extraction

### What skills are available by default?
Default skills include `/extract` (12-point paper extraction), `/review` (journal-style critical review), `/summarize` (concise summary), `/academic-writing` (publication-style writing assistant), and `/caveman` (ultra-compressed mode). See **Settings → Skills** for the full list.

### How do I use /extract?
In chat, type `/extract` followed by your question or paste a paper abstract. The AI runs the full 12-point extraction protocol on the content and returns a structured analysis.

### What is the 12-point extraction protocol exactly?
The 12 points are: 1) The Problem, 2) The Gap, 3) Research Questions, 4) Purpose/Objective, 5) Theory/Framework, 6) Methodology, 7) Key Findings, 8) Contribution, 9) Limitations, 10) Implications, 11) Key Citations, 12) Critical Position.

### Can I run auto-extraction on upload?
Yes. Enable **Auto-Extract** in **Settings → General**. Every paper you upload will automatically go through the 12-point extraction after conversion.

### Where are extracted analyses saved?
In the project's `02-EXTRACTIONS/` folder, as a `.md` file with the same name as the source paper.

---

## 🆘 Common Problems

### The AI is not responding / "No engine configured"
Open **Settings → AI Engines**. Enable at least one engine and make sure your API key is saved. If using Ollama, make sure the Ollama app is running locally first.

### My API key is not working
Double-check the key was copied fully (no leading or trailing spaces). Make sure the key is active and has not been revoked. For Claude, keys are at https://console.anthropic.com. For OpenAI, at https://platform.openai.com.

### My project does not show up in the Chat dropdown
The project may be missing from `01-PROJECTS/`. Create it in the **Projects** tab first. Then refresh the Chat page and it will appear in the project dropdown.

### My uploaded file is not in the Library
Check the destination project you selected at upload. Files sent to INCOMING do not appear in any project's Library. Move them via **Web Research → Imported Papers** or the **Memory** tab. Also check the file format is supported (PDF, DOCX, PPTX, TXT, MD, HTML).

### My file failed to convert after upload
The conversion may have failed silently. Check the file is not password-protected or corrupted. Try opening the file yourself to verify it is readable. Re-upload if needed.

### The Knowledge Graph is empty
Click **Refresh** in the Graph toolbar. Make sure your projects have content in `01-LIBRARY/`. Empty files and folders with no `.md` content are ignored.

### The server will not start
Make sure Python 3.10+ is installed. Run `pip install -r requirements.txt` in the `web-app/` folder. Check that port 8000 is not already in use by another process.

### Chat says the context is too long
Reduce the **Context Size** setting in **Settings → General**. Alternatively, use the **File** dropdown in Chat to focus on one file instead of the whole project library.

### How do I export or share my work?
All chats, extractions, and drafts are `.md` files stored locally. Open them in Obsidian, copy them to any Markdown editor, push to Git, or convert to PDF with any Markdown tool.

### How do I export a literature review?
Use the API endpoint `GET /api/export/lit-review?project=P1-NAME`. It bundles all 12-point extractions from that project into a single Markdown file ready for editing.

---

## ⌨️ Keyboard Shortcuts

### What keyboard shortcuts are available?
Keys 1–9 switch between tabs (1 = Dashboard, 2 = Chat, 3 = Web Research, and so on). Press `/` to jump focus to the chat input when on the Chat tab. Press `Esc` to close any open modal.

### How do I jump to the chat input quickly?
Press `/` (forward slash) from anywhere on the Chat tab. Focus moves directly to the message input field.

### How do I close a modal or popup?
Press `Esc`. Any open modal, detail panel, or overlay closes immediately.

---

## 🧭 Navigation

### How do I switch between tabs?
Click any tab in the top navigation bar. Or press the number key matching the tab position (1 = Dashboard, 2 = Chat, 3 = Web Research, etc.).

### How do I navigate inside Settings?
Open **Settings** (last tab in the nav). The left sidebar lists all 13 sections. Click any section name to open it. No page reload needed.

### How do I get back to the Dashboard?
Click the **Dashboard** tab in the top nav, or press `1`.

---

## 📞 Still Stuck?

### How do I ask the Help bot a question?
Click the floating **?** button in the bottom-right corner of any page. Type your question in the chat input and press Enter. I will search the FAQ first and only use the AI if no match is found.

### What if the Help bot does not know the answer?
If I cannot find an answer in the FAQ, I will try the configured AI engine. If that also fails, I will show you the closest FAQ matches I found. You can also check **Settings → Version Details** or the full README on GitHub.

### Can the Help bot take actions for me?
No. I am strictly read-only. I can point you to the right tab or setting, but I cannot create projects, upload files, move papers, or change any settings. Use the **Chat** tab for actions.

---

## 📁 Projects & Library

### What is a project?
A project is a research folder under `01-PROJECTS/` with a clear focus. It contains your papers in `01-LIBRARY/`, 12-point analyses in `02-EXTRACTIONS/`, drafts in `03-MANUSCRIPTS/`, and a project manifest in `99-META/`.

### What is the project manifest?
The file `99-META/PROJECT-MANIFEST.md` inside each project. It records the project title, focus, goals, and research questions. The AI uses this when answering project-specific questions in Chat.

### What is the folder structure of a project?
Each project has: `01-LIBRARY/` (your papers as .md), `02-EXTRACTIONS/` (12-point analyses), `03-MANUSCRIPTS/` (writing drafts), `99-META/` (manifest and metadata).

### How do I read a paper in the library?
Open the **Library** tab inside the Projects view, pick a project, then click **Read** on any file. A modal opens with the full Markdown content.

### How do I rename a project?
In the **Projects** tab, click the rename/edit icon next to the project. Or ask the Chat AI: "Rename project P2-OLD to P2-NEW". The AI will show an action card.

### How do I delete a project?
In the **Projects** tab, click the delete icon next to the project. Deleted projects move to **Settings → Trash** and can be restored within 30 days.

### How many projects can I have?
Unlimited. The system creates folders on disk — there is no cap. Performance stays fast even with dozens of projects.

### What does the P1, P2 naming mean?
It is a convention, not a requirement. `P1-NAME` means Project 1 with that name. Use any prefix you like. Consistent naming (P1, P2, P3) makes sorting and AI context easier to manage.

---

## 🕸️ Knowledge Graph

### What is the knowledge graph?
A visual map of all your research files — papers, extractions, notes, chats — connected by shared keywords, project membership, and references. Built with D3.js, fully interactive in the browser.

### What dimensions can I filter the graph by?
Seven dimensions: **Author**, **Year**, **Journal**, **Quartile**, **Method**, **Framework**, and **Keyword**. Combine any of them with AND/OR logic using up to 4 filter layers.

### How do I add a filter layer to the graph?
Click **+ Add Layer** in the Graph toolbar. Pick a dimension and value. Stack up to 4 layers at once. All active layers are applied simultaneously.

### What is cluster mode in the graph?
Cluster mode groups nodes by a category (Author, Year, Journal, etc.) without filtering them out. Papers cluster around a central category hub. You can mix cluster mode with filter layers.

### How do I refresh the graph?
Click **Refresh** in the Graph tab header. This re-scans all your project files and rebuilds the full node/edge network from scratch.

### What are nodes and edges in the graph?
Each **node** is a paper, extraction, note, or keyword. **Edges** connect nodes that share keywords, belong to the same project, or reference each other. Thicker edges indicate stronger connections.

### How do I open a file from the graph?
Click any node. A tooltip appears with the file name and metadata. Click **Open** in the tooltip to read the full file in a modal.

### Why is the graph empty?
Click **Refresh**. If still empty, make sure your projects have files in `01-LIBRARY/`. Empty files and folders with no content are ignored by the graph builder.

---

## 🧠 Memory Tab

### What is the Memory tab in Settings?
Memory shows every `.md` file anywhere in the system — chats, papers, extractions, notes, and drafts across all projects. It is a global file browser, not limited to one project.

### What is the difference between Memory and Library?
**Library** shows only the papers inside one specific project's `01-LIBRARY/` folder. **Memory** shows every `.md` file system-wide, including chats, notes, and drafts from all projects.

### How do I view a file in Memory?
Find the file in the Memory table, then click **👁 Read**. A modal opens with the full Markdown content.

### How do I delete a file from Memory?
Click the **🗑 Delete** button next to the file. Deleted files move to **Settings → Trash** and can be restored within 30 days.

### What files appear in Memory?
All `.md` files the system tracks: papers from INCOMING, extraction analyses, saved chat sessions, quick notes, drafts, and project manifest files.

### What is Settings › Trash?
Trash holds recently deleted files. Files stay here for 30 days. Click **Restore** to bring a file back to its original location. Click **Delete Forever** to permanently remove it.

### What is Settings › Chats?
Chats lists all saved chat sessions stored as `.md` files in `99-SYSTEM-BACKEND/chats/`. You can read, download, or delete old sessions from here.

---

## ⚙️ Settings

### What does Settings › General do?
General controls: timezone, theme (dark/light), AI context window size, auto-extract on upload toggle, and auto-start server on login.

### How do I change the theme from dark to light?
Open **Settings → General**. Toggle the **Theme** switch. The change applies instantly across the whole app.

### What are AI Engines in Settings?
AI Engines is where you configure every AI backend: Claude API, OpenAI, Gemini, Ollama, OpenRouter, and custom endpoints. Each engine has a priority number — lower = tried first.

### How many AI engines can I configure?
Unlimited. Enable as many as you like. The failover router tries them in priority order. Multiple engines mean the AI keeps working even when one service is down.

### What are Skills in Settings?
Skills are reusable Markdown instruction files the AI loads when you type `/skillname` in chat. They work like saved prompt templates. View, add, or edit skills in **Settings → Skills**.

### How do I add a custom skill?
In **Settings → Skills**, click **+ Add Skill**. Give it a name and paste the instruction text. Save. Use it in chat by typing `/yourskillname`.

### What is the Learned Profile (Settings › Learned Profile)?
The Learned Profile is an auto-built synthesis stored in `00-SYSTEM-CORE/MASTER-KNOWLEDGE-BASE.md`. The AI uses it to give answers drawing on your whole research history, not just one project.

### How do keywords work in Settings?
Keywords are important terms auto-extracted from your `.md` files. Click **Auto-Scan** to refresh. Add or delete manually. Deleted keywords are remembered forever and never re-added automatically.

### What is Settings › Predatory Journals?
A blocklist of known predatory publishers. The system flags any Web Research result from a journal on this list. Click **Fetch Latest Online** to update the list from a public source.

### What is the Author section in Settings?
Your name, institution, email, and ORCID. The system uses this when generating paper metadata, citations, and extraction document headers.

### What is Settings › Plugins?
Plugins lets you install third-party AI engine extensions. Drop `.py` files into `00-SYSTEM-CORE/plugins/` or use the plugin installer in this section.

### How do I open Obsidian from ResearchPilot?
Go to **Settings → Obsidian** and click **Open Vault**. Obsidian launches with your entire ResearchPilot folder as the vault. Click **Open Graph** to go straight to the Obsidian graph view.

### What is Settings › Version Details?
Version Details shows the full release history of ResearchPilot — each version with its date and description of changes. Click any version to expand the full release notes.

---

## 🧩 Skills & Extraction

### What skills are built in?
Default skills include `/extract` (12-point analysis), `/review` (critical journal-style review), `/summarize` (concise summary), `/academic-writing` (publication-quality writing mode), and `/caveman` (ultra-compressed output). Open **Settings → Skills** for the full list.

### How do I run a 12-point extraction?
In chat, type `/extract` then paste a paper abstract or ask about a paper already in your library. The AI runs all 12 points and returns a structured analysis.

### What are the 12 extraction points exactly?
1) The Problem, 2) The Gap, 3) Research Questions, 4) Purpose/Objective, 5) Theory/Framework, 6) Methodology, 7) Key Findings, 8) Contribution, 9) Limitations, 10) Implications, 11) Key Citations, 12) Critical Position.

### Can extraction run automatically on upload?
Yes. Enable **Auto-Extract** in **Settings → General**. Every paper you upload will immediately get a 12-point extraction after conversion.

### Where are extraction files saved?
In the project's `02-EXTRACTIONS/` folder, as a `.md` file matching the source paper name.

---

## 🆘 Common Problems

### The AI is not responding or says "No engine configured"
Open **Settings → AI Engines**. Enable at least one engine and make sure your API key is saved. If using Ollama, confirm the Ollama app is running locally before testing.

### My API key is not working
Check the key was copied in full with no leading or trailing spaces. Make sure it is active and not revoked. Claude keys: https://console.anthropic.com. OpenAI keys: https://platform.openai.com.

### My project does not appear in the Chat dropdown
The project may not exist in `01-PROJECTS/`. Create it first in the **Projects** tab, then refresh the Chat page — it will appear in the project dropdown.

### My uploaded file is not in the Library
Check the destination project selected during upload. Files sent to INCOMING do not appear in any project Library. Move them via **Web Research → Imported Papers** or the **Memory** tab.

### The file conversion failed after upload
The file may be password-protected or corrupted. Try opening it yourself to confirm it is readable. Supported formats: PDF, DOCX, DOC, PPTX, PPT, HTML, TXT, CSV, JSON, MD.

### The Knowledge Graph is empty after upload
Click **Refresh** in the Graph toolbar. Only files with actual content are indexed — empty files are ignored.

### The server will not start
Confirm Python 3.10+ is installed. Run `pip install -r requirements.txt` in the `web-app/` folder. Check that port 8000 is not already in use by another application.

### Chat says the context is too long
Reduce **Context Size** in **Settings → General**. Alternatively, use the **File** dropdown in Chat to narrow focus to one document instead of the whole library.

### How do I export or share my research?
All outputs are `.md` files stored locally. Open them in Obsidian, copy to any Markdown editor, or push to Git. They are already shareable in their current format.

### How do I export a full literature review?
Use the endpoint `GET /api/export/lit-review?project=P1-NAME`. It bundles all 12-point extractions from that project into one Markdown file ready for editing.

---

## ⌨️ Keyboard Shortcuts

### What keyboard shortcuts does ResearchPilot support?
Press `1`–`9` to switch tabs (1 = Dashboard, 2 = Chat, 3 = Web Research, etc.). Press `/` to jump focus to the chat input on the Chat tab. Press `Esc` to close any open modal.

### How do I jump to the chat input with the keyboard?
Press `/` (forward slash) from anywhere on the Chat tab. Focus moves directly to the message input field.

### How do I close a modal or popup with the keyboard?
Press `Esc`. Any open modal, detail panel, or overlay closes immediately.

---

## 🧭 Navigation

### How do I switch between the main tabs?
Click any tab label in the top navigation bar. Or press the number key for that tab position (1 = Dashboard, 2 = Chat, 3 = Web Research, and so on).

### How do I navigate between Settings sections?
Open **Settings** (last tab in the nav). Click any section name in the left sidebar. No page reload — sections switch instantly.

### How do I get back to the Dashboard?
Click the **Dashboard** tab in the top nav bar, or press `1`.

---

## 📞 Still Stuck?

### How do I ask the Help bot a question?
Click the **?** button in the bottom-right corner of any page. Type your question and press Enter. I search the FAQ first, then the AI if needed.

### What if the Help bot does not know the answer?
I will show the closest FAQ matches I found. You can also check **Settings → Version Details** or browse the full README at https://github.com/pavelblank/ResearchPilot.

### Can the Help bot take actions for me?
No. I am strictly read-only. I point you to the right place, but I cannot create projects, upload files, move papers, or change settings. For actions, use the **Chat** tab.

---

## 🔄 Alternative Phrasings & Quick Lookups

### How do I add a paper?
Drag the PDF or DOCX onto the **Upload** tab, or click the upload area to browse. The file converts to Markdown automatically and lands in your chosen project folder.

### How do I import a file?
Open the **Upload** tab and drop your file there. Supported formats: PDF, DOCX, TXT, and MD. The system converts and indexes it automatically.

### Where do I drop my PDF?
Go to the **Upload** tab. The large drop zone in the centre accepts any PDF or DOCX. You can also drop multiple files at once.

### How do I start a chat?
Click the **Chat** tab in the top navigation. Type your question in the input box at the bottom and press Enter or click Send.

### How do I talk to the AI?
Open the **Chat** tab. Make sure you have at least one AI engine configured in **Settings → AI Engines**, then type your question and press Enter.

### How do I search my papers?
Use the **Chat** tab — ask the AI directly about your uploaded papers. For searching across the web, use the **Web Research** tab.

### Where is the knowledge graph?
Click the **Graph** tab in the top navigation bar. It shows all your uploaded papers as connected nodes.

### How do I see all my papers?
Open the **Library** tab. It lists every uploaded paper with title, date, and project tag. Click any row to read the full extracted content.

### Where are my projects?
Click the **Projects** tab. All your active projects are listed there with their paper counts and goals.

### How do I change AI settings?
Go to **Settings** (gear icon) and click **AI Engines** in the left sidebar.

### Where do I put my API key?
Open **Settings → AI Engines**. Select your provider, paste the key, and click **Save AI Settings**.

### How do I set up Claude?
In **Settings → AI Engines**, choose **Claude API**. Get your key from https://console.anthropic.com, paste it, and save.

### How do I use GPT?
In **Settings → AI Engines**, choose **OpenAI Compatible**. Paste your key from https://platform.openai.com and save. Works with GPT-4o, GPT-4-turbo, and others.

### How do I use a free AI model?
Use **OpenRouter** — it offers many free models. In **Settings → AI Engines**, choose **OpenAI Compatible**, set the URL to `https://openrouter.ai/api/v1`, and paste your OpenRouter key.

### How do I run AI locally?
Install Ollama (https://ollama.com), pull a model (`ollama pull llama3`), then in **Settings → AI Engines** choose **Ollama**. No API key needed.

### Can I use this without the internet?
Yes, mostly. Upload, Library, Graph, and Memory all work offline. AI chat requires internet unless you use local Ollama. Web Research requires internet to search databases.

### Does this app save my data online?
No. All data is stored locally on your machine as Markdown files. Nothing is sent to external servers unless you use a cloud AI engine (Claude, OpenAI, etc.) for chat.

### Is my data safe?
Yes. Everything stays on your machine. API keys are encrypted at rest with AES-128. No personal research data is ever uploaded.

---

## ⚠️ Errors & Troubleshooting

### I get a 500 error
A 500 error means the Python server hit an unexpected problem. Check the terminal where you launched `python main.py` for