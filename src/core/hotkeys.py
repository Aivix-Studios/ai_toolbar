"""Global hotkey handling for AI Toolbar."""

import threading
from pynput import keyboard
from PyQt5.QtCore import QObject, pyqtSignal
from typing import Callable, Dict, Set

class HotkeyManager(QObject):
    """Manages global hotkeys for the application."""
    
    # Signal emitted when hotkey is pressed
    hotkey_pressed = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.listener = None
        self.hotkeys: Dict[str, Callable] = {}
        self.pressed_keys: Set[str] = set()
        self.running = False
    
    def register_hotkey(self, hotkey: str, callback: Callable = None):
        """Register a global hotkey.
        
        Args:
            hotkey: Hotkey combination (e.g., 'alt+w', 'ctrl+shift+t')
            callback: Optional callback function to call when hotkey is pressed
        """
        hotkey = hotkey.lower().replace(' ', '')
        self.hotkeys[hotkey] = callback
        
        if not self.running:
            self.start_listener()
    
    def unregister_hotkey(self, hotkey: str):
        """Unregister a global hotkey."""
        hotkey = hotkey.lower().replace(' ', '')
        if hotkey in self.hotkeys:
            del self.hotkeys[hotkey]
    
    def start_listener(self):
        """Start the global hotkey listener."""
        if self.running:
            return
        
        self.running = True
        try:
            self.listener = keyboard.Listener(
                on_press=self._on_key_press,
                on_release=self._on_key_release
            )
            self.listener.start()
        except Exception as e:
            print(f"Failed to start hotkey listener: {e}")
            self.running = False
    
    def stop_listener(self):
        """Stop the global hotkey listener."""
        if self.listener and self.running:
            self.listener.stop()
            self.running = False
    
    def _on_key_press(self, key):
        """Handle key press events."""
        try:
            key_name = self._get_key_name(key)
            self.pressed_keys.add(key_name)
            
            # Check for hotkey matches
            for hotkey, callback in self.hotkeys.items():
                if self._check_hotkey_match(hotkey):
                    self.hotkey_pressed.emit(hotkey)
                    if callback:
                        callback()
                    break
        except Exception as e:
            print(f"Error in key press handler: {e}")
    
    def _on_key_release(self, key):
        """Handle key release events."""
        try:
            key_name = self._get_key_name(key)
            self.pressed_keys.discard(key_name)
        except Exception as e:
            print(f"Error in key release handler: {e}")
    
    def _get_key_name(self, key) -> str:
        """Convert key object to standardized string name."""
        if hasattr(key, 'char') and key.char:
            return key.char.lower()
        elif hasattr(key, 'name'):
            name = key.name.lower()
            # Standardize modifier key names
            if name == 'alt_l' or name == 'alt_r':
                return 'alt'
            elif name == 'ctrl_l' or name == 'ctrl_r':
                return 'ctrl'
            elif name == 'shift_l' or name == 'shift_r':
                return 'shift'
            elif name == 'cmd' or name == 'cmd_l' or name == 'cmd_r':
                return 'cmd'
            return name
        else:
            return str(key).lower()
    
    def _check_hotkey_match(self, hotkey: str) -> bool:
        """Check if the current pressed keys match a hotkey."""
        hotkey_parts = set(hotkey.split('+'))
        return hotkey_parts.issubset(self.pressed_keys)
    
    def is_running(self) -> bool:
        """Check if the hotkey listener is running."""
        return self.running