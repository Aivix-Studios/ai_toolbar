"""Web engine integration for AI Toolbar."""

from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineSettings
from PyQt5.QtCore import QUrl, pyqtSignal
from PyQt5.QtWidgets import QWidget

class AIWebView(QWebEngineView):
    """Custom web view for AI tools."""
    
    # Signal emitted when title changes
    titleChanged = pyqtSignal(str)
    
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setup_web_engine()
        
        # Connect signals
        self.page().titleChanged.connect(self.titleChanged.emit)
    
    def setup_web_engine(self):
        """Configure web engine settings."""
        # Get the default profile
        profile = QWebEngineProfile.defaultProfile()
        
        # Configure settings for better AI tool compatibility
        settings = self.settings()
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        settings.setAttribute(QWebEngineSettings.AutoLoadImages, True)
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        settings.setAttribute(QWebEngineSettings.AllowRunningInsecureContent, False)
        
        # Set user agent to appear as a regular browser
        profile.setHttpUserAgent(
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
    
    def load_ai_tool(self, url: str):
        """Load an AI tool URL."""
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        self.load(QUrl(url))
    
    def get_current_url(self) -> str:
        """Get current URL as string."""
        return self.url().toString()
    
    def get_current_title(self) -> str:
        """Get current page title."""
        return self.title()

class WebEngineManager:
    """Manages web engine instances and settings."""
    
    def __init__(self):
        self.web_views = {}
    
    def create_web_view(self, tool_name: str) -> AIWebView:
        """Create a new web view for an AI tool."""
        web_view = AIWebView()
        self.web_views[tool_name] = web_view
        return web_view
    
    def get_web_view(self, tool_name: str) -> AIWebView:
        """Get existing web view for a tool."""
        return self.web_views.get(tool_name)
    
    def remove_web_view(self, tool_name: str):
        """Remove web view for a tool."""
        if tool_name in self.web_views:
            del self.web_views[tool_name]
    
    def get_all_web_views(self) -> dict:
        """Get all web views."""
        return self.web_views.copy()