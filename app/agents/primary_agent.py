from app.agents.task_agent import task_agent
from app.agents.calendar_agent import calendar_agent
from app.agents.notes_agent import notes_agent

def primary_agent(query):
    query = query.lower()
    
    responses = []
    parts = query.split(" and ")

    for part in parts:
        part = part.strip()

        if "task" in part:
            responses.append(task_agent(part))

        elif "schedule" in part or "event" in part:
            responses.append(calendar_agent(part))

        elif "note" in part:
            responses.append(notes_agent(part))

        else:
            responses.append(f"Unknown request: {part}")

    return responses