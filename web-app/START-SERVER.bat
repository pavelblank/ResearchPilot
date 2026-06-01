@echo off
title ERA Research Assistant
echo.
echo  ============================================================
echo   ERA Research Assistant - Starting Server...
echo  ============================================================
echo.

REM Set Gemini API key here if you have one (remove the REM)
REM set GEMINI_API_KEY=your_key_here

REM Set Ollama model preference (default: llama3)
REM set OLLAMA_MODEL=mistral

cd /d "C:\F- Drive\MYWORK-Research1\web-app"

echo  Starting on http://127.0.0.1:8000
echo  (Local only — not exposed to network)
echo.
echo  Press Ctrl+C to stop the server.
echo.

python main.py

pause
