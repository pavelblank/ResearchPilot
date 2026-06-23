# 99-META

This folder holds **project-level context** — the high-level notes that tell the AI what your project is about, so chat answers and extractions are tailored to your actual research.

## What goes here

- **Project brief** — what you're researching and why
- **Research questions** — your RQ1, RQ2, RQ3
- **Scope** — what's in, what's out
- **Methodology decisions** — qualitative? quantitative? mixed? why?
- **Timeline** — milestones, deadlines
- **Terminology** — domain-specific terms the AI should know
- **Progress notes** — weekly updates, decisions made

## Why it matters

The chat assistant and the 12-point extractor use these files as context. Without them, the AI has to guess what your project is about. With them, every answer is more relevant.

## Suggested file

Create a file called `PROJECT-CONTEXT.md` at the top of this folder with:

```markdown
# Project: P1-MY-RESEARCH

## What this project is about
[Brief description]

## Research questions
- RQ1: ...
- RQ2: ...
- RQ3: ...

## Methodology
[Approach and why]

## Key terms
- Term 1 — definition
- Term 2 — definition

## What I want from the AI
[How you want the AI to help]
```

The system will pick this up automatically when you chat.
