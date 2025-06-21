# AI Interactive Tool Package
"""
AI Interactive Tool - MCP Server Implementation

This package provides a comprehensive Model Context Protocol (MCP) server
with advanced UI capabilities for AI-developer interactive.

Features:
- Modern PyQt5 UI with dark theme
- File and folder attachment system
- Image attachment with drag & drop
- Multi-language support (EN/VI)
- Workspace-aware path handling
- Continue conversation functionality
"""

from .description import AI_INTERACTIVE_DESCRIPTION

__version__ = "2.2.0"
__author__ = "DemonVN"
__email__ = "contact@demonvn.com"
__description__ = "AI Interactive Tool - Advanced MCP Server with UI"

# Core functionality
from .core import (
    ai_interactive_tool,
    get_tool_description,
    InputDialog,
    ConfigManager,
    ResponseFormatter
)

# UI Components
from .ui import (
    FileDialog,
    ImageAttachmentWidget,
    ImageViewer,
    FileTreeWidget,
    MODERN_DARK_STYLE
)

# Utilities
from .utils import (
    TranslationManager,
    FileUtils,
    ImageProcessor
)

# Export main components
__all__ = [
    # Core
    'ai_interactive_tool',
    'get_tool_description',
    'InputDialog',
    'ConfigManager', 
    'ResponseFormatter',
    
    # UI
    'FileDialog',
    'ImageAttachmentWidget',
    'ImageViewer',
    'FileTreeWidget',
    'MODERN_DARK_STYLE',
    
    # Utils
    'TranslationManager',
    'FileUtils',
    'ImageProcessor',
    
    # Metadata
    'AI_INTERACTIVE_DESCRIPTION',
    '__version__',
    '__author__',
    '__email__',
    '__description__'
]

def ai_interactive():
    """Entry point for the AI Interactive tool"""
    from .core.mcp_handler import ai_interactive_tool
    return ai_interactive_tool()