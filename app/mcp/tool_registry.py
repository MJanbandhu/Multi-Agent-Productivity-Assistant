from tools.task_tool import create_task, get_tasks
from tools.calendar_tool import create_event, get_events
from tools.notes_tool import add_note, get_notes

TOOLS = {
    "create_task": create_task,
    "get_tasks": get_tasks,
    "create_event": create_event,
    "get_events": get_events,
    "add_note": add_note,
    "get_notes": get_notes
}