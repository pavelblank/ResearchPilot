@echo off
REM ============================================================
REM   ResearchPilot — Auto-Start on Windows Login
REM
REM   Run this ONCE to make ResearchPilot start every time
REM   you log in. The browser will open automatically.
REM
REM   Usage: Right-click → "Run as administrator"
REM
REM   To REMOVE auto-start later, open an admin Command Prompt
REM   and run:
REM     schtasks /delete /tn "ResearchPilot" /f
REM ============================================================

title ResearchPilot - Auto-Start Setup
echo.
echo ============================================================
echo   ResearchPilot - Auto-Start Setup
echo ============================================================
echo.

REM --- Check for admin rights ---
net session >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] This script needs Administrator privileges.
    echo.
    echo How to fix:
    echo   1. Right-click this file
    echo   2. Select "Run as administrator"
    echo.
    pause
    exit /b 1
)

REM --- Build path to launcher ---
set "RESEARCHPILOT_DIR=%~dp0.."
set "LAUNCHER=%RESEARCHPILOT_DIR%\start-research.bat"

if not exist "%LAUNCHER%" (
    echo [ERROR] Could not find launcher at:
    echo   %LAUNCHER%
    echo.
    echo Make sure you run this from inside the web-app folder.
    pause
    exit /b 1
)

echo Registering ResearchPilot to start on Windows login...
echo.

REM --- Remove any old task from previous installs ---
schtasks /delete /tn "ResearchPilot" /f >nul 2>&1
schtasks /delete /tn "ERA-ResearchAssistant" /f >nul 2>&1
schtasks /delete /tn "ERA" /f >nul 2>&1

REM --- Create the new task ---
schtasks /create ^
    /tn "ResearchPilot" ^
    /tr "\"%LAUNCHER%\"" ^
    /sc ONLOGON ^
    /rl HIGHEST ^
    /ru "%USERNAME%" ^
    /f

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Could not register the task.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   SUCCESS!
echo ============================================================
echo.
echo   ResearchPilot will now start automatically every time
echo   you log in to Windows. Your browser will open to:
echo.
echo       http://127.0.0.1:8000
echo.
echo   To remove auto-start later, open an admin Command
echo   Prompt and run:
echo.
echo       schtasks /delete /tn "ResearchPilot" /f
echo.
echo ============================================================
pause
