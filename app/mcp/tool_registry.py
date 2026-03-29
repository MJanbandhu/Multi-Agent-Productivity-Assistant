from app.tools.task_tool import create_task, get_tasks
from app.tools.notes_tool import create_note, get_notes
from app.tools.calendar_tool import create_event, get_events

TOOLS = {
    "create_task": create_task,
    "get_tasks": get_tasks,
    "create_note": create_note,
    "get_notes": get_notes,
    "create_event": create_event,
    "get_events": get_events,
}