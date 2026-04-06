from app.mcp.tool_registry import TOOLS


def call_tool(tool_name, data=None):
    # Check if tool exists
    if tool_name not in TOOLS:
        return {"error": f"Unknown tool: {tool_name}"}

    try:
        tool_function = TOOLS[tool_name]

        # If tool requires input
        if data is not None:
            result = tool_function(data)
        else:
            result = tool_function()

        return {"result": result}

    except Exception as e:
        return {"error": str(e)}