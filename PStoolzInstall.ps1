$url = "https://download.sysinternals.com/files/PSTools.zip"
$outputDirectory = "$env:TEMP\PSTools"
$outputFile = "$outputDirectory\PSTools.zip"
$targetDirectory = "C:\Windows\System32"

# Create the output directory if it doesn't exist
if (!(Test-Path -Path $outputDirectory)) {
    New-Item -ItemType Directory -Path $outputDirectory | Out-Null
}

# Download the PsTools archive
Invoke-WebRequest -Uri $url -OutFile $outputFile

# Extract the archive to the output directory
Expand-Archive -Path $outputFile -DestinationPath $outputDirectory

# Copy the PsExec executable to the target directory
Copy-Item "$outputDirectory\PsExec.exe" $targetDirectory

# Clean up the output directory and archive
Remove-Item -Recurse $outputDirectory
Remove-Item $outputFile
