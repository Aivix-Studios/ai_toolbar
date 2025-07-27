#!/bin/bash
# AI Toolbar Installation Script for Linux Mint/Ubuntu
# This script installs system dependencies and sets up the AI Toolbar application

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if running on supported OS
check_os() {
    if [[ -f /etc/os-release ]]; then
        . /etc/os-release
        OS=$NAME
        VER=$VERSION_ID
    else
        print_error "Cannot determine OS version"
        exit 1
    fi
    
    print_status "Detected OS: $OS $VER"
    
    # Check if it's a supported Ubuntu-based distribution
    if [[ $OS != *"Ubuntu"* ]] && [[ $OS != *"Linux Mint"* ]] && [[ $OS != *"Pop"* ]]; then
        print_warning "This script is designed for Ubuntu-based distributions"
        print_warning "You may need to manually install dependencies"
    fi
}

# Function to check Python version
check_python() {
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
        print_status "Python version: $PYTHON_VERSION"
        
        # Check if Python version is >= 3.8
        if python3 -c 'import sys; exit(0 if sys.version_info >= (3, 8) else 1)'; then
            print_success "Python version is compatible"
        else
            print_error "Python 3.8+ is required. Current version: $PYTHON_VERSION"
            exit 1
        fi
    else
        print_error "Python 3 is not installed"
        exit 1
    fi
}

# Function to install system dependencies
install_system_deps() {
    print_status "Installing system dependencies..."
    
    # Update package list
    sudo apt update
    
    # Install required system packages
    sudo apt install -y \
        python3-dev \
        python3-pip \
        python3-venv \
        python3-setuptools \
        python3-wheel \
        qt5-default \
        python3-pyqt5 \
        python3-pyqt5.qtwebengine \
        libqt5webkit5-dev \
        xvfb \
        libnss3-dev \
        libxss1 \
        libasound2-dev \
        libxtst6 \
        libxrandr2 \
        libasound2-dev \
        libpangocairo-1.0-0 \
        libatk1.0-0 \
        libcairo-gobject2 \
        libgtk-3-0 \
        libgdk-pixbuf2.0-0
        
    print_success "System dependencies installed"
}

# Function to create virtual environment
create_venv() {
    print_status "Creating virtual environment..."
    
    VENV_DIR="$HOME/.ai-toolbar-venv"
    
    if [[ -d "$VENV_DIR" ]]; then
        print_warning "Virtual environment already exists at $VENV_DIR"
        read -p "Do you want to recreate it? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf "$VENV_DIR"
        else
            print_status "Using existing virtual environment"
            return 0
        fi
    fi
    
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    
    # Upgrade pip
    pip install --upgrade pip setuptools wheel
    
    print_success "Virtual environment created at $VENV_DIR"
}

# Function to install Python dependencies
install_python_deps() {
    print_status "Installing Python dependencies..."
    
    VENV_DIR="$HOME/.ai-toolbar-venv"
    source "$VENV_DIR/bin/activate"
    
    # Install from requirements.txt
    pip install -r requirements.txt
    
    print_success "Python dependencies installed"
}

# Function to install the AI Toolbar package
install_package() {
    print_status "Installing AI Toolbar package..."
    
    VENV_DIR="$HOME/.ai-toolbar-venv"
    source "$VENV_DIR/bin/activate"
    
    # Install in development mode
    pip install -e .
    
    print_success "AI Toolbar package installed"
}

# Function to create desktop entry
create_desktop_entry() {
    print_status "Creating desktop entry..."
    
    DESKTOP_FILE="$HOME/.local/share/applications/ai-toolbar.desktop"
    VENV_DIR="$HOME/.ai-toolbar-venv"
    CURRENT_DIR=$(pwd)
    
    mkdir -p "$HOME/.local/share/applications"
    
    cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=AI Toolbar
Comment=Minimalist desktop toolbar for quick access to AI tools
Exec=$VENV_DIR/bin/python $CURRENT_DIR/src/main.py
Icon=$CURRENT_DIR/src/resources/icons/ai-toolbar.png
Terminal=false
Categories=Utility;Network;
StartupNotify=true
EOF
    
    chmod +x "$DESKTOP_FILE"
    
    print_success "Desktop entry created"
}

# Function to create launch script
create_launch_script() {
    print_status "Creating launch script..."
    
    SCRIPT_PATH="$HOME/.local/bin/ai-toolbar"
    VENV_DIR="$HOME/.ai-toolbar-venv"
    CURRENT_DIR=$(pwd)
    
    mkdir -p "$HOME/.local/bin"
    
    cat > "$SCRIPT_PATH" << EOF
#!/bin/bash
# AI Toolbar Launch Script
source "$VENV_DIR/bin/activate"
cd "$CURRENT_DIR"
python src/main.py "\$@"
EOF
    
    chmod +x "$SCRIPT_PATH"
    
    # Add to PATH if not already there
    if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
        print_warning "Added $HOME/.local/bin to PATH in .bashrc"
        print_warning "Run 'source ~/.bashrc' or restart your terminal"
    fi
    
    print_success "Launch script created at $SCRIPT_PATH"
}

# Function to run tests
run_tests() {
    print_status "Running basic tests..."
    
    VENV_DIR="$HOME/.ai-toolbar-venv"
    source "$VENV_DIR/bin/activate"
    
    cd tests
    python -m pytest test_basic.py -v
    cd ..
    
    print_success "Tests completed"
}

# Main installation function
main() {
    echo "================================"
    echo "AI Toolbar Installation Script"
    echo "================================"
    echo
    
    # Check if running as root
    if [[ $EUID -eq 0 ]]; then
        print_error "Do not run this script as root"
        print_error "The script will ask for sudo permissions when needed"
        exit 1
    fi
    
    # Run installation steps
    check_os
    check_python
    install_system_deps
    create_venv
    install_python_deps
    install_package
    create_desktop_entry
    create_launch_script
    
    # Optional: Run tests
    read -p "Do you want to run basic tests? (Y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        run_tests
    fi
    
    echo
    print_success "AI Toolbar installation completed!"
    echo
    echo "To start the application:"
    echo "  1. Run: ai-toolbar"
    echo "  2. Or search for 'AI Toolbar' in your application menu"
    echo "  3. Or run directly: python src/main.py"
    echo
    echo "Configuration will be stored in: ~/.config/ai-toolbar/"
    echo
}

# Run main function
main "$@"