from mcp.tool_registry import TOOLS

def call_tool(tool_name, *args):
    if tool_name in TOOLS:
        return TOOLS[tool_name](*args)
    return "Tool not found"