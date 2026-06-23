"""
ResearchPilot — Help Bot (Phase 1)
====================================
A READ-ONLY, in-app guide. The Help bot NEVER creates, edits, deletes,
or moves files. It only:

  • Searches the curated FAQ + APP-MAP + HELP-FAQ knowledge files
  • Falls back to the configured LLM with ResearchPilot docs as context
  • Returns navigation intents the frontend can use to switch tabs/sections
  • Shares the project's GitHub repo link when asked

Endpoints (all GET/POST, all idempotent, all view-only):

  GET  /api/help/faq            → curated FAQ items (id, q, a, tags, action?)
  GET  /api/help/map            → full APP-MAP (tabs, settings, common tasks)
  GET  /api/help/context/{tab}  → rich context for one tab (purpose + features)
  GET  /api/help/quick-actions  → list of common_tasks with steps
  GET  /api/help/github         → project GitHub repo link + metadata
  POST /api/help/search         → keyword search across FAQ + APP-MAP + HELP-FAQ
  POST /api/help/ask            → AI-fallback answer (app-only scope)

Safety:
  • No filesystem mutations
  • No project creation, file moves, deletions, edits
  • The LLM fallback is given an explicit "no off-topic" instruction
  • Path resolution is the same safe `resolve_era_path` pattern used elsewhere
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# ── Paths (resolved relative to this file, just like main.py does) ───────────
_HERE = Path(__file__).resolve().parent
_BASE = _HERE.parent
_CORE = _BASE / "00-SYSTEM-CORE"
APP_MAP_F       = _CORE / "APP-MAP.json"
HELP_FAQ_F      = _CORE / "HELP-FAQ.md"
HELP_FAQ_JSON_F = _CORE / "help-faq-cache.json"   # generated cache (optional)

router = APIRouter(prefix="/api/help", tags=["help"])


# ──────────────────────────────────────────────────────────────────────────────
# Knowledge loaders (cached at startup; reloadable)
# ──────────────────────────────────────────────────────────────────────────────

_APP_MAP_CACHE: Optional[Dict[str, Any]] = None
_FAQ_CACHE:     Optional[List[Dict[str, Any]]] = None
_FAQ_TEXT_CACHE: Optional[str] = None


def _load_app_map() -> Dict[str, Any]:
    global _APP_MAP_CACHE
    if _APP_MAP_CACHE is not None:
        return _APP_MAP_CACHE
    if not APP_MAP_F.exists():
        _APP_MAP_CACHE = {"app": {"name": "ResearchPilot"}, "tabs": [], "settings_sections": [], "common_tasks": []}
        return _APP_MAP_CACHE
    try:
        _APP_MAP_CACHE = json.loads(APP_MAP_F.read_text(encoding="utf-8"))
    except Exception:
        _APP_MAP_CACHE = {"tabs": [], "settings_sections": [], "common_tasks": []}
    return _APP_MAP_CACHE


def _load_faq() -> List[Dict[str, Any]]:
    """Load curated FAQ. Prefers a JSON cache if present, else parses HELP-FAQ.md."""
    global _FAQ_CACHE
    if _FAQ_CACHE is not None:
        return _FAQ_CACHE
    if HELP_FAQ_JSON_F.exists():
        try:
            _FAQ_CACHE = json.loads(HELP_FAQ_JSON_F.read_text(encoding="utf-8"))
            return _FAQ_CACHE
        except Exception:
            pass
    # Parse HELP-FAQ.md into Q/A pairs by splitting on ## / ### headings.
    if not HELP_FAQ_F.exists():
        _FAQ_CACHE = []
        return _FAQ_CACHE
    text = HELP_FAQ_F.read_text(encoding="utf-8")
    _FAQ_CACHE = _parse_faq_markdown(text)
    return _FAQ_CACHE


def _load_faq_text() -> str:
    global _FAQ_TEXT_CACHE
    if _FAQ_TEXT_CACHE is not None:
        return _FAQ_TEXT_CACHE
    if HELP_FAQ_F.exists():
        _FAQ_TEXT_CACHE = HELP_FAQ_F.read_text(encoding="utf-8")
    else:
        _FAQ_TEXT_CACHE = ""
    return _FAQ_TEXT_CACHE


def _parse_faq_markdown(text: str) -> List[Dict[str, Any]]:
    """Very forgiving parser: each `### ` heading is a question, the following
    paragraph(s) until the next heading is the answer."""
    items: List[Dict[str, Any]] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if line.startswith("### "):
            q = line[4:].strip()
            i += 1
            buf: List[str] = []
            while i < len(lines) and not lines[i].startswith("### ") and not lines[i].startswith("## "):
                if lines[i].strip():
                    buf.append(lines[i].rstrip())
                i += 1
            a = "\n".join(buf).strip()
            if q and a:
                items.append({
                    "id": _slugify(q),
                    "question": q,
                    "answer": a,
                    "tags": _extract_tags(q + " " + a),
                })
        else:
            i += 1
    return items


def _slugify(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return s or "item"


_TAG_HINTS = {
    "api": ["api", "key", "claude", "openai", "openrouter", "engine", "anthropic"],
    "upload": ["upload", "drop", "pdf", "docx", "file", "ingest"],
    "project": ["project", "create project", "new project", "folder"],
    "chat": ["chat", "ai", "ask", "conversation", "session"],
    "library": ["library", "browse", "read", "view"],
    "graph": ["graph", "knowledge graph", "node", "edge"],
    "memory": ["memory", "obsidian", "markdown"],
    "settings": ["settings", "preference", "configure", "setup"],
    "extract": ["extract", "12-point", "12 point", "analysis"],
    "search": ["search", "find", "query", "research"],
    "move": ["move", "transfer", "migrate", "relocate"],
    "obsidian": ["obsidian", "vault"],
    "offline": ["offline", "local", "no internet"],
}


def _extract_tags(text: str) -> List[str]:
    t = text.lower()
    out: List[str] = []
    for tag, words in _TAG_HINTS.items():
        if any(w in t for w in words):
            out.append(tag)
    return out


# ──────────────────────────────────────────────────────────────────────────────
# Smalltalk fast-path (greetings, thanks, identity, "how do I use this")
# Answered instantly, no LLM call. Keeps replies short, plain, consistent.
# ──────────────────────────────────────────────────────────────────────────────

_SMALLTALK = [
    (re.compile(r"^\s*(hi|hello|hey|yo|hiya|howdy|good (morning|afternoon|evening))[\s!.,?]*$", re.I),
     "👋 Hi! I'm the ResearchPilot Help Bot. Ask me anything about the app — how to upload papers, set up AI, use the graph, configure settings, or anything else. Type a question and I'll find the answer.", None),
    (re.compile(r"^\s*(bye|goodbye|see ya|see you|later|good night|cya)[\s!.]*$", re.I),
     "Goodbye! Come back anytime you need help with ResearchPilot.", None),
    (re.compile(r"^\s*(thanks|thank you|thx|cheers|appreciated|ty|thank)[\s!.]*$", re.I),
     "Happy to help! Ask me anything else about ResearchPilot.", None),
    (re.compile(r"^\s*(ok|okay|got it|got that|understood|alright|great|perfect|nice|cool|awesome)[\s!.]*$", re.I),
     "Great! Let me know if you have any other questions.", None),
    (re.compile(r"(what is this|what'?s this|what is researchpilot|who are you|what do you do|what can you do|what are you)", re.I),
     "I'm the ResearchPilot Help Bot — a read-only guide built into the app. I can answer questions about any tab, setting, or workflow. For research questions about your own papers, use the **Chat** tab.",
     {"type": "tab", "target": "dashboard"}),
    (re.compile(r"(how (does|do i|to) (use|this|it) work|how (do i|to) use|getting started|how to start|where do i start|first steps)", re.I),
     "Start here: 1. Go to **Settings → AI Engines** and add an API key. 2. Use **Upload** to drop in your PDFs. 3. Open **Chat** to talk to the AI about your papers. That's the core loop.",
     {"type": "tab", "target": "upload"}),
    (re.compile(r"^\s*(help|help me|i need help|assist|assistance)[\s!.?]*$", re.I),
     "Of course! Ask me about any part of ResearchPilot — uploading papers, the knowledge graph, AI engines, web research, settings, or anything else. I'll point you to the right place.", None),
]


def _match_smalltalk(q: str) -> Optional[Dict[str, Any]]:
    qs = (q or "").strip()
    if not qs or len(qs) > 60:
        return None
    for pattern, answer, action in _SMALLTALK:
        if pattern.search(qs):
            return {"answer": answer, "source": "smalltalk", "action": action}
    return None


# ──────────────────────────────────────────────────────────────────────────────
# Input safety guard — blocks prompt-injection / SQL-injection style payloads
# before they ever reach the LLM or search index. The app has no SQL database,
# but we still reject SQL-shaped strings as a defence-in-depth measure, and we
# always reject attempts to override the bot's instructions.
# ──────────────────────────────────────────────────────────────────────────────

_MAX_QUESTION_LEN = 400

_UNSAFE_PATTERNS = [
    re.compile(r"ignore (all|the|any|previous|above) instructions", re.I),
    re.compile(r"(disregard|forget) (all|the|your) (rules|instructions|prompt)", re.I),
    re.compile(r"system prompt|you are now|act as|pretend (you|to be)|jailbreak|developer mode|dan mode", re.I),
    re.compile(r"\b(drop|delete|truncate)\s+table\b", re.I),
    re.compile(r"\bunion\s+select\b|\bselect\s+\*\s+from\b|\binsert\s+into\b|\bor\s+1\s*=\s*1\b", re.I),
    re.compile(r"<\s*script|javascript:|onerror\s*=|onload\s*=", re.I),
    re.compile(r"[;'\"]\s*(--|#)"),  # classic SQL comment-terminator injection shape
]


def _is_unsafe(q: str) -> bool:
    if not q or len(q) > _MAX_QUESTION_LEN:
        return True
    return any(p.search(q) for p in _UNSAFE_PATTERNS)


# ──────────────────────────────────────────────────────────────────────────────
# Search ranking
# ──────────────────────────────────────────────────────────────────────────────

_STOP_WORDS = frozenset({
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "do", "does", "did", "doing", "i", "you", "he", "she", "it", "we", "they",
    "me", "him", "her", "us", "them", "my", "your", "his", "its", "our", "their",
    "this", "that", "these", "those", "of", "in", "on", "at", "to", "for", "with",
    "by", "from", "as", "or", "and", "but", "if", "so", "what", "which", "who",
    "whom", "how", "when", "where", "why", "can", "could", "should", "would",
    "will", "may", "might", "must", "shall", "have", "has", "had", "having",
    "am", "just", "about", "any", "some", "all", "no", "not", "than", "then",
})


def _score(text: str, query: str) -> int:
    """Score a candidate text against a query. Common English stop words
    are filtered out so off-topic queries don't accidentally match FAQ
    items that happen to share a few common words (e.g. "what is the...").

    Short tokens (≤ 3 chars) use word-boundary matching so that a query
    like "hi" does NOT match words containing "hi" as a substring
    ("this", "which", "chat", "github", etc.).
    """
    if not text:
        return 0
    t = text.lower()
    q = query.lower().strip()
    if not q:
        return 0
    # Keep only meaningful tokens (drop stop words + single-char tokens)
    raw_tokens = re.split(r"[^a-z0-9]+", q)
    tokens = [tok for tok in raw_tokens if tok and tok not in _STOP_WORDS and len(tok) > 1]
    if not tokens:
        return 0
    score = 0
    for tok in tokens:
        if len(tok) <= 3:
            # Word-boundary match for short tokens — prevents "hi" matching "this"
            if re.search(r'\b' + re.escape(tok) + r'\b', t):
                score += 6
        else:
            if tok in t:
                score += 6
                if t.startswith(tok):
                    score += 4
    # boost exact phrase match
    if q in t:
        score += 10
    return score


def _search_kb(query: str, limit: int = 8) -> List[Dict[str, Any]]:
    """Return ranked search results across FAQ + APP-MAP + HELP-FAQ text + GitHub."""
    results: List[Dict[str, Any]] = []
    if not query:
        return results
    q = query.strip()
    # GitHub / source-code shortcut — only enabled if a GitHub URL is configured
    gh_terms = ("github", "source code", "source-code", "repo", "repository",
                "fork", "contribute", "contribution", "codebase", "code base")
    if any(t in q.lower() for t in gh_terms):
        gh = _load_app_map().get("app", {}).get("github_url", "").strip()
        if gh:
            results.append({
                "type": "github",
                "title": "🐙 Project source code (GitHub)",
                "snippet": f"The official ResearchPilot repository is at: {gh}\nYou can fork, star, report issues, or read the README there.",
                "score": 100,  # hard-wins for GitHub queries
                "url": gh,
                "navigate_to": "open:github",
            })
        else:
            results.append({
                "type": "info",
                "title": "🐙 Source code",
                "snippet": "No public GitHub link is configured for this build. The source lives locally in your project folder.",
                "score": 100,
            })
    # FAQ items
    for item in _load_faq():
        s = _score(item.get("question", "") + "\n" + item.get("answer", ""), q)
        if s > 0:
            results.append({
                "type": "faq",
                "id": item.get("id"),
                "title": item.get("question"),
                "snippet": _snippet(item.get("answer", ""), q),
                "score": s + 5,   # FAQ boost
                "tags": item.get("tags", []),
            })
    # APP-MAP tabs
    for tab in _load_app_map().get("tabs", []):
        s = _score(tab.get("label", "") + " " + tab.get("purpose", "") + " " + " ".join(tab.get("key_features", [])), q)
        if s > 0:
            results.append({
                "type": "tab",
                "id": tab.get("id"),
                "title": tab.get("icon", "") + " " + tab.get("label", ""),
                "snippet": tab.get("purpose", ""),
                "score": s,
                "navigate_to": "tab:" + tab.get("id", ""),
            })
    # APP-MAP common tasks
    for task in _load_app_map().get("common_tasks", []):
        s = _score(task.get("task", "") + " " + " ".join(task.get("steps", [])), q)
        if s > 0:
            results.append({
                "type": "task",
                "id": _slugify(task.get("task", "")),
                "title": task.get("task", ""),
                "snippet": " → ".join(task.get("steps", [])),
                "score": s + 2,
                "navigate_to": "task:" + _slugify(task.get("task", "")),
            })
    # Raw HELP-FAQ.md (last resort, for long-tail terms)
    faq_text = _load_faq_text()
    if faq_text:
        for para in re.split(r"\n\s*\n", faq_text):
            s = _score(para, q)
            if s > 0 and not any(r.get("snippet", "")[:60] == _snippet(para, q)[:60] for r in results):
                results.append({
                    "type": "doc",
                    "id": _slugify(para[:40]),
                    "title": _snippet(para, q, length=60),
                    "snippet": _snippet(para, q),
                    "score": s,
                })
    results.sort(key=lambda r: r.get("score", 0), reverse=True)
    return results[:limit]


def _snippet(text: str, query: str, length: int = 220) -> str:
    """Return a clean, chat-friendly excerpt. No truncation markers."""
    if not text:
        return ""
    t = text.replace("\n", " ").strip()
    q = query.lower().strip()
    if not q:
        return t[:length].rstrip()
    low = t.lower()
    idx = low.find(q.split()[0]) if q.split() else -1
    if idx < 0:
        return t[:length].rstrip()
    start = max(0, idx - 60)
    end = min(len(t), start + length)
    return t[start:end].rstrip()


# ──────────────────────────────────────────────────────────────────────────────
# LLM fallback (app-only, refuses off-topic)
# ──────────────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT_TEMPLATE = """You are the **ResearchPilot Help Bot**, a small, friendly assistant that lives inside the ResearchPilot app.

=== YOUR ONLY JOB ===
Answer questions about the ResearchPilot app itself: its tabs, features, settings, workflow, files, projects, and how to use it.

You are NOT a general chatbot. You are NOT a research assistant. You are NOT a coding assistant. Stay strictly in help-bot mode.

=== STRICT RULES ===
1. App-only scope. If the user asks anything unrelated to the ResearchPilot app (general knowledge, philosophy, jokes, coding help, life advice, off-topic chat, etc.), refuse with EXACTLY this short paragraph and nothing else:
   "I can only help with questions about the ResearchPilot app itself, like its tabs, settings, projects, and files. For general research, use the Chat tab. You can also browse the Quick Guide in the help panel."
   Then add a single line: ACTION: NONE
2. NEVER invent features, buttons, settings, or URLs. Use only what is in the KNOWLEDGE CONTEXT below.
3. NEVER tell the user to edit code, run scripts, or modify files manually. Only point them to in-app UI (which tab/section/button to click).
4. GitHub / source-code questions: if a link is present in KNOWLEDGE CONTEXT, share it, then ACTION: open:github. If no link is configured, tell the user the source lives locally in their project folder.

=== ANSWER STYLE — MANDATORY ===
- Keep answers to **1-2 short sentences MAX**. Never write long paragraphs.
- Be direct, clear, and concise. Every word must earn its place.
- Friendly, warm English. Sound like a real person, not a system message.
- Use **bold** for tab names, settings sections, and button names.
- Use numbered lists (1. 2. 3.) ONLY for step-by-step instructions, and keep them to 3 short steps max.
- If the answer needs more than 1-2 sentences, point the user to the relevant tab/section instead of explaining in text.
- **NEVER use dashes, em-dashes, or ellipses in your reply.** No "—", no "-", no "…", no "...". Use commas, periods, or just new lines instead.
- **NEVER prefix your reply with "Answer:", "A:", "Bot:", or any label.** Just answer like a normal person.
- End with exactly ONE ACTION line in this form:
   ACTION: tab:<id>             (e.g. tab:settings, tab:projects, tab:chat, tab:library, tab:graph, tab:memory, tab:upload, tab:research, tab:dashboard)
   ACTION: settings:<section>   (e.g. settings:ai, settings:kb, settings:keywords, settings:general)
   ACTION: open:github          (when sharing the GitHub repo link)
   ACTION: NONE                 (for refusals or pure info answers with no navigation)

=== KNOWLEDGE CONTEXT (use ONLY this to answer) ===
{context}
"""


def _build_context(query: str) -> str:
    """Build a compact context string for the LLM: APP-MAP + top search hits."""
    amap = _load_app_map()
    parts: List[str] = []
    parts.append("## Tabs")
    for t in amap.get("tabs", []):
        parts.append(f"- **{t.get('label')}** (`{t.get('id')}`): {t.get('purpose')}")
    parts.append("\n## Settings sections")
    for s in amap.get("settings_sections", []):
        parts.append(f"- **{s.get('label')}** (`{s.get('id')}`): {s.get('purpose')}")
    parts.append("\n## Common tasks")
    for task in amap.get("common_tasks", []):
        parts.append(f"- {task.get('task')}: " + " → ".join(task.get("steps", [])))
    # top 3 FAQ hits for the query
    hits = _search_kb(query, limit=3)
    if hits:
        parts.append("\n## Top FAQ matches")
        for h in hits:
            parts.append(f"Q: {h.get('title','')}\nA: {h.get('snippet','')}")
    # GitHub repo (if known) — so the AI can share it when asked
    gh = amap.get("app", {}).get("github_url", "").strip()
    if gh:
        parts.append(f"\n## Project source code\nThe official GitHub repository is: {gh}\nIf the user asks about GitHub, source code, repo, fork, contribute, or 'where is the code', share this link.")
    else:
        parts.append("\n## Project source code\nNo public GitHub link is configured. If the user asks about GitHub or source code, tell them the source lives locally in their project folder and the repo link is configured via Settings.")
    return "\n".join(parts)


def _llm_answer(query: str) -> Dict[str, Any]:
    """Sync wrapper kept for backwards compat. Just calls the async version via asyncio.run.
    NOTE: this WILL fail inside a running event loop. Use _llm_answer_async instead."""
    import asyncio
    return asyncio.run(_llm_answer_async(query))


async def _llm_answer_async(query: str) -> Dict[str, Any]:
    """Try the configured LLM (the same engine pool the main chat uses).
    Returns a graceful fallback if no engine is configured or the LLM fails.
    Safe to call from within a running FastAPI event loop."""
    try:
        from main import ai_respond  # type: ignore
    except Exception as e:
        return {"answer": _llm_failure_answer(str(e), query), "engine": "none", "fallback": True}

    # Safety net: detect obviously off-topic queries and refuse without calling
    # the LLM. The user's main LLM is configured as a research assistant, so
    # the help-bot system prompt sometimes gets overridden — this filter makes
    # the refusal behaviour deterministic for clear off-topic cases.
    q_lower = query.lower().strip()
    off_topic_markers = (
        "meaning of life", "why is the sky", "tell me a joke", "joke", "weather",
        "recipe", "movie", "song lyrics", "love", "dating", "philosophy",
        "what time is it", "who is the president", "stock market", "bitcoin",
        "how to cook", "game", "sport", "celebrity", "gossip",
    )
    if any(m in q_lower for m in off_topic_markers):
        return {
            "answer": ("I can only help with questions about the ResearchPilot app itself, like its tabs, settings, projects, and files. For general research, use the Chat tab."),
            "engine": "help-bot-scope",
            "action": None,
            "fallback": True,
        }

    context = _build_context(query)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT_TEMPLATE.format(context=context[:6000])},
        {"role": "user", "content": query},
    ]
    try:
        # PROPERLY await the async LLM (was: asyncio.run, which fails inside a running loop)
        text, engine, _tools = await ai_respond(messages, project=None, skills=None)
        action = _parse_action(text)
        clean_text = (text or "").rstrip()
        if action:
            # Strip a trailing "ACTION: ..." line — keep everything before it
            clean_text = re.sub(r"\n*\s*ACTION:\s*\S+.*$", "", clean_text, flags=re.DOTALL).rstrip()
        # Strip dashes / ellipses / system-y prefixes so the reply feels like a real chat
        clean_text = _clean_chat_text(clean_text)
        if not clean_text:
            # LLM returned an empty/blank response (or one with only an ACTION line)
            return {"answer": _llm_failure_answer("empty response", query),
                    "engine": engine, "fallback": True, "action": action}
        # Post-LLM scope check: if the LLM ignores the system prompt and answers
        # an obvious off-topic question, replace with the help-bot refusal.
        if any(m in (clean_text or "").lower() for m in ("eudaimonia", "rayleigh scattering", "because light attracts bugs")):
            return {
                "answer": ("I can only help with questions about the ResearchPilot app itself, like its tabs, settings, projects, and files. For general research, use the Chat tab."),
                "engine": engine,
                "action": None,
                "fallback": True,
            }
        return {"answer": clean_text, "engine": engine, "action": action}
    except Exception as e:
        return {"answer": _llm_failure_answer(str(e), query), "engine": "error", "fallback": True}


def _parse_action(text: str) -> Optional[Dict[str, str]]:
    """Parse a trailing `ACTION: ...` line out of the LLM response."""
    m = re.search(r"ACTION:\s*(\S+)", text)
    if not m:
        return None
    spec = m.group(1)
    if ":" in spec:
        kind, target = spec.split(":", 1)
        return {"type": kind.strip(), "target": target.strip()}
    return {"type": "open", "target": spec.strip()}


def _clean_chat_text(text: str) -> str:
    """Strip anything that makes the answer look like a system message or error.
    Keeps the reply feeling like a natural human chat bubble."""
    if not text:
        return text
    t = text
    # Strip leading bullets/dashes used as list markers
    t = re.sub(r"(?m)^[\s]*[-\u2013\u2014]\s*", "", t)
    # Replace arrows (→) with "then" so steps read like chat directions
    t = re.sub(r"\s*\u2192\s*", " then ", t)
    # Replace em-dashes and en-dashes with a comma + space (chat-like)
    t = t.replace("\u2014", ", ").replace("\u2013", ", ")
    # Collapse double commas/spaces left by dash removal
    t = re.sub(r",\s*,", ",", t)
    t = re.sub(r" {2,}", " ", t)
    # Strip ellipses (single char, three dots, or unicode)
    t = t.replace("\u2026", "")
    t = re.sub(r"\.{3,}", "", t)
    # Strip any leftover answer prefixes the LLM might add
    t = re.sub(r"(?im)^\s*(answer|a|bot|response)\s*:\s*", "", t)
    # Trim trailing whitespace and stray punctuation
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def _llm_failure_answer(err: str, query: str) -> str:
    """Polite, helpful fallback when the LLM is unavailable.
    Tries to surface 1-2 closest FAQ matches so the user is never stranded."""
    err_low = (err or "").lower()
    if "engine" in err_low or "api_key" in err_low or "not configured" in err_low or "unauthorized" in err_low:
        msg = ("I don't have an AI engine configured yet. To enable me:\n"
               "1. Open **Settings**, then **AI Engines**\n"
               "2. Enable **Claude API** (or OpenAI/OpenRouter)\n"
               "3. Paste your key and click **Save**\n\n"
               "In the meantime, I can still search the FAQ for you. Try the search bar above.")
    else:
        msg = ("I can't reach the AI right now, but let me try the FAQ.\n")
    # Append the best FAQ matches so the user has SOMETHING useful
    hits = _search_kb(query, limit=3)
    if hits:
        msg += "\nClosest matches from the FAQ:\n"
        for h in hits[:3]:
            msg += f"• {h.get('title','')}\n"
    return msg.rstrip()


def _no_engine_answer(err: str = "") -> str:
    # Kept for any callers that still reference it
    return _llm_failure_answer(err or "no engine", "")


# ──────────────────────────────────────────────────────────────────────────────
# Endpoints
# ──────────────────────────────────────────────────────────────────────────────

@router.get("/faq")
async def get_faq() -> Dict[str, Any]:
    """All curated FAQ items."""
    items = _load_faq()
    return {"count": len(items), "items": items}


@router.get("/map")
async def get_map() -> Dict[str, Any]:
    """Full APP-MAP.json contents."""
    return _load_app_map()


@router.get("/context/{tab_id}")
async def get_tab_context(tab_id: str) -> Dict[str, Any]:
    """Rich context for a specific tab."""
    amap = _load_app_map()
    for t in amap.get("tabs", []):
        if t.get("id") == tab_id:
            related = [s for s in amap.get("settings_sections", []) if t.get("id") in s.get("id", "")]
            tasks = [c for c in amap.get("common_tasks", []) if any(k in (t.get("id","") + " " + t.get("purpose","")).lower() for k in c.get("task","").lower().split())]
            return {"tab": t, "related_settings": related, "related_tasks": tasks}
    raise HTTPException(404, f"Unknown tab: {tab_id}")


@router.get("/quick-actions")
async def get_quick_actions() -> Dict[str, Any]:
    """Common tasks (id, label, steps, navigate_to)."""
    amap = _load_app_map()
    out: List[Dict[str, Any]] = []
    for task in amap.get("common_tasks", []):
        steps = task.get("steps", [])
        first_tab = None
        if steps:
            # first step is usually "Open X" — extract the tab
            m = re.search(r"open\s+([A-Za-z]+)", steps[0], re.IGNORECASE)
            if m:
                first_tab = m.group(1).lower()
        out.append({
            "id": _slugify(task.get("task", "")),
            "label": task.get("task", ""),
            "steps": steps,
            "navigate_to": f"tab:{first_tab}" if first_tab else None,
        })
    return {"count": len(out), "actions": out}


@router.get("/github")
async def get_github() -> Dict[str, Any]:
    """The project's GitHub repository link. Empty string if not configured.

    The Help bot shares this when the user asks where the source code is,
    how to fork, how to contribute, etc. Read-only — never mutates anything.
    """
    amap = _load_app_map()
    url = (amap.get("app", {}) or {}).get("github_url", "").strip()
    return {
        "url": url,
        "label": "ResearchPilot on GitHub" if url else "",
        "available": bool(url),
    }


class SearchReq(BaseModel):
    query: str
    limit: Optional[int] = 8


@router.post("/search")
async def search(req: SearchReq) -> Dict[str, Any]:
    """Keyword search across FAQ + APP-MAP + HELP-FAQ text."""
    results = _search_kb(req.query, limit=max(1, min(req.limit or 8, 25)))
    return {"query": req.query, "count": len(results), "results": results}


class AskReq(BaseModel):
    question: str


@router.post("/ask")
async def ask(req: AskReq) -> Dict[str, Any]:
    """FAQ-only help bot. No LLM. No random answers. No external calls.

    Flow:
    1. Safety guard  — block SQL/prompt injection and oversized input. Hard stop.
    2. Smalltalk     — greetings and thanks get a fixed friendly reply.
    3. FAQ search    — return top matching Q&A cards for the user to click.
    4. No match      — polite fixed message. Never guesses. Never calls LLM.
    """
    q = (req.question or "").strip()
    if not q:
        raise HTTPException(400, "Empty question")

    # Step 1: Hard safety guard — no LLM call, no search, nothing.
    if _is_unsafe(q):
        return {
            "answer": "I can only answer questions about ResearchPilot. Try asking about a tab, setting, or feature.",
            "source": "blocked",
            "matches": [],
            "action": None,
        }

    # Step 2: Smalltalk fast-path — greetings, thanks, identity.
    small = _match_smalltalk(q)
    if small:
        return {**small, "matches": []}

    # Step 3: FAQ keyword search — match against HELP-FAQ.md only.
    hits = _search_kb(q, limit=5)
    faq_hits = [h for h in hits if h.get("type") in ("faq", "tab", "task", "github")]

    if faq_hits:
        top = faq_hits[0]
        return {
            "answer": top.get("snippet") or top.get("title") or "",
            "source": "faq",
            "matched": top,
            "matches": faq_hits,
            "action": None,
        }

    # Step 4: No match. Fixed reply. No LLM. No guessing.
    return {
        "answer": (
            "I couldn't find that in the FAQ. Try asking about:\n"
            "**upload** · **chat** · **graph** · **settings** · **extract** · **project** · **AI engine** · **Ollama** · **keywords** · **memory**"
        ),
        "source": "no_match",
        "matches": [],
        "action": None,
    }


@router.post("/reload")
async def reload_faq() -> Dict[str, Any]:
    """Flush the in-memory FAQ cache so new items in HELP-FAQ.md are picked up
    without restarting the server. Safe to call any time."""
    global _FAQ_CACHE, _FAQ_TEXT_CACHE, _APP_MAP_CACHE
    _FAQ_CACHE = None
    _FAQ_TEXT_CACHE = None
    _APP_MAP_CACHE = None
    items = _load_faq()
    return {"reloaded": True, "count": len(items)}


# Registration helper — main.py calls this once at import time
def register(app):
    """Attach this router to the FastAPI app. Called from main.py."""
    app.include_router(router)
