# SEARCH-API.ps1
# ResearchPilot Parallel Multi-Source Paper Search
#
# Runs paper searches against multiple APIs IN PARALLEL using PowerShell Jobs
# (works on both Windows PowerShell 5.1 and PowerShell 7+), merges results,
# and dedupes by DOI first, then by title similarity.
#
# Pre-wired sources (free, no API key):
#   1. OpenAlex  (https://api.openalex.org)
#   2. Crossref  (https://api.crossref.org)
#   3. Semantic Scholar (https://api.semanticscholar.org)
#
# Rate limits (well-known, apply at IP level):
#   - OpenAlex:        ~10 req/sec, soft 100k/day; returns meta.count=0 when throttled
#   - Crossref:        polite pool ~50 req/sec with mailto: in User-Agent
#   - SemanticScholar: 100 req / 5 min unauthenticated (HTTP 429 on burst)
#
# The script gracefully handles a 0-count or 429 by returning an empty
# result set for that source. The other sources still come through.
#
# Usage:
#   pwsh SEARCH-API.ps1 -Query '"cybersecurity readiness" AND "higher education"' -MaxPerSource 25
#   pwsh SEARCH-API.ps1 -Query "..." -Sources OpenAlex,Crossref -YearFrom 2020 -YearTo 2025
#   pwsh SEARCH-API.ps1 -Query "..." -OutputJson "results.json"
#   pwsh SEARCH-API.ps1 -Query "..." -NoParallel     # sequential (for debugging)

param(
    [Parameter(Mandatory=$true)]
    [string]$Query,

    [Parameter(Mandatory=$false)]
    [int]$YearFrom = 0,

    [Parameter(Mandatory=$false)]
    [int]$YearTo = 0,

    [Parameter(Mandatory=$false)]
    [int]$MaxPerSource = 25,

    [Parameter(Mandatory=$false)]
    [string[]]$Sources = @("OpenAlex","Crossref","SemanticScholar"),

    [Parameter(Mandatory=$false)]
    [string]$OutputJson = "",

    [Parameter(Mandatory=$false)]
    [switch]$NoParallel,

    [Parameter(Mandatory=$false)]
    [int]$InterSourceDelayMs = 200
)

# Ensure TLS 1.2 is used (OpenAlex / Crossref require it; PS 5.1 default is TLS 1.0)
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# ---------------------------------------------------------------------------
# Source: OpenAlex (free, no key)
# Docs: https://docs.openalex.org/
# ---------------------------------------------------------------------------
function Search-OpenAlex {
    param([string]$Q, [int]$YFrom, [int]$YTo, [int]$Max)

    $url = "https://api.openalex.org/works?search=" + [uri]::EscapeDataString($Q) + "&per-page=$Max"
    if ($YFrom -gt 0) { $url += "&filter=publication_year:>$($YFrom-1)" }
    if ($YTo -gt 0)   { $url += ",publication_year:<$($YTo+1)" }

    try {
        $resp = Invoke-RestMethod -Uri $url -TimeoutSec 30 -Headers @{
            "User-Agent" = "ResearchPilot/1.0 (mailto:research@example.com)"
        }
        $results = @()
        foreach ($w in $resp.results) {
            $doi = $w.doi -replace '^https?://(dx\.)?doi\.org/', ''
            $results += [PSCustomObject]@{
                Title    = $w.title
                Authors  = ($w.authorships | ForEach-Object { $_.author.display_name }) -join ", "
                Journal  = if ($w.primary_location -and $w.primary_location.source) { $w.primary_location.source.display_name } else { "" }
                Year     = $w.publication_year
                DOI      = $doi
                Citations= $w.cited_by_count
                IsOA     = [bool]$w.open_access.is_oa
                IsInDoaj = [bool]$w.open_access.is_in_doaj
                Source   = "OpenAlex"
                URL      = $w.doi
            }
        }
        return ,$results
    } catch {
        Write-Warning "OpenAlex failed: $_"
        return ,@()
    }
}

# ---------------------------------------------------------------------------
# Source: Crossref (free, no key)
# Docs: https://api.crossref.org/swagger-ui/index.html
# ---------------------------------------------------------------------------
function Search-Crossref {
    param([string]$Q, [int]$YFrom, [int]$YTo, [int]$Max)

    $url = "https://api.crossref.org/works?query=" + [uri]::EscapeDataString($Q) + "&rows=$Max"
    if ($YFrom -gt 0 -or $YTo -gt 0) {
        $from = if ($YFrom -gt 0) { $YFrom } else { 0 }
        $to   = if ($YTo   -gt 0) { $YTo   } else { 9999 }
        $url += "&filter=from-pub-date:$from-01-01,until-pub-date:$to-12-31"
    }

    try {
        $resp = Invoke-RestMethod -Uri $url -TimeoutSec 30 -Headers @{
            "User-Agent" = "ResearchPilot/1.0 (mailto:research@example.com)"
        }
        $results = @()
        foreach ($item in $resp.message.items) {
            $doi = $item.DOI
            $results += [PSCustomObject]@{
                Title    = ($item.title | Select-Object -First 1)
                Authors  = (($item.author | ForEach-Object { "$($_.given) $($_.family)" }) -join ", ")
                Journal  = ($item."container-title" | Select-Object -First 1)
                Year     = [int]($item.issued."date-parts"[0][0])
                DOI      = $doi
                Citations= $item."is-referenced-by-count"
                IsOA     = $false
                IsInDoaj = $false
                Source   = "Crossref"
                URL      = "https://doi.org/$doi"
            }
        }
        return ,$results
    } catch {
        Write-Warning "Crossref failed: $_"
        return ,@()
    }
}

# ---------------------------------------------------------------------------
# Source: Semantic Scholar (free, no key for basic use)
# Docs: https://api.semanticscholar.org/graph/v1
# ---------------------------------------------------------------------------
function Search-SemanticScholar {
    param([string]$Q, [int]$YFrom, [int]$YTo, [int]$Max)

    $url = "https://api.semanticscholar.org/graph/v1/paper/search?query=" + [uri]::EscapeDataString($Q) +
           "&limit=$Max&fields=title,authors,year,journal,citationCount,externalIds,isOpenAccess,publicationVenue"

    if ($YFrom -gt 0 -or $YTo -gt 0) {
        $from = if ($YFrom -gt 0) { $YFrom } else { 0 }
        $to   = if ($YTo   -gt 0) { $YTo   } else { 9999 }
        $url += "&year=$from-$to"
    }

    try {
        $resp = Invoke-RestMethod -Uri $url -TimeoutSec 30
        $results = @()
        foreach ($p in $resp.data) {
            $doi = $p.externalIds.DOI
            $journalName = if ($p.publicationVenue) { $p.publicationVenue.name } elseif ($p.journal) { $p.journal.name } else { "" }
            $results += [PSCustomObject]@{
                Title    = $p.title
                Authors  = ($p.authors | ForEach-Object { $_.name }) -join ", "
                Journal  = $journalName
                Year     = $p.year
                DOI      = $doi
                Citations= $p.citationCount
                IsOA     = [bool]$p.isOpenAccess
                IsInDoaj = $false
                Source   = "SemanticScholar"
                URL      = "https://www.semanticscholar.org/paper/$($p.paperId)"
            }
        }
        return ,$results
    } catch {
        Write-Warning "SemanticScholar failed: $_"
        return ,@()
    }
}

# ---------------------------------------------------------------------------
# Dedupe by DOI first, then by title similarity
# ---------------------------------------------------------------------------
function Get-TitleSimilarity {
    param([string]$A, [string]$B)
    if ([string]::IsNullOrWhiteSpace($A) -or [string]::IsNullOrWhiteSpace($B)) { return 0 }
    $a = ($A.ToLower() -replace '[^\w\s]',' ') -split '\s+' | Where-Object { $_.Length -gt 2 } | Select-Object -Unique
    $b = ($B.ToLower() -replace '[^\w\s]',' ') -split '\s+' | Where-Object { $_.Length -gt 2 } | Select-Object -Unique
    $intersect = @($a | Where-Object { $b -contains $_ }).Count
    $union     = @($a + $b | Select-Object -Unique).Count
    if ($union -eq 0) { return 0 }
    return $intersect / $union
}

function Dedupe-Papers {
    param([array]$Papers)

    $byDoi = @{}
    $noDoi = @()
    foreach ($p in $Papers) {
        $d = ($p.DOI -as [string]).Trim().ToLower()
        if (-not [string]::IsNullOrWhiteSpace($d) -and $d -ne "null") {
            if ($byDoi.ContainsKey($d)) {
                if ($p.Citations -gt $byDoi[$d].Citations) { $byDoi[$d] = $p }
            } else {
                $byDoi[$d] = $p
            }
        } else {
            $noDoi += $p
        }
    }

    $deduped = @($byDoi.Values)
    foreach ($p in $noDoi) {
        $isDup = $false
        foreach ($d in $deduped) {
            $sim = Get-TitleSimilarity -A $p.Title -B $d.Title
            if ($sim -ge 0.85) {
                $isDup = $true
                if ($p.Citations -gt $d.Citations) {
                    $idx = $deduped.IndexOf($d)
                    $deduped[$idx] = $p
                }
                break
            }
        }
        if (-not $isDup) { $deduped += $p }
    }
    return ,$deduped
}

# ---------------------------------------------------------------------------
# Main: dispatch all sources in parallel, then merge + dedupe
# ---------------------------------------------------------------------------
Write-Host "[1/3] Dispatching $($Sources.Count) sources..." -ForegroundColor Cyan
$sw = [System.Diagnostics.Stopwatch]::StartNew()

$AllPapers = @()
if ($NoParallel) {
    # Sequential (for debugging)
    $first = $true
    foreach ($src in $Sources) {
        if (-not $first -and $InterSourceDelayMs -gt 0) {
            Start-Sleep -Milliseconds $InterSourceDelayMs
        }
        $first = $false
        $r = switch ($src) {
            "OpenAlex"        { Search-OpenAlex        -Q $Query -YFrom $YearFrom -YTo $YearTo -Max $MaxPerSource }
            "Crossref"        { Search-Crossref        -Q $Query -YFrom $YearFrom -YTo $YearTo -Max $MaxPerSource }
            "SemanticScholar" { Search-SemanticScholar -Q $Query -YFrom $YearFrom -YTo $YearTo -Max $MaxPerSource }
            default           { @() }
        }
        $AllPapers += $r
        Write-Host "  $src : $($r.Count) papers" -ForegroundColor DarkGray
    }
} else {
    # Parallel via Start-Job (works on PowerShell 5.1 and 7+)
    # Each job gets its own API call. We Wait-Job at the end.
    $Jobs = @()
    foreach ($src in $Sources) {
        $Jobs += Start-Job -ScriptBlock {
            param($src, $Q, $YF, $YT, $Max)
            # Set TLS12 inside the job (Start-Job creates a fresh session)
            [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
            $ua = "ResearchPilot/1.0 (mailto:research@example.com)"
            $results = @()
            switch ($src) {
                "OpenAlex" {
                    $url = "https://api.openalex.org/works?search=" + [uri]::EscapeDataString($Q) + "&per-page=$Max"
                    if ($YF -gt 0) { $url += "&filter=publication_year:>$($YF-1)" }
                    if ($YT -gt 0)   { $url += ",publication_year:<$($YT+1)" }
                    try {
                        $resp = Invoke-RestMethod -Uri $url -TimeoutSec 30 -Headers @{"User-Agent"=$ua}
                        foreach ($w in $resp.results) {
                            $doi = $w.doi -replace '^https?://(dx\.)?doi\.org/', ''
                            $results += [PSCustomObject]@{
                                Title    = $w.title
                                Authors  = ($w.authorships | ForEach-Object { $_.author.display_name }) -join ", "
                                Journal  = if ($w.primary_location -and $w.primary_location.source) { $w.primary_location.source.display_name } else { "" }
                                Year     = $w.publication_year
                                DOI      = $doi
                                Citations= $w.cited_by_count
                                IsOA     = [bool]$w.open_access.is_oa
                                IsInDoaj = [bool]$w.open_access.is_in_doaj
                                Source   = "OpenAlex"
                                URL      = $w.doi
                            }
                        }
                    } catch { Write-Warning "OpenAlex failed: $_" }
                }
                "Crossref" {
                    $url = "https://api.crossref.org/works?query=" + [uri]::EscapeDataString($Q) + "&rows=$Max"
                    if ($YF -gt 0 -or $YT -gt 0) {
                        $from = if ($YF -gt 0) { $YF } else { 0 }
                        $to   = if ($YT -gt 0) { $YT } else { 9999 }
                        $url += "&filter=from-pub-date:$from-01-01,until-pub-date:$to-12-31"
                    }
                    try {
                        $resp = Invoke-RestMethod -Uri $url -TimeoutSec 30 -Headers @{"User-Agent"=$ua}
                        foreach ($w in $resp.results) {
                            $doi = $w.doi -replace '^https?://(dx\.)?doi\.org/', ''
                            $results += [PSCustomObject]@{
                                Title    = $w.title
                                Authors  = ($w.authorships | ForEach-Object { $_.author.display_name }) -join ", "
                                Journal  = if ($w.primary_location -and $w.primary_location.source) { $w.primary_location.source.display_name } else { "" }
                                Year     = $w.publication_year
                                DOI      = $doi
                                Citations= $w.cited_by_count
                                IsOA     = [bool]$w.open_access.is_oa
                                IsInDoaj = [bool]$w.open_access.is_in_doaj
                                Source   = "OpenAlex"
                                URL      = $w.doi
                            }
                        }
                    } catch { Write-Warning "OpenAlex failed: $_" }
                }
                "Crossref" {
                    $url = "https://api.crossref.org/works?query=" + [uri]::EscapeDataString($Q) + "&rows=$Max"
                    if ($YF -gt 0 -or $YT -gt 0) {
                        $from = if ($YF -gt 0) { $YF } else { 0 }
                        $to   = if ($YT -gt 0) { $YT } else { 9999 }
                        $url += "&filter=from-pub-date:$from-01-01,until-pub-date:$to-12-31"
                    }
                    try {
                        $resp = Invoke-RestMethod -Uri $url -TimeoutSec 30 -Headers @{"User-Agent"="ResearchPilot/1.0"}
                        foreach ($item in $resp.message.items) {
                            $results += [PSCustomObject]@{
                                Title    = ($item.title | Select-Object -First 1)
                                Authors  = (($item.author | ForEach-Object { "$($_.given) $($_.family)" }) -join ", ")
                                Journal  = ($item."container-title" | Select-Object -First 1)
                                Year     = [int]($item.issued."date-parts"[0][0])
                                DOI      = $item.DOI
                                Citations= $item."is-referenced-by-count"
                                IsOA     = $false
                                IsInDoaj = $false
                                Source   = "Crossref"
                                URL      = "https://doi.org/$($item.DOI)"
                            }
                        }
                    } catch { Write-Warning "Crossref failed: $_" }
                }
                "SemanticScholar" {
                    $url = "https://api.semanticscholar.org/graph/v1/paper/search?query=" + [uri]::EscapeDataString($Q) +
                           "&limit=$Max&fields=title,authors,year,journal,citationCount,externalIds,isOpenAccess,publicationVenue"
                    if ($YF -gt 0 -or $YT -gt 0) {
                        $from = if ($YF -gt 0) { $YF } else { 0 }
                        $to   = if ($YT -gt 0) { $YT } else { 9999 }
                        $url += "&year=$from-$to"
                    }
                    try {
                        $resp = Invoke-RestMethod -Uri $url -TimeoutSec 30
                        foreach ($p in $resp.data) {
                            $doi = $p.externalIds.DOI
                            $journalName = if ($p.publicationVenue) { $p.publicationVenue.name } elseif ($p.journal) { $p.journal.name } else { "" }
                            $results += [PSCustomObject]@{
                                Title    = $p.title
                                Authors  = ($p.authors | ForEach-Object { $_.name }) -join ", "
                                Journal  = $journalName
                                Year     = $p.year
                                DOI      = $doi
                                Citations= $p.citationCount
                                IsOA     = [bool]$p.isOpenAccess
                                IsInDoaj = $false
                                Source   = "SemanticScholar"
                                URL      = "https://www.semanticscholar.org/paper/$($p.paperId)"
                            }
                        }
                    } catch { Write-Warning "SemanticScholar failed: $_" }
                }
            }
            return @{ Source = $src; Papers = $results }
        } -ArgumentList $src, $Query, $YearFrom, $YearTo, $MaxPerSource
    }

    # Wait for all jobs in parallel
    $AllPapers = Wait-Job -Job $Jobs | ForEach-Object {
        $r = Receive-Job -Job $_
        Write-Host "  $($r.Source) : $($r.Papers.Count) papers" -ForegroundColor DarkGray
        $r.Papers
    }
    Remove-Job -Job $Jobs -Force
}
$sw.Stop()
Write-Host "  Total time: $($sw.ElapsedMilliseconds) ms" -ForegroundColor DarkCyan

# ---------------------------------------------------------------------------
# Dedupe
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "[2/3] Dedupe by DOI first, then title similarity..." -ForegroundColor Cyan
$RawCount = $AllPapers.Count
$DedupedPapers = Dedupe-Papers -Papers $AllPapers
Write-Host "  Raw: $RawCount -> Unique: $($DedupedPapers.Count)" -ForegroundColor Green

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "[3/3] RESULTS (top 20):" -ForegroundColor Cyan
$DedupedPapers | Select-Object -First 20 |
    Format-Table Title, Journal, Year, DOI, Citations, Source -AutoSize

if ($OutputJson) {
    $DedupedPapers | ConvertTo-Json -Depth 5 | Out-File -LiteralPath $OutputJson -Encoding UTF8
    Write-Host ""
    Write-Host "Saved $($DedupedPapers.Count) papers to: $OutputJson" -ForegroundColor Cyan
}

# Return the deduped list
return ,$DedupedPapers
