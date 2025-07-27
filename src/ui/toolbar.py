"""Toolbar component for AI tools."""

from PyQt5.QtWidgets import (QToolBar, QToolButton, QAction, QWidget, 
                             QHBoxLayout, QLabel, QSizePolicy)
from PyQt5.QtCore import pyqtSignal, Qt, QSize
from PyQt5.QtGui import QIcon, QFont
from typing import List, Dict
import os

from ..core.ai_tools import AITool, AIToolsManager
from .styles import get_tool_button_style, CATEGORY_COLORS

class AIToolButton(QToolButton):
    """Custom tool button for AI tools."""
    
    # Signal emitted when tool is clicked
    tool_clicked = pyqtSignal(AITool)
    
    def __init__(self, tool: AITool, parent=None):
        super().__init__(parent)
        self.tool = tool
        self.setup_button()
    
    def setup_button(self):
        """Set up the button appearance and behavior."""
        self.setText(self.tool.name)
        self.setToolTip(f"Open {self.tool.name}\n{self.tool.url}")
        self.setMinimumSize(QSize(100, 40))
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        
        # Set icon if available
        icon_path = self._get_icon_path()
        if icon_path and os.path.exists(icon_path):
            self.setIcon(QIcon(icon_path))
            self.setIconSize(QSize(24, 24))
            self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        else:
            self.setToolButtonStyle(Qt.ToolButtonTextOnly)
        
        # Apply category-specific styling
        self.setStyleSheet(get_tool_button_style(self.tool.category))
        
        # Connect click signal
        self.clicked.connect(lambda: self.tool_clicked.emit(self.tool))
    
    def _get_icon_path(self) -> str:
        """Get full path to the tool's icon."""
        icons_dir = os.path.join(
            os.path.dirname(__file__), '..', 'resources', 'icons'
        )
        return os.path.join(icons_dir, self.tool.icon)

class CategorySeparator(QWidget):
    """Visual separator between tool categories."""
    
    def __init__(self, category: str, parent=None):
        super().__init__(parent)
        self.category = category
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the separator UI."""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        
        # Category label
        label = QLabel(self.category.replace('-', ' ').title())
        label.setStyleSheet(f"""
            QLabel {{
                color: {CATEGORY_COLORS.get(self.category, '#58a6ff')};
                font-weight: bold;
                font-size: 12px;
                padding: 2px 8px;
                background-color: #21262d;
                border-radius: 3px;
                border: 1px solid {CATEGORY_COLORS.get(self.category, '#58a6ff')};
            }}
        """)
        layout.addWidget(label)

class AIToolbar(QToolBar):
    """Main toolbar containing AI tool buttons."""
    
    # Signal emitted when an AI tool is selected
    tool_selected = pyqtSignal(AITool)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tools_manager = AIToolsManager()
        self.tool_buttons: Dict[str, AIToolButton] = {}
        self.setup_toolbar()
    
    def setup_toolbar(self):
        """Set up the toolbar with AI tool buttons."""
        self.setMovable(False)
        self.setFloatable(False)
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.setIconSize(QSize(24, 24))
        
        # Group tools by category
        tools_by_category = {}
        for tool in self.tools_manager.get_tools():
            if tool.category not in tools_by_category:
                tools_by_category[tool.category] = []
            tools_by_category[tool.category].append(tool)
        
        # Add tools grouped by category
        categories = ['chatbot', 'agent', 'low-code']
        for i, category in enumerate(categories):
            if category in tools_by_category:
                # Add category separator
                if i > 0:  # Don't add separator before first category
                    self.addSeparator()
                
                separator = CategorySeparator(category)
                self.addWidget(separator)
                
                # Add tools in this category
                for tool in tools_by_category[category]:
                    self.add_tool_button(tool)
        
        # Add spacer to push everything to the left
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.addWidget(spacer)
        
        # Add utility buttons
        self.add_utility_buttons()
    
    def add_tool_button(self, tool: AITool):
        """Add a button for an AI tool."""
        button = AIToolButton(tool)
        button.tool_clicked.connect(self.tool_selected.emit)
        self.tool_buttons[tool.name] = button
        self.addWidget(button)
    
    def add_utility_buttons(self):
        """Add utility buttons to the toolbar."""
        # Settings button
        settings_action = QAction("Settings", self)
        settings_action.setToolTip("Open settings")
        settings_action.triggered.connect(self.show_settings)
        self.addAction(settings_action)
        
        # Close all tabs button
        close_all_action = QAction("Close All", self)
        close_all_action.setToolTip("Close all open tabs")
        close_all_action.triggered.connect(self.close_all_tabs)
        self.addAction(close_all_action)
    
    def get_tool_button(self, tool_name: str) -> AIToolButton:
        """Get tool button by name."""
        return self.tool_buttons.get(tool_name)
    
    def highlight_active_tool(self, tool_name: str):
        """Highlight the active tool button."""
        # Reset all buttons
        for name, button in self.tool_buttons.items():
            if name == tool_name:
                # Highlight active button
                button.setStyleSheet(f"""
                    QToolButton {{
                        background-color: {CATEGORY_COLORS.get(button.tool.category, '#58a6ff')};
                        border: 1px solid {CATEGORY_COLORS.get(button.tool.category, '#58a6ff')};
                        color: white;
                        font-weight: bold;
                    }}
                """)
            else:
                # Reset inactive buttons
                button.setStyleSheet(get_tool_button_style(button.tool.category))
    
    def clear_highlights(self):
        """Clear all button highlights."""
        for button in self.tool_buttons.values():
            button.setStyleSheet(get_tool_button_style(button.tool.category))
    
    def show_settings(self):
        """Show settings dialog."""
        # TODO: Implement settings dialog
        print("Settings clicked - TODO: Implement settings dialog")
    
    def close_all_tabs(self):
        """Signal to close all tabs."""
        # This will be connected to the main window's close_all_tabs method
        pass