"""
Filename standardization utilities — Protocol 7.

Every paper-related artifact in ResearchPilot uses the canonical format:

    {AuthorLastName}_{Year}[_{note}][_{disambiguator}].{ext}

Where:
    AuthorLastName  — first author's surname, sanitized for filesystem safety
    Year            — 4-digit publication year
    note            — optional short tag (summary / details / quotes / chapter3 / etc.)
    disambiguator   — auto-appended counter if a name collides (2, 3, 4, ...)

Special rules:
    - Extraction files keep the P-code prefix so citations like
      ``[P001, 2024]`` (Protocol 4) stay stable:
          P001_Foshay_2015.md
    - Library PDFs have no P-code:
          Foshay_2015.pdf
    - Web imports and uploaded files use the same author_year format.
    - If author or year cannot be determined, fall back gracefully:
          Untitled_{YearOrUploadDate}.md
"""
from __future__ import annotations
import re
import unicodedata
from pathlib import Path
from typing import Optional, Tuple


# ─── Name sanitization ───────────────────────────────────────────────────────
# Allowed: letters, digits, underscore, hyphen, dot (for the extension).
# Everything else collapses to underscore. This keeps the name safe on
# Windows / macOS / Linux and shell-friendly.

_DISALLOWED = re.compile(r'[^\w\-.]', re.UNICODE)
_MULTI_UNDERSCORE = re.compile(r'_+')
_TRAILING_UNDERSCORE = re.compile(r'(_|\.)+$')


def _sanitize_token(token: str) -> str:
    """Make a string safe for use in a filename. Strips diacritics, removes
    forbidden characters, collapses runs of underscores, trims edge junk."""
    if not token:
        return ""
    # Normalize unicode: "Müller" → "Muller", "François" → "Francois"
    token = unicodedata.normalize("NFKD", token)
    token = token.encode("ascii", "ignore").decode("ascii")
    token = _DISALLOWED.sub("_", token)
    token = _MULTI_UNDERSCORE.sub("_", token)
    token = _TRAILING_UNDERSCORE.sub("", token)
    return token.strip("._-")


# ─── APA reference parser ────────────────────────────────────────────────────
# The 12-Point Extraction protocol emits a "1. **APA Reference**: ..." line.
# We parse it for first-author surname + year.
#
# APA format examples we must handle:
#   "Smith, J. (2020). Title here. *Journal*, 10(2), 100-110."
#   "Smith, J., & Doe, A. (2020). Title here. *Journal*."
#   "Smith, J., Doe, A., & Roe, B. (2020). Title. *Journal*."
#   "Smith, J., Doe, A., ... (2020a). Title."   ← in-text disambiguation letter
#   "Alyami, A., & Yang, H. (2023). Title."
#   "O'Brien, K. (2019). ..."        → surname "OBrien"
#   "Van Der Berg, L. (2018). ..."   → surname "Van_Der_Berg"

_APA_YEAR = re.compile(r'\((\d{4})([a-z]?)\)\s*\.')   # (2020). or (2020a).
_APA_FIRST_AUTHOR = re.compile(
    r'^\s*\**\s*([A-Z][A-Za-z\'\-\s]+?),\s*[A-Z]\.'  # "Smith, J."
)
# Find an APA line anywhere in multi-line text. Matches:
#   "1. **APA Reference**: Smith..."
#   "1. APA Reference: Smith..."
#   "**APA Reference**: Smith..."
#   "APA Reference: Smith..."
_APA_LINE = re.compile(
    r'\d*\.\s*\*+\s*APA\s+Reference\s*\*+\s*:\s*'
    r'|'
    r'^\*+\s*APA\s+Reference\s*\*+\s*:\s*',
    re.IGNORECASE | re.MULTILINE,
)


def parse_apa_reference(text: str) -> Tuple[Optional[str], Optional[str]]:
    """Extract (surname, year) from a string that contains an APA-style
    reference. Returns (None, None) if neither can be found.

    The parser is intentionally permissive: it locates the APA Reference line
    anywhere in the input, then looks for a Year + Surname pattern in the
    surrounding 300 characters.
    """
    if not text:
        return None, None

    # Locate the APA Reference line and take the 300 chars after it
    m = _APA_LINE.search(text)
    if m:
        work = text[m.end():m.end() + 300]
    else:
        work = text[:600]

    work = work.replace("**", "").strip()
    if not work:
        return None, None

    # Year: look for (YYYY) or (YYYYa)
    year = None
    m = _APA_YEAR.search(work[:200])
    if m:
        year = m.group(1)

    # First author: anchored at start (after the prefix is stripped), else search
    surname = None
    m = _APA_FIRST_AUTHOR.match(work)
    if m:
        surname = m.group(1).strip()
    else:
        m = re.search(r'([A-Z][A-Za-z\'\-\s]{1,40}?),\s*[A-Z]\.', work[:200])
        if m:
            surname = m.group(1).strip()

    if surname:
        surname = _sanitize_token(surname)
    return surname or None, year or None


# ─── Best-effort PDF text scanner ────────────────────────────────────────────
# When a PDF is uploaded but no extraction exists yet, we scan the first
# 2000 chars of the extracted text for an author + year hint.

def parse_pdf_text_for_metadata(text: str) -> Tuple[Optional[str], Optional[str]]:
    """Heuristically find (surname, year) in raw PDF text. Used as a
    fallback when no APA reference line exists yet."""
    if not text:
        return None, None

    # Try APA parser first
    surname, year = parse_apa_reference(text)
    if surname and year:
        return surname, year

    # Year: find any 4-digit year between 1980 and current+1
    year_match = re.search(r'\b(19[89]\d|20[0-3]\d)\b', text[:3000])
    year = year_match.group(1) if year_match else None

    # Common false positives that match the "Surname, X." pattern but
    # are not actually author names.
    _FALSE_POSITIVES = {
        "vol", "no", "pp", "eq", "ed", "eds", "university", "department",
        "school", "college", "journal", "press", "publishers", "publisher",
        "research", "studies", "review", "quarterly", "annual", "bulletin",
        "proceedings", "letters", "communications", "transactions", "series",
        "section", "chapter", "figure", "table", "page", "issue", "vol",
    }

    # Author: look for a line that has a comma followed by an initial,
    # e.g. "Smith, J." or "Smith, J. K."
    surname = None
    for m in re.finditer(r'\b([A-Z][a-zA-Z\-\']{1,30}),\s*[A-Z]\.', text[:2000]):
        cand = _sanitize_token(m.group(1))
        if cand.lower() not in _FALSE_POSITIVES:
            surname = cand
            break

    return surname, year


# ─── Canonical filename builder ──────────────────────────────────────────────

def build_paper_filename(
    author: Optional[str],
    year: Optional[str],
    note: Optional[str] = None,
    ext: str = ".md",
) -> str:
    """Build the canonical filename for a paper-related artifact.

    Examples:
        build_paper_filename("Foshay", "2015")                  → "Foshay_2015.md"
        build_paper_filename("Smith", "2024", note="summary")   → "Smith_2024_summary.md"
        build_paper_filename(None, "2024")                      → "Untitled_2024.md"
        build_paper_filename("Smith", None)                     → "Smith_Undated.md"
        build_paper_filename(None, None)                        → "Untitled_Undated.md"
        build_paper_filename("S", "2024", ext="")               → "S_2024"
    """
    a = _sanitize_token(author) if author else ""
    y = _sanitize_token(year) if year else ""

    if not a:
        a = "Untitled"
    if not y:
        y = "Undated"

    parts = [a, y]
    if note:
        n = _sanitize_token(note)
        if n:
            parts.append(n)

    base = "_".join(parts)
    # Cap the name at 100 chars before the extension to keep paths manageable
    if len(base) > 100:
        base = base[:100].rstrip("_-.")
    # Extension is optional — empty ext returns the stem only
    if ext:
        if not ext.startswith("."):
            ext = "." + ext
        return f"{base}{ext}"
    return base


def build_extraction_filename(
    code: str,                       # "P001"
    author: Optional[str],
    year: Optional[str],
    note: Optional[str] = None,
) -> str:
    """Build an extraction filename with the P-code prefix preserved so that
    the Protocol 4 citation contract ``[P001, 2024]`` keeps working."""
    code = _sanitize_token(code) or "P000"
    stem = build_paper_filename(author, year, note=note, ext="")
    return f"{code}_{stem}.md"


# ─── Disambiguation helper ───────────────────────────────────────────────────

def disambiguate_filename(folder: Path, base_name: str) -> str:
    """If ``base_name`` already exists in ``folder``, append ``_2``, ``_3`` ...
    until a free name is found. ``base_name`` is the full filename including
    extension.

    Existing files in the OLD format (P### - Content Extraction.md) are
    also considered as collisions, so a re-rename always picks a fresh slot.
    """
    candidate = base_name
    if not (folder / candidate).exists():
        return candidate
    stem, dot, ext = candidate.rpartition(".")
    if not dot:
        stem, ext = candidate, ""
    n = 2
    while (folder / f"{stem}_{n}{('.' + ext) if ext else ''}").exists():
        n += 1
        if n > 9999:   # pathological — bail out
            break
    return f"{stem}_{n}{('.' + ext) if ext else ''}"


# ─── Convenience: detect legacy P-code filenames ─────────────────────────────

# Require spaces around the separator (` - ` or ` _ `) so the canonical form
# `P001_Foshay_2015.md` (no spaces around the underscore) is NOT matched as
# legacy. The legacy style is `P001 - Content Extraction.md`.
_LEGACY_P_EXTRACTION = re.compile(r'^P(\d+)\s+[-_]\s+.+\.md$', re.IGNORECASE)
# Author may include "et al." so dots are allowed in the author class.
# We anchor on " - " or " _ " (with surrounding spaces) as the separator so
# that the author class doesn't slurp up the year. Extension may be .md or
# .pdf (or any alphanumeric ext) — match `\.[A-Za-z0-9]+$` at the end.
_LEGACY_AUTHOR_YEAR   = re.compile(
    r'^([A-Z][\w\-\s\.]+?)\s+[-_]\s+(\d{4})\.[A-Za-z0-9]+$', re.IGNORECASE)


def is_legacy_p_extraction(name: str) -> bool:
    """``P001 - Content Extraction.md`` style → True."""
    return bool(_LEGACY_P_EXTRACTION.match(name))


def is_legacy_author_year(name: str) -> bool:
    """``Foshay - 2015.pdf`` or ``Alyami et al. - 2023.md`` style → True.

    These are the hand-typed filenames that some users (e.g. this repo)
    already use. The new format is ``Foshay_2015.md``."""
    return bool(_LEGACY_AUTHOR_YEAR.match(name))


def parse_legacy_author_year(name: str) -> Tuple[Optional[str], Optional[str]]:
    """Best-effort parse of ``Foshay et al. - 2015.pdf`` → (``Foshay``, ``2015``)."""
    m = _LEGACY_AUTHOR_YEAR.match(name)
    if not m:
        return None, None
    raw_author = m.group(1).strip()
    # "et al." → keep first author only ("Alyami et al." → "Alyami")
    raw_author = re.split(r'\s+et\s+al\.?', raw_author, maxsplit=1, flags=re.IGNORECASE)[0]
    # "and Axelton" / "& Axelton" → keep first author
    raw_author = re.split(r'\s+(?:and|&)\s+', raw_author, maxsplit=1, flags=re.IGNORECASE)[0]
    return _sanitize_token(raw_author), m.group(2)


# ─── Author / year helpers for web import payloads ──────────────────────────
# Search-result payloads from Crossref / OpenAlex / Semantic Scholar hand us
# `authors` as a list of full names. We just need the first author's surname.

def first_author_surname(authors) -> Optional[str]:
    """Extract the first author's surname from a list of full names.

    Handles many shapes:
        ["John Smith", ...]              → "Smith"
        ["Alyami A.", ...]               → "Alyami"
        ["Alyami, A.", ...]              → "Alyami"
        ["Smith, J. K.", ...]            → "Smith"
        ["van der Berg, L.", ...]        → "Berg"   (last whitespace token after comma)
        ["Madonna", ...]                 → "Madonna"  (single name, no comma)
    """
    if not authors:
        return None
    first = str(authors[0]).strip()
    if not first:
        return None
    if "," in first:
        # APA-ish "Surname, Initials." → take before the comma
        return _sanitize_token(first.split(",", 1)[0])
    # No comma — last whitespace-separated token is the surname
    parts = first.split()
    if len(parts) >= 2:
        return _sanitize_token(parts[-1])
    return _sanitize_token(first)


def canonical_from_web_payload(authors, year: Optional[str], title: str = "") -> Tuple[Optional[str], Optional[str]]:
    """Build (author, year) for a web import from a search-result payload.

    Falls back gracefully:
        1. First author surname from `authors` list
        2. First word of `title` if no authors
        3. ``None`` if nothing is usable (caller decides the fallback)
    """
    author = first_author_surname(authors)
    if not author and title:
        words = re.findall(r"[A-Za-z][A-Za-z'\-]+", title)
        if words:
            author = _sanitize_token(words[0])
    yr = _sanitize_token(str(year)) if year else None
    return author, yr


def next_extraction_code(folder: Path) -> str:
    """Return the next free ``P###`` code in a folder. Skips both legacy
    (``P001 - Content Extraction.md``) and new (``P001_Foshay_2015.md``)
    forms. Returns ``P001`` for an empty folder.
    """
    used = []
    for f in folder.glob("P*.md"):
        m = re.match(r"P(\d+)", f.stem)
        if m:
            used.append(int(m.group(1)))
    return f"P{(max(used, default=0) + 1):03d}"
