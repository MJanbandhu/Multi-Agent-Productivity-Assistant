from app.mcp.server import call_tool

def task_agent(query):
    query = query.lower()

    if "create task" in query or "add task" in query:
        title = query.replace("create task", "").replace("add task", "").strip()
        return call_tool("create_task", title)

    elif "show tasks" in query or "list tasks" in query:
        return call_tool("get_tasks")

    return "Task Agent: Unable to understand request"