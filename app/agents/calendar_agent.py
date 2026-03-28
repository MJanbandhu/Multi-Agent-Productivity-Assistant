from mcp.server import call_tool
from datetime import datetime

def handle_calendar(query):
    query = query.lower()

    # Create Event
    if "schedule" in query or "add event" in query:
        # simple parsing (can improve later)
        title = query.replace("schedule", "").replace("add event", "").strip()
        event_time = datetime.now()  # default (improve later)
        return call_tool("create_event", title, event_time)

    # Get Events
    elif "show events" in query:
        return call_tool("get_events")

    return "Calendar Agent: Unable to understand request"