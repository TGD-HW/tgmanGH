# Change directory to the location of the Python script
Set-Location -Path "docs\Manual\source\tab\"

# Run the Python script
try {
    python readXLSXmakeMD.py
} catch {
    Write-Host "An error occurred while running the Python script."
    pause
    exit 1
}

# Change directory back to the original location
Set-Location -Path "../../../../"

# Build the MkDocs site
try {
    mkdocs build --clean
} catch {
    Write-Host "An error occurred while building the MkDocs site."
    pause
    exit 1
}

# Serve the MkDocs site
try {
    mkdocs serve
} catch {
    Write-Host "An error occurred while serving the MkDocs site."
    pause
    exit 1
}

# Pause to prevent the PowerShell window from closing
pause