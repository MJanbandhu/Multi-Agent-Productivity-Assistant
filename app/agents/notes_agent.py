from mcp.server import call_tool

def handle_notes(query):
    query = query.lower()

    # Add Note
    if "add note" in query or "save note" in query:
        content = query.replace("add note", "").replace("save note", "").strip()
        return call_tool("add_note", content)

    # Get Notes
    elif "show notes" in query:
        return call_tool("get_notes")

    return "Notes Agent: Unable to understand request"