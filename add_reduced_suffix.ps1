# PowerShell script to add _reduced suffix to all image files

# Define image extensions to process
$imageExtensions = @('*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp')

# Get all image files recursively in the current directory (excluding ones already with _reduced)
$imageFiles = Get-ChildItem -Path . -Recurse -Include $imageExtensions -File | Where-Object { $_.Name -notmatch '_reduced\.' }

Write-Host "Found $($imageFiles.Count) image files to rename" -ForegroundColor Cyan

$renamed = 0

foreach ($file in $imageFiles) {
    try {
        # Get the file name without extension and the extension
        $nameWithoutExt = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
        $extension = $file.Extension
        $directory = $file.DirectoryName

        # Create new name with _reduced suffix
        $newName = "${nameWithoutExt}_reduced${extension}"
        $newPath = Join-Path $directory $newName

        Write-Host "Renaming: $($file.Name) -> $newName" -ForegroundColor Yellow

        # Rename the file
        Rename-Item -Path $file.FullName -NewName $newName -Force

        $renamed++
        Write-Host "  Success!" -ForegroundColor Green

    } catch {
        Write-Host "  ERROR: $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host "`n=== Summary ===" -ForegroundColor Cyan
Write-Host "Renamed: $renamed images" -ForegroundColor Green
Write-Host "Complete!" -ForegroundColor Cyan
