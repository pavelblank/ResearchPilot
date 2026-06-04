# SCORE-AGAINST-INPUT.ps1
# ResearchPilot Input-Driven Scoring Engine (no project config required)
#
# Takes the user's ORIGINAL SEARCH INPUT and a paper's text, then scores the
# paper's relevance by counting how many of the EXTRACTED input PHRASES
# (multi-word) appear in the paper.
#
# STRICT MODE: single-word tokens are weak signal, multi-word phrases are
# the primary signal. A paper is ACCEPT only if it contains the user's
# actual concepts (phrases), not just any single word from the input.
#
# Usage (direct):
#   $r = & SCORE-AGAINST-INPUT.ps1 -InputText "cybersecurity readiness higher education" -PaperText "Paper title + abstract"
#
# Usage (with file):
#   $r = & SCORE-AGAINST-INPUT.ps1 -InputText "cybersecurity readiness higher education" -FilePath "C:\papers\paper.md"

param(
    [Parameter(Mandatory=$true)]
    [string]$InputText,

    [Parameter(Mandatory=$false)]
    [string]$PaperText = "",

    [Parameter(Mandatory=$false)]
    [string]$FilePath = "",

    [Parameter(Mandatory=$false)]
    [switch]$JustScore
)

$EngineRoot   = $PSScriptRoot
$ExtractScript = Join-Path $EngineRoot "EXTRACT-KEYWORDS.ps1"

# Resolve paper text
if (-not $PaperText -and $FilePath) {
    if (-not (Test-Path -LiteralPath $FilePath)) {
        Write-Error "File not found: $FilePath"
        return @{ Score = 0; Matches = @(); Decision = "REJECT - file not found" }
    }
    $PaperText = Get-Content -LiteralPath $FilePath -Raw -Encoding UTF8
}
if (-not $PaperText) {
    Write-Error "Provide -PaperText or -FilePath"
    return @{ Score = 0; Matches = @(); Decision = "REJECT - no text" }
}

# ---------------------------------------------------------------------------
# STEP 1: Extract keywords from the user's INPUT (not from any project)
# ---------------------------------------------------------------------------
$Extraction = & $ExtractScript -InputText $InputText -Mode analyze -Project "DEFAULT"

# Trigrams (3-word phrases) = the strong signal. These are the user's actual concepts.
# Bigrams (2-word phrases) = the medium signal.
# Single-word tokens (Tier A) = the weak signal.

# Build vocabulary from ALL trigrams in the input, then add unique bigrams and singles
$Trigrams = @()
if ($Extraction.RawTrigrams) {
    $Trigrams = @($Extraction.RawTrigrams)
}

$Bigrams = @()
if ($Extraction.RawBigrams) {
    $Bigrams = @($Extraction.RawBigrams)
}

$SingleWords = @()
if ($Extraction.Tokens) {
    foreach ($t in @($Extraction.Tokens)) {
        $wordCount = ($t -split '\s+').Count
        if ($wordCount -eq 1) { $SingleWords += $t }
    }
}
$SingleWords = $SingleWords | Select-Object -Unique

if ($Trigrams.Count -eq 0 -and $Bigrams.Count -eq 0 -and $SingleWords.Count -eq 0) {
    $Result = @{
        Score    = 0
        Matches  = @()
        Decision = "REJECT - no keywords extracted from input"
    }
    if ($JustScore) { return 0 }
    return $Result
}

# ---------------------------------------------------------------------------
# STEP 2: Score the paper
# ---------------------------------------------------------------------------
$PaperLower = $PaperText.ToLower()
$Score = 0
$MatchedTrigrams = @()
$MatchedBigrams = @()
$MatchedSingles = @()
$MatchDetails = @()

# 2a. Trigrams (3-word phrases) = strong signal (4 pts per match)
foreach ($tri in $Trigrams) {
    $p = $tri.ToLower().Trim()
    if ([string]::IsNullOrWhiteSpace($p)) { continue }

    $occurrences = ([regex]::Matches($PaperLower, [regex]::Escape($p))).Count
    if ($occurrences -gt 0) {
        $weight = 4
        $freqBonus = 0
        if ($occurrences -ge 3) { $freqBonus = 2 }
        elseif ($occurrences -ge 2) { $freqBonus = 1 }

        $termScore = $weight + $freqBonus
        $Score += $termScore
        $MatchedTrigrams += $tri
        $MatchDetails += [PSCustomObject]@{
            Term        = $tri
            Type        = "TRIGRAM"
            Occurrences = $occurrences
            Score       = $termScore
        }
    }
}

# 2b. Bigrams (2-word phrases) = medium signal (2 pts per match)
foreach ($bi in $Bigrams) {
    $p = $bi.ToLower().Trim()
    if ([string]::IsNullOrWhiteSpace($p)) { continue }

    $occurrences = ([regex]::Matches($PaperLower, [regex]::Escape($p))).Count
    if ($occurrences -gt 0) {
        $weight = 2
        $freqBonus = 0
        if ($occurrences -ge 3) { $freqBonus = 1 }

        $termScore = $weight + $freqBonus
        $Score += $termScore
        $MatchedBigrams += $bi
        $MatchDetails += [PSCustomObject]@{
            Term        = $bi
            Type        = "BIGRAM"
            Occurrences = $occurrences
            Score       = $termScore
        }
    }
}

# 2c. Single words = weak signal (1 pt each, capped at 3 total)
$singleScore = 0
foreach ($word in $SingleWords) {
    $w = $word.ToLower().Trim()
    if ([string]::IsNullOrWhiteSpace($w)) { continue }
    if ($singleScore -ge 3) { break }  # cap

    $occurrences = ([regex]::Matches($PaperLower, [regex]::Escape($w))).Count
    if ($occurrences -gt 0) {
        $singleScore += 1
        $MatchedSingles += $word
        $MatchDetails += [PSCustomObject]@{
            Term        = $word
            Type        = "SINGLE"
            Occurrences = $occurrences
            Score       = 1
        }
    }
}
$Score += $singleScore

# ---------------------------------------------------------------------------
# STEP 3: Decision
#   - ACCEPT: at least 2 trigrams matched, OR (1 trigram + score >= 6)
#   - REVIEW: at least 1 trigram matched, OR (2 bigrams + score >= 4)
#   - REJECT: nothing meaningful matched
# ---------------------------------------------------------------------------
$trigramCount = $MatchedTrigrams.Count
$bigramCount  = $MatchedBigrams.Count

if ($trigramCount -ge 2)                 { $Decision = "ACCEPT - HIGHLY RELEVANT" }
elseif ($trigramCount -ge 1 -and $Score -ge 6)  { $Decision = "ACCEPT - LIKELY RELEVANT" }
elseif ($trigramCount -ge 1)             { $Decision = "REVIEW - partial trigram match" }
elseif ($bigramCount -ge 3)              { $Decision = "REVIEW - multiple bigrams matched" }
elseif ($bigramCount -ge 1 -and $Score -ge 4)  { $Decision = "REVIEW MANUALLY" }
else                                     { $Decision = "REJECT - LOW RELEVANCE" }

# ---------------------------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------------------------
$Result = @{
    Score           = $Score
    Decision        = $Decision
    TrigramMatches  = $MatchedTrigrams | Select-Object -Unique
    BigramMatches   = $MatchedBigrams | Select-Object -Unique
    SingleMatches   = $MatchedSingles | Select-Object -Unique
    MatchDetails    = $MatchDetails
    Trigrams        = $Trigrams
    Bigrams         = $Bigrams
    SingleWords     = $SingleWords
}

if ($JustScore) {
    return $Score
}
return $Result
