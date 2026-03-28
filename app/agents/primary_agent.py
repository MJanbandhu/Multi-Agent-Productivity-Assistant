from agents.task_agent import handle_task
from agents.calendar_agent import handle_calendar
from agents.notes_agent import handle_notes

def primary_agent(query):
    query = query.lower()
    
    responses = []

    # Multi-step splitting (basic)
    parts = query.split(" and ")

    for part in parts:
        part = part.strip()

        # Route to Task Agent
        if "task" in part:
            responses.append(handle_task(part))

        # Route to Calendar Agent
        elif "schedule" in part or "event" in part:
            responses.append(handle_calendar(part))

        # Route to Notes Agent
        elif "note" in part:
            responses.append(handle_notes(part))

        else:
            responses.append(f"Unknown request: {part}")

    return responses