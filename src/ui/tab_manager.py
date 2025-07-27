"""Tab management system for AI Toolbar."""

from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QLabel, QTabBar
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon
from typing import Dict, Optional
import os

from ..core.web_engine import AIWebView, WebEngineManager
from ..core.ai_tools import AITool

class AITabWidget(QTabWidget):
    """Custom tab widget for AI tools."""
    
    # Signal emitted when a tab is requested to be closed
    tab_close_requested = pyqtSignal(int, str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setDocumentMode(True)
        
        # Connect signals
        self.tabCloseRequested.connect(self._on_tab_close_requested)
    
    def _on_tab_close_requested(self, index: int):
        """Handle tab close request."""
        tool_name = self.tabData(index)
        if tool_name:
            self.tab_close_requested.emit(index, tool_name)

class TabManager(QWidget):
    """Manages tabs for AI tools."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.web_manager = WebEngineManager()
        self.tabs: Dict[str, int] = {}  # tool_name -> tab_index
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the tab manager UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Create tab widget
        self.tab_widget = AITabWidget()
        self.tab_widget.tab_close_requested.connect(self.close_tab)
        layout.addWidget(self.tab_widget)
        
        # Create welcome tab
        self.create_welcome_tab()
    
    def create_welcome_tab(self):
        """Create a welcome tab when no AI tools are open."""
        welcome_widget = QWidget()
        layout = QVBoxLayout(welcome_widget)
        
        welcome_label = QLabel("""
        <h2 style='color: #58a6ff; text-align: center;'>Welcome to AI Toolbar</h2>
        <p style='color: #c9d1d9; text-align: center; font-size: 14px;'>
        Click on any AI tool button in the toolbar above to get started.<br><br>
        
        <b>Available Tools:</b><br>
        • ChatGPT, Gemini, Grok, Claude (Chatbots)<br>
        • Manus, Mini-Max (AI Agents)<br>
        • GitHub Copilot, Windsurf, AI Studio (Development Tools)<br><br>
        
        <b>Hotkeys:</b><br>
        • Alt + W: Show/Hide toolbar<br>
        • Click X on tabs to close them
        </p>
        """)
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setWordWrap(True)
        layout.addWidget(welcome_label)
        
        self.tab_widget.addTab(welcome_widget, "Welcome")
    
    def open_ai_tool(self, tool: AITool) -> int:
        """Open an AI tool in a new tab or switch to existing one.
        
        Args:
            tool: AITool instance to open
            
        Returns:
            Index of the tab
        """
        # Check if tool is already open
        if tool.name in self.tabs:
            tab_index = self.tabs[tool.name]
            self.tab_widget.setCurrentIndex(tab_index)
            return tab_index
        
        # Remove welcome tab if it's the only tab
        if self.tab_widget.count() == 1 and self.tab_widget.tabText(0) == "Welcome":
            self.tab_widget.removeTab(0)
        
        # Create web view for the tool
        web_view = self.web_manager.create_web_view(tool.name)
        web_view.load_ai_tool(tool.url)
        
        # Connect title change signal to update tab title
        web_view.titleChanged.connect(
            lambda title, name=tool.name: self._update_tab_title(name, title)
        )
        
        # Add tab
        tab_index = self.tab_widget.addTab(web_view, tool.name)
        self.tab_widget.setTabData(tab_index, tool.name)
        self.tabs[tool.name] = tab_index
        
        # Switch to new tab
        self.tab_widget.setCurrentIndex(tab_index)
        
        # Set icon if available
        icon_path = self._get_icon_path(tool.icon)
        if icon_path and os.path.exists(icon_path):
            self.tab_widget.setTabIcon(tab_index, QIcon(icon_path))
        
        return tab_index
    
    def close_tab(self, index: int, tool_name: str):
        """Close a tab and clean up resources."""
        # Remove from tabs dict
        if tool_name in self.tabs:
            del self.tabs[tool_name]
        
        # Remove web view
        self.web_manager.remove_web_view(tool_name)
        
        # Remove tab
        self.tab_widget.removeTab(index)
        
        # Update remaining tab indices
        self._update_tab_indices()
        
        # Show welcome tab if no tabs left
        if self.tab_widget.count() == 0:
            self.create_welcome_tab()
    
    def close_all_tabs(self):
        """Close all open tabs."""
        # Clear all tabs
        self.tab_widget.clear()
        self.tabs.clear()
        
        # Clear web views
        for tool_name in list(self.web_manager.get_all_web_views().keys()):
            self.web_manager.remove_web_view(tool_name)
        
        # Show welcome tab
        self.create_welcome_tab()
    
    def get_current_tool(self) -> Optional[str]:
        """Get the name of the currently active tool."""
        current_index = self.tab_widget.currentIndex()
        if current_index >= 0:
            return self.tab_widget.tabData(current_index)
        return None
    
    def get_open_tools(self) -> list:
        """Get list of currently open tool names."""
        return list(self.tabs.keys())
    
    def _update_tab_title(self, tool_name: str, title: str):
        """Update tab title when web page title changes."""
        if tool_name in self.tabs:
            tab_index = self.tabs[tool_name]
            # Show tool name and page title
            display_title = f"{tool_name}"
            if title and title != tool_name:
                display_title = f"{tool_name} - {title[:30]}..."
            self.tab_widget.setTabText(tab_index, display_title)
    
    def _update_tab_indices(self):
        """Update internal tab indices after tab removal."""
        new_tabs = {}
        for i in range(self.tab_widget.count()):
            tool_name = self.tab_widget.tabData(i)
            if tool_name:
                new_tabs[tool_name] = i
        self.tabs = new_tabs
    
    def _get_icon_path(self, icon_name: str) -> str:
        """Get full path to icon file."""
        icons_dir = os.path.join(
            os.path.dirname(__file__), '..', 'resources', 'icons'
        )
        return os.path.join(icons_dir, icon_name)