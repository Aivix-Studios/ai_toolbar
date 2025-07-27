#!/usr/bin/env python3
"""
Basic Tests for AI Toolbar

Tests basic functionality and imports for the AI Toolbar application.
"""

import unittest
import sys
import os
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))

class TestBasicImports(unittest.TestCase):
    """Test basic imports and module structure."""
    
    def test_main_module_import(self):
        """Test that main module can be imported."""
        try:
            import main
            self.assertTrue(hasattr(main, 'main'))
        except ImportError as e:
            self.fail(f"Failed to import main module: {e}")
    
    def test_ui_modules_import(self):
        """Test that UI modules can be imported."""
        try:
            from ui import main_window, tab_manager, toolbar, styles
            self.assertTrue(hasattr(main_window, 'MainWindow'))
            self.assertTrue(hasattr(tab_manager, 'TabManager'))
            self.assertTrue(hasattr(toolbar, 'Toolbar'))
            self.assertTrue(hasattr(styles, 'CyberpunkTheme'))
        except ImportError as e:
            self.fail(f"Failed to import UI modules: {e}")
    
    def test_core_modules_import(self):
        """Test that core modules can be imported."""
        try:
            from core import hotkeys, config, web_engine, ai_tools
            self.assertTrue(hasattr(hotkeys, 'HotkeyManager'))
            self.assertTrue(hasattr(config, 'ConfigManager'))
            self.assertTrue(hasattr(web_engine, 'WebEngine'))
            self.assertTrue(hasattr(ai_tools, 'AITool'))
            self.assertTrue(hasattr(ai_tools, 'AIToolManager'))
        except ImportError as e:
            self.fail(f"Failed to import core modules: {e}")

class TestConfigManager(unittest.TestCase):
    """Test configuration management."""
    
    def setUp(self):
        """Set up test environment."""
        from core.config import ConfigManager
        self.config_manager = ConfigManager()
    
    def test_default_config_structure(self):
        """Test that default configuration has expected structure."""
        config = self.config_manager.default_config
        self.assertIn('window', config)
        self.assertIn('theme', config)
        self.assertIn('hotkeys', config)
        self.assertIn('behavior', config)
    
    def test_config_get_set(self):
        """Test configuration get/set functionality."""
        self.config_manager.set('test.value', 'test_data')
        result = self.config_manager.get('test.value')
        self.assertEqual(result, 'test_data')

class TestAIToolManager(unittest.TestCase):
    """Test AI tool management."""
    
    def setUp(self):
        """Set up test environment."""
        from core.ai_tools import AIToolManager, AITool
        self.tool_manager = AIToolManager()
        self.AITool = AITool
    
    def test_default_tools_loaded(self):
        """Test that default AI tools are loaded."""
        tools = self.tool_manager.get_all_tools()
        self.assertGreaterEqual(len(tools), 9)  # Should have at least 9 tools
        
        # Check for specific tools
        tool_names = [tool.name for tool in tools]
        expected_tools = ['ChatGPT', 'Claude', 'Gemini', 'Perplexity', 'GitHub Copilot']
        for expected_tool in expected_tools:
            self.assertIn(expected_tool, tool_names)
    
    def test_add_remove_tool(self):
        """Test adding and removing tools."""
        test_tool = self.AITool("Test Tool", "https://test.com", description="Test tool")
        
        # Add tool
        self.tool_manager.add_tool(test_tool)
        self.assertIsNotNone(self.tool_manager.get_tool("Test Tool"))
        
        # Remove tool
        self.tool_manager.remove_tool("Test Tool")
        self.assertIsNone(self.tool_manager.get_tool("Test Tool"))
    
    def test_categories(self):
        """Test tool categories."""
        categories = self.tool_manager.get_categories()
        expected_categories = ['chat', 'search', 'coding', 'image', 'development']
        for category in expected_categories:
            self.assertIn(category, categories)

class TestCyberpunkTheme(unittest.TestCase):
    """Test cyberpunk theme functionality."""
    
    def setUp(self):
        """Set up test environment."""
        from ui.styles import CyberpunkTheme
        self.theme = CyberpunkTheme()
    
    def test_color_scheme(self):
        """Test that color scheme is properly defined."""
        colors = self.theme.COLORS
        required_colors = ['primary', 'secondary', 'background', 'surface', 'accent', 'text']
        for color in required_colors:
            self.assertIn(color, colors)
            self.assertTrue(colors[color].startswith('#'))  # Should be hex color
    
    def test_stylesheet_generation(self):
        """Test that stylesheets are generated."""
        stylesheet = self.theme.get_complete_stylesheet()
        self.assertIsInstance(stylesheet, str)
        self.assertGreater(len(stylesheet), 0)

if __name__ == '__main__':
    unittest.main()