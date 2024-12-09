@echo off
echo Installing required Python libraries...

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Please install Python and add it to PATH.
    pause
    exit /b
)

REM Install required libraries
echo Installing PyQt5...
pip install PyQt5

REM Confirm installation
echo All required libraries have been installed.
pause
