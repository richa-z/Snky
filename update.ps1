$gitlink = "https://github.com/richa-z/Snky/archive/refs/heads/main.zip"

$cfg_save = Get-Content .\cfg\config.json | Out-String | ConvertFrom-Json
#download full payload

Invoke-WebRequest -Uri $gitlink -OutFile "$($env:TEMP)\Snky.zip"
Expand-Archive -Path "$($env:TEMP)\Snky.zip" -DestinationPath "$($env:LOCALAPPDATA)\Snky" -Force
cmd.exe /c python -m pip install --upgrade pip
cmd.exe /c pip install -r "$($env:LOCALAPPDATA)\Snky\Snky-main\requirements.txt"

#replace template cfg with saved cfg
$cfg_save | ConvertTo-Json | Out-File "$($env:LOCALAPPDATA)\Snky\Snky-main\cfg\config.json"
