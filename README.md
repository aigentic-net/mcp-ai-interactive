# MCP Server AI Interactive

**Modern AI interaction tool with advanced UI and powerful features for Model Context Protocol (MCP)**

A comprehensive MCP server that provides an interactive UI popup system for enhanced AI communication, complete with file/folder attachment, image support, and advanced cognitive enhancement features.

## 🚀 Quick Installation

### Using uvx (Recommended)
```bash
# Install and run directly
uvx mcp-server-ai-interactive
```

### Using pip
```bash
# Install the package
pip install mcp-server-ai-interactive

# Run the server
mcp-server-ai-interactive
```

### Using python -m
```bash
# After installing, run as a module
python -m ai_interaction_tool
```

## 📋 MCP Client Configuration

Add this to your MCP client configuration file:

### Claude Desktop Configuration
**Config file paths:**
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/claude/claude_desktop_config.json`

**Configuration:**
```json
{
  "mcpServers": {
    "ai-interactive": {
      "command": "uvx",
      "args": ["mcp-server-ai-interactive"]
    }
  }
}
```

### Alternative configurations:

**Using pip installation:**
```json
{
  "mcpServers": {
    "ai-interactive": {
      "command": "mcp-server-ai-interactive"
    }
  }
}
```

**Using python module:**
```json
{
  "mcpServers": {
    "ai-interactive": {
      "command": "python",
      "args": ["-m", "ai_interaction_tool"]
    }
  }
}
```

### Cursor IDE Configuration
For Cursor IDE users:
1. Open Command Palette (`Cmd/Ctrl + Shift + P`)
2. Search "Configure MCP Servers"
3. Add the ai-interactive server configuration above

## 🎯 Core Features

### 🖥️ Interactive UI System
- **Modern PyQt5 Interface** with responsive design
- **Content Input Dialog** with formatting support
- **Multi-language Support** (English/Vietnamese)
- **Conversation Control** with continue chat options

### 📁 File & Folder Attachment
- **Workspace Integration** with intelligent path processing
- **Drag & Drop Support** for easy file attachment
- **File Tree View** with context menu operations
- **Cross-project Compatibility** with workspace-aware paths

### 🖼️ Image Attachment System (v2.2.0)
- **Drag & Drop Images** directly into the UI
- **Multi-image Support** with preview and management
- **Format Support**: PNG, JPG, JPEG, GIF, BMP, WEBP
- **Secure Storage** in local `user_images/` directory
- **Base64 Encoding** for AI processing
- **Preview System** with click-to-enlarge
- **Persistent State** with save options

### 🧠 Cognitive Enhancement
- **Maximum Cognitive Power** activation
- **Tag-based Output Format** for AI agent integration
- **Ultra-Enhancement Modes** with 10 breakthrough cognitive modes
- **Thinking Protocols** for quality responses

## 🔧 Development Setup

### Prerequisites
- **Python 3.8+** (Python 3.10+ recommended)
- **PyQt5** for UI components
- **Modern display** (1024x768 minimum, 1920x1080+ recommended)

### Local Development
```bash
# Clone the repository
git clone <repository-url>
cd mcp-ai-interactive

# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Run the server
mcp-server-ai-interactive
```

### Using uv (Performance Optimized)
```bash
# Install uv if not already installed
pip install uv

# Install dependencies with uv
uv pip install -r requirements.txt

# Install in development mode
uv pip install -e .
```

## 🎮 Usage Guide

### AI Interaction Tool
The main tool provides an interactive popup interface:

```python
# The tool is automatically available in MCP clients
# Call "ai_interaction" to launch the UI
```

**Features:**
- Input complex content with formatting
- Attach files/folders from workspace
- Attach multiple images with drag & drop
- Control AI thinking modes and reasoning levels
- Multi-language interface support

### Output Format
The tool uses structured tag-based output:

```
User message content with natural line breaks

<AI_INTERACTION_ATTACHED_FILES>
FOLDERS:
- workspace_name/relative/path/to/folder

FILES:
- workspace_name/relative/path/to/file.js
</AI_INTERACTION_ATTACHED_FILES>

<AI_INTERACTION_WORKSPACE>workspace_name</AI_INTERACTION_WORKSPACE>
<AI_INTERACTION_CONTINUE_CHAT>true/false</AI_INTERACTION_CONTINUE_CHAT>
```

## 🧠 AI Agent Integration (REQUIRED)

**For optimal AI agent operation, you MUST configure custom instructions:**

### Setup Custom Instructions
1. **Access Settings** in your AI client (Claude Desktop/Cursor)
2. **Find Custom Instructions** section
3. **Copy content** from rule files:
   - **English**: `rule_for_ai_EN.txt`
   - **Vietnamese**: `rule_for_ai_VI.txt`
4. **Paste and save** the rules

### Why This is Essential
- ✅ **Behavioral Framework**: Defines how AI processes tool output
- ✅ **Thinking Protocols**: Activates enhanced reasoning patterns
- ✅ **Tag Processing**: Handles control tags and continuation logic
- ✅ **Cognitive Enhancement**: Unlocks maximum AI performance

### Quick Setup Commands
```bash
# View English rules
cat rule_for_ai_EN.txt

# Copy to clipboard (macOS)
cat rule_for_ai_EN.txt | pbcopy

# Copy to clipboard (Linux)
cat rule_for_ai_EN.txt | xclip -selection clipboard

# Copy to clipboard (Windows)
type rule_for_ai_EN.txt | clip
```

## 📦 Package Structure

```
mcp-ai-interactive/
├── ai_interaction_tool/       # Main package
│   ├── core/                 # Core dialog and configuration
│   │   ├── dialog.py         # Main UI dialog
│   │   └── config.py         # Configuration management
│   ├── ui/                   # Interface components
│   │   ├── file_dialog.py    # File attachment dialogs
│   │   ├── file_tree.py      # File system tree view
│   │   ├── image_attachment.py # Image attachment system
│   │   └── styles.py         # UI styling
│   ├── utils/                # Utilities
│   │   ├── translations.py   # Multi-language support
│   │   └── file_utils.py     # File operations
│   ├── cli.py               # CLI entry point
│   ├── server.py            # MCP server implementation
│   ├── engine.py            # Main engine
│   └── __init__.py          # Package exports
├── user_images/             # Secure image storage
├── requirements.txt         # Dependencies
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## 🔧 Troubleshooting

### Common Issues

**"Command not found" error:**
- Ensure Python is in PATH
- Try `python -m ai_interaction_tool` instead
- Reinstall with `pip install -e .` for development

**"Module not found" error:**
- Run `pip install -r requirements.txt`
- Check virtual environment activation
- For uv users: `uv pip install -e .`

**UI not displaying:**
- Verify PyQt5 installation: `pip install PyQt5`
- Check display environment variables
- Try running with `--transport stdio` flag

**Image attachment issues:**
- Check `user_images/` directory permissions
- Verify supported formats: PNG, JPG, JPEG, GIF, BMP, WEBP
- Clear config: Remove `last_attached_images` from config.json

**MCP Connection Issues:**
- Restart AI client after configuration changes
- Verify JSON syntax in config file
- Check server process: `ps aux | grep mcp-server-ai-interactive`

### Debug Mode
Run server directly for debugging:
```bash
mcp-server-ai-interactive --transport stdio
```

## 🔄 Version History

- **v2.2.0** (Latest): 🖼️ **Image Attachment System** - Complete image support with drag & drop, multi-image management, security enhancements
- **v2.1.0**: Enhanced UI/UX, Cursor IDE integration, Debounce configuration
- **v2.0.0**: Refactored architecture with modern PyQt5 UI
- **v1.x**: Core functionality and basic features

## 🌟 System Requirements

### Minimum Requirements
- **OS**: Windows 10+ / macOS 10.14+ / Ubuntu 18.04+
- **Python**: 3.8 or higher
- **RAM**: 512MB available
- **Storage**: 100MB free space
- **Display**: 1024x768 minimum

### Recommended Setup
- **OS**: Windows 11 / macOS 12+ / Ubuntu 20.04+
- **Python**: 3.10+ with virtual environment
- **RAM**: 2GB available
- **Storage**: 500MB free space
- **Display**: 1920x1080 or higher

## 🛡️ Security & Privacy

- **Local Processing**: All operations are local-only, no external uploads
- **Secure Storage**: Images stored safely in `user_images/` directory
- **Path Validation**: Robust security checks for file access
- **No Data Collection**: Zero telemetry or external data transmission
- **User Control**: Complete control over file and image attachments

## 🤝 Contributing

This is a private repository. For suggestions or issues:
1. Create detailed issue reports
2. Provide reproduction steps
3. Include system information
4. Attach relevant logs or screenshots

## 📚 Documentation & Resources

### Documentation Files
- `rule_for_ai_VI.txt` - Vietnamese agent behavior rules
- `rule_for_ai_EN.txt` - English agent behavior rules
- `pyproject.toml` - Project configuration

### Useful Links
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [Claude Desktop Official Guide](https://claude.ai/desktop)
- [Cursor IDE Official Site](https://cursor.sh/)
- [PyQt5 Documentation](https://doc.qt.io/qtforpython-5/)

## 📄 License

MIT License

Copyright (c) 2025 DemonVN - AI Interaction Tool

---

**🚀 Happy Coding with MCP Server AI Interactive!**

*For support, issues, or feature requests, please open an issue on the GitHub repository.*
