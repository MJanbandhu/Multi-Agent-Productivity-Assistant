from app.mcp.server import call_tool
from datetime import datetime

def calendar_agent(query):
    query = query.lower()

    if "schedule" in query or "add event" in query:
        title = query.replace("schedule", "").replace("add event", "").strip()
        event_time = datetime.now()
        return call_tool("create_event", title, event_time)

    elif "show events" in query:
        return call_tool("get_events")

    return "Calendar Agent: Unable to understand request"