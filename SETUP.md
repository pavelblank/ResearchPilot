# 🚀 ResearchPilot — Setup Guide

**For non-technical researchers. If you can use a web browser, you can run this system.**

This guide takes about **10 minutes** the first time. After that, the system launches in under 5 seconds.

> 💡 **You only need to do steps 1–3 ONCE.** After that, you just double-click one file to start.

---

## 📑 Table of Contents

1. [What is ResearchPilot?](#1-what-is-researchpilot)
2. [What you need (Prerequisites)](#2-what-you-need-prerequisites)
3. [Step 1: Install Python](#step-1-install-python)
4. [Step 2: Download ResearchPilot](#step-2-download-researchpilot)
5. [Step 3: Install dependencies](#step-3-install-dependencies-one-time)
6. [Step 4: Start the system](#step-4-start-the-system)
7. [Optional: Auto-start on every login](#optional-auto-start-on-every-login)
8. [Where do I put my research files?](#where-do-i-put-my-research-files)
9. [How do I update ResearchPilot?](#how-do-i-update-researchpilot)
10. [How do I uninstall?](#how-do-i-uninstall)
11. [Troubleshooting](#troubleshooting)

---

## 1. What is ResearchPilot?

ResearchPilot is a **personal research assistant that runs on YOUR computer**. It is not a website you log into — it is software that lives on your hard drive. Your papers, your notes, your AI keys — all stay on your machine.

When you start it, it opens in your web browser at `http://127.0.0.1:8000` (which is just your own computer, not the internet).

---

## 2. What you need (Prerequisites)

| Requirement | What it is | How to check |
|---|---|---|
| **A computer** | Windows 10/11, macOS 11+, or Linux | — |
| **Python 3.10 or newer** | A free programming tool that runs ResearchPilot | See Step 1 below |
| **500 MB free disk space** | For the system + a few hundred papers | — |
| **An internet connection** | Only when using AI engines or searching papers | — |
| **(Optional) Ollama** | Run AI completely offline, for free | <https://ollama.com> |

That's it. No subscriptions. No accounts. No cloud.

---

## Step 1: Install Python

Python is the language ResearchPilot is written in. It is free and safe.

### 🪟 Windows

1. Go to **<https://www.python.org/downloads/>**
2. Click the big yellow button **"Download Python 3.X.X"**
3. Run the installer (.exe file you just downloaded)
4. ⚠️ **CRITICAL: On the first installer screen, tick the box that says:**
   ```
   ☑ Add Python to PATH
   ```
   This is at the very bottom. Don't miss it.
5. Click **"Install Now"**
6. Wait for the green "Setup was successful" message
7. Click **Close**

**To verify:** Open the **Start menu**, type `cmd`, press Enter. A black window appears. Type:

```
python --version
```

You should see something like `Python 3.11.9`. If you see "Python was not found", restart your computer and try again.

### 🍎 macOS

macOS usually has Python 3 already, but it may be an old version. The easiest way to get a current one:

1. Open the **Terminal** app (press `Cmd + Space`, type `Terminal`, press Enter)
2. Install [Homebrew](https://brew.sh) if you don't have it — paste this into the Terminal and press Enter:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Then install Python:
   ```
   brew install python@3.11
   ```
4. Verify:
   ```
   python3 --version
   ```
   You should see `Python 3.11.x` or similar.

### 🐧 Linux (Ubuntu/Debian)

Most Linux distros come with Python. Verify:

```
python3 --version
```

If it's older than 3.10, install a newer one:

```
sudo apt update
sudo apt install python3.11 python3.11-venv
```

---

## Step 2: Download ResearchPilot

You have two options. **Pick one.**

### Option A: Download as ZIP (easiest, recommended for non-coders)

1. Go to **<https://github.com/researchpilot/ResearchPilot>**
2. Click the big green **`<> Code`** button
3. Click **"Download ZIP"**
4. Once downloaded, **right-click the ZIP → Extract All...**
5. **Choose where to put it.** Suggested locations:
   - Windows: `C:\Users\YourName\Documents\ResearchPilot\`
   - macOS: `/Users/YourName/ResearchPilot/`
   - Linux: `/home/yourname/ResearchPilot/`
6. **Remember this location** — you'll need it in Step 4.

### Option B: Git clone (for users comfortable with the command line)

Open a terminal and run:

```bash
git clone https://github.com/researchpilot/ResearchPilot.git
cd ResearchPilot
```

This creates a folder called `ResearchPilot` in your current directory.

---

## Step 3: Install dependencies (one time)

The first time only, you need to install some helper software. After this, you never need to do it again.

### 🪟 Windows

1. Open the **`ResearchPilot` folder** you extracted
2. Open the **`web-app` folder** inside it
3. **Hold Shift** and **right-click** in the empty space
4. Select **"Open PowerShell window here"** (or "Open in Terminal" on Windows 11)
   - A blue/black window appears with the prompt showing `...\web-app>`
5. Type this and press Enter:
   ```
   python -m pip install -r requirements.txt
   ```
6. Wait 1–3 minutes while it downloads. You'll see lots of text scrolling. That's normal.
7. When you see the prompt again, you're done.

> 💡 **Trouble?** Use Command Prompt instead of PowerShell. From the same `web-app` folder, type `cmd` in the address bar of File Explorer and press Enter.

### 🍎 macOS / 🐧 Linux

1. Open **Terminal**
2. Navigate to the `web-app` folder:
   ```
   cd /path/to/ResearchPilot/web-app
   ```
   (Tip: in Finder, drag the `web-app` folder into the Terminal window — it auto-pastes the path)
3. Install dependencies:
   ```
   python3 -m pip install -r requirements.txt
   ```
4. Wait for the prompt to return.

---

## Step 4: Start the system

**From now on, this is the only thing you do to use ResearchPilot.**

### 🪟 Windows

1. Open the **`web-app` folder**
2. **Double-click `START-SERVER.bat`**
3. A black window appears. Wait 3–10 seconds. It says:
   ```
   ResearchPilot - Starting Server...
   Starting on http://127.0.0.1:8000
   ```
4. Your web browser **automatically opens** to the dashboard
5. **Leave the black window open** while you use ResearchPilot
6. To stop: close the black window, or press `Ctrl + C` inside it

> 💡 **Tip:** Right-click `START-SERVER.bat` → "Send to" → "Desktop (create shortcut)" to put a launcher on your Desktop.

### 🍎 macOS

1. Open **Terminal**
2. Navigate to the `web-app` folder (or use Finder):
   ```
   cd /path/to/ResearchPilot/web-app
   ```
3. Make the launcher executable (first time only):
   ```
   chmod +x START-SERVER.sh
   ```
4. Run it:
   ```
   ./START-SERVER.sh
   ```
5. Browser opens automatically

**Alternative for macOS users who don't like Terminal:**

1. Open the `web-app` folder in Finder
2. Right-click `START-SERVER.sh` → **"Open With" → "Other..."** → choose **Terminal**
3. Check "Always Open With" if you want
4. Now you can double-click it from Finder

### 🐧 Linux

Same as macOS — `./START-SERVER.sh` from the `web-app` folder.

---

## Optional: Auto-start on every login

Don't want to remember to launch it? Make it start automatically.

### 🪟 Windows

1. Open the **`web-app` folder**
2. **Right-click `REGISTER-AUTOSTART.bat` → "Run as administrator"**
   - If you don't see "Run as administrator", double-click it instead. If it fails, open an **administrator** Command Prompt and run it from there
3. You should see "Done!" — the system will now start every time you log into Windows
4. **To turn it off:** open an admin Command Prompt and run:
   ```
   schtasks /delete /tn "ResearchPilot" /f
   ```

### 🍎 macOS

1. Open **System Settings → General → Login Items → Open at Login**
2. Click the **`+`** button
3. Navigate to your `web-app` folder and select `START-SERVER.sh`
4. Done. It will start every time you log in.

### 🐧 Linux

Add this line to `~/.config/autostart/researchpilot.desktop`:

```ini
[Desktop Entry]
Type=Application
Name=ResearchPilot
Exec=/path/to/ResearchPilot/web-app/START-SERVER.sh
Terminal=false
```

---

## Where do I put my research files?

**You don't have to move anything.** ResearchPilot creates its own folders when it starts for the first time.

When you upload a PDF through the web UI, the system stores it in:

```
ResearchPilot/
├── 01-PROJECTS/                  ← your research projects
│   ├── 00-TEMPLATE/              ← blueprint (don't use, just for reference)
│   ├── P1-MY-FIRST-PROJECT/      ← each project has 4 subfolders:
│   │   ├── 01-LIBRARY/           ←   PDFs you upload
│   │   ├── 02-EXTRACTIONS/       ←   AI-generated 12-point analyses
│   │   ├── 03-MANUSCRIPTS/       ←   your draft writing
│   │   └── 99-META/              ←   project notes, manifests
│   └── P2-MY-SECOND-PROJECT/
├── 00-SYSTEM-CORE/               ← system internals (don't touch)
├── 99-SYSTEM-BACKEND/            ← settings, logs, chats (don't touch)
└── INCOMING/                     ← new papers waiting to be sorted
```

### How to create a new project

1. Open ResearchPilot in your browser
2. Go to **⚙️ Settings → Projects**
3. Type a project name (e.g., `P3-LITERATURE-REVIEW`)
4. Click **"+ Create"**
5. The system automatically creates the 4 subfolders

### How to change where projects are stored

By default, projects live in `01-PROJECTS/` inside the ResearchPilot folder. If you want to keep them on a different drive (e.g., `D:\Research\`), you can:

1. **Move the entire `ResearchPilot` folder** to wherever you want (e.g., `D:\Research\ResearchPilot\`)
2. The system will auto-detect the new location on next start
3. **OR** create a Windows shortcut / macOS symlink from the new location to the old one

> ⚠️ The system uses the folder you downloaded it to. If you move it, everything still works — the BASE path is auto-detected.

### How to add a PDF

**Option 1: Drag and drop**
1. Open ResearchPilot in your browser
2. Click the **📤 Upload** tab
3. Drag a PDF from your computer into the upload zone
4. The system auto-converts it to markdown and stores it

**Option 2: Browse**
1. Same tab
2. Click the upload zone
3. Choose your PDF from the file picker

**Option 3: Drop into INCOMING folder**
1. Put PDFs directly into `ResearchPilot/INCOMING/`
2. Then in the UI: **🔍 Web Research → UNREAD-WEB tab → "Move to project"**

---

## How do I update ResearchPilot

### 🪟 Windows (no git)

1. Download the new ZIP from GitHub
2. Extract it to a temporary folder
3. Copy your personal folders from your old installation to the new one:
   - `01-PROJECTS/`
   - `99-SYSTEM-BACKEND/settings.json` (your encrypted API keys)
   - `99-SYSTEM-BACKEND/.settings_key` (the encryption key)
   - `99-SYSTEM-BACKEND/notes.json` (your quick notes)
4. Run the install-dependencies step (Step 3) again
5. Delete the old folder

### 🍎 / 🐧 macOS / Linux (with git)

From inside the `ResearchPilot` folder:

```bash
git pull
cd web-app
python3 -m pip install -r requirements.txt --upgrade
```

Then restart the server.

---

## How do I uninstall

1. **Stop the server** (close the black window, or `Ctrl+C` in the terminal)
2. **(Windows only) Remove auto-start:**
   ```
   schtasks /delete /tn "ResearchPilot" /f
   ```
3. **Delete the `ResearchPilot` folder** — that's it. Everything is self-contained.

Your papers, settings, and notes live inside that folder, so make sure to back them up first if you want to keep them.

---

## Troubleshooting

### "python is not recognized as a command" (Windows)

You forgot to tick **"Add Python to PATH"** during install. Fix:
1. Re-run the Python installer
2. Choose **"Modify"**
3. Tick **"Add Python to PATH"**
4. Click Install
5. Restart your computer

### "Address already in use" / Port 8000 is busy

Something else is using port 8000. Two options:

**Option A — Change the port:**
1. Right-click `start-research.bat` → Edit (or open in Notepad)
2. Find the line `set PORT=8000` and change to `8001` (or any free port)
3. Save and run again
4. Open `http://127.0.0.1:8001` in your browser

**Option B — Find and stop the other process:**

Windows:
```
netstat -ano | findstr :8000
taskkill /PID <number> /F
```

macOS/Linux:
```
lsof -i :8000
kill -9 <PID>
```

### "Permission denied" when running scripts (macOS/Linux)

Make the script executable:
```
chmod +x START-SERVER.sh
```

### The page won't load / browser shows "This site can't be reached"

The server isn't running. Check the black/terminal window — is there an error message? Most common causes:
- Python wasn't installed correctly (see above)
- Dependencies weren't installed (re-run Step 3)
- A firewall is blocking it (allow Python through Windows Firewall when prompted)

### "ModuleNotFoundError: No module named 'fastapi'"

Dependencies weren't installed. Re-run Step 3:
```
python -m pip install -r requirements.txt
```

### My AI engines say "no API key"

1. Open ResearchPilot in your browser
2. Go to **⚙️ Settings → AI Engines**
3. For each engine you want to use, paste your API key
4. The key is **encrypted and stored locally** — never sent anywhere except the engine provider

If you don't have an API key yet, **install Ollama** (<https://ollama.com>) — it's free and runs AI completely on your computer.

### I want to move ResearchPilot to a different folder

Just **move the folder**. The system auto-detects its location on startup. No reconfiguration needed.

### I want to use a different port

Set the `PORT` environment variable before starting:
- Windows: `set PORT=9000` then run `START-SERVER.bat`
- macOS/Linux: `PORT=9000 ./START-SERVER.sh`

---

## Still stuck?

- 💬 Open an issue: <https://github.com/researchpilot/ResearchPilot/issues>
- 📖 Read the architecture: [SYSTEM-DOCUMENTATION.md](SYSTEM-DOCUMENTATION.md)
- 🔒 Security questions: [SECURITY.md](SECURITY.md)

---

<p align="center"><sub>Last updated: 2026-06-04 · ResearchPilot V5.4 · Made with care for researchers worldwide.</sub></p>
