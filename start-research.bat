@echo off
title ResearchPilot
cd /d "C:\F- Drive\MYWORK-Research1\web-app"
echo ============================================================
echo   ResearchPilot System Starting...
echo ============================================================
echo.
echo  Starting web server (this may take 30-60s on first run)...
start /b python main.py

echo  Waiting for server to become ready...
setlocal enabledelayedexpansion
set "READY="
for /l %%i in (1,1,60) do (
    timeout /t 1 /nobreak >nul
    >nul 2>&1 curl -s http://127.0.0.1:8000/api/status && set "READY=1" && goto :ready
)
:ready
if defined READY (
    echo  Server is ready!
    echo  Opening browser...
    start "" http://127.0.0.1:8000
) else (
    echo  WARNING: Could not verify server started.
    echo  Try manually opening: http://127.0.0.1:8000
    start "" http://127.0.0.1:8000
)
echo.
echo  ResearchPilot running at: http://127.0.0.1:8000
echo  Close this window to stop the server.
