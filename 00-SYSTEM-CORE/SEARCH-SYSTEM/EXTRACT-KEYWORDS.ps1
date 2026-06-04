# EXTRACT-KEYWORDS.ps1
# ResearchPilot Input-Driven Keyword Extractor (v2 - strict 8-step pipeline)
#
# This script implements the EXACT pipeline specified by the user:
#   STEP 1 - Extract year (1900-2099) first
#   STEP 2 - Remove stopwords (from the user-specified list)
#   STEP 3 - Remove punctuation (keep hyphens inside compound tokens)
#   STEP 4 - Remove loose numbers (not years)
#   STEP 5 - Classify tokens: Tier A (always keep), Tier B (paired only), Tier C (discard)
#   STEP 6 - Build phrases (max 5, min 2, longest first)
#   STEP 7 - Score phrases and tokens (with frequency bonus)
#   STEP 8 - Build final query: PRIMARY (top 4 AND), FALLBACK (next 3 OR), DATE, DROPPED
#
# The output is a structured object with PRIMARY, FALLBACK, DATE, DROPPED fields
# ready to be pasted into Scopus/WoS/Google Scholar.
#
# ============================================================================
# ARCHITECTURAL RULE (CRITICAL - DO NOT VIOLATE):
# ============================================================================
# This script is PURELY USER-INPUT-DRIVEN.
# The project config is NOT consulted for tier lists, stopwords, or
# lemmatization. Those enrichments would bias the extraction toward the
# project's pre-known keywords instead of what the user actually typed.
#
# The -Project parameter is accepted only for script-signature consistency
# (so callers can pass it without breaking) but it is INTENTIONALLY IGNORED
# for the extraction logic.
#
# The project config IS consulted by:
#   - KEYWORD-FILTER.ps1  (for SCORING search results)
#   - PRE-FILTER.ps1      (for ACCEPT/REJECT decisions)
#   - SEARCH.ps1          (for the must_not_have EXCLUSION block only)
# ============================================================================

param(
    [Parameter(Mandatory=$true)]
    [string]$InputText,

    [Parameter(Mandatory=$false)]
    [string]$Mode = "query",   # query | analyze | keywords | json | scholar

    [Parameter(Mandatory=$false)]
    [string]$ConfigPath = "",

    [Parameter(Mandatory=$false)]
    [string]$Project = "DEFAULT"
)

$EngineRoot = $PSScriptRoot
if (-not $ConfigPath) {
    $ConfigPath = Join-Path $EngineRoot "projects\$Project.json"
}
$Config = $null
if (Test-Path -LiteralPath $ConfigPath) {
    $Config = Get-Content -LiteralPath $ConfigPath -Raw -Encoding UTF8 | ConvertFrom-Json
}

# =========================================================================
# WORD LISTS
# =========================================================================

# User-specified stopword list (STEP 2)
$Stopwords = @(
    # Aux verbs / modals
    "a","an","the","is","are","was","were","be","been","being",
    "do","does","did","have","has","had",
    "can","could","may","might","must","should","would","will","shall",
    # Prepositions
    "of","to","from","in","on","at","by","for","with","through","between","among","during","after",
    "before","about","within","without",
    # Conjunctions
    "and","or","but","if","because","although","however","therefore","thus","hence","so","yet",
    # Pronouns / demonstratives
    "this","that","these","those","it","its","they","them","their","he","she","his","her",
    "we","us","our","you","your","who","which","what",
    # Quantifiers
    "any","some","many","much","few","several","each","every","all","both","most","more","less",
    # Adverbs
    "also","just","only","very","quite","rather","often","always","never","sometimes",
    "usually","generally","largely","mainly","mostly",
    # Generic academic filler verbs (low information value, NOT domain-specific)
    "examine","explore","investigate","discuss","consider","present","provide","describe",
    "show","suggest","indicate","find","focus","address","analyse","analyze","look","review","study",
    "emerge","appear","arise","imply","reveal","highlight","emphasize","emphasise","note",
    "argue","claim","state","demonstrate","demonstrate","propose","illustrate","observe",
    "outline","report","mention","refer","cite","acknowledge","conclude","summarize","summarise",
    "assess","evaluate","interpret","identify","examine","identify","establish","determine",
    "contribute","contribute","add","adds","offer","offers","highlighted","emphasised","emphasized",
    "noted","argued","claimed","stated","demonstrated","proposed","illustrated","observed",
    "outlined","reported","mentioned","referred","cited","acknowledged","concluded","summarized",
    "assessed","evaluated","interpreted","identified","established","determined","contributed",
    # Generic academic past participles (same fillers, but past forms)
    "examined","explored","investigated","discussed","considered","presented","provided","described",
    "shown","suggested","indicated","found","focused","addressed","analysed","analyzed",
    # Academic intro / closing phrases
    "however","moreover","furthermore","nevertheless","nonetheless","therefore","thus","hence",
    # Search-pleading / meta-words (user input wrappers, not topics)
    "papers","paper","articles","article","research","work","works","title","titles"
)

# Tier A - always keep (domain nouns, proper nouns, named theories/models/acronyms, technical adjectives)
# Default Tier A words. Project config may extend this list.
$DefaultTierA = @(
    # Security / privacy
    "cybersecurity","security","privacy","encryption","phishing","malware","threat","vulnerability",
    "breach","attack","hacking","password","authentication","authorization","firewall","network",
    "ransomware","social-engineering","biometric","cryptography","forensics","steganography",
    # People / roles / institutions
    "user","users","staff","faculty","student","students","leader","leaders","employee","employees",
    "workforce","management","team","department","organisation","organizations","institution","institutions",
    "government","industry","sector","enterprise","university","universities","school","schools",
    "student","learner","teacher","faculty",
    # Education / training
    "education","educational","training","learning","teaching","curriculum","pedagogy","academic",
    "literacy","awareness","knowledge","skill","skills","competence","competency",
    # Theory / model / method
    "theory","model","framework","method","methodology","approach","design","science","paradigm",
    "analysis","study","review","literature","survey","case","experiment","trial","pilot",
    "qualitative","quantitative","mixed-methods","longitudinal","cross-sectional",
    # Behavioural / cognitive
    "behaviour","behavior","behavioural","behavioral","cognitive","psychological","attitude",
    "intention","perception","belief","motivation","motivation","compliance","engagement","trust",
    "fatigue","stress","workload","workarounds","habit","intention",
    # Culture / organisation
    "culture","cultural","clan","adhocracy","hierarchy","market","leadership","governance",
    "policy","policies","procedure","procedure","rule","regulation","compliance","accountability",
    "transparency","ethics","ethical","value","values","norm","norms","artefact","artifact","assumption","assumptions",
    # Mental model
    "mental","model","schema","mindset","heuristic","bias","interpretation","perception",
    # HEI specific
    "hei","heis","higher-education","college","campus","decentralised","decentralized",
    # Technical adjectives
    "organisational","organizational","institutional","adversarial","sociotechnical","socio-technical",
    "interdisciplinary","multidisciplinary","cross-disciplinary","user-centric","human-centric",
    # Acronyms
    "pmt","tpb","tam","sct","gdpr","hipaa","nist","iso","owasp","seta","mfa","soc","siem","ids","ips",
    "vpn","api","lms","cio","ciso","ioc","ttp","ttp","ttp",
    # Risk / outcome
    "risk","impact","outcome","incident","resilience","readiness","posture","maturity","preparedness",
    "effectiveness","efficiency","performance","quality","adoption","acceptance","adherence","violation",
    # Assessment / evaluation
    "assessment","evaluation","diagnostic","measurement","metric","indicator","framework",
    "checklist","index","score","rating","benchmark","criterion","criteria",
    # Misc domain
    "information","technology","system","systems","data","process","control","controls",
    "tool","tools","application","applications","platform","service","services",
    "communication","interaction","feedback","support","resource","resources"
)

# Tier B - keep only if paired with a Tier A token
# Domain-specific verbs and evaluative adjectives
$DefaultTierB = @(
    "authenticate","authorize","encrypt","decrypt","mitigate","predict","classify","optimise","optimize",
    "detect","prevent","protect","defend","respond","recover","restore","audit","monitor","scan",
    "adopt","adopt","influence","motivate","persuade","reinforce","shape","mediate","interpret","enact",
    "structure","organise","organize","facilitate","hinder","enable","constrain",
    "leak","expose","breach","compromise","exfiltrate",
    "critical","significant","robust","effective","ineffective","sustainable","scalable",
    "sufficient","insufficient","adequate","inadequate","measurable","observable","detectable",
    "vulnerable","secure","insecure","malicious","benign","suspicious","trustworthy","distrusted",
    "common","typical","atypical","novel","unique","specific","general","broad","narrow",
    "frequent","infrequent","recurrent","persistent","transient","temporary","permanent"
)

# Tier C - always discard (generic nouns and weak adjectives)
$DefaultTierC = @(
    # Generic nouns
    "way","thing","aspect","issue","factor","area","type","form","kind","sort","set","group","class",
    "case","example","instance","part","element","component","feature","characteristic","property",
    "level","degree","extent","amount","number","amount","quantity","size","scope","range",
    "case","context","background","setting","environment","situation","condition","state",
    # Weak adjectives
    "good","bad","new","old","large","small","different","various","important","relevant","interesting",
    "useful","helpful","certain","particular","specific","general","basic","simple","complex",
    "similar","same","other","another","own","main","major","minor","key","primary","secondary",
    "overall","total","full","empty","open","closed","complete","partial","whole",
    # Generic verbs not already in stopwords
    "make","do","take","give","get","go","come","see","know","say","tell","put","set","use","work",
    "try","ask","seem","feel","want","need","help","let","keep","hold","bring","begin","start",
    "become","remain","stay","leave","reach","turn","move","play","run","live","believe","include",
    "continue","change","follow","stop","create","open","close","send","receive","increase","decrease",
    "appear","develop","grow","produce","provide","involve","build","apply","form","contain","include",
    "require","suggest","raise","pass","offer","decide","pull","draw","write","stand","lose","pay",
    "meet","include","continue","set","learn","change","lead","understand","watch","follow","stop",
    "create","speak","read","allow","add","grow","open","walk","win","offer","remember","consider",
    "appear","buy","wait","serve","die","send","expect","build","stay","fall","cut","reach","kill",
    # Domain-overused
    "system"   # unless paired with strong Tier A
)

# Lemmatization map (collapse word forms to base form)
$Lemmatize = @{
    "developed"="develop";"developing"="develop";"develops"="develop"
    "structured"="structure";"structuring"="structure";"structures"="structure"
    "behaviors"="behaviour";"behavioural"="behaviour";"behavioral"="behaviour";"behavior"="behaviour";"behaviours"="behaviour"
    "organizational"="organisational";"organizations"="organisation";"organization"="organisation";"organisations"="organisation"
    "policies"="policy";"universities"="university";"colleges"="college";"schools"="school"
    "analyzing"="analyse";"analyzed"="analyse";"analyses"="analyse";"analyzes"="analyse"
    "compliance"="comply";"complied"="comply";"complies"="comply";"complying"="comply"
    "readinesses"="readiness";"readiness's"="readiness"
    "cybersecurity's"="cybersecurity";"cyber-security"="cybersecurity";"cyber security"="cybersecurity"
    "models"="model";"model's"="model";"assessments"="assessment";"assessment's"="assessment"
    "leaders"="leader";"institutions"="institution";"institutional"="institution"
    "staffs"="staff";"students"="student";"faculties"="faculty";"learners"="learner";"teachers"="teacher"
    "technologies"="technology";"technological"="technology"
    "cultures"="culture";"cultural"="culture"
    "educations"="education";"educational"="education"
    "considering"="consider";"considered"="consider";"considers"="consider"
    "explored"="explore";"exploring"="explore";"explores"="explore"
    "examined"="examine";"examining"="examine";"examines"="examine"
    "investigated"="investigate";"investigating"="investigate"
    "related"="relate";"relating"="relate";"relates"="relate"
    "focused"="focus";"focusing"="focus";"focuses"="focus"
    "emerging"="emerge";"emerges"="emerge";"emerged"="emerge"
    "based"="base";"basing"="base";"bases"="base"
    "towards"="toward"
    "given"="give";"giving"="give";"gives"="give"
    "shown"="show";"showing"="show";"shows"="show"
    "found"="find";"finding"="find";"finds"="find"
    "provided"="provide";"providing"="provide";"provides"="provide"
    "described"="describe";"describing"="describe";"describes"="describe"
    "regarding"="regard";"regards"="regard";"regarded"="regard"
    "using"="use";"used"="use";"uses"="use"
    "enforced"="enforce";"enforcement"="enforce"
    "mediated"="mediate";"mediation"="mediate"
    "interpreted"="interpret";"interpretation"="interpret"
    "enacted"="enact";"enactment"="enact"
    "predicted"="predict";"predicting"="predict";"predicts"="predict"
    "detected"="detect";"detecting"="detect";"detects"="detect"
    "adopted"="adopt";"adopting"="adopt";"adopts"="adopt"
    "influenced"="influence";"influencing"="influence";"influences"="influence"
    "motivated"="motivate";"motivating"="motivate";"motivates"="motivate"
    "mitigated"="mitigate";"mitigating"="mitigate";"mitigates"="mitigate"
    "encrypted"="encrypt";"encrypting"="encrypt";"encrypts"="encrypt"
    "classified"="classify";"classifying"="classify";"classifies"="classify"
    "optimised"="optimise";"optimising"="optimise";"optimises"="optimise"
    "optimized"="optimize";"optimizing"="optimize";"optimizes"="optimize"
    "authenticated"="authenticate";"authenticating"="authenticate";"authenticates"="authenticate"
    "authorized"="authorize";"authorizing"="authorize";"authorizes"="authorize"
    "organised"="organise";"organising"="organise";"organises"="organise"
    "organized"="organize";"organizing"="organize";"organizes"="organize"
    "facilitated"="facilitate";"facilitating"="facilitate";"facilitates"="facilitate"
    "hindered"="hinder";"hindering"="hinder";"hinders"="hinder"
    "enabled"="enable";"enabling"="enable";"enables"="enable"
    "constrained"="constrain";"constraining"="constrain";"constrains"="constrain"
    "reinforced"="reinforce";"reinforcing"="reinforce";"reinforces"="reinforce"
    "shaped"="shape";"shaping"="shape";"shapes"="shape"
    "mediating"="mediate";"mediates"="mediate"
    "interpreting"="interpret";"interprets"="interpret"
    "enacting"="enact";"enacts"="enact"
}

# =========================================================================
# IMPORTANT: This script is PURELY USER-INPUT-DRIVEN.
# The project config is NOT used to enrich the tier lists, stopwords,
# or lemmatization here. Those enrichments would bias the extraction
# toward the project's pre-known keywords instead of the user's input.
#
# The project config is ONLY consulted by KEYWORD-FILTER.ps1 (for
# SCORING search results) and by PRE-FILTER.ps1 (for ACCEPT/REJECT
# decisions). EXTRACT-KEYWORDS produces the search query from the
# input alone.
# =========================================================================
# Project config is loaded but not used for tier enrichment:
# (kept as a placeholder so the calling scripts can pass -Project
#  without breaking; the value is intentionally ignored here.)
if ($Config) {
    # No-op: project config is intentionally NOT applied to tier
    # lists, stopwords, or lemmatization in this extractor.
}

# Build sets for O(1) lookup
$StopSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$Stopwords, [System.StringComparer]::OrdinalIgnoreCase)
$TierASet = [System.Collections.Generic.HashSet[string]]::new([string[]]$DefaultTierA, [System.StringComparer]::OrdinalIgnoreCase)
$TierBSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$DefaultTierB, [System.StringComparer]::OrdinalIgnoreCase)
$TierCSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$DefaultTierC, [System.StringComparer]::OrdinalIgnoreCase)

# =========================================================================
# STEP 1 - EXTRACT YEAR (1900-2099)
# =========================================================================
$DATE_FILTER = $null
$yearPattern = '\b(19[0-9]{2}|20[0-9]{2})\b'
$years = [regex]::Matches($InputText, $yearPattern)
if ($years.Count -gt 0) {
    $yearList = @()
    foreach ($m in $years) { $yearList += [int]$m.Value }
    $yearList = $yearList | Sort-Object -Unique
    if ($yearList.Count -eq 1) {
        $DATE_FILTER = $yearList[0]
    } else {
        $DATE_FILTER = "$($yearList[0])..$($yearList[-1])"
    }
}

# Also detect year ranges like "2020-2024" or "2020 to 2024"
$rangePattern = '\b(19[0-9]{2}|20[0-9]{2})\s*(?:-|to|–|—)\s*(19[0-9]{2}|20[0-9]{2})\b'
$rangeMatch = [regex]::Match($InputText, $rangePattern)
if ($rangeMatch.Success) {
    $startYear = [int]$rangeMatch.Groups[1].Value
    $endYear = [int]$rangeMatch.Groups[2].Value
    if ($endYear -ge $startYear) {
        $DATE_FILTER = "$startYear..$endYear"
    }
}

# Remove year matches from text before further processing
$textNoYear = $InputText -replace $yearPattern, ' '

# =========================================================================
# STEP 2 - REMOVE STOPWORDS
# =========================================================================
# Tokenize first (so we can do exact-word matching)
$rawTokens = $textNoYear -split '\s+' | Where-Object { $_ -ne '' }

# Step 2a: exact-match stopword removal
$afterStop = @()
$droppedStop = @()
foreach ($t in $rawTokens) {
    if ($StopSet.Contains($t.ToLower())) {
        $droppedStop += $t
    } else {
        $afterStop += $t
    }
}

# =========================================================================
# STEP 3 - REMOVE PUNCTUATION
# =========================================================================
# Keep hyphens inside compound tokens (e.g., cyber-security, e-learning)
$cleaned = @()
$droppedPunct = @()
foreach ($t in $afterStop) {
    if ([string]::IsNullOrWhiteSpace($t)) { continue }
    $tk = $t
    # Strip punctuation except internal hyphens
    # Pattern: a hyphen between two letters = keep; hyphen at start/end = strip
    if ($tk -match '^[a-zA-Z]+(-[a-zA-Z]+)+$') {
        # Pure compound with internal hyphens: keep as-is
        $cleaned += $tk
    } else {
        # Remove all punctuation including standalone hyphens
        $orig = $tk
        $tk = $tk -replace '[^\w\s-]', ''
        $tk = $tk -replace '^-|-$', ''   # remove leading/trailing hyphens
        if ($tk -ne $orig -and $tk -eq '') { $droppedPunct += $orig; continue }
        if ($tk -ne '' -and $tk -ne $orig) { $droppedPunct += $orig }
        if ($tk -ne '') { $cleaned += $tk }
    }
}

# =========================================================================
# STEP 4 - REMOVE LOOSE NUMBERS
# =========================================================================
$afterNoNum = @()
$droppedNum = @()
foreach ($t in $cleaned) {
    if ($t -match '^\d+$') {
        $droppedNum += $t
    } else {
        $afterNoNum += $t
    }
}

# =========================================================================
# STEP 5 - CLASSIFY TOKENS
# =========================================================================
# Lemmatize first
$lemmatized = @()
foreach ($t in $afterNoNum) {
    $key = $t.ToLower()
    if ($Lemmatize.ContainsKey($key)) { $lemmatized += $Lemmatize[$key] }
    else { $lemmatized += $t.ToLower() }
}

# Classify each token
$classified = @()
$droppedTierC = @()
foreach ($w in $lemmatized) {
    if ($StopSet.Contains($w)) {
        # Already removed, but defensive
        continue
    }
    if ($TierCSet.Contains($w)) {
        $droppedTierC += $w
        continue
    }
    if ($TierASet.Contains($w)) {
        $classified += @{ Word = $w; Tier = "A" }
    }
    elseif ($TierBSet.Contains($w)) {
        $classified += @{ Word = $w; Tier = "B" }
    }
    else {
        # Unknown - treat as Tier B (might be domain term from input)
        # But length filter: too short = drop
        if ($w.Length -ge 4) {
            $classified += @{ Word = $w; Tier = "B" }
        }
        # else dropped silently
    }
}

# =========================================================================
# STEP 6 - BUILD PHRASES (max 5, min 2, longest first)
# =========================================================================
# Strategy: greedy longest-phrase extraction
# - Try to merge 5 consecutive Tier A/B tokens
# - Then 4, then 3, then 2
# - A phrase must contain at least one Tier A token
# - Never combine two Tier B tokens without a Tier A anchor

# Build token indices for the original classified list
$tokens = @($classified | ForEach-Object { $_.Word })
$tiers = @($classified | ForEach-Object { $_.Tier })

# Mark used tokens to prevent overlap
$used = @(0) * $tokens.Count

# Extract phrases greedily, longest first
$phrases = New-Object System.Collections.ArrayList

# Helper: check if any token in the range is Tier A
function Test-HasTierA {
    param([int]$Start, [int]$End, [array]$Tiers)
    for ($i = $Start; $i -le $End; $i++) {
        if ($Tiers[$i] -eq "A") { return $true }
    }
    return $false
}

# Helper: try to extract a phrase of length N starting at position i
function Try-ExtractPhrase {
    param([int]$Start, [int]$Length, [array]$Tokens, [array]$Tiers, [array]$Used, [System.Collections.ArrayList]$Phrases)
    $end = $Start + $Length - 1
    if ($end -ge $Tokens.Count) { return $false }
    # Check no token in range is used
    for ($i = $Start; $i -le $end; $i++) {
        if ($Used[$i]) { return $false }
    }
    # Must contain at least one Tier A
    if (-not (Test-HasTierA -Start $Start -End $end -Tiers $Tiers)) { return $false }
    # Mark used and add phrase
    for ($i = $Start; $i -le $end; $i++) { $Used[$i] = $true }
    $phrase = ($Tokens[$Start..$end] -join " ")
    # Count Tier A tokens in this range
    $tierACount = 0
    for ($i = $Start; $i -le $end; $i++) {
        if ($Tiers[$i] -eq "A") { $tierACount++ }
    }
    $Phrases.Add(@{ Phrase = $phrase; Length = $Length; TierA_Count = $tierACount }) | Out-Null
    return $true
}

# Try 5-word phrases first
for ($i = 0; $i -lt $tokens.Count; $i++) {
    [void](Try-ExtractPhrase -Start $i -Length 5 -Tokens $tokens -Tiers $tiers -Used $used -Phrases $phrases)
}
# Try 4-word phrases (where 5 didn't fit)
for ($i = 0; $i -lt $tokens.Count; $i++) {
    [void](Try-ExtractPhrase -Start $i -Length 4 -Tokens $tokens -Tiers $tiers -Used $used -Phrases $phrases)
}
# Try 3-word phrases
for ($i = 0; $i -lt $tokens.Count; $i++) {
    [void](Try-ExtractPhrase -Start $i -Length 3 -Tokens $tokens -Tiers $tiers -Used $used -Phrases $phrases)
}
# Try 2-word phrases
for ($i = 0; $i -lt $tokens.Count; $i++) {
    [void](Try-ExtractPhrase -Start $i -Length 2 -Tokens $tokens -Tiers $tiers -Used $used -Phrases $phrases)
}

# Standalone Tier A tokens
$standaloneTierA = @()
for ($i = 0; $i -lt $tokens.Count; $i++) {
    if (-not $used[$i] -and $tiers[$i] -eq "A") {
        $standaloneTierA += $tokens[$i]
        $used[$i] = $true
    }
}

# Tier B tokens used alone (for penalty later)
$standaloneTierB = @()
for ($i = 0; $i -lt $tokens.Count; $i++) {
    if (-not $used[$i] -and $tiers[$i] -eq "B") {
        $standaloneTierB += $tokens[$i]
    }
}

# =========================================================================
# STEP 7 - SCORE EVERY PHRASE AND TOKEN
# =========================================================================
# Base score by length and tier
function Get-TokenBaseScore {
    param([string]$Tier, [int]$Length)
    if ($Length -eq 1) {
        if ($Tier -eq "A") { return 1 }
        else { return 0.5 }
    }
    switch ($Length) {
        2 { return 3 }
        3 { return 5 }
        4 { return 7 }
        5 { return 9 }
        default { return 0 }
    }
}

# Count frequency in ORIGINAL input (case-insensitive)
$originalLower = $InputText.ToLower()

$scored = @()

# Score phrases
foreach ($p in $phrases) {
    $phrase = $p.Phrase
    $base = Get-TokenBaseScore -Tier "A" -Length $p.Length
    # Frequency bonus
    $count = ([regex]::Matches($originalLower, [regex]::Escape($phrase))).Count
    $bonus = 0
    if ($count -ge 11) { $bonus = 4 }
    elseif ($count -ge 6) { $bonus = 3 }
    elseif ($count -ge 3) { $bonus = 2 }
    elseif ($count -ge 2) { $bonus = 1 }
    $scored += [PSCustomObject]@{
        Term  = $phrase
        Type  = "phrase-$($p.Length)"
        Base  = $base
        Bonus = $bonus
        Count = $count
        Score = $base + $bonus
    }
}

# Score standalone Tier A tokens
foreach ($w in $standaloneTierA) {
    $base = 1
    $count = ([regex]::Matches($originalLower, [regex]::Escape($w))).Count
    $bonus = 0
    if ($count -ge 11) { $bonus = 4 }
    elseif ($count -ge 6) { $bonus = 3 }
    elseif ($count -ge 3) { $bonus = 2 }
    elseif ($count -ge 2) { $bonus = 1 }
    $scored += [PSCustomObject]@{
        Term  = $w
        Type  = "1word-A"
        Base  = $base
        Bonus = $bonus
        Count = $count
        Score = $base + $bonus
    }
}

# Score standalone Tier B tokens (with PENALTY)
foreach ($w in $standaloneTierB) {
    $count = ([regex]::Matches($originalLower, [regex]::Escape($w))).Count
    $bonus = 0
    if ($count -ge 11) { $bonus = 4 }
    elseif ($count -ge 6) { $bonus = 3 }
    elseif ($count -ge 3) { $bonus = 2 }
    elseif ($count -ge 2) { $bonus = 1 }
    $scored += [PSCustomObject]@{
        Term  = $w
        Type  = "1word-B"
        Base  = 0.5
        Bonus = $bonus
        Count = $count
        Score = 0.5 + $bonus - 0.5   # Tier B standalone penalty
    }
}

# Sort by total score descending
$scored = $scored | Sort-Object -Property Score -Descending

# Deduplicate (keep highest-scoring instance)
$seen = @{}
$finalTerms = @()
foreach ($s in $scored) {
    if (-not $seen.ContainsKey($s.Term)) {
        $seen[$s.Term] = $true
        $finalTerms += $s
    }
}

# =========================================================================
# STEP 8 - BUILD FINAL QUERY
# =========================================================================
# PRIMARY: top 4 highest-scored PHRASES (not 1-word) joined with AND
$primaryCandidates = @($finalTerms | Where-Object { $_.Type -like "phrase-*" })
$primary = @($primaryCandidates | Select-Object -First 4)

# FALLBACK: next 3 terms (any type) joined with OR
$fallback = @($finalTerms | Select-Object -Skip ($primary.Count) -First 3)

# Build query strings
$primaryQuery = ($primary | ForEach-Object { '"' + $_.Term + '"' }) -join ' AND '
$fallbackQuery = ($fallback | ForEach-Object { '"' + $_.Term + '"' }) -join ' OR '

# Build DROPPED list
$dropped = @()
foreach ($w in $droppedStop)   { $dropped += [PSCustomObject]@{ Term = $w; Reason = "stopword" } }
foreach ($w in $droppedPunct)  { $dropped += [PSCustomObject]@{ Term = $w; Reason = "punctuation" } }
foreach ($w in $droppedNum)    { $dropped += [PSCustomObject]@{ Term = $w; Reason = "loose number" } }
foreach ($w in $droppedTierC)  { $dropped += [PSCustomObject]@{ Term = $w; Reason = "Tier C (generic)" } }
foreach ($w in $standaloneTierB) { $dropped += [PSCustomObject]@{ Term = $w; Reason = "Tier B unpaired (penalty)" } }

# =========================================================================
# EXPOSE ALL BIGRAMS AND TRIGRAMS for downstream scoring
# These are computed from the final cleaned token list, regardless of
# whether they survived phrase extraction. Downstream scorers can use
# these for robust partial-phrase matching.
# =========================================================================
$bigrams = @()
$trigrams = @()
if ($tokens.Count -ge 2) {
    for ($i = 0; $i -lt $tokens.Count - 1; $i++) {
        $bigrams += "$($tokens[$i]) $($tokens[$i + 1])"
    }
}
if ($tokens.Count -ge 3) {
    for ($i = 0; $i -lt $tokens.Count - 2; $i++) {
        $trigrams += "$($tokens[$i]) $($tokens[$i + 1]) $($tokens[$i + 2])"
    }
}

# =========================================================================
# OUTPUT
# =========================================================================

$result = [PSCustomObject]@{
    Primary      = $primary
    Fallback     = $fallback
    Date         = $DATE_FILTER
    Dropped      = $dropped
    AllScored    = $finalTerms
    Tokens       = $tokens
    Tiers        = $tiers
    RawBigrams   = $bigrams
    RawTrigrams  = $trigrams
}

switch ($Mode) {
    "query" {
        Write-Host "==========================================" -ForegroundColor Cyan
        Write-Host " ResearchPilot SEARCH (v2 - strict 8-step)" -ForegroundColor Cyan
        Write-Host "==========================================" -ForegroundColor Cyan
        Write-Host " Input:  $InputText"
        Write-Host ""
        Write-Host " DATE_FILTER:  $DATE_FILTER" -ForegroundColor Magenta
        Write-Host ""
        Write-Host " PRIMARY (top 4 phrases, AND-joined):" -ForegroundColor Green
        if ($primary.Count -gt 0) {
            Write-Host "   $primaryQuery" -ForegroundColor White
        } else {
            Write-Host "   (no phrases - input too short)" -ForegroundColor Red
        }
        Write-Host ""
        Write-Host " FALLBACK (next 3 terms, OR-joined):" -ForegroundColor Yellow
        if ($fallback.Count -gt 0) {
            Write-Host "   $fallbackQuery" -ForegroundColor White
        } else {
            Write-Host "   (none)" -ForegroundColor Red
        }
        Write-Host ""
        Write-Host " DROPPED ($($dropped.Count) terms):" -ForegroundColor DarkYellow
        $dropped | Group-Object Reason | ForEach-Object {
            Write-Host "   $($_.Name): $($_.Group.Term -join ', ')" -ForegroundColor DarkGray
        }
        Write-Host ""
        Write-Host " ALL SCORED TERMS (top 15):" -ForegroundColor Cyan
        $finalTerms | Select-Object -First 15 | ForEach-Object {
            $color = if ($_.Score -ge 5) {"Green"} elseif ($_.Score -ge 2) {"Yellow"} else {"DarkGray"}
            Write-Host "   $($_.Score.ToString('F1').PadLeft(4)) | $($_.Type.PadRight(10)) | $($_.Term)" -ForegroundColor $color
        }
    }
    "analyze" { return $result }
    "keywords" {
        return $finalTerms | Select-Object -First 12 | ForEach-Object { $_.Term }
    }
    "json" { return ($result | ConvertTo-Json -Depth 8) }
    "scholar" {
        $lines = @()
        $lines += "# Primary AND-query:"
        $lines += $primaryQuery
        $lines += ""
        $lines += "# Fallback OR-query:"
        $lines += $fallbackQuery
        if ($DATE_FILTER) {
            $lines += ""
            $lines += "# Date filter: $DATE_FILTER"
        }
        return ($lines -join "`n")
    }
    default {
        Write-Host "Unknown mode: $Mode" -ForegroundColor Red
    }
}
