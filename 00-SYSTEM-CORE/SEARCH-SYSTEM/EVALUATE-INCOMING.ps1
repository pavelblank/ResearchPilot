# EVALUATE-INCOMING.ps1
# Top-level single-shot evaluator.
# Combines:
#   1. PRE-FILTER (relevance scoring against project config)
#   2. JOURNAL-QUALITY-FILTER (tier + quality scoring)
# For an INCOMING paper, producing a final ACCEPT/REVIEW/REJECT verdict.
#
# Usage:
#   pwsh -File EVALUATE-INCOMING.ps1 -FilePath "..\..\INCOMING\paper.md" -Project P1-HEI-CULTURE
#   pwsh -File EVALUATE-INCOMING.ps1 -FilePath "paper.md" -Project P1-HEI-CULTURE -MetadataJson "paper.meta.json"

param(
    [Parameter(Mandatory=$true)]
    [string]$FilePath,

    [Parameter(Mandatory=$false)]
    [string]$ConfigPath = "",

    [Parameter(Mandatory=$false)]
    [string]$Project = "P1-HEI-CULTURE",

    [Parameter(Mandatory=$false)]
    [string]$MetadataJson = "",

    [Parameter(Mandatory=$false)]
    [string]$OutputCsv = "",

    [Parameter(Mandatory=$false)]
    [switch]$MoveRejects,

    [Parameter(Mandatory=$false)]
    [switch]$ShowPredatory,

    [Parameter(Mandatory=$false)]
    [string]$ExtraPredatoryPath = ""
)

$EngineRoot  = $PSScriptRoot
$PreFilter   = Join-Path $EngineRoot "PRE-FILTER.ps1"
$QualityFilt = Join-Path $EngineRoot "JOURNAL-QUALITY-FILTER.ps1"

if (-not (Test-Path $FilePath)) {
    Write-Host "File not found: $FilePath" -ForegroundColor Red
    exit 1
}

# -------------------------------------------------------------------------
# Stage 1: Relevance filter (single run, suppress PRE-FILTER's host output)
# -------------------------------------------------------------------------
Write-Host "Stage 1: Relevance scoring..." -ForegroundColor Cyan

# Capture all streams (Write-Host bypasses normal output redirection, so use *>&1)
$preOutput = & $PreFilter -FilePath $FilePath -ConfigPath $ConfigPath -Project $Project *>&1 | Out-String

# Extract the integer score from the SCORE line
$relScore = 0
foreach ($line in (($preOutput -replace "`r`n","`n" -replace "`r","`n") -split "`n")) {
    if ($line -match "SCORE:\s+(\d+)") { $relScore = [int]$matches[1]; break }
}

# Show only the PRE-FILTER REPORT block (suppress the inner keyword analysis)
$showing = $false
foreach ($line in (($preOutput -replace "`r`n","`n" -replace "`r","`n") -split "`n")) {
    if ($line -match "PRE-FILTER REPORT") { $showing = $true }
    if ($showing) { Write-Host $line }
}

# Detect auto-reject
$autoReject = $false
foreach ($line in (($preOutput -replace "`r`n","`n" -replace "`r","`n") -split "`n")) {
    if ($line -match "AUTO-REJECT:\s+True") { $autoReject = $true; break }
}

# Recompute decision from score (single source of truth)
$ConfigObj = if ($ConfigPath) {
    Get-Content -LiteralPath $ConfigPath -Raw -Encoding UTF8 | ConvertFrom-Json
} else {
    Get-Content -LiteralPath (Join-Path $EngineRoot "projects\$Project.json") -Raw -Encoding UTF8 | ConvertFrom-Json
}
$AcceptThresh = if ($ConfigObj.scoring.accept_threshold) { $ConfigObj.scoring.accept_threshold } else { 20 }
$ReviewMin    = if ($ConfigObj.scoring.review_min)       { $ConfigObj.scoring.review_min }       else { 10 }
$RejectThresh = if ($ConfigObj.scoring.reject_threshold) { $ConfigObj.scoring.reject_threshold } else { 5 }

if ($autoReject)        { $relDecision = "REJECT (sector/population mismatch)" }
elseif ($relScore -ge $AcceptThresh) { $relDecision = "ACCEPT - HIGHLY RELEVANT" }
elseif ($relScore -ge $ReviewMin)    { $relDecision = "ACCEPT - LIKELY RELEVANT" }
elseif ($relScore -ge $RejectThresh) { $relDecision = "REVIEW MANUALLY" }
else                                  { $relDecision = "REJECT - LOW RELEVANCE" }

# -------------------------------------------------------------------------
# Stage 2: Journal quality (requires metadata)
# -------------------------------------------------------------------------
$quality = $null
if ($MetadataJson -and (Test-Path $MetadataJson)) {
    Write-Host "Stage 2: Journal quality scoring..." -ForegroundColor Cyan
    . $QualityFilt
    $Meta = Get-Content $MetadataJson -Raw | ConvertFrom-Json
    $quality = Get-JournalQuality -JournalName   $Meta.journalName `
                                  -Publisher     $Meta.publisher `
                                  -CitationCount ([int]$Meta.citationCount) `
                                  -Year          ([int]$Meta.year) `
                                  -IsOpenAccess  ([bool]$Meta.isOpenAccess) `
                                  -IsInDoaj      ([bool]$Meta.isInDoaj) `
                                  -IsPreprint    ([bool]$Meta.isPreprint) `
                                  -Source        $Meta.source `
                                  -RelevanceScore $relScore `
                                  -ExtraPredatoryPath $ExtraPredatoryPath `
                                  -ShowPredatory:$ShowPredatory
}
else {
    Write-Host "Stage 2: SKIPPED (no -MetadataJson provided)" -ForegroundColor DarkGray
}

# -------------------------------------------------------------------------
# Combined verdict
# -------------------------------------------------------------------------
$finalScore = if ($quality) { $quality.FinalScore } else { $relScore }
$verdict = switch -Wildcard ($relDecision) {
    "*REJECT*sector*" { "REJECT (auto: sector/population mismatch)" }
    "*HIGHLY RELEVANT*" {
        if ($quality -and $quality.Tier -eq 4) { "REJECT (predatory journal)" }
        elseif ($quality -and $quality.Tier -eq 3 -and $quality.QualityScore -lt 0) { "REVIEW (unverified, low quality)" }
        else { "ACCEPT (high relevance)" }
    }
    "*LIKELY RELEVANT*" {
        if ($quality -and $quality.Tier -eq 4) { "REJECT (predatory journal)" }
        else { "ACCEPT (likely relevant)" }
    }
    "*REVIEW MANUALLY*" {
        if ($quality -and $quality.Tier -eq 4) { "REJECT (predatory journal)" }
        elseif ($quality -and $quality.Tier -eq 1) { "ACCEPT (relevance borderline, but journal Tier 1)" }
        else { "REVIEW MANUALLY" }
    }
    "*LOW RELEVANCE*" { "REJECT (low relevance)" }
    default { "UNKNOWN" }
}

$color = switch -Wildcard ($verdict) {
    "*ACCEPT*" { "Green" }
    "*REVIEW*" { "Yellow" }
    "*REJECT*" { "Red" }
    default { "Gray" }
}

# -------------------------------------------------------------------------
# Combined report
# -------------------------------------------------------------------------
Write-Host ""
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host " FINAL VERDICT" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host " Project:    $Project"
Write-Host " File:       $(Split-Path -Leaf $FilePath)"
Write-Host " Relevance:  $relScore  -> $relDecision"
if ($quality) {
    Write-Host " Journal:    $($quality.TierName) (Tier $($quality.Tier))"
    Write-Host " Quartile:   $($quality.Quartile)"
    Write-Host " Peer-Reviewed: $($quality.IsPeerReviewed)"
    Write-Host " Quality:    $($quality.QualityScore)"
    Write-Host " Badges:     $($quality.Badges)"
}
Write-Host " Final:      $finalScore"
Write-Host " Verdict:    $verdict" -ForegroundColor $color
Write-Host ""

# -------------------------------------------------------------------------
# CSV row
# -------------------------------------------------------------------------
if ($OutputCsv) {
    $row = [PSCustomObject]@{
        FileName      = Split-Path -Leaf $FilePath
        Project       = $Project
        Relevance     = $relScore
        RelevanceDec  = $relDecision
        Tier          = if ($quality) { $quality.Tier } else { "" }
        TierName      = if ($quality) { $quality.TierName } else { "" }
        Quality       = if ($quality) { $quality.QualityScore } else { "" }
        FinalScore    = $finalScore
        Badges        = if ($quality) { $quality.BadgeList } else { "" }
        Verdict       = $verdict
        EvaluatedAt   = (Get-Date -Format "yyyy-MM-dd HH:mm")
    }
    $row | Export-Csv -LiteralPath $OutputCsv -Append -NoTypeInformation -Encoding UTF8
    Write-Host " Logged to: $OutputCsv" -ForegroundColor DarkGray
}

# Exit code
switch -Wildcard ($verdict) {
    "*ACCEPT*"      { exit 0 }
    "*REVIEW*"      { exit 2 }
    "*REJECT*"      { exit 1 }
    default         { exit 3 }
}
