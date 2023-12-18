
@echo off

timeout /t 1 >nul

rmdir /s /q %USERPROFILE%/Appdata/Roaming/WindowsUpdates

rmdir /s /q %USERPROFILE%/AppData/Local/Snky
reg del HKEY_CURRENT_USER\Software\WindowsUpdates /va /f
