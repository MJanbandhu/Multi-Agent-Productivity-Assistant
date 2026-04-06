from app.db.queries import execute_query
from datetime import datetime

def create_event(title):
    event_time = datetime.now()

    query = "INSERT INTO events (title, event_time) VALUES (%s, %s);"
    execute_query(query, (title, event_time))

    return "Event created successfully"

def get_events():
    query = "SELECT * FROM events;"
    return execute_query(query)