"""
AI Tools Definitions for AI Toolbar

Contains definitions and management for various AI tools.
"""

class AITool:
    """Represents a single AI tool."""
    
    def __init__(self, name, url, icon=None, description="", category="general", hotkey=None):
        """Initialize an AI tool."""
        self.name = name
        self.url = url
        self.icon = icon
        self.description = description
        self.category = category
        self.hotkey = hotkey
        self.is_active = False
        
    def to_dict(self):
        """Convert AI tool to dictionary."""
        return {
            'name': self.name,
            'url': self.url,
            'icon': self.icon,
            'description': self.description,
            'category': self.category,
            'hotkey': self.hotkey
        }
        
    @classmethod
    def from_dict(cls, data):
        """Create AI tool from dictionary."""
        return cls(
            name=data.get('name', ''),
            url=data.get('url', ''),
            icon=data.get('icon'),
            description=data.get('description', ''),
            category=data.get('category', 'general'),
            hotkey=data.get('hotkey')
        )

class AIToolManager:
    """Manages collection of AI tools."""
    
    def __init__(self):
        """Initialize AI tool manager."""
        self.tools = {}
        self.categories = set()
        self._load_default_tools()
        
    def _load_default_tools(self):
        """Load default AI tools."""
        default_tools = [
            AITool("ChatGPT", "https://chat.openai.com", description="OpenAI's conversational AI", category="chat"),
            AITool("Claude", "https://claude.ai", description="Anthropic's AI assistant", category="chat"),
            AITool("Gemini", "https://gemini.google.com", description="Google's AI model", category="chat"),
            AITool("Perplexity", "https://perplexity.ai", description="AI-powered search engine", category="search"),
            AITool("GitHub Copilot", "https://github.com/features/copilot", description="AI coding assistant", category="coding"),
            AITool("Midjourney", "https://midjourney.com", description="AI image generation", category="image"),
            AITool("DALL-E", "https://labs.openai.com", description="OpenAI's image generator", category="image"),
            AITool("Stable Diffusion", "https://stability.ai", description="Open-source image generation", category="image"),
            AITool("Hugging Face", "https://huggingface.co", description="AI model hub and tools", category="development")
        ]
        
        for tool in default_tools:
            self.add_tool(tool)
            
    def add_tool(self, tool):
        """Add an AI tool."""
        self.tools[tool.name] = tool
        self.categories.add(tool.category)
        
    def remove_tool(self, tool_name):
        """Remove an AI tool."""
        if tool_name in self.tools:
            del self.tools[tool_name]
            # Update categories
            self.categories = set(tool.category for tool in self.tools.values())
            
    def get_tool(self, tool_name):
        """Get a specific AI tool."""
        return self.tools.get(tool_name)
        
    def get_tools_by_category(self, category):
        """Get all tools in a specific category."""
        return [tool for tool in self.tools.values() if tool.category == category]
        
    def get_all_tools(self):
        """Get all AI tools."""
        return list(self.tools.values())
        
    def get_categories(self):
        """Get all tool categories."""
        return list(self.categories)
        
    def search_tools(self, query):
        """Search tools by name or description."""
        query = query.lower()
        results = []
        for tool in self.tools.values():
            if (query in tool.name.lower() or 
                query in tool.description.lower() or
                query in tool.category.lower()):
                results.append(tool)
        return results
        
    def export_tools(self):
        """Export tools to dictionary format."""
        return {name: tool.to_dict() for name, tool in self.tools.items()}
        
    def import_tools(self, tools_data):
        """Import tools from dictionary format."""
        for name, tool_data in tools_data.items():
            tool = AITool.from_dict(tool_data)
            self.add_tool(tool)