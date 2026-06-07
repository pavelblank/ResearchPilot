# ResearchPilot , Help & FAQ

> This file is the canonical knowledge base for the **Help bot** (the floating **?** button).
> The Help bot is **view-only** , it never edits, creates, or deletes files. It only guides you.

---

## 💡 Quick Answers

Short, plain replies for the most common things people ask. Tap a question, or just type it.

### What is ResearchPilot?

It's a local research workspace for academic work. You drop papers in, the AI helps you read them, extract findings, and write drafts, and everything is saved as plain Markdown files in your own folders.

### What can you help me with?

I can guide you around the app and answer questions about how it works. For research questions about your own papers, use the **Chat** tab.

### What day is today? / What time is it? / What's the date?

Open the **Dashboard** tab. There's a live calendar and clock widget right at the top of the page.

### What is the difference between Library and Memory?

**Library** holds the papers inside one specific project. **Memory** shows every `.md` file across the whole system, including chats, notes, and drafts from all projects.

### Where do my files go?

All your work lives as `.md` (Markdown) files inside `01-PROJECTS/` (per project) and `99-SYSTEM-BACKEND/` (chats, logs). You can open the folder in Obsidian any time.

### Can the help bot do things for me (create projects, move files)?

No, I'm read-only. I can only point you to the right place. The **Chat** tab AI can take actions and shows you an Undo button.

### Is my data private?

Yes. Everything is stored locally on your machine as Markdown files. Nothing is uploaded to a server unless you connect your own AI engine key.

---

## 🚀 Getting Started

### How do I set up my first AI engine (Claude / OpenAI / OpenRouter)?

1. Click the **⚙️ Settings** tab (top right, or press its number key).
2. In the left sidebar, click **AI Engines**.
3. Pick the engine you want:
 - **Claude API**. Get a key at https://console.anthropic.com
 - **OpenAI Compatible**. Works with OpenAI, OpenRouter, Jan, LocalAI, etc.
 - **Custom API**. For any OpenAI-compatible endpoint.
4. Paste your key, click **Save AI Settings**.

> The Help bot can take you there in one click. Just ask: *"How do I set up my API key?"*

### Where do I drop new papers?

- Use the **📤 Upload** tab , drag & drop PDF/DOCX/PPTX. Choose a project, or send to **INCOMING** to sort later.
- The file is auto-converted to Markdown and stored in the project's `01-LIBRARY/`.

### How do I create a new project?

- Open the **📁 Projects** tab then **+ New Project**.
- Use the ID format: `P1-NAME`, `P2-NAME`, etc. (any prefix works, but stick to one style).
- Set the focus and goals , this helps the AI give better answers in that project.

---

## 💬 Chat Tab

### What can I do in Chat?

- Ask the AI to **analyze papers**, **write literature reviews**, **compare findings**.
- Use **/skillname** in your message to activate a specific skill (e.g. `/extract`, `/review`).
- Pick a **project** in the top toolbar to use that project's files as context.
- Pick a **File** to focus the AI on one document.
- Press **/** (forward slash) anywhere to jump focus to the chat input.

### Does the chat save?

Yes, every chat is auto-saved as a Markdown file in `99-SYSTEM-BACKEND/chats/`. You can also click **💾 Save** to clear the chat and keep a `.md` copy.

### Can the AI do things for me (create projects, move files)?

The **main Chat tab AI** can. Ask naturally: *"Create a new project called P5-BRAIN-COMPUTER"* or *"Move paper X to P3-EEG"*. The AI will show you an **Action card** and you can **Undo** any action.

The **Help bot** (the floating **?**) cannot. It's read-only and just guides you.

---

## 🔍 Web Research

### Which sources are available?

OpenAlex (always free), Crossref, Semantic Scholar, PubMed, Google Scholar (experimental). Toggle them in **Web Research → Sources** before searching.

### How do I download a paper?

For **Open Access (OA)** papers, click **Download PDF**. The PDF plus `.md` are saved. For **non-OA** papers, click **Download .md (12-Point)**. The AI generates a 12-point analysis stub from the abstract.

### How do I move an imported paper into a project?

In **Web Research → Imported Papers**, pick a project from the dropdown, then click **Move**.
The file is moved to that project's `01-LIBRARY/`.

---

## 📁 Projects & Library

### What is a "project"?

A project is a folder under `01-PROJECTS/` that holds a focused research topic. It has a manifest (`00-PROJECT-MANIFEST.md`), your papers in `01-LIBRARY/`, the 12-point analyses in `02-EXTRACTIONS/`, writing in progress in `03-DRAFTS/`, and published work in `99-OUTPUT/`.

### How do I read a paper in the library?

Open the **Library** tab, pick a project then click **Read** on any file. A modal opens with the content.

---

## 🕸️ Graph Tab

### What is the graph?

A visual map of all your **.md files**, **code files**, **extractions**, **keywords**, and **chats**, connected by shared keywords, project membership, and references.

### How do I use the filters?

- Up to **4 layers** of filters (e.g. `year:2024 AND journal:Nature AND author:Smith`).
- Click **+ Add Layer** to stack filters.
- Click **Clear** to reset.

---

## 🧠 Memory Tab

### What's the difference between Memory and Library?

**Memory** shows every `.md` file anywhere in the system (chats, extractions, notes, drafts). **Library** shows only the papers inside one specific project's `01-LIBRARY/` folder. Both are accessible from the **Memory** tab in the top nav, or from **Settings → Memory**.

---

## ⚙️ Settings, Detailed

### What do the Settings sections do?

Open **Settings** (last tab). The left sidebar has 13 sections, in order: **General** for timezone and theme, **AI Engines** to configure Claude, OpenAI, OpenRouter, or local models, **Skills** to add reusable AI instructions, **Knowledge Base** for the synthesized cross-project view, **Keywords** to search important words across your papers, **Predatory Journals** to block low-quality publishers, **Author** to save your name and ORCID, **Plugins** to add extra AI engines, **Obsidian** to open the vault, **Memory** to browse every .md file, **Trash** to restore deleted items, **Chats** to manage saved chat sessions, and **Changelog** to see what changed.

You don't have to configure everything at once. Start with **AI Engines** (so the AI can talk to you) and **Author** (so it knows who you are). Add the rest as you need them.

### How do I search the web for papers?

1. Open the **🔍 Web Research** tab.
2. Type a detailed query. Full sentences work better than 1 or 2 keywords
 (e.g. *"cybersecurity awareness programs in higher education institutions and their impact on student data protection behavior"*).
3. Pick a **Year** range (e.g. 2020 to 2025) and enable one or more **Sources**:
 OpenAlex, Crossref, Semantic Scholar, PubMed, Google Scholar.
4. Pick a **Sort**: relevance, citations, or year.
5. Click **Search**. Results appear as cards.
6. For each paper you can **Read** (modal preview), **Open** (browser),
 **Download PDF** (OA papers) or **Download .md (12-Point)** (non-OA papers).
7. After download, use the **Move** dropdown to send the paper to a project.

### AI Engines

The available engine types are: **Claude API** (best for long-context, nuanced analysis, needs `ANTHROPIC_API_KEY`), **OpenAI Compatible** (for `gpt-4o`, `gpt-4-turbo`, etc., or use with **OpenRouter** for many models), **Custom API** (any OpenAI-format endpoint like Jan, LM Studio, LocalAI), **Gemini** (Google AI), and **Ollama** (local models, must be running locally).

The system **fails over** automatically: if Claude is down, it tries OpenAI then the next, etc.

### Skills

- Skills are reusable instruction files the AI loads on demand. Type `/skillname` in chat.
- Default skills include `/extract`, `/review`, `/summarize`, and more.
Add your own in `00-SYSTEM-CORE/skills/` (or via Settings → Skills).

### Knowledge Base

- The **Master Knowledge Base** (in `00-SYSTEM-CORE/MASTER-KNOWLEDGE-BASE.md`) is a synthesized view of all your projects.
- The AI uses it to give cross-project answers.

### Keywords

- Auto-scanned from your `.md` files.
Click **Auto-Scan** in Settings → Keywords to refresh.
- Add/remove manually. Discarded keywords won't be re-added.

### Predatory Journals

- A blocklist. The system flags any search result published in a journal on this list.
- Click **Fetch Latest Online** to download the latest public blocklist.

### Author

- Your name, affiliation, email, ORCID.
- Used when generating paper metadata and citations.

### Plugins

- Install third-party AI engine plugins (`.py` files into `00-SYSTEM-CORE/plugins/`).

### Obsidian

Click **Open Vault** to launch Obsidian pointed at your research folder. The folder is a standard Obsidian vault, so your chats, extractions, and notes are all readable there.

### Changelog

What changed in each version of ResearchPilot.

---

## 🆘 Common Problems

### "AI isn't responding" or "No engine configured"

Open **Settings → AI Engines**. Enable at least one engine and save your API key.

### "My project doesn't show up in Chat"

Save the chat (💾 Save) and pick the project from the **Project** dropdown in the chat toolbar. If the project is missing there, it may not be in `01-PROJECTS/`. Create it in the **Projects** tab.

### "My file isn't in the library"

Check the **destination project** you uploaded to. Files uploaded to INCOMING won't appear in any project's library. Move them via **Web Research → Imported Papers** or the **Memory** tab (or **Settings → Memory**).

The file may have failed auto-conversion. Check the file is `.pdf`, `.docx`, `.pptx`, `.txt`, `.md`, or `.html`.

### "Graph is empty"

Click **Refresh** in the Graph tab header to re-scan files and rebuild the graph. Make sure your files have content (empty files are ignored).

### "How do I export / share my work?"

All chats, extractions, and drafts are `.md` files. They're already shareable. Open them in Obsidian, copy to any Markdown editor, or push to Git.

### "Can I use ResearchPilot offline?"

The web app runs locally. The AI engines need internet (or a local Ollama). Everything else (uploads, library, graph, memory) works offline.

---

## 🧭 Keyboard Shortcuts

| Key | Action |
|---|---|
| `1` to `9` | Switch to tab N (1=Dashboard, 2=Chat, 3=Research, ) |
| `/` | Focus the chat input (when on Chat tab) |
| `Esc` | Close the open modal |

---

## 📞 Still stuck?

The **floating ? button** (bottom-right corner) is the Help bot. Ask it anything about ResearchPilot:
- *"How do I set up my API key?"*
- *"Where do I find the knowledge graph?"*
- *"How do I move a file from INCOMING to a project?"*
- *"What does the Memory tab do?"*

It only knows about ResearchPilot. For general research questions, use the **💬 Chat** tab.

---

## 🐙 About the project

### Where is the source code / GitHub repo?

The GitHub repository is configured in Settings (or ask the Help bot for the current link if one is set). If no link is set, this build is private and the source is local.

### Can I contribute / fork the project?

Yes. The project is yours to fork, star, or extend. See the README for the license and contribution guidelines.
