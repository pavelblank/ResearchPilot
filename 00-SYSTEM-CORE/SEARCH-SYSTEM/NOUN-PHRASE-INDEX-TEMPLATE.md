# Noun Phrase Index Template

> **How to use**: For your project, copy this template to `01-PROJECTS/<YourProjectCode>/99-META/queries/NOUN-PHRASE-INDEX.md` and fill in YOUR project's specific noun phrases. Do NOT modify the `KEYWORD-FILTER.ps1` engine for project-specific keywords - put them in the JSON config.

---

## How to Use This Index

1. Pick the **framework layer** (L1-L5) you want to search
2. Copy the **trigram queries** (highest precision) into your search tool
3. If too few results, fall back to **bigram queries**
4. Wrap every multi-word concept in **double quotes** (forces exact match)
5. Combine layers with `AND`, alternatives within a layer with `OR`

---

## L0 - Core Construct (must match)

### Bigrams (2-word)
```
"<your core construct 1>"
"<your core construct 2>"
```

### Trigrams (3-word) - HIGHEST PRECISION
```
"<your core construct trigram 1>"
"<your core construct trigram 2>"
```

---

## L1 - <Layer Name 1>

### Bigrams
```
"<noun phrase 1>"
"<noun phrase 2>"
```

### Trigrams
```
"<trigram 1>"
"<trigram 2>"
```

---

## L2 - <Layer Name 2>

### Bigrams
```
"<noun phrase 1>"
"<noun phrase 2>"
```

### Trigrams
```
"<trigram 1>"
"<trigram 2>"
```

---

## Context Anchor (Sector / Setting)

### Bigrams
```
"<sector term 1>"
"<sector term 2>"
```

### Trigrams
```
"<trigram sector term 1>"
```

---

## Population Anchors (Who the study is ABOUT)

```
"<population 1>"
"<population 2>"
```

**Auto-reject if the population is**: `<wrong population 1>`, `<wrong population 2>`

---

## Method Anchors (Methodology)

```
"<method 1>"
"<method 2>"
```

---

## Theory Anchors (Theoretical Frameworks)

```
"<theory 1>"
"<theory 2>"
```

---

## Journal Quality Filter (use in Scopus/WoS)

```
"<Q1/Q2 journal 1>"
"<Q2 journal 2>"
```

---

## Auto-Reject Vocabulary (signals irrelevance)

If a paper is **primarily** about these, auto-reject:

```
"<irrelevant topic 1>"
"<irrelevant topic 2>"
```

---

## Building a Search String (Worked Example)

**Goal**: Find papers about <your specific research question>.

**Step 1 - Pick the layers**:
- L1 (<layer 1>)
- L2 (<layer 2>)
- Context (<your context>)

**Step 2 - Pick one trigram per layer** (highest precision):
```
"<L1 trigram>"      (L1)
"<L2 trigram>"      (L2)
"<context trigram>" (Context)
```

**Step 3 - Build the Boolean string** (Scopus):
```
TITLE-ABS-KEY ( "<L1 trigram>" OR "<L1 trigram alt>" )
AND TITLE-ABS-KEY ( "<L2 trigram>" OR "<L2 trigram alt>" )
AND TITLE-ABS-KEY ( "<context trigram>" OR "<context bigram>" )
AND NOT TITLE-ABS-KEY ( "<reject 1>" OR "<reject 2>" )
AND PUBYEAR > 2019
```

**Step 4 - For Google Scholar** (paste one per line):
```
"<L1 bigram>" "<L2 bigram>" "<context bigram>"
"<L1 trigram>" "<context bigram>"
```

---

## Last Updated
<date> - Initial index built for <ProjectCode>
