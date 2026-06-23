# KEYWORD-FILTER.ps1
# ResearchPilot Universal Search Filter Engine
# Project-agnostic: reads keywords from a JSON config file
# Implements: tokenize -> stopword removal -> lemmatize -> noun-phrase extract -> score

param(
    [Parameter(Mandatory=$true)]
    [string]$InputText,

    [Parameter(Mandatory=$false)]
    [string]$Mode = "analyze",   # analyze | score | extract | clean

    [Parameter(Mandatory=$false)]
    [string]$ConfigPath = "",

    [Parameter(Mandatory=$false)]
    [string]$Project = "P1-HEI-CULTURE"
)

$EngineRoot = $PSScriptRoot
if (-not $ConfigPath) {
    $ConfigPath = Join-Path $EngineRoot "projects\$Project.json"
}
if (-not (Test-Path -LiteralPath $ConfigPath)) {
    Write-Host "Config not found: $ConfigPath" -ForegroundColor Red
    Write-Host "Pass -ConfigPath or place a JSON at projects\<ProjectCode>.json" -ForegroundColor Red
    exit 1
}

$Config = Get-Content -LiteralPath $ConfigPath -Raw -Encoding UTF8 | ConvertFrom-Json

# =========================================================================
# LOAD CONFIG
# =========================================================================
$CorePhrases   = @($Config.core_constructs.ngrams)
$CoreWeight    = if ($Config.core_constructs.weight) { $Config.core_constructs.weight } else { 10 }
$ContextMust   = @($Config.context_anchors.must_have_any)
$ContextWeight = if ($Config.context_anchors.weight) { $Config.context_anchors.weight } else { 3 }
$ContextReject = @($Config.context_anchors.must_not_have)
$PopReject     = @($Config.population_anchors.auto_reject_populations)
$MethodPhrases = @($Config.method_anchors.preferred)
$MethodWeight  = if ($Config.method_anchors.weight) { $Config.method_anchors.weight } else { 1 }
$TheoryPhrases = @($Config.theory_anchors.preferred)
$TheoryWeight  = if ($Config.theory_anchors.weight) { $Config.theory_anchors.weight } else { 1 }
$AcceptThresh  = if ($Config.scoring.accept_threshold) { $Config.scoring.accept_threshold } else { 20 }
$ReviewMin     = if ($Config.scoring.review_min) { $Config.scoring.review_min } else { 10 }
$RejectThresh  = if ($Config.scoring.reject_threshold) { $Config.scoring.reject_threshold } else { 5 }

# Build noun-phrase dictionary from hashtable
$NounPhrases = @{}
if ($Config.noun_phrases) {
    $Config.noun_phrases.PSObject.Properties | ForEach-Object {
        $propName = $_.Name
        # Skip metadata/comment fields
        if ($propName -like "_*") { return }
        $val = $_.Value
        if ($val -is [string]) {
            Write-Verbose "Skipping non-numeric noun phrase entry: $propName"
            return
        }
        $NounPhrases[$propName] = [int]$val
    }
}

# Add layer phrases (with their weights) to the dictionary
if ($Config.framework_layers) {
    $Config.framework_layers.PSObject.Properties | ForEach-Object {
        $layerName = $_.Name
        if ($layerName -like "_*") { return }
        $layer = $_.Value
        $w = if ($layer.weight) { [int]$layer.weight } else { 7 }
        foreach ($n in @($layer.ngrams)) {
            if (-not [string]::IsNullOrWhiteSpace($n) -and -not $NounPhrases.ContainsKey($n)) {
                $NounPhrases[$n] = $w
            }
        }
    }
}

# Build lemmatization map
$Lemmatize = @{}
if ($Config.lemmatize) {
    $Config.lemmatize.PSObject.Properties | ForEach-Object {
        $propName = $_.Name
        if ($propName -like "_*") { return }
        $Lemmatize[$propName] = $_.Value
    }
}
# Add engine defaults for universal suffixes (project-agnostic)
$DefaultLemmas = @{
    "developed"="develop";"developing"="develop";"develops"="develop"
    "structured"="structure";"structuring"="structure";"structures"="structure"
    "behaviors"="behaviour";"behavioural"="behaviour";"behavioral"="behaviour";"behavior"="behaviour";"behaviours"="behaviour"
    "organizational"="organisational";"organizations"="organisation";"organization"="organisation";"organisations"="organisation"
    "policies"="policy";"policymakers"="policy"
    "universities"="university";"university's"="university"
    "analyzing"="analyse";"analyzed"="analyse";"analyses"="analyse";"analyzes"="analyse"
    "compliance"="comply";"complied"="comply";"complies"="comply";"complying"="comply"
    "enforced"="enforce";"enforces"="enforce";"enforcement"="enforce"
    "mediated"="mediate";"mediates"="mediate";"mediation"="mediate"
    "interpreted"="interpret";"interpretation"="interpret";"interpreting"="interpret"
    "enacted"="enact";"enactment"="enact";"enacting"="enact"
    "readiness's"="readiness"
    "cybersecurity's"="cybersecurity";"cyber-security"="cybersecurity";"cyber security"="cybersecurity"
    "models"="model";"model's"="model"
    "assessments"="assessment";"assessment's"="assessment"
    "leaders"="leader";"leader's"="leader";"leadership's"="leadership"
    "governances"="governance"
    "institutions"="institution";"institution's"="institution";"institutional"="institution"
    "staffs"="staff";"staff's"="staff"
    "students"="student";"student's"="student"
    "faculties"="faculty";"faculty's"="faculty"
    "technologies"="technology";"technology's"="technology";"technological"="technology"
    "threats"="threat";"threat's"="threat"
    "vulnerabilities"="vulnerability";"vulnerability's"="vulnerability"
    "cultures"="culture";"culture's"="culture";"cultural"="culture"
    "educations"="education";"education's"="education";"educational"="education"
}
foreach ($k in $DefaultLemmas.Keys) {
    if (-not $Lemmatize.ContainsKey($k)) { $Lemmatize[$k] = $DefaultLemmas[$k] }
}

# Build stopword list
$UniversalStop = @(
    "a","an","the",
    "it","its","they","them","their","this","that","these","those","he","she","his","her",
    "from","in","on","at","to","for","of","with","by","through","between","among","into","onto","upon","about","over","under","within","without","before","after","during","since","until",
    "is","am","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","will","would","shall","should","can","could","may","might","must",
    "and","or","but","so","yet","nor","although","though","because","unless","whereas","while",
    "any","some","many","each","every","all","most","more","less","few","several","both","either","neither",
    "make","use","show","find","study","examine","analyse","analyze","investigate","consider","look","give","take","get","put","set","go","come","see","know","say","tell","work",
    "paper","article","research","analysis","review","framework","approach","method","methodology","results","findings","conclusion","introduction","background","discussion","section","table","figure","year","years","percent","percentage","number","level","case","cases","example","examples","context","contexts","part","parts","aspect","aspects","type","types","kind","form","forms",
    "new","novel","current","present","based","proposed","developed","designed","presented","explored","provided","shown","identified","highlighted","emphasized","outlined","described"
)
$Stopwords = @($UniversalStop)
if ($Config.stopwords.universal) { $Stopwords += @($Config.stopwords.universal) }
if ($Config.stopwords.project_specific) { $Stopwords += @($Config.stopwords.project_specific) }

# =========================================================================
# FUNCTIONS
# =========================================================================

function Clean-Text {
    param([string]$Text)
    $t = $Text.ToLower()
    $t = $t -replace '[^\w\s-]',' '
    $t = $t -replace '\s+',' '
    $t = $t.Trim()
    return $t
}

function Remove-Stopwords {
    param([string[]]$Tokens)
    $stopSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$Stopwords, [System.StringComparer]::OrdinalIgnoreCase)
    return $Tokens | Where-Object { -not $stopSet.Contains($_) }
}

function Invoke-Lemmatize {
    param([string[]]$Tokens)
    $out = @()
    foreach ($t in $Tokens) {
        $key = $t.ToLower()
        if ($Lemmatize.ContainsKey($key)) { $out += $Lemmatize[$key] }
        else { $out += $t }
    }
    return $out
}

function Get-Bigrams {
    param([string[]]$Tokens)
    $bigrams = @()
    for ($i=0; $i -lt $Tokens.Count-1; $i++) {
        $bigrams += "$($Tokens[$i]) $($Tokens[$i+1])"
    }
    return $bigrams
}

function Get-Trigrams {
    param([string[]]$Tokens)
    $trigrams = @()
    for ($i=0; $i -lt $Tokens.Count-2; $i++) {
        $trigrams += "$($Tokens[$i]) $($Tokens[$i+1]) $($Tokens[$i+2])"
    }
    return $trigrams
}

function Test-AutoReject {
    param([string]$Text)
    $lowered = $Text.ToLower()
    $allReject = @($ContextReject) + @($PopReject)
    # Auto-reject only if MULTIPLE bad terms match (single accidental mention does not disqualify)
    $matchCount = 0
    $matchedTerms = @()
    foreach ($bad in $allReject) {
        if (-not [string]::IsNullOrWhiteSpace($bad) -and $lowered -like "*$bad*") {
            $matchCount++
            $matchedTerms += $bad
            if ($matchCount -ge 2) { return $true }
        }
    }
    return $false
}

function Get-RelevanceScore {
    param([string]$Text)
    $score = 0
    $lowered = $Text.ToLower()
    $matches = @()
    $matchesCore = @()
    $matchesContext = @()
    $matchesMethod = @()
    $matchesTheory = @()

    foreach ($key in $NounPhrases.Keys) {
        if ([string]::IsNullOrWhiteSpace($key)) { continue }
        if ($lowered -like "*$key*") {
            $score += $NounPhrases[$key]
            $matches += $key
        }
    }
    foreach ($p in $CorePhrases) {
        if (-not [string]::IsNullOrWhiteSpace($p) -and $lowered -like "*$p*") {
            $score += $CoreWeight
            $matchesCore += $p
        }
    }
    foreach ($c in $ContextMust) {
        if (-not [string]::IsNullOrWhiteSpace($c) -and $lowered -like "*$c*") {
            $score += $ContextWeight
            $matchesContext += $c
        }
    }
    foreach ($m in $MethodPhrases) {
        if (-not [string]::IsNullOrWhiteSpace($m) -and $lowered -like "*$m*") {
            $score += $MethodWeight
            $matchesMethod += $m
        }
    }
    foreach ($t in $TheoryPhrases) {
        if (-not [string]::IsNullOrWhiteSpace($t) -and $lowered -like "*$t*") {
            $score += $TheoryWeight
            $matchesTheory += $t
        }
    }

    return @{
        Score       = $score
        Matches     = $matches     | Select-Object -Unique
        CoreHits    = $matchesCore | Select-Object -Unique
        ContextHits = $matchesContext | Select-Object -Unique
        MethodHits  = $matchesMethod | Select-Object -Unique
        TheoryHits  = $matchesTheory | Select-Object -Unique
    }
}

# =========================================================================
# PIPELINE
# =========================================================================

$CleanText = Clean-Text -Text $InputText
$RawTokens = $CleanText -split '\s+' | Where-Object { $_ -ne '' }
$Filtered  = Remove-Stopwords -Tokens $RawTokens
$Lemmas    = Invoke-Lemmatize -Tokens $Filtered
$Bigrams   = Get-Bigrams -Tokens $Lemmas
$Trigrams  = Get-Trigrams -Tokens $Lemmas
$IsReject  = Test-AutoReject -Text $InputText
$Relevance = Get-RelevanceScore -Text $InputText

switch ($Mode) {
    "analyze" {
        Write-Host "===== KEYWORD FILTER ANALYSIS =====" -ForegroundColor Cyan
        Write-Host " Project:     $($Config.project.code) - $($Config.project.name)" -ForegroundColor DarkCyan
        Write-Host " Config:      $ConfigPath"
        Write-Host "--------------------------------------"
        Write-Host " Original:    $($InputText.Length) chars"
        Write-Host " Tokens raw:  $($RawTokens.Count)"
        Write-Host " After stop:  $($Filtered.Count)"
        Write-Host " After lem:   $($Lemmas.Count)"
        Write-Host " Bigrams:     $($Bigrams.Count)"
        Write-Host " Trigrams:    $($Trigrams.Count)"
        Write-Host ""
        Write-Host " AUTO-REJECT: $IsReject" -ForegroundColor $(if($IsReject){"Red"}else{"Green"})
        Write-Host " SCORE:       $($Relevance.Score)  (accept>=$AcceptThresh, review>=$ReviewMin, reject<$RejectThresh)" -ForegroundColor $(
            if ($Relevance.Score -ge $AcceptThresh) {"Green"}
            elseif ($Relevance.Score -ge $ReviewMin) {"Yellow"}
            else {"Red"})
        Write-Host " DECISION:    $(
            if ($IsReject) {"REJECT (sector/population mismatch)"}
            elseif ($Relevance.Score -ge $AcceptThresh) {"ACCEPT - HIGHLY RELEVANT"}
            elseif ($Relevance.Score -ge $ReviewMin) {"ACCEPT - LIKELY RELEVANT"}
            elseif ($Relevance.Score -ge $RejectThresh) {"REVIEW MANUALLY"}
            else {"REJECT - LOW RELEVANCE"})"
        Write-Host ""
        if ($Relevance.Matches.Count -gt 0) {
            Write-Host " Noun phrases matched ($($Relevance.Matches.Count)):" -ForegroundColor Cyan
            $Relevance.Matches | ForEach-Object { Write-Host "   - $_" }
        }
        if ($Relevance.CoreHits.Count -gt 0) {
            Write-Host ""
            Write-Host " Core construct hits (+$CoreWeight each):" -ForegroundColor Magenta
            $Relevance.CoreHits | ForEach-Object { Write-Host "   * $_" }
        }
        if ($Relevance.ContextHits.Count -gt 0) {
            Write-Host ""
            Write-Host " Context hits (+$ContextWeight each):" -ForegroundColor Magenta
            $Relevance.ContextHits | ForEach-Object { Write-Host "   * $_" }
        }
        if ($Relevance.MethodHits.Count -gt 0) {
            Write-Host ""
            Write-Host " Method hits (+$MethodWeight each):" -ForegroundColor DarkMagenta
            $Relevance.MethodHits | ForEach-Object { Write-Host "   * $_" }
        }
        if ($Relevance.TheoryHits.Count -gt 0) {
            Write-Host ""
            Write-Host " Theory hits (+$TheoryWeight each):" -ForegroundColor DarkMagenta
            $Relevance.TheoryHits | ForEach-Object { Write-Host "   * $_" }
        }
    }
    "score" { return $Relevance.Score }
    "extract" {
        return @{
            Tokens   = $Lemmas
            Bigrams  = $Bigrams
            Trigrams = $Trigrams
            Score    = $Relevance
        }
    }
    "clean" { return $Lemmas -join " " }
    default {
        Write-Host "Unknown mode: $Mode" -ForegroundColor Red
        Write-Host "Valid modes: analyze | score | extract | clean"
    }
}
