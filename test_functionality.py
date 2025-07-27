#!/usr/bin/env python3
"""
Test script for AI Toolbar - verifies functionality without GUI
"""

import sys
import os
import json

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_config_system():
    """Test configuration management."""
    print("Testing configuration system...")
    try:
        from core.config import Config
        config = Config()
        
        # Test getting values
        width = config.get('window.width', 1000)
        hotkey = config.get('hotkey.show_hide', 'alt+w')
        
        print(f"✓ Window width: {width}")
        print(f"✓ Hotkey: {hotkey}")
        
        # Test setting values
        config.set('test.value', 42)
        assert config.get('test.value') == 42
        print("✓ Configuration get/set working")
        
        return True
    except Exception as e:
        print(f"✗ Configuration test failed: {e}")
        return False

def test_ai_tools():
    """Test AI tools management."""
    print("\nTesting AI tools system...")
    try:
        from core.ai_tools import AIToolsManager, AITool
        manager = AIToolsManager()
        
        tools = manager.get_tools()
        print(f"✓ Loaded {len(tools)} AI tools")
        
        # Test categories
        chatbots = manager.get_tools_by_category('chatbot')
        agents = manager.get_tools_by_category('agent')
        lowcode = manager.get_tools_by_category('low-code')
        
        print(f"✓ Chatbots: {len(chatbots)}")
        print(f"✓ Agents: {len(agents)}")
        print(f"✓ Low-code tools: {len(lowcode)}")
        
        # Test getting specific tool
        chatgpt = manager.get_tool_by_name('ChatGPT')
        assert chatgpt is not None
        assert chatgpt.url == 'https://chat.openai.com'
        print("✓ Tool lookup working")
        
        return True
    except Exception as e:
        print(f"✗ AI tools test failed: {e}")
        return False

def test_ui_modules():
    """Test UI module imports."""
    print("\nTesting UI modules...")
    try:
        from ui.styles import CYBERPUNK_STYLE, get_tool_button_style, CATEGORY_COLORS
        
        assert len(CYBERPUNK_STYLE) > 1000
        print("✓ Cyberpunk styles loaded")
        
        assert 'chatbot' in CATEGORY_COLORS
        assert 'agent' in CATEGORY_COLORS
        assert 'low-code' in CATEGORY_COLORS
        print("✓ Category colors defined")
        
        # Test style generation
        style = get_tool_button_style('chatbot')
        assert 'QToolButton' in style
        print("✓ Dynamic style generation working")
        
        return True
    except Exception as e:
        print(f"✗ UI modules test failed: {e}")
        return False

def test_resources():
    """Test resource files."""
    print("\nTesting resources...")
    try:
        # Test config file
        config_path = os.path.join('src', 'resources', 'config.json')
        assert os.path.exists(config_path)
        
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        
        assert 'ai_tools' in config_data
        assert len(config_data['ai_tools']) == 9
        print("✓ Default configuration file valid")
        
        # Test icon files
        icons_dir = os.path.join('src', 'resources', 'icons')
        assert os.path.exists(icons_dir)
        
        icon_files = [f for f in os.listdir(icons_dir) if f.endswith('.svg')]
        assert len(icon_files) == 9
        print(f"✓ Found {len(icon_files)} icon files")
        
        # Test required icons exist
        required_icons = [
            'chatgpt.svg', 'gemini.svg', 'grok.svg', 'claude.svg',
            'manus.svg', 'minimax.svg', 'github-copilot.svg',
            'windsurf.svg', 'ai-studio.svg'
        ]
        
        for icon in required_icons:
            icon_path = os.path.join(icons_dir, icon)
            assert os.path.exists(icon_path)
        
        print("✓ All required icons present")
        
        return True
    except Exception as e:
        print(f"✗ Resources test failed: {e}")
        return False

def test_installation_files():
    """Test installation and setup files."""
    print("\nTesting installation files...")
    try:
        # Test setup.py
        assert os.path.exists('setup.py')
        
        # Test requirements.txt
        assert os.path.exists('requirements.txt')
        with open('requirements.txt', 'r') as f:
            requirements = f.read()
        
        required_packages = ['PyQt5', 'PyQtWebEngine', 'pynput', 'keyring']
        for package in required_packages:
            assert package in requirements
        
        print("✓ Requirements file contains all dependencies")
        
        # Test desktop file
        assert os.path.exists('ai-toolbar.desktop')
        print("✓ Desktop file present")
        
        # Test install script
        assert os.path.exists('install.sh')
        assert os.access('install.sh', os.X_OK)
        print("✓ Install script present and executable")
        
        return True
    except Exception as e:
        print(f"✗ Installation files test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("AI Toolbar - Functionality Test Suite")
    print("=" * 40)
    
    tests = [
        test_config_system,
        test_ai_tools,
        test_ui_modules,
        test_resources,
        test_installation_files
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n" + "=" * 40)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! AI Toolbar is ready for deployment.")
        return 0
    else:
        print("❌ Some tests failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())