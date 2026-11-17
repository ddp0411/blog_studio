# Blog Studio setup for Windows (PowerShell). Safe to run more than once.
#   powershell -ExecutionPolicy Bypass -File .\setup.ps1
#   powershell -ExecutionPolicy Bypass -File .\setup.ps1 -NoGlobal
param([switch]$NoGlobal)
$ErrorActionPreference = "Stop"

$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$ClaudeHome = Join-Path $HOME ".claude"
Write-Host "Blog Studio: $Here"

foreach ($tool in "python", "claude", "git") {
  if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) { Write-Host "WARN: $tool not found on PATH" }
}

if (-not $NoGlobal) {
  New-Item -ItemType Directory -Force -Path (Join-Path $ClaudeHome "skills") | Out-Null

  # Global CLAUDE.md block, replaced between markers
  $GFile = Join-Path $ClaudeHome "CLAUDE.md"
  if (-not (Test-Path $GFile)) { New-Item -ItemType File -Path $GFile | Out-Null }
  $g = Get-Content $GFile -Raw -Encoding UTF8
  if ($null -eq $g) { $g = "" }
  $block = (Get-Content (Join-Path $Here "global\CLAUDE.global.md") -Raw -Encoding UTF8).Trim()
  $block = $block.Replace("work inside my blog-studio folder", "work inside my blog-studio folder ($Here)")
  $pattern = "(?s)<!-- BLOG-STUDIO:START.*?BLOG-STUDIO:END -->"
  if ($g -match $pattern) {
    $g = [regex]::Replace($g, $pattern, [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $block })
    Write-Host "Global CLAUDE.md: block updated"
  } else {
    if ($g.Trim().Length -gt 0) { $g = $g.TrimEnd() + "`r`n`r`n" }
    $g = $g + $block + "`r`n"
    Write-Host "Global CLAUDE.md: block added"
  }
  [System.IO.File]::WriteAllText($GFile, $g, (New-Object System.Text.UTF8Encoding $false))

  # Humanizer as a personal skill
  $Dest = Join-Path $ClaudeHome "skills\humanizer"
  if (Test-Path $Dest) { Remove-Item -Recurse -Force $Dest }
  Copy-Item -Recurse (Join-Path $Here ".claude\skills\humanizer") $Dest
  Write-Host "Humanizer skill: installed to $Dest"
}

if ((Get-Command git -ErrorAction SilentlyContinue) -and -not (Test-Path (Join-Path $Here ".git"))) {
  git -C $Here init -q
  Write-Host "Git: initialized. Push to a PRIVATE repo:"
  Write-Host "  git add -A; git commit -m 'Blog studio setup'; gh repo create blog-studio --private --source=. --push"
}

Write-Host ""
Write-Host "Done. Next:"
Write-Host "  1. Add 2-4 of your own paragraphs to voice\samples\"
Write-Host "  2. cd `"$Here`"; claude"
Write-Host "  3. Try: /blog-draft new my-first-post"
Write-Host "Note: on Windows the lint command is: python scripts\ai_tells.py <file>"
