# PRE-FILTER.ps1
# ResearchPilot Universal Paper Gatekeeper
# Project-agnostic: reads keywords from a JSON config file
# Run this on every paper in INCOMING/ BEFORE moving it to 01-LIBRARY/

param(
    [Parameter(Mandatory=$true)]
    [string]$FilePath,

    [Parameter(Mandatory=$false)]
    [string]$ConfigPath = "",

    [Parameter(Mandatory=$false)]
    [string]$Project = "P1-HEI-CULTURE",

    [Parameter(Mandatory=$false)]
    [string]$OutputCsv = "",

    [Parameter(Mandatory=$false)]
    [switch]$MoveRejects,

    [Parameter(Mandatory=$false)]
    [string]$RejectFolder = "",

    [Parameter(Mandatory=$false)]
    [switch]$ScoreOnly
)

$EngineRoot = $PSScriptRoot
$FilterScript = Join-Path $EngineRoot "KEYWORD-FILTER.ps1"

if (-not $ConfigPath) {
    $ConfigPath = Join-Path $EngineRoot "projects\$Project.json"
}
if (-not (Test-Path -LiteralPath $ConfigPath)) {
    Write-Host "Config not found: $ConfigPath" -ForegroundColor Red
    exit 1
}
$Config = Get-Content -LiteralPath $ConfigPath -Raw -Encoding UTF8 | ConvertFrom-Json

if (-not $OutputCsv) {
    # $PSScriptRoot is ...\00-SYSTEM-CORE\SEARCH-SYSTEM\
    # Project queries folder is ...\01-PROJECTS\<folder>\99-META\queries\
    $folderName = if ($Config.project.folder) { $Config.project.folder } else { $Config.project.code }
    $ProjectQueries = Join-Path $PSScriptRoot "..\..\01-PROJECTS\$folderName\99-META\queries"
    if (Test-Path -LiteralPath $ProjectQueries) {
        $OutputCsv = Join-Path $ProjectQueries "PRE-FILTER-RESULTS.csv"
    } else {
        $OutputCsv = Join-Path (Split-Path $ConfigPath) "PRE-FILTER-RESULTS.csv"
    }
}

if (-not $RejectFolder) {
    $RejectFolder = "C:\F- Drive\MYWORK-Research1\INCOMING\_REJECTED"
}

if (-not (Test-Path -LiteralPath $FilePath)) {
    Write-Host "File not found: $FilePath" -ForegroundColor Red
    exit 1
}

# -------------------------------------------------------------------------
# Read paper text
# -------------------------------------------------------------------------
$content = Get-Content -LiteralPath $FilePath -Raw -Encoding UTF8
$head = $content.Substring(0, [Math]::Min(5000, $content.Length))

# Heuristic abstract extraction
$abstract = ""
if ($content -match '(?is)abstract\s*[:\-]?\s*(.+?)(?=\n\s*(?:introduction|1\.|keywords|index terms))') {
    $abstract = $matches[1].Trim()
}
if ([string]::IsNullOrWhiteSpace($abstract)) {
    $abstract = $head
}

# -------------------------------------------------------------------------
# Run the filter
# -------------------------------------------------------------------------
$scoreResult = & $FilterScript -InputText $abstract -Mode score -ConfigPath $ConfigPath -Project $Project
$analysisText = & $FilterScript -InputText $abstract -Mode analyze -ConfigPath $ConfigPath -Project $Project 2>&1 | Out-String

$scoreNumber = if ($scoreResult -is [int]) { $scoreResult } else { 0 }

if ($ScoreOnly) {
    Write-Output $scoreNumber
    exit 0
}

# Derive decision from score + auto-reject directly (more reliable than parsing text)
$AcceptThresh = if ($Config.scoring.accept_threshold) { $Config.scoring.accept_threshold } else { 20 }
$ReviewMin    = if ($Config.scoring.review_min) { $Config.scoring.review_min } else { 10 }
$RejectThresh = if ($Config.scoring.reject_threshold) { $Config.scoring.reject_threshold } else { 5 }

# Auto-reject from analysis text
$autoReject = $false
$normalizedAnalysis = $analysisText -replace "`r`n","`n" -replace "`r","`n"
foreach ($line in ($normalizedAnalysis -split "`n")) {
    if ($line -match "AUTO-REJECT:\s+True") { $autoReject = $true; break }
}

if ($autoReject) {
    $decision = "REJECT (sector/population mismatch)"
}
elseif ($scoreNumber -ge $AcceptThresh) {
    $decision = "ACCEPT - HIGHLY RELEVANT"
}
elseif ($scoreNumber -ge $ReviewMin) {
    $decision = "ACCEPT - LIKELY RELEVANT"
}
elseif ($scoreNumber -ge $RejectThresh) {
    $decision = "REVIEW MANUALLY"
}
else {
    $decision = "REJECT - LOW RELEVANCE"
}

# -------------------------------------------------------------------------
# Build record
# -------------------------------------------------------------------------
$record = [PSCustomObject]@{
    ProjectCode  = $Config.project.code
    FileName     = Split-Path -Leaf $FilePath
    FilePath     = $FilePath
    Score        = $scoreNumber
    Decision     = $decision
    AutoRejected = $autoReject
    FilteredAt   = (Get-Date -Format "yyyy-MM-dd HH:mm")
    WordCount    = ($content -split '\s+').Count
}

$record | Export-Csv -LiteralPath $OutputCsv -Append -NoTypeInformation -Encoding UTF8

# -------------------------------------------------------------------------
# Output
# -------------------------------------------------------------------------
Write-Host ""
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host " PRE-FILTER REPORT" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host " Project:   $($Config.project.code) - $($Config.project.name)"
Write-Host " File:      $($record.FileName)"
Write-Host " Score:     $scoreNumber" -ForegroundColor $(
    if ($scoreNumber -ge $Config.scoring.accept_threshold) {"Green"}
    elseif ($scoreNumber -ge $Config.scoring.review_min) {"Yellow"}
    else {"Red"})
Write-Host " Decision:  $decision" -ForegroundColor $(
    if ($decision -like "*ACCEPT*") {"Green"}
    elseif ($decision -like "*REVIEW*") {"Yellow"}
    else {"Red"})
Write-Host " Log:       $OutputCsv"
Write-Host ""

if ($MoveRejects -and ($decision -like "*REJECT*")) {
    if (-not (Test-Path -LiteralPath $RejectFolder)) {
        New-Item -ItemType Directory -Path $RejectFolder -Force | Out-Null
    }
    $dest = Join-Path $RejectFolder $record.FileName
    Move-Item -LiteralPath $FilePath -Destination $dest -Force
    Write-Host "Moved to: $dest" -ForegroundColor Red
}

# Exit codes for pipeline chaining
switch -Wildcard ($decision) {
    "*ACCEPT - HIGHLY*" { exit 0 }
    "*ACCEPT - LIKELY*" { exit 0 }
    "*REVIEW*"          { exit 2 }
    default             { exit 1 }
}
