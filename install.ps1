# ==============================================================================
# LM Studio Presets Installer (PowerShell)
# ==============================================================================

$ErrorActionPreference = "Stop"

$PresetsSource = Join-Path $PSScriptRoot "presets"
$TargetDir = Join-Path $HOME ".lmstudio\config-presets"

if (-not (Test-Path $PresetsSource)) {
    Write-Error "Presets folder not found at: $PresetsSource"
    exit 1
}

if (-not (Test-Path $TargetDir)) {
    Write-Host "Creating LM Studio presets directory: $TargetDir" -ForegroundColor Cyan
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
}

$presetFiles = Get-ChildItem -Path $PresetsSource -Filter "*.json"

Write-Host "`n📦 Installing LM Studio Presets to: $TargetDir" -ForegroundColor Green
Write-Host "--------------------------------------------------------"

foreach ($file in $presetFiles) {
    $dest = Join-Path $TargetDir $file.Name
    Copy-Item -Path $file.FullName -Destination $dest -Force
    Write-Host " ✔ Installed: $($file.Name)" -ForegroundColor White
}

Write-Host "--------------------------------------------------------"
Write-Host "✨ Successfully installed $($presetFiles.Count) presets!" -ForegroundColor Green
Write-Host "Restart or refresh LM Studio to see your new presets in the right sidebar.`n" -ForegroundColor Yellow
