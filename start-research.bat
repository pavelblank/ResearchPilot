@echo off
REM ============================================================
REM   ResearchPilot — Root Launcher (Windows)
REM
REM   Double-click this to start the system. The browser
REM   opens automatically.
REM
REM   This file is self-locating: it works no matter where
REM   you move the ResearchPilot folder.
REM ============================================================

setlocal
title ResearchPilot

REM --- Get the directory this script lives in ---
set "RP_DIR=%~dp0"
if "%RP_DIR:~-1%"=="\" set "RP_DIR=%RP_DIR:~0,-1%"

echo.
echo ============================================================
echo   ResearchPilot System Starting...
echo ============================================================
echo.
echo   Install location: %RP_DIR%
echo.

REM --- Find Python ---
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not in PATH.
    echo See SETUP.md for installation instructions.
    pause
    exit /b 1
)

REM --- Start server in background, in the web-app folder ---
cd /d "%RP_DIR%\web-app"

echo   Starting web server (this takes 3-10 seconds)...
start "ResearchPilot-Server" /min python main.py

REM --- Wait for the server to come up ---
echo   Waiting for server to be ready...
set "READY=0"
for /l %%i in (1,1,60) do (
    timeout /t 1 /nobreak >nul
    >nul 2>&1 curl -s http://127.0.0.1:8000/api/health && (set "READY=1" & goto :server_ready)
)

:server_ready
if "%READY%"=="1" (
    echo   Server is ready!
) else (
    echo   WARNING: Could not verify server started in 60 seconds.
    echo   Try opening http://127.0.0.1:8000 manually.
)

echo.
echo ============================================================
echo   ResearchPilot is running!
echo.
echo   URL:    http://127.0.0.1:8000
echo   Folder: %RP_DIR%
echo.
echo   To stop: close the "ResearchPilot-Server" window
echo            in the taskbar, or right-click its icon.
echo ============================================================
echo.

REM --- Open browser ---
start "" http://127.0.0.1:8000

endlocal
