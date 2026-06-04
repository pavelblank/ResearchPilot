@echo off
REM ============================================================
REM   ResearchPilot Windows Setup
REM   One-time setup: installs Python dependencies.
REM
REM   Usage: Double-click this file. Or from cmd:
REM          install-windows.bat
REM
REM   What it does:
REM     1. Checks Python is installed
REM     2. Installs all required packages
REM     3. Creates default folders
REM ============================================================

setlocal
title ResearchPilot - Setup

echo.
echo ============================================================
echo   ResearchPilot - First-Time Setup
echo ============================================================
echo.

REM --- Check Python ---
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not in PATH.
    echo.
    echo Please install Python 3.10 or newer from:
    echo   https://www.python.org/downloads/
    echo.
    echo IMPORTANT: During install, tick the box that says
    echo "Add Python to PATH" at the bottom of the first screen.
    echo.
    pause
    exit /b 1
)

echo [OK] Python is installed:
python --version
echo.

REM --- Install dependencies ---
echo [1/3] Installing required packages (this takes 1-3 minutes)...
echo.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Failed to install some packages.
    echo Try running this in an Administrator Command Prompt.
    pause
    exit /b 1
)
echo.
echo [OK] All packages installed.
echo.

REM --- Create default folders ---
echo [2/3] Creating default folders...
if not exist "..\01-PROJECTS" mkdir "..\01-PROJECTS"
if not exist "..\00-SYSTEM-CORE" mkdir "..\00-SYSTEM-CORE"
if not exist "..\99-SYSTEM-BACKEND" mkdir "..\99-SYSTEM-BACKEND"
if not exist "..\INCOMING" mkdir "..\INCOMING"
if not exist "..\INCOMING\UNREAD-WEB" mkdir "..\INCOMING\UNREAD-WEB"
if not exist "..\99-SYSTEM-BACKEND\chats" mkdir "..\99-SYSTEM-BACKEND\chats"
if not exist "..\00-SYSTEM-CORE\skills" mkdir "..\00-SYSTEM-CORE\skills"
echo [OK] Folders created.
echo.

REM --- Done ---
echo [3/3] Setup complete!
echo.
echo ============================================================
echo   Next steps:
echo   1. Double-click START-SERVER.bat to launch the system
echo   2. Your browser will open automatically
echo   3. To enable auto-start on login, run REGISTER-AUTOSTART.bat
echo.
echo   For detailed help, see SETUP.md
echo ============================================================
echo.
pause
