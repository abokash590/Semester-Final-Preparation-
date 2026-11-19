@echo off
title Semester Final Codex
echo ========================================================
echo   Launching Semester Final Codex on http://localhost:8000
echo ========================================================
echo.
echo Opening browser...
start http://localhost:8000
echo.
echo Starting local web server... (Press Ctrl+C to stop)
python -m http.server 8000
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Python was not found in PATH. Trying py launcher...
    py -m http.server 8000
)
pause
