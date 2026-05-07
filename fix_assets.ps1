# CVK Assets Fixer
# This script copies the generated images from the internal brain directory to the assets folder.

$sourceDir = "C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c"
$destDir = "$PSScriptRoot\assets"

if (-not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir
}

$filesToCopy = @{
    "cvk_logo_1778012047100.png" = "logo.png"
    "chris_portrait_1778012017308.png" = "chris-profile.png"
    "hero_fallback_1778012032882.png" = "hero-fallback.png"
}

foreach ($src in $filesToCopy.Keys) {
    $srcPath = Join-Path $sourceDir $src
    $destPath = Join-Path $destDir $filesToCopy[$src]
    
    if (Test-Path $srcPath) {
        Write-Host "Copying $src to $($filesToCopy[$src])..."
        Copy-Item -Path $srcPath -Destination $destPath -Force
    } else {
        Write-Warning "Source file not found: $srcPath"
    }
}

Write-Host "Assets sync complete! Refresh your browser."
