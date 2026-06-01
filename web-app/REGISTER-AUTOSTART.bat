@echo off
title ERA - Register Auto-Start
echo ============================================================
echo   Registering ERA to start with Windows...
echo ============================================================
echo.

schtasks /create /tn "ERA-ResearchAssistant" /tr "\"C:\F- Drive\MYWORK-Research1\start-research.bat\"" /sc ONLOGON /ru "%USERNAME%" /f

echo.
echo  Done! ERA will start automatically when you log in.
echo  Access at: http://localhost:8000
echo.
echo  To start manually: double-click start-research.bat
echo  To remove auto-start: schtasks /delete /tn "ERA-ResearchAssistant" /f
echo.
pause
