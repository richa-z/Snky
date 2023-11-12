
@echo off

timeout /t 1 >nul

set "dir_path=%~dp0"

cd /d "%dir_path%..\"

rmdir /s /q "%dir_path%"
