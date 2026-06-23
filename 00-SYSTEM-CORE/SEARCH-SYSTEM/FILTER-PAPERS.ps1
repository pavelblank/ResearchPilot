# FILTER-PAPERS.ps1
# ResearchPilot Universal Paper Filter (project-free, input-driven)
#
# Takes a user's search intent + a folder of papers, and rates each paper
# for relevance to the intent. NO project config, NO predefined keywords.
# The extracted keywords from the input ARE the scoring vocabulary.
#
# Usage:
#   pwsh FILTER-PAPERS.ps1 -InputText "cybersecurity readiness in higher education" -Folder "C:\papers"
#   pwsh FILTER-PAPERS.ps1 -InputText "..." -Folder "..." -OutputCsv "results.csv"
#   pwsh FILTER-PAPERS.ps1 -InputText "..." -Folder "..." -MoveRejects -RejectFolder "C:\papers\_rejected"
#   pwsh FILTER-PAPERS.ps1 -InputText "..." -Folder "..." -EnableQualityFilter -ShowPredatory
#
# Switches:
#   -ShowPredatory         Tier 4 (Beall's-list) papers are HIDDEN by default;
#                          pass this to expose them with a red "Predatory" badge.
#   -EnableQualityFilter   Run JOURNAL-QUALITY-FILTER alongside the relevance
#                          scorer. Reads metadata from YAML frontmatter or from
#                          inline "**Journal:** ..." lines in the .md file.
#                          Downgrades ACCEPT -> REVIEW for Tier 3; REJECTS
#                          Tier 4 (unless -ShowPredatory is also passed).

param(
    [Parameter(Mandatory=$true)]
    [string]$InputText,

    [Parameter(Mandatory=$true)]
    [string]$Folder,

    [Parameter(Mandatory=$false)]
    [string]$Pattern = "*.md",

    [Parameter(Mandatory=$false)]
    [string]$OutputCsv = "",

    [Parameter(Mandatory=$false)]
    [switch]$MoveRejects,

    [Parameter(Mandatory=$false)]
    [string]$RejectFolder = "",

    [Parameter(Mandatory=$false)]
    [switch]$NoColor,

    [Parameter(Mandatory=$false)]
    [switch]$ShowPredatory,

    [Parameter(Mandatory=$false)]
    [switch]$EnableQualityFilter,

    [Parameter(Mandatory=$false)]
    [string]$ExtraPredatoryPath = ""
)

$EngineRoot    = $PSScriptRoot
$ScoreScript   = Join-Path $EngineRoot "SCORE-AGAINST-INPUT.ps1"
$ExtractScript = Join-Path $EngineRoot "EXTRACT-KEYWORDS.ps1"
$QualityScript = Join-Path $EngineRoot "JOURNAL-QUALITY-FILTER.ps1"

if ($EnableQualityFilter) {
    . $QualityScript
}

function W {
    param([string]$Text, [string]$Color = "White")
    if ($NoColor) { Write-Host $Text } else { Write-Host $Text -ForegroundColor $Color }
}

# ---------------------------------------------------------------------------
# Parse paper metadata from YAML frontmatter or inline "Key: Value" lines
# ---------------------------------------------------------------------------
function Get-PaperMetadata {
    param([string]$FilePath)
    $meta = [PSCustomObject]@{
        JournalName = ""
        Publisher   = ""
        Doi         = ""
        Year        = 0
        Citations   = 0
        IsOpenAccess = $false
        IsInDoaj    = $false
        IsPreprint  = $false
        Source      = ""
    }
    if (-not (Test-Path -LiteralPath $FilePath)) { return $meta }

    $content = Get-Content -LiteralPath $FilePath -Raw -ErrorAction SilentlyContinue
    if (-not $content) { return $meta }

    # 1. YAML frontmatter (between first two --- lines)
    if ($content -match '(?s)\A---\s*\r?\n(.*?)\r?\n---\s*\r?\n') {
        $fm = $Matches[1]
        foreach ($line in ($fm -split '\r?\n')) {
            if ($line -match '^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.+?)\s*$') {
                $k = $Matches[1]; $v = $Matches[2].Trim().Trim('"').Trim("'")
                switch ($k) {
                    "Journal"      { $meta.JournalName = $v }
                    "Publisher"    { $meta.Publisher   = $v }
                    "JournalName"  { $meta.JournalName = $v }
                    "Doi"          { $meta.Doi         = $v }
                    "DOI"          { $meta.Doi         = $v }
                    "Year"         { if ([int]::TryParse($v,[ref]$null)) { $meta.Year = [int]$v } }
                    "Citations"    { if ([int]::TryParse($v.Replace(',',''),[ref]$null)) { $meta.Citations = [int]$v.Replace(',','') } }
                    "CitationCount"{ if ([int]::TryParse($v.Replace(',',''),[ref]$null)) { $meta.Citations = [int]$v.Replace(',','') } }
                    "OpenAccess"   { $meta.IsOpenAccess = ($v -match '^(true|yes|1)$') }
                    "IsOpenAccess" { $meta.IsOpenAccess = ($v -match '^(true|yes|1)$') }
                    "InDoaj"       { $meta.IsInDoaj    = ($v -match '^(true|yes|1)$') }
                    "IsInDoaj"     { $meta.IsInDoaj    = ($v -match '^(true|yes|1)$') }
                    "Preprint"     { $meta.IsPreprint  = ($v -match '^(true|yes|1)$') }
                    "IsPreprint"   { $meta.IsPreprint  = ($v -match '^(true|yes|1)$') }
                    "Source"       { $meta.Source      = $v }
                }
            }
        }
    }

    # 2. Inline patterns (only fill missing fields)
    $inline = @{
        'Journal'      = { param($v) $meta.JournalName = $v }
        'Publisher'    = { param($v) $meta.Publisher   = $v }
        'DOI'          = { param($v) $meta.Doi         = $v }
        'Year'         = { param($v) if ($meta.Year -eq 0 -and [int]::TryParse($v,[ref]$null)) { $meta.Year = [int]$v } }
        'Citations'    = { param($v) if ($meta.Citations -eq 0 -and [int]::TryParse($v.Replace(',',''),[ref]$null)) { $meta.Citations = [int]$v.Replace(',','') } }
        'Open Access'  = { param($v) $meta.IsOpenAccess = ($v -match '^(true|yes|1)$') }
        'In DOAJ'      = { param($v) $meta.IsInDoaj    = ($v -match '^(true|yes|1)$') }
        'Preprint'     = { param($v) $meta.IsPreprint  = ($v -match '^(true|yes|1)$') }
    }
    foreach ($kv in $inline.GetEnumerator()) {
        $pattern = '(?im)^\s*(?:\*\*)?' + [regex]::Escape($kv.Key) + '(?:\*\*)?\s*[:\-]\s*(.+?)\s*$'
        if ($content -match $pattern) {
            $v = $Matches[1].Trim().Trim('*').Trim()
            & $kv.Value $v
        }
    }

    return $meta
}

if (-not (Test-Path -LiteralPath $Folder)) {
    W "Folder not found: $Folder" "Red"
    exit 1
}

# ---------------------------------------------------------------------------
# STEP 0: Show extracted keywords so the user sees what the system is searching for
# ---------------------------------------------------------------------------
W "=============================================" "Cyan"
W " ResearchPilot FILTER-PAPERS (input-driven)" "Cyan"
W "=============================================" "Cyan"
W " Folder:   $Folder"
W " Pattern:  $Pattern"
W " Input:    $InputText"
if ($EnableQualityFilter) {
    W " Quality:  ENABLED (JOURNAL-QUALITY-FILTER)"
    if ($ShowPredatory) {
        W " Predatory: SHOWN (override active)"
    } else {
        W " Predatory: HIDDEN (default)"
    }
} else {
    W " Quality:  disabled (relevance only)"
}
W ""
W "[1/3] Extracted keywords from your input:" "Yellow"
W "------------------------------------------"

$Extraction = & $ExtractScript -InputText $InputText -Mode analyze -Project "DEFAULT"
$SearchTerms = @()
if ($Extraction.Primary) { foreach ($p in @($Extraction.Primary)) { $SearchTerms += $p.Term } }
if ($Extraction.Fallback) { foreach ($f in @($Extraction.Fallback)) { $SearchTerms += $f.Term } }

W " PRIMARY (AND-joined):" "Green"
$primary = @($Extraction.Primary | ForEach-Object { $_.Term })
if ($primary.Count -gt 0) {
    $primaryQuery = ($primary | ForEach-Object { '"' + $_ + '"' }) -join ' AND '
    W "   $primaryQuery" "White"
} else {
    W "   (none)" "DarkGray"
}
W ""
W " FALLBACK (OR-joined):" "Yellow"
$fallback = @($Extraction.Fallback | ForEach-Object { $_.Term })
if ($fallback.Count -gt 0) {
    $fallbackQuery = ($fallback | ForEach-Object { '"' + $_ + '"' }) -join ' OR '
    W "   $fallbackQuery" "White"
} else {
    W "   (none)" "DarkGray"
}
W ""
W " READY-TO-PASTE Scopus/WoS query (with no project exclusions):" "Cyan"
W "------------------------------------------"
$scopus = ""
if ($primary.Count -gt 0) {
    $scopus = "TITLE-ABS-KEY ( " + (($primary | ForEach-Object { '"' + $_ + '"' }) -join ' OR ') + " )"
} elseif ($fallback.Count -gt 0) {
    $scopus = "TITLE-ABS-KEY ( " + (($fallback | ForEach-Object { '"' + $_ + '"' }) -join ' OR ') + " )"
}
W "   $scopus" "White"
W "------------------------------------------"
W ""

# ---------------------------------------------------------------------------
# STEP 2: Loop through every paper in the folder
# ---------------------------------------------------------------------------
W "[2/3] Scoring papers against your input keywords..." "Yellow"
W ""

$Files = Get-ChildItem -LiteralPath $Folder -Filter $Pattern -File
$Total = $Files.Count
$i = 0

# Pre-collect search terms for fast access
$FlatSearchTerms = $SearchTerms | Where-Object { $_ -and $_.Trim() -ne "" } | Select-Object -Unique

$Results = @()
foreach ($f in $Files) {
    $i++
    W "  ($i/$Total) $($f.Name) ..." "DarkGray" -NoNewline
    $r = & $ScoreScript -InputText $InputText -FilePath $f.FullName

    $color = if ($r.Score -ge 15) {"Green"}
             elseif ($r.Score -ge 7) {"Yellow"}
             else {"Red"}
    W " score=$($r.Score) -> $($r.Decision)" $color

    if ($r.TrigramMatches -and $r.TrigramMatches.Count -gt 0) {
        W "      trigrams: $($r.TrigramMatches -join ' | ')" "DarkCyan"
    }
    if ($r.BigramMatches -and $r.BigramMatches.Count -gt 0 -and $r.BigramMatches.Count -le 5) {
        W "      bigrams:  $($r.BigramMatches -join ' | ')" "DarkGray"
    } elseif ($r.BigramMatches -and $r.BigramMatches.Count -gt 5) {
        $top5 = @($r.BigramMatches | Select-Object -First 5)
        W "      bigrams:  $($top5 -join ' | ') ... (+$($r.BigramMatches.Count - 5) more)" "DarkGray"
    }

    # Optional: journal quality check
    $Tier = 0
    $Badges = ""
    $Action = $r.Decision
    $QualityNote = ""
    if ($EnableQualityFilter) {
        $meta = Get-PaperMetadata -FilePath $f.FullName
        $q = Get-JournalQuality -JournalName $meta.JournalName `
                                -Publisher $meta.Publisher `
                                -Doi $meta.Doi `
                                -CitationCount $meta.Citations `
                                -Year $meta.Year `
                                -IsOpenAccess:$meta.IsOpenAccess `
                                -IsInDoaj:$meta.IsInDoaj `
                                -IsPreprint:$meta.IsPreprint `
                                -Source $meta.Source `
                                -RelevanceScore $r.Score `
                                -ExtraPredatoryPath $ExtraPredatoryPath `
                                -ShowPredatory:$ShowPredatory
        $Tier = $q.Tier
        $Badges = $q.Badges
        $Action = $q.Action

        $qColor = switch ($Tier) {
            1 { "Green" }
            2 { "Cyan" }
            3 { "Yellow" }
            4 { "Red" }
            default { "DarkGray" }
        }
        W "      [Tier $Tier] $($q.TierName) | badges: $Badges" $qColor
        W "      quartile=$($q.Quartile)  peer-reviewed=$($q.IsPeerReviewed)" $qColor
        W "      quality-score=$($q.QualityScore) final=$($q.FinalScore) action=$Action" $qColor

        # Combine: if quality says HIDE, override to REJECT even if relevance was ACCEPT
        if ($q.IsHidden) {
            $Action = "REJECT (predatory - hidden by filter)"
        }
        elseif ($Tier -eq 3 -and $r.Decision -like "ACCEPT*") {
            $Action = "REVIEW (ACCEPT-by-relevance, Tier 3 unverified journal - manual check needed)"
        }
    }

    $Results += [PSCustomObject]@{
        FileName       = $f.Name
        FilePath       = $f.FullName
        Score          = $r.Score
        Decision       = $r.Decision
        Tier           = $Tier
        Quartile       = if ($q) { $q.Quartile } else { "" }
        IsPeerReviewed = if ($q) { $q.IsPeerReviewed } else { "" }
        Badges         = $Badges
        Action         = $Action
        Matches        = (($r.TrigramMatches + $r.BigramMatches) | Select-Object -Unique) -join "; "
    }
}

# ---------------------------------------------------------------------------
# STEP 3: Summary + CSV
# ---------------------------------------------------------------------------
W ""
W "[3/3] SUMMARY" "Cyan"
W "=============================================" "Cyan"

# Use combined Action (relevance + quality) when -EnableQualityFilter is on
$FinalCol = if ($EnableQualityFilter) { "Action" } else { "Decision" }
$Accepted = @($Results | Where-Object { $_.$FinalCol -like "ACCEPT*" -or $_.$FinalCol -like "KEEP*" })
$Review   = @($Results | Where-Object { $_.$FinalCol -like "REVIEW*" })
$Rejected = @($Results | Where-Object { $_.$FinalCol -like "REJECT*" -or $_.$FinalCol -like "HIDE*" })

W " ACCEPT: $($Accepted.Count)" "Green"
$Accepted | ForEach-Object {
    $tierTxt = if ($_.Tier -gt 0) { " [Tier $($_.Tier)]" } else { "" }
    $qTxt    = if ($_.Quartile) { " [$($_.Quartile)]" } else { "" }
    $prTxt   = if ($_.IsPeerReviewed -eq $true) { " [peer-reviewed]" } elseif ($_.IsPeerReviewed -eq $false) { " [NOT peer-reviewed]" } else { "" }
    W "   + $($_.FileName) (score=$($_.Score)$tierTxt$qTxt$prTxt)" "Green"
}
W " REVIEW: $($Review.Count)" "Yellow"
$Review | ForEach-Object {
    $tierTxt = if ($_.Tier -gt 0) { " [Tier $($_.Tier)]" } else { "" }
    $qTxt    = if ($_.Quartile) { " [$($_.Quartile)]" } else { "" }
    $prTxt   = if ($_.IsPeerReviewed -eq $true) { " [peer-reviewed]" } elseif ($_.IsPeerReviewed -eq $false) { " [NOT peer-reviewed]" } else { "" }
    W "   ? $($_.FileName) (score=$($_.Score)$tierTxt$qTxt$prTxt)" "Yellow"
}
W " REJECT: $($Rejected.Count)" "Red"
$Rejected | ForEach-Object {
    $tierTxt = if ($_.Tier -gt 0) { " [Tier $($_.Tier)]" } else { "" }
    $qTxt    = if ($_.Quartile) { " [$($_.Quartile)]" } else { "" }
    $prTxt   = if ($_.IsPeerReviewed -eq $true) { " [peer-reviewed]" } elseif ($_.IsPeerReviewed -eq $false) { " [NOT peer-reviewed]" } else { "" }
    W "   - $($_.FileName) (score=$($_.Score)$tierTxt$qTxt$prTxt)" "Red"
}
W ""

# CSV log
if ($OutputCsv) {
    $Results | Export-Csv -LiteralPath $OutputCsv -NoTypeInformation -Encoding UTF8
    W " Logged to: $OutputCsv" "DarkGray"
}

# Optionally move rejects
if ($MoveRejects -and $Rejected.Count -gt 0) {
    if (-not $RejectFolder) { $RejectFolder = Join-Path $Folder "_rejected" }
    if (-not (Test-Path -LiteralPath $RejectFolder)) {
        New-Item -ItemType Directory -Path $RejectFolder -Force | Out-Null
    }
    foreach ($r in $Rejected) {
        $dest = Join-Path $RejectFolder $r.FileName
        Move-Item -LiteralPath $r.FilePath -Destination $dest -Force
        W "  Moved: $($r.FileName) -> _rejected" "Red"
    }
}

# Exit code
$acceptCount = $Accepted.Count
$rejectCount = $Rejected.Count
if ($acceptCount -gt 0) { exit 0 }
elseif ($rejectCount -eq $Total) { exit 1 }
else { exit 2 }
