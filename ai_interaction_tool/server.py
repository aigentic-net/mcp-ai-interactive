import argparse
from mcp.server.fastmcp import FastMCP
from .core import ai_interaction_tool, get_tool_description

def create_server():
    """Create and configure the MCP server instance"""
    mcp = FastMCP("AI Interaction")
    mcp.add_tool(ai_interaction_tool, description=get_tool_description())
    return mcp

def main():
    """Main entry point for the MCP server"""
    parser = argparse.ArgumentParser(description="AI Interaction MCP Server")
    parser.add_argument(
        "--transport", 
        default="stdio", 
        help="Transport mechanism (default: stdio)"
    )
    args = parser.parse_args()
    
    # Create and run the server
    server = create_server()
    server.run(transport=args.transport)

if __name__ == "__main__":
    main() 