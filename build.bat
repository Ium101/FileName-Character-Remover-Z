@echo off
REM ==========================================
REM Filename Character Remover - Build Script
REM Windows Build Script
REM ==========================================

setlocal enabledelayedexpansion

echo.
echo ========================================
echo Building .exe GUI application...
echo For Linux/macOS, use: build.sh
echo ========================================
echo.

REM Ensure Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Installing PyInstaller (if not already installed)...
python -m pip install --upgrade pyinstaller

if %errorlevel% neq 0 (
    echo Error: Failed to install PyInstaller
    pause
    exit /b 1
)

REM Clean previous builds
echo.
echo Cleaning previous builds...
if exist build (
    rmdir /s /q build >nul 2>&1
)
if exist dist (
    rmdir /s /q dist >nul 2>&1
)
if exist "filename-character-remover-z.spec" (
    del "filename-character-remover-z.spec" >nul 2>&1
)

echo.
echo Building executable from source...
echo.

REM Build using PyInstaller (use python -m for reliability)
if exist app.ico (
    echo Using custom icon...
    python -m PyInstaller filename-character-remover-z.py ^
        --onefile ^
        --windowed ^
        --name filename-character-remover-z ^
        --icon=app.ico ^
        --noconfirm
) else (
    echo Building without custom icon...
    python -m PyInstaller filename-character-remover-z.py ^
        --onefile ^
        --windowed ^
        --name filename-character-remover-z ^
        --noconfirm
)

if %errorlevel% neq 0 (
    echo.
    echo Error: Build failed!
    echo Please check the Python file for syntax errors.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo Build completed successfully!
echo ==========================================
echo.
echo The executable is located at:
echo   dist\filename-character-remover-z.exe
echo.
echo Single-file executable ready to distribute!
echo No additional files needed.
echo.
pause
