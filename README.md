# AI Toolbar

A minimalist desktop application that serves as a quick-access toolbar and tab manager for various AI tools on Linux Mint Xfce. The application functions like a standalone browser window specifically designed for AI tools, separate from your main browser.

![AI Toolbar Screenshot](docs/screenshot.png)

## Features

### 🔥 Core Functionality
- **Global Hotkey**: Press `Alt + W` to show/hide the toolbar instantly
- **Tab Management**: Chrome-style tabs for switching between AI tools
- **Cyberpunk Theme**: Modern dark theme with neon accents
- **System Integration**: Minimizes to panel, autostart options
- **Lightweight**: Fast startup and minimal resource usage

### 🤖 Supported AI Tools

**Chatbots:**
- [ChatGPT](https://chat.openai.com) - OpenAI's conversational AI
- [Gemini](https://gemini.google.com) - Google's AI assistant
- [Grok](https://x.ai/grok) - X.AI's witty AI assistant
- [Claude](https://claude.ai) - Anthropic's helpful AI assistant

**AI Agents:**
- [Manus](https://manus.chat) - Advanced AI agent platform
- [Mini-Max](https://minimax.chat) - Specialized AI agent

**Development Tools:**
- [GitHub Copilot](https://copilot.github.com) - AI pair programmer
- [Windsurf](https://codeium.com/windsurf) - AI-powered development environment
- [Google AI Studio](https://aistudio.google.com) - AI development platform

## Installation

### Quick Install (Recommended)

```bash
git clone https://github.com/Aivix-Studios/ai_toolbar.git
cd ai_toolbar
chmod +x install.sh
./install.sh
```

### Manual Installation

1. **Prerequisites:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-pyqt5 python3-pyqt5.qtwebengine python3-pip

# Fedora
sudo dnf install python3-qt5 python3-qt5-webengine python3-pip

# Arch Linux
sudo pacman -S python-pyqt5 python-pyqtwebengine python-pip
```

2. **Install AI Toolbar:**
```bash
git clone https://github.com/Aivix-Studios/ai_toolbar.git
cd ai_toolbar
pip install -r requirements.txt
pip install -e .
```

3. **Create launcher script:**
```bash
mkdir -p ~/.local/bin
cat > ~/.local/bin/ai-toolbar << 'EOF'
#!/bin/bash
cd /path/to/ai_toolbar
python src/main.py "$@"
EOF
chmod +x ~/.local/bin/ai-toolbar
```

## Usage

### Starting the Application

```bash
# From command line
ai-toolbar

# Or from applications menu
# Search for "AI Toolbar"
```

### Keyboard Shortcuts

- `Alt + W`: Toggle toolbar visibility
- `Ctrl + T`: Open new tab (planned)
- `Ctrl + W`: Close current tab (planned)
- `Ctrl + Q`: Quit application

### Basic Workflow

1. **Launch**: Start AI Toolbar from applications menu or command line
2. **Select Tool**: Click any AI tool button in the toolbar
3. **Work**: Use the AI tool in its dedicated tab
4. **Switch**: Click tabs to switch between tools
5. **Hide**: Press `Alt + W` to hide toolbar when not needed

## Configuration

### Configuration File

AI Toolbar stores its configuration in `~/.config/ai-toolbar/config.json`:

```json
{
    "window": {
        "width": 1200,
        "height": 800,
        "always_on_top": false,
        "opacity": 0.95
    },
    "hotkey": {
        "show_hide": "alt+w",
        "enabled": true
    },
    "appearance": {
        "theme": "cyberpunk",
        "show_toolbar": true,
        "show_tabs": true
    },
    "autostart": false,
    "minimize_to_panel": true
}
```

### Customization

- **Change Hotkey**: Modify `hotkey.show_hide` in config file
- **Window Size**: Adjust `window.width` and `window.height`
- **Transparency**: Change `window.opacity` (0.0 - 1.0)
- **Autostart**: Set `autostart` to `true`

## System Integration

### Desktop Environment

Optimized for **Xfce** on Linux Mint, but works on other desktop environments:
- KDE Plasma
- GNOME
- MATE
- Cinnamon

### Panel Integration

When minimized, AI Toolbar appears as a grouped icon in the system panel showing:
- Number of open tabs
- Quick access to restore window
- Context menu with common actions

### Autostart

To enable autostart:
```bash
mkdir -p ~/.config/autostart
cp ai-toolbar.desktop ~/.config/autostart/
```

## Development

### Project Structure

```
ai_toolbar/
├── src/
│   ├── main.py              # Entry point
│   ├── ui/
│   │   ├── main_window.py   # Main window class
│   │   ├── tab_manager.py   # Tab management
│   │   ├── toolbar.py       # Toolbar buttons
│   │   └── styles.py        # Cyberpunk styling
│   ├── core/
│   │   ├── hotkeys.py       # Global hotkey handling
│   │   ├── config.py        # Configuration management
│   │   ├── web_engine.py    # Web rendering engine
│   │   └── ai_tools.py      # AI tool definitions
│   └── resources/
│       ├── icons/           # Tool icons (SVG)
│       ├── styles/          # QSS theme files
│       └── config.json      # Default configuration
├── requirements.txt         # Python dependencies
├── setup.py                # Installation script
├── install.sh              # Linux installation script
├── ai-toolbar.desktop      # Desktop entry file
└── README.md               # This file
```

### Dependencies

- **Python 3.8+**
- **PyQt5** - GUI framework
- **PyQtWebEngine** - Web content rendering
- **pynput** - Global hotkey handling
- **keyring** - Secure credential storage (future use)

### Running from Source

```bash
cd ai_toolbar
python src/main.py
```

### Building Distribution

```bash
python setup.py sdist bdist_wheel
```

## Troubleshooting

### Common Issues

**Hotkey not working:**
- Check if other applications are using `Alt + W`
- Ensure pynput has proper permissions
- Try running as: `sudo ai-toolbar` (not recommended for regular use)

**Web pages not loading:**
- Check internet connection
- Ensure PyQtWebEngine is properly installed
- Clear web cache: `rm -rf ~/.cache/ai-toolbar/`

**Application won't start:**
- Verify Python and PyQt5 installation
- Check error output: `ai-toolbar --debug`
- Install missing dependencies

### Logs

Application logs are stored in:
- Linux: `~/.local/share/ai-toolbar/logs/`
- Debug mode: Run with `ai-toolbar --debug`

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Areas for Contribution

- 🎨 **UI/UX improvements**
- 🔧 **New AI tool integrations**
- 🐛 **Bug fixes and testing**
- 📚 **Documentation**
- 🌍 **Internationalization**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **PyQt5** for the excellent GUI framework
- **AI Tool Providers** for their amazing platforms
- **Linux Mint & Xfce** for the desktop environment
- **Open Source Community** for inspiration and support

## Support

- 📖 **Documentation**: [GitHub Wiki](https://github.com/Aivix-Studios/ai_toolbar/wiki)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/Aivix-Studios/ai_toolbar/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Aivix-Studios/ai_toolbar/discussions)
- 📧 **Contact**: [contact@aivix.com](mailto:contact@aivix.com)

---

**Made with ❤️ by [Aivix Studios](https://aivix.com)**
