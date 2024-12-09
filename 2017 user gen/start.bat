@echo off
echo Starting UserGen...

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Please install Python and add it to PATH.
    pause
    exit /b
)

REM Run the UserGen.py file
python UserGen.py

REM Keep the terminal open after execution
pause
