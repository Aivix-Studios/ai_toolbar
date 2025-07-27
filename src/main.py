"""Main entry point for AI Toolbar application."""

import sys
import os
import signal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from ui.main_window import AIToolbarMainWindow
from ui.styles import apply_cyberpunk_theme

def signal_handler(signum, frame):
    """Handle system signals gracefully."""
    QCoreApplication.quit()

def main():
    """Main application entry point."""
    # Handle system signals
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("AI Toolbar")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Aivix Studios")
    app.setOrganizationDomain("aivix.com")
    
    # Apply cyberpunk theme
    apply_cyberpunk_theme(app)
    
    # Create and show main window
    window = AIToolbarMainWindow()
    window.show()
    
    # Make sure the app can be interrupted by Ctrl+C
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    # Run application
    try:
        exit_code = app.exec_()
        
        # Save window state before exit
        window.save_window_state()
        
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\nShutting down AI Toolbar...")
        window.close_application()
        sys.exit(0)

if __name__ == "__main__":
    main()