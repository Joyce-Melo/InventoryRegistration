$exclude = @("venv", "Inventory.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Inventory.zip" -Force