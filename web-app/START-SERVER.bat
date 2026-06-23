@echo off
REM ============================================================
REM   ResearchPilot — One-Click Server Launcher
REM
REM   First run: automatically installs dependencies
REM   Later runs: just starts the server
REM
REM   Usage: Double-click this file
REM ============================================================

setlocal
title ResearchPilot

echo.
echo ============================================================
echo   ResearchPilot - Starting Server...
echo ============================================================
echo.

cd /d "%~dp0"

REM --- Check Python ---
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed.
    echo.
    echo Please install Python 3.10+ from:
    echo   https://www.python.org/downloads/
    echo.
    echo IMPORTANT: During install, tick "Add Python to PATH"
    echo at the bottom of the first screen.
    echo.
    echo For detailed instructions, see SETUP.md
    echo.
    pause
    exit /b 1
)

REM --- Auto-install dependencies on first run ---
if not exist ".installed" (
    echo [1/2] First run detected - installing dependencies...
    echo       This takes 1-3 minutes the first time.
    echo.
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    if %ERRORLEVEL% NEQ 0 (
        echo.
        echo [ERROR] Failed to install some packages.
        echo Try running install-windows.bat as Administrator.
        pause
        exit /b 1
    )
    echo. > .installed
    echo [OK] Dependencies installed. Server starting...
    echo.
)

REM --- Start server ---
echo [2/2] Starting ResearchPilot...
echo.
echo   URL: http://127.0.0.1:8000
echo   (Local only - not exposed to network)
echo.
echo   Press Ctrl+C to stop the server.
echo   Close this window to quit.
echo.

python main.py

echo.
echo   ResearchPilot stopped.
pause
