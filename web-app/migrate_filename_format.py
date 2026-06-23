"""
Filename-format migration (Protocol 7) — opt-in, dry-run by default.

Renames existing files in the ResearchPilot system to the canonical
``{Author}_{Year}[_{note}][_{disambiguator}].{ext}`` format:

    P001 - Content Extraction.md   ->  P001_Foshay_2015.md
    P002 - Content Extraction.md   ->  P002_Alyami_2023.md
    Foshay et al. - 2015.pdf       ->  Foshay_2015.pdf
    Bansal and Axelton - 2024.pdf  ->  Bansal_Axelton_2024.pdf
    GEORGIOS 2025.md               ->  Georgios_2025.md   (or Untitled_2025.md)

The script reads the APA reference from the first lines of each
extraction .md (Protocol 4 requires it) and uses the PDF first-page
text-mining fallback for library PDFs.

USAGE
    python migrate_filename_format.py              # dry-run (default)
    python migrate_filename_format.py --apply      # actually rename
    python migrate_filename_format.py --backup     # copy old files to .bak/ first
    python migrate_filename_format.py --apply --backup

The script never deletes a file. It only renames. If a target name is
already taken (e.g. two papers with the same author+year), it appends
``_2``, ``_3`` etc.

Run from the project root:
    cd web-app
    python migrate_filename_format.py
"""
import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Make sibling _filename_utils importable
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _filename_utils as fu


# ─── Resolve the project root from this script ───────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent


def project_path() -> Path:
    """Mirror main.py's BASE auto-detection."""
    import os
    env = os.getenv("RESEARCHPILOT_HOME", "").strip()
    return Path(env) if env else PROJECT_ROOT


# ─── Per-file rename planner ────────────────────────────────────────────────

def plan_extraction_renames(folder: Path):
    """Yield (old_path, new_name, reason) for every extraction file in folder."""
    for f in sorted(folder.glob("*.md")):
        # Skip files already in new format: P001_Foshay_2015.md
        if "_" in f.stem and fu._LEGACY_P_EXTRACTION.match(f.name):
            # Could be ambiguous (e.g. "P001_Smith_2024.md" vs "P001 - Smith_2024.md");
            # only consider the dash form legacy.
            pass
        # Already in new format?
        # Pattern: "P###_Author_Year[_note].md"
        if f.stem.startswith("P") and "_" in f.stem[1:]:
            parts = f.stem.split("_", 2)
            if len(parts) >= 3 and parts[0][1:].isdigit() and parts[1]:
                # Looks like new format already
                yield (f, None, "already in new format")
                continue

        # Legacy "P### - Something.md" form
        if fu.is_legacy_p_extraction(f.name):
            # Read APA from the first ~30 lines
            try:
                head = "\n".join(f.read_text(encoding="utf-8", errors="ignore").splitlines()[:30])
            except Exception:
                head = ""
            author, year = fu.parse_apa_reference(head)
            if not author or not year:
                # Try a wider scan (sometimes the APA is further down)
                try:
                    body = f.read_text(encoding="utf-8", errors="ignore")
                except Exception:
                    body = ""
                author, year = fu.parse_apa_reference(body[:2000])
            if not author or not year:
                yield (f, None, f"could not extract author/year (skipped): {f.name}")
                continue
            # Find the P-code
            import re
            mt = re.match(r"P(\d+)", f.stem)
            code = f"P{int(mt.group(1)):03d}" if mt else "P000"
            new_name = fu.build_extraction_filename(code, author, year)
            yield (f, new_name, "P### - ... -> P###_Author_Year.md")
            continue

        # Other .md files in extractions (e.g. hand-written notes) — skip
        yield (f, None, f"not an extraction file (skipped): {f.name}")


def plan_library_renames(folder: Path):
    """Yield (old_path, new_name, reason) for every PDF in a library folder."""
    for f in sorted(folder.glob("*.pdf")):
        # Skip if already in new format (heuristic: contains a 4-digit year
        # after an underscore)
        import re
        if re.search(r"_\d{4}(?:_|\.)", f.stem):
            yield (f, None, f"already looks canonical (skipped): {f.name}")
            continue
        # Prefer the existing filename (e.g. "Alyami et al. - 2023.pdf") — it's
        # been hand-curated by the user and is far more reliable than scanning
        # arbitrary PDF text. Only fall through to PDF text mining if the
        # filename has no usable year.
        author, year = fu.parse_legacy_author_year(f.name)
        if not author or not year:
            try:
                text = extract_first_n_chars(f, 3000)
            except Exception:
                text = ""
            a2, y2 = fu.parse_pdf_text_for_metadata(text)
            author = author or a2
            year = year or y2
        if not author:
            author = fu._sanitize_token(f.stem.split(" ")[0].split("_")[0])
        if not year:
            year = str(datetime.now().year)
        new_name = fu.build_paper_filename(author, year, ext=".pdf")
        yield (f, new_name, "library PDF -> Author_Year.pdf")


def plan_incoming_renames(folder: Path):
    """Yield rename plans for files in INCOMING/ and INCOMING/UNREAD-WEB/."""
    if not folder.exists():
        return
    for f in sorted(folder.iterdir()):
        if not f.is_file() or f.name.startswith("."):
            continue
        if f.name == ".gitkeep":
            yield (f, None, "gitkeep (skipped)")
            continue
        if f.suffix.lower() not in (".pdf", ".md"):
            yield (f, None, f"unsupported extension (skipped): {f.name}")
            continue
        # Already in new format?
        import re
        if re.search(r"_\d{4}(?:_|\.)", f.stem):
            yield (f, None, f"already looks canonical (skipped): {f.name}")
            continue
        # Prefer legacy filename parsing — the user typed "Kizilcec 2024.md" or
        # "GEORGIOS 2025.md" by hand, and that signal is more reliable than
        # mining arbitrary text. Only fall through to file-content scanning
        # if the filename has no usable year.
        author, year = fu.parse_legacy_author_year(f.name)
        if not author:
            # Try to extract first word of stem as a surname
            first_word = f.stem.split(" ")[0].split("_")[0]
            author = fu._sanitize_token(first_word) if first_word else None
        if not year:
            text = ""
            if f.suffix.lower() == ".md":
                try:
                    text = f.read_text(encoding="utf-8", errors="ignore")[:2000]
                except Exception:
                    text = ""
            elif f.suffix.lower() == ".pdf":
                try:
                    text = extract_first_n_chars(f, 3000)
                except Exception:
                    text = ""
            m = re.search(r"\b(19[89]\d|20[0-3]\d)\b", text[:500])
            if m:
                year = m.group(1)
        if not year:
            year = str(datetime.now().year)
        ext = f.suffix
        new_name = fu.build_paper_filename(author, year, ext=ext)
        yield (f, new_name, f"incoming file -> Author_Year{ext}")


# ─── Helpers ────────────────────────────────────────────────────────────────

def extract_first_n_chars(pdf_path: Path, n: int) -> str:
    """Read the first ``n`` characters of text from a PDF. Pure-Python, no
    docling dependency, used by the migration script to keep startup fast."""
    try:
        import fitz
        doc = fitz.open(str(pdf_path))
        buf = []
        total = 0
        for page in doc:
            buf.append(page.get_text())
            total += len(buf[-1])
            if total >= n:
                break
        doc.close()
        return "".join(buf)[:n]
    except Exception:
        return ""


# ─── Dry-run / apply engine ──────────────────────────────────────────────────

def run(dry_run: bool, backup: bool, base: Path):
    """Walk every project library + INCOMING and emit a rename plan."""
    audit_log = base / "99-SYSTEM-BACKEND" / "audit.log"
    plan_log = []

    def emit(action, **details):
        line = f"{action} | " + " | ".join(f"{k}={v}" for k, v in details.items())
        plan_log.append(line)
        print(line)

    if backup and not dry_run:
        backup_root = base / "99-SYSTEM-BACKEND" / "filename_migration_backup"
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = backup_root / ts
        backup_dir.mkdir(parents=True, exist_ok=True)
        emit("migration.backup.start", dest=str(backup_dir))
    else:
        backup_dir = None

    # 1. Extractions in every project
    projects_dir = base / "01-PROJECTS"
    backup_dir = base / "99-SYSTEM-BACKEND" / "filename_migration_backup" if backup else None
    if projects_dir.exists():
        for project in sorted(projects_dir.iterdir()):
            if not project.is_dir() or project.name.startswith("00-"):
                continue
            ext_dir = project / "02-EXTRACTIONS"
            if not ext_dir.exists():
                continue
            emit("scan.folder", kind="extractions", path=str(ext_dir))
            for old, new, reason in plan_extraction_renames(ext_dir):
                if new is None:
                    emit("skip", file=old.name, reason=reason)
                    continue
                target = ext_dir / new
                target = disambiguate_within(ext_dir, target)
                do_rename(old, target, dry_run, backup_dir, emit)

    # 2. Library PDFs in every project
    if projects_dir.exists():
        for project in sorted(projects_dir.iterdir()):
            if not project.is_dir() or project.name.startswith("00-"):
                continue
            lib_dir = project / "01-LIBRARY"
            if not lib_dir.exists():
                continue
            emit("scan.folder", kind="library", path=str(lib_dir))
            for old, new, reason in plan_library_renames(lib_dir):
                if new is None:
                    emit("skip", file=old.name, reason=reason)
                    continue
                target = lib_dir / new
                target = disambiguate_within(lib_dir, target)
                do_rename(old, target, dry_run, backup_dir, emit)

    # 3. INCOMING + UNREAD-WEB
    for incoming_dir in [base / "INCOMING", base / "INCOMING" / "UNREAD-WEB"]:
        if not incoming_dir.exists():
            continue
        emit("scan.folder", kind="incoming", path=str(incoming_dir))
        for old, new, reason in plan_incoming_renames(incoming_dir):
            if new is None:
                emit("skip", file=old.name, reason=reason)
                continue
            target = incoming_dir / new
            target = disambiguate_within(incoming_dir, target)
            do_rename(old, target, dry_run, backup_dir, emit)

    if dry_run:
        print("\n*** DRY-RUN — no files were renamed. Re-run with --apply to commit. ***")
    else:
        print("\n*** Migration complete. ***")

    # Persist a JSON plan for the user's records
    plan_file = base / "99-SYSTEM-BACKEND" / f"migration_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    plan_file.write_text("\n".join(plan_log), encoding="utf-8")
    print(f"\nFull plan written to: {plan_file}")


def disambiguate_within(folder: Path, target: Path) -> Path:
    """If the target name is already taken (or is the source itself), bump
    a ``_2`` / ``_3`` suffix."""
    name = target.name
    stem, dot, ext = name.rpartition(".")
    if not dot:
        stem, ext = name, ""
    n = 2
    candidate = target
    while candidate.exists() and candidate != target:
        suffix = f".{ext}" if ext else ""
        candidate = folder / f"{stem}_{n}{suffix}"
        n += 1
        if n > 9999:
            break
    return candidate


def do_rename(old: Path, new: Path, dry_run: bool, backup_root, emit):
    if old == new:
        emit("skip", file=old.name, reason="source == target")
        return
    if dry_run:
        emit("would_rename", src=str(old), dst=str(new))
    else:
        if backup_root:
            try:
                rel = old.relative_to(PROJECT_ROOT)
            except ValueError:
                rel = Path(old.name)
            backup_path = backup_root / rel
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(old, backup_path)
        old.rename(new)
        emit("renamed", src=str(old), dst=str(new))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true",
                    help="Actually rename files (default is dry-run)")
    ap.add_argument("--backup", action="store_true",
                    help="Copy old files to 99-SYSTEM-BACKEND/filename_migration_backup/ before renaming")
    args = ap.parse_args()

    base = project_path()
    print(f"Project root: {base}")
    print(f"Mode: {'APPLY' if args.apply else 'DRY-RUN'}{' + BACKUP' if args.backup else ''}\n")
    run(dry_run=not args.apply, backup=args.backup, base=base)


if __name__ == "__main__":
    main()
