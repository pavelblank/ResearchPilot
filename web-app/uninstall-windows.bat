@echo off
REM ============================================================
REM   ResearchPilot Windows Uninstaller
REM
REM   Removes:
REM     - Auto-start task (if registered)
REM     - Server processes
REM     - Python cache files
REM
REM   Does NOT delete your:
REM     - 01-PROJECTS/   (your research)
REM     - 99-SYSTEM-BACKEND/settings.json   (your API keys)
REM
REM   To COMPLETELY remove everything, including your data,
REM   manually delete the ResearchPilot folder afterwards.
REM ============================================================

title ResearchPilot - Uninstaller
echo.
echo ============================================================
echo   ResearchPilot Uninstaller
echo ============================================================
echo.

REM --- Remove auto-start task ---
echo [1/3] Removing auto-start task...
schtasks /delete /tn "ResearchPilot" /f >nul 2>&1 && echo       Done. || echo       None registered.

REM --- Kill any running server ---
echo.
echo [2/3] Stopping any running servers...
taskkill /FI "WINDOWTITLE eq ResearchPilot*" /T /F >nul 2>&1 && echo       Done. || echo       None running.

REM --- Clean Python cache ---
echo.
echo [3/3] Cleaning Python cache files...
if exist "__pycache__" rd /s /q __pycache__ >nul 2>&1
if exist "..\01-PROJECTS\00-TEMPLATE\web-app\__pycache__" rd /s /q "..\01-PROJECTS\00-TEMPLATE\web-app\__pycache__" >nul 2>&1
for /d /r "..\01-PROJECTS" %%d in (__pycache__) do rd /s /q "%%d" >nul 2>&1
echo       Done.

echo.
echo ============================================================
echo   Uninstall complete.
echo.
echo   Your research data, projects, and settings are still
echo   in the ResearchPilot folder. Delete the folder manually
echo   to remove them permanently.
echo.
echo   To re-install, see SETUP.md
echo ============================================================
echo.
pause
