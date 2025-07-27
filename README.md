# AI Toolbar

Minimalist desktop toolbar for quick access to AI tools on Linux Mint Xfce

A sleek, cyberpunk-styled desktop application that provides instant access to 9 popular AI tools through a unified interface. Built specifically for Linux Mint with Xfce desktop environment.

## Features

### 🤖 AI Tools Integration
- **ChatGPT** - OpenAI's conversational AI
- **Claude** - Anthropic's AI assistant  
- **Gemini** - Google's AI model
- **Perplexity** - AI-powered search engine
- **GitHub Copilot** - AI coding assistant
- **Midjourney** - AI image generation
- **DALL-E** - OpenAI's image generator
- **Stable Diffusion** - Open-source image generation
- **Hugging Face** - AI model hub and tools

### 🎨 Cyberpunk Design
- Dark theme with neon green and pink accents
- Matrix-inspired color scheme
- Sleek, modern interface elements
- Customizable styling options

### ⚡ Quick Access Features
- Global hotkeys for instant tool access
- Always-on-top toolbar option
- Tab-based browsing within tools
- System tray integration
- Auto-hide functionality

### 🔧 Customization
- Configurable hotkeys for each tool
- Adjustable window positioning
- Theme customization options
- Startup behavior settings

## Prerequisites

### System Requirements
- **OS**: Linux Mint 20+ or Ubuntu 20.04+ (Xfce desktop environment recommended)
- **Python**: 3.8 or higher
- **Display**: X11 (Wayland support coming soon)
- **Memory**: Minimum 512MB RAM available
- **Storage**: 100MB free space

### Required System Packages
The installation script will automatically install these, but if installing manually:

```bash
sudo apt install python3-dev python3-pip python3-venv python3-pyqt5 python3-pyqt5.qtwebengine qt5-default
```

## Installation

### Automatic Installation (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Aivix-Studios/ai_toolbar.git
   cd ai_toolbar
   ```

2. **Run the installation script**:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

3. **Follow the prompts** - the script will:
   - Install system dependencies
   - Create a virtual environment
   - Install Python packages
   - Set up desktop integration
   - Create launch scripts

### Manual Installation

1. **Install system dependencies**:
   ```bash
   sudo apt update
   sudo apt install python3-dev python3-pip python3-venv python3-pyqt5 python3-pyqt5.qtwebengine
   ```

2. **Create virtual environment**:
   ```bash
   python3 -m venv ~/.ai-toolbar-venv
   source ~/.ai-toolbar-venv/bin/activate
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the package**:
   ```bash
   pip install -e .
   ```

## Usage

### Starting the Application

**Method 1: Command Line**
```bash
ai-toolbar
```

**Method 2: Desktop Menu**
- Search for "AI Toolbar" in your application menu
- Click to launch

**Method 3: Direct Python**
```bash
cd ai_toolbar
python src/main.py
```

### Default Hotkeys

| Hotkey | Action |
|--------|--------|
| `Ctrl+Alt+T` | Toggle toolbar visibility |
| `Ctrl+Alt+C` | Quick chat (opens default chat tool) |
| `Ctrl+Alt+S` | Quick search (opens Perplexity) |
| `Ctrl+Alt+1` | Open ChatGPT |
| `Ctrl+Alt+2` | Open Claude |
| `Ctrl+Alt+3` | Open Gemini |
| `Ctrl+Alt+4` | Open Perplexity |
| `Ctrl+Alt+5` | Open GitHub Copilot |
| `Ctrl+Alt+6` | Open Midjourney |
| `Ctrl+Alt+7` | Open DALL-E |
| `Ctrl+Alt+8` | Open Stable Diffusion |
| `Ctrl+Alt+9` | Open Hugging Face |

## Configuration

### Configuration File Location
```
~/.config/ai-toolbar/config.json
```

### Customizing AI Tools
Edit the configuration file to modify tool URLs, hotkeys, or add new tools:

```json
{
  "ai_tools": {
    "CustomTool": {
      "name": "Custom Tool",
      "url": "https://example.com",
      "icon": "icons/custom.png",
      "description": "My custom AI tool",
      "category": "custom",
      "hotkey": "ctrl+alt+0"
    }
  }
}
```

### Theme Customization
Modify colors in the configuration:

```json
{
  "theme": {
    "primary_color": "#00FF41",
    "secondary_color": "#FF0080",
    "background_color": "#0D1117"
  }
}
```

## Development

### Setting Up Development Environment

1. **Fork and clone the repository**
2. **Install development dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

3. **Run tests**:
   ```bash
   python -m pytest tests/
   ```

### Project Structure

```
ai_toolbar/
├── src/
│   ├── main.py              # Application entry point
│   ├── ui/                  # User interface components
│   │   ├── main_window.py   # Main application window
│   │   ├── tab_manager.py   # Tab management
│   │   ├── toolbar.py       # Toolbar components
│   │   └── styles.py        # Cyberpunk theme styling
│   ├── core/                # Core functionality
│   │   ├── hotkeys.py       # Global hotkey handling
│   │   ├── config.py        # Configuration management
│   │   ├── web_engine.py    # Web rendering engine
│   │   └── ai_tools.py      # AI tool definitions
│   └── resources/           # Static resources
│       ├── config.json      # Default configuration
│       ├── icons/           # Tool icons
│       └── styles/          # QSS theme files
├── tests/                   # Unit tests
├── requirements.txt         # Python dependencies
├── setup.py                # Package installation
├── install.sh              # Linux installation script
└── ai-toolbar.desktop      # Desktop entry file
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## Troubleshooting

### Common Issues

**Issue**: Application won't start
- **Solution**: Check Python version (3.8+ required)
- **Solution**: Ensure all dependencies are installed
- **Solution**: Check if virtual environment is activated

**Issue**: Global hotkeys not working
- **Solution**: Make sure the application has accessibility permissions
- **Solution**: Check for hotkey conflicts with other applications

**Issue**: Web pages not loading
- **Solution**: Check internet connection
- **Solution**: Verify PyQtWebEngine is properly installed

**Issue**: Desktop entry not appearing
- **Solution**: Run `update-desktop-database ~/.local/share/applications/`
- **Solution**: Log out and log back in

### Getting Help

1. **Check the [Issues](https://github.com/Aivix-Studios/ai_toolbar/issues)** page for known problems
2. **Search existing issues** before creating new ones
3. **Provide system information** when reporting bugs:
   - OS version and desktop environment
   - Python version
   - Full error messages

### Debug Mode

Run with debug output:
```bash
ai-toolbar --debug
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- PyQt5 team for the excellent GUI framework
- All AI tool providers for their amazing services
- Linux Mint and Xfce communities for the great desktop environment

## Roadmap

### Phase 1 ✅
- [x] Basic project structure
- [x] Core dependencies setup
- [x] Installation scripts
- [x] Configuration framework

### Phase 2 (Next)
- [ ] GUI implementation
- [ ] Web engine integration
- [ ] Basic AI tool buttons
- [ ] Theme application

### Phase 3 (Future)
- [ ] Global hotkey implementation
- [ ] Advanced tab management
- [ ] Plugin system
- [ ] Wayland support

---

**Made with ❤️ by Aivix Studios**
