# EVALUATE-RESULT.ps1
# Single-paper test harness for the journal quality filter.
# Loads a paper JSON descriptor from disk and runs JOURNAL-QUALITY-FILTER.ps1.

param(
    [Parameter(Mandatory=$true)]
    [string]$PaperFile,

    [Parameter(Mandatory=$false)]
    [switch]$ShowPredatory,

    [Parameter(Mandatory=$false)]
    [string]$ExtraPredatoryPath = ""
)

$ScriptDir  = $PSScriptRoot
$FilterPath = Join-Path $ScriptDir "JOURNAL-QUALITY-FILTER.ps1"

if (-not (Test-Path $PaperFile)) {
    Write-Error "Paper descriptor not found: $PaperFile"
    exit 1
}

# Source the filter script
. $FilterPath

$Paper = Get-Content $PaperFile -Raw | ConvertFrom-Json

$Result = Get-JournalQuality -JournalName   $Paper.journalName `
                              -Publisher     $Paper.publisher `
                              -Doi           $Paper.doi `
                              -CitationCount ([int]$Paper.citationCount) `
                              -Year          ([int]$Paper.year) `
                              -IsOpenAccess  ([bool]$Paper.isOpenAccess) `
                              -IsInDoaj      ([bool]$Paper.isInDoaj) `
                              -IsPreprint    ([bool]$Paper.isPreprint) `
                              -Source        $Paper.source `
                              -RelevanceScore ([int]$Paper.relevanceScore) `
                              -ExtraPredatoryPath $ExtraPredatoryPath `
                              -ShowPredatory:$ShowPredatory

# Pretty print
"`n=== PAPER ==="
"Title    : $($Paper.title)"
"Journal  : $($Paper.journalName)"
"Year     : $($Paper.year)"
"Cited by : $($Paper.citationCount)"
"OA       : $($Paper.isOpenAccess)  DOAJ: $($Paper.isInDoaj)  Preprint: $($Paper.isPreprint)"
"`n=== QUALITY FILTER RESULT ==="
"TIER     : $($Result.TierName) (Tier $($Result.Tier))"
"QUARTILE : $($Result.Quartile)"
"PEER-REVIEW : $($Result.IsPeerReviewed)"
"SCORES   : Relevance $($Result.RelevanceScore)  Quality $($Result.QualityScore)  FINAL $($Result.FinalScore)"
"BADGES   : $($Result.Badges)"
"REASONS  : $($Result.Reasons)"
"ACTION   : $($Result.Action)"
"`n"

# Also emit a CSV row for batch processing
$Result | Export-Csv -Path ([System.IO.Path]::ChangeExtension($PaperFile, ".evaluated.csv")) -NoTypeInformation -Append
