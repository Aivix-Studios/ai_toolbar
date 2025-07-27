"""Main window for AI Toolbar application."""

from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QMenuBar, QStatusBar, QApplication, QSystemTrayIcon, 
                             QMenu, QAction, QMessageBox)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QSize
from PyQt5.QtGui import QIcon, QKeySequence, QCloseEvent
import sys
import os

from ..core.config import Config
from ..core.hotkeys import HotkeyManager
from ..core.ai_tools import AIToolsManager, AITool
from .toolbar import AIToolbar
from .tab_manager import TabManager
from .styles import apply_cyberpunk_theme

class AIToolbarMainWindow(QMainWindow):
    """Main window for the AI Toolbar application."""
    
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.tools_manager = AIToolsManager()
        self.hotkey_manager = HotkeyManager()
        self.is_hidden = False
        
        self.setup_ui()
        self.setup_hotkeys()
        self.setup_system_tray()
        self.apply_configuration()
    
    def setup_ui(self):
        """Set up the main user interface."""
        self.setWindowTitle("AI Toolbar")
        self.setMinimumSize(QSize(1000, 600))
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Create and add toolbar
        self.ai_toolbar = AIToolbar()
        self.ai_toolbar.tool_selected.connect(self.open_ai_tool)
        self.addToolBar(Qt.TopToolBarArea, self.ai_toolbar)
        
        # Create and add tab manager
        self.tab_manager = TabManager()
        layout.addWidget(self.tab_manager)
        
        # Create menu bar
        self.setup_menu_bar()
        
        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("AI Toolbar ready - Press Alt+W to toggle visibility")
        
        # Connect tab manager signals
        self.tab_manager.tab_widget.currentChanged.connect(self.on_tab_changed)
    
    def setup_menu_bar(self):
        """Set up the menu bar."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('File')
        
        # Close all tabs action
        close_all_action = QAction('Close All Tabs', self)
        close_all_action.setShortcut(QKeySequence.Close)
        close_all_action.triggered.connect(self.tab_manager.close_all_tabs)
        file_menu.addAction(close_all_action)
        
        file_menu.addSeparator()
        
        # Exit action
        exit_action = QAction('Exit', self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close_application)
        file_menu.addAction(exit_action)
        
        # View menu
        view_menu = menubar.addMenu('View')
        
        # Toggle toolbar action
        toggle_toolbar_action = QAction('Toggle Toolbar', self)
        toggle_toolbar_action.setCheckable(True)
        toggle_toolbar_action.setChecked(True)
        toggle_toolbar_action.triggered.connect(self.toggle_toolbar)
        view_menu.addAction(toggle_toolbar_action)
        
        # Always on top action
        always_on_top_action = QAction('Always on Top', self)
        always_on_top_action.setCheckable(True)
        always_on_top_action.setChecked(self.config.get('window.always_on_top', False))
        always_on_top_action.triggered.connect(self.toggle_always_on_top)
        view_menu.addAction(always_on_top_action)
        
        # Tools menu
        tools_menu = menubar.addMenu('Tools')
        
        # Add actions for each AI tool
        for tool in self.tools_manager.get_tools():
            action = QAction(f"Open {tool.name}", self)
            action.triggered.connect(lambda checked, t=tool: self.open_ai_tool(t))
            tools_menu.addAction(action)
        
        # Help menu
        help_menu = menubar.addMenu('Help')
        
        # About action
        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def setup_hotkeys(self):
        """Set up global hotkeys."""
        hotkey = self.config.get('hotkey.show_hide', 'alt+w')
        if self.config.get('hotkey.enabled', True):
            self.hotkey_manager.register_hotkey(hotkey, self.toggle_visibility)
            self.hotkey_manager.hotkey_pressed.connect(self.on_hotkey_pressed)
    
    def setup_system_tray(self):
        """Set up system tray icon."""
        if QSystemTrayIcon.isSystemTrayAvailable():
            self.tray_icon = QSystemTrayIcon(self)
            
            # Set icon (use a default icon for now)
            self.tray_icon.setIcon(self.style().standardIcon(self.style().SP_ComputerIcon))
            
            # Create tray menu
            tray_menu = QMenu()
            
            show_action = QAction("Show", self)
            show_action.triggered.connect(self.show_window)
            tray_menu.addAction(show_action)
            
            hide_action = QAction("Hide", self)
            hide_action.triggered.connect(self.hide_window)
            tray_menu.addAction(hide_action)
            
            tray_menu.addSeparator()
            
            quit_action = QAction("Quit", self)
            quit_action.triggered.connect(self.close_application)
            tray_menu.addAction(quit_action)
            
            self.tray_icon.setContextMenu(tray_menu)
            self.tray_icon.activated.connect(self.on_tray_icon_activated)
            self.tray_icon.show()
        else:
            self.tray_icon = None
    
    def apply_configuration(self):
        """Apply configuration settings."""
        # Window size
        width = self.config.get('window.width', 1200)
        height = self.config.get('window.height', 800)
        self.resize(width, height)
        
        # Window opacity
        opacity = self.config.get('window.opacity', 0.95)
        self.setWindowOpacity(opacity)
        
        # Always on top
        if self.config.get('window.always_on_top', False):
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
    
    def open_ai_tool(self, tool: AITool):
        """Open an AI tool in a new tab."""
        self.tab_manager.open_ai_tool(tool)
        self.status_bar.showMessage(f"Opened {tool.name}")
        
        # Highlight the active tool in toolbar
        self.ai_toolbar.highlight_active_tool(tool.name)
    
    def on_tab_changed(self, index: int):
        """Handle tab change."""
        if index >= 0:
            tool_name = self.tab_manager.tab_widget.tabData(index)
            if tool_name and tool_name != "Welcome":
                self.ai_toolbar.highlight_active_tool(tool_name)
                self.status_bar.showMessage(f"Active: {tool_name}")
            else:
                self.ai_toolbar.clear_highlights()
                self.status_bar.showMessage("AI Toolbar ready")
        else:
            self.ai_toolbar.clear_highlights()
    
    def toggle_visibility(self):
        """Toggle window visibility."""
        if self.isVisible() and not self.is_hidden:
            self.hide_window()
        else:
            self.show_window()
    
    def show_window(self):
        """Show the window."""
        self.show()
        self.raise_()
        self.activateWindow()
        self.is_hidden = False
    
    def hide_window(self):
        """Hide the window."""
        self.hide()
        self.is_hidden = True
    
    def on_hotkey_pressed(self, hotkey: str):
        """Handle hotkey press."""
        if hotkey == self.config.get('hotkey.show_hide', 'alt+w'):
            self.toggle_visibility()
    
    def on_tray_icon_activated(self, reason):
        """Handle tray icon activation."""
        if reason == QSystemTrayIcon.DoubleClick:
            self.toggle_visibility()
    
    def toggle_toolbar(self, checked: bool):
        """Toggle toolbar visibility."""
        self.ai_toolbar.setVisible(checked)
    
    def toggle_always_on_top(self, checked: bool):
        """Toggle always on top setting."""
        if checked:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        self.show()  # Required to apply window flags
        
        # Save setting
        self.config.set('window.always_on_top', checked)
        self.config.save_config()
    
    def show_about(self):
        """Show about dialog."""
        QMessageBox.about(self, "About AI Toolbar", 
                         "AI Toolbar v1.0.0\n\n"
                         "A minimalist desktop toolbar for quick access to AI tools.\n\n"
                         "Hotkeys:\n"
                         "• Alt + W: Show/Hide toolbar\n\n"
                         "© 2024 Aivix Studios")
    
    def close_application(self):
        """Close the application completely."""
        self.hotkey_manager.stop_listener()
        QApplication.quit()
    
    def closeEvent(self, event: QCloseEvent):
        """Handle window close event."""
        if self.tray_icon and self.tray_icon.isVisible():
            # Hide to tray instead of closing
            event.ignore()
            self.hide_window()
            if not hasattr(self, '_tray_message_shown'):
                self.tray_icon.showMessage(
                    "AI Toolbar",
                    "Application is still running in the system tray. "
                    "Right-click the tray icon to quit.",
                    QSystemTrayIcon.Information,
                    3000
                )
                self._tray_message_shown = True
        else:
            # No tray, close application
            self.close_application()
            event.accept()
    
    def save_window_state(self):
        """Save current window state to configuration."""
        self.config.set('window.width', self.width())
        self.config.set('window.height', self.height())
        self.config.save_config()