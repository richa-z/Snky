$gitlink = "https://github.com/richa-z/Snky/archive/refs/heads/main.zip"

Copy-Item -Path "$($env:LOCALAPPDATA)\Snky\Snky-main\cfg\" -Destination "${env:TEMP}\cfg" -Recurse -Force
#download full payload

Invoke-WebRequest -Uri $gitlink -OutFile "$($env:TEMP)\Snky.zip"
Expand-Archive -Path "$($env:TEMP)\Snky.zip" -DestinationPath "$($env:LOCALAPPDATA)\Snky" -Force
cmd.exe /c python -m pip install --upgrade pip
cmd.exe /c pip install -r "$($env:LOCALAPPDATA)\Snky\Snky-main\requirements.txt"

#replace template cfg with saved cfg
Copy-Item -Path "${env:TEMP}\cfg\" -Destination "$($env:LOCALAPPDATA)\Snky\Snky-main\cfg" -Recurse -Force
