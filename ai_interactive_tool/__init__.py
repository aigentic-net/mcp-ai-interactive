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
    format_mixed_response,
    format_text_only_response,
    build_error_response,
    validate_response_data
)

# UI Components
from .ui import (
    FileAttachDialog,
    FileTreeView,
    FileSystemModel,
    FileTreeDelegate,
    ImageAttachmentWidget,
    DragDropImageWidget,
    get_main_stylesheet,
    get_file_dialog_stylesheet
)

# Utilities
from .utils import (
    get_translations,
    read_file_content,
    validate_file_path,
    process_images,
    validate_image_data,
    get_image_info
)

# Export main components
__all__ = [
    # Core
    'ai_interactive_tool',
    'get_tool_description',
    'InputDialog',
    'ConfigManager', 
    'format_mixed_response',
    'format_text_only_response',
    'build_error_response',
    'validate_response_data',
    
    # UI
    'FileAttachDialog',
    'FileTreeView',
    'FileSystemModel',
    'FileTreeDelegate',
    'ImageAttachmentWidget',
    'DragDropImageWidget',
    'get_main_stylesheet',
    'get_file_dialog_stylesheet',
    
    # Utils
    'get_translations',
    'read_file_content',
    'validate_file_path',
    'process_images',
    'validate_image_data',
    'get_image_info',
    
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