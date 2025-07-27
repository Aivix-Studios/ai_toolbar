"""
Configuration Management for AI Toolbar

Handles loading, saving, and managing application configuration.
"""

import json
import os
from pathlib import Path

class ConfigManager:
    """Manages application configuration."""
    
    def __init__(self):
        """Initialize configuration manager."""
        self.config_file = self._get_config_path()
        self.config = {}
        self.default_config = self._get_default_config()
        
    def _get_config_path(self):
        """Get the configuration file path."""
        # Use user's home directory for config
        home_dir = Path.home()
        config_dir = home_dir / '.config' / 'ai-toolbar'
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir / 'config.json'
        
    def _get_default_config(self):
        """Get default configuration."""
        return {
            "window": {
                "width": 800,
                "height": 600,
                "always_on_top": True,
                "start_minimized": False,
                "remember_position": True,
                "x": 100,
                "y": 100
            },
            "theme": {
                "style": "cyberpunk",
                "primary_color": "#00FF41",
                "secondary_color": "#FF0080",
                "background_color": "#0D1117"
            },
            "hotkeys": {
                "toggle_toolbar": "ctrl+alt+t",
                "quick_chat": "ctrl+alt+c",
                "quick_search": "ctrl+alt+s"
            },
            "behavior": {
                "auto_hide": False,
                "hide_on_focus_lost": True,
                "startup_with_system": False
            }
        }
        
    def load_config(self):
        """Load configuration from file."""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
                # Merge with defaults for missing keys
                self.config = self._merge_with_defaults(self.config)
            else:
                self.config = self.default_config.copy()
                self.save_config()
        except Exception as e:
            print(f"Error loading config: {e}")
            self.config = self.default_config.copy()
            
    def save_config(self):
        """Save configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            print(f"Error saving config: {e}")
            
    def get(self, key, default=None):
        """Get configuration value by key."""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
        
    def set(self, key, value):
        """Set configuration value by key."""
        keys = key.split('.')
        config_ref = self.config
        for k in keys[:-1]:
            if k not in config_ref:
                config_ref[k] = {}
            config_ref = config_ref[k]
        config_ref[keys[-1]] = value
        
    def _merge_with_defaults(self, config):
        """Merge loaded config with default values."""
        def merge_dict(default, loaded):
            result = default.copy()
            for key, value in loaded.items():
                if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                    result[key] = merge_dict(result[key], value)
                else:
                    result[key] = value
            return result
        return merge_dict(self.default_config, config)