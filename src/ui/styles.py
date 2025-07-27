"""
Cyberpunk Styling for AI Toolbar

Contains QSS styles and theme management for the cyberpunk aesthetic.
"""

class CyberpunkTheme:
    """Cyberpunk theme styling for AI Toolbar."""
    
    # Color scheme
    COLORS = {
        'primary': '#00FF41',      # Matrix green
        'secondary': '#FF0080',    # Cyberpunk pink
        'background': '#0D1117',   # Dark background
        'surface': '#161B22',      # Surface color
        'accent': '#00D4FF',       # Electric blue
        'text': '#C9D1D9',         # Light text
        'hover': '#21262D',        # Hover state
        'border': '#30363D',       # Border color
    }
    
    def __init__(self):
        """Initialize the cyberpunk theme."""
        self.main_style = self._create_main_style()
        self.button_style = self._create_button_style()
        self.toolbar_style = self._create_toolbar_style()
        
    def _create_main_style(self):
        """Create main window styling."""
        return f"""
        QMainWindow {{
            background-color: {self.COLORS['background']};
            color: {self.COLORS['text']};
            border: 1px solid {self.COLORS['border']};
        }}
        """
        
    def _create_button_style(self):
        """Create button styling."""
        return f"""
        QPushButton {{
            background-color: {self.COLORS['surface']};
            color: {self.COLORS['text']};
            border: 1px solid {self.COLORS['primary']};
            border-radius: 5px;
            padding: 8px 16px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: {self.COLORS['hover']};
            border-color: {self.COLORS['accent']};
            color: {self.COLORS['accent']};
        }}
        QPushButton:pressed {{
            background-color: {self.COLORS['primary']};
            color: {self.COLORS['background']};
        }}
        """
        
    def _create_toolbar_style(self):
        """Create toolbar styling."""
        return f"""
        QToolBar {{
            background-color: {self.COLORS['surface']};
            border: 1px solid {self.COLORS['border']};
            spacing: 5px;
        }}
        """
        
    def get_complete_stylesheet(self):
        """Get the complete stylesheet for the application."""
        return self.main_style + self.button_style + self.toolbar_style
        
    def apply_theme(self, application):
        """Apply the cyberpunk theme to the application."""
        # TODO: Apply stylesheet to PyQt5 application
        pass