from app.mcp.tool_registry import TOOLS


def call_tool(tool_name, data):
    if tool_name == "task":
        return {"message": f"Task tool executed with {data}"}
    
    elif tool_name == "calendar":
        return {"message": f"Calendar tool executed with {data}"}
    
    elif tool_name == "notes":
        return {"message": f"Notes tool executed with {data}"}
    
    else:
        return {"error": "Unknown tool"}