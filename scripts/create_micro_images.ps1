# Create micro versions of all _reduced.png images for rapid bug scanning
# Keeps original _reduced.png files, creates new _micro.png files at 50% size

Write-Host "Creating micro versions of all reduced images..." -ForegroundColor Cyan

# Counter for progress
$processedCount = 0
$errorCount = 0

# Find all _reduced.png files recursively
$reducedImages = Get-ChildItem -Path "sectors" -Filter "*_reduced.png" -Recurse

Write-Host "Found $($reducedImages.Count) reduced images to process" -ForegroundColor Yellow

foreach ($image in $reducedImages) {
    try {
        # Get the full path and create the micro filename
        $reducedPath = $image.FullName
        $microPath = $reducedPath -replace "_reduced\.png$", "_micro.png"

        # Skip if micro version already exists
        if (Test-Path $microPath) {
            Write-Host "  Skipping (exists): $($image.Name)" -ForegroundColor Gray
            continue
        }

        # Load the reduced image
        Add-Type -AssemblyName System.Drawing
        $reducedImg = [System.Drawing.Image]::FromFile($reducedPath)

        # Calculate new dimensions (65% of reduced size - sweet spot for readability)
        $newWidth = [int]($reducedImg.Width * 0.65)
        $newHeight = [int]($reducedImg.Height * 0.65)

        # Create the micro image
        $microImg = New-Object System.Drawing.Bitmap($newWidth, $newHeight)
        $graphics = [System.Drawing.Graphics]::FromImage($microImg)

        # Set high quality rendering
        $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

        # Draw the resized image
        $graphics.DrawImage($reducedImg, 0, 0, $newWidth, $newHeight)

        # Save the micro image
        $microImg.Save($microPath, [System.Drawing.Imaging.ImageFormat]::Png)

        # Clean up
        $graphics.Dispose()
        $microImg.Dispose()
        $reducedImg.Dispose()

        $processedCount++
        Write-Host "  Created: $($image.DirectoryName | Split-Path -Leaf)/$($image.Name -replace '_reduced', '_micro')" -ForegroundColor Green

    } catch {
        $errorCount++
        Write-Host "  ERROR processing $($image.Name): $_" -ForegroundColor Red
    }
}

Write-Host "`nProcessing complete!" -ForegroundColor Cyan
Write-Host "  Successfully created: $processedCount micro images" -ForegroundColor Green
if ($errorCount -gt 0) {
    Write-Host "  Errors encountered: $errorCount" -ForegroundColor Red
}

# List all micro images by strategy for easy review
Write-Host "`nMicro images created by strategy:" -ForegroundColor Yellow
Get-ChildItem -Path "sectors" -Filter "*_micro.png" -Recurse |
    Group-Object { ($_.Name -split '-')[0] } |
    Sort-Object Name |
    ForEach-Object {
        Write-Host "  $($_.Name): $($_.Count) images" -ForegroundColor Cyan
    }

Write-Host "`nTo quickly review all micro images, open this directory in an image viewer:" -ForegroundColor Yellow
Write-Host "  sectors\" -ForegroundColor White
Write-Host "`nLook for images where left and right numbers diverge significantly (potential bugs)" -ForegroundColor Magenta
