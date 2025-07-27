"""Configuration management for AI Toolbar."""

import json
import os
from typing import Dict, Any

class Config:
    """Configuration manager for AI Toolbar."""
    
    def __init__(self, config_path: str = None):
        if config_path is None:
            # Default config path
            config_dir = os.path.expanduser("~/.config/ai-toolbar")
            os.makedirs(config_dir, exist_ok=True)
            self.config_path = os.path.join(config_dir, "config.json")
        else:
            self.config_path = config_path
        
        self.default_config_path = os.path.join(
            os.path.dirname(__file__), '..', 'resources', 'config.json'
        )
        self._config = {}
        self.load_config()
    
    def load_config(self):
        """Load configuration from file."""
        # First try user config
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as f:
                    self._config = json.load(f)
                return
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        # Fall back to default config
        try:
            with open(self.default_config_path, 'r') as f:
                self._config = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            # Use hardcoded defaults
            self._config = self._get_default_config()
    
    def save_config(self):
        """Save configuration to file."""
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        with open(self.config_path, 'w') as f:
            json.dump(self._config, f, indent=4)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key (supports dot notation)."""
        keys = key.split('.')
        value = self._config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
    
    def set(self, key: str, value: Any):
        """Set configuration value by key (supports dot notation)."""
        keys = key.split('.')
        config = self._config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Return default configuration."""
        return {
            "window": {
                "width": 1200,
                "height": 800,
                "always_on_top": False,
                "opacity": 0.95
            },
            "hotkey": {
                "show_hide": "alt+w",
                "enabled": True
            },
            "appearance": {
                "theme": "cyberpunk",
                "show_toolbar": True,
                "show_tabs": True
            },
            "autostart": False,
            "minimize_to_panel": True
        }