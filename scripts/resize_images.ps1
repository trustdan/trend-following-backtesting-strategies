# PowerShell script to resize all images in the repository by 35% (to 65% of original size)

# Add System.Drawing assembly for image manipulation
Add-Type -AssemblyName System.Drawing

# Define image extensions to process
$imageExtensions = @('*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp')

# Get all image files recursively in the current directory (excluding ones already with _reduced)
$imageFiles = Get-ChildItem -Path . -Recurse -Include $imageExtensions -File | Where-Object { $_.Name -notmatch '_reduced\.' }

Write-Host "Found $($imageFiles.Count) image files to resize (excluding already reduced images)" -ForegroundColor Cyan

$processed = 0
$errors = 0

foreach ($file in $imageFiles) {
    try {
        Write-Host "Processing: $($file.FullName)" -ForegroundColor Yellow

        # Load the original image
        $originalImage = [System.Drawing.Image]::FromFile($file.FullName)

        # Calculate new dimensions (65% of original = 35% reduction)
        $newWidth = [int]($originalImage.Width * 0.65)
        $newHeight = [int]($originalImage.Height * 0.65)

        Write-Host "  Original: $($originalImage.Width)x$($originalImage.Height) -> New: ${newWidth}x${newHeight}" -ForegroundColor Gray

        # Capture the image format BEFORE disposing
        $imageFormat = $originalImage.RawFormat

        # Create new bitmap with new dimensions
        $newImage = New-Object System.Drawing.Bitmap $newWidth, $newHeight

        # Create graphics object for high-quality resizing
        $graphics = [System.Drawing.Graphics]::FromImage($newImage)
        $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

        # Draw the resized image
        $graphics.DrawImage($originalImage, 0, 0, $newWidth, $newHeight)

        # Clean up graphics object and original image
        $graphics.Dispose()
        $originalImage.Dispose()

        # Create new filename with _reduced suffix
        $nameWithoutExt = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
        $extension = $file.Extension
        $directory = $file.DirectoryName
        $newFileName = "${nameWithoutExt}_reduced${extension}"
        $outputPath = Join-Path $directory $newFileName

        # Save the resized image with the original format
        $newImage.Save($outputPath, $imageFormat)
        $newImage.Dispose()

        # Delete the original larger file
        Remove-Item $file.FullName -Force
        Write-Host "  Deleted original file" -ForegroundColor Gray

        $processed++
        Write-Host "  Successfully resized and saved as: $newFileName" -ForegroundColor Green

    } catch {
        $errors++
        Write-Host "  ERROR: $($_.Exception.Message)" -ForegroundColor Red

        # Clean up on error
        if ($originalImage) { $originalImage.Dispose() }
        if ($newImage) { $newImage.Dispose() }
        if ($graphics) { $graphics.Dispose() }
    }
}

Write-Host "`n=== Summary ===" -ForegroundColor Cyan
Write-Host "Processed: $processed images" -ForegroundColor Green
Write-Host "Errors: $errors images" -ForegroundColor $(if ($errors -gt 0) { 'Red' } else { 'Green' })
Write-Host "Complete!" -ForegroundColor Cyan
