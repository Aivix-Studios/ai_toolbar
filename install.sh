#!/bin/bash

# AI Toolbar Installation Script for Linux

set -e

echo "AI Toolbar Installation Script"
echo "=============================="

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   echo "This script should not be run as root for security reasons."
   echo "Please run as a regular user."
   exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
REQUIRED_VERSION="3.8"

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "Error: Python 3.8 or higher is required. You have Python $PYTHON_VERSION"
    exit 1
fi

echo "✓ Python $PYTHON_VERSION found"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is not installed. Please install python3-pip"
    exit 1
fi

echo "✓ pip3 found"

# Install system dependencies for PyQt5
echo "Installing system dependencies..."
if command -v apt-get &> /dev/null; then
    # Debian/Ubuntu
    echo "Detected Debian/Ubuntu system"
    sudo apt-get update
    sudo apt-get install -y python3-pyqt5 python3-pyqt5.qtwebengine python3-pip
elif command -v dnf &> /dev/null; then
    # Fedora
    echo "Detected Fedora system"
    sudo dnf install -y python3-qt5 python3-qt5-webengine python3-pip
elif command -v pacman &> /dev/null; then
    # Arch Linux
    echo "Detected Arch Linux system"
    sudo pacman -S --noconfirm python-pyqt5 python-pyqtwebengine python-pip
else
    echo "Warning: Could not detect package manager. Please install PyQt5 and PyQtWebEngine manually."
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv ~/.local/share/ai-toolbar-venv

# Activate virtual environment
source ~/.local/share/ai-toolbar-venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Install the application
echo "Installing AI Toolbar..."
pip install -e .

# Create wrapper script
echo "Creating launcher script..."
mkdir -p ~/.local/bin

cat > ~/.local/bin/ai-toolbar << 'EOF'
#!/bin/bash
source ~/.local/share/ai-toolbar-venv/bin/activate
python -m src.main "$@"
EOF

chmod +x ~/.local/bin/ai-toolbar

# Install desktop file
echo "Installing desktop entry..."
mkdir -p ~/.local/share/applications
cp ai-toolbar.desktop ~/.local/share/applications/

# Update desktop database
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database ~/.local/share/applications/
fi

# Create autostart entry if requested
read -p "Do you want AI Toolbar to start automatically on login? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    mkdir -p ~/.config/autostart
    cp ai-toolbar.desktop ~/.config/autostart/
    echo "✓ Autostart enabled"
fi

echo ""
echo "Installation completed successfully!"
echo ""
echo "You can now:"
echo "  • Run 'ai-toolbar' from the command line"
echo "  • Launch from your applications menu"
echo "  • Use Alt+W hotkey to show/hide the toolbar"
echo ""
echo "Note: Make sure ~/.local/bin is in your PATH to run from command line."
echo "You may need to log out and back in for the PATH to be updated."