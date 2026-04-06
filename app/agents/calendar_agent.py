from app.mcp.server import call_tool

def calendar_agent(query):
    query = query.lower()

    # Create Event
    if "schedule" in query or "add event" in query:
        title = query.replace("schedule", "").replace("add event", "").strip()
        return call_tool("create_event", title)

    # Get Events
    elif "show events" in query:
        return call_tool("get_events")

    return {"error": "Calendar Agent: Unable to understand request"}