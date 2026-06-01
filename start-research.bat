@echo off
title AI Research Assistant (MRBLANK_RA)
cd /d "C:\F- Drive\MYWORK-Research1\web-app"
echo ============================================================
echo   AI Research Assistant (MRBLANK_RA) System Starting...
echo ============================================================
echo.
echo  Starting web server...
start /b python main.py
timeout /t 4 /nobreak >nul
echo  Opening browser...
start "" chrome --new-window "http://192.168.68.103:8000"
echo.
echo  MRBLANK_RA running at: http://192.168.68.103:8000
echo  Close this window to stop the server.
