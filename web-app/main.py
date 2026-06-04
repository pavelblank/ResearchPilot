"""
ResearchPilot — v2.0
Multi-AI backbone (never stops), universal file ingestion, settings from web UI,
project management, skills system. All chats saved as .md for Obsidian.
"""

import os, json, re, shutil, datetime, traceback, asyncio, hashlib, secrets, base64
from pathlib import Path
from cryptography.fernet import Fernet
from typing import List, Optional, Any

# ─── Load .env ────────────────────────────────────────────────────────────────
_env = Path(__file__).parent / ".env"
if _env.exists():
    for _l in _env.read_text().splitlines():
        _l = _l.strip()
        if _l and not _l.startswith("#") and "=" in _l:
            _k, _v = _l.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip())

import fitz                         # PyMuPDF
import html2text
import httpx
import aiofiles
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# optional heavy imports — graceful fallback
try:
    from docx import Document as DocxDoc
    HAS_DOCX = True
except ImportError:
    HAS_DOCX = False

try:
    from pptx import Presentation as PptxPres
    HAS_PPTX = True
except ImportError:
    HAS_PPTX = False

try:
    import anthropic as _anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

# docling — heavy PDF→MD converter (lazy import to avoid slow startup)
HAS_DOCLING = None  # None = not checked yet

# scholarly — Google Scholar scraper (free, no key)
try:
    import scholarly as _scholarly
    HAS_SCHOLARLY = True
except ImportError:
    HAS_SCHOLARLY = False

# ─── Paths ────────────────────────────────────────────────────────────────────
BASE       = Path(r"C:\F- Drive\MYWORK-Research1")
PROJECTS   = BASE / "01-PROJECTS"
CORE       = BASE / "00-SYSTEM-CORE"
BACKEND    = BASE / "99-SYSTEM-BACKEND"
INCOMING   = BASE / "INCOMING"
CHATS_DIR  = BACKEND / "chats"
SKILLS_DIR = CORE / "skills"
PLUGINS_DIR = BACKEND / "plugins"
SETTINGS_F = BACKEND / "settings.json"
SETTINGS_KEY_FILE = BACKEND / ".settings_key"
STATIC     = Path(__file__).parent / "static"

# ─── Auth token ─────────────────────────────────────────────────────────
TOKEN_FILE = BASE / ".token"
if not TOKEN_FILE.exists():
    TOKEN_FILE.write_text(secrets.token_hex(32))
AUTH_TOKEN = TOKEN_FILE.read_text().strip()

# ─── Settings encryption ────────────────────────────────────────────────
def _get_fernet() -> Fernet:
    if not SETTINGS_KEY_FILE.exists():
        SETTINGS_KEY_FILE.write_text(Fernet.generate_key().decode())
    key = SETTINGS_KEY_FILE.read_text().strip().encode()
    return Fernet(key)

def _encrypt_val(val: str) -> str:
    if not val:
        return val
    return _get_fernet().encrypt(val.encode()).decode()

def _decrypt_val(val: str) -> str:
    if not val:
        return val
    try:
        return _get_fernet().decrypt(val.encode()).decode()
    except Exception:
        return val  # already plaintext or corrupted — return as-is

def _encrypt_settings(data: dict) -> dict:
    d = json.loads(json.dumps(data))  # deep copy
    for eng in d.get("ai_engines", []):
        if eng.get("api_key"):
            eng["api_key"] = _encrypt_val(eng["api_key"])
    return d

def _decrypt_settings(data: dict) -> dict:
    d = json.loads(json.dumps(data))  # deep copy
    for eng in d.get("ai_engines", []):
        if eng.get("api_key"):
            eng["api_key"] = _decrypt_val(eng["api_key"])
    return d

# ─── Load saved plugin API keys ─────────────────────────────────────────
_plugins_dir = BACKEND / "plugins"
if _plugins_dir.exists():
    for _pf in _plugins_dir.glob("*.json"):
        try:
            _pd = json.loads(_pf.read_text())
            for _pk, _pv in _pd.items():
                if _pv:
                    os.environ.setdefault(_pk.upper(), _pv)
        except Exception:
            pass

UNREAD_WEB      = INCOMING / "UNREAD-WEB"
PREDATORY_FILE  = CORE / "predatory_journals.json"

for d in [CHATS_DIR, INCOMING, SKILLS_DIR, PLUGINS_DIR, PROJECTS, UNREAD_WEB]:
    d.mkdir(parents=True, exist_ok=True)

# ─── Settings ─────────────────────────────────────────────────────────────────
DEFAULT_SETTINGS = {
    "ai_engines": [
        {"name":"Ollama (Local)","type":"ollama","url":"http://localhost:11434","model":"llama3","api_key":"","enabled":True,"priority":1,"note":"Free local AI. Install from https://ollama.com"},
        {"name":"LM Studio (Local)","type":"openai_compat","url":"http://localhost:1234/v1","model":"local-model","api_key":"lm-studio","enabled":False,"priority":2,"note":"Free local. Open LM Studio → start local server."},
        {"name":"Gemini Flash (Free)","type":"gemini","url":"","model":"gemini-1.5-flash","api_key":"","enabled":False,"priority":3,"note":"Free tier. https://aistudio.google.com/app/apikey"},
        {"name":"Gemini Pro","type":"gemini","url":"","model":"gemini-1.5-pro","api_key":"","enabled":False,"priority":4,"note":"Same Gemini key, stronger model."},
        {"name":"Claude Haiku (Fast)","type":"anthropic","url":"","model":"claude-haiku-4-5","api_key":"","enabled":False,"priority":5,"note":"Anthropic API. https://console.anthropic.com"},
        {"name":"Claude Sonnet (Deep)","type":"anthropic","url":"","model":"claude-sonnet-4-5","api_key":"","enabled":False,"priority":6,"note":"Deep research. Same Anthropic key."},
        {"name":"OpenRouter (Free Models)","type":"openai_compat","url":"https://openrouter.ai/api/v1","model":"mistralai/mistral-7b-instruct:free","api_key":"","enabled":False,"priority":7,"note":"Many free models. https://openrouter.ai"},
        {"name":"Custom API","type":"openai_compat","url":"http://localhost:8080/v1","model":"custom-model","api_key":"","enabled":False,"priority":8,"note":"Any OpenAI-compatible API (Jan, LocalAI, etc.)"}
    ],
    "auto_extract_on_upload": True,
    "max_context_chars": 40000,
    "system_name": "ResearchPilot",
    "chats_folder": "99-SYSTEM-BACKEND/chats",
    "skills_folder": "00-SYSTEM-CORE/skills",
    "auto_start": False,
    "timezone": "UTC"
}

def load_settings() -> dict:
    if SETTINGS_F.exists():
        try:
            raw = json.loads(SETTINGS_F.read_text(encoding="utf-8"))
            return _decrypt_settings(raw)
        except Exception:
            pass
    SETTINGS_F.write_text(json.dumps(_encrypt_settings(DEFAULT_SETTINGS), indent=2), encoding="utf-8")
    return DEFAULT_SETTINGS.copy()

def save_settings(data: dict):
    SETTINGS_F.write_text(json.dumps(_encrypt_settings(data), indent=2), encoding="utf-8")

# ─── Tool Definitions (for local AI file access) ──────────────────────────────
# These let the AI read/search/list any file in the ResearchPilot system on demand.

ResearchPilot_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read the full content of any file in the ResearchPilot research system. Path is relative to the ResearchPilot root.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Relative path like '00-SYSTEM-CORE/MASTER-KNOWLEDGE-BASE.md' or '01-PROJECTS/P1-HEI-CULTURE/02-EXTRACTIONS/P001 - Content Extraction.md'"}
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_files",
            "description": "Search across all files in the ResearchPilot system for matching text (case-insensitive). Returns matching files and snippets.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Text or regex pattern to search for"},
                    "max_results": {"type": "integer", "description": "Max results to return (default 20)"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_directory",
            "description": "List files and subdirectories in any ResearchPilot directory.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Relative path from ResearchPilot root, e.g. '01-PROJECTS/P1-HEI-CULTURE' or '00-SYSTEM-CORE'"}
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_project_list",
            "description": "List all research projects with their paper count and extraction count."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_knowledge_base",
            "description": "Read the full Master Knowledge Base — a synthesis of all papers across all projects."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_extractions_list",
            "description": "List all extraction files available for a given research project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project": {"type": "string", "description": "Project ID like 'P1-HEI-CULTURE' or 'P2-YEAHIA-BACKBONE'"}
                },
                "required": ["project"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_extraction",
            "description": "Read a specific 12-point extraction file by project and filename.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project": {"type": "string", "description": "Project ID like 'P1-HEI-CULTURE'"},
                    "filename": {"type": "string", "description": "Extraction filename like 'P001 - Content Extraction.md'"}
                },
                "required": ["project", "filename"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_project_manifest",
            "description": "Read the PROJECT-MANIFEST.md for any project to get its focus, goals, and status.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project": {"type": "string", "description": "Project ID like 'P1-HEI-CULTURE'"}
                },
                "required": ["project"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_system_structure",
            "description": "Get the full ResearchPilot folder structure overview."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_system_core",
            "description": "Read any file from the 00-SYSTEM-CORE directory (protocols, specs, connections, etc.).",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "Filename like 'SYSTEM-PROTOCOLS.md', 'ResearchPilot-SYSTEM-SPECIFICATION.md', 'GLOBAL-CONNECTIONS.md', 'PUBLISHING-ROADMAP.md'"}
                },
                "required": ["filename"]
            }
        }
    }
]

def resolve_era_path(relative_path: str) -> Path:
    """Resolve a relative path safely within the ResearchPilot BASE directory."""
    full = (BASE / relative_path).resolve()
    if not str(full).startswith(str(BASE.resolve())):
        raise PermissionError(f"Access denied: path escapes ResearchPilot root: {relative_path}")
    return full

def safe_project_path(project: str, subfolder: str, filename: str) -> Path:
    """Build a safe project file path with traversal protection."""
    safe_proj = re.sub(r'[^\w\-]', '', project)
    safe_name = sanitize_filename(filename)
    if not safe_proj or not safe_name:
        raise HTTPException(400, "Invalid path")
    if project == "INCOMING":
        full = (INCOMING / safe_name).resolve()
    else:
        full = (PROJECTS / safe_proj / subfolder / safe_name).resolve()
    if not str(full).startswith(str(BASE.resolve())):
        raise HTTPException(403, "Access denied")
    return full

async def execute_tool(name: str, args: dict) -> dict:
    """Execute a tool by name with given arguments and return results."""
    try:
        if name == "read_file":
            path_str = args.get("path", "")
            if not path_str:
                return {"error": "Missing required argument: path"}
            path = resolve_era_path(path_str)
            if not path.exists():
                return {"error": f"File not found: {path_str}"}
            if path.is_dir():
                return {"error": f"Path is a directory, not a file: {path_str}"}
            content = path.read_text(encoding="utf-8", errors="replace")
            return {"content": content, "path": path_str, "size_kb": round(path.stat().st_size / 1024, 1)}

        if name == "search_files":
            query = args.get("query", "")
            max_results = min(args.get("max_results", 20), 50)
            results = []
            for f in BASE.rglob("*"):
                if f.is_file() and f.suffix.lower() in (".md", ".txt", ".py", ".json", ".yaml", ".yml", ".csv", ".html"):
                    try:
                        text = f.read_text(encoding="utf-8", errors="ignore")
                        if query.lower() in text.lower():
                            rel = str(f.relative_to(BASE))
                            # Find context around match
                            idx = text.lower().find(query.lower())
                            start = max(0, idx - 60)
                            end = min(len(text), idx + len(query) + 60)
                            snippet = text[start:end].replace("\n", " ")
                            results.append({"file": rel, "snippet": snippet})
                            if len(results) >= max_results:
                                break
                    except Exception:
                        continue
            return {"results": results, "count": len(results), "query": query}

        if name == "list_directory":
            path = resolve_era_path(args.get("path", ""))
            if not path.exists():
                return {"error": f"Directory not found: {args.get('path', '')}"}
            if not path.is_dir():
                return {"error": f"Not a directory: {args.get('path', '')}"}
            items = []
            for item in sorted(path.iterdir()):
                items.append({
                    "name": item.name,
                    "type": "dir" if item.is_dir() else "file",
                    "size_kb": round(item.stat().st_size / 1024, 1) if item.is_file() else None
                })
            return {"path": args.get("path", ""), "items": items, "count": len(items)}

        if name == "get_project_list":
            projects = []
            for p in sorted(PROJECTS.iterdir()):
                if not p.is_dir() or p.name.startswith("00-"):
                    continue
                lib = p / "01-LIBRARY"
                ext = p / "02-EXTRACTIONS"
                projects.append({
                    "id": p.name,
                    "papers": len(list(lib.glob("*.*"))) if lib.exists() else 0,
                    "extractions": len(list(ext.glob("*.md"))) if ext.exists() else 0
                })
            return {"projects": projects}

        if name == "read_knowledge_base":
            kb = CORE / "MASTER-KNOWLEDGE-BASE.md"
            if not kb.exists():
                return {"content": "# Master Knowledge Base\n\n*Empty*", "path": "00-SYSTEM-CORE/MASTER-KNOWLEDGE-BASE.md"}
            return {"content": kb.read_text(encoding="utf-8"), "path": "00-SYSTEM-CORE/MASTER-KNOWLEDGE-BASE.md"}

        if name == "read_extractions_list":
            project = args.get("project", "")
            if not project:
                return {"error": "Missing required argument: project"}
            ext_dir = PROJECTS / project / "02-EXTRACTIONS"
            if not ext_dir.exists():
                return {"error": f"No extractions found for project: {project}"}
            files = []
            for md in sorted(ext_dir.glob("*.md")):
                files.append({
                    "filename": md.name,
                    "size_kb": round(md.stat().st_size / 1024, 1)
                })
            return {"project": project, "files": files}

        if name == "read_extraction":
            project = args.get("project", "")
            filename = args.get("filename", "")
            if not project or not filename:
                return {"error": "Missing required arguments: project and filename"}
            ext_dir = PROJECTS / project / "02-EXTRACTIONS"
            fp = ext_dir / filename
            if not fp.exists():
                matches = list(ext_dir.glob(f"*{filename}*"))
                if not matches:
                    return {"error": f"Extraction not found: {project}/{filename}"}
                fp = matches[0]
            return {
                "content": fp.read_text(encoding="utf-8"),
                "project": project,
                "filename": fp.name
            }

        if name == "read_project_manifest":
            project = args.get("project", "")
            if not project:
                return {"error": "Missing required argument: project"}
            mf = PROJECTS / project / "99-META" / "PROJECT-MANIFEST.md"
            if not mf.exists():
                return {"error": f"No manifest found for project: {project}"}
            return {"content": mf.read_text(encoding="utf-8"), "project": project}

        if name == "get_system_structure":
            structure = {
                "00-SYSTEM-CORE": "Centralized intelligence, protocols, master knowledge base",
                "01-PROJECTS": "Research projects (P1, P2, etc.) with LIBRARY/EXTRACTIONS/MANUSCRIPTS/META",
                "99-SYSTEM-BACKEND": "System logs, chat history, automation reports",
                "INCOMING": "Landing zone for new papers"
            }
            return {"structure": structure}

        if name == "read_system_core":
            filename = args.get("filename", "")
            if not filename:
                return {"error": "Missing required argument: filename"}
            fp = CORE / filename
            if not fp.exists():
                return {"error": f"File not found in 00-SYSTEM-CORE: {filename}"}
            return {"content": fp.read_text(encoding="utf-8"), "filename": filename}

        return {"error": f"Unknown tool: {name}"}
    except PermissionError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Tool execution error: {str(e)}"}

# ─── RAG: Context Retrieval ────────────────────────────────────────────────────
# Searches ALL project files for content relevant to the user's query,
# then injects it into the prompt so any AI engine can use it.

def retrieve_relevant_context(query: str, project: str = None, max_chars: int = 25000) -> str:
    """Search all ResearchPilot files for content relevant to the query. Returns formatted context block."""
    query_lower = query.lower()
    query_words = [w for w in query_lower.split() if len(w) > 3]
    if not query_words:
        query_words = query_lower.split()[:5]

    scored = []  # (score, label, content)

    # 1. Score extraction files
    ext_dirs = []
    if project and project != "INCOMING":
        ed = PROJECTS / project / "02-EXTRACTIONS"
        if ed.exists():
            ext_dirs.append((project, ed))
    else:
        for proj in sorted(PROJECTS.iterdir()):
            if proj.is_dir() and not proj.name.startswith("00-"):
                ed = proj / "02-EXTRACTIONS"
                if ed.exists():
                    ext_dirs.append((proj.name, ed))

    for proj_name, ext_dir in ext_dirs:
        for md in sorted(ext_dir.glob("*.md")):
            try:
                text = md.read_text(encoding="utf-8", errors="ignore")
                text_lower = text.lower()
                score = sum(1 for w in query_words if w in text_lower)
                # Title match bonus
                if any(w in md.stem.lower() for w in query_words):
                    score += 3
                if score > 0:
                    scored.append((score, f"[{proj_name}] {md.stem}", text[:8000]))
            except Exception:
                continue

    # 2. Score knowledge base
    kb = CORE / "MASTER-KNOWLEDGE-BASE.md"
    if kb.exists():
        try:
            text = kb.read_text(encoding="utf-8", errors="ignore")
            text_lower = text.lower()
            score = sum(2 for w in query_words if w in text_lower)
            if score > 0:
                scored.append((score * 2, "MASTER KNOWLEDGE BASE", text[:10000]))
        except Exception:
            pass

    # 3. Score library files (papers converted to markdown)
    lib_dirs = []
    if project and project != "INCOMING":
        ld = PROJECTS / project / "01-LIBRARY"
        if ld.exists():
            lib_dirs.append((project, ld))
    else:
        for proj in sorted(PROJECTS.iterdir()):
            if proj.is_dir() and not proj.name.startswith("00-"):
                ld = proj / "01-LIBRARY"
                if ld.exists():
                    lib_dirs.append((proj.name, ld))

    for proj_name, lib_dir in lib_dirs:
        for f in lib_dir.glob("*.md"):
            try:
                text = f.read_text(encoding="utf-8", errors="ignore")
                text_lower = text.lower()
                score = sum(1 for w in query_words if w in text_lower)
                if any(w in f.stem.lower() for w in query_words):
                    score += 2
                if score > 0:
                    scored.append((score, f"[{proj_name}] {f.stem}", text[:6000]))
            except Exception:
                continue

    # 4. Score system core files (.md and .json)
    for ext in ["*.md", "*.json"]:
        for f in CORE.glob(ext):
            if f.name == "MASTER-KNOWLEDGE-BASE.md":
                continue
            try:
                text = f.read_text(encoding="utf-8", errors="ignore")
                text_lower = text.lower()
                score = sum(1 for w in query_words if w in text_lower)
                if score > 0:
                    label = f"00-SYSTEM-CORE/{f.stem}"
                    scored.append((score, label, text[:5000]))
            except Exception:
                continue

    # 5. Score project manifest files
    for proj in sorted(PROJECTS.iterdir()):
        if not proj.is_dir() or proj.name.startswith("00-"):
            continue
        mf = proj / "99-META" / "PROJECT-MANIFEST.md"
        if mf.exists():
            try:
                text = mf.read_text(encoding="utf-8", errors="ignore")
                text_lower = text.lower()
                score = sum(1 for w in query_words if w in text_lower)
                if score > 0:
                    scored.append((score, f"[{proj.name}] PROJECT-MANIFEST", text[:3000]))
            except Exception:
                continue

    # Sort by score descending, take top matches
    scored.sort(key=lambda x: -x[0])
    context_sections = []
    used_chars = 0

    for score, label, content in scored:
        if used_chars >= max_chars:
            break
        chunk = content[:max_chars - used_chars]
        context_sections.append(f"### {label}\n{chunk}")
        used_chars += len(chunk)

    if not context_sections:
        return ""

    return "\n\n---\n## RELEVANT RESEARCH CONTENT (from project files)\n\n" + "\n\n".join(context_sections) + "\n\n---\n"

# ─── System prompt ────────────────────────────────────────────────────────────
ResearchPilot_SYSTEM = """You are ResearchPilot — v2.0.
You have FULL ACCESS to the user's research files via built-in tools.

AVAILABLE TOOLS (call them whenever you need file data):
- read_file(path): Read ANY file in the research system. Path is relative to ResearchPilot root.
- search_files(query): Search all files for matching text.
- list_directory(path): List files in any directory.
- get_project_list(): List all research projects with stats.
- read_knowledge_base(): Read the Master Knowledge Base (synthesis of ALL papers).
- read_extractions_list(project): List extraction files for a project.
- read_extraction(project, filename): Read a specific 12-point extraction.
- read_project_manifest(project): Read a project's manifest (goals, status).
- get_system_structure(): Get the full ResearchPilot folder structure.
- read_system_core(filename): Read any system file (protocols, specs, etc.).

IMPORTANT: Use these tools proactively to answer questions. Do NOT guess — read the actual files.

RULES (always apply):
- Zero hallucination: use ONLY the content you read from files.
- When quoting, use exact text in "quotation marks" with source reference.
- Academic rigor: cite APA format. No outside knowledge for research claims.
- Be helpful, clear, and direct.
STRUCTURE: 00-SYSTEM-CORE/ | 01-PROJECTS/ | 99-SYSTEM-BACKEND/chats/"""

def build_rag_prompt(query: str, project: str = None, skills: list = None) -> str:
    """Build a RAG-enhanced system prompt with relevant file content for the query."""
    # Base instructions
    prompt = ResearchPilot_SYSTEM
    if skills:
        for sk in skills:
            sf = SKILLS_DIR / sk
            if sf.exists():
                prompt += f"\n\n## Skill: {sk}\n{sf.read_text(encoding='utf-8')}"
    # Inject relevant context from all files
    context = retrieve_relevant_context(query, project)
    if context:
        prompt += context
    # Add project structure info
    prompt += "\n\n## ResearchPilot FOLDER STRUCTURE\n- 00-SYSTEM-CORE/: System files, protocols, master knowledge base\n- 01-PROJECTS/[PROJECT]/01-LIBRARY/: Paper PDFs and converted markdown\n- 01-PROJECTS/[PROJECT]/02-EXTRACTIONS/: 12-point paper extractions\n- 01-PROJECTS/[PROJECT]/99-META/: Project manifests, connections, notes"
    return prompt

# ─── SSRF Guard ──────────────────────────────────────────────────────────────
_PRIVATE_RANGES = (
    "127.", "10.", "169.254.", "172.16.", "172.17.", "172.18.", "172.19.",
    "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.",
    "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.",
    "192.168.", "0.", "::1", "::ffff:",
)
def _validate_engine_url(url: str):
    """Reject SSRF-prone URLs: private IPs, non-https schemes, file/gopher."""
    if not url:
        return
    import urllib.parse
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Disallowed URL scheme: {parsed.scheme}")
    host = parsed.hostname or ""
    host_lower = host.lower()
    if host_lower in ("localhost", "localhost.localdomain"):
        return  # localhost is OK for Ollama/LM Studio
    for prefix in _PRIVATE_RANGES:
        if host_lower.startswith(prefix):
            raise ValueError(f"Private IP range not allowed: {host}")

# ─── Multi-AI Router ──────────────────────────────────────────────────────────
async def _try_ollama(engine: dict, messages: list) -> tuple[str, list]:
    async with httpx.AsyncClient(timeout=300.0) as c:
        # Fast health check — failover if not reachable within 3s
        r = await c.get(f"{engine['url']}/api/tags", timeout=3.0)
        if r.status_code != 200:
            raise Exception("Ollama not reachable")

        model = engine["model"]

        # Quick model info check
        model_ctx = 8192
        try:
            r2 = await c.post(f"{engine['url']}/api/show", json={"name": model}, timeout=3.0)
            if r2.status_code == 200:
                info = r2.json()
                if "modelfile" in info:
                    for line in info["modelfile"].split("\n"):
                        if "num_ctx" in line.lower():
                            parts = line.split()
                            if len(parts) >= 2:
                                model_ctx = int(parts[-1])
                                break
        except Exception:
            pass

        tool_uses = []
        for iteration in range(3):
            payload = {
                "model": model,
                "messages": messages,
                "stream": False,
                "options": {"num_ctx": min(model_ctx, 64000)}
            }

            if iteration == 0:
                payload["tools"] = ResearchPilot_TOOLS

            r = await c.post(f"{engine['url']}/api/chat", json=payload, timeout=120.0)
            if r.status_code != 200:
                err = ""
                try: err = r.json().get("error", r.text[:200])
                except: err = r.text[:200]
                raise Exception(f"Ollama returned {r.status_code}: {err}")
            data = r.json()
            msg = data.get("message", {})

            tool_calls = msg.get("tool_calls", [])
            if tool_calls:
                messages.append({"role": "assistant", "content": msg.get("content", ""), "tool_calls": tool_calls})
                for tc in tool_calls:
                    fn = tc["function"]["name"]
                    fn_args = tc["function"]["arguments"]
                    if isinstance(fn_args, str):
                        try:
                            fn_args = json.loads(fn_args)
                        except json.JSONDecodeError:
                            fn_args = {}
                    result = await execute_tool(fn, fn_args)
                    status = "ok" if "error" not in result else "error"
                    tool_uses.append({"tool": fn, "args": fn_args, "status": status})
                    content_str = json.dumps(result, ensure_ascii=False)
                    messages.append({"role": "tool", "content": content_str, "name": fn})
                continue

            content = msg.get("content", "")
            return content, tool_uses

        return "I read several files but couldn't formulate a complete response. Please try asking more specifically.", tool_uses

async def _try_openai_compat(engine: dict, messages: list) -> tuple[str, list]:
    # Fail fast if no API key
    api_key = engine.get("api_key", "")
    if not api_key or api_key in ("", "lm-studio"):
        raise Exception(f"{engine.get('name','OpenAI')}: no API key configured")

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    # Add OpenRouter identity headers if using OpenRouter
    if "openrouter" in engine.get("url", "").lower():
        headers["HTTP-Referer"] = "https://github.com/ResearchPilot"
        headers["X-Title"] = "ResearchPilot"

    # Quick health check — try a models list request
    async with httpx.AsyncClient(timeout=10.0) as c:
        try:
            hr = await c.get(f"{engine['url']}/models", timeout=3.0)
        except Exception:
            pass  # not all APIs support /models; proceed anyway

    tool_uses = []
    async with httpx.AsyncClient(timeout=300.0) as c:
        for iteration in range(3):
            payload = {
                "model": engine["model"],
                "messages": messages,
                "max_tokens": 8192,
            }
            if iteration == 0:
                payload["tools"] = ResearchPilot_TOOLS

            r = await c.post(
                f"{engine['url']}/chat/completions",
                json=payload,
                headers=headers,
                timeout=60.0
            )
            if r.status_code != 200:
                err = ""
                try: err = r.json().get("error", {}).get("message", r.text[:200])
                except: err = r.text[:200]
                raise Exception(f"{engine.get('name','API')} returned {r.status_code}: {err}")
            data = r.json()
            msg = data.get("choices", [{}])[0].get("message", {})

            # Check for tool calls
            tool_calls = msg.get("tool_calls", [])
            if tool_calls:
                messages.append({
                    "role": "assistant",
                    "content": msg.get("content") or "",
                    "tool_calls": tool_calls
                })
                for tc in tool_calls:
                    fn = tc["function"]["name"]
                    fn_args = tc["function"]["arguments"]
                    if isinstance(fn_args, str):
                        try:
                            fn_args = json.loads(fn_args)
                        except json.JSONDecodeError:
                            fn_args = {}
                    result = await execute_tool(fn, fn_args)
                    status = "ok" if "error" not in result else "error"
                    tool_uses.append({"tool": fn, "args": fn_args, "status": status})
                    content_str = json.dumps(result, ensure_ascii=False)
                    messages.append({
                        "role": "tool",
                        "content": content_str,
                        "name": fn,
                        "tool_call_id": tc.get("id", "")
                    })
                continue

            content = msg.get("content") or ""
            return content, tool_uses

    return "I read several files but couldn't formulate a complete response.", tool_uses

async def _try_gemini(engine: dict, messages: list) -> tuple[str, list]:
    key = engine.get("api_key", "") or os.getenv("GEMINI_API_KEY", "")
    if not key:
        raise Exception("No Gemini API key")
    contents = []
    for m in messages:
        if m["role"] == "system":
            continue
        role = "user" if m["role"] == "user" else "model"
        contents.append({"role": role, "parts": [{"text": m["content"]}]})
    sys_msgs = [m for m in messages if m["role"] == "system"]
    if sys_msgs:
        contents.insert(0, {"role": "user", "parts": [{"text": sys_msgs[0]["content"]}]})
        contents.insert(1, {"role": "model", "parts": [{"text": "Understood. I will follow these instructions."}]})
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{engine['model']}:generateContent?key={key}"
    async with httpx.AsyncClient(timeout=60.0) as c:
        r = await c.post(url, json={"contents": contents, "generationConfig": {"maxOutputTokens": 8192}}, timeout=120.0)
        return r.json()["candidates"][0]["content"]["parts"][0]["text"], []

async def _try_anthropic(engine: dict, messages: list) -> tuple[str, list]:
    key = engine.get("api_key", "") or os.getenv("ANTHROPIC_API_KEY", "")
    if not key:
        raise Exception("No Anthropic API key")
    system_text = next((m["content"] for m in messages if m["role"] == "system"), ResearchPilot_SYSTEM)
    chat_msgs = [m for m in messages if m["role"] != "system"]
    headers = {"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"}
    payload = {"model": engine["model"], "max_tokens": 8192, "system": system_text, "messages": chat_msgs}
    async with httpx.AsyncClient(timeout=120.0) as c:
        r = await c.post("https://api.anthropic.com/v1/messages", json=payload, headers=headers, timeout=120.0)
        return r.json()["content"][0]["text"], []

async def _try_claude_plugin(engine: dict, messages: list) -> tuple[str, list]:
    """Claude plugin: tries claude CLI first, then Anthropic API as fallback."""
    tool_uses = []

    # Try Claude Code CLI first (requires `claude` installed and logged in)
    try:
        import subprocess
        system_text = next((m["content"] for m in messages if m["role"] == "system"), ResearchPilot_SYSTEM)
        chat_msgs = [m for m in messages if m["role"] != "system"]
        user_msg = next((m["content"] for m in reversed(chat_msgs) if m["role"] == "user"), "")
        prompt = f"{system_text}\n\nUser: {user_msg}"
        r = subprocess.run(
            ["claude", "-p", prompt[:16000]],
            capture_output=True, text=True, timeout=120
        )
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()[:4000], tool_uses
    except (FileNotFoundError, subprocess.TimeoutExpired, Exception):
        pass

    # Fallback: try the `anthropic` Python SDK
    if HAS_ANTHROPIC:
        try:
            key = engine.get("api_key", "") or os.getenv("ANTHROPIC_API_KEY", "")
            if not key:
                raise Exception("No Anthropic API key")
            client = _anthropic.Anthropic(api_key=key)
            system_text = next((m["content"] for m in messages if m["role"] == "system"), ResearchPilot_SYSTEM)
            chat_msgs = [m for m in messages if m["role"] != "system"]
            api_msgs = []
            for m in chat_msgs:
                if m["role"] in ("user", "assistant"):
                    api_msgs.append({"role": m["role"], "content": m["content"]})
            r = client.messages.create(
                model=engine.get("model", "claude-sonnet-4-20250514"),
                max_tokens=4096,
                system=system_text[:10000],
                messages=api_msgs[-10:]
            )
            return r.content[0].text, tool_uses
        except Exception:
            pass

    raise Exception("Claude not available. Install CLI: 'pip install claude-cli' or add API key.")

ENGINE_HANDLERS = {
    "ollama": _try_ollama,
    "openai_compat": _try_openai_compat,
    "gemini": _try_gemini,
    "anthropic": _try_anthropic,
    "claude_plugin": _try_claude_plugin,
}

async def ai_respond(messages: list, project: str = None, skills: list = None) -> tuple[str, str, list]:
    """Try all enabled engines in priority order. Never returns empty. Returns (text, engine_name, tool_uses)."""
    cfg = load_settings()
    engines = sorted(
        [e for e in cfg["ai_engines"] if e.get("enabled", False)],
        key=lambda x: x.get("priority", 99)
    )
    # Extract the last user query for RAG context retrieval
    user_query = ""
    for m in reversed(messages):
        if m.get("role") == "user":
            user_query = m.get("content", "")
            break
    # Build RAG-enhanced system prompt with relevant file context
    sys_prompt = build_rag_prompt(user_query, project, skills)
    full_msgs = [{"role": "system", "content": sys_prompt}] + \
                [m for m in messages if m.get("role") != "system"]

    errors = []
    for engine in engines:
        handler = ENGINE_HANDLERS.get(engine["type"])
        if not handler:
            continue
        try:
            result, tool_uses = await handler(engine, full_msgs)
            if result and result.strip():
                return result, engine["name"], tool_uses
        except Exception as e:
            errors.append(f"{engine['name']}: {str(e)[:80]}")
            continue

    if errors:
        return (
            f"⚠️ ResearchPilot could not reach any AI engine. Tried:\n" +
            "\n".join(f"  • {e}" for e in errors) +
            "\n\n**To fix:** Go to ⚙️ Settings → AI Engines and enable/configure at least one engine.",
            "none",
            []
        )
    return (
        "⚠️ No AI engines are enabled.\n\nGo to ⚙️ Settings → AI Engines to enable Ollama, Gemini, Claude, or any free API.",
        "none",
        []
    )

# ─── Universal File → Markdown ────────────────────────────────────────────────
def _check_docling():
    global HAS_DOCLING
    if HAS_DOCLING is None:
        try:
            from docling.document_converter import DocumentConverter
            globals()["_docling_converter"] = DocumentConverter
            HAS_DOCLING = True
        except ImportError:
            HAS_DOCLING = False

def file_to_markdown(path: Path) -> str:
    """Convert any supported file to markdown text. Uses docling for PDFs."""
    ext = path.suffix.lower()

    if ext == ".pdf":
        _check_docling()
        if HAS_DOCLING:
            try:
                converter = _docling_converter()
                result = converter.convert(str(path))
                return result.document.export_to_markdown()
            except Exception:
                pass  # fallback to fitz
        doc = fitz.open(str(path))
        pages = [page.get_text() for page in doc]
        doc.close()
        return "\n\n".join(pages)

    if ext in (".docx", ".doc") and HAS_DOCX:
        doc = DocxDoc(str(path))
        parts = []
        for para in doc.paragraphs:
            if para.style.name.startswith("Heading"):
                lvl = para.style.name.split()[-1] if para.style.name.split()[-1].isdigit() else "1"
                parts.append(f"{'#' * int(lvl)} {para.text}")
            elif para.text.strip():
                parts.append(para.text)
        return "\n\n".join(parts)

    if ext in (".pptx", ".ppt") and HAS_PPTX:
        prs = PptxPres(str(path))
        parts = []
        for i, slide in enumerate(prs.slides, 1):
            parts.append(f"## Slide {i}")
            for shape in slide.shapes:
                if hasattr(shape, "text") and shape.text.strip():
                    parts.append(shape.text.strip())
        return "\n\n".join(parts)

    if ext in (".html", ".htm"):
        h = html2text.HTML2Text()
        h.ignore_links = False
        return h.handle(path.read_text(encoding="utf-8", errors="ignore"))

    if ext in (".txt", ".md", ".csv", ".json", ".yaml", ".yml"):
        return path.read_text(encoding="utf-8", errors="ignore")

    return f"[Unsupported file type: {ext}. Content not extracted.]"

def save_as_md(source_path: Path, dest_folder: Path, extra_meta: str = "") -> Path:
    """Convert file and save as .md alongside original."""
    dest_folder.mkdir(parents=True, exist_ok=True)
    md_name = source_path.stem + ".md"
    md_path = dest_folder / md_name
    text = file_to_markdown(source_path)
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    md_path.write_text(
        f"# {source_path.stem}\n"
        f"*Source: `{source_path.name}` | Imported: {ts}*\n"
        f"{extra_meta}\n\n---\n\n{text}\n",
        encoding="utf-8"
    )
    return md_path

# ─── Chat persistence ──────────────────────────────────────────────────────────
def chat_path(session_id: str) -> Path:
    return CHATS_DIR / f"{session_id}.md"

def load_chat_messages(session_id: str) -> list:
    p = chat_path(session_id)
    if not p.exists():
        return []
    messages, cur_role, cur_lines = [], None, []
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.startswith("### 👤 You"):
            if cur_role:
                messages.append({"role": cur_role, "content": "\n".join(cur_lines).strip()})
            cur_role, cur_lines = "user", []
        elif line.startswith("### 🤖 ERA") or line.startswith("### 🤖 AI Research Assistant") or line.startswith("### 🤖 ResearchPilot"):
            if cur_role:
                messages.append({"role": cur_role, "content": "\n".join(cur_lines).strip()})
            cur_role, cur_lines = "assistant", []
        elif cur_role is not None:
            cur_lines.append(line)
    if cur_role:
        messages.append({"role": cur_role, "content": "\n".join(cur_lines).strip()})
    return messages

def append_to_chat(session_id: str, role: str, content: str, engine: str = "", project: str = ""):
    p = chat_path(session_id)
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not p.exists():
        tags = "#ResearchPilot #research #chat"
        proj_line = ""
        if project:
            tags += f" #{project}"
            proj_line = f"*Project: {project}*\n"
        p.write_text(
            f"# ResearchPilot Chat: {session_id}\n"
            f"*Started: {ts}*\n"
            f"{proj_line}"
            f"Tags: {tags}\n\n---\n\n",
            encoding="utf-8"
        )
    icon = "👤 You" if role == "user" else f"🤖 ResearchPilot ({engine})"
    with open(p, "a", encoding="utf-8") as f:
        f.write(f"\n### {icon}\n*{ts}*\n\n{content}\n\n---\n")

# ─── PDF 12-point extraction ──────────────────────────────────────────────────
def extract_pdf_text(path: Path, max_chars: int = 40000) -> str:
    text = file_to_markdown(path)
    return text[:max_chars]

# ─── FastAPI App ──────────────────────────────────────────────────────────────
app = FastAPI(title="ResearchPilot", version="2.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory=str(STATIC)), name="static")

# ─── Auth middleware ──────────────────────────────────────────────────────────
from fastapi import Request as _Req
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse as _JSONResp

SKIP_AUTH_PATHS = ("/static/", "/docs", "/redoc", "/openapi.json")

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: _Req, call_next):
        path = request.url.path
        # Skip static files, docs, and the root page
        if any(path.startswith(p) for p in SKIP_AUTH_PATHS):
            return await call_next(request)
        if path == "/":
            return await call_next(request)
        # Short-circuit OPTIONS (CORS preflight)
        if request.method == "OPTIONS":
            return await call_next(request)
        # Require Bearer token on all other requests
        auth = request.headers.get("Authorization", "")
        if not auth.startswith("Bearer ") or auth[7:] != AUTH_TOKEN:
            return _JSONResp({"error": "Unauthorized — restart the server and refresh the page"}, status_code=401)
        return await call_next(request)

app.add_middleware(AuthMiddleware)

@app.get("/", response_class=HTMLResponse)
async def root():
    html = Path(STATIC / "index.html").read_text(encoding="utf-8")
    # Inject auth token for frontend to use
    token_script = f'<script>window.__AUTH_TOKEN__="{AUTH_TOKEN}";</script>'
    html = html.replace("</head>", f"{token_script}</head>")
    return HTMLResponse(html)

# ── Settings ──
@app.get("/api/settings")
async def get_settings():
    return load_settings()

def strip_html(val):
    if isinstance(val, str):
        return val.replace("<", "&lt;").replace(">", "&gt;")
    if isinstance(val, dict):
        return {k: strip_html(v) for k, v in val.items()}
    if isinstance(val, list):
        return [strip_html(v) for v in val]
    return val

@app.post("/api/settings")
async def update_settings(request: Request):
    data = await request.json()
    if not isinstance(data, dict):
        raise HTTPException(400, "Invalid settings data")
    data = strip_html(data)
    save_settings(data)
    return {"ok": True}

# ── Author ──
AUTHOR_FILE = CORE / "author.json"
VERSIONS_FILE = CORE / "versions.json"

@app.get("/api/settings/author")
async def get_author():
    if AUTHOR_FILE.exists():
        try:
            d = json.loads(AUTHOR_FILE.read_text(encoding="utf-8"))
            has_pw = bool(d.pop("_password_hash", ""))
            d["has_password"] = has_pw
            return d
        except Exception:
            pass
    return {"name": "", "title": "", "phd": "", "masters": "", "copyright": "", "has_password": False}

@app.post("/api/settings/author")
async def save_author(request: Request):
    data = await request.json()
    if not isinstance(data, dict):
        raise HTTPException(400, "Invalid data")
    # Load existing to preserve password hash
    existing = {}
    if AUTHOR_FILE.exists():
        try: existing = json.loads(AUTHOR_FILE.read_text(encoding="utf-8"))
        except: pass
    # Only save if password is verified or being set
    pw = data.pop("admin_password", "")
    is_setting_pw = data.pop("_setting_password", False)
    if is_setting_pw:
        existing["_password_hash"] = hashlib.sha256(pw.encode()).hexdigest()
    else:
        stored_hash = existing.get("_password_hash", "")
        if stored_hash:
            if hashlib.sha256(pw.encode()).hexdigest() != stored_hash:
                raise HTTPException(403, "Incorrect admin password")
    # Merge fields with length limits
    for k in ("name", "title", "phd", "masters", "copyright"):
        if k in data and isinstance(data[k], str):
            existing[k] = data[k][:2000]
    AUTHOR_FILE.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    return {"ok": True}

@app.post("/api/settings/author/verify")
async def verify_author_password(request: Request):
    """Verify admin password without saving any data."""
    data = await request.json()
    pw = data.get("password", "")
    existing = {}
    if AUTHOR_FILE.exists():
        try: existing = json.loads(AUTHOR_FILE.read_text(encoding="utf-8"))
        except: pass
    stored_hash = existing.get("_password_hash", "")
    if not stored_hash:
        return {"ok": True, "has_password": False}  # No password set = always OK
    import hashlib
    if hashlib.sha256(pw.encode()).hexdigest() == stored_hash:
        return {"ok": True, "has_password": True}
    return {"ok": False, "has_password": True}

@app.get("/api/settings/versions")
async def get_versions():
    if VERSIONS_FILE.exists():
        try: return json.loads(VERSIONS_FILE.read_text(encoding="utf-8"))
        except: pass
    return {"versions": []}

@app.post("/api/settings/versions")
async def update_versions(request: Request):
    data = await request.json()
    action = data.get("action", "add")
    current = {"versions": []}
    if VERSIONS_FILE.exists():
        try: current = json.loads(VERSIONS_FILE.read_text(encoding="utf-8"))
        except: pass
    if action == "add":
        current.setdefault("versions", []).append({
            "date": data.get("date", ""),
            "version": data.get("version", ""),
            "description": data.get("description", "")
        })
    elif action == "remove":
        date = data.get("date", "")
        desc = data.get("description", "")
        current["versions"] = [v for v in current.get("versions", [])
                               if not (v.get("date") == date and v.get("description", "")[:50] == desc[:50])]
    VERSIONS_FILE.write_text(json.dumps(current, indent=2, ensure_ascii=False), encoding="utf-8")
    return {"ok": True}

@app.post("/api/auto-start")
async def toggle_auto_start(request: Request):
    """Enable/disable Windows auto-start via scheduled task."""
    data = await request.json()
    enabled = data.get("enabled", False)
    import subprocess
    try:
        if enabled:
            bat_path = str(BASE / "start-research.bat")
            r = subprocess.run(
                ["schtasks", "/create", "/tn", "ResearchPilot-ResearchAssistant",
                 "/tr", bat_path, "/sc", "ONLOGON", "/ru", os.environ.get("USERNAME", ""), "/f"],
                capture_output=True, text=True, timeout=10
            )
            ok = r.returncode == 0
        else:
            r = subprocess.run(
                ["schtasks", "/delete", "/tn", "ResearchPilot-ResearchAssistant", "/f"],
                capture_output=True, text=True, timeout=10
            )
            ok = r.returncode == 0
    except Exception as e:
        return {"ok": False, "error": str(e), "enabled": False}
    cfg = load_settings()
    cfg["auto_start"] = enabled
    save_settings(cfg)
    return {"ok": ok, "enabled": enabled}

@app.get("/api/auto-start")
async def get_auto_start():
    """Check if auto-start is configured."""
    import subprocess
    try:
        r = subprocess.run(
            ["schtasks", "/query", "/tn", "ResearchPilot-ResearchAssistant", "/fo", "LIST"],
            capture_output=True, text=True, timeout=5
        )
        exists = r.returncode == 0
    except Exception:
        exists = False
    # Also check Startup folder shortcut
    startup_shortcut = Path(os.environ.get("APPDATA", "")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup" / "ResearchPilot-ResearchAssistant.lnk"
    shortcut_exists = startup_shortcut.exists()
    cfg = load_settings()
    enabled = cfg.get("auto_start", False)
    method = "task" if exists else ("startup_folder" if shortcut_exists else None)
    return {"enabled": enabled or shortcut_exists, "task_exists": exists, "shortcut_exists": shortcut_exists, "method": method}

# ── Plugin Management ──
PLUGIN_REGISTRY = {
    "claude": {
        "id": "claude",
        "name": "Claude AI",
        "icon": "🤖",
        "description": "Connect your Anthropic API key to use Claude models (Sonnet, Haiku). Get key at console.anthropic.com",
        "docs_url": "https://console.anthropic.com",
        "type": "anthropic"
    },
    "claude_login": {
        "id": "claude_login",
        "name": "Claude Login",
        "icon": "🔐",
        "description": "Login with your paid Claude account. Requires 'claude' CLI: pip install claude-cli && claude login",
        "docs_url": "https://claude.ai",
        "type": "claude_plugin"
    },
    "gemini": {
        "id": "gemini",
        "name": "Google Gemini",
        "icon": "🔮",
        "description": "Free tier Gemini Flash model. Get key at aistudio.google.com",
        "docs_url": "https://aistudio.google.com/app/apikey",
        "type": "gemini"
    },
    "ollama": {
        "id": "ollama",
        "name": "Ollama (Local)",
        "icon": "🦙",
        "description": "Free local AI models. Install from ollama.com, pull a model like llama3 or qwen2.5",
        "docs_url": "https://ollama.com",
        "type": "ollama"
    }
}

@app.get("/api/plugins")
async def list_plugins():
    """List all available engine plugins and their connection status."""
    cfg = load_settings()
    engines = cfg.get("ai_engines", [])
    result = []
    for pid, info in PLUGIN_REGISTRY.items():
        engine = next((e for e in engines if e.get("type") == info["type"]), None)
        connected = engine is not None and engine.get("enabled", False)
        if engine and engine.get("api_key"):
            connected = True
        # Check Claude CLI availability
        cli_available = False
        if pid == "claude_login":
            try:
                import subprocess
                r = subprocess.run(["claude", "--version"], capture_output=True, text=True, timeout=5)
                cli_available = r.returncode == 0
            except Exception:
                pass
        result.append({
            "id": pid,
            "name": info["name"],
            "icon": info["icon"],
            "description": info["description"],
            "connected": connected,
            "cli_available": cli_available,
            "docs_url": info["docs_url"],
            "type": info["type"]
        })
    return {"plugins": result}

@app.post("/api/plugins/{plugin_id}/connect")
async def connect_plugin(plugin_id: str, request: Request):
    """Connect a plugin by saving its API key and enabling the engine."""
    data = await request.json()
    api_key = data.get("api_key", "")
    plugin = PLUGIN_REGISTRY.get(plugin_id)
    if not plugin:
        raise HTTPException(404, "Plugin not found")
    cfg = load_settings()
    engines = cfg.get("ai_engines", [])
    existing = next((e for e in engines if e.get("type") == plugin["type"]), None)
    if existing:
        existing["api_key"] = api_key
        existing["enabled"] = True
    else:
        engines.append({
            "name": plugin["name"],
            "type": plugin["type"],
            "url": "",
            "model": "claude-sonnet-4-20250514" if plugin["type"] == "anthropic" else "gemini-1.5-flash" if plugin["type"] == "gemini" else "",
            "api_key": api_key,
            "enabled": True,
            "priority": len(engines) + 1,
            "note": f"Connected via plugin: {plugin['name']}"
        })
    cfg["ai_engines"] = engines
    save_settings(cfg)
    return {"ok": True, "plugin": plugin_id}

@app.post("/api/plugins/{plugin_id}/disconnect")
async def disconnect_plugin(plugin_id: str):
    """Disconnect a plugin by disabling its engine."""
    plugin = PLUGIN_REGISTRY.get(plugin_id)
    if not plugin:
        raise HTTPException(404, "Plugin not found")
    cfg = load_settings()
    for e in cfg.get("ai_engines", []):
        if e.get("type") == plugin["type"]:
            e["enabled"] = False
            e["api_key"] = ""
    save_settings(cfg)
    return {"ok": True, "plugin": plugin_id}

# ── AI Status ──
@app.get("/api/status")
async def status():
    cfg = load_settings()
    engines_status = []
    for e in sorted(cfg["ai_engines"], key=lambda x: x.get("priority", 99)):
        if not e.get("enabled", False):
            engines_status.append({"name": e["name"], "status": "disabled"})
            continue
        # Quick ping
        ok = False
        try:
            if e["type"] == "ollama":
                async with httpx.AsyncClient(timeout=2.0) as c:
                    r = await c.get(f"{e['url']}/api/tags")
                    ok = r.status_code == 200
            elif e["type"] in ("openai_compat",):
                async with httpx.AsyncClient(timeout=2.0) as c:
                    r = await c.get(f"{e['url']}/models")
                    ok = r.status_code == 200
            elif e["type"] == "gemini":
                ok = bool(e.get("api_key") or os.getenv("GEMINI_API_KEY"))
            elif e["type"] == "anthropic":
                ok = bool(e.get("api_key") or os.getenv("ANTHROPIC_API_KEY"))
            elif e["type"] == "claude_plugin":
                ok = bool(e.get("api_key") or os.getenv("ANTHROPIC_API_KEY"))
                if not ok:
                    try:
                        import subprocess
                        r = subprocess.run(["claude", "--version"], capture_output=True, text=True, timeout=5)
                        ok = r.returncode == 0
                    except Exception:
                        ok = False
        except Exception:
            pass
        engines_status.append({"name": e["name"], "status": "online" if ok else "offline", "type": e["type"]})
    active = next((e["name"] for e in engines_status if e["status"] == "online"), "none")
    return {"engines": engines_status, "active": active}

# ── Projects ──
@app.get("/api/projects")
async def list_projects():
    result = []
    for p in sorted(PROJECTS.iterdir()):
        if not p.is_dir() or p.name.startswith("00-"):
            continue
        lib = p / "01-LIBRARY"
        ext = p / "02-EXTRACTIONS"
        pdf_count = len(list(lib.glob("*.*"))) if lib.exists() else 0
        ext_count = len(list(ext.glob("*.md"))) if ext.exists() else 0
        result.append({
            "id": p.name,
            "name": p.name,
            "papers": pdf_count,
            "extractions": ext_count,
        })
    return result

@app.post("/api/projects")
async def create_project(request: Request):
    data = await request.json()
    name = re.sub(r'[^\w\-]', '-', data.get("name", "NEW-PROJECT")).upper()
    proj_path = PROJECTS / name
    if proj_path.exists():
        raise HTTPException(400, "Project already exists")
    for folder in ["01-LIBRARY", "02-EXTRACTIONS", "03-MANUSCRIPTS", "99-META"]:
        (proj_path / folder).mkdir(parents=True, exist_ok=True)
    # Write manifest
    ts = datetime.datetime.now().strftime("%Y-%m-%d")
    (proj_path / "99-META" / "PROJECT-MANIFEST.md").write_text(
        f"# Project: {name}\n\nCreated: {ts}\n\nFocus: {data.get('focus','')}\nGoal: {data.get('goal','')}\n\n"
        f"## Status\n- [ ] Phase 1: Library\n- [ ] Phase 2: Extractions\n- [ ] Phase 3: Drafting\n- [ ] Phase 4: Submit\n",
        encoding="utf-8"
    )
    return {"ok": True, "id": name}

@app.delete("/api/projects/{project_id}")
async def delete_project(project_id: str):
    p = PROJECTS / project_id
    if not p.exists():
        raise HTTPException(404)
    shutil.rmtree(str(p))
    return {"ok": True}

@app.put("/api/projects/{project_id}")
async def rename_project(project_id: str, request: Request):
    """Rename a project folder + update all references across the system."""
    data = await request.json()
    new_name = re.sub(r'[^\w\-]', '-', data.get("new_name", "")).upper()
    if not new_name:
        raise HTTPException(400, "New name is required")
    old_path = PROJECTS / project_id
    new_path = PROJECTS / new_name
    if not old_path.exists():
        raise HTTPException(404, f"Project {project_id} not found")
    if new_path.exists():
        raise HTTPException(400, f"Project {new_name} already exists")

    # Rename folder
    old_path.rename(new_path)

    # Update keywords.json: replace old project paths with new
    kw_path = CORE / "keywords.json"
    if kw_path.exists():
        try:
            kw_data = json.loads(kw_path.read_text(encoding="utf-8"))
            changed = 0
            old_prefix = "01-PROJECTS\\" + project_id
            new_prefix = "01-PROJECTS\\" + new_name
            for word, v in kw_data.items():
                new_files = []
                for fp in v.get("files", []):
                    if fp.startswith(old_prefix):
                        new_files.append(fp.replace(old_prefix, new_prefix, 1))
                        changed += 1
                    else:
                        new_files.append(fp)
                v["files"] = new_files
            if changed:
                kw_path.write_text(json.dumps(kw_data, indent=2, ensure_ascii=False), encoding="utf-8")
        except Exception:
            pass

    return {"ok": True, "id": new_name}

# ── Library ──
@app.get("/api/library")
async def library(project: str = None):
    result = []
    def scan(folder: Path, proj_name: str):
        if not folder.exists():
            return
        for f in sorted(folder.iterdir()):
            if f.is_file() and not f.name.startswith("."):
                has_md = (folder / (f.stem + ".md")).exists()
                result.append({
                    "project": proj_name,
                    "filename": f.name,
                    "stem": f.stem,
                    "ext": f.suffix.lower(),
                    "size_kb": round(f.stat().st_size / 1024),
                    "has_md": has_md,
                    "modified": datetime.datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d")
                })
    for proj in sorted(PROJECTS.iterdir()):
        if not proj.is_dir() or proj.name.startswith("00-"):
            continue
        if project and proj.name != project:
            continue
        for subdir in ["01-LIBRARY", "02-EXTRACTIONS", "99-META"]:
            scan(proj / subdir, proj.name)
    scan(INCOMING, "INCOMING")
    return result

MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50MB
ALLOWED_MIME_TYPES = {
    "application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "text/html", "text/plain", "text/markdown", "text/csv",
    "application/json", "application/octet-stream",
}

def _check_mime(content: bytes) -> str:
    """Detect MIME type from content bytes. Returns empty string if python-magic not available."""
    try:
        import magic as _magic
        return _magic.from_buffer(content, mime=True)
    except ImportError:
        return ""  # skip check if python-magic not installed

def sanitize_filename(name: str) -> str:
    name = name.replace("..", "").replace("~", "")
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    return name.strip()

# ── Upload (any file type) ──
@app.post("/api/upload")
async def upload_file(
    file: UploadFile = File(...),
    project: str = Form(default="INCOMING")
):
    content = await file.read()
    if len(content) > MAX_UPLOAD_SIZE:
        raise HTTPException(413, "File too large (max 50MB)")
    mime = _check_mime(content)
    if mime and mime not in ALLOWED_MIME_TYPES:
        raise HTTPException(415, f"File type not allowed: {mime}")
    fname = sanitize_filename(file.filename or "uploaded_file")

    if project == "INCOMING":
        dest_folder = INCOMING
    else:
        dest_folder = PROJECTS / project / "01-LIBRARY"
        dest_folder.mkdir(parents=True, exist_ok=True)

    dest = dest_folder / fname
    if dest.exists():
        raise HTTPException(409, f"File already exists: {fname}")
    dest.write_bytes(content)

    # Auto-convert to markdown
    md_path = None
    try:
        md_path = save_as_md(dest, dest_folder, extra_meta=f"*Project: {project}*")
    except Exception as e:
        pass

    cfg = load_settings()
    return {
        "ok": True,
        "saved_to": str(dest),
        "md_created": str(md_path) if md_path else None,
        "size_kb": round(len(content) / 1024)
    }

# ── Upload folder (as new project) ──
@app.post("/api/upload-folder")
async def upload_folder(
    files: List[UploadFile] = File(...),
    project: str = Form(...)
):
    if len(files) > 100:
        raise HTTPException(413, "Too many files (max 100)")
    proj_path = PROJECTS / project
    lib = proj_path / "01-LIBRARY"
    lib.mkdir(parents=True, exist_ok=True)
    for folder in ["02-EXTRACTIONS", "03-MANUSCRIPTS", "99-META"]:
        (proj_path / folder).mkdir(exist_ok=True)
    results = []
    for f in files:
        content = await f.read()
        if len(content) > MAX_UPLOAD_SIZE:
            results.append({"file": f.filename, "error": "File too large (max 50MB)"})
            continue
        mime = _check_mime(content)
        if mime and mime not in ALLOWED_MIME_TYPES:
            results.append({"file": f.filename, "error": f"Type not allowed: {mime}"})
            continue
        fname = sanitize_filename(f.filename or "uploaded_file")
        dest = lib / fname
        if dest.exists():
            results.append({"file": fname, "error": "Already exists"})
            continue
        dest.write_bytes(content)
        try:
            md = save_as_md(dest, lib)
            results.append({"file": f.filename, "md": md.name})
        except Exception as e:
            results.append({"file": f.filename, "error": str(e)})
    return {"ok": True, "files": results}

# ── Move Library File (with .md companion) ──
@app.post("/api/library/move")
async def move_library_file(request: Request):
    data = await request.json()
    source_project = data.get("source_project", "")
    dest_project = data.get("dest_project", "")
    filename = data.get("filename", "")
    if not source_project or not dest_project or not filename:
        raise HTTPException(400, "source_project, dest_project, and filename are required")

    # Source
    if source_project == "INCOMING":
        src = INCOMING / filename
    else:
        src = PROJECTS / source_project / "01-LIBRARY" / filename
    if not src.exists():
        raise HTTPException(404, f"Source file not found: {source_project}/{filename}")

    # Destination
    if dest_project == "INCOMING":
        dst = INCOMING / filename
    else:
        dst = PROJECTS / dest_project / "01-LIBRARY" / filename
        dst.parent.mkdir(parents=True, exist_ok=True)

    if dst.exists():
        raise HTTPException(409, f"File already exists in {dest_project}: {filename}")

    shutil.move(str(src), str(dst))

    # Also move companion .md if it exists
    src_md = src.with_suffix(".md")
    dst_md = dst.with_suffix(".md")
    if src_md.exists():
        if dst_md.exists():
            dst_md.unlink()
        shutil.move(str(src_md), str(dst_md))

    return {"ok": True, "source": source_project, "destination": dest_project, "filename": filename}

# ── Delete Library File (with .md companion) ──
@app.delete("/api/library/{project}/{filename}")
async def delete_library_file(project: str, filename: str):
    fp = safe_project_path(project, "01-LIBRARY", filename)
    if not fp.exists():
        raise HTTPException(404, "File not found")

    md_fp = fp.with_suffix(".md")
    if md_fp.exists():
        md_fp.unlink()
    fp.unlink()

    return {"ok": True, "deleted": filename, "project": project}

# ── Extractions ──
@app.get("/api/extractions")
async def list_extractions(project: str = None):
    result = []
    for proj in sorted(PROJECTS.iterdir()):
        if not proj.is_dir() or proj.name.startswith("00-"):
            continue
        if project and proj.name != project:
            continue
        ext_dir = proj / "02-EXTRACTIONS"
        if ext_dir.exists():
            for md in sorted(ext_dir.glob("*.md")):
                result.append({
                    "project": proj.name,
                    "filename": md.name,
                    "size_kb": round(md.stat().st_size / 1024),
                    "modified": datetime.datetime.fromtimestamp(md.stat().st_mtime).strftime("%Y-%m-%d")
                })
    return result

@app.get("/api/extraction/{project}/{filename}")
async def get_extraction(project: str, filename: str):
    p = safe_project_path(project, "02-EXTRACTIONS", filename)
    if not p.exists():
        raise HTTPException(404)
    return {"content": p.read_text(encoding="utf-8")}

@app.delete("/api/extraction/{project}/{filename}")
async def delete_extraction(project: str, filename: str):
    p = safe_project_path(project, "02-EXTRACTIONS", filename)
    if not p.exists():
        raise HTTPException(404, "Extraction not found")
    p.unlink()
    return {"ok": True, "deleted": filename}

# ── Extract paper (12-point via AI) ──
class ExtractReq(BaseModel):
    project: str
    filename: str

@app.post("/api/extract")
async def extract_paper(req: ExtractReq):
    if req.project == "INCOMING":
        pdf_path = INCOMING / req.filename
    else:
        pdf_path = PROJECTS / req.project / "01-LIBRARY" / req.filename
    if not pdf_path.exists():
        raise HTTPException(404, "File not found")

    text = extract_pdf_text(pdf_path)
    prompt = (
        "Apply the full 12-Point Elite Extraction Protocol. Output structured markdown:\n"
        "1. APA Reference  2. DOI  3. Journal Name  4. Quartile Ranking (Q1/Q2/Q3/Q4)\n"
        "5. Indexing (Scopus/WoS)  6. Research Method  7. Theoretical Framework\n"
        "8. Exact Relevance  9. Section Support  10. Key Contribution\n"
        "11. Limitations  12. Classification (Behaviour/Governance/Technical/Essential)\n\n"
        f"Paper content:\n{text}"
    )
    messages = [{"role": "user", "content": prompt}]
    result, engine, _ = await ai_respond(messages, project=req.project)

    ext_dir = PROJECTS / req.project / "02-EXTRACTIONS" if req.project != "INCOMING" else INCOMING
    ext_dir.mkdir(exist_ok=True)
    existing = []
    for f in ext_dir.glob("P*.md"):
        mt = re.search(r"P(\d+)", f.stem)
        if mt:
            existing.append(int(mt.group(1)))
    code = f"P{(max(existing, default=0) + 1):03d}"
    out = ext_dir / f"{code} - {pdf_path.stem}.md"
    out.write_text(
        f"# {code} — {pdf_path.stem}\n"
        f"*Extracted: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} | Engine: {engine}*\n\n{result}\n",
        encoding="utf-8"
    )
    # Move from INCOMING to project library
    if req.project != "INCOMING" and (INCOMING / req.filename).exists():
        dest = PROJECTS / req.project / "01-LIBRARY" / req.filename
        dest.parent.mkdir(exist_ok=True)
        shutil.move(str(INCOMING / req.filename), str(dest))

    return {"ok": True, "code": code, "file": out.name, "engine": engine}

# ── Chat ──
class ChatReq(BaseModel):
    session_id: str
    message: str
    project: Optional[str] = None
    pdf_context: Optional[str] = None
    skills: Optional[List[str]] = None
    exclude_summary: Optional[bool] = False

@app.post("/api/chat")
async def chat(req: ChatReq):
    history = load_chat_messages(req.session_id)
    messages = history + [{"role": "user", "content": req.message}]

    # Parse /skillname commands from message — auto-load matching skills
    skill_names = set(req.skills or [])
    clean_msg = req.message
    for match in re.finditer(r'/([\w\-]+)', req.message):
        cmd = match.group(1).lower()
        skill_file = SKILLS_DIR / f"{cmd}.md"
        if skill_file.exists():
            skill_names.add(skill_file.name)
            clean_msg = clean_msg.replace(match.group(0), "").strip()
    req.skills = list(skill_names)
    req.message = clean_msg or req.message
    if clean_msg != req.message:
        messages[-1]["content"] = clean_msg or req.message

    # Inject PDF context if requested
    if req.pdf_context:
        for search_dir in [
            PROJECTS / req.project / "01-LIBRARY" if req.project and req.project != "INCOMING" else None,
            INCOMING
        ]:
            if search_dir and (search_dir / req.pdf_context).exists():
                txt = extract_pdf_text(search_dir / req.pdf_context)
                messages[-1]["content"] = (
                    f"[Using document: {req.pdf_context}]\n\n"
                    f"Document content:\n{txt}\n\n"
                    f"Question: {req.message}"
                )
                break

    append_to_chat(req.session_id, "user", req.message, project=req.project or "")

    # If exclude_summary, add instruction to avoid summary
    if req.exclude_summary and messages:
        for m in reversed(messages):
            if m.get("role") == "user":
                m["content"] = (
                    f"IMPORTANT: Provide a FULL, DETAILED response with all available information. "
                    f"Do NOT give a short summary. Be comprehensive and thorough.\n\n---\n\n"
                    f"{m['content']}"
                )
                break

    # Increase max_tokens for longer responses (handled per-engine)
    response, engine, tool_uses = await ai_respond(messages, project=req.project, skills=req.skills)
    append_to_chat(req.session_id, "assistant", response, engine)

    # Summarize tool usage for the response
    tools_summary = []
    for tu in tool_uses:
        t = tu.get("tool", "")
        a = tu.get("args", {})
        tools_summary.append({"tool": t, "args": a, "status": tu.get("status", "ok")})

    return {
        "response": response,
        "engine": engine,
        "session_id": req.session_id,
        "tools_used": tools_summary
    }

@app.post("/api/chat/new")
async def new_chat():
    sid = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    return {"session_id": sid}

@app.get("/api/chats")
async def list_chats():
    result = []
    for md in sorted(CHATS_DIR.glob("*.md"), reverse=True):
        project = ""
        try:
            first = md.read_text(encoding="utf-8", errors="ignore")[:300]
            pm = re.search(r'\*Project:\s*(.+?)\*', first)
            if pm:
                project = pm.group(1).strip()
        except Exception:
            pass
        result.append({
            "id": md.stem,
            "filename": md.name,
            "project": project,
            "modified": datetime.datetime.fromtimestamp(md.stat().st_mtime).strftime("%Y-%m-%d %H:%M"),
            "size_kb": round(md.stat().st_size / 1024, 1)
        })
    return result

@app.get("/api/chat/{session_id}")
async def get_chat(session_id: str):
    p = chat_path(session_id)
    if not p.exists():
        raise HTTPException(404)
    content = p.read_text(encoding="utf-8")
    project = ""
    try:
        pm = re.search(r'\*Project:\s*(.+?)\*', content[:300])
        if pm:
            project = pm.group(1).strip()
    except Exception:
        pass
    return {"content": content, "messages": load_chat_messages(session_id), "project": project}

@app.delete("/api/chat/{session_id}")
async def delete_chat(session_id: str):
    p = chat_path(session_id)
    if p.exists():
        p.unlink()
    return {"ok": True}

@app.post("/api/chat/{session_id}/clear")
async def clear_chat(session_id: str):
    """Clear the chat and archive it as a named .md file, then start fresh."""
    p = chat_path(session_id)
    if not p.exists():
        raise HTTPException(404, "Chat not found")

    content = p.read_text(encoding="utf-8")
    ts = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    archive_name = f"ARCHIVED-{session_id}.md"
    archive_path = CHATS_DIR / archive_name
    archive_path.write_text(
        f"# Archived Chat: {session_id}\n"
        f"*Archived: {ts}*\n"
        f"Tags: #ResearchPilot #research #chat #archived\n\n---\n\n"
        f"{content}\n",
        encoding="utf-8"
    )
    p.unlink()
    return {"ok": True, "archived_as": archive_name}

# ── Skills ──
@app.get("/api/skills")
async def list_skills():
    result = []
    for f in sorted(SKILLS_DIR.glob("*.md")):
        result.append({
            "name": f.name,
            "stem": f.stem,
            "size_kb": round(f.stat().st_size / 1024, 1),
            "preview": f.read_text(encoding="utf-8")[:200]
        })
    return result

@app.post("/api/skills")
async def save_skill(request: Request):
    data = await request.json()
    name = re.sub(r'[^\w\-]', '-', data["name"]) + ".md"
    (SKILLS_DIR / name).write_text(data["content"], encoding="utf-8")
    return {"ok": True, "name": name}

@app.delete("/api/skills/{name}")
async def delete_skill(name: str):
    p = SKILLS_DIR / name
    if p.exists():
        p.unlink()
    return {"ok": True}

# ── Tools API ──
class ToolExecReq(BaseModel):
    tool: str
    args: dict = {}

@app.post("/api/tools/execute")
async def api_execute_tool(req: ToolExecReq):
    """Execute a tool directly (for frontend or testing)."""
    result = await execute_tool(req.tool, req.args)
    return {"ok": "error" not in result, "result": result}

@app.get("/api/tools")
async def api_list_tools():
    """List all available tools with descriptions."""
    return {"tools": [
        {"name": t["function"]["name"], "description": t["function"]["description"]}
        for t in ResearchPilot_TOOLS
    ]}

# ── Knowledge Base ──
@app.get("/api/knowledge-base")
async def get_kb():
    kb = CORE / "MASTER-KNOWLEDGE-BASE.md"
    return {"content": kb.read_text(encoding="utf-8") if kb.exists() else "# Master Knowledge Base\n\n*Empty*"}

# ── Memory: All .md files (library + extractions) ──
@app.get("/api/memory")
async def list_memory():
    result = []
    # Library .md files
    for proj in sorted(PROJECTS.iterdir()):
        if not proj.is_dir() or proj.name.startswith("00-"):
            continue
        lib = proj / "01-LIBRARY"
        if lib.exists():
            for f in sorted(lib.glob("*.md")):
                result.append({
                    "source": "Library",
                    "project": proj.name,
                    "filename": f.name,
                    "size_kb": round(f.stat().st_size / 1024, 1),
                    "modified": datetime.datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d"),
                    "mode": "library"
                })
    # Extraction .md files
    for proj in sorted(PROJECTS.iterdir()):
        if not proj.is_dir() or proj.name.startswith("00-"):
            continue
        ext = proj / "02-EXTRACTIONS"
        if ext.exists():
            for f in sorted(ext.glob("*.md")):
                result.append({
                    "source": "Extraction",
                    "project": proj.name,
                    "filename": f.name,
                    "size_kb": round(f.stat().st_size / 1024, 1),
                    "modified": datetime.datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d"),
                    "mode": "extraction"
                })
    # INCOMING .md files
    if INCOMING.exists():
        for f in sorted(INCOMING.glob("*.md")):
            result.append({
                "source": "Library",
                "project": "INCOMING",
                "filename": f.name,
                "size_kb": round(f.stat().st_size / 1024, 1),
                "modified": datetime.datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d"),
                "mode": "library"
            })
    return result

@app.get("/api/file/{project}/{filename:path}")
async def get_file(project: str, filename: str):
    p = safe_project_path(project, "01-LIBRARY", filename)
    if not p.exists():
        alt = p.with_suffix(".md")
        if alt.exists():
            p = alt
        else:
            raise HTTPException(404, f"File not found: {project}/{filename}")
    if p.suffix.lower() not in (".md", ".txt", ".json", ".csv", ".yaml", ".html", ".htm"):
        return {"content": f"[Cannot preview binary file: {p.name}]"}
    return {"content": p.read_text(encoding="utf-8")}

# ── Graph: Multi-Dimension Knowledge Graph ──
GRAPHIFY_DIR = BASE / "graphify-out" / "cache" / "ast"

EXCLUDED_FILENAMES = {"readme.md", "session-summary.md", "connection.md", "project-manifest.md", "pdf-workflow.md", "reference-library.md", "project-changelog.md"}

def _cat(filepath: Path) -> str:
    p = str(filepath.resolve()).lower()
    if "99-system-backend" in p and "chats" in p: return "chat"
    if "02-extractions" in p: return "extraction"
    if "01-library" in p: return "research"
    if "00-system-core" in p: return "system"
    if "99-system-backend" in p: return "system"
    if "graphify-out" in p: return "system"
    if "99-meta" in p: return "system"
    if filepath.name.lower() in EXCLUDED_FILENAMES: return "system"
    if filepath.suffix in (".py", ".js", ".json", ".bat", ".ps1"): return "code"
    if filepath.suffix == ".md": return "research"
    return "other"

def _parse_metadata(text: str) -> dict:
    """Extract author, year, journal, quartile, method, framework from extraction .md."""
    meta = {"author": "", "year": "", "journal": "", "quartile": "", "method": "", "framework": "", "keyword": ""}
    m = re.search(r'\*\*APA Reference\*\*\s*:\s*(.+?)(?:\n|$)', text)
    if m:
        ref = m.group(1)
        ym = re.search(r'\((\d{4})\)', ref)
        if ym: meta["year"] = ym.group(1)
        am = re.match(r'([A-Z][a-zA-Z\-\xe9\xe8\xea\xeb\xe0\xe2\xec\xee\xf2\xf4\xf9\xfb\xe7\xe1]+)', ref)
        if am: meta["author"] = am.group(1).strip()
    m = re.search(r'\*\*Journal Name\*\*\s*:\s*(.+?)(?:\n|$)', text)
    if m: meta["journal"] = m.group(1).strip()
    m = re.search(r'\*\*Quartile Ranking\*\*\s*:\s*(.+?)(?:\n|$)', text)
    if m: meta["quartile"] = m.group(1).strip()
    m = re.search(r'\*\*Research Method\*\*\s*:\s*(.+?)(?:\n|$)', text)
    if m: meta["method"] = m.group(1).strip()
    m = re.search(r'\*\*Theoretical Framework\*\*\s*:\s*(.+?)(?:\n|$)', text)
    if m: meta["framework"] = m.group(1).strip()
    m = re.search(r'\*\*Keywords?\*\*\s*:\s*(.+?)(?:\n|$)', text)
    if m: meta["keyword"] = m.group(1).strip()
    return meta

def _scan_md_files() -> tuple:
    """Scan all .md research files, returning nodes + edges."""
    nodes, edges, seen = [], [], set()
    proj_files, file_meta = {}, {}

    for root in [CORE, BACKEND, INCOMING]:
        if root.exists():
            for f in root.rglob("*.md"):
                rel = str(f.relative_to(BASE)); cat = _cat(f); nid = f"file:{rel}"
                if nid not in seen:
                    seen.add(nid)
                    nodes.append({"id": nid, "label": f.name, "file_type": cat, "source_file": str(f), "source_location": "L1", "rel_path": rel})
                    if cat in ("research", "extraction"):
                        proj_files.setdefault("_".join(rel.split("\\")[:2]), []).append(nid)
    for root_dir in PROJECTS.iterdir():
        if not root_dir.is_dir() or root_dir.name.startswith("00-"): continue
        for sub in ["01-LIBRARY", "02-EXTRACTIONS", "99-META"]:
            d = root_dir / sub
            if d.exists():
                for f in d.rglob("*.md"):
                    rel = str(f.relative_to(BASE)); cat = _cat(f); nid = f"file:{rel}"
                    if nid not in seen:
                        seen.add(nid)
                        nodes.append({"id": nid, "label": f.name, "file_type": cat, "source_file": str(f), "source_location": "L1", "rel_path": rel})
                        proj_files.setdefault(root_dir.name, []).append(nid)
                    # Parse metadata + keywords for extraction/research files
                    if cat in ("research", "extraction"):
                            try:
                                txt = f.read_text(encoding="utf-8", errors="ignore")
                                file_meta[nid] = _parse_metadata(txt)
                            except: pass

    # Project cluster edges
    for pkey, flist in proj_files.items():
        for i in range(1, min(len(flist), 30)):
            edges.append({"source": flist[0], "target": flist[i], "relation": "same_project", "weight": 0.3, "source_file": pkey, "label": pkey, "source_location": ""})
    # Keyword edges: one edge per paper pair listing all shared keywords
    kw_data = _load_keywords()
    kw_to_files = {}
    for word, v in kw_data.items():
        for fp in v.get("files", []):
            nid = f"file:{fp}"
            if nid in file_meta:
                kw_to_files.setdefault(word, []).append(nid)
    pair_kws = {}
    for word, nids in kw_to_files.items():
        for i in range(len(nids)):
            for j in range(i + 1, len(nids)):
                pair = tuple(sorted([nids[i], nids[j]]))
                pair_kws.setdefault(pair, []).append(word)
    for (a, b), kws in pair_kws.items():
        cnt = len(kws)
        edges.append({"source": a, "target": b, "relation": "keyword", "weight": min(cnt / 10, 1.0), "label": "", "shared_keywords": ", ".join(sorted(kws)[:15]), "shared_kw_count": cnt, "source_file": ", ".join(sorted(kws)[:5]), "source_location": ""})
    return nodes, edges, file_meta

def _build_filter_edges(file_meta: dict, filter_by: str) -> list:
    """Build edges between research/extraction files based on filter dimension."""
    edges, seen_pairs = [], set()
    items = [(nid, m) for nid, m in file_meta.items() if m.get(filter_by)]
    if not items: return edges
    for i in range(len(items)):
        nid_i, mi = items[i]
        key = mi.get(filter_by, "")
        if not key: continue
        if filter_by == "year": key = key[:4]
        for j in range(i + 1, len(items)):
            nid_j, mj = items[j]
            if mi.get(filter_by) == mj.get(filter_by):
                pk = f"{nid_i}|{nid_j}"
                if pk not in seen_pairs:
                    seen_pairs.add(pk)
                    edges.append({"source": nid_i, "target": nid_j, "relation": filter_by, "weight": 1.0, "source_file": key, "source_location": ""})

    # Also add filter-value nodes for this dimension
    return edges

@app.get("/api/graph/filters")
async def get_graph_filters(context: str = ""):
    """Return available filter dimensions and their values from metadata.
    If context is provided (e.g. "year:2025"), only return values present
    in files matching that context filter.
    """
    _, _, file_meta = _scan_md_files()

    # Apply context filter if provided
    if context and context != "all":
        multi_layers = _parse_multi_layer_filter(context)
        matched_files = None
        for layer in multi_layers:
            dim = layer["dim"]
            val = layer["val"].lower().strip()
            op = layer.get("op", "AND")
            layer_matched = set()
            if dim == "keyword":
                kw_data = _load_keywords()
                for word, v in kw_data.items():
                    if word.lower().strip() == val:
                        for fp in v.get("files", []):
                            nid = f"file:{fp}"
                            if nid in file_meta:
                                layer_matched.add(nid)
                        break
            else:
                for nid, m in file_meta.items():
                    mv = m.get(dim, "").strip().lower()
                    if mv and val in mv:
                        layer_matched.add(nid)
            if matched_files is None:
                matched_files = layer_matched
            elif op == "AND":
                matched_files &= layer_matched
            else:
                matched_files |= layer_matched
        if matched_files is not None:
            file_meta = {nid: m for nid, m in file_meta.items() if nid in matched_files}

    dims = {"author": set(), "year": set(), "journal": set(), "quartile": set(), "method": set(), "framework": set()}
    for nid, m in file_meta.items():
        for d in dims:
            v = m.get(d, "").strip()
            if v:
                if d == "year": v = v[:4]
                dims[d].add(v)
    # Add keyword dimension from keywords.json
    kw_data = _load_keywords()
    kw_vals = sorted({w for w, v in kw_data.items() if v.get("files")})[:100]
    dims_list = [{"id": k, "label": k.capitalize(), "values": sorted(v) if v else []} for k, v in dims.items()]
    dims_list.append({"id": "keyword", "label": "Keyword", "values": kw_vals})
    return {"dimensions": dims_list}

def _parse_multi_layer_filter(filter_str: str):
    """Parse filter string into layers.
    Format: dim1:val1|AND:dim2:val2|OR:dim3:val3
    Returns list of {dim, val, op} where op is AND/OR (empty for first layer).
    """
    if not filter_str or filter_str == "all":
        return []
    parts = filter_str.split("|")
    layers = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        segs = p.split(":", 1)
        if len(segs) == 2:
            if segs[0] in ("AND", "OR"):
                sub = segs[1].split(":", 1)
                layers.append({"dim": sub[0], "val": sub[1] if len(sub) > 1 else "", "op": segs[0]})
            else:
                layers.append({"dim": segs[0], "val": segs[1], "op": ""})
    return layers

@app.get("/api/graph")
async def get_graph_data(filter: str = "all"):
    """Return graph data. filter=all|dim:val|AND:dim:val|..."""
    multi_layers = _parse_multi_layer_filter(filter)
    is_multi = bool(multi_layers)

    # 1. Code nodes from graphify cache
    code_nodes, code_edges = [], []
    if GRAPHIFY_DIR.exists():
        for f in sorted(GRAPHIFY_DIR.glob("*.json")):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                for n in data.get("nodes", []):
                    if isinstance(n, dict) and n.get("id") not in {x["id"] for x in code_nodes}:
                        src = n.get("source_file", "")
                        if n.get("file_type") == "code":
                            if "web-app" in src.lower(): n["file_type"] = "code"
                            elif "graphify-out" in src.lower() or ".claude" in src.lower(): n["file_type"] = "system"
                            else: n["file_type"] = "code"
                        code_nodes.append(n)
                code_edges.extend(data.get("edges", []))
            except: pass

    # 2. Research file nodes with metadata
    md_nodes, md_edges, file_meta = _scan_md_files()

    # If no multi-layer filter, use old single-filter logic
    if not is_multi:
        # Always exclude system/code/other from base node set — only show research papers
        keep_types = {"research", "extraction", "chat"}
        if filter == "keyword":
            keep_types.add("keyword")
        code_nodes = [n for n in code_nodes if n.get("file_type") in keep_types]
        md_nodes = [n for n in md_nodes if n.get("file_type") in keep_types]
        all_nodes = code_nodes + md_nodes
        filter_edges = []
        if filter == "all":
            filter_edges = list(md_edges)
        elif filter == "keyword":
            kw_data = _load_keywords()
            for word, v in kw_data.items():
                nid = f"keyword:{word}"
                all_nodes.append({"id": nid, "label": word, "file_type": "keyword", "source_file": str(KEYWORDS_FILE), "source_location": "L1", "rel_path": ""})
                for fp in v.get("files", [])[:20]:
                    t = f"file:{fp}"
                    fpath = BASE / fp
                    if fpath.exists():
                        fcat = _cat(fpath)
                        if fcat not in ("research", "extraction"):
                            continue
                    filter_edges.append({"source": nid, "target": t, "relation": "keyword", "weight": 0.8, "source_file": str(KEYWORDS_FILE), "source_location": ""})
        elif filter in ("author", "year", "journal", "quartile", "method", "framework"):
            filter_edges = _build_filter_edges(file_meta, filter)
            seen_vals = set()
            for e in filter_edges:
                v = e["source_file"]
                if v and v not in seen_vals:
                    seen_vals.add(v)
                    vnid = f"{filter}:{v}"
                    all_nodes.append({"id": vnid, "label": v, "file_type": "keyword", "source_file": f"Filter: {filter}", "source_location": v, "rel_path": ""})
            final_edges = []
            for e in filter_edges:
                vnid = f"{filter}:{e['source_file']}"
                final_edges.append({"source": vnid, "target": e["source"], "relation": filter, "weight": 0.5, "source_file": vnid, "source_location": ""})
                final_edges.append({"source": vnid, "target": e["target"], "relation": filter, "weight": 0.5, "source_file": vnid, "source_location": ""})
            filter_edges = final_edges
        else:
            filter_edges = list(md_edges)
    else:
        # --- Multi-layer filter logic ---
        # Build set of files matching ALL layers (AND between layers)
        # For OR, we accumulate across layers
        matched_files = None  # None = no constraint yet
        for layer in multi_layers:
            dim = layer["dim"]
            val = layer["val"].lower().strip()
            op = layer.get("op", "AND")

            # Get files matching this dimension=value
            layer_matched = set()
            if dim == "keyword":
                # Use keywords.json for keyword matching
                kw_data = _load_keywords()
                for word, v in kw_data.items():
                    if word.lower().strip() == val:
                        for fp in v.get("files", []):
                            nid = f"file:{fp}"
                            if nid in file_meta:
                                layer_matched.add(nid)
                        break
            else:
                for nid, m in file_meta.items():
                    mv = m.get(dim, "").strip().lower()
                    if mv and val in mv:
                        layer_matched.add(nid)

            if matched_files is None:
                matched_files = layer_matched
            elif op == "AND":
                matched_files &= layer_matched
            else:  # OR
                matched_files |= layer_matched

        if matched_files is None:
            matched_files = set(file_meta.keys())

        # Build filtered node/edge sets
        keep_nids = set()
        for n in md_nodes:
            if n.get("id") and n["id"] in matched_files:
                keep_nids.add(n["id"])
        md_nodes_filtered = [n for n in md_nodes if n["id"] in keep_nids]
        md_edges_filtered = [e for e in md_edges if e.get("source") in keep_nids and e.get("target") in keep_nids]
        # When keyword filter is active, hide project edges (only show keyword connections)
        if any(l["dim"] == "keyword" for l in multi_layers):
            md_edges_filtered = [e for e in md_edges_filtered if e.get("relation") != "same_project"]

        # Also add filter-value nodes for each layer
        filter_val_nodes = []
        for layer in multi_layers:
            dim = layer["dim"]
            val = layer["val"]
            if dim and val:
                vnid = f"filter:{dim}:{val}"
                filter_val_nodes.append({"id": vnid, "label": f"{dim}: {val}", "file_type": "keyword",
                    "source_file": f"Filter: {dim}", "source_location": val, "rel_path": ""})
                # Connect value node to all matched file nodes
                for n in md_nodes_filtered:
                    md_edges_filtered.append({"source": vnid, "target": n["id"], "relation": dim,
                        "weight": 0.5, "source_file": vnid, "source_location": ""})

        # Strip non-research nodes from code_nodes and md_nodes for cleaner view
        code_nodes_filtered = [n for n in code_nodes if n.get("file_type") in {"research", "extraction", "chat", "keyword"}]
        md_nodes_filtered = [n for n in md_nodes_filtered if n.get("file_type") in {"research", "extraction", "chat"}]

        all_nodes = code_nodes_filtered + md_nodes_filtered + filter_val_nodes
        filter_edges = md_edges_filtered

    # 5. Dedup edges
    edge_keys = {f"{e['source']}|{e['target']}|{e.get('relation','')}" for e in code_edges}
    all_edges = list(code_edges)
    for e in filter_edges:
        k = f"{e['source']}|{e['target']}|{e.get('relation','')}"
        if k not in edge_keys:
            edge_keys.add(k)
            all_edges.append(e)

    # Strip edges touching system/code/other nodes (only research/extraction/chat edges)
    sys_types = {"system", "code", "other"}
    ntypes = {}
    for n in all_nodes:
        ntypes[n["id"]] = n.get("file_type", "other")
    all_edges = [e for e in all_edges
        if ntypes.get(e.get("source", ""), "other") not in sys_types
        and ntypes.get(e.get("target", ""), "other") not in sys_types]

    cats = {}
    for n in all_nodes:
        cats[n.get("file_type","other")] = cats.get(n.get("file_type","other"), 0) + 1
    return {"nodes": all_nodes, "edges": all_edges, "files_analyzed": len(all_nodes), "categories": cats, "active_filter": filter}

@app.get("/api/graph/file")
async def get_graph_file(rel_path: str = ""):
    if not rel_path: raise HTTPException(400, "Missing rel_path param")
    try:
        fp = resolve_era_path(rel_path)
    except PermissionError:
        raise HTTPException(403, "Access denied")
    if not fp.exists():
        raise HTTPException(404, "File not found")
    return {"content": fp.read_text(encoding="utf-8", errors="replace"), "path": rel_path, "ext": fp.suffix}

@app.post("/api/graph/refresh")
async def refresh_graph_data():
    """Re-scan all .md files for keywords + metadata, rebuild graph cache."""
    # Re-scan keywords from all .md files
    kw_result = await scan_keywords()
    # Force re-parse of metadata
    _, _, file_meta = _scan_md_files()
    dims = {}
    for m in file_meta.values():
        for k, v in m.items():
            if v: dims[k] = dims.get(k, 0) + 1
    return {"ok": True, "keywords_added": kw_result.get("added", 0), "keywords_total": kw_result.get("total", 0), "dimensions": {k: v for k, v in dims.items() if v}}

# ── Keywords System ──
KEYWORDS_FILE     = CORE / "keywords.json"
DISCARDED_FILE    = CORE / "discarded_keywords.json"

def _load_keywords() -> dict:
    """{ "keyword": { "files": ["rel/path.md", ...], "note": "" }, ... }"""
    if KEYWORDS_FILE.exists():
        try: return json.loads(KEYWORDS_FILE.read_text(encoding="utf-8"))
        except Exception: pass
    return {}

def _save_keywords(data: dict):
    KEYWORDS_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def _load_predatory() -> set:
    """Set of predatory journal name fragments (lowercase)."""
    if PREDATORY_FILE.exists():
        try: return set(json.loads(PREDATORY_FILE.read_text(encoding="utf-8")))
        except Exception: pass
    return set()

def _save_predatory(words: set):
    PREDATORY_FILE.write_text(json.dumps(sorted(words), indent=2, ensure_ascii=False), encoding="utf-8")

def _load_discarded() -> set:
    """Set of keyword strings the user has explicitly deleted (never re-auto-add)."""
    if DISCARDED_FILE.exists():
        try: return set(json.loads(DISCARDED_FILE.read_text(encoding="utf-8")))
        except Exception: pass
    return set()

def _save_discarded(words: set):
    DISCARDED_FILE.write_text(json.dumps(sorted(words), indent=2, ensure_ascii=False), encoding="utf-8")

@app.get("/api/keywords")
async def get_keywords():
    kw = _load_keywords()
    return {"keywords": [{"word": k, "files": v.get("files", []), "note": v.get("note", ""), "count": len(v.get("files", []))} for k, v in sorted(kw.items())]}

@app.post("/api/keywords")
async def save_keywords(request: Request):
    data = await request.json()
    action = data.get("action", "add")
    word = data.get("word", "").strip().lower()
    kw = _load_keywords()
    discarded = _load_discarded()
    if action == "batch_remove":
        words = data.get("words", [])
        for w in words:
            kw.pop(w, None)
            discarded.add(w)
        _save_keywords(kw)
        _save_discarded(discarded)
        return {"ok": True}
    if not word: raise HTTPException(400, "Keyword required")
    if action == "add":
        discarded.discard(word)
        _save_discarded(discarded)
        kw.setdefault(word, {"files": [], "note": data.get("note", "")})
        kw[word]["note"] = data.get("note", kw[word].get("note", ""))
    elif action == "remove":
        kw.pop(word, None)
        discarded.add(word)
        _save_discarded(discarded)
    elif action == "edit":
        new_word = data.get("new_word", word).strip().lower()
        if new_word and new_word != word:
            kw[new_word] = kw.pop(word)
            kw[new_word]["note"] = data.get("note", kw[new_word].get("note", ""))
        elif new_word == word:
            kw[word]["note"] = data.get("note", kw[word].get("note", ""))
    elif action == "set_files":
        kw.setdefault(word, {"files": [], "note": ""})
        kw[word]["files"] = data.get("files", [])
    _save_keywords(kw)
    return {"ok": True}

@app.post("/api/keywords/scan")
async def scan_keywords():
    """Scan all .md files and auto-extract frequent terms as keyword suggestions."""
    kw = _load_keywords()
    discarded = _load_discarded()
    from collections import Counter
    word_counter = Counter()
    file_words = {}
    stopwords = {"the","this","that","with","from","for","and","not","are","was","were","has","have","had","but","its","all","can","each","which","their","they","will","would","could","should","about","also","more","than","into","over","such","only","other","than","then","these","those","what","when","where","there","been","being","some","them","very","just","after","before","because","between","both","under","above","while","file","files","data","research","study","paper","analysis","based","using","used","also","well"}
    special_terms = {"q1","q2","q3","q4","scopus","wos","researchpilot","heis","p1","p2","ai","nlp","rag","llm","lstm","cnn","rnn","bert","gpt","tfidf","svm","kmeans","pca","hei","culture","publication","extraction","methodology","qualitative","quantitative","mixed","theoretical","framework","limitations","contribution"}
    for f in BASE.rglob("*.md"):
        try:
            cat = _cat(f)
            if cat in ("system", "code", "chat", "other"):
                continue
            txt = f.read_text(encoding="utf-8", errors="ignore").lower()
            rel = str(f.relative_to(BASE))
            # Extract words (3+ chars)
            words = set(re.findall(r'\b[a-z]{3,}\b', txt))
            # Score: special terms get higher weight
            for w in words:
                if w in stopwords: continue
                if w in discarded: continue
                weight = 5 if w in special_terms else 1
                word_counter[w] += weight
                file_words.setdefault(w, set()).add(rel)
        except Exception:
            continue
    # Add top 50 new words as suggestions (not replacing existing)
    added = 0
    for w, cnt in word_counter.most_common(200):
        if w not in kw and cnt >= 2:
            kw[w] = {"files": sorted(file_words.get(w, set())), "note": f"auto (score: {cnt})"}
            added += 1
        elif w in kw and cnt >= 2:
            # Update file list for existing keywords
            existing = set(kw[w].get("files", []))
            existing.update(file_words.get(w, set()))
            kw[w]["files"] = sorted(existing)
    # Purge any system/chat/code file references from existing keywords
    for word, v in kw.items():
        files = v.get("files", [])
        clean = [fp for fp in files if _cat(BASE / fp) in ("research", "extraction")]
        if len(clean) != len(files):
            kw[word]["files"] = clean
    _save_keywords(kw)
    return {"ok": True, "added": added, "total": len(kw)}

@app.get("/api/keywords/search")
async def search_keywords(q: str = ""):
    """Search keywords and return matching file paths."""
    kw = _load_keywords()
    if not q: return {"results": []}
    q = q.lower()
    results = {}
    for word, v in kw.items():
        if q in word:
            for fp in v.get("files", []):
                results.setdefault(fp, []).append(word)
    return {"results": [{"file": k, "keywords": v} for k, v in sorted(results.items())]}

@app.get("/api/keywords/discarded")
async def get_discarded():
    """Return list of discarded (never-auto-add) keywords."""
    return {"discarded": sorted(_load_discarded())}

@app.post("/api/keywords/discarded")
async def restore_discarded(request: Request):
    """Remove a word from the discarded list so it can be auto-added again."""
    data = await request.json()
    word = data.get("word", "").strip().lower()
    if not word: raise HTTPException(400, "Word required")
    d = _load_discarded()
    d.discard(word)
    _save_discarded(d)
    return {"ok": True}

# ── Predatory Journals ──
@app.get("/api/predatory")
async def get_predatory():
    return {"journals": sorted(_load_predatory())}

@app.post("/api/predatory")
async def save_predatory(request: Request):
    data = await request.json()
    action = data.get("action", "add")
    name = data.get("name", "").strip().lower()
    pj = _load_predatory()
    if action == "add":
        if name: pj.add(name)
    elif action == "remove":
        pj.discard(name)
    elif action == "set_list":
        pj = set(data.get("names", []))
    _save_predatory(pj)
    return {"ok": True}

@app.get("/api/predatory/online")
async def fetch_predatory_online():
    """Fetch known predatory journal lists from public sources."""
    urls = [
        "https://raw.githubusercontent.com/nicole-richey/predatory-journals/main/predatory-journals.json",
        "https://raw.githubusercontent.com/stop-predatory-journals/stop-predatory-journals-data/main/data/predatory_journals.json",
    ]
    all_names = set()
    for url in urls:
        try:
            async with httpx.AsyncClient(timeout=15.0) as c:
                r = await c.get(url)
                if r.status_code == 200:
                    data = r.json()
                    if isinstance(data, list):
                        for entry in data:
                            if isinstance(entry, str):
                                all_names.add(entry.lower().strip())
                            elif isinstance(entry, dict):
                                for v in entry.values():
                                    if isinstance(v, str):
                                        all_names.add(v.lower().strip())
                    elif isinstance(data, dict):
                        for v in data.values():
                            if isinstance(v, str):
                                all_names.add(v.lower().strip())
                            elif isinstance(v, list):
                                for item in v:
                                    if isinstance(item, str):
                                        all_names.add(item.lower().strip())
        except Exception:
            continue
    existing = _load_predatory()
    existing.update(all_names)
    _save_predatory(existing)
    return {"ok": True, "added": len(all_names), "total": len(existing)}

# ── Quick Notes ──
NOTES_FILE = BACKEND / "notes.json"

def _load_notes() -> list:
    if NOTES_FILE.exists():
        try: return json.loads(NOTES_FILE.read_text(encoding="utf-8"))
        except: pass
    return []

def _save_notes(notes: list):
    NOTES_FILE.write_text(json.dumps(notes, ensure_ascii=False, indent=2), encoding="utf-8")

@app.get("/api/notes")
async def get_notes():
    return {"notes": _load_notes()}

@app.post("/api/notes")
async def create_note():
    notes = _load_notes()
    n = len(notes) + 1
    note = {
        "id": f"n{int(datetime.datetime.now().timestamp())}",
        "title": f"Note {n}",
        "content": "",
        "created": datetime.datetime.now().isoformat(),
        "updated": datetime.datetime.now().isoformat()
    }
    notes.append(note)
    _save_notes(notes)
    return note

@app.put("/api/notes/{note_id}")
async def update_note(note_id: str, req: Request):
    data = await req.json()
    notes = _load_notes()
    for note in notes:
        if note["id"] == note_id:
            if "title" in data: note["title"] = data["title"]
            if "content" in data: note["content"] = data["content"]
            note["updated"] = datetime.datetime.now().isoformat()
            _save_notes(notes)
            return note
    raise HTTPException(404, "Note not found")

@app.delete("/api/notes/{note_id}")
async def delete_note(note_id: str):
    notes = _load_notes()
    notes = [n for n in notes if n["id"] != note_id]
    _save_notes(notes)
    return {"ok": True}

# ─── Research Web Search ──────────────────────────────────────────────────────
def _decode_openalex_abstract(inverted_index: dict) -> str:
    if not inverted_index:
        return ""
    try:
        max_pos = max(max(positions) for positions in inverted_index.values())
        words = [""] * (max_pos + 1)
        for word, positions in inverted_index.items():
            for pos in positions:
                words[pos] = word
        return " ".join(words)
    except Exception:
        return ""

def _clean_authors(authors_list: list, source: str) -> list:
    names = []
    for a in authors_list[:20]:
        if source == "openalex":
            n = a.get("author", {}).get("display_name", "")
        elif source == "crossref":
            given = a.get("given", "")
            family = a.get("family", "")
            n = f"{given} {family}".strip()
        elif source == "semantic":
            n = a.get("name", "")
        else:
            n = str(a)
        if n and n not in names:
            names.append(n)
    return names


_STOPWORDS = set("the a an of in to and for is on that this with by as are be was were at from or but not have has had its their our your his her its all each which what who when where why how do does did will would can could may might shall should about into over after before between under above below up down out off only just also very too so some any such more most many much other than then them these those".split())


def _extract_keywords(query: str) -> list:
    """Extract meaningful keywords from a search query."""
    import re
    words = re.findall(r"[a-zA-Z]+(?:[-&][a-zA-Z]+)*", query.lower())
    keywords = [w for w in words if len(w) > 2 and w not in _STOPWORDS]
    seen = set()
    unique = []
    for k in keywords:
        if k not in seen:
            seen.add(k)
            unique.append(k)
    multi_word = re.findall(r'"([^"]+)"', query)
    for mw in multi_word:
        mw_clean = mw.strip().lower()
        if mw_clean and mw_clean not in seen:
            seen.add(mw_clean)
            unique.append(mw_clean)
    return unique


def _score_keyword_match(keywords: list, title: str, abstract: str) -> int:
    """Score a result by how many query keywords appear in its title/abstract."""
    title_lower = (title or "").lower()
    abstract_lower = (abstract or "").lower()
    combined = title_lower + " " + abstract_lower
    score = 0
    for kw in keywords:
        if kw in title_lower:
            score += 3
        elif kw in abstract_lower:
            score += 1
    return score


def _build_optimized_query(keywords: list, raw_query: str) -> str:
    """Build an optimized query string from extracted keywords."""
    if not keywords:
        return raw_query
    quoted = [f'"{k}"' for k in keywords[:5]]
    return " ".join(quoted)


async def _search_openalex(q: str, year_from: str, year_to: str, max_results: int) -> list:
    try:
        params = {"search": q, "per_page": max_results}
        filters = []
        if year_from:
            filters.append(f"from_publication_date:{year_from}-01-01")
        if year_to:
            filters.append(f"to_publication_date:{year_to}-12-31")
        if filters:
            params["filter"] = ",".join(filters)
        headers = {"User-Agent": "ResearchPilot-ResearchAssistant/2.0 (mailto:research@researchpilot.local)"}
        async with httpx.AsyncClient(timeout=15.0) as c:
            r = await c.get("https://api.openalex.org/works", params=params, headers=headers)
            if r.status_code != 200:
                return []
            data = r.json()
        results = []
        for work in data.get("results", []):
            doi = (work.get("doi") or "").replace("https://doi.org/", "").lower()
            abstract = _decode_openalex_abstract(work.get("abstract_inverted_index") or {})
            venue = work.get("primary_location") or {}
            source_obj = venue.get("source") or {}
            results.append({
                "title": work.get("title", "Untitled"),
                "authors": _clean_authors(work.get("authorships", []), "openalex"),
                "year": str(work.get("publication_year", "")),
                "journal": source_obj.get("display_name", ""),
                "doi": doi,
                "abstract": abstract[:800] if abstract else "",
                "url": f"https://doi.org/{doi}" if doi else "",
                "citations": work.get("cited_by_count", 0),
                "is_oa": work.get("open_access", {}).get("is_oa", False),
                "oa_url": work.get("open_access", {}).get("oa_url", ""),
                "source": "OpenAlex",
                "pdf_url": work.get("open_access", {}).get("oa_url", ""),
                "primary_location": doi or ""
            })
        return results
    except Exception as e:
        print(f"[Research] OpenAlex error: {e}")
        return []

async def _search_crossref(q: str, year_from: str, year_to: str, max_results: int) -> list:
    try:
        params = {"query": q, "rows": max_results}
        filters = []
        if year_from:
            filters.append(f"from-pub-date:{year_from}-01-01")
        if year_to:
            filters.append(f"until-pub-date:{year_to}-12-31")
        if filters:
            params["filter"] = ",".join(filters)
        async with httpx.AsyncClient(timeout=15.0) as c:
            r = await c.get("https://api.crossref.org/works", params=params)
            if r.status_code != 200:
                return []
            data = r.json()
        results = []
        for item in data.get("message", {}).get("items", []):
            doi = (item.get("DOI") or "").lower()
            abstracts = item.get("abstract", "")
            if abstracts:
                abstracts = re.sub(r'<[^>]+>', '', abstracts)[:800]
            pub_info = item.get("published-print") or item.get("published-online") or item.get("issued") or {}
            parts = pub_info.get("date-parts", [[]])
            year = str(parts[0][0]) if parts and parts[0] else ""
            results.append({
                "title": (item.get("title") or ["Untitled"])[0],
                "authors": _clean_authors(item.get("author", []), "crossref"),
                "year": year,
                "journal": (item.get("container-title") or [""])[0],
                "doi": doi,
                "abstract": abstracts,
                "url": f"https://doi.org/{doi}" if doi else "",
                "citations": item.get("is-referenced-by-count", 0),
                "is_oa": False,
                "oa_url": "",
                "source": "Crossref",
                "pdf_url": "",
                "primary_location": doi or ""
            })
        return results
    except Exception as e:
        print(f"[Research] Crossref error: {e}")
        return []

async def _search_semantic_scholar(q: str, year_from: str, year_to: str, max_results: int) -> list:
    try:
        fields = "title,authors,year,externalIds,abstract,venue,citationCount,openAccessPdf,publicationDate"
        params = {"query": q, "limit": max_results, "fields": fields}
        if year_from or year_to:
            params["year"] = f"{year_from or '1900'}-{year_to or '2030'}"
        headers = {"User-Agent": "ResearchPilot-ResearchAssistant/2.0"}
        # Use API key if available (via env or settings — loaded from .env)
        api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
        if api_key:
            headers["x-api-key"] = api_key
        async with httpx.AsyncClient(timeout=15.0) as c:
            r = await c.get("https://api.semanticscholar.org/graph/v1/paper/search", params=params, headers=headers)
            # Exponential backoff for rate limiting (up to 3 retries)
            retries = 0
            while r.status_code == 429 and retries < 3:
                wait = 1.5 * (retries + 1)
                print(f"[Research] Semantic Scholar rate limited, retrying in {wait}s...")
                await asyncio.sleep(wait)
                r = await c.get("https://api.semanticscholar.org/graph/v1/paper/search", params=params, headers=headers)
                retries += 1
            if r.status_code != 200:
                print(f"[Research] Semantic Scholar returned {r.status_code}")
                return []
            data = r.json()
        results = []
        for paper in data.get("data", []):
            ext_ids = paper.get("externalIds") or {}
            doi = (ext_ids.get("DOI") or "").lower()
            oa = paper.get("openAccessPdf") or {}
            results.append({
                "title": paper.get("title", "Untitled"),
                "authors": _clean_authors(paper.get("authors", []), "semantic"),
                "year": str(paper.get("year", "")),
                "journal": paper.get("venue", ""),
                "doi": doi,
                "abstract": (paper.get("abstract") or "")[:800],
                "url": f"https://doi.org/{doi}" if doi else f"https://api.semanticscholar.org/CorpusID:{paper.get('paperId','')}",
                "citations": paper.get("citationCount", 0),
                "is_oa": bool(oa.get("url")),
                "oa_url": oa.get("url", ""),
                "source": "Semantic Scholar",
                "pdf_url": oa.get("url", ""),
                "primary_location": paper.get("paperId", "")
            })
        return results
    except Exception as e:
        print(f"[Research] Semantic Scholar error: {e}")
        return []

async def _search_google_scholar(q: str, year_from: str, year_to: str, max_results: int) -> list:
    """Search Google Scholar via scholarly library (free, no API key)."""
    if not HAS_SCHOLARLY:
        return []
    try:
        loop = asyncio.get_event_loop()
        search_query = _scholarly.scholarly.search_pubs(q)
        results = []
        count = 0
        # Limit to 5 max to avoid long timeouts (Google Scholar is inherently slow)
        limit = min(max_results, 5)
        max_attempts = limit * 8  # prevent infinite loop when year filter skips all results
        attempts = 0
        while count < limit and attempts < max_attempts:
            attempts += 1
            try:
                pub = await asyncio.wait_for(
                    loop.run_in_executor(None, lambda: next(search_query)),
                    timeout=5.0
                )
            except StopIteration:
                break
            except asyncio.TimeoutError:
                continue  # skip slow paper, try next
            except Exception:
                continue  # skip error, try next
            if not pub or not pub.get("bib"):
                continue
            bib = pub["bib"]
            raw_year = bib.get("pub_year", "")
            try:
                year = str(int(raw_year))
            except (ValueError, TypeError):
                year = ""
            # Year filter
            if year_from and year and int(year) < int(year_from):
                continue
            if year_to and year and int(year) > int(year_to):
                continue
            authors = bib.get("author", "")
            if isinstance(authors, str):
                authors = [a.strip() for a in authors.split(" and ")]
            elif not isinstance(authors, list):
                authors = []
            doi = (pub.get("doi") or pub.get("gsrank") or "")
            results.append({
                "title": bib.get("title", "Untitled"),
                "authors": authors[:20],
                "year": year,
                "journal": bib.get("journal", ""),
                "doi": str(doi),
                "abstract": (bib.get("abstract") or "")[:800],
                "url": pub.get("url", "") or pub.get("pub_url", ""),
                "citations": pub.get("num_citations", 0),
                "is_oa": False,
                "oa_url": "",
                "source": "Google Scholar",
                "pdf_url": pub.get("eprint_url", ""),
                "primary_location": doi or ""
            })
            count += 1
        return results
    except Exception as e:
        print(f"[Research] Google Scholar error: {e}")
        return []

async def _search_pubmed(q: str, year_from: str, year_to: str, max_results: int) -> list:
    try:
        # Step 1: Search for IDs — build clean keyword query for PubMed
        keywords = _extract_keywords(q)
        if keywords:
            term_parts = [f'({kw}[Title/Abstract])' for kw in keywords[:8]]
        else:
            term_parts = [f'({q})']
        query_parts = ["+AND+".join(term_parts)]
        if year_from:
            query_parts.append(f'("{year_from}"[Date - Publication] : "{year_to or "2030"}"[Date - Publication])')
        elif year_to:
            query_parts.append(f'("1900"[Date - Publication] : "{year_to}"[Date - Publication])')
        query_str = "+AND+".join(query_parts).replace(' ', '+')
        import urllib.parse
        query_str = urllib.parse.quote(query_str, safe='+()[]":,-')
        search_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query_str}&retmax={max_results}&retmode=json"
        headers = {"User-Agent": "ResearchPilot-ResearchAssistant/2.0"}
        async with httpx.AsyncClient(timeout=15.0) as c:
            r = await c.get(search_url, headers=headers)
            if r.status_code != 200:
                return []
            search_data = r.json()
            id_list = search_data.get("esearchresult", {}).get("idlist", [])
            if not id_list:
                return []
        # Step 2: Fetch details for each ID
        ids = ",".join(id_list[:max_results])
        fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={ids}&retmode=json"
        async with httpx.AsyncClient(timeout=15.0) as c:
            r = await c.get(fetch_url, headers=headers)
            if r.status_code != 200:
                return []
            fetch_data = r.json()
        results = []
        for uid in id_list:
            entry = fetch_data.get("result", {}).get(uid, {})
            if not entry:
                continue
            title = entry.get("title", "Untitled")
            authors = []
            for a in entry.get("authors", [])[:20]:
                if isinstance(a, dict) and a.get("name"):
                    authors.append(a["name"])
            pub_date = entry.get("pubdate", "")
            year = pub_date[:4] if pub_date else ""
            source = entry.get("source", "")
            doi = ""
            for aid in entry.get("articleids", []):
                if isinstance(aid, dict) and aid.get("idtype") == "doi":
                    doi = aid.get("value", "").lower()
                    break
            pmcid = ""
            for aid in entry.get("articleids", []):
                if isinstance(aid, dict) and aid.get("idtype") == "pmc":
                    pmcid = aid.get("value", "")
                    break
            url_link = f"https://pubmed.ncbi.nlm.nih.gov/{uid}/"
            abstract = entry.get("abstract", "")
            if isinstance(abstract, str):
                abstract = abstract[:800]
            elif isinstance(abstract, dict):
                abstract = str(abstract)[:800]
            else:
                abstract = ""
            results.append({
                "title": title,
                "authors": authors,
                "year": year,
                "journal": source,
                "doi": doi,
                "abstract": abstract,
                "url": url_link,
                "citations": 0,
                "is_oa": False,
                "oa_url": f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/" if pmcid else "",
                "source": "PubMed",
                "pdf_url": f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/" if pmcid else "",
                "primary_location": uid
            })
        return results
    except Exception as e:
        print(f"[Research] PubMed error: {e}")
        return []

def _dedup_results(results: list) -> list:
    seen_dois = set()
    seen_titles = set()
    deduped = []
    for r in results:
        key = r.get("doi", "").lower().strip()
        if key and key in seen_dois:
            continue
        title_key = r.get("title", "").lower().strip()[:60]
        if title_key and title_key in seen_titles:
            continue
        if key:
            seen_dois.add(key)
        if title_key:
            seen_titles.add(title_key)
        deduped.append(r)
    return deduped

@app.get("/api/research/search")
async def research_web_search(
    q: str = "",
    year_from: str = "",
    year_to: str = "",
    max_results: int = 15,
    sort: str = "citations",
    sources: str = "openalex,crossref,semantic"
):
    if not q:
        return {"results": [], "total": 0}
    max_results = min(max_results, 50)

    # Normalize year range — auto-swap if inverted (from > to)
    try:
        yf = int(year_from) if year_from else None
        yt = int(year_to) if year_to else None
        if yf is not None and yt is not None and yf > yt:
            year_from, year_to = str(yt), str(yf)
    except (ValueError, TypeError):
        pass

    # Extract keywords from query for smarter matching
    keywords = _extract_keywords(q)
    opt_query = _build_optimized_query(keywords, q)

    source_list = [s.strip().lower() for s in sources.split(",") if s.strip()]
    tasks = {}

    # Use optimized query for better keyword matching
    if "openalex" in source_list:
        tasks["openalex"] = _search_openalex(opt_query, year_from, year_to, min(max_results * 2, 50))
    if "crossref" in source_list:
        tasks["crossref"] = _search_crossref(opt_query, year_from, year_to, min(max_results * 2, 50))
    if "semantic" in source_list:
        tasks["semantic"] = _search_semantic_scholar(q, year_from, year_to, max_results)
    if "pubmed" in source_list:
        tasks["pubmed"] = _search_pubmed(q, year_from, year_to, max_results)
    if "google_scholar" in source_list:
        tasks["google_scholar"] = _search_google_scholar(q, year_from, year_to, min(max_results, 5))

    t0 = datetime.datetime.now()
    results_map = {}
    source_errors = {}
    if tasks:
        gathered = await asyncio.gather(*tasks.values(), return_exceptions=True)
        for (sk, sr), res in zip(tasks.items(), gathered):
            if isinstance(res, Exception):
                source_errors[sk] = str(res)
                results_map[sk] = []
            else:
                results_map[sk] = res

    combined = []
    for sk, sr in results_map.items():
        combined.extend(sr)
    deduped = _dedup_results(combined)

    # Filter out predatory journals
    predatory = _load_predatory()
    clean = []
    for r in deduped:
        journal = (r.get("journal") or "").lower().strip()
        is_pred = any(p in journal for p in predatory) if journal else False
        r["is_predatory"] = is_pred
        if not is_pred:
            clean.append(r)
    deduped = clean

    # Score each result by keyword match in title + abstract
    for r in deduped:
        r["kw_score"] = _score_keyword_match(keywords, r.get("title", ""), r.get("abstract", ""))

    # Apply sorting
    if sort == "date":
        deduped.sort(key=lambda x: (x.get("year", "") or "0"), reverse=True)
    elif sort == "citations":
        deduped.sort(key=lambda x: (x.get("kw_score", 0) * 100 + x.get("citations", 0) or 0), reverse=True)
    else:  # relevance — keyword match score first, then citations
        deduped.sort(key=lambda x: (x.get("kw_score", 0), x.get("citations", 0) or 0), reverse=True)

    t1 = datetime.datetime.now()
    elapsed = f"{(t1 - t0).total_seconds():.1f}s"

    return {
        "results": deduped[:max_results],
        "total": len(deduped),
        "sources": {k: len(v) for k, v in results_map.items()},
        "source_errors": source_errors,
        "query_time": elapsed,
        "keywords": keywords
    }

@app.post("/api/research/import")
async def research_web_import(request: Request):
    data = await request.json()
    title = data.get("title", "Untitled")
    doi = data.get("doi", "")
    authors = data.get("authors", [])
    year = data.get("year", "")
    journal = data.get("journal", "")
    abstract = data.get("abstract", "")
    oa_url = data.get("oa_url", "") or data.get("pdf_url", "")
    url = data.get("url", "")
    source = data.get("source", "Web")
    safe_name = re.sub(r'[^\w\s\-]', '', title)[:80].strip()
    safe_name = re.sub(r'\s+', '-', safe_name)
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    pdf_path = None
    pdf_downloaded = False
    if oa_url:
        try:
            async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as c:
                r = await c.get(oa_url)
                if r.status_code == 200 and "application/pdf" in r.headers.get("content-type", "").lower():
                    pdf_name = f"{safe_name}.pdf"
                    pdf_path = UNREAD_WEB / pdf_name
                    pdf_path.write_bytes(r.content)
                    pdf_downloaded = True
        except Exception as e:
            print(f"[Research] PDF download failed: {e}")
    if not pdf_downloaded and doi:
        for try_url in [
            f"https://doi.org/{doi}",
            f"https://sci-hub.se/{doi}",
            f"https://unpaywall.org/{doi}"
        ]:
            try:
                async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as c:
                    r = await c.get(try_url, headers={"User-Agent": "ResearchPilot/2.0"})
                    if r.status_code == 200:
                        ct = r.headers.get("content-type", "").lower()
                        if "application/pdf" in ct or "application/octet-stream" in ct:
                            pdf_name = f"{safe_name}.pdf"
                            pdf_path = UNREAD_WEB / pdf_name
                            pdf_path.write_bytes(r.content)
                            pdf_downloaded = True
                            break
            except Exception:
                continue
    md_fulltext = ""
    if pdf_downloaded and pdf_path:
        try:
            md_fulltext = file_to_markdown(pdf_path)
        except Exception as e:
            print(f"[Research] PDF->MD conversion failed: {e}")
    meta_md = (
        f"# {title}\n"
        f"*Source: Web Import ({source}) | Imported: {ts}*\n"
        f"*Status: 📥 Unread (needs analysis)*\n"
        f"*DOI: {doi}*\n"
        f"*Authors: {', '.join(authors[:8])}*\n"
        f"*Year: {year}*\n"
        f"*Journal: {journal}*\n\n"
        f"---\n\n"
        f"**DOI**: `{doi}`\n\n"
        f"**Authors**: {', '.join(authors[:8])}\n\n"
        f"**Year**: {year}\n\n"
        f"**Journal**: {journal}\n\n"
        f"**URL**: {url}\n\n"
        f"**PDF Downloaded**: {'Yes' if pdf_downloaded else 'No'}\n\n"
        f"---\n\n"
        f"## Abstract\n\n{abstract}\n"
    )
    if md_fulltext:
        meta_md += f"\n\n---\n\n## Full Text (auto-extracted from PDF)\n\n{md_fulltext}\n"
    md_name = f"{safe_name}.md"
    md_path = UNREAD_WEB / md_name
    md_path.write_text(meta_md, encoding="utf-8")
    return {
        "ok": True,
        "title": title,
        "doi": doi,
        "md_file": md_name,
        "pdf_downloaded": pdf_downloaded,
        "pdf_file": pdf_path.name if pdf_path and pdf_downloaded else None,
        "folder": "INCOMING/UNREAD-WEB"
    }

@app.post("/api/research/save-md")
async def research_save_md_only(request: Request):
    """Save paper metadata + abstract as .md file. NO auto-PDF download."""
    data = await request.json()
    title = data.get("title", "Untitled")
    doi = data.get("doi", "")
    authors = data.get("authors", [])
    year = data.get("year", "")
    journal = data.get("journal", "")
    abstract = data.get("abstract", "")
    oa_url = data.get("oa_url", "") or data.get("pdf_url", "")
    url = data.get("url", "")
    source = data.get("source", "Web")
    safe_name = re.sub(r'[^\w\s\-]', '', title)[:80].strip()
    safe_name = re.sub(r'\s+', '-', safe_name)
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    meta_md = (
        f"# {title}\n"
        f"*Source: Web Save ({source}) | Saved: {ts}*\n"
        f"*Status: 📥 Unread (needs analysis)*\n"
        f"*DOI: {doi}*\n"
        f"*Authors: {', '.join(authors[:8])}*\n"
        f"*Year: {year}*\n"
        f"*Journal: {journal}*\n\n"
        f"---\n\n"
        f"**DOI**: `{doi}`\n\n"
        f"**Authors**: {', '.join(authors[:8])}\n\n"
        f"**Year**: {year}\n\n"
        f"**Journal**: {journal}\n\n"
        f"**URL**: {url}\n\n"
        f"**Open Access URL**: {oa_url}\n\n"
        f"**Source**: {source}\n\n"
        f"---\n\n"
        f"## Abstract\n\n{abstract}\n"
    )
    md_name = f"{safe_name}.md"
    md_path = UNREAD_WEB / md_name
    # Avoid overwriting
    counter = 1
    while md_path.exists():
        md_name = f"{safe_name}_{counter}.md"
        md_path = UNREAD_WEB / md_name
        counter += 1
    md_path.write_text(meta_md, encoding="utf-8")
    return {
        "ok": True,
        "title": title,
        "doi": doi,
        "md_file": md_name,
        "folder": "INCOMING/UNREAD-WEB"
    }

# ── 12-point AI analysis ──
_12_POINT_SYSTEM = """You are an expert academic research analyst. Given the following paper metadata and abstract, produce a structured 12-point analysis. Follow this exact format:

## 1. The Problem
What real-world or theoretical problem does this paper address? Why does it matter?

## 2. The Gap
What is missing in existing literature? What has not been studied before?

## 3. The Research Question(s)
What specific question(s) is the paper trying to answer?

## 4. The Purpose / Objective
What does the paper set out to do? (Explore, explain, predict, compare, develop, or test?)

## 5. The Theory or Framework
What theoretical lens does the paper use? Why did they choose it?

## 6. The Methodology
Research design, data collection, sample, analysis method.

## 7. The Key Findings
What did the study actually discover?

## 8. The Contribution
Does it confirm, extend, or introduce new knowledge?

## 9. The Limitations
What did the study not do or could not do?

## 10. The Implications
What do the findings mean in practice? Who should act and how?

## 11. Key Citations
Which authors/works does the paper build on?

## 12. Your Critical Position
Is the evidence sufficient? Methodology appropriate? What would you challenge?

Be thorough but concise. Base everything on the provided abstract/metadata only."""

async def _generate_12_point_analysis(paper: dict) -> str:
    """Generate 12-point analysis using connected AI engine."""
    prompt = (
        f"**Title:** {paper.get('title', 'Untitled')}\n"
        f"**Authors:** {', '.join(paper.get('authors', [])[:8])}\n"
        f"**Year:** {paper.get('year', '')}\n"
        f"**Journal:** {paper.get('journal', '')}\n"
        f"**DOI:** {paper.get('doi', '')}\n\n"
        f"**Abstract:**\n{paper.get('abstract', 'No abstract')}\n\n"
        f"Produce the full 12-point analysis as specified."
    )
    msgs = [{"role": "user", "content": prompt}]
    try:
        text, engine_name, _ = await ai_respond(msgs)
        if engine_name != "none" and text:
            return text
    except Exception:
        pass
    return ""

@app.post("/api/research/save-md-with-analysis")
async def research_save_md_with_analysis(request: Request):
    """Save paper as .md with full metadata + 12-point AI analysis (for non-OA papers)."""
    data = await request.json()
    title = data.get("title", "Untitled")
    doi = data.get("doi", "")
    authors = data.get("authors", [])
    year = data.get("year", "")
    journal = data.get("journal", "")
    abstract = data.get("abstract", "")
    url = data.get("url", "")
    source = data.get("source", "Web")
    is_predatory = data.get("is_predatory", False)
    safe_name = re.sub(r'[^\w\s\-]', '', title)[:80].strip()
    safe_name = re.sub(r'\s+', '-', safe_name)
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # Generate 12-point analysis
    analysis = await _generate_12_point_analysis(data)

    pred_warn = "*⚠️ PREDATORY JOURNAL — verify carefully*\n" if is_predatory else ""
    meta_md = (
        f"# {title}\n"
        f"*Source: Web Save ({source}) | Saved: {ts}*\n"
        f"*Status: 📥 Unread (needs analysis)*\n"
        f"*DOI: {doi}*\n"
        f"*Authors: {', '.join(authors[:8])}*\n"
        f"*Year: {year}*\n"
        f"*Journal: {journal}*\n"
        f"{pred_warn}"
        f"*Type: 12-Point Analysis*\n\n"
        f"---\n\n"
        f"**DOI**: `{doi}`\n\n"
        f"**Authors**: {', '.join(authors[:8])}\n\n"
        f"**Year**: {year}\n\n"
        f"**Journal**: {journal}\n\n"
        f"**URL**: {url}\n\n"
        f"**Source**: {source}\n\n"
        f"---\n\n"
        f"## Abstract\n\n{abstract}\n\n"
        f"---\n\n"
    )
    if analysis:
        meta_md += f"## 12-Point Research Analysis\n\n{analysis}\n"
    else:
        meta_md += (
            "## 12-Point Research Analysis\n\n"
            "*⚠️ AI analysis could not be generated (no AI engine enabled).*\n\n"
            "Please fill in manually:\n\n"
            "### 1. The Problem\n\n\n"
            "### 2. The Gap\n\n\n"
            "### 3. The Research Question(s)\n\n\n"
            "### 4. The Purpose / Objective\n\n\n"
            "### 5. The Theory or Framework\n\n\n"
            "### 6. The Methodology\n\n\n"
            "### 7. The Key Findings\n\n\n"
            "### 8. The Contribution\n\n\n"
            "### 9. The Limitations\n\n\n"
            "### 10. The Implications\n\n\n"
            "### 11. Key Citations\n\n\n"
            "### 12. Your Critical Position\n"
        )

    md_name = f"{safe_name}.md"
    md_path = UNREAD_WEB / md_name
    counter = 1
    while md_path.exists():
        md_name = f"{safe_name}_{counter}.md"
        md_path = UNREAD_WEB / md_name
        counter += 1
    md_path.write_text(meta_md, encoding="utf-8")
    return {
        "ok": True,
        "title": title,
        "doi": doi,
        "md_file": md_name,
        "folder": "INCOMING/UNREAD-WEB",
        "ai_analysis": bool(analysis)
    }

@app.post("/api/research/download-pdf")
async def research_download_pdf(request: Request):
    """Download OA paper PDF to UNREAD-WEB + auto-convert to .md via docling."""
    data = await request.json()
    title = data.get("title", "Untitled")
    doi = data.get("doi", "")
    authors = data.get("authors", [])
    year = data.get("year", "")
    journal = data.get("journal", "")
    abstract = data.get("abstract", "")
    oa_url = data.get("oa_url", "") or data.get("pdf_url", "")
    url = data.get("url", "")
    source = data.get("source", "Web")
    is_predatory = data.get("is_predatory", False)
    safe_name = re.sub(r'[^\w\s\-]', '', title)[:80].strip()
    safe_name = re.sub(r'\s+', '-', safe_name)
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # Download PDF
    pdf_downloaded = False
    pdf_path = None
    if oa_url:
        try:
            async with httpx.AsyncClient(timeout=45.0, follow_redirects=True) as c:
                r = await c.get(oa_url, headers={"User-Agent": "ResearchPilot-ResearchAssistant/2.0"})
                if r.status_code == 200:
                    ct = r.headers.get("content-type", "").lower()
                    if "application/pdf" in ct or "application/octet-stream" in ct or not ct:
                        pdf_name = f"{safe_name}.pdf"
                        pdf_path = UNREAD_WEB / pdf_name
                        counter = 1
                        while pdf_path.exists():
                            pdf_name = f"{safe_name}_{counter}.pdf"
                            pdf_path = UNREAD_WEB / pdf_name
                            counter += 1
                        pdf_path.write_bytes(r.content)
                        pdf_downloaded = True
        except Exception as e:
            print(f"[Research] PDF download failed: {e}")

    # Convert PDF to .md via docling
    md_fulltext = ""
    if pdf_downloaded and pdf_path:
        try:
            md_fulltext = file_to_markdown(pdf_path)
        except Exception as e:
            print(f"[Research] Docling conversion failed: {e}")

    # Generate 12-point analysis from abstract
    analysis = await _generate_12_point_analysis(data)

    pred_warn = "*⚠️ PREDATORY JOURNAL — verify carefully*\n" if is_predatory else ""
    pdf_downloaded_str = "Yes" if pdf_downloaded else "No"
    meta_md = (
        f"# {title}\n"
        f"*Source: Web PDF Import ({source}) | Imported: {ts}*\n"
        f"*Status: 📥 Unread (needs analysis)*\n"
        f"*DOI: {doi}*\n"
        f"*Authors: {', '.join(authors[:8])}*\n"
        f"*Year: {year}*\n"
        f"*Journal: {journal}*\n"
        f"{pred_warn}"
        f"*PDF Downloaded: {pdf_downloaded_str}*\n"
        f"*Type: Full PDF + 12-Point Analysis*\n\n"
        f"---\n\n"
        f"**DOI**: `{doi}`\n\n"
        f"**Authors**: {', '.join(authors[:8])}\n\n"
        f"**Year**: {year}\n\n"
        f"**Journal**: {journal}\n\n"
        f"**URL**: {url}\n\n"
        f"**OA URL**: {oa_url}\n\n"
        f"**Source**: {source}\n\n"
        f"**PDF Downloaded**: {pdf_downloaded_str}\n\n"
        f"---\n\n"
        f"## Abstract\n\n{abstract}\n\n"
        f"---\n\n"
    )
    if analysis:
        meta_md += f"## 12-Point Research Analysis\n\n{analysis}\n\n---\n\n"
    if md_fulltext:
        meta_md += f"## Full Text (via Docling)\n\n{md_fulltext}\n"

    md_name = f"{safe_name}.md"
    md_path = UNREAD_WEB / md_name
    counter = 1
    while md_path.exists():
        md_name = f"{safe_name}_{counter}.md"
        md_path = UNREAD_WEB / md_name
        counter += 1
    md_path.write_text(meta_md, encoding="utf-8")

    return {
        "ok": True,
        "title": title,
        "doi": doi,
        "pdf_downloaded": pdf_downloaded,
        "pdf_file": pdf_path.name if pdf_path and pdf_downloaded else None,
        "md_file": md_name,
        "folder": "INCOMING/UNREAD-WEB",
        "ai_analysis": bool(analysis)
    }

@app.get("/api/research/papers")
async def research_list_papers():
    result = []
    if not UNREAD_WEB.exists():
        return result
    for f in sorted(UNREAD_WEB.iterdir()):
        if f.is_file() and not f.name.startswith("."):
            is_pdf = f.suffix.lower() == ".pdf"
            is_md = f.suffix.lower() == ".md"
            has_meta = None
            if is_md:
                try:
                    content = f.read_text(encoding="utf-8", errors="ignore")
                    status_m = re.search(r'\*Status:\s*(.+?)\*', content)
                    has_meta_s = re.search(r'\*Source: Web (Save|Import|PDF Import)', content)
                    has_meta = bool(has_meta_s)
                except Exception:
                    has_meta = False
            result.append({
                "filename": f.name,
                "stem": f.stem,
                "ext": f.suffix.lower(),
                "size_kb": round(f.stat().st_size / 1024, 1),
                "modified": datetime.datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M"),
                "is_pdf": is_pdf,
                "is_metadata": has_meta if is_md else False
            })
    return result

@app.get("/api/research/pdf/{filename:path}")
async def research_serve_pdf(filename: str):
    fp = (UNREAD_WEB / filename).resolve()
    if not str(fp).startswith(str(UNREAD_WEB.resolve())) or not fp.exists():
        raise HTTPException(404, "PDF not found")
    return FileResponse(str(fp), media_type="application/pdf", filename=filename)

@app.get("/api/research/file/{filename:path}")
async def research_serve_file(filename: str):
    fp = (UNREAD_WEB / filename).resolve()
    if not str(fp).startswith(str(UNREAD_WEB.resolve())) or not fp.exists():
        raise HTTPException(404, "File not found")
    if fp.suffix.lower() == ".md":
        return {"content": fp.read_text(encoding="utf-8")}
    return FileResponse(str(fp))

@app.post("/api/research/move-to-project")
async def research_move_to_project(request: Request):
    data = await request.json()
    filename = data.get("filename", "")
    project = data.get("project", "")
    if not filename or not project:
        raise HTTPException(400, "filename and project required")
    src = UNREAD_WEB / filename
    if not src.exists():
        raise HTTPException(404, f"File not found: {filename}")
    proj_lib = PROJECTS / project / "01-LIBRARY"
    proj_lib.mkdir(parents=True, exist_ok=True)
    dst = proj_lib / filename
    if dst.exists():
        raise HTTPException(409, f"File already exists in project {project}")
    shutil.move(str(src), str(dst))
    stem = Path(filename).stem
    src_md = UNREAD_WEB / f"{stem}.md"
    dst_md = proj_lib / f"{stem}.md"
    if src_md.exists():
        shutil.move(str(src_md), str(dst_md))
    src_pdf = UNREAD_WEB / f"{stem}.pdf"
    dst_pdf = proj_lib / f"{stem}.pdf"
    if src_pdf.exists():
        shutil.move(str(src_pdf), str(dst_pdf))
    return {"ok": True, "filename": filename, "project": project}

@app.delete("/api/research/paper/{filename:path}")
async def research_delete_paper(filename: str):
    fp = UNREAD_WEB / filename
    if fp.exists():
        fp.unlink()
    stem = Path(filename).stem
    for ext in [".md", ".pdf"]:
        companion = UNREAD_WEB / f"{stem}{ext}"
        if companion.exists() and companion.name != filename:
            companion.unlink()
    return {"ok": True, "deleted": filename}

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host=host, port=port, log_level="info")
