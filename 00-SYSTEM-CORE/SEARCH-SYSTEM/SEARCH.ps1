# SEARCH.ps1
# ResearchPilot One-Shot Web Search Wrapper (v2)
# Takes user input, runs the 8-step pipeline, returns PRIMARY/FALLBACK/DATE/DROPPED

param(
    [Parameter(Mandatory=$true)]
    [string]$InputText,

    [Parameter(Mandatory=$false)]
    [string]$Project = "DEFAULT",

    [Parameter(Mandatory=$false)]
    [string]$OutputFormat = "all",  # all | primary | fallback | scholar | scopus | json

    [Parameter(Mandatory=$false)]
    [int]$MaxKeywords = 12,

    [Parameter(Mandatory=$false)]
    [string]$ExtraExclude = "",

    [Parameter(Mandatory=$false)]
    [switch]$NoColor
)

$EngineRoot = $PSScriptRoot
$ExtractScript = Join-Path $EngineRoot "EXTRACT-KEYWORDS.ps1"

function W {
    param([string]$Text, [string]$Color = "White")
    if ($NoColor) { Write-Host $Text } else { Write-Host $Text -ForegroundColor $Color }
}

W "==========================================" "Cyan"
W " ResearchPilot SEARCH (v2 - 8-step pipeline)" "Cyan"
W "==========================================" "Cyan"
W " Project:  $Project"
W " Input:    $InputText"
W ""

# -------------------------------------------------------------------------
# Run the 8-step pipeline
# -------------------------------------------------------------------------
W "[1/4] Running 8-step pipeline (year -> stopwords -> punct -> numbers -> tier -> phrases -> score -> query)..." "Yellow"

$result = & $ExtractScript -InputText $InputText -Mode analyze -Project $Project

if (-not $result) {
    W "Pipeline failed - no result returned." "Red"
    exit 1
}

# Build strings from the result object
$primaryList = @($result.Primary | ForEach-Object { $_.Term })
$fallbackList = @($result.Fallback | ForEach-Object { $_.Term })
$dateFilter = $result.Date
$dropped = @($result.Dropped)

$primaryQuery = ($primaryList | ForEach-Object { '"' + $_ + '"' }) -join ' AND '
$fallbackQuery = ($fallbackList | ForEach-Object { '"' + $_ + '"' }) -join ' OR '

# Build Scopus-formatted query with project exclusions
$scopusPrimary = ""
if ($primaryList.Count -gt 0) {
    $scopusPrimary = "TITLE-ABS-KEY ( " + (($primaryList | ForEach-Object { '"' + $_ + '"' }) -join ' OR ') + " )"
}
$scopusFallback = ""
if ($fallbackList.Count -gt 0) {
    $scopusFallback = "TITLE-ABS-KEY ( " + (($fallbackList | ForEach-Object { '"' + $_ + '"' }) -join ' OR ') + " )"
}

# Add exclusion block from project config
$excludeList = @()
if ($ExtraExclude) { $excludeList += $ExtraExclude -split ',' | ForEach-Object { $_.Trim() } }
if ($Project -ne "DEFAULT") {
    $ConfigPath = Join-Path $EngineRoot "projects\$Project.json"
    if (Test-Path -LiteralPath $ConfigPath) {
        $Config = Get-Content -LiteralPath $ConfigPath -Raw -Encoding UTF8 | ConvertFrom-Json
        if ($Config.context_anchors.must_not_have) { $excludeList += @($Config.context_anchors.must_not_have) }
        if ($Config.population_anchors.auto_reject_populations) { $excludeList += @($Config.population_anchors.auto_reject_populations) }
    }
}
$excludeBlock = ""
if ($excludeList.Count -gt 0) {
    $excludes = $excludeList | ForEach-Object { '"' + $_ + '"' }
    $excludeBlock = " AND NOT TITLE-ABS-KEY ( $($excludes -join ' OR ') )"
}

# Add year filter to Scopus query
$yearBlock = ""
if ($dateFilter -and $dateFilter -match '\d{4}') {
    if ($dateFilter -match '\d{4}\.\.\d{4}') {
        $parts = $dateFilter -split '\.\.'
        $yearBlock = " AND PUBYEAR > $($parts[0]-1) AND PUBYEAR < $($parts[1]+1)"
    } else {
        $yearBlock = " AND PUBYEAR = $dateFilter"
    }
}

$scopusFull = $scopusPrimary + $excludeBlock + $yearBlock
if (-not $scopusFull) { $scopusFull = "(no primary query built)" }

# -------------------------------------------------------------------------
# Output
# -------------------------------------------------------------------------
switch ($OutputFormat) {
    "primary" { return $primaryQuery }
    "fallback" { return $fallbackQuery }
    "scopus" { return $scopusFull }
    "json" { return ($result | ConvertTo-Json -Depth 8) }
    "scholar" {
        W "[2/4] Google Scholar batch (paste one phrase per search):" "Cyan"
        W "----------------------------------------"
        if ($primaryList.Count -gt 0) {
            W "  PRIMARY (AND-joined):" "Green"
            W "  $primaryQuery" "White"
        }
        if ($fallbackList.Count -gt 0) {
            W ""
            W "  FALLBACK (OR-joined):" "Yellow"
            W "  $fallbackQuery" "White"
        }
        W "----------------------------------------"
        W ""
        W "[3/4] One-line search (Scopus / WoS TITLE-ABS-KEY):" "Cyan"
        W "----------------------------------------"
        W "  $scopusFull" "White"
        W "----------------------------------------"
        if ($dateFilter) {
            W ""
            W "  DATE_FILTER: $dateFilter" "Magenta"
        }
    }
    default {
        W "[2/4] PRIMARY query (top 4 phrases, AND-joined):" "Cyan"
        W "----------------------------------------"
        if ($primaryList.Count -gt 0) {
            W "  $primaryQuery" "Green"
        } else {
            W "  (none - input too short)" "Red"
        }
        W "----------------------------------------"
        W ""
        W "[3/4] FALLBACK query (next 3 terms, OR-joined):" "Cyan"
        W "----------------------------------------"
        if ($fallbackList.Count -gt 0) {
            W "  $fallbackQuery" "Yellow"
        } else {
            W "  (none)" "DarkGray"
        }
        W "----------------------------------------"
        W ""
        W "[4/4] Ready-to-paste Scopus/WoS query (with exclusions + year):" "Cyan"
        W "----------------------------------------"
        W "  $scopusFull" "White"
        W "----------------------------------------"
        if ($dateFilter) {
            W ""
            W "  DATE_FILTER: $dateFilter" "Magenta"
        }
        W ""
        W "DROPPED ($($dropped.Count) terms):" "DarkYellow"
        $dropped | Group-Object Reason | ForEach-Object {
            W "   $($_.Name): $($_.Group.Term -join ', ')" "DarkGray"
        }
    }
}

W ""
W "NEXT STEPS:" "Yellow"
W "  1. Copy the PRIMARY query (or Scopus-formatted one) above" "White"
W "  2. Run the search" "White"
W "  3. For each result, run:" "White"
W "     .\PRE-FILTER.ps1 -FilePath <paper> -Project $Project" "White"
