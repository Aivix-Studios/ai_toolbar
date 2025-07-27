"""Cyberpunk theme styles for AI Toolbar."""

# Main application stylesheet
CYBERPUNK_STYLE = """
/* Main Window */
QMainWindow {
    background-color: #0d1117;
    color: #c9d1d9;
    border: 1px solid #30363d;
}

/* Toolbar */
QToolBar {
    background-color: #161b22;
    border: none;
    border-bottom: 1px solid #21262d;
    spacing: 5px;
    padding: 5px;
}

QToolButton {
    background-color: #21262d;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 8px 12px;
    color: #c9d1d9;
    font-weight: bold;
    min-width: 80px;
}

QToolButton:hover {
    background-color: #30363d;
    border-color: #58a6ff;
    color: #58a6ff;
    box-shadow: 0 0 10px rgba(88, 166, 255, 0.3);
}

QToolButton:pressed {
    background-color: #1f6feb;
    border-color: #58a6ff;
    color: white;
}

/* Tab Widget */
QTabWidget::pane {
    border: 1px solid #30363d;
    background-color: #0d1117;
}

QTabBar::tab {
    background-color: #21262d;
    border: 1px solid #30363d;
    border-bottom: none;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    padding: 8px 16px;
    margin-right: 2px;
    color: #8b949e;
    min-width: 120px;
}

QTabBar::tab:selected {
    background-color: #0d1117;
    color: #58a6ff;
    border-color: #58a6ff;
    border-bottom: 1px solid #0d1117;
}

QTabBar::tab:hover:!selected {
    background-color: #30363d;
    color: #c9d1d9;
    border-color: #58a6ff;
}

QTabBar::close-button {
    image: url(close.png);
    subcontrol-position: right;
}

QTabBar::close-button:hover {
    background-color: #da3633;
    border-radius: 2px;
}

/* Menu Bar */
QMenuBar {
    background-color: #161b22;
    color: #c9d1d9;
    border-bottom: 1px solid #21262d;
}

QMenuBar::item {
    background-color: transparent;
    padding: 4px 8px;
}

QMenuBar::item:selected {
    background-color: #30363d;
    border-radius: 4px;
}

QMenu {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 6px;
}

QMenu::item {
    padding: 6px 12px;
    color: #c9d1d9;
}

QMenu::item:selected {
    background-color: #30363d;
    color: #58a6ff;
}

/* Status Bar */
QStatusBar {
    background-color: #161b22;
    color: #8b949e;
    border-top: 1px solid #21262d;
}

/* Scrollbars */
QScrollBar:vertical {
    background-color: #21262d;
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #484f58;
    border-radius: 6px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #58a6ff;
}

QScrollBar:horizontal {
    background-color: #21262d;
    height: 12px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background-color: #484f58;
    border-radius: 6px;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #58a6ff;
}

/* Buttons */
QPushButton {
    background-color: #21262d;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 6px 12px;
    color: #c9d1d9;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #30363d;
    border-color: #58a6ff;
    color: #58a6ff;
}

QPushButton:pressed {
    background-color: #1f6feb;
    border-color: #58a6ff;
    color: white;
}

/* Input Fields */
QLineEdit {
    background-color: #0d1117;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 6px 8px;
    color: #c9d1d9;
}

QLineEdit:focus {
    border-color: #58a6ff;
    box-shadow: 0 0 5px rgba(88, 166, 255, 0.3);
}

/* Tooltips */
QToolTip {
    background-color: #161b22;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 4px;
    padding: 4px 8px;
}
"""

# Category colors for AI tools
CATEGORY_COLORS = {
    'chatbot': '#58a6ff',    # Blue
    'agent': '#a5f3fc',      # Cyan  
    'low-code': '#7c3aed'    # Purple
}

def get_tool_button_style(category: str) -> str:
    """Get custom style for AI tool buttons based on category."""
    color = CATEGORY_COLORS.get(category, '#58a6ff')
    return f"""
    QToolButton {{
        background-color: #21262d;
        border: 1px solid #30363d;
        border-radius: 6px;
        padding: 8px 12px;
        color: #c9d1d9;
        font-weight: bold;
        min-width: 100px;
    }}
    
    QToolButton:hover {{
        background-color: #30363d;
        border-color: {color};
        color: {color};
        box-shadow: 0 0 10px rgba({_hex_to_rgb(color)}, 0.3);
    }}
    
    QToolButton:pressed {{
        background-color: {color};
        border-color: {color};
        color: white;
    }}
    """

def _hex_to_rgb(hex_color: str) -> str:
    """Convert hex color to RGB values for CSS."""
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"{r}, {g}, {b}"

def apply_cyberpunk_theme(app):
    """Apply cyberpunk theme to the application."""
    app.setStyleSheet(CYBERPUNK_STYLE)