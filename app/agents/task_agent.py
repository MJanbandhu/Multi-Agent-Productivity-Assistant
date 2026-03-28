from mcp.server import call_tool

def handle_task(query):
    query = query.lower()

    # Create Task
    if "create task" in query or "add task" in query:
        title = query.replace("create task", "").replace("add task", "").strip()
        return call_tool("create_task", title)

    # Get Tasks
    elif "show tasks" in query or "list tasks" in query:
        return call_tool("get_tasks")

    return "Task Agent: Unable to understand request"