#!/bin/bash

# ==========================================
# Filename Character Remover - Build Script
# Universal build script for Linux, macOS
# ==========================================

set -e  # Exit on error

echo ""
echo "=========================================="
echo "Building .exe GUI application..."
echo "=========================================="
echo ""
echo "Detected OS: $(uname -s)"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.6 or higher"
    exit 1
fi

echo "Python version:"
python3 --version
echo ""

echo "Installing PyInstaller (if not already installed)..."
python3 -m pip install --upgrade pyinstaller

if [ $? -ne 0 ]; then
    echo "Error: Failed to install PyInstaller"
    exit 1
fi

# Clean previous builds
echo ""
echo "Cleaning previous builds..."
rm -rf build dist *.spec 2>/dev/null || true

echo ""
echo "Building executable from source..."
echo ""

# Build using PyInstaller
OS=$(uname -s)
if [ "$OS" = "Darwin" ]; then
    # macOS-specific settings
    python3 -m PyInstaller filename-character-remover-z.py \
        --onefile \
        --windowed \
        --name filename-character-remover-z \
        --noconfirm \
        --osx-bundle-identifier "com.customcharacterremover.app"
elif [ "$OS" = "Linux" ]; then
    # Linux build
    python3 -m PyInstaller filename-character-remover-z.py \
        --onefile \
        --windowed \
        --name filename-character-remover-z \
        --noconfirm
else
    # Generic build for other Unix-like systems
    python3 -m PyInstaller filename-character-remover-z.py \
        --onefile \
        --windowed \
        --name filename-character-remover-z \
        --noconfirm
fi

if [ $? -ne 0 ]; then
    echo ""
    echo "Error: Build failed!"
    echo "Please check the Python file for syntax errors."
    exit 1
fi

echo ""
echo "=========================================="
echo "Build completed successfully!"
echo "=========================================="
echo ""

if [ "$OS" = "Darwin" ]; then
    echo "The application is located at:"
    echo "  dist/filename-character-remover-z.app"
    echo ""
    echo "To run: open dist/filename-character-remover-z.app"
    echo "Or double-click the app in Finder"
else
    echo "The executable is located at:"
    echo "  dist/filename-character-remover-z"
    echo ""
    echo "To run: ./dist/filename-character-remover-z"
    echo "Or make it executable: chmod +x dist/filename-character-remover-z"
fi

echo ""
echo "Single-file executable ready to distribute!"
echo ""
