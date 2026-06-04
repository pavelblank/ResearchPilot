# JOURNAL-QUALITY-FILTER.ps1
# Post-results journal quality filter.
# Inputs: paper metadata (journal name, publisher, DOI, citation count, year, isOA, isInDoaj, isPreprint, source).
# Reads: JOURNAL-TIERS.json + 00-SYSTEM-CORE/predatory_journals.json
# Outputs: tier, badges, quality score, final recommendation.
# Usage:
#   . .\JOURNAL-QUALITY-FILTER.ps1
#   $r = Get-JournalQuality -JournalName "..." -Publisher "..." -CitationCount 0 ...

function Get-JournalQuality {
    param(
        [string]$JournalName      = "",
        [string]$Publisher        = "",
        [string]$Doi              = "",
        [int]$CitationCount       = 0,
        [int]$Year                = 0,
        [bool]$IsOpenAccess       = $false,
        [bool]$IsInDoaj           = $false,
        [bool]$IsPreprint         = $false,
        [string]$Source           = "",
        [int]$RelevanceScore      = 0,
        [string]$PredatoryListPath = "",
        [string]$ExtraPredatoryPath = "",
        [switch]$ShowPredatory   # Toggle: by default Tier 4 (predatory) is HIDDEN; pass this to show with a red badge
    )

    # --- 0. Paths ---
    $ScriptDir  = $PSScriptRoot
    $TiersPath  = Join-Path $ScriptDir "JOURNAL-TIERS.json"
    $QuartilesPath = Join-Path $ScriptDir "JOURNAL-QUARTILES.json"
    if (-not $PredatoryListPath) {
        $PredatoryListPath = Join-Path $ScriptDir "..\predatory_journals.json"
    }

    if (-not (Test-Path $TiersPath)) {
        throw "JOURNAL-TIERS.json not found at $TiersPath"
    }
    $Tiers = Get-Content $TiersPath -Raw | ConvertFrom-Json
    $Quartiles = if (Test-Path $QuartilesPath) { Get-Content $QuartilesPath -Raw | ConvertFrom-Json } else { $null }

    # Load predatory list (flat array of journal names, lowercased).
    # - PredatoryListPath: built-in Beall's list (always loaded)
    # - ExtraPredatoryPath: user-supplied extra list (optional)
    $PredatoryNames = @()
    if (Test-Path $PredatoryListPath) {
        $Raw = Get-Content $PredatoryListPath -Raw | ConvertFrom-Json
        if ($Raw -isnot [System.Array]) { $Raw = @($Raw) }
        $PredatoryNames += $Raw | ForEach-Object { $_.ToString().ToLower().Trim() }
    }
    if ($ExtraPredatoryPath -and (Test-Path $ExtraPredatoryPath)) {
        $Raw2 = Get-Content $ExtraPredatoryPath -Raw | ConvertFrom-Json
        if ($Raw2 -isnot [System.Array]) { $Raw2 = @($Raw2) }
        $PredatoryNames += $Raw2 | ForEach-Object { $_.ToString().ToLower().Trim() }
    }
    $PredatoryNames = $PredatoryNames | Where-Object { $_ } | Select-Object -Unique

    # --- 1. Helpers ---
    function _CitationBonus([int]$c) {
        $s = $Tiers.quality_scoring.citation_bonus
        if ($c -eq 0)       { return [int]$s.'0' }
        elseif ($c -le 10)  { return [int]$s.'1-10' }
        elseif ($c -le 50)  { return [int]$s.'11-50' }
        elseif ($c -le 200) { return [int]$s.'51-200' }
        elseif ($c -le 500) { return [int]$s.'201-500' }
        else                { return [int]$s.'500+' }
    }

    function _RecencyBonus([int]$y) {
        if ($y -eq 0) { return 0 }
        $currentYear = (Get-Date).Year
        $age = $currentYear - $y
        $s = $Tiers.quality_scoring.recency_bonus
        if ($age -le 2)  { return [int]$s.last_2_years }
        elseif ($age -le 5)  { return [int]$s.last_5_years }
        elseif ($age -le 10) { return [int]$s.'6_to_10_years_ago' }
        else                   { return [int]$s.'11_plus_years_ago' }
    }

    # --- 2. Tier classification ---
    $Tier    = 3
    $Reasons = @()
    $Badges  = @()

    # 2a. Preprint check
    if ($IsPreprint) {
        $Tier = 3
        $Badges += "Preprint"
        $Reasons += "Preprint server detected (arXiv, SSRN, etc.)"
    }
    elseif ($Source -match "arxiv\.org|ssrn\.com|biorxiv\.org|medrxiv\.org|researchsquare\.net|preprints\.org") {
        $Tier = 3
        $Badges += "Preprint"
        $Reasons += "Source URL matches a known preprint server"
    }

    # 2b. Predatory blocklist (substring match)
    $JournalLower = $JournalName.ToLower().Trim()
    $MatchedPredatory = $null
    if ($PredatoryNames.Count -gt 0) {
        $MatchedPredatory = $PredatoryNames | Where-Object { $JournalLower -like "*$_*" } | Select-Object -First 1
    }
    if ($MatchedPredatory) {
        $Tier = 4
        $Badges += "Flagged: Possible Predatory"
        $Reasons += "Journal name matches Beall's List entry: '$MatchedPredatory'"
    }
    else {
        # 2c. Tier 1: trusted publisher
        $Tier1Hit = $Tiers.tiers.tier_1_trusted.publisher_patterns | Where-Object {
            $Publisher -like "*$_*" -or $JournalLower -like "*$($_.ToLower())*"
        } | Select-Object -First 1
        if ($Tier1Hit) {
            $Tier = 1
            $Badges += "Scopus / WoS Indexed"
            $Reasons += "Trusted publisher: $Tier1Hit"
        }
    }

    # 2d. Tier 2: DOAJ (only if not Tier 1 or 4)
    if ($Tier -eq 3) {
        if ($IsInDoaj) {
            $Tier = 2
            $Badges += "DOAJ Open Access"
            $Reasons += "OpenAlex is_in_doaj = true"
        }
        elseif ($Source -match "doaj\.org") {
            $Tier = 2
            $Badges += "DOAJ Open Access"
            $Reasons += "Source is DOAJ"
        }
    }

    # 2e. Tier 3 amber warning
    if ($Tier -eq 3 -and ($Badges -notcontains "Preprint")) {
        $WarningHit = $Tiers.tiers.tier_4_predatory.warning_patterns | Where-Object {
            $JournalLower -like "*$($_.ToLower())*"
        } | Select-Object -First 1
        if ($WarningHit) {
            $Badges += "Unverified Journal"
            $Reasons += "Warning pattern: '$WarningHit' (Beall's List category)"
        }
        elseif ($Badges.Count -eq 0) {
            $Badges += "Unverified Journal"
            $Reasons += "No trusted publisher or DOAJ match; journal could not be tier-1/2 confirmed"
        }
    }

    # 2f. OA badge (independent of tier)
    if ($IsOpenAccess -and ($Badges -notcontains "DOAJ Open Access")) {
        $Badges += "Open Access PDF"
    }

    # 2g. Quartile (Q1-Q4) detection from JOURNAL-QUARTILES.json.
    # Word-boundary match: 'science' matches 'Science' but not 'Computer Science'.
    $Quartile = $null
    $QMatch = ""
    if ($Quartiles) {
        function _MatchQuartile($list) {
            foreach ($needle in $list) {
                $p = '(^|\b)' + [regex]::Escape($needle) + '(\b|$)'
                if ([bool]([regex]::IsMatch($JournalLower, $p, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase))) {
                    return $needle
                }
            }
            return $null
        }
        $q1 = _MatchQuartile @($Quartiles.q1_journals)
        $q2 = _MatchQuartile @($Quartiles.q2_journals)
        $q3 = _MatchQuartile @($Quartiles.q3_journals)
        $q4 = _MatchQuartile @($Quartiles.q4_journals)
        # Priority: Q1 > Q2 > Q3 > Q4
        if ($q1)      { $Quartile = "Q1"; $QMatch = $q1 }
        elseif ($q2)  { $Quartile = "Q2"; $QMatch = $q2 }
        elseif ($q3)  { $Quartile = "Q3"; $QMatch = $q3 }
        elseif ($q4)  { $Quartile = "Q4"; $QMatch = $q4 }
        if ($Quartile) {
            $Badges += "Quartile $Quartile"
            $Reasons += "JCR/Scopus quartile: $Quartile (matched: '$QMatch')"
        }
    }

    # 2h. Peer-review detection.
    # Word-boundary match: 'review of' matches 'Annual Review of...' but not 'Peer Review of Studies'.
    $IsPeerReviewed = $null
    $PrMatch = ""
    if ($Quartiles -and $Quartiles.peer_review_indicators) {
        $noSignals = @()
        foreach ($sig in @($Quartiles.peer_review_indicators.no_signals)) {
            $p = '(^|\b)' + [regex]::Escape($sig) + '(\b|$)'
            $matched = [bool]([regex]::IsMatch($JournalLower, $p, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase))
            if (-not $matched -and $Source) {
                $matched = [bool]([regex]::IsMatch($Source.ToLower(), $p, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase))
            }
            if ($matched) { $noSignals += $sig; break }
        }
        $yesSignals = @()
        foreach ($sig in @($Quartiles.peer_review_indicators.yes_signals)) {
            $p = '(^|\b)' + [regex]::Escape($sig) + '(\b|$)'
            if ([bool]([regex]::IsMatch($JournalLower, $p, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase))) {
                $yesSignals += $sig; break
            }
        }
        $noSig = if ($noSignals.Count -gt 0) { $noSignals[0] } else { "" }
        $yesSig = if ($yesSignals.Count -gt 0) { $yesSignals[0] } else { "" }
        if ($noSig) {
            $IsPeerReviewed = $false
            $PrMatch = $noSig
        }
        elseif ($yesSig -and ($Tier -eq 1 -or $Tier -eq 2)) {
            $IsPeerReviewed = $true
            $PrMatch = $yesSig
        }
        elseif ($Tier -eq 1 -or $Tier -eq 2) {
            $IsPeerReviewed = $true
            $PrMatch = "tier 1/2 trusted journal"
        }
        elseif ($IsPreprint) {
            $IsPeerReviewed = $false
            $PrMatch = "preprint server"
        }
    }
    if ($IsPeerReviewed -eq $true)  { $Badges += "Peer-reviewed"; $Reasons += "Peer-review: yes ($PrMatch)" }
    elseif ($IsPeerReviewed -eq $false) { $Badges += "Not peer-reviewed"; $Reasons += "Peer-review: no ($PrMatch)" }

    # --- 3. Quality score ---
    $CitationBonus = _CitationBonus $CitationCount
    $TierBonus     = switch ($Tier) {
        1 { [int]$Tiers.quality_scoring.tier_bonus.tier_1 }
        2 { [int]$Tiers.quality_scoring.tier_bonus.tier_2 }
        3 { [int]$Tiers.quality_scoring.tier_bonus.tier_3 }
        4 { [int]$Tiers.quality_scoring.tier_bonus.tier_4 }
        default { 0 }
    }
    $OaBonus      = if ($IsOpenAccess) { [int]$Tiers.quality_scoring.open_access_bonus } else { 0 }
    $RecencyBonus = _RecencyBonus $Year

    # Q-rank bonus (Q1 boosts, Q4 neutral, unknown = 0)
    $QuartileBonus = 0
    if ($Quartile -and $Quartiles -and $Quartiles.quartile_bonus) {
        $qb = $Quartiles.quartile_bonus.$Quartile
        if ($qb -ne $null) { $QuartileBonus = [int]$qb }
    }
    # Peer-review bonus
    $PeerReviewBonus = 0
    if ($Quartiles -and $Quartiles.peer_review_bonus) {
        $key = if ($IsPeerReviewed -eq $true) { "yes" } elseif ($IsPeerReviewed -eq $false) { "no" } else { "unknown" }
        $prb = $Quartiles.peer_review_bonus.$key
        if ($prb -ne $null) { $PeerReviewBonus = [int]$prb }
    }

    $QualityScore = $CitationBonus + $TierBonus + $OaBonus + $RecencyBonus + $QuartileBonus + $PeerReviewBonus

    # --- 4. Final action ---
    $FinalScore = $RelevanceScore + $QualityScore
    $TierName = switch ($Tier) {
        1 { "Tier 1: Trusted" }
        2 { "Tier 2: DOAJ/OA" }
        3 { "Tier 3: Unverified" }
        4 { "Tier 4: Predatory" }
        default { "Unknown" }
    }
    $Action = switch ($Tier) {
        1 { "KEEP (Tier 1, high quality)" }
        2 { "KEEP (Tier 2, DOAJ / open access)" }
        3 { "REVIEW (Tier 3, unverified journal)" }
        4 {
            if ($ShowPredatory) {
                "SHOW-WITH-WARNING (Tier 4, predatory) - user override active"
            } else {
                "HIDE (Tier 4, flagged as predatory) - pass -ShowPredatory to override"
            }
        }
        default { "REVIEW" }
    }

    # --- 5. Output ---
    return [PSCustomObject]@{
        JournalName    = $JournalName
        Publisher      = $Publisher
        Year           = $Year
        Citations      = $CitationCount
        Tier           = $Tier
        TierName       = $TierName
        Quartile       = if ($Quartile) { $Quartile } else { "" }
        IsPeerReviewed = $IsPeerReviewed
        Badges         = ($Badges -join " | ")
        BadgeList      = $Badges -join ","
        QualityScore   = $QualityScore
        RelevanceScore = $RelevanceScore
        FinalScore     = $FinalScore
        Action         = $Action
        IsHidden       = ($Tier -eq 4 -and -not $ShowPredatory)
        ShowPredatory  = [bool]$ShowPredatory
        Reasons        = ($Reasons -join " | ")
    }
}
