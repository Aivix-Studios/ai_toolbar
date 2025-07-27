"""AI Tools definitions and configurations."""

from dataclasses import dataclass
from typing import List
import json
import os

@dataclass
class AITool:
    """Represents an AI tool with its configuration."""
    name: str
    url: str
    icon: str
    category: str

class AIToolsManager:
    """Manages AI tools configuration and access."""
    
    def __init__(self, config_path: str = None):
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'config.json')
        self.config_path = config_path
        self._tools = []
        self.load_tools()
    
    def load_tools(self):
        """Load AI tools from configuration file."""
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
                self._tools = [
                    AITool(**tool_config) 
                    for tool_config in config.get('ai_tools', [])
                ]
        except FileNotFoundError:
            # Use default tools if config file not found
            self._tools = self._get_default_tools()
    
    def _get_default_tools(self) -> List[AITool]:
        """Return default AI tools configuration."""
        return [
            AITool("ChatGPT", "https://chat.openai.com", "chatgpt.svg", "chatbot"),
            AITool("Gemini", "https://gemini.google.com", "gemini.svg", "chatbot"),
            AITool("Grok", "https://x.ai/grok", "grok.svg", "chatbot"),
            AITool("Claude", "https://claude.ai", "claude.svg", "chatbot"),
            AITool("Manus", "https://manus.chat", "manus.svg", "agent"),
            AITool("Mini-Max", "https://minimax.chat", "minimax.svg", "agent"),
            AITool("GitHub Copilot", "https://copilot.github.com", "github-copilot.svg", "low-code"),
            AITool("Windsurf", "https://codeium.com/windsurf", "windsurf.svg", "low-code"),
            AITool("AI Studio", "https://aistudio.google.com", "ai-studio.svg", "low-code"),
        ]
    
    def get_tools(self) -> List[AITool]:
        """Get all AI tools."""
        return self._tools
    
    def get_tools_by_category(self, category: str) -> List[AITool]:
        """Get AI tools filtered by category."""
        return [tool for tool in self._tools if tool.category == category]
    
    def get_tool_by_name(self, name: str) -> AITool:
        """Get an AI tool by name."""
        for tool in self._tools:
            if tool.name == name:
                return tool
        return None